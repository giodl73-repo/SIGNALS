Written to `simulations/quest/golden/listen-feedback-golden-2026-03-14.md`.

The document contains:

- **Frontmatter** as specified (skill, target, date, rounds 20, rubric v18, score 245, GOLDEN)
- **Exact V-05 simplified prompt body** verbatim — three sections (Persona Reference, Persona Feedback Cards with 8-field manifest, Blocker Escalation, Cross-Persona Theme Matrix)
- **5 "What made it golden" patterns:**
  1. Structured Field 1 sub-fields (A-16) — four named anchors, not prose
  2. Bilateral enforcement with conjunctive framing (A-17 + A-21) — each field names the other, omission is architecturally detectable
  3. Sub-field cross-reference chain (A-24) — A-16 is a structural prerequisite, confirmed by V-02's failure
  4. Directional delta separation (A-28) — asymmetric band-crossing effects reported as distinct lines
  5. Full CI enforcement stack at derivation (A-30 + A-31) — closes the retroactive decoration path
- **Rubric summary** across all three tiers (Essential/Recommended/Aspirational, 33 criteria, 255 pts max)
rt Lead | Ticket deflection, self-service coverage, escalation clarity |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |
| C-09 | Mobile-First User | Mobile responsiveness, offline capability, push notifications |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard navigation, screen reader compatibility |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure, input validation |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, business outcomes |

---

### Section 1 — Persona Feedback Cards

For each persona C-01 through C-12, produce a card using the numbered field manifest below. All numbered fields are required.

**C-NN — [Persona Role]**

1. **Current approach:**
   - **What it delivers:** Name the status-quo tool or workflow and what it provides this persona today.
   - **Where it falls short:** The specific gap or limitation the current approach does not address for this persona.
   - **Floor-level switching cost:** The minimum friction this persona bears when switching away from their current approach.
   - **Persona-specific workflow disruption:** How adoption would disrupt this persona's specific daily workflow, beyond the general switching cost.

2. **Gains from this spec** (requires corresponding **Losses and switching costs** [Field 3] — completing Field 2 without Field 3 constitutes bilateral coverage failure; anchor gain from **"Where it falls short"** in Field 1): One sentence naming what this persona gains from the spec relative to their current approach. Reference at least one named spec element.

3. **Losses and switching costs** (requires corresponding **Gains from this spec** [Field 2] — completing Field 3 without Field 2 constitutes bilateral coverage failure; anchor cost from **"Floor-level switching cost"** and **"Persona-specific workflow disruption"** in Field 1): One sentence naming what this persona gives up or bears when adopting.

4. **NPS:** [integer 1–10] — [one sentence synthesizing Fields 2 and 3 into a net score; reference at least one named spec element]

5. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

6. **Feedback** (blocking first, then major, minor, cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

7. **Willingness to adopt:** [percentage or Low/Medium/High]. Clears adoption threshold (>=60%): [Yes/No].

8. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

---

### Section 2 — Blocker Escalation

**Blockers Requiring Resolution:**

Aggregate every `blocking` severity item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist.

---

### Section 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

---

## What Made It Golden

**1. Structured Field 1 sub-fields (A-16)**
The `Current approach:` field is decomposed into four named sub-fields: *What it delivers*, *Where it falls short*, *Floor-level switching cost*, and *Persona-specific workflow disruption*. This is not a label — it is a structured baseline that forces the model to produce differentiable components rather than undifferentiated prose. These named sub-fields become the downstream anchors for Fields 2 and 3.

**2. Bilateral enforcement with conjunctive framing (A-17 + A-21)**
Fields 2 and 3 are not independent outputs. Each instruction explicitly names the other field by label and declares that completing one without the other constitutes a bilateral coverage failure. This creates a conjunctive constraint: the model cannot close Field 2 without Field 3 present, and vice versa. Prior variations (V-01) had bilateral intent but no structural prohibition — omission was instructionally discouraged but not architecturally detectable.

**3. Sub-field cross-reference chain (A-24)**
Fields 2 and 3 each anchor their content to a specific named sub-field from Field 1 — gains anchor to *"Where it falls short"*, costs anchor to *"Floor-level switching cost"* and *"Persona-specific workflow disruption"*. This makes bilateral completeness a structural side-effect of Field 1 granularity: a model cannot satisfy A-24 unless A-16's sub-fields exist. V-02 demonstrated this gating relationship — bilateral fields present, no named sub-fields, A-24 structurally unreachable.

**4. Directional delta separation (A-28)**
Sensitivity analysis reports `Upward delta (+1)` and `Downward delta (-1)` as distinct lines per high-influence persona rather than a single symmetric ±1 figure. When a score sits at the 6/7 or 8/9 boundary, the upward move crosses a band threshold while the downward move does not — producing qualitatively different narrative implications that a symmetric ±1 silently suppresses. V-03 and V-05 pass; V-01/V-02/V-04 fail on this criterion.

**5. Full CI enforcement stack co-located at derivation (A-30 + A-31)**
The CI formula is required at generation time (A-30: cannot reach D.2 without formula stated at D.1) and the failure mode is annotated inline with the constraint itself (A-31: "without the formula parenthetical, a reader cannot confirm whether the interval was computed via the correct method"). This closes the retroactive decoration path — a formula added to the output after computation is detectable as a protocol violation. Combined with A-29 (formula required in output), the full stack eliminates three independent failure paths simultaneously.

---

## Final Rubric Summary (v18)

### Essential (75 pts max — 15 pts each)

| ID | Criterion |
|----|-----------|
| C-01 | 12 persona cards present |
| C-02 | NPS score and justification per card |
| C-03 | Severity-labeled feedback per card |
| C-04 | Aggregate NPS computed and threshold applied |
| C-05 | Cross-persona theme matrix present |

### Recommended (15 pts)

| ID | Criterion |
|----|-----------|
| R-01 | Blocking issues escalated |

### Aspirational (165 pts max — 5 pts each)

| ID | Criterion | Category |
|----|-----------|----------|
| A-01 to A-08 | Persona card completeness and structural fidelity | coverage |
| A-09 | Current approach field labeled | format |
| A-10 to A-15 | NPS reasoning, spectrum diversity, aggregate computation | correctness |
| A-16 | Structured 4-sub-field Current approach | depth |
| A-17 | Bilateral gains/losses coverage enforced | depth |
| A-18 to A-20 | Persona influence weighting, band distribution, sensitivity | depth |
| A-21 | Conjunctive framing (each field names the other) | depth |
| A-22 to A-23 | Revision recommendations, adoption threshold | depth |
| A-24 | Field completion requires invoking named A-16 sub-field | depth |
| A-25 | UX-before-PM rationale co-located with ordering instruction | depth |
| A-26 | Persona influence weighting present | depth |
| A-27 | Failure mode annotation co-located with constraint | depth |
| A-28 | Directional sensitivity: upward/downward delta reported separately | depth |
| A-29 | CI formula in output format | depth |
| A-30 | Derivation-phase protocol (formula enforced at generation time) | depth |
| A-31 | CI formula failure mode named at point of constraint | depth |
| A-32 | CI formula enforcement stack complete (A-29 + A-30 + A-31 simultaneously) | depth |
| A-33 | Bilateral field system complete (A-16 + A-17 + A-21 + A-24 simultaneously) | depth |

**Score:** 245 / 245 (100%) — V-05, Round 20
