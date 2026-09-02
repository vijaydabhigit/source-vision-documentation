#!/usr/bin/env bash
#
# check-sources.sh — detect when client source files change.
#
# Why this exists:
#   01-Requirement-Understanding.md and the two skills in
#   skills/ are derived from client files. If a client file changes and
#   nobody updates them, we build from stale requirements. This script makes
#   that drift impossible to miss.
#
# Usage:
#   bash check-sources.sh            # check, report drift
#   bash check-sources.sh --update   # accept current state as new baseline
#   bash check-sources.sh --list     # list every tracked file + hash
#
# Exit codes:  0 = no drift   1 = drift found   2 = no baseline yet   3 = source folder missing
#
# Override the watched folder with:  SV_DOC_ROOT=/path bash check-sources.sh

set -uo pipefail

# Client documents moved here on 12 Aug 2026 (previously
# /var/www/html/source-vision-test/Documentation).
ROOT="${SV_DOC_ROOT:-/home/nls157/Documents/Projects/Source Vision}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASELINE="$HERE/sources.sha256"
MODE="${1:-check}"

if [ ! -d "$ROOT" ]; then
    echo "MISSING SOURCE FOLDER"
    echo "  Expected client documents at: $ROOT"
    echo "  Set SV_DOC_ROOT if they live somewhere else."
    exit 3
fi

# Snapshot: "<sha256>  <relative path>", sorted by path so output is stable.
snapshot() {
    (cd "$ROOT" && find . -type f ! -name '.DS_Store' -exec sha256sum {} + 2>/dev/null) \
        | sed 's|  \./|  |' | LC_ALL=C sort -k2
}

CURRENT="$(snapshot)"

if [ "$MODE" = "--list" ]; then
    echo "$CURRENT"
    echo "---"
    echo "$(echo "$CURRENT" | wc -l) file(s) tracked under $ROOT"
    exit 0
fi

if [ "$MODE" = "--update" ]; then
    {
        echo "# Source fingerprints for Source Vision client documents."
        echo "# Folder: $ROOT"
        echo "# Updated: $(date '+%Y-%m-%d %H:%M:%S %Z')"
        echo "# Regenerate with: bash check-sources.sh --update"
        echo "$CURRENT"
    } > "$BASELINE"
    echo "OK — baseline updated with $(echo "$CURRENT" | wc -l) file(s)."
    echo "Now record what changed in 03-Change-Log.md"
    exit 0
fi

if [ ! -f "$BASELINE" ]; then
    echo "NO BASELINE"
    echo "  Run: bash check-sources.sh --update"
    exit 2
fi

BASE_BODY="$(grep -v '^#' "$BASELINE" | grep -v '^[[:space:]]*$')"

DRIFT="$(
    BASE="$BASE_BODY" CUR="$CURRENT" python3 - <<'PY'
import os

def parse(blob):
    out = {}
    for line in blob.splitlines():
        line = line.rstrip("\n")
        if not line.strip():
            continue
        sha, _, path = line.partition("  ")
        if path:
            out[path] = sha
    return out

base = parse(os.environ["BASE"])
cur = parse(os.environ["CUR"])

changed = sorted(p for p in cur.keys() & base.keys() if cur[p] != base[p])
new = sorted(cur.keys() - base.keys())
missing = sorted(base.keys() - cur.keys())

for p in changed:
    print(f"CHANGED  {p}")
for p in new:
    print(f"NEW      {p}")
for p in missing:
    print(f"MISSING  {p}")
PY
)"

if [ -z "$DRIFT" ]; then
    echo "OK — all $(echo "$CURRENT" | wc -l) client source file(s) match the baseline."
    echo "Documentation and skills are in sync. Safe to continue."
    exit 0
fi

echo "DRIFT DETECTED — client source files no longer match our documentation."
echo
echo "$DRIFT"
echo
echo "Required action (see 04-Skill-Update-Rules.md):"
echo "  1. Read the changed / new file."
echo "  2. Update 01-Requirement-Understanding.md."
echo "  3. Update ../skills/source-vision-design/SKILL.md if design changed."
echo "  4. Update ../skills/source-vision-functionality/SKILL.md if behaviour changed."
echo "  5. Add a row to 03-Change-Log.md."
echo "  6. Run: bash check-sources.sh --update"
exit 1
