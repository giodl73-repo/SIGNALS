---

## Quest Score — prove-topic Round 5 (Rubric v5)

### Scoring Basis

All R5 variations extend specific R4 single-axis or combined-axis bases. The R4 scorecard (2026-03-16) established:
- R4 V-01 (C-18 only): 96/100 on v4 rubric — fails C-19, C-20
- R4 V-02 (C-19 only): 96/100 — fails C-18, C-20
- R4 V-03 (C-20 only): 96/100 — fails C-18, C-19
- R4 V-04 (C-18+C-19): 98/100 — fails C-20
- R4 V-05 (all three): 100/100 — passes everything

R5 adds C-21 (INCUMBENT ANCHOR prohibition), C-22 (Invariant D binding resolution note), C-23 (Stage 5 artifact Displacement read citation). The v5 rubric rebalances aspirational pts: C-09/C-10 drop 3→2, C-11 drops 2→1, C-15/C-16/C-19 drop 2→1. New criteria add 6 pts total; pool stays at 26.

---

### V-01 — Axis: C-21 (INCUMBENT ANCHOR + prohibition)

**Base**: R4 V-01 (C-18 only). No other changes.

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs; Stage 0 CLEARANCE TABLE → gate_open; Stages 1–5 each emit STAGE N COMPLETE |
| C-02 | 10 | **PASS** | 6 artifacts: ROLE B gate record, hypothesis, websearch, interview, prototype, synthesis — each confirmed written |
| C-03 | 10 | **PASS** | SESSION INVARIANTS Invariant D templates verbatim at Stages 2/3/4; Template deviation = FORMAT ERROR registered |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS section; hypothesis_verdict / confidence_composite / key_risk all three fields declared |
| C-05 | 10 | **PASS** | Stage 4 cross-check with explicit running-count statement; Stage 5 reconstructs S2→S3→S4 chain independently |
| C-06 | 8 | **PASS** | ROLE B declared with scout_artifact (glob or ABSENT) and gate_s_cleared = true/CAMPAIGN BLOCKED |
| C-07 | 8 | **PASS** | PRE-COMMITTED HANDOFF SCHEMA all 11 fields with [derived from: X]; schema_compliance_confirmed present |
| C-08 | 8 | **PASS** | Stage 5 COUNTER-HYPOTHESIS RESOLUTION TABLE; verdict REFUTED/PARTIALLY REFUTED/OPEN RISK with citation |
| C-09 | 2 | **PASS** | ATOMIC DUAL-LOCK: both locks fire when null_tally_final ≥ 3; not_triggered path present |
| C-10 | 2 | **PASS** | Per-stage INCUMBENT CHECK TABLE has Yes/No/Inconclusive; Stage 5 evidence_summary cites Stage 4 displacement verdict |
| C-11 | 1 | **PASS** | Mechanical labels throughout: FORMAT ERROR, INTEGRITY FAILURE, DUAL-LOCK ERROR; no advisory softening |
| C-12 | 2 | **PASS** | SESSION INVARIANTS standalone block before Stage 0 ENTRY CONDITIONS; all six rows (D, A, B, C, E, F) |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS section with isolated key-value fields; each extractable by label match |
| C-14 | 2 | **PASS** | Failure labels registered in SESSION INVARIANTS; inline enforcement echoes exact registered labels |
| C-15 | 1 | **PASS** | CAMPAIGN OPEN block pre-registers topic, date, status_quo_comparator, incumbent fields before Stage 0 |
| C-16 | 1 | **PASS** | Stages 2, 3, 4 each carry "Displacement read:" synthesis field above INCUMBENT CHECK TABLE |
| C-17 | 2 | **PASS** | SYNTHESIS DECLARATIONS header: "Do not embed these values in prose sentences" explicit prohibition |
| C-18 | 2 | **PASS** | SESSION INVARIANTS Invariant E: "Invariant E checkpoint — FAIL" canonical label registered; ROLE A confirms; schema_compliance_confirmed echoes verbatim |
| C-19 | 1 | **FAIL** | Invariant D uses `{status_quo_comparator}` template variable — does not reference "CAMPAIGN OPEN" by name. R4 V-01 base inherited this gap |
| C-20 | 2 | **FAIL** | Write confirmations do not describe Displacement read as artifact file content — field appears in stage output only. R4 V-01 base did not carry C-20 |
| C-21 | 2 | **PASS** | CAMPAIGN OPEN contains labeled INCUMBENT ANCHOR sub-section + explicit prohibition: "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN." |
| C-22 | 2 | **FAIL** | No binding resolution note in Invariant D; no "naming as literal string = FORMAT ERROR" label registered |
| C-23 | 2 | **FAIL** | Stage 5 evidence_summary cites Stage 4 verdict but not artifact Displacement read values — C-20 not present, so chain is broken upstream |

**Essential**: 5/5 (50 pts) | **Recommended**: 3/3 (24 pts) | **Aspirational**: 19/26 pts
**V-01 Composite: 93/100** — All essential PASS ✓

---

### V-02 — Axis: C-22 (Invariant D binding resolution note + literal-string failure label)

**Base**: R4 V-02 (C-19 only). No other changes.

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs in order (inherited) |
| C-02 | 10 | **PASS** | All 6 artifacts written and confirmed (inherited) |
| C-03 | 10 | **PASS** | Invariant D templates verbatim at S2/3/4 with FORMAT ERROR label (inherited) |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS with all three synthesis body fields (inherited) |
| C-05 | 10 | **PASS** | Null tally chain cross-check at Stage 4; Stage 5 chain reconstruction (inherited) |
| C-06 | 8 | **PASS** | ROLE B with scout_artifact + gate_s_cleared (inherited) |
| C-07 | 8 | **PASS** | 11-field HANDOFF TABLE with derivations (inherited) |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution table with typed verdict (inherited) |
| C-09 | 2 | **PASS** | Dual-lock both locks; not_triggered path (inherited) |
| C-10 | 2 | **PASS** | Per-stage Displacement framing; Stage 5 cites Stage 4 verdict (inherited) |
| C-11 | 1 | **PASS** | Mechanical failure language at all three checkpoints (inherited) |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS block before Stage 0 (inherited) |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS isolation (inherited) |
| C-14 | 2 | **PASS** | Two-layer bidirectional enforcement (inherited) |
| C-15 | 1 | **PASS** | CAMPAIGN OPEN pre-registers incumbent fields (inherited) |
| C-16 | 1 | **PASS** | Per-stage Displacement read fields (inherited) |
| C-17 | 2 | **PASS** | SYNTHESIS DECLARATIONS explicit prohibition (inherited) |
| C-18 | 2 | **FAIL** | No Invariant E canonical label in SESSION INVARIANTS. R4 V-02 base (C-19 only axis) did not carry C-18 |
| C-19 | 1 | **PASS** | Invariant D uses `[incumbent from CAMPAIGN OPEN]` binding in all three stage templates; "literal re-establishment = FORMAT ERROR" at ROLE A confirmation |
| C-20 | 2 | **FAIL** | Artifact write confirmations do not describe Displacement read as file content. R4 V-02 base did not carry C-20 |
| C-21 | 2 | **FAIL** | No INCUMBENT ANCHOR sub-section in CAMPAIGN OPEN; no "Do not re-establish" prohibition |
| C-22 | 2 | **PASS** | Invariant D carries: (a) "Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name" resolution note and (b) "naming as literal string = FORMAT ERROR" canonical failure label — C-14-class mechanism applied to C-19 binding rule |
| C-23 | 2 | **FAIL** | Stage 5 does not cite artifact Displacement read values; C-20 absent so no artifact values to consume |

**Essential**: 5/5 (50 pts) | **Recommended**: 3/3 (24 pts) | **Aspirational**: 18/26 pts
**V-02 Composite: 92/100** — All essential PASS ✓

---

### V-03 — Axis: C-23 (Stage 5 cites artifact Displacement read by value)

**Base**: R4 V-03 (C-20 only). No other changes.

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs in order (inherited) |
| C-02 | 10 | **PASS** | All 6 artifacts; write confirmations include Displacement read values (inherited, C-20 present) |
| C-03 | 10 | **PASS** | Invariant D templates verbatim (inherited) |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS with three synthesis fields (inherited) |
| C-05 | 10 | **PASS** | Null tally chain cross-check complete (inherited) |
| C-06 | 8 | **PASS** | ROLE B with gate (inherited) |
| C-07 | 8 | **PASS** | 11-field HANDOFF TABLE (inherited) |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution (inherited) |
| C-09 | 2 | **PASS** | Dual-lock (inherited) |
| C-10 | 2 | **PASS** | Per-stage displacement framing; Stage 5 cites Stage 4 verdict (inherited) |
| C-11 | 1 | **PASS** | Mechanical language (inherited) |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS block (inherited) |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS isolation (inherited) |
| C-14 | 2 | **PASS** | Two-layer enforcement (inherited) |
| C-15 | 1 | **PASS** | CAMPAIGN OPEN pre-registers (inherited) |
| C-16 | 1 | **PASS** | Per-stage Displacement read fields (inherited) |
| C-17 | 2 | **PASS** | SYNTHESIS DECLARATIONS prohibition (inherited) |
| C-18 | 2 | **FAIL** | No Invariant E canonical label. R4 V-03 base (C-20 only) did not carry C-18 |
| C-19 | 1 | **FAIL** | Invariant D uses `{status_quo_comparator}` — no `[incumbent from CAMPAIGN OPEN]` binding. R4 V-03 did not carry C-19 |
| C-20 | 2 | **PASS** | Websearch, interview, prototype write confirmations each describe "Artifact content includes: Displacement read: [copy — written to file]" |
| C-21 | 2 | **FAIL** | No INCUMBENT ANCHOR sub-section; no "Do not re-establish" prohibition |
| C-22 | 2 | **FAIL** | No binding resolution note in Invariant D |
| C-23 | 2 | **PASS** | Stage 5 evidence_summary contains direct citation: "websearch Displacement read: [value]" naming artifact file and read value — confirmed by C-20 artifact presence |

**Essential**: 5/5 (50 pts) | **Recommended**: 3/3 (24 pts) | **Aspirational**: 19/26 pts
**V-03 Composite: 93/100** — All essential PASS ✓

---

### V-04 — Combined: C-21 + C-22 (registration layer complete)

**Base**: R4 V-04 (C-18 + C-19). Adds C-21 and C-22.

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs; Stage 0 EXIT names Invariant D binding + Invariant E label (inherited) |
| C-02 | 10 | **PASS** | All 6 artifacts confirmed (inherited) |
| C-03 | 10 | **PASS** | `[incumbent from CAMPAIGN OPEN]` bound templates at S2/3/4; FORMAT ERROR label active (inherited from C-19) |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS all three fields (inherited) |
| C-05 | 10 | **PASS** | Stage 4 cross-check + Stage 5 chain confirmation (inherited) |
| C-06 | 8 | **PASS** | ROLE B with scout_artifact, gate_s_cleared, CAMPAIGN BLOCKED (inherited) |
| C-07 | 8 | **PASS** | 11 fields; schema_compliance_confirmed echoes "Invariant E checkpoint — FAIL" (inherited from C-18) |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution with typed verdict (inherited) |
| C-09 | 2 | **PASS** | ATOMIC DUAL-LOCK both locks with DUAL-LOCK ERROR label (inherited) |
| C-10 | 2 | **PASS** | Displacement framing; Stage 5 cites Stage 4 verdict by bound name (inherited) |
| C-11 | 1 | **PASS** | Mechanical enforcement language (inherited) |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS block (inherited) |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS isolation (inherited) |
| C-14 | 2 | **PASS** | Bidirectional enforcement: all failure modes (D, A, B, C, E, F) registered (inherited) |
| C-15 | 1 | **PASS** | CAMPAIGN OPEN + INCUMBENT ANCHOR block (inherited; C-21 makes the sub-section named) |
| C-16 | 1 | **PASS** | Per-stage Displacement read fields (inherited) |
| C-17 | 2 | **PASS** | SYNTHESIS DECLARATIONS prohibition (inherited) |
| C-18 | 2 | **PASS** | Invariant E: "Invariant E checkpoint — FAIL" canonical label registered; echoed at schema_compliance_confirmed (inherited from R4 V-04) |
| C-19 | 1 | **PASS** | `[incumbent from CAMPAIGN OPEN]` in all three templates; bound text carried to stage tables (inherited from R4 V-04) |
| C-20 | 2 | **FAIL** | Write confirmations do not describe Displacement read as artifact file content. R4 V-04 base failed C-20; V-04 does not add it |
| C-21 | 2 | **PASS** | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section named; "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN." prohibition present |
| C-22 | 2 | **PASS** | Invariant D: "Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name" + "naming as literal string = FORMAT ERROR" — C-14-class label registered for binding violation |
| C-23 | 2 | **FAIL** | Stage 5 does not require artifact Displacement read citation; C-20 absent so no artifact values available to cite |

**Essential**: 5/5 (50 pts) | **Recommended**: 3/3 (24 pts) | **Aspirational**: 22/26 pts
**V-04 Composite: 96/100** — All essential PASS ✓

---

### V-05 — Full R5 Integration (C-21 + C-22 + C-23 on R4 gold base)

**Base**: R4 V-05 (all three R4 criteria). Adds C-21, C-22, C-23.

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs; Stage 0 EXIT declares Invariant D binding, Invariant E label, and ARTIFACT DISPLACEMENT RULE active |
| C-02 | 10 | **PASS** | All 6 artifacts with Displacement read values in write confirmations |
| C-03 | 10 | **PASS** | `[incumbent from CAMPAIGN OPEN]` bound templates verbatim at S2/3/4; "Naming incumbent as literal string = FORMAT ERROR" inline echo |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS section; hypothesis_verdict / confidence_composite / key_risk each on own line; Invariant F checkpoint echo |
| C-05 | 10 | **PASS** | Stage 4: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]." Stage 5: S2+S3+S4 chain reconstructed; "null_tally_final confirmed: [N]" |
| C-06 | 8 | **PASS** | ROLE B execution — scout_artifact path required output; gate_s_cleared explicit; CAMPAIGN BLOCKED on absent |
| C-07 | 8 | **PASS** | 11 fields + [derived from: X]; schema_compliance_confirmed echoes "Invariant E checkpoint — FAIL" verbatim |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution table; OPEN RISK triggers one-tier confidence reduction before ATOMIC DUAL-LOCK |
| C-09 | 2 | **PASS** | ATOMIC DUAL-LOCK: Lock 1 (adversarial reviewer named) + Lock 2 (cap values shown); not_triggered path; DUAL-LOCK ERROR if conditions met without both locks |
| C-10 | 2 | **PASS** | Per-stage reads; Stage 5 cites Stage 4 displacement verdict and artifact Displacement read values by value (C-23 closes this framing chain) |
| C-11 | 1 | **PASS** | Mechanical labels throughout: "Cannot be softened or overridden"; all three checkpoints use registered labels |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS before Stage 0; all six rows (D, A, B, C, E, F) with activation conditions |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS with explicit prohibition and Invariant F label; fields isolatable by label match |
| C-14 | 2 | **PASS** | All failure modes bidirectionally detectable; C-22 extends this to the binding mechanism itself |
| C-15 | 1 | **PASS** | CAMPAIGN OPEN with incumbent + incumbent_strength declared before SESSION INVARIANTS |
| C-16 | 1 | **PASS** | Stages 2, 3, 4 each have "Displacement read:" field; Stage 5 ENTRY CONDITIONS confirm all three written |
| C-17 | 2 | **PASS** | "Do not embed these values in prose sentences"; Invariant F checkpoint — SYNTHESIS FORMAT ERROR |
| C-18 | 2 | **PASS** | SESSION INVARIANTS E: canonical "Invariant E checkpoint — FAIL" registered; ROLE A confirms at Step 3; schema_compliance_confirmed echoes verbatim |
| C-19 | 1 | **PASS** | `[incumbent from CAMPAIGN OPEN]` in all three Invariant D templates; binding resolves to incumbent_name; literal string = FORMAT ERROR at ROLE A |
| C-20 | 2 | **PASS** | Each write confirmation: "Artifact content includes: Displacement read: [copy — written to file]"; Stage 5 ENTRY CONDITIONS: "All three evidence artifacts confirmed written with Displacement read fields" |
| C-21 | 2 | **PASS** | CAMPAIGN OPEN INCUMBENT ANCHOR sub-section with named header + "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN." prohibition |
| C-22 | 2 | **PASS** | Invariant D: "Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name" + "naming as literal string = FORMAT ERROR" registered canonical label |
| C-23 | 2 | **PASS** | Stage 5 evidence_summary cites at least one artifact Displacement read value directly (e.g., "websearch Displacement read: [value]"); Stage 5 ENTRY CONDITIONS gate on artifact reads confirmed written |

**Essential**: 5/5 (50 pts) | **Recommended**: 3/3 (24 pts) | **Aspirational**: 26/26 pts
**V-05 Composite: 100/100** — All essential PASS ✓ — Golden ✓

---

## Rankings

| Rank | Variation | Composite | All Essential | New criteria passing |
|------|-----------|-----------|---------------|---------------------|
| 1 | V-05 (full R5 integration) | **100** | ✓ | C-21, C-22, C-23 |
| 2 | V-04 (C-21 + C-22) | **96** | ✓ | C-21, C-22 |
| 3 | V-01 (C-21 only) | **93** | ✓ | C-21 |
| 3 | V-03 (C-23 only) | **93** | ✓ | C-23 |
| 5 | V-02 (C-22 only) | **92** | ✓ | C-22 |

**Single-axis gap**: V-01/V-03 score 93 (gain C-21 or C-23, each 2 pts; lose 5 pts from aspirational rebalancing of their gaps). V-02 scores 92 (gain C-22, 2 pts; lose 6 pts including C-19 rebalancing, since C-19 is now 1 pt vs prior 2).

**Score delta pattern**: V-04 = V-05 − 4 pts (missing C-20 and C-23). V-05 achieves 100 because R4 V-05 already closed C-20, and adding C-21/C-22/C-23 fills the remaining gap.

---

## Excellence Signals — V-05

**Signal 1 — Symmetric prohibition pair: INCUMBENT ANCHOR mirrors SYNTHESIS DECLARATIONS.**
V-05 is the first variation where both drift-prone zones have an upstream named prohibition: C-17 prevents synthesis fields from being embedded in prose ("Do not embed in prose sentences"), and C-21 prevents the incumbent from being re-established per stage ("Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN."). The structural mechanism is identical: name the section, state what must not happen. Any deviation is self-incriminating from two directions simultaneously (prohibition text present + registered failure label). Prior rounds protected synthesis fields; V-05 closes the symmetric gap at the registration layer.

**Signal 2 — Every declared failure mode now has a registered canonical label.**
C-22 completes the C-14-class two-layer enforcement for the C-19 binding rule: "naming as literal string = FORMAT ERROR" is registered in SESSION INVARIANTS, not expressed only as mechanical prose. Before V-05 (or R5), C-19 had enforcement language but no registered canonical label for its specific binding violation. V-05 closes this: every failure mode (D-FORMAT ERROR, A-DUAL-LOCK ERROR, B-DUAL-LOCK ERROR, C-FORMAT ERROR, E-Invariant E checkpoint — FAIL, F-SYNTHESIS FORMAT ERROR, binding-FORMAT ERROR) has a canonical entry in SESSION INVARIANTS. Bidirectional enforcement is now architecturally complete.

**Signal 3 — Stage 5 artifact citation closes the three-layer displacement evidence chain.**
The chain is now end-to-end traceable: C-16 (each stage declares Displacement read in output) → C-20 (artifact file carries the field as file content) → C-23 (Stage 5 synthesis cites artifact field value directly, not stage output). In V-01 through V-04, Stage 5 can pass C-10 by restating stage verdicts, effectively bypassing the artifact files. C-23 + Stage 5 ENTRY CONDITIONS requiring artifact reads confirmed means Stage 5 must consume the artifact storage layer, not just the stage output layer. The portability investment of C-20 is now verifiably used, not optional.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["symmetric prohibition pair: INCUMBENT ANCHOR sub-section with Do-not-re-establish prohibition mirrors SYNTHESIS DECLARATIONS prohibition — both drift-prone zones now have upstream named sections that make deviation self-incriminating before any enforcement checkpoint fires", "every declared failure mode has a registered canonical label: C-22 adds binding-violation FORMAT ERROR to SESSION INVARIANTS, completing the C-14-class two-layer architecture for the C-19 binding rule — no failure mode is now expressed only as mechanical prose", "Stage 5 ENTRY CONDITIONS gate on artifact Displacement reads confirmed written — C-23 closes the three-layer chain C-16→C-20→C-23 and forces synthesis to consume artifact storage, not bypass it"]}
```
