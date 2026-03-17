Scorecard written. Summary:

| Rank | V | Score |
|------|---|-------|
| 1 | V-02, V-04, V-05 | **108** — ceiling (tie) |
| 2 | V-01 | 103 |
| 3 | V-03 | 97 |

**What separated the field:**
- V-01 (sub-phase decomposition) passes C-16 via PHASE 6 bracketed gate blocks but fails C-17 — field blocks have no column headers, so mechanism (2) of the triple lock is structurally impossible
- V-03 (imperative prohibition) fails C-13 and C-16 — naming the same strings as "doesn't pass" in prose is not equivalent to a `[GATE: ...]` block
- V-02/V-04/V-05 all achieve 108 because table FINDINGS format preserves column headers, enabling all three triple-lock mechanisms simultaneously

```json
{"top_score": 108, "all_essential_pass": true, "new_patterns": ["Sub-phase FINDINGS decomposition and triple-lock FINDINGS are architecturally incompatible: converting FINDINGS to per-finding field blocks satisfies C-16 gate coverage per column type but eliminates the column-header embedding mechanism required for C-17; table FINDINGS format is required for triple-lock, making the two structural approaches mutually exclusive within the same FINDINGS section", "Gate-block formalism is not substitutable by imperative prohibition: explicitly naming prohibited strings as does-not-pass in prose instructions provides zero structural equivalence to a bracketed GATE block -- V-03 names the same escape strings that V-02 gates but fails both C-13 and C-16, confirming that enforcement format is an independent structural property from which strings are named"]}
```
s | YES | YES | YES | YES | YES |

### Ranking

| Rank | V | Score | Key wins | Key misses |
|------|---|-------|----------|------------|
| 1 | V-02, V-04, V-05 | 108 -- ceiling | C-16 + C-17 both pass | -- |
| 2 | V-01 | 103 | C-16 via PHASE 6 sub-phase gates | C-07 partial; C-17 fail (no column headers in field-block FINDINGS) |
| 3 | V-03 | 97 | C-12, C-14 from Phase 4 | C-07 partial; C-13 fail; C-16 fail; C-17 fail |

### Key findings

C-16 discrimination: V-01 (sub-phase decomposition) passes via PHASE 6C bracketed gate block.
V-02 (dual-column gate) passes via single FINDINGS GATE block covering both column families.
V-03 (imperative prohibition) fails -- prose "doesn't pass" statements are not gate blocks.
Gate-block formalism is not substitutable by imperative prose.

C-17 structural ceiling: V-01 field-block FINDINGS has mandatory fields + gate (mechanisms 1+3)
but no column headers (mechanism 2 absent). Sub-phase decomposition forecloses header-embedding.
V-02/V-04/V-05 use table FINDINGS -- column headers enable all three mechanisms co-present.
Sub-phase FINDINGS and triple-lock FINDINGS are architecturally incompatible.

New patterns confirmed:
1. Sub-phase FINDINGS decomposition and triple-lock FINDINGS are architecturally incompatible.
2. Gate-block formalism is not substitutable by imperative prohibition.

### C-16 Evidence

V-01 PASS: PHASE 6C GATE: "Writing no impact does not close DO-NOTHING COST SURVEY. Writing minor issue does not close DO-NOTHING COST SURVEY. Writing low risk does not close DO-NOTHING COST SURVEY." PHASE 6A GATE also intercepts "may have performance issues", "could cause issues", "might affect users."
V-02 PASS: FINDINGS GATE covers Do-nothing cost ("no impact", "minor issue", "low risk", "no user-facing consequence") AND Problem column ("may have performance issues", "could cause issues", "might affect users", "potential re-render problem"). Single gate block, 8+ strings.
V-03 FAIL: No bracketed FINDINGS GATE block. Imperative "doesn't pass" statements are prose, not gate format. No interception of "no impact"/"minor issue"/"low risk" in FINDINGS.
V-04 PASS: FINDINGS GATE names "no impact", "minor issue", "low risk", "no user-facing consequence", "no production risk" for Do-nothing cost column. Five strings.
V-05 PASS: FINDINGS GATE covers Problem column (5 strings) and Do-nothing cost column (4 strings). Most complete in R4. Closes R3 V-05 gap where "may have performance issues" could still clear FINDINGS.

### C-17 Evidence

V-01 FAIL: Field-block FINDINGS has (1) mandatory Do-nothing cost requirement + (3) PHASE 6C gate, but (2) column-header embedding absent. Field labels are not column headers. Two of three mechanisms; triple lock incomplete.
V-02 PASS: Do-nothing cost column -- (1) N/A-prohibited in setup block; (2) constraint embedded in column header cell; (3) FINDINGS GATE names "no impact"/"minor issue"/"low risk" as non-closers for that column. All three co-present.
V-03 FAIL: Field-block FINDINGS, no column headers, no gate for Do-nothing cost strings. Zero mechanisms co-present on any FINDINGS column.
V-04 PASS: Do-nothing cost column -- (1) "MANDATORY -- N/A is not allowed"; (2) constraint in column header cell; (3) FINDINGS GATE names weak strings for that column. All three co-present.
V-05 PASS: Problem column -- (1) "MANDATORY -- N/A is not allowed"; (2) constraint in column header cell; (3) FINDINGS GATE names "may have performance issues"/"could cause issues" for Problem column. Do-nothing cost column also carries all three. C-17 satisfied via both columns.

### Excellence Signals from V-02, V-04, V-05

Signal 1: Dual-column gate is sufficient. A single FINDINGS GATE block covering both column families achieves C-16 without sub-section decomposition.
Signal 2: Triple lock is column-agnostic. V-04 targets Do-nothing cost; V-05 targets Problem column. Both achieve C-17.
Signal 3: Sub-phase FINDINGS and triple-lock FINDINGS are architecturally incompatible. Table format enables both C-16 and C-17; sub-phase format enables only C-16.
Signal 4: Imperative prohibition fails two criteria that gate-block formalism passes. Same strings, wrong format, fails C-13 and C-16.

```json
{"top_score": 108, "all_essential_pass": true, "new_patterns": ["Sub-phase FINDINGS decomposition and triple-lock FINDINGS are architecturally incompatible: converting FINDINGS to per-finding field blocks satisfies C-16 gate coverage per column type but eliminates the column-header embedding mechanism required for C-17; table FINDINGS format is required for triple-lock, making the two structural approaches mutually exclusive within the same FINDINGS section", "Gate-block formalism is not substitutable by imperative prohibition: explicitly naming prohibited strings as does-not-pass in prose instructions provides zero structural equivalence to a bracketed GATE block -- V-03 names the same escape strings that V-02 gates but fails both C-13 and C-16, confirming that enforcement format is an independent structural property from which strings are named"]}
```
