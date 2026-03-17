Written to `simulations/quest/variations/topic-report-variations-R1-2026-03-14.md`.

---

## Variations: topic-report R1

**5 variations, 4 axes:**

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Baseline | Spec as written; weakest on C-09 (readiness names blockers) and C-10 (Teams card purity) |
| V-02 | Output format (section-locked) | Hard named slots prevent structural omissions — C-03/C-05 mechanical fails |
| V-03 | Lifecycle emphasis (discover-then-render) | Gate-checked discovery phase locks counts before any prose, targeting C-02/C-04 accuracy |
| V-04 | Phrasing register (question-framed) | Self-check questions before writing force verification without imposing template |
| V-05 | Combined (locked slots + discover gate + blocker-naming) | All three levers together; explicit BLOCKERS list before readiness targets C-09 aspirational |

**Key design decisions:**

- **V-02** introduces hard `SLOT 1–4` labels with explicit acceptance criteria per slot — the primary defense against C-03 (owner absent) and C-05 (next step generic).
- **V-03** adds a `CHECKPOINT` line the model must emit before rendering — forces count commitment before prose generation, targeting C-02/C-04.
- **V-04** is the phrasing outlier: five `Q1–Q5` questions replace all imperative commands. Tests whether self-check framing outperforms structural constraints for C-03/C-04 consistency.
- **V-05** adds a dedicated `PHASE 2: BLOCKERS` between discover and render — the model must enumerate blocking signals by name *before* writing the readiness statement. Direct path to C-09.
- `--format teams` is a conditional branch in all five; V-02 and V-05 spell out the branch rules most completely, which is also the most likely path to C-10.

**Recommended scoring order:** V-01 baseline → V-05 ceiling → V-02 vs V-03 to isolate structure vs sequencing for C-02/C-04 → V-04 last as behavioral-register control.
* Run V-01 as baseline, V-05 as ceiling candidate (most likely to hit C-09/C-10), then compare V-02 vs V-03 to isolate whether structure or sequencing matters more for C-02/C-04 accuracy.

---

## V-01: Baseline

Axis: Spec as written — minimal interpretation
Hypothesis: Direct transcription of the skill description satisfies essentials but produces
a generic readiness statement (C-04 pass, C-09 fail) and a Teams card with markdown leakage (C-06 pass, C-10 fail).

```
You are running /topic:report. Write a shareable status document for a topic.
This is the file variant of topic-status — the same information, written to disk.

INPUTS:
- Topic name (required). If not provided, ask once.
- --format teams (optional flag). If present, switch to compact ASCII card output.

DISCOVER:
Glob simulations/**/{topic}-* to find all signal artifacts for the topic.
Read simulations/TOPICS.md (or simulations/{topic}/strategy.md if present) to get
the planned signal list with namespace, skill, item name, owner, and priority.
Cross-reference discovered artifacts against planned signals.
Compute: signals_found, signals_planned, signals_open = planned - found.

WRITE (default format):
Write artifact to simulations/{topic}/status-{date}.md with frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  format: default

Artifact sections (in order):
1. PROGRESS TABLE
   A markdown table. Columns: Namespace | Skill | Status | Owner.
   Status = DONE (artifact found) or OPEN (artifact missing).
   Include one row per planned signal. Include a summary row: X of Y complete (Z%).

2. OPEN SIGNALS
   A list. Each entry: namespace, skill type, owner (use "unassigned" if unknown).
   Omit nothing. If signals_open == 0, write "No open signals."

3. READINESS STATEMENT
   A single labeled line: "Readiness: [ready / not ready / conditionally ready]"
   Followed by one sentence of justification. Must be consistent with the counts
   in the progress table. Do not write "ready" if any essential signals are open.

4. NEXT STEP
   One concrete recommended action. Match the most critical open signal.
   Example: "Run prove-analysis (namespace: prove) — no analysis signal exists yet."
   If no open signals: "Run topic-story to synthesize available signals."

WRITE (--format teams):
Produce a single ASCII block. No markdown headers. No fenced code blocks.
Max 40 lines. Max 80 characters per line.
All four sections (progress, open signals, readiness, next step) must appear.
Use plain dashes and pipes for table borders.

Echo the artifact path when done: "Report written to simulations/{topic}/status-{date}.md"
```

---

## V-02: Section-locked template

Axis: Output format — hard section slots with fill-in-the-blank structure
Hypothesis: Named, locked sections with explicit acceptance criteria per slot reduce
structural omissions that cause C-03 (owner missing) and C-05 (next step absent) essential fails.

```
You are running /topic:report. This skill writes a status file for a topic.
All output is organized into four named slots. Every slot is required.
A slot left blank is a failure — do not omit, summarize, or merge slots.

INPUTS:
- Topic name (required). If absent, ask once.
- --format teams flag (optional). Activates compact mode.

--- PHASE 1: DISCOVER ---

Glob simulations/**/{topic}-* to collect all existing signal artifacts.
Load simulations/{topic}/strategy.md or simulations/TOPICS.md for the planned signal list.
For each planned signal record: namespace, skill, item name, priority, owner.
Mark each as DONE (artifact found matching namespace+skill+topic) or OPEN (not found).
Count: total_planned, total_done, total_open, coverage_pct = total_done / total_planned * 100.

Pause. Verify your counts once before writing. Recount if uncertain.

--- PHASE 2: RENDER (default format) ---

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}

SLOT 1 — PROGRESS TABLE
Required columns: Namespace | Skill | Status | Owner
One row per planned signal. Status = DONE or OPEN.
Final row (bold): "**Total** | | {total_done}/{total_planned} ({coverage_pct}%) | "
No row may be omitted. If a signal has no owner from strategy.md, write "unassigned".

SLOT 2 — OPEN SIGNALS
Header: "## Open Signals"
One list item per OPEN signal. Each item must include:
  - namespace (e.g., `prove`)
  - skill type (e.g., `prove-analysis`)
  - owner (e.g., `unassigned`)
If total_open == 0, write "None — all planned signals complete."
Do not describe signals in prose. List format only.

SLOT 3 — READINESS STATEMENT
Header: "## Readiness"
Format: "Status: [Ready | Not Ready | Conditionally Ready]"
Then one sentence. The sentence must be logically consistent with SLOT 1 counts.
Consistency rule: if total_open > 0 for any essential signal, status cannot be "Ready".

SLOT 4 — NEXT STEP
Header: "## Next Step"
One sentence. Name the specific skill to run and the namespace.
Match the highest-priority open signal from SLOT 2.
If no open signals: "Run /topic:story to synthesize available signals into a narrative."
Generic next steps ("continue gathering signals") fail this slot.

--- PHASE 2 (--format teams) ---

Instead of the above, produce a compact ASCII card.
Rules:
- No markdown headers (#, ##, ###)
- No fenced code blocks (no backtick sequences)
- No angle brackets
- Max 40 lines total
- Max 80 characters per line
- Use + - | characters for table borders
- All four slots must appear, compressed

Structure:
  Line 1:    TOPIC: {topic}  STATUS: {Ready/Not Ready/Conditionally Ready}
  Lines 2-N: Progress table (plain ASCII, one row per signal, condensed to Namespace+Skill+Status+Owner)
  Then:      OPEN: {count} signals
             - {namespace}/{skill} ({owner})  [one line per open signal]
  Then:      NEXT: {concrete action}

--- PHASE 3: CONFIRM ---

Echo the file path: "Report written to simulations/{topic}/status-{date}.md"
```

---

## V-03: Lifecycle emphasis (discover-then-render)

Axis: Lifecycle emphasis — two explicit phases with a checkpoint gate between them
Hypothesis: Making DISCOVER a named, gate-checked phase before any writing reduces
count errors (C-02) and readiness-table mismatches (C-04) by forcing the model to
commit to a single set of counts before prose generation begins.

```
You are running /topic:report. Before you write a single line of the report,
you will complete a full DISCOVER phase and lock your numbers. Only then render.

INPUTS:
- Topic name (required). Prompt once if absent.
- --format teams (optional).

=== PHASE 1: DISCOVER ===

Step 1.1 — Glob
Run: simulations/**/{topic}-*
Collect every matching file path. List them.

Step 1.2 — Load strategy
Read simulations/{topic}/strategy.md (or simulations/TOPICS.md entry for this topic).
Extract each planned signal: namespace, skill, owner, priority (essential / recommended / optional).

Step 1.3 — Cross-reference
For each planned signal, check whether a file path from Step 1.1 matches
(namespace and skill must both appear in the filename or path).
Mark: DONE or OPEN.

Step 1.4 — Lock counts (checkpoint)
State the following before proceeding:
  "DISCOVER COMPLETE: {total_done} of {total_planned} signals found ({coverage_pct}%).
   Open signals: {list each open signal as namespace/skill}"
Do not proceed to PHASE 2 until this checkpoint is stated.

=== PHASE 2: RENDER ===

Using only the locked counts from PHASE 1, render the report.

Default format — write simulations/{topic}/status-{date}.md:

Frontmatter: skill, topic, date, signals_found, signals_planned.

## Progress

Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal using locked values from PHASE 1.
Summary: "{total_done}/{total_planned} signals complete ({coverage_pct}%)"

## Open Signals

List each OPEN signal. Include: namespace, skill type, owner.
Use "unassigned" if owner is unknown.
If none: "All planned signals complete."

## Readiness

One labeled line + one sentence.
Label: Ready / Not Ready / Conditionally Ready.
Derive directly from locked counts — do not re-evaluate from scratch.
If any essential signal is OPEN: label must be "Not Ready" or "Conditionally Ready".

## Next Step

One concrete action: skill name + namespace.
Prioritize by: essential OPEN first, then recommended, then optional.
If all complete: "Run /topic:story to synthesize signals."

--format teams branch:
Apply the same locked counts but render as ASCII card.
No markdown syntax. Max 40 lines / 80 chars. Use plain pipes and dashes.
Four sections: progress rows, open signal list, readiness label, next step.

=== PHASE 3: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-04: Phrasing register (conversational / question-framed)

Axis: Phrasing register — questions instead of imperatives; self-check framing throughout
Hypothesis: Asking the model to answer questions before writing (rather than issuing commands)
forces self-verification at each step, improving C-03/C-04 consistency without
imposing rigid template structure.

```
You are running /topic:report. Your job is to write a status file that someone
can drop into a standup doc or share with stakeholders. Before writing anything,
answer each question below — your answers become the source of truth for the file.

What topic are we reporting on? (If not provided, ask once.)
Is --format teams set? (If yes, you will produce an ASCII card at the end.)

--- QUESTIONS TO ANSWER BEFORE WRITING ---

Q1: What signals are planned for this topic?
Read simulations/{topic}/strategy.md or simulations/TOPICS.md.
List each planned signal with: namespace, skill, owner, priority.

Q2: Which signals have been gathered?
Glob simulations/**/{topic}-* and match files to planned signals.
For each planned signal, state: found or missing.

Q3: What are the exact counts?
State: "X of Y planned signals are complete (Z%)."
State: "N signals are still open."
If N > 0, list each open signal: namespace, skill type, owner.

Q4: Is this topic ready?
Look at your open signals. Are any of them essential?
If yes: the topic is not ready (or conditionally ready if close).
If no: the topic may be ready — confirm all essential signals are done.
State your readiness label and one sentence justification.

Q5: What should happen next?
Look at the highest-priority open signal.
What is the concrete next action? Name the skill and namespace.
If no open signals: the next step is to synthesize with /topic:story.

--- NOW WRITE THE FILE ---

Write simulations/{topic}/status-{date}.md using your answers above.
Frontmatter: skill: topic-report, topic, date.

Structure the file as:
  ## Progress
  Table from Q2 answers. Columns: Namespace | Skill | Status | Owner.
  Summary row with count and percentage from Q3.

  ## Open Signals
  List from Q3. namespace/skill (owner).
  "None" if Q3 found no open signals.

  ## Readiness
  Label + sentence from Q4. Must be consistent with Q3 counts.

  ## Next Step
  Your answer to Q5. One sentence. Specific skill and namespace.

If --format teams:
  Instead of markdown, render an ASCII card.
  No backticks, no # headers, no angle brackets.
  Max 40 lines. Max 80 chars per line.
  Use plain pipes and dashes for table borders.
  Include all four sections.

Finish with: "Report written to simulations/{topic}/status-{date}.md"
```

---

## V-05: Combined (section-locked + discover-first + blocker-naming)

Axis: Combined — section locking (V-02) + phased discovery gate (V-03) + explicit blocker enumeration before readiness
Hypothesis: Locking counts first, enforcing named slots second, and requiring an explicit
BLOCKERS list before the readiness statement is written together produce the strongest
C-04/C-09 signal: a readiness statement that names its own blocking signals.

```
You are running /topic:report.
This skill writes a shareable status artifact for a topic.
Execution has three phases: DISCOVER, BLOCKERS, RENDER.
You must complete each phase in order. Do not skip ahead.

INPUTS:
- Topic name (required). Ask once if absent.
- --format teams (optional flag).

=== PHASE 1: DISCOVER ===

1a. Glob simulations/**/{topic}-* — collect all artifact paths.

1b. Read simulations/{topic}/strategy.md (or simulations/TOPICS.md for this topic).
    Extract: namespace, skill, item name, priority (essential/recommended/optional), owner.

1c. Cross-reference 1a against 1b.
    For each planned signal: mark DONE (matching artifact found) or OPEN (not found).
    Matching rule: artifact path must contain both the namespace folder and the skill name.

1d. CHECKPOINT — state before continuing:
    "DISCOVER: {total_done}/{total_planned} complete ({pct}%). Open: {list namespace/skill for each OPEN signal}"

=== PHASE 2: BLOCKERS ===

2a. From your OPEN signals, identify which are essential priority.
2b. State:
    "BLOCKERS: {list each essential OPEN signal as namespace/skill}"
    If no essential signals are open: "BLOCKERS: none (all essential signals complete)"

This BLOCKERS list will be used verbatim in the readiness statement.
Do not revise it during RENDER.

=== PHASE 3: RENDER ===

--- Default format ---
Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

### SLOT 1 — PROGRESS TABLE
Markdown table. Columns: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Values from PHASE 1 only — do not re-derive.
Final row (bold): **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if unknown.

### SLOT 2 — OPEN SIGNALS
List every OPEN signal. Each entry: `namespace/skill (owner)`.
If total_open == 0: "None — all planned signals gathered."

### SLOT 3 — READINESS
Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
The sentence must reference the BLOCKERS list from PHASE 2 by name.
Example: "Not ready — missing prove-analysis (prove) and review-design (review)."
If BLOCKERS is empty: "Ready — all essential signals are present."

### SLOT 4 — NEXT STEP
One concrete action. Must name skill and namespace.
Source: highest-priority entry from SLOT 2.
If SLOT 2 is empty: "Run /topic:story to synthesize all gathered signals."
Generic steps ("gather more signals") are not acceptable.

--- --format teams branch ---

Produce a single ASCII card. Rules:
- No markdown headers, no fenced code, no backticks, no angle brackets
- Max 40 lines / 80 chars per line
- Table borders: + - | only

Card structure:
  Line 1:    TOPIC REPORT: {topic}
  Line 2:    DATE: {date}
  Line 3:    (blank)
  Lines 4+:  Progress table (condensed: Namespace | Skill | Status | Owner)
  Then:      OPEN ({total_open}): list namespace/skill (owner) per line
  Then:      READINESS: {label} -- {blocker names if any}
  Then:      NEXT: {concrete action}

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```
