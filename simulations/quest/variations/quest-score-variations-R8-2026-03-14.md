Written to `simulations/quest/rubrics/quest-score-rubric-v8-variations-R8-2026-03-15.md`.

---

## R8 Variations -- quest-score

**5 complete, standalone skill body prompts. Single-axis ablations first, combination pass last.**

---

### V-01 -- Baseline R8 Full Stack

**Axis:** N_aspirational=16, 23-row criterion roster, C-22 SETUP exclusion embedded in preservation rule, C-23 three-form enumeration in C-20 diagnostic question.

All R7 V-05 structures retained. Key new elements vs. R7:
- Preservation rule: "...must remain in the FAILURE PATTERNS action line -- **do not relocate it to SETUP**, to a roster diagnostic question, or to a preservation checkpoint." (C-22 PASS)
- C-20 diagnostic: three disqualifying forms -- interrogative + conditional + weak-modal (C-23 PASS)
- C-22 diagnostic: "PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language."
- Formula uses N_aspirational=16; roster has 23 rows.

---

### V-02 -- C-22 Ablation

**Axis:** Preservation rule is imperative (C-19 PASS, C-20 PASS) but contains no location constraint -- neither FAILURE PATTERNS named as required, nor SETUP named as disqualifying.

**Single change from V-01:** Step 1.1 preservation rule reads: "...must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder." -- location language stripped entirely.

Expected: C-22 FAIL. All other criteria identical to V-01.

---

### V-03 -- C-23 PARTIAL Ablation

**Axis:** C-20 diagnostic question enumerates exactly two grammatical form failures (interrogative + conditional); weak-modal ("should be carried forward") omitted.

**Single change from V-01:** C-20 row in the roster reads: "Three disqualifying forms: (1) interrogative -- 'Has the worked example been carried forward?' earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- 'If the axis shifts, carry forward the example' earns C-20 FAIL. Mandatory verb required for PASS." Weak-modal form absent.

Expected: C-23 PARTIAL. All other criteria identical to V-01.

---

### V-04 -- C-23 FAIL Ablation

**Axis:** C-20 diagnostic question enumerates only one grammatical form failure (interrogative only); conditional and weak-modal omitted.

**Single change from V-01:** C-20 row reads: "Does the primary preservation rule contain a mandatory verb ('must', 'shall', 'is required to')? Interrogative form earns C-20 FAIL -- 'Has the worked example been carried forward?' is a diagnostic probe, not an enforceable instruction. Location alone does not satisfy C-20." One form only.

Expected: C-23 FAIL. Together with V-03, provides the C-23 three-point evidence ladder (FAIL/PARTIAL/PASS anchored by V-01).

---

### V-05 -- Combination Pass (C-24 Seed)

**Axis:** All R8 structures from V-01, plus C-22 diagnostic question explicitly enumerates all three verdict cases (FAIL/PARTIAL/PASS) with structural contrasting examples -- the missing element in V-01.

**Single addition to V-01:** C-22 row in the roster now reads: "Three verdict cases with structural contrasts: (FAIL) rule is imperative but contains no location language -- e.g., 'must be carried forward verbatim' without any FAILURE PATTERNS reference; (PARTIAL) rule names the required location ('must remain in the FAILURE PATTERNS action line') but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase."

**Potential C-24:** "C-22 diagnostic question enumerates all three verdict cases (FAIL/PARTIAL/PASS) with distinct structural contrasting examples for each." This closes the gap in V-01 where the PARTIAL/FAIL boundary for C-22 is described but the three-scale enumeration is not explicitly illustrated -- the same structural deficiency that C-23 was designed to close for C-20.

---

**Evidence ladders:**
- C-22: V-02 (no location) = FAIL; V-01/V-03/V-04/V-05 (SETUP exclusion present) = PASS
- C-23: V-04 (1 form) = FAIL; V-03 (2 forms) = PARTIAL; V-01/V-02/V-05 (3 forms) = PASS
- **Spread prediction:** ~1.25 pts (each criterion contributes 0.625 pt; V-02 loses 1 aspirational on C-22; V-03 loses 0.5 on C-23 PARTIAL; V-04 loses 1 on C-23 FAIL; V-01/V-05 lose 0)
