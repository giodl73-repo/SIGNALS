**v9 rubric written** to `simulations/quest/rubrics/prove-topic-rubric-v9-2026-03-15.md`.

Three new aspirational criteria extracted from Round 9 excellence signals:

| ID | Axis | Pattern | Exemplar |
|----|------|---------|---------|
| **C-28** | Symmetric path chain | Both lock fields carry `positive_derivation:` + `independence_chain:` — `co_activation_confirmed` proves its own derivation through dual-lock and independence from the campaign-outcome path | V-02 |
| **C-29** | Per-stage schema integrity counts | SCHEMA INTEGRITY NOTE at each evidence stage counting declared fields populated so far — C-20's accumulation discipline applied to schema compliance | V-03 |
| **C-30** | Annotation rule as session invariant | DERIVATION ANNOTATION RULE declared as SESSION INVARIANT C at CAMPAIGN OPEN with "cannot be bypassed" language — C-19's invariant discipline applied to C-25 enforcement | V-04 |

**Weight outcome:** Max rises 156 → 168. Aspirational expands to 22 criteria × 4 pts = 88 pts. Golden threshold unchanged at 80.

**Structural note:** C-28/C-29/C-30 form two extensions to the v8 architecture:
- **Handoff Contract Chain** grows to four entries: C-25 (annotation) → C-26 (pre-commitment) → C-27 (independence proof) → C-28 (symmetric proof)
- **Contract Enforcement Symmetry** is a new section: C-29 applies the C-20 accumulation model to schema integrity; C-30 applies the C-19 invariant model to annotation enforcement

A v8-ceiling variation (156/156) can still fail all three: `co_activation_confirmed` chain unannotated (C-28 FAIL), no per-stage schema counts (C-29 FAIL), annotation rule reactive rather than invariant-declared (C-30 FAIL).
stent across all artifacts

PASS: Every artifact path referenced in the response starts with `{topic}-`. A prefix
defined once at session opening but not repeated in per-artifact write instructions is a
PARTIAL (5 pts). Per-artifact path naming in each write instruction is full PASS.

---

## Recommended Criteria (10 pts each)

### C-06 — Stage order enforced

PASS: The five sub-skills are presented in a fixed sequence with a forward-only
constraint. No mechanism to skip back, re-run stages in arbitrary order, or proceed
without completing the prior stage is a FAIL.

### C-07 — Scout signal handoff is explicit

PASS: A named scout anchor (slug, path, or `scout-record` field) is required in the
hypothesis frontmatter or stage-entry block. The scout artifact must be named, not just
generally referenced. A vague "use your scout research" instruction without naming the
artifact is a PARTIAL (4 pts).

### C-08 — Synthesis signals readiness for topic-story

PASS: The synthesis stage includes a handoff indicator pointing to `topic-story` or
equivalent downstream artifact. A synthesis that ends without a named next step is a
PARTIAL (4 pts).

---

## Aspirational Criteria (4 pts each)

### C-09 — Thin-evidence acknowledgment propagates

PASS: If any evidence stage (web search, interview, prototype) yields thin or conflicting
evidence, that signal is carried forward explicitly to the synthesis. A flag at Stage 4
that is not referenced in Stage 5 is a PARTIAL (2 pts). Full PASS requires the synthesis
to name the thin-evidence finding and qualify confidence accordingly.

### C-10 — Progress narrated per stage

PASS: Each stage produces an explicit natural-language confirmation of what was found or
done before advancing — not just a structural gate. Verdict tokens alone (e.g., `[X]`,
`--`) without accompanying prose acknowledgment are a PARTIAL (2 pts).

### C-11 — Hypothesis entry is hard-gated on scout confirmation

*Excellence signal from V-01 (Round 1).*

PASS: The scout-load step structurally prevents any hypothesis work until the scout
artifact is confirmed present. Examples: an explicit GATE block before Stage 1, a
forward-condition checkbox required before the hypothesis section opens, or an explicit
"do not proceed until scout-record is on file" instruction. A named anchor (satisfying
C-07) without a blocking gate is insufficient for C-11. The V-01 GATE S pattern is the
exemplar.

Failure mode addressed: variations that name a scout anchor but allow hypothesis
formation to proceed from general knowledge rather than the loaded artifact.

### C-12 — Thin-evidence comparator anchored at session open

*Excellence signal from V-04 (Round 1).*

PASS: A status-quo baseline or incumbent comparator is named at the session's opening
— before any evidence gathering — and explicitly referenced at each evidence stage. This
grounds any thin-evidence acknowledgment in a concrete alternative rather than an
isolated caveat. A comparator introduced only at Stage 4 or only in the synthesis is a
PARTIAL (2 pts). The pattern — "status-quo comparator at campaign opening → referenced
at each evidence stage → Warning+effect at Stage 4 traced to synthesis" — is the
exemplar.

Failure mode addressed: C-09 partials where thin-evidence flags appear late and are not
connected to a pre-established baseline, making the confidence qualification untethered.

### C-13 — Per-artifact path enforcement on each write instruction

*Excellence signal from V-01 (Round 1).*

PASS: Every write instruction in the response names the full artifact path (e.g.,
`{topic}-hypothesis-{date}.md`), not just the topic prefix or a filename stem. A prefix
defined once at session opening without per-instruction path naming is a PARTIAL (2 pts).
This prevents prefix drift across sub-stages and multi-turn sessions.

Failure mode addressed: C-05 partials where a correctly-defined opening prefix drifts by
Stage 3-4 because individual write instructions do not restate it.

### C-14 — Counter-evidence unconditionally required in synthesis

*Excellence signal from V-04/V-05 (Round 2).*

PASS: The synthesis section requires counter-evidence as a named, mandatory field — not
as a conditional section or optional addition. The instruction must make counter-evidence
unconditionally required, with an explicit fallback for the case where none was gathered
during the campaign (e.g., "If no counter-evidence was found, state why."). A synthesis
that says "include counter-evidence if any was found" is a PARTIAL (2 pts).

Failure mode addressed: synthesis sections that silently elide counter-evidence when all
evidence was uniformly positive, inflating confidence in the output. The pattern —
Counter-Evidence listed as a mandatory section alongside Findings and Confidence, with a
required fallback instruction — is the exemplar.

### C-15 — Gate clearance state propagated into hypothesis artifact

*Excellence signal from V-04/V-05 (Round 2).*

PASS: After GATE S clears, the hypothesis artifact or its frontmatter includes an
explicit field recording gate clearance (e.g., `gate_s_cleared: true`). This provides a
traceable record that the gate was checked — visible in the artifact itself, not only in
the session preamble. A GATE block with no artifact-level record of clearance satisfies
C-11 but not C-15. FAIL if C-11 is FAIL (no gate defined at all). PARTIAL (2 pts) if
the gate clears but clearance is recorded only in the session log, not in the hypothesis
frontmatter.

Failure mode addressed: gate instructions that leave no trace in the artifact chain,
making it impossible to audit gate compliance from the artifact alone without replaying
the full session.

### C-16 — Null counter-evidence triggers adversarial escalation

*Excellence signal from V-01/V-02/V-03 (Round 3).*

PASS: When the synthesis counter-evidence section records a null result (no
counter-evidence gathered during the campaign), the response explicitly recommends
adversarial review or an equivalent challenge activity as a required next step — not as
an optional aside. Recording null without an escalation instruction is a PARTIAL (2 pts).
The Round 3 pattern — "null result recorded → adversarial review explicitly recommended"
— is the exemplar.

Failure mode addressed: C-14 requires the null to be recorded with a fallback statement;
it does not require the null to trigger downstream action. A synthesis can satisfy C-14
by acknowledging null passively. C-16 requires the null to be treated as an open signal
that demands a response — making the absence of counter-evidence a forward obligation,
not a closed audit entry.

### C-17 — Confidence composite mechanically capped by counter-evidence state

*Excellence signal from V-02/V-03 (Round 3).*

PASS: The synthesis confidence level is computed or capped via an explicit rule tied to
counter-evidence state — not only narrated. Examples: "maximum score reduced by 1 point
if null counter-evidence result", a numeric ceiling triggered by `thin_evidence_propagated`,
or a frontmatter field (e.g., `cap_applied: true`) confirming the rule fired. Confidence
that is verbally qualified without a traceable computation rule or cap instruction is a
PARTIAL (2 pts). V-02's "maximum score reduced by 1 point" and V-03's "cannot be rated
HIGH without adversarial input" constraint are the exemplars.

Failure mode addressed: variations where C-09 (thin-evidence propagation) passes because
the synthesis mentions thin evidence verbally, but the confidence level itself is unchanged
or unconstrained. The verbal qualification exists but exerts no mechanical effect on the
output score. C-17 requires the evidence quality to structurally limit what the confidence
level can claim — not merely annotate it.

### C-18 — Null CE synthesis doubly locked

*Excellence signal from V-04 (Round 4).*

PASS: When counter-evidence is null, the synthesis simultaneously applies both
constraints: promotion is blocked or escalated (C-16), and confidence is mechanically
capped (C-17). Both must be active in the same synthesis output — not satisfied in
separate conditional branches where one could fire without the other. A synthesis where
only one constraint activates on null CE is a PARTIAL (2 pts). FAIL if neither activates.
V-02's ATOMIC DUAL-LOCK — "Both locks activate from this single entry. Partial activation
is a format error." with `co_activation_confirmed` required — is the exemplar.

Failure mode addressed: systems where C-16 and C-17 each pass in isolation across
different variations but no single synthesis output applies both. A builder satisfying
each criterion in a different conditional branch produces a skill that is individually
compliant on C-16 and C-17 but leaves open a null-CE output that is promotion-eligible
(C-16 branch not taken) or confidence-unconstrained (C-17 branch not taken). C-18
requires both locks to be active in the same synthesis output, closing the null-CE path
completely.

### C-19 — Full null-CE protocol pre-committed at campaign open

*Excellence signal from V-04 (Round 4).*

PASS: The CAMPAIGN OPEN block — declared before Stage 0 — names both the adversarial
reviewer type (required by C-16) and the confidence cap rule (required by C-17) as
session-level commitments using invariant language (e.g., "cannot be modified or
bypassed", "session-level invariant", "pre-registered — not a synthesis decision"). A
block that registers both fields but uses registration framing without invariant language
is a PARTIAL (2 pts). FAIL if neither is declared before Stage 0. V-01's PROTOCOL
DECLARATION ("Do not modify after this point") and V-03's SESSION INVARIANT REGISTRY
("binding for the full session — cannot be modified or bypassed at synthesis time") are
the exemplars.

Failure mode addressed: variations where C-16 and C-17 are satisfied at synthesis time
only — the reviewer is appointed and the cap is applied reactively when null CE is
detected, rather than as pre-established protocol. Without invariant language, a builder
can implicitly suppress either mechanism before Stage 1 by treating them as conditional
responses. Pre-commitment with invariant language makes the adversarial reviewer and cap
rule session properties, not runtime decisions.

### C-20 — Per-stage null tally accumulates with protocol reference

*Excellence signal from V-03 (Round 5).*

PASS: When an evidence stage returns null, its null-result note contributes to a running
tally with explicit count language ("Running tally: N null. X stages remain...") and
references the pre-committed invariants as already-activated obligations — not as
decisions pending synthesis. A null-result note that records the null without tally
accumulation is a PARTIAL (2 pts). FAIL if null results are recorded only at synthesis
without any per-stage notes. V-03's per-stage notes framing null results as "pre-committed
session obligations, not conditional judgments" with running stage counts is the exemplar.

Failure mode addressed: systems where null-CE propagation satisfies C-09
(synthesis-level acknowledgment) but the accumulation is computed retroactively at Stage
5 — leaving open the possibility that a multi-stage null session is not recognized as
such until the terminal step. Per-stage running tally language makes the accumulation
auditable at each evidence stage. Tally notes that reference the pre-committed invariants
make visible that the null path was anticipated and pre-loaded — not assembled in response
to what was found. A variation can satisfy C-09 and C-19 and still fail C-20: null
acknowledged at synthesis (C-09 PASS) and protocol pre-committed (C-19 PASS), but no
per-stage accumulation exists between collection and synthesis.

### C-21 — Co-activation state echoed into handoff artifact

*Excellence signal from V-02 (Round 5).*

PASS: The handoff section of the synthesis includes a field (e.g.,
`co_activation_confirmed: [must equal dual_lock_fired]`) that propagates the dual-lock
co-activation outcome from the synthesis block into the handoff artifact. A synthesis
that satisfies C-18 (both locks fire) but does not carry the co-activation outcome into
the handoff is a PARTIAL (2 pts). FAIL if C-18 is FAIL. V-02's integrity constraint
`co_activation_confirmed: [must equal dual_lock_fired]` in the Handoff section —
requiring the field value to match the synthesis-level activation record — is the
exemplar.

Failure mode addressed: C-18 verifies that both locks fire atomically inside the
synthesis block; it does not require the outcome to be visible from the handoff artifact
alone. A handoff without a co-activation field forces downstream consumers (e.g.,
`topic-story`) to trace back into the synthesis to verify null-CE closure. C-21 makes
co-activation self-documenting in the handoff, enabling point-in-chain audit without
full session replay. A variation can satisfy C-18 completely — atomic dual-lock, both
fields, format-error guard — and still fail C-21 if the handoff section is structurally
complete (satisfying C-08) but carries no co-activation echo.

### C-22 — Invariant registry confirmed as distinct gate field

*Excellence signal from V-03 (Round 5).*

PASS: The hypothesis frontmatter includes a dedicated field confirming the invariant
registry was verified before Stage 1 opened (e.g., `invariant_registry_confirmed: true`),
separate from the scout-load gate field (`gate_s_cleared: true`). GATE S must require
both fields before Stage 1 proceeds. A GATE S that requires only `gate_s_cleared` without
a corresponding invariant-registry confirmation field satisfies C-15 but not C-22. PARTIAL
(2 pts) if an invariant confirmation is noted in the session log but not reflected in a
named hypothesis frontmatter field. FAIL if C-19 is FAIL (no invariant registry to
confirm). V-03's GATE S requiring both `gate_s_cleared: true` and
`invariant_registry_confirmed: true` is the exemplar.

Failure mode addressed: C-15 records scout-gate clearance in the hypothesis artifact; it
does not record whether the pre-committed null-CE invariants were in scope when the
hypothesis was formed. Without a distinct invariant-registry field, a hypothesis artifact
may satisfy C-15 (gate cleared) and C-19 (registry declared at session open) while leaving
no auditable link between the two — making it impossible to verify, from the artifact
alone, that the invariant registry was active at the point hypothesis formation began, as
opposed to being declared earlier and then operationally ignored.

### C-23 — Campaign-outcome boolean as independent handoff field

*Excellence signal from V-05 (Round 6).*

PASS: The handoff section includes a named campaign-outcome boolean field (e.g.,
`incumbent_defense_closed: [true if all null, false if any found]`) that is structurally
independent of the dual-lock co-activation field (`co_activation_confirmed`). This field
answers the campaign-level question directly as a readable boolean — downstream consumers
(e.g., `topic-story`) can determine campaign state without tracing dual-lock semantics. A
handoff satisfying C-21 (carries `co_activation_confirmed`) but defining campaign outcome
only through the co-activation field is a PARTIAL (2 pts). FAIL if C-21 is FAIL. V-05's
`incumbent_defense_closed: [true if all null, false if any found]` as a separate field
alongside `co_activation_confirmed` in the Handoff is the exemplar.

Failure mode addressed: C-21 carries the dual-lock co-activation state into the handoff,
enabling point-in-chain audit. However, interpreting `co_activation_confirmed` to
determine campaign outcome requires knowing what `dual_lock_fired` means — it creates a
semantic dependency on the null-CE machinery. C-23 requires a clean campaign-level signal
that downstream consumers can read without internal knowledge of the dual-lock mechanism.
A variation can satisfy C-21 completely and still fail C-23: the co-activation field is
present and correctly valued, but no independent campaign-outcome boolean exists, forcing
`topic-story` to decode dual-lock state rather than read a direct answer.

### C-24 — Role-structural dual attestation

*Excellence signal from V-05 (Round 6).*

PASS: The GATE S block assigns structurally distinct roles or blocking positions for
scout-load attestation (`gate_s_cleared`) and invariant-registry attestation
(`invariant_registry_confirmed`) — so that each field is owned by a separate structural
element within the gate. The two-field requirement is enforced by construction: dropping
either role means losing exactly one attestation field, creating an immediately auditable
structural gap. A GATE S that lists both fields but assigns them to the same agent or step
satisfies C-22 (both fields present) but not C-24 (structural ownership separation).
PARTIAL (2 pts) if roles are named but the gate logic permits a single role to certify
both fields. FAIL if C-22 is FAIL. V-05's two blocking roles each producing exactly one
attestation field — making C-22 drift-resistant by construction rather than by instruction
— is the exemplar.

Failure mode addressed: C-22 requires two distinct named fields in the hypothesis
frontmatter. A builder can satisfy C-22 by having a single procedural step populate both
fields — making the two-field requirement instruction-dependent and fragile: the step can
be simplified or the second field omitted without violating any structural rule. C-24
requires each field to have a dedicated structural owner so that loss of either owner is a
structural change with an auditable consequence, not an invisible simplification. A
variation can satisfy C-22 completely — both fields present and correctly valued — and
still fail C-24 if the two fields share a single structural origin.

### C-25 — Handoff fields carry inline derivation annotations

*Excellence signal from V-01/V-04/V-05 (Round 8).*

PASS: Every field in the handoff section of the synthesis carries an inline derivation
annotation of the form `[derived from: X]`, naming the upstream artifact, stage output,
or computation that produced the field value. A DERIVATION ANNOTATION RULE must be
declared as a separate enforcement clause — distinct from the schema compliance check —
with an explicit consequence for violations (e.g., "unlabeled field = format error"). A
handoff where derivation sources appear only in a pre-committed schema table at CAMPAIGN
OPEN but are not repeated as per-field inline labels at synthesis time is a FAIL. A
handoff where a subset of fields carry derivation labels while others are bare is a
PARTIAL (2 pts). V-01's and V-05's DERIVATION ANNOTATION RULE with "Unlabeled field =
format error" and all 8/9 fields labeled are the exemplars.

Failure mode addressed: C-23 ensures `incumbent_defense_closed` is present and
independent; C-21 ensures `co_activation_confirmed` propagates into the handoff. Neither
requires the consumer to know where each field's value originated. A handoff can satisfy
C-21, C-23, and C-26 (pre-committed schema) while being fully unauditable at the field
level — every field is present and schema-compliant, but no label connects any field to
its source stage or artifact. C-25 makes derivation provenance a structural requirement
of the synthesis output itself, enabling field-level audit without session replay. A
variation can satisfy the full v7 stack and still fail C-25: all handoff fields present
and correctly valued (C-21, C-23 PASS), schema declared at CAMPAIGN OPEN (C-26 PASS if
present), but no field carries a `[derived from: X]` label.

### C-26 — Handoff schema pre-committed at campaign open

*Excellence signal from V-02/V-04/V-05 (Round 8).*

PASS: The CAMPAIGN OPEN block declares a complete handoff schema table — all required
field names and their required derivation sources — before Stage 0. The synthesis write
instruction must reference this pre-committed schema by name and include a compliance
check (e.g., `schema_compliance_confirmed: true`) confirming no fields were added,
removed, or derivation-source-mismatched. A handoff schema assembled reactively at
synthesis time (no schema declared before Stage 0) is a FAIL. A pre-committed schema
without a compliance check at synthesis — or a compliance check without a named reference
to the CAMPAIGN OPEN schema — is a PARTIAL (2 pts). FAIL if C-19 is FAIL (no CAMPAIGN
OPEN block). V-02's 8-field DECLARED FIELDS table with derivation sources at CAMPAIGN
OPEN and `schema_compliance_confirmed` at synthesis, V-04's PRE-COMMITTED HANDOFF SCHEMA
with compliance check before synthesis writes, and V-05's schema including
`schema_compliance_confirmed` as a declared field itself with "no additions, no omissions,
derivation-source mismatch is format error" are the exemplars.

Failure mode addressed: C-25 requires inline derivation labels on every handoff field at
synthesis time. Without a pre-committed schema, the field list and derivation sources can
still be assembled reactively during synthesis — a builder satisfying C-25 by labeling
all fields at synthesis time could silently add or omit fields, or mislabel sources,
without any auditable contract to check against. C-26 locks the handoff contract before
evidence gathering begins, making schema deviations detectable from the CAMPAIGN OPEN
block alone. A variation can satisfy C-25 (all fields labeled inline) and still fail
C-26: every field carries a `[derived from: X]` label, but no schema was declared before
Stage 0, leaving the field list and source assignments without a pre-registered baseline
to enforce.

### C-27 — Independence path chain explicit on campaign-outcome derivation

*Excellence signal from V-03 (Round 8).*

PASS: The derivation annotation for `incumbent_defense_closed` (required by C-25) includes
an explicit independence path chain — a named sequence of stage outputs or artifact fields
demonstrating that the value is derived without passing through `co_activation_confirmed`
or `dual_lock_fired`. The chain must be structural: each step names a source field and the
stage or artifact that produced it. A derivation annotation that names a source for
`incumbent_defense_closed` without an independence chain (e.g., `[derived from: Stage 3
null tally]` with no chain) is a PARTIAL (2 pts). FAIL if C-25 is FAIL (no derivation
annotations) or if `incumbent_defense_closed` carries no derivation annotation. V-03's
`positive_derivation:` and `independence_chain:` fields on `incumbent_defense_closed` are
the exemplar.

Failure mode addressed: C-23 requires `incumbent_defense_closed` to be structurally
independent of `co_activation_confirmed` — the field must exist as a separate boolean.
C-25 requires a derivation annotation naming the source. But a derivation annotation
alone does not prove independence: a builder can label a field `[derived from:
dual_lock_result]` and the annotation satisfies C-25 while violating C-23. C-27 requires
the independence claim to be made explicit as a traceable chain — enumerating the stage
outputs that feed the derivation and confirming none of them pass through the dual-lock
mechanism. A variation can satisfy C-23 (field is present) and C-25 (field is labeled)
and still fail C-27: `incumbent_defense_closed` carries a `[derived from: X]` label, but
no path chain exists to verify the independence assertion.

### C-28 — Symmetric independence path chain on both lock fields

*Excellence signal from V-02 (Round 9).*

PASS: Both `incumbent_defense_closed` AND `co_activation_confirmed` carry explicit
`positive_derivation:` and `independence_chain:` annotations — each proving its own
derivation path independently of the other. The chains must be directionally distinct:
`incumbent_defense_closed` proves independence from the dual-lock path (required by C-27);
`co_activation_confirmed` proves derivation through — and only through — the ATOMIC
DUAL-LOCK mechanism and independence from the campaign-outcome path. C-27 must pass. A
handoff where only `incumbent_defense_closed` carries the full chain while
`co_activation_confirmed` carries only a brief NOT annotation or a single-line note
satisfies C-27 but not C-28. PARTIAL (2 pts) if `co_activation_confirmed` carries a
`positive_derivation:` annotation but no `independence_chain:`. FAIL if C-27 is FAIL.
V-02's full `positive_derivation:` + `independence_chain:` on both fields — each chain
verifiably non-intersecting at the derivation level — is the exemplar.

Failure mode addressed: C-27 makes the independence of `incumbent_defense_closed` from
`co_activation_confirmed` a verifiable chain. But it places no symmetric requirement on
`co_activation_confirmed` — a builder satisfying C-27 knows where `incumbent_defense_closed`
comes from; `co_activation_confirmed`'s derivation path remains unannotated. C-28 closes
the asymmetry: both fields must publish their full derivation chains, and the chains must
be mutually non-intersecting — making the structural independence of C-23 verifiable from
both directions simultaneously. A variation can satisfy C-27 completely — `incumbent_defense_closed`
carries a full `positive_derivation:` + `independence_chain:` — and still fail C-28 if
`co_activation_confirmed` is present and correctly valued (C-21 PASS) but its derivation
source is unannotated or incompletely chained.

### C-29 — Per-stage schema integrity counts

*Excellence signal from V-03 (Round 9).*

PASS: Every evidence stage that writes a handoff-relevant artifact includes a SCHEMA
INTEGRITY NOTE (or equivalent named construct) with explicit count language (e.g.,
"SCHEMA INTEGRITY: 3/8 declared fields populated — 0 additions, 0 omissions, 0 source
mismatches detected so far"), accumulating toward the full schema across stages. C-20
and C-26 must both pass: per-stage null tally and pre-committed schema are prerequisites
for schema integrity counts to be meaningful. A per-stage null tally without schema
integrity counts satisfies C-20 but not C-29. PARTIAL (2 pts) if schema integrity counts
appear at some evidence stages but not all. FAIL if C-26 is FAIL (no pre-committed
schema to count against). V-03's per-stage SCHEMA INTEGRITY NOTE pairing its field
population count with the NULL TALLY NOTE at each stage is the exemplar.

Failure mode addressed: C-26 requires the schema to be pre-committed at CAMPAIGN OPEN
and compliance-checked at synthesis. C-20 requires null results to be tallied per stage.
Neither requires schema compliance to be monitored during collection — schema drift can
accumulate silently from Stage 2 through Stage 4 and only be detected at the terminal
synthesis compliance check. C-29 applies the same accumulation discipline to schema
integrity that C-20 applies to null-CE events: compliance is a running observation, not
a terminal audit. A variation can satisfy C-20 (per-stage null tally), C-26 (schema
pre-committed, compliance confirmed at synthesis), and C-25 (all fields labeled) while
failing C-29: no stage between collection and synthesis explicitly tracks schema
population progress, leaving schema drift undetectable until the final step.

### C-30 — Derivation annotation rule pre-committed as session invariant

*Excellence signal from V-04 (Round 9).*

PASS: The DERIVATION ANNOTATION RULE is declared as a named SESSION INVARIANT at CAMPAIGN
OPEN — on par with the null-CE invariants of C-19 — with explicit invariant language
(e.g., SESSION INVARIANT C: "Every handoff field carries `[derived from: X]` — cannot be
modified or bypassed at synthesis time"). C-19, C-25, and C-26 must all pass. An
annotation rule enforced via a synthesis instruction or embedded within the schema table
at CAMPAIGN OPEN but without explicit session-invariant naming and language satisfies
C-25 and C-26 but not C-30. PARTIAL (2 pts) if the annotation rule is referenced at
CAMPAIGN OPEN but without invariant naming or "cannot be bypassed" language. FAIL if
C-19 is FAIL (no CAMPAIGN OPEN invariant block). V-04's SESSION INVARIANT C declaring
the derivation annotation requirement alongside SESSION INVARIANTs A and B (the null-CE
invariants) at CAMPAIGN OPEN is the exemplar.

Failure mode addressed: C-25 and C-26 together ensure derivation annotations are
required and the schema is locked at CAMPAIGN OPEN. But without invariant pre-commitment,
both requirements exist only as synthesis-stage instructions or schema compliance notes —
subject to the same late-assembly failure mode that C-19 addresses for null-CE protocol.
A builder satisfying C-25 and C-26 treats annotation enforcement as a synthesis-time
rule: the schema was declared at CAMPAIGN OPEN, but the annotation compliance check fires
reactively when synthesis runs. C-30 elevates the annotation requirement to the same
invariant tier as the null-CE protocol: pre-registered before Stage 0, immune to
synthesis-time suppression. A variation can satisfy C-25 (all fields labeled inline) and
C-26 (schema pre-committed with compliance check) and still fail C-30: derivation
annotation enforcement is active at synthesis but reactive — not pre-registered as a
named session invariant.

---

## Scoring

### Weights

| Tier | Points | Criteria | Per criterion |
|------|--------|----------|---------------|
| Essential | 50 | 5 | 10 pts |
| Recommended | 30 | 3 | 10 pts |
| Aspirational | 88 | 22 | 4 pts |
| **Max composite** | **168** | | |

### Formula

```
composite = (essential_pts) + (recommended_pts) + (aspirational_pts)
```

### Thresholds

| Result | Condition |
|--------|-----------|
| **Golden** | All C-01 through C-05 pass AND composite >= 80 |
| **Passing** | All essential pass, composite < 80 |
| **Failing** | Any essential criterion fails |

### Example score calculations

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 14/19 pass → 56
- **Composite = 136** — Golden (v6 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 16/19 pass → 64
- **Composite = 144** — Golden (v7 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 19/19 pass → 76
- **Composite = 156** — Golden (v8 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 22/22 pass → 88
- **Composite = 168** — Golden (v9 ceiling)

---

## Design Rationale

### Essential tier

Focuses on the three things that make this skill an orchestrator rather than a
single-step skill: all stages ran (C-01), context was loaded from scout (C-02), and
artifacts were written progressively (C-03). C-04/C-05 ensure the terminal output is
usable and discoverable.

### Recommended tier

Adds traceability (C-06, C-07) and downstream handoff (C-08). All three were full PASS
in the highest-scoring Round 1 and Round 2 variations; partial failures here are the
primary separator between 85- and 95-range scores. The recommended tier and essential
tier together sum to exactly 80 — the golden threshold — making these six criteria the
complete baseline for a qualifying skill output.

### Aspirational tier

Targets the failure modes unique to orchestration. The twenty-two criteria form six
pairs, one triple, one quartet, one quintet, and two standalones:

- **C-09, C-12**: Confidence inflation from thin evidence. C-09 checks propagation;
  C-12 checks whether the comparator that makes thin evidence meaningful was established
  upfront. Complementary — C-12 is the upstream condition that makes C-09 actionable.

- **C-10, C-11**: Opaque progress and silent gateway failures. C-10 asks for narrative
  confirmation; C-11 asks for a hard blocking gate before hypothesis formation. Together
  they prevent the failure mode where a variation looks complete but the scout-load step
  was nominal.

- **C-13, C-15**: Prefix drift and gate-trace gaps. C-13 checks per-instruction path
  enforcement; C-15 checks that gate clearance is recorded in the artifact. Both address
  the same failure pattern: a correct instruction at session open that leaves no trace
  in the artifact chain.

- **C-14, C-16**: Counter-evidence posture. C-14 makes the section unconditionally
  required with a null fallback; C-16 requires the null to trigger adversarial escalation.
  C-14 is the structural gate; C-16 is the forward obligation that the null finding
  generates. A variation can satisfy C-14 by acknowledging null passively and still fail
  C-16.

- **C-17** (standalone): Mechanical confidence capping. Extends C-09 from verbal
  qualification to structural constraint.

- **C-18, C-19**: Severity stack integration (added v5). C-18 verifies that C-16 and
  C-17 co-fire in the same synthesis output. C-19 verifies that the null-CE protocol was
  pre-committed at CAMPAIGN OPEN with invariant language, not assembled reactively at
  synthesis time. Together they close the gap between individual criterion compliance and
  structural invariance.

- **C-20, C-21, C-22**: Audit completeness (added v6). Each extends an existing
  criterion's coverage from synthesis-internal or session-local to collection-phase or
  cross-artifact visibility. C-20 extends C-09 from synthesis-level acknowledgment to
  per-stage accumulation. C-21 extends C-18 from synthesis-block co-activation to
  cross-artifact echo. C-22 extends C-15 from scout-gate confirmation to
  invariant-registry confirmation.

- **C-23, C-24**: Structural enforcement (added v7). Each tightens a v6 audit criterion
  from presence to independence. C-23 extends C-21 by requiring a campaign-outcome
  boolean independent of the dual-lock mechanism. C-24 extends C-22 by requiring
  role-structural ownership of each attestation field.

- **C-25, C-26, C-27**: Handoff contract integrity (added v8). Each extends the handoff
  audit chain from structural presence to derivation transparency and pre-registered
  contract. C-25 requires every handoff field to carry an inline `[derived from: X]`
  label. C-26 requires the complete handoff schema to be locked at CAMPAIGN OPEN. C-27
  requires the derivation annotation on `incumbent_defense_closed` to include an explicit
  independence path chain. A variation can satisfy the full v7 stack and still fail all
  three.

- **C-28, C-29, C-30**: Contract enforcement symmetry (added v9). Each extends a v8
  criterion from unidirectional or terminal coverage to symmetric or pre-emptive coverage.
  C-28 extends C-27 from a unidirectional independence chain (on `incumbent_defense_closed`
  only) to a symmetric chain (on both lock fields — each proving its own derivation path
  independently of the other). C-29 extends C-20 and C-26 by applying the same per-stage
  accumulation discipline to schema integrity that C-20 applies to null-CE events —
  making schema drift detectable per stage, not only at the terminal compliance check.
  C-30 extends C-19 and C-25 by elevating the derivation annotation requirement from a
  synthesis-stage enforcement rule to a pre-committed session invariant at CAMPAIGN OPEN
  — on par with the null-CE invariants. A variation can satisfy the full v8 stack and
  still fail all three: both independence chains unannotated on `co_activation_confirmed`
  (C-28 FAIL), no per-stage schema integrity count (C-29 FAIL), annotation rule enforced
  reactively rather than as a session invariant (C-30 FAIL).

---

## Severity Stack: C-14 / C-16 / C-17 / C-18 / C-19 / C-20 / C-21 / C-22 / C-23 / C-24

Ten criteria form a complete null-CE closure chain spanning recording, enforcement,
collection, co-activation, pre-commitment, audit, and structural robustness:

| Criterion | Role | What it closes |
|-----------|------|----------------|
| C-14 | Recording | Null CE must be named, not elided |
| C-16 | Escalation | Null CE must trigger adversarial review |
| C-17 | Consequence | Null CE must cap confidence mechanically |
| C-18 | Co-activation | C-16 and C-17 must fire together in the same output |
| C-19 | Pre-commitment | The full protocol must be declared as invariant before Stage 0 |
| C-20 | Accumulation | Null results must accumulate per stage with protocol reference |
| C-21 | Handoff echo | Co-activation outcome must propagate into the handoff artifact |
| C-22 | Registry trace | Invariant registry confirmation must appear as a distinct gate field |
| C-23 | Campaign outcome | Campaign state readable as a direct boolean without dual-lock inference |
| C-24 | Role separation | Dual attestation drift-resistant by construction, not by instruction |

The null-CE severity stack is unchanged from v7 and v8.

---

## Handoff Contract Chain: C-25 / C-26 / C-27 / C-28

Four criteria form a complete handoff contract integrity chain spanning annotation,
pre-commitment, independence proof, and symmetric proof:

| Criterion | Role | What it closes |
|-----------|------|----------------|
| C-25 | Derivation annotation | Every handoff field labeled with its upstream source; unlabeled field = format error |
| C-26 | Schema pre-commitment | Complete field+source contract locked at CAMPAIGN OPEN; compliance verified at synthesis |
| C-27 | Independence path chain | `incumbent_defense_closed` derivation includes explicit chain proving no path through dual-lock |
| C-28 | Symmetric path chain | Both lock fields carry full chains; `co_activation_confirmed` chain proves positive derivation through dual-lock and independence from campaign-outcome path |

C-25 makes the handoff auditable at field level. C-26 makes the schema contract auditable
from session open. C-27 makes the independence claim on `incumbent_defense_closed`
verifiable, not merely asserted by field separation. C-28 closes the asymmetry: C-27
proves where `incumbent_defense_closed` does NOT come from; C-28 requires `co_activation_confirmed`
to also prove where it DOES come from — making both directions of the mutual independence
claim simultaneously verifiable.

---

## Contract Enforcement Symmetry: C-29 / C-30

Two criteria complete the v9 extension by applying the per-stage accumulation and
pre-committed invariant disciplines — previously established for null-CE events
(C-19/C-20) — to schema integrity and annotation enforcement:

| Criterion | Extends | What it closes |
|-----------|---------|----------------|
| C-29 | C-20 + C-26 | Schema compliance monitored per stage; drift detectable before synthesis |
| C-30 | C-19 + C-25 | Derivation annotation rule declared as session invariant; enforcement pre-committed, not reactive |

C-29 applies the C-20 accumulation model to schema integrity: rather than a single
terminal compliance check, schema population is counted at each evidence stage, making
drift visible in real time. C-30 applies the C-19 invariant model to the annotation
requirement: rather than a synthesis-stage enforcement rule, the DERIVATION ANNOTATION
RULE is a named session invariant — pre-registered before Stage 0, immune to
synthesis-time suppression. Together, C-29 and C-30 make the handoff contract chain as
structurally pre-committed as the null-CE severity stack.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-15 | Initial rubric, 10 criteria (5 essential, 3 recommended, 2 aspirational), max 100 |
| v2 | 2026-03-15 | Add C-11, C-12, C-13 from Round 1 excellence signals; rebalance weights: essential 10 pts, recommended 10 pts, aspirational 4 pts; max unchanged at 100 |
| v3 | 2026-03-15 | Add C-14, C-15 from Round 2 excellence signals; max rises to 108; golden threshold unchanged at 80 |
| v4 | 2026-03-15 | Add C-16, C-17 from Round 3 excellence signals; max rises to 116; golden threshold unchanged at 80 |
| v5 | 2026-03-15 | Add C-18, C-19 from Round 4 excellence signals; max rises to 124; golden threshold unchanged at 80 |
| v6 | 2026-03-15 | Add C-20, C-21, C-22 from Round 5 excellence signals; max rises to 136; golden threshold unchanged at 80 |
| v7 | 2026-03-15 | Add C-23, C-24 from Round 6 excellence signals; max rises to 144; golden threshold unchanged at 80 |
| v8 | 2026-03-15 | Add C-25, C-26, C-27 from Round 8 excellence signals; max rises to 156; golden threshold unchanged at 80 |
| v9 | 2026-03-15 | Add C-28, C-29, C-30 from Round 9 excellence signals; max rises to 168; golden threshold unchanged at 80 |

### Weight change note (v8 -> v9)

v8: max 156, aspirational 19 criteria x 4 pts = 76 pts.
v9: max 168, aspirational 22 criteria x 4 pts = 88 pts.

Essential and recommended weights are unchanged. Max rises by 12 to accommodate three
new aspirational criteria at full 4-pt weight. The golden threshold holds at 80, which
equals essential + recommended exactly — the same structural relationship as all prior
versions.

### New criteria source table (v9)

| ID | Source | Pattern |
|----|--------|---------|
| C-28 | V-02 (Round 9) | Symmetric independence path chain on both lock fields. C-27 requires `positive_derivation:` + `independence_chain:` only on `incumbent_defense_closed`. V-02 extends this to `co_activation_confirmed` — each field carries a full bidirectional chain, making the mutual independence of C-23 verifiable from both directions simultaneously rather than only from the `incumbent_defense_closed` side. |
| C-29 | V-03 (Round 9) | Per-stage schema integrity counts. C-20 requires null tallies per stage. V-03 pairs each NULL TALLY NOTE with a SCHEMA INTEGRITY NOTE counting the cumulative declared fields populated so far and confirming zero additions, omissions, or source mismatches — applying the C-20 accumulation discipline to schema compliance so that drift is detectable per stage rather than only at the terminal synthesis check. |
| C-30 | V-04 (Round 9) | Derivation annotation rule pre-committed as session invariant. C-25 requires a DERIVATION ANNOTATION RULE at synthesis with "unlabeled field = format error". V-04 elevates this to a named SESSION INVARIANT at CAMPAIGN OPEN (alongside the null-CE invariants of C-19) with "cannot be modified or bypassed" language — applying the C-19 invariant discipline to annotation enforcement so the requirement is pre-registered before Stage 0, not reactive at synthesis time. |
