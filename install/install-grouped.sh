#!/usr/bin/env bash
# Signal — Grouped binding install
# Skills installed with namespace aggregators: /scout shows menu, /scout-competitors runs directly.
# All 68 atomic skills are present and directly invokable.
# Namespace aggregators route to the most contextually relevant sub-skill or show a menu.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-grouped"
TARGET="${1:-.claude/skills}"

# Resolve target relative to caller's working directory
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

echo "Signal v0.1 — grouped binding install"
echo "  source : $SIGNAL_ROOT/output/binding-grouped/"
echo "  target : $TARGET"
echo ""

# Check if generated output exists
OUTPUT_DIR="$SIGNAL_ROOT/output/binding-grouped"
if [[ ! -d "$OUTPUT_DIR" ]]; then
    echo "Output directory not found. Generating from $BINDING.program.yaml ..."
    if ! command -v craft &>/dev/null; then
        echo "ERROR: craft CLI not found. Install craftworks or copy output/ from a pre-built release."
        echo "  https://github.com/your-org/craftworks"
        exit 1
    fi
    cd "$SIGNAL_ROOT"
    cp "bindings/$BINDING.program.yaml" program.yaml
    craft generate --stage program
    echo ""
fi

# Create target directory
mkdir -p "$TARGET"

# Count skills before copy
BEFORE=$(find "$TARGET" -name "SKILL.md" 2>/dev/null | wc -l)

# Copy binding output
cp -r "$OUTPUT_DIR/"* "$TARGET/"

AFTER=$(find "$TARGET" -name "SKILL.md" 2>/dev/null | wc -l)
INSTALLED=$((AFTER - BEFORE + $(find "$OUTPUT_DIR" -name "SKILL.md" 2>/dev/null | wc -l)))

echo "Signal v0.1 installed: $INSTALLED skills -> $TARGET"
echo ""
echo "First commands to try:"
echo "  /scout <your-feature>              Type the namespace, get a menu of 8 scout skills"
echo "  /scout-competitors <your-feature>  Run a specific skill directly (still works)"
echo "  /topic <your-feature>              See the topic namespace menu"

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
