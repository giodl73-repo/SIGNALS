Written to `simulations/quest/golden/campaign-validate-variate-R3-2026-03-16.md`.

---

## campaign-validate — R3 Variations Summary

**5 variations, 3 single-axis + 2 combined:**

---

### V-01 — Phase-Gate Role Sequence
**Axis**: Execution enforced by explicit GATE markers. Each sub-skill is a named phase; no phase exit is valid without logging findings. The GATE 4 → PHASE 5 boundary carries a required categorical declaration ("listen-feedback = what customers SAY; listen-adoption = what they DO").

**Hypothesis**: Gate markers prevent listen-adoption from being silently skipped or merged. C-14 passes by construction — the author must write the categorical declaration as the gate condition text, not as prose they can omit. **Hardest remaining**: C-15, C-16.

---

### V-02 — Table Skeleton Format
**Axis**: All five sub-skill tables are pre-declared with headers (including `Severity` and `Adoption Impact` as separate columns) before execution begins. Table 4 (listen-feedback) and Table 5 (listen-adoption) each carry a scope annotation. An empty table = "ran, found nothing." A missing table = "skipped."

**Hypothesis**: Pre-declared table structure enforces C-11 and C-12 simultaneously. Rogers segment rows in Table 5 make absent segments visually detectable. **Hardest remaining**: C-14 (still advisory), C-16 (no inertia column).

---

### V-03 — Inertia Framing
**Axis**: An **Inertia Baseline Statement** is established before any sub-skill runs: "Users today do X. This feature requires giving up X because Y. The population still doing X after ship is the adoption risk segment." Every blocker is then evaluated against this anchor.

**Hypothesis**: The workaround's user population IS the adoption risk segment — so C-16 (inertia citation) and C-09 (segment identification with %) reinforce each other without separate enforcement. Also strengthens C-06 synthesis because Phase 1 and Phase 5 findings become connectable via the shared inertia root. **Hardest remaining**: C-11, C-15.

---

### V-04 — Combined (Phase-Gate + Two-Phase Lifecycle)
**Axes**: Phase gates (V-01) + explicit two-phase structure: Phase 1 = design evidence (review-design, review-users, review-customers), Phase 2 = customer signal (listen-feedback, listen-adoption).

**Hypothesis**: The Phase 1 → Phase 2 transition IS the categorical boundary — it declares "design quality" vs. "customer behavior" as structurally different analytical modes. The gate within Phase 2 between Step 4 and Step 5 is the C-14 enforcement point. C-01 is enforced because each of 5 sub-skills has a named gate exit. **Hardest remaining**: C-15 (Rogers rows still prose, not pre-declared table rows), C-16.

---

### V-05 — Combined (Table-First + Rogers Rows + Inertia Column)
**Axes**: Table skeleton (V-02) + Rogers segments as 5 required pre-declared rows in Table 5 + `Status-Quo Workaround` and `Switching Cost` as required columns in the Top Blockers table.

**Hypothesis**: This is structural maximum. Rogers rows → C-15 by construction. Inertia columns → C-16 by construction. Both force C-09 (one segment estimate per row) without a separate enforcement point. Table 5's pre-declared Rogers skeleton makes listen-adoption a visibly distinct section → C-14 by layout. The only criteria still requiring author discipline: C-06 (synthesis) and C-03 (verdict). **Expected score ceiling**: ~125+.
