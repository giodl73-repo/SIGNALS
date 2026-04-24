---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 4
rubric: v4
rubric_criteria_new: [C-15, C-16]
rubric_max: 130
---

# Variations: `topic:echo` -- Round 4 (rubric v4 / C-15 + C-16)

**Rubric:** v4 | **Date:** 2026-03-16 | **Max:** 130

---

## Design Context

R3 established the full structural foundation: Archivist / Signal Reader / Echo Author role
sequence with information-boundary enforcement (C-13), mandatory triple-pointer entry schema
(C-14), and the full aspirational suite. R3 V-05 scored 120/120 on the v3 rubric.

v4 adds two new aspirational criteria built on top of C-11/C-13/C-14:

**C-15 -- Pre-commitment enforcement mechanism declaration** (correctness, gate: C-11)
The artifact must *declare* how the PBI was isolated from signal knowledge -- not merely that
a PBI section exists. Two mechanism types exist: temporal provenance (phase gate + freeze
timestamp) and structural provenance (role-scope exclusion). Temporal is weaker: a phase gate
sequences file access but does not prevent the model from drawing on its own prior reasoning
across phases. Structural is stronger: the Archivist role makes signal content unavailable
before PBI production because no signals have been extracted yet. The declaration must be
explicit so a reviewer can calibrate C-13 trust without performing their own content analysis.

**C-16 -- Production-time per-entry verification attestation** (behavior, gate: C-14)
Each surprise entry must include a producer attestation naming each of the three verification
checks performed before writing: (1) handle confirmed in Handle Ledger, (2) PBI-Ref confirmed
at that identifier, (3) source artifact confirmed in Signal Findings. A generic "verified"
fails -- each check must be enumerated individually. This shifts audit burden from reviewer
obligation (C-14) to producer evidence (C-16).

**Gap analysis from R3 V-05 (120/120 on v3):**

*C-15 gap:* V-05's role boundary *creates* structural provenance but the freeze declaration
reads "Archivist complete. PBI frozen. Signal Reader begins." -- a reviewer must infer from
the role structure that this is structural (not temporal) provenance. C-15 requires the
*declaration* of mechanism type, not just the mechanism's presence.

*C-16 gap:* V-05's entry self-check reads "A reviewer reading only this entry must be able
to verify..." -- this is reviewer-framing. C-16 requires the model to produce a per-entry
attestation in declaration language stating which checks were performed as a producer
commitment, not a reviewer reminder.

**Variation axes selected for R4:**

1. **Mechanism declaration format** (C-15 target) -- one-line freeze label vs. standalone
   `## Pre-Commitment Provenance` section with mechanism vocabulary, strength category, and
   reviewer calibration note.

2. **Attestation granularity** (C-16 target) -- `Verified:` labeled schema field with named
   checks vs. post-entry checklist step.

3. **Phrasing register** (both) -- minimal declarative ("Mechanism: structural provenance")
   vs. evidentiary with value quotes ("PBI-03 confirmed at identifier: entry reads '...'").

**Variation plan:**

| Variation | Primary axes | Hypothesis |
|-----------|-------------|------------|
| V-01 | Mechanism declaration (minimal -- freeze label only) | One-line label in freeze declaration satisfies C-15 without provenance section overhead |
| V-02 | Per-entry attestation (Verified field, named checks) | Required `Verified:` field satisfies C-16 without mechanism declaration |
| V-03 | Mechanism declaration (strong -- dedicated provenance section) | Standalone provenance section with mechanism vocabulary produces stronger C-15 than freeze label |
| V-04 | Mechanism declaration (minimal) + Per-entry attestation | Both criteria satisfied with minimal overhead; tests whether freeze label + Verified field is sufficient |
| V-05 | Provenance section (strong) + Per-entry attestation (evidentiary, with value quotes) | Full synthesis: strongest C-15 + strongest C-16; evidentiary attestation quotes specific values, shifting audit burden completely to producer |

**Discriminating pairs:**

- V-01 vs V-03: Freeze label vs. provenance section -- which declaration depth is required for C-15 PASS
- V-01 vs V-04: C-15 alone vs. C-15 + C-16 -- does adding attestation help C-15 or only C-16
- V-02 vs V-04: C-16 alone vs. C-15 + C-16 -- marginal value of mechanism declaration for overall score
- V-03 vs V-05: Strong C-15 vs. strong C-15 + C-16 -- isolates attestation contribution
- V-04 vs V-05: Minimal C-15+C-16 vs. strong C-15+C-16 -- whether provenance section + evidentiary quoting adds score

---

## V-01 -- Single-axis: Mechanism Declaration (Minimal -- Freeze Label)

**Variation axis:** Mechanism declaration format. A single-sentence provenance type label is
added to the Archivist's freeze declaration, explicitly naming the mechanism. All other
structure is identical to R3 V-05. The role boundary already creates structural provenance;
this variation adds the declaration that makes the mechanism legible without content analysis.

**Hypothesis:** R3 V-05's freeze says "Archivist complete. PBI frozen. Signal Reader begins."
A reviewer sees that a role boundary governed PBI production but must infer mechanism type.
Adding "Mechanism: structural provenance (role-scope exclusion) -- Archivist had no access to
signal artifacts." makes C-15 satisfy without provenance section overhead. C-16 is not
targeted -- the entry self-check remains reviewer-framed, so per-entry attestation will depend
on model discipline. This is the discriminator between V-01 and V-04.

**C-15 target:** Mechanism label in freeze declaration.
**C-16 target:** Not addressed. Self-check is reviewer-framed.

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

Write the freeze declaration exactly as follows:

"Archivist complete. Mechanism: structural provenance (role-scope exclusion) --
the Archivist role operated with no access to signal artifacts; PBI entries were
produced from domain knowledge only. PBI frozen. Signal Reader begins."

Do not revise the PBI after this point.

---

## Role 2: Signal Reader

**Scope:** Signal artifacts only. The PBI exists but this role does not reference it.
Findings are extracted independently of the stated beliefs.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for paths matching `*{topic}*`. List all artifact paths by namespace.

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

### Echo Author Step 2 -- Named handles

Assign each surprise a handle: 2--5 words in finding language. Handles name what
was discovered, not what was expected.

Independence test: does the handle echo PBI entry language verbatim? If yes, rewrite
it in finding language specific to what the signals showed.

Specificity test: could this handle appear in any investigation? If yes, rewrite until
it names the specific finding.

### Echo Author Step 3 -- Handle Ledger

Write section `## Handle Ledger`:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

One row per surprise. The ledger is the index; the entries are the bodies.

### Echo Author Step 4 -- Surprise entries

Each surprise is a structured record with all fields required. Missing any field is
a structural error.

```
### {handle}

Handle:    {2--5 word handle -- must match Handle Ledger row exactly}
PBI-Ref:   PB-NN  {must match an identifier from ## Prior Belief Inventory}
Source:    {artifact name -- must appear in ## Signal Findings}
Expected:  {PBI entry at PB-NN -- quoted or closely paraphrased}
Found:     {Finding from Source artifact}
Departure: {Why Expected vs Found is a non-trivial surprise}
Impact:    {confirming|redirecting|destabilizing} -- {named decision or question}
```

Self-check (required before writing the artifact):
A reviewer reading only this entry must be able to verify:
1. Handle exists in ## Handle Ledger
2. PBI-Ref entry exists in ## Prior Belief Inventory at the named identifier
3. Source artifact appears in ## Signal Findings with the finding stated

If any pointer is missing or unverifiable, add the missing pointer before writing.

### Echo Author Step 5 -- Cross-signal patterns

If two or more surprises share an underlying cause or implication, name the pattern
and state its design implication. If independent, state this explicitly with rationale.

### Echo Author Step 6 -- Surprise ranking

Rank by design impact. Argue each position by naming the load-bearing decision affected.
A sorted list without argument fails.

### Echo Author Step 7 -- Risk escalation

Flag the riskiest surprise. Name: assumption at risk, source artifact, survival condition.

### Echo Author Step 8 -- Institutional forward

Address the next team. Name what to investigate first. Frame as "things you would not
predict by reading today's materials alone."

---

## Output Artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter: `skill: topic-echo`, `topic: {topic}`, `date: {date}`
2. `## Prior Belief Inventory` (Archivist -- verbatim, not revised; freeze declaration appears
   at the end of this section with the mechanism label)
3. `## Signal Findings` (Signal Reader)
4. `## Handle Ledger` (Echo Author)
5. `## Surprises` (all fields required)
6. `## Cross-Signal Patterns`
7. `## Surprise Ranking`
8. `## Risk Escalation`
9. `## Institutional Forward`
```

---

## V-02 -- Single-axis: Per-Entry Producer Attestation (Verified Field)

**Variation axis:** Output format / attestation granularity. A `Verified:` labeled field is
added to the entry schema requiring the model to write a production-time attestation that
names each of the three checks explicitly. The entry self-check from R3 V-05 is rewritten as
a producer commitment in declaration language. No mechanism declaration is added -- the freeze
remains identical to R3 V-05 ("Archivist complete. PBI frozen. Signal Reader begins.").

**Hypothesis:** R3 V-05's self-check is "a reviewer must be able to verify..." -- reviewer
obligation framing. Adding a required `Verified:` field with named checks ("Handle '{handle}'
confirmed in Handle Ledger; PB-NN confirmed in Prior Belief Inventory; '{artifact}' confirmed
in Signal Findings. All three checks performed before writing.") makes C-16 satisfy as a
structural output constraint. C-15 is not targeted -- mechanism type is implied by role
structure but not declared, so a reviewer still must infer it.

**C-15 target:** Not addressed. Mechanism implied but not declared.
**C-16 target:** `Verified:` field with named per-check attestation required.

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

### Archivist Step 1 -- Namespace estimate

Based on the topic name only, estimate which Signal namespaces likely have coverage.
Do not verify -- that is the Signal Reader's job.

### Archivist Step 2 -- Prior Belief Inventory

Write section `## Prior Belief Inventory` with 4--8 entries:

```
PB-NN: [Belief statement: "We expected...", "We assumed...", "We believed..."]
```

- Belief language only. No finding language.
- No handle names. Handles do not exist until Signal Reader completes.
- No artifact references. Archivist has not read signals.
- Entries addressable by identifier (PB-01, PB-02, ...)

### Archivist Step 3 -- Freeze

Write: "Archivist complete. PBI frozen. Signal Reader begins."

Do not revise the PBI after this point.

---

## Role 2: Signal Reader

**Scope:** Signal artifacts only. Do not reference the PBI.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for paths matching `*{topic}*`. List all artifact paths by namespace.

### Signal Reader Step 2 -- Read

Open each artifact. Extract key findings. Record exact artifact filenames.

### Signal Reader Step 3 -- Findings register

Write section `## Signal Findings`:

```
**{artifact-name}** ({namespace}):
- {finding 1}
- {finding 2}
...
```

### Signal Reader Step 4 -- Close

Write: "Signal Reader complete. Echo Author begins."

---

## Role 3: Echo Author

**Scope:** Both Archivist PBI and Signal Reader findings. Synthesizes surprises.

### Echo Author Step 1 -- Surprise identification

For each finding, compare to every PBI entry. A surprise is a meaningful departure.
Discard confirmations. Discard generic observations not specific to this topic.

### Echo Author Step 2 -- Named handles

Assign each surprise a handle: 2--5 words in finding language.
Independence test: does it echo PBI language verbatim? Rewrite if yes.
Specificity test: could it appear in any investigation? Rewrite if yes.

### Echo Author Step 3 -- Handle Ledger

Write section `## Handle Ledger`:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

### Echo Author Step 4 -- Surprise entries

Each entry is a structured record. All fields are required. A record missing any field
must not appear in the artifact.

For each entry: complete the substantive fields (Handle through Impact), then write the
`Verified:` field as a producer attestation naming each check individually. "Verified"
without naming which checks were performed fails -- each of the three checks must be
stated by name.

```
### {handle}

Handle:    {2--5 word handle -- must match Handle Ledger entry exactly}
PBI-Ref:   PB-NN  {must match an identifier from ## Prior Belief Inventory}
Source:    {artifact name -- must appear in ## Signal Findings}
Expected:  {PBI entry at PB-NN -- quoted or closely paraphrased}
Found:     {Finding from Source artifact}
Departure: {Why Expected vs Found is a non-trivial surprise}
Impact:    {confirming|redirecting|destabilizing} -- {named decision or question}
Verified:  (1) Handle '{handle}' confirmed in Handle Ledger at that exact title.
           (2) PBI-Ref 'PB-NN' confirmed in Prior Belief Inventory at that identifier.
           (3) Source '{artifact}' confirmed in Signal Findings register.
           All three checks performed at production time before writing this entry.
```

Write the `Verified:` field in declaration language ("confirmed"), not reminder
language ("should be confirmed by reviewer"). This is producer evidence, not a
reviewer checklist.

### Echo Author Step 5 -- Cross-signal patterns

If two or more surprises share an underlying cause, name the pattern and state the
design implication. If independent, state this explicitly with rationale.

### Echo Author Step 6 -- Surprise ranking

Rank by design impact. Argue each position by naming the load-bearing decision affected.
A sorted list without argument fails.

### Echo Author Step 7 -- Risk escalation

Flag the riskiest surprise. Name: assumption at risk, source artifact, survival condition.

### Echo Author Step 8 -- Institutional forward

Address the next team. Name what to investigate first. Frame as "things you would not
predict by reading today's materials alone."

---

## Output Artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter: `skill: topic-echo`, `topic: {topic}`, `date: {date}`
2. `## Prior Belief Inventory` (Archivist -- verbatim)
3. `## Signal Findings` (Signal Reader)
4. `## Handle Ledger` (Echo Author)
5. `## Surprises` (all fields including Verified required)
6. `## Cross-Signal Patterns`
7. `## Surprise Ranking`
8. `## Risk Escalation`
9. `## Institutional Forward`
```

---

## V-03 -- Single-axis: Dedicated Pre-Commitment Provenance Section (Strong C-15)

**Variation axis:** Lifecycle emphasis / provenance section depth. After the Archivist writes
the PBI, a dedicated `## Pre-Commitment Provenance` section is added to the artifact declaring:
mechanism type, provenance strength category, why this type is stronger than the alternative,
and a reviewer calibration statement. No per-entry attestation change from R3 V-05.

**Hypothesis:** V-01's one-line freeze label names the mechanism but provides no calibration
guidance -- a reviewer must still reason about what structural vs. temporal means for C-13
trust. A dedicated provenance section that names the mechanism, explains the strength
hierarchy, and states the reviewer implication eliminates that reasoning burden. This matches
the vocabulary the v4 rubric uses for C-15 (temporal < structural; "reviewer must calibrate
trust"). A section that mirrors the rubric's vocabulary makes C-15 satisfy more reliably than
a label that requires the reviewer to map the label to the rubric's strength hierarchy.

**C-15 target:** Dedicated `## Pre-Commitment Provenance` section with mechanism type,
strength category, and reviewer calibration statement.
**C-16 target:** Not addressed. Self-check remains reviewer-framed (from R3 V-05).

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

### Archivist Step 1 -- Namespace estimate

Based on the topic name only, estimate which Signal namespaces likely have coverage.
Do not verify -- that is the Signal Reader's job.

### Archivist Step 2 -- Prior Belief Inventory

Write section `## Prior Belief Inventory` with 4--8 entries:

```
PB-NN: [Belief statement: "We expected...", "We assumed...", "We believed..."]
```

- Belief language only. No finding language.
- No handle names. Handles do not exist until Signal Reader completes.
- No artifact references. Archivist has not read signals.
- Entries addressable by identifier (PB-01, PB-02, ...)

### Archivist Step 3 -- Pre-Commitment Provenance Declaration

Immediately after the PBI section, write a section titled `## Pre-Commitment Provenance`.
This section is a standing audit declaration a reviewer reads once to calibrate their
trust in PBI/handle independence without performing content analysis.

The section must contain all four elements:

**Element 1: Mechanism type declaration.** Name which of the two mechanism types governs
this PBI:
- Structural provenance (role-scope exclusion): the PBI-writing role had no access to
  signal artifacts. Signal content was unavailable, not merely instructed-against.
  Handles, which require signal reading, did not exist at Archivist time.
- Temporal provenance (phase gate): the PBI was written before signal files were opened,
  enforced by a phase gate. The model's prior reasoning may have bridged phases.

**Element 2: Mechanism declaration sentence** (write exactly):
If structural (applies to this role-based prompt):
"Mechanism: structural provenance -- role-scope exclusion. The Archivist operated with
scope 'domain knowledge and topic name only; no file reads; no signal content of any
kind.' PBI entries reflect pre-evidence domain beliefs. Handles, which name what signals
revealed, could not appear in PBI entries at Archivist time -- they did not exist."

**Element 3: Strength category.** Write:
"Provenance strength: structural (stronger). A role-scope boundary makes signal content
structurally unavailable; a phase gate sequences file access but does not prevent
cross-phase reasoning. Structural provenance is the stronger type because it eliminates
the possibility of prior reasoning contamination, not merely the sequence of file reads."

**Element 4: Reviewer calibration statement.** Write:
"Reviewer implication: C-13 independence between ## Prior Belief Inventory and
## Handle Ledger is structurally enforced by role scope. A reviewer can confirm
independence through content analysis (PBI entries use belief language; handles use
finding language with no PBI vocabulary echo), but content analysis is confirmatory --
it is not required to establish the independence claim. The mechanism declaration is
the primary evidence."

### Archivist Step 4 -- Freeze

Write at the end of the provenance section:
"Archivist complete. PBI and provenance declaration frozen. Signal Reader begins."

Do not revise the PBI or Pre-Commitment Provenance section after this point.

---

## Role 2: Signal Reader

**Scope:** Signal artifacts only. Do not reference the PBI.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for paths matching `*{topic}*`. List all artifact paths by namespace.

### Signal Reader Step 2 -- Read

Open each artifact. Extract key findings. Record exact artifact filenames.

### Signal Reader Step 3 -- Findings register

Write section `## Signal Findings`:

```
**{artifact-name}** ({namespace}):
- {finding 1}
- {finding 2}
...
```

### Signal Reader Step 4 -- Close

Write: "Signal Reader complete. Echo Author begins."

---

## Role 3: Echo Author

**Scope:** Both Archivist PBI and Signal Reader findings. Synthesizes surprises.

### Echo Author Step 1 -- Surprise identification

For each finding, compare to every PBI entry. A surprise is a meaningful departure.
Test: "Would a team member who read only the PBI and then read this finding have been
surprised?" Discard confirmations. Discard generic observations not specific to this topic.

### Echo Author Step 2 -- Named handles

Assign each surprise a handle: 2--5 words in finding language.

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

### Echo Author Step 4 -- Surprise entries

Each entry is a structured record with all fields required. Missing any field is a
structural error.

```
### {handle}

Handle:    {2--5 word handle -- must match Handle Ledger entry exactly}
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

If any pointer is missing or unverifiable, add it before writing.

### Echo Author Step 5 -- Cross-signal patterns

If two or more surprises share an underlying cause, name the pattern and state the
design implication. If independent, state this explicitly with rationale.

### Echo Author Step 6 -- Surprise ranking

Rank by design impact. Argue each position by naming the load-bearing decision affected.

### Echo Author Step 7 -- Risk escalation

Flag the riskiest surprise. Name: assumption at risk, source artifact, survival condition.

### Echo Author Step 8 -- Institutional forward

Address the next team. Name what to investigate first. Frame as "things you would not
predict by reading today's materials alone."

---

## Output Artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter: `skill: topic-echo`, `topic: {topic}`, `date: {date}`
2. `## Prior Belief Inventory` (Archivist -- verbatim, not revised)
3. `## Pre-Commitment Provenance` (mechanism type, strength category, reviewer calibration,
   freeze declaration)
4. `## Signal Findings` (Signal Reader)
5. `## Handle Ledger` (Echo Author)
6. `## Surprises` (all fields required)
7. `## Cross-Signal Patterns`
8. `## Surprise Ranking`
9. `## Risk Escalation`
10. `## Institutional Forward`
```

---

## V-04 -- Combined: Mechanism Declaration (Minimal) + Per-Entry Attestation

**Variation axes:** Mechanism declaration (V-01 freeze label) + Per-entry attestation
(V-02 Verified field). Combines the one-sentence provenance type label in the freeze
declaration with a mandatory `Verified:` field in every surprise entry schema. Both C-15
and C-16 targeted. No dedicated provenance section -- the freeze label carries C-15; the
schema field carries C-16.

**Hypothesis:** V-01 satisfies C-15 but not C-16. V-02 satisfies C-16 but not C-15. V-04
combines both with minimal overhead. The question is whether the rubric's C-15 pass condition
requires the vocabulary depth of a dedicated provenance section (V-03/V-05) or whether a
freeze label is sufficient. If both score the same on C-15, V-04 is the simpler winner over
V-05 since it achieves full C-15+C-16 satisfaction with less structural overhead.

**C-15 target:** Freeze label with mechanism type and role-scope note.
**C-16 target:** `Verified:` field with named per-check attestation.

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

### Archivist Step 1 -- Namespace estimate

Based on the topic name only, estimate which Signal namespaces likely have coverage.
Do not verify -- that is the Signal Reader's job.

### Archivist Step 2 -- Prior Belief Inventory

Write section `## Prior Belief Inventory` with 4--8 entries:

```
PB-NN: [Belief statement: "We expected...", "We assumed...", "We believed..."]
```

- Belief language only. No finding language.
- No handle names. Handles do not exist until Signal Reader completes.
- No artifact references. Archivist has not read signals.
- Entries addressable by identifier (PB-01, PB-02, ...)

### Archivist Step 3 -- Freeze

Write the freeze declaration exactly as follows:

"Archivist complete. Mechanism: structural provenance (role-scope exclusion) --
the Archivist role operated with no access to signal artifacts; PBI entries were
produced from domain knowledge only. PBI frozen. Signal Reader begins."

Do not revise the PBI after this point.

---

## Role 2: Signal Reader

**Scope:** Signal artifacts only. Do not reference the PBI.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for paths matching `*{topic}*`. List all artifact paths by namespace.

### Signal Reader Step 2 -- Read

Open each artifact. Extract key findings. Record exact artifact filenames.

### Signal Reader Step 3 -- Findings register

Write section `## Signal Findings`:

```
**{artifact-name}** ({namespace}):
- {finding 1}
- {finding 2}
...
```

### Signal Reader Step 4 -- Close

Write: "Signal Reader complete. Echo Author begins."

---

## Role 3: Echo Author

**Scope:** Both Archivist PBI and Signal Reader findings. Synthesizes surprises.

### Echo Author Step 1 -- Surprise identification

For each finding, compare to every PBI entry. A surprise is a meaningful departure.
Discard confirmations. Discard generic observations not specific to this topic.

### Echo Author Step 2 -- Named handles

Assign each surprise a handle: 2--5 words in finding language.

Independence test: does it echo PBI language verbatim? Rewrite if yes (finding language,
not belief language).
Specificity test: could it appear in any investigation? Rewrite if yes.

### Echo Author Step 3 -- Handle Ledger

Write section `## Handle Ledger`:

```
- {handle} | PBI: PB-NN | Source: {artifact-name}
```

### Echo Author Step 4 -- Surprise entries

Each entry is a structured record. All fields are required. Missing any field is a
structural error -- do not write the entry until all fields are complete.

For each entry, complete the substantive fields (Handle through Impact), then perform
the three production-time checks and record them in the `Verified:` field. Name each
check individually. A `Verified:` field without named checks fails.

```
### {handle}

Handle:    {2--5 word handle -- must match Handle Ledger entry exactly}
PBI-Ref:   PB-NN  {must match an identifier from ## Prior Belief Inventory}
Source:    {artifact name -- must appear in ## Signal Findings}
Expected:  {PBI entry at PB-NN -- quoted or closely paraphrased}
Found:     {Finding from Source artifact}
Departure: {Why Expected vs Found is a non-trivial surprise}
Impact:    {confirming|redirecting|destabilizing} -- {named decision or question}
Verified:  (1) Handle '{handle}' confirmed in Handle Ledger at that exact title.
           (2) PBI-Ref 'PB-NN' confirmed in Prior Belief Inventory at that identifier.
           (3) Source '{artifact}' confirmed in Signal Findings register.
           All three checks performed at production time before writing this entry.
```

Write the `Verified:` field in declaration language ("confirmed"), not reminder language
("should be checked by reviewer"). This is producer evidence, not a reviewer checklist.

### Echo Author Step 5 -- Cross-signal patterns

If two or more surprises share an underlying cause, name the pattern and state the
design implication. If independent, state this explicitly with rationale.

### Echo Author Step 6 -- Surprise ranking

Rank by design impact. Argue each position by naming the load-bearing decision affected.
A sorted list without argument fails.

### Echo Author Step 7 -- Risk escalation

Flag the riskiest surprise. Name: assumption at risk, source artifact, survival condition.

### Echo Author Step 8 -- Institutional forward

Address the next team. Name what to investigate first. Frame as "things you would not
predict by reading today's materials alone."

---

## Output Artifact

Write to `simulations/topic/echo/{topic}-echo-{date}.md`:

1. Frontmatter: `skill: topic-echo`, `topic: {topic}`, `date: {date}`
2. `## Prior Belief Inventory` (Archivist -- verbatim; freeze declaration with mechanism
   label appears at the end of this section)
3. `## Signal Findings` (Signal Reader)
4. `## Handle Ledger` (Echo Author)
5. `## Surprises` (all fields including Verified required)
6. `## Cross-Signal Patterns`
7. `## Surprise Ranking`
8. `## Risk Escalation`
9. `## Institutional Forward`
```

---

## V-05 -- Full Synthesis: Provenance Section + Evidentiary Attestation + Hierarchy Note

**Variation axes:** All three. Dedicated `## Pre-Commitment Provenance` section (strong C-15,
from V-03) + `Verified:` field with evidentiary quoting (C-16, stronger than V-02/V-04) +
provenance hierarchy explanation within the section. The Verified field in V-05 goes beyond
V-02/V-04 by requiring the model to quote the specific values confirmed -- not just name which
checks were done, but cite the actual PBI text and artifact name that were verified. This is
the evidentiary tier of C-16: the attestation is now a signed record a reviewer can inspect
without any inference.

**Hypothesis:** V-04 achieves minimal C-15 + C-16 compliance but leaves residual reviewer
work: (a) for C-15, the reviewer must map the freeze label to the rubric's strength hierarchy
(structural > temporal); (b) for C-16, the reviewer sees named checks but must still look up
the PBI entry and artifact to confirm they match. V-05 eliminates both residuals: the
provenance section explains the strength hierarchy explicitly, and the Verified field quotes
the specific values so the reviewer can confirm correctness from the field alone. If the rubric
scores these additional completeness properties, V-05 outscores V-04 on both criteria.

**C-15 target:** Dedicated provenance section with mechanism vocabulary, strength hierarchy,
and reviewer calibration statement.
**C-16 target:** `Verified:` field quoting actual PBI entry text and artifact name; attestation
is evidentiary, not merely declarative.

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

### Archivist Step 3 -- Pre-Commitment Provenance Declaration

Write a section titled `## Pre-Commitment Provenance` immediately after the PBI.
This section is a standing audit declaration. A reviewer reads it once to understand
exactly what independence was enforced and what that entitles them to trust.

Write all four elements:

**Element 1 -- Mechanism type:**
"Mechanism: structural provenance -- role-scope exclusion."

**Element 2 -- Mechanism description:**
"The Archivist role operated with scope boundary: 'domain knowledge and topic name
only; no file reads; no signal content of any kind.' PBI entries were produced from
pre-evidence domain beliefs. Handle names, which are assigned by the Echo Author
after signal reading, did not exist at Archivist time and cannot appear in PBI entries.
The information boundary is structural: it is enforced by role sequencing, not by
instruction."

**Element 3 -- Strength hierarchy:**
"Provenance strength: structural (the stronger type). Two types exist:
- Structural provenance (this artifact): role-scope boundary makes signal content
  unavailable before PBI production. The Archivist literally cannot have read signals
  that the Signal Reader has not yet extracted.
- Temporal provenance (weaker): a phase gate sequences file access but does not prevent
  cross-phase reasoning. A model following a phase gate may carry forward internal
  knowledge of its own prior reasoning.
Structural provenance eliminates the contamination path that temporal provenance only
sequences."

**Element 4 -- Reviewer calibration:**
"Reviewer implication: C-13 independence between ## Prior Belief Inventory and
## Handle Ledger is structurally enforced. Content analysis (confirming that PBI entries
use belief language with no Handle Ledger vocabulary echo) is confirmatory verification,
not a required primary check. The provenance declaration is the primary evidence of
independence. Reviewers may perform content analysis to confirm the boundary held; they
are not obligated to derive independence from content alone."

Write at the end of this section:
"Archivist complete. PBI and provenance declaration frozen. Signal Reader begins."

Do not revise the PBI or Pre-Commitment Provenance after this point.

---

## Role 2: Signal Reader

**Scope:** Signal artifacts only. The PBI exists but this role does not reference it.
Findings are extracted independently of the stated beliefs.

### Signal Reader Step 1 -- Discovery

Glob `simulations/` for paths matching `*{topic}*`. List all artifact paths by namespace.

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

This section is the Signal Reader's complete output. The Echo Author uses it as the
finding-side input.

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

For each surprise, note: PBI-Ref (PB-NN), Source artifact, expected state, found state.

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

One row per surprise. The ledger is the index; the entries are the bodies.

### Echo Author Step 4 -- Surprise entries

Each surprise is a structured record. All fields are required. Missing any field is
a structural error -- do not write the entry to the artifact until all fields are complete.

For each entry:
1. Complete all substantive fields (Handle through Impact).
2. Perform the three production-time verification checks.
3. Write the `Verified:` field quoting the specific values confirmed at each step.
   The attestation must be evidentiary: a reviewer reading only `Verified:` must see
   what was confirmed, including the specific text or name of what was checked.
   Naming the check without quoting the value is insufficient; a generic "verified"
   without naming what was checked fails.

```
### {handle}

Handle:    {2--5 word handle -- must match Handle Ledger entry exactly}
PBI-Ref:   PB-NN  {must match an identifier from ## Prior Belief Inventory}
Source:    {artifact name -- must appear in ## Signal Findings}
Expected:  {PBI entry at PB-NN -- quoted or closely paraphrased from Archivist output}
Found:     {Finding from Source artifact -- from Signal Reader output}
Departure: {Why Expected vs Found constitutes a non-trivial surprise}
Impact:    {confirming|redirecting|destabilizing} -- {named design decision or question}
Verified:  (1) Handle '{exact handle text}' confirmed in Handle Ledger at that exact title.
           (2) PBI-Ref 'PB-NN' confirmed in Prior Belief Inventory at that identifier;
               entry reads: '{verbatim or close paraphrase of the PBI entry text}'.
           (3) Source '{exact artifact filename}' confirmed in Signal Findings register;
               finding reads: '{key finding text from Signal Findings entry}'.
           Audit burden: producer. All three checks performed before writing this entry.
```

The `Verified:` field is evidentiary attestation. The quoted values allow a reviewer
to confirm correctness from the field alone without navigating to the PBI or Signal
Findings sections. Write actual values, not placeholders.

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
2. `## Prior Belief Inventory` (Archivist -- verbatim, not revised)
3. `## Pre-Commitment Provenance` (mechanism type, strength hierarchy, reviewer
   calibration, freeze declaration)
4. `## Signal Findings` (Signal Reader -- key findings per artifact)
5. `## Handle Ledger` (Echo Author -- one row per surprise)
6. `## Surprises` (all fields required; Verified field quotes actual checked values)
7. `## Cross-Signal Patterns` (or explicit independence statement with rationale)
8. `## Surprise Ranking` (with argued rationale per position)
9. `## Risk Escalation`
10. `## Institutional Forward`
```

---

## Discriminating Pairs

| Pair | Axis isolated | C-15 prediction | C-16 prediction |
|------|--------------|-----------------|-----------------|
| V-01 vs V-03 | Freeze label vs provenance section | V-03 > V-01 -- section provides strength hierarchy and reviewer calibration that a label cannot | Equal -- neither addresses C-16 |
| V-01 vs V-04 | C-15 alone vs C-15 + C-16 | Equal -- same mechanism label | V-04 > V-01 -- Verified field adds named-check attestation |
| V-02 vs V-04 | C-16 alone vs C-15 + C-16 | V-04 > V-02 -- mechanism label added | Equal -- same Verified field |
| V-03 vs V-05 | Strong C-15 only vs strong C-15 + evidentiary C-16 | Equal -- same provenance section | V-05 > V-03 -- evidentiary quoting vs reviewer-framed self-check |
| V-04 vs V-05 | Minimal C-15+C-16 vs strong C-15+C-16 | V-05 > V-04 -- provenance section vs freeze label | V-05 >= V-04 -- evidentiary quoting vs named checks without quotes |

**Key discriminating question for R4 -- C-15:** Does the rubric's pass condition require
the vocabulary depth of a provenance section (V-03/V-05) or is the freeze label (V-01/V-04)
sufficient? The rubric says "Without a mechanism declaration, a reviewer must infer
pre-commitment quality from content analysis alone." A freeze label declares the mechanism.
A provenance section additionally explains the strength hierarchy and tells the reviewer
what to conclude. If the rubric's pass bar is met by declaration alone, V-04 wins. If the
bar requires reviewer-calibration guidance, V-05 wins.

**Key discriminating question for R4 -- C-16:** Does C-16's "names each check explicitly"
require quoting the actual values (V-05) or is naming the check type sufficient (V-02/V-04)?
The rubric says "An attestation that names each check explicitly is a pass; a generic
'verified' statement without naming what was verified fails." V-02 and V-04 name the checks
("Handle confirmed in Handle Ledger; PB-NN confirmed in PBI; artifact confirmed in Signal
Findings"). V-05 quotes the specific values at each check. The rubric appears to require
named checks -- whether quoting values adds score depends on whether "names each check
explicitly" means the check type or the check result.
