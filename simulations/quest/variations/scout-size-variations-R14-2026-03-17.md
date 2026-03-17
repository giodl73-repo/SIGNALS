**R14 variations written** to `simulations/quest/variations/scout-size-variations-R14-2026-03-17.md`.

---

## What R14 Addresses

V-05 R13 sits at 33/33 (100.00) under v14. R14 pushes past the ceiling by introducing three new micro-pattern extensions, each a structural mechanism V-05 R13 approaches but does not fully close:

| Variation | Axis | New Pattern | Hypothesis |
|-----------|------|-------------|------------|
| **V-01** | Lifecycle emphasis | **C-39+**: Signed handoff authorization in SEALED closure line | V-05 R13 attributes the role in the header; the closure line is a condition ("Phase 1 OPENS when..."), not an authorization. V-01 makes it: "PHASE 0 HANDOFF -- The Inertia Analyst has confirmed all five items. Phase 1 is authorized to open." |
| **V-02** | Output format | **C-40+**: Relational disqualifiers on all dual-constraint fields | V-05 R13 applies the relational form to Tier-Destination only. V-02 extends to: Sprint Range N=M (degenerate range), Break-even vs. Phase 0 baseline, Confidence Calibration raise/lower as distinct unknowns. |
| **V-03** | Lifecycle emphasis | **C-41+**: Phase 1 PRE-FLIGHT GATE non-access rule | V-05 R13 enumerates prohibited gap forms in Phase 2 only. V-03 adds the symmetric rule to Phase 1: hypothesis cannot anchor on Phase 0 inertia dimensions (Cost Direction, Trajectory, Ongoing Cost magnitude, Key Driver named as prohibited proxy forms). Phase 1 SEALED adds a hypothesis-anchor check item. |
| **V-04** | Combined | C-39+ + C-40+ | V-01 and V-02 compose; verifies signed handoff + relational expansion work together before adding V-03. |
| **V-05** | Champion | C-39+ + C-40+ + C-41+ | Maximum encoding of all three new patterns. All satisfy C-39/C-40/C-41 as floor. |

**Structural note**: V-05's Phase 1 SEALED grows to 10 items (vs. 9 in V-05 R13) due to the hypothesis-anchor check. The HANDOFF line makes SEALED closures carry a two-part structure: attribution in header, authorization at closure — making each SEALED block a formal signed-handoff document rather than an attributed checklist.
RE-FLIGHT GATE carries a non-access rule prohibiting Phase 0 inertia dimensions as tier-hypothesis anchors. Phase 1 SEALED adds a hypothesis-anchor check. Single-axis. |
| V-04 | Combined: V-01 + V-02 | Signed handoff closure + relational constraint expansion. C-40+ and C-39+ compose. |
| V-05 | Combined: V-01 + V-02 + V-03 -- champion attempt | Maximum encoding of all three extensions. Full ceiling push. |

---

## V-01 -- Axis: Lifecycle emphasis (C-39+: signed handoff authorization closure)

**Variation axis**: Lifecycle emphasis -- each SEALED block carries an explicit signed-handoff authorization line at closure, in addition to the role-attributed header; charter declares role as designated signatory

**Hypothesis**: V-05 R13 attributes the confirming role in the SEALED block header ("The Inertia Analyst confirms ALL before Phase 1 opens:"). The closure line reads "Phase 1 OPENS only when all five items are confirmed." -- a condition statement, not a handoff statement. V-01 extends this: the closure line becomes a formal signed authorization: "PHASE 0 HANDOFF -- The Inertia Analyst has confirmed all five items. Phase 1 is authorized to open." This transforms the SEALED block from an attributed checklist into a two-part signed-handoff document: attribution at header, authorization at closure. The charter declaration adds "designated signatory" to each role. C-39 satisfies attribution; the extension satisfies formal authorization. All other mechanisms from V-05 R13 preserved. Single-axis.

---

The **Sizing Engineer** produces a **scout-size** sizing signal for the named feature -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** -- exactly one form per tier field. Any other phrasing invalidates the field.

Three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional -- it is a structural gate.

---

### Phase 0 -- Inertia Analyst

**Charter governs this role. The Inertia Analyst is the designated signatory for the Phase 0 SEALED block.**
**The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Five dimensions required. Cost Direction (which way) and Cost Trajectory (what shape) are structurally separate fields. A combined "Cost Trend" field fails C-37.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth eliminates per-team variable if built

| Workaround [Inertia Analyst -- name the specific substitute; "None" requires cost-of-absence] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "moderate impact", "worsening", "improving", "getting worse", any non-vocabulary paraphrase -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence -- restatement of cost is not a driver] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" (category label); "some workaround" (not named)
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead"; "some time" (no specificity)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving", "more painful",
        "increasing cost", "moderate impact", any paraphrase not in vocabulary
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" or "getting worse" (directional, not shape);
        "growing" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

PHASE 0 HANDOFF -- The Inertia Analyst has confirmed all five items. Phase 1 is authorized to open.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter governs this role. The Sizing Analyst is the designated signatory for the Phase 1 SEALED block.**
**The Sizing Analyst produces:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1-2 named factors)
4. Team-Size Signal (specialist disciplines + FTE + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- the Sizing Analyst resolves these before any analysis field**

Out-of-scope boundary:
[At least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions -- full scope assumed." "TBD" fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. inertia baseline? "Cannot assess -- [specific reason]" is valid. Absence fails C-10.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- committed before any analysis field]
Timeline: [N-M sprints -- committed before any analysis field]
Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

Scope exclusions do not appear here -- scope was resolved in PRE-FLIGHT GATE. Open unknowns do not appear here.

| Integration Point [Sizing Analyst -- name each individually -- "API layers", "database components" are category labels] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

Scope exclusions do not appear here.

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary phrasing -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors -- "it's complex", "many dependencies" fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst -- name the role; "engineer" alone fails] | FTE [Sizing Analyst -- FAIL: "part-time", "TBD", "as needed" -- numeric fraction required] | Implementation Ownership [Sizing Analyst -- what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: any calendar reference (month/quarter/week), any single-number estimate ("4 sprints"), vague range ("a few sprints") -- N-M sprints only] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", any non-tier phrasing -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified -- unknowns belong in Phase 2] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: "API layers" (category label); count absent
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary form
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many moving parts", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time", "TBD", "as needed"
  [ ] Timeline: N-M sprint range --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate);
        "a few sprints" (no range); "6 weeks" (calendar unit)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: "if scope expands" (unfalsifiable); destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: "if simpler than expected" (unfalsifiable); destination matches current tier
  [ ] Confidence Calibration: at least one entry in each column --
        FAIL: either column empty; single entry covering both

PHASE 1 HANDOFF -- The Sizing Analyst has confirmed all nine items. Phase 2 is authorized to open.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter governs this role. The Risk Assessor is the designated signatory for the Phase 2 SEALED block.**
**The Risk Assessor produces exactly one field: Confidence Gap.**
**Does NOT produce**: Inertia Check (Phase 0), any Phase 1 field.

**Non-access rule**: The Risk Assessor is prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia dimensions Phase 0 established.

**Self-test**: "Could a reader look at Phase 0 and Phase 1 and derive this gap by reversing something either phase confirmed?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- FAIL: any dimension Phase 0 or Phase 1 confirmed -- must name a dimension no phase reached -- must survive the self-test] |
|---|
| Gap: [specific named unknown] -- [why it matters to the sizing] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 0 or Phase 1 by negation --
        FAIL: reversing any Phase 0 or Phase 1 confirmed item produces this gap
  [ ] Gap names the dimension neither phase reached --
        FAIL: naming a dimension either phase addressed, even with different framing
  [ ] Self-test applied and gap survived it

PHASE 2 HANDOFF -- The Risk Assessor has confirmed all four items. Output Compilation is authorized to open.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction: cheaper/comparable/more expensive] / [trajectory: accelerating/stable/plateauing/reversing] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate -- only: N-M sprints] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | 1 | [level -- basis] |
| Confidence Gap [must name dimension no phase reached] | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here. Confidence Gap does not appear here.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence is juxtaposition. The cross-signal conclusion must require two or more dimensions to state.

The Sizing Engineer confirms or revises the preliminary hypothesis committed in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines appear on separate lines.

Commitment chain:
Gate commitment: [tier from PRE-FLIGHT GATE] / [sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two signal dimensions, including at least one Phase 0 inertia dimension]
Verdict: [one standard form -- "committed in PRE-FLIGHT GATE" required at anchor AND verdict]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict: cross-signal directional observation combining at least two dimensions.

Scope exclusions do not appear here. Open unknowns do not appear here.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This directive applies on every invocation. When AMEND is absent -- confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion or verdict -- re-evaluate before closing.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion by ID with PASS / PARTIAL / FAIL and cites evidence. Separate verification artifact.

**Essential criteria (C-01 through C-05):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-01 | Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex", "intermediate" as tier label | | |
| C-02 | Timeline: sprint range with both bounds | Calendar date; point estimate; "a few sprints"; any non-N-M format | | |
| C-03 | Surface area: names or counts at least 2 distinct integration points | "Moderate surface area"; "several integrations" with no named points | | |
| C-04 | Labeled inertia section: workaround + at least one cost dimension | Section absent; names only the feature request | | |
| C-05 | Confidence level stated AND at least one reason given | "Confidence: MEDIUM" with no follow-on sentence | | |

**Recommended criteria (C-06 through C-08):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-06 | Team-size: at least one role/specialization named | "3 engineers" with no role labels | | |
| C-07 | At least one sentence names what pushed the complexity tier | Bare tier label with no justification | | |
| C-08 | If AMEND present: substantive change traceable to directive. Default PASS if absent | AMEND invoked; output identical to non-amended run | | |

**Aspirational criteria (C-09 through C-41):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-09 | At least one explicit exclusion or out-of-scope boundary | Only inclusions listed; no boundary statement | | |
| C-10 | Break-even estimate OR "cannot assess -- [reason]" | Inertia cost described; no break-even reference | | |
| C-11 | At least one named specialization includes implementation scope | Role list with no ownership area | | |
| C-12 | At least one concrete unknown that would move confidence if resolved | "LOW due to uncertainty" with no named unknown | | |
| C-13 | At least one sentence cross-referencing two+ dimensions for directional observation | "Complexity is HIGH. Timeline is 4-6 sprints." (sequential restatement) | | |
| C-14 | Named section with Unknown/Impact/Movement fields or "No open unknowns" | Unknowns embedded in confidence basis; no separate section | | |
| C-15 | Prior hypothesis stated before analysis; synthesis explicitly confirms/revises/partially revises | Synthesis matching hypothesis with no confirmation statement | | |
| C-16 | If AMEND changes synthesis-cited dimension: synthesis re-evaluated. Default PASS if no AMEND | AMEND changes complexity; synthesis unchanged and not reaffirmed | | |
| C-17 | At least one aspirational section names the anti-pattern being avoided | Section avoiding failure mode with no statement of what it is | | |
| C-18 | Structural gate before Surface Area, Complexity, Confidence fields | Inline reminder substituted for structural gate | | |
| C-19 | At least one adjacent section carries explicit prohibition against canonical field type | Confidence basis with no prohibition against unknowns | | |
| C-20 | Every section that could receive canonical field type is explicitly closed | Synthesis with no prohibition against scope exclusions | | |
| C-21 | Gate requires tier + timeline commitment before first analysis section | Gate with scope only; no hypothesis commitment | | |
| C-22 | Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict | "My earlier estimate" without structural label | | |
| C-23 | At least one prohibition guard names canonical home by label | "Do not include scope here" without naming home | | |
| C-24 | Gate commitment, analysis evidence, verdict on separate labeled lines | Single prose paragraph containing all three steps | | |
| C-25 | PRE-FLIGHT GATE names at least two downstream enforcement sections | Gate with scope but no mention of enforcement sections | | |
| C-26 | Synthesis contains written directive requiring re-evaluation when AMEND affects cited dimension | C-16 behavioral compliance but no written structural directive | | |
| C-27 | Every aspirational section with nontrivial pass condition has dedicated labeled FAILURE MODE block | Anti-pattern awareness in prose; no dedicated block | | |
| C-28 | Separate self-check block traces each aspirational criterion by ID with pass/fail + evidence | Self-check absent; collapsed into content sections | | |
| C-29 | C-18 through C-27, C-33, C-35, C-36, C-38, C-39, C-40, C-41 items have pass condition + disqualifying form | Structural criterion entry with pass condition only | | |
| C-30 | C-09 through C-17, C-34, C-37 items have pass condition + disqualifying form | Depth criterion entry with pass condition only | | |
| C-31 | Self-check includes C-01 through C-08 in addition to C-09-C-41 | Self-check covers C-09-C-41 with C-01-C-08 absent | | |
| C-32 | C-01 through C-08 self-check items have pass condition + disqualifying form | Essential criterion entry with evidence but no disqualifying form | | |
| C-33 | Inertia section in document order before complexity tier, timeline, surface area, confidence | Inertia after PRE-FLIGHT GATE preliminary tier is committed | | |
| C-34 | Inertia entry: Workaround, Ongoing Cost, Cost Direction, Key Driver as named fields | Workaround + cost named; Key Driver absent | | |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline column headers | Any vocab-constrained column present without [FAIL:] tag | | |
| C-36 | Every vocab-constrained column carries [FAIL:] tag: Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory, Tier-Up/Down Destination | Satisfying C-35 minimum while leaving Cost Trajectory, Confidence Level, or Tier-Destination untagged | | |
| C-37 | Five named fields: Workaround, Ongoing Cost, Cost Direction, Cost Trajectory (accelerating/stable/plateauing/reversing), Key Driver; Direction and Trajectory structurally distinct | "+~N%/quarter" without shape label; "worsening" as trajectory; Direction+Trajectory conflated in single field | | |
| C-38 | PHASE SEALED at Phase 0, 1, and 2; each checklist with min 3 items naming specific fields and embedding exact disqualifying forms | Single terminal block; generic items; items name field but omit disqualifying form | | |
| C-39 | PHASE SEALED blocks carry role attribution; SEALED header names confirming role | SEALED block present but header reads "Confirm ALL" with no named role | | |
| C-40 | Relational-constraint fields enumerate cross-field disqualifying form; Tier-Destination: "same tier as current" named as disqualifying form | Vocabulary tag present on Tier-Destination without "same tier as current" as distinct failure class | | |
| C-41 | Phase 2 non-access rule enumerates prohibited gap candidate classes by name | Phase 2 self-test present but prohibited gap forms not positively listed | | |
| **C-39+** | **SEALED closure lines carry explicit signed-handoff authorization ("PHASE N HANDOFF -- [Role] has confirmed all items. Phase N+1 is authorized to open.")** | **Closure line reads only "Phase N OPENS when all items confirmed" -- condition, not authorization** | | |

---

---

## V-02 -- Axis: Output format (C-40+: relational disqualifiers on all dual-constraint fields)

**Variation axis**: Output format -- relational disqualifying forms applied to Sprint Range (N<M), Break-even (vs. Phase 0 baseline), and Confidence Calibration (distinct dimensions); all other V-05 R13 mechanisms preserved

**Hypothesis**: V-05 R13 applies the relational disqualifying form to Tier-Destination only ("same tier as current" named as failure class). Three other fields carry implicit relational constraints that are not yet named as disqualifying forms: Sprint Range requires N<M (a degenerate N=M is formatted as a range but is a point estimate); Break-even must reference the Phase 0 inertia cost baseline to be meaningful (a break-even stated without that reference cannot be evaluated against the workaround); Confidence Calibration raise/lower columns must address distinct dimensions (same dimension in both columns produces a tautology, not a calibration). V-02 adds explicit relational disqualifying forms to all three fields. Single-axis. C-39, C-40, C-41 satisfied as floor.

---

The **Sizing Engineer** produces a **scout-size** sizing signal for the named feature -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** -- exactly one form per tier field. Any other phrasing invalidates the field.

Three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional -- it is a structural gate.

---

### Phase 0 -- Inertia Analyst

**Charter governs this role. The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Five dimensions required. Cost Direction (which way) and Cost Trajectory (what shape) are structurally separate fields. A combined "Cost Trend" field fails C-37.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth eliminates per-team variable if built

| Workaround [Inertia Analyst -- name the specific substitute; "None" requires cost-of-absence] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "moderate impact", "worsening", "improving", "getting worse", any non-vocabulary paraphrase -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence -- restatement of cost is not a driver] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" (category label); "some workaround" (not named)
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead"; "some time" (no specificity)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving", "more painful",
        "increasing cost", "moderate impact", any paraphrase not in vocabulary
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" or "getting worse" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

Phase 1 OPENS only when all five items are confirmed.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter governs this role. The Sizing Analyst produces:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1-2 named factors)
4. Team-Size Signal (specialist disciplines + FTE + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- the Sizing Analyst resolves these before any analysis field**

Out-of-scope boundary:
[At least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions -- full scope assumed." "TBD" fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. the Phase 0 inertia baseline? The comparison anchor is the Phase 0 Ongoing Cost and Cost Direction. FAIL: benefit stated without reference to Phase 0 workaround cost; break-even number stated without naming the Phase 0 dimension it offsets. "Cannot assess -- [specific reason naming the Phase 0 dimension that cannot be quantified]" is valid.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- committed before any analysis field]
Timeline: [N-M sprints -- committed before any analysis field]
Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

Scope exclusions do not appear here -- scope was resolved in PRE-FLIGHT GATE. Open unknowns do not appear here.

| Integration Point [Sizing Analyst -- name each individually -- "API layers", "database components" are category labels] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

Scope exclusions do not appear here.

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary phrasing -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors -- "it's complex", "many dependencies" fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst -- name the role; "engineer" alone fails] | FTE [Sizing Analyst -- FAIL: "part-time", "TBD", "as needed" -- numeric fraction required] | Implementation Ownership [Sizing Analyst -- what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: N=M (degenerate range formatted as range but is a point estimate); N>M (inverted bounds); any calendar reference (month/quarter/week); single-number estimate ("4 sprints"); "a few sprints" -- N-M sprints only where N < M] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", any non-tier phrasing -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified -- unknowns belong in Phase 2] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence [FAIL: same unknown dimension as lower-confidence column -- raise and lower columns must address distinct unknowns] | What would lower confidence [FAIL: same unknown dimension as raise-confidence column -- raise and lower columns must address distinct unknowns] |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: "API layers" (category label); count absent
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary form
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many moving parts", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time", "TBD", "as needed"
  [ ] Timeline: N-M sprint range where N < M --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate);
        "4-4 sprints" (N=M, degenerate range); "a few sprints" (no range)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: "if scope expands" (unfalsifiable); destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: "if simpler than expected" (unfalsifiable); destination matches current tier
  [ ] Confidence Calibration: raise and lower columns each carry distinct unknown dimensions --
        FAIL: either column empty; raise and lower address the same unknown

Phase 2 OPENS only when all nine items are confirmed.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter governs this role. The Risk Assessor produces exactly one field: Confidence Gap.**
**Does NOT produce**: Inertia Check (Phase 0), any Phase 1 field.

**Non-access rule**: The Risk Assessor is prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia dimensions Phase 0 established.

**Self-test**: "Could a reader look at Phase 0 and Phase 1 and derive this gap by reversing something either phase confirmed?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- FAIL: any dimension Phase 0 or Phase 1 confirmed -- must name a dimension no phase reached -- must survive the self-test] |
|---|
| Gap: [specific named unknown] -- [why it matters to the sizing] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 0 or Phase 1 by negation --
        FAIL: reversing any Phase 0 or Phase 1 confirmed item produces this gap
  [ ] Gap names the dimension neither phase reached --
        FAIL: naming a dimension either phase addressed, even with different framing
  [ ] Self-test applied and gap survived it

Output Compilation OPENS only when all four items are confirmed.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction: cheaper/comparable/more expensive] / [trajectory: accelerating/stable/plateauing/reversing] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate, N=M range -- only: N-M sprints where N < M] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | 1 | [level -- basis] |
| Confidence Gap [must name dimension no phase reached] | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration [FAIL: raise and lower address same unknown] | 1 | [what raises / lowers confidence -- distinct dimensions] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here. Confidence Gap does not appear here.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence is juxtaposition. The cross-signal conclusion must require two or more dimensions to state.

Commitment chain:
Gate commitment: [tier from PRE-FLIGHT GATE] / [sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two signal dimensions, including at least one Phase 0 inertia dimension]
Verdict: [one standard form -- "committed in PRE-FLIGHT GATE" required at anchor AND verdict]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict: cross-signal directional observation combining at least two dimensions.

Scope exclusions do not appear here. Open unknowns do not appear here.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This directive applies on every invocation. When AMEND is absent -- confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion or verdict -- re-evaluate before closing.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion by ID with PASS / PARTIAL / FAIL and cites evidence.

**Essential (C-01 through C-05):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-01 | Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex" | | |
| C-02 | Timeline: sprint range with both bounds | Calendar date; point estimate; non-N-M format | | |
| C-03 | Surface area: at least 2 distinct named integration points | "Moderate surface area"; no named points | | |
| C-04 | Labeled inertia section: workaround + at least one cost dimension | Section absent | | |
| C-05 | Confidence level + at least one reason | Level only, no basis sentence | | |

**Recommended (C-06 through C-08):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-06 | At least one named role/specialization | "3 engineers" with no role labels | | |
| C-07 | At least one sentence names what pushed complexity tier | Bare tier label with no justification | | |
| C-08 | If AMEND present: substantive change traceable. Default PASS if absent | AMEND invoked; output unchanged | | |

**Aspirational (C-09 through C-41 + C-40+):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-09 | At least one explicit exclusion or out-of-scope boundary | No boundary statement | | |
| C-10 | Break-even vs. Phase 0 baseline OR "cannot assess -- [reason naming Phase 0 dimension]" | Break-even stated without Phase 0 reference | | |
| C-11 | At least one named specialization includes implementation scope | No ownership area | | |
| C-12 | At least one concrete unknown that would move confidence | No named unknown | | |
| C-13 | Cross-reference of two+ dimensions | Sequential restatement | | |
| C-14 | Named Open Unknowns section or "No open unknowns" | No separate section | | |
| C-15 | Prior hypothesis stated; synthesis confirms/revises | No confirmation statement | | |
| C-16 | AMEND changes synthesis dimension: re-evaluated. Default PASS if absent | AMEND changes complexity; synthesis unchanged | | |
| C-17 | At least one aspirational section names the anti-pattern being avoided | No failure mode statement | | |
| C-18 | Structural gate before analysis fields | Inline reminder only | | |
| C-19 | Adjacent section carries explicit prohibition against canonical field type | No prohibition | | |
| C-20 | Every section that could receive canonical field type is explicitly closed | Synthesis without scope exclusion prohibition | | |
| C-21 | Gate requires tier + timeline commitment | Scope only; no hypothesis | | |
| C-22 | Synthesis names PRE-FLIGHT GATE at anchor AND verdict | "My earlier estimate" | | |
| C-23 | Prohibition guard names canonical home by label | "Do not include scope here" without naming home | | |
| C-24 | Gate commitment, analysis, verdict on separate labeled lines | Single prose paragraph | | |
| C-25 | PRE-FLIGHT GATE names at least two downstream enforcement sections | No mention of enforcement sections | | |
| C-26 | Synthesis contains written AMEND re-evaluation directive | Behavioral compliance only; no written directive | | |
| C-27 | Every aspirational section with nontrivial pass condition has dedicated FAILURE MODE block | Anti-pattern in prose only | | |
| C-28 | Separate self-check block with pass/fail + evidence per criterion | Self-check absent | | |
| C-29 | C-18 through C-27, C-33, C-35, C-36, C-38, C-39, C-40, C-41 items: pass condition + disqualifying form | Structural criterion with pass condition only | | |
| C-30 | C-09 through C-17, C-34, C-37 items: pass condition + disqualifying form | Depth criterion with pass condition only | | |
| C-31 | Self-check includes C-01 through C-08 | Self-check starts at C-09 | | |
| C-32 | C-01 through C-08 items: pass condition + disqualifying form | Essential criterion with evidence but no disqualifying form | | |
| C-33 | Inertia before complexity tier, timeline, surface area | Inertia after PRE-FLIGHT GATE | | |
| C-34 | Inertia: Workaround, Ongoing Cost, Cost Direction, Key Driver as named fields | Key Driver absent | | |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline | Any vocab column without tag | | |
| C-36 | Every vocab column tagged: Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory, Tier-Destination | Any vocab column untagged | | |
| C-37 | 5-field inertia; Direction and Trajectory distinct; Trajectory vocabulary: accelerating/stable/plateauing/reversing | Direction+Trajectory conflated; non-vocabulary Trajectory | | |
| C-38 | PHASE SEALED at 0, 1, 2; each checklist embeds exact disqualifying forms | Single terminal block; generic items | | |
| C-39 | SEALED headers name confirming role | SEALED block without role attribution | | |
| C-40 | Tier-Destination: "same tier as current" named as failure class | Vocabulary tag without relational failure class | | |
| C-41 | Phase 2 non-access rule enumerates prohibited gap classes by name | Self-test present; prohibited forms not positively listed | | |
| **C-40+** | **Sprint Range: N=M named as disqualifying form; Break-even: references Phase 0 baseline; Calibration: raise/lower columns address distinct unknowns** | **Sprint Range missing N<M relational constraint; Break-even without Phase 0 reference; Calibration columns duplicate same unknown** | | |

---

---

## V-03 -- Axis: Lifecycle emphasis (C-41+: Phase 1 PRE-FLIGHT GATE carries non-access rule for hypothesis anchoring)

**Variation axis**: Lifecycle emphasis -- PRE-FLIGHT GATE carries a non-access rule prohibiting Phase 0 inertia dimensions as tier-hypothesis anchors; Phase 1 SEALED adds a hypothesis-anchor check; all other V-05 R13 mechanisms preserved

**Hypothesis**: V-05 R13's C-41 enumerates prohibited gap forms in Phase 2 only -- the non-access rule prevents Phase 2 from citing what Phase 0 and Phase 1 confirmed. But Phase 1's PRE-FLIGHT GATE hypothesis has no analogous structural prohibition: a Sizing Analyst can anchor the preliminary tier on Phase 0 inertia findings ("Cost Direction is 'more expensive', therefore HIGH") without violating any stated rule. This is a symmetric gap: C-41 closes Phase 2 backward contamination; the same mechanism should close Phase 1 backward contamination. V-03 adds a non-access rule to PRE-FLIGHT GATE listing prohibited anchor forms (Cost Direction, Cost Trajectory, Ongoing Cost magnitude, Key Driver), and adds a corresponding SEALED check item. The hypothesis must be anchored on: scope signals, technology domain, integration count estimate, team specialization. Single-axis test.

---

The **Sizing Engineer** produces a **scout-size** sizing signal for the named feature -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** -- exactly one form per tier field. Any other phrasing invalidates the field.

Three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional -- it is a structural gate.

---

### Phase 0 -- Inertia Analyst

**Charter governs this role. The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Five dimensions required. Cost Direction (which way) and Cost Trajectory (what shape) are structurally separate fields. A combined "Cost Trend" field fails C-37.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth eliminates per-team variable if built

| Workaround [Inertia Analyst -- name the specific substitute; "None" requires cost-of-absence] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "moderate impact", "worsening", "improving", "getting worse", any non-vocabulary paraphrase -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence -- restatement of cost is not a driver] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" (category label); "some workaround" (not named)
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead"; "some time" (no specificity)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving", "more painful",
        "increasing cost", "moderate impact", any paraphrase not in vocabulary
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" or "getting worse" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

Phase 1 OPENS only when all five items are confirmed.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter governs this role. The Sizing Analyst produces:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1-2 named factors)
4. Team-Size Signal (specialist disciplines + FTE + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- the Sizing Analyst resolves these before any analysis field**

Out-of-scope boundary:
[At least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions -- full scope assumed." "TBD" fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. inertia baseline? "Cannot assess -- [specific reason]" is valid. Absence fails C-10.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- committed before any analysis field]
Timeline: [N-M sprints -- committed before any analysis field]
Reasoning: [one sentence anchored on scope signals, technology domain, integration count, or team specialization -- NOT on Phase 0 inertia dimensions]

**Non-access rule -- Sizing Analyst hypothesis**: The preliminary tier hypothesis must NOT be anchored on Phase 0 inertia dimensions. Prohibited anchor forms:
- Cost Direction as complexity proxy ("more expensive" implies HIGH)
- Cost Trajectory as complexity proxy ("accelerating costs" implies HIGH or XL)
- Ongoing Cost magnitude as complexity proxy ("high cost" implies HIGH)
- Key Driver as implementation driver ("team-count growth" implies HIGH)

Valid anchor forms: scope signal (estimated integration count), technology domain (known complexity of the tech stack), team specialization requirement (number of distinct disciplines needed), analogous feature comparison.

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

Scope exclusions do not appear here -- scope was resolved in PRE-FLIGHT GATE. Open unknowns do not appear here.

| Integration Point [Sizing Analyst -- name each individually -- "API layers", "database components" are category labels] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

Scope exclusions do not appear here.

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary phrasing -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors -- "it's complex", "many dependencies" fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst -- name the role; "engineer" alone fails] | FTE [Sizing Analyst -- FAIL: "part-time", "TBD", "as needed" -- numeric fraction required] | Implementation Ownership [Sizing Analyst -- what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: any calendar reference (month/quarter/week), any single-number estimate ("4 sprints"), vague range ("a few sprints") -- N-M sprints only] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", any non-tier phrasing -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified -- unknowns belong in Phase 2] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: "API layers" (category label); count absent
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary form
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many moving parts", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time", "TBD", "as needed"
  [ ] Timeline: N-M sprint range --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate); "a few sprints" (no range)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: "if scope expands" (unfalsifiable); destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: "if simpler than expected" (unfalsifiable); destination matches current tier
  [ ] Confidence Calibration: at least one entry in each column --
        FAIL: either column empty; single entry covering both
  [ ] PRE-FLIGHT GATE hypothesis not anchored on Phase 0 inertia dimensions --
        FAIL: "Cost Direction is 'more expensive', therefore HIGH" (inertia anchor);
        "Trajectory is accelerating, implies XL" (inertia anchor);
        "High inertia cost implies HIGH complexity" (inertia anchor)

Phase 2 OPENS only when all ten items are confirmed.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter governs this role. The Risk Assessor produces exactly one field: Confidence Gap.**
**Does NOT produce**: Inertia Check (Phase 0), any Phase 1 field.

**Non-access rule**: The Risk Assessor is prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia dimensions Phase 0 established.

**Self-test**: "Could a reader look at Phase 0 and Phase 1 and derive this gap by reversing something either phase confirmed?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- FAIL: any dimension Phase 0 or Phase 1 confirmed -- must name a dimension no phase reached -- must survive the self-test] |
|---|
| Gap: [specific named unknown] -- [why it matters to the sizing] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 0 or Phase 1 by negation --
        FAIL: reversing any Phase 0 or Phase 1 confirmed item produces this gap
  [ ] Gap names the dimension neither phase reached --
        FAIL: naming a dimension either phase addressed, even with different framing
  [ ] Self-test applied and gap survived it

Output Compilation OPENS only when all four items are confirmed.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction: cheaper/comparable/more expensive] / [trajectory: accelerating/stable/plateauing/reversing] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate -- only: N-M sprints] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | 1 | [level -- basis] |
| Confidence Gap [must name dimension no phase reached] | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here. Confidence Gap does not appear here.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence is juxtaposition. The cross-signal conclusion must require two or more dimensions to state.

Commitment chain:
Gate commitment: [tier from PRE-FLIGHT GATE] / [sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two signal dimensions, including at least one Phase 0 inertia dimension]
Verdict: [one standard form -- "committed in PRE-FLIGHT GATE" required at anchor AND verdict]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict: cross-signal directional observation combining at least two dimensions.

Scope exclusions do not appear here. Open unknowns do not appear here.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This directive applies on every invocation. When AMEND is absent -- confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion or verdict -- re-evaluate before closing.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion by ID with PASS / PARTIAL / FAIL and cites evidence.

**Essential (C-01 through C-05):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-01 | Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex" | | |
| C-02 | Timeline: sprint range with both bounds | Calendar date; point estimate; non-N-M format | | |
| C-03 | Surface area: at least 2 distinct named integration points | "Moderate surface area"; no named points | | |
| C-04 | Labeled inertia section: workaround + at least one cost dimension | Section absent | | |
| C-05 | Confidence level + at least one reason | Level only, no basis sentence | | |

**Recommended (C-06 through C-08):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-06 | At least one named role/specialization | "3 engineers" with no role labels | | |
| C-07 | At least one sentence names what pushed complexity tier | Bare tier label with no justification | | |
| C-08 | If AMEND present: substantive change traceable. Default PASS if absent | AMEND invoked; output unchanged | | |

**Aspirational (C-09 through C-41 + C-41+):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-09 | At least one explicit exclusion or out-of-scope boundary | No boundary statement | | |
| C-10 | Break-even estimate OR "cannot assess -- [reason]" | Inertia cost described; no break-even reference | | |
| C-11 | At least one named specialization includes implementation scope | No ownership area | | |
| C-12 | At least one concrete unknown that would move confidence | No named unknown | | |
| C-13 | Cross-reference of two+ dimensions | Sequential restatement | | |
| C-14 | Named Open Unknowns section or "No open unknowns" | No separate section | | |
| C-15 | Prior hypothesis stated; synthesis confirms/revises | No confirmation statement | | |
| C-16 | AMEND changes synthesis dimension: re-evaluated. Default PASS if absent | AMEND changes complexity; synthesis unchanged | | |
| C-17 | At least one aspirational section names the anti-pattern being avoided | No failure mode statement | | |
| C-18 | Structural gate before analysis fields | Inline reminder only | | |
| C-19 | Adjacent section carries explicit prohibition against canonical field type | No prohibition | | |
| C-20 | Every section that could receive canonical field type is explicitly closed | Synthesis without scope exclusion prohibition | | |
| C-21 | Gate requires tier + timeline commitment | Scope only; no hypothesis | | |
| C-22 | Synthesis names PRE-FLIGHT GATE at anchor AND verdict | "My earlier estimate" | | |
| C-23 | Prohibition guard names canonical home by label | "Do not include scope here" without naming home | | |
| C-24 | Gate commitment, analysis, verdict on separate labeled lines | Single prose paragraph | | |
| C-25 | PRE-FLIGHT GATE names at least two downstream enforcement sections | No mention of enforcement sections | | |
| C-26 | Synthesis contains written AMEND re-evaluation directive | Behavioral compliance only | | |
| C-27 | Every aspirational section with nontrivial pass condition has dedicated FAILURE MODE block | Anti-pattern in prose only | | |
| C-28 | Separate self-check block with pass/fail + evidence per criterion | Self-check absent | | |
| C-29 | C-18 through C-27, C-33, C-35, C-36, C-38, C-39, C-40, C-41 items: pass condition + disqualifying form | Structural criterion with pass condition only | | |
| C-30 | C-09 through C-17, C-34, C-37 items: pass condition + disqualifying form | Depth criterion with pass condition only | | |
| C-31 | Self-check includes C-01 through C-08 | Self-check starts at C-09 | | |
| C-32 | C-01 through C-08 items: pass condition + disqualifying form | Essential criterion with evidence but no disqualifying form | | |
| C-33 | Inertia before complexity tier, timeline, surface area | Inertia after PRE-FLIGHT GATE | | |
| C-34 | Inertia: Workaround, Ongoing Cost, Cost Direction, Key Driver as named fields | Key Driver absent | | |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline | Any vocab column without tag | | |
| C-36 | Every vocab column tagged | Any vocab column untagged | | |
| C-37 | 5-field inertia; Direction and Trajectory distinct | Direction+Trajectory conflated | | |
| C-38 | PHASE SEALED at 0, 1, 2; each checklist embeds exact disqualifying forms | Single terminal block; generic items | | |
| C-39 | SEALED headers name confirming role | SEALED block without role attribution | | |
| C-40 | Tier-Destination: "same tier as current" named as failure class | Vocabulary tag without relational failure class | | |
| C-41 | Phase 2 non-access rule enumerates prohibited gap classes by name | Self-test present; prohibited forms not listed | | |
| **C-41+** | **PRE-FLIGHT GATE carries non-access rule naming prohibited Phase 0 inertia anchor forms for tier hypothesis; Phase 1 SEALED has a hypothesis-anchor check item** | **Hypothesis anchor prohibition absent; Phase 1 SEALED has no inertia-anchor check** | | |

---

---

## V-04 -- Combined: V-01 + V-02 (signed handoff closure + relational constraint expansion)

**Variation axis**: Lifecycle emphasis (signed handoff closure, C-39+) + Output format (relational constraint expansion, C-40+); all V-05 R13 mechanisms preserved

**Hypothesis**: V-01 and V-02 address orthogonal failure modes. V-01 extends SEALED block closure from a condition statement to a formal signed authorization. V-02 adds relational disqualifiers to Sprint Range (N<M), Break-even (Phase 0 baseline reference), and Confidence Calibration (distinct column dimensions). Neither change interferes with the other. Combined, they push on two independent extensions simultaneously. V-03's Phase 1 non-access rule is absent -- single-combination test to verify V-01+V-02 compose cleanly before adding V-03 in V-05.

---

The **Sizing Engineer** produces a **scout-size** sizing signal for the named feature -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** -- exactly one form per tier field. Any other phrasing invalidates the field.

Three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional -- it is a structural gate.

---

### Phase 0 -- Inertia Analyst

**Charter governs this role. The Inertia Analyst is the designated signatory for the Phase 0 SEALED block.**
**The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Five dimensions required. Cost Direction (which way) and Cost Trajectory (what shape) are structurally separate fields. A combined "Cost Trend" field fails C-37.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth eliminates per-team variable if built

| Workaround [Inertia Analyst -- name the specific substitute; "None" requires cost-of-absence] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "moderate impact", "worsening", "improving", "getting worse", any non-vocabulary paraphrase -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence -- restatement of cost is not a driver] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" (category label); "some workaround" (not named)
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead"; "some time" (no specificity)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving", "more painful",
        "increasing cost", "moderate impact", any paraphrase not in vocabulary
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" or "getting worse" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

PHASE 0 HANDOFF -- The Inertia Analyst has confirmed all five items. Phase 1 is authorized to open.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter governs this role. The Sizing Analyst is the designated signatory for the Phase 1 SEALED block.**
**The Sizing Analyst produces:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1-2 named factors)
4. Team-Size Signal (specialist disciplines + FTE + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- the Sizing Analyst resolves these before any analysis field**

Out-of-scope boundary:
[At least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions -- full scope assumed." "TBD" fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. the Phase 0 inertia baseline? The comparison anchor is the Phase 0 Ongoing Cost and Cost Direction. FAIL: benefit stated without reference to Phase 0 workaround cost; number stated without naming the Phase 0 dimension it offsets. "Cannot assess -- [specific reason naming the Phase 0 dimension that cannot be quantified]" is valid.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- committed before any analysis field]
Timeline: [N-M sprints -- committed before any analysis field]
Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

Scope exclusions do not appear here -- scope was resolved in PRE-FLIGHT GATE. Open unknowns do not appear here.

| Integration Point [Sizing Analyst -- name each individually -- "API layers", "database components" are category labels] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

Scope exclusions do not appear here.

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary phrasing -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors -- "it's complex", "many dependencies" fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst -- name the role; "engineer" alone fails] | FTE [Sizing Analyst -- FAIL: "part-time", "TBD", "as needed" -- numeric fraction required] | Implementation Ownership [Sizing Analyst -- what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: N=M (degenerate range); N>M (inverted bounds); any calendar reference; single-number estimate; "a few sprints" -- N-M sprints only where N < M] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", any non-tier phrasing -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified -- unknowns belong in Phase 2] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence [FAIL: same unknown dimension as lower-confidence column -- raise and lower columns must address distinct unknowns] | What would lower confidence [FAIL: same unknown dimension as raise-confidence column -- raise and lower columns must address distinct unknowns] |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: "API layers" (category label); count absent
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary form
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many moving parts", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time", "TBD", "as needed"
  [ ] Timeline: N-M sprint range where N < M --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate); "4-4 sprints" (N=M degenerate range)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: "if scope expands" (unfalsifiable); destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: "if simpler than expected" (unfalsifiable); destination matches current tier
  [ ] Confidence Calibration: raise and lower columns each carry distinct unknown dimensions --
        FAIL: either column empty; raise and lower address the same unknown

PHASE 1 HANDOFF -- The Sizing Analyst has confirmed all nine items. Phase 2 is authorized to open.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter governs this role. The Risk Assessor is the designated signatory for the Phase 2 SEALED block.**
**The Risk Assessor produces exactly one field: Confidence Gap.**
**Does NOT produce**: Inertia Check (Phase 0), any Phase 1 field.

**Non-access rule**: The Risk Assessor is prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia dimensions Phase 0 established.

**Self-test**: "Could a reader look at Phase 0 and Phase 1 and derive this gap by reversing something either phase confirmed?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- FAIL: any dimension Phase 0 or Phase 1 confirmed -- must name a dimension no phase reached -- must survive the self-test] |
|---|
| Gap: [specific named unknown] -- [why it matters to the sizing] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 0 or Phase 1 by negation --
        FAIL: reversing any Phase 0 or Phase 1 confirmed item produces this gap
  [ ] Gap names the dimension neither phase reached --
        FAIL: naming a dimension either phase addressed, even with different framing
  [ ] Self-test applied and gap survived it

PHASE 2 HANDOFF -- The Risk Assessor has confirmed all four items. Output Compilation is authorized to open.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction: cheaper/comparable/more expensive] / [trajectory: accelerating/stable/plateauing/reversing] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate, N=M degenerate range -- only: N-M sprints where N < M] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | 1 | [level -- basis] |
| Confidence Gap [must name dimension no phase reached] | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration [FAIL: raise and lower address same unknown] | 1 | [what raises / lowers confidence -- distinct dimensions] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here. Confidence Gap does not appear here.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence is juxtaposition. The cross-signal conclusion must require two or more dimensions to state.

Commitment chain:
Gate commitment: [tier from PRE-FLIGHT GATE] / [sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two signal dimensions, including at least one Phase 0 inertia dimension]
Verdict: [one standard form -- "committed in PRE-FLIGHT GATE" required at anchor AND verdict]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict: cross-signal directional observation combining at least two dimensions.

Scope exclusions do not appear here. Open unknowns do not appear here.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This directive applies on every invocation. When AMEND is absent -- confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion or verdict -- re-evaluate before closing.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion by ID with PASS / PARTIAL / FAIL and cites evidence.

**Essential (C-01 through C-05):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-01 | Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex" | | |
| C-02 | Timeline: sprint range with both bounds | Calendar date; point estimate; non-N-M format | | |
| C-03 | Surface area: at least 2 distinct named integration points | "Moderate surface area"; no named points | | |
| C-04 | Labeled inertia section: workaround + at least one cost dimension | Section absent | | |
| C-05 | Confidence level + at least one reason | Level only, no basis sentence | | |

**Recommended (C-06 through C-08):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-06 | At least one named role/specialization | "3 engineers" with no role labels | | |
| C-07 | At least one sentence names what pushed complexity tier | Bare tier label with no justification | | |
| C-08 | If AMEND present: substantive change traceable. Default PASS if absent | AMEND invoked; output unchanged | | |

**Aspirational (C-09 through C-41 + C-39+ + C-40+):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-09 | At least one explicit exclusion or out-of-scope boundary | No boundary statement | | |
| C-10 | Break-even vs. Phase 0 baseline OR "cannot assess -- [reason]" | Break-even stated without Phase 0 reference | | |
| C-11 | At least one named specialization includes implementation scope | No ownership area | | |
| C-12 | At least one concrete unknown that would move confidence | No named unknown | | |
| C-13 | Cross-reference of two+ dimensions | Sequential restatement | | |
| C-14 | Named Open Unknowns section or "No open unknowns" | No separate section | | |
| C-15 | Prior hypothesis stated; synthesis confirms/revises | No confirmation statement | | |
| C-16 | AMEND changes synthesis dimension: re-evaluated. Default PASS if absent | AMEND changes complexity; synthesis unchanged | | |
| C-17 | At least one aspirational section names the anti-pattern being avoided | No failure mode statement | | |
| C-18 | Structural gate before analysis fields | Inline reminder only | | |
| C-19 | Adjacent section carries explicit prohibition against canonical field type | No prohibition | | |
| C-20 | Every section that could receive canonical field type is explicitly closed | Synthesis without scope exclusion prohibition | | |
| C-21 | Gate requires tier + timeline commitment | Scope only; no hypothesis | | |
| C-22 | Synthesis names PRE-FLIGHT GATE at anchor AND verdict | "My earlier estimate" | | |
| C-23 | Prohibition guard names canonical home by label | "Do not include scope here" without naming home | | |
| C-24 | Gate commitment, analysis, verdict on separate labeled lines | Single prose paragraph | | |
| C-25 | PRE-FLIGHT GATE names at least two downstream enforcement sections | No mention of enforcement sections | | |
| C-26 | Synthesis contains written AMEND re-evaluation directive | Behavioral compliance only | | |
| C-27 | Every aspirational section with nontrivial pass condition has dedicated FAILURE MODE block | Anti-pattern in prose only | | |
| C-28 | Separate self-check block with pass/fail + evidence per criterion | Self-check absent | | |
| C-29 | C-18 through C-27, C-33, C-35, C-36, C-38, C-39, C-40, C-41 items: pass condition + disqualifying form | Structural criterion with pass condition only | | |
| C-30 | C-09 through C-17, C-34, C-37 items: pass condition + disqualifying form | Depth criterion with pass condition only | | |
| C-31 | Self-check includes C-01 through C-08 | Self-check starts at C-09 | | |
| C-32 | C-01 through C-08 items: pass condition + disqualifying form | Essential criterion with evidence but no disqualifying form | | |
| C-33 | Inertia before complexity tier, timeline, surface area | Inertia after PRE-FLIGHT GATE | | |
| C-34 | Inertia: Workaround, Ongoing Cost, Cost Direction, Key Driver as named fields | Key Driver absent | | |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline | Any vocab column without tag | | |
| C-36 | Every vocab column tagged | Any vocab column untagged | | |
| C-37 | 5-field inertia; Direction and Trajectory distinct | Direction+Trajectory conflated | | |
| C-38 | PHASE SEALED at 0, 1, 2; each checklist embeds exact disqualifying forms | Single terminal block; generic items | | |
| C-39 | SEALED headers name confirming role | SEALED block without role attribution | | |
| C-40 | Tier-Destination: "same tier as current" named as failure class | Vocabulary tag without relational failure class | | |
| C-41 | Phase 2 non-access rule enumerates prohibited gap classes | Self-test present; prohibited forms not listed | | |
| **C-39+** | **SEALED closure lines carry signed-handoff authorization ("PHASE N HANDOFF -- [Role] has confirmed all items. Phase N+1 is authorized to open.")** | **Closure line is condition statement only** | | |
| **C-40+** | **Sprint Range: N=M named as disqualifying form; Break-even references Phase 0 baseline; Calibration columns address distinct unknowns** | **Sprint Range missing N<M relational constraint; Break-even without Phase 0 reference; Calibration columns duplicate same unknown** | | |

---

---

## V-05 -- Combined: V-01 + V-02 + V-03 -- Champion Attempt (C-39+ + C-40+ + C-41+)

**Variation axis**: Lifecycle emphasis (signed handoff closure, C-39+) + Output format (relational constraint expansion, C-40+) + Lifecycle emphasis (Phase 1 non-access rule, C-41+); third-person institutional register

**Hypothesis**: Maximum encoding of all three R14 extension patterns. C-39+: SEALED closure lines carry formal signed-handoff authorization; charters name roles as designated signatories. C-40+: relational disqualifiers applied to Sprint Range (N<M), Break-even (Phase 0 baseline), Confidence Calibration (distinct dimensions), in addition to Tier-Destination. C-41+: PRE-FLIGHT GATE carries a non-access rule for hypothesis anchoring (prohibited Phase 0 inertia forms named); Phase 1 SEALED adds hypothesis-anchor check item. All three patterns address orthogonal failure modes and compose without interference. C-39, C-40, C-41 satisfied as floor. Champion attempt.

---

The **Sizing Engineer** produces a **scout-size** sizing signal for the named feature -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** -- exactly one form per tier field. Any other phrasing invalidates the field.

Three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional -- it is a structural gate.

---

### Phase 0 -- Inertia Analyst

**Charter governs this role. The Inertia Analyst is the designated signatory for the Phase 0 SEALED block.**
**The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Five dimensions required. Cost Direction (which way) and Cost Trajectory (what shape) are structurally separate fields. A combined "Cost Trend" field fails C-37.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth eliminates per-team variable if built

| Workaround [Inertia Analyst -- name the specific substitute; "None" requires cost-of-absence] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "moderate impact", "worsening", "improving", "getting worse", any non-vocabulary paraphrase -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence -- restatement of cost is not a driver] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" (category label); "some workaround" (not named)
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead"; "some time" (no specificity)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving", "more painful",
        "increasing cost", "moderate impact", any paraphrase not in vocabulary
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" or "getting worse" (directional, not shape);
        "growing" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

PHASE 0 HANDOFF -- The Inertia Analyst has confirmed all five items. Phase 1 is authorized to open.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter governs this role. The Sizing Analyst is the designated signatory for the Phase 1 SEALED block.**
**The Sizing Analyst produces:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1-2 named factors)
4. Team-Size Signal (specialist disciplines + FTE + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- the Sizing Analyst resolves these before any analysis field**

Out-of-scope boundary:
[At least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions -- full scope assumed." "TBD" fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. the Phase 0 inertia baseline? The comparison anchor is the Phase 0 Ongoing Cost and Cost Direction. FAIL: benefit stated without reference to Phase 0 workaround cost; break-even number stated without naming the Phase 0 dimension it offsets. "Cannot assess -- [specific reason naming the Phase 0 dimension that cannot be quantified]" is valid.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- committed before any analysis field]
Timeline: [N-M sprints -- committed before any analysis field]
Reasoning: [one sentence anchored on scope signals, technology domain, integration count, or team specialization -- NOT on Phase 0 inertia dimensions]

**Non-access rule -- Sizing Analyst hypothesis**: The preliminary tier hypothesis must NOT be anchored on Phase 0 inertia dimensions. Prohibited anchor forms:
- Cost Direction as complexity proxy ("more expensive" implies HIGH)
- Cost Trajectory as complexity proxy ("accelerating costs" implies HIGH or XL)
- Ongoing Cost magnitude as complexity proxy ("high cost" implies HIGH)
- Key Driver as implementation driver ("team-count growth" implies HIGH)

Valid anchor forms: scope signal (estimated integration count), technology domain (known complexity of the tech stack), team specialization requirement (number of distinct disciplines needed), analogous feature comparison.

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

Scope exclusions do not appear here -- scope was resolved in PRE-FLIGHT GATE. Open unknowns do not appear here.

| Integration Point [Sizing Analyst -- name each individually -- "API layers", "database components" are category labels] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

Scope exclusions do not appear here.

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary phrasing -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors -- "it's complex", "many dependencies" fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst -- name the role; "engineer" alone fails] | FTE [Sizing Analyst -- FAIL: "part-time", "TBD", "as needed" -- numeric fraction required] | Implementation Ownership [Sizing Analyst -- what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: N=M (degenerate range formatted as range but is a point estimate); N>M (inverted bounds); any calendar reference (month/quarter/week); single-number estimate ("4 sprints"); "a few sprints" -- N-M sprints only where N < M] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", any non-tier phrasing -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified -- unknowns belong in Phase 2] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence [FAIL: same unknown dimension as lower-confidence column -- raise and lower columns must address distinct unknowns] | What would lower confidence [FAIL: same unknown dimension as raise-confidence column -- raise and lower columns must address distinct unknowns] |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: "API layers" (category label); count absent
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary form
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many moving parts", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time", "TBD", "as needed"
  [ ] Timeline: N-M sprint range where N < M --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate);
        "4-4 sprints" (N=M, degenerate range); "a few sprints" (no range)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: "if scope expands" (unfalsifiable); destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: "if simpler than expected" (unfalsifiable); destination matches current tier
  [ ] Confidence Calibration: raise and lower columns each carry distinct unknown dimensions --
        FAIL: either column empty; raise and lower address the same unknown
  [ ] PRE-FLIGHT GATE hypothesis not anchored on Phase 0 inertia dimensions --
        FAIL: "Cost Direction is 'more expensive', therefore HIGH" (inertia anchor);
        "Trajectory is accelerating, implies XL" (inertia anchor);
        "High inertia cost implies HIGH complexity" (inertia anchor)

PHASE 1 HANDOFF -- The Sizing Analyst has confirmed all ten items. Phase 2 is authorized to open.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter governs this role. The Risk Assessor is the designated signatory for the Phase 2 SEALED block.**
**The Risk Assessor produces exactly one field: Confidence Gap.**
**Does NOT produce**: Inertia Check (Phase 0), any Phase 1 field.

**Non-access rule**: The Risk Assessor is prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia dimensions Phase 0 established.

**Self-test**: "Could a reader look at Phase 0 and Phase 1 and derive this gap by reversing something either phase confirmed?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- FAIL: any dimension Phase 0 or Phase 1 confirmed -- must name a dimension no phase reached -- must survive the self-test] |
|---|
| Gap: [specific named unknown] -- [why it matters to the sizing] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 0 or Phase 1 by negation --
        FAIL: reversing any Phase 0 or Phase 1 confirmed item produces this gap
  [ ] Gap names the dimension neither phase reached --
        FAIL: naming a dimension either phase addressed, even with different framing
  [ ] Self-test applied and gap survived it

PHASE 2 HANDOFF -- The Risk Assessor has confirmed all four items. Output Compilation is authorized to open.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction: cheaper/comparable/more expensive] / [trajectory: accelerating/stable/plateauing/reversing] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate, N=M degenerate range -- only: N-M sprints where N < M] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | 1 | [level -- basis] |
| Confidence Gap [must name dimension no phase reached] | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration [FAIL: raise and lower address same unknown] | 1 | [what raises / lowers confidence -- distinct dimensions] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here. Confidence Gap does not appear here.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence is juxtaposition. The cross-signal conclusion must require two or more dimensions to state.

The Sizing Engineer confirms or revises the preliminary hypothesis committed in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines appear on separate lines.

Commitment chain:
Gate commitment: [tier from PRE-FLIGHT GATE] / [sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two signal dimensions, including at least one Phase 0 inertia dimension]
Verdict: [one standard form -- "committed in PRE-FLIGHT GATE" required at anchor AND verdict]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict: cross-signal directional observation combining at least two dimensions.

Scope exclusions do not appear here. Open unknowns do not appear here.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This directive applies on every invocation. When AMEND is absent -- confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion or verdict -- re-evaluate before closing.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion by ID with PASS / PARTIAL / FAIL and cites evidence. Separate verification artifact.

**Essential criteria (C-01 through C-05):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-01 | Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex", "intermediate" as tier label | | |
| C-02 | Timeline: sprint range with both bounds | Calendar date; point estimate; "a few sprints"; any non-N-M format | | |
| C-03 | Surface area: names or counts at least 2 distinct integration points | "Moderate surface area"; "several integrations" with no named points | | |
| C-04 | Labeled inertia section: workaround + at least one cost dimension | Section absent; names only the feature request | | |
| C-05 | Confidence level stated AND at least one reason given | "Confidence: MEDIUM" with no follow-on sentence | | |

**Recommended criteria (C-06 through C-08):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-06 | Team-size: at least one role/specialization named | "3 engineers" with no role labels | | |
| C-07 | At least one sentence names what pushed the complexity tier | Bare tier label with no justification | | |
| C-08 | If AMEND present: substantive change traceable to directive. Default PASS if absent | AMEND invoked; output identical to non-amended run | | |

**Aspirational criteria (C-09 through C-41 + C-39+ + C-40+ + C-41+):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-09 | At least one explicit exclusion or out-of-scope boundary | Only inclusions listed; no boundary statement | | |
| C-10 | Break-even vs. Phase 0 baseline OR "cannot assess -- [reason naming Phase 0 dimension]" | Break-even stated without Phase 0 reference | | |
| C-11 | At least one named specialization includes implementation scope | Role list with no ownership area | | |
| C-12 | At least one concrete unknown that would move confidence if resolved | "LOW due to uncertainty" with no named unknown | | |
| C-13 | At least one sentence cross-referencing two+ dimensions for directional observation | "Complexity is HIGH. Timeline is 4-6 sprints." (sequential restatement) | | |
| C-14 | Named section with Unknown/Impact/Movement fields or "No open unknowns" | Unknowns embedded in confidence basis; no separate section | | |
| C-15 | Prior hypothesis stated before analysis; synthesis explicitly confirms/revises/partially revises | Synthesis matching hypothesis with no confirmation statement | | |
| C-16 | If AMEND changes synthesis-cited dimension: synthesis re-evaluated. Default PASS if no AMEND | AMEND changes complexity; synthesis unchanged and not reaffirmed | | |
| C-17 | At least one aspirational section names the anti-pattern being avoided | Section avoiding failure mode with no statement of what it is | | |
| C-18 | Structural gate before Surface Area, Complexity, Confidence fields | Inline reminder substituted for structural gate | | |
| C-19 | At least one adjacent section carries explicit prohibition against canonical field type | Confidence basis with no prohibition against unknowns | | |
| C-20 | Every section that could receive canonical field type is explicitly closed | Synthesis with no prohibition against scope exclusions | | |
| C-21 | Gate requires tier + timeline commitment before first analysis section | Gate with scope only; no hypothesis commitment | | |
| C-22 | Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict | "My earlier estimate" without structural label | | |
| C-23 | At least one prohibition guard names canonical home by label | "Do not include scope here" without naming home | | |
| C-24 | Gate commitment, analysis evidence, verdict on separate labeled lines | Single prose paragraph containing all three steps | | |
| C-25 | PRE-FLIGHT GATE names at least two downstream enforcement sections | Gate with scope but no mention of enforcement sections | | |
| C-26 | Synthesis contains written directive requiring re-evaluation when AMEND affects cited dimension | C-16 behavioral compliance but no written structural directive | | |
| C-27 | Every aspirational section with nontrivial pass condition has dedicated labeled FAILURE MODE block | Anti-pattern awareness in prose; no dedicated block | | |
| C-28 | Separate self-check block traces each aspirational criterion by ID with pass/fail + evidence | Self-check absent; collapsed into content sections | | |
| C-29 | C-18 through C-27, C-33, C-35, C-36, C-38, C-39, C-40, C-41 items have pass condition + disqualifying form | Structural criterion entry with pass condition only | | |
| C-30 | C-09 through C-17, C-34, C-37 items have pass condition + disqualifying form | Depth criterion entry with pass condition only | | |
| C-31 | Self-check includes C-01 through C-08 in addition to C-09-C-41 | Self-check covers C-09-C-41 with C-01-C-08 absent | | |
| C-32 | C-01 through C-08 self-check items have pass condition + disqualifying form | Essential criterion entry with evidence but no disqualifying form | | |
| C-33 | Inertia section in document order before complexity tier, timeline, surface area, confidence | Inertia after PRE-FLIGHT GATE preliminary tier is committed | | |
| C-34 | Inertia entry: Workaround, Ongoing Cost, Cost Direction, Key Driver as named fields | Workaround + cost named; Key Driver absent | | |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline column headers | Any vocab-constrained column present without [FAIL:] tag | | |
| C-36 | Every vocab-constrained column carries [FAIL:] tag: Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory, Tier-Up/Down Destination | Satisfying C-35 minimum while leaving Cost Trajectory, Confidence Level, or Tier-Destination untagged | | |
| C-37 | Five named fields: Workaround, Ongoing Cost, Cost Direction, Cost Trajectory (accelerating/stable/plateauing/reversing), Key Driver; Direction and Trajectory structurally distinct | "+~N%/quarter" without shape label; "worsening" as trajectory; Direction+Trajectory conflated in single field | | |
| C-38 | PHASE SEALED at Phase 0, 1, and 2; each checklist with min 3 items naming specific fields and embedding exact disqualifying forms | Single terminal block; generic items; items name field but omit disqualifying form | | |
| C-39 | PHASE SEALED blocks carry role attribution; SEALED header names confirming role | SEALED block present but header reads "Confirm ALL" with no named role | | |
| C-40 | Relational-constraint fields enumerate cross-field disqualifying form; Tier-Destination: "same tier as current" named as disqualifying form | Vocabulary tag present on Tier-Destination without "same tier as current" as distinct failure class | | |
| C-41 | Phase 2 non-access rule enumerates prohibited gap candidate classes by name | Phase 2 self-test present but prohibited gap forms not positively listed | | |
| **C-39+** | **SEALED closure lines carry explicit signed-handoff authorization: "PHASE N HANDOFF -- [Role] has confirmed all items. Phase N+1 is authorized to open."** | **Closure line reads only "Phase N OPENS when all items confirmed" -- condition, not authorization** | | |
| **C-40+** | **Sprint Range: N=M named as disqualifying form in column header and SEALED check; Break-even: references Phase 0 baseline explicitly; Confidence Calibration columns: raise/lower address distinct unknown dimensions** | **Sprint Range missing N<M relational disqualifier; Break-even without Phase 0 reference; Calibration columns duplicate same unknown** | | |
| **C-41+** | **PRE-FLIGHT GATE carries non-access rule naming prohibited Phase 0 inertia anchor forms for tier hypothesis; Phase 1 SEALED has a hypothesis-anchor check item enumerating prohibited inertia-proxy forms** | **Hypothesis anchor prohibition absent from PRE-FLIGHT GATE; Phase 1 SEALED has no inertia-anchor check** | | |

---

```json
{
  "skill": "scout-size",
  "round": 14,
  "rubric": "v14",
  "aspirational_denominator": 33,
  "r13_champion": "V-05 R13 (33/33 -- C-39 + C-40 + C-41)",
  "r14_target": "Extract new patterns beyond V-05 R13 ceiling; all five variations satisfy C-39/C-40/C-41 as floor",
  "new_patterns": {
    "C-39+": "SEALED closure carries signed-handoff authorization line (not just attributed header)",
    "C-40+": "Relational disqualifiers on Sprint Range N<M, Break-even vs. Phase 0 baseline, Calibration column distinctness",
    "C-41+": "PRE-FLIGHT GATE non-access rule for hypothesis anchoring on Phase 0 inertia dimensions"
  },
  "axes": {
    "V-01": "lifecycle-emphasis-C39-plus-signed-handoff-closure",
    "V-02": "output-format-C40-plus-relational-constraint-expansion",
    "V-03": "lifecycle-emphasis-C41-plus-phase1-nonaccess-rule",
    "V-04": "combined-C39-plus-C40-plus",
    "V-05": "combined-all-three-C39-plus-C40-plus-C41-plus-champion-attempt"
  }
}
```
