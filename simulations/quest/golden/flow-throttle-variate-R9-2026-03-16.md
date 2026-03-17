# flow-throttle Variate — Round 9 (v9 Rubric)

**Date:** 2026-03-16
**Rubric:** v9 (C-01 through C-26, N_essential=5, N_recommended=3, N_aspirational=18)
**Baseline ceiling:** R8 V-05 (confirmed passes C-01 through C-24 under v8)

---

## State Analysis: What R8 V-05 Has vs. What R9 Must Add

**R8 V-05 coverage under v9 (confirmed):**
- C-01 through C-22: all pass (verified through R8)
- C-23: passes — each prose passage carries an inline authorization tag referencing the
  specific C-20 exception by number or label (e.g., `[prose: item 2 — burst narrative]`)
- C-24: passes — TYPE SCAN GATE appears between TABLE E (risk taxonomy) and TABLE F
  (mitigations), enumerates each expected type category (Burst, Cascade, RetryAfter),
  reports per-category Y/N presence verdict, and states an explicit PROCEED or BLOCKED
  decision before TABLE F opens

**C-25 failure in R8 V-05:**

R8 V-05's PROSE-RESTRICTION DECLARATION enumerates the complete closed list of
prose-permitted contexts and satisfies C-20. It does not enumerate a structured-output
exemption class. The declaration is of the form:

> "Prose is permitted in exactly three contexts: (1) binding-tier causal reason, (2)
> binding constraint exclusivity statement, (3) global criterion-coverage verdict notes."

An executor applying C-23 to this declaration and encountering a TYPE SCAN GATE verdict
line ("PROCEED" or "BLOCKED") or a cross-artifact header line ("One row per risk from
TABLE E. No risk may be omitted.") must decide whether these require `[prose: item N]`
tags. The declaration names what is prose; it does not name what is not prose. The
classification boundary is implicit. A tagger can produce false compliance (tagging
PROCEED as `[prose: item 1]`) or false violation (omitting tags from gate verdicts and
receiving a C-23 audit failure). C-25 closes the boundary at the declaration level by
naming the structured-output types that are exempt from C-23 tagging, making
classification determinable by element type without content interpretation.

**C-26 failure in R8 V-05:**

R8 V-05's TYPE SCAN GATE satisfies C-24: a named gate step, per-category presence
verdicts, PROCEED/BLOCKED decision. The gate carries no Purpose annotation. An executor
reading the gate block sees the requirement to confirm each type category and deliver a
verdict — but the gate does not name the failure mode it prevents, nor does it explain
the gap above C-22 that makes it necessary. C-26 requires this annotation: "C-22 ensures
the Type column is present and all categories appear in the finished output. This gate
ensures type completeness is an explicit named structural check, not an implicit property
verifiable only by reading TABLE E in full. A missing category is a structural block here,
not a detectable gap in hindsight."

Without the Purpose annotation, an executor who reasons "C-22 already requires all three
types; the gate is redundant" has no prompt-grounded counter-argument. The annotation
demolishes that reasoning at the point of execution.

---

## Round 9 Variation Map

| Variation | Axes | C-25 | C-26 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Inertia framing (single axis) | PASS | PASS | 175+/180 |
| V-02 | Phrasing register (single axis) | PASS | PASS | 175+/180 |
| V-03 | Lifecycle emphasis (single axis) | PASS | PASS | 175+/180 |
| V-04 | Role sequence + Inertia framing (combined) | PASS | PASS | 175+/180 |
| V-05 | Role sequence + Lifecycle emphasis + Inertia framing (combined) | PASS | PASS | 180/180 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Does escape-route naming for C-25/C-26 outperform explanatory
register, or are both equally reliable once the requirement is explicit?
Hypothesis: both pass C-25/C-26; V-01 may produce more auditable exemption-class text
because the named escape route makes the required form visible at the point of definition.

Q2 (V-01 vs V-03): Does expanding the C-25 exemption class to a parallel named sub-section
improve compliance compared to inline framing within the prose-restriction declaration?
Hypothesis: V-03's structural expansion may improve output clarity but not compliance rate —
C-25 requires the exemption class to be present in the declaration, not separately housed.
V-03 tests whether co-location at the declaration vs. a parallel section affects the criterion.

Q3 (V-04 vs V-05): Does adding lifecycle emphasis (expanded C-26 annotation block) on top
of role sequencing produce incremental gains, or does the role-sequence change dominate?
Hypothesis: the role-sequence change (Format Analyst activating first) dominates C-25
compliance because it makes the exemption class a precondition for all output; C-26
benefits more from the lifecycle expansion.

---

## V-01 — Single Axis: Inertia Framing

**Axis:** C-25 and C-26 additions name the specific escape-route misjudgments at their
enforcement points. C-25's exemption class includes an explicit statement of what
misjudgment the class prevents (tagging structured output as prose from content
inspection). C-26's Purpose annotation names the specific reasoning chain that leads
executors to omit it (C-22 already ensures type completeness — gate appears redundant).

**Hypothesis:** Naming the misjudgment pattern at the enforcement point is more
durable than stating the requirement in abstract form. An executor who reads "gate
appears redundant because C-22 already requires all types" has a named escape route;
the annotation demolishes it in place rather than leaving it implicit.

**v9 predicted scoring:** C-25 PASS (exemption class present with named escape route).
C-26 PASS (Purpose annotation with named failure mode and escape-route rebuttal).
All other criteria carry from R8 baseline. Predicted composite: 175+/180.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

**PROSE-RESTRICTION DECLARATION**

This declaration is the format contract for all output below. It precedes every table.

Prose is permitted in exactly three contexts:
1. **Binding-tier causal reason** — one paragraph naming why the primary bottleneck tier
   fails before all others under the described load pattern. (C-01)
2. **Binding constraint exclusivity statement** — one sentence naming the mechanism that
   prevents at least one non-binding tier from failing first. (C-14)
3. **Global criterion-coverage verdict notes** — one sentence per criterion in the final
   coverage step, for FAIL verdicts only.

All other content must appear in structured tables. A prose passage outside these three
declared contexts is a format violation detectable without content review.

**STRUCTURED OUTPUT EXEMPTION CLASS — prevents false-positive C-23 tagging (C-25):**

The following element types are structured output, not prose, and are **exempt from C-23
inline citation requirements**:
- Gate decision lines: PROCEED / BLOCKED (produced by the TYPE SCAN GATE)
- Cross-artifact header lines at derived tables: "One row per [source]. No [item] may
  be omitted." (produced at the opening of TABLE C, TABLE E, TABLE F)
- Phase boundary prohibition lines: "PROHIBITED: ..." (produced at phase transitions)
- Per-criterion verdict lines in the global coverage step: "C-NN: PASS / FAIL"

**Escape route for C-25:** The temptation is to treat gate decision lines as prose
because they appear in narrative positions and PROCEED is an affirmative statement that
content inspection classifies as non-table output. An executor applying C-23 without an
exemption class must interpret content to determine whether PROCEED needs a `[prose:
item N]` tag — producing either false compliance (tagging a gate verdict) or an
unresolvable ambiguity (omitting the tag without a stated basis). The exemption class
forecloses content inspection: an element is structured output if its type is listed
above, regardless of where it appears.

---

**PHASE 1 — EVIDENCE PHASE**

**PHASE 1 ENTRY:** Read the signal in full before populating any table below.

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before any tier is named. Every numeric threshold cited in
Phases 1B and 2 must have a register entry. A tier with no entry is flagged UNDOCUMENTED
rather than assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

**PHASE 1A GATE:** Source register closed. PROHIBITED: adding a new Source-ID after
this line. — *prevents retroactive source injection; C-11 is verifiable by inspection
only if the evidence base was locked before claims were built*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

One row per rate-limiting component. No source-register entry = flag UNDOCUMENTED in
the Limit column rather than assigning an inferred value.

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance failure
  condition: an informal synonym ("the connector limit", "API gateway") in place of the
  T-NN identifier fails the threading requirement.
- `Limit` — a specific number with a unit (e.g., "1,200 req/min"). Compliance failure
  condition: a vague label ("limited", "throttled") in place of a specific number-with-unit
  fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — Y for the one tier that fails first at 1x; N for all others. Exactly one Y.
- `Failure mode` — hard rejection, queue saturation, silent drop, degraded throughput, or
  timeout. At least two distinct values must appear across rows.

**PHASE 1B GATE:** Tier inventory closed. PROHIBITED: introducing a new T-NN in any
Phase 2 section. — *prevents scope creep; a tier discovered during claims analysis is
evidence Phase 1 was incomplete, not a fill-in opportunity*

[prose: item 1 — binding-tier causal reason] **Primary bottleneck:** State which tier has Binding? = Y and why it reaches its limit before all others under 1x nominal load.

[prose: item 2 — binding constraint exclusivity] **Exclusivity statement:** For at least one Binding? = N tier, name the mechanism that prevents it from failing before the binding tier under the described load pattern.

---

**PHASE 2 — CLAIMS PHASE**

**PHASE 2 ENTRY CONDITION:** Phase 2 opens only after PHASE 1B GATE is cleared. The
tier registry is closed. PROHIBITED: opening Phase 2 before the PHASE 1B GATE is
cleared. — *prevents late evidence injection; a tier entering claims analysis without a
source register entry cannot be verified against C-11*

**For each tier in TABLE A** — enumerate all tiers from the Phase 1B inventory in every
downstream table. — *[C-17 enumeration anchor: coverage is verifiable by T-NN match
against TABLE A, not by reading the downstream table in full] — prevents coverage elision*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. No T-NN may appear here that is absent from TABLE A.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

- `From (Tier-ID)` — must reference a T-NN from TABLE A.
- `Mechanism` — Permitted values: queue-fill, connection-hold, retry-amplification,
  dependency-stall, timeout-cascade. Compliance failure condition: a generic term
  ("blocked", "slowed") in place of a named mechanism from the permitted set fails this
  column's precision requirement.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

- `Error code or signal` — specific HTTP status code or platform signal identifier
  (e.g., "HTTP 429", "HTTP 503"). Compliance failure condition: a plain description
  ("request fails", "throttle error") in place of a specific code or identifier fails
  this column's precision requirement.
- `Failure if Retry-After ignored` — name the escalation path specifically: retry storm
  (exponential backoff failure), quota exhaustion (circuit breaker), connection hold
  (pool exhaustion).

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no unprotected path exists, row 1 states the
conclusion with ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. At least one Burst row, one Cascade row, one
RetryAfter row. No T-NN may appear that is absent from TABLE A.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

- `Type` — Permitted values: Burst, Cascade, RetryAfter. Per-type minimum: ≥1 row each.
  Compliance failure condition: a risk list without type classification fails C-22 even
  if all required categories happen to appear, because the mechanism that makes category
  absence detectable is absent.

---

**TYPE SCAN GATE**

**Purpose — prevents category elision above C-22 (C-26):** C-22 ensures the Type column
is present and all three categories appear in the finished TABLE E. This gate ensures type
completeness is an explicit named structural check, not an implicit property verifiable
only by reading TABLE E in full. Without this gate, a missing category is detectable only
after the mitigation table is complete — at which point mitigation coverage for that
category is also absent. The gate makes a missing category a blocking condition before
TABLE F opens.

**Escape route for C-26:** The temptation is to omit this Purpose annotation on the
grounds that C-22 already requires the type taxonomy — the gate appears to add process
without adding substance. This reasoning is self-defeating: C-22 ensures the structure
*exists*; this gate ensures the structure is *verified before construction continues*. An
executor who completes TABLE F before noticing the missing Cascade row has produced an
output that satisfies C-22's structural requirement but has undetectably absent cascade
mitigations. The gate forecloses that execution path.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add a row for the missing type, then re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name. Compliance failure condition: a category of action ("add retry logic")
  in place of a specific parameter identifier fails this column's precision requirement.
- `Tradeoff` — name the cost or risk introduced by this mitigation (e.g., "higher memory
  pressure under burst", "increased latency on all requests"). A mitigation without a
  named tradeoff is incomplete.

**PHASE 2 EXIT PROHIBITION:** PROHIBITED: adding rows to TABLE E after TABLE F has
opened. — *prevents retroactive risk injection; a risk discovered during mitigation
analysis is evidence TABLE E was incomplete*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and names causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B has ≥2 rows with T-NN identifiers and specific mechanisms? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component and Scope filled? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID, no tier omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason or ≥2 named controls? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any criterion above that did not pass.

---

---

## V-02 — Single Axis: Phrasing Register

**Axis:** C-25 and C-26 additions use explanatory/WHY-first register rather than
normative SHALL/PROHIBITED form. The exemption class is introduced as a reasoning
explanation ("here is why classification cannot be left to content inspection") rather
than a declaration ("the following types are exempt"). The gate Purpose annotation frames
the C-22 gap as a logical consequence rather than a policy requirement.

**Hypothesis:** The conceptual gap for C-25 and C-26 is a comprehension problem — the
executor does not see why the exemption class or the Purpose annotation is necessary —
not a compliance problem. Explanatory register addresses comprehension directly. Risk:
explanatory prose is less auditable than normative declarations; an executor may absorb
the reasoning and still produce a non-compliant output form. Both register variants
should pass C-25/C-26; V-02 tests whether comprehension-first framing affects output
quality beyond criterion compliance.

**v9 predicted scoring:** C-25 PASS (exemption class present in explanation-form).
C-26 PASS (Purpose annotation present in reasoning-form). Predicted composite: 175+/180.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output — each table captures a finding category that prose cannot
represent with the same auditability. Produce sections in the order shown. Fill every cell.

---

**FORMAT CONTRACT**

The following declaration governs output format for this entire analysis. Read it before
producing the first table.

**Where prose appears:** Prose is permitted only for three specific functions: (1) the
binding-tier causal reason — one paragraph explaining why the primary bottleneck tier
fails before all others; (2) the binding constraint exclusivity statement — one sentence
contrasting the binding tier against at least one non-binding tier; and (3) verdict notes
in the final global coverage step, limited to FAIL verdicts.

Everywhere else, output is structured: tables, gate verdicts, artifact headers,
phase prohibitions. These are not prose — they are structured output types that convey
finding categories, compliance decisions, and phase-boundary conditions. **The reason
this matters:** C-23 requires inline authorization tags on prose passages, but not on
structured output. If the boundary between prose and structured output is left to content
inspection, an executor tagging output must interpret each element to decide whether it
needs a `[prose: item N]` label. Gate verdicts (PROCEED / BLOCKED) look like affirmative
statements in narrative positions, and content inspection could classify them as prose.
The right classification method is element type: gate decision lines, cross-artifact
header lines ("One row per risk from TABLE E. No risk may be omitted."), phase boundary
prohibition lines, and per-criterion verdict lines are structured output — their type
is determinable before their content is read.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER**

Before naming any tier, commit the sources that will supply numeric thresholds. The
reason: a number attributed after the analysis is built is harder to verify than a number
drawn from a pre-committed source register. Any tier with no source register entry receives
the flag UNDOCUMENTED in the Limit column rather than an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

Source register closed after this step. The reason adding new sources later is prohibited:
a source entered after the tier analysis is complete cannot be verified as the basis for
the numeric claim it purports to support — it may be a post-hoc attribution assembled to
satisfy C-11 rather than a pre-committed evidence source.

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register above required. Every
cell filled — an empty cell and "not applicable" produce identical scan results.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim downstream. Informal synonyms break T-NN
  threading and make cross-section tracing a name-resolution task.
- `Limit` — a specific number with a unit. Vague labels cannot anchor the STATUS
  transition logic or the LOAD SHAPE analysis, and tiers without numeric limits cannot
  be verified against the source register.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — Y for the one tier that fails first at 1x; N for all others. Exactly one Y.
- `Failure mode` — hard rejection, queue saturation, silent drop, degraded throughput,
  or timeout. At least two distinct values across rows.

Tier inventory closed after this step. The reason introducing a new T-NN in Phase 2 is
prohibited: a tier that enters claims analysis without a source register entry has no
verifiable Limit value, making the STATUS analysis for that tier unauditable.

**Binding-tier causal reason:** [prose: item 1 — binding-tier causal reason] Why does
the Binding? = Y tier reach its limit before all others under 1x nominal load?

**Binding constraint exclusivity:** [prose: item 2 — binding constraint exclusivity]
For at least one Binding? = N tier, what mechanism prevents it from failing first?

---

**PHASE 2 — CLAIMS PHASE**

Phase 2 opens only after the tier inventory is complete. Use T-NN identifiers from
TABLE A exclusively. The reason: each Phase 2 table derives from TABLE A, and T-NN
identifiers are the join key that makes derivation verifiable.

**Coverage anchor:** Address every tier from TABLE A in each downstream table that
derives from it — TABLE C (UX catalog) and the risk assessment. Coverage is verifiable
by T-NN match, not by reading the content.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must match TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Generic terms ("blocked", "throttled") prevent mechanism-specific
remediation because different mechanisms have different mitigations.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Error code must be a specific HTTP status code or platform signal identifier. A plain
description cannot be mapped to a remediation — "HTTP 429" and "connection reset" have
different retry-after semantics and different mitigation paths.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Type column required — the reason: a count-only
risk list can satisfy minimum-count requirements with two rows of the same failure
category, leaving an entire category uncovered without detection. The Type column makes
category-level gaps detectable by scan.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Per-type minimum: ≥1 Burst, ≥1 Cascade, ≥1 RetryAfter row.

---

**TYPE SCAN GATE**

Before opening TABLE F, verify type completeness in TABLE E. Here is why this gate step
is necessary even though C-22 already requires the Type column and per-type minimums:
C-22 ensures that the finished output has the correct type structure. This gate ensures
that type completeness is verified *during construction*, before the mitigation phase
opens. The practical consequence: an executor who builds TABLE F and then discovers a
missing Cascade row has produced a mitigation table with no Cascade mitigations. The
cascade risk is absent from TABLE F without a detectable gap — TABLE F can appear
complete (all TABLE E rows have mitigation entries) while the Cascade category is
entirely unmitigated. This gate converts that failure from a post-hoc detectable gap
into a blocking condition.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

`Setting or API parameter` — the exact configuration key or API attribute. A category of
action cannot be applied without further research; a named parameter can be applied
immediately.

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Maps output content to essential criterion categories by name.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] FAIL rationale for any criterion above that did not pass.

---

---

## V-03 — Single Axis: Lifecycle Emphasis

**Axis:** Structural space allocation for C-25 and C-26. C-25's exemption class is
elevated to a parallel named sub-section ("STRUCTURED OUTPUT REGISTER") at the same
level as the prose-permitted list, rather than an inline paragraph within the declaration.
C-26's Purpose annotation is expanded to a three-field annotation block with labeled
fields: (1) Failure mode prevented, (2) Gap above C-22, (3) Audit test.

**Hypothesis:** Structural symmetry between the prose-permitted list and the
structured-output exemption class signals equal treatment and produces a more complete
exemption class (all four element types named rather than only the most salient one).
The three-field C-26 annotation block produces a more reliably complete annotation than
inline prose because each field must be filled — an executor cannot satisfy "Purpose"
with a single sentence that references C-22 but omits the audit test.

**v9 predicted scoring:** C-25 PASS (STRUCTURED OUTPUT REGISTER sub-section with
named element types). C-26 PASS (three-field annotation block satisfying all three
C-26 requirements). Predicted composite: 175+/180.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts:
1. Binding-tier causal reason (one paragraph, Phase 1B exit)
2. Binding constraint exclusivity statement (one sentence, Phase 1B exit)
3. Global criterion-coverage verdict notes (FAIL verdicts only, global coverage step)

Every other content element must appear in a table, a gate step, a phase prohibition
line, or a per-criterion verdict line.

**Section B — STRUCTURED OUTPUT REGISTER (C-25)**

The following element types are structured output, not prose. They are exempt from C-23
inline citation requirements. Classification is by element type, not by content.

| Element type | Form | Exempt from C-23? |
|-------------|------|------------------|
| Gate decision lines | PROCEED / BLOCKED | Yes |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | Yes |
| Phase boundary prohibition lines | "PROHIBITED: [data class]" | Yes |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | Yes |

No other element types are added to this register without revising this contract.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; C-11 requires every numeric claim to have a co-located named source; sources
added after claims are built cannot be verified as prior commitments*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... verbatim downstream. Compliance failure condition: an
  informal synonym in place of T-NN fails the tier-ID threading requirement.
- `Limit` — number + unit. Compliance failure condition: vague label fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift across at least two bands.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries, or no
  Y entry, fail the at-most-one binding tier constraint.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
a tier discovered during claims analysis indicates Phase 1B was incomplete*

**[prose: item 1 — binding-tier causal reason]** Why does the Binding? = Y tier fail
before all others at 1x nominal load?

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
what mechanism prevents it from failing before the binding tier?

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; a T-NN entering claims analysis without a source register entry is unverifiable
against C-11*

**Enumeration anchor — for each tier in TABLE A** (C-17): downstream tables derive from
TABLE A and must cover every T-NN. Coverage is verifiable by T-NN count match, not by
content reading. — *prevents coverage elision at the consequence phase*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: generic term fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description in `Error code or signal` fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required; count alone cannot detect category absence.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: a risk list without a Type column with a named taxonomy
and per-type minimum-row constraint fails C-22 even if all categories happen to appear.

---

**TYPE SCAN GATE**

**Annotation block (C-26):**

- **Field 1 — Failure mode prevented:** Category elision — a type category (Burst,
  Cascade, or RetryAfter) is absent from TABLE E, but this is detectable only by reading
  the full table after the fact.
- **Field 2 — Gap above C-22:** C-22 ensures the Type column is present and all three
  categories appear in the *finished* output. This gate ensures type completeness is an
  explicit named structural check *before construction of TABLE F begins*. Without the
  gate, an executor can open TABLE F with an incomplete TABLE E; the mitigation table
  will appear complete (all TABLE E rows have entries) while an entire risk category has
  no mitigations.
- **Field 3 — Audit test:** If the gate is absent, verify type completeness by scanning
  TABLE E after TABLE F is complete. If the gate is present, verify by confirming the
  gate step appears between TABLE E and TABLE F and all three type verdicts are PASS.

Scan TABLE E:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: category of action in `Setting or API parameter` fails precision.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection after mitigation planning is underway*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Per-criterion PASS/FAIL mapped to criterion categories.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] FAIL rationale only.

---

---

## V-04 — Combined: Role Sequence + Inertia Framing

**Axes:** (1) Role sequence — a Format Analyst role activates before the Domain Expert
and produces the PROSE-RESTRICTION DECLARATION including the C-25 exemption class,
making the format contract a precondition for all domain analysis. (2) Inertia framing —
strong named escape-route framing for C-26 at the TYPE SCAN GATE, including the
specific "C-22 makes the gate redundant" reasoning chain that leads executors to omit
the Purpose annotation.

**Hypothesis:** Assigning the prose-restriction declaration (including the C-25 exemption
class) to a dedicated Format Analyst role enforces C-25 compliance because the exemption
class is a role output — the Format Analyst must produce it before the Domain Expert
activates, rather than it being an optional annotation within the Domain Expert's output.
The C-26 inertia framing addresses the comprehension gap independently of role structure:
the "redundancy" escape route is named and demolished at the gate step regardless of
which role produces it.

**v9 predicted scoring:** C-25 PASS (Format Analyst role produces the exemption class
as a required output). C-26 PASS (gate Purpose annotation with redundancy escape-route
named and rebutted). Predicted composite: 175+/180.

---

**ROLE 1 — FORMAT ANALYST**

You are a format analyst reviewing this output contract before the technical analysis
begins. Your output is the PROSE-RESTRICTION DECLARATION below. The Domain Expert in
Role 2 is bound by this declaration and may not modify it.

Produce the declaration by filling every section. Do not produce any analysis content.

**PROSE-RESTRICTION DECLARATION (your output):**

Prose-permitted contexts (closed list — you must enumerate exactly three):
1. [Binding-tier causal reason — one paragraph at Phase 1B exit]
2. [Binding constraint exclusivity — one sentence at Phase 1B exit]
3. [Global criterion-coverage verdict notes — FAIL verdicts only]

Structured-output exemption class (enumerate all types that are NOT prose and therefore
exempt from C-23 inline citation requirements):
- Gate decision lines: PROCEED / BLOCKED
- Cross-artifact header lines: "One row per [source]. No [item] may be omitted."
- Phase boundary prohibition lines: "PROHIBITED: [data class]"
- Per-criterion verdict lines: "C-NN: PASS / FAIL"

**Escape route note for Format Analyst (C-25):** The temptation is to enumerate only
the prose-permitted contexts and leave structured output unclassified, reasoning that
"non-prose" is the complement of the prose-permitted list. This is insufficient: an
executor reading only a prose-permitted list must classify each element by content
inspection (is PROCEED a prose statement or a structured verdict?). The exemption class
removes content inspection from the classification process.

State "FORMAT CONTRACT COMPLETE" when both sections above are filled.

---

**ROLE 2 — DOMAIN EXPERT ANALYSIS**

You are a Connectors / Power Automate throughput domain expert. The FORMAT CONTRACT
produced by the Format Analyst above governs all output below. You are bound by the
prose-restriction declaration and may not introduce prose outside the three declared
contexts.

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection — C-13 requires the evidence base to be committed before any tier is named;
a source added after tier analysis cannot be verified as a prior commitment*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... verbatim downstream. Compliance failure condition:
  informal synonym fails T-NN threading.
- `Limit` — number + unit. Compliance failure condition: vague label fails precision.
- `Binding?` — exactly one Y. At-most-one binding constraint: designating a primary
  bottleneck without explaining why competing tiers do not bind first is an assertion,
  not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete*

**[prose: item 1 — binding-tier causal reason]** Why does the Binding? = Y tier fail
before all others at 1x nominal load?

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from failing before the binding tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built from an incomplete tier inventory are unverifiable*

For each tier in TABLE A — every downstream derived table must cover all TABLE A T-NNs.
— *prevents coverage elision; omission is detectable by T-NN count match against TABLE A*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs from TABLE A only.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: generic term fails precision requirement.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description in `Error code or signal` fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: risk list without Type column with named taxonomy and
per-type minimum-row constraint fails C-22 even if all categories happen to appear.

---

**TYPE SCAN GATE**

**Purpose — prevents category elision above C-22 (C-26):** C-22 requires the Type
column and per-type minimum rows. This gate checks type completeness before TABLE F
opens. The distinction matters because the failure modes for missing categories differ
at construction time vs. post-completion:

*Without the gate:* An executor completes TABLE F (all TABLE E rows have mitigation
entries), then a post-hoc scan detects the missing Cascade row in TABLE E. At that
point, TABLE F also has no Cascade mitigations — two artifacts are incomplete, and the
mitigation table must be revised in addition to the risk table.

*With the gate:* The missing Cascade row is detected before TABLE F opens. Only TABLE E
requires revision. TABLE F opens from a complete risk inventory.

**Escape route for C-26 — "C-22 makes this gate redundant":** The reasoning is that
C-22 already requires all three type categories, so the gate adds process without adding
substance. This is self-defeating: C-22 ensures the finished output has the correct
structure; the gate ensures the structure is correct before downstream construction
begins. An output that satisfies C-22 by inspection may have been produced through an
execution path where TABLE F was completed before the type gap was detected — the gate
forecloses that path.

Scan TABLE E:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: category of action in `Setting or API parameter` fails precision.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection after mitigation planning is underway*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Maps output content to essential criterion categories by name.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] FAIL rationale only.

---

---

## V-05 — Combined: Role Sequence + Lifecycle Emphasis + Inertia Framing

**Axes:** (1) Role sequence — three-role pipeline: Format Analyst produces the output
contract; Domain Expert produces evidence and claims; Consequence Analyst produces the
mitigation phase and global coverage step. Each role is barred from activating before
the prior role's gate is cleared. (2) Lifecycle emphasis — C-25 exemption class appears
as a named STRUCTURED OUTPUT REGISTER sub-section at the same structural level as the
prose-permitted list; C-26 Purpose annotation uses three labeled fields. (3) Inertia
framing — both C-25 and C-26 carry explicit escape-route naming with the specific
reasoning chain that leads to the failure mode, followed by a structural rebuttal.

**Hypothesis:** The three-role pipeline enforces phase ordering at the structural level
rather than via prohibitions — each role's output is the precondition for the next role's
activation, making out-of-order execution architecturally impossible rather than merely
discouraged. The STRUCTURED OUTPUT REGISTER sub-section signals parallel treatment with
the prose-permitted list and produces a more complete exemption class by requiring each
element type to appear as a table row. The three-field C-26 annotation and escape-route
framing jointly address both the form requirement (all three C-26 sub-requirements filled)
and the comprehension gap (the redundancy reasoning is demolished in place). This variation
is the strongest candidate for 180/180 because it addresses C-25 and C-26 from three
independent angles simultaneously.

**v9 predicted scoring:** C-25 PASS (STRUCTURED OUTPUT REGISTER with escape-route
framing, produced as a role output). C-26 PASS (three-field annotation + escape-route
rebuttal). All other criteria carry from R8 baseline. Predicted composite: 180/180.

---

**ROLE 1 — FORMAT ANALYST**

You are the Format Analyst. Your output is the complete OUTPUT FORMAT CONTRACT below.
The Domain Expert (Role 2) and Consequence Analyst (Role 3) are bound by this contract
and may not modify it. Produce the contract by filling every section, then state
"ROLE 1 COMPLETE" before Role 2 activates.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Enumerate each with its scope:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains why
   the Binding? = Y tier fails before all others. Authorized by: C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism that prevents at least one non-binding tier from failing first.
   Authorized by: C-14.
3. **Global criterion-coverage verdict notes** — at the global coverage step, FAIL
   verdicts only. Scope: one sentence per failed criterion explaining the gap.
   Authorized by: C-19.

Any prose passage outside these three contexts is a format violation detectable without
content review — the violation is an element appearing in narrative position that
matches none of the three declared scopes.

**Section B — STRUCTURED OUTPUT REGISTER (C-25)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

**Escape route for C-25:** The temptation is to omit this register on the grounds that
structured output is the complement of the prose-permitted list — anything not in Section A
is implicitly structured. This reasoning requires content inspection to classify boundary
elements: a gate verdict line (PROCEED) appears in a narrative position, and its
classification as structured vs. prose requires interpreting whether it constitutes an
affirmative statement or a blocking decision. The register removes content inspection
from the equation — classification is determined by element type before content is read.

ROLE 1 COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A
(prose-restriction declaration) and Section B (structured output register).

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

---

**PHASE 1 — EVIDENCE PHASE**

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after ROLE 1 COMPLETE is stated.

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. Every numeric threshold cited in Steps
1B and Phase 2 must have a Source-ID entry here. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source entered after claims are built cannot be verified as the basis for
the numeric claim it purports to support — it may be post-hoc attribution assembled to
satisfy C-11 rather than a pre-committed evidence source*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank cell and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance
  failure condition: an informal synonym in place of T-NN fails the tier-ID threading
  requirement and makes cross-section tracing a name-resolution task.
- `Limit` — a specific number with a unit (e.g., "1,200 req/min", "500 connections").
  Compliance failure condition: a vague label ("limited", "throttled") in place of a
  specific number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands. The reason:
  a tier that never transitions cannot be the primary bottleneck at any band.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries fail the
  at-most-one binding constraint; a designation without a causal reason is an assertion.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
evidence that Phase 1 enumeration was incomplete is not a fill-in opportunity — it
requires returning to Step 1B, completing the registry, and restarting Phase 2 from
the point of discovery*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N
tier, name the mechanism that prevents it from binding before the primary tier.

ROLE 2 PHASE 1 COMPLETE. Role 2 Phase 2 opens only after TABLE A is fully populated.

**Step 1B GATE:** Every TABLE A row has all columns filled with non-placeholder values.
No vague labels in the Limit column. PROHIBITED: opening Phase 2 before this gate is
cleared. — *prevents late evidence injection; a claims phase built on an incomplete
tier inventory produces unverifiable findings*

---

**PHASE 2 — CLAIMS PHASE**

**PHASE 2 ENTRY CONDITION:** Phase 2 opens only after the Step 1B GATE is cleared.
The tier registry is closed.

**Enumeration anchor — for each tier in TABLE A (C-17):** every downstream table that
derives from TABLE A must include a row for every T-NN. Coverage is verifiable by T-NN
count match against TABLE A, not by reading downstream content. — *prevents coverage
elision; a tier absent from a derived table produces a detectable T-NN count gap*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: a generic term ("blocked", "throttled")
in place of a named mechanism from the permitted set fails this column's precision
requirement.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: a plain description ("request fails", "throttle error") in
`Error code or signal` in place of a specific HTTP status code or platform signal
identifier fails this column's precision requirement.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no unprotected path exists, row 1 names ≥2
controls as evidence that every entry point is protected.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — a count requirement without type classification
can be satisfied by two rows of the same category, leaving an entire category undetected.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: a risk list without a Type column with a named taxonomy
and per-type minimum-row constraint fails C-22 even if all required categories happen
to appear, because the mechanism that makes category absence detectable is absent.

ROLE 2 PHASE 2 COMPLETE. The Consequence Analyst (Role 3) activates after the TYPE
SCAN GATE below is cleared.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E, making the entire risk category unmitigated, but
  the absence is detectable only by a full table scan after TABLE F is complete.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the finished TABLE E. This gate ensures type completeness is verified
  *before TABLE F opens*. C-22 is a finished-output structural requirement; this gate
  is a construction-time blocking check. An executor who reasons "C-22 already requires
  all three types — the gate adds no substance" is confusing a structural requirement
  with a construction-time enforcement mechanism. C-22 ensures what the output must
  contain; the gate ensures the missing-category failure mode cannot be produced by
  any valid execution path.
- **Audit test:** Gate present → verify PROCEED/BLOCKED verdict appears between TABLE E
  and TABLE F, and all three type-presence verdicts are explicitly stated. Gate absent
  → verify type completeness by scanning TABLE E after TABLE F is complete. The gate
  is the only mechanism that makes type completeness a construction-time blocking
  condition rather than a post-hoc scan result.

**Escape route for C-26 — "the gate Purpose is redundant because C-22 already explains
why type coverage is required":** This reasoning conflates the *structural requirement*
(C-22's Type column mandate) with the *construction-time enforcement mechanism* (the
gate). C-22 tells the executor what the finished output must contain. The gate tells
the executor when to verify it. An output can satisfy C-22 and fail the construction-
time check — the executor simply produces TABLE F first and discovers the gap afterward.
The Purpose annotation demolishes the redundancy reasoning by naming the specific
execution path the gate forecloses: the mitigation table cannot be opened against an
incomplete risk table.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**ROLE 3 — CONSEQUENCE ANALYST**

You are the Consequence Analyst. You activate only after PROCEED is stated at the TYPE
SCAN GATE. Your scope is TABLE F (mitigation registry) and the global criterion-coverage
step. You are bound by the OUTPUT FORMAT CONTRACT from Role 1.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: a category of action ("add retry logic") in `Setting or
API parameter` in place of a specific parameter identifier (e.g., `connector.retryPolicy`)
fails this column's precision requirement. A row naming a category cannot be applied
without further research; a row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning is evidence TABLE E was
incomplete; it requires returning to Role 2, completing TABLE E, re-running the TYPE
SCAN GATE, and re-opening TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL verdict.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and names specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with named mechanism): [TABLE B has ≥2 rows with T-NN identifiers from TABLE A and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component and Scope filled, each row with a specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID and no tier is omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason, or ≥1 row with ≥2 named controls as evidence of protection? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any criterion above that did not pass.

ROLE 3 COMPLETE.
