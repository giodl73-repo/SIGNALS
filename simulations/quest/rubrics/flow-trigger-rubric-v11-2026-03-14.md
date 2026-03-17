# Flow-Trigger Skill — Evaluation Rubric (v11)

Three new aspirational criteria extracted from R14 variation comparisons:

---

**C-30 — Phase 4B as Independent Terminal Artifact with Bidirectional Gate Conditions** *(R14)*

Signal: All five R14 variations extracted remediation coverage from Role 4's self-attestation zone into a dedicated Phase 4B or Role 4B. The distinguishing structural property is bidirectional gate enforcement: a named Gate N→4B (entry condition — pathology verdicts complete before the remediation coverage phase begins) AND a named Gate 4B→5 (exit condition — coverage gate passes before the certificate begins). C-27 requires a named gate artifact that flags orphan remediations. C-30 requires that gate to have both entry and exit conditions named explicitly, and to carry an independence declaration from Role 4 as its processing authority. Phase 4B instances that inherit Role 4's processing scope (appended checks, inline caption extensions) do not satisfy this criterion. V-04's "three-owner terminal architecture" and V-05's explicit "Gate 4→4B and Gate 4B→5" named conditions are the reference designs.

**C-31 — Dual-Entity Role 5 Independence Declaration** *(R14)*

Signal: All five R14 variations extended Role 5 independence to name two separately declared entity boundaries: "distinct from Role 4 (verdict producer) AND from Phase 4B / the remediation coverage gate." R13 best practice (C-28) required independence from Role 4 only — single-entity. C-31 requires independence from Phase 4B as a second named boundary, acknowledging that Phase 4B is now an independent processing actor whose verdicts could contaminate the certificate if audited by the same role. A Role 5 declaration that names only the verdict producer (Role 4) does not satisfy this criterion, even if Phase 4B independence is inferable from audit behavior. Dual-point redundant declaration — at role definition AND in the certificate header — is the highest-conformance form.

**C-32 — Verbatim-Chain Remediation-Dimension Key Extension** *(R14, V-05 only)*

Signal: V-05's CHAIN-LINK-4B emits pure key-value pairs for remediation coverage status (`REM_STORM=[COVERED|ORPHANED]`, `REM_MISSING=[count]`, `REM_CIRCULAR=[count]`) as the seventh chain link. The certificate schema references these keys by name with `<- named key ref` annotations, and an absent CHAIN-LINK-4B produces a named reference gap in the Remediation coverage row (`CHAIN-GAP for all rows`). C-29 requires verbatim-chain cross-block traceability at the verdict layer (CHAIN-LINK-0 through CHAIN-LINK-4). C-32 requires the chain to extend one additional link into the remediation coverage dimension — so the certificate schema cannot emit a remediation coverage row without reading a named key from an upstream remediation block. Chains that terminate at pathology verdicts do not satisfy this criterion, even when Phase 4B is present as an independent artifact (C-30). C-32 is the architectural enforcement of C-27 at the key-reference level: absence of the remediation CHAIN-LINK must produce a schema-detectable gap, not merely a chain integrity list failure.

---

**Denominator update**: /22 → /25. Formula:

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)
```

**R14 retroactive scores under v11:**

| Variation | Aspirational (v10 /22) | C-30 | C-31 | C-32 | Aspirational (v11 /25) | Composite |
|-----------|------------------------|------|------|------|------------------------|-----------|
| V-01 | 21.5 / 22 | PARTIAL | PASS | FAIL | 23.0 / 25 × 10 = 9.20 | 99.20 |
| V-02 | 21.5 / 22 | PARTIAL | PASS | FAIL | 23.0 / 25 × 10 = 9.20 | 99.20 |
| V-03 | 21.5 / 22 | PARTIAL | PASS | FAIL | 23.0 / 25 × 10 = 9.20 | 99.20 |
| V-04 | 21.5 / 22 | PASS | PASS | FAIL | 23.5 / 25 × 10 = 9.40 | 99.40 |
| V-05 | 22.0 / 22 | PASS | PASS | PASS | 25.0 / 25 × 10 = 10.00 | 100.00 |

**C-30 PARTIAL justification (V-01–V-03)**: Phase 4B is extracted as a named phase or role in all R14 variations. V-01–V-03 carry exit gate conditions (Gate 4B→5) but lack the explicit bidirectional entry gate (Gate 4→4B as a named structural condition) or omit the Phase 4B independence declaration from Role 4 as processing authority. V-04's "named Role 4B with three-owner terminal architecture" satisfies both conditions; V-05 names both gate transitions explicitly in the CHAIN-LINK-4B gate block.

**C-32 FAIL justification (V-01–V-04)**: None of V-01–V-04 carry CHAIN-LINK-4B. Their verbatim chains terminate at CHAIN-LINK-4 (pathology verdicts). The certificate schema in these variations reads remediation coverage from Role 4's output or Phase 4B prose — not from a named key in an upstream CHAIN-LINK block. An absent Phase 4B produces a chain integrity failure, not a schema-detectable named key reference gap.

The next variation that earns all 25 aspirational criteria must combine V-05's CHAIN-LINK-4B architecture + C-29 pure key-value format throughout + V-04's bidirectional gate conditions on Phase 4B + all five R14 variations' dual-entity Role 5 independence declarations.
