#!/usr/bin/env bash
# Signal — GitHub Copilot install
# Installs .prompt.md files to .github/prompts/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET="${1:-.github/prompts}"
[[ "$TARGET" != /* ]] && TARGET="$(pwd)/$TARGET"

SOURCE_DIR="$SIGNAL_ROOT/sim-test/.github/prompts"
[[ ! -d "$SOURCE_DIR" ]] && echo "ERROR: $SOURCE_DIR not found" && exit 1

mkdir -p "$TARGET"
COUNT=$(ls "$SOURCE_DIR"/*.prompt.md 2>/dev/null | wc -l)
cp "$SOURCE_DIR"/*.prompt.md "$TARGET/"

echo "Signal v1.0 — GitHub Copilot"
echo "Installed: $COUNT prompt files -> $TARGET"
echo ""
echo "Usage: attach a prompt via Copilot Chat > paperclip > Prompt"
echo "Note: use --compact flag for complex skills if Copilot crashes"
