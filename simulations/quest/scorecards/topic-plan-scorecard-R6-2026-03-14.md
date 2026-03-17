## topic-plan — Round 6 Scoring (v6 rubric)

---

### Baseline: C-01–C-23 (carried from Round 5)

All five variations carry Round 5's mechanisms unchanged. The coverage matrix confirms PASS on all 23 pre-v6 criteria for every variation. This establishes a fixed baseline before scoring the four discriminators.

**Baseline contribution:**
- Essential (C-01–C-05): 5/5 × 60 = **60 pts**
- Recommended (C-06–C-08): 3/3 × 30 = **30 pts**
- Aspirational C-09–C-23: 15/19 criteria × 5 pts each = **75 pts**
- Baseline total: **165 pts** (identical across all variations)

Remaining: 4 criteria (C-24–C-27) × 5 pts each = 20 pts discriminator pool.

---

### C-24–C-27 Discriminator Scoring

| | C-24 | C-25 | C-26 | C-27 | Aspirational pts added |
|--|------|------|------|------|------------------------|
| **V-01** | PASS | FAIL | FAIL | FAIL | +5 |
| **V-02** | PARTIAL | PASS | FAIL | FAIL | +7.5 |
| **V-03** | PARTIAL | FAIL | PASS | FAIL | +7.5 |
| **V-04** | PARTIAL | FAIL | PASS | PASS | +12.5 |
| **V-05** | PASS | PASS | PASS | PASS | +20 |

**Evidence notes:**

**V-01 — C-24 PASS:** Dedicated Step 1b substep with Assumption ID column + "Why this is a delta candidate" column + signal inventory references assumption IDs. This is the named-act structure C-24 requires — assumption extraction as a separate act, not a row embedded in the stated-fields table. **C-25 FAIL:** No "If unchanged" column anywhere. **C-26 FAIL:** No upfront schema block — per-step adjacent declarations only. **C-27 FAIL:** Step 3 anti-pattern checkpoint only; no cascade to proposals or diff.

**V-02 — C-24 PARTIAL:** "What it assumed without naming" appears as a row in the Step 1 stated-fields table. Present, but not the dedicated substep with its own Assumption ID column that C-24 requires. The row can be filled mechanically; no "Why this is a delta candidate" reasoning column. **C-25 PASS:** Full "If unchanged" column with consequence-reasoning guidance; null rows carry N/A; "Nothing changes" explicitly prohibited as an entry. The preamble frames every proposal as a cost-of-inaction decision — framing is the distinguishing mechanism. **C-26 FAIL:** No consolidated upfront schema block. **C-27 FAIL:** Step 3 only.

**V-03 — C-24 PARTIAL:** Same as V-02 — "What it assumed without naming" row in Step 1 table, no dedicated substep. **C-25 FAIL:** No "If unchanged" column — the OUTPUT CONTRACT's proposals schema includes ID, Type, Change, Delta Finding, Evidence, Confidence but not inertia. **C-26 PASS:** Complete OUTPUT CONTRACT with all 6 table schemas + ★ column designations + all null templates declared before Step 1. The model commits to the full structural contract before touching any file. **C-27 FAIL:** Step 3 anti-pattern only; V-03 does not produce schema-commitment statements before proposals or diff.

**V-04 — C-24 PARTIAL:** Same partial mechanism as V-02/V-03. **C-25 FAIL:** Output Schema before Step 1 lists proposals columns as ID, Type, Change, Delta Finding, Evidence, Confidence — no "If unchanged" column in the priming block or in the proposals table itself. **C-26 PASS:** Complete Output Schema with all 6 tables + ★ designations before Step 1 — contract is committed before any reading. **C-27 PASS:** Three auditable checkpoints: Step 3 produces anti-pattern label + "Delta Findings schema: Finding ID ★, Strategy assumed ★..." verbatim; Step 6 produces "Proposals schema confirmed: Proposal ID ★, Type ★, Change ★, Delta Finding ★, Evidence ★, Confidence ★..." verbatim; Step 7 produces "Diff schema confirmed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★, Proposal ★" verbatim. Three independent auditable points.

**V-05 — C-24 PASS:** Dedicated Step 1b with Assumption ID + "Why this is a delta candidate" column; signal inventory has "Confirms or challenges which assumption?" column linking each signal to Step 1b assumption IDs. This creates a 4-step traceability chain: A-NN → S-NN → F-NN → Proposal ID. **C-25 PASS:** "If unchanged" column in proposals table + null rows carry N/A; OUTPUT CONTRACT primes the column as ★ before Step 1; Step 6 checkpoint statement names "If unchanged ★ (forward causal claim...)" verbatim — depth requirement is both instructed and verifiable as checkpoint output. **C-26 PASS:** Complete OUTPUT CONTRACT with all 6 schemas + ★ columns + null templates, including the "If unchanged ★" column in the Proposals schema — depth columns are in the priming block. **C-27 PASS:** Same 3-checkpoint cascade as V-04, but Step 6 checkpoint statement includes "If unchanged ★" as named mandatory column — the inertia column is committed to in verifiable output before the table is built.

---

### Composite Scores

Using formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/19 × 95)`

| Variation | Essential | Recommended | Aspirational (pass/19) | Total |
|-----------|-----------|-------------|------------------------|-------|
| V-01 | 60 | 30 | 16/19 → 80.0 | **170.0** |
| V-02 | 60 | 30 | 16.5/19 → 82.5 | **172.5** |
| V-03 | 60 | 30 | 16.5/19 → 82.5 | **172.5** |
| V-04 | 60 | 30 | 17.5/19 → 87.5 | **177.5** |
| V-05 | 60 | 30 | 19/19 → 95.0 | **185.0** |

**Rank: V-05 > V-04 > V-02 = V-03 > V-01**

---

### Ranking and Analysis

**1st — V-05 (185):** The only variation to achieve full aspirational coverage. The critical structural advantage over V-04 is double: (a) C-24's assumption-to-signal cross-reference column creates a 4-step traceability chain that didn't exist in any prior round, and (b) C-25's inertia column is simultaneously a depth requirement (column content) and an enforcement checkpoint (named in Step 6's verbatim commitment statement). The synergy claim in V-05's hypothesis holds: depth criteria survive context pressure only when the cascade checkpoints name them as ★ mandatory — not just instruct them in step guidance.

**2nd — V-04 (177.5):** Achieves both enforcement criteria (C-26 + C-27) cleanly, proving the cascade mechanism works independently of the depth criteria. The gap from V-04 to V-05 (7.5 pts) isolates the combined value of C-24 PASS + C-25 PASS vs two PARTIAL/FAILs — approximately 7.5 pts additional aspiration.

**3rd (tie) — V-02 = V-03 (172.5):** Each cleanly isolates one criterion. V-02's unique mechanism — "Nothing changes" is explicitly prohibited — distinguishes it from every other variation. V-03's null-template consolidation in the priming block is a genuine structural improvement over per-step distribution. They tie because a C-24 PARTIAL + one PASS equals the same aspirational score as a C-24 PASS + three FAILs only when the PARTIAL is 0.5; the single PASS offsets the C-24 gap.

**5th — V-01 (170):** Full C-24 PASS but fails every other new criterion. The assumption-mining substep is the strongest single-axis mechanism for C-24, but its score ceiling without C-25/C-26/C-27 is lower than the V-02/V-03 ceiling. A depth criterion alone without enforcement infrastructure ranks below an enforcement pair.

---

### Excellence Signals from V-05

**Signal 1 — Depth columns must appear in cascade checkpoint statements, not only in column guidance.** V-05's Step 6 checkpoint names "If unchanged ★ (forward causal claim: what degrades or closes if deferred)" verbatim before the table is built. This is the mechanism that distinguishes structural compliance from genuine consequence reasoning: a model that produces the checkpoint statement has committed to the inertia column as a mandatory verifiable output, not a column that can be filled with a synonym of the delta finding under context pressure. The pattern generalizes: any depth criterion that adds a column should also have that column named as ★ in the cascade checkpoint statement at its step — making depth enforcement auditable independently of whether the column instruction was read.

**Signal 2 — Signal inventory should cross-reference assumption IDs, creating an auditable 4-step traceability chain.** V-05's "Confirms or challenges which assumption?" column in the signal inventory links each artifact to a Step 1b Assumption ID. This means every finding in Step 3 can be traced backward: F-NN ← S-NN ← A-NN. Prior variations (and prior rounds) left the assumption extraction and signal inventory as parallel but unconnected acts — the assumption was extracted, the signal was read, but no column in the inventory forced the model to evaluate each signal against the assumption inventory. The cross-reference column makes the C-24 mechanism load-bearing through Step 3, not just at Step 1b.

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["Depth columns must appear in cascade checkpoint statements as ★ mandatory — any depth criterion adding a required column should name that column in the verbatim schema-commitment statement at its step's checkpoint, making depth enforcement verifiable independently of whether step guidance was read", "Signal inventory should include an assumption cross-reference column linking each artifact to Step 1b Assumption IDs — this creates an auditable 4-step chain (assumption → signal → finding → proposal) and makes unstated-assumption extraction load-bearing through the delta step, not only at the strategy read step"]}
```
