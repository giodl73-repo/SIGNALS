| Criterion | Evidence |
|-----------|----------|
| C-09 | Block 3: dual_lock_fired / not_triggered conditional; co_activation_confirmed present |
| C-10 | INCUMBENT CHECK TABLES at S2/S3/S4 have displacement verdicts; Stage 5 cites Stage 4 displacement verdict |
| C-11 | "FORMAT ERROR", "INTEGRITY FAILURE", "FAIL", "CHAIN INTEGRITY FAILURE. Halt." throughout |
| C-12 | SESSION INVARIANTS TABLE appears before Stage 0 gate_open in all |
| C-13 | SYNTHESIS DECLARATIONS: hypothesis_verdict, confidence_composite, key_risk each as labeled key-value pairs |
| C-14 | FORMAT ERROR registered for D and echoed at stage tables; FAIL registered for C and echoed at handoff — bidirectional architecture exists for at least one invariant in all. V-05 additionally echoes "DUAL-LOCK ERROR" precisely at Block 3 lock steps; still 1pt max |
| C-15 | CAMPAIGN OPEN block with topic, date, status_quo_comparator before SESSION INVARIANTS |
| C-16 | "Displacement read: [one sentence]" field at Stage 2, 3, 4 in all |
| C-17 | "Do not embed these values in prose sentences. Each on its own line, extractable by label match." in SYNTHESIS DECLARATIONS |
| C-18 | schema_compliance_confirmed row present with "Invariant E checkpoint -- FAIL if any field unlabeled" in all. V-02/V-04/V-05 additionally register SESSION INVARIANTS Invariant E (SYNTHESIS-FAIL) — richer registration, historically sufficient for PASS |
| C-19 | "[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]" in all three Invariant D templates |
| C-20 | "Artifact body includes Displacement read field" stated at S2/S3/S4 write instructions |
| C-21 | INCUMBENT ANCHOR sub-section present + "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN." |
| C-22 | "Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name. Naming as literal string = FORMAT ERROR." |
| C-23 | evidence_summary template cites at least one artifact Displacement read by source |
| C-24 | ROLE A: "INCUMBENT ANCHOR read: resolved incumbent_name confirmed. Invariant D binding active. Source: CAMPAIGN OPEN INCUMBENT ANCHOR sub-section." |
| C-25 | evidence_summary instruction enumerates all three: websearch / interview / prototype Displacement reads (mandatory) |
| C-26 | Binding note names "CAMPAIGN OPEN INCUMBENT ANCHOR" (sub-section precision) as source |
| C-27 | ROLE A carries both incumbent_anchor_read AND displacement_read_contract fields |
| C-28 | Stage 5 entry: "[ ] All three artifact Displacement read fields confirmed written ... Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt." |
| C-29 | Stage 5 EXIT SIGNAL names chain closure with "all three cited in evidence_summary" |
| C-30 | evidence_summary instruction: mandatory (not conditional), names websearch / interview / prototype |
| C-31 | Stage 5 entry: "[per ROLE A displacement_read_contract -- websearch, interview, prototype]" |
| C-32 | EXIT SIGNAL names websearch Displacement read, interview Displacement read, prototype Displacement read individually |
| C-33 | "Chain closed." appears as distinct terminal assertion after named-artifact enumeration in all five EXIT SIGNALs |
| C-34 | "Omission of any artifact Displacement read = FAIL" (V-01/V-03) or "= SYNTHESIS-FAIL" (V-02/V-04/V-05) present in evidence_summary instruction |

**Aspirational subtotal: 26/26 — all pass.**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 50 | 24 | 26 | **99** |
| V-02 | 50 | 24 | 26 | **99** |
| V-03 | 50 | 24 | 26 | **99** |
| V-04 | 50 | 24 | 26 | **99** |
| V-05 | 50 | 24 | 26 | **99** |

**All five pass the golden threshold (all essential PASS + composite >= 80).**

Score basis: R8 V-05 converted to 99/100 under v9 (C-18 reduction −1, C-33 +1, C-34 +1). All R9 variations carry that baseline. New structural axes — CLOSURE CANONICAL FORM, Invariant E as SESSION INVARIANTS row, Stage 0 pre-commits, dual-lock label precision — are excellence signal candidates for v10 and do not map to additional v9-scored criteria.

---

## Ranking

1. **V-05** — 99/100, 4 excellence signal patterns (highest structural density)
2. **V-04** — 99/100, 2 excellence signal patterns (CLOSURE FORM + Invariant E)
3. **V-02** — 99/100, 1 pattern (Invariant E as SESSION INVARIANT with SYNTHESIS-FAIL label)
4. **V-01** — 99/100, 1 pattern (CLOSURE CANONICAL FORM pre-registration)
5. **V-03** — 99/100, 1 pattern (Stage 0 forward pre-commitment chain)

V-01 and V-02 are peer-ranked differently only by which structural axis they test. V-03 ranks last because Stage 0 pre-commit doesn't extend the SESSION INVARIANTS registration layer.

---

## Excellence Signals — Candidates for v10 C-35+

**Signal 1 — CAMPAIGN CLOSURE CANONICAL FORM two-layer enforcement (V-01/V-04/V-05)**
Pre-register the Stage 5 EXIT SIGNAL terminal form as a named block before roles execute. Stage 5 EXIT SIGNAL echoes "Echoing registered CAMPAIGN CLOSURE CANONICAL FORM:" before the enumeration. Converts C-33 from a behavioral pattern into a bidirectional enforcement architecture: registered canonical source → Stage 5 verbatim echo. Structural analog of C-14 applied to C-33.

**Signal 2 — SESSION INVARIANTS Invariant E as SYNTHESIS EVIDENCE MANDATE (V-02/V-04/V-05)**
Elevate the evidence_summary omission mandate from an inline Stage 5 instruction to a named SESSION INVARIANTS row (Invariant E: SYNTHESIS EVIDENCE MANDATE, failure label SYNTHESIS-FAIL). evidence_summary instruction echoes "SESSION INVARIANT E active" and "(echoes SESSION INVARIANTS Invariant E registered failure label)". Creates full two-layer enforcement for C-34 with a registered source + inline echo. The C-14 architecture now spans D (FORMAT ERROR), C (FAIL), A/B (DUAL-LOCK ERROR), and E (SYNTHESIS-FAIL).

**Signal 3 — Stage 0 EXIT SIGNAL pre-commits Stage 5 closure form and synthesis mandate (V-03/V-05)**
Stage 0 gate_open EXIT SIGNAL names `synthesis_closure_form: 'Chain closed.'` and `synthesis_mandate_label: Omission = FAIL` as explicit forward-commitments. Stage 5 ENTRY CONDITIONS verify them by field name. Creates a Stage 0 → Stage 5 structural pre-commitment chain, parallel to ROLE A displacement_read_contract → Stage 5 entry verification (C-27/C-31).

**Signal 4 — Dual-lock inline label precision (V-05 only)**
Block 3 lock step annotations echo "DUAL-LOCK ERROR" verbatim: "Bypassing adversarial review = DUAL-LOCK ERROR. (echoes registered SESSION INVARIANT A label)" and "Softening or overriding cap = DUAL-LOCK ERROR. (echoes registered SESSION INVARIANT B label)". Resolves the R8 universal C-14 partial where inline used "dual_lock_fired / BLOCKED" instead of the registered label. The C-14 architecture is now complete for all five SESSION INVARIANTS (D/C/A/B/E).

**V-05 is the convergence candidate for v10.** All four patterns are present and mutually reinforcing. The five-link traceability chain established in v9 (C-27 → C-31 → C-30 → C-34 → C-32 → C-33) now has a parallel governance layer: CLOSURE CANONICAL FORM + Invariant E + Stage 0 pre-commit enforce C-33/C-34 at the registration level, not just the instruction level.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["CAMPAIGN CLOSURE CANONICAL FORM pre-registration creates two-layer enforcement for C-33: registered canonical terminal form before roles execute, Stage 5 EXIT SIGNAL echoes by registered block name", "SESSION INVARIANTS Invariant E (SYNTHESIS EVIDENCE MANDATE, SYNTHESIS-FAIL) elevates evidence_summary omission mandate to full two-layer enforcement for C-34: registered invariant source plus inline echo with Invariant E name", "Stage 0 EXIT SIGNAL pre-commits synthesis_closure_form and synthesis_mandate_label as named forward-declarations verified at Stage 5 ENTRY CONDITIONS by field name -- Stage 0 to Stage 5 closure commitment chain parallel to ROLE A displacement_read_contract", "Block 3 dual-lock echoes DUAL-LOCK ERROR precisely at each lock step resolving the R8 universal C-14 partial and completing bidirectional label enforcement for all five SESSION INVARIANTS"]}
```
