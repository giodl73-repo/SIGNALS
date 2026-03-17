## prove-synthesize — R7 Variations (V-01 through V-05)

Five complete, runnable variations. Single-axis first (V-01 through V-03), then combined (V-04), then maximum (V-05).

---

## V-01 — Role-Sequence Variation (Analyst → Skeptic → Synthesist)

**Variation axis**: Role sequence — three named internal roles deliberate before any output is written
**Hypothesis**: Role-ordered deliberation produces higher-quality synthesis than direct output by forcing explicit challenge before commitment

**Criteria prediction**: C-01–C-10 pass. C-11–C-28 not targeted (no structural phases, no violation names, no arrow-chain).

```
You are synthesizing a completed investigation. You have the hypothesis and all investigation
signal artifacts produced during the investigation.

Run these three internal roles in strict sequence before writing any output.

ROLE 1 — ANALYST
Read every investigation signal. For each signal, determine: does it support the hypothesis,
argue against it, or neither? Identify the three signals that most changed your view of the
answer. Rank them by influence, not by recency or length.

ROLE 2 — SKEPTIC
Challenge the Analyst's ranking. Ask: Is the top signal genuinely the strongest, or just the
most recent? Is there confirmation bias in the selection? Name the single strongest argument
*against* the Analyst's answer. Name it explicitly — do not soften or hedge it.

ROLE 3 — SYNTHESIST
Take the Analyst's ranking and the Skeptic's challenge. Issue a judgment. The Synthesist must
take a position — not hedge, not summarize. The synthesis supersedes every individual signal.

---

OUTPUT FORMAT

The first sentence is the answer. No preamble, no context-setting, no throat-clearing.

**ANSWER**: [One complete declarative sentence. Yes/No/Maybe with a direct claim attached.]

**CONFIDENCE**: [0–100]
[2–3 sentences: what drove the score up? What held it back?]

**KEY EVIDENCE**:
1. [Signal name] — [Why this signal influenced the answer more than the others. What specifically
   made it decisive, not just what it contains.]
2. [Signal name] — [Why this signal, not a different one. What it contributed.]
3. [Signal name] — [Why this signal made the top 3. Its specific role in the judgment.]

**COUNTER-EVIDENCE**:
[The strongest argument against the answer. Name the signal or finding. If no counter-evidence
exists, state "No counter-evidence found" and explain why that absence is itself meaningful or
a potential investigation gap.]

**PRINCIPLES EXTRACTED**:
[One or more declarative statements that generalize beyond this hypothesis. Format: "X implies
Y." Not a restatement of the finding. Something a future investigation could apply.]

**OPEN QUESTIONS**:
[One or more questions this investigation did not resolve. Specific and actionable — not "more
research needed." Name what specifically needs to be investigated next and why it matters to
the conclusion.]

---

SELF-CONTAINED MANDATE: This synthesis is the complete record of the investigation's
conclusion. A reader with no access to the underlying signals must be able to understand the
answer, the reasoning, and what to do next from this document alone. Write accordingly.
```

---

## V-02 — Output Format Variation (Tables + SURVEYOR + Arrow-Chain in RECORD DIAGNOSIS)

**Variation axis**: Output format + structural inventory — tables replace prose lists; SURVEYOR inventory phase and RECORD DIAGNOSIS with arrow-chain field:value notation introduced
**Hypothesis**: Structured tabular format combined with an explicit inventory step reduces evidence selection bias and improves rank argumentation

**Criteria prediction**: C-01–C-10 pass. C-24 (arrow-chain in RECORD DIAGNOSIS) added. C-23 (named violation categories at FRONTMATTER bounds) fails — fill instructions present but not violation-typed. C-25 (named PRE-FLIGHT) not present. C-26–C-28 not present.

```
You are synthesizing a completed investigation. You have the hypothesis and all investigation
signals.

FRONTMATTER — fill each field at the designated phase. Do not batch-fill at document open or
close. Do not fill ahead of the designated phase.

---
hypothesis: [fill now, before any phase work]
answer:      [fill at JUDGMENT phase only — not before]
confidence:  [fill at JUDGMENT phase only — not before]
key_evidence: [fill at JUDGMENT phase only — not before]
counter_evidence: [fill at JUDGMENT phase only — not before]
principles:  [fill at JUDGMENT phase only — not before]
open_questions: [fill at JUDGMENT phase only — not before]
---

---

PHASE 1 — SURVEYOR: SIGNAL INVENTORY

List every investigation signal in the table below.

| Signal ID | Name | Type | Addresses Hypothesis | Direction | Strength |
|-----------|------|------|----------------------|-----------|----------|
| S-01 | ... | ... | yes/partial/no | for/against/neutral | strong/moderate/weak |

Totals: For [N] · Against [N] · Neutral [N]

---

PHASE 2 — ADVERSARY: RECORD DIAGNOSIS

Select the 5 signals with highest influence on the answer. For each, produce an arrow-chain
using field:value notation:

  signal_id:signal_name → direction:[value] → strength:[value] → basis:[structural claim]

Example:
  S-03:prototype_validation → direction:for → strength:strong → basis:three_independent_sources_converged

Complete all 5 chains before continuing.

After the chains, identify the single failure mode most likely to invalidate this synthesis.
Be specific — name the exact vulnerability (e.g., "all three 'for' signals come from the same
source type, creating a single-source provenance risk").

---

PHASE 3 — JUDGMENT

Review the SURVEYOR table and the ADVERSARY arrow-chains. The confidence score must account
for the failure mode identified in Phase 2. Fill FRONTMATTER fields now.

---

SYNTHESIS BODY

State this first, before the answer: "This synthesis is self-contained and supersedes all
underlying investigation signals."

**ANSWER**: [Complete declarative sentence. Direct claim.]

**CONFIDENCE**: [0–100] — [Rationale. Reference the ADVERSARY arrow-chain result: which chains
were strong enough to elevate confidence? Which were weak enough to suppress it?]

**KEY EVIDENCE**:

| Rank | Signal | Why This Rank (Not the One Below) |
|------|--------|------------------------------------|
| 1 | [name] | [comparative: why rank 1 over rank 2 specifically] |
| 2 | [name] | [comparative: why rank 2 over rank 3 specifically] |
| 3 | [name] | [why included: what role relative to ranks 1 and 2] |

**COUNTER-EVIDENCE**:

| Signal | What It Argues | Weight Assigned | Reason for That Weight |
|--------|----------------|-----------------|------------------------|
| [name] | [argument]     | high/medium/low | [rationale]            |

If none: "No counter-evidence found. [Explain why the absence is meaningful or a gap.]"

**PRINCIPLES EXTRACTED**:
[Declarative. X implies Y. Generalizable beyond this investigation.]

**OPEN QUESTIONS**:
[Specific. Named. Actionable. What evidence would resolve each and why it matters.]
```

---

## V-03 — Lifecycle Emphasis Variation (Full Phased Pipeline + Inline Violation Names)

**Variation axis**: Lifecycle emphasis + inline violation categories — full named four-phase pipeline; FRONTMATTER bounds carry named violation types at each constraint
**Hypothesis**: Named failure-mode labels at field boundaries reduce premature and deferred completion errors more than unlabeled constraints

**Criteria prediction**: C-01–C-25 pass. C-26 (registry before FRONTMATTER) fails — no registry block present. C-27 (three-site arrow-chain) fails — JUDGE references ADVERSARY failure mode but not PRE-FLIGHT Phase B audit result; application site incomplete. C-28 (PRE-FLIGHT entry gate) fails — PRE-FLIGHT begins with Phase A steps directly, no preceding gate.

```
You are synthesizing a completed investigation into an authoritative answer document.
You have the hypothesis and all investigation signal artifacts.

FRONTMATTER — fill each field within its designated window. Named violations apply at each
bound.

---
hypothesis:       [fill at document open — NOT: defer past SURVEYOR — DEFERRED COMPLETION VIOLATION]
answer:           [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
confidence:       [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
key_evidence:     [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
counter_evidence: [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
principles:       [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
open_questions:   [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
---

---

PHASE 1 — SURVEYOR

Inventory every investigation signal. For each: signal ID, name, type, hypothesis relevance
(direct/indirect/none), direction (for/against/neutral), strength (strong/moderate/weak).

After completing the inventory, derive three structural record properties:
- Coverage: what aspects of the hypothesis have signals; what aspects are absent
- Convergence: whether signals point consistently or are scattered across directions
- Provenance: whether signal sources are diverse or concentrated in a single type

These properties are the traceable basis for ADVERSARY RECORD DIAGNOSIS. Do not proceed to
ADVERSARY until both the inventory table and the three properties are written.

---

PHASE 2 — ADVERSARY

RECORD DIAGNOSIS

For each of the top 5 signals (by strength), produce an arrow-chain using field:value notation:

  signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[claim]

Where [property] is one of: coverage | convergence | provenance

Example:
  S-05:interview_signal_2 → direction:for → strength:strong → derives_from:convergence::four_interviewees_named_same_pain_point

Complete all 5 chains. Then identify the record's primary failure mode:
- Name the failure mode
- Derive it explicitly from coverage, convergence, or provenance
- Name the specific signal or gap creating the exposure
- State what evidence would overturn the synthesis

---

PHASE 3 — PRE-FLIGHT

Phase A — EVIDENCE COUNT CHECK
Count signals by direction from SURVEYOR: for [N], against [N], neutral [N]. Verify totals
match the SURVEYOR inventory. Discrepancy: re-run SURVEYOR before continuing.

Phase B — SCHEMA-CITATION AUDIT
For each of the 5 ADVERSARY arrow-chains, verify: does the derives_from field cite one of the
three SURVEYOR structural properties (coverage, convergence, provenance)?
Mark each chain VERIFIED or UNVERIFIED.
Unverified chains must be corrected before Phase C.

Audit verdict: PASS (all verified) / PARTIAL (some unverified) / FAIL (majority unverified)

Phase C — FAILURE MODE REVIEW
Confirm the ADVERSARY failure mode derives from the structural properties, not from intuition.
If it cannot be traced to coverage, convergence, or provenance, revise it. Document the final
failure mode here.

---

PHASE 4 — JUDGE

FALSE ATTESTATION VIOLATION: stating a confidence score without having completed PRE-FLIGHT
Phase B SCHEMA-CITATION AUDIT.

DETERMINATION: [this word opens the commitment sentence — write the answer as a complete
declarative sentence immediately following this label]

Fill FRONTMATTER fields now.
NOT: leave any field empty at document close — DEFERRED COMPLETION VIOLATION.

---

SYNTHESIS BODY

First line: "This synthesis is self-contained and supersedes all underlying investigation
signals."

**ANSWER**: [Complete declarative sentence. First content after the opening mandate.]

**CONFIDENCE**: [0–100]
[2–3 sentences. Reference the ADVERSARY failure mode. State what held confidence below 100
or justified confidence above 75.]

**KEY EVIDENCE**:
1. [Signal name] — [Why this signal over the one below. Comparative argument, not description.]
2. [Signal name] — [Why this signal over the one below. Comparative argument.]
3. [Signal name] — [Role relative to ranks 1 and 2. Why it belongs in the top 3.]

**COUNTER-EVIDENCE**:
[Named signal or finding arguing against the answer. Weight assigned and why.]
If none: "No counter-evidence found." + rationale for absence.

**PRINCIPLES EXTRACTED**:
[X implies Y. One or more generalizable principles. Not a restatement of the finding.]

**OPEN QUESTIONS**:
[Specific. Named. Actionable. What evidence would resolve each.]
```

---

## V-04 — Combination: Lifecycle + Three-Site Arrow-Chain + PRE-FLIGHT Entry Gate

**Variation axis**: Lifecycle emphasis + phrasing register — adds PRE-FLIGHT entry gate naming PHASE-ADVANCE VIOLATION before phase steps (C-28); JUDGE explicitly applies arrow-chain from PRE-FLIGHT Phase B result, completing three-site traceability (C-27)
**Hypothesis**: Entry gate plus explicit three-site chain application together eliminate structural skip errors and false confidence attestations more completely than inline constraints alone

**Criteria prediction**: C-01–C-25 pass, C-27 and C-28 pass. C-26 (violation registry before FRONTMATTER) fails — violations named inline and at gate, but no named registry block precedes FRONTMATTER.

```
You are synthesizing a completed investigation into an authoritative answer document.
You have the hypothesis and all investigation signal artifacts.

FRONTMATTER — fill each field within its designated window. Named violations apply at each
bound.

---
hypothesis:       [fill at document open — NOT: defer past SURVEYOR — DEFERRED COMPLETION VIOLATION]
answer:           [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
confidence:       [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION;
                  FALSE ATTESTATION VIOLATION if PRE-FLIGHT Phase B is incomplete]
key_evidence:     [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
counter_evidence: [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
principles:       [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
open_questions:   [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
---

---

PHASE 1 — SURVEYOR

Inventory all investigation signals. For each: signal ID, name, type, hypothesis relevance
(direct/indirect/none), direction (for/against/neutral), strength (strong/moderate/weak).

After completing the inventory, derive three structural record properties:
- Coverage: what aspects of the hypothesis have signals; what aspects are absent
- Convergence: whether signals point consistently or are scattered across directions
- Provenance: whether signal sources are diverse or concentrated in a single type

Both the inventory table and the three structural properties must be present before ADVERSARY
begins. These properties are the traceable basis for RECORD DIAGNOSIS arrow-chains.

---

PHASE 2 — ADVERSARY

RECORD DIAGNOSIS

For each of the top 5 signals (by strength), produce an arrow-chain using field:value notation:

  signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[specific_claim]

Where [property] is one of: coverage | convergence | provenance

Complete all 5 chains before continuing.

Identify the record's primary failure mode:
- Name the failure mode
- Derive it from one or more structural properties (coverage, convergence, provenance)
- Name the specific signal or gap creating the exposure
- State what additional evidence would overturn the synthesis

---

PHASE 3 — PRE-FLIGHT

**PRE-FLIGHT ENTRY GATE**: Before reading Phase A, B, or C below — confirm that ADVERSARY
RECORD DIAGNOSIS is complete: all 5 arrow-chains written, failure mode named with structural
derivation. If ADVERSARY is incomplete, return to it now. Proceeding from ADVERSARY directly
to JUDGE without completing PRE-FLIGHT is a PHASE-ADVANCE VIOLATION.

Phase A — EVIDENCE COUNT CHECK
Count signals by direction from SURVEYOR: for [N], against [N], neutral [N]. Verify totals
match the SURVEYOR inventory. Discrepancy: re-run SURVEYOR before continuing.

Phase B — SCHEMA-CITATION AUDIT
For each of the 5 ADVERSARY arrow-chains, verify: does the derives_from field cite one of the
three SURVEYOR structural properties (coverage, convergence, provenance)?

| Chain | Signal ID | derives_from Cited | Property Match | Status |
|-------|-----------|--------------------|----------------|--------|
| 1 | ... | ... | coverage/convergence/provenance | VERIFIED/UNVERIFIED |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

Audit verdict: PASS (all verified) / PARTIAL (some unverified) / FAIL (majority unverified)

Unverified chains must be corrected before Phase C. Record the final audit verdict here for
use in JUDGE.

Phase C — FAILURE MODE REVIEW
Confirm the ADVERSARY failure mode is traceable to coverage, convergence, or provenance. If
it derives from intuition rather than the inventoried properties, revise it. Document the
final failure mode.

---

PHASE 4 — JUDGE

DETERMINATION: [this word opens the commitment sentence — write the answer as a complete
declarative sentence immediately following]

Apply the PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT result to the confidence score directly.
Per Phase B, the arrow-chain audit produced the following result: [cite the audit verdict and
the verified/unverified chain list]. The confidence score reflects this audit: a PASS audit
permits high confidence (≥75) if signal direction supports it; a PARTIAL audit caps confidence
at 70 unless explicitly mitigated; a FAIL audit caps confidence at 50.

FALSE ATTESTATION VIOLATION: stating a confidence score without having completed PRE-FLIGHT
Phase B SCHEMA-CITATION AUDIT and citing its result.

Fill FRONTMATTER fields now.
NOT: leave any field empty at document close — DEFERRED COMPLETION VIOLATION.

---

SYNTHESIS BODY

First line: "This synthesis is self-contained and supersedes all underlying investigation
signals. No access to underlying artifacts is required to understand the conclusion."

**ANSWER**: [Complete declarative sentence. First content after the opening mandate.]

**CONFIDENCE**: [0–100]
[2–3 sentences. Reference the PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT result explicitly:
"Phase B found [N] verified chains and [N] unverified (audit verdict: [value]). This
[elevated/suppressed/confirmed] confidence because [reason]."]

**KEY EVIDENCE**:
1. [Signal name] — [Why this signal over rank 2. Comparative argument: what makes it more
   decisive than the signal below it.]
2. [Signal name] — [Why this signal over rank 3. Comparative argument.]
3. [Signal name] — [Why included in the top 3. Its role relative to ranks 1 and 2.]

**COUNTER-EVIDENCE**:
[Named signal or finding arguing against the answer. Weight assigned (high/medium/low) and
rationale for that weight — not just what it argues but why the weight is proportionate.]
If none: "No counter-evidence found." + explanation of whether absence is expected or a gap.

**PRINCIPLES EXTRACTED**:
[X implies Y. Declarative. Generalizable to future investigations.]

**OPEN QUESTIONS**:
[Specific. Named. Actionable. For each: what evidence would resolve it and why it matters to
the conclusion.]
```

---

## V-05 — Full Combination: All v7 Criteria (Front-Indexed Registry + Three-Site + Entry Gate)

**Variation axis**: All axes — front-indexed violation taxonomy registry before FRONTMATTER (C-26), three-site arrow-chain traceability (C-27), PRE-FLIGHT entry gate (C-28), plus closure audit seeding potential R8 criteria
**Hypothesis**: Front-loading the complete violation taxonomy before the first fill window creates maximum protection against all four completion error types and makes the taxonomy addressable by reference throughout the document

**Criteria prediction**: C-01–C-28 all pass. Full 140.0 / 140.0 under v7. Closure audit (VIOLATION AUDIT CLOSE) seeds a potential R8 criterion requiring end-of-document violation confirmation.

```
VIOLATION TAXONOMY REGISTRY

All violation types that apply to this synthesis are indexed below. Each is referenced by
name at the structural point where its failure mode can occur.

| Violation Type | Trigger Condition |
|----------------|-------------------|
| PREMATURE COMPLETION VIOLATION | Filling a FRONTMATTER field before its designated structural phase begins |
| DEFERRED COMPLETION VIOLATION | Leaving a FRONTMATTER field unfilled after its designated structural phase closes |
| FALSE ATTESTATION VIOLATION | Stating a confidence score without completing PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT |
| PHASE-ADVANCE VIOLATION | Proceeding to a later named phase (PRE-FLIGHT, JUDGE) without completing all prior phases |

---

FRONTMATTER — fill each field within its designated window. Named violations from the
VIOLATION TAXONOMY REGISTRY apply at each bound.

---
hypothesis:       [fill at document open — NOT: defer past SURVEYOR — DEFERRED COMPLETION VIOLATION]
answer:           [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
confidence:       [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION;
                  FALSE ATTESTATION VIOLATION if PRE-FLIGHT Phase B incomplete]
key_evidence:     [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
counter_evidence: [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
principles:       [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
open_questions:   [fill at JUDGE — NOT: fill before JUDGE begins — PREMATURE COMPLETION VIOLATION]
---

---

PHASE 1 — SURVEYOR

Inventory all investigation signals. For each: signal ID, name, type, hypothesis relevance
(direct/indirect/none), direction (for/against/neutral), strength (strong/moderate/weak).

After completing the inventory, derive three structural record properties:
- Coverage: what aspects of the hypothesis have signals; what aspects are absent
- Convergence: whether signals point consistently or are scattered across directions
- Provenance: whether signal sources are diverse or concentrated in a single type

Both the inventory table and the three structural properties must be written before ADVERSARY
begins. These properties are the traceable basis for all RECORD DIAGNOSIS arrow-chain
derives_from fields. Do not proceed to ADVERSARY until both are complete.

---

PHASE 2 — ADVERSARY

RECORD DIAGNOSIS

For each of the top 5 signals (by strength), produce an arrow-chain using field:value notation:

  signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[specific_structural_claim]

Where [property] is one of: coverage | convergence | provenance

Example:
  S-04:interview_signal_3 → direction:for → strength:strong → derives_from:convergence::four_independent_interviewees_named_identical_pain_point

Complete all 5 chains before continuing.

Identify the record's primary failure mode:
- Name the failure mode (specific, not generic)
- Derive it explicitly from one or more structural properties (coverage, convergence, provenance)
- Name the specific signal or gap creating the exposure
- State what additional evidence would be sufficient to overturn the synthesis

---

PHASE 3 — PRE-FLIGHT

**PRE-FLIGHT ENTRY GATE**: Before reading Phase A, B, or C below — confirm that ADVERSARY
RECORD DIAGNOSIS is complete: all 5 arrow-chains written using field:value notation, failure
mode named with explicit structural derivation. If ADVERSARY is incomplete, return to it now.
Proceeding from ADVERSARY directly to JUDGE without completing PRE-FLIGHT is a PHASE-ADVANCE
VIOLATION. (Reference: VIOLATION TAXONOMY REGISTRY.)

Phase A — EVIDENCE COUNT CHECK
Count signals by direction from SURVEYOR: for [N], against [N], neutral [N]. Verify totals
match the SURVEYOR inventory. Discrepancy: re-run SURVEYOR before continuing.

Phase B — SCHEMA-CITATION AUDIT
Audit each ADVERSARY arrow-chain. For each chain, verify: does the derives_from field cite
one of the three SURVEYOR structural properties (coverage, convergence, provenance)?

| Chain | Signal ID:Name | derives_from Cited | Property Match | Status |
|-------|----------------|--------------------|----------------|--------|
| 1 | ... | ... | coverage/convergence/provenance | VERIFIED/UNVERIFIED |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

Audit verdict: PASS (all verified) / PARTIAL (some unverified) / FAIL (majority unverified)

Unverified chains must be corrected before Phase C. Record the final audit verdict and the
verified/unverified chain list here — JUDGE will cite this record directly.

Phase C — FAILURE MODE REVIEW
Confirm the ADVERSARY failure mode is traceable to coverage, convergence, or provenance. If
it derives from intuition rather than the inventoried properties, revise it. Document the
revised failure mode here.

---

PHASE 4 — JUDGE

DETERMINATION: [this word opens the commitment sentence — write the answer as a complete
declarative sentence immediately following this label]

Apply the PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT result to the confidence score. Per the
Phase B audit, the arrow-chain verification produced: [cite the audit verdict and the
verified/unverified chain list from Phase B]. The confidence score must reflect this result:
- PASS audit: high confidence (≥75) permitted if signal direction supports
- PARTIAL audit: confidence capped at 70 unless the unverified chains cover only weak signals
- FAIL audit: confidence capped at 50

FALSE ATTESTATION VIOLATION: stating a confidence score without citing the PRE-FLIGHT Phase B
audit verdict. (Reference: VIOLATION TAXONOMY REGISTRY.)

Fill FRONTMATTER fields now.
NOT: leave any field empty at document close — DEFERRED COMPLETION VIOLATION.
NOT: fill any JUDGE-designated field before this phase — PREMATURE COMPLETION VIOLATION.

---

SYNTHESIS BODY

First line: "This synthesis is self-contained and supersedes all underlying investigation
signals. No access to underlying signal artifacts is required to understand the answer, the
reasoning, or what to do next."

**ANSWER**: [Complete declarative sentence. First content after the opening mandate.]

**CONFIDENCE**: [0–100]
[2–3 sentences. Reference the PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT result explicitly:
"Phase B found [N] verified chains and [N] unverified chains (audit verdict: [value]). This
[elevated/suppressed/confirmed] confidence because [reason derived from the audit result]."]

**KEY EVIDENCE**:
1. [Signal name] — [Why this signal over rank 2. Comparative argument: what makes it more
   decisive than the signal immediately below it.]
2. [Signal name] — [Why this signal over rank 3. Comparative argument.]
3. [Signal name] — [Why included in the top 3 at all. Its specific role relative to ranks 1
   and 2.]

**COUNTER-EVIDENCE**:
[Named signal or finding arguing against the answer. Weight assigned (high/medium/low) and
rationale for that weight — why the weight is proportionate, not just what the signal argues.]
If none: "No counter-evidence found. [State whether the absence is expected given the
investigation scope or is itself a potential gap.]"

**PRINCIPLES EXTRACTED**:
[X implies Y. One or more declarative principles that generalize beyond this specific
hypothesis and would apply to future investigations of similar type.]

**OPEN QUESTIONS**:
[One or more specific, named questions this investigation did not resolve. For each: state
what evidence would resolve it and why it matters to the stated answer.]

---

VIOLATION AUDIT CLOSE

Before finalizing this document, confirm each of the following:
- [ ] PREMATURE COMPLETION VIOLATION: no FRONTMATTER field was filled before its designated phase
- [ ] DEFERRED COMPLETION VIOLATION: all FRONTMATTER fields are filled; no field is empty
- [ ] FALSE ATTESTATION VIOLATION: confidence score cites the PRE-FLIGHT Phase B audit verdict
- [ ] PHASE-ADVANCE VIOLATION: SURVEYOR, ADVERSARY, and PRE-FLIGHT phases were all completed
      before JUDGE began

If any check fails, correct the violation before marking the synthesis complete.
```

---

## Criteria Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-10 (Essential + Recommended + first Aspirational) | pass | pass | pass | pass | pass |
| C-11–C-22 (Prior-round Aspirational) | partial | + SURVEYOR/ADVERSARY progress | full | full | full |
| C-23 Inline violation names | — | — | pass | pass | pass |
| C-24 Arrow-chain in RECORD DIAGNOSIS | — | pass | pass | pass | pass |
| C-25 Named PRE-FLIGHT phase | — | — | pass | pass | pass |
| C-26 Registry before FRONTMATTER | — | — | — | — | **pass** |
| C-27 Three-site arrow-chain | — | — | — | **pass** | pass |
| C-28 PRE-FLIGHT entry gate | — | — | — | **pass** | pass |
| **Predicted score (v7)** | ~90 | ~100 | ~122.5 | ~130 | **140.0** |
