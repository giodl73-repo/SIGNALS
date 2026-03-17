---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 7
rubric: simulations/quest/rubrics/signal-rubric-v6-2026-03-16.md
---

# Quest Variate -- /signal (Round 7)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v6-2026-03-16.md` (v6, 14 aspirational criteria C-09 through C-22)

**R6 champion**: V-05 (100/100 on v5 rubric). QUALITY CONTRACT with 11 rules covering C-09
through C-19. COMPLIANCE AUDIT with 11 checkboxes. Bijective: 11 rules = 11 checkboxes.
"11/11 checked" PASS threshold present via V-04 bijection header (which V-05 inherited).

**R6 structural inventory** (what V-05 had; what v6 rubric exposes as missing):

| Rule | Criterion | Status in R6 V-05 |
|------|-----------|-------------------|
| RULE 1 (C-09) | Skill count in header | dedicated rule |
| RULE 2 (C-11) | Namespace tagline | dedicated rule |
| RULE 3 (C-12) | Blockquote routing hints | dedicated rule |
| RULE 4 (C-13) | Quantified output artifacts | dedicated rule |
| RULE 5 (C-10) | T3 annotations | dedicated rule |
| RULE 6 (C-14) | Bi-directional descriptions | dedicated rule |
| RULE 7 (C-15) | Mutually distinguishable taglines | dedicated rule |
| RULE 8 (C-16) | `->` separator structural enforcement | dedicated rule |
| RULE 9 (C-17) | Quality contract as numbered list | dedicated + count (C-09..C-19, Count=11) |
| RULE 10 (C-18) | Criterion-ID labels on each RULE | dedicated rule |
| RULE 11 (C-19) | Compliance gate ("do not proceed" language) | dedicated rule |
| -- | C-20 (count assertion in RULE 9) | **satisfied by RULE 9 content; no dedicated RULE 12 (C-20) entry** |
| -- | C-21 (explicit N/N pass threshold in gate) | **"11/11" present in gate; no dedicated RULE 13 (C-21) entry** |
| -- | C-22 (gate criterion as RULE entry) | **RULE 11 (C-19) exists; no dedicated RULE 14 (C-22) entry** |

**R7 structural obligation**: Three criteria (C-20, C-21, C-22) are satisfied by content in R6 V-05
but have no dedicated RULE entries. The E-1 pattern ("one criterion = one labeled rule") applied
to C-20, C-21, and C-22 requires:
- RULE 12 (C-20): dedicated entry for the count-assertion requirement
- RULE 13 (C-21): dedicated entry for the quantified pass-threshold requirement
- RULE 14 (C-22): dedicated entry for the gate-criterion-as-rule requirement
- RULE 9 (C-17) count assertion updated: "11 rules, C-09-C-19" becomes "14 rules, C-09-C-22"
- COMPLIANCE AUDIT: 11 checkboxes -> 14 checkboxes
- Gate PASS threshold: "11/11" -> "14/14 checked = valid output"
- COMPLETENESS SEAL: updated range and count

**Axes explored**:

- V-01: C-20 single-axis -- Add RULE 12 (C-20) as dedicated entry. Update RULE 9 count assertion
         to "12 rules, C-09-C-20, Count=12." COMPLIANCE AUDIT = 12 checkboxes.
         Hypothesis: C-20 is satisfied by RULE 9 content in R6 V-03+ but has no dedicated RULE
         entry. A scorer querying "which rule enforces C-20?" finds nothing in R6 -- O(N)
         inspection needed. RULE 12 (C-20) makes it O(1). This single axis isolates the
         bijection-closure effect of adding one rule for one criterion.

- V-02: C-20+C-21 dual-axis -- V-01 base + RULE 13 (C-21) added. RULE 9 updated to "13 rules,
         C-09-C-21, Count=13." COMPLIANCE AUDIT = 13 checkboxes. "13/13 checked = valid output"
         PASS threshold added to gate.
         Hypothesis: C-21 requires the pass threshold be in "N/N" fraction form. R6 V-04 had
         "11/11 = valid" but no dedicated RULE entry for C-21 itself. V-02 adds RULE 13 (C-21)
         as the named enforcement rule AND updates the gate to show "13/13". Both halves now
         explicit: the PASS fraction and the RULE that mandates it.

- V-03: Full 14-rule contract -- V-02 base + RULE 14 (C-22) added. RULE 9 updated to "14 rules,
         C-09-C-22, Count=14." COMPLIANCE AUDIT = 14 checkboxes. "14/14 checked = valid output."
         Hypothesis: RULE 14 (C-22) is the meta-completion rule: it names the bijection-
         through-gate-criterion requirement that C-22 describes. With RULE 14 present, every
         aspirational criterion C-09-C-22 has exactly one dedicated RULE entry. The bijection
         is closed. RULE 9's count assertion now covers the full set.

- V-04: Bijective invariant in header -- V-03 base + QUALITY CONTRACT header explicitly names
         the bijective invariant as a structural property of the contract itself.
         Header becomes: "QUALITY CONTRACT (14 rules -- one per criterion C-09 through C-22 --
         bijective invariant: N rules = N checkboxes always)."
         Hypothesis: R6 V-04 made bijection explicit in the COMPLIANCE AUDIT header. V-04 lifts
         it to the QUALITY CONTRACT header, making the invariant visible before any rule is read.
         A model that sees "bijective invariant: N rules = N checkboxes always" in the header
         cannot add a criterion without adding both a RULE and a checkbox -- the invariant is
         declared as a first-class constraint, not inferred from counting.

- V-05: Full integration -- V-04 base + RULE 12 (C-20), RULE 13 (C-21), and RULE 14 (C-22)
         enhanced with cross-references to the concrete evidence of their satisfaction.
         RULE 12 names RULE 9 explicitly; RULE 13 names the exact pass-string required; RULE 14
         names RULE 11 (C-19) as the concrete evidence.
         Hypothesis: Cross-referencing makes each new rule auditable in O(1) not just by label
         but by content: to verify RULE 12 (C-20), read RULE 9 and confirm "Count = 14" is
         present. To verify RULE 13 (C-21), read the gate and confirm "14/14 = valid output"
         is present. To verify RULE 14 (C-22), find RULE 11 (C-19) and confirm it exists.
         No inference at any step; each rule is a direct pointer to its evidence.

---

## V-01 -- RULE 12 (C-20) Dedicated Entry: C-20 Single-Axis

**Axis**: Add RULE 12 (C-20) as a dedicated labeled rule enforcing the count-assertion
requirement. Update RULE 9 (C-17) count assertion to cover 12 rules (C-09 through C-20).
COMPLIANCE AUDIT updated from 11 to 12 checkboxes. COMPLETENESS SEAL updated to RULE 12 (C-20).
Base: R6 V-05 (11 rules, 11 checkboxes, QUALITY CONTRACT label, "11/11" bijection header in
COMPLIANCE AUDIT, COMPLETENESS SEAL with bijection statement).
**Hypothesis**: R6 V-05 satisfies C-20 via RULE 9's content (it asserts "Count = 11, C-09-C-19")
but has no RULE 12 (C-20) entry. A scorer querying "which rule enforces the count-assertion
requirement (C-20)?" gets no direct answer from R6 V-05 -- they must inspect RULE 9 and infer
that C-20 is satisfied by RULE 9's body rather than by a dedicated rule. RULE 12 (C-20) closes
this gap: the O(1) lookup for C-20 returns RULE 12 directly. Expected: C-20 satisfaction
upgrades from implicit-pass to explicit-pass; C-21 and C-22 remain unresolved (no dedicated
RULE entries); score improves on C-20 but not on C-21/C-22 criteria.

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

QUALITY CONTRACT (12 rules -- one rule per criterion C-09 through C-20, each auditable by C-NN label):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 12 (C-20) -- is the complete
  quality contract. Exactly 12 rules, one per aspirational criterion C-09 through C-20. Count = 12.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 12 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 12 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): The RULE enforcing C-17 (RULE 9 above) must contain an explicit count assertion
  stating the exact rule total and criterion range covered. The assertion must be embedded within
  RULE 9 itself. RULE 9 in this contract asserts "Exactly 12 rules, one per aspirational criterion
  C-09 through C-20. Count = 12." This makes completeness O(1) machine-checkable by count.
  PASS: RULE 9 states "Exactly N rules, one per aspirational criterion C-09 through C-NN. Count = N."
  FAIL: RULE 9 states only "this numbered list is the complete quality contract" with no count.

COMPLIANCE AUDIT -- 12 checkboxes, one per RULE (bijective: each rule has exactly one checkbox):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 12 rules covering C-09 through C-20, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) contains an explicit count assertion with rule total and range
All 12 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: RULE 1 (C-09) through RULE 12 (C-20) is the exhaustive quality contract.

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

## V-02 -- RULE 13 (C-21) Added: C-20+C-21 Dual-Axis

**Axis**: V-01 base (12 rules, RULE 12 (C-20) dedicated, RULE 9 count=12). Add RULE 13 (C-21)
as dedicated labeled rule. Update RULE 9 count to "13 rules, C-09-C-21, Count=13." Update
COMPLIANCE AUDIT to 13 checkboxes. Add "13/13 checked = valid output" explicit PASS threshold
to the gate line. COMPLETENESS SEAL updated to RULE 13 (C-21).
**Hypothesis**: C-21 requires both halves of the gate to be explicit: the FAIL gate ("any
unchecked = invalid output") AND the PASS threshold in fraction form ("N/N checked = valid
output"). R6 V-04 introduced the "11/11" format but had no dedicated RULE for it -- a scorer
querying "which rule mandates the N/N pass threshold?" got no direct answer. RULE 13 (C-21)
closes this gap: O(1) lookup for C-21 returns RULE 13. The "13/13 checked = valid output" line
in the gate block is the concrete evidence of RULE 13 compliance. Expected: C-20 and C-21
now both have dedicated RULE entries; C-22 still does not (RULE 14 absent).

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

QUALITY CONTRACT (13 rules -- one rule per criterion C-09 through C-21, each auditable by C-NN label):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 13 (C-21) -- is the complete
  quality contract. Exactly 13 rules, one per aspirational criterion C-09 through C-21. Count = 13.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 13 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 13 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): The RULE enforcing C-17 (RULE 9 above) must contain an explicit count assertion
  stating the exact rule total and criterion range covered. RULE 9 in this contract asserts
  "Exactly 13 rules, one per aspirational criterion C-09 through C-21. Count = 13." This makes
  completeness O(1) machine-checkable: count the rules, compare to stated total, verify range.
  PASS: RULE 9 states "Exactly N rules, one per aspirational criterion C-09 through C-NN. Count = N."
  FAIL: RULE 9 states only "this numbered list is the complete quality contract" with no count.
RULE 13 (C-21): The COMPLIANCE AUDIT gate must state both halves of the binary explicitly: the
  PASS threshold ("N/N checked = valid output") AND the FAIL gate ("any unchecked box = invalid
  output; do not proceed"). A gate that states only the failure condition leaves the success
  condition implicit, which is a structural gap.
  PASS: Gate states "13/13 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only "Any unchecked box = invalid output; do not proceed." (no pass threshold)

COMPLIANCE AUDIT -- 13 checkboxes, one per RULE (bijective: each rule has exactly one checkbox):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 13 rules covering C-09 through C-21, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) contains an explicit count assertion with rule total and range
  [ ] RULE 13 (C-21): gate states both "13/13 = valid output" PASS and FAIL thresholds explicitly
13/13 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: RULE 1 (C-09) through RULE 13 (C-21) is the exhaustive quality contract.

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

## V-03 -- RULE 14 (C-22) Added: Full 14-Rule Contract

**Axis**: V-02 base (13 rules, RULE 12 C-20, RULE 13 C-21, "13/13" pass threshold). Add RULE 14
(C-22) as dedicated labeled rule. Update RULE 9 count to "14 rules, C-09-C-22, Count=14."
COMPLIANCE AUDIT = 14 checkboxes. Gate updated to "14/14 checked = valid output." COMPLETENESS
SEAL updated to "14 rules, 14 criteria, one-to-one bijection."
**Hypothesis**: RULE 14 (C-22) is the meta-completion rule: it names the bijection-through-gate-
criterion requirement. With RULE 14 present, every aspirational criterion C-09 through C-22 has
exactly one dedicated RULE entry in the quality contract. The bijection closes: 14 rules = 14
checkboxes = 14 criteria. RULE 9 (C-17) now asserts "Count = 14, C-09-C-22" -- a complete and
self-verifying count that covers the entire v6 aspirational tier. Expected: all 14 aspirational
criteria PASS; all 5 essential criteria PASS; composite 100/100 on v6 rubric.

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

QUALITY CONTRACT (14 rules -- one rule per criterion C-09 through C-22, each auditable by C-NN label):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 14 (C-22) -- is the complete
  quality contract. Exactly 14 rules, one per aspirational criterion C-09 through C-22. Count = 14.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 14 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 14 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): The RULE enforcing C-17 (RULE 9 above) must contain an explicit count assertion
  stating the exact rule total and criterion range covered. RULE 9 in this contract asserts
  "Exactly 14 rules, one per aspirational criterion C-09 through C-22. Count = 14." This makes
  completeness O(1) machine-checkable: count the rules, compare to stated total, verify range.
  PASS: RULE 9 states "Exactly N rules, one per aspirational criterion C-09 through C-NN. Count = N."
  FAIL: RULE 9 states only "this numbered list is the complete quality contract" with no count.
RULE 13 (C-21): The COMPLIANCE AUDIT gate must state both halves of the binary explicitly: the
  PASS threshold ("N/N checked = valid output") AND the FAIL gate ("any unchecked box = invalid
  output; do not proceed"). A gate with only a failure branch leaves the success condition implicit.
  PASS: Gate states "14/14 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only "Any unchecked box = invalid output; do not proceed." (no pass threshold)
RULE 14 (C-22): The criterion that mandates the compliance gate (C-19) must appear as a numbered
  RULE entry in this quality contract. RULE 11 (C-19) above is that entry. Without it, the gate
  enforces N criteria but the rule list covers only N-1, breaking the bijection at the gate
  criterion itself. A quality contract that enforces C-19 via a gate block but has no corresponding
  RULE 11 (C-19) entry does not satisfy this criterion.
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE N (C-19) exists in the numbered list.

COMPLIANCE AUDIT -- 14 checkboxes, one per RULE (bijective: each rule has exactly one checkbox):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 14 rules covering C-09 through C-22, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) contains an explicit count assertion with rule total and range
  [ ] RULE 13 (C-21): gate states both "14/14 = valid output" PASS and FAIL thresholds explicitly
  [ ] RULE 14 (C-22): RULE 11 (C-19) is present as a dedicated numbered entry in this quality contract
14/14 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 14 rules (C-09 through C-22), 14 checkboxes, one-to-one bijection.

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

## V-04 -- Bijective Invariant Declared in Header: Combination

**Axis**: V-03 base (14 rules, all three new RULE entries, "14/14" pass threshold, full bijection).
Single addition: QUALITY CONTRACT header explicitly declares the bijective invariant as a named
structural property of the contract -- not just implied by having equal counts of rules and
checkboxes. COMPLETENESS SEAL upgraded to name the invariant as an enforced constraint.
**Hypothesis**: V-03's bijection is structurally correct but the invariant is implicit -- a model
reading V-03 could add a 15th criterion without adding a 15th checkbox and still technically
"follow the rules" unless it counts. Making the bijective invariant explicit in the header
("bijective invariant: N rules = N checkboxes always") converts it from a verifiable structural
property into a declared enforced constraint. A model that reads "bijective invariant: N rules =
N checkboxes always" before reading any rule is primed to treat the bijection as inviolable.
Expected: all 14 aspirational PASS; structural robustness against contract mutation increases.

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

QUALITY CONTRACT (14 rules -- one per criterion C-09 through C-22 -- bijective invariant: N rules = N checkboxes always):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 14 (C-22) -- is the complete
  quality contract. Exactly 14 rules, one per aspirational criterion C-09 through C-22. Count = 14.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 14 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 14 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): The RULE enforcing C-17 (RULE 9 above) must contain an explicit count assertion
  stating the exact rule total and criterion range covered. RULE 9 in this contract asserts
  "Exactly 14 rules, one per aspirational criterion C-09 through C-22. Count = 14." This makes
  completeness O(1) machine-checkable: count the rules, compare to stated total, verify range.
  PASS: RULE 9 states "Exactly N rules, one per aspirational criterion C-09 through C-NN. Count = N."
  FAIL: RULE 9 states only "this numbered list is the complete quality contract" with no count.
RULE 13 (C-21): The COMPLIANCE AUDIT gate must state both halves of the binary explicitly: the
  PASS threshold ("N/N checked = valid output") AND the FAIL gate ("any unchecked box = invalid
  output; do not proceed"). A gate with only a failure branch leaves the success condition implicit.
  PASS: Gate states "14/14 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only "Any unchecked box = invalid output; do not proceed." (no pass threshold)
RULE 14 (C-22): The criterion that mandates the compliance gate (C-19) must appear as a numbered
  RULE entry in this quality contract. RULE 11 (C-19) above is that entry. Without it, the gate
  enforces N criteria but the rule list covers only N-1, breaking the bijection at the gate
  criterion itself. A quality contract that enforces C-19 via a gate block but has no corresponding
  RULE 11 (C-19) entry does not satisfy this criterion.
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE N (C-19) exists in the numbered list.

COMPLIANCE AUDIT -- 14 checkboxes, one per RULE (bijective invariant: 14 rules = 14 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 14 rules covering C-09 through C-22, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) contains an explicit count assertion with rule total and range
  [ ] RULE 13 (C-21): gate states both "14/14 = valid output" PASS and FAIL thresholds explicitly
  [ ] RULE 14 (C-22): RULE 11 (C-19) is present as a dedicated numbered entry in this quality contract
14/14 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 14 rules (C-09 through C-22), 14 checkboxes, bijective invariant confirmed.
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

## V-05 -- Full Integration: Cross-References in New Rule Definitions

**Axis**: V-04 base (14 rules, bijective invariant in header, "14/14" pass threshold, COMPLETENESS
SEAL with bijection structural rule). Three enhancements: RULE 12 (C-20) explicitly names RULE 9
as "RULE 9 (C-17) above" and quotes the specific count-assertion string it is verifying; RULE 13
(C-21) quotes the exact pass-threshold string ("14/14 checked = valid output") that must appear
in the gate; RULE 14 (C-22) names RULE 11 (C-19) as the concrete evidence of C-22 satisfaction,
pointing the verifier directly to the fulfillment location.
**Hypothesis**: V-04's new rules describe what is required but do not point to where it is
satisfied. A scorer verifying RULE 12 (C-20) must read RULE 9 and decide whether it contains the
required assertion -- that's a two-step inference. V-05 makes RULE 12 a pointer: "RULE 9 (C-17)
above currently asserts 'Exactly 14 rules, one per criterion C-09 through C-22. Count = 14.'"
Verification collapses to: find RULE 9, confirm the quoted string is present. Same for RULE 13
(point to "14/14 checked = valid output" in the gate) and RULE 14 (point to RULE 11 (C-19) by
name). Each new rule becomes a self-auditing pointer, not just a requirement statement. Expected:
all 14 aspirational PASS; C-20/C-21/C-22 verification is O(1) with zero inference required.

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

QUALITY CONTRACT (14 rules -- one per criterion C-09 through C-22 -- bijective invariant: N rules = N checkboxes always):
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
RULE 9 (C-17): This numbered list -- RULE 1 (C-09) through RULE 14 (C-22) -- is the complete
  quality contract. Exactly 14 rules, one per aspirational criterion C-09 through C-22. Count = 14.
  None outside. No quality rule exists in an appendix, separate block, or inline prose.
  If fewer than 14 rules are present, the contract is incomplete; do not proceed.
RULE 10 (C-18): Each RULE entry carries its enforcing criterion ID in the heading -- RULE N (C-NN).
  Every rule in this list has a C-NN label. A scorer mapping from criterion ID to its rule arrives
  in O(1): look up RULE N (C-NN) directly. No inference required.
  PASS: RULE 6 (C-14): [description]   FAIL: RULE 6: [description] -- no C-NN label
RULE 11 (C-19): Output generation is gated by the COMPLIANCE AUDIT block below. All 14 RULE
  checkboxes must be verified before any namespace section is transcribed. This rule is itself on
  the checklist -- verifying it confirms the gate was invoked. A compliance description living
  only in inline prose (not as a named block with checkboxes) does not satisfy this rule.
RULE 12 (C-20): RULE 9 (C-17) above must embed an explicit count assertion. RULE 9 in this
  contract currently asserts: "Exactly 14 rules, one per aspirational criterion C-09 through
  C-22. Count = 14. None outside." To verify this rule: find RULE 9 above and confirm the
  string "Count = 14" appears within it. Completeness is O(1) machine-checkable by count alone.
  PASS: RULE 9 contains "Count = N" and the criterion range endpoints.
  FAIL: RULE 9 asserts completeness without naming a count or range.
RULE 13 (C-21): The COMPLIANCE AUDIT gate below must state both the PASS threshold and the FAIL
  gate explicitly. The gate in this contract states: "14/14 checked = valid output. Any unchecked
  box = invalid output; do not proceed." To verify this rule: find the gate line below and
  confirm the string "14/14 checked = valid output" appears before the FAIL condition.
  PASS: Gate contains "14/14 checked = valid output. Any unchecked box = invalid output; do not proceed."
  FAIL: Gate states only the FAIL condition with no "N/N checked = valid output" threshold.
RULE 14 (C-22): The gate criterion (C-19) must appear as a dedicated numbered RULE entry in this
  quality contract. To verify this rule: find RULE 11 (C-19) above and confirm it exists as a
  numbered entry defining the gate. RULE 11 (C-19) is that entry -- it is the rule that mandates
  the gate, and it is itself audited by the gate (checkbox 11 below). A contract that enforces
  C-19 via a gate block but omits RULE 11 (C-19) from the numbered list fails this criterion.
  PASS: RULE 11 (C-19) exists in this numbered list as a dedicated entry defining the gate.
  FAIL: C-19 is enforced only via the gate block; no RULE 11 (C-19) appears in the numbered list.

COMPLIANCE AUDIT -- 14 checkboxes, one per RULE (bijective invariant: 14 rules = 14 checkboxes):
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): this list contains exactly 14 rules covering C-09 through C-22, none outside
  [ ] RULE 10 (C-18): every RULE entry carries a C-NN label in its heading
  [ ] RULE 11 (C-19): this COMPLIANCE AUDIT block exists and has been reached before output
  [ ] RULE 12 (C-20): RULE 9 (C-17) above contains "Count = 14" and the range "C-09 through C-22"
  [ ] RULE 13 (C-21): gate below states "14/14 checked = valid output" before the FAIL condition
  [ ] RULE 14 (C-22): RULE 11 (C-19) exists as a dedicated numbered entry in this quality contract
14/14 checked = valid output. Any unchecked box = invalid output; do not proceed.
COMPLETENESS SEAL: 14 rules (C-09 through C-22), 14 checkboxes, bijective invariant confirmed.
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
