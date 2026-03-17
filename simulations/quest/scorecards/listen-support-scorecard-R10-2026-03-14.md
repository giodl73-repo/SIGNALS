Now I have everything needed. Let me score all five variations.

---

## listen-support Round 10 — Variation Scorecard

**Rubric**: v10 (205 pts) | **New criteria**: C-30, C-31 | **Base**: R9 V-05 at ceiling on C-01–C-29

---

### Scoring Context

All five variations inherit the full R9 V-05 mechanism set for C-01 through C-29. The baseline is clean at 195 pts before C-30 and C-31 are applied. The only structural differences between variations are:

- **C-30** (5 pts): Is a genuine paraphrase gate present with explicit "do not proceed" language, and where does it fire?
- **C-31** (5 pts): Does Part C of Pass 2 contain both sub-checks — (1) inference scan per ticket, and (2) switching-friction field completeness as a verified output property?

---

### V-01 — Named Block Without Gate Language

**Axis**: C-30 gate strength weak. STEP 2C includes `INFERENCE RULE (stated):` named block but no explicit "Do not proceed to Step 3 until this block is filled" instruction. All C-31 mechanisms from R9 V-05 intact (both sub-checks in Part C with prose acknowledgment).

| ID | Pts | Result | Evidence |
|----|-----|--------|----------|
| C-01 | 12 | PASS | All five fields present — inherited from R9 V-05 |
| C-02 | 12 | PASS | Controlled vocabulary enforced — inherited |
| C-03 | 12 | PASS | Stock roles + persona-voice bodies — inherited |
| C-04 | 12 | PASS | Three sub-sections in Step 7 — inherited |
| C-05 | 12 | PASS | Eight tickets, five category values — inherited |
| C-06 | 10 | PASS | Inference rule constrains P2/P3 Phase 1 and P0/P1 Phase 3 |
| C-07 | 10 | PASS | Volume differentiated across high/medium/low via 4B audit |
| C-08 | 10 | PASS | Performance-mode declaration + first-person enforcement |
| C-09–C-29 | 5 ea. | PASS ×21 = 105 | Full R9 V-05 mechanism set: Step 6 flat format, Step 8 dual-pass, Step 4 pre-commitment, phase-body templates, inertia competitor, Step 2C rule text, Step 7 switching-friction sub-section — all present and unchanged |
| **C-30** | **5** | **FAIL** | Block labeled `INFERENCE RULE (stated):` exists but no gate language. No "do not proceed until filled" instruction. Model reads the block as a formatting slot — satisfied by verbatim copy or minimal rephrasing. Demonstrated encoding not required by prompt structure. |
| **C-31** | **5** | **PASS** | Both sub-checks present in Part C: (1) inference scan — Phase 1 P0/P1 flagged with outage test; Phase 3 P3 flagged with blocking test; compliance state required. (2) switching-friction field completeness — Migrating from: field check present in Part C closing statement. |

**V-01 Score: 200 / 205**
All essential: YES

---

### V-02 — C-30 Gate Relocated to Step 4 Header (Decision-Adjacent)

**Axis**: C-30 gate placement moved to Step 4 header. STEP 2C has full imperative rule text with "Read and accept this rule before proceeding to Step 3" but NO paraphrase block. Step 4 opens with: "Before filling any severity cell, state the inference rule from Step 2C in your own words. Do not fill the table until this line is written: `INFERENCE RULE (stated): [...]`". C-31 Part C unchanged from R9 V-05.

| ID | Pts | Result | Evidence |
|----|-----|--------|----------|
| C-01–C-29 | — | PASS all | Same R9 V-05 baseline; Step 2C retains imperative rule, STEP 2B/3/4/5/6/7/8 all intact |
| Essential (C-01–C-05) | 60 | PASS | — |
| Recommended (C-06–C-08) | 30 | PASS | — |
| Aspirational C-09–C-29 | 105 | PASS | — |
| **C-30** | **5** | **PASS** | Gate language present at Step 4 header: "Do not fill the table until this line is written." Paraphrase fires immediately before severity column — the paraphrase is the live preceding generation context when the model assigns severity values. Temporal coupling is tighter than STEP 2C placement (no STEP 3 prose to traverse between paraphrase and decision). |
| **C-31** | **5** | **PASS** | Part C has both sub-checks. Sub-check 1: Phase 1 scan for P0/P1 with outage test; Phase 3 scan for P3 with blocking test; explicit compliance state. Sub-check 2: Switching-Friction Gaps sub-section existence + Migrating from: verbatim check — confirmed in Part C closing statement (line 673). C-31 requires both sub-checks as Part C properties; both are present. |

**V-02 Score: 205 / 205**
All essential: YES

---

### V-03 — C-31 Part C Minimal (Inference Scan Only)

**Axis**: C-31 Part C contains only sub-check (1): Phase 1/3 inference scan with explicit exception acknowledgment format ("Exception acknowledged: T-NN is Phase 1 P0/P1 because [outage reason]"). Sub-check (2) — switching-friction field completeness as Part C property — is absent from Part C. That check exists in Part B (3. Switching-friction 4-field format) but is not re-verified in Part C. C-30 mechanisms from R9 V-05 preserved intact: STEP 2C hard gate with "Do not proceed to Step 3 until this block is filled" and paraphrase block.

| ID | Pts | Result | Evidence |
|----|-----|--------|----------|
| C-01–C-29 | — | PASS all | All R9 V-05 mechanisms intact; STEP 2C hard gate with `INFERENCE RULE (stated):` block preserved |
| Essential (C-01–C-05) | 60 | PASS | — |
| Recommended (C-06–C-08) | 30 | PASS | — |
| Aspirational C-09–C-29 | 105 | PASS | — |
| **C-30** | **5** | **PASS** | Same STEP 2C gate as R9 V-05. Hard gate language: "Do not proceed to Step 3 until this block is filled." Paraphrase block `INFERENCE RULE (stated):` present with "Required confirmation before proceeding" header. Demonstrated encoding required. |
| **C-31** | **5** | **FAIL** | Sub-check (2) is absent from Part C. The C-31 extraction rationale explicitly requires both: "(1) scan every ticket for C-28 directional compliance with exception acknowledgment gate, and (2) confirm the C-29 sub-section exists and all Migrating from: fields are populated." Without sub-check (2) in Part C, C-29 field completeness remains a generation-time structural assumption (verified once in Part B) rather than a verified output property. The criterion requires both checks to live in Part C. |

**V-03 Score: 200 / 205**
All essential: YES

---

### V-04 — Step 4 Decision-Adjacent Gate (C-30) + Structured Exception Sign-Off Block (C-31)

**Axes combined**: (1) Paraphrase gate at Step 4 header — same placement as V-02, STEP 2C has full imperative rule but no paraphrase block; (2) Part C replaces prose exception acknowledgment with structured `EXCEPTION SIGN-OFF BLOCK` containing five fields: Ticket ID, Phase, Assigned severity, Grounds, Disposition. Both sub-checks present. Field completeness verified in Sub-check 2.

| ID | Pts | Result | Evidence |
|----|-----|--------|----------|
| C-01–C-29 | — | PASS all | Step 2C imperative rule intact; all other R9 V-05 mechanisms preserved |
| Essential (C-01–C-05) | 60 | PASS | — |
| Recommended (C-06–C-08) | 30 | PASS | — |
| Aspirational C-09–C-29 | 105 | PASS | — |
| **C-30** | **5** | **PASS** | Step 4 header gate: "Before filling any severity cell, state the inference rule from Step 2C in your own words. Do not fill the table until this line is written: `INFERENCE RULE (stated):`". Decision-adjacent placement; paraphrase is live generation context immediately preceding severity column. |
| **C-31** | **5** | **PASS** | Both sub-checks present in Part C. Sub-check 1 (C-28): EXCEPTION SIGN-OFF BLOCK format — per-ticket fields (ID, Phase, severity, grounds, disposition) for any Phase 1 P0/P1 or Phase 3 P3. No-exception path also specified. Sub-check 2 (C-29): Switching-friction sub-section existence + per-entry Migrating from: value enumeration + verbal verbatim-check required. Structured exception record produces higher-quality evidence than prose count. |

**V-04 Score: 205 / 205**
All essential: YES

---

### V-05 — Full Synthesis (Maximum C-30 + Maximum C-31)

**Axes combined**: (1) C-30 double gate — hard gate at STEP 2C ("Do not proceed to Step 3 until this block is filled with your own-words paraphrase") AND paraphrase recalled at Step 4 header ("Do not fill the table until this line is written: `INFERENCE RULE (confirmed): [restate from 2C]`"); (2) C-31 Part C — both sub-checks + EXCEPTION SIGN-OFF BLOCK + paraphrase consistency confirmation (quotes Step 2C paraphrase, confirms paraphrase matches audit result).

| ID | Pts | Result | Evidence |
|----|-----|--------|----------|
| C-01–C-29 | — | PASS all | All prior mechanisms fully intact; STEP 2C now adds "genuine restatement — not a copy" instruction on top of the hard gate |
| Essential (C-01–C-05) | 60 | PASS | — |
| Recommended (C-06–C-08) | 30 | PASS | — |
| Aspirational C-09–C-29 | 105 | PASS | — |
| **C-30** | **5** | **PASS** | Double-gated. Gate 1: STEP 2C "Do not proceed to Step 3 until this block is filled" — paraphrase committed upstream. Gate 2: Step 4 "Do not fill the table until this line is written: `INFERENCE RULE (confirmed):`" — paraphrase recalled as live context immediately before severity column. Both gates enforce demonstrated encoding. Gate 2 eliminates dissipation risk: even if the upstream paraphrase fades across STEP 3, the Step 4 recall regenerates it as the immediate predecessor to severity assignments. |
| **C-31** | **5** | **PASS** | Full implementation. Sub-check 1 (C-28): EXCEPTION SIGN-OFF BLOCK per Phase 1 P0/P1 and Phase 3 P3 deviation. Sub-check 2 (C-29): per-entry Migrating from: value enumeration with verbatim check. Paraphrase consistency confirmation closes the C-30/C-31 chain: Part C quotes first 10 words of Step 2C paraphrase, states whether it was confirmed at Step 4, and compares against Phase 1/3 audit results. A self-contradicting paraphrase/audit pair (e.g., "Phase 1 = lower severity" paraphrase + Phase 1 P0 PASS audit) is structurally visible and requires explicit correction before finalization. |

**V-05 Score: 205 / 205**
All essential: YES

---

### Score Summary

| Variation | C-30 | C-31 | Score | Essential |
|-----------|------|------|-------|-----------|
| V-01 | FAIL | PASS | 200 / 205 | YES |
| V-02 | PASS | PASS | 205 / 205 | YES |
| V-03 | PASS | FAIL | 200 / 205 | YES |
| V-04 | PASS | PASS | 205 / 205 | YES |
| V-05 | PASS | PASS | 205 / 205 | YES |

**Rank**: V-05 > V-04 > V-02 (tied at 205, secondary rank by structural quality) >> V-01 = V-03 (200).

---

### Excellence Signals from V-05

**Signal 1: Double-gated paraphrase chain closes the dissipation window.**
V-05 places two paraphrase gates: one at STEP 2C (before model has written anything) and one at Step 4 (immediately preceding severity assignments). The Step 4 gate uses `INFERENCE RULE (confirmed):` rather than `INFERENCE RULE (stated):` — the label signals recall, not fresh statement. The gap between STEP 2C and Step 4 spans STEP 3 (performance mode declaration), which is dense prose that can degrade the model's generation-time access to the prior paraphrase. The Step 4 recall regenerates the committed encoding at the exact decision point. V-02 and V-04 achieve the same timing benefit from a single Step 4 gate, but V-05's upstream commitment at STEP 2C creates an earlier anchoring point — the model has produced the paraphrase twice before any severity value is assigned.

**Signal 2: Paraphrase-audit chain closure makes self-contradicting outputs structurally self-correcting.**
V-05's Part C closes a logical chain: the model committed a paraphrase at STEP 2C, recalled it at Step 4, and now must quote the first 10 words of that paraphrase and compare it against the audit result. If the paraphrase stated "Phase 1 tickets should be low severity because the old tool is still available" and the audit finds a Phase 1 P0 with no violation flag, the confirmation step requires the model to state "Paraphrase consistent with audit results: YES" — which it cannot do without contradiction. This is not a logic check added by the scorer; it is a self-verification step built into the prompt. The scorer benefit: any inconsistency that the model fails to catch in Part C produces a detectable trace (the paraphrase quote vs. the audit result) that the scorer can compare.

**Signal 3: Structured EXCEPTION SIGN-OFF BLOCK converts exception acknowledgment from prose count to attributed record.**
V-03's prose exception acknowledgment ("Exception acknowledged: T-NN is Phase 1 P0/P1 because [reason]") is verifiable but produces a sentence. V-04 and V-05's EXCEPTION SIGN-OFF BLOCK produces five named fields per exception: Ticket ID, Phase, Assigned severity, Grounds (outage-level YES/NO), Disposition (VALID EXCEPTION with reason OR VIOLATION with correction). This format separates classification (Grounds) from conclusion (Disposition) — a model that writes "Grounds: YES" and "Disposition: VALID EXCEPTION — no reason given" is scorably different from one that writes both with substantive content. The block format also enables grep-checkable verification: a scorer can search for `Disposition: VIOLATION` to find self-corrected entries without reading prose.

---

### New Pattern Candidates for R11

These patterns appear only in V-05 (above ceiling relative to V-02/V-04):

1. **Double-gate paraphrase recall**: upstream commitment (STEP 2C "stated") + decision-adjacent recall (Step 4 "confirmed") using distinct labels — the recall label makes retrieval explicit, not implicit.

2. **Paraphrase-audit chain closure with quoted first 10 words**: Part C quotes the paraphrase and compares it against the audit result — makes any contradiction between stated understanding and audit conclusion structurally visible within the model's own output.

---

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["Double-gate paraphrase recall: upstream STEP 2C commitment plus decision-adjacent Step 4 recall with distinct labels closes the dissipation window between rule encoding and severity decision", "Paraphrase-audit chain closure: Part C quotes first 10 words of Step 2C paraphrase and compares against audit results, making self-contradicting paraphrase-violation pairs structurally visible and self-correcting within the prompt"]}
```
