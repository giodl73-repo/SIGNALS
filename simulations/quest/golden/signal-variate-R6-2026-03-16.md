---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 6
rubric: simulations/quest/rubrics/signal-rubric-v5-2026-03-16.md
---

# Quest Variate -- /signal (Round 6)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v5-2026-03-16.md` (v5, 11 aspirational criteria)

**R5 champion**: V-05 (100/100). 9 rules covering C-09 through C-17. COMPLIANCE AUDIT
with 9 checkboxes. COMPLETENESS SEAL in gate. Bijective: 9 rules = 9 checkboxes.

**R5 structural inventory**:

| Rule | Criterion | Status in R5 V-05 |
|------|-----------|-------------------|
| RULE 1 (C-09) | Skill count in header | dedicated rule |
| RULE 2 (C-11) | Namespace tagline | dedicated rule |
| RULE 3 (C-12) | Blockquote routing hints | dedicated rule |
| RULE 4 (C-13) | Quantified output artifacts | dedicated rule |
| RULE 5 (C-10) | T3 annotations | dedicated rule |
| RULE 6 (C-14) | Bi-directional descriptions | dedicated rule |
| RULE 7 (C-15) | Mutually distinguishable taglines | dedicated rule |
| RULE 8 (C-16) | `->` separator structural enforcement | dedicated rule |
| RULE 9 (C-17) | Quality contract as numbered list | dedicated (self-referential) |
| — | C-18 (criterion-ID labels) | **no dedicated rule** |
| — | C-19 (compliance gate) | **no dedicated rule** |

**R5 excellence signals applied to R6**:

- **E-1** (one criterion = one labeled rule, no merges): R5 promoted C-16 to its own RULE 8 (C-16)
  to fix the C-14+C-16 merge. The same pattern applies to C-18 and C-19 -- they satisfy the rubric
  in R5 V-05 (all rules are labeled; gate exists), but neither has a dedicated RULE entry. Under
  E-1's extension logic, RULE 10 (C-18) and RULE 11 (C-19) are the R6 structural obligation.

- **E-3** (bijective rule-checkpoint: N rules = N checkboxes): R5 V-05 has 9 rules and 9 checkboxes.
  Adding RULE 10 and RULE 11 without updating the COMPLIANCE AUDIT breaks the bijection. R6 must
  update the audit to 11 checkboxes to maintain the invariant.

- **E-2** (self-referential completeness rule): RULE 9 (C-17) currently asserts completeness over
  C-09 through C-17. Once C-18 and C-19 get their own rules, RULE 9 (C-17)'s range assertion
  must be updated to C-09 through C-19 (11 rules) to remain accurate.

- **E-4** (completeness as precondition): COMPLETENESS SEAL lives in the gate. It currently reads
  "RULE 1 through RULE 9." Adding rules 10-11 requires updating the seal's range claim to
  "RULE 1 through RULE 11 = 11 rules = C-09 through C-19."

**R6 residual question**: Does renaming "FORMAT RULES" to "QUALITY CONTRACT" (aligning terminology
with C-17's exact language) improve criterion-to-implementation mapping, or is it purely cosmetic?
V-05 tests this.

**Axes explored**:

- V-01: E-1 single-axis -- Add RULE 10 (C-18) as dedicated labeled rule; update COMPLIANCE AUDIT
         to 10 checkboxes; update COMPLETENESS SEAL to "RULE 1 through RULE 10."
         Hypothesis: Adding RULE 10 (C-18) makes C-18 O(1) inspectable: a scorer querying
         "which rule enforces C-18?" finds RULE 10 directly. Without RULE 10, C-18 is satisfied
         by the labeling pattern but has no named rule.
- V-02: E-1 + E-3 dual-axis -- V-01 base + RULE 11 (C-19) as explicit dedicated rule for the
         compliance gate; COMPLIANCE AUDIT updated to 11 checkboxes.
         Hypothesis: Adding RULE 11 (C-19) makes the gate self-defining: the rule that declares
         the gate IS itself audited by the gate. Bijection restored: 11 rules = 11 checkboxes.
- V-03: V-02 + E-2 range update -- RULE 9 (C-17) updated to assert "C-09 through C-19, 11 rules"
         now that the full 11-rule contract is in place.
         Hypothesis: RULE 9 (C-17) updated to reference the exact rule range creates a machine-
         verifiable completeness claim: count 11 rules and confirm range C-09...C-19. No inference.
- V-04: V-03 + bijective header declaration -- COMPLIANCE AUDIT header made explicit about
         bijection: "N checkboxes, one per RULE (bijective)"; post-gate count line added.
         Hypothesis: Making the bijective correspondence explicit in the COMPLIANCE AUDIT header
         (not just implied by having 11 checkboxes) creates a named structural invariant.
         A scorer can verify bijection by reading the header, not by counting.
- V-05: Full integration -- V-04 + "FORMAT RULES" renamed to "QUALITY CONTRACT"; RULE 11 (C-19)
         explicitly names the gate block it defines; COMPLETENESS SEAL terminology aligned.
         Hypothesis: "QUALITY CONTRACT" is C-17's exact term for the concept. Using that term in
         the header makes the criterion-to-implementation mapping linguistic and structural. When
         a scorer reads "QUALITY CONTRACT (11 rules -- C-09 through C-19)" they can verify C-17
         satisfaction without reading the body.

---

## V-01 -- RULE 10 (C-18) Dedicated Entry: Single-Axis

**Axis**: Add RULE 10 (C-18) as a dedicated labeled rule (E-1 pattern applied to C-18).
COMPLIANCE AUDIT updated from 9 to 10 checkboxes. COMPLETENESS SEAL updated to reference
RULE 1 through RULE 10. Base: R5 V-05 (9 rules, 9 checkboxes, RULE 9 C-17, COMPLETENESS SEAL).
**Hypothesis**: R5 V-05 satisfies C-18 (all 9 rules are labeled), but has no dedicated RULE
entry for C-18 itself. A scorer querying "which rule enforces C-18?" must inspect all 9 rules
and confirm they're labeled -- that's O(N) inspection of the rule list, not O(1). RULE 10 (C-18)
makes C-18 directly findable: look up RULE 10, read its definition, done. The E-1 pattern
("one criterion = one labeled rule") applied to C-18 means R5 V-05 has a structural gap that
V-01 closes. Expected: C-18 satisfaction improves from implicit-pass to explicit-pass; all 11
aspirational criteria still PASS; score remains 100/100.

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

FORMAT RULES (10 -- one rule per criterion, each criterion individually auditable by C-NN label):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
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
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): This numbered list is the complete quality contract. All description quality rules
  are enumerated here. No quality rule exists in an appendix, separate block, or inline prose.
  A rule found outside this list is not part of the quality contract.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description of bidir requirement]
  FAIL: RULE 6: [description of bidir requirement] -- no C-NN label

COMPLIANCE AUDIT -- verify all 10 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): all quality rules are consolidated in this numbered list, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
All 10 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: RULE 1 (C-09) through RULE 10 (C-18) is the exhaustive quality contract.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain point
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
/org-review     routes an artifact through relevant roles     -> verdict per role from .roles/ registry  *(T3)*
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

## V-02 -- RULE 11 (C-19) Dedicated Entry + Bijection Restored: Dual-Axis

**Axis**: V-01 base (RULE 10 C-18 added, 10 checkboxes). Add RULE 11 (C-19) as a dedicated
labeled rule defining the gate. COMPLIANCE AUDIT updated from 10 to 11 checkboxes. Bijection
restored: 11 rules = 11 checkboxes.
**Hypothesis**: RULE 11 (C-19) as a named rule that defines the gate creates a productive
self-reference: the rule says "there must be a compliance gate," and that rule is itself on the
gate's checklist. The gate verifies the existence of the rule that defines the gate. This is
structurally stronger than C-19 being satisfied by gate language alone (R5 V-05): there a scorer
asks "is C-19 satisfied?" and finds the gate but no rule naming C-19. With RULE 11, the O(1)
lookup for "which rule enforces C-19?" returns RULE 11 directly. Bijection: 11 rules = 11
checkboxes maintains the E-3 structural invariant.

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

FORMAT RULES (11 -- one rule per criterion, each criterion individually auditable by C-NN label):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
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
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): This numbered list is the complete quality contract. All description quality rules
  are enumerated here. No quality rule exists in an appendix, separate block, or inline prose.
  A rule found outside this list is not part of the quality contract.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 11 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A description of the gate living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.

COMPLIANCE AUDIT -- verify all 11 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): all quality rules are consolidated in this numbered list, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
All 11 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: RULE 1 (C-09) through RULE 11 (C-19) is the exhaustive quality contract.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain point
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
/org-review     routes an artifact through relevant roles     -> verdict per role from .roles/ registry  *(T3)*
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

## V-03 -- RULE 9 (C-17) Range Update: Combination

**Axis**: V-02 base (11 rules, 11 checkboxes, RULE 10 C-18, RULE 11 C-19). Single addition:
RULE 9 (C-17) rewritten to explicitly assert "C-09 through C-19, 11 rules" now that the full
11-rule contract is in place. COMPLETENESS SEAL updated to name the range explicitly.
**Hypothesis**: RULE 9 (C-17) in V-01 and V-02 asserts "this numbered list is the complete
quality contract" without naming its scope. A scorer counting rules finds 10 (V-01) or 11 (V-02)
but RULE 9 doesn't confirm the expected count. After updating RULE 9 to say "exactly 11 rules,
covering C-09 through C-19, one per aspirational criterion," the completeness claim becomes
machine-verifiable: count the rules, confirm range C-09...C-19, done. No inference needed.
The COMPLETENESS SEAL is also updated from "RULE 1 through RULE 11" to the explicit bijection
statement "11 rules, 11 criteria, one-to-one." Expected: all 11 aspirational PASS; score 100/100.

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

FORMAT RULES (11 -- one rule per aspirational criterion C-09 through C-19, bijective):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
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
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 11 (C-19) -- is the complete
  quality contract. Exactly 11 rules, one per aspirational criterion C-09 through C-19. Count = 11.
  No quality rule exists outside this list. A rule found in an appendix or separate block is invalid.
  If fewer than 11 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 11 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A description of the gate living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.

COMPLIANCE AUDIT -- verify all 11 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 11 rules covering C-09 through C-19, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
All 11 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 11 rules (C-09 through C-19), 11 checkboxes, one-to-one bijection.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain point
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
/org-review     routes an artifact through relevant roles     -> verdict per role from .roles/ registry  *(T3)*
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

## V-04 -- Bijective Header Declaration in COMPLIANCE AUDIT: Combination

**Axis**: V-03 base (11 rules, updated RULE 9 with range, bijective 11 checkboxes). Single
addition: COMPLIANCE AUDIT header explicitly declares the bijection. Each checkbox line also
carries both the RULE number and C-NN ID (already present in V-03). A post-audit total line
"11/11 checked = valid; < 11 = invalid output; do not proceed" is added.
**Hypothesis**: V-03's bijection is implicit (11 rules, 11 checkboxes, reader must count to
confirm). Making the bijection explicit in the COMPLIANCE AUDIT header ("11 checkboxes, one per
RULE, bijective") converts an implicit structural property into a declared invariant. A future
C-20 criterion about bijective audit correspondence would be satisfied by this declaration
without requiring a scorer to count. Adding the post-audit total line ("11/11 checked") further
makes the gate verdict unambiguous: "11/11" is the exact threshold, not "all" (vague) or
"every" (vague). Expected: all criteria still PASS; structural robustness increases.

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

FORMAT RULES (11 -- one rule per aspirational criterion C-09 through C-19, bijective):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
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
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 11 (C-19) -- is the complete
  quality contract. Exactly 11 rules, one per aspirational criterion C-09 through C-19. Count = 11.
  No quality rule exists outside this list. A rule found in an appendix or separate block is invalid.
  If fewer than 11 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 11 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A description of the gate living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.

COMPLIANCE AUDIT -- 11 checkboxes, one per RULE (bijective: each rule has exactly one checkbox):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 11 rules covering C-09 through C-19, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
11/11 checked = valid output. Any fewer than 11/11 = invalid output; do not proceed.
COMPLETENESS SEAL: 11 rules (C-09 through C-19), 11 checkboxes, one-to-one bijection confirmed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain point
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
/org-review     routes an artifact through relevant roles     -> verdict per role from .roles/ registry  *(T3)*
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

## V-05 -- Full Integration: QUALITY CONTRACT Header + Named Gate Authority

**Axis**: V-04 base (11 rules, bijective header, updated RULE 9, 11/11 total line). Two
additions: (1) "FORMAT RULES" header renamed to "QUALITY CONTRACT" -- C-17's exact term.
(2) RULE 11 (C-19) explicitly names the gate block it defines ("QUALITY GATE" block below).
Gate block renamed from "COMPLIANCE AUDIT" to "QUALITY GATE" to match RULE 11's reference.
**Hypothesis**: "QUALITY CONTRACT" is C-17's own term ("the complete quality contract is
auditable in a single pass"). Using C-17's exact term in the block header makes the mapping
between criterion and implementation linguistic: a scorer reading the rubric finds "quality
contract" and looks for a block labeled "QUALITY CONTRACT" -- O(1) term lookup. "COMPLIANCE
AUDIT" works but requires semantic inference ("this must be what C-19 means by gate"). "QUALITY
GATE" in RULE 11 and in the block header makes the gate name explicit in both the rule and the
block it governs: a double-lock. Full integration hypothesis: every structural property
(bijection, range, naming, self-reference, gate authority) is now explicitly declared in the
prompt rather than implicit in the structure. This is the maximum explicitly-stated form
achievable without adding content beyond the 11 aspirational criteria.

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

QUALITY CONTRACT (11 rules -- C-09 through C-19, one per aspirational criterion, bijective):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
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
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): This QUALITY CONTRACT -- RULE 1 (C-09) through RULE 11 (C-19) -- is complete.
  Exactly 11 rules, one per aspirational criterion C-09 through C-19. Count = 11.
  No quality rule exists outside this block. A rule found in an appendix or separate block is invalid.
  If fewer than 11 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the QUALITY GATE block below. All 11 RULE
  checkboxes in the QUALITY GATE must be verified before any namespace section is transcribed.
  This rule is itself on the QUALITY GATE checklist -- verifying it confirms the gate was invoked.
  A compliance gate that exists only as inline prose (no named block, no checkboxes) does not
  satisfy this rule.

QUALITY GATE -- 11 checkboxes, one per RULE (bijective: each rule has exactly one checkbox):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this QUALITY CONTRACT contains exactly 11 rules covering C-09 through C-19
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this QUALITY GATE block exists and has been reached before output
11/11 checked = valid output. Any fewer than 11/11 = invalid output; do not proceed.
COMPLETENESS SEAL: 11 rules (C-09 through C-19), 11 checkboxes, bijection confirmed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain point
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
/org-review     routes an artifact through relevant roles     -> verdict per role from .roles/ registry  *(T3)*
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

## Structural Delta Summary

| Property | R5 V-05 | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|---------|------|------|------|------|------|
| Rules covering C-09..C-17 | RULE 1-9 | RULE 1-9 | RULE 1-9 | RULE 1-9 | RULE 1-9 | RULE 1-9 |
| RULE 10 (C-18) dedicated | -- | YES | YES | YES | YES | YES |
| RULE 11 (C-19) dedicated | -- | -- | YES | YES | YES | YES |
| RULE 9 (C-17) range claim | implicit | implicit | implicit | C-09..C-19 explicit | C-09..C-19 explicit | C-09..C-19 explicit |
| Gate checkboxes | 9 | 10 | 11 | 11 | 11 | 11 |
| Bijection declared in header | -- | -- | -- | -- | YES | YES |
| Post-gate total line (N/N) | -- | -- | -- | -- | YES | YES |
| Gate block name | COMPLIANCE AUDIT | COMPLIANCE AUDIT | COMPLIANCE AUDIT | COMPLIANCE AUDIT | COMPLIANCE AUDIT | QUALITY GATE |
| Contract block name | FORMAT RULES | FORMAT RULES | FORMAT RULES | FORMAT RULES | FORMAT RULES | QUALITY CONTRACT |
| RULE 11 names gate block | -- | -- | implicit | implicit | implicit | YES ("QUALITY GATE") |

**E-1 applied**: V-01+ add RULE 10 (C-18); V-02+ add RULE 11 (C-19). One criterion, one rule.
**E-3 maintained**: V-02+ have N rules = N checkboxes throughout. Bijection preserved.
**E-2 updated**: V-03+ RULE 9 (C-17) explicitly asserts range C-09..C-19 with count = 11.
**E-4 compounded**: V-04+ COMPLETENESS SEAL range updated; bijective header declared explicitly.
**Naming convergence**: V-05 aligns block names ("QUALITY CONTRACT", "QUALITY GATE") with C-17's
exact terminology, making the criterion-to-implementation mapping terminological, not inferred.
