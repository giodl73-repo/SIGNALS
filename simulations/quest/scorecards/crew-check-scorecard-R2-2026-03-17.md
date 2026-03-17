# crew-check — Quest Score: R2 (5 Variations, Rubric v2)

## Rubric v2 — Criteria Reference

| Tier | ID | Criterion | Pts |
|------|----|-----------|-----|
| Essential | C-01 | Role source traceability | 12 |
| Essential | C-02 | Review matrix structure | 12 |
| Essential | C-03 | Perspective fidelity | 12 |
| Essential | C-04 | Depth mode compliance | 12 |
| Essential | C-05 | Severity presence | 12 |
| Recommended | C-06 | Finding specificity | 10 |
| Recommended | C-07 | Recommendation actionability | 10 |
| Recommended | C-08 | Severity calibration consistency | 10 |
| Aspirational | C-09 | Cross-role synthesis | 2 |
| Aspirational | C-10 | AMEND responsiveness | 2 |
| Aspirational | C-11 | Lens-anchoring step | 2 |
| Aspirational | C-12 | Severity calibration contract | 2 |
| Aspirational | C-13 | Challenger-first sequencing | 2 |

---

## V-01 — Inertia framing

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 1 builds pool from `.craft/roles/` only; error+halt if absent |
| C-02 | **PASS** | Step 6 matrix has all 4 columns; no blank cells permitted |
| C-03 | **PASS** | Step 5a lens-anchor + challenger inertia reference enforce role voice differentiation |
| C-04 | **PASS** | Standard 2–4 relevant roles; `--depth deep` = all; challenger always included |
| C-05 | **PASS** | Step 4 severity contract applied per row via Step 5c |
| C-06 | **PASS** | "A finding without a named surface fails the specificity check" — section/field/assumption required |
| C-07 | **PASS** | "A recommendation without a location fails the actionability check" — what+where required |
| C-08 | **PASS** | Step 4 calibration anchored to inertia block; HIGH defined as "at least as urgent as the inertia gap" |
| C-09 | **PASS** | Step 7 requires convergence + conflict; "No cross-role signal detected" fallback |
| C-10 | **PASS** | AMEND block covers add, deep, rerun:inertia, rerun:[role] |
| C-11 | **PASS** | "Do not skip this step. A review without a lens anchor is invalid." — Step 5a |
| C-12 | **PASS** | Step 4 table: HIGH=blocks commitment, MEDIUM=fix before ship, LOW=advisory; inertia calibration anchor |
| C-13 | **PASS** | Step 5 "in this order (challenger roles first)" + Step 2 inertia block is pre-review mandatory gate |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 5/5**
**Composite: 60 + 30 + 10 = 100**

---

## V-02 — Coaching voice

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "Those files are your reviewer pool. Don't invent roles that aren't in the directory." |
| C-02 | **PASS** | Matrix with 4 columns; execution order: challengers first, domain roles after |
| C-03 | **PASS** | "your job is to let each perspective speak for itself — not collapse everything into a single generic voice" + lens step |
| C-04 | **PASS** | Standard 2–4, `--depth deep` = all; challengers always included |
| C-05 | **PASS** | Scale defined; Step 3 calibration applied per row |
| C-06 | **PASS** | "If you can't name where in the artifact the concern lives, the finding isn't ready yet" |
| C-07 | **PASS** | "something like 'add a switching-cost comparison to the Motivation section.' If your recommendation doesn't name a location, it isn't concrete enough yet." |
| C-08 | **PASS** | "If something feels 'HIGH-ish' — it's HIGH. The scale is intentionally small. Calibration matters more than granularity." |
| C-09 | **PASS** | Post-matrix "What did the reviewers agree on?" — two-or-more convergence + disagreement required |
| C-10 | **PASS** | AMEND block includes add, deep, rerun:[role], scope:[domain] |
| C-11 | **PASS** | "If you haven't done this step, you're not ready to write the finding." — strongest compliance framing across all variations |
| C-12 | **PASS** | Three-level definitions present; HIGH=cannot defer, MEDIUM=fix before ship, LOW=won't hold up |
| C-13 | **PASS** | "Work through your selected roles in this order: challenger archetype roles first" — explicit mandate |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 5/5**
**Composite: 60 + 30 + 10 = 100**

---

## V-03 — Severity-sorted matrix

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 1 builds pool from `.craft/roles/` only |
| C-02 | **PASS** | Step 5 matrix has 4 columns; sorted by severity score descending |
| C-03 | **PASS** | Step 4a lens-anchor before finding; "Do not proceed to the finding without it" |
| C-04 | **PASS** | Standard 2–4 + challenger; `--depth deep` = all |
| C-05 | **PASS** | Step 3 contract; Step 4c assigns label per row |
| C-06 | **PASS** | "No unnamed surfaces" — section/field/diagram/assumption required |
| C-07 | **PASS** | "One concrete action: what to do and where in the artifact" |
| C-08 | **PASS** | Numeric score forces calibration resolution before render; sort creates consistency pressure |
| C-09 | **PASS** | Step 7 convergence + conflict; naming of shared-concern roles required |
| C-10 | **PASS** | AMEND block includes add, deep, rerun:[role], unsorted variant |
| C-11 | **PASS** | "Do not proceed to the finding without it" — Step 4a |
| C-12 | **PASS** | Step 3 table: label + numeric score + operational meaning per row |
| C-13 | **PASS** | "Challenger archetype roles run first"; matrix sorts by severity within tier, but execution order mandate satisfies rubric "prompt mandates it" condition |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 5/5**
**Composite: 60 + 30 + 10 = 100**

---

## V-04 — Inertia + Sort (combination)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Stage 1: `.craft/roles/` only; ERROR+halt if missing |
| C-02 | **PASS** | Stage 6 severity-sorted matrix; 4 columns |
| C-03 | **PASS** | Stage 5 step 1: "Do not write the finding before writing the lens" |
| C-04 | **PASS** | Standard 2–4 + challenger; `--depth deep` = all |
| C-05 | **PASS** | Stage 3 contract applied at Stage 5 step 3 |
| C-06 | **PASS** | "No unnamed surfaces pass" — Stage 5 step 2 |
| C-07 | **PASS** | "Concrete action: what to do and where. Not a directive — a location is required." |
| C-08 | **PASS** | Sort + inertia baseline: dual calibration enforcement |
| C-09 | **PARTIAL** | Stage 8 says "convergence, conflict, or no signal" — does not explicitly mandate naming the specific roles that share a convergent concern; rubric requires "one convergent theme named with the roles that share it" |
| C-10 | **PASS** | Stage 9 AMEND: add, deep, rerun:inertia, rerun:[role], unsorted — richest coverage |
| C-11 | **PASS** | Stage 5 step 1 explicit; "Do not write the finding before writing the lens" |
| C-12 | **PASS** | Stage 3 table: label + score + operational meaning; "at least as urgent as the inertia gap" calibration |
| C-13 | **PASS** | Stage 5 "Challenger archetype roles run first" + mandatory inertia block |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: C-09 PARTIAL (1 pt), rest 2 pts × 4 = 9 pts**
**Composite: 60 + 30 + 9 = 99**

---

## V-05 — Full integration (Phase-gated)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | P1.1: `.craft/roles/` only; "Zero roles may be invented" |
| C-02 | **PASS** | Phase 4 R2 matrix: 4 columns; challenger rows first; lens gates as sub-headers above rows |
| C-03 | **PASS** | P1.4 + Phase 3: `Lens: "[quote]"` gate mandated before every finding; "finding risks collapsing into generic review language" named explicitly |
| C-04 | **PASS** | P2.1: `--depth deep` = all non-challenger roles; standard = 2–3 domain + all challengers |
| C-05 | **PASS** | SEVERITY CONTRACT defined at P1.2; referenced at every severity assignment |
| C-06 | **PASS** | "A finding that cannot name a surface is not specific enough" — Phase 3 gate |
| C-07 | **PASS** | "(1) what to do and (2) where in the artifact. Not a directive." — both phases |
| C-08 | **PASS** | Phase 3: "how does this compare to the inertia gap established in Phase 1? Calibrate accordingly" |
| C-09 | **PASS** | R3 requires "two or more roles independently flagged"; convergence + conflict, or explicit no-signal fallback |
| C-10 | **PASS** | R4 AMEND: add (archetype sequence), deep, skip:challengers, rerun:[role], rerun:challengers, scope:[domain] — most extensive coverage |
| C-11 | **PASS** | `Lens: "[quote]"` labeled token pattern: structural gate in P1.4 and Phase 3; "You may not proceed to the finding before this label is written" |
| C-12 | **PASS** | P1.2 SEVERITY CONTRACT block defined once, "Reference by name at every severity assignment throughout the run" |
| C-13 | **PASS** | Phase 1 runs challengers exclusively before Phase 2 (domain selection) even begins — strongest structural enforcement |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 5/5**
**Composite: 60 + 30 + 10 = 100**

---

## Ranking

| Rank | Variation | Score | Distinguishing feature |
|------|-----------|-------|------------------------|
| T-1 | V-01 | 100 | Inertia block as semantic baseline; inertia-missing → automatic HIGH |
| T-1 | V-02 | 100 | Coaching register; strongest anti-generic-voice framing |
| T-1 | V-03 | 100 | Severity-sorted matrix; numeric score as calibration forcing function |
| T-1 | V-05 | 100 | Phase-gated execution; row validation checklist; `Lens: "[quote]"` token; richest AMEND |
| 5 | V-04 | 99 | C-09 PARTIAL: synthesis section omits named-role requirement |

---

## Excellence Signals — R2 New Patterns

Three patterns from R2 are not present in R1 golden variations:

**1. `Lens: "[quote]"` labeled token pattern (V-05 P1.4 + Phase 3)**
Prior approach: instruction to quote the orientation frame (free-text compliance). R2 advance: making the lens anchor a required structural label — `Lens: "[quote]"` — that must appear as a syntactic token before the finding can proceed. This shifts compliance from intent to structure: a row missing the `Lens:` prefix is visibly malformed, not subtly wrong.

**2. Row validation checklist with Y/N gates before staging (V-05)**
No prior variation included a self-check step. V-05 adds explicit validation questions after each row (Lens gate written? Finding names surface? Severity is exactly HIGH/MEDIUM/LOW? Recommendation names what AND where? Finding is not a duplicate?) with "Revise any N before staging." This creates a reviewer loop that catches bad rows before they reach the matrix — an execution quality gate not achievable with single-pass prompts.

**3. Priority summary by severity tier (V-03 Step 6)**
Post-matrix tier count block: `HIGH: [N] finding(s) — [label]; MEDIUM: [N] finding(s); LOW: [N] finding(s)`. Forces the model to enumerate findings by tier after the matrix is complete, creating a coverage check that surfaces miscalibration (e.g., 0 HIGH in a review of a genuinely risky artifact).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Lens: \"[quote]\" labeled token pattern as mandatory structural prefix before each finding", "Row validation checklist with Y/N self-check gates before staging each reviewer row", "Priority summary block by severity tier after matrix (HIGH/MEDIUM/LOW counts with one-phrase labels)"]}
```
