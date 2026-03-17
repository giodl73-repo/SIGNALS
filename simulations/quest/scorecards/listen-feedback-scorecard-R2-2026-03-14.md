Scorecard written to `simulations/quest/scorecards/listen-feedback-scorecard-R2-2026-03-14.md`.

---

**Results:**

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-05 (Combined ceiling) | 115 |
| 2 | V-03 (Severity-first) | 100 |
| 3 | V-01, V-02, V-04 | 95 / 95 / 95* |

**All 5 essential criteria pass across all variations.** All 3 recommended criteria pass. Variance is entirely aspirational.

**Key findings:**

- **V-03 reaches A-03 without phase gates.** A single format rule — severity descending within cards + `[BLOCKING]` inline tag — is sufficient. No ascending NPS ordering, no phase structure required. Simpler path to 100 than anything in R1.
- **V-05 reaches 115 via compounding effects.** Inertia baseline anchors NPS quality; pre-scoring Phase 1 makes ascending order structurally reliable; Phase 3 bundles A-03 + A-05 collection in the same gate; NPS sensitivity analysis requires computed ROI, not observation.
- **R1 V-01 failure corrected.** R2 V-01 adds A-01 explicitly — the 90→95 delta is entirely explained by adding revision recs for NPS < 6.

**New patterns from R2 V-05:**

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["inertia-baseline-setup-before-scoring", "severity-first-within-card-plus-blocking-tag"]}
```
t) |
| New A-03 path | n/a | V-03 proves single-rule path to A-03 without phase gates |

---

## Criterion-by-Criterion

---

### C-01: All 12 stock personas included — PASS all (nominal)

All five variations enumerate all 12 personas explicitly. V-01 through V-05 use the same
pipe-delimited single-line listing in STOCK PERSONAS / PERSONAS section.

V-04 risk: compressed format has no explicit "all 12 cards required before any aggregate
section" stop. A model run could stop at 8-10 without structural enforcement catching it.
Nominal PASS; compliance rate lower than structural variations.

All others include: "All 12 cards required before any aggregate section."

---

### C-02: Every feedback item has a severity tag — PASS all (nominal)

- V-01: `[severity: blocking | major | minor | cosmetic]` per item in card template.
- V-02: Same severity tag format in STEP 3 card template.
- V-03: `Feedback items (descending severity — blocking first): - blocking: [text] [BLOCKING]`
  — severity-first ordering makes the severity label structurally load-bearing.
- V-04: `- [severity: blocking | major | minor | cosmetic] [feedback item]` — present but
  compressed. Lower enforcement reliability.
- V-05: Phase 2 descending severity listing. [BLOCKING] inline flag adds a second enforcement
  layer for the blocking tier.

V-03 and V-05 are strongest: the severity label determines card ordering, making it
structurally required rather than a formatting reminder.

---

### C-03: NPS per persona with justification — PASS all

- V-01: `NPS: [1-10] — [1-2 sentences: does this feature beat their status quo? What is the
  switching cost vs. the net benefit?]` — justification is explicitly a comparison, not free
  text. Inertia framing raises the quality floor on every justification.
- V-02: `NPS: [1-10] — [1-2 sentences... Ground the score in their specific role — do not
  echo the PM or UX read.]` — anti-echo directive constrains quality.
- V-03: `NPS: [1-10] — [1-2 sentences... Do not restate the number — explain what about the
  spec produced this reaction.]` — anti-restatement directive.
- V-04: `NPS: [1-10] — [justification grounded in persona role, goals, or anxieties]` —
  compressed but field present with grounding requirement.
- V-05: Two-part: Phase 1 rationale (status-quo comparison, 1 sentence), Phase 2 card header
  restates Phase 1 score. Score committed before feedback written, preventing post-hoc
  rationalization.

V-01 and V-05 produce the highest-quality justifications because every NPS rationale is
anchored to an inertia comparison, not just a persona description.

---

### C-04: Aggregate NPS computed and threshold applied — PASS all

- V-01: End of document, both threshold branches scripted.
  `"Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."` Explicit.
- V-02: STEP 6, after blocking items. Both branches.
- V-03: After PM READ and UX READ. Both branches. Explicit fail language.
- V-04: After all cards. Both branches. Compressed but formula-correct.
- V-05: End of Phase 1 — aggregate computed and result stated before any feedback cards.
  Phase gate: "Do not proceed to Phase 2 until all 12 scores, their ascending-order list,
  and the aggregate result are stated." Strongest enforcement position.

V-05 is structurally strongest: aggregate NPS is a Phase 1 output, making it a pre-condition
for feedback rather than a post-hoc summary.

---

### C-05: Cross-persona theme matrix — PASS all

All five include the three-column template (Theme | Personas | Highest Severity) with
"minimum one theme required."

V-01 and V-05 additionally classify themes as inertia-driven vs. net-new objections,
exceeding the rubric requirement. V-02 instructs whether themes were anticipated by the
pre-persona PM/UX reads or emerged independently.

---

### R-01: Blocking issues escalated to dedicated section — PASS all

- V-01: `BLOCKING ITEMS:` section. Zero-result scripted.
- V-02: STEP 5. Zero-result scripted.
- V-03: BLOCKING ITEMS explicitly framed as a verification pass: "Because blocking items
  appear at the top of each card (severity-first ordering), this section is a verification
  pass — scan each card's first item(s), collect what is tagged." R-01 and A-03 first-half
  both satisfied by the same instruction.
- V-04: BLOCKING ITEMS section, zero-result scripted. Compressed.
- V-05: Phase 3 BLOCKING ITEMS. Two-checkpoint verification described: "first item(s) of
  each card, then the inline [BLOCKING] tag." Zero-result scripted.

V-03 and V-05 are strongest: escalation is framed as tag-collection (verification), not
first-pass discovery. This simultaneously satisfies R-01 and the second half of A-03.

---

### R-02: PM and UX roles included — PASS all

All five include both PM READ and UX READ with 2-3 sentences each.

- V-01: PM focuses on inertia objections and switching-cost blockers. UX focuses on severity
  distribution and switching friction. Inertia-specific framing differentiates.
- V-02: PM and UX precede all persona cards. Unique axis: professional synthesis before
  customer reactions. Explicitly noted: "PM reads do not affect aggregate NPS."
- V-03: PM focuses on blocking/major count and distribution. UX focuses on leading items.
  Severity-framed synthesis.
- V-04: Role and length specified. Compressed.
- V-05: Phase 4. Both reads reference specific Phase 2 findings by instruction.

---

### R-03: Theme matrix includes severity distribution — PASS all

All five include "Highest Severity" as a column. V-03 adds an explicit annotation instruction.
V-01 and V-05 add inertia-driven vs. net-new classification, exceeding R-03.

---

### A-01: Revision recs for NPS < 6 — PASS V-01/V-02/V-03/V-05; PARTIAL V-04

- V-01: Explicit revision rec format with anti-pattern: "name the section, decision, or
  design choice that is causing the low score and what to change. Not 'improve clarity.'"
  Placed immediately after feedback items. PASS.
- V-02: Same phrasing and anti-pattern. PASS.
- V-03: "Revision rec: [specific, actionable change — name the section, decision, or design
  choice. Not 'improve clarity.' Name the thing and what to do.]" Strongest specificity
  requirement of the non-V-05 variations. PASS.
- V-04: `NPS < 6: add "Revision rec: [specific, actionable change]."` — parenthetical in card
  template, anti-pattern exclusion absent. Likely passes in most runs but structural
  enforcement weaker. PARTIAL.
- V-05: Phase 2 inline REVISION REC + Phase 3 REVISION RECS SUMMARY. Two-pass enforcement
  makes omission structurally harder. PASS.

**Note vs. R1:** R1 V-01 failed A-01 entirely (no revision rec instruction). R2 V-01 adds it
explicitly. The 90 → 95 delta from R1 to R2 for the inertia variation is entirely explained
by this addition.

---

### A-02: NPS sensitivity analysis — FAIL V-01/V-02/V-03/V-04; PASS V-05

- V-01 through V-04: No sensitivity analysis section. FAIL.
- V-05: Phase 4 NPS SENSITIVITY ANALYSIS:
  - Identify 2-3 leverage personas with rationale (low base, cluster representative,
    addressable with single inertia-reducing change)
  - Highest-ROI change per leverage persona
  - Final: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta],
    moving from [current] to approximately [projected]"
  - Format fully prescribed: three named per-persona fields plus final aggregate lift. PASS.

A-02 remains exclusive to V-05 in R2. Same finding as R1.

---

### A-03: Inline [BLOCKING] flags + escalation draws from them — FAIL V-01/V-02/V-04; PASS V-03/V-05

Both halves required: inline `[BLOCKING]` marker in cards AND escalation section frames
itself as a tag-collection pass (not first-pass discovery).

- V-01: No inline [BLOCKING] instruction. Blocking section is discovery, not collection. FAIL.
- V-02: No inline [BLOCKING] instruction. Blocking section is discovery. FAIL.
- V-03: Card template: `- blocking: [feedback item text] [BLOCKING]` — inline flag explicit.
  Blocking section: "Because blocking items appear at the top of each card (severity-first
  ordering), this section is a verification pass — scan each card's first item(s), collect
  what is tagged." Both halves present. PASS.
- V-04: No inline [BLOCKING] instruction. FAIL.
- V-05: Phase 2: `- blocking: [feedback item text] [BLOCKING]`. Phase 3: "Collect every item
  marked [BLOCKING] from Phase 2. Because blocking items appear at the top of each card
  (severity-first ordering), this is a two-checkpoint verification: first item(s) of each
  card, then the inline [BLOCKING] tag." Both halves, plus ascending NPS order compounds
  the effect. PASS.

**Central R2 finding:** V-03 achieves A-03 without ascending NPS ordering or phase gates.
A single format rule (severity-first + [BLOCKING] inline tag) is sufficient for A-03. V-05
proves that combining this with ascending NPS order adds a second structural checkpoint but
is not required for A-03 alone.

---

### A-04: Ascending NPS persona ordering — FAIL V-01/V-02/V-03/V-04; PASS V-05

- V-01 through V-04: No ascending NPS ordering instruction. Default C-01 → C-12 ordering.
  FAIL.
- V-05: Phase 1 lists all 12 scores in ascending order before any card is written. Phase 2
  cards follow the same ascending order from Phase 1. Tied scores ordered by persona ID.
  Two-phase structure makes ascending ordering structurally reliable: scores are committed
  before ordering is applied. PASS.

The pre-scoring phase is necessary for A-04 reliability. Without it, the model must either
pre-compute all NPS values mentally before writing any card, or re-order post-hoc — both
less reliable than committing scores first and then ordering.

---

### A-05: Two-pass revision recommendations — FAIL V-01/V-02/V-03/V-04; PASS V-05

Both passes required: inline within persona card AND collected into dedicated summary section.

- V-01 through V-04: Revision recs inline only. No collection phase. FAIL.
- V-05: Phase 2: "For any persona with NPS < 6: include a REVISION REC immediately after
  their feedback items." Phase 3 REVISION RECS SUMMARY: "Collect every REVISION REC from
  Phase 2. List: [C-NN] [Name] (NPS [score]) — [revision rec]. If no persona scored below 6:
  'No personas below NPS 6.'" Both passes explicit. Summary may be a pointer list. PASS.

Phase 3 bundles blocking item collection and revision rec collection in the same gate,
making both A-03 and A-05 second halves structurally required at the same checkpoint.

---

## Full Scoring Table

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 All 12 personas | 12 | PASS | PASS | PASS | PASS* | PASS |
| C-02 Severity tags | 12 | PASS | PASS | PASS | PASS* | PASS |
| C-03 NPS + justification | 12 | PASS | PASS | PASS | PASS* | PASS |
| C-04 Aggregate NPS + threshold | 12 | PASS | PASS | PASS | PASS* | PASS |
| C-05 Theme matrix | 12 | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking escalated | 10 | PASS | PASS | PASS | PASS | PASS |
| R-02 PM + UX reads | 10 | PASS | PASS | PASS | PASS | PASS |
| R-03 Theme matrix severity | 10 | PASS | PASS | PASS | PASS | PASS |
| A-01 Revision recs NPS < 6 | 5 | PASS | PASS | PASS | PARTIAL | PASS |
| A-02 NPS sensitivity | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| A-03 Inline [BLOCKING] | 5 | FAIL | FAIL | PASS | FAIL | PASS |
| A-04 Ascending NPS order | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| A-05 Two-pass recs | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| **Score** | **115** | **95** | **95** | **100** | **95*** | **115** |

*V-04: essential criteria nominally present but structural enforcement weaker. Actual run
scores may fall below 95 if model stops before 12 personas (C-01) or omits threshold
statement (C-04).

---

## Ranking

| Rank | Variation | Score | Key finding |
|------|-----------|-------|-------------|
| 1 | V-05 | 115 | All 5 aspirational; inertia + severity-first creates dual A-03 checkpoints |
| 2 | V-03 | 100 | A-03 via severity-first alone — no phase gates, no ascending NPS required |
| 3 | V-01 | 95 | A-01 corrected vs. R1; inertia improves quality, not structure |
| 3 | V-02 | 95 | PM/UX-first is a role-sequence quality axis; no new structural criteria |
| 3 | V-04 | 95* | Compression reveals which instructions are load-bearing; reliability TBD |

---

## Excellence Signals (from V-05)

Patterns that explain the V-05 score of 115 vs. V-03 at 100:

1. **Pre-scoring phase enables authentic ascending order** — Phase 1 commits all 12 NPS
   scores before any card is written. Ascending NPS ordering (A-04) requires all scores to
   be known. Without a dedicated scoring phase, ordering is either optimistic (model sorts
   internally without committing scores) or post-hoc (re-ordering after writing). Phase 1
   makes ascending order structurally guaranteed.

2. **Inertia baseline anchors NPS quality** — A single sentence at the top of Phase 1:
   "State in 1-2 sentences: what current workflow or approach does this feature change or
   replace? This is the inertia baseline." Forces every NPS rationale to name a comparison,
   not just describe persona reactions. Produces more discriminating scores and surfaces
   switching-cost objections that abstract evaluation misses.

3. **Severity-first + ascending NPS = dual A-03 checkpoint** — In V-03, A-03 is satisfied
   by severity position alone (blocking at card top). In V-05, ascending NPS order puts the
   lowest-NPS personas first — those most likely to have blocking items appear at the top of
   the output. Severity-first then puts their blocking items at the top of each card. The
   Phase 3 collection pass has two redundant structural signals to scan. A-03 failure
   requires both to misfire simultaneously.

4. **Phase 3 bundles A-03 and A-05 second halves** — BLOCKING ITEMS collection and
   REVISION RECS SUMMARY are both required in Phase 3. Neither can be skipped without
   skipping the phase. This makes A-03 and A-05 enforcement structurally coupled — pass or
   fail together.

5. **NPS sensitivity analysis with prescribed format** — Three named fields per leverage
   persona plus a final aggregate lift estimate. A vague observation ("C-03 seems important")
   cannot pass. The prescribed format requires the model to compute and name the ROI of each
   single change, not just observe that some personas scored lower.

---

## New Patterns from R2 V-05

Beyond the R1 V-05 patterns (inline-blocking-flags, ascending-nps-priority-ordering,
two-pass-revision-recs), R2 V-05 introduces:

1. **`inertia-baseline-setup-before-scoring`** — A 1-2 sentence status-quo statement placed
   before any NPS scores are generated. All scores become net-benefit comparisons rather
   than feature-satisfaction ratings. Implementation: "State in 1-2 sentences: what current
   workflow or approach does this feature change or replace? This is the inertia baseline.
   Every NPS score is a comparison against it." Applicable to any /listen:feedback skill
   variant where adoption friction is a risk.

2. **`severity-first-within-card-plus-blocking-tag`** — Combining descending severity
   ordering within cards (`- blocking: [text] [BLOCKING] - major: [text]...`) with an inline
   [BLOCKING] tag creates dual structural enforcement for A-03. V-03 proved this works as a
   single-rule path to A-03 without phase gates. V-05 integrates it with ascending NPS order
   so lowest-NPS personas appear first AND their blocking items appear at top of card —
   two-checkpoint verification with compounded reliability.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["inertia-baseline-setup-before-scoring", "severity-first-within-card-plus-blocking-tag"]}
```
