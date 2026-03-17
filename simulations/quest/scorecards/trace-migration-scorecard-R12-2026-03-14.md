## Round 12 Scoring — trace-migration (Rubric v10)

**Rubric:** 34 criteria · 220 pts · Golden ≥ 176 (80%) · New criterion: C-34 Phase Boundary Dual-Anchor Gate Block

---

## Shared Baseline (All Five Variations)

Before the per-variation tables, criteria that score identically across all five are resolved here.

| ID | Tier | All-V Verdict | Evidence |
|----|------|--------------|---------|
| C-01 | Essential | PASS | P0 step registry + B1 canonical table both require exact type names, constraint definitions, before/after states per entity |
| C-02 | Essential | PASS | DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE required in every Q section; NO requires explicit reasoning |
| C-03 | Essential | PASS | Per-type BINARY FIELDs (NOT NULL / FK / UNIQUE / CHECK) in every Q section; no free-form routing allowed |
| C-04 | Essential | PASS | DEFAULT presence check instruction appears in every Q section with "ALL tables, not financial columns only" prohibition |
| C-05 | Essential | PASS | Phase B carries explicit "C-05 is satisfied by Phase B alone" assertion; Phase A is explicitly excluded |
| C-06 | Recommended | PASS | Section F in Q1/Q2/Q3: table name, row count estimate, specific risk type required |
| C-07 | Recommended | PASS | ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) required in Section G of every Q section |
| C-08 | Recommended | PASS | B2 Domain Synthesis pre-seeded with domain-consequence example naming specific table + numeric threshold |
| C-09 | Aspirational | PASS | Section E (zero-downtime viability) in every Q section; maintenance window step + engine reason required |
| C-10 | Aspirational | PASS | Section H (idempotency check) in every Q section; failure mode required if not safe to re-run |
| C-11 | Aspirational | PASS | P0 registry established first; "Step N from P0" citation mandate in PARITY ENFORCEMENT BLOCK + per-Q sections |
| C-12 | Aspirational | PASS | B2 "(POSITIONED BEFORE B3 VERIFY)" label places domain synthesis before verification in all variations |
| C-13 | Aspirational | PASS | DATA LOSS PATH, NOT NULL RISK, ROLLBACK VIABILITY all use BINARY FIELD / fixed taxonomy; free-form omission is structurally visible |
| C-14 | Aspirational | PASS | "(BINARY FIELD)" annotation present at every definition site for critical fields across all Q sections |
| C-15 | Aspirational | PASS | PARSE GATE, TRACE GATE, DOMAIN SYNTHESIS GATE, VERIFY GATE, RECOMMENDATIONS GATE, VERDICT GATE — all carry OPEN/BLOCKED binary states guarding downstream phases |
| C-16 | Aspirational | PASS | Phase A (INTERROGATION) vs Phase B (CANONICAL OUTPUT) explicit separation with structural decoupling assertion |
| C-17 | Aspirational | PASS | Gate state fields carry "(BINARY FIELD)" annotation at definition site in all variations |
| C-18 | Aspirational | PASS | "Step N from P0" names P0 as source artifact in PARITY ENFORCEMENT BLOCK and in every Q section's citation line |
| C-19 | Aspirational | PASS | "**Citation**: Reference each affected step as 'Step N from P0.'" appears in Q1, Q2, and Q3 individually; not global-preamble-only |
| C-20 | Aspirational | PASS | B2 header: "(POSITIONED BEFORE B3 VERIFY -- complete before writing B3)" is a forward-named completion constraint |
| C-21 | Aspirational | PASS | Every phase transition gated: PARSE→Phase A, Phase A→Phase B (TRACE GATE), B1→B2, B2→B3, B3→B4, B4→VERDICT; chain is complete |
| C-22 | Aspirational | PASS | B2 in all variations contains a pre-seeded worked example as model output text (payment_amount / fulfillment_date examples) |
| C-23 | Aspirational | PASS | PARSE PHASE is a named phase wrapper with PARSE GATE (BINARY FIELD) at its exit; Phase A opening names PARSE GATE as entry prerequisite |
| C-24 | Aspirational | PASS | B1→B2: DOMAIN SYNTHESIS GATE; B2→B3: VERIFY GATE; at least one intra-Phase-B gate chain present with downstream section naming gate |
| C-25 | Aspirational | PASS | Phase B header explicitly carries "C-05 is satisfied by Phase B alone, not by any Phase A section" |
| C-26 | Aspirational | PASS | VERDICT section names VERDICT GATE as entry prerequisite, closing the terminal exit gap |
| C-27 | Aspirational | PASS | B2 pre-seeded example carries all three parts: prior working state + how migration breaks it + numeric business consequence |
| C-28 | Aspirational | PASS | Four dedicated BINARY FIELDs per Q section (NOT NULL / FK / UNIQUE / CHECK); DISQUALIFIER prohibition against free-form routing |
| C-29 | Aspirational | PASS | PARITY ENFORCEMENT BLOCK mandates complete 8-item checklist for every Q section; per-Q reminder repeats scope prohibitions |
| C-30 | Aspirational | PASS | Phase A domain expert sections (Q1/Q2/Q3) seed before/after analysis with domain-framed risk, satisfying C-27 Phase A requirement; B2 seeds distinct inertia-contrast example in Phase B |
| C-31 | Aspirational | PASS | P0a CONSTRAINT TYPE REGISTRY is a named table enumerating all four types before any analysis; described as "binding manifest" |
| C-32 | Aspirational | PASS | B1 canonical table columns include all four constraint-type BINARY FIELDs; P0a binding manifest enforces presence for YES-marked types |
| C-33 | Aspirational | PASS | PARITY ENFORCEMENT BLOCK appears before Q1 with numbered checklist and explicit "DO NOT SCOPE / apply to ALL roles" prohibitions per item |

**Shared base score (C-01 through C-33 all PASS):** 215 pts

---

## Per-Variation Scoring — C-34 and Delta Analysis

---

### V-01 — Axis A: C-34 EXIT BLOCK Advisory

**Axis**: EXIT BLOCKs removed from phase bottoms; gates appear only as inline fields (PARSE GATE, TRACE GATE, etc.) at phase exits without named EXIT BLOCK label. ENTRY REFERENCEs at phase tops preserved and annotated with (BINARY FIELD).

| ID | Verdict | Evidence |
|----|---------|---------|
| C-34 | **FAIL** | Every phase boundary has ENTRY REFERENCE at succeeding phase's opening — bilateral detectability fails. PARSE PHASE ends with `PARSE GATE (BINARY FIELD)` field but no named EXIT BLOCK structure restating what downstream phase it guards. Gate violation is visible from the succeeding phase's entry only; reading Phase A's final content reveals no named exit anchor. C-21 and C-17 PASS: the gate serves its transition function and carries (BINARY FIELD) annotation, but the anchor is at one structural position, not two. |

**V-01 Score: 215 / 220**
All essential PASS. Golden: YES (215 ≥ 176).

---

### V-02 — Axis B: C-34 ENTRY REFERENCE Advisory

**Axis**: ENTRY REFERENCEs removed from phase tops; named "PHASE A EXIT BLOCK", "DOMAIN SYNTHESIS GATE EXIT BLOCK", etc. at phase bottoms preserved and annotated with (BINARY FIELD). Succeeding phase headers carry no entry prerequisite statement.

| ID | Verdict | Evidence |
|----|---------|---------|
| C-34 | **FAIL** | Named EXIT BLOCK structures appear at every phase boundary bottom with forward-pointing instruction ("Do not begin Phase B until TRACE GATE = OPEN") — but Phase B's opening instruction does not name TRACE GATE as its entry prerequisite. Gate violation is visible from the preceding phase's exit only; opening Phase B reveals no entry anchor. C-21 PASS: forward-pointing EXIT BLOCK instruction establishes the gate as an entry prerequisite functionally. C-17 PASS: EXIT BLOCK carries (BINARY FIELD) annotation. C-34 FAIL: one structural position only. |

**V-02 Score: 215 / 220**
All essential PASS. Golden: YES (215 ≥ 176).

---

### V-03 — Axis C: BOUNDARY PROTOCOL Dual-Anchor Block

**Axis**: Every phase boundary carries a named `BOUNDARY PROTOCOL` block containing two explicit fields — `EXIT BLOCK (BINARY FIELD)` and `ENTRY REFERENCE (BINARY FIELD)` — as a self-contained structural unit at the boundary point.

| ID | Verdict | Evidence |
|----|---------|---------|
| C-34 | **PASS** | Named BOUNDARY PROTOCOL block present at every phase boundary. Both EXIT BLOCK and ENTRY REFERENCE appear as named fields with (BINARY FIELD) annotation within the same structural artifact. Gate compliance is verifiable from either phase's text: a reader at Parse Phase's end sees the EXIT BLOCK; a reader at Phase A's opening sees the ENTRY REFERENCE. Both positions annotated; bilateral detectability requirement satisfied. No gate boundary is left with single-anchor coverage. |

**C-35 candidate observed**: BOUNDARY PROTOCOL as a named structural artifact creates a new verifiability mechanism — gate coverage is computable from protocol block count (5 boundaries = 5 BOUNDARY PROTOCOL blocks). A missing block is a named-section gap detectable by header scan, not by reading phase interiors.

**V-03 Score: 220 / 220**
All essential PASS. Golden: YES.

---

### V-04 — Axes C + D: BOUNDARY PROTOCOL + Inertia-First Framing

**Axis**: V-03 BOUNDARY PROTOCOL blocks at every boundary + named `STATUS QUO COST` section inserted before Q1 in Phase A, establishing three-part inertia-contrast baseline (current schema condition + business process that currently works + accumulation trajectory if migration abandoned).

| ID | Verdict | Evidence |
|----|---------|---------|
| C-34 | **PASS** | BOUNDARY PROTOCOL dual-anchor blocks from V-03 fully preserved. |
| C-27 | **PASS** | STATUS QUO COST section forces three-part inertia-contrast structure before any role analysis begins, anchoring the inertia baseline at parse time. Q1/Q2/Q3 domain examples reference STATUS QUO COST baseline explicitly, elevating inertia-contrast density in Phase A. |
| C-30 | **PASS** | STATUS QUO COST creates a Phase A inertia anchor distinct from the Phase B B2 example; dual-phase seeding now has a pre-committed Phase A origin point rather than relying on role-section framing alone. |

**Excellence signals beyond V-03**:
- STATUS QUO COST as pre-Phase-A pre-commitment: forces cause-level reasoning (why the system currently works) before any role-specific analysis begins, preventing effect-level description from being the Phase A baseline.
- Inertia-contrast density elevated: Q1/Q2/Q3 anchor to STATUS QUO COST creates convergent cross-role inertia framing without cross-role example duplication.

**V-04 Score: 220 / 220**
All essential PASS. Golden: YES.

---

### V-05 — Axes C + D + E: BOUNDARY PROTOCOL + Inertia-First + Operations-First Role Sequence

**Axis**: V-04 in full + Operations Expert leads Phase A as Q1 (Commerce = Q2, Finance = Q3); STATUS QUO COST has infrastructure orientation; B2 requires a **cross-role inertia chain** seeding an Operations-grounded cause from Q1/STATUS QUO COST expressed as a Commerce or Finance consequence.

| ID | Verdict | Evidence |
|----|---------|---------|
| C-34 | **PASS** | BOUNDARY PROTOCOL dual-anchor blocks from V-03 fully preserved. |
| C-27 | **PASS** | STATUS QUO COST with infrastructure orientation + Operations-first framing forces inertia analysis to begin with the operational substrate (job queues, deployment scaffolding) that commerce and finance processes depend on. Inertia contrast is more causally anchored than commerce-first framing. |
| C-30 | **PASS** | STATUS QUO COST seeds Phase A inertia anchor; B2 cross-role chain seeds distinct Phase B example with a named cause-consequence pair. |
| C-08 | **PASS** | B2 cross-role inertia chain provides domain framing that a single-role example cannot: "Operations infrastructure condition (cause) → Commerce order pipeline consequence" names a failure mode that requires two roles to express. |
| C-29 | **PASS** | Operations-first ordering means the parity enforcement checklist is exercised against the infrastructure lens first; DEFAULT checks and zero-downtime viability appear in Operations context before Commerce reframes them. Cross-role mandate verified. |

**Excellence signals beyond V-04**:
- Operations-first role sequence: exposes STATUS QUO COST baseline to infrastructure lens before commerce framing applies; inertia cost is expressed as infrastructure risk (schema rigidity → deployment constraint → commerce dependency), generating a richer three-part anchor.
- Cross-role inertia chain in B2 as a new structural artifact class: an Operations-cause / Commerce-consequence pair that is unreachable from either role section alone, requiring B2 synthesis to name the causal link. Potential **C-36 candidate**: cross-role inertia chain as a required named structural artifact in B2 when multi-role Phase A analysis is present.

**V-05 Score: 220 / 220**
All essential PASS. Golden: YES.

---

## Composite Score Summary

| V | Score | / 220 | % | Golden | Differentiating Criteria |
|---|-------|-------|---|--------|--------------------------|
| V-01 | 215 | 215/220 | 97.7% | YES | C-34 FAIL (exit-side anchor only) |
| V-02 | 215 | 215/220 | 97.7% | YES | C-34 FAIL (entry-side anchor only) |
| V-03 | **220** | 220/220 | 100% | YES | C-34 PASS; C-35 candidate |
| V-04 | **220** | 220/220 | 100% | YES | C-34 PASS; STATUS QUO COST inertia anchor |
| V-05 | **220** | 220/220 | 100% | YES | C-34 PASS; cross-role inertia chain signal |

**Rank**: V-03 = V-04 = V-05 (220) > V-01 = V-02 (215)
**Tiebreak within top tier**: V-05 > V-04 > V-03 by excellence signal density

---

## Excellence Signals (V-05 as richest top-scoring variant)

**Signal 1 — BOUNDARY PROTOCOL as named structural artifact** (V-03+)
The BOUNDARY PROTOCOL block creates a first-class structural artifact at every phase boundary. Gate coverage becomes computable from protocol block count alone: N boundaries = N BOUNDARY PROTOCOL blocks. A missing block is detectable by scanning for BOUNDARY PROTOCOL headings without reading phase interiors. This decouples gate-compliance verification from phase-content reading.
*C-35 candidate*: require BOUNDARY PROTOCOL block count to equal named phase boundary count; a missing block is a manifest violation.

**Signal 2 — STATUS QUO COST pre-Phase-A pre-commitment** (V-04+)
The STATUS QUO COST section forces three-part inertia-contrast reasoning before any role analysis begins: (a) current schema condition, (b) business process that currently works because of it, (c) accumulation rate if migration is abandoned. This commits the inertia baseline at parse time, making all subsequent role-specific analyses refer back to a named baseline rather than constructing inertia framing independently. Prevents effect-level description from becoming the Phase A default.

**Signal 3 — Cross-role inertia chain as structural artifact in B2** (V-05)
The cross-role inertia chain (Operations-grounded cause expressed as Commerce or Finance consequence) is a structural artifact that no single-role Phase A section can produce. B2 Domain Synthesis becomes the first location where the causal chain crosses role boundaries, naming the structural dependency between infrastructure risk and commerce pipeline vulnerability.
*C-36 candidate*: when Phase A contains ≥2 domain roles, require B2 to seed one cross-role inertia chain naming role-A cause and role-B consequence as distinct named fields.

---

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["BOUNDARY PROTOCOL block as named structural artifact makes gate coverage computable from protocol block count — N boundaries requires N BOUNDARY PROTOCOL blocks, missing block detectable by header scan without reading phase interiors", "STATUS QUO COST pre-Phase-A section commits inertia baseline before role analysis begins, forcing cause-level reasoning and preventing effect-level description from becoming the Phase A default", "Cross-role inertia chain in B2 seeds an Operations-cause to Commerce-consequence pair that single-role Phase A sections cannot produce, making B2 the first site where inter-role causal dependency is named as a structural artifact"]}
```
