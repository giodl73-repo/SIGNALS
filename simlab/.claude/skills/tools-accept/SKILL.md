---
name: tools-accept
description: "Step 2 of mock-first workflow: review mock coverage picture and produce MOCK-ACCEPTED or REAL-REQUIRED decisions per nam"
allowed-tools: [Read, Write, Edit, Glob]
param_set: lean
---
You are running /tools-accept for: {{topic}}

Step 2 of the mock-first Signal workflow. Reviews mock artifact coverage and produces
MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace.

Usage:   /tools-accept {{topic}}
Step 1:  Run /tools-coverage {{topic}} first to see what mock coverage exists
Step 3:  Proceed with REAL-REQUIRED namespaces before committing

Flags:
  --tier 1    Only evaluate Tier 1 (essential) namespaces
  --tier 2    Evaluate Tier 1 + Tier 2 (recommended)
  --tier 3    Evaluate all namespaces (default)

Criteria:
  MOCK-ACCEPTED:  namespace has mock coverage AND decision is not ship-blocking
  REAL-REQUIRED:  namespace lacks coverage OR decision is high-stakes (ship/no-ship)

Full runbook: tools-accept.t3/SKILL.md

DISPLAY ONLY -- no file written.
