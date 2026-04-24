I now have all the information needed to score all five R12 variations. Let me produce the full scorecard.

---

# Quest Scorecard — campaign-behavior (R12)
**Rubric:** v10 (C-01–C-34, denominator 26)
**Date:** 2026-03-17
**Scoring formula:** Essential 50 + Recommended 30 + Aspirational (passed/26 x 10)

---

## Baseline Context

All R12 variations are built on the R11 V-05 template — the only variation to achieve 90/90 under v10. Each R12 variation adds incremental structural enforcement *on top of* R11 V-05 without removing or changing any existing elements. The scoring question is therefore: do any additions break existing criteria, and do the additions expose excellence signals beyond the current ceiling?

---

## Essential Criteria (C-01–C-05)

All five variations inherit the complete R11 V-05 structure. Assessment is identical across all:

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-01 — 5 sub-skills executed | PASS | All five phases (trace-state, trace-permissions, trace-contract, flow-lifecycle, flow-trigger) present with tables and EXIT CRITERIA |
| C-02 — Blast radius ranked | PASS | CONSOLIDATE uses ranked findings, tiebreaker protocol stated |
| C-03 — Spec gaps identified/cleared | PASS | Spec gaps section in CONSOLIDATE template |
| C-04 — Contract violations surfaced/cleared | PASS | Contract violations section with producer/consumer fields |
| C-05 — Lifecycle violations surfaced/cleared | PASS | Exception path column in flow-lifecycle table; flow-lifecycle EXIT CRITERIA evaluates all phases |

**Essential score: 50/50 — all variations**

---

## Recommended Criteria (C-06–C-08)

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-06 — Blast radius label per finding | PASS | Field 3 template: `[wide | medium | narrow] — propagation chain:` |
| C-07 — Confirmation status per finding | PASS | Field 6 template: `[CONFIRMED -- evidence: ... | RUNTIME ANOMALY | isolated]` |
| C-08 — Sub-skill attribution per finding | PASS | Field 2 template: `Source phase: [phase name]` |

**Recommended score: 30/30 — all variations**

---

## Aspirational Criteria (C-09–C-34)

All R12 variations inherit R11 V-05's 26/26 aspirational baseline. The analysis below confirms each inherited criterion survives the R12 additions intact, then identifies where new patterns sit relative to the current criteria ceiling.

### C-09 through C-26 — Inherited from R11 V-05

These criteria are satisfied identically by all five variations. No R12 addition affects them.

| Range | Status | Note |
|-------|--------|------|
| C-09 F-NN sequential IDs | PASS all | Atomic block `Finding [N]` in CONSOLIDATE |
| C-10 Lifecycle phase tag | PASS all | Phase tag column in flow-lifecycle and flow-trigger tables |
| C-11 Compound findings tracked | PASS all | Q3 and exit status tracking in CONSOLIDATE |
| C-12 Spec gap missing-clause citation | PASS all | Spec gaps format requires missing-clause citation |
| C-13 Contract violations name both parties | PASS all | Contract violations section format requires producer and consumer |
| C-14 Privilege escalation paths | PASS all | Privilege escalation paths section in CONSOLIDATE |
| C-15 Severity with defined scale | PASS all | Field 4 template + DEFINITIONS scale |
| C-16 Top-3 surfaced | PASS all | EXECUTIVE SUMMARY section present |
| C-17 Evidence basis per CONFIRMED | PASS all | Field 6 inline citation required |
| C-18 Q1–Qn calibration (n >= 3) | PASS all | Q1–Q7 present (n=7) |
| C-19 Atomic 7-field finding block | PASS all | Fields 1–7 explicitly labeled in CONSOLIDATE template |
| C-20 Tiebreaker protocol stated | PASS all | Tiebreaker stated in CONSOLIDATE header, "state whether ties" |
| C-21 SYSTEMIC enumerates phases | PASS all | Required format: "SYSTEMIC: yes — phases: [list]" |
| C-22 State-anchor first | PASS all | Phase 1 header with `[ANCHOR: state topology pre-classifies...]` |
| C-23 Permissions-anchor before flow | PASS all | Phase 2 header with `[ANCHOR: privilege boundary...]`, before Phases 3–5 |
| C-24 Anchor tags on headers | PASS all | `[ANCHOR:...]` inline in Ph1 and Ph2 headers |
| C-25 Q6 sequence integrity gate | PASS all | Q6 validates Ph1/Ph2 execution order and pre-classification guarantee |
| C-26 Propagation chain in field 3 | PASS all | Field 3 requires chain; VERDICT restates chain; DEFINITIONS establish format; Q1 traces to terminus |

### C-27 through C-34 — The v10 Aspirational Ceiling

These are the eight criteria added in v8–v10, all introduced from R10/R11 excellence signals.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-27 Chain Terminus Registry in Phase 0 | PASS | PASS | PASS | PASS | PASS |
| C-28 Dedicated EXECUTIVE SUMMARY heading | PASS | PASS | PASS | PASS | PASS |
| C-29 Inline CONFIRMED evidence citation in field 6 | PASS | PASS | PASS | PASS | PASS |
| C-30 EXECUTIVE SUMMARY chains reference T-NN codes | PASS | PASS | PASS | PASS | PASS |
| C-31 EXECUTIVE SUMMARY bullets carry inline citations | PASS | PASS | PASS | PASS | PASS |
| C-32 VALIDITY RULES rejection gate at write time | PASS | PASS | PASS | PASS | PASS |
| C-33 Q7 post-write output-boundary gate | PASS | PASS | PASS | PASS | PASS |
| C-34 Q2 extended to preview EXECUTIVE SUMMARY compliance | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- **C-27:** All five variations retain the T-NN registry table in Phase 0 unchanged. PASS.
- **C-28:** All five retain the `## EXECUTIVE SUMMARY` section with exactly 3 structured bullets. PASS.
- **C-29:** Field 6 template `CONFIRMED -- evidence: [source-phase]: [matching-finding-name]` unchanged. PASS.
- **C-30:** VALIDITY RULES rule 1 present in all variations: "A bullet with a free-form terminus is INVALID." PASS.
- **C-31:** VALIDITY RULES rule 2 present in all variations: "Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets." PASS.
- **C-32:** VALIDITY RULES co-located with EXECUTIVE SUMMARY template, explicit INVALID prohibition language present. PASS.
- **C-33:** `## Q7 — EXECUTIVE SUMMARY structural audit` section present in all variations with per-bullet status output. PASS.
- **C-34:** Q2 extended in all variations: "Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm that the same inline citation format will be used in the summary bullet..." PASS.

**Aspirational count: 26/26 — all variations**
**Aspirational score: (26/26) x 10 = 10 — all variations**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|-------------|-----------|
| V-01 | 50 | 30 | 10 | **90** |
| V-02 | 50 | 30 | 10 | **90** |
| V-03 | 50 | 30 | 10 | **90** |
| V-04 | 50 | 30 | 10 | **90** |
| V-05 | 50 | 30 | 10 | **90** |

**All five variations score 90/90 under v10.** This is the expected result: R12 targets structural territory beyond the current ceiling. The v10 rubric has no criteria for registry-lock, per-phase exit gates, or Q8 CONSOLIDATE audit — these are proposed v11 candidates. All variations preserve the full R11 V-05 base without degradation.

---

## Ranking

All variations tie at 90. For ordering within the tie, applying the structural quality gradient:

| Rank | Variation | Enforcement layers added | Why |
|------|-----------|--------------------------|-----|
| 1 | **V-05** | Registry-lock + per-phase exit gates + Q8 CONSOLIDATE gate | Full three-layer enforcement for CONSOLIDATE pipeline — mirrors R11 V-05's architecture for EXECUTIVE SUMMARY exactly |
| 2 | **V-04** | Registry-lock + per-phase exit gates | Two-layer upstream enforcement; covers declaration-time and per-phase production-time gaps; missing the post-write gate |
| 3 | **V-03** | Q8 CONSOLIDATE gate only | Post-write audit adds a new structural layer not present in v10; no upstream prevention |
| 4 | **V-01** | Per-phase exit gates only | Catches drift at each phase exit before propagation; registry can still grow silently |
| 5 | **V-02** | Registry-lock only | Immutable registry authority established; no per-phase chain verification or post-write gate |

---

## Excellence Signals — V-05 R12

V-05 is the apex variation. Its structural advances above the current v10 ceiling constitute the excellence signals for v11 criterion candidates:

### Signal 1 — Registry-lock declaration in Phase 0 (candidate C-35)

V-05 closes Phase 0 with an explicit lock statement:

> *"Registry lock: The terminus registry is now complete. No terminus component may be added, removed, or renamed after this point... State: 'Registry locked: [N] terminus entries. Phase execution may begin.'"*

Pattern: **declaration-time integrity gate for the terminus registry.** C-27 requires the registry to exist; C-35 would require it to be explicitly immutable. Without the lock, a model executing Phases 1–5 can silently introduce new terminus components without triggering a structural failure. The lock converts Phase 0 from a reference table into an authority contract.

Enforcement analogy: C-32 is the write-time rejection gate for EXECUTIVE SUMMARY format violations. C-35 is the declaration-time lock for the registry that all chains depend on. Both are pre-production gates — one at the section write site, one at the registry creation site.

### Signal 2 — Per-phase T-NN exit gate in EXIT CRITERIA (candidate C-36)

V-05 appends to each phase's EXIT CRITERIA:

> *"T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries. State: '[N] chains produced, [N] resolved to T-NN, [N] registry miss.' If any registry miss: flag 'unresolved chain — registry miss: [component name]' and carry forward to Q1."*

This appears in all five phases (Phases 1–5), producing an auditable chain-resolution status at each phase boundary. Pattern: **per-phase production-time integrity checkpoint.** Q1 catches unresolved chains post-hoc (after all phases complete); the per-phase gate catches them at source, before they propagate to CONSOLIDATE or EXECUTIVE SUMMARY.

New pattern type: no current criterion enforces at phase-exit granularity. C-36 would be the first criterion that fires during execution (at each phase boundary) rather than pre-execution (Phase 0) or post-output (Q7/Q8).

### Signal 3 — Q8 CONSOLIDATE completeness gate (candidate C-37)

V-05 inserts a new Q8 gate between CONSOLIDATE and VERDICT:

> *"Before writing VERDICT, audit every finding block written in CONSOLIDATE. For each finding block [N]: 7-field check... T-NN chain check... Classification format check... State the result for each block: 'Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS'"*

Q8 audits three dimensions: 7-field completeness (structural completeness), T-NN chain resolution (the same chain integrity that Q7 checks in EXECUTIVE SUMMARY bullets), and classification format (the same inline citation requirement that Q7 checks in EXECUTIVE SUMMARY bullets). Pattern: **post-write structural audit for CONSOLIDATE finding blocks**, exactly analogous to Q7's role for EXECUTIVE SUMMARY bullets.

The gap Q8 closes: Q1–Q6 validate inputs and calibration *before* CONSOLIDATE is written. Q8 is the only gate that fires *after* CONSOLIDATE is written. Without Q8, a model that writes structurally deficient finding blocks (missing fields, free-form chains, bare CONFIRMED tokens) faces no structural challenge before VERDICT.

### Signal 4 — Symmetric three-layer architecture for CONSOLIDATE pipeline

V-05 R12's three-layer architecture mirrors R11 V-05's three-layer architecture for EXECUTIVE SUMMARY exactly:

| Layer | EXECUTIVE SUMMARY (R11 V-05 / v10) | CONSOLIDATE (R12 V-05 / candidate v11) |
|-------|--------------------------------------|----------------------------------------|
| Pre-production gate | C-32: VALIDITY RULES at write site | C-35: Registry-lock in Phase 0 |
| Production-time gate | C-34: Q2 previews before writing | C-36: Per-phase exit gates during execution |
| Post-write gate | C-33: Q7 audits after EXECUTIVE SUMMARY | C-37: Q8 audits after CONSOLIDATE |

The structural symmetry is the signal: the same failure modes (format drift, terminus mismatch, citation omission) occur in both output sections; the same three-layer architecture addresses both. V-05 R12 completes the pattern by applying R11 V-05's design to the CONSOLIDATE pipeline.

### Signal 5 — Q8's three-dimension audit exceeds Q7's two-dimension scope

Q7 (C-33) checks two dimensions per bullet: C-30 terminus format and C-31 citation format. Q8 checks three dimensions per block: 7-field completeness (no Q7 equivalent), T-NN chain format, and classification format. The additional dimension — structural completeness of all seven fields — addresses a failure mode that EXECUTIVE SUMMARY bullets cannot exhibit (bullets have no equivalent of fields 1, 4, 5, and 7). This is not a deficiency of Q7; it reflects the structural difference between a three-bullet summary and a seven-field atomic block. C-37 would be Q8's standalone criterion, scoped specifically to CONSOLIDATE finding block completeness.

---

## Summary Table

| Variation | Score | New enforcement added above v10 ceiling |
|-----------|-------|-----------------------------------------|
| V-01 | **90** | Per-phase T-NN exit gates (Phases 1–5 EXIT CRITERIA) |
| V-02 | **90** | Registry-lock declaration at Phase 0 close |
| V-03 | **90** | Q8 CONSOLIDATE completeness gate (post-write, before VERDICT) |
| V-04 | **90** | V-01 + V-02 (registry-lock + per-phase exit gates) |
| V-05 | **90** | V-04 + V-03 (full three-layer CONSOLIDATE enforcement) |

All five variations achieve the v10 ceiling. V-05 is the top-ranked variation by structural completeness. Three candidate v11 criteria are well-supported by V-05's design: **C-35** (registry-lock), **C-36** (per-phase exit gates), **C-37** (Q8 CONSOLIDATE gate).

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Registry-lock declaration in Phase 0 makes terminus registry immutable before any phase executes — prevents silent terminus additions that undermine chain authority", "Per-phase T-NN exit gates in EXIT CRITERIA catch chain drift at source before propagation to CONSOLIDATE or EXECUTIVE SUMMARY", "Q8 CONSOLIDATE completeness gate fires after CONSOLIDATE and before VERDICT, auditing 7-field completeness + T-NN chain + classification format per block — mirrors Q7 for EXECUTIVE SUMMARY", "Symmetric three-layer enforcement for CONSOLIDATE pipeline (registry-lock + per-phase gates + Q8) mirrors the C-32/C-34/C-33 architecture introduced for EXECUTIVE SUMMARY in R11 V-05"]}
```
