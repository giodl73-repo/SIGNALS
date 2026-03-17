## Quest Variate — signal-setup — Round 15

**Rubric version**: v13 (29 criteria, A=29)
**New patterns targeted**: C-33 (adversary as victor), C-34 (two-step causal chain), C-35 (Route: prefix + one-branch-per-line)

---

## V-01 — Single axis: Lifecycle emphasis (heading-enforced gate boundaries, C-27)

**Hypothesis**: Making every gate and sub-gate a document heading lets a reader enumerate the full lifecycle by outline scan alone, without reading prose — satisfying C-27's structural prohibition on bold-label pseudo-gates and making C-12's edge-case promotion verifiable by structure.

---

You are running **signal-setup**. Configure Signal in this workspace after installation.

Teams commit build directions without asking whether the status quo is acceptable. Signal skills exist to make that question automatic. Setup writes the reminder into Claude's context once — so it survives every session without anyone having to remember.

---

### GATE 1 — Detect CLAUDE.md

Read the file `CLAUDE.md` in the current workspace root. Record whether the file exists.

#### GATE 1A — CLAUDE.md Not Found

If CLAUDE.md does not exist:

Display: "No CLAUDE.md found in this workspace. Signal setup appends to CLAUDE.md. I can create a minimal one now containing only the Signal section, or you can create it manually and re-run."

Ask: "Create CLAUDE.md with the Signal section? (yes / no)"

If yes → create CLAUDE.md with the Signal section content (see GATE 3 for exact content) → skip to GATE 5.

If no → display: "Signal not configured. At the planning stage, there is no reminder in your context to ask whether the status quo is acceptable before the spec is committed." → exit.

#### GATE 1B — CLAUDE.md Found

CLAUDE.md exists. Proceed to GATE 2.

---

### GATE 2 — Detect Existing Signal Section

Read CLAUDE.md. Search for a heading matching `## Signal` or `# Signal`.

#### GATE 2A — Already Configured

A Signal section already exists.

Display: "Signal is already configured. Your CLAUDE.md loads automatically every session — the inertia question is present in Claude's context without you having to remember it. The configuration is doing the work of a persistent reminder."

Exit.

#### GATE 2B — Not Yet Configured

No Signal section found. Proceed to GATE 3.

---

### GATE 3 — Preview

Display the following preview block to the user:

```
── Preview: Signal section to be appended to CLAUDE.md ──────────────────────

## Signal

Signal skills gather evidence before you commit to a build direction. Know
what you know before you build.

Available namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic.

**Inertia rule**: When signals are absent, inertia wins. A topic is ready
when signals exist to name what happens if nothing changes — and why that
outcome is unacceptable. Use /topic:status to check readiness.

─────────────────────────────────────────────────────────────────────────────
```

Proceed to GATE 4.

---

### GATE 4 — Confirmation

Ask: "Append this Signal section to CLAUDE.md? (yes / no)"

#### GATE 4A — User Confirms

Proceed to GATE 5.

#### GATE 4B — User Declines

Display: "Signal not configured. At the planning stage, there is no reminder in your context to ask whether inertia has been named before the spec is committed."

Exit.

---

### GATE 5 — Write and Report

Append the Signal section exactly as shown in GATE 3 to CLAUDE.md.

Display: "Signal section appended to CLAUDE.md. The inertia question will be present in Claude's context automatically every session."

Proceed to GATE 6.

---

### GATE 6 — Copilot Instructions (Optional Extension)

Ask: "Also add a Signal section to .github/copilot-instructions.md? (yes / no)"

#### GATE 6A — User Confirms

Check whether `.github/copilot-instructions.md` exists.

If the file does not exist: create the `.github/` directory if needed and create `copilot-instructions.md`. *(No sub-gate needed — no confirmation point; file creation is part of the confirmed action.)*

Append or write the Signal section to `.github/copilot-instructions.md` using the same content as GATE 3.

Display: "Signal section added to .github/copilot-instructions.md. When Copilot is suggesting implementation code, the inertia question is now present in that context."

#### GATE 6B — User Declines

Display: "Copilot instructions not updated. While Copilot is suggesting implementation code, there is no reminder in that context to surface the inertia question before the build direction is locked in."

---

*signal-setup complete.*

---

## V-02 — Single axis: Inertia as named victor + causal chain (C-33, C-34)

**Hypothesis**: Framing inertia as the entity that *wins* (not merely the principle that governs defaults) and naming the two-step causal chain — spec committed without a named competitor → question never gets asked — makes every decline path land with specific, felt consequence rather than abstract policy.

---

You are running **signal-setup**. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder to ask whether the status quo is acceptable. The spec gets committed without a named competitor — and the question never gets asked. Setup writes the reminder once, permanently, so inertia has a named opponent in every session.

---

**GATE 1 — Detect CLAUDE.md**

Read `CLAUDE.md` in the workspace root.

**If not found (GATE 1A):**
Display: "No CLAUDE.md found. Inertia wins the default choice here — without a file to append to, the reminder cannot persist. I can create a minimal CLAUDE.md containing only the Signal section."

Ask: "Create CLAUDE.md now? (yes / no)"

- Yes → create CLAUDE.md with Signal section (see GATE 3 content) → jump to GATE 5.
- No → display: "Signal not configured. At the planning stage, inertia wins — the spec gets committed without a named competitor, and the question never gets asked." → exit.

**If found (GATE 1B):** Proceed to GATE 2.

---

**GATE 2 — Detect Existing Signal Section**

Search CLAUDE.md for `## Signal` or `# Signal`.

**If found (GATE 2A):**
Display: "Signal is already configured. Inertia already has a named opponent here — your CLAUDE.md loads every session and carries the reminder automatically. You do not need to think about it; the configuration thinks for you."

Exit.

**If not found (GATE 2B):** Proceed to GATE 3.

---

**GATE 3 — Preview**

Display:

```
── Preview ──────────────────────────────────────────────────────────────────

## Signal

Signal skills gather evidence before you commit to a build direction. Know
what you know before you build.

Available namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic.

**Inertia rule**: When signals are absent, inertia wins the default choice.
A topic is ready when signals exist to name what happens if nothing changes —
and to name why that outcome is unacceptable. Use /topic:status to check
readiness.

─────────────────────────────────────────────────────────────────────────────
```

Proceed to GATE 4.

---

**GATE 4 — Confirmation**

Ask: "Append this Signal section to CLAUDE.md? (yes / no)"

- Yes → proceed to GATE 5.
- No → display: "Signal not configured. Inertia wins the default choice — at the planning stage, the spec gets committed without a named competitor, and the question never gets asked." → exit.

---

**GATE 5 — Write and Report**

Append the Signal section (exact content from GATE 3 preview) to CLAUDE.md.

Display: "Signal section appended to CLAUDE.md. Inertia now has a named opponent in Claude's context every session — the reminder loads automatically."

Proceed to GATE 6.

---

**GATE 6 — Copilot Instructions (Optional)**

Ask: "Also add a Signal section to .github/copilot-instructions.md? (yes / no)"

- Yes:
  - Check if `.github/copilot-instructions.md` exists. If not, create it (no additional confirmation needed — the user already said yes).
  - Append or write the Signal section.
  - Display: "Signal section added to .github/copilot-instructions.md. While Copilot is suggesting code, inertia now has a named opponent in that context too."
- No:
  - Display: "Copilot instructions not updated. While Copilot is suggesting implementation code, inertia wins that context — suggestions arrive without a reminder to ask whether the build direction was chosen against a named alternative."

---

*signal-setup complete.*

---

## V-03 — Single axis: Route: prefix + one-branch-per-line routing (C-35)

**Hypothesis**: Prefixing every routing block with `Route:` and writing each branch as a single `- condition → destination` line makes the gate graph parseable by line-scan without reading prose — the architectural improvement demonstrated in V-03 of the preceding round.

---

You are running **signal-setup**. Configure Signal in this workspace after installation.

Signal skills make the inertia question automatic. Without configuration, Claude has no reminder that teams sometimes choose nothing — not because nothing is the right answer, but because the question was never asked. Setup writes that reminder into CLAUDE.md once, so it persists.

---

**GATE 1 — Detect CLAUDE.md**

Read `CLAUDE.md` in the workspace root.

Route:
- CLAUDE.md not found → GATE 1A
- CLAUDE.md found → GATE 2

**GATE 1A — Create CLAUDE.md?**

Display: "No CLAUDE.md found. Signal setup appends to CLAUDE.md. I can create a minimal one now containing only the Signal section."

Ask: "Create CLAUDE.md with the Signal section? (yes / no)"

Route:
- yes → create CLAUDE.md with Signal section (GATE 3 content) → GATE 5
- no → display: "Signal not configured. At the planning stage, there is no reminder in your context to surface the inertia question before the spec is committed." → exit

---

**GATE 2 — Detect Existing Signal Section**

Read CLAUDE.md. Search for `## Signal` or `# Signal`.

Route:
- Signal section found → GATE 2A
- Signal section absent → GATE 3

**GATE 2A — Already Configured**

Display: "Signal is already configured. Your CLAUDE.md loads automatically every session — the inertia question is already present in Claude's context, and you do not need to remember to ask it."

Exit.

---

**GATE 3 — Preview**

Display:

```
── Preview: Signal section to be appended ───────────────────────────────────

## Signal

Signal skills gather evidence before you commit to a build direction. Know
what you know before you build.

Available namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic.

**Inertia rule**: When signals are absent, inertia wins. A topic is ready
when signals exist to name what happens if nothing changes — and to name why
that outcome is unacceptable. Use /topic:status to check readiness.

─────────────────────────────────────────────────────────────────────────────
```

Proceed to GATE 4.

---

**GATE 4 — Confirmation**

Ask: "Append this Signal section to CLAUDE.md? (yes / no)"

Route:
- yes → GATE 5
- no → display: "Signal not configured. At the planning stage, there is no reminder in your context to ask whether inertia has been named before the spec is committed." → exit

---

**GATE 5 — Write and Report**

Append the Signal section (exact content from GATE 3) to CLAUDE.md.

Display: "Signal section appended to CLAUDE.md. The inertia question is now present in Claude's context every session — it loads automatically with the file."

Proceed to GATE 6.

---

**GATE 6 — Copilot Instructions (Optional)**

Check whether `.github/copilot-instructions.md` exists. Ask: "Also add a Signal section to .github/copilot-instructions.md? (yes / no)"

Route:
- yes, file exists → append Signal section → GATE 6A
- yes, file not found → create .github/ if needed, create file, write Signal section → GATE 6A *(no sub-gate needed — creation is part of the confirmed append action)*
- no → GATE 6B

**GATE 6A — Copilot Updated**

Display: "Signal section added to .github/copilot-instructions.md. Copilot will see the inertia question while suggesting code."

**GATE 6B — Copilot Skipped**

Display: "Copilot instructions not updated. While Copilot is suggesting implementation code, there is no reminder in that context to surface the inertia question."

---

*signal-setup complete.*

---

## V-04 — Combined: V-01 (heading-enforced gates) + V-02 (inertia as named victor + causal chain)

**Hypothesis**: Heading-level gate structure (C-27) gives the document navigability; adversary framing (C-33) and the two-step causal chain (C-34) give every exit its full consequence weight. Combined, the spec is both structurally verifiable and rhetorically complete — no exit is consequence-free and no gate boundary is typographic.

---

You are running **signal-setup**. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** Without Signal configured, Claude has no reminder to name it. The spec gets committed without a named competitor — and the question never gets asked. Setup writes that opponent into CLAUDE.md once, so it persists through every session that follows.

---

### GATE 1 — Detect CLAUDE.md

Read `CLAUDE.md` in the workspace root. Record whether the file exists.

#### GATE 1A — CLAUDE.md Not Found

Display: "No CLAUDE.md found. Inertia wins by default here — without a file to carry the reminder, there is no persistent opponent for it to face. I can create a minimal CLAUDE.md now containing only the Signal section."

Ask: "Create CLAUDE.md with the Signal section? (yes / no)"

If yes → create CLAUDE.md with Signal section content (see GATE 3) → skip to GATE 5.

If no → display: "Signal not configured. At the planning stage, inertia wins — the spec gets committed without a named competitor, and the question never gets asked." → exit.

#### GATE 1B — CLAUDE.md Found

Proceed to GATE 2.

---

### GATE 2 — Detect Existing Signal Section

Read CLAUDE.md. Search for `## Signal` or `# Signal`.

#### GATE 2A — Already Configured

Display: "Signal is already configured. Inertia already has a named opponent here. Your CLAUDE.md loads automatically every session — the reminder persists without you having to remember it. The mechanism is the file load itself: no manual invocation required."

Exit.

#### GATE 2B — Not Yet Configured

Proceed to GATE 3.

---

### GATE 3 — Preview

Display:

```
── Preview: Signal section to be appended to CLAUDE.md ──────────────────────

## Signal

Signal skills gather evidence before you commit to a build direction. Know
what you know before you build.

Available namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic.

**Inertia rule**: When signals are absent, inertia wins the default choice.
A topic is ready when signals exist to name what happens if nothing changes —
and to name why that outcome is unacceptable. Use /topic:status to check
readiness.

─────────────────────────────────────────────────────────────────────────────
```

Proceed to GATE 4.

---

### GATE 4 — Confirmation

Ask: "Append this Signal section to CLAUDE.md? (yes / no)"

#### GATE 4A — User Confirms

Proceed to GATE 5.

#### GATE 4B — User Declines

Display: "Signal not configured. Inertia wins the default choice — at the planning stage, the spec gets committed without a named competitor, and the question never gets asked."

Exit.

---

### GATE 5 — Write and Report

Append the Signal section (exact content from GATE 3) to CLAUDE.md.

Display: "Signal section appended to CLAUDE.md. Inertia now has a named opponent in Claude's context — it loads automatically with the file every session."

Proceed to GATE 6.

---

### GATE 6 — Copilot Instructions (Optional Extension)

Ask: "Also add a Signal section to .github/copilot-instructions.md? (yes / no)"

#### GATE 6A — User Confirms

Check whether `.github/copilot-instructions.md` exists. If not, create the `.github/` directory if needed and create the file. *(No sub-gate needed — no additional confirmation point; creation is part of the already-confirmed append action.)*

Append the Signal section to `.github/copilot-instructions.md`.

Display: "Signal section added to .github/copilot-instructions.md. While Copilot is suggesting implementation code, inertia now has a named opponent in that context — the reminder is present at the implementation stage, not only at planning."

#### GATE 6B — User Declines

Display: "Copilot instructions not updated. While Copilot is suggesting implementation code, inertia wins that context — code suggestions arrive without a reminder to ask whether the build direction was chosen against a named alternative."

---

*signal-setup complete.*

---

## V-05 — Combined: V-02 (adversary framing) + V-03 (Route: format) + phase-indexed consequence anchors (C-22, C-23)

**Hypothesis**: Combining the adversary framing (C-33, C-34) with parseable routing (C-35) and explicit phase labels on every decline anchor (C-22, C-23) produces a spec where the gate graph is line-scannable, inertia is named as victor throughout, and no two decline paths share consequence vocabulary — each uses the phase-native terms of the context it protects.

---

You are running **signal-setup**. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** Teams do not choose nothing because nothing is right — they choose it because the question was never asked. Signal skills exist to ask it. Configuration writes the reminder into CLAUDE.md once so that, at the planning stage, inertia has a named opponent in Claude's context every session. Setup is a one-time act; the reminder it installs is permanent.

---

**GATE 1 — Detect CLAUDE.md**

Read `CLAUDE.md` in the workspace root.

Route:
- CLAUDE.md not found → GATE 1A
- CLAUDE.md found → GATE 2

**GATE 1A — CLAUDE.md Not Found**

Display: "No CLAUDE.md found. Signal setup appends to CLAUDE.md to make the reminder persistent. I can create a minimal one now."

Ask: "Create CLAUDE.md with the Signal section? (yes / no)"

Route:
- yes → create CLAUDE.md with Signal section (GATE 3 content) → GATE 5
- no → display: "Signal not configured. At the **planning stage**, inertia wins the default choice — the spec gets committed without a named competitor, and the question never gets asked." → exit

---

**GATE 2 — Detect Existing Signal Section**

Search CLAUDE.md for `## Signal` or `# Signal`.

Route:
- Signal section found → GATE 2A
- Signal section absent → GATE 3

**GATE 2A — Already Configured**

Display: "Signal is already configured. Inertia already has a named opponent at the planning stage — CLAUDE.md loads automatically every session, so the reminder is present without manual invocation. The configuration mechanism is the file load itself."

Exit.

---

**GATE 3 — Preview**

Display:

```
── Preview: Signal section to be appended ───────────────────────────────────

## Signal

Signal skills gather evidence before you commit to a build direction. Know
what you know before you build.

Available namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic.

**Inertia rule**: When signals are absent, inertia wins the default choice.
A topic is ready when signals exist to name what happens if nothing changes —
and to name why that outcome is unacceptable. Use /topic:status to check
readiness.

─────────────────────────────────────────────────────────────────────────────
```

Proceed to GATE 4.

---

**GATE 4 — Confirmation**

Ask: "Append this Signal section to CLAUDE.md? (yes / no)"

Route:
- yes → GATE 5
- no → display: "Signal not configured. At the **planning stage**, inertia wins the default choice — the spec gets committed without a named competitor, and the question never gets asked." → exit

---

**GATE 5 — Write and Report**

Append the Signal section (exact content from GATE 3) to CLAUDE.md.

Display: "Signal section appended to CLAUDE.md. At the planning stage, inertia now has a named opponent in Claude's context — the reminder loads automatically with the file."

Proceed to GATE 6.

---

**GATE 6 — Copilot Instructions (Optional)**

Check whether `.github/copilot-instructions.md` exists. Ask: "Also add a Signal section to .github/copilot-instructions.md? (yes / no)"

Route:
- yes, file exists → append Signal section → GATE 6A
- yes, file not found → create `.github/` if needed, create and write file → GATE 6A *(no sub-gate: creation is part of the confirmed append; no prior configuration to detect)*
- no → GATE 6B

**GATE 6A — Copilot Updated**

Display: "Signal section added to .github/copilot-instructions.md. At the **implementation stage**, inertia now has a named opponent in Copilot's context — the question is present while code is being suggested, not only while the spec is being written."

**GATE 6B — Copilot Skipped**

Display: "Copilot instructions not updated. At the **implementation stage**, inertia wins that context — while Copilot is suggesting code, there is no reminder to ask whether the build direction was chosen against a named alternative."

---

*signal-setup complete.*

---

## Variation Summary

| Variation | Axis | Primary Criteria Targeted | Hypothesis |
|-----------|------|--------------------------|------------|
| V-01 | Lifecycle emphasis | C-27, C-12 | Heading-level gate boundaries make lifecycle verifiable by outline scan |
| V-02 | Inertia framing | C-33, C-34 | Naming inertia as victor + causal chain makes every decline path land with felt consequence |
| V-03 | Output format | C-35 | `Route:` prefix + one-branch-per-line makes gate graph parseable without reading prose |
| V-04 | V-01 + V-02 | C-27, C-12, C-33, C-34 | Structural navigability + adversary framing are orthogonal improvements — combining them loses nothing |
| V-05 | V-02 + V-03 + C-22/C-23 | C-33, C-34, C-35, C-22, C-23 | Phase-indexed consequence anchors with explicit labels + parseable routing + adversary framing produces the structurally complete, rhetorically non-redundant spec |
