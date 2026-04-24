---

## org-roles Round 2 — 5 Variations

**Round 2 Variation Map**

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | role-sequence | Context analysis + domain expert derivation in Step 1 only; stock roles load in Step 2 — structurally enforces C-11 by forcing domain-specific language to be committed before PM/Architect/Strategy archetypes appear |
| V-02 | output-format | Fill-in-the-blank file template with every field/sub-field pre-named as a required slot — makes C-01 omission structurally visible and satisfies C-13 by embedding the format definition in the step |
| V-03 | phrasing-register | Every schema field has a `FAILURE MODE:` line naming the exact collapse pattern (frame→task-list, serves→frame-restatement, simplify→scope-description) — targets C-12 directly, secondary benefit to C-06/C-07 |
| V-04 | role-sequence + output-format | Combines V-01 context-first ordering with V-02 explicit templates — closes the co-occurring failure cluster of generic domain experts (C-11) + missing fields (C-01, C-13) |
| V-05 | phrasing-register + lifecycle-emphasis | Four-phase lifecycle with DO/DO NOT instructions and per-phase completion conditions — C-12 from named failure modes throughout, C-13 from completion conditions requiring output to be present and structurally correct before advancing |

---

**Key structural differences from Round 1 (org-chart):**

Round 1 variated on inertia framing, section scaffolds, role sequence for loading (not deriving), and imperative register. Round 2 targets the three new v2 criteria:

- **C-11** addressed by V-01/V-04: the ordering constraint is on derivation vs. loading, not just read-first-vs-read-later
- **C-12** addressed by V-03/V-05: `FAILURE MODE:` lines name the collapse patterns, not just the positive requirement
- **C-13** addressed by V-02/V-04/V-05: templates and completion conditions define output format at the step level, eliminating heading-only stubs

Output written to `simulations/quest/golden/org-roles-variate-R2-2026-03-16.md`.
