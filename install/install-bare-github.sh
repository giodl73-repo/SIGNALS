#!/usr/bin/env bash
# Signal — Bare binding install for GitHub Copilot
# Prompts installed as: decide.prompt.md, competitors.prompt.md, hypothesis.prompt.md, etc.
# 75 atomic prompt files in .github/prompts/
#
# Invocation differs from Claude Code:
#   Claude Code : /decide my-feature
#   GitHub Copilot: Open Copilot Chat, type @workspace, then select the prompt file
#                   or attach it via the paperclip > "Prompt" menu.
#
# Use when Signal is the only plugin and you want minimal typing.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-bare"
TARGET="${1:-.github/prompts}"

# Resolve target relative to caller's working directory, not this script
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

# Parent .github dir (one level up from prompts/)
GITHUB_DIR="$(dirname "$TARGET")"

echo "Signal v0.1 — bare binding install for GitHub Copilot"
echo "  source : $SIGNAL_ROOT/output/$BINDING/.github/"
echo "  target : $TARGET"
echo ""

# Check if generated output exists
OUTPUT_DIR="$SIGNAL_ROOT/output/$BINDING"
GITHUB_OUTPUT="$OUTPUT_DIR/.github"
if [[ ! -d "$GITHUB_OUTPUT" ]]; then
    echo "GitHub Copilot output not found. Generating from $BINDING.program.yaml ..."
    if ! command -v craft &>/dev/null; then
        echo "ERROR: craft CLI not found. Install craftworks or copy output/ from a pre-built release."
        echo "  https://github.com/your-org/craftworks"
        exit 1
    fi
    cd "$SIGNAL_ROOT"
    cp "bindings/$BINDING.program.yaml" program.yaml
    craft generate --stage program --target github-copilot
    echo ""
fi

# Create target directories
mkdir -p "$TARGET"
mkdir -p "$GITHUB_DIR"

# Count prompt files before copy
BEFORE=$(find "$TARGET" -name "*.prompt.md" 2>/dev/null | wc -l)

# Copy prompt files to .github/prompts/
if [[ -d "$GITHUB_OUTPUT/prompts" ]]; then
    cp -r "$GITHUB_OUTPUT/prompts/"* "$TARGET/"
fi

# Copy copilot-instructions.md to .github/ (not into prompts/)
if [[ -f "$GITHUB_OUTPUT/copilot-instructions.md" ]]; then
    cp "$GITHUB_OUTPUT/copilot-instructions.md" "$GITHUB_DIR/"
    echo "  copied : copilot-instructions.md -> $GITHUB_DIR/"
fi

# Count prompt files after copy
AFTER=$(find "$TARGET" -name "*.prompt.md" 2>/dev/null | wc -l)
INSTALLED=$((AFTER - BEFORE + $(find "$GITHUB_OUTPUT/prompts" -name "*.prompt.md" 2>/dev/null | wc -l)))

echo "Signal v0.1 (bare) installed for GitHub Copilot: $INSTALLED prompt files -> $TARGET"
echo ""
echo "First prompts to try:"
echo "  In Copilot Chat: @workspace then attach decide.prompt.md"
echo "    decide.prompt.md       Full pre-commitment decision campaign"
echo "    competitors.prompt.md  Scout inertia and named competitors"
echo "    hypothesis.prompt.md   Frame and falsify the core assumption"
echo ""
echo "Tip: In VS Code, open Copilot Chat (Ctrl+Shift+I), click the paperclip icon,"
echo "     choose 'Prompt...', and select any Signal prompt file."

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
