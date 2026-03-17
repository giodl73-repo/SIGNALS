---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 11
rubric: simulations/quest/rubrics/signal-rubric-v11-2026-03-17.md
---

# Quest Variate -- /signal (Round 11)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line
descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v11-2026-03-17.md`

---

## Context: what informed this round

R10 confirmed the independence of C-31 (labeled count formula), C-32 (named DOMAIN NOUN
TABLE), and C-33 (FULL gate Check 3 enumeration). All five R10 variations retroactively
score under v11 as follows: V-05 = 100.00, V-04 = 99.63, V-01/V-02/V-03 = 99.26. The
v11 rubric adds two new criteria extracted from R10 V-05:

- **C-34** (P axis): FULL MODE compliance gate includes section-format verification
  (Check 4). Closes the symmetry gap: FILTER had format check (C-29, R8), BARE had
  format check (C-18 Ch1, R4), FULL now has it too.
- **C-35** (Q axis): BARE MODE compliance gate includes canonical namespace emit-order
  check (Check 3). Closes the symmetry gap: FULL had order check (C-28/C-33, R8/R9),
  BARE now has it too; FILTER is N/A (single namespace, no ordering applies).

R11 goal: **confirm P and Q are independent, each contributing exactly +0.37.**

### Predicted scores

| Variation | C-34 (P) | C-35 (Q) | Asp (27) | Predicted |
|-----------|----------|----------|----------|-----------|
| V-01 (P only, -Q) | PASS | FAIL | 26/27 | **99.63** |
| V-02 (Q only, -P) | FAIL | PASS | 26/27 | **99.63** |
| V-03 (neither)    | FAIL | FAIL | 25/27 | **99.26** |
| V-04 (P+Q)        | PASS | PASS | 27/27 | **100.00** |
| V-05 (full golden) | PASS | PASS | 27/27 | **100.00** |

Independence confirmed if:
- V-01 - V-03 = +0.37 (P alone contributes)
- V-02 - V-03 = +0.37 (Q alone contributes)
- V-04 - V-01 = +0.37 (adding Q to P gives the same increment)
- V-04 - V-02 = +0.37 (adding P to Q gives the same increment)
- V-04 = V-05 = 100.00 (ceiling confirmed, axes are not overcounting)

All other R10 V-05 mechanisms are preserved across all five variations:
- Catalog-first ordering (C-17); active transcription gate with counted acknowledgment
  (C-22, C-23, C-26); labeled count formula in transcription gate + BARE Check 2 (C-31);
  named DOMAIN NOUN TABLE (C-32); FULL gate Check 3 enumerates all 12 namespaces (C-33);
  per-section count self-check (C-27); precomputed alignment table with example-pad (C-15,
  C-16); PARSE MODE enumerates all 12 canonical namespaces (C-19); slash-strip examples in
  BARE MODE (C-30); explicit BARE MODE anchors (C-21).

---

## V-01 -- Single-axis: FULL gate format check only (Axis P, no Q)

**Axis**: P only (C-34). FULL MODE compliance gate has Check 4 (section-format
verification). BARE MODE compliance gate has only 2 checks -- no order check (C-35
absent).
**Hypothesis**: P alone adds +0.37 over V-03. BARE gate missing Check 3 costs exactly
one criterion. Predicted 26/27 = 99.63.

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

Before emitting bare output, run both checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.

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

## V-02 -- Single-axis: BARE gate order check only (Axis Q, no P)

**Axis**: Q only (C-35). BARE MODE compliance gate has Check 3 (order check). FULL MODE
compliance gate has only 3 checks -- no section-format verification (C-34 absent).
**Hypothesis**: Q alone adds +0.37 over V-03. FULL gate missing Check 4 costs exactly
one criterion. Predicted 26/27 = 99.63.

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

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all three checks:
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

## V-03 -- Neither axis: no FULL gate format check, no BARE gate order check

**Axis**: Neither P nor Q. FULL MODE compliance gate has 3 checks (no format check).
BARE MODE compliance gate has 2 checks (no order check). This is the control baseline
showing what V-01 and V-02 each improve upon.
**Hypothesis**: Both C-34 and C-35 absent. Predicted 25/27 = 99.26. If both V-01 and
V-02 exceed this by exactly +0.37, independence is confirmed.

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

COMPLIANCE GATE -- FULL MODE

Before emitting FULL output, run all three checks:
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

COMPLIANCE GATE -- BARE MODE

Before emitting bare output, run both checks:
  Check 1 (format): Does any line contain anything other than a bare command name
    (no slash, no description, no header, no blank line)?
    If yes -- MODE: BARE format is violated. Restart.
  Check 2 (completeness): Does your output contain exactly 61 lines?
    (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +
     2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)
    If not -- a sub-skill is missing or duplicated. Restart.

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

## V-04 -- Combined-axis: both FULL gate format check and BARE gate order check (P+Q)

**Axis**: P+Q combined. FULL MODE compliance gate has all 4 checks (C-34 present). BARE
MODE compliance gate has all 3 checks (C-35 present). First variation with both new axes
present. Identical in criteria coverage to V-05.
**Hypothesis**: Both C-34 and C-35 present. Predicted 27/27 = 100.00. Confirms ceiling
and independence: V-04 - V-01 = +0.37 (Q added); V-04 - V-02 = +0.37 (P added).

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

## V-05 -- Full Integration: canonical golden baseline (R10 V-05 equivalent)

**Axis**: All 27 criteria present. This is the exact R10 V-05 text reproduced as the
canonical reference ceiling for v11. Identical in criteria to V-04; included as the
authoritative golden text.
**Hypothesis**: All criteria present. Predicted 27/27 = 100.00. V-05 = V-04 in score;
V-05 is the canonical golden prompt for v11.

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

## Axis Summary

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-34 | FULL gate Check 4 (section-format verification) | PASS | FAIL | FAIL | PASS | PASS |
| C-35 | BARE gate Check 3 (order check) | FAIL | PASS | FAIL | PASS | PASS |
| C-31 | Labeled count formula in transcription + BARE gates | PASS | PASS | PASS | PASS | PASS |
| C-32 | Named DOMAIN NOUN TABLE | PASS | PASS | PASS | PASS | PASS |
| C-33 | FULL gate Check 3 enumerates all 12 namespaces | PASS | PASS | PASS | PASS | PASS |
| **Predicted** | | **99.63** | **99.63** | **99.26** | **100.00** | **100.00** |

**Independence confirmation matrix:**

| Test | Formula | Expected | Confirms |
|------|---------|----------|---------|
| P alone | V-01 - V-03 | +0.37 | C-34 independent |
| Q alone | V-02 - V-03 | +0.37 | C-35 independent |
| P+Q | V-04 - V-03 | +0.74 | no interaction |
| Q added to P | V-04 - V-01 | +0.37 | Q independent of P |
| P added to Q | V-04 - V-02 | +0.37 | P independent of Q |

**Structural theme for R11**: *confirm mode symmetry gap closure is independent* -- C-34
(FULL format check) and C-35 (BARE order check) each close one side of the symmetry
matrix established in R8 and deepened in R9/R10. R11 verifies that each contributes
exactly one criterion-weight independently, with no interaction effect. If V-04 = V-05
= 100.00 and the increment from V-03 is +0.74 (= 2 x 0.37), the symmetry closure is
confirmed as two separable, non-interacting additions to the gate-check coverage matrix.
