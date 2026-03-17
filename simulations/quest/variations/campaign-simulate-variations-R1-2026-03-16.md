Written to `simulations/quest/golden/campaign-simulate-variate-R1-2026-03-16.md`.

---

## campaign-simulate -- Round 1 Variations

**Axes chosen:** Output format (V-01), Lifecycle emphasis (V-02), Phrasing register (V-03) as single-axis; Output format + Lifecycle emphasis (V-04) and Phrasing register + Blast radius prominence (V-05) as combinations.

---

### V-01 -- Output Format
**Axis:** Mandatory finding schema table defined before execution begins. All columns required; blank cells fail.
**Hypothesis:** C-06 and C-04 pass by construction -- source, spec location, and blast radius are enumerated columns. C-05 passes because "Spec Location" has an explicit rule that vague references fail. Hardest remaining: C-09 (cross-skill patterns), which the table structure alone won't surface.

### V-02 -- Lifecycle Emphasis
**Axis:** Each sub-skill runs a 3-phase cycle (setup / execute / extract) before the campaign advances. Sequential gate is structural.
**Hypothesis:** The setup phase makes silent skipping impossible (C-01), enforces ordering (C-02), and drives C-05 because the setup phase requires naming what spec sections are under examination.

### V-03 -- Phrasing Register
**Axis:** Direct imperative "you" framing. The task is a pre-implementation gate: "before you write code, prove the spec holds."
**Hypothesis:** The gate framing makes C-05 natural -- pointing to a spec section is the only way to prove the spec failed. C-08 (remediation) becomes natural because "what to fix" is the explicit goal of a gate check.

### V-04 -- Combined (Output Format + Lifecycle Emphasis)
**Hypothesis:** Phase protocol closes silent-skipping gaps (C-01, C-02); mandatory schema closes vague-findings gaps (C-05, C-06). The synthesis section adds a mandatory cross-skill pattern table making C-09 required. Most scaffolded variation.

### V-05 -- Combined (Phrasing Register + Blast Radius Prominence)
**Hypothesis:** Organizing the entire report around blast radius from the first sentence makes C-04 and C-10 structural. Compounding findings surface naturally because they get elevated blast radius and the report rewards surfacing them. Risk: may cause authors to skip low-blast sub-skills, threatening C-01 and C-07.

---

**Hardest rubric criteria to pass across all variations:** C-05 (spec anchoring) is the most likely to regress in V-01 if the finding schema field rules aren't read carefully; C-09 (cross-skill patterns) is hardest to pass in V-03, which has no structural prompt for it. V-04 is the best positioned for complete rubric coverage; V-05 is the best positioned for C-04/C-10 excellence at the cost of C-01/C-07 risk.
