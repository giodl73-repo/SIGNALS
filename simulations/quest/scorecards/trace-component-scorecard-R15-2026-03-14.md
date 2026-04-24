# trace-component — Round 15 Scoring

## Rubric Applied: v15 (170 pts, 48 criteria)

### Shared Baseline Assessment (all variations)

**Essential (C-01–C-05): all PASS across all variations**
All five share TABLE-1 through TABLE-6 with mandatory non-blank columns, GATE blocks, and traversal T-ID accounting. 60 pts each.

**Recommended (C-06–C-08): all PASS across all variations**
TABLE-5 zero-effects row, TABLE-7 five-category structure with N/A prohibited, FRAMEWORK DECLARATION header. 30 pts each.

**Aspirational Shared:**

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-09 Fix Recommendations | PASS | TABLE-7 Fix column with named APIs |
| C-10 Render Quantification | PASS | TABLE-4 `Yes (N)` co-located with Necessary verdict |
| C-11 Inline Phase-Close Gates | PASS | GATE-1 through GATE-7 with exact-phrase sets |
| C-12 Mandatory Comparison Column | PASS | TABLE-8 "Satisfying Schema Field" maps criterion→field per row, all rows populated |
| C-13 Exact-Phrase Gate Family | PASS | 3+ distinct escape strings across GATE-1/GATE-3/GATE-7 |
| C-14 Column-Header Escape Instruction | PASS | `Necessary? [Yes — reason / No — reason]`, `Finding [issue or "none detected — [reason]"]` |
| C-15 Do-Nothing Cost | PASS | TABLE-7 Do-Nothing Cost column |
| C-16 FINDINGS Section Gate | PASS | GATE-7 intercepts "no impact", "minor issue", "low risk", "no concerns found" |
| C-17 Triple Structural Lock | PASS | TABLE-7: mandatory column + header constraint + GATE-7 exact-phrase block |
| C-18 Table Format for Triple Lock | PASS | TABLE-7 uses column headers |
| C-19 Gate-Block Formalism | PASS | All gates in `[GATE-N: ...]` blocks |
| C-20 Framework Declaration Gate | PASS | FRAMEWORK DECLARATION header required before MANIFEST-1 |
| **C-21 Failure Mode Displacement** | **FAIL** | GATE blocks prevent bad phrases; no explicit "NOT 'state updates' — Owner: X" displacement text produced in output |
| C-22 Re-render Necessity Annotation | PASS | TABLE-4 `Necessary? [Yes — reason / No — reason]` per row |
| C-23 Four-Phase UI Progression | PASS | TABLE-6 four rows: pre-action, synchronous, async success, async error |
| C-24 Zero-Mutation Declaration | PASS | ZERO MUTATION DECLARATION block in TABLE-3 |
| C-25 Issue Category Completeness | PASS | TABLE-7 five mandatory rows covering render/re-renders/accessibility/async/memory |
| C-26 Unnecessary Re-render Promotion | PASS | F-02 UR cross-ref with PROMOTION BLOCK |
| C-27 Mutation Count Pre-Declaration | PASS | `Mutations: N=___ direct, M=___ inherited (total: ___)` |
| C-28 Per-Hop Direction Annotation | PASS | Direction cell per TABLE-2 row |
| C-29 Re-render Inventory by Traversal | PASS | "Every T-ID from TABLE-2 must appear" |
| C-30 Mutation Count Dual-Track | PASS | Direct/inherited separation in pre-declaration |
| C-31 Schema-Field Coverage | PASS | TABLE-8 maps C-20–C-29 to schema fields; ≥7 criteria covered |
| C-32 Blank-Blocked Field Primacy | PASS | TABLE-1 through TABLE-6 provide blank-blocked enforcement for all five essential criteria |
| C-33 Phase-Level Completeness Manifest | PASS | MANIFEST-1–5 each carry: components in scope, state keys, side effects (3 required fields; 5 phases) |
| C-34 Inert Pass-Through Explicit Marking | PASS | INERT-HOP DECLARATION block; explicit `no-op` or null-confirmed notation |
| C-35 Criteria Audit Cross-Validation Table | PASS | TABLE-8: C-01 through C-08 mapped to satisfying field with PASS/FAIL; 8 criteria covered |
| C-36 Inert-as-Default Direction Schema | PASS | All versions: Direction column label places default/null first, departure codes named as alternatives |
| C-37 Manifest-Analysis Paired Block Structure | PASS | 5 MANIFEST-N/TABLE-N adjacent pairs in all versions |
| C-39 Self-Authored Schema Constraint | PASS | Model produces TRAVERSAL-SCHEMA from blank slot; no pre-filled template |
| C-40 Dual-Constraint Placeholder | PASS | All Area 3 instructions explicitly require content + positional constraint in single instruction |
| C-41 Schema Causal Explanation Requirement | PASS | All versions ask WHY the close-line must occupy the terminal position before schema authorship |
| C-42 Anti-Reproduction Schema Authorship | PASS | Blank authorship slot + explicit no-reproduction instruction in all versions |
| C-43 Mutual-Constraint Entanglement Declaration | PASS | All versions require causal derivation of joint-necessity declaration within placeholder body |
| C-45 Dual-Requirement Count Declaration | PASS | All versions require count declaration as opening element (Q3-A / Q4 / DQ-4 / Q8 / DQ-6) |

**Shared aspirational base:** 34 PASS × 2 = 68 pts; 1 FAIL (C-21) = 0 pts

---

## Variable Criteria by Variation

### C-38 · Manifest-Close Adjacency Marker

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PARTIAL | Manifest slots close with `*[...verbatim, as this manifest's last line. Reproduce now.]*` — establishes terminal position but no explicit "TABLE-N begins immediately below" text in the manifest slot itself |
| V-02 | PARTIAL | Same pattern as V-01 |
| V-03 | PARTIAL | Same pattern |
| V-04 | PARTIAL | Same pattern |
| V-05 | **PASS** | Every manifest slot explicitly states: "This is the last content line of MANIFEST-N. TABLE-N header follows directly below." — the adjacency prohibition is embedded in the manifest slot as written text |

### C-44 · Numbered Constraint Enumeration in Placeholder

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | Schema Area 3 requires "enumerate each obligation as a labeled item" — Q3-B on "independently addressable label" reliably derives numbered `(1)...(2)...` form |
| V-02 | PASS | Area 3 Q2 asks "What structural property makes each requirement independently addressable?" — answer: numbered items; schema derives from answer |
| V-03 | PASS | DQ-2 asks "What structural property... makes partial satisfaction of one obligation... structurally visible?" — derives independent labeling |
| V-04 | PASS | "question 6 determines the enumeration form" — Q6 on independent addressability yields numbered items |
| V-05 | PASS | DQ-4 explicitly asks to distinguish cases (a) neither, (b) one, (c) both — requires independently addressable items; "DQ-4 determines enumeration form" |

### C-46 · Epistemic-Register Question Framing

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PARTIAL | Q2-1 through Q2-3 pass the substitution test (epistemic). Q3-A fails: "Why must the count appear before the obligations are read?" — "count" names the schema artifact implicitly |
| V-02 | PASS | All Area 2 and Area 3 questions pass substitution test. Q3 example: "What structural property makes each requirement independently addressable?" — does not name a schema field |
| V-03 | PARTIAL | NQ questions are fully epistemic. DQ-4: "What structural element should appear as the placeholder's opening to establish the number of distinct obligations?" — "opening element" is borderline; does not name "count declaration" directly but implies structural position |
| V-04 | PASS | All 8 CAUSAL PHASE questions pass substitution test. Q8: "What information about the instruction's scope should the agent know before reading the instruction's body?" — no schema field named |
| V-05 | PASS | All 12 questions (NQ-1–NQ-6, DQ-1–DQ-6) pass substitution test. DQ-6 strongest: "what information at the instruction's opening determines the agent's epistemic frame for how many distinct satisfaction targets must be met?" — derivation required |

### C-47 · Causal-Completion Gate Before Schema Authorship

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | CAUSAL PHASE (questions only) → explicit `CAUSAL PHASE CLOSE` paragraph → SCHEMA PHASE (blank slot as distinct section header) — structural document boundary present |
| V-02 | FAIL | Questions and schema authorship both within ROLE 1 Area 3 section. "Having answered all four questions, design the complete close-line placeholder" is advisory ordering, not a structural phase boundary |
| V-03 | FAIL | NULL REGISTER, DEPARTURE REGISTER, and placeholder design all within Area 3 of a single ROLE 1 section — no structural phase separation |
| V-04 | PASS | Same structure as V-01: CAUSAL PHASE → explicit `CAUSAL PHASE CLOSE` → SCHEMA PHASE as distinct document section |
| V-05 | PASS | CAUSAL PHASE (NULL REGISTER + DEPARTURE REGISTER) → `DEPARTURE REGISTER CLOSE` → SCHEMA PHASE opens as subsequent distinct section heading — boundary enforced by register-close structure |

### C-48 · Null-Hypothesis Register in Causal Question Set

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | FAIL | Q3-A/Q3-B/Q3-C address only departure properties. No null-register questions. No explicit NULL/DEPARTURE register labels |
| V-02 | PARTIAL | Q1 ("epistemic status of the structural space... before any structural rule has been applied") addresses the null case. Q2–Q4 address departure properties. Sequential ordering present but no explicit register labels or register-close markers |
| V-03 | PASS | Explicit `NULL REGISTER` block (NQ-1/NQ-2/NQ-3) + `NULL REGISTER CLOSE` paragraph + explicit `DEPARTURE REGISTER` block (DQ-1/DQ-2/DQ-3/DQ-4) + `DEPARTURE REGISTER CLOSE` paragraph — two labeled sequential registers with structural close markers |
| V-04 | PARTIAL | Q4–Q5 address null state ("epistemically correct characterization of its occupancy state"); Q6–Q8 address departure properties. Natural ordering but no explicit register labels or close markers |
| V-05 | PASS | Explicit `NULL REGISTER` (NQ-1–NQ-6, covering both traversal-hop null and manifest-adjacency null) + `NULL REGISTER CLOSE` + `DEPARTURE REGISTER` (DQ-1–DQ-6) + `DEPARTURE REGISTER CLOSE` — dual-domain null coverage with full register structure |

---

## Composite Scores

```
Base score (shared):
  Essential      60
  Recommended    30
  Aspirational   68   (34 PASS × 2; C-21 FAIL)
  ─────────────────
  Subtotal      158
```

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-38 | 1 | 1 | 1 | 1 | 2 |
| C-44 | 2 | 2 | 2 | 2 | 2 |
| C-46 | 1 | 2 | 1 | 2 | 2 |
| C-47 | 2 | 0 | 0 | 2 | 2 |
| C-48 | 0 | 1 | 2 | 1 | 2 |
| **Variable total** | **6** | **6** | **6** | **8** | **10** |
| **COMPOSITE** | **164/170** | **164/170** | **164/170** | **166/170** | **168/170** |

---

## Ranking

| Rank | Variation | Score | R15 criteria earned |
|------|-----------|-------|---------------------|
| 1 | **V-05** | **168/170** | C-46 PASS · C-47 PASS · C-48 PASS |
| 2 | **V-04** | **166/170** | C-46 PASS · C-47 PASS · C-48 PARTIAL |
| 3 | **V-01** | **164/170** | C-46 PARTIAL · C-47 PASS · C-48 FAIL |
| 3 | **V-02** | **164/170** | C-46 PASS · C-47 FAIL · C-48 PARTIAL |
| 3 | **V-03** | **164/170** | C-46 PARTIAL · C-47 FAIL · C-48 PASS |

---

## Excellence Signals from V-05

**Signal 1 — Phase Contract at manifest OPEN creates bidirectional manifest framing.**
V-05 adds a `Phase Contract` block before the manifest body that forward-declares the dual-constraint obligation at phase entry. Every manifest now has two enforcement points: the Phase Contract at open (entry declaration) and the DUAL-CONSTRAINT BLOCK at close (exit enforcement). V-01 through V-04 enforce only at close. Bidirectional framing means the model encounters the obligation count before writing the manifest body, not only at the terminal line.

**Signal 2 — Role 2 references CAUSAL PHASE question numbers by label.**
V-05's Role 2 instruction explicitly names the source question for each placeholder property: "Opening element derives from DQ-6... enumeration derives from DQ-4... entanglement derives from DQ-5." Violating the placeholder now contradicts specifically named reasoning steps, not just prior structural output. V-04 says "you derived the placeholder from epistemic reasoning" without naming which questions; V-05 names them, closing the escape path where a model could argue the placeholder wasn't definitively derived from a specific question.

**Signal 3 — NULL REGISTER covers both traversal hops and manifest adjacency in a single register.**
V-03 covers only manifest adjacency null (NQ-1–NQ-3). V-05's NULL REGISTER covers traversal-hop null (NQ-1–NQ-3) AND manifest-adjacency null (NQ-4–NQ-6) in a single unified register, establishing the null baseline for both structural objects before departure reasoning begins for either. NQ-6 explicitly draws the parallel: "In what structural sense are the two null states parallel epistemic objects?" — this cross-domain null unification is the mechanism that enables the unified null-hypothesis epistemology in the trace body.

**Signal 4 — Null-hypothesis framing extended to FINDINGS table.**
V-05 TABLE-7 header states: "a finding is a confirmed departure from the warranted null — not an observation, not a concern, not a risk." This reframes the findings criterion from enumeration coverage (V-01–V-04 pass C-25 by requiring 5 categories) to epistemic standard: a finding must meet the null-departure threshold, not just appear as a populated row. F-02 in V-05: "none — no unsupported re-render claims in TABLE-4" frames the null finding as a verified null claim, not an absence.

---

## Verdict on C-21 (Failure Mode Displacement) — Persistent Gap

C-21 is FAIL across all five variations. Every variation uses GATE blocks to intercept bad phrases but none requires the model output to explicitly produce displacement text ("NOT 'state updates' — Owner: X, Key: Y"). This gap has persisted since R5. It represents a structural tension: the gate-block formalism (C-19) and the table schema (C-32) together prevent the bad phrases from appearing in the output, but neither produces the explicit "blocked phrase → replacement" text C-21 requires. A variation targeting C-21 would need to require something like a DISPLACEMENT BLOCK at each gate that names the intercepted phrase and the required replacement form. This is a candidate R16 single-axis variation.

---

```json
{"top_score": 168, "all_essential_pass": true, "new_patterns": ["Phase Contract at manifest open creates bidirectional manifest framing — entry declaration before body, exit enforcement at terminal line", "Role 2 references CAUSAL PHASE questions by label (DQ-6, DQ-4, DQ-5) — placeholder violation contradicts specifically named reasoning steps, not just prior structural output", "Single NULL REGISTER covering both traversal-hop null and manifest-adjacency null before departure reasoning for either — dual-domain null unification enables cross-domain epistemic coherence", "Null-hypothesis framing extended to FINDINGS table — a finding is a confirmed departure from the warranted null, not an observation; the null finding is a verified null claim"]}
```
