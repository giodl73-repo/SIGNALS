---
name: research-pre-write
description: "Full pre-writing pipeline for academic papers. Reads plan.md, runs all discovery + argument + derivation skills, collects findings, resolves blocking items, then produces a ready spec."
allowed-tools: [Read, Write, Glob, Grep, WebSearch]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /research-pre-write for: {{topic}}

Run the full pre-writing signal pipeline for an academic paper. This orchestrates the discovery
skills, collects all findings into FINDINGS.md, resolves blocking items, and produces a ready
spec before writing begins.

---

## PHASE 1 -- READ THE PLAN

Read `research/*/publications/{{topic}}/plan.md` (or search for it with Glob).

Extract:
- **Paper type**: math-heavy if plan.md contains ODE / dR/dt / formula / derivation / integral / dimensional / spectral / electromagnetic
- **Target journal**: from `Venue:` field
- **Track**: from `Track:` field
- **Primary number**: the key quantitative claim the paper must deliver
- **Methodology**: how the paper will generate evidence

Print:
```
Paper: {{topic}}
Type: [MATH-HEAVY / EMPIRICAL / HISTORICAL / THEORETICAL]
Journal: [venue]
Track: [track]
Primary number: [primary number]
Math-heavy skills: [YES/NO — simulate-derivation + validate-dimensional]
```

---

## PHASE 2 -- DISCOVERY SEQUENCE

Run each skill in order. After each skill, append findings to FINDINGS.md in the paper directory.
Use the standard FINDINGS.md format: each finding gets an F-NN ID, one-sentence description,
section reference, and source link if from websearch.

Skills to run (in order):

1. `/discover-hypothesis {{topic}}` → append to FINDINGS.md under "From: discover-hypothesis"
2. `/discover-competitors {{topic}}` → append findings
3. `/discover-causal {{topic}}` → append findings
4. `/discover-websearch {{topic}}` → append findings
5. **If MATH-HEAVY:** `/simulate-derivation {{topic}}` → append findings
6. `/simulate-argument {{topic}}` → append findings (note: no paper written yet — trace the intended argument from plan.md and signals)

After each skill, summarize the top 1-2 findings before proceeding. Ask: "Continue to [next skill]?"

---

## PHASE 3 -- COHERENCE + SYNTHESIZE

7. `/discover-coherence {{topic}}` — produces blocking / advisory list

Print the verdict:
```
COHERENCE: [N] blocking, [M] advisory
Blocking items: [list]
```

8. `/discover-synthesize {{topic}}` — produces PROCEED / PAUSE / PIVOT

If **PROCEED**: continue to Phase 4.

If **PAUSE**: present the blocking items clearly. For each blocking item:
```
BLOCKING [N]: [description]
Resolution required: [what must change — in plan.md, methodology, anchor cases, etc.]
```

Wait for user to confirm resolution. Then re-run `/discover-coherence {{topic}}` to verify
blocks are cleared. If cleared, continue to Phase 4. If still blocked, present remaining
items and wait again.

If **PIVOT**: stop. Present the pivot recommendation to the user before proceeding.

---

## PHASE 4 -- UPDATE PLAN IF NEEDED

If Phase 3 identified changes needed to plan.md (new anchor cases, ODE modification, scope
change), update plan.md to reflect the revised methodology before running specify-spec.

Print the changes made:
```
Plan updated:
- [change 1: e.g., "ODE changed from dR/dt = α(1−R)O to dR/dt = α(R_max−R)O"]
- [change 2: e.g., "Anchor cases expanded from 2 to 4"]
```

---

## PHASE 5 -- SPECIFY-SPEC

Run `/specify-spec {{topic}}` using the updated plan.md as input.
The spec becomes the paper outline for authoring.

Output the spec summary:
```
SPEC READY: {{topic}}
Sections: [list of planned sections]
Primary number: [how it will be delivered]
Key methodology: [approach]
```

---

## PHASE 6 -- READINESS REPORT

Print a final pre-writing readiness report:

```
═══════════════════════════════════════════════════════
PRE-WRITE COMPLETE: {{topic}}
═══════════════════════════════════════════════════════

Skills run: [list]
Findings collected: [N] (in research/*/publications/{{topic}}/FINDINGS.md)
Blocking items resolved: [N]
Plan updates made: [N]

VERDICT: READY TO WRITE
Next: panel:publication author {{topic}}

Top 3 things to get right in the paper:
1. [most important finding from pipeline]
2. [second most important]
3. [third most important]
═══════════════════════════════════════════════════════
```

Write nothing to disk except FINDINGS.md updates (each skill writes its own artifact to signals/).
The spec is the primary output artifact.
