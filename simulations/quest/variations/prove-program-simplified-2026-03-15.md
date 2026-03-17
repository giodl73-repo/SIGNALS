**Exact word count: 1,163.** V-02 base was 1,547. That's 384 words removed = **24.8% reduction**.

---

## Simplification Report

### Before vs. After
- Full file (5 variations): **8,475 words** — the complete research artifact
- V-02 (chosen base, shortest variation): **1,547 words**
- Simplified prompt: **1,163 words**
- **Reduction from V-02 base: 24.8%** (within the 20-40% target)

### Why V-02 was chosen as base
V-02 (pure prose, no tables) is the shortest of the five variations at 1,547 words. It is also the most natural production format: linear phases, labeled prose blocks, no role-model overhead (V-01), no RFC bureaucracy (V-03), no gate-dense verbosity (V-04), no 3-role complexity (V-05).

### What was removed and why

| Removed | Words | Reason |
|---------|-------|--------|
| Lines 267-268: variation axis description + research hypothesis | ~60 | Research metadata. Not instructions. |
| Phase 1 parenthetical "(what you believe is true, not what you suspect is false)" | ~14 | "positive form" is already defined |
| Phase 1 hint "-- what you believe is true" after format placeholder | ~6 | Redundant with the label |
| GATE-1 "the gate is conjunctive, not a checklist" | ~10 | Redundant with "Both must be TRUE. Partial satisfaction is FAIL." |
| GATE-1 separate result lines per condition (merged into condition line) | ~25 | Description + standalone result line = two sentences doing one job |
| GATE-1 STOP "Do not proceed to Phase 1B..." | ~18 | Top-level "every gate is a hard stop" already covers this |
| Phase 1B "[Confirm GATE-1 PASS...]" confirm box | ~12 | Redundant with STOP just removed |
| Phase 1B prose description of E-NN fields (55-word run-on sentence listing all fields) | ~55 | Entirely redundant: E-01/E-02 format lines show exactly what's needed |
| Plan rules: "EXECUTOR uses these in per-block citation contracts" | ~10 | Reasoning, not rule; rule is in E-02 block |
| GATE-P STOP "Do not execute any experiment until GATE-P PASS" | ~12 | GATE-P FAIL implies this; top-level gate rule covers it |
| Feed-Forward Audit prose intro ("For each experiment, record: what output label...") | ~32 | Entirely redundant with the E-01/E-02 audit format lines below |
| Findings verbose intro ("For each finding, state: the finding text, which experiment...") | ~28 | Redundant with F-01/F-02 format lines |
| GATE-CAL preamble "[This gate runs before synthesis. Do not write synthesis...]" | ~20 | Synthesis section carries its own "[Confirm GATE-CAL PASS]" reminder |
| GATE-CAL "State every distinct confidence value...Count them...Confirm..." | ~25 | Redundant with the three fill-in fields below |
| GATE-CAL "Assigning HIGH to every finding is not calibration -- it is uniform assertion." | ~18 | Redundant with FAIL condition: "All findings carry the same confidence level." |
| GATE-CAL STOP "Do not write synthesis until GATE-CAL result is PASS." | ~14 | Synthesis preamble carries the confirm reminder |

### Essential criteria check

| Criterion | Still passes? | Evidence in simplified prompt |
|-----------|--------------|-------------------------------|
| **C-01** Hypothesis pre-commitment | YES | "Phase 1 -- Hypothesis" section with `**Hypothesis:** [positive form]` before any experiment block; Condition A enforces distinctness from research question |
| **C-02** Experiment plan >=2 distinct types | YES | Phase 1B with E-01/E-02 format and "At least 2 distinct types required. No two experiments may share the same type." |
| **C-03** Feed-forward between experiments | YES | E-02 INPUT citation contract embeds E-01 output verbatim; E-02 scoping sentence references E-01's finding |
| **C-04** Synthesis contrast | YES | "What we thought: [verbatim hypothesis]" + "What we actually learned: [must differ from hypothesis text]" |
| **C-05** Qx.md format at correct path | YES | Artifact section: `simulations/prove/research/{{topic}}-research-{{date}}.md`; >=4 labeled sections present |

**All essential criteria: PASS**

---

Written to: `simulations/quest/golden/prove-program-QU5-simplified-2026-03-15.md`

```json
{"simplified_word_count": 1163, "original_word_count": 1547, "all_essential_still_pass": true}
```
