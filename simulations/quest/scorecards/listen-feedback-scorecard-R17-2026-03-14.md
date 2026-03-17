## listen-feedback Round 17 — Scoring (Rubric v15)

### Scoring Key

| Tier | Points |
|------|--------|
| C-01–C-05 (Essential) | 15 pts each · 75 total |
| R-01–R-03 (Recommended) | 5 pts each · 15 total |
| A-01–A-28 (Aspirational) | 5 pts each · 140 total |
| **Max** | **230** |

PARTIAL = half points. All essentials are gateway (output fails without them).

---

## V-01 — Two-Bullet Directional Sensitivity Block

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | 12 persona cards | PASS | "Twelve customer personas (C-01 through C-12)" specified |
| C-02 | NPS + justification per card | PASS | Fields 5 and 7 |
| C-03 | Severity-labeled feedback | PASS | Field 8 with blocking/major/minor/cosmetic |
| C-04 | Aggregate NPS + threshold | PASS | Aggregate section, threshold 7.0 |
| C-05 | Cross-persona theme matrix | PASS | Final section with Severity Distribution column |

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| R-01 | Blocking issues escalated | PASS | BLOCKER ESCALATION section present |
| R-02 | PM and UX roles included | PASS | Both present in PROFESSIONAL LENS |
| R-03 | Theme matrix severity annotation | PASS | Per-severity counts in Severity Distribution column |

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Persona-specific revision recommendation | PASS | Field 9: "naming a specific spec element" |
| A-02 | NPS sensitivity analysis (2–3 personas) | PASS | Sensitivity section identifies 2–3 high-influence personas |
| A-03 | Inline [BLOCKING] flags | PASS | "`[BLOCKING]` prefix on all blocking items" |
| A-04 | Ascending-NPS persona ordering | PASS | "Sort all 12 cards ascending by NPS" |
| A-05 | Two-pass revision recommendations | PASS | Pass 1 per-persona + Pass 2 cross-persona ranked list |
| A-06 | Inertia-baseline NPS justification | PASS | Field 7: "naming what this persona gains AND what they lose relative to Field 1" |
| A-07 | Severity-first within-card ordering | PASS | Field 8: descending severity order stated |
| A-08 | Band annotation + distribution + Dominant Detractor | PASS | NPS + Band fields; aggregate has band distribution and Dominant Detractor objection |
| A-09 | Named `Current approach:` field | PASS | Field 1 in card |
| A-10 | `Dominant Detractor objection:` in aggregate | PASS | Explicit labeled field in aggregate section |
| A-11 | Header id/name/role only; `Current approach:` first | PASS | Card format shows header with `### [C-XX] [Name] — [Role]`; Field 1 = Current approach |
| A-12 | UX READ precedes PM READ | PASS | Section order: UX READ then PM READ |
| A-13 | Numbered field manifest with completeness enforcement | PASS | Fields 1–9 enumerated with "Omitting any numbered field…constitutes an incomplete card" |
| A-14 | CI or variance annotation | **FAIL** | Aggregate section has no SD or confidence interval |
| A-15 | `Willingness to adopt:` with threshold | PASS | Field 4 with 65% adoption bar and annotation |
| A-16 | Step 0 uses structured sub-fields | PASS | 4 named bold sub-fields: What teams do today, Where it falls short, Floor-level switching cost, Persona-specific workflow disruption |
| A-17 | Gains/losses enforce bilateral coverage | **FAIL** | Fields 2 and 3 describe their own scope; no explicit prohibition of completing one without the other |
| A-18 | NPS justification references named spec element | PASS | Field 7: "Must reference at least one named spec element" |
| A-19 | Revision recommendations tiered by implementation cost | **FAIL** | Pass 2 sorts by personas affected and severity only; no cost tier |
| A-20 | Sensitivity names score swing per persona | PASS | Two-bullet block: "+1 direction: aggregate moves from X.X to Y.Y" and "-1 direction: moves to Z.Z" |
| A-21 | Gains/losses field instructions use conjunctive framing | **FAIL** | Field 2 and Field 3 instructions do not reference each other by name |
| A-22 | Professional lens convergence statement | PASS | CONVERGENCE STATEMENT section required |
| A-23 | Numbered manifest with explicit completeness rule | PASS | "Omitting any numbered field for any card constitutes an incomplete card" stated in protocol |
| A-24 | Gains/losses cross-reference named Step 0 sub-fields | **FAIL** | Fields 2 and 3 do not name Step 0 sub-fields by label |
| A-25 | UX-before-PM with epistemic rationale | PASS | "Without this ordering, PM strategic framing would anchor the UX reading before friction signals are independently recorded" |
| A-26 | Aggregate section uses numbered field manifest | **FAIL** | Aggregate fields are bold-labeled only; no A1–A5 sequential numbering |
| A-27 | Structural constraint names failure mode | **PARTIAL** | Sensitivity section notes "+1 shift and -1 shift are not symmetric near the 7.0 threshold" — asymmetry described but canonical "without [constraint], [failure mode] cannot be detected" form not used on any constraint instruction |
| A-28 | Sensitivity states +1 and −1 as distinct figures | PASS | Two-bullet block with separate "+1 direction:" and "-1 direction:" bullets per persona |

**V-01 Score:** 75 + 15 + (21 × 5) + 2.5 = **197.5**

---

## V-02 — Threshold-Proximity Annotation per Direction

### Essential Criteria

All C-01–C-05: **PASS** (Steps A–G cover NPS, justification, severity-labeled feedback; aggregate section present; theme matrix present)

### Recommended Criteria

All R-01–R-03: **PASS**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Persona-specific revision recommendation | PASS | Step G: "naming a spec element and what should change" |
| A-02 | NPS sensitivity analysis | PASS | Sensitivity section present |
| A-03 | Inline [BLOCKING] flags | PASS | "`[BLOCKING]` prefix on blocking items" |
| A-04 | Ascending NPS ordering | PASS | "Sort all 12 cards ascending by NPS" |
| A-05 | Two-pass revision recommendations | PASS | Pass 1 per-persona + Pass 2 cross-persona list |
| A-06 | Inertia-baseline NPS justification | PASS | Step E: "Must name what this persona gains AND what they lose relative to their current approach" |
| A-07 | Severity-first within-card ordering | PASS | Step F: "Descending order within the card" |
| A-08 | Band annotation + distribution + Dominant Detractor | PASS | Band per card; aggregate has band distribution and Dominant Detractor objection |
| A-09 | Named `Current approach:` field | PASS | Step A = Current approach; first in card |
| A-10 | `Dominant Detractor objection:` in aggregate | PASS | Labeled field in aggregate |
| A-11 | Header id/name/role only; `Current approach:` first | PASS | Card header format + Step A first |
| A-12 | UX READ precedes PM READ | PASS | Section order maintained |
| A-13 | Numbered field manifest | **FAIL** | Steps A–G are lettered prose steps, not a numbered manifest table with positional verifiability |
| A-14 | CI or variance annotation | PASS | Aggregate has SD and 95% CI with formula |
| A-15 | `Willingness to adopt:` field | **FAIL** | Not present in card format; no adoption bar per card |
| A-16 | Step 0 structured sub-fields | **FAIL** | No Step 0 baseline section at all |
| A-17 | Bilateral coverage prohibition | **FAIL** | Step B and Step C describe their scope independently; no explicit bilateral prohibition |
| A-18 | NPS justification references spec element | PASS | Step E: "Must reference at least one named spec element" |
| A-19 | Revision recommendations tiered by cost | **FAIL** | No cost tier in Pass 2 |
| A-20 | Sensitivity names score swing | PASS | "+1 shift (score → [N+1]): aggregate moves from X.X to Y.Y" |
| A-21 | Conjunctive framing on gains/losses | **FAIL** | Steps B and C do not reference each other |
| A-22 | Convergence statement | PASS | CONVERGENCE STATEMENT section required |
| A-23 | Numbered manifest + completeness enforcement | **FAIL** | No numbered manifest → completeness rule is moot |
| A-24 | Gains/losses cross-reference Step 0 sub-fields | **FAIL** | No Step 0 → no sub-field cross-reference possible |
| A-25 | UX-before-PM epistemic rationale | PASS | "Without this ordering, PM framing would anchor the UX reading before friction signals are independently recorded" |
| A-26 | Aggregate numbered field manifest | **FAIL** | Aggregate fields bold-labeled only |
| A-27 | Constraint names failure mode | PASS | CI annotation: "A mean-only aggregate obscures whether the threshold pass is robust or marginal — a mean of 7.1 is indistinguishable in shipping confidence from a mean of 8.5 without the spread." Sensitivity: "Without separate directional figures, that one-way crossing is invisible." Multiple failure-mode statements using canonical form |
| A-28 | +1 and −1 as distinct figures with threshold annotation | PASS | "+1 shift: aggregate moves from X.X to Y.Y — [clears threshold by +N | crosses threshold from NOT MET to MET]" and "-1 shift: aggregate moves from X.X to Z.Z — [fails threshold | crosses threshold from MET to NOT MET]" — both directions stated separately with threshold consequence |

**V-02 Score:** 75 + 15 + (19 × 5) = **185**

---

## V-03 — Causal Band-Transition Narrative per Direction

### Essential Criteria

All C-01–C-05: **PASS** (Phase 2 cards + Phase 3 aggregate + theme matrix)

### Recommended Criteria

All R-01–R-03: **PASS**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Persona-specific revision recommendation | PASS | Phase 2 "Revision recommendation — One specific change naming a spec element" |
| A-02 | NPS sensitivity analysis | PASS | Phase 3 sensitivity section identifies 2–3 personas |
| A-03 | Inline [BLOCKING] flags | PASS | "`[BLOCKING]` inline prefix on all blocking items" |
| A-04 | Ascending NPS ordering | PASS | "Sort all 12 cards ascending by NPS (lowest first)" |
| A-05 | Two-pass revision recommendations | PASS | TWO-PASS REVISION RECOMMENDATIONS section present |
| A-06 | Inertia-baseline NPS justification | PASS | Phase 2 justification: "Must name what this persona gains AND what they sacrifice" |
| A-07 | Severity-first within-card ordering | PASS | Phase 2 "Descending order within the card" |
| A-08 | Band annotation + distribution + Dominant Detractor | PASS | Band per card; aggregate has band distribution and Dominant Detractor objection |
| A-09 | Named `Current approach:` field | PASS | Present as first field in Phase 2 card |
| A-10 | `Dominant Detractor objection:` in aggregate | PASS | Phase 3 aggregate has labeled field |
| A-11 | Header id/name/role only; `Current approach:` first | PASS | Card format confirms this |
| A-12 | UX READ precedes PM READ | PASS | Phase 1 = UX Read (before any personas); PM Read in Phase 3 (after aggregate) |
| A-13 | Numbered field manifest | **FAIL** | Phase 2 fields are prose-labeled, not a numbered manifest table |
| A-14 | CI or variance annotation | **FAIL** | Aggregate has no CI or SD |
| A-15 | `Willingness to adopt:` field | **FAIL** | Not in Phase 2 card format |
| A-16 | Step 0 structured sub-fields | **FAIL** | No Step 0; Phase 1 is UX Read from spec, not a status-quo baseline |
| A-17 | Bilateral coverage prohibition | **FAIL** | Gains and losses fields described separately with no bilateral prohibition |
| A-18 | NPS justification references spec element | PASS | "Reference at least one named spec element" |
| A-19 | Revision recommendations tiered by cost | **FAIL** | No cost tier in Pass 2 |
| A-20 | Sensitivity names score swing | PASS | "+1 shift: Aggregate moves from X.X to Y.Y" and "-1 shift: Aggregate moves from X.X to Z.Z" |
| A-21 | Conjunctive framing | **FAIL** | Gains and losses fields do not reference each other |
| A-22 | Convergence statement | PASS | CONVERGENCE STATEMENT section required after both reads |
| A-23 | Numbered manifest + completeness enforcement | **FAIL** | No numbered manifest |
| A-24 | Gains/losses cross-reference Step 0 sub-fields | **FAIL** | No Step 0 |
| A-25 | UX-before-PM epistemic rationale | PASS | Phase 1: "If PM Read ran first, its strategic framing would anchor the UX reading — categorizing interaction friction as acceptable trade-offs before that friction is independently recorded. Without this ordering constraint, the failure mode is PM-anchored UX: the UX read confirms the PM frame rather than challenging it." Full failure mode + rationale |
| A-26 | Aggregate numbered field manifest | **FAIL** | Aggregate fields bold-labeled only |
| A-27 | Constraint names failure mode | PASS | Phase 1: "Without this ordering constraint, the failure mode is PM-anchored UX." Convergence: "Without a convergence statement, UX and PM reads are parallel monologues." PM Read: "A PM Read before the data is available is forecasting." Multiple canonical failure mode statements |
| A-28 | +1 and −1 as distinct figures | PASS | Two-bullet block with band-transition narration per direction: D-count changes, P-count changes, threshold status — both directions stated separately and narrated as structural events |

**V-03 Score:** 75 + 15 + (18 × 5) = **180**

---

## V-04 — Two-Bullet Directional Format + Numbered Manifests (A-23/A-26)

### Essential Criteria

All C-01–C-05: **PASS**

### Recommended Criteria

All R-01–R-03: **PASS**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Persona-specific revision recommendation | PASS | Field 9 guidance: "must name the spec element and state the change" |
| A-02 | NPS sensitivity analysis | PASS | Sensitivity section present |
| A-03 | Inline [BLOCKING] flags | PASS | Field 7 guidance: "`[BLOCKING]` items first" |
| A-04 | Ascending NPS ordering | PASS | "Sort all 12 completed cards in ascending NPS order" — with failure mode note |
| A-05 | Two-pass revision recommendations | PASS | TWO-PASS section present |
| A-06 | Inertia-baseline NPS justification | PASS | Field 6: "Must state what this persona gains AND what they lose relative to Field 1" |
| A-07 | Severity-first within-card ordering | PASS | Field 7: "descending severity" |
| A-08 | Band annotation + distribution + Dominant Detractor | PASS | Field 5 = Band; A3 = band distribution; A4 = Dominant Detractor objection |
| A-09 | Named `Current approach:` field | PASS | Field 1 in manifest |
| A-10 | `Dominant Detractor objection:` in aggregate | PASS | A4 in numbered aggregate manifest |
| A-11 | Header id/name/role only; `Current approach:` first | PASS | "Card header: identifier, name, and role only. No summary or context in the header line"; Field 1 is first body field |
| A-12 | UX READ precedes PM READ | PASS | PROFESSIONAL LENS: UX READ before PM READ |
| A-13 | Numbered field manifest | PASS | PERSONA CARD MANIFEST table with 9 numbered fields and "Omitting any numbered field…is malformed" |
| A-14 | CI or variance annotation | **FAIL** | No CI or SD in aggregate manifest |
| A-15 | `Willingness to adopt:` with threshold | PASS | Field 8 = Willingness to adopt; 65% adoption bar |
| A-16 | Step 0 structured sub-fields | **FAIL** | No Step 0 baseline section |
| A-17 | Bilateral coverage prohibition | **FAIL** | Fields 2 and 3 describe scope independently; no bilateral prohibition |
| A-18 | NPS justification references spec element | PASS | Field 6: "Must reference at least one named spec element" |
| A-19 | Revision recommendations tiered by cost | **FAIL** | Pass 2 sorts by personas and severity only |
| A-20 | Sensitivity names score swing | PASS | "+1 direction: aggregate mean moves from X.X to Y.Y" and "-1 direction: moves to Z.Z" |
| A-21 | Conjunctive framing | **FAIL** | Fields 2 and 3 do not reference each other by label |
| A-22 | Convergence statement | PASS | CONVERGENCE STATEMENT required |
| A-23 | Numbered manifest + completeness enforcement | PASS | PERSONA CARD MANIFEST table + "Any card missing one or more manifest fields is malformed. Produce all 9 fields for all 12 cards." |
| A-24 | Gains/losses cross-reference Step 0 sub-fields | **FAIL** | No Step 0 |
| A-25 | UX-before-PM epistemic rationale | PASS | "UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded" |
| A-26 | Aggregate numbered field manifest | PASS | AGGREGATE MANIFEST table with A1–A5 + "Counting to A5 in document order verifies completeness without parsing labels" |
| A-27 | Constraint names failure mode | PASS | **Field 1:** "Without this field, Fields 2 and 3 have no baseline — gains and losses become feature descriptions rather than delta computations." **Field 5:** "Without Field 5 as a distinct field, band classification is lost when NPS values are extracted for aggregate analysis." **Card ordering:** "Without ascending-NPS ordering, Detractor-tier personas are buried in document sequence." Multiple inline failure-mode annotations embedded in manifest cells. |
| A-28 | +1 and −1 as distinct figures | PASS | Two-bullet block with "+1 direction:" and "-1 direction:"; "A reviewer verifies completeness by counting: each entry must contain exactly 2 direction bullets" |

**V-04 Score:** 75 + 15 + (22 × 5) = **200**

---

## V-05 — Directional Separation + Inertia Sub-Fields + Failure Mode Annotation

### Essential Criteria

All C-01–C-05: **PASS**

### Recommended Criteria

All R-01–R-03: **PASS**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Persona-specific revision recommendation | PASS | Field 7: "must name a specific spec element (section, field, behavior, or feature)" |
| A-02 | NPS sensitivity analysis | PASS | NPS SENSITIVITY ANALYSIS section present |
| A-03 | Inline [BLOCKING] flags | PASS | "`[BLOCKING]` prefix on blocking items" in Field 6 |
| A-04 | Ascending NPS ordering | PASS | "Sort all 12 cards ascending by NPS (lowest first)" |
| A-05 | Two-pass revision recommendations | PASS | TWO-PASS REVISION RECOMMENDATIONS with tiered Pass 2 |
| A-06 | Inertia-baseline NPS justification | PASS | Field 5: "Must name what this persona gains (Field 2) AND what they lose (Field 3) relative to Field 1" |
| A-07 | Severity-first within-card ordering | PASS | Field 6: "Descending order within the card" |
| A-08 | Band annotation + distribution + Dominant Detractor | PASS | NPS + Band per card; aggregate has band distribution and Dominant Detractor objection |
| A-09 | Named `Current approach:` field | PASS | Field 1 = Current approach; first in card body |
| A-10 | `Dominant Detractor objection:` in aggregate | PASS | Labeled field in aggregate section |
| A-11 | Header id/name/role only; `Current approach:` first | PASS | Card format confirmed |
| A-12 | UX READ precedes PM READ | PASS | PROFESSIONAL LENS: UX READ before PM READ |
| A-13 | Numbered field manifest | **PARTIAL** | Evaluation protocol uses "Field 1 — Current approach" through "Field 7" with sequential numbering in prose instructions, but CARD FORMAT template uses bold labels without numeric prefix — card template is not a numbered list as required by A-13 |
| A-14 | CI or variance annotation | **FAIL** | Aggregate section has no SD or confidence interval |
| A-15 | `Willingness to adopt:` field | **FAIL** | Card format has 7 fields; no Willingness to adopt; no adoption bar |
| A-16 | Step 0 structured sub-fields | PASS | 4 named bold sub-fields: "What the status quo delivers:", "Where the status quo falls short:", "Floor-level switching cost:", "Persona-specific workflow disruption:" |
| A-17 | Bilateral coverage prohibition | PASS | Field 2: "Neither Field 2 nor Field 3 is complete without the other: completing Gains without completing Losses constitutes an incomplete card." Field 3 mirrors. Explicit bilateral prohibition stated |
| A-18 | NPS justification references spec element | PASS | Field 5: "Must reference at least one named spec element" |
| A-19 | Revision recommendations tiered by cost | PASS | Pass 2 produces "Low-cost revisions (copy, label, messaging, or configuration changes)" and "High-cost revisions (workflow redesign, architectural changes…)" as distinct labeled tiers |
| A-20 | Sensitivity names score swing | PASS | "If shifted to [N+1]: aggregate mean moves from X.X to Y.Y" and "If shifted to [N-1]: aggregate mean moves from X.X to Z.Z" — separate figures per direction |
| A-21 | Conjunctive framing on gains/losses | PASS | Field 2 label: "Gains from this spec *(paired with Field 3, Losses and switching costs)*" — references Field 3 by name in the field label itself. Field 3 references Field 2. Both instructions cross-reference each other |
| A-22 | Convergence statement | PASS | CONVERGENCE STATEMENT section required; "Without a convergence statement, the two professional reads are parallel monologues" |
| A-23 | Numbered manifest + global completeness enforcement | **FAIL** | No global completeness enforcement rule ("omitting any numbered field constitutes an incomplete card"); only a bilateral rule on Fields 2 and 3 |
| A-24 | Gains/losses cross-reference named Step 0 sub-fields | PASS | Field 2: "computed from Step 0 'Where the status quo falls short:'" — names sub-field label. Field 3: "Compute losses from Step 0 'Floor-level switching cost:' and 'Persona-specific workflow disruption:'" — names two sub-field labels. Cross-reference structurally enforces bilateral coverage via Step 0 |
| A-25 | UX-before-PM epistemic rationale | PASS | "UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded" |
| A-26 | Aggregate numbered field manifest | **FAIL** | Aggregate fields are bold-labeled only; no sequential A1–A5 numbering |
| A-27 | Constraint names failure mode | PASS | Sensitivity: "**Why both directions must be stated separately:** Without the +1 and -1 figures as distinct values, a spec that survives a best-case swing but fails under a worst-case one cannot be detected from this output." Step 0 framing: "without a named baseline, gains and losses become feature descriptions rather than delta computations." Convergence: "Without a convergence statement, the two professional reads are parallel monologues." Canonical failure-mode language used across multiple constraints |
| A-28 | +1 and −1 as distinct figures | PASS | "If shifted to [N+1]:" and "If shifted to [N-1]:" as separate bullet-level entries; failure mode named inline for this specific constraint |

**V-05 Score:** 75 + 15 + (23 × 5) + 2.5 = **207.5**

---

## Ranking

| Rank | Variation | Score | Key Gap |
|------|-----------|-------|---------|
| 1 | **V-05** | **207.5** | Missing A-14 (CI), A-15 (adoption field), A-23 (global completeness rule), A-26 (numbered aggregate) |
| 2 | V-04 | 200 | Missing A-14, A-16, A-17, A-19, A-21, A-24 (no Step 0 chain) |
| 3 | V-01 | 197.5 | Missing A-14, A-17, A-19, A-21, A-24, A-26 |
| 4 | V-02 | 185 | Missing A-13, A-15, A-16, A-17, A-19, A-21, A-23, A-24, A-26 |
| 5 | V-03 | 180 | Missing A-13, A-14, A-15, A-16, A-17, A-19, A-21, A-23, A-24, A-26 |

---

## Excellence Signals from V-05

**1. Failure mode annotation applied specifically to A-28.** The sensitivity section uses a labeled "**Why both directions must be stated separately:**" block with canonical causal language: "Without the +1 and -1 figures as distinct values, a spec that survives a best-case swing but fails under a worst-case one cannot be detected." Prior rounds applied A-27 to UX-before-PM and other structural constraints; Round 17 closes the explanation gap at the sensitivity section itself.

**2. Step 0 sub-field cross-reference converts gains/losses from freeform to structured delta.** Field 2 instructs "computed from Step 0 'Where the status quo falls short:'" — names the sub-field label as a required input. Field 3 names two sub-fields: "Floor-level switching cost:" and "Persona-specific workflow disruption:". Neither field can be completed without consulting the named baseline sub-field, making bilateral coverage structurally enforced rather than instructionally implied.

**3. Conjunctive field labeling in the card template.** The field label itself reads "**Gains from this spec *(paired with Losses and switching costs):***" — the pairing is visible to an evaluator scanning the card, not buried in protocol instructions.

**4. Implementation cost-tiered revision list.** Round 17 V-05 is the first variation to add Low-cost / High-cost revision tiers in Pass 2, making revision prioritization actionable beyond severity rank.

---

**V-04 excellence signal (separate from V-05):** Failure mode rationale co-located within numbered manifest table cells. Field 1 and Field 5 each carry inline failure mode explanations in the constraint column — "Without this field, Fields 2 and 3 have no baseline"; "Without Field 5 as a distinct field, band classification is lost." The A-27 rationale is structurally inseparable from the field definition, unlike section-level notes that can be overlooked.

---

```json
{"top_score": 208, "all_essential_pass": true, "new_patterns": ["A-27 failure mode annotation applied to the A-28 sensitivity constraint specifically — 'without separate +1 and −1 figures, a spec that survives a best-case swing but fails under a worst-case one cannot be detected' converts directional-separation from structural rule to self-explaining contract at the point of the constraint", "field-level failure mode rationale embedded in numbered manifest table cells (V-04) — failure consequence co-located with field definition, structurally inseparable from the manifest entry rather than stated as a section note"]}
```
