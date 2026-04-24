Now I have enough context. Let me write all 5 variations.

---

## Quest Variate — signal-setup — Round 3

**Variation axes selected:**
- **Single-axis**: Lifecycle Emphasis (V-01), Inertia Framing (V-02), Phrasing Register (V-03)
- **Combination**: Role Sequence + Output Format (V-04), Inertia Framing + Decline Consequence (V-05)

---

## V-01: Lifecycle Emphasis

**Axis**: Explicit numbered gate checkpoints as structural skeleton. Each phase is a labeled gate; no phase can be implicitly skipped. Edge cases (already configured, missing CLAUDE.md) are promoted to dedicated gates, not inline conditionals.
**Hypothesis**: Making gates first-class structure forces completeness — the skill cannot skip detection or confirmation because the gates are enumerated in the spec itself.

---

```
You are running /signal-setup.

Configure Signal in this workspace after installation. Proceed through the gates below
in order. Do not advance past a gate until its condition is met.

---

GATE 1: DETECT WORKSPACE FILES

Read the following files if they exist:
- CLAUDE.md (workspace root)
- .github/copilot-instructions.md

For each file, report:
- EXISTS or MISSING
- If EXISTS: does it already contain a "## Signal" section? (YES / NO)

Do not write anything yet.

---

GATE 2: ALREADY-CONFIGURED CHECK

If CLAUDE.md exists AND already contains a "## Signal" section:
  Output: "Signal section detected in CLAUDE.md. Already configured. No changes needed."
  Ask: "Would you like to view the existing Signal section?"
  STOP — do not proceed to Gate 3.

If .github/copilot-instructions.md exists AND already contains a Signal reference:
  Note this for Gate 6 (Copilot path will also be skipped).

---

GATE 3: MISSING FILE CHECK

If CLAUDE.md is MISSING:
  Output: "CLAUDE.md not found in the workspace root."
  Ask: "Should I create CLAUDE.md with the Signal section, or create Signal as a standalone
  signal.md instead?"
  Wait for user response before proceeding.

  If user chooses CLAUDE.md: set target = new CLAUDE.md
  If user chooses standalone: set target = signal.md
  If user declines: Output "Setup cancelled. Signal not configured." STOP.

If CLAUDE.md EXISTS and not already configured: set target = CLAUDE.md, proceed to Gate 4.

---

GATE 4: PREVIEW

Display the exact content that will be appended (or written) to the target file.

The Signal section must include:
1. A one-line description of what Signal does
2. The full list of available skills, grouped by namespace (scout, draft, review, flow,
   trace, prove, listen, program, topic, quest, mock, org)
3. The inertia rule, stated explicitly:
   "A topic is ready when /topic-status shows green coverage across the namespaces in its
   strategy. Inertia — shipping without sufficient signal — is the primary risk Signal
   addresses."
4. A quick-start line: Run /topic-new <feature> to begin.

Output the preview enclosed in a fenced markdown block so the user can read it exactly.

---

GATE 5: CONFIRM WRITE

After displaying the preview, ask:
  "Write this Signal section to [target filename]? (yes / no)"

Do not proceed until user responds.
- If yes: proceed to Gate 6.
- If no: Output "No changes made. Signal not configured. Inertia remains unaddressed."
  STOP.

---

GATE 6: COPILOT CHECK

Ask: "Would you also like to add a Signal reference to .github/copilot-instructions.md?"

If yes:
  If the file does not exist: note that you will create it.
  If the file already has a Signal reference: Output "Copilot instructions already
  reference Signal. Skipping."
  Otherwise: append a brief Signal reference (one paragraph, listing namespaces and
  the inertia rule).

If no: skip without comment.

---

GATE 7: WRITE

Append (or write) the Signal section to the target file.
The written content must be byte-for-byte identical to the preview shown in Gate 4.

If Copilot update was confirmed in Gate 6: write that file too.

---

GATE 8: REPORT

Output a final status block:

  SIGNAL SETUP COMPLETE
  ---------------------
  CLAUDE.md           : [appended / created / skipped]
  Copilot instructions: [appended / created / skipped]

  Run /topic-new <feature> to begin gathering signals.
```

---

## V-02: Inertia Framing

**Axis**: The skill itself opens with a motivational preamble — inertia as the named competitor — before any procedural steps. The philosophy of *why* setup matters is front-loaded, not buried in the appended content.
**Hypothesis**: Leading with the inertia framing converts the skill from a mechanical installer into a context-setting artifact. The user understands what Signal is *for* before being asked to confirm anything.

---

```
You are running /signal-setup.

---

Every feature decision has a silent competitor: the choice to ship without enough
information. Teams call it "we already know what we're building." Signal calls it
inertia.

Signal exists to defeat inertia before it defeats the feature. It does this by
accumulating evidence — across scouting, drafting, reviewing, tracing, and listening
— and synthesizing that evidence into a topic story. The topic story tells you whether
you know what you know, or whether you are guessing.

But Signal can only do this if it is present in your workspace. /signal-setup makes
it present. Until setup runs, inertia has no named opponent in your CLAUDE.md.

---

SETUP SEQUENCE

Step 1 — Detect

Check for these files in the workspace root:
- CLAUDE.md
- .github/copilot-instructions.md

For each: report EXISTS or MISSING. For CLAUDE.md, check whether a "## Signal" section
already exists.

Step 2 — Already Configured?

If CLAUDE.md already contains a "## Signal" section:
  Say: "Signal is already configured in this workspace. Inertia already has a named
  opponent here."
  Offer to display the existing section. STOP.

Step 3 — Handle Missing CLAUDE.md

If CLAUDE.md does not exist:
  Say: "No CLAUDE.md found. Signal can create one, or append to a file you name."
  Ask: "Create CLAUDE.md with the Signal section? (yes / no / use different file)"
  Wait for response. If declined, say: "Setup cancelled." STOP.

Step 4 — Preview

Show the exact text that will be written. The Signal section must contain:

- Opening line: "Signal is installed. Use these skills to gather evidence before
  committing to a feature."
- The inertia rule: "The inertia rule: a topic is ready when /topic-status shows
  green coverage across the namespaces in its strategy. Ship without this and inertia
  wins."
- Full skill list grouped by namespace:

  Scout (8 skills): /scout-competitors, /scout-feasibility, /scout-naming,
  /scout-compliance, /scout-market, /scout-stakeholders, /scout-positioning,
  /scout-requirements

  Draft (4 skills): /draft-spec, /draft-proposal, /draft-pitch, /draft-brainstorm

  Review (4 skills): /review-design, /review-code, /review-users, /review-customers

  Flow (7 skills): /flow-lifecycle, /flow-conversation, /flow-trigger, /flow-dataflow,
  /flow-integration, /flow-throttle, /flow-resilience

  Trace (7 skills): /trace-request, /trace-state, /trace-contract, /trace-component,
  /trace-deployment, /trace-migration, /trace-permissions

  Prove (9 skills): /prove-hypothesis, /prove-websearch, /prove-intelligence,
  /prove-prototype, /prove-analysis, /prove-interview, /prove-synthesize,
  /prove-publish, /prove-topic

  Listen (3 skills): /listen-feedback, /listen-support, /listen-adoption

  Program (2 skills): /program-plan, /prove-program

  Topic (6 skills): /topic-new, /topic-status, /topic-report, /topic-plan,
  /topic-story, /topic-echo

  Quest (4 skills): /quest-rubric, /quest-variate, /quest-score, /quest-golden

  Mock (3 skills): /mock-all, /mock-ns, /mock-review

  Org (4 skills): /org-roles, /org-chart, /org-review, /org-committee

- Quick start: "Run /topic-new <feature> to register a topic and build a coverage plan."

Display this in a fenced block.

Step 5 — Confirm

Ask: "Write this to CLAUDE.md? (yes / no)"
Do not write without a yes.

If no: say "Setup cancelled. Signal not configured. Inertia remains unaddressed in
this workspace."
STOP.

Step 6 — Copilot

Ask: "Also update .github/copilot-instructions.md? (yes / no)"
If yes: append a Signal paragraph referencing the namespaces and the inertia rule.
If the file already has Signal: say "Copilot instructions already configured. Skipping."

Step 7 — Write

Append the previewed content to CLAUDE.md.
Write copilot-instructions.md if confirmed.
The written content must match the preview exactly.

Step 8 — Report

  SIGNAL SETUP COMPLETE
  CLAUDE.md: Signal section appended.
  [Copilot instructions: updated / skipped]

  Inertia now has a named opponent in this workspace.
  Run /topic-new <feature> to begin.
```

---

## V-03: Phrasing Register

**Axis**: Conversational, imperative register throughout — direct second-person instructions, minimal headers, no ceremony. The skill reads like a colleague giving you a quick walkthrough, not a formal specification.
**Hypothesis**: Conversational phrasing reduces friction during the first run. Users scan and follow rather than parse. May trade structural explicitness (C-11) for approachability.

---

```
You are running /signal-setup.

Let's get Signal configured in your workspace. This takes about 30 seconds.

---

First, check what's already here.

Look for CLAUDE.md in the workspace root. Also look for .github/copilot-instructions.md.
Tell me what you find: does each file exist, and does CLAUDE.md already have a Signal
section in it?

---

If CLAUDE.md already has a Signal section, you're done. Tell the user Signal is already
set up and offer to show them what's there.

If there's no CLAUDE.md at all, ask the user: "I don't see a CLAUDE.md here. Want me to
create one, or is there a different file you want me to update?" Wait for their answer.

---

Once you know the target file, show the user exactly what you're about to add. Put it
in a code block so they can read every line.

The content to add:

## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
you commit to a feature.

**The inertia rule**: A topic is ready when `/topic-status` shows green coverage
across the namespaces in its strategy. Until then, shipping means betting on what
you think you know — and inertia wins.

**Quick start**: Run `/topic-new <feature>` to register a topic and get a coverage plan.

### Skills by namespace

**Scout** — discover before you design
`/scout-competitors` `/scout-feasibility` `/scout-naming` `/scout-compliance`
`/scout-market` `/scout-stakeholders` `/scout-positioning` `/scout-requirements`

**Draft** — articulate before you build
`/draft-spec` `/draft-proposal` `/draft-pitch` `/draft-brainstorm`

**Review** — pressure-test before you ship
`/review-design` `/review-code` `/review-users` `/review-customers`

**Flow** — simulate domain processes
`/flow-lifecycle` `/flow-conversation` `/flow-trigger` `/flow-dataflow`
`/flow-integration` `/flow-throttle` `/flow-resilience`

**Trace** — trace platform behavior
`/trace-request` `/trace-state` `/trace-contract` `/trace-component`
`/trace-deployment` `/trace-migration` `/trace-permissions`

**Prove** — investigate before you decide
`/prove-hypothesis` `/prove-websearch` `/prove-intelligence` `/prove-prototype`
`/prove-analysis` `/prove-interview` `/prove-synthesize` `/prove-publish`
`/prove-topic`

**Listen** — anticipate post-ship signals
`/listen-feedback` `/listen-support` `/listen-adoption`

**Program** — orchestrate multi-skill campaigns
`/program-plan` `/prove-program`

**Topic** — manage the narrative
`/topic-new` `/topic-status` `/topic-report` `/topic-plan` `/topic-story`
`/topic-echo`

**Quest** — optimize your skills
`/quest-rubric` `/quest-variate` `/quest-score` `/quest-golden`

**Mock** — generate synthetic coverage
`/mock-all` `/mock-ns` `/mock-review`

**Org** — simulate organizational dynamics
`/org-roles` `/org-chart` `/org-review` `/org-committee`

---

After showing the preview, ask: "Look good? Should I write this to [filename]?"

Don't write anything until they say yes.

If they say no, just say: "No changes made. You can re-run /signal-setup whenever
you're ready."

---

If they said yes, write it. Make sure what you write matches the preview exactly —
no additions, no omissions.

---

After writing, ask: "Want me to also add a Signal reference to
.github/copilot-instructions.md?" If yes, write a short paragraph there referencing
Signal's namespaces and the inertia rule. If that file already mentions Signal,
skip and tell them.

---

Wrap up with a quick status line:

  Done. CLAUDE.md updated with the Signal section.
  [Copilot instructions updated / skipped.]
  Run /topic-new <feature> to get started.
```

---

## V-04: Role Sequence + Output Format

**Axis**: Detection runs first and produces a structured status table before any other action. The table makes the workspace state legible at a glance. Confirmation is phrased as a decision off the table, not a blind prompt.
**Hypothesis**: Surfacing detection output as a table (rather than prose) makes the pre-write state explicit and reviewable. The user can see exactly what will change before being asked. May improve trust in the idempotency check (C-05) and the preview-matches-write contract (C-09).

---

```
You are running /signal-setup.

---

PHASE 1: WORKSPACE SCAN

Scan the workspace root for configuration files. After scanning, output this status
table — fill in each cell based on what you find:

| File                                | Exists | Signal section present |
|-------------------------------------|--------|------------------------|
| CLAUDE.md                           |        |                        |
| .github/copilot-instructions.md     |        |                        |

For "Signal section present": check whether the file contains a line starting with
"## Signal". Mark YES, NO, or N/A (if file does not exist).

---

PHASE 2: ROUTING

Read the table you just produced and route accordingly:

Route A — CLAUDE.md exists, Signal section already present:
  Say: "Signal is already configured in CLAUDE.md. No write needed."
  Offer to display the current section contents.
  Proceed to Phase 5 (report). Skip Phases 3 and 4.

Route B — CLAUDE.md exists, Signal section NOT present:
  Proceed to Phase 3.

Route C — CLAUDE.md does not exist:
  Say: "CLAUDE.md not found."
  Ask: "Should I create CLAUDE.md with the Signal section, or use a different filename?"
  Wait for user response.
  If user specifies a filename: use that as the target and proceed to Phase 3.
  If user declines: say "Setup cancelled." Proceed to Phase 5 (report). Skip Phases 3 and 4.

---

PHASE 3: PREVIEW

Display the exact text to be written, in a fenced markdown block:

  ## Signal

  Signal is installed in this workspace. Know what you know before you commit.

  **Inertia rule**: A topic is ready when `/topic-status` shows green coverage across
  its strategy namespaces. Inertia — the choice to ship without sufficient signal —
  is the default. Signal is the override.

  **Quick start**: `/topic-new <feature>` registers a topic and creates a coverage plan.

  **Skills**

  | Namespace | Count | Skills |
  |-----------|-------|--------|
  | scout     | 8  | /scout-competitors /scout-feasibility /scout-naming /scout-compliance /scout-market /scout-stakeholders /scout-positioning /scout-requirements |
  | draft     | 4  | /draft-spec /draft-proposal /draft-pitch /draft-brainstorm |
  | review    | 4  | /review-design /review-code /review-users /review-customers |
  | flow      | 7  | /flow-lifecycle /flow-conversation /flow-trigger /flow-dataflow /flow-integration /flow-throttle /flow-resilience |
  | trace     | 7  | /trace-request /trace-state /trace-contract /trace-component /trace-deployment /trace-migration /trace-permissions |
  | prove     | 9  | /prove-hypothesis /prove-websearch /prove-intelligence /prove-prototype /prove-analysis /prove-interview /prove-synthesize /prove-publish /prove-topic |
  | listen    | 3  | /listen-feedback /listen-support /listen-adoption |
  | program   | 2  | /program-plan /prove-program |
  | topic     | 6  | /topic-new /topic-status /topic-report /topic-plan /topic-story /topic-echo |
  | quest     | 4  | /quest-rubric /quest-variate /quest-score /quest-golden |
  | mock      | 3  | /mock-all /mock-ns /mock-review |
  | org       | 4  | /org-roles /org-chart /org-review /org-committee |

After showing the preview, also show a write-plan table:

  | Action                              | Target                               | Status   |
  |-------------------------------------|--------------------------------------|----------|
  | Append Signal section               | CLAUDE.md                            | PENDING  |
  | Append Signal reference (optional)  | .github/copilot-instructions.md      | PENDING  |

Ask: "Proceed with the actions marked PENDING? (yes / no / yes but skip copilot)"

Do not write until user responds.
If no: mark all rows CANCELLED in the table and output it. Say "No changes made."
STOP.

---

PHASE 4: WRITE

For each PENDING action confirmed by the user:
  - Write the content.
  - Update the action's Status in the write-plan table to DONE or SKIPPED.

The Signal section written to CLAUDE.md must be byte-for-byte identical to the
preview shown in Phase 3.

For .github/copilot-instructions.md:
  - If it already contains a Signal reference: mark row as ALREADY CONFIGURED and skip.
  - If the file does not exist and the user confirmed: create it.

After writing, output the completed write-plan table with all statuses filled in.

---

PHASE 5: REPORT

Output a final summary:

  SIGNAL SETUP — [COMPLETE / CANCELLED / ALREADY CONFIGURED]

  [table from Phase 4 if write occurred, or explanation if skipped]

  Next step: Run /topic-new <feature> to register a topic.
```

---

## V-05: Inertia Framing + Decline Consequence

**Axis (combination)**: Inertia framing (C-13) + decline path names its consequence (C-14). The skill opens with three paragraphs of motivational philosophy before any instructions. The decline path explicitly names what the user is accepting — not just acknowledging the non-action.
**Hypothesis**: Together these two patterns make setup feel like a decision with stakes, not a mechanical installer. The opening preamble establishes *why*, and the decline consequence completes the arc by naming *what is foregone*. A user who reads the decline message understands they are choosing inertia, not just pressing Cancel.

---

```
You are running /signal-setup.

---

Before any feature ships, there is a moment where the team could stop and ask: do we
know what we're building? Not in the sense of having wireframes or a ticket — but in
the deeper sense of having evidence. Have we scouted the competitive landscape? Have
we simulated the failure modes? Have we heard from the personas who will actually use
this?

Most teams skip that moment. Not because they are careless, but because the cost of
skipping is invisible at the time. The cost appears later, in support tickets, in
adoption curves that flatten, in the feature that shipped and quietly never got used.
Signal calls this inertia: the default state of shipping without sufficient signal.

/signal-setup puts Signal's tools into your CLAUDE.md so they are present and named
when that moment arrives. A workspace without Signal configured is a workspace where
inertia has no named opponent. This skill names it.

---

STEP 1: DETECT

Read the following files if they exist in the workspace root:
- CLAUDE.md
- .github/copilot-instructions.md

Report:
- CLAUDE.md: EXISTS or MISSING
- CLAUDE.md Signal section: PRESENT or ABSENT (if file exists)
- copilot-instructions.md: EXISTS or MISSING

---

STEP 2: ALREADY CONFIGURED?

If CLAUDE.md exists and already contains a "## Signal" section:
  Say: "Signal is already configured in this workspace. Inertia already has a named
  opponent here."
  Offer to show the current section.
  STOP.

---

STEP 3: MISSING CLAUDE.MD?

If CLAUDE.md does not exist:
  Say: "No CLAUDE.md found. I can create one, or append the Signal section to a file
  you specify."
  Ask: "Create CLAUDE.md? (yes / specify filename / no)"
  Wait for response.

  If no or no response: say "Setup cancelled. Signal not configured. Inertia remains
  the default in this workspace — there is no named opponent for the choice to ship
  without evidence."
  STOP.

---

STEP 4: PREVIEW

Show the exact text to be appended, in a fenced block. Do not write yet.

The content must include all of the following:

  ## Signal

  Signal is installed in this workspace. Use these skills to gather evidence before
  you commit to a feature.

  **The inertia rule**: A topic is ready when `/topic-status` shows green coverage
  across the namespaces in its strategy. Inertia — shipping before that threshold —
  is the primary risk Signal exists to address. Do not ship on assumption when you
  can ship on signal.

  **Quick start**: Run `/topic-new <feature>` to register a topic and build a
  coverage plan.

  ### Available skills

  **Scout** (8) — discover before you design
  `/scout-competitors` `/scout-feasibility` `/scout-naming` `/scout-compliance`
  `/scout-market` `/scout-stakeholders` `/scout-positioning` `/scout-requirements`

  **Draft** (4) — articulate before you build
  `/draft-spec` `/draft-proposal` `/draft-pitch` `/draft-brainstorm`

  **Review** (4) — pressure-test before you ship
  `/review-design` `/review-code` `/review-users` `/review-customers`

  **Flow** (7) — simulate domain processes
  `/flow-lifecycle` `/flow-conversation` `/flow-trigger` `/flow-dataflow`
  `/flow-integration` `/flow-throttle` `/flow-resilience`

  **Trace** (7) — trace platform behavior
  `/trace-request` `/trace-state` `/trace-contract` `/trace-component`
  `/trace-deployment` `/trace-migration` `/trace-permissions`

  **Prove** (9) — investigate before you decide
  `/prove-hypothesis` `/prove-websearch` `/prove-intelligence` `/prove-prototype`
  `/prove-analysis` `/prove-interview` `/prove-synthesize` `/prove-publish`
  `/prove-topic`

  **Listen** (3) — anticipate post-ship signals
  `/listen-feedback` `/listen-support` `/listen-adoption`

  **Program** (2) — orchestrate multi-skill campaigns
  `/program-plan` `/prove-program`

  **Topic** (6) — manage the narrative
  `/topic-new` `/topic-status` `/topic-report` `/topic-plan` `/topic-story`
  `/topic-echo`

  **Quest** (4) — optimize your skills
  `/quest-rubric` `/quest-variate` `/quest-score` `/quest-golden`

  **Mock** (3) — generate synthetic coverage
  `/mock-all` `/mock-ns` `/mock-review`

  **Org** (4) — simulate organizational dynamics
  `/org-roles` `/org-chart` `/org-review` `/org-committee`

---

STEP 5: CONFIRM

After showing the preview, ask:
  "Write this Signal section to [target filename]? (yes / no)"

Do not write without a yes.

If yes: proceed to Step 6.

If no:
  Say: "Setup cancelled. Signal not configured. Inertia remains the default in this
  workspace. The 47 skills listed above will not be advertised to Claude Code, and
  the inertia rule will not be enforced at the point of decision. You can re-run
  /signal-setup at any time to change this."
  STOP.

---

STEP 6: COPILOT

Ask: "Also update .github/copilot-instructions.md with a Signal reference? (yes / no)"

If yes:
  If file does not exist: create it.
  If file already references Signal: say "Copilot instructions already configured.
  Skipping."
  Otherwise: append one paragraph:
    "Signal is installed. Use Signal skills (/scout, /draft, /review, /flow, /trace,
    /prove, /listen, /program, /topic) to gather evidence before committing to a
    feature. The inertia rule: a topic is ready when /topic-status shows green
    coverage. Ship on signal, not assumption."

If no: skip.

---

STEP 7: WRITE

Append the Signal section to the target file. The written content must be
byte-for-byte identical to the preview in Step 4.

Write copilot-instructions.md if confirmed.

---

STEP 8: REPORT

  SIGNAL SETUP COMPLETE
  ---------------------
  CLAUDE.md              : Signal section appended. [filename]
  Copilot instructions   : [updated / skipped]

  Inertia now has a named opponent in this workspace.
  Run /topic-new <feature> to begin gathering signals.
```

---

## Variation Summary

| Variation | Axis | C-13 target | C-14 target | C-11 target | C-12 target | Register |
|-----------|------|-------------|-------------|-------------|-------------|----------|
| V-01 | Lifecycle Emphasis | No | Partial | Strong | Strong | Formal |
| V-02 | Inertia Framing | Strong | No | Moderate | Moderate | Philosophical |
| V-03 | Phrasing Register | No | Partial | Weak | Moderate | Conversational |
| V-04 | Role Sequence + Output Format | No | No | Moderate | Moderate | Technical/tabular |
| V-05 | Inertia + Decline Consequence | Strong | Strong | Moderate | Moderate | Philosophical + consequentialist |

**Expected top performer**: V-05 — only variation directly targeting both new aspirational criteria (C-13, C-14) in combination. V-01 likely scores highest on C-11/C-12 (gate structure). V-04 likely scores best on C-09 (preview-matches-write, because the write-plan table makes the contract explicit).
