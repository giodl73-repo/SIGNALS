#!/usr/bin/env bash
# parse-narration.sh <narration.md>
# Parses narration markdown into JSON sections.
# Output: JSON array to stdout
#   [{"name":"intro","text":"This is the intro..."},...]
#
# Format: ## section-name followed by narration text.

set -euo pipefail

INPUT="$1"

if [[ ! -f "$INPUT" ]]; then
  echo "ERROR: narration file not found: $INPUT" >&2
  exit 1
fi

awk '
BEGIN { printf "["; first = 1; name = ""; text = "" }
/^## / {
  if (name != "") {
    gsub(/^ +| +$/, "", text)
    gsub(/"/, "\\\"", text)
    gsub(/\n+$/, "", text)
    if (!first) printf ","
    printf "{\"name\":\"%s\",\"text\":\"%s\"}", name, text
    first = 0
  }
  name = substr($0, 4)
  gsub(/^ +| +$/, "", name)
  text = ""
  next
}
name != "" && /[^ ]/ {
  if (text != "") text = text " "
  line = $0
  gsub(/^ +| +$/, "", line)
  text = text line
}
END {
  if (name != "") {
    gsub(/^ +| +$/, "", text)
    gsub(/"/, "\\\"", text)
    gsub(/\n+$/, "", text)
    if (!first) printf ","
    printf "{\"name\":\"%s\",\"text\":\"%s\"}", name, text
  }
  printf "]"
}
' "$INPUT"
