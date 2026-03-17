Reading the scorecard carefully for R4 excellence patterns not yet captured in v3.

**Three new patterns identified** (the "three R4 patterns" the scorecard names explicitly in the entry state recap and tiebreak rationale):

- **C-18** — Relay provenance: relay rows carry `InputName = "ResolvedValue"` binding pairs, so Verdict can verify resolution directly from relay without inspecting the Bind table. Stronger than C-10 (which only requires evidence fields present).
- **C-19** — Per-row conflict annotation: Bind carries a "Precedence applied" column, making rule application traceable at the row level. Stronger than C-17 (which only requires the conflict rule be declared once).
- **C-20** — Coverage Matrix CLOSED assertion: names each Required=YES input explicitly as the structural gate-pass element. Stronger than C-12 (which only requires BLOCKED declaration text).

---

```markdown
# trace-skill Rubric v4

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

**12 Aspirational** (10 pts total):

| ID   | Criterion                                                                                                                                                                                                              | Category  |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| C-09 | Gather includes Coverage Matrix table with closed-world preamble                                                                                                                                                       | coverage  |
| C-10 | Execute relays carry (role, signal, binding, status) evidence fields; Verdict reads, not reconstructs                                                                                                                  | depth     |
| C-11 | Gather enumerates spec inputs before invocation inputs — spec anchors the input space before constraints apply                                                                                                         | ordering  |
| C-12 | Coverage Matrix includes explicit BLOCKED declaration: any Gap=YES halts the trace immediately, no partial runs                                                                                                        | coverage  |
| C-13 | Execute wraps artifact with delimiter markers (`[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]`) for unambiguous extraction                                                                                          | format    |
| C-14 | A pre-trace Phase Label Schema table (immutable) declares all four phase headers before any trace content begins — enforces C-06 structurally                                                                         | format    |
| C-15 | Verdict is a structured compliance ledger table (columns: ID \| Result \| Evidence) rather than prose — stronger than C-07's criterion-ID citation                                                                    | depth     |
| C-16 | Bind rows carry an explicit three-value Status enum: RESOLVED / UNRESOLVED / BLOCKED — resolution state is unambiguous without inference                                                                              | depth     |
| C-17 | Bind declares an explicit conflict precedence rule: when spec value and invocation value disagree, the rule resolves which wins (e.g., spec anchors)                                                                  | depth     |
| C-18 | Relay rows carry explicit `InputName = "ResolvedValue"` binding pairs — resolution value is stated in the relay itself, so Verdict can verify binding without re-inspecting the Bind table                            | depth     |
| C-19 | Bind table carries a "Precedence applied" column — per-row annotation of which conflict rule resolved each binding, making rule application traceable at row level rather than only at the rule declaration level (C-17) | depth     |
| C-20 | Coverage Matrix carries a CLOSED assertion that names each Required=YES input explicitly — the enumerated closed-world is the structural gate-pass for C-12, not a bare text declaration                              | coverage  |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/12 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v4 change note: Added C-18 (relay binding key=value pairs), C-19 (Bind per-row "Precedence applied" column), C-20 (Coverage Matrix CLOSED assertion with named Required=YES inputs) from Round 4 excellence signals. Aspirational denominator updated from 9 to 12.*
```

---

**Rationale for each addition:**

- **C-18** — The R4 scorecard names "relay provenance" as one of the three R4 patterns and confirms V-01/V-04/V-05 extend relay binding to `InputName = "ResolvedValue"` pairs. C-10 requires evidence fields in relay rows; C-18 requires the resolved value itself be stated there, making the relay self-verifying from Verdict without a Bind table lookup.

- **C-19** — The R4 scorecard names "per-row conflict annotation" as one of the three R4 patterns and confirms V-03/V-04/V-05 carry a "Precedence applied" column in Bind. C-17 requires the conflict rule be declared once; C-19 requires each row show which rule applied — rule traceability is per-row, not just per-trace.

- **C-20** — The R4 scorecard names "Coverage Matrix closure assertion" as one of the three R4 patterns and confirms V-04/V-05 carry the CLOSED assertion listing each Required=YES input by name. C-12 requires a BLOCKED halt declaration; C-20 requires the closed-world be enumerated by name, which is the structural form of the gate-pass rather than a text declaration that could become stale.
