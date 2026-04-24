## trace-component — Round 6 Scoring (v6 rubric, 150 pts)

---

### V-01 — Role Sequence: Schema-First (5 roles)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Event chain complete | PASS | TABLE-01 fill rules: every causal hop, dispatch chains show both rows, no implicit jumps, UNKNOWN tokens at gaps |
| C-02 | Component tree traversal | PASS | §2 table with Direction/Carrier Name/Signal Type per hop; every §1 component required |
| C-03 | State delta shown | PASS | §3 Before/After/Selectors; UNKNOWN for undetermined keys |
| C-04 | Re-render list complete | PASS | TABLE-04 fill rules: memoized-skip as NO rows (not absent); Upstream Ref required for every row |
| C-05 | Side effects | PASS | §5 both branches required; MISSING-LOADING / MISSING-ERROR for unconfirmed |
| C-06 | Issue flags | PASS | §6 all four categories; "none detected" must cite specific §4/§5 rows |
| C-07 | Final UI state | PASS | §7 derivation citation from §3 required per item; chain §1→§3→§4→§7 traceable |
| C-08 | Optimization | PASS | §9 at least one entry or explicit "None" citing §4 NO rows — silence prohibited |
| C-09 | Framework-portable annotations | PASS | §8 Framework Notes as designated annotation layer; §1–§7 neutral vocabulary only |
| C-10 | Gap-visible format | PASS | TABLE-01 and TABLE-04 as named schema blocks; structured columns make gaps structurally apparent |
| C-11 | Evidence chaining | PASS | §12 Evidence Chain Audit: §7→§3, §4 Upstream Ref→§2/§3, §5 Upstream Ref→§1 |
| C-12 | Incompleteness tokens | PASS | UNKNOWN / MISSING-LOADING / MISSING-ERROR declared in schemas with fill rules |
| C-13 | Framework-neutral core enforcement | PASS | Active vocabulary binding in Role 4; §11 audits for MAP leaks in §1–§7 |
| C-14 | Vocabulary contract artifact | PASS | Role 2 sole output = §0 PART A + PART B; auditor §11 verifies no leaks |
| C-15 | Machine-readable completeness inventory | PASS | §10 stamp: counts + locations by category; cross-check record required |
| C-16 | PASS-THROUGH designation | PASS | PART B named artifact required; type values declared; no neutral alias for PASS-THROUGH names |
| C-17 | Stamp with active correction | PASS | Re-scan token-by-token; correction notation with before/after + location; cross-check record regardless |
| C-18 | Role-level enforcement gate | **PASS** | Role 3 (Enforcement Gate) is a standalone role whose sole output is GATE-VOCAB result; "Role 4 may not begin until this role outputs GATE-VOCAB: PASS" — named, blocking, separate role; checks planned cell values in TABLE-01/TABLE-04 column space |
| C-19 | Pre-declared named schemas | **PASS** | Role 1 (Schema Architect) sole output is TABLE-01 SCHEMA + TABLE-04 SCHEMA; declared before contract; named blocks with columns, required tokens, fill rules |

**V-01 Score: 150/150 — GOLDEN**

---

### V-02 — Role Sequence: Contract-First (4 roles)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-04 | Essential | PASS | TABLE-01 / TABLE-04 fill rules equivalent to V-01; UNKNOWN tokens at gaps |
| C-05–C-07 | Recommended | PASS | §5 both branches; §6 all four categories with row citations; §7 §3 derivation required |
| C-08–C-10 | Aspirational (format/depth) | PASS | §9 optimization; §8 Framework Notes; named schema blocks in Step 2a/2b |
| C-11–C-12 | Evidence/tokens | PASS | §12 Evidence Chain Audit; UNKNOWN/MISSING-LOADING tokens in schemas |
| C-13–C-14 | Vocabulary contract | PASS | Role 1 Contract Author produces §0 before schemas; §11 audits leaks |
| C-15–C-17 | Stamp/correction | PASS | §10 with active correction protocol and cross-check record |
| C-18 | Role-level enforcement gate | **PARTIAL** | Gate exists (Step 2c, named "GATE-VOCAB", blocks Role 3); but it inspects *column names* of TABLE-01/TABLE-04 schemas ("verify: no column name is a MAP term") rather than planned §1–§7 *cell values*. C-18 requires: "verify that no MAP entry... appears in that section's cell values." Column-name scope is narrower. Gate is named and blocking but does not cover the cell-value space C-18 specifies. |
| C-19 | Pre-declared named schemas | PASS | Step 2a/2b produce TABLE-01 SCHEMA and TABLE-04 SCHEMA as labeled blocks before trace; column names drawn from contract vocabulary |

**V-02 Score: 60 (essential) + 30 (recommended) + 55 (11 aspirational PASS × 5) + 3 (C-18 PARTIAL) = 148/150 — GOLDEN**

---

### V-03 — Phrasing Register: Imperative Checklist + STOP Block

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-04 | Essential | PASS | Steps T-1 through T-4 with explicit PASS/FAIL conditions; TABLE-01/TABLE-04 schemas from PRE-FLIGHT |
| C-05–C-07 | Recommended | PASS | T-5 both branches; T-6 all four categories with row citations; T-7 §3 derivation per item |
| C-08–C-10 | Aspirational (format/depth) | PASS | T-9 optimization; T-8 Framework Notes; P-1/P-2 declare named schema blocks |
| C-11–C-12 | Evidence/tokens | PASS | Step A-4 Evidence Chain Audit; UNKNOWN/MISSING-LOADING tokens in PRE-FLIGHT schemas |
| C-13–C-14 | Vocabulary contract | PASS | Step P-3 produces §0 PART A + PART B before trace checklist; A-3 vocabulary audit |
| C-15–C-17 | Stamp/correction | PASS | A-1 stamp; A-2 active correction protocol with cross-check record |
| C-18 | Role-level enforcement gate | **PASS** | Boxed STOP BLOCK: "GATE-VOCAB — REQUIRED BEFORE PROCEEDING TO TRACE CHECKLIST"; explicitly checks cell values ("verify it will not appear in §1–§7 cell values"); "STOP. Do not begin Step T-1 until this token is output." — named, blocking, checks cell space |
| C-19 | Pre-declared named schemas | **PASS** | PRE-FLIGHT Steps P-1/P-2 produce labeled TABLE-01 SCHEMA and TABLE-04 SCHEMA before trace checklist; FAIL conditions explicitly state "FAIL if: Schema appears inline within §1 content generation; schema is unlabeled" |

**V-03 Score: 150/150 — GOLDEN**

---

### V-04 — Lifecycle Emphasis: Phase-Gated Pipeline

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-04 | Essential | PASS | Phase 4 fills TABLE-01/TABLE-04 from SCHEMAS-ARTIFACT; fill rules inherited |
| C-05–C-07 | Recommended | PASS | §5 both branches; §6 four categories; §7 §3 derivation per item |
| C-08–C-10 | Aspirational (format/depth) | PASS | §9 optimization; §8 Framework Notes; named schema blocks from Phase 1 |
| C-11–C-12 | Evidence/tokens | PASS | §12 Evidence Chain Audit in Phase 5; UNKNOWN/MISSING-LOADING in schemas |
| C-13–C-14 | Vocabulary contract | PASS | Phase 2 produces CONTRACT-ARTIFACT with PART A + PART B; §11 vocabulary audit |
| C-15–C-17 | Stamp/correction | PASS | §10 active correction in Phase 5 with cross-check record |
| C-18 | Role-level enforcement gate | **PASS** | Phase 3 is the standalone Gate Phase; "Phase 4 cannot begin without `GATE-ARTIFACT: PASS`"; gate inspects MAP terms against "§1–§7 cell values… Handler, Owner (TABLE-01), Component, Reason (TABLE-04)"; GATE-ARTIFACT sole output of Phase 3 |
| C-19 | Pre-declared named schemas | **PASS** | Phase 1 (Schema Declaration) sole output = SCHEMAS-ARTIFACT; "No vocabulary mapping, no trace content, no outlines for Phase 2+"; `SCHEMAS-ARTIFACT: COMPLETE` completion token emitted |

**V-04 Score: 150/150 — GOLDEN**

---

### V-05 — Combined: Trace Architecture Fusion + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-04 | Essential | PASS | Role 2 fills TABLE-01/TABLE-04 from TRACE ARCHITECTURE |
| C-05–C-07 | Recommended | PASS | §5 both branches; §6 four categories; §7 §3 derivation per item |
| C-08–C-10 | Aspirational (format/depth) | PASS | §9 optimization; §8 Framework Notes; TABLE-01/TABLE-04 schemas as first two blocks of TRACE ARCHITECTURE |
| C-11–C-12 | Evidence/tokens | PASS | **EVIDENCE CHAIN CONTRACT** (named parallel obligation in TRACE ARCHITECTURE); §12 Evidence Chain Audit in Role 3 explicitly audits against it |
| C-13–C-14 | Vocabulary contract | PASS | TRACE ARCHITECTURE §0 PART A + PART B; Role 3 §11 scans for leaks and alias violations |
| C-15–C-17 | Stamp/correction | PASS | §10 active correction protocol; cross-check record required regardless |
| C-18 | Role-level enforcement gate | **PASS** | GATE-VOCAB embedded as final step of TRACE ARCHITECTURE; checks "planned column value in §1–§7 (Handler/Owner columns and Component/Reason columns)"; `TRACE ARCHITECTURE: SEALED` emitted only after PASS; "Role 2 may not begin until TRACE ARCHITECTURE: SEALED is output" — blocking named gate |
| C-19 | Pre-declared named schemas | **PASS** | TABLE-01 SCHEMA and TABLE-04 SCHEMA are the first two named blocks in TRACE ARCHITECTURE; declared before PART A, PART B, or gate; Role 2 blocked until SEALED |

**V-05 Score: 150/150 — GOLDEN**

---

## Scorecard

| Variation | C-01–04 | C-05–07 | C-08–17 | C-18 | C-19 | Total | Band |
|-----------|---------|---------|---------|------|------|-------|------|
| V-01 | 60/60 | 30/30 | 50/50 | 5/5 | 5/5 | **150/150** | GOLDEN |
| V-02 | 60/60 | 30/30 | 50/50 | 3/5 | 5/5 | **148/150** | GOLDEN |
| V-03 | 60/60 | 30/30 | 50/50 | 5/5 | 5/5 | **150/150** | GOLDEN |
| V-04 | 60/60 | 30/30 | 50/50 | 5/5 | 5/5 | **150/150** | GOLDEN |
| V-05 | 60/60 | 30/30 | 50/50 | 5/5 | 5/5 | **150/150** | GOLDEN |

**Ranking**: V-01 = V-03 = V-04 = V-05 (150) > V-02 (148)

---

## V-02 C-18 Gap (only differentiator)

V-02's gate checks whether schema *column names* contain MAP terms. C-18 requires verification that MAP terms won't appear in §1–§7 *cell values* — the Handler/Owner/Component/Reason values that the Trace Author fills. These are distinct: column names like "Handler", "Timing" are structurally neutral by construction; the cell-value space (function names, component names, neutral equivalents) is where MAP infiltration actually occurs. V-02's gate enforces the wrong scope.

---

## Excellence Signals

Four variations reached the ceiling simultaneously, each with a distinct architecture. The differences that are scorable under existing criteria are nil — all four solve C-18 and C-19. The signal value is in the structural patterns each uses.

**From V-05 — EVIDENCE CHAIN CONTRACT as a named pre-trace obligation**
The citation requirements (§4 Upstream Ref, §5 Upstream Ref, §7 §3 derivation, §6 row citations) are promoted from column instructions into a named contract artifact declared within TRACE ARCHITECTURE, parallel to schemas and vocabulary. Role 2 is bound to this contract as a structural obligation — "Failure to satisfy any of these is a citation gap, not a formatting choice" — not just a "populate the column" instruction. This is functionally analogous to what C-19 did for schemas: turning "use a table with these columns" into a pre-declared named artifact. An EVIDENCE CHAIN CONTRACT does the same for citation obligations.

**From V-04, V-01, V-05 — Named artifact sealing tokens**
Tokens like `SCHEMAS-ARTIFACT: COMPLETE`, `CONTRACT-ARTIFACT: COMPLETE`, `GATE-ARTIFACT: PASS`, `TRACE ARCHITECTURE: SEALED` make phase/role completion machine-readable. The handoff condition is testable: "Phase 4 cannot begin without `GATE-ARTIFACT: PASS`" is a token check, not a prose intention. V-03's STOP block works but relies on visual parsing; token-sealed artifacts create checkable handoff conditions. V-02 and V-03 partially demonstrate this — V-03 requires `[GATE-VOCAB: PASS]` output but doesn't use a sealed artifact pattern for schemas and contract.

---

## New Patterns

The two patterns above are distinct from C-18/C-19 and from each other:

- **Evidence chain as named contract artifact** is a pre-trace structural pattern (parallel to C-19's named schema artifact) that elevates citation requirements from column metadata to a named obligation the generating role is explicitly bound to.
- **Named artifact sealing tokens** are a handoff-enforcement mechanism (distinct from the blocking gate of C-18) that make role/phase completion observable by token presence rather than by prose compliance.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["Evidence chain declared as named pre-trace obligation — citation requirements (Upstream Ref, §3 derivation, §6 row citations) are promoted from column instructions into a named contract artifact (EVIDENCE CHAIN CONTRACT) declared within the architecture phase, binding the generating role to a citation graph as a structural obligation parallel to schemas and vocabulary — making citation gaps non-bypassable rather than column-level oversights", "Named artifact sealing tokens — role and phase completion is marked by machine-readable tokens (SCHEMAS-ARTIFACT: COMPLETE, TRACE ARCHITECTURE: SEALED, GATE-ARTIFACT: PASS) that make handoff conditions testable by token presence rather than prose instruction compliance — distinct from the blocking gate of C-18 which verifies vocabulary; sealing tokens verify completion of the artifact itself"]}
```
