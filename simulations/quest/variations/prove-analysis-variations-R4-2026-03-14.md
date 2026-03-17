Written to `simulations/quest/variations/prove-analysis-variations-R4-2026-03-14.md`.

---

## Round 4 Variations Summary

| V | Axis | Target | Predicted |
|---|------|--------|-----------|
| **V-01** | Output format: numbered chain-ID reference | C-17 only | 125/140 |
| **V-02** | Lifecycle emphasis: standalone write-gate section | C-18 only | 125/140 |
| **V-03** | Output format + lifecycle: chain-ID + write-gate, no pre-registration | C-17 + C-18 | 135/140 |
| **V-04** | Role sequence + output format: pre-registration + chain-ID, embedded audit | C-14 + C-17 | 130/140 |
| **V-05** | Multiple combined: full stack with structural write-gate | All new criteria | 140/140 |

**Key structural moves:**

- **C-17 enforcement** (V-01, V-03, V-04, V-05): All use numbered FC-IDs in chain blocks and a table column instruction reading "Copy from FC-[NN]. Do not rewrite." The chain-ID reference creates a numbered pointer that makes re-derivation structurally awkward — the table cell must name a specific block.

- **C-18 enforcement** (V-02, V-03, V-05): The `## VERDICT WRITE-GATE` is a standalone section between VOCABULARY COMPLIANCE AUDIT and VERDICT, distinct from Phase B. It requires Step 1 (draft), Step 2 (audit), Step 3 (cleared draft), and a write-gate status line — the VERDICT then copies from the cleared draft.

- **Key C-18 structural test (V-04)**: Phase B embeds a "VERDICT paragraphs -- planned language (audit before writing)" list item using pre-write framing. Prediction: FAIL — the embedded item uses the right language but doesn't produce a cleared draft artifact or carry standalone gate labeling. The rubric's "between the last analysis section and the VERDICT section" test is structural, not linguistic.

- **V-05 four-layer structure**: Vocabulary contract → Pre-registration gate → FC-ID chain → Table → Mechanism verdict → Counter-pattern → Quantified claims → Phase A+B audit → VERDICT WRITE-GATE → VERDICT. The write-gate is layer four, fully independent from Phase B.
e audit naming all sections + standalone VERDICT WRITE-GATE section (discrete from Phase B). Both C-17 and C-18 structurally enforced.

---

## V-01: Numbered Chain-ID Reference (C-17 only)

**Axis:** Output format -- numbered falsification chain blocks with FC-NN IDs; table column instruction requires copy-by-chain-ID
**Hypothesis:** Numbered chain IDs create a structural traceability link that passes C-17 without write-gate machinery.

```
You are running /prove-analysis. Read ALL sections before filling in any.

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

Contract applies to: table cells, falsification chain entries, mechanism entries,
counter-pattern entries, synthesis paragraphs, verdict sentences. No exceptions.

---

## HYPOTHESIS AND FALSIFICATION SETUP

Hypothesis: [State in one sentence. Exact wording from feature or topic context.]

Null expectation: [If the hypothesis is false, sources would show: one sentence describing
  the observable disconfirming pattern across all sources in aggregate.]

Proposed mechanism: [If this hypothesis is true, a plausible causal chain is: [X causes Y
  producing Z]. If no mechanism: "No causal mechanism implied -- correlational at best
  because [reason]."]

---

## FALSIFICATION CHAIN [Required -- number each block; complete before analysis table]

[For each source you will analyze, assign it a sequential FC-ID: FC-01, FC-02, FC-03, etc.
Each null condition must be specific to that source -- not a generic expectation shared
across sources. Minimum two blocks. Do not begin ANALYSIS TABLE until all blocks are
numbered and complete.]

---

### FC-01: [SOURCE NAME -- exact artifact identifier]

Source null condition: [If the hypothesis were false, this specific source would show: [X --
  observable and specific to this artifact, not shared with other sources.]]
Observed: [What this source actually shows. State directly, before interpretation.]
Source null verdict: [Write one:]
  "Null met -- disconfirming: [how observation matches null condition]"
  "Null not met -- consistent with hypothesis: [how observation differs from null condition]"
  "Ambiguous: [explain compatibility with both]"

---

### FC-02: [SOURCE NAME -- exact artifact identifier]

Source null condition: [Source-specific null condition, independent of FC-01.]
Observed: [Direct observation before interpretation.]
Source null verdict: [Null met / Null not met / Ambiguous + explanation]

---

[Add FC-03, FC-04, etc. for each additional source. Then proceed to ANALYSIS TABLE.]

---

## ANALYSIS TABLE

[All columns required. One row per numbered chain block. Do not add rows for unlisted sources.]

| Source | Pattern found | Source null verdict (FC-NN) | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|----------------------------|--------------------|-------------------|----------|
| [FC-01 name] | [Pattern or "No pattern detected"] | Copy from FC-01. Do not rewrite. | [Explicit link. One to two sentences.] | [Contract terms only] | [Tier + number/rate/count/argument] |
| [FC-02 name] | [Pattern or "No pattern detected"] | Copy from FC-02. Do not rewrite. | [Explicit link] | [Contract terms only] | [Tier + justification] |

Column instructions:
- **Source** (C-01): Exact artifact name from FALSIFICATION CHAIN. Not "the data."
- **Pattern found** (C-02): What you found. "No pattern detected" if none. No hedging.
- **Source null verdict (FC-NN)** (C-16, C-17): The chain committed the verdict before the
  table. Write: "Copy from FC-[NN]:" then paste the exact verdict text from that block.
  Do not rewrite, rephrase, or re-derive. The table references the chain by number.
- **Hypothesis bearing** (C-03): Explicit link. For "Null met" rows: explain disconfirmation.
- **Relationship type** (C-04, C-13): ONLY vocabulary contract terms. No forbidden terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or logical argument.

---

## MECHANISM ANALYSIS [Required]

[For each source with a pattern, write one mechanism sentence:]
[FC-01 source name]: ["A plausible cause is..." / "This could be explained by..." /
  "No causal mechanism apparent because..."]
[FC-02 source name]: [mechanism sentence]

Mechanism verdict: [Mechanism established / Mechanism plausible but unconfirmed /
  Mechanism disconfirmed / Mechanism untestable with available data] -- [basis]

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all "Null met" rows from the table and sources with no pattern.]
- [FC-NN source name]: [implication -- limit, scope condition, measurement artifact, or
  evidence against hypothesis?]
[If no disconfirming rows: "All sources inconsistent with their null conditions. No
disconfirming data found. Name at least one source expected to show its null condition
if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition (disconfirming)."
- [Additional quantified claims: rates, counts, percentages as warranted]

---

## VOCABULARY COMPLIANCE REVIEW [Required]

Table: Relationship type column -- all cells:
  [Clear.] OR [Row FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

Mechanism sentences -- all entries:
  [Clear.] OR [Sentence: found '[forbidden term]' -- corrected to '[contract term]'.]

Counter-pattern entries and synthesis narrative:
  [Clear.] OR [Entry: found '[forbidden term]' -- corrected to '[contract term]'.]

Compliance status: [All clear.] OR [Violations corrected -- proceeding to VERDICT.]

---

## VERDICT

Falsification summary: "[N] of [M] sources met their source-specific null condition
  (disconfirming); [K] did not (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. No forbidden terms.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and Relationship type column]
Scope (C-10): [Boundary conditions under which pattern holds and where it may not generalize.
  Population, time window, platform, configuration. Do not omit.]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count,
null_not_met_count, mechanism_verdict, causal_claim, overall_direction,
vocabulary_compliant: true.
```

---

## V-02: Standalone Write-Gate Section (C-18 only)

**Axis:** Lifecycle emphasis -- a discrete `## VERDICT WRITE-GATE` section positioned structurally between the last analysis section and `## VERDICT`; requires a drafted-and-audited verdict before the verdict section opens
**Hypothesis:** Promoting the pre-audit out of Phase B into a structurally independent gate section passes C-18 unambiguously. Tests whether C-18 depends on standalone structural positioning vs. embedded Phase B framing.

```
You are running /prove-analysis. Read ALL sections before filling in any.
Complete sections in the order written. Do not skip forward.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED replacement vocabulary:
  "Correlation only: [basis]"
  "Association (directional, not causal): [claim and basis]"
  "Causal (basis: [justification])"
  "No relationship detected"

Contract applies everywhere. Compliance audited in two phases before VERDICT WRITE-GATE.

---

## HYPOTHESIS AND FALSIFICATION SETUP

Hypothesis: [One sentence. Exact wording from feature or topic context.]

Null expectation: [If the hypothesis is false, sources would show: [observable pattern.
  One sentence, shared across all sources.]]

Proposed mechanism: [Plausible causal chain if hypothesis is true: [X causes Y producing Z].
  If none: "No causal mechanism implied because [reason]."]

---

## ANALYSIS TABLE

[Minimum two rows. All columns required. Fill every cell.]

| Source | Pattern found | Null expectation met? | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|----------------------|--------------------|-------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [Met: [how] / Not met: [how] / Ambiguous: [why]] | [Explicit link. One to two sentences.] | [Contract terms only] | [Tier + number/rate/count/argument] |
| [Name] | [Pattern or "No pattern detected"] | [Met / Not met / Ambiguous] | [Explicit link] | [Contract terms only] | [Tier + justification] |

Column instructions:
- **Source** (C-01): Specific named artifact. Not "the data." If you cannot name it, no row.
- **Pattern found** (C-02): What you found. No hedging.
- **Null expectation met?** (C-12): Whether observation matches the shared null expectation.
- **Hypothesis bearing** (C-03): Explicit link. "This bears on the hypothesis because..."
- **Relationship type** (C-04, C-13): ONLY vocabulary contract terms. Forbidden terms = error.
- **Strength** (C-05): Tier + at least one number, rate, count, or argument.

---

## MECHANISM ANALYSIS [Required]

[Per-source mechanism sentences.]
[Source name]: [A plausible cause is... / This could be explained by... /
  No causal mechanism apparent because...]

Mechanism verdict: [Mechanism established / Mechanism plausible but unconfirmed /
  Mechanism disconfirmed / Mechanism untestable with available data] -- [basis]

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all "Null met" rows and no-pattern sources.]
- [Source]: [implication]
[If none: state absence and name one source expected to show null condition if hypothesis fails.]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] analyzed sources met the shared null expectation (disconfirming)."
- [Additional quantified claims as warranted]

---

## VOCABULARY COMPLIANCE AUDIT [Required -- both phases before VERDICT WRITE-GATE]

### Phase A: Table Column Audit

Relationship type column -- all cells:
  [Clear.] OR [Row [source]: found '[forbidden term]' -- corrected to '[contract term]'.]

### Phase B: Prose Section Audit

[Audit each section below by name. Scan every sentence for relationship claims.]

PROPOSED MECHANISM (HYPOTHESIS AND FALSIFICATION SETUP):
  [Clear.] OR [Violation: '[forbidden term]' -- corrected to '[contract term]'.]

MECHANISM ANALYSIS -- each mechanism sentence and verdict:
  [Clear.] OR [Sentence: '[forbidden term]' -- corrected to '[contract term]'.]

COUNTER-PATTERN SUMMARY -- each entry:
  [Clear.] OR [Entry [source]: '[forbidden term]' -- corrected to '[contract term]'.]

Phase B status: [Phase B complete. All prose sections clear.] OR
  [Phase B complete. [N] violations corrected. All sections now clear.]

---

## VERDICT WRITE-GATE [Required -- complete before writing VERDICT]

[This section is a gate. VERDICT may not be written until this gate produces a cleared draft.]

**Step 1 -- Draft planned verdict language:**
  Overall direction (planned): "[Support / Contradict / Inconclusive] -- [one sentence
    summarizing direction, using vocabulary contract terms]"
  Causal claim (planned): "[Yes / No / Partial] -- [one sentence citing mechanism verdict
    and Relationship type column findings]"
  Scope (planned): "[Boundary conditions and validity limits. At least one explicit limit.]"
  Falsification summary (planned): "[N] of [M] sources met the null expectation..."

**Step 2 -- Audit planned language against vocabulary contract:**
  Overall direction: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Causal claim: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Scope: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Falsification summary: [Clear.]

**Step 3 -- Cleared draft:**
  [Restate corrected verdict language. VERDICT will copy from here.]
  Overall direction (cleared): [corrected text]
  Causal claim (cleared): [corrected text]
  Scope (cleared): [corrected text]
  Falsification summary (cleared): [corrected text]

Write-gate status: [Draft audited and cleared. Proceeding to VERDICT.]

---

## VERDICT

[Copy from VERDICT WRITE-GATE Step 3 cleared draft. Do not rewrite.]

Falsification summary: [Copy cleared text]
Overall direction: [Copy cleared text]
Causal claim: [Copy cleared text]
Scope (C-10): [Copy cleared text]
Vocabulary (C-15): "Phase A table column audit and Phase B prose section audit complete.
  Verdict copied from VERDICT WRITE-GATE cleared draft."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count,
null_not_met_count, mechanism_verdict, causal_claim, overall_direction,
vocabulary_compliant: true, prose_audit_complete: true, write_gate_complete: true.
```

---

## V-03: Chain-ID + Write-Gate Without Pre-Registration (C-17 + C-18, no C-14)

**Axis:** Output format + lifecycle emphasis -- numbered FC-ID chain with copy instruction and standalone write-gate, no mechanism pre-registration
**Hypothesis:** C-17 and C-18 are achievable without pre-registration overhead. Simpler structure; C-14 sacrificed to isolate the two new criteria together.

```
You are running /prove-analysis. Read ALL sections before filling in any.
Complete sections in the order written. Do not skip forward.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED replacement vocabulary:
  "Correlation only: [basis]"
  "Association (directional, not causal): [claim and basis]"
  "Causal (basis: [justification])"
  "No relationship detected"

Contract applies to: table cells, chain entries, mechanism entries, counter-pattern entries,
synthesis paragraphs, verdict sentences. Compliance audited in two phases before VERDICT WRITE-GATE.

---

## HYPOTHESIS AND MECHANISM SETUP

Hypothesis: [One sentence. Exact wording from feature or topic context.]

Proposed mechanism: [If the hypothesis is true, a plausible causal chain is: [X causes Y
  producing Z]. If no mechanism: "No causal mechanism implied because [reason]."]

---

## FALSIFICATION CHAIN [Required -- number each block; complete before analysis table]

[Assign each source a sequential FC-ID: FC-01, FC-02, etc. Each null condition must be
specific to that source. Minimum two blocks. Proceed to ANALYSIS TABLE only after all
blocks are numbered and complete.]

---

### FC-01: [SOURCE NAME -- exact artifact identifier]

Source null condition: [If the hypothesis were false, this specific source would show: [X --
  specific to this artifact's observable characteristics.]]
Observed: [What this source actually shows. Direct statement before interpretation.]
Source null verdict: [Write one:]
  "Null met -- disconfirming: [how observation matches null condition]"
  "Null not met -- consistent with hypothesis: [how observation differs from null condition]"
  "Ambiguous: [explain compatibility with both]"

---

### FC-02: [SOURCE NAME -- exact artifact identifier]

Source null condition: [Source-specific null condition, independent of FC-01.]
Observed: [Direct observation.]
Source null verdict: [Null met / Null not met / Ambiguous + explanation]

---

[Add FC-03, FC-04, etc. as needed. Then proceed to ANALYSIS TABLE.]

---

## ANALYSIS TABLE

[One row per numbered chain block. All columns required.]

| Source | Pattern found | Source null verdict (chain ref) | Hypothesis bearing | Relationship type | Strength |
|--------|--------------|--------------------------------|--------------------|-------------------|----------|
| [FC-01 name] | [Pattern or "No pattern detected"] | Copy from FC-01. Do not rewrite. | [Explicit link. One to two sentences.] | [Contract terms only] | [Tier + number/rate/count/argument] |
| [FC-02 name] | [Pattern or "No pattern detected"] | Copy from FC-02. Do not rewrite. | [Explicit link] | [Contract terms only] | [Tier + justification] |

Column instructions:
- **Source** (C-01): Exact artifact name from FALSIFICATION CHAIN. Not "the data."
- **Pattern found** (C-02): No hedging. "No pattern detected" if none.
- **Source null verdict (chain ref)** (C-16, C-17): Write "Copy from FC-[NN]:" followed by
  the exact verdict text from that chain block. Do not rewrite or rephrase. The chain
  committed the verdict before this table was written; the table references, not re-derives.
- **Hypothesis bearing** (C-03): Explicit link. For "Null met" rows: explain disconfirmation.
- **Relationship type** (C-04, C-13): ONLY vocabulary contract terms. No forbidden terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or logical argument.

---

## MECHANISM ANALYSIS [Required]

[For each source with a pattern, write one mechanism sentence.]
[FC-01 source name]: [A plausible cause is... / This could be explained by... /
  No causal mechanism apparent because...]
[FC-02 source name]: [mechanism sentence]

Mechanism verdict: [Mechanism established / Mechanism plausible but unconfirmed /
  Mechanism disconfirmed / Mechanism untestable with available data] -- [basis]

---

## COUNTER-PATTERN SUMMARY [Required]

[All "Null met" rows and no-pattern sources.]
- [FC-NN source name]: [implication]
[If none: "All sources inconsistent with null conditions. No disconfirming data found.
Name at least one source expected to show its null condition if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition (disconfirming)."
- [Additional quantified claims: rates, counts, percentages as warranted]

---

## VOCABULARY COMPLIANCE AUDIT [Required -- both phases before VERDICT WRITE-GATE]

### Phase A: Table Column Audit

Relationship type column -- all cells:
  [Clear.] OR [Row FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

### Phase B: Prose Section Audit

[Name each section explicitly. Scan every sentence for relationship claims.]

PROPOSED MECHANISM (HYPOTHESIS AND MECHANISM SETUP):
  [Clear.] OR [Violation: '[forbidden term]' -- corrected to '[contract term]'.]

FALSIFICATION CHAIN -- null condition sentences (blocks FC-01 through FC-[last]):
  [Clear.] OR [Block FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

MECHANISM ANALYSIS -- each mechanism sentence and verdict:
  [Clear.] OR [Sentence FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

COUNTER-PATTERN SUMMARY -- all entries:
  [Clear.] OR [Entry FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

Phase B status: [Phase B complete. All prose sections clear.] OR
  [Phase B complete. [N] violations corrected. All sections now clear.]

---

## VERDICT WRITE-GATE [Required -- structural gate; complete before writing VERDICT]

[VERDICT may not be written until this gate produces a cleared draft.]

**Step 1 -- Draft planned verdict language:**
  Falsification summary (planned): "[N] of [M] sources met their source-specific null
    condition (disconfirming); [K] did not (consistent with hypothesis)."
  Overall direction (planned): "[Support / Contradict / Inconclusive] -- [one sentence]"
  Causal claim (planned): "[Yes / No / Partial] -- [cite mechanism verdict]"
  Scope (planned): "[Boundary conditions under which pattern holds and where it may not
    generalize. At least one explicit limit.]"

**Step 2 -- Audit planned language against vocabulary contract:**
  Falsification summary: [Clear.] OR [Violation: corrected to '[contract term]'.]
  Overall direction: [Clear.] OR [Violation: corrected to '[contract term]'.]
  Causal claim: [Clear.] OR [Violation: corrected to '[contract term]'.]
  Scope: [Clear.] OR [Violation: corrected to '[contract term]'.]

**Step 3 -- Cleared draft (VERDICT copies from here):**
  Falsification summary (cleared): [text]
  Overall direction (cleared): [text]
  Causal claim (cleared): [text]
  Scope (cleared): [text]

Write-gate status: [Audit complete. Cleared draft produced. Proceeding to VERDICT.]

---

## VERDICT

[Copy from VERDICT WRITE-GATE Step 3 cleared draft. Do not rewrite.]

Falsification summary: [Copy cleared text]
Overall direction: [Copy cleared text]
Causal claim: [Copy cleared text]
Scope (C-10): [Copy cleared text]
Vocabulary (C-15): "Phase A table column audit and Phase B prose section audit complete.
  VERDICT WRITE-GATE cleared. All relationship claims use vocabulary contract terms."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count,
null_not_met_count, mechanism_verdict, causal_claim, overall_direction,
vocabulary_compliant: true, prose_audit_complete: true, write_gate_complete: true.
```

---

## V-04: Pre-Registration + Chain-ID, Embedded VERDICT Pre-Audit (C-14 + C-17, not C-18)

**Axis:** Role sequence + output format -- pre-registration gate + numbered FC-ID chain with copy instruction; VERDICT pre-audit embedded as Phase B list item, not a standalone gate section
**Hypothesis:** The embedded Phase B VERDICT annotation does not satisfy C-18. Structural positioning inside a list item within Phase B differs from a labeled gate section appearing between analysis and VERDICT. Tests the C-18 boundary: embedded annotation vs. standalone section.

```
You are running /prove-analysis. Read ALL sections before filling in any.
Complete sections in the order written. Do not skip forward.

---

## VOCABULARY CONTRACT [applies everywhere in this output]

FORBIDDEN standalone relationship terms:
  "appears related"   |   "suggests a link"       |   "may indicate"
  "seems to affect"   |   "could suggest"          |   "implies a connection"
  "points toward"     |   "is associated with"     [without a type label immediately following]

REQUIRED replacement vocabulary:
  "Correlation only: [basis]"
  "Association (directional, not causal): [claim and basis]"
  "Causal (basis: [justification])"
  "No relationship detected"

Contract applies everywhere. Compliance audited in two phases after analysis, before VERDICT.

---

## HYPOTHESIS AND PRE-REGISTRATION SETUP

Hypothesis: [One sentence. Exact wording from feature or topic context.]

Mechanism prediction [Required -- commit before naming any source]:
  [If this hypothesis is true, what causal chain produces the predicted pattern?
  Format: "If [hypothesis] is true, [mechanism M] operates: [X causes Y], producing
  observable evidence [Z] in available sources."
  If no mechanism: "No causal mechanism implied -- correlational at best because [reason]."
  Do not name any data source in this section.]

Mechanism observable: [Write one:]
  "Yes -- mechanism produces [observable evidence type] in available sources."
  "Partially -- testable in [source types] but not [others] because [reason]."
  "No -- observational sources only; [data type] needed."

PRE-REGISTRATION GATE: Mechanism prediction locked. Do not name any source before this gate.
Proceed to FALSIFICATION CHAIN.

---

## FALSIFICATION CHAIN [Required -- number each block; complete before analysis table]

[Assign each source a sequential FC-ID: FC-01, FC-02, etc. Each null condition must be
specific to that source. Minimum two blocks. Do not begin ANALYSIS TABLE until complete.]

---

### FC-01: [SOURCE NAME]

Source null condition: [What this specific source would show if the hypothesis is false.
  Specific to this artifact, not generic.]
Observed: [Direct observation, before interpretation.]
Source null verdict: [Null met -- disconfirming: [how] /
  Null not met -- consistent with hypothesis: [how] /
  Ambiguous: [why]]

---

### FC-02: [SOURCE NAME]

Source null condition: [Source-specific, independent of FC-01.]
Observed: [Direct observation.]
Source null verdict: [Null met / Null not met / Ambiguous + explanation]

---

[Add FC-03, FC-04, etc. as needed. Then proceed to ANALYSIS TABLE.]

---

## ANALYSIS TABLE

[Seven columns required. One row per numbered chain block.]

| Source | Pattern found | Source null verdict (FC-NN) | Hypothesis bearing | Relationship type | Strength | Mechanism adjudication |
|--------|--------------|----------------------------|--------------------|-------------------|----------|------------------------|
| [FC-01 name] | [Pattern or "No pattern detected"] | Copy from FC-01. Do not rewrite. | [Explicit link. One to two sentences.] | [Contract terms only] | [Tier + number/rate/count/argument] | [Confirmed: [match to prediction] / Not confirmed: [discrepancy] / Silent: [why]] |
| [FC-02 name] | [Pattern or "No pattern detected"] | Copy from FC-02. Do not rewrite. | [Explicit link] | [Contract terms only] | [Tier + justification] | [Confirmed / Not confirmed / Silent] |

Column instructions:
- **Source** (C-01): Exact artifact name from FALSIFICATION CHAIN. Not "the data."
- **Pattern found** (C-02): No hedging.
- **Source null verdict (FC-NN)** (C-16, C-17): Write "Copy from FC-[NN]:" then paste the
  exact verdict text. Do not rewrite or re-derive. Chain is committed; table references it.
- **Hypothesis bearing** (C-03): Explicit link. For "Null met" rows: explain disconfirmation.
- **Relationship type** (C-04, C-13): ONLY vocabulary contract terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or argument.
- **Mechanism adjudication** (C-14): Reference the pre-stated prediction in HYPOTHESIS AND
  PRE-REGISTRATION SETUP explicitly. Write one of:
  "Confirmed: [how observed pattern matches the pre-registered prediction]"
  "Not confirmed: [how observed pattern diverges from the prediction; be specific]"
  "Silent: [why this source cannot adjudicate the prediction]"
  Do not propose a new mechanism. Adjudicate the pre-registered prediction only.

---

## MECHANISM VERDICT [Required]

Mechanism confirmed in: [sources where adjudication = "Confirmed"]
Mechanism not confirmed in: [sources where adjudication = "Not confirmed"]
Mechanism silent in: [sources where adjudication = "Silent"]

Mechanism verdict (C-14): [Write one:]
  "Mechanism established -- [N] of [M] sources confirmed; [basis]"
  "Mechanism plausible but unconfirmed -- [N] consistent, no direct confirmation; [what needed]"
  "Mechanism disconfirmed -- [N] of [M] contradictory; [implication]"
  "Mechanism untestable with available data -- [data type needed]"

---

## COUNTER-PATTERN SUMMARY [Required]

- [FC-NN source]: [implication of Null met or no-pattern finding]
[If none: "No disconfirming data. Name at least one source expected to show its null
condition if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition (disconfirming)."
- "[N] of [M] sources produced Mechanism adjudication: Confirmed."

---

## VOCABULARY COMPLIANCE AUDIT [Required -- before VERDICT]

### Phase A: Table Column Audit

Relationship type column -- all cells:
  [Clear.] OR [Row FC-[NN]: '[forbidden term]' -- corrected to '[contract term]'.]

### Phase B: Prose Section Audit

[Audit each named section for relationship claims.]

HYPOTHESIS AND PRE-REGISTRATION SETUP -- mechanism prediction text:
  [Clear.] OR [Violation: '[forbidden term]' -- corrected to '[contract term]'.]

FALSIFICATION CHAIN -- null condition sentences (FC-01 through FC-[last]):
  [Clear.] OR [Block FC-[NN]: '[forbidden term]' -- corrected to '[contract term]'.]

MECHANISM VERDICT -- verdict sentence and supporting text:
  [Clear.] OR [Violation: '[forbidden term]' -- corrected to '[contract term]'.]

COUNTER-PATTERN SUMMARY -- all entries:
  [Clear.] OR [Entry FC-[NN]: '[forbidden term]' -- corrected to '[contract term]'.]

VERDICT paragraphs -- planned language (audit before writing):
  [Clear -- planned verdict language uses vocabulary contract terms.] OR
  [Planned use of '[forbidden term]' -- will use '[contract term]' instead.]

Phase B status: [Phase B complete. All prose sections clear. Proceeding to VERDICT.] OR
  [Phase B complete. [N] violations corrected. Proceeding to VERDICT.]

---

## VERDICT

Falsification summary (C-16): "[N] of [M] sources met their source-specific null condition
  (disconfirming); [K] did not."
Mechanism verdict (C-14): [Restate from MECHANISM VERDICT -- one of four permitted terms.]
Overall direction: [Support / Contradict / Inconclusive] -- [one sentence. No forbidden terms.]
Causal claim: [Yes / No / Partial] -- [cite mechanism verdict and Relationship type column]
Scope (C-10): [Explicit boundary conditions. At least one. Do not omit.]
Vocabulary: "Phase A and Phase B vocabulary audits complete."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count,
null_not_met_count, mechanism_verdict, mechanism_confirmed_count, causal_claim,
overall_direction, vocabulary_compliant: true, prose_audit_complete: true.
```

---

## V-05: Full 140/140 Stack

**Axes:** Multiple combined -- pre-registration gate (C-14) + numbered FC-ID falsification chain with copy-by-reference (C-16, C-17) + seven-column table + mechanism verdict + two-phase prose audit naming all sections including pre-registration text (C-13, C-15) + standalone VERDICT WRITE-GATE section as structural gate (C-18)
**Hypothesis:** All 18 criteria satisfied. C-17 via "Copy from FC-[NN]. Do not rewrite." instruction at the table column level. C-18 via a standalone VERDICT WRITE-GATE section -- separate from Phase B, positioned between VOCABULARY COMPLIANCE AUDIT and VERDICT, producing a cleared draft artifact.

```
You are running /prove-analysis. Read ALL sections before filling in any.
This template enforces all analytical obligations across four structural layers:
  (1) VOCABULARY CONTRACT covers all text; TWO-PHASE PROSE AUDIT before VERDICT WRITE-GATE
  (2) MECHANISM PREDICTION pre-registered before any source is named; adjudicated per source
  (3) FALSIFICATION CHAIN with numbered FC-IDs establishes per-source null conditions
      before the table; table copies by chain reference, not re-derives
  (4) VERDICT WRITE-GATE produces a cleared draft before the VERDICT section opens
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

Contract applies to: table cells, mechanism text, falsification chain entries,
counter-pattern entries, synthesis paragraphs, verdict sentences. No exceptions.

Compliance verified in two phases before VERDICT WRITE-GATE. Phase A audits the
Relationship type table column. Phase B audits each prose section by name. Both required.

---

## HYPOTHESIS AND PRE-REGISTRATION SETUP

Hypothesis: [State in one sentence. Use exact wording from the feature or topic context.
  All analysis below bears on this claim.]

Mechanism prediction [Required -- lock before naming any source]:
  [If this hypothesis is true, what causal chain produces the predicted pattern? One to two
  sentences as a prediction to be adjudicated, not a post-hoc explanation.
  Format: "If [hypothesis] is true, [mechanism M] operates: [X causes Y], producing
  observable evidence [Z] in available sources."
  If no mechanism: "No causal mechanism implied -- correlational at best because [reason]."
  Do not name any data source here.]

Mechanism observable: [Write one:]
  "Yes -- if the mechanism operates, [source types] would show [specific evidence]."
  "Partially -- testable in [source types] but not [others] because [reason]."
  "No -- sources observational; [data type] needed."

PRE-REGISTRATION GATE: Mechanism prediction locked. Do not name any data source before
this gate. Proceed to the FALSIFICATION CHAIN.

---

## FALSIFICATION CHAIN [Required -- number each block; complete before analysis table]

[Assign each source a sequential FC-ID: FC-01, FC-02, FC-03, etc. Each null condition must
be specific to that source -- not a generic expectation shared across sources. Minimum two
blocks. Do not begin ANALYSIS TABLE until all blocks are numbered and complete.]

---

### FC-01: [SOURCE NAME -- exact artifact identifier]

Source null condition: [If the hypothesis were false, this specific source would show: [X --
  observable and specific to this artifact. What would THIS source show, not any other?]]
Observed: [What this source actually shows. State directly, before interpretation.]
Source null verdict: [Write one:]
  "Null met -- disconfirming: [how observation matches null condition]"
  "Null not met -- consistent with hypothesis: [how observation differs from null condition]"
  "Ambiguous: [explain compatibility with both]"

---

### FC-02: [SOURCE NAME -- exact artifact identifier]

Source null condition: [Source-specific null condition, independent of FC-01.]
Observed: [Direct observation before interpretation.]
Source null verdict: [Null met / Null not met / Ambiguous + explanation]

---

[Add FC-03, FC-04, etc. for each additional source. Then proceed to ANALYSIS TABLE.]

---

## ANALYSIS TABLE

[All columns required. One row per numbered chain block. Do not add rows for sources
not listed in the FALSIFICATION CHAIN.]

| Source | Pattern found | Source null verdict (FC-NN) | Hypothesis bearing | Relationship type | Strength | Mechanism adjudication |
|--------|--------------|----------------------------|--------------------|-------------------|----------|------------------------|
| [FC-01 name] | [Pattern or "No pattern detected"] | Copy from FC-01. Do not rewrite. | [Explicit link. One to two sentences. For Null met: explain disconfirmation.] | [Contract terms only] | [Tier + number/rate/count/argument] | [Confirmed: [match to pre-registered prediction] / Not confirmed: [discrepancy, be specific] / Silent: [why source cannot adjudicate]] |
| [FC-02 name] | [Pattern or "No pattern detected"] | Copy from FC-02. Do not rewrite. | [Explicit link] | [Contract terms only] | [Tier + justification] | [Confirmed / Not confirmed / Silent] |

Column instructions:
- **Source** (C-01): Exact artifact name from FALSIFICATION CHAIN. Not "the data."
- **Pattern found** (C-02): What you found. "No pattern detected" if none. No hedging.
- **Source null verdict (FC-NN)** (C-16, C-17): The chain committed the verdict before this
  table. Write: "Copy from FC-[NN]:" then paste the exact verdict text from that block.
  Do not rewrite, rephrase, or re-derive. The table references the chain by number.
- **Hypothesis bearing** (C-03): Explicit link. For "Null met" rows: explain what the
  disconfirmation means for the hypothesis.
- **Relationship type** (C-04, C-13): ONLY vocabulary contract terms. No forbidden terms.
- **Strength** (C-05): Tier + at least one number, rate, count, or logical argument.
- **Mechanism adjudication** (C-14): Compare the observed pattern to the pre-registered
  prediction in HYPOTHESIS AND PRE-REGISTRATION SETUP. Reference that prediction explicitly.
  Write one of:
  "Confirmed: [how the observed pattern matches the pre-registered mechanism prediction]"
  "Not confirmed: [how the observed pattern diverges; be specific about the discrepancy]"
  "Silent: [why this source cannot speak to the mechanism]"
  Do not propose a new mechanism. Adjudicate the pre-registered prediction only.

---

## MECHANISM VERDICT [Required]

Mechanism confirmed in: [list sources where adjudication = "Confirmed"]
Mechanism not confirmed in: [list sources where adjudication = "Not confirmed"]
Mechanism silent in: [list sources where adjudication = "Silent"]

Mechanism verdict (C-14): [Write one permitted term:]
  "Mechanism established -- [N] of [M] sources confirmed; [basis for sufficiency]"
  "Mechanism plausible but unconfirmed -- consistent in [N] sources, no direct confirmation;
    [what data would establish it]"
  "Mechanism disconfirmed -- [N] of [M] sources showed contradictory patterns; [implication]"
  "Mechanism untestable with available data -- [data type] needed"

---

## COUNTER-PATTERN SUMMARY [Required]

[Collect all "Null met" rows from the table and sources with no pattern. Vocabulary contract applies.]

- [FC-NN source name]: [Implication -- genuine limit, scope condition, measurement artifact,
  or evidence against hypothesis?]
[If no "Null met" rows: "All sources inconsistent with their source-specific null conditions.
No disconfirming data found. Name at least one source expected to show its null condition
if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS [Required]

- "[N] of [M] sources met their source-specific null condition (disconfirming)."
- "[N] of [M] sources produced Mechanism adjudication: Confirmed."
- [Additional quantified claims: rates, counts, percentages, effect sizes as warranted]

---

## VOCABULARY COMPLIANCE AUDIT [Required -- both phases before VERDICT WRITE-GATE]

### Phase A: Table Column Audit

Relationship type column -- all cells:
  [Clear -- all cells use vocabulary contract terms.] OR
  [Row FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

### Phase B: Prose Section Audit

[Audit each prose section below by name. Scan every sentence for relationship claims.
Report "Clear" or the specific violation and correction for each section.]

HYPOTHESIS AND PRE-REGISTRATION SETUP -- mechanism prediction text:
  [Clear.] OR [Violation: found '[forbidden term]' -- corrected to '[contract term]'.]

FALSIFICATION CHAIN -- null condition sentences (blocks FC-01 through FC-[last]):
  [Clear -- all null condition and observed sentences use vocabulary contract terms.] OR
  [Block FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

MECHANISM VERDICT -- verdict sentence and rationale:
  [Clear.] OR [Violation: found '[forbidden term]' -- corrected to '[contract term]'.]

COUNTER-PATTERN SUMMARY -- all entries:
  [Clear.] OR [Entry FC-[NN]: found '[forbidden term]' -- corrected to '[contract term]'.]

Phase B status: [Phase B complete. All prose sections clear.] OR
  [Phase B complete. [N] violations corrected across prose sections. All sections now clear.]

---

## VERDICT WRITE-GATE [Required -- structural gate; complete before writing VERDICT]

[This section is a discrete gate between the audit and the verdict. It is not part of
Phase B. VERDICT may not be written until Step 3 below produces a cleared draft.]

**Step 1 -- Draft planned verdict language:**

  Falsification summary (planned): "[N] of [M] sources met their source-specific null
    condition (disconfirming); [K] did not (consistent with hypothesis)."
  Mechanism verdict (planned): [Restate from MECHANISM VERDICT -- one of the four permitted
    terms. Do not rephrase.]
  Overall direction (planned): "[Support / Contradict / Inconclusive] -- [one sentence
    summarizing direction. Vocabulary contract terms only.]"
  Causal claim (planned): "[Yes / No / Partial] -- [one sentence citing mechanism verdict
    and Relationship type column findings. Vocabulary contract terms only.]"
  Scope (planned): "[Conditions under which pattern holds and where it may not generalize.
    At least one explicit boundary condition: population, time window, platform, configuration.]"

**Step 2 -- Audit planned language against vocabulary contract:**

  Falsification summary: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Mechanism verdict: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Overall direction: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Causal claim: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]
  Scope: [Clear.] OR [Violation: '[term]' -- corrected to '[contract term]'.]

**Step 3 -- Cleared draft (VERDICT copies from here):**

  Falsification summary (cleared): [paste corrected text]
  Mechanism verdict (cleared): [paste corrected text]
  Overall direction (cleared): [paste corrected text]
  Causal claim (cleared): [paste corrected text]
  Scope (cleared): [paste corrected text]

Write-gate status: [Audit complete. Cleared draft produced. Proceeding to VERDICT.]

---

## VERDICT

[Copy from VERDICT WRITE-GATE Step 3 cleared draft. Do not rewrite.]

Falsification summary (C-16): [Copy cleared text]
Mechanism verdict (C-14): [Copy cleared text]
Overall direction: [Copy cleared text]
Causal claim: [Copy cleared text]
Scope (C-10): [Copy cleared text]
Vocabulary (C-15): "Phase A table column audit and Phase B prose section audit complete.
  VERDICT WRITE-GATE cleared. All relationship claims in this output use vocabulary
  contract terms. Verdict copied from cleared draft."

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count,
null_not_met_count, mechanism_verdict, mechanism_confirmed_count, causal_claim,
overall_direction, vocabulary_compliant: true, prose_audit_complete: true,
write_gate_complete: true.
```

---

## Predicted Scores Against v4 Rubric (140 pts)

| V | C-11 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | Aspirational | Total |
|---|------|------|------|------|------|------|------|-------------|-------|
| V-01 | ✓ | ✓ | — | — | ✓ | **✓** | — | 30 | **125** |
| V-02 | ✓ | ✓ | — | ✓ | — | — | **✓** | 30 | **125** |
| V-03 | ✓ | ✓ | — | ✓ | ✓ | **✓** | **✓** | 40 | **135** |
| V-04 | ✓ | ✓ | ✓ | — | ✓ | **✓** | — | 35 | **130** |
| V-05 | ✓ | ✓ | ✓ | ✓ | ✓ | **✓** | **✓** | 50 | **140** |

**Open scoring questions for R4:**

1. **V-04 C-18**: Does the Phase B embedded "VERDICT paragraphs -- planned language (audit before writing)" entry constitute a write-gate? C-18 requires the audit to appear as a structural step "between the last analysis section and the VERDICT section." Phase B is positionally between analysis and VERDICT -- but the pass condition requires "labeled or structured as occurring before the VERDICT is written," and "A compliance check appended after the completed verdict does not qualify." The embedded Phase B item uses pre-write framing ("audit before writing") but is a list item, not a standalone labeled section. Prediction: FAIL. The structural test is whether the framing produces a cleared draft artifact as a gate step, not whether it uses "before writing" language.

2. **V-01 C-15**: Compliance review covers mechanism sentences, counter-pattern entries, and synthesis narrative but does not name each prose section individually by document heading. Prediction: FAIL (consistent with R3 C-15 failure mode in V-01 and V-02).

3. **V-02 C-17**: No falsification chain exists in V-02 -- uses shared null expectation. No table cell can carry a copy-from-chain instruction because there is no chain. FAIL.

4. **V-03 C-14**: No PRE-REGISTRATION GATE. Mechanism proposed post-hoc in MECHANISM ANALYSIS. FAIL.

5. **V-05 C-15**: Phase B names four prose sections by document heading: HYPOTHESIS AND PRE-REGISTRATION SETUP (mechanism prediction), FALSIFICATION CHAIN (all FC blocks), MECHANISM VERDICT, COUNTER-PATTERN SUMMARY. VERDICT is audited in the VERDICT WRITE-GATE, not Phase B. Pass condition requires "compliance check section explicitly covers relationship claims outside the analysis table." Phase B covers four named sections; VERDICT WRITE-GATE covers verdict language. Combined coverage should satisfy C-15.
