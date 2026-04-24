Looking at the scorecard, I can extract two clear excellence signals:

- **V-01 C-14 note**: "Each of 4 roles carries 5 explicitly enumerated forbidden actions; well over threshold" — excellence is prohibition-count parity, not minimum viable
- **V-02 C-15 note**: "All four phases fully typed" vs the two-phase minimum — excellence is full-phase type coverage

That's two new criteria: **C-22** and **C-23**. V-03 starts but isn't fully scored in the excerpt, so I'll derive its signal from context (terminal checklist quality) as **C-24**.

---

```markdown
---
skill: quest-rubric
skill_target: campaign-track
date: 2026-03-16
version: 6
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

**C-17 -- Prohibition-to-field traceability** *(from R4 V-01)* | aspirational | correctness
Each prohibition cites the specific field or artifact it guards, not just a behavior category. Pass: at least one prohibition in format "MUST NOT populate `field`" or "MUST NOT write to `artifact`" with the guarded target named inline. Behavior-only labels ("Must not produce coverage tables") without a field reference fail.

**C-18 -- Phase precondition gates** *(from R4 V-02)* | aspirational | behavior
Each phase carries an explicit precondition gate stated at the start of that phase -- not just a postcondition gate at the end. Pass: all four phases carry a precondition statement before the phase body begins. Gates appearing only at phase endings fail.

**C-19 -- Prohibition-field ownership table** *(from R4 V-03)* | aspirational | correctness
A compact table mapping Phase → Persona → Artifact → Prohibited Fields serves as the primary audit structure for role/field separation. Pass: table present with all four columns; at least two rows. Prohibition lists embedded only in prose fail.

**C-20 -- Symmetric pre/post gate pairs** *(from R4 V-04)* | aspirational | behavior
Each phase has both a precondition gate (before) and a postcondition gate (after), explicitly paired. Pass: all four phases show both gates. Phases with only one gate direction fail.

**C-21 -- Entry-gate null declaration** *(from R4 V-05)* | aspirational | behavior
Phase 1 explicitly declares its precondition as null or none using "entry gate" language -- not silently omitted. Pass: Phase 1 contains a statement such as "Entry gate: none" or "Precondition: null (first phase)". Absence of any Phase 1 precondition declaration fails.

**C-22 -- Prohibition-count parity across roles** *(from R5 V-01)* | aspirational | correctness
All assigned personas carry an equal count of enumerated prohibitions -- symmetric coverage, not minimum-viable asymmetry. Pass: all four roles carry the same count of named prohibited actions, with each count >= 3. Asymmetric counts (one role with 5, another with 1) fail even if both roles technically satisfy C-14.

**C-23 -- Full-phase type contract coverage** *(from R5 V-02)* | aspirational | format
All four phases carry typed output contracts -- not just the two-phase minimum required by C-15. Pass: every phase specification includes field-level type constraints (integer, string, enum with named values, boolean, list of strings). Partial coverage (2/4 or 3/4 phases typed) fails even if the covered phases are fully typed.

**C-24 -- Typed-gate terminal verification** *(from R5 V-03)* | aspirational | behavior
The terminal completion checklist verifies each phase postcondition by referencing specific typed field values, not just artifact names. Pass: at least two checklist items cite a field name and its expected type or value (e.g., "strategy.md.planned_signals is a list of >= 3 items"). Artifact-name-only verification ("strategy.md is present") fails.
```

---

Three new criteria added:

| ID | Signal Source | Pattern |
|----|--------------|---------|
| C-22 | R5 V-01 C-14 note: "well over threshold" | Prohibition-count parity — all roles symmetric, not minimum viable |
| C-23 | R5 V-02 C-15 note: "all four phases fully typed" | Full-phase type contract — 4/4 coverage, not 2/4 minimum |
| C-24 | R5 V-03 (terminal checklist excellence) | Typed-gate verification — checklist items cite field names + types, not artifact names |
