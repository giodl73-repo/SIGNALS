v7 is written. Here's the summary:

**Two new criteria extracted from Round 6 excellence signals (V-05):**

| ID | Role in stack | Pattern |
|----|--------------|---------|
| C-23 | Campaign outcome | `incumbent_defense_closed` boolean in handoff — independent of `co_activation_confirmed`. Downstream consumers read campaign state directly without dual-lock inference. Extends C-21 from presence to independence. |
| C-24 | Role separation | Two blocking roles, each owning one attestation field. Dropping either role is an auditable structural gap. Extends C-22 from instruction-enforced to construction-enforced. |

**Weight outcome:** Max rises 136 → 144. Aspirational expands to 16 criteria × 4 pts = 64 pts. Golden threshold unchanged at 80.

**Severity stack extended to 10:** C-14 (recording) → C-16 (escalation) → C-17 (consequence) → C-18 (co-activation) → C-19 (pre-commitment) → C-20 (accumulation) → C-21 (handoff echo) → C-22 (registry trace) → **C-23 (campaign outcome)** → **C-24 (role separation)**.

**The v6 ceiling (136/136) is no longer the ceiling.** A variation satisfying v6 can still fail both v7 criteria: handoff has `co_activation_confirmed` but no `incumbent_defense_closed` (C-23 FAIL); gate fields exist but share one structural origin (C-24 FAIL).
e one) before advancing. Stages that complete with no artifact instruction are a FAIL.

### C-04 — Final synthesis is terminal and complete

PASS: The synthesis stage is the last stage and contains a defined set of required sections
(minimum: findings, confidence level, handoff). Synthesis placed mid-sequence or missing
required fields is a FAIL.

### C-05 — Topic prefix consistent across all artifacts

PASS: Every artifact path referenced in the response starts with `{topic}-`. A prefix
defined once at session opening but not repeated in per-artifact write instructions is a
PARTIAL (5 pts). Per-artifact path naming in each write instruction is full PASS.

---

## Recommended Criteria (10 pts each)

### C-06 — Stage order enforced

PASS: The five sub-skills are presented in a fixed sequence with a forward-only constraint.
No mechanism to skip back, re-run stages in arbitrary order, or proceed without completing
the prior stage is a FAIL.

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

Failure mode addressed: variations that name a scout anchor but allow hypothesis formation
to proceed from general knowledge rather than the loaded artifact.

### C-12 — Thin-evidence comparator anchored at session open

*Excellence signal from V-04 (Round 1).*

PASS: A status-quo baseline or incumbent comparator is named at the session's opening —
before any evidence gathering — and explicitly referenced at each evidence stage. This
grounds any thin-evidence acknowledgment in a concrete alternative rather than an isolated
caveat. A comparator introduced only at Stage 4 or only in the synthesis is a PARTIAL
(2 pts). The pattern — "status-quo comparator at campaign opening → referenced at each
evidence stage → Warning+effect at Stage 4 traced to synthesis" — is the exemplar.

Failure mode addressed: C-09 partials where thin-evidence flags appear late and are not
connected to a pre-established baseline, making the confidence qualification untethered.

### C-13 — Per-artifact path enforcement on each write instruction

*Excellence signal from V-01 (Round 1).*

PASS: Every write instruction in the response names the full artifact path (e.g.,
`{topic}-hypothesis-{date}.md`), not just the topic prefix or a filename stem. A prefix
defined once at session opening without per-instruction path naming is a PARTIAL (2 pts).
This prevents prefix drift across sub-stages and multi-turn sessions.

Failure mode addressed: C-05 partials where a correctly-defined opening prefix drifts by
Stage 3–4 because individual write instructions do not restate it.

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

PASS: After GATE S clears, the hypothesis artifact or its frontmatter includes an explicit
field recording gate clearance (e.g., `gate_s_cleared: true`). This provides a traceable
record that the gate was checked — visible in the artifact itself, not only in the session
preamble. A GATE block with no artifact-level record of clearance satisfies C-11 but not
C-15. FAIL if C-11 is FAIL (no gate defined at all). PARTIAL (2 pts) if the gate clears
but clearance is recorded only in the session log, not in the hypothesis frontmatter.

Failure mode addressed: gate instructions that leave no trace in the artifact chain, making
it impossible to audit gate compliance from the artifact alone without replaying the full
session.

### C-16 — Null counter-evidence triggers adversarial escalation

*Excellence signal from V-01/V-02/V-03 (Round 3).*

PASS: When the synthesis counter-evidence section records a null result (no counter-evidence
gathered during the campaign), the response explicitly recommends adversarial review or an
equivalent challenge activity as a required next step — not as an optional aside. Recording
null without an escalation instruction is a PARTIAL (2 pts). The Round 3 pattern —
"null result recorded → adversarial review explicitly recommended" — is the exemplar.

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

PASS: When counter-evidence is null, the synthesis simultaneously applies both constraints:
promotion is blocked or escalated (C-16), and confidence is mechanically capped (C-17).
Both must be active in the same synthesis output — not satisfied in separate conditional
branches where one could fire without the other. A synthesis where only one constraint
activates on null CE is a PARTIAL (2 pts). FAIL if neither activates. V-02's ATOMIC
DUAL-LOCK — "Both locks activate from this single entry. Partial activation is a format
error." with `co_activation_confirmed` required — is the exemplar.

Failure mode addressed: systems where C-16 and C-17 each pass in isolation across different
variations but no single synthesis output applies both. A builder satisfying each criterion
in a different conditional branch produces a skill that is individually compliant on C-16
and C-17 but leaves open a null-CE output that is promotion-eligible (C-16 branch not
taken) or confidence-unconstrained (C-17 branch not taken). C-18 requires both locks to be
active in the same synthesis output, closing the null-CE path completely.

### C-19 — Full null-CE protocol pre-committed at campaign open

*Excellence signal from V-04 (Round 4).*

PASS: The CAMPAIGN OPEN block — declared before Stage 0 — names both the adversarial
reviewer type (required by C-16) and the confidence cap rule (required by C-17) as session-
level commitments using invariant language (e.g., "cannot be modified or bypassed",
"session-level invariant", "pre-registered — not a synthesis decision"). A block that
registers both fields but uses registration framing without invariant language is a PARTIAL
(2 pts). FAIL if neither is declared before Stage 0. V-01's PROTOCOL DECLARATION
("Do not modify after this point") and V-03's SESSION INVARIANT REGISTRY ("binding for
the full session — cannot be modified or bypassed at synthesis time") are the exemplars.

Failure mode addressed: variations where C-16 and C-17 are satisfied at synthesis time
only — the reviewer is appointed and the cap is applied reactively when null CE is detected,
rather than as pre-established protocol. Without invariant language, a builder can
implicitly suppress either mechanism before Stage 1 by treating them as conditional
responses. Pre-commitment with invariant language makes the adversarial reviewer and cap
rule session properties, not runtime decisions.

### C-20 — Per-stage null tally accumulates with protocol reference

*Excellence signal from V-03 (Round 5).*

PASS: When an evidence stage returns null, its null-result note contributes to a running
tally with explicit count language ("Running tally: SN null. X stages remain…") and
references the pre-committed invariants as already-activated obligations — not as decisions
pending synthesis. A null-result note that records the null without tally accumulation is a
PARTIAL (2 pts). FAIL if null results are recorded only at synthesis without any per-stage
notes. V-03's per-stage notes framing null results as "pre-committed session obligations,
not conditional judgments" with running stage counts is the exemplar.

Failure mode addressed: systems where null-CE propagation satisfies C-09 (synthesis-level
acknowledgment) but the accumulation is computed retroactively at Stage 5 — leaving open
the possibility that a multi-stage null session is not recognized as such until the terminal
step. Per-stage running tally language makes the accumulation auditable at each evidence
stage. Tally notes that reference the pre-committed invariants make visible that the null
path was anticipated and pre-loaded — not assembled in response to what was found. A
variation can satisfy C-09 and C-19 and still fail C-20: null acknowledged at synthesis
(C-09 PASS) and protocol pre-committed (C-19 PASS), but no per-stage accumulation exists
between collection and synthesis.

### C-21 — Co-activation state echoed into handoff artifact

*Excellence signal from V-02 (Round 5).*

PASS: The handoff section of the synthesis includes a field (e.g.,
`co_activation_confirmed: [must equal dual_lock_fired]`) that propagates the dual-lock
co-activation outcome from the synthesis block into the handoff artifact. A synthesis
that satisfies C-18 (both locks fire) but does not carry the co-activation outcome into
the handoff is a PARTIAL (2 pts). FAIL if C-18 is FAIL. V-02's integrity constraint
`co_activation_confirmed: [must equal dual_lock_fired]` in the Handoff section — requiring
the field value to match the synthesis-level activation record — is the exemplar.

Failure mode addressed: C-18 verifies that both locks fire atomically inside the synthesis
block; it does not require the outcome to be visible from the handoff artifact alone. A
handoff without a co-activation field forces downstream consumers (e.g., `topic-story`) to
trace back into the synthesis to verify null-CE closure. C-21 makes co-activation
self-documenting in the handoff, enabling point-in-chain audit without full session replay.
A variation can satisfy C-18 completely — atomic dual-lock, both fields, format-error
guard — and still fail C-21 if the handoff section is structurally complete (satisfying
C-08) but carries no co-activation echo.

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
enabling point-in-chain audit. However, interpreting `co_activation_confirmed` to determine
campaign outcome requires knowing what `dual_lock_fired` means — it creates a semantic
dependency on the null-CE machinery. C-23 requires a clean campaign-level signal that
downstream consumers can read without internal knowledge of the dual-lock mechanism. A
variation can satisfy C-21 completely and still fail C-23: the co-activation field is
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

---

## Scoring

### Weights

| Tier | Points | Criteria | Per criterion |
|------|--------|----------|---------------|
| Essential | 50 | 5 | 10 pts |
| Recommended | 30 | 3 | 10 pts |
| Aspirational | 64 | 16 | 4 pts |
| **Max composite** | **144** | | |

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

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 14/16 pass → 56
- **Composite = 136** — Golden (v6 ceiling)

- Essential: 5/5 pass → 50; Recommended: 3/3 pass → 30; Aspirational: 16/16 pass → 64
- **Composite = 144** — Golden (v7 ceiling)

---

## Design Rationale

### Essential tier

Focuses on the three things that make this skill an orchestrator rather than a single-step
skill: all stages ran (C-01), context was loaded from scout (C-02), and artifacts were
written progressively (C-03). C-04/C-05 ensure the terminal output is usable and
discoverable.

### Recommended tier

Adds traceability (C-06, C-07) and downstream handoff (C-08). All three were full PASS in
the highest-scoring Round 1 and Round 2 variations; partial failures here are the primary
separator between 85- and 95-range scores. The recommended tier and essential tier together
sum to exactly 80 — the golden threshold — making these six criteria the complete baseline
for a qualifying skill output.

### Aspirational tier

Targets the failure modes unique to orchestration. The sixteen criteria form six pairs,
one triple, and two standalones:

- **C-09, C-12**: Confidence inflation from thin evidence. C-09 checks propagation;
  C-12 checks whether the comparator that makes thin evidence meaningful was established
  upfront. Complementary — C-12 is the upstream condition that makes C-09 actionable.

- **C-10, C-11**: Opaque progress and silent gateway failures. C-10 asks for narrative
  confirmation; C-11 asks for a hard blocking gate before hypothesis formation. Together
  they prevent the failure mode where a variation looks complete but the scout-load step
  was nominal.

- **C-13, C-15**: Prefix drift and gate-trace gaps. C-13 checks per-instruction path
  enforcement; C-15 checks that gate clearance is recorded in the artifact. Both address
  the same failure pattern: a correct instruction at session open that leaves no trace in
  the artifact chain.

- **C-14, C-16**: Counter-evidence posture. C-14 makes the section unconditionally required
  with a null fallback; C-16 requires the null to trigger adversarial escalation. C-14 is
  the structural gate; C-16 is the forward obligation that the null finding generates.
  A variation can satisfy C-14 by acknowledging null passively and still fail C-16.

- **C-17** (standalone): Mechanical confidence capping. Extends C-09 from verbal
  qualification to structural constraint.

- **C-18, C-19**: Severity stack integration (added v5). C-18 verifies that C-16 and C-17
  co-fire in the same synthesis output. C-19 verifies that the null-CE protocol was
  pre-committed at CAMPAIGN OPEN with invariant language, not assembled reactively at
  synthesis time. Together they close the gap between individual criterion compliance and
  structural invariance.

- **C-20, C-21, C-22**: Audit completeness (added v6). Each extends an existing criterion's
  coverage from synthesis-internal or session-local to collection-phase or cross-artifact
  visibility. C-20 extends C-09 from synthesis-level acknowledgment to per-stage
  accumulation. C-21 extends C-18 from synthesis-block co-activation to cross-artifact
  echo. C-22 extends C-15 from scout-gate confirmation to invariant-registry confirmation.

- **C-23, C-24**: Structural enforcement (added v7). Each tightens a v6 audit criterion
  from presence to independence. C-23 extends C-21 by requiring a campaign-outcome boolean
  independent of the dual-lock mechanism — downstream consumers read campaign state
  directly, without knowledge of co-activation semantics. C-24 extends C-22 by requiring
  role-structural ownership of each attestation field — the two-field requirement is
  drift-resistant by construction, not by instruction. A variation can satisfy C-21 and
  C-22 completely and still fail both: `co_activation_confirmed` is present but
  `incumbent_defense_closed` is absent (C-23 FAIL); both gate fields are populated but
  by the same structural origin (C-24 FAIL).

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

The v5 stack (C-14 through C-19) established that null CE must be: recorded, escalated,
capped, doubly-locked per output, and pre-committed per session. The v6 additions extend
that closure into collection and audit dimensions: accumulation auditable per stage (C-20),
co-activation visible in the handoff (C-21), invariant registry attested in the hypothesis
artifact (C-22). The v7 additions extend the audit criteria from presence to independence
and structural robustness: C-23 makes the campaign outcome readable without dual-lock
inference; C-24 makes the two-field gate requirement structurally enforced. A variation
that satisfies the full v6 stack can still fail both v7 criteria: the handoff carries
`co_activation_confirmed` but no `incumbent_defense_closed` boolean (C-23 FAIL); the
hypothesis frontmatter has both gate fields but they share a single structural origin
(C-24 FAIL).

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

### Weight change note (v6 → v7)

v6: max 136, aspirational 14 criteria × 4 pts = 56 pts.
v7: max 144, aspirational 16 criteria × 4 pts = 64 pts.

Essential and recommended weights are unchanged. Max rises by 8 to accommodate two new
aspirational criteria at full 4-pt weight. The golden threshold holds at 80, which equals
essential + recommended exactly — the same structural relationship as all prior versions.

### New criteria source table (v7)

| ID | Source | Pattern |
|----|--------|---------|
| C-23 | V-05 (Round 6) | Campaign-outcome boolean as independent handoff field. V-05's Handoff carries `incumbent_defense_closed: [true if all null, false if any found]` as a field distinct from `co_activation_confirmed`. A downstream `topic-story` skill reads the campaign state directly without inferring from dual-lock semantics. V-01 through V-04 carry `co_activation_confirmed` (C-21 compliant) but none adds a separate campaign-outcome boolean. |
| C-24 | V-05 (Round 6) | Role-structural dual attestation. V-05's GATE S uses two blocking roles — one for scout-load attestation, one for invariant-registry attestation — so that each field (`gate_s_cleared`, `invariant_registry_confirmed`) has a structurally distinct owner. Dropping either role creates an immediately auditable gap. V-01 through V-04 that satisfy C-22 do so by instruction (both fields listed under one step), not by structural separation. |
