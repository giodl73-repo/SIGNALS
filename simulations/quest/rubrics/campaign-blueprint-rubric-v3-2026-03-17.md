Two new patterns from the JSON signal block map cleanly to new criteria. Signal 3 (blank-filling template) is already covered by C-11, so only the two named patterns need codifying.

**New criteria:**
- **C-15** — Pre-artifact forcing function (Signal 1)
- **C-16** — Named do-nothing propagation (Signal 2)

Max total rises from 120 → 130. Golden threshold adjusts proportionally (80/120 = 67% → 87/130).

---

```markdown
## campaign-blueprint Rubric v3

**5 Essential (60 pts):**
- **C-01** — All three artifacts present and written to correct paths (spec/proposal/pitch)
- **C-02** — Spec has all five required sections: PURPOSE, REQUIREMENTS (MoSCoW), DESIGN, CONSTRAINTS, OPEN QUESTIONS
- **C-03** — Proposal has three options minimum including a do-nothing option, with RECOMMENDATION
- **C-04** — Pitch has three distinct audience versions: exec / developer / maker
- **C-05** — Sequence integrity: proposal references spec decisions, pitch references proposal's recommended option — no cross-artifact contradictions

**3 Recommended (30 pts):**
- **C-06** — Inertia baseline anchored in all three artifacts (what users do today / cost of not building)
- **C-07** — Scout signal scan performed; available signals incorporated into the appropriate artifact
- **C-08** — Spec self-review flags at least two specific open questions or gaps (not boilerplate)

**8 Aspirational (40 pts):**
- **C-09** — Artifact contract matrix (READ/WRITE/PRESERVE/CARRIES FORWARD) declared before execution begins
- **C-10** — Pitch contains explicit anti-positioning section with at least two "what this is NOT" statements
- **C-11** — Proposal's do-nothing option includes a quantified cost-of-inertia template with at least one concrete dimension (time, effort, or risk) — not qualitative description only
- **C-12** — Execution gate markers present: each artifact phase ends with a visible completion tag (e.g., `[SPEC WRITTEN]`, `[PROPOSAL WRITTEN — Option X recommended]`, `[PITCH WRITTEN]`) making execution state auditable in output
- **C-13** — Open questions split by discipline: spec includes at least one question from the product/user domain and at least one from the technical/architecture domain
- **C-14** — Per-audience delta statement: each pitch version contains an explicit "what changes for [audience]" statement — not just audience-appropriate language, but a named delta from the base recommendation
- **C-15** — Pre-artifact forcing function: a dedicated setup phase (e.g., Phase 0) is completed before any artifact is written; this phase anchors the inertia baseline and any cross-artifact invariants so that C-06 and C-03 compliance becomes structurally enforced rather than instructionally hoped for
- **C-16** — Named do-nothing propagation: the do-nothing option is assigned an explicit name in the setup phase (e.g., "Option 0: Status Quo") and that name propagates through the proposal options list and pitch framing — it is a tracked entity, not a catch-all final option

**Scoring:**
- Essential: 12 pts each = 60 pts max
- Recommended: 10 pts each = 30 pts max
- Aspirational (C-09–C-10): 5 pts each = 10 pts
- Aspirational (C-11–C-16): 5 pts each = 30 pts
- **Max total: 130 pts**
- PARTIAL = half criterion value; NO/FAIL = 0

**Golden threshold:** all 5 essentials at FULL + composite ≥ 87/130 (67%).
```

---

**What changed and why:**

| New criterion | Source | Pattern extracted |
|---|---|---|
| C-15 | V-01 Signal 1 | Phase 0 as a mandatory pre-artifact block makes inertia anchoring structurally inevitable across all three artifacts — distinct from C-09 (contract matrix) which is declarative, not temporal |
| C-16 | V-01 Signal 2 | Naming the do-nothing option in Phase 0 turns it into a tracked entity that carries forward by reference through proposal and pitch — prevents it from being a generic final fallback |

Signal 3 (blank-filling quantification template with forced dimension selection) is already captured by C-11's "concrete dimension" requirement and was not added as a separate criterion.
