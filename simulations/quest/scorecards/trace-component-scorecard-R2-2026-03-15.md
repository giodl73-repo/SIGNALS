## trace-component — Round 2 Scorecard (v2 Rubric)

**Rubric ceiling**: 110 pts | **Golden threshold**: ≥ 88

---

### Scoring Legend

| Rating | Points (Essential 15 / Recommended 10 / Aspirational 5) |
|--------|----------------------------------------------------------|
| PASS   | Full credit |
| PARTIAL | Half credit |
| FAIL   | 0 |

---

## V-01 — Role Sequence: Citation Auditor

**Mechanism**: Two-role structure. Role 1 (Domain Expert) produces full prose trace. Role 2 (Citation Auditor) verifies every downstream claim cites an upstream identifier and confirms the derivation chain end-to-end.

| ID | Criterion | Rating | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | PASS (15) | Role 1 requires every handler in causal order with dispatch shown; zero implicit entries permitted |
| C-02 | Component tree traversal | PASS (15) | Exact component names, direction, prop/callback names required; no gaps |
| C-03 | State delta shown | PASS (15) | Exact key, before, after, plus derived state identified |
| C-04 | Re-render list complete | PASS (15) | Both re-rendered and skipped components required with named reasons |
| C-05 | Side effects and async | PASS (10) | Three-state accounting with MISSING-LOADING / MISSING-ERROR tokens |
| C-06 | Issue flags present | PASS (10) | All four categories required; Role 2 audits every "no issues" against upstream citations |
| C-07 | Final UI state described | PASS (10) | Role 2 requires every UI element to name its State Delta key; unverifiable elements flagged |
| C-08 | Optimization opportunities | PARTIAL (3) | Optional section present with concrete structure; may be skipped |
| C-09 | Framework-portable annotations | FAIL (0) | No Framework Notes section; role says "use framework vocabulary throughout" — no neutral annotation layer |
| C-10 | Gap-visible format | FAIL (0) | Prose throughout; no tables or numbered enumeration for C-01 or C-04 |
| C-11 | Cross-section evidence chaining | PASS (5) | Role 2 Citation Auditor explicitly requires EC→State Delta→Re-render→UI chain by identifier; derivation check names each link |

**V-01 Score: 98 / 110 — Golden**

---

## V-02 — Output Format: Targeted Tables + Row Citation Protocol

**Mechanism**: Mandatory tables only for C-01 (Event Chain, EC-n rows) and C-04 (Re-render List, RR-n rows). Prose sections required to cite table rows by EC-n / RR-n identifier. Final UI State required to name State Delta keys inline.

| ID | Criterion | Rating | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | PASS (15) | Mandatory table; UNKNOWN permitted, omission not; Dispatches-To column enforces chain |
| C-02 | Component tree traversal | PASS (15) | Prose from EC-1 owner; every handoff with direction and prop/callback name |
| C-03 | State delta shown | PASS (15) | Prose enumeration with exact keys, before/after, derived values |
| C-04 | Re-render list complete | PASS (15) | Mandatory table; every component in affected subtree has a row; both YES/NO with named reasons |
| C-05 | Side effects and async | PASS (10) | Three-state with MISSING tokens; owner cites RR-n; state keys named from State Delta |
| C-06 | Issue flags present | PASS (10) | All four categories required; every finding must cite EC-n, RR-n, or State Delta key — uncited finding is explicitly invalid |
| C-07 | Final UI state described | PASS (10) | Every element must name its State Delta key in parentheses; UI state without traceable key may not appear |
| C-08 | Optimization opportunities | PARTIAL (3) | Optional section present; references RR-n; render reduction asked for |
| C-09 | Framework-portable annotations | PARTIAL (3) | Framework Notes section exists with correct framing ("core trace uses framework-neutral vocabulary"), but role setup says "use framework vocabulary throughout" — contradiction reduces confidence |
| C-10 | Gap-visible format | PASS (5) | Mandatory tables for both C-01 and C-04 — the two sections named by the criterion; row structure makes omissions structurally visible |
| C-11 | Cross-section evidence chaining | PASS (5) | Row-citation protocol (EC-n / RR-n) in Side Effects, Issue Audit; State Delta key citation in Final UI State; derivation chain traceable by row ID throughout |

**V-02 Score: 106 / 110 — Golden**

---

## V-03 — Lifecycle Emphasis: Phase Registry + Consume Protocol

**Mechanism**: Seven phases. Each phase emits a named Registry of identifiers produced. Each downstream phase opens with a "Consuming from Phase N" block that must cite upstream identifiers before the body begins. MISSING tokens flow from Phase 5 into Phase 6.

| ID | Criterion | Rating | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | PASS (15) | Phase 1 body requires every handler in causal order; UNKNOWN allowed, omission not; Registry emits handler names |
| C-02 | Component tree traversal | PASS (15) | Phase 2 unbroken path from Phase 1 starting component; every prop and callback named |
| C-03 | State delta shown | PASS (15) | Phase 3 before/after for every key; derived values with parent key; Registry emits all state keys |
| C-04 | Re-render list complete | PASS (15) | Phase 4 covers every Phase 2 component path component; both re-rendered and skipped with named reasons citing Phase 3 keys |
| C-05 | Side effects and async | PASS (10) | Phase 5 three-state accounting; MISSING tokens emitted to Phase 5 Registry for Phase 6 consumption |
| C-06 | Issue flags present | PASS (10) | Phase 6 consumes Phase 4+5 registries; all four categories; every "no issues" must cite the specific registry entry |
| C-07 | Final UI state described | PASS (10) | Phase 7 completion criterion: every element derives from a Phase 3 key; key must be named for each element |
| C-08 | Optimization opportunities | PARTIAL (3) | Phase 8 optional; consumes Phase 4 YES rows; concrete component + optimization + expected reduction required |
| C-09 | Framework-portable annotations | PARTIAL (3) | Framework Notes optional section with "core trace uses framework-neutral vocabulary"; role setup contradicts ("use framework vocabulary throughout") |
| C-10 | Gap-visible format | FAIL (0) | No tables; Phase 1 and Phase 4 use structured prose with enumeration but no tables or numbered rows; gaps in the body are less structurally visible than a table |
| C-11 | Cross-section evidence chaining | PASS (5) | Consume-from blocks make citation a structural entry condition; Phase 4 cites Phase 3 keys; Phase 7 cites Phase 3 keys; Phase 6 cites Phase 4+5 registries |

**V-03 Score: 101 / 110 — Golden**

---

## V-04 — Combined: Output Format + Lifecycle Emphasis

**Mechanism**: Tables for Phase 1 (Event Chain, EC-n) and Phase 4 (Re-render List, RR-n with Phase 2/3 identifier citations in reason column). Phase registry + consume protocol throughout. Two orthogonal mechanisms target C-10 (tables) and C-11 (phase consume blocks) independently.

| ID | Criterion | Rating | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | PASS (15) | Mandatory table; EC-n rows; Dispatches-To column; UNKNOWN over omission |
| C-02 | Component tree traversal | PASS (15) | Prose from Phase 1 starting component; every hop named with direction and exact prop/callback |
| C-03 | State delta shown | PASS (15) | Prose enumeration; primary keys and derived values; Phase 3 Registry emits all keys |
| C-04 | Re-render list complete | PASS (15) | Mandatory table; every Phase 2 component has RR-n row; YES reason cites Phase 2/3 identifier; NO reason names memoization type |
| C-05 | Side effects and async | PASS (10) | Prose with three-state; owner cites RR-n; MISSING tokens in Phase 5 Registry |
| C-06 | Issue flags present | PASS (10) | Consumes Phase 4+5 registries; all four categories; every finding cites EC-n, RR-n, or Phase 3 key; "no issues" cites registry entries |
| C-07 | Final UI state described | PASS (10) | Consumes Phase 3 registry; each element cited: "The [element] is [state] because `[Phase 3 key]` is now `[value]`"; no uncited UI state permitted |
| C-08 | Optimization opportunities | PARTIAL (3) | Phase 8 optional; consumes Phase 4 YES rows; conditional skip if no unnecessary renders |
| C-09 | Framework-portable annotations | PARTIAL (3) | Framework Notes optional section with framing language; same role-setup contradiction as other variations |
| C-10 | Gap-visible format | PASS (5) | Mandatory tables for Phase 1 and Phase 4 — the two highest-risk sections; table format makes row omissions structurally visible |
| C-11 | Cross-section evidence chaining | PASS (5) | Phase consume blocks as structural entry conditions; EC-n/RR-n citations in downstream prose; Phase 3 key citations in Phase 7; two independent enforcement mechanisms (tables + consume blocks) |

**V-04 Score: 106 / 110 — Golden**

---

## V-05 — Combined: Role Sequence + Phrasing Register

**Mechanism**: Conversational senior-engineer expert voice with explicit Citation Rule constraint applied inline throughout every downstream section. Framework Notes section keeps core trace accessible.

| ID | Criterion | Rating | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | PASS (15) | "Every event handler... in order... exact function name... event type... propagation path" — all required by name |
| C-02 | Component tree traversal | PASS (15) | "Name every component... name every prop and every callback... say whether DOWN or UP" — no generics permitted |
| C-03 | State delta shown | PASS (15) | "Exact state key, value before, value after. Derived state named with before/after" |
| C-04 | Re-render list complete | PASS (15) | Both re-rendered (cite state key) and insulated (name memo/selector) components required |
| C-05 | Side effects and async | PASS (10) | Three-branch walkthrough; citation rule explicitly invoked: state keys must come from State Delta; absent keys = noted gap |
| C-06 | Issue flags present | PASS (10) | All four categories with senior-engineer instincts framing; "uncited 'no issues' is not a valid conclusion" |
| C-07 | Final UI state described | PASS (10) | Citation rule "applies especially strongly": every UI element names its State Delta key by name; model example given |
| C-08 | Optimization opportunities | PARTIAL (3) | Optional "any quick wins?" with expert-specific optimization advice; expected render reduction requested |
| C-09 | Framework-portable annotations | PARTIAL (3) | Framework Notes section: "This keeps the core trace readable for someone who knows components but doesn't know [framework] internals." Framing is clear, but conversational expert voice throughout uses framework-specific idioms |
| C-10 | Gap-visible format | FAIL (0) | No tables or numbered enumeration; prose walkthrough throughout; event chain and re-render list both in prose |
| C-11 | Cross-section evidence chaining | PASS (5) | Citation Rule applied inline at every downstream section; re-renders cite state keys; final UI state cites state keys; issue audit cites handler/component names; derivation chain enforced by constraint rather than structure |

**V-05 Score: 101 / 110 — Golden**

---

## Rankings

| Rank | Variation | Score | Band | C-10 | C-11 |
|------|-----------|-------|------|------|------|
| 1 (tie) | **V-02** (Targeted Tables + Row Citation) | **106/110** | Golden | PASS | PASS |
| 1 (tie) | **V-04** (Tables + Phase Lifecycle) | **106/110** | Golden | PASS | PASS |
| 3 (tie) | V-03 (Phase Registry) | 101/110 | Golden | FAIL | PASS |
| 3 (tie) | V-05 (Conversational + Citation Rule) | 101/110 | Golden | FAIL | PASS |
| 5 | V-01 (Citation Auditor) | 98/110 | Golden | FAIL | PASS |

All five variations are Golden. The ceiling of 110 was not reached by any variation — the remaining 4 pts come from C-08 PARTIAL (−2) and C-09 PARTIAL (−2) across all top performers.

---

## Excellence Signals

**From V-02 and V-04 (joint leaders)**

### Signal 1: Row-ID citation over name-only citation

V-02 introduced `EC-n` / `RR-n` row identifiers as the cross-section reference currency. This is a tighter implementation of C-11 than "cite the component name" because:
- Row IDs are unambiguous even when component names are long or repeated
- A downstream section citing `RR-3` can be audited against the exact table row with no ambiguity
- Row ID gaps are visible in the table itself — if `RR-5` is referenced in an Issue Audit but there is no `RR-5` row, the error is structurally apparent

V-01 uses name-only citation (correct identifier required but no row ID). V-03/V-04/V-05 mix registry names with prose. V-02's row-ID protocol is the most auditable form of C-11.

### Signal 2: Consume-from block as pre-condition, not post-audit

V-03 and V-04 require each phase to open with a "Consuming from Phase N" block that must be populated *before* the phase body begins. This is structurally different from V-01's Role 2 audit:
- V-01: write the trace, then a second role checks citations afterward — the audit can be softened
- V-03/V-04: cite before you write — the phase body cannot begin without naming the upstream identifiers

This pre-condition mechanism converts C-11 from a quality-check to a structural entry gate. V-04 combines this with row-ID tables, giving it two independent C-11 enforcement paths — the highest C-11 confidence of any variation.

### Signal 3: Two orthogonal C-10/C-11 mechanisms in V-04

V-04's specific innovation is that neither mechanism depends on the other:
- If the table rows are complete but the consume-from blocks are sparse, C-10 still passes
- If the consume-from blocks are detailed but a table row is thin, C-11 still passes

This redundancy means a partial model failure on one mechanism doesn't collapse both new criteria. No other variation isolates the two new criteria so cleanly.

---

```json
{"top_score": 106, "all_essential_pass": true, "new_patterns": ["Row-ID citation protocol (EC-n/RR-n) makes cross-section references unambiguous and table-auditable, tighter than name-only citation for C-11", "Consume-from block as phase entry pre-condition converts C-11 from post-hoc audit to structural requirement — stronger than second-role auditor pattern", "Two orthogonal C-10/C-11 mechanisms (table format + phase consume blocks) in V-04 create independent enforcement paths so partial model failure on one does not collapse both new criteria"]}
```
