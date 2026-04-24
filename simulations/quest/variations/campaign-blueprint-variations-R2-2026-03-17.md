# campaign-blueprint Rubric v2 — Skill Variations V-01 through V-05

---

## V-01 — Single Axis: Inertia Framing

**Axis:** Inertia framing — the do-nothing option is treated as the primary competitor, named and quantified before writing begins.

**Hypothesis:** Foregrounding status-quo cost before drafting any artifact forces all three outputs to anchor against a concrete inertia baseline, making C-11 (quantified do-nothing) nearly impossible to miss and strengthening C-06 across all artifacts.

---

```markdown
You are executing the campaign-blueprint skill for the topic: **$ARGUMENTS**.

## Phase 0 — Name the Inertia Competitor

Before writing any artifact, answer these three questions in a visible block labeled `[INERTIA BASELINE]`:

1. **What do users do today** without this feature? (one sentence, concrete behavior)
2. **What is the cost of staying here?** Fill in at least one dimension:
   - Time cost: ___ hrs/week × ___ users = ___
   - Effort cost: ___ manual steps replaced by ___
   - Risk cost: ___ failure mode that persists without this feature
3. **What is the do-nothing option called?** Give it a name (e.g., "Option 0: Status Quo", "Option C: Continue Manual Process"). This name will appear in the proposal.

This block is your anchor. Every artifact must reference it.

---

## Phase 1 — Draft Spec

Write the technical specification. Required sections in order:

**PURPOSE** — What the feature does and why it exists. Include one sentence connecting to the inertia baseline you named above.

**REQUIREMENTS (MoSCoW)** — Must / Should / Could / Won't list. Minimum 3 Must items.

**DESIGN** — How it works. Include at least one diagram description or flow.

**CONSTRAINTS** — What the feature will not do, platform limits, scope boundaries.

**OPEN QUESTIONS** — At least two specific questions (not boilerplate). Split by discipline:
- Product/User domain: what do we not know about user behavior or business context?
- Technical/Architecture domain: what do we not know about implementation or system behavior?

End with: `[SPEC WRITTEN]`

---

## Phase 2 — Draft Proposal

Write the business proposal. Required structure:

**SITUATION** — One paragraph framing the opportunity. Reference the inertia baseline.

**OPTIONS** — At minimum three options:
- **Option 0: [Name from Phase 0]** — Do nothing. This section must include a quantified cost-of-inertia block:
  ```
  Cost of Option 0:
  - [Dimension 1]: [quantity or range]
  - [Dimension 2]: [quantity or range]
  - Risk if deferred: [specific failure mode]
  ```
- **Option 1** — Minimal viable implementation
- **Option 2** — Full implementation (or preferred alternative)

**RECOMMENDATION** — State the recommended option and reference the spec's key decisions.

End with: `[PROPOSAL WRITTEN — Option [X] recommended]`

---

## Phase 3 — Draft Pitch

Write three pitch versions for three distinct audiences. For each version, begin with:

> **What changes for [audience]:** [One sentence naming what is different about this version's framing, emphasis, or call to action — not just vocabulary, but a named delta from the base recommendation.]

**Exec version** — Business impact, cost of inertia, recommended option only.
**Developer version** — Technical design, constraints, open questions that affect implementation.
**Maker version** — User experience impact, what changes in daily workflow, concrete before/after.

Each version must include at least one "what this is NOT" statement.

End with: `[PITCH WRITTEN]`

---

## Completion Check

Before finishing, verify:
- [ ] `[INERTIA BASELINE]` block written with at least one quantified dimension
- [ ] `[SPEC WRITTEN]` tag present
- [ ] `[PROPOSAL WRITTEN — Option X recommended]` tag present — X matches the spec's direction
- [ ] `[PITCH WRITTEN]` tag present
- [ ] No cross-artifact contradictions: proposal references spec decisions, pitch references proposal recommendation
```

---

## V-02 — Single Axis: Execution Gate Markers

**Axis:** Lifecycle emphasis — every phase boundary is explicit, with dependency checks and completion tags that make execution state auditable in output.

**Hypothesis:** Requiring a visible dependency check before each phase and a completion tag after prevents the most common failure mode (writing pitch before proposal is settled) and makes C-05 (sequence integrity) mechanically enforced rather than aspirationally hoped for.

---

```markdown
You are executing the campaign-blueprint skill for the topic: **$ARGUMENTS**.

This skill runs three phases in strict sequence. Each phase begins with a dependency check and ends with a completion tag. Do not begin Phase N+1 until Phase N's completion tag is written.

---

## Phase 1 — Draft Spec

**[DEPENDENCY CHECK — SPEC]**
Required inputs: topic name ($ARGUMENTS). No prior artifacts needed.
Proceeding: YES

Write the technical specification with these five sections:

**PURPOSE** — One paragraph: what the feature does, why it exists, who it serves.

**REQUIREMENTS (MoSCoW)**
- Must: [at least 3 items]
- Should: [at least 2 items]
- Could: [at least 1 item]
- Won't: [at least 1 explicit exclusion]

**DESIGN** — Technical approach. Include at least one named component or flow step.

**CONSTRAINTS** — Platform limits, scope boundaries, explicit non-goals.

**OPEN QUESTIONS** — At least two specific, non-boilerplate questions that will affect design or implementation choices.

`[SPEC WRITTEN — key decisions: [list 2-3 decisions made in this spec that the proposal must honor]]`

---

## Phase 2 — Draft Proposal

**[DEPENDENCY CHECK — PROPOSAL]**
Required inputs: spec decisions listed in `[SPEC WRITTEN]` tag above.
Verify before proceeding:
- Spec decisions identified: [restate them here]
- Do-nothing option named: [name it]
Proceeding: YES

Write the business proposal:

**SITUATION** — Frame the opportunity in business terms. Reference what users do without this feature.

**OPTIONS** — Three options minimum:
- **Option 0: Do Nothing** — Current state. Include cost-of-inertia with at least one concrete dimension (time, effort, or risk).
- **Option 1** — Minimal approach
- **Option 2** — Recommended approach (or full build)

**RECOMMENDATION** — Name the recommended option. State which spec decisions it honors. State which open questions must be resolved before build begins.

`[PROPOSAL WRITTEN — Option [X] recommended — spec decisions honored: [list] — open questions blocking: [list or NONE]]`

---

## Phase 3 — Draft Pitch

**[DEPENDENCY CHECK — PITCH]**
Required inputs: proposal recommendation from `[PROPOSAL WRITTEN]` tag above.
Verify before proceeding:
- Recommended option: [restate it]
- Spec decisions in scope: [restate them]
- Blocking open questions: [restate or NONE]
Proceeding: YES

Write three audience versions of the pitch. Each version must be self-contained (no "as mentioned above").

**EXEC VERSION**
Audience: executive sponsor or budget holder.
Cover: business impact, cost of not acting, recommended option, ask.
Anti-positioning: at least one "what this is NOT" statement.
What changes for exec: [name the delta — what is different about this framing vs the base recommendation]

**DEVELOPER VERSION**
Audience: engineer who will implement.
Cover: technical design summary, constraints, open questions they need to answer.
Anti-positioning: at least one "what this is NOT" statement.
What changes for developer: [name the delta]

**MAKER VERSION**
Audience: end user or maker who will use the feature daily.
Cover: before/after workflow, what gets easier, what stays the same.
Anti-positioning: at least one "what this is NOT" statement.
What changes for maker: [name the delta]

`[PITCH WRITTEN — three versions: exec / developer / maker — all reference Option [X] from proposal]`

---

## Final Audit

Review the three completion tags. Confirm:
- Option letter is consistent across `[PROPOSAL WRITTEN]` and `[PITCH WRITTEN]`
- No spec decision contradicted in proposal or pitch
- All three pitch versions reference the same recommended option

`[CAMPAIGN COMPLETE — spec + proposal + pitch consistent, Option [X] throughout]`
```

---

## V-03 — Single Axis: Role Sequence (Discipline Split)

**Axis:** Role sequence — two named roles (PM and Architect) run alternating passes, each with a distinct gap-finding discipline, before any artifact prose is written.

**Hypothesis:** Assigning PM and Architect as explicit co-authors whose contributions are labeled produces deeper open questions (C-13) and forces the spec to surface unknowns that a single-voice draft misses, because each role has a different failure mode they are responsible for catching.

---

```markdown
You are executing the campaign-blueprint skill for the topic: **$ARGUMENTS**.

This skill uses two alternating voices throughout: **PM** (product/user/business domain) and **Architect** (technical/system/implementation domain). Each phase includes a PM pass and an Architect pass. Label contributions clearly.

---

## Phase 0 — Joint Gap Survey

Before writing, each role surfaces unknowns:

**PM — Business and User Unknowns:**
List 3–5 things we do not know about:
- User behavior or workflow
- Business context, stakeholders, or success metrics
- What "good" looks like from a user perspective

**Architect — Technical Unknowns:**
List 3–5 things we do not know about:
- System behavior, integration points, or edge cases
- Implementation constraints or platform limits
- What "done" looks like from a technical perspective

These lists feed the OPEN QUESTIONS section of the spec. Do not discard them.

---

## Phase 1 — Draft Spec

**PM pass — PURPOSE and REQUIREMENTS:**

Write PURPOSE: What does this feature do, why does it exist, who is it for? Include the inertia baseline: what do users do today without it?

Write REQUIREMENTS (MoSCoW):
- Must: [at least 3 items, user-facing or business-critical]
- Should: [at least 2 items]
- Could: [at least 1 item]
- Won't: [at least 1 explicit exclusion, user or scope boundary]

**Architect pass — DESIGN and CONSTRAINTS:**

Write DESIGN: How will this work technically? Name at least one component, interface, or flow step. Flag any design decisions that are not yet settled.

Write CONSTRAINTS: Platform limits, explicit non-goals from a system perspective, integration dependencies.

**Joint — OPEN QUESTIONS:**

Pull from the Phase 0 gap survey. Label each question by source:
- `[PM]` — product/user/business domain
- `[Architect]` — technical/architecture domain

Minimum: two questions total, at least one from each domain. Questions must be specific (not "is this feasible?" — instead: "does the existing event queue support back-pressure at 10k msg/sec?").

`[SPEC WRITTEN]`

---

## Phase 2 — Draft Proposal

**PM pass — SITUATION and RECOMMENDATION framing:**

Write SITUATION: Business context, user pain, opportunity. State what users do today (inertia baseline).

Draft the RECOMMENDATION narrative: which option serves the most users for the least coordination cost?

**Architect pass — OPTIONS technical assessment:**

Write or review each option for technical feasibility:
- **Option 0: Do Nothing** — Architect assesses: what technical debt accumulates if we don't build this? Include at least one concrete dimension (time, effort, or system risk).
- **Option 1** — Minimal implementation. Flag constraints or open questions that block it.
- **Option 2** — Full implementation. Flag the design decisions that must be settled first.

**Joint — RECOMMENDATION:**

PM names the recommended option and the user value rationale.
Architect confirms feasibility and names any blocking technical open questions.

`[PROPOSAL WRITTEN — Option [X] recommended]`

---

## Phase 3 — Draft Pitch

**PM pass — Exec and Maker versions:**

Write EXEC VERSION: Business impact, cost of inertia, recommended option, ask. Include one "what this is NOT" statement. State what changes for this audience vs the base recommendation.

Write MAKER VERSION: Before/after workflow, what gets easier, what stays the same. Include one "what this is NOT" statement. State what changes for this audience.

**Architect pass — Developer version:**

Write DEVELOPER VERSION: Technical design summary, constraints, open questions they own. Include one "what this is NOT" statement. State what changes for this audience vs the base recommendation.

`[PITCH WRITTEN]`

---

## Completion Check

- [ ] Phase 0 gap survey contributed at least one PM question and one Architect question to OPEN QUESTIONS
- [ ] All five spec sections present
- [ ] Proposal has three options including do-nothing with quantified cost dimension
- [ ] All three pitch versions present with per-audience delta statements
- [ ] No cross-artifact contradictions
```

---

## V-04 — Combined: Artifact Contract Matrix + Per-Audience Delta

**Axes combined:** Output format (artifact contract table declared upfront) + Lifecycle emphasis (per-audience delta as a named structural requirement at the pitch phase).

**Hypothesis:** Declaring a READ/WRITE/PRESERVE/CARRIES FORWARD contract before execution begins makes the sequence integrity check (C-05) structural rather than editorial, and requiring per-audience delta statements as labeled fields (not free-form prose) makes C-14 reliably present rather than sometimes present.

---

```markdown
You are executing the campaign-blueprint skill for the topic: **$ARGUMENTS**.

## Phase 0 — Artifact Contract Declaration

Before writing any artifact, declare the contract matrix. Fill in this table:

| Artifact | WRITES | READS FROM | PRESERVES | CARRIES FORWARD TO |
|---|---|---|---|---|
| Spec | Purpose, Requirements, Design, Constraints, Open Questions | (none — first artifact) | All decisions made explicit | Key decisions → Proposal |
| Proposal | Situation, Options, Recommendation | Spec: key decisions, constraints | All spec decisions | Recommended option → Pitch |
| Pitch | Exec / Dev / Maker versions | Proposal: recommended option; Spec: design summary | Proposal recommendation | (final artifact) |

Fill in the CARRIES FORWARD cells now, before writing:
- Spec carries forward: [list 2-3 decisions you expect to make in the spec]
- Proposal carries forward: [state the option you expect to recommend — update after writing if it changes]

`[CONTRACT DECLARED]`

---

## Phase 1 — Draft Spec

Write the technical specification:

**PURPOSE** — What the feature does, why it exists, who it serves. Include inertia baseline: what do users do today?

**REQUIREMENTS (MoSCoW)**
Must / Should / Could / Won't. Minimum 3 Must items, 1 explicit Won't.

**DESIGN** — Technical approach with at least one named component or flow.

**CONSTRAINTS** — Platform limits, explicit non-goals.

**OPEN QUESTIONS** — At least two specific questions, labeled by discipline:
- `[Product]` question about user behavior or business context
- `[Technical]` question about implementation or system behavior

Update the contract matrix: fill in "Spec CARRIES FORWARD" with the actual decisions made.

`[SPEC WRITTEN — carrying forward: [list decisions]]`

---

## Phase 2 — Draft Proposal

Verify contract: proposal must READ the decisions listed in `[SPEC WRITTEN]`.
State: "Reading spec decisions: [list them]"

Write the business proposal:

**SITUATION** — Business framing. Reference the inertia baseline.

**OPTIONS** — Minimum three:

**Option 0: Do Nothing**
```
Current state: [one sentence]
Cost of inertia:
  - [Dimension]: [quantity or range]
  - Risk if deferred: [specific failure mode]
  Qualitative: [one sentence on user experience impact]
```

**Option 1: [Name]** — [description, tradeoffs]
**Option 2: [Name]** — [description, tradeoffs, why preferred if recommending this]

**RECOMMENDATION** — Name the option. Confirm it honors the spec decisions listed above.

Update the contract matrix: fill in "Proposal CARRIES FORWARD" with the actual recommended option.

`[PROPOSAL WRITTEN — Option [X] recommended — carrying forward to pitch: Option X]`

---

## Phase 3 — Draft Pitch

Verify contract: pitch must READ the recommended option from `[PROPOSAL WRITTEN]`.
State: "Reading recommendation: Option [X] — [name]"

Write three audience versions. Each version has a required structural field:

**EXEC VERSION**

> **Audience delta:** [One sentence: what is different about this version's framing or ask, specifically for an exec audience, compared to the base recommendation? Name the delta — e.g., "Frames cost-of-inertia as competitive risk rather than productivity loss."]

Content: business impact, cost of inertia, recommended option, ask.
Anti-positioning: "This is NOT [statement]."

**DEVELOPER VERSION**

> **Audience delta:** [One sentence: what is different about this version for a developer? Name the delta — e.g., "Surfaces the two open questions they must resolve before sprint planning."]

Content: technical design, constraints, open questions they own.
Anti-positioning: "This is NOT [statement]."

**MAKER VERSION**

> **Audience delta:** [One sentence: what is different about this version for the end user? Name the delta — e.g., "Replaces option-level framing with before/after workflow comparison."]

Content: before/after workflow, what gets easier, what stays the same.
Anti-positioning: "This is NOT [statement]."

`[PITCH WRITTEN — exec / developer / maker — all reference Option [X]]`

---

## Final Contract Audit

Review the contract matrix you declared in Phase 0. For each row, confirm:
- Spec carried forward the decisions it declared
- Proposal read those decisions (no contradictions)
- Pitch reads the recommended option (consistent option letter throughout)

`[CAMPAIGN COMPLETE — contract honored, Option [X] consistent across all three artifacts]`
```

---

## V-05 — Combined: All Four Aspirational Patterns

**Axes combined:** Phase 0 setup (contract matrix) + inertia framing (quantified do-nothing) + execution gate markers + discipline-split open questions + per-audience delta.

**Hypothesis:** Stacking all four aspirational patterns in a single skill body produces a near-complete artifact suite (targeting ≥ 100/120) because each pattern addresses a different failure mode: contract prevents contradictions, inertia forces quantification, gates enforce sequence, discipline split deepens open questions, and delta statements prevent pitch versions from being superficial restatements.

---

```markdown
You are executing the campaign-blueprint skill for the topic: **$ARGUMENTS**.

This skill runs in five phases. Complete each phase fully before proceeding. Completion tags are required — they are your execution audit trail.

---

## Phase 0 — Setup: Contract + Inertia Baseline

**Step 0A — Artifact Contract Matrix**

Declare what each artifact owns before writing any of them:

| Artifact | WRITES | READS FROM | CARRIES FORWARD |
|---|---|---|---|
| Spec | Purpose · Requirements · Design · Constraints · Open Questions | (none) | Key decisions → Proposal |
| Proposal | Situation · Options · Recommendation | Spec decisions | Recommended option → Pitch |
| Pitch | Exec · Dev · Maker versions | Proposal recommendation | (terminal) |

Pre-fill "Spec CARRIES FORWARD": list 2–3 decisions you expect to make.
Pre-fill "Proposal CARRIES FORWARD": state your best-guess recommendation option (will be confirmed after writing).

**Step 0B — Inertia Baseline**

Answer before writing any artifact:

```
[INERTIA BASELINE]
Current user behavior: [what users do today without this feature]
Cost of inertia:
  Time cost:   [X hrs/week × Y users] OR [N/A — not time-driven]
  Effort cost: [X manual steps replaced] OR [N/A]
  Risk cost:   [specific failure mode that persists without this feature]
Do-nothing option name: [Option 0: ___]
```

**Step 0C — Gap Survey (Discipline Split)**

Before writing, surface unknowns by domain:

`[PM gaps]` — 3 things we do not know about user behavior, business context, or success metrics:
1.
2.
3.

`[Architect gaps]` — 3 things we do not know about implementation, system behavior, or integration:
1.
2.
3.

These feed the OPEN QUESTIONS section. Keep them visible.

`[SETUP COMPLETE — contract declared, inertia baseline set, gaps surveyed]`

---

## Phase 1 — Draft Spec

**[DEPENDENCY CHECK — SPEC]** Contract declared: YES. Inertia baseline set: YES. Proceeding.

**PURPOSE** — What the feature does, why it exists. One sentence connecting to the inertia baseline.

**REQUIREMENTS (MoSCoW)**
- Must: [≥ 3 items]
- Should: [≥ 2 items]
- Could: [≥ 1 item]
- Won't: [≥ 1 explicit exclusion]

**DESIGN** — Technical approach. At least one named component, interface, or flow step. Flag any unsettled design decisions.

**CONSTRAINTS** — Platform limits, explicit non-goals, scope boundaries.

**OPEN QUESTIONS** — Pull from the Phase 0 gap survey. Label each:
- `[PM]` at least one product/user/business question
- `[Architect]` at least one technical/architecture question
- Minimum two questions total. Questions must be specific and decision-relevant.

Update the contract matrix: confirm which decisions are now settled (carries forward to proposal).

`[SPEC WRITTEN — key decisions carrying forward: [list 2-3 decisions]]`

---

## Phase 2 — Draft Proposal

**[DEPENDENCY CHECK — PROPOSAL]**
Reading spec decisions: [restate the decisions from `[SPEC WRITTEN]`]
Inertia baseline option name: [restate from Phase 0]
Proceeding: YES

**SITUATION** — Business framing. Reference the inertia baseline (what users do today, cost of staying there).

**OPTIONS**

**Option 0: [Name from Phase 0]** — Do Nothing
```
Current state: [one sentence]
Quantified cost of inertia:
  [Dimension 1]: [quantity or range]
  [Dimension 2]: [quantity or range — or N/A with reason]
  Risk if deferred: [specific failure mode]
```

**Option 1: [Name]** — [description, tradeoffs, feasibility notes]

**Option 2: [Name]** — [description, tradeoffs, why preferred if this is the recommendation]

*(Add Option 3 if a meaningful alternative exists)*

**RECOMMENDATION** — Name the recommended option. Confirm it honors the spec decisions listed in the dependency check. Name any blocking open questions.

Update the contract matrix: confirmed recommendation is Option [X].

`[PROPOSAL WRITTEN — Option [X] recommended — spec decisions honored — blocking open questions: [list or NONE]]`

---

## Phase 3 — Draft Pitch

**[DEPENDENCY CHECK — PITCH]**
Reading recommendation: Option [X] — [name]
Spec design summary in scope: YES
Blocking open questions: [restate or NONE]
Proceeding: YES

Write three audience versions. Each version has three required structural elements:
1. **Audience delta** (labeled field) — what changes for this audience specifically
2. **Anti-positioning** — at least one "what this is NOT" statement
3. **Reference to Option [X]** — explicit, not implied

---

**EXEC VERSION**

> **Audience delta:** [One sentence naming the specific framing shift for an exec. Example: "Frames cost-of-inertia as competitive exposure rather than team productivity loss."]

Content:
- Business impact of Option [X]
- Quantified cost of Option 0 (do nothing) in business terms
- Recommended option and ask
- "This is NOT [anti-positioning statement]."

---

**DEVELOPER VERSION**

> **Audience delta:** [One sentence naming the specific shift for a developer. Example: "Shifts from business case to open questions that must be resolved before sprint planning begins."]

Content:
- Technical design summary (from spec DESIGN section)
- Constraints and non-goals relevant to implementation
- Open questions labeled `[Architect]` that developers own
- "This is NOT [anti-positioning statement]."

---

**MAKER VERSION**

> **Audience delta:** [One sentence naming the specific shift for a maker/end user. Example: "Replaces option-level framing with a before/after workflow comparison against what they do today."]

Content:
- Before: [current behavior from inertia baseline]
- After: [what changes with Option [X]]
- What stays the same
- "This is NOT [anti-positioning statement]."

`[PITCH WRITTEN — exec / developer / maker — all reference Option [X]]`

---

## Phase 4 — Final Audit

**Sequence integrity check:**
- [ ] Proposal references spec decisions from `[SPEC WRITTEN]` — no contradictions
- [ ] Pitch references Option [X] from `[PROPOSAL WRITTEN]` — no contradictions
- [ ] Option letter consistent: `[PROPOSAL WRITTEN — Option X]` matches `[PITCH WRITTEN — Option X]`

**Coverage check:**
- [ ] `[INERTIA BASELINE]` present with ≥ 1 quantified dimension
- [ ] Option 0 in proposal has quantified cost-of-inertia block
- [ ] OPEN QUESTIONS has ≥ 1 `[PM]` and ≥ 1 `[Architect]` question
- [ ] All three pitch versions have labeled "Audience delta" field
- [ ] All three pitch versions have ≥ 1 anti-positioning statement
- [ ] Completion tags present: `[SETUP COMPLETE]`, `[SPEC WRITTEN]`, `[PROPOSAL WRITTEN]`, `[PITCH WRITTEN]`

`[CAMPAIGN COMPLETE — all checks passed — Option [X] consistent throughout]`
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Hypothesis | New Criteria Targeted |
|---|---|---|---|---|
| V-01 | Inertia framing | — | Foregrounding do-nothing forces quantification across all artifacts | C-11, C-06 |
| V-02 | Lifecycle / gate markers | — | Completion tags make C-05 mechanically enforced | C-12, C-05 |
| V-03 | Role sequence (PM + Architect) | — | Discipline-split voices produce deeper open questions | C-13, C-08 |
| V-04 | Output format (contract table) | Per-audience delta as labeled field | Structural contract prevents contradictions; delta as field prevents omission | C-09, C-14 |
| V-05 | All four aspirational patterns | — | Stacking all patterns targets ≥ 100/120 by addressing each failure mode separately | C-09–C-14 |
