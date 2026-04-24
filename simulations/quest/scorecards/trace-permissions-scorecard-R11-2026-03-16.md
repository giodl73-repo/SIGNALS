## trace-permissions Round 13 — Quest Score (Rubric v12, denominator 28)

### Scoring Formula

```
composite = (essential_pass / 5 × 60)
          + (recommended_pass / 3 × 30)
          + (aspirational_pass / 28 × 10)
```

All variations carry the R12-V-05 base: 5/5 essential, 3/3 recommended, 25/28 aspirational. The only variables are C-34, C-35, C-36.

---

### Criterion-by-Criterion: C-34 / C-35 / C-36

**C-34** — Preamble contains a structural axis declaration naming execution order / closure-note format / CS self-reference as orthogonal dimensions with a binding non-interference statement.

**C-35** — SE-4's STRUCTURED CLOSE block contains a TABLE_4 row cross-reference at the SE-0 position; CA-1.9 verifies it as a distinct audit target from CA-1.4 and CA-1.7.

**C-36** — CA terminal verdict contains an explicit tri-dimensional self-evidence attestation naming each R12 dimension and its specific output-body evidence source.

---

### V-01 — Single-axis C-35

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 to C-33 | PASS (25) | R12-V-05 base preserved intact |
| C-34 | **FAIL** | No R12 STRUCTURAL AXIS DECLARATION block in Step 0.2; not targeted |
| C-35 | **PASS** | SE-4 STRUCTURED CLOSE (lines 365–369): "SE-0 cross-reference: TABLE_4 row [...]... it occupies the SE-0 slot of this closure block and is the subject of CA-1.9 verification." CA-1.9 pre-assigned in Step 0.2 (line 186), verified in Phase 3 (lines 443–448) as "distinct audit target from CA-1.4 and CA-1.7" |
| C-36 | **FAIL** | Terminal verdict (lines 450–452) lists CA-1.1–CA-1.9 results only; no TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block |

**Aspirational pass: 26/28**
**Score: 60 + 30 + (26/28 × 10) = 99.3 (26/28)**

---

### V-02 — Single-axis C-34

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 to C-33 | PASS (25) | R12-V-05 base preserved |
| C-34 | **PASS** | Lines 579–598: full R12 STRUCTURAL AXIS DECLARATION table with all three dimensions (Execution order / Closure-note format / CS self-reference), non-interference statement: "Satisfying one dimension does not satisfy or exempt any other" |
| C-35 | **FAIL** | No CA-1.9 (explicit: "CA-1.9 is NOT present in this variation", line 752). SE-4 STRUCTURED CLOSE (lines 728–734) cites SE-0 TABLE_4 row ID but not as an SE-0 slot cross-reference structure; no distinct CA-1.9 verification target |
| C-36 | **FAIL** | Terminal verdict (lines 754–759) cites "R12 Structural Axis Declaration authored in Step 0.2" but no TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block naming each dimension's output-body evidence source |

**Aspirational pass: 26/28**
**Score: 60 + 30 + (26/28 × 10) = 99.3 (26/28)**

---

### V-03 — Single-axis C-36

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 to C-33 | PASS (25) | R12-V-05 base preserved ("No axis declaration block. No CA-1.9.", line 838) |
| C-34 | **FAIL** | No R12 STRUCTURAL AXIS DECLARATION; explicitly not targeted |
| C-35 | **FAIL** | No CA-1.9. SE-4 STRUCTURED CLOSE (lines 904–907): cites SE-0 TABLE_4 row ID generically ("SE-4 STRUCTURED CLOSE cites SE-0 TABLE_4 row ID") but lacks the SE-0 slot structure and distinct CA-1.9 verification row |
| C-36 | **PASS** | Lines 922–938: full TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block. TABLE with R12 Dimension / Label / Specific Output-Body Evidence Source. All three dimensions named with precise output section citations. Closes: "All three dimensions are simultaneously active... No dimension's evidence source overlaps with another's." Dependencies (C-22+C-32+C-33) all met via R12-V-05 base. |

**Aspirational pass: 26/28**
**Score: 60 + 30 + (26/28 × 10) = 99.3 (26/28)**

---

### V-04 — Combined C-34+C-35

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 to C-33 | PASS (25) | R12-V-05 base |
| C-34 | **PASS** | Lines 1022–1039: R12 STRUCTURAL AXIS DECLARATION with CA Verification column mapping each dimension to its verifying CA row (CA-1.4+CA-1.9 / CA-1.7 / CA-1.8). Non-interference: "A model that satisfies one dimension and defers another on coverage grounds fails the non-interference contract." |
| C-35 | **PASS** | CA-1.9 pre-assigned (line 1020). SE-4 STRUCTURED CLOSE (lines 1077–1086): "SE-0 cross-reference: TABLE_4 row [...] This TABLE_4 row cross-reference is the SE-0 slot of this STRUCTURED CLOSE block; it is the subject of CA-1.9 verification and is distinct from the MANUAL GAP block above (CA-1.7) and TABLE_4's SE-0 execution order (CA-1.4)." CA-1.9 in Phase 3 (lines 1099–1104). |
| C-36 | **FAIL** | Terminal verdict (lines 1106–1110): cites Dimension 1/2/3 verification rows and "Non-interference contract active" but no TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block naming output-body evidence sources per C-36 |

**Aspirational pass: 27/28**
**Score: 60 + 30 + (27/28 × 10) = 99.6 (27/28)**

---

### V-05 — Full combination C-34+C-35+C-36

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 to C-33 | PASS (25) | R12-V-05 base |
| C-34 | **PASS** | Lines 1264–1283: R12 STRUCTURAL AXIS DECLARATION with four-column table (Dimension / Label / Structural Property / CA Verification). Non-interference statement names each CA row explicitly: "Verifying CA-1.7 does not verify Dimension 1 or 3. Verifying CA-1.8 does not verify Dimensions 1 or 2. Verifying CA-1.4+CA-1.9 does not verify Dimensions 2 or 3." |
| C-35 | **PASS** | CA-1.9 pre-assigned (line 1262). SE-4 STRUCTURED CLOSE (lines 1432–1438): TABLE_4 row SE-0 slot with inline scope disambiguation "distinct from the MANUAL GAP block above (CA-1.7's scope) and from TABLE_4's execution order at SE-0 (CA-1.4's scope)." CA-1.9 Phase 3 (lines 1511–1516): Registry anchor + Preamble anchor + triple-distinct note. |
| C-36 | **PASS** | Lines 1525–1543: TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block. Each dimension cites phase-labeled output sections (SE-0 header precedes SE-1 / SE-2 opens with exact string / CS-0 contains "Schema ID: CS-2" string). Closes: "This independence is the output-body manifestation of the non-interference declaration in the Phase 0 R12 Structural Axis Declaration" — bidirectional preamble↔attestation loop. All dependencies (C-22+C-32+C-33) met. |

**Aspirational pass: 28/28**
**Score: 60 + 30 + (28/28 × 10) = 100.0 (28/28)**

---

### Final Rankings

| Rank | Variation | Aspirational | Score | Delta from base |
|------|-----------|-------------|-------|-----------------|
| 1 | **V-05** | 28/28 | **100.0** | +1.1 vs R12-V-05 |
| 2 | **V-04** | 27/28 | **99.6** | +0.7 |
| 3 | V-01 | 26/28 | 99.3 | +0.4 |
| 3 | V-02 | 26/28 | 99.3 | +0.4 |
| 3 | V-03 | 26/28 | 99.3 | +0.4 |

All hypotheses confirmed. V-01/V-02/V-03 are indistinguishable at 99.3 because each adds exactly one of the three new criteria. V-04 adds two. V-05 adds all three.

---

### Excellence Signals — V-05

**1. Axis declaration with explicit CA-verification column linkage.** The R12 STRUCTURAL AXIS DECLARATION table in V-05 (and V-04) adds a fourth column naming the specific CA-1.X row(s) that verify each dimension (CA-1.4+CA-1.9 / CA-1.7 / CA-1.8). V-02's axis declaration lacks this column — it names dimensions but doesn't wire them to verification rows in the declaration table itself. The column makes the non-interference contract operationally verifiable, not just declarative.

**2. Inline scope disambiguation inside SE-4 STRUCTURED CLOSE.** V-01/V-04/V-05's SE-0 slot text names all three non-overlapping CA rows *within the STRUCTURED CLOSE block itself* ("distinct from the MANUAL GAP block above [CA-1.7's scope] and from TABLE_4's execution order at SE-0 [CA-1.4's scope]"). This prevents any CA-1.9 verification attempt from conflating the three audit targets — the disambiguation is co-located with the content being audited, not deferred to Phase 3.

**3. Bidirectional preamble↔attestation closure in TRI-DIMENSIONAL block.** V-05's attestation closing line — "This independence is the output-body manifestation of the non-interference declaration in the Phase 0 R12 Structural Axis Declaration" — creates a verifiable chain: C-34's preamble declares independence → C-36's attestation closes the proof in the output body. The attestation doesn't just name evidence sources; it traces its structural legitimacy back to the Phase 0 contract, making the terminal verdict self-grounding.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Axis declaration table with explicit CA-verification-row column linking each dimension to its verifying CA-1.X row(s) in the declaration itself", "Inline three-way scope disambiguation embedded inside SE-4 STRUCTURED CLOSE block co-locating CA-1.9 distinction from CA-1.4 and CA-1.7 at the audited content site", "Bidirectional preamble-to-attestation closure: TRI-DIMENSIONAL block cites the Phase 0 axis declaration as its structural authority, creating a self-grounding proof loop between C-34 and C-36"]}
```
