# Quest Variate — signal-setup — Round 14

Five complete skill body variations. V-01 to V-03 are single-axis; V-04 and V-05 are combined.

---

## V-01 — Baseline Structural

**Variation axis:** Gate structure  
**Hypothesis:** Named gates with prose routing and sub-gate lineage identifiers (GATE 1A/1B) satisfy C-11/C-12/C-25/C-27 at baseline. Consequence language is present but not adversarially framed and not phase-indexed. This is the control variation — it names every gate, routes explicitly, and names consequences, but inertia is a concept rather than a competitor.

---

Configure Signal in this workspace.

Signal is a developer tool for feature decision-making. Teams gather evidence across 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) before committing to a feature. The `/signal-setup` skill appends a Signal section to CLAUDE.md — and optionally `.github/copilot-instructions.md` — so that available skills and the inertia rule are present in Claude's context for every session.

---

## GATE 1 — Detect CLAUDE.md

Check whether CLAUDE.md exists in the workspace root.

- CLAUDE.md not found → proceed to GATE 1A
- CLAUDE.md found → proceed to GATE 1B

### GATE 1A — CLAUDE.md Not Found

CLAUDE.md does not exist. Signal requires a context file to persist in.

Construct the full Signal section content (as specified in GATE 3) and display it as a preview.

Ask: "CLAUDE.md not found. Create it now with the Signal section as its initial content? (yes/no)"

- Confirmed → create CLAUDE.md containing the Signal section content; proceed to GATE 5
- Declined → output: "Signal not configured. Without a CLAUDE.md, Signal skills and the inertia rule have no home in your context — they will not be present when planning the next feature." STOP

### GATE 1B — CLAUDE.md Found

CLAUDE.md exists. Proceed to content detection.

- Proceed to GATE 2

---

## GATE 2 — Detect Existing Signal Section

Read CLAUDE.md. Search for an existing Signal configuration block (look for `## Signal` heading or a "Signal skills" reference).

- Signal section found → proceed to GATE 2A
- Signal section not found → proceed to GATE 3

### GATE 2A — Already Configured

Output: "Signal is already configured in CLAUDE.md. CLAUDE.md loads automatically in every session, so Signal skills and the inertia rule are already present in Claude's context without manual invocation. No changes needed."

Proceed to GATE 6 to offer the optional Copilot instructions update.

---

## GATE 3 — Preview Signal Section

Construct the Signal section content. It must include:

1. `## Signal` heading
2. One-sentence purpose: Signal gathers evidence signals before feature commitment
3. Namespace list: scout, draft, review, flow, trace, prove, listen, program, topic
4. Inertia rule: "Inertia rule: doing nothing is always the default. Use `/topic:status` to learn when enough signals exist to name inertia as the loser."
5. Skill invocation pattern: `/signal:{namespace}:{skill}`

Display the full content as a fenced code block.

Output: "This is what will be appended to CLAUDE.md. Review it, then confirm at the next step."

---

## GATE 4 — Confirm Append

Ask: "Append this Signal section to CLAUDE.md? (yes/no)"

- Confirmed → proceed to GATE 5
- Declined → output: "No changes made. Signal not configured. Signal skills and the inertia rule will not be present in Claude's context for future sessions in this workspace." STOP (do not proceed to GATE 6)

---

## GATE 5 — Write Signal Section

Append the Signal section — exactly as previewed in GATE 3 — to CLAUDE.md.

Output: "Signal section appended to CLAUDE.md. Signal skills are now advertised in your context, and the inertia rule will be present for every session that opens this workspace."

Proceed to GATE 6.

---

## GATE 6 — Offer Copilot Instructions Update

Ask: "Would you also like to add Signal context to `.github/copilot-instructions.md`? (yes/no)"

Check whether `.github/copilot-instructions.md` exists and whether it already contains a Signal section.

- Already contains Signal section → output: "Copilot instructions already include Signal context. No changes needed." STOP
- Confirmed and file exists → append a brief Signal reference to the file; output: "Copilot instructions updated with Signal context." STOP
- Confirmed and file absent → create `.github/copilot-instructions.md` with Signal content; output: "Copilot instructions created with Signal context." STOP
- Declined → output: "Copilot instructions not updated. Signal context will not be present in GitHub Copilot interactions." STOP

---

---

## V-02 — Adversarial Inertia Framing

**Variation axis:** Inertia framing  
**Hypothesis:** Naming inertia as the active victor at every decline gate (C-33: "Inertia wins the default choice"), chaining the causal two-step at the primary decline (C-34: "spec committed without named competitor → question never asked"), and threading that consequence through all Signal-absent exit gates (C-19) are the three patterns that produce FAIL→PASS on C-16/C-18/C-33/C-34. Phase labels appear but are vocabulary-embedded rather than explicitly labeled — testing whether vocabulary alone satisfies C-22 or whether explicit labels are required.

---

Configure Signal in this workspace.

## Why This Setup Matters

Signal has one adversary: **inertia** — not a rule, not a principle, but a competitor that is already in the room before any feature discussion begins. Inertia does not need to make an argument. It wins the default choice every time the question "why would teams do nothing?" goes unasked.

This setup names that competitor. A Signal section in CLAUDE.md means the inertia question is present in Claude's context for every planning session that follows — not because you remember to invoke it, but because CLAUDE.md loads automatically. You configure once; inertia has a named opponent from that point forward.

---

## GATE 1 — Detect CLAUDE.md

Check whether CLAUDE.md exists in the workspace root.

- CLAUDE.md not found → proceed to GATE 1A
- CLAUDE.md found → proceed to GATE 2

### GATE 1A — CLAUDE.md Not Found

CLAUDE.md does not exist. Signal has no context file to persist in.

Construct and display the full Signal section as a preview.

Ask: "CLAUDE.md not found. Create it now with Signal configured? (yes/no)"

- Confirmed → create CLAUDE.md with Signal section content; proceed to GATE 5
- Declined → output: "Signal not configured. Inertia wins the default choice. Before the next feature spec is committed, the question 'why would teams do nothing?' will not be in your context — the spec gets committed without a named competitor, and the question never gets asked." STOP

---

## GATE 2 — Detect Existing Signal Section

Read CLAUDE.md. Search for an existing Signal configuration block.

- Signal section found → proceed to GATE 2A
- Signal section absent → proceed to GATE 3

### GATE 2A — Already Configured

"Signal is already configured here. CLAUDE.md loads automatically every session — inertia already has a named opponent in Claude's context, present before any spec is committed, without you having to remember to raise the question. The work this configuration does: it ensures 'why would teams do nothing?' is always in the room at the planning stage."

Proceed to GATE 6.

---

## GATE 3 — Preview Signal Section

Construct the Signal section. Include:

1. `## Signal` heading
2. Purpose: gathering evidence signals across 9 namespaces before committing to a feature
3. Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic
4. Inertia rule: "Inertia rule: the status-quo is always the default winner. Use `/topic:status` when you have enough signals to name it as the loser."
5. Skill pattern: `/signal:{namespace}:{skill}`

Display the complete content as a fenced code block.

Output: "This is the text that names inertia as a competitor in your context — what will be appended to CLAUDE.md. Review it."

---

## GATE 4 — Confirm Append

Ask: "Append this Signal section to CLAUDE.md? (yes/no)"

- Confirmed → proceed to GATE 5
- Declined → output: "Signal not configured. Inertia wins the default choice. Before the next spec is committed — at the planning stage where the feature story is first assembled — there will be no reminder in your context to ask why teams would do nothing. The spec is committed without a named competitor, and the question never gets asked." STOP (do not proceed to GATE 6)

---

## GATE 5 — Write Signal Section

Append the previewed Signal section to CLAUDE.md.

Output: "Signal configured. Inertia now has a named opponent in this workspace. Every session that opens here will carry the inertia question in Claude's context — present before any spec is committed, without manual invocation."

Proceed to GATE 6.

---

## GATE 6 — Offer Copilot Instructions

Ask: "Add Signal context to `.github/copilot-instructions.md` as well? (yes/no)"

Check for existing Signal content in `.github/copilot-instructions.md`.

- Already configured → output: "Copilot instructions already include Signal context. Inertia is already named in that context too — present when Copilot is suggesting implementation paths, not just when a spec is being written." STOP
- Confirmed and file exists → append Signal reference; output: "Copilot instructions updated. Inertia now has a named opponent at both the planning stage (CLAUDE.md) and the implementation stage (Copilot context)." STOP
- Confirmed and file absent → create file with Signal content; output: "Copilot instructions created. Inertia is named at both the planning and implementation stages." STOP
- Declined → output: "Copilot instructions not updated. When Copilot is suggesting implementation paths, Signal context will not be present — inertia wins the default choice at the implementation stage. The planning stage (CLAUDE.md) carries the question; the implementation stage does not." STOP

---

---

## V-03 — Route: Prefix Routing Format

**Variation axis:** Output format / routing structure  
**Hypothesis:** A `Route:` block closing each gate — one `(condition → GATE ID)` pair per line — satisfies C-29 at higher precision than prose routing and satisfies C-35 (machine-parseable by line-scan without reading prose). This also separates routing from consequence language, letting each serve its function cleanly without competing for the same sentence.

---

Configure Signal in this workspace.

Signal is a developer tool for feature decision-making. Before committing to a feature, teams gather evidence across 9 namespaces. This skill appends a Signal section to CLAUDE.md — and optionally `.github/copilot-instructions.md` — so that available skills and the inertia rule are present in Claude's context for every session.

Inertia is Signal's silent adversary: the status-quo that wins every decision where no competitor is named. This setup gives inertia a name. CLAUDE.md loads automatically every session — configure once, and the inertia question is always present.

---

## GATE 1 — Detect CLAUDE.md

Check whether CLAUDE.md exists in the workspace root.

```
Route:
- CLAUDE.md not found  → GATE 1A
- CLAUDE.md found      → GATE 2
```

### GATE 1A — CLAUDE.md Not Found

CLAUDE.md does not exist. Signal cannot persist without a context file.

Construct and display the full Signal section preview. Offer to create CLAUDE.md with the Signal section as its initial content.

Ask: "CLAUDE.md not found. Create it with Signal configured? (yes/no)"

On decline: "Signal not configured. Inertia wins the default choice. Before the next feature spec is committed, there will be no reminder in your context to ask why teams would do nothing — the question never gets asked."

```
Route:
- Confirmed  → create CLAUDE.md with Signal content, then GATE 5
- Declined   → output decline consequence, then STOP
```

---

## GATE 2 — Detect Existing Signal Section

Read CLAUDE.md. Search for an existing Signal configuration block (`## Signal` or Signal skills reference).

```
Route:
- Signal section found   → GATE 2A
- Signal section absent  → GATE 3
```

### GATE 2A — Already Configured

Output: "Signal is already configured here. CLAUDE.md loads automatically every session — inertia is already named in Claude's context at the planning stage, present before any spec is committed, without manual invocation. The work this configuration does: it ensures the question is always in the room."

```
Route:
- (automatic) → GATE 6
```

---

## GATE 3 — Preview Signal Section

Construct the Signal section. Include:

1. `## Signal` heading
2. Purpose: evidence gathering across 9 namespaces before feature commitment
3. Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic
4. Inertia rule: "Inertia rule: doing nothing is always the default. `/topic:status` tells you when signals are sufficient to name it as the loser."
5. Skill pattern: `/signal:{namespace}:{skill}`

Display the full content as a fenced code block.

Output: "This is what will be appended to CLAUDE.md. Review it, then proceed to confirm."

```
Route:
- (after user review) → GATE 4
```

---

## GATE 4 — Confirm Append

Ask: "Append this Signal section to CLAUDE.md? (yes/no)"

On decline: "No changes made. Signal not configured. Before the next spec is committed — at the planning stage where features are first assembled — there will be no Signal context in your CLAUDE.md. The spec is committed without a named competitor, and the inertia question never gets asked."

```
Route:
- Confirmed  → GATE 5
- Declined   → output decline consequence, then STOP
```

---

## GATE 5 — Write Signal Section

Append the Signal section (exactly as previewed in GATE 3) to CLAUDE.md.

Output: "Signal configured. Available skills are now advertised in your context. The inertia rule will be present for every session that opens this workspace."

```
Route:
- (automatic) → GATE 6
```

---

## GATE 6 — Offer Copilot Instructions

Ask: "Add Signal context to `.github/copilot-instructions.md`? (yes/no)"

Check for existing Signal content in `.github/copilot-instructions.md`.
(No sub-gate promoted here — this is a detection-only skip path inside an optional-extension gate, not a primary configuration confirmation point. Inline per C-28 scope.)

On already-configured: "Copilot instructions already include Signal context. When Copilot is suggesting implementation paths, inertia is already named in that context too."

On decline: "Copilot instructions not updated. When Copilot is suggesting implementation paths, Signal context will not be present — the inertia question will not be raised at the implementation stage."

On confirmed write: "Copilot instructions updated. Signal context is now present at both the planning stage (CLAUDE.md) and the implementation stage (Copilot context)."

```
Route:
- Already configured          → output already-configured affirmation, then STOP
- Confirmed, file exists       → append Signal reference to file, then STOP
- Confirmed, file absent       → create file with Signal content, then STOP
- Declined                     → output decline consequence, then STOP
```

---

---

## V-04 — Phase-Indexed Consequence Anchors

**Variation axis:** Lifecycle emphasis  
**Hypothesis:** C-22 and C-23 require explicit phase category labels at every decline anchor — not vocabulary-embedded phase references ("before the spec is committed") but named phase categories ("at the planning stage"). This variation tests whether explicit `[planning stage]` or `[implementation stage]` labels as structured annotations at every decline gate constitute the passing pattern. Sub-gate identifiers encode parent lineage throughout. Each gate carries its development phase as an explicit header annotation.

---

Configure Signal in this workspace.

## Preamble

Signal's purpose is evidence-gathering before commitment. Its adversary is inertia — not a passive absence, but the default winner in every decision where no competitor is named and no evidence is demanded. Configuring Signal gives that adversary a name.

The reason this setup must persist is mechanical: CLAUDE.md loads automatically in every session. You configure once, and the inertia question is present in Claude's context at every planning session that follows — not because you remember to raise it, but because the file is always there. That persistence is what makes the write worth doing.

---

## GATE 1 — Detect CLAUDE.md
*Phase: pre-configuration — workspace detection*

Check whether CLAUDE.md exists in the workspace root.

- CLAUDE.md not found → proceed to GATE 1A
- CLAUDE.md found → proceed to GATE 1B

### GATE 1A — CLAUDE.md Not Found
*Phase: pre-configuration — workspace detection — missing-file branch*

CLAUDE.md does not exist.

Construct and display the full Signal section as a preview. Offer to create CLAUDE.md.

Ask: "CLAUDE.md not found. Create it now with Signal configured? (yes/no)"

- Confirmed → create CLAUDE.md with Signal section; proceed to GATE 5
- Declined → "Signal not configured. Inertia wins the default choice. **At the planning stage** — the point where a feature is named and a spec begins to take shape — there will be no Signal context in your CLAUDE.md. The spec is committed without a named competitor, and the question never gets asked." STOP

### GATE 1B — CLAUDE.md Found
*Phase: pre-configuration — workspace detection — file-found branch*

CLAUDE.md exists. Proceed to content detection.

- Proceed to GATE 2

---

## GATE 2 — Detect Existing Signal Section
*Phase: pre-configuration — content detection*

Read CLAUDE.md. Search for an existing Signal configuration block.

- Signal section found → proceed to GATE 2A
- Signal section absent → proceed to GATE 3

### GATE 2A — Already Configured
*Phase: pre-configuration — content detection — already-present branch*

Output: "Signal is already configured here. The mechanism: CLAUDE.md loads automatically every session, so the inertia question is already present **at the planning stage** in Claude's context without manual invocation. Inertia already has a named opponent in this workspace."

Proceed to GATE 6.

---

## GATE 3 — Preview Signal Section
*Phase: configuration preview*

Construct the Signal section. Include:

1. `## Signal` heading
2. Purpose: evidence signals across 9 namespaces before feature commitment
3. Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic
4. Inertia rule: "Inertia rule: the status-quo wins every default. `/topic:status` tells you when signals are sufficient to name it as the loser."
5. Skill pattern: `/signal:{namespace}:{skill}`

Display the full content as a fenced code block.

Output: "This is the Signal section that will be appended — the text that names inertia as a competitor in your planning context. Review it."

---

## GATE 4 — Confirm Append
*Phase: configuration confirmation*

Ask: "Append this Signal section to CLAUDE.md? (yes/no)"

- Confirmed → proceed to GATE 5
- Declined → "No changes made. Signal not configured. **At the planning stage** — when the feature spec is being assembled and the team is deciding whether to commit — there will be no reminder in CLAUDE.md to ask 'why would teams do nothing?' The spec is committed without a named competitor, and the question never gets asked." STOP (do not proceed to GATE 6)

---

## GATE 5 — Write Signal Section
*Phase: configuration write*

Append the previewed Signal section to CLAUDE.md.

Output: "Signal configured. **At the planning stage**, inertia now has a named opponent in your context. Every session that opens this workspace will carry the question automatically."

Proceed to GATE 6.

---

## GATE 6 — Offer Copilot Instructions
*Phase: optional extension — implementation stage*

Ask: "Add Signal context to `.github/copilot-instructions.md`? (yes/no)"

Check `.github/copilot-instructions.md` for existing Signal content.
(No sub-gate promoted here — Copilot instructions detection is an optional-extension skip path, not a primary configuration confirmation point. Inline treatment is intentional per C-28: primary detection always promotes to GATE 2A; secondary optional-extension detection does not require promotion when no new confirmation is needed.)

- Already configured → output: "Copilot instructions already include Signal context. **At the implementation stage** — when Copilot is suggesting code paths and completing functions — inertia is already named in that context. The question is present at both stages." STOP
- Confirmed and file exists → append Signal reference; output: "Copilot instructions updated. Signal is now present **at both the planning stage** (CLAUDE.md) and **the implementation stage** (Copilot context)." STOP
- Confirmed and file absent → create file; output: "Copilot instructions created. Signal context is now present at both stages." STOP
- Declined → output: "Copilot instructions not updated. **At the implementation stage** — when Copilot is actively suggesting code paths — Signal context will not be present. The inertia question will not be raised there, only at the planning stage where CLAUDE.md already carries it." STOP

---

---

## V-05 — Combined: Adversarial Framing + Route: Format + Phase-Indexed Consequences

**Variation axis:** Combined — adversarial inertia framing (V-02/C-33/C-34) + `Route:` prefix with one-branch-per-line routing (V-03/C-35) + phase-indexed consequence anchors with explicit labels (V-04/C-22/C-23)  
**Hypothesis:** The three axes are orthogonal. Adversarial framing improves C-16/C-18/C-33/C-34 without affecting routing or phase labels. `Route:` blocks improve C-29/C-35 without affecting inertia language. Explicit phase labels improve C-22/C-23 without affecting the routing format or adversarial register. Combined, they should score the highest on all three criterion clusters simultaneously — with the added structural benefit that separating `Route:` from prose frees the consequence language to be fully adversarial without being diluted by routing mechanics.

---

Configure Signal in this workspace.

## Why This Configuration Matters

Signal has one adversary: **inertia** — not a concept, not a rule, but a named competitor that is already in the room before any feature discussion begins. Inertia does not make arguments. It wins the default choice every time the planning stage passes without the question being asked.

This setup names that competitor. A Signal section in CLAUDE.md means the inertia question is present in Claude's context at every planning session — not because you remember to invoke it, but because CLAUDE.md loads automatically. You configure once; inertia has a named opponent from that session forward.

That persistence is why the write matters: without it, the question has to be manually invoked, and manual memory loses to inertia at the planning stage, every time.

---

## GATE 1 — Detect CLAUDE.md
*Phase: pre-configuration — workspace detection*

Check whether CLAUDE.md exists in the workspace root.

```
Route:
- CLAUDE.md not found  → GATE 1A
- CLAUDE.md found      → GATE 1B
```

### GATE 1A — CLAUDE.md Not Found
*Phase: pre-configuration — workspace detection — missing-file branch*

CLAUDE.md does not exist. Inertia cannot be named in a context file that isn't there.

Construct and display the full Signal section as a preview. Offer to create CLAUDE.md.

Ask: "CLAUDE.md not found. Create it now with Signal configured? (yes/no)"

On decline: "Signal not configured. Inertia wins the default choice. **At the planning stage** — before the next feature spec is committed — there will be no reminder in your context to ask why teams would do nothing. The spec is committed without a named competitor, and the question never gets asked."

```
Route:
- Confirmed  → create CLAUDE.md with Signal section, then GATE 5
- Declined   → output decline consequence, then STOP
```

### GATE 1B — CLAUDE.md Found
*Phase: pre-configuration — workspace detection — file-found branch*

CLAUDE.md exists. Proceed to Signal content detection.

```
Route:
- (automatic) → GATE 2
```

---

## GATE 2 — Detect Existing Signal Section
*Phase: pre-configuration — content detection*

Read CLAUDE.md. Search for an existing Signal configuration block (`## Signal` or Signal skills reference).

```
Route:
- Signal section found   → GATE 2A
- Signal section absent  → GATE 3
```

### GATE 2A — Already Configured
*Phase: pre-configuration — content detection — already-present branch*

Output: "Signal is already configured here. The mechanism: CLAUDE.md loads automatically every session — inertia already has a named opponent in Claude's context, present **at the planning stage** before any spec is committed, without manual invocation. The work this configuration does: it ensures 'why would teams do nothing?' is always in the room."

```
Route:
- (automatic) → GATE 6
```

---

## GATE 3 — Preview Signal Section
*Phase: configuration preview*

Construct the Signal section. Include:

1. `## Signal` heading
2. Purpose: gathering evidence signals across 9 namespaces before committing to a feature
3. Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic
4. Inertia rule: "Inertia rule: the status-quo is always the default winner. Use `/topic:status` when you have enough signals to name it as the loser."
5. Skill pattern: `/signal:{namespace}:{skill}`

Display the full content as a fenced code block.

Output: "This is the text that names inertia as a competitor in your planning context — what will be appended to CLAUDE.md. Review it."

```
Route:
- (after user review) → GATE 4
```

---

## GATE 4 — Confirm Append
*Phase: configuration confirmation*

Ask: "Append this Signal section to CLAUDE.md? (yes/no)"

On decline: "Signal not configured. Inertia wins the default choice. **At the planning stage** — when the feature story is being assembled and a spec is about to be committed — there will be no Signal context in your CLAUDE.md. The spec is committed without a named competitor, and the question never gets asked."

```
Route:
- Confirmed  → GATE 5
- Declined   → output decline consequence, then STOP
```

---

## GATE 5 — Write Signal Section
*Phase: configuration write*

Append the Signal section (exactly as previewed in GATE 3) to CLAUDE.md.

Output: "Signal configured. Inertia now has a named opponent in this workspace. **At the planning stage**, every session that opens here will carry the inertia question in Claude's context — present before any spec is committed, without manual invocation."

```
Route:
- (automatic) → GATE 6
```

---

## GATE 6 — Offer Copilot Instructions
*Phase: optional extension — implementation stage*

Ask: "Add Signal context to `.github/copilot-instructions.md` as well? (yes/no)"

Check `.github/copilot-instructions.md` for existing Signal content.
(No sub-gate promoted here — this is a detection-only skip path inside an optional-extension gate, not a primary Signal configuration confirmation point. Intentionally inline per C-28: primary detection paths always promote to dedicated sub-gates; secondary optional-extension detection does not require promotion when no new user confirmation is needed.)

On already configured: "Copilot instructions already include Signal context. **At the implementation stage** — when Copilot is actively suggesting code paths — inertia is already named in that context. The question is present at both stages."

On decline: "Copilot instructions not updated. **At the implementation stage** — when Copilot is suggesting code paths and completing implementation — Signal context will not be present. Inertia wins the default choice there. The planning stage (CLAUDE.md) carries the question; the implementation stage does not."

On confirmed write: "Copilot instructions updated. Inertia now has a named opponent **at both the planning stage** (CLAUDE.md) and **the implementation stage** (Copilot context)."

```
Route:
- Already configured          → output already-configured affirmation, then STOP
- Confirmed, file exists       → append Signal reference to file, then STOP
- Confirmed, file absent       → create file with Signal content, then STOP
- Declined                     → output decline consequence, then STOP
```

---

## Variation Summary

| Variation | Primary Axis | Key Hypotheses | New Criteria Targeted |
|-----------|-------------|----------------|----------------------|
| V-01 | Gate structure | Named gates + sub-gate lineage satisfy C-11/C-12/C-25/C-27 at baseline | C-11, C-12, C-25, C-27 |
| V-02 | Inertia framing | Adversary-as-victor framing + two-step causal chain satisfy C-33/C-34; consequence threading satisfies C-19 | C-33, C-34, C-16, C-18, C-19 |
| V-03 | Route: format | `Route:` + one-branch-per-line satisfies C-35; separating routing from prose satisfies C-29 more cleanly | C-35, C-29 |
| V-04 | Lifecycle emphasis | Explicit phase labels at every decline anchor satisfy C-22/C-23; inline annotation for optional-extension detection satisfies C-30 | C-22, C-23, C-30 |
| V-05 | Combined (V-02 + V-03 + V-04) | Axes are orthogonal; combining should satisfy all three criterion clusters simultaneously | C-33, C-34, C-35, C-22, C-23, C-29, C-30 |
