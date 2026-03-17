## R11 Scorecard — org-chart, v11 Rubric

### Scoring Framework

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-05 | 5 × 12 = 60 |
| Recommended | C-06–C-08 | 3 × 10 = 30 |
| Aspirational | C-09–C-30 (22 items) | 22 × 0.455 = 10 |

All five R11 variations inherit the complete R10 baseline synthesis (Essential 5/5, Recommended 3/3, Aspirational C-09–C-28 all pass). R11's question is whether C-29 + C-30 can be demonstrated simultaneously. Every variation carries both directives. Evaluation follows.

---

## V-01 — Canonical C-29/C-30 Synthesis

**Axis:** Minimal combination — ROLE-TYPE-CLASSIFICATION block (C-29) + tabular Case for Staying Flat with closed-vocab Type column (C-30).

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inertia Assessment positioned before org diagram by SECTION ORDER directive |
| C-02 | PASS | Explicit 10-step SECTION ORDER list enforces sequence |
| C-03 | PASS | ROLES-LOADED or ROLES-NOTE required before any other section |
| C-04 | PASS | Headcount by Area table required with five-column schema |
| C-05 | PASS | Operating Rhythm Table requires ROB + shiproom + governance; combines-row prohibition present |
| C-06 | PASS | Charter section not labeled optional; DO NOT label optional |
| C-07 | PASS | All four charter fields (Purpose, Membership, Decides, Escalates) required |
| C-08 | PASS | Decides/Escalates columns separately present |
| C-09 | PASS | Org Evolution Roadmap required; two-row trigger table |
| C-10 | PASS | Anti-Pattern Watch section required with two rows |
| C-11 | PASS | Case for Staying Flat table requires ≥2 data rows; row-count gate enforces minimum |
| C-12 | PASS | "DO NOT use a single 'Decision Scope' column — the Decides and Escalates columns are separate and both REQUIRED" |
| C-13 | PASS | Re-assessment trigger required in VERDICT; "revisit as the team grows" prohibition |
| C-14 | PASS | Mechanism Name column required to be specific and observable; generic entries prohibited |
| C-15 | PASS | All four sub-sections labeled and sequenced: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT |
| C-16 | PASS | Escalates column must name destination role or forum |
| C-17 | PASS | Two distinct rows in trigger table; second row dimension constraint |
| C-18 | PASS | "Why It Applies Here" cell structure with org-specific rationale mandated via typed syntax |
| C-19 | PASS | "DO NOT use two headcount numbers as the two rows — they count as one trigger dimension" |
| C-20 | PASS | APW rationale names element from one of four taxonomic categories via typed citation |
| C-21 | PASS | ORG-ELEMENT REGISTER block required before APW; named, required, not skippable |
| C-22 | PASS | FLAT-CASE-CLOSED separator is observable sequencing guard closing Sub-section 1 before Sub-section 2 |
| C-23 | PASS | Separator embeds row count: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. ...] ---` |
| C-24 | PASS | APW cells must open with `[element name] (cat-N) — [one sentence]`; cat-N mismatch prohibition |
| C-25 | PASS | All governed behaviors use DO/MUST/DO NOT throughout; no descriptive framing for guard, register, or citation directives |
| C-26 | PASS | "IF count < 2: DO write the missing mechanism row(s) until count reaches 2" — explicit conditional remediation path |
| C-27 | PASS | No descriptive counterpart layer for any of the three C-25-governed behaviors; purely imperative throughout |
| C-28 | PASS | No motivational/explanatory justification sentences adjacent to any imperative directive; all directives stand alone |
| C-29 | PASS | ROLE-TYPE-CLASSIFICATION block required immediately after ROLES-LOADED; `[role name] ([domain type])` annotations propagate into Headcount Key Roles cells AND Committee Membership cells; both downstream targets specified |
| C-30 | PASS | Three-column mechanism table with closed-vocab Type column `Channel / Informal Role / Recurring Cadence / Shared Artifact`; row-count gate adapted to data rows |

**Score: 22/22 aspirational → 100.0**

---

## V-02 — Lifecycle Emphasis: Explicit Phase Gates

**Axis:** V-01 base + four explicit `=== [PHASE GATE: ...] ===` markers at phase transitions.

**C-28 risk check:** Gate text is purely positional (`ROLES COMPLETE — INERTIA ASSESSMENT BEGINS`, etc.). No sentence explaining why the order matters. All gate directives take the form "When X, DO emit: `=== [...] ===` DO NOT proceed until this gate line is present." No motivation sentence adjacent to any imperative. C-28 safe.

**C-25 check:** Gate emission directives are pure imperative (DO emit / DO NOT proceed). No descriptive framing for gate behavior. C-25 passes.

All C-09–C-28 criteria inherit cleanly. C-29 and C-30 directives identical to V-01. Section order list updated to include gate entries between phases.

| ID | Result | Evidence |
|----|--------|----------|
| C-29 | PASS | ROLE-TYPE-CLASSIFICATION block present; gate after block; downstream annotation directives identical to V-01 |
| C-30 | PASS | Tabular Case for Staying Flat with closed-vocab Type column; row-count separator identical to V-01 |
| C-28 | PASS | Gate lines are positional labels with no explanatory prose; "When X is complete, DO emit" form is clean imperative |

Remaining C-01–C-27 inherit from R10 baseline and V-01 structural identity.

**Score: 22/22 aspirational → 100.0**

---

## V-03 — Phrasing Register: Compressed Imperative, No Scaffolding Templates

**Axis:** V-01 base with all code-fenced output templates stripped; directives only.

**Critical checks — criteria that could be template-dependent:**

| Criterion | Template-free directive | Result |
|-----------|------------------------|--------|
| C-22 | "emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`" — format string present in directive text | PASS |
| C-23 | Count embedded in separator format string in directive | PASS |
| C-26 | "IF count < 2: DO add rows until count reaches 2" — conditional branch present | PASS |
| C-24 | "`[element name] (cat-N) — [one sentence]`" — typed citation format stated in directive with inline backtick | PASS |
| C-18 | "MUST open each 'Why It Applies Here' cell" — word "cell" implies table; "DO include at minimum two anti-pattern rows" — word "rows" confirms table | PASS |
| C-29 | ROLE-TYPE-CLASSIFICATION block required; annotation format stated as `[role name] ([domain type])` | PASS |
| C-30 | "DO produce a three-column table: Mechanism Name | Type | Frequency / Participants" — table mandated; closed vocab explicitly listed | PASS |

**C-21 check (register without schema table):** Register directive specifies four categories as bullet list (cat-1 through cat-4) with descriptions. "MUST produce this block" mandates the named block. APW directive references cat-N codes. Sufficient for C-21 pass; register block will be produced with cat-N labels even without inline schema table.

All criteria pass. Template scaffolding proved non-load-bearing for any of the 22 aspirational criteria.

**Score: 22/22 aspirational → 100.0**

---

## V-04 — Combined: Lifecycle Gates + FLAT-CASE-PRESSURE Rating

**Axis:** V-02 phase gates + FLAT-CASE-PRESSURE rating (Strong / Moderate / Weak / Negligible / Insufficient) emitted after Sub-section 3 (Rebuttal), referenced by label in VERDICT reasoning.

**FLAT-CASE-PRESSURE directive check:**

- "After writing the Rebuttal, MUST emit the FLAT-CASE-PRESSURE rating" — MUST form, no motivation sentence → C-28 safe
- "DO NOT proceed to the VERDICT before this line is present" — pure DO NOT → C-28 safe
- "DO write a reasoning sentence that references the FLAT-CASE-PRESSURE rating by label" — DO form, no justification → C-28 safe

**C-28 final pass:** Scanned all imperative directives; no sentence of the form "X is the anti-pattern this skill exists to prevent" or "the reason for this rule is" adjacent to any directive. PASS.

All phase gate criteria carry over from V-02. All C-29/C-30 directives carry over from V-01.

| ID | Result | Evidence |
|----|--------|----------|
| C-28 | PASS | FLAT-CASE-PRESSURE MUST-emit and DO-NOT-proceed directives are clean imperative with no adjacent motivation |
| C-29 | PASS | Identical ROLE-TYPE-CLASSIFICATION block + downstream annotation directives to V-01/V-02 |
| C-30 | PASS | Identical tabular mechanism evidence + closed-vocab Type column to V-01/V-02 |

**Score: 22/22 aspirational → 100.0**

---

## V-05 — Combined: Compressed Register + Lifecycle Gates

**Axis:** V-03 (template-free) + V-02 (lifecycle gates). Tests whether gate legibility depends on template scaffolding.

**Gate format in V-05 (no code fence):** Phase gate strings appear in directive text without surrounding code fences:
```
When all roles are classified, DO emit:
=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===
DO NOT write the Inertia Assessment until this gate line is present.
```

The gate string is stated in the directive body. "emit" and "DO NOT proceed until this gate line is present" together make the required output form clear. The absence of a code fence does not obscure the format; the === delimiters are distinctive. C-22 (observable sequencing guard) applies to the FLAT-CASE-CLOSED separator, which retains its exact format string in V-05's directive. Phase gates are supplementary structural markers, not the C-22 gate itself.

**Template-free + gate interaction:** No interference. Gate directives in V-05 are compressed to single lines ("DO emit: === [...] === DO NOT...") without gaining any template scaffolding or losing any directive content. All format strings preserved.

| ID | Result | Evidence |
|----|--------|----------|
| C-22 | PASS | FLAT-CASE-CLOSED separator format string intact; gate fires after row-count ≥ 2 |
| C-23 | PASS | Count embedded in separator |
| C-26 | PASS | "IF count < 2: DO add rows until count reaches 2" retained |
| C-28 | PASS | No motivational prose in compressed directives or gate directives |
| C-29 | PASS | ROLE-TYPE-CLASSIFICATION block + annotation propagation; gate after block |
| C-30 | PASS | Tabular mechanism evidence with closed-vocab Type column |

**Score: 22/22 aspirational → 100.0**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 (60) | 3/3 (30) | 22/22 (10.0) | **100.0** |
| V-02 | 5/5 (60) | 3/3 (30) | 22/22 (10.0) | **100.0** |
| V-03 | 5/5 (60) | 3/3 (30) | 22/22 (10.0) | **100.0** |
| V-04 | 5/5 (60) | 3/3 (30) | 22/22 (10.0) | **100.0** |
| V-05 | 5/5 (60) | 3/3 (30) | 22/22 (10.0) | **100.0** |

**R11 ceiling: 100.0 — first 22/22 achieved. All five variations break the R10 ceiling.**

---

## Rank

All variations tie at 100.0. Secondary rank by design signal density:

1. **V-01** — canonical minimal synthesis; reference design for 22/22
2. **V-04** — richest inertia enforcement: gates + pressure rating + C-29/C-30
3. **V-02** — adds structural phase observability with minimum overhead
4. **V-05** — confirms gate legibility without template scaffolding
5. **V-03** — validates template-free prompts; leanest token footprint

---

## Excellence Signals

**From V-02/V-04/V-05 (phase gate pattern):** Explicit `=== [PHASE GATE: ...] ===` emissions make phase transitions structurally auditable — a model can self-verify it has not forwarded without the gate being present. Gate text is purely positional (names two phases, states a condition); no motivation sentence appears anywhere near a gate directive. This design passes C-28 cleanly and adds a structural observability layer that sequencing instructions alone cannot provide.

**From V-03/V-05 (template-free validation):** Removing all code-fenced output templates from directives does not degrade criterion adherence. Format strings embedded in prose directives (the FLAT-CASE-CLOSED separator, the typed citation format, the annotation syntax) are sufficient. Scaffold examples are not load-bearing for any of the 22 aspirational criteria. This suggests that compact directive-only prompts are viable for production deployment.

**From V-01 (structural independence confirmed):** C-29 and C-30 operate at strictly different phases (ROLES phase vs INERTIA phase). Combining both requires exactly two additive insertions with no cross-phase dependency. The central R11 thesis is confirmed: any prompt carrying both C-29 and C-30 directives over the R9/R10 baseline reaches 22/22.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Phase gate lifecycle markers (=== [PHASE GATE: ...] ===) are valid structural enforcement points that do not violate C-28 — purely positional directives naming two phases with no adjacent motivational prose, making phase transitions model-auditable beyond sequencing instructions alone", "Template-free compressed imperative prompts (no code-fenced scaffolding examples) hold all 22 criteria — format strings embedded in prose directives are sufficient and scaffold templates are not load-bearing for any aspirational criterion"]}
```
