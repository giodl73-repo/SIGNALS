v3 written. Here is the complete updated rubric:

---

```
---
skill: quest-rubric
skill_target: campaign-track
date: 2026-03-16
version: 3
---
```

# Scoring Rubric: campaign-track

**Skill description**: Run the full topic narrative campaign. Orchestrates: topic-new (register), topic-roadmap (plan signals), topic-status (current coverage), topic-story (narrative synthesis). Output: complete topic dashboard showing what signals exist, what is missing, and the narrative arc. Use at the start and end of a signal-gathering session.

---

## Essential Criteria

**C-01 -- Orchestration sequence** | essential | correctness
All four sub-skills invoked in order. Pass: explicit phase trace with distinct artifact per phase.

**C-02 -- Topic registration artifact** | essential | correctness
strategy.md with >= 3 planned signals, namespace, and priority. Pass: strategy artifact present with namespace/priority fields.

**C-03 -- Coverage delta display** | essential | coverage
9-namespace coverage table: planned / collected / missing, named gaps. Pass: table present with named namespace/skill gap entries.

**C-04 -- Narrative synthesis present** | essential | depth
Verdict verb from controlled vocabulary + hypothesis mutation block. Pass: verdict verb + at least one S0 mutation entry.

**C-05 -- Session-bookend utility** | essential | behavior
Handles both empty (0 signals) and populated state. Pass: zero-signal case runs topic-story with NOT YET REACHED verdict; populated case reflects signals.

---

## Recommended Criteria

**C-06 -- Actionable next-signal recommendations** | recommended | depth
Top-3 next signals, each with namespace/skill + gap reason.

**C-07 -- Coverage ratio and readiness statement** | recommended | format
Numeric ratio (X/N) + labeled readiness verdict (READY / NOT READY / CONDITIONALLY READY).

**C-08 -- Cross-namespace signal balance** | recommended | coverage
Per-namespace breakdown; zero-signal namespaces flagged explicitly.

---

## Aspirational Criteria

**C-09 -- Echo integration** | aspirational | depth
Unexpected findings called out distinctly from planned coverage. Pass: at least one explicit echo entry with "if none: NONE" fallback.

**C-10 -- Dual-session delta** | aspirational | behavior
Session delta section: signals added, verdict change summary.

**C-11 -- Role-gated phases** *(from R1 V-01)* | aspirational | correctness
Each phase assigns a distinct named AI persona (Registrar / Planner / Analyst / Narrator). Pass: four distinct role labels, consistent assignment -- Registrar does not synthesize, Narrator does not plan. Generic "Assistant" labels fail.

**C-12 -- Explicit progression gates** *(from R1 V-01)* | aspirational | behavior
Phase ordering enforced as a hard constraint via "do not proceed until [artifact X] is written" gates. Pass: at least one explicit gate statement between adjacent phases. A bare numbered list with no gating language fails.

**C-13 -- Empty-state as named section** *(from R1 V-01)* | aspirational | behavior
Zero-signal first-invocation documented as a dedicated labeled section addressing each phase individually. Pass: distinct section present with per-phase behavior. A single buried sentence fails.

**C-14 -- Per-role prohibition lists** *(new, from R2 V-01)* | aspirational | correctness
Each assigned persona carries an explicit enumerated list of disallowed behaviors -- named forbidden actions, not just a role description. Pass: at least two roles with one or more named prohibited actions each. Implicit prohibition inferred from role title alone fails.

**C-15 -- Typed output contracts per phase** *(new, from R2 V-04)* | aspirational | format
Each phase's output artifact specifies exact value types or format contracts: cell values typed as integers, verdict fields typed as one of an enumerated set, required fields named. Pass: at least two phases with typed output specifications. Narrative descriptions without type/value constraints fail.

**C-16 -- Terminal completion checklist** *(new, from R2 V-05)* | aspirational | behavior
An end-to-end verification step after Phase 4: a named checklist confirming all four phase postconditions satisfied before the result is marked complete. Pass: explicit TERMINAL or completion checklist section present listing all four phases. Implicit completion assumption fails.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60 pts | C-01 through C-05 (5 criteria) |
| Recommended | 30 pts | C-06, C-07, C-08 (3 criteria) |
| Aspirational | 10 pts | C-09 through C-16 (8 criteria) |

**Golden threshold**: All 5 essential pass AND composite >= 80.

**Minimum viable output**: C-01 + C-03 + C-04 must all pass.

---

## What changed from v2

Three new aspirational criteria, denominator 5 → 8:

- **C-14** captures V-01's prohibition-list mechanism — the difference between "don't cross roles" as intent vs. "here is the enumerated list of what you cannot do" as contract.
- **C-15** captures V-04's typed output innovation — fixed cell types prevent the under-specified template failure that surfaced in R1.
- **C-16** captures V-05's TERMINAL checklist — an end-to-end gate after Phase 4, distinct from the between-phase gates in C-12.

V-01's R2 score under v3: still 100 (passes C-14, C-15 inferred from fixed template, C-16 inferred from full completion section). The practical effect is that C-13 is no longer the ceiling — C-16 is now the next hard boundary to crack.
