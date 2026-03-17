#!/usr/bin/env bash
# Signal Role Registry Installer
# Usage: ./install/install-roles.sh [--domain <name>] [--domain <name>...] [--all] [target-dir]
#
# Domains:
#   dynamics    Dynamics 365 / Power Platform (dataverse, automate, commerce, sales,
#               connectors, copilotstudio, customer-service, finance, operations,
#               power-pages, power-bi, teams)
#   flask       Python web (flask, fastapi)
#   mobile      iOS, Android, React Native
#   ml          Data science, ML engineering, data engineering
#   frontend    React, vanilla JS, designer sub-roles
#   security    Security, compliance (GDPR, SOC2, accessibility)
#   all         Every role in the registry (1.8MB)
#
# Default (no --domain): installs Signal's cross-cutting concern roles only (~200KB)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROLES_SRC="$SCRIPT_DIR/../.craft/roles"
TARGET_DIR="${!#}"
DOMAINS=()
ALL=false

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --domain) DOMAINS+=("$2"); shift 2 ;;
    --all)    ALL=true; shift ;;
    *)        TARGET_DIR="$1"; shift ;;
  esac
done

# Default target
if [[ -z "$TARGET_DIR" || "$TARGET_DIR" == --* ]]; then
  TARGET_DIR=".craft/roles"
fi

mkdir -p "$TARGET_DIR"

copy_role() {
  local src="$1"
  local base
  base=$(basename "$src")
  if [[ -d "$src" ]]; then
    cp -r "$src" "$TARGET_DIR/"
    echo "  + $base/ ($(find "$src" -name "*.md" | wc -l) files)"
  elif [[ -f "$src" ]]; then
    cp "$src" "$TARGET_DIR/"
    echo "  + $base"
  fi
}

echo "Signal Role Registry"
echo "Installing to: $TARGET_DIR"
echo ""

# Always: Signal cross-cutting concern roles
echo "Core Signal roles:"
copy_role "$ROLES_SRC/ROLE.md"
copy_role "$ROLES_SRC/inertia.md"
copy_role "$ROLES_SRC/inertia-advocate.md"
copy_role "$ROLES_SRC/discover"
copy_role "$ROLES_SRC/specify"
copy_role "$ROLES_SRC/validate"
copy_role "$ROLES_SRC/simulate"
copy_role "$ROLES_SRC/narrate"
copy_role "$ROLES_SRC/govern"

# Always: The 4 universal roles
echo ""
echo "Universal roles:"
copy_role "$ROLES_SRC/pm.md"
copy_role "$ROLES_SRC/architect.md"
copy_role "$ROLES_SRC/security"
copy_role "$ROLES_SRC/pm"
copy_role "$ROLES_SRC/architect"
copy_role "$ROLES_SRC/tpm"

if $ALL; then
  echo ""
  echo "Full registry (--all):"
  cp -r "$ROLES_SRC"/. "$TARGET_DIR/"
  echo "  + all roles"
else
  for domain in "${DOMAINS[@]}"; do
    echo ""
    echo "Domain: $domain"
    case "$domain" in
      dynamics)
        copy_role "$ROLES_SRC/backend/dataverse.md"
        copy_role "$ROLES_SRC/backend/automate.md"
        copy_role "$ROLES_SRC/backend/commerce.md"
        copy_role "$ROLES_SRC/backend/sales.md"
        copy_role "$ROLES_SRC/backend/connectors.md"
        copy_role "$ROLES_SRC/backend/copilotstudio.md"
        copy_role "$ROLES_SRC/backend/customer-service.md"
        copy_role "$ROLES_SRC/backend/finance.md"
        copy_role "$ROLES_SRC/backend/operations.md"
        copy_role "$ROLES_SRC/backend/power-pages.md"
        copy_role "$ROLES_SRC/backend/power-bi.md"
        copy_role "$ROLES_SRC/backend/teams.md"
        copy_role "$ROLES_SRC/backend/ROLE.md"
        ;;
      flask)
        copy_role "$ROLES_SRC/backend/flask-guide.md"
        copy_role "$ROLES_SRC/backend/fastapi-guide.md"
        copy_role "$ROLES_SRC/backend/ROLE.md"
        ;;
      mobile)
        copy_role "$ROLES_SRC/mobile"
        ;;
      ml)
        copy_role "$ROLES_SRC/data-scientist"
        copy_role "$ROLES_SRC/ml-engineer"
        copy_role "$ROLES_SRC/data-engineer"
        ;;
      frontend)
        copy_role "$ROLES_SRC/frontend"
        copy_role "$ROLES_SRC/designer"
        copy_role "$ROLES_SRC/ux-researcher"
        ;;
      security)
        copy_role "$ROLES_SRC/security"
        copy_role "$ROLES_SRC/compliance"
        ;;
      customer)
        copy_role "$ROLES_SRC/customer"
        ;;
      msft)
        copy_role "$ROLES_SRC/msft"
        ;;
      *)
        echo "  Unknown domain: $domain (skipped)"
        ;;
    esac
  done
fi

echo ""
TOTAL=$(find "$TARGET_DIR" -name "*.md" | wc -l)
SIZE=$(du -sh "$TARGET_DIR" 2>/dev/null | cut -f1)
echo "Installed: $TOTAL role files ($SIZE)"
echo ""
echo "Next: run /signal-setup to advertise Signal in your CLAUDE.md"
echo "      run /govern-roles to generate roles specific to your codebase"
# Note: customer and msft domains added below -- patch applied after initial write
