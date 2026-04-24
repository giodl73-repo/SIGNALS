Written to `simulations/quest/rubrics/scout-market-rubric-v5-2026-03-14.md`.

---

**Two new criteria added from R4 excellence signals:**

| ID | Signal | Criterion | Pass mechanism |
|----|--------|-----------|----------------|
| C-18 | ES-07 | Sequencing section uses multi-column table architecture | At least 3 named columns; prose/bullets fail; enables C-16 via column header; orthogonal to C-16 (structure vs. label precision) |
| C-19 | ES-08 | Dual-view -- per-segment cards and cross-segment summary table coexist | Per-cards preserved; summary table self-contained (independently satisfies C-15); Path B (pure wide-table) fails; Path A only |

**Formula updated:** `aspirational_pass/11 * 10` (was `/9`)

**Key structural consequence:** Path B (pure wide-table, V-02/V-04) is now capped at 9/11 = **98.2** — C-19 is structurally unreachable without per-cards. Path A (per-card + summary table, V-01/V-05) is the only architecture that can reach 100 under v5. V-05 remains the golden candidate; its one open question is C-18 (sequencing table format).
 V-04 | PASS | FAIL | 9/11 | 98.2 |
| V-05 | TBD | PASS | TBD | TBD |

V-05 (per-card + explicit label + C-17 chain + post-card summary table) remains golden candidate.
Path to 100 under v5: all eleven aspirational criteria must pass. V-05 + structured sequencing
table architecture yields 11/11 = 100.

---

## Essential Criteria (60 pts total)

All five must pass -- if any fail the output is not useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Segment IDs assigned** | coverage | essential | Every segment has a unique ID (e.g., S1, S2, S3); IDs appear consistently across all tables and the final ranking |
| C-02 | **TAM/SAM/SOM table present** | coverage | essential | A table with TAM, SAM, SOM values exists with one row per segment; no segment is omitted |
| C-03 | **3-dimension fit scoring applied** | correctness | essential | Pain, WTP, and Accessibility are all scored (1-10 scale); composite fit score = arithmetic mean of all three dimensions (no weights); no dimension is missing |
| C-04 | **Composite rank formula applied** | correctness | essential | Rank score = fit score + (10 - GTM difficulty) applied to every segment; final ranking matches the computed values |
| C-05 | **Beachhead recommendation with rationale** | depth | essential | One segment named as beachhead; rationale cites fit score, GTM difficulty, and why this segment is preferred over the highest-WTP segment |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Unit consistency** | correctness | recommended | Tooling segments use developer headcount; platform/enterprise segments use dollar TAM; units are not mixed within the same column of the same table |
| C-07 | **Sequencing path stated** | depth | recommended | A Y1 -> Y2+ adoption sequence is given (e.g., S1 -> S2 -> S3 -> defer S4) with one sentence of justification per transition |
| C-08 | **At least one amendment or open question** | depth | recommended | Phase 4 (or equivalent) lists 1+ concrete next steps to validate or refine the analysis (e.g., price-test assumption, disaggregate a segment, add a dimension) |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Non-obvious insight surfaced** | depth | aspirational | Output surfaces at least one finding that reverses naive intuition (e.g., highest-WTP segment ranks last because GTM difficulty dominates; free model for beachhead locks in methodology before monetization) |
| C-10 | **Revenue model per segment** | coverage | aspirational | Every segment has a stated revenue model (free, freemium, seat license, etc.) and at least one segment has a concrete price point or ARR target |
| C-11 | **STATUS QUO baseline stated before scoring** | depth | aspirational | A do-nothing / status quo cost is named before any fit scoring begins; pain scores or WTP scores for at least one segment are explicitly anchored to switching cost or observable inertia (not abstract ratings); the inertia anchor is traceable to the ranking output |
| C-12 | **Opportunity cost of inaction stated at beachhead** | depth | aspirational | The beachhead recommendation includes a "not building this means..." statement (or equivalent); the cost of deferring the beachhead segment is stated at the decision point -- quantified, estimated, or tied back to the STATUS QUO cost from C-11 |
| C-13 | **Revenue model co-located with WTP score** | coverage | aspirational | Revenue model and price point for each segment appear alongside (or within) the fit scoring view for that segment -- not in a separate trailing table; the co-location makes the WTP-vs-revenue-model comparison visible without cross-referencing; at least one segment shows a concrete price point adjacent to its WTP score; passes via either per-card vertical adjacency or wide-table column adjacency (see C-15) |
| C-14 | **Sequencing transition conditioned on inertia break** | depth | aspirational | The Y1->Y2+ sequencing transitions cite a named observable condition drawn from the STATUS QUO inertia analysis -- not a time-based assumption; at least one transition trigger is traceable to the inertia anchor from C-11 (e.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion"); passes via explicit or implicit trigger field (see C-16 for explicit-only scoring) |
| C-15 | **Unified cross-segment scoring table** | coverage | aspirational | A single table presents WTP, Revenue Model, Price Point, fit score, and GTM difficulty as adjacent columns with one row per segment; no dimension requires lookup in a separate section; direct cross-segment comparison is possible within one view; wide-table format only -- per-card format does not satisfy; three confirmed mechanisms: (1) wide-table as primary scoring view, (2) post-card cross-segment summary table, (3) pure wide-table swap |
| C-16 | **Inertia-break transition label forecloses time-based responses** | depth | aspirational | The sequencing section uses a pre-printed or explicitly-labeled field whose label type requires a named observable condition -- not a free-form justification field; label must be specific enough that "Year 2+" or "when adoption grows" is not a valid response to it (e.g., "Inertia-break condition:", "Named STATUS QUO trigger:"); implicit trigger fields (e.g., "Transition trigger: what inertia barrier is resolved") do not satisfy; two confirmed mechanisms: (1) per-block key-value field, (2) table column header (see C-18) |
| C-17 | **STATUS QUO quantification chain enforced at source and consumption** | depth | aspirational | Two conditions both required: (1) the STATUS QUO section includes a forward-reference instruction that pre-commits to a quantified estimate for use at beachhead (e.g., "required in 'Not building this means:' below -- do not write a vague estimate"); (2) the beachhead "not building this means:" cites the STATUS QUO cost by value and source (e.g., "costing approximately $X from STATUS QUO"); a reminder at consumption only (C-12 standard) does not satisfy this criterion |
| C-18 | **Sequencing section uses multi-column table architecture** | depth | aspirational | The Y1->Y2+ sequencing section is structured as a formal table with at least three named columns (e.g., Stage, Inertia-break condition, Outcome or Target segment); prose sequencing, numbered lists, and single-column bullet structures do not satisfy; the multi-column table creates field-level slots that cannot be bypassed with narrative fallback -- when a column header demands a named condition, no individual row can substitute a time-based value; satisfies via wide-table sequencing (C-16 column header mechanism) or per-card sequencing table with labeled columns; C-14 and C-16 may pass without C-18 if the trigger field appears in prose or inline text |
| C-19 | **Dual-view architecture -- per-segment cards and cross-segment summary table coexist** | coverage | aspirational | The output includes both per-segment card blocks (each with full dimension scoring, revenue model, and price point) AND a separate cross-segment summary table appearing after the per-cards; the summary table is self-contained and independently satisfies C-15; neither view is subordinate to the other -- per-cards are not replaced by the summary table and the summary table is not merely a footnote; pure wide-table architectures that replace per-cards (Path B: V-02, V-04) do not satisfy; per-card-only architectures without a summary table do not satisfy; Path A (V-01, V-05) is the production architecture for this criterion |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-19 that pass   (max 11)

composite = (essential_pass/5    * 60)
          + (recommended_pass/3  * 30)
          + (aspirational_pass/11 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

| Score | Label |
|-------|-------|
| 90-100 | Exemplary |
| 80-89 | Golden (meets threshold) |
| 60-79 | Partial -- review failed essential |
| < 60 | Failing |

---

## Failure Modes (from trace findings)

| Finding | Maps to | Impact if missed |
|---------|---------|-----------------|
| SF-04: Mixes dollar TAM and headcount TAM | C-06 | Recommended fail only; output still useful if fit scoring is correct |
| SF-05: Scoring scale not defined in spec | C-03 | Essential fail if dimensions are absent or composite is not an average |
| SF-06: Artifact path not confirmed | n/a | Not scored; informational |
| R1-P1: No STATUS QUO section | C-11 | Aspirational fail; also gates C-14, C-16, C-17 |
| R1-P2: No "not building this means..." at beachhead | C-12, C-17 | C-12 aspirational fail; C-17 also fails (no consumption anchor) |
| R2-P1: Revenue model in trailing table, not co-located | C-13 | Aspirational fail; C-09 may pass narratively but WTP-vs-model comparison is not forced |
| R2-P2: Sequencing uses time-based transitions, not inertia signals | C-14 | Aspirational fail; C-07 passes but sequencing is not grounded in STATUS QUO analysis |
| R3-P1: No unified cross-segment scoring table | C-15 | Aspirational fail; C-13 may pass via per-card adjacency, but cross-segment comparison requires section lookup |
| R3-P2: Implicit trigger field instead of explicit inertia-break label | C-16 | Aspirational fail; C-14 passes, but label forecloses time-based fallback at deployment scale |
| R3-P3: C-12 quantification reminder at consumption only, no source forward-reference | C-17 | Aspirational fail; C-12 passes (statement exists), but chain enforcement requires both ends |
| R4-P1: Sequencing in prose or bullet list, not a multi-column table | C-18 | Aspirational fail; C-16 may pass via per-block label, but column-header mechanism is unavailable; deployment-scale foreclosure operates at cell level only when column structure exists |
| R4-P2: Pure wide-table architecture replaces per-cards (Path B) | C-19 | Aspirational fail; C-15 still passes; per-segment depth is absent; dual-view Path A required for C-19 |

---

## Calibration Notes

### R1 Calibration

**Top score (R1):** 95 -- V-03 (Inertia framing) and V-05 (Full synthesis) tied.

**What separated the 95s from the 90s:** STATUS QUO section + mandatory inertia anchor column.
Without structural scaffolding, C-09 depends on model discretion; all three 90-point variations
prompted the WTP/GTM comparison but did not force it.

**C-11 independence from C-09:** A variation can pass C-09 (the insight occurs) without passing
C-11 (grounding is present before scoring). V-01, V-02, V-04 all show this -- C-09 PARTIAL
despite prompting the comparison, because inertia was never anchored.

**C-12 independence from C-09 and C-11:** V-05 uniquely surfaces the do-nothing cost a third
time at the beachhead via the "Not building this means:" pre-printed line. The insight is
restated *where the decision is made*, not just in the analysis.

**C-10 gap:** Failed in all five R1 variations. No template included a revenue model field.

### R2 Calibration

**Top score (R2):** 100 (v2 rubric) -- V-02 (Revenue Model Per Segment Card). First perfect
score under the rubric at that time.

**What separated R2-V-02 from R2-V-01 (C-13 delta):** V-01 places revenue model in a standalone
section after COMPOSITE RANK. V-02 embeds revenue model + price point in each per-segment
scoring card alongside WTP. The co-location in V-02 is what makes C-09 structural rather than
narrative -- the juxtaposition forces the model to confront whether a free entry model is
consistent with a high WTP score.

**C-14 evidence:** V-02's sequencing uses an explicit "transition trigger field" in each Y1/Y2+
row. The trigger must reference a named condition, not "Year 2." This is the first variation to
tie sequencing to STATUS QUO inertia analysis rather than arbitrary time periods.

**C-13 + C-14 independence:** C-13 is about where revenue model data appears; C-14 is about what
sequencing justifications cite. A variation could pass C-13 (co-located revenue model) and fail
C-14 (time-based sequencing), or vice versa.

### R3 Calibration

**Top score (R3):** 98.9 -- V-05 (Golden candidate). Per-card + explicit C-14 label +
quantified C-12 chain.

**R3 confirmed two structural paths to C-13:** Wide-table column adjacency (V-01, V-04: WTP |
Revenue Model | Price Point as adjacent columns in one unified scoring row) is architecturally
equivalent to per-card vertical adjacency (V-02, V-05: WTP immediately above Revenue Model and
Price Point within each segment block). C-13 pass condition updated to make both paths explicit.

**C-16 evidence:** V-02 uses a pre-printed "Inertia-break condition:" label. V-04 uses
"Transition trigger: what inertia barrier is resolved or what channel opens" -- an implicit
field. Both pass C-14; only V-02 and V-05 pass C-16. Identical scores under v3 because C-16 did
not exist; now differentiated.

**C-17 evidence (ES-06, V-05):** V-05 uniquely enforces quantification at STATUS QUO with a
forward-reference mandate ("required in 'Not building this means:' below -- do not write a vague
estimate"), and the beachhead statement includes a format-chain citation ("costing approximately
$X from STATUS QUO"). V-02 has a "not building this means:" line (passes C-12) but no source
forward-reference. V-05 is the sole R3 carrier of C-17.

**STATUS QUO gates (v5):** C-11, C-12, C-14, C-16, and C-17 all require STATUS QUO. C-18
requires sequencing table architecture; C-19 requires dual-view. Any template without STATUS QUO
is capped at 4/11 aspirational (C-09, C-10, C-13, C-15 can pass regardless; C-18 requires
sequencing structure but not STATUS QUO; C-19 requires dual-view but not STATUS QUO directly).

**C-15 vs. C-16 vs. C-17 independence:** Each new criterion is structurally orthogonal. C-15
(wide table format) can pass while C-16 fails (implicit trigger in sequencing sub-section). C-16
(explicit label) can pass while C-15 fails (per-card layout). C-17 (chain enforcement) can pass
regardless of format choice. No R3 variation passes all three; each current template embodies
exactly one or two of the new patterns.

### R4 Calibration

**Top score (R4):** 100 (v4 rubric) -- V-01, V-02, V-04, V-05 tied at 9/9 aspirational.
Under v5: V-02 and V-04 drop to 98.2 (C-19 FAIL -- no per-cards). V-01 and V-05 status pending
C-18 evaluation; if sequencing uses multi-column table, both reach 100.

**ES-07 (V-03 / V-04): Table column header is structurally equivalent to per-block field for
C-16.** "Inertia-break condition:" as a sequencing table column header forecloses "Year 2+"
entries at the column level. The mechanism differs (column vs. block) but the label string and
foreclosure effect are identical. Two C-16 mechanisms confirmed: per-block key-value field
(V-02, V-05) and table column header (V-03, V-04). C-18 formalizes the structural requirement
that enables the column-header mechanism: the sequencing section must be a multi-column table.

**ES-08 (V-01 / V-05): Post-card summary table is a valid C-15 path -- does not require
replacing per-cards.** C-15 is satisfied when the summary table is self-contained. The per-cards
remain as supporting depth; the summary table independently meets the criterion. Three C-15
mechanisms confirmed: (1) wide-table primary view, (2) post-card cross-segment summary table,
(3) pure wide-table swap. C-19 formalizes the dual-view requirement: per-cards preserved
alongside a self-contained summary table. Path A (V-01, V-05) satisfies C-19; Path B (V-02,
V-04) does not.

**Path A vs. Path B (v5 distinction):**
- Path A (per-card + summary table): V-01 and V-05 satisfy C-19; both satisfy C-15 via post-card
  summary. The only production architecture that can satisfy all 11 aspirational criteria.
- Path B (pure wide-table): V-02 and V-04 fail C-19 -- no per-cards present. Both satisfy C-15
  via primary wide-table. Ceiling under v5: 9/11 = 98.2 regardless of other passes.

**C-18 and C-16 relationship:** C-18 does not require C-16 to pass. A multi-column sequencing
table satisfies C-18 even if the column header label is implicit (e.g., "Transition trigger"
rather than "Inertia-break condition:"). C-16 then independently tests whether the specific
label forecloses time-based responses. The two criteria are orthogonal: C-18 tests structure;
C-16 tests label precision.

### R1 scores under v5 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R1-V-01 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/11 | 90.0 |
| R1-V-02 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/11 | 90.0 |
| R1-V-03 | PASS | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 2/11 | 91.8 |
| R1-V-04 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/11 | 90.0 |
| R1-V-05 | PASS | FAIL | PASS | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 3/11 | 92.7 |

### R2 scores under v5 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R2-V-01 | PASS | PASS | PASS | FAIL | FAIL | -- | FAIL | FAIL | FAIL | FAIL | FAIL | 3/11 | 92.7 |
| R2-V-02 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | PASS | FAIL | 7/11 | 96.4 |

Note: R2-V-02 drops from 97.8 (v4) to 96.4 (v5) -- C-18 PASS (sequencing table confirmed),
C-19 FAIL (no summary table; per-card only architecture).

### R3 scores under v5 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R3-V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | TBD | FAIL | 7+ | TBD |
| R3-V-02 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | PASS | FAIL | 7/11 | 96.4 |
| R3-V-03 | PASS | PASS | FAIL | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 3/11 | 92.7 |
| R3-V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | TBD | FAIL | 7+ | TBD |
| R3-V-05 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | FAIL | 8/11 | 97.3 |

Note: All R3 C-19 FAIL -- no R3 variation includes a post-card summary table. R3-V-05 drops
from 98.9 (v4) to 97.3 (v5). R3-V-01 and R3-V-04 C-18 pending sequencing format inspection.

### R4 scores under v5 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R4-V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | TBD | PASS | 8+ | TBD |
| R4-V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | 9/11 | 98.2 |
| R4-V-03 | PASS | PASS | FAIL | FAIL | PASS | FAIL | FAIL | PASS | FAIL | PASS | FAIL | 5/11 | 94.5 |
| R4-V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | 9/11 | 98.2 |
| R4-V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | TBD | PASS | 10+ | TBD |

Note: V-01 and V-05 C-18 pending sequencing format inspection. If both PASS: V-01 at 9/11 =
98.2; V-05 at 11/11 = 100. V-05 is the golden candidate for 100 under v5.

### Path to 100 (v5)

Must pass all eleven aspirational criteria. The five structural requirements are:

1. **C-15**: Unified cross-segment scoring table (wide-table format; post-card summary satisfies)
2. **C-16**: Explicit inertia-break label in sequencing (per-block or column header)
3. **C-17**: STATUS QUO quantification chain at source and consumption
4. **C-18**: Sequencing section is a multi-column table (enables column-header C-16; required
   for field-level foreclosure at deployment scale)
5. **C-19**: Dual-view -- per-segment cards AND cross-segment summary table coexist (Path A only)

Path B (pure wide-table) ceiling: 9/11 = 98.2. Cannot satisfy C-19 -- no per-cards present.
Path A (per-card + summary table) can satisfy all 11. V-05 is the candidate: per-card depth +
explicit C-16 label + C-17 quantification chain + post-card summary table (C-15, C-19) + STATUS
QUO baseline. Only open question: whether V-05's sequencing uses multi-column table (C-18).
If yes: 11/11 = 100.
