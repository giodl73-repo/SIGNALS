# trace-inspect — Quest Variate R4 (V-01 through V-05)

---

## V-01 — Single Axis: Output Format (table-first, field-complete)

**Axis**: Output format  
**Hypothesis**: Mandating a table for every structured element (relays, gates, promotion decisions, amendments) makes fields structurally impossible to omit — compliance with C-03, C-04, C-06, C-07 becomes mechanical rather than attentional.

---

```markdown
# trace-inspect

Hand-compile a skill execution. Given a skill spec and a test invocation,
produce the output that skill would generate — phase by phase, step by step.
The hand-compiled artifact IS the golden baseline for quest-golden.

## Inputs

- `$SKILL_SPEC` — path to the skill SKILL.md to trace
- `$INVOCATION` — the test call (topic, parameters, context)

---

## Schemas (locked — no substitutions permitted)

| Schema | Valid values only |
|--------|-------------------|
| Schema 1 — Severity | P1, P2, P3 |
| Schema 2 — Source | SA, SG, EG, QO |
| Schema 3 — Lifecycle | Stage 1 relay → SA-TO-SG PROMOTION → Stage 2 relay |
| Schema 4 — Gates | G-1, G-2, G-3 (all three, Step 3c) |
| Schema 5 — Sub-steps | 3a → 3b → 3c → 3d (in order) |

Any value outside these sets anywhere in your output is a structural error.
Stop and correct before proceeding.

---

## Phase 1 — Setup

Read `$SKILL_SPEC`. Identify every role the skill assigns.

For each role, emit one binding block in table form:

| Field            | Value                                              |
|------------------|----------------------------------------------------|
| Role             | `<role name>`                                      |
| Schema 1 binding | `<severity labels this role may emit>`             |
| Schema 2 binding | `<source labels this role may emit>`               |
| Gap attribution  | `<gap types this role is responsible for>`         |

Every role must have its own table. No role may be skipped.

Close Phase 1 with:
> Phase 1 complete — N roles bound: [list role names].

---

## Phase 2 — Execute

Run the three Schema 3 lifecycle events in order.

### Stage 1 relay

For each Stage 1 role, produce a relay table:

| Field                 | Value                                             |
|-----------------------|---------------------------------------------------|
| Role                  | `<role name>`                                     |
| Received from         | `<upstream role or input source>`                 |
| Received values       | `<what was handed off>`                           |
| Schema 2 compliance   | Sources used: `<list>` — Conformance: YES / NO    |
| SA gaps               | `<gap text, P-level, label — or NONE>`            |
| EG gaps               | `<execution gaps — or NONE>`                      |
| Produced              | `<content this role adds to the artifact>`        |

### SA-TO-SG PROMOTION

Evaluate every SA gap from Stage 1. Produce a promotion table:

| SA Gap       | P-level | Decision           | Reason (one sentence)  |
|--------------|---------|--------------------|------------------------|
| `<gap text>` | P1/P2/P3| PROMOTES TO SG / REMAINS SA | `<reason>` |

Post-promotion inventory (required):

| Count | Value |
|-------|-------|
| SA remaining     | N |
| SG from promotion| N |

### Stage 2 relay

For each Stage 2 role, produce a relay table (same structure as Stage 1).
SG gaps from promotion are now active — include them in the SG column.

### Artifact write

After all relays complete, write the artifact to:
`simulations/trace/skill/{topic}-skill-trace-{date}.md`

Confirm every section declared in the skill's artifact contract is present:

| Section heading | Status  |
|-----------------|---------|
| `<section>`     | WRITTEN |

Close Phase 2 with:
> Phase 2 complete — artifact written to `<path>`.

---

## Phase 3 — Findings

Run sub-steps in Schema 5 order. Each sub-step requires a named-artifact
prerequisite check before executing.

### Step 3a — Collect findings

Prerequisite check:

| Check                      | Result    | Named referent          |
|----------------------------|-----------|-------------------------|
| Phase 2 artifact exists    | YES / NO  | `<artifact path>`       |

Proceed only if YES.

List every gap from all relays, with Source and Severity for each.

> Step 3a complete. Step 3b is valid to begin.

---

### Step 3b — Build findings table

Prerequisite check:

| Check                              | Result    | Named referent          |
|------------------------------------|-----------|-------------------------|
| Step 3a findings list exists       | YES / NO  | `<N findings from 3a>`  |

Proceed only if YES.

Produce the consolidated findings table. Minimum 3 rows, at least 2 distinct
Source types. Action must be distinct from Finding text.

| #  | Finding       | Source      | Severity    | Action (distinct from finding) |
|----|---------------|-------------|-------------|-------------------------------|
| 1  | `<finding>`   | SA/SG/EG/QO | P1/P2/P3    | `<action>`                    |

> Step 3b complete. Step 3c is valid to begin.

---

### Step 3c — Enforce gates

Prerequisite check:

| Check                              | Result    | Named referent          |
|------------------------------------|-----------|-------------------------|
| Step 3b findings table exists      | YES / NO  | `<N rows in 3b>`        |

Proceed only if YES.

Evaluate all three gates. Record every result in the gate table:

| Gate | Condition                                              | Initial result |
|------|--------------------------------------------------------|----------------|
| G-1  | >= 2 distinct Source types in Step 3b table            | PASS / FAIL    |
| G-2  | No two same-Source findings share identical Action text| PASS / FAIL    |
| G-3  | All Step 3b entries use only {P1, P2, P3}              | PASS / FAIL    |

**If any gate FAILs**, document the remediation loop:

| Gate | Failure reason | Remediation action | Post-remediation result |
|------|---------------|-------------------|------------------------|
| G-N  | `<why failed>` | `<what was changed in 3b>` | PASS / FAIL     |

If all gates pass on first evaluation, emit:
> C-12 exemption applies — all gates passed on first evaluation.

**Gate-clearance summary** (required before Step 3d):

| Gate | Final result (post-remediation if applicable) |
|------|-----------------------------------------------|
| G-1  | PASS / FAIL                                   |
| G-2  | PASS / FAIL                                   |
| G-3  | PASS / FAIL                                   |

State: "G-1 `<result>`, G-2 `<result>`, G-3 `<result>` — Step 3d is valid
to begin." (If any FAIL, Step 3d is BLOCKED — do not proceed.)

> Step 3c complete. Step 3d is valid to begin [or BLOCKED].

---

### Step 3d — Classify verdict

Prerequisite check:

| Check                                | Result    | Named referent             |
|--------------------------------------|-----------|----------------------------|
| All gates PASS (gate-clearance table)| YES / NO  | `<gate-clearance row ref>` |

Proceed only if YES.

Apply classification rules in priority order:

| Rule | Condition                                         | Classification          |
|------|---------------------------------------------------|-------------------------|
| R-1  | Any P1 SA gap remains SA after promotion          | NEEDS-SPEC-REVISION     |
| R-2  | EG gaps > 3 AND indicate structural role gap      | NEEDS-REDESIGN          |
| R-3  | Otherwise                                         | USEFUL                  |

Record which rule triggered and the resulting classification.

> Step 3d complete. Phase 3 closed.

---

## Phase 4 — Amend

**Phase-entry gate-clearance summary** (must reflect post-remediation states,
not initial states):

| Gate | Final result |
|------|-------------|
| G-1  | PASS / FAIL  |
| G-2  | PASS / FAIL  |
| G-3  | PASS / FAIL  |

State: "G-1 `<result>`, G-2 `<result>`, G-3 `<result>` — Phase 4 is valid
to begin."

Produce an amendment table. At least one row required.

| # | Type                | Finding ref | Action taken                | Result    |
|---|---------------------|-------------|----------------------------|-----------|
| 1 | CHANGE / DISMISSAL  | F-NN        | `<what changed or why dismissed>` | Updated / Dismissed |

Close Phase 4 with:
> Phase 4 complete — N amendments recorded.

---

## Phase 5 — Verdict

**Verdict**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

**Rationale**: `<one paragraph — name specific findings that drove the decision>`

**VC Compliance Ledger** (observed behavior must name specific values,
not say "as expected"):

| VC   | Schema   | Observed behavior                                  | Result      |
|------|----------|----------------------------------------------------|-------------|
| VC-1 | Schema 1 | `<exact severity values used, e.g. "P1 ×2, P2 ×3">` | PASS / FAIL |
| VC-2 | Schema 2 | `<exact source values used, e.g. "SA ×3, EG ×2">`   | PASS / FAIL |
| VC-3 | Schema 3 | `<lifecycle events named in observed order>`          | PASS / FAIL |
| VC-4 | Schema 4 | `<"G-1, G-2, G-3 all checked at Step 3c: YES">`      | PASS / FAIL |
| VC-5 | Schema 5 | `<"3a→3b→3c→3d ran in declared order with transitions">` | PASS / FAIL |

Overall VC result: PASS / FAIL
```

---

## V-02 — Single Axis: Phrasing Register (direct imperative, conversational)

**Axis**: Phrasing register  
**Hypothesis**: Replacing declarative specification language ("the trace records…") with direct imperative commands ("write…", "emit…", "do not proceed until…") reduces the cognitive distance between reading the instruction and knowing what to produce — especially for C-10/C-13 compliance where the trace author must remember to emit transition sentences.

---

```markdown
# trace-inspect

You are hand-compiling a skill run. You have a skill spec and a test
invocation. Walk through every phase as if you are the skill. Produce
what the skill would produce. The output you write here becomes the
golden test baseline.

Do not summarize. Do not say "the skill would then…" Write the actual
output as if the skill is running right now.

---

## Your inputs

- The skill spec: `$SKILL_SPEC`
- The test call: `$INVOCATION`

## Your labels (use only these, everywhere, always)

Severity: **P1**, **P2**, **P3** — nothing else.
Source: **SA**, **SG**, **EG**, **QO** — nothing else.

If you catch yourself using any other value, stop and fix it before
you write another line.

---

## Phase 1 — Set up

Read the spec. Find every role it defines.

For each role, write a binding block. Include all four fields:
- **Role**: the role's name
- **Schema 1 binding**: which severity labels it can emit
- **Schema 2 binding**: which source labels it can emit
- **Gap attribution**: the kinds of gaps it owns

Do all roles. Skip none.

When you finish, write:
> Phase 1 complete — N roles bound: [role names].

---

## Phase 2 — Run it

Run the lifecycle in this exact order:
1. Stage 1 relay
2. SA-TO-SG PROMOTION
3. Stage 2 relay

**For each relay**, write a relay block. Every field is required:

- **Role**: who is running
- **Received from**: who handed off, or what input
- **Received values**: what the handoff contained
- **Schema 2 compliance**: which source labels did this role use, and does
  that match its Phase 1 binding? Write YES or NO.
- **SA gaps**: any spec-layer gaps this role found (P-level + SA label,
  or write NONE)
- **EG gaps**: any execution gaps this role encountered (P-level + EG label,
  or write NONE)
- **Produced**: what this role adds to the artifact

**For the SA-TO-SG PROMOTION**, go through every SA gap you collected.
For each one, decide: does it promote to SG, or does it stay SA?
Write a row for each:
- The gap text
- Its P-level
- PROMOTES TO SG or REMAINS SA
- One sentence explaining why

After all gaps are decided, write:
> SA remaining: N. SG from promotion: N.

Stage 2 roles get the SG gaps too. Include them.

**After all relays are done**, write the artifact file at:
`simulations/trace/skill/{topic}-skill-trace-{date}.md`

Check that every section from the artifact contract appears. List each one
with WRITTEN next to it.

Write:
> Phase 2 complete — artifact written to `<path>`.

---

## Phase 3 — Find problems

Work through sub-steps 3a, 3b, 3c, 3d in order. Before you start each one,
check that the previous step's output actually exists, and name it.

### Step 3a

Before you begin — write this check:
> Prerequisite: Phase 2 artifact exists. Check: YES. Referent: `<path>`.

Now list every gap you observed across all relays. Give each one a Source
and a Severity.

Write:
> Step 3a complete. Step 3b is valid to begin.

---

### Step 3b

Before you begin — write this check:
> Prerequisite: Step 3a findings list exists. Check: YES.
> Referent: `<N findings from Step 3a>`.

Build the findings table. Rules:
- At least 3 rows
- At least 2 different Source values
- The Action column must say something different from the Finding column —
  not a restatement, an actual action

Write:
> Step 3b complete. Step 3c is valid to begin.

---

### Step 3c

Before you begin — write this check:
> Prerequisite: Step 3b table exists. Check: YES. Referent: `<N rows>`.

Check all three gates:

**G-1**: Count the distinct Source values in your Step 3b table.
Is it 2 or more? PASS or FAIL.

**G-2**: For each Source value, check whether any two findings with
that same Source share identical Action text. If any do, FAIL. Otherwise PASS.

**G-3**: Check every Severity value in Step 3b. Are they all P1/P2/P3?
PASS or FAIL.

If any gate fails:
- Say exactly what is wrong
- Say exactly what you are changing in Step 3b to fix it
- Re-check the gate
- Write the updated result

If all three pass on the first check, write:
> C-12 exemption applies — all gates passed on first evaluation.

Now write the gate-clearance summary. This is mandatory:
> G-1 [result], G-2 [result], G-3 [result] — Step 3d is valid to begin.

(If any gate still fails, write BLOCKED instead and stop.)

Write:
> Step 3c complete. Step 3d is valid to begin.

---

### Step 3d

Before you begin — write this check:
> Prerequisite: All gates PASS. Check: YES.
> Referent: gate-clearance summary above.

Pick the verdict. Check these rules in order:
1. If any P1 SA gap is still SA after promotion → **NEEDS-SPEC-REVISION**
2. If EG gaps exceed 3 and they point to a structural role gap → **NEEDS-REDESIGN**
3. Otherwise → **USEFUL**

Write which rule fired and what the verdict is.

Write:
> Step 3d complete. Phase 3 closed.

---

## Phase 4 — Fix things

First, write the Phase 4 entry summary. Use the post-remediation gate
states — not what they were before any fixes:
> G-1 [final result], G-2 [final result], G-3 [final result] —
> Phase 4 is valid to begin.

For each finding from Step 3b, decide: change something, or dismiss it?
Write at least one entry:
- Type: CHANGE or DISMISSAL
- Which finding (F-NN)
- What you changed, or why you dismissed it
- Result: Updated or Dismissed

Write:
> Phase 4 complete — N amendments recorded.

---

## Phase 5 — Deliver

Write the verdict line:
> Verdict: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

Write one paragraph explaining the decision. Name the specific findings
that drove it.

Fill in the VC compliance ledger. For each row, say what you actually
observed — specific values, counts, named events. Do not write "as expected."

| VC   | Schema   | Observed behavior | Result |
|------|----------|-------------------|--------|
| VC-1 | Schema 1 | `<what you saw>` | PASS / FAIL |
| VC-2 | Schema 2 | `<what you saw>` | PASS / FAIL |
| VC-3 | Schema 3 | `<what you saw>` | PASS / FAIL |
| VC-4 | Schema 4 | `<what you saw>` | PASS / FAIL |
| VC-5 | Schema 5 | `<what you saw>` | PASS / FAIL |

Overall VC result: PASS / FAIL
```

---

## V-03 — Single Axis: Lifecycle Emphasis (verbose phase boundaries, explicit transition machinery)

**Axis**: Lifecycle emphasis  
**Hypothesis**: Dedicating structural space to phase-boundary ceremonies — entry conditions, transition confirmations, inter-phase handoff declarations — increases C-10/C-11/C-13/C-14 compliance because the compiler cannot reach the next phase without passing through a named gate. The boundaries become load-bearing structure rather than prose decoration.

---

```markdown
# trace-inspect

Hand-compile a skill execution to produce its expected artifact.
This skill is lifecycle-strict: every phase has an entry condition,
a body, and a closing declaration. You may not enter a phase until
its entry condition is satisfied and recorded. You may not leave a
phase until its closing declaration is written.

Inputs: `$SKILL_SPEC`, `$INVOCATION`

Locked schemas — any deviation is a structural error:
- Schema 1 severity: {P1, P2, P3}
- Schema 2 source: {SA, SG, EG, QO}
- Schema 3 lifecycle: Stage 1 relay → SA-TO-SG PROMOTION → Stage 2 relay
- Schema 4 gates: G-1, G-2, G-3 (all three, at Step 3c only)
- Schema 5 sub-steps: 3a → 3b → 3c → 3d (in declared order)

---

## ═══ PHASE 1 ENTRY ═══

Entry condition: `$SKILL_SPEC` has been read and all roles identified.

State the entry condition resolution:
> Phase 1 entry condition: `$SKILL_SPEC` read. Roles identified: [list].
> Phase 1 is open.

---

## Phase 1 — Setup

For each identified role, produce a binding block:

**Role: `<name>`**
- Schema 1 binding: `<severity labels>`
- Schema 2 binding: `<source labels>`
- Gap attribution: `<gap ownership>`

Complete all roles before closing Phase 1.

## ═══ PHASE 1 CLOSE ═══

> Phase 1 closing declaration:
> - Roles bound: N [list names]
> - Schema 1 coverage: [which labels are bound to which roles]
> - Schema 2 coverage: [which labels are bound to which roles]
> - Handoff to Phase 2: role binding tables are available for Phase 2
>   relay validation.
> Phase 1 is closed. Phase 2 entry condition is now satisfiable.

---

## ═══ PHASE 2 ENTRY ═══

Entry condition: Phase 1 is closed and role binding tables exist.

State the entry condition resolution:
> Phase 2 entry condition: Phase 1 closed. N role binding tables exist.
> Phase 2 is open. Lifecycle sequence: Stage 1 relay → SA-TO-SG
> PROMOTION → Stage 2 relay.

---

## Phase 2 — Execute

Run each lifecycle event in Schema 3 order.

### ── Lifecycle event: Stage 1 relay ──

For each Stage 1 role, write a relay block with all required fields:

**Relay: `<role>`**
- Received from: `<source>`
- Received values: `<content>`
- Schema 2 compliance: sources used `<list>` / conformance YES or NO
- SA gaps: `<gap, P-level, SA label — or NONE>`
- EG gaps: `<gap, P-level, EG label — or NONE>`
- Produced: `<artifact contribution>`

### ── Lifecycle event: SA-TO-SG PROMOTION ──

For every SA gap collected in Stage 1, make a promotion decision:

**SA gap: `<gap text>`** (P`<level>`)
- Decision: PROMOTES TO SG / REMAINS SA
- Reason: `<one sentence>`

Post-promotion inventory:
> SA remaining: N. SG from promotion: N.
> Promoted gaps are now active for Stage 2 relay.

### ── Lifecycle event: Stage 2 relay ──

For each Stage 2 role, write a relay block (same structure as Stage 1).
Include SG gaps from the promotion event in the relay.

### ── Artifact write ──

After all relays complete, produce the artifact at:
`simulations/trace/skill/{topic}-skill-trace-{date}.md`

For each section declared in the artifact contract:
> Section `<name>`: WRITTEN

## ═══ PHASE 2 CLOSE ═══

> Phase 2 closing declaration:
> - Lifecycle events completed: Stage 1 relay, SA-TO-SG PROMOTION,
>   Stage 2 relay — in Schema 3 order: YES
> - Relays written: N (list roles)
> - SA gaps observed: N. SG promotions: N. SA remaining: N.
> - EG gaps observed: N.
> - Artifact written: YES — path: `<path>`
> - Artifact sections complete: N of N
> - Handoff to Phase 3: relay outputs and artifact are available for
>   findings collection.
> Phase 2 is closed. Phase 3 entry condition is now satisfiable.

---

## ═══ PHASE 3 ENTRY ═══

Entry condition: Phase 2 is closed, artifact exists, relay outputs available.

State the entry condition resolution:
> Phase 3 entry condition: Phase 2 closed. Artifact at `<path>` confirmed.
> Relay outputs: N relays with gap inventory available.
> Phase 3 is open. Sub-step sequence: 3a → 3b → 3c → 3d.

---

## Phase 3 — Findings

Each sub-step has its own entry condition, body, and closing sentence.
Do not begin a sub-step until its entry condition is recorded.

### ═══ STEP 3a ENTRY ═══

Entry condition: Phase 2 artifact exists and relay gap records are available.

> Step 3a prerequisite: Phase 2 artifact exists.
> Check: YES. Named referent: `<artifact path>`.
> Relay gap records available: YES. Named referent: `<N relay outputs>`.
> Step 3a is open.

### Step 3a — Collect findings

List every gap from all relays. Assign Source and Severity to each.

### ═══ STEP 3a CLOSE ═══

> Step 3a closing: N raw findings collected. Source distribution:
> [SA: N, SG: N, EG: N, QO: N].
> Step 3a is complete. Step 3b entry condition is now satisfiable.

---

### ═══ STEP 3b ENTRY ═══

Entry condition: Step 3a findings list exists with at least one entry.

> Step 3b prerequisite: Step 3a findings list exists.
> Check: YES. Named referent: N findings from Step 3a.
> Step 3b is open.

### Step 3b — Build findings table

Produce the consolidated table. Rules: >= 3 rows, >= 2 distinct Source
types, Action must not restate Finding.

| # | Finding | Source | Severity | Action |
|---|---------|--------|----------|--------|
| … |         |        |          |        |

### ═══ STEP 3b CLOSE ═══

> Step 3b closing: N findings in table. Source types present: [list].
> Severity values present: [list]. All Actions distinct from Findings: YES.
> Step 3b is complete. Step 3c entry condition is now satisfiable.

---

### ═══ STEP 3c ENTRY ═══

Entry condition: Step 3b findings table exists with at least 3 rows.

> Step 3c prerequisite: Step 3b findings table exists.
> Check: YES. Named referent: N rows in findings table.
> Step 3c is open. Evaluating G-1, G-2, G-3.

### Step 3c — Enforce gates

Evaluate each gate. Record initial results:

**G-1**: >= 2 distinct Source types in Step 3b. Initial result: PASS / FAIL
**G-2**: No same-Source pair shares identical Action text. Initial result: PASS / FAIL
**G-3**: All Severity values in {P1, P2, P3}. Initial result: PASS / FAIL

If any gate FAILs, document the remediation loop before proceeding:

> Gate `<X>` FAIL — remediation:
> - Failure: `<what caused the failure>`
> - Action taken: `<what was changed in Step 3b>`
> - Re-evaluation of Gate `<X>`: PASS / FAIL

After any remediation, confirm the final state of all gates.

If all gates passed on first evaluation:
> C-12 exemption applies — all gates passed on first evaluation.

### ═══ STEP 3c GATE-CLEARANCE SUMMARY ═══

This summary must reflect final (post-remediation) states. If remediation
occurred, use the post-remediation result — not the initial FAIL:

> G-1: `<final result>` | G-2: `<final result>` | G-3: `<final result>`
> All gates cleared — Step 3d is valid to begin.
> (Or: Gate `<X>` failed — Step 3d is BLOCKED.)

### ═══ STEP 3c CLOSE ═══

> Step 3c closing: All gates evaluated. Final gate states recorded above.
> Step 3c is complete. Step 3d entry condition is now satisfiable
> [or BLOCKED if any gate remains FAIL].

---

### ═══ STEP 3d ENTRY ═══

Entry condition: All three gates show PASS in the Step 3c gate-clearance
summary.

> Step 3d prerequisite: All gates PASS.
> Check: YES. Named referent: Step 3c gate-clearance summary (G-1 PASS,
> G-2 PASS, G-3 PASS).
> Step 3d is open.

### Step 3d — Classify verdict

Apply rules in priority order:
1. P1 SA gap remaining after promotion → NEEDS-SPEC-REVISION
2. EG gaps > 3 AND structural role gap → NEEDS-REDESIGN
3. Otherwise → USEFUL

### ═══ STEP 3d CLOSE ═══

> Step 3d closing: Verdict classification: `<class>`. Rule triggered: R-`<N>`.
> Step 3d is complete.

## ═══ PHASE 3 CLOSE ═══

> Phase 3 closing declaration:
> - Sub-steps completed in order: 3a → 3b → 3c → 3d: YES
> - Findings: N total. Source types: [list]. Severity distribution: [list].
> - Gate final results: G-1 `<result>`, G-2 `<result>`, G-3 `<result>`
> - Verdict classification: `<class>` (Rule R-N)
> - Handoff to Phase 4: findings, gate states, and verdict available.
> Phase 3 is closed. Phase 4 entry condition is now satisfiable.

---

## ═══ PHASE 4 ENTRY ═══

Entry condition: Phase 3 is closed, all gates PASS, verdict is classified.

State the entry condition resolution (use post-remediation gate states;
if remediation occurred in Phase 3, these states must match the
post-remediation states documented there — not the initial states):

> Phase 4 entry condition: Phase 3 closed.
> Gate-clearance summary (post-remediation):
> G-1 `<final result>`, G-2 `<final result>`, G-3 `<final result>` —
> Phase 4 is valid to begin.
> Phase 4 is open.

---

## Phase 4 — Amend

For each finding from Step 3b, record an amendment or dismissal.
At least one entry required.

**Amendment `<N>`**
- Type: CHANGE / DISMISSAL
- Finding: F-`<NN>`
- Action: `<what was changed or why dismissed>`
- Result: Updated / Dismissed

## ═══ PHASE 4 CLOSE ═══

> Phase 4 closing declaration:
> - Amendments recorded: N (CHANGE: N, DISMISSAL: N)
> - All Step 3b findings addressed: YES
> Phase 4 is closed. Phase 5 entry condition is now satisfiable.

---

## ═══ PHASE 5 ENTRY ═══

Entry condition: Phase 4 is closed, all findings addressed, verdict from
Phase 3 is available.

> Phase 5 entry condition: Phase 4 closed. N amendments recorded.
> Verdict from Phase 3 is available: `<class>`.
> Phase 5 is open.

---

## Phase 5 — Verdict

**Verdict**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

**Rationale**: `<paragraph naming the specific findings that drove the verdict>`

**VC Compliance Ledger**:
Observed behavior must name specific values — not "as expected."

| VC   | Schema   | Observed behavior                              | Result      |
|------|----------|------------------------------------------------|-------------|
| VC-1 | Schema 1 | `<exact severity values, e.g. "P1×3, P2×2">`  | PASS / FAIL |
| VC-2 | Schema 2 | `<exact source values, e.g. "SA×4, EG×2">`    | PASS / FAIL |
| VC-3 | Schema 3 | `<lifecycle events observed, named in order>`  | PASS / FAIL |
| VC-4 | Schema 4 | `<"G-1, G-2, G-3 checked at Step 3c: YES">`   | PASS / FAIL |
| VC-5 | Schema 5 | `<"3a→3b→3c→3d in declared order: YES">`       | PASS / FAIL |

Overall VC result: PASS / FAIL
```

---

## V-04 — Combination: Role Sequence (EG-first) + Output Format (prose-led with inline tables)

**Axes**: Role sequence + Output format  
**Hypothesis**: Running the execution-layer (EG) roles before the spec-layer (SA) roles forces the trace author to surface what the skill *does* before reading what the spec *says*, preventing spec-anchoring bias that suppresses EG gaps. Prose-led format with inline tables keeps the narrative readable while ensuring structured fields remain complete.

---

```markdown
# trace-inspect

Hand-compile a skill execution. You have a skill spec and a test invocation.
Produce what the skill would produce, following the lifecycle exactly. This
output becomes the golden scenario baseline.

Inputs: `$SKILL_SPEC` — `$INVOCATION`

**Label constraint (enforced throughout)**:
Severity is P1, P2, or P3. Source is SA, SG, EG, or QO. No other values.

---

## Phase 1 — Setup

Read the spec. For each role, write a schema binding block. Four fields
required: role name, Schema 1 binding (severity labels), Schema 2 binding
(source labels), gap attribution (what kinds of gaps this role owns).

Collect all roles before proceeding.

> Phase 1 complete — N roles bound.

---

## Phase 2 — Execute

This variant runs the execution-layer (EG) roles first, before the
spec-layer (SA) roles run their SA gap surface. The motivation: by
identifying execution gaps without spec anchoring, you surface what
the skill fails to do before you know what the spec claims it should do.

**Lifecycle order in this variant**:
- EG Stage 1 relay (execution-gap roles only)
- SA Stage 1 relay (spec-gap roles)
- SA-TO-SG PROMOTION
- Stage 2 relay (all remaining roles)

### EG Stage 1 relay

Run execution-layer roles. For each, write a relay block in prose form
with an inline table for the schema compliance check:

> **`<Role>`** received `<what>` from `<source>`. It produced `<artifact
> contribution>`.
>
> Schema 2 compliance for this relay:
> | Source labels used | Declared in Phase 1 binding | Conformance |
> |--------------------|----------------------------|-------------|
> | `<label>`          | YES / NO                   | YES / NO    |
>
> EG gaps surfaced:
> - `<gap text>` — P`<level>`, EG
> - (or: No EG gaps in this relay.)

### SA Stage 1 relay

Run spec-layer roles. Same relay structure as above.

> **`<Role>`** received `<what>` from `<source>`. It produced `<artifact
> contribution>`.
>
> Schema 2 compliance: [table as above]
>
> SA gaps surfaced:
> - `<gap text>` — P`<level>`, SA
> - (or: No SA gaps in this relay.)

### SA-TO-SG PROMOTION

For every SA gap from the SA Stage 1 relay, write a promotion entry in
prose with the decision inline:

> **`<SA gap text>`** (P`<level>`) — PROMOTES TO SG. Reason: `<one sentence>`.

or

> **`<SA gap text>`** (P`<level>`) — REMAINS SA. Reason: `<one sentence>`.

Then state:
> Post-promotion inventory: SA remaining: N. SG from promotion: N.

### Stage 2 relay

Run remaining roles. Include SG gaps from promotion. Same relay structure.

### Artifact write

Write the artifact to `simulations/trace/skill/{topic}-skill-trace-{date}.md`.

For each section in the artifact contract:
> `<Section name>`: WRITTEN

> Phase 2 complete — artifact written to `<path>`.

---

## Phase 3 — Findings

### Step 3a — Collect

Before beginning, confirm:
> Prerequisite: Phase 2 artifact exists. Check: YES. Path: `<path>`.

List all gaps observed across all relays. Note: because EG roles ran
before SA roles in this variant, EG gaps were observed before spec context
was available — flag any EG gap whose scope or severity may shift now
that SA gaps are known.

> Step 3a complete. Step 3b is valid to begin.

### Step 3b — Build findings table

Before beginning, confirm:
> Prerequisite: Step 3a findings exist. Check: YES. N findings collected.

Build the consolidated findings table. Minimum 3 rows, minimum 2 distinct
Source types, Action distinct from Finding.

| # | Finding | Source | Severity | Action |
|---|---------|--------|----------|--------|
|   |         |        |          |        |

> Step 3b complete. Step 3c is valid to begin.

### Step 3c — Gate check

Before beginning, confirm:
> Prerequisite: Step 3b table exists. Check: YES. N rows.

Check all three gates:

**G-1** (>= 2 distinct Source types):
> Source types in table: [list]. Count: N. G-1: PASS / FAIL.

**G-2** (no same-Source pair with identical Action):
> Checked. G-2: PASS / FAIL.

**G-3** (all Severity values in {P1, P2, P3}):
> Severity values present: [list]. G-3: PASS / FAIL.

If any gate fails, document the remediation: what specifically failed,
what was changed in Step 3b, and the re-check result.

If all gates passed on first evaluation:
> C-12 exemption applies — all gates passed on first evaluation.

Gate-clearance summary (use final post-remediation states):
> G-1 `<result>`, G-2 `<result>`, G-3 `<result>` — Step 3d is valid to begin.

> Step 3c complete.

### Step 3d — Verdict classification

Before beginning, confirm:
> Prerequisite: All gates PASS. Check: YES. Referent: gate-clearance
> summary above (G-1 PASS, G-2 PASS, G-3 PASS).

Apply in priority order: NEEDS-SPEC-REVISION if P1 SA remains SA.
NEEDS-REDESIGN if EG gaps > 3 and structural. USEFUL otherwise.

> Verdict: `<class>`. Rule triggered: R-N.
> Step 3d complete. Phase 3 closed.

---

## Phase 4 — Amend

Phase-entry gate-clearance summary (reflects post-remediation states):
> G-1 `<final result>`, G-2 `<final result>`, G-3 `<final result>` —
> Phase 4 is valid to begin.

For each finding, write a prose amendment entry with inline type:

> **F-`<NN>`** [CHANGE / DISMISSAL]: `<what was changed, or why dismissed>`.
> Result: Updated / Dismissed.

At least one entry required.

> Phase 4 complete — N amendments recorded.

---

## Phase 5 — Verdict

**Verdict**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

**Rationale**: `<paragraph — name the specific findings>`

Note: because EG roles ran first in this variant, call out whether the
EG-first sequencing surfaced any gaps that spec-first sequencing would
likely have missed. This is the variant's delta signal.

**VC Compliance Ledger** (specific observed values, not "as expected"):

| VC   | Schema   | Observed behavior          | Result      |
|------|----------|---------------------------|-------------|
| VC-1 | Schema 1 | `<specific severity values>` | PASS / FAIL |
| VC-2 | Schema 2 | `<specific source values>`   | PASS / FAIL |
| VC-3 | Schema 3 | `<lifecycle events in order>`| PASS / FAIL |
| VC-4 | Schema 4 | `<gates checked at 3c>`      | PASS / FAIL |
| VC-5 | Schema 5 | `<sub-steps in order>`       | PASS / FAIL |

Overall VC result: PASS / FAIL
```

---

## V-05 — Combination: Inertia Framing (status-quo competitor named throughout) + Phrasing Register (diagnostic)

**Axes**: Inertia framing + Phrasing register  
**Hypothesis**: Framing each phase as a diagnostic against what a developer would ship without running this skill ("naive implementation") increases gap density and P-level honesty. A compiler who asks "what would break if this skill didn't exist?" surfaces more EG gaps and more P1s than one who asks "what does the spec say?" Diagnostic register ("why is this a problem?", "what did this catch?") sharpens Action column content and reduces restatements.

---

```markdown
# trace-inspect

You are running a diagnostic hand-compilation. You have a skill spec and
a test invocation. Your job is to walk through what the skill produces —
but always with the status-quo alternative in view.

The status-quo alternative is this: a developer reads the spec, builds
the skill without tracing it, and ships whatever they think it does.
Call this the **naive path**. Throughout the trace, note where the naive
path would diverge, fail silently, or produce a different artifact than
the one you produce here.

This framing is not optional. It is how the trace surfaces high-signal
gaps. A finding that the naive path would also catch is P3. A finding
that the naive path would miss entirely is P1 or P2.

Inputs: `$SKILL_SPEC`, `$INVOCATION`

Labels (no substitutions):
- Severity: P1 (naive path misses), P2 (partial miss), P3 (catchable without trace)
- Source: SA (spec gap), SG (promoted spec gap), EG (execution gap), QO (quality gap)

---

## Phase 1 — Diagnostic Setup

Read the spec. Identify every role. For each role, write a binding block:

**Role: `<name>`**
- Schema 1 binding: `<severity labels>`
- Schema 2 binding: `<source labels>`
- Gap attribution: `<gap types this role owns>`
- Naive-path risk: `<what a developer without this trace would likely
  get wrong or skip for this role>`

The naive-path risk field is required for every role. It is what makes
Phase 1 diagnostic rather than clerical.

> Phase 1 complete — N roles bound. Naive-path risks identified for all N.

---

## Phase 2 — Diagnostic Execution

Run the lifecycle in Schema 3 order:
1. Stage 1 relay
2. SA-TO-SG PROMOTION
3. Stage 2 relay

For each relay, write a relay block. After the standard fields, add a
diagnostic field: what the naive path would have produced for this role,
and how your relay output differs.

**Relay: `<role>`**
- Received from: `<source>`
- Received values: `<content>`
- Schema 2 compliance: sources used `<list>` / conformance YES or NO
- SA gaps: `<gap, P-level, SA — or NONE>`
- EG gaps: `<gap, P-level, EG — or NONE>`
- Produced: `<artifact contribution>`
- Naive-path delta: `<what the naive path would have done differently
  here, or "none — naive path would have produced the same output">`

For the SA-TO-SG PROMOTION, evaluate every SA gap:

**SA gap: `<text>`** (P`<level>`)
- Decision: PROMOTES TO SG / REMAINS SA
- Reason: `<one sentence>`
- Why the naive path misses this: `<one sentence — if it wouldn't miss
  it, say so explicitly and note that this reduces P-level>`

Post-promotion inventory:
> SA remaining: N. SG from promotion: N.

After all relays, write the artifact:
`simulations/trace/skill/{topic}-skill-trace-{date}.md`

List all required sections with WRITTEN status.

> Phase 2 complete — artifact written to `<path>`.
> Naive-path delta summary: N relays where trace output diverges from
> naive path. Key divergences: [brief list].

---

## Phase 3 — Diagnostic Findings

### Step 3a — Collect

Before beginning:
> Prerequisite: Phase 2 artifact exists. Check: YES. Referent: `<path>`.

List every gap. For each, ask: would the naive path surface this gap
before shipping? If yes, it is likely P3. If no, it is P1 or P2.

> Step 3a complete. Step 3b is valid to begin.

### Step 3b — Build findings table

Before beginning:
> Prerequisite: Step 3a findings exist. Check: YES. N findings.

Build the consolidated table. Action column must state a specific,
diagnostic action — not a restatement of the finding.

Diagnostic action format: start with a verb and name the failure mode
the action prevents. Example: "Add input validation contract to prevent
silent null pass-through" not "Input validation is missing."

| # | Finding | Source | Severity | Action (verb + failure mode) |
|---|---------|--------|----------|------------------------------|
|   |         |        |          |                              |

Minimum 3 rows. Minimum 2 distinct Source types. If all findings are
the same Source, the trace has not been diagnostic enough — add EG
findings from Phase 2 relay outputs.

> Step 3b complete. Step 3c is valid to begin.

### Step 3c — Gate check

Before beginning:
> Prerequisite: Step 3b table exists. Check: YES. N rows.

Check all three gates with diagnostic notes:

**G-1** (>= 2 distinct Source types):
> Sources present: [list]. Count: N.
> Diagnostic note: if only SA sources, execution was not traced deeply
> enough — revisit Phase 2 relay EG fields.
> G-1: PASS / FAIL.

**G-2** (no same-Source pair with identical Action):
> Checked all same-Source pairs.
> G-2: PASS / FAIL.

**G-3** (all Severity values in {P1, P2, P3}):
> Severity values observed: [list].
> G-3: PASS / FAIL.

If any gate fails, state:
1. The failure
2. What the naive path would have done at this gate (most likely: skipped it)
3. The specific remediation
4. The re-check result

If all gates passed first try:
> C-12 exemption applies — all gates passed on first evaluation.

Gate-clearance summary (post-remediation states):
> G-1 `<final>`, G-2 `<final>`, G-3 `<final>` — Step 3d is valid to begin.

> Step 3c complete.

### Step 3d — Verdict classification

Before beginning:
> Prerequisite: All gates PASS. Check: YES. Referent: gate-clearance
> summary (G-1 PASS, G-2 PASS, G-3 PASS).

Apply classification rules:
1. P1 SA gap remaining as SA → NEEDS-SPEC-REVISION
2. EG gaps > 3 and structural → NEEDS-REDESIGN
3. Otherwise → USEFUL

Name the rule and the classification.

Ask: would the naive path have reached this verdict? If the naive path
would have shipped USEFUL where the trace says NEEDS-REDESIGN, that
is the highest-signal finding in the entire trace. Note it.

> Step 3d complete. Phase 3 closed.

---

## Phase 4 — Amend

Phase-entry gate-clearance summary (post-remediation — not initial states):
> G-1 `<final>`, G-2 `<final>`, G-3 `<final>` — Phase 4 is valid to begin.

For each finding, write an amendment entry. Use diagnostic framing:
what failure does this amendment prevent?

**F-`<NN>`** [CHANGE / DISMISSAL]
- What: `<what was changed, or why dismissed>`
- Failure prevented: `<what would have gone wrong without this amendment>`
- Result: Updated / Dismissed

At least one entry required.

> Phase 4 complete — N amendments recorded.

---

## Phase 5 — Diagnostic Verdict

**Verdict**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

**Rationale**: `<paragraph — lead with what the naive path would have
missed, then name the specific findings that drove the classification>`

**Naive-path delta summary**: List the N highest-severity findings that
the trace surfaced and the naive path would not have. These are the
value proposition of running this skill.

**VC Compliance Ledger** (specific observed values only — no "as expected"):

| VC   | Schema   | Observed behavior                                | Result      |
|------|----------|--------------------------------------------------|-------------|
| VC-1 | Schema 1 | `<exact severity values and counts>`             | PASS / FAIL |
| VC-2 | Schema 2 | `<exact source values and counts>`               | PASS / FAIL |
| VC-3 | Schema 3 | `<lifecycle events named in observed order>`     | PASS / FAIL |
| VC-4 | Schema 4 | `<G-1, G-2, G-3 checked at Step 3c: confirmed>` | PASS / FAIL |
| VC-5 | Schema 5 | `<3a→3b→3c→3d ran in declared order: confirmed>` | PASS / FAIL |

Overall VC result: PASS / FAIL
```

---

## Variation Summary

| ID | Axis | Hypothesis | Key diff from baseline |
|----|------|-----------|----------------------|
| V-01 | Output format (table-first) | Tables make field omission structurally impossible | Every structured element is a table; no prose blocks |
| V-02 | Phrasing register (direct imperative) | Imperative commands reduce instruction-to-output cognitive gap | All instructions are "write X", "emit Y", "do not proceed until Z" |
| V-03 | Lifecycle emphasis (verbose boundaries) | Named entry/close ceremonies make phase boundaries load-bearing | Every phase and sub-step has ENTRY / CLOSE declarations |
| V-04 | Role sequence + output format | EG-first prevents spec-anchoring that suppresses execution gaps | EG roles run before SA roles; prose-led with inline tables |
| V-05 | Inertia framing + diagnostic register | Naming what naive path misses raises gap density and P-level honesty | Each phase asks "what would ship without this?"; Action = verb + failure mode |
