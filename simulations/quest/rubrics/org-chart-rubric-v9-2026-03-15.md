The v9 rubric is written to `simulations/quest/rubrics/org-chart-rubric-v9-2026-03-16.md`.

---

**What changed in v9:**

**C-26 — Count-verification protocol includes a conditional remediation path** (V-04/R8 source)

C-23 (v7) required the guard to embed a printed count. C-26 requires the guard to also specify what the model must do if the count check fails — an explicit Step 1 (count) / Step 2 (if count < 2, write missing reasons; once count ≥ 2, substitute N and emit) / verify-before-substituting procedure. Without a remediation path, a model that counts too few reasons reaches a silent-failure state: the guard blocks but provides no recovery. The two-step protocol makes verification algorithmic and self-repairing. Dep: C-23.

**C-27 — Imperative directive layer is free of conflicting descriptive prose** (V-02/R8 vs V-03/R8 contrast)

C-25 (v8) required DO NOT / MUST / REQUIRED for the three governed behaviors. C-27 additionally requires that no descriptive counterpart framing coexists for those same behaviors. The R8 finding: enforcement blocks appended to unchanged conversational prose (V-03/R8) and inline enforcement paragraphs injected within unchanged prose (V-01/R8, V-04/R8) both pass C-25 but create a dual-layer structure where the primary prose retains "by convention" / "typically" framing — a latent drift risk that C-25's binary pass does not surface. V-02/R8's full imperative conversion eliminates the dual layer. Dep: C-25.

**Denominator:** `/17` → `/19` (0.526 pts per criterion)

**R8 score ceiling:** 99.5 (18/19). V-02 reaches 18/19 via C-27 (no C-26); V-04 reaches 18/19 via C-26 (no C-27). A first 19/19 requires combining V-02's single-layer imperative framing with V-04's two-step remediation protocol — neither exists in R8.
