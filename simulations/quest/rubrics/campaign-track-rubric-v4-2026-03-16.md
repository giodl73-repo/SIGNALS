Looking at the Round 3 scorecard, V-04 is the key signal: combining C-14 (prohibitions) + C-15 (typed contracts) together reveals a new pattern — the two dimensions should *reference each other* (prohibitions guarding named output fields). And the symmetric gap C-16 pointed to a pre-condition counterpart. Two new criteria emerge:

- **C-17**: Prohibition-to-field traceability (from V-04 combination signal)
- **C-18**: Phase precondition gates (symmetric with C-16 postconditions)

---

```markdown
---
skill: quest-rubric
skill_target: campaign-track
date: 2026-03-16
version: 4
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

**C-14 -- Per-role prohibition lists** *(from R2 V-01)* | aspirational | correctness
Each assigned persona carries an explicit enumerated list of disallowed behaviors -- named forbidden actions, not just a role description. Pass: at least two roles with one or more named prohibited actions each. Implicit prohibition inferred from role title alone fails.

**C-15 -- Typed output contracts per phase** *(from R2 V-04)* | aspirational | format
Each phase's output artifact specifies exact value types or format contracts: cell values typed as integers, verdict fields typed as one of an enumerated set, required fields named. Pass: at least two phases with typed output specifications. Narrative descriptions without type/value constraints fail.

**C-16 -- Terminal completion checklist** *(from R2 V-05)* | aspirational | behavior
An end-to-end verification step after Phase 4: a named checklist confirming all four phase postconditions satisfied before the result is marked complete. Pass: explicit TERMINAL or completion checklist section present listing all four phases. Implicit completion assumption fails.

**C-17 -- Prohibition-to-field traceability** *(new, from R3 V-04)* | aspirational | correctness
Each role's prohibited actions trace to the specific output fields or artifact sections they guard -- forbidden verbs name the field that would be corrupted. Pass: at least one prohibition per role explicitly references a named output field or artifact section. Role-level prohibitions stated without any field reference fail. Generic "do not synthesize" with no named target fails.

**C-18 -- Phase precondition gates** *(new, from R3 V-04)* | aspirational | behavior
Each phase names its entry precondition -- the specific artifact or boolean state that must exist before the phase can begin. Symmetric with C-16's postconditions: C-16 checks exit, C-18 checks entry. Pass: at least two phases carry explicit named preconditions (e.g., "Phase 2 requires strategy.md from Phase 1 with namespace field populated"). Bare sequencing (Step 1, Step 2) or "proceeds naturally from prior output" fails.

---

## Scoring Formula

| Tier | Criteria | Points Each | Max |
|------|----------|-------------|-----|
| Essential | C-01..C-05 | 10 | 50 |
| Recommended | C-06..C-08 | 5 | 15 |
| Aspirational | C-09..C-18 | 4 | 40 |
| **Total** | | | **105** |

Scores normalized to 100 (×100/105). PASS = full points. PARTIAL = half. FAIL = 0.
