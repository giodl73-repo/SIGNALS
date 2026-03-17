# Scaffold Domain -- Create Roles + Pipeline + Design Area

When the user wants to set up a new domain of managed work (e.g., patents, compliance, security reviews), this skill creates the complete infrastructure in one operation.

## Input

- **Domain name**: Short lowercase identifier (e.g., `patent`, `compliance`, `security`)
- **Description**: What this domain manages (one sentence)
- **Roles**: List of specialist sub-roles needed (e.g., "lawyer, reviewer, strategist")
- **Pipeline stages**: Ordered list of stages the work flows through (e.g., "identify, evaluate, draft, review, submit")
- **Design area**: Whether to create a `design/{domain}/` directory (default: yes)

If the user doesn't provide all inputs, ask. Use the examples below for guidance on what to ask.

## Actions to Perform

### 1. Create the Role System (`.craft/roles/{domain}/`)

Every domain gets a **parent role** and **sub-roles**. Create these files:

#### Parent role: `.craft/roles/{domain}/{domain}.md`

```yaml
---
name: {domain}
version: "1.0"
archetype: structural

orientation:
  frame: "{How this role sees the problem domain}"
  serves: "{Who benefits from this role's work}"

lens:
  verify:
    - "{3-5 verification questions this role asks}"
  simplify:
    - "{3-5 principles this role follows}"

expertise:
  depth: "{What this role knows -- specific knowledge areas}"
  relevance: "{Why this knowledge matters to the project}"

scope: workspace
collaborates_with:
  - "{domain}:{sub-role-1}"
  - "{domain}:{sub-role-2}"

companion_files:
  - file: "{sub-role-1}.md"
    topic: "{One-line description}"
  - file: "{sub-role-2}.md"
    topic: "{One-line description}"

artifacts:
  - type: "{artifact-type}"
    directory: "design/{domain}/"
    format: markdown
    naming: "{naming-pattern}"

workflow:
  - step: "Intake"
    description: "{First step}"
  - step: "Execute"
    description: "{Main work}"
  - step: "Deliver"
    description: "{Output}"
---

# {Domain} -- Portfolio Manager

## Philosophy

{2-3 paragraphs on what this role does and why it matters}

## Key Responsibilities

{Bulleted list of responsibilities}
```

#### Sub-roles: `.craft/roles/{domain}/{sub-role}.md`

Same schema but with `archetype: craft` and no `companion_files`. Each sub-role:
- Has a distinct perspective (lens) on the domain
- Owns specific artifacts and workflow steps
- Collaborates with the parent and other sub-roles
- Body: Philosophy section + key responsibilities + domain-specific reference tables
- Target: 80-120 lines per file

### 2. Create the Pipeline (`.craft/pipelines/{domain}.yaml`)

```yaml
name: "{Domain} Pipeline"
description: "{One-line summary of the pipeline}"
docs: ".craft/pipelines/{domain}/"

stages:
  - id: {stage-1-id}
    description: "{What gets done}"
    role: {domain}:{sub-role}
    deliverables:
      - "{file-path-pattern}"
    review:
      reviewers: [{domain}:{reviewer-role}]
      blocking: true
```

Rules:
- Each stage has exactly one owning role
- Deliverables use `{id}` as a placeholder for the work item identifier
- Review gates are blocking for quality-sensitive stages, non-blocking for tracking stages
- Early stages (identify, evaluate) should be reviewed by different roles than the author

### 3. Create Stage Documentation (`.craft/pipelines/{domain}/`)

One `.md` file per stage, named `NN-{stage-id}.md` (e.g., `01-identify.md`).

Each stage doc contains:
```markdown
# Stage: {Name}

{2-3 sentence summary}

## Work

1. {Step-by-step instructions}
2. {What to produce}
3. {Who to involve}

## Gate Criteria

- [ ] {What must be true to advance to the next stage}
- [ ] {Quality check}
- [ ] {Review complete}

## Commit Message

`{domain}: {stage} — {what was done} ({work-item-id})`
```

### 4. Create Design Area (`design/{domain}/`)

#### `design/{domain}/README.md`
- Purpose and scope
- Current status
- Directory structure (show the tree)
- Links to roles and pipeline
- Key references

#### `design/{domain}/CLAUDE.md`
- Session driver with phase table
- Key references
- Session protocol (read this file, check current phase, resume)

#### Directory structure
```
design/{domain}/
├── README.md
├── CLAUDE.md
├── {work-items}/           # One directory per work item
│   └── {item-id}/
│       ├── plan.md         # Initial plan (stage 1 deliverable)
│       └── ...             # Other stage deliverables
└── research/               # Background research
```

### 5. Report What Was Created

Print a summary table:

```
Domain: {domain}
────────────────────────────────────────
Roles:     .craft/roles/{domain}/
           ├── {domain}.md (parent)
           ├── {sub-role-1}.md
           └── {sub-role-2}.md

Pipeline:  .craft/pipelines/{domain}.yaml
           .craft/pipelines/{domain}/
           ├── 01-{stage-1}.md
           └── 02-{stage-2}.md

Design:    design/{domain}/
           ├── README.md
           └── CLAUDE.md

Next:      Use the pipeline to start your first {domain} work item.
```

## Examples

### Example 1: Patent domain (what we built)
```
Domain: patent
Roles: patent (chair), counsel, finder, reviewer, strategist, prosecutor
Pipeline: identify -> evaluate -> draft -> review -> submit -> prosecute -> grant
Design area: design/patent/ with inventions/ subdirectory
```

### Example 2: Compliance domain
```
Domain: compliance
Roles: compliance (chair), auditor, remediator, certifier
Pipeline: scope -> assess -> remediate -> certify -> maintain
Design area: design/compliance/ with assessments/ subdirectory
```

### Example 3: Security review domain
```
Domain: security
Roles: security (chair), threat-modeler, pen-tester, responder
Pipeline: threat-model -> scan -> pentest -> remediate -> sign-off
Design area: design/security/ with reviews/ subdirectory
```

## Reference: Existing Domains

| Domain | Roles | Pipeline | Design Area | Purpose |
|--------|-------|----------|-------------|---------|
| astro | 17 sub-roles | 9 stages | design/astro/ | Compiler implementation |
| patent | 5 sub-roles | 7 stages | design/patent/ | IP portfolio management |
| flash | -- | 4 pipelines | design/flash/ | Data sync layer |
| admin | -- | 1 pipeline | design/admin/ | Artifact lifecycle |