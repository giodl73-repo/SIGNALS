**scout-inertia R4 — 5 variations written** to `simulations/quest/variations/scout-inertia-variations-R4-2026-03-16.md`.

---

## Summary

| Variation | Axis | Key design decision |
|-----------|------|---------------------|
| **V-01** | A-05 only | Question-primed entry at all 4 critical tables; standard linear order; isolates formulation discipline |
| **V-02** | A-06 only | Explicit cognitive bridges at every section boundary in fail-first structure; bridge language names the specific output being carried forward and the specific constraint it creates |
| **V-03** | A-08 only | Purest fail-first: C-05 is the absolute primary gate, all section identity derives from FM evidence; no question-priming to isolate the ordering effect |
| **V-04** | A-05 + A-06 + A-08 | Fail-first spine with question-primed entry and explicit bridges; V-01 formulation + V-02 linkage + V-03 ordering in a linear structure |
| **V-05** | A-05 + A-06 + A-07 + A-08 | All four new criteria; two-pass segmented analysis forces A-07; fail-first within each pass; question-primed tables throughout; inter-pass bridge enforces ID carry-forward into synthesis |

**Notable structural patterns introduced in R4:**

1. **ACTOR-A / ACTOR-B as declared IDs** (V-05) — extends the R3 V-05 commitment-chain pattern to segmented analysis; synthesis ID citation is structurally required, not advisory.

2. **Sentence-then-table contradiction test** (V-01, V-04, V-05) — the A-05 formulation sentence creates a consistency check: a table cell that contradicts the sentence you just wrote is visible before it becomes a downstream dependency.

3. **Bridge as a hard constraint specification** (V-02, V-04, V-05) — transitions don't say "consider what you found"; they say "the person who experienced the FM-01 symptom is the actor — use that role name; if you cannot, your Section 1 triggers were not specific enough." The bridge names both the upstream product and the downstream cell it constrains.
y written. The detection burden shifts from the composite gate
to the moment of formation. Standard linear order (C-01 → C-02 → C-05 → C-04) is preserved to
isolate the axis.

---

You are running `scout-inertia`. One question: **why does inertia lose?**

Before filling any table, write the answer as a sentence. The table is a transcription, not a
composition. Vague entries reveal themselves when they contradict the sentence you already wrote.
Catch them at the sentence, not the cell.

---

### Section 1 — Workaround Identity

**Formulate first**: Name the exact tool or process teams use as a workaround. Write this sentence
before filling the table: "The workaround is [name], performed by [role — not department, not
'users'] using [tool], [frequency], producing [artifact]."

> _Sentence_: ___

*If you wrote "the team" or a department name in the role slot, stop and rewrite. The sentence
must name a role before the table receives anything.*

Now transcribe into the table:

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — not department: e.g., "PM", "DevOps engineer", "data analyst"] | |
| Frequency [e.g., "weekly before Monday standup", "per release cycle"] | |
| Output artifact | |

**A-04 — Role precision gate**: Read "Who performs it." If it contains "teams", "users",
"people", or a department name, rewrite it before continuing. Your sentence should have named a
role — if it did not, revise the sentence, then re-transcribe. Only proceed to Section 2 once
the cell names a role.

**Self-score C-01**:
- [ ] PASS — Workaround name, tool, role actor, frequency, and output artifact all present; sentence is consistent with table entries
- [ ] FAIL — Return and add specifics before Section 2

---

### Section 2 — Switching Cost Quantification

**Formulate first**: What does it cost the [role from Section 1] to abandon this workaround?
Write this sentence: "Switching costs the [role] approximately [N units] in migration time,
[N hours] in training, and [N sprint-days or headcount] in workflow disruption."

> _Sentence_: ___

*If you cannot fill in specific numbers, write "unknown — assuming ~[range]" in the sentence.
An explicit uncertainty is stronger than an omission. "High" is not a number and does not pass.*

Now transcribe into the table:

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis [comparable migration, analogy, assumption, or explicit uncertainty range] |
|-----------|--------------------------------------------------------|------|----------------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per [role from Section 1] | |
| Training | | hours per [role from Section 1] | |
| Workflow disruption | | sprint-days or people affected | |

**Inertia threat score**: HIGH *(default — the feature being compelling does not reduce inertia;
switching costs are still paid in full. Reduce only with documented evidence that this workaround
is already being abandoned independent of this feature.)*

**Self-score C-02**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range; sentence is consistent
- [ ] FAIL — Return and quantify

**Self-score C-03**:
- [ ] PASS — Inertia threat score stated as HIGH
- [ ] FAIL — Restore to HIGH

**Self-score R-03**:
- [ ] PASS — At least one Estimate cell names the role from Section 1 alongside the number
- [ ] FAIL — Add role label to at least one estimate

---

### Section 3 — Failure Mode Inventory

**Formulate first**: Name two specific scenarios where this workaround breaks. Write this
sentence: "The workaround fails when [trigger — specific input, volume, or event], causing
[user-visible symptom]; and when [trigger], causing [symptom]."

> _Sentence_: ___

*Both triggers must be specific enough that a developer could write a test for them. Both
symptoms must be observable without reading an error log. If your sentence contains "slow",
"error", or "difficult" without a threshold or observable effect, rewrite it.*

Now transcribe into the table:

| # | Trigger [specific input, volume threshold, or workflow event — not a general category] | What breaks | User-visible symptom [observable without a log] | Estimated frequency |
|---|----------------------------------------------------------------------------------------|-------------|------------------------------------------------|---------------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

**Self-score C-05**:
- [ ] PASS — At least 2 rows with specific trigger and observable user-visible symptom; sentence is consistent with table entries
- [ ] FAIL — Return and sharpen triggers and symptoms before Section 4

---

### Section 4 — Conditions Under Which Inertia Loses

**Formulate first**: Under what observable conditions does a specific team type abandon the
workaround? Write this sentence: "When [observable threshold] occurs, [specific team type —
not 'users'] switches because the workaround [what it can no longer do, citing the FM]."

> _Sentence_: ___

*The threshold must be falsifiable — a third party can confirm whether it was crossed. The team
type must name a role or team context, not "users" or "teams." The FM reference must trace to
Section 3.*

Now transcribe into the table:

| # | Observable trigger [falsifiable — a third party can confirm it] | Team type [specific role or team context — not "all users"] | Linked FM | Consequence if not reached |
|---|----------------------------------------------------------------|------------------------------------------------------------|-----------|---------------------------|
| DC-01 | Teams switch when... | | FM-__ | |
| DC-02 | Teams switch when... | | FM-__ | |
| DC-03 (optional) | | | | |

**Falsifiability check**: For each row — can a third party observe whether the trigger was
crossed? "When they need it" fails. "When FM-01 recurs three times in a sprint" passes.

**Self-score C-04**:
- [ ] PASS — At least 2 rows with falsifiable triggers; your formulation sentence is consistent with the table
- [ ] FAIL — Return and add observable thresholds

**Self-score R-01**:
- [ ] PASS — At least one DC row names a specific team type
- [ ] FAIL — Scope at least one condition to a team type

**Self-score R-02**:
- [ ] PASS — Every actor in Sections 1 and 4 is a role, not a department
- [ ] FAIL — Correct vague labels

---

### Section 5 — Composite Gate

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-01 Workaround identity | 1 | PASS / FAIL | Section 1 |
| C-02 Switching costs quantified | 2 | PASS / FAIL | Section 2 |
| C-03 Inertia threat HIGH | 2 | PASS / FAIL | Section 2 |
| C-05 Failure modes with specific trigger + symptom | 3 | PASS / FAIL | Section 3 |
| C-04 Why inertia loses — falsifiable conditions | 4 | PASS / FAIL | Section 4 |
| R-01 Trigger scoped to team type | 4 | PASS / FAIL | Section 4 |
| R-02 Role-level precision | 1, 4 | PASS / FAIL | Section 1 or 4 |
| R-03 At least one cost cited to role | 2 | PASS / FAIL | Section 2 |
| **All essential (C-01–C-05) pass?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: Completion blocker. Any essential FAIL requires returning to the named
section and revising. Sentence formulation mismatches at any section are an early warning sign
for the corresponding criterion — catch them there, not here.

---

*End V-01*

---

## V-02 — Cognitive Linkage: A-06 as sole new axis

**Variation axis**: A-06 — explicit cognitive linkage at every section boundary.

**Hypothesis**: Fail-first ordering (from R3 V-03) establishes the right sequence but leaves
analysts free to treat sections as independent checklists: start Section 2, fill the cells,
ignore what Section 1 produced. Explicit cognitive bridges at every transition — naming what the
prior section produced and exactly how it constrains the next section's entries — should prevent
independent-checklist cognition without requiring question-priming. Isolating A-06 tests whether
named inter-section dependency enforcement alone closes the coherence gap.

---

You are running `scout-inertia`. One question: **why does inertia lose?**

The sections of this analysis are not independent checklists. Each section produces evidence that
constrains the next. Read each transition instruction carefully — it tells you exactly what you
learned and how to carry it forward.

---

### Section 1 — Failure Mode Discovery

Identify where the current workaround breaks. Map failures before mapping the workaround. The
workaround identity, actor, and cost all follow from where the tool breaks.

| # | Trigger [specific input, volume threshold, or workflow event — not a general category] | What breaks | User-visible symptom [observable without a log] | Estimated frequency |
|---|----------------------------------------------------------------------------------------|-------------|------------------------------------------------|---------------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

**Column contracts**:
- *Trigger*: Specific enough for a developer to write a test. "Large files" fails. "Files exceeding 10MB" passes.
- *User-visible symptom*: Observable without reading a log. "Internal error" fails. "Export dialog closes without producing a file" passes.

**Self-score C-05** *(primary gate — all sections depend on this passing)*:
- [ ] PASS — At least 2 rows with specific trigger and observable user-visible symptom
- [ ] FAIL — Do not continue. Vague triggers produce vague workaround identity in Section 2.

---

**Bridge 1 → 2**: The Section 1 symptom column reveals who was present when the workaround
failed — that person is the actor. The Section 1 trigger column defines what input or volume
threshold broke the tool — that boundary gives the workaround its precise name. Carry these
forward: (a) the actor is the person whose screen showed the symptom; (b) the tool name or
process description should reflect the thresholds you just documented. If Section 1 did not
surface a role, the triggers are not specific enough — the symptom line reveals the actor.

---

### Section 2 — Workaround Identity

Declare the workaround. The failure evidence from Section 1 constrains every cell.

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — the person who experienced the FM-01 symptom, not a department] | |
| Frequency | |
| Output artifact | |

**A-04 — Role precision gate**: Read "Who performs it." If it contains "teams", "users",
"people", or a department name, check Section 1's symptom column — the person who experienced
the symptom is the actor. Rewrite before continuing to Section 3.

**Self-score C-01**:
- [ ] PASS — Workaround name, tool, role actor, frequency, and output artifact all present
- [ ] FAIL — Return here. If actor is blocked, return to Section 1 and sharpen the symptom column.

---

**Bridge 2 → 3**: You named the actor and the tool. Switching cost is the cost to this specific
actor of abandoning this specific tool. Use the role from Section 2 as the Unit anchor for every
estimate. Use the tool category from Section 2 to calibrate the time estimate — migrating from
a spreadsheet differs from migrating from a custom CLI script. A cost with no role anchor is a
cost for nobody; a cost with no tool calibration is a cost for nothing.

---

### Section 3 — Switching Cost Quantification

Quantify switching costs for the role declared in Section 2. Cover at least two of the three
dimensions. Every estimate must be a number or range — qualitative labels do not pass.

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis [comparable migration, analogy, assumption, or explicit uncertainty] |
|-----------|--------------------------------------------------------|------|----------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per [role from Section 2] | |
| Training | | hours per [role from Section 2] | |
| Workflow disruption | | sprint-days or people affected | |

**Inertia threat score**: HIGH *(default — a compelling feature does not reduce inertia; switching
costs are paid in full before the value is received. Reduce only with documented evidence that this
workaround is being actively abandoned independent of this feature.)*

**Self-score C-02**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score C-03**:
- [ ] PASS — Inertia threat score stated as HIGH
- [ ] FAIL — Restore to HIGH

**Self-score R-03**:
- [ ] PASS — At least one Estimate row names the Section 2 role alongside the number, and at least one Basis carries an anchor
- [ ] FAIL — Add role label and basis anchor

---

**Bridge 3 → 4**: You have failure modes (Section 1) and switching costs (Section 3). Defeat
conditions explain why a team pays these costs. The mechanism: a failure mode recurs often enough,
or causes severe enough re-work, that switching costs become the cheaper option at a specific
threshold. For each DC row, identify the FM that makes the workaround untenable at that threshold.
A defeat condition without an FM root cause is a prediction without an explanation — it may be
true but it is not grounded in evidence you have documented.

---

### Section 4 — Conditions Under Which Inertia Loses

Map the defeat conditions. Every row must trace to a failure mode from Section 1 — the FM is the
mechanism; the DC is the observable threshold at which the mechanism crosses the switching cost.

| # | Observable trigger [falsifiable — a third party can confirm it] | Team type [specific role or team context — not "all users"] | Linked FM | Consequence if not reached |
|---|----------------------------------------------------------------|------------------------------------------------------------|-----------|---------------------------|
| DC-01 | Teams switch when... | | FM-__ | |
| DC-02 | Teams switch when... | | FM-__ | |
| DC-03 (optional) | | | | |

**Falsifiability check**: Can a third party confirm whether each trigger was crossed? "When they
need it" fails. "When FM-01 recurs twice in a single sprint" passes. Defeat conditions with no
FM link are hypotheses; defeat conditions linked to FM rows are evidence-grounded claims.

**Self-score C-04**:
- [ ] PASS — At least 2 rows with falsifiable triggers, each traceable to a Section 1 FM row
- [ ] FAIL — Return and ground conditions in failure evidence

**Self-score R-01**:
- [ ] PASS — At least one DC row names a specific team type
- [ ] FAIL — Scope at least one condition to a team type

**Self-score R-02**:
- [ ] PASS — Every actor in Sections 2 and 4 is a role, not a department
- [ ] FAIL — Correct vague labels

---

### Section 5 — Composite Gate

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-05 Failure modes (primary gate) | 1 | PASS / FAIL | Section 1 |
| C-01 Workaround identity | 2 | PASS / FAIL | Section 2 (or 1 if actor blocked) |
| C-02 Switching costs quantified | 3 | PASS / FAIL | Section 3 |
| C-03 Inertia threat HIGH | 3 | PASS / FAIL | Section 3 |
| C-04 Why inertia loses — falsifiable conditions | 4 | PASS / FAIL | Section 4 |
| R-01 Trigger scoped to team type | 4 | PASS / FAIL | Section 4 |
| R-02 Role-level precision | 2, 4 | PASS / FAIL | Section 2 or 4 |
| R-03 At least one cost cited to role | 3 | PASS / FAIL | Section 3 |
| **All essential (C-01–C-05) pass?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: Completion blocker. Section 1 (C-05) cascades — a failure there
propagates into all subsequent sections via the bridges. Begin all repairs at the earliest failing
section, then re-check downstream entries for consistency with the bridge constraints.

---

*End V-02*

---

## V-03 — Fail-First: A-08 as sole new axis

**Variation axis**: A-08 — failure modes section precedes workaround identity, in purest form.

**Hypothesis**: R3 V-03 introduced fail-first ordering but coupled it with question-priming and
an adversarial C-01 gate in the same variation, making attribution ambiguous. R4 V-03 isolates
A-08: standard table format (no question-priming), no segmentation, no adversarial structure —
but C-05 is the absolute primary gate and the only path to Section 2 requires specific failure
evidence. The test: does ordering alone, without formulation discipline or explicit bridges,
produce the epistemological chain? Failure modes before workaround identity means the actor and
tool are inferred from breakdown evidence, not assumed from prior mental model.

---

You are running `scout-inertia`. One question: **why does inertia lose?**

**This analysis is sequenced by the evidence it requires.** You cannot know precisely what the
workaround is until you know where it breaks. You cannot know who performs it until you know
who the workaround fails. You cannot know when inertia loses until you have named the specific
conditions that make the workaround untenable. Section 1 is mandatory; nothing else opens
until it passes.

---

### Section 1 — Failure Mode Discovery

Identify where the current workaround breaks. Two rows minimum. Do not fill in the workaround
identity yet — the failure evidence shapes that declaration.

| # | Trigger [specific input, volume threshold, or workflow event — not a general category] | What breaks | User-visible symptom [observable without reading a log] | Estimated frequency |
|---|----------------------------------------------------------------------------------------|-------------|--------------------------------------------------------|---------------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

**Column contracts**:
- *Trigger*: A developer must be able to write an automated test for this trigger. "Large files" fails. "Files exceeding 10MB" passes.
- *User-visible symptom*: The user observes this directly without reading a log. "Internal error in log" fails. "Export dialog closes without producing a file" passes.
- *"Manual is slow"* in any cell fails both columns.

**Self-score C-05** *(primary gate — this section must pass before any other section is entered)*:
- [ ] PASS — At least 2 rows with specific trigger and observable user-visible symptom. Proceed to Section 2.
- [ ] FAIL — Do not continue. Return to this table and sharpen triggers and symptoms. If you cannot identify specific failure scenarios, you have not identified the right workaround.

---

### Section 2 — Workaround Identity

Declare the workaround. The failure mode evidence from Section 1 is your evidence base: the actor
is the person who experienced the symptom; the tool name should reflect the threshold at which it
failed.

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — the person who experienced the FM-01 symptom, not a department] | |
| Frequency | |
| Output artifact | |

**A-04 — Role precision gate**: Read "Who performs it." If it contains "teams", "users", "people",
or a department name, check Section 1's symptom column — the person affected by the failure is
the actor. Rewrite as a role before entering Section 3. Do not proceed with a vague actor.

**Self-score C-01**:
- [ ] PASS — Workaround name, tool, role actor, frequency, and output artifact all present
- [ ] FAIL — Return here. If actor is blocked, return to Section 1 and sharpen the symptom column until the actor's role emerges.

---

### Section 3 — Switching Cost Quantification

Quantify switching costs for the role declared in Section 2. Cover at least two of the three
dimensions. Each estimate must carry a number or range — "high" and "low" do not pass.

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis [comparable migration, analogy, assumption, or explicit uncertainty range] |
|-----------|--------------------------------------------------------|------|----------------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per [role from Section 2] | |
| Training | | hours per [role from Section 2] | |
| Workflow disruption | | sprint-days or people affected | |

**Inertia threat score**: HIGH *(default — the feature being compelling does not reduce inertia;
switching costs are still paid before any value is received. Reduce only with documented evidence
that this workaround is being actively abandoned independent of this feature.)*

**Self-score C-02**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score C-03**:
- [ ] PASS — Inertia threat score stated as HIGH
- [ ] FAIL — Restore to HIGH

**Self-score R-03**:
- [ ] PASS — At least one Estimate row names the role alongside the number, and at least one Basis cell carries an anchor
- [ ] FAIL — Add role label and basis anchor

---

### Section 4 — Conditions Under Which Inertia Loses

Map observable defeat conditions. Each defeat condition must link to a failure mode from Section 1:
the FM is the mechanism by which the workaround becomes untenable; the DC is the threshold at
which that mechanism crosses the switching cost. Defeat conditions without FM links are predictions;
defeat conditions with FM links are evidence-grounded claims.

| # | Observable trigger [falsifiable — a third party can confirm it] | Team type [specific role or team context — not "all users"] | Linked FM from Section 1 | Consequence if not reached |
|---|----------------------------------------------------------------|------------------------------------------------------------|--------------------------|---------------------------|
| DC-01 | Teams switch when... | | FM-__ | |
| DC-02 | Teams switch when... | | FM-__ | |
| DC-03 (optional) | | | | |

**Falsifiability check**: For each row — can a third party confirm whether the trigger was
crossed? "When they see value" fails. "When FM-01 recurs twice in one sprint" passes.

**Self-score C-04**:
- [ ] PASS — At least 2 rows with falsifiable triggers; each traces to an FM in Section 1
- [ ] FAIL — Return and ground conditions in observable failure evidence

**Self-score R-01**:
- [ ] PASS — At least one DC row names a specific team type or role context
- [ ] FAIL — Scope at least one condition to a team type

**Self-score R-02**:
- [ ] PASS — Every actor in Sections 2 and 4 is a role, not a department
- [ ] FAIL — Correct vague labels

---

### Section 5 — Composite Gate

*C-05 is listed first — it is the primary gate that all subsequent sections depend on.*

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-05 Failure modes — primary gate | **1** | PASS / FAIL | **Section 1** |
| C-01 Workaround identity | 2 | PASS / FAIL | Section 2 (or 1 if actor blocked) |
| C-02 Switching costs quantified | 3 | PASS / FAIL | Section 3 |
| C-03 Inertia threat HIGH | 3 | PASS / FAIL | Section 3 |
| C-04 Why inertia loses — falsifiable conditions | 4 | PASS / FAIL | Section 4 |
| R-01 Trigger scoped to team type | 4 | PASS / FAIL | Section 4 |
| R-02 Role-level precision | 2, 4 | PASS / FAIL | Section 2 or 4 |
| R-03 At least one cost cited to role | 3 | PASS / FAIL | Section 3 |
| **All essential (C-01–C-05) pass?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: Completion blocker. Section 1 cascades forward — a failure there
propagates into workaround identity, cost, and defeat conditions. Begin all repairs at the
earliest failing section.

---

*End V-03*

---

## V-04 — Combination: A-05 + A-06 + A-08

**Variation axes**: A-08 (fail-first) as the structural spine + A-05 (question-primed entry) at
every table + A-06 (cognitive linkage) at every section boundary.

**Hypothesis**: A-08 alone establishes ordering but leaves analysts free to treat each section
as a fresh start. A-05 alone formulates each entry but doesn't connect sections. A-06 alone names
dependencies but doesn't force formulation. Together: A-05 commits the analyst to a specific claim
before entering each table; A-06 uses the formulated claims from one section as named inputs to the
next; A-08 ensures the ordering makes FM quality structurally determinative. The combination should
produce the highest within-section precision and strongest cross-section coherence in a linear
structure, without requiring segmentation.

---

You are running `scout-inertia`. One question: **why does inertia lose?**

**Order**: Failure modes first. Workaround identity second. Costs third. Defeat conditions last.
Each section produces evidence the next requires.

**Formulate before entering**: Each section opens with a sentence prompt. Write the sentence.
Then fill the table. Weak entries — vague actors, "high"/"low" costs, non-falsifiable triggers —
become visible when they contradict the sentence you already wrote.

**Bridges**: Each transition names what you just produced and exactly how it constrains what comes
next. Follow the bridges.

---

### Section 1 — Failure Mode Discovery

**Formulate**: Name two specific scenarios where the workaround fails. Write:
"The workaround fails when [trigger — specific input, volume, or event], causing
[user-visible symptom]; and when [trigger], causing [symptom]."

> _Sentence_: ___

*Both triggers must be specific enough for a developer to write a test. Both symptoms must be
observable without a log. If your sentence contains "slow", "difficult", or "error" without a
threshold or observable effect, rewrite it before filling the table.*

| # | Trigger [specific input, volume threshold, or workflow event] | What breaks | User-visible symptom [observable without a log] | Estimated frequency |
|---|---------------------------------------------------------------|-------------|------------------------------------------------|---------------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

**Self-score C-05** *(primary gate)*:
- [ ] PASS — At least 2 rows with specific trigger and observable symptom; your sentence is consistent with the table entries
- [ ] FAIL — Do not continue. Revise triggers and symptoms until a valid sentence can be written.

---

**Bridge 1 → 2**: You have named what breaks and who observes it. Carry these forward:
**(a) Actor**: The person whose screen showed the symptom is the workaround performer — use that
role name in "Who performs it"; a department name means the trigger was not specific enough.
**(b) Tool identity**: The tool is named by its failure threshold — a spreadsheet that silently
truncates rows is not just "a spreadsheet"; name the behavior. Use (a) and (b) to fill Section 2
with evidence-grounded entries, not prior assumptions.

---

### Section 2 — Workaround Identity

**Formulate**: Using the failure evidence from Section 1, declare the workaround. Write:
"The workaround is [name reflecting the FM threshold], performed by [role — the person from the
FM-01 symptom] using [tool], [frequency], producing [artifact]."

> _Sentence_: ___

*If your sentence says "the team" or a department name, return to Section 1 and identify whose
screen showed the symptom. The FM symptom column reveals the actor.*

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — carry from Section 1 symptom evidence, not from assumption] | |
| Frequency | |
| Output artifact | |

**A-04 — Role precision gate**: Read "Who performs it." If it contains "teams", "users",
"people", or a department name, check Section 1's symptom column and rewrite. Your formulation
sentence should name a role — if it doesn't, revise the sentence, then re-transcribe.

**Self-score C-01**:
- [ ] PASS — Workaround name, tool, role actor, frequency, and output artifact all present; sentence matches table
- [ ] FAIL — Return here. If actor blocked, return to Section 1 and sharpen symptom column.

---

**Bridge 2 → 3**: You named the actor and the tool. Switching cost is the cost to this actor
of abandoning this tool. Use:
**(a) Role anchor**: Every Unit cell must name the Section 2 role — a cost without a role is a
cost for nobody.
**(b) Tool calibration**: The tool type bounds the time estimate — spreadsheet-to-SaaS migrations
differ from custom-script migrations; use the tool category from Section 2 to set the order of
magnitude.
A sentence about cost that does not reference the Section 2 role is not about this workaround.

---

### Section 3 — Switching Cost Quantification

**Formulate**: State what it costs the [role from Section 2] to switch away from [tool from
Section 2]. Write: "Switching costs the [role] approximately [N units] to migrate, [N hours]
training, and [N sprint-days or headcount] disruption."

> _Sentence_: ___

*If you cannot fill in numbers, write "unknown — assuming ~[range]" explicitly. "High" is not
a number.*

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis [comparable migration, analogy, assumption, or explicit uncertainty] |
|-----------|--------------------------------------------------------|------|----------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per [role from Section 2] | |
| Training | | hours per [role from Section 2] | |
| Workflow disruption | | sprint-days or people affected | |

**Inertia threat score**: HIGH *(default — the feature being compelling does not reduce inertia;
switching costs are paid in full before any value arrives)*

**Self-score C-02**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range; sentence is consistent
- [ ] FAIL — Return and quantify

**Self-score C-03**:
- [ ] PASS — Inertia threat score stated as HIGH
- [ ] FAIL — Restore to HIGH

**Self-score R-03**:
- [ ] PASS — At least one Estimate row names the Section 2 role alongside the number
- [ ] FAIL — Add role label

---

**Bridge 3 → 4**: You have failure modes (Section 1) and switching costs (Section 3). Defeat
conditions explain why a team pays these costs. The mechanism: the FM recurs often enough, or
causes enough re-work, that the switching cost becomes the cheaper option at a specific threshold.
For each DC row:
**(a) FM link**: Identify the failure mode from Section 1 that makes the workaround untenable
at the defeat threshold. A DC with no FM link is a prediction without a mechanism.
**(b) Team type**: The team type experiencing the FM determines who switches first — use the
role from the Section 1 symptom column, or a closely related team type, not "users."
A defeat condition inconsistent with your Section 1 failures has no evidence base.

---

### Section 4 — Conditions Under Which Inertia Loses

**Formulate**: State when a specific team type stops tolerating the workaround. Write:
"When [observable threshold] occurs, [specific team type — from Section 1 evidence] switches
because [the specific FM that becomes untenable at that threshold]."

> _Sentence_: ___

*The threshold must be falsifiable — a third party can confirm it was crossed. The FM must
reference a row from Section 1. "When they see the value" fails on both counts.*

| # | Observable trigger [falsifiable — a third party can confirm it] | Team type [specific — not "all users"] | Linked FM | Consequence if not reached |
|---|----------------------------------------------------------------|----------------------------------------|-----------|---------------------------|
| DC-01 | Teams switch when... | | FM-__ | |
| DC-02 | Teams switch when... | | FM-__ | |
| DC-03 (optional) | | | | |

**Self-score C-04**:
- [ ] PASS — At least 2 rows with falsifiable triggers; each traces to a Section 1 FM; sentence is consistent
- [ ] FAIL — Return and ground in observable failure evidence

**Self-score R-01**:
- [ ] PASS — At least one DC row names a specific team type
- [ ] FAIL — Scope at least one condition

**Self-score R-02**:
- [ ] PASS — Every actor in Sections 2 and 4 is a role, not a department
- [ ] FAIL — Correct vague labels

---

### Section 5 — Composite Gate

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-05 Failure modes (primary gate) | **1** | PASS / FAIL | **Section 1** |
| C-01 Workaround identity | 2 | PASS / FAIL | Section 2 (or 1) |
| C-02 Switching costs quantified | 3 | PASS / FAIL | Section 3 |
| C-03 Inertia threat HIGH | 3 | PASS / FAIL | Section 3 |
| C-04 Why inertia loses — falsifiable conditions | 4 | PASS / FAIL | Section 4 |
| R-01 Trigger scoped to team type | 4 | PASS / FAIL | Section 4 |
| R-02 Role-level precision | 2, 4 | PASS / FAIL | Section 2 or 4 |
| R-03 At least one cost cited to role | 3 | PASS / FAIL | Section 3 |
| **All essential (C-01–C-05) pass?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: Completion blocker. Section 1 is the primary gate; its cascade is
encoded in Bridges 1→2, 2→3, and 3→4. A repair at Section 1 requires re-checking all downstream
entries for consistency with the updated failure evidence. Sentence formulation mismatches at any
section are the cheapest place to catch problems — the composite gate is the last resort.

---

*End V-04*

---

## V-05 — Full Integration: A-05 + A-06 + A-07 + A-08 with segmented analysis

**Variation axes**: All four new aspirationals in a segmented two-pass analysis.

**Hypothesis**: A-05, A-06, and A-08 were each sourced from different R3 variations (V-01, V-03,
V-03 respectively) and A-07 from V-02. No single R3 variation satisfied all four. V-05 tests
whether all four can coexist in one coherent structure: A-08 governs ordering within each pass
(FM first); A-05 governs entry into each critical table (question-primed); A-06 governs all
section and inter-pass transitions (explicit cognitive bridges); A-07 governs synthesis (ID
citation mandatory). The segmented structure makes A-07 structurally necessary rather than
advisory — the synthesis section cannot produce a team-scoped claim without referencing segment
IDs. The prediction: A-07 ID citation in synthesis should make R-01 unreachable as a failure,
as in R3 V-02.

---

You are running `scout-inertia`. One question: **why does inertia lose?**

This analysis runs in two passes — one per team type — then synthesizes into a single answer.
Segmentation reveals the adoption sequence; synthesis answers the central question.

**Order within each pass**: Failure modes first. Workaround identity second. Costs third.
Defeat conditions last. The failures reveal the actor; the actor anchors the costs; the costs
explain why defeat conditions are eventually paid.

**Formulate before entering**: Each critical table is preceded by a sentence prompt. Write the
sentence. Then fill the table. Contradictions between the sentence and the table reveal weak
entries at the cheapest correction point.

**Bridges**: Each transition and each pass boundary carries an explicit constraint instruction.
Follow them.

---

### Step 0 — Name the two team types

Before starting, identify the two team types most relevant to this feature.

- **Primary team type** (highest switching friction — most likely to stay with workaround): ___
- **Secondary team type** (lowest switching friction — most likely to adopt first): ___

*Both passes analyze the same or closely related workaround; if the two team types use
fundamentally different workarounds, note the divergence and document the shared root.*

---

## PASS A — Primary team type: [fill from Step 0]

---

### A1 — Failure Mode Discovery (Pass A)

**Formulate**: Name two specific scenarios where the workaround fails for the primary team type.
Write: "For [Primary team type], the workaround fails when [trigger], causing [symptom]; and
when [trigger], causing [symptom]."

> _Sentence_: ___

*Both triggers specific enough for a developer to write a test. Both symptoms observable without
a log. Rewrite if the sentence contains "slow" or "difficult" without a threshold.*

| # | Trigger [specific input, volume threshold, or workflow event] | What breaks | User-visible symptom [observable without a log] | Estimated frequency |
|---|---------------------------------------------------------------|-------------|------------------------------------------------|---------------------|
| FM-A01 | | | | |
| FM-A02 | | | | |
| FM-A03 (optional) | | | | |

**Self-score C-05 (Pass A)**:
- [ ] PASS — At least 2 rows with specific trigger and observable symptom; sentence consistent
- [ ] FAIL — Do not enter A2. Sharpen until sentence can be written.

---

**Bridge A1 → A2**: The symptom column reveals who experiences the failure — that is the actor
for Pass A. The trigger column defines the tool's breaking point — that bounds the workaround's
name. Carry the actor from the symptom column and the threshold from the trigger column into A2.
A vague actor in A2 means A1 triggers were not specific enough.

---

### A2 — Workaround Identity (Pass A)

**Formulate**: Using A1 failure evidence, declare the workaround for Pass A. Write:
"For [Primary team type], the workaround is [name], performed by [role — from A1 symptom] using
[tool], [frequency], producing [artifact]."

> _Sentence_: ___

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [ACTOR-A — role from A1 symptom evidence, not a department] | |
| Frequency for this team type | |
| Output artifact | |

**A-04 gate (Pass A)**: If "Who performs it" contains "teams", "users", "people", or a
department name, return to A1 symptom column and rewrite. Label the role as **ACTOR-A** — this
ID will be referenced throughout Pass A.

**Self-score C-01 (Pass A)**:
- [ ] PASS — Workaround name, tool, ACTOR-A, frequency, and output artifact all present
- [ ] FAIL — Return; if actor blocked, sharpen A1 symptom column

---

**Bridge A2 → A3**: ACTOR-A is declared. Every cost estimate in A3 is for ACTOR-A. The tool
category from A2 sets the order of magnitude for migration time. Do not estimate costs in the
abstract — anchor them to ACTOR-A and the specific tool.

---

### A3 — Switching Costs (Pass A)

**Formulate**: State the switching cost for ACTOR-A. Write: "Switching costs ACTOR-A
approximately [N units] to migrate, [N hours] training, and [N units] disruption."

> _Sentence_: ___

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis [comparable migration, analogy, assumption, or uncertainty range] |
|-----------|--------------------------------------------------------|------|-------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per ACTOR-A | |
| Training | | hours per ACTOR-A | |
| Workflow disruption | | sprint-days or people affected | |

**Self-score C-02 (Pass A)**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score R-03 (Pass A)**:
- [ ] PASS — At least one estimate names ACTOR-A alongside the number, with at least one Basis anchor
- [ ] FAIL — Add role label and basis anchor

---

**Bridge A3 → A4**: You have failure modes (A1) and switching costs (A3) for ACTOR-A. Defeat
conditions explain when ACTOR-A's team pays these costs. The FM recurs often enough, or causes
enough re-work, that switching becomes cheaper than tolerating. For each DC-A row: link the
trigger to an A1 FM row; scope the team type to ACTOR-A's context. Label each defeat condition
as **DC-A01**, **DC-A02**, etc. — these IDs will be cited in synthesis.

---

### A4 — Defeat Conditions (Pass A)

**Formulate**: When does the primary team type stop tolerating the workaround? Write:
"ACTOR-A's team switches when [observable threshold], because [FM-A0X] makes the workaround
untenable at that scale."

> _Sentence_: ___

| # | Observable trigger [falsifiable] | Team type [specific — ACTOR-A's context] | Linked FM | Consequence if not reached |
|---|----------------------------------|------------------------------------------|-----------|---------------------------|
| DC-A01 | Teams switch when... | | FM-A__ | |
| DC-A02 | Teams switch when... | | FM-A__ | |
| DC-A03 (optional) | | | | |

**Self-score C-04 (Pass A)** and **R-01 (Pass A)**:
- [ ] C-04 PASS — At least 2 falsifiable triggers, each tracing to an A1 FM row
- [ ] R-01 PASS — At least one DC-A row names ACTOR-A's team type specifically
- [ ] FAIL on either — Return and ground in failure evidence

---

**Bridge Pass A → Pass B**: You have ACTOR-A, FM-A01/FM-A02, DC-A01/DC-A02 declared and
labeled. Pass B replicates this structure for the secondary team type. Where the secondary team
type shares workaround mechanics, note it — the divergences in FM triggers and DC thresholds
between Pass A and Pass B will drive synthesis. Label all Pass B artifacts with B IDs.

---

## PASS B — Secondary team type: [fill from Step 0]

---

### B1 — Failure Mode Discovery (Pass B)

**Formulate**: Name two specific failure scenarios for the secondary team type. Write:
"For [Secondary team type], the workaround fails when [trigger], causing [symptom]; and when
[trigger], causing [symptom]."

> _Sentence_: ___

| # | Trigger [specific input, volume threshold, or workflow event] | What breaks | User-visible symptom [observable without a log] | Estimated frequency |
|---|---------------------------------------------------------------|-------------|------------------------------------------------|---------------------|
| FM-B01 | | | | |
| FM-B02 | | | | |
| FM-B03 (optional) | | | | |

**Self-score C-05 (Pass B)**:
- [ ] PASS — At least 2 rows with specific trigger and observable symptom; sentence consistent
- [ ] FAIL — Do not enter B2. Sharpen until sentence can be written.

---

**Bridge B1 → B2**: Same logic as A1 → A2. The symptom column reveals ACTOR-B. The trigger
column bounds the tool description. Carry both into B2. Label the role as **ACTOR-B**.

---

### B2 — Workaround Identity (Pass B)

**Formulate**: Declare the workaround for the secondary team type. Write:
"For [Secondary team type], the workaround is [name], performed by [ACTOR-B — role from B1
symptom] using [tool], [frequency], producing [artifact]."

> _Sentence_: ___

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [ACTOR-B — role from B1 symptom evidence] | |
| Frequency for this team type | |
| Output artifact | |

**A-04 gate (Pass B)**: Same rule as Pass A. Label the role as ACTOR-B.

**Self-score C-01 (Pass B)**:
- [ ] PASS — All fields present with ACTOR-B labeled
- [ ] FAIL — Return; sharpen B1 symptom column if actor blocked

---

**Bridge B2 → B3**: ACTOR-B declared. All B3 cost estimates are for ACTOR-B.

---

### B3 — Switching Costs (Pass B)

**Formulate**: State the switching cost for ACTOR-B. Write: "Switching costs ACTOR-B
approximately [N units] to migrate, [N hours] training, and [N units] disruption."

> _Sentence_: ___

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis |
|-----------|--------------------------------------------------------|------|-------|
| Time to migrate and ramp | | hours or days per ACTOR-B | |
| Training | | hours per ACTOR-B | |
| Workflow disruption | | sprint-days or people affected | |

**Self-score C-02 (Pass B)**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score R-03 (Pass B)**:
- [ ] PASS — At least one estimate names ACTOR-B alongside the number
- [ ] FAIL — Add role label

---

**Bridge B3 → B4**: You have FM-B rows and B3 costs for ACTOR-B. Label defeat conditions as
DC-B01, DC-B02, etc. These IDs are required in synthesis.

---

### B4 — Defeat Conditions (Pass B)

**Formulate**: When does the secondary team type switch? Write:
"ACTOR-B's team switches when [observable threshold], because [FM-B0X] makes the workaround
untenable."

> _Sentence_: ___

| # | Observable trigger [falsifiable] | Team type [ACTOR-B's context] | Linked FM | Consequence if not reached |
|---|----------------------------------|-------------------------------|-----------|---------------------------|
| DC-B01 | Teams switch when... | | FM-B__ | |
| DC-B02 | Teams switch when... | | FM-B__ | |
| DC-B03 (optional) | | | | |

**Self-score C-04 (Pass B)** and **R-01 (Pass B)**:
- [ ] C-04 PASS — At least 2 falsifiable triggers, each tracing to a B1 FM row
- [ ] R-01 PASS — At least one DC-B row names ACTOR-B's team type specifically
- [ ] FAIL on either — Return and ground in failure evidence

---

**Bridge Passes → Synthesis**: You have FM-A, DC-A, FM-B, DC-B all labeled with IDs. Synthesis
must cite these IDs directly — do not summarize in free prose. Identify: (a) whether the two
team types share a common trigger or diverge; (b) which team type is likely to reach its defeat
threshold first and why; (c) the combined "why inertia loses" statement grounded in at least two
FM citations.

---

## Inertia Threat Score

**Inertia threat score**: HIGH *(default across both team types — compelling features do not
reduce inertia; switching costs are still paid. Reduce only with documented evidence that
the workaround is being actively abandoned independent of this feature.)*

**Self-score C-03**:
- [ ] PASS — Score stated as HIGH for both team types
- [ ] FAIL — Restore to HIGH

---

## Synthesis — Why Inertia Loses

**This section is mandatory. Do not skip it.**

*Requirements for this section:*
- Reference at least two FM IDs (e.g., FM-A01, FM-B02) and at least two DC IDs (e.g., DC-A01,
  DC-B01) — free-prose summaries without IDs do not pass A-07.
- Produce at least two team-scoped, falsifiable conditions that synthesize across both passes.
- State which team type reaches the defeat threshold first and identify the FM that drives it.

| # | Synthesized defeat condition [must cite FM and DC IDs from both passes] | Team type that reaches this threshold first | Evidence anchor |
|---|-------------------------------------------------------------------------|---------------------------------------------|-----------------|
| SDC-01 | | | FM-__ / DC-__ |
| SDC-02 | | | FM-__ / DC-__ |

**Synthesis self-score C-04** *(primary C-04 gate — segment-level C-04 passes are necessary
but not sufficient; this gate is the definitive C-04 check)*:
- [ ] PASS — At least 2 SDC rows cite specific FM and DC IDs; conditions are falsifiable and team-scoped
- [ ] FAIL — Return to the relevant pass and sharpen FM or DC entries, then re-synthesize

**Synthesis self-score R-01**:
- [ ] PASS — Both SDC rows name a specific team type (structurally satisfied if SDC rows cite DC-A and DC-B IDs)
- [ ] FAIL — Scope SDC rows to team type using Pass A and B labels

---

## Composite Gate

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-05 Pass A failure modes | A1 | PASS / FAIL | A1 |
| C-05 Pass B failure modes | B1 | PASS / FAIL | B1 |
| C-01 Pass A workaround identity | A2 | PASS / FAIL | A2 (or A1) |
| C-01 Pass B workaround identity | B2 | PASS / FAIL | B2 (or B1) |
| C-02 Pass A switching costs | A3 | PASS / FAIL | A3 |
| C-02 Pass B switching costs | B3 | PASS / FAIL | B3 |
| C-03 Inertia threat HIGH | Score section | PASS / FAIL | Score section |
| C-04 Synthesis defeat conditions | Synthesis | PASS / FAIL | Synthesis (or A4/B4) |
| R-01 Team type scoped | Synthesis | PASS / FAIL | Synthesis |
| R-02 Role-level precision (all sections) | A2, B2, A4, B4 | PASS / FAIL | Earliest vague section |
| R-03 At least one cost cited to role | A3 or B3 | PASS / FAIL | A3 or B3 |
| **All essential (C-01–C-05) pass?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: Completion blocker. C-05 rows cascade: A1 FAIL propagates into A2
and A4; B1 FAIL propagates into B2 and B4. Synthesis FAIL may require repairing A4 or B4 entries
to produce stronger ID-referenced defeat conditions. Always repair at the earliest failing section,
then re-check the cascade.

---

*End V-05*
