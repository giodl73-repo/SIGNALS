# /quest:score — topic-plan Round 18 (Rubric v17)

## Rubric Reference

**58 criteria, 340 pts total**
- Essential (5): C-01–C-05 → 12 pts each
- Recommended (3): C-06–C-08 → 10 pts each
- Aspirational (50): C-09–C-58 → 5 pts each (PARTIAL = 2.5)
- Formula: `(ess/5×60) + (rec/3×30) + (asp/50×250)`
- Golden threshold: 210

---

## Baseline (common to all variations)

All five variations inherit from a common R17-winning core. Before scoring the variable criteria, the base is:

| Layer | Criteria | Score |
|-------|----------|-------|
| Essential | C-01–C-05: reads strategy.md, reads signals, identifies delta, types proposals, confirmation gate | 60/60 |
| Recommended | C-06–C-08: evidence citations, before/after view, all three change types | 30/30 |
| Aspirational base | C-09–C-52 + C-54 (45 criteria): all pass across all variations | 225/250 |
| **Base total** | | **315** |

**Baseline evidence (selected):** All variations carry COLUMN CONTRACT with 4 rules + purpose clauses (C-54), anti-pattern checkpoint (C-14), 9-namespace enumeration (C-15), two-level evidence chain (C-16), null-case Rule 3 templates (C-23/C-40), upfront schema block (C-26), cascade checkpoints (C-27), assumption table with 5 columns (C-29/C-30/C-33), decision-gate framing for "If unchanged" (C-31), reversibility three-value enumeration (C-32), pre-signal Defense Register (C-47), defense basis column (C-48), signal read-lock (C-49), challenge strength column (C-50), co-equal inertia framing in preamble (C-51), calibration check present (C-52), withdrawal-aware gate (C-44), Delta Finding Rule 4 (C-45).

---

## Variable Criteria — Per-Variation Analysis

The five criteria that differ across R18 variations:

| Criterion | Description | Target |
|-----------|-------------|--------|
| C-53 | Analytical narrative before each of five analytical tables | aspirational/format |
| C-55 | WHY clause at opening of each execution step | aspirational/enforcement |
| C-56 | Pre-role inertia framing + verbatim recurrence blocks at 3 named gates | aspirational/behavior |
| C-57 | Calibration check as pre-printed slot with "select exactly one" | aspirational/enforcement |
| C-58 | Narrative gate rows name degenerate register with format discriminator | aspirational/format |

---

## V-01: Inertia Framing — Verbatim Interrupt Blocks

**Axis:** C-56 recurrence form

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-53 | FAIL | No "Narrative — REQUIRED before table" sections at Steps 3/3b/4/5/6 |
| C-55 | FAIL | No "This step exists so that..." clauses on any step |
| C-56 | **PASS** | Inertia framing precedes role line; INERTIA-GATE verbatim block template defined; `[INERTIA-GATE]` reproduced at Steps 4, 4b, 7 — block presence/absence is structurally visible |
| C-57 | FAIL | Calibration check is conditional branch ("All Weak → write X; otherwise → write Y"), not pre-printed slot |
| C-58 | FAIL | No degenerate register naming at narrative sites |

**V-01 score:** 315 + 5 (C-56) = **320**

---

## V-02: Enforcement — Pre-Printed Slot Architecture Extended

**Axis:** C-57 generalized to all decision sites

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-53 | FAIL | No narrative requirement sections at analytical steps |
| C-55 | FAIL | No WHY clauses on steps |
| C-56 | FAIL | Inertia framing appears AFTER "You are running /topic:plan..." (post-role); recurrence in Steps 4/4b is inline prose ("Inertia is a co-equal option"), not verbatim block artifacts |
| C-57 | **PASS** | Pre-printed `[ ] A / [ ] B` slots at: schema commitment, null cases (Steps 1b, 3, 3b, 5), empty-type rows, schema checkpoints (Steps 4, 6), and calibration check — all with "select exactly one and write it as output" |
| C-58 | FAIL | No degenerate register naming; calibration check slots don't include register discrimination |

**V-02 score:** 315 + 5 (C-57) = **320**

---

## V-03: Format — Degenerate Register Discrimination

**Axis:** C-58

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-53 | **PASS** | Narrative Format Contract block defined upfront; "Narrative — REQUIRED before table" present at Steps 3, 3b, 4, 5, 6; PHASE 3 EXIT GATE checks register on all five sites |
| C-55 | FAIL | No WHY clauses on steps |
| C-56 | FAIL | Inertia framing is post-role; no verbatim INERTIA-GATE blocks at named gates (Step 4 has inline "Inertia is a co-equal option", Steps 4b and 7 have no explicit recurrence) |
| C-57 | FAIL | Calibration check uses conditional branch form, not pre-printed slot |
| C-58 | **PASS** | Narrative Format Contract names both REQUIRED register ("Narrative: conclusion before evidence") and DEGENERATE register ("Step-description narrative — FAIL"); concrete FAIL examples at every narrative site ("This table lists all artifacts for the topic"); gate rows use format discriminator "[conclusion before evidence] — NOT [step-description]"; PHASE 3 EXIT GATE enforces register compliance before confirmation |

**V-03 score:** 315 + 5 (C-53) + 5 (C-58) = **325**

---

## V-04: Role Sequence — Schema → Inertia → Role

**Axis:** Pre-task contract ordering

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-53 | FAIL | No "Narrative — REQUIRED before table" sections at analytical steps |
| C-55 | PARTIAL | Step 2 has a why clause ("This step commits strategic keep-arguments before any disconfirming signal is encountered; post-signal defenses are auditable as newly constructed rather than pre-committed") but no other steps carry systematic WHY clauses |
| C-56 | PARTIAL | Pre-role placement: ✓ (schema → inertia → role line order is correct, satisfies C-56 req 1); recurrence: ✗ only "Recall: inertia is a co-equal option. (See inertia framing above.)" at Steps 4, 4b, 7 — recalled sentences, not verbatim block artifacts, subject to same compression risk as inline instruction (fails C-56 req 2) |
| C-57 | **PASS** | Calibration check expressed as pre-printed slot: "[ ] 'Calibration: rubber-stamp risk...'" / "[ ] 'Calibration: over-zealous risk...'" / "[ ] 'Calibration: balanced...'" with "select exactly one and write it as output" |
| C-58 | FAIL | No degenerate register naming at narrative sites |

**V-04 score:** 315 + 2.5 (C-55 partial) + 2.5 (C-56 partial) + 5 (C-57) = **325**

---

## V-05: Combined — V-01 + V-02 + V-03

**Axis:** C-56 + C-57 + C-58 + full integration

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-53 | **PASS** | Narrative Format Contract upfront; "Narrative — REQUIRED before table" at Steps 3, 3b, 4, 5, 6; each site has `> [Write narrative here — REQUIRED register]` prompt; PHASE 3 EXIT GATE checks all five sites |
| C-55 | **PASS** | Every step carries "This step exists so that..." rationale before output specification: Step 1 (STRATEGY DATE partition), Step 2 (ante-signal commitment), Step 3 (closed evidence base), Step 3b (explicit contradiction naming), Step 4 (null competitor defeat), Step 4b (strongest argument before gate), Step 5 (conflict surfacing), Step 6 (diff as write audit surface), Step 8 (exactly confirmed changes) |
| C-56 | **PASS** | Inertia framing precedes role line ✓; INERTIA-GATE verbatim block defined with visual border box; reproduced verbatim at Steps 4, 4b, 7; PHASE 3 EXIT GATE explicitly checks "INERTIA-GATE blocks reproduced verbatim at Steps 4 and 4b"; block structural absence detectable as missing artifact |
| C-57 | **PASS** | Calibration pre-printed slot at Step 4b; schema commitment slots at Steps 1b, 3, 3b, 4, 4b, 6; empty-type slots for ADD/REMOVE/REPRIORITIZE; null slots at Step 5; all use "select exactly one and write it as output" pattern |
| C-58 | **PASS** | Narrative Format Contract: REQUIRED register named ("Narrative: conclusion before evidence — states what was found and why it matters") + DEGENERATE register named ("Step-description — FAIL") with two concrete FAIL examples; at every narrative site gate item reads "[ ] Narrative is in REQUIRED register — NOT in DEGENERATE register (step-description)"; explicit FAIL example per site; PHASE 3 EXIT GATE enforces before confirmation |

**V-05 score:** 315 + 5 (C-53) + 5 (C-55) + 5 (C-56) + 5 (C-57) + 5 (C-58) = **340**

---

## Score Summary

| Variation | C-53 | C-55 | C-56 | C-57 | C-58 | Variable pts | Total |
|-----------|------|------|------|------|------|-------------|-------|
| V-01 | FAIL | FAIL | **PASS** | FAIL | FAIL | +5 | **320** |
| V-02 | FAIL | FAIL | FAIL | **PASS** | FAIL | +5 | **320** |
| V-03 | **PASS** | FAIL | FAIL | FAIL | **PASS** | +10 | **325** |
| V-04 | FAIL | PARTIAL | PARTIAL | **PASS** | FAIL | +10 | **325** |
| V-05 | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | +25 | **340** |

**Rank:** V-05 > V-03 = V-04 > V-01 = V-02

**All essential pass:** Yes (C-01–C-05 pass in all five variations)

---

## Excellence Signals from V-05

**1. Verbatim-block recurrence converts INERTIA-GATE from semantic to structural**
The INERTIA-GATE template (with visual border box) must be reproduced verbatim at Steps 4, 4b, and 7. A missing block is a structurally absent section — visible in a single scan — not a sentence that's shorter than expected. V-01 established that pre-role placement matters; V-05 confirms that recurrence form is equally load-bearing. A recalled sentence ("Recall: inertia is a co-equal option") is compressible; a required output artifact is not.

**2. Slot architecture as universal decision-site pattern**
V-05 extends the pre-printed slot from calibration-only (C-57 minimum) to all closed-set decision sites: schema commitment, null cases, empty-type rows, and the confirmation gate. Every site where a model might silently omit or paraphrase is converted to a fill-in slot. The uncompleted slot is structurally visible; the omitted conditional branch is not.

**3. FAIL example is the load-bearing variable in register discrimination**
V-03 and V-05 both name the degenerate register ("Step-description narrative — FAIL") with concrete examples at every narrative site. The key finding from V-03's single-axis test: PASS-example-only gates can pass a step-description narrative that occupies the correct slot. FAIL examples make the wrong register feel like a category error because the model can pattern-match its output against the named degenerate form before advancing.

**4. WHY clauses front-loaded at every step prevent mechanical table generation**
V-05 is the only variation with "This step exists so that..." on every step. The rationale clause appears before the output specification, establishing the purpose the output must serve before the model encounters the table template. This converts steps from mechanical format requirements into purposeful analytical actions. V-04 partially explored this with a single step; V-05 demonstrates the full-coverage version.

**5. Additive independence of three failure modes**
V-05's 340/340 confirms the hypothesis from V-05's framing: preamble-level bias (C-56), slot-level enforceability (C-57), and narrative-level register discrimination (C-58) are independent failure modes that require independent solutions. V-01 solving C-56 alone reaches 320. V-03 solving C-53+C-58 reaches 325. V-05 combining all three plus C-55 reaches 340. No single-axis variation reaches the combined score.

---

```json
{"top_score": 340, "all_essential_pass": true, "new_patterns": ["Verbatim-block recurrence as required output artifact: INERTIA-GATE missing = structurally absent section, not shorter sentence", "Pre-printed slot architecture generalized from calibration-only to all closed-set decision sites — omission becomes uncompleted fill-in, not silent skip", "FAIL example is load-bearing in register discrimination: naming degenerate register makes wrong output a category error rather than mild formatting miss"]}
```
