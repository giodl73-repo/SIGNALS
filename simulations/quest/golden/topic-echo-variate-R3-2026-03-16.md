---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 3
rubric: v3
rubric_max: 120
---

# Variations: `topic:echo` -- Round 3

**Rubric:** v3 | **Date:** 2026-03-16

---

## Design Context

R2 established the C-11/C-12 infrastructure: a discrete Prior Belief Inventory (PBI)
with addressable entries, and named handles per surprise. R2 V-04/V-05 reached the
golden threshold (all essential + composite >= 80) by satisfying C-11 and C-12 alongside
the essential and recommended criteria.

v3 adds two new aspirational criteria built on top of C-11 and C-12:

**C-13 -- Dual phase-locked pre-commitment integrity**: The PBI and Handle Ledger must be
genuinely independent -- produced with different information at different temporal positions.
Independence fails if a PBI entry names a handle label by its final form (handle was
predictable at PBI time) or if a handle echoes PBI entry language verbatim (handle was
constructed by inverting a prediction, not naming a finding). The test is content-based:
PBI entries use belief language about domain expectations; handle titles use finding
language specific to what signals revealed.

**C-14 -- Single-entry audit trail completeness**: Each surprise entry must carry all three
pointers -- Handle Ledger title, PBI identifier, source signal artifact -- so a reviewer
can verify the full provenance chain from a single entry without navigating to other sections.
An entry missing any one of the three pointers fails.

C-13 and C-14 are gated: they are only applicable when both C-11 and C-12 pass.

**Gap analysis:**

The R2 prompt (best performer) structured the PBI and handles correctly but did not enforce
temporal independence. Both sections could have been written together after reading signals
("post-hoc alignment"). C-13 requires evidence of genuine phase separation. Separately, R2
entries carried the handle and source signal, but PBI-ref was omitted from individual entries
(it lived only in the PBI section). C-14 requires all three pointers in every entry.

**Variation axes selected for R3:**

1. **Lifecycle emphasis** -- explicit two-phase gate (Phase 1: commit PBI before signals;
   Phase 2: read signals and extract surprises). Targets C-13 by making temporal separation
   a structural constraint in the workflow, not a discipline requirement.

2. **Output format** -- mandatory triple-pointer entry schema (Handle + PBI-Ref + Source as
   required fields in every surprise entry). Targets C-14 by making all three pointers
   enforced columns, not optional prose elements.

3. **Role sequence** -- Archivist-first (a dedicated role commits the PBI from domain
   reasoning before any reading role opens a signal artifact). Targets C-13 via role
   boundary enforcement: the Archivist literally cannot know the signal content because
   they run before signals are read.

**Variation plan:**

| Variation | Primary axes | Hypothesis |
|-----------|-------------|------------|
| V-01 | Lifecycle emphasis only | Phase gate alone is sufficient to produce PBI/handle independence (C-13) |
| V-02 | Output format only | Triple-pointer entry schema alone produces all-three-pointer entries (C-14) |
| V-03 | Role sequence only | Archivist-first role separation enforces C-13 independence without lifecycle gating |
| V-04 | Lifecycle + Output format | Combined structural enforcement hits C-13 + C-14 without dedicated roles |
| V-05 | Lifecycle + Output format + Role sequence | Full synthesis: all three axes. Gold standard for v3 |

**Discriminating pairs:**

- V-01 vs V-02: C-13 isolation vs C-14 isolation; tests which new criterion is harder to hit alone
- V-01 vs V-03: lifecycle gate vs role boundary; tests alternative mechanisms for C-13
- V-02 vs V-04: whether lifecycle adds value over format alone for C-14
- V-03 vs V-05: whether format axis adds value over role sequence alone
- V-04 vs V-05: isolates the marginal value of dedicated Archivist role when lifecycle + format are already active

---

## V-01 -- Single-axis: Lifecycle Emphasis (Explicit Two-Phase Gate)

**Variation axis:** Lifecycle emphasis. The skill is divided into two named phases with
an explicit gate between them. Phase 1 (Pre-Signal Commitment) runs before any signal
artifacts are opened. The model must produce and commit the Prior Belief Inventory during
Phase 1. Only after explicitly declaring Phase 1 complete does Phase 2 (Signal Reading and
Surprise Extraction) begin. The phase boundary is named and enforced by the prompt
structure.

**Hypothesis:** R2 prompts asked for a PBI section but did not separate signal reading from
PBI creation into distinct workflow phases. A model following R2 could write the PBI and
read signals in the same cognitive pass, then construct "expected" states that fit the
findings. C-13 requires evidence of genuine temporal independence. When the prompt makes
Phase 1 a hard stop -- requiring committed PBI output before Phase 2 begins -- the model
cannot construct PBI entries from signal knowledge. The phase gate itself is the
independence evidence. C-14 is not directly targeted (no triple-pointer schema), so
per-entry audit completeness will depend on model discipline.

**C-12 status:** Named handles required. Handle Ledger as a separate section. C-12
baseline from R2 is preserved.

**C-14 status:** Not structurally enforced. PBI-ref appears in PBI section; individual
entries must cite it but no schema column forces the pointer. This is the discriminator
between V-01 and V-04.

---

### Prompt Body

```
## topic:echo

Ask one question: what did we learn that we did not expect?

This is not a summary of signals. Every entry in the output is a surprise -- a finding
that departed from what the team believed before the investigation. Expected findings
are excluded. The artifact is institutional memory for the next team.

**Input:** `{topic}` -- the topic name.

---

## Phase 1: Pre-Signal Commitment

**Rule: Do not open or read any signal artifact during Phase 1.**

### Step 1 -- Signal inventory (by name only)

Glob `simulations/` for files matching `*{topic}*`. List the file paths grouped by
namespace directory. Do not open any file. Note: how many namespaces have coverage?
Which are absent?

### Step 2 -- Prior Belief Inventory (PBI)

Before reading signals, commit what the team believed about this topic before gathering
evidence. Draw from the topic name, the namespace coverage pattern, and general domain
reasoning. Write priors in belief language -- what you expected, assumed, or treated as
settled before seeing any signal.

Write a section titled `## Prior Belief Inventory` containing 4--8 entries.

Each entry format:
```
PB-NN: [Belief statement in expectation language]
       "We expected ...", "We assumed ...", "We believed ..."
```

Requirements:
- Use domain expectation language, not finding language
- Entries must be statements about what the team believed BEFORE signal reading
- Do not use handle names (you have not read signals yet; handles do not exist)
- Entries are addressable by identifier (PB-01, PB-02, ...) -- each surprise will cite one

### Step 3 -- Phase gate

Write: "Phase 1 complete. PBI is frozen at {timestamp}. Opening signal artifacts now."

Do not revise the PBI after this point.

---

## Phase 2: Signal Reading and Surprise Extraction

### Step 4 -- Read signals

Open each artifact identified in Step 1. For each artifact, note:
- Namespace and artifact name
- Key findings

Do not filter yet -- note everything found.

### Step 5 -- Surprise identification

A surprise is a finding that meaningfully departed from a PBI entry. Apply the test:
"If the team had read the PBI before reading this artifact, would this finding have
registered as unexpected?" Only findings that pass this test are surprises.

For each candidate surprise, identify:
- Which PBI entry it departs from (by identifier: PB-NN)
- What the PBI entry said (the prior belief)
- What the signal found (the actual finding)
- Why the departure is non-trivial

Discard findings that merely elaborate on beliefs that proved correct. Discard generic
observations not specific to this topic's signal set.

### Step 6 -- Named handles

Assign each surprise a handle: 2--5 words, specific to this investigation.

Handle test: could a teammate say "remember the [handle] surprise?" and be unambiguously
understood by everyone who read the echo -- without re-reading it? If the handle could
appear in any investigation, it is too generic. Rewrite until it names the specific finding.

FAIL: "competitor-advantage surprise" -- applies universally
PASS: "scout-found-all-incumbents-treat-X-as-solved" -- names the specific finding

### Step 7 -- Handle Ledger

Write a section titled `## Handle Ledger` listing each surprise:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

This section must appear before the surprise entries.

### Step 8 -- Expectation counterfactual per entry

For each surprise, write the departure explicitly:
- Expected (from PBI): [quote or close paraphrase of the PBI entry]
- Found: [what the signal actually showed]

A reader new to the topic must be able to reconstruct the prior assumption from this
entry alone, without consulting the PBI section.

### Step 9 -- Design impact per surprise

Every surprise carries an explicit impact assessment. Impact categories:
- Confirming: validates a current design decision (name the decision)
- Redirecting: changes a specific design decision (name what changes and to what)
- Destabilizing: reopens a previously closed question (name the question)

"This changes things" without naming what changes fails.

### Step 10 -- Cross-signal patterns

Examine the full surprise set. Do two or more surprises share an underlying cause or
implication? Name the pattern and state what it implies for design. If the surprises
are genuinely independent, state this explicitly with a rationale (not just "they are
unrelated").

### Step 11 -- Surprise ranking

Rank all surprises by design impact from highest to lowest. Argue the ranking: name
the load-bearing decision each surprise affects and explain why the top surprise
outranks the others. A ranked list without argument fails.

### Step 12 -- Risk escalation

Flag the single surprise most likely to invalidate a core assumption. State:
- The assumption at risk
- The signal artifact that revealed the threat
- What would need to be true for the assumption to hold despite the surprise

### Step 13 -- Institutional forward

Write a closing section addressed to the next team. Name what they should investigate
first given these surprises. Frame the surprises as "things you would not predict from
reading today's materials."

---

## Output Artifact

Write the echo to `simulations/topic/echo/{topic}-echo-{date}.md` with this structure:

1. Frontmatter: `skill: topic-echo`, `topic: {topic}`, `date: {date}`
2. `## Prior Belief Inventory` (reproduced verbatim from Phase 1 -- do not revise)
3. `## Handle Ledger` (handle | PBI-ref | source per surprise)
4. `## Surprises` -- one subsection per surprise, each containing:
   - Handle (must match Handle Ledger entry exactly)
   - PBI-Ref (must match a PBI entry identifier)
   - Source: {artifact name}
   - Expected: [prior belief statement]
   - Found: [actual finding]
   - Design impact: [confirming|redirecting|destabilizing] -- [named decision/question]
5. `## Cross-Signal Patterns`
6. `## Surprise Ranking` (with argued rationale)
7. `## Risk Escalation`
8. `## Institutional Forward`
```

---

## V-02 -- Single-axis: Output Format (Triple-Pointer Entry Schema)

**Variation axis:** Output format. Every surprise entry is a structured record with
mandatory fields. Three of the fields are the audit pointers required by C-14: Handle
(matching the Handle Ledger), PBI-Ref (citing a specific PBI entry by identifier), and
Source (naming the specific signal artifact). The entry schema makes omitting any pointer
a structural violation -- there is no "prose embedding" path where a pointer can be
implied rather than named. The Handle Ledger is a separate section that the entry
schema cross-references.

**Hypothesis:** R2 entries carried the handle and source signal in prose but did not
include the PBI-Ref as a required field in individual entries. A model following R2
might write "this surprised us given our prior assumption about X" without citing
PB-NN explicitly. When the entry schema has `PBI-Ref:` as a labeled field with a
validation requirement ("must match a PBI entry identifier"), the model cannot omit it
without violating the schema. C-14 is satisfied by the schema constraint, not model
discipline. C-13 is not structurally enforced (no phase gate) -- the PBI and handles
could theoretically be co-constructed.

**C-13 status:** Not structurally enforced. PBI is required, but no temporal separation
is mandated. This is the discriminator between V-02 and V-04.

**C-11 status:** PBI required as a discrete labeled section with addressable entries.
Baseline from R2 preserved.

---

### Prompt Body

```
## topic:echo

Ask one question: what did we learn that we did not expect?

This is not a summary of signals. Every entry in the output is a surprise. Expected
findings are excluded. The artifact is institutional memory for the next team.

**Input:** `{topic}` -- the topic name.

---

## Step 1 -- Signal inventory

Glob `simulations/` for files matching `*{topic}*`. List all matching artifact paths
grouped by namespace. Note which namespaces have coverage and which are absent.

## Step 2 -- Prior Belief Inventory (PBI)

Before reading any signal artifact, commit the beliefs the team held about this topic
before the investigation. Write them in belief language -- what was expected, assumed,
or treated as settled.

Write section `## Prior Belief Inventory` with 4--8 entries:

```
PB-NN: [Belief in expectation language: "We expected...", "We assumed...", "We believed..."]
```

Entries must be addressable by identifier (PB-01, PB-02, ...). Each surprise entry will
cite one PBI entry by this identifier.

## Step 3 -- Read signals

Open each artifact. For each, note: what was found, whether it confirmed or departed
from any PBI entry.

## Step 4 -- Surprise identification

A surprise is a finding that meaningfully departed from a PBI entry. Apply the filter:
only findings that would have registered as unexpected to someone who had read the PBI
first. Discard findings that elaborated on correct beliefs. Discard generic observations.

## Step 5 -- Named handles

Assign each surprise a handle: 2--5 words, specific to this investigation. Test: can
a teammate cite it by name ("remember the [handle]?") without re-reading the echo and
be unambiguously understood? Generic handles fail. Rewrite until the handle names the
specific finding.

## Step 6 -- Handle Ledger

Write section `## Handle Ledger` before the surprise entries:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

Every surprise must have a ledger entry. The ledger is the index; the surprise entries
are the bodies.

## Step 7 -- Surprise entries

Write each surprise as a structured record. All fields are required. Omitting any
field is a structural violation.

```
### {handle}

Handle:    {2--5 word handle, must match Handle Ledger entry exactly}
PBI-Ref:   PB-NN (must match an identifier from the Prior Belief Inventory)
Source:    {artifact name -- the specific signal file that produced this finding}
Expected:  {Prior belief statement -- quote or close paraphrase of the PBI-Ref entry}
Found:     {Actual finding from the Source artifact}
Departure: {Why the finding was surprising -- what the expected/found gap means}
Impact:    {confirming|redirecting|destabilizing} -- {named decision or question affected}
```

Validation: a reviewer reading only this entry must be able to verify three things
without navigating elsewhere: (1) the handle exists in the Handle Ledger, (2) the
prior belief exists in the PBI at PB-NN, (3) the finding exists in the named Source
artifact. All three checks must be possible from the entry alone.

## Step 8 -- Cross-signal patterns

Examine all surprise entries. If two or more share an underlying cause or implication,
name the pattern and state what it implies for design. If all surprises are independent,
state this explicitly with a brief rationale.

## Step 9 -- Surprise ranking

Rank all surprises by design impact, highest to lowest. Argue each ranking position:
name the load-bearing decision affected and explain why it outranks those below. A
sorted list without argument fails.

## Step 10 -- Risk escalation

Flag the single surprise most likely to invalidate a core assumption. Name:
- The assumption at risk
- The Source artifact that revealed the threat
- What would need to be true for the assumption to hold despite the surprise

## Step 11 -- Institutional forward

Address the next team directly. Name what to investigate first given these surprises.
Frame the echo as "things you would not predict from reading today's materials."

---

## Output artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter
2. `## Prior Belief Inventory`
3. `## Handle Ledger`
4. `## Surprises` (structured records per Step 7 -- all fields required)
5. `## Cross-Signal Patterns`
6. `## Surprise Ranking`
7. `## Risk Escalation`
8. `## Institutional Forward`
```

---

## V-03 -- Single-axis: Role Sequence (Archivist-First)

**Variation axis:** Role sequence. Three sequential roles run in order, each with an
explicit scope boundary. The Archivist commits the Prior Belief Inventory from domain
knowledge before any signal is mentioned. The Signal Reader reads artifacts and
extracts findings without referencing the PBI. The Echo Author receives both outputs
and synthesizes the surprises by comparing them. The role boundary between Archivist
and Signal Reader is the independence evidence for C-13: the Archivist literally cannot
incorporate signal content because signals have not been read yet; the Signal Reader
literally cannot rationalize findings against prior beliefs because no prior beliefs
have been surfaced.

**Hypothesis:** R2 produced the PBI and handles in the same workflow pass, so a model
could co-construct them. The role boundary creates the same cognitive separation humans
need: the Archivist speaks only from domain intuition; the Signal Reader speaks only from
what the artifacts say. When the Echo Author compares them, the independence is structural,
not rhetorical. C-13 is satisfied because the two sections were produced by roles that
could not share information. C-14 is not structurally enforced (no triple-pointer schema)
-- the Echo Author must include all three pointers per entry through instruction, not schema.

**C-14 status:** Not structurally enforced. Entry format requires Handle, PBI-Ref, and
Source, but as named fields in a prose record rather than mandatory schema columns with
a validation rule. This is the discriminator between V-03 and V-05.

---

### Prompt Body

```
## topic:echo

Ask one question: what did we learn that we did not expect?

Not a summary of signals. Every entry is a surprise. Expected findings are excluded.
The artifact is institutional memory for the next team.

**Input:** `{topic}` -- the topic name.

Three roles execute in sequence. Each role has a hard scope boundary.

---

## Role 1: Archivist

**Scope: Domain knowledge only. No signal artifacts. No file reads.**

The Archivist records what the team believed about this topic before the investigation
began. This role speaks from domain intuition, prior experience, and general reasoning
about the topic area -- not from evidence.

### Archivist Step 1 -- Name the signal set (by pattern only)

State which namespaces likely have coverage for this topic based on the topic name alone.
Do not glob or list files. This is informed estimation, not discovery.

### Archivist Step 2 -- Prior Belief Inventory

Write section `## Prior Belief Inventory` with 4--8 entries using belief language:

```
PB-NN: [What the team expected, assumed, or treated as settled before investigation]
       Language: "We expected...", "We assumed...", "We believed..."
```

Requirements:
- Belief language only (expectation, assumption, prior conviction)
- No finding language (discovery, revealed, showed)
- No handle names (handles do not exist until the Signal Reader runs)
- Entries are addressable by identifier (PB-01, PB-02, ...)

### Archivist Step 3 -- Commit and close

Write: "Archivist complete. PBI is frozen. Signal Reader begins now."

The Archivist's output is the PBI section. It is not revised after this point.

---

## Role 2: Signal Reader

**Scope: Signal artifacts only. Do not reference the PBI.**

The Signal Reader reads the evidence without being anchored to the Archivist's priors.
This produces findings that are genuinely independent of the stated beliefs.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for files matching `*{topic}*`. List all matching artifacts by
namespace.

### Signal Reader Step 2 -- Read

Open each artifact. For each, note: namespace, artifact name, key findings. Extract
the content faithfully -- do not filter yet.

### Signal Reader Step 3 -- Finding summary

Write section `## Signal Findings` listing each artifact and its key findings.
This section is the raw input the Echo Author will use.

### Signal Reader Step 4 -- Close

Write: "Signal Reader complete. Echo Author begins now."

---

## Role 3: Echo Author

**Scope: Both Archivist output and Signal Reader output. Synthesizes surprises.**

The Echo Author receives the PBI (from Archivist) and the signal findings (from Signal
Reader). The Echo Author's job is to identify departures: findings that meaningfully
contradicted PBI entries.

### Echo Author Step 1 -- Surprise identification

For each signal finding, compare it to the PBI. A surprise is a finding where the
actual outcome meaningfully departed from what PB-NN said. Apply the test: "Would a
team member who had read the PBI before reading this signal have been surprised?"

Discard findings that confirmed or merely elaborated on beliefs that proved correct.
Discard generic observations not specific to this topic.

### Echo Author Step 2 -- Named handles

Assign each surprise a handle: 2--5 words, specific enough to be cited by a future
artifact. The handle names what was found, not what was expected. Test: could it appear
in any investigation? If yes, rewrite it.

Handles use finding language. They must not echo PBI entry language verbatim (that
would indicate the surprise entry was constructed by inverting a prediction, not by
naming a finding).

### Echo Author Step 3 -- Handle Ledger

Write section `## Handle Ledger`:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

### Echo Author Step 4 -- Surprise entries

For each surprise write a record with these named fields (all required):

```
### {handle}

Handle:   {handle -- must match Handle Ledger entry}
PBI-Ref:  PB-NN {must match a PBI entry identifier from the Archivist's section}
Source:   {artifact name from the Signal Reader's section}
Expected: {PBI entry statement -- what the Archivist committed before signals}
Found:    {Signal finding -- what the Reader found in the source artifact}
Impact:   {confirming|redirecting|destabilizing} -- {name the affected decision or question}
```

All three audit pointers (Handle, PBI-Ref, Source) must appear in the entry. A reviewer
reading one entry must be able to verify: handle in ledger, PBI entry exists, source
artifact named.

### Echo Author Step 5 -- Cross-signal patterns

Do two or more surprises share an underlying cause? Name it and state the design
implication. If independent, state this explicitly with rationale.

### Echo Author Step 6 -- Surprise ranking

Rank by design impact. Argue each position by naming the load-bearing decision affected.

### Echo Author Step 7 -- Risk escalation

Flag the riskiest surprise. Name: assumption at risk, source signal, survival condition.

### Echo Author Step 8 -- Institutional forward

Address the next team. What should they investigate first, given these surprises?
Frame as "things you would not predict from reading today's materials."

---

## Output Artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter
2. `## Prior Belief Inventory` (Archivist output -- verbatim)
3. `## Signal Findings` (Signal Reader output -- compressed to essentials)
4. `## Handle Ledger` (Echo Author)
5. `## Surprises` (structured records -- all fields required)
6. `## Cross-Signal Patterns`
7. `## Surprise Ranking`
8. `## Risk Escalation`
9. `## Institutional Forward`
```

---

## V-04 -- Combined: Lifecycle Emphasis + Output Format

**Variation axes:** Lifecycle emphasis (V-01) + Output format (V-02). Combines the
two-phase workflow gate with the mandatory triple-pointer entry schema. Phase 1 commits
the PBI before signals are opened, enforcing temporal independence (C-13). The entry
schema mandates Handle + PBI-Ref + Source as required fields in every surprise record,
enforcing per-entry audit completeness (C-14). No dedicated roles -- the workflow
structure does the work.

**Hypothesis:** V-01 targets C-13 but leaves C-14 to model discipline. V-02 targets
C-14 but leaves C-13 to model discipline. Combining both should hit both criteria
without requiring role machinery. The phase gate provides the independence evidence;
the schema provides the pointer completeness. The question is whether phase + schema
together are sufficient, or whether role separation (V-03) adds additional reliability
for C-13 that the phase gate alone cannot provide.

**C-13 prediction:** The phase gate creates the temporal separation evidence. Risk: a
model could write PBI entries that "anticipate" handle concepts (pre-loading specific
findings into expectation language). The gate is a workflow boundary, not an information
boundary -- the model has access to its own prior reasoning. Role separation (V-03) adds
an information boundary on top of the workflow boundary.

**C-14 prediction:** The entry schema with `PBI-Ref:` as a required labeled field
should make omission nearly impossible. High confidence.

---

### Prompt Body

```
## topic:echo

Ask one question: what did we learn that we did not expect?

Not a summary of signals. Every entry is a surprise. Expected findings are excluded.
The artifact is institutional memory for the next team.

**Input:** `{topic}` -- the topic name.

---

## Phase 1: Pre-Signal Commitment

**Rule: No signal artifacts may be opened during Phase 1.**

### Step 1 -- Inventory (names only)

Glob `simulations/` for paths matching `*{topic}*`. List the file paths by namespace.
Do not open any file. Note how many namespaces have coverage; note which are absent.

### Step 2 -- Prior Belief Inventory

Commit the beliefs held before the investigation. Write in belief language only.
Draw from the topic name, namespace coverage pattern, and domain reasoning.

Write section `## Prior Belief Inventory` with 4--8 entries:

```
PB-NN: [Expectation statement: "We expected...", "We assumed...", "We believed..."]
```

Requirements:
- Belief language only -- not finding language
- No handle names -- handles do not exist until Phase 2
- Entries addressable by identifier (PB-01, PB-02, ...)

### Step 3 -- Phase gate

Write: "Phase 1 complete. PBI is frozen. Beginning Phase 2: signal reading."

**Do not revise the PBI after this point.**

---

## Phase 2: Signal Reading and Surprise Extraction

### Step 4 -- Read signals

Open each artifact identified in Step 1. For each, extract key findings. Note the
exact artifact name -- this becomes the Source pointer in surprise entries.

### Step 5 -- Surprise identification

A surprise is a finding that meaningfully departed from a PBI entry. Test: would
someone who read the PBI before this artifact have been surprised? Discard confirmations.
Discard generic observations not specific to this topic.

For each surprise, identify: which PBI entry it departs from (by identifier), what
the PBI said, what the signal showed.

### Step 6 -- Named handles

Assign each surprise a handle: 2--5 words, specific to this investigation. Handle uses
finding language (what was discovered), not belief language (what was expected). Test:
is it unique to this investigation? Could it appear in any echo? If yes, rewrite.

### Step 7 -- Handle Ledger

Write section `## Handle Ledger` before surprise entries:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

### Step 8 -- Surprise entries

Every surprise is a structured record. All fields are required. A record missing any
field is incomplete and must be corrected before the artifact is written.

```
### {handle}

Handle:    {must match Handle Ledger entry exactly}
PBI-Ref:   PB-NN  {must match an identifier from ## Prior Belief Inventory}
Source:    {artifact name -- the specific file that produced this finding}
Expected:  {Prior belief -- from PBI-Ref entry, quoted or closely paraphrased}
Found:     {Actual finding -- from the Source artifact}
Departure: {Why the gap between Expected and Found constitutes a surprise}
Impact:    {confirming|redirecting|destabilizing} -- {named decision or question}
```

Self-check before writing: can a reviewer verify all three audit pointers from this
entry alone -- (1) handle in Handle Ledger, (2) PBI entry at PB-NN, (3) finding in
Source artifact -- without navigating to other sections? If not, add missing pointers.

### Step 9 -- Cross-signal patterns

Examine all surprises. Do two or more share an underlying cause or implication? Name
the pattern; state the design implication. If independent, state this explicitly with
rationale.

### Step 10 -- Surprise ranking

Rank all surprises by design impact. Argue the ranking: name the load-bearing decision
each surprise affects; explain why the top surprise outranks those below.

### Step 11 -- Risk escalation

Flag the single riskiest surprise. State: assumption at risk, Source artifact that
revealed the threat, what would need to be true for the assumption to survive.

### Step 12 -- Institutional forward

Address the next team. Name what to investigate first given these surprises. Frame the
echo as "things you would not predict from reading today's artifacts."

---

## Output artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter
2. `## Prior Belief Inventory` (Phase 1 output -- verbatim, no revision)
3. `## Handle Ledger`
4. `## Surprises` (all fields required per Step 8 schema)
5. `## Cross-Signal Patterns`
6. `## Surprise Ranking`
7. `## Risk Escalation`
8. `## Institutional Forward`
```

---

## V-05 -- Full Synthesis: Lifecycle + Output Format + Role Sequence

**Variation axes:** All three. The Archivist commits the PBI before signals are named
(role boundary + lifecycle phase). The Signal Reader reads artifacts without PBI
context. The Echo Author compares both outputs using a mandatory triple-pointer entry
schema. The role boundary provides the information separation evidence for C-13. The
entry schema provides the structural enforcement for C-14. The Handle Ledger is a
separate named section cross-referenced from entry fields.

**Hypothesis:** V-04 uses phase gating as the C-13 independence evidence, but the
model has access to its own prior reasoning across phases. The Archivist role adds an
information boundary: the Archivist scope is explicitly "no signal artifacts, no file
reads," so PBI entries cannot anticipate specific findings because no findings have
been extracted yet. Handles emerge from the Echo Author's synthesis -- they are named
in finding language after signals have been read, and are structurally unavailable to
the Archivist. The combination of role information boundary (C-13) and entry schema
with required pointer fields (C-14) is the strongest achievable enforcement of both
new aspirational criteria.

**Excellence signal being tested:** Can a prompt that enforces all six aspirational
criteria through structure (rather than instruction and discipline) achieve 100+ composite
on the v3 rubric? V-05 is the gold standard answer.

---

### Prompt Body

```
## topic:echo

Ask one question: what did we learn that we did not expect?

Not a summary of signals. Every entry is a surprise. Expected findings are excluded.
The artifact is institutional memory for the next team.

**Input:** `{topic}` -- the topic name.

Three roles execute in sequence. Each has a hard scope boundary. Role transitions are
explicit. No role may access information outside its scope.

---

## Role 1: Archivist

**Scope:** Domain knowledge and topic name only. No file reads. No signal artifacts.
No signal content of any kind.

The Archivist speaks from intuition, prior experience, and domain reasoning. The PBI
records the team's belief state before any evidence was gathered.

### Archivist Step 1 -- Namespace estimate

Based on the topic name only, estimate which Signal namespaces (scout, draft, review,
flow, trace, prove, listen, program, topic) likely have coverage. State the estimate
but do not verify -- that is the Signal Reader's job.

### Archivist Step 2 -- Prior Belief Inventory

Write section `## Prior Belief Inventory` with 4--8 entries:

```
PB-NN: [Belief statement in expectation language]
       "We expected...", "We assumed...", "We believed..."
```

Constraints enforced by this role's scope:
- Belief language only (expected, assumed, believed -- not found, revealed, showed)
- No handle names. Handles are finding-language labels assigned after signal reading.
  At Archivist time, signals have not been read. Handles do not exist.
- No specific artifact references. The Archivist does not know what was found.
- Entries are addressable by identifier (PB-01, PB-02, ...)

### Archivist Step 3 -- Freeze

Write: "Archivist complete. PBI frozen. Signal Reader begins."

---

## Role 2: Signal Reader

**Scope:** Signal artifacts only. The PBI exists but this role does not reference it.
Findings are extracted independently of the stated beliefs.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for paths matching `*{topic}*`. List all artifact paths by
namespace.

### Signal Reader Step 2 -- Read

Open each artifact. For each, extract key findings. Record the exact artifact filename
-- this becomes the Source pointer in surprise entries.

### Signal Reader Step 3 -- Findings register

Write section `## Signal Findings` listing each artifact with its key findings:

```
**{artifact-name}** ({namespace}):
- {finding 1}
- {finding 2}
...
```

This section is the Signal Reader's complete output. The Echo Author will use it as
the finding-side input.

### Signal Reader Step 4 -- Close

Write: "Signal Reader complete. Echo Author begins."

---

## Role 3: Echo Author

**Scope:** Both the Archivist's PBI and the Signal Reader's findings register.
Synthesizes surprises by comparing the two independent outputs.

### Echo Author Step 1 -- Surprise identification

For each finding in the Signal Findings register, compare it to every PBI entry.
A surprise is a finding that meaningfully departed from what PB-NN stated.

Test: "Would a team member who read only the PBI and then read this signal finding
have been surprised?" Discard confirmations. Discard generic observations not
falsifiable against this topic's specific artifacts.

For each surprise, note: which PBI-Ref (PB-NN), which Source artifact, what the
expected state was, what the found state was.

### Echo Author Step 2 -- Named handles

Assign each surprise a handle: 2--5 words in finding language. Handles name what
was discovered, not what was expected.

Independence test for C-13: does the handle echo PBI entry language verbatim? If yes,
the handle was constructed by inverting a prediction rather than naming a finding --
rewrite it in finding language specific to what the signals showed.

Specificity test for C-12: could this handle appear in any investigation? If yes,
it is too generic -- rewrite until it names the specific finding.

### Echo Author Step 3 -- Handle Ledger

Write section `## Handle Ledger`:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

One row per surprise. The ledger is the index; the surprise entries are the bodies.

### Echo Author Step 4 -- Surprise entries

Each surprise is a structured record with all fields required. Missing any field is
a structural error.

```
### {handle}

Handle:    {2--5 word handle -- must match Handle Ledger row exactly}
PBI-Ref:   PB-NN  {must match an identifier from ## Prior Belief Inventory}
Source:    {artifact name -- must appear in ## Signal Findings}
Expected:  {PBI entry at PB-NN -- quoted or closely paraphrased from Archivist output}
Found:     {Finding from Source artifact -- from Signal Reader output}
Departure: {Why Expected vs Found constitutes a non-trivial surprise}
Impact:    {confirming|redirecting|destabilizing} -- {named design decision or question}
```

Self-check (required before writing the artifact):
A reviewer reading only this entry must be able to verify:
1. Handle exists in ## Handle Ledger
2. PBI-Ref entry exists in ## Prior Belief Inventory at the named identifier
3. Source artifact appears in ## Signal Findings with the finding stated

All three verifications must be possible from the entry alone. If any pointer is
missing or unverifiable, the entry is incomplete -- add the missing pointer.

### Echo Author Step 5 -- Cross-signal patterns

Examine all surprise entries. If two or more share an underlying cause or implication,
name the pattern explicitly and state what it implies for design direction. If the
surprises are genuinely independent, state this with a brief rationale -- "these
surprises are unrelated" without explanation is insufficient.

### Echo Author Step 6 -- Surprise ranking

Rank all surprises by design impact, highest to lowest. Argue each position by naming
the specific load-bearing design decision affected and explaining why this surprise
ranks above those below it. A sorted list without per-entry argument fails.

### Echo Author Step 7 -- Risk escalation

Flag the single surprise most likely to invalidate a core assumption. Write:
- The assumption at risk (named)
- The Source artifact that revealed the threat (named)
- What would need to be true for the assumption to hold despite this surprise

### Echo Author Step 8 -- Institutional forward

Address the next team directly. Name the first thing they should investigate given
these surprises. Frame the echo as: "things you would not predict by reading today's
materials alone -- things that only surfaced because we gathered evidence."

---

## Output Artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter: `skill: topic-echo`, `topic: {topic}`, `date: {date}`
2. `## Prior Belief Inventory` (Archivist output -- verbatim, not revised)
3. `## Signal Findings` (Signal Reader output -- key findings per artifact)
4. `## Handle Ledger` (Echo Author -- one row per surprise)
5. `## Surprises` (Echo Author -- structured records, all fields required)
6. `## Cross-Signal Patterns` (or explicit independence statement)
7. `## Surprise Ranking` (with argued rationale per position)
8. `## Risk Escalation`
9. `## Institutional Forward`
```

---

## Discriminating Pairs

| Pair | Axis isolated | C-13 prediction | C-14 prediction |
|------|--------------|-----------------|-----------------|
| V-01 vs V-02 | Phase gate vs schema | V-01 > V-02 | V-02 > V-01 |
| V-01 vs V-03 | Phase gate vs role boundary | Uncertain -- both target C-13 via different mechanisms | V-03 >= V-01 |
| V-02 vs V-04 | Schema alone vs schema + phase | Equal -- schema does the C-14 work in both | V-04 >= V-02 for C-13 |
| V-03 vs V-05 | Role sequence alone vs full synthesis | Equal -- role boundary is the C-13 mechanism in both | V-05 > V-03 for C-14 |
| V-04 vs V-05 | Combined no-role vs full synthesis | V-05 > V-04 -- role adds information boundary | Equal -- schema is present in both |

**Key discriminating question for R3:** Does the role information boundary (V-03, V-05)
produce more reliable C-13 compliance than the workflow phase gate (V-01, V-04)? If
V-03 and V-04 score the same on C-13, the role structure adds no value over the phase
gate, and V-04 is the simpler winning variation. If V-03 > V-01 and V-05 > V-04 on
C-13, the role boundary adds reliability that the phase gate cannot provide.
