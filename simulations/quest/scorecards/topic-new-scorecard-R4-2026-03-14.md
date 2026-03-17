# Quest Score — topic-new R4

**Skill**: `topic:new` | **Rubric**: v4 | **Date**: 2026-03-14

---

## Per-Variation Scoring

### V-01: Stakeholder-Traceability Column

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | TOPICS.md entry exists | **PASS** | Explicit "Register in simulations/TOPICS.md" with table format |
| C-02 | Strategy at correct path | **PASS** | "Write simulations/{topic}/strategy.md" |
| C-03 | All five signal fields present | **PASS** | Namespace, Skill, Item name, Owner role, Priority all in FIELD SCHEMA |
| C-04 | Priority values valid | **PASS** | FIELD SCHEMA row 6: "essential / recommended / optional" with consequence |
| C-05 | At least one essential signal | **PASS** | COVERAGE SCHEMA row 1: ">=1" with gate consequence |
| C-06 | Multi-namespace coverage | **PASS** | Coverage Schema row 2: ">=2 distinct namespaces" |
| C-07 | Narrative rationale | **PASS** | "### Rationale" section with 2–4 sentences specified |
| C-08 | Owner roles differentiated | **PASS** | Coverage Schema row 3: ">=2 distinct owner roles from Stakeholders table" |
| C-09 | Commit gate defined | **PASS** | "### Commit Gate" section with testable condition requirement |
| C-10 | Artifact naming convention | **PASS** | "### Naming Reference" + Field Schema row 3 |
| C-11 | Checkbox-gate before phase transition | **PASS** | 10-item pre-write gate with explicit "Do not write any file until all ten checks pass" |
| C-12 | Invalid vocabulary as operational consequence | **PASS** | "strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold" |
| C-13 | Dedicated section per aspirational criterion | **PASS** | Commit Gate and Naming Reference are distinct named sections in strategy template |
| C-14 | Consequence framing pervasive | **PASS** | Every row in FIELD SCHEMA and COVERAGE SCHEMA carries a Consequence column |
| C-15 | Opens with stakeholder-risk enumeration | **PASS** | Prompt literally opens with "## Stakeholders at Risk" fill-in table |
| C-16 | Every criterion enforced by structural mechanism | **PASS** | Schema tables + coverage schema + 10-item gate + section headers — no prose-only enforcement |
| C-17 | Stakeholder-risk as active fill-in output step | **PASS** | Labeled "first required output"; "Do not proceed" gate; Stakeholder column in FIELD SCHEMA forces row-level traceability back to that table |
| C-18 | Constraints partitioned into named schemas with consequence columns | **PASS** | FIELD SCHEMA + COVERAGE SCHEMA are physically distinct; consequence columns present; gate checkboxes cite "Field Schema row N" / "Coverage Schema row N" by reference |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/10
**Composite**: 60 + 30 + 10 = **100** ✓ Golden

---

### V-02: Schema-First Ordering

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01–C-14 | All essential, recommended, and most aspirational | **PASS** | Schemas present with consequence columns; checkboxes; sections intact |
| C-15 | Opens with stakeholder-risk enumeration | **FAIL** | Prompt opens with "## Field Schema" — stakeholder-risk section is Step 1, physically third |
| C-16 | Every criterion enforced by structural mechanism | **PASS** | Schemas + checkboxes + section headers enforce all internal constraints; positional failure is a placement issue, not an absent mechanism |
| C-17 | Stakeholder-risk as active fill-in output step | **FAIL** | Labeled "Now produce the first required output" but schemas precede it — C-15's positional anchor is co-load-bearing; "first output" in C-17 is anchored to C-15's "opens with" |
| C-18 | Constraints partitioned into named schemas | **PASS** | Two distinct schemas with consequence columns and by-reference gate checkboxes intact |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 8/10 (C-15, C-17 fail)
**Composite**: 60 + 30 + 8 = **98** ✓ Golden

---

### V-03: Unified Contract Table

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01–C-17 | All essential, recommended, aspirational except C-18 | **PASS** | Prompt opens with Stakeholders fill-in (C-15 PASS); fill-in is first active output (C-17 PASS); consequence framing pervasive (C-14 PASS); structural mechanisms present throughout (C-16 PASS) |
| C-18 | Constraints partitioned into named schemas with consequence columns | **FAIL** | Single CONTRACT TABLE with a Scope column does not satisfy "two named schemas" — physical separation is required; per-field and coverage constraints share a table, eliminating the distinct structural homes the criterion specifies |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 9/10 (C-18 fails)
**Composite**: 60 + 30 + 9 = **99** ✓ Golden

---

### V-04: Template-First Structure

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01–C-14 | All essential, recommended, and early aspirational | **PASS** | Template + constraint structure provides coverage of C-01–C-14 |
| C-15 | Opens with stakeholder-risk enumeration | **FAIL** | Output template shown first — no stakeholder-risk opener |
| C-16 | Every criterion enforced by structural mechanism | **FAIL** | Without a dedicated stakeholder fill-in step, role differentiation (C-08) falls back to prose instruction — the structural mechanism for its enforcement is absent |
| C-17 | Stakeholder-risk as active fill-in output step | **FAIL** | No standalone gated Stakeholders step means there is no first-output fill-in table; bulk gate does not satisfy per-step gate requirement |
| C-18 | Constraints partitioned into named schemas | **PASS** | Two-schema separation can coexist with template-first ordering |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/10 (C-15, C-16, C-17 fail)
**Composite**: 60 + 30 + 7 = **97** ✓ Golden

---

### V-05: Cascade Consequences + Traceability Column

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01–C-13 | All essential, recommended, aspirational through C-13 | **PASS** | Full structure retained from baseline |
| C-14 | Consequence framing pervasive | **PASS** | Two-column consequence (Immediate failure / Downstream effect) deepens single-column baseline — every constraint carries both temporal levels |
| C-15 | Opens with stakeholder-risk enumeration | **PASS** | Prompt opens with Stakeholders fill-in table |
| C-16 | Every criterion enforced by structural mechanism | **PASS** | Cascade columns + Stakeholder field column + two schemas + gated fill-in — no prose-only enforcement remaining |
| C-17 | Stakeholder-risk as active fill-in output step | **PASS** | Stakeholder column in FIELD SCHEMA makes traceability a per-row auditable field back to opener table; fill-in is first output |
| C-18 | Constraints partitioned into named schemas with consequence columns | **PASS** | Two-column consequence satisfies C-18's consequence column requirement at higher fidelity; physical separation maintained |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/10
**Composite**: 60 + 30 + 10 = **100** ✓ Golden

---

## Round 4 Scoreboard

| V | Essential | Recommended | Aspirational | Composite | Golden | Fails |
|---|-----------|-------------|--------------|-----------|--------|-------|
| **V-01** | 5/5 | 3/3 | 10/10 | **100** | ✓ | — |
| **V-02** | 5/5 | 3/3 | 8/10 | **98** | ✓ | C-15, C-17 |
| **V-03** | 5/5 | 3/3 | 9/10 | **99** | ✓ | C-18 |
| **V-04** | 5/5 | 3/3 | 7/10 | **97** | ✓ | C-15, C-16, C-17 |
| **V-05** | 5/5 | 3/3 | 10/10 | **100** | ✓ | — |

All essential criteria pass in all variations. All variations clear the 80-composite golden threshold.

---

## Excellence Signals

**From V-01 and V-05 (tied top score):**

**Stakeholder-field encoding eliminates prose traceability.** V-01's addition of Stakeholder as a 6th field in FIELD SCHEMA — with allowed values restricted to rows in the Stakeholders table and its own Consequence entry — makes C-17 traceability auditable per-row via the pre-write gate checkbox rather than via cross-reference prose. The requirement "signal ownership must trace to the Stakeholders table" becomes mechanically verifiable for each row independently.

**Cascade consequences deepen C-14 beyond single failure mode.** V-05's two-column consequence structure (Immediate failure / Downstream effect) assigns each constraint two distinct failure modes at different temporal distances. This is a structural improvement over single-column consequences: immediate failures catch the validation problem; downstream effects communicate the operational cost to stakeholders who care about later phases.

**Positional anchor of C-17 confirmed by V-02.** When reference schemas precede the Stakeholders fill-in, both C-15 and C-17 fail even when the step is explicitly labeled "first required output." The diagnostic confirms that C-17's "first output" is co-anchored to C-15's "prompt opens with" — labeling a step as first does not substitute for placing it first.

**Physical table separation required by C-18, confirmed by V-03.** A unified CONTRACT TABLE with a Scope column fails C-18 despite containing the same information as two tables. The "two named schemas" requirement is physical, not logical — field-level and coverage-level constraints must occupy distinct tables, not a discriminated row in one table.

---

## New Patterns

**Pattern 1 — C-17 positional anchor:** C-17 inherits a positional constraint from C-15. "First output" means physically first in the prompt, not merely labeled as the first production step. Any reference material — including definitional schemas — placed before the Stakeholders fill-in breaks both criteria. The fix: schemas must follow the fill-in opener or be embedded within sections that come after it.

**Pattern 2 — C-18 physical separation requirement:** Two-schema separation is a physical layout constraint, not a logical partition. A single table with a `Scope` column (distinguishing per-field from whole-plan constraints) does not satisfy C-18, even if it contains every required column including consequences. Two tables must exist as distinct named blocks; each must have exactly one structural home per constraint.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-17 positional anchor: 'first output' is co-anchored with C-15's 'opens with' — reference schemas placed before the Stakeholders fill-in break both criteria even when the step is explicitly labeled 'first required output'", "C-18 physical separation requirement: two named schemas must be physically distinct tables — a single CONTRACT TABLE with a Scope column discriminating per-field vs whole-plan constraints does not satisfy the criterion regardless of column parity"]}
```
