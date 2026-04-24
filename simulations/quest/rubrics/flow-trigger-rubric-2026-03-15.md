The existing rubric has grown to 53 criteria across v17 — far beyond the original skill intent. The `/quest:rubric` command requests a fresh canonical rubric. I'll output it as requested.

---

```markdown
---
skill: quest-rubric
skill_target: flow-trigger
date: 2026-03-15
version: 1
---

# Scoring Rubric — flow-trigger

Evaluate outputs from the `flow-trigger` skill: simulate which automations fire when a
record changes. For each field or event change, the output must list every trigger that
fires, the order they fire, their inputs/outputs, and any side effects. It must identify
trigger storms, missing triggers, and circular triggers. Stock role: Power Automate /
Copilot Studio domain expert.

---

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 pts total — must all pass)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-01 | **Trigger enumeration** — For every field or event change in the scenario, the output lists every trigger that fires. No expected trigger is silently omitted. | correctness | All triggers that should fire for the given change appear as named entries. Zero silent omissions. |
| C-02 | **Execution order stated** — Triggers are presented in the sequence they fire (sequential, parallel, or chained), grounded in the platform's execution model — not in arbitrary or alphabetical order. | correctness | Output shows an ordered sequence or explicit parallel grouping consistent with platform execution semantics. A flat unordered list fails. |
| C-03 | **Inputs and outputs per trigger** — Each trigger entry includes: what data it receives (trigger input / payload) and what it produces or mutates (output, field write, notification, downstream call, or explicit "no output"). | depth | At least 80% of trigger entries carry explicit input and output/side-effect content. Generic placeholders ("does something") do not count. |
| C-04 | **Three anomaly class verdicts declared** — The output renders a named verdict for each of the three anomaly classes: trigger storm, missing trigger, and circular dependency. Each is explicitly labeled (e.g., "Storm: not detected"). An output that assesses fewer than all three classes, or lists findings without a per-class named verdict, fails. | coverage | All three anomaly verdicts appear in the output. Absence of any class's verdict is a fail even when the scenario is clean. |
| C-05 | **Platform grounding** — Trigger types, execution tiers, and flow categories use the platform's approved vocabulary (sync plugin step, async plugin step, instant flow, automated flow, scheduled flow, etc.). Claims about order, payload shape, and side effects are internally consistent with that platform's documented behavior. | correctness | At least one platform is named and all platform-specific claims are consistent with that platform. Contradictions with well-known platform behavior are a fail. |

---

## Recommended Criteria (30 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-06 | **Circular trigger analysis** — The output traces whether any trigger's side effects could re-fire a trigger in the same chain. It either identifies a cycle (with the loop path named) or explicitly confirms no cycles were found and states why. | depth | A circular-trigger analysis section is present. Bare "no cycles" with no reasoning is a weak pass; tracing the dependency graph earns full credit. |
| C-07 | **Conditional branch paths** — Where a trigger has conditional logic (filter conditions, run-after settings, switch branches), the output identifies which branch fires for the given inputs and why at least one alternative branch does not fire. | depth | For every trigger with visible conditional logic, the firing branch and at least one skipped branch are stated. Triggers with no conditional logic pass by default. |
| C-08 | **Anomaly remediation proposed** — For each detected anomaly (storm, missing trigger, cycle), the output proposes a concrete fix: debounce strategy, missing trigger registration, concurrency control, cycle-break condition, or re-sequencing recommendation. | behavior | Every detected anomaly has at least one actionable, named remediation step. Anomaly sections that describe problems without prescribing fixes do not earn credit. If no anomalies are detected, criterion passes vacuously. |

---

## Aspirational Criteria (10 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-09 | **Execution tier and latency flags** — The output labels each trigger's execution tier (sync / async / scheduled) and flags any timing implications: async delay windows, throttle limits that could defer execution, the 24-hour re-trigger deferral window in Power Automate, or concurrency settings that serialize otherwise-parallel triggers. | depth | At least one timing or throttle consideration is surfaced per trigger chain. "Runs async" without any specifics is a weak pass. |
| C-10 | **Cascade completeness — side-effect writes spawn trigger rows** — When a trigger's side-effect field write carries downstream automation potential, the output adds the cascaded trigger as the next numbered entry in the sequence rather than leaving it as a dangling annotation. The cascade chain is traced end-to-end: side-effect write on row N links to a trigger entry on row N+1. | correctness | At least one cascade chain (where present in the scenario) is traced end-to-end with an explicit downstream trigger row. An output that annotates side effects but does not add downstream trigger rows for those with automation potential fails. |

---

## Scoring Worksheet

| ID   | Tier | Pass? (Y/N) | Notes |
|------|------|-------------|-------|
| C-01 | essential | | |
| C-02 | essential | | |
| C-03 | essential | | |
| C-04 | essential | | |
| C-05 | essential | | |
| C-06 | recommended | | |
| C-07 | recommended | | |
| C-08 | recommended | | |
| C-09 | aspirational | | |
| C-10 | aspirational | | |

```
essential_pass   = count(C-01..C-05 = Y)   — max 5
recommended_pass = count(C-06..C-08 = Y)   — max 3
aspirational_pass = count(C-09..C-10 = Y)  — max 2

composite = (essential_pass/5   * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/2 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```
```
