Written to `simulations/quest/variations/discover-feasibility-alt-variations-R3-2026-03-17.md`.

---

## Round 3 Variations — `discover-feasibility-alt`

**Gap analysis:** R2 V-05 scored 100/100 on v2 rubric. Against v3's three new criteria:

| Criterion | R2 V-05 | Verdict |
|-----------|---------|---------|
| C-14 (4-step AMEND + named unaffected list) | Steps A-D + "Unaffected: [list]" declaration | Likely PASS — rubric confirms V-05 R2 as the source of this pattern |
| C-15 (arithmetic economics formula) | `base + adjustment (unit rate) = total` | **PASS** — rubric note line 89 explicitly confirms V-03/V-05 R2 = C-15 PASS |
| C-16 (3-column routing table) | 2-column table: `Downstream section \| Effect` | **FAIL** — rubric note line 90: "V-05 R2 prose Step 0 = C-11 PASS, C-16 FAIL" |

Estimated R2 V-05 under v3: 60 + 30 + 8.75 = **98.75** -- still Golden, missing only C-16.

**Single gap: C-16.** The fix is adding an explicit `Constraint` first column to Item C's routing table.

| Variation | Axis | Target | Key mechanism |
|-----------|------|--------|---------------|
| V-01 | C-16 minimal (constraint-per-row) | C-16 | Item C table: 3 columns, constraint phrase repeated on each of 4 section rows. Minimal diff from R2 V-05. |
| V-02 | C-16 table-first ordering | C-16 | Propagation Contract (3-column table) opens Step 0 BEFORE lens + economics. Tests whether writing the contract first makes delivery more reliable. |
| V-03 | C-16 explicit column semantics | C-16 | Column headers use rubric-aligned language: `Constraint introduced by focus \| Section where it surfaces \| Effect on that section`. "[same]" back-reference on rows 2-4. |
| V-04 | C-16 + C-14 named-unaffected precision | C-16, C-14 | 3-column table + AMEND PROTOCOL uses numbered (1)-(4) steps with "Affected sections: [names]. Unaffected sections: [names]. Unaffected sections will not be rewritten." |
| V-05 | Full battery: C-16 + C-14 + C-15 reinforced | C-16, C-14, C-15 | 3-column table + numbered AMEND steps + `focus_adjusted_total = base_cost + focus_adjustment` formula using exact rubric variable names across all downstream locations. |

**Run order**: V-01 first (diagnostic — is the minimal 3-column change sufficient?), V-03 second (alternative column-header form), V-05 last (ceiling test). If V-01 passes C-16, V-04/V-05 are hardening exercises, not gap fills.
xample. |
| **V-05** | Full battery: C-16 + C-14 + C-15 reinforced | C-16, C-14, C-15 | 3-column table + AMEND steps numbered (1)-(4) + C-15 formula uses exact rubric variable names (`base_cost + focus_adjustment = focus_adjusted_total`). Maximum precision on all three upgrade criteria. |

**Run order**: V-01 first (C-16 diagnostic -- does the minimal fix work?), V-03 second (alternative column-header form), V-05 last (full battery ceiling test).

---

## V-01 -- C-16 Minimal (Constraint-Per-Row 3-Column Table)

**Axis**: Output format -- 3-column propagation contract table with constraint repeated on each section row
**Hypothesis**: The only gap between R2 V-05 (100/100 on v2) and C-16 is that Item C's table has 2 columns instead of 3. Adding an explicit "Constraint" first column -- with the same constraint phrase repeated on each of the 4 section rows -- is the minimal change that makes C-16 structurally unambiguous. All other mechanics (economics calculator, AMEND PROTOCOL, failure-mode rejection) are carried over unchanged from R2 V-05.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than staying with the workaround?" Every section below answers that question.

**If a focus dimension is active**, it changes the economics of that competition. A compliance focus may reveal the workaround carries a regulatory liability that raises what "not building" costs per sprint. A stakeholders focus may reveal recurring escalation overhead. A size focus may reveal scaling degradation. The focus lens changes the competitive math -- it is not a section you add at the end. All focus content belongs inside the existing sections.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items:

**Item A -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item B -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use this number in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint -- what the workaround costs ignoring the focus lens]
  Focus adjustment: [Concrete focus-specific liability the workaround carries -- state as a unit rate:
    compliance focus: "audit exposure: +$X/sprint"; stakeholders focus: "sign-off overhead: +N hrs/sprint";
    size focus: "scaling degradation: +N hrs/sprint at current growth rate"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item C -- Propagation Contract:**
Map the primary constraint this focus introduces to every downstream section. Complete this table before writing any section heading.

| Constraint | Downstream Section | Stated Effect |
|------------|--------------------|---------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement"] | INERTIA | [How the focus-adjusted cost appears in the risk column or Baseline sentence] |
| [same constraint phrase as row 1] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW, referencing focus-adjusted economics] |
| [same constraint phrase as row 1] | VERDICT | [Prerequisite and/or score impact; confirm focus-adjusted cost appears in "Not building this means:"] |
| [same constraint phrase as row 1] | AMENDMENTS | [Focus-specific inertia savings: base recapture + focus adjustment eliminated = stated total] |

Every section below must deliver on the Stated Effect in its row.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item C's table, using the economics computed in Item B.

---

**INFERENCE GATE**
  Feature:   [One sentence.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

---

**INERTIA: STATUS QUO -- The Workaround the Team Already Has**
Fill this before PM: BUDGET. This is the competitor you are trying to beat.

[If focus active: use the focus-adjusted do-nothing cost from Step 0 Item B. Deliver on the INERTIA row of your Propagation Contract.]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [Focus-adjusted cost from Step 0 Item B if active; base cost if no focus] | [Risk -- include focus-specific liability from Propagation Contract if active] |

Baseline: "Without this feature, the team spends approximately [focus-adjusted or base N hrs/sprint or $N/sprint] on [workaround]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the workaround?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus-adjusted cost from Step 0 Item B where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. The focus-adjusted economics from Item B may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable, not only because of technical complexity. Apply focus-adjusted economics here. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus-adjusted cost from Step 0 Item B where it changes the rating] | [Focus-adjusted cost from Step 0 if active] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [Focus-adjusted cost from Step 0 Item B.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
If focus changes procurement logic, state it in the Rationale column.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact if it changes the recommendation] |

Cover at least half the components from ARCHITECT.

---

**VERDICT -- Does building beat staying on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The workaround wins on focus-adjusted economics. State the focus-adjusted do-nothing cost from Step 0 Item B and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. State base recapture and focus-specific savings separately so the total is transparent.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Base recapture: N hrs/sprint or $N/sprint. Focus savings: focus adjustment eliminated = N hrs/sprint or $N/sprint. Total: [base + focus] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis.

Step A -- Parse the change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus / threshold]
  To: [new focus / threshold]

Step B -- Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify affected sections. Note if focus economics change (new base cost or new focus adjustment).
  For a threshold adjustment: identify which components change color. Affected = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for changed components.
  Declare: "Affected: [list]. Unaffected: [list]. Unaffected sections will not be rewritten."

Step C -- Re-weave affected sections only:
  Rewrite each affected section with the amendment applied. Use original section headings.
  For a focus shift: update Step 0 Items A-D first, then propagate the new contract through affected sections.
  Mark each rewritten section: "[AMENDED: reason]"

Step D -- Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus-adjusted do-nothing cost if Step 0 Item B changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-02 -- C-16 Table-First Ordering

**Axis**: Role sequence -- 3-column routing table opens Step 0 BEFORE economics (Items reordered: Contract first, then Lens, then Economics, then Rejection)
**Hypothesis**: R2 V-05's Item C table comes third (after lens + economics), which means the model has already written 2 prose blocks before it reaches the structural contract. If the routing table is the FIRST thing written in Step 0 -- before the model forms any opinion about the analysis -- the constraint-to-section mapping is more likely to survive intact as a structural commitment rather than a trailing summary. This tests whether ordering affects C-16 reliability independently of table column count.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than staying with the workaround?" Every section below answers that question.

**If a focus dimension is active**, it changes the economics of that competition -- not via a bonus block appended after AMENDMENTS. The focus lens surfaces a constraint that propagates through the report: it changes ratings, adds prerequisites, and raises the inertia savings when addressed.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop and move the content into the section listed in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given:

**Item A -- Propagation Contract (write this first, before lens definition or economics):**
Name the primary constraint this focus introduces. Complete the full table before writing anything else in Step 0.

| Constraint | Downstream Section | Stated Effect |
|------------|--------------------|---------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "SOC 2 Type II gap", "VP sponsor not yet assigned", "identifier namespace collision at 300+ existing names"] | INERTIA | [How this constraint changes the workaround's ongoing cost or risk] |
| [same constraint phrase] | ARCHITECT | [Which component(s) it rates or re-rates, and to what color] |
| [same constraint phrase] | VERDICT | [Prerequisite added and/or score band impact] |
| [same constraint phrase] | AMENDMENTS | [Focus-specific inertia savings unlocked when this constraint is cleared] |

This table is your delivery contract. Every section below must fulfill the Stated Effect in its row.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. This number flows into every Do-nothing cost cell and VERDICT's "Not building this means:" line. It is what makes the competitive calculation provably different from a no-focus run.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint -- workaround cost ignoring the focus lens]
  Focus adjustment: [Focus-specific liability the workaround carries, as a unit rate:
    compliance focus: "audit exposure: +$X/sprint"; stakeholders focus: "sign-off overhead: +N hrs/sprint";
    size focus: "scaling degradation: +N hrs/sprint at current growth rate"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C.

---

**INFERENCE GATE**
  Feature:   [One sentence.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

---

**INERTIA: STATUS QUO -- The Workaround the Team Already Has**
Fill this before PM: BUDGET. This is the competitor you are trying to beat.

[If focus active: use the focus-adjusted do-nothing cost from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A).]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [Focus-adjusted cost from Step 0 Item C if active; base cost if no focus] | [Risk -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team spends approximately [focus-adjusted or base N hrs/sprint or $N/sprint] on [workaround]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the workaround?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus-adjusted cost from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). Apply focus-adjusted economics from Item C to the specific component(s) named there. Do not save focus content for a standalone section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference Propagation Contract row if focus changes this component's rating] | [Focus-adjusted cost from Step 0 Item C if active] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [Focus-adjusted cost from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
If focus changes procurement logic (e.g., compliance focus favors certified third-party over in-house), state it in Rationale.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact if it changes the recommendation] |

Cover at least half the components from ARCHITECT.

---

**VERDICT -- Does building beat staying on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The workaround wins on focus-adjusted economics. State the focus-adjusted do-nothing cost from Step 0 Item C and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). State base recapture and focus-specific savings separately so the total is transparent.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Base recapture: N hrs/sprint or $N/sprint. Focus savings: focus adjustment eliminated = N hrs/sprint or $N/sprint. Total: [base + focus] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis.

Step A -- Parse the change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus / threshold]
  To: [new focus / threshold]

Step B -- Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A) identify affected sections. Note if focus economics change (new base cost or new focus adjustment in Item C).
  For a threshold adjustment: identify which components change color. Affected = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for changed components.
  Declare: "Affected: [list]. Unaffected: [list]. Unaffected sections will not be rewritten."

Step C -- Re-weave affected sections only:
  Rewrite each affected section with the amendment applied. Use original section headings.
  For a focus shift: update Step 0 Items A-D first, then propagate the new contract through affected sections.
  Mark each rewritten section: "[AMENDED: reason]"

Step D -- Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus-adjusted do-nothing cost if Step 0 Item C changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-03 -- C-16 Explicit Column Semantics

**Axis**: Output format -- column headers use rubric-exact language; constraint column appears once as a labeled cell that anchors the section column
**Hypothesis**: R2 V-04's 2-column table (labeled "Downstream section | What this constraint produces here") passed C-16 in the rubric author's retroactive assessment because the constraint phrase above the table acts as an implicit first column. V-01 makes this explicit by repeating the constraint phrase in every row. V-03 tests a middle path: the table has 3 columns with rubric-exact header names ("Constraint introduced by focus | Section where it surfaces | Effect on that section"), and the constraint cell on the first row names the phrase while subsequent rows use "[same]" as a back-reference. This is the most readable 3-column form.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than staying with the workaround?" Every section below answers that question.

**If a focus dimension is active**, it changes the economics of that competition. A compliance focus may reveal the workaround carries a regulatory liability. A stakeholders focus may surface recurring escalation overhead. A size focus may reveal compounding degradation. The focus lens changes the competitive math -- it is not a section you add at the end.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. All focus content flows into existing sections through the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items:

**Item A -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item B -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint]
  Focus adjustment: [Unit rate for this focus type:
    compliance: "audit exposure: +$X/sprint"; stakeholders: "approval overhead: +N hrs/sprint";
    size: "scaling degradation: +N hrs/sprint at current growth"; requirements: "+N hrs/sprint per coverage gap"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item C -- Propagation Contract:**
Before writing any section heading, complete this table. The "Constraint introduced by focus" column names the single constraint that propagates through the report. The "Effect on that section" column commits to what the constraint produces in each section.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary constraint this focus introduces, e.g., "GDPR data residency gap", "executive sponsor unassigned", "query time budget exceeded at P99 under 3x load"] | INERTIA | [How the focus-adjusted do-nothing cost from Item B appears here -- risk column or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) rate RED or YELLOW because of this constraint and focus-adjusted economics] |
| [same] | VERDICT | [Whether this constraint adds a prerequisite or shifts the score band] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base recapture + focus adjustment eliminated = stated total] |

Every section below delivers on the "Effect on that section" cell in its row. No new section is created for focus content.

**Item D -- Failure-mode rejection:**
No heading matching the focus name (e.g., "## COMPLIANCE", "## STAKEHOLDERS") appears after AMENDMENTS. The constraint in Item C's table surfaces inside the sections -- it does not appear as a block after them.

---

**INFERENCE GATE**
  Feature:   [One sentence.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

---

**INERTIA: STATUS QUO -- The Workaround the Team Already Has**
Fill this before PM: BUDGET. This is the competitor you are trying to beat.

[If focus active: use the focus-adjusted do-nothing cost from Step 0 Item B. Deliver on the INERTIA row of your Propagation Contract.]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [Focus-adjusted cost from Step 0 Item B if active; base cost if no focus] | [Risk -- include focus-specific liability from Propagation Contract if active] |

Baseline: "Without this feature, the team spends approximately [focus-adjusted or base N hrs/sprint or $N/sprint] on [workaround]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the workaround?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus-adjusted cost from Step 0 Item B where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. The focus-adjusted economics from Item B may rate a component YELLOW or RED not only because of technical complexity but because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference Propagation Contract constraint effect if applicable] | [Focus-adjusted cost from Step 0 Item B if active] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [Focus-adjusted cost from Step 0 Item B.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
If focus changes procurement logic, state it in Rationale.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact if it changes the recommendation] |

Cover at least half the components from ARCHITECT.

---

**VERDICT -- Does building beat staying on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The workaround wins on focus-adjusted economics. State the focus-adjusted do-nothing cost from Step 0 Item B and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. State base recapture and focus-specific savings separately.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Base recapture: N hrs/sprint or $N/sprint. Focus savings: focus adjustment eliminated = N hrs/sprint or $N/sprint. Total: [base + focus] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis.

Step A -- Parse the change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus / threshold]
  To: [new focus / threshold]

Step B -- Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify affected sections. Note if focus economics change.
  For a threshold adjustment: identify which components change color. Affected = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for changed components.
  Declare: "Affected: [list]. Unaffected: [list]. Unaffected sections will not be rewritten."

Step C -- Re-weave affected sections only:
  Rewrite each affected section with the amendment applied. Use original section headings.
  For a focus shift: update Step 0 Items A-D first, then propagate the new contract.
  Mark each rewritten section: "[AMENDED: reason]"

Step D -- Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus-adjusted do-nothing cost if Step 0 Item B changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- C-16 + C-14 Named-Unaffected Precision

**Axis**: Output format (3-column table) + Lifecycle emphasis (AMEND PROTOCOL numbered steps 1-4 with named canonical unaffected set)
**Hypothesis**: R2 V-05's AMEND PROTOCOL uses "Step A / Step B / Step C / Step D" labeling and "Unaffected: [list]" declaration. C-14's rubric example says "Unaffected sections: INFERENCE GATE, ARCHITECT, STRATEGY. These will not be rewritten." -- a named canonical format. While R2 V-05 likely passes C-14 already, V-04 eliminates ambiguity by: (a) numbering steps (1)-(4) to match the rubric's "(1) parse / (2) identify-affected / (3) re-weave-only / (4) update-VERDICT" language, (b) using "Unaffected sections:" (plural, with colon) as the exact declaration keyword, and (c) prompting the model to name specific section titles rather than "[list]". Combined with the C-16 3-column table from V-01.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than staying with the workaround?" Every section below answers that question.

**If a focus dimension is active**, it changes the economics of that competition. A compliance focus may reveal the workaround carries a regulatory liability that raises what "not building" costs per sprint. A stakeholders focus may reveal recurring escalation overhead. A size focus may reveal compounding degradation. The focus lens changes the competitive math -- it is not a section you add at the end. All focus content belongs inside the existing sections.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items:

**Item A -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item B -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use this number in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint -- workaround cost ignoring focus lens]
  Focus adjustment: [Concrete focus-specific liability the workaround carries, stated as a unit rate:
    compliance focus: "audit exposure: +$X/sprint"; stakeholders focus: "sign-off overhead: +N hrs/sprint";
    size focus: "scaling degradation: +N hrs/sprint at current growth rate"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item C -- Propagation Contract:**
Map the primary constraint this focus introduces to every downstream section. Complete this table before writing any section heading.

| Constraint | Downstream Section | Stated Effect |
|------------|--------------------|---------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement"] | INERTIA | [How the focus-adjusted cost appears in the risk column or Baseline sentence] |
| [same constraint phrase as row 1] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW, referencing focus-adjusted economics] |
| [same constraint phrase as row 1] | VERDICT | [Prerequisite and/or score impact; confirm focus-adjusted cost appears in "Not building this means:"] |
| [same constraint phrase as row 1] | AMENDMENTS | [Focus-specific inertia savings: base recapture + focus adjustment eliminated = stated total] |

Every section below must deliver on the Stated Effect in its row.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item C's table, using the economics computed in Item B.

---

**INFERENCE GATE**
  Feature:   [One sentence.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

---

**INERTIA: STATUS QUO -- The Workaround the Team Already Has**
Fill this before PM: BUDGET. This is the competitor you are trying to beat.

[If focus active: use the focus-adjusted do-nothing cost from Step 0 Item B. Deliver on the INERTIA row of your Propagation Contract.]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [Focus-adjusted cost from Step 0 Item B if active; base cost if no focus] | [Risk -- include focus-specific liability from Propagation Contract if active] |

Baseline: "Without this feature, the team spends approximately [focus-adjusted or base N hrs/sprint or $N/sprint] on [workaround]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the workaround?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus-adjusted cost from Step 0 Item B where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. Focus-adjusted economics from Item B may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus-adjusted cost from Step 0 Item B where it changes the rating] | [Focus-adjusted cost from Step 0 if active] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [Focus-adjusted cost from Step 0 Item B.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
If focus changes procurement logic, state it in the Rationale column.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact if it changes the recommendation] |

Cover at least half the components from ARCHITECT.

---

**VERDICT -- Does building beat staying on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The workaround wins on focus-adjusted economics. State the focus-adjusted do-nothing cost from Step 0 Item B and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. State base recapture and focus-specific savings separately so the total is transparent.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Base recapture: N hrs/sprint or $N/sprint. Focus savings: focus adjustment eliminated = N hrs/sprint or $N/sprint. Total: [base + focus] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus or threshold value]
  To: [new focus or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item C) identify which sections are affected. Note if focus economics change (new base cost or new focus adjustment in Item B).
  For a threshold adjustment: identify which components change color. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for those components only.
  Then declare:
    "Affected sections: [list each affected section by name, e.g., INERTIA, ARCHITECT, VERDICT, AMENDMENTS].
     Unaffected sections: [list each unaffected section by name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use original section headings.
  For a focus shift: update Step 0 Items A-D first, then propagate the new contract through each affected section in turn.
  Mark each rewritten section with: "[AMENDED: reason]"
  Do not rewrite sections not listed as affected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus-adjusted do-nothing cost if Step 0 Item B changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-05 -- Full Battery: C-16 + C-14 + C-15 Reinforced

**Axes**: Output format (3-column table, C-16) + Lifecycle emphasis (numbered 1-4 AMEND steps with named unaffected set, C-14) + Inertia framing (labeled variable names in arithmetic formula, C-15)
**Hypothesis**: All three v3 upgrade criteria have separate precision levers. C-16 = 3-column table with repeated constraint column. C-14 = AMEND PROTOCOL numbered (1)-(4) with "Unaffected sections: [named list]" declaration. C-15 = arithmetic formula uses exact rubric variable names (`base_cost + focus_adjustment = focus_adjusted_total`) with the formula stated inline as a labeled equation. This is the maximum-coverage variation. If it scores 100/100, the R3 ceiling is confirmed and V-01 (minimal) vs V-05 (reinforced) comparison reveals which precision level is necessary.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than staying with the workaround?" Every section below answers that question.

**If a focus dimension is active**, it changes the economics of that competition. A compliance focus may reveal the workaround carries a regulatory liability that raises what "not building" costs per sprint. A stakeholders focus may reveal recurring escalation overhead. A size focus may reveal compounding degradation. The focus lens changes the competitive math -- it is not a section you add at the end. All focus content belongs inside the existing sections.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items:

**Item A -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item B -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use this number in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- workaround cost ignoring focus lens; source: inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the workaround carries:
    compliance focus: "audit exposure: +$X/sprint per open gap"; stakeholders focus: "sign-off overhead: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation: +N hrs/sprint per sprint at current growth rate"; requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item C -- Propagation Contract:**
Map the primary constraint this focus introduces to every downstream section. Complete this table before writing any section heading.

| Constraint | Downstream Section | Stated Effect |
|------------|--------------------|---------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How focus_adjusted_total from Item B appears in the risk column or Baseline sentence] |
| [same constraint phrase as row 1] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW, referencing focus_adjusted_total] |
| [same constraint phrase as row 1] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same constraint phrase as row 1] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = stated total] |

Every section below must deliver on the Stated Effect in its row.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item C's table, using the economics computed in Item B's formula.

---

**INFERENCE GATE**
  Feature:   [One sentence.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

---

**INERTIA: STATUS QUO -- The Workaround the Team Already Has**
Fill this before PM: BUDGET. This is the competitor you are trying to beat.

[If focus active: use focus_adjusted_total from Step 0 Item B. Deliver on the INERTIA row of your Propagation Contract.]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [focus_adjusted_total from Step 0 Item B if active; base_cost if no focus] | [Risk -- include focus-specific liability from Propagation Contract if active] |

Baseline: "Without this feature, the team spends approximately [focus_adjusted_total or base_cost per sprint] on [workaround]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the workaround?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item B where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. Focus_adjusted_total from Item B may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable, not only because of technical complexity. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus_adjusted_total from Step 0 Item B where it changes the rating] | [focus_adjusted_total from Step 0 if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item B.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
If focus changes procurement logic (e.g., compliance focus favors certified third-party over in-house), state it in Rationale.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact if it changes the recommendation] |

Cover at least half the components from ARCHITECT.

---

**VERDICT -- Does building beat staying on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The workaround wins on focus-adjusted economics. State focus_adjusted_total from Step 0 Item B and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured: N hrs/sprint or $N/sprint. focus_adjustment eliminated: N hrs/sprint or $N/sprint. Total inertia saved: base_cost + focus_adjustment = [stated total] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item C table) identify which sections are affected. Note whether focus_adjusted_total changes (new base_cost or new focus_adjustment in Item B formula).
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first (including the full Propagation Contract table and the updated Item B formula), then propagate the new contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus_adjusted_total if Step 0 Item B formula changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## Selection Notes

| Variation | Primary target | Best for | Risk |
|-----------|----------------|----------|------|
| V-01 | C-16 minimal | Diagnostic: does the minimal 3-column table change alone push C-16 to PASS? | No other changes from R2 V-05 -- cleanest signal for C-16 isolation |
| V-02 | C-16 table-first | Testing whether contract-before-economics ordering improves reliability | Items reordered (A=contract, B=lens, C=economics, D=rejection) -- per-section "deliver on Item A" pointers need updating throughout |
| V-03 | C-16 explicit headers | Testing whether rubric-aligned column names ("Constraint introduced by focus | Section where it surfaces | Effect on that section") raise C-16 PASS rate | Wordier column headers; "[same]" back-reference in rows 2-4 may reduce model compliance |
| V-04 | C-16 + C-14 | Reinforcing both C-16 and C-14 precisely; safe upgrade from V-01 | Minor verbosity increase in AMEND PROTOCOL; no new risk if V-01 passes C-16 |
| V-05 | C-16 + C-14 + C-15 | Maximum-precision ceiling test; all three upgrade criteria with exact rubric variable names | focus_adjusted_total used as a variable name throughout -- model must carry the label coherently across 6+ locations |
