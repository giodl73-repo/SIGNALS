Written to `simulations/quest/rubrics/org-committee-rubric-v19-2026-03-16.md`.

---

**What changed v18 -> v19**

Three new criteria extracted from R19 excellence signals. All three close gaps left by C-44, C-45, and C-46 respectively -- each new criterion addresses a cross-instance parity or accuracy dimension that the v18 rule required within a single instance but did not require to hold symmetrically or test for correctness.

**C-47 -- INVARIANT VALIDATE three-axis coverage is structurally symmetric across both seal declarations** *(new)*

C-44 requires three independent failure axes on each INVARIANT VALIDATE rule but does not require parity between the two rules. A variant with three axes on INERTIA INVARIANT but only one on STANCE INVARIANT satisfies C-44 per-rule while leaving the vote-anchor seal asymmetrically under-tested. The scoring evidence was explicit: both V-01 ("STANCE INVARIANT identical") and V-02 ("STANCE INVARIANT: same three axes named") carried the parity marker as a distinguishing structural signal.

**C-48 -- Bidirectionality VALIDATE appears symmetrically in both phase-commit fill rules** *(new)*

C-45 requires the half-coupling FAILS test in the dedicated fill rule for each bidirectionality clause but does not require symmetric coverage across both PHASE-1-COMMIT and PHASE-3-COMMIT. An output that applies the content-completeness test to PHASE-1-COMMIT only leaves the vote-anchor coupling unprotected. V-01 ("PHASE-3-COMMIT identical") and V-02 ("PHASE-3-COMMIT: same") both carried symmetric coverage across both commits.

**C-49 -- SYNTHESIZE instruction VALIDATE includes a FAILS case for incorrect affirmation** *(new)*

C-46 requires bilateral VALIDATE on the SYNTHESIZE instruction but does not specify the VALIDATE must test incorrect affirmation -- YES declared when no qualifying participant exists. An output that validates only structural absence passes C-46 while leaving a YES-without-injection path open. Both V-01 and V-02 explicitly named this failure mode: "VALIDATE with ACCEPTABLE/FAILS for absent section **and incorrect YES**."

**Scoring**: aspirational pool 38 -> 41; aspirational max 76 -> 82; composite max **166 -> 172**.
