## Scoring — org-build R12 / Rubric v8

---

### Scoring Key

| Symbol | Weight |
|--------|--------|
| PASS | 1.0 |
| PARTIAL | 0.5 |
| FAIL | 0.0 |

Formula: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/20 × 10)`

---

## V-01 — Role Sequence: Inertia-Advocate First

### Essential (5/5)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 5a: ASCII diagram with box-drawing chars, min 2 levels, headcount per area |
| C-02 | PASS | All five fields required in every role file; IA fields named explicitly |
| C-03 | PASS | Dedicated Phase 3 writes all IA files before any other role; enforced by construction |
| C-04 | PASS | Phase 1: "T1-DEPTH-FLAG = standard → MUST enumerate 20–30; deep → MUST enumerate 50+" |
| C-05 | PASS | Phase 5b: Area, Headcount, Key Roles, Decides, Escalates; "MUST be populated for every row" |

### Recommended (3/3)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | `.craft/roles/{area-slug}/` — min 2 area subdirs by construction |
| C-07 | PASS | Phase 5e: 3+ rhythm rows; charter with all 5 fields; Quorum as "N of M" fraction |
| C-08 | PASS | Phase 5d: `FLAT-CASE-PRESSURE:` + `VERDICT:` closed-set lines; generic prose FORBIDDEN |

### Aspirational (20 criteria)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 5f: Row 1 = headcount threshold; Row 2 = different category; two headcount rows forbidden |
| C-10 | PASS | Phase 5g: "every 'Why It Applies Here' cell MUST open with `[element name] (cat-N) —`" |
| C-11 | PASS | Phase 3 `scope` field keyed to T2-IA-TEMPLATE-KEY from Phase 2; templates declared before writing |
| C-12 | PASS | Phase 5g: category selection derives from T2-VERDICT with MUST/FORBIDDEN per path |
| C-13 | PASS | Phase 2: "FORBIDDEN: writing both. FORBIDDEN: omitting both and leaving verdict blank." |
| C-14 | PASS | Named typed outputs at each gate (T1-DEPTH-FLAG, T2-VERDICT, …); consuming phases list them by name |
| C-15 | PASS | Bidirectional guard present: both "both" and "neither" are explicitly FORBIDDEN |
| C-16 | PASS | Phase 5g: "Every Mitigation cell MUST contain a specific remediation action. FORBIDDEN: format guidance." |
| C-17 | PASS | Phase 3: "Apply verbatim. Copy the exact template text. No paraphrase. No adaptation." |
| C-18 | PASS | Phase 5g: CAN-OPERATE-FLAT → MUST cat-3/cat-2, FORBIDDEN cat-1/cat-4; inverse for STRUCTURE-WARRANTED |
| C-19 | PARTIAL | "Scan the repo to discover…", "Evaluate:", "Name the specific concern" — task instructions use plain imperative not MUST; constraint statements mostly MUST/FORBIDDEN but not universally |
| C-20 | PASS | Each gate names typed outputs; Phase 2 entry: "T1-AREA-COUNT and T1-AREA-LIST are the binding inputs"; downstream phases reference by name |
| C-21 | PARTIAL | T3-AREAS-COVERED/T3-AREAS-MISSING not explicitly constrained with MUST/FORBIDDEN in Phase 4 input contract; "IA files already exist — do not overwrite" is implicit FORBIDDEN rather than declared |
| C-22 | FAIL | No pre-print skeleton with named `___` slots keyed to gate variables; record block templates use `[…]` fill notation only |
| C-23 | PASS | Per-boundary outbound FORBIDDENs at Phases 1–5 end: "FORBIDDEN: proceeding to Phase N+1 before emitting record block" |
| C-24 | PASS | `=== RECORD: PHASE-N ===` block materializes every named gate variable after each phase |
| C-25 | PASS | Inbound FORBIDDENs at every consuming phase entry ("FORBIDDEN: executing Phase N before Phase N-1 record block is emitted") + outbound FORBIDDENs at every gate |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field inside every record block; single construct yields gate schema + ordering anchor + materialized checkpoint |
| C-27 | PASS | Phase 1: explicit conditional — "T1-DEPTH-FLAG = standard → MUST enumerate 20–30; deep → MUST enumerate 50+"; FORBIDDEN flat range without binding |
| C-28 | PASS | Every `=== RECORD: PHASE-N ===` opens with `PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins before this block is emitted.` as first named field |

**Aspirational points: 17 + 0.5 + 0.5 = 18.0 / 20**

**V-01 Score: (5/5 × 60) + (3/3 × 30) + (18.0/20 × 10) = 60 + 30 + 9.0 = 99.0**

---

## V-02 — Output Format: Scan-Record-Driven Flat Structure

### Essential (5/5)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Section 1: ASCII diagram, box-drawing chars, headcount per area |
| C-02 | PASS | Five fields listed for each role type |
| C-03 | PASS | Phase 3: inertia-advocate written first per area before standard/specialized |
| C-04 | PASS | Phase 1: "MUST generate 20–30 / 50+ role files total" bound to T1-DEPTH-FLAG |
| C-05 | PASS | Phase 4 Section 2: all 5 columns; "Decides and Escalates MUST be populated for every row. Empty cells fail." |

### Recommended (3/3)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Area subdirectory structure present |
| C-07 | PASS | Phase 4 Section 5: 3+ rows; charter with Purpose/Owner/Quorum/Inputs/Outputs; "FORBIDDEN: Quorum without 'of M' denominator" |
| C-08 | PASS | Phase 4 Section 4: FLAT-CASE-PRESSURE and VERDICT labeled lines; closed-set values only |

### Aspirational (20 criteria)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 4 Section 6: Row 1 headcount type; Row 2 must differ |
| C-10 | PASS | Phase 4 Section 7: `[element name] (cat-N) —` syntax MUST; FORBIDDEN T2-FORBIDDEN-CAT |
| C-11 | PASS | IA scope keyed to T2-IA-TEMPLATE-KEY; verbatim copy required |
| C-12 | PASS | Phase 2 anti-pattern rule table: derives REQUIRED-CAT and FORBIDDEN-CAT from T2-VERDICT |
| C-13 | PASS | Phase 2: "FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts." |
| C-14 | PASS | Typed named outputs per gate; consuming phases declare "Input contract: consumes T1-…, T2-… from prior record blocks" |
| C-15 | PASS | Bidirectional: "FORBIDDEN: writing both" + "FORBIDDEN: omitting both" |
| C-16 | PASS | "Every Mitigation cell MUST contain a remediation action, not format guidance." |
| C-17 | PASS | "Copy the T2-IA-TEMPLATE-KEY template text VERBATIM. No changes. No paraphrase." |
| C-18 | PASS | Explicit REQUIRED-CAT and FORBIDDEN-CAT emitted in Phase 2 record block; Phase 4 Section 7 enforces them |
| C-19 | PARTIAL | "Score the org on four pressure dimensions" and "Derive composite T2-PRESSURE" use non-MUST instructional forms; "Emit the scan findings as inline observations" is advisory |
| C-20 | PASS | Systematic: each gate names outputs; consuming phases list input contracts with "Input contract: consumes …" |
| C-21 | PARTIAL | Some gate variables consumed by bulk "from prior record blocks" without per-variable MUST/FORBIDDEN binding; T3-LENS-UNIQUE not constrained in consuming phase with explicit FORBIDDEN |
| C-22 | FAIL | No pre-print skeleton; SCAN-FINDINGS block is inline observation, not a named-slot template |
| C-23 | PASS | Global outbound rule at header: "FORBIDDEN: beginning any phase before emitting the prior phase's record block"; FORBIDDEN per-boundary in Phase 1 instruction |
| C-24 | PASS | Named record blocks materialize typed variables after each phase |
| C-25 | PARTIAL | Global outbound FORBIDDEN covers all phases but is not per-boundary at each gate; inbound FORBIDDENs are per-boundary. C-25 requires both directions at each boundary individually — global rule fails the per-gate specificity test |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field; record block unifies gate schema, ordering anchor, and materialized checkpoint |
| C-27 | PASS | Phase 1: "Depth-flag role count binding (MUST be stated here, in this phase)"; FORBIDDEN deferring or stating flat range without condition |
| C-28 | PASS | Every record block opens with `PHASE-ORDERING-GUARD: FORBIDDEN: Phase N begins before this block is emitted.` |

**Aspirational points: 16 + 0.5 + 0.5 + 0.5 = 17.5 / 20**

**V-02 Score: (5/5 × 60) + (3/3 × 30) + (17.5/20 × 10) = 60 + 30 + 8.75 = 98.75**

---

## V-03 — Lifecycle Emphasis: Strict Sequential Gates with Double-Guard

### Essential (5/5)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Section 1: ASCII diagram, min 2 levels |
| C-02 | PASS | All five fields required for every role type |
| C-03 | PASS | Phase 3: inertia-advocate first per area; FORBIDDEN two IA files with identical lens/expertise |
| C-04 | PASS | Phase 1: "T1-DEPTH-FLAG = standard → MUST write 20–30; deep → MUST write 50+; FORBIDDEN flat count without condition" |
| C-05 | PASS | Phase 4 Section 2: all 5 columns; "Decides and Escalates MUST be populated. Empty cells fail." |

### Recommended (3/3)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Area subdirectory structure |
| C-07 | PASS | Phase 4 Section 5: charters with all 5 fields; "FORBIDDEN: Quorum without 'of M' denominator" |
| C-08 | PASS | Phase 4 Section 4: labeled FLAT-CASE-PRESSURE + VERDICT lines |

### Aspirational (20 criteria)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | "Row 1 MUST be headcount type. Row 2 MUST be a different type." |
| C-10 | PASS | `[element name] (cat-N) —` syntax required; FORBIDDEN wrong cats; FORBIDDEN format-guidance mitigations |
| C-11 | PASS | IA scope keyed to T2-IA-TEMPLATE-KEY; Phase 3 scope MUST be verbatim copy |
| C-12 | PASS | Anti-pattern derivation from T2-VERDICT: CAN-OPERATE-FLAT → cat-3/cat-2; STRUCTURE-WARRANTED → cat-1/cat-4 |
| C-13 | PASS | "VERDICT GUARD: FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither verdict. Only one verdict. Both is an error. Neither is an error." |
| C-14 | PASS | Named typed outputs at each gate; consuming phases declare "Consume T1-…, T2-…, T3-…" by name |
| C-15 | PASS | Bidirectional: "Both is an error. Neither is an error." + FORBIDDEN both directions explicitly |
| C-16 | PASS | "Mitigation MUST be a remediation action, not format guidance" |
| C-17 | PASS | "MUST be verbatim copy of T2-IA-TEMPLATE-KEY template. No paraphrase." + "FORBIDDEN: paraphrasing the T2-IA-TEMPLATE-KEY scope template." |
| C-18 | PASS | "MUST use cat-3, cat-2. FORBIDDEN: cat-1, cat-4." and inverse — explicit FORBIDDEN per verdict path |
| C-19 | PARTIAL | Phase 3: "For each area in T1-AREA-LIST, write: inertia-advocate → standard roles → specialized roles." — not MUST. Phase 4 chart-writing instruction: "Write org-chart.md with these seven sections" — imperative without MUST. Non-MUST task instructions remain in non-constraint positions |
| C-20 | PASS | Systematic: each gate declares typed outputs; consuming phases list them in "Consume…" input contracts |
| C-21 | PARTIAL | T3-SCOPE-VERBATIM and T3-LENS-UNIQUE consumed at Phase 5 VERIFY via "Consume all T1–T4 record block fields" — bulk reference, not per-variable MUST/FORBIDDEN binding in the consuming phase header |
| C-22 | PASS | Pre-print skeletons with named `___` slots before every record block: `T1-DEPTH-FLAG: ___`, `T1-ROLE-TARGET: ___`, etc. — slots keyed to gate variable names; fill step precedes formal `=== RECORD ===` emission |
| C-23 | PASS | Per-boundary outbound FORBIDDENs: "Outbound rule: FORBIDDEN: beginning Phase N+1 before Phase N record block is emitted." at every gate |
| C-24 | PASS | Named `=== RECORD: PHASE-N ===` blocks materialize all typed variables after each phase |
| C-25 | PASS | Every boundary: "Outbound rule: FORBIDDEN: beginning Phase N+1…" AND "Inbound rule: FORBIDDEN: executing Phase N+1 before Phase N record block is emitted." — bidirectional, per-boundary |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field inside record block; block is the single artifact yielding gate schema + ordering anchor + checkpoint |
| C-27 | PASS | Phase 1: flag-conditioned count floor bound inside phase instruction; "FORBIDDEN: writing a flat count range without its T1-DEPTH-FLAG condition attached." |
| C-28 | PASS | Every `=== RECORD: PHASE-N ===` opens with PHASE-ORDERING-GUARD as named first field |

**Aspirational points: 18 + 0.5 + 0.5 = 19.0 / 20**

**V-03 Score: (5/5 × 60) + (3/3 × 30) + (19.0/20 × 10) = 60 + 30 + 9.5 = 99.5**

---

## V-04 — Role Sequence + Inertia Framing (Combination)

### Essential (5/5) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 5: 7-section org-chart.md including ASCII diagram |
| C-02 | PASS | Five fields required with MUST; FORBIDDEN generic framing |
| C-03 | PASS | Dedicated Phase 3 for all IA files across all areas before Phase 4 |
| C-04 | PASS | Phase 1: "T1-DEPTH-FLAG = standard → MUST write 20–30; deep → MUST write 50+" |
| C-05 | PASS | Phase 5 Section 2: all 5 columns; "Decides and Escalates MUST be populated per row." |

### Recommended (3/3) — PASS all

### Aspirational (20 criteria)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 5 Section 6: Row 1 headcount; Row 2 different type |
| C-10 | PASS | `[element name] (cat-N) —` syntax; FORBIDDEN T2-FORBIDDEN-CAT; MUST remediation action |
| C-11 | PASS | Templates pre-declared as `IA-SCOPE-TEMPLATES:` named artifact in Phase 2 before any file written; ACTIVE-KEY + ACTIVE-TEMPLATE named explicitly |
| C-12 | PASS | ANTI-PATTERN-RULE block in Phase 2 gives explicit derivation rationale: "CAN-OPERATE-FLAT selects cat-2/cat-3 because flat org failure modes are coordination theater and span inflation — not authority vacuums (cat-1)…" |
| C-13 | PASS | Phase 2: "Only one verdict. Both is an error. Neither is an error." + FORBIDDEN both directions |
| C-14 | PASS | Named typed outputs; consuming phases declare input contracts naming those variables |
| C-15 | PASS | Bidirectional guard: "FORBIDDEN: writing both… FORBIDDEN: omitting both" |
| C-16 | PASS | Phase 5 Section 7: "Mitigation MUST be a remediation action." |
| C-17 | PASS | Phase 3: "scope: MUST be verbatim copy of ACTIVE-TEMPLATE text. Verbatim. No edits. No paraphrase. Copy-paste only." |
| C-18 | PASS | ANTI-PATTERN-RULE block: "REQUIRED-CATS / FORBIDDEN-CATS" explicitly per verdict; Phase 5 Section 7 enforces MUST/FORBIDDEN per category set |
| C-19 | PARTIAL | Phase 1: "Scan the repo or scan-results. Discover all areas…" not MUST. Phase 3: "Write one inertia-advocate file for every area…" not MUST. Some task instructions remain in plain imperative |
| C-20 | PASS | Systematic gate declarations; consuming phases list "Consume…" by name |
| C-21 | PARTIAL | T2-TEMPLATES-DECLARED consumed in Phase 3 input contract but its constraint binding reads "MUST copy ACTIVE-TEMPLATE text verbatim" — the variable itself is not wrapped with a per-variable MUST/FORBIDDEN; implicit rather than explicit binding |
| C-22 | FAIL | No pre-print skeleton with `___` slots; no fill-then-emit step preceding record blocks |
| C-23 | PASS | Per-boundary outbound FORBIDDENs: "FORBIDDEN: beginning Phase N before emitting [Phase N-1 record block]" at every gate |
| C-24 | PASS | Named `=== RECORD: PHASE-N ===` blocks materialize all gate variables |
| C-25 | PASS | Every boundary has both outbound FORBIDDEN (at gate end) and inbound FORBIDDEN ("Inbound rule: FORBIDDEN: executing Phase N before Phase N-1 record block is emitted.") |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field inside every record block |
| C-27 | PASS | Phase 1 count floor binds standard → 20–30, deep → 50+ inside phase instruction |
| C-28 | PASS | Every record block opens with PHASE-ORDERING-GUARD as first named field |

**Aspirational points: 17 + 0.5 + 0.5 = 18.0 / 20**

**V-04 Score: (5/5 × 60) + (3/3 × 30) + (18.0/20 × 10) = 60 + 30 + 9.0 = 99.0**

---

## V-05 — Phrasing Register + Lifecycle Emphasis (Combination)

### Essential (5/5) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4: "MUST write org-chart.md with all seven sections. FORBIDDEN: omitting any section." Section 1 = ASCII diagram |
| C-02 | PASS | "MUST include all five fields" per role type; FORBIDDEN generic framing |
| C-03 | PASS | Phase 3: "Inertia-advocate — MUST write one per area. FORBIDDEN: skipping any area." |
| C-04 | PASS | Phase 1 DEPTH-FLOOR-DECLARATION block: "T1-DEPTH-FLAG = standard → MUST write 20–30; deep → MUST write 50+"; FORBIDDEN flat range without condition; FORBIDDEN deferring to later phase |
| C-05 | PASS | Phase 4 Section 2: "MUST include columns: Area, Headcount, Key Roles, Decides, Escalates. MUST populate Decides and Escalates for every row. FORBIDDEN: empty Decides or Escalates cells." |

### Recommended (3/3) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Area subdirectory structure; MUST per-area |
| C-07 | PASS | Phase 4 Section 5: "Quorum MUST be expressed as 'N of M'. FORBIDDEN: Quorum as bare number or percentage." Charter fields all required |
| C-08 | PASS | Phase 4 Section 4: "MUST include FLAT-CASE-PRESSURE line. MUST include VERDICT line. FORBIDDEN: generic prose verdict without labeled lines." |

### Aspirational (20 criteria)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | "Row 1 MUST have type: headcount. Row 2 MUST have a different type. FORBIDDEN: two rows of the same type." |
| C-10 | PASS | "Every 'Why It Applies Here' cell MUST open with `[element name] (cat-N) —`. FORBIDDEN: cells that do not open with this syntax." |
| C-11 | PASS | IA scope template table declared in Phase 2; "Phase 3 MUST copy T2-IA-TEMPLATE verbatim into every IA file scope field" |
| C-12 | PASS | Phase 2: "T2-VERDICT = CAN-OPERATE-FLAT → MUST use cat-3, cat-2. FORBIDDEN: cat-1, cat-4. T2-VERDICT = STRUCTURE-WARRANTED → MUST use cat-1, cat-4. FORBIDDEN: cat-2, cat-3." |
| C-13 | PASS | "Only one verdict. Both is an error. Neither is an error." + FORBIDDEN both directions |
| C-14 | PASS | Named typed outputs at every gate; every consuming phase opens with "MUST consume T1-…, T2-…" naming variables |
| C-15 | PASS | "FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. FORBIDDEN: omitting both verdicts and leaving T2-VERDICT blank." |
| C-16 | PASS | "Every Mitigation cell MUST contain a remediation action. FORBIDDEN: Mitigation cells containing format guidance or descriptive column instructions." |
| C-17 | PASS | "scope: MUST be T2-IA-TEMPLATE copied verbatim. FORBIDDEN: any paraphrase or adaptation." |
| C-18 | PASS | Explicit REQUIRED/FORBIDDEN categories per verdict; Phase 4 Section 7: "Category MUST be drawn from T2-REQUIRED-CAT. FORBIDDEN: using any category in T2-FORBIDDEN-CAT." |
| C-19 | PASS | Global imperative register rule declared upfront: "Every constraint in every phase MUST use MUST or FORBIDDEN. FORBIDDEN: using 'should', 'prefer', 'typically', 'consider', 'may', 'might', 'can'…" — variation delivers on this throughout: "MUST identify", "MUST score four pressure dimensions", "MUST write role files", "MUST write org-chart.md", "MUST append to org-chart.md", "MUST run each check" |
| C-20 | PASS | Every gate names typed outputs; every consuming phase header declares "MUST consume T1-…, T2-…" with variable names |
| C-21 | PASS | Global MUST/FORBIDDEN register + "MUST consume" input contracts mean every named gate variable binding at a consuming phase is governed by MUST or FORBIDDEN. Phase 6 VERIFY: "MUST run each check" covers all prior gate variables |
| C-22 | FAIL | No pre-print skeleton; DEPTH-FLOOR-DECLARATION is a constraint declaration block, not a named-slot fill template; record blocks use `[…]` notation only |
| C-23 | PASS | Per-boundary outbound: "Outbound: FORBIDDEN: beginning Phase N+1 before Phase N record block is emitted." at every gate |
| C-24 | PASS | Named `=== RECORD: PHASE-N ===` blocks materialize all typed gate variables after each phase |
| C-25 | PASS | "Every phase boundary carries two orthogonal FORBIDDENs: Outbound… Inbound… Both FORBIDDENs MUST be observed. Observing only one direction is a build error." — executed per-boundary throughout |
| C-26 | PASS | PHASE-ORDERING-GUARD as first named field inside every record block |
| C-27 | PASS | Phase 1 DEPTH-FLOOR-DECLARATION: flag-conditional count floors inside phase instruction; FORBIDDEN flat range without condition; FORBIDDEN deferring |
| C-28 | PASS | Every `=== RECORD: PHASE-N ===` block opens with `PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins before this block is emitted.` as named first field |

**Aspirational points: 19.0 / 20 (only C-22 fails)**

**V-05 Score: (5/5 × 60) + (3/3 × 30) + (19.0/20 × 10) = 60 + 30 + 9.5 = 99.5**

---

## Rankings

| Rank | Variation | Score | Aspirational | Key delta |
|------|-----------|-------|-------------|-----------|
| **1** | **V-03** | **99.5** | 19.0/20 | C-22 PASS (pre-print skeletons); C-25 PASS (per-boundary double-guard) |
| **1** | **V-05** | **99.5** | 19.0/20 | C-19 PASS (full MUST/FORBIDDEN); C-21 PASS (constraint-completeness) |
| 3 | V-01 | 99.0 | 18.0/20 | C-22 FAIL; C-19/C-21 PARTIAL |
| 3 | V-04 | 99.0 | 18.0/20 | C-22 FAIL; C-19/C-21 PARTIAL; strongest C-12 derivation prose |
| 5 | V-02 | 98.75 | 17.5/20 | C-22 FAIL; C-25 PARTIAL (global outbound rule, not per-boundary) |

---

## Excellence Signals from V-03 and V-05

**From V-03 (C-22 winner):**
- Pre-print skeleton as a distinct fill-then-emit step before each record block. The skeleton uses `fieldname: ___` notation (named slots) so the variable identity is preserved. A reader seeing only the skeleton can infer the full gate schema without reading the record block template. This is the C-26 structural unification property expressed at a lower level — the skeleton is the draft artifact; the record block is the finalized artifact.

**From V-05 (C-19/C-21 winner):**
- Global imperative register header declared before Phase 1. Rather than relying on per-phase MUST/FORBIDDEN discipline, V-05 declares the rule universally upfront and then executes it consistently: every task instruction uses MUST (not plain imperative "write" or "score"), every prohibition uses FORBIDDEN. This eliminates the gap where task descriptions look imperative but lack the MUST keyword C-19 requires.
- MUST consume in consuming-phase headers. Where other variations write "Input contract: consumes T1-AREA-LIST, T1-AREA-COUNT from Phase 1 record block" (imperative), V-05 writes "MUST consume T1-AREA-LIST, T1-AREA-COUNT" — the consumption itself is under MUST, making C-21 binding unambiguous.

**Common to both top variations:**
- Per-boundary double-guard at every phase transition (not global-only) — each gate boundary has an explicit outbound FORBIDDEN naming the next phase, and each consuming phase has an explicit inbound FORBIDDEN naming the prior phase's record block.
- DEPTH-FLOOR-DECLARATION / explicit phase-1 depth binding as its own labeled sub-block, not inline prose — makes the C-27 compliance structurally visible without reading surrounding text.

---

```json
{"top_score": 99.5, "all_essential_pass": true, "new_patterns": ["global-imperative-register-header: declaring all cross-cutting MUST/FORBIDDEN rules as a named section before Phase 1 rather than distributing them per-phase — produces uniform C-19 coverage without per-phase discipline", "amend-section-as-structured-output: a dedicated post-build phase that emits an AMEND section with concrete substituted values (actual area slugs, depth, verdict) for amendment operations — not currently tested by any criterion"]}
```
