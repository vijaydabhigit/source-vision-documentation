#!/usr/bin/env bash
#
# session-start-check.sh — SessionStart hook wrapper around check-sources.sh.
#
# Wired into .claude/settings.json so it runs automatically at the start of every
# Claude Code session. Purpose: nobody has to remember to check whether the
# client's source documents changed.
#
# Behaviour:
#   sources in sync  -> silent, exit 0 (no noise at session start)
#   sources changed  -> prints JSON with a systemMessage for the user and
#                       additionalContext for Claude, then exits 0
#
# Always exits 0. This hook reports; it never blocks a session.

set -uo pipefail

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)" || exit 0
[ -f check-sources.sh ] || exit 0

OUT="$(bash check-sources.sh 2>&1)"
ST=$?

# Secondary check: are the client-facing .docx copies older than their .md source?
DOCX_OUT=""
if [ -f build-docs.sh ]; then
    if ! DOCX_RAW="$(bash build-docs.sh --check 2>&1)"; then
        DOCX_OUT="$(printf '%s\n' "$DOCX_RAW" | grep -E '^(STALE|MISSING)' || true)"
    fi
fi

# check-sources exit 0 = in sync. Exit 3 = source folder unreachable (e.g. working
# off-site) — not a requirement change, so stay quiet rather than nag every session.
SOURCES_OK=0
if [ "$ST" -eq 0 ] || [ "$ST" -eq 3 ]; then
    SOURCES_OK=1
fi

# Nothing wrong at all -> stay silent.
if [ "$SOURCES_OK" -eq 1 ] && [ -z "$DOCX_OUT" ]; then
    exit 0
fi

# Only the Word copies are stale -> small, specific nudge.
if [ "$SOURCES_OK" -eq 1 ] && [ -n "$DOCX_OUT" ]; then
    jq -nc --arg o "$DOCX_OUT" \
        '{systemMessage: ("Source Vision: the Word (.docx) copies are out of date.\nRun: bash build-docs.sh\n\n" + $o),
          hookSpecificOutput: {hookEventName: "SessionStart",
            additionalContext: ("The generated .docx copies of the Source Vision documents are older than their .md sources. Run `bash build-docs.sh` to regenerate them. The .md files are the source of truth; never edit the .docx by hand.\n\n" + $o)}}'
    exit 0
fi

# Sources drifted (possibly plus stale .docx) -> full update instructions.
if [ -n "$DOCX_OUT" ]; then
    OUT="${OUT}

${DOCX_OUT}"
fi

USER_MSG="Source Vision: the client's source documents have CHANGED.
Update the documentation and skills BEFORE writing code — see 04-Skill-Update-Rules.md

${OUT}"

CLAUDE_MSG="check-sources.sh reported that the Source Vision client source documents no longer match our documentation baseline.

Before doing ANY Source Vision work, follow 04-Skill-Update-Rules.md Rule 2, in this order:
  1. Read the changed / new client file
  2. Update 01-Requirement-Understanding.md
  3. Update 02-Open-Questions.md if new conflicts appear
  4. Update ../skills/source-vision-design/SKILL.md if design rules changed
  5. Update ../skills/source-vision-functionality/SKILL.md if behaviour or scope changed
  6. Add a row to 03-Change-Log.md
  7. Run: bash build-docs.sh          (regenerate the client .docx copies)
  8. Run: bash check-sources.sh --update

${OUT}"

jq -nc \
    --arg user "$USER_MSG" \
    --arg claude "$CLAUDE_MSG" \
    '{
        systemMessage: $user,
        hookSpecificOutput: {
            hookEventName: "SessionStart",
            additionalContext: $claude
        }
    }'

exit 0
