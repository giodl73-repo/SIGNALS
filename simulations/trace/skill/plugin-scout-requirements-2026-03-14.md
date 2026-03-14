---
skill: trace-skill
topic: plugin
item: scout-requirements
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-requirements

**Invocation**: `/scout-requirements "Signal plugin -- build all 48 atomic skills with binding variants and topic narrative management"`
**Scenario**: Architect and PM pair starting implementation sprint

## Phase 1: Setup

Prior scout runs searched. Trace artifacts found in `simulations/trace/skill/` (not `simulations/scout/`). Spec says "pull from prior scout runs" but does not specify which directory to search.

**SF-01 (P1)**: Undefined search path for prior scout runs. Spec must specify: search both `simulations/scout/` (real runs) AND `simulations/trace/skill/` (hand-compiled traces). Without this rule, requirements context is lost.

## Phase 2: Execute

20 requirements extracted across PM / Architect / UX / Compliance lenses.

### Must Have (P0)

| ID | Category | Requirement |
|----|----------|-------------|
| R-01 | Functional | 48 atomic skills as independent SKILL.md files |
| R-02 | Functional | /topic: namespace with new/status/report/plan/story/echo skills |
| R-03 | Functional | signal.program.yaml as single source of truth for all bindings |
| R-04 | Functional | Artifact naming: {topic}-{item}-{date}.md in simulations/{namespace}/{skill}/ |
| R-05 | Functional | Frontmatter in every artifact (skill, topic, item, date, skill_version, input) |
| R-06 | Constraint | Binding-agnostic skill bodies -- no invocation form in skill content |
| R-07 | Constraint | CLI-only operation, no GUI, no server |
| R-08 | Constraint | Works on Windows, macOS, Linux |
| R-09 | Constraint | Zero config first run -- copy one SKILL.md and run |
| R-10 | Constraint | skills-in-repo as primary delivery model (not plugin) |

### Should Have (P1)

| ID | Category | Requirement |
|----|----------|-------------|
| R-11 | Functional | --json sidecar flag for structured output |
| R-12 | Functional | signal.manifest.json upgrade contract with version-hash strategy |
| R-13 | Functional | /topic:report --format teams for Teams-card output |
| R-14 | Functional | binding-flat.program.yaml generates 48 standalone skills |
| R-15 | Functional | binding-grouped.program.yaml generates 9 namespace dispatchers |
| R-16 | Usability | Each skill surfaces custom persona path on first run |
| R-17 | Usability | --quick and --full flags work on all skills regardless of default mode |

### Could Have (P2)

| ID | Category | Requirement |
|----|----------|-------------|
| R-18 | Functional | /signal:achieve namespace for achievement system |
| R-19 | Functional | CREST.md as alternative input to program.yaml |
| R-20 | Functional | /trace-skill as standalone skill for skill body validation |

## Phase 3: Findings

**Dependency root**: R-09 (zero config first run) blocks R-01, R-02, R-06, R-16. All usability requirements depend on first-run experience.

**Ambiguity flags**:
- AF-01: Binding generation spec not finalized -- flat vs grouped vs plugin constraints differ
- AF-02: ROLE.md schema not defined -- custom persona path undefined
- AF-03: TOPICS.md ownership ambiguous -- who updates it, when, automatically or manually?

**Suspicious silences**:
- SS-01: No versioning/migration strategy for simulation data as skills evolve
- SS-02: No equivalence testing spec -- how to validate flat and grouped bindings produce equivalent results
- SS-03: Scout search path (trace artifacts vs real runs) -- critical for requirements context

## Phase 4: Amend

1. Promote R-12 (manifest upgrade contract) to P0 -- teams need upgrade path before any binding ships
2. Add R-21 (explicit search path behavior for prior scout runs) as P0
3. Escalate SS-02 (binding equivalence testing) to pre-sprint blocker -- equivalence is the whole point of binding-agnostic design

## Verdict

**Result**: USEFUL. 20 real requirements extracted. Dependency root (R-09) and 3 suspicious silences surfaced. SF-01 (undefined search path) is a spec gap that affects all 8 scout skills.

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | Undefined search path for prior scout runs (trace vs real) | P1 |
| SF-02 | AF-01: Binding generation spec not finalized | P1 |
| SF-03 | AF-02: ROLE.md schema undefined | P1 |
| SF-04 | AF-03: TOPICS.md ownership ambiguous | P1 |
| SF-05 | SS-01: No versioning/migration for simulation data | P2 |
| SF-06 | SS-02: No binding equivalence testing spec | P2 |
| SF-07 | SS-03: Scout search path undefined | P2 |
