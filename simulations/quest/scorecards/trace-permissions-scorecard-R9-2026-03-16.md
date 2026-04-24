## trace-permissions — Round 13 Scoring (Rubric v12)

**Date:** 2026-03-17
**Denominator:** 28 criteria | 100 pts (Essential 60 + Recommended 30 + Aspirational 10)
**Aspirational weight:** 10/28 = 0.357 pts per criterion
**Base state:** R12-V-05 = 25/28 (98.9) — all criteria C-01–C-33 pass; C-34/C-35/C-36 missing

---

### Scoring Premise

All five variations are built explicitly on R12-V-05. R12-V-05 scored 25/25 under v11 (all C-01–C-33 pass). The only differentiation across R13 variations is which subset of {C-34, C-35, C-36} each variation activates.

**C-01 through C-33: PASS for all five variations** — no variation removes any R12-V-05 mechanism. Confirmed by inspection:
- C-01–C-05 (Essential): TABLE_1–TABLE_5 + SHALL-A–E + CA-1.1–CA-1.5 present in all
- C-06–C-08 (Recommended): Dataverse terminology, sharing conflict analysis, remediation specificity — all preserved
- C-09–C-16: Defense-in-depth, triple-lock, CA auditor role — all preserved
- C-17–C-23: Preamble matrix, quad-lock, CA-first, Registry, closed loop, phase labels, double-anchor — all preserved
- C-24–C-33: Inline-concatenation prohibition, Tier column, SE-4 citing SE-0, CS-0 acknowledgment — all preserved

---

### New Criterion Scoring (C-34, C-35, C-36)

**C-34** — Preamble contains R12 STRUCTURAL AXIS DECLARATION naming all three dimensions as orthogonal with non-interference statement:

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | No axis declaration block present; Step 0.2 has preamble matrix + SHALLs only; no R12 dimension table | **FAIL** |
| V-02 | Full R12 STRUCTURAL AXIS DECLARATION block after preamble table; 3-row dimension table (label / property / verification); explicit non-interference statement naming which CA rows verify each dimension | **PASS** |
| V-03 | Explicitly marked "No axis declaration block. No CA-1.9." (line 838); Phase 0 identical to R12-V-05 | **FAIL** |
| V-04 | Full axis declaration block identical to V-02 except Dimension 1 verification column names "CA-1.4+CA-1.9"; non-interference statement explicitly cites CA-1.4+CA-1.9, CA-1.7, CA-1.8 per dimension | **PASS** |
| V-05 | Full axis declaration block with CA-1.4+CA-1.9 on Dimension 1; non-interference statement enumerates verifiers per dimension by row ID; binding contract language ("fails this declaration") | **PASS** |

**C-35** — SE-4's STRUCTURED CLOSE block contains TABLE_4 row cross-reference at SE-0 position; CA-1.9 verifies as audit target distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels):

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | SE-4 STRUCTURED CLOSE opens with explicit "SE-0 cross-reference: TABLE_4 row [specific vector]..." slot (lines 365–369); CA-1.9 pre-assigned in Step 0.2 supplementary table and verified in Phase 3 with Registry + Preamble anchors; scope distinction from CA-1.4 and CA-1.7 explicitly stated | **PASS** |
| V-02 | SE-4 STRUCTURED CLOSE (lines 728–734) says "citing the SE-0 TABLE_4 row ID" but lacks the explicit SE-0 slot structure at the STRUCTURED CLOSE opening; Phase 3 says "CA-1.9 is NOT present in this variation" | **FAIL** |
| V-03 | Explicitly states "No TABLE_4 SE-0 slot cross-reference in STRUCTURED CLOSE block beyond the existing citation" (line 895–896); no CA-1.9 | **FAIL** |
| V-04 | Inherits V-01's SE-4 STRUCTURED CLOSE SE-0 slot structure; CA-1.9 pre-assigned in Phase 0 (supplementary table row); CA-1.9 verified in Phase 3 with double-anchor; distinction from CA-1.4 and CA-1.7 stated at both pre-assignment and verification | **PASS** |
| V-05 | Full SE-0 slot cross-reference in SE-4 STRUCTURED CLOSE (lines 1433–1443); CA-1.9 pre-assigned; CA-1.9 Phase 3 verification with "third non-overlapping audit target" distinction statement | **PASS** |

**C-36** — CA terminal verdict contains explicit TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION naming each R12 dimension and its specific output-body evidence source:

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | CA terminal verdict cites CA-1.1 through CA-1.9 plus overall verdict; no tri-dimensional attestation block | **FAIL** |
| V-02 | CA terminal verdict mentions "R12 Axis Declaration non-interference contract: all three dimensions active and non-overlapping" but no named table with per-dimension evidence sources | **FAIL** |
| V-03 | Full TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block (lines 922–938); 3-row table (Dimension / Label / Evidence Source) with specific output-body locators for each dimension; independence statement across dimensions | **PASS** |
| V-04 | Terminal verdict cites R12 Structural Axis Declaration and CA-1.4+CA-1.9, CA-1.7, CA-1.8 by dimension (line 1109–1110); but no TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table with per-dimension output-body evidence sources | **FAIL** |
| V-05 | Full TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table (lines 1532–1536); each row names specific Phase 2 section headers, table structures, or Phase 1 sub-section strings as evidence; attestation explicitly closes loop to CA-1.9 for Dimension 1 evidence; independence of evidence sources across dimensions stated | **PASS** |

---

### Composite Scores

Score = 60 (Essential) + 30 (Recommended) + n × (10/28) where n = aspirational criteria passed

| Variation | C-34 | C-35 | C-36 | n (aspirational) | Score | Rank |
|-----------|------|------|------|-----------------|-------|------|
| V-01 | FAIL | PASS | FAIL | 26 | 60 + 30 + 9.286 = **99.3** | T-2 |
| V-02 | PASS | FAIL | FAIL | 26 | 60 + 30 + 9.286 = **99.3** | T-2 |
| V-03 | FAIL | FAIL | PASS | 26 | 60 + 30 + 9.286 = **99.3** | T-2 |
| V-04 | PASS | PASS | FAIL | 27 | 60 + 30 + 9.643 = **99.6** | 2 |
| V-05 | PASS | PASS | PASS | 28 | 60 + 30 + 10.000 = **100.0** | 1 |

---

### V-05 Excellence Signals

**1. Dual-verifier named in axis declaration** — V-05's R12 STRUCTURAL AXIS DECLARATION explicitly names "CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref)" as the combined verifier for Dimension 1. This makes the axis declaration self-consistent with the CA-1.9 addition: the declaration is the reason CA-1.9 exists, not an afterthought. V-02's declaration names only "CA-1.4" for Dimension 1 (missing CA-1.9), weakening the contract.

**2. Attestation table closes loop to prior verification rows** — V-05's Dimension 1 evidence source says "the specific row is identified by CA-1.9 verification above." This threads the terminal attestation back to a named CA-1 row in the same output, making the attestation a structural summary of prior verification rather than a standalone prose claim.

**3. Terminal verdict names axis declaration as a third cited structural basis** — V-05's CA Format Compliance Verdict cites "R12 Structural Axis Declaration (Step 0.2, Phase 0)" as a distinct citation alongside the Schema Registry and preamble. V-03 omits this because it has no axis declaration. This closes the chain: CA authored the declaration; CA's terminal verdict cites its own declaration as one of three structural bases.

**4. Non-interference statement enumerates per-dimension verifiers** — "Verifying CA-1.7 (Dimension 2) does not verify Dimension 1 or Dimension 3" — V-05 names each verifier and explicitly states what it does not verify. This converts the non-interference statement from a general assertion into a per-dimension falsifiable contract.

**5. Three-row evidence table over prose** — All three evidence sources in the attestation are in a table row, not prose paragraphs. Each row is independently locatable: a model or reviewer can check Dimension 2 without reading Dimensions 1 or 3. V-03 uses the same pattern, but V-05 is the version where all three active mechanisms (C-34+C-35+C-36) are simultaneously present and cross-referencing each other.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["dual-verifier axis declaration — naming CA-1.4+CA-1.9 as co-verifiers of Dimension 1 inside the declaration itself makes the new CA row structurally load-bearing from Phase 0", "attestation-to-verification closure — terminal attestation evidence source explicitly cross-references the CA-1 row that verified it, making attestation a structural summary not a parallel claim", "axis declaration cited in terminal verdict — CA terminal verdict cites R12 Structural Axis Declaration as a named structural basis alongside Registry and preamble, closing the authorship chain"]}
```
