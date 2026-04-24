## listen-feedback — Round 16 Scoring (Rubric v14)

**Scoring weights:** Essential = 15 pts each (75 max) · Recommended = 5 pts each (15 max) · Aspirational = 5 pts each (135 max) · **Total max: 225 pts**

---

## V-01 — Willingness-to-Adopt Axis

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | 12 persona cards | PASS | Protocol instructs C-01–C-12 explicitly |
| C-02 | NPS + justification | PASS | Step E (NPS + band) + Step F (2–4 sentences, gains AND losses) |
| C-03 | Severity-labeled feedback | PASS | Step G: blocking/major/minor/cosmetic with `[BLOCKING]` prefix |
| C-04 | Aggregate NPS + threshold | PASS | Aggregate section: mean + "Threshold (7.0): MET / NOT MET" |
| C-05 | Theme matrix | PASS | Final section with Severity Distribution column |

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| R-01 | Blocking issues escalated | PASS | `### BLOCKER ESCALATION` section |
| R-02 | PM and UX roles | PASS | PROFESSIONAL LENS with UX READ + PM READ |
| R-03 | Theme matrix severity annotation | PASS | Per-severity counts per row in matrix |

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-01 | Persona revision recommendations | PASS | Step H: named spec element required |
| A-02 | NPS sensitivity analysis | PASS | Dedicated section with contribution delta |
| A-03 | Inline [BLOCKING] flags | PASS | Step G specifies `[BLOCKING]` prefix inline |
| A-04 | Ascending NPS ordering | PASS | "Sort all 12 cards ascending by NPS" |
| A-05 | Two-pass revision recommendations | PASS | Pass 1 (per card) + Pass 2 (cross-persona ranked list) |
| A-06 | Inertia-baseline NPS justification | PASS | Step F: "relative to their current approach" required |
| A-07 | Severity-first within-card ordering | PASS | Step G: "Order by descending severity within the card" |
| A-08 | Band + distribution + Dominant Detractor | PASS | Band field in card; band distribution + Dominant Detractor in aggregate |
| A-09 | `Current approach:` field | PASS | First body field in card format |
| A-10 | `Dominant Detractor objection:` labeled field | PASS | Labeled in aggregate section |
| A-11 | Header id/name/role; Current approach first | PASS | Card header constraint; Current approach is first body field |
| A-12 | UX READ precedes PM READ | PASS | UX READ appears before PM READ in PROFESSIONAL LENS |
| A-13 | Numbered field manifest + completeness rule | FAIL | Steps lettered A–H; no numbered manifest or enforcement rule |
| A-14 | CI or variance annotation | FAIL | No SD or CI in aggregate section |
| A-15 | Willingness to adopt + threshold | PASS | Step D: 0–100% + "Clears adoption bar ≥65% / Adoption risk <65%"; adoption summary in aggregate |
| A-16 | Step 0 structured sub-fields | PASS | 4 labeled sub-fields: "What teams do today instead / Where it falls short / Floor-level switching cost / Persona-specific workflow disruption" |
| A-17 | Gains/losses bilateral coverage instruction | FAIL | Steps B and C are independent; no mutual prohibition |
| A-18 | NPS justification names spec element | PASS | Step F: "Must reference at least one named spec element" |
| A-19 | Cost-tiered revisions | FAIL | Pass 2 is ranked list only; no Low-cost/High-cost tiers |
| A-20 | Sensitivity analysis ±1 swing | PARTIAL | Uses "current ±1" notation — implies both directions but collapses into single Y.Y value; does not separate +1 and -1 deltas |
| A-21 | Conjunctive framing | FAIL | Steps B and C do not reference each other |
| A-22 | Convergence statement | FAIL | Professional Lens has UX + PM reads but no convergence section |
| A-23 | Numbered manifest + explicit completeness rule | FAIL | No numbered manifest (A-13 fails) |
| A-24 | Gains/losses cross-reference Step 0 sub-fields | FAIL | Steps B and C do not name Step 0 sub-fields by label |
| A-25 | UX-before-PM epistemic rationale | FAIL | Bare ordering instruction; no epistemic rationale stated |
| A-26 | Numbered aggregate manifest | FAIL | Labeled fields; no A1–A5 sequential numbering |
| A-27 | Failure mode annotations | PASS | Step D: "Without this field, that pattern is invisible in the per-card output" — explicit failure mode named |

**V-01 Score: 75 + 15 + 82.5 = 172.5 / 225**

---

## V-02 — Statistical Depth Axis

### Essential / Recommended: All PASS (same as V-01 pattern) — 75 + 15 = 90

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-01–A-12 | Baseline R13 set | PASS ×12 | All present and well-specified |
| A-13 | Numbered field manifest | FAIL | Steps lettered A–G |
| A-14 | CI or variance | PASS | Aggregate: "**Standard deviation:** SD = [X.X]" + "**95% Confidence interval:** CI: [...]". Formula for CI given (SD/3.46). |
| A-15 | Willingness to adopt | FAIL | No adoption field in card |
| A-16 | Step 0 sub-fields | FAIL | No Step 0 section |
| A-17 | Bilateral coverage instruction | FAIL | Steps B and C independent |
| A-18 | NPS justification names spec element | PASS | Step E requires named spec element |
| A-19 | Cost-tiered revisions | FAIL | Ranked list only |
| A-20 | Sensitivity analysis ±1 swing | PASS | Explicitly separate: "if shifted to [current + 1]... if shifted to [current - 1]" — both directions stated |
| A-21 | Conjunctive framing | FAIL | Steps B and C independent |
| A-22 | Convergence statement | FAIL | No convergence section |
| A-23 | Numbered manifest completeness rule | FAIL | No numbered manifest |
| A-24 | Gains/losses cross-reference Step 0 | FAIL | No Step 0 |
| A-25 | UX-before-PM epistemic rationale | FAIL | Bare ordering instruction |
| A-26 | Numbered aggregate manifest | FAIL | Labeled fields only |
| A-27 | Failure mode annotations | PASS | Aggregate section: "without the CI, a mean of 7.1 is indistinguishable in confidence from a mean of 8.5" — names the failure mode |

**V-02 Score: 75 + 15 + 80 = 170 / 225**

---

## V-03 — Professional Lens Depth Axis

### Essential / Recommended: All PASS — 75 + 15 = 90

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-01–A-12 | Baseline R13 set | PASS ×12 | All present |
| A-13 | Numbered field manifest | FAIL | Steps lettered A–G |
| A-14 | CI or variance | FAIL | No SD/CI in Phase 3 aggregate |
| A-15 | Willingness to adopt | FAIL | No adoption field |
| A-16 | Step 0 sub-fields | FAIL | No Step 0 section |
| A-17 | Bilateral coverage instruction | FAIL | Steps B and C independent |
| A-18 | NPS justification names spec element | PASS | Step E requires named spec element |
| A-19 | Cost-tiered revisions | FAIL | Ranked list only |
| A-20 | Sensitivity analysis ±1 swing | PARTIAL | "current ±1" collapses into single mean value; does not explicitly separate both directions |
| A-21 | Conjunctive framing | FAIL | Steps B and C independent |
| A-22 | Convergence statement | PASS | CONVERGENCE STATEMENT section: "Address both: Where UX and PM agree / Where UX and PM diverge" |
| A-23 | Numbered manifest completeness rule | FAIL | No numbered manifest |
| A-24 | Gains/losses cross-reference Step 0 | FAIL | No Step 0 |
| A-25 | UX-before-PM epistemic rationale | PASS | PHASE 1: "This ordering is epistemic, not stylistic: behavioral friction in a design is most visible before individual persona contexts filter it. If PM Read ran first, its strategic framing would anchor the UX reading..." |
| A-26 | Numbered aggregate manifest | FAIL | Labeled fields; not sequentially numbered |
| A-27 | Failure mode annotations | PASS | PHASE 1: "Without this ordering constraint, the failure mode is PM-anchored UX: the UX read confirms the PM frame rather than challenging it." Also CONVERGENCE STATEMENT: "Without a convergence statement, the two professional reads are parallel monologues." |

**V-03 Score: 75 + 15 + 82.5 = 172.5 / 225**

---

## V-04 — Numbered Manifests + Failure Mode Annotations

### Essential / Recommended: All PASS — 75 + 15 = 90

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-01–A-12 | Baseline R13 set | PASS ×12 | All present |
| A-13 | Numbered field manifest + completeness rule | PASS | PERSONA CARD MANIFEST: numbered table 1–9; "Omitting any numbered field for any persona constitutes an incomplete card and must be corrected before the output is considered valid." |
| A-14 | CI or variance | FAIL | No SD/CI in aggregate manifest |
| A-15 | Willingness to adopt + threshold | PASS | Field 8: "Percentage (0–100%) + annotation: Clears adoption bar (≥65%) / Adoption risk (<65%). Adoption bar threshold: 65%." A5 aggregate field: adoption summary |
| A-16 | Step 0 sub-fields | FAIL | No Step 0 section |
| A-17 | Bilateral coverage instruction | FAIL | Fields 2 and 3 in manifest are independent; no "neither complete without the other" language |
| A-18 | NPS justification names spec element | PASS | Field 6: "Must reference at least one named spec element" |
| A-19 | Cost-tiered revisions | FAIL | Pass 2 ranked list only; no Low/High-cost tiers |
| A-20 | Sensitivity analysis ±1 swing | PARTIAL | "current ±1" — same issue as V-01/V-03; single Y.Y for both directions |
| A-21 | Conjunctive framing | FAIL | Fields 2 and 3 do not cross-reference each other |
| A-22 | Convergence statement | FAIL | No convergence section in Professional Lens |
| A-23 | Numbered manifest + explicit completeness rule | PASS | "Completeness enforcement rule: Any card missing one or more manifest fields is malformed. Produce all 9 fields for all 12 cards." |
| A-24 | Gains/losses cross-reference Step 0 | FAIL | No Step 0 sub-fields in V-04 |
| A-25 | UX-before-PM epistemic rationale | FAIL | "UX Read precedes PM Read in document order." — bare ordering instruction, no rationale |
| A-26 | Numbered aggregate manifest | PASS | AGGREGATE MANIFEST: A1–A5 numbered table; "Aggregate completeness enforcement rule: All 5 aggregate fields (A1–A5) must be present. Counting to A5 in document order verifies completeness without parsing labels." |
| A-27 | Failure mode annotations | PASS | Field 1: "Without this field, Fields 2 and 3 have no baseline — gains and losses become feature descriptions rather than delta computations." Field 5: "Without Field 5 as a distinct field, band classification is lost...band cannot be recovered from the score alone." CARD ORDERING: "Without ascending-NPS ordering, Detractor-tier personas are buried in document sequence." Three failure modes explicitly named. |

**V-04 Score: 75 + 15 + 92.5 = 182.5 / 225**

---

## V-05 — Inertia Delta + Conjunctive Framing + Cost-Tiered Revisions

### Essential / Recommended: All PASS — 75 + 15 = 90

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-01–A-12 | Baseline R13 set | PASS ×12 | All present |
| A-13 | Numbered field manifest + completeness rule | FAIL | Evaluation protocol uses "Field 1—" through "Field 7—" labels; card format uses labeled (not numbered) fields; no completeness enforcement rule stated |
| A-14 | CI or variance | FAIL | No SD/CI in aggregate section |
| A-15 | Willingness to adopt | FAIL | No adoption field in card or aggregate |
| A-16 | Step 0 structured sub-fields | PASS | 4 named sub-fields: "What the status quo delivers / Where the status quo falls short / Floor-level switching cost / Persona-specific workflow disruption" |
| A-17 | Bilateral coverage instruction | PASS | Field 2: "Neither Field 2 nor Field 3 is complete without the other: completing Gains without completing Losses constitutes an incomplete card." Field 3 mirrors symmetrically. |
| A-18 | NPS justification names spec element | PASS | Field 5: "Must reference at least one named spec element" |
| A-19 | Cost-tiered revisions | PASS | Pass 2 explicitly separates **Low-cost revisions** (≤1 day, no architecture changes) and **High-cost revisions** (>1 week) with definitions |
| A-20 | Sensitivity analysis ±1 swing | PARTIAL | "current ±1" collapses into single Y.Y; does not separately state +1 and -1 mean deltas as V-02 does |
| A-21 | Conjunctive framing | PASS | Field 2 names Field 3 by label: "*(paired with Field 3, Losses and switching costs)*". Field 3 names Field 2: "*(paired with Field 2, Gains from this spec)*". Both labels present in field headers AND in prohibition text. |
| A-22 | Convergence statement | FAIL | No convergence section in Professional Lens |
| A-23 | Numbered manifest completeness rule | FAIL | No numbered manifest (A-13 fails); no explicit completeness rule |
| A-24 | Gains/losses cross-reference Step 0 sub-fields | PASS | Field 2: "computed from Step 0 'Where the status quo falls short:'" Field 3: "Compute losses from Step 0 'Floor-level switching cost:' and 'Persona-specific workflow disruption:'" — both fields name specific Step 0 sub-fields by label |
| A-25 | UX-before-PM epistemic rationale | PASS | Professional Lens: "UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded." |
| A-26 | Numbered aggregate manifest | FAIL | Aggregate uses labeled fields only; no A1–A5 numbering scheme |
| A-27 | Failure mode annotations | PASS | STEP 0: "without a named baseline, gains and losses become feature descriptions rather than delta computations, and the NPS justifications cannot be verified as inertia-comparative." Professional Lens UX-before-PM note names the same failure mode. |

**V-05 Score: 75 + 15 + 102.5 = 192.5 / 225**

---

## Round 16 Ranking

| Rank | Variation | Score | % Max | Key wins | Key gaps |
|------|-----------|-------|-------|----------|----------|
| 1 | **V-05** | **192.5** | 85.6% | A-16, A-17, A-18, A-19, A-21, A-24, A-25, A-27 | A-13/A-23 (numbered manifest), A-14 (CI), A-15 (adoption), A-22 (convergence), A-26 |
| 2 | **V-04** | **182.5** | 81.1% | A-13, A-15, A-23, A-26, A-27 (3 failure modes) | A-14, A-16, A-17, A-21, A-22, A-24, A-25 |
| 3 | **V-01** | **172.5** | 76.7% | A-15, A-16, A-27 | A-13, A-14, A-17, A-19, A-21–A-26 |
| 3 | **V-03** | **172.5** | 76.7% | A-22, A-25, A-27 | A-13, A-14, A-15, A-16, A-17, A-19, A-21, A-23, A-24, A-26 |
| 5 | **V-02** | **170.0** | 75.6% | A-14 (CI + SD), A-20 (both ±1 directions explicit) | A-13, A-15, A-16, A-17, A-19, A-21–A-26 |

---

## Excellence Signals from V-05

**Pattern 1 — Layered bilateral enforcement compounds structural resistance.** V-05 stacks A-17 (prose bilateral prohibition), A-21 (conjunctive field labeling where each field names the other), and A-24 (named Step 0 sub-field dependency) on the same gains/losses axis. Any single layer is bypassable; all three together make one-sided output require suppressing a named baseline sub-field — a structural impossibility rather than an instructional one.

**Pattern 2 — Step 0 sub-fields as a traceable dependency anchor.** When downstream fields (Field 2, Field 3) must explicitly cite Step 0 sub-field labels by name, the Step 0 section becomes an auditable reference, not just context. This converts the baseline from a framing device into a computation input that evaluators cannot skip without it being visible in the output.

**Pattern 3 — Cost-tier framing makes revision recommendations dual-audience.** Separating Low-cost (≤1 day) from High-cost (>1 week) in Pass 2 makes the same ranked list useful to engineering (quick wins vs. architectural scope) and product (prioritization vs. roadmap commitment) without adding criteria — it reframes the existing revision list.

---

```json
{"top_score": 193, "all_essential_pass": true, "new_patterns": ["three-layer bilateral enforcement (prose prohibition + conjunctive field cross-reference + named Step 0 sub-field dependency) makes one-sided gains/losses structurally impossible rather than instructionally discouraged", "named Step 0 sub-fields as traceable computation inputs — downstream fields must cite sub-field labels, converting baseline from framing context into auditable dependency", "cost-tier framing (Low-cost / High-cost) makes a single ranked revision list dual-audience without adding criteria — engineering reads quick wins, product reads roadmap scope"]}
```
