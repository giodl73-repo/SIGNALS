#!/usr/bin/env bash
# Signal — Prefixed binding install
# Skills installed as: /signal-scout-competitors, /signal-trace-contract, /signal-draft-spec, etc.
# Use this binding in multi-plugin environments where /scout, /draft, or /trace
# collide with commands from another plugin in the same workspace.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-prefixed"
TARGET="${1:-.claude/skills}"

# Resolve target relative to caller's working directory
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

echo "Signal v0.1 — prefixed binding install"
echo "  source : $SIGNAL_ROOT/output/binding-prefixed/"
echo "  target : $TARGET"
echo ""

# Check if generated output exists
OUTPUT_DIR="$SIGNAL_ROOT/output/binding-prefixed"
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
echo "  /signal-scout-competitors <feature>  Scout inertia and named competitors"
echo "  /signal-trace-contract <feature>     Verify implementation matches spec"
echo "  /signal-topic-status <feature>       Check coverage and readiness"

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
