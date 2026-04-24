Written to `simulations/quest/variations/discover-feasibility-alt-variations-R4-2026-03-17.md`.

---

## Round 4 Variations — `discover-feasibility-alt`

**Gap analysis (R3 → v4):**

| Criterion | R3 V-04/V-05 | Under v4 |
|-----------|--------------|----------|
| C-17 (table-first) | Table is Item C — after lens and economics | FAIL |
| C-18 (rubric-aligned headers + `[same]`) | `Constraint \| Downstream Section \| Stated Effect` with verbatim repeat | FAIL |

Estimated R3 V-04/V-05 under v4: **98.0** — Golden but missing 2.0 pts.

**Item letter remapping** for table-first variations (V-01, V-03, V-04, V-05): Old A→B, Old B→C, Old C→A, D unchanged. All "Item B" economics pointers become "Item C"; "Propagation Contract (Item C)" becomes "(Item A)".

---

**Variation map:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| Table-first (C-17) | YES | no | YES | YES | YES |
| Rubric-aligned headers + `[same]` (C-18) | no | YES | YES | YES | YES |
| Numbered (1)-(4) AMEND (C-14 PASS) | YES | YES | no | YES | YES |
| Exact variable names `focus_adjusted_total` (C-15) | prose | prose | prose | prose | YES |
| Expected score under v4 | 99.0 | 99.0 | ~98.5 | **100.0** | **100.0** |

**Run order**: V-01 and V-02 first (single-axis diagnostics); V-03 second (C-14 load-bearing test); V-04/V-05 last (ceiling confirmation). V-05 adds one distinguishing feature over V-04: `focus_adjusted_total` referenced inside the Stated Effect cells of the table itself, closing the contract-to-formula loop at the token level.
d Item B (Economics) → Item C
- Old Item C (Contract/table) → Item A
- Item D (Rejection) unchanged
- All "Item B" economics references in body → "Item C"; "Propagation Contract (Item C)" → "(Item A)"

| Variation | Axis | Targets | Key mechanism |
|-----------|------|---------|---------------|
| V-01 | Ordering only (C-17) — V-04-R3 base | C-17 | Table moves to Item A (first). Lens → Item B, Economics → Item C. Generic headers. C-14 numbered (1)-(4) preserved. |
| V-02 | Column semantics only (C-18) — V-04-R3 base | C-18 | Table stays at Item C (third position). Rubric-aligned headers + `[same]` on rows 2-4. C-14 numbered (1)-(4) preserved. |
| V-03 | C-17 + C-18 on minimal base | C-17, C-18 | Table-first + rubric-aligned headers on V-01-R3 base (Step A-B-C-D AMEND, C-14 PARTIAL). Diagnoses whether C-14 precision is load-bearing for achieving 100 under v4. |
| V-04 | C-17 + C-18 combined — V-04-R3 base | C-17, C-18, ceiling | Table-first + rubric-aligned headers + `[same]` on V-04-R3 base (C-14 numbered 1-4, C-15 formula). Expected 100.000. |
| V-05 | Full battery: C-17 + C-18 — V-05-R3 base | C-17, C-18, ceiling | Table-first + rubric-aligned headers + `[same]` + exact variable names in Stated Effect cells + C-14 + exact C-15 formula. Maximum precision ceiling test. |

**Run order**: V-01 and V-02 first (single-axis diagnostics — do C-17 and C-18 each pass independently on the V-04 base?), V-03 second (does C-14 precision matter for reaching 100?), V-04/V-05 last (ceiling confirmation).

---

## V-01 -- C-17 Ordering Only (Table-First, Generic Headers, V-04-R3 Base)

**Axis**: Role sequence -- propagation contract table opens Step 0 BEFORE lens definition and focus economics
**Hypothesis**: R3 V-04 scored 100.000 under v3 but fails C-17 because its table is Item C -- third in Step 0, after two prose blocks. The single change tested here is moving the table to Item A (first element in Step 0, before lens definition in Item B and economics in Item C). Column headers remain generic (`Constraint | Downstream Section | Stated Effect`). C-14 numbered (1)-(4) protocol and C-15 formula are preserved unchanged from R3 V-04. If C-17 PASS with C-18 FAIL, this variation reaches 99.0 under v4 (one aspirational criterion missed). Combined with V-02, it isolates whether ordering and semantics are independent axes.

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

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table now, before writing Item B or Item C.

| Constraint | Downstream Section | Stated Effect |
|------------|--------------------|---------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How this constraint changes the workaround's ongoing cost or risk] |
| [same constraint phrase as row 1] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW] |
| [same constraint phrase as row 1] | VERDICT | [Prerequisite added and/or score band impact] |
| [same constraint phrase as row 1] | AMENDMENTS | [Focus-specific inertia savings unlocked when this constraint is cleared] |

This table is your delivery contract. Every section below must fulfill the Stated Effect in its row.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use this number in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint -- workaround cost ignoring focus lens]
  Focus adjustment: [Concrete focus-specific liability the workaround carries, stated as a unit rate:
    compliance focus: "audit exposure: +$X/sprint"; stakeholders focus: "sign-off overhead: +N hrs/sprint";
    size focus: "scaling degradation: +N hrs/sprint at current growth rate"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics computed in Item C.

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
| [Describe workaround] | [Focus-adjusted cost from Step 0 Item C if active; base cost if no focus] | [Risk -- include focus-specific liability from Propagation Contract if active] |

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

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). Focus-adjusted economics from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable, not only because of technical complexity. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus-adjusted cost from Step 0 Item C where it changes the rating] | [Focus-adjusted cost from Step 0 Item C if active; base cost if no focus] |

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
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify which sections are affected. Note whether focus economics change (new base cost or new focus adjustment in Item C).
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first (including the full Propagation Contract table in Item A and the updated Item C economics), then propagate the new contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
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

## V-02 -- C-18 Column Semantics Only (Table Third, Rubric-Aligned Headers, V-04-R3 Base)

**Axis**: Output format -- column headers use rubric-aligned vocabulary; `[same]` back-reference on rows 2-4
**Hypothesis**: R3 V-04 fails C-18 because its column headers are bare generics (`Constraint | Downstream Section | Stated Effect`) and rows 2-4 repeat the constraint phrase verbatim. The single change tested here is: (1) headers become "Constraint introduced by focus | Section where it surfaces | Effect on that section" and (2) rows 2-4 use `[same]` instead of the full phrase. The table stays in Item C (third position in Step 0) -- C-17 is expected FAIL. C-14 numbered (1)-(4) protocol and C-15 formula are preserved unchanged from R3 V-04. If C-18 PASS with C-17 FAIL, this variation reaches 99.0 under v4. Combined with V-01, it confirms that C-17 and C-18 are independently achievable before combining them.

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

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint -- workaround cost ignoring focus lens]
  Focus adjustment: [Concrete focus-specific liability the workaround carries, stated as a unit rate:
    compliance focus: "audit exposure: +$X/sprint"; stakeholders focus: "sign-off overhead: +N hrs/sprint";
    size focus: "scaling degradation: +N hrs/sprint at current growth rate"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item C -- Propagation Contract:**
Map the primary constraint this focus introduces to every downstream section. Complete this table before writing any section heading. The "Constraint introduced by focus" column names the single constraint that propagates through the report; use `[same]` on rows 2-4 to avoid verbatim repetition while preserving traceability.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How the focus-adjusted cost from Item B appears in the risk column or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW, referencing focus-adjusted economics] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus-adjusted cost appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base recapture + focus adjustment eliminated = stated total] |

Every section below must deliver on the "Effect on that section" cell in its row.

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

[If focus active: use the focus-adjusted do-nothing cost from Step 0 Item B. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item C).]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [Focus-adjusted cost from Step 0 Item B if active; base cost if no focus] | [Risk -- include focus constraint effect from Propagation Contract if active] |

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

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item C). Focus-adjusted economics from Item B may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable, not only because of technical complexity. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus-adjusted cost from Step 0 Item B where it changes the rating] | [Focus-adjusted cost from Step 0 Item B if active; base cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [Focus-adjusted cost from Step 0 Item B.]

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
Not building this means: "[The workaround wins on focus-adjusted economics. State the focus-adjusted do-nothing cost from Step 0 Item B and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item C).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item C). State base recapture and focus-specific savings separately so the total is transparent.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Base recapture: N hrs/sprint or $N/sprint. Focus savings: focus adjustment eliminated = N hrs/sprint or $N/sprint. Total: [base + focus] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item C table) identify which sections are affected. Note whether focus economics change (new base cost or new focus adjustment in Item B).
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first (including the full Propagation Contract table in Item C and the updated Item B economics), then propagate the new contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

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

## V-03 -- C-17 + C-18 on Minimal Base (Step A-B-C-D AMEND, C-14 PARTIAL)

**Axis**: Output format (table-first + rubric-aligned headers) on V-01-R3 base; lifecycle emphasis reduced (Steps A-B-C-D AMEND, not numbered 1-4)
**Hypothesis**: R3 V-04 achieves C-14 PASS via numbered (1)-(4) AMEND steps with explicit "Unaffected sections: [list]" declaration. This variation applies both C-17 (table-first) and C-18 (rubric-aligned headers + `[same]`) to the leaner V-01-R3 AMEND structure (Step A-B-C-D labeling, which scored C-14 PARTIAL in R3). If this variation still fails C-14 (PARTIAL), the finding confirms that C-14 precision is independent of C-17/C-18 and the correct upgrade path is V-04 (combine all three). If it somehow passes C-14 (PASS), that would suggest the scoring of R3 V-01 was lenient and the Step A-B-C-D structure is sufficient -- a useful calibration.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than staying with the workaround?" Every section below answers that question.

**If a focus dimension is active**, it changes the economics of that competition. A compliance focus may reveal the workaround carries a regulatory liability. A stakeholders focus may surface recurring escalation overhead. A size focus may reveal compounding degradation. The focus lens changes the competitive math -- it is not a section you add at the end.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "SOC 2 Type II gap", "VP sponsor not yet assigned", "identifier namespace collision at 300+ names"] | INERTIA | [How this constraint changes the workaround's ongoing cost or risk] |
| [same] | ARCHITECT | [Which component(s) it rates RED or YELLOW, and to what color] |
| [same] | VERDICT | [Prerequisite added and/or score band impact] |
| [same] | AMENDMENTS | [Focus-specific inertia savings unlocked when this constraint is cleared] |

This table is your delivery contract. Every section below must fulfill the "Effect on that section" cell in its row.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use this number in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint]
  Focus adjustment: [Unit rate for this focus type:
    compliance: "audit exposure: +$X/sprint"; stakeholders: "approval overhead: +N hrs/sprint";
    size: "scaling degradation: +N hrs/sprint at current growth"; etc.]
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

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). Focus-adjusted economics from Item C may change a component's rating. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus-adjusted cost from Step 0 Item C where it changes the rating] | [Focus-adjusted cost from Step 0 Item C if active; base cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [Focus-adjusted cost from Step 0 Item C.]

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

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). State base recapture and focus-specific savings separately.]

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
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify affected sections. Note if focus economics change (new base cost or new focus adjustment in Item C).
  For a threshold adjustment: identify which components change color. Affected = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for changed components.
  Declare: "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten."

Step C -- Re-weave affected sections only:
  Rewrite each affected section with the amendment applied. Use original section headings.
  For a focus shift: update Step 0 Items A-D first (full Propagation Contract table in Item A and updated Item C economics), then propagate through affected sections.
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

## V-04 -- C-17 + C-18 Combined on V-04-R3 Base (Ceiling Test)

**Axes**: Role sequence (table-first, C-17) + Output format (rubric-aligned headers + `[same]`, C-18) on V-04-R3 base (C-14 numbered 1-4, C-15 formula)
**Hypothesis**: R3 V-04 is the minimum-C-14 base that scored 100.000 under v3. This variation adds precisely the two v4 gaps to that base: table moves to Item A (C-17), column headers become rubric-aligned with `[same]` back-references (C-18). No other changes. If V-01 and V-02 each confirm their respective criterion passes independently, V-04 is the expected ceiling at 100.000 under v4. The combination is a minimal diff from R3 V-04: the table moves to Item A, headers change, all body pointers updated, the numbered AMEND protocol and C-15 formula are untouched.

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

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C. The "Constraint introduced by focus" column names the single constraint that propagates through the report; use `[same]` on rows 2-4 to avoid repetition while preserving traceability.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How this constraint changes the workaround's ongoing cost or risk] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW, referencing focus-adjusted economics] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus-adjusted cost appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base recapture + focus adjustment eliminated = stated total] |

This table is your delivery contract. Every section below must fulfill the "Effect on that section" cell in its row.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use this number in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run.

  Base do-nothing cost (no-focus): [N hrs/sprint or $N/sprint -- workaround cost ignoring focus lens]
  Focus adjustment: [Concrete focus-specific liability the workaround carries, stated as a unit rate:
    compliance focus: "audit exposure: +$X/sprint"; stakeholders focus: "sign-off overhead: +N hrs/sprint";
    size focus: "scaling degradation: +N hrs/sprint at current growth rate"; etc.]
  Focus-adjusted do-nothing cost: [base + adjustment = TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics computed in Item C.

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

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). Focus-adjusted economics from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable, not only because of technical complexity. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus-adjusted cost from Step 0 Item C where it changes the rating] | [Focus-adjusted cost from Step 0 Item C if active; base cost if no focus] |

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
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify which sections are affected. Note whether focus economics change (new base cost or new focus adjustment in Item C).
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first (including the full Propagation Contract table in Item A and the updated Item C economics), then propagate the new contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
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

## V-05 -- Full Battery: C-17 + C-18 on V-05-R3 Base (Maximum Precision)

**Axes**: Role sequence (table-first, C-17) + Output format (rubric-aligned headers + `[same]`, C-18) + Inertia framing (exact rubric variable names `focus_adjusted_total = base_cost + focus_adjustment` in formula AND in Stated Effect cells, C-15) + Lifecycle emphasis (numbered 1-4 AMEND with named unaffected, C-14)
**Hypothesis**: R3 V-05's advantage over R3 V-04 was using exact rubric variable names (`focus_adjusted_total`, `base_cost`, `focus_adjustment`) as tokens throughout the prompt -- in the formula, in body section pointers, and in AMENDMENTS. This variation propagates that precision one step further: the Stated Effect cells in the Propagation Contract table also reference `focus_adjusted_total` explicitly (e.g., "How focus_adjusted_total from Item C appears in the Baseline sentence"), creating a closed contract where the table's own cells name the variable the economics section will produce. This tests whether wiring the table cells to the formula tokens (not just prose descriptions) improves the reliability of C-15 and C-09 in production, beyond what V-04 achieves.

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

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing the economics.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How focus_adjusted_total from Item C appears in the risk column or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. base_cost-only run] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = stated total] |

This table is your delivery contract. Every section below must fulfill the "Effect on that section" cell in its row using the formula variables from Item C.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- workaround cost ignoring focus lens; source: inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the workaround carries:
    compliance focus: "audit exposure: +$X/sprint per open gap"; stakeholders focus: "sign-off overhead: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation: +N hrs/sprint per sprint at current growth rate"; requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics computed in Item C's formula.

---

**INFERENCE GATE**
  Feature:   [One sentence.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

---

**INERTIA: STATUS QUO -- The Workaround the Team Already Has**
Fill this before PM: BUDGET. This is the competitor you are trying to beat.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A).]

| What the team does instead | What it costs per sprint | What happens if this continues |
|----------------------------|--------------------------|-------------------------------|
| [Describe workaround] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk -- include focus constraint effect from Propagation Contract if active] |

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
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable, not only because of technical complexity. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. the focus-adjusted workaround | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses -- reference focus_adjusted_total from Step 0 Item C where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the workaround wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

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
Not building this means: "[The workaround wins on focus-adjusted economics. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the workaround on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the workaround stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent.]

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
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify which sections are affected. Note whether focus_adjusted_total changes (new base_cost or new focus_adjustment in Item C formula).
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first (including the full Propagation Contract table in Item A and the updated Item C formula), then propagate the new contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus_adjusted_total if Step 0 Item C formula changed.
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

| Variation | Primary targets | Best for | Risk |
|-----------|----------------|----------|------|
| V-01 | C-17 only | Isolating ordering axis on C-14-PASS base -- cleanest C-17 diagnostic | C-18 expected FAIL; item letter references (Item C for economics) must be consistent throughout |
| V-02 | C-18 only | Isolating column-semantics axis on C-14-PASS base -- cleanest C-18 diagnostic | C-17 expected FAIL; `[same]` on rows 2-4 is a new model behavior -- watch for model expanding it verbatim |
| V-03 | C-17 + C-18, C-14 PARTIAL base | Diagnosing whether C-14 numbered steps are necessary to reach 100 under v4 | Step A-B-C-D AMEND may score C-14 PARTIAL as in R3; result tells us whether C-14 is a prerequisite for 100 |
| V-04 | C-17 + C-18 + C-14 PASS, ceiling | Minimum-change ceiling test on V-04-R3 base | All three new-criterion changes combined; item letter consistency across 10+ body locations is the main error surface |
| V-05 | Full battery ceiling | Maximum precision: formula variable names wired into table cells | `focus_adjusted_total` referenced inside Stated Effect cells creates tighter contract but more template complexity |
