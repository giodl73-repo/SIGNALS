Here are the five complete Round 2 variations, written against rubric v2 (C-01–C-12, 115 pts).

---

## Summary: variation axes and rubric coverage

| Variation | Primary axis | Key C-10/C-11/C-12 mechanisms |
|-----------|-------------|-------------------------------|
| **V-01 — Role sequence** | Role map → phase grouping → handoff gates | C-10: BAD/GOOD gate table in Step 3. C-11: echo pre-positioned in YAML template. C-12: role catalog table (anchor-1 for C-03/C-04) + YAML inline gate comments (anchor-2). |
| **V-02 — Annotated skeleton** | Pre-filled YAML with `# REQUIRED`/`# BAD`/`# GOOD` markers | C-10: inline `# BAD:` / `# GOOD:` at every gate slot. C-11: echo pre-placed with `# REQUIRED: DO NOT REMOVE`; skeleton makes correct output path of least resistance. C-12: prose rules section + skeleton inline comments = dual anchor for all 4 essentials. |
| **V-03 — Question framing** | Each stage = investigation question; gate = "what proves we answered it?" | C-10: BAD/GOOD table contrasting "skill ran" vs "question answered." C-11: echo framed as structural non-question, separating it from skill stages. C-12: question bank (anchor-1 for C-03/C-04) + `# Question:` YAML comment (anchor-2). |
| **V-04 — Bands + roles (combined)** | Four lifecycle bands (Prove It / Design It / Simulate It / Listen Ahead) with role-handoff boundaries | C-10: BAD flat-plan vs GOOD banded-plan opening contrast. C-11: band structure in YAML template enforces namespace ordering; echo `# REQUIRED` after Band 4. C-12: per-band catalogs (anchor-1 for C-03) + YAML band-divider inline options (anchor-2). |
| **V-05 — Inertia + annotated template (golden synthesis)** | BAD/GOOD YAML pair + pre-annotated template + pre-printed checklist | C-10: labeled BAD/GOOD YAML pair targeting gate specificity and skill ordering. C-11: echo `# REQUIRED: DO NOT REMOVE` + layer divider comments enforce both C-02 and C-05 structurally. C-12: opening contrast + template annotations + checklist = triple anchor for all 4 essentials. |

**Key R2 advances over R1:**

1. **C-12 coverage is deliberate**: every variation explicitly lists two independent anchors for each of C-01–C-04, not just C-04 and C-07.
2. **C-11 targets essential criteria**: R1 V-04 used bands to enforce C-05 (recommended). R2 V-02/V-05 embed `# REQUIRED` annotations directly at the echo position and gate positions to enforce C-02 and C-04 structurally.
3. **C-10 in every variation**: R1 had contrast only in V-05. All five R2 variations include a BAD/GOOD pair anchored to an essential criterion.
4. **V-05 is the golden candidate**: opening identity (C-07, C-12 anchor-1) + BAD/GOOD YAML (C-10, C-12 anchor-2) + annotated template (C-11) + pre-printed checklist (C-11, C-12 anchor-3) + layer dividers (C-05, C-09).

Written to `simulations/quest/golden/program-plan-variate-R2-2026-03-15.md`.
