---
skill: quest-variate
skill_target: corps-scan
round: 1
date: 2026-03-16
rubric_version: 1
---

# Variate R1 — corps-scan

5 complete prompt body variations for the `corps-scan` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (YAML-first inline vs section-gated table vs prose scan summary) | V-01, V-05 |
| Lifecycle emphasis (implicit steps vs explicit named phase gates) | V-03, V-05 |
| Phrasing register (technical-imperative vs conversational-descriptive) | V-02 |
| Role sequence (archaeologist first vs skeptic first before YAML draft) | V-04 |
| Inertia framing (naming the cost of no org map; Inertia Advocate note) | V-04 |

---

## V-01 — Output Format: YAML-First, Inline Annotation

**Axis**: Output format
**Hypothesis**: Producing the `org.yaml` block immediately -- before any prose explanation --
makes C-01 unfailsble by design: the model cannot promise YAML "below" because the YAML is the
first thing written. Inline YAML comments (`# detected from: /services/payments/`) satisfy C-09
co-located with the data rather than in a separate prose section. The amend menu at the end
satisfies C-08. Risk: C-06 pivot mode rationale may be compressed into a header comment rather
than a named prose sentence -- acceptable if the comment is substantive.

---

You are running `corps-scan`. Your job: walk this repo and produce a draft `org.yaml` -- the
org configuration contract -- ready for human review and confirmation.

This is a **draft-only** skill. Do NOT write `.craft/roles/` files. Do NOT instruct the user to
create role files. Do NOT include role file content. The output is `org.yaml` for review; the
separate `corps-build` skill materializes roles after the human confirms this draft.

---

**Step 1 -- Choose pivot mode**

Read the repo structure. Glob top-level directories and any `src/`, `packages/`, `services/`,
`apps/`, or `modules/` subdirectories. Identify which pivot mode fits the strongest signal:

| Mode | Use when... |
|------|-------------|
| `directory` | Repo has distinct top-level service or app directories |
| `concept` | Repo is a monolith organized by domain concepts (auth, billing, notifications) |
| `service` | Repo has explicit service manifests (docker-compose, k8s, helm charts) |
| `domain` | Repo is organized by bounded context or DDD aggregates |

State the selected pivot mode as a YAML comment on the first line of the output block.

**Step 2 -- Draft `org.yaml` immediately**

Write the complete YAML block now. Do not describe what the YAML would contain.
Structure:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [directory|concept|service|domain]
# rationale: [one sentence explaining why this mode was chosen from repo signals]

org:
  exec-office:
    name: "Office of the [CTO|VP Eng|Platform Lead -- infer from repo context or use placeholder]"
    # placeholder: confirm name before running corps-build

  groups:
    - name: "[Division/Tribe/Pillar name inferred from repo structure]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area name]"
          # detected from: [directory path, service name, or domain term found in repo]
          roles:
            - [Role name]     # e.g. PM, Engineer, Tech Lead
            - [Role name]
            # Inertia Advocate added automatically by corps-build -- not listed here
          [... repeat for each detected team area in this group]

    - name: "[Second group if warranted]"
      type: [...]
      teams:
        [...]
```

Rules:
- Every team area name must be traceable to an actual repo signal (directory name, service
  identifier, module path, or domain term). No generic names like `team-a` or `area-1`.
- Every team area must list at least 2 named roles. Role names must be specific
  (Engineer, PM, Tech Lead, Security Architect -- not "roles go here").
- Include at least one group-level container (division, tribe, or pillar) above teams.
  A flat list of teams with no grouping fails this step.
- Include the `exec-office` section even if the name is a placeholder.
- Add `# detected from:` comments on at least half the team areas.

**Step 3 -- Amend menu**

After the YAML block, write exactly this section:

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode]
  Alternatives detected: [list any other modes that could apply based on repo signals]
  How: re-run /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name used above]"
  How: re-run /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [list group names]
  Alternatives: [e.g. flatten to 1 group, split into 3, add cross-cutting platform pillar]
  How: re-run /corps-scan --groups "[new structure description]"
```

All three amend options are required. "Let me know if you want changes" does not count.

---

## V-02 — Phrasing Register: Conversational + Descriptive

**Axis**: Phrasing register
**Hypothesis**: A conversational, think-aloud register encourages the model to narrate its
detection reasoning naturally, which produces C-09 detection rationale and C-10 Inertia Advocate
notes without requiring explicit instructions for each. The risk is C-05 boundary enforcement --
the draft-only constraint must be stated explicitly even in conversational framing, or the model
may helpfully offer to create role files. This variation front-loads the boundary statement as
a named constraint, then switches to conversational mode for the rest.

---

You are running `corps-scan`. Here's what this skill does and what you'll produce at the end.

**What corps-scan does**

It reads the repo and drafts an `org.yaml` file -- a configuration contract that describes how
the codebase maps to a team structure. This is the first step in the `corps-*` skill family. The
human reviews this draft, amends it, and then runs `corps-build` to materialize the role files.

**One hard rule before you start**

corps-scan is a *draft-only* skill. You will not write `.craft/roles/` files. You will not
tell the user to create role files. You will not include role file content of any kind in your
output. If you find yourself about to describe what a role file would contain, stop -- that is
`corps-build` territory, not `corps-scan` territory. The org.yaml you produce is a proposal for
human review, nothing more.

---

**What to scan**

Start by exploring the repo structure. Walk the top-level directories. Look inside `src/`,
`services/`, `packages/`, `apps/`, and `modules/` if they exist. Note what you find -- what
names the directories use, how they cluster, whether there are service manifests or package
configs that reveal domain boundaries.

Tell me in a short paragraph (2-4 sentences) what the repo looks like and which pivot mode
fits best: `directory`, `concept`, `service`, or `domain`. Explain your choice in plain language.
For example: "The repo has a clear `/services` directory with six named subdirectories -- each
looks like an independent service. Directory mode is the best fit here."

---

**Draft the org.yaml**

Now write the draft `org.yaml`. This is the main deliverable -- produce it as an actual YAML
code block, not as a description of what it would contain.

The structure should look something like this, adapted to what you actually found:

```yaml
org:
  exec-office:
    name: "Office of the [title you inferred or a reasonable placeholder]"

  groups:
    - name: "[A group name -- division, tribe, or pillar -- that fits the repo structure]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area, named after what you found in the repo]"
          roles:
            - [Role 1]
            - [Role 2]
        - name: "[Another team area]"
          roles:
            - [Role 1]
            - [Role 2]
```

A few things to keep in mind as you write it:

- Every team area name should come from something real in the repo -- a directory name, a service
  identifier, a module name, a domain term in the code. If you're making up names, you're
  probably in the wrong mode.
- Each team should have at least 2 named roles. Think about who would realistically work on
  that area: a PM? an engineer? a tech lead? a security architect? Be specific.
- You need at least one grouping level above the teams (a division, tribe, or pillar).
  A flat list with no grouping makes the chart hard to navigate.
- Include an exec-office section. Even a placeholder name is better than nothing, because
  `corps-rob` will need it later.
- If you can see where a team area came from in the repo (a specific directory path or service
  name), add a comment on that team's entry so the human can verify it. Something like
  `# detected from: /services/payments/`.
- Note somewhere in your output that `corps-build` will automatically add an Inertia Advocate
  to each team's role files -- you don't need to include it in the draft YAML, but the user
  should know to expect it.

---

**Amend options**

Close with three concrete amend options the user can act on:

1. **Switch pivot mode** -- name the mode you used and the alternatives that might apply.
   Tell them the exact command to re-run with a different mode.
2. **Rename the exec office** -- name what you used as the placeholder and how to change it.
3. **Adjust the group structure** -- name how you grouped things and what a different grouping
   might look like (e.g., flatten, split, add a cross-cutting platform group).

For each, give a concrete command or instruction -- not just "let me know."

---

## V-03 — Lifecycle Emphasis: Explicit Phase Gates

**Axis**: Lifecycle emphasis
**Hypothesis**: Named phase gates (SCAN GATE, PIVOT GATE, DRAFT GATE, AMEND GATE) prevent the
most common failure mode -- jumping to a YAML block that isn't grounded in the repo (C-02 fail).
Each gate produces an explicit checkpoint statement that the next phase consumes, making it
mechanically hard to skip the scan. DRAFT GATE explicitly states the draft-only constraint
(C-05) as an entry condition before any YAML is written. This is the variation most likely
to pass C-02 on a sparse repo where the model might otherwise invent team names.

---

You are running `corps-scan`. Work through the phases in order. Each phase has an entry
condition and a gate confirmation. State the gate output before proceeding to the next phase.

This is a **draft-only** skill. At no point will you write `.craft/roles/` files, instruct
the user to create role files, or include role file content. The output is a draft `org.yaml`
for human review. Any phase output that produces role file content is a phase failure.

---

### PHASE 1 -- REPO SCAN

**Entry condition**: Repo directory accessible.

Glob the top-level repo structure. Also scan:
- `src/`, `services/`, `packages/`, `apps/`, `modules/` if present
- Any service manifests: `docker-compose.yml`, `k8s/`, `helm/`
- Any package configs: `package.json` workspaces, `Cargo.toml` workspace members, `go.work`

Build an internal registry (not written to output, only referenced in gate):
```
SCAN REGISTRY (internal):
  Top-level directories: [list]
  Service or module subdirectories: [list, or "none found"]
  Service manifests detected: [list, or "none"]
  Domain terms detected: [any obvious bounded contexts -- auth, billing, notifications, etc.]
```

**SCAN GATE**: Output:
> "SCAN GATE: found [n] top-level directories, [n] service/module subdirectories,
> [n] service manifests. Domain signals: [brief list or 'none detected']. Proceeding to pivot selection."

If the repo is empty or cannot be read, output:
> "SCAN GATE: repo is empty or unreadable. Pivot mode will default to `directory`. org.yaml
> will use placeholder team names -- replace with real names before running corps-build."
Then proceed with empty scan data.

---

### PHASE 2 -- PIVOT SELECTION

**Entry condition**: SCAN GATE confirmed.

Select the pivot mode that best fits the scan data:

| Mode | Select when... |
|------|----------------|
| `directory` | Distinct top-level service or app directories are the primary organizing structure |
| `concept` | Monolith organized by domain concepts; directories reflect business capabilities |
| `service` | Service manifests (docker-compose, k8s) are present and enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code, config, or directory structure |

Output the pivot decision as:
```
Pivot mode: [mode]
Rationale: [one sentence grounded in scan data -- name specific directories, files, or terms]
Alternative modes considered: [any that were plausible but rejected, and why]
```

**PIVOT GATE**: Output:
> "PIVOT GATE: pivot mode is `[mode]`. Rationale recorded. Proceeding to YAML draft."

---

### PHASE 3 -- YAML DRAFT

**Entry condition**: PIVOT GATE confirmed.
**Draft-only constraint**: This phase produces `org.yaml` only. No `.craft/roles/` files.
No role file content. No instructions to create role files. Violation of this constraint is a
phase failure regardless of YAML quality.

Using the scan data and selected pivot mode, produce the `org.yaml` draft now:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [selected mode]
# status: DRAFT -- for human review and confirmation before corps-build

org:
  exec-office:
    name: "[Inferred exec title or placeholder -- confirm before corps-build]"

  groups:
    - name: "[Group 1 name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- traceable to repo signal]"
          # detected from: [directory path, service name, or domain term]
          roles:
            - [Named role 1]
            - [Named role 2]
            # Note: Inertia Advocate added automatically by corps-build

        - name: "[Team area 2]"
          # detected from: [repo signal]
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2 name, if warranted]"
      type: [...]
      teams:
        [...]
```

Constraints verified before writing:
- [ ] Every team area name traceable to a real repo signal
- [ ] Every team area has 2+ named roles (not "roles go here")
- [ ] At least one group-level container above teams
- [ ] exec-office section present
- [ ] `# detected from:` comment on at least half the team areas
- [ ] No `.craft/roles/` content anywhere in this output

**DRAFT GATE**: Output:
> "DRAFT GATE: org.yaml draft complete. [n] groups, [n] team areas, [n] roles across all teams.
> Exec office: '[name]'. Draft-only constraint: confirmed -- no role files written."

---

### PHASE 4 -- AMEND OPTIONS

**Entry condition**: DRAFT GATE confirmed.

Write the amend menu. All three options are required:

```
## Amend Options

AMEND-A: Switch pivot mode
  Current mode: [mode from Phase 2]
  Alternative modes: [any plausible alternatives identified in Phase 2]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current name: "[name from YAML]"
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current structure: [n] [group type(s)] -- [list group names]
  Possible adjustments: [e.g., collapse to 1 group, split engineering from product, add platform pillar]
  Command: /corps-scan --groups "[description of desired structure]"
```

**AMEND GATE**: Output:
> "AMEND GATE: 3 amend options written. corps-scan complete. Review org.yaml draft above, then
> confirm or amend before running /corps-build."

---

## V-04 — Role Sequence + Inertia Framing (Combination)

**Axes**: Role sequence (repo archaeologist before org drafter) + inertia framing (naming the
cost of no org map as a named pattern)
**Hypothesis**: Running a "repo archaeologist" role first forces C-02 grounding by construction --
the drafter cannot invent team names because it has an explicit inventory to draw from. A
"status-quo challenger" role in the middle names the failure mode of skipping corps-scan (teams
named by convention, wrong people reviewing wrong PRs, no exec office defined). This primes the
amend options to be anti-inertia rather than generic. C-10 Inertia Advocate note emerges
naturally from the role that frames the inertia risk. This combination is strongest on C-02,
C-09, and C-10, and carries the best C-08 amend quality because each option is framed against
the specific stagnation pattern found.

---

You are running `corps-scan`. Work through three roles in sequence. Do not advance to a role
until the prior role's output is complete.

**Hard constraint that applies to all roles**: This is a draft-only skill. No role may write
`.craft/roles/` files, include role file content, or instruct the user to create role files.
The final output is a draft `org.yaml` for human review. `corps-build` runs after human
confirmation.

---

### ROLE 1 -- REPO ARCHAEOLOGIST

Your job: discover what exists. Produce an inventory, nothing more.

Walk the repo. Note every top-level directory, every subdirectory under `src/`, `services/`,
`packages/`, `apps/`, `modules/`. Check for service manifests (`docker-compose.yml`, `k8s/`,
Helm charts). Check for workspace configs (npm workspaces, Cargo workspace, go.work).

Output:

```
## Repo Archaeology -- {{date}}

Top-level directories: [list]
Service/module subdirectories: [list, or "none"]
Service manifests: [list, or "none"]
Domain terms detected: [any bounded context names, business capability names, or "none"]

Pivot mode candidates:
  - directory: [yes/possible/no -- explain in one phrase]
  - concept: [yes/possible/no -- explain in one phrase]
  - service: [yes/possible/no -- explain in one phrase]
  - domain: [yes/possible/no -- explain in one phrase]

Strongest signal: [mode] because [one sentence]
```

If the repo is empty or inaccessible: state this explicitly and use a `directory` pivot with
placeholder names. Do not invent names.

---

### ROLE 2 -- STATUS-QUO CHALLENGER

Before drafting the org, name what happens when teams skip this step.

Look at what the Repo Archaeologist found. What does the repo's *current* implied org structure
look like if no `org.yaml` exists? Name the stagnation pattern (one of the following, or define
your own if none fits):

- **Name Soup**: directories use inconsistent naming conventions with no grouping logic visible
- **Lone Archaeologist**: the repo has one clear owner pattern and no evidence of shared team
  structure
- **Service Island**: services exist but are disconnected -- no grouping, no exec layer, no
  standard roles
- **Ghost Org**: the repo is mature but has no org configuration at all -- the team org lives
  only in someone's head

Output:

```
## Status-Quo Assessment

Stagnation Pattern: [name]
Evidence: [what in the archaeology supports this -- names directories, file counts, or absence]
Cost of skipping corps-scan: [one sentence -- what stays undefined, what breaks downstream]

Note: Inertia Advocate will be auto-added to each team's roles when corps-build runs -- this
role explicitly advocates for the status-quo and must be overcome during reviews. Naming it
now prepares the team to expect it.
```

---

### ROLE 3 -- ORG DRAFTER

Your job: produce the `org.yaml` draft from the Repo Archaeology inventory. The Stagnation
Pattern from Role 2 informs the amend options you generate -- each option should address one
dimension of the pattern.

**Draft-only constraint**: No `.craft/roles/` files. No role file content. org.yaml only.

Using the strongest pivot mode from Role 1, write:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [selected mode]
# stagnation-pattern: [pattern from Role 2 -- for amend context]
# status: DRAFT -- review and confirm before corps-build

org:
  exec-office:
    name: "[Infer from repo context or use: 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from archaeology inventory]"
          # detected from: [exact directory or service name from Role 1]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build

        - name: "[Team area 2]"
          # detected from: [...]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if warranted by inventory]"
      type: [...]
      teams: [...]
```

Every team area must come from the Role 1 inventory. If the inventory is empty, use explicit
placeholders labeled `# PLACEHOLDER -- replace before corps-build`. No invented names.

**Amend options (anti-inertia)**

Each option must address one dimension of the Stagnation Pattern identified in Role 2:

```
## Amend Options

AMEND-A: Switch pivot mode
  Addresses: [which dimension of the stagnation pattern this helps clarify]
  Current: [mode] | Alternatives: [list from Role 1]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Addresses: [why the exec office name matters given the stagnation pattern]
  Current: "[name]"
  Command: /corps-scan --exec-office "[name]"

AMEND-C: Adjust group structure
  Addresses: [how the grouping choice relates to the stagnation pattern]
  Current: [structure description]
  Alternatives: [options based on the inventory]
  Command: /corps-scan --groups "[description]"
```

---

## V-05 — Output Format + Lifecycle Emphasis (Combination)

**Axes**: Output format (scaffolded section skeleton) + lifecycle emphasis (section headers as
implicit phase checkpoints)
**Hypothesis**: Giving the model an explicit output skeleton with required sections forces
completeness by construction -- every section must be filled, so a missing YAML block (C-01),
missing exec office (C-07), or missing amend menu (C-08) requires actively skipping a named
section rather than passively omitting it. The section headers serve as lightweight phase
checkpoints without the verbosity of explicit gate statements. This is the variation most
likely to produce a complete, well-structured output on first run. The risk is C-09 depth --
the fixed skeleton may be filled formulaically, with shallow inline comments rather than
substantive rationale.

---

You are running `corps-scan`. Produce a draft `org.yaml` for human review and confirmation.

**Non-negotiable constraint**: This skill does not write `.craft/roles/` files. It does not
tell the user to create role files. It does not include role file content. org.yaml is the
only output. `corps-build` runs after the human confirms this draft.

Fill each section below in order. Every section is required. A missing section is an error.

---

### Section 1 -- Repo Scan

Scan the repo structure. Walk top-level directories and any `src/`, `services/`, `packages/`,
`apps/`, `modules/` subdirectories. Note service manifests and workspace configs if present.

Write a bullet list of discovered directories and signals (one line each):

```
- [directory or path] -- [one phrase: what this tells you about the org structure]
- [directory or path] -- [...]
```

If the repo is empty: write "Repo is empty or unreadable -- proceeding with placeholder draft."

---

### Section 2 -- Pivot Decision

Name the pivot mode selected and give one sentence of rationale grounded in the scan:

```
Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence naming specific repo signals that drove the choice]
```

---

### Section 3 -- Draft org.yaml

Write the complete `org.yaml` block. This is the primary deliverable.

Requirements:
- Include `exec-office` section with a name (placeholder is fine, but it must be present)
- Include at least one group-level container (division, tribe, or pillar) above teams
- Each team area name must be traceable to a repo signal from Section 1
- Each team area must list at least 2 named roles (Engineer, PM, Tech Lead, etc.)
- Add `# detected from:` comments on at least half the team areas
- Add a note `# Inertia Advocate: added automatically by corps-build` inside at least one
  team's roles block, so the user knows to expect it

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [mode]
# rationale: [one sentence]
# status: DRAFT -- confirm with human before running corps-build

org:
  exec-office:
    name: "[exec office name or placeholder]"

  groups:
    - name: "[group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[team area]"
          # detected from: [repo signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build
        - name: "[team area 2]"
          # detected from: [repo signal]
          roles:
            - [Named role]
            - [Named role]

    - name: "[group 2, if warranted]"
      type: [...]
      teams:
        [...]
```

Do not describe what the YAML would contain. Write it.

---

### Section 4 -- Amend Menu

Write all three amend options. Each must be actionable, not generic:

```
AMEND-A: Switch pivot mode
  Current: [mode] | Why you might switch: [one sentence]
  How: /corps-scan --pivot [alternative mode]

AMEND-B: Rename exec office
  Current: "[name in Section 3]" | Why you might rename: [one sentence]
  How: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [description of grouping from Section 3]
  Alternatives: [2-3 named options based on what you found in Section 1]
  How: /corps-scan --groups "[description]"
```

"Let me know if you want changes" does not pass this section. Name the options.

---

### Section 5 -- Confirmation Prompt

Close with exactly this line (fill in the blanks):

> "Draft org.yaml produced using `[mode]` pivot mode. [n] groups, [n] team areas, [n] total
> roles. Review the draft above. Amend using options A-C, or confirm to run `/corps-build`."
