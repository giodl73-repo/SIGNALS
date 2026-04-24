# ai-simulation-techniques — Signal Strategy

## Rationale

Signal's technique set was assembled from codebase evidence — real artifacts from real projects. Before committing to a 9-technique taxonomy as the plugin's permanent structure, the team needs external validation: does the research literature and industry practice recognize these same techniques? The prove namespace is the right instrument here: websearch establishes the external vocabulary, hypothesis tests coverage completeness, and synthesize resolves gaps into a commit-ready verdict.

## Stakeholder Map

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---|---|---|---|
| S-01 | Plugin Architect | Ships a technique set that duplicates known space or misses significant techniques; Signal's credibility undermined when practitioners cite techniques Signal doesn't cover | Whether Signal's 9 techniques constitute a complete and defensible technique taxonomy worth building into the plugin |
| S-02 | Research Lead | Invests simulation effort in techniques that external literature doesn't validate; wastes effort or misses higher-leverage techniques not yet in Signal | Which techniques from external literature should be adopted, adapted, or noted as gaps in Signal's coverage |
| S-03 | Developer Advocate | Demos Signal to practitioners who ask "how does this compare to what others do?" — without evidence, the comparison is speculation | Whether Signal's technique set is presentable as a coherent, evidence-backed approach vs. ad-hoc accumulation |

## Signal Plan

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer -> Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|---|---|---|---|---|---|---|
| essential | prove | websearch | ai-simulation-techniques-websearch-2026-03-15.md | Research Lead -> Plugin Architect | S-01, S-02 | -> IR-01 |
| essential | prove | hypothesis | ai-simulation-techniques-hypothesis-2026-03-15.md | Research Lead -> Plugin Architect | S-01, S-02 | -> IR-01 |
| recommended | prove | synthesize | ai-simulation-techniques-synthesize-2026-03-15.md | Plugin Architect -> Developer Advocate | S-01, S-03 | -> IR-05 |

## Commit Gate

```
COMMIT GATE for ai-simulation-techniques
========================
Design commit is authorized when ALL of the following signals are present
in simulations/ai-simulation-techniques/:

REQUIRED (essential -- see COV-01):
  1. ai-simulation-techniques-websearch-2026-03-15.md
  2. ai-simulation-techniques-hypothesis-2026-03-15.md

PERMITTED AFTER COMMIT (recommended / optional):
  - ai-simulation-techniques-synthesize-2026-03-15.md

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```
