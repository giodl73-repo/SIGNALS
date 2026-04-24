Reading the scorecard carefully to extract new excellence patterns not yet captured in v2.

**New patterns identified:**

- **V-01**: "Immutable Phase Label Schema table" — a pre-trace declaration table that structurally locks all four phase headers before content begins. Distinct from C-06 (which just requires exact labels at runtime).
- **V-01**: "Compliance ledger structure" in Verdict — a structured table (ID | Result | Evidence) rather than prose citation. Stronger than C-07 (which only requires criterion IDs appear).
- **V-03**: Bind three-value Status enum (RESOLVED / UNRESOLVED / BLOCKED) — explicit status column in every Bind row. Distinct from C-12 (which is a pre-Gather gate); the scorecard flags these as separate when V-03 gets C-12 PARTIAL precisely because the BLOCKED halt lives in Bind, not before Gather.
- **V-02**: Explicit conflict precedence rule in Bind — when spec value and invocation value disagree, a declared rule resolves the conflict (e.g., spec anchors, invocation overrides). V-02's axis is spec-first enumeration (C-11) but the conflict rule is an additional structural signal.

That gives four new aspirationals: C-14 through C-17.

---

```markdown
# trace-skill Rubric v3

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

**9 Aspirational** (10 pts total):

| ID   | Criterion                                                                                                                                              | Category  |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| C-09 | Gather includes Coverage Matrix table with closed-world preamble                                                                                       | coverage  |
| C-10 | Execute relays carry (role, signal, binding, status) evidence fields; Verdict reads, not reconstructs                                                  | depth     |
| C-11 | Gather enumerates spec inputs before invocation inputs — spec anchors the input space before constraints apply                                         | ordering  |
| C-12 | Coverage Matrix includes explicit BLOCKED declaration: any Gap=YES halts the trace immediately, no partial runs                                        | coverage  |
| C-13 | Execute wraps artifact with delimiter markers (`[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]`) for unambiguous extraction                          | format    |
| C-14 | A pre-trace Phase Label Schema table (immutable) declares all four phase headers before any trace content begins — enforces C-06 structurally          | format    |
| C-15 | Verdict is a structured compliance ledger table (columns: ID \| Result \| Evidence) rather than prose — stronger than C-07's criterion-ID citation    | depth     |
| C-16 | Bind rows carry an explicit three-value Status enum: RESOLVED / UNRESOLVED / BLOCKED — resolution state is unambiguous without inference               | depth     |
| C-17 | Bind declares an explicit conflict precedence rule: when spec value and invocation value disagree, the rule resolves which wins (e.g., spec anchors)   | depth     |

**Scoring**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/9 × 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v3 change note: Added C-14 (Phase Label Schema table), C-15 (Verdict compliance ledger), C-16 (Bind three-value Status enum), C-17 (Bind conflict precedence rule) from Round 2 excellence signals. Aspirational denominator updated from 5 to 9.*
```

---

**Rationale for each addition:**

- **C-14** — V-01 scores 85 largely because the Phase Label Schema table makes C-06 a structural guarantee rather than a convention. It's a distinct excellence pattern: the schema exists before the trace runs, not inside it.
- **C-15** — V-01's "compliance ledger structure with criterion-ID column" is categorically stronger than C-07. C-07 says IDs must appear; C-15 says Verdict must be a table. A trace that passes C-07 can still bury IDs in prose.
- **C-16** — V-03's three-value Status is not C-12. The scorecard makes this explicit: V-03 gets C-12 PARTIAL because its BLOCKED is inside Bind, not a pre-Gather gate. The three-value enum is a separate structural pattern for resolution clarity in Bind rows.
- **C-17** — V-02's conflict rule (spec vs. invocation value) doesn't have a home in any existing criterion. C-03 only requires resolution happens; C-17 requires the rule governing resolution to be declared explicitly, which prevents silent precedence assumptions.
