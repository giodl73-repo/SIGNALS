#!/usr/bin/env bash
# Signal — Flat binding install
# Skills installed as: /scout-competitors, /trace-contract, /draft-spec, etc.
# 68 atomic skills, direct invocation
# Default for all new installs.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BINDING="binding-flat"
TARGET="${1:-.claude/skills}"

# Resolve target relative to caller's working directory, not this script
if [[ "$TARGET" != /* ]]; then
    TARGET="$(pwd)/$TARGET"
fi

echo "Signal v0.1 — flat binding install"
echo "  source : $SIGNAL_ROOT/output/binding-flat/"
echo "  target : $TARGET"
echo ""

# Check if generated output exists
OUTPUT_DIR="$SIGNAL_ROOT/output/binding-flat"
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

# Count skills after copy
AFTER=$(find "$TARGET" -name "SKILL.md" 2>/dev/null | wc -l)
INSTALLED=$((AFTER - BEFORE + $(find "$OUTPUT_DIR" -name "SKILL.md" 2>/dev/null | wc -l)))

echo "Signal v0.1 installed: $INSTALLED skills -> $TARGET"
echo ""
echo "First commands to try:"
echo "  /scout-competitors <your-feature>   Scout inertia and named competitors"
echo "  /draft-spec <your-feature>          Write a spec from intent"
echo "  /topic-status <your-feature>        Check coverage and readiness"

echo ""
echo "Next: run /signal-setup to add Signal to your CLAUDE.md"
