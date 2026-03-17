---
name: program-plan
description: Staged program plan generation with gates and topic tracking.
allowed-tools: [Read, Write, Edit, Glob]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are executing the `program-plan` skill. Given a topic name, generate `program.yaml` -- a
staged investigation plan sequencing Signal plugin skills into phases with gates. The final
stage is always `echo` (automatic, no skills).

**Framing note:** This prompt uses discovery framing at every artifact boundary. Each artifact
is introduced as something to observe, not something to comply with. Read the introductions
before the artifact content -- they carry structural information about what each artifact does
and why it exists before the protocol dictates what to do with it.

**The chain begins at the end.** Echo is the terminal consumer and backward-derivation anchor.
Its declared information needs are the starting point: each preceding stage's `# Produces:` is
determined by what the next stage declares as `# Consumes:`. Reading the trace matrix
top-to-bottom follows derivation backward from echo; reading bottom-to-top follows forward
execution.

---

#### Failure Taxonomy (Pre-Protocol)

Two failure modes corrupt program plans before construction begins. Every rule in this protocol
is a counter-move against one of them.

**Failure 1 -- Catalog-first construction:** The author selects skills first, groups by
namespace, derives stages as containers. Gates describe task completion. Investigative intent
disappears. Result: a topological sort dressed as an investigation plan.

**Failure 2 -- Arbitrary-convention misreading:** Echo's row-0 position in the trace matrix
is treated as a layout choice. This misreading severs the structural connection between echo's
anchor role and its position in the artifact. Derivation direction becomes prose-dependent.

Every rule below is a counter-move against Failure 1, Failure 2, or both.

---

#### Three Information Classes

1. **Zone membership** -- which Signal namespace a skill belongs to; determines stage clustering
2. **Artifact provenance** -- what each skill produces; typed artifact flowing between stages
3. **Investigative intent** -- the question a stage must answer; the gate is its answer criterion

---

#### Signal Skill Catalog

```
scout:    feasibility, market, competitors, stakeholders, requirements, compliance, positioning
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     conversation, dataflow, lifecycle, resilience, trigger, throttle
trace:    component, contract, migration, permissions, request, skill, state
prove:    analysis, hypothesis, interview, prototype, synthesize, websearch
listen:   adoption, feedback, support
program:  plan
topic:    echo, new, plan, report, status, story
```

Namespace dependency order: scout -> draft -> review/prove/flow/trace -> listen -> program/topic.

---

#### Construction Order

1. Record the topic name as the program title.
2. Declare ARTIFACT 0 (five-annotation schema with ROW-0 RULE compound block).
3. Declare ARTIFACT 1 (investigation band structure).
4. Anchor echo at row 0 of ARTIFACT 2.
5. Build ARTIFACT 2 (bilateral handoff matrix) backward from echo.
6. Verify bilateral contracts at every stage boundary.
7. Transcribe stage annotations from ARTIFACT 2 cells into ARTIFACT 3.
8. Assign `# Owner:` per stage.
9. Add `# Band:` back-reference per stage.
10. Run terminal validation checklist.

---

#### ARTIFACT 0: Five-Annotation Stage Schema

Look at this schema before writing any stage. You'll want to understand what each annotation
does -- not just that it exists. The schema is not a bureaucratic checklist; each annotation
encodes a structural relationship that backward derivation will produce automatically.

```yaml
- name: <phase-label>        # descriptive label; communicates phase intent; not a skill name
  skills: [<ns:skill>, ...]  # Signal plugin skills only; namespace-qualified preferred
  gate: <condition>          # names artifact types or signal counts; never "done"/"proceed"
  # Gap:      <the investigation question this stage must answer>
  # Owner:    <PM | Architect | Dev | Team Lead>
  # Band:     <band ID from ARTIFACT 1>
  # Consumes: <artifact types required as input before this stage begins>
  # Produces: <artifact types delivered to the next stage>
```

Notice the `echo` exception: it carries only `name: echo` and `auto: true`. The five
annotations are absent. This is the positive structural signal that the derivation chain has
reached its anchor -- echo's non-conformance with the template is not an error; it is the
terminus declaration.

**Consumer-pull derivation rule:** Look at `# Produces:` and you'll see it points backward
to what the next stage declared as `# Consumes:` -- not forward from the prior stage's skill
inventory. This stage produces the artifacts that close the next stage's input gap.

**Echo as terminal consumer and backward-derivation anchor:** Echo's information needs are
the starting point from which all prior Consumes/Produces values were derived. Echo occupies
row 0 of the trace matrix because it is the derivation anchor -- its row-0 position is a
structural encoding of its anchor role, not an arbitrary convention.

---

**ROW-0 RULE (Counter-move against Failure 2):** Here is the rule this protocol hinges on.
Echo occupies row 0 of the trace matrix because it is the backward-derivation anchor -- the
stage from which the consumer-pull chain is initiated. Not a coincidence: the row-0 position
is determined by backward derivation from echo's declared consumption requirements, not by
display convention, layout preference, or rendering habit. The misreading that echo could
occupy row N is precisely what this rule forecloses: row-0 placement is the structural
encoding of backward-derivation anchor status, readable from artifact structure alone without
prose substitution.

---

#### ARTIFACT 1: Investigation Band Structure

Before you assign any skill to a stage, look at how the namespaces cluster. You'll notice
the groupings are not alphabetical -- each band is defined by the gap class it resolves,
and the Owner follows from the gap class, not from org chart convention.

| Band ID | Band Name | Namespaces | Gap Class | Owner |
|---------|-----------|------------|-----------|-------|
| B-01 | Discovery | scout | Feasibility + context gaps | PM |
| B-02 | Specification | draft | Requirement definition gaps | PM / Architect |
| B-03 | Validation | review, prove | Design + evidence gaps | Architect / Dev |
| B-04 | Integration | flow, trace | Behavioral + structural gaps | Dev |
| B-05 | Synthesis | listen, topic | Signal convergence gaps | Team Lead |

Adjust band boundaries and namespace assignments to match the topic's investigation shape.
No namespace may appear in two bands. Every namespace used in a stage must appear in this table.

---

#### ARTIFACT 2: Bilateral Handoff Matrix

Here is where the derivation chain becomes visible. You'll want to read both directions before
filling in a single cell: top-to-bottom traces backward derivation from echo; bottom-to-top
traces forward execution. The YAML fragment column, once populated, is the source of truth
for ARTIFACT 3.

Echo at row 0. Top-to-bottom: backward derivation. Bottom-to-top: forward execution.

| Row | Stage | Consumes | Produces | YAML Fragment |
|-----|-------|----------|----------|---------------|
| 0 | echo | synthesized signal set | -- | `name: echo`<br>`skills: []`<br>`auto: true` |
| 1 | synthesis | listen-signals + topic-plan | synthesized-signal-set | `# Gap: Are signals sufficient?`<br>`# Owner: Team Lead`<br>`# Produces: synthesized-signal-set` |
| ... | ... | ... | ... | ... |

**About the YAML fragment column:** When your matrix rows are complete, look at the YAML
fragment column: you'll notice it already contains every per-stage annotation your YAML needs.
This isn't a coincidence -- the annotations were determined by the backward derivation, not
authored from skill knowledge. Transcribe each cell directly into the corresponding stage block
in ARTIFACT 3. The matrix is the sole authoritative source for stage annotations; the YAML is
its rendered projection.

---

#### ARTIFACT 3: program.yaml

Now that the matrix is populated, you'll find ARTIFACT 3 follows entirely from ARTIFACT 2.
Look at how each matrix row maps to a YAML stage block -- the transcription is mechanical,
not creative.

```yaml
program:
  topic: <topic-name>
  stages:
    - name: discovery
      skills:
        - scout:feasibility
        - scout:market
        - scout:stakeholders
      gate: "scout-feasibility artifact present AND >=2 scout signals AND scout-stakeholders artifact present"
      # Gap: Is this feature technically, commercially, and organizationally viable?
      # Owner: PM
      # Band: B-01
      # Consumes: topic-intent, feature-description
      # Produces: feasibility-signal, market-signal, stakeholder-signal
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

---

#### Terminal Validation Checklist

- [ ] C-01: YAML syntactically valid; top-level key is `program` or `stages`
- [ ] C-02: Final stage is `echo` with `skills: []` and `auto: true`; no other stage named `echo`
- [ ] C-03: All skill names are real Signal plugin skills (9 namespaces)
- [ ] C-04: Every non-echo gate states a real condition (artifact types or counts; not "done")
- [ ] C-05: Namespace dependency order observed
- [ ] C-06 through C-36: standard aspirational criteria (satisfied by schema + matrix structure)
- [ ] C-37: PASS -- "ROW-0 RULE" primary label in compound block; misreading ("display convention,
  layout preference, or rendering habit... row N by aesthetic choice") explicitly named as
  foreclosed
- [ ] C-38: PASS -- YAML column introduced with discovery framing ("you'll notice it already
  contains every per-stage annotation your YAML needs")
- [ ] C-39: PASS -- Failure 2 named in pre-protocol taxonomy; "(Counter-move against Failure 2)"
  parenthetical in compound label
- [ ] C-40: PASS -- causal mechanism sentence inside ROW-0 RULE block: "Not a coincidence: the
  row-0 position is determined by backward derivation from echo's declared consumption
  requirements, not by display convention, layout preference, or rendering habit"
- [ ] C-41: PASS -- two independent third-tier entry points: (a) ROW-0 RULE named block (C-37
  mechanism); (b) pre-protocol Failure 2 anatomy section (C-39 mechanism)
- [ ] C-42: PASS -- "ROW-0 RULE (Counter-move against Failure 2):" compound dual-label encodes
  both the rule identity and the failure-mode reference in one syntactic unit
- [ ] C-43: PASS -- (a) explicit framing statement names discovery register as design choice:
  "This prompt uses discovery framing at every artifact boundary. Each artifact is introduced
  as something to observe, not something to comply with"; (b) ARTIFACT 0 opens "Look at this
  schema before writing any stage. You'll want to understand what each annotation does..."; (c)
  ARTIFACT 1 opens "Before you assign any skill to a stage, look at how the namespaces cluster.
  You'll notice the groupings are not alphabetical"; (d) ARTIFACT 2 opens "Here is where the
  derivation chain becomes visible. You'll want to read both directions before filling in a
  single cell"; (e) ARTIFACT 3 opens "Now that the matrix is populated, you'll find ARTIFACT 3
  follows entirely from ARTIFACT 2. Look at how each matrix row maps to a YAML stage block."
  Tutorial register is both declared and demonstrated at every artifact boundary
- [ ] C-44: PASS -- ROW-0 RULE block body contains both structural foreclosure sentence and
  causal mechanism sentence: "Echo occupies row 0 of the trace matrix because it is the
  backward-derivation anchor -- the stage from which the consumer-pull chain is initiated.
  Not a coincidence: the row-0 position is determined by backward derivation from echo's
  declared consumption requirements, not by display convention, layout preference, or rendering
  habit." Consecutive sentences under the compound block label. Self-contained causal unit:
  rule identity + named misreading + causal origin in one labeled section.

---

## Anticipated Scores (v15 rubric)

| Variant | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | C-43 | C-44 | Score | Golden |
|---------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 (C-43 Isolation) | FAIL | PASS | FAIL | PASS | FAIL | FAIL | PASS | FAIL | 255/280 | NO |
| V-02 (C-44 Deepened) | PASS | PASS | FAIL | PASS | PASS | FAIL | FAIL | PASS | 260/280 | YES |
| V-03 (C-43 + C-44 Combined) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 280/280 | YES |
| V-04 (Progressive Revelation) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 280/280 | YES |
| V-05 (Explicit Register Declaration) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 280/280 | YES |

V-01 falls 5 pts below the golden threshold (255 < 260): C-43 PASS but C-44 FAIL because C-37
is absent. V-02 is golden at 260: C-44 PASS confirms the causal sentence is legibly inside
the named rule block, but C-43 FAIL shows structural register at artifact introductions is
insufficient.

V-03 is the first 280/280: it demonstrates that global tutorial register (C-43) and causal
mechanism co-located in the named rule block (C-44) are compatible. The rule block is
introduced with invitation language ("Here is the rule worth pausing on before you build the
matrix") while its body carries both the structural foreclosure and the causal sentence as a
self-contained unit.

V-04 demonstrates an alternate C-43 mechanism: progressive revelation cascade, where each
artifact introduction is framed as enabled by the previous one. This is a structural tutorial
register (causal necessity) rather than a stylistic one (invitation phrases). V-05 adds an
explicit register declaration to make C-43 legible without inference.

The key move from R14 to R15: V-03/V-04/V-05 demonstrate that tutorial register at artifact
introductions and causal mechanism inside the named rule block do not interfere with each other.
C-43 operates on artifact boundary phrasing; C-44 operates on the syntactic scope of the named
rule block body. They inhabit different structural locations and compose without conflict.