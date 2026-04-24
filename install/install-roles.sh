#!/usr/bin/env bash
# Signal — Domain roles install
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SIGNAL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DOMAIN="all"
TARGET="${2:-.roles}"
[[ "$TARGET" != /* ]] && TARGET="$(pwd)/$TARGET"

while [[ $# -gt 0 ]]; do
    case $1 in --domain) DOMAIN="$2"; shift 2 ;; *) shift ;; esac
done

SOURCE_DIR="$SIGNAL_ROOT/.roles"
[[ ! -d "$SOURCE_DIR" ]] && echo "ERROR: $SOURCE_DIR not found" && exit 1

install_domain() {
    local d="$1"
    [[ ! -d "$SOURCE_DIR/$d" ]] && echo "  $d: not found" && return
    mkdir -p "$TARGET/$d"
    cp "$SOURCE_DIR/$d"/*.md "$TARGET/$d/" 2>/dev/null || true
    echo "  $d: $(ls "$SOURCE_DIR/$d"/*.md 2>/dev/null | wc -l) roles"
}

echo "Signal v1.0 — domain roles ($DOMAIN)"
mkdir -p "$TARGET"

case "$DOMAIN" in
    all) for d in dynamics msft flask customer backend; do install_domain "$d"; done ;;
    *)   install_domain "$DOMAIN" ;;
esac

echo "Roles installed to $TARGET"
