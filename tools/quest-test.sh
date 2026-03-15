#!/bin/bash
# quest-test.sh -- Unit test: verify Claude API is reachable from the relay
# Usage: dispatch via relay, check stdout for "PASS"

set -e

echo "=== quest-test: Claude API reachability ==="

# Call Claude via claude -p (the relay is designed for nested claude invocations)
TEXT=$(claude -p "Reply with exactly the word: RELAY_OK" 2>/dev/null)

echo "Response: $TEXT"

if echo "$TEXT" | grep -q "RELAY_OK"; then
  echo "PASS: claude -p works from relay"
else
  echo "FAIL: claude -p did not return expected response (got: $TEXT)"
  exit 1
fi
