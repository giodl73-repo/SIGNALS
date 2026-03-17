Written to `simulations/quest/golden/topic-echo-variate-R12-2026-03-16.md`.

---

## R12 — `topic:echo` Variations

**Rubric:** v11 | 5 complete prompt bodies

---

### Design Context

R11 V-05 reaches **100.0** under v11 (all 24 aspirational criteria pass). R12 explores two axes never tested in any prior round — **phrasing register** and **inertia framing** — plus a fresh output format angle, then combines them.

---

### V-01 — Single-axis: Phrasing Register (Declarative/Contractual)

**Axis:** Register shift only. All R11 V-05 structural features retained exactly — same roles, same 12 steps, same entry template schema, same PHASE/SCOPE/INPUT/OUTPUT blocks. Every imperative instruction ("Recover the team's prior belief set") becomes a declarative contract statement ("The CB-ID register is the BC's sole deliverable; signal artifact access is a contract violation"). Gates become violation conditions; scope boundaries become exclusion contracts.

**Hypothesis:** Declarative register may strengthen C-20 (audit scope differentiation) and C-21 (enforcement pipeline staging) because contracts make scope exclusions explicitly testable. Risk: C-04 (actionability) may slightly degrade if the concrete-misdesign mandate is more reliably produced under imperative phrasing than a contract statement. The discriminating question: does phrasing register independently affect scoring, or is it structurally neutral?

**Expected score:** ~100.0 if neutral; possible C-04 soft degradation if not.

---

### V-02 — Single-axis: Inertia Framing (Prominent)

**Axis:** R11 V-01 structural baseline (BC + CB-IDs, C-30 + C-31 active; C-24/C-25/C-11/C-12 not activated; C-14 PARTIAL). A new **Inertia Statement** block opens the prompt, declaring the default build path without the echo. Each entry gains a `Without this echo:` field naming the specific wrong artifact produced under inertia. Step 9 adds an Inertia Comparison section.

**Hypothesis:** The `If the next team carries the old assumption:` field (C-04) and `wrong action a future team would take` (C-09) are the same concept at different levels of specificity. Providing a visible inertia prototype at the opening and per-entry may cause both fields to be filled more concretely — they have a reference artifact to diverge from. Risk: inertia fields could crowd out synthesis content in Step 8.

**Expected score:** ~98.5 — C-04/C-09 improve; C-24/C-25/C-11/C-12 still fail.

---

### V-03 — Single-axis: Output Format (Table-Centric Entries)

**Axis:** R11 V-01 structural baseline. Step 7 changes from prose entry blocks to a structured markdown table — each row is one surprise, each column is a required field (`defeats`, `We believed`, `The surprise`, `If carries old assumption`, `Without this echo`, etc.). Gate structure, synthesis, and Rules of Thumb remain prose.

**Hypothesis:** Table format enforces C-01 (entry count: rows are countable), C-02 (cross-signal citation: dedicated column), and C-30 (`defeats: CB-{n}` as a named column, not prose) mechanically. Risk: C-03 (falsifiable belief framing) may degrade if a table cell is too constrained to contain a full falsifiable claim.

**Expected score:** ~97.5–98.0 — C-01/C-02/C-30 mechanical gain; C-03 soft risk.

---

### V-04 — Combination: Phrasing Register + Inertia Framing

**Axes:** Declarative phrasing throughout + prominent inertia framing. Base: R11 V-03 (C-24 + C-25 active). Declarative contracts clarify scope; inertia framing clarifies consequence. Adds `Without this echo:` field per entry and Inertia Comparison section in Step 9.

**Hypothesis:** These two axes target orthogonal dimensions — phrasing affects scope legibility (C-20/C-21/C-27); inertia affects actionability specificity (C-04/C-09/C-15). Additive improvement expected without structural interference. The discriminating pair is V-02 vs V-04: if V-04 scores higher than the R11 V-03 baseline + V-02's inertia delta alone, the declarative phrasing is adding independent value.

**Expected score:** ~99.0–99.5 — C-24/C-25 active; C-04/C-09 strengthened.

---

### V-05 — Full Synthesis: All Three R12 Axes

**Axes:** Declarative phrasing + prominent inertia framing + table-format entries organized by defeated CB-ID. Base: R11 V-05 (all 24 aspirational criteria active). All three R12 axes applied simultaneously. The table format in Step 7 carries CB-ID group headers (preserving C-12), and a `Without this echo:` column (adding inertia framing). The production chain trace at Step 12 explicitly names all R12 additions.

**Hypothesis:** R11 V-05 at 100.0 is the structural ceiling. R12 tests whether the three new axes are compatible with it or introduce interference — specifically whether table entries + CB-ID grouping + inertia columns produce a row that is too wide to be readable without degrading scoring. If V-05 holds 100.0, all three axes are safe to combine. If it drops, the production chain trace names which node is the failure source.

**Expected score:** 100.0 (if axes compose without interference) or slight degradation localized to C-03/C-08.

---

### Discriminating pairs

| Pair | What's isolated |
|------|----------------|
| V-01 vs V-05 | Phrasing register alone vs all axes |
| V-02 vs V-04 | Inertia framing value with/without declarative phrasing |
| V-03 vs V-05 | Table format effect when full-feature stack is active |
| V-01 vs R11 V-05 | Whether declarative register is neutral or has scoring consequence |
| V-02 vs R11 V-01 | Net value of inertia framing on the minimal baseline |
