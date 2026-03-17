# /quest:variate — mock-all Round 11

**Skill:** mock-all | **Rubric:** v11 | **Criteria count:** 17 (C-01 through C-25 active)

**Variation axes selected:**
- **Single-axis A:** Phrasing register (occupancy-language vs being-language) — directly tests C-24/C-25
- **Single-axis B:** Role sequence (one global role block vs per-namespace activation) — tests C-23 (affirmation at each activation)
- **Single-axis C:** Output format (prose artifact bodies vs structured field tables) — tests artifact body semantics
- **Combinations:** A+B (being-language × per-namespace), B+C (per-namespace × inertia-grounded tables)

---

## V-01

**Variation axis:** Phrasing register — occupancy-language baseline
**Hypothesis:** Descriptive "In the X role, your task is…" phrasing feels natural and complete but fails C-25 (occupancy, not being) and likely C-24 (role description precedes affirmation). Establishes the diagnostic floor.

---

```
# /mock:all {topic}

Produce a complete synthetic signal coverage pass for topic **{topic}** across all
9 Signal namespaces. One mock artifact per namespace. Order: scout → draft → review
→ flow → trace → prove → listen → program → topic.

---

## Operational Roles

This skill runs three roles in sequence across the namespace pass.

**In the CLASSIFIER role**, your task is to assign the correct category to each
namespace from the taxonomy: HIGH-STRUCTURE (scout, draft, review, flow, trace),
EVIDENCE-HEAVY (prove-*, listen-*), MIXED (program, topic).

**In the ARTIFACT WRITER role**, your task is to produce a realistic 150–250 word
mock artifact body for each namespace. Content should be plausible first-pass signal
for a team evaluating whether to build {topic}. Ground each artifact in the topic.

**In the COVERAGE ANALYST role**, your task is to produce the final coverage summary
table listing all nine namespaces with their category, any flags, and a recommended
next step.

---

## Compliance Pre-Check

Before generating artifacts, evaluate {topic} for compliance sensitivity.
If {topic} involves user data, permissions, access control, or regulated domains:
- Pre-flag `scout-compliance` REAL-REQUIRED
- Pre-flag `trace-permissions` REAL-REQUIRED
These flags apply regardless of structural quality of the mock artifact.

---

## Tier Pre-Check

The following namespaces are Tier 2/3 critical and must be flagged TIER-CRITICAL
in the coverage summary: `trace`, `scout-feasibility`, `listen`.

---

## Namespace Pass

For each namespace, emit the section exactly as shown. Replace bracketed
placeholders with content grounded in {topic}.

---

### 1. scout

In the CLASSIFIER role, assign: HIGH-STRUCTURE.
In the ARTIFACT WRITER role, generate:

---
MOCK ARTIFACT
Skill: scout-competitors
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[150–250 words. Identify 3–4 competitive analogues or direct competitors.
Describe each competitor's positioning, key capability, and one weakness.
Conclude with one exploitable gap {topic} could address.]

---

### 2. draft

In the CLASSIFIER role, assign: HIGH-STRUCTURE.
In the ARTIFACT WRITER role, generate:

---
MOCK ARTIFACT
Skill: draft-spec
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[150–250 words. State the problem being solved. Describe the proposed interface
or API surface at a high level. Identify one open question the spec has not resolved.]

---

### 3. review

In the CLASSIFIER role, assign: HIGH-STRUCTURE.
In the ARTIFACT WRITER role, generate:

---
MOCK ARTIFACT
Skill: review-design
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[150–250 words. Present one structural concern about the design. State one
approval condition that must be met before the design can advance. Assign a
preliminary confidence rating (Low / Medium / High).]

---

### 4. flow

In the CLASSIFIER role, assign: HIGH-STRUCTURE.
In the ARTIFACT WRITER role, generate:

---
MOCK ARTIFACT
Skill: flow-conversation
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[150–250 words. Walk the happy-path conversation for {topic}. Identify one
edge case that breaks the path. Note how the system should recover.]

---

### 5. trace

In the CLASSIFIER role, assign: HIGH-STRUCTURE.
In the ARTIFACT WRITER role, generate:

Note: trace is Tier 2/3 critical — flag TIER-CRITICAL in coverage summary.

---
MOCK ARTIFACT
Skill: trace-component
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[150–250 words. Name the component being traced. Describe entry state, one
primary operation with inputs and outputs, and the expected exit state.
Identify one invariant that must hold throughout.]

---

### 6. prove

In the CLASSIFIER role, assign: EVIDENCE-HEAVY.
In the ARTIFACT WRITER role, generate:

**REAL-REQUIRED** — prove-* sections require real execution evidence.
This mock artifact is a structural scaffold only; do not treat it as signal.

---
MOCK ARTIFACT
Skill: prove-interview
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

[150–250 words. Include one synthetic user quote. Identify one friction point
the interview would surface. State one adoption signal a positive interview
would confirm.]

---

### 7. listen

In the CLASSIFIER role, assign: EVIDENCE-HEAVY.
In the ARTIFACT WRITER role, generate:

**REAL-REQUIRED** — listen-* sections require real user feedback signals.
This mock artifact is a structural scaffold only; do not treat it as signal.

Note: listen is Tier 2/3 critical — flag TIER-CRITICAL in coverage summary.

---
MOCK ARTIFACT
Skill: listen-adoption
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

[150–250 words. Describe one early-adopter signal pattern that would confirm
pull. Describe one resistance pattern that would indicate friction. State what
a positive adoption read would look like at 30 days.]

---

### 8. program

In the CLASSIFIER role, assign: MIXED.
In the ARTIFACT WRITER role, generate:

---
MOCK ARTIFACT
Skill: program-plan
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

[150–250 words. Outline a 3-phase delivery structure. Name one cross-team
dependency. State the milestone that gates Phase 1 exit.]

---

### 9. topic

In the CLASSIFIER role, assign: MIXED.
In the ARTIFACT WRITER role, generate:

---
MOCK ARTIFACT
Skill: topic-story
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

[150–250 words. Narrate the arc from problem to signal to decision. State one
readiness indicator that would tell the team they have enough signal to commit.]

---

## Coverage Summary

In the COVERAGE ANALYST role, produce the following table. Fill each Flag cell
using: REAL-REQUIRED, TIER-CRITICAL, COMPLIANCE-REQUIRED, or leave blank.
Fill Recommended next step with a concrete action (not a category label).

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
| scout | HIGH-STRUCTURE | | |
| draft | HIGH-STRUCTURE | | |
| review | HIGH-STRUCTURE | | |
| flow | HIGH-STRUCTURE | | |
| trace | HIGH-STRUCTURE | TIER-CRITICAL | |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED, TIER-CRITICAL | |
| program | MIXED | | |
| topic | MIXED | | |

---

Next: /mock:review {topic} {this-file}
```

---

## V-02

**Variation axis:** Role sequence — per-namespace being-language activation (identity-first at every header)
**Hypothesis:** Placing "You ARE the X" as syntactically first element at each namespace activation — not once in a preamble — satisfies C-23 (affirmation at each activation), C-24 (affirmation syntactically first), and C-25 (being-language, not occupancy). Demonstrates the ceiling for the role/identity staircase.

---

```
# /mock:all {topic}

Produce a complete synthetic signal coverage pass for topic **{topic}** across all
9 Signal namespaces. One mock artifact per namespace. Order: scout → draft → review
→ flow → trace → prove → listen → program → topic.

---

## Role Inventory

Three roles execute across this pass. Each activates at the point of use — not
in a preamble. The identity header at each activation is the authoritative
activation; no preamble declaration substitutes for it.

- **CLASSIFIER** — assigns namespace category from the taxonomy
- **ARTIFACT WRITER** — generates the mock artifact body
- **COVERAGE ANALYST** — produces the final coverage summary table

---

## Category Taxonomy

- HIGH-STRUCTURE: scout, draft, review, flow, trace, program*, topic*
- EVIDENCE-HEAVY: prove-*, listen-*
- MIXED: program, topic (when artifact contains both structural and evidence elements)

*program and topic default HIGH-STRUCTURE; escalate to MIXED if artifact body
contains both structural scaffold and evidence content.

---

## Compliance Pre-Check

Before generating artifacts, evaluate {topic} for compliance sensitivity.
Topics touching user data, permissions, access control, or regulated domains
trigger mandatory pre-flagging:
- scout-compliance → REAL-REQUIRED
- trace-permissions → REAL-REQUIRED
These flags apply regardless of structural quality of the resulting mock artifact.

---

## Namespace Pass

---

### 1. scout

**You ARE the CLASSIFIER.** Generating artifact content while in the CLASSIFIER
role is an ontological contradiction — the CLASSIFIER has no artifact-writing
existence. Your sole output here is the category assignment.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** The CLASSIFIER no longer exists at this
activation. Your entire existence is the production of a realistic mock artifact
body for the scout namespace. Write 150–250 words of plausible competitor
intelligence for {topic}: 3–4 named analogues, their positioning, and one
exploitable gap.

---
MOCK ARTIFACT
Skill: scout-competitors
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 2. draft

**You ARE the CLASSIFIER.** Your sole output is the category assignment.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** Write 150–250 words: problem statement,
proposed interface at high level, and one unresolved open question.

---
MOCK ARTIFACT
Skill: draft-spec
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 3. review

**You ARE the CLASSIFIER.** Your sole output is the category assignment.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** Write 150–250 words: one structural design
concern, one approval condition, and a preliminary confidence rating.

---
MOCK ARTIFACT
Skill: review-design
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 4. flow

**You ARE the CLASSIFIER.** Your sole output is the category assignment.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** Write 150–250 words: happy-path walk,
one edge case, and recovery behavior.

---
MOCK ARTIFACT
Skill: flow-conversation
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 5. trace

**You ARE the CLASSIFIER.** Your sole output is the category assignment.
Note: trace is Tier 2/3 critical. You do not apply flags — that is COVERAGE
ANALYST work. Your output here is category only.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** Write 150–250 words: named component,
entry state, primary operation (inputs → outputs), exit state, one invariant.

---
MOCK ARTIFACT
Skill: trace-component
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 6. prove

**You ARE the CLASSIFIER.** Your sole output is the category assignment.

Category: EVIDENCE-HEAVY

---

**You ARE the ARTIFACT WRITER.** REAL-REQUIRED: prove-* sections require real
execution evidence. This artifact is structural scaffold only.

Write 150–250 words: one synthetic user quote, one friction point, one
adoption signal a positive interview would confirm.

---
MOCK ARTIFACT
Skill: prove-interview
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 7. listen

**You ARE the CLASSIFIER.** Your sole output is the category assignment.
Note: listen is Tier 2/3 critical. Category assignment only.

Category: EVIDENCE-HEAVY

---

**You ARE the ARTIFACT WRITER.** REAL-REQUIRED: listen-* sections require real
user feedback. This artifact is structural scaffold only.

Write 150–250 words: one early-adopter signal, one resistance pattern, what a
positive adoption read looks like at 30 days.

---
MOCK ARTIFACT
Skill: listen-adoption
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 8. program

**You ARE the CLASSIFIER.** Your sole output is the category assignment.

Category: MIXED

---

**You ARE the ARTIFACT WRITER.** Write 150–250 words: 3-phase delivery
structure, one cross-team dependency, milestone gating Phase 1 exit.

---
MOCK ARTIFACT
Skill: program-plan
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 9. topic

**You ARE the CLASSIFIER.** Your sole output is the category assignment.

Category: MIXED

---

**You ARE the ARTIFACT WRITER.** Write 150–250 words: arc from problem to
signal to decision, one readiness indicator that tells the team they have
enough signal to commit.

---
MOCK ARTIFACT
Skill: topic-story
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

[Artifact body]

---

## Coverage Summary

**You ARE the COVERAGE ANALYST.** The ARTIFACT WRITER no longer exists at this
activation. Your entire existence is the production of the coverage summary table.
Generating additional artifact content here is an ontological contradiction —
the COVERAGE ANALYST does not write artifacts.

Fill each Flag cell: REAL-REQUIRED, TIER-CRITICAL, COMPLIANCE-REQUIRED, or blank.
Fill Recommended next step with a concrete action.

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
| scout | HIGH-STRUCTURE | | |
| draft | HIGH-STRUCTURE | | |
| review | HIGH-STRUCTURE | | |
| flow | HIGH-STRUCTURE | | |
| trace | HIGH-STRUCTURE | TIER-CRITICAL | |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED, TIER-CRITICAL | |
| program | MIXED | | |
| topic | MIXED | | |

---

Next: /mock:review {topic} {this-file}
```

---

## V-03

**Variation axis:** Output format — structured field tables replace prose artifact bodies
**Hypothesis:** Tabular artifact bodies improve parsability and make field gaps machine-detectable, but may sacrifice the narrative depth expected in EVIDENCE-HEAVY namespaces. Tests whether format change affects C-02 category signal clarity and C-03 REAL-REQUIRED legibility.

---

```
# /mock:all {topic}

Produce a complete synthetic signal coverage pass for topic **{topic}** across all
9 Signal namespaces. One mock artifact per namespace. Order: scout → draft → review
→ flow → trace → prove → listen → program → topic.

---

## Roles

**You ARE the CLASSIFIER** when assigning namespace categories.
**You ARE the ARTIFACT WRITER** when producing artifact tables.
**You ARE the COVERAGE ANALYST** when producing the final summary table.

Do not mix roles within a single output block.

---

## Category Taxonomy

- HIGH-STRUCTURE: scout, draft, review, flow, trace
- EVIDENCE-HEAVY: prove-*, listen-*
- MIXED: program, topic

---

## Artifact Format

Each artifact uses a structured field table instead of prose. Fields vary by
namespace but always include: Skill, Topic, Category, Date, Status, plus
namespace-specific evidence fields (see below).

---

## Compliance Pre-Check

Evaluate {topic} before generating artifacts. If compliance-sensitive:
- Pre-flag `scout-compliance` REAL-REQUIRED
- Pre-flag `trace-permissions` REAL-REQUIRED

---

## Namespace Pass

---

### 1. scout

---
MOCK ARTIFACT
Skill: scout-competitors
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Competitor A | [Name + positioning in 1 sentence] |
| Competitor B | [Name + positioning in 1 sentence] |
| Competitor C | [Name + positioning in 1 sentence] |
| Key gap | [One exploitable gap {topic} addresses] |
| Confidence | Low / Medium / High |
| Signal quality | MOCK — no real research conducted |

---

### 2. draft

---
MOCK ARTIFACT
Skill: draft-spec
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Problem statement | [1–2 sentences] |
| Proposed interface | [High-level API or UX surface description] |
| Open question | [One unresolved design question] |
| Spec status | DRAFT — not reviewed |
| Signal quality | MOCK — no real spec work conducted |

---

### 3. review

---
MOCK ARTIFACT
Skill: review-design
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Structural concern | [One design concern] |
| Approval condition | [What must be true before design advances] |
| Reviewer confidence | Low / Medium / High |
| Review status | MOCK — no real review conducted |
| Signal quality | MOCK |

---

### 4. flow

---
MOCK ARTIFACT
Skill: flow-conversation
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Happy path | [Step 1 → Step 2 → Step 3] |
| Edge case | [One breakage scenario] |
| Recovery | [Expected recovery behavior] |
| Flow coverage | PARTIAL — happy path only |
| Signal quality | MOCK |

---

### 5. trace

**Note:** trace is Tier 2/3 critical — flag TIER-CRITICAL in coverage summary.

---
MOCK ARTIFACT
Skill: trace-component
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Component | [Named component] |
| Entry state | [Pre-condition] |
| Operation | [Input] → [Output] |
| Exit state | [Post-condition] |
| Invariant | [One invariant that must hold throughout] |
| Signal quality | MOCK |

---

### 6. prove

**REAL-REQUIRED** — prove-* artifacts require real execution evidence.
This table is a structural scaffold only. Do not treat fields as signal.

---
MOCK ARTIFACT
Skill: prove-interview
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Synthetic quote | "[Plausible user quote for {topic}]" |
| Friction point | [One pain point the interview would surface] |
| Adoption signal | [What a positive interview confirms] |
| Evidence status | REAL-REQUIRED — conduct actual interviews |
| Signal quality | MOCK — no real interviews conducted |

---

### 7. listen

**REAL-REQUIRED** — listen-* artifacts require real user feedback.
**Note:** listen is Tier 2/3 critical — flag TIER-CRITICAL in coverage summary.

---
MOCK ARTIFACT
Skill: listen-adoption
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Early-adopter signal | [Pattern indicating pull] |
| Resistance pattern | [Pattern indicating friction] |
| 30-day read | [What positive adoption looks like at 30 days] |
| Evidence status | REAL-REQUIRED — deploy adoption survey |
| Signal quality | MOCK — no real feedback collected |

---

### 8. program

---
MOCK ARTIFACT
Skill: program-plan
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Phase 1 | [Name + scope] |
| Phase 2 | [Name + scope] |
| Phase 3 | [Name + scope] |
| Cross-team dependency | [One named dependency] |
| Phase 1 gate | [Milestone that closes Phase 1] |
| Signal quality | MOCK |

---

### 9. topic

---
MOCK ARTIFACT
Skill: topic-story
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

| Field | Value |
|-------|-------|
| Problem framing | [1 sentence] |
| Signal arc | [How signals accumulate toward a decision] |
| Readiness indicator | [One condition that means the team has enough signal] |
| Current signal count | MOCK — 0 real signals; 9 mock scaffolds |
| Signal quality | MOCK |

---

## Coverage Summary

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
| scout | HIGH-STRUCTURE | | Run scout-competitors with real market research |
| draft | HIGH-STRUCTURE | | Promote mock spec to draft-spec with real author |
| review | HIGH-STRUCTURE | | Schedule design review with named reviewer |
| flow | HIGH-STRUCTURE | | Run flow-conversation with real scenario inputs |
| trace | HIGH-STRUCTURE | TIER-CRITICAL | Execute trace-component against real implementation |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | Conduct 3–5 user interviews; replace mock quotes |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED, TIER-CRITICAL | Deploy listen-adoption instrument; collect real signals |
| program | MIXED | | Validate phases with engineering lead |
| topic | MIXED | | Re-run topic-story after first 3 real signals land |

---

Next: /mock:review {topic} {this-file}
```

---

## V-04

**Variation axes (combined):** Being-language × Lifecycle emphasis
**Hypothesis:** Pairing identity-first role headers with explicit phase gates (PHASE 1: CLASSIFY → PHASE 2: WRITE → PHASE 3: ASSESS) reduces inter-namespace drift — each namespace restart re-anchors both the role identity and the phase position. Addresses C-23/C-24/C-25 while also improving structural legibility when the output is long.

---

```
# /mock:all {topic}

Produce a complete synthetic signal coverage pass for topic **{topic}** across all
9 Signal namespaces. One mock artifact per namespace. Order: scout → draft → review
→ flow → trace → prove → listen → program → topic.

---

## Lifecycle Structure

Each namespace section executes three phases in strict sequence:

**PHASE 1 — CLASSIFY**: Assign the correct category. Output only.
**PHASE 2 — WRITE**: Produce the mock artifact body. Output only.
**PHASE 3 — ASSESS** (trace, prove, listen only): Apply tier and evidence flags.

Phase transitions are hard boundaries. Content from one phase must not appear
in another phase's output block.

---

## Roles (activated per phase, per namespace)

**You ARE the CLASSIFIER** during PHASE 1 of each namespace.
**You ARE the ARTIFACT WRITER** during PHASE 2 of each namespace.
**You ARE the FLAG ASSESSOR** during PHASE 3 of each namespace (where applicable).

Each role activation begins with its being-statement as the syntactically first
element of the block. Role identity at activation is not a description of what
you are doing — it is what you are.

---

## Category Taxonomy

- HIGH-STRUCTURE: scout, draft, review, flow, trace
- EVIDENCE-HEAVY: prove-*, listen-*
- MIXED: program, topic

---

## Compliance Pre-Check

Before entering the namespace pass, evaluate {topic}:
- Compliance-sensitive topics → pre-flag scout-compliance and trace-permissions REAL-REQUIRED.
- This pre-check executes outside all three phases and outside all role activations.

---

## Namespace Pass

---

### 1. scout

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Assigning category is the totality of your existence
in this phase. Generating artifact content here is an ontological contradiction —
the CLASSIFIER has no artifact body to produce.

Category: HIGH-STRUCTURE

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** The CLASSIFIER no longer exists. Your sole
output is the mock artifact body below: 150–250 words of realistic competitor
intelligence for {topic}. Include 3–4 named analogues, their positioning, and
one gap {topic} exploits.

---
MOCK ARTIFACT
Skill: scout-competitors
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 2. draft

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: problem statement, proposed
interface surface, one unresolved open question.

---
MOCK ARTIFACT
Skill: draft-spec
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 3. review

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: one structural concern,
one approval condition, preliminary confidence rating.

---
MOCK ARTIFACT
Skill: review-design
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 4. flow

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: happy-path walk, one edge
case, recovery behavior.

---
MOCK ARTIFACT
Skill: flow-conversation
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 5. trace

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only. Tier status is assessed
in PHASE 3, not here.

Category: HIGH-STRUCTURE

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: named component, entry state,
primary operation (inputs → outputs), exit state, one invariant.

---
MOCK ARTIFACT
Skill: trace-component
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

[Artifact body]

#### PHASE 3 — ASSESS

**You ARE the FLAG ASSESSOR.** The ARTIFACT WRITER no longer exists. Your output
is the tier flag only.

TIER-CRITICAL: trace is a Tier 2/3 critical namespace.
Recommended: Execute against a real implementation artifact before committing.

---

### 6. prove

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: EVIDENCE-HEAVY

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: one synthetic user quote, one
friction point, one adoption signal a positive interview would confirm.

**REAL-REQUIRED** — prove-* artifacts require real execution evidence.
This body is structural scaffold only.

---
MOCK ARTIFACT
Skill: prove-interview
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

[Artifact body]

#### PHASE 3 — ASSESS

**You ARE the FLAG ASSESSOR.**

REAL-REQUIRED: prove-interview requires real user interviews.
Recommended: Conduct 3–5 interviews with target users; retire this mock.

---

### 7. listen

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: EVIDENCE-HEAVY

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: one early-adopter signal,
one resistance pattern, what positive adoption looks like at 30 days.

**REAL-REQUIRED** — listen-* artifacts require real user feedback.
This body is structural scaffold only.

---
MOCK ARTIFACT
Skill: listen-adoption
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

[Artifact body]

#### PHASE 3 — ASSESS

**You ARE the FLAG ASSESSOR.**

REAL-REQUIRED: listen-adoption requires real feedback collection.
TIER-CRITICAL: listen is a Tier 2/3 critical namespace.
Recommended: Deploy adoption instrument and collect signals before committing.

---

### 8. program

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: MIXED

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: 3-phase delivery structure,
one cross-team dependency, milestone gating Phase 1 exit.

---
MOCK ARTIFACT
Skill: program-plan
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

[Artifact body]

---

### 9. topic

#### PHASE 1 — CLASSIFY

**You ARE the CLASSIFIER.** Category assignment only.

Category: MIXED

#### PHASE 2 — WRITE

**You ARE the ARTIFACT WRITER.** 150–250 words: arc from problem to signal
to decision, one readiness indicator for commit confidence.

---
MOCK ARTIFACT
Skill: topic-story
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

[Artifact body]

---

## Coverage Summary

**You ARE the COVERAGE ANALYST.** PHASE 1 and PHASE 2 roles no longer exist.
Your output is the summary table only. Generating artifact content here is an
ontological contradiction — the COVERAGE ANALYST exists to assess, not to write.

Fill Flag: REAL-REQUIRED, TIER-CRITICAL, COMPLIANCE-REQUIRED, or blank.
Fill Recommended next step with a concrete action.

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
| scout | HIGH-STRUCTURE | | |
| draft | HIGH-STRUCTURE | | |
| review | HIGH-STRUCTURE | | |
| flow | HIGH-STRUCTURE | | |
| trace | HIGH-STRUCTURE | TIER-CRITICAL | |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED, TIER-CRITICAL | |
| program | MIXED | | |
| topic | MIXED | | |

---

Next: /mock:review {topic} {this-file}
```

---

## V-05

**Variation axes (combined):** Being-language × Inertia framing
**Hypothesis:** Naming the inertia artifact explicitly in each namespace body — what a team currently does instead of gathering this signal, and what the cost of that inertia is — grounds each mock artifact in realistic decision context, raises signal density, and tests whether inertia framing interacts with C-02 category correctness (does inertia prose get miscategorized as EVIDENCE-HEAVY?). Satisfies C-24/C-25 while testing the depth anchor criterion.

---

```
# /mock:all {topic}

Produce a complete synthetic signal coverage pass for topic **{topic}** across all
9 Signal namespaces. One mock artifact per namespace. Order: scout → draft → review
→ flow → trace → prove → listen → program → topic.

Each artifact body opens with an **Inertia block**: what the team currently does
instead of gathering this signal, and what commitment decision that produces.
The inertia block is part of the artifact body — it is not a separate section.

---

## Roles

**You ARE the CLASSIFIER** when assigning namespace categories.
**You ARE the ARTIFACT WRITER** when producing artifact bodies.
**You ARE the COVERAGE ANALYST** when producing the final summary table.

At each namespace, the CLASSIFIER activates first, then the ARTIFACT WRITER.
The being-statement is the syntactically first element of each activation block.
A role description that names what you are doing before naming what you are
violates the identity contract — do not do this.

---

## Category Taxonomy

- HIGH-STRUCTURE: scout, draft, review, flow, trace
- EVIDENCE-HEAVY: prove-*, listen-*
- MIXED: program, topic

---

## Inertia Block Format (required in every artifact body)

> **Inertia:** [What the team does today instead of running this namespace skill —
> 1 sentence.] **Inertia cost:** [What decision this produces — 1 sentence.]

Place this block as the first paragraph of every artifact body, before any
other content.

---

## Compliance Pre-Check

Evaluate {topic} before generating artifacts. Compliance-sensitive topics
(user data, permissions, access control, regulated domains):
- Pre-flag scout-compliance REAL-REQUIRED
- Pre-flag trace-permissions REAL-REQUIRED

---

## Namespace Pass

---

### 1. scout

**You ARE the CLASSIFIER.** Category assignment is your complete output here.
Generating artifact content is an ontological contradiction at this activation.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** Produce a 200–280 word artifact body for
scout-competitors. Open with the Inertia block. Then: 3–4 named analogues,
positioning, one exploitable gap.

---
MOCK ARTIFACT
Skill: scout-competitors
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

> **Inertia:** Team relies on informal awareness of 1–2 tools mentioned in
> recent meetings. **Inertia cost:** Commits to a feature space already
> saturated by a competitor with 18 months of head start.

[Remaining artifact body — competitor intelligence grounded in {topic}]

---

### 2. draft

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: problem statement, proposed interface, one unresolved open question.

---
MOCK ARTIFACT
Skill: draft-spec
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

> **Inertia:** Team writes a ticket with acceptance criteria instead of a spec.
> **Inertia cost:** Interface ambiguity surfaces in code review, not design.

[Remaining artifact body]

---

### 3. review

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: one structural concern, one approval condition, confidence rating.

---
MOCK ARTIFACT
Skill: review-design
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

> **Inertia:** Design is reviewed informally in standup rather than a structured
> review. **Inertia cost:** Structural concerns emerge post-implementation when
> cost of change is highest.

[Remaining artifact body]

---

### 4. flow

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: happy path, one edge case, recovery behavior.

---
MOCK ARTIFACT
Skill: flow-conversation
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

> **Inertia:** Team mentally walks the happy path without simulating edge cases.
> **Inertia cost:** Edge case handling is designed under production pressure
> rather than upfront.

[Remaining artifact body]

---

### 5. trace

**You ARE the CLASSIFIER.** Category assignment only.

Category: HIGH-STRUCTURE

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: named component, entry state, operation (inputs → outputs), exit state,
one invariant. Note: trace is Tier 2/3 critical — note this in the artifact
body, not as a separate flag block.

---
MOCK ARTIFACT
Skill: trace-component
Topic: {topic}
Category: HIGH-STRUCTURE
Date: {date}
Status: MOCK
---

> **Inertia:** Component behavior is inferred from reading the implementation
> rather than traced from spec. **Inertia cost:** Behavioral assumptions diverge
> silently across team members until a production bug forces reconciliation.

[Remaining artifact body. Note inline: TIER-CRITICAL namespace — real trace
required before implementation is considered stable.]

---

### 6. prove

**You ARE the CLASSIFIER.** Category assignment only.

Category: EVIDENCE-HEAVY

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: one synthetic user quote, one friction point, one adoption signal.
REAL-REQUIRED applies — this is structural scaffold only.

---
MOCK ARTIFACT
Skill: prove-interview
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

**REAL-REQUIRED** — prove-* requires real execution evidence.

> **Inertia:** Team assumes they know user pain from support tickets rather than
> interviews. **Inertia cost:** Features are built to resolve the loudest tickets,
> not the highest-frequency silent friction.

[Remaining artifact body with synthetic quote, friction point, adoption signal]

---

### 7. listen

**You ARE the CLASSIFIER.** Category assignment only.

Category: EVIDENCE-HEAVY

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: early-adopter signal, resistance pattern, 30-day adoption read.
REAL-REQUIRED applies — this is structural scaffold only.
Note: listen is Tier 2/3 critical.

---
MOCK ARTIFACT
Skill: listen-adoption
Topic: {topic}
Category: EVIDENCE-HEAVY
Date: {date}
Status: MOCK
---

**REAL-REQUIRED** — listen-* requires real user feedback.

> **Inertia:** Team monitors NPS and support volume as adoption proxies.
> **Inertia cost:** NPS conflates satisfaction with breadth of use; teams
> mistake silence for adoption and ship without a pull signal.

[Remaining artifact body. Note inline: TIER-CRITICAL — real listen signal
required before adoption assumptions drive roadmap decisions.]

---

### 8. program

**You ARE the CLASSIFIER.** Category assignment only.

Category: MIXED

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: 3-phase delivery structure, one cross-team dependency, Phase 1 gate.

---
MOCK ARTIFACT
Skill: program-plan
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

> **Inertia:** Team writes a roadmap slide rather than a phased program plan.
> **Inertia cost:** Phase dependencies and cross-team blockers are discovered
> at the start of each phase rather than planned across the full arc.

[Remaining artifact body]

---

### 9. topic

**You ARE the CLASSIFIER.** Category assignment only.

Category: MIXED

---

**You ARE the ARTIFACT WRITER.** 200–280 words. Open with Inertia block.
Then: problem-to-signal-to-decision arc, one readiness indicator.

---
MOCK ARTIFACT
Skill: topic-story
Topic: {topic}
Category: MIXED
Date: {date}
Status: MOCK
---

> **Inertia:** Team treats the topic as decided once a PM has written a PRD.
> **Inertia cost:** Commitment happens before signal accumulation; pivots cost
> 3–5x more than upfront signal gathering would have.

[Remaining artifact body — signal arc, readiness indicator]

---

## Coverage Summary

**You ARE the COVERAGE ANALYST.** The ARTIFACT WRITER no longer exists.
Your output is the summary table only. Producing additional artifact content
here is an ontological contradiction — the COVERAGE ANALYST does not write,
it assesses.

Fill Flag: REAL-REQUIRED, TIER-CRITICAL, COMPLIANCE-REQUIRED, or blank.
Recommended next step must be a concrete action, not a category label.

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
| scout | HIGH-STRUCTURE | | Name 3 real competitors; replace mock intelligence |
| draft | HIGH-STRUCTURE | | Assign spec owner; promote mock to real draft-spec |
| review | HIGH-STRUCTURE | | Schedule structured design review with named reviewer |
| flow | HIGH-STRUCTURE | | Run flow-conversation with real scenario inputs |
| trace | HIGH-STRUCTURE | TIER-CRITICAL | Execute trace-component against real implementation |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | Conduct 3–5 real interviews; retire synthetic quotes |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED, TIER-CRITICAL | Deploy adoption instrument; collect real pull signals |
| program | MIXED | | Validate phases with engineering lead; resolve dependency |
| topic | MIXED | | Re-run topic-story after first 3 real signals are filed |

---

Next: /mock:review {topic} {this-file}
```

---

## Variation Summary

| Variation | Axis | C-24 / C-25 | C-23 | Inertia framing | Format |
|-----------|------|-------------|------|-----------------|--------|
| V-01 | Register: occupancy-language | FAIL (occupancy) | FAIL (preamble only) | Absent | Prose |
| V-02 | Sequence: being-language per-namespace | PASS | PASS | Absent | Prose |
| V-03 | Format: structured tables | PASS (preamble) | PARTIAL | Absent | Tables |
| V-04 | Being-language + lifecycle phases | PASS | PASS | Absent | Prose + phases |
| V-05 | Being-language + inertia framing | PASS | PASS | Every artifact | Prose + inertia |

**Diagnostic gradient:** V-01 is the floor (fails C-25, C-24, C-23). V-02 clears the role/identity staircase. V-03 tests whether format change disrupts identity criteria. V-04 adds lifecycle scaffolding. V-05 adds inertia depth — the aspirational ceiling for this round.
