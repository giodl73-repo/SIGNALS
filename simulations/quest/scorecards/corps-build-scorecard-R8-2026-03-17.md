# corps-build Scorecard — Round 8 (2026-03-17)
**Rubric**: v6 | **Variations**: V-01 through V-05 | **Max**: 170

---

## Scoring Summary

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| **Essential (12 pts each)** | | | | | | |
| C-01 | Role file completeness | PASS | PASS | PASS | PASS | PASS |
| C-02 | org-chart.md ASCII hierarchy | PASS | PASS | PASS | PASS | PASS |
| C-03 | IA in every team | PASS | PASS | PASS | PASS | PASS |
| C-04 | org.yaml structural fidelity | PASS | PASS | PASS | PASS | PASS |
| C-05 | Role file typed fields | PASS | PASS | PASS | PASS | PASS |
| **Recommended (10 pts each)** | | | | | | |
| C-06 | Headcount table + levels | PASS | PASS | PASS | PASS | PASS |
| C-07 | Standard vs specialized | PASS | PASS | PASS | PASS | PASS |
| C-08 | AMEND three options | PASS | PASS | PASS | PASS | PASS |
| **Aspirational (5 pts each)** | | | | | | |
| C-09 | IA team-contextualized | PASS | PASS | PASS | PARTIAL | PASS |
| C-10 | Cross-ref integrity | PASS | PASS | PASS | PASS | PASS |
| C-11 | Named invariants block | PASS | PASS | PASS | PASS | PASS |
| C-12 | Auditable check-output | PASS | PASS | PASS | PASS | PASS |
| C-13 | Named failure modes | PASS | PASS | PASS | PASS | PASS |
| C-14 | Dedicated pre-step FAILURE MODES | PASS | PASS | PASS | PASS | PASS |
| C-15 | Named CHECK-OUTPUT PROTOCOL | PASS | PASS | PASS | PASS | PASS |
| C-16 | Phase-exit guard tokens | PASS | PASS | PASS | PASS | PASS |
| C-17 | Per-artifact TRANSCRIPTION-RECEIPT | PASS | PASS | PASS | PASS | PASS |
| C-18 | BUILD-VERIFY single-purpose | PASS | PASS | PASS | PASS | PASS |
| C-19 | TRANSCRIPTION-RECEIPT in-phase remediation | PASS | PASS | PASS | PASS | PASS |
| C-20 | BUILD-VERIFY exclusion manifest | PASS | PASS | PASS | PASS | PASS |
| C-21 | TRANSCRIPTION-CLEAR all-artifact re-audit | PASS | PASS | PASS | PASS | PASS |
| C-22 | IA failure mode contrast pair | PASS | PASS | PASS | PASS | PASS |
| C-23 | Typed STRUCTURAL-ERROR code taxonomy | PASS | PASS | PASS | PASS | PASS |
| C-24 | Premature-exit violation as STRUCTURAL-ERROR | PASS | PASS | PASS | PASS | PASS |
| **Composite** | | **170** | **170** | **170** | **167.5** | **170** |

---

## Per-Variation Evidence Notes

### V-01 — 170/170

**New axis**: ENTRY-GATE tokens at each phase start (Phase 2–10), naming required prior exit token with halt instruction if absent (`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS`). Bidirectional boundary enforcement.

- C-01: CROSS-REF Phase 10 emits explicit `org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]` plus `table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n]`. PASS.
- C-09: WRITE-IA has named transplantable/non-transplantable contrast pair ("Any change to the existing architecture..." vs "The claim routing table's 847 active rule entries..."). PROFILE has inline contrast examples for defended-artifact quality ("the existing pipeline architecture" vs "the schema contract table that maps 34 external callers"). PASS.
- C-16: Phase gates present (PARSE-PASS, VALIDATE-PASS, TABLE-CLOSED, CONTRACT-SEAL-PASS, PROFILE-GATE, IA-PHASE-COMPLETE, ROLES-COMPLETE, CHART-WRITTEN, BUILD-VERIFY-COMPLETE). NEW: ENTRY-GATE checks at every receiving phase. Bidirectional — both exit and entry are named. PASS.
- C-23: Inline STRUCTURAL-ERROR codes per phase + typed EXCLUSION-MANIFEST table in BUILD-VERIFY. Codes are grep-detectable and typed (inherited from R7 V-05 baseline). PASS.
- C-24: `STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT -- CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B is a structural error.` Present. PASS.

No regressions from baseline. Entry gates are an additive structural frame.

---

### V-02 — 170/170

**New axis**: STRUCTURAL-ERROR-CATALOG table before Phase 1. Lists all 13 codes with Phase and Trigger columns. Phase bodies reference codes by name rather than re-defining them (`Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog)`).

- C-09: WRITE-IA has named IA contrast pair. PROFILE failure modes include inline contrast: "the existing pipeline architecture" (bad) vs "the event-resequencing buffer that handles out-of-order arrivals" (good). PASS.
- C-20: BUILD-VERIFY EXCLUSION-MANIFEST table still present, now annotated `(all codes in catalog)` — confirms table persists and points to catalog for canonical definition. PASS.
- C-23: Upfront STRUCTURAL-ERROR-CATALOG table organizes all codes by code, phase, and trigger before Phase 1 begins. This is the fullest possible satisfaction of "organized as a typed taxonomy table" — stronger than inline codes. PASS (highest fidelity on this criterion).
- C-24: STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT defined in catalog and referenced inline in WRITE-CHART. PASS.

No regressions from baseline. Catalog creates a pre-execution auditable taxonomy.

---

### V-03 — 170/170

**New axis**: PROFILE phase receives typed violation codes: STRUCTURAL-ERROR:PROFILE-CATEGORY, STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED, STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS. Dedicated typed violations table in Phase 5. Named failure mode contrast pair also added to PROFILE for defended-artifact quality.

- C-09: PROFILE now has BOTH typed codes AND a dedicated labeled contrast pair in Phase 5 (`FAIL (category): "the existing pipeline architecture"` / `PASS (specific): "the event-resequencing buffer that preserves order during backpressure"`), PLUS the WRITE-IA non-transplantable contrast pair. IA team-contextualization enforced at derivation source AND at write time. PASS — highest coverage of this criterion.
- C-22: The IA contrast pair in WRITE-IA satisfies C-22. V-03 additionally provides a parallel PROFILE contrast pair for the defended-artifact quality check — the FAIL/PASS labeling mirrors the IA contrast structure but at the upstream derivation phase. PASS plus extension.
- C-23: PROFILE typed codes extend the taxonomy to the upstream phase. The full code set now covers VALIDATE, CONTRACT, PROFILE, WRITE-IA, WRITE-CHART, and BUILD-VERIFY — all major phases with constraint-bearing operations. PASS.
- C-24: STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT present. PASS.
- PROFILE-GATE gate wording upgraded: `No STRUCTURAL-ERROR:PROFILE-* violations outstanding. All defended-artifacts name specific things. All lens-phrases derived from team vocabulary. All lens-phrases unique across teams.` — PROFILE-DUPLICATE-LENS check now explicit in gate closure condition.

---

### V-04 — 167.5/170

**Axes**: V-01 (entry gates) + V-02 (upfront catalog). PROFILE compressed to accommodate structural preamble.

- C-09: **PARTIAL.** WRITE-IA retains the named transplantable/non-transplantable contrast pair (full IA contrast — satisfies C-22). However, PROFILE failure modes are stripped to bare terse statements: `"Failure modes: — Defended-artifact names a category -> rewrite before next team. — Lens-phrase uses vocabulary absent from defended-artifact or change-pressure -> rewrite."` No contrast examples, no inline illustrations. Every other variation retains inline contrast examples at the PROFILE stage. The failure mode is named but not testable from PROFILE alone — contrast examples are missing from the upstream derivation source. PARTIAL (2.5 pts).
- C-22: PASS — IA contrast pair preserved in WRITE-IA.
- C-23: PASS — upfront catalog covers all codes.
- C-16: PASS — entry gates on all phases (same as V-01).

The compression trade-off: V-04's catalog + entry gate combination is structurally complete, but PROFILE failure mode depth is sacrificed. The PROFILE section's quality regression is the only meaningful criterion impact.

---

### V-05 — 170/170

**Axes**: V-01 + V-02 + V-03 — full integration. All three R8 axes simultaneously.

- C-09: PASS — PROFILE has dedicated typed violations table + labeled contrast pair (`FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture"` / `PASS: "the event-resequencing buffer that preserves order during backpressure"`). WRITE-IA has full non-transplantable contrast pair. Both stages present.
- C-22: PASS — IA contrast pair present at highest fidelity. The PROFILE contrast pair mirrors C-22 structure at the upstream derivation source, creating end-to-end contrast coverage.
- C-23: PASS — STRUCTURAL-ERROR-CATALOG is the most complete taxonomy: 16 codes (13 from V-02 + 3 PROFILE codes from V-03), all indexed before Phase 1. PROFILE codes appear in catalog and phase bodies reference `(see catalog)`. No code appears in a phase that is absent from the catalog.
- C-24: PASS — STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT in catalog and inline in WRITE-CHART PATH-B.
- PROFILE-GATE wording: `No STRUCTURAL-ERROR:PROFILE-* violations outstanding. All defended-artifacts name specific things. All lens-phrases derived from team vocabulary. All lens-phrases unique across teams.` — closes all three PROFILE error classes.
- WRITE-CHART maintains full four-step structure (8a–8d) with detailed step labels. WRITE-IA maintains detailed field descriptions. No compression artifacts.

V-05 closes all three R8 structural asymmetries simultaneously:
1. Phase entries were unnamed → ENTRY-GATE tokens make every transition authorized
2. Error codes were scattered → STRUCTURAL-ERROR-CATALOG makes taxonomy navigable before Phase 1
3. PROFILE used prose enforcement → Typed codes match downstream verification precision

---

## Ranking

| Rank | Variation | Score | Key Distinction |
|------|-----------|-------|-----------------|
| 1 (tied) | V-05 | 170 | All three axes; fullest integration; PROFILE catalog coverage |
| 1 (tied) | V-03 | 170 | PROFILE typed codes + double contrast coverage |
| 1 (tied) | V-02 | 170 | Upfront catalog; highest C-23 navigability |
| 1 (tied) | V-01 | 170 | Entry gate bidirectionality; cleanest single-axis |
| 5 | V-04 | 167.5 | C-09 PARTIAL: PROFILE quality compressed |

All variations exceed golden threshold (141). All five essential criteria PASS across all variations.

---

## Excellence Signals

Three patterns emerge from the top variations that current rubric criteria do not yet capture:

### Signal 1 — Bidirectional Phase Boundary Enforcement (V-01, V-04, V-05)

Phase exits have been named since R4 (C-16). R8 V-01 adds ENTRY-GATE checks at each receiving phase: `ENTRY-GATE: PARSE-PASS required. If PARSE-PASS not present in prior output, halt: ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS. Re-run PARSE before proceeding.`

Any phase transition is now auditable at both ends — the producing phase emits an exit token, the receiving phase confirms that token before executing. A skill runner cannot produce phase content without both the prior exit and the current entry authorization being visible in output. **Candidate C-25**: phase boundaries must be enforced bidirectionally — exit token emitted by producing phase, entry token confirmed by receiving phase before any phase-content output.

### Signal 2 — Pre-Execution Structural Error Catalog (V-02, V-04, V-05)

R7 V-05 had typed codes inline per phase. R8 V-02 adds a STRUCTURAL-ERROR-CATALOG table before Phase 1 listing all codes, phases, and triggers. Phase bodies reference by name rather than re-define. Result: catalog completeness is auditable by reading the table alone, without reading phase bodies. A new phase that introduces a code absent from the catalog is immediately detectable. **Candidate C-25** (alternate framing): all structural error codes must appear in a catalog table before Phase 1; inline phase declarations must reference rather than re-define catalog entries.

### Signal 3 — Upstream Derivation Phase Enforcement Parity (V-03, V-05)

C-23 and C-24 enforce typed codes at BUILD-VERIFY and WRITE-CHART — the downstream end of the derivation chain. PROFILE is the upstream source: it produces the lens-phrase that IA-WRITTEN confirms at write time and BUILD-VERIFY confirms at verification time. V-03/V-05 add typed codes to PROFILE (STRUCTURAL-ERROR:PROFILE-CATEGORY, PROFILE-LENS-UNDERIVED, PROFILE-DUPLICATE-LENS) with a dedicated violation table and FAIL/PASS contrast pair for defended-artifact quality. The full chain (PROFILE → WRITE-IA → BUILD-VERIFY) now carries typed enforcement at every checkpoint. **Candidate C-26**: upstream derivation phases must use typed STRUCTURAL-ERROR codes with the same precision as downstream verification phases; the derivation chain must be uniformly typed from source to sink.

---

```json
{"top_score": 170, "all_essential_pass": true, "new_patterns": ["bidirectional phase boundary enforcement via ENTRY-GATE tokens at each phase start naming the required prior exit token", "pre-execution STRUCTURAL-ERROR-CATALOG table before Phase 1 making all codes navigable and completeness auditable without reading phase bodies", "upstream derivation phase enforcement parity: PROFILE typed codes (PROFILE-CATEGORY, PROFILE-LENS-UNDERIVED, PROFILE-DUPLICATE-LENS) match downstream verification precision across the full PROFILE->IA-WRITTEN->BUILD-VERIFY chain"]}
```
