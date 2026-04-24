## trace-skill — Round 4 Scoring / Rubric v3

**Entry state recap**: R3 V-05 achieved all 17 criteria. R4 explores three residual patterns (relay provenance, per-row conflict annotation, Coverage Matrix closure assertion) across five variation axes.

---

### Criterion Evaluation by Variation

#### Essential (C-01 through C-05)

All five variations inherit the R3 V-05 phase structure intact. Full evaluation:

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Four phases in sequence | PASS | PASS | PASS | PASS | PASS |
| C-02 | Gather inputs by name with source | PASS | PASS | PASS | PASS | PASS |
| C-03 | Bind maps all inputs to resolved value | PASS | PASS | PASS | PASS | PASS |
| C-04 | Execute produces artifact: naming + sections | PASS | PASS | PASS | PASS | PASS |
| C-05 | Verdict declares PASS/FAIL with rationale | PASS | PASS | PASS | PASS | PASS |

*Evidence basis*: Every variation carries explicit Gather Tier 1 + Tier 2 tables, a Bind resolution table with Resolved Value column non-blank for all rows, a relay table + artifact body in Execute, and a Verdict compliance ledger with an Overall row. All five: 5/5 essential.

---

#### Recommended (C-06 through C-08)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Exact schema labels (Gather/Bind/Execute/Verdict) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Verdict cites criterion IDs | PASS | PASS | PASS | PASS | PASS |
| C-08 | No elision markers in artifact | PASS | PASS | PASS | PASS | PASS |

*Evidence*:
- C-06: Phase Label Schema preamble present in all five. V-02 labels it "IMMUTABLE — pre-trace preamble." Same structure.
- C-07: All Verdicts are structured compliance ledger tables with C-01 through C-17 as rows. V-02 additionally has self-check questions that pre-verify this before writing the table.
- C-08: All five require "Complete artifact — every required section, no '...', no '[content here]'" — explicit prohibition of elision markers stated in Execute instruction.

All five: 3/3 recommended.

---

#### Aspirational (C-09 through C-17)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Coverage Matrix + closed-world preamble | PASS | PASS | PASS | PASS | PASS |
| C-10 | Relay carries evidence fields; Verdict reads relay | PASS | PASS | PASS | PASS | PASS |
| C-11 | Spec inputs before invocation in Gather | PASS | PASS | PASS | PASS | PASS |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS | PASS | PASS | PASS | PASS |
| C-13 | Artifact delimiter markers | PASS | PASS | PASS | PASS | PASS |
| C-14 | Phase Label Schema table pre-trace | PASS | PASS | PASS | PASS | PASS |
| C-15 | Verdict is compliance ledger (ID/Result/Evidence) | PASS | PASS | PASS | PASS | PASS |
| C-16 | Bind Status Enum (3-value) declared | PASS | PASS | PASS | PASS | PASS |
| C-17 | Bind conflict precedence rule declared | PASS | PASS | PASS | PASS | PASS |

**Criterion-by-criterion notes:**

**C-09**: All five carry Coverage Matrix with explicit "closed-world authority" preamble before Gather. V-04 and V-05 additionally carry the Coverage Matrix CLOSED assertion naming each Required=YES input — this exceeds C-09 but C-09 itself passes.

**C-10**: C-10 requires relay carries (role, signal, binding, status) and Verdict reads relay. V-01/V-04/V-05 extend binding to `InputName = "ResolvedValue"` pairs — stronger than C-10 requires but C-10 criterion is satisfied in all five. V-02/V-03 carry standard binding (input name only) — meets the criterion as written.

**C-11**: All five carry Gather Tier 1 (spec-declared inputs, source type) before Tier 2 (invocation-supplied values). V-02 adds self-check question #2 confirming this order before content.

**C-12**: All five carry BLOCKED gate text. V-04 and V-05 additionally carry the CLOSED assertion as the named gate-pass structural element — stronger, but C-12 passes in all five.

**C-13**: All five carry `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` explicitly written in Execute.

**C-14**: All five carry Phase Label Schema as an immutable pre-trace table before Coverage Matrix and before any phase content. V-05 explicitly notes "before Coverage Matrix; before any phase content" in the Verdict evidence row.

**C-15**: All five Verdicts are structured as ID | Criterion | Result | Evidence tables with evidence citing specific structural elements (table headers, row counts, delimiter strings, relay row statuses).

**C-16**: All five declare the three-value Status Enum (RESOLVED / UNRESOLVED / BLOCKED) as a formal definition table above the Bind resolution table, with Execute effects column.

**C-17**: Rubric criterion requires only "declares an explicit conflict precedence rule." All five carry a named Conflict Precedence Rule block (invocation override + BLOCKED exception) above the first resolution row. V-03/V-04/V-05 additionally carry the "Precedence applied" column for per-row traceability — exceeds C-17 but the declaration requirement passes in all five.

All five: 9/9 aspirational.

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | All Essential? |
|-----------|---------------|-----------------|------------------|-------|----------------|
| V-01 | 60 | 30 | 10 | **100** | YES |
| V-02 | 60 | 30 | 10 | **100** | YES |
| V-03 | 60 | 30 | 10 | **100** | YES |
| V-04 | 60 | 30 | 10 | **100** | YES |
| V-05 | 60 | 30 | 10 | **100** | YES |

**All five meet the golden threshold** (all essential PASS + composite ≥ 80).

---

### Ranking

All five score 100. Tiebreak by structural density of new evidence contributions not yet captured in v3:

1. **V-05** — All three R4 patterns combined (relay provenance + per-row conflict + CM closure assertion). Most structurally complete.
2. **V-04** — Two of three R4 patterns (relay provenance + per-row conflict + CM closure assertion).
3. **V-01** — Relay provenance alone, cleanest single-axis demonstration.
4. **V-03** — Per-row conflict annotation alone, cleanest demonstration of C-17 extension.
5. **V-02** — Self-check questions; no new structural elements produced, but compliance checking migrated from terminal to continuous per phase.

---

### Excellence Signals from V-05

Three patterns in V-05 are structurally stronger than the corresponding v3 criteria but have no criterion yet:

**Pattern A: Relay-to-Bind provenance (V-01/V-04/V-05)**
The Execute relay Binding column carries `InputName = "ResolvedValue"` verbatim pairs rather than just input names. Effect: the relay row is self-verifying against the Bind table. A reader can confirm binding without backtracking through the artifact body. C-10 passes with input-name-only binding; this pattern makes C-10 a structural chain, not just a structural presence.

**Pattern B: Per-row conflict annotation (V-03/V-04/V-05)**
The Bind resolution table gains a "Precedence applied" column with a declared three-value vocabulary (`override` / `default` / `BLOCKED`). Effect: C-17's conflict rule is now traceable at each resolution decision, not just at declaration. A conflict rule declared as a block can be mechanically present without ever being applied; the per-row column makes application visible.

**Pattern C: Coverage Matrix closure assertion (V-04/V-05)**
After the BLOCKED gate passes, an explicit "Coverage Matrix: CLOSED" assertion names each Required=YES input confirmed Gap=NO. Effect: the gate's exit is a named structural element the Verdict can cite for C-09 and C-12. Without the assertion, the Verdict must infer gate passage from the absence of a BLOCKED branch — the assertion converts an absence-of-evidence argument into a positive citation target.

**Pattern D (secondary, V-02): Phase-internal self-check questions**
Each phase opens with 2–3 criterion-aligned questions (answered YES/NO inline). Effect: compliance checking migrates from terminal Verdict activity to continuous in-phase activity. Does not produce new structural elements the Verdict cites, but surfaces failures earlier. Less citable as a v4 criterion than A/B/C; more of a prompt-design technique.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["relay Binding column carries InputName=ResolvedValue pairs verbatim — relay-to-Bind chain is structurally verifiable without backtracking", "Bind resolution table gains Precedence applied column (override/default/BLOCKED) — C-17 conflict rule traceable at each row, not just at declaration", "Coverage Matrix CLOSED assertion written after gate passes — gate exit is a named structural element Verdict can cite for C-09 and C-12"]}
```
