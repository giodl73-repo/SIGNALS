## discover-competitors-alt — Scorecard R1

### Per-Criterion Evaluation

**V-01 — Competitor-Zero Table**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 inertia assessed first | PASS | "Competitor 0 is always the inertia competitor... Inertia must appear as the first row" — structural first-row rule |
| C-02 focus woven not appended | PASS | Focus becomes a column in the same table; explicit rule: "Do not add a trailing section for the focus content — it lives in the column" |
| C-03 threat level per competitor | PASS | Every row has a required Threat field; "No competitor appears without HIGH, MEDIUM, or LOW" |
| C-04 whitespace identified | PASS | Required WHITESPACE finding labeled `**WHITESPACE:**` in FINDINGS section |
| C-05 auto-detect without prompting | PASS | "Do not ask the user for the topic or competitor names. Infer from what you find." |
| C-06 inertia stickiness reasoning | PASS | "Switching cost / habit lock-in column is required for all rows — name the mechanism, not a label" including Competitor 0 row |
| C-07 web-verified competitive claim | FAIL | WebSearch instruction is in table Rules block but not procedurally gated — unguided; model may or may not call WebSearch |
| C-08 AMEND 3 actionable adjustments | PASS | Exactly 3 AMEND entries; each names what user changes and what changes in output |
| C-09 cross-dimensional whitespace | PARTIAL | "at least one finding must reference both... a gap that neither... alone would surface" — requires both but does not apply the exclusion test ("cannot be produced by dropping focus") |
| C-10 grounded findings | PARTIAL | "Each finding must name at least one competitor row by label" — positive instruction exists but no prohibition on findings that satisfy by accident |

Essential pass: 5/5 | Recommended pass: 2/3 | Aspirational pass: 1/2 (0.5+0.5)

Composite = (5/5 × 60) + (2/3 × 30) + (1/2 × 10) = 60 + 20 + 5 = **85**

---

**V-02 — Focused Map Table + Grounded Findings List**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 inertia assessed first | PASS | "Inertia... is always the first row" structural rule; Row 0 template in table header |
| C-02 focus woven not appended | PASS | Focus column in MAP table; "This is the only place focus content appears — do not add a trailing focus analysis section" |
| C-03 threat level per competitor | PASS | "Column 4 (threat) is required for every row. Use H, M, or L." |
| C-04 whitespace identified | PASS | WHITESPACE is required numbered finding #1 with labeled format |
| C-05 auto-detect without prompting | PASS | "Do not ask the user to name competitors or supply the domain." |
| C-06 inertia stickiness reasoning | PARTIAL | "Why that threat level" column requires a mechanism but Row 0 has no inertia-specific prompt; model may produce generic switching-cost language |
| C-07 web-verified competitive claim | PASS | "Run WebSearch on at least one external competitor... before populating their row. Inline the citation." Procedurally gated before MAP completion |
| C-08 AMEND 3 actionable adjustments | PASS | 3 AMEND entries; each specifies what user changes and what output changes |
| C-09 cross-dimensional whitespace | PARTIAL | CROSS-DIMENSIONAL finding requires citing both columns but does not require the finding to be unreachable without both — citation condition, not exclusion condition |
| C-10 grounded findings | PASS | "Findings that do not reference a MAP row are prohibited" — explicit prohibition |

Essential pass: 5/5 | Recommended pass: 2.5/3 (PARTIAL = 0.5) | Aspirational pass: 1.5/2

Composite = (5/5 × 60) + (2.5/3 × 30) + (1.5/2 × 10) = 60 + 25 + 7.5 = **92.5**

---

**V-03 — Lifecycle Phases**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 inertia assessed first | PASS | Phase 2 (Assess Inertia) is a named phase that must complete before Phase 3 (external competitors) — phase gating enforces ordering |
| C-02 focus woven not appended | PASS | "Focus lens (if active): apply the focus dimension to this competitor's row... Integrate this analysis into the inertia row — do not reserve it for a later section" |
| C-03 threat level per competitor | PASS | "Every competitor must have an explicit threat level" in Phase 3 rules |
| C-04 whitespace identified | PASS | Phase 4 requires WHITESPACE finding labeled `WHITESPACE:` |
| C-05 auto-detect without prompting | PASS | Phase 1 explicit: "Do not ask the user to supply the domain, topic, or competitor names." |
| C-06 inertia stickiness reasoning | PASS | Phase 2 requires: "Mechanism: Name the specific switching cost, habit lock-in, or workaround satisfaction... One sentence." |
| C-07 web-verified competitive claim | PASS | Phase 3 gate: "Use WebSearch to verify at least one external competitor characterization. Add inline citation to that row." |
| C-08 AMEND 3 actionable adjustments | PASS | Phase 5 has exactly 3 numbered adjustments; each names both the change and the output delta |
| C-09 cross-dimensional whitespace | FAIL | Phase 4 CROSS-DIMENSIONAL requirement says "cannot be produced by dropping the focus input" is stated but it is a description not an exclusion test; FAIL because the criterion requires the finding to be demonstrably unreachable without both dimensions |
| C-10 grounded findings | PASS | "Each finding must name at least one entry from Phase 2 or Phase 3... No free-floating findings." |

Essential pass: 5/5 | Recommended pass: 3/3 | Aspirational pass: 1/2 (C-09 FAIL, C-10 PASS)

Composite = (5/5 × 60) + (3/3 × 30) + (1/2 × 10) = 60 + 30 + 5 = **95**

---

**V-04 — Conversational Register**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 inertia assessed first | PARTIAL | "Begin with the status quo" is a suggestion; no structural first-row rule — model may embed inertia mid-narrative |
| C-02 focus woven not appended | PASS | "Don't save the focus content for a separate section at the end — weave it into each competitor as you go" |
| C-03 threat level per competitor | PASS | "For each one, give a threat level" stated per competitor |
| C-04 whitespace identified | PARTIAL | "The most important finding is the whitespace" — nudge without a required label; criterion requires "stated in its own finding or clearly labeled" |
| C-05 auto-detect without prompting | PASS | "Don't ask the user to tell you the topic or name any competitors — infer it all." |
| C-06 inertia stickiness reasoning | PASS | "Say in one sentence *why* it's sticky: what switching cost, habit, or workaround satisfaction keeps users there." |
| C-07 web-verified competitive claim | FAIL | "Use WebSearch to verify at least one claim" exists but conversational register makes it easy to skip; no procedural gate |
| C-08 AMEND 3 actionable adjustments | PASS | "Give the user exactly three ways to adjust" with "what the user changes and what changes in the output" |
| C-09 cross-dimensional whitespace | FAIL | "try to surface a finding that only exists because both... are in play" — aspirational language, not required |
| C-10 grounded findings | FAIL | "each one should reference a specific competitor by name" — suggestion without prohibition; no citation rule |

Essential pass: 4/5 (C-01 PARTIAL=0.5, C-04 PARTIAL=0.5) | Recommended pass: 2/3 | Aspirational pass: 0/2

Composite = (4/5 × 60) + (2/3 × 30) + (0/2 × 10) = 48 + 20 + 0 = **68**

All essential pass? **No** — C-01 and C-04 are PARTIAL. Not golden.

---

**V-05 — Combined**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 inertia assessed first | PASS | Phase 2 is a named phase for inertia assessment; Phase 3 table has Competitor 0 as first row from Phase 2 output; doubly enforced |
| C-02 focus woven not appended | PASS | FOCUS column in Phase 3 MAP; "Do not add a trailing section for focus content"; focus applied in Phase 2 with Competitor 0 |
| C-03 threat level per competitor | PASS | "Every row must have a threat level. No row appears without H, M, or L." |
| C-04 whitespace identified | PASS | Phase 4 requires labeled WHITESPACE finding; required block |
| C-05 auto-detect without prompting | PASS | Phase 1 explicit: "Infer the topic. Do not ask." |
| C-06 inertia stickiness reasoning | PASS | Phase 2 explicit: "name the specific switching cost, habit lock-in, or workaround satisfaction. Not just 'inertia is high.'" |
| C-07 web-verified competitive claim | PASS | Phase 3 gate + print: "Verify with WebSearch. Inline citation... Phase 3 complete. Web-verified: {name}" |
| C-08 AMEND 3 actionable adjustments | PASS | Phase 5 has exactly 3 numbered adjustments; each specifies what the user changes and what changes in the output |
| C-09 cross-dimensional whitespace | PASS | "must cite at least one competitor row and at least one focus column entry. It cannot be produced by dropping the focus input." — exclusion test present |
| C-10 grounded findings | PASS | "Free-floating findings that do not cite a table row are prohibited." — prohibition framing |

Essential pass: 5/5 | Recommended pass: 3/3 | Aspirational pass: 2/2

Composite = (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = **100**

---

### Composite Ranking

| Variation | Essential | Recommended | Aspirational | Composite | Golden | Grade |
|-----------|-----------|-------------|--------------|-----------|--------|-------|
| V-05 Combined | 5/5 | 3/3 | 2/2 | **100** | Yes | Exceptional |
| V-03 Lifecycle Phases | 5/5 | 3/3 | 1/2 | **95** | Yes | Exceptional |
| V-02 Focused Map+Findings | 5/5 | 2.5/3 | 1.5/2 | **92.5** | Yes | Strong |
| V-01 Competitor-Zero Table | 5/5 | 2/3 | 1/2 | **85** | Yes | Strong |
| V-04 Conversational Register | 4/5 | 2/3 | 0/2 | **68** | No | Below bar |

---

### Excellence Signals from V-05

**1. Layered enforcement via phase + table schema.** When inertia-first ordering is enforced by *both* a named phase (Phase 2 must complete before Phase 3) *and* a structural table position (Competitor 0 is the first row from Phase 2), C-01 becomes structurally unavoidable rather than instruction-dependent. Single-layer enforcement (V-01 table-only or V-03 phase-only) is weaker than both together.

**2. Prohibition framing beats positive instruction for C-10.** "Free-floating findings that do not cite a table row are prohibited" (V-05) is more reliable than "each finding must name at least one competitor row by label" (V-01). The prohibition eliminates the escape hatch — a finding cannot accidentally satisfy a positive rule but it cannot accidentally satisfy a prohibition.

**3. The exclusion test is the load-bearing condition for C-09.** "Cannot be produced by dropping the focus input" is what separates a PASS from a PARTIAL on cross-dimensional whitespace. Citation requirements (V-02: cite both columns) are necessary but not sufficient — a model can cite both columns without the finding being genuinely cross-dimensional. The exclusion condition forces the model to verify the finding's dependence on both inputs.

**4. Token anchors create lightweight commit checkpoints.** `C0: {name}`, `C0-ASSESS: Threat=..., Mechanism=...`, and phase-completion print statements (`Phase 2 complete...`) create traceable intermediate outputs without full ledger machinery. These make it hard to skip a phase silently — the missing token is visible in the output.

**5. Conversational register (V-04) reliably degrades structural criteria.** Soft language ("begin with," "try to surface," "should reference") causes C-01, C-04, C-07, C-09, and C-10 to degrade from PASS to PARTIAL or FAIL. This confirms that structural position and prohibition language — not linguistic register — are the reliable load-bearing elements for rubric compliance.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Layered enforcement via named phase plus structural table position is more reliable than single-layer enforcement for inertia-first ordering", "Prohibition framing (free-floating findings prohibited) is more reliable than positive instruction framing (must name a row) for grounding findings", "The exclusion test (cannot be produced by dropping focus input) is the load-bearing condition for cross-dimensional whitespace — citation requirements alone are insufficient", "Token anchors create lightweight commit checkpoints that make silent phase-skipping visible in output", "Conversational register reliably degrades structural criteria — soft language produces PARTIAL where hard structural rules produce PASS"]}
```
