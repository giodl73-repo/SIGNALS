Written to `simulations/quest/rubrics/quest-score-rubric-v6-2026-03-16.md`.

---

**What changed v5 -> v6:**

Two new Aspirational criteria. N_aspirational: 10 -> 12.

---

**C-19 -- Phase 2 entry gate binary declaration** (correctness)
Source: R5 scorecard MODEL CELL + ENTRY LOCK. The R5 scorer closes the MODEL CELL block with "ENTRY LOCK: no verdict row written before model cell. Confirmed." -- a binary-declaration applied to the Phase 2 entry constraint itself. Extends the same pattern as C-12 (arithmetic: YES|NO) and C-18 (symmetry: Symmetric: YES/NO) to temporal ordering. Distinct from C-14 (placement): C-14 asks whether the anchor is placed at Phase 2 entry -- verifiable by tracing output order. C-19 asks whether the anchor *declares* the constraint was satisfied -- verifiable by scanning for a labeled field.

**C-20 -- Criterion-anchored inertia labels** (behavior)
Source: R5 scorecard inertia labels throughout Phase 1 and Phase 2 entry. Every inertia label in the R5 output names specific criterion IDs: "Inertia (C-01):", "Inertia (C-13, C-15):", "Inertia (C-11, C-14):", "Inertia (C-18):". C-17 requires departure labels; C-20 requires those labels to name which criteria would fail. Distinct from C-17: C-17 prevents the failure mode (no departure label). C-20 makes criterion-coverage auditable -- a reader can verify that every scored criterion appears in at least one inertia label by scanning labels, rather than cross-referencing mechanisms and criteria separately.

**Formula update:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)   <- was /10
```
an
verify that every scored criterion appears in at least one inertia label by scanning labels
rather than cross-referencing mechanisms and criteria separately.

**Formula update:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)   <- was /10
```

---

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PARTIAL counts as 0.5 toward pass count.
FAIL counts as 0.

Scorecard anchor values:
- N_essential = 5
- N_recommended = 3
- N_aspirational = 12

---

## Criteria

### ESSENTIAL -- must all pass

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Rubric load verification** -- the output confirms the rubric was read; lists all criteria IDs and tiers, states the formula, and names the golden threshold before scoring begins | correctness | A load summary block exists (table, list, or prose) that names: (a) all criteria IDs with their tier labels, (b) the exact composite formula text, (c) the golden threshold condition, and (d) the count or list of outputs being scored. PARTIAL if any one of the four is missing. FAIL if the rubric is not referenced at all. |
| C-02 | **Per-criterion verdict matrix** -- every rubric criterion has a PASS/PARTIAL/FAIL verdict for every scored output | correctness | A table, prose block set, or equivalent structure exists where each criterion-output pair has an explicit verdict. No criterion-output cell is blank, merged-without-explanation, or implied. PARTIAL if verdicts exist for all criteria but one or more outputs are absent. FAIL if any criterion row is missing entirely. |
| C-03 | **Evidence for every verdict** -- every PASS/PARTIAL/FAIL verdict is backed by a direct quote, paraphrase, or specific structural reference to the scored output | correctness | No verdict stands alone as a label. Each criterion-output verdict is accompanied by text that references the output specifically -- either a quoted passage, a named section or line, or a structural observation about the output's format or content. PARTIAL if evidence exists for most verdicts but one or more are bare labels without reference. FAIL if a majority of verdicts lack evidence, or if evidence is present but consistently restates the criterion rather than quoting or referencing the output. |
| C-04 | **Composite score per output** -- each scored output has a numeric composite score computed from its verdict counts, shown with explicit calculation | correctness | A score is present for every output. The score is derived from a weighted formula (essential/recommended/aspirational tier counts). The calculation is shown explicitly -- e.g., "V-XX: E=X/5, R=X/3, A=X/12 -> composite = YY" -- not just the final number. PARTIAL if scores are present but calculations are omitted or partial. FAIL if scores are absent for any output. |
| C-05 | **Failure patterns section** -- criteria that receive zero PASS across all scored outputs are identified as failure patterns, or their absence is explicitly stated | coverage | A section labeled "Failure Patterns" (or equivalent) exists. Any criterion receiving no PASS across all N outputs is named. If no such criterion exists, the output states that explicitly (e.g., "No failure patterns -- all criteria passed in at least one output"). FAIL if the section is omitted entirely or if a criterion that failed across all outputs is not surfaced. |

### RECOMMENDED -- output is better with these

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Ranked leaderboard** -- all scored outputs are listed in descending composite score order; ties are noted explicitly | format | A leaderboard or ranking section exists. All N outputs appear, ordered from highest to lowest composite score. Ties are broken (with stated rule) or explicitly noted as tied. PARTIAL if the leaderboard exists but some outputs are absent or the order cannot be verified from stated scores. FAIL if the section is absent or ordering is implicit ("see scores above"). |
| C-07 | **Excellence signals** -- outputs scoring unusually high on a specific criterion are identified; any criterion where one output clearly leads the field is named with the structural feature that produced the outlier | depth | An "excellence signals" section exists. At least one specific output-criterion pair is highlighted with an explanation of what structural feature in that output produced the higher score. Generic comments ("V-05 scored highest overall") do not satisfy this criterion -- the signal must name the criterion and the mechanism. If no outlier pair exists, that is stated explicitly. |
| C-08 | **Per-output synthesis notes** -- each scored output has a brief narrative note explaining its key score drivers: what it did structurally that raised or lowered its score relative to other outputs | depth | A narrative note exists for each output beyond its verdict table or prose blocks. Each note explains at least one structural feature of the output that differentiates its score -- not a restatement of the verdict counts. PARTIAL if notes exist for most but not all outputs, or if notes only list counts without explaining mechanism. |

### ASPIRATIONAL -- raise the bar once essential/recommended are stable

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Regression signals** -- if a prior-round scorecard is provided, any criterion-output pair that degraded from PASS (or PARTIAL) to a lower verdict since the prior round is flagged | behavior | A regression section exists. If prior-round data was provided, any PASS->FAIL or PASS->PARTIAL degradation is named with the criterion ID, output ID, and prior verdict. If no regressions occurred, that is stated. If no prior-round file was provided or available, the output writes "No prior round data -- regression analysis cannot be performed" and the criterion receives PARTIAL (not FAIL). |
| C-10 | **Score arithmetic verification** -- the composite scores in the output are arithmetically correct given the stated verdict counts and formula | correctness | At least one composite score in the output can be independently verified from the stated PASS/PARTIAL/FAIL counts and formula. Arithmetic errors are absent or flagged. PARTIAL if scores are stated without enough detail to verify. FAIL if a score is demonstrably wrong given the stated counts. |
| C-11 | **Evidence positive anchor** -- the scoring output includes at least one worked example demonstrating what constitutes acceptable evidence for a criterion, showing the difference between criterion restatement and genuine output reference | depth | At least one criterion-output pair in the body of the scoring output includes a worked positive example: a model evidence cell that references a specific quote, named section, or locatable structural feature in the scored output. Anti-anchor text alone ("generic observations not tied to specific output text do not qualify") does not satisfy this criterion -- a positive model must exist. PARTIAL if a positive example exists but it is confined to the instructions rather than demonstrated within the scored body. FAIL if no positive evidence model appears anywhere in the output. |
| C-12 | **Discrepancy declaration** -- the arithmetic verification section includes an explicit match/mismatch declaration rather than an implicit pass-through | correctness | The arithmetic verification includes a labeled declaration field -- e.g., "Matches stated score: YES" or "Matches stated score: NO -- discrepancy: stated X, computed Y" -- that requires the scorer to affirm a match or name the exact discrepancy. Narrative statements like "the score checks out" or "verification performed" do not satisfy this criterion. PARTIAL if the match/mismatch is stated clearly in prose but without a labeled declaration field. FAIL if no explicit match/mismatch statement exists in the verification section, or if C-10 was not attempted. |
| C-13 | **Formula version delta declaration** -- when the applied rubric version introduces formula parameter changes from a known prior version, the scoring output explicitly names what changed before any score is computed | correctness | A delta notice appears before or within the Phase 1 LOAD block that names: (a) the prior rubric version or formula parameter value, and (b) the current value -- e.g., "N_aspirational=12 (was 10 in v5)" or "Aspirational denominator changed: 10 -> 12". The notice must appear in the scoring output, not only in the prompt instructions. PARTIAL if the current formula is correctly loaded (C-01 PASS) but no prior-vs-current comparison is made and a version change is in scope. FAIL if a formula version change is in scope and no delta is declared, or if an outdated denominator appears in any computation. When no rubric version change is in scope, write "No prior version delta -- scoring under v[N] as the baseline version" -> PARTIAL (not FAIL). |
| C-14 | **Pre-scoring mechanism placement** -- the evidence positive anchor is positioned at Phase 2 entry, the earliest viable point, so it prevents evidence restatement before it can occur rather than correcting it afterward | correctness | The evidence positive anchor (MODEL CELL or equivalent) appears at or before Phase 2 entry -- in the first criterion-output evidence cell of the scoring section. If the anchor appears mid-way through Phase 2 or later, it cannot prevent earlier cells from containing criterion restatement. Post-scoring verification mechanisms are exempt from this criterion -- by design they belong at Phase 3. PARTIAL if a positive anchor exists (C-11 PASS) but is placed after the first three evidence cells of Phase 2. FAIL if no positive anchor exists in the scored body (implies C-11 FAIL), or if the anchor is deferred entirely to Phase 3 or a post-scoring summary. |
| C-15 | **Symmetric comparison completeness** -- every delta comparison in the output supplies both the prior-state value and the current-state value; naming only the current side of a required contrast does not confirm the transition was registered | correctness | Every comparison the output constructs between a prior state and a current state names both sides explicitly. For formula version comparisons: prior parameter value AND current parameter value. For regression comparisons: prior verdict AND current verdict. For arithmetic discrepancy comparisons: stated score AND computed score. PARTIAL if current-state values are correct and present in all comparisons but prior-state values are absent in one or more comparisons. FAIL if required delta comparisons name only the current side across the majority of comparisons. N/A rule: if no delta comparisons are required in the scoring context, write "No prior-state values available for comparison in this scoring run" -> PARTIAL (not FAIL). |
| C-16 | **Phase-distinct mechanism distribution** -- the scoring output deploys structural enforcement mechanisms at two or more distinct lifecycle phases, distributing prevention across the scoring lifecycle rather than clustering all enforcement at one point | behavior | The output contains identifiable structural enforcement mechanisms at two or more of: Phase 1 (pre-scoring -- formula delta blocks, version declarations, complete load summaries), Phase 2 (during evidence writing -- positive anchor rows, pre-labeled entry cells, model evidence cells that fire before any verdict is written), Phase 3 (post-scoring -- arithmetic re-derivation blocks, discrepancy declaration fields, regression comparison sections). Each qualifying mechanism must actively enforce at least one rubric criterion; bare section headers and boilerplate labels do not qualify. PARTIAL if mechanisms exist at exactly one phase. FAIL if the output contains no identifiable structural enforcement mechanisms beyond the required verdict labels and bare evidence cells (implies C-10, C-11, C-12, C-13, C-14 are all FAIL or PARTIAL from absence). |
| C-17 | **Inertia departure labeling** -- each structural enforcement mechanism in the output is accompanied by a labeled statement of the failure mode it prevents, making the scoring cost of omission visible at the moment of writing | behavior | Each structural enforcement mechanism present in the output includes a labeled statement of the failure mode it prevents -- either a named "Inertia:" label, a "without this mechanism:" clause, or a concrete example of the bare-scorecard output that would result from its absence. PARTIAL if at least one mechanism (but not all mechanisms present in the output) includes a labeled departure explanation. FAIL if no mechanism labels its departure from the bare-scorecard baseline. N/A rule: if the output contains no structural enforcement mechanisms beyond verdict labels (implies C-16 FAIL), write "No mechanisms present -- inertia labeling not applicable" -> PARTIAL (not FAIL). |
| C-18 | **Bilateral symmetry audit sweep** -- the output includes a post-write bilateral audit sweep at at least one phase boundary, producing a per-comparison binary verdict (Symmetric: YES/NO or equivalent) for each required delta comparison | correctness | A bilateral audit sweep exists at Phase 1 exit or Phase 3 exit that checks each comparison in scope for presence of both prior and current state values and records a binary per-comparison verdict. PARTIAL if a bilateral audit exists but covers only a subset of the comparisons in scope -- e.g., formula delta swept but regression and arithmetic discrepancy comparisons not included. FAIL if no bilateral symmetry audit sweep exists -- C-15 compliance relies entirely on prevention mechanisms or author memory, with no independent catch mechanism. N/A rule: if no delta comparisons are in scope for this scoring run, write "No comparisons in scope -- bilateral audit not applicable" -> PARTIAL (not FAIL). |
| C-19 | **Phase 2 entry gate binary declaration** -- the positive anchor at Phase 2 entry includes an explicit binary confirmation that no verdict row was written before it, making the entry constraint declared and scannable rather than inferred from output order | correctness | The positive anchor / MODEL CELL at Phase 2 entry includes a labeled binary gate declaration -- e.g., "ENTRY LOCK: no verdict row written before model cell. Confirmed." or equivalent named field with a binary YES/NO or Confirmed/Violated value. This declaration must be part of the anchor block itself, not a post-hoc annotation elsewhere in the output. PARTIAL if the positive anchor exists at Phase 2 entry (C-14 PASS) but no binary gate declaration accompanies it -- temporal correctness is structurally evident from output order but undeclared. FAIL if no positive anchor exists at Phase 2 entry (implies C-14 FAIL or PARTIAL). N/A rule: if Phase 2 is absent from the scoring output (no outputs scored), write "No Phase 2 in scope -- entry gate declaration not applicable" -> PARTIAL (not FAIL). |
| C-20 | **Criterion-anchored inertia labels** -- each inertia departure label names the specific criterion ID(s) that the associated mechanism enforces, making criterion-coverage auditable by scanning labels rather than by cross-referencing mechanisms and criteria | behavior | Every inertia departure label present in the output names at least one criterion ID in parentheses after the label keyword -- e.g., "Inertia (C-01):" or "Inertia (C-13, C-15):" rather than bare "Inertia:". This enables a reader to verify that every scored criterion appears in at least one inertia label without separately mapping mechanisms to the criteria they enforce. PARTIAL if at least one but not all inertia labels include criterion ID anchoring. FAIL if no inertia label names a criterion ID -- departure labels are present (C-17 PASS or PARTIAL) but none identifies which criterion(s) would fail. N/A rule: if the output contains no structural enforcement mechanisms (implies C-16 FAIL, C-17 N/A-to-PARTIAL), write "No mechanisms present -- criterion-anchored labeling not applicable" -> PARTIAL (not FAIL). |

---

## Weight Summary

| Tier | Criteria | N | Weight |
|------|----------|---|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20 | 12 | 10 |

**Formula (explicit):**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

Score at all essential + all recommended + all aspirational: 100.
Score at all essential + all recommended + no aspirational: 90.
Score at all essential + no recommended + no aspirational: 60.
Golden threshold: all 5 essentials PASS AND composite >= 80.

---

## Scoring Notes

**C-01 (load verification):** The load summary can appear anywhere before the first output
is scored -- preamble, header block, or first phase. What matters is that it precedes scoring,
not that it appears in a specific format.

**C-02 (verdict matrix):** Formats vary -- table cells, prose blocks labeled by output, or
grouped criterion blocks -- as long as every criterion-output combination has a stated verdict.
Implied verdicts ("all PASS") count only when the N is small and the claim is unambiguous.

**C-03 (evidence):** Evidence that restates the criterion ("the output has a leaderboard")
does not satisfy C-03. Evidence must refer to the output's specific content: a quoted phrase,
a section title, a structural observation about the output's layout, or a line-level reference.
The test: could you find the referenced feature in the output using only the evidence text?

**C-04 (composite score):** "Explicit calculation" means the tier counts are stated before the
final score is given (e.g., "E=4/5, R=2/3, A=9/12"). A final number alone is PARTIAL. Note the
aspirational denominator is now 12; any computation using /10 or /8 is a formula version error.

**C-05 (failure patterns):** The section is required even when empty. The correct empty-section
text is: "No failure patterns -- all criteria passed in at least one output." Omitting the
section entirely is FAIL even when the scoring otherwise looks complete.

**C-06 (leaderboard):** A table that happens to be sorted by score satisfies C-06 only if the
sort order is unambiguous. "See scores above" or a pointer to the composite score table does
not satisfy C-06 -- the ranking must be restated as a ranked list or explicitly sorted table.

**C-07 (excellence signals):** "V-05 scored highest overall" is not an excellence signal. An
excellence signal requires a specific output-criterion pairing with a structural explanation.
Example: "V-03 leads on C-18 because it introduces a bilateral sweep table at Phase 1 exit
that produces a per-row Symmetric: YES/NO verdict, making asymmetric comparisons detectable
by column scan rather than by re-reading comparison prose."

**C-08 (per-output notes):** Notes that only list "PASS x4, PARTIAL x1" do not satisfy C-08.
The note must explain what the output did structurally that drove its result.

**C-09 (regression):** Round N/A rule: if no prior-round file exists, writing the prescribed
N/A statement earns PARTIAL. Omitting the section entirely earns FAIL.

**C-10 (arithmetic):** Score this criterion by picking one output and verifying its composite
from the stated counts and formula. PARTIAL if counts are absent (cannot verify). FAIL only
if a demonstrable arithmetic error exists.

**C-11 (evidence positive anchor):** The distinction between C-03 and C-11 is level of
demonstration. C-03 asks: does evidence exist? C-11 asks: does the scoring output model what
good evidence looks like? An output can pass C-03 (evidence is present) while failing C-11
(the scorer never showed what a well-formed evidence cell looks like, so borderline cells
recur across criteria). The positive anchor need not be a separate section -- a criterion-output
cell that is demonstrably complete (specific quote, locatable structural reference) satisfies
C-11 as a model, provided it is not the only non-trivial cell.

**C-12 (discrepancy declaration):** C-12 is a tightening of C-10. C-10 asks: is the arithmetic
correct? C-12 asks: did the scorer declare the result explicitly, in a form that forces a
binary choice? A scorer who writes "the formula gives 91, matching the stated score" satisfies
C-12 at PARTIAL level. A scorer who uses a labeled declaration field with an explicit YES/NO
and discrepancy slot satisfies C-12 at PASS level.

**C-13 (formula version delta):** The N/A rule mirrors C-09: if no prior rubric version is
identifiable from context, write the prescribed baseline statement to earn PARTIAL. Omitting
all version-delta reasoning earns FAIL when a version bump is in scope, PARTIAL when baseline
status cannot be determined.

**C-14 (pre-scoring mechanism placement):** "Phase 2 entry" means the first evidence cell
written in the scoring section -- before any verdicts have been rendered. The three-cell
grace window in the PARTIAL condition exists to accommodate prompt designs that use a brief
preamble before the first full-model cell; this window should not be used to justify deferring
the anchor to mid-scoring.

**C-15 (symmetric comparison completeness):** The most common failure mode is stating the
current value only -- "N_aspirational=12" without "was 10 in v5". This is sufficient for C-01
(the formula is loaded correctly) but not for C-15 (the transition was not confirmed). Score
this criterion by scanning every comparison the output makes: formula parameters, regression
entries, and arithmetic discrepancies.

**C-16 (phase-distinct mechanism distribution):** Count phases, not mechanisms. Two mechanisms
both at Phase 3 count as one phase. One mechanism at Phase 1 and one at Phase 3 count as two
phases. The criterion is met at PASS if any two of the three phases contain at least one active
mechanism. "Active mechanism" means a structural element that enforces a rubric criterion by
making a specific failure mode structurally harder to commit.

**C-17 (inertia departure labeling):** Score this criterion by reading each structural
enforcement mechanism in the output and asking: does this mechanism announce what it prevents?
A labeled inertia failure mode, a "without this mechanism:" clause, or a concrete negative
example all satisfy the condition. An enforcement mechanism that operates silently -- a delta
block with no explanation of why it is there -- does not satisfy C-17 even if it correctly
enforces C-13. PARTIAL is appropriate when only some mechanisms carry departure labels; this
commonly occurs in hybrid designs where one axis applies inertia framing and others do not.

**C-18 (bilateral symmetry audit sweep):** A bilateral audit sweep is distinct from a
bilateral instruction ("write both values"). An instruction asks the scorer to remember;
a sweep checks after the fact and produces a detectable YES/NO record. The sweep format need
not be a table -- a checklist or any structure that produces a per-comparison binary verdict
satisfies the criterion. The key test: could a reader determine which comparisons were
symmetric by scanning the sweep output without reading the underlying comparison prose? The
PARTIAL condition (subset coverage) is the most common failure mode: a scorer who sweeps
formula delta only leaves regression and arithmetic comparisons uncaught.

**C-19 (Phase 2 entry gate binary declaration):** C-19 is a tightening of C-14. C-14 asks:
is the positive anchor placed at Phase 2 entry? C-19 asks: did the anchor declare that it
fired before any verdicts were written? These are separable properties. An output can pass
C-14 (anchor is structurally first in the output) while failing C-19 (no binary declaration
field -- the ordering must be verified by tracing the output rather than by scanning for a
labeled gate). The gate declaration format ("ENTRY LOCK: ... Confirmed" or equivalent) is not
mandated; any named binary field that affirms or denies the entry constraint satisfies the
criterion. A "Violated" or "NO" declaration earns PASS on C-19 (the mechanism reported
accurately) while earning FAIL on C-14 (the placement constraint was breached).

**C-20 (criterion-anchored inertia labels):** C-20 is a tightening of C-17. C-17 asks: does
each mechanism carry a departure label? C-20 asks: does that label name the criterion(s) that
would fail? The criterion-ID anchoring enables completeness auditing: a reader can scan all
"Inertia (C-XX):" labels and check whether the union of criterion IDs covers all scored
criteria. Without anchoring, departure labels explain mechanisms but do not make coverage
gaps visible. PARTIAL is earned when some labels include criterion IDs -- for example, a
prompt that applies C-17 framing to some mechanisms but uses a bare "Inertia:" label for
boilerplate checks.

---

## Design Notes

**Why C-01 (load verification) is Essential, not Recommended:**
The prior cycle showed that scorers who skip or abbreviate the load step produce verdict
matrices with incorrect criterion counts, missing N/A rules, and wrong formula denominators.
A missing load summary is a leading indicator of downstream errors in C-02 through C-04.
Making it Essential surfaces this class of error early.

**Why C-03 (evidence) requires explicit output reference, not restatement:**
The highest-frequency failure mode in the prior cycle (observed across Rounds 1-6) was
scorers writing evidence that restates the criterion name instead of quoting the output.
"The output provides evidence for each verdict" is not evidence; it is circular. The pass
condition is written to force a specific reference because generic observations consistently
produced scorecards that could not drive rubric evolution -- they had no diagnostic content.

**Why C-05 (failure patterns) is Essential:**
Failure patterns are the primary value of batch scoring over single-output scoring. A score
report that does not surface criteria failing across all outputs cannot tell you whether the
rubric has a gap or the skill has a design issue. Without this section, the scoring exercise
cannot produce actionable output.

**Why C-06 (leaderboard) is Recommended, not Essential:**
The leaderboard is a navigation aid, not a primary output. The composite scores in C-04
contain the same information; the leaderboard reorganizes them for readability. A scoring
output missing only the leaderboard is still useful for rubric evolution -- it is degraded,
not broken.

**Why C-11 (evidence positive anchor) is Aspirational, not Recommended:**
C-03 already requires that evidence exists and references the output. C-11 is a quality
multiplier: it asks whether the scoring output itself teaches correct evidence behavior by
demonstrating a complete positive example. This behavior emerged once in Round 1 (V-01,
C-04 CALC slot) as an excellence signal; it is not yet the norm across variations.

**Why C-12 (discrepancy declaration) is Aspirational, not part of C-10:**
C-10 at PASS level already requires arithmetic correctness. C-12 is a structural discipline
criterion: it asks whether the output forces an explicit declaration rather than allowing
a silent pass-through. The Round 1 V-01 excellence signal was the [YES | NO -- discrepancy:]
field, which makes arithmetic errors visible even when the scorer is not looking for them.

**Why C-13 (formula version delta) is Aspirational, not Essential:**
C-01 already requires that the current formula is loaded correctly. C-13 is a versioning
discipline criterion: it asks whether the scorer consciously confirmed they upgraded from the
prior formula parameters. This matters most during rubric evolution (when N values change)
and least when a rubric is applied for the first time.

**Why C-14 (pre-scoring mechanism placement) is Aspirational, not part of C-11:**
C-11 requires that a positive evidence anchor exists somewhere in the scored body. C-14
asks whether that anchor is placed at Phase 2 entry -- the earliest point it can prevent
errors rather than only illustrate them. This temporal property is separable from C-11's
existence property: an output can pass C-11 (anchor exists) while failing C-14 (anchor
fires too late).

**Why C-15 (symmetric comparison completeness) is Aspirational, not part of C-13:**
C-13 already enforces both-sides naming for the specific case of formula version deltas.
C-15 generalizes this requirement to every delta comparison the output constructs. The
R3 V-03 signal (Axis I naming only the current denominator) revealed that this failure mode
is not limited to formula version changes. C-15 is Aspirational rather than an extension of
C-13 because the generalization requires the scorer to audit their entire output for
incomplete comparisons, not just check one block.

**Why C-16 (phase-distinct mechanism distribution) is Aspirational, not part of C-14:**
C-14 requires the positive evidence anchor to be placed at Phase 2 entry. C-16 asks whether
the output as a whole distributes enforcement mechanisms across the lifecycle. An output can
pass C-14 (anchor at Phase 2 entry) while failing C-16 (all other mechanisms at Phase 3,
Phase 1 completely unguarded). C-16 is Aspirational because it requires the scorer to think
about phase coverage holistically.

**Why C-17 (inertia departure labeling) is Aspirational, not part of C-16:**
C-16 requires mechanisms at 2+ distinct phases. C-17 requires each mechanism to document
the failure mode it prevents. An output can pass C-16 (mechanisms at Phase 1 and Phase 2)
while failing C-17 (neither mechanism explains what it prevents -- they are structurally
present but purpose-silent). C-17 is a meta-criterion: it does not require additional
mechanisms, only that existing mechanisms carry departure labels. The R4 V-05 synthesis note
named this pattern explicitly as the expected next criterion. C-17 is Aspirational because
it requires the scorer to understand each mechanism's purpose well enough to articulate the
bare-scorecard failure mode at the point of writing, not just place the mechanism correctly.

**Why C-18 (bilateral symmetry audit sweep) is Aspirational, not part of C-15:**
C-15 requires that both sides of each comparison be present. C-18 requires a structural
catch mechanism that detects asymmetric comparisons at a phase boundary, independent of
whatever prevention mechanisms are in place. An output can pass C-15 (both sides present
through structural enforcement or author memory) while failing C-18 (no sweep -- no
independent verification that prevention succeeded). C-18 is the symmetry analogue of C-12:
just as C-12 added a binary-declaration requirement to C-10's arithmetic correctness, C-18
adds a binary-declaration sweep requirement to C-15's both-sides-present requirement. The
R4 V-03 excellence signal (Axis L SYMMETRY AUDIT SWEEP) was the first observed application
of this pattern class to symmetry verification. C-18 is Aspirational because it requires
deliberate output design beyond what C-15 mandates -- the sweep complements prevention rather
than replacing it, and designing the sweep to cover all comparison types in scope requires
explicit scope planning.

**Why C-19 (Phase 2 entry gate binary declaration) is Aspirational, not part of C-14:**
C-14 requires the positive anchor to be placed at Phase 2 entry -- a structural property
verifiable by reading output order. C-19 requires the anchor to declare the entry constraint
was satisfied -- a self-verification property that makes the temporal ordering checkable by
scanning for a labeled field. An output can pass C-14 (anchor is structurally first) while
failing C-19 (no binary declaration -- the constraint is met but undeclared). C-19 applies
the binary-declaration pattern (established by C-12 for arithmetic and C-18 for symmetry)
to the Phase 2 entry constraint. It is Aspirational because it requires the scorer to add
a labeled self-check to a mechanism that already achieves its structural purpose without one.
The R5 scorecard MODEL CELL + ENTRY LOCK block was the first observed application of this
pattern to the Phase 2 entry gate.

**Why C-20 (criterion-anchored inertia labels) is Aspirational, not part of C-17:**
C-17 requires that each mechanism carry a departure label. C-20 requires that each label
names the criterion(s) that would fail, enabling coverage auditing. An output can pass C-17
(all mechanisms carry departure labels explaining what they prevent) while failing C-20
(no label names a criterion ID -- the explanation is present but not auditable against the
scored criteria list). C-20 is the criterion-coverage analogue of C-18's symmetry audit:
C-18 makes comparison coverage scannable by producing per-comparison binary verdicts; C-20
makes criterion-mechanism coverage scannable by requiring criterion IDs in departure labels.
It is Aspirational because it requires deliberate label design beyond what C-17 mandates --
the criterion-ID anchoring adds no explanatory content to the label but makes structural
completeness auditable. The R5 scorecard's use of "Inertia (C-XX):" labels throughout Phase 1
and Phase 2 was the first observed application of this pattern at full coverage.
