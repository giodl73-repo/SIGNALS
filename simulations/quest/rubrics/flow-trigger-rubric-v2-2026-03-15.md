Reading the scorecard carefully for cross-variation excellence signals before writing the updated rubric.

The patterns that appear consistently across all four scored variations but aren't captured as criteria:

1. **Denominator declaration** — every high-scoring variation pre-scanned candidates and named a count before enumeration. Outputs that do this make completeness auditable without relying on the scorer's memory.

2. **Gap tokens in enumeration sequence** — V-01 and V-04 explicitly place `[FLAGGED GAP]` / `[NOT IN PASS 2 CHAIN]` tokens for candidates that don't fire, rather than silently omitting them. This is distinct from C-01 (no silent omissions of *fired* triggers) — it's about explicitly disposing of *non-firing* candidates.

3. **Anomaly verdict evidence citation** — V-02 and V-04 required anomaly verdicts to cite specific numbered rows. "Storm: not detected" without a row citation was flagged as weak-pass. This isn't captured by C-04 (which only requires verdicts to exist) or C-06/C-08 (which address depth/remediation).

These three become C-11, C-12, C-13 in the aspirational tier. The formula denominator for aspirational grows from 2 to 5.

---

```markdown
---
skill: quest-rubric
skill_target: flow-trigger
date: 2026-03-15
version: 2
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
| C-11 | **Candidate denominator declared** — Before the detailed trigger enumeration begins, the output states the full set of trigger candidates considered: a named list or explicit count of every trigger that was evaluated, including those that did not fire. This makes completeness auditable independent of the scorer's platform knowledge. | coverage | The output contains a pre-enumeration candidate set (list or count) that covers both firing and non-firing triggers. An output that only lists what fired, with no reference to what was considered and ruled out, fails. |
| C-12 | **Gap tokens for non-firing candidates** — When a candidate trigger is evaluated and does not fire for the given input, the output inserts an explicit gap token (e.g., `[NOT FIRED — {reason}]`) in the numbered sequence at the position where that trigger would have appeared. Silent omission of non-firing candidates is a structural gap; named disposal is a structural pass. | coverage | At least one non-firing candidate (where present in the scenario) is disposed of with an explicit inline token and a stated reason. An output that identifies candidates in a preamble but then silently drops them from the numbered sequence fails. If all candidates fire, criterion passes vacuously. |
| C-13 | **Anomaly verdict evidence citation** — Each anomaly verdict (storm, missing trigger, circular) cites the specific numbered trigger rows that support the finding. A clean verdict ("Storm: not detected") must cite the row range inspected. A positive finding must name the rows involved in the anomaly. Verdicts that assert without row-level citation are weak passes at best. | depth | Every anomaly verdict — clean or positive — references at least one numbered row or row range from the trigger enumeration section. A verdict section with no row citations fails. |

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
| C-11 | aspirational | | |
| C-12 | aspirational | | |
| C-13 | aspirational | | |

**Score calculation**:
- Essential: `___ / 5` × 60 = ___
- Recommended: `___ / 3` × 30 = ___
- Aspirational: `___ / 5` × 10 = ___
- **Composite: ___**
- Golden threshold met? (all essential pass AND composite ≥ 80): **YES / NO**
```

---

**What changed from v1:**

| New criterion | Source signal | Distinguished from existing |
|---|---|---|
| C-11 Candidate denominator | All four variations pre-scan candidates; V-01/V-04 explicitly built a denominator before enumeration | C-01 checks fired triggers aren't omitted — C-11 checks that the scope of consideration is made explicit |
| C-12 Gap tokens | V-01 `[FLAGGED GAP]`, V-04 `[NOT IN PASS 2 CHAIN]` — non-firing candidates disposed of inline, not silently dropped | C-01 covers silent omission of fired triggers — C-12 covers silent omission of evaluated-but-not-fired candidates |
| C-13 Anomaly verdict evidence citation | V-02 "verdicts must cite specific rows from Sections 2–3"; V-04 note flagged bare verdicts as insufficient | C-04 checks verdicts exist — C-13 checks that verdicts are evidence-bound to numbered rows |

The C-08 `PARTIAL` pattern (remediation described but not mandated per-anomaly) remains in recommended rather than aspirational — it was structural weakness in the *prompts*, not an excellence signal in the *outputs*. A future round may surface it as a promotion candidate if outputs consistently pass C-08 only weakly.
