## Scorecard — flow-trigger Round 3, Rubric v2

### Evaluation Framework

Scoring prompt designs as structural guarantees: does each variation's architecture make each criterion pass-by-construction?

Essential: 5 criteria (60 pts) | Recommended: 3 criteria (30 pts) | Aspirational: 5 criteria (10 pts)

---

### V-01 — Role Sequence: Scanner Gate → Executor → Verdict Writer

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Trigger enumeration | **PASS** | Role B: "Every manifest entry from Role A must appear — as a firing entry OR inline gap token. A manifest ID with no entry is a structural omission." Zero-omission enforcement is in the role contract. |
| C-02 | Execution order stated | **PASS** | B-1: "sync entries first (by priority within sync tier), then async entries (by platform scheduling, noting non-deterministic ordering)." |
| C-03 | Inputs/outputs per trigger | **PASS** | B-1 template has explicit `Reads: {Entity}.{Field}`, `Produces: {connector}—{action}—{target}—{state}`, `Writes:` with note "no generic descriptions." |
| C-04 | Three anomaly verdicts | **PASS** | Role C: C-1 Storm, C-2 Missing Trigger, C-3 Circular Dependency — all three required sections. |
| C-05 | Platform grounding | **PASS** | B-0 Platform Term Contract with approved term set; violations → `[NC: {term}]`. |
| C-06 | Circular trigger analysis | **PASS** | C-3 builds directed edge set; asks whether any path "returns to a trigger already on the path from the root change event." |
| C-07 | Conditional branch paths | **PASS** | B-1 firing entry template: `[filter = value] EXECUTED — {reason}` / `[filter ≠ value] SKIPPED — {non-fire condition}`. Both branches in the format string. |
| C-08 | Anomaly remediation | **PASS** | Verdict format: `Remediation: {if DETECTED: one named, actionable fix} / {if CLEARED: none required}`. |
| C-09 | Execution tier + latency | **PASS** | B-1: `Latency: Inline (sync, blocks transaction) [OR: ~N min [{standard \| premium} connector tier] (async)]`. |
| C-10 | Cascade completeness | **PASS** | "If Writes: is non-empty and the written field matches any M-ID candidate's trigger condition, insert a cascade child row immediately below the parent." Traces to termination. |
| C-11 | Denominator declared before | **PASS** | Scanner role's ONLY job is the manifest and count — role boundary enforces completion before Role B (enumeration) begins. Structurally impossible to enumerate before declaring. |
| C-12 | Gap tokens inline | **PASS** | B-1 gap token placed "at the manifest entry's position in sequence." B-2 reconciliation table with totals equation must balance. |
| C-13 | Verdict evidence citation | **PASS** | Role C precondition: "Each verdict MUST cite specific Role B sequence numbers as evidence. A verdict block without row numbers is structurally incomplete." Format string has mandatory `Rows inspected:` field. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10 | **Composite: 100**

---

### V-02 — Output Format: Two-Pass Numbered Ledger

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Trigger enumeration | **PASS** | "Every allocated row must receive content in Pass 2 — either a full trigger entry or an explicit gap token. There is no 'row 3 is just blank' state." |
| C-02 | Execution order stated | **PASS** | "Walk the ledger in execution order: sync rows first (by priority), then async rows. Within async, state non-deterministic ordering explicitly." |
| C-03 | Inputs/outputs per trigger | **PASS** | Full trigger entry template: `Reads: {Entity}.{Field}, ... [no generic descriptions]`, `Produces: {connector}—{action}—{target}—{state}`, `Writes:`. |
| C-04 | Three anomaly verdicts | **PASS** | Anomaly Verdicts section requires Storm, Missing Trigger, Circular Dependency verdict blocks. |
| C-05 | Platform grounding | **PASS** | Platform Term Contract with `[NC: {term}]` violation marking. |
| C-06 | Circular analysis | **PASS** | Circular Dependency verdict: directed edge set from all Writes fields; cycle check for path back to traversed row. |
| C-07 | Conditional branches | **PASS** | Firing entry: `Condition: {executed branch — reason} / {skipped branch — reason}`. |
| C-08 | Anomaly remediation | **PASS** | Verdict block: `Remediation: {named fix if DETECTED; "none required" if CLEARED}`. |
| C-09 | Execution tier + latency | **PASS** | `Latency: Inline (sync, blocks transaction) [OR: ~N min [{standard \| premium}] (async)]`. |
| C-10 | Cascade completeness | **PASS** | "If Writes: is non-empty and the written field matches any Pass 1 row's trigger condition: add a cascade row numbered L-NN.1." |
| C-11 | Denominator declared before | **PASS** | Pass 1 row allocation IS the denominator. `Denominator: N rows allocated.` appears before any condition evaluation or firing status determination. Note in Pass 1 footer: "A Pass 1 row with no Pass 2 content is a structural gap." |
| C-12 | Gap tokens inline | **PASS** | "For each allocated row, produce exactly one of: Full trigger entry OR Gap token." Every row must have content; there is no path to skip a row. |
| C-13 | Verdict evidence citation | **PASS** | Verdict format: `Rows examined: L-{NN} through L-{MM}` — mandatory field; "Row citations are required — a verdict block cannot close without citing the rows." |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10 | **Composite: 100**

---

### V-03 — Phrasing Register: Failure Mode Catalog (FM-01–FM-13)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Trigger enumeration | **PASS** | FM-01 names the defect. Section 1: "SHALL: every Section 0 row SHALL have a corresponding Section 1 entry." |
| C-02 | Execution order stated | **PASS** | FM-02 names unordered sequence as a defect. Section 1: "Walk candidates in execution order (sync before async)." |
| C-03 | Inputs/outputs per trigger | **PASS** | FM-03 "Payload vacancy" names the defect. Firing entry template has `Reads:`, `Produces:` with inline `[FM-03 check]` markers. |
| C-04 | Three anomaly verdicts | **PASS** | FM-04 "Verdict absence." Section 3: "SHALL: all three verdict blocks SHALL appear. Absence of any block is FM-04." |
| C-05 | Platform grounding | **PASS** | FM-05 "Vocabulary violation." Term contract with `[NC:]` enforcement. |
| C-06 | Circular analysis | **PASS** | FM-06 "Circular analysis absent." Section 3 includes Circular Dependency verdict block. |
| C-07 | Conditional branches | **PASS** | FM-07 "Branch coverage gap." Firing entry has EXECUTED/SKIPPED branches with inline `[FM-07 check]` marker. |
| C-08 | Anomaly remediation | **PASS** | FM-08 "Remediation gap." Verdict format: `Remediation:` with `[FM-08 check]`. |
| C-09 | Execution tier + latency | **PASS** | FM-09 "Latency unanchored." Firing entry: `Latency:` with `[FM-09 check]`. |
| C-10 | Cascade completeness | **PASS** | FM-10 "Cascade truncation." FM-10 check inline in firing entry; cascade child row insertion specified. |
| C-11 | Denominator declared before | **PASS** | FM-11 "Denominator withheld." Section 0: `Candidate count: N. ← SHALL appear here, before any Section 1 content.` Violation condition stated explicitly. |
| C-12 | Gap tokens inline | **PASS** | FM-12 "Gap token absent." Section 1 gap token with `[FM-12 check — token present]` marker. Section 2 reconciliation detects totals mismatch. |
| C-13 | Verdict evidence citation | **PASS** | FM-13 "Verdict uncited." Section 3 verdict format: `Rows cited:` with `[FM-13 check — mandatory]`. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10 | **Composite: 100**

---

### V-04 — Lifecycle Emphasis + Output Format: Phase Gate Model

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Trigger enumeration | **PASS** | Phase 1: "Every R-ID from Phase 0 must appear — as a firing entry or inline gap token." Gate 1 fails if any R-ID is unaccounted: `[GATE 1: FAILED — R-IDs without entries: {list}]`. |
| C-02 | Execution order stated | **PASS** | 1-B: "Walk candidates in execution order: sync entries by priority first, then async entries." |
| C-03 | Inputs/outputs per trigger | **PASS** | Firing entry template: `Reads: {Entity}.{Field} [specific fields — no generic descriptions]`, `Produces: {connector}—{action verb}—{target}—{state}`. |
| C-04 | Three anomaly verdicts | **PASS** | Phase 2: 2-A Storm, 2-B Missing Trigger, 2-C Circular Dependency — all three blocks required. |
| C-05 | Platform grounding | **PASS** | Phase 0-B Platform Term Contract; `[NC: {term}]` for violations. |
| C-06 | Circular analysis | **PASS** | 2-C: directed edge set from Writes fields; cycle check "does any path return to a node already traversed from the root?" |
| C-07 | Conditional branches | **PASS** | Firing entry: `[filter] EXECUTED — {reason}` / `[filter] SKIPPED — {condition for non-fire}`. |
| C-08 | Anomaly remediation | **PASS** | Verdict format: `Remediation: {one named, actionable fix}`. |
| C-09 | Execution tier + latency | **PASS** | `Latency: Inline (sync, blocks transaction) [OR: ~N min [{standard\|premium} tier] (async)]`. |
| C-10 | Cascade completeness | **PASS** | "If Writes: is non-empty and the written field matches any R-ID's trigger condition: insert a cascade child row immediately below the parent." |
| C-11 | Denominator declared before | **PASS** | Gate 0 condition: "Is there a declared candidate count after the registry table?" `[GATE 0: PASSED — N candidates declared, denominator set]` / `[GATE 0: FAILED — add candidate count before proceeding]`. Gate marker is structurally visible in output. |
| C-12 | Gap tokens inline | **PASS** | Gap token placed "at the registry entry's sequence position." Gate 1: "Does every Phase 0 R-ID appear in the sequence (fired or gap)?" — visible fail marker if any R-ID missing. |
| C-13 | Verdict evidence citation | **PASS** | Gate 2 condition: "Do all three verdict blocks contain at least one Phase 1 row citation?" `[GATE 2: PASSED/FAILED]`. Verdict format: `Phase 1 rows inspected: Seq {N}–{M}` — mandatory field. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10 | **Composite: 100**

---

### V-05 — Inertia Framing + Role Sequence: Override Model

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Trigger enumeration | **PASS** | Override 2 requires ALL manifest entries as firing rows or gap tokens. Section 4 confirms this. |
| C-02 | Execution order stated | **PASS** | Section 4: "All manifest entries as firing rows or inline gap tokens, in execution order (sync before async)." |
| C-03 | Inputs/outputs per trigger | **PARTIAL** | Overrides 3/4/6 drive rich behavior (condition branches, cascades, latency). But the firing row format is never explicitly templated with `Reads:` / `Produces:` fields — only the gap token format is fully specified in Override 2. An output following V-05 could satisfy the override behaviors while omitting structured payload fields. Weaker structural guarantee than V-01 through V-04. |
| C-04 | Three anomaly verdicts | **PASS** | Section 6: "Three verdict blocks (Storm, Missing Trigger, Circular Dependency)." |
| C-05 | Platform grounding | **PASS** | Section 2 Platform Term Contract with `[NC: {term}]` for violations. |
| C-06 | Circular analysis | **PASS** | Override 4: cycle edge annotation. Section 6 includes Circular Dependency verdict. |
| C-07 | Conditional branches | **PASS** | Override 3 explicitly requires both branches with `EXECUTED / SKIPPED` format. |
| C-08 | Anomaly remediation | **PASS** | Override 5 verdict format: `Remediation: {named fix if DETECTED; "none required" if CLEARED}`. |
| C-09 | Execution tier + latency | **PASS** | Override 6 is the most explicit: requires estimated delay range AND throttle/concurrency implications. Strongest C-09 enforcement of any variation. |
| C-10 | Cascade completeness | **PASS** | Override 4 names the default failure ("noted in side effects column") and explicitly requires cascade rows as numbered sequence entries. |
| C-11 | Denominator declared before | **PASS** | Override 1 names the default failure and the override. Section 3: `Candidate count: N. ← must appear here before Section 4 begins`. |
| C-12 | Gap tokens inline | **PASS** | Override 2 names the default failure ("reconciliation table at the end") and the override (inline gap token at execution-order position). |
| C-13 | Verdict evidence citation | **PASS** | Override 5 names the default failure ("assertoric verdicts") and the override with `Rows examined:` in the format string. |

**Essential**: 4.5/5 (C-03 partial) → 54 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10 | **Composite: 94**

Note: C-03 partial means all_essential_pass = **false** for V-05.

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | All Essential Pass |
|-----------|-----------|-------------|--------------|-----------|-------------------|
| V-01 | 5/5 → 60 | 3/3 → 30 | 5/5 → 10 | **100** | YES |
| V-02 | 5/5 → 60 | 3/3 → 30 | 5/5 → 10 | **100** | YES |
| V-03 | 5/5 → 60 | 3/3 → 30 | 5/5 → 10 | **100** | YES |
| V-04 | 5/5 → 60 | 3/3 → 30 | 5/5 → 10 | **100** | YES |
| V-05 | 4.5/5 → 54 | 3/3 → 30 | 5/5 → 10 | **94** | NO |

---

## Excellence Signals

**Four-way tie at 100** — the distinguishing signals are in HOW each top variation guarantees compliance:

| Signal | Source | What It Adds Over Prior Round |
|--------|--------|-------------------------------|
| **Self-auditing gate markers in output** | V-04 | `[GATE N: PASSED/FAILED — {what missing}]` tokens appear IN the output, making structural compliance directly readable without scorer intervention. Prior rounds required external rubric review to detect C-11/C-12/C-13 violations; V-04 makes violations self-reporting. |
| **Role isolation as structural barrier** | V-01 | Scanner role's explicit prohibition on condition evaluation or firing entries means C-11 is structurally impossible to violate — not merely instructed. Prior rounds relied on instruction compliance; V-01 relies on role contract. |
| **FM catalog with detection signals** | V-03 | Each failure mode has a named detection signal — an observable output property that reveals the failure. Makes self-checking mechanical: an output producer can verify FM compliance without fully re-reading the rubric. |
| **Inertia naming** | V-05 | Naming the DEFAULT behavior that produces each defect (not just the requirement) is architecturally superior for durable compliance — but V-05 didn't fully implement the firing entry template, proving that inertia framing alone is insufficient without format enforcement. |

**C-03 gap in V-05** confirms a cross-round finding: **override framing without a complete format template is insufficient**. V-01 through V-04 all provide explicit `Reads:` / `Produces:` / `Writes:` fields in their firing entry templates; V-05 relies on practitioners inferring the payload requirements from override descriptions alone.

**New pattern not yet captured as a criterion**: Gate markers embedded in output — the practice of inserting `[GATE N: PASSED]` / `[GATE N: FAILED — {what missing}]` tokens at structural checkpoints so that a reviewer can assess compliance by scanning the output for gate tokens, without needing to apply the rubric against every detail.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Self-auditing gate markers: [GATE N: PASSED/FAILED] tokens embedded at structural checkpoints in the output make compliance directly readable without scorer intervention — a reviewer can scan for gate tokens rather than re-applying the full rubric"]}
```
