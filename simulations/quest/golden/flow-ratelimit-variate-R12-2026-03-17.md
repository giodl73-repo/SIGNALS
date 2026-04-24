---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 12
rubric_version: 12
---

# flow-ratelimit — Variate R12

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence — complete 11-role sequence with dedicated pre-reconciler Role 9 and 4-check terminal reconciler), V-02 (output format — 4-check terminal reconciler without dedicated pre-reconciler role), V-03 (lifecycle emphasis — dedicated pre-reconciler role with basic 2-check terminal reconciler).
Combination variations: V-04 (role sequence + partial reconciler — pre-reconciler + 3-check reconciler), V-05 (full integration — pre-reconciler with explicit deferred-source annotation + 4-check reconciler).

**R12 target criteria: C-32, C-33**

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role count | 11 | 10 | 11 | 11 | 11 |
| Dedicated pre-reconciler (C-32) | YES | NO | YES | YES | YES |
| Reconciler check count | 4 | 4 | 2 | 3 | 4 |
| Deferred annotation explicit | implicit | n/a | implicit | implicit | explicit ("deferred from Role N") |
| C-32 | PASS | FAIL | PASS | PASS | PASS |
| C-33 | PASS | PASS | FAIL | FAIL | PASS |

---

## V-01

**Axis:** Role sequence — complete 11-role sequence with dedicated VERDICT CURRENCY CHECK (Role 9) and 4-check terminal reconciler (Role 10). Both C-32 and C-33 satisfied.

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
- Schema B CONTENT: a field contains a non-answer (e.g., "N/A", "varies", blank)

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints for the integration under analysis. For each endpoint state:
- Numeric threshold (requests per window)
- Window duration
- Scope (per-user / per-tenant / global)
- Type (connector-enforced vs platform-enforced)
- Verdict currency check: confirm Claim (a) applies — header present or backoff signal documented

If any endpoint lacks a Retry-After header, insert REVISED marker at Claim (a) with forward reference to this role.

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
- DERIVATION CHAIN: show the causal chain step-by-step — which endpoint hits limit first, which downstream calls are blocked, compounding effect on retry volume

Describe the compounding effect in prose following the table.

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain (not bare conclusion).

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

For each endpoint from Role 2, determine: does the response include a usable Retry-After value (or equivalent)?

Verdict per endpoint: YES / NO / PARTIAL
- YES: header present with numeric or date value, client can honor it automatically
- NO: header absent; failure mode: client must guess backoff interval, risks amplifying burst
- PARTIAL: header present but value is unreliable (e.g., always returns 0)

If any endpoint is NO or PARTIAL, this is evidence against Claim (a). Insert REVISED marker at Claim (a) with forward reference to this role if not already inserted.

Gate 5→6: All endpoints assessed. Any NO/PARTIAL endpoints have failure modes documented.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a Schema A table with at least three volume tiers. Include a 5x load spike row.

| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|
| [tier 1 volume] | [protected threshold] | [arithmetic: e.g., 200 req/min baseline × 5 = 1000 req/min spike; limit = 500 req/min; overflow = 500 req/min; queue depth at T+30s = 500 × 0.5 = 250 queued] |
| [tier 2 volume] | ... | ... |
| [5x spike] | ... | [must show multiplication and overflow arithmetic explicitly] |

Every DERIVATION CHAIN cell must show computation steps. Bare conclusions ("exceeds limit") are Schema A CONTENT violations.

Gate 6→7: Schema A table with >= 3 tiers including 5x spike row. All DERIVATION CHAIN cells contain arithmetic.

---

## ROLE 7 — MITIGATIONS

For each bottleneck identified in Roles 3–6, prescribe a mitigation. Present each mitigation with:
- BEFORE state (current behavior without mitigation)
- AFTER state (behavior after mitigation applied)
- Which burst path(s) from Role 3 the mitigation addresses

Gate 7→8: Each bottleneck has a mitigation. BEFORE/AFTER states present for each.

---

## ROLE 8 — UX PER THROTTLE TIER

For each burst path tier from Role 3 (use Role 3's count B directly), produce a Schema B UX block.

Each block must pass the six-item gate:
(a) ERROR SIGNAL field present and specific
(b) USER-VISIBLE BEHAVIOR field present and specific
(c) VISIBILITY LEVEL field present (Silent / Banner / Modal / Blocking)
(d) RECOVERY PATH field present and actionable
(e) Tier count in this role equals burst path count B from Role 3 (verify directly — do not use Verdict Claim (d))
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
[If N > 0, itemize each: "Claim (X) — deferred from Role N — [reason marker was not placed at gate boundary]"]

Gate 9→10: Currency sweep complete. Named output produced (either "0 deferred markers inserted" or itemized list with source roles). All deferred markers annotated with origin role.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Currency sweep complete (Role 9 CURRENCY SWEEP FINDINGS output present).
Gate out: This is the final section. Reconciler findings published before document close.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Scan Verdict Block claims (a)–(d). For each claim, confirm:
- An inline REVISED marker is present for every claim revised during analysis
- Each marker includes a forward reference to the revising role
This check is pure verification only — Role 9 has already inserted any missing markers.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate each gated transition (Gate 0→1 through Gate 8→9). For each gate confirm:
- Named prior-section deliverables are present in the document
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 4 and 6).
- Flag any cell containing only a conclusion without computation steps as a Schema A CONTENT violation
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8.
- Flag any tier block missing one or more of the four field labels (ERROR SIGNAL, USER-VISIBLE BEHAVIOR, VISIBILITY LEVEL, RECOVERY PATH) as a Schema B STRUCTURAL violation
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]

---

## V-02

**Axis:** Output format — 10-role sequence (no dedicated pre-reconciler role). Terminal Reconciler (Role 9) contains all four checks (a)–(d). C-33 PASS, C-32 FAIL (no dedicated pre-reconciler role; check (a) performs deferred marker correction rather than pure verification).

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete.
Claim (d): UX tier count will match burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Schema A (three-column table):
| BASELINE | PROTECTED | DERIVATION CHAIN |

Schema B (UX tier block — four named fields, all required):
```
ERROR SIGNAL: [value]
USER-VISIBLE BEHAVIOR: [value]
VISIBILITY LEVEL: [value]
RECOVERY PATH: [value]
```

Rejection clauses: Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT.

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate-limited endpoints. For each: numeric threshold, window, scope, connector vs platform type, Retry-After availability. Insert REVISED at Claim (a) if any endpoint lacks a backoff signal.

Gate 2→3: All endpoints enumerated. Verdict currency check complete for Claim (a).

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Classify each STRUCTURAL or INCIDENTAL. Record total count B for use in Role 8 gate item (e).

Gate 3→4: Burst path count B recorded. Each path classified.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Schema A table with causal chain in DERIVATION CHAIN column. Show step-by-step which endpoint triggers first, downstream block sequence, compounding retry volume arithmetic.

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

Assess each endpoint: YES / NO / PARTIAL. Document failure mode for non-YES. Insert REVISED at Claim (a) if not already inserted for any NO/PARTIAL.

Gate 5→6: All endpoints assessed. Failure modes documented.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with >= 3 volume tiers including 5x spike row. All DERIVATION CHAIN cells show arithmetic steps (e.g., "200 req/min × 5 = 1000 req/min; limit = 500; overflow = 500 req/min; queue depth T+30s = 500 × 0.5 = 250").

Gate 6→7: Schema A table with >= 3 tiers. All DERIVATION CHAIN cells show computation steps.

---

## ROLE 7 — MITIGATIONS

For each bottleneck, prescribe a mitigation with BEFORE/AFTER states and reference to burst path(s) from Role 3.

Gate 7→8: Each bottleneck has a mitigation with BEFORE/AFTER states.

---

## ROLE 8 — UX PER THROTTLE TIER

For each burst path tier (count B from Role 3), produce a Schema B UX block. Six-item gate: (a) ERROR SIGNAL present, (b) USER-VISIBLE BEHAVIOR present, (c) VISIBILITY LEVEL present, (d) RECOVERY PATH present, (e) tier count equals B (verify from Role 3 directly), (f) Schema B STRUCTURAL compliance. Insert REVISED at Claim (d) if tier count mismatches.

Gate 8→9: All B tiers present. Six-item gate checked for each tier.

---

## ROLE 9 — TERMINAL RECONCILER

Gate in: Role 8 UX tiers complete.
Gate out: Final section. Reconciler findings published before document close.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Scan Verdict Block claims (a)–(d). For each claim, confirm an inline REVISED marker is present for every revision. If a marker is missing, insert it now (this check performs both correction and verification — no dedicated pre-reconciler role precedes it).
Findings: "Verdict Audit: N marker(s) verified/inserted, M gap(s) resolved"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 7→8. Confirm named deliverables are present for each gate.
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

## V-03

**Axis:** Lifecycle emphasis — 11-role sequence with dedicated VERDICT CURRENCY CHECK (Role 9, satisfies C-32), but Terminal Reconciler (Role 10) only has checks (a) and (b). C-32 PASS, C-33 FAIL (checks c and d absent), C-24 PARTIAL (check c absent from reconciler), C-27 PARTIAL (check d absent from reconciler).

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below.

## ROLE 0 — VERDICT BLOCK

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete.
Claim (d): UX tier count will match burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated.

---

## ROLE 1 — FORMAT CONTRACT

Schema A: | BASELINE | PROTECTED | DERIVATION CHAIN |
Schema B four named fields: ERROR SIGNAL, USER-VISIBLE BEHAVIOR, VISIBILITY LEVEL, RECOVERY PATH.
Rejection clauses: Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT.

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate endpoints with numeric thresholds, scope, type, and Retry-After availability. Insert REVISED at Claim (a) if any endpoint lacks a backoff signal.

Gate 2→3: Endpoints enumerated. Claim (a) currency check complete.

---

## ROLE 3 — BURST PATH AUDIT

Identify burst paths, classify STRUCTURAL or INCIDENTAL, record count B for Role 8.

Gate 3→4: Count B recorded. Each path classified.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Schema A table. DERIVATION CHAIN shows causal chain step-by-step with arithmetic.

Gate 4→5: Schema A table present with complete DERIVATION CHAIN.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

YES / NO / PARTIAL per endpoint. Failure mode for non-YES. REVISED at Claim (a) if needed.

Gate 5→6: All endpoints assessed.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table >= 3 tiers with 5x spike row. All DERIVATION CHAIN cells show arithmetic steps.

Gate 6→7: Schema A table complete with computation steps in every DERIVATION CHAIN cell.

---

## ROLE 7 — MITIGATIONS

Per-bottleneck prescriptions with BEFORE/AFTER states.

Gate 7→8: Each bottleneck has BEFORE/AFTER mitigation.

---

## ROLE 8 — UX PER THROTTLE TIER

Schema B blocks for all B tiers. Six-item gate (a)–(f). Verify tier count against Role 3 directly (not Claim (d)). Insert REVISED at Claim (d) if mismatch.

Gate 8→9: All B tiers present. Six-item gate checked.

---

## ROLE 9 — VERDICT CURRENCY CHECK

Sweep all prior roles (1–8) for Verdict claim revisions where the REVISED marker was not inserted at the originating gate boundary.

Step 1: Identify all revisions made during analysis (Roles 2–8).
Step 2: Confirm each has an inline REVISED marker at the gate boundary of the revising role.
Step 3: For each gap: insert the REVISED marker now, annotated as "deferred from Role N" to distinguish from gate-boundary insertions.
Step 4: Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[If N > 0: itemize with role origin]

Gate 9→10: Currency sweep complete. Named output produced. Deferred markers annotated with source role.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Role 9 CURRENCY SWEEP FINDINGS present.
Gate out: Final section.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Verify all claims revised during analysis have inline REVISED markers. Role 9 has already inserted deferred markers, so this is verification only.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9. Confirm deliverables present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

RECONCILER FINDINGS: N violation(s) total across checks (a)–(b).

---

## V-04

**Axis:** Role sequence + partial reconciler — 11-role sequence with dedicated VERDICT CURRENCY CHECK (Role 9, C-32 PASS), but Terminal Reconciler has checks (a), (b), (c) without check (d). C-32 PASS, C-24 PASS, C-27 PARTIAL (no check d), C-33 FAIL (check d absent).

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below.

## ROLE 0 — VERDICT BLOCK

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete.
Claim (d): UX tier count will match burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated.

---

## ROLE 1 — FORMAT CONTRACT

Schema A: | BASELINE | PROTECTED | DERIVATION CHAIN |
Schema B: ERROR SIGNAL, USER-VISIBLE BEHAVIOR, VISIBILITY LEVEL, RECOVERY PATH (all four required).
Rejection clauses: Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT.

Gate 1→2: Both schemas defined. All four rejection clauses stated.

---

## ROLE 2 — RATE LIMIT REGISTRY

Enumerate endpoints with numeric thresholds, window, scope, type, Retry-After availability. Insert REVISED at Claim (a) if needed.

Gate 2→3: Endpoints enumerated. Claim (a) currency check complete.

---

## ROLE 3 — BURST PATH AUDIT

Classify burst paths STRUCTURAL or INCIDENTAL. Record count B.

Gate 3→4: Count B recorded.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Schema A table. DERIVATION CHAIN shows step-by-step causal chain arithmetic.

Gate 4→5: Schema A table with complete DERIVATION CHAIN.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

YES / NO / PARTIAL per endpoint. Failure mode for non-YES. REVISED at Claim (a) if needed.

Gate 5→6: All endpoints assessed.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table >= 3 tiers with 5x spike row. All DERIVATION CHAIN cells show arithmetic steps.

Gate 6→7: Schema A table complete.

---

## ROLE 7 — MITIGATIONS

BEFORE/AFTER states per bottleneck.

Gate 7→8: All bottlenecks covered.

---

## ROLE 8 — UX PER THROTTLE TIER

Schema B blocks for all B tiers. Six-item gate (a)–(f). Verify tier count from Role 3 directly. Insert REVISED at Claim (d) if mismatch.

Gate 8→9: All B tiers present. Six-item gate checked.

---

## ROLE 9 — VERDICT CURRENCY CHECK

Sweep Roles 1–8 for revision gaps. For each gap, insert REVISED marker annotated as "deferred from Role N". Produce named output:

CURRENCY SWEEP FINDINGS: [N] deferred marker(s) inserted
[Itemize if N > 0]

Gate 9→10: Currency sweep complete. Named output produced. Deferred markers carry source role annotation.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Role 9 CURRENCY SWEEP FINDINGS present.
Gate out: Final section.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Verify all revised claims have inline REVISED markers (Role 9 handled insertions; this is verification only).
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9. Confirm deliverables present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 4 and 6). Flag cells with conclusions but no computation steps.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

RECONCILER FINDINGS: N violation(s) total across checks (a)–(c).

---

## V-05

**Axis:** Full integration — same as V-01 but Role 9 uses explicit "deferred from Role N — [reason]" annotation language, making the source of each deferral traceable during terminal verification. V-05 matches V-01 score (120/120) with enhanced auditability.

---

You are executing the `flow-ratelimit` skill. Produce a structured analysis document following the role sequence below.

## ROLE 0 — VERDICT BLOCK

State four claims before any analysis begins.

Claim (a): All rate-limited endpoints expose a Retry-After header or equivalent backoff signal.
Claim (b): No DERIVATION CHAIN cell will contain a bare conclusion without computation steps.
Claim (c): All Schema A tables will be structurally complete (BASELINE | PROTECTED | DERIVATION CHAIN).
Claim (d): UX tier count will match burst path count from Role 3; Schema B four-field template applied to every tier.

Gate 0→1: All four claims stated. No analysis yet.

---

## ROLE 1 — FORMAT CONTRACT

Schema A (three-column table):
| BASELINE | PROTECTED | DERIVATION CHAIN |

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

Enumerate all rate-limited endpoints. For each: numeric threshold, window duration, scope, connector vs platform type, Retry-After header availability. Insert REVISED at Claim (a) if any endpoint lacks a backoff signal.

Gate 2→3: All endpoints enumerated with numeric thresholds and scope. Verdict currency check complete for Claim (a).

---

## ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Classify each STRUCTURAL or INCIDENTAL. Record total count B — this is the authoritative source for gate item (e) in Role 8.

Gate 3→4: Burst path count B recorded. Each path classified.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

Schema A table showing cascading failure. DERIVATION CHAIN must show: which endpoint triggers first, which downstream calls are blocked, compounding retry volume arithmetic step-by-step.

Gate 4→5: Schema A table present. DERIVATION CHAIN shows step-by-step causal chain with arithmetic.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

For each endpoint from Role 2, assess: YES / NO / PARTIAL. Document failure mode for non-YES. Insert REVISED at Claim (a) if not already inserted.

Gate 5→6: All endpoints assessed. Failure modes documented for non-YES.

---

## ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with >= 3 volume tiers including a 5x load spike row. Every DERIVATION CHAIN cell must show computation steps (e.g., "200 req/min × 5 = 1000 req/min; limit = 500 req/min; overflow = 500 req/min; queue depth at T+30s = 500 × 0.5 = 250 queued").

Gate 6→7: Schema A table with >= 3 tiers. All DERIVATION CHAIN cells show arithmetic steps.

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
(e) Tier count equals B from Role 3 (verified directly)
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

Gate 9→10: Currency sweep complete. Named output produced. All deferred markers carry explicit "deferred from Role N — [reason]" annotation. Zero ambiguity between deferred and gate-boundary insertions.

---

## ROLE 10 — TERMINAL RECONCILER

Gate in: Currency sweep complete (Role 9 CURRENCY SWEEP FINDINGS output present).
Gate out: Final section. Reconciler findings published before document close.

Perform four separate audit checks. Each check produces its own named findings output.

CHECK (a) — VERDICT REVISION MARKER AUDIT
Scan Verdict Block claims (a)–(d). For each claim, confirm:
- An inline REVISED marker is present for every claim revised during analysis
- Each marker includes a forward reference to the revising role
This check is pure verification — Role 9 has already inserted all missing markers (with "deferred from Role N — [reason]" annotation).
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

CHECK (b) — GATE DELIVERABLE AUDIT
Enumerate gated transitions Gate 0→1 through Gate 8→9. For each gate confirm named deliverables are present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables"

CHECK (c) — DERIVATION CHAIN CELL AUDIT
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 4 and 6). Flag any cell with only a conclusion and no computation steps as a Schema A CONTENT violation.
Findings: "Derivation Chain Audit: N cells checked, M Schema A CONTENT violation(s)"

CHECK (d) — SCHEMA B STRUCTURAL SCAN
Count field labels in every UX tier block in Role 8. Flag any block missing one or more of the four field labels.
Findings: "Schema B Scan: N tier(s) checked, M Schema B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
