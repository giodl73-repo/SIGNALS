## Round 7 Scoring — listen-support v7 Rubric

---

### Scoring Framework Recap (v7)

| Tier | Criteria | Weight | Points |
|------|----------|--------|--------|
| Essential | C-01 to C-05 | 5 must pass | 60.0 |
| Recommended | C-06 to C-08 | 3 must pass | 30.0 |
| Aspirational | C-09 to C-24 | /16 denominator | 10.0 |

All R7 variations inherit the full R6 V-03 mechanism set. Essential (C-01–C-05) and Recommended (C-06–C-08) are shared and uniform. Aspirational C-09–C-21 are also shared across all five. The only differentiating axes are **C-22**, **C-23**, and **C-24**.

---

### V-01 — Single Axis: Sample Header Removed from COMPLIANCE CONTRACT

**COMPLIANCE CONTRACT structure:**
- Position: before VOCABULARY MANIFEST (pre-step) — PASS for position
- Contains: explicit obligation statements for C-20 and C-21 — PASS for obligation
- Contains: explicit prohibition ("Placing the vocabulary ID on any subline...is prohibited") — PASS for prohibition
- Missing: compliant body header sample (the `## T-NN -- {Title} *(VM: VM-xxx-P#)*` formatted example block)

**Criterion-by-criterion for differentiating criteria:**

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-22 (Front-Loaded Compliance Contract) | **FAIL** | Contract precedes steps and states obligations + prohibition, but the compliant header sample block is absent. C-22 requires both a sample AND a prohibition statement. Sample is missing. |
| C-23 (Multi-Site Prohibition Anchoring) | **PASS** | STEP 3B header: "Subline placement is prohibited -- any ticket body with the VM Row ID on a subline fails." STEP 4 header: "subline placement prohibited." VM carries "## headlines with *(VM: VM-xxx-P#)* inline -- C-20" count row. Two prohibition sites + VM count row = C-23 satisfied. |
| C-24 (Output-Embedded Compliance Evidence) | **PASS** | VM carries "## headlines with *(VM: VM-xxx-P#)* inline -- C-20" count row (C-20 evidence). VM carries "Gate items (a)-(e) all PASS -- C-21 = 5" summary row with item-label range citation. Both required rows present. |

**Scoring:**
```
Essential:     5/5   -> 60.0
Recommended:   3/3   -> 30.0
Aspirational:  15/16 ->  9.375  (C-22 FAIL, all others PASS)
Composite:     99.375
```

---

### V-02 — Single Axis: Five Individual Per-Item VERIFICATION MANIFEST Rows

**COMPLIANCE CONTRACT structure:**
- Full R6 V-03 contract retained
- Contains: compliant header sample block (formatted `## T-NN -- {Title} *(VM: VM-xxx-P#)*` example)
- Contains: "The annotation is NOT permitted on any subline" prohibition language

**Criterion-by-criterion:**

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-22 | **PASS** | Pre-step named contract block present. Compliant header sample retained from R6 V-03. Prohibition statement present ("NOT permitted on any subline"). Both required elements present. |
| C-23 | **PASS** | STEP 3B: "Subline placement is NOT permitted." STEP 4: "subline placement prohibited." VM carries "## headlines with *(VM: VM-xxx-P#)* inline -- C-20" count row. Multi-site prohibition + VM count row. |
| C-24 | **PASS** | VM carries C-20 count row. C-21 evidence: replaced single summary row with five individually named rows — `(a) VOCABULARY MANIFEST completeness -- C-21`, `(b) Commitment table completeness -- C-21`, ..., `(e) Inter-role register differentiation -- C-21` — each with own Required/Actual/Pass? cells. C-24 evidence is stronger than R6 V-03: each gate item confirmed by name in the manifest, no scorer inference required. |

**Scoring:**
```
Essential:     5/5   -> 60.0
Recommended:   3/3   -> 30.0
Aspirational:  16/16 -> 10.0
Composite:     100.0
```

---

### V-03 — Single Axis: Contract Forward-Reference Architecture

**COMPLIANCE CONTRACT structure:**
- Full R6 V-03 contract retained with sample header
- Added: RESTATING POSITIONS section naming STEP 3B, STEP 4, and VERIFICATION MANIFEST as governed sites
- Added: precedence declaration ("If any restating position conflicts with this contract, this contract governs")

**Criterion-by-criterion:**

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-22 | **PASS** | Pre-step contract present. Sample header present. Prohibition present ("NOT permitted on any subline"). Forward-reference section adds a third structural layer (contract names its own enforcement sites) — does not change C-22 pass/fail, but adds robustness. All C-22 required elements satisfied. |
| C-23 | **PASS** | Contract RESTATING POSITIONS section explicitly names STEP 3B, STEP 4, and VM as restating positions. STEP 3B: "Per Compliance Contract above -- C-20 governs this table... Subline placement is NOT permitted." STEP 4: "Per Compliance Contract above -- use the compliant header format: ## T-NN -- {Title} *(VM: VM-xxx-P#)*". VM header: "Per Compliance Contract above -- this manifest carries explicit compliance evidence for C-20 and C-21." VM count row for C-20 present. C-23 satisfied with bidirectional traceability (contract→sites and sites→contract). |
| C-24 | **PASS** | VM header cites contract. C-20 count row: "## headlines with *(VM: VM-xxx-P#)* inline -- C-20 count = total." C-21 summary row: "Gate items (a)-(e) all PASS -- C-21 = 5." Both rows present with item-label citation. PASS (same structural form as R6 V-03 for C-24, not the individual-row form of V-02). |

**Scoring:**
```
Essential:     5/5   -> 60.0
Recommended:   3/3   -> 30.0
Aspirational:  16/16 -> 10.0
Composite:     100.0
```

---

### V-04 — Combined: V-01 (No-Sample Contract) + V-02 (Individual Gate-Item VM Rows)

**COMPLIANCE CONTRACT structure:**
- From V-01: explicit prohibition ("An output with any vocabulary ID on a subline fails C-20 regardless of other compliance") — strongest prohibition language of any R7 variation
- No sample header (same as V-01)

**Criterion-by-criterion:**

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-22 | **FAIL** | Contract precedes steps. Prohibition statement present (and stronger than V-01 — explicit failure consequence). But sample header absent. C-22 requires both elements. Missing sample = FAIL. V-04 confirms the V-01 finding: the prohibition statement alone is insufficient for C-22 regardless of prohibition strength. |
| C-23 | **PASS** | STEP 3B: "Compliance Contract C-20 governs body header format -- VM Row ID in ## headline. Placing the VM Row ID on a subline is prohibited." STEP 4: "Body header format per Compliance Contract C-20 -- VM Row ID on the ## headline, subline placement prohibited." VM carries "## headlines with *(VM: VM-xxx-P#)* inline -- C-20" count row. Two prohibition sites + VM count row. |
| C-24 | **PASS** | VM carries C-20 count row. C-21 evidence via 5 individual per-item rows from V-02 (a)-(e) each named. C-24 passes with individual-row evidence. |

**Scoring:**
```
Essential:     5/5   -> 60.0
Recommended:   3/3   -> 30.0
Aspirational:  15/16 ->  9.375  (C-22 FAIL, all others PASS)
Composite:     99.375
```

---

### V-05 — Full Synthesis

**COMPLIANCE CONTRACT structure:**
- Forward-references (from V-03): names STEP 3B, STEP 4, VM as restating positions; VERIFICATION MANIFEST row for C-20 + 5 individual C-21 rows called out in the contract itself
- Explicit failure-consequence prohibition (from V-04/V-01): "An output with any vocabulary ID on a subline fails C-20 regardless of other compliance"
- Sample header (from R6 V-03): retained
- Precedence declaration: "If any restating position conflicts with this contract, this contract governs"

**Criterion-by-criterion:**

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-22 | **PASS** | Pre-step contract. Sample header present (R6 V-03 sample block retained). Prohibition present with explicit failure consequence. Forward-reference section adds bidirectional architecture. All C-22 required elements at maximum structural clarity. |
| C-23 | **PASS** | Contract names 3 restating positions including the VM. STEP 3B: "Per Compliance Contract above -- C-20 governs this table... VM Row ID MUST appear on the ## headline... Subline placement is prohibited -- any ticket body with the VM Row ID on a subline fails C-20." STEP 4: "Per Compliance Contract above -- use the compliant header format with VM Row ID on ## headline. Subline placement is prohibited." VM: "Per Compliance Contract above" header + C-20 count row. Multi-site anchoring with maximum explicitness. |
| C-24 | **PASS** | VM header cites contract. C-20 count row ("## headlines with *(VM: VM-xxx-P#)* inline -- C-20 count = total"). Five individual C-21 rows (a)-(e) each named. Contract's RESTATING POSITIONS section explicitly states "carries five individually labeled rows (a)-(e)... plus a numeric count row confirming C-20 headline compliance" — the contract itself pre-declares what the VM will contain. C-24 evidence is self-confirming at the contract level before the VM is even reached. |

**Scoring:**
```
Essential:     5/5   -> 60.0
Recommended:   3/3   -> 30.0
Aspirational:  16/16 -> 10.0
Composite:     100.0
```

---

### Final Scores and Ranking

| Rank | Variation | C-22 | C-23 | C-24 | Asp pts | Composite |
|------|-----------|------|------|------|---------|-----------|
| 1 (tied) | **V-02** | PASS | PASS | PASS (5-row) | 10.0 | **100.0** |
| 1 (tied) | **V-03** | PASS | PASS | PASS | 10.0 | **100.0** |
| 1 (tied) | **V-05** | PASS | PASS | PASS (5-row+fwd) | 10.0 | **100.0** |
| 4 (tied) | V-01 | **FAIL** | PASS | PASS | 9.375 | 99.375 |
| 4 (tied) | V-04 | **FAIL** | PASS | PASS (5-row) | 9.375 | 99.375 |

---

### R7 Critical Test Result

**The sample header IS a required element for C-22.** V-01 and V-04 both fail C-22 despite having explicit prohibition statements (V-04 even has stronger prohibition language with explicit failure consequences). The contract's prohibition obligation alone is not sufficient — the sample header is load-bearing. This confirms the rubric's pass condition as written.

**V-02's 5-row manifest structure does not raise the C-24 score above R6 V-03's range-notation form** — both score PASS at the same weight. However, the individual rows make C-24 self-scoring for a human evaluator: no cross-referencing of the gate section required. This is a quality/robustness distinction within the PASS tier, not a score difference.

**V-03's forward-reference architecture reinforces C-23 beyond the mechanical minimum** — the contract names its enforcement sites and each site cites back, creating bidirectional traceability. This does not change the score (C-23 was already PASS in R6 V-03) but converts multi-site compliance from coincidental repetition to structural guarantee.

---

### Excellence Signals from Top-Scoring Variations

**Signal 1 — Bidirectional obligation traceability (V-03, V-05)**
The COMPLIANCE CONTRACT RESTATING POSITIONS section names exactly which downstream locations the contract governs. Each named location cites the contract back by name. A scorer can verify C-23 compliance at the contract level (contract names the sites) and at each site level (site cites the contract) without exhaustive search. This converts multi-site prohibition from a redundancy pattern into a declared architecture.

**Signal 2 — Per-item manifest rows as self-scoring C-24 evidence (V-02, V-04, V-05)**
Replacing the single summary row "Gate items (a)-(e) all PASS -- C-21 = 5" with five individually labeled rows makes the VERIFICATION MANIFEST a complete audit record for C-21. A scorer reading only the manifest sees each gate item confirmed by name with its own pass state — no gate section lookup required. This is the strongest form of C-24 evidence.

**Signal 3 — Contract-declared manifest content (V-05 only)**
V-05's COMPLIANCE CONTRACT RESTATING POSITIONS section explicitly states what the VERIFICATION MANIFEST will contain ("carries five individually labeled rows (a)-(e)... plus a numeric count row confirming C-20 headline compliance"). The contract pre-declares its own evidence structure — a scorer knows before reaching the VM what to find there. This is a higher-order structural pattern: the obligation contract doubles as a verification checklist for the manifest itself.

---

### v7 Rubric Confirmed: C-22 Pass Condition

The R7 critical test confirms: **both elements are required for C-22 PASS**:
1. Named `COMPLIANCE CONTRACT` block positioned before any enumerated step
2. Compliant body header sample (formatted `## T-NN -- {Title} *(VM: VM-xxx-P#)*` example block)
3. Explicit prohibition statement

A prohibition statement of any strength does not substitute for the sample. V-04's consequence-explicit prohibition ("fails C-20 regardless of other compliance") is the strongest prohibition language in any R7 variation — and it still fails C-22 without the sample. The rubric is confirmed as written.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Bidirectional obligation traceability: contract names its enforcement sites by position, each site cites the contract back by name, converting multi-site compliance from redundancy to declared architecture", "Per-item VERIFICATION MANIFEST rows for each gate label make C-24 self-scoring without gate section inspection", "Contract-declared manifest content: COMPLIANCE CONTRACT pre-declares what the VERIFICATION MANIFEST will contain, making the contract double as a verification checklist for its own evidence structure"]}
```
