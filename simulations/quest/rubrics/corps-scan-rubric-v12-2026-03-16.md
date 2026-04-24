Written to `simulations/quest/rubrics/corps-scan-rubric-v12-2026-03-17.md`.

**Four new criteria from R12:**

| ID | Name | Source | Extends | New dimension |
|----|------|--------|---------|---------------|
| C-45 | Hypothesis contract fields carry machine-readable type annotations | V-01 | C-41 | Each PREDICTED-MODE / STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL field carries `[type: ...]` — turns the labeled contract into a typed schema |
| C-46 | DARK SIGNALS Penalty column typed as composite `[label:string, magnitude:0-4]` | V-01 | C-43 | Adds numeric severity magnitude alongside label citation — penalty is now quantified, not binary |
| C-47 | Net Score delta annotated as independently verifiable | V-01 | C-44 | Inline `(independently verifiable)` declaration on the amend delta — closes the audit chain from table to recommendation |
| C-48 | Deliberation table carries organizational cost dimension beyond evidence structure | V-02 | C-43 | Inertia Cost (or equivalent) as a 5th column orthogonal to evidence-for/against — makes pivot selection cost-weighted, not only signal-weighted |

**Scoring: 270 → 290 pts** (40 aspirationals × 5 = 200 + 90). Golden threshold unchanged at 80 pts.

**R12 reference scores under v12:** V-01 = 285/290 (passes C-45/C-46/C-47, fails C-48). V-02 = 275/290 (passes C-48, fails C-45/C-46/C-47). The axes remain orthogonal — V-01 deepens the typing and audit layer; V-02 extends the deliberation table into organizational cost territory.
