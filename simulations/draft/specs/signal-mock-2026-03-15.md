# Mock Specification

**Topic**: signal
**Namespace**: /mock:
**Skills**: 3
**Default mode**: Lightweight
**Audience**: Anyone beginning a new feature topic investigation -- PMs, developers, architects,
team leads who want a panoramic coverage picture before committing to real skill runs.

## Purpose

The mock namespace answers the question every team faces at the start of a feature investigation:

> "What does my coverage picture look like before I've done any work?"

Running every Signal skill takes time. A `prove-interview` skill requires actual user conversations.
A `listen-support` skill requires real ticket data. A `prove-websearch` skill requires live search.
Before any of that work is done, a team has no visibility into which namespaces look structurally
thin, which enforcement mechanisms are missing, and which domains need the deepest investigation.

The mock namespace solves this with a **mock-first workflow**: generate synthetic preview artifacts
for all 9 namespaces in a single pass, review the coverage picture to identify structural gaps and
flag evidence-heavy namespaces, then run targeted real skills only for what was flagged. Coverage
gaps become visible at the cost of one multi-namespace mock pass rather than being discovered
sequentially as real runs are completed.

**The founding insight** (from S4-01, S4-03): mock fidelity splits along a structural/evidential
axis. Structural fidelity is high across all skill categories because the seven enforcement
archetypes (gates, comparison tables, role cards, named-output lists, numeric rubrics, decision
trees, dual-channel response structures) constrain both mock and real outputs to the same form.
Evidential fidelity is high for skills where structure is the substance (scout-feasibility,
trace-request), and low for skills where value is in the data collected (prove-interview,
listen-support). Mocks are reliable for structural planning; they are not reliable for evidential
decisions.

The mock namespace exists to make this distinction operational -- not just as a warning in docs,
but as annotations embedded in every artifact the namespace produces.

---

## Annotation Schema

Every mock artifact produced by any `/mock:` skill begins with this header block, immediately
after the frontmatter:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED
Date: {date}
Status: MOCK (awaiting review)
```

The Status field follows a defined transition lifecycle:

| Status | Meaning | Set by |
|--------|---------|--------|
| MOCK | Generated, not reviewed | mock-all or mock-ns at generation time |
| MOCK-ACCEPTED | Reviewed; accepted as structurally adequate for current decision tier | mock-review (with explicit reason code) |
| REAL-REQUIRED | Reviewed; flagged as requiring a real skill run | mock-review (automatic for evidence-heavy, explicit for others) |

**Critical distinction**: MOCK is the generation-time state. MOCK-ACCEPTED is the review-time
acceptance decision. These are separate acts. Reading a MOCK annotation does not produce
MOCK-ACCEPTED status. `mock-review` writes the MOCK-ACCEPTED annotation -- it does not merely
read. An artifact that was generated but never reviewed remains MOCK (not MOCK-ACCEPTED) and
is treated as UNVERIFIED by `topic-status`.

**MOCK-ACCEPTED reason codes** (one or both must be recorded):

| Code | Meaning |
|------|---------|
| STRUCTURAL-COVERAGE-SUFFICIENT | Artifact structure and enforcement mechanisms are correct; structural coverage is adequate for current decision tier |
| DOMAIN-KNOWLEDGE-CONSISTENT | Artifact content is consistent with team's domain knowledge; no contradictions identified in review |

---

## Skill Category Classification

The category embedded in each mock artifact header is drawn from S4-01's fidelity framework.
It determines automatic flagging behavior in `mock-review` and signals to the team whether
real runs are likely needed.

| Category | Skills | Mock validity |
|----------|--------|--------------|
| HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-request, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger, flow-integration, program-plan | Structure is the substance. Mock is structurally reliable. MOCK-ACCEPTED appropriate for Tier 1. |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption | Value is in the data collected. Structure is right; content is fabricated. REAL-REQUIRED unless Tier 1 structural-only use. |
| MIXED | scout-competitors (comparison table + real WebSearch), prove-hypothesis (hypothesis framework + real evidence), review-customers, review-users | Partially structural, partially evidential. Review content for plausibility. Flag for real run at Tier 2/3. |

**Critical namespace rules** (S3-02 / S4-03): For Tier 2 and Tier 3 features, the following
namespaces require VERIFIED (real skill run), not MOCK-ACCEPTED, regardless of mock structural
quality:

- `trace` (any trace-* skill) -- implementability risk at Tier 2+
- `scout-feasibility` -- build constraint risk at Tier 2+
- `listen` (any listen-* skill) -- adoption evidence risk at Tier 2+
- `scout-competitors` -- inertia assessment cannot be fabricated at Tier 2+

Compliance-sensitive features additionally require VERIFIED for `scout-compliance` and
`trace-permissions` at all tiers.

---

## Skills

### /mock:all

**What**: Generate synthetic signal artifacts for all 9 namespaces in a single pass, producing a
unified coverage picture that shows structural completeness, skill categories, and flagging status
across every namespace before any real skill runs have been done.

**Stock roles**: None required -- the skill uses the category registry embedded in the skill
definition to classify and annotate each namespace output.

**Input**: Topic name (required). Optional: `--tier 1|2|3` to set the decision tier for
automatic flagging (default: 1). Optional: `--compliance` to pre-flag compliance-adjacent
namespaces as REAL-REQUIRED regardless of structural quality.

**Output**: A unified mock artifact at `simulations/mock/{topic}-mock-{date}.md` containing:
- Nine namespace sections, one per namespace, each with the mock output following the golden
  rubric structure for the representative skill of that namespace
- MOCK ARTIFACT header block on each namespace section (Skill, Topic, Category, Date, Status)
- Automatic flagging: EVIDENCE-HEAVY namespaces marked `Flag: REAL-REQUIRED (evidence-heavy)`
- Automatic flagging: MIXED namespaces marked `Flag: REVIEW-FOR-PLAUSIBILITY`
- HIGH-STRUCTURE namespaces marked `Flag: none (structural coverage reliable)`
- If `--compliance` flag or compliance tags in TOPICS.md: compliance-adjacent namespaces marked
  `Flag: REAL-REQUIRED (compliance-sensitive)`
- Coverage summary table at the end: one row per namespace, columns: Namespace, Category, Flag,
  Recommended next step

**Lifecycle**:
- Setup: Read TOPICS.md to check for the topic (existing strategy, compliance tags, tier
  classification). If topic not registered, proceed with defaults -- no blocking prompt.
  Identify the representative skill for each namespace based on the topic description context.
  For broad topics, default to the most commonly run skill per namespace.
- Execute: For each of the 9 namespaces in order, generate a mock artifact following the skill's
  golden prompt structure exactly. The mock generation prompt instructs the AI to follow the
  exact structure of the skill, including all required sections, fields, and enforcement
  mechanisms, while generating synthetic but structurally representative content. Each namespace
  section opens with the MOCK ARTIFACT header block. After all 9 sections, write the coverage
  summary table.
- Findings: The unified mock artifact is the coverage picture. Do not interpret it -- present
  it. The next step is `mock-review`. The final line of the artifact is:
  `Next: /mock:review {topic} {this-file}` to make Step 2 invocation obvious.
- Amend: Not applicable. Each mock-all run is a complete new coverage picture. If the picture
  needs adjustment, run `mock-ns` to regenerate a single namespace.

**Lightweight**: All 9 namespaces in one pass. No confirmation prompts. No iterative refinement.
Category flags are automatic.

**Artifact**: `simulations/mock/{topic}-mock-{date}.md`

**Tools**: Read, Write, Glob

**Example**:
```
User: /mock:all frogs
> Reading TOPICS.md... topic frogs found, tier: 1, compliance tags: none
> Generating 9 namespace mock artifacts...

[MOCK ARTIFACT -- NOT VERIFIED]
Skill: scout-feasibility
Topic: frogs
Category: HIGH-STRUCTURE
Date: 2026-03-15
Status: MOCK (awaiting review)
Flag: none (structural coverage reliable)

## Feasibility Assessment (MOCK)
| Component | Complexity | Risk | Build/Buy |
|-----------|-----------|------|-----------|
| CRM sync engine | 3/5 | YELLOW | Buy |
| Field mapping layer | 2/5 | GREEN | Build |
| Conflict resolution | 4/5 | RED | Build |
Overall: 58/100 -- CONDITIONAL FEASIBLE
Gate: PASS (conditional on conflict resolution approach)

---

[MOCK ARTIFACT -- NOT VERIFIED]
Skill: listen-support
Topic: frogs
Category: EVIDENCE-HEAVY
Date: 2026-03-15
Status: MOCK (awaiting review)
Flag: REAL-REQUIRED (evidence-heavy -- real ticket data needed)

## Support Prediction (MOCK -- content fabricated)
...

---

## Coverage Summary

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
| scout | HIGH-STRUCTURE | none | MOCK-ACCEPTED after review |
| draft | HIGH-STRUCTURE | none | MOCK-ACCEPTED after review |
| review | MIXED | REVIEW-FOR-PLAUSIBILITY | Real run if design is VERIFIED |
| flow | HIGH-STRUCTURE | none | MOCK-ACCEPTED after review |
| trace | HIGH-STRUCTURE | none | MOCK-ACCEPTED (Tier 1); REAL-REQUIRED (Tier 2+) |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | Real skill run needed |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED | Real skill run needed |
| program | HIGH-STRUCTURE | none | MOCK-ACCEPTED for planning |
| topic | HIGH-STRUCTURE | none | MOCK-ACCEPTED for planning |

> Artifact written: simulations/mock/frogs-mock-2026-03-15.md
> Next: /mock:review frogs simulations/mock/frogs-mock-2026-03-15.md
```

---

### /mock:ns

**What**: Generate a mock artifact for a single namespace. Useful for targeted preview when
one namespace needs a structural look before committing to a real skill run, or when
`mock-all` produced a thin output for one namespace that should be regenerated.

**Stock roles**: None required.

**Input**: Topic (required). Namespace -- one of: scout | draft | review | flow | trace | prove |
listen | program | topic (required). Optional: `--skill {skill-id}` to specify a particular
skill within the namespace (default: representative skill for the namespace). Optional:
`--tier 1|2|3` (default: 1).

**Output**: A single mock artifact at `simulations/mock/{topic}-{namespace}-mock-{date}.md`
containing:
- MOCK ARTIFACT header block (Skill, Topic, Category, Date, Status)
- Mock output following the golden rubric structure for the specified skill
- Automatic category flag (same logic as mock-all)
- Single-namespace recommended next step

**Lifecycle**:
- Setup: Identify the skill to mock. If `--skill` is specified, use it. Otherwise, use the
  representative skill for the namespace: scout=scout-feasibility, draft=draft-spec,
  review=review-design, flow=flow-resilience, trace=trace-request, prove=prove-hypothesis,
  listen=listen-support, program=program-plan, topic=topic-status is excluded (meta-structural;
  use topic-plan instead).
- Execute: Generate the mock following the skill's golden prompt structure. Same generation
  protocol as mock-all but for one namespace.
- Findings: The mock artifact. Final line: `Next: /mock:review {topic} {this-file}` unless
  this was called from within a mock-review session to regenerate a thin namespace.
- Amend: Not applicable. Regenerate with adjusted `--skill` if the output is thin.

**Lightweight**: Single-pass. One namespace. No prompts.

**Artifact**: `simulations/mock/{topic}-{namespace}-mock-{date}.md`

**Tools**: Read, Write, Glob

**Example**:
```
User: /mock:ns frogs trace --skill trace-component
> Generating mock for trace/trace-component (topic: frogs)...

[MOCK ARTIFACT -- NOT VERIFIED]
Skill: trace-component
Topic: frogs
Category: HIGH-STRUCTURE
Date: 2026-03-15
Status: MOCK (awaiting review)
Flag: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

## Component Dependency Map (MOCK)
| Component | Type | Owner | Contracts | Risk |
|-----------|------|-------|-----------|------|
| Dynamics connector | External | Platform | CRM API v3 | HIGH |
| Salesforce adapter | External | Platform | REST API v53 | MEDIUM |
| Sync orchestrator | Internal | Team | event-bus | HIGH |

Gate: YELLOW -- two external dependencies with undocumented version pinning

> Artifact written: simulations/mock/frogs-trace-mock-2026-03-15.md
> Next: /mock:review frogs simulations/mock/frogs-trace-mock-2026-03-15.md
```

---

### /mock:review

**What**: Step 2 of the mock-first workflow. Review the coverage picture from `mock-all` or
`mock-ns` and produce explicit MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace.
This skill WRITES the annotation update -- it does not merely read and recommend.
The MOCK-ACCEPTED annotation only exists after `mock-review` runs; it is never set by
generation alone.

**Stock roles**: PM (coverage adequacy), Architect (structural quality), Strategy (tier
risk assessment)

**Input**: Topic (required). Mock artifact file path -- output from `mock-all` or `mock-ns`
(required). Optional: `--tier 1|2|3` (default: read from TOPICS.md, else 1).

**Output**: A coverage review artifact at `simulations/mock/{topic}-review-{date}.md` containing:
- Per-namespace review table (Namespace, Category, Mock Quality, Decision, Reason code)
- Decision for each namespace: MOCK-ACCEPTED (with reason code) or REAL-REQUIRED (with reason)
- Automatic REAL-REQUIRED for all EVIDENCE-HEAVY namespaces at any tier
- Automatic REAL-REQUIRED for trace, scout-feasibility, listen at Tier 2+
- Automatic REAL-REQUIRED for compliance-adjacent namespaces if compliance tags present
- "Next steps" list: which namespaces to run real skills for, in recommended priority order
- Updated Status annotations written back to the source mock artifact (the MOCK header Status
  field is updated from `MOCK (awaiting review)` to `MOCK-ACCEPTED` or `REAL-REQUIRED`)

**Lifecycle**:
- Setup: Read the specified mock artifact file. Parse the MOCK ARTIFACT header block from each
  namespace section. Read TOPICS.md for tier classification and compliance tags. Apply automatic
  flagging rules before review begins: EVIDENCE-HEAVY = REAL-REQUIRED; Tier 2/3 critical
  namespaces = REAL-REQUIRED; compliance-tagged = REAL-REQUIRED for compliance-adjacent.
- Execute: For each non-auto-flagged namespace (HIGH-STRUCTURE, MIXED, and Tier 1 only):
  - PM role: assess structural completeness (are required sections present? gates present?
    tables well-formed?)
  - Architect role: assess technical plausibility (does the mock content contradict known
    architectural facts about the topic?)
  - Strategy role: assess coverage adequacy (is this namespace covered well enough for the
    current decision tier?)
  - Record decision (MOCK-ACCEPTED or REAL-REQUIRED) and reason code(s).
- Findings: Write the coverage review artifact. Then update the source mock artifact's Status
  fields: for each namespace, replace `Status: MOCK (awaiting review)` with either
  `Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]`
  or `Status: REAL-REQUIRED [{reason}]`. The update is an in-place edit of the Status line only
  -- the only permitted exception to Signal's append-only principle, because the annotation is
  a property of the artifact being reviewed, not a new artifact.
- Amend: If a namespace decision is disputed, user can override by providing a specific reason.
  The override is recorded in the review artifact alongside the original decision.

**Lightweight**: Single-pass review. Automatic flagging rules applied first; PM/Architect/
Strategy evaluation applied to remaining namespaces. No iterative back-and-forth.

**Artifact**: `simulations/mock/{topic}-review-{date}.md`

**Tools**: Read, Write, Edit, Glob

**Example**:
```
User: /mock:review frogs simulations/mock/frogs-mock-2026-03-15.md --tier 2
> Reading mock artifact...
> Applying automatic rules for Tier 2...
>   trace: REAL-REQUIRED (critical namespace, Tier 2)
>   scout-feasibility: REAL-REQUIRED (critical namespace, Tier 2)
>   listen: REAL-REQUIRED (critical namespace, Tier 2)
>   prove (evidence-heavy): REAL-REQUIRED (evidence-heavy)
> Reviewing remaining namespaces...

## Coverage Review (frogs, Tier 2)

| Namespace | Category | Mock Quality | Decision | Reason |
|-----------|----------|-------------|----------|--------|
| scout | HIGH-STRUCTURE | Good -- feasibility table well-formed, gate present | REAL-REQUIRED | Critical namespace at Tier 2 |
| draft | HIGH-STRUCTURE | Good -- spec structure complete, all sections present | MOCK-ACCEPTED | STRUCTURAL-COVERAGE-SUFFICIENT |
| review | MIXED | Moderate -- challenge framework present, content generic | REAL-REQUIRED | Draft is VERIFIED needed first |
| flow | HIGH-STRUCTURE | Good -- resilience scenarios well-formed | MOCK-ACCEPTED | STRUCTURAL-COVERAGE-SUFFICIENT; DOMAIN-KNOWLEDGE-CONSISTENT |
| trace | HIGH-STRUCTURE | Good -- component map present | REAL-REQUIRED | Critical namespace at Tier 2 |
| prove | EVIDENCE-HEAVY | Structural only -- content fabricated | REAL-REQUIRED | Evidence-heavy |
| listen | EVIDENCE-HEAVY | Structural only -- content fabricated | REAL-REQUIRED | Evidence-heavy (critical at Tier 2) |
| program | HIGH-STRUCTURE | Good -- plan template well-formed | MOCK-ACCEPTED | STRUCTURAL-COVERAGE-SUFFICIENT |
| topic | HIGH-STRUCTURE | Planning only | MOCK-ACCEPTED | STRUCTURAL-COVERAGE-SUFFICIENT |

## Next Steps (priority order)
1. /scout:feasibility frogs -- critical namespace, Tier 2 gate
2. /trace:component frogs -- critical namespace, Tier 2 gate
3. /listen:support frogs -- critical namespace, adoption evidence
4. /prove:websearch frogs -- evidence required
5. /review:design frogs -- after draft is VERIFIED

> Annotations updated in: simulations/mock/frogs-mock-2026-03-15.md
> Review written: simulations/mock/frogs-review-2026-03-15.md
```

---

## Integration with topic-status

`topic-status` reads signal artifacts to compute a coverage score. For the mock-first workflow
to be safe in decision-bearing contexts, `topic-status` must distinguish VERIFIED, MOCK-ACCEPTED,
and UNVERIFIED signals. This is a hard implementation dependency (S4-02 R1, R2, R3).

**What topic-status must implement** before mock artifacts can be used in commitment decisions:

- **R1 -- Header reading**: For each signal artifact, read the MOCK ARTIFACT header block.
  An artifact with the header is MOCK or MOCK-ACCEPTED depending on the Status field value.
  An artifact without the header is VERIFIED.

- **R2 -- Three-state reporting**: Report namespace coverage as three counts: VERIFIED,
  MOCK-ACCEPTED, UNVERIFIED. The readiness verdict must distinguish total coverage (all states)
  from verified coverage (VERIFIED only).

- **R3 -- Tier-conditional thresholds**:
  - Tier 1: READY when total coverage (VERIFIED + MOCK-ACCEPTED) meets 4/9 minimum and no
    critical namespace is UNVERIFIED
  - Tier 2: READY when VERIFIED coverage includes all critical namespaces (trace, scout-feasibility,
    listen) and total coverage is 7/9+
  - Tier 3: READY when all 9 namespaces are VERIFIED and confidence exposure is below 20%

**Until R1/R2/R3 are implemented**, mock-first must be used as an orientation and coverage
planning tool only. Teams must not use `topic-status` readiness verdicts as commitment gates
when mock artifacts are present, because the tool cannot see the annotations and will treat
mock coverage as equivalent to verified coverage.

The `topic-status` spec should be updated to document this integration. A `topic-status` run
that finds mock artifacts with no annotation-reading implementation active should warn:
`Warning: {N} MOCK artifacts found. topic-status cannot distinguish mock from real coverage.
Readiness verdict is artifact-presence only. Run /mock:review before treating as commitment gate.`

---

## Workflow Example

The mock-first workflow end to end for topic `frogs` (Tier 2 feature):

**Step 1 -- Generate coverage picture**
```
/mock:all frogs --tier 2
```
- Produces: `simulations/mock/frogs-mock-2026-03-15.md`
- Contains 9 namespace sections, each annotated `Status: MOCK (awaiting review)`
- Evidence-heavy namespaces pre-flagged `REAL-REQUIRED (evidence-heavy)`
- Tier 2 critical namespaces pre-flagged in the coverage summary

Time: 1 LLM call, ~10-15 minutes including team read.

**Step 2 -- Review coverage picture**
```
/mock:review frogs simulations/mock/frogs-mock-2026-03-15.md --tier 2
```
- Produces: `simulations/mock/frogs-review-2026-03-15.md`
- Updates Status fields in the source mock artifact
- Result for frogs: 4 namespaces MOCK-ACCEPTED (draft, flow, program, topic), 5 REAL-REQUIRED

Time: Step 2 review ~20-30 minutes including team discussion of flagged namespaces.

**Step 3 -- Run targeted real skills (priority order)**
```
/scout:feasibility frogs
/trace:component frogs
/listen:support frogs
/prove:websearch frogs
/review:design frogs  (after draft is written)
```
- 5 real skill runs instead of 9 (or 12-15 for a full Tier 2 investigation)
- Each real skill run produces a VERIFIED artifact (no MOCK header)

Time: 5 real runs x ~5-10 minutes each = ~25-50 minutes.

**Step 4 -- Assess readiness**
```
/topic:status frogs
```
With R1/R2/R3 implemented:
- VERIFIED: 5 namespaces (scout, trace, listen, prove, review)
- MOCK-ACCEPTED: 4 namespaces (draft, flow, program, topic)
- UNVERIFIED: 0
- Readiness verdict: READY for Tier 2 (VERIFIED coverage includes all critical namespaces;
  total coverage is 9/9)

**Cost comparison**:
- Real-first (Tier 2, 9 namespaces): 12-15 real skill runs
- Mock-first (Tier 2, frogs): 1 mock pass + 5 real runs = 6 total operations
- Reduction: ~50-60% fewer real skill runs

---

## Design Decisions and Rationale

**D-01: Unified artifact for mock-all, not one-file-per-namespace**

The coverage picture's value is panoramic -- the team sees all 9 namespaces simultaneously.
Writing 9 separate files reduces the coverage assessment to sequential reading of individual
artifacts. The unified artifact enables relative assessment ("trace looks much stronger than
listen") that sequential individual files cannot provide. The cost is a larger single file.
This is acceptable: mock-all is read once in Step 2, not repeatedly over time.

**D-02: mock-review WRITES annotations, not merely recommends**

S4-02 R1 specifies that `topic-status` must read annotations to distinguish VERIFIED from
MOCK-ACCEPTED. For that reading to be possible, the annotation must exist in the artifact.
A `mock-review` that only produces a review document but does not update the source mock
artifact's Status fields forces teams to manually propagate the review decision -- which
is exactly the failure mode (MOCK silently treated as coverage) the workflow is designed
to prevent. Writing the annotation is the mechanism that makes the three-state model
machine-readable.

The in-place edit of the Status line is the only planned exception to Signal's P-02
(Append-Only Artifacts) principle. The justification: the Status field is a property of
the artifact whose truth value changes as the review process proceeds. A new artifact
cannot represent this -- it would leave the original mock artifact's Status field in the
misleading `MOCK (awaiting review)` state while a separate review artifact records the
real decision. Downstream tools (including `topic-status`) read the artifact itself, not
a separate review document.

**D-03: Automatic flagging for evidence-heavy and critical namespaces**

Teams should not need to remember the skill category taxonomy or the Tier 2/3 critical
namespace list. These are stable rules derived from S4-01 and S3-02 respectively. Building
them into `mock-review`'s automatic flagging removes a cognitive burden from Step 2 and
prevents the most dangerous failure mode (Section 7.1 of S4-03): treating a fluent
evidence-heavy mock as MOCK-ACCEPTED because it looks plausible. The rule is structural:
evidence-heavy = real run required, regardless of mock quality.

**D-04: Category embedded in each artifact header, not just in docs**

The skill category (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED) is embedded in every mock
artifact header. This prevents the failure mode where a team opens a mock artifact days
after generation and has lost context about whether its content should be trusted. The
category annotation is a persistent structural property of the artifact, not a
documentation note.

**D-05: Compliance pre-flagging from TOPICS.md tags**

Compliance-sensitive features require VERIFIED signals for compliance-adjacent namespaces
at all tiers (S4-03 Section 5.4). Relying on team judgment to apply this rule in Step 2
is insufficient -- a team might not remember the compliance tag when reviewing a
structurally well-formed mock compliance artifact. Reading the compliance tags from
TOPICS.md and pre-flagging those namespaces before the team's Step 2 review enforces the
absolute compliance condition at the tool level.

**D-06: mock namespace is outside the 9 investigation namespaces**

The `/mock:` namespace is an infrastructure namespace, not an investigation namespace. Its
artifacts live in `simulations/mock/` rather than `simulations/{namespace}/{skill}/`. Mock
artifacts are not signals toward a topic's story -- they are structural previews that are
superseded by the real skill runs they inform. `topic-status` should count real VERIFIED
artifacts and MOCK-ACCEPTED artifacts per namespace; it should not count mock artifacts
from the mock directory as independent signals.

**D-07: quest_status DESIGNED, not GOLDEN**

The 3 mock skills are new skills without quest history. They are designed from the S4-03
paper's requirements but have not been quested (no golden prompt, no rubric, no scored
runs). The quest_status is DESIGNED to reflect this. The skills are runnable but their
prompt quality has not been validated through the quest loop. A quest campaign for
mock-all, mock-ns, and mock-review should be run once the skill namespace is deployed
and initial real runs have produced outputs to score.

---

## Fidelity Warnings

These warnings appear in every mock artifact and in the mock-review output. They are not
optional boilerplate -- they are the workflow's safety mechanism.

**For EVIDENCE-HEAVY namespaces**:
```
WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally correct but
evidentially fabricated. Do not use this output to draw conclusions about {topic}. The
sections are right; the contents are invented. A real {skill-id} run is required before
any evidence-based decision can be made from this namespace.
```

**For MIXED namespaces**:
```
CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement mechanisms)
are reliable. Specific claims (competitor names, market data, research findings) may be
partially accurate (well-known facts from training data) or partially fabricated (recent,
proprietary, or domain-specific claims). Review for plausibility before accepting coverage.
```

**For HIGH-STRUCTURE namespaces**:
```
NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement mechanisms
are reliable. Content is synthetically generated but structurally representative. Adequate
for structural planning and coverage orientation at Tier 1. REAL-REQUIRED at Tier 2+ for
critical namespaces (trace, scout-feasibility, listen).
```
