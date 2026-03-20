#!/usr/bin/env bash
# Signal — Flat binding install
# Commands: /discover-competitors, /specify-spec, /validate-design, etc.
# 62 skills across 9 namespaces.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET="${1:-.claude/skills}"
[[ "$TARGET" != /* ]] && TARGET="$(pwd)/$TARGET"

echo "Signal v1.0 — flat binding"
echo "  source : $SIGNAL_ROOT/sim-test/.claude/skills/"
echo "  target : $TARGET"
echo ""

SOURCE_DIR="$SIGNAL_ROOT/sim-test/.claude/skills"
[[ ! -d "$SOURCE_DIR" ]] && echo "ERROR: $SOURCE_DIR not found" && exit 1

# Canonical 62 skills (discover-*, specify-*, validate-*, simulate-*, rhythm-*, roles-*, signal*, tools-*, achievements)
CANONICAL=(
  achievements
  discover-analysis discover-brainstorm discover-causal discover-coherence discover-compare
  discover-competitors discover-competitors-alt discover-feasibility discover-feasibility-alt
  discover-hypothesis discover-inertia discover-orchestrate discover-risk discover-synthesize
  discover-websearch
  rhythm-achievements rhythm-behavior rhythm-brief rhythm-decide rhythm-qa rhythm-status rhythm-story
  roles-build roles-chart roles-check roles-committee roles-create roles-generate
  roles-leaderboard roles-product-review roles-pull-request roles-scan
  signal signal-health signal-layout signal-setup
  simulate-contract simulate-conversation simulate-lifecycle simulate-permissions
  simulate-request simulate-state simulate-stress
  specify-commitment specify-pitch specify-proposal specify-spec
  tools-accept tools-coverage tools-preview
  validate-adoption validate-adoption-blocker validate-code validate-customers
  validate-design validate-feedback validate-support validate-users
)

mkdir -p "$TARGET"
INSTALLED=0

for skill in "${CANONICAL[@]}"; do
    src="$SOURCE_DIR/$skill"
    [[ ! -f "$src/SKILL.md" ]] && echo "  MISSING: $skill" && continue
    mkdir -p "$TARGET/$skill"
    cp "$src/SKILL.md" "$TARGET/$skill/SKILL.md"
    [[ -f "$src/SKILL.t3.md" ]] && cp "$src/SKILL.t3.md" "$TARGET/$skill/SKILL.t3.md"
    INSTALLED=$((INSTALLED + 1))
done

echo "Installed: $INSTALLED skills -> $TARGET"
echo ""

# Update CLAUDE.md
CLAUDE_MD="$(pwd)/CLAUDE.md"
if grep -q "Signal is installed" "$CLAUDE_MD" 2>/dev/null; then
    echo "Signal already in CLAUDE.md — skipping"
else
    cat >> "$CLAUDE_MD" << 'CLAUDE_BLOCK'

## Signal

Signal is installed. 62 skills across 9 namespaces.

Quick start:
  /discover-competitors <feature>   Scout inertia and named competitors
  /discover-inertia <feature>       Why would teams do nothing instead?
  /signal                           See all 62 commands
  /rhythm-decide <feature>          Full pre-commitment decision campaign

Artifacts: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Use /tools-coverage <feature> to see coverage gaps.
Use /signal-health to check workspace health.

The primary competitor is always inertia.
CLAUDE_BLOCK
    echo "Added Signal context to CLAUDE.md"
fi
