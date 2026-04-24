Good — rubric v4 is at `org-review-rubric-v4-2026-03-15.md`. I have everything I need. Writing R4 now.

---

# org-review Variations — Round 4
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v4-2026-03-15.md

Round 1 axes explored: inertia-first sequence, strict table, null-hypothesis-universal,
formal register + lifecycle phases, parallel blind reviews.

Round 2 axes explored: multi-dimension scorecard, four-gate structure, challenger-last
rebuttal, inertia bracket + per-role null hypothesis verdict, verdict cards + disposition matrix.

Round 3 axes explored: gate sequencing with verdict propagation (C-13), pre-printed template
surface (structural surface guarantee), formula-first algebra (C-14), adversarial bracket +
propagation combination, pre-printed template + algebra + adversarial bracket triple
combination.

Round 4 strategy: three single-axis variations isolating C-16 (pre-run algebra commitment
as immutable named contract), C-17 (challenge text assigned a unique ID; downstream sections
carry a mandatory CH-ID RESPONSE field), and C-18 (bracket closing override authority
constitutionally declared before any reviewer runs). Then two combinations: C-16 + C-17,
and C-16 + C-17 + C-18 with pre-printed template surface.

---

## V-01 — Pre-Run Algebra Commitment: Named Disposition Contract

**Variation axis**: C-16 isolation — the disposition algebra is declared as a named,
immutable `DISPOSITION_CONTRACT` block before the role manifest. Every reviewer section
references the contract by name when issuing a verdict. The synthesis step evaluates the
contract; it does not restate or re-derive it.

**Hypothesis**: R3 V-03 states the formula in the preamble, but as inline instruction
text that the model generates as part of running the prompt — which still permits silent
override at the synthesis step by re-narrating the algebra. Making the formula a named
contract (a specific block with a name the model must cite) makes deviation structurally
visible: a synthesis step that editorializes is ignoring a named contract, not just
drifting from inline guidance. The temporal constraint of C-16 — algebra committed before
execution — is enforced by naming the contract before the role manifest appears.

---

You are running `org-review` on the artifact provided below.

**DISPOSITION_CONTRACT** *(declared before the review begins; this block is the evaluation
contract for the final disposition; do not alter, paraphrase, or re-derive it at the
synthesis step — evaluate it)*:

```
Name: DISPOSITION_CONTRACT
Version: org-review/v4

Let G = { g_null, g_domain, g_lifecycle }
Each gi ∈ { PASS, CONDITIONAL, FAIL }

BLOCKED      ← ∃ gi = FAIL
CONDITIONAL  ← (∀ gi ≠ FAIL) ∧ (∃ gi = CONDITIONAL)
READY        ← ∀ gi = PASS

Tiebreaker: g_null = FAIL → BLOCKED regardless of other verdicts.
No domain or lifecycle verdict overrides a challenger FAIL.
```

All reviewers must issue verdicts from `{ PASS, CONDITIONAL, FAIL }`. No other values are
valid inputs to the DISPOSITION_CONTRACT evaluation.

---

**Step 1 — Role Manifest**

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per archetype slot: CHALLENGER (inertia-advocate
  archetype), DOMAIN (technical/architecture archetype), LIFECYCLE (PM/program archetype).
  Map each role to the slot based on `expertise.relevance` for this artifact type. State
  each assignment and one-sentence rationale.
- **`--depth deep`**: Assign all matching roles per slot. State total count and slot
  distribution. For multiple domain reviewers, g_domain = worst verdict among the slot.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**Step 2 — Reviewer Gates**

Run each slot in sequence: CHALLENGER → DOMAIN → LIFECYCLE. For each reviewer, produce
findings in their specific frame, issue a verdict, and cite the DISPOSITION_CONTRACT by
name.

---

**CHALLENGER — [Role name]**

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact Response**: Does the artifact name and address the null hypothesis?
  `yes / partial / no`
- **Findings**: 2–3 findings from this role's `lens.verify`. Switching costs, workaround
  viability, adoption friction. Each finding is a distinct claim, not a summary.
- **Severity**: HIGH / MEDIUM / LOW.
  *Anchor: HIGH = artifact does not address the null hypothesis; LOW = convincingly
  defeated.*
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify` list.
- **Simplify**: One observation from this role's `lens.simplify`.

**g_null Verdict**: PASS / CONDITIONAL / FAIL
**g_null Reason**: One sentence.
**Contract Cite**: `DISPOSITION_CONTRACT applies: g_null = [value] → if FAIL, BLOCKED
regardless of downstream verdicts.`

---

**DOMAIN — [Role name]**

- **Null Hypothesis Address**: Does the artifact defeat the null hypothesis from this
  role's technical frame? One sentence. Frame boundary: domain assesses whether the
  technical approach makes the workaround obsolete, not whether the workaround is
  inconvenient.
- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. Frame
  boundary: technical merit, boundary correctness, feasibility. Do not re-argue the null
  hypothesis challenge — address it through technical analysis.
- **Severity**: HIGH / MEDIUM / LOW.
  *Anchor: HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory.*
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify` list.
- **Simplify**: One observation from this role's `lens.simplify`.

**g_domain Verdict**: PASS / CONDITIONAL / FAIL
**g_domain Reason**: One sentence. If CONDITIONAL: name the specific technical condition.
If FAIL: name the specific gap.
**Contract Cite**: `DISPOSITION_CONTRACT applies: g_domain = [value] → contributes to
BLOCKED / CONDITIONAL / READY evaluation.`

*(For `--depth deep`: repeat this section for each additional domain reviewer, labeled
DOMAIN-2, DOMAIN-3, etc. g_domain aggregate = worst verdict among all domain rows.
State aggregate explicitly after the last domain section.)*

---

**LIFECYCLE — [Role name]**

- **Decision-Readiness Assessment**: Is the accumulated evidence sufficient for commitment?
  One paragraph. Reference g_null and g_domain explicitly — do not re-evaluate the artifact
  independently; assess whether the gate record supports a commitment decision.
- **Null Hypothesis Status**: Given g_null and g_domain, has the null hypothesis been
  addressed to commitment-readiness? `yes / partial / no` — one sentence.
- **Findings**: 2–3 findings from this role's `lens.verify` and `expertise.depth`.
  Frame boundary: commitment readiness, program concerns, decision sufficiency.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify` list.
- **Simplify**: One observation from this role's `lens.simplify`.

**g_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
**g_lifecycle Reason**: One sentence.
**Contract Cite**: `DISPOSITION_CONTRACT applies: g_lifecycle = [value] → contributes to
BLOCKED / CONDITIONAL / READY evaluation.`

---

**Step 3 — Contract Evaluation**

Collect verdicts issued above:

| Slot | Reviewer | Verdict Issued |
|------|----------|----------------|
| CHALLENGER | [role] | g_null = [value] |
| DOMAIN | [role] | g_domain = [value] |
| LIFECYCLE | [role] | g_lifecycle = [value] |

**Evaluate DISPOSITION_CONTRACT** *(do not re-derive; apply the named contract to the
verdict set)*:

```
G = { g_null=[_], g_domain=[_], g_lifecycle=[_] }
∃ g_null = FAIL? → BLOCKED (tiebreaker: challenger veto)
∃ g_domain = FAIL? → BLOCKED
∃ g_lifecycle = FAIL? → BLOCKED
No FAIL, ∃ CONDITIONAL? → CONDITIONAL
All PASS? → READY
```

**Overall Disposition**: READY / CONDITIONAL / BLOCKED
*(Result of applying DISPOSITION_CONTRACT — not an editorial assertion.)*

**Primary driver**: The gate and verdict most responsible for this disposition — one
sentence citing the specific reviewer and verdict value.

**Conditions** *(if CONDITIONAL, in contract order: g_null before g_domain before
g_lifecycle)*:
1. [Condition from first CONDITIONAL gate — what must be resolved for it to upgrade to PASS.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: [The FAIL gate, reviewer, and specific finding — one sentence.]

---

**Artifact to review:**

{{artifact}}

---

## V-02 — Challenge Text Carry-Forward: Unique Challenge IDs

**Variation axis**: C-17 isolation — the challenger issues numbered challenge IDs
(CH-01, CH-02...) alongside findings. Every downstream reviewer section carries a
mandatory `CH-XX RESPONSE` field per challenge ID received. The closing section produces
a traceability table mapping each CH-ID to every reviewer's response and verdict impact.
Domain may not issue PASS without a non-`UNANSWERED` entry for every CH-ID.

**Hypothesis**: R3 V-04 carries challenge *text* forward in the gate header but does not
require a formal response field — a domain reviewer who mentions the challenge topic in
their findings still passes. Assigning a unique ID to each challenge and requiring a
mandatory per-ID response field in every downstream section makes non-response structurally
absent (a missing field) rather than editorially weak. The traceability table at close
exposes every partial or unanswered challenge across all reviewers, making C-17 compliance
fully visible without editorial interpretation.

---

You are running `org-review` on the artifact provided below.

**Challenge ID protocol**: The challenger section issues numbered challenge IDs in the
form `CH-01`, `CH-02`, etc. Every subsequent reviewer section carries a `CH-XX RESPONSE`
subsection — one entry per challenge ID issued. A domain or lifecycle reviewer may not
issue a PASS verdict while any challenge ID is marked `UNANSWERED`. An `ANSWERED` entry
requires an explicit evidence sentence; `PARTIAL` requires a named remaining gap.

---

**Step 1 — Role Manifest**

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per slot — CHALLENGER, DOMAIN, LIFECYCLE.
  Map from `expertise.relevance` for this artifact type. State each assignment and
  one-sentence rationale.
- **`--depth deep`**: Assign all matching roles per slot. State total count and slot
  distribution.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**CHALLENGER — [Role name]**

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact Response**: Does the artifact address the null hypothesis? `yes / partial / no`
- **Findings**: 2–3 findings. For each finding that represents a specific challenge the
  artifact must answer, issue a challenge ID.

> **CH-01**: [Challenge text — one sentence; a specific claim the artifact must defeat.
> Starts with "The artifact must show..." or "The record must demonstrate..."]
>
> **CH-02**: [Optional second challenge — only if genuinely distinct from CH-01.]

- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**Gate 1 Verdict**: PASS / CONDITIONAL / FAIL
**Gate 1 Reason**: One sentence.

*All challenge IDs issued above (CH-01 [, CH-02...]) carry forward to all downstream
reviewer sections.*

---

**DOMAIN — [Role name]**

*Challenges received: CH-01 [, CH-02...] — copy from CHALLENGER section*

- **Null Hypothesis Address**: Does the artifact defeat the null hypothesis from this
  role's technical frame? One sentence. Technical frame boundary: does the approach make
  the workaround obsolete?
- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**CH-XX RESPONSE** *(mandatory — one entry per challenge ID received)*:

> **CH-01**: [ANSWERED / PARTIAL / UNANSWERED]
> Evidence: [One sentence referencing this role's specific finding that addresses the
> challenge. If PARTIAL: name the remaining gap. If UNANSWERED: state why and acknowledge
> this blocks PASS.]*
>
> *(Repeat for CH-02 if present.)*

**Gate 2 Verdict**: PASS / CONDITIONAL / FAIL
*Domain may not issue PASS if any CH-XX entry is UNANSWERED.*
**Gate 2 Reason**: One sentence. If CONDITIONAL: name the condition. If FAIL: name the gap.

*(For `--depth deep`: repeat this section for each additional domain reviewer, labeled
DOMAIN-2, DOMAIN-3, etc. Each carries its own CH-XX RESPONSE block. Gate 2 aggregate =
worst verdict.)*

---

**LIFECYCLE — [Role name]**

*Challenges received: CH-01 [, CH-02...] — copy from CHALLENGER section*
*Gate 2 aggregate: [copy from DOMAIN section]*

- **Decision-Readiness Assessment**: Is accumulated evidence sufficient for commitment?
  Reference Gate 1 and Gate 2 explicitly.
- **Null Hypothesis Status**: `yes / partial / no` — one sentence.
- **Findings**: 2–3 findings from this role's `lens.verify` and `expertise.depth`.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**CH-XX RESPONSE** *(mandatory — one entry per challenge ID received)*:

> **CH-01**: [ANSWERED / PARTIAL / UNANSWERED]
> Evidence: [One sentence from this role's commitment/program frame. If UNANSWERED:
> acknowledge this blocks PASS.]*
>
> *(Repeat for CH-02 if present.)*

**Gate 3 Verdict**: PASS / CONDITIONAL / FAIL
*Lifecycle may not issue PASS if any CH-XX entry is UNANSWERED.*
**Gate 3 Reason**: One sentence.

---

**Step 3 — Challenge Traceability Table**

| Challenge | Challenger Statement | Domain Response | Lifecycle Response | Verdict Impact |
|-----------|---------------------|-----------------|-------------------|----------------|
| CH-01 | [Copy challenge text] | [ANSWERED/PARTIAL/UNANSWERED] | [ANSWERED/PARTIAL/UNANSWERED] | [Blocks PASS at: none / DOMAIN / LIFECYCLE / both] |
| CH-02 | [Copy if present] | … | … | … |

**Unanswered challenges**: [List any CH-ID with at least one UNANSWERED entry, or write
"None — all challenges answered or partially addressed."]

---

**Disposition**

Gate verdict vector: G1 = [challenger], G2 = [domain aggregate], G3 = [lifecycle]

Algebra:
- **BLOCKED** if any gate = FAIL
- **CONDITIONAL** if no FAIL and at least one CONDITIONAL. State conditions in gate order.
- **READY** if all PASS.

*Additional rule*: If any challenge ID remains UNANSWERED in the traceability table, the
corresponding gate cannot be PASS. If it was issued as PASS above, downgrade to CONDITIONAL
and name the unanswered challenge as the condition.

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence naming the gate and specific finding most responsible.

**Conditions** *(if CONDITIONAL)*:
1. [First condition — reference CH-ID if applicable.]
2. [Additional conditions if present.]

**Artifact to review:**

{{artifact}}

---

## V-03 — Constitutional Override Authority: Pre-Declared Bracket Hierarchy

**Variation axis**: C-18 isolation — a `REVIEW_AUTHORITY_HIERARCHY` block is declared
before the role manifest, establishing GClose as the supreme verdict authority. All
reviewer sections carry an authority acknowledgment. The lifecycle reviewer explicitly
acknowledges they cannot override GClose. The bracket closing section opens with a
constitutional authority citation and its override statement is derived from the preamble
declaration, not asserted inline.

**Hypothesis**: R3 V-04 and V-05 state override authority in the bracket closing section —
after domain and lifecycle reviewers have already run. This means a lifecycle reviewer who
issues a strong PASS can editorially undermine GClose before the override is declared.
Declaring override authority in the preamble, before any reviewer runs, makes every
reviewer issue their verdict in full knowledge of the hierarchy. A lifecycle PASS issued
after reading "GClose = FAIL overrides all verdicts" is structurally acknowledged, not
invisible. C-18's requirement is not just that override semantics exist — it is that they
are explicit and prior, so no reviewer can credibly argue their verdict supersedes GClose.

---

You are running `org-review` on the artifact provided below.

**REVIEW_AUTHORITY_HIERARCHY** *(declared before the review begins; applies to all
reviewer sections and the final disposition; do not alter or override this block)*:

```
Name: REVIEW_AUTHORITY_HIERARCHY
Version: org-review/v4

Authority order (highest to lowest):
  1. GClose  — challenger bracket closing verdict (supreme)
  2. G_null  — challenger bracket opening verdict
  3. G_domain — domain reviewer verdict(s)
  4. G_lifecycle — lifecycle reviewer verdict

Override rule:
  GClose = FAIL → BLOCKED, regardless of any other gate verdict.
  A HOLDS verdict (GClose = FAIL) is not overturned by PASS verdicts at G_domain
  or G_lifecycle. The challenger's final verdict is the last word on whether the
  null hypothesis is defeated.

Acknowledgment requirement:
  Each reviewer section must carry: "Authority acknowledged: [role] verdicts at
  authority level [N]."
```

All reviewers must carry the acknowledgment before issuing their verdict.

---

**Step 1 — Role Manifest**

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per slot — CHALLENGER (bracket open + close),
  DOMAIN, LIFECYCLE. Map from `expertise.relevance`. State each assignment and one-sentence
  rationale.
- **`--depth deep`**: Assign all matching roles per slot. The CHALLENGER bracket positions
  remain fixed: one challenger role runs both Bracket Opening and Bracket Closing. State
  total count and slot distribution.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**Bracket Opening — CHALLENGER: Null Hypothesis Declaration**

Authority acknowledged: [role] verdicts at authority level 2 (G_null).

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Challenge**: One specific question that domain and lifecycle reviewers must answer to
  defeat this null hypothesis.
- **Findings**: 2–3 findings from this role's `lens.verify`. Switching costs, workaround
  viability, adoption friction.
- **Severity**: HIGH / MEDIUM / LOW.
  *Anchor: HIGH = artifact does not address the null hypothesis; LOW = convincingly
  defeated.*
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**G_null Verdict**: PASS / CONDITIONAL / FAIL
**G_null Reason**: One sentence.

*The challenge stated above and G_null carry forward to all downstream sections.*

---

**Domain Gate — DOMAIN — [Role name]**

Authority acknowledged: [role] verdicts at authority level 3 (G_domain). This reviewer
may not override G_null. A domain PASS does not overturn a G_null FAIL. If GClose issues
a FAIL verdict, this reviewer's PASS does not change the disposition.

- **Null Hypothesis Address**: Does the artifact defeat the null hypothesis from this
  technical frame? One sentence.
- **Challenge Response**: Does this role's analysis answer the challenger's challenge from
  Bracket Opening? One sentence.
- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**G_domain Verdict**: PASS / CONDITIONAL / FAIL
**G_domain Reason**: One sentence. If CONDITIONAL: name the condition. If FAIL: name gap.

*(For `--depth deep`: repeat for each domain reviewer, labeled DOMAIN-2, DOMAIN-3, etc.
G_domain aggregate = worst verdict. Authority acknowledgment appears in each section.)*

---

**Lifecycle Gate — LIFECYCLE — [Role name]**

Authority acknowledged: [role] verdicts at authority level 4 (G_lifecycle). This reviewer
may not override G_null or G_domain. If GClose issues a FAIL verdict, this reviewer's PASS
does not change the disposition. This reviewer assesses commitment readiness given the
existing gate record; they do not re-evaluate the null hypothesis.

- **Decision-Readiness Assessment**: Is accumulated evidence sufficient for commitment?
  Reference G_null and G_domain explicitly.
- **Null Hypothesis Status**: Given G_null and G_domain, has the null hypothesis been
  addressed to commitment-readiness? `yes / partial / no` — one sentence.
- **Findings**: 2–3 findings from this role's `lens.verify` and `expertise.depth`.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**G_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
**G_lifecycle Reason**: One sentence.

---

**Bracket Closing — CHALLENGER: Final Verdict**

Authority acknowledged: [role] verdicts at authority level 1 (GClose — supreme). By the
REVIEW_AUTHORITY_HIERARCHY, GClose = FAIL constitutes BLOCKED regardless of G_domain or
G_lifecycle verdicts.

Full record received: artifact + all gate findings and verdicts above.

**Domain Evidence Review**:

| Domain Reviewer | Challenge Response | Challenge Answered? |
|-----------------|-------------------|---------------------|
| [role] | [one-sentence summary of their challenge response] | yes / partial / no |

**Lifecycle Evidence Review**: Did the lifecycle reviewer's decision-readiness assessment
engage with the null hypothesis challenge? `yes / partial / no` — one sentence.

**Remaining Gaps**: What the domain and lifecycle reviewers failed to address from the
challenge declared in Bracket Opening. If nothing: "None — challenge fully answered."

**GClose Verdict**: PASS / CONDITIONAL / FAIL
- PASS (DEFEATED): accumulated record convincingly defeats the null hypothesis.
- CONDITIONAL (PARTIAL): record addresses some but leaves a named material gap.
- FAIL (HOLDS): null hypothesis survives; case for doing nothing is stronger than for
  building.

**GClose Rationale**: 2–3 sentences.

**Authority invocation**: Per REVIEW_AUTHORITY_HIERARCHY, GClose = [value]. If FAIL:
"GClose = FAIL overrides G_domain = [value] and G_lifecycle = [value]. BLOCKED."

---

**Disposition**

Gate vector: G_null = [_], G_domain = [_], G_lifecycle = [_], GClose = [_]

Apply REVIEW_AUTHORITY_HIERARCHY:
- GClose = FAIL → **BLOCKED** (supreme authority; override declared in preamble hierarchy)
- Any other gate = FAIL → **BLOCKED**
- No FAIL, any CONDITIONAL → **CONDITIONAL**
- All PASS → **READY**

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence naming the gate authority level and verdict responsible.

**Conditions** *(if CONDITIONAL, in authority order: G_null before G_domain before
G_lifecycle before GClose)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: One sentence. If GClose = FAIL, lead with:
"REVIEW_AUTHORITY_HIERARCHY: GClose = FAIL (supreme) overrides G_domain = [value] and
G_lifecycle = [value] — [reason from GClose Rationale]."

---

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Algebra Lock + Challenge ID Traceability

**Variation axes**: C-16 (DISPOSITION_CONTRACT pre-stated as named constant before role
manifest) + C-17 (challenges issued as numbered IDs; downstream sections carry mandatory
CH-XX RESPONSE fields; traceability table at close)

**Hypothesis**: V-01 and V-02 each provide one pre-run commitment: V-01 commits to the
derivation contract (how the disposition is computed), V-02 commits to the evidence
contract (what specific claims must be answered). Together they close two independent
post-hoc escape routes: the model cannot rewrite the formula it did not generate, and it
cannot PASS a reviewer without answering a challenge it cannot un-issue. The combination
is additive — each blocks a distinct class of deviation — and they share a structural
surface: both appear in the preamble, before the role manifest, as named locked blocks.
A synthesis step that editorializes must violate both named contracts simultaneously,
making deviation maximally visible.

---

You are running `org-review` on the artifact provided below.

**DISPOSITION_CONTRACT** *(pre-stated before review begins; evaluated at synthesis step;
do not alter, paraphrase, or re-derive)*:

```
Name: DISPOSITION_CONTRACT
Version: org-review/v4

Let G = { g_null, g_domain, g_lifecycle }
Each gi ∈ { PASS, CONDITIONAL, FAIL }

BLOCKED      ← ∃ gi = FAIL
CONDITIONAL  ← (∀ gi ≠ FAIL) ∧ (∃ gi = CONDITIONAL)
READY        ← ∀ gi = PASS

Tiebreaker: g_null = FAIL → BLOCKED regardless of other verdicts.
```

**CHALLENGE_ID PROTOCOL** *(declared before review begins)*:

- The challenger section issues numbered challenge IDs in the form CH-01, CH-02, etc.
- Every downstream reviewer section (DOMAIN, LIFECYCLE) carries a `CH-XX RESPONSE`
  subsection — one mandatory entry per CH-ID issued.
- Response values: `ANSWERED` (evidence sentence required) / `PARTIAL` (remaining gap
  required) / `UNANSWERED` (reason required; blocks PASS).
- A reviewer may not issue PASS while any CH-XX entry is UNANSWERED.
- The synthesis step produces a challenge traceability table before applying the
  DISPOSITION_CONTRACT.

---

**Step 1 — Role Manifest**

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per slot — CHALLENGER, DOMAIN, LIFECYCLE.
  Map from `expertise.relevance`. State each assignment and one-sentence rationale.
- **`--depth deep`**: Assign all matching roles per slot. State total count. For multiple
  domain reviewers, g_domain = worst verdict among the slot.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**CHALLENGER — [Role name]**

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact Response**: `yes / partial / no`
- **Findings and Challenges**: 2–3 findings from this role's `lens.verify`. For each
  finding that is a specific claim the artifact must defeat, issue a CH-ID:

> **CH-01**: [Challenge text — "The artifact must show..." or "The record must demonstrate..."
> — one sentence. This challenge propagates to all downstream reviewer sections.]
>
> **CH-02**: [Optional second challenge — only if genuinely distinct from CH-01.]

- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**g_null Verdict**: PASS / CONDITIONAL / FAIL
**g_null Reason**: One sentence.
**Contract Cite**: `DISPOSITION_CONTRACT: g_null = [value]`

*All CH-IDs issued above carry forward to all downstream sections. Challenges cannot be
withdrawn or modified after this section.*

---

**DOMAIN — [Role name]**

*Challenges received: CH-01 [, CH-02...] — copy from CHALLENGER*

- **Null Hypothesis Address**: One sentence from this role's technical frame.
- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**CH-XX RESPONSE** *(mandatory — one entry per CH-ID)*:

> **CH-01**: [ANSWERED / PARTIAL / UNANSWERED]
> Evidence: [One sentence from this role's findings. If PARTIAL: name the gap. If
> UNANSWERED: state why; this reviewer cannot issue PASS.]
>
> *(Repeat for CH-02 if issued.)*

**g_domain Verdict**: PASS / CONDITIONAL / FAIL
*PASS blocked if any CH-XX = UNANSWERED.*
**g_domain Reason**: One sentence.
**Contract Cite**: `DISPOSITION_CONTRACT: g_domain = [value]`

*(For `--depth deep`: repeat for each domain reviewer. Each carries its own CH-XX RESPONSE
block. State g_domain aggregate — worst verdict — after the last domain section.)*

---

**LIFECYCLE — [Role name]**

*Challenges received: CH-01 [, CH-02...] — copy from CHALLENGER*
*g_domain aggregate: [copy from DOMAIN section]*

- **Decision-Readiness Assessment**: Is accumulated evidence sufficient? Reference g_null
  and g_domain explicitly.
- **Null Hypothesis Status**: `yes / partial / no`
- **Findings**: 2–3 findings from this role's `lens.verify` and `expertise.depth`.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.

**CH-XX RESPONSE** *(mandatory — one entry per CH-ID)*:

> **CH-01**: [ANSWERED / PARTIAL / UNANSWERED]
> Evidence: [One sentence from this role's commitment frame. If UNANSWERED: this reviewer
> cannot issue PASS.]
>
> *(Repeat for CH-02 if issued.)*

**g_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
*PASS blocked if any CH-XX = UNANSWERED.*
**g_lifecycle Reason**: One sentence.
**Contract Cite**: `DISPOSITION_CONTRACT: g_lifecycle = [value]`

---

**Step 3 — Synthesis**

**Challenge Traceability Table**:

| ID | Challenge | Domain | Lifecycle | Net Status |
|----|-----------|--------|-----------|------------|
| CH-01 | [Copy challenge text] | [ANSWERED/PARTIAL/UNANSWERED] | [A/P/U] | [CLOSED / PARTIAL / OPEN] |
| CH-02 | [Copy if present] | … | … | … |

**Unanswered challenges**: [CH-IDs with at least one UNANSWERED, or "None."]

**Contract Evaluation** *(apply DISPOSITION_CONTRACT to the verdict set — do not
re-derive)*:

| Slot | Reviewer | Verdict |
|------|----------|---------|
| g_null | [role] | [value] |
| g_domain | [role] | [value] |
| g_lifecycle | [role] | [value] |

```
G = { g_null=[_], g_domain=[_], g_lifecycle=[_] }
∃ g_null = FAIL? → BLOCKED (tiebreaker)
∃ other gi = FAIL? → BLOCKED
No FAIL, ∃ CONDITIONAL? → CONDITIONAL
All PASS? → READY
```

**Overall Disposition**: READY / CONDITIONAL / BLOCKED
*(DISPOSITION_CONTRACT evaluation result — not an editorial assertion.)*

**Primary driver**: One sentence, citing gate name and reviewer.

**Conditions** *(if CONDITIONAL; in contract order)*:
1. [Condition from first CONDITIONAL gate, CH-ID reference if applicable.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: Gate, reviewer, finding — one sentence.

---

**Artifact to review:**

{{artifact}}

---

## V-05 — Combination: Algebra Lock + Challenge ID Traceability + Constitutional Override + Pre-printed Template

**Variation axes**: C-16 (DISPOSITION_CONTRACT, pre-stated locked block) + C-17
(CH-ID protocol, mandatory response fields, traceability table) + C-18 (REVIEW_AUTHORITY_
HIERARCHY, constitutionally declared before any reviewer, bracket closing as supreme
authority) + Output format (pre-printed template surface — structural surface guarantee
from R3 V-02; model fills `[BRACKETED_FIELDS]` only)

**Hypothesis**: Each mechanism in V-01/V-02/V-03 blocks one deviation class. Pre-printed
template surface (R3 V-02) adds a fourth: structural surface loss (model cannot drop a
section it did not generate). Combining all four in a single variation yields the maximum
structural guarantee achievable: (a) formula is a named locked constant — formula
deviation is structurally visible; (b) every challenge has an ID — non-response is a
missing field; (c) GClose authority is preamble-declared — override violation is
constitutional non-compliance; (d) every section is pre-printed — section loss is
physically impossible. This is the strongest C-13/C-14/C-15/C-16/C-17/C-18 candidate
achievable in a single prompt and the first variation to address all three R4 rubric
additions simultaneously.

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, omit, or add
to any pre-printed heading, label, structural element, formula block, or protocol block.
If a field cannot be filled, write `[N/A — reason]`.

---

**DISPOSITION_CONTRACT** *(pre-stated; evaluated at DISPOSITION section; do not alter)*:

```
Name: DISPOSITION_CONTRACT
Version: org-review/v4

Let G = { GOpen, G_domain, G_lifecycle, GClose }
Each Gi ∈ { PASS, CONDITIONAL, FAIL }

BLOCKED      ← GClose = FAIL  [challenger final: supreme override]
              OR ∃ other Gi = FAIL
CONDITIONAL  ← (∀ Gi ≠ FAIL) ∧ (∃ Gi = CONDITIONAL)
READY        ← ∀ Gi = PASS
```

**CHALLENGE_ID PROTOCOL** *(pre-stated; applies to all downstream sections)*:

```
Challenger issues: CH-01, CH-02, ...
Each downstream section carries a CH-XX RESPONSE block.
Response values: ANSWERED (evidence required) / PARTIAL (gap required) / UNANSWERED
  (reason required; blocks PASS in that section).
Traceability table produced at SYNTHESIS before DISPOSITION.
```

**REVIEW_AUTHORITY_HIERARCHY** *(pre-stated; applies to all sections)*:

```
1. GClose     — supreme (challenger bracket closing)
2. GOpen      — challenger bracket opening
3. G_domain   — domain reviewer(s)
4. G_lifecycle — lifecycle reviewer

GClose = FAIL overrides all other verdicts.
A HOLDS verdict from the challenger is not overturned by domain or lifecycle PASSes.
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot from that directory.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add rows. CHALLENGER bracket positions are fixed. State total count.)*

---

## BRACKET OPENING — CHALLENGER

**Authority acknowledged**: [ROLE_NAME] verdicts at authority level 2 (GOpen).

**Null hypothesis**: [What the team does today instead — one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW — how strong is the case for doing
nothing?]

**Findings and Challenges**:
1. [Finding 1 — challenger's `lens.verify`. Switching costs, workaround viability, or
   adoption friction.]
2. [Finding 2.]
3. [Optional: Finding 3.]

*(Issue a CH-ID for each finding that constitutes a specific claim downstream reviewers
must defeat:)*

> **CH-01**: [Challenge text — "The artifact must show..." / "The record must demonstrate..."
> — one sentence.]
>
> **CH-02**: [Optional — only if genuinely distinct.]

**Severity**: [HIGH / MEDIUM / LOW]
*Anchor: HIGH = artifact does not address null hypothesis; LOW = convincingly defeated.*

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**Contract Cite**: `DISPOSITION_CONTRACT: GOpen = [value]`

*GOpen, all CH-IDs, and the challenge texts above carry forward to all downstream sections.*

---

## DOMAIN — [ROLE_NAME]

**Authority acknowledged**: [ROLE_NAME] verdicts at authority level 3 (G_domain). This
reviewer may not override GOpen. If GClose issues FAIL, this reviewer's PASS does not
change the disposition.

*Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]*
*Challenges received: CH-01 [, CH-02 — copy from BRACKET OPENING]*

**Null hypothesis address**: [From this role's technical frame — does the artifact make
the workaround obsolete? One sentence.]

**Findings**:
1. [Finding 1 — from this role's `lens.verify` and `expertise.depth`. At least one
   finding must engage CH-01.]
2. [Finding 2.]
3. [Optional: Finding 3.]
4. [Optional: Finding 4.]

**Severity**: [HIGH / MEDIUM / LOW]
*Anchor: HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**CH-XX RESPONSE** *(mandatory — one entry per CH-ID issued in BRACKET OPENING)*:

> **CH-01**: [ANSWERED / PARTIAL / UNANSWERED]
> Evidence: [One sentence referencing the specific finding above. If PARTIAL: name the
> remaining gap. If UNANSWERED: state why; this blocks PASS.]
>
> **CH-02**: [ANSWERED / PARTIAL / UNANSWERED — complete only if CH-02 was issued.]
> Evidence: [...]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
*PASS blocked if any CH-XX = UNANSWERED.*
**G_domain Reason**: [One sentence. If CONDITIONAL: name the condition. If FAIL: name gap.]
**Contract Cite**: `DISPOSITION_CONTRACT: G_domain = [value]`

*(For `--depth deep`: repeat this section labeled DOMAIN-2, DOMAIN-3, etc. Each carries
its own authority acknowledgment, CH-XX RESPONSE block, and verdict cite. G_domain
aggregate = worst verdict; state explicitly after last domain section.)*

---

## LIFECYCLE — [ROLE_NAME]

**Authority acknowledged**: [ROLE_NAME] verdicts at authority level 4 (G_lifecycle). This
reviewer may not override GOpen or G_domain. If GClose issues FAIL, this reviewer's PASS
does not change the disposition.

*Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]*
*Received G_domain: [PASS / CONDITIONAL / FAIL — copy from DOMAIN; use aggregate if multiple]*
*Challenges received: CH-01 [, CH-02 — copy from BRACKET OPENING]*

**Decision-readiness assessment**: [Is evidence sufficient for commitment given GOpen and
G_domain? One paragraph referencing both verdicts explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, defeated? yes / partial / no —
one sentence.]

**Findings**:
1. [Finding 1 — from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [Finding 2.]

**Severity**: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**CH-XX RESPONSE** *(mandatory — one entry per CH-ID)*:

> **CH-01**: [ANSWERED / PARTIAL / UNANSWERED]
> Evidence: [One sentence from this role's commitment frame. If UNANSWERED: blocks PASS.]
>
> **CH-02**: [Complete only if issued.]
> Evidence: [...]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
*PASS blocked if any CH-XX = UNANSWERED.*
**G_lifecycle Reason**: [One sentence.]
**Contract Cite**: `DISPOSITION_CONTRACT: G_lifecycle = [value]`

---

## BRACKET CLOSING — CHALLENGER

**Authority acknowledged**: [ROLE_NAME] verdicts at authority level 1 (GClose — supreme).
Per REVIEW_AUTHORITY_HIERARCHY: GClose = FAIL constitutes BLOCKED regardless of G_domain
or G_lifecycle verdicts.

*Full record received: artifact + all gate findings and verdicts above.*

**Domain evidence assessment**:

| Reviewer | Null Hypothesis Address | CH-01 Answered? | [CH-02 Answered?] |
|----------|------------------------|-----------------|-------------------|
| [DOMAIN ROLE_NAME] | [One-sentence summary] | [yes / partial / no] | [...] |

**Lifecycle evidence assessment**: [Did lifecycle engage with the null hypothesis challenge?
yes / partial / no — one sentence.]

**Remaining gaps**: [What domain and lifecycle reviewers failed to address from the
challenges declared in BRACKET OPENING. If nothing: "None — all challenges addressed."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): accumulated record convincingly defeats null hypothesis.
- CONDITIONAL (= PARTIAL): record addresses some but leaves a named gap.
- FAIL (= HOLDS): null hypothesis survives; case for doing nothing is stronger.

**GClose Rationale**: [2–3 sentences.]
**Contract Cite**: `DISPOSITION_CONTRACT: GClose = [value]`
**Authority invocation**: [Per REVIEW_AUTHORITY_HIERARCHY: GClose = [value]. If FAIL:
"GClose = FAIL (supreme) overrides G_domain = [value] and G_lifecycle = [value].
BLOCKED."]

---

## SYNTHESIS

**Challenge Traceability Table**:

| ID | Challenge | Domain | Lifecycle | Net Status |
|----|-----------|--------|-----------|------------|
| CH-01 | [Copy challenge text from BRACKET OPENING] | [A/P/U] | [A/P/U] | [CLOSED / PARTIAL / OPEN] |
| CH-02 | [Copy if issued] | [A/P/U] | [A/P/U] | [CLOSED / PARTIAL / OPEN] |

**Unanswered challenges**: [CH-IDs with at least one UNANSWERED entry, or "None."]

**Cross-role signals**:
- **Conflicts**: [Two reviewers with incompatible recommendations — name roles and tension.
  If none: "None detected."]
- **Convergence**: [Two or more reviewers naming the same concern — name it and state why
  it is the highest-confidence signal.]

---

## DISPOSITION

**Gate vector** *(fill from sections above)*:

- GOpen = [copy from BRACKET OPENING]
- G_domain = [copy from DOMAIN; aggregate if multiple]
- G_lifecycle = [copy from LIFECYCLE]
- GClose = [copy from BRACKET CLOSING]

**Apply DISPOSITION_CONTRACT** *(do not alter formula; evaluate gate vector against
pre-stated contract)*:

```
G = { GOpen=[_], G_domain=[_], G_lifecycle=[_], GClose=[_] }
GClose = FAIL? → BLOCKED  (REVIEW_AUTHORITY_HIERARCHY: supreme override)
Any other Gi = FAIL? → BLOCKED
No FAIL, ∃ CONDITIONAL? → CONDITIONAL
All PASS? → READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED — result of applying
DISPOSITION_CONTRACT; not an editorial assertion.]

**Primary driver**: [The gate authority level and verdict most responsible — one sentence.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate — in contract order: GOpen before G_domain
   before G_lifecycle before GClose. Reference CH-ID if applicable.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [One sentence. If GClose = FAIL, lead with:
"REVIEW_AUTHORITY_HIERARCHY: GClose = FAIL (supreme) — [reason from GClose Rationale].
DISPOSITION_CONTRACT: BLOCKED."]

---

**Artifact to review:**

{{artifact}}

---

**Variation summary:**

| Variation | Single/Combined | Primary axis | New rubric target |
|-----------|----------------|--------------|-------------------|
| V-01 | Single | C-16: DISPOSITION_CONTRACT as named locked constant | C-16 isolation |
| V-02 | Single | C-17: CH-ID protocol with mandatory RESPONSE fields | C-17 isolation |
| V-03 | Single | C-18: REVIEW_AUTHORITY_HIERARCHY declared in preamble | C-18 isolation |
| V-04 | Combined | C-16 + C-17: algebra lock + challenge traceability | C-16 + C-17 |
| V-05 | Combined | C-16 + C-17 + C-18 + pre-printed template | C-16 + C-17 + C-18 |
