Written to `simulations/quest/rubrics/trace-migration-rubric-v5-2026-03-14.md`.

---

## What changed: v4 → v5

Four new aspirational criteria, each closing a gap left open by a v4 criterion:

| New | Closes gap in | Pattern source | What it adds |
|-----|--------------|----------------|--------------|
| **C-19** Per-Section Citation Repetition | C-18 | V-01 (Q2–Q9), V-03 (all phases) | C-18 requires source artifact named in *at least one* instruction; C-19 requires it at *every* section so no section can silently revert to generic ordinals |
| **C-20** Domain Section Completion Constraint | C-12 | V-01 B2 label | C-12 tests positional placement post-hoc; C-20 requires a forward-named completion instruction in the domain header that makes the constraint executable rather than just observable |
| **C-21** Complete Phase Gate Chain | C-15 | V-03 (5-gate cascade) | C-15 requires at least one gate; C-21 requires every phase transition to be gated with each phase header naming its prerequisite gate -- no ungated gaps |
| **C-22** Pre-Seeded Inline Domain Example | C-08 | V-03 DOMAIN IMPACT PHASE | C-08 requires domain framing in the output; C-22 requires the template itself to contain a pre-filled worked example (table, type change, numeric threshold) as model output text, not as instruction |

**Scoring:** Aspirational tier 50 → 70 pts (10 → 14 criteria). Total max 140 → 160. Golden threshold 80% = 128 pts.
ULT is present on a non-empty table, this is flagged as a migration risk. |
| C-05 | **Chronological Step Ordering** | format | essential | Migration steps are presented in execution order. The trace follows the actual sequence a database engine would apply them -- not alphabetical by table, not grouped by type. The reader can follow the migration state forward in time. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Performance Cliff Detection** | depth | recommended | The output identifies at least one operation likely to cause a performance cliff on large tables (e.g., full-table rewrite, index rebuild on wide table, type cast requiring row scan). For each, it names the table, estimated row count if knowable, and the specific risk (lock duration, I/O spike, replication lag). |
| C-07 | **Rollback Viability Assessment** | depth | recommended | For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation), the output assesses whether the step is reversible: (a) fully reversible with down migration, (b) reversible only from backup, or (c) irreversible. At least one step is classified. |
| C-08 | **Domain Expert Framing** | behavior | recommended | The output applies at least one Commerce, Finance, or Operations lens. This means naming a real-world consequence of the migration risk in domain terms -- e.g., "a truncated amount column could silently zero-out refunds over $10k" not just "decimal precision is reduced." |

---

## Aspirational Criteria (70 points total)

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
| C-17 | **Gate Field Annotation Compound** | structure | aspirational | At least one C-15 gate state field carries a C-14-style explicit type annotation at its definition site -- e.g., "DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED" or "GATE STATE (BINARY FIELD): OPEN / BLOCKED." This applies C-14 and C-15 enforcement simultaneously at the same field: a non-conformant value triggers both a type mismatch (C-14) and an unresolved phase block (C-15). An output that satisfies C-14 and C-15 independently but leaves gate state fields without type annotations does not satisfy this criterion. |
| C-18 | **Named Artifact Citation** | structure | aspirational | Citation instructions that require step-number references must name the specific source artifact -- e.g., "Step N from Q1," "step number from SECTION 0 registry," or "step number from PARSE PHASE." The source-artifact suffix prevents implicit re-numbering by anchoring citations to a named location rather than a generic ordinal. In two-phase structures, this instruction must appear in Phase A question text. In single-phase structures, it must appear in at least one analytical section instruction. A citation instruction that says only "reference by step number" or "cite by Step N" without naming the source artifact does not satisfy this criterion. |
| **C-19** | **Per-Section Citation Repetition** | structure | aspirational | The citation instruction naming the source artifact appears in EVERY analytical section or question -- not just in a global preamble or registry header. Each section or question carries its own explicit instruction (e.g., "Reference each affected step as 'Step N from Q1'"), so no section can silently revert to generic ordinals. An output whose citation instruction appears only once globally -- even if that instruction says "all sections must cite from [ARTIFACT]" -- does not satisfy this criterion if downstream section text contains no per-section repetition. |
| **C-20** | **Domain Section Completion Constraint** | structure | aspirational | The domain section header or label carries an explicit forward-reference naming the downstream section it must precede -- e.g., "(POSITIONED BEFORE B3 VERIFY — complete before writing B3)." This transforms the C-12 positional requirement into a live execution constraint: the instruction cannot be satisfied without writing domain content before advancing to the named downstream section. A domain section that satisfies C-12 by placement alone, without a forward-named completion instruction in its header or label, does not satisfy this criterion. |
| **C-21** | **Complete Phase Gate Chain** | structure | aspirational | Every phase transition in the output has a named binary gate as both the output of the preceding phase and the stated prerequisite of the succeeding phase. No ungated phase transitions exist: each phase header or opening instruction names the gate it requires to be OPEN before the phase may be written. A structure with gates at some but not all phase transitions, or a single gate between two phases in a multi-phase output, does not satisfy this criterion. |
| **C-22** | **Pre-Seeded Inline Domain Example** | behavior | aspirational | The domain section contains at least one pre-filled worked example as model output text -- not as instruction -- naming a specific table, a column type change (before and after), an operation, and a numeric business threshold (e.g., "Step 3 reduces decimal(19,4) to decimal(10,2) on payment_amount -- charges over $9,999,999.99 silently capped"). The example demonstrates the required specificity rather than instructing the reader to provide it. A domain section that instructs "provide a numeric threshold example" without pre-seeding one does not satisfy this criterion. |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 70 | 14 (C-09 to C-22) |
| **Total** | **160** | **22** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80% (128 pts).

---

## Evaluator Notes

*(all v4 notes carried forward, four new notes added)*

- **C-02 explicit negative**: If the migration genuinely has no data loss paths, the output must say so with a brief argument -- silence is not a pass.
- **C-03 scope**: Focus on constraint *changes*, not constraints that exist unchanged before and after.
- **C-05 structural conflict**: Single-phase question-driven formats (Q1=steps, Q2=state, Q3=data loss...) that organize output by analytical concern rather than execution sequence fail C-05 even if Q1 lists steps correctly.
- **C-05 two-phase exception**: Phase B, explicitly labeled as the canonical artifact and strictly ordered by execution sequence, satisfies C-05. The single-phase structural conflict applies only to single-phase outputs.
- **C-06 threshold**: C-06 auto-passes with a note if the schema is empty/new.
- **C-08 domain lens**: Concrete business object required (order, invoice, ledger entry, shipment) -- generic database terminology alone does not satisfy this criterion.
- **C-11 reference depth**: "see step 3 above" satisfies; "the column rename step" without a number does not.
- **C-11 two-phase gap**: Phase A questions do not inherit step-number citation from Phase B tables. Citation must be explicitly stated in Phase A question text.
- **C-12 placement test**: Domain section must have at least one non-trivial section (verification, summary, recommendations) after it.
- **C-13 critical fields only**: Applies only to data loss, NOT NULL risk, and rollback viability fields.
- **C-14 vs C-13**: C-13 requires binary/enumerated values; C-14 requires the type label at the definition site. Not redundant.
- **C-15 vs C-12**: C-12 tests positional placement; C-15 tests whether a resolvable binary state blocks the next phase. Not redundant.
- **C-16 and C-11**: Two-phase structure satisfies C-05 but does not automatically satisfy C-11 in Phase A. Evaluate both phases independently.
- **C-17 vs C-14 + C-15**: C-17 only fires at the intersection -- both C-14 and C-15 must be applied to the same gate state field. Satisfying each criterion independently in separate places is not sufficient.
- **C-18 vs C-11**: C-11 requires step-number citation; C-18 requires the source artifact name in the citation instruction. Labeling the registry "(AUTHORITATIVE ARTIFACT)" at the registry site does not substitute for naming the source in downstream citation instructions.
- **C-19 vs C-18** *(new)*: C-18 requires the source artifact to be named in citation instructions; C-19 requires that instruction to appear at every analytical section. An output can pass C-18 with a single correctly-named instruction while failing C-19 because remaining sections contain no per-section repetition. Evaluate C-19 by counting sections that lack their own citation instruction, not by checking whether a global citation rule exists.
- **C-20 vs C-12** *(new)*: C-12 tests whether the domain section is positioned before verification. C-20 tests whether the domain section header explicitly names the section it must precede and instructs completion before advancing. An output that satisfies C-20 automatically satisfies C-12, but not vice versa. The distinguishing signal is the forward-named section in the completion instruction.
- **C-21 vs C-15** *(new)*: C-15 requires at least one gate. C-21 requires every phase transition to be gated, with each phase header naming its prerequisite gate. Count phase transitions, then count gated transitions -- any gap fails C-21. A two-phase output with one gate satisfies C-15 but fails C-21 if either the Phase A exit gate or the Phase B entry prerequisite is unnamed.
- **C-22 vs C-08** *(new)*: C-08 requires domain framing in the output; C-22 requires a pre-filled worked example as model output text within the template. The distinction is instruction vs demonstration: C-08 passes if the output contains concrete domain framing; C-22 passes only if the template itself contains a pre-seeded example. An output can satisfy C-08 from correct LLM behavior without C-22 ever being present in the template.

---

## v5 Change Log

Four new aspirational criteria added from Round 4 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| V-01 repeats "Reference each affected step as 'Step N from Q1'" at Q2 through Q9. V-03 repeats "Step N from PARSE PHASE REGISTRY" at every phase. C-18 requires the source artifact named in at least one instruction; neither V-01 nor V-03 leaves any section without its own citation instruction. This prevents per-section regression to generic ordinals even if the global rule is ignored. | C-19: Per-Section Citation Repetition |
| V-01's domain section (B2) carries "(POSITIONED BEFORE B3 VERIFY — complete before writing B3)." C-12 tests positional placement after the fact; this label makes the constraint executable -- the instruction cannot be satisfied without writing domain content before advancing to B3. | C-20: Domain Section Completion Constraint |
| V-03 has five gates (PARSE, TRACE, DOMAIN, OPERATIONAL, VERIFY) where each phase header names its prerequisite: "TRACE PHASE (requires PARSE GATE = OPEN)," etc. C-15 requires at least one gate; V-03's pattern closes every phase transition in a directed chain with no ungated gaps. | C-21: Complete Phase Gate Chain |
| V-03's DOMAIN IMPACT PHASE pre-fills: "Step 3 from PARSE PHASE REGISTRY reduces decimal(19,4) to decimal(10,2) on payment_amount -- charges over $9,999,999.99 silently capped." This is model output text in the template, not instruction text. C-08 requires domain framing; C-22 requires the template to demonstrate rather than just instruct that specificity. | C-22: Pre-Seeded Inline Domain Example |

**Scoring changes:**
- Aspirational tier: 50 pts (10 criteria) -> 70 pts (14 criteria)
- Total max: 140 -> 160
- Golden threshold: unchanged at 80% composite (now 128 pts) + all essential pass
