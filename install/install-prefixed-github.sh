#!/usr/bin/env bash
# Signal — Prefixed binding install for GitHub Copilot
# Prompts installed as: signal-scout-competitors.prompt.md, signal-trace-contract.prompt.md, etc.
# Use this binding in repos where other Copilot prompt files already use names like
# scout.prompt.md, draft.prompt.md, or trace.prompt.md.
#
# Invocation differs from Claude Code:
#   Claude Code : /signal-scout-competitors my-feature
#   GitHub Copilot: In Copilot Chat, attach signal-scout-competitors.prompt.md
#                   (the signal- prefix is visible in the prompt picker, preventing collisions)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-prefixed"
TARGET="${1:-.github/prompts}"

# Resolve target relative to caller's working directory, not this script
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

GITHUB_DIR="$(dirname "$TARGET")"

echo "Signal v0.1 — prefixed binding install for GitHub Copilot"
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
echo "    signal-scout-competitors.prompt.md   Scout inertia and named competitors"
echo "    signal-trace-contract.prompt.md      Verify implementation matches spec"
echo "    signal-topic-status.prompt.md        Check coverage and readiness"
echo ""
echo "Tip: All prompt files are prefixed with signal- so they sort together in the"
echo "     prompt picker and never collide with your repo's existing prompt files."

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
