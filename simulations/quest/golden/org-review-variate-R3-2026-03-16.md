# org-review Variations — Round 3
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v3-2026-03-15.md

Round 1 axes explored: inertia-first sequence, strict table, null-hypothesis-universal,
formal register + lifecycle phases, parallel blind reviews.

Round 2 axes explored: multi-dimension scorecard, four-gate structure, challenger-last
rebuttal, inertia bracket + per-role null hypothesis verdict, verdict cards + disposition matrix.

Round 3 strategy: three single-axis variations targeting C-13/C-14 (gate propagation and
disposition algebra) and the pre-printed template surface (new structural axis for this skill),
then two combinations layering the strongest mechanisms for C-13 + C-14 + C-15.

---

## V-01 — Gate Sequencing: Verdict Propagation Chain

**Variation axis**: Gate sequencing — each gate produces a typed verdict that becomes a
named input to the next gate; the downstream gate's task changes based on the received
verdict, not just its background context

**Hypothesis**: R2-V02 has a four-gate structure but Gate 2 reviewers see "Gate 1's null
hypothesis statement but not Gate 1's verdict." Making the verdict — not just the statement — a
named propagating input means a Gate 1 CONDITIONAL changes what Gate 2 is asked to do:
domain reviewers must address the named gap, not just be aware of it. This is the C-13
distinction between verdict propagation and lifecycle coverage.

---

You are running `org-review` on the artifact provided below.

This review is structured as three sequential gates. Each gate produces a typed verdict
(PASS / CONDITIONAL / FAIL) that propagates as a named input to the next gate. A gate's
verdict is not a finding — it is a typed signal that changes the task of downstream gates.

**Step 0 — Role Manifest**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Fill three archetype slots from `.craft/roles/signal/`: CHALLENGER
  (inertia-advocate archetype), DOMAIN (technical/architecture archetype), LIFECYCLE
  (PM/program archetype). Assign one role per slot based on `expertise.relevance`. State each
  assignment and one-sentence rationale.
- **`--depth deep`**: Fill each slot with all matching roles. Multiple domain reviewers may
  occupy the DOMAIN slot. State total count and slot distribution.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

---

**Gate 1 — Null Hypothesis Gate** *(CHALLENGER slot)*

The challenger runs first, in isolation. This gate determines whether the null hypothesis
is named and addressed by the artifact.

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact's Response**: Does the artifact name and address the null hypothesis?
  yes / partial / no
- **Findings**: 2–3 findings from the challenger's `lens.verify`. Switching costs, workaround
  viability, adoption friction.
- **Severity**: HIGH / MEDIUM / LOW. Anchor: HIGH = artifact does not address the null
  hypothesis; LOW = null hypothesis convincingly defeated.
- **Verify Question**: One from the challenger's `lens.verify` list.

**Gate 1 Verdict**: PASS / CONDITIONAL / FAIL

**Propagation rules — read before Gate 2 begins**:
- Gate 1 **PASS**: Domain reviewers evaluate the artifact's technical merits. Null hypothesis
  is treated as addressed. No additional null hypothesis response required.
- Gate 1 **CONDITIONAL**: Domain reviewers must each identify whether their findings address
  the specific null hypothesis gap stated in Gate 1. Each domain verdict must account for that
  gap. A domain reviewer may not issue Gate 2 PASS unless their findings address the Gate 1 gap.
- Gate 1 **FAIL**: Domain reviewers evaluate the artifact but must each state whether their
  technical analysis would change the Gate 1 verdict. The Gate 1 FAIL persists in the final
  disposition unless all domain reviewers explicitly argue for upgrade to CONDITIONAL.

State Gate 1's verdict at the top of Gate 2 as: `Received Gate 1 Verdict: [value]`

---

**Gate 2 — Domain Gate** *(DOMAIN slot)*

The domain reviewer opens with the received Gate 1 verdict.

For each domain reviewer:

---
**[Role name] — DOMAIN**

*Received Gate 1 Verdict: [copy from Gate 1]*

*(If Gate 1 = CONDITIONAL or FAIL: my findings must address the null hypothesis gap named in
Gate 1. I may not issue a PASS verdict without doing so.)*

- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. At least
  one finding must engage with Gate 1's null hypothesis gap if Gate 1 is not PASS. Other
  findings address technical merit, boundary correctness, or feasibility concerns.
- **Severity**: HIGH / MEDIUM / LOW. Calibrate to this reviewer's domain. Do not copy Gate 1's
  severity level.
- **Recommendation**: One concrete action from this role's expertise frame.
- **Verify Question**: One from this role's `lens.verify` list.
- **Simplify**: One observation from this role's `lens.simplify`.
- **Gate 2 Verdict**: PASS / CONDITIONAL / FAIL for this reviewer's dimension.
  - CONDITIONAL: name the specific condition that must be met before this verdict upgrades.
  - FAIL: name the specific gap that blocks commitment.

*(If Gate 1 = FAIL and this reviewer argues for upgrade: state "Gate 2 argues Gate 1 FAIL
upgrades to CONDITIONAL if [condition]. Gate 1 FAIL stands until all domain reviewers agree.")*

---

*(For `--depth deep`: repeat for each additional domain reviewer. Each carries their own
Gate 2 Verdict.)*

**Gate 2 Aggregate Verdict** = worst verdict among all domain reviewers
(FAIL > CONDITIONAL > PASS). State it explicitly.

State Gate 2 Aggregate Verdict at the top of Gate 3 as:
`Received Gate 2 Aggregate Verdict: [value]`

---

**Gate 3 — Commitment Readiness Gate** *(LIFECYCLE slot)*

*Received Gate 1 Verdict: [value]*
*Received Gate 2 Aggregate Verdict: [value]*

*My task: assess whether the accumulated evidence, given these specific gate verdicts,
supports a commitment decision.*

- **Decision-Readiness Assessment**: Is evidence sufficient for commitment? Reference both
  received gate verdicts explicitly. Do not re-evaluate the null hypothesis independently —
  Gate 1 already determined that.
- **Null Hypothesis Status**: Given the Gate 1 verdict and Gate 2 findings, has the null
  hypothesis been addressed to commitment-readiness? yes / partial / no.
- **Findings**: 2–3 findings from this role's `lens.verify` and `expertise.depth`. Address
  commitment readiness, program concerns, or decision sufficiency.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify` list.
- **Simplify**: One from this role's `lens.simplify`.
- **Gate 3 Verdict**: PASS / CONDITIONAL / FAIL.

---

**Disposition**

Gate Verdict Vector: G1 = [_], G2 = [_], G3 = [_]

Compute disposition from the vector:
- **BLOCKED** if any gate verdict = FAIL.
- **CONDITIONAL** if no gate = FAIL and at least one gate = CONDITIONAL. State the conditions
  in gate order: Gate 1 condition (null hypothesis gap) before Gate 2 (domain issue) before
  Gate 3 (commitment gap).
- **READY** if all gate verdicts = PASS.

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

State the highest-severity gate verdict and its finding in one sentence. Do not editorially
reason from findings — the disposition derives from the verdict vector.

**Artifact to review:**

{{artifact}}

---

## V-02 — Output Format: Pre-printed Template Surface

**Variation axis**: Output format — the entire review skeleton is pre-printed with bracketed
fill fields `[LIKE_THIS]`; the model fills values only and does not generate section headers,
column names, or field labels

**Hypothesis**: Pre-printing the structure eliminates the class of failures where the model
follows the intent but reformats the surface — drops the null hypothesis section, merges
reviewer findings, replaces archetype headers with prose. The model cannot drop or reformat
what it did not generate. This is the strongest structural guarantee pattern identified in
scout-feasibility R3; this variation applies it to org-review for the first time. C-01/C-03/C-04
compliance becomes mechanical rather than instructional.

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]` with the appropriate value. Do not alter,
reorder, or omit any pre-printed heading, label, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A — reason]`.

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Fill each archetype slot with a role from that directory.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add rows as needed. Label each additional row with its slot. State
total count.)*

---

## CHALLENGER: NULL HYPOTHESIS

**Null hypothesis**: [What the team does today instead of building this — one sentence,
from the challenger's frame.]

**Artifact's response**: [yes / partial / no]

**Findings**:
1. [Finding 1 — from challenger's `lens.verify`. Switching costs, workaround viability, or
   adoption friction.]
2. [Finding 2 — from challenger's `lens.verify`.]
3. [Optional: Finding 3.]

**Severity**: [HIGH / MEDIUM / LOW]
*Anchor: HIGH = artifact does not address the null hypothesis; LOW = null hypothesis
convincingly defeated.*

**Verify Question**: [One question from the challenger's `lens.verify` list.]

**Simplify**: [One observation from challenger's `lens.simplify` — what could be removed
or collapsed.]

**Gate 1 Verdict**: [PASS / CONDITIONAL / FAIL]

**Gate 1 Reason**: [One sentence.]

---

## DOMAIN: [ROLE_NAME]

*Received Gate 1 Verdict: [PASS / CONDITIONAL / FAIL — copy from CHALLENGER section above]*

**Findings**:
1. [Finding 1 — from this role's `lens.verify` and `expertise.depth`. If Gate 1 is not PASS,
   at least this finding must address the null hypothesis gap named above.]
2. [Finding 2 — from this role's lens.]
3. [Optional: Finding 3.]
4. [Optional: Finding 4.]

**Severity**: [HIGH / MEDIUM / LOW]
*Anchor: HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory.*

**Recommendation**: [One concrete action from this role's expertise frame.]

**Verify Question**: [One question from this role's `lens.verify` list.]

**Simplify**: [One observation from this role's `lens.simplify`.]

**Gate 2 Verdict**: [PASS / CONDITIONAL / FAIL]

**Gate 2 Reason**: [One sentence. If CONDITIONAL: name the specific condition. If FAIL: name
the specific gap.]

*(For `--depth deep`: repeat this section for each additional domain reviewer, labeled
DOMAIN-2, DOMAIN-3, etc. Each carries its own Gate 2 Verdict.)*

---

## LIFECYCLE: [ROLE_NAME]

*Received Gate 1 Verdict: [PASS / CONDITIONAL / FAIL — copy from CHALLENGER section]*
*Received Gate 2 Verdict: [PASS / CONDITIONAL / FAIL — copy from DOMAIN section; if multiple
domain rows, use the worst verdict among them]*

**Decision-readiness assessment**: [Is evidence sufficient for commitment given the received
gate verdicts? One paragraph referencing both verdicts explicitly.]

**Null hypothesis status**: [Given Gate 1 and Gate 2 verdicts, has the null hypothesis been
defeated? yes / partial / no — one sentence of justification.]

**Findings**:
1. [Finding 1 — from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [Finding 2.]

**Severity**: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]

**Verify Question**: [One question from this role's `lens.verify` list.]

**Simplify**: [One observation from this role's `lens.simplify`.]

**Gate 3 Verdict**: [PASS / CONDITIONAL / FAIL]

**Gate 3 Reason**: [One sentence.]

---

## GATE VERDICT TABLE

| Gate | Reviewer | Verdict | Primary Finding |
|------|----------|---------|-----------------|
| Gate 1 — null hypothesis | [ROLE_NAME] | [PASS / CONDITIONAL / FAIL] | [One sentence] |
| Gate 2 — domain | [ROLE_NAME] | [PASS / CONDITIONAL / FAIL] | [One sentence] |
| Gate 3 — lifecycle | [ROLE_NAME] | [PASS / CONDITIONAL / FAIL] | [One sentence] |

**Gate vector**: G1=[_] G2=[_] G3=[_]

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers whose recommendations are incompatible — name the roles and the
tension. If none: write "None detected."]

**Convergence**: [Two or more reviewers naming the same concern independently — name it and
state why it is the highest-confidence signal.]

**Areas not covered**: [Artifact sections no reviewer examined. If none: write "None — full
surface covered."]

---

## DISPOSITION

*Apply the algebra below to the gate vector above. Do not reason editorially.*

- BLOCKED if any gate = FAIL
- CONDITIONAL if no gate = FAIL and at least one gate = CONDITIONAL
- READY if all gates = PASS

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary driver**: [The gate and finding most responsible for this disposition — one sentence.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from the first CONDITIONAL gate — what must be true before it upgrades to PASS.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [The specific finding from the FAIL gate — one
sentence.]

---

**Artifact to review:**

{{artifact}}

---

## V-03 — Disposition Derivation: Formula-First Algebra

**Variation axis**: Disposition derivation — the READY / CONDITIONAL / BLOCKED algebra is
stated as an explicit formula in the preamble, before any reviewer runs; the synthesis step
evaluates the formula against recorded verdicts and does not reason editorially

**Hypothesis**: C-14 requires disposition to derive from gate algebra, not editorial
assertion. Stating the formula before the review means: (1) the model knows its derivation
task before generating findings; (2) the synthesis step is formula evaluation, not a narrative
conclusion; (3) any reviewer that editorializes the disposition is visibly non-compliant.
R2-V02 and R2-V05 both state derivation rules at the synthesis step, after reviewers have run.
A formula in the preamble is harder to silently override than an inline rule at the close.

---

You are running `org-review` on the artifact provided below.

**Disposition formula** — read this before the review begins. The final disposition will be
derived by evaluating this formula against gate verdicts. Do not assert the disposition;
evaluate it.

```
Let G = {g_null, g_domain, g_lifecycle}
Each gi in {PASS, CONDITIONAL, FAIL}

Disposition:
  BLOCKED      <-- exists gi = FAIL
  CONDITIONAL  <-- (all gi != FAIL) AND (exists gi = CONDITIONAL)
  READY        <-- all gi = PASS

Tiebreaker: g_null = FAIL always yields BLOCKED, regardless of other verdicts.
A domain or lifecycle PASS does not override a challenger FAIL.
```

The review produces verdicts. The formula produces the disposition.

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select one role per archetype slot: CHALLENGER, DOMAIN, LIFECYCLE.
  Map each to a role in `.craft/roles/signal/` whose `expertise.relevance` matches this artifact
  type. State each assignment and one-sentence rationale.
- **`--depth deep`**: Fill each slot with all matching roles. State total count and slot
  distribution.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Reviewer Gates**

Run each archetype slot in this sequence: CHALLENGER → DOMAIN → LIFECYCLE.

For each reviewer:

---
**Gate [N] — [Slot name]: [Role name]**

**Findings**: 2–4 findings grounded in this role's `lens.verify` and `expertise.depth`. Do not
echo other reviewers' frames. Frame boundaries:
- CHALLENGER: workaround viability, switching costs, adoption friction
- DOMAIN: technical merit, boundary correctness, feasibility
- LIFECYCLE: commitment readiness, decision sufficiency, program concerns

**Severity**: HIGH / MEDIUM / LOW (HIGH = blocks commitment; MEDIUM = conditions; LOW =
advisory). Calibrate independently — do not copy another gate's level.

**Recommendation**: One concrete action from this role's frame.

**Verify Question**: One from this role's `lens.verify` list.

**Simplify**: One observation from this role's `lens.simplify`.

**Null Hypothesis Stance**: From this role's specific frame — does the artifact justify
building over the status quo? One sentence. These stances must differ substantively across
roles:
- CHALLENGER: is the workaround actually worse?
- DOMAIN: does the technical approach make the workaround obsolete?
- LIFECYCLE: is the decision case strong enough to commit?

**Gate [N] Verdict**: PASS / CONDITIONAL / FAIL
*Calibration: PASS = artifact satisfies this gate's concerns; CONDITIONAL = satisfies with
named condition; FAIL = named gap blocks commitment at this gate.*

---

*(Repeat for DOMAIN and LIFECYCLE in sequence.)*

**Step 3 — Formula Evaluation**

Collect all gate verdicts:

| Gate | Slot | Reviewer | Verdict |
|------|------|----------|---------|
| Gate 1 | CHALLENGER | [role] | [verdict] |
| Gate 2 | DOMAIN | [role] | [verdict] |
| Gate 3 | LIFECYCLE | [role] | [verdict] |

**Gate verdict set G** = { [list all verdicts] }

**Evaluate the preamble formula**:
- Exists any gi = FAIL? → BLOCKED. Name the gate.
- No FAIL, exists any gi = CONDITIONAL? → CONDITIONAL. List conditions.
- All PASS? → READY.

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: The gate verdict most responsible for this disposition, in one sentence.
Do not reason from findings — the formula already completed the derivation.

**Conditions** *(if CONDITIONAL)*: In priority order (CHALLENGER conditions before DOMAIN
before LIFECYCLE), state exactly what must be resolved for each CONDITIONAL gate to upgrade
to PASS.

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Adversarial Bracket + Gate Verdict Propagation

**Variation axes**: Role sequence (adversarial bracket — challenger runs first AND last,
bracketing all domain and lifecycle testimony, C-15) + Gate sequencing with verdict propagation
(each gate's verdict is a typed input to the next gate, C-13)

**Hypothesis**: R2-V04 introduced the bracket but domain reviewers only "must explicitly
address the null hypothesis" — they are not structured to receive the Gate 0 verdict as a
typed input that changes their task. Combining bracket architecture with explicit gate
propagation means: (a) the null hypothesis is the first AND last structural element; (b) each
gate changes what downstream gates do, not just what background they have. A domain PASS that
doesn't address Gate 0's gap is structurally non-compliant, not just editorially weak. The
bracket close then evaluates the full record against that original declaration.

---

You are running `org-review` on the artifact provided below.

This review uses a bracket structure with verdict propagation. The challenger runs twice:
first to declare the null hypothesis and open the gate (Bracket Opening), last to deliver a
final verdict on whether the accumulated evidence defeats it (Bracket Closing). Domain and
lifecycle reviewers run between the two bracket positions. Each gate produces a typed verdict
that propagates as a named input to subsequent gates.

**Step 0 — Role Manifest**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard**: Assign one role per slot: CHALLENGER (inertia-advocate archetype), DOMAIN
  (technical archetype), LIFECYCLE (PM/program archetype). State assignments and rationale.
- **`--depth deep`**: Multiple domain reviewers allowed. The CHALLENGER bracket positions
  remain fixed regardless of depth. State counts per slot.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

---

**Bracket Opening — CHALLENGER: Null Hypothesis Declaration**

The challenger runs first. This is a declaration pass, not a full review.

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Challenge to Domain Reviewers**: One specific question that domain reviewers must answer
  to defeat this null hypothesis. This is the anchor all subsequent reviewers must address.
- **Null Hypothesis Strength**: HIGH / MEDIUM / LOW — how strong is the case for doing nothing?
- **Findings**: 2–3 findings from the challenger's verify lens. Switching costs, workaround
  viability, adoption friction.
- **Severity**: HIGH / MEDIUM / LOW.
- **Verify Question**: One from the challenger's `lens.verify`.

**Gate 0 Verdict**: PASS / CONDITIONAL / FAIL
- PASS = artifact explicitly names and addresses the null hypothesis.
- CONDITIONAL = artifact names but incompletely addresses it.
- FAIL = null hypothesis not addressed.

**Gate 0 carries forward.** All subsequent gates open with:
`Received Gate 0 Verdict: [value] | Challenge: "[challenge text from above]"`

---

**Domain Gate — DOMAIN slot**

For each domain reviewer:

---
**[Role name] — DOMAIN**

*Received Gate 0 Verdict: [value]*
*Challenger's challenge to address: "[Copy challenge from Bracket Opening]"*

My domain analysis must answer the challenger's challenge. A PASS verdict here is only valid
if my findings address the challenger's specific question.

- **Null Hypothesis Address**: From this role's technical frame — does the artifact defeat the
  null hypothesis? One sentence. Must differ from the challenger's framing: the challenger
  assessed workaround viability; I assess whether the technical approach makes it obsolete.
- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. At least
  one finding must directly engage the challenger's question.
- **Severity**: HIGH / MEDIUM / LOW. Calibrate independently.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's verify lens.
- **Simplify**: One from this role's simplify lens.
- **Gate 1 Verdict**: PASS / CONDITIONAL / FAIL
  - CONDITIONAL: name the specific technical condition that must be met.
  - FAIL: name the specific technical gap blocking commitment.

---

*(For `--depth deep`: repeat for each additional domain reviewer.)*

**Gate 1 Aggregate Verdict** = worst verdict among all domain reviewers
(FAIL > CONDITIONAL > PASS). State explicitly.

**Gate 1 Aggregate carries forward.** Lifecycle reviewer opens with:
`Received Gate 0 Verdict: [value] | Received Gate 1 Aggregate Verdict: [value]`

---

**Lifecycle Gate — LIFECYCLE slot**

*Received Gate 0 Verdict: [value]*
*Received Gate 1 Aggregate Verdict: [value]*

My role: assess whether the accumulated evidence, given these specific verdicts, supports a
commitment decision.

- **Decision-Readiness Assessment**: Is evidence sufficient for commitment? Reference both
  received gate verdicts explicitly.
- **Null Hypothesis Status**: Given Gate 0 and Gate 1, has the null hypothesis been addressed
  to commitment-readiness? yes / partial / no.
- **Findings**: 2–3 findings from this role's verify and expertise.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's verify lens.
- **Simplify**: One from this role's simplify lens.
- **Gate 2 Verdict**: PASS / CONDITIONAL / FAIL.

**Gate 2 carries forward.** Bracket Closing receives all three gate verdicts.

---

**Bracket Closing — CHALLENGER: Final Verdict**

Full record received: artifact + all gate findings and verdicts above.

**Domain Evidence Assessment**: Did each domain reviewer's null hypothesis address actually
answer the challenger's Gate 0 question?

| Domain Reviewer | Null Hypothesis Address | Challenge Answered? |
|-----------------|------------------------|---------------------|
| [role] | [one-sentence summary of their address] | yes / partial / no |

**Remaining Gaps**: What the domain and lifecycle reviewers failed to address from the null
hypothesis declared in Bracket Opening. If nothing: "None — null hypothesis fully addressed."

**Challenger Final Verdict**: DEFEATED / PARTIAL / HOLDS
- DEFEATED: accumulated record convincingly defeats the null hypothesis.
- PARTIAL: record addresses some but leaves material gaps — name the gap.
- HOLDS: null hypothesis survives; case for doing nothing is stronger than for building.

**Rationale**: 2–3 sentences.

**GClose Verdict**: PASS (DEFEATED) / CONDITIONAL (PARTIAL) / FAIL (HOLDS)

GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict from the challenger is
not overturned by domain or lifecycle PASses.

---

**Disposition**

Gate Vector: G0=[_] G1=[_] G2=[_] GClose=[_]

Algebra:
- **BLOCKED** if GClose = FAIL (null hypothesis holds — challenger override). OR if any other
  gate = FAIL.
- **CONDITIONAL** if no gate = FAIL and at least one gate = CONDITIONAL. State conditions in
  gate order.
- **READY** if all gates = PASS.

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence naming the gate verdict most responsible.

**Cross-role conflicts**: Did any domain reviewer produce a null hypothesis address that
contradicted the Bracket Closing verdict? Name the tension — this is the most important
signal in the review if present.

**Artifact to review:**

{{artifact}}

---

## V-05 — Combination: Pre-printed Template + Stated Algebra + Adversarial Bracket

**Variation axes**: Output format (pre-printed template surface, strongest structural
guarantee) + Disposition algebra (formula pre-stated before review runs, C-14) + Role
sequence (adversarial bracket architecture, C-15)

**Hypothesis**: Each mechanism handles one class of failure. Pre-printed template prevents
structural surface loss (model cannot drop sections it did not generate). Stated algebra
prevents editorial disposition (model evaluates a formula, does not narrate one). Adversarial
bracket prevents null hypothesis displacement (challenger is structurally first AND last,
not just instructionally required to be). Pre-printing the bracket positions as fixed section
headers means the model cannot reorder them. Pre-printing the formula in the DISPOSITION
section means the model evaluates it against pre-printed field values, producing the strongest
C-13/C-14/C-15 structural guarantee achievable in a single variation.

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, structural element, or formula line. Do not add sections between
pre-printed headers. If a field cannot be filled, write `[N/A — reason]`.

**Disposition formula** *(pre-stated; evaluated at DISPOSITION section — do not alter this
block)*:

```
G = {GOpen, G_domain, G_lifecycle, GClose}
BLOCKED      <-- GClose = FAIL  [challenger final: null hypothesis holds — overrides all]
              OR any other Gi = FAIL
CONDITIONAL  <-- no Gi = FAIL AND any Gi = CONDITIONAL
READY        <-- all Gi = PASS
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot to a role from that directory.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add rows. CHALLENGER bracket positions remain fixed; additional domain
or lifecycle reviewers slot between them. State total count.)*

---

## BRACKET OPENING — CHALLENGER

**Null hypothesis**: [What the team does today instead of building this — one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW — how strong is the case for doing nothing?]

**Challenge to downstream reviewers**: [One specific question that domain and lifecycle
reviewers must address to defeat this null hypothesis. This is the anchor all subsequent
reviews respond to.]

**Findings**:
1. [Finding 1 — challenger's lens: switching costs, workaround viability, adoption friction.]
2. [Finding 2.]
3. [Optional: Finding 3.]

**Severity**: [HIGH / MEDIUM / LOW]
*Anchor: HIGH = artifact does not address null hypothesis; LOW = null hypothesis convincingly
defeated.*

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and the challenge text above carry forward to all downstream sections.*

---

## DOMAIN — [ROLE_NAME]

*Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]*
*Challenge to address: "[Copy challenge text from BRACKET OPENING]"*

**Null hypothesis address**: [From this role's technical frame, does the artifact defeat the
null hypothesis? One sentence. Must differ from challenger's framing: challenger assessed
workaround viability; this role assesses whether the technical approach makes it obsolete.]

**Findings**:
1. [Finding 1 — from this role's `lens.verify` and `expertise.depth`. At least this finding
   must engage the challenge from BRACKET OPENING.]
2. [Finding 2.]
3. [Optional: Finding 3.]
4. [Optional: Finding 4.]

**Severity**: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name the condition. If FAIL: name the gap.]

*(For `--depth deep`: repeat this section labeled DOMAIN-2, DOMAIN-3, etc. G_domain aggregate
= worst verdict among all domain rows. State aggregate explicitly.)*

---

## LIFECYCLE — [ROLE_NAME]

*Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]*
*Received G_domain: [PASS / CONDITIONAL / FAIL — copy from DOMAIN; use aggregate if multiple]*

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both received
verdicts? One paragraph referencing both explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no — one sentence.]

**Findings**:
1. [Finding 1 — from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [Finding 2.]

**Severity**: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

---

## BRACKET CLOSING — CHALLENGER

*Full record received: artifact + all gate findings and verdicts above.*

**Domain evidence assessment**:

| Reviewer | Null Hypothesis Address | Challenge Answered? |
|----------|------------------------|---------------------|
| [DOMAIN ROLE_NAME] | [One sentence summary of their null hypothesis address] | yes / partial / no |

**Remaining gaps**: [What domain and lifecycle reviewers failed to address from the null
hypothesis and challenge declared in BRACKET OPENING. If nothing: "None — null hypothesis
fully addressed."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): accumulated record convincingly defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): record addresses some but leaves material gaps — name the gap.
- FAIL (= HOLDS): null hypothesis survives; case for doing nothing is stronger than for
  building.

**GClose Rationale**: [2–3 sentences explaining the verdict.]

---

## DISPOSITION

**Gate vector** *(fill from sections above)*:
- GOpen = [copy from BRACKET OPENING]
- G_domain = [copy from DOMAIN; aggregate if multiple]
- G_lifecycle = [copy from LIFECYCLE]
- GClose = [copy from BRACKET CLOSING]

**Apply pre-stated formula** *(do not alter the formula; do not reason editorially — evaluate
the gate vector against the formula)*:

```
G = {GOpen=[_], G_domain=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (null hypothesis holds; override)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED — result of evaluating the formula
above]

**Primary driver**: [The gate verdict most responsible for this disposition — one sentence.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from the first CONDITIONAL gate — what must be resolved for it to upgrade
   to PASS.]
2. [Additional conditions if present, in gate order: GOpen before G_domain before G_lifecycle
   before GClose.]

**Blocker** *(complete only if BLOCKED)*: [The specific finding from the FAIL gate that
blocks commitment — one sentence. If GClose = FAIL, lead with: "Challenger final verdict HOLDS
— [reason from GClose Rationale]."]

---

**Artifact to review:**

{{artifact}}
