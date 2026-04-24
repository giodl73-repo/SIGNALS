## flow-trigger — Round 5 Scoring (Rubric v2)

**Rubric**: C-01 through C-13 | **Formula**: essential 60 + recommended 30 + aspirational 10

---

### V-01 — Scenario Decomposition Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | **PASS** | Step 2b requires one entry per C-ID; Gate 2 enforces F + NF = N |
| C-02 | Execution order stated | **PASS** | "Ordered by execution tier and sequence within tier" |
| C-03 | Inputs/outputs per trigger | **PASS** | `Reads:` / `Produces:` / `Writes:` explicit slots in firing entry format |
| C-04 | Three anomaly verdicts | **PASS** | Phase 3 requires exactly three verdict blocks; Gate 3 verifies |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract + platform named in event tuple |
| C-06 | Circular trigger analysis | **PASS** | Phase 3: directed edge set + back-edge detection required |
| C-07 | Conditional branch paths | **PASS** | `Condition (EXECUTED)` and `Condition (SKIPPED would be)` in firing entry; `Condition (WOULD FIRE if)` in gap entry |
| C-08 | Anomaly remediation proposed | **PASS** | `Remediation:` field in every verdict block format |
| C-09 | Execution tier and latency flags | **PASS** | `Execution tier:` and `Latency:` slots in firing entry |
| C-10 | Cascade completeness | **PASS** | `Cascades to: Entry #{N}` spawned when `Writes` is non-empty |
| C-11 | Candidate denominator declared | **PASS** | `DENOMINATOR: N = {count} candidates within scope of Phase 1 event tuple` before Step 2b |
| C-12 | Gap tokens for non-firing candidates | **PASS** | `[NOT FIRED — {name}]` format in gap entries; Gate 2 checks all C-IDs accounted for |
| C-13 | Anomaly verdict evidence citation | **PASS** | `Rows inspected: Entry {#} through Entry {#}` required; Gate 3 explicitly enforces citations |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 5/5

**New mechanism**: DECOMPOSITION GATE (Phase 1 event tuple) closes candidate scope structurally before any candidate is named — first variation across all rounds to make false-positive candidates impossible by definition rather than by correctness check.

**Composite: 100/100** | All essential: YES

---

### V-02 — Counterfactual Pairing

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | **PASS** | Step 2 enumerates all C-IDs; Gate 2 checks F + NF = N |
| C-02 | Execution order stated | **PASS** | "Ordered by execution tier and sequence within tier" |
| C-03 | Inputs/outputs per trigger | **PASS** | `Reads:` / `Produces:` / `Writes:` slots in firing entry |
| C-04 | Three anomaly verdicts | **PASS** | Step 3 requires three verdict blocks; Gate 3 verifies |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract with approved terms |
| C-06 | Circular trigger analysis | **PASS** | Step 3: directed edge set, full edge list, back-edge detection required |
| C-07 | Conditional branch paths | **PASS** | `Fires because:` + `Counterfactual [Flip to NOT FIRE]` captures firing branch and skipped-branch logic; gap entry has `Counterfactual [Flip to FIRE]` |
| C-08 | Anomaly remediation proposed | **PASS** | `Remediation:` in verdict block format |
| C-09 | Execution tier and latency flags | **PASS** | `Execution tier:` and `Latency:` slots in firing entry |
| C-10 | Cascade completeness | **PASS** | `Cascades to:` slot in firing entry |
| C-11 | Candidate denominator declared | **PASS** | `DENOMINATOR: N = {count} candidates` in Step 1 before enumeration |
| C-12 | Gap tokens for non-firing candidates | **PASS** | `[NOT FIRED — {name}]` with `Counterfactual [Flip to FIRE]`; Gate 2 enforces all C-IDs present |
| C-13 | Anomaly verdict evidence citation | **PASS** | `Rows inspected: Entry {#} through Entry {#}` in every verdict; Gate 3 verifies |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 5/5

**New mechanism**: Bilateral counterfactual pair for every entry collapses C-07 and C-12 into a single unified obligation — both the "skipped branch" and the "gap token" are satisfied by the mandatory pair, making separate compliance checks redundant.

**Composite: 100/100** | All essential: YES

---

### V-03 — Non-Firer-First Enumeration

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | **PASS** | Block 1 + Block 2 cover all C-IDs; Gate B2 enforces F + NF = N |
| C-02 | Execution order stated | **PASS** | Block 2 firing entries ordered by execution tier and sequence |
| C-03 | Inputs/outputs per trigger | **PASS** | `Reads:` / `Produces:` / `Writes:` slots in Block 2 firing entry |
| C-04 | Three anomaly verdicts | **PASS** | Block 3 requires three verdict blocks; Gate B3 verifies |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract present |
| C-06 | Circular trigger analysis | **PASS** | Block 3: edge set from Block 2 Cascades-to fields; back-edge detection with edge list |
| C-07 | Conditional branch paths | **PASS** | Block 2 has `Condition (EXECUTED)` + `Condition (SKIPPED would be)`; Block 1 has `Condition (WOULD FIRE if)` |
| C-08 | Anomaly remediation proposed | **PASS** | `Remediation:` in verdict block format |
| C-09 | Execution tier and latency flags | **PASS** | `Execution tier:`, `Latency:`, `Latency note:` in Block 2 |
| C-10 | Cascade completeness | **PASS** | `Cascades to:` in Block 2 firing entry |
| C-11 | Candidate denominator declared | **PASS** | `DENOMINATOR: N = {count} candidates` in Block 0 |
| C-12 | Gap tokens for non-firing candidates | **PASS** | Block 1 is the structurally prior gap-disposal block; every non-firer disposed before Block 2 opens; `[DEFERRED TO BLOCK 2]` placeholders for firers |
| C-13 | Anomaly verdict evidence citation | **PASS** | Block 3 verdicts require block-prefixed row citations (`Block N, Entry #`) — more precise than any prior variation |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 5/5

**New mechanism**: Non-firer-first ordering makes C-12 structurally prior — Block 1 (gap disposal) must complete before Block 2 (firing sequence) can begin. The `[DEFERRED TO BLOCK 2]` placeholder for firing candidates ensures every C-ID has an explicit Block 1 disposition, eliminating trailing-cleanup risk.

**Composite: 100/100** | All essential: YES

---

### V-04 — Witness Citation Per Entry

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | **PASS** | Pass 2 enumerates all C-IDs; Gate 2 enforces F + NF = N |
| C-02 | Execution order stated | **PASS** | "Ordered by execution tier and sequence" |
| C-03 | Inputs/outputs per trigger | **PASS** | `Reads:` / `Produces:` / `Writes:` slots in firing entry |
| C-04 | Three anomaly verdicts | **PASS** | Pass 3 requires three verdict blocks; Gate 3 verifies |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract + `Registration witness` per entry makes C-05 a per-row structural requirement |
| C-06 | Circular trigger analysis | **PASS** | Pass 3: edge set, back-edge detection, edge list required |
| C-07 | Conditional branch paths | **PASS** | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` in firing entry; `Condition (WOULD FIRE if)` in gap entry |
| C-08 | Anomaly remediation proposed | **PASS** | `Remediation:` in verdict block format |
| C-09 | Execution tier and latency flags | **PASS** | `Execution tier:` and `Latency:` slots in firing entry |
| C-10 | Cascade completeness | **PASS** | `Cascades to:` in firing entry |
| C-11 | Candidate denominator declared | **PASS** | `DENOMINATOR: N = {count} candidates` in Pass 1; `UNWITNESSED count: U = {count}` adds second denominator dimension |
| C-12 | Gap tokens for non-firing candidates | **PASS** | `[NOT FIRED — {name}]` with `Registration witness` + `Reason not fired` in gap entry |
| C-13 | Anomaly verdict evidence citation | **PASS** | `Rows inspected: Entry {#} through Entry {#}` + `registration witness` grounding in evidence |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 5/5

**New mechanism**: Per-entry `Registration witness` citation turns C-05 from a global document-level declaration into a per-row structural check. `[UNWITNESSED]` marker flags inferred (potentially hallucinated) triggers; `UNWITNESSED count: U` is a grounding health metric visible to the reviewer. Gap entries also carry witness fields, confirming whether the trigger is registered but not firing vs. not registered at all.

**Composite: 100/100** | All essential: YES

---

### V-05 — Combined: Decomposition + Counterfactual Pairs + Authority Contracts

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | **PASS** | Role B produces one entry per C-ID from Role A; Gate B enforces F + NF = N |
| C-02 | Execution order stated | **PASS** | Most precise ordering rules across all R5 variations: pre-validation → pre-op sync → rank within stage → post-op sync → async → background |
| C-03 | Inputs/outputs per trigger | **PASS** | `Reads:` / `Produces:` / `Writes:` in Role B firing entry |
| C-04 | Three anomaly verdicts | **PASS** | Role C requires exactly three verdict blocks; Gate C verifies |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract with definitions column |
| C-06 | Circular trigger analysis | **PASS** | Role C: directed edge set, full edge list, back-edge detection required |
| C-07 | Conditional branch paths | **PASS** | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` in firing entry; `Condition (SKIPPED)` in gap entry |
| C-08 | Anomaly remediation proposed | **PASS** | `Remediation:` in verdict block format |
| C-09 | Execution tier and latency flags | **PASS** | `Execution tier:` and `Latency:` in firing entry |
| C-10 | Cascade completeness | **PASS** | `Cascades to:` in firing entry |
| C-11 | Candidate denominator declared | **PASS** | Gate A2 enforces `DENOMINATOR: N` before Role B begins |
| C-12 | Gap tokens for non-firing candidates | **PASS** | `[NOT FIRED — {name}]` gap entry format in Role B |
| C-13 | Anomaly verdict evidence citation | **PASS** | `Rows inspected: Entry {#} through Entry {#}` mandatory in Role C; Gate C enforces; "verdict block without row citations is a structural violation" |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 5/5

**New mechanisms**: (1) Role prohibition contracts — "A prohibited action appearing in a role's output is a structural violation" — enforce role boundaries more strongly than any prior variation; violations are self-detectable by inspection. (2) Counterfactual invalidity constraint: `"Remove the automation registration" is not a valid counterfactual — it must be a change to the triggering event, field value, or condition` — first variation to gate counterfactual *quality*, blocking trivial loop-out answers. (3) Explicit multi-level execution ordering rules (pipeline stage → rank within stage) make C-02 the most precisely specified of any R5 variation.

**Composite: 100/100** | All essential: YES

---

## Round 5 Summary

| Variation | Essential | Recommended | Aspirational | Composite | All Essential |
|-----------|-----------|-------------|--------------|-----------|---------------|
| V-01 | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-02 | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-03 | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-04 | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-05 | 60/60 | 30/30 | 10/10 | **100** | YES |

**Rubric v2 is fully saturated for the fifth consecutive round.** All five structural axes (decomposition gate, counterfactual pairing, non-firer-first ordering, witness citation, combined authority-contract stack) achieve 100/100.

---

## Excellence Signals from R5 — Ranking

**V-05** is the highest-quality variation by structural depth, not score:
- Prohibition-based authority contracts make role drift structurally detectable (not just discouraged)
- Counterfactual invalidity constraint blocks trivial counterfactual answers (`"Remove the registration"` explicitly disallowed)
- Explicit tier-within-tier ordering rules (pre-op/post-op, rank within stage) are the most precise execution model of any variation across all rounds

**V-01** introduces the most consequential single mechanism: the decomposition gate closes the candidate scope before any C-ID is named — making false-positive candidates impossible by structural exclusion rather than correctness review.

**V-04** introduces the most novel grounding mechanism: per-entry witness citation with `[UNWITNESSED]` markers converts the latent false-positive risk into a visible, countable metric.

---

## New Patterns Not Yet Captured by Rubric

Three structural innovations from R5 are not represented by any existing criterion:

1. **Pre-scan scope closure gate** (V-01, V-05): The event tuple produced before the candidate scan defines a closed entity+message scope. Any candidate outside the tuple is structurally excluded before evaluation begins. This eliminates a class of false positives (domain-inferred candidates on the wrong entity or message) that C-01 through C-05 address only after the fact.

2. **Bilateral counterfactual pair as unified C-07/C-12 obligation** (V-02, V-05): Requiring a flip condition for *every* entry — regardless of firing status — collapses C-07 (conditional branch paths for firers) and C-12 (gap tokens for non-firers) into a single bilateral structural check. The invalidity constraint on trivial counterfactuals (V-05) adds a quality gate the rubric does not currently capture.

3. **Per-entry registration witness with unwitnessed health metric** (V-04): Requiring every entry to cite its named registration artifact converts C-05 from a global claim into a row-level structural assertion. The `UNWITNESSED count: U` metric quantifies the false-positive exposure — an output with U > 0 is grounding-weak even if C-05 passes globally.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-scan scope closure gate: event tuple produced before candidate scan defines closed entity+message scope, structurally excluding false-positive candidates before evaluation begins", "bilateral counterfactual pair per entry: every entry (firing and non-firing) carries a flip condition, collapsing C-07 and C-12 into a single unified obligation with invalidity constraint blocking trivial answers", "per-entry registration witness with unwitnessed health metric: every entry cites named registration artifact, converting C-05 from global claim to row-level structural check; UNWITNESSED count quantifies false-positive exposure"]}
```
