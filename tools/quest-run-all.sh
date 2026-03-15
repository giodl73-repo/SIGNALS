#!/bin/bash
# quest-run-all.sh -- Dispatch quest-run-one.sh for all non-golden skills in parallel
# Each skill runs as an independent relay job (P-01 concurrent by default)
# Usage: bash tools/quest-run-all.sh [--namespace scout] [--dry-run]

RELAY="http://127.0.0.1:8716"
REPO="C:/src/sim"
SKILLS_YAML="$REPO/signal.skills.yaml"
NAMESPACE_FILTER=""
DRY_RUN=false
MAX_CONCURRENT=8   # relay job limit

while [[ $# -gt 0 ]]; do
  case $1 in
    --namespace) NAMESPACE_FILTER="$2"; shift 2 ;;
    --dry-run)   DRY_RUN=true; shift ;;
    *) shift ;;
  esac
done

echo "=== quest-run-all ==="
echo "Relay: $RELAY"
[ -n "$NAMESPACE_FILTER" ] && echo "Namespace filter: $NAMESPACE_FILTER"
$DRY_RUN && echo "[DRY RUN]"
echo ""

# Get all skills without golden status
SKILLS=$(python -c "
import yaml, sys
with open('$SKILLS_YAML') as f:
    data = yaml.safe_load(f)
for s in data.get('skills', []):
    ns = s.get('namespace', '')
    skip = s.get('quest_status', '').startswith('GOLDEN')
    skip = skip or ns == 'meta'
    ns_filter = '$NAMESPACE_FILTER'
    if ns_filter and ns != ns_filter:
        skip = True
    if not skip:
        print(s['id'])
")

SKILL_COUNT=$(echo "$SKILLS" | grep -c . || echo 0)
echo "Skills to process: $SKILL_COUNT"
echo "$SKILLS" | while read s; do echo "  $s"; done
echo ""

if $DRY_RUN; then
  echo "[DRY RUN] Would dispatch $SKILL_COUNT jobs"
  exit 0
fi

if [ "$SKILL_COUNT" -eq 0 ]; then
  echo "All skills are already GOLDEN."
  exit 0
fi

# Dispatch all jobs
declare -a JOB_IDS
declare -a JOB_SKILLS

i=0
echo "$SKILLS" | while read SKILL_ID; do
  [ -z "$SKILL_ID" ] && continue

  JOB=$(curl -s -X POST "$RELAY/run" \
    -H 'Content-Type: application/json' \
    -d "{\"script\":\"tools/quest-run-one.sh\",\"args\":[\"$SKILL_ID\"],\"cwd\":\"$REPO\"}")
  JOB_ID=$(echo "$JOB" | python -c "import sys,json; print(json.load(sys.stdin).get('job_id','ERROR'))" 2>/dev/null)
  echo "[$SKILL_ID] dispatched -> $JOB_ID"
  echo "$JOB_ID:$SKILL_ID" >> /tmp/quest-jobs-$$.txt
done

echo ""
echo "All jobs dispatched. Polling for completion..."
echo ""

# Poll until all done
while true; do
  ALL_DONE=true
  DONE_COUNT=0
  FAIL_COUNT=0
  TOTAL=0

  while IFS=: read JOB_ID SKILL_ID; do
    [ -z "$JOB_ID" ] && continue
    TOTAL=$((TOTAL + 1))
    STATUS=$(curl -s "$RELAY/status/$JOB_ID" | python -c "import sys,json; print(json.load(sys.stdin).get('status','unknown'))" 2>/dev/null)
    case $STATUS in
      done)   DONE_COUNT=$((DONE_COUNT + 1)) ;;
      failed) FAIL_COUNT=$((FAIL_COUNT + 1)) ;;
      running|pending) ALL_DONE=false ;;
    esac
  done < /tmp/quest-jobs-$$.txt

  echo "Progress: $DONE_COUNT done, $FAIL_COUNT failed, $((TOTAL - DONE_COUNT - FAIL_COUNT)) running / $TOTAL total"

  $ALL_DONE && break
  sleep 30
done

echo ""
echo "=== Results ==="
while IFS=: read JOB_ID SKILL_ID; do
  [ -z "$JOB_ID" ] && continue
  STATUS=$(curl -s "$RELAY/status/$JOB_ID" | python -c "import sys,json; d=json.load(sys.stdin); print(d.get('status'), d.get('exit_code',''))" 2>/dev/null)
  echo "[$SKILL_ID] $STATUS"
done < /tmp/quest-jobs-$$.txt

rm -f /tmp/quest-jobs-$$.txt

echo ""
echo "Done. Check signal.skills.yaml for updated quest_status fields."
echo "Next: python tools/gen-binding-flat.py && craft generate --stage program"
