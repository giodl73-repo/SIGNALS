Done. Here is the complete updated rubric:

---

# trace-skill Rubric v5

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

**15 Aspirational** (10 pts total):

| ID   | Criterion                                                                 | Category  |
|------|---------------------------------------------------------------------------|-----------|
| C-09 | Gather includes Coverage Matrix table with closed-world preamble | coverage |
| C-10 | Execute relays carry (role, signal, binding, status) evidence fields; Verdict reads, not reconstructs | depth |
| C-11 | Gather enumerates spec inputs before invocation inputs | ordering |
| C-12 | Coverage Matrix includes explicit BLOCKED declaration | coverage |
| C-13 | Execute wraps artifact with delimiter markers | format |
| C-14 | Pre-trace Phase Label Schema table (immutable) before any trace content | format |
| C-15 | Verdict is a structured compliance ledger table | depth |
| C-16 | Bind rows carry explicit three-value Status enum: RESOLVED / UNRESOLVED / BLOCKED | depth |
| C-17 | Bind declares explicit conflict precedence rule | depth |
| C-18 | Relay rows carry `InputName = "ResolvedValue"` binding pairs | depth |
| C-19 | Bind table carries "Precedence applied" column with per-row annotation | depth |
| C-20 | Coverage Matrix carries CLOSED assertion naming each Required=YES input | coverage |
| **C-21** | **Relay Schema carries explicit anti-pattern prohibition ("Do NOT write input name only" or equivalent) — active enforcement of C-18's format, not passive declaration** | depth |
| **C-22** | **"Precedence applied" column declares closed three-value vocabulary (override / default / BLOCKED) — vocabulary closure makes C-19's column self-validating** | depth |
| **C-23** | **CLOSED ASSERTION block terminates with explicit closure declaration line ("Coverage Matrix is CLOSED for this invocation." or equivalent) — formal terminus makes C-20's enumeration self-evidencing** | coverage |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/15 × 10)`
**Golden threshold**: all 5 essential PASS + composite >= 80

---

**R5 pattern structure:** Each new criterion is a precision upgrade to its R4 counterpart along a consistent axis — from *declared* to *enforced*:

| R4 | R5 | Upgrade axis |
|----|----|--------------|
| C-18: format declared | C-21: forbidden form named | passive → active enforcement |
| C-19: column present | C-22: vocabulary closed | open annotation → type-closed annotation |
| C-20: inputs enumerated | C-23: block formally terminated | inference-based completeness → structural completeness |
                       | ordering  |
| C-12 | Coverage Matrix includes explicit BLOCKED declaration: any Gap=YES halts the trace immediately, no partial runs                                                                                                                  | coverage  |
| C-13 | Execute wraps artifact with delimiter markers (`[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]`) for unambiguous extraction                                                                                                    | format    |
| C-14 | A pre-trace Phase Label Schema table (immutable) declares all four phase headers before any trace content begins — enforces C-06 structurally                                                                                   | format    |
| C-15 | Verdict is a structured compliance ledger table (columns: ID \| Result \| Evidence) rather than prose — stronger than C-07's criterion-ID citation                                                                              | depth     |
| C-16 | Bind rows carry an explicit three-value Status enum: RESOLVED / UNRESOLVED / BLOCKED — resolution state is unambiguous without inference                                                                                        | depth     |
| C-17 | Bind declares an explicit conflict precedence rule: when spec value and invocation value disagree, the rule resolves which wins (e.g., spec anchors)                                                                            | depth     |
| C-18 | Relay rows carry explicit `InputName = "ResolvedValue"` binding pairs — resolution value is stated in the relay itself, so Verdict can verify binding without re-inspecting the Bind table                                      | depth     |
| C-19 | Bind table carries a "Precedence applied" column — per-row annotation of which conflict rule resolved each binding, making rule application traceable at row level rather than only at the rule declaration level (C-17)         | depth     |
| C-20 | Coverage Matrix carries a CLOSED assertion that names each Required=YES input explicitly — the enumerated closed-world is the structural gate-pass for C-12, not a bare text declaration                                        | coverage  |
| C-21 | Relay Schema carries an explicit anti-pattern prohibition ("Do NOT write input name only" or equivalent) — makes the `InputName = "ResolvedValue"` format requirement actively enforced rather than passively declared (C-18)    | depth     |
| C-22 | "Precedence applied" column declares a closed three-value vocabulary (override / default / BLOCKED) — vocabulary closure prevents ambiguous annotation values and makes the column self-validating (C-19)                        | depth     |
| C-23 | CLOSED ASSERTION block terminates with an explicit closure declaration line ("Coverage Matrix is CLOSED for this invocation." or equivalent) — formal terminus makes the closed-world claim self-evidencing, not inferred from enumeration alone (C-20) | coverage  |

**Scoring**: `(essential_pass/5 x 60) + (recommended_pass/3 x 30) + (aspirational_pass/15 x 10)`
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v5 change note: Added C-21 (Relay Schema anti-pattern prohibition), C-22 (Precedence applied closed three-value vocabulary), C-23 (CLOSED ASSERTION terminus declaration line) from Round 5 excellence signals. Each is a precision upgrade to its R4 counterpart: C-18 -> C-21 (passive declaration -> active enforcement), C-19 -> C-22 (column exists -> vocabulary closed), C-20 -> C-23 (inputs enumerated -> closed-world formally terminated). Aspirational denominator updated from 12 to 15.*
```

---

**Rationale for each addition:**

- **C-21** — V-01's C-18 evidence names "Relay Schema block declares Binding column as `InputName = "ResolvedValue"` with example and 'Do NOT write input name only' prohibition." C-18 requires the format be declared; C-21 requires the forbidden form be explicitly named in the schema. An anti-pattern prohibition is structurally stronger than a positive-only format declaration: it closes the gap between "I declared the right format" and "I blocked the wrong format," which are distinct claims.

- **C-22** — V-02's C-19 evidence names "Bind Schema Part 3 declares 'Precedence applied' as required column with three-value vocabulary (override/default/BLOCKED)." C-19 requires the column carry per-row annotation; C-22 requires the annotation vocabulary be closed and declared. An open vocabulary allows annotation values that satisfy C-19's letter ("the column is present with a value") while being ambiguous at the type level -- vocabulary closure is the next structural gate.

- **C-23** — V-03's C-20 evidence names "closes with 'Coverage Matrix is CLOSED for this invocation.'" and the Verdict row cites placement "between Coverage Matrix gate and Gather." C-20 requires the Required=YES inputs be enumerated by name; C-23 requires the block terminate with a formal closure statement. Enumeration proves the closed-world was identified; the terminus declaration asserts the identification is complete. Without the terminus, a reader must infer completeness from context -- C-23 makes it structural.
