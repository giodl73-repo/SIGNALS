Written to `simulations/quest/variations/prove-analysis-variations-R2-2026-03-14.md`.

---

## Round 2 Variations -- prove-analysis

| V | Axis | Core mechanism | Primary target | Predicted score |
|---|------|----------------|----------------|-----------------|
| **V-01** | Output format + inertia (R1 prescribed hybrid) | V-05 null-table + post-table MECHANISM [Required] + QUANTIFIED CLAIMS [Required] | C-09 closed without losing C-08 | 110/115 |
| **V-02** | Phrasing register: vocabulary lock | Pre-printed VOCABULARY CONTRACT + per-row "Relationship type" column + compliance check step before VERDICT | C-13 (vocabulary precision) | 105/115 |
| **V-03** | Inertia framing: per-source falsification blocks | Mini null block per source (own null condition, not shared) + Mechanism field inside each block | C-12 per-source depth; C-09 incidental | 110/115 |
| **V-04** | Role sequence: mechanism-first | Mechanism predicted before any source examined; per-source "Expected if mechanism operates" + Mechanism status adjudication | C-09 as organizing frame | 90/115 |
| **V-05** | Multiple combined: full aspirational stack | Null table + vocabulary contract + mechanism section + compliance check + scope block | All five aspirational (115/115 attempt) | 115/115 |

---

**Key design decisions:**

**V-01** executes the exact hybrid the R1 scorecard prescribed: V-05 null-table base, post-table MECHANISM [Required] with three sentence templates, QUANTIFIED CLAIMS [Required]. This closes C-09 without any structural cost to C-01 through C-08. The mechanism templates ("A plausible cause is..." / "This could be explained by... but cannot be confirmed because..." / "No causal mechanism is apparent because...") are the exact C-09 pass condition sentences pre-printed as options.

**V-03** strengthens C-12 relative to V-01/V-05: each source gets its own null condition ("if this specific source did not support the hypothesis, it would show X") rather than one shared null expectation. This may produce richer falsification reasoning or may produce formulaic per-source repetition -- the open research question for R2.

**V-04** is the inversion test: mechanism stated before data, sources evaluated as mechanism confirmations or refutations. Predicted to lose C-11 (no fixed-column table structure) and C-12 (mechanism status is not falsification framing), but produce the deepest C-09 content.

**V-05** is the 115/115 structural candidate. The open question is whether the stacked vocabulary contract + null table + mechanism section + compliance audit + scope block produces output complexity that causes the model to compress or skip sections under output-length pressure.
e running /prove-analysis. Fill in the pre-printed template below.
All column headers are fixed. Fill in every cell for every data source row.
State the null expectation before filling any rows.
Do not rename, reorder, omit, or leave blank any column.

---

## HYPOTHESIS

Hypothesis: [State the hypothesis in one sentence. All patterns in the analysis table bear on
  this claim. Use exact wording from the feature or topic context.]

Null expectation: [What would the data look like if this hypothesis were false? One sentence.
  This is the comparison baseline for every "Null expectation met?" cell in the table below.
  Fill this in before writing any table row. Do not omit.]

---

## ANALYSIS TABLE

[Column instructions -- read before filling any row:]
- **Source** (C-01): Name the specific artifact: file name, table name, schema, scenario set,
  telemetry log, test suite, or system. Not "the data." Not "existing telemetry." If you cannot
  name it, you do not have access to it -- do not add a row for it.
- **Pattern found** (C-02): State what pattern exists in this source. Write "No pattern detected"
  if none. Do not hedge.
- **Null expectation met?**: Compare the pattern to the null expectation stated above. Write:
  -- "Null met" -- data matches the null; this source does not support the hypothesis
  -- "Null not met" -- data differs from the null; source is consistent with the hypothesis
  -- "Ambiguous" -- compatible with both; explain in the Hypothesis bearing column
- **Hypothesis bearing** (C-03): How this pattern bears on the hypothesis. One to two sentences.
  Explicit link required -- do not leave the connection implicit. For "Null met" rows, explain
  what the disconfirmation means.
- **Correlation or causal?** (C-04): Write one of:
  -- "Correlation only" -- [state why causation cannot be inferred from this source]
  -- "Association (directional, not causal)" -- [state the directional claim and its basis]
  -- "Causal (basis: [one clause])" -- [state the logical or evidential basis]
  Do not write "relationship" without this label. Do not omit.
- **Strength** (C-05): Write weak / moderate / strong + at least one of: a number, rate, count,
  or logical argument. Do not write "significant" or "notable" without backing.

| Source | Pattern found | Null expectation met? | Hypothesis bearing | Correlation or causal? | Strength |
|--------|--------------|----------------------|-------------------|------------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Bearing -- for Null met rows explain disconfirmation] | [Correlation only / Association / Causal (basis: ...)] | [Tier + justification] |
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Bearing -- for Null met rows explain disconfirmation] | [Correlation only / Association / Causal (basis: ...)] | [Tier + justification] |
[Add one row per distinct accessible data source. Minimum two rows required.]

---

## MECHANISM [Required]

[For each source with a pattern in the table, write one mechanism sentence. Do not omit this
section. For correlation-labeled rows: rule out the mechanism or name the confound. For causal-
labeled rows: state the mechanism that produces the effect. Sources with no pattern: skip.]

For each source with a pattern:
- [Source name]: [Choose one sentence form:]
  "A plausible cause is [X] because [basis -- logical necessity, temporal order, or experimental
    evidence]." (use when mechanism can be proposed)
  "This could be explained by [X], but causation cannot be confirmed from this source because
    [reason -- observational data, shared confound, reverse causation possible, etc.]." (use when
    mechanism is plausible but not confirmable from this source)
  "No causal mechanism is apparent because [reason]; the correlation may reflect [confound or
    shared cause] rather than a direct causal pathway." (use when no plausible mechanism exists)

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all rows where "Null expectation met?" is "Null met" or where no pattern was detected.
These are the disconfirming data. Do not omit this section.]

- [Source (Null met or no pattern)]: [What this disconfirmation implies for the hypothesis --
  is this a genuine limit, a scope condition, a measurement artifact, or evidence against
  the hypothesis?]
[If no sources met the null: "All analyzed sources produced patterns inconsistent with the null
expectation. No disconfirming data was found in the available sources -- this is a genuine gap.
Identify at least one source that would be expected to show the null pattern if the hypothesis
does not hold."]

---

## QUANTIFIED CLAIMS [Required]

[At least one numeric claim must appear here. Extract from the table or state directly.
Vague qualifiers alone ("most", "often", "sometimes") do not satisfy this section.]

- [Quantified claim: "N of M sources showed patterns inconsistent with the null expectation",
  "X% of scenarios...", "N cases out of M...", "effect size N", "p < N", etc.]
[Add additional quantified claims as warranted by the data.]

---

## VERDICT

Null summary: "[N] of [M] analyzed sources met the null expectation (hypothesis unsupported
  in those sources); [K] did not (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence summary]
Causal claim supportable: [Yes / No / Partial] -- [one sentence basis citing the table labels
  and the mechanism section]
Scope: [Conditions under which these patterns hold and where they may not generalize --
  population, time window, platform, or configuration constraints.]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
causal_claim, overall_direction.
```

---

## V-02: Vocabulary-Locked Table

**Axis:** Phrasing register -- pre-printed VOCABULARY CONTRACT governing all relationship language
throughout the output; five-column table with "Relationship type" column restricted to contract
vocabulary; post-table compliance check step before proceeding to verdict
**Hypothesis:** C-13 (vocabulary precision) requires that no unclassified hedged relationship term
stands alone in the output. Instruction-based phrasing advice ("use precise vocabulary") is
insufficient because the model will follow the spirit but not the letter when under compositional
pressure. Structurally pre-printing the forbidden terms and their required replacements -- and adding
a dedicated compliance check step -- forces the model to audit its own output against the contract
before advancing. Tests whether a vocabulary contract as a structural element (rather than an
instruction) produces complete C-13 compliance across all relationship claims.

```
You are running /prove-analysis. Fill in the pre-printed template below.
A VOCABULARY CONTRACT governs all relationship language in this output.
Read the contract before filling in any section. The compliance check step fires before VERDICT.

---

## VOCABULARY CONTRACT

The following terms are FORBIDDEN as standalone relationship characterizations:
  "appears related"        "suggests a link"       "may indicate"
  "seems to affect"        "could suggest"          "implies a connection"
  "points toward"          "is associated with"    [without an explicit type label following it]

Every relationship claim in this output must use one and only one of:
  "Correlation only: [basis for the limitation]"
  "Association (directional, not causal): [directional claim and its basis]"
  "Causal (basis: [evidential or logical justification])"
  "No relationship detected"

If you are tempted to write a forbidden term, replace it immediately with the closest permitted
type and add the required qualifier. This contract applies to ALL text in this output: table
cells, counter-pattern entries, mechanism notes, and verdict paragraphs.

---

## HYPOTHESIS

Hypothesis: [State the hypothesis in one sentence. All patterns in the analysis table bear on
  this claim.]

---

## ANALYSIS TABLE

[Column instructions -- read before filling any row:]
- **Source** (C-01): Specific named artifact: file name, table name, schema, scenario set,
  telemetry log, test suite. Not "the data." Not "existing telemetry." If you cannot name it,
  do not add a row.
- **Pattern found** (C-02): What you found. Write "No pattern detected" if none. Do not hedge.
- **Hypothesis bearing** (C-03): How this pattern bears on the hypothesis. One to two sentences.
  Explicit link required. Do not leave the connection implicit.
- **Relationship type** (C-04 + C-13): Use ONLY vocabulary contract terms. Write one of:
  "Correlation only: [basis]" / "Association (directional, not causal): [claim]" /
  "Causal (basis: [justification])" / "No relationship detected"
  No other terms permitted. Forbidden terms in this column are an automatic compliance violation.
- **Strength** (C-05): weak / moderate / strong + at least one of: number, rate, count, or
  logical argument. Do not write "significant" or "notable" without backing.

| Source | Pattern found | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|-------------------|-------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [How this bears on hypothesis] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [Tier + justification] |
| [Name] | [Pattern or "No pattern detected"] | [How this bears on hypothesis] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [Tier + justification] |
[Add one row per distinct accessible data source. Minimum two rows required.]

---

## COUNTER-PATTERNS [Required]

[Note data that weakens, contradicts, or limits the patterns in the table. At least one entry.
Vocabulary contract applies to all relationship language here.]

- [Source]: [Data that weakens or limits the pattern. Or: "No counter-evidence in this source
  -- [reason why absence is plausible or a genuine gap]."]
[One entry per source where counter-evidence exists or was sought and not found.]

---

## QUANTIFIED CLAIMS [Required]

[At least one numeric claim. Vague qualifiers alone do not satisfy this section.]

- [Quantified claim with number: "N of M sources showed...", "X% of scenarios...",
  "N cases out of M...", "effect size N", "p < N", etc.]

---

## VOCABULARY COMPLIANCE CHECK [Required -- complete before VERDICT]

[Review every cell in the Relationship type column and every sentence in COUNTER-PATTERNS.
Flag any cell or sentence that contains a forbidden term or uses an unclassified relationship
characterization. Correct violations before writing VERDICT. Report the compliance status.]

Compliance status:
[Write one of:]
  "All Relationship type cells and counter-pattern entries use vocabulary contract terms.
   No violations found. Proceeding to VERDICT."
OR
  "[Source name], Relationship type column: found '[forbidden term]' -- corrected to
   '[contract term]'. [Repeat for each violation.] All violations corrected. Proceeding to VERDICT."

---

## VERDICT

Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. Vocabulary contract
  applies. No forbidden terms.]
Causal claim supportable: [Yes / No / Partial] -- [one sentence basis citing the table]
Scope: [Conditions under which patterns hold and where they may not generalize.]
Vocabulary: "All relationship claims in this output use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, causal_claim, overall_direction,
vocabulary_compliant: true.
```

---

## V-03: Per-Source Falsification Blocks

**Axis:** Inertia framing -- instead of V-05's single null expectation stated once before the table,
each source gets its own mini falsification block stating the null condition specific to that source,
the actual observation, and an explicit null verdict before any pattern analysis begins
**Hypothesis:** V-05's single top-level null expectation is the same for all sources, which means the
"Null met / Null not met" verdict per row is always the same comparison. Per-source falsification
blocks force a source-specific null condition: "if this source did not support the hypothesis, it
would show [X specific to this source]." This produces richer C-12 falsification content (each source
has its own disconfirmation threshold rather than a shared one) and naturally surfaces C-07 counter-
patterns because the falsification block precedes the pattern analysis. Tests whether per-source
falsification blocks produce more specific and honest disconfirmation reasoning than a single shared
null expectation.

```
You are running /prove-analysis. Work through each accessible data source using the per-source
template below. Each source has a FALSIFICATION BLOCK: before stating the pattern, you must
state what this specific source would show if the hypothesis were false, then report what you
actually observed.

---

## HYPOTHESIS

[State the hypothesis before examining any source. One sentence.]
Hypothesis: [FILL IN -- use exact wording from the feature or topic context]

---

## SOURCE ANALYSIS

[Repeat this entire block once per accessible data source. Replace [SOURCE NAME] in the header
with the exact source identifier. Add blocks for all accessible sources before writing SYNTHESIS.
Minimum two sources required.]

---

### SOURCE: [SOURCE NAME]

**Source identifier** (C-01): [Specific named artifact -- file name, table name, schema, scenario
  set, telemetry log, test suite, or system. Not "the data." Not "existing telemetry." If you
  cannot name it, you do not have access to it -- do not use this source.]

**Falsification block** (C-12):
  Null condition for this source: [If the hypothesis were false, what would THIS specific source
    show? One sentence tailored to this source -- not a generic null expectation. "If [hypothesis]
    does not hold, [source name] would show [specific observable evidence of falsification]."]
  Observed: [What this source actually shows. State it directly before any interpretation.]
  Null verdict: [Choose one: "Null met (disconfirming)" / "Null not met (consistent with
    hypothesis)" / "Ambiguous (compatible with both -- explain in Hypothesis bearing below)"]

**Pattern** (C-02): [What pattern was found in this source. If none: "No pattern detected." Do
  not hedge. Do not interpret yet -- state the finding.]

**Hypothesis bearing** (C-03): [How this pattern bears on the hypothesis stated above. One to two
  sentences. Explicit link required -- start with "This bears on the hypothesis because..." or
  equivalent. For "Null met" sources: explain what the disconfirmation means for the hypothesis.]

**Relationship type** (C-04): [Label the relationship. Pick one:]
  "Correlation only" -- [state why causation cannot be inferred from this source]
  "Association (directional, not causal)" -- [state the directional claim and its basis]
  "Causal (basis: [justification])" -- [state the logical or evidential basis. Be specific.]

**Mechanism** (C-09): [State one mechanism sentence:]
  "A plausible cause is [X] because [basis]." OR
  "This could be explained by [X], but causation cannot be confirmed from this source because [Y]." OR
  "No causal mechanism is apparent because [reason]."

**Strength** (C-05): [Tier: weak / moderate / strong + at least one of: number, rate, N of M
  cases, effect size, p-value, or logical argument for the tier. Not "significant" without backing.]

**Counter-evidence**: [Data within this source that weakens or contradicts the pattern. If none:
  "No counter-evidence in this source -- [reason why absence is plausible or a genuine gap]."]

[Repeat from "### SOURCE: [SOURCE NAME]" for each accessible data source.]

---

## SYNTHESIS

Falsification tally: "[N] of [M] sources met the null expectation (disconfirming); [K] sources
  produced patterns inconsistent with the null (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive -- two to three sentences drawing on
  patterns and null verdicts across all sources. Reference the tally.]
Causation verdict: [Yes / No / Partial -- cite the specific source(s) and relationship type
  labels from the blocks above. State the basis in one sentence.]
Scope (C-10): [Conditions under which these patterns hold and where they may not generalize.
  At least one explicit boundary condition: population, time window, platform, configuration,
  or version constraint.]

---

## QUANTIFIED CLAIMS [Required]

[At least one numeric claim drawn from the source blocks above. Do not use vague qualifiers alone.]

- [Quantified claim: "N of M sources met the null expectation", "X% of...",
  "N cases out of M...", etc.]
[Add additional quantified claims as warranted.]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_analyzed, null_met_count, null_not_met_count,
causal_claim, overall_direction.
```

---

## V-04: Mechanism-Front-Loaded Analysis

**Axis:** Role sequence -- inverts the standard analysis order; the causal mechanism for the
hypothesis is proposed before any source is examined; per-source analysis then evaluates each
source against the predicted mechanism; the causation verdict flows from mechanism confirmation
rather than from post-hoc labeling of already-stated patterns
**Hypothesis:** In standard analysis (V-01 through V-03), the model finds a pattern, connects it to
the hypothesis, then labels the relationship type, then states a mechanism if prompted. This produces
the "correlation/causation label as afterthought" problem: the label is applied to a pattern that
was never framed with mechanism testing in mind. Mechanism-first inverts this: the mechanism
prediction is the organizing frame, and each source is evaluated against it. A source either
confirms the mechanism, fails to confirm it, or cannot speak to it. This naturally produces C-09
content (mechanism sentences are the analysis itself, not a post-table requirement) and produces
more principled C-04 labeling (causal claim is defensible when mechanism is confirmed, not when
the model simply decides to label something "causal"). Tests whether mechanism-first organization
produces higher-quality causal reasoning than mechanism-as-afterthought labeling.

```
You are running /prove-analysis. This analysis begins with the mechanism, not the data.
Before examining any source, state the causal mechanism that would produce the pattern predicted
by the hypothesis. Then analyze each source as a mechanism test.

---

## PHASE 1: HYPOTHESIS AND MECHANISM PREDICTION

Hypothesis: [State the hypothesis in one sentence. Use exact wording from the feature or topic context.]

Proposed mechanism: [If this hypothesis is true, what causal chain produces the predicted pattern?
  State the mechanism in one to two sentences: "Hypothesis H would be true if X causes Y via
  mechanism M, which would produce observable evidence Z in available data sources."
  If no causal mechanism is plausible, state explicitly: "This hypothesis does not imply a
  causal mechanism because [reason] -- the relationship would be correlational at best if
  supported by data."]

Mechanism observable: [Can the proposed mechanism be tested with available data? Write one of:]
  "Yes -- if the mechanism operates, [specific source or sources] would show [specific evidence]."
  "Partially -- mechanism is testable in [source(s)] but not in [source(s)] because [reason]."
  "No -- available sources are observational only; mechanism confirmation requires [missing data]."

PHASE 1 GATE: Hypothesis and mechanism stated. Do not name or analyze any data source until
this gate is complete.

---

## PHASE 2: SOURCE ANALYSIS

[For each accessible data source, complete the per-source block below. Replace [SOURCE NAME]
with the exact source identifier. Minimum two sources required. The mechanism prediction from
PHASE 1 is the anchor for every "Mechanism status" field below.]

### SOURCE: [SOURCE NAME]

Source (C-01): [Specific named artifact -- file, table, schema, scenario set, log, test suite.
  Not "the data." If you cannot name it, do not include this source.]

Expected if mechanism operates: [If the mechanism from PHASE 1 is active, what would this
  specific source show? One sentence -- write this before examining the source. "If the
  mechanism operates, [source] would show [X]."]

Pattern found (C-02): [What the source actually shows. State it directly. If none:
  "No pattern detected." Do not hedge.]

Mechanism status: [Compare the pattern to the expected mechanism evidence. Write one of:]
  "Mechanism confirmed" -- [data matches the mechanism prediction above; state the match]
  "Mechanism not confirmed" -- [data does not match the prediction; state the discrepancy]
  "Mechanism silent" -- [this source cannot speak to the mechanism; state why -- wrong data
    type, wrong time window, no comparable observations, etc.]
  "No mechanism expected here" -- [this source was not expected to show mechanism evidence;
    explain why it was included and what it does show about the hypothesis]

Hypothesis bearing (C-03): [How the pattern and mechanism status together bear on the hypothesis.
  One to two sentences. Explicit link -- do not leave it implicit.]

Relationship type (C-04): [Derive from mechanism status above. Pick one:]
  "Correlation only" -- [Mechanism status was "not confirmed" or "silent"; state why
    mechanism confirmation is not available from this source]
  "Association (directional, not causal)" -- [Directionality is established but mechanism is
    not; state what directional evidence exists]
  "Causal (basis: [mechanism])" -- [Mechanism status was "confirmed"; state the confirmation
    basis from the mechanism status field above]

Strength (C-05): [Tier: weak / moderate / strong + at least one number, rate, N of M cases,
  effect size, or logical argument for the tier. Not "significant" without backing.]

Counter-evidence: [Data in this source that weakens or contradicts the pattern or mechanism
  confirmation. Or: "None -- [reason]."]

[Repeat this block for each accessible data source.]

---

## PHASE 3: MECHANISM VERDICT

[Review all Mechanism status fields from PHASE 2. Render a verdict on the mechanism.]

Mechanism confirmed in: [List sources where Mechanism status was "confirmed"]
Mechanism not confirmed in: [List sources where Mechanism status was "not confirmed"]
Mechanism silent in: [List sources that could not speak to the mechanism]

Mechanism verdict: [Write one:]
  "Mechanism established" -- [N of M sources confirmed; explain why this count is sufficient]
  "Mechanism plausible but unconfirmed" -- [evidence is consistent but not conclusive; state
    what additional source or data would confirm it]
  "Mechanism ruled out" -- [N of M sources showed contradictory evidence; state what this means
    for the hypothesis -- does the hypothesis fail, or only the proposed mechanism?]
  "Mechanism untestable with available data" -- [explain what data type would be needed; state
    whether the hypothesis can still be supported on correlational grounds]

Causal claim: [Given the mechanism verdict, what is the relationship type across all sources?]
  "Causal" -- [mechanism established in PHASE 3; state the supporting sources]
  "Correlation only" -- [mechanism unconfirmed or untestable; state the basis]
  "Association (directional, not causal)" -- [directionality established, mechanism not]
  "Mixed" -- [some sources causal, some correlational; detail which and why]

---

## SYNTHESIS

Overall direction: [Support / Contradict / Inconclusive -- draw on patterns and mechanism verdict.
  Two to three sentences referencing PHASE 2 source results and PHASE 3 verdict.]
Causation summary: [Yes / No / Partial -- cite the PHASE 3 mechanism verdict explicitly.]
Disconfirming data: [How many sources produced patterns inconsistent with the hypothesis or
  failed to confirm the mechanism? Name them and state the implication.]
Scope (C-10): [Where do these patterns hold and where may the mechanism not operate?
  Population, time window, platform, configuration, or version constraints.]

---

## QUANTIFIED CLAIMS [Required]

[At least one numeric claim. Not "significant" or "notable" without backing.]

- [N of M sources produced patterns consistent with the proposed mechanism]
- [Additional quantified claims: rates, counts, percentages, effect sizes as warranted]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, mechanism_verdict, sources_count,
mechanism_confirmed_count, mechanism_silent_count, causal_claim, overall_direction.
```

---

## V-05: Full Aspirational Stack

**Axes:** Multiple combined -- V-05's 6-column null table (C-11, C-12) + vocabulary contract from
V-02 (C-13) + required MECHANISM section from V-01 (C-09) + explicit scope block (C-10); targets
all five aspirational criteria as pre-printed structural requirements; 115/115 candidate
**Hypothesis:** Each aspirational criterion can be targeted individually (V-01 through V-04). The
question is whether stacking all five structural guarantees into a single template produces a
template that is still runnable without overwhelming the model with competing pre-print obligations.
V-05 tests the upper bound: if all five aspirational criteria are structurally enforced, what is
the actual score, and what overhead cost does the structural density impose? The design prediction
is that the criteria reinforce rather than compete -- null framing (C-12) elicits mechanism
reasoning (C-09) which demands vocabulary precision (C-13) which is enforced by the table structure
(C-11) which scopes its own validity (C-10). Tests whether aspirational criteria are synergistic
when combined or whether they impose additive template overhead that causes output compression.

```
You are running /prove-analysis. Read all sections before filling in any.
This template structurally enforces all analytical obligations. A VOCABULARY CONTRACT applies
throughout. Complete sections in order.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms -- any of these standing alone as the relationship
characterization is a vocabulary error:
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

## HYPOTHESIS AND FALSIFICATION SETUP

Hypothesis: [State the hypothesis in one sentence. All patterns in the analysis table bear on
  this claim. Use exact wording from the feature or topic context.]

Null expectation: [What would the data look like if this hypothesis were false? One sentence.
  This is the comparison baseline for every "Null expectation met?" cell below. Fill this in
  before writing any table row. Do not omit.]

Proposed mechanism: [What causal mechanism would produce the pattern if the hypothesis is true?
  One to two sentences. If no causal mechanism is plausible: "No causal mechanism is implied --
  the relationship would be correlational if supported because [reason]."]

---

## ANALYSIS TABLE

[All columns are required. Fill every cell for every row. Column instructions below.]

| Source | Pattern found | Null expectation met? | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|----------------------|-------------------|-------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Explicit link to hypothesis -- for Null met rows explain disconfirmation] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [weak/moderate/strong + number, rate, count, or logical argument] |
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Explicit link to hypothesis -- for Null met rows explain disconfirmation] | [Correlation only: ... / Association: ... / Causal (basis: ...)] | [weak/moderate/strong + number, rate, count, or logical argument] |
[Add one row per distinct accessible data source. Minimum two rows required.]

Column instructions:
- **Source** (C-01): Specific named artifact. Not "the data." If you cannot name it, do not add a row.
- **Pattern found** (C-02): What you found. "No pattern detected" if none. No hedging.
- **Null expectation met?** (C-12): Compare to null stated above. Write:
  "Null met" / "Null not met" / "Ambiguous" -- ambiguous requires explanation in Hypothesis bearing.
- **Hypothesis bearing** (C-03): Explicit link. One to two sentences. Do not leave implicit.
- **Relationship type** (C-04 + C-13): Use ONLY vocabulary contract terms above. No forbidden terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or logical argument.

---

## MECHANISM ANALYSIS [Required]

[For each source with a pattern in the table above, write one mechanism sentence and assess its
relationship to the proposed mechanism from HYPOTHESIS AND FALSIFICATION SETUP. Do not omit.
Vocabulary contract applies -- no forbidden terms.]

For each source with a pattern:
- [Source name]: [Mechanism sentence -- choose one form:]
  "A plausible cause is [X] because [basis from the proposed mechanism or evidence in this source]."
  "This could be explained by [X], but causation cannot be confirmed because [reason -- observational
    data, shared confound, reverse causation, or missing temporal evidence]."
  "No causal mechanism is apparent because [reason]; the [correlation/association] may reflect
    [confound or shared cause] rather than a direct causal pathway."

Mechanism verdict: [Overall: "Mechanism established (N of M sources confirmed)" /
  "Mechanism plausible but unconfirmed (consistent but no source confirms directly)" /
  "Mechanism ruled out (N of M sources show contradictory evidence)" /
  "Mechanism untestable (sources are observational only; [data type] would be needed)"]

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all rows where "Null expectation met?" is "Null met" and all sources with no pattern.
These are the disconfirming data. Do not omit this section. Vocabulary contract applies.]

- [Source (Null met or no pattern)]: [What this disconfirmation implies -- genuine limit, scope
  condition, measurement artifact, or evidence against the hypothesis?]
[If no sources met the null: "All analyzed sources produced patterns inconsistent with the null
expectation. Disconfirming data was not found in the available sources -- this is a genuine gap.
Identify at least one source expected to show the null pattern if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

[At least one numeric claim. Vague qualifiers alone ("most", "often") do not satisfy this section.]

- "N of M analyzed sources met the null expectation."
- [Additional quantified claims: rates, counts, percentages, effect sizes, N of M patterns, etc.]

---

## VOCABULARY COMPLIANCE REVIEW [Required -- complete before VERDICT]

[Scan all Relationship type cells in the table, all mechanism entries, and all counter-pattern
sentences. Report any forbidden term found. Correct violations before writing VERDICT.]

Compliance: [Write one of:]
  "All Relationship type cells, mechanism entries, and counter-pattern sentences use vocabulary
   contract terms. No violations found. Proceeding to VERDICT."
OR
  "[Location]: found '[forbidden term]' -- corrected to '[contract term]'. [Repeat per violation.]
   All violations corrected. Proceeding to VERDICT."

---

## VERDICT

Null summary: "[N] of [M] sources met the null expectation (hypothesis unsupported in those
  sources); [K] did not (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. Vocabulary contract
  applies. No forbidden terms.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and table relationship type labels]
Scope (C-10): [Conditions under which these patterns hold and where they may not generalize.
  State at least one explicit boundary condition: population, time window, platform, version,
  or configuration constraint. Do not omit.]
Vocabulary: "All relationship claims in this output use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
mechanism_verdict, causal_claim, overall_direction, vocabulary_compliant: true.
```

---

## Round 2 Design Notes

### Design basis

R1 produced two co-leaders (V-02, V-05 at 97/100) with one shared gap (C-09: mechanism sentences
never required) and one trailing variant (V-04 at 95/100) that closed C-09 but cost C-08. The R1
scorecard prescribed a specific hybrid: V-05 null-table base + dedicated MECHANISM section +
QUANTIFIED CLAIMS section. V-01 (R2) executes that prescription exactly.

The rubric v2 expansion adds three new aspirational criteria that translate directly into structural
designs: C-11 (structured format) validates the table approach from R1; C-12 (null framing) validates
V-05; C-13 (vocabulary precision) is new and untested -- V-02 (R2) is its structural test.

### C-09 targeting across variations

| V | C-09 mechanism | How it fires |
|---|---------------|--------------|
| V-01 | MECHANISM [Required] section post-table | Fires after table; three sentence templates force choice |
| V-02 | Not primary target; table structure compatible | Vocabulary contract may incidentally improve mechanism language precision |
| V-03 | Per-source Mechanism field | Part of per-source block; fires inside falsification context |
| V-04 | Mechanism-first (organizing frame) | Mechanism is predicted before data; each source tests mechanism; C-09 is the analysis itself |
| V-05 | MECHANISM ANALYSIS [Required] + mechanism verdict | Fires post-table with verdict integration |

### C-12 depth comparison: single null vs per-source falsification

| Approach | Mechanism | Depth |
|----------|-----------|-------|
| V-01, V-05: single top-level null | One null expectation applies to all sources | Shared comparison baseline; simpler to state, may be generic |
| V-03: per-source falsification blocks | Each source gets its own null condition | Source-specific threshold; may produce richer disconfirmation reasoning at cost of template length |

Key question for R2 scoring: Does per-source falsification (V-03) produce more specific C-12
content than single null (V-01, V-05), or does the per-source overhead produce formulaic
repetition ("if [source] showed null, I'd expect X" stated identically for every source)?

### C-13 structural test

V-02's vocabulary contract + compliance check is the only variation that creates a self-auditing
mechanism: the model must explicitly review its own output against a forbidden-terms list before
writing the verdict. This is a structural guarantee that no other variation provides. The question
is whether the audit step (a) actually catches violations that the vocabulary-aware column header
did not prevent, or (b) produces pro-forma "No violations found" without genuine review.

If V-02's table-column header alone ("Relationship type [ONLY vocabulary contract terms]") is
sufficient to prevent forbidden-term violations, the compliance check step adds no value. If
violations slip through the table but are caught by the compliance step, the step is load-bearing.
This is the structural test V-02 runs.

### V-04 inversion risk

Mechanism-first analysis (V-04) has a structural risk not present in other variations: the model
may bias toward "Mechanism confirmed" because it stated the mechanism and now faces evidence it
described before examining. The "Expected if mechanism operates" field per source could lead the
model to fit observations to predictions rather than report independently. This is the mechanism-
first confirmation bias question -- the opposite of V-05's potential null-framing over-reporting
risk from R1.

Counter-design: the "Expected if mechanism operates" field is written before examining the source,
then "Pattern found" reports what was actually seen without reference to the expectation. The
"Mechanism status" field then explicitly adjudicates the match. This separation should reduce
confirmation bias while maintaining mechanism-first framing.

### Predicted R2 differentiation under v2 rubric (115 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-05 (essential) | 60 | 60 | 60 | 60 | 60 |
| C-06 (multiple sources) | 10 | 10 | 10 | 10 | 10 |
| C-07 (counter-patterns) | 10 | 10 | 10 | 10 | 10 |
| C-08 (quantified claims) | 10 | 10 | 10 | 10 | 10 |
| C-09 (mechanism) | 5 | 0 | 5 | 5 | 5 |
| C-10 (scope) | 5 | 5 | 5 | 5 | 5 |
| C-11 (structured format) | 5 | 5 | 5 | 0 | 5 |
| C-12 (null/falsification) | 5 | 0 | 5 | 0 | 5 |
| C-13 (vocabulary precision) | 0 | 5 | 0 | 0 | 5 |
| **Predicted total** | **110** | **105** | **110** | **90** | **115** |

Notes on predictions:
- V-04 loses C-11 (per-source blocks are not a table format; pass condition requires "table with
  labeled columns or numbered block with labeled fields" -- V-04's per-source template uses labeled
  fields but they are not pre-printed as a fixed-column table) -- this depends on scoring interpretation
- V-04 loses C-12 (no null expectation stated; sources are evaluated against mechanism prediction
  rather than a falsification condition) -- mechanism status is not equivalent to null/falsification framing
- V-02 loses C-09 and C-12 (no mechanism prompt; no null framing)
- V-05 is the 115/115 structural candidate; the open question is whether stacking all five
  aspirational structures produces output complexity that causes essential or recommended failures

### Open research questions for R2

1. Does V-04's mechanism-first framing produce more principled causal labeling than V-01/V-05's
   post-pattern labeling -- or does it produce mechanism confirmation bias?
2. Does V-03's per-source falsification produce richer C-12 content than V-01/V-05's shared null --
   or does it produce formulaic per-source null repetition?
3. Does V-02's vocabulary compliance check step catch violations not prevented by the column header
   alone -- or is the audit pro-forma?
4. Does V-05's full aspirational stack produce the theoretically predicted 115/115 -- or does the
   structural density cause output compression and essential criterion failures?
5. Can V-04 claim C-11 under the "numbered block with labeled fields" interpretation of the pass
   condition, or does the absence of a fixed-column table disqualify it?

### V-golden candidate prediction

**V-05** is the structural 115/115 candidate: all five aspirational criteria are pre-printed
structural requirements. The only risk is template density causing the model to compress or skip
sections under output-length pressure.

**V-01** is the conservative ceiling candidate at 110: it adds exactly the MECHANISM section
that V-05 adds, without the vocabulary contract or compliance check overhead. If V-05's density
causes failures, V-01 is the fallback golden.

**V-03** is the strongest C-12 candidate: per-source falsification blocks are richer than a
shared null expectation, and the falsification block is structurally upstream of the pattern
analysis for each source. If C-12 partial scoring is possible (depth tiers), V-03 may outscore
V-01 on that criterion specifically.
