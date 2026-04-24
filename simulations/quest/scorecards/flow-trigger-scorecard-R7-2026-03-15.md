## flow-trigger — Round 7 Score Report (Rubric v4)

**Rubric**: v4 | N_essential=5, N_recommended=3, N_aspirational=11  
**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/11 × 10)`  
**Golden threshold**: all essential PASS AND composite ≥ 80

---

## V-01 — Role Sequence: Preamble Architect Authority Contract

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | PASS | Step 2b requires one entry per C-ID; gap entries enforce no silent omission |
| C-02 | Execution order stated | PASS | Entries ordered per Artifact 1b; `Positioned because: EOR-{NN}` mandatory per firing entry |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:`, `Produces:`, `Writes:` slots in all firing entry templates; no placeholder allowed |
| C-04 | Three anomaly verdicts | PASS | Role 3 mandate: produce EXACTLY three verdict blocks (Storm, Missing, Circular); PROHIBITION bars role from adding entries |
| C-05 | Platform grounding | PASS | Full VOCABULARY CONTRACT table with eight approved terms; `[NC: {term}]` violation marker specified |
| C-06 | Circular trigger analysis | PASS | "Build the directed edge set from Role 2's Cascades-to fields... Apply back-edge detection. Show the edge set. Name the cycle path or confirm no back-edges." Full graph trace. |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED):` + `Condition (SKIPPED would be):` both required in firing entry |
| C-08 | Anomaly remediation | PASS | `Remediation:` slot mandatory in verdict block; `if DETECTED: one named actionable fix` |
| C-09 | Execution tier and latency | PASS | `Execution tier:` + `Latency:` slots in every entry; three tier options enumerated |
| C-10 | Cascade completeness | PASS | Cascade entry format with `Spawned by: Entry #{parent}` — cascade children get numbered rows; `Cascades to: Entry #{N}` links root→child |
| C-11 | Candidate denominator | PASS | `DENOMINATOR: N = {count} candidates within scope of Artifact 1a.` before enumeration |
| C-12 | Gap tokens | PASS | `[NOT FIRED — {Candidate Name}] [C-ID: C-{NN}]` gap format with `Reason not fired:` |
| C-13 | Verdict evidence citation | PASS | `Rows inspected: Entry {#} through Entry {#}` mandatory in verdict block format |
| C-14 | Scope-closing event gate | PASS | Artifact 1a is explicit structured event tuple; Role 1 PROHIBITION bars candidates from appearing until `[ROLE 1: CERTIFIED]` issued |
| C-15 | Bilateral counterfactual | PASS | `Counterfactual [Flip to NOT FIRE]:` in firing entries; `Counterfactual [Flip to FIRE]:` in gap entries — both sides required inline |
| C-16 | Per-entry registration witness | PASS | `Registration witness:` slot in all entry types; `[UNWITNESSED]` token specified as fallback |
| C-17 | Per-entry EOR rule citation | PASS | Artifact 1b is named EOR table (7 rules pre-populated); `Positioned because: EOR-{NN}` required per firing entry; closure check: `Firing entries missing EOR citation: {count} [must be 0]` |
| C-18 | Cascade depth budget | PASS | CASCADE DEPTH BUDGET block in Artifact 1c; `[Depth: N/MAX]` on cascade entries; `[DEPTH EXCEEDED]` entry format; DE count in closure; storm verdict checks `DE > 0` |
| C-19 | Exclusion log + verdict citation | PASS | EXCLUSION LOG in Artifact 1c (9 layers); Role 3 mandate requires BOTH `Rows inspected:` AND `Exclusion log reference: EL-{NN}` per verdict — dual citation obligation stated as structural gap if either absent |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 11/11 = 10

**Composite: 100**

---

## V-02 — Output Format: Protocol Ledger

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | PASS | Phase 2 Step 2b: one entry per C-ID; gap entries in sequence |
| C-02 | Execution order stated | PASS | Entries ordered per Ledger L2; `Ledger ref: EOR-{NN}` in every firing entry — explicit per-entry EOR anchor |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:`, `Produces:`, `Writes:` slots in root and cascade firing entry templates |
| C-04 | Three anomaly verdicts | PASS | Phase 3: `Produce exactly three verdict blocks`; format template for Storm, Missing, Circular |
| C-05 | Platform grounding | PASS | Full VOCABULARY CONTRACT table; `[NC: {term used}]` inline violation marker |
| C-06 | Circular trigger analysis | PASS | "Build directed edge set from Phase 2 Cascades-to fields. Apply back-edge detection. Show edge set. Name cycle or confirm none." |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED):` + `Condition (SKIPPED would be):` in root and cascade firing templates |
| C-08 | Anomaly remediation | PASS | `Remediation:` slot in verdict format |
| C-09 | Execution tier and latency | PASS | `Execution tier:` + `Latency:` in all firing entry templates |
| C-10 | Cascade completeness | PASS | Cascade entry format with `Spawned by:` and linked `Cascades to:` rows; child entries numbered in sequence |
| C-11 | Candidate denominator | PASS | `DENOMINATOR: N = {count} candidates in scope.` in Phase 2 Step 2a |
| C-12 | Gap tokens | PASS | `[NOT FIRED — {Candidate Name}] [C-ID: C-{NN}]` with `Reason not fired:` |
| C-13 | Verdict evidence citation | PASS | `Rows inspected: Entry {#} through Entry {#}` in verdict format |
| C-14 | Scope-closing event gate | PASS | Ledger L1 event tuple with explicit scope rule; `[LEDGER SEALED — Phase 2 may begin]` gate token |
| C-15 | Bilateral counterfactual | PASS | `Counterfactual [Flip to NOT FIRE]:` in firing entries; `Counterfactual [Flip to FIRE]:` in gap entries |
| C-16 | Per-entry registration witness | PASS | `Registration witness:` in all entry types; `[UNWITNESSED]` fallback |
| C-17 | Per-entry EOR rule citation | PASS | Ledger L2 is named EOR table (7 rules); every firing entry carries `Ledger ref: EOR-{NN}` — explicit per-entry EOR citation; closure check: `Missing Ledger ref: {count} [must be 0]` |
| C-18 | Cascade depth budget | PASS | CASCADE DEPTH BUDGET in Ledger L3; `[Depth: N/MAX]` on cascade entries; `[DEPTH EXCEEDED]` format; DE count tracked; storm verdict checks DE > 0 |
| C-19 | Exclusion log + verdict citation | PASS | Exclusion log in Ledger L3 (8 layers + dispositions); Phase 3 verdict block requires `Exclusion log reference: EL-{NN}` (exact canonical field) citing Ledger L3; both citation types mandated per verdict |

**Note**: V-02 uses `Ledger ref: EOR-{NN}` instead of `Positioned because: EOR-{NN}` for C-17. The pass condition specifies "explicit EOR rule citation" — the Ledger ref satisfies this. The composite citation design means one slot satisfies both EOR position and preamble anchor. However, Phase 2 lacks the explicit PROHIBITION contracts present in V-01 — phase boundaries are enforced by gate tokens rather than named violations.

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 11/11 = 10

**Composite: 100**

---

## V-03 — Lifecycle Emphasis: Compact Preamble, Maximal Entry Template

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | PASS | Block C: one entry per C-ID; "all slots required" mandate eliminates silent omission |
| C-02 | Execution order stated | PASS | `Positioned because: EOR-{NN}` in root and cascade firing templates; closure check: `EOR citations missing: {count} [must be 0]` |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:`, `Produces:`, `Writes:` in all firing entries; "An empty named slot is a structural gap — it is not equivalent to 'not applicable.'" |
| C-04 | Three anomaly verdicts | PASS | Block D: three verdict blocks required; verdict format with five named slots — any missing slot is structural gap |
| C-05 | Platform grounding | PASS | VOCABULARY CONTRACT table present; `[NC: {term used}]` inline marker |
| C-06 | Circular trigger analysis | PASS | "Build directed edge set from Cascades-to fields... Apply back-edge detection. Show edge set." |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED):` + `Condition (SKIPPED would be):` in both root and cascade firing entries |
| C-08 | Anomaly remediation | PASS | `Remediation:` slot in verdict format; "named fix if DETECTED; 'none required' if NOT DETECTED" |
| C-09 | Execution tier and latency | PASS | `Execution tier:` + `Latency:` in all entry templates |
| C-10 | Cascade completeness | PASS | Cascade entry with `[Depth: N/MAX]` + `Spawned by:` + `Cascades to:` link |
| C-11 | Candidate denominator | PASS | `DENOMINATOR: N = {count}` in Block B |
| C-12 | Gap tokens | PASS | `[NOT FIRED — {Candidate Name}] [C-ID: C-{NN}]` gap format |
| C-13 | Verdict evidence citation | PASS | `Rows inspected: Entry {#} through Entry {#}` in verdict format; missing slot is structural gap |
| C-14 | Scope-closing event gate | PASS | A1 event tuple table with scope rule; `[BLOCK A: COMPLETE]` gate before Block B |
| C-15 | Bilateral counterfactual | PASS | `Counterfactual [Flip to NOT FIRE]:` in firing entries; `Counterfactual [Flip to FIRE]:` in gap entries; "all slots required" mandate enforces both sides |
| C-16 | Per-entry registration witness | PASS | `Registration witness:` in all entry types; `[UNWITNESSED]` fallback; "all slots required" |
| C-17 | Per-entry EOR rule citation | PASS | A2 EOR table (7 rules); `Positioned because: EOR-{NN}` in all firing entry templates; closure: `EOR citations missing: {count} [must be 0]` |
| C-18 | Cascade depth budget | PASS | A4: `MAX = {N}` declared with rationale; `[Depth: N/MAX]` on cascade entries; DEPTH EXCEEDED format; DE counted in closure check |
| C-19 | Exclusion log + verdict citation | PASS | A3 exclusion log (8 layers); Block D verdict format requires `Exclusion log reference:` citing A3 EL IDs; missing slot = structural gap enforcement |

**Note**: V-03's strongest feature is the "all slots required" mandate applied uniformly to every entry slot. This makes partial omission of C-15, C-16, C-17, C-18 obligations structurally impossible without producing a named gap. The compact preamble trades verbosity for density.

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 11/11 = 10

**Composite: 100**

---

## V-04 — Phrasing Register: Instructional Advisory

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | PASS | Step 3: "Write one entry for every C-ID" — enumeration mandate present |
| C-02 | Execution order stated | PASS | `Positioned because: EOR-{NN}` in entry template; "order them by the execution sequence from Step 1b" |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:`, `Produces:`, `Writes:` in firing entry template; "Fill in every line of the template" |
| C-04 | Three anomaly verdicts | PASS | Step 4: "Write one block for each investigation" — three blocks required (Storm, Missing Trigger, Circular) |
| C-05 | Platform grounding | PASS | Vocabulary table present; `[NC: {what you used}]` inline marker |
| C-06 | Circular trigger analysis | PASS | "list every edge in your cascade graph (Entry A -> Entry B for each Cascades-to entry). Check whether any edge points back to a node already in the chain. Show the edge list." |
| C-07 | Conditional branch paths | PASS | `Condition that fired (EXECUTED branch):` + `What would stop it (SKIPPED branch):` in firing entry template |
| C-08 | Anomaly remediation | PASS | `Fix (if needed): {one specific, named remediation step}` in verdict format |
| C-09 | Execution tier and latency | PASS | `Execution tier:` + `Latency:` in firing entries |
| C-10 | Cascade completeness | PASS | Cascade entry format with `[Depth: N/MAX]` + `Spawned by:` + `Triggers next:` link |
| C-11 | Candidate denominator | PASS | `Total candidates N = {count}` declared in Step 2 |
| C-12 | Gap tokens | PASS | `[NOT FIRED — {Candidate Name}] [C-ID: C-{NN}]` with reason |
| C-13 | Verdict evidence citation | PASS | `Entries I looked at: Entry {#} through Entry {#}` in verdict format — row range cited (advisory field name but content equivalent) |
| C-14 | Scope-closing event gate | PASS | Step 1a event tuple table with scope rule; "locks your scope" framing |
| C-15 | Bilateral counterfactual | PASS | `To make it NOT fire:` in firing entries; `To make it fire:` in gap entries — both directions required |
| C-16 | Per-entry registration witness | PASS | `Registered in:` in all entry types; `[UNWITNESSED]` fallback |
| C-17 | Per-entry EOR rule citation | PARTIAL | Step 1b EOR table present (7 rules); `Positioned because: EOR-{NN}` in entry template. Closure check uses "all should be cited" vs "must be 0" — softer enforcement signal leaves compliance at model discretion rather than structurally mandated. Template requirement is present; audit language is advisory only. |
| C-18 | Cascade depth budget | PASS | Step 1d: `CASCADE DEPTH BUDGET: MAX = {N}`; `[Depth: N/MAX]` on cascade entries; DEPTH EXCEEDED format; DE counted; storm check: `check whether DE > 0` |
| C-19 | Exclusion log + verdict citation | PARTIAL | Step 1c exclusion log (8 layers, named EXCLUSION LOG); verdict cites `From my exclusion log (Step 1c): EL-{NN}` — content equivalent to `Exclusion log reference:` but uses advisory field label; canonical field name absent; no structural gap mandate on missing field. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: (9 PASS + 2 × 0.5 PARTIAL)/11 × 10 = **9.09**

**Composite: 99.09 → 99**

---

## V-05 — Inertia Framing: Three Default Failures, Three Structural Overrides

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | PASS | Phase 2 Step 2b: one entry per C-ID; phase prohibition bars verdicts from Phase 2 |
| C-02 | Execution order stated | PASS | EOR Table present (OVERRIDE-1 section); `Positioned because: EOR-{NN}` in firing entries; closure: `OVERRIDE-1 gaps: {count} [must be 0]` |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:`, `Produces:`, `Writes:` slots in all firing entry templates |
| C-04 | Three anomaly verdicts | PASS | Phase 3: three verdict blocks; each carries Exclusion log reference with OVERRIDE-3 active label |
| C-05 | Platform grounding | PASS | VOCABULARY CONTRACT table; `[NC: {term used}]` inline marker |
| C-06 | Circular trigger analysis | PASS | "Build directed edge set from Cascades-to fields... Apply back-edge detection. Show edge set. Name cycle or confirm none." |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED):` + `Condition (SKIPPED would be):` in all firing entries |
| C-08 | Anomaly remediation | PASS | `Remediation:` slot in verdict format; "if DETECTED: one named actionable fix" |
| C-09 | Execution tier and latency | PASS | `Execution tier:` + `Latency:` in entry templates |
| C-10 | Cascade completeness | PASS | Cascade entry with `Spawned by:` + `Cascades to:` child link; DEPTH EXCEEDED entry names DEFAULT-2 would have continued silently |
| C-11 | Candidate denominator | PASS | `DENOMINATOR: N = {count} candidates in scope.` in Phase 2 Step 2a |
| C-12 | Gap tokens | PASS | `[NOT FIRED — {Candidate Name}] [C-ID: C-{NN}]` in gap format |
| C-13 | Verdict evidence citation | PASS | `Rows inspected: Entry {#} through Entry {#}` in verdict format |
| C-14 | Scope-closing event gate | PASS | Event Tuple with `[SCOPE GATE: CLOSED]` token; Phase 1 prohibition bars candidates |
| C-15 | Bilateral counterfactual | PASS | `Counterfactual [Flip to NOT FIRE]:` in firing entries; `Counterfactual [Flip to FIRE]:` in gap entries |
| C-16 | Per-entry registration witness | PASS | `Registration witness:` in all entry types; `[UNWITNESSED]` fallback |
| C-17 | Per-entry EOR rule citation | PASS | EOR Table with OVERRIDE-1 label (7 rules); `Positioned because: EOR-{NN} — {rule — OVERRIDE-1 active when populated}` per firing entry; closure: `OVERRIDE-1 active: {count} / {FR + FC}` AND `OVERRIDE-1 gaps: {count} [must be 0]` — dual compliance count |
| C-18 | Cascade depth budget | PASS | CASCADE DEPTH BUDGET with OVERRIDE-2 label; cascade entries carry `[Depth: N/MAX — OVERRIDE-2 active]`; DEPTH EXCEEDED entry states "DEFAULT-2 would have continued silently; OVERRIDE-2 terminates it here"; closure: `OVERRIDE-2 active: cascade entries with [Depth: N/MAX] = {count} / FC [must equal FC]` |
| C-19 | Exclusion log + verdict citation | PASS | EXCLUSION LOG with OVERRIDE-3 label (8 layers); verdict format: `Exclusion log reference: EL-{NN} — {layer} ({disposition}) — OVERRIDE-3 active`; Phase 3 preamble: "A verdict block without this citation is running DEFAULT-3" — named failure consequence for omission |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 11/11 = 10

**Composite: 100**

---

## Composite Score Summary

| Rank | Variation | Essential | Recommended | Aspirational | Composite |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 (tie) | V-01 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** |
| 1 (tie) | V-02 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** |
| 1 (tie) | V-03 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** |
| 1 (tie) | V-05 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** |
| 5 | V-04 | 5/5 (60) | 3/3 (30) | 10/11 (9.09) | **99** |

**All essential criteria pass across all five variations.**

---

## Qualitative Ranking (tiebreak within 100-scorers)

**V-05 > V-01 > V-02 > V-03 > V-04**

Rationale for V-05 at top:

1. **Self-certifying compliance per entry** — `[Depth: N/MAX — OVERRIDE-2 active]` and `— OVERRIDE-3 active` in verdict blocks make override compliance visible at the row level without requiring a reviewer to read the preamble. V-01 requires reading Artifact 1c to confirm the citation; V-05 confirms it inline.

2. **Motivationally grounded structural obligations** — the three-row DEFAULT table names the OBSERVABLE SYMPTOM of non-compliance (not just the rule). A model under pressure knows WHY each override matters, not just WHAT it must produce. This addresses the root cause of drift rather than patching it with prohibition language.

3. **Dual OVERRIDE compliance counts in closure** — `OVERRIDE-1 active: {count} / {FR+FC}` AND `OVERRIDE-1 gaps: {count} [must be 0]` are both tracked, giving an affirmative count (how many overrides are active) AND a gap count (how many are missing). V-01 only counts gaps.

V-01 ranks second: the CERTIFIED role-gate and explicit PROHIBITIONS make boundary violations named rather than silently absorbed — strongest structural gating model.

---

## Excellence Signals (top variation: V-05)

1. **Inline self-certification of override status** — labeling override state directly in entry fields (`— OVERRIDE-2 active`, `— OVERRIDE-3 active`) converts per-row compliance from implicit obligation to explicit, scannable status. A reviewer can confirm all three new criteria are met by reading entries alone, without cross-referencing the preamble.

2. **Named default failure as compliance motivation** — the `THREE DEFAULT FAILURE MODES` table with observable symptoms provides causal grounding for each structural mechanism. When a model encounters pressure to skip an artifact, it has a named failure consequence (not just a prohibition) to reason against. This is structurally distinct from a PROHIBITION, which names a violation after the fact; the DEFAULT table names the consequence before any omission occurs.

3. **Joint multi-artifact gate token** (shared V-01/V-05) — `[ROLE 1: CERTIFIED — artifacts 1a, 1b, 1c all present]` and `[PHASE 1: ALL THREE OVERRIDES ACTIVE — Phase 2 may begin]` are unified go/no-go signals that confirm the complete set of required preamble artifacts together. This is more structurally robust than three sequential `[ARTIFACT N: COMPLETE]` tokens, which can each pass while a different artifact is incomplete.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inline override self-certification per entry — labeling override status directly in entry fields (e.g., [Depth: N/MAX — OVERRIDE-2 active]) makes per-row compliance visible without requiring preamble cross-reference; converts implicit obligation to explicit scannable state", "Named default failure table with observable symptom before the protocol — stating the failure mode and its observable consequence before providing the structural override gives the model causal grounding to resist omission under pressure, not just a prohibition to enforce after the fact", "Joint multi-artifact preamble gate token — a single unified certification token (e.g., [PHASE 1: ALL THREE OVERRIDES ACTIVE]) confirming the complete set of required pre-enumeration artifacts before enumeration begins is more structurally robust than sequential per-artifact completion tokens, which can each pass while another artifact is absent"]}
```
