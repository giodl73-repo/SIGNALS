## flow-trigger — Round 1 Scorecard

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 | 4/4 | 3/3 | 2/2 | **100** | GOLD |
| V-01 | 4/4 | 3/3 | 1/2 | **95** | GOLD |
| V-02 | 4/4 | 3/3 | 1/2 | **95** | GOLD |
| V-03 | 4/4 | 3/3 | 1/2 | **95** | GOLD |
| V-04 | 4/4 | 1/3 | 1/2 | **75** | SILVER |

---

**V-05 is the only variation that passes C-09** (trigger storm quantification). All other variations rely on the model volunteering API budget analysis — V-05 pre-prints a `STORM BUDGET` template with `storm_depth`, `api_requests`, `platform_limit`, `budget_consumed`, and `run_duration` as required fields.

**V-04 is the only SILVER.** It passes all 4 essential criteria and writes the sharpest remediation instructions of any variation — but the conversational format distributes C-05 (side effects) and C-06 (condition evaluation) as walkthrough questions rather than enforcing them per-trigger via columns. PARTIAL on both, which collapses the recommended score.

**V-01, V-02, V-03 are all tied at 95.** The differentiating factor within the tier: V-03 has the strongest C-07 enforcement (explicit "do not proceed" gate + confirmation line), V-01 has the most scannable table format, V-02's two-pass separation best guards against enumeration shortcutting. None exposes a structural gap in any essential criterion.

**Excellence signals from V-05:**
1. **Proactive budget trigger** — budget section fires when `M >= 3 AND any side effect exists`, not only on confirmed storm. Converts C-09 from reactive to proactive.
2. **Dual-population table** — single table with `Fires? YES/NO` column covers both registered and firing triggers, preventing the registry/firing split that models could inconsistently resolve.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["proactive-budget-trigger", "dual-population-table"]}
```
duce a well-formed row without filling both |
| C-04 | PASS | PATHOLOGY SCAN section requires PRESENT or ABSENT for all three types; "If a pathology is absent, explicitly confirm it with evidence" |
| C-05 | PASS | Dedicated Side Effects column; "Do not leave any column blank" — downstream effects structurally required per row |
| C-06 | PASS | Gate Condition column in table cannot be blank; column description asks for "filter condition or scope that determines whether it fires" |
| C-07 | PASS | SCENARIO section asks for Triggering change and Environment (table, solution layer) before enumeration begins |
| C-08 | PASS | STEP 3: REMEDIATION with "Fix: [Concrete remediation using a specific Power Automate or Copilot Studio construct]" and "Platform reference" required for each pathology found |
| C-09 | FAIL | No storm budget or cascade quantification section; no API request estimate required; storm depth is not pre-printed as a required field |

**Essential**: 4/4 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 1/2 → 5
**Composite**: **95** — GOLD

---

### V-02 — Role Sequence (Single Axis)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | Pass 1 summary checkpoint "Catalog contains [N] registered triggers, [M] fire for this change" creates accountability; enumeration is a dedicated pass with no pathology distraction |
| C-02 | PASS | "Number the triggers in firing sequence. Sync triggers first (ordered by plug-in execution pipeline stage if relevant), then async" — explicit per-trigger ordering requirement |
| C-03 | PASS | Pass 1 asks Inputs and Outputs per trigger in structured bulleted format; each firing trigger requires both fields |
| C-04 | PASS | Pass 2 has three named and separated pathology sections (Storm, Missing, Circular); each requires STORM DETECTED/NO STORM, MISSING TRIGGERS FOUND/CATALOG COMPLETE, CIRCULAR TRIGGER FOUND/NO CIRCULAR TRIGGER |
| C-05 | PASS | Pass 1 explicitly asks "Side effects: does any output write a field or record that could itself trigger another automation?" per firing trigger |
| C-06 | PASS | Pass 1 asks "Gate condition: the filter, scope, or condition that determines whether it fires for this specific change" per trigger, with YES/NO firing determination |
| C-07 | PASS | Pass 1 Step 1 "State the scenario boundary" with four required bullet fields: Table, Change type, Field changed, Environment/solution |
| C-08 | PASS | Pass 2 Remediation section requires Pathology, Affected triggers, Remediation (specific construct), and Implementation note (where to apply) |
| C-09 | FAIL | Storm Analysis asks to "Estimate execution budget impact (number of Power Platform API requests consumed, or approximate run duration if determinable)" — the "if determinable" hedge allows model to omit the estimate; no pre-printed budget template |

**Essential**: 4/4 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 1/2 → 5
**Composite**: **95** — GOLD

---

### V-03 — Lifecycle Emphasis (Single Axis)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | Section 2 explicitly instructs "List every automation registered against this table, regardless of whether it fires for the declared scenario" with YES/NO for each; registry summary required |
| C-02 | PASS | Section 3 blocks numbered in execution order with "[SYNC | ASYNC]" label required; within-sync ordering by plug-in pipeline stage provided |
| C-03 | PASS | Each Section 3 block requires Inputs and Outputs as named fields; format is explicit per trigger |
| C-04 | PASS | Section 4 addresses all three types with required [DETECTED | ABSENT] / [FOUND | CATALOG COMPLETE] verdicts; "ABSENT is a valid answer only if accompanied by evidence" — cannot skip with an unsupported ABSENT |
| C-05 | PASS | Section 3 block includes "Side effects" field with "or 'None'" — absence must be declared, not omitted |
| C-06 | PASS | Section 2 requires gate condition for every NO trigger; Section 3 requires "Gate condition" block for every firing trigger — double coverage |
| C-07 | PASS | Section 1 SCENARIO DECLARATION is fully gated: "Do not begin trigger enumeration until the SCENARIO DECLARATION section is complete" + explicit scenario confirmation line required before proceeding — strongest C-07 enforcement of any single-axis variation |
| C-08 | PASS | Section 5 REMEDIATION with "Recommended fix" (specific construct) and "Where to apply" (exact location in platform) required per pathology found |
| C-09 | FAIL | Section 4 storm analysis has no budget quantification requirement; cascade depth and API request estimate are not requested |

**Essential**: 4/4 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 1/2 → 5
**Composite**: **95** — GOLD

---

### V-04 — Conversational Debug Mode (Single Axis)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | "Once you've worked through everything that fires, go back and note anything that was registered but didn't fire -- and why it got skipped" — fires and non-fires both required |
| C-02 | PASS | "Number each item. Keep them in the order they actually execute" + "Does it run before the database commits, or after? (Sync or async)" per item |
| C-03 | PASS | "What did it read from the record? What did it write, send, or create?" — concrete I/O question asked per trigger in the walkthrough |
| C-04 | PASS | "Now look for trouble" section covers all three types: 1. Too many fires (storm), 2. Missing automations, 3. Loops — each numbered, each requires a verdict |
| C-05 | PARTIAL | "Did anything it wrote or created set off something else?" — side effects asked in the walkthrough flow, but embedded conversationally rather than enforced per trigger; a model summarizing "interesting" triggers could omit side effect analysis for lower-signal triggers |
| C-06 | PARTIAL | "What condition did it check before firing? Did it pass? Why?" — condition evaluation is a conversational question in the walkthrough; less structurally enforced than a dedicated column; models may compress gate logic for simpler triggers |
| C-07 | PASS | Opening "set the scene" section asks for table, field, old/new values, environment; explicit instruction to state assumptions before proceeding |
| C-08 | PASS | "For each issue you flagged above, give me one concrete fix. Not 'add a condition' -- tell me which condition, on which flow or plug-in, checking which field or context value. Name the exact Power Automate node or Dataverse registration setting" — strongest remediation specificity instruction of any variation |
| C-09 | FAIL | "If the chain is longer than 3 steps, name every step and count them" — captures cascade depth but does not ask for API budget impact, platform limit reference, or execution duration estimate |

**Essential**: 4/4 → 60
**Recommended**: 1/3 → 10 (C-05 PARTIAL = FAIL, C-06 PARTIAL = FAIL, C-07 PASS)
**Aspirational**: 1/2 → 5
**Composite**: **75** — SILVER

Note: V-04 passes all essential criteria and produces the most concrete remediation instructions (C-08) of any variation. The silver rating is driven entirely by the conversational format's weaker per-trigger enforcement of C-05 and C-06.

---

### V-05 — Combined: Role Sequence + Table + Storm Quantification

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | Full table has YES/NO "Fires?" column covering both registered and firing triggers; Pass 1 summary "[N] triggers registered, [M] fire for this change" creates accountability; both populations must appear in the same table |
| C-02 | PASS | Row # = execution order; "Sync rows appear before Async rows. Renumber if needed" — ordering is a structural property of the numbered table, not just an instruction |
| C-03 | PASS | Dedicated Inputs and Outputs columns; "Fill every cell. 'None' and 'N/A' are valid -- blank is not" — structural enforcement of completeness |
| C-04 | PASS | Pass 2 has three named sections (Storm, Missing, Circular) each requiring a binary assessment verdict (STORM DETECTED/NO STORM; MISSING TRIGGERS FOUND/CATALOG COMPLETE; CIRCULAR TRIGGER FOUND/NO CIRCULAR TRIGGER) |
| C-05 | PASS | Dedicated Side Effects column in table; "blank is not" valid — absence must be declared as "None" |
| C-06 | PASS | Gate Condition column in table with "why it fires or skips" description; blank is not valid |
| C-07 | PASS | Pass 1 Step 1 scenario declaration block with all required fields; "Fill every cell...blank is not" applies to the declaration block as well |
| C-08 | PASS | Each pathology section in Pass 2 includes an inline Remediation field with "Specific fix" examples naming exact Power Automate nodes and Dataverse constructs |
| C-09 | PASS | Section 2d STORM BUDGET with pre-printed template: storm depth, API requests (computed), platform limit (with license tier), budget consumed (as % of daily limit), run duration, risk level — proactive completion trigger: "complete if storm detected OR if [M] >= 3 and any trigger has a side effect that writes a field" |

**Essential**: 4/4 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 2/2 → 10
**Composite**: **100** — GOLD

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 | 4/4 | 3/3 | 2/2 | **100** | GOLD |
| V-01 | 4/4 | 3/3 | 1/2 | **95** | GOLD |
| V-02 | 4/4 | 3/3 | 1/2 | **95** | GOLD |
| V-03 | 4/4 | 3/3 | 1/2 | **95** | GOLD |
| V-04 | 4/4 | 1/3 | 1/2 | **75** | SILVER |

---

## Variation Ranking

1. **V-05** (100) — Only variation with a structural guarantee for C-09; dual-population table covers all recommended criteria by column enforcement; proactive storm budget trigger fires before a storm is confirmed.
2. **V-03** (95) — Strongest C-07 enforcement (explicit gating with confirmation line); double-coverage of C-06 (Section 2 + Section 3 blocks). Tied composite with V-01 and V-02.
3. **V-01** (95) — Most visually scannable format; table column enforcement is the strongest structural guarantee for C-03/C-05/C-06. Weaker C-07 enforcement (no gate line) compared to V-03.
4. **V-02** (95) — Two-pass role separation is the best guard against enumeration shortcutting, but the "if determinable" hedge in C-09 prevents it from closing the aspirational gap.
5. **V-04** (75) — Produces the most grounded remediation instructions (C-08) due to debug-session framing; fails recommended threshold due to conversational underenforcement of C-05 and C-06 per-trigger.

---

## Excellence Signals from V-05

1. **Proactive budget trigger**: the STORM BUDGET section completes when `M >= 3 AND any trigger has a side effect`, not only when a storm is confirmed. This converts C-09 from a reactive check into a proactive risk surface — a model running V-05 must quantify storm risk even for borderline cases.

2. **Dual-population table**: a single table with a `Fires? YES/NO` column captures both the full registry (for C-01 completeness) and the firing subset (for C-02 ordering, C-03 I/O, C-05 side effects, C-06 conditions) in one structure. No second pass needed to recover non-firing triggers; no registry/firing split that models could inconsistently resolve.

3. **"Blank is not valid" as a completeness guarantee**: by explicitly naming `None` and `N/A` as the required absent-value tokens, V-05 forces the model to commit to a value rather than omitting a cell. This is a subtle but reliable enforcement pattern — the model cannot accidentally satisfy the table format while skipping criteria.

4. **Inline remediation per pathology section**: V-05 places the remediation block immediately inside each pathology section (not deferred to a separate Step 3), so a model that stops after Section 2b cannot produce a pathology-without-fix output. The structure makes remediation omission a structural error.

---

## Round 1 Findings

**C-09 is the only criterion that separates V-05 from V-01/V-02/V-03.** All four gold variations pass all 4 essential and all 3 recommended criteria. The entire tier-1 differentiation comes from whether the prompt pre-prints a storm budget template (V-05 does; V-01/V-02/V-03 do not).

**V-04's failure mode is register, not structure.** V-04 passes all essential criteria and produces the sharpest remediation language of any variation. Its recommended-tier deficit is caused by the conversational format distributing per-trigger requirements across prose questions rather than enforcing them through table columns. The finding: conversational register trades structural completeness for specificity depth.

**Golden output for R1**: V-05 is confirmed as the R1 golden prompt. No R1 variation exposes a structural gap in the essential criteria.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["proactive-budget-trigger", "dual-population-table"]}
```
