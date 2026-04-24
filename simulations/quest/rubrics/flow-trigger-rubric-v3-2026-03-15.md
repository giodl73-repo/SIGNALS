Reading the scorecard carefully before writing.

The four Round 5 variations each introduced a structurally distinct mechanism not covered by C-01–C-13:

| Source | Mechanism | What makes it new |
|--------|-----------|-------------------|
| V-01 | Decomposition Gate — event tuple closes scope before candidates are named | C-11 declares a count; this closes the *eligibility boundary* making false-positive candidates impossible by construction |
| V-02 | Bilateral counterfactual per entry — every entry carries flip-to-NOT-FIRE (firing) and flip-to-FIRE (gap) | C-07 and C-12 are separate checks; this collapses them into a single per-entry structural obligation |
| V-03 | `[DEFERRED TO BLOCK 2]` placeholder — every C-ID gets a Block 1 disposition even if it fires | C-12 requires gap tokens for non-firers; this adds the *mirror obligation* for firers, completing the two-way accounting |
| V-04 | Per-entry Registration Witness + UNWITNESSED denominator | C-05 grounds the output at document level; this anchors every individual row to a concrete platform artifact |

That yields C-14, C-15, C-16. N_aspirational grows from 5 to 8.

---

```markdown
---
skill: quest-rubric
skill_target: flow-trigger
date: 2026-03-16
version: 3
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

N_essential = 5 | N_recommended = 3 | N_aspirational = 8

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
| C-14 | **Scope-closing event gate** — Before any candidate is named, the output declares a formal scope constraint — an event tuple specifying at minimum: entity type, operation (create/update/delete), and triggering field or event — that bounds which trigger candidates are eligible. This gate makes false-positive candidates structurally impossible by definition rather than caught by correctness review after the fact. A denominator (C-11) counts candidates; this gate defines what qualifies as a candidate. | coverage | A formal scope declaration (event entity, operation, field or event bounds) appears before candidate enumeration. The declaration must be specific enough that an evaluator can determine in-scope vs. out-of-scope for any given trigger without reading the full enumeration. A narrative preamble that does not constitute a named, structured gate fails. |
| C-15 | **Bilateral counterfactual per entry** — Every enumerated entry — firing and non-firing — carries a counterfactual that states the flip condition: firing entries declare what would cause the trigger to NOT fire; gap entries declare what would cause it to FIRE. This collapses C-07 (conditional branch paths) and C-12 (gap tokens) into a single unified per-entry obligation, eliminating the structural risk that one side of the pair is satisfied while the other is omitted. | depth | At least 80% of entries (firing and non-firing combined) carry an explicit counterfactual statement. An output where counterfactuals appear only in a summary section rather than inline per entry is a weak pass. An output where only one direction (flip-to-fire or flip-to-not-fire) is covered across the full enumeration fails. |
| C-16 | **Per-entry registration witness** — Each trigger entry — firing and non-firing — cites a concrete platform artifact that confirms the trigger's existence and registration: a configuration screen path, plugin step type, flow trigger event type, API endpoint, or registration ID. This elevates C-05 (platform grounding at document level) to a per-row structural requirement. Where the C-11 denominator is extended with an UNWITNESSED count (the number of candidates that could not be confirmed by a platform artifact), that count appears alongside the total. | correctness | At least 80% of trigger entries carry a `Registration witness` or equivalent field citing a concrete artifact. An output where trigger existence is asserted document-wide without any per-row artifact citation fails. If an UNWITNESSED count is declared, it must be numerically consistent with the entries that lack a witness citation. |
```
