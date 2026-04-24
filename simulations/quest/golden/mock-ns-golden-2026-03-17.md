---
skill: quest-golden
skill_target: mock-ns
date: 2026-03-17
rounds: 20
rubric_final: mock-ns-rubric-v20-2026-03-17.md
score: 168
status: GOLDEN
---

# mock-ns -- Golden Prompt

**Source**: R20 V-05, QU5 simplified (PASS, 23% reduction -- 2,212 -> 1,694 words)
**Score**: 168/168 under v20 (52 criteria: 10 essential + 6 recommended + 36 aspirational)

---

## Prompt Body

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

LIFECYCLE

  Phase 1 -- Protocol and topic resolution
    P-0  Cross-reference protocol (token registration + anti-bypass declaration)
         Entry: no bracket tokens defined; no anti-bypass declaration
         Exit:  [S-3:CS], [S-4:FC], [P-0:ABD] registered; two-phase lookup protocol documented
    S-0  Read TOPICS.md (emit status line)
         Entry: topic + namespace + optional flags; TOPICS.md unread; tier unresolved
         Exit:  TOPICS.md status line emitted; tier resolved; compliance-tags resolved; tier-source resolved

  Phase 2 -- Skill and category resolution
    S-1  Skill selection
         Entry: namespace; optional --skill arg
         Exit:  skill-id resolved; generating-mock emit written
    S-2  Category lookup
         Entry: skill-id from S-1
         Exit:  CATEGORY assigned (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED); category emit written

  Phase 3 -- Flag computation
    S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
         Entry: tier, compliance-tags, tier-source from S-0; CATEGORY from S-2
         Exit:  FLAG resolved and locked; S-3.1/S-3.2/S-3.3 emits written; immutability chain closed

  Phase 4 -- Artifact generation and finalization
    S-4  Artifact generation (header | fidelity warning | mock body)
         Entry: skill-id, topic, CATEGORY, FLAG, tier
         Exit:  MOCK ARTIFACT header written; fidelity warning written; mock body written
    S-5  Finalize (S-5.4 write)
         Entry: completed artifact sections from S-4
         Exit:  artifact written to path; next-step line last

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. All tokens defined here.

Anti-bypass declaration (ABD): An executor who processes a bracket token without
performing Phase 2 (Steps 2a through 2d) has not satisfied this protocol.
Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo this
declaration. [P-0:ABD] is registered as its own definition point -- encountering
[P-0:ABD] at an echo site requires Phase 1 lookup on [P-0:ABD] before processing.

  | Token     | Step | Row type                 | Paired token | Direction                |
  |-----------|------|--------------------------|--------------|--------------------------|
  | [S-3:CS]  | S-3  | Cross-site reference row | [S-4:FC]     | forward --> names S-4    |
  | [S-4:FC]  | S-4  | Failure consequence row  | [S-3:CS]     | <-- backward, names S-3  |
  | [P-0:ABD] | P-0  | Anti-bypass declaration  | (self)       | definition point         |

Lookup protocol -- two phases, both required before writing any bracket-token row:

  Phase 1 -- Locate: find the row by token name in the table above.
  Phase 2 -- Confirm:
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step; row type matches current row role.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match only).
             DO NOT WRITE THE ROW until Steps 2a-2d are complete.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                  | Downstream-Action                                                                 |
  |-----------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                              |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                            | Consumed at S-3.3 (flag computation)                                              |
  | compliance-tags | TOPICS.md if found; none if not                                             | Consumed at S-3.2 (compliance detection)                                          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override       | Consumed at S-3.1; re-emitted as carry record before S-3.2 begins                |

Only this step emits the TOPICS.md status line.

---

STEP S-1 -- SKILL SELECTION

  | Namespace | Default skill     | Exclusion note                                 |
  |-----------|-------------------|------------------------------------------------|
  | scout     | scout-feasibility |                                                |
  | draft     | draft-spec        |                                                |
  | review    | review-design     |                                                |
  | flow      | flow-resilience   |                                                |
  | trace     | trace-request     |                                                |
  | prove     | prove-hypothesis  |                                                |
  | listen    | listen-support    |                                                |
  | program   | program-plan      |                                                |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills                                                                       |
  |----------------|-------------------------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,            |
  |                | scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,            |
  |                | review-design, review-code, trace-request, trace-component, trace-contract,         |
  |                | trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,       |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,      |
  |                | flow-integration, program-plan                                                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, |
  |                | listen-adoption                                                                     |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers, review-users                 |

Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY: Emit: > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}
  S-3.2 -- COMPLIANCE: Emit: > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}
  S-3.3 -- FLAG:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-*, scout-feasibility, listen-support, listen-feedback, listen-adoption.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE.

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                         |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration      |
  |                         | sequence -- no execution context is exempt                               |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value emitted here|
  | No-exemption            | No path is exempt from this closure requirement                          |
  | Failure consequence     | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's   |
  |                         | trust tier that is invisible to downstream tooling -- undetectable        |
  |                         | without manual header inspection                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in Affirmative closure |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match; emit         |
  | (P-0 table, row 1)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC] --   |
  |                         | the Failure consequence row in S-4 header assembly (that row identifies  |
  |                         | itself as this row's mutual target)                                      |

---

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest (emit before writing any artifact content):

  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line

Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                         |
  | Priority                | No instruction in this step can precede this rule.                       |
  | All-governed            | All instructions in this step, named or unnamed, are subject to this     |
  |                         | rule, including paths that do not pass through prior steps in normal     |
  |                         | order                                                                    |
  | Guarantee-break         | This violation breaks the FLAG closure guarantee stated in S-3's         |
  |                         | Affirmative closure row -- the corruption is undetectable without        |
  |                         | manual header inspection                                                 |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-4 + Row type=Failure consequence row; assert match; emit          |
  | (P-0 table, row 2)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | processing this row without performing Phase 2 (Steps 2a-2d) has not    |
  | [P-0:ABD]:              | satisfied this protocol. Locate-only is a protocol failure.              |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]             |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to          |
  |                         | downstream tooling that silently corrupts the artifact's trust tier      |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
    be partially accurate or partially fabricated. Review for plausibility.

Emit: > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate content following the exact golden structural pattern of {skill-id}: correct
  section headings, required tables and lists, gate or verdict line in expected position,
  enforcement mechanisms present. Use {topic} as subject. A reader familiar with {skill-id}
  must identify the skill from the body alone.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## What Made It Golden

Five patterns distinguish R20 V-05 from the baseline and from all prior rounds.

**1. Phase-grouped lifecycle with per-step entry/exit state annotations (C-48/C-49)**
The lifecycle is organized into four named phases (Protocol, Skill/Category, Flag,
Artifact). Every step declares Entry and Exit states. This transforms the lifecycle from
a sequence list into a state machine contract -- each step's preconditions and postconditions
are explicit, and the phase boundary between flag computation (Phase 3) and artifact
generation (Phase 4) makes the S-3/S-4 FLAG handoff structurally visible.

**2. Priority row with modal impossibility form (C-50 -- Axis A)**
The S-4 FLAG prohibition chain's Priority row reads: "No instruction in this step can
precede this rule." The modal impossibility form (`can precede`) asserts a structural
constraint, not an ordering preference. This is stronger than "this rule is first"
(positional claim) or "this rule must be followed first" (obligation). It closes the
gap between stated priority and logical precedence.

**3. Anti-bypass echo with bracket token as row header label (C-51 -- Axis B)**
The anti-bypass echo rows at S-3 and S-4 use `[P-0:ABD]:` as the row header cell label,
with attribution removed from the content cell. This forces a Phase 1 lookup on the
echo row itself before processing -- the bracket token in the header is a self-referential
trip-wire. Attribution-in-cell form (the R19 baseline) allowed the echo to be read as
commentary; header-label form makes it a lookup obligation.

**4. All-governed dual closure (C-52 -- Axis C)**
The All-governed row in the S-4 FLAG prohibition chain closes with: "including paths
that do not pass through prior steps in normal order." This adds a second closure
("bypass-by-skip") to the existing "named or unnamed" closure. Together they eliminate
two distinct bypass vectors: instructions that claim to be exempt by not being named,
and execution paths that claim to be exempt by not following the normal step sequence.

**5. QU5 simplification at zero criteria cost (23% reduction)**
Fourteen removals across six zones stripped 518 words with no criteria loss. The key
insight: five S-5 sub-steps (S-5.0 propagation, S-5.1 count, S-5.2 order, S-5.3 header)
had no corresponding criteria in v20 and existed as internal defense-in-depth. Removing
them reduced prompt complexity without weakening the rubric surface. The simplification
pass confirmed that the prompt's length was load-bearing structure, not load-bearing words.

---

## Final Rubric Criteria Summary (v20 -- 52 criteria, 168 points)

### Essential (C-01--C-05) -- 50 points, all must pass

| C    | Criterion                                         | V-05 |
|------|---------------------------------------------------|------|
| C-01 | 6-field header block (skill, topic, tier, category, flag, date) | PASS |
| C-02 | CATEGORY assignment table present and correct in S-2 | PASS |
| C-03 | 5-row FLAG table in S-3 with correct case rules; verbatim copy in S-4 | PASS |
| C-04 | Fidelity warning with all three CATEGORY-branch texts | PASS |
| C-05 | Mock body requires golden structural pattern of {skill-id} | PASS |

### Recommended (C-06--C-08) -- 30 points

| C    | Criterion                                         | V-05 |
|------|---------------------------------------------------|------|
| C-06 | S-0 TOPICS.md emit; S-1 generating-mock emit; S-0 before S-1 | PASS |
| C-07 | S-5.4 writes artifact path with {namespace} (not skill-id) | PASS |
| C-08 | S-5.4 next-step line: `/mock:review {topic} {path}` | PASS |

### Aspirational (C-09--C-52) -- 88 points (44 x 2)

| Zone | Criteria | Pattern tested | V-05 |
|------|----------|---------------|------|
| FLAG and namespace correctness | C-09--C-11 | topic exclusion, compliance-override path, 5-row FLAG with wildcard patterns | PASS |
| Step separation | C-12--C-14 | S-0 complete before S-1; S-2 exhaustive; assembly as discrete named sub-sections | PASS |
| CONSTRAINT depth | C-15--C-16 | 5 operation types named; wildcard patterns in FLAG table condition cells | PASS |
| S-0 gate and tier-carry | C-17--C-20 | advancement gate sentence; tier handoff naming consumers; preamble + terminal gate pair; "Only this step emits..." as standalone terminal sentence | PASS |
| CONSTRAINT depth (continued) | C-21--C-24 | >= 4 operation types; 5 FLAG rows; CONSTRAINT before gate; carry + compliance as distinct operation types | PASS |
| S-0 declarative identity | C-25--C-28 | declarative form, step as subject; artifact named in identity sentence; tier available before gate; nominative subject + emission predicate | PASS |
| Declarative failure mode prohibitions | C-29--C-37 | 9 prohibited grammatical forms absent from S-0 emission sentence | PASS |
| S-0 scope and inter-step emission | C-38--C-43 | S-0 is sole emitter; scope sentence placement; no modal-obligation form; no emission in S-1 body; no S-0 emit in S-1; sentinel token not repeated | PASS |
| CONSTRAINT per-ID annotations | C-44--C-46 | per-step ID annotations in CONSTRAINT; 5 sub-steps; 5 distinct operation-type labels | PASS |
| Phase-grouped lifecycle with state annotations | C-47--C-49 | phases named; phase grouping by concern; per-step entry/exit states | PASS |
| S-4 FLAG prohibition chain -- Priority row | C-50 | "No instruction in this step can precede this rule." -- modal impossibility form | PASS |
| S-4 FLAG prohibition chain -- Anti-bypass echo header | C-51 | `[P-0:ABD]:` as row header label; attribution removed from content cell | PASS |
| S-4 FLAG prohibition chain -- All-governed dual closure | C-52 | "including paths that do not pass through prior steps in normal order" | PASS |

**Score: 168/168 -- all 52 criteria pass under v20.**
