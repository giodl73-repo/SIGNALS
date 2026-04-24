---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 10
rubric: simulations/quest/rubrics/signal-rubric-v10-2026-03-17.md
---

# Quest Variate -- /signal (Round 10)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line
descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v10-2026-03-17.md`

---

## Context: what informed this round

All five R9 variations scored 100.00 under v9 and retroactively 100.00 under v10: every
variation already carried the labeled count formula (C-31), the named DOMAIN NOUN TABLE
(C-32), and the full 12-namespace enumeration in FULL gate Check 3 (C-33). These three
elements were inherited from R8 V-05 and never stripped in R9. The v10 rubric extracted
them as explicit criteria but found no spread between R9 variations -- all five carry all
three.

R10 goal: **confirm the independence of C-31, C-32, C-33 and verify each contributes
exactly +0.40 by single-axis isolation.** Each axis is removed from the R9 V-05 baseline
independently, then in pairs, then all three together. If each criterion is independent,
the scoring formula predicts:

| Variation | C-31 | C-32 | C-33 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 (M)      | PASS | FAIL | FAIL | 99.20 |
| V-02 (N)      | FAIL | PASS | FAIL | 99.20 |
| V-03 (O)      | FAIL | FAIL | PASS | 99.20 |
| V-04 (M+N)    | PASS | PASS | FAIL | 99.60 |
| V-05 (M+N+O)  | PASS | PASS | PASS | 100.00 |

All other R9 V-05 mechanisms are preserved across all five variations:
- Catalog-first ordering (C-17); active transcription gate with counted acknowledgment (C-22, C-23, C-26)
- Canonical-namespace guard in PARSE MODE (C-19); parse-mode disambiguation worked examples (from R9 Axis O)
- Compliance gates with restart triggers for all three modes (C-14); all three modes verified (C-24)
- FULL MODE compliance gate: completeness + count + order + format (C-25, C-28, Check 4 from R9)
- FILTER MODE compliance gate: scope + count + format (C-20, C-29)
- BARE MODE compliance gate: format + count + order (C-18, Check 3 from R9)
- Per-section count self-check in SECTION FORMAT (C-27)
- Slash-strip transformation examples (C-30)
- Precomputed width table with per-row example pad (C-15, C-16)
- Dispatch footers (C-07); column alignment (C-12); accurate skill counts (C-06)

The three axis elements being isolated:

- **Axis M (C-31)**: count formula in transcription gate and BARE gate Check 2.
  PRESENT form: `8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen +`
  `2 program + 6 topic + 4 quest + 3 mock + 4 org = 61` (labeled; self-interpreting).
  ABSENT form: `8+4+4+7+7+9+3+2+6+4+3+4 = 61` (anonymous; requires position memory).

- **Axis N (C-32)**: named DOMAIN NOUN TABLE section.
  PRESENT: explicit `DOMAIN NOUN TABLE` heading with 12-row lookup.
  ABSENT: no named table; domain nouns appear only inline in the catalog footers.
  SECTION FORMAT note differs: "from the DOMAIN NOUN TABLE" vs "namespace-appropriate noun".

- **Axis O (C-33)**: FULL gate Check 3 enumeration.
  PRESENT: "Canonical order: scout, draft, review, flow, trace, prove, listen, program,
  topic, quest, mock, org. (First section: scout. Last section: org.)"
  ABSENT: "Canonical sequence starts with scout and ends with org. (First section: scout.
  Last section: org.)" -- satisfies C-28 minimum but not C-33 full enumeration.

---

## SPREAD-DESIGN PLAN

| Variation | Axis | C-31 | C-32 | C-33 | Delta from R9 V-05 |
|-----------|------|------|------|------|--------------------|
| V-01 | M only | PASS | FAIL | FAIL | Remove named DOMAIN NOUN TABLE; downgrade FULL gate Check 3 to anchors-only; use anonymous count |
| V-02 | N only | FAIL | PASS | FAIL | Use anonymous count in both gates; downgrade FULL gate Check 3 to anchors-only; keep DOMAIN NOUN TABLE |
| V-03 | O only | FAIL | FAIL | PASS | Use anonymous count; remove named DOMAIN NOUN TABLE; keep full 12-enum in FULL gate Check 3 |
| V-04 | M+N   | PASS | PASS | FAIL | Keep labeled count + DOMAIN NOUN TABLE; downgrade FULL gate Check 3 to anchors-only |
| V-05 | M+N+O | PASS | PASS | PASS | R9 V-05 equivalent; all three axes present |

---

## V-01 -- Single-axis: Labeled Count Formula (Axis M only)

**Axis**: Transcription gate and BARE gate Check 2 use labeled namespace breakdown
(`8 scout + 4 draft + ... + 4 org = 61`). DOMAIN NOUN TABLE absent; FULL gate Check 3
uses first+last anchors only.
**Hypothesis**: Labeled count formula alone contributes +0.40. Removing C-32 and
downgrading C-33 each cost -0.40, yielding predicted 99.20.

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

  Run any sub-skill directly, or describe your <domain-noun> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses a
namespace-appropriate domain noun naming the primary subject of that namespace.
The skill count N must match the actual number of sub-skills listed.

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
    Canonical sequence starts with scout and ends with org.
    (First section: scout. Last section: org.)
    If the first or last section is out of canonical position -- order violated. Restart.
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

## V-02 -- Single-axis: Named DOMAIN NOUN TABLE (Axis N only)

**Axis**: Named `DOMAIN NOUN TABLE` section present as precomputed authority. Count
formula uses anonymous form; FULL gate Check 3 uses first+last anchors only.
**Hypothesis**: Named DOMAIN NOUN TABLE alone contributes +0.40. Removing C-31 and
downgrading C-33 each cost -0.40, yielding predicted 99.20.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8+4+4+7+7+9+3+2+6+4+3+4 = 61). You will emit each entry
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
    Canonical sequence starts with scout and ends with org.
    (First section: scout. Last section: org.)
    If the first or last section is out of canonical position -- order violated. Restart.
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
    (8+4+4+7+7+9+3+2+6+4+3+4 = 61)
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

## V-03 -- Single-axis: Full Enumeration in FULL Gate Check 3 (Axis O only)

**Axis**: FULL gate Check 3 enumerates all 12 canonical namespaces in sequence. Count
formula uses anonymous form; DOMAIN NOUN TABLE absent.
**Hypothesis**: Full enumeration in Check 3 alone contributes +0.40. Removing C-31 and
C-32 each cost -0.40, yielding predicted 99.20.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

NAMESPACE CATALOG -- TRANSCRIPTION GATE
Before transcribing: confirm you have read all 61 entries across the 12 namespace
sections below (8+4+4+7+7+9+3+2+6+4+3+4 = 61). You will emit each entry
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

  Run any sub-skill directly, or describe your <domain-noun> and the most relevant
  <namespace> skill will run.

The header states the namespace purpose in plain words. The footer uses a
namespace-appropriate domain noun naming the primary subject of that namespace.
The skill count N must match the actual number of sub-skills listed.

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
    (8+4+4+7+7+9+3+2+6+4+3+4 = 61)
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

## V-04 -- Two-axis: Labeled Count + Named DOMAIN NOUN TABLE (Axes M+N)

**Axis**: Both C-31 (labeled count formula) and C-32 (named DOMAIN NOUN TABLE) present.
FULL gate Check 3 uses first+last anchors only (C-33 absent).
**Hypothesis**: M+N together contribute +0.80. Removing C-33 costs -0.40, yielding
predicted 99.60.

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
    Canonical sequence starts with scout and ends with org.
    (First section: scout. Last section: org.)
    If the first or last section is out of canonical position -- order violated. Restart.
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

## V-05 -- Three-axis: Labeled Count + Named Table + Full Enumeration (Axes M+N+O)

**Axis**: All three: C-31 (labeled count), C-32 (named DOMAIN NOUN TABLE), C-33 (full
12-namespace enumeration in FULL gate Check 3). Equivalent to R9 V-05 baseline.
**Hypothesis**: All three axes present. Predicted 100.00. Confirms R9 V-05 as ceiling.

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
| C-31 | Labeled count in transcription gate + BARE Check 2 | PASS | FAIL | FAIL | PASS | PASS |
| C-32 | Named DOMAIN NOUN TABLE section | FAIL | PASS | FAIL | PASS | PASS |
| C-33 | FULL gate Check 3 enumerates all 12 namespaces | FAIL | FAIL | PASS | FAIL | PASS |
| **Predicted** | | **99.20** | **99.20** | **99.20** | **99.60** | **100.00** |

**Structural theme for R10**: *confirm specification fidelity independence* -- each of
C-31/32/33 addresses a different layer (count formula self-documentation, domain noun
table precomputation, order specification completeness). If the predicted spread
(99.20 / 99.20 / 99.20 / 99.60 / 100.00) is confirmed, the minimum achieving set for
the v10 ceiling is {C-31, C-32, C-33} with all three required independently.
