Written to `simulations/quest/golden/mock-all-variate-R8-2026-03-15.md`.

---

## mock-all Variate — Round 8

**Rubric:** v8 (frozen; no new criteria)
**Baseline:** V-05 R7 is the confirmed 100% reference implementation

### What R7 Left Open

Both R7 open questions are resolved by v8's confirmation annotations:
- **C-19:** longer token text is permitted; sentence count as first element is the pass condition
- **C-20:** ROLE 3 derivation bridge is the confirmed passing form; no coverage table column required

R8 therefore shifts to structural robustness: can 100% be achieved with meaningfully different structural choices?

---

### Axis-Assignment Plan

| Variation | Axis | Key change | C-18 risk | Predicted |
|-----------|------|------------|-----------|-----------|
| V-01 | role-sequence | Consolidate all identity-violation warnings into single preamble; strip per-role repetition | UNCERTAIN — passes if role name + preamble satisfy C-18; fails if per-role enforcement is required | 12/12 or 11/12 |
| V-02 | output-format | Add "Inertia gap skeleton" as 8th column in ROLE 1 classification table; ROLE 2 extends skeleton with topic-specific content | PASS | 12/12 + improved C-20 quality |
| V-03 | phrasing-register | Replace "You ARE the CLASSIFIER" ontological framing with prohibition-forward framing ("CLASSIFIER: generate X only. Generating Y is prohibited.") | UNCERTAIN — tests whether C-18 requires "You ARE" specifically | 12/12 or 11/12 |
| V-04 | lifecycle-emphasis | Convert all stop-gate phrases to markdown checkbox lists (one checkbox per required field) | PASS | 12/12 |
| V-05 | combination | V-01 consolidated preamble + V-02 inertia skeleton table + V-04 checklist gates | PASS if V-01 passes | 12/12 |

### Key Discriminators

**V-01 vs V-05 R7 (C-18):** V-05 R7 repeats "Writing X here means you are ROLE N, which you are not yet" at every role. V-01 removes per-role repetition, keeping only the preamble + role names. Tests whether per-role framing is load-bearing or decorative for C-18.

**V-03 (C-18):** Tests the hardest boundary — does C-18 require the ontological "You ARE" construct, or does prohibition-forward ("CLASSIFIER: generate X only; Y is prohibited") satisfy "identity violation"? The rubric says "the model knows it *is* the CLASSIFIER, not merely *is in step 1*."

**V-02/V-05 (C-20 quality):** The inertia skeleton pre-seeded in ROLE 1 constrains ROLE 2 answers to the namespace's epistemic function before the topic is applied. If this produces measurably better artifact bodies than free-form, it may be the R8 excellence signal for a potential v9 criterion about inertia-answer specificity depth.
