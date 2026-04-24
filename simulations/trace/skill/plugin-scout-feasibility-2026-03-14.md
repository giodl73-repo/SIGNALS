---
skill: trace-skill
topic: plugin
item: scout-feasibility
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-feasibility

**Invocation**: `/scout-feasibility "Signal plugin -- 48 skills across 9 namespaces, skills-in-repo model"`
**Scenario**: Architect evaluating feasibility of building all 48 signal skills in one sprint

## Phase 1: Setup

No package.json, tsconfig.json, Cargo.toml found. Fallback to CLAUDE.md + program.yaml + signal.bindings.md. Git log: 1 contributor, 3 commits. Stack: TypeScript/YAML (asserted in CLAUDE.md only). Scope parsed: 48 skills, 9 namespaces, skills-in-repo model, one sprint.

**SF-01 (P2)**: Silent fallback when stack files absent -- skill should surface the inference explicitly ("Stack inferred from CLAUDE.md assertion only -- no package.json found").

**SF-03 (P2)**: "One sprint" inferred without surfacing the inference. Spec should require skill to show inferred team size and timeline when flags are omitted.

## Phase 2: Execute

### Component complexity (Architect)

| Component | Complexity | Risk | Build/Buy |
|-----------|-----------|------|-----------|
| 9 namespace SKILL.md bodies | 3/5 | YELLOW | Build |
| craft generate compiler | 3/5 | YELLOW | Use existing |
| Binding variants (5 x program.yaml) | 4/5 | RED | Build |
| SKILL.md schema / template | 3/5 | YELLOW | Build (blocker for other skills) |
| trial scenarios per skill | 4/5 | YELLOW | Build |
| E2E validation pipeline | 4/5 | RED | Build |

**RED blockers**: Multi-binding packaging (5 variants x 48 skills = 240 artifacts) and no canonical SKILL.md schema to assess authoring complexity.

**SF-02 (P1)**: No canonical SKILL.md schema discoverable in repo -- Architect cannot score authoring complexity accurately. The template skill is a prerequisite for accurate feasibility assessment.

### PM timeline overlay

Estimated 88h vs ~80h available for 1 contributor. Borderline over budget.

### Strategy recommendation

Defer multi-binding to sprint-2. Sprint-1 target: flat-standalone binding only, compiler-assisted. Scoped feasibility: 62/100 (FEASIBLE with caveats).

## Phase 3: Findings

| Component | Rating | Notes |
|-----------|--------|-------|
| Flat binding (48 SKILL.md stubs) | GREEN | Compiler generates; 1 day |
| SKILL.md bodies (9 namespaces) | YELLOW | ~5h per namespace body |
| Template skill first | GREEN | Prerequisite -- must do first |
| Multi-binding variants | RED | Defer to sprint-2 |
| Trial scenarios | YELLOW | Concurrent with body authoring |

**Overall (full scope)**: 38/100 NOT FEASIBLE in one sprint
**Overall (scoped -- flat binding only)**: 62/100 FEASIBLE with 4 prerequisites

**Prerequisites**: (1) SKILL.md template defined, (2) compiler hydration validated, (3) scope limited to flat binding, (4) team size confirmed

## Phase 4: Amend

1. Constrain to one binding variant for sprint-1
2. Validate compiler (craft generate --hydrate) before authoring at scale
3. Define SKILL.md schema as sprint-0 deliverable

## Verdict

**Result**: USEFUL. Correctly surfaces two red blockers. SKILL.md template is a prerequisite for both accurate feasibility scoring and skill authoring.

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | Silent fallback when stack files missing -- surface inference explicitly | P2 |
| SF-02 | No SKILL.md schema in repo -- Architect cannot score authoring complexity | P1 |
| SF-03 | Inferred team size and timeline not surfaced to user | P2 |
