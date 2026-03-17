## mock-ns Round 5 — Scoring (rubric v5, 108-point scale)

---

### Shared Baseline Assessment

All 5 variations share identical S-1, S-2, S-3 (FLAG computation), and A-1 through A-5 steps. The deliberate single-axis changes are isolated to S-0 and the FLAG table. I will verify the shared criteria once, then focus on the axis-specific deltas.

**Essential criteria (C-01–C-05) — verified identical across all variations:**

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-01 | A-1 has all 6 fields: Skill, Topic, Category, Date, Status, Flag | PASS all |
| C-02 | S-2 category table matches canonical HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED lists | PASS all |
| C-03 | S-3 FLAG computation table produces correct values for all category/tier/compliance paths | PASS all |
| C-04 | A-2 has category-matched fidelity warning with correct language per category | PASS all |
| C-05 | A-3 requires skill-specific section headings, tables, verdict line; reader-identifiable without header | PASS all |

**Recommended criteria (C-06–C-08) — verified identical:**

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-06 | S-0 emits TOPICS.md status line; S-1 emits `> Generating mock for...`; S-0 precedes S-1 | PASS all |
| C-07 | A-4 path uses `{topic}-{namespace}-mock-{date}.md`; write confirmation emitted | PASS all |
| C-08 | A-5 final line: `Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md` | PASS all |

**Aspirational C-09 through C-18 — verified identical:**

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-09 | S-1 table: `topic -> topic-plan \| NEVER topic-status` | PASS all |
| C-10 | Compliance override rule present in S-3; default pass when no tags | PASS all |
| C-11 | FLAG table covers all 5 functional cases; `trace-*`, `scout-feasibility`, `listen-*` named explicitly | PASS all |
| C-12 | S-0 and S-1 are distinct labeled steps; tier resolved in S-0 before S-1 begins | PASS all |
| C-13 | S-2: "emit an error that names the unrecognized skill-id and points to the registry. Stop. Do not assign a fallback category." | PASS all |
| C-14 | STEP A-1 through STEP A-5 each labeled with single output responsibility | PASS all |
| C-15 | (See per-variation below — V-01 is the axis) | varies |
| C-16 | FLAG table row 3 condition cell: "skill-id matches trace-*, scout-feasibility, or listen-*" | PASS all |
| C-17 | Terminal gate names S-1 (or equivalent) in all variations | PASS all |
| C-18 | Standalone sentence names S-2 and S-3 as consumers in all variations | PASS all |

---

### Per-Variation Scoring

---

#### V-01 — C-21 Boundary: 3-op CONSTRAINT

**Axis change**: CONSTRAINT: `No skill selection. No category lookup. No mock generation.` — exactly 3 ops. "No body generation." absent.

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-15 | 3 op types named by type (skill selection, category lookup, mock generation) | PASS |
| C-19 | Preamble: "Before any other step begins, emit the TOPICS.md status line below." ✓ Terminal: "Do not begin S-1 until this line is emitted." ✓ Both present | PASS |
| C-20 | Table "Carry into S-2 and S-3" ✓ Standalone "Carry the resolved tier into S-2 and S-3." ✓ Both name consumers | PASS |
| **C-21** | Only 3 ops named. "No body generation." absent. Gap remains where artifact content could begin before S-0 completes. C-15 minimum met but C-21 4-op requirement not met | **FAIL** |
| C-22 | Rows: EVIDENCE-HEAVY / MIXED / HS critical tier≥2 / HS critical tier=1 / HS all other. 5 rows, tier=1 critical explicit | PASS |

**C-21 FAIL confirmed** — exactly the predicted trap pattern: C-15 passes because op-type naming is present (3 ops), but the 4th op (body generation) is absent.

**Score: 106/108** (loses C-21: −2)

---

#### V-02 — C-22 Boundary: 4-row FLAG Table

**Axis change**: FLAG table has 4 rows. "HS critical tier=1" row removed; catch-all reads "HIGH-STRUCTURE, all other conditions."

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-15 | 4 ops: skill selection, category lookup, mock generation, body generation | PASS |
| C-19 | Preamble "Before any other step begins..." ✓ Terminal "Do not begin S-1 until this line is emitted." ✓ | PASS |
| C-20 | Table "Carry into S-2 and S-3" ✓ Standalone "Carry the resolved tier into S-2 and S-3." ✓ | PASS |
| C-21 | 4 ops including body generation | PASS |
| C-11 | 4-row table: EVIDENCE-HEAVY, MIXED, HS-critical-tier≥2 (with trace-*, listen-* named), catch-all. Rubric explicitly permits collapse of cases 1+2 when they share the same flag value. All 5 functional cases covered | PASS |
| C-16 | Tier≥2 critical row condition cell: "skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2" — wildcards in cell | PASS |
| **C-22** | HS-critical-tier=1 case absorbed into "HIGH-STRUCTURE, all other conditions." No dedicated row for tier=1 critical case. C-22 requires structural row separation even when flag value is identical. Collapsed into catch-all | **FAIL** |

**C-22 FAIL confirmed** — exactly the predicted trap: scorer might award C-22 because C-11 passes and 5 cases are functionally covered, but C-22 requires a dedicated row, not just functional coverage.

**Score: 106/108** (loses C-22: −2)

---

#### V-03 — C-19 Boundary: Terminal Gate Only

**Axis change**: "Before any other step begins, emit the TOPICS.md status line below." removed from S-0. Only terminal gate remains.

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-15 | 4 ops present | PASS |
| **C-19** | Preamble gate: absent — the "Before any other step begins..." sentence was removed. Terminal gate: "Do not begin S-1 until this line is emitted." ✓ Only one gate form present. C-19 requires both entry-position and exit-position coverage | **FAIL** |
| C-17 | Terminal gate names S-1: "Do not begin S-1 until this line is emitted." C-17 content requirement met via terminal gate alone | PASS |
| C-20 | Table "Carry into S-2 and S-3" ✓ Standalone "Carry the resolved tier into S-2 and S-3." ✓ | PASS |
| C-21 | 4 ops including body generation | PASS |
| C-22 | 5-row FLAG table, tier=1 critical row explicit | PASS |

**C-19 FAIL confirmed** — exactly the predicted trap: C-17 passes (terminal gate names S-1) but C-19 requires the preamble gate at entry position as well. A reader scanning S-0 encounters the resolution table before any gate language.

**Score: 106/108** (loses C-19: −2)

---

#### V-04 — C-20 Trap: Table Column Without Named Consumers

**Axis change**: Tier row downstream-use column reads "Used in S-3 flag computation" (generic use description, no consumer labels). Standalone sentence unchanged: "Carry the resolved tier into S-2 and S-3."

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-15 | 4 ops present | PASS |
| C-19 | Preamble "Before any other step begins..." ✓ Terminal "Do not begin S-1 until this line is emitted." ✓ Both present | PASS |
| C-18 | Standalone sentence "Carry the resolved tier into S-2 and S-3." names both S-2 and S-3 | PASS |
| **C-20** | Table downstream-use cell: "Used in S-3 flag computation" — describes tier's use but does not name consumers by label. Standalone sentence names S-2 and S-3 (satisfying C-18). C-20 requires BOTH registers to contain the named-consumer form. Table column fails this register | **FAIL** |
| C-21 | 4 ops including body generation | PASS |
| C-22 | 5-row FLAG table, tier=1 critical row explicit | PASS |

**C-20 FAIL confirmed** — exactly the predicted trap: C-18 passes via the standalone sentence, and a table column is present, but the table cell uses a generic description ("Used in S-3 flag computation") rather than naming S-2 and S-3 as consumers. C-20's dual-register requirement means both positions must carry the named-consumer form.

**Score: 106/108** (loses C-20: −2)

---

#### V-05 — Convergent: All 22 Criteria via Alternative Surface Forms

**Axis**: Form-independence test. All 4 v5 criteria achieved via distinct phrasing from R4 V-05.

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-15 | "No skill lookup. No category classification. No mock generation. No artifact content production." — 4 ops. Synonymic op names: "skill lookup" ≡ skill selection; "category classification" ≡ category lookup; "artifact content production" ≡ body generation. Semantic match satisfies C-15 | PASS |
| C-19 | Preamble: "This step executes first. Emit the TOPICS.md status line below before any other step begins." (two-clause declarative+directive form, before resolution bullets) ✓ Terminal: "S-1 must not start until the line above has been written." (backward-reference form, after resolution bullets) ✓ Both gate positions covered | PASS |
| C-17 | Terminal gate "S-1 must not start until the line above has been written." — names S-1 explicitly; prohibits advance. Content-based requirement met despite backward-reference phrasing | PASS |
| C-20 | Table downstream-use: "Propagates to S-2 and S-3" — names both consumers in table cell ✓. Standalone: "Carry the resolved tier forward to S-2 and S-3." — names both consumers in prose ✓. Both registers present | PASS |
| C-21 | 4 ops named including "artifact content production" for body generation. C-21 is semantic, not lexical: any phrase denoting body/artifact content generation satisfies the prohibition | PASS |
| C-22 | Rows: EVIDENCE-HEAVY / MIXED / HS critical tier≥2 / HS critical tier=1 / "HIGH-STRUCTURE, non-critical skills, any tier". 5 rows, tier=1 critical is a dedicated explicit row | PASS |
| C-01–C-18 | All shared baseline criteria verified identical to boundary variates | PASS all |

**All 22 criteria pass** — form-independence confirmed across all 4 v5 axes.

**Score: 108/108**

---

### Composite Score Table

| Variate | Essential (50) | Recommended (30) | Aspirational (28) | Total | Fails |
|---------|---------------|-----------------|------------------|-------|-------|
| V-01 | 50 | 30 | 26 | **106/108** | C-21 |
| V-02 | 50 | 30 | 26 | **106/108** | C-22 |
| V-03 | 50 | 30 | 26 | **106/108** | C-19 |
| V-04 | 50 | 30 | 26 | **106/108** | C-20 |
| **V-05** | 50 | 30 | **28** | **108/108** | none |

All 5 variates hit exactly their predicted scores. All 5 hypotheses confirmed.

---

### Excellence Signals from V-05

**Signal 1 — Two-clause preamble gate form (C-19)**
V-05 uses "This step executes first. Emit... before any other step begins." — a declarative assertion of step primacy followed by the emit directive. This is stronger than the single-sentence form in R4 V-05 because it asserts execution order as a fact before stating the requirement. Separating the primacy claim from the emit requirement makes each independently scannable.

**Signal 2 — Backward-reference terminal gate (C-17/C-19)**
"S-1 must not start until the line above has been written." The phrase "the line above" references the emit line by structural position rather than restating its content. This is the first confirmed backward-reference terminal gate form. It satisfies C-17 and C-19 (terminal gate position, names S-1) without forward-referencing the emit line explicitly. Confirms terminal gate criterion is positional + S-1-naming, not verbatim-form-dependent.

**Signal 3 — Semantic CONSTRAINT op-naming (C-21)**
"No artifact content production" instead of "No body generation." Confirms that C-21 matches the semantic of the prohibition (preventing artifact body assembly before S-0 completes), not the specific lexical form. Any phrase denoting body/content generation works. This is the first documented synonym confirmed for the 4th op.

**Signal 4 — Table carry verb variation (C-20)**
"Propagates to S-2 and S-3" in the downstream-use column instead of "Carry into S-2 and S-3." Confirms that C-20's table-register requirement is about naming the consumer labels (S-2 and S-3), not about using a specific verb. Propagation / carry / forward / handoff — all satisfy the criterion if the consumer labels are present.

---

### New Failure Traps Confirmed (R5)

| Failure | Criterion | Description |
|---------|-----------|-------------|
| 3-op CONSTRAINT omits body generation | C-21 | CONSTRAINT passes C-15 (3 op types named) but body generation absent; model may begin generating artifact content during S-0 |
| HS-critical-tier=1 collapsed into catch-all | C-22 | 4-row FLAG table passes C-11 (functional coverage) but tier=1 critical has no dedicated row; documented only implicitly |
| Preamble gate absent | C-19 | Terminal gate (C-17 pass) present; preamble gate missing; reader encounters resolution logic before any gate language |
| Table column describes use without naming consumers | C-20 | Table cell generic ("Used in S-3 flag computation"); standalone sentence names S-2+S-3; C-18 passes but C-20 table-register requirement unmet |

---

```json
{"top_score": 108, "all_essential_pass": true, "new_patterns": ["backward-reference terminal gate form ('S-1 must not start until the line above has been written') satisfies C-17/C-19 terminal gate -- reference to prior structural position equivalent to forward prohibition naming S-1", "two-clause preamble gate form ('This step executes first. Emit... before any other step begins.') strengthens C-19 by asserting step primacy as fact before stating emit requirement -- declarative+directive separation makes each clause independently scannable", "semantic CONSTRAINT op synonym confirmed: 'artifact content production' satisfies C-21 body-generation prohibition -- criterion is semantic (denotes body assembly), not lexical (does not require 'body generation' verbatim)", "table carry verb variation confirmed: 'Propagates to S-2 and S-3' satisfies C-20 table-register requirement -- verb-agnostic as long as consumer labels S-2 and S-3 are named in the cell"]}
```
