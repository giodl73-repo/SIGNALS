You are running /simulate-argument for: {{topic}}

Trace the logical argument chain of a paper step by step — the way simulate-state traces state transitions. Academic papers have causal chains (P01's formula → P02's states → P03's dynamics). Hand-compile the argument to find exactly where it breaks.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

---

## PHASE 2 -- CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |
...

Types:
- **premise**: accepted without proof in this paper (must be cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

Minimum: 6 claims. Every paper section should contribute at least 1 claim.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 -- STEP-BY-STEP TRACE

For each inference step (any claim with type=inference), verify:

```
STEP [C-ID]: [claim text]
Depends on: [C-IDs]
Logical form: [If X and Y then Z — or name the logical structure]
Validity check:
  - Does the conclusion follow from the premises? [YES / WEAK / NO]
  - Are the premises empirically supported? [YES / CITED / ASSUMED / UNSUPPORTED]
  - Are key terms used consistently with their definitions? [YES / DRIFT: describe]
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the gap]
```

---

## PHASE 4 -- FAULT REGISTER

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

---

## PHASE 5 -- AMEND

Three structural fixes ordered by severity:
1. [P1 fix: how to repair or replace the broken inference]
2. [P2 fix: how to strengthen the weakest empirical claim]
3. [P3 fix: where a definition is drifting and how to stabilize it]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]
