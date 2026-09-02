#!/usr/bin/env python3
"""Force every table in a .docx to full page width, and square up the margins.

Why this exists: LibreOffice's HTML importer ignores `table { width: 100% }` and
sizes tables from their content instead, which leaves them at roughly a third of
the page. It also writes asymmetric page margins. Both look wrong in a document
that goes to a client.

What it does, per table:
  * tblW       -> 100% (pct 5000), so the table fills the text column
  * gridCol    -> scaled so the columns sum to the available text width
  * tcW        -> converted to proportional percentages of the table
  * tblLayout  -> fixed, so the proportions are respected rather than recomputed
  * tblCellMar -> real cell padding (LibreOffice writes 28 twips, i.e. none, so
                  the text sits flat against the cell border)
  * tblHeader  -> set on the first row, so the header repeats when a long table
                  breaks across pages

Usage:  python3 fix-docx-tables.py <file.docx> [more.docx ...]
"""
import re
import shutil
import sys
import zipfile

DOC = 'word/document.xml'

# Symmetric page margins, in twips (1440 = 1 inch). 1134 = 2 cm.
MARGIN_LR = 1134
MARGIN_TB = 1134

# Cell padding, in twips. 113 = 0.2 cm across, 68 = 0.12 cm down.
CELL_PAD_LR = 113
CELL_PAD_TB = 68

# Brand navy for the header row, and a light grey for row separators.
HEADER_FILL = '192A4B'
RULE_COLOR = 'C8D0DC'


def rewrite_margins(xml):
    """Make left/right and top/bottom margins symmetric."""
    def repl(m):
        tag = m.group(0)
        tag = re.sub(r'w:left="\d+"', f'w:left="{MARGIN_LR}"', tag)
        tag = re.sub(r'w:right="\d+"', f'w:right="{MARGIN_LR}"', tag)
        tag = re.sub(r'w:top="\d+"', f'w:top="{MARGIN_TB}"', tag)
        tag = re.sub(r'w:bottom="\d+"', f'w:bottom="{MARGIN_TB}"', tag)
        return tag

    return re.sub(r'<w:pgMar[^/]*/>', repl, xml)


def available_width(xml):
    """Text-column width = page width minus the left and right margins."""
    page = re.search(r'<w:pgSz[^>]*w:w="(\d+)"', xml)
    page_w = int(page.group(1)) if page else 11906  # A4 default
    return page_w - (2 * MARGIN_LR)


def fix_table(block, avail):
    """Widen one <w:tbl> block to the full available width."""
    cols = [int(w) for w in re.findall(r'<w:gridCol w:w="(\d+)"', block)]
    if not cols:
        return block
    total = sum(cols) or 1

    # 1. Scale the grid so the columns fill the text column exactly.
    scaled = [max(1, round(c * avail / total)) for c in cols]
    scaled[-1] += avail - sum(scaled)          # absorb rounding drift

    grid_iter = iter(scaled)
    block = re.sub(r'<w:gridCol w:w="\d+"',
                   lambda m: f'<w:gridCol w:w="{next(grid_iter)}"',
                   block)

    # 2. Table width = 100% of the text column. pct is in fiftieths of a percent.
    if re.search(r'<w:tblW[^/]*/>', block):
        block = re.sub(r'<w:tblW[^/]*/>',
                       '<w:tblW w:w="5000" w:type="pct"/>', block, count=1)
    else:
        block = block.replace('<w:tblPr>',
                              '<w:tblPr><w:tblW w:w="5000" w:type="pct"/>', 1)

    # 3. Fixed layout, so our proportions are honoured, not recalculated.
    if re.search(r'<w:tblLayout[^/]*/>', block):
        block = re.sub(r'<w:tblLayout[^/]*/>',
                       '<w:tblLayout w:type="fixed"/>', block, count=1)
    else:
        block = block.replace('<w:tblW w:w="5000" w:type="pct"/>',
                              '<w:tblW w:w="5000" w:type="pct"/>'
                              '<w:tblLayout w:type="fixed"/>', 1)

    # 4. Cell widths as percentages of the table, matching the grid proportions.
    pcts = [max(1, round(c * 5000 / avail)) for c in scaled]
    pcts[-1] += 5000 - sum(pcts)

    ncols = len(pcts)
    counter = {'i': 0}

    def cell(m):
        p = pcts[counter['i'] % ncols]
        counter['i'] += 1
        return f'<w:tcW w:w="{p}" w:type="pct"/>'

    block = re.sub(r'<w:tcW[^/]*/>', cell, block)

    # 5. Real cell padding. LibreOffice writes 28 twips, which reads as none.
    pad = (f'<w:tblCellMar>'
           f'<w:top w:w="{CELL_PAD_TB}" w:type="dxa"/>'
           f'<w:left w:w="{CELL_PAD_LR}" w:type="dxa"/>'
           f'<w:bottom w:w="{CELL_PAD_TB}" w:type="dxa"/>'
           f'<w:right w:w="{CELL_PAD_LR}" w:type="dxa"/>'
           f'</w:tblCellMar>')
    if '<w:tblCellMar>' in block:
        block = re.sub(r'<w:tblCellMar>.*?</w:tblCellMar>', pad, block,
                       count=1, flags=re.S)
    else:
        block = block.replace('</w:tblPr>', pad + '</w:tblPr>', 1)

    # 5b. Row separators. LibreOffice writes empty <w:tcBorders></w:tcBorders>,
    #     which suppresses every line, so drop those and set table-level borders:
    #     a rule above and below, thin lines between rows, no vertical lines.
    block = block.replace('<w:tcBorders></w:tcBorders>', '')
    borders = (f'<w:tblBorders>'
               f'<w:top w:val="single" w:sz="8" w:space="0" w:color="{HEADER_FILL}"/>'
               f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="{HEADER_FILL}"/>'
               f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
               f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
               f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{RULE_COLOR}"/>'
               f'<w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
               f'</w:tblBorders>')
    if '<w:tblBorders>' in block:
        block = re.sub(r'<w:tblBorders>.*?</w:tblBorders>', borders, block,
                       count=1, flags=re.S)
    else:
        block = block.replace('<w:tblLayout w:type="fixed"/>',
                              '<w:tblLayout w:type="fixed"/>' + borders, 1)

    # 6. First row: repeat it across page breaks, and move the header fill from
    #    the paragraph to the cell, so the navy runs edge to edge with no gaps
    #    at the cell padding.
    rows = list(re.finditer(r'<w:tr\b[^>]*>.*?</w:tr>', block, re.S))
    if rows:
        head = rows[0].group(0)
        new = head

        if '<w:trPr>' in new:
            new = re.sub(r'<w:trPr>(.*?)</w:trPr>',
                         lambda m: f'<w:trPr><w:tblHeader/>{m.group(1)}</w:trPr>',
                         new, count=1, flags=re.S)
        else:
            new = re.sub(r'(<w:tr\b[^>]*>)',
                         r'\1<w:trPr><w:tblHeader/></w:trPr>', new, count=1)

        shd = (f'<w:shd w:val="clear" w:color="auto" w:fill="{HEADER_FILL}"/>')

        def shade_cell(m):
            tcpr = m.group(0)
            if '<w:shd' in tcpr:
                return re.sub(r'<w:shd[^/]*/>', shd, tcpr, count=1)
            return tcpr.replace('<w:tcPr>', '<w:tcPr>' + shd, 1)

        new = re.sub(r'<w:tcPr>.*?</w:tcPr>', shade_cell, new, flags=re.S)
        block = block[:rows[0].start()] + new + block[rows[0].end():]

    return block


def process(path):
    xml = zipfile.ZipFile(path).read(DOC).decode('utf-8')

    n_tables = xml.count('<w:tbl>')
    xml = rewrite_margins(xml)
    avail = available_width(xml)

    xml = re.sub(r'<w:tbl>.*?</w:tbl>',
                 lambda m: fix_table(m.group(0), avail),
                 xml, flags=re.S)

    # Rewrite the archive, replacing only document.xml.
    src = zipfile.ZipFile(path)
    tmp = path + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as out:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == DOC:
                data = xml.encode('utf-8')
            out.writestr(item, data)
    src.close()
    shutil.move(tmp, path)

    print(f'  {path.split("/")[-1]}: {n_tables} table(s) set to full width '
          f'({avail} twips)')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('usage: fix-docx-tables.py <file.docx> [...]')
    for p in sys.argv[1:]:
        process(p)
