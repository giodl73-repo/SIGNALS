# org-review Variations — Round 2
Generated: 2026-03-15
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v2-2026-03-15.md

Round 1 axes already explored: inertia-first sequence (V-01), strict table (V-02), null-hypothesis-universal inertia framing (V-03), formal register + lifecycle phases (V-04), parallel blind reviews + structured prose (V-05).

Round 2 strategy: three single-axis variations on underexplored axes, then two combinations that target C-11 + C-12 structurally (making disposition code and null-hypothesis anchoring emerge from the format, not from editorial judgment).

---

## V-01 — Output Format: Multi-Dimension Scorecard

**Variation axis**: Output format — each reviewer scores the artifact on three dimensions (Decision-Readiness, Technical-Soundness, Inertia-Risk) at levels 1–3, alongside the four required fields
**Hypothesis**: A multi-dimension score separates severity into three components that different roles naturally weight differently. The PM's primary axis is Decision-Readiness; the architect's is Technical-Soundness; the inertia-advocate's is Inertia-Risk. Structural separation at the score level forces C-03 divergence even when reviewers might otherwise produce similar prose, and makes cross-role weighting conflicts (C-09) appear in the numbers before they appear in words. C-12 null hypothesis anchoring emerges as a required cell in every scorecard row.

---

You are running `org-review` on the artifact provided below.

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select reviewers whose `expertise.relevance` matches this artifact type. Minimum 2 roles. State each selected role and one-sentence selection rationale.
- **`--depth deep`**: Include all roles in `.craft/roles/signal/`. State the total count.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Reviewer Scorecards**

For each selected reviewer, produce a scorecard section:

---
**[Role name] — [Role archetype]**

**Null Hypothesis Stance**: From this role's perspective, does the artifact justify building over doing nothing? One sentence: yes / conditional / no, with the reason from this role's frame.

**Findings**: 2–4 findings grounded in this role's `lens.verify` and `expertise.depth`. Stay in this role's frame. Do not echo other reviewers.

**Dimension Scores** (1 = low / 2 = moderate / 3 = high):

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Decision-Readiness | 1/2/3 | [Is the decision case strong enough to act?] |
| Technical-Soundness | 1/2/3 | [Is the implementation approach viable as specified?] |
| Inertia-Risk | 1/2/3 | [How strong is the case for doing nothing? 3 = null hypothesis is strong] |

Score guidance:
- **Decision-Readiness** is the PM's primary axis. 3 = commitment is clearly justified; 1 = decision case is absent or insufficient.
- **Technical-Soundness** is the architect's primary axis. 3 = spec is implementable as written; 1 = unresolved boundary or complexity issues.
- **Inertia-Risk** is the inertia-advocate's primary axis. 3 = status quo is not threatened (null hypothesis is strong); 1 = artifact clearly defeats the workaround.

Not every reviewer weights all three dimensions equally. A PM scoring Technical-Soundness is less authoritative than an architect doing the same. A reviewer's primary axis score carries the most weight.

**Overall Severity**: HIGH / MEDIUM / LOW — driven by the lowest primary-axis score for this reviewer. Anchor: HIGH = blocks commitment, MEDIUM = conditions commitment, LOW = advisory.

**Recommendation**: One concrete action from this role's expertise frame.

**Verify Question**: One question from this role's `lens.verify` list.

**Simplify**: One observation from this role's `lens.simplify` — what could be removed, collapsed, or clarified?

---

[Repeat for each selected reviewer]

**Step 3 — Scorecard Matrix**

Produce an aggregated table:

| Role | Decision-Readiness | Technical-Soundness | Inertia-Risk | Severity | Recommendation |
|------|--------------------|---------------------|--------------|----------|----------------|

Scan the matrix for:
- **Dimension conflicts**: Two roles scoring the same dimension differently (e.g., PM scores Decision-Readiness 3; inertia-advocate scores it 1). Name any such conflicts — they are the most important cross-role signals.
- **Dimension gaps**: Any dimension where no reviewer scored it highly (all ≤ 2). This signals an artifact area with no strong advocate.

**Step 4 — Disposition**

Based on the scorecard matrix, emit:

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

- **READY**: All primary-axis scores are ≥ 2 across roles. No HIGH severity findings.
- **CONDITIONAL**: At least one MEDIUM finding exists, or at least one dimension has a cross-role conflict. State the conditions.
- **BLOCKED**: At least one HIGH severity finding, or a primary-axis score of 1 that is undisputed. State the blocker.

Include one sentence naming the highest-severity finding or dimension conflict driving the disposition.

**Artifact to review:**

{{artifact}}

---

## V-02 — Lifecycle Emphasis: Four-Gate Structure

**Variation axis**: Lifecycle emphasis — the review is structured as four sequential gates that the artifact must pass in order; each reviewer is assigned to the gate most relevant to their archetype
**Hypothesis**: An explicit gate sequence (Null Hypothesis → Domain Evidence → Commitment Readiness → Synthesis) assigns reviewers to lifecycle phases, not just artifact types. C-05 (depth flag) becomes visible at the gate level: deep runs add reviewers per gate. C-11 (disposition code) becomes a natural gate-pass/fail aggregate rather than an editorial conclusion. C-12 (null hypothesis anchoring) is mandatory output of Gate 1, which every subsequent gate must reference.

---

You are running `org-review` on the artifact provided below.

This review is structured as four sequential gates. An artifact must pass each gate to advance. Gate failures produce a CONDITIONAL or BLOCKED disposition at the end.

**Gate 0 — Reviewer Manifest**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select reviewers whose `expertise.relevance` matches this artifact type. Assign each reviewer to the gate most appropriate to their archetype (Gate 1 = challenger/inertia archetypes; Gate 2 = technical/domain archetypes; Gate 3 = product/PM archetypes). State assignments.
- **`--depth deep`**: Include all roles from `.craft/roles/signal/`. Assign each to their gate. State total count and gate distribution.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

**Gate 1 — Null Hypothesis Gate**

The inertia-advocate reviews the artifact first, in isolation, before any other reviewer speaks.

Task: Construct the null hypothesis — what is the team doing today instead of building this? Is the null hypothesis named in the artifact? Does the artifact provide evidence that defeats it?

Output:
- **Null Hypothesis Statement**: What the team does today instead of this feature (one sentence).
- **Artifact's Response**: Does the artifact address this? yes / partial / no
- **Findings**: 2–3 findings from the inertia-advocate's lens — switching costs, workaround viability, adoption friction.
- **Gate 1 Verdict**: PASS (artifact names and addresses the null hypothesis) / CONDITIONAL (artifact names it but incompletely addresses it) / FAIL (null hypothesis not addressed)
- **Verify Question**: One question from the inertia-advocate's verify lens.

**Gate 2 — Domain Evidence Gate**

Technical and domain reviewers evaluate whether the artifact's evidence base and technical approach are sound. These reviewers have seen Gate 1's null hypothesis statement but not Gate 1's verdict.

For each domain reviewer assigned to Gate 2:

**[Role name]**

- **Findings**: 2–4 findings from this role's lens. Reference the null hypothesis where relevant: does the technical approach make the workaround clearly obsolete?
- **Severity**: HIGH / MEDIUM / LOW (HIGH = blocks commitment, MEDIUM = conditions it, LOW = advisory)
- **Gate 2 Verdict**: PASS / CONDITIONAL / FAIL for this reviewer's dimension
- **Verify Question**: One from this role's verify lens.
- **Simplify**: One observation from this role's simplify lens.

If multiple domain reviewers are assigned to Gate 2, each produces their own entry. Their verdicts are independent.

**Gate 3 — Commitment Readiness Gate**

The PM (or product-archetype reviewer) evaluates whether the accumulated evidence from Gates 1 and 2 supports a commitment decision. This reviewer has access to all prior gate outputs.

Output:
- **Decision-Readiness Assessment**: Given the artifact and prior gate findings, is the decision case strong enough to commit? State why.
- **Null Hypothesis Address**: Does the accumulated record defeat the null hypothesis established in Gate 1?
- **Severity**: HIGH / MEDIUM / LOW
- **Gate 3 Verdict**: PASS / CONDITIONAL / FAIL
- **Condition** *(if CONDITIONAL)*: What specific condition must be met before commitment?
- **Verify Question**: One from this role's verify lens.
- **Simplify**: One observation from this role's simplify lens.

**Gate 4 — Synthesis and Disposition**

Aggregate the gate verdicts:

**Gate Summary Table**:

| Gate | Reviewer | Verdict | Primary Finding |
|------|----------|---------|-----------------|

**Cross-Gate Conflicts**: Where do gate verdicts contradict each other? Name any roles whose verdicts are incompatible and state the decision the reader must make to resolve the conflict.

**Areas Not Covered**: Any aspect of the artifact that no gate reviewer examined.

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

Logic:
- **READY**: All gates PASS.
- **CONDITIONAL**: At least one gate CONDITIONAL; no gate FAIL.
- **BLOCKED**: At least one gate FAIL.

Include one sentence naming the gate or reviewer finding that drives the disposition.

**Artifact to review:**

{{artifact}}

---

## V-03 — Inertia Framing: Challenger-Last (Rebuttal Structure)

**Variation axis**: Inertia framing — the inertia-advocate runs last, reading all domain reviewers' findings as the record to rebut; domain reviewers build the positive case first without knowing the challenger's frame
**Hypothesis**: Challenger-last is the structural opposite of Round 1 V-01's inertia-first. When the inertia-advocate runs last, their findings address the accumulated case the other reviewers made — they can attack specific arguments rather than setting a general baseline. This tests whether a targeted rebuttal structure or a baseline-setting structure more effectively forces C-12 null hypothesis anchoring across all roles, and whether it produces stronger C-09 conflict detection (inertia's rebuttal of domain findings is a named conflict, not a coincidental overlap).

---

You are running `org-review` on the artifact provided below.

In this review, the inertia-advocate runs last. Domain reviewers build the positive case first. The inertia-advocate then reads the accumulated record and decides whether it defeats the null hypothesis.

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select domain reviewers (non-challenger archetypes) whose `expertise.relevance` matches this artifact type. The inertia-advocate is always included and always runs last. State the selected domain roles and selection rationale.
- **`--depth deep`**: Include all non-challenger roles from `.craft/roles/signal/`, plus the inertia-advocate (last). State total count.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Domain Reviews**

These reviewers have not seen the inertia challenge. They review the artifact on its own merits.

For each domain reviewer:

---
**[Role name] — [Role archetype]**

**Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. Frame from this role's orientation only. Do not anticipate or address the inertia case.

**Severity**: HIGH / MEDIUM / LOW (HIGH = blocks commitment, MEDIUM = conditions it, LOW = advisory)

**Recommendation**: One concrete action from this role's frame.

**Verify Question**: One question from this role's `lens.verify` list.

**Simplify**: One observation from this role's `lens.simplify`.

**Build/Don't-Build Stance**: From this role's perspective, does the evidence support building? One sentence: yes / yes with conditions / no, and why.

---

[Repeat for each domain reviewer]

**Step 3 — Inertia-Advocate Rebuttal**

The inertia-advocate now reviews the full record: the artifact AND all domain reviewers' findings above. This reviewer has access to everything.

**The Null Hypothesis**: What is the team doing today instead of building this? State it explicitly in one sentence.

**Record Assessment**: For each domain reviewer, evaluate their Build/Don't-Build stance. Does it actually address the null hypothesis?

| Domain Reviewer | Their Build/Don't-Build Stance | Addresses the Null Hypothesis? |
|-----------------|-------------------------------|--------------------------------|
| [role] | [summary of stance] | yes / partial / no |

**Inertia-Advocate Findings**: 2–4 findings from the inertia-advocate's lens — switching costs, workaround viability, adoption friction. Focus on what the domain reviewers failed to address.

**Severity**: HIGH / MEDIUM / LOW — calibrate to how well the accumulated record defeats the null hypothesis.

**Recommendation**: One concrete action, from the inertia-advocate's frame.

**Verify Question**: One question from the inertia-advocate's verify lens.

**Rebuttal Verdict**: DEFEATS NULL / PARTIAL / DOES NOT DEFEAT NULL

- **Condition** *(if PARTIAL)*: What specific gap must the artifact address to defeat the null hypothesis?
- **Blocker** *(if DOES NOT DEFEAT NULL)*: What is the strongest argument for the status quo that the record fails to answer?

**Step 4 — Cross-Role Summary**

After all reviews:

- **Where domain reviewers agreed** (same concern, same severity, or same recommendation)
- **Where domain reviewers diverged** (incompatible recommendations — name the roles and the tension)
- **Inertia verdict vs. domain consensus**: Does the inertia-advocate's rebuttal verdict align with or overturn the domain reviewers' collective build stance?
- **Overall Disposition**: READY / CONDITIONAL / BLOCKED — one sentence naming the primary driver

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Inertia Bracket + Per-Role Null Hypothesis Verdict

**Variation axes**: Role sequence (inertia-advocate runs first AND last, bracketing domain reviews) + explicit per-role null hypothesis verdict required from every domain reviewer
**Hypothesis**: A bracket structure where inertia sets the null hypothesis, domain reviewers must individually address it, and inertia delivers a final verdict on whether the accumulated evidence defeats it — this is a stronger C-12 mechanism than independently asking each role to anchor. The bracket also creates a natural C-09 opportunity: if PM and architect produce strong counter-evidence but inertia's final verdict still holds (null hypothesis not defeated), that overturn is the most important finding in the review, not buried in a single-reviewer section.

---

You are running `org-review` on the artifact provided below.

This review uses a bracket structure. The inertia-advocate runs twice: first to set the null hypothesis, last to deliver a final verdict on whether the accumulated evidence defeats it. Domain reviewers run between the two bracket positions and must each explicitly address the null hypothesis established in Round 1.

**Setup — Role Registry**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select domain reviewers most relevant to this artifact type. The inertia-advocate always participates in both bracket positions. State selected domain roles and selection rationale (one sentence each).
- **`--depth deep`**: Include all roles from `.craft/roles/signal/`. The inertia-advocate bracket remains in place; all other roles run between the two bracket positions. State total count.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

**Bracket Round 1 — Inertia-Advocate: Null Hypothesis Declaration**

The inertia-advocate reviews the artifact first. This is a declaration pass, not a full review.

Output:
- **Null Hypothesis**: What is the team doing today instead of building this? One sentence.
- **Null Hypothesis Strength**: How strong is the case for doing nothing? HIGH / MEDIUM / LOW — with a one-sentence rationale.
- **Challenge to Domain Reviewers**: One specific question or gap the domain reviewers must address to defeat this null hypothesis. This is the anchor every domain reviewer must respond to.

**Domain Reviews (middle of bracket)**

Each domain reviewer has seen the null hypothesis declaration above. Every reviewer must address it.

For each domain reviewer:

---
**[Role name]**

**Null Hypothesis Address** *(required)*: From this role's perspective, does the artifact defeat the null hypothesis set in Bracket Round 1? Answer: yes / conditional / no. Give the reason from this role's frame. The PM's answer is about decision sufficiency. The architect's answer is about whether the technical approach makes the workaround obsolete. These answers must differ substantively from each other.

**Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. At least one finding must connect to the null hypothesis. Other findings may address other artifact concerns.

**Severity**: HIGH / MEDIUM / LOW (HIGH = blocks commitment, MEDIUM = conditions it, LOW = advisory). Calibrate independently — do not copy another reviewer's level.

**Recommendation**: One concrete action from this role's expertise frame.

**Verify Question**: One question from this role's `lens.verify` list.

**Simplify**: One observation from this role's `lens.simplify`.

---

[Repeat for each domain reviewer]

**Bracket Round 2 — Inertia-Advocate: Final Verdict**

The inertia-advocate reads the full record: artifact + all domain reviewer findings. This is the closing bracket.

**Record Review**: For each domain reviewer, assess their null hypothesis address:

| Reviewer | Null Hypothesis Address (summary) | Adequate? |
|----------|----------------------------------|-----------|
| [role] | [summary of stance] | yes / partial / no |

**Remaining Gaps**: What aspects of the null hypothesis the domain reviewers failed to address.

**Inertia-Advocate Final Verdict**: DEFEATED / PARTIAL DEFEAT / HOLDS

- **DEFEATED**: The accumulated record convincingly answers the null hypothesis. The case for doing nothing has been addressed.
- **PARTIAL DEFEAT**: The record addresses some of the null hypothesis but leaves material gaps that, if unresolved, would justify the status quo.
- **HOLDS**: The null hypothesis survives the review. The case for doing nothing is stronger than the case for building.

**Rationale**: 2–3 sentences explaining the verdict.

**Step 5 — Synthesis**

- **Cross-role conflicts**: Did any two domain reviewers give incompatible recommendations? Name the roles and the tension.
- **Inertia-verdict alignment**: Does the inertia final verdict (Bracket Round 2) align with the domain reviewers' collective recommendation, or does it overturn it? If it overturns it, name that as an explicit conflict — this is the most important finding in the review.
- **Areas not covered**: Any artifact section no reviewer examined.
- **Overall Disposition**: READY / CONDITIONAL / BLOCKED
  - READY: Final inertia verdict = DEFEATED + no unresolved HIGH findings
  - CONDITIONAL: Final inertia verdict = PARTIAL DEFEAT, or MEDIUM findings remain
  - BLOCKED: Final inertia verdict = HOLDS, or any HIGH finding unresolved

Include one sentence naming the primary driver of the disposition.

**Artifact to review:**

{{artifact}}

---

## V-05 — Combination: Verdict Cards + Structured Disposition Matrix

**Variation axes**: Output format (each reviewer issues a BUILD / CONDITIONAL / BLOCK verdict card) + disposition code emerges structurally from aggregating verdict cards into a matrix, not from editorial judgment
**Hypothesis**: When each reviewer produces a structured verdict card (verdict + primary evidence + condition if CONDITIONAL + blocker if BLOCK), the disposition code (C-11) becomes a computation over the cards rather than an editorial decision. Cross-role conflicts (C-09) become structurally visible as divergent verdicts in the matrix. C-12 null hypothesis anchoring is enforced by requiring each verdict card to include a null hypothesis stance — the reviewer must say why they chose BUILD vs. BLOCK vs. CONDITIONAL, which requires addressing the build/don't-build question explicitly.

---

You are running `org-review` on the artifact provided below.

Each reviewer issues a structured verdict card: BUILD / CONDITIONAL / BLOCK, plus the evidence and reasoning that drives that verdict. The cards are aggregated into a disposition matrix to produce the overall signal.

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select reviewers from `.craft/roles/signal/` whose `expertise.relevance` matches this artifact type. Minimum 2 reviewers; the inertia-advocate is always included. State which roles were selected and why.
- **`--depth deep`**: Include all roles in `.craft/roles/signal/`. State total count. Every reviewer issues a verdict card.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Verdict Cards**

For each selected reviewer, produce a verdict card using this exact structure:

---
**VERDICT CARD: [Role name] ([Role archetype])**

**Verdict**: BUILD / CONDITIONAL / BLOCK *(choose exactly one)*

- **BUILD**: This reviewer's analysis supports committing to this feature. Evidence is sufficient from their frame.
- **CONDITIONAL**: This reviewer supports building, contingent on a named condition being met first.
- **BLOCK**: This reviewer's analysis does not support commitment. A named blocker must be resolved before commitment.

**Null Hypothesis Stance**: From this role's perspective — does the artifact justify building over doing nothing? One sentence framed from this role's lens (PM: decision sufficiency; architect: technical justification over workaround; inertia-advocate: workaround viability).

**Primary Evidence**: The 1–2 findings most important to this verdict. Grounded in this role's `lens.verify` and `expertise.depth`. These findings must differ substantively from other reviewers' primary evidence — different frame, different concern, different artifact dimension.

**Severity**: HIGH / MEDIUM / LOW for the primary finding (HIGH = blocks commitment, MEDIUM = conditions it, LOW = advisory).

**Condition** *(required if CONDITIONAL)*: Exactly what must be true before this reviewer changes their verdict to BUILD? One sentence.

**Blocker** *(required if BLOCK)*: Exactly what must be resolved before this reviewer changes their verdict to CONDITIONAL or BUILD? One sentence.

**Verify Question**: One question from this role's `lens.verify` list.

**Simplify**: One observation from this role's `lens.simplify`.

---

[Repeat for each selected reviewer]

**Step 3 — Verdict Matrix**

Produce an aggregated matrix:

| Role | Verdict | Primary Finding | Severity | Condition / Blocker |
|------|---------|-----------------|----------|---------------------|

Scan the matrix for:
- **Conflicts**: Two reviewers with opposite verdicts (one BUILD, one BLOCK). Name both roles and describe the tension in one sentence. This is the most important output of the matrix.
- **CONDITIONAL convergence**: Multiple reviewers naming the same condition — this is a high-confidence gate that must be met before commitment.
- **Orphan blockers**: A BLOCK verdict whose named blocker is not mentioned by any other reviewer — may represent a perspective blind spot or a false positive. Flag for author follow-up.

**Step 4 — Disposition**

Based on the verdict matrix, compute the overall disposition:

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

Logic:
- **READY**: All verdict cards are BUILD. No BLOCK verdicts. No unresolved HIGH severity findings.
- **CONDITIONAL**: At least one CONDITIONAL verdict; no BLOCK verdicts. State the conditions in priority order (highest-confidence gates first).
- **BLOCKED**: At least one BLOCK verdict, or any HIGH finding that no other reviewer disputes as authoritative.

Tiebreaker when verdicts conflict: A BLOCK verdict from the inertia-advocate carries the highest weight — the null hypothesis must be defeated for READY or CONDITIONAL to hold. A BUILD verdict from a single domain reviewer does not override an inertia-advocate BLOCK unless supported by at least one other reviewer.

Include one sentence naming the verdict card or matrix conflict most responsible for the disposition.

**Artifact to review:**

{{artifact}}
