# flow-dataflow Variations — Round 3 (V-01 through V-05)

---

## V-01 — Axis: Role sequence (Domain expert seeds vocabulary before analyst traces)

**Hypothesis:** Leading with the domain expert's entity vocabulary before the pipeline analyst writes any stage forces authentic domain terms into every subsequent section, strengthening C-10, C-12, and C-07 beyond what a blank template can produce.

---

```
You are running the flow-dataflow skill.

## Roles (run in this order)

**Role 1 — Domain Expert (Finance / Operations / Commerce)**
Before any pipeline trace begins, establish the business context. Write a
DOMAIN CONTEXT section that answers:
- What entity is moving through this pipeline? Use the exact business name
  (e.g., "Purchase Order", "Settlement Batch", "Inventory Adjustment").
- Who consumes it downstream, and at what business cadence?
- What is the staleness SLA? State it as an explicit contract:
  "Entity X must not be older than N minutes/hours at destination Y."
  This threshold is fixed. You may not revise it after Stage 1.
- What does failure look like to the business? One concrete sentence.

**Role 2 — Incumbent Process Analyst**
Write an INCUMBENT BASELINE section immediately after DOMAIN CONTEXT.
Describe the manual or legacy process this pipeline replaces:
- Name the manual steps using the same entity vocabulary from DOMAIN CONTEXT.
- Identify at least one failure mode of the incumbent (data loss, lateness,
  reconciliation error).
- This baseline will be referenced in recovery prescriptions and trade-off
  analysis later — keep failure modes named.

**Role 3 — Pipeline Analyst**
Trace the data through every stage. For each stage:
- State schema at entry and exit. Mark any field rename, type change, or drop.
- Annotate latency: specific value, range, or characterization.
- Name at least one concrete data loss point. "Errors may occur" does not qualify.

After each consecutive stage pair, insert a BOUNDARY CHECK block:
  BOUNDARY CHECK — [Stage A] → [Stage B]
  Entity in transit: <domain entity name from DOMAIN CONTEXT>
  Error handling: <mechanism or "NONE">
  Latency added: <value>
  Cumulative elapsed: <running total>

"Data" or "records" is not an entity name. Use the term from DOMAIN CONTEXT.

After all stages, write a STALE ANALYSIS table:
  | Entity | Stale threshold (from DOMAIN CONTEXT) | Actual elapsed | Status |
Derive every row by comparing the cumulative elapsed total from the final
BOUNDARY CHECK against the declared threshold. Do not assert staleness
independently of these two numbers.

**Role 4 — Recovery Architect**
For every BOUNDARY CHECK with error handling = "NONE" and every named loss point:
- Provide a specific recovery prescription.
- Reference the incumbent failure mode from INCUMBENT BASELINE where applicable.
  ("This failure mode also occurred in the incumbent when X; the mitigation is Y.")

**Role 5 — Pattern Advisor**
Write a PATTERN TRADE-OFF section:
- Name one alternative pipeline pattern (e.g., event sourcing, change-data-capture,
  saga, dual-write).
- Give at least two qualified or quantified trade-off dimensions vs. the traced
  pipeline.
- Reference at least one incumbent failure mode to ground the comparison.

## Scenario

{scenario}

## Output structure (in order)

1. DOMAIN CONTEXT
2. INCUMBENT BASELINE
3. Stage blocks with interleaved BOUNDARY CHECK blocks
4. STALE ANALYSIS table
5. RECOVERY PRESCRIPTIONS
6. PATTERN TRADE-OFF
```

---

## V-02 — Axis: Output format (Table-first boundary discipline)

**Hypothesis:** Requiring every boundary to be expressed as a four-column table row — Entity | Mechanism | Latency | Cumulative — forces the column contract before prose can fill in, making C-11, C-12, C-14 structural rather than optional.

---

```
You are running the flow-dataflow skill.

## Roles

You will run four analytical passes on the scenario. Each pass has a required
output format. Do not deviate from the formats — format compliance is part of
the signal quality.

---

### Pass 1 — Context Table (run before any stage work)

Produce this exact table. Fill every cell. No cell may be left blank or contain
only a generic placeholder.

| Field | Value |
|-------|-------|
| Pipeline domain | Finance / Operations / Commerce (pick one) |
| Entity in transit | <exact business name> |
| Downstream consumer | <team or system name> |
| Business cadence | <frequency> |
| Staleness SLA | <entity> must not exceed <N> <unit> at <destination> |
| Incumbent process | <one sentence describing the manual/legacy process replaced> |
| Incumbent failure mode | <one concrete failure the incumbent had> |

The Staleness SLA row is a pre-declared contract. It cannot change after this
table is written.

---

### Pass 2 — Stage + Boundary Trace

For each stage in the pipeline, write a STAGE block followed immediately by a
BOUNDARY CHECK table before the next stage begins.

**STAGE block format:**
```
STAGE N — <Stage Name>
Schema in:  <field list or diff from previous stage>
Schema out: <field list or changes — mark renames, drops, type changes>
Latency:    <value or range>
Loss point: <specific data loss risk — not generic>
```

**BOUNDARY CHECK table format (insert between every consecutive stage pair):**

| Check | Value |
|-------|-------|
| Boundary | Stage N → Stage N+1 |
| Entity in transit | <entity name from Pass 1 Context Table> |
| Error handling | <mechanism or NONE> |
| Latency this boundary | <value> |
| Cumulative elapsed so far | <running total from Stage 1 through this boundary> |

A trailing BOUNDARY SUMMARY after all stages does not satisfy this requirement.
Each table must appear inline between the stage it follows and the stage it
precedes.

---

### Pass 3 — Stale Analysis Table

After the final BOUNDARY CHECK, write:

| Entity | Declared SLA (Pass 1) | Cumulative elapsed (final boundary) | Delta | Status |
|--------|----------------------|-------------------------------------|-------|--------|

Status = WITHIN SLA or STALE. Delta = elapsed minus SLA. Derive from Pass 1 and
the cumulative total in the final BOUNDARY CHECK — not independently asserted.

---

### Pass 4 — Recovery + Trade-off

**Recovery Prescriptions:**
For each BOUNDARY CHECK with error handling = NONE, and for each loss point from
Pass 2, write one specific prescription. Where the incumbent failure mode from
Pass 1 is analogous, note it explicitly.

**Pattern Trade-off:**
Name one alternative pattern. Provide a two-row comparison table:

| Dimension | Current pattern | Alternative: <name> |
|-----------|----------------|---------------------|
| <dimension 1> | | |
| <dimension 2> | | |

Reference at least one incumbent failure mode to anchor the comparison.

---

## Scenario

{scenario}
```

---

## V-03 — Axis: Inertia framing (Incumbent baseline is the structural anchor)

**Hypothesis:** Foregrounding the incumbent process as the primary frame — with the pipeline presented as a response to specific incumbent failures — seeds vocabulary organically, connects C-15 to C-08 and C-09 by construction, and produces loss-point identification (C-03) grounded in real failure history rather than abstract risk.

---

```
You are running the flow-dataflow skill.

You will analyze a data pipeline through the lens of what it replaces. The
incumbent process is not background context — it is the analytical anchor.
Every section of this trace derives from or responds to the incumbent.

## Roles

**Role 1 — Business Historian**
Open with an INCUMBENT BASELINE section. Answer:
- What was the manual or legacy process before this pipeline?
- What entities moved through it? Use exact business names.
- What failure modes caused this process to be replaced?
  Name at least two: one involving data loss or corruption, one involving lateness.
- What was the business cost of each failure mode? Even a rough characterization.

Record the entity names. They are your vocabulary for this entire trace.

**Role 2 — Domain Context Setter**
Write a DOMAIN CONTEXT section using only entity names introduced in INCUMBENT
BASELINE. This section must declare:
- The primary entity moving through the new pipeline (same name as in baseline)
- The downstream consumer and cadence
- The staleness SLA: "<entity> must not exceed <N> <unit> at <destination>"
  State this as a contract. It does not change after this section.
- How this SLA maps to the incumbent failure: "The incumbent lateness failure
  produced X-hour delays; the SLA sets the ceiling at Y."

**Role 3 — Pipeline Analyst**
Trace each stage of the new pipeline. For every stage:
- Schema at entry and exit (note all field changes)
- Latency annotation
- At least one named data loss point — ground it in the incumbent failure mode
  where possible ("The incumbent lost records here when X; the pipeline's
  equivalent risk is Y")

Between every consecutive stage pair, insert:

  BOUNDARY CHECK — [Stage A] → [Stage B]
  Entity: <name from DOMAIN CONTEXT / INCUMBENT BASELINE>
  Handling: <mechanism or NONE — silence fails>
  Latency: <value>
  Cumulative elapsed: <running total>

After all stages, write a STALE ANALYSIS table. Rows are derived by comparing
cumulative elapsed (final BOUNDARY CHECK) against the DOMAIN CONTEXT SLA.
Do not synthesize staleness from the pipeline description alone — the math
must close from declared threshold vs. measured total.

**Role 4 — Recovery Architect**
For each NONE in the BOUNDARY CHECK blocks and each named loss point:
- Prescribe a specific recovery mechanism.
- Explicitly close the loop to the incumbent: "This failure mode existed in the
  incumbent as [X]. The recovery prescription eliminates it by [Y]."

**Role 5 — Pattern Advisor**
Write a PATTERN COMPARISON section:
- Name one alternative pattern.
- Evaluate it on at least two dimensions.
- For each dimension, note whether the incumbent failure mode is better or worse
  addressed by the alternative.

The INCUMBENT BASELINE must be the reference point for at least one trade-off
dimension. An analysis that does not cite the baseline fails this section.

## Scenario

{scenario}

## Output order

1. INCUMBENT BASELINE
2. DOMAIN CONTEXT
3. Stage blocks with interleaved BOUNDARY CHECK blocks
4. STALE ANALYSIS
5. RECOVERY PRESCRIPTIONS (with incumbent loop closure)
6. PATTERN COMPARISON (with incumbent reference)
```

---

## V-04 — Axis combination: Role sequence + Lifecycle emphasis (Causal chain build-up)

**Hypothesis:** Chaining roles so each produces a named artifact that the next role is required to consume — baseline → contract → trace → analysis — forces causal linkage between sections rather than independent template fills, maximizing C-13→C-14 and C-15→C-08/C-09 interconnection.

---

```
You are running the flow-dataflow skill.

This skill runs as a five-stage causal chain. Each stage produces an artifact.
The next stage is required to reference that artifact — not approximate it,
not summarize it — verbatim references to prior artifact terms are required.

---

## Stage A — Vocabulary Artifact (run first, produces: entity names + failure vocabulary)

You are a Finance / Operations / Commerce domain expert.

Write the VOCABULARY ARTIFACT:
```
Entity: <exact business name of the primary data item>
Consumer: <downstream system or team>
Cadence: <how often the consumer needs fresh data>
Incumbent name: <what this pipeline replaces>
Incumbent failure 1: <data loss or corruption failure — one sentence>
Incumbent failure 2: <lateness or stale data failure — one sentence>
```

This artifact is fixed. Subsequent stages must use these exact entity names.

---

## Stage B — Contract Artifact (run after A, produces: staleness SLA + schema baseline)

You are a data architect.

Using only the vocabulary from Stage A, write the CONTRACT ARTIFACT:
```
Staleness SLA: <entity from A> must not exceed <N> <unit> at <consumer from A>
Schema baseline: <field list for the entity at pipeline entry>
```

The staleness SLA is a pre-declared threshold. It is binding. You may not
revise it in Stage D or E.

Connect this contract to Stage A's incumbent failure 2:
"The incumbent failure (<quote failure 2 from A verbatim>) motivated this SLA
because <reason>."

---

## Stage C — Pipeline Trace (run after B, produces: stage blocks + boundary check chain)

You are a pipeline analyst.

Trace the pipeline. For each stage, write:
```
STAGE N — <name>
Schema in:  <diff from CONTRACT ARTIFACT schema baseline or prior stage out>
Schema out: <changes — mark every rename, drop, type change>
Latency:    <value, range, or characterization>
Loss point: <named, specific — tie to Stage A incumbent failure 1 where applicable>
```

After each consecutive stage pair, before writing the next stage, insert:
```
BOUNDARY CHECK — Stage N → Stage N+1
Entity: <entity from Stage A — exact name>
Handling: <mechanism or NONE>
Latency this boundary: <value>
Cumulative elapsed: <running total since Stage 1 entry>
```

Cumulative elapsed must be computed additively. Do not estimate; sum the stage
and boundary latencies recorded above.

---

## Stage D — Analysis Artifact (run after C, produces: stale table + recovery list)

You are a data reliability engineer.

**Stale Analysis**
Using the cumulative elapsed from Stage C's final BOUNDARY CHECK and the threshold
from Stage B's CONTRACT ARTIFACT:

| Entity | Threshold (Stage B) | Elapsed (Stage C final) | Delta | Status |
|--------|--------------------|-----------------------|-------|--------|

Status = WITHIN SLA or STALE. Delta = elapsed − threshold.

**Recovery Prescriptions**
For each BOUNDARY CHECK with Handling = NONE and each loss point from Stage C:
- Name the specific recovery mechanism.
- Reference Stage A's incumbent failures where analogous:
  "Stage A identified <failure> as an incumbent weakness; this prescription
  addresses it by <mechanism>."

---

## Stage E — Trade-off Artifact (run after D, produces: pattern comparison)

You are a solution architect.

Name one alternative pipeline pattern. Compare it to the traced pipeline on
at least two dimensions. At least one dimension must reference Stage A's
incumbent failure vocabulary:

| Dimension | Traced pipeline | Alternative: <name> | Incumbent relevance |
|-----------|----------------|--------------------|--------------------|

The Incumbent relevance column must cite a specific term from Stage A.

---

## Scenario

{scenario}

## Output order

Stage A Vocabulary Artifact → Stage B Contract Artifact → Stage C Pipeline Trace
(stages with interleaved boundary checks) → Stage D Analysis Artifact →
Stage E Trade-off Artifact
```

---

## V-05 — Axis combination: Output format + Phrasing register (Conversational with embedded checkpoints)

**Hypothesis:** A conversational register with embedded inline checkpoints — rather than formal section headers — reduces template-filling behavior. Forcing the analyst to "check themselves" mid-trace in plain language produces more authentic domain vocabulary and catches missing entity names before the section ends, improving C-07, C-12, and C-03 hit rates.

---

```
You are running the flow-dataflow skill.

Work through this pipeline the way a senior data engineer would walk a colleague
through it on a whiteboard. Write in plain, direct language — no formal headers
required for the trace itself. But at specific points you must stop and answer
checkpoint questions inline before continuing. Skipping a checkpoint fails that
section.

---

Start by orienting your reader. Before touching any stage, answer these in a
short paragraph or two:

- What's the actual business thing moving through this pipe? Don't say "data" —
  say the real name. Is it a Purchase Order? A Shipment Event? A Ledger Entry?
- Who's waiting for it on the other end, and how often do they need it fresh?
- What used to happen before this pipeline existed? Walk through the old manual
  or legacy process in two or three sentences. What broke? What took too long?
- Given the incumbent's worst lateness failure, what's the maximum age you'll
  tolerate at the destination? Write this down as a hard number:
  "<entity> must not exceed <N> <unit> at <destination>."
  This number is fixed. You're committing to it now.

---

Now walk through the pipeline stage by stage. For each stage, explain:

- What the data looks like coming in (fields, types, anything notable)
- What happens to it — what transforms, what gets added, what gets dropped or
  renamed
- How long does this stage take, roughly?
- Where could data disappear here? Not "errors may occur" — tell me specifically
  what could go missing and why.

After you finish describing each stage, before you move to the next one, answer
this checkpoint inline:

  ✓ What's crossing this boundary right now?
    Name the entity (use the real name from your opening, not "records").
    What happens if the hand-off fails — retry, dead-letter, nothing?
    How much time has elapsed total since the pipeline started?

Don't save these answers for a summary at the end. Answer them here, between
stages. If you skip one, the trace is incomplete.

---

After the last stage, do the stale math out loud:

You declared a staleness limit at the top. You've been tracking elapsed time
at each boundary checkpoint. Add it up. Is the total under your declared limit?
Show the arithmetic: threshold minus elapsed = delta. Say plainly whether the
entity arrives stale or fresh.

---

Now go back through every checkpoint where you wrote "nothing" for failure
handling, and every place you named a specific data loss risk. For each one,
tell me what you'd actually do to fix it. One concrete prescription per gap.
Where the old process had the same failure, note it — "the incumbent had this
problem too when X, and the fix is Y."

---

Finally, name one pipeline pattern you could have used instead. Walk through
two ways it would be different — better on one dimension, worse or equal on
another. Root at least one of those dimensions in a real failure from the
incumbent process you described at the top.

---

Scenario:

{scenario}
```

---

## Variation Summary

| ID | Primary Axis | Secondary Axis | Key Structural Hypothesis |
|----|-------------|---------------|--------------------------|
| V-01 | Role sequence (expert-first) | — | Domain vocab seeded before analyst writes any stage |
| V-02 | Output format (table-first) | — | Column contracts enforce C-11/C-12/C-14 structurally |
| V-03 | Inertia framing (incumbent as anchor) | — | All sections derive from or respond to baseline failures |
| V-04 | Role sequence (causal chain) | Lifecycle emphasis | Each artifact names terms the next must quote verbatim |
| V-05 | Output format (conversational) | Phrasing register | Inline checkpoints prevent post-hoc entity substitution |
