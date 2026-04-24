- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor — Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 — verifying...
- Verification — Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? -> PASS / FAIL

**CA-1.4** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6** *(SHALL-F compliance)*:
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected field, SE-Actual field, Delta field] — all three required per SHALL-F declaration in Phase 0.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7** *(SHALL-G compliance)*:
- Registry anchor — CONTEXT section exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G requires two-part blocks with exact label in brackets.
- Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails; single-line annotation fails; CA-1.7 verifies.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? Followed by `STRUCTURED CLOSE:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8** *(CS-0 acknowledgment + CS-2/CS-3 Schema Registry registration)*:
- Registry anchor — Schema Registry declared CS-2 as a named schema entry with SE-updatable columns SE Cross-Reference and SE Confirmation and SE-update protocol co-located. Schema Registry declared CS-3 same. PHASE 1 mandate requires CS-0 sub-section to acknowledge both schema IDs and list SE-updatable columns before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 are Schema Registry entries alongside TABLE_1-5. CS-0 acknowledgment is a PHASE 1 structural requirement: CS cites both schema IDs and SE-updatable columns before authoring expectation rows. CA-1.8 verifies.
- Verification — CS-2 in Schema Registry with SE-updatable column declarations? CS-3 same? CS-0 present before CS-1? CS-0 cites "Schema ID: CS-2" by exact label? CS-0 cites "Schema ID: CS-3" by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA-1.9 — SHALL-H + D-2 vocabulary match verification** *(D-2 axis; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: Sharing rules row (Row 2, Vector = "Sharing rules") is the designated SE-0 cross-reference target for SE-4 STRUCTURED CLOSE as declared in Phase 0 Step 0.1. The evidence token "TABLE_4 Sharing rules row (SE-0):" was registered as a named SE-0 output addressable by its Vector value.
- Preamble anchor — SHALL-H and D-2 axis Output-Body Evidence Token as authored by CA in Phase 0: SE-4 STRUCTURED CLOSE MUST output the literal prefix "TABLE_4 Sharing rules row (SE-0):" as its first citation element before the cross-tier differential summary. This token is the D-2 output-body evidence as declared in the R12 Orthogonal Dimensions Declaration table. CA-1.9 verifies the exact vocabulary match between the D-2 preamble declaration and the SE-4 STRUCTURED CLOSE output — a distinct audit target from CA-1.4 (TABLE_4 placement before SE-1) and CA-1.7 (MANUAL GAP exact-label accuracy).
- Verification — SE-4 STRUCTURED CLOSE contains the literal prefix "TABLE_4 Sharing rules row (SE-0):" as its first citation element? The prefix appears before (not after, not embedded within) the cross-tier differential summary? Vocabulary matches the D-2 token declared in Phase 0 R12 Dimensions table exactly? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation + R12 Tri-Dimensional Self-Evidence Attestation:**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). CS-0 acknowledgment (CA-1.8). SHALL-H + D-2 vocabulary match (CA-1.9). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**R12 Tri-Dimensional Self-Evidence Attestation:**
Each R12 dimension is attested as PRESENT in this output. Status is pre-declared ATTESTED for
all three dimensions. The CA confirms each dimension by locating its evidence token at the
"Verify at:" output-body section. If the evidence token is absent at the stated location, CA MUST
change that row's CA Confirmation to NON-COMPLIANT and attribute the gap to the responsible phase.

| Dimension | ID | Required Status | Verify at (output-body section) | Evidence Token | CA Confirmation |
|-----------|----|-----------------|---------------------------------|----------------|-----------------|
| Execution order | D-1 | ATTESTED | PHASE 0 section header + Step 0.2 close + Phase 3 CA-1 rows | "PHASE 0 — CA:" header present in output body; "Handing to PHASE 1 — CS" handoff string at Step 0.2 close; "(Phase 0 M4 pre-assignment CA-1.x)" provenance label on each CA-1 row above | ATTESTED — D-1 evidence tokens confirmed at Phase 0 header, Step 0.2 handoff string, and CA-1.x provenance labels / NON-COMPLIANT — [missing element, attributed to CA Phase 0] |
| Closure-note format | D-2 | ATTESTED | SE-4 STRUCTURED CLOSE section | Literal prefix "TABLE_4 Sharing rules row (SE-0):" appearing as the first citation element in SE-4 STRUCTURED CLOSE — confirmed by CA-1.9 PASS above | ATTESTED — D-2 evidence token "TABLE_4 Sharing rules row (SE-0):" confirmed at SE-4 STRUCTURED CLOSE per CA-1.9 / NON-COMPLIANT — CA-1.9 FAIL; attributed to SE Phase 2 SE-4 |
| CS self-reference | D-3 | ATTESTED | CS-0 sub-section | "Schema ID: CS-2 — Sharing Rule Expectations" and "Schema ID: CS-3 — Cross-Role Access Differential Expectations" present in CS-0 before first CS-1/CS-2/CS-3 row — confirmed by CA-1.8 PASS above | ATTESTED — D-3 evidence tokens confirmed at CS-0 per CA-1.8 / NON-COMPLIANT — CA-1.8 FAIL; attributed to CS Phase 1 CS-0 |

Overall tri-dimensional attestation: ATTESTED (all three D-1/D-2/D-3 evidence tokens confirmed
in output body at stated locations) / NON-COMPLIANT (one or more dimensions failed — see CA
Confirmation column for phase attribution).
```

---

## Scoring Prediction (R7 vs R6)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-34 (preamble axis declaration) | **+** FM-1 fix | — | — | **+** FM-1 fix | **+** FM-1 fix |
| C-35 (SE-4 STRUCTURED CLOSE row cross-ref + CA-1.9) | — | **+** FM-2 fix | — | **+** FM-2 fix | **+** FM-2 fix |
| C-36 (tri-dimensional terminal attestation) | partial (output-body check exists but conditional) | — | **+** FM-3 fix | — | **+** FM-3 fix |
| Predicted score | 26/28 | 26/28 | 26/28 | 27/28 | **28/28** |

**Key diagnostic signal:** If V-04 scores 27/28 (fails C-36) and V-05 scores 28/28, all three failure modes were correctly identified. If V-05 still fails any of C-34/C-35/C-36, the remaining failure mode is isolated in whichever single-axis variation (V-01/V-02/V-03) also fails — narrowing the next round's fix target.

**Path to rubric update:** Once V-05 achieves 28/28, propose C-37: the CA verdict MUST cross-reference CA-1.9's PASS result as the D-2 attestation basis — making the attestation table and the CA-1.9 verification row explicitly co-dependent rather than structurally parallel.
