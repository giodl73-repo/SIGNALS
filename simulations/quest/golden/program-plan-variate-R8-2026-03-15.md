---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 8
rubric: v8
total_pts: 180
golden_threshold: 160
new_criteria: C-24, C-25, C-26
---

# program-plan — R8 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v8 (C-01 through C-26, 180 pts, golden >= 160).

**R7 retrospective under v8 rubric:**
- V-01 (Conversational/Imperative): 165/180 — C-24 FAIL (band table drives derivation; no consumer-pull rule normative); C-25 FAIL (no pre-YAML trace artifact; bilateral contracts in per-stage annotations only); C-26 FAIL (echo named as normative exception; derivation anchor role not declared)
- V-02 (R-NN Role Handoff Table): 165/180 — C-24 FAIL ("Delivers to next role" column explicit but rule not stated normatively); C-25 FAIL (role handoff table is meta-structure, not a dedicated Produces/Consumes trace artifact); C-26 FAIL (echo structural contract present; terminal consumer role not declared)
- V-03 (F-NN Failure Precondition): 165/180 — C-24 FAIL (failure lifecycle order drives derivation; consumer-pull rule not stated as normative constraint); C-25 FAIL (failure precondition table is meta-structure, not a bilateral Produces/Consumes trace); C-26 FAIL (echo "does not rule out a failure mode — normative"; derivation anchor role not declared)
- V-04 (Consumer-Pull + D-NN Displacement Chain): 180/180 — C-24 PASS ("Consumer-pull rule: `# Produces` is determined by what the NEXT stage declares as `# Consumes`"); C-25 PASS (ARTIFACT 2 backward trace worksheet lists all Produces/Consumes pairs before stage YAML); C-26 PASS ("echo is the terminal consumer; its information needs drove the entire backward derivation")
- V-05 (All R7 axes): 165/180 — C-24 FAIL (consumer-pull rule present but framed as trace instruction, not normative rule); C-25 FAIL (backward derivation trace is fill-in prose, not a dedicated Produces/Consumes worksheet artifact); C-26 FAIL (echo named as terminal consumer in echo footer but not as derivation anchor in schema)

**R8 target:** All five variants >= 180/180. C-24/C-25/C-26 are now baseline requirements. Explore fresh single-axis variations for V-01/V-02/V-03; combine in V-04/V-05.

**R7 axis coverage (reference):**

| R7 axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Phrasing register (conversational/imperative) | X | | | | X |
| Role sequence (R-NN role handoff table) | | X | | | X |
| Failure precondition (F-NN failure mode table) | | | X | | X |
| Consumer-pull backward derivation | | | | X | X |
| Inertia framing (D-NN displacement chain) | | | | X | |
| All gates quantified | | | | | X |

**R8 new axes (all carry C-24/C-25/C-26 as baseline):**

| Axis | Description |
|------|-------------|
| Lifecycle emphasis (zone-anchor) | Meta-structure is a lifecycle arc-zone table (Z-NN); backward trace is a zone transition worksheet; zone entry/exit criteria make consumer-pull mechanically visible |
| Output format (handoff-matrix table) | Backward trace is a compact matrix table — Produces and Consumes appear as adjacent columns; bilateral contracts auditable by scanning two columns |
| Phrasing register (specification-constraint language) | Formal constraint specification language (SHALL/MUST/NORMATIVE); consumer-pull rule is a named constraint (P-01); backward trace is a constraint satisfaction record |
| Inertia framing (displacement-woven) + role sequence | Displacement language woven into every gap/gate annotation, not just meta-structure; R-NN provides structural index; backward trace is a displacement proof chain |
| All R8 axes combined | Zone-anchor + handoff-matrix + constraint language + displacement + all gates quantified |

**R8 variation lineup:**

- V-01 (single): Lifecycle emphasis — arc zone table (Z-NN); zone transition worksheet as C-25 artifact
- V-02 (single): Output format — handoff matrix table; Produces/Consumes as adjacent auditable columns
- V-03 (single): Phrasing register — specification constraint language; P-01 rule; constraint satisfaction trace
- V-04 (combined): Displacement framing woven + role sequence (R-NN) + consumer-pull baseline
- V-05 (combined): All R8 axes — zone-anchor + handoff-matrix + constraint language + displacement + all gates quantified

---

## V-01 — Lifecycle Emphasis: Zone-Anchor Format (Z-NN)

**Axis:** Lifecycle emphasis — the meta-structure is an arc-zone table (Z-NN) where each zone
represents a phase of the feature's lifecycle with explicit entry and exit criteria. The backward
trace worksheet is a "Zone Transition Worksheet" organized by zone boundaries. Zone entry criteria
are exactly the prior zone's Produces, making the consumer-pull derivation visible as a structural
property of the zone table itself.

**Hypothesis:** R7 used phase bands (B-NN) or role clusters (R-NN) as meta-structure. Z-NN
formalizes phases as lifecycle zones with zone entry/exit artifact families declared in the table
itself — not just as per-stage annotations. This collapses C-14 (bilateral contracts) and C-15
(meta-structure) into a single table where the "Zone exit" column is the prior zone's Produces and
the "Zone entry" column is the next zone's Consumes, making the consumer-pull rule visually
self-evident from ARTIFACT 1. C-24 is satisfied by declaring the consumer-pull rule normatively
in the schema (ARTIFACT 0). C-25 is satisfied by generating a Zone Transition Worksheet (ARTIFACT
2) that lists every zone boundary's Produces/Consumes pair before stage YAML. C-26 is satisfied
by naming echo as the terminal consumer whose zone-entry needs anchor the backward derivation.
Anticipated score: 180/180.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

Structure the program plan around lifecycle arc zones: each zone is a phase of the feature's
existence, and the program advances the feature from one zone to the next by producing the
evidence required for zone entry. The gate is the exit criterion for the current zone —
equivalently, the entry criterion for the next zone.

Output four artifacts in this order:

0. **Stage schema template** — the five-annotation per-stage contract with consumer-pull rule
   (FIRST — before any zone table or stage YAML)
1. **Arc zone table** — the lifecycle arc as Z-NN zones with entry/exit evidence families
2. **Zone transition worksheet** — backward trace from echo's zone-entry needs to Z-01's output
3. **program.yaml** — stages derived from the zone worksheet, in execution order

---

**ARTIFACT 0 — Stage schema template**

Write this block before the arc zone table and before any stage YAML.

```
Stage Schema Template for {{topic}}

Every non-echo stage carries all five annotations:

  # Zone: Z-NN          <- back-reference to arc zone table row (the zone this stage belongs to)
  # Gap: "We don't yet know [specific question this stage answers within Z-NN's lifecycle gap]"
  # Owner: <functional role from Z-NN Owner column — PM | Architect | Dev | Team Lead>
  # Consumes: [artifact types this stage requires as input — derived from zone entry requirements]
  # Produces: [artifact types this stage yields as output — derived to satisfy the NEXT
               zone's entry requirements, as established in the zone transition worksheet]

  name: <label derived from the lifecycle gap — not "stage1", not a skill name>
  skills: [Signal skills from Z-NN namespace assignment]
  gate: "<produces artifact-types present [+ quality condition satisfying Z-NN exit criteria]>"

Consumer-pull rule: # Produces for each stage is determined by what the NEXT zone/stage
declares as # Consumes — not by the prior stage's skill output inventory. Complete the
zone transition worksheet (ARTIFACT 2) before writing any stage YAML.

Exception: the final stage (name: echo) carries no # Zone: annotation and none of the five
per-stage annotations. It carries auto: true and skills: [] instead.
Echo is the terminal consumer — its zone-entry information needs (what must exist for echo to
have meaningful retrospective content?) anchor the entire backward derivation in ARTIFACT 2.
This exception is normative — echo is outside the zone schema.
```

---

**ARTIFACT 1 — Arc zone table**

After writing the schema, declare the lifecycle arc as a sequence of named zones. Each Z-NN entry
names the phase, its lifecycle gap class, the entry evidence required from the prior zone, the
exit evidence produced for the next zone, and the namespaces the zone works in.

```
Arc Zone Table for {{topic}}

| ID   | Zone name    | Lifecycle gap class                                     | Zone entry (Consumes from prior)     | Zone exit (Produces for next)       | Owner           | Namespaces            |
|------|--------------|--------------------------------------------------------|--------------------------------------|-------------------------------------|-----------------|-----------------------|
| Z-01 | Discovery    | "We don't yet know [market/feasibility gap]"           | (none — first zone)                  | scout signal artifacts              | PM              | scout                 |
| Z-02 | Design       | "We don't yet know [design/spec gap]"                  | scout signal artifacts               | spec and prototype artifacts        | Architect       | draft, prove          |
| Z-03 | Validation   | "We don't yet know [design quality gap]"               | spec and prototype artifacts         | validated design artifacts          | Architect+Dev   | review, flow, trace   |
| Z-04 | Synthesis    | "We don't yet know [adoption/readiness gap]"           | validated design artifacts           | synthesis and readiness artifacts   | PM+Team         | listen, topic         |
```

Rules:
- Z-NN IDs are the authoritative zone identifiers; stages reference them via `# Zone: Z-NN`
- "Zone exit" column names the artifact family this zone produces — it becomes the next zone's
  "Zone entry" (this is the consumer-pull rule made structurally visible: zone exit = next
  zone's Consumes)
- Namespace column is MECE: every namespace used in any stage appears in exactly one Z-NN row;
  no namespace in two rows; no used namespace unassigned
- Gap class uses gap-language: "We don't yet know [X]" — not task-language
- Only include zones applicable to {{topic}} and {{strategy}}
- Write AFTER ARTIFACT 0, BEFORE zone transition worksheet and stage YAML

---

**ARTIFACT 2 — Zone transition worksheet**

Before writing stage YAML, complete this worksheet. It makes every stage-boundary Produces/Consumes
pair independently auditable from a single artifact — a reader can verify bilateral contracts
by reading this worksheet alone, without scanning stage YAML.

```
Zone Transition Worksheet for {{topic}}

Echo (terminal consumer — derivation anchor):
  Echo's zone-entry need: [What artifact families must exist for echo to assess what was
                           learned? What would give echo meaningful retrospective content?]
  Echo implicitly Consumes: [artifact types — this is the seed of the backward derivation]

Working backward from echo to Z-01:

  Zone boundary Z-04 -> echo:
    Z-04 final Produces:  [artifact types — SHALL equal echo's implicit Consumes above]
    echo Consumes:        [same artifact types — bilateral contract at this boundary]
    Z-04 gate:            [evidence state proving Z-04 produced the required artifacts]

  Zone boundary Z-03 -> Z-04:
    Z-03 final Produces:  [artifact types — SHALL equal Z-04's first Consumes]
    Z-04 first Consumes:  [same artifact types — bilateral contract at this boundary]
    Z-03 gate:            [evidence state; numeric threshold preferred: >=N or =0 findings]

  Zone boundary Z-02 -> Z-03:
    Z-02 final Produces:  [artifact types — SHALL equal Z-03's first Consumes]
    Z-03 first Consumes:  [same artifact types — bilateral contract at this boundary]
    Z-02 gate:            [evidence state]

  Zone boundary Z-01 -> Z-02:
    Z-01 final Produces:  [artifact types — SHALL equal Z-02's first Consumes]
    Z-02 first Consumes:  [same artifact types — bilateral contract at this boundary]
    Z-01 gate:            [evidence state; numeric threshold preferred]

  Z-01 entry:
    Z-01 first Consumes:  [] (first zone — no prior zone)
```

Fill in all bracketed fields using {{topic}} and {{strategy}} before writing stage YAML. The
stage YAML is a transcription of this worksheet — every `# Produces:` and `# Consumes:` value
in stage YAML SHALL match the corresponding worksheet entry.

---

**ARTIFACT 3 — program.yaml**

Transcribe the zone transition worksheet into forward-ordered stage YAML. Each stage's `# Produces:`
and `# Consumes:` were established in ARTIFACT 2.

For each zone Z-NN, write 1-3 stages. Each stage is an instance of the schema in ARTIFACT 0 that
closes a sub-gap within Z-NN's lifecycle gap class.

```yaml
# ARTIFACT 3: program.yaml for {{topic}}
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # === Zone Z-01: Discovery ===
    # Zone gap: "We don't yet know [Z-01 lifecycle gap class]"
    - name: <lifecycle-gap-derived label>
      # Zone: Z-01
      # Gap: "We don't yet know [specific sub-question within Z-01's lifecycle gap]"
      # Owner: PM
      # Consumes: []
      # Produces: [artifact types — from Z-01 row of zone transition worksheet]
      skills: [...]
      gate: "<produces artifact-types present [+ Z-01 exit quality condition]>"

    # === Zone boundary Z-01 -> Z-02 ===
    # Z-01 final Produces: [artifact types — from zone transition worksheet]
    # Z-02 first Consumes: [same artifact types — bilateral contract confirmed]

    - name: <lifecycle-gap-derived label>
      # Zone: Z-02
      # Gap: "We don't yet know [specific sub-question within Z-02's lifecycle gap]"
      # Owner: Architect
      # Consumes: [artifact types from Z-01 Produces — from zone transition worksheet]
      # Produces: [artifact types — from Z-02 row of zone transition worksheet]
      skills: [...]
      gate: "<produces artifact-types present [+ Z-02 exit quality condition]>"

    # [continue for Z-03, Z-04]

    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

**Single-referent rule (C-17):** For every non-echo stage, `# Gap:`, `# Produces:`, and `gate:`
describe the same lifecycle evidence claim from three angles:
- "We don't yet know [X]" — the gap
- "artifact-A and artifact-B proving [X]" — what this stage produces
- "artifact-A and artifact-B present [+ quality condition]" — the gate

Changing the artifact name in `# Produces:` forces revision of both the gate and the gap.
If those three can drift independently, they describe three separate things instead of three
views of one claim.

**Quantified gate requirement (C-10):** At least one gate must carry a numeric threshold:
`">=2 Z-01 artifacts with no blocking gaps"` or `"0 P0 findings in Z-03 validation artifacts"`.

---

**Available Signal skills**

| Namespace | Skills |
|-----------|--------|
| scout     | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft     | spec, proposal, pitch |
| review    | design, code, users, customers |
| prove     | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow      | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace     | request, state, contract, component, deployment, migration, permissions |
| listen    | feedback, support, adoption |
| topic     | status, report |

Namespace dependency order: scout -> draft -> review/prove -> flow/trace -> listen -> topic.
A stage cannot consume artifacts that no earlier stage has produced.

---

**Echo (do not modify)**

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn that we didn't expect?"
```

Echo carries no `# Zone:` annotation. This is the normative exception declared in ARTIFACT 0.
Echo is the terminal consumer — its zone-entry needs seeded the entire backward derivation in
ARTIFACT 2.

---

**Completeness check:**
- [ ] ARTIFACT 0 (schema template) written FIRST — before arc zone table and stage YAML (C-23);
      names all five annotations + consumer-pull rule + echo exception as normative (C-21, C-22, C-24)
- [ ] Arc zone table (ARTIFACT 1): Z-NN IDs, zone entry/exit columns, MECE namespace column (C-15, C-20)
- [ ] Zone transition worksheet (ARTIFACT 2): every Z-NN boundary's Produces/Consumes pair listed
      in sequence before stage YAML; echo named as terminal consumer / derivation anchor (C-25, C-26)
- [ ] Every non-echo stage has all five annotations simultaneously (C-18, C-19)
- [ ] Gap, Produces, Gate describe the same lifecycle gap claim — single referent (C-17)
- [ ] Stage N Produces = Stage N+1 Consumes at every boundary (C-14)
- [ ] At least one gate quantified with numeric threshold (C-10)
- [ ] Echo: last, `skills: []`, `auto: true`, no `# Zone:` annotation (C-02)

---

## V-02 — Output Format: Handoff-Matrix Table as Primary Derivation Artifact

**Axis:** Output format — the backward trace worksheet IS a compact matrix table where Produces
and the next stage's Consumes appear as adjacent columns in the same row. A reader can audit
every bilateral contract by scanning two columns of a single table, without reading stage YAML
or cross-referencing sections. Echo is row 0 of the matrix (since derivation runs backward, echo
is at the top). The matrix is filled backward from row 0 and transcribed forward into YAML.

**Hypothesis:** V-04 from R7 and V-01 of R8 use a prose fill-in-the-blank block for the backward
trace. A table format makes the Produces/Consumes pairing visually structural: adjacent columns
in the same row are provably equal (Produces of row N = Consumes of row N+1), not just asserted
equal in prose. This is the strongest form of C-25 — the audit surface is the table's column
alignment, not a prose reading. C-24 is satisfied by stating the consumer-pull rule in ARTIFACT 0
with an explicit note that the handoff matrix enforces it structurally. C-26 is satisfied by
naming echo as row 0 of the matrix (the seed row) and the terminal consumer in ARTIFACT 0.
Anticipated score: 180/180.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

Build the program plan in two phases: derive first, transcribe second. Derivation runs backward
from echo through a handoff matrix table — filling in one row at a time from echo (row 0)
backward to the first stage. Transcription reads the matrix forward into stage YAML. The matrix
is the authoritative artifact; the YAML is its transcription.

Output four artifacts in this order:

0. **Stage schema** — five-annotation per-stage contract with consumer-pull rule (FIRST)
1. **Band taxonomy** — investigation arc as phase bands (B-NN IDs) with MECE namespace column
2. **Handoff matrix** — backward-derivation table from echo (row 0) to B-01 (last row); one
   row per stage; Produces and next-stage Consumes appear as adjacent auditable columns
3. **program.yaml** — stages transcribed from the handoff matrix, in execution order

---

**ARTIFACT 0 — Stage schema (write before band taxonomy and handoff matrix)**

```
Stage Schema for {{topic}}

Every non-echo stage carries all five annotations:

  # Band: B-NN          <- back-reference to band taxonomy row
  # Gap: "We don't yet know [specific sub-question this stage answers within B-NN]"
  # Owner: <functional role from B-NN Owner column — PM | Architect | Dev | Team Lead>
  # Consumes: [artifact types this stage requires as input]
  # Produces: [artifact types this stage yields as output]

  name: <label derived from the gap question — not "stage1", not a skill name>
  skills: [Signal skills from B-NN namespace assignment]
  gate: "<produces artifact-types present [+ quality condition]>"

Consumer-pull rule: # Produces for each stage is determined entirely by what the NEXT stage
declares as # Consumes — not by the prior stage's skill output inventory. The handoff matrix
(ARTIFACT 2) enforces this structurally: each row's Produces column is filled from the
consuming row above it. No stage's Produces may be written independently of its consumer's
Consumes.

Exception: the final stage (name: echo) carries no # Band: annotation and none of the five
per-stage annotations. It carries auto: true and skills: [] instead.
Echo is the terminal consumer — it is row 0 of the handoff matrix, and its implicit information
needs seed the backward derivation for every prior stage. This exception is normative — echo
is outside the band schema.
```

---

**ARTIFACT 1 — Band taxonomy**

After the schema, declare the investigation arc as phase bands. The band taxonomy partitions
Signal namespaces into a MECE investigation arc.

```
Band Taxonomy for {{topic}}

| ID   | Band name    | Investigation gap class                                   | Owner           | Namespaces            |
|------|--------------|-----------------------------------------------------------|-----------------|-----------------------|
| B-01 | Discovery    | "We don't yet know [market/feasibility gap for topic]"    | PM              | scout                 |
| B-02 | Design       | "We don't yet know [design/spec gap for topic]"           | Architect       | draft, prove          |
| B-03 | Validation   | "We don't yet know [design quality gap for topic]"        | Architect+Dev   | review, flow, trace   |
| B-04 | Synthesis    | "We don't yet know [adoption/readiness gap for topic]"    | PM+Team         | listen, topic         |
```

Rules:
- Namespace column is MECE: every namespace used in any stage appears in exactly one B-NN row;
  no namespace in two rows; no used namespace unassigned
- Gap class uses gap-language: "We don't yet know [X]"
- Only include bands applicable to {{topic}} and {{strategy}}
- Write AFTER ARTIFACT 0, BEFORE handoff matrix and stage YAML

---

**ARTIFACT 2 — Handoff matrix (backward-derivation table)**

Before writing stage YAML, build this table. It is the sole pre-YAML artifact making every
stage boundary's bilateral Produces/Consumes contract independently verifiable.

**How to fill in the matrix (backward from echo):**
1. Fill row 0 (echo): in the "Consumes (implicit)" cell, write what artifact families echo needs
   for meaningful retrospective content.
2. Fill each subsequent row's **Produces** cell by copying the Consumes of the row above it.
3. Fill each subsequent row's **Consumes** cell from the Produces of the row below it (or [] for
   the first stage row).
4. If a band has multiple stages, insert intermediate rows and chain Produces/Consumes through each.

**Audit rule:** A reader can verify all bilateral contracts by checking that every row's
**Produces** cell equals the **Consumes** cell of the row above it. No stage YAML reading required.

```
Handoff Matrix for {{topic}}
(Fill backward from row 0; transcribe to YAML reading downward from the last row)

Consumer-pull rule in effect: Produces(row N) is derived from Consumes(row N-1 above it).

| Row | Stage name             | Band | Gap (sub-question this stage answers)              | Produces                              | Consumes (next stage, row above)       | Gate condition                       | Owner     |
|-----|------------------------|------|----------------------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|-----------|
| 0   | echo (terminal anchor) | —    | [What must exist for echo to have content?]        | —                                     | [echo's implicit Consumes — seed here] | auto: true                           | —         |
| 4   | <synthesis stage>      | B-04 | "We don't yet know [B-04 sub-gap]"                 | [= row 0 Consumes — fill from above]  | [what B-04 needs from B-03]            | [quality condition, threshold if +]  | PM+Team   |
| 3   | <validation stage>     | B-03 | "We don't yet know [B-03 sub-gap]"                 | [= row 4 Consumes — fill from above]  | [what B-03 needs from B-02]            | [quality condition]                  | Arch+Dev  |
| 2   | <design stage>         | B-02 | "We don't yet know [B-02 sub-gap]"                 | [= row 3 Consumes — fill from above]  | [what B-02 needs from B-01]            | [quality condition]                  | Architect |
| 1   | <discovery stage>      | B-01 | "We don't yet know [B-01 sub-gap]"                 | [= row 2 Consumes — fill from above]  | [] (first stage)                       | [>=N threshold preferred]            | PM        |
```

After filling the matrix, verify: Produces(row N) = Consumes(row N-1) at every adjacent pair.

---

**ARTIFACT 3 — program.yaml**

Transcribe the handoff matrix from bottom to top (row 1 first, then 2, 3, 4, then echo). Every
annotation value SHALL match the corresponding matrix cell.

```yaml
# ARTIFACT 3: program.yaml for {{topic}}
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # === Band B-01: Discovery (Matrix row 1) ===
    - name: <gap-derived label from matrix row 1>
      # Band: B-01
      # Gap: "We don't yet know [B-01 sub-gap from matrix row 1]"
      # Owner: PM
      # Consumes: []
      # Produces: [from matrix row 1 Produces column]
      skills: [...]
      gate: "<produces artifact-types present [+ numeric threshold]>"

    # === Band boundary B-01 -> B-02 ===
    # B-01 final Produces: [from matrix — bilateral contract]
    # B-02 first Consumes: [same artifacts — from matrix]

    - name: <gap-derived label from matrix row 2>
      # Band: B-02
      # Gap: "We don't yet know [B-02 sub-gap from matrix row 2]"
      # Owner: Architect
      # Consumes: [matrix row 1 Produces = row 2 Consumes]
      # Produces: [from matrix row 2 Produces column]
      skills: [...]
      gate: "<produces artifact-types present>"

    # [continue for B-03, B-04]

    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

**Single-referent rule (C-17):** Each matrix row's Gap, Produces, and Gate describe the same
evidence claim. Changing the artifact type in Produces forces updates to both the Gate (which
checks for it) and the Gap (which names the question those artifacts answer).

**Quantified gate requirement (C-10):** At least one stage gate must carry a numeric threshold.

---

**Available Signal skills**

| Namespace | Skills |
|-----------|--------|
| scout     | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft     | spec, proposal, pitch |
| review    | design, code, users, customers |
| prove     | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow      | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace     | request, state, contract, component, deployment, migration, permissions |
| listen    | feedback, support, adoption |
| topic     | status, report |

Namespace dependency order: scout -> draft -> review/prove -> flow/trace -> listen -> topic.

---

**Echo (do not modify)**

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn that we didn't expect?"
```

Echo carries no `# Band:` annotation. This is the normative exception declared in ARTIFACT 0.
Echo is the terminal consumer — row 0 of the handoff matrix, the seed of the backward derivation.

---

**Completeness check:**
- [ ] ARTIFACT 0 (schema) written FIRST — before band taxonomy and handoff matrix (C-23); names
      all five annotations + consumer-pull rule + echo exception as normative (C-21, C-22, C-24)
- [ ] Band taxonomy (ARTIFACT 1): B-NN IDs, MECE namespace column (C-15, C-20)
- [ ] Handoff matrix (ARTIFACT 2): every boundary's Produces/Consumes pair as adjacent columns;
      echo is row 0 as the terminal consumer and derivation seed; completed before YAML (C-25, C-26)
- [ ] Every non-echo stage has all five annotations simultaneously (C-18, C-19)
- [ ] Gap, Produces, Gate are three angles on the same evidence claim (C-17)
- [ ] Stage N Produces = Stage N+1 Consumes at every boundary (C-14)
- [ ] At least one gate quantified with numeric threshold (C-10)
- [ ] Echo: last, `skills: []`, `auto: true`, no `# Band:` annotation (C-02)

---

## V-03 — Phrasing Register: Specification-Constraint Language (P-NN Constraints)

**Axis:** Phrasing register — formal specification constraint language throughout: SHALL, MUST,
REQUIRED, NORMATIVE. The meta-structure is a band registry (B-NN). The consumer-pull rule is a
named normative constraint (P-01). The echo exception is a named constraint (P-02). The backward
trace is a "Constraint Satisfaction Trace" that constitutes a compliance record for P-01. This
is the most formal register of any variant so far.

**Hypothesis:** Previous variants use imperative ("write this block") or annotation-schema
register. Specification language is the register where constraint rules are native: "SHALL be
derived exclusively from" is stronger than "is determined by." The consumer-pull rule as P-01
makes C-24 maximally explicit. The constraint satisfaction trace as a named compliance record
for P-01 makes C-25 explicitly purposeful — it is not just a design artifact but a verification
record. C-26 is satisfied by P-02 naming echo as the terminal consumer from which the P-01
constraint is initialized. Anticipated score: 180/180.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

Construct the program plan as a constraint-compliant artifact. Every stage SHALL carry five
required annotations. Every stage transition SHALL satisfy bilateral contract constraints. The
full Produces/Consumes chain SHALL be derivable from the terminal consumer backward, as
established by the constraint specification before any plan-specific content is written.

Output four artifacts in this order:

0. **Constraint specification** — normative schema, derivation constraints P-01 and P-02
   (FIRST — before any meta-structure or stage content)
1. **Investigation band registry** — phase taxonomy with MECE namespace assignments (B-NN IDs)
2. **Constraint satisfaction trace** — the P-01 compliance record; every boundary's
   Produces/Consumes pair in sequence; echo as P-02 initialization point
3. **program.yaml** — the compliant plan, derived from the satisfaction trace

---

**ARTIFACT 0 — Constraint specification (write before any meta-structure or stage content)**

```
Constraint Specification for {{topic}}

ANNOTATION SCHEMA — every non-echo stage SHALL carry all five annotations:

  # Band: B-NN     REQUIRED: back-reference to band registry row (phase cluster identifier)
  # Gap: "..."     REQUIRED: "We don't yet know [specific sub-question this stage answers]"
  # Owner: ...     REQUIRED: functional role (PM | Architect | Dev | Team Lead)
  # Consumes: [...] REQUIRED: artifact types this stage requires as input (array, may be [])
  # Produces: [...] REQUIRED: artifact types this stage yields as output (non-empty array)

  name: REQUIRED — human-readable label derived from the Gap question (not "stage1")
  skills: REQUIRED — Signal plugin skills from B-NN namespace assignment
  gate: REQUIRED — evidence-state condition; NOT a task-completion check

DERIVATION CONSTRAINT P-01 (NORMATIVE):
  The # Produces annotation of each stage SHALL be derived exclusively from what the
  immediately following stage declares as # Consumes. The prior stage's capability
  inventory or skill output set is NOT a valid source for # Produces derivation.
  This constraint enforces consumer-pull derivation direction throughout the plan.
  Compliance SHALL be demonstrated in the constraint satisfaction trace (ARTIFACT 2),
  which MUST be completed before any stage YAML is written.

ECHO EXCEPTION P-02 (NORMATIVE):
  The stage named "echo" SHALL NOT carry the # Band: annotation or any of the five
  required annotations above. It SHALL carry auto: true and skills: [] only.
  Echo is the TERMINAL CONSUMER: its information needs are the initialization input
  for the P-01 constraint satisfaction trace in ARTIFACT 2. The trace SHALL begin
  by identifying echo's implicit Consumes and then derive each prior stage's Produces
  backward through the band registry. A plan that applies the P-01 constraint without
  naming echo as the initialization point does not fully satisfy P-02.
  This exception is normative — echo is outside the annotation schema.
```

---

**ARTIFACT 1 — Investigation band registry**

After the constraint specification, declare the investigation phase taxonomy. Each B-NN entry
assigns a namespace cluster to a named investigation phase.

```
Investigation Band Registry for {{topic}}

| ID   | Band name    | Investigation gap class                                      | Owner           | Namespaces (MECE assignment)  |
|------|--------------|--------------------------------------------------------------|-----------------|-------------------------------|
| B-01 | Discovery    | "We don't yet know [market/feasibility gap for {{topic}}]"   | PM              | scout                         |
| B-02 | Design       | "We don't yet know [design/spec gap for {{topic}}]"          | Architect       | draft, prove                  |
| B-03 | Validation   | "We don't yet know [design quality gap for {{topic}}]"       | Architect+Dev   | review, flow, trace           |
| B-04 | Synthesis    | "We don't yet know [adoption/readiness gap for {{topic}}]"   | PM+Team         | listen, topic                 |
```

MECE CONSTRAINT (per ANNOTATION SCHEMA): Every namespace used in any stage YAML entry SHALL
appear in exactly one B-NN row. No namespace SHALL be assigned to two rows. No namespace used
in stage skills SHALL be absent from the registry.

Omit bands not applicable to {{topic}} and {{strategy}}.
Write AFTER ARTIFACT 0, BEFORE constraint satisfaction trace and stage YAML.

---

**ARTIFACT 2 — Constraint satisfaction trace**

REQUIRED before writing stage YAML. This artifact constitutes the compliance record for
DERIVATION CONSTRAINT P-01. It lists every stage-boundary Produces/Consumes pair in sequence,
with echo as the P-02 initialization point, making all bilateral contracts independently
verifiable from this single artifact without reading stage YAML.

```
Constraint Satisfaction Trace for {{topic}}
(P-01 compliance record — demonstrates consumer-pull derivation at every boundary)

P-02 INITIALIZATION — Echo as terminal consumer:
  Echo's implicit Consumes: [What artifact families must exist for echo to produce meaningful
                             retrospective content? This is the P-01 derivation seed.]

P-01 BACKWARD DERIVATION — each stage's Produces derived from its consumer's Consumes:

  Boundary B-04 -> echo (P-01 application):
    B-04 final Produces:   [artifact types — SHALL equal echo's implicit Consumes above]
    echo Consumes:         [same artifact types — P-01 satisfied at this boundary: YES/NO]
    B-04 gate condition:   [evidence state proving B-04 Produces are present]

  Boundary B-03 -> B-04 (P-01 application):
    B-03 final Produces:   [artifact types — SHALL equal B-04's first Consumes]
    B-04 first Consumes:   [same artifact types — P-01 satisfied at this boundary: YES/NO]
    B-03 gate condition:   [evidence state; numeric threshold preferred: >=N or =0 findings]

  Boundary B-02 -> B-03 (P-01 application):
    B-02 final Produces:   [artifact types — SHALL equal B-03's first Consumes]
    B-03 first Consumes:   [same artifact types — P-01 satisfied at this boundary: YES/NO]
    B-02 gate condition:   [evidence state]

  Boundary B-01 -> B-02 (P-01 application):
    B-01 final Produces:   [artifact types — SHALL equal B-02's first Consumes]
    B-02 first Consumes:   [same artifact types — P-01 satisfied at this boundary: YES/NO]
    B-01 gate condition:   [evidence state; numeric threshold preferred]

  B-01 entry — P-01 constraint not applicable (first stage, no prior stage):
    B-01 first Consumes:   []

P-01 COMPLIANCE STATUS: [ ] All boundaries satisfied — Produces(N) = Consumes(N+1) verified
```

Fill in all bracketed fields using {{topic}} and {{strategy}} before proceeding to stage YAML.

---

**ARTIFACT 3 — program.yaml**

Transcribe the constraint satisfaction trace into forward-ordered stage YAML. Every stage's
`# Produces:` and `# Consumes:` SHALL match the values established in ARTIFACT 2.

```yaml
# ARTIFACT 3: program.yaml for {{topic}}
# Derived from constraint satisfaction trace (ARTIFACT 2)
# All stages comply with Constraint Specification (ARTIFACT 0)
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # === Band B-01: Discovery ===
    - name: <gap-derived label>
      # Band: B-01
      # Gap: "We don't yet know [specific B-01 sub-question from band registry]"
      # Owner: PM
      # Consumes: []
      # Produces: [from B-01 boundary in constraint satisfaction trace]
      skills: [...]
      gate: "<produces artifact-types present [+ numeric threshold per trace]>"

    # === Band boundary B-01 -> B-02 — P-01 compliant ===
    # B-01 final Produces: [artifacts from trace]
    # B-02 first Consumes: [same artifacts — P-01 satisfied]

    - name: <gap-derived label>
      # Band: B-02
      # Gap: "We don't yet know [specific B-02 sub-question from band registry]"
      # Owner: Architect
      # Consumes: [from trace: B-01 Produces = B-02 Consumes]
      # Produces: [from B-02 boundary in constraint satisfaction trace]
      skills: [...]
      gate: "<produces artifact-types present>"

    # [continue for B-03, B-04]

    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

**Single-referent requirement (C-17):** For every non-echo stage, the Gap, Produces, and Gate
SHALL describe the same underlying evidence claim. The practical test: modifying the artifact
type in `# Produces:` SHALL force revision of both the gate (which tests for it) and the gap
(which frames the question those artifacts answer). If they can drift independently, they are
three separate constructs rather than three surfaces of one claim.

---

**Available Signal skills**

| Namespace | Skills |
|-----------|--------|
| scout     | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft     | spec, proposal, pitch |
| review    | design, code, users, customers |
| prove     | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow      | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace     | request, state, contract, component, deployment, migration, permissions |
| listen    | feedback, support, adoption |
| topic     | status, report |

Namespace dependency order: scout -> draft -> review/prove -> flow/trace -> listen -> topic.
A stage SHALL NOT consume artifacts that no earlier stage has produced.

---

**Echo (do not modify)**

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn that we didn't expect?"
```

Echo carries no `# Band:` annotation. This is ECHO EXCEPTION P-02, declared normatively in
ARTIFACT 0. Echo is the terminal consumer — P-02 establishes that the P-01 constraint
satisfaction trace SHALL be initialized from echo's implicit information needs.

---

**Completeness check:**
- [ ] ARTIFACT 0 (constraint specification) written FIRST — before band registry and trace (C-23);
      declares five-annotation schema + P-01 consumer-pull constraint + P-02 echo exception as
      normative; names echo as terminal consumer and P-01 initialization point (C-21, C-22, C-24, C-26)
- [ ] Band registry (ARTIFACT 1): B-NN IDs, MECE namespace assignments declared explicitly (C-15, C-20)
- [ ] Constraint satisfaction trace (ARTIFACT 2): every boundary's Produces/Consumes pair listed
      as P-01 compliance record; echo named as P-02 initialization; completed before YAML (C-25)
- [ ] Every non-echo stage has all five annotations simultaneously (C-18, C-19)
- [ ] Gap, Produces, Gate describe the same evidence claim per stage (C-17)
- [ ] Stage N Produces = Stage N+1 Consumes at every boundary (C-14)
- [ ] At least one gate carries a numeric threshold (C-10)
- [ ] Echo: last, `skills: []`, `auto: true`, no `# Band:` annotation (C-02)

---

## V-04 — Combined: Displacement Framing (woven) + Role Sequence (R-NN) + Consumer-Pull

**Axes:**
1. **Inertia framing (woven into every annotation):** The status quo is named in the preamble.
   Every stage's gap question is displacement-anchored ("We can't yet prove we beat [status quo]
   at X"). Every gate is phrased as displacement evidence. Not just the meta-structure but every
   annotation is infused with displacement language.
2. **Role sequence (R-NN):** The meta-structure is a role handoff table where each R-NN entry is
   a functional owner responsible for producing displacement evidence in their domain.
3. **Consumer-pull baseline (C-24/C-25/C-26):** Full backward trace as ARTIFACT 2; consumer-pull
   rule stated normatively in schema; echo as terminal consumer and derivation anchor.

**Hypothesis:** R7 V-04 combined displacement chain (D-NN) and consumer-pull — D-NN was both the
structural index and the inertia framing mechanism. This variant separates the two: R-NN provides
the structural index (who owns what phase); displacement language is the mandatory annotation
content format (the gap is always "we can't yet prove we beat [status quo] at X"). This achieves
stronger C-12/C-16 (role ownership per stage, every stage) while maintaining the C-24/C-25/C-26
baseline. The displacement framing also strengthens C-13/C-17: "we can't yet prove we beat X at Y"
(gap) / "artifacts proving we beat X at Y" (produces) / "artifacts present [quality threshold]"
(gate) are three tighter surfaces of one claim than generic "we don't yet know" language.
Anticipated score: 180/180.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

Build the program as a displacement proof: every stage produces evidence that the proposed
feature beats the status quo at a specific claim. The program is not complete until echo has
received evidence of displacement across every lifecycle phase. The plan runs backward from
echo's displacement summary needs and forward into stage execution.

Output four artifacts in this order:

0. **Stage schema template** — five-annotation contract with displacement gap format and
   consumer-pull rule (FIRST — before role table or stage YAML)
1. **Role handoff table** — who owns each displacement phase; what displacement evidence they
   deliver to the next role (R-NN IDs)
2. **Displacement backward trace** — consumer-pull derivation from echo's needs backward
   through R-04 to R-01; every boundary's Produces/Consumes pair listed
3. **program.yaml** — stages in execution order, derived from the backward trace

---

**ARTIFACT 0 — Stage schema template**

Write this block before the role handoff table and before any stage YAML.

```
Stage Schema Template for {{topic}}

Status quo for {{topic}}: [name the status quo — what teams do today without this feature,
or what existing approach this feature displaces]

Every non-echo stage carries all five annotations:

  # Role: R-NN          <- back-reference to role handoff table row
  # Gap: "We can't yet prove we beat [status quo] at [specific displacement sub-claim]"
  # Owner: <functional role from R-NN Owner column — PM | Architect | Dev | Team Lead>
  # Consumes: [artifact types this stage requires — prior role's displacement evidence]
  # Produces: [displacement evidence artifacts — derived from what the NEXT stage needs
               as input to make its displacement case, NOT from this stage's skill inventory]

  name: <label derived from the displacement sub-claim — not "stage1", not a skill name>
  skills: [Signal skills from R-NN namespace assignment]
  gate: "<displacement evidence present [+ quality condition proving the sub-claim is closed]>"

Consumer-pull rule: # Produces for each stage is determined by what the NEXT stage declares
as # Consumes. The prior stage's skill inventory is not a valid derivation source for #
Produces. Complete the displacement backward trace (ARTIFACT 2) from echo's needs before
writing any stage YAML.

Exception: the final stage (name: echo) carries no # Role: annotation and none of the five
per-stage annotations. It carries auto: true and skills: [] instead.
Echo is the terminal consumer of all displacement evidence — its information needs (what would
give echo a complete picture of whether the feature displaced the status quo?) anchor the
entire backward derivation in ARTIFACT 2. This exception is normative — echo is outside the
role schema.
```

---

**ARTIFACT 1 — Role handoff table**

After the schema, declare who owns each displacement phase. Each R-NN row defines a functional
owner responsible for producing displacement evidence in their domain.

```
Role Handoff Table for {{topic}}

Status quo: [restate the status quo in one line]

| ID   | Owner           | Displacement phase  | Gap class                                                             | Namespaces            | Displacement evidence -> next role |
|------|-----------------|---------------------|-----------------------------------------------------------------------|-----------------------|------------------------------------|
| R-01 | PM              | Market viability    | "We can't yet prove we beat [SQ] at market viability/feasibility"     | scout                 | Viability evidence -> R-02         |
| R-02 | Architect       | Design proof        | "We can't yet prove we beat [SQ] at design/spec quality"              | draft, prove          | Design evidence -> R-03            |
| R-03 | Architect+Dev   | Technical proof     | "We can't yet prove we beat [SQ] at technical validation"             | review, flow, trace   | Technical evidence -> R-04         |
| R-04 | PM+Team         | Adoption proof      | "We can't yet prove we beat [SQ] at adoption/readiness"               | listen, topic         | Adoption evidence -> echo          |
```

Rules:
- Gap class uses displacement-anchored language throughout: "We can't yet prove we beat [status
  quo] at [X]" — not generic gap-language
- "Displacement evidence -> next role" column names what crosses the role boundary; this feeds
  directly into ARTIFACT 2's backward trace
- Namespace column is MECE: every namespace used in any stage appears in exactly one R-NN row;
  no overlap; no used namespace unassigned
- Only include role rows applicable to {{topic}} and {{strategy}}
- Write AFTER ARTIFACT 0, BEFORE displacement backward trace and stage YAML

---

**ARTIFACT 2 — Displacement backward trace**

Before writing stage YAML, complete this trace. It establishes every stage boundary's
Produces/Consumes pair in sequence, making bilateral displacement contracts auditable from
this single artifact without scanning stage YAML.

```
Displacement Backward Trace for {{topic}}

Echo (terminal consumer — displacement summary anchor):
  Echo's implicit Consumes: [What displacement evidence families must exist for echo to assess
                             whether the feature successfully displaced the status quo?
                             — this is the seed of the backward derivation]

Working backward from echo through role clusters:

  R-04 (adoption proof) -> echo:
    R-04 must Produce:      [artifact types = echo's implicit Consumes — displacement evidence
                             proving adoption/readiness over status quo]
    echo Consumes:          [same artifact types — bilateral contract at this boundary]
    R-04 gate condition:    [evidence state proving R-04 displacement; numeric threshold preferred]
    R-04 first Consumes:    [what must R-04 receive from R-03's final stage?]

  R-03 (technical proof) -> R-04:
    R-03 must Produce:      [artifact types = R-04's first Consumes — technical displacement
                             evidence proving design beats status quo at validation]
    R-04 first Consumes:    [same artifact types — bilateral contract at this boundary]
    R-03 gate condition:    [evidence state; numeric threshold: >=N artifacts or =0 P0 findings]
    R-03 first Consumes:    [what must R-03 receive from R-02's final stage?]

  R-02 (design proof) -> R-03:
    R-02 must Produce:      [artifact types = R-03's first Consumes — design displacement
                             evidence proving spec beats status quo at design quality]
    R-03 first Consumes:    [same artifact types — bilateral contract at this boundary]
    R-02 gate condition:    [evidence state proving R-02 displacement]
    R-02 first Consumes:    [what must R-02 receive from R-01's final stage?]

  R-01 (market viability) -> R-02:
    R-01 must Produce:      [artifact types = R-02's first Consumes — viability displacement
                             evidence proving feasibility/market over status quo]
    R-02 first Consumes:    [same artifact types — bilateral contract at this boundary]
    R-01 gate condition:    [evidence state; numeric threshold preferred: >=N scout artifacts]
    R-01 first Consumes:    [] (first role — no prior role)

Bilateral contract audit (verify before proceeding to stage YAML):
  [ ] R-01 Produces = R-02 Consumes?
  [ ] R-02 Produces = R-03 Consumes?
  [ ] R-03 Produces = R-04 Consumes?
  [ ] R-04 Produces = echo Consumes?
```

Fill in all bracketed fields using {{topic}} and {{strategy}} before proceeding to stage YAML.

---

**ARTIFACT 3 — program.yaml**

Transcribe the displacement backward trace into forward-ordered stage YAML. Each stage's
displacement gap, Produces, and gate were established in ARTIFACT 2.

```yaml
# ARTIFACT 3: program.yaml for {{topic}}
# Displacement proof — every stage closes a displacement sub-claim
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # === Role R-01: PM / Market viability ===
    # Displacement goal: prove we beat [status quo] at market/feasibility
    - name: <displacement-claim label>
      # Role: R-01
      # Gap: "We can't yet prove we beat [status quo] at [specific R-01 sub-claim]"
      # Owner: PM
      # Consumes: []
      # Produces: [displacement evidence from R-01 row of backward trace]
      skills: [...]
      gate: "<displacement evidence present [+ numeric threshold]>"

    # === Role boundary R-01 -> R-02 ===
    # R-01 final Produces: [displacement artifacts from trace]
    # R-02 first Consumes: [same displacement artifacts — bilateral contract]

    - name: <displacement-claim label>
      # Role: R-02
      # Gap: "We can't yet prove we beat [status quo] at [specific R-02 sub-claim]"
      # Owner: Architect
      # Consumes: [from R-01 displacement trace]
      # Produces: [displacement evidence from R-02 row of backward trace]
      skills: [...]
      gate: "<displacement evidence present>"

    # [continue for R-03, R-04]

    - name: echo
      skills: []
      auto: true
      question: "What did we learn — and did we actually displace the status quo?"
```

**Displacement single-referent rule (C-17):** `# Gap:`, `# Produces:`, and `gate:` describe
the same displacement claim:
- "We can't yet prove we beat [status quo] at X" — the gap
- "artifact-A and artifact-B proving we beat [status quo] at X" — what we produce
- "artifact-A and artifact-B present [quality condition]" — the gate

Changing the artifact in `# Produces:` forces updating both the gap (the claim being closed)
and the gate (the evidence test).

**Quantified gate requirement (C-10):** At least one gate must carry a numeric threshold:
`">=2 scout-* artifacts with no P0 blockers"` or `"0 unresolved P0 findings in review"`.

---

**Available Signal skills**

| Namespace | Skills |
|-----------|--------|
| scout     | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft     | spec, proposal, pitch |
| review    | design, code, users, customers |
| prove     | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow      | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace     | request, state, contract, component, deployment, migration, permissions |
| listen    | feedback, support, adoption |
| topic     | status, report |

Namespace dependency order: scout -> draft -> review/prove -> flow/trace -> listen -> topic.

---

**Echo (do not modify)**

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn — and did we actually displace the status quo?"
```

Echo carries no `# Role:` annotation. This is the normative exception declared in ARTIFACT 0.
Echo is the terminal consumer of all displacement evidence — its needs seeded the backward
derivation in ARTIFACT 2.

---

**Completeness check:**
- [ ] ARTIFACT 0 (schema template) written FIRST — before role handoff table and trace (C-23);
      names five annotations with displacement gap format + consumer-pull rule + echo exception as
      normative + echo as terminal consumer anchor (C-21, C-22, C-24, C-26)
- [ ] Role handoff table (ARTIFACT 1): R-NN IDs, displacement evidence column, MECE namespace
      column (C-15, C-20)
- [ ] Displacement backward trace (ARTIFACT 2): every R-NN boundary's Produces/Consumes pair in
      sequence; echo named as terminal consumer and derivation seed; bilateral audit checkboxes;
      completed before YAML (C-25)
- [ ] Every non-echo stage has all five annotations simultaneously, displacement-anchored (C-18, C-19)
- [ ] Gap, Produces, Gate describe the same displacement claim — single referent (C-17)
- [ ] Stage N Produces = Stage N+1 Consumes at every boundary (C-14)
- [ ] At least one gate quantified with numeric threshold (C-10)
- [ ] Echo: last, `skills: []`, `auto: true`, no `# Role:` annotation (C-02)

---

## V-05 — Combined: All R8 Axes

**Axes:** Zone-anchor format (Z-NN, V-01) + handoff-matrix table (V-02) + specification-
constraint language (V-03) + displacement framing woven throughout (V-04) + consumer-pull
derivation baseline (all variants) + ALL gates quantified (exceeds C-10 baseline)

**Hypothesis:** Each R8 single-axis variant pushes one dimension to its extreme. This combination
tests whether all four reinforce rather than conflict. Zone-anchor provides lifecycle-grounded
meta-structure where zone exit/entry makes consumer-pull structurally self-evident. Handoff-matrix
format makes bilateral contracts maximally auditable. Specification language makes every constraint
normatively named. Displacement framing woven into every gap/gate produces maximally concrete,
testable evidence claims. Full gate quantification (every gate, not just one) provides the
strongest C-10 signal and forces specificity at every phase boundary. Echo is named as the
terminal consumer in both the constraint specification (ARTIFACT 0) and as row 0 of the
handoff matrix (ARTIFACT 2). Anticipated score: 180/180 with all gates quantified.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

Build a displacement-proof program with maximum structural rigor: lifecycle zones anchor the
phase arc; a handoff matrix table captures the full backward derivation with bilateral contracts
auditable as adjacent columns; constraint specification language makes derivation rules
normative; displacement framing is woven into every gap and gate annotation; every gate carries
a numeric threshold. The program is a staged displacement proof from discovery to echo.

Output five artifacts in this order:

0. **Constraint specification** — normative schema, derivation constraints, displacement gap
   format, quantification rule (FIRST — before any zone or stage content)
1. **Lifecycle zone registry** — arc zones with displacement gap classes and MECE namespace
   assignments (Z-NN IDs)
2. **Handoff matrix table** — backward derivation from echo (row 0) through Z-01 (last row);
   one row per stage; Produces and next-stage Consumes appear as adjacent auditable columns
3. **program.yaml** — stages transcribed from the handoff matrix, in execution order
4. **Self-audit** — bilateral contract compliance confirmation

---

**ARTIFACT 0 — Constraint specification (NORMATIVE — write before zones, matrix, or stages)**

```
Constraint Specification for {{topic}}

Status quo: [name the status quo — what teams do today without this feature, or what this
            feature displaces]

ANNOTATION SCHEMA — every non-echo stage SHALL carry all five annotations:

  # Zone: Z-NN     REQUIRED: back-reference to lifecycle zone registry row
  # Gap: "..."     REQUIRED: displacement-anchored gap language —
                   "We can't yet prove we beat [status quo] at [specific displacement sub-claim]"
                   Generic "we don't know X" language does NOT satisfy this requirement.
  # Owner: ...     REQUIRED: functional role (PM | Architect | Dev | Team Lead)
  # Consumes: [...] REQUIRED: artifact types this stage requires as input
  # Produces: [...] REQUIRED: displacement evidence artifacts this stage yields

  name: REQUIRED — human-readable label derived from the displacement sub-claim (not "stage1")
  skills: REQUIRED — Signal plugin skills from Z-NN namespace assignment
  gate: REQUIRED — ">=N [displacement evidence artifacts] present [quality condition]"

DERIVATION CONSTRAINT C-01 (NORMATIVE):
  The # Produces annotation of each stage SHALL be derived from what the immediately following
  stage declares as # Consumes. The prior stage's capability inventory SHALL NOT be used as
  a Produces derivation source. Consumer-pull: Produces is determined by what the NEXT stage
  declares as Consumes. The handoff matrix (ARTIFACT 2) SHALL be completed backward from echo
  before any stage YAML is written.

QUANTIFICATION CONSTRAINT C-02 (NORMATIVE):
  Every gate SHALL carry a numeric threshold — >=N count or =0 findings. No gate is valid
  if it cannot be evaluated with a count. "Artifacts present" without a number does not satisfy
  this constraint.

ECHO EXCEPTION C-03 (NORMATIVE):
  The stage named "echo" SHALL NOT carry the # Zone: annotation or any of the five required
  annotations. It SHALL carry auto: true and skills: [] only.
  Echo is the TERMINAL CONSUMER: its information needs about whether the feature displaced the
  status quo are the C-01 initialization constraint. The handoff matrix (ARTIFACT 2) SHALL
  begin with echo as row 0, and its implicit Consumes SHALL seed the backward derivation for
  Z-04 through Z-01. A plan that satisfies C-01 without naming echo as the initialization
  anchor does not fully satisfy C-03.
  This exception is normative — echo is outside the annotation schema.
```

---

**ARTIFACT 1 — Lifecycle zone registry**

After the constraint specification, declare the displacement arc as lifecycle zones. Each zone
is a phase of the feature's existence; the program advances the feature from one zone to the
next by proving displacement at that phase.

```
Lifecycle Zone Registry for {{topic}}

Status quo context: [restate status quo]

| ID   | Zone name       | Displacement gap class                                              | Zone entry (Consumes from prior zone) | Zone exit (Produces for next zone)   | Owner           | Namespaces (MECE) |
|------|-----------------|---------------------------------------------------------------------|---------------------------------------|--------------------------------------|-----------------|-------------------|
| Z-01 | Market proof    | "Can't yet prove we beat [SQ] at market viability"                  | (none — first zone)                   | market displacement evidence         | PM              | scout             |
| Z-02 | Design proof    | "Can't yet prove we beat [SQ] at design/spec quality"               | market displacement evidence          | design displacement evidence         | Architect       | draft, prove      |
| Z-03 | Technical proof | "Can't yet prove we beat [SQ] at technical validation"              | design displacement evidence          | technical displacement evidence      | Architect+Dev   | review, flow, trace |
| Z-04 | Adoption proof  | "Can't yet prove we beat [SQ] at adoption/readiness"                | technical displacement evidence       | adoption displacement evidence       | PM+Team         | listen, topic     |
```

MECE CONSTRAINT (C-01): Every namespace used in any stage SHALL appear in exactly one Z-NN row.
Note: Zone exit column names the artifact family produced by the zone — it becomes the next zone's
Zone entry (consumer-pull made structurally visible in the zone table itself).
Write AFTER ARTIFACT 0, BEFORE handoff matrix and stage YAML.

---

**ARTIFACT 2 — Handoff matrix table (backward derivation)**

Build this table backward from echo (row 0) to Z-01 (last row). This is the C-01 compliance
record. It makes every stage boundary's bilateral displacement contract independently verifiable:
a reader can audit all contracts by checking that the **Produces** column of row N equals the
**Consumes** column of row N-1 (the row above it). No stage YAML reading required.

**How to fill in (backward from echo):**
1. Row 0 (echo): identify echo's implicit Consumes — what displacement evidence summary it needs.
2. Row 4 Produces: SHALL equal row 0 (echo's) Consumes.
3. Row 3 Produces: SHALL equal row 4's Consumes.
4. Row 2 Produces: SHALL equal row 3's Consumes.
5. Row 1 Produces: SHALL equal row 2's Consumes.
6. Insert intermediate rows for zones with multiple stages; chain Produces/Consumes through each.

```
Handoff Matrix for {{topic}}
(Backward derivation — C-01 compliance record)

Audit rule: Produces(row N) SHALL equal Consumes(row N-1). Verify by scanning these two
columns without reading stage YAML.

| Row | Stage name              | Zone | Displacement gap (sub-claim)                                         | Produces (displacement evidence)   | Consumes (row above's Produces)     | Gate (>=N threshold, displacement quality)       | Owner     |
|-----|-------------------------|------|----------------------------------------------------------------------|------------------------------------|-------------------------------------|--------------------------------------------------|-----------|
| 0   | echo (terminal anchor)  | —    | [What displacement evidence must exist for echo to assess outcome?]  | —                                  | [echo's implicit Consumes — seed]   | auto: true                                       | —         |
| 4   | <adoption-proof stage>  | Z-04 | "Can't yet prove we beat [SQ] at [Z-04 sub-claim]"                   | [= row 0 Consumes]                 | [Z-04 needs from Z-03]              | ">=N [adoption displacement artifacts]"          | PM+Team   |
| 3   | <technical-proof stage> | Z-03 | "Can't yet prove we beat [SQ] at [Z-03 sub-claim]"                   | [= row 4 Consumes]                 | [Z-03 needs from Z-02]              | "=0 P0 findings in technical validation OR >=N"  | Arch+Dev  |
| 2   | <design-proof stage>    | Z-02 | "Can't yet prove we beat [SQ] at [Z-02 sub-claim]"                   | [= row 3 Consumes]                 | [Z-02 needs from Z-01]              | ">=N [design displacement artifacts]"            | Architect |
| 1   | <market-proof stage>    | Z-01 | "Can't yet prove we beat [SQ] at [Z-01 sub-claim]"                   | [= row 2 Consumes]                 | [] (first zone)                     | ">=N [market displacement artifacts, no P0s]"    | PM        |
```

After completing the table, verify:
- [ ] Row 4 Produces = Row 0 Consumes (Z-04 -> echo boundary)
- [ ] Row 3 Produces = Row 4 Consumes (Z-03 -> Z-04 boundary)
- [ ] Row 2 Produces = Row 3 Consumes (Z-02 -> Z-03 boundary)
- [ ] Row 1 Produces = Row 2 Consumes (Z-01 -> Z-02 boundary)

---

**ARTIFACT 3 — program.yaml**

Transcribe the handoff matrix from the bottom row upward (row 1 first, then 2, 3, 4, then
echo). Every annotation value SHALL match the corresponding matrix cell.

```yaml
# ARTIFACT 3: program.yaml for {{topic}}
# Displacement proof — derived from handoff matrix (ARTIFACT 2)
# All stages comply with Constraint Specification (ARTIFACT 0)
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # === Zone Z-01: Market proof (Matrix row 1) ===
    - name: <displacement-claim label from matrix row 1>
      # Zone: Z-01
      # Gap: "We can't yet prove we beat [status quo] at [Z-01 sub-claim from matrix]"
      # Owner: PM
      # Consumes: []
      # Produces: [from matrix row 1 Produces column]
      skills: [...]
      gate: ">=N [market displacement artifact types] present [no P0 findings]"

    # === Zone boundary Z-01 -> Z-02 — C-01 compliant ===
    # Z-01 final Produces: [displacement artifacts from matrix]
    # Z-02 first Consumes: [same displacement artifacts — bilateral contract]

    - name: <displacement-claim label from matrix row 2>
      # Zone: Z-02
      # Gap: "We can't yet prove we beat [status quo] at [Z-02 sub-claim from matrix]"
      # Owner: Architect
      # Consumes: [matrix row 1 Produces = row 2 Consumes — C-01 satisfied]
      # Produces: [from matrix row 2 Produces column]
      skills: [...]
      gate: ">=N [design displacement artifact types] present [quality condition]"

    # [continue for Z-03, Z-04 — every gate carries >=N threshold]

    - name: echo
      skills: []
      auto: true
      question: "What did we learn — and did we actually displace the status quo?"
```

---

**ARTIFACT 4 — Self-audit**

After writing stage YAML, confirm compliance with the Constraint Specification (ARTIFACT 0):

```
Self-audit for {{topic}}

Schema and methodology compliance:
  [ ] ARTIFACT 0 (constraint spec) written FIRST — before zone registry and handoff matrix (C-23)
  [ ] Schema names five annotations + C-03 echo exception as normative (C-21, C-22)
  [ ] C-01 consumer-pull constraint stated normatively: "Produces determined by next Consumes" (C-24)
  [ ] Echo named as TERMINAL CONSUMER and C-01 initialization anchor in ARTIFACT 0 (C-26)

Pre-YAML derivation artifacts:
  [ ] Zone registry (ARTIFACT 1): Z-NN IDs, displacement gap classes, MECE namespace column,
      zone entry/exit columns (C-15, C-20)
  [ ] Handoff matrix (ARTIFACT 2): every boundary's Produces/Consumes as adjacent auditable columns;
      row 0 is echo (terminal consumer and derivation seed); positioned before YAML (C-25)
  [ ] Bilateral audit checkboxes completed in ARTIFACT 2 (C-14 evidence)

Per-stage compliance:
  [ ] Every non-echo stage has all five annotations simultaneously (C-18)
  [ ] Every non-echo stage carries a Z-NN back-reference to zone registry row (C-19)
  [ ] Gap uses displacement language "Can't yet prove we beat [SQ] at X" — not generic (C-11)
  [ ] Gap, Produces, Gate describe the same displacement claim — single referent (C-17)
  [ ] Stage N Produces = Stage N+1 Consumes at every boundary (C-14)
  [ ] EVERY gate carries a numeric threshold — not just one (C-10 exceeded: all-gates quantified)

Structural compliance:
  [ ] Echo: last, skills: [], auto: true, no # Zone: annotation (C-02)
  [ ] All skills are valid Signal plugin skills from the namespace table (C-03)
  [ ] Namespace dependency order maintained: scout -> draft -> review/prove -> flow/trace -> listen -> topic (C-05)
```

---

**Available Signal skills**

| Namespace | Skills |
|-----------|--------|
| scout     | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft     | spec, proposal, pitch |
| review    | design, code, users, customers |
| prove     | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow      | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace     | request, state, contract, component, deployment, migration, permissions |
| listen    | feedback, support, adoption |
| topic     | status, report |

Namespace dependency order: scout -> draft -> review/prove -> flow/trace -> listen -> topic.

---

**Echo (do not modify)**

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn — and did we actually displace the status quo?"
```

Echo carries no `# Zone:` annotation. This is ECHO EXCEPTION C-03, declared normatively in
ARTIFACT 0. Echo is the terminal consumer — row 0 of the handoff matrix, the C-01 initialization
seed for the entire backward derivation.

---

## R8 Axis Coverage Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Lifecycle emphasis — zone-anchor (Z-NN) | X | | | | X |
| Output format — handoff-matrix table | | X | | | X |
| Phrasing register — specification-constraint (SHALL/P-NN) | | | X | | X |
| Inertia framing — displacement woven into every annotation | | | | X | X |
| Role sequence (R-NN role handoff) | | | | X | |
| All gates quantified (not just one) | | | | | X |
| Consumer-pull baseline (C-24/C-25/C-26) | X | X | X | X | X |

## C-24 / C-25 / C-26 Compliance Map

| Variant | C-24 (consumer-pull rule normative) | C-25 (pre-YAML trace worksheet) | C-26 (echo as terminal consumer + anchor) |
|---------|-------------------------------------|---------------------------------|-------------------------------------------|
| V-01 | PASS — "Consumer-pull rule: # Produces... is determined by what the NEXT zone/stage declares as # Consumes" in ARTIFACT 0 | PASS — Zone Transition Worksheet (ARTIFACT 2) lists every Z-NN boundary Produces/Consumes pair before YAML | PASS — "Echo is the terminal consumer... its zone-entry information needs anchor the entire backward derivation in ARTIFACT 2" in ARTIFACT 0 |
| V-02 | PASS — "Consumer-pull rule: # Produces... determined entirely by what the NEXT stage declares as # Consumes" in ARTIFACT 0; matrix enforces structurally | PASS — Handoff matrix (ARTIFACT 2) has Produces and Consumes as adjacent auditable columns for every boundary; echo is row 0 before YAML | PASS — "Echo is the terminal consumer — it is row 0 of the handoff matrix, and its implicit information needs seed the backward derivation" in ARTIFACT 0 |
| V-03 | PASS — "DERIVATION CONSTRAINT P-01 (NORMATIVE): The # Produces annotation... SHALL be derived exclusively from what the immediately following stage declares as # Consumes" in ARTIFACT 0 | PASS — Constraint Satisfaction Trace (ARTIFACT 2) is explicitly the P-01 compliance record; lists every boundary Produces/Consumes with echo as initialization; before YAML | PASS — "ECHO EXCEPTION P-02: Echo is the TERMINAL CONSUMER: its information needs are the initialization input for the P-01 constraint satisfaction trace" in ARTIFACT 0 |
| V-04 | PASS — "Consumer-pull rule: # Produces... is determined by what the NEXT stage declares as # Consumes... Complete the displacement backward trace (ARTIFACT 2) from echo's needs before writing any stage YAML" in ARTIFACT 0 | PASS — Displacement Backward Trace (ARTIFACT 2) lists every R-NN boundary Produces/Consumes pair with bilateral audit checkboxes; before YAML | PASS — "Echo is the terminal consumer of all displacement evidence — its information needs... anchor the entire backward derivation in ARTIFACT 2" in ARTIFACT 0 |
| V-05 | PASS — "DERIVATION CONSTRAINT C-01: Consumer-pull: Produces is determined by what the NEXT stage declares as Consumes" in ARTIFACT 0 | PASS — Handoff matrix (ARTIFACT 2) has adjacent Produces/Consumes columns; echo is row 0; positioned before YAML; audit checkboxes | PASS — "ECHO EXCEPTION C-03: Echo is the TERMINAL CONSUMER... its implicit Consumes SHALL seed the backward derivation... A plan that satisfies C-01 without naming echo as the initialization anchor does not fully satisfy C-03" in ARTIFACT 0 |
