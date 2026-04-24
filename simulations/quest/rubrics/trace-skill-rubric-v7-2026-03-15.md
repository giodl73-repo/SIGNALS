Reading the V-01/V-02/V-03 PASS patterns against C-24/C-25/C-26, each reveals a third-generation upgrade axis — from *structurally self-contained* to *schema-normalized*:

- **V-01**: C-24 PASS means the Required column now carries two semantically distinct values (YES / VIOLATION) — an implicit multi-value field. The natural next step: declare it as a closed vocabulary, the same way C-22 closed the Precedence applied column.
- **V-02**: C-25 PASS introduces `(TypeName)` annotation in a column header — a reusable convention. Applied to one column, it's an improvement; applied uniformly across all typed columns, it becomes a schema-wide self-description pattern.
- **V-03**: C-26 PASS names the defect as "structural defect" (prose). The natural upgrade: assign a formal defect classification, making violations citable in the Verdict compliance ledger by code rather than paraphrased.

Three new criteria: C-27 (C-24 upgrade), C-28 (C-25 upgrade), C-29 (C-26 upgrade). Aspirational denominator: 18 → 21.

---

# trace-skill Rubric v7

**5 Essential** (all must pass, 60 pts total):

| ID   | Criterion                                                                 | Category    |
|------|---------------------------------------------------------------------------|-------------|
| C-01 | Four phases present in sequence: Gather, Bind, Execute, Verdict           | format      |
| C-02 | Gather enumerates all inputs by name with source                          | correctness |
| C-03 | Bind maps every Gather input to a single resolved value                   | correctness |
| C-04 | Execute produces target skill artifact with correct naming and sections   | behavior    |
| C-05 | Verdict declares explicit PASS/FAIL with rationale                        | correctness |

**3 Recommended** (30 pts total):

| ID   | Criterion                                                                 | Category    |
|------|---------------------------------------------------------------------------|-------------|
| C-06 | Phases carry exact schema labels (Gather/Bind/Execute/Verdict)            | format      |
| C-07 | Verdict cites criterion IDs, not free-form prose                          | depth       |
| C-08 | Artifact complete — no elision markers anywhere                           | correctness |

**21 Aspirational** (10 pts total):

| ID   | Criterion                                                                                                                                                                                                                      | Category  |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| C-09 | Gather includes Coverage Matrix table with closed-world preamble                                                                                                                                                              | coverage  |
| C-10 | Execute relays carry (role, signal, binding, status) evidence fields; Verdict reads, not reconstructs                                                                                                                         | depth     |
| C-11 | Gather enumerates spec inputs before invocation inputs                                                                                                                                                                        | ordering  |
| C-12 | Coverage Matrix includes explicit BLOCKED declaration: any Gap=YES halts the trace immediately, no partial runs                                                                                                                | coverage  |
| C-13 | Execute wraps artifact with delimiter markers (`[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]`) for unambiguous extraction                                                                                                  | format    |
| C-14 | A pre-trace Phase Label Schema table (immutable) declares all four phase headers before any trace content begins — enforces C-06 structurally                                                                                 | format    |
| C-15 | Verdict is a structured compliance ledger table (columns: ID \| Result \| Evidence) rather than prose — stronger than C-07's criterion-ID citation                                                                            | depth     |
| C-16 | Bind rows carry an explicit three-value Status enum: RESOLVED / UNRESOLVED / BLOCKED — resolution state is unambiguous without inference                                                                                      | depth     |
| C-17 | Bind declares an explicit conflict precedence rule: when spec value and invocation value disagree, the rule resolves which wins (e.g., spec anchors)                                                                          | depth     |
| C-18 | Relay rows carry explicit `` `InputName = "ResolvedValue"` `` binding pairs — resolution value is stated in the relay itself, so Verdict can verify binding without re-inspecting the Bind table                              | depth     |
| C-19 | Bind table carries a "Precedence applied" column — per-row annotation of which conflict rule resolved each binding, making rule application traceable at row level                                                            | depth     |
| C-20 | Coverage Matrix carries a CLOSED assertion that names each Required=YES input explicitly — the enumerated closed-world is the structural gate-pass for C-12                                                                   | coverage  |
| C-21 | Relay Schema carries an explicit anti-pattern prohibition ("Do NOT write input name only" or equivalent) — makes the `InputName = "ResolvedValue"` format requirement actively enforced rather than passively declared (C-18) | depth     |
| C-22 | "Precedence applied" column declares a closed three-value vocabulary (override / default / BLOCKED) — vocabulary closure prevents ambiguous annotation values and makes the column self-validating (C-19)                     | depth     |
| C-23 | CLOSED ASSERTION block terminates with an explicit closure declaration line ("Coverage Matrix is CLOSED for this invocation." or equivalent) — formal terminus makes the closed-world claim self-evidencing (C-20)            | coverage  |
| C-24 | Relay Schema anti-pattern prohibition is a structurally independent row with `VIOLATION` in the Required column — independently citable without parsing the Format cell, structural isolation rather than inline embedding (C-21) | depth |
| C-25 | Conflict precedence vocabulary is declared as a named type (`PrecedenceVocabulary` or equivalent); the "Precedence applied" column header cites the type by name — column is self-validating via type reference, not by proximity to the declaration (C-22) | depth |
| C-26 | Closure terminus line is a labeled structural mandate in the prompt (not emergent from model depth) — the line appears as an instructed, named element so it is reproduced reliably rather than inferred from context (C-23) | coverage |
| **C-27** | **Relay Schema Required column declares a closed two-value vocabulary (`YES` \| `VIOLATION`) — vocabulary closure makes row type (compliance vs prohibition) independently identifiable without sub-table name inspection, upgrading C-24 from structurally isolated to self-validating (C-24)** | depth |
| **C-28** | **Type annotations in column headers follow a uniform convention (`ColumnName (TypeName)`) applied consistently to all typed columns in the schema — uniform annotation makes the schema self-describing without external type registry lookup, upgrading C-25 from single-column typing to schema-wide typing (C-25)** | depth |
| **C-29** | **Named structural mandates (per C-26) carry a formal defect classification for violations (e.g., `DEFECT: OPEN-WORLD-ASSERTION`) — defect classifications are citable in the Verdict compliance ledger by defect class rather than paraphrased, upgrading C-26 from mandated to classified (C-26)** | coverage |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/21 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v7 change note: Added C-27, C-28, C-29 from Round 7 excellence signals. Each is a third-generation precision upgrade along the schema-normalization axis — from self-contained to schema-consistent:*

| R6 | R7 | Upgrade axis |
|----|-----|-------------|
| C-24: anti-pattern row structurally independent (own sub-table + VIOLATION in Required) | C-27: Required column declares closed vocabulary (`YES` \| `VIOLATION`) — row type self-validating without sub-table name | row self-contained → row vocabulary typed |
| C-25: vocabulary given named type; column header cites type | C-28: type annotation convention `(TypeName)` applied uniformly to all typed columns | single column typed → schema-wide typing |
| C-26: terminus line is labeled structural mandate | C-29: mandate carries formal defect classification, citable by code in Verdict ledger | terminus mandated → violation classified |

*Aspirational denominator updated from 18 to 21.*
