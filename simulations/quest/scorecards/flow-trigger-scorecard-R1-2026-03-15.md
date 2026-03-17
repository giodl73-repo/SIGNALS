## Quest Score — flow-trigger, Round 1 (Rubric v1)

*Rubric: C-01 through C-10, 5 essential / 3 recommended / 2 aspirational. No trace artifact — scoring prompt structural quality to produce passing outputs.*

---

### Scoring Methodology

Since the trace artifact is `placeholder`, each criterion is assessed as: **does this variation's prompt design create a structural constraint (cannot be omitted) or an advisory instruction (could be skipped)?** PARTIAL = the prompt creates the column or section but does not enforce actionable content.

---

### V-01 — Role Sequence: Cascade Mapper Before Enumerator

| ID | Tier | Pass? | Evidence |
|----|------|-------|----------|
| C-01 | E | **PASS** | Role A → B chain pre-commits all cascade rows; Role C C-1/C-2 reconciles every candidate with explicit FLAGGED GAP verdict |
| C-02 | E | **PASS** | Role B: "in execution order (sync before async within each layer)"; layer numbers from Role A constrain sequence |
| C-03 | E | **PASS** | Role B Reads requires `{Entity}.{Field}` (no generics); Produces requires specific verb+connector+target patterns; templates structurally reject "the record" |
| C-04 | E | **PASS** | Role C has C-3 (Storm), C-4 (Missing), C-5 (Circular) — each with named verdict template; "Every class requires a named verdict — even when clean" explicit |
| C-05 | E | **PASS** | PA Flow Type enforces `Automated – Dataverse / Automated – SharePoint / Instant / Scheduled` exact terms; Produces uses connector-specific verbs |
| C-06 | R | **PASS** | C-5 traces full directed edge set, checks back-edges, declares DAG/CYCLIC; "without edge-set enumeration is insufficient" explicit |
| C-07 | R | **PASS** | Role B "Fires When" includes "State at least one condition that would cause this trigger NOT to fire" |
| C-08 | R | **PARTIAL** | C-6 summary has Mitigation column; individual verdict sections (C-3/C-4/C-5) describe problems without requiring concrete fix steps — "debounce strategy," "concurrency control," etc. not mandated in verdict templates |
| C-09 | A | **PASS** | Execution Tier slot: `Async (~[latency] on [standard\|premium] tier)` — async delay window present; weak pass (no throttle/concurrency/24h window) |
| C-10 | A | **PASS** | Role A builds cascade graph before enumeration; Role B: "Cascaded triggers must appear as consecutive numbered entries — a trigger spawned by a side-effect write in row N must appear at row N+1. Do not annotate cascades separately." |

**Essential**: 5/5 pass → 60 pts
**Recommended**: 2.5/3 → 25 pts
**Aspirational**: 2/2 → 10 pts
**Composite: 95** | Golden threshold: MET (all essential pass, composite ≥ 80)

---

### V-02 — Output Format: Two-Tier Firing Table with Cascade Depth Column

| ID | Tier | Pass? | Evidence |
|----|------|-------|----------|
| C-01 | E | **PASS** | Section 3 registry reconciliation requires every trigger to appear; FLAGGED GAP is a structural gap; cascade rule makes cascade rows mandatory numbered entries |
| C-02 | E | **PASS** | Two-tier table (sync / async) structurally enforces execution-tier ordering; sequential row numbering continues across both tiers |
| C-03 | E | **PASS** | Input Fields: `{Entity}.{Field}` with "Never write 'the record'"; Output Action: required verb list; anti-examples table at bottom shows wrong/correct — vocabulary violations are visible non-conforming cells |
| C-04 | E | **PASS** | Section 4 requires all three: Trigger Storm, Missing Triggers, Circular Triggers; "All three anomaly class verdicts required. Each verdict must cite specific rows from Sections 2–3." |
| C-05 | E | **PASS** | PA Flow Type: "Exactly one of: Automated – Dataverse, Automated – SharePoint, Instant, Scheduled. No other forms accepted." Anti-examples table demonstrates exact correct/wrong pairings — strongest C-05 anti-example enforcement of all five variations |
| C-06 | R | **PASS** | Section 4 Circular: full edge set enumeration, back-edge check, DAG/CYCLIC; anti-example shows "No circular triggers" without edge-set fails |
| C-07 | R | **PASS** | "Not When" column required in both sync and async tables; "Unconditional only if the trigger truly has no conditions" |
| C-08 | R | **PARTIAL** | Section 5 "Recommended Mitigation" column; individual anomaly verdict blocks in Section 4 do not mandate concrete fix types |
| C-09 | A | **PASS** | Latency column: `~N min standard tier` or `~N min premium tier`; sync/async tier split in table structure itself |
| C-10 | A | **PASS** | Cascade Depth column required; "A trigger spawned by a side-effect write must appear at depth N+1 immediately after the parent row"; anti-example explicitly shows "(cascade trigger as footnote)" fails |

**Essential**: 5/5 → 60 pts
**Recommended**: 2.5/3 → 25 pts
**Aspirational**: 2/2 → 10 pts
**Composite: 95** | Golden threshold: MET

---

### V-03 — Phrasing Register: Conversational Named-Slot Blocks

| ID | Tier | Pass? | Evidence |
|----|------|-------|----------|
| C-01 | E | **PASS** | Step 2 candidate pre-scan creates denominator; Step 4 reconciles every candidate; FLAGGED GAP catches omissions |
| C-02 | E | **PASS** | "Number them in execution order — sync first, then async"; Depth indicator in block header provides implicit depth ordering |
| C-03 | E | **PASS** | Named slots Reads and Produces are required; "Empty slots are failures"; required verb list for Produces; absent values are visible as blank lines |
| C-04 | E | **PASS** | Step 4: Q1 (Storm), Q2 (Missing), Q3 (Circular) — "Every question gets a named verdict. A verdict without evidence from Step 3 is marked [INSUFFICIENT]" |
| C-05 | E | **PASS** | Type slot enforces exact PA flow types; Produces requires connector vocabulary |
| C-06 | R | **PASS** | Q3 constructs edge set, checks back-edges, declares DAG/CYCLIC; named verdict required with edge set enumeration |
| C-07 | R | **PASS** | "Doesn't fire when" is a required named slot — absence is a visible blank line |
| C-08 | R | **PARTIAL** | Step 5 has "Fix" column (conditional on anomalies confirmed); individual verdict blocks (Q1/Q2/Q3) do not require concrete fix types in the verdict text |
| C-09 | A | **PASS** | Tier slot: `Async (~[N] min [standard\|premium] tier)` — latency window present; weak pass |
| C-10 | A | **PASS** | "Cascade rule: if this trigger's Side effects writes a field... that trigger is the very next numbered block (Depth incremented by 1). Do not annotate it separately." Cascade rule explicit though advisory |

**Essential**: 5/5 → 60 pts
**Recommended**: 2.5/3 → 25 pts
**Aspirational**: 2/2 → 10 pts
**Composite: 95** | Golden threshold: MET

*Note: Weakest structural enforcement of the five — instructions are clear but lack the handoff constraints and inline violation markers of V-04/V-05. Likely produces passing outputs but with higher variance under adversarial scenarios.*

---

### V-04 — Combined: Lifecycle Emphasis + Role Sequence (Four-Pass)

| ID | Tier | Pass? | Evidence |
|----|------|-------|----------|
| C-01 | E | **PASS** | Pass 1 candidate scan as denominator; Pass 4A reconciles every candidate; "Pass 3 may not add triggers that weren't in the Pass 2 chain without a [NOT IN PASS 2 CHAIN — reason] note" — strongest C-01 boundary enforcement |
| C-02 | E | **PASS** | Pass 2 produces explicit ordered sync/async execution chain; Pass 3 handoff: "must number triggers in this exact order. Pass 3 must not reorder or omit entries from this chain." — structurally strongest C-02 enforcement |
| C-03 | E | **PASS** | Pass 3 table: Input Fields (`{Entity}.{Field}`, no generic), Output Action (required verb list), Side Effect Writes (`{Entity}.{Field} = {value}`); P2-Ref column creates structural audit trail |
| C-04 | E | **PASS** | Pass 4: 4B (Storm), 4C (Missing), 4D (Circular) — each with named verdict template; all three required |
| C-05 | E | **PASS** | Pass 3 PA Flow Type: "Automated – Dataverse, Automated – SharePoint, Instant, Scheduled — exact PA vocabulary only" |
| C-06 | R | **PASS** | Pass 4D carries forward Pass 2 directed edge set; back-edge check; DAG/CYCLIC property; carries the cascade graph from Pass 2 rather than reconstructing from prose |
| C-07 | R | **PASS** | Pass 3 "Fires When" and "Not When" columns; "At least one condition that would prevent this trigger from firing" |
| C-08 | R | **PARTIAL** | Pass 4E Risk-Ranked Summary has Mitigation column; individual Pass 4B/C/D verdict sections describe findings without mandating actionable fix vocabulary |
| C-09 | A | **PASS** | Pass 3 Tier: "Async with latency: ~N min [standard\|premium] tier" |
| C-10 | A | **PASS** | Pass 2 is a dedicated cascade-map pass; Pass 3 consumes Pass 2 output as the ordering constraint — C-10 is load-bearing: Pass 3 ordering depends on Pass 2 cascade chain. Strongest C-10 enforcement of all five variations |

**Essential**: 5/5 → 60 pts
**Recommended**: 2.5/3 → 25 pts
**Aspirational**: 2/2 → 10 pts
**Composite: 95** | Golden threshold: MET

*Highest structural enforcement for C-02 and C-10 — the Pass 2 → Pass 3 handoff constraint cannot be circumvented without a structural violation marker.*

---

### V-05 — Combined: Inertia Framing + Output Format

| ID | Tier | Pass? | Evidence |
|----|------|-------|----------|
| C-01 | E | **PASS** | Step 1 candidate pre-scan; Step 3 denominator reconciliation; C-Ref column ties each firing trigger to a Step 1 candidate — every trigger in the firing table has a candidate provenance |
| C-02 | E | **PASS** | Sync tier first, async tier second in table; sequential numbering across both tiers |
| C-03 | E | **PASS** | Input Fields: `{Entity}.{Field}`; Output Action: required verb list with inline `[VOCAB FAIL: "{exact text}" — should be: "{correct form}"]` markers — violations become visible cells rather than hidden prose |
| C-04 | E | **PASS** | Step 4: Trigger Storm, Missing Triggers, Circular Triggers — all three, each with named verdict template |
| C-05 | E | **PASS** | PA vocabulary enforcement section enumerates flow types, field references, action verbs, connector names; non-conforming vocabulary triggers inline VOCAB FAIL cells — structurally strongest C-05 enforcement |
| C-06 | R | **PASS** | Step 4 Circular: edge set construction, back-edge check, DAG/CYCLIC; named verdict with edge set |
| C-07 | R | **PASS** | "Fires When / Not When" columns explicitly required; "Unconditional only if no conditions" |
| C-08 | R | **PARTIAL** | Step 5 risk-ranked summary with Mitigation column; individual Step 4 verdict blocks do not mandate actionable fix types |
| C-09 | A | **PASS** | Latency column: `~N min [standard\|premium] tier` |
| C-10 | A | **PASS** | Failure Mode 3 section names cascade truncation as a failure mode and its structural fix; "It is never acceptable to leave a cascaded trigger as an annotation or note — if it executes, it has a row" |

**Essential**: 5/5 → 60 pts
**Recommended**: 2.5/3 → 25 pts
**Aspirational**: 2/2 → 10 pts
**Composite: 95** | Golden threshold: MET

*Highest structural enforcement for C-05 and C-03 — inline VOCAB FAIL markers make vocabulary violations visible in the output rather than hidden. Failure mode framing provides motivational enforcement alongside structural.*

---

## Ranking

| Rank | Variation | Composite | All Essential | Distinguishing Quality |
|------|-----------|-----------|---------------|----------------------|
| 1 (tie) | **V-04** | 95 | YES | Strongest C-02 + C-10: Pass 2 → Pass 3 handoff makes cascade ordering a load-bearing structural constraint |
| 1 (tie) | **V-05** | 95 | YES | Strongest C-03 + C-05: VOCAB FAIL inline markers make vocabulary violations structurally visible; failure mode framing motivates compliance |
| 3 | **V-01** | 95 | YES | Strong C-10: dedicated Cascade Mapper role pre-commits all cascade rows before enumeration begins |
| 4 | **V-02** | 95 | YES | Strong C-05: anti-examples table provides the clearest wrong/correct vocabulary reference; two-tier table is clean |
| 5 | **V-03** | 95 | YES | Adequate coverage; simplest to follow; highest variance under adversarial scenarios due to advisory (not structural) enforcement |

**C-08 is the universal weak point**: all five variations place mitigation in a summary table column but do not enforce actionable fix vocabulary (debounce strategy, cycle-break condition, etc.) in individual anomaly verdict sections.

---

## Excellence Signals (from V-04 and V-05)

**Pattern 1 — Cascade-map as an ordering constraint**: V-04's dedicated Pass 2 makes the cascade graph an explicit input to Pass 3. The execution order cannot be set arbitrarily because Pass 3's sequencing depends on Pass 2's output. This converts C-10 from an advisory rule into a structural dependency — the only way to omit a cascade row is to also omit it from Pass 2's chain, which creates a double-violation that is harder to hide.

**Pattern 2 — Inline vocabulary failure markers**: V-05's `[VOCAB FAIL: "{exact text}" — should be: "{correct form}"]` format makes non-conforming vocabulary appear as a visible cell in the output rather than a hidden prose deficiency. This inverts the enforcement model: instead of requiring a reviewer to catch vague language, the structure asks the LLM to self-annotate failures. The reviewer sees the violation without needing domain expertise to detect it.

**Pattern 3 — Failure mode framing as motivational enforcement**: V-05's four named failure modes (undeclared denominator, vocabulary drift, cascade truncation, post-hoc pathology scan) connect each protocol requirement to the specific failure it prevents. This provides a "why" for each structural constraint, which increases reliability when the LLM encounters edge cases not explicitly covered by the protocol rules.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["Cascade-map as a dedicated pass produces the execution ordering as a required input to the enumeration pass, converting C-10 from an advisory rule into a structural dependency that cannot be violated without a double-omission", "Inline VOCAB FAIL cell markers surface vocabulary violations as visible output cells rather than hidden prose, creating structural self-annotation enforcement for C-03 and C-05", "Failure mode framing connects each protocol step to the named failure it prevents, providing motivational enforcement alongside structural constraints"]}
```
