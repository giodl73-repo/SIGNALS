Now writing the 5 complete R6 variations. The catalog is confirmed at **47 skills** (8 namespaces, scout has `scout-competitors` as 8th, trace has `trace-skill` as 8th).

---

## R6 Variation Set — program-plan

**R6 design goal:** All 5 variations pass C-22 and C-23 as baseline. Variation axes explore structural dimensions beyond the R5 ceiling that may surface R7 criteria.

**Confirmed skill catalog (R6):** 47 skills, 8 namespaces (scout×8, draft×3, review×4, flow×7, trace×8, prove×8, listen×3, topic×6). `program-plan` and `quest` namespace skills excluded from usable catalog — a plan cannot invoke itself, and quest skills are meta-evaluation tools.

**R5 ceiling gap:** C-22 (gate template has cascade-if-removed) and C-23 (arc-strategy names first gate) — only R5 V-04 passed both. All R6 variations must pass both as baseline.

---

### Variation axes

| Variation | Axis | Type | Hypothesis |
|-----------|------|------|------------|
| V-01 | Gate cascade arrow notation in template | Single | Extending C-22's clause to require `->` notation + 2+ hop depth IN the gate format string (parallel to how C-20 extended C-18 by adding cascade notation to the actor header) eliminates single-consequence removal clauses at every boundary |
| V-02 | All-gates cascade pre-computation table | Single | A dedicated Gate Cascade Audit table before YAML assembly (parallel to actor ordering table before stage design) forces the model to reason about ALL cascades as a pre-work pass, producing more consequential and cross-linked gate language |
| V-03 | Echo stage displacement reasoning | Single | Requiring explicit justification for why echo cannot run earlier — what arc-completion signal does echo emit, what breaks if it fires at stage 2 — extends displacement-impossibility to the echo stage specifically and surfaces that echo's position is architecturally required, not conventional |
| V-04 | V-01 + V-02 | Combination | Gate audit table forces cascade chain content (V-02); `->` notation in the gate format string enforces cascade format (V-01); together they produce well-formed multi-hop cascades at every boundary |
| V-05 | V-01 + V-02 + V-03 + gate-to-gate chain | Combination | Adding a gate-to-gate chain column (removing gate N explicitly impacts gate N+1) to the full V-04 foundation produces a program plan where every boundary is causally linked to adjacent boundaries across the full arc |

---

## V-01 — Gate Cascade Arrow Notation in Template

**Variation axis:** Gate cascade notation in format string (single)
**Hypothesis:** The same load-bearing-instruction principle that produced C-20 (extending C-18 by embedding `->` notation + depth in the column header) applies to the gate format string. A gate template that specifies `->` notation and minimum cascade depth within its cascade-if-removed element will produce multi-hop chains at every boundary — eliminating single-consequence removal clauses by structural requirement rather than post-hoc check.

---

A program plan whose gate format strings carry a cascade-if-removed clause but impose no notation requirement produces single-consequence removal statements — the model names one downstream effect and stops. This variation defeats single-hop cascade clauses in gate strings by embedding the `->` notation requirement and minimum depth directly inside the gate format string, making cascade depth structural at every boundary in the same way C-20 made it structural at every actor table row.

### Task

Generate `program.yaml` for topic: **{{topic}}**

Stages group Signal skills into coherent phases. Each non-echo stage has a gate specifying what must exist before the next stage begins. The final stage is always `echo` (`auto: true`, empty skills list). The program is a plan — every skill also runs standalone.

### Skill Catalog (inline — use only these skills)

```
scout:  scout-competitors, scout-compliance, scout-feasibility, scout-market,
        scout-naming, scout-positioning, scout-requirements, scout-stakeholders
draft:  draft-pitch, draft-proposal, draft-spec
review: review-code, review-customers, review-design, review-users
flow:   flow-conversation, flow-dataflow, flow-integration, flow-lifecycle,
        flow-resilience, flow-throttle, flow-trigger
trace:  trace-component, trace-contract, trace-deployment, trace-migration,
        trace-permissions, trace-request, trace-skill, trace-state
prove:  prove-analysis, prove-hypothesis, prove-intelligence, prove-interview,
        prove-prototype, prove-publish, prove-synthesize, prove-websearch
listen: listen-adoption, listen-feedback, listen-support
topic:  topic-echo, topic-new, topic-plan, topic-report, topic-status, topic-story
```

No other skill names exist. Do not use `program-plan` in any stage's skills list.

---

### Step 1 — Select relevant skills

List skills from the catalog that apply to {{topic}}. For each: one sentence — what signal it produces and why it is relevant. Omit irrelevant skills. Group by namespace.

---

### Step 2 — Actor ordering table

For each namespace actor that will appear as a stage, complete this table.

| Actor | Cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences crossing arc-layer boundaries) |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Strategist (scout) | First actor — no earlier position exists; if delayed past stage 1: Architect designs without validated problem assumptions -> Researcher proves a hypothesis with no market grounding -> Reviewer critiques artifacts anchored in untested assumptions |
| Architect+PM (draft) | Cannot run before Strategist; if moved earlier: draft-spec encodes invented requirements without feasibility data -> Researcher builds a prototype against an unvalidated spec -> Reviewer finds no validated baseline to judge the design against |
| Researcher (prove) | Cannot run before Architect+PM; if moved earlier: prove-prototype builds without a design artifact to test against -> prove-hypothesis tests an unformalized assumption -> Reviewer receives evidence that has no design artifact as a comparison baseline |
| Reviewer (review+trace) | Cannot run before Researcher; if moved earlier: review-design critiques a design without prototype evidence -> prove-publish incorporates no review findings -> topic-story cites a review that was conducted on a design with no validation backing |
| Field team (listen) | Cannot run before meaningful artifacts exist; if moved to stage 2: listen-feedback collects reactions to a spec not a working artifact -> listen-adoption measures adoption of a design document -> topic-status reports adoption data with no implementation baseline |
| Synthesizer (topic) | Cannot run before all signal types present; if moved to stage 2: topic-status aggregates zero depth signals -> topic-plan creates a plan with no validation findings -> topic-story writes a narrative unsupported by any research or review outcome |

Every row uses `->` notation with 3 ordered consequences crossing arc-layer boundaries. A single-consequence or 2-consequence entry fails this step.

---

### Step 3 — Stage design

Group selected skills into 3–5 stages (plus echo). Each stage:
- Name communicates phase intent (not `stage1`, not a skill name)
- Contains skills producing related signal types
- Precedes stages that depend on its outputs

Suggested phases: `discovery` (scout), `specification` (draft), `validation` (prove + review), `synthesis` (topic), `echo` (always last, auto).

---

### Step 4 — Gate writing

For every non-echo stage, write a gate using this exact format:

```
[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present
— removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries]
```

The `->` notation and minimum 2-hop cascade depth are required elements of the cascade-if-removed clause. A removal clause with no `->` arrows, or one that names only a single downstream consequence, fails this step.

**Concrete example:**
```
Strategist hands off to Architect+PM when >=3 scout-signal artifacts present
— removing this gate: draft-spec runs without validated requirements -> prove-prototype
builds against an unvalidated design -> review-design critiques a prototype with no
market-grounded baseline
```

Requirements:
- `>=N` is a specific numeric threshold (not "sufficient", not "done")
- `artifact_type` names a specific artifact category (not just "signals" or "artifacts")
- Cascade: `->` notation, 2+ hops, crossing at least one arc-layer boundary
- The cascade-if-removed clause is a required element of the gate string — not an annotation added afterward

---

### Step 5 — Arc strategy

Write 3–4 sentences explaining why this arc is correct for {{topic}}.

Answer explicitly:
1. What broad-to-deep signal progression does this arc follow?
2. **Specifically:** what is the multi-hop consequence cascade if the first gate (scout handoff) is removed? Trace at least 3 downstream consequences using `->` notation. Do not answer with "any gate" — name the scout handoff gate specifically.
3. What is the second most consequential gate? Trace its removal cascade using `->` notation.

---

### Step 6 — Assemble program.yaml

Produce valid YAML:
- Top-level key: `stages` (list)
- Each stage: `name` (string), `skills` (list), `gate` (string)
- Echo stage: `name: echo`, `skills: []`, `auto: true`, no `gate` field
- Only the `echo` stage is named `echo`
- Skills in dependency order (scout before draft before prove, etc.)
- Every non-echo gate uses the format from Step 4 (includes `->` cascade in removal clause)
- No skills outside the catalog

Output as a fenced YAML code block.

---

## V-02 — All-Gates Cascade Pre-Computation Table

**Variation axis:** All-gates cascade pre-computation table (single)
**Hypothesis:** The actor ordering table forces the model to reason about ALL actor positions before stage design begins. A parallel Gate Cascade Audit table — computed before any gate strings are written — forces the model to reason about ALL gate cascades as a structured pre-work pass. Cascades computed in a dedicated table before YAML assembly are more consequential and internally consistent than cascades written inline during YAML construction, because the model has established the full cascade graph before encoding it.

---

A program plan whose gate strings are authored inline during YAML assembly has the same problem as a build pipeline where each module's interface is designed at the moment of implementation: each gate is reasoned in isolation, without awareness of how its cascade relates to adjacent stages. This variation defeats isolated gate cascade reasoning by requiring all gate cascades to be pre-computed in a structured audit table before any gate string is written — the same mechanism the actor ordering table uses to anchor stage design before YAML.

### Task

Generate `program.yaml` for topic: **{{topic}}**

Stages group Signal skills into coherent phases. Each non-echo stage has a gate. Final stage is always `echo` (`auto: true`, empty skills list). The program is a plan — every skill also runs standalone.

### Skill Catalog (inline — use only these skills)

```
scout:  scout-competitors, scout-compliance, scout-feasibility, scout-market,
        scout-naming, scout-positioning, scout-requirements, scout-stakeholders
draft:  draft-pitch, draft-proposal, draft-spec
review: review-code, review-customers, review-design, review-users
flow:   flow-conversation, flow-dataflow, flow-integration, flow-lifecycle,
        flow-resilience, flow-throttle, flow-trigger
trace:  trace-component, trace-contract, trace-deployment, trace-migration,
        trace-permissions, trace-request, trace-skill, trace-state
prove:  prove-analysis, prove-hypothesis, prove-intelligence, prove-interview,
        prove-prototype, prove-publish, prove-synthesize, prove-websearch
listen: listen-adoption, listen-feedback, listen-support
topic:  topic-echo, topic-new, topic-plan, topic-report, topic-status, topic-story
```

No other skill names exist. Do not use `program-plan` in any stage's skills list.

---

### Step 1 — Select relevant skills

List skills from the catalog that apply to {{topic}}. For each: one sentence — what signal it produces. Omit irrelevant skills. Group by namespace.

---

### Step 2 — Actor ordering table

For each namespace actor that will appear as a stage, complete this table.

| Actor | Cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences crossing arc-layer boundaries) |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Strategist (scout) | First actor — no earlier position exists; if delayed: Architect designs without validated assumptions -> Researcher proves a hypothesis with no market grounding -> Reviewer critiques artifacts anchored in untested assumptions |
| Architect+PM (draft) | Cannot run before Strategist; if moved earlier: draft-spec encodes invented requirements -> Researcher builds prototype against unvalidated spec -> Reviewer has no validated baseline to judge against |
| Researcher (prove) | Cannot run before Architect+PM; if moved earlier: prove-prototype builds without a design artifact -> prove-hypothesis tests an unformalized assumption -> Reviewer receives evidence with nothing to compare against |
| Reviewer (review+trace) | Cannot run before Researcher; if moved earlier: review-design critiques without prototype evidence -> prove-publish incorporates no review findings -> topic-story cites a review with no validation backing |
| Field team (listen) | Cannot run before meaningful artifacts exist; if moved earlier: listen-feedback collects reactions to a spec not a feature -> listen-adoption measures document adoption -> topic-status reports adoption with no implementation baseline |
| Synthesizer (topic) | Cannot run before all signal types present; if moved earlier: topic-status aggregates zero depth signals -> topic-plan creates an evidence-free plan -> topic-story writes a narrative with no research or review backing |

Every row uses `->` notation with 3 ordered consequences crossing arc-layer boundaries.

---

### Step 3 — Stage design

Group selected skills into 3–5 stages (plus echo). Each stage:
- Name communicates phase intent (not `stage1`, not a skill name)
- Contains skills producing related signal types
- Precedes stages that depend on its outputs

---

### Step 4 — Gate Cascade Audit

Before writing any gate strings, complete this audit table for every non-echo stage:

| Stage | Delivering Actor → Receiving Actor | Threshold | Cascade if Removed (-> notation, 2+ hops, crossing arc-layer boundaries) |
|-------|-------------------------------------|-----------|--------------------------------------------------------------------------|
| [stage name] | [Delivering Actor] → [Receiving Actor] | >=N artifact_type | [A -> B -> C] |
| ... | ... | ... | ... |

Requirements:
- Every row: specific numeric threshold (`>=N`, not "sufficient" or "done")
- Every row: `->` cascade with 2+ hops crossing at least one arc-layer boundary
- Complete this ENTIRE table before writing any gate strings in Step 5
- The cascade chains computed here are the authoritative source for Step 5 gate strings

This is pre-work. The model that writes gate strings without this table has no cross-gate cascade awareness.

---

### Step 5 — Gate writing

For every non-echo stage, write a gate using this format:

```
[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present
— removing this gate: [cascade chain from Step 4 audit]
```

Use the cascade chains from the Step 4 audit. The cascade-if-removed clause is a required element of every gate string.

**Concrete example:**
```
Strategist hands off to Architect+PM when >=3 scout-signal artifacts present
— removing this gate: draft-spec runs without validated requirements -> prove-prototype
builds against an unvalidated design -> review-design critiques with no market-grounded baseline
```

---

### Step 6 — Arc strategy

Write 3–4 sentences explaining why this arc is correct for {{topic}}.

Answer explicitly:
1. What broad-to-deep signal progression does this arc follow?
2. **Specifically:** what is the multi-hop consequence cascade if the first gate (scout handoff) is removed? Trace at least 3 downstream consequences using `->` notation. Name the scout handoff gate — a generic "any gate" answer fails this item.
3. Looking at your Gate Cascade Audit from Step 4 — which gate has the longest downstream cascade? Why is that gate the highest-leverage boundary in this arc?

---

### Step 7 — Assemble program.yaml

Produce valid YAML:
- Top-level key: `stages` (list)
- Each stage: `name` (string), `skills` (list), `gate` (string)
- Echo stage: `name: echo`, `skills: []`, `auto: true`, no `gate` field
- Only the `echo` stage is named `echo`
- Skills in dependency order
- Every non-echo gate uses the format from Step 5 (actor names + threshold + artifact type + cascade-if-removed)
- No skills outside the catalog

Output as a fenced YAML code block.

---

## V-03 — Echo Stage Displacement Reasoning

**Variation axis:** Echo stage displacement reasoning (single)
**Hypothesis:** The displacement-impossibility forcing function (C-18, C-20) is applied to all namespace actors in the ordering table but not to the echo stage, which has a fundamentally different nature: it is auto-triggered, has no skills, and emits an arc-completion signal. Requiring explicit echo displacement reasoning — what signal does echo emit, what breaks if it fires at stage 2 — forces the model to understand that echo's last position is architecturally required: an arc-completion signal on an incomplete arc is a false positive that downstream systems act on.

---

A program plan that places echo last "by convention" produces gates whose final threshold is calibrated to stage completeness rather than arc-completion pre-conditions. This variation defeats convention-based echo placement by requiring explicit echo displacement reasoning before stage design begins — if the model cannot explain what breaks when echo fires at stage 2, it has not understood what the arc-completion signal means.

### Task

Generate `program.yaml` for topic: **{{topic}}**

Stages group Signal skills into coherent phases. Each non-echo stage has a gate. Final stage is always `echo` (`auto: true`, empty skills list). The program is a plan — every skill also runs standalone.

### Skill Catalog (inline — use only these skills)

```
scout:  scout-competitors, scout-compliance, scout-feasibility, scout-market,
        scout-naming, scout-positioning, scout-requirements, scout-stakeholders
draft:  draft-pitch, draft-proposal, draft-spec
review: review-code, review-customers, review-design, review-users
flow:   flow-conversation, flow-dataflow, flow-integration, flow-lifecycle,
        flow-resilience, flow-throttle, flow-trigger
trace:  trace-component, trace-contract, trace-deployment, trace-migration,
        trace-permissions, trace-request, trace-skill, trace-state
prove:  prove-analysis, prove-hypothesis, prove-intelligence, prove-interview,
        prove-prototype, prove-publish, prove-synthesize, prove-websearch
listen: listen-adoption, listen-feedback, listen-support
topic:  topic-echo, topic-new, topic-plan, topic-report, topic-status, topic-story
```

No other skill names exist. Do not use `program-plan` in any stage's skills list.

---

### Step 1 — Select relevant skills

List skills from the catalog that apply to {{topic}}. For each: one sentence — what signal it produces. Omit irrelevant skills. Group by namespace.

---

### Step 2 — Actor ordering table

For each namespace actor that will appear as a stage, complete this table.

| Actor | Cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences crossing arc-layer boundaries) |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Strategist (scout) | First actor — no earlier position exists; if delayed: Architect designs without validated assumptions -> Researcher proves a hypothesis with no market grounding -> Reviewer critiques artifacts anchored in untested assumptions |
| Architect+PM (draft) | Cannot run before Strategist; if moved earlier: draft-spec encodes invented requirements -> Researcher builds prototype against unvalidated spec -> Reviewer has no validated baseline to judge against |
| Researcher (prove) | Cannot run before Architect+PM; if moved earlier: prove-prototype builds without a design artifact -> prove-hypothesis tests an unformalized assumption -> Reviewer receives evidence with nothing to compare against |
| Reviewer (review+trace) | Cannot run before Researcher; if moved earlier: review-design critiques without prototype evidence -> prove-publish incorporates no review findings -> topic-story cites a review with no validation backing |
| Field team (listen) | Cannot run before meaningful artifacts exist; if moved earlier: listen-feedback collects reactions to a spec not a feature -> listen-adoption measures document adoption -> topic-status reports adoption with no implementation baseline |
| Synthesizer (topic) | Cannot run before all signal types present; if moved earlier: topic-status aggregates zero depth signals -> topic-plan creates an evidence-free plan -> topic-story writes a narrative with no research or review backing |

Every row uses `->` notation with 3 ordered consequences crossing arc-layer boundaries.

---

### Step 2.5 — Echo Stage Justification

Before designing stages, answer these questions:

1. What signal does `topic-echo` emit when it runs? What does that signal mean for the arc — what state does it assert?
2. What happens if the echo stage runs at stage 2 (before validation)? Trace the consequence using `->` notation, at least 2 hops crossing arc-layer boundaries. (What does the arc-completion signal assert on an arc that has no depth signals yet?)
3. What specific artifact types or signal thresholds must exist before echo fires? Name them. (Not "all stages complete" — what artifact types specifically?)

Write 2–3 sentences answering all three questions. Use this reasoning in Step 3: the final non-echo stage's gate threshold must match the pre-conditions you identified in item 3.

---

### Step 3 — Stage design

Group selected skills into 3–5 stages (plus echo). Each stage:
- Name communicates phase intent (not `stage1`, not a skill name)
- Contains skills producing related signal types
- Precedes stages that depend on its outputs

The final non-echo stage's gate threshold must satisfy the echo pre-conditions identified in Step 2.5.

---

### Step 4 — Gate writing

For every non-echo stage, write a gate using this format:

```
[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present
— removing this gate: [cascade chain, -> notation, 2+ hops crossing arc-layer boundaries]
```

The cascade-if-removed clause is a required element of every gate string.

**Concrete example:**
```
Strategist hands off to Architect+PM when >=3 scout-signal artifacts present
— removing this gate: draft-spec runs without validated requirements -> prove-prototype
builds against an unvalidated design -> review-design critiques with no market-grounded baseline
```

Requirements: `>=N` specific threshold, named artifact type, `->` cascade 2+ hops.

---

### Step 5 — Arc strategy

Write 3–4 sentences explaining why this arc is correct for {{topic}}.

Answer explicitly:
1. What broad-to-deep signal progression does this arc follow?
2. **Specifically:** what is the multi-hop consequence cascade if the first gate (scout handoff) is removed? Trace at least 3 downstream consequences using `->` notation. Name the scout handoff gate — a generic "any gate" answer fails this item.
3. How does the echo stage justification from Step 2.5 anchor the final gate threshold? If the final gate's condition does not match echo's pre-conditions, what does that mean for the arc-completion signal?

---

### Step 6 — Assemble program.yaml

Produce valid YAML:
- Top-level key: `stages` (list)
- Each stage: `name` (string), `skills` (list), `gate` (string)
- Echo stage: `name: echo`, `skills: []`, `auto: true`, no `gate` field
- Only the `echo` stage is named `echo`
- Skills in dependency order
- Every non-echo gate uses the format from Step 4
- No skills outside the catalog
- Final non-echo stage gate threshold satisfies the echo pre-conditions from Step 2.5

Output as a fenced YAML code block.

---

## V-04 — Gate Cascade Notation in Template + Pre-Computation Table

**Variation axis:** V-01 + V-02 (combination)
**Hypothesis:** The pre-computation table (V-02) forces all cascade chains to be reasoned before YAML — establishing what each cascade should say. The `->` notation requirement in the gate format string (V-01) enforces how each cascade is expressed — multi-hop chains with arc-layer crossings. Together they produce well-formed cascades at every boundary: the content is pre-reasoned and the format is structurally required.

---

A program plan that writes gate cascade clauses inline during YAML assembly produces two simultaneous failures: the cascade content is reasoned in isolation at each gate without cross-gate awareness, and even when a cascade clause exists, it collapses to a single consequence because the format string makes no demand on depth. This variation defeats isolated cascade reasoning and single-hop clause content by two structural mechanisms: (1) a Gate Cascade Audit table that pre-computes all cascades before YAML assembly, establishing full cross-gate cascade awareness, and (2) a gate format string that requires `->` notation and minimum cascade depth within the cascade-if-removed element itself.

### Task

Generate `program.yaml` for topic: **{{topic}}**

Stages group Signal skills into coherent phases. Each non-echo stage has a gate. Final stage is always `echo` (`auto: true`, empty skills list). The program is a plan — every skill also runs standalone.

### Skill Catalog (inline — use only these skills)

```
scout:  scout-competitors, scout-compliance, scout-feasibility, scout-market,
        scout-naming, scout-positioning, scout-requirements, scout-stakeholders
draft:  draft-pitch, draft-proposal, draft-spec
review: review-code, review-customers, review-design, review-users
flow:   flow-conversation, flow-dataflow, flow-integration, flow-lifecycle,
        flow-resilience, flow-throttle, flow-trigger
trace:  trace-component, trace-contract, trace-deployment, trace-migration,
        trace-permissions, trace-request, trace-skill, trace-state
prove:  prove-analysis, prove-hypothesis, prove-intelligence, prove-interview,
        prove-prototype, prove-publish, prove-synthesize, prove-websearch
listen: listen-adoption, listen-feedback, listen-support
topic:  topic-echo, topic-new, topic-plan, topic-report, topic-status, topic-story
```

No other skill names exist. Do not use `program-plan` in any stage's skills list.

---

### Step 1 — Select relevant skills

List skills from the catalog that apply to {{topic}}. For each: one sentence — what signal it produces. Group by namespace.

---

### Step 2 — Actor ordering table

For each namespace actor that will appear as a stage, complete this table.

| Actor | Cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences crossing arc-layer boundaries) |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Strategist (scout) | First actor — no earlier position exists; if delayed: Architect designs without validated assumptions -> Researcher proves a hypothesis with no market grounding -> Reviewer critiques artifacts anchored in untested assumptions |
| Architect+PM (draft) | Cannot run before Strategist; if moved earlier: draft-spec encodes invented requirements -> Researcher builds prototype against unvalidated spec -> Reviewer has no validated baseline to judge against |
| Researcher (prove) | Cannot run before Architect+PM; if moved earlier: prove-prototype builds without a design artifact -> prove-hypothesis tests an unformalized assumption -> Reviewer receives evidence with nothing to compare against |
| Reviewer (review+trace) | Cannot run before Researcher; if moved earlier: review-design critiques without prototype evidence -> prove-publish incorporates no review findings -> topic-story cites a review with no validation backing |
| Field team (listen) | Cannot run before meaningful artifacts exist; if moved earlier: listen-feedback collects reactions to a spec not a feature -> listen-adoption measures document adoption -> topic-status reports adoption with no implementation baseline |
| Synthesizer (topic) | Cannot run before all signal types present; if moved earlier: topic-status aggregates zero depth signals -> topic-plan creates an evidence-free plan -> topic-story writes a narrative with no research or review backing |

Every row uses `->` notation with 3 ordered consequences crossing arc-layer boundaries.

---

### Step 3 — Stage design

Group selected skills into 3–5 stages (plus echo). Names communicate phase intent; not `stage1`, not skill names.

---

### Step 4 — Gate Cascade Audit

Before writing any gate strings, complete this audit table for every non-echo stage:

| Stage | Delivering Actor → Receiving Actor | Threshold | Cascade if Removed (-> notation, 2+ hops, crossing arc-layer boundaries) |
|-------|-------------------------------------|-----------|--------------------------------------------------------------------------|
| [stage name] | [Delivering Actor] → [Receiving Actor] | >=N artifact_type | [A -> B -> C] |
| ... | ... | ... | ... |

Requirements:
- Every row: specific numeric threshold
- Every row: `->` cascade with 2+ hops crossing at least one arc-layer boundary
- Complete this ENTIRE table before writing gate strings in Step 5

The cascade chains in this table are the authoritative source for Step 5.

---

### Step 5 — Gate writing

For every non-echo stage, write a gate using this exact format:

```
[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present
— removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries]
```

Use cascade chains from the Step 4 audit. The `->` notation and minimum 2-hop depth are required elements of the cascade-if-removed clause — a single-consequence clause or a clause with no arrows fails this step.

**Concrete example:**
```
Strategist hands off to Architect+PM when >=3 scout-signal artifacts present
— removing this gate: draft-spec runs without validated requirements -> prove-prototype
builds against an unvalidated design -> review-design critiques with no market-grounded baseline
```

---

### Step 6 — Arc strategy

Write 3–4 sentences:
1. What broad-to-deep signal progression does this arc follow?
2. **Specifically:** what is the multi-hop consequence cascade if the first gate (scout handoff) is removed? Trace at least 3 downstream consequences using `->` notation. Name the scout handoff gate — do not answer generically about "any gate."
3. Reference your Gate Cascade Audit from Step 4 — which gate, if removed, has the longest downstream cascade? Why is it the highest-leverage boundary?

---

### Step 7 — Assemble program.yaml

Produce valid YAML:
- Top-level key: `stages` (list)
- Each stage: `name` (string), `skills` (list), `gate` (string)
- Echo stage: `name: echo`, `skills: []`, `auto: true`, no `gate` field
- Only the `echo` stage is named `echo`
- Skills in dependency order
- Every non-echo gate uses the format from Step 5 (actor names + threshold + artifact type + `->` cascade-if-removed)
- No skills outside the catalog

Output as a fenced YAML code block.

---

## V-05 — Full Cascade Integration

**Variation axis:** V-01 + V-02 + V-03 + gate-to-gate chain column (combination)
**Hypothesis:** Adding a gate-to-gate chain column to the Gate Cascade Audit table — where removing gate N explicitly names how it renders gate N+1's threshold unreachable — extends cascade awareness from individual boundary reasoning to full arc-chain reasoning. A model that can trace how removing gate N propagates into gate N+1 failing has demonstrated genuine arc-awareness, not just isolated boundary knowledge. Combined with V-01's notation requirement, V-02's pre-computation, and V-03's echo justification, this produces the most structurally grounded program plan in the R6 set.

---

Four failure modes coexist in program plans: (1) gate cascade clauses with no notation requirement collapse to single-consequence statements; (2) gate strings written inline during YAML assembly have no cross-gate cascade awareness; (3) echo stage treated as convention rather than architectural requirement; (4) each gate's removal consequence is analyzed in isolation without tracing how removing gate N makes gate N+1's threshold unreachable. This variation defeats all four by: embedding `->` notation and depth in the gate format string, pre-computing all cascades in an audit table with a gate-to-gate chain column, requiring explicit echo displacement reasoning, and specifying the highest-leverage first-gate cascade in the arc-strategy step.

### Task

Generate `program.yaml` for topic: **{{topic}}**

Stages group Signal skills into coherent phases. Each non-echo stage has a gate. Final stage is always `echo` (`auto: true`, empty skills list). The program is a plan — every skill also runs standalone.

### Skill Catalog (inline — use only these skills)

```
scout:  scout-competitors, scout-compliance, scout-feasibility, scout-market,
        scout-naming, scout-positioning, scout-requirements, scout-stakeholders
draft:  draft-pitch, draft-proposal, draft-spec
review: review-code, review-customers, review-design, review-users
flow:   flow-conversation, flow-dataflow, flow-integration, flow-lifecycle,
        flow-resilience, flow-throttle, flow-trigger
trace:  trace-component, trace-contract, trace-deployment, trace-migration,
        trace-permissions, trace-request, trace-skill, trace-state
prove:  prove-analysis, prove-hypothesis, prove-intelligence, prove-interview,
        prove-prototype, prove-publish, prove-synthesize, prove-websearch
listen: listen-adoption, listen-feedback, listen-support
topic:  topic-echo, topic-new, topic-plan, topic-report, topic-status, topic-story
```

No other skill names exist. Do not use `program-plan` in any stage's skills list.

---

### Step 1 — Select relevant skills

List skills from the catalog that apply to {{topic}}. For each: one sentence — what signal it produces. Group by namespace.

---

### Step 2 — Actor ordering table

For each namespace actor that will appear as a stage, complete this table.

| Actor | Cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences crossing arc-layer boundaries) |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Strategist (scout) | First actor — no earlier position exists; if delayed: Architect designs without validated assumptions -> Researcher proves a hypothesis with no market grounding -> Reviewer critiques artifacts anchored in untested assumptions |
| Architect+PM (draft) | Cannot run before Strategist; if moved earlier: draft-spec encodes invented requirements -> Researcher builds prototype against unvalidated spec -> Reviewer has no validated baseline to judge against |
| Researcher (prove) | Cannot run before Architect+PM; if moved earlier: prove-prototype builds without a design artifact -> prove-hypothesis tests an unformalized assumption -> Reviewer receives evidence with nothing to compare against |
| Reviewer (review+trace) | Cannot run before Researcher; if moved earlier: review-design critiques without prototype evidence -> prove-publish incorporates no review findings -> topic-story cites a review with no validation backing |
| Field team (listen) | Cannot run before meaningful artifacts exist; if moved earlier: listen-feedback collects reactions to a spec not a feature -> listen-adoption measures document adoption -> topic-status reports adoption with no implementation baseline |
| Synthesizer (topic) | Cannot run before all signal types present; if moved earlier: topic-status aggregates zero depth signals -> topic-plan creates an evidence-free plan -> topic-story writes a narrative with no research or review backing |

Every row uses `->` notation with 3 ordered consequences crossing arc-layer boundaries.

---

### Step 2.5 — Echo Stage Justification

Before designing stages, answer these three questions:

1. What signal does `topic-echo` emit? What arc state does it assert when it fires?
2. What breaks if echo runs at stage 2 (before validation)? Use `->` notation, 2+ hops crossing arc-layer boundaries. What does the arc-completion signal assert on an arc with no depth signals?
3. What artifact types or signal thresholds must be present before echo fires? Name them specifically.

Write 2–3 sentences. The final non-echo stage's gate condition in Step 7 must match your answer to item 3.

---

### Step 3 — Stage design

Group selected skills into 3–5 stages (plus echo). Names communicate phase intent. The final non-echo stage's gate must satisfy the echo pre-conditions from Step 2.5.

---

### Step 4 — Gate Cascade Audit

Before writing any gate strings, complete this audit table for every non-echo stage:

| Stage | Delivering Actor → Receiving Actor | Threshold | Cascade if Removed (-> notation, 2+ hops crossing arc-layer boundaries) | Impact on next gate if this gate removed |
|-------|-------------------------------------|-----------|--------------------------------------------------------------------------|------------------------------------------|
| [stage 1] | [Delivering Actor] → [Receiving Actor] | >=N artifact_type | [A -> B -> C] | Next gate's threshold becomes unreachable because [reason] |
| [stage 2] | ... | ... | ... | Next gate's threshold becomes unreachable because [reason] / This is the final gate — echo fires with [consequence] |
| ... | | | | |

Requirements:
- Every row: specific numeric threshold
- Every row: `->` cascade with 2+ hops crossing at least one arc-layer boundary
- Every row: explicit statement of how removing this gate makes the NEXT gate's threshold unreachable (gate-to-gate chain awareness)
- Complete the ENTIRE table before writing any gate strings in Step 5

---

### Step 5 — Gate writing

For every non-echo stage, write a gate using this exact format:

```
[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present
— removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries]
```

Use cascade chains from Step 4. The `->` notation and minimum 2-hop depth are required elements of the cascade-if-removed clause.

**Concrete example:**
```
Strategist hands off to Architect+PM when >=3 scout-signal artifacts present
— removing this gate: draft-spec runs without validated requirements -> prove-prototype
builds against an unvalidated design -> review-design critiques with no market-grounded baseline
```

---

### Step 6 — Arc strategy

Write 3–4 sentences:
1. What broad-to-deep signal progression does this arc follow?
2. **Specifically:** what is the multi-hop consequence cascade if the first gate (scout handoff) is removed? Trace at least 3 downstream consequences using `->` notation. Name the scout handoff gate specifically — do not answer generically.
3. Using your Gate Cascade Audit gate-to-gate chain column: trace what happens when the first gate is removed through to the second gate's condition also becoming unreachable. What does this chain reveal about why gate ordering is not arbitrary?
4. How does the echo stage justification (Step 2.5) anchor the final gate threshold? What would it mean for the arc-completion signal if the final gate's condition did not match echo's pre-conditions?

---

### Step 7 — Assemble program.yaml

Produce valid YAML:
- Top-level key: `stages` (list)
- Each stage: `name` (string), `skills` (list), `gate` (string)
- Echo stage: `name: echo`, `skills: []`, `auto: true`, no `gate` field
- Only the `echo` stage is named `echo`
- Skills in dependency order
- Every non-echo gate uses the format from Step 5 (actor names + threshold + artifact type + `->` cascade-if-removed)
- Final non-echo stage gate condition satisfies echo pre-conditions from Step 2.5
- No skills outside the catalog

Output as a fenced YAML code block.

---

## R6 Hypotheses to Resolve

| ID | Hypothesis | Variation | What to look for in output |
|----|------------|-----------|---------------------------|
| R6-H01 | Does `->` notation + depth requirement in the gate format string (V-01 axis) produce multi-hop cascade chains at every gate boundary, or do models still collapse to single-consequence clauses? | V-01, V-04, V-05 | Count hops in each gate's cascade-if-removed clause; check for `->` arrows |
| R6-H02 | Does the Gate Cascade Audit pre-computation table (V-02 axis) produce more consequential and cross-linked cascades than inline YAML authoring? | V-02, V-04, V-05 | Compare cascade depth and cross-gate consistency vs. V-01 |
| R6-H03 | Does echo stage displacement reasoning (V-03 axis) produce a final gate threshold that is causally grounded in the echo pre-condition, rather than a generic "all stages complete" condition? | V-03, V-05 | Check whether the final gate condition names specific artifact types matching Step 2.5 answer |
| R6-H04 | Does the gate-to-gate chain column (V-05 axis) produce output that explicitly links removing gate N to gate N+1's threshold becoming unreachable? | V-05 | Look for cross-gate cascade traces in the arc strategy and gate strings |
| R6-H05 | Does the updated 47-skill catalog (with `scout-competitors` and `trace-skill` added vs. R5's 46) affect skill selection quality? | All | Check whether scout-competitors or trace-skill appear in plans where relevant |

---

## Predicted R6 scoring (pre-run estimate)

All 5 variations are designed to score **165/165** under the v6 rubric. The variation axes are additive, not substitutive — no baseline criterion is sacrificed for any axis. The axes test structural dimensions beyond the current ceiling:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-22 (gate cascade clause) | PASS | PASS | PASS | PASS | PASS |
| C-23 (first-gate specificity) | PASS | PASS | PASS | PASS | PASS |
| All other criteria | PASS | PASS | PASS | PASS | PASS |
| **Predicted total** | **165** | **165** | **165** | **165** | **165** |

If any variation scores below 165, the miss indicates a new rubric gap for R7. Watch especially for:
- V-01 misses: gate `->` notation requirement not honored → potential C-24 (gate cascade notation)
- V-02 misses: audit table not consulted → potential C-25 (pre-computation completeness)
- V-03 misses: echo justification not used in final gate → potential C-26 (echo-gate alignment)
- V-05 misses: gate-to-gate chain not traced → potential C-27 (inter-gate cascade chain)
