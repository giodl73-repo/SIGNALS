Reading the Round 10 scorecard against C-33/C-34/C-35, each reveals a sixth-generation upgrade axis — from *validation-independent* to *mandate-guaranteed and defect-traceable*:

- **R10 / C-33**: V-01 demonstrates `**Independence Statement**:` as a bolded labeled element structurally isolated from the definition body — independently citable without parsing the bullet definitions. The natural upgrade: the `**Independence Statement**:` label is declared as a named structural mandate in the prompt (paralleling C-26's closure terminus instruction) — the label is an instructed element reproduced reliably rather than inferred from model context, upgrading C-33 from independence-statement-present to independence-statement-mandated.
- **R10 / C-34**: V-02 demonstrates the `**C-28 COUNT GATE**:` block with explicit IF/THEN conditional where the verdict (`confirmed` / `mismatch`) is derived from the rule, not annotated externally. The natural upgrade: gate failure emits a `DefectCodeVocab`-coded defect citation (`DEFECT: COUNT-MISMATCH` or equivalent) independently citable in the Verdict compliance ledger by defect code — gate outcomes are ledger-traceable, not just self-reported inside the gate block.
- **R10 / C-35**: V-03 demonstrates a `**PRE-READ GATE**:` section structurally ordered before the C-29 audit block. The natural upgrade: the pre-read gate carries a formal defect classification — when the gate fires, it emits a `DefectCodeVocab`-coded defect (`DEFECT: EMPTY-CELL` or equivalent) independently citable in the Verdict compliance ledger, making the gate defect-emitting rather than ordering-only.

Three new criteria: C-36 (C-33 upgrade), C-37 (C-34 upgrade), C-38 (C-35 upgrade). Aspirational denominator: 27 → 30.

---

# trace-skill Rubric v10

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

**30 Aspirational** (10 pts total):

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
| **C-36** | **The `**Independence Statement**:` label within the `DefectCodeVocab` type declaration is declared as a named structural mandate in the prompt (paralleling C-26's closure terminus instruction) — the label is an instructed, named element reproduced reliably rather than inferred from model context; a scorer confirms C-33 compliance by label presence alone without parsing surrounding definition bullets, upgrading C-33 from independence-statement-present to independence-statement-mandated (C-33)** | depth |
| **C-37** | **The `**C-28 COUNT GATE**:` block carries a formal defect classification for gate failure — when the IF/THEN resolves to `mismatch`, the gate emits a `DefectCodeVocab`-coded defect citation (e.g., `DEFECT: COUNT-MISMATCH`) independently citable in the Verdict compliance ledger by defect code rather than by gate-block description; gate outcomes are ledger-traceable, upgrading C-34 from self-evaluating to defect-emitting (C-34)** | depth |
| **C-38** | **The `**PRE-READ GATE**:` carries a formal defect classification for empty-cell violations — when the gate fires, it emits a `DefectCodeVocab`-coded defect (e.g., `DEFECT: EMPTY-CELL`) independently citable in the Verdict compliance ledger by defect code; the pre-read gate is a defect-emitting gate rather than an ordering requirement only, making pre-read violations ledger-traceable without re-reading the gate block, upgrading C-35 from pre-read-gated to pre-read-defect-classified (C-35)** | coverage |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/30 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v10 change note: Added C-36, C-37, C-38 from Round 10 excellence signals. Each is a sixth-generation upgrade — from validation-independent to mandate-guaranteed and defect-traceable:*

| R9 | R10 | Upgrade axis |
|----|-----|-------------|
| C-33: `DefectCodeVocab` closed-type declaration includes explicit independence statement — schema error detectable without registry lookup; validation at point of annotation | C-36: `**Independence Statement**:` label is a prompt-mandated structural constant — reproduced reliably because instructed, not inferred; compliance confirmed by label presence without parsing definition body | validation-independent → structurally-mandated |
| C-34: C-28 audit count assertion resolves to explicit PASS/FAIL binary (`confirmed` / `mismatch`) — audit block is self-evaluating; count confirmation is a gate, not a tally | C-37: gate failure emits `DefectCodeVocab`-coded defect citation — gate outcomes are independently citable in the Verdict compliance ledger by defect code, not by gate-block description | count-as-gate → gate-as-defect-emitter |
| C-35: C-32 empty-cell check is a named pre-read gate structurally ordered before ledger traversal — violations caught before traversal begins, ordering is prompt-instructed | C-38: pre-read gate carries formal defect classification — gate violations emit `DefectCodeVocab` code independently citable in the Verdict ledger; gate is defect-emitting, not ordering-only | pre-read-gated → pre-read-defect-classified |

*Aspirational denominator updated from 27 to 30.*
