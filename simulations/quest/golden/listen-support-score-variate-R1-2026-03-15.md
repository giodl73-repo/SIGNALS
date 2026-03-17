---
skill: quest-score
skill_target: listen-support
rubric_version: 1
variate_file: listen-support-variate-R1-2026-03-15.md
date: 2026-03-15
round: 1
---

# listen-support — Score Report, Round 1

**Rubric:** v1 (C-01 through C-10, 100-pt ceiling)
**Variations scored:** V-01 through V-05 (axes: role sequence / output format / lifecycle)
**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
**Golden threshold:** all essential pass AND composite >= 80
**PARTIAL scoring:** 0.5 weight (prompt incentivizes criterion but does not enforce it)

---

## Criterion Evaluation

### C-01 — Ticket Inventory Present (essential)

Rubric requires: every ticket has title, category, volume, severity — all from controlled vocabulary. Zero missing or out-of-enum values.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | 6-field format with explicit allowed values per field; Self-Check gate at Step 4 scans all fields |
| V-02 | PASS | TABLE CHECK fires before any prose body; vocabulary constraint block explicitly states "no other values are valid" |
| V-03 | PASS | 6-field format with hard constraints section; phase label adds a seventh structural field |
| V-04 | PASS | TABLE CHECK with expanded "Support rows appear before SRE rows" check; all V-01 + V-02 gates combined |
| V-05 | PASS | Phase column added to table; TABLE CHECK + PHASE CONFIRMATION in Step 5B; strongest structural coverage |

---

### C-02 — Persona Attribution Per Ticket (essential)

Rubric requires: every ticket has a named persona from the stock set. At least two distinct personas.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Stock persona set listed; role activation enforces Support>=2, SRE>=1, PM/UX>=1, C-xx>=2 (4+ distinct types) |
| V-02 | PASS | TABLE CHECK: "Distinct personas: [N] (required: >= 2)" gated before proceeding; stock values listed |
| V-03 | PASS | Persona from stock set required; hard constraint "at least 2 distinct Persona values" |
| V-04 | PASS | TABLE CHECK persona gate + role activation order; stronger than either axis alone |
| V-05 | PASS | ROLE-PHASE CROSS-MATRIX pre-declares per-role counts; strongest enforcement of persona diversity |

---

### C-03 — Sample Ticket Body in Persona Voice (essential)

Rubric requires: every body >= 2 sentences, **written in first person**, role-consistent language.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PARTIAL | Register described per role (procedural/technical/strategic); 2-5 sentences required; role characterizations are authentic; **first-person pronoun not explicitly required** |
| V-02 | PARTIAL | Voice guidance per persona tier in Step 2; 2-5 sentences required; same first-person gap |
| V-03 | PARTIAL | Phase descriptions frame register (Phase 1: setup confusion, Phase 3: operational frustration); same first-person gap |
| V-04 | PARTIAL | Most detailed voice guidance of any single-axis variation (6-tier breakdown); same first-person gap |
| V-05 | PARTIAL | Voice guidance in Step 4, phase-aware register; same first-person gap as all others |

**Root cause:** No variation issues "Write in first person — 'I', 'my', 'we' — third person is prohibited." Rubric requires this; all five variations omit it. Universal PARTIAL.

---

### C-04 — Gap Analysis Produced (essential)

Rubric requires: all three categories present and non-empty; each gap entry **references at least one ticket by ID or title**; generic gaps do not count.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PARTIAL | 3 sections required with specific-artifact enforcement; good counter-examples shown; "Derive gaps from the tickets generated" creates implicit derivation linkage but **no ticket ID/title citation required in gap entry format** |
| V-02 | PARTIAL | 3 sections with specific artifact names required; no ticket ID reference requirement |
| V-03 | PARTIAL | 3 sections with specific artifacts; same ticket ID gap |
| V-04 | PARTIAL | 3 sections with specific artifacts; same ticket ID gap |
| V-05 | PARTIAL | 3 sections with specific artifacts; same ticket ID gap |

**Root cause:** No variation specifies "each gap entry must cite at least one ticket by ID (e.g., T-NN) or by title." The rubric's hardest gate fires here in all five variations. Universal PARTIAL.

---

### C-05 — Volume/Severity Distribution Non-Trivial (essential)

Rubric requires: >=2 distinct volume values, >=2 distinct severity values, P0 <= 25%, high-volume <= 50%.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | "At most 1 P0 ticket" + "at least 1 medium or low Volume entry" + role activation anchors P2/P3 dominance via Support-first ordering |
| V-02 | PASS | TABLE CHECK: P0 count (required: <= 1), Low/medium volume entries (required: >= 1); gate fires before bodies |
| V-03 | PASS | Hard constraints same as V-01; phase character descriptions (Phase 1 = P2/P3, Phase 3 = P0/P1) produce natural calibration across phases |
| V-04 | PASS | TABLE CHECK gates from V-02 + role ordering from V-01; double enforcement |
| V-05 | PASS | TABLE CHECK + PHASE CONFIRMATION + phase-severity guidance; strongest. Inline phase character table maps expected severity range per phase window |

---

### C-06 — Ticket Count in [6, 12] (recommended)

Rubric requires: ticket count in [6, 12] inclusive.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PARTIAL | Role minimums (Support>=2, SRE>=1, PM/UX>=1, C-xx>=2 to reach >=7) enforce lower bound; **no upper cap of 12 stated anywhere** |
| V-02 | PARTIAL | TABLE CHECK: "Total rows: [N] (required: >= 7)"; **no upper cap** |
| V-03 | PARTIAL | Phase constraints enforce total >= 7 (Phase 1 >= 3, all three non-zero); **no upper cap** |
| V-04 | PARTIAL | TABLE CHECK >= 7; **no upper cap** |
| V-05 | PARTIAL | Phase distribution target + TABLE CHECK + PHASE CONFIRMATION; **no upper cap** |

**Root cause:** All five variations enforce the lower bound but not the upper bound. A model could generate 15+ tickets and pass all gates.

---

### C-07 — Cross-Persona Coverage >= 3 distinct, no persona > 50% (recommended)

Rubric requires: >=3 distinct personas; dominant persona <= 50%.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | 4 role buckets with minimums (Support>=2, SRE>=1, PM/UX>=1, C-xx remaining to total>=7); Support share <= 2/7 = 28%; 4+ distinct types structurally guaranteed |
| V-02 | PARTIAL | TABLE CHECK requires >= 2 distinct personas (not >= 3); no 50% dominance cap stated |
| V-03 | PARTIAL | "At least 2 distinct Persona values" constraint; no 50% cap; no explicit >=3 requirement |
| V-04 | PASS | V-01 role activation inherited: 4 bucket minimums; TABLE CHECK adds explicit persona count gate |
| V-05 | PASS | ROLE-PHASE CROSS-MATRIX at Step 3A pre-declares counts for SRE, Support, PM, UX, and customer personas (5 role types); strongest guarantee |

---

### C-08 — Gap Actionability >= 75% named artifacts (recommended)

Rubric requires: >= 75% of gap entries include a named artifact or action specific enough for a team member to execute.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Counter-examples in every section ("Add troubleshooting section to getting-started guide covering error code E-4023" vs. "Improve documentation"); both acceptable and failing examples shown |
| V-02 | PASS | "Each entry must name a specific artifact" stated for all 3 sections |
| V-03 | PASS | "Each entry must name a specific artifact" stated; minimal but present |
| V-04 | PASS | Both V-01 and V-02 specificity framing combined |
| V-05 | PASS | Step 6 Gap Analysis maintains the same artifact-naming requirement |

---

### C-09 — Ticket Clustering and Theme Identification (aspirational)

Rubric requires: >=2 named themes; each contains >=2 tickets; theme description identifies underlying product/doc failure.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | No clustering step; Self-Check at Step 4 does not include theme analysis |
| V-02 | FAIL | No clustering step |
| V-03 | PARTIAL | Phase groupings (Phase 1: "setup friction / activation errors", Phase 2: "adoption edge cases", Phase 3: "steady-state operational") function as named temporal clusters with failure-type descriptions; short of product-risk framing per theme but provides scaffold |
| V-04 | FAIL | No clustering step |
| V-05 | PARTIAL | Inherits V-03 phase groupings; phases are named temporal clusters, not thematic clusters; lack explicit "what product failure generates this cluster" statement per rubric |

---

### C-10 — Ticket Lifecycle and Resolution Path (aspirational)

Rubric requires: for all high-volume and P0/P1 tickets, a resolution path with triage owner, root cause category, and resolution type (doc/eng/design).

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | No resolution path step |
| V-02 | FAIL | No resolution path step |
| V-03 | FAIL | No resolution path step |
| V-04 | FAIL | No resolution path step |
| V-05 | FAIL | No resolution path step |

---

## Composite Scores

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Essential | Rec | Asp | **Total** |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|-----|-----|-----------|
| V-01 | P | P | 0.5 | 0.5 | P | 0.5 | P | P | F | F | 48 | 25 | 0 | **73** |
| V-02 | P | P | 0.5 | 0.5 | P | 0.5 | 0.5 | P | F | F | 48 | 20 | 0 | **68** |
| V-03 | P | P | 0.5 | 0.5 | P | 0.5 | 0.5 | P | 0.5 | F | 48 | 20 | 2.5 | **70.5** |
| V-04 | P | P | 0.5 | 0.5 | P | 0.5 | P | P | F | F | 48 | 25 | 0 | **73** |
| V-05 | P | P | 0.5 | 0.5 | P | 0.5 | P | P | 0.5 | F | 48 | 25 | 2.5 | **75.5** |

P = 1.0, PARTIAL = 0.5, F = 0

**Ranking:** V-05 (75.5) > V-01 = V-04 (73) > V-03 (70.5) > V-02 (68)

**Golden status:** NONE — all essential criteria pass requires C-03 = PASS and C-04 = PASS; both are PARTIAL across all five variations.

---

## Root Cause Analysis — Why No Variation Reached Golden

**Critical gap 1 — C-03 first-person enforcement (universal)**
Every variation describes register ("procedural, volume-aware"), but none issues the prohibition: "Write in first person — 'I', 'my', 'we'. Do not write 'the user', 'the SRE', or any third-person role form." Without this, a model following the prompt can produce technically correct voice-register bodies in third person and still pass the prompt's stated requirements. Fix: add a PERFORMANCE MODE DECLARATION step (cf. golden Step 4) before body generation.

**Critical gap 2 — C-04 ticket ID cross-reference (universal)**
Every variation requires specific artifacts in gap entries, but none requires "each gap entry must cite at least one ticket by ID (T-NN) or by title." A gap analysis that names a concrete doc page but does not tie it to a specific ticket is unanchored — a scorer cannot verify the derivation chain. Fix: add "Tickets it relates to: [T-NN, ...]" as a required field in all three gap sections.

**Structural gap — C-06 upper bound (universal)**
Lower bound enforced (>=7), upper bound not. All five variations could produce 15+ tickets without a gate firing. Fix: add "Total rows: [N] (required: >= 6 and <= 12)" to all TABLE CHECK or constraint blocks.

---

## Excellence Signals from V-05

V-05 scored highest on three of the five axes where differentiation was possible (C-05, C-07, C-09):

**1. Three-gate pipeline prevents three distinct failure classes at different stages**
Phase distribution target (Step 1) → role-ordered vocabulary table (Step 3) → post-generation phase confirmation (Step 5B) forms a pipeline where each gate catches a different failure: Phase 1 clustering, role concentration, and post-body distribution drift respectively. No other variation tests for all three.

**2. Per-role minimums + phase binding prevents compound concentration**
V-01's role-bucket minimums prevented role concentration. V-03's phase targets prevented temporal clustering. V-05 combining them prevents per-role phase concentration — Support tickets cannot all cluster in Phase 1 without the PHASE CONFIRMATION firing. The interaction between the two axes is load-bearing.

**3. Phase character guidance (Phase 1 = P2/P3 / Phase 3 = P0/P1) produces natural severity calibration**
The phase character table at Step 2 in V-05 provides a semantically grounded reason for the severity distribution that the model can follow without needing an explicit "P0 <= 25%" constraint. This approaches what the golden achieves with its PHASE-SEVERITY INFERENCE RULE (C-45 through C-50).

**4. Role-Phase Cross-Matrix at Step 3A is the canonical extension path**
V-05 declares per-role counts per phase at Step 3A. The golden extends this to a 5-column ROLE-PHASE CROSS-MATRIX with Constraint 1B (per-phase-per-role verification). V-05 is one structural step below the golden's mechanism — it declares counts but verifies only totals, not per-phase-per-role cells.

---

## Recommendations for Round 2

| Priority | Change | Criterion unlocked |
|----------|--------|-------------------|
| P0 | Add PERFORMANCE MODE DECLARATION step: "You ARE the persona. Write every body in first person — 'I', 'my'. 'The SRE', 'the user', and all third-person role forms are prohibited." | C-03 PASS |
| P0 | Add "Tickets it relates to: [T-NN, ...]" as required field in all three gap sections | C-04 PASS |
| P1 | Add upper bound to all ticket count constraints: "Total rows: [N] (required: >= 6 and <= 12)" | C-06 PASS |
| P2 | Add named-theme clustering step after ticket generation: group 2+ related tickets under a short theme name, state the underlying product/doc failure | C-09 PASS |
| P3 | Add resolution path for high-volume/P0-P1 tickets: triage owner, root cause category, resolution type (doc/eng/design) | C-10 PASS |

With P0 fixes applied: C-03 and C-04 become PASS in all essential slots → essential_pass/5 = 5/5 → 60/60 essential, composite rises to 85+ for V-05 equivalent → golden threshold reached.

---

```json
{"top_score": 76, "all_essential_pass": false, "new_patterns": ["three-gate pipeline (phase declare at step 1 -> role-ordered table at step 3 -> phase confirm at step 5B) catches three distinct failure classes at different generation stages", "per-role minimums combined with phase distribution binding prevents compound concentration where single-role tickets cluster in single phase window", "phase character guidance (Phase 1 P2/P3 / Phase 3 P0/P1) produces natural severity calibration without explicit percentage constraints"]}
```
