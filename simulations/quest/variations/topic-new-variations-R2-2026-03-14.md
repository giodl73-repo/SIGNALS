Here are the 5 R2 variations, written to `simulations/quest/variations/topic-new-variations-R2-2026-03-14.md`.

---

## Round 2 Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Role sequence | Four canonical roles (PM/Engineer/Designer/Researcher) enumerated before any task — model draws from a named set, preventing C-08 collapse |
| **V-02** | Inertia framing | Opens with the failure scenario ("teams commit without evidence"); commit gate becomes the skill's existential purpose, not a section to fill in |
| **V-03** | Extreme compression | All 13 criteria in ~50 lines — tests whether structure is the mechanism, not length |
| **V-04** | Role sequence + inertia | Leads with "who is at risk?" then maps risk-owners to signal ownership; both new axes combined |
| **V-05** | Inertia + pervasive consequence | Every field rule and coverage requirement carries its downstream-failure consequence — not just C-04 |

**Key R2 design intent:** All five variations explicitly bake in C-11 (checkbox-gate before phase transition), C-12 (operational consequence for invalid vocab), and C-13 (dedicated `## Commit Gate` + `## Naming Reference` sections). The variations differ in *how* they deliver those patterns — not whether they deliver them.

**Predicted ceiling:** V-05 — consequence framing on every rule means no constraint reads as a style preference. V-03 is the most interesting stress test: if it scores 100, the structural patterns are length-independent and V-05's elaboration is rhetorical rather than mechanical.
t carries its downstream-failure consequence — not just C-04 | "Coverage gate — verify before writing the file" checklist | "loses the ability to hold a design commit" | ## Commit Gate + ## Naming Reference as sections |

**Predicted ceiling:** V-05 — consequence framing on every rule means no constraint can be read as a style preference. V-04 is next; the role taxonomy anchors C-08 structurally, and inertia framing elevates C-09 from formality to operational purpose. V-03 tests the floor: if the structural patterns (checkbox-gate, operational consequence, dedicated sections) work in minimal form, length is not the mechanism.

**New axes explored in R2:** Role sequence (V-01, V-04) and inertia framing (V-02, V-04, V-05) were not covered in R1. All R1 variations used task-first sequencing and neutral register. R2 tests whether leading with roles or leading with the failure scenario changes how the model produces the signal plan.

**Key difference from R1:** All five R2 variations explicitly satisfy C-11, C-12, C-13 as design intentions — not as emergent properties. The variations differ in HOW they deliver those patterns, not WHETHER.

---

## V-01: Role Sequence

**Axis:** Role sequence — four canonical investigator roles are enumerated before any task
definition, so the model draws from a named set when assigning signal ownership.
**Hypothesis:** Anchoring PM / Engineer / Designer / Researcher at the top of the prompt
primes the model to differentiate ownership before it sees the signal table. C-08 failures
(all signals defaulting to one role) occur when role assignment is an afterthought; making
roles a named pre-condition eliminates that failure surface.

```
You are running /topic:new.

---

ROLES

Four owner roles anchor this investigation. Every signal in the plan belongs to
one of these roles — or another role you add explicitly if the signal type demands it:

  PM           sets scope; defines what decision this investigation must support
  Engineer     assesses feasibility; traces state machines, data flows, contracts
  Designer     reviews user impact; evaluates flow and experience signals
  Researcher   proves hypotheses; synthesizes findings; publishes intelligence

Assign roles deliberately. A plan where every signal defaults to a single role has
not been thought through — it does not tell the reader who does the work.

---

STEP 1 — COLLECT INPUT

Read from the user's invocation:
  topic:       short slug, no spaces (e.g., atlas, frogs, sync)
  description: one sentence describing the feature under investigation
  target:      what decision this investigation must inform

If topic or description is missing, ask once and wait before proceeding.

---

STEP 2 — REGISTER

Open simulations/TOPICS.md. Create if absent.
Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 3 — BUILD SIGNAL PLAN

Determine which signals this topic needs. Use the ROLES table above to assign
ownership to each signal. Every signal gets five fields — no blank cells:

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| (scout/draft/review/flow/trace/prove/listen/program/topic) | {skill} | {topic}-{slug}-{today}.md | (PM/Engineer/Designer/Researcher/other) | (essential/recommended/optional) |

Priority — exactly three values, nothing else:
  essential     — required before design commit; its absence blocks the gate
  recommended   — deepens confidence; not blocking
  optional      — pursue only if time permits

Using high, medium, low, required, P1, or any other value makes the strategy
invalid as a commit gate. The downstream scoring will reject it.

Before moving to STEP 4, verify all five checks:
  [ ] At least one signal is marked essential
  [ ] At least 2 distinct namespaces appear in the Namespace column
  [ ] At least 2 distinct roles appear in the Owner role column
  [ ] Every cell in every row is filled
  [ ] Every priority value is essential, recommended, or optional — nothing else

Do not proceed to STEP 4 until all five checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md with this structure:

## Rationale

[2-4 sentences: why does this topic need investigation before design commit?
What decision does it inform? What is the cost of committing without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate

Design commit is permitted when: [explicit minimum signal set].

## Naming Reference

All item names in this plan follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 5 — CONFIRM

Print to terminal:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential signals: {count}
  Owner roles used: {list}
  Namespaces covered: {list}
```

---

## V-02: Inertia Framing

**Axis:** Inertia framing — opens with the failure scenario (team commits to design without
investigation) and frames the skill as the prevention mechanism. The commit gate becomes the
skill's existential purpose, not an optional output.
**Hypothesis:** When the failure mode is stated before the task, the model generates a commit
gate that references real operational conditions rather than a generic "gather enough evidence"
sentence. Inertia framing elevates C-09 from a section to fill in to a problem to prevent.

```
You are running /topic:new.

---

WHY THIS SKILL EXISTS

Teams commit to designs without evidence. They assume requirements are stable, that
users want what PMs describe, that the architecture will hold under production load.
These assumptions fail. The investigation strategy is the plan that tests whether
those assumptions are safe before the team is too far committed to reverse.

This skill produces that plan. The commit gate it defines is the threshold the team
must clear before design decisions are locked.

---

STEP 1 — COLLECT INPUT

Read from the user's invocation:
  topic:       short slug, no spaces (e.g., atlas, vault, sync)
  description: one sentence — what feature is under investigation?
  target:      what decision will this investigation unlock?

If topic or description is missing, ask once and wait.

---

STEP 2 — REGISTER

Open simulations/TOPICS.md. Create it if absent.
Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 3 — PLAN SIGNALS

An investigation that covers only one namespace is blind to the full risk surface.
An investigation with no essential signals has no defined commit gate — the team
can always say "good enough" without a testable condition.

Plan the signals. Every row fills every column:

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| (scout/draft/review/flow/trace/prove/listen/program/topic) | {skill} | {topic}-{slug}-{today}.md | (PM/developer/architect/designer/researcher/other) | ??? |

Priority — three values only:
  essential     — blocks design commit; absent = gate cannot close
  recommended   — improves confidence; not blocking
  optional      — useful if time permits

Any other value (high, medium, low, required, P1, critical, nice-to-have) makes
this strategy invalid as a commit gate. The team will have no enforceable threshold,
and the investigation becomes advisory rather than gating.

Coverage check before writing the file:
  [ ] At least one signal is essential — if zero, the gate never closes (invalid plan)
  [ ] At least 2 distinct namespaces represented — single-namespace plans are incomplete
  [ ] At least 2 distinct owner roles represented — single-role plans are undistributed
  [ ] Every row fills all five columns — incomplete rows are unusable signal references

Do not write the strategy file until all four checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Rationale

[2-4 sentences: what is the default path if this investigation does not happen?
What assumptions is the team currently relying on? What decision does this
investigation produce? What does the team lose if those assumptions prove false?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate

Design commit is permitted when: [state the minimum signal set explicitly].

The gate is a condition. It can pass or fail. "Enough evidence" is not a gate.
Example: "All essential signals gathered AND at least 2 recommended signals gathered."

## Naming Reference

All item names follow this convention: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 5 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential signals: {count}
  Total signals: {count}
  Gate: {one-line statement from the Commit Gate section}
```

---

## V-03: Extreme Compression

**Axis:** Phrasing register (extreme brevity) — all 13 criteria present in the shortest
possible form. Tests whether structural patterns (checkbox-gate, operational consequence,
dedicated sections) require length to function, or whether structure is the mechanism
independent of word count.
**Hypothesis:** A prompt under 60 lines can satisfy all 13 criteria if every line earns its
place. C-11, C-12, C-13 can be satisfied with a single sentence each. If V-03 scores 100,
length is not what makes R1 V-05 reliable — structure is.

```
You are running /topic:new. Two artifacts: TOPICS.md entry + simulations/{topic}/strategy.md.

---

INPUT — collect before writing anything:
  topic:       slug, no spaces
  description: one line
  target:      what decision this informs (infer from description if not given, then confirm)

---

ARTIFACT 1 — simulations/TOPICS.md
Append: | {topic} | {description} | {today} | active |

---

ARTIFACT 2 — simulations/{topic}/strategy.md

### Rationale
2-4 sentences: why investigate? what decision? cost of skipping?

### Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Rules:
- Namespace: one of scout/draft/review/flow/trace/prove/listen/program/topic
- Item name: {topic}-{slug}-{today}.md (see Naming Reference below)
- Priority: essential / recommended / optional ONLY
  Using high/medium/low/P1/required/critical invalidates the strategy as a commit gate.
  The downstream system will not accept it.

Pre-write check:
  [ ] >=1 signal is essential — zero essential = no commit gate = invalid
  [ ] >=2 namespaces — single namespace leaves the investigation incomplete
  [ ] >=2 owner roles — all one role means no real distribution plan
  [ ] All cells filled

Do not write the file until all boxes pass.

### Commit Gate
Design commit is permitted when: [minimum signal set, stated as a condition].

### Naming Reference
Format: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

OUTPUT
  Topic: {topic} | Strategy: simulations/{topic}/strategy.md | Essential: {count} / Total: {count}
```

---

## V-04: Role Sequence + Inertia Framing

**Axes:** Role sequence + inertia framing. Opens with "who is at risk if this design is
wrong?" — naming the stakeholders at risk (inertia framing) — then maps from those
people to who should own each signal (role sequence). The combination should make C-07
(narrative rationale) and C-08 (differentiated roles) emerge naturally from the prompt
structure without requiring hard-coded coverage rules.
**Hypothesis:** Starting from stakeholder risk produces more differentiated owner
assignments than starting from a task list. When the model must ask "who carries this
risk?" for each signal, it naturally picks different roles for different signal types.

```
You are running /topic:new.

---

WHO IS AT RISK?

Before designing a feature, ask: who gets hurt if the design is wrong?

  PM / Product owner    — makes commitments to stakeholders based on this design
  Engineer / Architect  — builds what the design specifies; inherits its assumptions
  Designer / UX         — shapes the user experience; depends on the design holding
  Researcher / Analyst  — interprets results; needs the design to have been testable

A signal plan distributes investigation across these roles so no single perspective
carries the full risk. Assign signals deliberately — an investigation where every
signal belongs to one role is not a plan, it is a single person's opinion.

---

STEP 1 — COLLECT

Read from the user's invocation:
  topic:       slug, no spaces (e.g., onboarding, sync, atlas)
  description: one sentence — what feature is under investigation?
  target:      what decision will this investigation unlock?

If topic or description is missing, ask once and wait.

---

STEP 2 — REGISTER

Open simulations/TOPICS.md. Create if absent.
Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 3 — BUILD SIGNAL PLAN

For each signal the investigation needs, determine:
  1. Who from the ROLES table above should gather it?
  2. What namespace does it belong to?
  3. What skill produces the artifact?
  4. What is the artifact name?
  5. How critical is it to design commit?

Fill the table. No blank cells. Assign roles from the four categories above, adding
others (SRE, compliance, marketing) where the signal type demands it.

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| (scout/draft/review/flow/trace/prove/listen/program/topic) | {skill} | {topic}-{slug}-{today}.md | (role from categories above) | (essential/recommended/optional) |

Priority values — three only:
  essential     — the gate cannot close without this signal
  recommended   — improves confidence; not blocking
  optional      — only if time permits

Substituting high/medium/low or any other value breaks the commit gate logic.
The strategy will be treated as advisory, not gating, and the team loses the
ability to enforce a clear threshold before design commit.

Coverage gate — check before writing:
  [ ] At least one signal marked essential
  [ ] At least 2 distinct namespaces represented
  [ ] At least 2 distinct roles from the ROLES categories above
  [ ] Every cell in every row is filled
  [ ] Every priority is essential, recommended, or optional — no substitutes

Do not proceed to STEP 4 until all five checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Rationale

[2-4 sentences: which stakeholders are at risk if this design is wrong? What
assumption is the team currently relying on? What decision does this investigation
produce? What does the team lose if they commit without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate

Design commit is permitted when: [explicit minimum signal set].

Write this as a condition that can be tested. Not: "enough evidence gathered."
Correct: "All essential signals gathered AND at least 1 recommended signal gathered."

## Naming Reference

All item names follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 5 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential: {count}  Recommended: {count}  Optional: {count}
  Owner roles: {list}
  Namespaces: {list}
```

---

## V-05: Operational Consequence Throughout

**Axes:** Inertia framing + operational consequence applied to every constraint. Every
field rule and coverage requirement includes its downstream-failure consequence — not just
the priority vocabulary (C-12), but namespace validity, item naming, owner assignment,
and coverage requirements. The inertia frame is set once at the top, then each rule
carries its own "what breaks" sentence.
**Hypothesis:** When every rule has a "what breaks downstream" attached, the model
internalizes the intent rather than following rules by rote. A model that understands
WHY each field matters will produce better-formed strategies across diverse topics than
one that has memorized a validation checklist. This is the highest-coverage variation
on the consequence-framing axis.

```
You are running /topic:new.

The purpose of this skill is to prevent a team from committing to a design without
knowing what they are committing to. The two artifacts it produces are the evidence
that the team ran a structured investigation before locking decisions.

---

STEP 1 — COLLECT INPUT

Read from the user's invocation:
  topic:       short slug, no spaces
  description: one sentence — what feature is under investigation?
  target:      what decision does this investigation enable?

Why it matters: a strategy without a clear target cannot be declared complete.
The team will not know when they have gathered enough.

If topic or description is missing, ask once and wait before proceeding.

---

STEP 2 — REGISTER IN TOPICS.md

Open simulations/TOPICS.md. Create it if absent.
Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

Why it matters: without a TOPICS.md entry, the topic is invisible to the registry.
Other investigators cannot discover it or link their work to it.

---

STEP 3 — PLAN SIGNALS

Determine the signals this topic needs. For each signal, fill all five fields:

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| (scout/draft/review/flow/trace/prove/listen/program/topic) | {skill} | {topic}-{slug}-{today}.md | (PM/developer/architect/designer/researcher/SRE/other) | (essential/recommended/optional) |

FIELD RULES — each with its operational consequence:

Namespace — must be one of the nine listed above. Using an unknown namespace means
  the signal will not be found by the skill runner that processes this strategy.

Item name — must follow {topic}-{slug}-{date}.md. Any other format means the artifact
  will not match the registry lookup pattern and will be ignored by downstream skills.

Owner role — must be a real role. Using a generic placeholder like "team" means no
  individual is accountable, and the signal may never actually be gathered.

Priority — exactly one of three values:
  essential     — blocks design commit; the gate cannot close without it
  recommended   — adds confidence; does not block commit
  optional      — only if time permits

Using high/medium/low/required/P1/critical or any other value for priority makes
this strategy invalid as a commit gate. The downstream system will treat the
strategy as advisory-only, and the team loses the ability to hold the design commit.

COVERAGE REQUIREMENTS — each with its consequence:

At least one essential: if no signal is marked essential, the commit gate has no
  blocking conditions. The investigation can always be declared done. This invalidates
  the strategy as a decision gate.

At least 2 namespaces: if only one namespace is covered, the investigation is blind
  to signals from other dimensions (e.g., technical feasibility without user research).

At least 2 owner roles: if all signals belong to one role, cross-functional coverage
  is absent and the risk of unchallenged assumptions is high.

All cells filled: a row with a blank cell cannot be assigned, tracked, or scored.
  It is a placeholder, not a signal.

Coverage gate — verify before writing the strategy file:
  [ ] At least one signal is essential
  [ ] At least 2 distinct namespaces
  [ ] At least 2 distinct owner roles
  [ ] Every cell in every row is filled
  [ ] Every priority value is essential, recommended, or optional — no others

Do not write the strategy file until all five checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Rationale

[2-4 sentences: what is the team currently assuming? What decision does this
investigation produce? What is the cost of committing to a design without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate

Design commit is permitted when: [state the minimum signal set as a condition].

The gate must be testable. "Enough signals" is not a condition.
"All essential signals gathered AND at least 2 recommended" is a condition.
If this section is left implicit, the investigation has no enforceable threshold.

## Naming Reference

All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

Artifact names that do not follow this convention will not match the lookup
pattern used by downstream skills and will not be found.

---

STEP 5 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement}
```
