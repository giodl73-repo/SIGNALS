---
skill: quest-variate
skill_target: scout-risk
round: 1
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-risk-rubric-v1-2026-03-16.md
axes_explored: [output-format, inertia-framing, phrasing-register, role-sequence+lifecycle, full-integration]
---

# scout-risk — Prompt Variations R1

Five complete, runnable skill body prompts. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

---

## V-01 — Axis: Output Format (table-first)

**Hypothesis**: A strict table schema enforces the three-field anatomy (severity/likelihood/mitigation) and dimension labeling structurally — the model cannot omit a column from every row. This should produce near-perfect C-03 and C-06 compliance. Risk: inertia may lose its primacy if it gets visually flattened into a row.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a risk register for the topic. The register surfaces what could go wrong before commitment is made.

STEP 1 — INERTIA RISK (always first, always its own row)

Before listing any other risks, assess the inertia risk: the risk that the status quo was sufficient and this feature is the wrong thing to build. Give it dimension label "Inertia". Assign severity, likelihood, and mitigation the same as any other risk.

STEP 2 — RISK REGISTER TABLE

Output as a markdown table with these columns:

| # | Dimension | Risk | Severity | Likelihood | Mitigation |

Rules:
- # starts at 0 for inertia, then 1, 2, 3... for all others
- Dimension values: Inertia / Technical / Market / Compliance / Dependency / Timeline
- Severity values: HIGH / MEDIUM / LOW (no other values)
- Likelihood: a condition or scenario, not just "possible" or "unlikely"
- Mitigation: a concrete action, owner class, or control — not "monitor closely"
- Cover at least 3 of the 5 non-inertia dimensions (Technical, Market, Compliance, Dependency, Timeline)
- Order rows after inertia by severity descending (HIGH → MEDIUM → LOW)

STEP 3 — AMEND (if present in prompt)

If the prompt includes AMEND: focus on [dimension] or AMEND: adjust severity threshold to [level], apply that transformation to the table. Retain inertia (row 0) regardless of the amendment scope. Re-sort after applying the amendment.

STEP 4 — WRITE ARTIFACT

Write to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-02 — Axis: Inertia Framing (prominent status-quo competitor)

**Hypothesis**: Giving inertia its own named section with rich prose analysis before the main register makes C-01 (inertia first) structurally unavoidable and produces a deeper inertia entry. Risk: the expanded inertia prose may push the model toward generic "status quo is comfortable" writing rather than topic-specific analysis.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a risk register for the topic. The register is organized into two parts: the inertia risk (always first, always its own section) and the dimensional risk register (technical, market, compliance, dependency, timeline).

---

## 0. Inertia Risk — The Status Quo Competitor

This is always risk #0. It is the risk that the current state of the world is good enough — that the feature being built solves a problem the market does not actually have, or solves it at a cost that exceeds the value delivered.

Assess:
- What would a team or user do instead of adopting this feature?
- What does "doing nothing" cost them, and how visible is that cost?
- What makes inertia sticky for this specific domain?

Then state the inertia risk in the standard anatomy:
- **Severity**: HIGH / MEDIUM / LOW
- **Likelihood**: [specific condition or scenario]
- **Mitigation**: [concrete action to reduce this risk before commitment]

---

## 1. Dimensional Risk Register

List risks across the five dimensions. Cover at least 3 of the 5. For each risk:

**[Dimension]: [Risk title]**
- Severity: HIGH / MEDIUM / LOW
- Likelihood: [condition or scenario — not just "possible"]
- Mitigation: [concrete action, owner class, or control — not "monitor closely"]

Dimensions:
- **Technical** — implementation unknowns, platform constraints, irreversible architectural choices
- **Market** — adoption risk, wrong-audience fit, timing
- **Compliance** — regulatory exposure, policy constraints, audit surface
- **Dependency** — third-party library, platform API, vendor lock-in
- **Timeline** — schedule risk, scope creep, blocking dependencies

Order: highest severity first within the dimensional register.

---

## 2. Risk Interdependencies (optional but valuable)

If any two risks compound each other — if one materializing raises the severity of another — note it explicitly. Example: "If Market risk M-1 materializes, Timeline risk T-2 escalates to HIGH."

---

## 3. AMEND (if present in prompt)

AMEND: focus on [dimension] — narrow the dimensional register to that dimension only. Retain inertia (section 0) regardless.
AMEND: adjust severity threshold to [level] — exclude risks below that severity from the register. Retain inertia regardless.

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-03 — Axis: Phrasing Register (imperative/conversational)

**Hypothesis**: Direct imperative instructions ("Do X. Then do Y. Never do Z.") produce more literal compliance with hard structural rules like C-01 (inertia first) and C-04 (severity scale). A model following commands is less likely to drift than one following descriptions. Risk: imperative tone may produce a mechanical register that misses the depth needed for C-05 and C-07.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Here is the exact sequence to follow.

**First: write the inertia risk.**

The inertia risk is always entry #1. It is the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip this. Do not move it. Do not bury it after technical risks. Write it first.

Give it:
- Severity: one of HIGH, MEDIUM, or LOW — nothing else
- Likelihood: name the condition that would make this risk real, not just "possible"
- Mitigation: name what the team should do to test whether inertia applies before building

**Second: write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5–10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: what specific condition or scenario triggers this risk
- Mitigation: a concrete action — not "monitor the situation", not "be careful", not "consider alternatives"

Sort the dimensional risks from highest to lowest severity.

**Third: check your mitigations.**

Read back every mitigation you wrote. If two or more say something like "monitor closely", "keep an eye on", "revisit later", or "consider alternatives" — replace them. A mitigation must name what someone should do or check, not that something should happen eventually.

**Fourth (only if AMEND is in the prompt):**

If the prompt contains AMEND: focus on [dimension], remove all dimensional risks except that dimension. Keep inertia.
If the prompt contains AMEND: adjust severity threshold to [level], remove risks below that level. Keep inertia.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-04 — Axis: Role Sequence + Lifecycle Emphasis (explicit multi-role protocol)

**Hypothesis**: Running three named analyst roles in an explicit sequence — each contributing risks from their distinctive lens — produces better dimensional coverage (C-02) and richer mitigations (C-05) because each role has a different failure-mode vocabulary. The explicit lifecycle (Setup → Roles → Synthesis → Amend) helps the model stay on task across a longer prompt. Risk: the role protocol may produce redundant risks or dilute the clarity of the inertia-first rule.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal artifacts). Do not prompt unless context is absent.

Run the scout-risk lifecycle in four phases.

---

### PHASE 1 — SETUP

Identify: topic name, product or feature scope, team context (if inferrable). Summarize in 2–3 sentences. This context feeds all three analyst roles.

---

### PHASE 2 — ANALYST ROLES

Run each role in sequence. Each contributes risks from their lens.

**Role A: The Skeptic**
Lens: "Why will this fail to deliver value?"
Focus dimensions: Inertia (always), Market, Compliance
Required output:
- Inertia risk (first, with severity/likelihood/mitigation)
- 1–2 Market or Compliance risks (with severity/likelihood/mitigation)

**Role B: The Realist**
Lens: "What will break during implementation?"
Focus dimensions: Technical, Dependency
Required output:
- 2–3 Technical or Dependency risks (with severity/likelihood/mitigation)

**Role C: The Scheduler**
Lens: "What will blow the timeline?"
Focus dimensions: Timeline, Dependency (cross-check with Role B)
Required output:
- 1–2 Timeline risks (with severity/likelihood/mitigation)
- Note if any Dependency risk from Role B also appears here (interdependency)

---

### PHASE 3 — SYNTHESIS

Merge all risks into a single ordered register. Rules:
- Inertia (from Role A) is always position #1
- All other entries sorted by severity descending (HIGH → MEDIUM → LOW)
- Each entry carries: Dimension, Risk title, Severity, Likelihood, Mitigation
- Severity scale: HIGH / MEDIUM / LOW only
- Mitigations must be specific actions — not "monitor", not "revisit"
- Cover at least 3 of the 5 non-inertia dimensions

If Role B and Role C flagged the same Dependency risk independently, note the interdependency explicitly.

---

### PHASE 4 — AMEND (if present in prompt)

AMEND: focus on [dimension] — retain inertia, drop all other dimensions not matching [dimension].
AMEND: adjust severity threshold to [level] — retain inertia, drop risks below [level].

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-05 — Axis: Full Integration (format + inertia + imperative + roles + interdependencies)

**Hypothesis**: Combining the strongest signals from each single-axis variation — table schema from V-01, named inertia section from V-02, imperative structural rules from V-03, role sequence from V-04, and explicit interdependency requirement from the rubric — produces the highest composite score. The table format enforces C-03/C-06 compliance; the named section enforces C-01; the imperative rules reinforce C-04/C-05; the roles drive C-02 coverage; the interdependency instruction unlocks C-09. Risk: the combined prompt is long and may cause the model to lose the imperative force of the individual rules.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal artifacts). Do not prompt unless context is absent.

Build a risk register. Follow these steps in order. Do not skip any step.

---

**STEP 1 — INERTIA RISK (mandatory, always first)**

Write the inertia risk before anything else. The inertia risk is: the risk that the status quo is good enough and this feature is the wrong thing to build.

Run the Skeptic lens: given what this topic does and who it is for, what does the team or user do instead? How sticky is that alternative? What does building this cost relative to the value it delivers?

Output the inertia risk in this exact format:

**0. Inertia — [one-line risk title]**
- Dimension: Inertia
- Severity: HIGH / MEDIUM / LOW
- Likelihood: [name the specific condition that makes inertia win]
- Mitigation: [name the concrete pre-build test or gate that would resolve this risk]

---

**STEP 2 — DIMENSIONAL RISKS (3 roles, table output)**

Run three analyst roles. Each contributes risks from their lens. Then merge all into a single table.

Roles:
- **Skeptic** (Market, Compliance): why will this fail to deliver value?
- **Realist** (Technical, Dependency): what will break during build?
- **Scheduler** (Timeline, cross-check Dependency): what will slip the date?

Cover at least 3 of the 5 dimensions: Technical, Market, Compliance, Dependency, Timeline.

Merge all role contributions into this table, sorted by severity descending after inertia:

| # | Dimension | Risk | Severity | Likelihood | Mitigation |
|---|-----------|------|----------|------------|------------|

Rules — enforce these absolutely:
- Severity: only HIGH, MEDIUM, or LOW. No numbers, percentages, or invented labels.
- Likelihood: a specific condition or scenario. Not "possible", not "may occur".
- Mitigation: a named action, owner class, or control. Not "monitor closely", not "keep an eye on", not "be careful". If you write a generic hedge, replace it.

---

**STEP 3 — INTERDEPENDENCIES**

Read all risks in the table. If any two risks compound each other — if one materializing raises the severity or likelihood of another — write a one-line note:

"If [Risk A] materializes, [Risk B] escalates to [severity]."

At least one interdependency is expected for most topics. If none exist, write "No compound risks identified."

---

**STEP 4 — SELF-CHECK**

Before writing the artifact, verify:
- [ ] Inertia is row 0 (before any Technical/Market/Compliance/Dependency/Timeline risk)
- [ ] Severity values are only HIGH, MEDIUM, or LOW
- [ ] At least 3 dimensions covered in the table
- [ ] Fewer than 2 mitigations are generic non-actions
- [ ] Rows after inertia are sorted high-to-low severity

Fix any violation before proceeding.

---

**STEP 5 — AMEND (if present in prompt)**

AMEND: focus on [dimension] — keep inertia (row 0), remove all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0), remove rows below [level]. Re-sort.

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## Variation Summary

| ID | Axis | Key Structural Bet | Expected C-01 | Expected C-03 | Expected C-05 | Expected C-06 | Expected C-09 |
|----|------|--------------------|---------------|---------------|---------------|---------------|---------------|
| V-01 | Output format (table) | Table schema enforces anatomy fields | Medium (row 0 convention) | High (columns required) | Medium (no explicit anti-generic rule) | High (Dimension column) | Low (no prompt) |
| V-02 | Inertia framing (named section) | Own section makes C-01 impossible to miss | High (own section) | Medium (anatomy stated once) | Medium | Medium | Medium (optional section) |
| V-03 | Phrasing register (imperative) | Commands reduce drift on structural rules | High (explicit "write it first") | High (step-by-step anatomy) | High (explicit re-check step) | Medium | Low |
| V-04 | Role sequence + lifecycle | Roles drive dimensional coverage | High (Role A owns inertia) | High (anatomy per role) | High (roles name actions) | Medium | High (Role B/C cross-check) |
| V-05 | Full integration | All wins combined; self-check gate | High (step 1 owns inertia) | High (table + self-check) | High (explicit replace rule) | High (Dimension column) | High (step 3 explicit) |
