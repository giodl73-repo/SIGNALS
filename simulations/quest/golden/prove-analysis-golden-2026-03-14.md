Written to `simulations/quest/golden/prove-analysis-golden-2026-03-14.md`.

**Score: 140/140** (v4 rubric) | **Status: GOLDEN**

The five patterns that made V-05 the winner:

1. **PRE-REGISTRATION GATE sentence** — not a field in setup, but a standalone gate line that explicitly locks the mechanism before the FC chain begins. Skipping it breaks document order visibly.

2. **Mechanism adjudication column** — seventh column in the analysis table. Per-source confirmation verdicts live inside the row, not deferred to a post-table synthesis section. The column instruction requires referencing the pre-stated prediction by name.

3. **FC-ID copy constraint** — "Copy from FC-[NN]. Do not rewrite." at the cell level. The numbered pointer forces a paste-by-reference action, making in-table re-derivation structurally awkward rather than just advised against.

4. **VERDICT WRITE-GATE as a discrete three-step artifact producer** — structurally separate from Phase B. Step 3 produces a cleared draft; the VERDICT copies from it. No cleared draft = malformed VERDICT, not just a weak one.

5. **Four-layer ordering preamble** — names all four structural layers before the first section, making out-of-order composition an explicit instruction violation rather than a stylistic choice.
rrelation only: [basis for the limitation]"
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

## What Made It Golden

**1. Pre-registration gate as a structural boundary, not a field**

V-01 through V-04 placed the mechanism prediction as a named field inside the hypothesis setup section. The PRE-REGISTRATION GATE line in V-05 is a standalone sentence that explicitly names itself as a gate and instructs the model to proceed -- creating a visible structural lock between setup and evidence. A field can be added retroactively; a gate sentence that says "Do not name any data source before this gate" cannot be skipped without breaking document order.

**2. Mechanism adjudication column forces per-source verdicts inside the table**

Earlier variations post-hoc collected mechanism verdicts in a MECHANISM ANALYSIS section after the table. V-05 adds a seventh column -- Mechanism adjudication -- with three permitted verdict terms (Confirmed / Not confirmed / Silent) and a column instruction requiring explicit reference to the pre-stated prediction. Post-table synthesis cannot satisfy this criterion because the verdict must appear in the table row for that source.

**3. Falsification chain traceability via FC-ID copy constraint**

The "Copy from FC-[NN]. Do not rewrite." instruction at the column level creates a numbered pointer that makes in-table re-derivation structurally awkward. The model must name a specific block, paste its exact text, and acknowledge the constraint -- three separate actions that collectively prevent softening of null verdicts after observing pattern data.

**4. VERDICT WRITE-GATE as a discrete gate section, not Phase B**

The VOCABULARY COMPLIANCE AUDIT (Phase A + Phase B) and the VERDICT WRITE-GATE are structurally separate. Phase B audits prose sections. The VERDICT WRITE-GATE is a three-step artifact producer: Step 1 drafts, Step 2 audits, Step 3 produces a cleared draft. The VERDICT then copies from Step 3. This means a VERDICT composed before Step 3 is structurally malformed -- the write-gate produces a discrete artifact that either exists or doesn't.

**5. Four-layer ordering preamble locks execution sequence**

The four-bullet preamble ("Read ALL sections before filling in any. Complete sections in the order written. Do not skip forward.") names the four structural layers explicitly. A model that attempts to compose the VERDICT first must skip three labeled sections -- the preamble makes that skip visible and in violation of explicit instruction rather than merely inadvisable.

---

## Final Rubric Summary (v5)

| Tier | Criteria | Count | Points |
|------|----------|-------|--------|
| Essential | C-01 Source named, C-02 Pattern stated, C-03 Hypothesis connection, C-04 Correlation/causation labeled, C-05 Strength assessed | 5 | 60 |
| Recommended | C-06 Multiple data sources, C-07 Counter-patterns, C-08 Quantified claims | 3 | 30 |
| Aspirational | C-09 Causal mechanism, C-10 Scope conditions, C-11 Per-source structured format, C-12 Null/falsification framing, C-13 Vocabulary precision, C-14 Pre-registered mechanism, C-15 Document-wide vocabulary audit, C-16 Per-source falsification, C-17 Falsification chain traceability, C-18 Pre-write verdict audit, C-19 Mechanism pre-registration gate, C-20 Per-source mechanism adjudication column | 12 | 60 |
| **Total** | | **20** | **150** |

V-05 scored **140/140** against the v4 rubric (the active rubric at time of quest run).
C-19 and C-20 were introduced in the v5 rubric after R4 completed; V-05 satisfies both structurally.
