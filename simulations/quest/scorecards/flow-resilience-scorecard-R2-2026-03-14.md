Scorecard written to `simulations/quest/scorecards/flow-resilience-scorecard-R2-2026-03-14.md`.

---

## Round 2 Scorecard — flow-resilience

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-03 Resilience contract | 5/5 | 3/3 | 5/5 | **100** | YES |
| 1 | V-04 Combined: chaos + observability | 5/5 | 3/3 | 5/5 | **100** | YES |
| 1 | V-05 Full aspirational scaffold | 5/5 | 3/3 | 5/5 | **100** | YES |
| 4 | V-01 Chaos block per scenario | 5/5 | 3/3 | 4/5 | **98** | YES |
| 4 | V-02 Per-finding observability | 5/5 | 3/3 | 4/5 | **98** | YES |

**All 5 variations reach golden threshold.**

---

### Key findings

**The 98 ceiling for single-axis variations is exact.** V-01 (chaos, no observability) and V-02 (observability, no chaos) are symmetric misses — each closes exactly one of the two missing aspirational criteria. Under v2's 5-criterion aspirational tier, 4/5 = 8 points, total = 98. The only path to 100 is combining both axes.

**V-03's integration dividend is real.** Placing chaos + observability as rows in the same contract table as the four-field trace eliminates section-skip risk by eliminating the section boundary itself. The model fills rows in sequence; it never makes a structural decision about whether to include a chaos section. This is a different and arguably stronger mechanism than appending a separate sub-table (V-04/V-05).

**V-05 is the tightest structure.** The three criteria that distinguish it from V-04:
- **C-11**: Recovery is `client -> [action] / server -> [action]...` as explicit fill-in slots per actor, not just a named chain in the instruction
- **C-12**: `-> Selected: ___________` fill-in field eliminates the paraphrase path that free-text description still allows
- **C-13**: Completeness checklist in the output — "2 of 3" is self-annotating evidence of failure, not just a rubric miss

**Recommended golden**: V-05 for strictest structural enforcement; V-04 as production default (same score, simpler prompt, no checklist overhead).

**Round 3 potential**: Ceiling is closed under v2. A Round 3 variation could test V-03's integration approach + V-05's output checklist at lower output footprint.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Fill-in chaos test table appended at scenario level (4 rows: injection/expected/pass/fail) eliminates section-skip risk for C-09 -- model fills rows, never decides whether to include a chaos section", "Per-finding observability hook inline on every GAP/DCV/MRF entry (metric=|alert=|owner=) prevents C-10 omission by section-collapsing -- the hook is structurally adjacent to each finding, not in a separate section", "Completeness checklist as fill-in output element with N-of-3 counter satisfies C-13 marker-in-output condition -- an incomplete output is self-annotating evidence of failure, not just a rubric miss"]}
```
 PASS | 4-row chaos table pre-printed after Classification per scenario: Injection / Expected behavior / Pass signal / Fail signal |
| C-10 | Observability hooks | FAIL | No metric/alert/owner requirements; Section 4 findings carry no observability annotation |
| C-11 | Named actor chain in Recovery | PASS | Recovery template names the chain as fill instruction |
| C-12 | Constrained conflict vocabulary | PASS | last-write-wins | merge | manual-reconcile | reject-stale embedded in Section 3 |
| C-13 | Structural gap-merge prevention | PASS | "(mandatory -- do not omit or merge)" section header; per-type headers structurally distinct |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4/5

```
composite = (5/5 * 60) + (3/3 * 30) + (4/5 * 10)
          = 60 + 30 + 8
          = 98
```

**Score: 98 / 100 -- GOLDEN**

---

### V-02 -- Per-Finding Observability Hook

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three distinct sections |
| C-02 | Four-field structure per scenario | PASS | Pre-printed four-field trace table with actor-chain Recovery template |
| C-03 | Gap identification (3 types) | PASS | Section 4 mandatory annotation; observability hooks reinforce distinct type structure |
| C-04 | Distributed systems accuracy | PASS | Two-role structure; Developer validates SME |
| C-05 | Commerce domain grounding | PASS | SME floor anchor; commerce service vocabulary in Section 2 |
| C-06 | Severity + blast radius | PASS | Classification block pre-printed per scenario |
| C-07 | Recovery path specificity | PASS | Recovery template names actor chain |
| C-08 | Conflict resolution strategy | PASS | Constrained strategy list + adequacy requirement |
| C-09 | Chaos engineering test cases | FAIL | No chaos test block in any scenario; no injection/expected/pass/fail requirements |
| C-10 | Observability hooks | PASS | Every GAP, DCV, and MRF finding carries inline hook: metric/alert/owner; embedded per-finding -- cannot be omitted by section-collapsing |
| C-11 | Named actor chain in Recovery | PASS | Recovery template names actor chain |
| C-12 | Constrained conflict vocabulary | PASS | Constrained list in Section 3 |
| C-13 | Structural gap-merge prevention | PASS | "(mandatory -- do not omit or merge)" header; per-type headers; per-finding hooks reinforce structural distinctness |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4/5

```
composite = (5/5 * 60) + (3/3 * 30) + (4/5 * 10)
          = 60 + 30 + 8
          = 98
```

**Score: 98 / 100 -- GOLDEN**

V-01 and V-02 are symmetric misses: each closes one aspirational criterion and leaves the other open. The only path from 98 to 100 is combining both axes.

---

### V-03 -- Resilience Contract (Integrated)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three distinct scenarios: Full Connectivity Loss, Dependent Service Unavailable, Eventual Consistency Conflict |
| C-02 | Four-field structure per scenario | PASS | Contract table rows 1-4: State / Capability / Data at risk / Recovery -- all present per scenario |
| C-03 | Gap identification (3 types) | PASS | Section 4 "(mandatory -- do not omit or merge with scenarios)"; three separate subsection headers with numbered IDs |
| C-04 | Distributed systems accuracy | PASS | Single domain-expert persona ("Commerce / Distributed Systems domain expert"); chaos injection and expected-outcome fields force technical specificity |
| C-05 | Commerce domain grounding | PASS | "cashier / customer / operator" vocabulary in Capability field; Section 2 names specific services; commerce operations embedded in scenario framing |
| C-06 | Severity + blast radius | PASS | Classification block pre-printed per scenario |
| C-07 | Recovery path specificity | PASS | Recovery row template: actor-labeled step sequence; chain named in row |
| C-08 | Conflict resolution strategy | PASS | Contract row: strategy from constrained list with adequacy assessment |
| C-09 | Chaos engineering test cases | PASS | Contract rows: Chaos injection / Expected outcome / Pass signal / Fail signal -- same table as four-field trace; cannot be skipped as a section |
| C-10 | Observability hooks | PASS | Contract row: metric/alert/owner per scenario; three scenario-level hooks satisfy "at least two linked to a named scenario" |
| C-11 | Named actor chain in Recovery | PASS | Recovery row names chain as template notation |
| C-12 | Constrained conflict vocabulary | PASS | Contract row uses constrained vocabulary with adequacy assessment |
| C-13 | Structural gap-merge prevention | PASS | "(mandatory -- do not omit or merge with scenarios)"; per-type bold headers structurally distinct |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5

```
composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

Integration dividend: placing chaos + observability as rows in the same table as the four-field trace eliminates section-skip risk by eliminating the section boundary itself. No separate chaos section to omit -- only table rows to fill.

Note: observability is per-scenario (not per-finding in Section 4). C-10 passes because scenario-level linkage satisfies the criterion. Finding-level gaps do not have individual observability hooks.

---

### V-04 -- Combined: Chaos Per Scenario + Observability Per Finding

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three sections: Offline / Partial Service Failure / Eventual Consistency |
| C-02 | Four-field structure per scenario | PASS | Pre-printed four-field trace table; Recovery template names actor chain |
| C-03 | Gap identification (3 types) | PASS | Section 4 "(mandatory -- do not omit or merge)"; per-finding observability hooks inline enforce type distinctness |
| C-04 | Distributed systems accuracy | PASS | Two-role: Developer validates SME; chaos injection fields force technical specificity |
| C-05 | Commerce domain grounding | PASS | SME floor anchor; commerce service vocabulary in Section 2 |
| C-06 | Severity + blast radius | PASS | Classification block pre-printed per scenario |
| C-07 | Recovery path specificity | PASS | Recovery template names actor chain |
| C-08 | Conflict resolution strategy | PASS | Section 3 constrained vocabulary + adequacy requirement |
| C-09 | Chaos engineering test cases | PASS | 4-row chaos table appended after Classification per scenario; all three scenarios have blocks |
| C-10 | Observability hooks | PASS | Per-finding inline hooks on every GAP, DCV, and MRF entry: metric/alert/owner; cannot be omitted by section-collapsing |
| C-11 | Named actor chain in Recovery | PASS | Recovery template names actor chain as fill instruction |
| C-12 | Constrained conflict vocabulary | PASS | Constrained list embedded in Section 3 |
| C-13 | Structural gap-merge prevention | PASS | "(mandatory -- do not omit or merge)" header; per-type headers; per-finding hooks reinforce structural separation |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5

```
composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

V-04 confirms the ceiling: V-01 + V-02 axes are additive on the V-05 R1 base. The two mechanisms target different structural locations without conflict -- chaos blocks per-scenario, observability hooks per-finding.

---

### V-05 -- Full Aspirational Scaffold

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three sections: Offline / Partial Service Failure / Eventual Consistency |
| C-02 | Four-field structure per scenario | PASS | Pre-printed four-field trace table; Recovery field has explicit fill-in slots per actor: client -> [action] / server -> [action] / operator -> [action] / user -> [action] |
| C-03 | Gap identification (3 types) | PASS | Section 4 completeness checklist + "(mandatory -- do not omit or merge)"; per-finding observability hooks; numbered IDs |
| C-04 | Distributed systems accuracy | PASS | Two-role: Developer validates SME; constrained-vocabulary fields reduce free-text error surface |
| C-05 | Commerce domain grounding | PASS | SME floor anchor; Section 2 commerce service vocabulary |
| C-06 | Severity + blast radius | PASS | Classification block pre-printed per scenario |
| C-07 | Recovery path specificity | PASS | Recovery field uses explicit slot notation per actor -- strongest actor-chain enforcement of any variation |
| C-08 | Conflict resolution strategy | PASS | Explicit fill-in slot "-> Selected: ___________" after constrained vocabulary list -- strategy selection is mandatory, paraphrase path eliminated |
| C-09 | Chaos engineering test cases | PASS | 4-row chaos table per scenario; all rows empty fill-ins |
| C-10 | Observability hooks | PASS | Per-scenario observability hook AND per-finding inline hooks in Section 4 -- double coverage |
| C-11 | Named actor chain in Recovery | PASS | Recovery slots are fill-ins per actor: client -> [action] / server -> [action] / operator -> [action] / user -> [action] -- strongest C-11 mechanism of any variation |
| C-12 | Constrained conflict vocabulary | PASS | "-> Selected: ___________" fill-in after constrained list; paraphrase failure mode structurally eliminated |
| C-13 | Structural gap-merge prevention | PASS | Completeness checklist must appear in artifact with all three boxes checked and "Finding types present: 3 of 3" confirmed -- only variation where completeness marker is required output content |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5

```
composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

V-05 is the structurally tightest variation. Distinctions over V-03 and V-04:
- C-11: Recovery slots are fill-in per actor, not just a named-chain instruction
- C-12: "-> Selected:" field eliminates the last escape path from constrained vocabulary
- C-13: Completeness checklist is required output content; "2 of 3" is self-annotating evidence of incompleteness

---

## Excellence Signals -- Round 2

### E-1: Fill-in chaos test table at scenario level eliminates section-skip risk for C-09

V-01/V-04/V-05's per-scenario chaos table (4 rows: Injection / Expected behavior / Pass signal /
Fail signal) produces reliable C-09 compliance because the table is inside the scenario, not a
separate appendage section. V-03's approach is stronger: when chaos rows are in the same table
as the four-field trace, the model fills rows in sequence and never faces a structural decision
about whether to include a chaos section.

### E-2: Per-finding inline observability hook prevents C-10 omission by section-collapsing

V-02/V-04/V-05's approach of attaching metric/alert/owner directly to each numbered finding
means the model cannot omit observability by collapsing the section. If the finding exists, the
hook is structurally adjacent. This applies the same fill-vs-design principle that made the
four-field table effective in Round 1 -- now applied to observability at the finding granularity.

### E-3: Completeness checklist as fill-in output element satisfies C-13 marker-in-output condition

V-05's completeness checklist -- three checkbox lines plus "Finding types present: ___ of 3" --
must appear in the artifact with all boxes checked. This closes the gap between "do not omit or
merge" as a prompt instruction (V-01 through V-04) and "do not omit or merge" as evidence in the
output (V-05). An output with "2 of 3" is a visible failure signal in the artifact, not just a
rubric miss.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- 100/100 -- strongest structural enforcement in the 100-score cluster
- Strongest C-11 mechanism: per-actor fill-in slots in Recovery field
- Strongest C-12 mechanism: explicit "-> Selected:" field prevents paraphrase
- Strongest C-13 mechanism: completeness checklist as required output content

**V-04** is the recommended production default -- same score as V-05, simpler structure, no
checklist block. If production evidence confirms checklist compliance, promote V-05.

**Round 3 potential**: The 100-score ceiling is closed under v2 scoring. A Round 3 variation
might test whether V-03's integration approach (chaos + observability in one contract table per
scenario) combined with V-05's output checklist produces a structurally tighter prompt at lower
output footprint than V-05's two-section approach.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Fill-in chaos test table appended at scenario level (4 rows: injection/expected/pass/fail) eliminates section-skip risk for C-09 -- model fills rows, never decides whether to include a chaos section", "Per-finding observability hook inline on every GAP/DCV/MRF entry (metric=|alert=|owner=) prevents C-10 omission by section-collapsing -- the hook is structurally adjacent to each finding, not in a separate section", "Completeness checklist as fill-in output element with N-of-3 counter satisfies C-13 marker-in-output condition -- an incomplete output is self-annotating evidence of failure, not just a rubric miss"]}
```
