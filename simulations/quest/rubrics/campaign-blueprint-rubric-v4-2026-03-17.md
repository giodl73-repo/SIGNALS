Now I have all the signals. The scorecard's JSON block has two new patterns. Signal 2 (inertia-first ordering) is a negative finding — explicitly noted as not changing the score — so only Signals 1 and 3 become new criteria.

**Pattern extraction:**

| Signal | Source | Pattern | Becomes |
|--------|--------|---------|---------|
| Signal 1 | V-02, V-04 (130/130 differentiator) | C-09 + C-15 + C-16 co-located in Phase 0 form a single structural gate — satisfying Phase 0 satisfies all three simultaneously | C-17 |
| Signal 2 | V-04 vs V-02 | Inertia-first ordering does NOT add score over neutral ordering when ledger template present | Not a criterion — diagnostic finding |
| Signal 3 | V-05 (127.5/130) | A 4-field Phase 0 block achieves full C-15/C-16 credit; gate marker and propagation rule are load-bearing, not density | C-18 |

---

```markdown
## campaign-blueprint Rubric v4

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

**10 Aspirational (50 pts):**
- **C-09** — Artifact contract matrix (READ/WRITE/PRESERVE/CARRIES FORWARD) declared before execution begins
- **C-10** — Pitch contains explicit anti-positioning section with at least two "what this is NOT" statements
- **C-11** — Proposal's do-nothing option includes a quantified cost-of-inertia template with at least one concrete dimension (time, effort, or risk) — not qualitative description only
- **C-12** — Execution gate markers present: each artifact phase ends with a visible completion tag (e.g., `[SPEC WRITTEN]`, `[PROPOSAL WRITTEN — Option X recommended]`, `[PITCH WRITTEN]`) making execution state auditable in output
- **C-13** — Open questions split by discipline: spec includes at least one question from the product/user domain and at least one from the technical/architecture domain
- **C-14** — Per-audience delta statement: each pitch version contains an explicit "what changes for [audience]" statement — not just audience-appropriate language, but a named delta from the base recommendation
- **C-15** — Pre-artifact forcing function: a dedicated setup phase (e.g., Phase 0) is completed before any artifact is written; this phase anchors the inertia baseline and any cross-artifact invariants so that C-06 and C-03 compliance becomes structurally enforced rather than instructionally hoped for
- **C-16** — Named do-nothing propagation: the do-nothing option is assigned an explicit name in the setup phase (e.g., "Option 0: Status Quo") and that name propagates through the proposal options list and pitch framing — it is a tracked entity, not a catch-all final option
- **C-17** — Compound Phase 0 co-location: the artifact contract matrix (C-09), the pre-artifact forcing function (C-15), and the named do-nothing propagation (C-16) are all placed inside Phase 0, making them structurally co-dependent at a single mandatory gate — an executor who completes Phase 0 satisfies all three simultaneously with no separate declaration step that can be skipped
- **C-18** — Canonical Phase 0 form: Phase 0 specifies an explicit minimum field list (inertia baseline, Option 0 name, Option 0 cost, scout result) and names the gate marker and propagation rule as the load-bearing elements — the skill makes clear that density beyond these fields is not required for C-15/C-16 compliance, removing executor ambiguity about what Phase 0 must contain

**Scoring:**
- Essential: 12 pts each = 60 pts max
- Recommended: 10 pts each = 30 pts max
- Aspirational (C-09–C-10): 5 pts each = 10 pts
- Aspirational (C-11–C-18): 5 pts each = 40 pts
- **Max total: 140 pts**
- PARTIAL = half criterion value; NO/FAIL = 0

**Golden threshold:** all 5 essentials at FULL + composite ≥ 94/140 (67%).
```

---

**What changed and why:**

| New criterion | Source | Pattern extracted |
|---|---|---|
| C-17 | V-02, V-04 (Signal 1) | Placing C-09 + C-15 + C-16 inside Phase 0 removes three independent obligations and replaces them with one structural gate — the compound gate is observable and scoreable as a distinct property from any of the three individual criteria |
| C-18 | V-05 (Signal 3) | Minimal sufficiency confirmation: a 4-field Phase 0 achieves full C-15/C-16 credit; naming the canonical form and identifying the load-bearing elements (gate + propagation rule) is a skill design property distinct from whether Phase 0 is physically present |

Signal 2 (inertia-first ordering, V-04) was not codified: the scorecard explicitly shows it does not add score over neutral ordering when the ledger template is present. The ledger template is the load-bearing element, already captured by C-16.

**Scoring math:** 130 → 140 (+2 aspirational × 5 pts). Golden threshold: 87/130 = 66.9% → 94/140 (67.1%).
