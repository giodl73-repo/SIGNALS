#!/usr/bin/env bash
# Signal — Grouped binding install
# Commands: /discover (menu), /discover-competitors (direct), etc.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$SCRIPT_DIR/install-flat.sh" "$@"

TARGET="${1:-.claude/skills}"
[[ "$TARGET" != /* ]] && TARGET="$(pwd)/$TARGET"

for ns in discover specify validate simulate rhythm roles tools; do
    mkdir -p "$TARGET/$ns"
    cat > "$TARGET/$ns/SKILL.md" << MENU
---
name: $ns
description: "${ns^} namespace — shows available subcommands. Or run /$ns-<subcommand> directly."
allowed-tools: [Read, Glob]
param_set: lean
---
Run /$ns <subcommand> <topic> or use direct commands like /$ns-competitors <topic>.

Available /$ns subcommands:
\$(ls .claude/skills/ 2>/dev/null | grep "^$ns-" | sed 's/^/  \//')
MENU
done

echo "Added namespace menus: /discover, /specify, /validate, /simulate, /rhythm, /roles, /tools"
