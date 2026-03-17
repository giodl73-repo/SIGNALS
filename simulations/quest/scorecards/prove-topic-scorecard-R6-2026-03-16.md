## Quest Score — prove-topic R6

---

### Scoring Reference

**Essential** (50 pts): C-01 through C-05 × 10 each
**Recommended** (24 pts): C-06 through C-08 × 8 each
**Aspirational** (26 pts): C-09 through C-26 per rubric

PASS = full pts | PARTIAL = half (rounded down) | FAIL = 0

---

## V-01 — ROLE A Binding Confirmation (C-24 single axis)

**What it adds over baseline**: ROLE A Step 1 reads CAMPAIGN OPEN INCUMBENT ANCHOR, records `incumbent_anchor_read`, Step 2 confirms binding note match before Stage 0. Also adds C-22 floor (binding note + failure label), but binding note references "CAMPAIGN OPEN" (parent block), not the sub-section. No Displacement read fields. No "Do not re-establish" prohibition in INCUMBENT ANCHOR.

| ID | Pts | Score | Evidence note |
|----|-----|-------|---------------|
| C-01 | 10 | PASS 10 | All 6 EXIT SIGNALs present in order |
| C-02 | 10 | PASS 10 | All 6 artifacts written + confirmed |
| C-03 | 10 | PASS 10 | Invariant D templates registered + echoed at S2/S3/S4 entry conditions verbatim |
| C-04 | 10 | PASS 10 | hypothesis_verdict, confidence_composite, key_risk all present in SYNTHESIS BODY |
| C-05 | 10 | PASS 10 | Stage 4 cross-check + Stage 5 null tally chain reconstruction both present |
| C-06 | 8 | PASS 8 | ROLE B execution with scout_artifact + gate_s_cleared fields |
| C-07 | 8 | PASS 8 | All 11 fields + schema_compliance_confirmed with [derived from: X] on every row |
| C-08 | 8 | PASS 8 | COUNTER-HYPOTHESIS RESOLUTION TABLE with verdict + citation present |
| C-09 | 1 | PASS 1 | Invariant A registered, ATOMIC DUAL-LOCK with both locks + not_triggered else branch |
| C-10 | 1 | PASS 1 | evidence_summary requires explicit incumbent displacement verdict from Stage 4 |
| C-11 | 1 | PASS 1 | FORMAT ERROR (Inv D), integrity failure (null tally rule), format error (Inv C) all mechanical |
| C-12 | 1 | PASS 1 | SESSION INVARIANTS TABLE in standalone block before Stage 0 with all four rows |
| C-13 | 2 | PASS 2 | hypothesis_verdict, confidence_composite, key_risk as labeled key-value fields in SYNTHESIS BODY |
| C-14 | 2 | PARTIAL 1 | FORMAT ERROR bidirectional for Inv D; format error for Inv C derivation — no DUAL-LOCK ERROR or INTEGRITY FAILURE canonically registered in SESSION INVARIANTS TABLE |
| C-15 | 1 | PASS 1 | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section with incumbent_name + incumbent_strength |
| C-16 | 1 | FAIL 0 | No "Displacement read:" field in Stages 2, 3, 4 |
| C-17 | 2 | FAIL 0 | No SYNTHESIS DECLARATIONS section; no explicit prohibition text |
| C-18 | 2 | FAIL 0 | No Invariant E registered in SESSION INVARIANTS TABLE; schema_compliance_confirmed row present but no canonical label echoed |
| C-19 | 1 | FAIL 0 | Invariant D templates use `{status_quo_comparator}` literal, not `[incumbent from CAMPAIGN OPEN]` bound reference |
| C-20 | 2 | FAIL 0 | No Displacement read field in artifact content for any of the three evidence artifacts |
| C-21 | 1 | FAIL 0 | INCUMBENT ANCHOR sub-section present but no "Do not re-establish per stage" prohibition text |
| C-22 | 1 | PASS 1 | Binding note present: "[incumbent from CAMPAIGN OPEN] resolves to incumbent_name. Naming as literal string = FORMAT ERROR" — has note + failure label |
| C-23 | 1 | FAIL 0 | evidence_summary requires Stage 4 displacement verdict but no artifact Displacement read citation |
| C-24 | 2 | PASS 2 | ROLE A Step 1: reads CAMPAIGN OPEN INCUMBENT ANCHOR sub-section, records incumbent_anchor_read, confirms Invariant D binding active before Stage 0 gate_open |
| C-25 | 2 | FAIL 0 | No artifact Displacement reads to cite |
| C-26 | 2 | FAIL 0 | Binding note names "CAMPAIGN OPEN" (parent block), not "CAMPAIGN OPEN INCUMBENT ANCHOR" sub-section |

**V-01 composite: 85 / 100** | All essential: PASS | Golden: YES

---

## V-02 — Per-Artifact Displacement Read Fields (C-25 single axis)

**What it adds over baseline**: Stages 2, 3, 4 each add "Displacement read:" synthesis field explicitly noted as artifact content. Stage 5 evidence_summary must cite all three artifact values with source + value (FAIL if fewer than three). No ROLE A binding step (standard ROLE A confirmation only). No binding reference in Invariant D (still uses `{status_quo_comparator}`). No "Do not re-establish" prohibition.

| ID | Pts | Score | Evidence note |
|----|-----|-------|---------------|
| C-01 | 10 | PASS 10 | All 6 EXIT SIGNALs present |
| C-02 | 10 | PASS 10 | All 6 artifacts written + confirmed; artifact write instructions note Displacement read field in content |
| C-03 | 10 | PASS 10 | Invariant D templates registered + applied verbatim at stage entry conditions |
| C-04 | 10 | PASS 10 | All three synthesis body fields present |
| C-05 | 10 | PASS 10 | Stage 4 cross-check + Stage 5 chain reconstruction present |
| C-06 | 8 | PASS 8 | ROLE B execution with scout_artifact + gate_s_cleared |
| C-07 | 8 | PASS 8 | All 11 fields + schema_compliance_confirmed with derivation annotations |
| C-08 | 8 | PASS 8 | Counter-hypothesis resolution table with verdict + citation |
| C-09 | 1 | PASS 1 | Dual-lock properly configured |
| C-10 | 1 | PASS 1 | evidence_summary requires Stage 4 displacement verdict + all three artifact Displacement reads |
| C-11 | 1 | PASS 1 | Mechanical failure language at all three checkpoints |
| C-12 | 1 | PASS 1 | Standalone SESSION INVARIANTS TABLE before Stage 0 |
| C-13 | 2 | PASS 2 | Synthesis fields isolated as labeled key-value pairs |
| C-14 | 2 | PARTIAL 1 | Inv D + Inv C bidirectional; DUAL-LOCK ERROR / INTEGRITY FAILURE not canonically registered |
| C-15 | 1 | PASS 1 | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section present |
| C-16 | 1 | PASS 1 | Stages 2, 3, 4 each have labeled "Displacement read:" field; note confirms it must appear in artifact body |
| C-17 | 2 | FAIL 0 | No SYNTHESIS DECLARATIONS section with explicit prohibition |
| C-18 | 2 | FAIL 0 | No Invariant E in SESSION INVARIANTS TABLE |
| C-19 | 1 | FAIL 0 | Invariant D templates use `{status_quo_comparator}`, not bound reference |
| C-20 | 2 | PASS 2 | Each of the three stage artifacts explicitly includes "Displacement read:" field in artifact body per confirmation instruction |
| C-21 | 1 | FAIL 0 | INCUMBENT ANCHOR sub-section present but no "Do not re-establish" prohibition |
| C-22 | 1 | FAIL 0 | No binding resolution note in Invariant D entry |
| C-23 | 1 | PASS 1 | evidence_summary requires all three artifact reads — satisfies at-least-one floor |
| C-24 | 2 | FAIL 0 | Standard ROLE A: confirms four invariant rows but no incumbent_anchor_read step tracing to INCUMBENT ANCHOR sub-section |
| C-25 | 2 | PASS 2 | evidence_summary explicitly requires all three artifact Displacement read values; FAIL label for fewer than three |
| C-26 | 2 | FAIL 0 | No binding resolution note at all in Invariant D |

**V-02 composite: 88 / 100** | All essential: PASS | Golden: YES

---

## V-03 — Binding Note Sub-Section Precision (C-26 single axis)

**What it adds over baseline**: Invariant D templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` (bound reference). Binding note explicitly names INCUMBENT ANCHOR sub-section with failure labels for literal-string use and per-stage re-establishment. ROLE A confirms bound reference is active (not standard registry confirmation). Stage ENTRY CONDITIONS and BODY tables echo the bound reference. No ROLE A binding read / `incumbent_anchor_read`. No "Do not re-establish" prohibition in INCUMBENT ANCHOR header. No Displacement read fields.

| ID | Pts | Score | Evidence note |
|----|-----|-------|---------------|
| C-01 | 10 | PASS 10 | All 6 EXIT SIGNALs including Stage 0 EXIT naming sub-section binding |
| C-02 | 10 | PASS 10 | All 6 artifacts written |
| C-03 | 10 | PASS 10 | Bound-reference templates registered in SESSION INVARIANTS TABLE + applied verbatim at every stage entry condition |
| C-04 | 10 | PASS 10 | Synthesis verdict fields present |
| C-05 | 10 | PASS 10 | Null tally cross-check at Stage 4 close + Stage 5 reconstruction |
| C-06 | 8 | PASS 8 | ROLE B execution |
| C-07 | 8 | PASS 8 | Full handoff table with derivation annotations |
| C-08 | 8 | PASS 8 | Counter-hypothesis resolution table |
| C-09 | 1 | PASS 1 | Dual-lock present |
| C-10 | 1 | PASS 1 | Stage 4 displacement verdict required in evidence_summary |
| C-11 | 1 | PASS 1 | Mechanical failure language at enforcement checkpoints |
| C-12 | 1 | PASS 1 | Standalone SESSION INVARIANTS TABLE before Stage 0 |
| C-13 | 2 | PASS 2 | Synthesis fields isolated |
| C-14 | 2 | PARTIAL 1 | Inv D bidirectional (FORMAT ERROR + literal-string FORMAT ERROR registered + echoed); Inv C bidirectional; DUAL-LOCK ERROR not registered |
| C-15 | 1 | PASS 1 | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section with incumbent_name + strength |
| C-16 | 1 | FAIL 0 | No "Displacement read:" fields in stage bodies |
| C-17 | 2 | FAIL 0 | No SYNTHESIS DECLARATIONS section |
| C-18 | 2 | FAIL 0 | No Invariant E |
| C-19 | 1 | PASS 1 | Invariant D templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` bound reference |
| C-20 | 2 | FAIL 0 | No Displacement read fields in artifact content |
| C-21 | 1 | FAIL 0 | INCUMBENT ANCHOR sub-section present but no "Do not re-establish" prohibition |
| C-22 | 1 | PASS 1 | Binding note: "[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name in INCUMBENT ANCHOR sub-section. Naming as literal string = FORMAT ERROR." |
| C-23 | 1 | FAIL 0 | No artifact Displacement reads in evidence_summary |
| C-24 | 2 | FAIL 0 | ROLE A confirms bound reference active but no `incumbent_anchor_read` record tracing to sub-section — binding confirmation is a check, not a pre-stage read |
| C-25 | 2 | FAIL 0 | No artifact Displacement reads exist |
| C-26 | 2 | PASS 2 | Binding note explicitly names "CAMPAIGN OPEN INCUMBENT ANCHOR sub-section (sub-section, not parent block)" as resolution source |

**V-03 composite: 86 / 100** | All essential: PASS | Golden: YES

---

## V-04 — Combined C-24 + C-26

**What it adds over baseline**: ROLE A Step 1 reads INCUMBENT ANCHOR sub-section by name, records `incumbent_anchor_read`; Step 2 verifies binding note names sub-section and that `incumbent_anchor_read` matches. Invariant D templates use bound reference `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]`. Binding note names sub-section as canonical source. INCUMBENT ANCHOR has "Do not re-establish" prohibition. Stage 0 EXIT SIGNAL names both sub-section-scoped binding and ROLE A activation. No Displacement read fields.

| ID | Pts | Score | Evidence note |
|----|-----|-------|---------------|
| C-01 | 10 | PASS 10 | All 6 EXIT SIGNALs; Stage 0 EXIT explicitly confirms sub-section binding + ROLE A activation |
| C-02 | 10 | PASS 10 | All 6 artifacts written |
| C-03 | 10 | PASS 10 | Bound-reference templates applied verbatim at stage entry conditions |
| C-04 | 10 | PASS 10 | All three synthesis fields present |
| C-05 | 10 | PASS 10 | Stage 4 cross-check + Stage 5 chain reconstruction |
| C-06 | 8 | PASS 8 | ROLE B execution |
| C-07 | 8 | PASS 8 | Full handoff table with derivation annotations |
| C-08 | 8 | PASS 8 | Counter-hypothesis resolution table |
| C-09 | 1 | PASS 1 | Dual-lock present |
| C-10 | 1 | PASS 1 | Stage 4 displacement verdict in evidence_summary |
| C-11 | 1 | PASS 1 | Mechanical failure language |
| C-12 | 1 | PASS 1 | Standalone SESSION INVARIANTS TABLE |
| C-13 | 2 | PASS 2 | Synthesis fields isolated as labeled pairs |
| C-14 | 2 | PARTIAL 1 | Inv D bidirectional (FORMAT ERROR registered + echoed); Inv C bidirectional; no DUAL-LOCK ERROR / INTEGRITY FAILURE registration |
| C-15 | 1 | PASS 1 | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section present |
| C-16 | 1 | FAIL 0 | No Displacement read fields in stage bodies |
| C-17 | 2 | FAIL 0 | No SYNTHESIS DECLARATIONS section with prohibition |
| C-18 | 2 | FAIL 0 | No Invariant E in SESSION INVARIANTS TABLE |
| C-19 | 1 | PASS 1 | Invariant D templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` bound reference |
| C-20 | 2 | FAIL 0 | No Displacement read in artifact content |
| C-21 | 1 | PASS 1 | INCUMBENT ANCHOR sub-section has "Do not re-establish the incumbent per stage. Carry forward from this sub-section only." |
| C-22 | 1 | PASS 1 | Binding note: resolves to incumbent_name in INCUMBENT ANCHOR sub-section; "Naming as literal string = FORMAT ERROR" + "Re-establishing per stage = FORMAT ERROR" |
| C-23 | 1 | FAIL 0 | No artifact Displacement reads in evidence_summary |
| C-24 | 2 | PASS 2 | ROLE A Step 1: reads INCUMBENT ANCHOR sub-section by name, records incumbent_anchor_read; "Tracing to parent block without naming INCUMBENT ANCHOR sub-section = FAIL"; Step 2 confirms match. Record before Stage 0 gate_open. |
| C-25 | 2 | FAIL 0 | No Displacement read infrastructure |
| C-26 | 2 | PASS 2 | Binding note explicitly names "CAMPAIGN OPEN INCUMBENT ANCHOR sub-section (the named sub-section, not the CAMPAIGN OPEN parent block)" |

**V-04 composite: 89 / 100** | All essential: PASS | Golden: YES

---

## V-05 — All-Axis: C-24 + C-25 + C-26

**What it adds over baseline**: All changes from V-04 plus Displacement read infrastructure. ROLE A Step 2 additionally confirms displacement read commitment for Stages 2/3/4. Stage 5 entry conditions gate on all three artifact Displacement reads confirmed. Stages 2/3/4 write Displacement read field to artifact content. Stage 5 evidence_summary cites all three. Stage 5 EXIT SIGNAL explicitly confirms "All three artifact Displacement reads cited in evidence_summary."

| ID | Pts | Score | Evidence note |
|----|-----|-------|---------------|
| C-01 | 10 | PASS 10 | All 6 EXIT SIGNALs; Stage 5 EXIT uniquely confirms displacement reads consumed |
| C-02 | 10 | PASS 10 | All 6 artifacts written; three evidence artifacts explicitly include Displacement read field |
| C-03 | 10 | PASS 10 | Bound-reference templates applied verbatim at all stage entry conditions |
| C-04 | 10 | PASS 10 | All three synthesis body fields present |
| C-05 | 10 | PASS 10 | Stage 4 cross-check + Stage 5 chain reconstruction |
| C-06 | 8 | PASS 8 | ROLE B execution |
| C-07 | 8 | PASS 8 | Full handoff table with derivation annotations |
| C-08 | 8 | PASS 8 | Counter-hypothesis resolution table |
| C-09 | 1 | PASS 1 | Dual-lock with both lock conditions + not_triggered else |
| C-10 | 1 | PASS 1 | evidence_summary requires Stage 4 verdict + all three artifact Displacement reads |
| C-11 | 1 | PASS 1 | Mechanical failure language at all checkpoints |
| C-12 | 1 | PASS 1 | Standalone SESSION INVARIANTS TABLE before Stage 0 |
| C-13 | 2 | PASS 2 | Synthesis fields isolated as labeled key-value pairs |
| C-14 | 2 | PARTIAL 1 | Inv D bidirectional FORMAT ERROR; Inv C bidirectional format error; no DUAL-LOCK ERROR / INTEGRITY FAILURE canonically registered |
| C-15 | 1 | PASS 1 | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section with incumbent + strength |
| C-16 | 1 | PASS 1 | Stages 2, 3, 4 each have labeled "Displacement read:" field written to artifact body |
| C-17 | 2 | FAIL 0 | No SYNTHESIS DECLARATIONS section with explicit prohibition against prose embedding |
| C-18 | 2 | FAIL 0 | No Invariant E in SESSION INVARIANTS TABLE; schema_compliance_confirmed row present but no canonical label registered and echoed |
| C-19 | 1 | PASS 1 | Invariant D templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` bound reference |
| C-20 | 2 | PASS 2 | All three evidence artifacts include "Displacement read:" field in artifact body; FAIL label for any absent |
| C-21 | 1 | PASS 1 | INCUMBENT ANCHOR sub-section + "Do not re-establish per stage. Carry forward from this sub-section only." |
| C-22 | 1 | PASS 1 | Binding note with resolution statement + "Naming as literal string = FORMAT ERROR" + "Re-establishing per stage = FORMAT ERROR" |
| C-23 | 1 | PASS 1 | evidence_summary requires all three artifact reads — floors C-23 and surpasses it |
| C-24 | 2 | PASS 2 | ROLE A Step 1: reads INCUMBENT ANCHOR sub-section by name, records incumbent_anchor_read; Step 2 confirms binding note, incumbent_anchor_read match, AND displacement read commitment for Stages 2/3/4 — extends C-24 beyond binding into chain contract |
| C-25 | 2 | PASS 2 | evidence_summary explicitly requires all three artifact reads by source + value; Stage 5 entry condition gates on all three confirmed; FAIL if fewer than three |
| C-26 | 2 | PASS 2 | Binding note names "CAMPAIGN OPEN INCUMBENT ANCHOR sub-section (sub-section, not parent block)" |

**V-05 composite: 95 / 100** | All essential: PASS | Golden: YES

---

## Summary & Rankings

| Rank | Variation | Score | New v6 criteria hit | Gap |
|------|-----------|-------|---------------------|-----|
| 1 | V-05 (all-axis) | 95 | C-24 + C-25 + C-26 | C-14 partial (-1), C-17 (-2), C-18 (-2) |
| 2 | V-04 (C-24+C-26) | 89 | C-24 + C-26 | +C-25 chain missing (-6 vs V-05) |
| 3 | V-02 (C-25) | 88 | C-25 | +C-24, C-26 missing (-7 vs V-05) |
| 4 | V-03 (C-26) | 86 | C-26 | +C-24, C-25, C-21 missing |
| 5 | V-01 (C-24) | 85 | C-24 | +C-26, C-25, C-21 missing |

**Gap analysis (V-04 vs V-05: 6 pts)**: V-04 gets C-24 + C-26 but misses the entire Displacement read chain (C-16, C-20, C-23, C-25 = 0+0+0+0 vs V-05's 1+2+1+2). The 6-point gap is entirely the displacement evidence chain.

**Gap analysis (V-05 vs perfect: 5 pts)**: C-14 partial (-1), C-17 FAIL (-2), C-18 FAIL (-2). C-17 (SYNTHESIS DECLARATIONS with explicit prohibition) and C-18 (Invariant E checkpoint with canonical label registered + echoed) are absent from the installed baseline across all five variations.

---

## Excellence Signals from V-05

**Signal 1 — ROLE A unifies binding activation and displacement read contract in a single initialization step.** V-05's ROLE A Step 2 confirms both `incumbent_anchor_read` matches the binding note AND that Stages 2/3/4 are committed to write "Displacement read:" fields to their artifact bodies. This makes ROLE A's pre-stage initialization the structural anchor for two parallel chains (binding chain: C-24/C-26, displacement evidence chain: C-25) rather than just the binding chain. The pattern: a single initialization step can activate multiple downstream chains simultaneously, reducing inter-chain coordination risk.

**Signal 2 — Stage 5 entry conditions as a structural gate on chain completeness.** V-05 adds `[ ] All three artifact Displacement read fields confirmed written (websearch, interview, prototype) -- Stage 5 will consume all three` as a Stage 5 entry condition. This creates an architectural gate: synthesis cannot begin until the displacement evidence chain is structurally complete. Previous variations required Stage 5 to cite the values but placed no pre-synthesis gate. The pattern: entry conditions can enforce cross-stage chain completeness, not just the immediately preceding EXIT SIGNAL.

**Signal 3 — Stage EXIT SIGNAL as output-level chain closure confirmation.** V-05's Stage 5 EXIT SIGNAL explicitly states "All three artifact Displacement reads cited in evidence_summary." This elevates the EXIT SIGNAL from a simple stage-completion declaration to a chain closure audit record. The pattern: EXIT SIGNALs can name specific chain properties that were fulfilled, making the campaign log a chain-verification trace rather than a sequence of stage names.

**Next-round targets (not yet captured by any criterion):**

- **C-17** (SYNTHESIS DECLARATIONS with explicit prohibition): 0/2 pts across all five variations — the installed baseline doesn't have this section. High-value 2-pt target absent from all R6 outputs.
- **C-18** (Invariant E checkpoint with registered canonical label echoed in HANDOFF TABLE): 0/2 pts across all five — no Invariant E in SESSION INVARIANTS TABLE in any variation.
- **C-14 full pass** (DUAL-LOCK ERROR + INTEGRITY FAILURE as canonically registered labels): all five are PARTIAL — the null tally and dual-lock failure labels are not yet in the SESSION INVARIANTS TABLE.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["ROLE A unifies binding activation and displacement read contract in a single initialization step, anchoring two parallel chains from one pre-stage execution block", "Stage 5 entry conditions gate on all three artifact Displacement reads confirmed written, enforcing chain completeness before synthesis can begin", "Stage 5 EXIT SIGNAL explicitly names displaced reads consumed, converting the exit declaration into an output-level chain closure audit record"]}
```
