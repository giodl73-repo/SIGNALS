#!/usr/bin/env bash
# Signal — Bare binding install
# Commands: /competitors, /spec, /design, /lifecycle, /status, etc.
# Shortest possible command names.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET="${1:-.claude/skills}"
[[ "$TARGET" != /* ]] && TARGET="$(pwd)/$TARGET"

echo "Signal v1.0 — bare binding (shortest names)"

PREFIXES=(discover- specify- validate- simulate- rhythm- roles- signal- tools-)

SOURCE_DIR="$SIGNAL_ROOT/sim-test/.claude/skills"
[[ ! -d "$SOURCE_DIR" ]] && echo "ERROR: $SOURCE_DIR not found" && exit 1

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
    [[ ! -f "$src/SKILL.md" ]] && continue

    bare_name="$skill"
    for prefix in "${PREFIXES[@]}"; do
        if [[ "$skill" == ${prefix}* ]]; then
            bare_name="${skill#$prefix}"
            break
        fi
    done

    mkdir -p "$TARGET/$bare_name"
    sed "s/^name: .*/name: $bare_name/" "$src/SKILL.md" > "$TARGET/$bare_name/SKILL.md"
    [[ -f "$src/SKILL.t3.md" ]] && cp "$src/SKILL.t3.md" "$TARGET/$bare_name/SKILL.t3.md"
    INSTALLED=$((INSTALLED + 1))
done

echo "Installed: $INSTALLED skills -> $TARGET"
echo ""

CLAUDE_MD="$(pwd)/CLAUDE.md"
if ! grep -q "Signal is installed" "$CLAUDE_MD" 2>/dev/null; then
    cat >> "$CLAUDE_MD" << 'CLAUDE_BLOCK'

## Signal

Signal is installed. 62 skills across 9 namespaces (bare binding — shortest commands).

Quick start:
  /competitors <feature>   Scout inertia and named competitors
  /inertia <feature>       Why would teams do nothing instead?
  /status <feature>        Current signal coverage
  /decide <feature>        Full pre-commitment decision campaign

Artifacts: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
The primary competitor is always inertia.
CLAUDE_BLOCK
    echo "Added Signal context to CLAUDE.md"
fi
