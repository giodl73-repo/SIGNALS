# trace-skill Prompt Variations — Round 1

---

## V-01 — Axis: Role Sequence
**Hypothesis**: Enumerating spec inputs before invocation inputs (spec-first) reduces binding errors because the spec defines what's possible before the invocation constrains what's actual.

---

```markdown
You are executing trace-skill.

TASK: Hand-compile a skill execution. You have a skill spec and a test invocation.
Trace the 4-phase lifecycle — Gather, Bind, Execute, Verdict — and produce the
target artifact exactly as the skill would produce it. The hand-compiled artifact
IS the golden baseline.

---

## Phase 1: Gather

Enumerate every input the skill requires. Process in this order:

1. **Spec inputs** — read the skill spec and list every named parameter the skill declares.
   For each: name, type, required/optional, default if any, source = "spec".

2. **Invocation inputs** — read the test invocation and list every argument provided.
   For each: name, value (exact), source = "invocation".

3. **Context inputs** — list any ambient values the skill reads from the environment
   (date, working directory, topic registry, etc.).
   For each: name, value, source = "context".

Close with a **Coverage Matrix**:

> Closed-world assumption: every input not listed here is not used.

| Input Name | Required | Provided | Gap? |
|------------|----------|----------|------|
| ...        | ...      | ...      | ...  |

Any Gap = YES means the trace cannot proceed. Declare BLOCKED and stop.

---

## Phase 2: Bind

For every input in Gather, resolve to exactly one value. No ranges, no ambiguity.

| Input Name | Source | Resolved Value |
|------------|--------|----------------|
| ...        | ...    | ...            |

If any input cannot be resolved to a single value, declare UNRESOLVABLE and explain why.

---

## Phase 3: Execute

Run the skill logic step by step using only the bound values. Produce the target artifact
in full — no elision markers ([...], etc.), no placeholders.

Artifact naming: `{topic}-{signal}-{date}.md`
Artifact storage path: `simulations/{namespace}/{skill}/`

Begin the artifact immediately after this line:

---

[ARTIFACT BEGINS HERE — write the complete artifact]

---

[ARTIFACT ENDS HERE]

---

## Phase 4: Verdict

Evaluate against the rubric. Cite criterion IDs directly.

| Criterion | ID | PASS / FAIL | Evidence |
|-----------|----|-------------|----------|
| Four phases present in sequence | C-01 | ... | ... |
| Gather enumerates all inputs by name with source | C-02 | ... | ... |
| Bind maps every input to resolved value | C-03 | ... | ... |
| Execute produces artifact with correct naming and sections | C-04 | ... | ... |
| Verdict declares PASS/FAIL with rationale | C-05 | ... | self-referential |
| Phases carry exact schema labels | C-06 | ... | ... |
| Verdict cites criterion IDs | C-07 | ... | self-referential |
| Artifact complete — no elision markers | C-08 | ... | ... |
| Gather includes Coverage Matrix | C-09 | ... | ... |
| Execute relays carry evidence fields | C-10 | ... | ... |

**Essential (C-01–C-05)**: _/5 PASS
**Overall**: PASS / FAIL

If any essential criterion FAILs, the overall verdict is FAIL regardless of score.
```

---

## V-02 — Axis: Output Format
**Hypothesis**: A prose-dominant format (with tables only where structure is mandatory) reduces cognitive load for reviewers evaluating whether the trace reflects real skill logic, because narrative flow is easier to audit than sparse table rows.

---

```markdown
You are executing trace-skill.

Hand-compile this skill execution. You have a spec and an invocation. Walk through
four phases and produce the artifact the skill would produce. The output of this
trace IS the golden baseline — it must be complete, unambiguous, and fully written out.

---

## Phase 1 — Gather

Write a short paragraph identifying the skill being traced and the invocation being tested.

Then list every input the skill needs. For each input, write one line:
- **{name}** (`{type}`, {required|optional}): {description of what it is} — sourced from {spec | invocation | context}

After the list, state the closed-world assumption in your own words: you are committing
to a finite set of inputs and will not use anything not listed.

If any required input is missing from the invocation, state this clearly and stop.

---

## Phase 2 — Bind

Write a paragraph explaining how you resolve each input to a working value.
Where the invocation provides an explicit value, say so. Where you draw from context
(today's date, the topic registry), say what value you read and from where.

Then produce a concise binding summary:

```
{name} = {exact value}
{name} = {exact value}
...
```

Every name from Gather must appear here. No exceptions.

---

## Phase 3 — Execute

Narrate the skill execution step by step as if you are the skill running. Use present
tense: "The skill reads... The skill produces... The skill writes..."

After the narration, produce the artifact in full. Write it exactly as it would appear
on disk. No ellipsis, no "[content omitted]", no "[see above]". Every section complete.

Artifact file: `{topic}-{signal}-{date}.md`
Artifact path: `simulations/{namespace}/{skill}/`

---

## Phase 4 — Verdict

Write one paragraph summarizing what the trace produced and whether it satisfies the
skill's purpose.

Then address each rubric criterion explicitly:

- **C-01** (four phases): ...
- **C-02** (Gather enumerates inputs): ...
- **C-03** (Bind resolves all inputs): ...
- **C-04** (Execute produces artifact): ...
- **C-05** (Verdict declares PASS/FAIL): ...
- **C-06** (exact phase labels): ...
- **C-07** (criterion IDs cited): ...
- **C-08** (no elision): ...
- **C-09** (Coverage Matrix): ...
- **C-10** (carry evidence fields): ...

Close with a single line: **PASS** or **FAIL**, and one sentence stating why.
```

---

## V-03 — Axis: Lifecycle Emphasis
**Hypothesis**: Front-loading detail in Gather (explicit coverage matrix, gap detection) and compressing Bind/Verdict reduces drift — most trace failures originate from missed inputs, not bad execution logic.

---

```markdown
You are executing trace-skill.

Produce a hand-compiled skill execution trace. Four phases: Gather, Bind, Execute, Verdict.
The Execute phase produces the real artifact. Everything before it earns the right to execute.

---

## Phase 1: Gather  ← THIS PHASE IS THE CRITICAL GATE

Gather is where most traces fail. Do it thoroughly.

**Step 1.1 — Read the spec.**
List every input declared in the skill spec. For each:
- Name
- Type
- Required or optional
- Default value (if any)
- What it controls in the skill's logic

**Step 1.2 — Read the invocation.**
List every argument provided in the test invocation. For each:
- Name
- Exact value as provided
- Whether it matches a declared spec input (yes/no)

**Step 1.3 — Read the context.**
List every ambient value the skill will consume:
- Today's date
- Working directory
- Any registry or index files the skill reads
Note the exact value for each.

**Step 1.4 — Build the Coverage Matrix.**

Closed-world assumption: any input not in this table is not used by this trace.

| Input | Spec Declared | Invocation Provided | Context Provided | Gap? |
|-------|--------------|---------------------|------------------|------|
| ...   | ✓ / –        | ✓ / –               | ✓ / –            | Y/N  |

**Step 1.5 — Gate check.**
If any row has Gap = Y and Required = yes: BLOCKED. Do not proceed.
If all required inputs are covered: proceed to Bind.

---

## Phase 2: Bind

Resolve each gathered input to exactly one value. One line per input.

`{name}` = `{value}`  (source: {spec-default | invocation | context})

---

## Phase 3: Execute

Produce the artifact using bound values only. Write it completely — no elision.

File: `{topic}-{signal}-{date}.md` at `simulations/{namespace}/{skill}/`

---

[BEGIN ARTIFACT]

[END ARTIFACT]

---

## Phase 4: Verdict

Criterion table:

| ID | Criterion | Result | Note |
|----|-----------|--------|------|
| C-01 | Four phases in sequence | PASS/FAIL | |
| C-02 | Gather enumerates inputs with source | PASS/FAIL | |
| C-03 | Bind resolves all inputs | PASS/FAIL | |
| C-04 | Artifact correct naming + sections | PASS/FAIL | |
| C-05 | Verdict declares PASS/FAIL | PASS/FAIL | |
| C-06 | Exact phase labels | PASS/FAIL | |
| C-07 | Verdict cites criterion IDs | PASS/FAIL | |
| C-08 | No elision markers | PASS/FAIL | |
| C-09 | Coverage Matrix present | PASS/FAIL | |
| C-10 | Carry evidence fields in Execute | PASS/FAIL | |

Essential pass rate: _/5. **Overall: PASS / FAIL.**
```

---

## V-04 — Axis: Phrasing Register
**Hypothesis**: A conversational, first-person register ("I am reading...") makes the trace easier to follow because it signals that each statement is the result of active interpretation, not mechanical template-filling.

---

```markdown
You are executing trace-skill.

I want you to act as if you are the skill — narrate your own execution in first person.
Walk through four labeled phases. At the end, the artifact you produce is the golden baseline.

---

### Gather

Start by saying: "I am gathering inputs for this trace."

Tell me what skill you're tracing and what invocation you're working from.
Then go through everything you'll need:

- What does the spec say you need? Name each input, say where it comes from, say whether
  it's required. Be specific — not "topic name" but "the topic_name parameter declared in
  the spec's `inputs:` block."

- What does the invocation actually give you? Go through the call arguments one by one.

- What are you reading from context? Date, directory, any files you'd automatically open?

Close Gather with this line verbatim:
> "Closed-world: I will use only the inputs listed above. Nothing else."

If anything required is missing, say: "I cannot proceed — {input} is required but not provided."

---

### Bind

Say: "I am binding each input to its working value."

Go through each input from Gather and tell me exactly what value you're using:

"For {name}, I'm using {value}, which came from {source}."

Every input must get a binding statement. No skipping.

---

### Execute

Say: "I am executing the skill now."

Narrate what you're doing as you do it. Then produce the artifact — completely, fully written,
exactly as it would appear if the skill had run for real.

File goes to: `simulations/{namespace}/{skill}/{topic}-{signal}-{date}.md`

Write the whole thing. No "[abbreviated]", no "[omitted for brevity]". The full artifact.

---

### Verdict

Say: "I am evaluating this trace."

Go through each criterion and make a call:

- C-01 (four phases in sequence): I [did / did not] include all four phases in order. → PASS / FAIL
- C-02 (Gather inputs by name with source): I [did / did not] name and source every input. → PASS / FAIL
- C-03 (Bind resolves all inputs): I [did / did not] bind every gathered input. → PASS / FAIL
- C-04 (Execute artifact correct): The artifact [is / is not] complete with correct naming. → PASS / FAIL
- C-05 (Verdict states PASS/FAIL): [By writing this I am satisfying this criterion.] → PASS
- C-06 (exact labels): I [did / did not] use exact phase labels. → PASS / FAIL
- C-07 (criterion IDs cited): I [am / am not] citing criterion IDs in this verdict. → PASS / FAIL
- C-08 (no elision): The artifact [contains / does not contain] any elision markers. → PASS / FAIL
- C-09 (Coverage Matrix): Gather [did / did not] include a coverage matrix. → PASS / FAIL
- C-10 (carry evidence fields): Execute [did / did not] relay role, signal, binding, status. → PASS / FAIL

Essential criteria (C-01–C-05): _/5 passing.

Final call: **PASS** / **FAIL**
```

---

## V-05 — Combined Axes: Lifecycle Emphasis × Output Format × Phrasing Register
**Hypothesis**: Combining a gate-heavy Gather (lifecycle emphasis) with mixed table/prose format and a direct imperative register produces the most auditable trace — structured gates force completeness, tables enable fast scanning, imperative phrasing eliminates hedging.

---

```markdown
You are executing trace-skill.

Hand-compile the skill execution below. Four phases. Each phase has a gate.
A phase gate must pass before the next phase begins. If any gate fails, stop and
report the failure — do not continue to the next phase.

The artifact you produce in Execute IS the golden baseline. Write it completely.

---

## PHASE 1 — GATHER

**Objective**: Enumerate every input this skill will consume. Miss one and the trace
is wrong. There are no implicit inputs.

**1a. Spec inputs**

Read the skill spec. For each declared input, add a row:

| Name | Type | Required | Default | What it controls |
|------|------|----------|---------|-----------------|
| | | | | |

**1b. Invocation inputs**

Read the test invocation. For each provided argument, add a row:

| Name | Value | Maps to spec input? |
|------|-------|---------------------|
| | | |

**1c. Context inputs**

List everything the skill reads from environment:

| Name | Value | Source |
|------|-------|--------|
| date | | system clock |
| working_dir | | shell |
| | | |

**1d. Coverage Matrix** ← GATE

Closed-world assumption: the inputs below are the complete and finite set used by this trace.

| Input | Required | Covered? | Gap? |
|-------|----------|----------|------|
| | Y/N | Y/N | Y/N |

**GATE 1**: Any Required=Y + Gap=Y → BLOCKED. Stop.
All required inputs covered → PASS GATE 1. Proceed to Bind.

---

## PHASE 2 — BIND

**Objective**: Resolve every gathered input to a single unambiguous value.

| Input | Resolved Value | Source |
|-------|---------------|--------|
| | | spec-default / invocation / context |

**GATE 2**: Any input unresolvable → UNRESOLVABLE. Stop and explain.
All inputs resolved → PASS GATE 2. Proceed to Execute.

---

## PHASE 3 — EXECUTE

**Objective**: Produce the artifact using bound values only.

Artifact path: `simulations/{namespace}/{skill}/{topic}-{signal}-{date}.md`

For each section of the artifact, state:
- **Role** producing this section (which part of the skill's logic)
- **Signal** (what evidence or output this section carries)
- **Binding** (which bound value(s) drive this section)
- **Status** (complete / partial / blocked)

Then write the section in full.

Repeat for every section. No elision markers anywhere.

**GATE 3**: Any section Status = partial or blocked → INCOMPLETE. Document which section
and why, then continue with remaining sections.

---

## PHASE 4 — VERDICT

**Objective**: Evaluate the trace against rubric criteria. Cite IDs. Make a binary call.

| ID | Criterion | PASS / FAIL | Evidence (one line) |
|----|-----------|-------------|---------------------|
| C-01 | Four phases in sequence | | |
| C-02 | Gather enumerates inputs with source | | |
| C-03 | Bind resolves all inputs | | |
| C-04 | Artifact naming + sections correct | | |
| C-05 | Verdict declares PASS/FAIL | PASS | self-referential |
| C-06 | Exact phase schema labels | | |
| C-07 | Verdict cites criterion IDs | PASS | self-referential |
| C-08 | No elision markers in artifact | | |
| C-09 | Coverage Matrix with closed-world preamble | | |
| C-10 | Execute sections carry role/signal/binding/status | | |

Essential (C-01–C-05): _/5
Recommended (C-06–C-08): _/3
Aspirational (C-09–C-10): _/2

Score: `({essential}/5 × 60) + ({recommended}/3 × 30) + ({aspirational}/2 × 10)` = **_/100**

**Overall: PASS / FAIL**

PASS requires: all 5 essential criteria pass AND score ≥ 80.
If either condition fails, verdict is FAIL.
```

---

## Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence (spec-first → invocation → context) | Spec-first ordering reduces binding errors by establishing possibility space before constraints |
| V-02 | Output format (prose-dominant with minimal tables) | Narrative flow is more auditable than sparse table rows for logic traces |
| V-03 | Lifecycle emphasis (Gather as critical gate, Execute/Verdict compressed) | Most trace failures originate from missed inputs — front-load the gate |
| V-04 | Phrasing register (conversational first-person) | First-person narration signals active interpretation vs mechanical template-filling |
| V-05 | Combined (gate-heavy lifecycle × mixed format × imperative register) | Structured gates + scannable tables + no-hedge phrasing maximizes audit speed and completeness |
