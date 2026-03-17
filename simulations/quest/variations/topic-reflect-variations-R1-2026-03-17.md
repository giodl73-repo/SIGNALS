Written to `simulations/quest/golden/topic-echo-variate-R1-2026-03-17.md`.

---

## Round 1 Variations — topic-echo

5 complete prompt bodies. Single-axis: V-01, V-02, V-03. Combination: V-04, V-05.

---

### V-01 — Role Sequence
**Hypothesis:** Insert a **Gate Criteria Preview** between Stage 1 and Stage 2. The five gate checks are presented as an active lookup table *before* the sweep begins. The model enters the sweep already knowing what qualifies, rather than cataloging everything and filtering retroactively.

**What it changes:** Sequence only. Stage structure is 1 → Gate Preview → 2 → 3 → 4 → 5 → 6. No content removed. Addresses **C-05** (gate execution) and **C-01** (surprise orientation) by priming discrimination at collection time.

---

### V-02 — Lifecycle Emphasis
**Hypothesis:** Expanding Stage 3 with two worked examples (one VALID, one INVALID) eliminates gate theater — the failure where the model fills in the table without genuine discrimination. A calibration anchor prevents confirmation-as-surprise from passing.

**What it changes:** Stage 3 gains ~300 words of worked examples and check-by-check rationale. All other stages unchanged. Directly targets **C-01** and **C-05**; the INVALID example is specifically a *confirmation disguised as surprise*, the most common entry inflation pattern.

---

### V-03 — Phrasing Register
**Hypothesis:** Short imperative sentences (verb-first, no subordinate clauses) reduce instruction-following failures. The original opens with a 9-sentence paragraph explaining six structural commitments. V-03 replaces all explanatory prose with a 6-item rule list and strips stage introductions to one sentence.

**What it changes:** Register throughout. All six structural commitments become numbered rules at the top. Stage intros collapse from paragraphs to single imperatives. Structure and tables identical to baseline. Targets token omission failures and lifecycle collapse.

---

### V-04 — Role Sequence + Lifecycle Emphasis
**Hypothesis:** Gate Preview (V-01) primes the model to search for qualifiers during sweep; worked examples (V-02) calibrate the discrimination threshold during gate execution. These two interventions target different points in the same failure chain. Combined, they close both the *priming gap* and the *calibration gap* that cause entry inflation.

**What it changes:** Gate Criteria Preview table inserted before Stage 2 (with failure-mode column added), plus Stage 3 expanded with a VALID and INVALID calibration example drawn from the Signal domain. The strongest treatment for **C-01** and **C-05**.

---

### V-05 — Phrasing Register + Output Format
**Hypothesis:** Stage 4's table format creates pressure to abbreviate Signal Source and Design Impact into 3-word fragments, the primary cause of **C-03** and **C-04** failures. V-05 keeps the imperative register of V-03 but replaces Stage 4's table with numbered prose entries using a fixed template. Full sentences for `Signal Source` and `Design Impact` are structurally enforced by the template — you cannot write a one-word cell in prose.

**What it changes:** Stage 4 output format becomes templated prose (6 labeled fields per entry, full sentence required for each). All other stages use the same short-register tables as V-03. Uniquely targets the two most specific-content criteria: **C-03** (signal tracing) and **C-04** (design impact specificity).
