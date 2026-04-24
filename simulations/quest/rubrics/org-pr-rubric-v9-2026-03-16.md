```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 9
supersedes: org-pr-rubric-v8-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v8 -> v9)

Three new aspirational criteria extracted from R9 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=19 to N=22.

**C-30** (gate content sufficiency): V-03 and V-04 satisfy C-09 via an inline gate
sentence in the opening topic line rather than a dedicated "### Phase Gate" section. This
is the first round to confirm that gate structure is not load-bearing for C-09. The
criterion fires on gate content alone: if the lifecycle condition, halt instruction, and
alternative path reference are all present, the gate satisfies C-09 regardless of whether
it appears as an inline clause, a labeled subsection, or a named block. A gate that
has the correct label but omits one of the three content elements fails C-09 regardless
of placement. C-30 canonizes this: structural form is irrelevant; content completeness is
the only criterion. PASS if the phase/lifecycle gate contains all three elements —
(1) lifecycle condition identifying the phase boundary, (2) explicit halt instruction,
(3) alternative path reference — regardless of where in the prompt the gate appears or
whether it is labeled. FAIL if a gate construct is present but one or more of the three
elements is absent. N/A if the prompt contains no phase/lifecycle gating requirement
(counts as PASS).

**C-31** (named-invalid-form 2-form floor): V-01, V-04, and V-05 satisfy both C-12
(named invalid forms) and C-24 (correction-paired catalog) with exactly 2 named forms
(Untagged + Revision). This is the first round to confirm that 2 forms is the minimum
sufficient catalog size. The key constraint is that each retained form must address a
distinct governance failure mode — a decision-path corruption, not a formatting constraint.
Untagged addresses verdict formula corruption (a finding without a severity tag cannot be
counted in the consensus formula); Revision addresses authority chain corruption (a
Revision finding without an upstream override record cannot be traced). These are distinct
failure modes. A catalog of 2 forms satisfies C-12 and C-24 when this condition holds.
A catalog that expands to include formatting-only forms (e.g., Aggregate as a formatting
note rather than a governance rule) does not improve the governance coverage — it dilutes
it. PASS if the named-invalid-form catalog contains at least 2 forms, each with a
correction instruction, and each addressing a distinct decision-path governance failure
mode. FAIL if the catalog contains fewer than 2 forms, or if no form addresses a
decision-path failure mode (all forms are formatting constraints only). N/A if the prompt
uses no named-form output structure (counts as PASS).

**C-32** (self-correction gate 3-item floor): V-02, V-04, and V-05 satisfy C-16 with
self-correction gates of exactly 3 items. These variations omit items present in V-01/V-03
gates (if-stays field fill, upstream override prohibition, locator validity check), but
in each case the omitted items are enforced by named structural elements elsewhere in the
prompt — the if-stays fill requirement is in the finding template, the upstream override
prohibition is in the authority chain declaration, the locator validity check is in the
locator self-correction gate (C-08). This is the first round to confirm that item count
alone does not determine C-16 satisfaction; what matters is that post-generation outputs
are covered, either in the gate or by named structural redundancy. 3 items is the minimum
check depth when structural redundancy is present. A gate with fewer than 3 items raises
the probability that at least one post-generation output is uncovered with no structural
backstop. PASS if the self-correction gate contains at least 3 items covering
post-generation outputs, and any output types absent from the gate are enforced by a
named structural element (template field, authority chain declaration, named gate)
elsewhere in the prompt. FAIL if the gate contains fewer than 3 items and the gap is not
covered by named structural redundancy — or if gap coverage is present but not named
(implicit coverage does not satisfy the redundancy condition). N/A if the prompt contains
no self-correction gate (counts as PASS).

---

## Changelog (v7 -> v8)

Two new aspirational criteria extracted from R8 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=17 to N=19.

**C-28** (distributed conflict table completeness): V-01 and V-02 satisfy C-22 via
per-role sub-tables — each role block contains its own 4-column conflict table (Surface /
This Role's Assessment / Upstream Role Assessment / Resolution). This is the first round
to confirm the distributed-table path as a valid C-22 form. The per-role architecture
means a role specialist reading only their section sees the complete conflict picture: the
surface in dispute, both positions, and the resolution outcome. A table missing any of
these four fields forces cross-section traversal — the reviewer cannot determine the
resolution without leaving their role block, which increases the chance that the wrong
resolution rule is applied. V-03/V-04/V-05 use centralized Conflict Analysis sections and
do not raise this criterion. PASS if every per-role conflict sub-table includes all four
fields: (1) conflict surface or criterion identifier, (2) this role's position, (3) the
conflicting role's position or role identifier, (4) resolution outcome or resolution rule
reference. FAIL if any per-role table is missing one or more of these fields. N/A if
conflict governance is centralized rather than per-role (counts as PASS).

**C-29** (governance declaration co-location): V-05 places both the axis count declaration
(C-26: "two governance axes") and the judgment-elimination declaration (C-23: "no judgment
required") in a single opening reconciliation rule. V-01/V-02 declare axis count in the
opening but place judgment-elimination inside per-role sub-table resolution entries.
V-03 declares axis count in the opening but places judgment-elimination in the standalone
Conflict Analysis section's resolution column instruction. In both cases the declarations
are present but separated. Separation creates a reading-path vulnerability: a reviewer who
enters the Conflict Analysis section directly — or reads only the resolution column
template — encounters the mechanism without its characterization and may apply judgment
under the belief that the prompt does not prohibit it. Co-location eliminates this
vulnerability by making the complete governance model visible at the prompt's entry point,
before any operational content begins. PASS if the prompt includes a single preamble or
opening block that contains both the governance scope declaration (axis count or
equivalent) and the resolution mechanism's characterization (mechanical/non-judgment or
equivalent). FAIL if both declarations are present in the prompt but separated across
different structural locations without a cross-reference. N/A if only one of the two
declarations is present — no co-location requirement applies to a single-declaration prompt
(counts as PASS).

---

## Scoring Formula

Composite = Essential (max 60) + Recommended (max 30) + Aspirational (max 10).

Aspirational = (PASS_equiv / N_aspirational) × 10, rounded to 2 decimal places.

PASS_equiv weights: N/A → 1.0, PASS → 1.0, PARTIAL → 0.5, FAIL → 0.

N_aspirational = **22** (v9).

---

## Essential Criteria (60 pts / 12 pts each)

| Criterion | Description |
|-----------|-------------|
| C-01 | Per-role finding output |
| C-02 | Severity classification (P1/P2/P3) |
| C-03 | Consensus analysis section |
| C-04 | Go/no-go recommendation |
| C-05 | Role scoping (relevant roles only) |

Definitions carried forward from v7 unchanged.

---

## Recommended Criteria (30 pts / 6 pts each)

| Criterion | Description |
|-----------|-------------|
| C-06 | Projection-aware consensus |
| C-07 | Conflict analysis (resolution present) |
| C-08 | Locator self-correction gate |
| C-09 | Phase/lifecycle gating |
| C-10 | Downstream risk field |

Definitions carried forward from v7 unchanged.

---

## Aspirational Criteria (10 pts, N=22)

| Criterion | Description |
|-----------|-------------|
| C-11 | Formula lock |
| C-12 | Named invalid forms |
| C-13 | Inertia / if-stays framing |
| C-14 | Verdict escape closure |
| C-15 | Projection convergence call |
| C-16 | Self-correction gate pre-commit |
| C-17 | Role authority sequence declaration |
| C-18 | Axis conflict resolution rule |
| C-19 | Verdict hardening pair |
| C-20 | Priority table |
| C-21 | Authority-inertia reconciliation rule |
| C-22 | Conflict table structural completeness |
| C-23 | Judgment-elimination declaration |
| C-24 | Correction-paired invalid-form catalog |
| C-25 | Upstream override prohibition |
| C-26 | Governance axis count declaration |
| C-27 | If-stays field coverage |

Definitions for C-11 through C-27 carried forward from v7/v8 unchanged.

---

### C-28 — Distributed Conflict Table Completeness

*(added v8 — see Changelog v7→v8 for full derivation)*

PASS if every per-role conflict sub-table includes all four fields: (1) conflict surface
or criterion identifier, (2) this role's position, (3) the conflicting role's position or
role identifier, (4) resolution outcome or resolution rule reference.

FAIL if any per-role table is missing one or more of these fields.

N/A if conflict governance is centralized rather than per-role (counts as PASS).

---

### C-29 — Governance Declaration Co-location

*(added v8 — see Changelog v7→v8 for full derivation)*

PASS if the prompt includes a single preamble or opening block that contains both the
governance scope declaration (axis count or equivalent) and the resolution mechanism's
characterization (mechanical/non-judgment or equivalent).

FAIL if both declarations are present in the prompt but separated across different
structural locations without a cross-reference.

N/A if only one of the two declarations is present — no co-location requirement applies
to a single-declaration prompt (counts as PASS).

---

### C-30 — Gate Content Sufficiency

*(added v9 — see Changelog v8→v9 for full derivation)*

PASS if the phase/lifecycle gate contains all three elements — (1) lifecycle condition
identifying the phase boundary, (2) explicit halt instruction, (3) alternative path
reference — regardless of where in the prompt the gate appears or whether it is labeled.

FAIL if a gate construct is present but one or more of the three elements is absent.

N/A if the prompt contains no phase/lifecycle gating requirement (counts as PASS).

---

### C-31 — Named-Invalid-Form 2-Form Floor

*(added v9 — see Changelog v8→v9 for full derivation)*

PASS if the named-invalid-form catalog contains at least 2 forms, each with a correction
instruction, and each addressing a distinct decision-path governance failure mode.

FAIL if the catalog contains fewer than 2 forms, or if no form addresses a decision-path
failure mode (all forms are formatting constraints only).

N/A if the prompt uses no named-form output structure (counts as PASS).

---

### C-32 — Self-Correction Gate 3-Item Floor

*(added v9 — see Changelog v8→v9 for full derivation)*

PASS if the self-correction gate contains at least 3 items covering post-generation
outputs, and any output types absent from the gate are enforced by a named structural
element (template field, authority chain declaration, named gate) elsewhere in the prompt.

FAIL if the gate contains fewer than 3 items and the gap is not covered by named
structural redundancy — or if gap coverage is present but not named (implicit coverage
does not satisfy the redundancy condition).

N/A if the prompt contains no self-correction gate (counts as PASS).
```
