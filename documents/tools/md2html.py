#!/usr/bin/env python3
"""Markdown -> styled HTML, for LibreOffice to convert into .docx.

Covers exactly what the Source Vision docs use: headings, pipe tables,
bullet/numbered/checkbox lists, fenced code, blockquotes, rules, and inline
bold / italic / code / links. No external dependencies.
"""
import html
import re
import sys

NAVY = '#192A4B'
BLUE = '#001FFA'
ORANGE = '#FD5104'

CSS = f"""
body {{ font-family: 'Space Grotesk','Segoe UI',Arial,sans-serif; font-size: 10.5pt;
        color: #1a1a1a; line-height: 1.45; }}
h1 {{ font-size: 22pt; color: {NAVY}; font-weight: 700; margin: 0 0 4pt 0; }}
h2 {{ font-size: 15pt; color: {NAVY}; font-weight: 700;
      margin: 20pt 0 6pt 0; border-bottom: 1.5pt solid {BLUE}; padding-bottom: 3pt; }}
h3 {{ font-size: 12.5pt; color: {NAVY}; font-weight: 700; margin: 14pt 0 4pt 0; }}
h4 {{ font-size: 11pt; color: {BLUE}; font-weight: 700; margin: 11pt 0 3pt 0; }}
h5, h6 {{ font-size: 10.5pt; color: {NAVY}; font-weight: 700; margin: 9pt 0 3pt 0; }}
p {{ margin: 0 0 6pt 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 6pt 0 10pt 0; }}
th {{ background-color: {NAVY}; color: #ffffff; font-weight: 700; font-size: 9.5pt;
      border: 0.5pt solid {NAVY}; padding: 4pt 5pt; text-align: left; }}
td {{ border: 0.5pt solid #b8c0cc; padding: 4pt 5pt; font-size: 9.5pt;
      vertical-align: top; }}
code {{ font-family: 'Consolas','Courier New',monospace; font-size: 9pt;
        background-color: #eef0f4; color: {NAVY}; }}
pre {{ font-family: 'Consolas','Courier New',monospace; font-size: 9pt;
       background-color: #f4f6f9; border-left: 3pt solid {BLUE};
       padding: 6pt 8pt; margin: 6pt 0 10pt 0; }}
blockquote {{ border-left: 3pt solid {ORANGE}; background-color: #fff6f2;
              padding: 6pt 10pt; margin: 6pt 0 10pt 0; }}
ul, ol {{ margin: 0 0 8pt 0; padding-left: 20pt; }}
li {{ margin: 0 0 2pt 0; }}
hr {{ border: none; border-top: 0.75pt solid #c4ccd8; margin: 14pt 0; }}
a {{ color: {BLUE}; }}
.subtitle {{ font-size: 11pt; color: #55607a; margin: 0 0 14pt 0; }}
"""


def inline(text):
    """Inline markdown -> HTML. Code spans are protected from other rules."""
    spans = []

    def stash(m):
        spans.append(m.group(1))
        return f'\x00{len(spans) - 1}\x00'

    text = re.sub(r'`([^`]+)`', stash, text)
    text = html.escape(text, quote=False)

    # [label](target): keep real URLs as links, render internal .md links as text
    def link(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(('http://', 'https://', 'mailto:')):
            return f'<a href="{html.escape(target, quote=True)}">{label}</a>'
        return f'<b>{label}</b>'

    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<i>\1</i>', text)
    text = re.sub(r'~~([^~]+)~~', r'<s>\1</s>', text)

    for i, raw in enumerate(spans):
        text = text.replace(f'\x00{i}\x00',
                            f'<code>{html.escape(raw, quote=False)}</code>')
    return text


def is_table_sep(line):
    return bool(re.fullmatch(r'\s*\|?[\s:|-]+\|[\s:|-]*', line)) and '-' in line


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


def convert(md):
    lines = md.split('\n')
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # HTML comment block -> drop
        if line.lstrip().startswith('<!--'):
            while i < n and '-->' not in lines[i]:
                i += 1
            i += 1
            continue

        # fenced code
        if line.lstrip().startswith('```'):
            i += 1
            buf = []
            while i < n and not lines[i].lstrip().startswith('```'):
                buf.append(html.escape(lines[i], quote=False))
                i += 1
            i += 1
            out.append('<pre>' + '\n'.join(buf) + '</pre>')
            continue

        # table
        if '|' in line and i + 1 < n and is_table_sep(lines[i + 1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < n and '|' in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            width = max([len(header)] + [len(r) for r in rows]) if rows else len(header)
            t = ['<table>', '<tr>']
            for c in header + [''] * (width - len(header)):
                t.append(f'<th>{inline(c)}</th>')
            t.append('</tr>')
            for r in rows:
                t.append('<tr>')
                for c in r + [''] * (width - len(r)):
                    t.append(f'<td>{inline(c)}</td>')
                t.append('</tr>')
            t.append('</table>')
            out.append(''.join(t))
            continue

        # heading
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline(m.group(2).strip())}</h{lvl}>')
            i += 1
            continue

        # horizontal rule
        if re.fullmatch(r'\s*([-*_])\1{2,}\s*', line):
            out.append('<hr/>')
            i += 1
            continue

        # blockquote
        if line.lstrip().startswith('>'):
            buf = []
            while i < n and lines[i].lstrip().startswith('>'):
                buf.append(re.sub(r'^\s*>\s?', '', lines[i]))
                i += 1
            inner = '<br/>'.join(inline(b) for b in buf if b.strip())
            out.append(f'<blockquote>{inner}</blockquote>')
            continue

        # lists (bullet, checkbox, numbered)
        if re.match(r'^\s*([-*+]|\d+\.)\s+', line):
            ordered = bool(re.match(r'^\s*\d+\.\s+', line))
            tag = 'ol' if ordered else 'ul'
            items = []
            while i < n and re.match(r'^\s*([-*+]|\d+\.)\s+', lines[i]):
                item = re.sub(r'^\s*([-*+]|\d+\.)\s+', '', lines[i])
                item = re.sub(r'^\[([ xX])\]\s*', lambda m:
                              '&#9746; ' if m.group(1).lower() == 'x' else '&#9744; ',
                              item)
                items.append(f'<li>{inline(item)}</li>')
                i += 1
            out.append(f'<{tag}>' + ''.join(items) + f'</{tag}>')
            continue

        # blank
        if not line.strip():
            i += 1
            continue

        # paragraph
        buf = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(
                r'^(#{1,6}\s|\s*([-*+]|\d+\.)\s|>|```|\s*([-*_])\3{2,}\s*$)', lines[i]) \
                and not ('|' in lines[i] and i + 1 < n and is_table_sep(lines[i + 1])):
            buf.append(lines[i])
            i += 1
        out.append('<p>' + inline(' '.join(b.strip() for b in buf)) + '</p>')

    return '\n'.join(out)


if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding='utf-8') as f:
        md = f.read()
    body = convert(md)
    title = re.search(r'^#\s+(.*)$', md, re.M)
    title = title.group(1).strip() if title else 'Source Vision'
    doc = (f'<!DOCTYPE html><html><head><meta charset="utf-8">'
           f'<title>{html.escape(title, quote=False)}</title>'
           f'<style type="text/css">{CSS}</style></head><body>{body}</body></html>')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(doc)
    print(f'{src} -> {dst} ({len(doc) // 1024} KB html)')
