Written to `simulations/quest/variations/prove-analysis-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- prove-analysis

**5 variations across 3 single-axis + 2 combined:**

| V | Axis | Core mechanism | C-04 guarantee |
|---|------|----------------|----------------|
| **V-01** | Role sequence: inventory-first | INVENTORY GATE separates source enumeration from analysis | Per-source `Correlation or causal:` field |
| **V-02** | Output format: 5-column table | Pre-printed columns map 1:1 to C-01 through C-05 | Fixed `Correlation or causal?` column |
| **V-03** | Phrasing register: imperative | "Say correlation or causation" as a direct command | Step 4 is a discrete imperative action |
| **V-04** | Role sequence + Lifecycle: gated phases | PHASE 5 is dedicated solely to causal labeling for all sources | Standalone gated phase fires for every source |
| **V-05** | Output format + Inertia framing: table + null column | Pre-printed "Null expectation met?" column makes disconfirmation structurally visible | Fixed column + null comparison sharpens causal vs correlational labeling |

**Key design translation:** The `prove-analysis` "inertia" analog is the **null hypothesis** -- the status-quo explanation the hypothesis must beat. V-05 forces the analyst to state what the data would look like if the hypothesis were false before any source is analyzed, then tracks "Null met / Null not met" per row. This is structurally identical to the feasibility skill's "Do-nothing cost" column: it demands comparison against the alternative, not just confirmation of the hypothesis.

**Predicted ceiling:** V-02 and V-05 (table columns cannot be skipped). V-05 is the richer candidate if the null framing improves C-07 depth. V-04 is the strongest for aspirational criteria C-09/C-10 via gated phase structure. V-03 is the minimum-structure floor test.
register alone produces the five obligations without structural scaffolding.

**Predicted ceiling:** V-02 and V-05 -- table structures physically cannot omit columns and cannot
leave a cell blank without violating the template. V-04 is the closest competitor via gated phases.
V-03 is the minimum-structure test: if imperative register produces 100/100, structural overhead is
not justified. V-01 is the mid-structure approach: inventory gate ensures C-01 completeness before
any analysis begins.

---

## V-01: Inventory-First Role Sequence

**Axis:** Role sequence -- explicit INVENTORY GATE separates source enumeration from analysis; per-source
template applied to each source in the inventory after the gate clears
**Hypothesis:** Leading with a dedicated source-enumeration step before any analysis begins prevents the
"phantom data" failure mode (C-01) and ensures the model cannot analyze a source that was not explicitly
named in the inventory. The per-source analysis template then applies C-02 through C-05 uniformly. Tests
whether separating "what do I have?" from "what does it show?" produces more grounded analysis than
integrated analysis instructions.

```
You are running /prove-analysis. Fill in this structured template.
Complete each section in order. Do not begin any ANALYSIS section until INVENTORY is complete.

---

## SETUP: HYPOTHESIS

Hypothesis under investigation: [State the hypothesis in one sentence. Use the exact wording from the
feature context or topic file. This is the claim all patterns must be evaluated against.]

---

## INVENTORY: DATA SOURCES

[List every data source you have access to before analyzing any of them.
A data source must be a named, specific artifact: a file, table, schema, scenario set, telemetry
log, test suite, or system -- not "the data" or "existing telemetry".
Do not analyze anything yet. Enumerate only.]

Available data sources:
1. [Source name]: [What kind of artifact it is and where it comes from]
2. [Source name]: [What kind of artifact it is and where it comes from]
3. [Add all accessible sources -- include sources even if you expect no pattern there]

Sources inaccessible or not present: [List any expected sources you cannot access. Write "None" if
all expected sources are accessible.]

[INVENTORY GATE: Do not begin any ANALYSIS section until this inventory is complete and all source
names are filled in above.]

---

## ANALYSIS: [SOURCE NAME]

[Repeat this section once per source listed in INVENTORY. Replace [SOURCE NAME] with the exact
source name from the inventory list. Do not add sources that were not in the inventory.]

Source: [Exact name from INVENTORY -- must match]
Pattern: [What pattern was found in this source. State it directly. If no pattern was found,
  write: "No pattern detected." Do not hedge.]
Hypothesis bearing: [How this pattern bears on the hypothesis stated in SETUP. Explain the
  connection explicitly -- one to two sentences. Do not leave it implicit.]
Correlation or causal: [Label this relationship. Use one of: "Correlation only", "Association
  (directional, not causal)", or "Causal". If causal, state the basis in one clause. If
  correlation only, state that causation cannot be inferred from this source and why not.
  Do not omit this label. Do not use "relationship" without a type.]
Strength: [Assess the strength of this pattern. Provide at least one of: sample size, prevalence
  rate, N of M cases, effect size, confidence level, or a reasoned tier (weak / moderate / strong)
  with explicit justification. Vague qualifiers ("significant", "notable") without backing do not
  satisfy this field.]
Counter-evidence: [Note any data within this source that weakens, contradicts, or limits the
  pattern. If none, write: "No counter-evidence in this source -- [reason why absence is
  plausible or a genuine gap]."]

[Repeat ANALYSIS section for each source in INVENTORY]

---

## SYNTHESIS

Overall direction: [Summarize what the combined patterns say about the hypothesis. Does the weight
  of evidence support, contradict, or leave the hypothesis unresolved?]
Strongest source: [Name the source with the strongest pattern and state why it is strongest.]
Weakest or absent: [Name any sources where no pattern was found or where evidence was too thin.]
Causation verdict: [Across all sources, is any causal claim supportable? State yes, no, or
  partial -- and the basis in one sentence.]
Scope: [Under what conditions do these patterns hold? Where might they not generalize?]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_analyzed, sources_inaccessible,
causal_claim, overall_direction.
```

---

## V-02: Per-Source 5-Column Table

**Axis:** Output format -- pre-printed 5-column table with columns mapped directly to C-01 through
C-05; one row per data source; supplementary sections for counter-patterns and quantified claims
**Hypothesis:** A pre-printed table whose column headers correspond exactly to the five essential
criteria physically cannot omit any criterion for any source: a blank cell is a visible, detectable
gap. Tests whether table structure is sufficient to guarantee essential criterion coverage without
gating, phasing, or imperative instruction. The supplementary sections are pre-printed to guarantee
C-07 and C-08 surface even when the table rows are complete.

```
You are running /prove-analysis. Fill in the pre-printed template below.
All column headers are fixed. Fill in every cell for every data source row. Do not add, rename,
reorder, or remove any column. Do not leave any cell blank.

---

## HYPOTHESIS

[State the hypothesis in one sentence. All patterns in the ANALYSIS TABLE bear on this hypothesis.]
Hypothesis: [FILL IN]

---

## ANALYSIS TABLE

[Read all column instructions before filling in any row.]

Column instructions:
- **Source** (C-01): Name the specific artifact: file name, table name, schema, scenario set,
  telemetry log, test suite. Not "the data." Not "existing telemetry." If you cannot name it,
  you do not have access to it -- do not add that row.
- **Pattern found** (C-02): State what pattern exists in this source. Write "No pattern detected"
  if none. Do not hedge.
- **Hypothesis bearing** (C-03): Explain how this pattern bears on the hypothesis above.
  One to two sentences. Do not leave the connection implicit.
- **Correlation or causal?** (C-04): Write one of: "Correlation only", "Association (directional,
  not causal)", or "Causal (basis: [one clause])". Do not omit. Do not write "relationship"
  without this label.
- **Strength** (C-05): Write weak / moderate / strong -- followed by at least one of: a number,
  rate, count, or logical argument. Do not write "significant" or "notable" without backing.

| Source | Pattern found | Hypothesis bearing | Correlation or causal? | Strength |
|--------|--------------|-------------------|------------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [How it bears on the hypothesis] | [Correlation only / Association / Causal (basis: ...)] | [Tier + justification] |
| [Name] | [Pattern or "No pattern detected"] | [How it bears on the hypothesis] | [Correlation only / Association / Causal (basis: ...)] | [Tier + justification] |
[Add one row per distinct accessible data source. Minimum two rows required.]

---

## COUNTER-PATTERNS

[Required. At least one entry must be present. Note data that weakens, contradicts, or limits the
patterns in the ANALYSIS TABLE. If a source had no counter-evidence, explain why its absence is
plausible or identify it as a genuine gap.]

- [Source]: [Data that weakens, contradicts, or limits the pattern from the table.
  Or: "[Source]: No counter-evidence found -- [reason why absence is plausible or a genuine gap]."]
[One entry per source where counter-evidence exists or was sought and not found.]

---

## QUANTIFIED SUMMARY

[Required. At least one numeric claim must appear here. Extract from the table or provide directly.
Vague qualifiers alone ("most", "often", "sometimes") do not satisfy this section.]

- [Pattern claim with number: "N of M sources showed...", "X% of scenarios...",
  "N cases out of M total...", "p < N", "effect size N", etc.]
[Add additional quantified claims as warranted by the data.]

---

## VERDICT

Overall direction: [Support / Contradict / Inconclusive] -- [one sentence summary]
Causal claim supportable: [Yes / No / Partial] -- [one sentence basis citing the table]
Scope: [Conditions under which these patterns hold and where they may not generalize.]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, causal_claim, overall_direction.
```

---

## V-03: Imperative/Conversational Register

**Axis:** Phrasing register -- short imperative sentences per analytical obligation; direct commands
replace formal section headers; no pre-printed table structure; five-step checklist framing
**Hypothesis:** Direct imperative phrasing ("Name it. State the pattern. Say whether it is
correlation or causation.") reduces the hedge language and evasive qualification that formal
descriptive instructions often invite. The checklist framing makes each obligation feel like
a discrete action to complete, not a criterion to satisfy. Tests whether register alone produces
five-obligation coverage without structural scaffolding, and whether conversational phrasing
produces less causation underclaim or strength vacuum than formal templates.

```
You are running /prove-analysis.

Analyze the data you have access to for patterns that bear on the hypothesis. Work through each
data source. For each one, complete five steps in order. No skipping steps.

---

**The hypothesis:**
State it here before you look at anything.
Hypothesis: [FILL IN -- one sentence, exact wording from the feature or topic context]

---

**For each data source, do these five things:**

**Step 1 -- Name it.**
Use the exact file name, table name, schema name, scenario set, or log identifier. "The data" is
not a name. "Existing telemetry" is not a name. If you cannot name it, you do not have access to
it -- do not cite it.

**Step 2 -- State the pattern.**
What did you actually find? Be direct. "X correlates with Y." "When A increases, B increases." If
you found nothing, say: "No pattern detected in [source]." Do not hedge.

**Step 3 -- Connect it to the hypothesis.**
Say explicitly how this pattern bears on the hypothesis you wrote above. Do not leave it implied.
One or two sentences. Start with: "This bears on the hypothesis because..." or equivalent.

**Step 4 -- Say correlation or causation.**
Label it. Pick one: this is a correlation, an association, or a causal relationship.
- If causal: say what makes you confident causation is established (logical necessity, experimental
  isolation, temporal precedence, or other basis).
- If correlation only: say you cannot infer causation from this source and state why not.
Do not skip this step. Do not use "relationship" without a type.

**Step 5 -- Assess the strength.**
Give it a number, a rate, a count, or a tier (weak / moderate / strong) with a reason.
"Significant" without backing does not count. "Notable" without backing does not count.

---

**Work through each source now:**

[ANALYSIS: SOURCE 1]
Source: [Name]
Pattern: [What you found, or "No pattern detected"]
Hypothesis connection: [How this bears on the hypothesis, starting with an explicit link]
Correlation or causal: [Your label + basis or reason for limitation]
Strength: [Your assessment with backing -- number, rate, count, or tier + justification]
Counter-evidence: [Anything in this source that weakens the pattern, or "None -- [brief reason]"]

[ANALYSIS: SOURCE 2]
Source: [Name]
Pattern: [What you found, or "No pattern detected"]
Hypothesis connection: [How this bears on the hypothesis, starting with an explicit link]
Correlation or causal: [Your label + basis or reason for limitation]
Strength: [Your assessment with backing -- number, rate, count, or tier + justification]
Counter-evidence: [Anything in this source that weakens the pattern, or "None -- [brief reason]"]

[Continue for each accessible data source. Use [ANALYSIS: SOURCE N] as the section header.]

---

**When you have worked through all sources, summarize:**

What do the patterns say together? Does the evidence support the hypothesis, cut against it, or
leave it unresolved? Be direct.
Overall: [FILL IN -- two to three sentences]

Is any causal claim defensible across sources?
Causation: [Yes / No / Partial] -- [one sentence basis citing the specific sources that support it]

Where do these patterns not apply? Name the boundaries.
Scope: [FILL IN -- population, time window, platform, or configuration limits]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_analyzed, causal_claim, overall_direction.
```

---

## V-04: Gated Phase Lifecycle

**Axes:** Role sequence + Lifecycle emphasis -- numbered phases with explicit GATE lines map each
phase to one essential criterion; no phase output is valid until the previous GATE fires; the
gating prevents criteria from bleeding into each other or being collapsed
**Hypothesis:** Explicitly sequencing the five essential obligations as discrete phases with gate
lines prevents the most common omission pattern in multi-criterion skills: the model satisfies
some criteria by implication while skipping others because they were never independently demanded.
Separating pattern extraction (PHASE 3) from hypothesis connection (PHASE 4) from causal labeling
(PHASE 5) makes each obligation a standalone completion event. Tests whether gate-enforced
sequencing produces higher per-criterion completeness than integrated per-source templates.

```
You are running /prove-analysis. Execute each phase in order.
A GATE must be satisfied before the next phase begins. Do not skip phases, merge phases, or
produce output from a later phase before the current phase GATE is met.

---

## PHASE 1: HYPOTHESIS

[GATE: Write the hypothesis before any data source is named or analyzed. No source names.
No patterns. Hypothesis only.]

Hypothesis: [State the hypothesis in one sentence. Use the exact wording from the feature context
or topic file. This is the claim that all subsequent phases bear on.]

PHASE 1 GATE: Hypothesis stated above. Proceed to PHASE 2.

---

## PHASE 2: INVENTORY

[GATE: Enumerate all accessible data sources before analyzing any. A source must be named -- a
specific file, table, schema, scenario set, telemetry log, test suite, or system. "The data" and
"existing telemetry" are not source names. List inaccessible sources explicitly.]

| # | Source name | Type (file / table / schema / scenario set / log / test suite) | Accessible? |
|---|------------|---------------------------------------------------------------|-------------|
| 1 | [Name]     | [Type]                                                        | Yes / No    |
| 2 | [Name]     | [Type]                                                        | Yes / No    |
[Continue for all sources, including inaccessible ones. All subsequent phases operate on
accessible sources only.]

PHASE 2 GATE: All sources inventoried. Proceed to PHASE 3 for accessible sources only.

---

## PHASE 3: PATTERN EXTRACTION

[GATE: For each accessible source from PHASE 2, state the pattern found. No hypothesis
connections yet. No correlation/causation labels yet. No strength assessments yet. Patterns only.
Also note counter-evidence in the same pass.]

For each source:
- [Source name]: [Pattern found. Or: "No pattern detected."]
  Counter-evidence: [Data that weakens or contradicts the pattern. Or: "None identified."]
[One entry per accessible source from PHASE 2.]

PHASE 3 GATE: All patterns and counter-evidence stated. Proceed to PHASE 4.

---

## PHASE 4: HYPOTHESIS CONNECTION

[GATE: For each source with a pattern from PHASE 3, explicitly connect the pattern to the
hypothesis from PHASE 1. No correlation/causation labels yet. No strength assessments. Connections
only. For sources with no pattern, state what the absence implies.]

For each source:
- [Source name]: [How this pattern bears on the hypothesis stated in PHASE 1. One to two sentences.
  Do not leave the connection implicit. Start with: "This bears on the hypothesis because..." or
  equivalent explicit link.]
  [For sources with no pattern: "No pattern detected. Absence is [consistent with / inconsistent
  with / uninformative about] the hypothesis because [brief reason]."]
[One entry per accessible source from PHASE 2.]

PHASE 4 GATE: All patterns connected to hypothesis. Proceed to PHASE 5.

---

## PHASE 5: CORRELATION vs. CAUSATION

[GATE: For each source that produced a pattern in PHASE 3, assign a relationship label. This is
a dedicated labeling phase -- not a label that appears incidentally elsewhere. Every source with
a pattern must receive an explicit label here.]

For each source with a pattern:
- [Source name]: [Choose one label:]
  "Correlation only" -- [State why causation cannot be inferred from this source.]
  "Association (directional, not causal)" -- [State the directional claim and its basis.]
  "Causal" -- [State the basis: logical necessity, temporal precedence, experimental isolation,
    or other justification. Be specific.]

PHASE 5 GATE: All relationships labeled. Proceed to PHASE 6.

---

## PHASE 6: STRENGTH ASSESSMENT

[GATE: For each source, assess the statistical or logical strength of its pattern. Vague
qualifiers alone ("significant", "notable", "strong evidence") without backing do not satisfy
this phase. Each entry must include a number, a rate, a count, or a logical argument for
the strength tier assigned.]

For each source:
- [Source name]: [Strength tier: weak / moderate / strong]
  Justification: [At least one of: sample size, N of M cases, percentage, effect size,
    p-value, logical argument for why the evidence is or is not compelling.
    Do not repeat the pattern description. Assess only the strength of the evidence.]

PHASE 6 GATE: All strengths assessed. Proceed to SYNTHESIS.

---

## SYNTHESIS

Overall direction: [Does the combined evidence from all phases support, contradict, or leave
  unresolved the hypothesis? One paragraph drawing on all phase outputs.]
Strongest source: [Which source provided the strongest evidence and why -- reference PHASE 6.]
Causation verdict: [Across all sources, is any causal claim supportable? State yes, no, or
  partial. Cite the PHASE 5 labels explicitly.]
Scope: [Where do these patterns hold and where may they not generalize? Population, time window,
  platform, or configuration constraints on validity.]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_inventoried, sources_with_patterns,
causal_claim, overall_direction.
```

---

## V-05: Table + Null Hypothesis Column

**Axes:** Output format + Inertia framing -- pre-printed 6-column table adds a "Null expectation
met?" column that forces explicit comparison against what the data would look like if the
hypothesis were false; null expectation is pre-stated before any row is filled
**Hypothesis:** The "inertia" of data analysis is the null hypothesis -- the status-quo explanation
that the hypothesis must beat. Explicitly naming the null expectation before analysis begins and
then forcing a per-row "Null met / Null not met / Ambiguous" judgment produces stronger C-04
labeling (because correlation claims are easier to separate from causal claims when the null is
visible) and structurally demands C-07 counter-pattern identification (because "Null met" rows
are by definition disconfirming evidence). Tests whether null-hypothesis framing as a pre-printed
column produces richer and more honest analysis than analysis that never explicitly states what
would falsify the hypothesis.

```
You are running /prove-analysis. Fill in the pre-printed template below.
All column headers are fixed. Fill in every cell for every data source row.
The "Null expectation met?" column is required -- it compares each pattern against what the data
would look like if the hypothesis were false. State the null expectation before filling any rows.
Do not rename, reorder, omit, or leave blank any column.

---

## HYPOTHESIS

[State the hypothesis in one sentence.]
Hypothesis: [FILL IN]

Null expectation: [What would the data look like if this hypothesis were false? One sentence.
  This is the comparison baseline for every "Null expectation met?" cell in the table below.
  Fill this in before writing any table row. Do not omit.]

---

## ANALYSIS TABLE

[Column instructions -- read before filling any row:]
- **Source** (C-01): Specific named artifact. Not "the data." Not "existing telemetry." If you
  cannot name it, do not add a row for it.
- **Pattern found** (C-02): What you found. Write "No pattern detected" if none. Do not hedge.
- **Null expectation met?**: Compare the pattern to the null expectation stated above.
  Write one of:
  -- "Null met" -- the data looks like the null; this source does not support the hypothesis
  -- "Null not met" -- the data differs from the null; this source is consistent with the hypothesis
  -- "Ambiguous" -- the data is compatible with both; state why in the Hypothesis bearing column
- **Hypothesis bearing** (C-03): How this pattern bears on the hypothesis. One to two sentences.
  Do not leave the connection implicit. For "Null met" rows, explain what the disconfirmation means.
- **Correlation or causal?** (C-04): Write one of: "Correlation only", "Association (directional,
  not causal)", or "Causal (basis: [one clause])". Required. Do not use "relationship" without type.
- **Strength** (C-05): Tier (weak / moderate / strong) + at least one number, rate, count, or
  logical justification. Do not write "significant" or "notable" without backing.

| Source | Pattern found | Null expectation met? | Hypothesis bearing | Correlation or causal? | Strength |
|--------|--------------|----------------------|-------------------|------------------------|----------|
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Bearing on hypothesis -- for Null met rows explain the disconfirmation] | [Correlation only / Association / Causal (basis: ...)] | [Tier + justification] |
| [Name] | [Pattern or "No pattern detected"] | [Null met / Null not met / Ambiguous] | [Bearing on hypothesis -- for Null met rows explain the disconfirmation] | [Correlation only / Association / Causal (basis: ...)] | [Tier + justification] |
[Add one row per distinct accessible data source. Minimum two rows required.]

---

## COUNTER-PATTERN SUMMARY

[Collect all rows where "Null expectation met?" is "Null met" or where no pattern was detected.
These are the disconfirming data. Required -- do not omit.]

- [Source (Null met)]: [What this disconfirmation implies for the hypothesis -- is this a genuine
  limit, a scope condition, a measurement artifact, or evidence the hypothesis is wrong?]
[If no sources met the null and no patterns were absent: "All analyzed sources produced patterns
inconsistent with the null expectation. Disconfirming data was not found in the available
sources -- this is a genuine gap; identify at least one source that would be expected to show
the null pattern if the hypothesis does not hold."]

---

## QUANTIFIED CLAIMS

[Required. At least one numeric claim. Extract from the table or provide directly.]

- [Quantified claim: "N of M sources showed patterns inconsistent with the null" or
  "X% of scenarios..." or "N cases out of M..." or effect size or rate.]
[Add additional quantified claims as warranted.]

---

## VERDICT

Null summary: "[N] of [M] analyzed sources met the null expectation (hypothesis unsupported in
  those sources); [K] did not (consistent with hypothesis)."
Overall direction: [Support / Contradict / Inconclusive]
Causal claim supportable: [Yes / No / Partial] -- [one sentence basis citing the table]
Scope: [Conditions under which these patterns hold. Where might they not generalize?
  Population, time window, platform, or configuration constraints.]

---

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, hypothesis, sources_count, null_met_count, null_not_met_count,
causal_claim, overall_direction.
```

---

## Round 1 Design Notes

### Core structural challenge for prove-analysis

Unlike scout-feasibility (which has a single linear pipeline: PM -> Architect -> Strategy -> Verdict),
`prove-analysis` has a per-source loop. The model must apply five distinct obligations to every data
source. The primary failure modes this creates:

- **Partial loop coverage**: C-04 and C-05 are satisfied for the first source but omitted for subsequent ones
- **Criteria bleeding**: correlation/causation labels appear in strength paragraphs; strength claims bleed into
  hypothesis connection sentences; the model satisfies two criteria in one sentence without explicit labels
- **Phantom data**: sources are cited that the model inferred rather than accessed
- **Loop collapse**: multiple sources are analyzed in a single block without per-source delineation

### How each variation addresses the loop problem

| V | Loop mechanism | Omission risk |
|---|---------------|---------------|
| V-01 | Inventory gate + per-source named sections | Low -- named sections enforce per-source delineation |
| V-02 | Table rows + fixed columns | Very low -- blank cells are visible failures |
| V-03 | Imperative checklist repeated per source | Moderate -- model may compress steps without explicit gating |
| V-04 | Gated phases where each phase fires for ALL sources | Low -- phases separate criteria; partial firing is visible |
| V-05 | Table rows + null column | Very low -- blank cells; "Null met" rows are structurally counter-patterns |

### Inertia framing translation

For analysis skills, "inertia" is the null hypothesis -- the status-quo explanation that the
hypothesis must beat. V-05 makes this explicit: before any source is analyzed, the analyst must
state what the data would look like if the hypothesis were false. Every pattern is then evaluated
against that baseline. This is the analytical equivalent of the feasibility skill's "Do-nothing cost":
it forces the analyst to reason about the alternative before committing to a conclusion.

### C-07 structural guarantee comparison

| V | How C-07 is guaranteed |
|---|------------------------|
| V-01 | Pre-printed "Counter-evidence:" field per source |
| V-02 | Pre-printed COUNTER-PATTERNS section (required, cannot be omitted) |
| V-03 | "Counter-evidence:" field per source in imperative template |
| V-04 | Counter-evidence captured in PHASE 3 alongside pattern extraction |
| V-05 | "Null met" rows in table ARE the counter-patterns; COUNTER-PATTERN SUMMARY section pre-printed |

### Predicted differentiation under rubric

All five variations target 100/100 under the v1 rubric. Within-100 differentiation:

| Dimension | Strongest | Why |
|-----------|----------|-----|
| C-01 phantom-data prevention | V-01, V-04 | Inventory gate prevents unchecked citation |
| C-04 structural guarantee | V-02, V-05 | Fixed column cannot be skipped |
| C-07 counter-pattern depth | V-05 | Null column makes disconfirmation structurally visible |
| C-08 quantification | V-02, V-05 | Pre-printed QUANTIFIED CLAIMS section enforces numeric output |
| C-09 causal mechanism (aspirational) | V-04 | Phase 5 basis requirement prompts mechanism reasoning |
| C-10 scope (aspirational) | V-04, V-05 | Explicit scope field pre-printed in synthesis/verdict |
| Template overhead | V-03 | Minimum structure; tests imperative register floor |

### Open research questions for R1

1. Does V-03's imperative register produce shorter but more direct outputs, or does it produce
   outputs that satisfy criteria by implication without explicit labels?
2. Does V-05's null-column framing cause the model to over-report "Null met" rows (confirmation
   bias reversal) or does it produce more honest disconfirmation acknowledgment?
3. Does V-04's phase separation produce richer per-phase depth or cause the model to repeat
   the same content across phases?

### V-golden candidate

**V-02** is the baseline target: table structure forces all five essential criteria per source,
supplementary sections cover C-07 and C-08, format is compact enough to run without output overload.

**V-05** is the richer candidate: null-column framing adds hypothesis-falsification discipline and
structurally guarantees C-07 through "Null met" row counting. Key open question: does the null
framing improve analysis quality enough to justify the additional setup overhead (pre-stating null
expectation before any row)?

**V-04** is the strongest structural competitor for aspirational criteria (C-09, C-10): gated phases
naturally elicit mechanism reasoning in Phase 5 and scope reasoning in Synthesis.
