#!/usr/bin/env bash
# Signal simlab bootstrap
# Creates a simlab workspace peer to your current directory, or at a path you specify.
#
# Usage:
#   bash bootstrap.sh                        # creates ../simlab
#   bash bootstrap.sh my-simlab             # creates ../my-simlab
#   bash bootstrap.sh /path/to/my-simlab    # creates at absolute path
#
# Via curl:
#   curl -s https://raw.githubusercontent.com/gim-home/craftworks-research/main/toolkits/simlab/bootstrap.sh | bash
#   curl -s ...bootstrap.sh | bash -s my-simlab
#   curl -s ...bootstrap.sh | bash -s /path/to/my-simlab

set -euo pipefail

ARG="${1:-}"

if [[ "$ARG" == /* ]]; then
  # Absolute path provided
  DEST="$ARG"
elif [[ -n "$ARG" ]]; then
  # Name provided — place as peer
  DEST="$(cd "$(pwd)/.." && pwd)/$ARG"
else
  # Default — peer named simlab
  DEST="$(cd "$(pwd)/.." && pwd)/simlab"
fi
REPO_URL="https://github.com/gim-home/craftworks-research"
SPARSE_PATH="toolkits/simlab"
TMP=$(mktemp -d)

echo ""
echo "Signal simlab bootstrap"
echo "  destination : $DEST"
echo ""

# Check destination
if [[ -d "$DEST" ]]; then
  echo "ERROR: $DEST already exists. Remove it or pass a different name:"
  echo "  bash bootstrap.sh my-simlab"
  exit 1
fi

# Sparse clone just toolkits/simlab
echo "Fetching simlab from craftworks-research..."
git clone --filter=blob:none --sparse --quiet "$REPO_URL" "$TMP/craftworks-research"
cd "$TMP/craftworks-research"
git sparse-checkout set "$SPARSE_PATH" --quiet

# Copy to destination
cp -r "$SPARSE_PATH" "$DEST"

# Cleanup
rm -rf "$TMP"

echo "Done."
echo ""
echo "  $DEST"
echo "  ├── .claude/skills/     68 Signal skills (Claude Code)"
echo "  ├── .github/prompts/    GitHub Copilot prompts"
echo "  ├── signals/            artifact output"
echo "  ├── CLAUDE.md           pre-wired"
echo "  └── CONTEXT.md          fill this in"
echo ""

# Optionally init as a git repo
read -r -p "Initialize as a git repo? (y/N) " GIT_INIT
if [[ "${GIT_INIT,,}" == "y" ]]; then
  cd "$DEST"
  git init --quiet
  git add .
  git commit -m "Initial simlab workspace" --quiet
  echo "Git repo initialized."
  echo ""
fi

echo "Next: open simlab in Claude Code and run /signal-setup"
