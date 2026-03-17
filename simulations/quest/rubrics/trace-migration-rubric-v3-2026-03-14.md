Rubric v3 written. Here's what changed:

---

## v3 Summary

**3 new aspirational criteria** from Round 2 excellence patterns:

| C-NN | Name | Source Pattern |
|------|------|----------------|
| C-14 | **Critical Field Type Annotation** | Explicit "(BINARY FIELD)" label at the field definition site converts a formatting convention into a structural type annotation — non-conformant prose is a type mismatch, not an omission. Stronger enforcement than C-13 (which only requires binary values) because the label is visible at every occurrence. |
| C-15 | **Forward-Progress Gate with Binary State** | A gate with explicit OPEN/BLOCKED state that a downstream phase must name as a prerequisite before it can open. Stronger than C-12 (positional placement) because the model must *resolve* a state, not just *sequence* content. |
| C-16 | **Two-Phase Analytical Decoupling** | Interrogative Phase A organizes by concern freely; canonical Phase B produces the mandatory step-ordered artifact. Decouples analytical depth from chronological obligation. Phase B satisfies C-05; Phase A does not violate it. |

**Scoring changes:**
- Aspirational tier: 25 pts (5 criteria) → 40 pts (8 criteria)
- Total max: 115 → 130
- Golden threshold: unchanged at 80% composite + all essential pass

**Two new evaluator notes:**
- **C-05 two-phase exception**: Phase B canonical trace satisfies C-05 even when Phase A organizes by concern. The single-phase conflict note applies only to single-phase question-driven outputs.
- **C-11 two-phase gap**: Phase A questions do not inherit step-number citation from Phase B tables. Full C-11 credit requires explicit citation instruction in Phase A question text — formalizing the V-04 R2 residual (3/5 on C-11) so future evaluators don't have to rediscover it.

**Separation of C-14 vs C-13 and C-15 vs C-12** is clarified in evaluator notes: each pair is distinct enforcement, not redundant.
erformance Cliff Detection** | depth | recommended | The output identifies at least one operation likely to cause a performance cliff on large tables (e.g., full-table rewrite, index rebuild on wide table, type cast requiring row scan). For each, it names the table, estimated row count if knowable, and the specific risk (lock duration, I/O spike, replication lag). |
| C-07 | **Rollback Viability Assessment** | depth | recommended | For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation), the output assesses whether the step is reversible: (a) fully reversible with down migration, (b) reversible only from backup, or (c) irreversible. At least one step is classified. |
| C-08 | **Domain Expert Framing** | behavior | recommended | The output applies at least one Commerce, Finance, or Operations lens. This means naming a real-world consequence of the migration risk in domain terms -- e.g., "a truncated amount column could silently zero-out refunds over $10k" not just "decimal precision is reduced." |

---

## Aspirational Criteria (40 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Zero-Downtime Viability** | depth | aspirational | The output assesses whether the migration can be run without downtime using an expand/contract pattern or online DDL, and -- if not -- names the specific step that requires a maintenance window and why. |
| C-10 | **Idempotency Check** | coverage | aspirational | The output evaluates whether each migration step is safe to run twice (idempotent). Any step that would corrupt data or fail on re-run is flagged with the specific failure mode (e.g., duplicate key error, double-applied data transform). |
| C-11 | **Locked Execution Sequence as Named Artifact** | structure | aspirational | The execution order is established once -- as a numbered table or explicitly labeled list -- in the first substantive section. At least two subsequent sections reference steps by those assigned numbers rather than re-describing them. This prevents reordering or regrouping in downstream analysis sections. |
| C-12 | **Domain Section Pre-Positioned Before Verification** | structure | aspirational | The domain/business impact section appears before any summary, verification, or recommendations section -- not deferred to the end. A domain section placed last or second-to-last fails this criterion, because deferral is indistinguishable from omission in practice. |
| C-13 | **Silence-is-Failure Completeness Enforcement** | structure | aspirational | Critical fields (data loss statement, NOT NULL risk flag, rollback viability per step) use binary or enumerated choices -- YES/NO/PARTIAL, checkbox, or a fixed taxonomy -- such that the absence of a choice is structurally detectable. Free-form omittable fields for these critical fields do not satisfy this criterion. |
| C-14 | **Critical Field Type Annotation** | structure | aspirational | At least the three critical fields (data loss statement, NOT NULL risk, rollback viability) carry an explicit type annotation -- e.g., "(BINARY FIELD)", "(BINARY)", "(fixed taxonomy)" -- at every point of definition: section headers, column names, or inline field labels. The annotation names the structural class of the expected value, making non-conformant free-form prose a visible type mismatch rather than an implicit omission. A critical field label without a type annotation does not satisfy this criterion. |
| C-15 | **Forward-Progress Gate with Binary State** | structure | aspirational | At least one dependency gate uses an explicit binary state (e.g., OPEN/BLOCKED, PASS/FAIL) that must be resolved before a downstream phase can proceed. The downstream phase's header or instruction explicitly names the gate state as a prerequisite -- e.g., "VERIFY PHASE: domain gate must be OPEN before writing verify checks." A section that is merely positioned before another section without a resolvable binary state does not satisfy this criterion. |
| C-16 | **Two-Phase Analytical Decoupling** | structure | aspirational | The output explicitly separates an interrogative phase (Phase A) that organizes analytical work by concern, entity, or risk type from a canonical synthesis phase (Phase B) that produces a mandatory step-ordered artifact. Phase B must be labeled as the authoritative output. This decouples analytical depth from chronological output obligation: Phase A can interrogate freely without violating C-05, which is satisfied by Phase B alone. |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 40 | 8 (C-09 to C-16) |
| **Total** | **130** | **16** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80%.

---

## Evaluator Notes

- **C-02 explicit negative**: If the migration genuinely has no data loss paths, the output must say so with a brief argument -- silence is not a pass.
- **C-03 scope**: Focus on constraint *changes*, not constraints that exist unchanged before and after.
- **C-05 structural conflict**: Single-phase question-driven formats (Q1=steps, Q2=state, Q3=data loss...) that organize output by analytical concern rather than execution sequence fail C-05 even if Q1 lists steps correctly -- the reader cannot follow migration state forward in time across later questions.
- **C-05 two-phase exception**: When a two-phase structure is used (C-16), Phase A organizing by analytical concern does not fail C-05. Phase B, if explicitly labeled as the canonical artifact and strictly ordered by execution sequence, satisfies C-05. The single-phase structural conflict applies only to single-phase outputs.
- **C-06 threshold**: Performance cliff detection only applies if the migration touches tables with non-trivial row counts (>10k rows implied or stated). If the schema is empty/new, C-06 auto-passes with a note.
- **C-08 domain lens**: A passing answer names a concrete business object (order, invoice, ledger entry, shipment) -- generic database terminology alone does not satisfy this criterion.
- **C-11 reference depth**: A section that says "see step 3 above" satisfies the reference requirement; a section that re-describes "the column rename step" without a number does not.
- **C-11 two-phase gap**: When using two-phase structure (C-16), Phase A questions organized by entity or concern do not inherit step-number citation from Phase B tables. To earn full C-11 credit with a two-phase structure, step-number citation must be explicitly required in Phase A question text -- e.g., "for each entity, reference it by its Step N from Q1." Phase B enforcing citation alone is insufficient if Phase A leaves re-description paths open.
- **C-12 placement test**: Count sections from the end. If the domain section is the last or second-to-last section, it fails. It must have at least one non-trivial section (verification, summary, recommendations) after it.
- **C-13 critical fields only**: This criterion applies only to the three named field types (data loss, NOT NULL risk, rollback viability). Free-form prose is acceptable for non-critical fields such as performance notes or idempotency commentary.
- **C-14 vs C-13**: C-13 requires that critical fields use binary or enumerated values. C-14 requires an explicit type label at the field definition site. An output can pass C-13 (uses YES/NO) without passing C-14 (no "(BINARY FIELD)" annotation). Both can be satisfied simultaneously and are not redundant.
- **C-15 vs C-12**: C-12 requires positional placement of the domain section before verification. C-15 requires an explicit binary gate state that blocks the next phase. A gate merely positioned before another section without a resolvable binary state satisfies C-12 but not C-15.
- **C-16 and C-11**: Two-phase structure satisfies C-05 but does not automatically satisfy C-11 in Phase A. Evaluators should check both phases independently for step-number citation discipline.

---

## v3 Change Log

Three new aspirational criteria added from Round 2 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| "BINARY FIELD" meta-annotation converts critical fields from formatting conventions to structural type annotations -- model treats absence or non-conformance as a type error, not an omission (V-03, V-05) | C-14: Critical Field Type Annotation |
| Gate binary (OPEN/BLOCKED) blocks forward progress on dependent phases -- stronger than positional placement alone because the model must resolve a state, not just sequence content (V-02, V-05) | C-15: Forward-Progress Gate with Binary State |
| Two-phase structure (interrogative Phase A + synthesis Phase B) decouples analytical depth from chronological output obligation -- Phase A questions organize by concern freely, Phase B table enforces canonical step-ordered artifact (V-04) | C-16: Two-Phase Analytical Decoupling |

**Scoring changes:**
- Aspirational tier: 25 pts (5 criteria) -> 40 pts (8 criteria)
- Total max: 115 -> 130
- Golden threshold: unchanged at 80% composite + all essential pass

**Two new evaluator notes added:**
- **C-05 two-phase exception**: Two-phase structure satisfies C-05 via Phase B; the single-phase conflict note does not apply to two-phase outputs.
- **C-11 two-phase gap**: Phase A questions organized by concern do not inherit step-number citation from Phase B tables -- citation must be explicitly stated in Phase A question text to close the gap (formalizing the V-04 R2 residual finding).
