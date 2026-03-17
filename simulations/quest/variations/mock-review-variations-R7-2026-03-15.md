# /quest:mock-review — Variations V-01 through V-05

**Variation axes selected:**
- **Axis A — Role sequence**: which evaluator runs first (PM-first vs Architect-first vs Strategy-first)
- **Axis B — Inertia framing**: how explicitly REAL-REQUIRED is established as the default position
- **Axis C — Lifecycle emphasis**: how explicit and mechanical phase boundaries are

Single-axis: V-01 (A), V-02 (B), V-03 (C). Combinations: V-04 (B+C), V-05 (A+B+C).

---

## V-01 — Role Sequence Axis
**Hypothesis**: Architect-first evaluation catches technical blockers before PM spends time on structural completeness — REAL-REQUIRED from a hard architectural contradiction is worth surfacing before softer structural gaps.

---

```markdown
# /quest:mock-review

You are performing mock coverage review for Signal skill artifact `{topic}`.
This skill reads the source mock artifact, applies automatic classification rules,
evaluates non-auto namespaces by three roles in sequence, writes decisions back
into the artifact Status fields, and produces a prioritized next-steps list.

---

## STEP 0 — READ INPUTS

Read the source mock artifact for `{topic}`.
Identify every namespace block. Each block has a `Status:` field.

State at the top of your output:
```
Tier: {N}  source: {TOPICS.md | default-Tier-1}
Namespaces found: {comma-separated list}
```

Do not proceed until all namespace names are listed.

---

## STEP 1 — AUTOMATIC CLASSIFICATION

Apply these three rules in order. Rules are not role-overridable.

**Rule 1 — EVIDENCE-HEAVY**
If a namespace is tagged `evidence-heavy` in the mock artifact or in TOPICS.md:
→ Decision: REAL-REQUIRED
→ trigger = EVIDENCE-HEAVY
DO NOT mark an EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock
quality, role consensus, or completeness of structural coverage.

**Rule 2 — TIER-CRITICAL**
If Tier >= 2 AND namespace is one of: `trace`, `scout-feasibility`, `listen`:
→ Decision: REAL-REQUIRED
→ trigger = TIER-CRITICAL
DO NOT mark a TIER-CRITICAL namespace MOCK-ACCEPTED regardless of how well
structured the mock data appears.

**Rule 3 — COMPLIANCE**
If the namespace is tagged `compliance` in the mock artifact or TOPICS.md:
→ Decision: REAL-REQUIRED
→ trigger = COMPLIANCE
DO NOT mark a COMPLIANCE-TAGGED namespace MOCK-ACCEPTED under any conditions.

Output the auto-classification list:
```
AUTO-CLASSIFIED:
- {namespace}: REAL-REQUIRED  trigger = {rule label}
...
REMAINING FOR EVALUATION:
- {namespace}
...
```

**STOP. Do not proceed to STEP 2 until all auto-classified namespaces are listed
and the remaining list is confirmed. DO NOT apply role evaluation to any
namespace in the AUTO-CLASSIFIED list.**

---

## STEP 2 — ARCHITECT EVALUATION (runs first)

For each namespace in the REMAINING list, Architect evaluates technical
plausibility. Architect runs before PM because a hard architectural contradiction
makes structural completeness analysis moot.

Architect sub-questions (each answer must name a specific artifact, element,
or architectural fact — "yes/no" answers do not satisfy these questions):

- **ASQ-1**: What specific architectural component or interaction does this
  namespace's mock data need to represent? Name the component.
- **ASQ-2**: What specific architectural invariant, known constraint, or
  platform fact (e.g., event delivery guarantees, state machine boundaries)
  would be violated if mock data were treated as real evidence here? Name it.
- **ASQ-3**: Name the specific data shape, protocol, or dependency contract
  that mock generation cannot plausibly reproduce without real system execution.
  If none, name what structural feature makes mock plausible.

Architect verdict: `PLAUSIBLE` | `CONTRADICTS-ARCHITECTURE`

If `CONTRADICTS-ARCHITECTURE`:
→ Decision: REAL-REQUIRED (evaluation-driven)
→ Artifact state: {the specific invariant named in ASQ-2 that mock cannot satisfy}
→ Record in block: `architect-verdict = CONTRADICTS-ARCHITECTURE`

If `PLAUSIBLE`:
→ Namespace passes to PM evaluation.

Output format per namespace:
```
ARCHITECT — {namespace}
ASQ-1: {answer naming specific component}
ASQ-2: {answer naming specific invariant}
ASQ-3: {answer naming specific contract or structural feature}
Verdict: {PLAUSIBLE | CONTRADICTS-ARCHITECTURE}
```

**DO NOT proceed to STEP 3 until all REMAINING namespaces have an Architect
verdict. DO NOT apply PM evaluation to namespaces with
`architect-verdict = CONTRADICTS-ARCHITECTURE`.**

---

## STEP 3 — PM EVALUATION

For each namespace that passed Architect with `PLAUSIBLE`:

PM sub-questions:

- **PSQ-1**: Name the specific section, table, or gate in the mock artifact
  that covers the happy-path scenario for this namespace. If absent, name the
  gap.
- **PSQ-2**: Name the specific section, table, or gate that covers at least
  one failure or boundary condition. If absent, name the gap.
- **PSQ-3**: What specific structural decision, tier boundary, or feature gate
  does this namespace's data need to support? Name the decision.

PM verdict: `STRUCTURALLY-COMPLETE` | `STRUCTURAL-GAP`

If `STRUCTURAL-GAP`:
→ Decision: REAL-REQUIRED (evaluation-driven)
→ Artifact state: {the specific gap named in PSQ-1 or PSQ-2}
→ Record: `pm-verdict = STRUCTURAL-GAP`

If `STRUCTURALLY-COMPLETE`:
→ Namespace passes to Strategy evaluation.

Output format per namespace:
```
PM — {namespace}
PSQ-1: {answer naming specific section/gate}
PSQ-2: {answer naming specific section/gate}
PSQ-3: {answer naming specific decision}
Verdict: {STRUCTURALLY-COMPLETE | STRUCTURAL-GAP}
```

**DO NOT proceed to STEP 4 until all PLAUSIBLE namespaces have a PM verdict.**

---

## STEP 4 — STRATEGY EVALUATION

For each namespace that passed both Architect and PM:

DEFAULT DECISION POSITION: REAL-REQUIRED.
MOCK-ACCEPTED is an earned escape that requires a positive argument against the
default. A namespace that is merely not-failed is not MOCK-ACCEPTED.

Strategy sub-questions:

- **SSQ-1**: What specific tier decision or feature gate does this namespace
  feed? Name the decision. (This answer anchors the Structural position slot.)
- **SSQ-2**: Name the specific coverage threshold this namespace's mock data
  must meet to be adequate for the tier decision named in SSQ-1. Does the
  mock artifact meet it?
- **SSQ-3**: Name the specific risk that would remain undetected if mock data
  were accepted here instead of real evidence.

Strategy verdict: `COVERAGE-ADEQUATE` | `COVERAGE-INSUFFICIENT`

If `COVERAGE-INSUFFICIENT`:
→ Decision: REAL-REQUIRED (evaluation-driven)
→ Artifact state: {the specific risk named in SSQ-3}

If `COVERAGE-ADEQUATE`:
→ Proceed to MOCK-ACCEPTED decision block below.

```
STRATEGY — {namespace}
SSQ-1: {answer naming specific tier decision}
SSQ-2: {answer naming specific threshold + pass/fail}
SSQ-3: {answer naming specific risk}
Verdict: {COVERAGE-ADEQUATE | COVERAGE-INSUFFICIENT}
```

---

## STEP 5 — DECISIONS OUTPUT

Produce the full decision list. Format each entry as:

**REAL-REQUIRED (auto-classified):**
```
{namespace}: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}
```

**REAL-REQUIRED (evaluation-driven):**
```
{namespace}: REAL-REQUIRED
  trigger = {ARCHITECT-CONTRADICTS | PM-STRUCTURAL-GAP | STRATEGY-COVERAGE-INSUFFICIENT}
  driving-verdict: {role} found: {specific SQ answer that drove the verdict}
  artifact-state: {what mock cannot satisfy}
```

**MOCK-ACCEPTED:**
```
{namespace}: MOCK-ACCEPTED
  reason-code: {STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT}
  structural-position: {specific tier decision this namespace feeds, from SSQ-1}
  contrast: {why this namespace does not cross the threshold that would require
    real evidence — naming the specific structural features that make mock
    adequate here, contrasted against what a trace or scout-feasibility
    namespace would require}
```

The `contrast:` slot must produce a contrastive sentence — not a confirmatory
sentence. "Structural coverage is sufficient here" does not satisfy the slot.
"This namespace has no tier-gating decisions and no platform-invariant
dependencies, unlike trace where event delivery guarantees require real
execution" satisfies the slot.

**STOP. Do not proceed to STEP 6 until every namespace has exactly one
decision entry.**

---

## STEP 6 — STATUS WRITE-BACK (mandatory)

For each namespace, edit the source mock artifact's Status field in-place:

- REAL-REQUIRED: `Status: REAL-REQUIRED  trigger = {rule label}`
- MOCK-ACCEPTED: `Status: MOCK-ACCEPTED  reason = {reason-code}`

After completing all edits, output the confirmation canary:

```
WRITE-BACK COMPLETE: 0 Status fields remain as `MOCK (awaiting review)`.
```

**PROHIBITION**: Do not output the confirmation canary if any Status field
remains as `MOCK (awaiting review)`. Writing the canary when the condition is
not met is a named error: FALSE-CANARY. The canary's presence asserts the
condition is fully satisfied.

---

## STEP 7 — NEXT-STEPS LIST

Produce a prioritized next-steps list. State the ordering rule explicitly:

**Ordering rule**: Tier-critical namespaces (trace, scout-feasibility, listen)
first; then other REAL-REQUIRED namespaces ordered by evaluation-driven verdict
severity (ARCHITECT-CONTRADICTS before PM-STRUCTURAL-GAP before
STRATEGY-COVERAGE-INSUFFICIENT); then EVIDENCE-HEAVY last.

Entry format (artifact state propagated forward):
```
/{skill-id} {topic} — {artifact state from decision block}
```

Cross-namespace risk statement (required):
After the list, write one sentence naming the highest-concentration risk across
all REAL-REQUIRED decisions — the pattern or theme that, if unresolved, blocks
the most downstream work.

Urgency grouping: Label groups IMMEDIATE / BEFORE-COMMIT / DEFER with
a one-sentence criterion for each group boundary.
```

---

## V-02 — Inertia Framing Axis
**Hypothesis**: Establishing REAL-REQUIRED as an explicit named default position at the top of the skill — before any rules or evaluation appear — forces every MOCK-ACCEPTED decision to produce a genuine contrastive argument rather than a confirmatory one. The inversion is structural, not advisory.

---

```markdown
# /quest:mock-review

---

## DEFAULT DECISION POSITION

**REAL-REQUIRED is the default decision for every namespace.**

MOCK-ACCEPTED is not a symmetric alternative. It is an earned escape from the
default that requires a positive argument. A namespace is REAL-REQUIRED unless
it survives all three escape tests:

1. Not auto-flagged by any automatic rule (EVIDENCE-HEAVY, TIER-CRITICAL,
   COMPLIANCE).
2. No role evaluation finds a blocker.
3. Strategy confirms mock coverage is adequate for the specific tier decision
   this namespace feeds — and produces a contrastive argument explaining why
   this namespace does not cross the real-evidence threshold.

A namespace that merely passes all sub-questions without failing is not
MOCK-ACCEPTED. The author must argue against the default.

---

## STEP 0 — READ + TIER

Read source mock artifact for `{topic}`. List every namespace found.

```
Tier: {N}  source: {TOPICS.md | default-Tier-1}
Namespaces: {list}
```

---

## STEP 1 — AUTOMATIC RULES  *(non-overridable)*

Rules fire before any role evaluation. Role verdicts cannot reverse them.

**EVIDENCE-HEAVY rule**
Trigger: namespace tagged `evidence-heavy`.
→ REAL-REQUIRED  trigger = EVIDENCE-HEAVY
Forbidden output: DO NOT mark EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
of mock completeness, role consensus, or any other factor.

**TIER-CRITICAL rule**
Trigger: Tier >= 2 AND namespace ∈ {trace, scout-feasibility, listen}.
→ REAL-REQUIRED  trigger = TIER-CRITICAL
Forbidden output: DO NOT mark TIER-CRITICAL namespace MOCK-ACCEPTED regardless
of how well-structured the mock data appears.

**COMPLIANCE rule**
Trigger: namespace tagged `compliance`.
→ REAL-REQUIRED  trigger = COMPLIANCE
Forbidden output: DO NOT mark COMPLIANCE-TAGGED namespace MOCK-ACCEPTED under
any conditions.

Output:
```
AUTO-CLASSIFIED (REAL-REQUIRED):
  {namespace}  trigger = {rule}
  ...
REMAINING (subject to role evaluation):
  {namespace}
  ...
```

**═══ HARD GATE ═══**
DO NOT apply role evaluation to any AUTO-CLASSIFIED namespace.
Applying role evaluation to an auto-classified namespace is a named error:
CONTAMINATION. Proceed to STEP 2 only for REMAINING namespaces.

---

## STEP 2 — ROLE EVALUATION

The three-role evaluation is an attempt to defeat the REAL-REQUIRED default.
Each role is a separately completable step. A namespace must survive all three
to reach MOCK-ACCEPTED.

### STEP 2a — PM Evaluation

PM asks: does structural completeness justify escaping the default?

Sub-questions (each must name a specific artifact, section, or gate):
- **PSQ-1**: Name the specific section or gate in the mock artifact covering
  the happy-path scenario for this namespace. If absent, name the gap.
- **PSQ-2**: Name the specific section or gate covering at least one failure
  or boundary condition. If absent, name the gap.
- **PSQ-3**: Name the specific tier decision or feature gate that this
  namespace's structural coverage must support.

PM verdict: `PASSES-PM` | `BLOCKED-PM`

Blocked: → REAL-REQUIRED (evaluation-driven), artifact-state = {gap named}
Passes: → continue to STEP 2b.

```
PM — {namespace}
PSQ-1: {answer}
PSQ-2: {answer}
PSQ-3: {answer}
Verdict: {PASSES-PM | BLOCKED-PM}
```

**DO NOT proceed to STEP 2b until all REMAINING namespaces have PM verdicts.
DO NOT apply Architect evaluation to BLOCKED-PM namespaces.**

### STEP 2b — Architect Evaluation

Architect asks: does technical plausibility justify escaping the default?

Sub-questions:
- **ASQ-1**: Name the specific architectural component or interaction this
  namespace's mock data must represent.
- **ASQ-2**: Name the specific architectural invariant or platform constraint
  that would be violated if mock data were treated as real evidence here.
  If no violation exists, name the structural feature that makes mock plausible.
- **ASQ-3**: Name the specific dependency contract or data shape that mock
  generation cannot reproduce without real system execution. If none, name it
  explicitly.

Architect verdict: `PASSES-ARCHITECT` | `BLOCKED-ARCHITECT`

Blocked: → REAL-REQUIRED (evaluation-driven), artifact-state = {invariant named}
Passes: → continue to STEP 2c.

```
ARCHITECT — {namespace}
ASQ-1: {answer}
ASQ-2: {answer}
ASQ-3: {answer}
Verdict: {PASSES-ARCHITECT | BLOCKED-ARCHITECT}
```

**DO NOT proceed to STEP 2c until all PASSES-PM namespaces have Architect
verdicts. DO NOT apply Strategy evaluation to BLOCKED-ARCHITECT namespaces.**

### STEP 2c — Strategy Evaluation

Strategy asks: is mock coverage adequate for the specific tier decision at stake?
This is the final escape test. Failing here returns the namespace to the default.

Sub-questions:
- **SSQ-1**: What specific tier decision does this namespace feed? Name it.
  (This answer becomes the `structural-position` field in any MOCK-ACCEPTED
  decision block.)
- **SSQ-2**: Name the specific coverage threshold the mock artifact must meet
  for the decision named in SSQ-1. Does the artifact meet it?
- **SSQ-3**: Name the specific risk that would remain if mock data were accepted
  here. This risk drives the `contrast:` slot: if the risk is structural rather
  than execution-dependent, that supports MOCK-ACCEPTED; if execution-dependent,
  REAL-REQUIRED.

Strategy verdict: `PASSES-STRATEGY` | `BLOCKED-STRATEGY`

Blocked: → REAL-REQUIRED (evaluation-driven), artifact-state = {risk named}
Passes: → proceed to MOCK-ACCEPTED decision block.

---

## STEP 3 — DECISIONS OUTPUT

**REAL-REQUIRED (auto):**
```
{namespace}: REAL-REQUIRED
  trigger = {rule label}
```

**REAL-REQUIRED (evaluation-driven):**
```
{namespace}: REAL-REQUIRED
  trigger = {BLOCKED-PM | BLOCKED-ARCHITECT | BLOCKED-STRATEGY}
  driving-SQ: {role} {SQ-id}: {exact SQ answer that produced the block}
  artifact-state: {what the mock cannot satisfy}
```

**MOCK-ACCEPTED** (only for namespaces that survived all three escape tests):

The MOCK-ACCEPTED block encodes the argument against the REAL-REQUIRED default.
Both slots are required. A block with only `structural-position` or only
`contrast` is incomplete and must be revised.

```
{namespace}: MOCK-ACCEPTED
  reason-code: {STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT}
  structural-position: {specific tier decision this namespace feeds — from SSQ-1}
  contrast: {one sentence naming what structural features make mock adequate here,
    contrasted against what a trace or scout-feasibility namespace would require —
    naming the specific threshold this namespace does not cross and why}
```

**Contrast slot grammar rule**: The contrast sentence must name a threshold
that the namespace does NOT cross. "Structural coverage is sufficient here"
is a confirmatory sentence and does not satisfy this slot. A satisfying sentence
names both sides: what this namespace lacks (making mock adequate) and what a
threshold-crossing namespace would have.

---

## STEP 4 — STATUS WRITE-BACK

Edit source artifact Status fields in-place:
- → `Status: REAL-REQUIRED  trigger = {rule or blocked-label}`
- → `Status: MOCK-ACCEPTED  reason = {reason-code}`

Required output after all edits:
```
WRITE-BACK COMPLETE: 0 Status fields remain as `MOCK (awaiting review)`.
```

**CANARY PROHIBITION**: This statement asserts all Status fields are updated.
Do not write it if any Status field remains `MOCK (awaiting review)`. Writing
the canary under false conditions is a named error: FALSE-CANARY.

---

## STEP 5 — NEXT-STEPS

Ordering rule (state this explicitly in output):
Tier-critical REAL-REQUIRED first → other REAL-REQUIRED by blocker type →
EVIDENCE-HEAVY last.

Entry format:
```
/{skill-id} {topic} — {artifact-state}
```

Then: one cross-namespace risk statement naming the dominant unresolved theme.
Then: urgency grouping (IMMEDIATE / BEFORE-COMMIT / DEFER) with one-sentence
criterion per boundary.
```

---

## V-03 — Lifecycle Emphasis Axis
**Hypothesis**: Hard-labeled, numbered phases with explicit PROCEED/STOP gates at every boundary reduce contamination risk and make the skill mechanically verifiable. Each phase is completable in isolation; gates name the specific next phase being blocked.

---

```markdown
# /quest:mock-review

---

## PHASE 1 OF 5 — INPUT ACQUISITION

**Action**: Read source mock artifact for `{topic}`.

**Required output before proceeding**:
```
=== PHASE 1 OUTPUT ===
Tier: {N}  source: {TOPICS.md | default-Tier-1}
Namespaces found ({count}):
  1. {namespace}
  2. {namespace}
  ...
Status fields found: {count} × "MOCK (awaiting review)"
=====================
```

**GATE 1→2**: All namespace names listed AND tier sourced.
DO NOT proceed to PHASE 2 until GATE 1→2 is satisfied.

---

## PHASE 2 OF 5 — AUTOMATIC CLASSIFICATION

**Purpose**: Apply non-overridable rules. Rules fire independently of and prior
to any role evaluation. Role verdicts cannot reverse Phase 2 decisions.

**Rule A — EVIDENCE-HEAVY**
Condition: namespace tagged `evidence-heavy` in artifact or TOPICS.md.
Result: REAL-REQUIRED  `trigger = EVIDENCE-HEAVY`
Enforcement: DO NOT mark an EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
of mock quality, structural completeness, or any role consensus.

**Rule B — TIER-CRITICAL**
Condition: Tier >= 2 AND namespace ∈ {trace, scout-feasibility, listen}.
Result: REAL-REQUIRED  `trigger = TIER-CRITICAL`
Enforcement: DO NOT mark a TIER-CRITICAL namespace MOCK-ACCEPTED regardless
of how well the mock artifact appears structured.

**Rule C — COMPLIANCE**
Condition: namespace tagged `compliance` in artifact or TOPICS.md.
Result: REAL-REQUIRED  `trigger = COMPLIANCE`
Enforcement: DO NOT mark a COMPLIANCE-TAGGED namespace MOCK-ACCEPTED under
any conditions whatsoever.

**Required output before proceeding**:
```
=== PHASE 2 OUTPUT ===
AUTO-CLASSIFIED:
  {namespace}  REAL-REQUIRED  trigger = {rule label}
  ...
REMAINING FOR EVALUATION ({count}):
  {namespace}
  ...
=====================
```

**GATE 2→3**: Every namespace is in exactly one list (AUTO-CLASSIFIED or
REMAINING). No namespace is absent from both lists.
**CONTAMINATION GUARD**: After GATE 2→3 is satisfied, role evaluation in
PHASE 3 applies ONLY to REMAINING namespaces. DO NOT apply role evaluation
to any AUTO-CLASSIFIED namespace. Applying evaluation to an auto-classified
namespace is a named error: CONTAMINATION. If CONTAMINATION is detected,
halt and re-output PHASE 2 before continuing.
DO NOT proceed to PHASE 3 until GATE 2→3 is satisfied.

---

## PHASE 3 OF 5 — ROLE EVALUATION

Applies to REMAINING namespaces only.

Each role is a separately completable sub-phase with its own gate.

---

### PHASE 3a — PM EVALUATION

For each REMAINING namespace, PM assesses structural completeness.

PM sub-questions (answers must name specific sections, gates, or tables — not
produce yes/no or general assessments):

**PSQ-1**: Name the specific section or gate in the mock artifact that covers
the happy-path scenario for this namespace. If absent, name the gap explicitly.

**PSQ-2**: Name the specific section or gate covering at least one failure or
boundary condition. If absent, name the gap.

**PSQ-3**: Name the specific tier decision, feature gate, or structural decision
this namespace's coverage must support.

PM verdict options:
- `PM: PASS` — all three sub-questions answered with named artifacts, no gaps
- `PM: FAIL` — one or more sub-questions identifies a gap

**Required output format per namespace**:
```
PM — {namespace}
  PSQ-1: {answer naming specific section/gate or naming gap}
  PSQ-2: {answer naming specific section/gate or naming gap}
  PSQ-3: {answer naming specific decision}
  PM verdict: {PASS | FAIL}
  [If FAIL] artifact-state: {gap name from PSQ-1 or PSQ-2}
```

**GATE 3a→3b**: All REMAINING namespaces have PM verdicts.
DO NOT proceed to PHASE 3b until GATE 3a→3b is satisfied.
DO NOT apply Architect evaluation to PM-FAIL namespaces.

---

### PHASE 3b — ARCHITECT EVALUATION

For each namespace with PM: PASS, Architect assesses technical plausibility.

Architect sub-questions:

**ASQ-1**: Name the specific architectural component or interaction that this
namespace's mock data must represent.

**ASQ-2**: Name the specific architectural invariant, platform constraint, or
known system behavior that would be violated if mock data were substituted for
real evidence here. If no violation exists, name the structural feature that
makes mock technically plausible.

**ASQ-3**: Name the specific data shape, protocol, or execution-time contract
that mock generation cannot reproduce. If none exists, name that explicitly.

Architect verdict:
- `ARCHITECT: PASS` — technically plausible, no invariant violations
- `ARCHITECT: FAIL` — specific invariant named that mock cannot satisfy

**Required output format per namespace**:
```
ARCHITECT — {namespace}
  ASQ-1: {answer}
  ASQ-2: {answer naming invariant or structural feature}
  ASQ-3: {answer naming contract or naming its absence}
  ARCHITECT verdict: {PASS | FAIL}
  [If FAIL] artifact-state: {invariant from ASQ-2}
```

**GATE 3b→3c**: All PM-PASS namespaces have Architect verdicts.
DO NOT proceed to PHASE 3c until GATE 3b→3c is satisfied.
DO NOT apply Strategy evaluation to ARCHITECT-FAIL namespaces.

---

### PHASE 3c — STRATEGY EVALUATION

For each namespace with ARCHITECT: PASS, Strategy assesses coverage adequacy.

Strategy sub-questions:

**SSQ-1**: What specific tier decision or feature gate does this namespace feed?
Name it. (This answer populates the `structural-position:` slot in any
MOCK-ACCEPTED block produced in PHASE 4.)

**SSQ-2**: Name the specific coverage threshold the mock artifact must meet
for the decision named in SSQ-1. Does the artifact meet this threshold?

**SSQ-3**: Name the specific detection risk that would persist if mock data
replaced real evidence here. If risk is purely structural (discoverable without
execution), mock may be adequate. If risk is execution-dependent, real evidence
is required.

Strategy verdict:
- `STRATEGY: PASS` — coverage adequate for the stated tier decision
- `STRATEGY: FAIL` — specific coverage gap or execution-dependent risk named

**Required output format per namespace**:
```
STRATEGY — {namespace}
  SSQ-1: {answer naming specific decision}
  SSQ-2: {answer naming threshold + pass/fail assessment}
  SSQ-3: {answer naming specific risk and its type: structural | execution-dependent}
  STRATEGY verdict: {PASS | FAIL}
  [If FAIL] artifact-state: {risk from SSQ-3}
```

**GATE 3c→4**: All ARCHITECT-PASS namespaces have Strategy verdicts.
DO NOT proceed to PHASE 4 until GATE 3c→4 is satisfied.

---

## PHASE 4 OF 5 — DECISIONS OUTPUT

Compile complete decision list. Every namespace must appear exactly once.

**REAL-REQUIRED (auto-classified)**:
```
{namespace}: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}
```

**REAL-REQUIRED (evaluation-driven)**:
```
{namespace}: REAL-REQUIRED
  trigger = {PM-FAIL | ARCHITECT-FAIL | STRATEGY-FAIL}
  driving-verdict: {Role} {SQ-id} answer: "{exact SQ answer text}"
  artifact-state: {what mock cannot satisfy — propagates to next-steps}
```

**MOCK-ACCEPTED** (only for namespaces passing all three evaluation phases):
```
{namespace}: MOCK-ACCEPTED
  reason-code: {STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT}
  structural-position: {tier decision from SSQ-1}
  contrast: {contrastive sentence naming what this namespace lacks that would
    require real evidence — explicitly naming the threshold it does not cross,
    contrasted against what trace or scout-feasibility would require}
```

`contrast:` must not be a confirmatory sentence. It must name a threshold
and name this namespace's structural position relative to that threshold.

**GATE 4→5**: Every namespace has exactly one decision entry.
DO NOT proceed to PHASE 5 until GATE 4→5 is satisfied.

---

## PHASE 5 OF 5 — WRITE-BACK AND NEXT-STEPS

### 5a — STATUS WRITE-BACK

Edit source artifact Status fields in-place:
- REAL-REQUIRED: `Status: REAL-REQUIRED  trigger = {label}`
- MOCK-ACCEPTED: `Status: MOCK-ACCEPTED  reason = {reason-code}`

Edit every namespace. No Status field may remain as `MOCK (awaiting review)`.

Required confirmation output:
```
WRITE-BACK COMPLETE: 0 Status fields remain as `MOCK (awaiting review)`.
```

**CANARY RULE**: This statement is a canary. Its presence asserts the condition
is satisfied. Do not output it if any Status field remains unchanged. Writing
it when the condition is false is the named error: FALSE-CANARY.

### 5b — NEXT-STEPS LIST

Ordering rule (state verbatim in output): Tier-critical REAL-REQUIRED first
(trace, scout-feasibility, listen), then other evaluation-driven REAL-REQUIRED
ordered by blocker type (ARCHITECT-FAIL → PM-FAIL → STRATEGY-FAIL), then
EVIDENCE-HEAVY auto-classified last.

Entry format (artifact-state field propagated from PHASE 4):
```
/{skill-id} {topic} — {artifact-state}
```

Cross-namespace risk statement: one sentence naming the dominant unresolved
theme across all REAL-REQUIRED decisions.

Urgency groups: IMMEDIATE / BEFORE-COMMIT / DEFER with one-sentence criterion
per boundary.
```

---

## V-04 — Combination: Inertia Framing + Lifecycle Emphasis
**Hypothesis**: Decision inversion (B) combined with explicit phase gates (C) close two distinct failure modes simultaneously — confirmatory-escape in MOCK-ACCEPTED rationale, and contamination of auto-classified namespaces. Neither axis alone closes both.

---

```markdown
# /quest:mock-review

---

## DECISION INVERSION FRAME

This skill operates under decision inversion.

**Default position: REAL-REQUIRED.**
Every namespace is REAL-REQUIRED unless it survives automatic rule screening
AND all three role evaluations AND produces a positive contrastive argument
that it does not cross the real-evidence threshold. MOCK-ACCEPTED is not a
default outcome for namespaces that merely avoid failure — it requires an
argument against the default.

This inversion is in effect throughout all phases. It governs the `contrast:`
slot requirement in PHASE 4: a confirmatory sentence restates the default
escape as an assertion rather than an argument and does not satisfy the slot.

---

## PHASE 1 — INPUT

Read source mock artifact for `{topic}`.

```
Tier: {N}  source: {TOPICS.md | default-Tier-1}
Namespaces ({count}): {list}
```

**GATE 1→2**: Tier sourced, all namespaces listed.

---

## PHASE 2 — AUTOMATIC CLASSIFICATION (non-overridable)

Rules apply before role evaluation. Role verdicts do not affect Phase 2 outputs.

| Rule | Trigger | Result | Forbidden output |
|------|---------|--------|------------------|
| EVIDENCE-HEAVY | `evidence-heavy` tag | REAL-REQUIRED | DO NOT mark MOCK-ACCEPTED regardless of mock quality or role consensus |
| TIER-CRITICAL | Tier ≥ 2 AND ns ∈ {trace, scout-feasibility, listen} | REAL-REQUIRED | DO NOT mark MOCK-ACCEPTED regardless of mock structure |
| COMPLIANCE | `compliance` tag | REAL-REQUIRED | DO NOT mark MOCK-ACCEPTED under any conditions |

Output:
```
AUTO-CLASSIFIED: {namespace}  trigger = {rule label}
REMAINING: {namespace list}
```

**GATE 2→3**: Every namespace is in exactly one list.
**CONTAMINATION GUARD**: Role evaluation in PHASE 3 applies to REMAINING only.
DO NOT apply evaluation to AUTO-CLASSIFIED namespaces. This error is named:
CONTAMINATION. A contaminated output must be regenerated from PHASE 2.

---

## PHASE 3 — ROLE EVALUATION  *(REMAINING namespaces only)*

Evaluation is an attempt to defeat the REAL-REQUIRED default for each namespace.
Three sequential sub-phases. A namespace blocked in any sub-phase does not
advance. Each sub-phase has its own gate.

### PHASE 3a — PM

PM asks: does structural completeness justify escaping the default?

Sub-questions (answers must name specific artifacts — yes/no answers fail):
- **PSQ-1**: Name the section or gate covering the happy-path scenario, or name
  the gap.
- **PSQ-2**: Name the section or gate covering a failure or boundary condition,
  or name the gap.
- **PSQ-3**: Name the specific structural decision this namespace's coverage must
  support.

```
PM — {ns}
PSQ-1: {named artifact or named gap}
PSQ-2: {named artifact or named gap}
PSQ-3: {named decision}
PM: {PASS | FAIL}
[FAIL] artifact-state: {gap}
```

**GATE 3a→3b**: All REMAINING have PM verdicts.
DO NOT apply Architect to PM-FAIL namespaces.
DO NOT proceed to PHASE 3b until GATE 3a→3b is satisfied.

### PHASE 3b — ARCHITECT

Architect asks: does technical plausibility justify escaping the default?

- **ASQ-1**: Name the architectural component this namespace's mock must
  represent.
- **ASQ-2**: Name the specific invariant that would be violated by treating
  mock as real evidence, or name the feature making mock plausible.
- **ASQ-3**: Name the execution-time contract mock cannot reproduce, or state
  none explicitly.

```
ARCHITECT — {ns}
ASQ-1: {component}
ASQ-2: {invariant or plausibility feature}
ASQ-3: {contract or explicit none}
ARCHITECT: {PASS | FAIL}
[FAIL] artifact-state: {invariant}
```

**GATE 3b→3c**: All PM-PASS have Architect verdicts.
DO NOT apply Strategy to ARCHITECT-FAIL namespaces.
DO NOT proceed to PHASE 3c until GATE 3b→3c is satisfied.

### PHASE 3c — STRATEGY

Strategy asks: is coverage adequate for the tier decision at stake, and can
the author produce a genuine contrastive argument against the REAL-REQUIRED default?

- **SSQ-1**: Name the specific tier decision this namespace feeds. (Becomes
  `structural-position:` in the MOCK-ACCEPTED block.)
- **SSQ-2**: Name the coverage threshold required for SSQ-1's decision and
  assess whether the artifact meets it.
- **SSQ-3**: Name the detection risk that would persist if mock replaced real
  evidence. Classify it: `structural` (mock can cover it) or
  `execution-dependent` (real evidence required).

```
STRATEGY — {ns}
SSQ-1: {named decision}
SSQ-2: {threshold + pass/fail}
SSQ-3: {named risk — structural | execution-dependent}
STRATEGY: {PASS | FAIL}
[FAIL] artifact-state: {risk}
```

**GATE 3c→4**: All ARCHITECT-PASS have Strategy verdicts.
DO NOT proceed to PHASE 4 until GATE 3c→4 is satisfied.

---

## PHASE 4 — DECISIONS

**Default reminder**: REAL-REQUIRED unless argued out. Every MOCK-ACCEPTED entry
must carry a contrastive argument, not an assertion of adequacy.

**REAL-REQUIRED (auto)**:
```
{ns}: REAL-REQUIRED
  trigger = {rule label}
```

**REAL-REQUIRED (evaluation-driven)**:
```
{ns}: REAL-REQUIRED
  trigger = {PM-FAIL | ARCHITECT-FAIL | STRATEGY-FAIL}
  driving-SQ: {Role} {SQ-id}: "{exact SQ answer}"
  artifact-state: {what mock cannot satisfy}
```

**MOCK-ACCEPTED** (earned escape from REAL-REQUIRED default):
```
{ns}: MOCK-ACCEPTED
  reason-code: {STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT}
  structural-position: {tier decision from SSQ-1}
  contrast: {contrastive sentence — must name the threshold this namespace does
    not cross AND what structural feature keeps it below that threshold, contrasted
    against what would require real evidence; confirmatory sentences ("adequate
    here") do not satisfy this slot}
```

**GATE 4→5**: Every namespace has exactly one decision entry.

---

## PHASE 5 — WRITE-BACK AND NEXT-STEPS

### Write-back

Edit source artifact Status fields in-place. No field may remain as
`MOCK (awaiting review)`.

```
WRITE-BACK COMPLETE: 0 Status fields remain as `MOCK (awaiting review)`.
```

CANARY PROHIBITION: Do not write this statement if any field remains unchanged.
Writing it falsely is the named error: FALSE-CANARY.

### Next-steps

**Ordering rule** (state explicitly): Tier-critical REAL-REQUIRED first
→ evaluation-driven REAL-REQUIRED by blocker type (ARCHITECT → PM → STRATEGY)
→ EVIDENCE-HEAVY auto-classified last.

Entry format (artifact-state propagated from Phase 4):
```
/{skill-id} {topic} — {artifact-state}
```

Cross-namespace risk statement: dominant unresolved theme in one sentence.
Urgency groups: IMMEDIATE / BEFORE-COMMIT / DEFER with one-sentence boundary
criteria.
```

---

## V-05 — Full Combination: Role Sequence + Inertia Framing + Lifecycle Emphasis + Structured Trigger Notation
**Hypothesis**: Architect-first evaluation (A) surfaces hard technical blockers before PM structural analysis, while decision inversion (B) + explicit gates (C) + parseable structured trigger fields (D) produce output that is mechanically verifiable at every decision point — the combination yields both better ordering and better auditability.

---

```markdown
# /quest:mock-review

---

## DECISION INVERSION FRAME

**Default position: REAL-REQUIRED.**

Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape that
requires passing three sequential role evaluations AND producing a two-part
rationale: a structural position statement (what tier decision this namespace
feeds) AND a contrast statement (why this namespace does not cross the
real-evidence threshold, named against what a threshold-crossing namespace would
require).

A namespace that passes all sub-questions without a blocking answer is not
automatically MOCK-ACCEPTED. The author must write the contrastive argument.
Confirmatory sentences assert the escape without arguing for it; they do not
satisfy the `contrast:` slot.

This frame applies throughout. It governs the template structure, the gate
logic, and the CANARY output.

---

## PHASE 1 — INPUT ACQUISITION

Read source mock artifact for `{topic}`.

Required output:
```
=== PHASE 1 ===
Tier: {N}  source: {TOPICS.md | default-Tier-1}
Namespaces ({count}): {list}
Status fields found: {count} × "MOCK (awaiting review)"
===============
```

**GATE 1→2**: Tier sourced, all namespaces listed.

---

## PHASE 2 — AUTOMATIC CLASSIFICATION

Rules are non-overridable. They fire before role evaluation. Role verdicts
cannot override Phase 2 decisions.

**Rule EVIDENCE-HEAVY**
Trigger condition: namespace tagged `evidence-heavy`.
Decision: REAL-REQUIRED
Structured trigger field: `trigger = EVIDENCE-HEAVY`
Forbidden output: DO NOT mark EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
of mock completeness, role consensus, or any other factor.

**Rule TIER-CRITICAL**
Trigger condition: Tier ≥ 2 AND namespace ∈ {trace, scout-feasibility, listen}.
Decision: REAL-REQUIRED
Structured trigger field: `trigger = TIER-CRITICAL`
Forbidden output: DO NOT mark TIER-CRITICAL namespace MOCK-ACCEPTED regardless
of apparent mock structure quality.

**Rule COMPLIANCE**
Trigger condition: namespace tagged `compliance`.
Decision: REAL-REQUIRED
Structured trigger field: `trigger = COMPLIANCE`
Forbidden output: DO NOT mark COMPLIANCE-TAGGED namespace MOCK-ACCEPTED under
any conditions.

Required output:
```
=== PHASE 2 ===
AUTO-CLASSIFIED:
  ns={namespace}  decision=REAL-REQUIRED  trigger={rule label}
  ...
REMAINING:
  ns={namespace}
  ...
===============
```

**GATE 2→3**: Every namespace appears in exactly one list.
**CONTAMINATION GUARD**: Phase 3 evaluation applies to REMAINING list only.
Applying role evaluation to any AUTO-CLASSIFIED namespace is the named error
CONTAMINATION. A CONTAMINATED output must be regenerated from Phase 2.
DO NOT proceed to PHASE 3 until GATE 2→3 is satisfied.

---

## PHASE 3 — ROLE EVALUATION  *(applies to REMAINING list only)*

Evaluation order: Architect → PM → Strategy.

Rationale for ordering: Architect first surfaces architectural invariant
violations that make structural completeness analysis moot. PM second assesses
structural completeness for technically plausible namespaces. Strategy third
assesses coverage adequacy for structurally complete, plausible namespaces.

A namespace blocked at any sub-phase does not advance.

---

### PHASE 3a — ARCHITECT EVALUATION

Architect: is mock data technically plausible for this namespace?

Sub-questions (answers must name specific artifacts — present-tense artifact
naming required, e.g., "Section 4.3 has no fallback path"; past-tense verdict
restatements are the named error VERDICT-ECHO and do not satisfy these questions):

**ASQ-1**: Name the specific architectural component or interaction that this
namespace's mock data must represent.

**ASQ-2**: Name the specific architectural invariant, platform constraint, or
known system behavior that would be violated if mock data substituted for real
evidence. If no violation exists, name the structural feature that makes mock
technically plausible for this namespace.

**ASQ-3**: Name the specific execution-time contract or data shape that mock
generation cannot reproduce without real system execution. If none exists,
state that explicitly with the name of the feature that removes this barrier.

Architect verdict:
- `ARCH-PASS`: mock is technically plausible; no invariant violation found
- `ARCH-FAIL`: specific invariant or contract violation named; mock cannot
  satisfy it

Required output per namespace:
```
ARCHITECT — {namespace}
  ASQ-1: {named component}
  ASQ-2: {named invariant | named plausibility feature}
  ASQ-3: {named contract | explicit none with feature name}
  arch-verdict = {ARCH-PASS | ARCH-FAIL}
  [ARCH-FAIL] artifact-state: {invariant from ASQ-2}
```

**GATE 3a→3b**: All REMAINING namespaces have arch-verdict fields.
DO NOT apply PM evaluation to ARCH-FAIL namespaces.
DO NOT proceed to PHASE 3b until GATE 3a→3b is satisfied.

---

### PHASE 3b — PM EVALUATION

PM: does structural completeness justify escaping the REAL-REQUIRED default?

Applies to ARCH-PASS namespaces only.

Sub-questions (present-tense artifact naming required; VERDICT-ECHO prohibited):

**PSQ-1**: Name the specific section, table, or gate in the mock artifact that
covers the happy-path scenario for this namespace. If absent, name the gap.

**PSQ-2**: Name the specific section, table, or gate covering at least one
failure or boundary condition for this namespace. If absent, name the gap.

**PSQ-3**: Name the specific tier decision, feature gate, or structural decision
this namespace's coverage must support to justify escaping REAL-REQUIRED.

PM verdict:
- `PM-PASS`: named sections/gates present for both happy-path and
  failure/boundary; no structural gaps
- `PM-FAIL`: one or more gaps named; structural completeness insufficient

Required output per namespace:
```
PM — {namespace}
  PSQ-1: {named section/gate | named gap}
  PSQ-2: {named section/gate | named gap}
  PSQ-3: {named decision}
  pm-verdict = {PM-PASS | PM-FAIL}
  [PM-FAIL] artifact-state: {gap from PSQ-1 or PSQ-2}
```

**GATE 3b→3c**: All ARCH-PASS namespaces have pm-verdict fields.
DO NOT apply Strategy evaluation to PM-FAIL namespaces.
DO NOT proceed to PHASE 3c until GATE 3b→3c is satisfied.

---

### PHASE 3c — STRATEGY EVALUATION

Strategy: is coverage adequate for the specific tier decision at stake, and
can the author argue against the REAL-REQUIRED default?

Applies to PM-PASS namespaces only.

Sub-questions (present-tense artifact naming required; VERDICT-ECHO prohibited):

**SSQ-1**: What specific tier decision or feature gate does this namespace feed?
Name it. This answer becomes the `structural-position:` field in any
MOCK-ACCEPTED block. Naming a generic structural role ("this namespace has
limited scope") without naming the specific decision does not satisfy SSQ-1.

**SSQ-2**: Name the specific coverage threshold the mock artifact must meet
for the decision named in SSQ-1. State whether the artifact meets this threshold
and name the evidence.

**SSQ-3**: Name the specific detection risk that would persist if mock replaced
real evidence. Classify it:
  - `structural`: discoverable without execution → mock may be adequate
  - `execution-dependent`: requires real system execution → REAL-REQUIRED

Strategy verdict:
- `STRAT-PASS`: coverage adequate; SSQ-3 risk is structural; contrastive
  argument producible
- `STRAT-FAIL`: coverage inadequate or SSQ-3 risk is execution-dependent

Required output per namespace:
```
STRATEGY — {namespace}
  SSQ-1: {named tier decision}
  SSQ-2: {named threshold + pass/fail with named evidence}
  SSQ-3: {named risk — structural | execution-dependent}
  strat-verdict = {STRAT-PASS | STRAT-FAIL}
  [STRAT-FAIL] artifact-state: {risk from SSQ-3}
```

**GATE 3c→4**: All PM-PASS namespaces have strat-verdict fields.
DO NOT proceed to PHASE 4 until GATE 3c→4 is satisfied.

---

## PHASE 4 — DECISIONS OUTPUT

Compile complete decision list. Every namespace appears exactly once.

**REAL-REQUIRED (auto-classified)**:
```
{namespace}: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}
```

**REAL-REQUIRED (evaluation-driven)**:
```
{namespace}: REAL-REQUIRED
  trigger = {ARCH-FAIL | PM-FAIL | STRAT-FAIL}
  driving-SQ: {Role} {SQ-id} — "{exact present-tense SQ answer}"
  artifact-state: {what mock cannot satisfy}
```

Note: The `driving-SQ` field distinguishes a genuine SQ answer from a verdict
restatement. "Section 4.3 has no fallback path documented" (present-tense
artifact naming) satisfies the field. "Architect found no fallback path"
(past-tense verdict restatement / VERDICT-ECHO) does not.

**MOCK-ACCEPTED** (earned escape from REAL-REQUIRED default):
Both slots are mandatory. A block missing either slot is incomplete.
```
{namespace}: MOCK-ACCEPTED
  reason-code: {STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT}
  structural-position: {specific tier decision from SSQ-1 — not a generic scope
    statement; names the decision this namespace feeds}
  contrast: {contrastive sentence naming (a) the structural features that keep
    this namespace below the real-evidence threshold AND (b) what a
    threshold-crossing namespace would have — e.g., "This namespace has no
    tier-gating decisions and no platform-invariant dependencies; unlike trace,
    where event delivery guarantees require real execution data, structural
    coverage is sufficient here because the decision it feeds [SSQ-1 decision]
    depends only on schema shape, not runtime behavior"}
```

**Contrast slot rule**: The sentence must name both sides. One side names
this namespace's structural features (why it does not cross the threshold).
The other side names what a threshold-crossing namespace would require.
A sentence with only one side is confirmatory, not contrastive, and does not
satisfy the slot.

**GATE 4→5**: Every namespace has exactly one decision entry.
DO NOT proceed to PHASE 5 until GATE 4→5 is satisfied.

---

## PHASE 5 — WRITE-BACK, NEXT-STEPS

### PHASE 5a — Status Write-Back

Edit source artifact Status fields in-place. Format:
- REAL-REQUIRED: `Status: REAL-REQUIRED  trigger = {label}`
- MOCK-ACCEPTED: `Status: MOCK-ACCEPTED  reason = {reason-code}`

All Status fields must be updated. No field may remain `MOCK (awaiting review)`.

Required confirmation:
```
WRITE-BACK COMPLETE: 0 Status fields remain as `MOCK (awaiting review)`.
```

**CANARY RULE**: This statement asserts the condition is fully satisfied.
Do not write it if any Status field remains unchanged. Writing it under false
conditions is the named error: FALSE-CANARY. The canary is prohibited while
any field is unresolved.

### PHASE 5b — Next-Steps List

**Ordering rule** (output verbatim): Tier-critical REAL-REQUIRED first (trace,
scout-feasibility, listen) → evaluation-driven REAL-REQUIRED ordered by blocker
severity (ARCH-FAIL → PM-FAIL → STRAT-FAIL) → EVIDENCE-HEAVY auto-classified
last.

Entry format (artifact-state propagated end-to-end from Phase 3 SQ answer →
Phase 4 artifact-state field → here):
```
/{skill-id} {topic} — {artifact-state}
```

**Cross-namespace risk statement** (required): One sentence naming the dominant
unresolved theme across all REAL-REQUIRED decisions — the pattern that, if
unresolved, blocks the most downstream decisions.

**Urgency grouping**:
- IMMEDIATE: blocks a decision required before any further skill execution
- BEFORE-COMMIT: required before this topic can advance to the next tier
- DEFER: informational; no blocking dependency on current work

State one-sentence criterion for each boundary.
```

---

## Variation Summary

| Variation | Axis | Key Structural Choice | Primary Coverage Target |
|-----------|------|-----------------------|------------------------|
| V-01 | Role sequence (Architect-first) | Architect runs before PM; PM gates before Strategy | C-07, C-14, C-15, C-21 |
| V-02 | Inertia framing | Named DEFAULT DECISION POSITION block; MOCK-ACCEPTED as earned escape | C-22, C-20, C-25, C-10 |
| V-03 | Lifecycle emphasis | Hard PHASE N OF 5 labels; every gate names next phase being blocked | C-02, C-12, C-16, C-17, C-18 |
| V-04 | B+C | Inversion frame + phase gates | C-22+C-17, C-20+C-12, C-16, C-25 |
| V-05 | A+B+C+D | Architect-first + inversion + gates + `field=value` trigger notation | C-01–C-25 full coverage attempt |

**Single-axis gap hypothesis**: V-01 likely covers C-13/C-14/C-15/C-21 but leaves C-22 uncovered (no inversion frame). V-02 covers C-22/C-20/C-25 but leaves C-17/C-18 at risk (no explicit gate language). V-03 covers C-12/C-16/C-17/C-18 but leaves C-23/C-25 at risk (no structured rationale template). V-04 closes the C-22+C-17 and C-20+C-12 pairs. V-05 targets all 25 but may score lower on individual execution quality if the prompt is too dense to follow cleanly.
