## `/quest:variate` — topic-retro · Round 5 · V-01 through V-05

---

## V-01 — Axis: Role Sequence (Forensic-first, audit-locked Echo)

**Hypothesis**: Framing the agent as a forensic auditor who locks the Echo before touching any data prevents post-hoc rationalization. The audit role's natural sequence (observation → record → verify) structurally enforces C-12, C-17, and C-16.

---

```
You are a forensic retrospective auditor. Your job is to examine a completed feature topic and produce an immutable record of signal accuracy. You work in strict phase order. You do not revise earlier phases based on later findings — you document the tension instead.

## Inputs

- Topic: {{topic}}
- Signals gathered (list artifact names, dates, namespaces): {{signals}}
- What actually happened after the feature shipped: {{outcomes}}
- Prior retro reference (optional, for calibration): {{prior_retro}}
- AMEND scope (optional): {{amend}}

---

## Phase 1 — ECHO (LOCKED)

Before reading any signal data, state the single most surprising thing you learned from this retrospective. This is your gut observation from the surface-level review only.

Format:
> **ECHO (LOCKED):** [Single sentence. Surprising. Not anticipated. Written before accuracy data is computed.]

This Echo is now sealed. It cannot be revised. Any tension between this Echo and later analysis must be documented in Phase 5, not resolved by editing Phase 1.

---

## Phase 2 — Signal Inventory

List every signal artifact for this topic. One row per artifact. No omissions.

| Namespace | Artifact | Date | Prediction at Signal Time |
|-----------|----------|------|--------------------------|
| … | … | … | … |

If AMEND scope is provided, include only artifacts within scope.

---

## Phase 3 — Accuracy Scoring

For each artifact, compare the prediction to what actually happened.

Accuracy column header: `Score: (C×100 + P×50) / (C+P+W)  [e.g. C=2, P=1, W=1 → 62.5]`

| Namespace | Artifact | Outcome | Result (C/P/W) | Revision Log |
|-----------|----------|---------|----------------|--------------|
| … | … | … | … | *(leave blank or note tension)* |

After the table, compute per-namespace accuracy using the formula above. Then render an overall accuracy judgment: ratio, score, and qualitative tier (Strong / Adequate / Weak).

Break accuracy down by namespace. Do not average namespaces into a single number without also showing the per-namespace breakdown.

---

## Phase 4 — Gap Analysis

Identify signal types that were absent for this topic. For each gap:

| Missing Signal Type | Namespace | Why It Mattered | Concrete Next Action |
|--------------------|-----------|-----------------|----------------------|
| … | … | … | *(skill to run, question to ask, threshold to set)* |

Generic statements ("we had fewer signals than ideal") do not satisfy this phase. Each gap must name a namespace, a signal type, and a specific corrective action.

If AMEND scope is active, restrict gaps to within-scope namespaces only.

---

## Phase 5 — Conflict Audit (Mandatory — runs whether or not tension is perceived)

Review every entry in the Revision Log column from Phase 3. For each:
- If a Phase 3 or Phase 4 finding would change the Echo: document the tension explicitly. Preserve the Phase 1 Echo unchanged.
- If no tension exists: state explicitly: "No conflict detected. Echo preserved as written."

This phase produces an explicit result in all cases. Silence is not a valid output.

| Source Phase | Finding | Tension with Echo? | Resolution |
|-------------|---------|-------------------|------------|
| … | … | Yes / No | *(preserve Echo, note tension)* or "No conflict" |

---

## Calibration (if prior retro provided)

Compare this topic's overall accuracy to the prior retro. Is prediction quality improving, degrading, or stable? One paragraph.

## Echo Feedback Loop

Translate the locked Echo into a concrete change proposal. Not "we learned X" — but "therefore, skill Y should be amended / rubric Z should add criterion / threshold T should shift from A to B."
```

---

## V-02 — Axis: Output Format (Table-dominant, formula-anchored columns)

**Hypothesis**: When every section is a named table with formula-anchored column headers, the scorer can verify all 18 criteria purely by inspecting column labels — no prose interpretation required. Maximizes C-13, C-15, C-18 signal density.

---

```
Run a post-commitment retrospective on the topic below. Produce output as a sequence of five named tables. Every scoring column must carry its formula in the header. Work in the order shown — do not reorder phases.

## Inputs

Topic: {{topic}}
Signals: {{signals}}
Outcomes after ship: {{outcomes}}
Prior retro (optional): {{prior_retro}}
AMEND scope (optional): {{amend}}

---

### PHASE 1 — ECHO (LOCKED)

Single-cell table. Written before any signal data is processed.

| ECHO (LOCKED) |
|---------------|
| *[One sentence. The most surprising thing from initial surface review. Immutable after this phase.]* |

---

### PHASE 2 — Signal Inventory

One row per artifact. No omissions. If AMEND scope provided, include only in-scope artifacts.

| # | Namespace | Artifact Name | Date | Prediction Made at Signal Time |
|---|-----------|---------------|------|-------------------------------|
| 1 | … | … | … | … |

---

### PHASE 3 — Accuracy Table

Column header carries formula and worked example. Compute per-namespace sub-totals at the bottom.

| Namespace | Artifact | Actual Outcome | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Revision Log |
|-----------|----------|----------------|-------|----------------------------------------------------------|--------------|
| … | … | … | … | … | *(blank or tension note)* |
| **[namespace subtotal]** | | | C=_ P=_ W=_ | *[computed]* | |
| **OVERALL** | | | C=_ P=_ W=_ | *[computed]* | Tier: Strong / Adequate / Weak |

---

### PHASE 4 — Gap Registry

| Gap # | Missing Signal Type | Namespace | Consequence | Action: Skill / Question / Threshold |
|-------|--------------------|-----------|-----------|-----------------------------------------|
| G-01 | … | … | … | … |

---

### PHASE 5 — Conflict Audit (Unconditional)

This table runs regardless of whether tension exists. Every row from the Revision Log is examined. If Revision Log was empty, produce one explicit row confirming no conflict.

| Source | Phase-3/4 Finding | Tension with ECHO? | Disposition |
|--------|------------------|-------------------|-------------|
| … | … | Yes / No | Preserve Echo + note tension *or* No conflict detected |

---

### Calibration Block (if prior retro available)

| Dimension | This Topic | Prior Retro | Trend |
|-----------|-----------|-------------|-------|
| Overall Score | … | … | Improving / Stable / Degrading |
| Weakest Namespace | … | … | … |

---

### Echo Feedback

| Echo (Locked) | Proposed Change | Target Artifact |
|--------------|-----------------|-----------------|
| *[repeat locked Echo]* | *[concrete skill/rubric/threshold change]* | *[skill name, rubric ID, or threshold label]* |
```

---

## V-03 — Axis: Phrasing Register (Conversational, first-person team voice)

**Hypothesis**: A conversational register lowers the cognitive barrier for teams writing their first retro. The five-phase structure remains intact but reads like a facilitated team exercise rather than a scoring instrument. Tests whether friendlier framing reduces omissions (C-01, C-03) without sacrificing structural requirements (C-12, C-17, C-18).

---

```
You're running a post-ship retrospective for the team. This isn't a post-mortem — it's a signal calibration session. You want to understand: which signals told the truth, which didn't, and what the team didn't see coming. Work through the five phases below in order. Phase ordering is not optional.

---

**What you're working with:**

- Topic: {{topic}}
- Signals the team gathered (names, dates, namespaces): {{signals}}
- What actually happened: {{outcomes}}
- A prior retro for comparison (if you have one): {{prior_retro}}
- Narrowed scope (if the team only wants to review certain signals): {{amend}}

---

## Phase 1 — ECHO (LOCKED)
*Do this before you look at any numbers.*

What's the one thing that genuinely surprised you about how the signals played out? Not "we could have done better" — something you actually didn't see coming. Write it as a single sentence.

> **ECHO (LOCKED):** ___

Once you've written it, that's it. You don't get to revise it later. If the data later makes you want to change it, you'll note that in Phase 5 instead of editing this line.

---

## Phase 2 — What Signals Did We Actually Gather?

Make a table. Every artifact the team produced for this topic gets a row. Don't leave any out — the point is to see the full picture.

| Namespace | Artifact | Date | What We Expected When We Made It |
|-----------|----------|------|----------------------------------|
| | | | |

If you're working within a narrowed scope (AMEND), only list the in-scope artifacts.

---

## Phase 3 — How Accurate Were We?

For each artifact from Phase 2, write down what actually happened and grade it:
- **C** — Correct: the prediction was right
- **P** — Partial: it pointed the right direction but missed something
- **W** — Wrong: the prediction didn't hold up

Use this formula for namespace scores (put it in the column header so it's always visible):
`Score: (C×100 + P×50) / (C+P+W)  [e.g. C=2, P=1, W=1 → 62.5]`

| Namespace | Artifact | What Happened | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Notes |
|-----------|----------|--------------|-------|--------------------------------------------------------|-------|
| | | | | | |

After filling in the table: compute a score per namespace. Then give an overall judgment — is the team's signal accuracy Strong, Adequate, or Weak, and what's the number behind that?

---

## Phase 4 — What Signals Were We Missing?

Look at what you didn't gather. For each gap, you need to be specific: name the namespace, name the signal type, and say what you'd do differently next time (which skill to run, what question to ask, what threshold to check). "We should have more signals" isn't useful here.

| Missing Type | Namespace | Why It Would Have Helped | What to Do Next Time |
|-------------|-----------|-------------------------|--------------------|
| | | | |

---

## Phase 5 — Conflict Audit
*This phase runs no matter what. Even if you think nothing conflicts with the Echo.*

Go back through anything you flagged in Phase 3. Does any of that analysis make you want to revise the Echo? If yes: don't revise it — write down the tension here. If no: write that explicitly too. Silence doesn't count.

| What Phase 3 or 4 Found | Does This Conflict With the Echo? | What We're Doing About It |
|------------------------|----------------------------------|--------------------------|
| | Yes / No | Preserve Echo + document tension *or* No conflict — Echo stands |

---

## Calibration (if you have a prior retro)

How does this compare to last time? Is the team getting better at predicting, about the same, or slipping? One paragraph is fine.

---

## What Does the Echo Tell Us to Change?

The Echo is locked — but it should teach us something. Translate it into one concrete change: amend a skill, adjust a rubric criterion, shift a threshold. "We learned X" is the start; "therefore we're changing Y" is the finish.
```

---

## V-04 — Combined Axes: Role Sequence + Lifecycle Emphasis (Evidence Steward, weighted phase space)

**Hypothesis**: Assigning a named "Evidence Steward" role that explicitly owns each phase boundary, combined with giving Phase 3 (accuracy) substantially more structural space than other phases, drives higher C-07 and C-11 scores. The Steward role also models the team behavior the skill is trying to instill.

---

```
You are the Evidence Steward for topic {{topic}}. Your responsibility is to produce a durable, auditable record of how well this topic's signals predicted reality. You own the fidelity of this record — not its flattery.

Work through the five phases below in strict order. As Evidence Steward, you transition each phase only after its deliverable is complete. The Echo in Phase 1 is sealed before Phase 2 begins.

---

## Inputs

| Field | Value |
|-------|-------|
| Topic | {{topic}} |
| Signals gathered | {{signals}} |
| Post-ship outcomes | {{outcomes}} |
| Prior retro (optional) | {{prior_retro}} |
| AMEND scope (optional) | {{amend}} |

---

## Phase 1 — Echo Capture (LOCKED)

**Steward duty**: Before examining any signal data, record the single most unexpected finding from your initial surface read of this topic's history. This is your pre-analysis impression.

> **ECHO (LOCKED):** [One sentence. The genuinely unexpected thing. Sealed at this phase boundary.]

**Phase boundary**: Echo is now immutable. Proceed to Phase 2.

---

## Phase 2 — Signal Inventory (Steward: verify completeness)

List every artifact produced for this topic. One row per artifact. The Steward certifies that no known artifact is omitted.

| # | Namespace | Artifact Name | Date Produced | Prediction at Signal Time |
|---|-----------|---------------|---------------|--------------------------|
| | | | | |

*If AMEND scope is active, note it here and restrict to in-scope artifacts only.*

**Phase boundary**: Inventory complete. Proceed to Phase 3.

---

## Phase 3 — Accuracy Analysis (Steward: this phase receives the most space — be thorough)

This is the core of the retro. The Steward works through three layers:

### Layer A — Artifact-level accuracy

Grade each artifact against outcomes. Column header carries the formula and a worked example.

| Namespace | Artifact | Actual Outcome | Result (C/P/W) | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Revision Log Entry |
|-----------|----------|----------------|----------------|----------------------------------------------------------|-------------------|
| | | | | | *(blank, or note tension for Phase 5)* |

### Layer B — Namespace-level accuracy

For each namespace represented in the inventory, compute the namespace score using the same formula. Do not collapse namespaces into a single number.

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Reliability Tier |
|-----------|---|---|---|----------------------------------------------------------|-----------------|
| | | | | | Strong (≥80) / Adequate (50–79) / Weak (<50) |

### Layer C — Overall accuracy judgment

Aggregate the full signal set. State the ratio (e.g., 7C/2P/1W), the composite score (formula above applied to totals), and the overall tier. Identify the strongest and weakest namespace.

**Phase boundary**: Accuracy analysis complete. Proceed to Phase 4.

---

## Phase 4 — Gap Registry (Steward: actionability required)

The Steward identifies signal types that were absent and assigns a corrective action to each.

| Gap # | Missing Signal Type | Namespace | Counterfactual Impact | Corrective Action (Skill / Question / Threshold) |
|-------|--------------------|-----------|-----------------------|--------------------------------------------------|
| G-01 | | | | |

Generic entries ("should gather more") fail Steward standards. Each gap must specify namespace, signal type, and a concrete next action.

**Phase boundary**: Gap registry complete. Proceed to Phase 5.

---

## Phase 5 — Conflict Audit (Unconditional — Steward runs this regardless of perceived tension)

The Steward examines every Revision Log entry from Phase 3, Layer A. This audit runs whether or not entries were made.

**If Revision Log entries exist**: For each, document whether it conflicts with the Phase 1 Echo. If it does, record the tension and preserve the Echo unchanged.

**If Revision Log was empty**: Produce one explicit row: "No tension detected. Echo preserved as written."

| Audit # | Revision Log Entry | Conflict With Echo? | Disposition |
|---------|-------------------|---------------------|-------------|
| A-01 | | Yes / No | *Preserve Echo + tension note* or *No conflict* |

**Phase boundary**: Conflict audit complete. Record is sealed.

---

## Calibration (if prior retro provided)

The Steward compares this topic's accuracy profile to the prior retro. State whether prediction quality is improving, degrading, or stable, and identify the primary driver of the change.

| Metric | This Topic | Prior Retro | Trend |
|--------|-----------|-------------|-------|
| Overall Score | | | |
| Best Namespace | | | |
| Worst Namespace | | | |

---

## Echo Feedback

The locked Echo must produce a concrete artifact proposal. State what changes as a result.

| Locked Echo | Proposed Change | Type | Target |
|------------|-----------------|------|--------|
| *[repeat Echo verbatim]* | | Skill amendment / Rubric criterion / Threshold shift | *[artifact name]* |
```

---

## V-05 — Combined Axes: Output Format + Inertia Framing (Status-quo competitor as explicit foil)

**Hypothesis**: Framing the retro's gap analysis explicitly against a "no-retro" baseline — what the team would have concluded if they'd shipped and moved on without retrospecting — sharpens the actionability of C-06 and C-10 while also making the Echo's value concrete. The status-quo competitor is a structural section, not a rhetorical device.

---

```
You are running a calibration retrospective. The goal is to determine whether the signals gathered for this topic were worth gathering — and whether the team's future signal strategy should change as a result.

Work in the five phases below. Phase 1 is locked before Phase 2 begins. All phases produce tables. Phase 5 runs unconditionally.

---

## Inputs

- Topic: {{topic}}
- Signals (artifact names, dates, namespaces): {{signals}}
- Post-ship outcomes: {{outcomes}}
- Prior retro for calibration (if available): {{prior_retro}}
- AMEND scope restriction (if any): {{amend}}

---

## Phase 1 — ECHO (LOCKED)

Write the single most surprising finding from this retrospective. One sentence. Written before signal data is analyzed.

> **ECHO (LOCKED):** ___

This line does not change after Phase 1. Any later analysis that would change it goes into the Conflict Audit (Phase 5) instead.

---

## Phase 2 — Signal Inventory

Every artifact for this topic. One row per artifact. Zero omissions. (AMEND scope: restrict to in-scope artifacts only if provided.)

| # | Namespace | Artifact | Date | Prediction at Signal Time |
|---|-----------|----------|------|--------------------------|
| | | | | |

---

## Phase 3 — Accuracy Analysis

Grade each artifact. Use the formula in the column header throughout.

| Namespace | Artifact | Outcome | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Revision Flag |
|-----------|----------|---------|-------|--------------------------------------------------------|---------------|
| | | | | | *(blank or flag for Phase 5)* |

**Namespace accuracy breakdown** (do not skip):

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Tier |
|-----------|---|---|---|--------------------------------------------------------|------|
| | | | | | Strong / Adequate / Weak |

**Overall accuracy:** [ratio] → [score] → [tier]

---

## Phase 4 — Gap Analysis + Status-Quo Foil

Two-part phase. First, identify missing signals. Second, compare against the no-retro baseline.

### Part A — Gap Registry

| Gap # | Missing Signal Type | Namespace | What It Would Have Changed | Action: Skill / Question / Threshold |
|-------|--------------------|-----------|--------------------------|-----------------------------------------|
| G-01 | | | | |

### Part B — Status-Quo Foil

If the team had shipped without running this retro and moved on, what would they have concluded? Complete this table to make the retro's value explicit.

| Dimension | Without This Retro (Status Quo) | With This Retro | Delta |
|-----------|-------------------------------|-----------------|-------|
| Accuracy perception | *(what the team would have assumed)* | *(what the data shows)* | |
| Namespace blind spot | *(which namespace failures would stay invisible)* | *(what was surfaced)* | |
| Next-topic strategy | *(what signals would be skipped next time)* | *(what should be added)* | |

---

## Phase 5 — Conflict Audit (Unconditional)

Examine every Revision Flag from Phase 3. This phase runs whether flags exist or not.

| Flag Source | Phase 3/4 Finding | Conflict With ECHO (LOCKED)? | Disposition |
|------------|------------------|------------------------------|-------------|
| | | Yes / No | Preserve Echo + note tension *or* No conflict detected — Echo stands |

*If Phase 3 Revision Flag column was blank: produce one row: "No flags raised. Conflict audit complete. Echo preserved as written."*

---

## Calibration (if prior retro available)

Compare this topic's accuracy profile to the prior retro. Identify trend direction and primary driver.

| Metric | This Topic | Prior Retro | Trend |
|--------|-----------|-------------|-------|
| Overall Score | | | Improving / Stable / Degrading |
| Best Namespace | | | |
| Weakest Namespace | | | |

---

## Echo Feedback Loop

Translate the locked Echo into one concrete change to signal design. The status-quo foil from Phase 4B makes the cost of not changing visible.

| ECHO (LOCKED) | Proposed Change | Type | Target Artifact | Cost of Inaction (from Foil) |
|--------------|-----------------|------|-----------------|------------------------------|
| *[verbatim]* | | Skill / Rubric / Threshold | | *(what the status quo loses if this change isn't made)* |
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Structural Bet |
|-----------|-------------|----------------|-------------------|
| **V-01** | Role: forensic auditor | — | Audit role enforces phase locking by professional identity |
| **V-02** | Format: all-table, formula headers | — | Scorer can verify C-13/C-15/C-18 by column inspection alone |
| **V-03** | Register: conversational/facilitated | — | Lower barrier reduces C-01/C-03 omissions in team use |
| **V-04** | Role: Evidence Steward | Lifecycle: Phase 3 weighted | Named role + expanded accuracy layer drives C-07/C-11 depth |
| **V-05** | Format: structured tables | Inertia: status-quo foil | No-retro baseline makes Echo feedback (C-10) concrete and defensible |
