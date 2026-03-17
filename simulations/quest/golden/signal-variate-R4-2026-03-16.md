---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 4
rubric: simulations/quest/rubrics/signal-rubric-v4-2026-03-16.md
---

# Quest Variate -- /signal (Round 4)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v4-2026-03-16.md`
**Rubric changes from v3**: Added C-16 (-> separator structurally enforced in every description),
C-17 (all description quality rules consolidated into explicit numbered list in skill output);
aspirational denominator updated from 7 to 9.

**Context**: R3 champion was V-04/V-05 (100 pts on v3). All R3 aspirational criteria (C-09 through
C-15) are carried forward as the established base. The two new criteria emerged from R3 excellence
signals:

- C-16 from R3 V-02 vs V-03 delta: V-02 descriptions were "deliverable-only" because RULE 6 allowed
  conceptual bidir without enforcing the `->` marker. V-03 passed because the `->` separator was
  syntactically required -- the pre-print template made it structurally impossible to omit. C-16 is
  not just "bidir present" (C-14) but "`->` syntactically enforced, absence is a validity failure."
- C-17 from R3 V-04 evidence: R3 V-04's 7 individually numbered RULE N labels made the complete
  quality contract auditable in a single pass. R3 V-05's 5 merged rules required inference to
  determine which criteria were covered. C-17 requires every quality rule to be individually numbered
  and enumerable, not merged into compound rules.

**Axes explored**:
- V-01: C-16 single-axis -- SEPARATOR CONTRACT block declaring -> a structural requirement, not a
         style preference (R3 V-04 hybrid base + explicit validity-failure declaration)
- V-02: C-17 single-axis -- 5 merged FORMAT RULES from R3 V-05 expanded to 7 individually numbered
         rules, one per criterion (pre-print base, no other changes)
- V-03: C-16 + criterion-ID annotations -- R3 V-04 base + "(C-NN)" labels on each RULE +
         SEPARATOR CONTRACT block (confirms no interaction between ID labels and enforcement)
- V-04: Pre-print + 7 individually numbered rules -- R3 V-05 structural pre-print base + 7 rules
         with criterion IDs replacing the 5 merged rules (full C-16 + C-17 in pre-print mode)
- V-05: Pre-print + 7 rules + criterion IDs + COMPLIANCE AUDIT -- V-04 plus an explicit
         COMPLIANCE AUDIT pre-check block that lists all rules as a contract before the namespace
         sections; maximum auditability and enforcement

**Canonical sub-skill counts** (per rubric C-02):

| Namespace | Count |
|-----------|-------|
| scout     | 8     |
| draft     | 4     |
| review    | 4     |
| flow      | 7     |
| trace     | 7     |
| prove     | 9     |
| listen    | 3     |
| program   | 2     |
| topic     | 6     |
| quest     | 4     |
| mock      | 3     |
| org       | 4     |
| **Total** | **61** |

---

## Spread-Design Phase

**PARTIAL AMPLIFIER TRAJECTORY TABLE** (accumulated through Round 4):

| Round | Axis | Occurrence | Recommended Action |
|-------|------|------------|-------------------|
| R1 | Format: namespace headers lack skill count | First | Add count to header (-> C-09) -- resolved |
| R1 | Format: routing hints as inline prose, not blockquote | First | Enforce > blockquote routing hints (-> C-12) -- resolved |
| R1 | Depth: descriptions generic, no quantified outputs | First | Add quantified artifact references (-> C-13) -- resolved |
| R2 | Depth: T3-only skills not annotated | First | Add *(T3)* tier annotations (-> C-10) -- resolved |
| R2 | Format: namespace headers lack purpose taglines | First | Add verb-first taglines per namespace (-> C-11) -- resolved |
| R3 | Depth: descriptions deliverable-only, no mechanism verb | First | Add BIDIR RULE: mechanism + deliverable (-> C-14) -- resolved |
| R3 | Format: taglines generic, interchangeable across namespaces | First | Add SWAP TEST for tagline uniqueness (-> C-15) -- resolved |
| R4 | Format: -> present in descriptions but not declared as validity requirement | First | Add SEPARATOR CONTRACT block (-> C-16) |
| R4 | Depth: merged rules require inference to determine per-criterion compliance | First | Split to 7 individually numbered rules with criterion IDs (-> C-17) |

**Axis assignment plan**:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | C-16 only: SEPARATOR CONTRACT block, hybrid base | R3 V-02/V-03 delta -- -> absent vs present | C-16 PASS | ~94 |
| V-02 | C-17 only: 7 individual rules replacing 5 merged, pre-print base | R3 V-04 evidence -- enumerable rules | C-17 PASS | ~94 |
| V-03 | C-16 + criterion-ID labels on rules | V-01 + per-rule C-NN labels | C-16 PASS, C-17 PASS | ~100 |
| V-04 | Pre-print base + 7 rules with IDs | R3 V-05 structural + R3 V-04 rule set | C-16 + C-17 PASS | ~100 |
| V-05 | Pre-print + 7 rules with IDs + COMPLIANCE AUDIT block | Maximum enforcement + auditability | C-16 + C-17 maximally explicit | ~100 |

Predicted spread: V-01 and V-02 should diverge on exactly one of C-16 or C-17.
V-03 through V-05 should converge at 100, confirming that both criteria are satisfiable together.

---

## V-01 -- C-16 Single-Axis: SEPARATOR CONTRACT Block

**Axis**: C-16 enforcement -- declare `->` a structural requirement with explicit validity-failure
condition, not just a formatting preference.
**Hypothesis**: R3 V-04 has RULE 6 requiring bidir with `->`, but RULE 6 describes the format
without declaring absence a validity failure. Adding a SEPARATOR CONTRACT block that explicitly
states "descriptions without `->` are invalid output" makes C-16 structurally enforced at the
instruction level. The contract statement is distinct from the rule: rules guide behavior, contracts
declare failure conditions. If C-16 requires structural enforcement, a contract declaration satisfies
it even without structural pre-print.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

What are you trying to do?
  Research before committing            ->  /scout   (8 skills)
  Author a design artifact              ->  /draft   (4 skills)
  Validate design or code               ->  /review  (4 skills)
  Simulate a domain process             ->  /flow    (7 skills)
  Hand-compile platform behavior        ->  /trace   (7 skills)
  Gather and prove evidence             ->  /prove   (9 skills)
  Hear customer signals before ship     ->  /listen  (3 skills)
  Orchestrate multi-topic work          ->  /program (2 skills)
  Manage topic narrative and coverage   ->  /topic   (6 skills)
  Improve skill prompts                 ->  /quest   (4 skills)
  Generate synthetic coverage           ->  /mock    (3 skills)
  Simulate org structure and review     ->  /org     (4 skills)

Describe what you need and the most relevant skill will run automatically.

INVOCATION MODES:
  /signal                  full index (routing guide + all 12 namespace sections)
  /signal <namespace>      one namespace only (no routing guide; that section only)
  /signal --bare           flat list of all 61 command names, one per line, no other text

SEVEN FORMAT RULES -- every rule must be satisfied in every output:

RULE 1 (C-09 COUNT): Every namespace header must embed the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>

RULE 2 (C-11 TAGLINE): Every namespace header must end with a purpose tagline starting with a verb.
  The tagline must answer "what is this namespace for?" distinctly from all other namespaces.
  PASS: ### Scout -- 8 skills -- map the competitive landscape before you commit to a direction
  FAIL: ### Scout -- 8 skills (no tagline)

RULE 3 (C-12 BLOCKQUOTE): Every namespace section must end with a Markdown blockquote routing hint.
  The > must be at line start. Inline prose routing hints are not acceptable.
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.

RULE 4 (C-13 QUANTIFIED): Every sub-skill description must name a specific output artifact --
  a count, named format, or rated deliverable. Vague single-word nouns alone are not sufficient.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"

RULE 5 (C-10 T3): Skills whose full runbook loads on demand carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

RULE 6 (C-14 BIDIR): Every description must be BI-DIRECTIONAL -- naming BOTH the mechanism
  (what the skill does -- a verb phrase) AND the deliverable (what you receive -- a noun with
  count, format, or rating). Neither alone is sufficient.
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no deliverable)
  FAIL: "5-8 rivals with ratings" (no mechanism verb)

RULE 7 (C-15 SWAP TEST): Every namespace tagline must be NAMESPACE-LOCKED.
  Test: could this tagline appear under any other namespace header and still make sense?
  If yes, reject it and write a more specific tagline.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (could be scout, prove, or listen)

SEPARATOR CONTRACT:
The `->` separator in every sub-skill description is a STRUCTURAL REQUIREMENT, not a
formatting preference. A description that does not contain `->` is INVALID OUTPUT regardless
of how specific or descriptive its content is. Before finalizing any description line, verify:
  1. The line contains `->` as a separator.
  2. The text before `->` is a verb phrase (mechanism).
  3. The text after `->` is a quantified noun (deliverable).
If any of these three conditions fails, the description is invalid and must be rewritten.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.

---

### Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

/scout-competitors   scans competitive landscape with inertia-first framing -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one -> shortlist with trademark clearance, domain availability, and per-persona score per name
/scout-compliance    surveys regulatory obligations for a domain -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- commit design intent to a written artifact that others can review and challenge

/draft-spec        structures design intent into sections -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options against criteria -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story for each audience -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates idea candidates and scores them comparatively -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- challenge design and code through structured expert and user critique

/review-design     runs design through 6 expert disciplines -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level across disciplines -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 persona advocates walking the design -> usability score per persona with cross-persona synthesis
/review-customers  simulates 12 customer personas evaluating the feature -> would-adopt rating, NPS prediction, and top concern per persona

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate how a domain process plays out before building the implementation

/flow-lifecycle    traces a document lifecycle phase by phase -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates a multi-turn conversation through a topic graph -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires a trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces an ETL or sync pipeline stage by stage -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- step through implementation mechanics one boundary at a time before assumptions harden

/trace-request     compiles request path hop by hop -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows a user action through the UI component tree -> re-render count and state update path per component traversal
/trace-deployment  steps through a deployment sequence -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies a schema change to sample data -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case before claiming certainty

/prove-hypothesis  frames a falsifiable claim -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for supporting and opposing evidence -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal codebase and docs for evidence -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable implementation -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for causal patterns -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all gathered evidence against the hypothesis -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation as a research paper -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype -> adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-02 -- C-17 Single-Axis: 7 Individually Numbered Rules Replacing 5 Merged

**Axis**: C-17 enumeration -- expand R3 V-05's 5 merged FORMAT RULES to 7 individually numbered
rules, one per criterion, making the complete quality contract auditable without inference.
**Hypothesis**: R3 V-05's FORMAT RULES merged C-13+C-14 into RULE 4 and C-11+C-15 into RULE 2.
This required a reader to infer that two criteria were covered by one rule. C-17 requires all
description quality rules to be individually enumerable -- no merges. Splitting RULE 2 and RULE 4
into separate numbered rules (7 total) satisfies C-17 without changing the structural pre-print
content (which already satisfies C-16 via transcribe-exactly). Single axis: C-17 only.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

What are you trying to do?
  Research before committing            ->  /scout   (8 skills)
  Author a design artifact              ->  /draft   (4 skills)
  Validate design or code               ->  /review  (4 skills)
  Simulate a domain process             ->  /flow    (7 skills)
  Hand-compile platform behavior        ->  /trace   (7 skills)
  Gather and prove evidence             ->  /prove   (9 skills)
  Hear customer signals before ship     ->  /listen  (3 skills)
  Orchestrate multi-topic work          ->  /program (2 skills)
  Manage topic narrative and coverage   ->  /topic   (6 skills)
  Improve skill prompts                 ->  /quest   (4 skills)
  Generate synthetic coverage           ->  /mock    (3 skills)
  Simulate org structure and review     ->  /org     (4 skills)

Describe what you need and the most relevant skill will run automatically.

INVOCATION MODES:
  /signal                  full index (routing guide + all 12 namespace sections)
  /signal <namespace>      one namespace only (no routing guide; that section only)
  /signal --bare           flat list of all 61 command names, one per line, no other text

FORMAT RULES (7 -- one per quality criterion):
RULE 1: Header format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2: Tagline must start with a verb. Tagline must answer "what is this namespace for?"
  PASS: ### Scout -- 8 skills -- map the competitive landscape before you commit to a direction
  FAIL: ### Scout -- 8 skills (no tagline)
RULE 3: Section ends with Markdown blockquote (> at line start).
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.
RULE 4: Description must name a specific quantified output artifact -- a count, named format,
  or rated deliverable. Vague single-word nouns alone are not sufficient.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"
RULE 5: T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6: Description must be bi-directional: left of `->` is a mechanism verb phrase (what
  the skill does); right of `->` is a quantified deliverable (what you receive). Neither alone
  is sufficient. The `->` separator is REQUIRED in every description.
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no deliverable, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb)
RULE 7: Every namespace tagline must pass the SWAP TEST: could this tagline appear under any
  other namespace header and still make sense? If yes, it is too generic. Rewrite until locked.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen equally)

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design begins

/scout-competitors   scans competitive landscape with inertia-first framing    -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one           -> shortlist with trademark clearance, domain availability, and per-persona score
/scout-compliance    surveys regulatory obligations for a domain                -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment                    -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence        -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience                -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements               -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

## Draft -- 4 skills -- commit design thinking to a written artifact ready for review

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

## Review -- 4 skills -- challenge an artifact through expert discipline and user perspective critique

/review-design     runs design through 6 expert lenses        -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level                -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain
/review-customers  simulates 12 customer personas              -> would-adopt rating, NPS prediction, and top concern per customer persona

> Describe your review artifact and the most relevant review skill will run.

---

## Flow -- 7 skills -- simulate domain process behavior before writing the implementation

/flow-lifecycle    traces document lifecycle phase by phase                          -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates multi-turn agent conversation through a topic graph     -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces ETL or sync pipeline stage by stage                        -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs             -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput                          -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model                -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

## Trace -- 7 skills -- step through platform mechanics one boundary at a time before assumptions harden

/trace-request     compiles request path hop by hop                                    -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition                      -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern     -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows user action through the UI component tree                   -> re-render count and state update path per component traversal
/trace-deployment  steps through deployment sequence                                   -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies schema change to sample data                                -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set                     -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

## Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case before claiming certainty

/prove-hypothesis  frames a falsifiable claim                                     -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for supporting and opposing evidence           -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal codebase and docs for evidence              -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable implementation                    -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for causal patterns                        -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews                     -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all gathered evidence against the hypothesis            -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation as a research paper                 -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign                          -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

## Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping          -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype           -> adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

## Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates     -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research            -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

## Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals         -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage                   -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot         -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives     -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story   -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals     -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

## Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill           -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison       -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric        -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop      -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

## Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace   -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace         -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

## Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape     -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure        -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles     -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation           -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-03 -- C-16 + Criterion-ID Annotations: Separator Contract + Labeled Rules

**Axis**: C-16 + C-17 combined via instructional (non-pre-print) approach -- SEPARATOR CONTRACT
block declares `->` a validity requirement; each RULE is labeled with its criterion ID (C-NN)
making the complete contract auditable by criterion-ID lookup.
**Hypothesis**: V-01 adds a SEPARATOR CONTRACT block but the rules carry no criterion-ID labels.
V-03 adds "(C-NN)" to each RULE label AND the SEPARATOR CONTRACT block. If C-17 requires each
rule to be individually labeled with its criterion (not just individually numbered), then criterion-
ID labels satisfy the "auditable in a single pass" requirement more directly: a scorer can verify
C-14 compliance by finding "RULE N (C-14)" in the rule list without inference. This tests whether
the ID label adds value beyond V-01 for C-17.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

What are you trying to do?
  Research before committing            ->  /scout   (8 skills)
  Author a design artifact              ->  /draft   (4 skills)
  Validate design or code               ->  /review  (4 skills)
  Simulate a domain process             ->  /flow    (7 skills)
  Hand-compile platform behavior        ->  /trace   (7 skills)
  Gather and prove evidence             ->  /prove   (9 skills)
  Hear customer signals before ship     ->  /listen  (3 skills)
  Orchestrate multi-topic work          ->  /program (2 skills)
  Manage topic narrative and coverage   ->  /topic   (6 skills)
  Improve skill prompts                 ->  /quest   (4 skills)
  Generate synthetic coverage           ->  /mock    (3 skills)
  Simulate org structure and review     ->  /org     (4 skills)

Describe what you need and the most relevant skill will run automatically.

INVOCATION MODES:
  /signal                  full index (routing guide + all 12 namespace sections)
  /signal <namespace>      one namespace only (no routing guide; that section only)
  /signal --bare           flat list of all 61 command names, one per line, no other text

SEVEN FORMAT RULES -- complete quality contract; one rule per criterion:

RULE 1 (C-09): Every namespace header embeds the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>

RULE 2 (C-11): Every namespace header ends with a purpose tagline that begins with a verb.
  PASS: ### Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ### Scout -- 8 skills (no tagline present)

RULE 3 (C-12): Every namespace section ends with a Markdown blockquote routing hint.
  The > must be at line start. Inline prose is not acceptable.
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Describe your need and a skill will run.

RULE 4 (C-13): Every sub-skill description names a specific quantified output -- a count,
  named format, or rated deliverable. Vague single-word nouns do not satisfy this rule.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"

RULE 5 (C-10): Skills whose full runbook loads on demand carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

RULE 6 (C-14): Every description is bi-directional: left of `->` names the mechanism (a verb
  phrase -- what the skill does); right of `->` names the quantified deliverable (what you receive).
  Neither side alone satisfies this rule.
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (deliverable-only, no mechanism verb)
  FAIL: "5-8 rivals with ratings" (deliverable-only, no mechanism verb)

RULE 7 (C-15): Every namespace tagline passes the SWAP TEST: if this tagline appeared under
  a different namespace header, it would be wrong. If it could appear anywhere, rewrite it.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (too broad -- applies to scout, prove, listen)

SEPARATOR CONTRACT (C-16 enforcement):
The `->` separator is a STRUCTURAL REQUIREMENT in every sub-skill description line.
Absence of `->` constitutes invalid output regardless of description quality or specificity.
Before writing each description, verify three conditions:
  1. The `->` separator is present.
  2. The text before `->` is a verb phrase (mechanism: what the skill does).
  3. The text after `->` is a quantified noun (deliverable: what you receive).
Failure on any of these three conditions makes the description invalid. Rewrite it.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.

---

### Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

/scout-competitors   scans competitive landscape with inertia-first framing -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one -> shortlist with trademark clearance, domain availability, and per-persona score per name
/scout-compliance    surveys regulatory obligations for a domain -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- commit design intent to a written artifact that others can review and challenge

/draft-spec        structures design intent into sections -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options against criteria -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story for each audience -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates idea candidates and scores them comparatively -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- challenge design and code through structured expert and user critique

/review-design     runs design through 6 expert disciplines -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level across disciplines -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 persona advocates walking the design -> usability score per persona with cross-persona synthesis
/review-customers  simulates 12 customer personas evaluating the feature -> would-adopt rating, NPS prediction, and top concern per persona

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate how a domain process plays out before building the implementation

/flow-lifecycle    traces a document lifecycle phase by phase -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates a multi-turn conversation through a topic graph -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires a trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces an ETL or sync pipeline stage by stage -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- step through implementation mechanics one boundary at a time

/trace-request     compiles request path hop by hop -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through its transitions -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual outputs using three-directory pattern -> mismatch severity (CRITICAL/MAJOR/MINOR) per delta  *(T3)*
/trace-component   follows a user action through the UI component tree -> re-render count and state update path per component
/trace-deployment  steps through a deployment sequence -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies a schema change to sample data -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case to test it

/prove-hypothesis  frames a falsifiable claim -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for evidence -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal sources for evidence -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable artifact -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for patterns -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all evidence for an answer -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign -> hypothesis card through synthesis in one automated command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype -> adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-04 -- Pre-Print Base + 7 Individually Numbered Rules with Criterion IDs

**Axis**: C-16 + C-17 full combination in structural pre-print mode -- R3 V-05's "transcribe
exactly" enforcement of `->` (C-16) combined with 7 individually numbered rules each labeled
with its criterion ID (C-17).
**Hypothesis**: R3 V-05 had 5 merged FORMAT RULES without criterion-ID labels; it likely scored
PARTIAL on C-17. Replacing those 5 merged rules with 7 individually numbered rules (one per
criterion, each with a C-NN label) while keeping the structural pre-print satisfies both C-16
(structural enforcement via "transcribe exactly" + pre-printed `->`) and C-17 (7 individually
numbered, individually labeled rules). This is the cleanest combination of R3 V-04 (rule rigor)
and R3 V-05 (structural enforcement) -- no new mechanism needed.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

What are you trying to do?
  Research before committing            ->  /scout   (8 skills)
  Author a design artifact              ->  /draft   (4 skills)
  Validate design or code               ->  /review  (4 skills)
  Simulate a domain process             ->  /flow    (7 skills)
  Hand-compile platform behavior        ->  /trace   (7 skills)
  Gather and prove evidence             ->  /prove   (9 skills)
  Hear customer signals before ship     ->  /listen  (3 skills)
  Orchestrate multi-topic work          ->  /program (2 skills)
  Manage topic narrative and coverage   ->  /topic   (6 skills)
  Improve skill prompts                 ->  /quest   (4 skills)
  Generate synthetic coverage           ->  /mock    (3 skills)
  Simulate org structure and review     ->  /org     (4 skills)

Describe what you need and the most relevant skill will run automatically.

INVOCATION MODES:
  /signal                  full index (routing guide + all 12 namespace sections)
  /signal <namespace>      one namespace only (no routing guide; that section only)
  /signal --bare           flat list of all 61 command names, one per line, no other text

FORMAT RULES (7 -- one rule per criterion, each criterion individually auditable):
RULE 1 (C-09): Header format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ### Scout -- 8 skills -- map the competitive landscape before you commit to a direction
  FAIL: ### Scout -- 8 skills (no tagline)
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.
RULE 4 (C-13): Description names a specific quantified output artifact (count, named format,
  or rated deliverable). Vague single-word nouns do not satisfy this rule.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional. Left of `->`: mechanism verb phrase (what skill
  does). Right of `->`: quantified deliverable (what you receive). The `->` separator is required.
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen)

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design begins

/scout-competitors   scans competitive landscape with inertia-first framing    -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one           -> shortlist with trademark clearance, domain availability, and per-persona score
/scout-compliance    surveys regulatory obligations for a domain                -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment                    -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence        -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience                -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements               -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

## Draft -- 4 skills -- commit design thinking to a written artifact ready for review

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

## Review -- 4 skills -- challenge an artifact through expert discipline and user perspective critique

/review-design     runs design through 6 expert lenses        -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level                -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain
/review-customers  simulates 12 customer personas              -> would-adopt rating, NPS prediction, and top concern per customer persona

> Describe your review artifact and the most relevant review skill will run.

---

## Flow -- 7 skills -- simulate domain process behavior before writing the implementation

/flow-lifecycle    traces document lifecycle phase by phase                          -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates multi-turn agent conversation through a topic graph     -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces ETL or sync pipeline stage by stage                        -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs             -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput                          -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model                -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

## Trace -- 7 skills -- step through platform mechanics one boundary at a time before assumptions harden

/trace-request     compiles request path hop by hop                                    -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition                      -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern     -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows user action through the UI component tree                   -> re-render count and state update path per component traversal
/trace-deployment  steps through deployment sequence                                   -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies schema change to sample data                                -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set                     -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

## Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case before claiming certainty

/prove-hypothesis  frames a falsifiable claim                                     -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for supporting and opposing evidence           -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal codebase and docs for evidence              -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable implementation                    -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for causal patterns                        -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews                     -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all gathered evidence against the hypothesis            -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation as a research paper                 -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign                          -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

## Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping          -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype           -> adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

## Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates     -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research            -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

## Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals         -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage                   -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot         -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives     -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story   -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals     -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

## Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill           -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison       -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric        -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop      -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

## Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace   -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace         -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

## Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape     -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure        -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles     -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation           -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-05 -- Pre-Print + 7 Rules with IDs + COMPLIANCE AUDIT Block

**Axis**: Maximum C-16 + C-17 enforcement -- V-04 base plus a COMPLIANCE AUDIT block that
explicitly states the complete 7-rule contract as a numbered checklist before the namespace
sections begin, making the quality contract a standalone auditable section distinct from the
rules/instructions.
**Hypothesis**: V-04 has 7 individually labeled rules in an instruction block that precedes the
namespace sections -- a reader scanning the prompt encounters rules, then sees the pre-print.
V-05 adds a second artifact: a COMPLIANCE AUDIT block positioned after the rules and before the
pre-print, which re-states all 7 rules as a checklist. This creates two separately auditable
representations of the quality contract (the rules and the audit block), and makes the contract
explicitly nameable: it has a heading (COMPLIANCE AUDIT), a clear scope (7 criteria), and a
pass/fail framing. If C-17 benefits from the quality contract being a discrete, named section
rather than an instruction block, V-05 satisfies that stronger form.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

What are you trying to do?
  Research before committing            ->  /scout   (8 skills)
  Author a design artifact              ->  /draft   (4 skills)
  Validate design or code               ->  /review  (4 skills)
  Simulate a domain process             ->  /flow    (7 skills)
  Hand-compile platform behavior        ->  /trace   (7 skills)
  Gather and prove evidence             ->  /prove   (9 skills)
  Hear customer signals before ship     ->  /listen  (3 skills)
  Orchestrate multi-topic work          ->  /program (2 skills)
  Manage topic narrative and coverage   ->  /topic   (6 skills)
  Improve skill prompts                 ->  /quest   (4 skills)
  Generate synthetic coverage           ->  /mock    (3 skills)
  Simulate org structure and review     ->  /org     (4 skills)

Describe what you need and the most relevant skill will run automatically.

INVOCATION MODES:
  /signal                  full index (routing guide + all 12 namespace sections)
  /signal <namespace>      one namespace only (no routing guide; that section only)
  /signal --bare           flat list of all 61 command names, one per line, no other text

FORMAT RULES (7 -- one rule per criterion, each criterion individually auditable):
RULE 1 (C-09): Header format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
RULE 4 (C-13): Description names a specific quantified output artifact.
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional: left of `->` = mechanism verb; right = quantified
  deliverable. Both sides required. `->` separator is required.
RULE 7 (C-15): Tagline passes SWAP TEST -- locked to this namespace; cannot belong to any other.

COMPLIANCE AUDIT -- verify all 7 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has count embedded
  [ ] RULE 2 (C-11): every tagline starts with a verb
  [ ] RULE 3 (C-12): every section ends with > blockquote
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)*
  [ ] RULE 6 (C-14): every description has mechanism -> deliverable with `->` separator present
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
All 7 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design begins

/scout-competitors   scans competitive landscape with inertia-first framing    -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one           -> shortlist with trademark clearance, domain availability, and per-persona score
/scout-compliance    surveys regulatory obligations for a domain                -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment                    -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence        -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience                -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements               -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

## Draft -- 4 skills -- commit design thinking to a written artifact ready for review

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

## Review -- 4 skills -- challenge an artifact through expert discipline and user perspective critique

/review-design     runs design through 6 expert lenses        -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level                -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain
/review-customers  simulates 12 customer personas              -> would-adopt rating, NPS prediction, and top concern per customer persona

> Describe your review artifact and the most relevant review skill will run.

---

## Flow -- 7 skills -- simulate domain process behavior before writing the implementation

/flow-lifecycle    traces document lifecycle phase by phase                          -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates multi-turn agent conversation through a topic graph     -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces ETL or sync pipeline stage by stage                        -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs             -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput                          -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model                -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

## Trace -- 7 skills -- step through platform mechanics one boundary at a time before assumptions harden

/trace-request     compiles request path hop by hop                                    -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition                      -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern     -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows user action through the UI component tree                   -> re-render count and state update path per component traversal
/trace-deployment  steps through deployment sequence                                   -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies schema change to sample data                                -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set                     -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

## Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case before claiming certainty

/prove-hypothesis  frames a falsifiable claim                                     -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for supporting and opposing evidence           -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal codebase and docs for evidence              -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable implementation                    -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for causal patterns                        -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews                     -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all gathered evidence against the hypothesis            -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation as a research paper                 -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign                          -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

## Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping          -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype           -> adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

## Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates     -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research            -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

## Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals         -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage                   -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot         -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives     -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story   -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals     -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

## Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill           -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison       -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric        -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop      -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

## Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace   -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace         -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

## Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape     -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure        -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles     -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation           -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## Predicted Score Matrix

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| C-01 All 12 namespaces | E | PASS | PASS | PASS | PASS | PASS |
| C-02 Sub-skill counts match | E | PASS | PASS | PASS | PASS | PASS |
| C-03 Every sub-skill has description | E | PASS | PASS | PASS | PASS | PASS |
| C-04 Filtered mode works | E | PASS | PASS | PASS | PASS | PASS |
| C-05 Bare mode works | E | PASS | PASS | PASS | PASS | PASS |
| C-06 Descriptions specific + differentiating | R | PASS | PASS | PASS | PASS | PASS |
| C-07 Visual hierarchy | R | PASS | PASS | PASS | PASS | PASS |
| C-08 Routing hint per namespace | R | PASS | PASS | PASS | PASS | PASS |
| C-09 Count in header line | A | PASS | PASS | PASS | PASS | PASS |
| C-10 T3 annotations | A | PASS | PASS | PASS | PASS | PASS |
| C-11 Namespace tagline | A | PASS | PASS | PASS | PASS | PASS |
| C-12 Blockquote routing hints | A | PASS | PASS | PASS | PASS | PASS |
| C-13 Quantified output artifacts | A | PASS | PASS | PASS | PASS | PASS |
| C-14 Bi-directional descriptions | A | PASS | PASS | PASS | PASS | PASS |
| C-15 Mutually distinguishable taglines | A | PASS | PASS | PASS | PASS | PASS |
| C-16 -> separator structurally enforced | A | PASS | PASS | PASS | PASS | PASS |
| C-17 Explicit numbered RULE list | A | PARTIAL | PASS | PASS | PASS | PASS |
| COMPOSITE (predicted) | | ~99 | ~100 | ~100 | ~100 | ~100 |
| RANK (predicted) | | 5 | 1-tie | 1-tie | 1-tie | 1-tie |

**V-01 C-17 analysis**: V-01 carries 7 individually numbered rules from R3 V-04 in the SEVEN FORMAT
RULES block -- but the SEPARATOR CONTRACT block adds enforcement language that is NOT numbered as
RULE 8. This may create an unnumbered rule outside the main list, raising the question of whether
the contract is "complete" in a single numbered block. PARTIAL predicted on C-17 if the scorer
requires all quality rules to be in the numbered list; PASS if the contract + rules together satisfy
the criterion.

**V-02 C-16 analysis**: V-02 uses structural pre-print with RULE 6 explicitly requiring `->` and
the pre-printed descriptions all containing `->`. The "transcribe exactly" instruction makes it
structurally impossible to omit. PASS predicted on C-16.

**V-03 through V-05**: Both C-16 and C-17 are satisfied: 7 individually numbered rules (C-17), all
descriptions use `->` with enforcement (C-16). V-05's COMPLIANCE AUDIT block is additive, not
replacing.

**Key spread**: V-01 vs V-02-V-05 on C-17 -- if SEPARATOR CONTRACT counts as an unnumbered rule,
V-01 PARTIAL; if 7 numbered rules are sufficient regardless of additional prose blocks, V-01 PASS.

---

## Notes for Quest-Score

When scoring:
1. C-16 PASS condition: Is `->` syntactically enforced in every description? Check that the skill
   body makes absence a validity failure (SEPARATOR CONTRACT, pre-print + transcribe-exactly, or
   equivalent mechanism). Rule-only enforcement without explicit failure declaration = PARTIAL.

2. C-17 PASS condition: Are ALL description quality rules consolidated into an explicitly numbered
   list where each rule has its own number and each criterion is covered by exactly one rule (no
   merges, no criteria discoverable only by inference)? Merged rules (e.g., C-13+C-14 in one RULE)
   = PARTIAL. Individual numbered rules covering all criteria = PASS.

3. V-01 C-17 edge case: The SEPARATOR CONTRACT block is a quality rule (C-16 enforcement) that is
   not in the numbered RULE list. Score as PARTIAL if C-17 requires ALL quality rules to be numbered
   in the single list. Score as PASS if the numbered list + enforcement contract together satisfy
   the "auditable in a single pass" requirement.
