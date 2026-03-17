# listen-support Round 7 — Skill Body Prompt Variations

**Rubric target**: v7 (180 pts) | **New criteria**: C-24, C-25, C-26

---

## V-01: Output Format — Formal AUDIT RESULT Gate

**Axis**: Output format (C-24 mechanism strength)
**Hypothesis**: The load-bearing mechanism for C-24 is the output slot. Requiring "AUDIT RESULT: PASS" before proceeding forces a declarable result. A correction gate without an output slot permits implicit passing — the model writes the check text but skips correction. The AUDIT RESULT slot makes the audit checkable in under 5 seconds. C-25 minimal (2 collocations); C-26 present.

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO
## STEP 2 — PHASE-CHARACTER MAP (split Severity Range / Volume Character columns)
## STEP 3 — CONTROLLED VOCABULARY
## STEP 4 — SUMMARY TABLE
## STEP 4B — COLLECTIVE-DISTRIBUTION AUDIT
  AUDIT RESULT: [PASS / FAIL]
  (1) Phase distribution: [PASS / FAIL]
  (2) Category spread: [PASS / FAIL]
  (3) Volume distribution: [PASS / FAIL]
  (4) Phase-character compliance: [PASS / FAIL]
  If FAIL: Correction made: [row, field, new value]. Re-run.
  Do not write any card body until AUDIT RESULT: PASS.
## STEP 5 — FULL TICKET CARDS (You ARE + 2 verb collocations prohibited + Every action by "I")
## STEP 6 — CROSS-TICKET PATTERN (flat consequence fields + Prohibited sentinels)
## STEP 7 — GAP ANALYSIS
## STEP 8 — DUAL-PASS: PASS 1 + END OF PASS 1. Switch to frontmatter verification mode. + PASS 2
```

---

## V-02: Phrasing Register — Exhaustive Verb-Subject Enumeration

**Axis**: Phrasing register (C-25 mechanism depth)
**Hypothesis**: A 2-collocation prohibition list leaves most verb-role pairings unlisted as escape routes. Exhaustive enumeration of 13+ pairs across all stock roles, plus a catch-all ("any role title precedes any verb"), closes the unlisted-collocation path structurally. C-24 minimal (3 constraints, no AUDIT RESULT slot); C-26 present.

Key Step 5 mechanism:
```
  ALL of the following verb-subject forms are prohibited:
    "the SRE ran"     "the SRE observed"    "the SRE noticed"
    "the SRE confirmed"  "the SRE checked"
    "the PM reviewed"  "the PM flagged"     "the PM escalated"
    "the engineer ran"  "the engineer noted"  "the engineer observed"
    "the Support agent opened"   "the Support agent confirmed"
    "the C-[NN] clicked"   "the C-[NN] attempted"
    "the UX designer flagged"   "the UX designer observed"
    Any construction where a role title precedes any verb whatsoever.
  Every action in this ticket was taken by "I".
```

---

## V-03: Inertia Framing — Named Inertia Competitor

**Axis**: Inertia framing (STATUS QUO mechanism depth)
**Hypothesis**: Naming the competing tool explicitly as the "Inertia Competitor" produces stronger STATUS QUO traces — a tool name in the coverage audit column is unambiguous; "the old workflow" requires interpretation. The named competitor also produces phase-differentiated ticket bodies no prior variation achieved: P1 bodies describe dual-tool parallelism ("I still have [tool] open"); P3 bodies describe parity-gap frustration ("In [tool] I could do X; here I cannot"). C-24 minimal, C-25 minimal, C-26 present.

Key Step 1 mechanism:
```
**INERTIA COMPETITOR**:
- Name it: [specific tool name -- not a category; "Jira custom-field approach",
  "manual kubectl scripts in the deploy repo"]
- Name one cost users have already absorbed that they will not re-absorb switching.
- Name one capability the inertia competitor has that this feature does not replicate.
- Name the first action a new user will try that they currently perform in it.
```

Key Step 2 addition:
```
P1: users run inertia competitor and this feature in parallel -- dual-tool confusion.
P2: adoption gap -- some committed, some reverting.
P3: committed users compare a specific missing capability to the inertia competitor's equivalent.
```

---

## V-04: C-24 Strong + C-25 Strong (Combined)

**Axes**: Output format (AUDIT RESULT gate) + Phrasing register (exhaustive enumeration)
**Hypothesis**: C-24 and C-25 address non-overlapping failure surfaces. C-24 catches table-level distribution bias before any body is written; C-25 catches analyst-stance drift inside bodies after they are written. Combining at full strength closes both simultaneously. No inertia framing — standard STATUS QUO to isolate the C-24/C-25 interaction.

---

## V-05: Full Synthesis

**Axes**: Inertia framing + C-24 STRONG + C-25 exhaustive + C-26 delimiter + C-22 explicit independence
**Hypothesis**: Inertia competitor naming produces phase-differentiated bodies and unambiguous coverage traces; C-24 AUDIT RESULT gate prevents distribution bias; C-25 exhaustive enumeration closes all verb-subject analyst-stance paths; C-26 mode-switch delimiter makes pass independence structurally unambiguous; C-22 "detectable by reading two cells" makes column independence explicit. All 26 criteria at ceiling simultaneously.

**Above-ceiling signal candidate**: The inertia competitor phase framing (P1 dual-tool / P3 parity-gap body instructions) is a richer C-11 mechanism than any prior STATUS QUO formulation — may become a new criterion distinguishing *named-competitor grounding* from *baseline-scenario grounding*.

---

## Variation Map

| V | Axis | C-24 | C-25 | C-26 | Inertia |
|---|------|------|------|------|---------|
| V-01 | Output format | STRONG: AUDIT RESULT slot + 4 constraints | minimal (2 pairs) | present | no |
| V-02 | Phrasing register | minimal (3 constraints, no slot) | STRONG: 13+ pairs + catch-all | present | no |
| V-03 | Inertia framing | minimal | minimal | present | STRONG: named competitor + phase framing |
| V-04 | C-24 + C-25 combined | STRONG | STRONG | present | no |
| V-05 | Full synthesis | STRONG | STRONG | present | STRONG |

**Expected ceiling under v7**: V-05 = 180/180

Saved to `simulations/quest/rubrics/listen-support-rubric-v7-variations-R7-2026-03-14.md`.
