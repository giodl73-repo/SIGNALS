#!/usr/bin/env bash
# Signal — Domains binding install for GitHub Copilot
# Adds 6 cross-namespace workflow prompt files plus all 68 atomic skill prompts.
#
# Domain prompts installed:
#   decide.prompt.md    Decision brief: market + viability + evidence + recommendation
#   simulate.prompt.md  Simulation report: lifecycle + conversation + state + contract + permissions
#   validate.prompt.md  Validation brief: expert findings + usability scores + NPS forecast
#   specify.prompt.md   Spec package: technical spec + decision record + pitch
#   evidence.prompt.md  Full evidence dossier: hypothesis -> websearch -> intelligence -> synthesize
#   track.prompt.md     Topic dashboard: coverage + narrative + readiness statement
#
# Invocation differs from Claude Code:
#   Claude Code : /decide my-feature
#   GitHub Copilot: In Copilot Chat, attach decide.prompt.md
#
# Use when teams think in outcomes rather than skill names.
# Good for PMs and execs running sprint kickoffs.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-domains"
TARGET="${1:-.github/prompts}"

# Resolve target relative to caller's working directory, not this script
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

GITHUB_DIR="$(dirname "$TARGET")"

echo "Signal v0.1 — domains binding install for GitHub Copilot"
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
echo "    decide.prompt.md    Full decision brief: is this worth building?"
echo "    validate.prompt.md  Full validation brief: will users adopt this?"
echo "    track.prompt.md     Topic dashboard: what signals exist, what is missing"
echo ""
echo "Tip: Domain prompts compose multiple Signal skills into a single workflow."
echo "     Use them for sprint kickoffs or exec reviews. Atomic skill prompts"
echo "     (scout-competitors.prompt.md, etc.) are also installed for direct runs."

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
