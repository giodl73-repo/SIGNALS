Now I have the full picture: 13 prior rounds were against a much larger rubric (up to 48 criteria). This is Round 1 against the new v1 rubric (10 criteria, 100 pts). Fresh axes apply.

---

# Variate R1 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v1 rubric (10 criteria, 100 pts). This is Round 1 against the new rubric. No prior axes to avoid.

**Single-axis selections:**
- V-01 — **Lifecycle emphasis**: explicit 3-phase structure with phase-closure separators; phases enforce criterion order
- V-02 — **Output format**: pre-YAML inventory as a structured table with typed columns
- V-03 — **Phrasing register**: conversational/descriptive second-person narrative, no DO/MUST imperatives

**Combinations:**
- V-04 — Lifecycle emphasis + Phrasing register (explicit phase gates, conversational language)
- V-05 — Lifecycle emphasis + Output format + Phrasing register (full integration: phase gates + typed inventory table + imperative DO/MUST register)

**Hypothesis:** All five variations are designed to satisfy all 10 criteria. Scoring differences will surface which structural mechanisms most reliably produce C-09 (pre-YAML inventory) and C-10 (front-loaded draft boundary), the two aspirationals that represent the main spread between 80 and 100.

---

## V-01 — Lifecycle emphasis

**Axis:** Explicit 3-phase structure (SCAN → DRAFT → AMEND) with phase-closure separator lines. The draft boundary appears as the document's first line. Each phase has a single job; no phase content bleeds across phase boundaries.

**Hypothesis:** Phase gates enforce criterion order mechanically — C-10 fires before any scan output, C-09 fires before the YAML block, C-08 fires only after the YAML is complete. This should maximize all three aspirationals by making the sequence structurally unavoidable.

---

```
DRAFT NOTICE: This output is a draft org.yaml for human review and confirmation.
No .craft/roles/ files will be written.

You are running /corps-scan {repo}.

--- PHASE 1: SCAN ---

Walk the repo. Collect signals: top-level directory names, subdirectory paths under
prominent source roots, module identifiers, service path segments, and domain terminology
appearing in file names or package names.

List your findings as a pre-YAML scan inventory before writing any YAML:

- [signal name] — [source path]
- [signal name] — [source path]
...

Include one entry per distinct signal. The inventory must appear before the YAML block.
It is what allows the reviewer to verify that the YAML is grounded in actual repo
structure, not invented names.

After listing signals, declare your pivot mode and rationale:

> Pivot mode: [directory / concept / service / domain]
> Rationale: [one sentence explaining why this mode fits the signals found above]

When you have listed the inventory and declared the pivot mode, emit:
--- [SCAN COMPLETE] ---

--- PHASE 2: DRAFT ---

Produce a single org.yaml code fence. The YAML must contain:

  pivot-mode: [matches Phase 1 declaration]

  exec-office:
    name: [placeholder or detected exec name]

  groups:
    - name: [group name]
      teams:
        - name: [team name]
          roles:
            - [substantive role name]
        ...

Requirements:
- groups: must contain at least one named group with teams beneath it
- Each team must have a roles: list with at least one substantive role name
  (e.g., "Engineer", "Product Manager", "Tech Lead")
- Do NOT include "Inertia Advocate" in any roles list — it is added automatically
  by corps-build and is outside corps-scan scope
- Do NOT write .craft/roles/ file content anywhere in this output

When the code fence is complete, emit:
--- [DRAFT COMPLETE] ---

--- PHASE 3: AMEND ---

List at least 2 named amend options from this set:

- AMEND: switch pivot mode — run /corps-scan --pivot [mode]
- AMEND: rename exec office — run /corps-scan --exec-office "[name]"
- AMEND: adjust group structure — run /corps-scan --groups "[restructure instruction]"

Each option must name the specific change and the action to take it.
A generic "let me know if you want changes" does not count.
```

---

## V-02 — Output format

**Axis:** The pre-YAML scan inventory is a structured table with typed columns (`Signal | Type | Source Path | Pivot Relevance`). Column vocabulary is constrained. The draft boundary opens the output. Amend options are formatted as a labeled list with action pairs.

**Hypothesis:** A typed table makes C-02 grounding independently verifiable by column inspection rather than prose reading. The `Pivot Relevance` column makes the mode selection step traceable to specific rows. This should increase C-09 quality and improve C-06 rationale specificity.

---

```
DRAFT NOTICE: This is a draft org.yaml for human review and confirmation.
No .craft/roles/ files will be written anywhere in this output.

You are running /corps-scan {repo}.

STEP 1 — SCAN INVENTORY

Walk the repo. Before writing any YAML, produce this table:

| Signal | Type | Source Path | Pivot Relevance |
|--------|------|-------------|-----------------|

Column rules:
- Signal: the name of the detected signal (directory name, service identifier, module name,
  domain term)
- Type: exactly one of — directory / module / service / domain-term
- Source Path: the file system path or location where the signal was found
- Pivot Relevance: exactly one of — high / medium / low

Include at minimum 3 rows. If the repo yields fewer than 3 distinct signals, write 3 rows
with Pivot Relevance: low and add a note that the repo is signal-sparse.

DO NOT begin STEP 2 until the table is written.

STEP 2 — PIVOT MODE

After the inventory table, write:

> Selected pivot mode: [directory / concept / service / domain]
> Rationale: [one sentence citing at least one specific Signal from the table above]

The rationale must name a signal from the inventory table. A generic rationale that could
apply to any repo does not satisfy this step.

STEP 3 — ORG.YAML DRAFT

Produce a single ```yaml code fence containing the draft org.yaml. Required sections:

  pivot-mode: [matches Step 2]

  exec-office:
    name: [name or placeholder]

  groups:
    - name: [group name]
      teams:
        - name: [team name based on inventory signals]
          roles:
            - [substantive role name]

Rules:
- groups: must have at least one named group containing teams beneath it
- Each team must have a roles: list with at least one substantive role name
- Do NOT include "Inertia Advocate" — added by corps-build, not corps-scan
- Do NOT write .craft/roles/ file content anywhere in this output

STEP 4 — AMEND OPTIONS

Close with at least 2 amend options in this format:

AMEND A — [name the change]: [command or action to take it]
AMEND B — [name the change]: [command or action to take it]

Options must be drawn from: change pivot mode / rename exec office / adjust group structure.
Each option must be independently actionable.
```

---

## V-03 — Phrasing register

**Axis:** Conversational, second-person narrative throughout. No DO/MUST imperatives. Instructions are written as guidance the model follows naturally. The draft boundary is the opening sentence of a natural paragraph. The amend options are presented as suggestions to the reviewer.

**Hypothesis:** Conversational register tests whether criterion satisfaction survives under lighter structural pressure. If criteria fail under conversational phrasing, the gap is in structure not register — pointing to where harder enforcement is needed.

---

```
Start with a single sentence telling the reviewer that what follows is a draft for their
review — nothing gets built from this output.

Then scan the repo before writing any YAML. Look at directory names, service paths, module
names, and any domain terminology appearing in file or package names. List what you find as
a readable inventory — a bulleted list of signal names with the path where you found each one.
This inventory is what allows the reviewer to check that the YAML you produce is grounded in
the actual repo rather than invented or generic names.

Next, pick a pivot mode: directory, concept, service, or domain. Write one sentence explaining
why you chose it, naming at least one signal from your inventory as evidence.

Now write the org.yaml in a YAML code fence. It should include:

- The pivot mode you selected
- An exec-office section with at least a name field (a placeholder is fine)
- At least one group that organizes teams beneath it
- A roles list for each team with at least one real role name, like "Engineer" or
  "Product Manager"

Two things to leave out:
- Don't add an "Inertia Advocate" to any roles list — corps-build adds that automatically
- Don't write or draft any .craft/roles/ file content — that's corps-build's job, not yours

End by offering 2 or more ways the reviewer can adjust the draft before confirming it.
For example: switch to a different pivot mode, rename the exec office, or restructure the
groups into more or fewer containers. Make each suggestion specific enough that the reviewer
knows exactly what to ask for and what would change.
```

---

## V-04 — Lifecycle emphasis + Phrasing register

**Axis combination:** The 3-phase structure of V-01 (SCAN → DRAFT → AMEND with closure markers) combined with the conversational register of V-03. Phases provide structural order; conversational language avoids mechanical-sounding instructions.

**Hypothesis:** Conversational phrasing within explicit phase boundaries should retain the C-10/C-09/C-08 ordering benefits of V-01 while being easier for the model to execute smoothly. If V-01 produces rigid or clunky outputs, V-04 may produce more natural outputs with the same criterion coverage.

---

```
You are running /corps-scan {repo}.

Open with a single sentence stating that this is a draft for review — nothing gets built yet.

SCAN PHASE

Before you write any YAML, walk the repo and list what you find. Look for top-level directory
names, service subdirectories, module identifiers, and any domain terminology in file or
package names. List each signal as a bullet with the path where you found it. This is your
pre-YAML inventory — it's how the reviewer can confirm that the YAML you produce is grounded
in actual repo structure.

After listing your signals, choose a pivot mode — directory, concept, service, or domain —
and explain in one sentence why that mode fits what you found.

When the inventory and pivot mode are written, emit: --- [SCAN COMPLETE] ---

DRAFT PHASE

Write the org.yaml in a single YAML code fence. What it needs:

- `pivot-mode:` matching what you declared in the SCAN PHASE
- `exec-office:` with at least a name field (a placeholder is acceptable)
- `groups:` with at least one named group that has teams beneath it
- `roles:` under each team with at least one substantive role name

Two things to leave out:
1. Don't include "Inertia Advocate" in any roles list — corps-build adds that automatically
2. Don't write .craft/roles/ file content anywhere — that's corps-build's job, not yours

When the YAML code fence is complete, emit: --- [DRAFT COMPLETE] ---

AMEND PHASE

Close with 2 or more specific amend options. Each option should tell the reviewer what
changes and how to request it. Draw from these three amend types:

- Switch pivot mode (e.g., "AMEND: switch to service mode — run /corps-scan --pivot service")
- Rename exec office (e.g., "AMEND: rename exec office — run /corps-scan --exec-office 'Platform'")
- Adjust group structure (e.g., "AMEND: split into two pillars — run /corps-scan --groups 'split by domain'")

A vague "let me know if you want changes" doesn't count — each option needs to name the
specific change and how to take it.
```

---

## V-05 — Lifecycle emphasis + Output format + Phrasing register (full integration)

**Axis combination:** All three single-axis variations combined. Phase gates enforce criterion order (V-01). The pre-YAML inventory is a typed table with constrained column vocabulary (V-02). Instructions use strong DO/MUST imperative register (inverts V-03, applying the strongest structural pressure across all three axes simultaneously).

**Hypothesis:** Full integration with imperative register should produce the most consistently criterion-complete outputs. If any criteria fail under this variation, the cause is a gap in the prompt logic itself, not a phrasing or formatting issue — making V-05 the most diagnostic variation in the set.

---

```
DRAFT BOUNDARY: This output is a draft org.yaml for human review and confirmation.
No .craft/roles/ files will be written at any point.

You are running /corps-scan {repo}.

=== SCAN PHASE ===

DO walk the repo before producing any YAML or making any pivot mode decision.
DO collect signals: top-level directory names, service subdirectory paths, module identifiers,
and domain-term file and package names.

MUST produce the pre-YAML signal inventory as a table with these exact columns:

| Signal | Type | Source Path | Pivot Relevance |
|--------|------|-------------|-----------------|

- Type MUST be exactly one of: directory / module / service / domain-term
- Pivot Relevance MUST be exactly one of: high / medium / low
- MUST include at least 3 rows
- DO NOT embed the inventory inside the YAML as comments only
- DO NOT begin the pivot mode declaration until the table is complete

After the table, DO declare pivot mode and rationale:

> PIVOT MODE: [directory / concept / service / domain]
> RATIONALE: [one sentence citing at least one Signal by name from the inventory table]

DO NOT choose a pivot mode without citing a named signal from the table.

When the table and pivot mode declaration are complete, emit:
=== [SCAN COMPLETE — DRAFT PHASE BEGINS] ===

=== DRAFT PHASE ===

MUST produce exactly one ```yaml code fence containing the full org.yaml.

The YAML MUST contain all four of these sections:

  pivot-mode: [matches SCAN PHASE declaration]

  exec-office:
    name: [detected or placeholder name]

  groups:
    - name: [group name]
      teams:
        - name: [team name grounded in inventory signals]
          roles:
            - [substantive role name]

Requirements:
- groups: must contain at least one named group with teams beneath it (a flat team list
  at the top level without a group container does not pass)
- Each team must have a roles: list with at least one substantive role name
  (e.g., "Engineer", "Product Manager", "Tech Lead")
- DO NOT include "Inertia Advocate" in any roles list — it is added by corps-build
- DO NOT write .craft/roles/ file content anywhere in this output

When the code fence is complete, emit:
=== [DRAFT COMPLETE — AMEND PHASE BEGINS] ===

=== AMEND PHASE ===

MUST conclude with at least 2 amend options from this closed set:

- AMEND: switch pivot mode — run /corps-scan --pivot [mode]
- AMEND: rename exec office — run /corps-scan --exec-office "[name]"
- AMEND: adjust group structure — run /corps-scan --groups "[restructure instruction]"

Each AMEND entry MUST name the specific change and the command to take it.
DO NOT write a generic offer to adjust things. Each option must be independently actionable.
```

---

## Summary

| Variation | Axis | Key Mechanism | Primary Criteria Pressure |
|-----------|------|---------------|--------------------------|
| V-01 | Lifecycle emphasis | Phase gates (SCAN/DRAFT/AMEND) with closure separators | C-09, C-10 ordering enforced |
| V-02 | Output format | Typed 4-column inventory table with constrained vocabulary | C-02, C-09 grounding quality |
| V-03 | Phrasing register | Conversational second-person narrative, no imperatives | Baseline criterion survival under light structure |
| V-04 | Lifecycle + Phrasing | Phase gates with conversational language | C-10/C-09/C-08 ordering, natural execution |
| V-05 | Lifecycle + Format + Phrasing | Phase gates + typed table + DO/MUST imperatives | Maximum structural forcing, diagnostic variation |
