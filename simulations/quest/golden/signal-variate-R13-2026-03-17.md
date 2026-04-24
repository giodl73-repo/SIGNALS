---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 13
rubric: simulations/quest/rubrics/signal-rubric-v13-2026-03-17.md
---

# Quest Variate -- /signal (Round 13)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line
descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v13-2026-03-17.md`

---

## Context: what informed this round

R12 confirmed the independence of C-36 (coverage matrix), C-37 (verbatim FULL Check 4 embed),
and C-38 (line-range BARE Check 3 notation). Under v12, R12 V-06 (R+S+T) saturates v12 at
100.00. The v13 rubric adds three new criteria derived from R12 signals:

- **C-39** (U axis): The COMPLIANCE GATE COVERAGE MATRIX cells must carry the implementing
  check number (e.g. "Ch1"). R12 matrices carry criterion IDs (C-25, C-34, etc.) but not gate-
  qualified check numbers. A reader must enter each gate section to find which check covers
  which dimension. C-39 requires the check number to be stated directly in the cell.

- **C-40** (V axis): FULL gate Check 4 verbatim embed must label each sub-element explicitly
  with a named designator ("Header:", "Separator:", "Footer:") rather than numbered positional
  labels ("(1)", "(2)", "(3)"). Numbered labels require positional counting to locate an
  element; named labels allow direct element-name lookup.

- **C-41** (W axis): BARE gate Check 3 must use absolute cumulative line offsets
  ("lines 1-8: scout-*", "lines 9-12: draft-*", ...) rather than relative incremental counts
  ("first 8 lines, next 4, ..."). Relative counts require running addition to verify any
  non-initial group; absolute offsets allow direct position lookup with zero arithmetic.

**R12 retroactive under v13:** R12 V-04/V-05 drop to 98.79. The R13 implicit baseline
(V-00 = R12 V-06 equivalent: all of C-01..C-38 passing) scores 30/33 = 99.09 under v13.
Each of C-39, C-40, C-41 contributes exactly 1/33 x 10 = 0.303 if independent.

**R13 isolation plan:** V-01=U, V-02=V, V-03=W (single-axis); V-04=U+V, V-05=U+W
(dual-axis). V-06=U+V+W (convergence, not generated here) should saturate v13 at 100.00
if all three axes are independent.

### Predicted scores under v13

| Variation         | C-39 | C-40 | C-41 | Asp (33) | Predicted  |
|-------------------|------|------|------|----------|------------|
| **V-01** (U only) | PASS | FAIL | FAIL | 31/33    | **99.39**  |
| **V-02** (V only) | FAIL | PASS | FAIL | 31/33    | **99.39**  |
| **V-03** (W only) | FAIL | FAIL | PASS | 31/33    | **99.39**  |
| **V-04** (U+V)    | PASS | PASS | FAIL | 32/33    | **99.70**  |
| **V-05** (U+W)    | PASS | FAIL | PASS | 32/33    | **99.70**  |

Independence check: V-04 - V-01 = +0.30 (V added); V-04 - V-02 = +0.30 (U added);
V-05 - V-01 = +0.30 (W added); V-05 - V-03 = +0.30 (U added). All deltas must equal
exactly +0.30 to confirm axis independence.

**Axis-specific changes** (all other sections identical across all 5 variations):

| Section                    | U-axis change (C-39)                         | V-axis change (C-40)                      | W-axis change (C-41)                        |
|----------------------------|----------------------------------------------|-------------------------------------------|---------------------------------------------|
| COVERAGE MATRIX cells      | criterion IDs -> gate-qualified check numbers| (no change)                               | (no change)                                 |
| FULL gate Check 4 labels   | (no change)                                  | numbered "(1)(2)(3)" -> named labels      | (no change)                                 |
| BARE gate Check 3 offsets  | (no change)                                  | (no change)                               | relative incremental -> absolute cumulative |

---

## V-01 -- Single-axis: check-number annotations in coverage matrix (Axis U, C-39 only)

**Axis**: U only (C-39). COMPLIANCE GATE COVERAGE MATRIX cells carry gate-qualified check
numbers (Ch1, Ch2, Ch3, Ch4). FULL gate Check 4 uses numbered positional labels (C-40 absent).
BARE gate Check 3 uses relative incremental line-range counts (C-41 absent).
**Hypothesis**: U alone adds +0.30 over the v13 baseline. Check-number annotation is the sole
addition. All 11 applicable cells annotated. Predicted 31/33 = 99.39.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
2 program + 6 topic + 4 quest + 3 mock + 4 org = 61). You will emit each entry
character-for-character. The catalog below IS the output for FULL and FILTER modes.
Do not paraphrase, condense, reorder, or reconstruct from memory. Any deviation from
the catalog text is an output failure, not an acceptable approximation.

- /scout -- Scout namespace -- 8 skills for discovery and research

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.

- /draft -- Draft namespace -- 4 skills for authoring design artifacts

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

- /review -- Review namespace -- 4 skills for design and code validation

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- Flow namespace -- 7 skills for domain process simulation

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

- /trace -- Trace namespace -- 7 skills for platform-level simulation

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- Prove namespace -- 9 skills for hypothesis-driven investigation

/prove-hypothesis   -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch    -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype    -> smallest-possible prototype with predicted vs actual results
/prove-analysis     -> data pattern analysis distinguishing correlation from causation
/prove-interview    -> persona-driven stakeholder interview simulation
/prove-synthesize   -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish      -> investigation write-up as paper with abstract and limitations
/prove-topic        -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- Listen namespace -- 3 skills for post-ship signal simulation

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- Program namespace -- 2 skills for orchestration and planning

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- Topic namespace -- 6 skills for narrative management

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- Quest namespace -- 4 skills for prompt engineering and golden prompt discovery

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- Mock namespace -- 3 skills for synthetic signal generation

/mock-all    -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns     -> mock artifact for a single namespace with category annotation
/mock-review -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- Org namespace -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER if <namespace> is a canonical namespace; FULL otherwise
  anything else        -> FULL

Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove,
listen, program, topic, quest, mock, org.
If the word after /signal is not in this list, emit FULL as if no argument was given.
Examples: /signal review-code -> FULL (sub-skill name is not a canonical namespace)
          /signal feature      -> FULL (arbitrary string is not a canonical namespace)

SECTION FORMAT (FULL and FILTER modes)

Each namespace section must follow this template exactly -- no deviations:

  - /<namespace> -- <what this namespace is for> -- <N> skills

  /<skill>  -> <one-line description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses the exact
domain noun from the DOMAIN NOUN TABLE. The skill count N must match the actual
number of sub-skills listed.

Per-section count self-check: before emitting the dispatch footer for each namespace
section, verify: the number of sub-skill lines above the footer equals the canonical
count for that namespace (scout=8, draft=4, review=4, flow=7, trace=7, prove=9,
listen=3, program=2, topic=6, quest=4, mock=3, org=4) AND equals the N stated in the
section header. If either count differs, restart the section from its header.

ALIGNMENT RULE

Within each namespace section, all `->` separators must form a single vertical column.
Use the ALIGNMENT WIDTH TABLE to determine padding. For each command name in a section:
  1. Look up the section's width in the table.
  2. Count the command name's characters.
  3. Add trailing spaces: (width - name_length) spaces, then 1 more space, then `->`.

ALIGNMENT WIDTH TABLE (precomputed -- do not recount)

  namespace  longest command name        width  example pad
  ---------  -------------------------  -----  -----------
  scout      /scout-stakeholders           19   /scout-naming (13) needs 7 spaces
  draft      /draft-brainstorm             17   /draft-spec (11) needs 7 spaces
  review     /review-customers             17   /review-code (12) needs 6 spaces
  flow       /flow-conversation            17   /flow-trigger (13) needs 5 spaces
  trace      /trace-permissions            18   /trace-state (12) needs 7 spaces
  prove      /prove-intelligence           19   /prove-topic (12) needs 8 spaces
  listen     /listen-feedback              16   /listen-support (15) needs 2 spaces
  program    /prove-program                14   /program-plan (13) needs 2 spaces
  topic      /topic-status                 13   /topic-new (10) needs 4 spaces
  quest      /quest-variate                14   /quest-score (12) needs 3 spaces
  mock       /mock-review                  12   /mock-all (9) needs 4 spaces
  org        /org-committee                14   /org-roles (10) needs 5 spaces

DOMAIN NOUN TABLE

Replace <DOMAIN-NOUN> in each footer with the exact noun listed here.
Do not use a generic placeholder. Do not omit the noun.

  scout    -> research goal
  draft    -> draft artifact
  review   -> artifact
  flow     -> process scenario
  trace    -> system
  prove    -> hypothesis
  listen   -> feature
  program  -> program
  topic    -> topic management need
  quest    -> optimization goal
  mock     -> coverage gap
  org      -> organizational need

COMPLIANCE GATE COVERAGE MATRIX

Navigate: (mode column) x (check-type row) -> implementing check number. No gate-section
lookup required. All 11 applicable cells carry gate-qualified check numbers.

  Check type | FULL gate | FILTER gate | BARE gate
  -----------|-----------|-------------|----------
  Presence   | Ch1       | Ch1         | Ch2
  Count      | Ch2       | Ch2         | Ch2
  Order      | Ch3       | N/A         | Ch3
  Format     | Ch4       | Ch3         | Ch1

  N/A: FILTER mode is single-namespace -- no multi-namespace sequence to verify.

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all four checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are namespace sections emitted in canonical order?
    Canonical order: scout, draft, review, flow, trace, prove, listen, program,
    topic, quest, mock, org. (First section: scout. Last section: org.)
    If any section appears out of canonical sequence -- order violated. Restart.
  Check 4 (format): Does each namespace section follow SECTION FORMAT?
    Required per section: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any section is missing a required element or has a malformed element --
    FULL format violated. Restart.

COMPLIANCE GATE -- BARE MODE

Before emitting bare output, run all three checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are names emitted in canonical namespace group order?
    Canonical sequence: first 8 lines are scout-* names, next 4 are draft-* names,
    next 4 are review-* names, next 7 are flow-* names, next 7 are trace-* names,
    next 9 are prove-* names, next 3 are listen-* names, next 2 are program entries,
    next 6 are topic-* names, next 4 are quest-* names, next 3 are mock-* names,
    last 4 are org-* names.
    If any name appears before its namespace group's turn -- BARE order violated. Restart.

COMPLIANCE GATE -- FILTER MODE

Before emitting filter output, run all three checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.
  Check 3 (format): Does the filter output follow SECTION FORMAT?
    Required elements: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any required element is absent or malformed -- FILTER output format violated. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.

Slash-strip transformation: catalog entries carry a leading `/`. Strip it.
  `/scout-competitors` becomes `scout-competitors`  (first entry)
  `/org-committee`     becomes `org-committee`      (last entry)
Remove only the leading `/`. No other characters change.
```

---

## V-02 -- Single-axis: labeled FULL gate Check 4 sub-elements (Axis V, C-40 only)

**Axis**: V only (C-40). FULL gate Check 4 verbatim embed explicitly labels each SECTION
FORMAT sub-element as "Header:", "Separator:", "Footer:". No check-number matrix (C-39 absent).
BARE gate Check 3 uses relative incremental line-range counts (C-41 absent).
**Hypothesis**: V alone adds +0.30 over the v13 baseline. Named sub-element labels in Check 4
are the sole addition. Predicted 31/33 = 99.39.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
2 program + 6 topic + 4 quest + 3 mock + 4 org = 61). You will emit each entry
character-for-character. The catalog below IS the output for FULL and FILTER modes.
Do not paraphrase, condense, reorder, or reconstruct from memory. Any deviation from
the catalog text is an output failure, not an acceptable approximation.

- /scout -- Scout namespace -- 8 skills for discovery and research

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.

- /draft -- Draft namespace -- 4 skills for authoring design artifacts

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

- /review -- Review namespace -- 4 skills for design and code validation

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- Flow namespace -- 7 skills for domain process simulation

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

- /trace -- Trace namespace -- 7 skills for platform-level simulation

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- Prove namespace -- 9 skills for hypothesis-driven investigation

/prove-hypothesis   -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch    -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype    -> smallest-possible prototype with predicted vs actual results
/prove-analysis     -> data pattern analysis distinguishing correlation from causation
/prove-interview    -> persona-driven stakeholder interview simulation
/prove-synthesize   -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish      -> investigation write-up as paper with abstract and limitations
/prove-topic        -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- Listen namespace -- 3 skills for post-ship signal simulation

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- Program namespace -- 2 skills for orchestration and planning

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- Topic namespace -- 6 skills for narrative management

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- Quest namespace -- 4 skills for prompt engineering and golden prompt discovery

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- Mock namespace -- 3 skills for synthetic signal generation

/mock-all    -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns     -> mock artifact for a single namespace with category annotation
/mock-review -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- Org namespace -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER if <namespace> is a canonical namespace; FULL otherwise
  anything else        -> FULL

Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove,
listen, program, topic, quest, mock, org.
If the word after /signal is not in this list, emit FULL as if no argument was given.
Examples: /signal review-code -> FULL (sub-skill name is not a canonical namespace)
          /signal feature      -> FULL (arbitrary string is not a canonical namespace)

SECTION FORMAT (FULL and FILTER modes)

Each namespace section must follow this template exactly -- no deviations:

  - /<namespace> -- <what this namespace is for> -- <N> skills

  /<skill>  -> <one-line description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses the exact
domain noun from the DOMAIN NOUN TABLE. The skill count N must match the actual
number of sub-skills listed.

Per-section count self-check: before emitting the dispatch footer for each namespace
section, verify: the number of sub-skill lines above the footer equals the canonical
count for that namespace (scout=8, draft=4, review=4, flow=7, trace=7, prove=9,
listen=3, program=2, topic=6, quest=4, mock=3, org=4) AND equals the N stated in the
section header. If either count differs, restart the section from its header.

ALIGNMENT RULE

Within each namespace section, all `->` separators must form a single vertical column.
Use the ALIGNMENT WIDTH TABLE to determine padding. For each command name in a section:
  1. Look up the section's width in the table.
  2. Count the command name's characters.
  3. Add trailing spaces: (width - name_length) spaces, then 1 more space, then `->`.

ALIGNMENT WIDTH TABLE (precomputed -- do not recount)

  namespace  longest command name        width  example pad
  ---------  -------------------------  -----  -----------
  scout      /scout-stakeholders           19   /scout-naming (13) needs 7 spaces
  draft      /draft-brainstorm             17   /draft-spec (11) needs 7 spaces
  review     /review-customers             17   /review-code (12) needs 6 spaces
  flow       /flow-conversation            17   /flow-trigger (13) needs 5 spaces
  trace      /trace-permissions            18   /trace-state (12) needs 7 spaces
  prove      /prove-intelligence           19   /prove-topic (12) needs 8 spaces
  listen     /listen-feedback              16   /listen-support (15) needs 2 spaces
  program    /prove-program                14   /program-plan (13) needs 2 spaces
  topic      /topic-status                 13   /topic-new (10) needs 4 spaces
  quest      /quest-variate                14   /quest-score (12) needs 3 spaces
  mock       /mock-review                  12   /mock-all (9) needs 4 spaces
  org        /org-committee                14   /org-roles (10) needs 5 spaces

DOMAIN NOUN TABLE

Replace <DOMAIN-NOUN> in each footer with the exact noun listed here.
Do not use a generic placeholder. Do not omit the noun.

  scout    -> research goal
  draft    -> draft artifact
  review   -> artifact
  flow     -> process scenario
  trace    -> system
  prove    -> hypothesis
  listen   -> feature
  program  -> program
  topic    -> topic management need
  quest    -> optimization goal
  mock     -> coverage gap
  org      -> organizational need

COMPLIANCE GATE COVERAGE MATRIX

Maps which criterion governs each check-type dimension in each output mode.
Consult before emitting to verify all dimensions are covered.

  Check type | FULL      | FILTER    | BARE
  -----------|-----------|-----------|-------------
  Presence   | C-25      | C-20      | C-18
  Count      | C-25      | C-20      | C-18/C-31
  Order      | C-28/C-33 | N/A       | C-35/C-38
  Format     | C-34      | C-29      | C-18

  N/A: FILTER mode is single-namespace -- no multi-namespace sequence to verify.

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all four checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are namespace sections emitted in canonical order?
    Canonical order: scout, draft, review, flow, trace, prove, listen, program,
    topic, quest, mock, org. (First section: scout. Last section: org.)
    If any section appears out of canonical sequence -- order violated. Restart.
  Check 4 (format): Does each namespace section follow SECTION FORMAT?
    Required per section:
      Header:    "- /<namespace> -- <purpose> -- <N> skills"
      Separator: sub-skill lines each using the "-> " separator (column-aligned)
      Footer:    "Run any sub-skill directly, or describe your <domain-noun>..."
    Verify each labeled element is present and correctly formed. If any labeled element
    is absent or malformed -- FULL format violated. Restart.

COMPLIANCE GATE -- BARE MODE

Before emitting bare output, run all three checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are names emitted in canonical namespace group order?
    Canonical sequence: first 8 lines are scout-* names, next 4 are draft-* names,
    next 4 are review-* names, next 7 are flow-* names, next 7 are trace-* names,
    next 9 are prove-* names, next 3 are listen-* names, next 2 are program entries,
    next 6 are topic-* names, next 4 are quest-* names, next 3 are mock-* names,
    last 4 are org-* names.
    If any name appears before its namespace group's turn -- BARE order violated. Restart.

COMPLIANCE GATE -- FILTER MODE

Before emitting filter output, run all three checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.
  Check 3 (format): Does the filter output follow SECTION FORMAT?
    Required elements: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any required element is absent or malformed -- FILTER output format violated. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.

Slash-strip transformation: catalog entries carry a leading `/`. Strip it.
  `/scout-competitors` becomes `scout-competitors`  (first entry)
  `/org-committee`     becomes `org-committee`      (last entry)
Remove only the leading `/`. No other characters change.
```

---

## V-03 -- Single-axis: absolute cumulative offsets in BARE gate Check 3 (Axis W, C-41 only)

**Axis**: W only (C-41). BARE gate Check 3 uses absolute cumulative line offsets for all 12
namespace groups (lines 1-8, 9-12, 13-16...). No check-number matrix (C-39 absent). FULL gate
Check 4 uses numbered positional labels (C-40 absent).
**Hypothesis**: W alone adds +0.30 over the v13 baseline. Absolute offsets in BARE Check 3 are
the sole addition. Zero arithmetic at gate time. Predicted 31/33 = 99.39.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
2 program + 6 topic + 4 quest + 3 mock + 4 org = 61). You will emit each entry
character-for-character. The catalog below IS the output for FULL and FILTER modes.
Do not paraphrase, condense, reorder, or reconstruct from memory. Any deviation from
the catalog text is an output failure, not an acceptable approximation.

- /scout -- Scout namespace -- 8 skills for discovery and research

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.

- /draft -- Draft namespace -- 4 skills for authoring design artifacts

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

- /review -- Review namespace -- 4 skills for design and code validation

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- Flow namespace -- 7 skills for domain process simulation

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

- /trace -- Trace namespace -- 7 skills for platform-level simulation

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- Prove namespace -- 9 skills for hypothesis-driven investigation

/prove-hypothesis   -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch    -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype    -> smallest-possible prototype with predicted vs actual results
/prove-analysis     -> data pattern analysis distinguishing correlation from causation
/prove-interview    -> persona-driven stakeholder interview simulation
/prove-synthesize   -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish      -> investigation write-up as paper with abstract and limitations
/prove-topic        -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- Listen namespace -- 3 skills for post-ship signal simulation

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- Program namespace -- 2 skills for orchestration and planning

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- Topic namespace -- 6 skills for narrative management

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- Quest namespace -- 4 skills for prompt engineering and golden prompt discovery

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- Mock namespace -- 3 skills for synthetic signal generation

/mock-all    -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns     -> mock artifact for a single namespace with category annotation
/mock-review -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- Org namespace -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER if <namespace> is a canonical namespace; FULL otherwise
  anything else        -> FULL

Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove,
listen, program, topic, quest, mock, org.
If the word after /signal is not in this list, emit FULL as if no argument was given.
Examples: /signal review-code -> FULL (sub-skill name is not a canonical namespace)
          /signal feature      -> FULL (arbitrary string is not a canonical namespace)

SECTION FORMAT (FULL and FILTER modes)

Each namespace section must follow this template exactly -- no deviations:

  - /<namespace> -- <what this namespace is for> -- <N> skills

  /<skill>  -> <one-line description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses the exact
domain noun from the DOMAIN NOUN TABLE. The skill count N must match the actual
number of sub-skills listed.

Per-section count self-check: before emitting the dispatch footer for each namespace
section, verify: the number of sub-skill lines above the footer equals the canonical
count for that namespace (scout=8, draft=4, review=4, flow=7, trace=7, prove=9,
listen=3, program=2, topic=6, quest=4, mock=3, org=4) AND equals the N stated in the
section header. If either count differs, restart the section from its header.

ALIGNMENT RULE

Within each namespace section, all `->` separators must form a single vertical column.
Use the ALIGNMENT WIDTH TABLE to determine padding. For each command name in a section:
  1. Look up the section's width in the table.
  2. Count the command name's characters.
  3. Add trailing spaces: (width - name_length) spaces, then 1 more space, then `->`.

ALIGNMENT WIDTH TABLE (precomputed -- do not recount)

  namespace  longest command name        width  example pad
  ---------  -------------------------  -----  -----------
  scout      /scout-stakeholders           19   /scout-naming (13) needs 7 spaces
  draft      /draft-brainstorm             17   /draft-spec (11) needs 7 spaces
  review     /review-customers             17   /review-code (12) needs 6 spaces
  flow       /flow-conversation            17   /flow-trigger (13) needs 5 spaces
  trace      /trace-permissions            18   /trace-state (12) needs 7 spaces
  prove      /prove-intelligence           19   /prove-topic (12) needs 8 spaces
  listen     /listen-feedback              16   /listen-support (15) needs 2 spaces
  program    /prove-program                14   /program-plan (13) needs 2 spaces
  topic      /topic-status                 13   /topic-new (10) needs 4 spaces
  quest      /quest-variate                14   /quest-score (12) needs 3 spaces
  mock       /mock-review                  12   /mock-all (9) needs 4 spaces
  org        /org-committee                14   /org-roles (10) needs 5 spaces

DOMAIN NOUN TABLE

Replace <DOMAIN-NOUN> in each footer with the exact noun listed here.
Do not use a generic placeholder. Do not omit the noun.

  scout    -> research goal
  draft    -> draft artifact
  review   -> artifact
  flow     -> process scenario
  trace    -> system
  prove    -> hypothesis
  listen   -> feature
  program  -> program
  topic    -> topic management need
  quest    -> optimization goal
  mock     -> coverage gap
  org      -> organizational need

COMPLIANCE GATE COVERAGE MATRIX

Maps which criterion governs each check-type dimension in each output mode.
Consult before emitting to verify all dimensions are covered.

  Check type | FULL      | FILTER    | BARE
  -----------|-----------|-----------|-------------
  Presence   | C-25      | C-20      | C-18
  Count      | C-25      | C-20      | C-18/C-31
  Order      | C-28/C-33 | N/A       | C-35/C-38
  Format     | C-34      | C-29      | C-18

  N/A: FILTER mode is single-namespace -- no multi-namespace sequence to verify.

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all four checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are namespace sections emitted in canonical order?
    Canonical order: scout, draft, review, flow, trace, prove, listen, program,
    topic, quest, mock, org. (First section: scout. Last section: org.)
    If any section appears out of canonical sequence -- order violated. Restart.
  Check 4 (format): Does each namespace section follow SECTION FORMAT?
    Required per section: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any section is missing a required element or has a malformed element --
    FULL format violated. Restart.

COMPLIANCE GATE -- BARE MODE

Before emitting bare output, run all three checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are names emitted in canonical namespace group order?
    Absolute line positions (precomputed -- zero arithmetic required):
      lines  1- 8: scout-* names
      lines  9-12: draft-* names
      lines 13-16: review-* names
      lines 17-23: flow-* names
      lines 24-30: trace-* names
      lines 31-39: prove-* names
      lines 40-42: listen-* names
      lines 43-44: program entries
      lines 45-50: topic-* names
      lines 51-54: quest-* names
      lines 55-57: mock-* names
      lines 58-61: org-* names
    Verify each line's absolute index falls within its group's precomputed range.
    If any name falls outside its range -- BARE order violated. Restart.

COMPLIANCE GATE -- FILTER MODE

Before emitting filter output, run all three checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.
  Check 3 (format): Does the filter output follow SECTION FORMAT?
    Required elements: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any required element is absent or malformed -- FILTER output format violated. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.

Slash-strip transformation: catalog entries carry a leading `/`. Strip it.
  `/scout-competitors` becomes `scout-competitors`  (first entry)
  `/org-committee`     becomes `org-committee`      (last entry)
Remove only the leading `/`. No other characters change.
```

---

## V-04 -- Dual-axis: check-number matrix + labeled Check 4 (Axes U+V, C-39+C-40)

**Axis**: U+V combined (C-39 + C-40). COVERAGE MATRIX cells carry gate-qualified check numbers.
FULL gate Check 4 uses "Header:", "Separator:", "Footer:" labels. BARE gate Check 3 uses
relative incremental counts (C-41 absent).
**Hypothesis**: U+V add +0.61 over the v13 baseline, +0.30 over V-01 (V added), +0.30 over
V-02 (U added). Predicted 32/33 = 99.70.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
2 program + 6 topic + 4 quest + 3 mock + 4 org = 61). You will emit each entry
character-for-character. The catalog below IS the output for FULL and FILTER modes.
Do not paraphrase, condense, reorder, or reconstruct from memory. Any deviation from
the catalog text is an output failure, not an acceptable approximation.

- /scout -- Scout namespace -- 8 skills for discovery and research

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.

- /draft -- Draft namespace -- 4 skills for authoring design artifacts

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

- /review -- Review namespace -- 4 skills for design and code validation

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- Flow namespace -- 7 skills for domain process simulation

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

- /trace -- Trace namespace -- 7 skills for platform-level simulation

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- Prove namespace -- 9 skills for hypothesis-driven investigation

/prove-hypothesis   -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch    -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype    -> smallest-possible prototype with predicted vs actual results
/prove-analysis     -> data pattern analysis distinguishing correlation from causation
/prove-interview    -> persona-driven stakeholder interview simulation
/prove-synthesize   -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish      -> investigation write-up as paper with abstract and limitations
/prove-topic        -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- Listen namespace -- 3 skills for post-ship signal simulation

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- Program namespace -- 2 skills for orchestration and planning

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- Topic namespace -- 6 skills for narrative management

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- Quest namespace -- 4 skills for prompt engineering and golden prompt discovery

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- Mock namespace -- 3 skills for synthetic signal generation

/mock-all    -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns     -> mock artifact for a single namespace with category annotation
/mock-review -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- Org namespace -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER if <namespace> is a canonical namespace; FULL otherwise
  anything else        -> FULL

Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove,
listen, program, topic, quest, mock, org.
If the word after /signal is not in this list, emit FULL as if no argument was given.
Examples: /signal review-code -> FULL (sub-skill name is not a canonical namespace)
          /signal feature      -> FULL (arbitrary string is not a canonical namespace)

SECTION FORMAT (FULL and FILTER modes)

Each namespace section must follow this template exactly -- no deviations:

  - /<namespace> -- <what this namespace is for> -- <N> skills

  /<skill>  -> <one-line description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses the exact
domain noun from the DOMAIN NOUN TABLE. The skill count N must match the actual
number of sub-skills listed.

Per-section count self-check: before emitting the dispatch footer for each namespace
section, verify: the number of sub-skill lines above the footer equals the canonical
count for that namespace (scout=8, draft=4, review=4, flow=7, trace=7, prove=9,
listen=3, program=2, topic=6, quest=4, mock=3, org=4) AND equals the N stated in the
section header. If either count differs, restart the section from its header.

ALIGNMENT RULE

Within each namespace section, all `->` separators must form a single vertical column.
Use the ALIGNMENT WIDTH TABLE to determine padding. For each command name in a section:
  1. Look up the section's width in the table.
  2. Count the command name's characters.
  3. Add trailing spaces: (width - name_length) spaces, then 1 more space, then `->`.

ALIGNMENT WIDTH TABLE (precomputed -- do not recount)

  namespace  longest command name        width  example pad
  ---------  -------------------------  -----  -----------
  scout      /scout-stakeholders           19   /scout-naming (13) needs 7 spaces
  draft      /draft-brainstorm             17   /draft-spec (11) needs 7 spaces
  review     /review-customers             17   /review-code (12) needs 6 spaces
  flow       /flow-conversation            17   /flow-trigger (13) needs 5 spaces
  trace      /trace-permissions            18   /trace-state (12) needs 7 spaces
  prove      /prove-intelligence           19   /prove-topic (12) needs 8 spaces
  listen     /listen-feedback              16   /listen-support (15) needs 2 spaces
  program    /prove-program                14   /program-plan (13) needs 2 spaces
  topic      /topic-status                 13   /topic-new (10) needs 4 spaces
  quest      /quest-variate                14   /quest-score (12) needs 3 spaces
  mock       /mock-review                  12   /mock-all (9) needs 4 spaces
  org        /org-committee                14   /org-roles (10) needs 5 spaces

DOMAIN NOUN TABLE

Replace <DOMAIN-NOUN> in each footer with the exact noun listed here.
Do not use a generic placeholder. Do not omit the noun.

  scout    -> research goal
  draft    -> draft artifact
  review   -> artifact
  flow     -> process scenario
  trace    -> system
  prove    -> hypothesis
  listen   -> feature
  program  -> program
  topic    -> topic management need
  quest    -> optimization goal
  mock     -> coverage gap
  org      -> organizational need

COMPLIANCE GATE COVERAGE MATRIX

Navigate: (mode column) x (check-type row) -> implementing check number. No gate-section
lookup required. All 11 applicable cells carry gate-qualified check numbers.

  Check type | FULL gate | FILTER gate | BARE gate
  -----------|-----------|-------------|----------
  Presence   | Ch1       | Ch1         | Ch2
  Count      | Ch2       | Ch2         | Ch2
  Order      | Ch3       | N/A         | Ch3
  Format     | Ch4       | Ch3         | Ch1

  N/A: FILTER mode is single-namespace -- no multi-namespace sequence to verify.

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all four checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are namespace sections emitted in canonical order?
    Canonical order: scout, draft, review, flow, trace, prove, listen, program,
    topic, quest, mock, org. (First section: scout. Last section: org.)
    If any section appears out of canonical sequence -- order violated. Restart.
  Check 4 (format): Does each namespace section follow SECTION FORMAT?
    Required per section:
      Header:    "- /<namespace> -- <purpose> -- <N> skills"
      Separator: sub-skill lines each using the "-> " separator (column-aligned)
      Footer:    "Run any sub-skill directly, or describe your <domain-noun>..."
    Verify each labeled element is present and correctly formed. If any labeled element
    is absent or malformed -- FULL format violated. Restart.

COMPLIANCE GATE -- BARE MODE

Before emitting bare output, run all three checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are names emitted in canonical namespace group order?
    Canonical sequence: first 8 lines are scout-* names, next 4 are draft-* names,
    next 4 are review-* names, next 7 are flow-* names, next 7 are trace-* names,
    next 9 are prove-* names, next 3 are listen-* names, next 2 are program entries,
    next 6 are topic-* names, next 4 are quest-* names, next 3 are mock-* names,
    last 4 are org-* names.
    If any name appears before its namespace group's turn -- BARE order violated. Restart.

COMPLIANCE GATE -- FILTER MODE

Before emitting filter output, run all three checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.
  Check 3 (format): Does the filter output follow SECTION FORMAT?
    Required elements: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any required element is absent or malformed -- FILTER output format violated. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.

Slash-strip transformation: catalog entries carry a leading `/`. Strip it.
  `/scout-competitors` becomes `scout-competitors`  (first entry)
  `/org-committee`     becomes `org-committee`      (last entry)
Remove only the leading `/`. No other characters change.
```

---

## V-05 -- Dual-axis: check-number matrix + absolute BARE offsets (Axes U+W, C-39+C-41)

**Axis**: U+W combined (C-39 + C-41). COVERAGE MATRIX cells carry gate-qualified check numbers.
BARE gate Check 3 uses absolute cumulative line offsets. FULL gate Check 4 uses numbered
positional labels (C-40 absent).
**Hypothesis**: U+W add +0.61 over the v13 baseline, +0.30 over V-01 (W added), +0.30 over
V-03 (U added). Predicted 32/33 = 99.70.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
2 program + 6 topic + 4 quest + 3 mock + 4 org = 61). You will emit each entry
character-for-character. The catalog below IS the output for FULL and FILTER modes.
Do not paraphrase, condense, reorder, or reconstruct from memory. Any deviation from
the catalog text is an output failure, not an acceptable approximation.

- /scout -- Scout namespace -- 8 skills for discovery and research

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.

- /draft -- Draft namespace -- 4 skills for authoring design artifacts

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

- /review -- Review namespace -- 4 skills for design and code validation

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- Flow namespace -- 7 skills for domain process simulation

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

- /trace -- Trace namespace -- 7 skills for platform-level simulation

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- Prove namespace -- 9 skills for hypothesis-driven investigation

/prove-hypothesis   -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch    -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype    -> smallest-possible prototype with predicted vs actual results
/prove-analysis     -> data pattern analysis distinguishing correlation from causation
/prove-interview    -> persona-driven stakeholder interview simulation
/prove-synthesize   -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish      -> investigation write-up as paper with abstract and limitations
/prove-topic        -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- Listen namespace -- 3 skills for post-ship signal simulation

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- Program namespace -- 2 skills for orchestration and planning

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- Topic namespace -- 6 skills for narrative management

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- Quest namespace -- 4 skills for prompt engineering and golden prompt discovery

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- Mock namespace -- 3 skills for synthetic signal generation

/mock-all    -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns     -> mock artifact for a single namespace with category annotation
/mock-review -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- Org namespace -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER if <namespace> is a canonical namespace; FULL otherwise
  anything else        -> FULL

Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove,
listen, program, topic, quest, mock, org.
If the word after /signal is not in this list, emit FULL as if no argument was given.
Examples: /signal review-code -> FULL (sub-skill name is not a canonical namespace)
          /signal feature      -> FULL (arbitrary string is not a canonical namespace)

SECTION FORMAT (FULL and FILTER modes)

Each namespace section must follow this template exactly -- no deviations:

  - /<namespace> -- <what this namespace is for> -- <N> skills

  /<skill>  -> <one-line description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses the exact
domain noun from the DOMAIN NOUN TABLE. The skill count N must match the actual
number of sub-skills listed.

Per-section count self-check: before emitting the dispatch footer for each namespace
section, verify: the number of sub-skill lines above the footer equals the canonical
count for that namespace (scout=8, draft=4, review=4, flow=7, trace=7, prove=9,
listen=3, program=2, topic=6, quest=4, mock=3, org=4) AND equals the N stated in the
section header. If either count differs, restart the section from its header.

ALIGNMENT RULE

Within each namespace section, all `->` separators must form a single vertical column.
Use the ALIGNMENT WIDTH TABLE to determine padding. For each command name in a section:
  1. Look up the section's width in the table.
  2. Count the command name's characters.
  3. Add trailing spaces: (width - name_length) spaces, then 1 more space, then `->`.

ALIGNMENT WIDTH TABLE (precomputed -- do not recount)

  namespace  longest command name        width  example pad
  ---------  -------------------------  -----  -----------
  scout      /scout-stakeholders           19   /scout-naming (13) needs 7 spaces
  draft      /draft-brainstorm             17   /draft-spec (11) needs 7 spaces
  review     /review-customers             17   /review-code (12) needs 6 spaces
  flow       /flow-conversation            17   /flow-trigger (13) needs 5 spaces
  trace      /trace-permissions            18   /trace-state (12) needs 7 spaces
  prove      /prove-intelligence           19   /prove-topic (12) needs 8 spaces
  listen     /listen-feedback              16   /listen-support (15) needs 2 spaces
  program    /prove-program                14   /program-plan (13) needs 2 spaces
  topic      /topic-status                 13   /topic-new (10) needs 4 spaces
  quest      /quest-variate                14   /quest-score (12) needs 3 spaces
  mock       /mock-review                  12   /mock-all (9) needs 4 spaces
  org        /org-committee                14   /org-roles (10) needs 5 spaces

DOMAIN NOUN TABLE

Replace <DOMAIN-NOUN> in each footer with the exact noun listed here.
Do not use a generic placeholder. Do not omit the noun.

  scout    -> research goal
  draft    -> draft artifact
  review   -> artifact
  flow     -> process scenario
  trace    -> system
  prove    -> hypothesis
  listen   -> feature
  program  -> program
  topic    -> topic management need
  quest    -> optimization goal
  mock     -> coverage gap
  org      -> organizational need

COMPLIANCE GATE COVERAGE MATRIX

Navigate: (mode column) x (check-type row) -> implementing check number. No gate-section
lookup required. All 11 applicable cells carry gate-qualified check numbers.

  Check type | FULL gate | FILTER gate | BARE gate
  -----------|-----------|-------------|----------
  Presence   | Ch1       | Ch1         | Ch2
  Count      | Ch2       | Ch2         | Ch2
  Order      | Ch3       | N/A         | Ch3
  Format     | Ch4       | Ch3         | Ch1

  N/A: FILTER mode is single-namespace -- no multi-namespace sequence to verify.

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all four checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are namespace sections emitted in canonical order?
    Canonical order: scout, draft, review, flow, trace, prove, listen, program,
    topic, quest, mock, org. (First section: scout. Last section: org.)
    If any section appears out of canonical sequence -- order violated. Restart.
  Check 4 (format): Does each namespace section follow SECTION FORMAT?
    Required per section: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any section is missing a required element or has a malformed element --
    FULL format violated. Restart.

COMPLIANCE GATE -- BARE MODE

Before emitting bare output, run all three checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.
  Check 3 (order): Are names emitted in canonical namespace group order?
    Absolute line positions (precomputed -- zero arithmetic required):
      lines  1- 8: scout-* names
      lines  9-12: draft-* names
      lines 13-16: review-* names
      lines 17-23: flow-* names
      lines 24-30: trace-* names
      lines 31-39: prove-* names
      lines 40-42: listen-* names
      lines 43-44: program entries
      lines 45-50: topic-* names
      lines 51-54: quest-* names
      lines 55-57: mock-* names
      lines 58-61: org-* names
    Verify each line's absolute index falls within its group's precomputed range.
    If any name falls outside its range -- BARE order violated. Restart.

COMPLIANCE GATE -- FILTER MODE

Before emitting filter output, run all three checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.
  Check 3 (format): Does the filter output follow SECTION FORMAT?
    Required elements: (1) a header line in the form "- /<namespace> -- <purpose> --
    <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
    footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
    If any required element is absent or malformed -- FILTER output format violated. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.

Slash-strip transformation: catalog entries carry a leading `/`. Strip it.
  `/scout-competitors` becomes `scout-competitors`  (first entry)
  `/org-committee`     becomes `org-committee`      (last entry)
Remove only the leading `/`. No other characters change.
```

---

## Variation diff summary

| Section                         | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------------------------------|------|------|------|------|------|
| Matrix: gate-qualified Ch# cells| YES  | NO   | NO   | YES  | YES  |
| Check 4: Header/Separator/Footer| NO   | YES  | NO   | YES  | NO   |
| Check 3: absolute offsets       | NO   | NO   | YES  | NO   | YES  |
| C-39 target                     | PASS | FAIL | FAIL | PASS | PASS |
| C-40 target                     | FAIL | PASS | FAIL | PASS | FAIL |
| C-41 target                     | FAIL | FAIL | PASS | FAIL | PASS |
| Predicted composite             | 99.39| 99.39| 99.39| 99.70| 99.70|

Independence confirmation (if scores match predictions):
- V-04 - V-01 = +0.30 confirms V axis independent of U
- V-04 - V-02 = +0.30 confirms U axis independent of V
- V-05 - V-01 = +0.30 confirms W axis independent of U
- V-05 - V-03 = +0.30 confirms U axis independent of W
- V-06 (U+V+W, not generated) should = 99.09 + 3x0.303 = 100.00
