Written to `simulations/quest/rubrics/trace-migration-rubric-v7-2026-03-14.md`.

---

## What changed: v6 -> v7

Two new aspirational criteria from Round 6 excellence signals:

| New | Closes gap in | Pattern source | What it adds |
|-----|--------------|----------------|--------------|
| **C-26** Terminal Output Gating | C-24 | V-05 RECOMMENDATIONS GATE B4->VERDICT | C-24 minimum (B2->B3) can still exit ungated to VERDICT. C-26 requires the terminal output node itself to carry an entry prerequisite, closing the last structural gap in the gate chain. |
| **C-27** Inertia-Contrast Framing | C-22 | V-05 E-02 inertia framing | C-22 requires a pre-seeded example with table/type/threshold. C-27 additionally requires naming the prior working state and showing how the migration breaks it -- three-part structure: before/condition, after/broken, consequence. |

**Scoring:** 175 -> 185 total max (19 aspirational criteria, 95 pts). Golden threshold 80% = 148 pts.

---

**Key evaluator distinctions:**
- **C-26 vs C-24**: B2->B3 and B3->B4 gates satisfy C-24. C-26 only passes if the VERDICT/terminal node header names an upstream gate as its entry prerequisite.
- **C-27 vs C-22**: C-22 passes without a "before" clause. C-27 requires the explicit prior-working-state named in the example -- the reader must be able to infer the pre-migration state without consulting the schema diff.
B2->B3 and B3->B4 gates can both pass C-24 while B4 exits ungated to VERDICT, failing C-26. The test is whether the terminal node carries an entry prerequisite naming the last B-section's gate.
- **C-27 vs C-22**: C-22 passes with a pre-seeded example naming table, type change, and numeric threshold. C-27 additionally requires naming the working state before the migration ("before Step N, X worked because Y") and showing how the migration breaks that condition. An example that states only the risk and consequence without naming the prior working state passes C-22 but fails C-27. The distinguishing signal is the explicit "before" clause naming the condition that held before the migration.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Before/After State** | correctness | essential | For each changed entity (table, column, constraint, index), the output explicitly shows the state before the migration and the state after. "Changed" includes additions, removals, type changes, nullability changes, and constraint changes. An entity described in generic terms without before/after values does not satisfy this criterion. |
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

## Aspirational Criteria (95 points total)

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
| C-23 | **Step Registry Phase Encapsulation** | structure | aspirational | The step registry (whether named Q1, STEP REGISTRY, PARSE PHASE, or equivalent) is enclosed in a named phase header, and that phase carries an explicit exit gate state field. The first analytical section's header or opening instruction names that gate as its entry prerequisite -- e.g., "TRACE PHASE (requires PARSE GATE = OPEN)." This closes the structural gap where Q-format registries emit no gate, leaving the registry-to-first-analytical-section transition ungated and causing PARTIAL on C-21. A step registry that appears as a standalone section without a named phase wrapper and exit gate does not satisfy this criterion even if the registry content is otherwise complete. |
| C-24 | **Intra-Phase-B Gate Chain** | structure | aspirational | Phase B contains at least one named binary gate between two of its internal sub-sections, and the downstream sub-section's header or opening instruction names that gate as its entry prerequisite -- e.g., "B3 VERIFY (requires DOMAIN SYNTHESIS GATE = OPEN)." This extends the C-21 gate chain requirement into the canonical output phase itself. Phase B that contains internal sub-sections (domain, verify, recommendations) without any internal gates does not satisfy this criterion even if the inter-phase gate chain (C-21) is otherwise complete. |
| C-25 | **Explicit Phase-B Canonical Claim** | structure | aspirational | Phase B's header or first substantive line contains an explicit statement asserting that chronological step ordering (C-05) is satisfied by Phase B alone -- not by any Phase A section. The assertion may take the form "C-05 is satisfied here, not by any Phase A section," "This phase provides the canonical execution-ordered output," or equivalent. An output that satisfies C-16 and C-05 by structure, but whose Phase B header contains no such explicit claim, does not satisfy this criterion. The claim eliminates evaluator ambiguity about the two-phase exception by making the design intent machine-readable at the Phase B entry point. |
| **C-26** | **Terminal Output Gating** | structure | aspirational | The final output node -- VERDICT, CONCLUSION, SUMMARY, or equivalent -- is preceded by a named binary gate from the last Phase B sub-section, and that final node's header or opening instruction names the gate as its entry prerequisite -- e.g., "VERDICT (requires RECOMMENDATIONS GATE = OPEN)." This closes the terminal exit gap left open when C-24's minimum gate chain (B2->B3) does not extend through B4. A Phase B that satisfies C-21 and C-24 but allows the final output node to be written without an upstream gate resolution does not satisfy this criterion. The complete gate-reachable structure runs from the registry phase through every Phase B sub-section to the terminal output node with no ungated exit. |
| **C-27** | **Inertia-Contrast Framing** | behavior | aspirational | At least one domain example (in the domain section or any Phase A question) names the working state before the migration step: the specific condition that held before the migration and made the relevant business process function correctly. The example then shows how the migration breaks that condition and states the concrete consequence. The required three-part structure is: (a) "before Step N, [process] worked because [condition]," (b) "after Step N, [condition] no longer holds because [migration change]," (c) "[specific business consequence, numeric or named]." An example that states risk and consequence without naming the prior working state -- even if it satisfies C-22 -- does not satisfy this criterion. Anchoring in the broken prior state forces cause-level reasoning rather than effect-level description. |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 95 | 19 (C-09 to C-27) |
| **Total** | **185** | **27** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80% (148 pts).

---

## Evaluator Notes

*(all v6 notes carried forward, two new notes added)*

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
- **C-23 vs C-21**: C-21 requires every phase transition to be gated. C-23 specifically targets the registry-to-first-analytical-section gap that Q-format structures leave ungated by default. An output that satisfies C-21 (full chain) automatically satisfies C-23, but the converse is not true. Evaluate C-23 independently: does the registry section have a named phase wrapper AND an exit gate AND does the first analytical section name that gate as its prerequisite? All three conditions required.
- **C-24 vs C-21**: C-21 addresses transitions between major phases (Phase A to Phase B, Phase B to VERDICT). C-24 addresses transitions within Phase B's internal sub-sections. These are orthogonal: an output can achieve a complete inter-phase gate chain (C-21 PASS) while Phase B sub-sections are ungated (C-24 FAIL). Count Phase B sub-sections, count internal gates -- any ungated internal transition fails C-24.
- **C-25 vs C-16**: C-16 requires Phase B to be labeled as the authoritative output and decoupled from Phase A analytically. C-25 requires Phase B to contain an explicit textual assertion that C-05 chronological ordering is satisfied by Phase B alone. An output can satisfy C-16 by structural decoupling without any explicit claim text in Phase B -- that satisfies C-16 but fails C-25. The evaluator signal is a direct quote or close paraphrase of the canonical claim, not an inference from structure.
- **C-26 vs C-24** *(new)*: C-24 requires at least one named binary gate between Phase B sub-sections (minimum B2->B3). C-26 requires the terminal output node -- VERDICT, CONCLUSION, or equivalent -- to be explicitly gated from the last Phase B sub-section. An output with B2->B3 and B3->B4 gates satisfies C-24 but fails C-26 if B4 exits to VERDICT without a named gate. The distinguishing check: does the VERDICT/terminal node header name an upstream gate as its entry prerequisite?
- **C-27 vs C-22** *(new)*: C-22 requires a pre-seeded worked example naming table, type change, and numeric threshold. C-27 requires the example to also name the prior working state -- the condition that held before the migration and made the business process function -- and show how the migration breaks that condition. An example satisfying C-22 ("Step 3 reduces decimal(19,4) to decimal(10,2) -- charges over $9,999,999.99 silently capped") fails C-27 if it omits the "before" clause ("before Step 3, payment processing correctly represented amounts up to $999,999,999,999.9999 because decimal(19,4)"). The test: can the reader infer the specific pre-migration working state from the example without consulting the schema diff?

---

## v7 Change Log

Two new aspirational criteria added from Round 6 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| V-05 adds RECOMMENDATIONS GATE B4->VERDICT with VERDICT requiring it OPEN. Complete chain: PARSE->TRACE->DOMAIN->OPERATIONAL->VERIFY->B1->DOMAIN SYNTHESIS GATE->B3->VERIFY COMPLETION GATE->B4->RECOMMENDATIONS GATE->VERDICT. Every node gate-reachable, no node writable without resolving all upstream gates. V-05 is the sole Round 6 variation where the terminal output node itself is gated -- a property no other variation achieves. | C-26: Terminal Output Gating |
| V-05 frames domain examples as: "Before Step N, [business process] worked because [condition]. After Step N, [condition] no longer holds because [migration change]. The consequence is [numeric or named failure]." This inertia-contrast structure anchors domain reasoning in a named working state rather than abstract risk categories. Pre-seeded specificity at Phase A flows naturally because the baseline is already defined; Phase B synthesis then inherits the causal chain rather than reconstructing it from effect descriptions. | C-27: Inertia-Contrast Framing |

**Scoring changes:**
- Aspirational tier: 85 pts (17 criteria) -> 95 pts (19 criteria)
- Total max: 175 -> 185
- Golden threshold: unchanged at 80% composite (now 148 pts) + all essential pass
