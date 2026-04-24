Here are the 5 complete variations for R8:

---

## V-01 — Role Sequence (Single axis: C-30)
**Hypothesis**: When each role names its own failure at definition, bypass is a role-identity contradiction.

Lean structure (no structural phases). Three roles in sequence — ANALYST, ADVERSARY, SYNTHESIST — each declaring what they risk:
- ANALYST: "selective collection — filtering by direction before inventory is complete"
- ADVERSARY: "generic challenge — claims that don't falsify against this inventory"
- SYNTHESIST: "hedging — qualifying a clear answer into maybe"

KEY EVIDENCE uses post-ranking comparative prose (C-09 pass, C-29 intentionally fail). **Predicted: ~112.5/147.5**

---

## V-02 — Output Format (Single axis: C-29)
**Hypothesis**: A named prose sub-item at each rank makes omission structurally visible — not a style choice.

Lean structure. KEY EVIDENCE uses per-rank blocks, each with a required `Why not the rank below:` labeled sub-item at rank 1, 2, and 3. This resolves the C-12/C-29 tension from R7 V-02 (which used a table column — C-29 pass, C-12 fail). No role-native failure mode ownership (C-30 intentionally fail). **Predicted: ~112.5/147.5**

---

## V-03 — Lifecycle Emphasis (Single axis: C-31)
**Hypothesis**: Requiring a count ("N of M top signals share source type") makes the adversarial challenge falsifiable against the inventory.

Built on R7 V-03 full pipeline (SURVEYOR + arrow-chain + PRE-FLIGHT). ADVERSARY phase expanded with explicit pattern-of-N analysis: after completing 5 arrow-chains, must state source-type count, direction-concentration count, and cross-type confirmation. Failure mode must be derived from the distribution. No role-native failure modes (C-30 intentionally fail). **Predicted: ~135/147.5**

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis (C-30 + C-31)
**Hypothesis**: ADVERSARY's self-declared failure mode is "generic challenge" — and pattern-of-N enforces the non-generic alternative. The role's stated risk and the structural requirement close the same gap from two directions.

R7 V-05 full baseline. Every phase names its own failure (SURVEYOR → selective inventory, ADVERSARY → generic challenge, JUDGE → hedging). ADVERSARY adds pattern-of-N with counts. C-29 borderline (comparative embedded in per-rank prose, not a separate named sub-item). **Predicted: ~142.5/147.5**

---

## V-05 — Full Combination (C-29 + C-30 + C-31)
**Hypothesis**: All three new criteria are mutually reinforcing and fail or pass together in a well-designed synthesis.

R7 V-05 baseline + all three v8 axes:
- **C-30**: every phase (SURVEYOR, ADVERSARY, JUDGE) names its own failure mode at definition
- **C-31**: ADVERSARY must state N-of-M counts before failure mode derivation
- **C-29**: KEY EVIDENCE uses `Why not the rank below:` as a required structural sub-item at each of 3 rank entries (VIO-5 added to taxonomy for rank-skip)

C-12/C-29 tension resolved unambiguously via labeled prose sub-items. **Predicted: 147.5/147.5 (maximum)**

---

The file is at `simulations/quest/variations/prove-synthesize-variations-R8-2026-03-14.md`. The key structural innovation in V-05 is `VIO-5: RANK-SKIP VIOLATION` — adding a named violation for missing the "Why not the rank below:" sub-item, which makes C-29 enforcement parallel to how C-23/C-26 enforced fill-window compliance in prior rounds.
 before listing every signal from the investigation input,
regardless of direction.

For each signal, record: signal ID, source type, one-sentence claim, direction
(SUPPORTS / OPPOSES / NEUTRAL).

---

ROLE 2 — ADVERSARY

What ADVERSARY does: examines the ANALYST inventory for structural vulnerabilities.
Identifies the failure mode most likely to invalidate the synthesis given the specific
composition of this evidence set. ADVERSARY cannot advocate for any answer.
ADVERSARY cannot introduce signals not in the ANALYST inventory.

ADVERSARY failure mode (own this): generic challenge — naming weaknesses that apply
identically to any synthesis (e.g., "sample may be small," "more data needed") rather
than failures derived from this inventory's specific distribution. If ADVERSARY's
challenge would apply equally to a different evidence set with different signals,
ADVERSARY has failed at ADVERSARY's task. The test: can the challenge be verified or
falsified against ANALYST's inventory entries? If not, revise it.

Name the structural property of this specific inventory that creates exposure: source
type concentration, direction convergence without cross-type confirmation, provenance
overlap, or coverage gap over a key hypothesis dimension.

---

ROLE 3 — SYNTHESIST

What SYNTHESIST does: reads the ANALYST inventory and the ADVERSARY challenge; issues
a verdict. Takes a position.

SYNTHESIST failure mode (own this): hedging — qualifying the answer into "maybe with
caveats" when the evidence and the adversarial challenge together support a clear answer.
If SYNTHESIST cannot distinguish between a genuine uncertainty and an uncomfortable
certainty, SYNTHESIST has failed at SYNTHESIST's task. The synthesis supersedes every
individual signal — it does not summarize them.

NOT: confidence >= 70 with the adversarial challenge addressed produces a MAYBE answer.
NOT: output that restates what each signal said instead of taking a position.

---

OUTPUT FORMAT

The first element is the answer. No preamble, no context-setting, no throat-clearing.

**ANSWER**: [YES / NO / MAYBE] — [one complete declarative sentence. This is the
position of record. It does not restate the hypothesis as a question.]

**CONFIDENCE**: [0–100]
[2–3 sentences: what drove the score up? What held it back? Address the ADVERSARY
challenge by name.]

**KEY EVIDENCE** (exactly 3, prose argument slots — NOT a table):
1. [Signal ID + name] — [Why this signal influenced the answer. One or more sentences
   of argument — not description of what the signal contains.]
2. [Signal ID + name] — [Why this signal, and not a different one.]
3. [Signal ID + name] — [Its specific role in the judgment.]

Why these signals over others: [comparative argument — explain why this ordered set
of three, not alternatives. What property makes rank 1 more decisive than rank 2?
What places rank 2 above rank 3? State the ranking rationale explicitly.]

**COUNTER-EVIDENCE**:
[Named signal or finding arguing against the answer. If none: "No counter-evidence
found — [explain whether absence is expected or a gap in the investigation]."]

**PRINCIPLES EXTRACTED**:
[X implies Y. One or more generalizable statements that apply beyond this hypothesis
to future investigations of similar type.]

**OPEN QUESTIONS**:
[Specific and actionable. Not "more research needed." Name what specifically needs
investigating and why it matters to the stated answer.]
```

---

## V-02 — Output Format: Per-Rank Comparative Slot (C-12/C-29 Resolved)

**Variation axis**: Output format — each KEY EVIDENCE rank position has a structurally required labeled sub-item asking "why this rank, not the one below," implemented as prose (not table), resolving the C-12/C-29 tension that existed in R7 V-02.
**Hypothesis**: A named prose sub-item at each rank entry — structurally required, not instructed — makes rank omission visible as a structural gap rather than a prose style choice. The per-rank slot forces comparative reasoning at assignment time, not as an afterthought.

**Criteria targeted (v8 new)**: C-29 only, via labeled prose sub-items at each rank (C-12 compatible). C-30 intentionally not satisfied (no role-native failure mode ownership). C-31 intentionally not satisfied (no pattern-of-N count). Single-axis isolation.

```
You are synthesizing a completed investigation. You have the hypothesis and all
investigation signal artifacts.

This synthesis is self-contained and supersedes all underlying investigation signals.
A reader with no access to the investigation artifacts must be able to understand the
answer, the reasoning, and what to do next from this document alone. Write accordingly.

---

Run these three roles in sequence before writing output.

ROLE 1 — ANALYST
Read every signal. For each: signal ID, source type, one-sentence claim, direction
(SUPPORTS / OPPOSES / NEUTRAL). Identify the signals most relevant to the hypothesis
answer. Do not rank yet. Complete the full inventory before proceeding.

ROLE 2 — ADVERSARY
Examine the ANALYST inventory for structural vulnerabilities. Identify the single failure
mode most likely to invalidate the synthesis. Be specific — name the exact vulnerability
(e.g., "all three top signals come from the same source type, creating provenance
concentration"). This challenge precedes the verdict; the verdict must account for it.
ADVERSARY cannot advocate for any answer.

ROLE 3 — SYNTHESIST
Take the ANALYST inventory and the ADVERSARY challenge. Issue a judgment. The synthesis
supersedes every individual signal — it does not summarize them.

---

OUTPUT FORMAT

**ANSWER**: [YES / NO / MAYBE] — [complete declarative sentence]

**CONFIDENCE**: [0–100]
[2–3 sentences: what drove the score up? What held it back?]

**KEY EVIDENCE**

Exactly 3 entries. Each entry is a prose argument block. NOT: table format for this
section. The "Why not the rank below:" sub-item is required at every rank position;
its absence at any rank is a structural gap.

**Rank 1 — [Signal ID + name]**
Claim: [What this signal asserts, one sentence]
Bearing: [Why this signal influenced the answer — argument, not description]
Why not the rank below: [The specific property that makes this signal more decisive
than rank 2. Name the property. Do not use comparative prose that covers all three
entries — answer this at rank 1 specifically.]

**Rank 2 — [Signal ID + name]**
Claim: [What this signal asserts]
Bearing: [Why this influenced the answer]
Why not the rank below: [The specific property separating rank 2 from rank 3.
What does rank 2 have that rank 3 lacks, or lacks that rank 3 has, for this verdict?]

**Rank 3 — [Signal ID + name]**
Claim: [What this signal asserts]
Bearing: [Why this influenced the answer]
Why not the rank below: [Why rank 3 belongs in the top 3 over any candidate at rank 4.
If only 3 signals exist, state: "No rank 4 candidate — this signal is included on merit,
not by elimination."]

**COUNTER-EVIDENCE**:
[Named signal or finding arguing against the answer. If none: "No counter-evidence
found — [rationale]."]

**PRINCIPLES EXTRACTED**:
[X implies Y. Generalizable beyond this hypothesis.]

**OPEN QUESTIONS**:
[Specific and actionable. What evidence would resolve each and why it matters to the
stated answer.]
```

---

## V-03 — Lifecycle Emphasis: Pattern-of-N Adversarial Input

**Variation axis**: Lifecycle emphasis — the ADVERSARY phase receives explicit pattern-of-N treatment: the challenge must be derived from the aggregate distribution of the signal inventory (N-of-M count required), not from any single signal's properties.
**Hypothesis**: Requiring the adversary to state counts forces examination of the inventory as a whole. "N of M top signals share the same source type" is falsifiable against the inventory; "the evidence may be biased" is not. The count makes the difference between a real structural challenge and a generic placeholder.

**Criteria targeted (v8 new)**: C-31 only. C-29 intentionally not satisfied (comparative language embedded in each rank entry — borderline, not a structurally separate sub-item). C-30 intentionally not satisfied (no role-native failure mode ownership). Single-axis isolation. Built on R7 V-03 full pipeline baseline.

```
You are synthesizing a completed investigation into an authoritative answer document.
You have the hypothesis and all investigation signal artifacts.

FRONTMATTER — fill each field at the designated phase only. Named violations apply.

---
hypothesis:       [fill now — NOT: defer past SURVEYOR — DEFERRED COMPLETION VIOLATION]
answer:           [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
confidence:       [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
key_evidence:     [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
counter_evidence: [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
principles:       [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
open_questions:   [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
---

---

PHASE 1 — SURVEYOR

Inventory every investigation signal. For each: signal ID, name, source type, hypothesis
relevance (direct / indirect / none), direction (for / against / neutral), strength
(strong / moderate / weak).

After the inventory, derive three structural record properties:
- Coverage: which hypothesis dimensions have signals; which are absent
- Convergence: whether signals point consistently or are scattered in direction
- Provenance: whether source types are diverse or concentrated in a single type

Do not proceed to ADVERSARY until both the inventory table and the three structural
properties are written.

---

PHASE 2 — ADVERSARY

RECORD DIAGNOSIS

For each of the top 5 signals (by strength), produce an arrow-chain:

  signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[claim]

Where [property] is one of: coverage | convergence | provenance

Complete all 5 chains before the pattern analysis below.

Pattern-of-N analysis (required — C-31 prerequisite to valid failure mode):

After completing the 5 chains, count the following and state the counts explicitly:

  Source type distribution: N of 5 top signals share the same source type — [state N]
  Direction concentration: N of 5 top signals point in the same direction — [state N]
  Cross-type confirmation: signals from at least 2 different source types agree on
    direction? YES / NO

NOT: derive the failure mode without stating these counts. NOT: challenge that does not
name a distribution property visible only by examining the signal inventory as a whole.

Derive the failure mode from the distribution pattern:
  Pattern: [N] of [M] top signals [property — e.g., share source type / all support /
    lack cross-type confirmation]
  Vulnerability: [what this distribution means for the answer's credibility]
  Challenge: [the specific failure mode this pattern could produce — not generic]

The challenge is falsifiable: it names a count, it names a pattern, and both can be
verified against the SURVEYOR inventory.

---

PHASE 3 — PRE-FLIGHT

Phase A — EVIDENCE COUNT CHECK
Count signals by direction from SURVEYOR: for [N], against [N], neutral [N]. Verify
totals match the SURVEYOR inventory. Discrepancy: re-run SURVEYOR.

Phase B — SCHEMA-CITATION AUDIT
For each of the 5 ADVERSARY arrow-chains, verify that the derives_from field cites one
of the three SURVEYOR structural properties (coverage, convergence, provenance). Mark
each chain VERIFIED or UNVERIFIED.
Audit verdict: PASS (all verified) / PARTIAL (some unverified) / FAIL (majority unverified).
Unverified chains must be corrected before Phase C.

Phase C — PATTERN COUNT VERIFICATION
Confirm the Pattern-of-N analysis states explicit counts (N of M). If counts are absent
or stated without cross-reference to the inventory, return to ADVERSARY.

---

PHASE 4 — JUDGE

DETERMINATION: [this word opens the commitment sentence]

Apply the PRE-FLIGHT Phase B audit result to the confidence score. Per Phase B:
[cite the audit verdict and chain list]. Confidence must reflect this audit:
- PASS: high confidence (>=75) permitted if signal direction supports
- PARTIAL: confidence capped at 70
- FAIL: confidence capped at 50

FALSE ATTESTATION VIOLATION: stating confidence without citing PRE-FLIGHT Phase B
audit verdict.

Fill FRONTMATTER fields now.
NOT: leave any field empty at document close — DEFERRED COMPLETION VIOLATION.

---

SYNTHESIS BODY

First line: "This synthesis is self-contained and supersedes all underlying investigation
signals."

**ANSWER**: [Complete declarative sentence.]

**CONFIDENCE**: [0–100]
[2–3 sentences. Reference the PRE-FLIGHT Phase B audit result and the Pattern-of-N
finding: "The distribution shows [N] of [M] top signals [pattern property], which
[elevated/suppressed/confirmed] confidence because [structural reason]."]

**KEY EVIDENCE**:
1. [Signal name] — [Why this signal over the one below it. Comparative argument: what
   specific property makes it more decisive than rank 2.]
2. [Signal name] — [Why this signal over rank 3. Comparative argument.]
3. [Signal name] — [Why included in the top 3. Its specific role relative to ranks 1-2.]

**COUNTER-EVIDENCE**:
[Named signal arguing against. Weight assigned and rationale.]
If none: "No counter-evidence found. [Rationale for absence.]"

**PRINCIPLES EXTRACTED**:
[X implies Y. Declarative. Generalizable.]

**OPEN QUESTIONS**:
[Specific. Named. What evidence would resolve each.]
```

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis (C-30 + C-31)

**Variation axis**: Role sequence + lifecycle emphasis — each cognitive role names its own failure mode at role definition (C-30), AND the adversary derives its challenge from aggregate signal distribution with count stated (C-31). Built on the R7 V-05 full structural baseline.
**Hypothesis**: Pairing role-native failure mode ownership with pattern-of-N adversarial input creates a closed loop: ADVERSARY's self-declared failure mode is "generic challenge," and the pattern-of-N requirement forecloses that failure by forcing structural evidence distribution analysis. The role defines what it must not do; the structural requirement makes compliance verifiable.

**Criteria targeted (v8 new)**: C-30 + C-31. C-29 not specifically targeted (per-rank comparative language embedded in KEY EVIDENCE prose — may borderline pass; full unambiguous resolution deferred to V-05). Combination of V-01 and V-03 axes on the R7 V-05 baseline.

```
VIOLATION TAXONOMY REGISTRY

All violation types in effect for this synthesis, indexed before any fill window.
(Reference this registry at every violation invocation.)

| Violation | Trigger |
|-----------|---------|
| PREMATURE COMPLETION VIOLATION | FRONTMATTER field filled before its designated phase |
| DEFERRED COMPLETION VIOLATION | FRONTMATTER field not filled after its designated phase |
| PHASE-ADVANCE VIOLATION | Downstream phase entered before upstream phase completes |
| FALSE ATTESTATION VIOLATION | JUDGE issues confidence without citing PRE-FLIGHT Phase B verdict |

---

FRONTMATTER — fill each field at its designated phase. Named violations apply at each
bound. (Reference: VIOLATION TAXONOMY REGISTRY.)

---
hypothesis:       [fill at document open — NOT: defer past SURVEYOR — DEFERRED COMPLETION VIOLATION]
answer:           [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
confidence:       [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION;
                  FALSE ATTESTATION VIOLATION if PRE-FLIGHT Phase B incomplete]
key_evidence:     [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
counter_evidence: [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
principles:       [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
open_questions:   [fill at JUDGE — NOT: fill before JUDGE — PREMATURE COMPLETION VIOLATION]
---

---

PHASE 1 — SURVEYOR

SURVEYOR cannot judge, rank, or conclude. SURVEYOR cannot select signals by direction.

SURVEYOR failure mode (own this): selective inventory — populating the signal list from
signals aligned with the expected answer while leaving opposing signals unrecorded. A
SURVEYOR inventory that lacks any OPPOSES or NEUTRAL signals when the investigation
produced them has failed as SURVEYOR.

Inventory all investigation signals. For each: signal ID, name, source type, hypothesis
relevance (direct / indirect / none), direction (for / against / neutral), strength
(strong / moderate / weak).

After the inventory, derive three structural record properties:
- Coverage: which hypothesis dimensions have signals; which are absent
- Convergence: whether signals point consistently or are scattered in direction
- Provenance: whether source types are diverse or concentrated

Do not proceed to ADVERSARY until both the inventory table and the three structural
properties are written.

---

PHASE 2 — ADVERSARY

ADVERSARY cannot advocate for any answer. ADVERSARY cannot introduce signals not in the
SURVEYOR inventory.

ADVERSARY failure mode (own this): generic challenge — issuing a structural-sounding
objection that applies identically to any synthesis regardless of evidence composition
(e.g., "more signals needed," "sample may be biased"). If the challenge cannot be
verified or falsified against specific SURVEYOR inventory entries, ADVERSARY has failed
as ADVERSARY. The test: does the challenge name a count, a distribution property, or a
specific signal gap that is only visible by examining this inventory?

RECORD DIAGNOSIS (chain of custody site 1):

For each of the top 5 signals (by strength), arrow-chain in field:value notation:

  signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[claim]

Where [property] is one of: coverage | convergence | provenance. Complete all 5 chains.

Pattern-of-N analysis (required before failure mode can be stated):

  Source type: N of 5 top signals share the same source type — state [N] explicitly
  Direction: N of 5 top signals point in the same direction — state [N] explicitly
  Cross-type confirmation: do at least 2 different source types agree on direction? YES / NO

Derive the adversarial challenge from the distribution, not from any single signal:
  Pattern: [N] of [M] top signals [distribution property]
  Vulnerability: [what this means for the synthesis's credibility]
  Challenge: [the specific failure mode this pattern produces — not generic]

---

PHASE 3 — PRE-FLIGHT

**PRE-FLIGHT ENTRY GATE**: Confirm ADVERSARY RECORD DIAGNOSIS is complete — all 5
arrow-chains written, Pattern-of-N counts stated, failure mode named with distribution
derivation — before reading Phase A, B, or C. NOT: proceed from ADVERSARY to JUDGE
without completing PRE-FLIGHT — PHASE-ADVANCE VIOLATION. (Reference: VIOLATION
TAXONOMY REGISTRY.)

Phase A — EVIDENCE COUNT CHECK
Direction totals from SURVEYOR: for [N], against [N], neutral [N]. Verify against
SURVEYOR inventory. Discrepancy: re-run SURVEYOR.

Phase B — SCHEMA-CITATION AUDIT (chain of custody site 2):
Audit each ADVERSARY arrow-chain: does derives_from cite one of the three SURVEYOR
structural properties?

| Chain | Signal ID:Name | derives_from | Property Match | Status |
|-------|----------------|--------------|----------------|--------|
| 1 | ... | ... | coverage/convergence/provenance | VERIFIED/UNVERIFIED |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

Audit verdict: PASS / PARTIAL / FAIL
Fill `preflight_verdict` (used by JUDGE). Unverified chains corrected before Phase C.

Phase C — PATTERN VERIFICATION
Confirm Pattern-of-N counts are stated and cross-referenceable to SURVEYOR inventory.

---

PHASE 4 — JUDGE

JUDGE cannot introduce new evidence. JUDGE cannot reopen the SURVEYOR inventory. JUDGE
reads the ADVERSARY RECORD DIAGNOSIS as audited by PRE-FLIGHT Phase B.

JUDGE failure mode (own this): hedging — issuing a qualified "maybe with caveats" when
the audited chain and the adversarial challenge together support a definite answer.
NOT: confidence >= 70 with adversarial challenge addressed produces a MAYBE verdict —
FALSE ATTESTATION VIOLATION. A JUDGE that hedges when the chain is clean has failed as
JUDGE.

DETERMINATION: [this word opens the commitment sentence — the complete declarative
answer appears immediately after this label]

Confidence paragraph (chain of custody site 3):
"Per PRE-FLIGHT Phase B, the arrow-chain audit verdict is [cite `preflight_verdict`
from Phase B, with chain list]. The Pattern-of-N analysis found [N] of [M] top signals
[distribution property], [with / without] cross-type confirmation. This produces
confidence [score] because [structural reason]. Confidence cap applied: [PASS/PARTIAL/FAIL
— PASS permits >=75; PARTIAL caps at 70; FAIL caps at 50]." NOT: confidence paragraph
that does not name `preflight_verdict` — FALSE ATTESTATION VIOLATION. (Reference:
VIOLATION TAXONOMY REGISTRY.)

Fill FRONTMATTER fields now.
NOT: leave any field empty at document close — DEFERRED COMPLETION VIOLATION.
NOT: fill any JUDGE-designated field before this phase — PREMATURE COMPLETION VIOLATION.

---

SYNTHESIS BODY

First line: "This synthesis is self-contained and supersedes all underlying investigation
signals. No access to underlying artifacts is required to understand the answer, the
reasoning, or what to do next."

**ANSWER**: [Complete declarative sentence. First content after the opening mandate.]

**CONFIDENCE**: [0–100]
[2–3 sentences. Cite PRE-FLIGHT Phase B verdict and Pattern-of-N finding explicitly.]

**KEY EVIDENCE** (exactly 3, prose argument slots — NOT a table):
1. [Signal name] — [Why this signal over rank 2. Comparative argument: what makes this
   signal more decisive than the one immediately below.]
2. [Signal name] — [Why rank 2 over rank 3. Comparative argument.]
3. [Signal name] — [Why included in the top 3. Its role relative to ranks 1 and 2.]

**COUNTER-EVIDENCE**:
[Named signal arguing against the answer. Weight (high/medium/low) and rationale for
that weight.]
If none: "No counter-evidence found. [State whether absence is expected or a gap.]"

**PRINCIPLES EXTRACTED**:
[X implies Y. Declarative. Generalizable to future investigations.]

**OPEN QUESTIONS**:
[Specific. Named. For each: what evidence would resolve it and why it matters.]

---

VIOLATION AUDIT CLOSE
- [ ] No PREMATURE COMPLETION VIOLATION: no FRONTMATTER field filled before its phase
- [ ] No DEFERRED COMPLETION VIOLATION: all FRONTMATTER fields filled
- [ ] No FALSE ATTESTATION VIOLATION: JUDGE confidence names `preflight_verdict`
- [ ] No PHASE-ADVANCE VIOLATION: PRE-FLIGHT completed before JUDGE
```

---

## V-05 — Full Combination: All v8 Criteria (C-29 + C-30 + C-31)

**Variation axis**: Role sequence + output format + lifecycle emphasis — all three new v8 criteria added to the R7 V-05 full structural baseline. Role-native failure mode ownership at every phase (C-30); per-rank labeled prose sub-items for comparative reasoning (C-29, C-12 compatible); pattern-of-N adversarial challenge with count (C-31).
**Hypothesis**: C-29, C-30, and C-31 are mutually reinforcing: role-native failure mode ownership forecloses ADVERSARY from issuing generic challenges (its stated risk), the pattern-of-N requirement structurally enforces the non-generic alternative, and per-rank prose slots force comparative reasoning at assignment time rather than as post-hoc reflection. All three criteria fail together or pass together in a well-designed synthesis.

**Criteria targeted (v8 new)**: C-29 + C-30 + C-31. Built on R7 V-05 full structural baseline (all 20 v7 criteria). Target score: 147.5/147.5.

```
VIOLATION TAXONOMY REGISTRY

All violation types in effect for this synthesis. Indexed here before any fill window
is encountered. (Reference this registry at every violation invocation.)

| ID | Violation | Trigger |
|----|-----------|---------|
| VIO-1 | PREMATURE COMPLETION VIOLATION | FRONTMATTER field filled before its designated phase |
| VIO-2 | DEFERRED COMPLETION VIOLATION | FRONTMATTER field not filled after its designated phase |
| VIO-3 | PHASE-ADVANCE VIOLATION | Downstream phase entered before upstream phase completes |
| VIO-4 | FALSE ATTESTATION VIOLATION | JUDGE issues confidence without citing PRE-FLIGHT Phase B verdict by name |
| VIO-5 | RANK-SKIP VIOLATION | KEY EVIDENCE rank entry missing its required "Why not the rank below:" sub-item |

---

FRONTMATTER — fill each field at its designated phase only. Named violations from the
VIOLATION TAXONOMY REGISTRY apply at each bound.

---
hypothesis:       [fill at document open — NOT: defer past SURVEYOR — VIO-2]
answer:           [fill at JUDGE — NOT: fill before JUDGE begins — VIO-1]
confidence:       [fill at JUDGE — NOT: fill before JUDGE begins — VIO-1;
                  NOT: fill without PRE-FLIGHT Phase B verdict — VIO-4]
key_evidence:     [fill at JUDGE — NOT: fill before JUDGE begins — VIO-1]
counter_evidence: [fill at JUDGE — NOT: fill before JUDGE begins — VIO-1]
principles:       [fill at JUDGE — NOT: fill before JUDGE begins — VIO-1]
open_questions:   [fill at JUDGE — NOT: fill before JUDGE begins — VIO-1]
---

---

PHASE 1 — SURVEYOR

SURVEYOR cannot rank, judge, or reach conclusions about hypothesis truth. SURVEYOR
cannot exclude signals based on direction.

SURVEYOR failure mode (own this): selective inventory — filtering signals by direction
or plausibility before recording them, producing an inventory that confirms rather than
represents. An inventory with no OPPOSES or NEUTRAL signals when the investigation
produced them is a SURVEYOR failure, not a clean finding. Every signal in the
investigation input appears in the SURVEYOR table, regardless of direction.

Inventory all investigation signals. For each: signal ID, name, source type, hypothesis
relevance (direct / indirect / none), direction (for / against / neutral), strength
(strong / moderate / weak).

After the inventory, derive three structural record properties:
- Coverage: which hypothesis dimensions have signals; which are absent
- Convergence: whether signals point consistently or are scattered in direction
- Provenance: whether source types are diverse or concentrated in a single type

Do not proceed to ADVERSARY until the inventory table and all three structural
properties are written.

---

PHASE 2 — ADVERSARY

ADVERSARY cannot advocate for any answer. ADVERSARY cannot introduce signals not in the
SURVEYOR inventory. ADVERSARY cannot conclude.

ADVERSARY failure mode (own this): generic challenge — issuing objections applicable to
any synthesis regardless of evidence composition (e.g., "sample may be small," "evidence
is incomplete," "more research needed"). An ADVERSARY whose challenge would apply
identically to a completely different evidence set has failed as ADVERSARY. The
verification test: can this challenge be confirmed or refuted against specific SURVEYOR
inventory entries with counts? If no, the challenge is generic and must be revised.

RECORD DIAGNOSIS (chain of custody site 1):

For each of the top 5 signals (by strength), arrow-chain in field:value notation:

  signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[specific_structural_claim]

Where [property] is one of: coverage | convergence | provenance

Example:
  S-04:beta_user_interviews → direction:for → strength:strong →
  derives_from:convergence::seven_independent_users_named_same_workflow_gap

Complete all 5 chains. Label this block: ADVERSARY ARROW CHAIN.

Pattern-of-N distribution analysis (required before failure mode derivation):

After completing the 5 chains, state the following counts against the SURVEYOR inventory:

  Source type: [N] of 5 top signals share the same source type — state N
  Direction: [N] of 5 top signals point in the same direction — state N
  Cross-type confirmation: at least 2 different source types agree on direction? YES / NO

NOT: proceed to failure mode derivation without stating these counts. NOT: failure mode
that names a distribution property without the count being cross-referenceable to the
ADVERSARY ARROW CHAIN entries.

Derive the adversarial challenge from the distribution, not from any single signal:
  Pattern: [N] of [M] top signals [distribution property — e.g., share source type /
    all point same direction / lack cross-type confirmation]
  Vulnerability: [what this distribution means for the synthesis's credibility]
  Challenge: [the specific failure mode this pattern produces in a synthesis that
    ignores it — not generic, not applicable to any other evidence set]

---

PHASE 3 — PRE-FLIGHT

**PRE-FLIGHT ENTRY GATE**: Before reading Phase A, B, or C — confirm that ADVERSARY
RECORD DIAGNOSIS is complete: all 5 arrow-chains written in field:value notation;
Pattern-of-N counts stated with cross-reference to ADVERSARY ARROW CHAIN; failure mode
derived from distribution, not from a single signal. NOT: proceed from ADVERSARY to
JUDGE without completing PRE-FLIGHT — PHASE-ADVANCE VIOLATION (VIO-3). (Reference:
VIOLATION TAXONOMY REGISTRY.)

Phase A — EVIDENCE COUNT CHECK
Direction totals from SURVEYOR: for [N], against [N], neutral [N]. Verify totals match
the SURVEYOR inventory. Discrepancy: re-run SURVEYOR before continuing.

Phase B — SCHEMA-CITATION AUDIT (chain of custody site 2):
Audit every chain in ADVERSARY ARROW CHAIN. For each chain, verify: does derives_from
cite one of the three SURVEYOR structural properties (coverage, convergence, provenance)?

| Chain | Signal ID:Name | derives_from Cited | Property Match | Status |
|-------|----------------|--------------------|----------------|--------|
| 1 | ... | ... | coverage/convergence/provenance | VERIFIED/UNVERIFIED |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

Audit verdict: PASS (all verified) / PARTIAL (>= 1 unverified, no inconsistent) /
FAIL (any inconsistent or majority unverified).

Unverified chains must be corrected before Phase C. Record the final verdict and chain
list here — JUDGE will cite this record directly. (Reference: VIOLATION TAXONOMY
REGISTRY.)

Phase C — PATTERN AND RANK VERIFICATION
1. Confirm Pattern-of-N counts are stated and traceable to ADVERSARY ARROW CHAIN.
2. Confirm the output will include exactly 3 KEY EVIDENCE entries. Confirm each will
   include a "Why not the rank below:" sub-item. Absence at any rank = VIO-5.

---

PHASE 4 — JUDGE

JUDGE cannot introduce new evidence. JUDGE cannot reopen the SURVEYOR inventory. JUDGE
reads the ADVERSARY ARROW CHAIN as audited by PRE-FLIGHT Phase B.

JUDGE failure mode (own this): hedging — issuing a qualified "maybe with caveats" when
the audited chain and the adversarial challenge together support a definite answer.
NOT: confidence >= 70 with adversarial challenge addressed produces MAYBE — VIO-4.
A JUDGE that qualifies a clean verdict into ambiguity has failed as JUDGE.

DETERMINATION: [this word opens the commitment sentence — the complete declarative
answer appears immediately after this label, not after any further preamble]

Confidence paragraph (chain of custody site 3 — applies PRE-FLIGHT Phase B result):
"Per PRE-FLIGHT Phase B, the arrow-chain audit verdict is [cite verdict from Phase B
by name, with the verified/unverified chain list]. The Pattern-of-N analysis found
[N] of [M] top signals [distribution property], [with / without] cross-type
confirmation. Confidence cap applied: [PASS permits >=75 / PARTIAL caps at 70 / FAIL
caps at 50]. Confidence is [score] because [structural reason grounded in the audit
result and the distribution finding]." NOT: confidence paragraph that omits `preflight
verdict` by name — VIO-4. (Reference: VIOLATION TAXONOMY REGISTRY.)

Fill FRONTMATTER fields now.
NOT: leave any field empty at document close — VIO-2.
NOT: fill any JUDGE-designated field before this phase — VIO-1.

---

SYNTHESIS BODY

First line: "This synthesis is self-contained and supersedes all underlying investigation
signals. No access to the underlying investigation artifacts is required to understand
the answer, the reasoning, or what to do next."

**ANSWER**: [Complete declarative sentence. First content after the opening mandate.
This is the position of record.]

**CONFIDENCE**: [0–100]
[2–3 sentences. Cite PRE-FLIGHT Phase B audit verdict and Pattern-of-N distribution
finding by name. State what drove the score up and what held it back.]

**KEY EVIDENCE**

Exactly 3 entries. Prose argument blocks — NOT a table (VIO-5 applies at each rank).
The "Why not the rank below:" sub-item is a required structural slot at every rank
position. Its absence at any rank is a RANK-SKIP VIOLATION (VIO-5) regardless of
whether comparative language appears elsewhere in the synthesis.

**Rank 1 — [Signal ID + name]**
Claim: [What this signal asserts, one sentence]
Bearing: [Why this signal influenced the answer — argument, not description of contents]
Why not the rank below: [The specific property of rank 1 that makes it more decisive
than rank 2. Name the property at this rank position, not as prose commentary after
all three entries.]

**Rank 2 — [Signal ID + name]**
Claim: [What this signal asserts]
Bearing: [Why this influenced the answer]
Why not the rank below: [The specific property separating rank 2 from rank 3. What
does rank 2 provide that rank 3 cannot substitute for in this verdict?]

**Rank 3 — [Signal ID + name]**
Claim: [What this signal asserts]
Bearing: [Why this influenced the answer]
Why not the rank below: [Why rank 3 belongs in the top 3 over any rank 4 candidate.
If only 3 signals exist in the evidence set, state: "No rank 4 candidate — signal
included on merit, not by elimination."]

**COUNTER-EVIDENCE**:
[Named signal or finding arguing against the answer. Weight (high / medium / low) and
rationale for that weight — why the weight is proportionate, not just what the signal
argues. If none: "No counter-evidence found. [State whether absence is expected given
the investigation scope or is itself a potential gap.]"]

**PRINCIPLES EXTRACTED**:
[X implies Y. One or more declarative principles that generalize beyond this specific
hypothesis to future investigations of similar type. Not a restatement of the finding.]

**OPEN QUESTIONS**:
[One or more specific, named questions this investigation did not resolve. For each:
state what evidence would resolve it and why it matters to the stated answer.]

---

VIOLATION AUDIT CLOSE — confirm before finalizing:
- [ ] VIO-1: no FRONTMATTER field was filled before its designated phase
- [ ] VIO-2: all FRONTMATTER fields are filled; none empty
- [ ] VIO-3: SURVEYOR, ADVERSARY, and PRE-FLIGHT all completed before JUDGE executed
- [ ] VIO-4: JUDGE confidence paragraph cites `preflight_verdict` by name
- [ ] VIO-5: all three KEY EVIDENCE rank entries include "Why not the rank below:" sub-item

If any check fails, correct the violation before marking the synthesis complete.
```

---

## Criteria Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-08 Essential + Recommended | pass | pass | pass | pass | pass |
| C-09 Evidence hierarchy argued | pass | pass | pass | pass | pass |
| C-10 Self-contained mandate | pass | pass | pass | pass | pass |
| C-11 Anti-pattern gates | pass | pass | pass | pass | pass |
| C-12 Prose (not table) for evidence | pass | pass | pass | pass | pass |
| C-13 NOT:-first ordering | pass | pass | pass | pass | pass |
| C-14 Formal verdict register | pass | pass | pass | pass | pass |
| C-15 Pre-committed counter-evidence | pass | pass | pass | pass | pass |
| C-16 Role-labeled + identity foreclosure | pass (partial) | pass (partial) | pass | pass | pass |
| C-17 Record-specific anti-pattern | partial | partial | pass | pass | pass |
| C-18 Register word opens commitment | pass | pass | pass | pass | pass |
| C-19–C-28 Structural phases (frontmatter, SURVEYOR, arrow-chain, PRE-FLIGHT, three-site) | — | — | C-19–C-25 pass | all pass | all pass |
| **C-29 Per-rank comparative slot** | FAIL | **PASS** | borderline | borderline | **PASS** |
| **C-30 Role-native failure mode ownership** | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| **C-31 Pattern-of-N adversarial input** | FAIL | FAIL | **PASS** | **PASS** | **PASS** |
| **Predicted score (v8)** | ~112.5 | ~112.5 | ~135 | ~142.5 | **147.5** |

**V-05 path to 147.5**: R7 V-05 baseline (140.0) + C-29 (+2.5) + C-30 (+2.5) + C-31 (+2.5) = 147.5.
C-29/C-12 tension resolved via per-rank labeled prose sub-items — table-free, slot-enforced.
