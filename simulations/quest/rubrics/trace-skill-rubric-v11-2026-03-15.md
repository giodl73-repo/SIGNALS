Reading the Round 11 scorecard, three excellence signals each define a new upgrade axis — from *self-citing* to *self-scoring* to *parallel-by-contract*:

- **R11 / Pattern 1**: V-01 demonstrates `STRUCTURAL MANDATE (C-36)` with the criterion ID embedded in the block header — scorer can navigate from prompt instruction to rubric criterion bidirectionally without table lookup. Natural upgrade of C-36: the inline criterion citation is itself declared as a required element of every structural mandate block, upgrading from named-structural-mandate to self-citing-structural-mandate.
- **R11 / Pattern 2**: V-01 closes the C-36 mandate block with "A scorer confirms C-33 compliance by label presence alone without parsing surrounding definition bullets." The scoring heuristic is embedded in the prompt, making compliance confirmation self-documenting. Natural upgrade of C-39: the scorer confirmation heuristic is a required element of every structural mandate block, upgrading self-citing to self-scoring.
- **R11 / Pattern 3**: C-26 and C-36 now follow identical `STRUCTURAL MANDATE (C-XX)` syntax — the parallelism makes C-37 and C-38 fixes mechanically derivable. Natural upgrade: the canonical mandate template is declared explicitly so all blocks conform by contract rather than by practice, making any new mandate structurally checkable against a single declared form.

Three new criteria: C-39 (Pattern 1), C-40 (Pattern 2), C-41 (Pattern 3). Aspirational denominator: 30 → 33.

---

# trace-skill Rubric v11

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

**33 Aspirational** (10 pts total):

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
| C-27 | Relay Schema Required column declares a closed two-value vocabulary (`YES` \| `VIOLATION`) — vocabulary closure makes row type (compliance vs prohibition) independently identifiable without sub-table name inspection, upgrading C-24 from structurally isolated to self-validating (C-24) | depth |
| C-28 | Type annotations in column headers follow a uniform convention (`ColumnName (TypeName)`) applied consistently to all typed columns in the schema — uniform annotation makes the schema self-describing without external type registry lookup, upgrading C-25 from single-column typing to schema-wide typing (C-25) | depth |
| C-29 | Named structural mandates (per C-26) carry a formal defect classification for violations (e.g., `DEFECT: OPEN-WORLD-ASSERTION`) — defect classifications are citable in the Verdict compliance ledger by defect class rather than paraphrased, upgrading C-26 from mandated to classified (C-26) | coverage |
| C-30 | `DefectCodeVocab` is declared as a closed type in the Defect Classification Registry with all defect codes enumerated — the same vocabulary-closure discipline applied to `RequiredVocabulary` by C-27 propagates to `DefectCodeVocab`, making every named type in the schema closed-typed and self-enumerating rather than open-ended (C-27) | depth |
| C-31 | C-28's uniform `(TypeName)` annotation convention propagates to all typed columns introduced by composed criteria — the Defect Classification Registry's code column and the Verdict compliance ledger's defect code column both carry `(DefectCodeVocab)` annotation; the C-28 audit block tracks total annotation site count to confirm composed-column coverage (C-28) | depth |
| C-32 | Verdict compliance ledger `Defect code` column is fully populated: every row carries a value — FAIL rows cite a `DefectCodeVocab` code, PASS rows carry `--` as an explicit sentinel; a C-29 audit block at Verdict top confirms (a) registry present before Stage 1, (b) all FAIL citations drawn from `DefectCodeVocab`, (c) no empty cells — ledger is self-certifying without re-inspecting the registry (C-29) | coverage |
| C-33 | The `DefectCodeVocab` closed-type declaration includes an explicit independence statement — "any value outside this vocabulary is a schema error independently detectable without consulting registry rows" (or equivalent) — making the closed type validation-independent: compliance can be checked at the point of annotation without registry lookup, upgrading C-30 from vocabulary-closed to self-validating-at-annotation (C-30) | depth |
| C-34 | The C-28 annotation-site count assertion resolves to an explicit PASS/FAIL binary verdict ("confirmed / mismatch" or equivalent) keyed to count match — the audit block is self-evaluating rather than a tally requiring external judgment; the count confirmation is the gate, not a reported number, upgrading C-31 from composed-columns-counted to count-as-gate (C-31) | depth |
| C-35 | The C-32 empty-cell check (check c of the C-29 audit block) is structurally ordered before ledger reading — declared as a named pre-read gate so violations are caught before traversal begins, not discovered mid-ledger; a prompt instruction makes this ordering a structural requirement rather than emergent, upgrading C-32 from fully-populated + self-certified to pre-read-gated + structurally-ordered (C-32) | coverage |
| C-36 | The `**Independence Statement**:` label within the `DefectCodeVocab` type declaration is declared as a named structural mandate in the prompt (paralleling C-26's closure terminus instruction) — the label is an instructed, named element reproduced reliably rather than inferred from model context; a scorer confirms C-33 compliance by label presence alone without parsing surrounding definition bullets, upgrading C-33 from independence-statement-present to independence-statement-mandated (C-33) | depth |
| C-37 | The `**C-28 COUNT GATE**:` block carries a formal defect classification for gate failure — when the IF/THEN resolves to `mismatch`, the gate emits a `DefectCodeVocab`-coded defect citation (e.g., `DEFECT: COUNT-MISMATCH`) independently citable in the Verdict compliance ledger by defect code rather than by gate-block description; gate outcomes are ledger-traceable, upgrading C-34 from self-evaluating to defect-emitting (C-34) | depth |
| C-38 | The `**PRE-READ GATE**:` carries a formal defect classification for empty-cell violations — when the gate fires, it emits a `DefectCodeVocab`-coded defect (e.g., `DEFECT: EMPTY-CELL`) independently citable in the Verdict compliance ledger by defect code; the pre-read gate is a defect-emitting gate rather than an ordering requirement only, making pre-read violations ledger-traceable without re-reading the gate block, upgrading C-35 from pre-read-gated to pre-read-defect-classified (C-35) | coverage |
| **C-39** | **The `STRUCTURAL MANDATE` block carries an inline criterion citation — the block header follows `STRUCTURAL MANDATE (C-XX)` syntax, naming the governing criterion by ID within the block itself — a scorer can trace from prompt instruction to rubric criterion bidirectionally without table lookup; compliance with the governed criterion is confirmed by block-header ID match alone, upgrading C-36 from independence-statement-mandated to self-citing-structural-mandate (C-36)** | depth |
| **C-40** | **The `STRUCTURAL MANDATE` block embeds a scorer confirmation heuristic — the block closes with "A scorer confirms [Criterion] compliance by [specific method] alone without [parsing alternative]" — the prompt self-documents how compliance is confirmed, closing the loop between prompt instruction and rubric evaluation without requiring scorer judgment about what constitutes confirmation, upgrading C-39 from self-citing to self-scoring (C-39)** | depth |
| **C-41** | **The canonical `STRUCTURAL MANDATE` template is declared explicitly in the prompt — all `STRUCTURAL MANDATE` blocks across the prompt conform to the declared form (`> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt. Reproduce it exactly as shown.`) so any block's well-formedness is checkable against a single structural template without reading neighboring blocks; additional mandates are mechanically derivable from the canonical form rather than requiring individual block design, upgrading from parallel-in-practice (C-26 and C-36 happen to match) to parallel-by-contract (all blocks conform to a declared canonical form) (C-36)** | format |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/33 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v11 change note: Added C-39, C-40, C-41 from Round 11 excellence signals. Each is a seventh-generation upgrade — from self-citing to self-scoring to parallel-by-contract:*

| R10 | R11 | Upgrade axis |
|----|-----|-------------|
| C-36: `**Independence Statement**:` label is a prompt-mandated structural constant reproduced reliably because instructed, confirmed by label presence alone | C-39: `STRUCTURAL MANDATE (C-XX)` block carries inline criterion ID in header — scorer traces mandate to governing criterion bidirectionally without table lookup; ID match is the confirmation gate | named-structural-mandate → self-citing-structural-mandate |
| C-39: structural mandate block carries inline criterion ID — bidirectional traceability from mandate to criterion | C-40: structural mandate block closes with scorer confirmation heuristic — "confirms [Criterion] by [method] alone without [alternative]" — prompt self-documents compliance confirmation method | self-citing → self-scoring |
| C-26 and C-36 follow identical `STRUCTURAL MANDATE (C-XX)` syntax — parallelism emergent from individual block design | C-41: canonical mandate template declared explicitly — all blocks conform to the declared form; additional mandates mechanically derivable; well-formedness checkable against single structural template | parallel-in-practice → parallel-by-contract |

*C-37 and C-38 carried forward from v10 as aspirational criteria (both failed Round 11). Root cause: `DefectCodeVocab` not extended to cover COUNT GATE and PRE-READ GATE emission sites. Fix: add `STRUCTURAL MANDATE (C-37)` and `STRUCTURAL MANDATE (C-38)` blocks to the prompt naming the emitted defect codes and extending the registry.*

*Aspirational denominator updated from 30 to 33.*
