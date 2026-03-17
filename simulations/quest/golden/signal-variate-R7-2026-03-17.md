---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 7
rubric: simulations/quest/rubrics/signal-rubric-v7-2026-03-17.md
---

# Quest Variate -- /signal (Round 7)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line
descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v7-2026-03-17.md`

---

## Context: what informed this round

R6 V-05 achieved 100.00 under v7: all 16/16 aspirational criteria pass. The v7 rubric
introduced C-23 (catalog-as-output labeling) and C-24 (symmetric mode completeness --
all three emission paths explicitly verified). Both were already present in R6 V-05,
confirming V-05 as the new universal baseline.

Under v7 the leaderboard is:

| Rank | V | C-23 | C-24 | Aspirational | Composite |
|------|---|------|------|--------------|-----------|
| 1 | **V-05** | PASS | PASS | 16/16 -> 10 | **100.00** |
| 2 | V-03 | PASS | PARTIAL | 14/16 -> 8.75 | **98.75** |
| 3 | V-04 | FAIL | PARTIAL | 13/16 -> 8.13 | **98.13** |
| 4 (tie) | V-01 | FAIL | PARTIAL | 12/16 -> 7.50 | **97.50** |
| 4 (tie) | V-02 | FAIL | FAIL | 12/16 -> 7.50 | **97.50** |

R7 goal: **excellence-signal discovery beyond the current ceiling.** The rubric is
complete for everything we have proven so far. The question is: what failure modes
remain that V-05 does not address? Three candidate axes identified from structural
analysis of V-05:

- **Axis G**: The transcription gate (C-22/C-23) is a commitment statement, not a
  structured restart gate. BARE mode has a restart gate (C-18) and FILTER mode has
  one (C-20). FULL mode has only the transcription pledge. Adding an explicit
  COMPLIANCE GATE -- FULL MODE with namespace-presence and per-namespace count checks
  would create fully symmetric restart coverage across all three emission paths.
  This is distinct from C-24 (which tests for coverage of all three paths) and C-22
  (which tests for the commitment mechanism): a variation can pass C-22 and C-24
  while having no restart trigger for FULL mode.

- **Axis H**: The transcription gate says "confirm you have read every entry" but
  does not require an explicit 61-entry count verification. C-18 extended C-14's
  restart gate with an exact count; C-26 (predicted) would extend C-22's commitment
  with the same upgrade: "confirm you have read all 61 entries (8+4+4+7+7+9+3+
  2+6+4+3+4=61)." Reading and counting are different operations; the count closes
  the gap between implicit comprehension and explicit verification.

- **Axis I**: SECTION FORMAT specifies a template but does not instruct the model
  to self-check that the number of sub-skills emitted matches the canonical count
  before closing each section. C-06 tests header accuracy in output; C-18/C-20 test
  completeness via document-level restart gates. A per-section count self-check in
  SECTION FORMAT would catch a model that emits a correct header (N=7) but silently
  emits 6 sub-skills. This operates at section granularity, not document granularity.

All five R7 variations carry the full R6 V-05 mechanism set:
- Catalog-first ordering (C-17)
- Active transcription commitment gate with "IS the output" labeling (C-22 + C-23)
- Bare-mode count gate with per-namespace breakdown (C-18)
- Canonical-namespace guard enumerating all 12 names (C-19)
- Both compliance gates with restart triggers (C-14)
- Filter-mode count gate (C-20)
- Bare order anchors: Begin with scout-competitors, End with org-committee (C-21)
- Symmetric mode completeness -- all three paths verified (C-24)
- Precomputed width table (C-15)
- Per-row example-pad derivation (C-16)
- Domain noun table (C-11)
- Format consistency (C-13)
- Accurate skill counts (C-06)
- Dispatch footers (C-07)
- Column alignment (C-12)

---

## SPREAD-DESIGN PLAN

| Variation | Axis | Source Signal | Target Criteria | Predicted |
|-----------|------|--------------|-----------------|-----------|
| V-01 | Axis G single: COMPLIANCE GATE -- FULL MODE | Structural gap: BARE+FILTER have restart gates; FULL has only a commitment pledge. Add explicit namespace-presence + per-namespace-count restart gate for FULL mode. | C-25 (predicted) | 100.00 |
| V-02 | Axis H single: Transcription gate entry-count confirmation | C-18 pattern applied to transcription gate: "confirm you have read all 61 entries (8+4+...=61)." Count verification before pledging, not just acknowledgment. | C-26 (predicted) | 100.00 |
| V-03 | Axis I single: Per-section count self-check in SECTION FORMAT | Before closing each namespace section, verify sub-skill count matches header N and canonical count. Section-level gate vs. document-level gate. | C-27 (predicted) | 100.00 |
| V-04 | Axes G+H combined | FULL mode restart gate + transcription entry count confirmation. Both structural upgrades without per-section check. | C-25+C-26 (predicted) | 100.00 |
| V-05 | Axes G+H+I: triple convergence | All three axes applied to R6 V-05 base. Predicted to satisfy any C-25/C-26/C-27 criteria the rubric may extract from R7 signals. | C-25+C-26+C-27 (predicted) | 100.00 |

All five variations are predicted to score 100.00 under v7 since all carry the full
R6 V-05 mechanism set. The axes probe for excellence signals beyond the current
ceiling -- the rubric will decide whether they encode new criteria.

---

## V-01 -- Single-axis: COMPLIANCE GATE -- FULL MODE (Axis G)

**Axis**: Explicit namespace-presence + per-namespace-count restart gate added for
FULL mode output, symmetric with BARE (C-18) and FILTER (C-20) compliance gates.
**Hypothesis**: R6 V-05 has two structured restart gates -- BARE MODE (Check 1:
format; Check 2: 61-line count) and FILTER MODE (Check 1: scope; Check 2: canonical
count) -- but FULL mode has only the transcription commitment gate (C-22/C-23).
A commitment gate pledges fidelity; a restart gate enforces completeness. The
transcription pledge prevents paraphrase; it does not prevent a model from omitting
a namespace entirely or emitting 11 of 12 namespace sections. Adding COMPLIANCE
GATE -- FULL MODE with Check 1 (namespace presence: all 12 canonical namespaces
appear) and Check 2 (per-namespace count: each section has exactly its canonical
number of sub-skills) closes the structural gap and creates four-gate symmetry
across all three emission paths.
No change to NAMESPACE CATALOG header, BARE MODE, or FILTER MODE gate.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read every entry in the 12 namespace sections
below and will emit each entry character-for-character. The catalog below IS the output
for FULL and FILTER modes. Do not paraphrase, condense, reorder, or reconstruct from
memory. Any deviation from the catalog text is an output failure, not an acceptable
approximation.

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

Before emitting FULL output, run both checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.

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

Before emitting filter output, run both checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.
```

---

## V-02 -- Single-axis: Transcription Gate Entry-Count Confirmation (Axis H)

**Axis**: NAMESPACE CATALOG transcription gate upgraded to include explicit 61-entry
count verification before the commitment pledge.
**Hypothesis**: R6 V-05's transcription gate says "confirm you have read every entry
in the 12 namespace sections below." This is a comprehension acknowledgment, not a
count verification. C-18 extended C-14's restart gate with an exact line count
(61 lines = 8+4+4+7+7+9+3+2+6+4+3+4); the same pattern applied to the transcription
gate would require the model to explicitly verify it has counted 61 entries before
pledging character-for-character fidelity. "I read all of them" and "I counted exactly
61 of them" are different levels of rigor. A model that skips a namespace may still
satisfy the commitment framing without catching the omission. Adding the count
verification -- "confirm you have read all 61 entries (8+4+4+7+7+9+3+2+6+4+3+4=61)"
-- makes the pre-transcription verification structurally equivalent to the pre-bare
verification in C-18.
No change to COMPLIANCE GATE -- FILTER MODE (scope+count already present) or
BARE MODE (anchors already present). No COMPLIANCE GATE -- FULL MODE added.

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

Before emitting filter output, run both checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.
```

---

## V-03 -- Single-axis: Per-Section Count Self-Check in SECTION FORMAT (Axis I)

**Axis**: SECTION FORMAT upgraded with an explicit per-section count self-check
instruction before closing each namespace section.
**Hypothesis**: R6 V-05's SECTION FORMAT specifies the structural template but does
not instruct the model to self-check that the count of emitted sub-skills matches
the canonical count before moving to the next namespace. C-06 tests whether section
header counts are accurate in the final output; C-18/C-20 enforce document-level
restart gates. Neither addresses a model that emits a correct header (e.g. "-- 7
skills") but silently emits 6 sub-skills, because the document-level gate catches
total-document count, not per-section count (61 total could be correct while one
section has 6 and another has 8). A per-section count self-check -- "before closing
each namespace section, verify: the number of sub-skills listed equals the header's
N value and the canonical count; if not, restart the section" -- operates at section
granularity and closes the gap. This is an I-instruction (section-level), not a
gate-with-restart at the document level.
No change to NAMESPACE CATALOG header or compliance gates.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read every entry in the 12 namespace sections
below and will emit each entry character-for-character. The catalog below IS the output
for FULL and FILTER modes. Do not paraphrase, condense, reorder, or reconstruct from
memory. Any deviation from the catalog text is an output failure, not an acceptable
approximation.

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

Before emitting filter output, run both checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.
```

---

## V-04 -- Combined: Axes G+H (FULL Mode Gate + Entry Count Confirmation)

**Axis**: Both structural completion mechanisms for FULL mode without the per-section
check -- COMPLIANCE GATE -- FULL MODE (G) + transcription gate entry-count (H).
**Hypothesis**: Axis G adds a structured restart gate for FULL mode (symmetric with
BARE/FILTER gates); Axis H adds explicit 61-entry count confirmation to the
transcription gate preamble. G addresses structural completeness (what namespaces and
counts are present); H addresses reading completeness (did the model process all 61
entries before pledging). The two mechanisms are structurally independent: G operates
as a pre-emit gate in the compliance gate block; H operates as a pre-transcription
verification in the catalog header. No interaction effects are predicted. V-05 adds I
to confirm the per-section check is independently additive.
No change to SECTION FORMAT (no per-section check).

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

Before emitting FULL output, run both checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.

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

Before emitting filter output, run both checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.
```

---

## V-05 -- Triple Convergence: Axes G+H+I (Golden Target)

**Axis**: All three R7 axes combined in the R6 V-05 base -- the first variation to
probe all three post-ceiling mechanisms simultaneously.
**Hypothesis**: Axis G (FULL mode restart gate), Axis H (transcription gate entry-count
confirmation), and Axis I (per-section count self-check) address three structurally
independent levels of completeness verification:
- G: document level, FULL mode, post-generation restart gate
- H: pre-transcription, entry-count verification before the commitment pledge
- I: section level, per-section count check before closing each namespace block

None modifies the same section or mechanism as another. Each is independently
isolation-tested in V-01/V-02/V-03. G+H combination confirmed in V-04. Adding I to
the G+H base should produce triple convergence.

The three changes from R6 V-05 to R7 V-05:
1. NAMESPACE CATALOG header: "confirm you have read every entry" -> "confirm you
   have read all 61 entries (8+4+4+7+7+9+3+2+6+4+3+4=61)" (Axis H)
2. SECTION FORMAT: add per-section count self-check instruction before dispatch
   footer (Axis I)
3. Add COMPLIANCE GATE -- FULL MODE block between DOMAIN NOUN TABLE and
   COMPLIANCE GATE -- BARE MODE (Axis G)

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

Before emitting FULL output, run both checks:
  Check 1 (completeness): Does your output include sections for all 12 canonical
    namespaces: scout, draft, review, flow, trace, prove, listen, program, topic,
    quest, mock, org?
    If any namespace is absent -- MODE: FULL is incomplete. Restart.
  Check 2 (count): Does each namespace section contain exactly the canonical number
    of sub-skills?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If any section's count differs -- a sub-skill is missing or duplicated. Restart.

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

Before emitting filter output, run both checks:
  Check 1 (scope): Does your output include any command from a namespace other than
    the one requested?
    If yes -- MODE: FILTER scope is violated. Restart.
  Check 2 (completeness): Does your output contain exactly the canonical count of skills
    for the requested namespace?
    Canonical counts: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
    program=2, topic=6, quest=4, mock=3, org=4.
    If not -- a sub-skill is missing or duplicated in the filter output. Restart.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
Begin with scout-competitors. End with org-committee.
```

---

## Structural summary of changes from R6 V-05

| Section | R6 V-05 | V-01 (G) | V-02 (H) | V-03 (I) | V-04 (G+H) | V-05 (G+H+I) |
|---------|---------|---------|---------|---------|------------|--------------|
| TRANSCRIPTION GATE | "every entry" | unchanged | "all 61 entries (breakdown)" | unchanged | "all 61 entries (breakdown)" | "all 61 entries (breakdown)" |
| SECTION FORMAT | template only | unchanged | unchanged | + per-section count self-check | unchanged | + per-section count self-check |
| COMPLIANCE GATE -- FULL MODE | absent | added (12-ns + counts) | absent | absent | added (12-ns + counts) | added (12-ns + counts) |
| COMPLIANCE GATE -- BARE MODE | unchanged | unchanged | unchanged | unchanged | unchanged | unchanged |
| COMPLIANCE GATE -- FILTER MODE | unchanged | unchanged | unchanged | unchanged | unchanged | unchanged |
| BARE MODE | unchanged | unchanged | unchanged | unchanged | unchanged | unchanged |
