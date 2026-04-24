#!/usr/bin/env bash
# Signal — Grouped binding install for GitHub Copilot
# Prompts installed with namespace dispatchers: scout.prompt.md routes to sub-skills,
# plus all 68 atomic skill prompts (scout-competitors.prompt.md, etc.)
#
# Invocation differs from Claude Code:
#   Claude Code : /scout my-feature     (shows menu)
#   GitHub Copilot: Attach scout.prompt.md in Copilot Chat for a guided namespace menu,
#                   or attach scout-competitors.prompt.md to run a specific skill directly.
#
# Use for onboarding: teams describe intent and get routed to the right skill.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-grouped"
TARGET="${1:-.github/prompts}"

# Resolve target relative to caller's working directory, not this script
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

GITHUB_DIR="$(dirname "$TARGET")"

echo "Signal v0.1 — grouped binding install for GitHub Copilot"
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

# Copy copilot-instructions.md to .github/
if [[ -f "$GITHUB_OUTPUT/copilot-instructions.md" ]]; then
    cp "$GITHUB_OUTPUT/copilot-instructions.md" "$GITHUB_DIR/"
    echo "  copied : copilot-instructions.md -> $GITHUB_DIR/"
fi

# Count prompt files after copy
AFTER=$(find "$TARGET" -name "*.prompt.md" 2>/dev/null | wc -l)
INSTALLED=$((AFTER - BEFORE + $(find "$GITHUB_OUTPUT/prompts" -name "*.prompt.md" 2>/dev/null | wc -l)))

echo "Signal v0.1 installed for GitHub Copilot: $INSTALLED prompt files -> $TARGET"
echo ""
echo "First prompts to try:"
echo "  In Copilot Chat: @workspace then attach a prompt file"
echo "    scout.prompt.md               Namespace menu — pick from 8 scout skills"
echo "    scout-competitors.prompt.md   Run scout-competitors directly (also works)"
echo "    topic.prompt.md               See the topic namespace menu"
echo ""
echo "Tip: Namespace dispatch prompts (scout.prompt.md, draft.prompt.md, etc.) describe"
echo "     all skills in that namespace. Use them when you know the domain but not the"
echo "     exact skill. Atomic skill prompts run the skill directly."

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
