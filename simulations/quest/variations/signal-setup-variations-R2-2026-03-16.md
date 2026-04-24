# Quest Variate — signal-setup (Round 2)

Five complete, runnable skill body prompts. V-01, V-02, V-03 are single-axis. V-04 and V-05 are combined.

---

## V-01: Lifecycle Emphasis — Named Gate Checkpoints

**Axis**: Lifecycle emphasis
**Hypothesis**: Explicit numbered gates with pass/fail conditions make phase boundaries impossible to skip, directly satisfying C-11 and C-12. Each edge case gets its own gate rather than an inline branch.

---

You are configuring Signal in this workspace. Execute the gates below in strict order. Each gate must complete before the next begins. An edge-case gate exits the skill entirely — never falls through to the happy path.

---

### GATE 1 — DETECT

Read these two files:

- `CLAUDE.md` (workspace root)
- `.github/copilot-instructions.md`

For each, record:
1. Exists: yes / no
2. If exists — contains Signal section: yes / no
   (Signal section marker: `## Signal` or the string `signal-topic`)

Output a detection report before proceeding:

```
DETECTION REPORT
CLAUDE.md:                        [found | not found]
  Signal section present:         [yes | no | n/a]
.github/copilot-instructions.md:  [found | not found]
  Signal section present:         [yes | no | n/a]
```

---

### GATE 2A — ALREADY CONFIGURED *(edge case — exits skill)*

**Trigger**: CLAUDE.md exists AND contains a Signal section.

Output:
> "Signal is already configured in CLAUDE.md. No changes needed."

If `.github/copilot-instructions.md` also contains a Signal section:
> "GitHub Copilot instructions also already configured."

**Stop. Do not proceed to any further gate.**

---

### GATE 2B — MISSING CLAUDE.md *(edge case — modifies write behavior)*

**Trigger**: CLAUDE.md does not exist.

Output:
> "No CLAUDE.md found. Signal will create one containing only the Signal section."

Set mode: **CREATE** (not append). Continue to Gate 3.

---

### GATE 3 — PREVIEW

Display the exact content to be written. Label it clearly: `PREVIEW — this is exactly what will be written`.

````
## Signal — AI Evidence-Gathering Skills

Signal gathers structured evidence before you commit to a feature.
Nine namespaces. Each artifact a signal toward your decision.

**Available skills:**
- /signal-scout    — scout (competitors, market, feasibility, requirements,
                     compliance, stakeholders, naming, positioning)
- /signal-draft    — draft (brainstorm, spec, proposal, pitch)
- /signal-review   — review (code, design, customers, users)
- /signal-flow     — flow (lifecycle, trigger, throttle, resilience,
                     dataflow, integration, conversation)
- /signal-trace    — trace (permissions, state, contract, request, component,
                     deployment, migration)
- /signal-prove    — prove (topic, hypothesis, analysis, prototype, interview,
                     websearch, intelligence, synthesize, program, publish)
- /signal-listen   — listen (support, feedback, adoption)
- /signal-program  — program (plan)
- /signal-topic    — topic (new, plan, echo, status, story, report)

**Inertia Rule:** The default decision is to not ship. Inertia — the pull toward
delay — must be overcome by evidence. When /signal-topic shows sufficient signals
across the relevant namespaces, you have overcome inertia. Until then, do not commit.
````

---

### GATE 4 — CONFIRM

Ask:
> "Append this Signal section to CLAUDE.md? (yes / no)"

If `.github/copilot-instructions.md` was found (Gate 1) and has no Signal section:
> "Also update .github/copilot-instructions.md? (yes / no)"

Wait for explicit responses. If the answer to CLAUDE.md is no:
> "No changes made."
**Stop.**

---

### GATE 5 — WRITE AND REPORT

Write the content from Gate 3 **exactly as previewed — no modifications**.

- CLAUDE.md: append if existed (Gate 1), create if missing (Gate 2B)
- `.github/copilot-instructions.md`: append if confirmed in Gate 4

Output a results report:

```
SETUP COMPLETE
CLAUDE.md:                        [appended | created | skipped]
.github/copilot-instructions.md:  [appended | skipped | not found]

Next: Run /signal-topic new to create your first topic.
```

---

## V-02: Output Format — Table-Heavy Structured Preview

**Axis**: Output format
**Hypothesis**: Replacing prose instructions with tables throughout makes the state machine scannable, reduces ambiguity in detection output, and forces the preview content to be visually distinct from explanatory text — supporting C-02 and C-09.

---

You are the Signal setup assistant. Your output format throughout is: tables for state, code blocks for content, labeled sections for phases. Every output must be scannable at a glance. No prose where a table will do.

---

### Step 1: Scan

Read `CLAUDE.md` and `.github/copilot-instructions.md`. Produce this table (fill all cells):

| File | Exists | Contains Signal Section |
|------|--------|------------------------|
| `CLAUDE.md` | yes / no | yes / no / n/a |
| `.github/copilot-instructions.md` | yes / no | yes / no / n/a |

Output this table before doing anything else.

---

### Step 2: Determine Path

Based on the scan table, select exactly one path:

| Condition | Path |
|-----------|------|
| CLAUDE.md has Signal section | **SKIP** — already configured |
| CLAUDE.md exists, no Signal section | **APPEND** — add to existing file |
| CLAUDE.md does not exist | **CREATE** — new file |

State which path applies. If **SKIP**:

> "Signal already configured in CLAUDE.md. No changes needed."

Also note: if `.github/copilot-instructions.md` also has a Signal section, say so. Then **stop**.

---

### Step 3: Preview

Show the Signal section as a labeled code block. This exact content — unchanged — is what will be written.

**PREVIEW:**

````markdown
## Signal — AI Evidence-Gathering Skills

Signal gathers structured evidence before you commit to a feature.
Nine namespaces cover the full decision surface.

**Available skills:**

| Namespace | Sub-skills |
|-----------|------------|
| /signal-scout | competitors, market, feasibility, requirements, compliance, stakeholders, naming, positioning |
| /signal-draft | brainstorm, spec, proposal, pitch |
| /signal-review | code, design, customers, users |
| /signal-flow | lifecycle, trigger, throttle, resilience, dataflow, integration, conversation |
| /signal-trace | permissions, state, contract, request, component, deployment, migration |
| /signal-prove | topic, hypothesis, analysis, prototype, interview, websearch, intelligence, synthesize, program, publish |
| /signal-listen | support, feedback, adoption |
| /signal-program | plan |
| /signal-topic | new, plan, echo, status, story, report |

**Inertia Rule:** Not shipping is always the easier choice. Signal exists to build
evidence strong enough to overcome that inertia. Use /signal-topic to assess whether
you have sufficient signals to commit. If not, inertia wins — and that is correct.
````

---

### Step 4: Confirm

Present a pending-actions table:

| Action | Target | Awaiting |
|--------|--------|---------|
| Append / Create Signal section | `CLAUDE.md` | Your confirmation |
| Append Signal section | `.github/copilot-instructions.md` | Your answer (if file exists) |

Ask:
> "Confirm: write Signal section to CLAUDE.md? (yes / no)"

If `.github/copilot-instructions.md` was found in Step 1 without a Signal section:
> "Also update .github/copilot-instructions.md? (yes / no)"

Do not write until answers received. If CLAUDE.md is declined: output "No changes made." and stop.

---

### Step 5: Write and Report

Write the previewed content **without modification**. Then output a results table:

| File | Action Taken | Outcome |
|------|-------------|---------|
| `CLAUDE.md` | appended / created / skipped | done / skipped |
| `.github/copilot-instructions.md` | appended / skipped / not found | done / skipped |

Final status: `Signal setup complete. Run /signal-topic new to begin.`

---

## V-03: Phrasing Register — Conversational/Imperative

**Axis**: Phrasing register
**Hypothesis**: Plain, direct language with "I/you" framing reduces cognitive load and makes the confirmation step feel like a real conversation — improving the user's mental model of what the skill is doing, especially for first-time setup.

---

You're helping someone set up Signal in their workspace. Talk like a helpful colleague: direct, practical, plain. Use first person where it reads naturally. Keep sentences short.

Here's the sequence. Follow it exactly — don't skip steps, don't combine them.

---

**Step 1 — Check what's already here.**

Look for two files:
- `CLAUDE.md` in the workspace root
- `.github/copilot-instructions.md`

Tell the user what you found, in plain terms:
- "I found CLAUDE.md." or "No CLAUDE.md here yet."
- "I found .github/copilot-instructions.md." or "No Copilot instructions file."

Now check whether either file already has a Signal section (look for `## Signal` or `signal-topic`).

If CLAUDE.md already has a Signal section, stop here:
> "Signal is already set up in this workspace. Nothing to do — I'll leave it as-is."

If `.github/copilot-instructions.md` also has one, mention that too. Then stop.

---

**Step 2 — Show them exactly what you'll add.**

Before touching anything, show the Signal section. Make it clear this is a preview — not something you've written yet.

Say: "Here's exactly what I'll add:"

---

## Signal — AI Evidence-Gathering Skills

Signal helps you gather evidence before committing to a feature. Nine namespaces, each focused on a different part of the decision.

**Skills you can run:**
- `/signal-scout` — research the landscape (competitors, market, feasibility, requirements, compliance, stakeholders, naming, positioning)
- `/signal-draft` — generate draft artifacts (brainstorm, spec, proposal, pitch)
- `/signal-review` — review what you have (code, design, customers, users)
- `/signal-flow` — analyze system behavior (lifecycle, trigger, throttle, resilience, dataflow, integration, conversation)
- `/signal-trace` — trace internals (permissions, state, contract, request, component, deployment, migration)
- `/signal-prove` — run investigations (topic, hypothesis, analysis, prototype, interview, websearch, intelligence, synthesize, program, publish)
- `/signal-listen` — gather qualitative input (support, feedback, adoption)
- `/signal-program` — coordinate the program (plan)
- `/signal-topic` — manage the topic (new, plan, echo, status, story, report)

**The inertia rule:** Not shipping is always the path of least resistance. That's inertia. Signal exists so you can build enough evidence that shipping becomes the stronger case. Run `/signal-topic` to check whether you've gathered enough signals to overcome inertia and commit.

---

Then say: "That's it — nothing extra, nothing changed from what you see."

If there's no CLAUDE.md, add: "Since there's no CLAUDE.md yet, I'll create one with just this section in it."

---

**Step 3 — Ask before writing anything.**

Don't write a thing yet. Ask:
> "Should I add this to CLAUDE.md? (yes / no)"

If `.github/copilot-instructions.md` exists without a Signal section, also ask:
> "Want me to update .github/copilot-instructions.md too? (yes / no)"

Wait for answers. If they say no to CLAUDE.md:
> "Got it — no changes made."

Stop.

---

**Step 4 — Write it exactly as shown, then tell them what you did.**

Append (or create) the file with the same content from Step 2. Don't change a word.

Tell them what happened:
- "Added Signal section to CLAUDE.md."
- "Also updated .github/copilot-instructions.md." (if they confirmed)
- "Skipped .github/copilot-instructions.md." (if they declined or it wasn't found)

Finish with: "You're set. Run `/signal-topic new` to create your first topic and start gathering signals."

---

## V-04: Combined — Role Sequence + Lifecycle Gates

**Axes**: Role sequence + Lifecycle emphasis
**Hypothesis**: Splitting the skill into three named, single-responsibility roles (Detector, Planner, Writer) with explicit hand-off points creates the strongest structural enforcement of phase separation — each role cannot see ahead, which eliminates implicit sequencing and satisfies C-11 while making the Planner the natural home for both edge cases (C-12).

---

Signal setup runs as three sequential roles. Each role has exactly one responsibility. A role does not read ahead or act outside its scope. Complete each role fully before proceeding.

---

## Role 1: DETECTOR

**Responsibility**: Gather facts only. No decisions. No writing. No previews.

**Execute:**
1. Check whether `CLAUDE.md` exists in the workspace root.
2. If it exists, check whether it contains a Signal section (`## Signal` or `signal-topic`).
3. Check whether `.github/copilot-instructions.md` exists.
4. If it exists, check whether it contains a Signal section.

**Output this report — nothing else:**

```
DETECTION REPORT
================
CLAUDE.md:                        [found | not found]
  Signal section present:         [yes | no | n/a]
.github/copilot-instructions.md:  [found | not found]
  Signal section present:         [yes | no | n/a]
```

Hand off the report to Role 2.

---

## Role 2: PLANNER

**Responsibility**: Receive the Detection Report. Decide what happens. Show the preview. Get confirmation. Never write files.

**Case A — Signal section already present in CLAUDE.md:**

Output:
> "Signal is already configured. No action needed."

If Copilot file also has a Signal section: note that too.
**Stop. Do not hand off to Role 3.**

---

**Case B — CLAUDE.md not found:**

Output:
> "No CLAUDE.md found. Signal will create a new one containing only the Signal section."

Proceed to preview.

---

**Case C — CLAUDE.md found, no Signal section:**

Output:
> "CLAUDE.md found. Signal section will be appended."

Proceed to preview.

---

**Preview (Cases B and C):**

Output the following, labeled `PREVIEW — exact content to be written`:

````
## Signal — AI Evidence-Gathering Skills

Signal gathers structured evidence before you commit to a feature.
Nine namespaces. Each artifact a signal toward your decision.

**Available skills:**
- /signal-scout    — scout (competitors, market, feasibility, requirements,
                     compliance, stakeholders, naming, positioning)
- /signal-draft    — draft (brainstorm, spec, proposal, pitch)
- /signal-review   — review (code, design, customers, users)
- /signal-flow     — flow (lifecycle, trigger, throttle, resilience,
                     dataflow, integration, conversation)
- /signal-trace    — trace (permissions, state, contract, request, component,
                     deployment, migration)
- /signal-prove    — prove (topic, hypothesis, analysis, prototype, interview,
                     websearch, intelligence, synthesize, program, publish)
- /signal-listen   — listen (support, feedback, adoption)
- /signal-program  — program (plan)
- /signal-topic    — topic (new, plan, echo, status, story, report)

**Inertia Rule:** The default decision is to not ship. Inertia — the pull toward
delay, the safe choice of waiting — must be overcome by evidence. When /signal-topic
shows sufficient signals across relevant namespaces, you have overcome inertia.
Until then, do not commit.
````

**Confirmation:**

Ask:
> "Append this Signal section to CLAUDE.md? (yes / no)"

If `.github/copilot-instructions.md` was found in the Detection Report without a Signal section:
> "Also update .github/copilot-instructions.md? (yes / no)"

If CLAUDE.md is declined: output `"No changes made."` **Stop.**

If confirmed: hand off to Role 3 with:
- The exact preview text
- The operation for CLAUDE.md (append vs create)
- Whether to update `.github/copilot-instructions.md`

---

## Role 3: WRITER

**Responsibility**: Receive the confirmed plan from Role 2. Execute it exactly. Report outcome.

**Rules:**
- Write the previewed content byte-for-byte. No rewording. No additions.
- CLAUDE.md: append if it existed; create if it was missing.
- `.github/copilot-instructions.md`: append if confirmed in Role 2.

**Output:**

```
SETUP COMPLETE
==============
CLAUDE.md:                        [appended | created | skipped]
.github/copilot-instructions.md:  [appended | skipped | not found]

Signal is active in this workspace.
Next: Run /signal-topic new to create your first topic.
```

---

## V-05: Combined — Inertia Framing Prominent + Edge Cases First-Class

**Axes**: Inertia framing + Edge-case promotion to first-class gates
**Hypothesis**: Leading with the inertia rule as a design principle (not a footnote) primes the user to understand *why* they are running setup — making the confirmation step carry more weight. Promoting edge cases to pre-flight gates before the happy path reduces spec complexity by eliminating nested conditionals entirely (C-12).

---

Signal exists for one reason: to overcome inertia.

The default in any feature decision is to not ship. Waiting is safer. Delay is easy. Inertia is the strongest force in product work — it costs nothing and requires no justification. Signal gives teams a structured way to gather enough evidence that the case for shipping becomes stronger than the case for waiting. The inertia rule is the heart of the plugin: don't commit until `/signal-topic` says you're ready.

This skill installs Signal in your workspace so that Claude Code knows these skills exist and applies the inertia rule when helping you make feature decisions.

---

## Pre-flight: Resolve edge cases before the happy path.

The following gates run first. If either triggers, the skill ends at that gate.

---

### PRE-FLIGHT GATE A — Already Configured

Check: does `CLAUDE.md` exist AND contain a Signal section (`## Signal` or `signal-topic`)?

If yes:
> "Signal is already configured in this workspace. The inertia rule is already active.
> No changes needed."

Also check `.github/copilot-instructions.md`. If it too has a Signal section:
> "GitHub Copilot instructions also configured."

**Skill ends here. The happy path does not run.**

---

### PRE-FLIGHT GATE B — No CLAUDE.md

Check: does `CLAUDE.md` exist?

If no:
> "No CLAUDE.md found. Signal will create one containing only the Signal section."

Set write mode to **CREATE**. Continue to the happy path.

*(If CLAUDE.md does exist and has no Signal section, skip this gate and continue.)*

---

## Happy Path

### Phase 1 — Detect

Both edge cases resolved. Now gather remaining facts:

- Confirm CLAUDE.md state (exists, no Signal section — already established)
- Check `.github/copilot-instructions.md`: exists? Has Signal section?

Report: "CLAUDE.md found — will append. Copilot file: [found / not found]."

---

### Phase 2 — Preview

Show the exact content to be written. Label it: `PREVIEW — this is exactly what gets written`.

````
## Signal — AI Evidence-Gathering Skills

Signal helps you make better commit decisions by gathering structured evidence first.
Nine namespaces form the evidence surface.

**The Inertia Rule (core principle):**
Not shipping is always the easier choice. Signal exists to build evidence strong
enough to overcome that inertia. Run /signal-topic to assess readiness. If you
don't have enough signals, inertia wins — and that is correct behavior.

**Available skills:**

Scout namespace — understand the landscape:
  /signal-scout  competitors | market | feasibility | requirements |
                 compliance | stakeholders | naming | positioning

Draft namespace — generate options:
  /signal-draft  brainstorm | spec | proposal | pitch

Review namespace — evaluate quality:
  /signal-review  code | design | customers | users

Flow namespace — analyze system behavior:
  /signal-flow  lifecycle | trigger | throttle | resilience |
                dataflow | integration | conversation

Trace namespace — inspect internals:
  /signal-trace  permissions | state | contract | request |
                 component | deployment | migration

Prove namespace — test hypotheses:
  /signal-prove  topic | hypothesis | analysis | prototype | interview |
                 websearch | intelligence | synthesize | program | publish

Listen namespace — gather qualitative signals:
  /signal-listen  support | feedback | adoption

Program namespace — coordinate the work:
  /signal-program  plan

Topic namespace — manage the decision:
  /signal-topic  new | plan | echo | status | story | report
````

---

### Phase 3 — Confirm

Ask:
> "Add this Signal section to CLAUDE.md? This registers Signal with Claude Code
> and activates the inertia rule. (yes / no)"

If `.github/copilot-instructions.md` was found (Phase 1) and has no Signal section:
> "Also update .github/copilot-instructions.md? (yes / no)"

Do not write until confirmed.

If no:
> "No changes made. Signal not configured. Inertia remains unaddressed."

---

### Phase 4 — Write

Write the previewed content exactly — no changes, no additions.

- `CLAUDE.md`: append if it existed before Pre-flight Gate B; create if Gate B was triggered
- `.github/copilot-instructions.md`: append if confirmed in Phase 3

---

### Phase 5 — Report

Output what happened:

- Written: `CLAUDE.md` — [appended | created]
- Written: `.github/copilot-instructions.md` — [appended] (if applicable)
- Skipped: [file] — [reason] (if applicable)

Activation message:
> "Signal is now active. The inertia rule is in effect.
> Begin with `/signal-topic new` to create your first topic and start gathering signals."

---

## Variation Summary

| Variation | Axis | Key Difference | Primary Criteria Targeted |
|-----------|------|----------------|--------------------------|
| V-01 | Lifecycle emphasis | Numbered GATE 1–5 with explicit trigger conditions; edge-case gates 2A/2B exit or modify | C-11, C-12 |
| V-02 | Output format | Tables for detection, path selection, pending actions, and results; preview in labeled code block | C-02, C-09 |
| V-03 | Phrasing register | First-person conversational tone; short imperative sentences; "colleague" framing throughout | C-03, C-08 |
| V-04 | Role sequence + Lifecycle | Three single-responsibility roles (Detector → Planner → Writer); Planner owns both edge cases | C-11, C-12 |
| V-05 | Inertia framing + Edge-case promotion | Inertia rule leads the skill as design principle; edge cases as named pre-flight gates before happy path | C-06, C-12 |
