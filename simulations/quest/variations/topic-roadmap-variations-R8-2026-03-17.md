---

# topic-roadmap / Round 8 Variations

**Rubric:** v8 (C-01–C-20, formula `/24*10`)  
**New criteria this round:** C-19 (phase entry/exit conditions) + C-20 (bias labels at every structural guard point)  
**Axes selected:** lifecycle_emphasis / inertia_framing / bias_label_completeness → combined in V-04 and V-05

---

## V-01 — Axis: Lifecycle Emphasis

**Hypothesis:** C-19 requires entry conditions that reference the preceding phase by number and exit conditions that confirm completion. Baking `ENTRY CONDITION: Phase N-1 EXIT CRITERION met` and `EXIT CRITERION: [token]. Phase N may NOT open until this is met` as labeled fields in every phase header makes gate skipping structurally detectable at the boundary — not inferred from output structure. Phase ordering alone achieves partial credit; explicit named entry/exit conditions achieve full pass.

**Key structural move:** Every phase (1–8) carries both an ENTRY CONDITION and EXIT CRITERION block, including both passes of the INERTIA-GATE and the confirmation gate.

---

## V-02 — Axis: Inertia Framing

**Hypothesis:** Naming INERTIA as a competitor (not a process rule) converts every decision cell from "should I propose this?" to "does this evidence defeat INERTIA?" This eliminates action-default bias at the cognitive level. C-01, C-11, C-13 become structurally natural: INERTIA RETAINED ACROSS ALL DIMENSIONS is a defeat-verdict outcome, not an empty-table fallback. Phase 6 entry condition is crisp: "INERTIA was defeated on at least one dimension."

**Key structural move:** INERTIA COMPETITOR DECLARATION up front; Phase 5 framed as an adjudication; Phase 6/7/8 use INERTIA displacement vocabulary throughout.

---

## V-03 — Axis: Bias Label Completeness

**Hypothesis:** C-20 tests completeness — every named structural guard carries an inline bias label at the guard site itself, not only in proposal table columns or phase-level headings. Using `>>> GUARD: [name]` / `>>> Bias blocked: [bias]` / `>>> Mechanism: [description]` inline at each guard makes the label auditable at the guard site. A scoring agent looking for the label on the SIGNAL READ-LOCK finds it directly at the lock, not inferred from a preamble.

**Guards labeled:** PHASE-1-READ-BARRIER / SIGNAL READ-LOCK / INERTIA-GATE (twice: Phase 5 + Phase 6) / CONFIRMATION GATE / WRITE GUARD.

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing

**Hypothesis:** The two axes are synergistic. INERTIA framing gives entry conditions semantic sharpness: `ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present` is tighter than `Phase 5 is complete` because it names the relevant output token. The lifecycle structure gives the inertia vocabulary a phase-numbered scaffold that makes violations detectable before inspecting output structure. C-19 and C-01/C-11/C-13 reinforce each other.

---

## V-05 — Full Integration: Lifecycle Emphasis + Inertia Framing + Bias Label Completeness + Output Schema

**Hypothesis:** C-19 and C-20 are orthogonal — a skill can have entry/exit conditions while leaving guards unlabeled (C-19 pass / C-20 fail), and can label every guard while using soft narrative phases (C-20 pass / C-19 fail). V-05 achieves both by combining V-01's phase-numbered entry/exit structure (C-19), V-03's inline `>>> GUARD` labels at every named guard site (C-20), and V-02's inertia-competitor framing (C-01/C-11/C-13). The upfront table schema commitment (table-first) converts column completeness from soft to structural — adding hardening for C-03 and C-05.

**New structural element:** SCHEMA COMMITMENT block upfront with all table schemas fixed before any file is read. The `>>> GUARD: SCHEMA COMMITMENT` label makes this guard site visible for C-20 scoring.

---

Output written to `simulations/quest/golden/topic-roadmap-variate-R8-2026-03-17.md`.

**Scoring predictions against v8:**

| Variation | C-19 (entry/exit) | C-20 (guard labels) | C-01 (inertia prior) | Predicted composite |
|-----------|-------------------|---------------------|----------------------|---------------------|
| V-01 | Full (2) | Partial (1) — phases labeled but guard sites not all inline | Full (2) | ~95 |
| V-02 | Partial (1) — no explicit entry/exit | Partial (1) — guard labels in phases only | Full (2) | ~92 |
| V-03 | Partial (1) — no explicit entry/exit | Full (2) — every guard site labeled | Full (2) | ~93 |
| V-04 | Full (2) | Partial (1) | Full (2) | ~97 |
| V-05 | Full (2) | Full (2) | Full (2) | **100** |
