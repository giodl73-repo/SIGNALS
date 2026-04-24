## Round 17 Scoring — topic-plan (v16 rubric)

### Criteria Reference

**Essential (C-01–C-05 | 12 pts each | 60 total):** read strategy, read signals, identify delta, type proposals, confirm gate
**Recommended (C-06–C-08 | 10 pts each | 30 total):** evidence citations, before/after view, all three change types
**Aspirational (C-09–C-55 | ~5 pts each | 235 total)**

---

### Common-to-All Assessment

All five variations are complete prompts that inherit from the same strong foundation. Before scoring differentiators, I confirm the following hold for **all five variations**:

| Range | Assessment | Rationale |
|---|---|---|
| C-01–C-05 (Essential) | PASS × 5 | Step 1 reads strategy, Step 3 inventories signals, Step 3b names delta, proposals are typed ADD/REMOVE/REPRIORITIZE, Step 7 gates before write |
| C-06–C-08 (Recommended) | PASS × 3 | Evidence artifacts in proposal columns; Step 6 diff table; explicit no-change rows for all three types |
| C-09–C-18 | PASS × 10 | All have 9-namespace assessment, conflict audit, typed gate verb (YES), no-change rows, inline evidence brackets, anti-pattern checkpoint, namespace enumeration, two-hop traceability, null-conflict declaration, structured delta format |
| C-19–C-32 | PASS × 14 | Diff has Proposal cross-ref column; Delta Finding column; column-completeness declarations; active anti-pattern naming; verbatim null templates; unstated assumption extraction; before/after columns; upfront schema; cascade checkpoints; named role and dimensions; back-fill adjudication; forward-arc columns; inertia disqualification rule; reversibility three-value enum |
| C-33–C-49 | PASS × 17 | Assumption schema in upfront block; prose-prohibition at both declaration sites; operationalized independence test; PASS/FAIL concrete examples; step-level activation cross-ref; null-case as Contract Rule 3; rule-reference annotations in schema; Delta Finding as Rule 4; 4-rule minimum CONTRACT; pre-signal Defense Register; Defense basis column; Signal Read-Lock gate |

---

### Differentiating Criteria — C-43, C-50–C-55

#### C-43 — Cross-rule pass/fail example coverage (all rules must carry symmetric examples)

| Variation | Rule 1 examples | Rule 2 | Rule 3 | Rule 4 | Rating |
|---|---|---|---|---|---|
| V-01 | None (prose-prohibition only, no labeled PASS/FAIL) | PASS/FAIL present | No labeled examples | No labeled examples | **PARTIAL** |
| V-02 | PASS example + FAIL example | PASS/FAIL | Rule 3 symmetry check with PASS/FAIL | Rule 4 symmetry check with PASS/FAIL | **PASS** |
| V-03 | PASS/FAIL pairs | PASS/FAIL | PASS/FAIL | PASS/FAIL | **PASS** |
| V-04 | PASS/FAIL pairs | PASS/FAIL | PASS/FAIL | PASS/FAIL | **PASS** |
| V-05 | PASS/FAIL pairs | PASS/FAIL | PASS/FAIL | PASS/FAIL | **PASS** |

---

#### C-50 — Challenge strength column (Strong/Moderate/Weak, governed by Rule 1)

All 5: **PASS** — "Challenge strength: Strong / Moderate / Weak [Rule 1]" appears in Rule 1 and in the Defender Challenge Table schema in every variation.

---

#### C-51 — Co-equal inertia framing in the preamble

| Variation | Placement | Recurrence | Rating |
|---|---|---|---|
| V-01 | **First line** before role declaration, before any schema | Explicit at proposals, Defender Table, confirmation gate | **PASS** |
| V-02 | After role line ("You are running /topic:plan…"); labeled "(C-51)" | Implicit — not named at key decision steps | **PASS** |
| V-03 | After role line | Once in preamble, once implicitly at proposals | **PASS** |
| V-04 | After role line | Once in preamble | **PASS** |
| V-05 | **First paragraph** before role declaration; "This framing holds at every step" with explicit recurrence named | Explicit at proposals step, Defender Table, confirmation gate | **PASS** |

All 5 pass — preamble framing is present before any step in all variations.

---

#### C-52 — Calibration check after Defender Challenge Table (required output artifact)

| Variation | Mechanism | Rating |
|---|---|---|
| V-01 | Three-branch conditional with quoted verdict strings for each case | **PASS** |
| V-02 | Pre-printed checkbox slot — "select exactly one and write it as output" — with all three strings pre-filled | **PASS** (strongest: unforgeable slot) |
| V-03 | "required output artifact — select and write one" with three conditional branches | **PASS** |
| V-04 | Calibration check with abbreviated verdict strings, labeled "(C-52)" | **PASS** |
| V-05 | "required output artifact — select one and write it" with full three-branch verdicts | **PASS** |

---

#### C-53 — Analytical narrative (2–3 sentences) before each table at Steps 3, 3b, 4, 5, 6

| Variation | Step 3 | Step 3b | Step 4 | Step 5 | Step 6 | Gate enforcement | Rating |
|---|---|---|---|---|---|---|---|
| V-01 | None — steps go directly to tables or anti-pattern checkpoint | None | None | None | None | None | **FAIL** |
| V-02 | None — fill-template format, no narrative slot | None | None | None | None | None | **FAIL** |
| V-03 | None — "This step exists so that…" is a why-clause, not an analytical narrative | None | None | None | None | None | **FAIL** (why-clauses are step rationale, not pre-table analytical conclusions) |
| V-04 | ✓ "Narrative (required before table — 2–3 sentences)" with format spec | ✓ | ✓ | ✓ | ✓ | Phase 1 gate checks Step 3; Phase 3 gate checks Steps 3b/4/5/6 with format validation | **PASS** |
| V-05 | ✓ "Narrative (2–3 sentences before the table)" at Step 3 | ✓ | ✓ | ✓ | ✓ | "[Narrative: conclusion before evidence]" format marker; degenerate form named | **PASS** |

---

#### C-54 — PURPOSE clause on each CONTRACT rule ("This rule exists because…")

All 5: **PASS** — All four rules (1–4) in every variation open with "This rule exists because…" before the constraint specification.

---

#### C-55 — Why clause at the opening of each execution step ("This step exists so that…")

| Variation | Steps with why-clauses | Coverage | Rating |
|---|---|---|---|
| V-01 | Step 3 (Defense Register) only: "This step exists before any delta analysis so that…" | 1 of ~9 steps | **PARTIAL** |
| V-02 | No steps have why-clause openers — all begin with instructions or fill templates | 0 of ~9 | **FAIL** |
| V-03 | Steps 1, 1b, 2, 3, 3b, 4, 4b, 5, 6, 7, 8 all open with "This step exists so that…"; SIGNAL READ-LOCK itself has why-clause | Full coverage | **PASS** |
| V-04 | No steps have why-clause openers — focuses on phase gates and narrative-completeness checks | 0 of ~9 | **FAIL** |
| V-05 | Steps 1, 2, 3, 3b, 4, 4b, 5, 6, 7, 8 all open with "This step exists so that…"; SIGNAL READ-LOCK: "This step exists so that the written inventory is the authoritative closed set" | Full coverage | **PASS** |

---

### Per-Variation Criterion Grids

#### V-01: Inertia Framing

| Criterion | Tier | Result | Evidence |
|---|---|---|---|
| C-01 | essential | PASS | Step 1 reads strategy.md, records STRATEGY DATE |
| C-02 | essential | PASS | Step 2 signal inventory with NEW/PRIOR classification |
| C-03 | essential | PASS | Step 3b delta findings with "Strategy assumed X / Signal revealed Y" |
| C-04 | essential | PASS | Typed ADD/REMOVE/REPRIORITIZE proposals |
| C-05 | essential | PASS | Step 7 gate with "Stop here. Write nothing further until the user replies." |
| C-06 | recommended | PASS | Evidence artifact column in proposals |
| C-07 | recommended | PASS | Step 6 before/after diff table |
| C-08 | recommended | PASS | Explicit null rows for all three change types |
| C-09–C-49 | aspirational | PASS ×39, see note | All base aspirational criteria present |
| C-43 | aspirational | **PARTIAL** | Rule 1 has no labeled PASS/FAIL examples; Rules 3–4 have no labeled pairs → not all rules carry symmetric examples |
| C-50 | aspirational | PASS | Rule 1 lists "Challenge strength: Strong / Moderate / Weak [Rule 1]"; appears in Defender Table schema |
| C-51 | aspirational | PASS | First line of prompt, before role line; recurs explicitly at proposals, Defender Table, and gate |
| C-52 | aspirational | PASS | Three-branch calibration check with quoted verdict strings, labeled "required artifact" |
| C-53 | aspirational | **FAIL** | No pre-table analytical narrative requirement at any of the five analytical steps |
| C-54 | aspirational | PASS | All four rules open with "This rule exists because…" |
| C-55 | aspirational | **PARTIAL** | Only Step 3 (Defense Register) has a why-clause opener; 8 other steps lack it |

**V-01 score:** 325 − 2.5 (C-43 PARTIAL) − 5 (C-53 FAIL) − 2.5 (C-55 PARTIAL) = **315 pts**

---

#### V-02: Output Format (pre-printed template)

| Criterion | Tier | Result | Evidence |
|---|---|---|---|
| C-01–C-05 | essential | PASS × 5 | All essential criteria met |
| C-06–C-08 | recommended | PASS × 3 | Evidence column, diff table, three-type null rows |
| C-09–C-49 | aspirational | PASS ×41 | All base aspirational criteria; Rule 3 and Rule 4 symmetry checks → C-43 PASS |
| C-50 | aspirational | PASS | Rule 1 lists Challenge strength; pre-printed Defender Table template has column slot visible |
| C-51 | aspirational | PASS | Preamble after role line: "Inertia is a co-equal option, not a fallback. (C-51)" |
| C-52 | aspirational | PASS | Pre-printed checkbox slot forces selection of one of three verdict strings → structurally unforgeable |
| C-53 | aspirational | **FAIL** | No narrative requirement before any table; fill-template format goes straight to table rows |
| C-54 | aspirational | PASS | All four rules open with "This rule exists because…" |
| C-55 | aspirational | **FAIL** | No step opens with "This step exists so that…"; all steps begin with instructions or fill notation |

**V-02 score:** 325 − 5 (C-53) − 5 (C-55) = **315 pts**

---

#### V-03: Phrasing Register (explanatory throughout)

| Criterion | Tier | Result | Evidence |
|---|---|---|---|
| C-01–C-05 | essential | PASS × 5 | All essential criteria met |
| C-06–C-08 | recommended | PASS × 3 | Evidence column, diff table, three-type null rows |
| C-09–C-49 | aspirational | PASS ×41 | All base aspirational criteria; all rules have labeled PASS/FAIL pairs → C-43 PASS |
| C-50 | aspirational | PASS | Rule 1 includes Challenge strength in closed enum; present in Defender Table schema |
| C-51 | aspirational | PASS | Preamble after role line: "The result may be zero changes…. Inertia is a co-equal option, not a fallback." |
| C-52 | aspirational | PASS | "required output artifact — select and write one" with three conditional branches |
| C-53 | aspirational | **FAIL** | "This step exists so that…" openers are rationale anchors, not analytical narratives about findings. No "Narrative (2–3 sentences)" instruction before any table. |
| C-54 | aspirational | PASS | All four rules open with "This rule exists because…" |
| C-55 | aspirational | PASS | Every step from Step 1 through Step 8 (including SIGNAL READ-LOCK) opens with "This step exists so that…" |

**V-03 score:** 325 − 5 (C-53) = **320 pts**

---

#### V-04: Lifecycle Emphasis (narrative-forward with phase gates)

| Criterion | Tier | Result | Evidence |
|---|---|---|---|
| C-01–C-05 | essential | PASS × 5 | All essential criteria met |
| C-06–C-08 | recommended | PASS × 3 | Evidence column, diff table, three-type null rows |
| C-09–C-49 | aspirational | PASS ×41 | All base aspirational criteria; all rules have PASS/FAIL pairs → C-43 PASS |
| C-50 | aspirational | PASS | Rule 1 includes Challenge strength; Defender Table schema has column |
| C-51 | aspirational | PASS | Preamble present: "Inertia is a co-equal option, not a fallback." |
| C-52 | aspirational | PASS | Calibration check with three conditional verdicts, labeled "(C-52)" |
| C-53 | aspirational | PASS | "Narrative (required before table — 2–3 sentences)" at Steps 3, 3b, 4, 5, 6. Phase 1 gate checks narrative at Step 3. Phase 3 gate checks Steps 3b/4/5/6 with format validation ("states what was found + why it matters — NOT a description of the step") before advancement |
| C-54 | aspirational | PASS | All four rules open with "This rule exists because…" |
| C-55 | aspirational | **FAIL** | No step opens with "This step exists so that…". PHASE headers and narrative-completeness gates are lifecycle enforcement, not step-level rationale anchoring. The Defense Register step ("Complete before reading any NEW artifact") lacks a why-clause. |

**V-04 score:** 325 − 5 (C-55) = **320 pts**

---

#### V-05: Combined (C-51 + C-53 + C-54 + C-55)

| Criterion | Tier | Result | Evidence |
|---|---|---|---|
| C-01–C-05 | essential | PASS × 5 | All essential criteria met |
| C-06–C-08 | recommended | PASS × 3 | Evidence column, diff table, three-type null rows |
| C-09–C-49 | aspirational | PASS ×41 | All base aspirational criteria; all rules have labeled PASS/FAIL pairs → C-43 PASS |
| C-50 | aspirational | PASS | Rule 1 closes "Challenge strength: Strong / Moderate / Weak"; present in Defender Table schema |
| C-51 | aspirational | PASS | **Opening paragraph before role line**: "Inertia is a co-equal option, not a fallback. The burden of proof rests on change. This framing holds at every step." Explicit recurrence at proposals, Defender Table, and confirmation gate |
| C-52 | aspirational | PASS | "required output artifact — select one and write it" with full three-branch conditional verdicts |
| C-53 | aspirational | PASS | "Narrative (2–3 sentences before the table)" at Steps 3, 3b, 4, 5, 6 with format marker "[Narrative: conclusion before evidence]" and explicit degenerate-form rejection |
| C-54 | aspirational | PASS | All four rules open with "This rule exists because…" with substantive purpose explanations |
| C-55 | aspirational | PASS | Every step (1, 1b→integrated, 2, 3, 3b, 4, 4b, 5, 6, 7, 8) opens with "This step exists so that…"; SIGNAL READ-LOCK itself: "This step exists so that the written inventory is the authoritative closed set" |

**V-05 score:** 325 pts (perfect — all 55 criteria pass)

---

### Composite Scores and Ranking

| Rank | Variation | Score | Threshold gap |
|---|---|---|---|
| 1 | **V-05** — Combined | **325 / 325** | +115 above threshold |
| 2 | **V-03** — Phrasing Register | **320 / 325** | +110 |
| 2 | **V-04** — Lifecycle Emphasis | **320 / 325** | +110 |
| 4 | **V-01** — Inertia Framing | **315 / 325** | +105 |
| 4 | **V-02** — Output Format | **315 / 325** | +105 |

All variations exceed the golden threshold (**≥ 210**).

---

### Excellence Signals — V-05

**What V-05 does that others don't:**

**1. Two-tier explanatory architecture creates redundant compression recovery.** V-03 has step why-clauses but no narrative enforcement. V-04 has narrative enforcement but no step why-clauses. V-05 has both: PURPOSE clauses at the rule level (C-54) and why-clauses at the step level (C-55) mean that even if the constraint specification is absorbed under context pressure, the output shape is recoverable from the stated purpose at two independent levels. Rule-level rationale and step-level rationale are different recovery paths — a model that loses the step specification can recover from the step's why-clause; a model that loses the rule constraint can recover from the rule's purpose.

**2. Rationale anchoring extends to structural gating mechanisms, not just procedural steps.** The SIGNAL READ-LOCK in V-05 carries a why-clause: "This step exists so that the written inventory is the authoritative closed set." The confirmation gate's Step 7 carries: "This step exists so that strategy.md is never modified without explicit user approval at an identifiable gate; auto-application removes the user's ability to catch analytical errors before they become durable changes." Rationale-anchoring gating mechanisms makes them harder to rationalize past under compression — the model must override a stated purpose, not just skip an instruction.

**3. Explicit degenerate-form naming in narrative specification.** V-05's narrative format spec includes "[Narrative: conclusion before evidence]" as an output marker and the degenerate form is named: "Do not describe the conflict audit step." This pattern — state what valid output looks like AND name what invalid output looks like in the same specification — makes the format self-verifiable by the model before producing each table, parallel to how PASS/FAIL examples make Rule 1 self-verifiable.

---

```json
{"top_score": 325, "all_essential_pass": true, "new_patterns": ["Two-tier explanatory architecture: PURPOSE clauses on CONTRACT rules (C-54) and why-clauses on execution steps (C-55) create two independent compression-recovery paths — specification-only degradation is caught by stated rationale at whichever level survives context pressure", "Rationale anchoring on gating mechanisms: applying why-clauses to SIGNAL READ-LOCK and the confirmation gate (not just procedural steps) makes gates harder to rationalize past under compression because the model must override a stated purpose rather than skip an instruction", "Explicit degenerate-form naming in narrative specification: '[Narrative: conclusion before evidence]' marker combined with 'NOT a description of the step' rejection makes narrative format self-verifiable by the model before each table, parallel to PASS/FAIL examples making Rule 1 self-verifiable"]}
```
