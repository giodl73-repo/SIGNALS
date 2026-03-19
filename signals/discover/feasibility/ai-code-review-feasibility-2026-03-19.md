---
skill: discover-feasibility
topic: ai-code-review
date: 2026-03-19
score: 72
label: FEASIBLE WITH CAVEATS
team_inferred: 2 engineers (inferred from Signal plugin team size)
timeline_inferred: 3-4 sprints (6-8 weeks)
hours_available: 480
hours_estimated: 340
stack_source: Signal plugin architecture (signal.skills.yaml, PRINCIPLES.md)
inertia_cost_per_sprint: 28 hrs reviewer time (~$3,360/sprint for 5-dev team)
---

# Feasibility Assessment: ai-code-review

---

## INFERENCE GATE

Feature: AI-powered code review skill that produces structured, topic-scoped review artifacts with cross-PR pattern detection, integrated into the Signal plugin namespace architecture.

Team: 2 engineers -- inferred from: Signal plugin is authored by a small team; skill authoring follows the pattern of one author + one reviewer per skill (evidenced by quest loop structure in signal.skills.yaml).

Timeline: 3-4 sprints (6-8 weeks) -- inferred from: comparable skills (discover-competitors, discover-risk) went through 20+ quest rounds over ~2 weeks each; a new skill with LLM integration, artifact output, and cross-PR memory adds integration complexity.

---

## INERTIA: STATUS QUO

| Current workaround | Sprint cost (hrs or $ estimate) | Risk if unchanged |
|--------------------|---------------------------------|-------------------|
| Ad-hoc paste-to-LLM + human PR review | ~28 hrs/sprint reviewer labor ($3,360/sprint at $120/hr for 5-dev team) | Bugs slip through without audit trail; same anti-patterns ship repeatedly; post-mortem coverage questions unanswerable |

Baseline: "Without this feature, the team spends approximately 28 hrs/sprint on human PR review with no structured AI augmentation and no cross-PR defect pattern tracking."

---

## PM: BUDGET

Available hours = 2 engineers x 40 hrs/sprint x 4 sprints = 320 hrs (conservative) to 480 hrs (if 3-sprint target met with buffer)

| Component | Estimated Hours |
|-----------|----------------|
| Skill prompt engineering (review-code skill body) | 60 |
| Reviewer persona system (stock roles + custom) | 40 |
| Artifact output pipeline (frontmatter, naming, storage) | 30 |
| Cross-PR pattern memory (topic-scoped finding aggregation) | 80 |
| Integration with git diff / PR context extraction | 50 |
| Quest loop (rubric, golden, scoring rounds) | 50 |
| Customer simulation testing (P-11) | 30 |
| **Total** | **340** |

Budget chain:
  Estimated: 340 hrs
  Available: 480 hrs (4 sprints, 2 engineers)
  Delta: +140 hrs buffer
  Flag: UNDER-BUDGET

---

## ARCHITECT: COMPLEXITY

| Component | Rating | Est. Hours | Rationale | Do-nothing cost (hrs/sprint) |
|-----------|--------|------------|-----------|------------------------------|
| Skill prompt engineering | GREEN | 60 | Well-understood pattern; 9+ skills already authored with quest loop | 28 (full human review time) |
| Reviewer persona system | GREEN | 40 | Stock role pattern established (P-05); existing persona infrastructure from techniques 04-07 | 28 |
| Artifact output pipeline | GREEN | 30 | Naming contract (P-07) and frontmatter (P-09) already defined; standard skill output | 28 |
| Cross-PR pattern memory | YELLOW | 80 | No existing skill reads prior artifacts at execution time (P-03 tension); requires design decision on how to aggregate findings without breaking self-containment | 28 |
| Git diff / PR context extraction | YELLOW | 50 | Requires interfacing with git CLI or GitHub API for diff extraction; platform-specific (Windows MSYS2); not yet done in any existing skill | 28 |
| Quest loop | GREEN | 50 | Established process; 20+ rounds typical for golden status | N/A |
| Customer simulation | GREEN | 30 | P-11 pattern established | N/A |

RED Blockers: No RED components.

YELLOW Caveats:
- **Cross-PR pattern memory**: This is the key architectural tension. P-03 (Self-Contained Skills) says "No skill depends on another skill's output file at execution time." Cross-PR pattern detection requires reading prior review artifacts. Resolution options: (a) make it an explicit opt-in mode (`--memory`), (b) implement as a separate synthesis skill (not the review skill itself), (c) define "reading your own prior artifacts" as within P-03 scope (a skill reading its own namespace's history, not another skill's output). Option (c) is the cleanest but requires a PRINCIPLES.md amendment.
- **Git diff extraction**: Platform-specific complexity. Must work on Windows (MSYS2/Git Bash), macOS, and Linux. Git CLI is universally available, but extracting structured diff context (file-level, hunk-level, with surrounding context) requires careful implementation. Lift condition: build a standalone diff extraction utility and test on 3 platforms before integrating.

---

## STRATEGY: BUILD-VS-BUY

| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| Skill prompt engineering | Build | Core competency; Signal's skill authoring is the product |
| Reviewer persona system | Build | Extends existing persona infrastructure |
| Artifact output pipeline | Use existing | Standard skill output pathway already built |
| Cross-PR pattern memory | Build (phased) | No existing tool provides topic-scoped review aggregation; build as opt-in Phase 2 after base review skill ships |
| Git diff extraction | Build | Simple git CLI wrapper; no third-party dependency warranted |

---

## VERDICT

Composite score: 72/100
Label: FEASIBLE WITH CAVEATS

Not building this means: "Teams continue spending ~28 hrs/sprint on unaided human review with no artifact trail, no cross-PR pattern detection, and no structured AI augmentation. Ongoing cost: ~$3,360/sprint ($87K/year) for a 5-dev team."

Prerequisites (YELLOW components must be addressed):
1. Resolve P-03 tension for cross-PR memory: decide whether to amend P-03, implement as separate synthesis skill, or ship base review without memory (Phase 1) and add memory later (Phase 2).
2. Build and test cross-platform diff extraction utility before sprint 2 integration milestone.

---

## AMENDMENTS

1. [Action for Cross-PR Pattern Memory (YELLOW)]: Ship Phase 1 without cross-PR memory. The base review skill produces a per-PR artifact. Phase 2 adds a `review-patterns` skill that reads prior `review-code` artifacts for the same topic and surfaces recurring findings. This avoids P-03 tension entirely -- the review skill remains self-contained; the patterns skill is a separate synthesis skill.
   Completing this moves Cross-PR Pattern Memory from YELLOW to GREEN (for Phase 1), raising score by approximately 10 pts.
   Inertia saved: 28 hrs/sprint (the base review skill already provides structured AI review, which is the primary inertia-breaking value).

2. [Action for Git Diff Extraction (YELLOW)]: Build a minimal `signal-diff` utility that wraps `git diff` with structured output (JSON: files changed, hunks, context lines). Test on Windows, macOS, Linux in CI. Estimate: 2 days.
   Completing this moves Git Diff Extraction from YELLOW to GREEN, raising score by approximately 8 pts.
   Inertia saved: 28 hrs/sprint (diff extraction is a prerequisite for the review skill to function at all).
