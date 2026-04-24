---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 8
rubric: simulations/quest/rubrics/signal-rubric-v7-2026-03-16.md
---

# Quest Variate -- /signal (Round 8)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v7-2026-03-16.md` (v7, 15 aspirational criteria C-09 through C-23)

**R7 champion**: V-05 (14 rules covering C-09 through C-22; RULES 12-14 carry inline evidence;
bijective invariant declared in QUALITY CONTRACT header and COMPLIANCE AUDIT header).

**R7 structural inventory** (what V-05 R7 had; what v7 rubric exposes as missing):

| Rule | Criterion | Status in R7 V-05 |
|------|-----------|-------------------|
| RULE 1 (C-09) | Skill count in header | dedicated rule |
| RULE 2 (C-11) | Namespace tagline | dedicated rule |
| RULE 3 (C-12) | Blockquote routing hints | dedicated rule |
| RULE 4 (C-13) | Quantified output artifacts | dedicated rule |
| RULE 5 (C-10) | T3 annotations | dedicated rule |
| RULE 6 (C-14) | Bi-directional descriptions | dedicated rule |
| RULE 7 (C-15) | Mutually distinguishable taglines | dedicated rule |
| RULE 8 (C-16) | `->` separator structural enforcement | dedicated rule |
| RULE 9 (C-17) | Quality contract as numbered list | dedicated + count (C-09..C-22, Count=14) |
| RULE 10 (C-18) | Criterion-ID labels on each RULE | dedicated rule |
| RULE 11 (C-19) | Compliance gate ("do not proceed" language) | dedicated rule |
| RULE 12 (C-20) | Count assertion in RULE 9 | dedicated + inline evidence quoting RULE 9 |
| RULE 13 (C-21) | Quantified pass threshold in gate | dedicated + inline evidence quoting gate string |
| RULE 14 (C-22) | Gate criterion as RULE entry | dedicated + inline evidence naming RULE 11 |
| -- | C-23 (meta-rule inline evidence) | **satisfied by behavior of RULES 12-14; no dedicated RULE 15 (C-23) entry** |

**R8 structural obligation**: C-23 is satisfied by the behavior of RULES 12-14 in R7 V-05 (rubric
confirms V-05 PASS on C-23). However, applying the bijection pattern -- one criterion = one labeled
RULE -- requires:
- RULE 15 (C-23): dedicated entry for the meta-rule inline evidence requirement
- RULE 9 (C-17) count assertion updated: "14 rules, C-09-C-22, Count=14" -> "15 rules, C-09-C-23, Count=15"
- COMPLIANCE AUDIT: 14 checkboxes -> 15 checkboxes
- Gate PASS threshold: "14/14" -> "15/15 checked = valid output"
- QUALITY CONTRACT header: "14 rules" -> "15 rules -- one per criterion C-09 through C-23"
- COMPLETENESS SEAL: updated range and count

**Axes explored**:

- V-01: C-23 single-axis -- Add RULE 15 (C-23) as a dedicated labeled rule stating the
         meta-rule inline evidence requirement. Update RULE 9 count assertion to "15 rules,
         C-09-C-23, Count=15." COMPLIANCE AUDIT = 15 checkboxes. "15/15 checked = valid output."
         Hypothesis: R7 V-05 satisfies C-23 by behavior (RULES 12-14 carry inline evidence) but
         has no RULE 15 (C-23). A scorer querying "which rule enforces C-23?" finds nothing in
         R7 -- O(N) inspection needed. RULE 15 (C-23) closes this gap: O(1) lookup returns
         RULE 15 directly. Minimal single-axis change isolating the bijection-closure effect.

- V-02: RULE 15 with meta-rule inventory -- V-01 base + RULE 15 (C-23) carries an explicit
         named inventory of the three meta-rules it governs: RULE 12 (C-20), RULE 13 (C-21),
         RULE 14 (C-22). The inventory names them by number so that a scorer verifying C-23
         finds the three targets without searching the full contract.
         Hypothesis: V-01's RULE 15 states the requirement but doesn't name which rules it
         governs. A scorer verifying C-23 must inspect each rule to identify the three meta-rules.
         V-02 collapses this to O(1): RULE 15 names the targets directly.

- V-03: RULE 15 with full evidence citations -- V-02 base + RULE 15 (C-23) carries not only
         the inventory but the quoted evidence from each meta-rule: what string RULE 12 quotes,
         what string RULE 13 quotes, what reference RULE 14 carries. This makes RULE 15 a
         complete audit chain: names the three meta-rules AND states what each one contains.
         Hypothesis: V-02 names the meta-rules but doesn't quote their evidence. A scorer must
         still read RULE 12, 13, 14 to confirm they contain the right evidence. V-03 makes
         RULE 15 a self-contained audit: verify C-23 by reading RULE 15 alone.

- V-04: Evidence chain declared in QUALITY CONTRACT header -- V-03 base + QUALITY CONTRACT
         header explicitly declares the meta-rule evidence chain as a named structural property
         alongside the bijective invariant. Header becomes: "15 rules -- one per criterion
         C-09 through C-23 -- bijective invariant: N rules = N checkboxes always -- evidence
         chain: each meta-rule carries a pointer to its verification artifact."
         Hypothesis: The evidence chain is a structural property worth declaring at the top of
         the contract. A model that reads "evidence chain: each meta-rule carries a pointer to
         its verification artifact" before reading any rule is primed to maintain the chain
         property when adding new meta-criteria.

- V-05: Full integration -- recursive self-example -- V-04 base + RULE 15 (C-23) is itself
         an example of the principle it enforces. It names the three meta-rules it governs,
         quotes their inline evidence, AND states that RULE 15 demonstrates C-23 compliance
         by carrying its own inline evidence (the three named rules). The rule about requiring
         evidence carries evidence of its own application. This closes the chain: RULE 15 (C-23)
         both enforces the requirement and exemplifies it -- its compliance is verifiable by
         reading the rule itself without searching elsewhere.

---

## V-01 -- RULE 15 (C-23) Dedicated Entry: C-23 Single-Axis

**Axis**: Add RULE 15 (C-23) as a dedicated labeled rule enforcing the meta-rule inline evidence
requirement. Update RULE 9 (C-17) count assertion to cover 15 rules (C-09 through C-23).
COMPLIANCE AUDIT updated from 14 to 15 checkboxes. Gate updated to "15/15 checked = valid output."
QUALITY CONTRACT header updated to "15 rules". COMPLETENESS SEAL updated.
Base: R7 V-05 (14 rules, 14 checkboxes, bijective invariant in header and COMPLIANCE AUDIT header,
RULES 12-14 carry inline evidence).
**Hypothesis**: R7 V-05 satisfies C-23 via the behavior of RULES 12-14 but has no dedicated
RULE 15 (C-23) entry. A scorer querying "which rule enforces the meta-rule inline evidence
requirement (C-23)?" gets no direct answer from R7 V-05 -- they must inspect each rule to find
that C-23 is satisfied by RULES 12-14 collectively, not by a dedicated entry. RULE 15 (C-23)
closes this gap: O(1) lookup for C-23 returns RULE 15 directly. Expected: C-23 satisfaction
upgrades from implicit-pass-via-behavior to explicit-pass-via-dedicated-rule; composite improves
on C-23 bijection; no other changes from R7 V-05.

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

QUALITY CONTRACT (15 rules -- one rule per criterion C-09 through C-23, each auditable by C-NN label):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 15 (C-23) -- is the complete
  quality contract. Exactly 15 rules, one per aspirational criterion C-09 through C-23. Count = 15.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 15 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 15 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): RULE 9 (C-17) above must embed an explicit count assertion. RULE 9 in this
  contract currently asserts: "Exactly 15 rules, one per aspirational criterion C-09 through
  C-23. Count = 15. None outside." To verify this rule: find RULE 9 above and confirm the
  string "Count = 15" appears within it. Completeness is O(1) machine-checkable by count alone.
  PASS: RULE 9 contains "Count = N" and the criterion range endpoints.
  FAIL: RULE 9 asserts completeness without naming a count or range.
RULE 13 (C-21): The COMPLIANCE AUDIT gate below must state both the PASS threshold and the FAIL
  gate explicitly. The gate in this contract states: "15/15 checked = valid output. Any unchecked
  box = invalid output; do not proceed." To verify this rule: find the gate line below and
  confirm the string "15/15 checked = valid output" appears before the FAIL condition.
  PASS: Gate contains "15/15 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only the FAIL condition with no "N/N checked = valid output" threshold.
RULE 14 (C-22): The gate criterion (C-19) must appear as a dedicated numbered RULE entry in this
  quality contract. To verify this rule: find RULE 11 (C-19) above and confirm it exists as a
  numbered entry defining the gate. RULE 11 (C-19) is that entry -- it is the rule that mandates
  the gate, and it is itself audited by the gate (checkbox 11 below). A contract that enforces
  C-19 via a gate block but omits RULE 11 (C-19) from the numbered list fails this criterion.
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE 11 (C-19) appears in the numbered list.
RULE 15 (C-23): Each RULE entry that enforces a meta-criterion (C-20, C-21, or C-22) must carry
  inline evidence: either a quoted string from the artifact it verifies, or an explicit named
  reference (RULE number) pointing to the artifact's location. A meta-rule that states a
  requirement without pointing to its verification artifact does not satisfy this criterion.
  PASS: RULE 12 (C-20) quotes the count string from RULE 9; RULE 13 (C-21) quotes the pass
  threshold from the gate; RULE 14 (C-22) names RULE 11 (C-19) by number.
  FAIL: RULE 12, 13, or 14 state requirements only, with no quoted string or named reference.

COMPLIANCE AUDIT -- 15 checkboxes, one per RULE (bijective invariant: 15 rules = 15 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 15 rules covering C-09 through C-23, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) above contains "Count = 15" and the range "C-09 through C-23"
  [ ] RULE 13 (C-21): gate below states "15/15 checked = valid output" before the FAIL condition
  [ ] RULE 14 (C-22): RULE 11 (C-19) exists as a dedicated numbered entry in this quality contract
  [ ] RULE 15 (C-23): RULE 12, RULE 13, RULE 14 each carry inline evidence (quoted string or RULE reference)
15/15 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 15 rules (C-09 through C-23), 15 checkboxes, bijective invariant confirmed.
  Structural rule: adding any criterion requires adding both a RULE and a checkbox to maintain bijection.

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

## V-02 -- RULE 15 with Meta-Rule Inventory: C-23 + Named Targets

**Axis**: V-01 base (15 rules, RULE 15 (C-23) dedicated). Single enhancement: RULE 15 (C-23)
carries an explicit named inventory of the three meta-rules it governs -- RULE 12 (C-20),
RULE 13 (C-21), RULE 14 (C-22) -- listed by number within RULE 15 itself.
All other rules, checkboxes, and namespace sections identical to V-01.
**Hypothesis**: V-01's RULE 15 states the meta-rule inline evidence requirement but does not
name which rules it governs. A scorer verifying C-23 must inspect RULE 12, 13, and 14 to
confirm each carries inline evidence -- that is O(3) inspection even after finding RULE 15.
Adding a named inventory to RULE 15 reduces the verification path: RULE 15 names the three
targets, and the scorer verifies each target by number. O(1) identification + O(3) confirmation
= fully directed verification, no search. Expected: C-23 verification path is O(1) target
identification; structural distinction from V-01 is the target inventory in RULE 15.

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

QUALITY CONTRACT (15 rules -- one rule per criterion C-09 through C-23, each auditable by C-NN label):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 15 (C-23) -- is the complete
  quality contract. Exactly 15 rules, one per aspirational criterion C-09 through C-23. Count = 15.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 15 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 15 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): RULE 9 (C-17) above must embed an explicit count assertion. RULE 9 in this
  contract currently asserts: "Exactly 15 rules, one per aspirational criterion C-09 through
  C-23. Count = 15. None outside." To verify this rule: find RULE 9 above and confirm the
  string "Count = 15" appears within it. Completeness is O(1) machine-checkable by count alone.
  PASS: RULE 9 contains "Count = N" and the criterion range endpoints.
  FAIL: RULE 9 asserts completeness without naming a count or range.
RULE 13 (C-21): The COMPLIANCE AUDIT gate below must state both the PASS threshold and the FAIL
  gate explicitly. The gate in this contract states: "15/15 checked = valid output. Any unchecked
  box = invalid output; do not proceed." To verify this rule: find the gate line below and
  confirm the string "15/15 checked = valid output" appears before the FAIL condition.
  PASS: Gate contains "15/15 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only the FAIL condition with no "N/N checked = valid output" threshold.
RULE 14 (C-22): The gate criterion (C-19) must appear as a dedicated numbered RULE entry in this
  quality contract. To verify this rule: find RULE 11 (C-19) above and confirm it exists as a
  numbered entry defining the gate. RULE 11 (C-19) is that entry -- it is the rule that mandates
  the gate, and it is itself audited by the gate (checkbox 11 below).
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE 11 (C-19) appears in the numbered list.
RULE 15 (C-23): Each RULE entry that enforces a meta-criterion (C-20, C-21, or C-22) must carry
  inline evidence pointing to the artifact it verifies. The three meta-rules in this contract are:
  RULE 12 (C-20), RULE 13 (C-21), and RULE 14 (C-22). Each must carry either a quoted string
  from the artifact it verifies or an explicit RULE number reference. A meta-rule that states a
  requirement without pointing to its verification artifact does not satisfy this criterion.
  PASS: RULE 12 (C-20) quotes the count string; RULE 13 (C-21) quotes the pass threshold;
  RULE 14 (C-22) names RULE 11 (C-19) by number.
  FAIL: Any of RULE 12, 13, or 14 states requirements with no quoted string or named reference.

COMPLIANCE AUDIT -- 15 checkboxes, one per RULE (bijective invariant: 15 rules = 15 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 15 rules covering C-09 through C-23, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) above contains "Count = 15" and the range "C-09 through C-23"
  [ ] RULE 13 (C-21): gate below states "15/15 checked = valid output" before the FAIL condition
  [ ] RULE 14 (C-22): RULE 11 (C-19) exists as a dedicated numbered entry in this quality contract
  [ ] RULE 15 (C-23): RULE 12, RULE 13, RULE 14 each carry inline evidence (quoted string or RULE reference)
15/15 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 15 rules (C-09 through C-23), 15 checkboxes, bijective invariant confirmed.
  Structural rule: adding any criterion requires adding both a RULE and a checkbox to maintain bijection.

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

## V-03 -- RULE 15 with Full Evidence Citations: Self-Contained Audit Chain

**Axis**: V-02 base (15 rules, RULE 15 names the three meta-rules by number). Single enhancement:
RULE 15 (C-23) additionally quotes the specific inline evidence each meta-rule carries:
what string RULE 12 cites, what string RULE 13 cites, what reference RULE 14 carries.
All other rules, checkboxes, and namespace sections identical to V-02.
**Hypothesis**: V-02 names the three meta-rules in RULE 15 so the scorer knows where to look.
But the scorer must still read RULE 12, 13, 14 to confirm each contains the right evidence.
V-03 makes RULE 15 a complete audit in itself: it names each meta-rule AND states what evidence
it carries. A scorer verifying C-23 reads RULE 15, sees the three targets and their expected
evidence strings, then confirms each. Zero open-ended search required at any step.

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

QUALITY CONTRACT (15 rules -- one rule per criterion C-09 through C-23, each auditable by C-NN label):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 15 (C-23) -- is the complete
  quality contract. Exactly 15 rules, one per aspirational criterion C-09 through C-23. Count = 15.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 15 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 15 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): RULE 9 (C-17) above must embed an explicit count assertion. RULE 9 in this
  contract currently asserts: "Exactly 15 rules, one per aspirational criterion C-09 through
  C-23. Count = 15. None outside." To verify this rule: find RULE 9 above and confirm the
  string "Count = 15" appears within it. Completeness is O(1) machine-checkable by count alone.
  PASS: RULE 9 contains "Count = N" and the criterion range endpoints.
  FAIL: RULE 9 asserts completeness without naming a count or range.
RULE 13 (C-21): The COMPLIANCE AUDIT gate below must state both the PASS threshold and the FAIL
  gate explicitly. The gate in this contract states: "15/15 checked = valid output. Any unchecked
  box = invalid output; do not proceed." To verify this rule: find the gate line below and
  confirm the string "15/15 checked = valid output" appears before the FAIL condition.
  PASS: Gate contains "15/15 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only the FAIL condition with no "N/N checked = valid output" threshold.
RULE 14 (C-22): The gate criterion (C-19) must appear as a dedicated numbered RULE entry in this
  quality contract. To verify this rule: find RULE 11 (C-19) above and confirm it exists as a
  numbered entry defining the gate. RULE 11 (C-19) is that entry -- it is the rule that mandates
  the gate, and it is itself audited by the gate (checkbox 11 below).
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE 11 (C-19) appears in the numbered list.
RULE 15 (C-23): Each RULE entry that enforces a meta-criterion (C-20, C-21, or C-22) must carry
  inline evidence pointing to its verification artifact. The three meta-rules in this contract
  and their required evidence are:
    RULE 12 (C-20): must contain the quoted string "Count = 15" from RULE 9
    RULE 13 (C-21): must contain the quoted string "15/15 checked = valid output" from the gate
    RULE 14 (C-22): must name RULE 11 (C-19) explicitly by number
  To verify C-23: confirm each of the three meta-rules above contains its stated evidence.
  A meta-rule that states a requirement without the quoted string or RULE reference fails this rule.
  PASS: all three meta-rules contain their evidence as stated above.
  FAIL: any meta-rule carries only a requirement statement with no quoted string or named reference.

COMPLIANCE AUDIT -- 15 checkboxes, one per RULE (bijective invariant: 15 rules = 15 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 15 rules covering C-09 through C-23, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) above contains "Count = 15" and the range "C-09 through C-23"
  [ ] RULE 13 (C-21): gate below states "15/15 checked = valid output" before the FAIL condition
  [ ] RULE 14 (C-22): RULE 11 (C-19) exists as a dedicated numbered entry in this quality contract
  [ ] RULE 15 (C-23): RULE 12 contains "Count = 15"; RULE 13 contains "15/15 checked = valid output"; RULE 14 names RULE 11
15/15 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 15 rules (C-09 through C-23), 15 checkboxes, bijective invariant confirmed.
  Structural rule: adding any criterion requires adding both a RULE and a checkbox to maintain bijection.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

[Namespace sections identical to V-01. Transcribe Scout through Org sections exactly as in V-01,
followed by BARE MODE and FILTERED MODE instructions.]
```

---

## V-04 -- Evidence Chain Declared in QUALITY CONTRACT Header: Combination

**Axis**: V-03 base (15 rules, RULE 15 carries full evidence citations for all three meta-rules).
Single addition: QUALITY CONTRACT header explicitly declares the meta-rule evidence chain as a
named structural property alongside the bijective invariant.
Header becomes: "15 rules -- one per criterion C-09 through C-23 -- bijective invariant:
N rules = N checkboxes always -- evidence chain: each meta-rule carries a pointer to its
verification artifact."
All rules, checkboxes, and namespace sections identical to V-03.
**Hypothesis**: V-03's evidence chain is structurally present but not declared at the contract
level. A model reading V-03 encounters the evidence chain only when reading RULE 15. Making
the evidence chain a named contract property -- declared in the header before any rule is read --
primes the model to maintain the chain when adding new meta-criteria. The header declaration
converts the evidence chain from an observed behavior into an enforced contract invariant.
Expected: all 15 aspirational PASS; the structural distinction from V-03 is visibility of
the evidence chain at contract entry, not within the rule body.

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

QUALITY CONTRACT (15 rules -- one per criterion C-09 through C-23 -- bijective invariant: N rules = N checkboxes always -- evidence chain: each meta-rule carries a pointer to its verification artifact):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 15 (C-23) -- is the complete
  quality contract. Exactly 15 rules, one per aspirational criterion C-09 through C-23. Count = 15.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 15 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 15 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): RULE 9 (C-17) above must embed an explicit count assertion. RULE 9 in this
  contract currently asserts: "Exactly 15 rules, one per aspirational criterion C-09 through
  C-23. Count = 15. None outside." To verify this rule: find RULE 9 above and confirm the
  string "Count = 15" appears within it. Completeness is O(1) machine-checkable by count alone.
  PASS: RULE 9 contains "Count = N" and the criterion range endpoints.
  FAIL: RULE 9 asserts completeness without naming a count or range.
RULE 13 (C-21): The COMPLIANCE AUDIT gate below must state both the PASS threshold and the FAIL
  gate explicitly. The gate in this contract states: "15/15 checked = valid output. Any unchecked
  box = invalid output; do not proceed." To verify this rule: find the gate line below and
  confirm the string "15/15 checked = valid output" appears before the FAIL condition.
  PASS: Gate contains "15/15 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only the FAIL condition with no "N/N checked = valid output" threshold.
RULE 14 (C-22): The gate criterion (C-19) must appear as a dedicated numbered RULE entry in this
  quality contract. To verify this rule: find RULE 11 (C-19) above and confirm it exists as a
  numbered entry defining the gate. RULE 11 (C-19) is that entry -- it is the rule that mandates
  the gate, and it is itself audited by the gate (checkbox 11 below).
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE 11 (C-19) appears in the numbered list.
RULE 15 (C-23): Each RULE entry that enforces a meta-criterion (C-20, C-21, or C-22) must carry
  inline evidence pointing to its verification artifact. Per the evidence chain declared in the
  QUALITY CONTRACT header above, the three meta-rules and their required evidence are:
    RULE 12 (C-20): must contain the quoted string "Count = 15" from RULE 9
    RULE 13 (C-21): must contain the quoted string "15/15 checked = valid output" from the gate
    RULE 14 (C-22): must name RULE 11 (C-19) explicitly by number
  To verify C-23: confirm each of the three meta-rules above contains its stated evidence.
  A meta-rule that states a requirement without the quoted string or RULE reference fails this rule.
  PASS: all three meta-rules contain their evidence as stated above.
  FAIL: any meta-rule carries only a requirement statement with no quoted string or named reference.

COMPLIANCE AUDIT -- 15 checkboxes, one per RULE (bijective invariant: 15 rules = 15 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 15 rules covering C-09 through C-23, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) above contains "Count = 15" and the range "C-09 through C-23"
  [ ] RULE 13 (C-21): gate below states "15/15 checked = valid output" before the FAIL condition
  [ ] RULE 14 (C-22): RULE 11 (C-19) exists as a dedicated numbered entry in this quality contract
  [ ] RULE 15 (C-23): RULE 12 contains "Count = 15"; RULE 13 contains "15/15 checked = valid output"; RULE 14 names RULE 11
15/15 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 15 rules (C-09 through C-23), 15 checkboxes, bijective invariant confirmed,
  evidence chain confirmed: RULE 12->RULE 9, RULE 13->gate, RULE 14->RULE 11, RULE 15->all three.
  Structural rule: adding any criterion requires adding both a RULE and a checkbox to maintain bijection.
  Evidence chain rule: adding any meta-criterion requires its enforcing RULE to carry inline evidence.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

[Namespace sections identical to V-01. Transcribe Scout through Org sections exactly as in V-01,
followed by BARE MODE and FILTERED MODE instructions.]
```

---

## V-05 -- Full Integration: Recursive Self-Example

**Axis**: V-04 base (15 rules, bijective invariant + evidence chain both declared in header,
RULE 15 carries full evidence citations). Single enhancement: RULE 15 (C-23) is itself an
example of the principle it enforces. It states that its own compliance is verifiable by the
named references it carries (to RULE 12, RULE 13, RULE 14), making RULE 15 both the rule
that requires evidence AND the demonstration that a rule about evidence can itself carry evidence.
All other rules, checkboxes, and namespace sections identical to V-04.
**Hypothesis**: V-04's RULE 15 carries full citations but does not name its own compliance
posture -- it doesn't say "this rule itself demonstrates C-23 compliance." A scorer verifying
that the quality contract is internally consistent must check: does RULE 15 satisfy its own
requirement? V-05 makes this explicit: RULE 15 carries inline evidence (the three named rules)
AND states that verifying RULE 15 compliance requires only reading RULE 15 itself. The rule
is self-demonstrating: its compliance is verifiable without searching elsewhere. This closes
the recursive audit loop -- every meta-rule in the contract, including the one about meta-rules,
is auditable O(1) from the rule itself.

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

QUALITY CONTRACT (15 rules -- one per criterion C-09 through C-23 -- bijective invariant: N rules = N checkboxes always -- evidence chain: each meta-rule carries a pointer to its verification artifact):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 15 (C-23) -- is the complete
  quality contract. Exactly 15 rules, one per aspirational criterion C-09 through C-23. Count = 15.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 15 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 15 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): RULE 9 (C-17) above must embed an explicit count assertion. RULE 9 in this
  contract currently asserts: "Exactly 15 rules, one per aspirational criterion C-09 through
  C-23. Count = 15. None outside." To verify this rule: find RULE 9 above and confirm the
  string "Count = 15" appears within it. Completeness is O(1) machine-checkable by count alone.
  PASS: RULE 9 contains "Count = N" and the criterion range endpoints.
  FAIL: RULE 9 asserts completeness without naming a count or range.
RULE 13 (C-21): The COMPLIANCE AUDIT gate below must state both the PASS threshold and the FAIL
  gate explicitly. The gate in this contract states: "15/15 checked = valid output. Any unchecked
  box = invalid output; do not proceed." To verify this rule: find the gate line below and
  confirm the string "15/15 checked = valid output" appears before the FAIL condition.
  PASS: Gate contains "15/15 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only the FAIL condition with no "N/N checked = valid output" threshold.
RULE 14 (C-22): The gate criterion (C-19) must appear as a dedicated numbered RULE entry in this
  quality contract. To verify this rule: find RULE 11 (C-19) above and confirm it exists as a
  numbered entry defining the gate. RULE 11 (C-19) is that entry -- it is the rule that mandates
  the gate, and it is itself audited by the gate (checkbox 11 below).
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE 11 (C-19) appears in the numbered list.
RULE 15 (C-23): Each RULE entry that enforces a meta-criterion (C-20, C-21, or C-22) must carry
  inline evidence pointing to its verification artifact. This rule itself demonstrates compliance
  with C-23 by carrying inline evidence: it names the three meta-rules it governs (RULE 12,
  RULE 13, RULE 14) and states the evidence each must carry. To verify C-23, read this rule alone:
    RULE 12 (C-20) must contain: "Count = 15" (quoted from RULE 9 above)
    RULE 13 (C-21) must contain: "15/15 checked = valid output" (quoted from the gate below)
    RULE 14 (C-22) must name: RULE 11 (C-19) by number (present above as a dedicated entry)
  This rule is self-demonstrating: its own compliance is verifiable by reading RULE 15 alone,
  without searching elsewhere in the contract. The evidence chain is closed.
  PASS: all three meta-rules contain their stated evidence; RULE 15 names all three by number.
  FAIL: any meta-rule lacks its evidence; or RULE 15 does not name the three meta-rules by number.

COMPLIANCE AUDIT -- 15 checkboxes, one per RULE (bijective invariant: 15 rules = 15 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 15 rules covering C-09 through C-23, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) above contains "Count = 15" and the range "C-09 through C-23"
  [ ] RULE 13 (C-21): gate below states "15/15 checked = valid output" before the FAIL condition
  [ ] RULE 14 (C-22): RULE 11 (C-19) exists as a dedicated numbered entry in this quality contract
  [ ] RULE 15 (C-23): RULE 12 contains "Count = 15"; RULE 13 contains "15/15 checked = valid output"; RULE 14 names RULE 11; RULE 15 names all three meta-rules by number
15/15 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 15 rules (C-09 through C-23), 15 checkboxes, bijective invariant confirmed,
  evidence chain confirmed: RULE 12->RULE 9, RULE 13->gate, RULE 14->RULE 11, RULE 15->all three.
  Structural rule: adding any criterion requires adding both a RULE and a checkbox to maintain bijection.
  Evidence chain rule: adding any meta-criterion requires its enforcing RULE to carry inline evidence.

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
