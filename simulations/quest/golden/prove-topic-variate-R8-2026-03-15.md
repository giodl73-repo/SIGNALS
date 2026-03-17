---
skill: quest-variate
skill_target: prove-topic
round: R8
date: 2026-03-15
rubric: prove-topic-rubric-v7-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [handoff_derivation_annotations, precommitted_handoff_schema, independence_path_chain]
  combined: [V-04, V-05]
r7_anchor: "V-05 (role_sequence + output_format + inertia_framing + handoff_field_independence + role_field_ownership — satisfies C-01 through C-24, 144/144)"
r8_targets: >
  Three patterns present in R7 V-05 that exceed any current criterion's requirement:
  (1) All handoff fields carry derivation-source annotations (not just incumbent_defense_closed).
  C-23 requires the field to be independent; it does not require derivation to be labeled for
  all fields. (2) CAMPAIGN OPEN pre-commits the complete handoff schema — not just the null-CE
  protocol. C-19 pre-commits the adversarial reviewer and confidence cap; it does not require
  the full handoff field contract to be declared before Stage 0. (3) incumbent_defense_closed
  carries an independence path chain — an explicit negation statement naming what it is NOT
  derived from, not just an absence. C-23 requires structural independence; it does not require
  a negative derivation assertion.
severity_stack_gap: >
  R7 V-05 includes derivation_source labels on handoff fields, a HANDOFF SCHEMA at campaign
  open, and an independence_note on incumbent_defense_closed. None of these patterns is required
  by any current criterion. A variation satisfying C-01 through C-24 can still: produce a
  handoff where only incumbent_defense_closed carries a derivation label while all other fields
  are unlabeled (handoff derivation annotations missing); assemble the handoff schema reactively
  at synthesis without pre-committing it at campaign open (pre-committed handoff schema missing);
  declare incumbent_defense_closed as independent only by its derivation source without a
  negative assertion naming what it is not derived from (independence path chain missing).
---

# prove-topic — Variation Round R8

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 8 targets three patterns in R7 V-05 that go beyond the v7 rubric ceiling:

- **Handoff derivation annotations** — Every handoff field carries a derivation label, not just
  `incumbent_defense_closed`. R7 V-05 annotates the campaign-outcome boolean but leaves other
  handoff fields (confidence, null_tally_final, co_activation_confirmed) unannotated. A new
  criterion would require all handoff fields to name their derivation source, making the complete
  handoff chain auditable without session replay.

- **Pre-committed handoff schema** — The full set of handoff field names and derivation sources
  is declared at CAMPAIGN OPEN, before Stage 0, as a session-level invariant. R7 V-05's HANDOFF
  SCHEMA (present in V-03 of R7) pre-commits the field list but not with invariant language
  binding synthesis to produce exactly those fields. A new criterion would require the handoff
  contract to be locked at campaign open — synthesis may not add or remove fields at runtime.

- **Independence path chain on `incumbent_defense_closed`** — The handoff includes an explicit
  negative derivation assertion naming what `incumbent_defense_closed` is NOT derived from
  (`NOT from dual_lock_fired`, `NOT from co_activation_confirmed`), alongside the positive
  derivation trace. R7 V-05 includes an `independence_note` as prose; a new criterion would
  require a structured negative chain as a distinct handoff field, making the independence
  assertion machine-readable, not embedded in a note string.

A variation satisfying all 24 v7 criteria can fail all three R8 targets simultaneously:
handoff fields lack derivation labels (R8 axis 1 FAIL); handoff schema assembled at synthesis
(R8 axis 2 FAIL); independence of `incumbent_defense_closed` unstated beyond its derivation
source (R8 axis 3 FAIL).

---

| Variation | Axis | Type | New target | All prior criteria |
|-----------|------|------|------------|-------------------|
| V-01 | handoff-derivation-annotations | single-axis | Derivation label on every handoff field | C-01 through C-24 |
| V-02 | precommitted-handoff-schema | single-axis | Full handoff schema locked at CAMPAIGN OPEN | C-01 through C-24 |
| V-03 | independence-path-chain | single-axis | Structured negative chain on incumbent_defense_closed | C-01 through C-24 |
| V-04 | handoff-derivation-annotations x precommitted-handoff-schema | combination (V-01 x V-02) | Axes 1 + 2 | C-01 through C-24 |
| V-05 | all R7 V-05 axes + R8 V-01 + V-02 + V-03 | full compound | Axes 1 + 2 + 3 + full R7 V-05 stack | C-01 through C-24 |

**Anchor designation (preliminary):** V-05.

---

## V-01 — Axis: Handoff Derivation Annotations (all fields labeled)

**Variation axis**: Handoff derivation annotations — every field in the Handoff section carries
a `[derived from: X]` annotation naming its structural source. `incumbent_defense_closed`,
`co_activation_confirmed`, `null_tally_final`, and `confidence` each carry an explicit
derivation label. The annotation format is consistent: `field_name: [value] — derived from: X`.
Missing annotations on any handoff field are a format error.

**Hypothesis**: When derivation labeling is applied uniformly to all handoff fields — not
selectively to `incumbent_defense_closed` — the handoff becomes fully self-documenting.
Downstream consumers (e.g., `topic-story`) can audit the provenance of every field they read
without tracing back into the synthesis block. A variation satisfying C-23 (one labeled field)
but leaving other handoff fields unlabeled produces a mixed-provenance handoff: some fields
are directly auditable, others require session replay. Uniform labeling closes this asymmetry.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign opens with two blocking roles, followed by five evidence stages.
All roles and stages execute in fixed sequence — forward only, no skipping.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants, pre-committed now:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Binding: pre-registered here, not a synthesis decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Binding: locked formula — cannot be softened or overridden at synthesis.

Both invariants are now locked for the full session. Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Declare that both SESSION INVARIANTS above are now active and locked.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Output: invariant_registry_confirmed.
Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Locate the scout record for {topic}: {topic}-scout-record-{date}.md
If not found: STOP. Record: "GATE S FAIL — scout record missing. Awaiting scout completion."
If found: load the record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true              [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Output: gate_s_cleared. Both attestation fields on record — open Stage 1.

---

## GATE S

Requires ROLE A and ROLE B both complete. Check both owned fields.

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source)

Dropping ROLE A: invariant_registry_confirmed is absent — auditable structural gap.
Dropping ROLE B: gate_s_cleared is absent — auditable structural gap.

If either field is false or missing: STOP. Do not open Stage 1.
If both fields are true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded from ROLE B]
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source]
  incumbent: [from status_quo_comparator — CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A — CAMPAIGN OPEN]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B — CAMPAIGN OPEN]

Body:
  Hypothesis statement: [one sentence — what this topic claims to do better than the incumbent]
  Basis: [3-5 signals from the scout record that support this hypothesis]
  Counter-hypothesis: [what the incumbent would claim in rebuttal]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. ROLE A + ROLE B both attested. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}:
- Independent analyses comparing {topic} to the status quo comparator.
- Adoption signals, production deployments, failure reports.
- Counter-evidence: published criticism, documented failures, expert objections.

For each source found, record: claim, source URL, CE-relevant (yes/no), quote.

NULL RESULT NOTE (if no counter-evidence found in this stage):
  Stage 2 CE result: NULL
  Running tally: [count] null. [X] evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B remain active — no change.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Web search complete. CE result: [found / NULL]. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources for evidence on {topic}:
- Prior analyses, design documents, prototype results, team discussions.
- Counter-evidence: documented concerns, unresolved objections, performance flags.

For each source found, record: artifact path, claim, CE-relevant (yes/no).

NULL RESULT NOTE (if no counter-evidence found in this stage):
  Stage 3 CE result: NULL
  Running tally: [count] null. [X] evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B remain active — no change.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Intelligence scan complete. CE result: [found / NULL]. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence gathered across Stages 2 and 3:
- Strength of supporting evidence for the hypothesis.
- Counter-evidence summary: all CE found, sources, and credibility.
- If CE was found: qualify the hypothesis and adjust confidence.
- If CE was null across both stages: acknowledge explicitly with sources checked.

### CAMPAIGN OUTCOME BLOCK

Compute campaign outcome from evidence tally. This block runs before synthesis.

  null_tally_final: [count of evidence stages that returned null CE — range 0 to 3]
  incumbent_defense_closed: [true if null_tally_final = 3; false if any CE was found]
  derivation: "null_tally_final = {count}. Formula: null_tally_final >= 3 → true."

Note: incumbent_defense_closed is derived from null_tally_final above.
It is not inferred from dual_lock_fired or co_activation_confirmed.
Both fields are consumers of null_tally_final — neither derives the other.

Confirm: "Campaign outcome computed: incumbent_defense_closed = [true/false]. Stage 4 complete."

Artifact written: {topic}-analysis-{date}.md.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Retrieve SESSION INVARIANTs A and B from CAMPAIGN OPEN. Confirm both are still in scope.

  adversarial_reviewer_type: [confirmed from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [confirmed from SESSION INVARIANT B]

### Findings

Summarize: what the evidence campaign established about {topic} vs the incumbent.
Format: 3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION. Counter-evidence is unconditionally required.
If CE was found: list each item with source artifact and credibility rating.
If CE was null: state: "No counter-evidence found. Sources checked: [Stage 2 sources], [Stage 3 sources]. This null result is the primary risk to the hypothesis."

If CE is null:
  - Adversarial review is required before any promotion decision.
    Assign: {adversarial_reviewer_type} (pre-committed SESSION INVARIANT A — this is execution, not a new decision).
  - Confidence is mechanically capped by SESSION INVARIANT B:
    CE-score = -2. This cap cannot be bypassed.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion. Pre-committed. Execution only.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B):
    ce_score_formula applied: CE-score = -2 (all-null).
    Maximum claim: MEDIUM. HIGH is blocked without adversarial input.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

Compute from evidence quality + CE-score:
  evidence_score: [assessed 0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B formula]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2]

### Handoff

DERIVATION ANNOTATION RULE: Every field in this section must carry
a `[derived from: X]` label naming its structural source. Unlabeled fields
are a format error.

  scout_anchor: {topic}-scout-record-{date}.md [derived from: ROLE B — GATE S]
  hypothesis: {topic}-hypothesis-{date}.md [derived from: Stage 1 artifact]
  analysis: {topic}-analysis-{date}.md [derived from: Stage 4 artifact]
  null_tally_final: [0-3] [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]
  incumbent_defense_closed: [true/false] [derived from: null_tally_final via formula "null_tally_final >= 3" — NOT from co_activation_confirmed]
  co_activation_confirmed: [true/false] [derived from: dual_lock_fired in ATOMIC DUAL-LOCK — NOT from incumbent_defense_closed]
  confidence: [LOW/MEDIUM/HIGH] [derived from: evidence_score + ce_score formula]
  next: topic-story — evidence brief is ready

Confirm: "Synthesis complete. Derivation labels applied to all handoff fields. Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-02 — Axis: Pre-committed Handoff Schema (full contract locked at CAMPAIGN OPEN)

**Variation axis**: Pre-committed handoff schema — the complete set of handoff field names and
their derivation sources is declared at CAMPAIGN OPEN, before Stage 0, alongside the null-CE
invariants. This handoff schema is a session-level invariant: synthesis must produce exactly
the declared fields. No field may be added or removed at synthesis time. A synthesis that
produces an undeclared field or omits a declared field is a format error, auditable from the
campaign-open block without replaying the session.

**Hypothesis**: When the handoff schema is pre-committed as a session invariant — alongside
the adversarial reviewer and confidence cap — the handoff contract becomes as binding as the
null-CE protocol. C-19 requires the null-CE protocol to be pre-committed; it does not require
the handoff field list to be pre-committed. A synthesis can satisfy C-19 (protocol pre-committed)
while constructing the handoff schema reactively — selecting which fields to include based on
what was found. Pre-committing the schema eliminates this discretion: the contract is known
before any evidence runs, and synthesis is constrained to fulfill it.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Stages execute in fixed sequence. All handoff fields are declared at campaign open
and locked for the session — synthesis may not add or remove fields.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages return null CE.
    Binding: pre-registered now — not a synthesis decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Binding: locked formula — cannot be overridden at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant:

The following fields MUST appear in the Handoff section of the synthesis artifact.
No field may be added or removed at synthesis time. This schema is locked now.

  DECLARED FIELDS:
    scout_anchor          [derived from: ROLE B scout load]
    hypothesis            [derived from: Stage 1 artifact write]
    analysis              [derived from: Stage 4 artifact write]
    null_tally_final      [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]
    incumbent_defense_closed   [derived from: null_tally_final — NOT from co_activation_confirmed]
    co_activation_confirmed    [derived from: dual_lock_fired in synthesis]
    confidence            [derived from: evidence_score + ce_score formula]
    next                  [derived from: static — "topic-story"]

Schema lock confirmed. Synthesis must produce exactly these 8 fields. Format error if any
field is absent; format error if any undeclared field is added.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field.

Execute first. Confirm that SESSION INVARIANTs A and B AND the PRE-COMMITTED HANDOFF
SCHEMA are all active as session invariants.

  invariant_registry_confirmed: true    [ROLE A's owned field — covers all three declared invariants]

ROLE A COMPLETE. Output: invariant_registry_confirmed.
Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field.

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true              [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Output: gate_s_cleared. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source, covers null-CE protocol + handoff schema)

If either is false or missing: STOP. Do not open Stage 1.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source; includes handoff schema lock]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true      [confirmed — schema declared at CAMPAIGN OPEN, binding]

Body: Hypothesis statement, basis, counter-hypothesis.

Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Schema lock confirmed in frontmatter."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for: evidence on {topic} vs the status quo comparator; counter-evidence.

NULL RESULT NOTE (if no CE found):
  Stage 2 CE: NULL
  Running tally: [count] null. [X] stages remain.
  Protocol status: SESSION INVARIANTs A and B active. Handoff schema locked.

Artifact written: {topic}-websearch-{date}.md.

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources for evidence; record CE if found.

NULL RESULT NOTE (if no CE found):
  Stage 3 CE: NULL
  Running tally: [count] null. [X] stage remains.
  Protocol status: SESSION INVARIANTs A and B active. Handoff schema locked.

Artifact written: {topic}-intelligence-{date}.md.

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence. Summarize findings and CE state.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula. Independent of co_activation_confirmed."

Artifact written: {topic}-analysis-{date}.md.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B are in scope. Confirm HANDOFF SCHEMA is in scope.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION. State CE found or record null with sources checked.
If null: assign adversarial reviewer (SESSION INVARIANT A). Apply CE-score cap (SESSION INVARIANT B).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  dual_lock_fired: [true/false]
  co_activation_confirmed: [must equal dual_lock_fired]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2]
  confidence: [LOW/MEDIUM/HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — before writing this section, retrieve PRE-COMMITTED HANDOFF
SCHEMA from CAMPAIGN OPEN. Confirm all 8 declared fields will be produced. If any declared
field cannot be produced, record: "SCHEMA ERROR: {field_name} missing." Do not suppress.

Write exactly the 8 declared fields — no additions, no omissions:

  scout_anchor: {topic}-scout-record-{date}.md
  hypothesis: {topic}-hypothesis-{date}.md
  analysis: {topic}-analysis-{date}.md
  null_tally_final: [0-3]
  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired]
  confidence: [LOW/MEDIUM/HIGH]
  next: topic-story

  schema_compliance_confirmed: true    [all 8 declared fields present, no undeclared fields added]

Confirm: "Synthesis complete. Handoff schema compliance confirmed. Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-03 — Axis: Independence Path Chain on `incumbent_defense_closed`

**Variation axis**: Independence path chain — `incumbent_defense_closed` in the handoff carries
a structured two-part derivation record: (1) a positive derivation chain naming the source
tally and formula, and (2) a negative assertion explicitly naming what it is NOT derived from.
The negative assertion is a distinct, structured field — not embedded in a prose note. Format:
`independence_chain: NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed.`
A handoff missing the negative assertion is a format error even if the positive derivation is
correct.

**Hypothesis**: C-23 requires `incumbent_defense_closed` to be structurally independent of
`co_activation_confirmed`. Independence is demonstrated by the derivation path (it comes from
`null_tally_final`, not from the co-activation chain). But a downstream consumer reading
the handoff field can only verify independence if they know that `co_activation_confirmed` is
a plausible alternative derivation path — and that it was explicitly not used. An independence
assertion that only names the positive source (`derived from null_tally_final`) leaves the
negative path implicit. A structured negative chain makes the assertion explicit, parseable,
and auditable: any reader can confirm that the two forbidden derivation sources are named and
negated, without domain knowledge of the dual-lock mechanism.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Stages execute in fixed sequence. The campaign outcome boolean carries a structured
independence chain with both positive derivation and negative assertion.

---

## CAMPAIGN OPEN

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages return null CE.
    Binding: pre-registered now — not a synthesis decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Binding: locked — cannot be overridden at synthesis.

Both invariants locked. Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed

  invariant_registry_confirmed: true    [ROLE A — sole producer]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record.

  gate_s_cleared: true    [ROLE B — sole producer]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source)

Both true: advance to Stage 1. Either false: STOP.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]

Body: Hypothesis statement, basis, counter-hypothesis.

Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for evidence on {topic} vs status quo comparator; counter-evidence.

NULL RESULT NOTE (if no CE found):
  Stage 2 CE: NULL
  Running tally: [count] null. [X] stages remain.
  Protocol status: SESSION INVARIANTs A and B active — pre-committed obligations pending.

Artifact written: {topic}-websearch-{date}.md.

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources.

NULL RESULT NOTE (if no CE found):
  Stage 3 CE: NULL
  Running tally: [count] null. [X] stage remains.
  Protocol status: SESSION INVARIANTs A and B active — pre-committed obligations pending.

Artifact written: {topic}-intelligence-{date}.md.

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze evidence. Summarize CE state.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3]

### INDEPENDENCE PATH BLOCK (for incumbent_defense_closed)

  positive_derivation:
    source: null_tally_final
    formula: "null_tally_final >= 3"
    result: [true if null_tally_final = 3; false otherwise]

  independence_chain:
    NOT derived from: dual_lock_fired
    NOT derived from: co_activation_confirmed
    Basis: both dual_lock_fired and co_activation_confirmed are downstream consumers
           of null_tally_final, same as incumbent_defense_closed. Neither is an
           upstream source. Derivation paths are parallel, not sequential.

  incumbent_defense_closed: [value from positive_derivation.result above]

Confirm: "Campaign outcome computed with full independence chain. Stage 4 complete."

Artifact written: {topic}-analysis-{date}.md.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B are in scope.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION.
If CE found: list with source and credibility.
If null: state sources checked, record null. Assign adversarial reviewer (SESSION INVARIANT A).
Apply CE-score cap (SESSION INVARIANT B).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  dual_lock_fired: [true/false]
  co_activation_confirmed: [must equal dual_lock_fired]
  Note: co_activation_confirmed and incumbent_defense_closed are parallel consumers
        of null_tally_final — neither derives the other.

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  confidence: [LOW/MEDIUM/HIGH — HIGH blocked if ce_score = -2]

### Handoff

  scout_anchor: {topic}-scout-record-{date}.md
  hypothesis: {topic}-hypothesis-{date}.md
  analysis: {topic}-analysis-{date}.md
  null_tally_final: [0-3]

  incumbent_defense_closed: [true/false]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [Derivation chains confirmed from Stage 4 INDEPENDENCE PATH BLOCK]

  co_activation_confirmed: [true/false — must equal dual_lock_fired; NOT an upstream source of incumbent_defense_closed]
  confidence: [LOW/MEDIUM/HIGH]
  next: topic-story

Confirm: "Synthesis complete. Independence path chain confirmed in handoff. Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-04 — Axes: Handoff Derivation Annotations + Pre-committed Handoff Schema (combination)

**Variation axes**: Handoff derivation annotations (V-01) combined with pre-committed handoff
schema (V-02). All handoff fields carry derivation labels AND the full schema is declared at
CAMPAIGN OPEN as a session invariant. The pre-committed schema lists field names AND their
expected derivation sources — so at synthesis, a schema compliance check can verify both field
presence and derivation-label correctness against the pre-declared contract.

**Hypothesis**: V-01 labels derivation sources uniformly at synthesis time; V-02 pre-commits
the field contract at campaign open. Together, they create a two-checkpoint verification:
(1) the campaign open declares what fields and derivation sources will appear; (2) synthesis
checks each field against the pre-declared schema. A discrepancy (wrong derivation source,
missing field, added field) is a format error detectable without session replay. Neither
axis alone creates this double-check: V-01 labels correctly but reactively; V-02 locks the
contract but doesn't enforce per-field labeling. Combined, they close both gaps.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Stages execute in fixed sequence. All handoff fields carry derivation labels.
The complete handoff schema is pre-committed at campaign open and binding for the session.

---

## CAMPAIGN OPEN

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages return null CE.
    Binding: pre-registered now — not a synthesis decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Binding: locked — cannot be overridden at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant:

Schema is locked now. Synthesis must produce exactly these fields with exactly these
derivation sources. Missing field: format error. Wrong derivation source: format error.
Added undeclared field: format error.

  FIELD                      | REQUIRED DERIVATION SOURCE
  ---------------------------|--------------------------------------------
  scout_anchor               | ROLE B scout load
  hypothesis                 | Stage 1 artifact write
  analysis                   | Stage 4 artifact write
  null_tally_final           | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed   | null_tally_final (NOT co_activation_confirmed)
  co_activation_confirmed    | dual_lock_fired in synthesis (NOT incumbent_defense_closed)
  confidence                 | evidence_score + ce_score formula
  next                       | static: "topic-story"

Schema locked. All fields must appear in Handoff with stated derivation labels.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed

Execute first. Confirm SESSION INVARIANTs A and B and PRE-COMMITTED HANDOFF SCHEMA
are all active as session invariants.

  invariant_registry_confirmed: true    [ROLE A — sole producer; covers null-CE protocol + handoff schema]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B — sole producer]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers null-CE + handoff schema)

Both true: advance to Stage 1. Either false: STOP.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source; includes handoff schema lock]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true      [schema declared at CAMPAIGN OPEN — binding]

Body: Hypothesis statement, basis, counter-hypothesis.

Confirm: "Hypothesis written. Schema lock confirmed in frontmatter. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for evidence on {topic} vs status quo comparator; counter-evidence.

NULL RESULT NOTE (if no CE found):
  Stage 2 CE: NULL
  Running tally: [count] null. [X] stages remain.
  Protocol status: SESSION INVARIANTs A and B active. Handoff schema locked.

Artifact written: {topic}-websearch-{date}.md.

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources; record CE if found.

NULL RESULT NOTE (if no CE found):
  Stage 3 CE: NULL
  Running tally: [count] null. [X] stage remains.
  Protocol status: SESSION INVARIANTs A and B active. Handoff schema locked.

Artifact written: {topic}-intelligence-{date}.md.

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze evidence. Summarize CE state.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3 — count of evidence stages returning null CE]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula. Independent of co_activation_confirmed."

Artifact written: {topic}-analysis-{date}.md.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B are in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION.
If CE found: list with source and credibility.
If null: record null with sources checked. Assign adversarial reviewer (SESSION INVARIANT A).
Apply confidence cap (SESSION INVARIANT B).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  dual_lock_fired: [true/false]
  co_activation_confirmed: [must equal dual_lock_fired]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  confidence: [LOW/MEDIUM/HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — before writing, verify against PRE-COMMITTED HANDOFF SCHEMA.
Confirm: each of the 8 declared fields will be produced with its declared derivation source.
Any mismatch: record "SCHEMA ERROR: {field} — expected derivation: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE — all fields carry [derived from: X] labels.
Missing labels are a format error independent of schema compliance.

Write all 8 declared fields with derivation labels:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    [derived from: null_tally_final via formula — NOT from co_activation_confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    [derived from: dual_lock_fired in ATOMIC DUAL-LOCK — NOT from incumbent_defense_closed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true    [all 8 declared fields present with declared derivation sources]

Confirm: "Synthesis complete. Derivation labels applied. Schema compliance confirmed. Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-05 — Axes: Role Sequence + Output Format + Inertia Framing + All R8 Axes (full compound)

**Variation axes**: All three R7 V-05 axes (role sequence, table output format, inertia framing)
combined with all three R8 axes (handoff derivation annotations, pre-committed handoff schema,
independence path chain). This is the full compound variation targeting all patterns from both
rounds simultaneously.

**Hypothesis**: The three R8 axes address different structural layers:
V-01 closes uniform derivation labeling (synthesis-artifact layer);
V-02 closes handoff pre-commitment (session-invariant layer);
V-03 closes independence assertion (field-semantics layer).
A variation satisfying all three simultaneously, on top of the full R7 V-05 stack, demonstrates
that the patterns are composable without interference: pre-committing the schema with derivation
sources (V-02) does not conflict with per-field labeling at synthesis (V-01); adding an
independence path chain (V-03) on `incumbent_defense_closed` is consistent with the pre-committed
derivation source for that field. All three axes reinforce rather than duplicate each other.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign opens with two blocking roles followed by five evidence stages in fixed sequence.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

**Current approach note:** Every section will compare against this comparator.
Thin evidence does not become strong evidence in the absence of the incumbent's record.

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants — locked now:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered. Cannot be modified or bypassed.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Invariant language: locked formula. Cannot be softened or overridden at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant — locked now:

Synthesis must produce exactly these 9 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch is a format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|--------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 INCUMBENT-DEFENSE TABLE
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired (NOT incumbent_defense_closed)
  confidence                  | evidence_score + ce_score formula (SESSION INVARIANT B)
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check

All three session invariants (A, B, and Handoff Schema) are now locked.
Do not modify any of them after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: `invariant_registry_confirmed`
Sole producer of this field. Structural ownership declared here.
Dropping ROLE A from the schema creates an auditable gap: invariant_registry_confirmed
is absent. This absence is detectable from the GATE S manifest without session replay.

Execute first. Confirm SESSION INVARIANT A, SESSION INVARIANT B, and PRE-COMMITTED
HANDOFF SCHEMA are all active as session invariants.

  invariant_registry_confirmed: true    [ROLE A's owned field — sole producer]

ROLE A COMPLETE. Output: invariant_registry_confirmed.
Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: `gate_s_cleared`
Sole producer of this field. Structural ownership declared here.
Dropping ROLE B from the schema creates an auditable gap: gate_s_cleared is absent.
This absence is detectable from the GATE S manifest without session replay.

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing. ROLE A invariants are locked
but scout prerequisite unmet. Campaign cannot proceed."
If found: load record. Extract: market signal, competitor landscape, feasibility finding,
status_quo evidence (needed for comparator grounding at each evidence stage).

  gate_s_cleared: true    [ROLE B's owned field — sole producer]

ROLE B COMPLETE. Output: gate_s_cleared.
Both attestation fields on record — open Stage 1.

---

## GATE S

ROLE FIELD MANIFEST:
  | Role   | Owned Field                  | Status |
  |--------|------------------------------|--------|
  | ROLE A | invariant_registry_confirmed | true   |
  | ROLE B | gate_s_cleared               | true   |

Both fields required. Loss of either role creates an auditable gap in this manifest.

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers null-CE + handoff schema)

If either is false or missing: STOP. Do not open Stage 1.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source; covers all three session invariants]
  incumbent: [from CAMPAIGN OPEN status_quo_comparator]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true      [PRE-COMMITTED HANDOFF SCHEMA active — schema from CAMPAIGN OPEN]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Incumbent rebuttal: [what the incumbent claims — grounded in scout record]
  Basis: [3-5 signals from scout record]
  Counter-hypothesis: [strongest incumbent defense]

Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. All session invariants confirmed
          in frontmatter. Field provenance: ROLE A + ROLE B. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding:

| Source | Claim | Supports Hypothesis | CE-Relevant | Quote |
|--------|-------|---------------------|-------------|-------|
| ...    | ...   | yes/no              | yes/no      | ...   |

Incumbent comparator: [from CAMPAIGN OPEN]. Does any evidence address whether the
incumbent has equivalent capability? Record incumbent evidence in its own table row.

NULL RESULT NOTE (if no CE found in this stage):
  Stage 2 CE result: NULL
  Running tally: 1 null. 2 evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B are active — null CE obligations
  are pre-committed obligations, not synthesis decisions.
  Handoff schema locked — null result does not change the schema.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found / NULL]. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding:

| Artifact | Claim | Supports Hypothesis | CE-Relevant |
|----------|-------|---------------------|-------------|
| ...      | ...   | yes/no              | yes/no      |

Incumbent note: document any internal evidence comparing {topic} to the status quo comparator.

NULL RESULT NOTE (if no CE found in this stage):
  Stage 3 CE result: NULL
  Running tally: [count] null. 1 evidence stage remains.
  Protocol status: SESSION INVARIANTs A and B active — obligations locked.
  Handoff schema locked — no field changes permitted at evidence stages.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found / NULL]. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3.

### Evidence Summary Table

| Stage | Evidence Type | CE Found | Incumbent Reference | Notes |
|-------|--------------|----------|---------------------|-------|
| S2    | Web Search   | yes/no   | yes/no              | ...   |
| S3    | Intelligence | yes/no   | yes/no              | ...   |

### INCUMBENT-DEFENSE TABLE

| Stage | CE Result | Running Null Count |
|-------|-----------|--------------------|
| S2    | [NULL / found] | [1 or 0]      |
| S3    | [NULL / found] | [running count] |

  null_tally_final: [final count from table above — 0 to 3]

### CAMPAIGN OUTCOME BLOCK

Compute incumbent_defense_closed from null_tally_final.

  POSITIVE DERIVATION:
    source: null_tally_final = {value}
    formula: "null_tally_final >= 3 → true; otherwise → false"
    result: [true / false]

  INDEPENDENCE PATH BLOCK:
    positive_derivation_chain: null_tally_final → formula → boolean
    independence_chain:
      NOT derived from: dual_lock_fired
      NOT derived from: co_activation_confirmed
      Basis: dual_lock_fired and co_activation_confirmed are parallel consumers
             of null_tally_final. Neither is an upstream source of this field.
             Downstream consumers read incumbent_defense_closed directly without
             knowledge of the dual-lock mechanism.

  incumbent_defense_closed: [value from POSITIVE DERIVATION.result]

Confirm: "Campaign outcome computed: incumbent_defense_closed = [value].
          Independence path chain confirmed: derivation from null_tally_final only.
          Advancing to Stage 5."

Artifact written: {topic}-analysis-{date}.md.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

**Step 1 — Invariant Recall**
Retrieve SESSION INVARIANTs A and B from CAMPAIGN OPEN.
Retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.

  | Invariant | Value | Source |
  |-----------|-------|--------|
  | adversarial_reviewer_type | [from SESSION INVARIANT A] | CAMPAIGN OPEN |
  | ce_score_formula | CE-score = -2 if all null | SESSION INVARIANT B |
  | handoff_schema | 9 fields declared | CAMPAIGN OPEN — locked |

### Findings

| Finding | Evidence | Artifact | Confidence |
|---------|----------|----------|------------|
| ...     | ...      | ...      | ...        |

Incumbent comparison row required: how does the evidence compare {topic} to the
status_quo_comparator defined at campaign open?

### Counter-Evidence

MANDATORY SECTION. Counter-evidence unconditionally required.

If CE was found: list each item — source, claim, credibility, implication for hypothesis.
If CE was null across all evidence stages:
  State: "Counter-evidence: NULL. Sources checked: [Stage 2 sources], [Stage 3 sources].
  This null result is the primary risk flag for this hypothesis."
  Then:
  — Assign adversarial reviewer: {adversarial_reviewer_type} (SESSION INVARIANT A — execution, not new decision).
  — Apply confidence cap: ce_score = -2 (SESSION INVARIANT B — execution, not new decision).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

LOCK 1 — Reviewer Challenge (SESSION INVARIANT A):
  adversarial_reviewer_type: [confirmed from CAMPAIGN OPEN]
  Required before any promotion decision. Pre-committed. This is execution.

LOCK 2 — Confidence Cap (SESSION INVARIANT B):
  ce_score_formula applied: CE-score = -2.
  Maximum claim: MEDIUM. HIGH is blocked without adversarial input.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]
  Note: co_activation_confirmed and incumbent_defense_closed are parallel consumers
        of null_tally_final. Neither derives the other.

### Confidence Level

| Dimension | Score | Rule |
|-----------|-------|------|
| evidence_score | [0-5] | assessed from Findings |
| ce_score | [0 or -2] | SESSION INVARIANT B formula |
| incumbent_delta | [assessed +/- vs comparator] | from Findings incumbent row |
| confidence | [LOW/MEDIUM/HIGH] | HIGH blocked if ce_score = -2 |

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields will be produced with their declared derivation sources.
Any mismatch: record "SCHEMA ERROR: {field} — expected derivation: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE — all fields carry [derived from: X] labels. Unlabeled field = format error.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load — per HANDOFF SCHEMA]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — per HANDOFF SCHEMA]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write — per HANDOFF SCHEMA]

  null_tally_final: [0-3]
    [derived from: Stage 4 INCUMBENT-DEFENSE TABLE — per HANDOFF SCHEMA]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — per HANDOFF SCHEMA; independent of co_activation_confirmed confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    [derived from: dual_lock_fired in ATOMIC DUAL-LOCK — per HANDOFF SCHEMA; NOT from incumbent_defense_closed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B — per HANDOFF SCHEMA]

  next: topic-story
    [derived from: static handoff target — per HANDOFF SCHEMA]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — all 9 declared fields present with declared derivation sources; no additions; no omissions]

Confirm: "Synthesis complete. Derivation labels applied to all handoff fields.
          Schema compliance confirmed (9/9 fields, derivation sources matched).
          Independence path chain confirmed on incumbent_defense_closed.
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## Anchor Designation

**Anchor: V-05.**

V-05 is the full compound: all three R7 V-05 axes (role sequence, table output format, inertia
framing) plus all three R8 axes (handoff derivation annotations, pre-committed handoff schema,
independence path chain). All 24 v7 criteria are satisfied, and all three R8 targets are
present.

| Criterion | Source in V-05 |
|-----------|----------------|
| C-01 through C-24 | All present — full v7 stack inherited from R7 V-05 architecture |
| R8 axis 1 (handoff derivation annotations) | All 9 handoff fields carry [derived from: X] labels; unlabeled field = format error |
| R8 axis 2 (pre-committed handoff schema) | HANDOFF SCHEMA declared at CAMPAIGN OPEN as session invariant; 9 fields with derivation sources locked before Stage 0; schema_compliance_confirmed field at synthesis |
| R8 axis 3 (independence path chain) | incumbent_defense_closed carries both positive_derivation chain and independence_chain with explicit NOT assertions on dual_lock_fired and co_activation_confirmed |

**Stress test for V-05:** A variation implementing R8 axis 3 (independence path chain on
`incumbent_defense_closed`) but without R8 axis 2 (pre-committed schema) would satisfy the
independence assertion at synthesis time while still allowing the handoff schema to be assembled
reactively. The pre-committed schema closes this gap: the independence assertion is visible at
campaign open, not just at synthesis. Dropping axis 2 while keeping axis 3 satisfies the negative
assertion but not the pre-commitment contract.

**Ceiling status under v7:** V-05 achieves 144/144 under the current rubric. The three R8 axes
are candidate criteria for v8 — none is required by any criterion in v7. A v7-compliant
variation can fail all three: handoff fields without derivation labels (R8 axis 1 gap), schema
assembled at synthesis (R8 axis 2 gap), independence of `incumbent_defense_closed` unstated
beyond its positive derivation source (R8 axis 3 gap).
