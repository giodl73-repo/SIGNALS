# prove-topic Rubric — v13

## Overview

This rubric scores the `prove-topic` skill, which orchestrates five sub-skills to carry
a hypothesis from scout-loaded context through evidence collection, synthesis, and handoff
to `topic-story`. The skill is evaluated against thirty-nine criteria spanning essential
structure, recommended traceability, and aspirational evidence integrity.

---

## Essential Criteria (10 pts each)

### C-01 — All stages present

PASS: The response includes all five evidence stages (Stage 1 hypothesis, Stage 2 web
search, Stage 3 interview, Stage 4 prototype, Stage 5 synthesis) plus a gate block
(GATE S), role definitions (ROLE A / ROLE B or equivalent), and a CAMPAIGN OPEN
preamble. Any missing stage is a FAIL.

### C-02 — Scout artifact loaded

PASS: The response explicitly loads a named scout artifact (e.g.,
`{topic}-scout-record-{date}.md`) before hypothesis formation — typically assigned to
ROLE B or an equivalent stage-entry function. A hypothesis formed from general knowledge
without referencing a named scout artifact is a FAIL.

### C-03 — Progressive artifact writes

PASS: At least one write instruction is issued per stage, producing a distinct artifact
at each step (hypothesis, web-search summary, interview summary, prototype result,
synthesis brief). A response that collects all evidence then writes a single artifact at
Stage 5 is a FAIL.

### C-04 — Synthesis readiness signal

PASS: The synthesis stage (Stage 5) includes an explicit statement confirming that the
evidence brief is ready for the downstream consumer — e.g., "Evidence brief ready for
topic-story." A synthesis that ends without a readiness signal or named next step is a
PARTIAL (5 pts).

### C-05 — Artifact naming consistent

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
both directions simultaneously. A variation can satisfy C-27 completely —
`incumbent_defense_closed` carries a full `positive_derivation:` + `independence_chain:`
— and still fail C-28 if `co_activation_confirmed` is present and correctly valued (C-21
PASS) but its derivation source is unannotated or incompletely chained.

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

### C-31 — Per-stage CE verdict as owned schema field

*Excellence signal from V-01 (Round 10).*

PASS: The pre-committed handoff schema (required by C-26) includes named per-stage CE
verdict fields — one per evidence stage (e.g., `s2_ce_verdict`, `s3_ce_verdict`,
`s4_ce_verdict`) — declared with a CE VERDICT OWNERSHIP TABLE at CAMPAIGN OPEN assigning
each field to its owning stage. The `null_tally_final` derivation annotation (required by
C-25) must reference all named CE verdict fields explicitly in its formula rather than
treating the tally as an opaque running count. C-25 and C-26 must both pass. A schema
that includes `null_tally_final` without naming per-stage CE verdict fields as owned
schema members satisfies C-26 but not C-31. PARTIAL (2 pts) if per-stage CE verdict
fields appear in the schema but the `null_tally_final` derivation formula does not name
them explicitly. FAIL if C-26 is FAIL. V-01's `s2_ce_verdict`, `s3_ce_verdict`,
`s4_ce_verdict` as OWNED FIELDs with CE VERDICT OWNERSHIP TABLE at CAMPAIGN OPEN, and
`null_tally_final` derivation formula listing all three named fields, is the exemplar.

Failure mode addressed: C-20 requires per-stage null tallies; C-26 pre-commits the
handoff schema. Neither requires CE verdicts to be named schema fields with declared
per-stage ownership. A `null_tally_final` computed at synthesis from an unstructured
running count satisfies both — it does not expose which stage contributed which verdict,
making per-stage CE audit require full session replay. C-31 makes each stage's CE verdict
a named handoff-schema field with declared ownership, so that `null_tally_final`'s
derivation chain names its inputs explicitly rather than treating the tally as an opaque
counter. A variation can satisfy C-20 (per-stage null tallies), C-26 (schema
pre-committed), and C-25 (all fields labeled at synthesis) and still fail C-31: the null
tally accumulates correctly per stage, the schema is locked at CAMPAIGN OPEN, and every
handoff field carries a derivation label — but no per-stage CE verdict field is declared
as an owned schema member, and `null_tally_final`'s formula does not name its per-stage
sources.

### C-32 — Counter-hypothesis declared at Stage 1 and closed at synthesis

*Excellence signal from V-02 (Round 10).*

PASS: A `counter_hypothesis:` field is required in the hypothesis artifact (Stage 1),
naming one or more competing explanations or alternative outcomes that could falsify the
primary hypothesis. The synthesis (Stage 5) includes a COUNTER-HYPOTHESIS RESOLUTION
section with an explicit verdict — one of REFUTED, PARTIALLY REFUTED, or OPEN RISK —
for each declared counter-hypothesis. An OPEN RISK verdict must mechanically reduce
confidence one tier, applying the same capping rule as C-17 applies to null CE. C-14 and
C-17 must both pass. A hypothesis artifact without a `counter_hypothesis:` field satisfies
C-01 but not C-32. A synthesis with a counter-hypothesis section but no structured
per-verdict classification (REFUTED / PARTIALLY REFUTED / OPEN RISK) is a PARTIAL (2 pts).
FAIL if C-17 is FAIL (no confidence-capping mechanism — OPEN RISK cannot apply a
mechanical cap). V-02's `counter_hypothesis:` at Stage 1 and COUNTER-HYPOTHESIS
RESOLUTION section at Stage 5 with three structured verdicts, OPEN RISK reducing
confidence one tier, is the exemplar.

Failure mode addressed: C-14 requires counter-evidence to be a mandatory section at
synthesis with a null fallback; C-17 mechanically caps confidence on null CE. Neither
requires the counter-argument to be named and owned from the moment of hypothesis
formation. Without a declared `counter_hypothesis:` at Stage 1, the synthesis
counter-evidence section is assembled from whatever disconfirming evidence happened to
surface during collection — not from a pre-declared opposing claim. C-32 pre-commits
the counter-hypothesis at Stage 1 alongside the primary hypothesis, so that the
resolution section is closing a declared challenge rather than summarizing incidental
contrary evidence. The three-verdict classification (REFUTED, PARTIALLY REFUTED, OPEN
RISK) makes the outcome actionable: OPEN RISK is not merely acknowledged but mechanically
propagated to the confidence level. A variation can satisfy C-14 (mandatory section) and
C-17 (mechanical cap on null CE) and still fail C-32: the synthesis has a counter-evidence
section and applies a confidence cap, but no counter-hypothesis was declared at Stage 1
and no structured verdict classification is present.

### C-33 — Null tally chain reconstructed in ATOMIC DUAL-LOCK

*Excellence signal from V-03 (Round 10).*

PASS: The ATOMIC DUAL-LOCK block at synthesis (required by C-18) includes a NULL TALLY
CHAIN reconstruction — a named sub-block that explicitly restates the per-stage null
accumulation sequence (e.g., S2→N, S3→N, S4→N = null_tally_final) and cross-checks the
terminal `null_tally_final` value against the Stage 4 running count, producing an explicit
match/mismatch verdict. A NULL TALLY CHAIN RULE must be declared at CAMPAIGN OPEN
requiring this reconstruction. C-18 and C-20 must both pass. An ATOMIC DUAL-LOCK that
applies both constraints without a null chain reconstruction satisfies C-18 but not C-33.
PARTIAL (2 pts) if the chain reconstruction is present inside the ATOMIC DUAL-LOCK but
the cross-check against Stage 4's running count is absent. FAIL if C-18 is FAIL or C-20
is FAIL. V-03's NULL TALLY CHAIN RULE at CAMPAIGN OPEN and NULL TALLY CHAIN block inside
the ATOMIC DUAL-LOCK reconstructing S2→N, S3→N, S4→N = null_tally_final with a Stage 4
cross-check is the exemplar.

Failure mode addressed: C-20 requires null results to accumulate per stage with protocol
reference. C-18 requires both locks to fire atomically at synthesis. C-21 carries the
co-activation outcome into the handoff. None of these require the per-stage accumulation
to be structurally echoed inside the dual-lock itself — the ATOMIC DUAL-LOCK fires from
the synthesis-level `null_tally_final` without tracing the chain that produced it. Without
a reconstruction, a dual-lock that fires on an incorrect `null_tally_final` (due to tally
error or accumulation drift between stages) cannot be audited from the dual-lock block
alone; detecting the discrepancy requires cross-referencing all per-stage tally notes.
C-33 makes the accumulation chain a structural component of the locking mechanism: the
lock fires on a `null_tally_final` that is immediately cross-checkable against the
per-stage record. A variation can satisfy C-18 (dual-lock fires), C-20 (per-stage tally
notes), and C-21 (co-activation in handoff) and still fail C-33: the dual-lock block
applies both constraints and co-activation is confirmed, but the null tally chain is not
reconstructed inside the dual-lock and no cross-check against Stage 4 exists.

### C-34 — Named per-stage incumbent check block at each evidence stage with Stage 4 displacement verdict

*Excellence signal from V-01 (Round 11).*

PASS: Each evidence stage (Stages 2, 3, and 4) includes a named INCUMBENT CHECK section
or equivalent dedicated structural block that explicitly references the incumbent loaded
at CAMPAIGN OPEN and poses a stage-specific question about displacement evidence. Stage
4's INCUMBENT CHECK must explicitly ask whether the accumulated evidence "makes a credible
case for displacing {incumbent}" — naming the incumbent by placeholder and requiring a
Yes / No / Pending answer at that stage. C-12 must pass (incumbent anchored at CAMPAIGN
OPEN). A design satisfying C-12 (incumbent named at CAMPAIGN OPEN and present somewhere
in each stage) but without a named INCUMBENT CHECK block at every evidence stage is a
PARTIAL (2 pts). PARTIAL also applies when Stage 4 includes an INCUMBENT CHECK but does
not include the displacement verdict question. FAIL if C-12 is FAIL. V-01's named
INCUMBENT CHECK block at Stages 2, 3, and 4, with Stage 4 asking "does evidence make a
credible case for displacing {incumbent}?" and requiring an explicit answer, is the
exemplar.

Failure mode addressed: C-12 requires the incumbent to be anchored at session open and
explicitly referenced at each evidence stage. It does not require the per-stage references
to take a structurally named form or to include a stage-specific displacement verdict
question. A design can satisfy C-12 by tracking the incumbent implicitly through a
CE-RELEVANT column (V-02: C-12 PARTIAL, C-34 FAIL) or by naming it in Stage 2 ENTER
only and omitting it from Stages 3 and 4 WORK sections (V-03: C-12 PARTIAL, C-34 FAIL).
In both cases, the comparator exists in the campaign but is not consistently visible as
a named structural decision point at each evidence stage — making per-stage incumbent
reasoning traceable only by searching stage prose rather than reading a dedicated block.
The named INCUMBENT CHECK block makes the comparator a first-class structural presence at
each stage, and Stage 4's displacement verdict forces an explicit pre-synthesis answer to
the campaign's core question before synthesis begins. A variation can satisfy C-12
completely — incumbent anchored at CAMPAIGN OPEN, referenced in each stage's body —
and still fail C-34: all stage references exist but none is a named INCUMBENT CHECK
block, and Stage 4 produces no displacement verdict question.

### C-35 — Gate-structural incumbent threat role

*Excellence signal from V-01 (Round 12).*

PASS: CAMPAIGN OPEN defines a dedicated ROLE C (INCUMBENT THREAT ANALYST or equivalent)
whose analysis produces a locked field (e.g., `incumbent_threat_locked`) that GATE S
requires for clearance — alongside `gate_s_cleared` and `invariant_registry_confirmed`
— before Stage 1 opens. The INCUMBENT CHECK blocks at each evidence stage must cite ROLE
C fields (e.g., `incumbent_name`, `incumbent_strength`, `incumbent_vulnerability`) as
their structural origin rather than referencing only the incumbent named in the preamble.
C-34 must pass. A design satisfying C-34 (named INCUMBENT CHECK blocks at all evidence
stages with Stage 4 displacement verdict) but without a gate-enforcing role structure is a
PARTIAL (2 pts). PARTIAL also applies if ROLE C is defined but `incumbent_threat_locked`
is not listed as a GATE S requirement. FAIL if C-34 is FAIL. V-01's ROLE C producing
`incumbent_threat_locked` as a GATE S field, with INCUMBENT CHECK blocks at Stages 2–4
citing ROLE C fields as structural origin, is the exemplar.

Failure mode addressed: C-34 requires named INCUMBENT CHECK blocks at Stages 2, 3, and
4 with a Stage 4 displacement verdict. It does not require the blocks to be owned by a
pre-committed structural role or gated at session entry. A design can satisfy C-34
completely — named INCUMBENT CHECK blocks at all three stages, Stage 4 displacement
verdict — while keeping the incumbent analysis as an open preamble instruction: no
dedicated role, no gate enforcement, no locked field. Removing or simplifying the blocks
produces a C-34 FAIL, but no structural gap appears in the gate check — the gate can
clear without any evidence of incumbent analysis. C-35 makes losing the incumbent analysis
create an immediately auditable gate-level gap: ROLE C's `incumbent_threat_locked` field
is a GATE S requirement, so any design that lacks ROLE C cannot open Stage 1 without a
visible gate failure. A variation can satisfy C-34 completely — named INCUMBENT CHECK
blocks at all three stages with Stage 4 displacement verdict — and still fail C-35: the
blocks exist and are structurally present, but the incumbent analysis lives in the
CAMPAIGN OPEN preamble rather than as a gated role output with a gate-clearing field.

### C-36 — Phrasing register pre-committed as session invariant

*Excellence signal from V-04 (Round 12).*

PASS: A named SESSION INVARIANT (e.g., SESSION INVARIANT D or the next available
invariant slot) at CAMPAIGN OPEN declares a consistent formal vocabulary register for the
campaign — specifying the required phrasing template for INCUMBENT CHECK
displacement-question formulations across Stages 2, 3, and 4. The register must use
invariant language ("cannot be modified or bypassed", "binding for the full session", or
equivalent). C-19 and C-34 must both pass. A phrasing register noted at CAMPAIGN OPEN
without invariant naming or "cannot be bypassed" language is a PARTIAL (2 pts). FAIL if
C-19 is FAIL (no SESSION INVARIANT block) or C-34 is FAIL (no INCUMBENT CHECK blocks for
the register to govern). V-04's SESSION INVARIANT D (or equivalent) declaring a formal
vocabulary register alongside SESSION INVARIANTs A, B, and C at CAMPAIGN OPEN, ensuring
consistent displacement-question phrasing across all evidence stages, is the exemplar.

Failure mode addressed: C-34 requires named INCUMBENT CHECK blocks with a displacement
verdict question at Stage 4. C-19 pre-commits the null-CE protocol and cap rule as
session invariants. C-30 pre-commits the derivation annotation rule as a session
invariant. None of these require the phrasing of displacement questions across stages to
be consistent or pre-committed. Without a declared register, INCUMBENT CHECK blocks can
use different question formulations at Stages 2, 3, and 4 — varying enough between runs
or stages that per-stage audits are comparing non-equivalent questions. A phrasing
register declared without invariant language can be overridden at synthesis time or
silently ignored mid-session; invariant framing makes deviations from the declared
template format errors rather than style choices. A variation can satisfy C-34 (named
INCUMBENT CHECK blocks, Stage 4 displacement verdict) and C-19 (session invariants
A/B/C pre-committed) and still fail C-36: the INCUMBENT CHECK blocks exist and the
null-CE invariants are registered, but no invariant governs the vocabulary or phrasing
of the displacement questions themselves — inter-stage consistency is informal, not
structurally enforced.

### C-37 — Gate chain role ordering encodes dependency sequence

*Excellence signal from V-01/V-05 (Round 13).*

PASS: Roles at CAMPAIGN OPEN are declared in execution-dependency order — ROLE C
(incumbent threat analysis) first, followed by ROLE B (scout load), followed by ROLE A
(hypothesis formation) — so that the clearance sequence C→B→A is readable from the role
declaration order itself. A ROLE OWNERSHIP TABLE (or equivalent named construct) that
lists ROLE C as its first row, with ROLE B and ROLE A following, satisfies this criterion.
C-35 must pass. A design satisfying C-35 — ROLE C exists and produces `incumbent_threat_locked`
as a GATE S field — but with roles declared in a different order (e.g., B, A, C or A, B,
C) is a PARTIAL (2 pts). FAIL if C-35 is FAIL. V-01's C→B→A role declaration sequence at
CAMPAIGN OPEN and V-05's ROLE OWNERSHIP TABLE with ROLE C as the first row — making the
dependency chain readable before the gate block is reached — are the exemplars.

Failure mode addressed: C-35 requires ROLE C to produce `incumbent_threat_locked` as a
GATE S field, making absent incumbent analysis an auditable gate gap. It does not require
the roles to be declared in an order that encodes the logical execution dependency. A
design satisfying C-35 can list ROLE B first, then ROLE A, then ROLE C — all roles are
present, the gate field is correctly assigned, and the gate clears correctly — but the
declaration order implies a different execution sequence than what the gate enforces.
C-37 encodes the dependency chain into the role declaration order: ROLE C first signals
that incumbent threat analysis is logically prior to scout artifact loading, which is
prior to hypothesis formation. The C→B→A ordering makes the dependency semantically
load-bearing — you cannot meaningfully load a scout artifact until you have named what
it must help displace. A variation can satisfy C-35 completely — ROLE C defined,
`incumbent_threat_locked` gating Stage 1, INCUMBENT CHECK blocks citing ROLE C fields —
and still fail C-37: all roles exist with correct gate semantics, but the declaration
order does not encode the C→B→A execution dependency.

### C-38 — Phrasing template printed verbatim at point of use

*Excellence signal from V-04 (Round 13).*

PASS: The SESSION INVARIANT D phrasing template (required by C-36) is printed verbatim
immediately before or within each INCUMBENT CHECK block at Stages 2, 3, and 4 — with
variable slots identified as bracketed tokens (e.g., `[evidence_type]`, `[incumbent]`).
A TEMPLATE ECHO RULE must be declared at CAMPAIGN OPEN requiring verbatim echo at each
point of use. C-36 must pass. A design satisfying C-36 — SESSION INVARIANT D declared
at CAMPAIGN OPEN with invariant language — but referencing the invariant by name only at
each INCUMBENT CHECK ("apply SESSION INVARIANT D template") without printing the template
verbatim is a PARTIAL (2 pts): any deviation is formally a format error, but detecting
it requires backward lookup to the CAMPAIGN OPEN registry. FAIL if C-36 is FAIL. V-04's
pattern — "Template (SESSION INVARIANT D, Stage N — verbatim, fill bracketed slots
only):" printed immediately above each INCUMBENT CHECK before the stage work begins — is
the exemplar.

Failure mode addressed: C-36 requires SESSION INVARIANT D to be declared at CAMPAIGN
OPEN with invariant language, making phrasing deviations format errors by rule. It does
not require the declared template to be co-located with the execution point. A builder
satisfying C-36 declares the template once at CAMPAIGN OPEN and references it by name
at each INCUMBENT CHECK — any deviation is formally a format error, but identifying it
requires comparing the stage question to the registry entry. C-38 requires the template
to be physically present at the execution point so that deviation is immediately visible
before it happens rather than detectable only by backward reference. A variation can
satisfy C-36 — SESSION INVARIANT D declared with invariant language, inter-stage
consistency structurally enforced — and still fail C-38: the template is in the registry
and the invariant is binding, but each INCUMBENT CHECK cites the invariant by name
without printing the template, making per-stage compliance require registry lookup rather
than forward inspection.

### C-39 — Dual-site template enforcement: gate obligation and execution obligation

*Excellence signal from V-05 (Round 13).*

PASS: The SESSION INVARIANT D phrasing template appears at both structural sites for each
evidence stage — in the ENTRY CONDITIONS for Stages 2, 3, and 4 (gate obligation: template
confirmed before entering the stage) AND in the INCUMBENT CHECK block headers or preamble
(execution obligation: template printed at the moment of use). C-38 must pass. A design
satisfying C-38 — template printed at execution point (INCUMBENT CHECK block) — but
without template echo in ENTRY CONDITIONS is a PARTIAL (2 pts): the execution obligation
is present, but stage entry is not conditioned on template confirmation. PARTIAL also
applies if the template appears in ENTRY CONDITIONS but not in INCUMBENT CHECK block
headers. FAIL if C-38 is FAIL or C-36 is FAIL. V-05's full template echoed in ENTRY
CONDITIONS for Stages 2, 3, and 4 AND in INCUMBENT CHECK TABLE headers — providing
gate-level enforcement before entry and execution-level enforcement at the point of use
— is the exemplar.

Failure mode addressed: C-38 requires the template to be co-located with the execution
point (INCUMBENT CHECK block), making deviation immediately visible at the moment of
execution. It does not require stage entry to be conditioned on template confirmation.
A builder satisfying C-38 can enter Stage N and reach the INCUMBENT CHECK without the
phrasing template having been confirmed at the entry gate — template awareness is required
at execution, not at entry, leaving a window between stage entry and INCUMBENT CHECK
execution where the obligation is not structurally visible. C-39 adds a gate obligation:
ENTRY CONDITIONS for each evidence stage must include the template, so that template
confirmation is required for stage entry AND again at execution — two independent
structural sites each enforcing the same phrasing contract. A variation can satisfy C-38
completely — template printed verbatim above each INCUMBENT CHECK — and still fail C-39:
the template is co-located with execution, but ENTRY CONDITIONS for Stages 2, 3, and 4
do not include the template, leaving stage entry unconditioned on phrasing confirmation.

---

## Scoring

### Weights

| Tier | Points | Criteria | Per criterion |
|------|--------|----------|---------------|
| Essential | 50 | 5 | 10 pts |
| Recommended | 30 | 3 | 10 pts |
| Aspirational | 124 | 31 | 4 pts |
| **Max composite** | **204** | | |

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

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 25/25 pass → 100
- **Composite = 180** — Golden (v10 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 26/26 pass → 104
- **Composite = 184** — Golden (v11 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 28/28 pass → 112
- **Composite = 192** — Golden (v12 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 31/31 pass → 124
- **Composite = 204** — Golden (v13 ceiling)

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

Targets the failure modes unique to orchestration. The thirty-one criteria form six
pairs, one triple, one quartet, one quintet, one sextet, and four standalones:

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
  still fail all three.

- **C-31, C-32, C-33**: Evidence chain integrity (added v10). Each extends the evidence
  audit chain from accumulated observations to structurally owned, pre-declared, and
  cross-verified records. C-31 extends C-20 and C-26 by elevating per-stage CE verdicts
  from unstructured running-count contributions to named owned schema fields with a
  declared CE VERDICT OWNERSHIP TABLE — making `null_tally_final`'s derivation formula
  chain-complete. C-32 extends C-14 and C-17 by pre-declaring the counter-hypothesis at
  Stage 1 alongside the primary hypothesis, so that the synthesis resolution section
  closes a declared challenge with a structured three-verdict classification, OPEN RISK
  mechanically propagating to the confidence level. C-33 extends C-18 and C-20 by
  reconstructing the per-stage null accumulation chain inside the ATOMIC DUAL-LOCK itself
  with a Stage 4 cross-check — making the lock's input auditable from the dual-lock block
  without cross-referencing all per-stage notes. A variation can satisfy the full v9
  stack (168/168) and still fail all three.

- **C-34** (standalone, added v11): Comparator tracking depth. Extends C-12 from
  incumbent presence at each stage to named structural visibility at each stage. C-12
  requires the incumbent to be anchored at CAMPAIGN OPEN and referenced in each evidence
  stage; C-34 requires each such reference to be a named INCUMBENT CHECK block — not an
  implicit column or incidental prose mention — and Stage 4's block to include an explicit
  displacement verdict question. A variation can satisfy C-12 completely — incumbent
  anchored at CAMPAIGN OPEN, referenced throughout — and still fail C-34: per-stage
  references exist but none takes the form of a named, dedicated check block, and no
  Stage 4 displacement verdict is required before synthesis begins.

- **C-35, C-36, C-37, C-38, C-39** (added v12–v13): Comparator gate enforcement,
  phrasing invariance, and phrasing delivery. Each extends the comparator tracking
  discipline from named structural visibility (C-34) through gate-enforced ownership
  (C-35), pre-committed vocabulary (C-36), dependency-ordered role declaration (C-37),
  template co-location at execution (C-38), and dual-site gate-plus-execution enforcement
  (C-39). C-35 makes absent incumbent analysis an auditable gate gap via ROLE C's locked
  field. C-36 declares the phrasing template as a session invariant alongside the
  null-CE invariants. C-37 encodes the C→B→A execution dependency into the role
  declaration sequence, making the logical ordering readable without reaching the gate
  block. C-38 requires the declared template to be printed verbatim at each point of
  execution — deviation is visible before it happens, not only by backward registry
  lookup. C-39 adds a gate obligation alongside the execution obligation: ENTRY
  CONDITIONS for each evidence stage must include the template, so that phrasing
  confirmation is structurally required at stage entry and again at execution. A variation
  can satisfy C-34 through C-36 completely and still fail all three additions: named
  INCUMBENT CHECK blocks at all stages with Stage 4 verdict (C-34 PASS), ROLE C owning
  a gate field (C-35 PASS), SESSION INVARIANT D declared with invariant language (C-36
  PASS) — but roles declared in annotation order rather than dependency order (C-37 FAIL),
  invariant referenced by name rather than printed at execution (C-38 FAIL), and templates
  absent from ENTRY CONDITIONS (C-39 FAIL).

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

The null-CE severity stack is unchanged from v7 through v13.

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
proves where `incumbent_defense_closed` does NOT come from; C-28 requires
`co_activation_confirmed` to also prove where it DOES come from — making both directions
of the mutual independence claim simultaneously verifiable.

The handoff contract chain is unchanged from v9 through v13.

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

The contract enforcement symmetry section is unchanged from v9 through v13.

---

## Evidence Chain Integrity: C-31 / C-32 / C-33

Three criteria extend the evidence audit chain from accumulated observations to
structurally owned, pre-declared, and cross-verified records:

| Criterion | Extends | What it closes |
|-----------|---------|----------------|
| C-31 | C-20 + C-26 | Per-stage CE verdicts as owned schema fields; `null_tally_final` derivation formula chain-complete |
| C-32 | C-14 + C-17 | Counter-hypothesis pre-declared at Stage 1; synthesis closes it with structured verdict; OPEN RISK mechanically caps confidence |
| C-33 | C-18 + C-20 | Null tally chain reconstructed inside ATOMIC DUAL-LOCK with Stage 4 cross-check; lock input auditable in place |

C-31 closes the gap that C-20 and C-26 leave open: per-stage null tallies accumulate and
the schema is locked, but the individual stage verdicts that feed `null_tally_final` are
not named schema members — the tally is an opaque counter. C-31 requires each stage to
own a named verdict field so that `null_tally_final`'s derivation formula is
chain-complete. C-32 closes the gap that C-14 and C-17 leave open: counter-evidence is
mandatory and confidence is capped on null, but the competing explanation is assembled
reactively from whatever surfaced — not pre-declared alongside the primary hypothesis.
C-32 requires the counter-hypothesis to be a named field at Stage 1 so that synthesis
closes a declared challenge, not an emergent one. C-33 closes the gap that C-18 and C-20
leave open: both locks fire and per-stage tallies exist, but the ATOMIC DUAL-LOCK fires
on a terminal value whose chain it does not reconstruct — tally errors are undetectable
from the dual-lock block alone. C-33 requires the per-stage chain to be echoed inside the
ATOMIC DUAL-LOCK with a Stage 4 cross-check, making the lock's input auditable in place.

The evidence chain integrity section is unchanged from v10 through v13.

---

## Comparator Tracking Depth: C-34 / C-35 / C-36 / C-37 / C-38 / C-39

Six criteria form a complete comparator tracking depth chain spanning named structural
visibility, gate-enforced ownership, pre-committed phrasing invariance, dependency-ordered
role declaration, template co-location at execution, and dual-site gate-plus-execution
enforcement:

| Criterion | Extends | What it closes |
|-----------|---------|----------------|
| C-34 | C-12 | Named INCUMBENT CHECK block required at Stages 2, 3, and 4; Stage 4 block includes explicit displacement verdict question before synthesis |
| C-35 | C-34 | Dedicated ROLE C owns `incumbent_threat_locked` as GATE S field; INCUMBENT CHECK blocks cite ROLE C fields as structural origin; absent role = auditable gate gap |
| C-36 | C-19 + C-34 | Phrasing register pre-committed as named SESSION INVARIANT; displacement-question vocabulary locked at CAMPAIGN OPEN; inter-stage phrasing deviation = format error |
| C-37 | C-35 | Roles declared in C→B→A execution-dependency order; dependency chain readable from role declaration sequence without reaching gate block |
| C-38 | C-36 | SESSION INVARIANT D template printed verbatim at each INCUMBENT CHECK execution point; deviation visible before it happens, not only by registry lookup |
| C-39 | C-38 | Template appears at both gate site (ENTRY CONDITIONS) and execution site (INCUMBENT CHECK headers); phrasing confirmed at stage entry AND at moment of use |

C-34 establishes the per-stage structural form: named INCUMBENT CHECK blocks at each
evidence stage make the comparator a first-class decision point rather than an implicit
tracking artifact. C-35 closes the gate-level gap that C-34 leaves open: named blocks
can still live in an open preamble without a structural owner — removing them degrades
output quality but leaves no gate failure. ROLE C's `incumbent_threat_locked` field makes
the comparator analysis gate-mandatory, creating an auditable structural gap on omission.
C-36 closes the vocabulary gap that C-34 and C-35 leave open: the displacement question
is now structurally present (C-34) and gate-enforced (C-35), but its phrasing can vary
across stages and runs without an invariant to enforce it. SESSION INVARIANT D makes the
question template a pre-committed session property — deviations are format errors, not
style choices. C-37 closes the dependency-ordering gap that C-35 leaves open: ROLE C
exists and gates Stage 1, but the role declarations may appear in any order — the
C→B→A dependency is enforced by the gate, not visible from the role sequence itself.
Declaring roles in C→B→A order makes the execution dependency readable before the gate
block is reached, encoding it as structural convention rather than an implicit rule.
C-38 closes the detection-proximity gap that C-36 leaves open: the phrasing template is
declared as a session invariant, but a builder referencing it by name at each INCUMBENT
CHECK forces deviation detection by backward lookup — the template is not visible at
the point of use. Printing the template verbatim above each execution point makes
deviation immediately visible before it happens. C-39 closes the single-site gap that
C-38 leaves open: the template is printed at execution (INCUMBENT CHECK block), but
stage entry is not conditioned on template confirmation — a builder can enter a stage
without the phrasing obligation being reinforced at the gate. ENTRY CONDITIONS for each
evidence stage must also include the template, so that phrasing is confirmed at two
independent structural sites: the entry gate and the execution point.

The comparator tracking depth section extends v13.

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
| v10 | 2026-03-16 | Add C-31, C-32, C-33 from Round 10 excellence signals; max rises to 180; golden threshold unchanged at 80 |
| v11 | 2026-03-16 | Add C-34 from Round 11 excellence signals; max rises to 184; golden threshold unchanged at 80 |
| v12 | 2026-03-16 | Add C-35, C-36 from Round 12 excellence signals; max rises to 192; golden threshold unchanged at 80; Comparator Tracking Depth section expands from C-34 standalone to C-34/C-35/C-36 chain |
| v13 | 2026-03-16 | Add C-37, C-38, C-39 from Round 13 excellence signals; max rises to 204; golden threshold unchanged at 80; Comparator Tracking Depth section extends to C-34 through C-39 chain |
