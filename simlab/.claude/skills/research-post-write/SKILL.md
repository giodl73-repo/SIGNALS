---
name: research-post-write
description: "Full post-writing validation pipeline. Runs consistency + dimensional + contract + referee + abstract skills, outputs a pre-submission checklist. Configures itself from the paper type."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /research-post-write for: {{topic}}

Run the full post-writing validation pipeline for an academic paper. This orchestrates the
validation skills, appends findings to FINDINGS.md, and produces a pre-submission checklist.

---

## PHASE 1 -- READ THE PAPER

Read `research/*/publications/{{topic}}/plan.md` and all section files.

Extract:
- **Paper type**: math-heavy if ODE / formula / derivation / dimensional in plan or sections
- **Target journal**: from `Venue:` field
- **Stage**: from `_panel.yaml`
- **Primary number**: the key quantitative claim

Print:
```
Paper: {{topic}}
Journal: [venue]
Stage: [stage from _panel.yaml]
Math-heavy: [YES/NO]
```

---

## PHASE 2 -- CONSISTENCY CHECK (always)

Run `/validate-consistency {{topic}}`

Append findings to FINDINGS.md. Print:
```
CONSISTENCY: [PASS/FAIL] — [N] mismatches found
Critical: [list any P1 mismatches]
```

If P1 mismatches found, STOP and present them. Do not proceed until resolved.

---

## PHASE 3 -- DIMENSIONAL CHECK (math-heavy only)

If math-heavy: Run `/validate-dimensional {{topic}}`

Append findings to FINDINGS.md. Print:
```
DIMENSIONAL: [PASS/FAIL] — [N] errors found
```

If P1 errors found, STOP and present them.

---

## PHASE 4 -- CONTRACT CHECK (always)

Run `/simulate-contract {{topic}}`

This checks whether the paper delivers what its methodology promises.

Append findings to FINDINGS.md. Print:
```
CONTRACT: [PASS/FAIL]
Mismatches: [list any items where claims exceed methodology]
```

---

## PHASE 5 -- ABSTRACT (always)

Run `/specify-abstract {{topic}} --for journal:[journal from plan.md]`

If journal is:
- Journal of Consciousness Studies → `--for journal:jcs`
- Journal of Theoretical Biology → `--for journal:jtb`
- Complexity → `--for journal:complexity`
- PNAS → `--for journal:pnas`
- Psychological Science → `--for journal:psych-science`
- Other → `--for journal:default`

Print the merged abstract (200-250 words) and word count.

---

## PHASE 6 -- REFEREE SIMULATION (always)

Run `/validate-referee {{topic}} --for journal:[journal]`

Print the likely decision and P1 blockers.

```
REFEREE SIMULATION: [likely decision]
P1 blockers: [I-NN list]
Strongest referee: [who and why]
```

---

## PHASE 7 -- PRE-SUBMISSION CHECKLIST

Print the full pre-submission checklist derived from the validation pass:

```
═══════════════════════════════════════════════════════
POST-WRITE COMPLETE: {{topic}}
═══════════════════════════════════════════════════════

Validation results:
  Consistency:  [PASS/FAIL — N mismatches]
  Dimensional:  [PASS/FAIL / N/A]
  Contract:     [PASS/FAIL — N mismatches]
  Referee sim:  [likely decision]

Abstract: [word count] words — [ON TARGET/OVER/UNDER]

PRE-SUBMISSION CHECKLIST:
□ All P1 consistency mismatches resolved
□ All P1 dimensional errors resolved (if math paper)
□ Contract: all quantification promises deliverable
□ Abstract within 250 words, 6-part structure
□ Referee P1 blockers addressed (I-NN, I-NN)
□ R measured independently of τ (Principle 2)
□ Falsification condition stated with specific observable
□ Null hypothesis stated and distinguished from RMM prediction
□ Primary number delivered (from plan.md quantification contract)
□ Three placeholder citations verified (if any flagged)

VERDICT: [READY TO SUBMIT / FIXES REQUIRED]
Items requiring action: [N]
═══════════════════════════════════════════════════════
```

If FIXES REQUIRED, list each item with the section reference and the specific fix needed.
