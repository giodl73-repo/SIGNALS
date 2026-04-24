Written to `simulations/quest/rubrics/trace-migration-rubric-v6-2026-03-14.md`.

---

## What changed: v5 -> v6

Three new aspirational criteria from Round 5 excellence signals:

| New | Closes gap in | Pattern source | What it adds |
|-----|--------------|----------------|--------------|
| **C-23** Step Registry Phase Encapsulation | C-21 | V-03 PARSE PHASE + PARSE GATE | Q-format registries emit no gate, leaving Q1->Q2 ungated. C-23 requires the registry wrapped in a named phase with an exit gate and the first analytical section naming it as prerequisite. |
| **C-24** Intra-Phase-B Gate Chain | C-21 | V-05 DOMAIN SYNTHESIS GATE B2->B3, VERIFY COMPLETION GATE B3->B4 | C-21 covers inter-phase transitions. C-24 extends the requirement into Phase B's internal sub-sections -- at least one named binary gate between Phase B sections. |
| **C-25** Explicit Phase-B Canonical Claim | C-16 | V-03 E-03 ("C-05 is satisfied here, not by any Phase A section") | C-16 requires Phase B labeled as authoritative. C-25 requires Phase B to explicitly assert it alone satisfies C-05, making the two-phase exception machine-readable rather than evaluator-inferred. |

**Scoring:** 160 -> 175 total max (17 aspirational criteria, 85 pts). Golden threshold 80% = 140 pts.

---

**Evaluator notes added:**
- **C-23 vs C-21**: C-21 full chain automatically satisfies C-23, not vice versa. Evaluate all three conditions independently: phase wrapper + exit gate + downstream prerequisite.
- **C-24 vs C-21**: Orthogonal. Inter-phase chain (C-21) and intra-Phase-B chain (C-24) are independent. Count Phase B sub-sections, count internal gates.
- **C-25 vs C-16**: C-16 passes by structural decoupling; C-25 passes only by explicit textual assertion in Phase B. Inference from structure is not sufficient.
udes additions, removals, type changes, nullability changes, and constraint changes. An entity described in generic terms without before/after values does not satisfy this criterion. |
| C-02 | **Data Loss Path Identification** | correctness | essential | The output identifies at least one concrete data loss path if one exists, OR explicitly states "no data loss paths found" with reasoning. A data loss path is any migration step that can silently drop rows, truncate values, or discard columns without surfacing an error. |
| C-03 | **Constraint Violation Analysis** | correctness | essential | For each constraint change (NOT NULL, UNIQUE, FK, CHECK), the output identifies whether existing data satisfies the new constraint. If it does not, it names which records violate it and what the migration does about it (fail, skip, backfill). |
| C-04 | **Missing Default Value Detection** | correctness | essential | For any new NOT NULL column added to an existing table, the output checks whether a DEFAULT is provided. If no DEFAULT is present on a non-empty table, this is flagged as a migration risk. |
| C-05 | **Chronological Step Ordering** | format | essential | Migration steps are presented in execution order. The trace follows the actual sequence a database engine would apply them -- not alphabetical by table, not grouped by type. The reader can follow the migration state forward in time. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Performance Cliff Detection** | depth | recommended | The output identifies at least one operation likely to cause a performance cliff on large tables (e.g., full-table rewrite, index rebuild on wide table, type cast requiring row scan). For each, it names the table, estimated row count if knowable, and the specific risk (lock duration, I/O spike, replication lag). |
| C-07 | **Rollback Viability Assessment** | depth | recommended | For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation), the output assesses whether the step is reversible: (a) fully reversible with down migration, (b) reversible only from backup, or (c) irreversible. At least one step is classified. |
| C-08 | **Domain Expert Framing** | behavior | recommended | The output applies at least one Commerce, Finance, or Operations lens. This means naming a real-world consequence of the migration risk in domain terms -- e.g., "a truncated amount column could silently zero-out refunds over $10k" not just "decimal precision is reduced." |

---

## Aspirational Criteria (85 points total)

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
| C-19 | **Per-Section Citation Repetition** | structure | aspirational | The citation instruction naming the source artifact appears in EVERY analytical section or question -- not just in a global preamble or registry header. Each section or question carries its own explicit instruction (e.g., "Reference each affected step as 'Step N from Q1'"), so no section can silently revert to generic ordinals. An output whose citation instruction appears only once globally -- even if that instruction says "all sections must cite from [ARTIFACT]" -- does not satisfy this criterion if downstream section text contains no per-section repetition. |
| C-20 | **Domain Section Completion Constraint** | structure | aspirational | The domain section header or label carries an explicit forward-reference naming the downstream section it must precede -- e.g., "(POSITIONED BEFORE B3 VERIFY -- complete before writing B3)." This transforms the C-12 positional requirement into a live execution constraint: the instruction cannot be satisfied without writing domain content before advancing to the named downstream section. A domain section that satisfies C-12 by placement alone, without a forward-named completion instruction in its header or label, does not satisfy this criterion. |
| C-21 | **Complete Phase Gate Chain** | structure | aspirational | Every phase transition in the output has a named binary gate as both the output of the preceding phase and the stated prerequisite of the succeeding phase. No ungated phase transitions exist: each phase header or opening instruction names the gate it requires to be OPEN before the phase may be written. A structure with gates at some but not all phase transitions, or a single gate between two phases in a multi-phase output, does not satisfy this criterion. |
| C-22 | **Pre-Seeded Inline Domain Example** | behavior | aspirational | The domain section contains at least one pre-filled worked example as model output text -- not as instruction -- naming a specific table, a column type change (before and after), an operation, and a numeric business threshold (e.g., "Step 3 reduces decimal(19,4) to decimal(10,2) on payment_amount -- charges over $9,999,999.99 silently capped"). The example demonstrates the required specificity rather than instructing the reader to provide it. A domain section that instructs "provide a numeric threshold example" without pre-seeding one does not satisfy this criterion. |
| **C-23** | **Step Registry Phase Encapsulation** | structure | aspirational | The step registry (whether named Q1, STEP REGISTRY, PARSE PHASE, or equivalent) is enclosed in a named phase header, and that phase carries an explicit exit gate state field. The first analytical section's header or opening instruction names that gate as its entry prerequisite -- e.g., "TRACE PHASE (requires PARSE GATE = OPEN)." This closes the structural gap where Q-format registries emit no gate, leaving the registry-to-first-analytical-section transition ungated and causing PARTIAL on C-21. A step registry that appears as a standalone section without a named phase wrapper and exit gate does not satisfy this criterion even if the registry content is otherwise complete. |
| **C-24** | **Intra-Phase-B Gate Chain** | structure | aspirational | Phase B contains at least one named binary gate between two of its internal sub-sections, and the downstream sub-section's header or opening instruction names that gate as its entry prerequisite -- e.g., "B3 VERIFY (requires DOMAIN SYNTHESIS GATE = OPEN)." This extends the C-21 gate chain requirement into the canonical output phase itself. Phase B that contains internal sub-sections (domain, verify, recommendations) without any internal gates does not satisfy this criterion even if the inter-phase gate chain (C-21) is otherwise complete. |
| **C-25** | **Explicit Phase-B Canonical Claim** | structure | aspirational | Phase B's header or first substantive line contains an explicit statement asserting that chronological step ordering (C-05) is satisfied by Phase B alone -- not by any Phase A section. The assertion may take the form "C-05 is satisfied here, not by any Phase A section," "This phase provides the canonical execution-ordered output," or equivalent. An output that satisfies C-16 and C-05 by structure, but whose Phase B header contains no such explicit claim, does not satisfy this criterion. The claim eliminates evaluator ambiguity about the two-phase exception by making the design intent machine-readable at the Phase B entry point. |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 85 | 17 (C-09 to C-25) |
| **Total** | **175** | **25** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80% (140 pts).

---

## Evaluator Notes

*(all v5 notes carried forward, three new notes added)*

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
- **C-19 vs C-18**: C-18 requires the source artifact to be named in citation instructions; C-19 requires that instruction to appear at every analytical section. An output can pass C-18 with a single correctly-named instruction while failing C-19 because remaining sections contain no per-section repetition. Evaluate C-19 by counting sections that lack their own citation instruction, not by checking whether a global citation rule exists.
- **C-20 vs C-12**: C-12 tests whether the domain section is positioned before verification. C-20 tests whether the domain section header explicitly names the section it must precede and instructs completion before advancing. An output that satisfies C-20 automatically satisfies C-12, but not vice versa. The distinguishing signal is the forward-named section in the completion instruction.
- **C-21 vs C-15**: C-15 requires at least one gate. C-21 requires every phase transition to be gated, with each phase header naming its prerequisite gate. Count phase transitions, then count gated transitions -- any gap fails C-21. A two-phase output with one gate satisfies C-15 but fails C-21 if either the Phase A exit gate or the Phase B entry prerequisite is unnamed.
- **C-22 vs C-08**: C-08 requires domain framing in the output; C-22 requires a pre-filled worked example as model output text within the template. The distinction is instruction vs demonstration: C-08 passes if the output contains concrete domain framing; C-22 passes only if the template itself contains a pre-seeded example. An output can satisfy C-08 from correct LLM behavior without C-22 ever being present in the template.
- **C-23 vs C-21** *(new)*: C-21 requires every phase transition to be gated. C-23 specifically targets the registry-to-first-analytical-section gap that Q-format structures leave ungated by default. An output that satisfies C-21 (full chain) automatically satisfies C-23, but the converse is not true. Evaluate C-23 independently: does the registry section have a named phase wrapper AND an exit gate AND does the first analytical section name that gate as its prerequisite? All three conditions required.
- **C-24 vs C-21** *(new)*: C-21 addresses transitions between major phases (Phase A to Phase B, Phase B to VERDICT). C-24 addresses transitions within Phase B's internal sub-sections. These are orthogonal: an output can achieve a complete inter-phase gate chain (C-21 PASS) while Phase B sub-sections are ungated (C-24 FAIL). Count Phase B sub-sections, count internal gates -- any ungated internal transition fails C-24.
- **C-25 vs C-16** *(new)*: C-16 requires Phase B to be labeled as the authoritative output and decoupled from Phase A analytically. C-25 requires Phase B to contain an explicit textual assertion that C-05 chronological ordering is satisfied by Phase B alone. An output can satisfy C-16 by structural decoupling without any explicit claim text in Phase B -- that satisfies C-16 but fails C-25. The evaluator signal is a direct quote or close paraphrase of the canonical claim, not an inference from structure.

---

## v6 Change Log

Three new aspirational criteria added from Round 5 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| V-03 wraps the step registry in PARSE PHASE with its own PARSE GATE. TRACE PHASE header requires "PARSE GATE = OPEN." This closes the Q1->first-analytical-section ungated transition that causes PARTIAL on C-21 in all Q-format variations (V-01, V-02, V-04, V-05). The fix is one addition: a named phase wrapper + exit gate on the registry. | C-23: Step Registry Phase Encapsulation |
| V-05 adds DOMAIN SYNTHESIS GATE between B2 and B3, and VERIFY COMPLETION GATE between B3 and B4. This extends the gate chain into Phase B's internal sections. V-05's multi-gate architecture positively differentiates over V-01/V-04, which have no intra-Phase-B gates. | C-24: Intra-Phase-B Gate Chain |
| V-03 Phase B opens with: "C-05 is satisfied here, not by any Phase A section." This eliminates evaluator doubt about the two-phase exception. Other variations satisfy C-05 by structure but never assert it, leaving the evaluator to infer the design intent rather than read it. | C-25: Explicit Phase-B Canonical Claim |

**Scoring changes:**
- Aspirational tier: 70 pts (14 criteria) -> 85 pts (17 criteria)
- Total max: 160 -> 175
- Golden threshold: unchanged at 80% composite (now 140 pts) + all essential pass
