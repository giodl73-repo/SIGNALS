**R8 variations written** to:
- `simulations/quest/golden/corps-build-variate-R8-2026-03-16.md`
- `simulations/quest/variations/corps-build-variations-R8-2026-03-16.md`

---

## Variate R8 -- corps-build Summary

**Baseline:** R7 V-04 and V-05 both scored 100/100 on rubric v7. All 23 criteria reachable. R8 explores three axes that were untouched at the 100-point ceiling.

### Variation Axes

| V | Axis | Hypothesis |
|---|------|-----------|
| V-01 | **Lifecycle emphasis** (base: V-04 R7) | `PHASE-ENTERED` / `PHASE-EXITED` tokens at every phase boundary make entry preconditions structural assertions rather than implied by gate ordering. Candidate C-24. |
| V-02 | **Inertia framing** (base: V-05 R7) | `ARTIFACT-D` resistance landscape table derived verbatim from PROFILE entries, sealed with A/B/C, and transcribed into org-chart.md as a sixth section. TRANSCRIPTION-RECEIPT and TRANSCRIPTION-CLEAR cover all four artifacts. Candidate C-25. |
| V-03 | **Role sequence** (base: V-04 R7) | WRITE-ROLES splits into three named passes: `PASS-EXEC` / `PASS-SHARED` / `PASS-TEAM`, each with its own receipt token. A merged single-pass WRITE-ROLES is structurally undifferentiated. Candidate C-26. |
| V-04 | Lifecycle + inertia framing combined | PROFILE-before-CONTRACT ordering (required for ARTIFACT-D derivation) + PHASE-ENTERED/PHASE-EXITED + four-artifact TRANSCRIPTION-RECEIPT/CLEAR. |
| V-05 | Full integration | V-05 R7 base + all three axes. Six org-chart.md sections. Causal chain traced: profiles as causal source of both ARTIFACT-D and IA role files. Highest-signal variation for rubric extraction. |

### Key Structural Decisions

- **V-02/V-04/V-05**: ARTIFACT-D is produced in the CONTRACT phase *from* PROFILE entries (not independently) — making it a derived artifact. This is only possible in PROFILE-before-CONTRACT ordering (V-05 R7's architecture), which is why V-04 R8 reorders to match.
- **TRANSCRIPTION-CLEAR expansion**: Adding ARTIFACT-D raises the four-artifact threshold. C-21's "fewer than three artifacts" rule would become "fewer than four artifacts" in any v8 criterion extracted from this.
- **V-01 exemption**: PHASE-ENTERED/PHASE-EXITED adds no semantic content — only structural lifecycle visibility. This should score 100 on rubric v7 with a potential new pattern for extraction.
 TRANSCRIPTION-RECEIPT
audits all four. TRANSCRIPTION-CLEAR re-audits all four. FINAL SUMMARY leads with
`resistance-landscape:` row. All other structure from V-05 R7 preserved unchanged. Pure
single-axis variation.

**V-03 (role sequence axis, base = V-04 R7):** One modification to V-04 R7: WRITE-ROLES
splits into three named passes in fixed order: PASS-EXEC (exec office roles, receipt:
EXEC-WRITTEN), PASS-SHARED (shared group roles, receipt: SHARED-WRITTEN), PASS-TEAM
(team-level standard and specialized, receipt: TEAM-PASS-WRITTEN). ROLES-COMPLETE
aggregates all three receipts. A correct WRITE-ROLES names all three passes; a phase
that merges them into a single undifferentiated pass is structurally undifferentiated.
FINAL SUMMARY role-files row shows EXEC+SHARED+TEAM-PASS breakdown. All other structure
from V-04 R7 preserved unchanged. Pure single-axis variation.

**V-04 (lifecycle + inertia framing, combined):** V-04 R7's step architecture adapted to
PROFILE-before-CONTRACT ordering (required for ARTIFACT-D derivation from profiles) plus
PHASE-ENTERED/PHASE-EXITED at every boundary plus ARTIFACT-D in CONTRACT and SEAL. Phase
sequence: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL -> WRITE-IA ->
WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF. TRANSCRIPTION-RECEIPT and
TRANSCRIPTION-CLEAR cover all four artifacts. All declarative correctness rules from V-04
R7 preserved; added for ARTIFACT-D and four-artifact TRANSCRIPTION-CLEAR. CHART-PATH
emission preserved.

**V-05 (full integration, base = V-05 R7):** All three R8 axes on V-05 R7's architecture.
PHASE-ENTERED/PHASE-EXITED + ARTIFACT-D resistance landscape + named write passes. Six
org-chart.md sections. Four-artifact TRANSCRIPTION-RECEIPT and TRANSCRIPTION-CLEAR.
Declarative correctness rules for all blocks including ARTIFACT-D and named passes. FINAL
SUMMARY traces causal chain: "profiles are causal source of ARTIFACT-D and IA role files."
Highest-signal variation for rubric extraction.
