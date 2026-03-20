---
mode: agent
description: "Show topic coverage and commitment readiness. DISPLAY ONLY. Use --view for supplementary perspectives: --view roadmap (w"
---
You are running /rhythm-status for: {{topic}}

DISPLAY ONLY. Do not write a file.

Show the current state of a topic: which signals exist on disk, which are missing,
and whether the topic is ready to commit.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
If no signals found: output "No signals found for {{topic}}" and stop.

List each found signal:
  <namespace>/<skill>/<filename>  <date>

---

## PHASE 2 -- COVERAGE ASSESSMENT

Read signals/strategy.md if it exists.
- If absent: output "No planned baseline -- commit exposure is unquantifiable." and continue.
- If present: extract planned signals for {{topic}}.

For each planned signal:
  VERIFIED   -- signal artifact exists on disk
  UNVERIFIED -- no artifact found

---

## PHASE 3 -- COMMITMENT READINESS DISPLAY

Output the following terminal view:

```
SIGNAL STATUS: {{topic}}
========================

Found:   N signals
Missing: M signals
Coverage: N/(N+M) = Z%

SIGNALS FOUND:
  <namespace>/<skill>  <date>
  ...

BLOCKING GAPS (required before commit):
  <namespace>/<skill>  -- <inertia risk: what team is assuming if they commit today>
  ...
  (None -- all planned signals present)

OPTIONAL GAPS:
  <namespace>/<skill>  -- <trade-off if skipped>
  ...
  (None)

COMMITMENT READINESS: READY | NOT READY | NO BASELINE

HIGHEST PRIORITY RISK:
  /<namespace> <skill> {{topic}}
```

COMMITMENT READINESS rules:
- READY: all BLOCKING signals verified OR no strategy.md baseline exists but 3+ signals present
- NOT READY: one or more BLOCKING signals unverified
- NO BASELINE: strategy.md absent and fewer than 3 signals present

--view options (append to command):
  --view roadmap    Show planned signal sequence and target dates
  --view gaps       Show only missing signals with inertia risk assessment
  --view exec       Condensed executive view: coverage %, readiness, top risk only

Do not write a file. This is a terminal display command.
