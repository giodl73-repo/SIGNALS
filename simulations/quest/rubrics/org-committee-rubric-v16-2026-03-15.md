Written to `simulations/quest/rubrics/org-committee-rubric-v16-2026-03-16.md`.

---

**What changed v15 → v16**

**C-40 — Named manifest sections carry an explicit post-commit seal declaration** *(new)*

Signal: V-04's "Inertia Invariant" axis. C-37 requires INERTIA RECORD and STANCE MANIFEST to be named first-class skeleton sections; C-38 requires commits to reference them by heading. Neither criterion requires the section itself to declare its own immutability. An output satisfying both can have a navigable, commit-referenced manifest whose lifecycle boundary is only inferrable from the phase lock — not stated at the artifact level. C-40 requires each manifest section to carry an explicit seal marker (`INERTIA INVARIANT: sealed at PHASE-1-COMMIT...` or equivalent) so the section is self-documenting: immutability is asserted at the source, not derived from the position of the commit that closed it.

**C-41 — Commit heading cross-references include an explicit bidirectionality constraint statement** *(new)*

Signal: V-04's "C-38 Explicit" axis. C-38 requires the commit to name the manifest section by heading, creating an implied bidirectional link. The link is structural but not stated — a model that updates the section without updating the commit pointer has violated no written rule. C-41 requires the cross-reference to include an explicit coupling clause in both directions (`modifications to that record require updating this commit; modifications to this commit require updating that record`), converting the pointer from a navigational reference into a governed contract. This is C-38's active-obligation upgrade, parallel to how C-32 upgraded C-31 (terminal-position rule must be stated, not assumed).

**Scoring**: aspirational pool 31 → 33; aspirational max 62 → 66; composite max **152 → 156**.
