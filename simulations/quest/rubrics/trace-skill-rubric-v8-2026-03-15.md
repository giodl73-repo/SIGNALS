Reading the V-05 scorecard evidence against C-27/C-28/C-29, each reveals a fourth-generation upgrade axis — from *schema-typed* to *composition-closed*:

- **V-05 / C-27**: `RequiredVocabulary` is a closed type. V-05 introduces `DefectCodeVocab` (via C-29) as a *second* closed type. The natural upgrade: vocabulary closure propagates to every named type in the schema — `DefectCodeVocab` is declared closed the same way `RequiredVocabulary` is, making all named types self-enumerating.
- **V-05 / C-28**: 11 annotation sites vs V-04's 10 — the extra site is the `Defect code (DefectCodeVocab)` column introduced by C-29. The natural upgrade: C-28's convention propagates automatically to columns introduced by composed criteria; the C-28 audit block tracks site count so composed coverage is verifiable.
- **V-05 / C-29**: PASS rows carry `--` (sentinel), and a C-29 audit block at Verdict top confirms registry integrity + vocabulary discipline. The natural upgrade: the ledger is fully populated (no empty cells) and the audit block self-certifies ledger integrity, making defect discipline verifiable without re-inspecting the registry.

Three new criteria: C-30 (C-27 upgrade), C-31 (C-28 upgrade), C-32 (C-29 upgrade). Aspirational denominator: 21 → 24.

---

# trace-skill Rubric v8

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

**24 Aspirational** (10 pts total):

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
| **C-30** | **`DefectCodeVocab` is declared as a closed type in the Defect Classification Registry with all defect codes enumerated — the same vocabulary-closure discipline applied to `RequiredVocabulary` by C-27 propagates to `DefectCodeVocab`, making every named type in the schema closed-typed and self-enumerating rather than open-ended (C-27)** | depth |
| **C-31** | **C-28's uniform `(TypeName)` annotation convention propagates to all typed columns introduced by composed criteria — the Defect Classification Registry's code column and the Verdict compliance ledger's defect code column both carry `(DefectCodeVocab)` annotation; the C-28 audit block tracks total annotation site count to confirm composed-column coverage (C-28)** | depth |
| **C-32** | **Verdict compliance ledger `Defect code` column is fully populated: every row carries a value — FAIL rows cite a `DefectCodeVocab` code, PASS rows carry `--` as an explicit sentinel; a C-29 audit block at Verdict top confirms (a) registry present before Stage 1, (b) all FAIL citations drawn from `DefectCodeVocab`, (c) no empty cells — ledger is self-certifying without re-inspecting the registry (C-29)** | coverage |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/24 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v8 change note: Added C-30, C-31, C-32 from Round 8 excellence signals. Each is a fourth-generation composition upgrade — from schema-typed to composition-closed:*

| R7 | R8 | Upgrade axis |
|----|-----|-------------|
| C-27: `RequiredVocabulary` declared as closed two-value type | C-30: `DefectCodeVocab` also declared as closed type — vocabulary closure propagates to all named types, not only `RequiredVocabulary` | single vocabulary closed → all vocabularies closed |
| C-28: `(TypeName)` annotation applied uniformly to all pre-existing typed columns; 10 annotation sites | C-31: C-28 convention propagates to columns introduced by composed criteria (C-29's registry column + ledger column); audit block tracks site count to confirm composed coverage (11 sites in R8 target) | pre-composed columns typed → composed columns also typed |
| C-29: structural mandates carry defect codes; Verdict ledger cites by code | C-32: Verdict ledger fully populated (PASS rows `--` sentinel, FAIL rows code, no empty cells) + C-29 audit block self-certifies ledger integrity at Verdict top | mandated + cited → fully populated + self-certified |

*Aspirational denominator updated from 21 to 24.*
