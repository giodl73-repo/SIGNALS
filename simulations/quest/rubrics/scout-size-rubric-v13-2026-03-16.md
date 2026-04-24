**v13 written** to `simulations/quest/rubrics/scout-size-rubric-v13-2026-03-17.md`.

---

**What changed from v12**

Two new aspirational criteria added. Scoring denominator updated from 25 to 27.

---

**C-34 — Failure-class label co-encoded in WRONG instance examples**

Derived from two independent R12 signals: V-02's "DIAGNOSIS: basis-negation detected" labeled field inside the WRONG block (noted in C-21 evidence), and V-05's "Failure class: basis-negation" structural header inside the WRONG block (noted as V-05's distinguishing feature in the ranking row).

C-33 requires the self-test's affirmative branch to name the failure class — the model encounters that label during self-evaluation, after the field draft is formed. C-34 extends the failure-class name backward to the WRONG/CORRECT example itself, so the model encounters the failure class label at example-exposure time — while priming the field — rather than only during the self-test check. The two sites are distinct: C-33 covers the self-test branch; C-34 covers the WRONG block. Both can be satisfied simultaneously by using a labeled DIAGNOSIS or Failure-class annotation within the WRONG instance.

**C-35 — Pre-analysis gate phase with binary entry signal**

Derived from V-05's Phase 0 CLOSED/OPEN inertia gate. In V-05's three-phase design, Phase 0 outputs exactly CLOSED or OPEN before Phase 1 begins; a CLOSED output halts analysis and names the unmet precondition; Phase 1 production is structurally conditioned on OPEN.

The distinction from C-20 (role-separated production for relational field pairs): C-20 separates Phase 1 and Phase 2 to prevent constraint conflation between complementary output fields. C-35 adds a Phase 0 that gates whether the analysis sequence should run at all — it is not concerned with field-level relational constraints but with enforcing entry preconditions (e.g., C-05 signal boundary) as a production dependency rather than a prose instruction.
