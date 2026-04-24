## flow-lifecycle — Quest Score Run, Round 1

---

### Scoring Notes

**Trace artifact**: placeholder — no golden output exists yet. Scoring evaluates prompt structure's *likelihood to satisfy* each criterion, not actual output.

**Variations received**: V-01 and V-02 only. V-03 through V-05 were not included in this run. Scoring proceeds on V-01 and V-02.

---

### V-01 — Roles First

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | State Transition Coverage | **PASS** | Step 2 mandates ≥6 states with explicit entry/exit triggers and owner role — "no then X happens" is directly echoed |
| C-02 | Exception Flow Traces | **PASS** | Step 4 requires ≥3 exceptions, each naming triggering condition, divergence state, and path to recovery or failure terminal |
| C-03 | Terminal State Completeness | **PASS** | Step 6 explicitly requires 1 success + 1 failure terminal, with verification that every traced path reaches a named terminal |
| C-04 | Bottleneck and Gap Identification | **PASS** | Step 7 asks for ≥2 bottlenecks (cause + impact) and ≥1 process gap (missing step + consequence) |
| C-05 | Domain Role Assignment | **PASS** | Step 1 demands domain-qualified titles with explicit anti-pattern example ("not 'Approver'"); every gate must have an owner before proceeding |
| C-06 | Parallel Path Modeling | **PASS** | Step 5 asks for named parallel paths + join condition; explicit "state why" required if none exist |
| C-07 | Decision Point Explicitness | **PASS** | Step 3 mandates ≥3 decision points with condition, owner role, and all outcome branches |
| C-08 | Edge Case Enumeration | **PASS** | Step 8 asks for 2+ edge cases distinct from exceptions, with scenario + gap reason + consequence |
| C-09 | Cross-Lifecycle Dependencies | **PASS** | Step 9 explicitly names the requirement: direction, partner lifecycle, coupling state |
| C-10 | SLA and Timing Annotation | **FAIL** | No timing or SLA language anywhere in the prompt |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 1/2 → 5  
**Composite: 95**

---

### V-02 — Table-First

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | State Transition Coverage | **PASS** | Table 2 columns (Entry Trigger, Exit Trigger, Owner Role) enforce the requirement directly; ≥6 rows mandated |
| C-02 | Exception Flow Traces | **PASS** | Table 4 has Triggering Condition + Divergence State + Exception Path + Terminal State — all four fields required by C-02 |
| C-03 | Terminal State Completeness | **PASS** | Table 2 State Type column flags terminals; row classifier "(success)" vs "(failure/cancel)" required |
| C-04 | Bottleneck and Gap Identification | **PASS** | Tables 6 and 7 explicitly require ≥2 bottleneck rows and ≥1 gap row with cause/consequence columns |
| C-05 | Domain Role Assignment | **PASS** | Table 1 requires ≥3 domain-qualified roles with gating ownership |
| C-06 | Parallel Path Modeling | **PASS** | Table 5 requires join condition; explicit "None" row with rationale required if no parallel paths |
| C-07 | Decision Point Explicitness | **PASS** | Table 3 has Condition + Owner Role + Branch columns; ≥3 rows with all branches referencing Table 2 states |
| C-08 | Edge Case Enumeration | **FAIL** | Prompt ends at Table 7 (Process Gaps) — no edge case table present |
| C-09 | Cross-Lifecycle Dependencies | **FAIL** | Not present |
| C-10 | SLA and Timing Annotation | **FAIL** | Not present |

**Essential**: 5/5 → 60  
**Recommended**: 2/3 → 20  
**Aspirational**: 0/2 → 0  
**Composite: 80**

---

### Ranking

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| 1 | **V-01** | **95** | Yes | Covers 9/10 criteria; only C-10 (SLA) absent |
| 2 | V-02 | 80 | Yes | Structural enforcement is strong; incomplete — V-03–V-05 not provided |
| — | V-03–V-05 | n/a | n/a | Not received |

---

### Excellence Signals (from V-01)

1. **Role-first ordering creates ownership pressure throughout** — assigning the expert panel in Step 1, before any state is named, forces domain vocabulary into every subsequent transition. Generic phrasing can't survive the named-owner requirement.

2. **Explicit anti-pattern negation** — the prompt names the failure mode directly ("not 'Approver' — use 'Senior Credit Analyst'"), which blocks the most common rubric failure without requiring the model to infer it.

3. **Sequential gate locking** — "Do not proceed to Step 2 until every role is named" creates a structural dependency that prevents skipping the hardest criterion (C-05).

4. **Terminal state verification pass** — Step 6 closes the loop explicitly: "Verify: every traced path (happy + exception) reaches a named terminal." This converts C-03 from a count check into a structural completeness check.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["role-first ordering forces domain vocabulary into all downstream transitions", "explicit anti-pattern negation blocks common rubric failures without inference", "sequential gate locking prevents skipping hard criteria", "terminal state verification pass converts count check into structural completeness check"]}
```
