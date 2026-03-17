# trace-skill Scorecard — Round 11

**Rubric version**: v10 (30 aspirational criteria, denominator 30)
**Variations available**: V-01 only (V-02 through V-05 not provided — scored as single-variation round)

---

## V-01 Criterion Scores

### Essential (C-01–C-05) — 60 pts total

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | All four phases defined in sequence: Gather → Bind → Execute → Verdict |
| C-02 | PASS | Section 1 (Spec Inputs) and Section 2 (Invocation Inputs) enumerate inputs with Name + Source columns |
| C-03 | PASS | Bind Table includes Resolved Value column; every Gather input maps to a single resolved value |
| C-04 | PASS | Relay Schema + delimiter markers instruct complete artifact production |
| C-05 | PASS | Compliance ledger with PASS/FAIL is structurally mandated via C-29 audit block and C-32 population rules |

**Essential**: 5/5 → **60 pts**

---

### Recommended (C-06–C-08) — 30 pts total

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | PASS | Phase Label Schema table emitted before trace content; exact headers `## GATHER` etc. mandated |
| C-07 | PASS | Compliance ledger ID column maps to criterion IDs; ledger is the Verdict mechanism |
| C-08 | PASS | Execute instructs "complete artifact — no elision, no placeholder sections" |

**Recommended**: 3/3 → **30 pts**

---

### Aspirational (C-09–C-38) — 10 pts total

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Coverage Matrix section present with closed-world preamble and CLOSED ASSERTION block |
| C-10 | PASS | Relay Schema defines Role, Signal, Binding, Status — four fields; Verdict reads the ledger |
| C-11 | PASS | Explicit ordering: "spec inputs first, invocation inputs second" |
| C-12 | PASS | BLOCKED rule: "If any Required=YES has Gap=YES, emit DEFECT: OPEN-WORLD-ASSERTION and HALT" |
| C-13 | PASS | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` delimiter markers instructed |
| C-14 | PASS | "Emit this registry BEFORE any trace content begins. It is immutable." |
| C-15 | PASS | Compliance ledger table with ID \| Result \| Evidence implied by C-32 population rules and C-29 audit |
| C-16 | PASS | StatusVocab CLOSED TYPE: RESOLVED / UNRESOLVED / BLOCKED; Status column cites type by name |
| C-17 | PASS | "Conflict Precedence Rule" section with explicit prose declaration |
| C-18 | PASS | Relay Schema Binding field: `` `InputName = "ResolvedValue"` `` — resolved value stated in relay |
| C-19 | PASS | Bind Table column "Precedence applied (PrecedenceVocabulary)" present |
| C-20 | PASS | CLOSED ASSERTION enumerates: "Required inputs covered: [name1], [name2], ..." |
| C-21 | PASS | Anti-pattern row: "Do NOT write input name only — binding pair with resolved value is required" |
| C-22 | PASS | PrecedenceVocabulary CLOSED TYPE declared: override / default / BLOCKED |
| C-23 | PASS | "Coverage Matrix is CLOSED for this invocation." as explicit closure terminus line |
| C-24 | PASS | Anti-pattern row is structurally independent with VIOLATION in Required cell |
| C-25 | PASS | PrecedenceVocabulary CLOSED TYPE; column header "Precedence applied (PrecedenceVocabulary)" cites type |
| C-26 | PASS | "is a named structural mandate (C-26). Reproduce it exactly as shown." — mandated in prompt |
| C-27 | PASS | "RequiredVocabulary (CLOSED TYPE): `YES` \| `VIOLATION`" — two-value closure |
| C-28 | PASS | Uniform `(TypeName)` on all typed columns: Status (StatusVocab), Precedence applied (PrecedenceVocabulary), Required (RequiredVocabulary), Defect code (DefectCodeVocab) |
| C-29 | PASS | Closure terminus violation emits: `DEFECT: OPEN-WORLD-ASSERTION` — named mandate carries defect code |
| C-30 | PASS | Defect Classification Registry declares DefectCodeVocab as CLOSED TYPE; single code enumerated explicitly |
| C-31 | PASS | C-28 audit site table Site 4 lists "Defect code (DefectCodeVocab)"; Registry column "Defect Code (DefectCodeVocab)" — both carry annotation |
| C-32 | PASS | C-29 audit block (a)(b)(c) instructs full ledger self-certification before traversal; PRE-READ GATE enforces (c) |
| C-33 | PASS | `**Independence Statement**:` present and isolated: "Any value outside this vocabulary is a schema error independently detectable without consulting registry rows." |
| C-34 | PASS | "**C-28 COUNT GATE**: IF actual == expected THEN `confirmed` ELSE `mismatch`" — binary self-evaluating gate |
| C-35 | PASS | "**PRE-READ GATE**:" section; "Run phases (a), (b), and (c) BEFORE reading the ledger" — structural ordering mandated |
| **C-36** | **PASS** | STRUCTURAL MANDATE (C-36) block present: "The label `**Independence Statement**:` above is a named structural mandate of this prompt. Reproduce it exactly — as a bolded labeled element structurally isolated from the definition body..." — scorer confirms C-33 by label presence alone |
| **C-37** | **FAIL** | COUNT GATE emits `mismatch` but carries no `DefectCodeVocab`-coded defect citation; `DEFECT: COUNT-MISMATCH` (or equivalent) absent from both the gate block and the DefectCodeVocab registry — gate outcome is not ledger-traceable by defect code |
| **C-38** | **FAIL** | PRE-READ GATE says "HALT and report violation in the ledger" but emits no `DefectCodeVocab`-coded defect; `DEFECT: EMPTY-CELL` (or equivalent) absent from both the gate block and the registry — gate is ordering-only, not defect-emitting |

**Aspirational**: 28/30 → **9.33 pts**

---

## V-01 Composite Score

| Band | Pass | Possible | Pts |
|------|------|----------|-----|
| Essential | 5 | 5 | 60.00 |
| Recommended | 3 | 3 | 30.00 |
| Aspirational | 28 | 30 | 9.33 |
| **Total** | | | **99.33** |

**Golden threshold**: all 5 essential PASS ✓ + composite ≥ 80 ✓ → **GOLDEN**

---

## Excellence Signals — V-01

**Pattern 1 — Inline criterion citation in structural mandate block**: The C-36 mandate block labels itself `STRUCTURAL MANDATE (C-36)` with the criterion ID embedded. This creates bidirectional traceability: the mandate text references its governing criterion, so a scorer can link prompt instruction → criterion → output without table lookup.

**Pattern 2 — Scorer confirmation heuristic in mandate text**: The C-36 block ends with "A scorer confirms C-33 compliance by label presence alone without parsing surrounding definition bullets." Embedding the scoring heuristic in the prompt instruction closes the loop between prompt design and rubric evaluation — the prompt self-documents how compliance is confirmed.

**Pattern 3 — Parallel mandate architecture established**: C-26 (closure terminus) and C-36 (independence statement) now follow identical structural mandate syntax. The pattern is: "> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate... Reproduce it exactly..." This parallelism makes C-37 and C-38 mechanically derivable — both gates need a comparable "> STRUCTURAL MANDATE (C-XX)" block that names the emitted defect code and extends DefectCodeVocab.

---

## Failure Analysis — C-37 and C-38

Both failures share the same root: **DefectCodeVocab is not extended to cover new gate emission sites**. The fix is mechanical and additive:

1. Add `DEFECT: COUNT-MISMATCH` and `DEFECT: EMPTY-CELL` to the Defect Classification Registry table
2. Amend the COUNT GATE: `IF actual == expected THEN confirmed ELSE mismatch → emit DEFECT: COUNT-MISMATCH`
3. Amend the PRE-READ GATE: `If any cell is empty: HALT → emit DEFECT: EMPTY-CELL`
4. Add "> STRUCTURAL MANDATE (C-37)" and "> STRUCTURAL MANDATE (C-38)" blocks following the C-36 pattern

These are the sole deltas between v10 and a hypothetical v11 prompt that would pass all 30 aspirational criteria.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Inline criterion citation in structural mandate block (STRUCTURAL MANDATE (C-XX) labels itself with ID for bidirectional traceability)", "Scorer confirmation heuristic embedded in mandate text (prompt self-documents how compliance is confirmed)", "Parallel mandate architecture established (C-26 and C-36 share identical syntax, making C-37/C-38 mechanically derivable)"]}
```
