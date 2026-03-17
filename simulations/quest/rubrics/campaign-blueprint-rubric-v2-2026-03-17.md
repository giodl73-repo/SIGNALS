Looking at the scorecard, I'll extract patterns that scored FULL and represent behaviors above what the existing criteria capture:

- **V-01**: Do-nothing option has an explicit inertia quantification template; pitch versions each state "what changes for that audience specifically"
- **V-02**: Dependency check + completion tags (`[PROPOSAL WRITTEN — Option X recommended]`) make execution state auditable; C-05 mechanically enforced
- **V-03**: PM surfaces business/user unknowns, Architect surfaces technical unknowns — two distinct gap disciplines
- **V-05**: Phase 0 setup before writing any artifact makes omission nearly impossible

Four new aspirational criteria: **C-11** (quantified do-nothing), **C-12** (execution gate markers), **C-13** (discipline-split open questions), **C-14** (per-audience delta statement).

```markdown
## campaign-blueprint Rubric v2

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

**6 Aspirational (30 pts):**
- **C-09** — Artifact contract matrix (READ/WRITE/PRESERVE/CARRIES FORWARD) declared before execution begins
- **C-10** — Pitch contains explicit anti-positioning section with at least two "what this is NOT" statements
- **C-11** — Proposal's do-nothing option includes a quantified cost-of-inertia template with at least one concrete dimension (time, effort, or risk) — not qualitative description only
- **C-12** — Execution gate markers present: each artifact phase ends with a visible completion tag (e.g., `[SPEC WRITTEN]`, `[PROPOSAL WRITTEN — Option X recommended]`, `[PITCH WRITTEN]`) making execution state auditable in output
- **C-13** — Open questions split by discipline: spec includes at least one question from the product/user domain and at least one from the technical/architecture domain
- **C-14** — Per-audience delta statement: each pitch version contains an explicit "what changes for [audience]" statement — not just audience-appropriate language, but a named delta from the base recommendation

**Scoring:**
- Essential: 12 pts each = 60 pts max
- Recommended: 10 pts each = 30 pts max
- Aspirational (C-09–C-10): 5 pts each = 10 pts
- Aspirational (C-11–C-14): 5 pts each = 20 pts
- **Max total: 120 pts**
- PARTIAL = half criterion value; NO/FAIL = 0

**Golden threshold:** all 5 essentials at FULL + composite ≥ 80/120 (67%).
```

---

**What changed and why:**

| New criterion | Source variant | Pattern extracted |
|---|---|---|
| C-11 | V-01 | Do-nothing option with quantified inertia template scored FULL on C-03 — the quantification is what made it "strongest of all non-V05 variants" |
| C-12 | V-02 | Completion tags enforced C-03/C-04 mechanically; dependency check made C-05 the "strongest on this criterion" — the auditability pattern is the driver |
| C-13 | V-03 | Two distinct gap sources (PM + Architect) made C-08 FULL where other variants were PARTIAL — discipline split is the differentiator |
| C-14 | V-01 | "Each pitch version must state what changes for that audience specifically" is distinct from C-10 (anti-positioning) — it's positive delta framing, not negation framing |

Note: the golden threshold denominator changes from 100 to 120. Variants V-01 and V-02 that scored 82.5/100 (82.5%) would need re-scoring against the new max.
