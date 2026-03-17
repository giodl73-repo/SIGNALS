## Signal Check — Round 3 Scorecard

**Rubric:** v3 (16 criteria, aspirational denominator = 8)

### Results

| Rank | Variation | Score | Grade | Fails |
|------|-----------|-------|-------|-------|
| 1 (tie) | **V-04** | **100** | A+ | none |
| 1 (tie) | **V-05** | **100** | A+ | none |
| 3 (tie) | V-01 | 97.5 | A | C-15, C-16 |
| 3 (tie) | V-02 | 97.5 | A | C-13, C-16 |
| 3 (tie) | V-03 | 97.5 | A | C-13, C-15 |

All 5 variations pass all 5 essential criteria. The 97.5-tier variations each implement one new v3 axis but lack the other two — exactly the designed gap. V-04 and V-05 are the first variations to pass all 16 criteria simultaneously.

### What made V-04/V-05 score 100

The four R3 axes are structurally compatible — that's the core finding. The synthesis ordering (calibration → severity table → DRAFT summary → dimension analysis with inline markers) works because each step informs the next without contradiction.

**V-05's census layer** adds genuine value (11-section report, namespace × artifacts × dates matrix as shared reference foundation, reframing the report from diagnostic to evidentiary) but doesn't change the score. For R4 consideration: make the census conditional on inventory depth.

**V-02's residual gap**: the post-analysis CONFIRMED/REVISED at Step 6 is the legacy R2 pattern. Pairing V-02's calibration rationale with V-01's per-dimension markers would tighten the integration (STALENESS marker cites the calibration rationale inline).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-dimension CONFIRMED/REVISED lifecycle marker placed inline at each finding's production site against pre-declared predictions — not assembled post-hoc", "staleness threshold calibration rationale names the decision-velocity causal mechanism, not just the inventory rule", "INTERNAL ANALYSIS BLOCK with cross-step prohibition on severity labels appearing in the coaching narrative — architectural register separation", "evidence census matrix as pre-analysis shared reference foundation — maps all artifacts before any analytical claim, reframing report from diagnostic to evidentiary"]}
```
missing |
| C-05 | PASS | "Coaching register throughout — surface observations, suggest next steps. Do not block the team or render verdicts." |
| C-06 | PASS | "Threshold: 30 days" explicitly stated in STALENESS section |
| C-07 | PASS | Every dimension ends with "name at least one concrete next action" — required for all four |
| C-08 | PASS | Report structure item 1 is Draft readiness summary (Step 2), which precedes all per-dimension sections |
| C-09 | PASS | Step 4: "identify the root weakness they share. Name it explicitly. Do not recap the individual flags." |
| C-10 | PASS | Step 6: "List every namespace with no artifact... characterize the gap: expected given the topic's stage, or a meaningful blind spot?" |
| C-11 | PASS | "CAUSAL GAP (analyze first)" explicit label; report structure positions it as item 2, first among the four dimensions |
| C-12 | PASS | Two required sub-questions inside CAUSAL GAP: sub-question 2 is the full inertia check with explicit gap-flag requirement |
| C-13 | PASS | V-01's focus. Step 2 requires per-dimension predictions (CLEAN/FLAG); Step 3 requires CONFIRMED/REVISED marker "immediately after the conclusion — before the next dimension begins." Lifecycle is at the production site, not deferred. |
| C-14 | PASS | All four dimension examples consistently use `/namespace:skill` syntax ("`/signal:scout-inertia`", "`/signal:scout-size`", "`/signal:discover-compare`", "`/signal:discover-competitors`") — modeling is structurally consistent across all dimensions |
| C-15 | FAIL | Fixed 30-day threshold with no calibration rationale based on inventory composition; no decision-velocity mechanism declared |
| C-16 | FAIL | No severity table; no INTERNAL ANALYSIS BLOCK; no architectural separation between analytical tier and coaching register |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 6/8

**Composite:** (5/5)x60 + (3/3)x30 + (6/8)x10 = 60 + 30 + 7.5 = **97.5**

---

### V-02 — Calibrated Threshold with Decision-Velocity Rationale

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four dimensions analyzed in Step 4 with explicit order |
| C-02 | PASS | "Name specific artifacts if present; name the gap if not. Do not restate the hypothesis." |
| C-03 | PASS | Calibrated threshold (14 or 30 days) declared in Step 2; STALENESS requires list of artifacts beyond threshold by name |
| C-04 | PASS | "Does any artifact provide evidence that this feature causes the claimed outcome? Name what exists and what is missing." |
| C-05 | PASS | "Coaching register: you observe, characterize, and suggest. You do not block or render verdicts." |
| C-06 | PASS | Concrete threshold declared as labeled block in Step 2 — either 14 or 30 days |
| C-07 | PASS | Step 4 explicitly requires: "at least one concrete next action (use `/namespace:skill` format, e.g., 'Run `/signal:scout-inertia`')" |
| C-08 | PASS | Draft readiness summary (Step 3) precedes all per-dimension analysis (Step 4); summary-before-dimensions constraint satisfied |
| C-09 | PASS | Step 5: "identify the root weakness they share. Name it explicitly. Do not simply recap the flags." |
| C-10 | PASS | Step 7: "List every namespace with no artifact. For each, characterize the gap: expected at this topic's stage, or a meaningful blind spot?" |
| C-11 | PASS | Step 4 specifies CAUSAL GAP "(analyze first)"; report structure item 3 positions it first among the four dimension sections |
| C-12 | PASS | Two required questions in CAUSAL GAP: "Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly." |
| C-13 | FAIL | CONFIRMED/REVISED appears only once at Step 6 ("Return to Step 3. Write CONFIRMED or REVISED") — a single post-analysis overall check, not per-dimension inline markers. C-13 requires each dimension to carry its own lifecycle marker at the production site. |
| C-14 | PASS | Step 4 explicitly mandates format: "use `/namespace:skill` format, e.g., 'Run `/signal:scout-inertia`'" — strongest explicit mandate of the non-synthesis variations |
| C-15 | PASS | V-02's focus. Threshold declared with full causal chain: "competitive environment can shift significantly within days... competitive positioning changes faster than underlying market structure. 14 days reflects this higher decision velocity." Mechanism named, not just the rule. |
| C-16 | FAIL | No severity table; no INTERNAL ANALYSIS BLOCK; no architectural separation layer |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 6/8

**Composite:** (5/5)x60 + (3/3)x30 + (6/8)x10 = 60 + 30 + 7.5 = **97.5**

---

### V-03 — Severity Table with Named INTERNAL ANALYSIS BLOCK

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four dimensions in Step 4 (team-facing narrative) and Step 3 (severity table), in explicit order |
| C-02 | PASS | Step 4 CAUSAL GAP: "Name specific artifacts or name the gap. Do not restate the hypothesis." |
| C-03 | PASS | "Threshold: 30 days" stated in Step 4; STALENESS requires listing every artifact older than 30 days by name |
| C-04 | PASS | Direct mechanism sub-question required in CAUSAL GAP; naming present/missing is mandatory |
| C-05 | PASS | "Advisory register: surface observations, suggest next steps, let the team decide. Nothing in this output is a blocking gate." |
| C-06 | PASS | 30-day threshold explicitly stated in STALENESS section |
| C-07 | PASS | Step 4 explicitly requires: "name at least one concrete next action (use `/namespace:skill` format, e.g., 'Run `/signal:scout-inertia`')" for gap/concern severity |
| C-08 | PASS | Report structure item 1 is Draft readiness summary (Step 2) — leads the report before all dimension sections |
| C-09 | PASS | Step 5 item 1: "Cross-dimension pattern: if two or more dimensions are gap or concern in Step 3, name the root weakness they share. Translate from the severity table to a plain-language diagnosis." |
| C-10 | PASS | Step 6: "List each namespace with no artifact. For each, characterize: expected given topic stage, or a meaningful blind spot?" |
| C-11 | PASS | Step 4 analysis order specifies CAUSAL GAP first; report structure item 3 positions it first among dimension sections |
| C-12 | PASS | CAUSAL GAP required question 2: "Would doing nothing also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly." |
| C-13 | FAIL | V-03's confirm/revise step (Step 5 item 2) is a single overall "Return to Step 2. Write CONFIRMED or REVISED." No per-dimension lifecycle markers; no pre-declared per-dimension predictions to confirm or revise against. |
| C-14 | PASS | Step 4 explicitly mandates: "use `/namespace:skill` format, e.g., 'Run `/signal:scout-inertia`'" — format is structurally required, not modeled by example |
| C-15 | FAIL | Fixed 30-day threshold with no calibration rationale; inventory composition not consulted; no decision-velocity mechanism declared |
| C-16 | PASS | V-03's focus. INTERNAL ANALYSIS BLOCK bounded by named header/footer, with framing sentence before the table: "The table below is for your reference only — it is not team-facing output. Severity ratings are internal analytical notation, not blocking gates." Architectural separation, not inline disclaim. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 6/8

**Composite:** (5/5)x60 + (3/3)x30 + (6/8)x10 = 60 + 30 + 7.5 = **97.5**

---

### V-04 — Full v3 Synthesis (C-13 + C-14 + C-15 + C-16)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four dimensions in Step 5 with explicit analysis order |
| C-02 | PASS | "Name specific artifacts if present; name the gap if not. Do not restate the hypothesis." |
| C-03 | PASS | Calibrated threshold from Step 2; STALENESS requires listing artifacts beyond threshold with sole-evidence annotation |
| C-04 | PASS | Direct mechanism sub-question in CAUSAL GAP; explicit naming requirement for present/missing |
| C-05 | PASS | "Coaching register throughout — surface observations, name next steps, let the team decide. Do not block the team or render verdicts." |
| C-06 | PASS | Calibrated threshold declared as labeled block in Step 2 — 14 or 30 days depending on inventory |
| C-07 | PASS | Step 5 requires "at least one next action in `/namespace:skill` format" for every flagged dimension |
| C-08 | PASS | Draft readiness summary (Step 4) precedes all dimension analysis (Step 5); summary-before-dimensions satisfied |
| C-09 | PASS | Step 6: "identify the root weakness they share. Name it explicitly." with worked structural example in prompt text |
| C-10 | PASS | Step 8: "List each namespace with no artifact. For each, characterize: expected at this topic's stage, or a meaningful blind spot?" |
| C-11 | PASS | Step 5 labels CAUSAL GAP "(analyze first)"; report structure item 4 positions it first among the four dimension sections |
| C-12 | PASS | Full inertia check in CAUSAL GAP with reinforcing framing: "This is the question teams most commonly skip. Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean." |
| C-13 | PASS | Step 4 declares per-dimension predictions (CLEAN/FLAG). Step 5 requires lifecycle marker "immediately after each dimension's conclusion — before the next dimension begins." Per-dimension commitment is made and resolved at each production site. |
| C-14 | PASS | Step 5 explicitly mandates: "provide at least one next action in `/namespace:skill` format" — structurally required across all four dimensions |
| C-15 | PASS | Step 2 declares calibrated threshold with full causal mechanism: "competitive positioning changes faster than underlying market structure. 14 days reflects this higher decision velocity." Mechanism is named, not just the rule. |
| C-16 | PASS | Step 3 INTERNAL ANALYSIS BLOCK: bounded header/footer, framing sentence before the table: "Severity ratings below are for your analytical reference only — they are not team-facing output and not blocking gates. The coaching narrative in Step 5 is what the team reads." Severity labels "do not appear in the narrative below" — register boundary is architectural and enforced by cross-step reference. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 8/8

**Composite:** (5/5)x60 + (3/3)x30 + (8/8)x10 = 60 + 30 + 10 = **100**

---

### V-05 — Evidence Census Foundation Layer

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four dimensions in Step 5 with explicit order |
| C-02 | PASS | "Name specific census entries or name the gap if none exist. Do not restate the hypothesis." |
| C-03 | PASS | Calibrated threshold from Step 2; STALENESS lists every artifact from census beyond threshold by name |
| C-04 | PASS | CAUSAL GAP sub-question 1: "Do any census entries show artifact evidence that this feature causes the claimed outcome? Name specific census entries or name the gap." |
| C-05 | PASS | "Coaching register: surface what the evidence shows, suggest next steps, let the team decide. No blocking language." |
| C-06 | PASS | Calibrated threshold declared as labeled block in Step 2 — 14 or 30 days with rationale |
| C-07 | PASS | Step 5 requires: "provide a next action in `/namespace:skill` format" for every flagged dimension |
| C-08 | PASS | Draft readiness summary (Step 4) precedes all dimension analysis (Step 5); census/threshold/severity table are pre-analytic scaffolding, not per-dimension sections |
| C-09 | PASS | Step 6: "use the census and severity table to identify the root weakness. Name it explicitly — reference specific census gaps to ground the diagnosis." |
| C-10 | PASS | Step 8: "Take every namespace with zero artifacts from the census. For each, characterize: is the absence expected at this topic's stage, or a notable blind spot?" |
| C-11 | PASS | Step 5 labels CAUSAL GAP first in analysis order; report structure item 5 positions it first among the four dimension sections |
| C-12 | PASS | CAUSAL GAP sub-question 2: "Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Reference any census artifact that addresses this. If none exist, flag the inertia gap explicitly." |
| C-13 | PASS | Step 4 declares per-dimension predictions (CLEAN/FLAG), marked "census-derived." Step 5 requires lifecycle marker after each dimension: "Then write the lifecycle marker: CONFIRMED or REVISED." Inline per-dimension resolution against pre-declared predictions. |
| C-14 | PASS | Step 5 explicitly mandates: "provide a next action in `/namespace:skill` format" — consistently required across all four dimensions |
| C-15 | PASS | Step 2 declares calibrated threshold with causal mechanism: "competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk. 14 days reflects the higher decision velocity these evidence types demand." Mechanism named. |
| C-16 | PASS | Step 3 INTERNAL ANALYSIS BLOCK: bounded header/footer, framing sentence: "This table is for your reference only — not team-facing, not a blocking gate. The coaching narrative in Step 5 is the team-facing output." Architectural separation with explicit cross-step reference. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 8/8

**Composite:** (5/5)x60 + (3/3)x30 + (8/8)x10 = 60 + 30 + 10 = **100**

---

### Ranking

| Rank | Variation | Score | Grade | Note |
|------|-----------|-------|-------|------|
| 1 (tie) | V-04 | 100 | A+ | Synthesis of all four v3 criteria; cleanest step architecture (8 steps, 10-section report) |
| 1 (tie) | V-05 | 100 | A+ | Same v3 synthesis plus evidence census foundation layer; 11-section report |
| 3 (tie) | V-01 | 97.5 | A | C-15 fail (fixed threshold, no calibration rationale); C-16 fail (no severity table) |
| 3 (tie) | V-02 | 97.5 | A | C-13 fail (post-analysis confirm/revise only, not per-dimension inline); C-16 fail (no severity table) |
| 3 (tie) | V-03 | 97.5 | A | C-13 fail (no per-dimension markers, no per-dimension predictions); C-15 fail (fixed threshold) |

---

### Excellence Signals

**From V-04 and V-05 (100-tier synthesis):**

**1. Compound structure holds without internal contradictions.** V-04 combines four independently designed axes (C-13 per-dimension markers, C-14 skill commands, C-15 calibrated threshold, C-16 severity table) in a single 8-step prompt without the axes interfering. The ordering is disciplined: calibration (Step 2) -> severity table (Step 3) -> DRAFT summary (Step 4) -> dimension analysis with inline lifecycle markers (Step 5). Each step informs the next. The fact that V-04 passes all 16 criteria is evidence that these four patterns are structurally compatible.

**2. Per-dimension CONFIRMED/REVISED at the production site.** V-01 established this axis; V-04 and V-05 integrate it into the synthesis. The key structural insight: placing the lifecycle marker immediately after each dimension's conclusion (before the next dimension begins) makes the commitment verifiable at the source. The pre-declared per-dimension predictions (CLEAN/FLAG in the DRAFT step) are what each CONFIRMED/REVISED marker resolves against. The two elements are semantically linked — not just structurally adjacent.

**3. Decision-velocity mechanism as calibration rationale.** V-02 established this axis. The key advance over R2 is naming the mechanism — "competitive positioning changes faster than underlying market structure" — rather than just the rule ("use 14 days if competitive signals exist"). The mechanism makes the threshold defensible to a reader who disagrees with the calibration, because the disagreement has a specific point of engagement.

**4. INTERNAL ANALYSIS BLOCK with enforced register separation.** V-03 established this axis. The architectural advance over R2 V-03 (which disclaimed inside a severity row) is the framing sentence before the table, at the block level. V-04 further strengthens this with an explicit cross-step prohibition: "Severity labels from this block do not appear in the narrative below" — the register boundary is declared and enforced.

**From V-05 exclusively (novel axis, not in R1/R2):**

**5. Evidence census as shared reference foundation.** The census matrix (namespace x artifacts x dates x count) built in Step 1 serves as the single authoritative reference for all dimension findings. Dimension sections cite census entries directly rather than re-listing artifacts per section. This reframes the report's epistemology: from "here is what is wrong" (diagnostic) to "here is what evidence exists and what it says together" (evidentiary). The diagnosis follows from the evidence base, not the other way around. Gaps are structurally visible before any analytical claim is made.

**V-05 note for R4:** The census adds genuine organizational value but extends the report to 11 sections. For topics with thin artifact inventories, the overhead may exceed the insight gain. Candidate refinement: make the census conditional on inventory depth — full matrix if 10+ artifacts, inline list otherwise.

**V-02 note for R4:** The single post-analysis CONFIRMED/REVISED (Step 6) is the residual legacy pattern from R2. V-02 otherwise achieves strong v3 compliance. Pairing V-02's calibration axis with V-01's per-dimension marker axis would produce a specialized variant where the calibration rationale feeds directly into the STALENESS CONFIRMED/REVISED marker — a tighter integration than the synthesis currently provides.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-dimension CONFIRMED/REVISED lifecycle marker placed inline at each finding's production site against pre-declared predictions — not assembled post-hoc", "staleness threshold calibration rationale names the decision-velocity causal mechanism, not just the inventory rule", "INTERNAL ANALYSIS BLOCK with cross-step prohibition on severity labels appearing in the coaching narrative — architectural register separation", "evidence census matrix as pre-analysis shared reference foundation — maps all artifacts before any analytical claim, reframing report from diagnostic to evidentiary"]}
```
