Written to `simulations/quest/variations/prove-analysis-variations-R3-2026-03-14.md`.

---

## Round 3 Variations Summary

| V | Axis | Target | Predicted |
|---|------|--------|-----------|
| **V-01** | Role sequence: mechanism column | C-14 only | 115/130 |
| **V-02** | Output format: falsification chain | C-16 only | 120/130 |
| **V-03** | Phrasing register: two-phase prose audit | C-15 only | 120/130 |
| **V-04** | Role sequence + inertia framing: per-source blocks | C-14 + C-16 | 115–120/130 |
| **V-05** | Multiple combined: full stack | C-14 + C-15 + C-16 | 130/130 |

**Key structural decisions:**

- **V-01** adds one column ("Mechanism adjudication") and one section (MECHANISM VERDICT) to the V-05 (R2) table. Minimal surface area for C-14. C-13 gap persists because the compliance review doesn't name prose sections individually.

- **V-02** adds a FALSIFICATION CHAIN section before the table — each source gets its own null condition block, observation, and verdict. The table copies chain verdicts. C-11 (table) preserved.

- **V-03** splits VOCABULARY COMPLIANCE REVIEW into Phase A (table column) and Phase B (prose sections named individually: proposed mechanism, MECHANISM ANALYSIS, COUNTER-PATTERN SUMMARY, VERDICT). This is the minimal structural change that makes C-15's "outside the table" requirement explicit.

- **V-04** combines C-14 + C-16 in per-source blocks — each block carries both a falsification field and a mechanism adjudication field co-located. C-11 borderline. C-15 not addressed.

- **V-05** stacks all three: preamble pre-registration gate + falsification chain before the table + mechanism adjudication column + two-phase prose audit. Three pre-table structural elements is the density risk.

**The open R3 research question:** Does the column-based adjudication (V-01) produce adequate C-14 per-source coverage, or does cell-space compression disqualify it? This determines whether V-01 reaches 115 or drops lower.
able is filled. V-05 (R2) table format preserved for C-11. C-14 and C-15 not targeted. Predicts 120/130: gains C-16.

**V-03** expands V-05 (R2)'s VOCABULARY COMPLIANCE REVIEW into two named phases. Phase A covers the Relationship type table column. Phase B audits each prose section by name: MECHANISM ANALYSIS sentences, COUNTER-PATTERN SUMMARY entries, VERDICT paragraphs. C-15 requires explicit coverage of relationship claims outside the table -- Phase B provides this. C-14 and C-16 not targeted. Predicts 120/130: gains C-15.

**V-04** uses per-source blocks to combine C-14 and C-16. Phase 1 pre-registers the mechanism. Each source block carries both a Falsification block (source-specific null condition + verdict) and a Mechanism adjudication field (confirmed / not confirmed / silent vs Phase 1 prediction). Phase 3 renders both verdicts. C-11 borderline (labeled fields may qualify). C-15 not targeted. Predicts 120/130 if C-11 awarded; 115/130 if not.

**V-05** is the 130/130 structural candidate. Combines: (1) V-01's pre-registration gate + mechanism adjudication column + MECHANISM VERDICT, (2) V-02's FALSIFICATION CHAIN before the table, (3) V-03's two-phase prose audit. Design question: does three-layer pre-table structure (vocabulary contract, pre-registration gate, falsification chain) plus post-analysis two-phase audit create template density that causes essential criterion compression?

---

## V-01: Pre-Registered Mechanism Column

**Axis:** Role sequence -- mechanism prediction locked in preamble with an explicit gate before any source is named; "Mechanism adjudication" column added to the analysis table so each source adjudicates the pre-stated prediction (confirmed / not confirmed / silent); MECHANISM VERDICT section aggregates per-source adjudications into a synthesis verdict using permitted verdict terms
**Hypothesis:** V-05 (R2) passes C-09 but not C-14 because (a) the preamble mechanism is stated but not explicitly gated as a pre-registration, and (b) per-source mechanism analysis proposes new sentences rather than adjudicating the pre-stated prediction. The minimal fix is two structural changes: a pre-registration gate in the preamble and a new table column. Tests whether column-based adjudication (one cell per source) produces adequate C-14 per-source coverage without requiring a full per-source block restructure.

```
You are running /prove-analysis. Read all sections before filling in any.
This template structurally enforces all analytical obligations. A VOCABULARY CONTRACT applies
throughout. A MECHANISM PREDICTION is registered before any source is named and adjudicated
per source in the table. Complete sections in order -- do not skip forward.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms -- any of these standing alone is a vocabulary error:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED replacement vocabulary -- every relationship claim must use one of:
  "Correlation only: [basis for the limitation]"
  "Association (directional, not causal): [directional claim and basis]"
  "Causal (basis: [evidential or logical justification])"
  "No relationship detected"

This contract applies to: table cells, mechanism entries, counter-pattern entries, synthesis
paragraphs, and verdict sentences. Violations must be corrected before writing VERDICT.

---

## HYPOTHESIS AND MECHANISM PRE-REGISTRATION

Hypothesis: [State the hypothesis in one sentence. Use exact wording from the feature or topic
  context. All patterns in the analysis table bear on this claim.]

Null expectation: [What would the data look like if this hypothesis were false? One sentence.
  This is the comparison baseline for the "Null expectation met?" column below. Fill this in
  before writing any table row. Do not omit.]

Mechanism prediction [Required -- lock before naming any data source]:
  [If this hypothesis is true, what causal chain produces the predicted pattern? State the
  mechanism in one to two sentences as a prediction to be adjudicated, not a post-hoc
  explanation. Format: "If [hypothesis] is true, [mechanism M] operates: [X causes Y], which
  would produce observable evidence [Z] in the available sources."
  If no causal mechanism is plausible: "No causal mechanism is implied -- the relationship
  would be correlational at best because [reason]." State this before the table even if no
  mechanism exists. Do not name any data source in this field.]

MECHANISM PRE-REGISTRATION GATE: Hypothesis, null expectation, and mechanism prediction are
now locked. Do not modify the mechanism prediction after this point. Proceed to the analysis
table and adjudicate the pre-registered prediction per source in the Mechanism adjudication
column.

---

## ANALYSIS TABLE

[All columns required. Fill every cell. Column instructions below.]

| Source | Pattern found | Null expectation met? | Hypothesis bearing | Relationship type | Strength | Mechanism adjudication |
|--------|--------------|----------------------|-------------------|-------------------|----------|------------------------|
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Explicit link -- disconfirmation explained for Null met rows] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [weak/moderate/strong + number, rate, count, or argument] | [Confirmed: [how pattern matches pre-registered prediction] / Not confirmed: [discrepancy from prediction] / Silent: [why source cannot adjudicate]] |
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Explicit link] | [Vocabulary contract terms only] | [Tier + justification] | [Confirmed / Not confirmed / Silent + explanation] |
[Add one row per distinct accessible data source. Minimum two rows required.]

Column instructions:
- **Source** (C-01): Specific named artifact. Not "the data." If you cannot name it, no row.
- **Pattern found** (C-02): What you found. "No pattern detected" if none. No hedging.
- **Null expectation met?** (C-12): "Null met" / "Null not met" / "Ambiguous" -- ambiguous
  requires explanation in Hypothesis bearing.
- **Hypothesis bearing** (C-03): Explicit link. One to two sentences. Do not leave implicit.
  For "Null met" rows: explain what the disconfirmation means.
- **Relationship type** (C-04 + C-13): ONLY vocabulary contract terms. No forbidden terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or logical argument.
- **Mechanism adjudication** (C-14): Compare the pattern in this source to the mechanism
  prediction above. Reference the pre-registered prediction explicitly. Write one of:
  "Confirmed: [how the observed pattern matches the pre-registered mechanism prediction]"
  "Not confirmed: [how the observed pattern diverges from the prediction; be specific]"
  "Silent: [why this source cannot speak to the mechanism -- data type, time window, etc.]"
  Do not propose a new mechanism here. Adjudicate the pre-registered prediction only.

---

## MECHANISM VERDICT [Required]

[Review all Mechanism adjudication cells from the table. Render a synthesis verdict on the
pre-registered mechanism. Reference the count.]

Mechanism confirmed in: [list sources where adjudication was "Confirmed"]
Mechanism not confirmed in: [list sources where adjudication was "Not confirmed"]
Mechanism silent in: [list sources where adjudication was "Silent"]

Mechanism verdict: [Write one of the following permitted verdict terms:]
  "Mechanism established -- [N] of [M] sources confirmed; [basis for sufficiency]"
  "Mechanism plausible but unconfirmed -- consistent in [N] sources but no direct
    confirmation; [what data would establish it]"
  "Mechanism disconfirmed -- [N] of [M] sources showed contradictory patterns;
    [implication for hypothesis: does it fail, or only the proposed mechanism?]"
  "Mechanism untestable with available data -- [data type] needed to adjudicate"

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all rows where "Null expectation met?" is "Null met" and sources with no pattern.
Vocabulary contract applies.]

- [Source (Null met or no pattern)]: [Implication -- genuine limit, scope condition,
  measurement artifact, or evidence against hypothesis?]
[If no sources met the null: "All analyzed sources produced patterns inconsistent with the null
expectation. No disconfirming data found -- genuine gap. Identify at least one source expected
to show the null pattern if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] analyzed sources met the null expectation."
- "[N] of [M] sources produced Mechanism adjudication: Confirmed."
- [Additional quantified claims: rates, counts, percentages, effect sizes as warranted]

---

## VOCABULARY COMPLIANCE REVIEW [Required -- complete before VERDICT]

[Scan all Relationship type cells in the table, all mechanism entries, counter-pattern
sentences, and narrative paragraphs. Report any forbidden term. Correct before VERDICT.]

Compliance: [Write one of:]
  "All Relationship type cells, mechanism entries, counter-pattern sentences, and synthesis
   narrative use vocabulary contract terms. No violations found. Proceeding to VERDICT."
OR
  "[Location]: found '[forbidden term]' -- corrected to '[contract term]'. [Repeat per
   violation.] All violations corrected. Proceeding to VERDICT."

---

## VERDICT

Null summary: "[N] of [M] sources met the null expectation (hypothesis unsupported in those
  sources); [K] did not (consistent with hypothesis)."
Mechanism verdict: [Restate from MECHANISM VERDICT -- one of the four permitted terms.
  Vocabulary contract applies.]
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. Vocabulary contract
  applies. No forbidden terms.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and Relationship type column]
Scope (C-10): [Conditions under which patterns hold and where they may not generalize.
  At least one explicit boundary condition: population, time window, platform, version, or
  configuration constraint. Do not omit.]
Vocabulary: "All relationship claims in this output use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
mechanism_verdict, mechanism_confirmed_count, causal_claim, overall_direction,
vocabulary_compliant: true.
```

---

## V-02: Per-Source Falsification Chain

**Axis:** Output format -- dedicated FALSIFICATION CHAIN section before the analysis table; each source gets a standalone block with a source-specific null condition, the actual observation, and an explicit null verdict; the table copies chain verdicts rather than deriving them from a shared top-level null expectation
**Hypothesis:** V-05 (R2) passes C-12 with one shared null expectation applied to all sources but fails C-16 because C-16 requires each source to carry its own null condition. The structural fix: a named FALSIFICATION CHAIN section forces per-source null conditions before any pattern is analyzed. The chain is upstream of the table -- the model commits to what each source would show if false before observing the pattern. Tests whether a separate chain section (rather than embedded per-source fields) produces adequate C-16 coverage while preserving the V-05 table format for C-11.

```
You are running /prove-analysis. Read all sections before filling in any.
A VOCABULARY CONTRACT governs all relationship language. A FALSIFICATION CHAIN establishes
source-specific null conditions for each source before pattern analysis begins. Complete
sections in order.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED vocabulary -- every relationship claim must use one of:
  "Correlation only: [basis for the limitation]"
  "Association (directional, not causal): [directional claim and basis]"
  "Causal (basis: [evidential or logical justification])"
  "No relationship detected"

This contract applies to all text in this output.

---

## HYPOTHESIS

Hypothesis: [State the hypothesis in one sentence. Use exact wording from the feature or topic
  context. All sources in the falsification chain and analysis table bear on this claim.]

---

## FALSIFICATION CHAIN [Required -- complete before analysis table]

[For each data source you will analyze, complete one block below. Each null condition must be
source-specific -- not a generic expectation shared across all sources. Ask: "If this hypothesis
were false, what would THIS specific source show -- what observable evidence in this artifact,
and no other, would indicate the hypothesis does not hold?"

Add one block per accessible source. Minimum two blocks required. Do not name a source here
that you cannot identify by artifact name. Do not begin the ANALYSIS TABLE until all blocks
are complete.]

---

### Falsification: [SOURCE NAME -- exact artifact identifier]

Source null condition: [If the hypothesis were false, [source name] would show: [X --
  specific to this artifact, not a generic "no pattern." What observable evidence in THIS
  source would signal the hypothesis is false?]]
Observed: [What this source actually shows. State directly before any interpretation.]
Source null verdict: [Write one:]
  "Null met -- disconfirming: [how the observation matches the source null condition]"
  "Null not met -- consistent with hypothesis: [how observation differs from null condition]"
  "Ambiguous -- compatible with both: [explain the ambiguity]"

---

### Falsification: [SOURCE NAME]

Source null condition: [Source-specific null condition for this source.]
Observed: [Direct observation before any interpretation.]
Source null verdict: [Null met / Null not met / Ambiguous + explanation]

---

[Add one block per accessible source. Minimum two. Then proceed to ANALYSIS TABLE.]

---

## ANALYSIS TABLE

[Column instructions -- read before filling any row:]
- **Source** (C-01): Exact source name from the FALSIFICATION CHAIN above. Do not add rows
  for sources not listed in the chain.
- **Pattern found** (C-02): What pattern exists in this source. "No pattern detected" if none.
  Do not hedge.
- **Source null verdict** (C-16): Copy the verdict from the FALSIFICATION CHAIN block for
  this source. Do not rewrite: "Null met" / "Null not met" / "Ambiguous".
- **Hypothesis bearing** (C-03): How the pattern and null verdict together bear on the
  hypothesis. One to two sentences. Explicit link. For "Null met" rows: explain the
  disconfirmation.
- **Relationship type** (C-04 + C-13): ONLY vocabulary contract terms. No forbidden terms.
- **Strength** (C-05): weak / moderate / strong + at least one number, rate, count, or
  logical argument.

| Source | Pattern found | Source null verdict | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|--------------------|--------------------|-------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Bearing -- disconfirmation explained for Null met rows] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [Tier + justification] |
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Bearing] | [Vocabulary contract terms only] | [Tier + justification] |

---

## MECHANISM ANALYSIS [Required]

[For each source with a pattern, write one mechanism sentence. Vocabulary contract applies.
Address each source individually.]

For each source with a pattern:
- [Source name]: [Choose one sentence form:]
  "A plausible cause is [X] because [basis: logical necessity, temporal order, or experimental
    evidence]."
  "This could be explained by [X], but causation cannot be confirmed from this source because
    [reason]."
  "No causal mechanism is apparent because [reason]; the [correlation/association] may reflect
    [confound or shared cause] rather than a direct causal pathway."

Mechanism verdict: ["Mechanism established (N of M sources support)" / "Mechanism plausible
  but unconfirmed" / "Mechanism ruled out (N of M contradictory)" / "Mechanism untestable
  (observational sources only; [data type] needed)"]

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all "Null met" rows from the table and sources with no pattern. Vocabulary contract
applies.]

- [Source (Null met or no pattern)]: [Implication for the hypothesis.]
[If no "Null met" rows: "All sources inconsistent with their source-specific null conditions.
No disconfirming data found -- genuine gap. Name at least one source that would show its null
condition if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition (disconfirming)."
- "[N] of [M] sources produced patterns inconsistent with their null condition (consistent
  with hypothesis)."
- [Additional quantified claims: rates, counts, percentages as warranted]

---

## VOCABULARY COMPLIANCE REVIEW [Required -- complete before VERDICT]

[Scan all Relationship type cells in the table, all mechanism sentences, all counter-pattern
entries, and synthesis narrative. Report any forbidden term. Correct before VERDICT.]

Compliance: ["All Relationship type cells, mechanism sentences, counter-pattern entries, and
  synthesis narrative use vocabulary contract terms. No violations. Proceeding to VERDICT."
OR "[Location]: found '[forbidden term]' -- corrected to '[contract term]'. [Repeat per
  violation.] All violations corrected. Proceeding to VERDICT."]

---

## VERDICT

Null summary: "[N] of [M] sources met their source-specific null condition (disconfirming);
  [K] did not (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. Vocabulary contract
  applies.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and Relationship type column]
Scope (C-10): [Conditions under which patterns hold and where they may not generalize.
  At least one explicit boundary condition: population, time window, platform, version, or
  configuration constraint.]
Vocabulary: "All relationship claims in this output use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
mechanism_verdict, causal_claim, overall_direction, vocabulary_compliant: true.
```

---

## V-03: Two-Phase Narrative Vocabulary Audit

**Axis:** Phrasing register -- vocabulary compliance check split into two named phases; Phase A audits the Relationship type table column; Phase B audits each prose section individually by name (MECHANISM ANALYSIS sentences, COUNTER-PATTERN SUMMARY entries, VERDICT paragraphs); Phase B must report on each section separately; neither phase alone satisfies the audit requirement
**Hypothesis:** V-05 (R2) passes C-13 but its COMPLIANCE REVIEW says "all Relationship type cells, mechanism entries, and counter-pattern sentences" without naming synthesis narrative or verdict paragraphs as discrete audit targets. C-15 requires a compliance check that explicitly covers relationship claims outside the analysis table, naming those sections. A two-phase audit structure names each prose section individually in Phase B, making implicit coverage explicit. Tests whether section-by-section naming in the audit step produces the C-15 structural guarantee that V-05 achieves incidentally for C-13.

```
You are running /prove-analysis. Read all sections before filling in any.
This template structurally enforces all analytical obligations. A VOCABULARY CONTRACT governs
all relationship language. A TWO-PHASE COMPLIANCE AUDIT fires before VERDICT: Phase A covers
the Relationship type table column; Phase B audits each prose section individually by name.
Both phases are required. Complete sections in order.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms -- any of these standing alone is a vocabulary error:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without an explicit type label following]

REQUIRED replacement vocabulary -- every relationship claim must use one of:
  "Correlation only: [basis for the limitation]"
  "Association (directional, not causal): [directional claim and basis]"
  "Causal (basis: [evidential or logical justification])"
  "No relationship detected"

This contract applies to ALL text: table cells, mechanism narrative, counter-pattern entries,
synthesis paragraphs, scope statements, and verdict sentences. No exceptions.

Compliance is verified in two phases before VERDICT. Phase A covers the Relationship type
table column only. Phase B covers every prose section by name. Neither phase alone satisfies
the compliance requirement -- both must run and both must report clear.

---

## HYPOTHESIS AND FALSIFICATION SETUP

Hypothesis: [State the hypothesis in one sentence. Use exact wording from the feature or topic
  context.]

Null expectation: [What would the data look like if this hypothesis were false? One sentence.
  Fill this in before writing any table row. Do not omit.]

Proposed mechanism: [What causal mechanism would produce the pattern if the hypothesis is
  true? One to two sentences. If no mechanism is plausible: "No causal mechanism is implied
  -- the relationship would be correlational at best because [reason]."]

---

## ANALYSIS TABLE

[All columns required. Vocabulary contract applies to all cells.]

| Source | Pattern found | Null expectation met? | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|----------------------|-------------------|-------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Explicit link -- disconfirmation explained for Null met rows] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [weak/moderate/strong + number, rate, count, or argument] |
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Explicit link] | [Vocabulary contract terms only] | [Tier + justification] |
[Minimum two rows. Source = specific named artifact. Not "the data."]

Column instructions:
- **Source** (C-01): Specific named artifact. Not "the data." If you cannot name it, no row.
- **Pattern found** (C-02): What you found. "No pattern detected" if none. No hedging.
- **Null expectation met?** (C-12): "Null met" / "Null not met" / "Ambiguous".
- **Hypothesis bearing** (C-03): Explicit link. One to two sentences.
- **Relationship type** (C-04 + C-13): ONLY vocabulary contract terms. Forbidden terms = error.
- **Strength** (C-05): Tier + at least one number, rate, count, or argument.

---

## MECHANISM ANALYSIS [Required]

[Vocabulary contract applies to all text in this section. For each source with a pattern,
write one mechanism sentence. No forbidden terms.]

For each source with a pattern:
- [Source name]: [Choose one form:]
  "A plausible cause is [X] because [basis: logical necessity, temporal order, or experimental
    evidence]."
  "This could be explained by [X], but causation cannot be confirmed from this source because
    [reason]."
  "No causal mechanism is apparent because [reason]; the [correlation/association] may reflect
    [confound or shared cause] rather than a direct pathway."

Mechanism verdict: ["Mechanism established (N of M sources confirmed)" / "Mechanism plausible
  but unconfirmed" / "Mechanism ruled out" / "Mechanism untestable (observational only;
  [data type] needed)"]

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all "Null met" rows and sources with no pattern. Vocabulary contract applies to
all relationship language here.]

- [Source]: [Implication -- genuine limit, scope condition, measurement artifact, or evidence
  against hypothesis.]
[If no "Null met" rows: "All sources inconsistent with null. No disconfirming data found --
genuine gap. Name at least one source expected to show null pattern."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] analyzed sources met the null expectation."
- [Additional quantified claims: rates, counts, percentages, effect sizes as warranted]

---

## VOCABULARY COMPLIANCE AUDIT [Required -- both phases required before VERDICT]

### Phase A: Table Column Audit

[Review every cell in the Relationship type column of the ANALYSIS TABLE above.]

Relationship type column: [Write one:]
  "All Relationship type cells use vocabulary contract terms. Table column clear."
OR
  "[Row / source name]: found '[forbidden term]' -- corrected to '[contract term]'. [Repeat
   for each cell violation.] Table column violations corrected."

### Phase B: Prose Section Audit

[Audit each prose section below individually by name. For each section, scan every sentence
for relationship claims. Report "Clear" or the specific violation and correction. A compliance
check that covers only the table column does not satisfy Phase B.]

PROPOSED MECHANISM (HYPOTHESIS AND FALSIFICATION SETUP):
  [Clear -- mechanism sentence uses vocabulary contract terms.]
  OR [Violation: found '[forbidden term]' -- corrected to '[contract term]'.]

MECHANISM ANALYSIS -- each mechanism sentence and verdict:
  [Clear -- all mechanism sentences and verdict use vocabulary contract terms.]
  OR [Violation in [source name]: found '[forbidden term]' -- corrected to '[contract term]'.
   [Repeat per sentence.]]

COUNTER-PATTERN SUMMARY -- each entry:
  [Clear -- all entries use vocabulary contract terms.]
  OR [Violation in [source name] entry: found '[forbidden term]' -- corrected to
   '[contract term]'.]

VERDICT paragraphs (pre-audit before writing):
  [Clear -- planned verdict language uses vocabulary contract terms.]
  OR [Planned use of '[forbidden term]' -- will use '[contract term]' instead.]

Phase B status: [Write one:]
  "Phase B complete. All prose sections clear. Proceeding to VERDICT."
OR
  "Phase B complete. [N] violations corrected across prose sections. All sections now clear.
   Proceeding to VERDICT."

---

## VERDICT

Null summary: "[N] of [M] sources met the null expectation (hypothesis unsupported in those
  sources); [K] did not (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. Vocabulary contract
  applies. No forbidden terms.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and Relationship type column]
Scope (C-10): [Conditions under which patterns hold and where they may not generalize.
  At least one explicit boundary condition: population, time window, platform, version, or
  configuration constraint. Do not omit.]
Vocabulary (C-15): "Phase A table column audit and Phase B prose section audit complete.
  All relationship claims in this output use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
mechanism_verdict, causal_claim, overall_direction, vocabulary_compliant: true,
prose_audit_complete: true.
```

---

## V-04: Mechanism Chain + Per-Source Falsification Blocks

**Axes:** Role sequence + inertia framing -- Phase 1 pre-registers the hypothesis and mechanism prediction; Phase 2 analyzes each source using per-source blocks that each carry both a Falsification block (source-specific null condition + verdict) and a Mechanism adjudication field (confirmed / not confirmed / silent vs the Phase 1 prediction); Phase 3 renders both the mechanism verdict and the falsification tally
**Hypothesis:** V-01 adds C-14 to a flat table column. V-02 adds C-16 as a chain before a flat table. The question is whether both criteria are better served by per-source blocks that co-locate the falsification condition and mechanism adjudication within the same structural unit. Co-location forces the model to adjudicate both simultaneously for each source rather than filling two distant columns in a table, potentially producing richer per-source reasoning. Tests whether the V-04 (R2) block format scales to carry two new structural obligations per source without template bloat.

```
You are running /prove-analysis. This template organizes analysis into three phases.
Phase 1 locks the hypothesis and mechanism prediction before any source is named.
Phase 2 analyzes each source with per-source blocks containing both a falsification block
and a mechanism adjudication field. Phase 3 renders both verdicts. A VOCABULARY CONTRACT
applies throughout.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED vocabulary:
  "Correlation only: [basis]"
  "Association (directional, not causal): [claim and basis]"
  "Causal (basis: [justification])"
  "No relationship detected"

Applies to all text. Violations corrected in VOCABULARY COMPLIANCE REVIEW before VERDICT.

---

## PHASE 1: HYPOTHESIS AND MECHANISM PRE-REGISTRATION

Hypothesis: [State the hypothesis in one sentence. Use exact wording from the feature or topic
  context. Do not name any data source in this section.]

Mechanism prediction [Required -- lock before any source is named]:
  [State the causal mechanism that would produce the predicted pattern IF the hypothesis is
  true. One to two sentences as a prediction to be adjudicated, not a post-hoc explanation.
  Format: "If [hypothesis] is true, [mechanism M] operates: [X causes Y], producing
  observable evidence [Z] in the available sources."
  If no causal mechanism is plausible: "No causal mechanism is implied -- the relationship
  would be correlational at best because [reason]." State this before Phase 2 even if
  no mechanism exists. Do not name any data source here.]

Mechanism observable: [Write one:]
  "Yes -- if the mechanism operates, [source types] would show [specific evidence]."
  "Partially -- testable in [source types] but not [others] because [reason]."
  "No -- sources are observational; [data type] would be needed to adjudicate."

PHASE 1 GATE: Hypothesis and mechanism prediction locked. Do not name or analyze any source
until this gate is complete.

---

## PHASE 2: PER-SOURCE ANALYSIS

[For each accessible data source, complete one full source block below. Minimum two blocks
required. Do not begin Phase 3 until all source blocks are complete.

Each block carries two required structural elements:
  1. Falsification block (C-16): source-specific null condition, direct observation, verdict
  2. Mechanism adjudication (C-14): comparison to the Phase 1 mechanism prediction

Do not share null conditions across sources -- each must be specific to the source it
describes. Do not propose a new mechanism in the adjudication field -- adjudicate the
Phase 1 prediction only.]

---

### SOURCE: [SOURCE NAME -- exact artifact identifier]

**Source** (C-01): [Specific named artifact -- file, table, schema, scenario set, log, test
  suite. Not "the data." If you cannot name it, do not use this source block.]

**Falsification block** (C-16):
  Source null condition: [If the hypothesis were false, this source would show: [X --
    specific to this artifact, not a generic null. What would THIS source show,
    specifically, if the hypothesis does not hold?]]
  Observed: [What this source actually shows. State directly before any interpretation.]
  Source null verdict: [Write one:]
    "Null met -- disconfirming: [how the observation matches the source null condition]"
    "Null not met -- consistent with hypothesis: [how observation differs from null]"
    "Ambiguous: [explain compatibility with both]"

**Pattern found** (C-02): [What pattern was found. "No pattern detected" if none.
  Do not hedge. State the finding without reference to the falsification block.]

**Hypothesis bearing** (C-03): [How the pattern and falsification verdict together bear on
  the hypothesis. One to two sentences. Explicit link -- start with "This bears on the
  hypothesis because..." or equivalent. For "Null met" blocks: explain what disconfirmation
  means.]

**Relationship type** (C-04): [Vocabulary contract terms only. Write one:]
  "Correlation only: [why causation cannot be inferred from this source]"
  "Association (directional, not causal): [directional claim and its basis]"
  "Causal (basis: [logical or evidential justification])"

**Mechanism adjudication** (C-14): [Compare the pattern in this source to the Phase 1
  mechanism prediction. Reference the pre-registered prediction explicitly. Write one:]
  "Confirmed: [how the observed pattern matches the pre-registered mechanism prediction]"
  "Not confirmed: [how the observed pattern diverges from the prediction; be specific]"
  "Silent: [why this source cannot speak to the mechanism -- data type, time window, etc.]"
  Do not propose a new mechanism. Adjudicate the Phase 1 prediction only.

**Strength** (C-05): [Tier: weak / moderate / strong + at least one number, rate, N of M,
  effect size, p-value, or logical argument. Not "significant" without backing.]

**Counter-evidence** (C-07): [Data in this source that weakens or contradicts the pattern.
  Or: "No counter-evidence -- [reason why absence is plausible or a genuine gap]."]

[Repeat from "### SOURCE: [SOURCE NAME]" for each accessible data source.]

---

## PHASE 3: SYNTHESIS AND VERDICTS

### Mechanism Verdict (C-14)

[Review all Mechanism adjudication fields from Phase 2.]

Mechanism confirmed in: [list sources where adjudication was "Confirmed"]
Mechanism not confirmed in: [list sources where adjudication was "Not confirmed"]
Mechanism silent in: [list sources where adjudication was "Silent"]

Mechanism verdict: [Write one permitted verdict term:]
  "Mechanism established -- [N] of [M] sources confirmed; [basis for sufficiency]"
  "Mechanism plausible but unconfirmed -- consistent in [N] sources, no direct confirmation;
    [what data would establish it]"
  "Mechanism disconfirmed -- [N] of [M] sources contradicted the prediction; [implication
    for hypothesis]"
  "Mechanism untestable with available data -- [data type] needed"

### Falsification Tally (C-16)

Null met in: [list sources where source null verdict was "Null met"]
Null not met in: [list sources where source null verdict was "Null not met"]
Ambiguous in: [list sources where source null verdict was "Ambiguous"]

Falsification summary: "[N] of [M] sources met their source-specific null condition
  (disconfirming); [K] did not (consistent with hypothesis)."

### Overall Synthesis

Overall direction: [Support / Contradict / Inconclusive] -- [two to three sentences drawing
  on Phase 2 source patterns, falsification tally, and mechanism verdict. Vocabulary contract
  applies.]
Causal claim: [Yes / No / Partial] -- [cite Phase 3 mechanism verdict; one sentence basis]
Scope (C-10): [Conditions under which patterns hold and where they may not generalize.
  At least one explicit boundary condition: population, time window, platform, configuration,
  or version constraint.]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition."
- "[N] of [M] source blocks produced Mechanism adjudication: Confirmed."
- [Additional quantified claims: rates, counts, percentages, effect sizes as warranted]

---

## VOCABULARY COMPLIANCE REVIEW [Required -- complete before writing artifact]

[Scan all Relationship type fields from Phase 2, all mechanism adjudication entries, all
counter-evidence entries, and all Phase 3 synthesis paragraphs. Report any forbidden term.
Correct before writing the artifact.]

Compliance: ["All relationship fields, mechanism adjudications, counter-evidence entries,
  and synthesis text use vocabulary contract terms. No violations. Proceeding to artifact."
OR "[Location]: found '[forbidden term]' -- corrected to '[contract term]'. [Repeat per
  violation.] All violations corrected. Proceeding to artifact."]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, mechanism_verdict, sources_count, null_met_count,
null_not_met_count, mechanism_confirmed_count, causal_claim, overall_direction,
vocabulary_compliant: true.
```

---

## V-05: Full 130/130 Stack

**Axes:** Multiple combined -- V-05 (R2) base with all three structural upgrades: (1) mechanism pre-registration gate in preamble + "Mechanism adjudication" column in table + MECHANISM VERDICT section (C-14); (2) FALSIFICATION CHAIN section before the table with per-source null condition blocks (C-16); (3) two-phase compliance audit naming each prose section individually in Phase B (C-15)
**Hypothesis:** Each new criterion is targeted individually in V-01 through V-03. V-04 combines C-14 and C-16 in per-source blocks. V-05 tests whether all three can be stacked in a table-format template without essential criterion failures. Design prediction: the three pre-table structural layers (vocabulary contract, pre-registration gate, falsification chain) reinforce rather than compete -- both the mechanism pre-registration and the falsification chain require preamble commitment before the table, so they share structural position rather than adding length. The two-phase audit is a post-analysis step with no interaction cost. The 130/130 risk is template density at the preamble stage causing the model to compress or skip the falsification chain.

```
You are running /prove-analysis. Read ALL sections before filling in any.
This template enforces all analytical obligations across three structural layers:
  (1) A VOCABULARY CONTRACT covers all text with a TWO-PHASE PROSE AUDIT before VERDICT
  (2) A MECHANISM PREDICTION is pre-registered before any source is named and adjudicated
      per source in the analysis table
  (3) A FALSIFICATION CHAIN establishes source-specific null conditions before the table
Complete sections in the order written. Do not skip forward.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED replacement vocabulary -- every relationship claim must use one of:
  "Correlation only: [basis for the limitation]"
  "Association (directional, not causal): [directional claim and basis]"
  "Causal (basis: [evidential or logical justification])"
  "No relationship detected"

This contract applies to: table cells, mechanism text, falsification chain entries,
counter-pattern entries, synthesis paragraphs, and verdict sentences. No exceptions.

Compliance verified in two phases before VERDICT. Phase A audits the Relationship type
table column. Phase B audits each prose section individually by name. Both are required.

---

## HYPOTHESIS AND PRE-REGISTRATION SETUP

Hypothesis: [State the hypothesis in one sentence. Use exact wording from the feature or
  topic context. All analysis below bears on this claim.]

Mechanism prediction [Required -- lock before naming any source]:
  [If this hypothesis is true, what causal chain produces the predicted pattern? One to two
  sentences as a prediction to be adjudicated, not a post-hoc explanation.
  Format: "If [hypothesis] is true, [mechanism M] operates: [X causes Y], producing
  observable evidence [Z] in available sources."
  If no mechanism is plausible: "No causal mechanism is implied -- the relationship would
  be correlational at best because [reason]." State before the falsification chain even
  if absent. Do not name any data source here.]

Mechanism observable: [Write one:]
  "Yes -- if the mechanism operates, [source types] would show [specific evidence]."
  "Partially -- testable in [source types] but not [others] because [reason]."
  "No -- sources observational; [data type] would be needed."

PRE-REGISTRATION GATE: Mechanism prediction locked. Do not name any data source before
this gate. Proceed to the FALSIFICATION CHAIN.

---

## FALSIFICATION CHAIN [Required -- complete before analysis table]

[For each source you will analyze, state the source-specific null condition below. Each
null condition must be specific to that source -- not a generic expectation shared across
sources. Ask: "If the hypothesis were false, what would THIS specific source show, and
no other?" Minimum two blocks. Do not begin the ANALYSIS TABLE until all blocks are
complete.]

---

### Falsification: [SOURCE NAME -- exact artifact identifier]

Source null condition: [If the hypothesis were false, [source name] would show: [X --
  observable and specific to this artifact. Not "no pattern" -- what specific observation
  in THIS source would indicate the hypothesis is false?]]
Observed: [What this source actually shows -- state directly, before interpretation.]
Source null verdict: [Write one:]
  "Null met -- disconfirming: [how observation matches null condition]"
  "Null not met -- consistent with hypothesis: [how observation differs from null condition]"
  "Ambiguous: [explain compatibility with both]"

---

### Falsification: [SOURCE NAME]

Source null condition: [Source-specific null condition.]
Observed: [Direct observation before interpretation.]
Source null verdict: [Null met / Null not met / Ambiguous + explanation]

---

[Add one block per accessible source. Minimum two. Then proceed to ANALYSIS TABLE.]

---

## ANALYSIS TABLE

[All columns required. Fill every cell. Column instructions below.]

| Source | Pattern found | Source null verdict | Hypothesis bearing | Relationship type | Strength | Mechanism adjudication |
|--------|--------------|--------------------|--------------------|-------------------|----------|------------------------|
| [Name] | [Pattern or "No pattern detected"] | [Copy from Falsification Chain: Null met / Null not met / Ambiguous] | [Explicit link -- disconfirmation explained for Null met rows] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [weak/moderate/strong + number, rate, count, or argument] | [Confirmed: [match to pre-registered prediction] / Not confirmed: [discrepancy] / Silent: [why source cannot adjudicate]] |
| [Name] | [Pattern or "No pattern detected"] | [Copy from Falsification Chain] | [Explicit link] | [Vocabulary contract terms only] | [Tier + justification] | [Confirmed / Not confirmed / Silent] |
[One row per source in the Falsification Chain. Do not add rows for unnamed sources.]

Column instructions:
- **Source** (C-01): Exact artifact name from Falsification Chain. Not "the data."
- **Pattern found** (C-02): What you found. "No pattern detected" if none. No hedging.
- **Source null verdict** (C-16): Copy from Falsification Chain. Do not rewrite.
- **Hypothesis bearing** (C-03): Explicit link. One to two sentences. For "Null met" rows:
  explain what the disconfirmation means for the hypothesis.
- **Relationship type** (C-04 + C-13): ONLY vocabulary contract terms. No forbidden terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or logical argument.
- **Mechanism adjudication** (C-14): Compare pattern to pre-registration in HYPOTHESIS AND
  PRE-REGISTRATION SETUP. Reference the pre-stated prediction explicitly. Write one of:
  "Confirmed: [how pattern matches the pre-registered prediction]"
  "Not confirmed: [how pattern diverges from the pre-registered prediction; be specific]"
  "Silent: [why source cannot speak to the mechanism]"
  Do not propose a new mechanism. Adjudicate the pre-registered prediction only.

---

## MECHANISM VERDICT [Required]

[Review all Mechanism adjudication cells. Render synthesis verdict. Vocabulary contract
applies.]

Mechanism confirmed in: [list sources where adjudication was "Confirmed"]
Mechanism not confirmed in: [list sources where adjudication was "Not confirmed"]
Mechanism silent in: [list sources where adjudication was "Silent"]

Mechanism verdict (C-14): [Write one permitted verdict term:]
  "Mechanism established -- [N] of [M] sources confirmed; [basis for sufficiency]"
  "Mechanism plausible but unconfirmed -- consistent in [N] sources, no direct confirmation;
    [what data would establish it]"
  "Mechanism disconfirmed -- [N] of [M] sources showed contradictory patterns; [implication
    for hypothesis]"
  "Mechanism untestable with available data -- [data type] needed"

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all "Null met" rows from the table and sources with no pattern. Vocabulary contract
applies.]

- [Source (Null met or no pattern)]: [Implication -- genuine limit, scope condition,
  measurement artifact, or evidence against hypothesis?]
[If no "Null met" rows: "All sources inconsistent with their source-specific null conditions.
No disconfirming data found -- genuine gap. Name at least one source expected to show its
null condition if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition (disconfirming)."
- "[N] of [M] sources produced Mechanism adjudication: Confirmed."
- [Additional quantified claims: rates, counts, percentages, effect sizes as warranted]

---

## VOCABULARY COMPLIANCE AUDIT [Required -- both phases required before VERDICT]

### Phase A: Table Column Audit

[Review every cell in the Relationship type column of the ANALYSIS TABLE.]

Relationship type column: [Write one:]
  "All Relationship type cells use vocabulary contract terms. Table column clear."
OR
  "[Row / source]: found '[forbidden term]' -- corrected to '[contract term]'. [Repeat for
   each cell violation.] Table column violations corrected."

### Phase B: Prose Section Audit

[Audit each prose section below individually by name. Scan every sentence for relationship
claims. Report "Clear" or the specific violation and correction for each section.
A compliance check covering only the table column does not satisfy Phase B.]

HYPOTHESIS AND PRE-REGISTRATION SETUP -- mechanism prediction:
  [Clear.] OR [Violation: found '[forbidden term]' -- corrected to '[contract term]'.]

FALSIFICATION CHAIN -- null condition sentences (all blocks):
  [Clear -- all null condition and observed sentences use vocabulary contract terms.]
  OR [Block [source name]: found '[forbidden term]' -- corrected to '[contract term]'.]

MECHANISM VERDICT -- verdict sentence and rationale:
  [Clear.] OR [Violation: found '[forbidden term]' -- corrected to '[contract term]'.]

COUNTER-PATTERN SUMMARY -- all entries:
  [Clear.] OR [Entry [source name]: found '[forbidden term]' -- corrected to '[contract term]'.]

VERDICT (pre-audit):
  [Clear -- planned verdict language uses vocabulary contract terms.]
  OR [Planned use of '[forbidden term]' -- will use '[contract term]' instead.]

Phase B status: [Write one:]
  "Phase B complete. All prose sections clear. Proceeding to VERDICT."
OR
  "Phase B complete. [N] violations corrected across prose sections. All sections now clear.
   Proceeding to VERDICT."

---

## VERDICT

Falsification summary (C-16): "[N] of [M] sources met their source-specific null condition
  (hypothesis unsupported in those sources); [K] did not (consistent with hypothesis)."
Mechanism verdict (C-14): [Restate from MECHANISM VERDICT -- one of the four permitted terms.
  Vocabulary contract applies.]
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. No forbidden terms.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and Relationship type column]
Scope (C-10): [Conditions under which patterns hold and where they may not generalize.
  At least one explicit boundary condition: population, time window, platform, version, or
  configuration constraint. Do not omit.]
Vocabulary (C-15): "Phase A table column audit and Phase B prose section audit complete.
  All relationship claims in this output use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
mechanism_verdict, mechanism_confirmed_count, causal_claim, overall_direction,
vocabulary_compliant: true, prose_audit_complete: true.
```

---

## Round 3 Design Notes

### New criteria mapping

| New criterion | Structural guarantee required | Single-axis variation |
|---------------|------------------------------|----------------------|
| C-14 (pre-registered mechanism) | Mechanism locked in preamble gate + per-source adjudication + synthesis verdict | V-01 |
| C-15 (document-wide vocabulary audit) | Two-phase audit: table column Phase A + prose sections named individually Phase B | V-03 |
| C-16 (per-source falsification) | FALSIFICATION CHAIN before table with source-specific blocks | V-02 |

### C-14 structural test: column adjudication vs block adjudication

| | V-01 (table column) | V-04 (per-source block) |
|-|--------------------|-----------------------|
| Adjudication location | One column cell per row | Dedicated labeled field inside block |
| Co-location with falsification | No -- separate columns | Yes -- both fields inside same block |
| Pre-registration gate | Yes -- preamble gate | Yes -- Phase 1 gate |
| C-11 risk | None -- table preserved | Borderline -- "labeled fields qualifies" |

Key question: Does the cell-space constraint in V-01 produce compressed adjudications
that fail the per-source reference requirement? Or is one cell per source sufficient?

### C-15 structural test: named sections vs implicit coverage

V-05 (R2) compliance review covers "mechanism entries and counter-pattern sentences" but
does not name verdict paragraphs or synthesis narrative as discrete audit targets.
V-03 (R3) Phase B names: PROPOSED MECHANISM, MECHANISM ANALYSIS, COUNTER-PATTERN SUMMARY,
VERDICT paragraphs. Key question: does naming each section individually produce a genuine
C-15 compliance check, or does the model produce pro-forma "Clear" for each section?

### C-16 structural test: chain-before-table vs per-source block embedding

| | V-02 (chain before table) | V-04 (block embedding) |
|-|--------------------------|------------------------|
| Table format | Preserved (C-11 intact) | Not a table (C-11 borderline) |
| Source-specificity | Chain instructs non-generic null | Block field instructs non-generic null |
| Pre-analysis commitment | Chain complete before table | Falsification field precedes pattern field |
| C-14 co-location | No (separate section) | Yes (both fields inside block) |

### Predicted R3 differentiation under v3 rubric (130 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-05 (essential, 60) | 60 | 60 | 60 | 60 | 60 |
| C-06 through C-08 (recommended, 30) | 30 | 30 | 30 | 30 | 30 |
| C-09 (mechanism) | 5 | 5 | 5 | 5 | 5 |
| C-10 (scope) | 5 | 5 | 5 | 5 | 5 |
| C-11 (structured format) | 5 | 5 | 5 | 0* | 5 |
| C-12 (null/falsification) | 5 | 5 | 5 | 5 | 5 |
| C-13 (vocabulary precision) | 0 | 5 | 5 | 0 | 5 |
| C-14 (pre-registered mechanism) | 5 | 0 | 0 | 5 | 5 |
| C-15 (document-wide vocab audit) | 0 | 0 | 5 | 0 | 5 |
| C-16 (per-source falsification) | 0 | 5 | 0 | 5 | 5 |
| **Predicted total** | **115** | **120** | **120** | **115/120*** | **130** |

*V-04 C-11: borderline. If "numbered block with labeled fields qualifies" applies: 120/130.
If C-11 denied: 115/130. V-04 C-13: no vocabulary contract applied to Phase 3 synthesis
narrative -- compliance review covers Phase 2 fields only.

V-01 C-13: vocabulary compliance review covers table cells and mechanism entries but does
not name prose sections individually -- same C-13 gap as R2 V-01. C-15 fails.

### V-golden candidate prediction

**V-05** is the 130/130 structural candidate. All three new aspirational criteria are
pre-printed structural requirements. The design question is whether three pre-table
structural elements (vocabulary contract, pre-registration gate, falsification chain)
create preamble density that causes the model to compress or skip the table.

**V-02** and **V-03** are the single-criterion candidates at predicted 120/130, each closing
exactly one new criterion without disturbing the others.

**V-01** is the conservative 115/130 estimate -- gains C-14 but still misses C-13 (no
named-section prose audit). If the compliance review is scored as passing C-13 under
V-05 (R2) interpretation, V-01 would reach 120/130. The scoring boundary is the same
question as R2: does "mechanism entries and counter-pattern sentences" implicitly cover
narrative prose, or must each section be named?

### Open research questions for R3

1. Does V-01's table column adjudication produce adequate C-14 depth (explicit per-source
   reference to the pre-stated mechanism), or does cell compression fail the pass condition?
2. Does V-02's FALSIFICATION CHAIN section (separate from the table) produce equivalent C-16
   coverage to V-04's embedded falsification fields?
3. Does V-03's Phase B audit produce genuine per-section C-15 coverage, or does the model
   produce pro-forma "Clear" entries without meaningful review of each named section?
4. Does V-05's preamble density (vocabulary contract + pre-registration gate + falsification
   chain) cause essential criterion failures from output compression?
5. What is V-04's C-11 verdict under the "numbered block with labeled fields qualifies"
   interpretation with eight labeled fields per block?
