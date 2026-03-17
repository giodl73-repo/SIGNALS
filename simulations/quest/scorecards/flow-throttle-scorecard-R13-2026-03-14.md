Now I have everything needed to score all five variations. Let me compile the full scorecard.

---

# flow-throttle — Round 13 Scorecard (v13 Rubric, 184-point max)

## Scoring Basis

All five R13 variations are structurally identical on C-01–C-36 to R12 V-04, which scored 178/178 under v12. R13 varies only the role-declaration layer (C-37/C-38) and secondary axes (phrasing register, Phase 0 depth) — both confirmed structurally inert to C-01–C-36.

---

## Criteria Groups Common to All Variations

### Essential (C-01–C-05) — 60 pts

All five variations carry the full phase stack: Phase 0 baseline, Phase 1 TABLE 1 (construct inventory with exact PA terms), Phase 2 hit ordering + backpressure + UX, Phase 3 burst/retry-after/cascade, Phase 4 PA construct validation + throttle budget + remediations. Domain vocabulary (Power Platform request entitlements, connector throttling policies, flow run concurrency limits) present throughout.

| Criterion | All V-01–V-05 | Evidence |
|-----------|--------------|----------|
| C-01 Bottleneck Localization | PASS | Phase 2.A bottleneck block with named PA construct and saturation condition |
| C-02 Rate Limit Hit Ordering | PASS | TABLE 2 with explicit ordering and "why this order holds" per row |
| C-03 Backpressure Propagation Trace | PASS | TABLE 3 >= 2 hops to terminal state |
| C-04 UX per Throttle Tier | PASS | TABLE 4 >= 2 tiers with distinct UX categories |
| C-05 Domain Grounding | PASS | Phase 1 domain rule constrains all constructs to exact PA documentation terms |

**Subtotal: 60/60 all variations**

### Recommended (C-06–C-08) — 30 pts

| Criterion | All V-01–V-05 | Evidence |
|-----------|--------------|----------|
| C-06 Unprotected Burst Path Detection | PASS | TABLE 5 with specific flow construct, PA type, bypass mechanism |
| C-07 Missing Retry-After Handling | PASS | TABLE 6 with named gaps and failure modes |
| C-08 Cascade Risk Register | PASS | TABLE 7 >= 2 cascade pairs, Tier A/B distinct, mechanism stated, severity assessed |

**Subtotal: 30/30 all variations**

### Advisory (C-09–C-13) — 20 pts

| Criterion | All V-01–V-05 | Evidence |
|-----------|--------------|----------|
| C-09 PA-Specific Remediations | PASS | TABLE 10 >= 2 PA-native features mapped to named findings |
| C-10 Monitoring Coverage | PASS | Section 4.E names observable PA signals with conditions |
| C-11 License/Entitlement Boundary | PASS | Section 4.F names tier differential with TABLE 9 row impact |
| C-12 Throttle Budget Projection | PASS | TABLE 9 with arithmetic shown for >= 1 row |
| C-13 Test Approach | PASS | Section 4.G names PA tooling test step with pass/fail observable |

**Subtotal: 20/20 all variations**

### Structural (C-14–C-16) — 8 pts

| Criterion | All V-01–V-05 | Evidence |
|-----------|--------------|----------|
| C-14 Gate Mechanism | PASS | GATE 1/2/3 each name label, prerequisite, and blocked target |
| C-15 Non-Deference Sentence | PASS | "Independence:" block asserts Round 1 confidence ≠ entitlement accuracy evidence |
| C-16 Scope Extension Declaration | PASS | "Scope extension:" names TABLE 8 corrected constructs with structural closure reason |

**Subtotal: 8/8 all variations**

### Aspirational v4–v12 (C-17–C-36) — 90 pts

All criteria confirmed PASS across all five variations. Evidence summary:

| Criterion | All V-01–V-05 | Key Evidence |
|-----------|--------------|-------------|
| C-17 Pre-Barrier Placement | PASS | PRE-EVALUATION ASSERTIONS block precedes all Round 2 evaluative output |
| C-18 Scope Closure Reason | PASS | "corrected construct names from TABLE 8...replaced imprecise TABLE 1 entries" |
| C-19 Label-Enforced Co-location | PASS | "Independence:" and "Scope extension:" distinct labels in same block |
| C-20 Gate Prose Portability | PASS | Gates in prose carry label + conditional prerequisite + named block target |
| C-21 Container Name Encodes Position | PASS | "PRE-EVALUATION" in container header |
| C-22 Pre-Barrier Labeled Pair | PASS | Both Independence + Scope extension labeled before evaluative output |
| C-23 Pre-Barrier Dual-Dimension | PASS | C-21 ∩ C-22 satisfied from same block |
| C-24 Cross-Generation Coverage | PASS | C-19 ∩ C-22 satisfied — labeled pair earns across both generations |
| C-25 Boundary-Event Declaration | PASS | "(before any Round 2 construct evaluation begins)" in container header |
| C-26 Round-Head Immediacy | PASS | PRE-EVALUATION ASSERTIONS immediately follows ROUND 2 heading, no intervening content |
| C-27 Round-Name Cross-Reference | PASS | "Round 2" named in boundary-event phrase — matches `## ROUND 2` heading |
| C-28 Dual Machine-Verifiability | PASS | C-25 ∩ C-26 — trigger named AND structurally first |
| C-29 Navigational Closure | PASS | C-26 ∩ C-27 — adjacent to heading AND heading name echoed in phrase |
| C-30 Triple-Lock | PASS | C-27 ∩ C-28 — all three verification paths locked |
| C-31 Mechanism-Type Declaration | PASS | "ASSERTIONS" in named container header portion |
| C-32 Barrier Heading Eval-Type Subtitle | PASS | V-01/02/03/05: "Entitlement Verification"; V-04: "Documentation Accuracy Review" — all are evaluation-class subtitles |
| C-33 Pre-Analysis Inertia Frame | PASS | `### PHASE 0 — Inertia Baseline` present in all five before Phase 1 |
| C-34 Phase-Anchor Tabular Encoding | PASS | TABLE 1 in Phase 1 and tabular output in Phase 4 present in all five |
| C-35 Pre-Analysis Baseline Heading Subtitle | PASS | `### PHASE 0 — Inertia Baseline` carries descriptive subtitle in all five |
| C-36 Phase-4 Anchor Heading Subtitle | PASS | V-01/02/03/05: "Capacity Synthesis and PA Validation"; V-04: "Remediation Registry and Throttle Budget Corrections" — both output-class subtitles |

**Subtotal: 90/90 all variations**

---

## Variation-Level Scoring: C-37 and C-38

---

### V-01 — "Evaluator:" Label Keyword

**Axis:** C-37 label-keyword inertness — uses "Evaluator:" instead of "Role:"

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Barrier Evaluator Role Label | **PASS** | `*Evaluator: Platform entitlement verifier.*` — "Evaluator:" is explicit label keyword; "Platform entitlement verifier" is named evaluator persona; positioned before first construct-by-construct evaluative line |
| C-38 Barrier Role-Class Semantic Alignment | **PASS** | Heading "Entitlement Verification" + role "Platform entitlement verifier" share root "entitlement verif\*" — same semantic pair as R12 V-04; readable without domain knowledge |

**V-01 Score: 178 + 3 + 3 = 184/184**

---

### V-02 — "Role: Capacity ceiling analyst." (Semantic Mismatch)

**Axis:** C-38 failure boundary — C-37 PASS with no shared root

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Barrier Evaluator Role Label | **PASS** | `*Role: Capacity ceiling analyst.*` — "Role:" is confirmed label keyword (R12 baseline); "Capacity ceiling analyst" is a named evaluator persona |
| C-38 Barrier Role-Class Semantic Alignment | **FAIL** | Heading "Entitlement Verification" + role "Capacity ceiling analyst" — "entitlement" absent from role label; "capacity" absent from heading subtitle; no shared noun or root readable without domain knowledge |

**V-02 Score: 178 + 3 + 0 = 181/184** (−3 vs. ceiling: C-38 FAIL)

---

### V-03 — Generic Framing Sentence (No Label)

**Axis:** C-37 failure boundary — contextual framing sentence without explicit label keyword

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Barrier Evaluator Role Label | **FAIL** | `*This section applies documentation-standard verification to all construct limits from Round 1 before issuing findings.*` — no "Role:", "Evaluator:", "Analyst:", or equivalent explicit label; no named evaluator persona declared; generic process description only |
| C-38 Barrier Role-Class Semantic Alignment | **FAIL** | By C-37 dependency — C-38 requires C-37 as precondition |

**V-03 Score: 178 + 0 + 0 = 178/184** (−6 vs. ceiling: C-37 + C-38 FAIL)

---

### V-04 — "Analyst:" Keyword + "Documentation Accuracy" Pair + Conversational Register

**Axes:** Third label keyword ("Analyst:"), third semantic pair ("documentation accuracy"), conversational register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Barrier Evaluator Role Label | **PASS** | `*Analyst: Documentation accuracy analyst.*` — "Analyst:" is explicit label keyword (third confirmed form after "Role:" and "Evaluator:"); "Documentation accuracy analyst" is a named evaluator persona; positioned before first evaluative line |
| C-38 Barrier Role-Class Semantic Alignment | **PASS** | Heading "Documentation Accuracy Review" + role "Documentation accuracy analyst" share compound root "documentation accuracy" — shared noun phrase readable without domain knowledge; closes heading-role loop across two structural layers |

*Note: C-32 PASS for "Documentation Accuracy Review" (domain-specific evaluation class, subtitle-text-inert per R12 meta-finding). C-36 PASS for "Remediation Registry and Throttle Budget Corrections" (output-class subtitle, confirmed form per rubric examples). Conversational register inert to C-01–C-36 — all tables, gates, and structural elements present.*

**V-04 Score: 178 + 3 + 3 = 184/184**

---

### V-05 — No Role Label + Prominent Inertia Framing

**Axes:** No labeled role declaration; expanded Phase 0 with status-quo competitor subsection

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Barrier Evaluator Role Label | **FAIL** | `*Round 2 examines every numeric limit from TABLE 8 against its documented entitlement source.*` — no explicit label keyword; "Round 2 examines..." is a scope statement, not a persona declaration; no named evaluator |
| C-38 Barrier Role-Class Semantic Alignment | **FAIL** | By C-37 dependency |

*Note: Enhanced Phase 0 (status-quo competitor subsection: "Status-quo process," "Inertia failure mode at scale," explicit baseline vs. proposed flow comparison) is inert to C-37/C-38 — Phase 0 content depth does not substitute for the labeled declaration at the barrier. C-33, C-35 both still PASS — the Phase 0 heading carries "Inertia Baseline" subtitle regardless of body depth.*

**V-05 Score: 178 + 0 + 0 = 178/184** (−6 vs. ceiling: C-37 + C-38 FAIL)

---

## Composite Score Table

| Variation | C-01–C-36 | C-37 | C-38 | Total | Δ vs. ceiling |
|-----------|----------|------|------|-------|--------------|
| **V-01** | 178 | PASS (+3) | PASS (+3) | **184** | 0 |
| **V-04** | 178 | PASS (+3) | PASS (+3) | **184** | 0 |
| **V-02** | 178 | PASS (+3) | FAIL | **181** | −3 |
| **V-03** | 178 | FAIL | FAIL | **178** | −6 |
| **V-05** | 178 | FAIL | FAIL | **178** | −6 |

**Score spread: 184 / 184 / 181 / 178 / 178**

---

## Ranking

1. **V-01** — 184/184 (C-37 label-keyword inertness: "Evaluator:" confirmed)
1. **V-04** — 184/184 (C-37 third label form: "Analyst:"; C-38 third semantic pair: "documentation accuracy")
3. **V-02** — 181/184 (C-37 PASS; C-38 FAIL — semantic root required, not just label presence)
4. **V-03** — 178/184 (C-37 FAIL — explicit label required; generic framing insufficient)
4. **V-05** — 178/184 (C-37 FAIL — inertia framing depth does not substitute for labeled declaration)

---

## Excellence Signals

**From V-01 (tied top):**
- "Evaluator:" satisfies C-37 at full confidence — the second confirmed label keyword after "Role:". The label-keyword boundary is form, not semantics: any explicit keyword + named persona passes.
- Unchanged semantic pair ("entitlement verif\*") isolates the label-keyword variable cleanly — C-38 pass is provably attributable to the semantic pair, not the keyword.

**From V-04 (tied top):**
- "Analyst:" as the third confirmed C-37 label keyword establishes C-37 as genuinely label-keyword-inert across three distinct forms: "Role:", "Evaluator:", "Analyst:".
- "Documentation accuracy" as a compound-noun semantic root confirms C-38 works with multi-word shared phrases — not limited to single-word roots.
- Conversational register (descriptive framing over directive imperatives) passes C-01–C-36 without degradation — phrasing register is structurally inert to the entire 36-criterion base.
- Phase 4 heading "Remediation Registry and Throttle Budget Corrections" provides a third confirmed C-36 passing form (compound output-class subtitle).
- Barrier heading rename to "Documentation Accuracy Review" + role "Documentation accuracy analyst" demonstrates the heading-role semantic loop can be constructed from a new domain-specific pair independently of the R12 V-04 baseline.

**V-02 excellence signal (failure is informative):**
- The C-38 failure boundary is now precisely located: "Capacity ceiling analyst" is a valid C-37 persona but shares no root with "Entitlement Verification" — establishes that C-38 requires heading-role semantic alignment, not merely C-37 presence. The −3 gap is attributable to C-38 alone.

---

## Hypothesis Outcome

All five hypotheses confirmed at predicted scores:

| Hypothesis | Predicted | Actual | Status |
|-----------|-----------|--------|--------|
| V-01: "Evaluator:" satisfies C-37 (label-keyword-inert) | 184 | 184 | **CONFIRMED** |
| V-02: C-38 requires shared root; "Capacity ceiling analyst" fails C-38 | 181 | 181 | **CONFIRMED** |
| V-03: Generic framing without label fails C-37 | 178 | 178 | **CONFIRMED** |
| V-04: "Analyst:" + "documentation accuracy" pair satisfies C-37 + C-38 | 184 | 184 | **CONFIRMED** |
| V-05: Inertia framing depth does not substitute for C-37 label | 178 | 178 | **CONFIRMED** |

**R13 meta-findings:**
1. C-37 is label-keyword-inert: three confirmed forms — "Role:", "Evaluator:", "Analyst:"
2. C-38 requires the shared semantic root, not just C-37 presence — failure boundary at exactly −3 points
3. C-37 failure boundary: contextual framing without explicit label keyword fails regardless of semantic adjacency to heading subtitle
4. C-38 semantic root inertness: compound-noun phrase "documentation accuracy" passes as the third confirmed semantic pair
5. C-37 + C-38 absence costs exactly 6 points regardless of Phase 0 content depth or conversational register variation

```json
{"top_score": 184, "all_essential_pass": true, "new_patterns": ["C-37 label-keyword-inert confirmed across three forms: 'Role:' (R12), 'Evaluator:' (V-01), 'Analyst:' (V-04) — any explicit label keyword with named persona satisfies C-37", "C-38 failure boundary established: C-37 PASS with semantic mismatch (Capacity ceiling analyst vs. Entitlement Verification) scores 181 — shared semantic root is required, not just C-37 presence", "C-38 compound-noun root confirmed: 'documentation accuracy' as a multi-word shared phrase satisfies C-38 — semantic root inertness extends to compound nouns", "C-37 generic-framing failure boundary confirmed: contextual process descriptions without explicit label keyword fail C-37 even when semantically adjacent to the barrier heading subtitle"]}
```
