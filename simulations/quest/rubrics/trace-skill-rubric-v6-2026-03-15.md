Reading the scorecard's R6 excellence signals: each V-0x produces a structurally distinct PASS pattern for C-21/C-22/C-23, revealing a second-generation upgrade axis — from *present* to *structurally self-contained*:

- **V-01**: Anti-pattern row is its own independent row (`VIOLATION` in Required column) → independently citable without parsing the Format cell
- **V-02**: Closed vocabulary is given a **named type** (`PrecedenceVocabulary`); column header cites the type → column becomes self-validating via type reference
- **V-03**: Terminus line is a **labeled structural mandate** in the prompt → reproduced by model, not emergent

Three new criteria: C-24 (C-21 upgrade), C-25 (C-22 upgrade), C-26 (C-23 upgrade). Aspirational denominator: 15 → 18.

---

# trace-skill Rubric v6

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

**18 Aspirational** (10 pts total):

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
| **C-24** | **Relay Schema anti-pattern prohibition is a structurally independent row with `VIOLATION` in the Required column — independently citable without parsing the Format cell, structural isolation rather than inline embedding (C-21)** | depth |
| **C-25** | **Conflict precedence vocabulary is declared as a named type (`PrecedenceVocabulary` or equivalent); the "Precedence applied" column header cites the type by name — column is self-validating via type reference, not by proximity to the declaration (C-22)** | depth |
| **C-26** | **Closure terminus line is a labeled structural mandate in the prompt (not emergent from model depth) — the line appears as an instructed, named element so it is reproduced reliably rather than inferred from context (C-23)** | coverage |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/18 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v6 change note: Added C-24, C-25, C-26 from Round 6 excellence signals. Each is a second-generation precision upgrade along the same structural-isolation axis — from declared to self-contained:*

| R5 | R6 | Upgrade axis |
|----|-----|-------------|
| C-21: anti-pattern prohibition present as row | C-24: anti-pattern row structurally independent (own Required=VIOLATION cell) | row present → row self-contained |
| C-22: closed vocabulary declared | C-25: vocabulary given named type; column header cites type | vocabulary closed → vocabulary typed |
| C-23: terminus line present | C-26: terminus line is labeled structural mandate | terminus present → terminus structurally mandated |

*Aspirational denominator updated from 15 to 18.*
