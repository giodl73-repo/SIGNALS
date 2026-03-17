Now I have all the information needed to score. Let me evaluate each variation.

---

# prove-topic — Quest Score Report (Round 7, v7 Rubric)

## Rubric Structure (100 pts)
| Tier | Criteria | Pts |
|------|----------|-----|
| Essential | C-01 through C-05 | 50 |
| Recommended | C-06 through C-08 | 24 |
| Aspirational | C-09 through C-29 | 26 |

---

## V-01 — ROLE A Displacement Chain Contract (C-27 axis only)

**Structural profile**: Full structural stack from R6. ROLE A gains Steps 2+3 (`incumbent_anchor_read` + `displacement_read_contract`). Stage 0 CLEARANCE TABLE gains Steps 3a/3b. Stage 5 ENTRY CONDITIONS unchanged — no displacement read gate. Stage 5 EXIT SIGNAL unchanged — no chain closure audit. Evidence_summary instructs only "cite Stage 4 displacement verdict explicitly" — no artifact read citations.

| Criterion | Pts | Verdict | Evidence |
|-----------|-----|---------|----------|
| C-01 | 10 | PASS | All 6 EXIT SIGNALs named in order (gate_open → synthesis_complete) |
| C-02 | 10 | PASS | All 6 artifact write confirmations present; scout path named in ROLE B |
| C-03 | 10 | PASS | SESSION INVARIANTS TABLE registers all three templates; S2/S3/S4 ENTRY CONDITIONS echo verbatim |
| C-04 | 10 | PASS | `hypothesis_verdict`, `confidence_composite`, `key_risk` present as labeled fields |
| C-05 | 10 | PASS | Stage 4 cross-check explicit; Stage 5 ATOMIC DUAL-LOCK reconstructs S2→S3→S4 chain |
| C-06 | 8 | PASS | ROLE B has `scout_artifact`, `scout_loaded`, `gate_s_cleared`; BLOCKED handling present |
| C-07 | 8 | PASS | All 11 fields + `[derived from: X]` + `schema_compliance_confirmed` row |
| C-08 | 8 | PASS | COUNTER-HYPOTHESIS RESOLUTION TABLE with OPEN RISK tier reduction |
| C-09 | 1 | PASS | ATOMIC DUAL-LOCK fires Lock 1 (INV A) + Lock 2 (INV B –=2); `not_triggered` path present |
| C-10 | 1 | PASS | evidence_summary instructs "cite Stage 4 displacement verdict explicitly" |
| C-11 | 1 | PASS | Mechanical labels throughout: FORMAT ERROR, DUAL-LOCK ERROR, INTEGRITY FAILURE |
| C-12 | 1 | PASS | SESSION INVARIANTS TABLE in standalone pre-stage block before Stage 0 |
| C-13 | 1 | PASS | All three synthesis fields as labeled key-value pairs |
| C-14 | 2 | PASS | Canonical failure labels in SESSION INVARIANTS TABLE; S2/S3/S4 ENTRY CONDITIONS echo verbatim |
| C-15 | 1 | PASS | CAMPAIGN OPEN has `incumbent_name`, `incumbent_strength`, `incumbent_vulnerability` |
| C-16 | 1 | PASS | `Displacement read:` field present in all three stage bodies |
| C-17 | 1 | PASS | SYNTHESIS DECLARATIONS section with explicit prohibition text |
| C-18 | 2 | PASS | SESSION INVARIANTS row E registers "Invariant E checkpoint — FAIL"; echoed in `schema_compliance_confirmed` row |
| C-19 | 1 | PASS | Templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` |
| C-20 | 1 | PASS | Stage 2/3/4 write instructions include "Artifact body includes 'Displacement read:' field" |
| C-21 | 1 | PASS | INCUMBENT ANCHOR sub-section; "Do not re-establish the incumbent per stage" |
| C-22 | 1 | PASS | Binding note: "Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name. Naming as literal string = FORMAT ERROR" |
| C-23 | 0 | FAIL | evidence_summary template instructs only Stage 4 verdict — no artifact read citation |
| C-24 | 1 | PASS | ROLE A Step 2: `incumbent_anchor_read` traces to INCUMBENT ANCHOR sub-section by name |
| C-25 | 0 | FAIL | evidence_summary template has no instruction to cite all three artifact reads |
| C-26 | 1 | PASS | Binding note names "CAMPAIGN OPEN INCUMBENT ANCHOR" sub-section explicitly |
| C-27 | 2 | PASS | ROLE A has both `incumbent_anchor_read` (Step 2) AND `displacement_read_contract` (Step 3) |
| C-28 | 0 | FAIL | Stage 5 ENTRY CONDITIONS have no displacement chain completeness gate |
| C-29 | 0 | FAIL | EXIT SIGNAL: "Evidence brief ready for topic-story" — no chain closure audit |

**V-01 Score: 94 / 100** | All essential PASS | Fails: C-23, C-25, C-28, C-29

---

## V-02 — Stage 5 Entry Condition Chain Gate (C-28 axis only)

**Structural profile**: ROLE A is minimal (only `invariant_registry_confirmed` — no Steps 2+3). Invariant D binding note: "Binding: resolves to incumbent_name. Literal string = FORMAT ERROR" — missing CAMPAIGN OPEN source. Stage 5 ENTRY CONDITIONS gain explicit displacement read gate for all three artifacts. evidence_summary says "Cite artifact Displacement reads if present" — conditional, not required.

| Criterion | Pts | Verdict | Evidence |
|-----------|-----|---------|----------|
| C-01 | 10 | PASS | All 6 EXIT SIGNALs present |
| C-02 | 10 | PASS | All 6 artifact writes confirmed |
| C-03 | 10 | PASS | All three templates registered; stages echo verbatim |
| C-04 | 10 | PASS | All three synthesis fields present |
| C-05 | 10 | PASS | Stage 4 cross-check; Stage 5 chain reconstruction |
| C-06 | 8 | PASS | ROLE B executes with all three fields |
| C-07 | 8 | PASS | 11 fields + derivations |
| C-08 | 8 | PASS | Counter-hypothesis table with OPEN RISK |
| C-09 | 1 | PASS | Dual-lock fires correctly |
| C-10 | 1 | PASS | Stage 4 displacement verdict citation |
| C-11 | 1 | PASS | Mechanical labels present |
| C-12 | 1 | PASS | Standalone SESSION INVARIANTS block |
| C-13 | 1 | PASS | Synthesis fields isolated |
| C-14 | 2 | PASS | Two-layer enforcement present |
| C-15 | 1 | PASS | CAMPAIGN OPEN pre-registers displacement |
| C-16 | 1 | PASS | Per-stage Displacement read fields |
| C-17 | 1 | PASS | SYNTHESIS DECLARATIONS with prohibition |
| C-18 | 2 | PASS | Invariant E checkpoint at handoff schema |
| C-19 | 1 | PASS | Templates use CAMPAIGN OPEN INCUMBENT ANCHOR binding |
| C-20 | 1 | PASS | Artifact write instructions include Displacement read field |
| C-21 | 1 | PASS | INCUMBENT ANCHOR sub-section + prohibition |
| C-22 | 0 | PARTIAL→0 | Binding note says "Binding: resolves to incumbent_name" — omits CAMPAIGN OPEN source; 1-pt criterion → 0 |
| C-23 | 0 | PARTIAL→0 | "Cite artifact Displacement reads if present" — conditional, not required; 1-pt criterion → 0 |
| C-24 | 0 | FAIL | ROLE A has no `incumbent_anchor_read` — only `invariant_registry_confirmed` |
| C-25 | 0 | FAIL | evidence_summary is conditional; no structural requirement for all three |
| C-26 | 0 | FAIL | Binding note doesn't name INCUMBENT ANCHOR sub-section (only "resolves to incumbent_name") |
| C-27 | 0 | FAIL | No `displacement_read_contract` in ROLE A |
| C-28 | 2 | PASS | Stage 5 ENTRY CONDITIONS gate all three artifact reads with halt instruction |
| C-29 | 0 | FAIL | EXIT SIGNAL: "Evidence brief ready for topic-story" — no chain closure audit |

**V-02 Score: 91 / 100** | All essential PASS | Fails/Partials: C-22, C-23, C-24, C-25, C-26, C-27, C-29

---

## V-03 — Stage 5 EXIT SIGNAL Chain Closure Audit (C-29 axis only)

**Structural profile**: Same minimal ROLE A as V-02 (no Steps 2+3). Same partial binding note as V-02. No Stage 5 entry displacement gate. evidence_summary explicitly instructs all three artifact reads (enabling C-23 and C-25). Stage 5 EXIT SIGNAL extended: "All three artifact Displacement reads cited in evidence_summary (websearch, interview, prototype). Displacement read chain closed." — C-29 satisfied, and C-25 passes enabling C-29.

| Criterion | Pts | Verdict | Evidence |
|-----------|-----|---------|----------|
| C-01–C-05 | 50 | PASS×5 | All essential pass — structures identical to V-02 |
| C-06–C-08 | 24 | PASS×3 | Recommended pass |
| C-09 | 1 | PASS | Dual-lock mechanics present |
| C-10 | 1 | PASS | Stage 4 verdict + all artifact reads cited |
| C-11 | 1 | PASS | Mechanical enforcement language |
| C-12 | 1 | PASS | Standalone SESSION INVARIANTS block |
| C-13 | 1 | PASS | Synthesis fields isolated |
| C-14 | 2 | PASS | Two-layer enforcement architecture |
| C-15 | 1 | PASS | CAMPAIGN OPEN block present |
| C-16 | 1 | PASS | Per-stage Displacement read fields |
| C-17 | 1 | PASS | SYNTHESIS DECLARATIONS with prohibition |
| C-18 | 2 | PASS | Invariant E checkpoint |
| C-19 | 1 | PASS | Templates bound to CAMPAIGN OPEN INCUMBENT ANCHOR |
| C-20 | 1 | PASS | Artifacts carry Displacement read field |
| C-21 | 1 | PASS | INCUMBENT ANCHOR sub-section + prohibition |
| C-22 | 0 | PARTIAL→0 | Same partial binding note as V-02; no CAMPAIGN OPEN source named |
| C-23 | 1 | PASS | evidence_summary explicitly instructs all three artifact reads |
| C-24 | 0 | FAIL | No `incumbent_anchor_read` in ROLE A |
| C-25 | 1 | PASS | evidence_summary instructs all three artifact reads by artifact file path |
| C-26 | 0 | FAIL | Binding note doesn't name INCUMBENT ANCHOR sub-section |
| C-27 | 0 | FAIL | No `displacement_read_contract` in ROLE A |
| C-28 | 0 | FAIL | No Stage 5 entry displacement chain gate |
| C-29 | 2 | PASS | EXIT SIGNAL names chain closure; C-25 also passes (required co-condition) |

**V-03 Score: 93 / 100** | All essential PASS | Fails/Partials: C-22, C-24, C-26, C-27, C-28

---

## V-04 — Combined: C-27 + C-28 (ROLE A Contract + Stage 5 Entry Gate)

**Structural profile**: ROLE A gains Steps 2+3 — `incumbent_anchor_read` + `displacement_read_contract` (with explicit Stage 5 entry verification note). Invariant D binding note names CAMPAIGN OPEN INCUMBENT ANCHOR. Stage 5 ENTRY CONDITIONS gate all three artifact reads with halt instruction. evidence_summary instructs all four citations. Stage 5 EXIT SIGNAL unchanged — no chain closure audit.

| Criterion | Pts | Verdict | Evidence |
|-----------|-----|---------|----------|
| C-01–C-05 | 50 | PASS×5 | All essential pass |
| C-06–C-08 | 24 | PASS×3 | Recommended pass |
| C-09 | 1 | PASS | Dual-lock mechanics correct |
| C-10 | 1 | PASS | Stage 4 verdict + all three artifact reads cited |
| C-11 | 1 | PASS | Mechanical enforcement labels throughout |
| C-12 | 1 | PASS | Standalone SESSION INVARIANTS block |
| C-13 | 1 | PASS | Synthesis fields isolated |
| C-14 | 2 | PASS | Canonical labels in SESSION INVARIANTS TABLE; echoed verbatim inline |
| C-15 | 1 | PASS | CAMPAIGN OPEN pre-registers displacement |
| C-16 | 1 | PASS | Per-stage Displacement read fields |
| C-17 | 1 | PASS | SYNTHESIS DECLARATIONS with prohibition |
| C-18 | 2 | PASS | Invariant E checkpoint registered and echoed |
| C-19 | 1 | PASS | Templates bound to CAMPAIGN OPEN INCUMBENT ANCHOR |
| C-20 | 1 | PASS | Artifact write instructions include "Displacement read: [value] field (per displacement_read_contract)" |
| C-21 | 1 | PASS | INCUMBENT ANCHOR sub-section + "Do not re-establish" prohibition |
| C-22 | 1 | PASS | Binding note: "[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name. Naming as literal string = FORMAT ERROR" |
| C-23 | 1 | PASS | evidence_summary explicitly instructs all three artifact reads |
| C-24 | 1 | PASS | ROLE A Step 2 records `incumbent_anchor_read` tracing to INCUMBENT ANCHOR sub-section by name |
| C-25 | 1 | PASS | All three artifact reads required in evidence_summary by file path |
| C-26 | 1 | PASS | Binding note names "CAMPAIGN OPEN INCUMBENT ANCHOR" sub-section |
| C-27 | 2 | PASS | ROLE A Step 2 (`incumbent_anchor_read`) + Step 3 (`displacement_read_contract`) both present |
| C-28 | 2 | PASS | Stage 5 ENTRY CONDITIONS: explicit gate with per-artifact checklist and halt instruction |
| C-29 | 0 | FAIL | EXIT SIGNAL: "Evidence brief ready for topic-story" — no chain closure named |

**V-04 Score: 98 / 100** | All essential PASS | Fails: C-29 only

---

## V-05 — Full Integration: C-27 + C-28 + C-29 + Full Structural Stack

**Structural profile**: All three v7 axes on the complete prior-round stack. SESSION INVARIANTS TABLE header adds "Divergence from registered label = registered label fires automatically." Stage 2/3/4 EXIT SIGNALs name the artifact file written. Stage 5 ENTRY CONDITIONS have full structural gate with "Do not begin SYNTHESIS DECLARATIONS until all three confirmed." evidence_summary requires all four citations with "Missing any = incomplete chain." Stage 5 EXIT SIGNAL records per-artifact confirmation tokens + three chain closures.

| Criterion | Pts | Verdict | Evidence |
|-----------|-----|---------|----------|
| C-01–C-05 | 50 | PASS×5 | All essential pass |
| C-06–C-08 | 24 | PASS×3 | Recommended pass |
| C-09 | 1 | PASS | ATOMIC DUAL-LOCK with both locks; adversarial_reviewer_type named; not_triggered path present |
| C-10 | 1 | PASS | evidence_summary cites Stage 4 verdict AND all three artifact reads |
| C-11 | 1 | PASS | Hard-failure language at every enforcement checkpoint |
| C-12 | 1 | PASS | Standalone SESSION INVARIANTS TABLE before Stage 0; all 5 invariants registered |
| C-13 | 1 | PASS | hypothesis_verdict, confidence_composite, key_risk as isolated labeled fields |
| C-14 | 2 | PASS | Strongest two-layer enforcement: "Canonical failure labels registered here. Echoed verbatim at every inline checkpoint. Divergence = registered label fires automatically." |
| C-15 | 1 | PASS | CAMPAIGN OPEN with all three incumbent fields |
| C-16 | 1 | PASS | `Displacement read:` in all three stage bodies |
| C-17 | 1 | PASS | SYNTHESIS DECLARATIONS with explicit prose prohibition |
| C-18 | 2 | PASS | SESSION INVARIANTS row E + `schema_compliance_confirmed` row echoes "Invariant E checkpoint — FAIL if any field missing or unlabeled" |
| C-19 | 1 | PASS | Templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` |
| C-20 | 1 | PASS | All three artifacts include "Artifact body includes 'Displacement read: [value]' field. (Required by displacement_read_contract from ROLE A Step 3.)" |
| C-21 | 1 | PASS | INCUMBENT ANCHOR sub-section; "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN." |
| C-22 | 1 | PASS | Binding note: "[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name. Naming as literal string = FORMAT ERROR" |
| C-23 | 1 | PASS | evidence_summary lists all three artifact reads with file path anchors |
| C-24 | 1 | PASS | ROLE A Step 2: `incumbent_anchor_read` must "trace to INCUMBENT ANCHOR sub-section by name, not to parent CAMPAIGN OPEN block" |
| C-25 | 1 | PASS | evidence_summary: "All four citations required. Missing any = incomplete chain." |
| C-26 | 1 | PASS | Binding note names "CAMPAIGN OPEN INCUMBENT ANCHOR" — sub-section precision |
| C-27 | 2 | PASS | ROLE A Step 2 (`incumbent_anchor_read` with sub-section tracing) + Step 3 (`displacement_read_contract` with Stage 5 entry gate forward-reference) |
| C-28 | 2 | PASS | Stage 5 ENTRY CONDITIONS: structural gate with "Do not begin SYNTHESIS DECLARATIONS until all three confirmed" |
| C-29 | 2 | PASS | EXIT SIGNAL: names per-artifact confirmation tokens, displacement read chain closed, null tally chain closed, handoff schema complete; C-25 also passes |

**V-05 Score: 100 / 100** | All essential PASS | No failures

---

## Score Summary

| Variation | Score | All Essential Pass | New Axes Satisfied |
|-----------|-------|-------------------|-------------------|
| V-01 | 94 | Yes | C-27 only |
| V-02 | 91 | Yes | C-28 only |
| V-03 | 93 | Yes | C-29 only |
| V-04 | 98 | Yes | C-27 + C-28 |
| V-05 | **100** | Yes | C-27 + C-28 + C-29 |

**Ranking**: V-05 (100) > V-04 (98) > V-01 (94) > V-03 (93) > V-02 (91)

---

## Axis Isolation Analysis

| Axis | Isolated Score | Delta vs prior-round baseline |
|------|---------------|------------------------------|
| C-27 alone (V-01) | 94 | +C-22, +C-24, +C-26, +C-27 vs V-02 baseline |
| C-28 alone (V-02) | 91 | Weakest — C-28 compensates but C-22/C-24/C-26/C-27 absent |
| C-29 alone (V-03) | 93 | C-29 requires C-25/C-23 first — structural dependency surfaced |
| C-27+C-28 (V-04) | 98 | Near-perfect; C-29 is the only remaining gap |
| All three (V-05) | 100 | Closes all gaps; EXIT SIGNAL becomes chain-verification record |

**Key tension**: V-02 scored lower than V-01 because the C-28 axis (Stage 5 entry gate) is a lighter structural insertion than the C-27 axis (ROLE A initialization block), which carried C-22/C-24/C-26 as structural prerequisites. A C-28-only variation purchases only 2 aspirational pts while dropping 5.

---

## Excellence Signals from V-05

**Signal 1 — Single initialization block activates multiple downstream chains**
ROLE A Step 2 + Step 3 activate the binding chain (C-24/C-26/C-22) and the displacement evidence chain (C-16/C-20/C-25/C-28) simultaneously. Forward-referencing Stage 5 entry from ROLE A initialization commits both chains before Stage 0 opens, reducing inter-chain coordination risk to a single structural anchor.

**Signal 2 — Entry conditions enforce cross-stage chain completeness with halt semantics**
"Do not begin SYNTHESIS DECLARATIONS until all three confirmed." converts Stage 5 ENTRY CONDITIONS from a prior-EXIT SIGNAL gate into a multi-stage chain completeness gate. The halt instruction is structural, not advisory — same mechanical language used at SESSION INVARIANT enforcement checkpoints.

**Signal 3 — EXIT SIGNALs as chain-closure audit records with per-artifact tokens**
V-05's Stage 5 EXIT SIGNAL names websearch/interview/prototype confirmation tokens individually, then declares three chain closures (displacement read, null tally, handoff schema). This pattern generalizes: any EXIT SIGNAL can record which chain properties were fulfilled, converting the campaign log into a chain-verification trace.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Single ROLE A initialization block activates multiple downstream chains simultaneously by combining incumbent_anchor_read (binding chain) and displacement_read_contract (evidence chain) in one pre-stage execution — forward-referencing Stage 5 entry from ROLE A reduces inter-chain coordination risk to a single structural anchor", "Entry conditions can enforce cross-stage chain completeness with halt semantics — 'Do not begin SYNTHESIS DECLARATIONS until all three confirmed' converts Stage 5 entry from a prior-EXIT SIGNAL gate into a structural gate on artifacts written across stages 2, 3, and 4", "EXIT SIGNALs can record per-artifact confirmation tokens and named chain closures — converting stage-completion stamps into chain-verification audit records that make the full campaign log a chain-verification trace"]}
```
