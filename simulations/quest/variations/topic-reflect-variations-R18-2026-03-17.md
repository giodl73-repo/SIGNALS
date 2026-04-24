## V-01 — Single Axis: Phrasing Register (Formal / Specification)

**Hypothesis:** SHALL/SHALL NOT language + numbered invariants enforced by citation-only (not restatement) + DEFINITION blocks produce tighter structural compliance. The numbered namespace becomes an auditable compliance surface; downstream stages reference invariants by identifier rather than copying rule prose.

---

```markdown
# topic-reflect

You are executing **topic-reflect**. One question governs this execution:
**What did we learn that we did not expect?**

This is not a summary of findings. It is a synthesis of surprises — observations
that caused a prior belief to be revised. Every surprise must be named, traced to
its source signal, and assessed for design impact. The output is institutional
memory for the next team that walks this path.

---

## INVARIANT NAMESPACE

The following invariants govern all stages. Downstream stages SHALL enforce these
rules by citing the invariant number — not by restating the rule text.

| #   | Label              | Rule                                                                                                                                      |
|-----|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| V-1 | Surprise Origin    | Every Stage 4 entry SHALL reference a specific B-# from Stage 1. At least one entry SHALL contradict (not confirm) the opening model.    |
| V-2 | Signal Source      | Every Signal Source field SHALL name a specific artifact (name, namespace, and/or date). The phrases "multiple sources," "the signals," and "various artifacts" SHALL NOT appear. |
| V-3 | Dimension Vocab    | The only valid dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**. No substitutions are permitted. Do not paraphrase, combine, or extend these names. |

---

## Gate Sequence Overview

| Token                   | Issued At | Meaning                                      | Halt Condition                                 |
|-------------------------|-----------|----------------------------------------------|------------------------------------------------|
| COMMIT-STAGE-1          | Stage 1   | Opening model accepted                       | Fewer than 3 beliefs recorded                  |
| COMMIT-STAGE-2          | Stage 2   | Deviation log complete                       | No signal review conducted                     |
| GATE-CONFIRMED-[N]      | Stage 3   | Row N survives adversarial check             | —                                              |
| GATE-REJECTED-[N]       | Stage 3   | Row N fails adversarial check; discarded     | —                                              |
| COMMIT-STAGE-3-CLEAN    | Stage 3   | No foreknowledge flags; Stage 4 authorized   | —                                              |
| COMMIT-STAGE-3-FLAGGED  | Stage 3   | Foreknowledge identified; HALT               | Artifact SHALL NOT be written until resolved   |
| COMMIT-ENTRY            | Stage 4   | Entry passes four-field checklist            | Any field fails: rewrite before emitting       |
| COMMIT-STAGE-4          | Stage 4   | All entries written                          | Fewer than 2 GATE-CONFIRMED entries present    |
| COMMIT-STAGE-5          | Stage 5   | Cluster map complete                         | No named next-team assignment present          |
| COMMIT-STAGE-6          | Stage 6   | Symmetric Contract closed                   | FOREKNOWLEDGE-FLAGGED unresolved               |
| COMMIT-STAGE-7          | Stage 7   | Artifact delivered                           | Stage 6 not CLEAR                             |

---

## Stage 1: Opening Model

**DEFINITION — Opening Model:** The set of beliefs held about the topic *before*
signal artifacts are read. The opening model is the epistemic baseline against
which surprises are measured. It SHALL be constructed from memory and prior
context — not by consulting signal artifacts first.

**ENTER:** Execute this stage before reading any signal artifacts.

**PROCEDURE:**

1. State the topic name and the signal sweep that triggered this reflection.
2. Record the epistemic profile: for each dimension (cite INVARIANT V-3), assign
   a confidence level (HIGH / MEDIUM / LOW) and a one-sentence rationale.
3. Record at least 3 beliefs, numbered **B-1, B-2, B-3, …** Each belief is a full
   sentence stating what you expected to be true at the time signals were gathered.

**EXIT:** 3+ beliefs present, each on a separate numbered line, each a complete sentence.

> COMMIT-STAGE-1

---

## Stage 2: Deviation Tracking

**DEFINITION — Deviation Log:** The set of signal observations that diverged from
the opening model. A deviation is an artifact finding that was not predicted by any
B-# in Stage 1 or that directly contradicts one. The log is a working document;
entries may be added as additional artifacts are read.

**ENTER:** Read the signal artifacts. For each observation that diverges from Stage 1,
record an entry.

**PROCEDURE:**

For each deviation:

- **Signal:** artifact name (namespace, date if available) — cite INVARIANT V-2
- **Belief Tested:** B-# from Stage 1
- **What Was Found:** one specific sentence
- **Direction:** CONTRADICTS / EXTENDS / REFUTES

**EXIT:** At least one deviation recorded.

> COMMIT-STAGE-2

---

## Stage 3: Adversarial Gate

**DEFINITION — Validated Deviation Set:** The subset of Stage 2 deviations that
survive the five-check adversarial review. Only GATE-CONFIRMED entries are
permitted to proceed to Stage 4. A deviation that is not GATE-CONFIRMED in this
table SHALL NOT appear in Stage 4.

**ENTER:** For each Stage 2 deviation, run the five-check table.

**PROCEDURE:**

| Check | Condition                                                    | Verdict        |
|-------|--------------------------------------------------------------|----------------|
| 1     | Source names a specific artifact (INVARIANT V-2)            | VALID / INVALID |
| 2     | Entry traces to a specific B-# (INVARIANT V-1)              | VALID / INVALID |
| 3     | Finding contradicts or extends — not merely confirms         | VALID / INVALID |
| 4     | Finding was not already known before signal gathering began  | VALID / INVALID |
| 5     | Finding has a nameable impact on a component, API, flow, or decision | VALID / INVALID |

All 5 VALID → emit **GATE-CONFIRMED-[N]**.
Any INVALID → emit **GATE-REJECTED-[N]** and discard.

**Sweep extension:** If fewer than 2 GATE-CONFIRMED entries result, extend the
deviation sweep: re-read artifacts for overlooked divergences, add Stage 2 rows,
re-run the gate.

**Foreknowledge resolution:**
- If Check 4 is INVALID for any entry: mark it foreknowledge-flagged.
- If any flag is unresolved after sweep extension: emit **COMMIT-STAGE-3-FLAGGED**
  and HALT. Artifact SHALL NOT be written until the flag is resolved.
- If no flags remain: emit **COMMIT-STAGE-3-CLEAN**.

> COMMIT-STAGE-3-CLEAN  *or*  COMMIT-STAGE-3-FLAGGED (HALT)

---

## Stage 4: Surprise Entries

**DEFINITION — Surprise Set:** The set of named, traced, and impact-assessed
surprises that constitute the institutional memory artifact. Each surprise is a
GATE-CONFIRMED deviation rendered as a numbered prose block with four labeled
sub-fields. The Surprise Set is authoritative: it is the artifact. Either
authorizes Stage 5 execution or permanently closes it based on entry count.

**ENTER:** Proceed only if COMMIT-STAGE-3-CLEAN was emitted. Write one numbered
prose block per GATE-CONFIRMED entry.

---

**Field Reference** — consult before every entry:

| Field                      | Requirement                                                              |
|----------------------------|--------------------------------------------------------------------------|
| **What We Expected (B-[#]):**  | Full sentence referencing a specific B-# from Stage 1 — not generic    |
| **Surprise:**              | The named unexpected finding — specific, not a category                  |
| **Signal Source:**         | Artifact name with namespace and/or date (cite INVARIANT V-2) — no generics |
| **Design Impact:**         | Names a specific component, API, flow, or decision — not "the system"   |

---

**Surprise 0 (Calibration Entry — not a live entry):**

> **What We Expected (B-2):** We expected the topic scan to confirm that the
> component inventory was stable and complete before signal gathering began.
>
> **Surprise:** The scout-competitors signal identified two undocumented
> integrations not surfaced by the scan — the component inventory was less
> stable than B-2 assumed.
>
> **Signal Source:** scout-competitors-[topic]-2026-03-14.md (scout namespace)
>
> **Design Impact:** Integration registry design — the registry must account for
> integrations discovered late in the signal sweep, not only those known at topic
> creation.

---

**Entry loop** — repeat for each GATE-CONFIRMED-[N]:

Write the numbered prose block. Then run the COMMIT-ENTRY checklist before the
next entry:

- ✓ `What We Expected` cites a specific B-# from Stage 1 — full sentence, not generic
- ✓ `Surprise` names the finding specifically — not a category or theme
- ✓ `Signal Source` names a specific artifact (cite INVARIANT V-2) — no generics
- ✓ `Design Impact` names a specific component, API, flow, or decision

Any bullet fails → rewrite that field before proceeding.

> COMMIT-ENTRY

**EXIT:** All GATE-CONFIRMED entries written. COMMIT-ENTRY emitted per entry. At
least 2 entries present.

> COMMIT-STAGE-4

---

## Stage 5: Cluster Map

**DEFINITION — Cluster Map:** A grouped view of the Surprise Set organized by
impact dimension and routed to the team, role, or skill that should act on each
cluster. The cluster map is an action handoff, not a summary table.

**ENTER:** Group Stage 4 entries by design impact dimension (cite INVARIANT V-3).

**PROCEDURE:**

| Cluster Name | Surprises | Dimension        | Next Team / Skill           |
|--------------|-----------|------------------|-----------------------------|
| [name]       | S-[N] …   | [canonical name] | [named skill or named role] |

At least one row in the last column SHALL name a specific skill or role — not
only "investigate" or "review."

**EXIT:** Cluster map complete; at least one named next-team assignment present.

> COMMIT-STAGE-5

---

## Stage 6: Symmetric Contract

**DEFINITION — Symmetric Contract:** The closing epistemic verdict pairing Stage 1
beliefs against Stage 4 findings. The contract is symmetric: every belief gets a
verdict; every surprise traces back to a belief. Foreknowledge resolution status
is determined here and is binding for Stage 7 entry.

**ENTER:** For each B-# from Stage 1, assign a verdict against Stage 4.

**PROCEDURE:**

| Belief (abbreviated)    | B-# | Stage 4 Entry | Verdict                 | Revision Direction  |
|-------------------------|-----|---------------|-------------------------|---------------------|
| [text]                  | B-N | S-N or —      | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [direction or NONE] |

**Foreknowledge resolution:** If any row carries FOREKNOWLEDGE-FLAGGED, name the
responsible belief(s). Emit HALT. Artifact SHALL NOT be written.

**EXIT:** All B-# beliefs carry a verdict. Foreknowledge status recorded as CLEAR or FLAGGED.

> COMMIT-STAGE-6

---

## Stage 7: Artifact Delivery

**DEFINITION — Delivered Artifact:** The topic-reflect artifact in its final form,
authorized for storage. This stage delivers the output only when foreknowledge
resolution has been confirmed and the Symmetric Contract is closed. A
COMMIT-STAGE-6 where FOREKNOWLEDGE-FLAGGED is unresolved SHALL NOT be accepted
as entry to this stage.

**ENTER:** Proceed only if Stage 6 verdict is CLEAR and COMMIT-STAGE-6 was emitted
without a HALT signal.

**PROCEDURE:**

Assemble the final artifact in this order:
1. Header: topic name, signal sweep, date
2. Stage 1 Opening Model (epistemic profile + beliefs B-1 through B-N)
3. Stage 4 Surprise Set (all numbered prose entries)
4. Stage 5 Cluster Map
5. Stage 6 Symmetric Contract verdict table

Name the artifact: `{topic}-reflect-{date}.md`

**EXIT:** Artifact assembled and named.

> COMMIT-STAGE-7
```

---

## V-02 — Single Axis: Lifecycle Emphasis (Maximum Phase-Boundary Clarity)

**Hypothesis:** Devoting explicit narrative space to stage transitions — describing what changes at each boundary, what a gate failure means concretely, and what the next stage cannot do without the current one — produces more complete multi-stage execution and fewer stage-skip failures in long-context runs.

---

```markdown
# topic-reflect

You are executing **topic-reflect**. One question drives everything:
**What did we learn that we did not expect?**

Do not summarize findings. Synthesize surprises — moments when a belief was
disrupted by what a signal actually showed. Name each one, trace it, assess its
consequence. What you produce is a handoff document: the surprises the *next*
team needs to know before they build.

---

## Dimension Vocabulary (closed list)

The only valid dimension names throughout this skill are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute, abbreviate, or extend this list at any stage.

---

## How the Stages Sequence

Each stage produces something the next stage needs. You cannot skip ahead.

```
Stage 1 → builds the belief baseline
Stage 2 → logs what the signals actually showed
Stage 3 → filters out confirmation bias and foreknowledge
Stage 4 → writes the surprise entries (the artifact body)
Stage 5 → clusters entries into an action map
Stage 6 → closes the epistemic loop with verdicts
Stage 7 → delivers the finished artifact
```

Tokens mark transitions. Each COMMIT-STAGE-N token is a declaration that the
stage is structurally complete. Do not emit it if the exit condition is unmet —
stop, fix the gap, then emit.

| Token                  | What it signals                                 | What fails without it          |
|------------------------|-------------------------------------------------|--------------------------------|
| COMMIT-STAGE-1         | Belief baseline ready                           | Stage 2 has no reference point |
| COMMIT-STAGE-2         | Deviation log populated                         | Stage 3 has nothing to filter  |
| GATE-CONFIRMED-[N]     | Deviation N is a real surprise, not bias        | Entry N cannot enter Stage 4   |
| GATE-REJECTED-[N]      | Deviation N was bias or foreknowledge; discard  | —                              |
| COMMIT-STAGE-3-CLEAN   | No foreknowledge; Stage 4 is authorized         | —                              |
| COMMIT-STAGE-3-FLAGGED | Foreknowledge found; artifact blocked           | Do not proceed to Stage 4      |
| COMMIT-ENTRY           | This entry passes all four field checks         | Entry may not remain in artifact |
| COMMIT-STAGE-4         | All surprise entries written and checked        | Stage 5 has no entries to cluster |
| COMMIT-STAGE-5         | Cluster map ready with named assignments        | Stage 6 has no action routing  |
| COMMIT-STAGE-6         | Symmetric Contract closed                       | Stage 7 cannot authorize delivery |
| COMMIT-STAGE-7         | Artifact delivered                              | —                              |

---

## Stage 1: Build the Opening Model

*What this stage produces:* A record of what you believed before reading the signals.
This is the only moment when you can form these beliefs cleanly. Once you read
the signals, this window closes permanently.

**Before you do anything else:** Do not open any signal artifacts yet.

**Steps:**

1. Name the topic and the signal sweep.
2. For each dimension in the closed vocabulary above, write a confidence level
   (HIGH / MEDIUM / LOW) and one sentence explaining why.
3. Write at least 3 beliefs, each labeled **B-1, B-2, B-3, …** A belief is a
   complete sentence stating something you expected to be true.

**When Stage 1 is complete:** You have 3 or more beliefs, each on its own numbered
line, each a full sentence. Emit the stage token.

> COMMIT-STAGE-1

*What changes now:* You are now permitted to read signal artifacts.

---

## Stage 2: Log the Deviations

*What this stage produces:* A working list of moments when a signal showed
something different from what Stage 1 predicted. This is a scratchpad, not the
final artifact.

**Read the signal artifacts now.** For each moment of divergence, record:

- **Signal:** artifact name, namespace, date if available
- **Belief Tested:** which B-# did this touch?
- **What Was Found:** one specific sentence — what the signal actually showed
- **Direction:** CONTRADICTS / EXTENDS / REFUTES

Keep adding entries as you read. Anything that surprised you belongs here.

**When Stage 2 is complete:** At least one deviation entry is recorded.

> COMMIT-STAGE-2

*What changes now:* You have raw material for the gate. You have not yet
determined which deviations are genuine surprises.

---

## Stage 3: Run the Adversarial Gate

*What this stage produces:* A filtered set of genuine surprises. The gate
eliminates two failure modes: confirmation bias (entries that confirm rather than
disrupt beliefs) and foreknowledge (things you already knew before signals were gathered).

**For each Stage 2 entry, run this five-check table:**

| Check | Question                                                              | Verdict        |
|-------|-----------------------------------------------------------------------|----------------|
| 1     | Does the Signal field name a specific artifact (not "multiple sources")? | VALID / INVALID |
| 2     | Does the entry link to a specific B-# from Stage 1?                  | VALID / INVALID |
| 3     | Does the finding *disrupt or extend* a belief — not merely confirm it? | VALID / INVALID |
| 4     | Was this finding genuinely unknown before signal gathering started?   | VALID / INVALID |
| 5     | Can you name the specific component, API, flow, or decision affected? | VALID / INVALID |

- All 5 VALID → emit **GATE-CONFIRMED-[N]**
- Any INVALID → emit **GATE-REJECTED-[N]** (discard; do not carry to Stage 4)

**If fewer than 2 entries pass:** Go back to the signals. Look harder for
overlooked moments of divergence. Add Stage 2 rows and re-run the gate.

**Foreknowledge check (at end of gate):**

- Any entry that failed Check 4: record it as foreknowledge-flagged.
- If any foreknowledge flag remains unresolved: emit **COMMIT-STAGE-3-FLAGGED**
  and stop. You cannot write the artifact until the flag is resolved.
- If the gate is clean: emit **COMMIT-STAGE-3-CLEAN**.

> COMMIT-STAGE-3-CLEAN  *or*  COMMIT-STAGE-3-FLAGGED (stop here)

*What changes now:* You know exactly which entries are eligible for Stage 4. All
others are permanently discarded.

---

## Stage 4: Write the Surprise Entries

*What this stage produces:* The body of the institutional memory artifact. Each
entry is a numbered prose block — not a table row, not a bullet — with four
labeled sub-fields. This format prevents narrow-cell compression and forces each
field to carry a complete thought.

**Only enter this stage if COMMIT-STAGE-3-CLEAN was emitted.**

---

**Field definitions** — read these before writing any entry:

**What We Expected (B-[#]):**
A full sentence referencing a *specific* B-# from Stage 1. Not "we expected it
to work." Not "B-2 was wrong." A complete sentence: what you believed, stated
directly, with the B-# attached.

**Surprise:**
The named unexpected finding. Specific enough that the next team knows exactly
what happened. No category labels, no themes.

**Signal Source:**
The artifact that produced this surprise. Name it — skill namespace, topic,
date. Not "multiple sources." Not "the signals."

**Design Impact:**
A specific component, API, flow, or decision affected. Not "the system." Not
"architecture." The thing the next team needs to look at.

---

**Calibration entry (not a live entry) — read for format only:**

> **What We Expected (B-2):** We expected the topic scan to confirm the component
> inventory was stable before signal gathering began.
>
> **Surprise:** The scout-competitors signal identified two undocumented
> integrations not surfaced by the scan — the inventory was less complete than B-2 assumed.
>
> **Signal Source:** scout-competitors-[topic]-2026-03-14.md (scout namespace)
>
> **Design Impact:** Integration registry design — the registry must account for
> integrations discovered late in the signal sweep.

---

**Write each GATE-CONFIRMED entry now.** After each entry, run the four-field check:

- ✓ `What We Expected` contains a specific B-# and a full sentence
- ✓ `Surprise` names the finding — not a category
- ✓ `Signal Source` names a specific artifact — no generics
- ✓ `Design Impact` names a specific component, API, flow, or decision

A field that fails: rewrite it before emitting the entry token.

> COMMIT-ENTRY  *(once per entry)*

**When Stage 4 is complete:** All GATE-CONFIRMED entries written. Minimum 2.

> COMMIT-STAGE-4

*What changes now:* The artifact body exists. Stages 5 and 6 add structure and
close the epistemic loop.

---

## Stage 5: Build the Cluster Map

*What this stage produces:* An action handoff — the Stage 4 entries grouped by
dimension and routed to whoever should act on them next.

Group entries by the dimension their Design Impact touches (use the closed
vocabulary). Assign a specific next team, role, or skill — not just "investigate."

| Cluster Name | Entries  | Dimension        | Next Team / Skill   |
|--------------|----------|------------------|---------------------|
| [name]       | S-N, S-N | [canonical name] | [named skill/role]  |

At least one row must carry a specific skill or role name in the last column.

**When Stage 5 is complete:** Cluster map written; at least one named assignment present.

> COMMIT-STAGE-5

---

## Stage 6: Close the Symmetric Contract

*What this stage produces:* The closing verdict table. Every belief from Stage 1
gets a verdict against the Stage 4 surprises. This closes the epistemic loop
opened in Stage 1.

For each B-# from Stage 1:

| Belief (abbreviated) | B-# | Stage 4 Entry | Verdict                                   | Revision Direction  |
|----------------------|-----|---------------|-------------------------------------------|---------------------|
| [text]               | B-N | S-N or —      | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [direction or NONE] |

**If any row carries FOREKNOWLEDGE-FLAGGED:** Name which belief(s) are affected.
The artifact cannot be written. Stop here.

Record the foreknowledge status explicitly: CLEAR or FLAGGED.

**When Stage 6 is complete:** Every B-# has a verdict; foreknowledge status declared.

> COMMIT-STAGE-6

*What changes now:* The content is complete and verified. Stage 7 assembles and
names the artifact.

---

## Stage 7: Deliver the Artifact

*What this stage produces:* The named, structured artifact ready for storage.

**Only enter this stage if Stage 6 is CLEAR.**

Assemble in order:
1. Header: topic name, signal sweep, date
2. Opening Model from Stage 1 (profile + beliefs)
3. Surprise Set from Stage 4 (all numbered entries)
4. Cluster Map from Stage 5
5. Symmetric Contract from Stage 6

Name the file: `{topic}-reflect-{date}.md`

**When Stage 7 is complete:** Artifact assembled and named.

> COMMIT-STAGE-7
```

---

## V-03 — Single Axis: Role Sequence (Three Named Roles)

**Hypothesis:** Assigning three named roles — Recorder, Adversary, Curator — each owning distinct stages produces sharper separation between belief formation, gate enforcement, and synthesis. Naming prohibited Signal Source phrases closes the high-probability evasion surface the same way named synonym exclusions close dimension vocabulary drift.

---

```markdown
# topic-reflect

One question: **What did we learn that we did not expect?**

Not a summary. A synthesis of surprises. Each surprise: named, traced to its
source signal, assessed for design impact. The output is institutional memory.

This execution is structured around three named roles. Each role owns specific
stages. The roles enforce separation: the Recorder cannot read signals; the
Adversary cannot write entries; the Curator cannot invent sources.

---

## Roles

**The Recorder** owns Stages 1 and 2.
The Recorder builds what was believed *before* signals were read, then documents
what the signals actually showed.

**The Adversary** owns Stage 3.
The Adversary challenges every deviation. Nothing passes the gate without
surviving five checks. The Adversary's job is to find reasons to reject entries,
not reasons to accept them.

**The Curator** owns Stages 4 through 7.
The Curator writes the institutional memory. Every field must be specific. No
field may be generic. The Curator names, traces, and assesses — no approximation.

---

## Dimension Vocabulary (closed — all roles)

The only valid dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. Do not combine. Do not paraphrase.

---

## Gate Token Map

| Token                  | Stage | Owner    |
|------------------------|-------|----------|
| COMMIT-STAGE-1         | 1     | Recorder |
| COMMIT-STAGE-2         | 2     | Recorder |
| GATE-CONFIRMED-[N]     | 3     | Adversary |
| GATE-REJECTED-[N]      | 3     | Adversary |
| COMMIT-STAGE-3-CLEAN   | 3     | Adversary |
| COMMIT-STAGE-3-FLAGGED | 3     | Adversary (HALT) |
| COMMIT-ENTRY           | 4     | Curator  |
| COMMIT-STAGE-4         | 4     | Curator  |
| COMMIT-STAGE-5         | 5     | Curator  |
| COMMIT-STAGE-6         | 6     | Curator  |
| COMMIT-STAGE-7         | 7     | Curator  |

---

## RECORDER — Stage 1: Opening Model

*Do not read any signal artifacts yet.*

Build the belief baseline from memory. Once the Recorder reads signals, this
window closes.

**Steps:**

1. Name the topic and the signal sweep.
2. Epistemic profile: for each dimension in the closed vocabulary, assign
   HIGH / MEDIUM / LOW confidence and one sentence of rationale.
3. Write at least 3 beliefs, labeled **B-1, B-2, B-3, …** Each belief is a full
   sentence stating what you expected to be true.

Exit: 3+ beliefs recorded, each complete and numbered.

> COMMIT-STAGE-1

---

## RECORDER — Stage 2: Deviation Log

*The Recorder may now read signal artifacts.*

For each moment a signal showed something different from Stage 1:

- **Signal:** artifact name (namespace, date) — specific, not "the signals"
- **Belief Tested:** B-# from Stage 1
- **What Was Found:** one sentence — what the signal actually showed
- **Direction:** CONTRADICTS / EXTENDS / REFUTES

Exit: at least one entry recorded.

> COMMIT-STAGE-2

---

## ADVERSARY — Stage 3: Gate

*The Adversary now takes over. The Adversary's default posture is skepticism.*

Run the five-check table for every Stage 2 entry. Look for reasons to reject.

| Check | Question                                                                  | Verdict        |
|-------|---------------------------------------------------------------------------|----------------|
| 1     | Does the Signal field name a specific artifact?                           | VALID / INVALID |
| 2     | Does the entry trace to a specific B-#?                                   | VALID / INVALID |
| 3     | Does the finding disrupt or extend a belief — not merely confirm it?      | VALID / INVALID |
| 4     | Was this unknown before signal gathering began?                           | VALID / INVALID |
| 5     | Can a specific component, API, flow, or decision be named as affected?    | VALID / INVALID |

All 5 VALID → **GATE-CONFIRMED-[N]**.
Any INVALID → **GATE-REJECTED-[N]**. Discard. Do not carry to Stage 4.

**If fewer than 2 survive:** The Adversary returns to Stage 2 and demands more
coverage. Add entries, re-run.

**Foreknowledge ruling:** Any entry failing Check 4 is flagged. If unresolved:
emit **COMMIT-STAGE-3-FLAGGED** and halt. No artifact until cleared.

If clean: emit **COMMIT-STAGE-3-CLEAN**.

> COMMIT-STAGE-3-CLEAN  *or*  COMMIT-STAGE-3-FLAGGED (halt)

---

## CURATOR — Stage 4: Surprise Entries

*The Curator now takes over. The Curator's rule: no generic field is ever acceptable.*

**Field definitions the Curator enforces:**

**What We Expected (B-[#]):**
Full sentence with a specific B-#. Not "we expected things to work." Not "B-2."
A complete sentence stating the belief, with the B-# embedded.

**Surprise:**
Named finding — specific enough that the next team knows exactly what happened.
Not a category. Not a theme.

**Signal Source:**
Specific artifact name with namespace and/or date.
*Prohibited phrases the Curator SHALL reject:*
- "multiple sources"
- "the signals"
- "various artifacts"
- "signal sweep"
- "the evidence"
Any of these appearing in a Signal Source field means the entry fails COMMIT-ENTRY.

**Design Impact:**
Specific component, API, flow, or decision. Not "the system." Not "architecture."
Not "the design." The named thing the next team must investigate.

---

**Calibration Entry (not a live entry):**

> **What We Expected (B-2):** We expected the topic scan to confirm the component
> inventory was stable and complete before signal gathering began.
>
> **Surprise:** The scout-competitors signal identified two undocumented
> integrations not surfaced by the scan — the inventory was less stable than B-2 assumed.
>
> **Signal Source:** scout-competitors-[topic]-2026-03-14.md (scout namespace)
>
> **Design Impact:** Integration registry design — the registry must account for
> integrations discovered after topic creation, not only those known at scan time.

---

Write one numbered prose block per GATE-CONFIRMED entry.
After each entry, run the COMMIT-ENTRY check:

- ✓ `What We Expected` has a specific B-# and a full sentence
- ✓ `Surprise` names the finding (no category label)
- ✓ `Signal Source` uses no prohibited phrase; names a specific artifact
- ✓ `Design Impact` names a specific component, API, flow, or decision

Any failure → rewrite before emitting.

> COMMIT-ENTRY  *(per entry)*

Exit: all GATE-CONFIRMED entries written; minimum 2.

> COMMIT-STAGE-4

---

## CURATOR — Stage 5: Cluster Map

Group Stage 4 entries by design impact dimension (closed vocabulary). For each
cluster, name the skill or role that should act next — not just "investigate."

| Cluster | Entries | Dimension | Next Team / Skill |
|---------|---------|-----------|-------------------|
| [name]  | S-N, …  | [canonical name] | [named skill/role] |

Exit: at least one named next-team assignment.

> COMMIT-STAGE-5

---

## CURATOR — Stage 6: Symmetric Contract

Close the epistemic loop. For every B-# from Stage 1, issue a verdict.

| Belief | B-# | Stage 4 Entry | Verdict | Revision Direction |
|--------|-----|---------------|---------|-------------------|
| [text] | B-N | S-N or — | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [or NONE] |

If any row carries FOREKNOWLEDGE-FLAGGED: name the belief(s). Halt. No artifact.

Record foreknowledge status: CLEAR or FLAGGED.

> COMMIT-STAGE-6

---

## CURATOR — Stage 7: Deliver

Proceed only if Stage 6 is CLEAR.

Assemble:
1. Header: topic, sweep, date
2. Opening Model (epistemic profile + beliefs)
3. Surprise Set (all numbered entries)
4. Cluster Map
5. Symmetric Contract

Name: `{topic}-reflect-{date}.md`

> COMMIT-STAGE-7
```

---

## V-04 — Combined Axes: Formal Register + DEFINITION-Gate Architecture

**Hypothesis:** DEFINITION blocks that carry SHALL NOT downstream prohibitions — not just descriptive artifact declarations — convert each stage exit into a hard gate. The DEFINITION declares not only *what* the stage produces but *what the next stage is forbidden to do* without it, making artifact authorization prescriptive rather than descriptive.

---

```markdown
# topic-reflect

You are executing **topic-reflect**. One question governs this execution:
**What did we learn that we did not expect?**

This is not a summary of findings. It is a synthesis of surprises — observations
that disrupted prior beliefs. Every surprise must be named, traced, and assessed.
The output is institutional memory for the next team that walks this path.

---

## INVARIANT NAMESPACE

The following invariants govern all stages. Downstream stages SHALL enforce these
rules by citing the invariant number — not by restating the rule text.

| #   | Label           | Rule                                                                                                                                             |
|-----|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| V-1 | Surprise Origin | Every Stage 4 entry SHALL reference a specific B-# from Stage 1. At least one entry SHALL contradict the opening model.                         |
| V-2 | Signal Source   | Every Signal Source field SHALL name a specific artifact. The phrases "multiple sources," "the signals," "various artifacts" SHALL NOT appear.   |
| V-3 | Dimensions      | The only valid dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**. No substitutions are permitted.      |

---

## Gate Sequence Overview

| Token                  | Stage | Meaning                                      | Halt Condition                              |
|------------------------|-------|----------------------------------------------|---------------------------------------------|
| COMMIT-STAGE-1         | 1     | Opening model accepted                       | Fewer than 3 beliefs                        |
| COMMIT-STAGE-2         | 2     | Deviation log complete                       | No signal review conducted                  |
| GATE-CONFIRMED-[N]     | 3     | Row N survives adversarial check             | —                                           |
| GATE-REJECTED-[N]      | 3     | Row N discarded                              | —                                           |
| COMMIT-STAGE-3-CLEAN   | 3     | No foreknowledge; Stage 4 authorized         | —                                           |
| COMMIT-STAGE-3-FLAGGED | 3     | Foreknowledge found                          | Stage 4 SHALL NOT execute until resolved    |
| COMMIT-ENTRY           | 4     | Entry passes four-field checklist            | Field fails: rewrite before proceeding      |
| COMMIT-STAGE-4         | 4     | All entries written                          | Fewer than 2 GATE-CONFIRMED entries         |
| COMMIT-STAGE-5         | 5     | Cluster map complete                         | No named next-team assignment               |
| COMMIT-STAGE-6         | 6     | Symmetric Contract closed                   | FOREKNOWLEDGE-FLAGGED unresolved            |
| COMMIT-STAGE-7         | 7     | Artifact delivered                           | Stage 6 not CLEAR                          |

---

## Stage 1: Opening Model

**DEFINITION — Opening Model:** The set of beliefs held about the topic *before*
signal artifacts are read. The opening model is the epistemic baseline against
which Stage 4 surprises are measured. It SHALL be constructed from memory and
prior context — not from artifact review. A Stage 2 execution that has not
received COMMIT-STAGE-1 SHALL NOT read signal artifacts.

**ENTER:** Execute before reading any signal artifacts.

**PROCEDURE:**

1. State the topic name and the signal sweep.
2. Epistemic profile: for each dimension (cite INVARIANT V-3), assign HIGH / MEDIUM / LOW
   confidence and one-sentence rationale.
3. Record at least 3 beliefs labeled **B-1, B-2, B-3, …** Each is a full sentence
   stating what you expected to be true.

**EXIT:** 3+ beliefs present, each numbered, each a complete sentence.

> COMMIT-STAGE-1

---

## Stage 2: Deviation Tracking

**DEFINITION — Deviation Log:** The set of signal observations that diverged from
the opening model. A Stage 3 gate execution that has not received COMMIT-STAGE-2
SHALL NOT run adversarial checks, as it has no entries to evaluate.

**ENTER:** Read signal artifacts now.

**PROCEDURE:**

For each divergence from Stage 1:
- **Signal:** artifact name (namespace, date) — cite INVARIANT V-2
- **Belief Tested:** B-# from Stage 1
- **What Was Found:** one specific sentence
- **Direction:** CONTRADICTS / EXTENDS / REFUTES

**EXIT:** At least one deviation entry recorded.

> COMMIT-STAGE-2

---

## Stage 3: Adversarial Gate

**DEFINITION — Validated Deviation Set:** The subset of Stage 2 deviations that
survive the five-check adversarial review. Only GATE-CONFIRMED entries are
permitted to proceed to Stage 4. A deviation that is not GATE-CONFIRMED in this
table SHALL NOT appear in Stage 4. Either authorizes Stage 4 execution or
permanently closes it based on entry count and foreknowledge status.

**ENTER:** For each Stage 2 deviation, run the five-check table.

**PROCEDURE:**

| Check | Condition                                                              | Verdict        |
|-------|------------------------------------------------------------------------|----------------|
| 1     | Signal names a specific artifact (INVARIANT V-2)                       | VALID / INVALID |
| 2     | Entry traces to a specific B-# (INVARIANT V-1)                         | VALID / INVALID |
| 3     | Finding contradicts or extends — not merely confirms                   | VALID / INVALID |
| 4     | Finding was unknown before signal gathering began                      | VALID / INVALID |
| 5     | Specific component, API, flow, or decision can be named as affected    | VALID / INVALID |

All 5 VALID → **GATE-CONFIRMED-[N]**.
Any INVALID → **GATE-REJECTED-[N]** (discard).

**Sweep extension:** Fewer than 2 GATE-CONFIRMED → extend sweep, add Stage 2 rows, re-run.

**Foreknowledge resolution:**
- Check 4 INVALID on any entry → foreknowledge-flagged.
- Any unresolved flag → emit **COMMIT-STAGE-3-FLAGGED**. Stage 4 SHALL NOT execute.
- No flags → emit **COMMIT-STAGE-3-CLEAN**.

> COMMIT-STAGE-3-CLEAN  *or*  COMMIT-STAGE-3-FLAGGED (HALT)

---

## Stage 4: Surprise Entries

**DEFINITION — Surprise Set:** The set of named, traced, and impact-assessed
surprises that constitute the institutional memory artifact. Each surprise is a
GATE-CONFIRMED deviation rendered as a numbered prose block with four labeled
sub-fields. A stage execution that has not received COMMIT-STAGE-3-CLEAN SHALL
NOT write Stage 4 entries. Stage 5 SHALL NOT execute until COMMIT-STAGE-4 is
emitted with at least 2 entries present.

**ENTER:** Proceed only if COMMIT-STAGE-3-CLEAN was emitted.

---

**Field Reference** — consult before every entry:

| Field                         | Requirement                                                          |
|-------------------------------|----------------------------------------------------------------------|
| **What We Expected (B-[#]):** | Full sentence with specific B-# — not generic (cite INVARIANT V-1)  |
| **Surprise:**                 | Named finding — specific, not a category                             |
| **Signal Source:**            | Specific artifact name, namespace, date (cite INVARIANT V-2)         |
| **Design Impact:**            | Specific component, API, flow, or decision — not "the system"        |

---

**Surprise 0 (Calibration Entry — not a live entry):**

> **What We Expected (B-2):** We expected the topic scan to confirm the component
> inventory was complete before signal gathering began.
>
> **Surprise:** The scout-competitors signal identified two undocumented
> integrations not surfaced by the scan — the inventory was less complete than B-2 assumed.
>
> **Signal Source:** scout-competitors-[topic]-2026-03-14.md (scout namespace)
>
> **Design Impact:** Integration registry design — must account for integrations
> discovered late in the signal sweep.

---

**Entry loop** (repeat per GATE-CONFIRMED-[N]):

Write the numbered prose block. Run COMMIT-ENTRY checklist:

- ✓ `What We Expected` has a specific B-# and a full sentence (INVARIANT V-1)
- ✓ `Surprise` names the finding specifically
- ✓ `Signal Source` names a specific artifact (INVARIANT V-2)
- ✓ `Design Impact` names a specific component, API, flow, or decision

Any failure → rewrite before emitting.

> COMMIT-ENTRY

**EXIT:** All GATE-CONFIRMED entries written; COMMIT-ENTRY per entry; minimum 2 present.

> COMMIT-STAGE-4

---

## Stage 5: Cluster Map

**DEFINITION — Cluster Map:** A grouped view of the Surprise Set organized by
impact dimension and routed to next-team assignments. A Stage 6 execution that
has not received COMMIT-STAGE-5 SHALL NOT issue the Symmetric Contract, as
action routing has not been confirmed.

**ENTER:** Group Stage 4 entries by dimension (cite INVARIANT V-3).

**PROCEDURE:**

| Cluster | Entries | Dimension | Next Team / Skill |
|---------|---------|-----------|-------------------|
| [name]  | S-N, …  | [canonical name] | [named skill/role] |

At least one row SHALL name a specific skill or role — not only "investigate."

**EXIT:** Cluster map written; at least one named assignment present.

> COMMIT-STAGE-5

---

## Stage 6: Symmetric Contract

**DEFINITION — Symmetric Contract:** The closing epistemic verdict pairing Stage 1
beliefs against Stage 4 findings. Foreknowledge resolution is determined here and
is binding for Stage 7 entry. A Stage 7 execution that has not received
COMMIT-STAGE-6 with CLEAR status SHALL NOT deliver the artifact.

**ENTER:** For each B-# from Stage 1, assign a verdict.

| Belief (abbreviated)    | B-# | Stage 4 Entry | Verdict                                   | Revision Direction  |
|-------------------------|-----|---------------|-------------------------------------------|---------------------|
| [text]                  | B-N | S-N or —      | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [direction or NONE] |

If any row is FOREKNOWLEDGE-FLAGGED: name the belief(s). HALT. Artifact SHALL NOT be written.

Record foreknowledge status: CLEAR or FLAGGED.

**EXIT:** All B-# beliefs assigned verdicts; foreknowledge status declared.

> COMMIT-STAGE-6

---

## Stage 7: Artifact Delivery

**DEFINITION — Delivered Artifact:** The topic-reflect artifact in final form,
authorized for storage. This stage delivers the output only when foreknowledge
resolution has been confirmed and the Symmetric Contract is closed. A
COMMIT-STAGE-6 where FOREKNOWLEDGE-FLAGGED is unresolved SHALL NOT be accepted
as entry to this stage.

**ENTER:** Proceed only if Stage 6 is CLEAR and COMMIT-STAGE-6 was emitted without HALT.

**PROCEDURE:**

Assemble in order:
1. Header: topic name, sweep, date
2. Stage 1 Opening Model (profile + beliefs)
3. Stage 4 Surprise Set (all numbered entries)
4. Stage 5 Cluster Map
5. Stage 6 Symmetric Contract

Name: `{topic}-reflect-{date}.md`

**EXIT:** Artifact assembled and named.

> COMMIT-STAGE-7
```

---

## V-05 — Combined Axes: Formal Register + Anti-Restatement Mandate + DEFINITION Downstream Authorization

**Hypothesis:** Adding an explicit anti-restatement mandate *within* the Invariant Namespace declaration ("Downstream stages SHALL enforce these rules by citing the invariant number — SHALL NOT restate the rule text") converts the numbered namespace from a reference architecture into an anti-duplication contract with a named violation class. DEFINITION blocks that carry SHALL NOT prohibitions on downstream execution (not just descriptive artifact declarations) close the remaining compliance gap: citation is the only valid enforcement action, and restatement is an explicit violation.

---

```markdown
# topic-reflect

You are executing **topic-reflect**. One question governs this execution:
**What did we learn that we did not expect?**

This is not a summary of findings. It is a synthesis of surprises — observations
that caused prior beliefs to be revised. Every surprise is named, traced to its
source signal, and assessed for design impact. The output is institutional memory
for the next team that walks this path.

---

## INVARIANT NAMESPACE

The following invariants govern all stages.

**Enforcement protocol:** Downstream stages SHALL enforce these rules by citing
the invariant number — not by restating the rule text. A downstream stage that
reproduces a rule in prose rather than citing V-# is in violation of this
namespace protocol.

| #   | Label           | Rule                                                                                                                                             |
|-----|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| V-1 | Surprise Origin | Every Stage 4 entry SHALL reference a specific B-# from Stage 1. At least one entry SHALL contradict (not confirm) the opening model.           |
| V-2 | Signal Source   | Every Signal Source field SHALL name a specific artifact (name, namespace, date). The phrases "multiple sources," "the signals," and "various artifacts" SHALL NOT appear. |
| V-3 | Dimensions      | The only valid dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**. No substitutions are permitted. Do not paraphrase, combine, or extend these names. |

---

## Gate Sequence Overview

| Token                  | Stage | Meaning                                  | Halt Condition                             |
|------------------------|-------|------------------------------------------|--------------------------------------------|
| COMMIT-STAGE-1         | 1     | Opening model accepted                   | Fewer than 3 beliefs                       |
| COMMIT-STAGE-2         | 2     | Deviation log complete                   | No signal review conducted                 |
| GATE-CONFIRMED-[N]     | 3     | Row N survives adversarial check         | —                                          |
| GATE-REJECTED-[N]      | 3     | Row N discarded                          | —                                          |
| COMMIT-STAGE-3-CLEAN   | 3     | No foreknowledge; Stage 4 authorized     | —                                          |
| COMMIT-STAGE-3-FLAGGED | 3     | Foreknowledge found                      | Stage 4 SHALL NOT execute until resolved   |
| COMMIT-ENTRY           | 4     | Entry passes four-field checklist        | Any field fails: rewrite before proceeding |
| COMMIT-STAGE-4         | 4     | All entries written; Surprise Set closed | Fewer than 2 GATE-CONFIRMED entries        |
| COMMIT-STAGE-5         | 5     | Cluster map complete                     | No named next-team assignment              |
| COMMIT-STAGE-6         | 6     | Symmetric Contract closed               | FOREKNOWLEDGE-FLAGGED unresolved           |
| COMMIT-STAGE-7         | 7     | Artifact delivered                       | Stage 6 not CLEAR                         |

---

## Stage 1: Opening Model

**DEFINITION — Opening Model:** The set of beliefs held about the topic *before*
signal artifacts are read. The Opening Model is the epistemic baseline against
which Stage 4 surprises are measured. It SHALL be constructed from memory and
prior context — not from artifact review. A Stage 2 execution that has not
received COMMIT-STAGE-1 SHALL NOT proceed to reading signal artifacts.

**ENTER:** Execute this stage before reading any signal artifacts.

**PROCEDURE:**

1. Name the topic and the signal sweep.
2. Epistemic profile: for each dimension (cite V-3), assign HIGH / MEDIUM / LOW
   confidence and one sentence of rationale.
3. Record at least 3 beliefs, labeled **B-1, B-2, B-3, …** Each is a complete
   sentence stating what you expected to be true.

**EXIT:** 3+ beliefs present, each numbered, each a complete sentence.

> COMMIT-STAGE-1

---

## Stage 2: Deviation Tracking

**DEFINITION — Deviation Log:** The set of signal observations that diverged from
the Opening Model. A Stage 3 gate execution that has not received COMMIT-STAGE-2
SHALL NOT run adversarial checks — it has no entries to evaluate.

**ENTER:** Read signal artifacts now.

**PROCEDURE:**

For each divergence from Stage 1:
- **Signal:** artifact name, namespace, date — cite V-2 (no restatement of V-2 rule prose required)
- **Belief Tested:** B-# from Stage 1
- **What Was Found:** one specific sentence
- **Direction:** CONTRADICTS / EXTENDS / REFUTES

**EXIT:** At least one deviation entry recorded.

> COMMIT-STAGE-2

---

## Stage 3: Adversarial Gate

**DEFINITION — Validated Deviation Set:** The subset of Stage 2 deviations that
survive the five-check adversarial review. Only GATE-CONFIRMED entries are
permitted to proceed to Stage 4. A deviation that is not GATE-CONFIRMED in this
table SHALL NOT appear in Stage 4. Either authorizes Stage 4 execution or
permanently closes it based on entry count and foreknowledge resolution.

**ENTER:** For each Stage 2 deviation, run the five-check table.

**PROCEDURE:**

| # | Check                                                              | Verdict        |
|---|--------------------------------------------------------------------|----------------|
| 1 | Signal field complies with V-2 (specific artifact named)          | VALID / INVALID |
| 2 | Entry traces to a specific B-# per V-1                            | VALID / INVALID |
| 3 | Finding contradicts or extends — not merely confirms              | VALID / INVALID |
| 4 | Finding was unknown before signal gathering began                 | VALID / INVALID |
| 5 | Specific component, API, flow, or decision can be named as affected | VALID / INVALID |

All 5 VALID → **GATE-CONFIRMED-[N]**.
Any INVALID → **GATE-REJECTED-[N]** (discard).

**Sweep extension:** Fewer than 2 GATE-CONFIRMED → extend sweep, add Stage 2 rows, re-run.

**Foreknowledge resolution:**
- Check 4 INVALID → foreknowledge-flagged.
- Any unresolved flag → emit **COMMIT-STAGE-3-FLAGGED**. Stage 4 SHALL NOT execute.
- No flags → emit **COMMIT-STAGE-3-CLEAN**.

> COMMIT-STAGE-3-CLEAN  *or*  COMMIT-STAGE-3-FLAGGED (HALT)

---

## Stage 4: Surprise Entries

**DEFINITION — Surprise Set:** The set of named, traced, and impact-assessed
surprises constituting the institutional memory artifact. Each surprise is a
GATE-CONFIRMED deviation rendered as a numbered prose block with four labeled
sub-fields. A stage execution that has not received COMMIT-STAGE-3-CLEAN SHALL
NOT write Stage 4 entries. Stage 5 SHALL NOT execute until COMMIT-STAGE-4 is
emitted with at least 2 entries present.

**ENTER:** Proceed only if COMMIT-STAGE-3-CLEAN was emitted.

---

**Field Reference** — consult before every entry:

| Field                         | Requirement                                                     | Invariant Citation |
|-------------------------------|-----------------------------------------------------------------|--------------------|
| **What We Expected (B-[#]):** | Full sentence with specific B-# — not generic                  | V-1                |
| **Surprise:**                 | Named finding — specific, not a category                        | —                  |
| **Signal Source:**            | Specific artifact name with namespace and/or date              | V-2                |
| **Design Impact:**            | Specific component, API, flow, or decision — not "the system"  | V-1 (impact scope) |

*Enforcement: cite the invariant identifier in the entry checklist — do not restate the rule text.*

---

**Surprise 0 (Calibration Entry — not a live entry):**

> **What We Expected (B-2):** We expected the topic scan to confirm that the
> component inventory was stable and complete before signal gathering began.
>
> **Surprise:** The scout-competitors signal identified two undocumented
> integrations not surfaced by the scan — the inventory was less complete than
> B-2 assumed.
>
> **Signal Source:** scout-competitors-[topic]-2026-03-14.md (scout namespace)
>
> **Design Impact:** Integration registry design — must account for integrations
> discovered late in the signal sweep, not only those known at topic creation.

---

**Entry loop** (repeat per GATE-CONFIRMED-[N]):

Write the numbered prose block. Run the COMMIT-ENTRY checklist:

- ✓ `What We Expected` has a specific B-# and full sentence — V-1
- ✓ `Surprise` names the finding (not a category)
- ✓ `Signal Source` complies with V-2 — specific artifact, no prohibited generics
- ✓ `Design Impact` names a specific component, API, flow, or decision

Any failure → rewrite before emitting.

> COMMIT-ENTRY

**EXIT:** All GATE-CONFIRMED entries written; COMMIT-ENTRY per entry; minimum 2.

> COMMIT-STAGE-4

---

## Stage 5: Cluster Map

**DEFINITION — Cluster Map:** A grouped action handoff — Stage 4 entries organized
by impact dimension and routed to named next-team assignments. A Stage 6 execution
that has not received COMMIT-STAGE-5 SHALL NOT issue the Symmetric Contract
verdict table, as action routing has not been established.

**ENTER:** Group Stage 4 entries by dimension (cite V-3).

| Cluster | Entries | Dimension        | Next Team / Skill   |
|---------|---------|------------------|---------------------|
| [name]  | S-N, …  | [canonical name] | [named skill/role]  |

At least one row SHALL name a specific skill or named role — not only "investigate."

**EXIT:** Cluster map written; at least one named assignment.

> COMMIT-STAGE-5

---

## Stage 6: Symmetric Contract

**DEFINITION — Symmetric Contract:** The closing epistemic verdict pairing Stage 1
beliefs against Stage 4 findings. Foreknowledge resolution is determined here and
is binding for Stage 7. A Stage 7 execution that has not received COMMIT-STAGE-6
with CLEAR status SHALL NOT deliver the artifact; delivery on an unresolved
FOREKNOWLEDGE-FLAGGED contract is a protocol violation.

**ENTER:** For each B-# from Stage 1, assign a verdict.

| Belief (abbreviated)    | B-# | Stage 4 Entry | Verdict                                          | Revision Direction  |
|-------------------------|-----|---------------|--------------------------------------------------|---------------------|
| [text]                  | B-N | S-N or —      | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [direction or NONE] |

If any row carries FOREKNOWLEDGE-FLAGGED: name the responsible belief(s). HALT.
Artifact SHALL NOT be written.

Record foreknowledge status explicitly: CLEAR or FLAGGED.

**EXIT:** All B-# beliefs assigned verdicts; status declared.

> COMMIT-STAGE-6

---

## Stage 7: Artifact Delivery

**DEFINITION — Delivered Artifact:** The topic-reflect artifact in final form,
authorized for storage. This stage delivers the output only when foreknowledge
resolution has been confirmed and the Symmetric Contract is closed. A
COMMIT-STAGE-6 where FOREKNOWLEDGE-FLAGGED is unresolved SHALL NOT be accepted
as entry to this stage — foreknowledge-contaminated artifacts are not institutional
memory; they are open hypotheses.

**ENTER:** Proceed only if Stage 6 status is CLEAR and COMMIT-STAGE-6 was emitted
without a HALT signal.

**PROCEDURE:**

Assemble in order:
1. Header: topic name, signal sweep, date
2. Stage 1 Opening Model (epistemic profile + beliefs B-1 through B-N)
3. Stage 4 Surprise Set (all numbered prose entries)
4. Stage 5 Cluster Map
5. Stage 6 Symmetric Contract verdict table

Name the artifact: `{topic}-reflect-{date}.md`

**EXIT:** Artifact assembled and named.

> COMMIT-STAGE-7
```

---

## Variation Summary

| # | Axis | Key Differentiator | Rubric Hypothesis |
|---|------|--------------------|-------------------|
| V-01 | Phrasing register (formal/spec) | SHALL/SHALL NOT throughout; numbered invariants; DEFINITION blocks; ✓ checklist COMMIT-ENTRY | Formal obligation language + numbered namespace → tighter compliance, auditable invariant surface |
| V-02 | Lifecycle emphasis | Conversational register; stage-transition narrative ("what changes now"); maximum boundary clarity | Explicit transition prose reduces stage-skip in long context; failure consequences named at every gate |
| V-03 | Role sequence (three named roles) | Recorder → Adversary → Curator ownership; named prohibited Signal Source phrases enumerated by name | Role separation prevents cross-stage contamination; named antipatterns close evasion surface |
| V-04 | Formal + DEFINITION-gate architecture | DEFINITION blocks carry SHALL NOT prohibitions on next-stage entry (not only descriptive artifact declarations) | Prescriptive DEFINITION converts each exit from a description of what is produced into a prohibition on what the next stage may do without it |
| V-05 | Formal + anti-restatement mandate + DEFINITION authorization | Invariant Namespace carries explicit "SHALL cite by number — SHALL NOT restate rule text" enforcement protocol; all DEFINITION blocks carry downstream SHALL NOT | Anti-restatement mandate makes citation the *only* valid enforcement action; restatement is a named violation class rather than a structural gap |
