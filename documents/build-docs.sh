#!/usr/bin/env bash
#
# build-docs.sh — regenerate the Word (.docx) versions of the client-facing documents.
#
# The Markdown files are the SOURCE OF TRUTH. The .docx files are generated
# copies for sharing with the client. Never edit the .docx by hand — your edit
# will be lost the next time this script runs.
#
# Run this whenever 01-Requirement-Understanding.md or 02-Open-Questions.md changes
# (it is step 6b of Rule 2 in 04-Skill-Update-Rules.md).
#
# Usage:
#   bash build-docs.sh          # rebuild both .docx
#   bash build-docs.sh --check  # fail if a .docx is older than its .md
#
# Requires: python3 and libreoffice (soffice). No other dependencies.

set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS=("00-MVP-and-Full-System-Scope" "01-Requirement-Understanding" "02-Open-Questions" "05-Client-Discussion-Module-Functionality")
MODE="${1:-build}"

if [ "$MODE" = "--check" ]; then
    STALE=0
    for d in "${DOCS[@]}"; do
        md="$HERE/$d.md"
        docx="$HERE/$d.docx"
        if [ ! -f "$docx" ]; then
            echo "MISSING  $d.docx — run: bash build-docs.sh"
            STALE=1
        elif [ "$md" -nt "$docx" ]; then
            echo "STALE    $d.docx is older than $d.md — run: bash build-docs.sh"
            STALE=1
        else
            echo "OK       $d.docx is up to date"
        fi
    done
    exit $STALE
fi

command -v soffice >/dev/null || { echo "ERROR: libreoffice (soffice) not found."; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

for d in "${DOCS[@]}"; do
    [ -f "$HERE/$d.md" ] || { echo "ERROR: $d.md not found."; exit 1; }
    python3 "$HERE/tools/md2html.py" "$HERE/$d.md" "$TMP/$d.html" || exit 1
done

soffice --headless --norestore \
    -env:UserInstallation="file://$TMP/lo-profile" \
    --convert-to 'docx:MS Word 2007 XML' \
    --outdir "$TMP/out" "$TMP"/*.html >/dev/null 2>&1

FAIL=0
BUILT=()
for d in "${DOCS[@]}"; do
    if [ -f "$TMP/out/$d.docx" ]; then
        mv "$TMP/out/$d.docx" "$HERE/$d.docx"
        BUILT+=("$HERE/$d.docx")
        SIZE=$(( $(stat -c%s "$HERE/$d.docx") / 1024 ))
        TABLES=$(python3 -c "
import zipfile,sys
x=zipfile.ZipFile('$HERE/$d.docx').read('word/document.xml').decode('utf-8')
print(x.count('<w:tbl>'))
" 2>/dev/null || echo '?')
        echo "built    $d.docx  (${SIZE} KB, ${TABLES} tables)"
    else
        echo "FAILED   $d.docx was not produced"
        FAIL=1
    fi
done

# LibreOffice ignores `table { width: 100% }` and sizes tables from their content,
# leaving them at roughly a third of the page. Force full width afterwards.
if [ ${#BUILT[@]} -gt 0 ]; then
    echo "widening tables:"
    python3 "$HERE/tools/fix-docx-tables.py" "${BUILT[@]}" || FAIL=1
fi

exit $FAIL
