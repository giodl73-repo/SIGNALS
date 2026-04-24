---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 14
rubric_version: 14
---

# flow-ratelimit — Variate R14

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence — R12 V-05 baseline carry, no NMI, implicit declarations), V-02 (lifecycle emphasis — NMI declared inside Role 10 body as first element), V-03 (output format — standalone NMI section before Role 10, no name reference in check (a)).
Combination variations: V-04 (role sequence + output format — standalone NMI + explicit three declarations + name reference), V-05 (full integration — V-04 + explicit "deferred from Role N — [reason]" annotation).

**R14 target criteria: C-34, C-35**

---

## State Analysis: What R12 V-05 Has vs. What R14 Must Add

**R12 V-05 coverage under v14 (assessed):**

C-34 requires the reconciler's check (a) to produce three explicit behavioral declarations from within the reconciler body:
- Declaration (i): mode = VERIFICATION-ONLY
- Declaration (ii): this role does not insert REVISED markers
- Declaration (iii): REVISED marker insertion count for this role = zero

R12 V-05 check (a): "This check is pure verification — Role 9 has already inserted all missing markers (with 'deferred from Role N — [reason]' annotation)."
- Declaration (i): covered by "pure verification" (implicit)
- Declaration (ii): implied by "Role 9 has already inserted" (implicit — reconciler non-insertion is inferred, not stated)
- Declaration (iii): zero count — NOT STATED

**R12 V-05 C-34 verdict:** BORDERLINE FAIL — zero-count declaration absent. The criterion requires three declarations "produced during the reconciler's own execution"; a count declaration that must be inferred is not produced.

C-35 requires a named formal invariant declared before the terminal reconciler section opens (not inside it), with four components: (a) names itself, (b) states the reconciler does not insert REVISED markers, (c) states insertion count is zero, (d) names the violation condition by invariant name. The reconciler's check (a) must reference the invariant by its declared name.

**R12 V-05 C-35 verdict:** FAIL — no invariant declared before Role 10 opens; check (a) asserts verification-only from within the reconciler body without referencing any pre-declared constraint.

**Summary:**

| Criterion | R12 V-05 under v14 | Gap |
|-----------|-------------------|-----|
| C-34 | BORDERLINE FAIL | Declaration (iii) — zero count — not explicitly produced |
| C-35 | FAIL | No pre-declared NMI; check (a) does not reference an invariant by name |

**R12 V-05 under v14 composite:** (26/27 × 30) + 60 + 30 = 28.89 + 90 = 118.89/120

---

## Round 14 Variation Map

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role count | 11 | 11 | 12 | 12 | 12 |
| NMI position | none | inside Role 10 body | standalone pre-terminal section | standalone pre-terminal section | standalone pre-terminal section |
| Explicit 3 declarations in check (a) | implicit | yes | implicit | yes | yes |
| Check (a) references NMI by name | n/a | yes | no | yes | yes |
| Gate 9→10 names NMI-01 as deliverable | no | no | no | no | yes |
| C-34 | BORDERLINE FAIL | PASS | BORDERLINE FAIL | PASS | PASS |
| C-35 | FAIL | FAIL (inside body) | FAIL (no name reference) | PASS | PASS |
| Predicted composite | 118.89/120 | 118.89/120 | 118.89/120 | 120/120 | 120/120 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Do explicit three behavioral declarations in check (a) satisfy C-34 independently of NMI position? Hypothesis: yes — C-34 requires the three declarations to appear "from within the reconciler pass"; placing them as named bullet points in check (a) satisfies the criterion regardless of whether a pre-declared NMI exists.

Q2 (V-02 vs V-04): Does NMI position (inside vs. before the reconciler section) determine C-35 compliance independently of three-declaration quality? Hypothesis: yes — C-35 explicitly excludes invariants "declared inside the reconciler body"; V-02's NMI-01 block at the top of Role 10 is structurally inside Role 10, so C-35 fails regardless of how well check (a) is written.

Q3 (V-03 vs V-04): Does the absence of the NMI name reference in check (a) alone cause C-35 failure when the NMI is correctly positioned? Hypothesis: yes — "The reconciler's check (a) must reference the invariant by its declared name" is a stated pass condition; V-03 has the NMI in the right place but check (a) never says "NMI-01", so C-35 fails on the reference requirement alone.

---

## V-01 — Single Axis: Role Sequence (R12 V-05 baseline carry — C-34 borderline, C-35 FAIL)

**Axis:** Role sequence — identical to R12 V-05. 11-role sequence with dedicated VERDICT CURRENCY CHECK (Role 9) and 4-check terminal reconciler (Role 10). No NMI declared before Role 10 opens. Check (a) states "pure verification" implicitly covering declaration (i); non-insertion implied; zero count not stated. Three behavioral declarations are implicit, not explicit.

**Hypothesis:** C-34 BORDERLINE FAIL — the zero-count declaration is absent from the reconciler body; the criterion requires three declarations produced by the reconciler's own execution, and an inferred count is not produced. C-35 FAIL — no named invariant exists before Role 10; check (a) does not reference any pre-declared constraint. C-01 through C-33 all PASS (R12 V-05 baseline). Composite: 118.89/120.

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below. Each role produces named deliverables gated into the next role. Do not skip roles or merge roles.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins. These claims will be revised inline if evidence contradicts them.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell in any Schema A table will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete (BASELINE | PROTECTED | DERIVATION CHAIN columns present).
Claim (d): UX tier count will match the burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Define the schemas that govern all subsequent output.

Schema A (three-column table for all quantitative analysis):
| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|

- BASELINE: observed or specified value before mitigation
- PROTECTED: target value after mitigation applied
- DERIVATION CHAIN: show every arithmetic step; conclusions without computation steps are a Schema A CONTENT violation

Schema B (UX tier block — four named fields, all required):
```
ERROR SIGNAL: [value]
USER-VISIBLE BEHAVIOR: [value]
VISIBILITY LEVEL: [value]
RECOVERY PATH: [value]
```

Rejection clauses:
- Schema A STRUCTURAL: table missing one or more column headers
- Schema A CONTENT: DERIVATION CHAIN cell contains conclusion without computation steps
- Schema B STRUCTURAL: tier block missing one or more of the four field labels
- Schema B CONTENT: a field contains a non-answer (blank, "N/A", "varies")

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints for the integration under analysis. For each endpoint state:
- Numeric threshold (requests per window)
- Window duration
- Scope (per-user / per-tenant / global)
- Type (connector-enforced vs platform-enforced)
- Retry-After header availability (YES / NO / PARTIAL)

If any endpoint lacks a Retry-After header or equivalent backoff signal, insert REVISED marker at Claim (a) with forward reference to this role.

Gate 2→3: All endpoints enumerated with numeric thresholds and scope. Verdict currency check complete for Claim (a).

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths in the integration. For each burst path:
- Classify as STRUCTURAL (unavoidable given the architecture) or INCIDENTAL (artifact of current implementation, removable)
- State the endpoint(s) involved

Record total burst path count as B. This count is the authoritative source for gate item (e) in Role 8. Do not derive tier count from Verdict Claim (d) — use this role's output directly.

Gate 3→4: Burst path count B recorded. Each path classified STRUCTURAL or INCIDENTAL.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Construct a Schema A table for the cascading failure scenario. Show:
- BASELINE: request volume at failure onset
- PROTECTED: volume threshold with circuit-breaker or backoff applied
- DERIVATION CHAIN: show the causal chain step-by-step — which endpoint hits limit first, which downstream calls are blocked, compounding effect on retry volume (arithmetic required)

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain with arithmetic.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

For each endpoint from Role 2, determine: does the response include a usable Retry-After value (or equivalent)?

Verdict per endpoint: YES / NO / PARTIAL
- YES: header present with numeric or date value, client can honor it automatically
- NO: header absent; failure mode: client must guess backoff interval, risks amplifying burst
- PARTIAL: header present but value is unreliable (e.g., always returns 0)

If any endpoint is NO or PARTIAL, insert REVISED marker at Claim (a) with forward reference to this role if not already inserted from Role 2.

Gate 5→6: All endpoints assessed. Any NO/PARTIAL endpoints have failure modes documented.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a Schema A table with at least three volume tiers. Include a 5x load spike row. Every DERIVATION CHAIN cell must show computation steps (e.g., "200 req/min × 5 = 1000 req/min; limit = 500 req/min; overflow = 500 req/min; queue depth at T+30s = 500 × 0.5 = 250 queued"). A bare conclusion without arithmetic is a Schema A CONTENT violation.

Gate 6→7: Schema A table with >= 3 tiers including 5x spike row. All DERIVATION CHAIN cells contain arithmetic steps.

---

## ROLE 7 — MITIGATIONS

For each bottleneck identified in Roles 3–6, prescribe a mitigation. Present each with:
- BEFORE state (current behavior without mitigation)
- AFTER state (behavior after mitigation applied)
- Which burst path(s) from Role 3 the mitigation addresses

Gate 7→8: Each bottleneck has a mitigation. BEFORE/AFTER states present for each.

---

## ROLE 8 — UX PER THROTTLE TIER

For each burst path tier from Role 3 (use Role 3's count B directly — do not use Verdict Claim (d)), produce a Schema B UX block.

Each block must pass the six-item gate:
(a) ERROR SIGNAL field present and specific
(b) USER-VISIBLE BEHAVIOR field present and specific
(c) VISIBILITY LEVEL present (Silent / Banner / Modal / Blocking)
(d) RECOVERY PATH present and actionable
(e) Tier count in this role equals burst path count B from Role 3 (verify directly — not from Verdict Claim (d))
(f) Each block has all four Schema B field labels (Schema B STRUCTURAL compliance)

If tier count does not match B, insert REVISED marker at Claim (d) with forward reference to this role.

Gate 8→9: All B tiers present. Six-item gate checked for each tier.

---

## ROLE 9 — VERDICT CURRENCY CHECK

This role is a dedicated pre-reconciler sweep. Its sole function is to ensure all Verdict Block revisions are marked before the Terminal Reconciler runs.

Step 1 — Sweep Roles 1–8 for every instance where a Verdict Claim was revised during analysis.
Step 2 — For each revision, confirm that an inline REVISED marker was inserted at the originating gate boundary (by the role that discovered the revision).
Step 3 — For each gap (revision occurred but no marker was inserted at the gate boundary): insert the REVISED marker in the Verdict Block now, annotated as "deferred from Role N" to distinguish it from markers inserted at gate boundaries (which carry no "deferred" annotation).
Step 4 — Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[If N > 0, itemize each: "Claim (X) — deferred from Role N — [reason]"]

Gate 9→10: Currency sweep complete. Named output produced. All deferred markers annotated with origin role.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Currency sweep complete (Role 9 CURRENCY SWEEP FINDINGS output present).
Gate out: This is the final section. Reconciler findings published before document close.

This check is pure verification — Role 9 has already inserted all missing markers.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Scan Verdict Block claims (a)–(d). For each claim, confirm:
- An inline REVISED marker is present for every claim revised during analysis
- Each marker includes a forward reference to the revising role
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate each gated transition (Gate 0→1 through Gate 8→9). For each gate confirm named prior-section deliverables are present in the document.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 4 and 6). Flag any cell containing only a conclusion without computation steps as a Schema A CONTENT violation.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8. Flag any tier block missing one or more of the four field labels as a Schema B STRUCTURAL violation.
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]

---

---

## V-02 — Single Axis: Lifecycle Emphasis (NMI inside Role 10 body — C-34 PASS, C-35 FAIL)

**Axis:** Lifecycle emphasis — NMI-01 is declared as the first named element inside Role 10's body, before check (a). The NMI block has all four required components: it names itself (NMI-01), states the reconciler does not insert REVISED markers, states insertion count is zero, and names the violation condition by invariant name. Check (a) references "NMI-01" by name and produces three explicit behavioral declarations. However, the NMI is declared inside the reconciler section, not before it opens.

**Hypothesis:** C-34 PASS — check (a) produces three explicit behavioral declarations (mode, non-modification, zero count) from within the reconciler body. C-35 FAIL — "An invariant declared inside the reconciler body... does not pass." Despite full four-component content and name reference in check (a), the structural position is wrong: NMI-01 appears after the "## ROLE 10 — TERMINAL RECONCILER" header, placing it inside the reconciler. The compliance delta from V-04 is exactly one structural change: moving the NMI block from inside Role 10 to a standalone section before the Role 10 header.

**v14 predicted scoring:** C-34 PASS. C-35 FAIL (inside body). Composite: 118.89/120.

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below. Each role produces named deliverables gated into the next role. Do not skip roles or merge roles.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell in any Schema A table will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete (BASELINE | PROTECTED | DERIVATION CHAIN columns present).
Claim (d): UX tier count will match the burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Schema A (three-column table):
| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|

Schema B (UX tier block — four named fields, all required):
```
ERROR SIGNAL: [value]
USER-VISIBLE BEHAVIOR: [value]
VISIBILITY LEVEL: [value]
RECOVERY PATH: [value]
```

Rejection clauses:
- Schema A STRUCTURAL: table missing one or more column headers
- Schema A CONTENT: DERIVATION CHAIN cell contains conclusion without computation steps
- Schema B STRUCTURAL: tier block missing one or more of the four field labels
- Schema B CONTENT: a field contains a non-answer (blank, "N/A", "varies")

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints. For each: numeric threshold, window duration, scope, type, Retry-After availability. Insert REVISED at Claim (a) if any endpoint lacks a backoff signal.

Gate 2→3: All endpoints enumerated with numeric thresholds and scope. Claim (a) currency check complete.

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Classify each STRUCTURAL or INCIDENTAL. Record total count B — authoritative source for gate item (e) in Role 8.

Gate 3→4: Burst path count B recorded. Each path classified.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Schema A table. DERIVATION CHAIN shows: which endpoint triggers first, which downstream calls are blocked, compounding retry volume arithmetic step-by-step.

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain with arithmetic.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

YES / NO / PARTIAL per endpoint. Failure mode for non-YES. Insert REVISED at Claim (a) if not already inserted.

Gate 5→6: All endpoints assessed. Failure modes documented for non-YES.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with >= 3 volume tiers including 5x spike row. Every DERIVATION CHAIN cell shows arithmetic steps.

Gate 6→7: Schema A table with >= 3 tiers. All DERIVATION CHAIN cells contain computation steps.

---

## ROLE 7 — MITIGATIONS

BEFORE/AFTER states per bottleneck. Reference which burst path(s) from Role 3 each mitigation addresses.

Gate 7→8: Each bottleneck has a mitigation. BEFORE/AFTER states present.

---

## ROLE 8 — UX PER THROTTLE TIER

Schema B blocks for all B tiers. Six-item gate (a)–(f). Verify tier count against Role 3 directly (not Claim (d)). Insert REVISED at Claim (d) if mismatch.

Gate 8→9: All B tiers present. Six-item gate checked for each tier.

---

## ROLE 9 — VERDICT CURRENCY CHECK

Sweep Roles 1–8 for revision gaps. For each gap, insert REVISED marker annotated as "deferred from Role N". Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[Itemize if N > 0]

Gate 9→10: Currency sweep complete. Named output produced. Deferred markers carry source role annotation.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Role 9 CURRENCY SWEEP FINDINGS present.
Gate out: Final section. Reconciler findings published before document close.

**FORMAL NON-MODIFICATION INVARIANT — NMI-01**
- NMI-01 names itself: this block is NMI-01.
- NMI-01 states: the reconciler (this role) does not insert REVISED markers into the Verdict Block or any other section.
- NMI-01 states: the count of REVISED markers inserted by this role is zero.
- NMI-01 violation condition: any REVISED marker appearing in the Verdict Block that was inserted during Role 10's execution constitutes a violation of NMI-01. Halt and report "NMI-01 VIOLATION" before producing further findings.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT (NMI-01 COMPLIANCE CONFIRMATION)
This check operates under NMI-01.
- Behavioral declaration (i): This role is in VERIFICATION-ONLY mode.
- Behavioral declaration (ii): This role does not insert REVISED markers.
- Behavioral declaration (iii): REVISED marker insertion count for this role: zero.
Referencing NMI-01: confirm the three declarations above comply with the invariant declared in this role. Role 9 has already inserted any missing markers; this check verifies only.
Scan Verdict Block claims (a)–(d). Confirm each revised claim has an inline REVISED marker with forward reference to the revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9. Confirm named deliverables are present for each.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables. Flag cells with conclusions but no computation steps as Schema A CONTENT violations.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8. Flag blocks missing any of the four field labels.
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]

---

---

## V-03 — Single Axis: Output Format (standalone NMI section, no name reference in check (a) — C-34 borderline, C-35 FAIL)

**Axis:** Output format — adds a standalone "## PRE-TERMINAL INVARIANT — NMI-01" section between Role 9 and Role 10. The NMI block has all four required components: names itself, states non-modification, states zero count, names violation condition by invariant name. Gate 9→10 includes NMI-01 production as a required deliverable. However, check (a) inside Role 10 does not reference "NMI-01" by name — it says "pure verification only" in generic terms without naming the invariant. Three behavioral declarations remain implicit (same as V-01).

**Hypothesis:** C-34 BORDERLINE FAIL — same as V-01; zero-count declaration still absent from check (a) body. C-35 FAIL — NMI-01 is correctly positioned (before Role 10 opens) and has all four content components, but "The reconciler's check (a) must reference the invariant by its declared name" is a pass-condition requirement; check (a) saying "pure verification only" without the string "NMI-01" does not satisfy the name-reference requirement. The compliance delta from V-04 is exactly one addition: inserting "NMI-01" in check (a) and adding the three explicit declarations.

**v14 predicted scoring:** C-34 BORDERLINE FAIL. C-35 FAIL (no name reference in check (a)). Composite: 118.89/120.

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below. Each role produces named deliverables gated into the next role. Do not skip roles or merge roles.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell in any Schema A table will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete (BASELINE | PROTECTED | DERIVATION CHAIN columns present).
Claim (d): UX tier count will match the burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Schema A (three-column table):
| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|

Schema B (UX tier block — four named fields, all required):
```
ERROR SIGNAL: [value]
USER-VISIBLE BEHAVIOR: [value]
VISIBILITY LEVEL: [value]
RECOVERY PATH: [value]
```

Rejection clauses:
- Schema A STRUCTURAL: table missing one or more column headers
- Schema A CONTENT: DERIVATION CHAIN cell contains conclusion without computation steps
- Schema B STRUCTURAL: tier block missing one or more of the four field labels
- Schema B CONTENT: a field contains a non-answer (blank, "N/A", "varies")

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints. For each: numeric threshold, window duration, scope, type, Retry-After availability. Insert REVISED at Claim (a) if any endpoint lacks a backoff signal.

Gate 2→3: All endpoints enumerated. Claim (a) currency check complete.

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Classify each STRUCTURAL or INCIDENTAL. Record count B — authoritative source for gate item (e) in Role 8.

Gate 3→4: Burst path count B recorded. Each path classified.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Schema A table. DERIVATION CHAIN shows step-by-step causal chain with arithmetic.

Gate 4→5: Schema A table present with complete DERIVATION CHAIN arithmetic.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

YES / NO / PARTIAL per endpoint. Failure mode for non-YES. Insert REVISED at Claim (a) if not already inserted.

Gate 5→6: All endpoints assessed.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with >= 3 tiers including 5x spike row. All DERIVATION CHAIN cells show arithmetic steps.

Gate 6→7: Schema A table complete.

---

## ROLE 7 — MITIGATIONS

BEFORE/AFTER states per bottleneck. Reference which burst path(s) from Role 3 each addresses.

Gate 7→8: Each bottleneck has a mitigation with BEFORE/AFTER states.

---

## ROLE 8 — UX PER THROTTLE TIER

Schema B blocks for all B tiers. Six-item gate (a)–(f). Verify tier count against Role 3 directly. Insert REVISED at Claim (d) if mismatch.

Gate 8→9: All B tiers present. Six-item gate checked.

---

## ROLE 9 — VERDICT CURRENCY CHECK

Sweep Roles 1–8 for revision gaps. For each gap, insert REVISED marker annotated as "deferred from Role N". Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[Itemize if N > 0]

Gate 9→PRE-TERMINAL INVARIANT: Currency sweep complete. Named output produced. NMI-01 block must be produced before Role 10 opens.

---

## PRE-TERMINAL INVARIANT — NMI-01

**FORMAL NON-MODIFICATION INVARIANT — NMI-01**

This invariant is declared before the Terminal Reconciler (Role 10) opens and governs the reconciler's execution.

- NMI-01 names itself: this block is NMI-01, the Pre-Terminal Non-Modification Invariant.
- NMI-01 states: the Terminal Reconciler (Role 10) does not insert REVISED markers into the Verdict Block or any other section of this document.
- NMI-01 states: the count of REVISED markers inserted by Role 10 is zero.
- NMI-01 violation condition: any REVISED marker appearing in the Verdict Block that was inserted during Role 10's execution constitutes a violation of NMI-01. The reconciler must halt and report "NMI-01 VIOLATION" by invariant name before producing any further findings.

Gate PRE-TERMINAL INVARIANT → Role 10: NMI-01 block present with all four components (name, non-modification statement, zero count, violation condition). Do not open Role 10 until this block is complete.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Currency sweep complete (Role 9 CURRENCY SWEEP FINDINGS present). NMI-01 block present.
Gate out: Final section. Reconciler findings published before document close.

This check is pure verification — Role 9 has already inserted all missing markers.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Scan Verdict Block claims (a)–(d). For each claim, confirm an inline REVISED marker is present for every claim revised during analysis. Each marker must include a forward reference to the revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9 and the PRE-TERMINAL INVARIANT gate. Confirm named deliverables present for each.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables. Flag cells with conclusions but no computation steps.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8. Flag blocks missing any of the four field labels.
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]

---

---

## V-04 — Combined Axes: Role Sequence + Output Format (standalone NMI + explicit three declarations + name reference — C-34 PASS, C-35 PASS)

**Axis:** Role sequence + output format — 12-section sequence. Standalone "## PRE-TERMINAL INVARIANT — NMI-01" section between Role 9 and Role 10 (V-03 structure). Check (a) inside Role 10 produces three explicit behavioral declarations labeled (i), (ii), (iii), and references NMI-01 by name as the pre-declared constraint being confirmed. Gate 9→PRE-TERMINAL INVARIANT requires the NMI block as a deliverable; Gate PRE-TERMINAL INVARIANT→Role 10 gates on the NMI block being complete.

**Hypothesis:** C-34 PASS — check (a) produces three explicitly labeled behavioral declarations ((i) verification-only mode, (ii) no REVISED marker insertion, (iii) zero insertion count) from within the reconciler body, satisfying the "three behavioral declarations produced during the reconciler's own execution" requirement. C-35 PASS — NMI-01 is declared in a standalone section before Role 10 opens; has all four required components; check (a) references "NMI-01" by name; the invariant is not inside the reconciler body.

**v14 predicted scoring:** C-34 PASS. C-35 PASS. All 27 aspirational criteria pass. Composite: 120/120.

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below. Each role produces named deliverables gated into the next role. Do not skip roles or merge roles.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins. These claims will be revised inline if evidence contradicts them.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell in any Schema A table will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete (BASELINE | PROTECTED | DERIVATION CHAIN columns present).
Claim (d): UX tier count will match the burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Define the schemas that govern all subsequent output.

Schema A (three-column table for all quantitative analysis):
| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|

- BASELINE: observed or specified value before mitigation
- PROTECTED: target value after mitigation applied
- DERIVATION CHAIN: show every arithmetic step; conclusions without computation steps are a Schema A CONTENT violation

Schema B (UX tier block — four named fields, all required):
```
ERROR SIGNAL: [value]
USER-VISIBLE BEHAVIOR: [value]
VISIBILITY LEVEL: [value]
RECOVERY PATH: [value]
```

Rejection clauses:
- Schema A STRUCTURAL: table missing one or more column headers
- Schema A CONTENT: DERIVATION CHAIN cell contains conclusion without computation steps
- Schema B STRUCTURAL: tier block missing one or more of the four field labels
- Schema B CONTENT: a field contains a non-answer (blank, "N/A", "varies")

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints for the integration under analysis. For each endpoint state:
- Numeric threshold (requests per window)
- Window duration
- Scope (per-user / per-tenant / global)
- Type (connector-enforced vs platform-enforced)
- Retry-After header availability (YES / NO / PARTIAL)

If any endpoint lacks a Retry-After header or equivalent backoff signal, insert REVISED marker at Claim (a) with forward reference to this role.

Gate 2→3: All endpoints enumerated with numeric thresholds and scope. Claim (a) currency check complete.

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths in the integration. For each burst path:
- Classify as STRUCTURAL (unavoidable given the architecture) or INCIDENTAL (artifact of current implementation, removable)
- State the endpoint(s) involved

Record total burst path count as B. This count is the authoritative source for gate item (e) in Role 8.

Gate 3→4: Burst path count B recorded. Each path classified STRUCTURAL or INCIDENTAL.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Construct a Schema A table for the cascading failure scenario. Show:
- BASELINE: request volume at failure onset
- PROTECTED: volume threshold with circuit-breaker or backoff applied
- DERIVATION CHAIN: which endpoint triggers first, which downstream calls are blocked, compounding retry volume arithmetic step-by-step

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain with arithmetic.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

For each endpoint from Role 2: YES / NO / PARTIAL. Document failure mode for non-YES. Insert REVISED at Claim (a) if not already inserted.

Gate 5→6: All endpoints assessed. Failure modes documented for non-YES.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with >= 3 volume tiers including 5x spike row. Every DERIVATION CHAIN cell shows computation steps (e.g., "200 req/min × 5 = 1000 req/min; limit = 500 req/min; overflow = 500 req/min; queue depth at T+30s = 500 × 0.5 = 250 queued").

Gate 6→7: Schema A table with >= 3 tiers. All DERIVATION CHAIN cells contain arithmetic steps.

---

## ROLE 7 — MITIGATIONS

For each bottleneck from Roles 3–6, prescribe mitigation with BEFORE state and AFTER state. Reference which burst path(s) from Role 3 the mitigation addresses.

Gate 7→8: Each bottleneck covered. BEFORE/AFTER states present.

---

## ROLE 8 — UX PER THROTTLE TIER

For each burst path tier (count B from Role 3 — verify directly, not from Verdict Claim (d)), produce a Schema B UX block.

Six-item gate per block:
(a) ERROR SIGNAL field present and specific
(b) USER-VISIBLE BEHAVIOR field present and specific
(c) VISIBILITY LEVEL present (Silent / Banner / Modal / Blocking)
(d) RECOVERY PATH present and actionable
(e) Tier count equals B from Role 3 (verified directly — not from Verdict Claim (d))
(f) Each block has all four Schema B field labels (Schema B STRUCTURAL compliance)

Insert REVISED at Claim (d) with forward reference to this role if tier count does not match B.

Gate 8→9: All B tiers present. Six-item gate checked for each tier.

---

## ROLE 9 — VERDICT CURRENCY CHECK

This role is a dedicated pre-reconciler sweep. Its sole function is to ensure all Verdict Block revisions are marked before the Terminal Reconciler runs.

Step 1 — Sweep Roles 1–8 for every instance where a Verdict Claim was revised during analysis.
Step 2 — For each revision, confirm that an inline REVISED marker was inserted at the originating gate boundary.
Step 3 — For each gap: insert the REVISED marker now, annotated as "deferred from Role N" to distinguish from gate-boundary insertions.
Step 4 — Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[If N > 0, itemize: "Claim (X) — deferred from Role N — [reason]"]

Gate 9→PRE-TERMINAL INVARIANT: Currency sweep complete. Named output produced. Deferred markers carry source role annotation. NMI-01 block must be produced before Role 10 opens.

---

## PRE-TERMINAL INVARIANT — NMI-01

**FORMAL NON-MODIFICATION INVARIANT — NMI-01**

This invariant is declared before the Terminal Reconciler (Role 10) opens and governs the reconciler's execution.

- NMI-01 names itself: this block is NMI-01, the Pre-Terminal Non-Modification Invariant.
- NMI-01 states: the Terminal Reconciler (Role 10) does not insert REVISED markers into the Verdict Block or any other section of this document.
- NMI-01 states: the count of REVISED markers inserted by Role 10 is zero.
- NMI-01 violation condition: any REVISED marker appearing in the Verdict Block that was inserted during Role 10's execution constitutes a violation of NMI-01. The reconciler must halt and report "NMI-01 VIOLATION" by invariant name before producing any further findings.

Gate PRE-TERMINAL INVARIANT → Role 10: NMI-01 block complete with all four components (name, non-modification statement, zero count, violation condition by invariant name). Do not open Role 10 until this block is confirmed complete.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Currency sweep complete (Role 9 CURRENCY SWEEP FINDINGS present). NMI-01 block confirmed complete.
Gate out: Final section. Reconciler findings published before document close.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT (NMI-01 COMPLIANCE CONFIRMATION)
This check operates under NMI-01.
- Behavioral declaration (i): This role is in VERIFICATION-ONLY mode.
- Behavioral declaration (ii): This role does not insert REVISED markers.
- Behavioral declaration (iii): REVISED marker insertion count for this role: zero.
Referencing NMI-01: the three declarations above confirm compliance with the pre-declared constraint NMI-01. Role 9 has already inserted any missing markers; this check verifies only. Any marker insertion by this role constitutes NMI-01 VIOLATION — halt and report by invariant name.
Scan Verdict Block claims (a)–(d). For each claim, confirm an inline REVISED marker is present for every claim revised during analysis. Each marker must include a forward reference to the revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9 and the PRE-TERMINAL INVARIANT gate. For each gate confirm named deliverables from the prior section are present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 4 and 6). Flag any cell containing only a conclusion without computation steps as a Schema A CONTENT violation.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8. Flag any block missing one or more of the four field labels as a Schema B STRUCTURAL violation.
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]

---

---

## V-05 — Combined Axes: Full Integration (V-04 + explicit "deferred from Role N — [reason]" annotation — C-34 PASS, C-35 PASS)

**Axis:** Role sequence + output format + phrasing register — identical to V-04 in structure, but Role 9's currency sweep uses the explicit annotation format "deferred from Role N — [reason gate-boundary insertion did not fire]", making the source of each deferral traceable during terminal verification. Gate 9→PRE-TERMINAL INVARIANT names NMI-01 as a required gate deliverable by identifier, not just by category. The V-05 phrasing register is the most explicit form: every gate condition names its deliverables by identifier, and deferred marker annotations carry both the role origin and the reason for non-firing.

**Hypothesis:** Structural compliance is identical to V-04 (C-34 PASS, C-35 PASS). The phrasing-register difference creates an auditability advantage: a reviewer scanning for deferred markers can distinguish at a glance whether a marker was deferred because a gate currency check did not fire (named reason) vs. because the analysis role omitted insertion silently. This distinction is not required by C-34 or C-35 but raises the structural enforcement floor: the "deferred from Role N" annotation (introduced in R12) becomes "deferred from Role N — [reason]" (R12 V-05 pattern), which is the most auditable form. V-04 and V-05 predict identical composite scores; the difference is auditability of deferred markers, not compliance.

**v14 predicted scoring:** C-34 PASS. C-35 PASS. All 27 aspirational criteria pass. Composite: 120/120.

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below. Each role produces named deliverables gated into the next role. Do not skip roles or merge roles.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins. These claims will be revised inline if evidence contradicts them.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell in any Schema A table will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete (BASELINE | PROTECTED | DERIVATION CHAIN columns present).
Claim (d): UX tier count will match the burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Define the schemas that govern all subsequent output.

Schema A (three-column table for all quantitative analysis):
| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|

- BASELINE: observed or specified value before mitigation
- PROTECTED: target value after mitigation applied
- DERIVATION CHAIN: show every arithmetic step; conclusions without computation steps are a Schema A CONTENT violation

Schema B (UX tier block — four named fields, all required):
```
ERROR SIGNAL: [value]
USER-VISIBLE BEHAVIOR: [value]
VISIBILITY LEVEL: [value]
RECOVERY PATH: [value]
```

Rejection clauses:
- Schema A STRUCTURAL: table missing one or more column headers
- Schema A CONTENT: DERIVATION CHAIN cell contains conclusion without computation steps
- Schema B STRUCTURAL: tier block missing one or more of the four field labels
- Schema B CONTENT: a field contains a non-answer (blank, "N/A", "varies")

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints for the integration under analysis. For each endpoint state:
- Numeric threshold (requests per window)
- Window duration
- Scope (per-user / per-tenant / global)
- Type (connector-enforced vs platform-enforced)
- Retry-After header availability (YES / NO / PARTIAL)

If any endpoint lacks a Retry-After header or equivalent backoff signal, insert REVISED marker at Claim (a) with forward reference to this role.

Gate 2→3: All endpoints enumerated with numeric thresholds and scope. Claim (a) currency check complete.

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths in the integration. For each burst path:
- Classify as STRUCTURAL (unavoidable given the architecture) or INCIDENTAL (artifact of current implementation, removable)
- State the endpoint(s) involved

Record total burst path count as B. This count is the authoritative source for gate item (e) in Role 8. Do not derive tier count from Verdict Claim (d).

Gate 3→4: Burst path count B recorded. Each path classified STRUCTURAL or INCIDENTAL.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Construct a Schema A table for the cascading failure scenario. Show:
- BASELINE: request volume at failure onset
- PROTECTED: volume threshold with circuit-breaker or backoff applied
- DERIVATION CHAIN: which endpoint triggers first, which downstream calls are blocked, compounding retry volume arithmetic step-by-step

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain with arithmetic.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

For each endpoint from Role 2: YES / NO / PARTIAL. Document failure mode for non-YES. Insert REVISED at Claim (a) if not already inserted.

Gate 5→6: All endpoints assessed. Failure modes documented for non-YES.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with >= 3 volume tiers including 5x spike row. Every DERIVATION CHAIN cell shows computation steps (e.g., "200 req/min × 5 = 1000 req/min; limit = 500 req/min; overflow = 500 req/min; queue depth at T+30s = 500 × 0.5 = 250 queued").

Gate 6→7: Schema A table with >= 3 tiers. All DERIVATION CHAIN cells contain arithmetic steps.

---

## ROLE 7 — MITIGATIONS

For each bottleneck from Roles 3–6, prescribe mitigation with BEFORE state and AFTER state. Reference which burst path(s) from Role 3 the mitigation addresses.

Gate 7→8: Each bottleneck covered. BEFORE/AFTER states present.

---

## ROLE 8 — UX PER THROTTLE TIER

For each burst path tier (count B from Role 3 — verify directly, not from Verdict Claim (d)), produce a Schema B UX block.

Six-item gate per block:
(a) ERROR SIGNAL field present and specific
(b) USER-VISIBLE BEHAVIOR field present and specific
(c) VISIBILITY LEVEL present (Silent / Banner / Modal / Blocking)
(d) RECOVERY PATH present and actionable
(e) Tier count equals B from Role 3 (verified directly — not from Verdict Claim (d))
(f) Each block has all four Schema B field labels (Schema B STRUCTURAL compliance)

Insert REVISED at Claim (d) with forward reference to this role if tier count does not match B.

Gate 8→9: All B tiers present. Six-item gate checked for each tier.

---

## ROLE 9 — VERDICT CURRENCY CHECK

This role is a dedicated pre-reconciler sweep. Its sole function is to ensure all Verdict Block revisions are marked before the Terminal Reconciler runs.

Step 1 — Sweep Roles 1–8 for every instance where a Verdict Claim was revised during analysis.
Step 2 — For each revision, confirm that an inline REVISED marker was inserted at the originating gate boundary (by the role that discovered the revision).
Step 3 — For each gap (revision confirmed but no gate-boundary marker inserted): insert the REVISED marker now, annotated with the explicit format:
  "deferred from Role N — [reason gate-boundary insertion did not fire]"
This annotation format is required and must distinguish deferred markers from gate-boundary markers (gate-boundary markers carry no "deferred" annotation).
Step 4 — Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[If N > 0, itemize each:
  "Claim (X): deferred from Role N — [reason gate currency check did not fire at Role N's gate boundary]"]

Gate 9→PRE-TERMINAL INVARIANT (NMI-01): Currency sweep complete. Named output produced. All deferred markers carry explicit "deferred from Role N — [reason]" annotation. Zero ambiguity between deferred and gate-boundary insertions. NMI-01 block must be produced as a named deliverable before Role 10 opens.

---

## PRE-TERMINAL INVARIANT — NMI-01

**FORMAL NON-MODIFICATION INVARIANT — NMI-01**

This invariant is declared before the Terminal Reconciler (Role 10) opens and governs the reconciler's execution. It is a structural antecedent: the constraint is named here so that the reconciler's check (a) confirms compliance with a pre-declared rule rather than issuing its own claim.

- NMI-01 names itself: this block is NMI-01, the Pre-Terminal Non-Modification Invariant.
- NMI-01 states: the Terminal Reconciler (Role 10) does not insert REVISED markers into the Verdict Block or any other section of this document.
- NMI-01 states: the count of REVISED markers inserted by Role 10 is zero.
- NMI-01 violation condition: any REVISED marker appearing in the Verdict Block that was inserted during Role 10's execution constitutes a violation of NMI-01. The reconciler must halt and report "NMI-01 VIOLATION" by invariant name before producing any further findings.

Gate PRE-TERMINAL INVARIANT (NMI-01) → Role 10: NMI-01 block complete with all four components: (a) self-naming, (b) non-modification statement, (c) zero-count statement, (d) violation condition named by invariant identifier. Do not open Role 10 until NMI-01 is confirmed complete.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Currency sweep complete (Role 9 CURRENCY SWEEP FINDINGS present, with "deferred from Role N — [reason]" annotations on any deferred markers). NMI-01 block confirmed complete per Gate PRE-TERMINAL INVARIANT → Role 10.
Gate out: Final section. Reconciler findings published before document close.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT (NMI-01 COMPLIANCE CONFIRMATION)
This check operates under NMI-01.
- Behavioral declaration (i): This role is in VERIFICATION-ONLY mode.
- Behavioral declaration (ii): This role does not insert REVISED markers.
- Behavioral declaration (iii): REVISED marker insertion count for this role: zero.
Referencing NMI-01: the three declarations (i), (ii), (iii) above confirm compliance with the pre-declared constraint NMI-01. Role 9 has already inserted any missing markers using the "deferred from Role N — [reason]" annotation format; this check verifies only. Any marker insertion by this role constitutes NMI-01 VIOLATION — halt and report "NMI-01 VIOLATION" before producing further findings.
Scan Verdict Block claims (a)–(d). For each claim, confirm an inline REVISED marker is present for every claim revised during analysis. Each marker must include a forward reference to the revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9 and the PRE-TERMINAL INVARIANT (NMI-01) gate. For each gate confirm the named deliverables from the prior section are present in the document.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 4 and 6). Flag any cell containing only a conclusion without computation steps as a Schema A CONTENT violation.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8. Flag any block missing one or more of the four field labels (ERROR SIGNAL, USER-VISIBLE BEHAVIOR, VISIBILITY LEVEL, RECOVERY PATH) as a Schema B STRUCTURAL violation.
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
