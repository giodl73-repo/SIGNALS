Written to `simulations/quest/rubrics/prove-topic-rubric-v5-2026-03-15.md`.

---

**New criteria extracted from Round 4:**

| ID | Source | Pattern |
|----|--------|---------|
| C-18 | V-04 | Null CE synthesis doubly locked — C-16 (escalation/block) and C-17 (mechanical cap) must co-fire in the same synthesis output. V-01 has C-16 PASS but C-17 PARTIAL; V-02 has C-17 PASS but C-16 FAIL. Individual criterion compliance does not guarantee co-activation. C-18 closes that gap. |
| C-19 | V-04 | Full null-CE protocol pre-committed at CAMPAIGN OPEN before Stage 0 — both the adversarial reviewer type (C-16 pre-registration) and the confidence cap rule (C-17 formula) declared as session-level invariants. V-02 and V-03 both lose C-12 PARTIAL because comparator appears in Stage 1 frontmatter; the generalized pattern is that the complete null-CE response must be committed before collection begins. |

**Weight outcome:** Max rises from 116 → 124. Golden threshold unchanged at 80 (essential + recommended = 50 + 30 = 80 exactly). Aspirational expands from 9 to 11 criteria at 4 pts each.

**New design note:** C-14/C-16/C-17/C-18/C-19 form a complete severity stack — *recording → escalation → consequence → co-activation → pre-commitment*. C-18 distinguishes individual criterion compliance from structural co-activation; C-19 distinguishes reactive compliance from session-level invariance. A variation can satisfy C-14 through C-17 and still fail both: each criterion fires in a separate branch (fails C-18) or fires only after null is detected at Stage 5 (fails C-19).
the model to
write one) before advancing. Stages that complete with no artifact instruction are a FAIL.

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
grounds any thin-evidence acknowledgment in a concrete alternative rather than an
isolated caveat. A comparator introduced only at Stage 4 or only in the synthesis is a
PARTIAL (2 pts). The pattern — "status-quo comparator at campaign opening → referenced at
each evidence stage → Warning+effect at Stage 4 traced to synthesis" — is the exemplar.

Failure mode addressed: C-09 partials where thin-evidence flags appear late and are not
connected to a pre-established baseline, making the confidence qualification untethered.

### C-13 — Per-artifact path enforcement on each write instruction

*Excellence signal from V-01 (Round 1).*

PASS: Every write instruction in the response names the full artifact path (e.g.,
`{topic}-hypothesis-{date}.md`), not just the topic prefix or a filename stem. A prefix
defined once at session opening without per-instruction path naming is a PARTIAL (2 pts).
This prevents prefix drift across sub-stages and multi-turn sessions. V-01's "`{topic}-`
in every path" enforcement pattern is the exemplar.

Failure mode addressed: C-05 partials where a correctly-defined opening prefix drifts by
Stage 3–4 because individual write instructions do not restate it.

### C-14 — Counter-evidence unconditionally required in synthesis

*Excellence signal from V-04/V-05 (Round 2).*

PASS: The synthesis section requires counter-evidence as a named, mandatory field — not as
a conditional section or optional addition. The instruction must make counter-evidence
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
"null result recorded → adversarial review explicitly recommended" (V-01/V-02: "Recommend
adversarial review"; V-03: "cannot be rated HIGH without adversarial input") — is the
exemplar.

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
activates on null CE is a PARTIAL (2 pts). FAIL if neither activates. V-04's combination of
V-01's adversarial block and V-02's CE-score formula co-firing from the same null detection
event is the exemplar.

Failure mode addressed: systems where C-16 and C-17 each pass in isolation across different
variations but no single synthesis output applies both. A builder satisfying each criterion
in a different branch of the null path produces a skill that is individually compliant on
C-16 and C-17 but leaves open a null-CE output that is promotion-eligible (C-16 branch not
taken) or confidence-unconstrained (C-17 branch not taken). C-18 requires both locks to be
active in the same synthesis output, closing the null-CE path completely.

### C-19 — Full null-CE protocol pre-committed at campaign open

*Excellence signal from V-04 (Round 4).*

PASS: The CAMPAIGN OPEN block — declared before Stage 0 — names both the adversarial
reviewer type (required by C-16) and the confidence cap rule (required by C-17) as session-
level commitments. Pre-commitment establishes the null-CE response before evidence
collection begins, removing the decision point from synthesis time. A CAMPAIGN OPEN block
that pre-registers the reviewer type but not the cap formula is a PARTIAL (2 pts). FAIL if
neither is declared before Stage 0. V-04's CAMPAIGN OPEN block (inherited from V-01)
declaring both the reviewer designation and the cap rule before Stage 1 opens is the
exemplar.

Failure mode addressed: variations where C-16 and C-17 are satisfied at synthesis time
only — the reviewer is appointed and the cap is applied reactively when null CE is detected,
rather than as pre-established protocol. Without pre-commitment, a builder could implicitly
skip either mechanism by deciding null CE was "unlikely" before Stage 1. Pre-commitment
makes the adversarial reviewer and cap rule invariant session properties, not conditional
responses.

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

Targets the failure modes unique to orchestration. The eleven criteria form five pairs plus
one standalone:

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

- **C-17** (standalone in v4): Mechanical confidence capping. Extends C-09 from verbal
  qualification to structural constraint.

- **C-18, C-19**: Severity stack integration (new in v5). C-18 verifies that C-16 and C-17
  co-fire in the same synthesis output — no output is both promotion-eligible and
  confidence-unconstrained when CE is null. C-19 verifies that the null-CE protocol was
  pre-committed at CAMPAIGN OPEN, not assembled reactively at synthesis time. Together they
  close the gap between individual criterion compliance and structural invariance: a skill
  that satisfies C-14–C-17 but fails C-18/C-19 is locally compliant but not structurally
  sound.

---

## Severity Stack: C-14 / C-16 / C-17 / C-18 / C-19

The five criteria form a complete null-CE closure chain:

| Criterion | Role | What it closes |
|-----------|------|----------------|
| C-14 | Recording | Null CE must be named, not elided |
| C-16 | Escalation | Null CE must trigger adversarial review |
| C-17 | Consequence | Null CE must cap confidence mechanically |
| C-18 | Co-activation | C-16 and C-17 must fire together in the same output |
| C-19 | Pre-commitment | The full protocol must be declared before Stage 0 |

A variation that satisfies C-14 through C-17 but fails C-18 may pass each criterion in a
separate conditional branch, leaving the null path exploitable. A variation that satisfies
C-14 through C-18 but fails C-19 applies the protocol reactively — the decision to escalate
and cap occurs at synthesis, leaving open the possibility of implicit suppression before
collection begins. Full stack compliance (all five) requires null CE to be: recorded (C-14),
escalated (C-16), capped (C-17), doubly-locked per output (C-18), and pre-committed per
session (C-19).

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-15 | Initial rubric, 10 criteria (5 essential, 3 recommended, 2 aspirational), max 100 |
| v2 | 2026-03-15 | Add C-11, C-12, C-13 from Round 1 excellence signals; rebalance weights: essential 10 pts, recommended 10 pts, aspirational 4 pts; max unchanged at 100 |
| v3 | 2026-03-15 | Add C-14, C-15 from Round 2 excellence signals; max rises to 108; golden threshold unchanged at 80 |
| v4 | 2026-03-15 | Add C-16, C-17 from Round 3 excellence signals; max rises to 116; golden threshold unchanged at 80 |
| v5 | 2026-03-15 | Add C-18, C-19 from Round 4 excellence signals; max rises to 124; golden threshold unchanged at 80 |

### Weight change note (v4 → v5)

v4: max 116, aspirational 9 criteria × 4 pts = 36 pts.
v5: max 124, aspirational 11 criteria × 4 pts = 44 pts.

Essential and recommended weights are unchanged. Max rises by 8 to accommodate the two new
aspirational criteria at full 4-pt weight. The golden threshold holds at 80, which equals
essential + recommended exactly — the same structural relationship as all prior versions.

### New criteria source table (v5)

| ID | Source | Pattern |
|----|--------|---------|
| C-18 | V-04 (Round 4) | Null CE path doubly locked — escalation and cap must co-fire in the same synthesis output. V-01 has C-16 PASS but C-17 PARTIAL (verbal cap only); V-02 has C-17 PASS but C-16 FAIL (no escalation); V-04 achieves both, revealing that individual criterion compliance does not guarantee co-activation. |
| C-19 | V-04 (Round 4) | Full null-CE protocol pre-committed at CAMPAIGN OPEN. V-01/V-02/V-03 all show C-12 PARTIAL when the comparator appears in Stage 1 frontmatter rather than CAMPAIGN OPEN; V-04's CAMPAIGN OPEN block (from V-01) pre-registers both the adversarial reviewer type and the cap rule before Stage 0, making them session-level invariants rather than reactive synthesis decisions. |
