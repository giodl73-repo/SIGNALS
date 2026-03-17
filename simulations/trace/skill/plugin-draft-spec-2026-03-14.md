---
skill: trace-skill
topic: plugin
item: draft-spec
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-draft-2026-03-14.md
---

# /trace-skill -- draft-spec

**Invocation**: `/draft-spec --from simulations/scout/requirements/plugin-requirements-2026-03-14.md`
**Scenario**: Architect drafting the spec for the Signal /scout: namespace after scout findings are complete

## Phase 1: Setup

Scout artifacts found in simulations/scout/ and simulations/trace/skill/:
- requirements trace: plugin-scout-requirements-2026-03-14.md (loaded -- 20 requirements, R-01..R-20)
- feasibility trace: plugin-scout-feasibility-2026-03-14.md (loaded -- overall 38/100 scoped, 62/100)
- compliance trace: plugin-scout-compliance-2026-03-14.md (loaded -- 0 blocking, compliance-favorable)
Repo conventions detected: signal.skills.yaml uses YAML frontmatter, simulations/ path convention.

## Phase 2: Execute

**Architect** structures the spec:

```
# Specification: Signal /scout: Namespace (SIG-SCOUT-01)

## 1. Overview
8 lightweight PM-facing skills that answer "Should we build this?" through
structured market, technical, regulatory, and stakeholder investigation.
Default mode: lightweight (single-pass, auto-detect from context).

## 2. Skill Catalog
| ID | Skill | P0 Req | Default mode |
|----|-------|--------|-------------|
| S-01 | scout-competitors | R-01 | lightweight |
| S-02 | scout-feasibility | R-02 | lightweight |
| S-03 | scout-naming | R-03 | lightweight |
| S-04 | scout-compliance | R-04 | lightweight |
| S-05 | scout-market | R-05 | lightweight |
| S-06 | scout-stakeholders | R-06 | lightweight |
| S-07 | scout-positioning | R-07 | lightweight |
| S-08 | scout-requirements | R-08 | lightweight |

## 3. Artifact Naming
All scout outputs: simulations/scout/{skill}/{topic}-{signal}-{date}.md
Frontmatter required: skill, topic, item, date, skill_version, input

## 4. Constraints (from compliance trace)
- No user data persistence beyond repo artifacts (compliance-favorable)
- Git-native output only (SR 11-7 posture maintained)

## 5. Stock Roles
PM, Strategy, Architect, Compliance, Design, UX, GTM (auto-selected per skill)
```

**PM** validates P0 coverage: all 8 P0 scout requirements map to S-01..S-08. PASS.
**Strategy** validates differentiation: inertia-as-competitor appears in S-01. PASS.

## Phase 3: Findings

Coverage: 8/8 P0 requirements covered. 0 gaps.
Contradiction: R-06 (zero-barrier) vs R-10 (skills-in-repo requires CLI) -- resolved:
  scope "zero-barrier" to developers explicitly (A-05 amendment from review:customers).
Hotspot: Section 2 (Skill Catalog) is the heaviest -- 8 skills with 47 sub-skills total.
  Consider splitting into namespace-level spec + per-skill specs for maintainability.

## Phase 4: Amend

1. Add `--from` flag documentation more explicitly (which file formats accepted?)
2. Add the "no prior scout context" fallback explicitly in spec (ask 3-5 sentence description)
3. Consider splitting the master spec into 8 per-skill specs for maintainability at scale

## Verdict

**Result**: USEFUL. draft-spec produces a clean, traceable spec from scout artifacts.
Key strength: R-ID traceability in every spec section is genuinely valuable for sign-off.

### Findings Register
| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | Artifact naming uses old sim- prefix (fixed in spec) | FIXED |
| SF-02 | --from flag accepts paths but format docs missing | MINOR |
| SF-03 | Contradiction detection (R-06 vs R-10) surfaced cleanly | DELIGHT |
| SF-04 | Hotspot: skill catalog section will exceed T2 budget at 47 sub-skills | MAJOR |
