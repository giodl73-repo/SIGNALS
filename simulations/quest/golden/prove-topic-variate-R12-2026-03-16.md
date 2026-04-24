---
skill: quest-variate
skill_target: prove-topic
round: R12
date: 2026-03-16
rubric: prove-topic-rubric-v10-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [inertia_framing, lifecycle_emphasis, output_format]
  combined: [V-04 (phrasing_register + role_sequence), V-05 (all_four)]
r11_anchor: >
  R11 V-01 scored 73.5 against v10 rubric. Stage 5 was truncated in input
  (C-01 partial, C-04/C-13/C-14/C-18 fail). No recovery procedure (C-24 fail).
  Scout anchor body citation partial (C-20). Entry conditions did not name
  prior stage checklist outputs (C-26 partial). C-33 and C-34 were identified
  as excellence signals in R11 and are now v10 criteria. All R12 variations
  carry complete Stage 5, recovery procedure, dual-layer anchor, and
  named-checklist entry conditions as baseline.
r12_targets: >
  V-01 makes the displacement context the structural axis — both fields
  in YAML for every stage artifact (C-34), THIN flags name displacement
  claim against comparator in flag prose (C-33), synthesis framed as
  displacement case (C-32). V-02 makes checklists the causal binding axis
  — named Exit Gates with dual-output emission rule co-located as final
  checklist item (C-31), causal commitment stated once before Stage 1
  (C-25/C-29). V-03 makes path traceability the structural axis — PATH
  CHAIN VERIFICATION table at every boundary (C-30), three-way path chain
  verifiable from single structure (C-28), FORM A/B as named dual schema
  (C-18). V-04 uses imperative register and leads with recovery (C-24),
  structural blocking gate before Stage 1 (C-10), scout anchor dual-layer
  check (C-20). V-05 combines all four.
---

# prove-topic — Quest Variate R12

## Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|----------------|------------|
| V-01 | Inertia Framing | C-32, C-33, C-34 | Making displacement fields structural YAML in all 5 artifacts enforces C-34; THIN flag template requiring comparator prose enforces C-33 |
| V-02 | Lifecycle Emphasis | C-25, C-29, C-31 | Co-locating the dual-output trigger as the final checklist item, with a campaign-level causal commitment before Stage 1, makes the binding inescapable by construction |
| V-03 | Output Format | C-28, C-30 | A named 3-row PATH CHAIN VERIFICATION table at each boundary makes the three-way path chain auditable from a single scannable structure without cross-section lookup |
| V-04 | Phrasing Register + Role Sequence | C-10, C-20, C-24 | Imperative register plus a recovery-first preamble ordering raises compliance because commands feel mandatory; structural blocking (not prose warning) enforces the scout gate |
| V-05 | Full Integration | C-01 through C-34 | Combining all four axes produces maximum coverage with no axis trade-off |

---

## V-01 — Inertia Framing

**Axis**: Inertia framing — how prominently and structurally the status-quo competitor is featured
**Hypothesis**: Making `status_quo_comparator` and `inertia_vulnerability` required YAML fields in every stage artifact (not only CAMPAIGN OPEN) satisfies C-34; requiring every THIN flag body to name the displacement claim against the comparator satisfies C-33; framing synthesis as a displacement brief satisfies C-32 — all three without displacing any prior structural requirement.

---

# prove-topic

Run the full prove evidence campaign for **{topic}**:
prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis → prove-synthesize.

Five stages. Five writes. No batching. Forward-only.

---

## INTERRUPTED-CAMPAIGN RECOVERY

If resuming a partial run:
1. Glob `simulations/prove/prove-*/` — find the most recent artifact for **{topic}**
2. Read its `stages_completed` field — lists which stages have run
3. Find the first gate clearance string absent from context (e.g., `GATE-1 CLEARED.`)
4. Resume from that stage; do not re-run stages already in `stages_completed`

---

## CAMPAIGN OPEN

Before Stage 1: read the most recent scout artifact for **{topic}**:
```
Glob: simulations/scout/scout-*/{topic}-scout-*-*.md
```

**If no scout artifact exists: STOP.** Run `/scout-feasibility {topic}` before continuing. Stage 1 cannot begin until a scout artifact is confirmed.

Extract both displacement fields and record them:

| Field | Definition | Value |
|-------|-----------|-------|
| `status_quo_comparator` | The incumbent solution being displaced — what users rely on today | _extracted_ |
| `inertia_vulnerability` | The specific resistance point making displacement non-trivial | _extracted_ |

Both fields must be non-empty before Stage 1 begins. Both fields **propagate as required YAML frontmatter into every stage artifact in this campaign (Stages 1–5)** — this is a structural requirement enforced at each stage's write instruction. Also record the scout artifact path; it becomes the `scout_anchor` value.

---

## Stage 1 — prove-hypothesis

**Entry**: CAMPAIGN OPEN complete. `status_quo_comparator` named. `inertia_vulnerability` named. Scout artifact path recorded.

Frame the hypothesis as a **displacement claim** — specifically what makes displacing `{status_quo_comparator}` worthwhile. Required:
- Name `{status_quo_comparator}` as the incumbent being displaced
- Identify which aspect of `inertia_vulnerability` the hypothesis must overcome
- List 3–5 testable sub-claims, each as a displacement assertion
- State the falsification condition: what evidence would confirm displacement fails?
- Cite the scout anchor path **inline in the artifact body** (required; body citation distinct from YAML `scout_anchor:`)

**Write** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`

```yaml
skill: prove-hypothesis
topic: {topic}
date: {date}
scout_anchor: simulations/scout/scout-{type}/{topic}-scout-{type}-{date}.md
status_quo_comparator: "{value from CAMPAIGN OPEN}"
inertia_vulnerability: "{value from CAMPAIGN OPEN}"
stages_completed: [stage-1-hypothesis]
```

**Stage 1 Completion Checklist**:
- [ ] Hypothesis names `{status_quo_comparator}` as the incumbent being displaced
- [ ] `inertia_vulnerability` named as the barrier the hypothesis must clear
- [ ] 3–5 displacement sub-claims listed
- [ ] Falsification condition stated
- [ ] Scout anchor path cited inline in artifact body (not only in YAML `scout_anchor:`)
- [ ] YAML includes `scout_anchor`, `status_quo_comparator`, `inertia_vulnerability`, `stages_completed`
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-1-hypothesis` to `stages_completed` in this artifact; (2) emit `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`. Single event, both outputs.**

---

## Stage 2 — prove-websearch

**Entry**: Stage 1 completion checklist satisfied AND `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` confirmed in context.

Search external sources for evidence on Stage 1's displacement sub-claims. For each source, note whether it supports or weakens the case for displacing `{status_quo_comparator}`. If evidence is absent or thin for a sub-claim, flag **at point of discovery**:

```
THIN: [{sub-claim text}] — weakens displacement of {status_quo_comparator} because [{reason}]
```

Every `THIN:` flag body must name `{status_quo_comparator}` explicitly. Do not defer flags to synthesis.

**Write** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`

```yaml
skill: prove-websearch
topic: {topic}
date: {date}
status_quo_comparator: "{same value as Stage 1}"
inertia_vulnerability: "{same value as Stage 1}"
stages_completed: [stage-1-hypothesis, stage-2-websearch]
```

**Stage 2 Completion Checklist**:
- [ ] External evidence gathered for each Stage 1 displacement sub-claim
- [ ] THIN flags written inline at point of discovery, each naming `{status_quo_comparator}`
- [ ] YAML includes both displacement fields and updated `stages_completed`
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-2-websearch` to `stages_completed`; (2) emit `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`. Single event, both outputs.**

---

## Stage 3 — prove-intelligence

**Entry**: Stage 2 completion checklist satisfied AND `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` confirmed in context.

Scan internal sources — existing artifacts, prior simulations, specs, codebase — for evidence on the displacement sub-claims. Same `THIN:` flag protocol as Stage 2; every flag body must name `{status_quo_comparator}`.

**Write** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`

```yaml
skill: prove-intelligence
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]
```

**Stage 3 Completion Checklist**:
- [ ] Internal sources scanned for each displacement sub-claim
- [ ] THIN flags written inline at point of discovery, each naming `{status_quo_comparator}`
- [ ] YAML includes both displacement fields and updated `stages_completed`
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-3-intelligence` to `stages_completed`; (2) emit `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`. Single event, both outputs.**

---

## Stage 4 — prove-analysis

**Entry**: Stage 3 completion checklist satisfied AND `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` confirmed in context.

**GATE 4A — Part A: Flag Aggregation** (complete before Part B begins):

Build the aggregation table from all THIN flags in Stages 2 and 3:

| # | THIN Flag | Source Stage | Displacement Claim Weakened vs `{status_quo_comparator}` |
|---|-----------|-------------|----------------------------------------------------------|
| 1 | … | Stage 2/3 | … |

If no THIN flags exist, write: "No THIN findings — aggregation table empty." Emit `GATE-4A CLEARED.` when the table is complete. Part B may not begin before GATE-4A is cleared.

**Part B: Hypothesis Mapping**

For each row: name the Stage 1 sub-claim weakened, state how this affects the displacement argument against `{status_quo_comparator}`, and assign a confidence impact (High/Medium/Low).

**Write** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`

```yaml
skill: prove-analysis
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]
```

**Stage 4 Completion Checklist**:
- [ ] GATE-4A cleared (aggregation table complete or empty-row stated)
- [ ] Every THIN flag mapped to a Stage 1 displacement sub-claim
- [ ] Confidence impact stated for each mapping vs `{status_quo_comparator}`
- [ ] YAML includes both displacement fields and updated `stages_completed`
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-4-analysis` to `stages_completed`; (2) emit `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`. Single event, both outputs.**

---

## Stage 5 — prove-synthesize

**Entry**: Stage 4 completion checklist satisfied AND `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` confirmed in context.

Synthesize all evidence into a brief. Frame the synthesis as **the case for displacing `{status_quo_comparator}`** — what the evidence confirms, what it weakens, and the adjusted confidence for the displacement claim.

**Confidence adjustment table — emit one named form:**

**FORM A** (when THIN flags exist — one row per flag):

| THIN Flag | Source Stage | Weakened Displacement Claim vs `{status_quo_comparator}` | Confidence Delta |
|-----------|-------------|----------------------------------------------------------|-----------------|
| … | … | … | −N% |

**FORM B** (when no THIN flags exist — always emit; never omit this section):

| THIN Flag | Source Stage | Weakened Displacement Claim | Confidence Delta |
|-----------|-------------|----------------------------|-----------------|
| no THIN findings | — | — | 0 |

The label `FORM A` or `FORM B` must appear as a named heading above the table.

Close with: **The next step for this topic is `/topic-story`.**

**Write** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`

```yaml
skill: prove-synthesize
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis, stage-5-synthesize]
```

**Stage 5 Completion Checklist**:
- [ ] Confidence adjustment table emitted (FORM A or FORM B, with label heading)
- [ ] Synthesis framed as displacement case against `{status_quo_comparator}`
- [ ] `/topic-story` explicitly named as the next step
- [ ] YAML includes both displacement fields and complete `stages_completed`
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-5-synthesize` to `stages_completed`; (2) emit `GATE-5 CLEARED. → simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`. Single event, both outputs.**

---

Campaign complete. All 5 artifacts written. Displacement case assembled. Hand off to `/topic-story`.

---

## V-02 — Lifecycle Emphasis

**Axis**: Lifecycle emphasis — how explicit stage boundaries are, and how causally bound the three output channels are
**Hypothesis**: Declaring a campaign-level causal commitment statement before Stage 1 that binds checklist completion to both output channels — then embedding the dual-output emission rule as the final item of each named Exit Gate checklist — makes C-31 inescapable by construction and C-29 undeniable by placement; no variation at execution can omit either output without violating the Exit Gate structure itself.

---

# prove-topic

Run the full prove evidence campaign for **{topic}**:
prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis → prove-synthesize.

Five stages. Five Exit Gates. Five writes. No batching. Forward-only.

---

## INTERRUPTED-CAMPAIGN RECOVERY

If resuming a partial run:
1. Glob `simulations/prove/prove-*/` — find the most recent artifact for **{topic}**
2. Read its `stages_completed` field — lists which stages have completed
3. Find the first gate clearance string absent from context (e.g., `GATE-1 CLEARED.`)
4. Resume from that stage; completed stages are final

---

## CAMPAIGN OPEN

Before Stage 1: read the most recent scout artifact for **{topic}**:
```
Glob: simulations/scout/scout-*/{topic}-scout-*-*.md
```

**If no scout artifact exists: STOP.** Run `/scout-feasibility {topic}` first. Stage 1 cannot begin without a confirmed scout artifact.

Record: scout artifact path (becomes `scout_anchor`), topic name, date.

---

## CAUSAL COMMITMENT — read before Stage 1

In this campaign, **each stage's Exit Gate completion is the sole trigger for two outputs**:
1. Appending the stage identifier to `stages_completed` in the artifact
2. Emitting the named gate clearance string with embedded artifact path

Neither output is emitted before the Exit Gate is cleared. Both outputs are emitted at the same moment Exit Gate is cleared. This binding holds across all five stages without exception. The dual-output emission rule appears as the final item in each Exit Gate checklist — co-located, not referenced from a separate block.

---

## Stage 1 — prove-hypothesis

**Stage 1 Entry Gate**: Scout artifact confirmed. Scout path recorded. All preconditions from CAMPAIGN OPEN met.

Write the hypothesis for **{topic}**. Required content:
- Central claim about {topic}
- Scout anchor path cited **inline in the artifact body** (body citation; distinct from YAML field)
- 3–5 falsifiable sub-claims
- Falsification condition

**Write** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`

```yaml
skill: prove-hypothesis
topic: {topic}
date: {date}
scout_anchor: simulations/scout/scout-{type}/{topic}-scout-{type}-{date}.md
stages_completed: [stage-1-hypothesis]
```

**Stage 1 Exit Gate**:
- [ ] Central claim stated
- [ ] Scout anchor path cited inline in artifact body (not only in YAML)
- [ ] 3–5 falsifiable sub-claims listed
- [ ] Falsification condition stated
- [ ] YAML frontmatter written: `scout_anchor`, `stages_completed: [stage-1-hypothesis]`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) confirm `stages_completed` in this artifact contains `stage-1-hypothesis`; (2) emit `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`. Checklist completion is the sole trigger. Both outputs. Single event.**

---

## Stage 2 — prove-websearch

**Stage 2 Entry Gate**: Stage 1 Exit Gate cleared. `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` confirmed in context.

Search external sources for evidence on each Stage 1 sub-claim. Note supporting vs. weakening evidence per sub-claim. Flag thin or absent evidence inline at point of discovery:

```
THIN: [{sub-claim}] — [{reason evidence is absent or insufficient}]
```

Do not defer THIN flags.

**Write** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`

```yaml
skill: prove-websearch
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch]
```

**Stage 2 Exit Gate**:
- [ ] All Stage 1 sub-claims searched externally
- [ ] Evidence noted per sub-claim (supporting or weakening)
- [ ] THIN flags written inline at point of discovery
- [ ] YAML includes updated `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) confirm `stages_completed` contains `stage-2-websearch`; (2) emit `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`. Checklist completion is the sole trigger. Both outputs. Single event.**

---

## Stage 3 — prove-intelligence

**Stage 3 Entry Gate**: Stage 2 Exit Gate cleared. `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` confirmed in context.

Scan internal sources — existing artifacts, prior simulations, specs, codebase — for evidence on Stage 1 sub-claims. Same `THIN:` flag protocol as Stage 2.

**Write** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`

```yaml
skill: prove-intelligence
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]
```

**Stage 3 Exit Gate**:
- [ ] Internal sources scanned per Stage 1 sub-claim
- [ ] THIN flags written inline at point of discovery
- [ ] YAML includes updated `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) confirm `stages_completed` contains `stage-3-intelligence`; (2) emit `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`. Checklist completion is the sole trigger. Both outputs. Single event.**

---

## Stage 4 — prove-analysis

**Stage 4 Entry Gate**: Stage 3 Exit Gate cleared. `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` confirmed in context.

**GATE 4A — Aggregation (Part A must complete before Part B)**:

Collect all THIN flags from Stages 2–3 into one aggregation table:

| # | THIN Flag | Source Stage | Sub-Claim Weakened |
|---|-----------|-------------|-------------------|
| 1 | … | … | … |

If no flags: write "No THIN findings." Emit `GATE-4A CLEARED.` when table is complete.

**Part B — Hypothesis Mapping**: For each aggregated flag, map the weakened sub-claim and state confidence impact.

**Write** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`

```yaml
skill: prove-analysis
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]
```

**Stage 4 Exit Gate**:
- [ ] GATE-4A cleared (aggregation complete)
- [ ] All THIN flags mapped to Stage 1 sub-claims (Part B complete)
- [ ] YAML includes updated `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) confirm `stages_completed` contains `stage-4-analysis`; (2) emit `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`. Checklist completion is the sole trigger. Both outputs. Single event.**

---

## Stage 5 — prove-synthesize

**Stage 5 Entry Gate**: Stage 4 Exit Gate cleared. `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` confirmed in context.

Synthesize all evidence into a brief ready for `/topic-story`.

**Confidence adjustment table — emit one of two named forms:**

**FORM A** (THIN flags exist):

| THIN Flag | Source Stage | Sub-Claim Weakened | Confidence Delta |
|-----------|-------------|-------------------|-----------------|
| … | … | … | −N% |

**FORM B** (no THIN flags — always emit this form; never omit):

| THIN Flag | Source Stage | Sub-Claim Weakened | Confidence Delta |
|-----------|-------------|-------------------|-----------------|
| no THIN findings | — | — | 0 |

Label heading (`FORM A` or `FORM B`) must appear above the table. Close with: **The next step for this topic is `/topic-story`.**

**Write** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`

```yaml
skill: prove-synthesize
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis, stage-5-synthesize]
```

**Stage 5 Exit Gate**:
- [ ] Confidence adjustment table emitted (FORM A or FORM B, labeled)
- [ ] `/topic-story` named as next step
- [ ] YAML includes complete `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) confirm `stages_completed` contains `stage-5-synthesize`; (2) emit `GATE-5 CLEARED. → simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`. Checklist completion is the sole trigger. Both outputs. Single event.**

---

Campaign complete. All 5 artifacts written. Hand off to `/topic-story`.

---

## V-03 — Output Format

**Axis**: Output format — table-dominant, path-chain-centric
**Hypothesis**: Placing a named PATH CHAIN VERIFICATION table with exactly three rows at every stage boundary — (1) write instruction path, (2) gate clearance path, (3) entry condition path — makes the three-way chain auditable from a single scannable structure without any cross-section lookup; this satisfies C-30 and makes C-28 verifiable statically.

---

# prove-topic

Run the full prove evidence campaign for **{topic}**:
prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis → prove-synthesize.

Five stages. Five writes. No batching. Forward-only.

---

## INTERRUPTED-CAMPAIGN RECOVERY

If resuming a partial run:
1. Glob `simulations/prove/prove-*/` — find the most recent artifact for **{topic}**
2. Read its `stages_completed` field
3. Find the first gate clearance string absent from context
4. Resume from that stage

---

## CAMPAIGN OPEN

Read the most recent scout artifact for **{topic}**:
```
Glob: simulations/scout/scout-*/{topic}-scout-*-*.md
```

**If absent: STOP.** Run `/scout-feasibility {topic}` first.

Record:

| Field | Value |
|-------|-------|
| Scout artifact path | `simulations/scout/scout-{type}/{topic}-scout-{type}-{date}.md` |
| Topic | {topic} |
| Date | {date} |

---

## Stage 1 — prove-hypothesis

**Entry**: Scout artifact confirmed. Path recorded.

Write the hypothesis for **{topic}**:
- Central claim, scout anchor cited inline in body (not only YAML), 3–5 sub-claims, falsification condition

**Write** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`

```yaml
skill: prove-hypothesis
topic: {topic}
date: {date}
scout_anchor: simulations/scout/scout-{type}/{topic}-scout-{type}-{date}.md
stages_completed: [stage-1-hypothesis]
```

**Stage 1 Completion Checklist**:
- [ ] Central claim stated
- [ ] Scout anchor path cited inline in artifact body
- [ ] 3–5 sub-claims listed
- [ ] Falsification condition stated
- [ ] YAML written with `scout_anchor`, `stages_completed`
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-1-hypothesis` to `stages_completed`; (2) emit `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 1 → Stage 2

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 1 | Stage 1 write | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| (2) Gate clearance — GATE-1 CLEARED | GATE-1 clearance string | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| (3) Entry condition — Stage 2 confirms | Stage 2 entry | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |

All three rows must name the identical path. Stage 2 cannot begin if any row differs.

---

## Stage 2 — prove-websearch

**Entry**: GATE-1 CLEARED confirmed. Path confirmed: `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`.

Search external sources for evidence on Stage 1 sub-claims. Flag thin evidence inline:

```
THIN: [{sub-claim}] — [{reason}]
```

**Write** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`

```yaml
skill: prove-websearch
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch]
```

**Stage 2 Completion Checklist**:
- [ ] All sub-claims searched externally
- [ ] THIN flags written inline
- [ ] YAML updated
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-2-websearch` to `stages_completed`; (2) emit `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 2 → Stage 3

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 2 | Stage 2 write | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| (2) Gate clearance — GATE-2 CLEARED | GATE-2 clearance string | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| (3) Entry condition — Stage 3 confirms | Stage 3 entry | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |

---

## Stage 3 — prove-intelligence

**Entry**: GATE-2 CLEARED confirmed. Path confirmed: `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`.

Scan internal sources for evidence on Stage 1 sub-claims. Same THIN flag protocol.

**Write** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`

```yaml
skill: prove-intelligence
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]
```

**Stage 3 Completion Checklist**:
- [ ] Internal sources scanned
- [ ] THIN flags written inline
- [ ] YAML updated
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-3-intelligence` to `stages_completed`; (2) emit `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 3 → Stage 4

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 3 | Stage 3 write | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| (2) Gate clearance — GATE-3 CLEARED | GATE-3 clearance string | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| (3) Entry condition — Stage 4 confirms | Stage 4 entry | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |

---

## Stage 4 — prove-analysis

**Entry**: GATE-3 CLEARED confirmed. Path confirmed: `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`.

**GATE 4A — Part A: Flag Aggregation** (complete before Part B):

| # | THIN Flag | Source Stage | Sub-Claim Weakened |
|---|-----------|-------------|-------------------|
| 1 | … | … | … |

Emit `GATE-4A CLEARED.` when complete. Then begin Part B: map each flag to its confidence impact.

**Write** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`

```yaml
skill: prove-analysis
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]
```

**Stage 4 Completion Checklist**:
- [ ] GATE-4A cleared
- [ ] All flags mapped (Part B complete)
- [ ] YAML updated
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-4-analysis` to `stages_completed`; (2) emit `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 4 → Stage 5

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 4 | Stage 4 write | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| (2) Gate clearance — GATE-4 CLEARED | GATE-4 clearance string | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| (3) Entry condition — Stage 5 confirms | Stage 5 entry | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |

---

## Stage 5 — prove-synthesize

**Entry**: GATE-4 CLEARED confirmed. Path confirmed: `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`.

Synthesize all evidence into a brief for `/topic-story`. Confidence adjustment table — emit one named form:

**FORM A** (THIN flags exist):

| THIN Flag | Source Stage | Sub-Claim Weakened | Confidence Delta |
|-----------|-------------|-------------------|-----------------|
| … | … | … | −N% |

**FORM B** (no THIN flags — always emit; never omit):

| THIN Flag | Source Stage | Sub-Claim Weakened | Confidence Delta |
|-----------|-------------|-------------------|-----------------|
| no THIN findings | — | — | 0 |

Label heading (`FORM A` or `FORM B`) must appear above the table. Close with: **The next step for this topic is `/topic-story`.**

**Write** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`

```yaml
skill: prove-synthesize
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis, stage-5-synthesize]
```

**Stage 5 Completion Checklist**:
- [ ] FORM A or FORM B emitted with label heading
- [ ] `/topic-story` named as next step
- [ ] YAML complete
- [ ] **DUAL OUTPUT TRIGGER — When all items above are checked: (1) append `stage-5-synthesize` to `stages_completed`; (2) emit `GATE-5 CLEARED. → simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`. Single event, both outputs.**

---

Campaign complete. All 5 artifacts written. Hand off to `/topic-story`.

---

## V-04 — Phrasing Register + Role Sequence

**Axis**: Phrasing register (imperative) + Role sequence (recovery-first ordering)
**Hypothesis**: Leading with the recovery procedure as the first structural block (before CAMPAIGN OPEN) signals that campaigns are resumable by design; imperative register throughout makes every gate and write feel mandatory rather than advisory; a numbered blocking procedure for the scout gate (C-10) is harder to skip than a prose warning because it requires explicit numbered-step completion.

---

# prove-topic

Run the full prove evidence campaign for **{topic}**.

---

## STEP 0 — RECOVERY CHECK (read first)

Check if this is a resumption before doing anything else.

1. Glob `simulations/prove/prove-*/` for any existing artifact with **{topic}** in the filename.
2. If found: read the most recent artifact. Read its `stages_completed` field.
3. Identify which gate clearance strings are absent from context. The absent gates tell you where to resume.
4. If resuming: skip to the first incomplete stage. Do not redo completed stages.
5. If no artifacts exist: continue to STEP 1.

---

## STEP 1 — SCOUT GATE (structural block)

Do not proceed to Stage 1 until all four checks below pass:

1. Glob `simulations/scout/scout-*/{topic}-scout-*-*.md`.
2. Confirm at least one file matches.
3. Read the most recent match. Confirm it contains evidence about **{topic}**.
4. Record the full file path. This path is required for `scout_anchor` in Stage 1 YAML and for inline body citation in Stage 1.

**If any check fails: STOP.** Run `/scout-feasibility {topic}`. Return to STEP 1 after it completes.

Only after all four checks pass does Stage 1 begin.

---

## STAGE 1 — prove-hypothesis

**Entry condition**: STEP 1 scout gate passed. Scout path recorded.

Write the hypothesis. Do it now.

- State the central claim about **{topic}**.
- Cite the scout anchor path **in the artifact body** — write the full path as a line of text in the artifact, separate from the YAML `scout_anchor:` field. Both locations required.
- List 3–5 falsifiable sub-claims.
- State what evidence would falsify the hypothesis.

**Write** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`

Frontmatter:
```yaml
skill: prove-hypothesis
topic: {topic}
date: {date}
scout_anchor: simulations/scout/scout-{type}/{topic}-scout-{type}-{date}.md
stages_completed: [stage-1-hypothesis]
```

Checklist before proceeding:
- [ ] Central claim written
- [ ] Scout anchor path written in body text (not only YAML)
- [ ] 3–5 sub-claims written
- [ ] Falsification condition written
- [ ] YAML written
- [ ] **When all above checked: append `stage-1-hypothesis` to `stages_completed`. Emit `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`. Both happen now. Neither happens before.**

---

## STAGE 2 — prove-websearch

**Entry condition**: `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` is present in context. Do not search before this string appears.

Search the web. Find evidence for and against each Stage 1 sub-claim. Right now, not later.

When evidence is thin or missing: write this immediately, inline, at the point you notice it — do not save it for later:

```
THIN: [{the sub-claim}] — [{why the evidence is thin}]
```

Do not batch THIN flags at the end.

**Write** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`

Frontmatter:
```yaml
skill: prove-websearch
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch]
```

Checklist before proceeding:
- [ ] All sub-claims searched
- [ ] Evidence noted per sub-claim
- [ ] THIN flags written inline
- [ ] YAML written
- [ ] **When all above checked: append `stage-2-websearch` to `stages_completed`. Emit `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`. Both happen now.**

---

## STAGE 3 — prove-intelligence

**Entry condition**: `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` is present in context.

Search internally. Read existing artifacts, specs, and code for evidence on Stage 1 sub-claims. Same inline THIN flag rule as Stage 2.

**Write** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`

Frontmatter:
```yaml
skill: prove-intelligence
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]
```

Checklist before proceeding:
- [ ] Internal sources searched per sub-claim
- [ ] THIN flags written inline
- [ ] YAML written
- [ ] **When all above checked: append `stage-3-intelligence` to `stages_completed`. Emit `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`. Both happen now.**

---

## STAGE 4 — prove-analysis

**Entry condition**: `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` is present.

**Do Part A first. Do not start Part B until Part A is done.**

**Part A — collect all THIN flags:**

| # | Flag | Stage | Sub-Claim |
|---|------|-------|-----------|
| 1 | … | … | … |

Write "no THIN findings" if none. Emit `GATE-4A CLEARED.`

**Part B — map each flag to its effect on the hypothesis.** State confidence impact per flag.

**Write** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`

Frontmatter:
```yaml
skill: prove-analysis
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]
```

Checklist before proceeding:
- [ ] GATE-4A cleared
- [ ] Flags mapped in Part B
- [ ] YAML written
- [ ] **When all above checked: append `stage-4-analysis` to `stages_completed`. Emit `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`. Both happen now.**

---

## STAGE 5 — prove-synthesize

**Entry condition**: `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` is present.

Write the synthesis brief. Answer the question: does the evidence support the hypothesis? What got weakened?

Emit the confidence adjustment table. Use FORM A if there were THIN flags; use FORM B if there were none.

**FORM A:**

| THIN Flag | Stage | Sub-Claim Weakened | Confidence Delta |
|-----------|-------|--------------------|-----------------|
| … | … | … | −N% |

**FORM B** (emit even when empty — do not skip):

| THIN Flag | Stage | Sub-Claim Weakened | Confidence Delta |
|-----------|-------|--------------------|-----------------|
| no THIN findings | — | — | 0 |

Write the label `FORM A` or `FORM B` as a heading above the table.

End with this line: **The next step for this topic is `/topic-story`.**

**Write** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`

Frontmatter:
```yaml
skill: prove-synthesize
topic: {topic}
date: {date}
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis, stage-5-synthesize]
```

Checklist before finishing:
- [ ] FORM A or FORM B written with label heading
- [ ] `/topic-story` named as next step
- [ ] YAML written
- [ ] **When all above checked: append `stage-5-synthesize` to `stages_completed`. Emit `GATE-5 CLEARED. → simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`. Both happen now.**

---

Done. Five artifacts written. Hand to `/topic-story`.

---

## V-05 — Full Integration

**Axis**: All four axes combined
**Hypothesis**: Combining inertia framing (C-32/C-33/C-34 via YAML propagation and displacement-typed THIN flags), lifecycle causal binding (C-25/C-29/C-31 via dual-output trigger as final checklist item with commitment preamble), PATH CHAIN VERIFICATION tables (C-28/C-30 via three-row tables at every boundary), and imperative recovery-first ordering (C-10/C-24 via blocking STEP 0 and STEP 1) achieves maximum criterion coverage while each axis reinforces the others: the incumbent name in every YAML makes path traceability meaningful; the causal binding makes the YAML propagation mandatory; the path tables make every gate auditable; the imperative register makes every structural requirement feel unavoidable.

---

# prove-topic

Run the full prove evidence campaign for **{topic}**:
prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis → prove-synthesize.

Five stages. Five Exit Gates. Five writes. Forward-only. No batching.

---

## STEP 0 — RECOVERY CHECK (read before anything else)

1. Glob `simulations/prove/prove-*/` for any existing artifact with **{topic}** in the filename.
2. If found: read the most recent. Read its `stages_completed` field and its `status_quo_comparator` + `inertia_vulnerability` fields.
3. Find the first gate clearance string absent from context. Resume from that stage.
4. If no existing artifacts: continue to STEP 1.

---

## STEP 1 — SCOUT GATE (structural block — all four checks required)

1. Glob `simulations/scout/scout-*/{topic}-scout-*-*.md`.
2. Confirm at least one file matches.
3. Read the most recent match. Confirm it contains evidence about **{topic}**.
4. Record the full file path as the `scout_anchor`.

**If any check fails: STOP.** Run `/scout-feasibility {topic}`. Return here.

---

## CAMPAIGN OPEN (displacement context)

From the scout artifact, extract both fields:

| Field | Definition | Value |
|-------|-----------|-------|
| `status_quo_comparator` | The incumbent being displaced — what users rely on today | _extracted_ |
| `inertia_vulnerability` | The resistance point making displacement non-trivial | _extracted_ |

Both fields must be non-empty before Stage 1 begins. Both fields **propagate into the YAML frontmatter of every stage artifact (Stages 1–5)**. This is a structural requirement. Neither field is optional in any stage's YAML.

---

## CAUSAL COMMITMENT

Each stage's Exit Gate completion is the **sole trigger** for two outputs:
1. Appending the stage identifier to `stages_completed`
2. Emitting the named gate clearance string with embedded artifact path

Both outputs fire at Exit Gate clearance. Neither fires before. The dual-output emission rule is the final item in each Exit Gate checklist — co-located, not separate.

---

## Stage 1 — prove-hypothesis

**Entry**: STEP 1 scout gate passed. CAMPAIGN OPEN complete. Both displacement fields recorded.

Frame the hypothesis as a displacement claim against `{status_quo_comparator}`:
- Name `{status_quo_comparator}` as the incumbent being displaced
- Identify which aspect of `inertia_vulnerability` the hypothesis must overcome
- List 3–5 testable displacement sub-claims
- State the falsification condition
- Cite the scout anchor path **inline in the artifact body** (body text, not only YAML)

**Write** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`

```yaml
skill: prove-hypothesis
topic: {topic}
date: {date}
scout_anchor: simulations/scout/scout-{type}/{topic}-scout-{type}-{date}.md
status_quo_comparator: "{value from CAMPAIGN OPEN}"
inertia_vulnerability: "{value from CAMPAIGN OPEN}"
stages_completed: [stage-1-hypothesis]
```

**Stage 1 Exit Gate**:
- [ ] Hypothesis names `{status_quo_comparator}` as the incumbent
- [ ] `inertia_vulnerability` named as the barrier to clear
- [ ] 3–5 displacement sub-claims listed
- [ ] Falsification condition stated
- [ ] Scout anchor path cited inline in body (separate from YAML)
- [ ] YAML includes `scout_anchor`, `status_quo_comparator`, `inertia_vulnerability`, `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) append `stage-1-hypothesis` to `stages_completed`; (2) emit `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`. Checklist completion is the sole trigger. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 1 → Stage 2

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 1 | Stage 1 write | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| (2) Gate clearance — GATE-1 CLEARED | GATE-1 clearance string | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| (3) Entry condition — Stage 2 confirms | Stage 2 entry | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |

All three rows must name the identical path.

---

## Stage 2 — prove-websearch

**Entry**: Stage 1 Exit Gate cleared. `GATE-1 CLEARED. → simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` confirmed. Path confirmed: `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`.

Search external sources. For each sub-claim, note supporting or weakening evidence vs displacing `{status_quo_comparator}`. At point of discovery, flag thin evidence:

```
THIN: [{sub-claim}] — weakens displacement of {status_quo_comparator} because [{reason}]
```

Every `THIN:` body must name `{status_quo_comparator}`. Do not defer.

**Write** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`

```yaml
skill: prove-websearch
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch]
```

**Stage 2 Exit Gate**:
- [ ] All Stage 1 sub-claims searched externally
- [ ] THIN flags written inline, each naming `{status_quo_comparator}`
- [ ] YAML includes both displacement fields and updated `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) append `stage-2-websearch` to `stages_completed`; (2) emit `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`. Sole trigger. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 2 → Stage 3

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 2 | Stage 2 write | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| (2) Gate clearance — GATE-2 CLEARED | GATE-2 clearance string | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| (3) Entry condition — Stage 3 confirms | Stage 3 entry | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |

---

## Stage 3 — prove-intelligence

**Entry**: Stage 2 Exit Gate cleared. `GATE-2 CLEARED. → simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` confirmed. Path confirmed: `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`.

Scan internal sources — artifacts, simulations, specs, codebase — for evidence on Stage 1 sub-claims. Same `THIN:` protocol; every flag body names `{status_quo_comparator}`.

**Write** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`

```yaml
skill: prove-intelligence
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]
```

**Stage 3 Exit Gate**:
- [ ] Internal sources scanned per Stage 1 sub-claim
- [ ] THIN flags written inline, each naming `{status_quo_comparator}`
- [ ] YAML includes both displacement fields and updated `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) append `stage-3-intelligence` to `stages_completed`; (2) emit `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`. Sole trigger. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 3 → Stage 4

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 3 | Stage 3 write | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| (2) Gate clearance — GATE-3 CLEARED | GATE-3 clearance string | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| (3) Entry condition — Stage 4 confirms | Stage 4 entry | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |

---

## Stage 4 — prove-analysis

**Entry**: Stage 3 Exit Gate cleared. `GATE-3 CLEARED. → simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` confirmed. Path confirmed: `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`.

**GATE 4A — Part A: Flag Aggregation** (complete before Part B):

Collect all THIN flags from Stages 2–3:

| # | THIN Flag | Source Stage | Displacement Claim Weakened vs `{status_quo_comparator}` |
|---|-----------|-------------|----------------------------------------------------------|
| 1 | … | … | … |

If no flags: write "No THIN findings." Emit `GATE-4A CLEARED.` when table is complete.

**Part B — Hypothesis Mapping**: For each row, name the Stage 1 sub-claim weakened, state the effect on the displacement argument against `{status_quo_comparator}`, and assign confidence impact (High/Medium/Low).

**Write** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`

```yaml
skill: prove-analysis
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]
```

**Stage 4 Exit Gate**:
- [ ] GATE-4A cleared (aggregation table complete or empty stated)
- [ ] All THIN flags mapped to Stage 1 sub-claims (Part B complete)
- [ ] Confidence impact stated per mapping vs `{status_quo_comparator}`
- [ ] YAML includes both displacement fields and updated `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) append `stage-4-analysis` to `stages_completed`; (2) emit `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`. Sole trigger. Single event, both outputs.**

### PATH CHAIN VERIFICATION: Stage 4 → Stage 5

| Row | Source | Path |
|-----|--------|------|
| (1) Write instruction — Stage 4 | Stage 4 write | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| (2) Gate clearance — GATE-4 CLEARED | GATE-4 clearance string | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| (3) Entry condition — Stage 5 confirms | Stage 5 entry | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |

---

## Stage 5 — prove-synthesize

**Entry**: Stage 4 Exit Gate cleared. `GATE-4 CLEARED. → simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` confirmed. Path confirmed: `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`.

Synthesize all evidence into a brief. Frame as **the case for displacing `{status_quo_comparator}`**. Confidence adjustment table — emit one named form:

**FORM A** (THIN flags exist — one row per flag):

| THIN Flag | Source Stage | Weakened Displacement Claim vs `{status_quo_comparator}` | Confidence Delta |
|-----------|-------------|----------------------------------------------------------|-----------------|
| … | … | … | −N% |

**FORM B** (no THIN flags — always emit; never omit):

| THIN Flag | Source Stage | Weakened Displacement Claim | Confidence Delta |
|-----------|-------------|----------------------------|-----------------|
| no THIN findings | — | — | 0 |

Label heading (`FORM A` or `FORM B`) must appear above the table. Close with: **The next step for this topic is `/topic-story`.**

**Write** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`

```yaml
skill: prove-synthesize
topic: {topic}
date: {date}
status_quo_comparator: "{same value}"
inertia_vulnerability: "{same value}"
stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis, stage-5-synthesize]
```

**Stage 5 Exit Gate**:
- [ ] Confidence adjustment table emitted (FORM A or FORM B, with label heading)
- [ ] Synthesis framed as displacement case against `{status_quo_comparator}`
- [ ] `/topic-story` explicitly named as the next step
- [ ] YAML includes both displacement fields and complete `stages_completed`
- [ ] **DUAL-OUTPUT EMISSION RULE — When all items above are checked: (1) append `stage-5-synthesize` to `stages_completed`; (2) emit `GATE-5 CLEARED. → simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`. Sole trigger. Single event, both outputs.**

---

Campaign complete. All 5 artifacts written. Displacement case assembled. Hand off to `/topic-story`.
