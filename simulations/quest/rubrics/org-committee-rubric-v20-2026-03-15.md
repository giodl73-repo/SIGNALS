Written to `simulations/quest/rubrics/org-committee-rubric-v20-2026-03-16.md`.

---

**What changed v19 -> v20**

Three new criteria extracted from R20 excellence signals. All three close enforcement-completeness gaps left by C-47, C-48, and C-49 — each new criterion addresses a dimension of *how* the symmetry/independence requirements are declared, not just *that* they are declared.

**C-50 -- Symmetry criterion ENFORCE clauses include an explicit named violation condition** *(new)*

C-47/C-48 require ENFORCE clauses stating the positive symmetry requirement but do not require the ENFORCE to name the specific asymmetric configuration that breaks the rule. V-04's ENFORCE clauses carried explicit failure-condition language ("C-47 fails if INERTIA INVARIANT VALIDATE enumerates three axes and STANCE INVARIANT VALIDATE enumerates fewer") that V-01's positive-only phrasing lacked. This converts the ENFORCE from a unidirectional contract (compliant form anchored) to a bidirectional contract (compliant form + violation form both anchored).

**C-51 -- Symmetry enforcement blocks are organized as named skeleton subsections** *(new)*

C-47/C-48 require symmetry enforcement to be present but do not require it to be architecturally visible. V-04 organized C-47 and C-48 as named subsections (`SEALING CONTRACT INTEGRITY SYMMETRY -- STANCE INVARIANT`, `COUPLING INTEGRITY SYMMETRY -- PHASE-3-COMMIT bidirectionality clause`) rather than inline ENFORCE postscripts within the parent fill rule. This applies C-37/C-40's named-section principle to the symmetry enforcement layer, making parity contracts independently navigable by section heading.

**C-52 -- SYNTHESIZE VALIDATE ENFORCE names the independence principle for its two FAILS axes** *(new)*

C-49 requires both FAILS axes to be present with an ENFORCE stating "both are independently required" but does not require naming *why* they are independent. V-04 and V-03 both carried the independence principle ("structural absence and incorrect affirmation are distinct testable violations" / "absent and wrong are different errors") beyond V-01's quantity-assertion ENFORCE. This converts the ENFORCE from a co-requirement list into a logical statement grounding the two-axis structure.

**Scoring**: aspirational pool 41 -> 44; aspirational max 82 -> 88; composite max **172 -> 178**.
