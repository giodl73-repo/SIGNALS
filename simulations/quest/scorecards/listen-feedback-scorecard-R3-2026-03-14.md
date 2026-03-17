---

## listen-feedback R3 Scorecard — Results

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-05 (Combined ceiling) | **125** |
| 2 | V-01, V-02, V-03 | **110** each |
| 5 | V-04 (Declarative sort rule) | **100** |

**All 5 essential + all 3 recommended criteria pass across all variations.** Variance is entirely aspirational.

---

### Key R3 findings

**V-04 confirms template is load-bearing for A-07.** The declarative sort rule ("sort by severity descending") without a template that demonstrates blocking-first line ordering is structurally weaker than V-02/V-03's demonstrated template. A-07 compliance rate unproven — predicted 100, drops to 95 if A-07 fails.

**V-03 vs. V-02 on A-06:** Both reach 110 via different A-06 paths. V-03's per-card `Current approach:` field produces more persona-specific comparisons (each persona's current behavior named explicitly). V-02's Detractor/Passive/Promoter band definitions enforce inertia framing by vocabulary (economical, definitionally structural). Neither is clearly superior; both pass.

**V-01 register test:** All R3 structural requirements survive the conversational register (PASS). Reliability concern on A-03 and A-07 — prose may produce less consistent inline tag placement and severity ordering vs. template-demonstrated approaches.

**V-05 ceiling mechanism:** Two new R3 patterns doubly enforce A-06 — Phase 1 band annotation (inertia by category definition) + Phase 2 `Current approach:` named field (inertia by per-card explicit statement). Either alone passes A-06; both together make it near-impossible to miss.

---

### New patterns

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["nps-category-bands-with-aggregate-mean", "named-current-approach-field-in-phase-card"]}
```
04 all include: "All 12 cards required before any aggregate section."
V-05 includes: "All 12 cards required, in ascending NPS order, before Phase 3."

V-01 adds: "in this order" (C-01 through C-12) — numeric ordering, not ascending NPS. Cards
are in persona-ID order. Distinct from A-04 (which requires ascending NPS). No structural gap.

---

### C-02: Every feedback item has a severity tag — PASS all

- V-01: "Each item carries its severity label." Severity tags named in prose. PASS.
- V-02: Template demonstrates: `- blocking: [text] [BLOCKING] / - major: [text] / - minor: /
  - cosmetic:`. Severity tag is the first token of each feedback line. PASS.
- V-03: Same template as V-02. Severity label is structurally load-bearing (determines ordering).
  PASS.
- V-04: `- [severity: blocking | major | minor | cosmetic] [feedback item text]` — tag present
  but as a slot in a generic format, not demonstrated in descending order. PASS (tag present);
  see A-07 for ordering concern.
- V-05: Phase 2 template: `- blocking: [text] [BLOCKING] / - major: [text] / - minor: /
  - cosmetic:`. Same template-demonstration as V-02/V-03. PASS.

V-02, V-03, V-05 are strongest: severity is the first token of each line, making it structurally
required.

---

### C-03: NPS per persona with justification — PASS all

- V-01: "give their NPS score (1 through 10) with a sentence or two explaining it. The
  explanation should directly compare this feature against the inertia baseline." Inertia
  framing elevates quality floor. PASS.
- V-02: NPS in card header includes Detractor/Passive/Promoter annotation. Band definition
  ("Detractor = switching cost > net benefit") anchors the justification type. PASS.
- V-03: `NPS: [1-10] — [1-2 sentences: does this feature beat their current approach? State the
  net benefit vs. the switching cost. The comparison must be explicit.]` Per-card inertia
  framing. PASS.
- V-04: `NPS: [1-10] — [1-2 sentences: does this feature beat their current approach? State the
  switching cost vs. net benefit explicitly. Persona preference description alone does not
  qualify.]` PASS.
- V-05: Two-part justification: Phase 1 rationale (1 sentence, category-anchored) + Phase 2 card
  header restates Phase 1 score with `Current approach:` field as context. Score committed
  before feedback, preventing post-hoc drift. PASS.

---

### C-04: Aggregate NPS computed and threshold applied — PASS all

- V-01: End of output. "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]." Both branches.
  PASS.
- V-02: AGGREGATE NPS section. Mean of 12 scores. Both branches. Explicit fail language. PASS.
- V-03: AGGREGATE NPS section. Same format. Both branches. PASS.
- V-04: AGGREGATE NPS section. Same format. Both branches. PASS.
- V-05: End of Phase 1 — aggregate computed and threshold stated before any feedback cards.
  Phase gate: "Do not proceed to Phase 2 until all 12 scores... and the aggregate result are
  stated." Earliest structural enforcement position across all variations. PASS.

---

### C-05: Cross-persona theme matrix — PASS all

All five include the three-column template (Theme | Personas | Highest Severity).
V-01: theme matrix includes inertia-driven vs. net-new classification.
V-02: THEME MATRIX + CATEGORY SUMMARY. Category summary counts Detractor/Passive/Promoter
  and names dominant Detractor objection pattern — supplemental above rubric requirement.
V-03: THEME MATRIX with classification. PM READ explicitly references `Current approach:`
  field patterns, tying the matrix to per-card inertia data.
V-04: THEME MATRIX with inertia-driven vs. net-new note.
V-05: Phase 4 THEME MATRIX with severity annotation and inertia/spec-specific classification.

---

### R-01: Blocking issues escalated — PASS all

- V-01: Dedicated BLOCKING ITEMS section. "Collect all [BLOCKING] items from the 12 cards."
  Zero-result scripted. PASS.
- V-02: BLOCKING ITEMS section. "Collect every item marked [BLOCKING]." Zero-result scripted.
  PASS.
- V-03: BLOCKING ITEMS. "Because blocking items appear at the top of each card (severity-first
  ordering), this is a verification pass over each card's leading feedback item(s)." Escalation
  framed as tag-collection, simultaneously satisfying R-01 and A-03 second half. PASS.
- V-04: BLOCKING ITEMS section. Zero-result scripted. Escalation framed as tag-collection
  ("Collect every item tagged [BLOCKING]"), but without template demonstrating inline position,
  the first-pass vs. collection distinction is weaker. PASS (R-01 requirement met).
- V-05: Phase 3 BLOCKING ITEMS. "Two-checkpoint verification: leading feedback item(s) of each
  card, then the inline [BLOCKING] tag." Ascending NPS order concentrates highest-risk personas
  at top of output. PASS.

---

### R-02: PM and UX roles included — PASS all

All five include PM READ and UX READ, each specified at 2-3 sentences.

Differentiation:
- V-01: PM focuses on adoption strategy and switching-cost blockers. UX focuses on design fit
  and switching friction. Conversational register; framing tied to inertia analysis.
- V-02: PM READ explicitly references Detractor/Passive/Promoter distribution and dominant
  inertia objection pattern. UX READ references severity distribution in Detractor cards.
  Category vocabulary makes reads more structured.
- V-03: PM READ explicitly references `Current approach:` field patterns and migration scope.
  UX READ references gap between current approaches and spec design — conceptual switching cost.
  Named field vocabulary carries through to synthesis reads.
- V-04: Both reads specified at 2-3 sentences; role descriptions standard.
- V-05: Phase 4. Both reads reference specific Phase 2 findings by instruction. PM READ
  references `Current approach:` patterns; UX READ references gap between current approaches
  and spec design.

V-02 and V-05 are strongest: reads are keyed to variation-specific structural vocabulary
(category distribution, `Current approach:` field), not generic role descriptions.

---

### R-03: Theme matrix includes severity distribution — PASS all

All five include "Highest Severity" column in the three-column template.
V-01, V-03, V-05 additionally classify themes as inertia-driven vs. spec-specific.
V-02 classifies themes and also notes whether themes were anticipated vs. emergent.

All exceed the rubric requirement.

---

### A-01: Revision recs for NPS < 6 — PASS V-01/V-02/V-03/V-04/V-05

- V-01: "For any persona whose NPS falls below 6, include a revision recommendation right after
  their feedback items. The recommendation should name the specific section, decision, or design
  choice... 'Improve clarity' or 'simplify the flow' don't count — name the thing." PASS.
- V-02: "For any persona with NPS < 6 (Detractor): include a revision recommendation immediately
  after their items: Revision rec: [specific, actionable change — name the section, decision,
  or design choice and what to change. Not 'improve clarity.' Name the thing.]" PASS.
- V-03: "Revision rec: [specific, actionable change — name the section, decision, or design
  choice and what to change. Not 'improve clarity.' Not 'simplify.' Name the thing and what
  to do.]" Strongest anti-pattern exclusion of the single-pass variations. PASS.
- V-04: "Revision rec: [specific, actionable change — name the section, decision, or design
  choice and what to change. Not 'improve clarity.']" Same standard. PASS.
- V-05: Phase 2 inline REVISION REC + Phase 3 REVISION RECS SUMMARY. Two-pass makes omission
  structurally harder. PASS (also satisfies A-05).

All five pass A-01 in R3. In R2, A-01 was missing from V-01; the R3 V-01 explicitly adds it.

---

### A-02: NPS sensitivity analysis — FAIL V-01/V-02/V-03/V-04; PASS V-05

- V-01 through V-04: No sensitivity analysis section. FAIL.
- V-05: Phase 4 NPS SENSITIVITY ANALYSIS:
  - Identify 2-3 leverage personas. Rationale required: low base, cluster representative, or
    addressable with single inertia-reducing change.
  - Per leverage persona: NPS score, why leverage, highest-ROI change referencing `Current
    approach:` and Revision rec if present.
  - Final: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta],
    moving from [current] to approximately [projected]."
  - V-03's `Current approach:` field per card makes sensitivity analysis more precise in V-05:
    the named field gives concrete inertia data to cite in the ROI calculation. PASS.

A-02 remains exclusive to V-05. New in R3: V-05's sensitivity analysis is anchored to the
`Current approach:` field data, making it more concrete than R2 V-05's version.

---

### A-03: Inline [BLOCKING] flags + escalation collects from them — PASS V-01*/V-02/V-03/V-04*/V-05

Both halves required: (1) inline `[BLOCKING]` marker in cards, (2) escalation section frames
itself as collection pass (not first-pass discovery).

- V-01: "Any blocking-severity item also carries a [BLOCKING] marker inline — this makes the
  escalation section at the end a collection pass, not a first-pass search." Both halves
  explicitly stated. Escalation section: "Collect all [BLOCKING] items from the 12 cards into
  a dedicated section. Because blocking items appear at the top of each card (severity-first
  ordering), this is a scan of each card's leading items for the inline marker."
  Both halves present. Reliability concern: conversational register may reduce consistency
  of inline tag placement vs. template-demonstrated position. PASS* (reliability concern).
- V-02: Card template: `- blocking: [feedback item text] [BLOCKING]`. BLOCKING ITEMS section:
  "Because blocking items appear at the top of each card (severity-first ordering), this is
  a verification pass over each card's leading feedback item(s)." Template-demonstrated
  inline position + collection framing. PASS.
- V-03: Same template as V-02 + same "verification pass" framing. PASS.
- V-04: "Tag every blocking-severity item with [BLOCKING] inline." BLOCKING ITEMS: "Collect
  every item tagged [BLOCKING] from all 12 cards." Both halves present as declarative rules.
  No template demonstrates inline tag position. A-03 first half: the rule says to tag inline,
  but no example shows `[BLOCKING]` appearing immediately after the item text. Reliability
  concern: without template demonstration, inline vs. end-of-card vs. line-prefix placement
  is ambiguous. PASS* (structural reliability unproven for declarative approach).
- V-05: Phase 2: `- blocking: [feedback item text] [BLOCKING]`. Phase 3: "two-checkpoint
  verification: leading feedback item(s) of each card, then the inline [BLOCKING] tag."
  Template-demonstrated + ascending NPS concentrates highest-risk personas at output top.
  PASS.

**R3 finding on V-04:** Declarative rule "tag with [BLOCKING] inline" is present but less
structurally constraining than template demonstration. V-04 is the single-axis test of whether
the rule suffices for A-03. PASS* — compliance requires verification.

---

### A-04: Ascending NPS persona ordering — FAIL V-01/V-02/V-03/V-04; PASS V-05

- V-01: "in this order" — C-01 through C-12. Persona-ID order. No NPS-based sorting. FAIL.
- V-02: No ascending NPS instruction. Card sequence is C-01 through C-12. FAIL.
- V-03: No ascending NPS instruction. FAIL.
- V-04: No ascending NPS instruction. FAIL.
- V-05: Phase 1 lists all 12 scores in ascending order before any card is written. Phase 2:
  "Write feedback cards in the same ascending NPS order from Phase 1 (lowest scorer first)."
  "Tied scores: order by persona ID." Two-phase structure makes ascending order structurally
  reliable: scores are committed and ordered before any feedback is written. PASS.

A-04 remains exclusive to V-05 in R3. The pre-scoring phase is the enabling mechanism:
ascending order requires all scores to be known before ordering can be applied.

---

### A-05: Two-pass revision recommendations — FAIL V-01/V-02/V-03/V-04; PASS V-05

Both passes required: (1) inline within persona card, (2) collected into dedicated summary.

- V-01 through V-04: Revision recs inline only (immediately after feedback items). No
  collection section. FAIL.
- V-05: Phase 2 inline REVISION REC + Phase 3 REVISION RECS SUMMARY: "Collect every REVISION
  REC from Phase 2. List: [C-NN] [Name] (NPS [score]) — [revision rec]. If no persona scored
  below 6: 'No personas below NPS 6.'" Both passes explicit. Phase 3 bundles blocking
  collection (A-03) and revision collection (A-05) in the same structural gate. PASS.

A-05 remains exclusive to V-05 in R3.

---

### A-06: Inertia-baseline NPS justification — PASS all

New in v3 rubric. Pass condition: at least one sentence per card contains explicit comparison
to what the persona currently does or uses (not just persona preference description).

- V-01: Two-tier enforcement: (1) global inertia baseline stated before any cards ("name the
  inertia baseline in a sentence or two: what current workflow, tool, or behavior does this
  feature change or replace?"), (2) per-card NPS justification explicitly required to "directly
  compare this feature against the inertia baseline you named above: does it beat what they
  do today? Is the switching cost worth the net benefit?" Both tiers present in conversational
  prose. PASS (reliability concern: prose framing may produce less consistent comparisons
  than template field).
- V-02: Two-tier enforcement: (1) global SETUP names baseline, (2) NPS band definitions
  make inertia comparison structural: "A Detractor score means the switching cost from their
  current approach exceeds the net benefit. A Promoter score means the net benefit is clear
  enough to overcome switching friction." Every band label IS an inertia comparison label.
  A-06 enforced by category definition — unique mechanism in R3. PASS.
- V-03: No global SETUP. Single-tier enforcement: `Current approach: [1 sentence — what does
  this persona currently do in the area this feature addresses? Name their specific tool,
  workflow, or behavior]`. NPS instruction: "does this feature beat their current approach?
  State the net benefit vs. the switching cost. The comparison must be explicit."
  Per-card named field makes inertia comparison structurally required for each persona
  independently. No shared baseline sentence — each persona names their own current behavior.
  PASS (cleanest per-card specificity of any R3 variation).
- V-04: Global SETUP: "State in 1-2 sentences: what current workflow, tool, or behavior does
  this feature change or replace? This is the inertia baseline." NPS template: "does this
  feature beat their current approach? State the switching cost vs. net benefit explicitly.
  Persona preference description alone does not qualify." Explicit per-card comparison
  required. PASS.
- V-05: Two-tier enforcement: (1) Phase 1 inertia baseline sentence + NPS band annotation
  (category = inertia comparison), (2) Phase 2 `Current approach:` named field per card.
  Doubled: global and per-card. Strongest A-06 structural enforcement of any variation.
  PASS.

**A-06 comparison across R3 variations:**
- V-02: Category-band mechanism — inertia via band definition (global, definitional)
- V-03: Named-field mechanism — inertia via `Current approach:` per card (local, specific)
- V-05: Both mechanisms combined — global band + local named field

All three pass A-06 by different structural paths. V-03's per-card named field produces the
most specific comparisons (each persona's current behavior named separately rather than inferred
from a global baseline). V-02's band definition is the most economical (no extra line per card).

---

### A-07: Severity-first within-card ordering — PASS* V-01/V-04; PASS V-02/V-03/V-05

Pass condition: in any card with a blocking item, the first feedback item is blocking; in any
card with a major item but no blocking item, the first feedback item is major. Rule applies
per card; one out-of-order card fails the whole output.

- V-01: "For each persona's feedback items, list them in descending severity — blocking concerns
  first, then major, then minor, then cosmetic." Present as explicit prose instruction with
  named severity levels in order. No template demonstrates the output form. Reliability concern:
  conversational register may produce unordered lists despite correct instruction. PASS*
  (structurally present, reliability unproven vs. template-demonstrated approach).
- V-02: Template: `Feedback items (descending severity — blocking first): - blocking: [text]
  [BLOCKING] / - major: [text] / - minor: [text] / - cosmetic: [text]`. Template demonstrates
  the exact output structure. Severity order is implicit in line sequence, not just label.
  PASS.
- V-03: Same template as V-02. PASS.
- V-04: "Sort feedback items in descending severity: blocking items first, then major, then
  minor, then cosmetic." Declarative sort rule. Card template: `- [severity: blocking | major
  | minor | cosmetic] [feedback item text]` — shows severity as a label but does NOT
  demonstrate descending ordering (blocking first in list). The rule names the ordering; the
  template does not demonstrate it. This is the critical A-07 test for R3. PASS* (declarative
  rule present; template-demonstration absent; compliance rate TBD vs. template-demonstrated
  approach).
- V-05: Phase 2 template: `Feedback items (descending severity — blocking first): - blocking:
  [text] [BLOCKING] / - major: [text] / - minor: [text] / - cosmetic:`. Same template as
  V-02/V-03. PASS.

**V-04 A-07 finding:** The critical R3 question — is the template structurally load-bearing
for A-07? V-04 tests the declarative rule as the single axis. If A-07 compliance is lower in
V-04 runs than V-02/V-03/V-05 runs, the template demonstration is confirmed as load-bearing
and required for reliable severity-first ordering.

---

## Full Scoring Table

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 All 12 personas | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 Severity tags | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 NPS + justification | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 Aggregate NPS + threshold | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 Theme matrix | 12 | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking escalated | 10 | PASS | PASS | PASS | PASS | PASS |
| R-02 PM + UX reads | 10 | PASS | PASS | PASS | PASS | PASS |
| R-03 Theme matrix severity | 10 | PASS | PASS | PASS | PASS | PASS |
| A-01 Revision recs NPS < 6 | 5 | PASS | PASS | PASS | PASS | PASS |
| A-02 NPS sensitivity | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| A-03 Inline [BLOCKING] | 5 | PASS* | PASS | PASS | PASS* | PASS |
| A-04 Ascending NPS order | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| A-05 Two-pass recs | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| A-06 Inertia baseline NPS | 5 | PASS | PASS | PASS | PASS | PASS |
| A-07 Severity-first within card | 5 | PASS* | PASS | PASS | PASS* | PASS |
| **Score** | **125** | **110** | **110** | **110** | **100** | **125** |

*V-01 A-03 and A-07: structurally present in conversational prose; reliability concern vs.
template-demonstrated position. Predicted score 110 treats PASS* as PASS with caveat:
actual run scores may fall to 100 if either criterion fails in practice.

*V-04 A-03 and A-07: declarative rules without template demonstration. Predicted score 100
treats these as structural reliability questions. If A-07 fails, score drops to 95.

---

## Ranking

| Rank | Variation | Score | Key finding |
|------|-----------|-------|-------------|
| 1 | V-05 | 125 | All 7 aspirational; A-06 doubly enforced via band + named field |
| 2 | V-01 | 110 | All R3 criteria structurally present; conversational register is reliability risk |
| 2 | V-02 | 110 | A-06 via category band definition; A-07 via template; no A-02/A-04/A-05 |
| 2 | V-03 | 110 | A-06 via per-card named field; cleaner per-persona specificity; no A-02/A-04/A-05 |
| 5 | V-04 | 100 | Declarative sort rule unproven for A-07; template confirmed as load-bearing |

---

## Excellence Signals (from V-05)

Patterns from V-05 that explain 125 vs. 110 for V-01/V-02/V-03:

1. **Phase gates enforce completeness** — "Do not proceed to Phase 2 until all 12 scores, their
   ascending-order list, and the aggregate result are stated." Phase 3: "Both outputs complete
   before Phase 4." Checkpoints prevent partial outputs and enforce structural completeness
   across A-02/A-03/A-04/A-05.

2. **Pre-scoring enables authentic ascending order (A-04)** — Phase 1 commits all 12 NPS scores
   before any card is written. Ascending NPS ordering requires all scores to be known. Without
   a dedicated scoring phase, ascending order requires either mental pre-computation or
   post-hoc re-ordering — both less reliable. Phase 1 makes A-04 structurally guaranteed.

3. **A-06 doubly enforced via band + named field** — Phase 1 Detractor/Passive/Promoter band
   annotation makes inertia comparison structural at scoring time. Phase 2 `Current approach:`
   named field makes it explicit per card before the NPS justification is written. Two
   independent structural checkpoints: a justification that passes only one still fails the
   other. This is the V-05 R3 ceiling mechanism.

4. **Phase 3 bundles A-03 and A-05** — BLOCKING ITEMS collection and REVISION RECS SUMMARY
   are required in the same phase gate. Neither can be omitted without abandoning Phase 3
   entirely. A-03 and A-05 second-pass enforcement are structurally coupled: pass or fail
   together.

5. **NPS sensitivity anchored to per-card data (A-02)** — Phase 4 sensitivity analysis
   references `Current approach:` field entries and Revision recs from Phase 2. The named
   field makes the ROI calculation concrete: "Highest-ROI change: [change referencing their
   Current approach: entry]." V-05 R3 sensitivity analysis is more precise than R2 V-05
   because the `Current approach:` field provides specific inertia data per persona.

6. **Two-checkpoint A-03 via ascending NPS + severity-first** — Ascending NPS order puts
   highest-risk personas first. Severity-first within card puts blocking items at card top.
   Phase 3 collection scans leading items of leading cards first. Two redundant structural
   signals: A-03 failure requires both ascending order AND severity-first to misfire
   simultaneously.

---

## New Patterns from R3

### R3 variation findings (single-axis tests)

| Finding | Source | Implication |
|---------|--------|-------------|
| Declarative sort rule insufficient for A-07 reliability | V-04 | Template demonstration is load-bearing for severity-first; future prompts must demonstrate, not just instruct |
| Per-card `Current approach:` field achieves A-06 without global SETUP | V-03 | Global baseline is scaffolding overhead; named field is the minimal sufficient structure |
| NPS category bands enforce A-06 via definition | V-02 | Alternative A-06 path: band label = inertia comparison type; economical (no extra card line) |
| Conversational register carries A-06/A-07 structurally but with reliability risk | V-01 | Register is NOT load-bearing for presence; IS load-bearing for reliability; formal imperative is safer |

### New reusable patterns for future prompts

1. **`nps-category-bands-with-aggregate-mean`** — Assign each NPS score a Detractor (1-6) /
   Passive (7-8) / Promoter (9-10) category annotation. Define the bands in terms of inertia
   comparison: "Detractor = switching cost > net benefit; Promoter = net benefit clears
   switching friction." Use mean of 12 scores for the 7.0 threshold test. Category breakdown
   provides supplemental adoption-readiness signal. Makes A-06 structurally enforced by
   band-definition vocabulary — naming a Detractor score without an inertia comparison
   contradicts the band definition.

2. **`named-current-approach-field-in-phase-card`** — Embed `Current approach: [1 sentence —
   name the specific tool, workflow, or behavior, not general role description]` as a
   named field in the per-persona card template, placed before the NPS justification.
   Each persona names their own inertia baseline independently. When combined with Phase 1's
   global inertia baseline + band annotation, doubles A-06 structural enforcement.
   Standalone (V-03): sufficient for A-06 without global SETUP sentence.
   Combined (V-05): per-card specificity + global framing.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["nps-category-bands-with-aggregate-mean", "named-current-approach-field-in-phase-card"]}
```
