#!/usr/bin/env bash
#
# install-global.sh — install the saas-flipper skill into your personal Claude Code
# skills directory (~/.claude/skills/) so it's available in EVERY project, including
# in the Claude Code desktop app.
#
# Usage:  bash install-global.sh
#
# Idempotent: re-run any time to update the installed copy to the latest version.

set -euo pipefail

# Resolve the repo root (the directory this script lives in).
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$SRC_DIR/.claude/skills/saas-flipper"

SKILLS_DIR="$HOME/.claude/skills"
SKILL_DEST="$SKILLS_DIR/saas-flipper"

if [ ! -f "$SKILL_SRC/SKILL.md" ]; then
  echo "Error: could not find the skill at $SKILL_SRC" >&2
  echo "Run this script from the root of the SaaS-Flipper repo." >&2
  exit 1
fi

# Track whether the top-level skills dir already existed — a brand-new one needs an app restart.
SKILLS_DIR_EXISTED=true
if [ ! -d "$SKILLS_DIR" ]; then
  SKILLS_DIR_EXISTED=false
fi

mkdir -p "$SKILLS_DIR"
rm -rf "$SKILL_DEST"
cp -r "$SKILL_SRC" "$SKILL_DEST"

echo "✅ Installed saas-flipper skill to: $SKILL_DEST"
echo

if [ "$SKILLS_DIR_EXISTED" = false ]; then
  echo "⚠️  ~/.claude/skills/ was just created."
  echo "    Fully QUIT and REOPEN the Claude Code desktop app so it picks up the new skills folder."
  echo
fi

echo "Then type  /saas-flipper  (one word, hyphen — not a space) in any project."
