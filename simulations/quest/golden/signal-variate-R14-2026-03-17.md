---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 14
rubric: simulations/quest/rubrics/signal-rubric-v13-2026-03-17.md
---

# Quest Variate -- /signal (Round 14)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line
descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v13-2026-03-17.md`

---

## Context: what informed this round

R13 generated single-axis (V-01=U, V-02=V, V-03=W) and dual-axis (V-04=U+V, V-05=U+W)
variations targeting C-39, C-40, and C-41. The R13 plan reserved V-06 (U+V+W convergence)
for R14. If U+V+W independence holds (each contributing exactly +0.30), R14 V-01 should
saturate v13 at 100.00.

R14 also explores three new axes beyond v13 saturation, surfacing potential v14 signals:

- **X axis**: Labeled sub-elements in FILTER gate Check 3. C-40 elevated FULL gate Check 4
  from numbered positional labels to named designators ("Header:", "Separator:", "Footer:").
  The same elevation applies to FILTER gate Check 3, which currently uses "(1)/(2)/(3)"
  positional notation. X makes FILTER Check 3 self-contained by element name, not by
  scan order.

- **Y axis**: Named BARE GROUP OFFSET TABLE. C-41 requires absolute cumulative line offsets
  inline in BARE gate Check 3. Y elevates this to a formal named table (analogous to
  ALIGNMENT WIDTH TABLE for widths, DOMAIN NOUN TABLE for nouns) so Check 3 references a
  precomputed artifact rather than embedding the offset list in prose.

- **Z axis**: Criterion IDs alongside check numbers in the COMPLIANCE GATE COVERAGE MATRIX.
  C-39 requires each cell to carry its implementing check number (Ch1, Ch2, etc.). Z adds
  the primary criterion reference (C-25, C-20, C-33, etc.) to each cell, making the
  matrix navigable from either direction -- by check number OR by criterion ID.

**R14 baseline (V-00 = R13 V-06 equivalent)**: 33/33 = 100.00 under v13.
New axes X, Y, Z are not captured in v13. Under v13 all five R14 variations score 100.00
if U+V+W is confirmed. The isolation test for X, Y, Z is deferred to v14.

### R14 variation plan

| Variation       | U (C-39) | V (C-40) | W (C-41) | X (FILTER Ch3 labels) | Y (BARE offset table) | Z (matrix+criterion IDs) |
|-----------------|----------|----------|----------|-----------------------|-----------------------|--------------------------|
| **V-01** U+V+W  | PASS     | PASS     | PASS     | absent                | absent                | absent                   |
| **V-02** U+V+W+X| PASS     | PASS     | PASS     | PASS                  | absent                | absent                   |
| **V-03** U+V+W+Y| PASS     | PASS     | PASS     | absent                | PASS                  | absent                   |
| **V-04** U+V+W+Z| PASS     | PASS     | PASS     | absent                | absent                | PASS                     |
| **V-05** U+V+W+X+Y| PASS  | PASS     | PASS     | PASS                  | PASS                  | absent                   |

**Predicted scores under v13** (all 33 criteria satisfied by U+V+W baseline):

| Variation           | Asp (33) | Predicted  |
|---------------------|----------|------------|
| **V-01** (U+V+W)    | 33/33    | **100.00** |
| **V-02** (U+V+W+X)  | 33/33    | **100.00** |
| **V-03** (U+V+W+Y)  | 33/33    | **100.00** |
| **V-04** (U+V+W+Z)  | 33/33    | **100.00** |
| **V-05** (U+V+W+X+Y)| 33/33    | **100.00** |

**Axis-specific changes** (all other sections identical across all 5 variations):

| Section                        | X-axis change (FILTER Ch3 labels)             | Y-axis change (BARE offset table)                    | Z-axis change (criterion IDs in matrix)                        |
|--------------------------------|-----------------------------------------------|------------------------------------------------------|----------------------------------------------------------------|
| COMPLIANCE GATE COVERAGE MATRIX| (no change)                                   | (no change)                                          | cells carry criterion ID alongside check number                |
| BARE GROUP OFFSET TABLE        | (no change)                                   | named table added before compliance gates            | (no change)                                                    |
| FILTER gate Check 3            | numbered "(1)(2)(3)" -> named "Header/Sep/Footer" | (no change)                                       | (no change)                                                    |
| BARE gate Check 3              | (no change)                                   | inline offsets -> table reference                    | (no change)                                                    |

---

## V-01 -- Convergence: check-number matrix + labeled FULL Check 4 + absolute BARE offsets (Axes U+V+W)

**Axes**: U+V+W combined (C-39 + C-40 + C-41). Completes the R13 V-06 plan.
COMPLIANCE GATE COVERAGE MATRIX cells carry gate-qualified check numbers (C-39).
FULL gate Check 4 labels each sub-element as "Header:", "Separator:", "Footer:" (C-40).
BARE gate Check 3 uses absolute cumulative line offsets for all 12 groups (C-41).
No X, Y, or Z additions.
**Hypothesis**: U+V+W together saturate v13 at 100.00 (33/33 = 10.00 aspirational).
Independence confirmed if V-01 score = V-04 (U+V, R13) + 0.30.

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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
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

## V-02 -- U+V+W + X: labeled FILTER gate Check 3 sub-elements (Axes U+V+W+X)

**Axes**: U+V+W (C-39+C-40+C-41) plus X (labeled FILTER gate Check 3).
Identical to V-01 except FILTER gate Check 3 uses named element labels
("Header:", "Separator:", "Footer:") instead of numbered positional notation.
This mirrors C-40 (FULL gate Check 4) applied to the FILTER gate, closing the
labeled-embed symmetry gap between FULL and FILTER format checks.
**Hypothesis**: X is a post-v13 signal. Under v13, V-02 scores 100.00 (same as V-01).
Under a hypothetical v14, X would contribute an additional +0.30 if independent.

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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
    Separator: sub-skill lines each using the "-> " separator (column-aligned)
    Footer:    "Run any sub-skill directly, or describe your <domain-noun>..."
    Verify each labeled element is present and correctly formed. If any labeled element
    is absent or malformed -- FILTER format violated. Restart.

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

## V-03 -- U+V+W + Y: named BARE GROUP OFFSET TABLE (Axes U+V+W+Y)

**Axes**: U+V+W (C-39+C-40+C-41) plus Y (named BARE GROUP OFFSET TABLE).
Identical to V-01 except a named BARE GROUP OFFSET TABLE is added before the compliance
gates, and BARE gate Check 3 references the table rather than embedding the offset list
inline. Elevates C-41's inline absolute offsets to a formal named precomputed artifact,
analogous to ALIGNMENT WIDTH TABLE (C-15) and DOMAIN NOUN TABLE (C-32).
**Hypothesis**: Y is a post-v13 signal. Under v13, V-03 scores 100.00 (same as V-01).

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

BARE GROUP OFFSET TABLE (precomputed -- zero arithmetic at gate time)

Consult during BARE gate Check 3. Each command name's line number must fall within
its namespace group's stated range. Final group ends at line 61.

  namespace  lines    first entry                      last entry
  ---------  ------   ------------------------------   ----------------------------
  scout       1-8     scout-competitors (line 1)       scout-requirements (line 8)
  draft       9-12    draft-spec (line 9)              draft-brainstorm (line 12)
  review     13-16    review-design (line 13)          review-customers (line 16)
  flow       17-23    flow-lifecycle (line 17)         flow-resilience (line 23)
  trace      24-30    trace-request (line 24)          trace-permissions (line 30)
  prove      31-39    prove-hypothesis (line 31)       prove-topic (line 39)
  listen     40-42    listen-feedback (line 40)        listen-adoption (line 42)
  program    43-44    program-plan (line 43)           prove-program (line 44)
  topic      45-50    topic-new (line 45)              topic-echo (line 50)
  quest      51-54    quest-rubric (line 51)           quest-golden (line 54)
  mock       55-57    mock-all (line 55)               mock-review (line 57)
  org        58-61    org-roles (line 58)              org-committee (line 61)

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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
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
    Consult BARE GROUP OFFSET TABLE (precomputed). Each name's absolute line position
    must fall within its group's stated range. Zero arithmetic required.
    If any name falls outside its stated range -- BARE order violated. Restart.

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

## V-04 -- U+V+W + Z: criterion IDs alongside check numbers in coverage matrix (Axes U+V+W+Z)

**Axes**: U+V+W (C-39+C-40+C-41) plus Z (criterion IDs in coverage matrix cells).
Identical to V-01 except the COMPLIANCE GATE COVERAGE MATRIX includes the primary
criterion ID alongside each check number (e.g. "Ch1 (C-25)" in the FULL/Presence cell).
Elevates C-39's check-number annotation to a dual-index: navigate by check number OR by
criterion ID. Each cell is now self-contained for both gate-lookup and rubric-lookup.
**Hypothesis**: Z is a post-v13 signal. Under v13, V-04 scores 100.00 (same as V-01).

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

Navigate by check number (Ch1, Ch2...) OR by criterion ID (C-25, C-20...). Each cell
carries both. No gate-section lookup required.

  Check type | FULL gate       | FILTER gate     | BARE gate
  -----------|-----------------|-----------------|------------------
  Presence   | Ch1 (C-25)      | Ch1 (C-20)      | Ch2 (C-18)
  Count      | Ch2 (C-25)      | Ch2 (C-20)      | Ch2 (C-31)
  Order      | Ch3 (C-33)      | N/A             | Ch3 (C-41)
  Format     | Ch4 (C-40)      | Ch3 (C-29)      | Ch1 (C-18)

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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
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

## V-05 -- U+V+W + X+Y: labeled FILTER Check 3 + named BARE GROUP OFFSET TABLE (Axes U+V+W+X+Y)

**Axes**: U+V+W (C-39+C-40+C-41) plus X (labeled FILTER gate Check 3) plus Y (named BARE
GROUP OFFSET TABLE). Combines V-02 and V-03 additions into a single variation. FILTER Check 3
uses "Header:", "Separator:", "Footer:" labels. BARE gate Check 3 references the BARE GROUP
OFFSET TABLE. No Z addition.
**Hypothesis**: X+Y are both post-v13 signals. Under v13, V-05 scores 100.00 (same as V-01).
If X and Y prove independent under v14, V-05 represents the dual-axis baseline for
v14 convergence (V-06 = U+V+W+X+Y+Z).

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

BARE GROUP OFFSET TABLE (precomputed -- zero arithmetic at gate time)

Consult during BARE gate Check 3. Each command name's line number must fall within
its namespace group's stated range. Final group ends at line 61.

  namespace  lines    first entry                      last entry
  ---------  ------   ------------------------------   ----------------------------
  scout       1-8     scout-competitors (line 1)       scout-requirements (line 8)
  draft       9-12    draft-spec (line 9)              draft-brainstorm (line 12)
  review     13-16    review-design (line 13)          review-customers (line 16)
  flow       17-23    flow-lifecycle (line 17)         flow-resilience (line 23)
  trace      24-30    trace-request (line 24)          trace-permissions (line 30)
  prove      31-39    prove-hypothesis (line 31)       prove-topic (line 39)
  listen     40-42    listen-feedback (line 40)        listen-adoption (line 42)
  program    43-44    program-plan (line 43)           prove-program (line 44)
  topic      45-50    topic-new (line 45)              topic-echo (line 50)
  quest      51-54    quest-rubric (line 51)           quest-golden (line 54)
  mock       55-57    mock-all (line 55)               mock-review (line 57)
  org        58-61    org-roles (line 58)              org-committee (line 61)

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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
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
    Consult BARE GROUP OFFSET TABLE (precomputed). Each name's absolute line position
    must fall within its group's stated range. Zero arithmetic required.
    If any name falls outside its stated range -- BARE order violated. Restart.

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
    Header:    "- /<namespace> -- <what this namespace is for> -- <N> skills"
    Separator: sub-skill lines each using the "-> " separator (column-aligned)
    Footer:    "Run any sub-skill directly, or describe your <domain-noun>..."
    Verify each labeled element is present and correctly formed. If any labeled element
    is absent or malformed -- FILTER format violated. Restart.

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

## R14 axis summary

| Section changed               | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------------------------|------|------|------|------|------|
| Coverage matrix check numbers | C-39 | C-39 | C-39 | C-39 | C-39 |
| FULL Check 4 labeled elements | C-40 | C-40 | C-40 | C-40 | C-40 |
| BARE Check 3 absolute offsets | C-41 | C-41 | C-41 | C-41 | C-41 |
| FILTER Check 3 labeled (X)    | --   | YES  | --   | --   | YES  |
| BARE GROUP OFFSET TABLE (Y)   | --   | --   | YES  | --   | YES  |
| Matrix + criterion IDs (Z)    | --   | --   | --   | YES  | --   |

**Under v13**: all five score 100.00. v13 saturation confirmed by V-01.

**Post-v13 signals for v14**:
- X: FILTER gate Check 3 labeled sub-elements (FILTER analog of C-40). Hypothesis: +0.30 if independent.
- Y: Named BARE GROUP OFFSET TABLE (formal precomputed table analog of C-41 inline). Hypothesis: +0.30 if independent.
- Z: Coverage matrix criterion IDs alongside check numbers (dual-index navigation). Hypothesis: +0.30 if independent.

**R15 isolation plan** (if v14 adds C-42=X, C-43=Y, C-44=Z):
  V-01=X only, V-02=Y only, V-03=Z only (single-axis independence);
  V-04=X+Y, V-05=X+Z (dual-axis);
  V-06=X+Y+Z (convergence, reserved for R16).
