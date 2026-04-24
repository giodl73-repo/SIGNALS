## Scout-Risk — Round 7 Scoring

### V-01 — Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia mandatory and first | **PASS** | "Write the Inertia Risk entry first. This entry is required. It cannot be omitted... or placed after dimensional risks." |
| C-02 | Dimensional coverage ≥3 | **PASS** | "generate risks across at least five of these six dimensions" |
| C-03 | Risk anatomy complete | **PASS** | All five fields required (Label, Severity, Inertia condition, Mitigation, Status-quo description) |
| C-04 | Severity scale {HIGH,MEDIUM,LOW} | **PASS** | "Exactly one of: HIGH, MEDIUM, LOW — no other values" |
| C-05 | Mitigations specific | **PASS** | Prohibited-phrase scan + replace instruction; inertia mitigation must be "a named validation" |
| C-06 | Risks dimension-labeled | **PASS** | Dimension field required per entry with five-label vocabulary |
| C-07 | Likelihood beyond binary | **PASS** | "Name the condition or scenario that activates this risk — not 'possible' or 'unlikely'" |
| C-08 | Priority ordering | **PASS** | "List risks highest-severity-first within the dimensional register" |
| C-09 | Interdependencies noted | **PASS** | Dedicated Risk Interdependencies section, ≥2 pairs |
| C-10 | AMEND behavior | **PASS** | AMEND section retains inertia, applies to dimensional register, retains interdependency section |
| C-11 | Zero-generic mitigations | **PASS** | 6-phrase prohibition list + replace instruction |
| C-12 | All likelihoods trigger-qualified | **PASS** | All entries must name "the condition or scenario"; inertia has dedicated "Inertia condition" field |
| C-13 | Interdependencies in dedicated section | **PASS** | Labeled "Risk Interdependencies" section with ≥2 named pairs |
| C-14 | IF-THEN syntactic form | **FAIL** | No IF-THEN form required; likelihoods are condition/scenario prose only |
| C-15 | Mitigation type declared | **FAIL** | No type taxonomy; mitigations are untyped concrete actions |
| C-16 | Interdependency count ≥3 | **FAIL** | Requires "at least two" pairs only |
| C-17 | Severity-transition labels | **PASS** | "IF [Risk A] activates, [Risk B] escalates from [FROM severity] to [TO severity]" |
| C-18 | ≥3 distinct type classes | **FAIL** | No type taxonomy present |
| C-19 | Enumerated forbidden phrases ≥3 | **PASS** | 6 phrases named: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "watch for issues" |
| C-20 | Count failure → upstream revision | **FAIL** | No repair loops; interdependency section has no self-healing |
| C-21 | Repair-loop count matches gates | **FAIL** | No repair loops |
| C-22 | Severity-transition columns type-constrained | **FAIL** | Prose interdependency section; no typed columns |
| C-23 | Repair loops named with unique labels | **FAIL** | No repair loops |
| C-24 | Complete 6-class taxonomy pre-defined | **FAIL** | No taxonomy defined |
| C-25 | Diversity audit in dedicated step | **FAIL** | No diversity audit step |

**V-01: 60 + 30 + 14 = 104** (Golden)

---

### V-02 — Typed-Column Tables

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia mandatory and first | **PASS** | Section 1 required, INERTIA-01 fixed; "An AMEND directive does not remove it" |
| C-02 | Dimensional coverage | **PASS** | "at least seven risk entries covering at least five of" five dimensions |
| C-03 | Risk anatomy complete | **PASS** | Severity, Likelihood, Mitigation columns all required with constraints |
| C-04 | Severity scale | **PASS** | Cell-level: "Must be exactly one of: HIGH \| MEDIUM \| LOW" |
| C-05 | Mitigations specific | **PASS** | 4-phrase prohibition in Content Standards + typed format required |
| C-06 | Dimension-labeled | **PASS** | Cell constraint: "Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline" |
| C-07 | Likelihood beyond binary | **PASS** | "Name the condition or scenario — not a bare label like 'possible'" |
| C-08 | Priority ordering | **PASS** | "Row order: HIGH rows first, then MEDIUM, then LOW" |
| C-09 | Interdependencies noted | **PASS** | Section 3 interdependency table, ≥2 rows |
| C-10 | AMEND behavior | **PASS** | AMEND section retains Section 1 (inertia), vocabulary constraints remain in force |
| C-11 | Zero-generic mitigations | **PASS** | "No prohibited phrases... are forbidden; replace with a typed concrete action" |
| C-12 | All likelihoods trigger-qualified | **PASS** | Both sections require naming conditions/scenarios for all rows |
| C-13 | Dedicated interdependency section | **PASS** | Labeled "Section 3 — Risk Interdependencies" table, ≥2 named pairs by Risk-ID |
| C-14 | IF-THEN syntactic form | **FAIL** | No IF-THEN form required in likelihood cells |
| C-15 | Mitigation type declared | **PASS** | All 6 classes defined in Reference block; "[Type-Class]: [Sub-field values] — [concrete action]" format enforced |
| C-16 | Interdependency count ≥3 | **FAIL** | Section 3 requires "at least two rows" only |
| C-17 | Severity-transition labels | **PASS** | From-Severity and To-Severity columns with "current severity before" / "escalated severity when" semantics |
| C-18 | ≥3 distinct type classes | **PASS** | "Use at least 3 distinct Type-Class labels across Section 1 and Section 2 combined" |
| C-19 | Enumerated forbidden phrases ≥3 | **PASS** | 4 phrases named: "monitor closely", "keep an eye on", "revisit later", "consider alternatives" |
| C-20 | Count failure → upstream revision | **FAIL** | No repair loops; Section 3 says "produce at least two rows" with no self-healing |
| C-21 | Repair-loop count matches gates | **FAIL** | No repair loops |
| C-22 | Severity-transition columns type-constrained | **PASS** | "From-Severity and To-Severity: each must contain exactly one of {HIGH, MEDIUM, LOW}" as explicit column rule |
| C-23 | Repair loops named | **FAIL** | No repair loops |
| C-24 | Complete 6-class taxonomy pre-defined | **PASS** | "Reference: Mitigation Type Taxonomy" block before any section defines all 6 classes with sub-fields |
| C-25 | Diversity audit in dedicated step | **FAIL** | Type diversity mentioned in Content Standards but no isolated phase |

**V-02: 60 + 30 + 22 = 112** (Golden)

---

### V-03 — Named Phases + Named Repair Loops

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia mandatory and first | **PASS** | "Phase 1 — Generate Inertia Risk (Required)... No AMEND directive removes it." |
| C-02 | Dimensional coverage | **PASS** | Phase 2: "at least seven risks covering at least five of these dimensions" |
| C-03 | Risk anatomy complete | **PASS** | Phase 1 and 2 fields all required (Severity, Likelihood, Mitigation, Type-Class) |
| C-04 | Severity scale | **PASS** | "Severity: exactly one of HIGH, MEDIUM, LOW" in both phases |
| C-05 | Mitigations specific | **PASS** | Phase 2a scans 6 prohibited phrases + Repair Loop A requires replacement |
| C-06 | Dimension-labeled | **PASS** | "Dimension: one label from the list above" per entry |
| C-07 | Likelihood beyond binary | **PASS** | "name the condition or scenario that activates this risk" for all entries |
| C-08 | Priority ordering | **PASS** | "Order entries highest-severity-first" |
| C-09 | Interdependencies noted | **PASS** | Phase 3: "at least three pairs" with naming required |
| C-10 | AMEND behavior | **PASS** | AMEND retains Phase 1, Phase 2b, Phase 4, all three repair loops |
| C-11 | Zero-generic mitigations | **PASS** | Phase 2a terminates only "when a full scan finds zero prohibited phrases" |
| C-12 | All likelihoods trigger-qualified | **PASS** | All entries require "name the condition or scenario"; inertia has explicit named-scenario instruction |
| C-13 | Dedicated interdependency section | **PASS** | Phase 3 labeled section, ≥3 named pairs by phase label + descriptor |
| C-14 | IF-THEN syntactic form | **FAIL** | No IF-THEN syntax required; likelihood is condition/scenario prose |
| C-15 | Mitigation type declared | **PARTIAL** | Taxonomy defined with 6 classes; Type-Class field required; but sub-field inclusion in mitigation text not explicitly enforced ("a concrete action typed against the taxonomy") |
| C-16 | Interdependency count ≥3 | **PASS** | Phase 3 requires "at least three pairs"; Phase 4 gate enforces it |
| C-17 | Severity-transition labels | **PASS** | "IF [Risk A] activates, [Risk B] escalates from [FROM severity] to [TO severity]" |
| C-18 | ≥3 distinct type classes | **PASS** | Phase 2b counts distinct Type-Class labels; Repair Loop B triggers if <3 |
| C-19 | Enumerated forbidden phrases ≥3 | **PASS** | 6 phrases named in Phase 2a |
| C-20 | Count failure → upstream revision | **PASS** | Phase 4: "Return to Phase 2 and add or refine entries"; Phase 2b: "Return to Phase 2 and revise mitigations" |
| C-21 | Repair-loop count matches gates | **PASS** | 3 gates (Phase 2a, Phase 2b, Phase 4) → 3 loops (A, B, C) |
| C-22 | Severity-transition columns type-constrained | **FAIL** | Prose interdependency section; no typed-column vocabulary constraints on From/To severity |
| C-23 | Repair loops named | **PASS** | "Repair Loop A", "Repair Loop B", "Repair Loop C" with unique labels |
| C-24 | Complete 6-class taxonomy pre-defined | **PARTIAL** | All 6 classes defined with sub-fields inside Phase 2 — not as a standalone pre-phase reference block before Phase 1 |
| C-25 | Diversity audit in dedicated step | **PASS** | "Phase 2b is a standalone audit step — do not merge it with Phase 2" |

**V-03: 60 + 30 + 28 = 118** (Golden)

---

### V-04 — V-02 + V-03 (Typed Tables + Named Phases + Named Loops)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia mandatory and first | **PASS** | Phase 1 required, INERTIA-01 fixed, "Cannot Be Amended Away" |
| C-02 | Dimensional coverage | **PASS** | Phase 2: ≥7 entries, ≥5 dimensions |
| C-03 | Risk anatomy complete | **PASS** | All columns required with constraints across Phase 1 and Phase 2 |
| C-04 | Severity scale | **PASS** | Cell-level: "Must be exactly one of: HIGH \| MEDIUM \| LOW" in both phases |
| C-05 | Mitigations specific | **PASS** | Phase 2a + Repair Loop A; 7 prohibited phrases enumerated |
| C-06 | Dimension-labeled | **PASS** | "Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline" |
| C-07 | Likelihood beyond binary | **PASS** | "IF [named condition], THEN [this risk activates]" — IF-THEN enforced, satisfies C-07 and C-14 |
| C-08 | Priority ordering | **PASS** | "Row order: HIGH rows first, then MEDIUM, then LOW" |
| C-09 | Interdependencies noted | **PASS** | Phase 3 table, ≥3 rows required |
| C-10 | AMEND behavior | **PASS** | AMEND retains Phase 1, Phase 2b, Phase 4, all three loops, all vocabulary constraints |
| C-11 | Zero-generic mitigations | **PASS** | Phase 2a terminates only when full scan finds zero prohibited phrases |
| C-12 | All likelihoods trigger-qualified | **PASS** | IF-THEN form required; "bare labels are violations" |
| C-13 | Dedicated interdependency section | **PASS** | Phase 3 table, ≥3 named pairs by Risk-ID |
| C-14 | IF-THEN syntactic form | **PASS** | "Likelihood: IF-THEN form required — bare labels ('possible,' 'likely,' 'high') are violations" enforced in all cells |
| C-15 | Mitigation type declared | **PASS** | Pre-phase reference taxonomy; mitigation format "[Type-Class]: [Sub-fields] — [concrete action]" explicitly required |
| C-16 | Interdependency count ≥3 | **PASS** | Phase 3: "Produce at least 3 rows"; Phase 4 gate + Repair Loop C |
| C-17 | Severity-transition labels | **PASS** | From-Severity / To-Severity columns with before/after semantics |
| C-18 | ≥3 distinct type classes | **PASS** | Phase 2b + Repair Loop B enforces minimum 3 distinct labels |
| C-19 | Enumerated forbidden phrases ≥3 | **PASS** | 7 phrases named in Phase 2a |
| C-20 | Count failure → upstream revision | **PASS** | Phase 4 → Repair Loop C returns to Phase 2; Phase 2b → Repair Loop B returns to Phase 2 |
| C-21 | Repair-loop count matches gates | **PASS** | 3 gates → 3 named loops (A, B, C) |
| C-22 | Severity-transition columns type-constrained | **PASS** | Phase 3: "From-Severity and To-Severity: each must contain exactly one of {HIGH, MEDIUM, LOW}" as explicit column rule |
| C-23 | Repair loops named | **PASS** | "Repair Loop A", "Repair Loop B", "Repair Loop C" |
| C-24 | Complete 6-class taxonomy pre-defined | **PASS** | "Reference: Mitigation Type Taxonomy (Pre-defined, Closed)" block before Phase 1; all 6 classes with sub-fields |
| C-25 | Diversity audit in dedicated step | **PASS** | "Phase 2b is distinct from Phase 2 — do not merge them" |

**V-04: 60 + 30 + 34 = 124** (Golden — Maximum)

---

### V-05 — Maximum Coverage (All Axes)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia mandatory and first | **PASS** | Phase 1 required + Status-quo column added; "AMEND does not remove it" |
| C-02 | Dimensional coverage | **PASS** | "at least seven risks covering at least five of these six dimensions" |
| C-03 | Risk anatomy complete | **PASS** | All columns with cell constraints across Phase 1 and Phase 2 |
| C-04 | Severity scale | **PASS** | Cell-level vocabulary constraint in all phases |
| C-05 | Mitigations specific | **PASS** | Phase 2a + Repair Loop A; 7-phrase enumerated prohibition |
| C-06 | Dimension-labeled | **PASS** | Cell constraint with exact vocabulary |
| C-07 | Likelihood beyond binary | **PASS** | IF-THEN form enforced in all cells, both phases |
| C-08 | Priority ordering | **PASS** | HIGH first, then MEDIUM, then LOW |
| C-09 | Interdependencies noted | **PASS** | Phase 3 table, ≥3 rows |
| C-10 | AMEND behavior | **PASS** | AMEND section names each preserved phase with its invariant: Phase 2b "must still use ≥3 distinct Type-Class labels"; Phase 4 "must still produce ≥3 pairs, or Repair Loop C activates" |
| C-11 | Zero-generic mitigations | **PASS** | Phase 2a terminates only at zero prohibited phrases |
| C-12 | All likelihoods trigger-qualified | **PASS** | Phase 1: "Must use IF-THEN form: IF [named status-quo condition holds]"; Phase 2: "bare labels are violations" |
| C-13 | Dedicated interdependency section | **PASS** | Phase 3 table, ≥3 named pairs by Risk-ID |
| C-14 | IF-THEN syntactic form | **PASS** | Both phases: "Must use IF-THEN form" as cell constraint; bare probability labels are violations |
| C-15 | Mitigation type declared | **PASS** | Complete pre-phase reference taxonomy; "[Type-Class]: [Sub-field values] — [concrete action]" enforced in both phases |
| C-16 | Interdependency count ≥3 | **PASS** | Phase 4 gate + Repair Loop C |
| C-17 | Severity-transition labels | **PASS** | From-Severity / To-Severity columns with before/after semantics |
| C-18 | ≥3 distinct type classes | **PASS** | Phase 2b gate + Repair Loop B |
| C-19 | Enumerated forbidden phrases ≥3 | **PASS** | 7 phrases enumerated by number in Phase 2a |
| C-20 | Count failure → upstream revision | **PASS** | Both count gates name the upstream step to return to |
| C-21 | Repair-loop count matches gates | **PASS** | 3 gates → Repair Loop A, B, C |
| C-22 | Severity-transition columns type-constrained | **PASS** | "each must contain exactly one of {HIGH, MEDIUM, LOW} — no other values, no compound entries, no prose labels" |
| C-23 | Repair loops named | **PASS** | Repair Loop A, B, C with unique labels |
| C-24 | Complete 6-class taxonomy pre-defined | **PASS** | "Reference: Mitigation Type Taxonomy (Complete — 6 Classes, Closed)" before Phase 1; expanded definitions including "A Spike requires a named unknown... and a time-box" |
| C-25 | Diversity audit in dedicated step | **PASS** | "Phase 2b is a standalone audit step — do not merge it with Phase 2 or Phase 2a" |

**V-05: 60 + 30 + 34 = 124** (Golden — Maximum)

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Status |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 60 | 30 | 14 | **104** | Golden |
| V-02 | 60 | 30 | 22 | **112** | Golden |
| V-03 | 60 | 30 | 28 | **118** | Golden |
| V-04 | 60 | 30 | 34 | **124** | Golden — Maximum |
| V-05 | 60 | 30 | 34 | **124** | Golden — Maximum |

V-04 and V-05 tie at maximum composite. V-03 fails only C-14 (IF-THEN syntax), C-22 (typed severity columns), and receives PARTIAL on C-15/C-24 for taxonomy placement. V-01 is strong on inertia framing but lacks the entire type-taxonomy and repair-loop infrastructure.

---

## Excellence Signals

**Both top variations score 124.** V-05 adds two structural patterns not yet captured by any rubric criterion:

**Pattern 1 — Repair loop revision ordering.** V-05's Repair Loop B specifies *where* to start revisions: "Change mitigations in LOW or MEDIUM entries first to minimize severity disruption." No criterion captures repair sequencing priority — only that a loop exists (C-23) and triggers on a count miss (C-21). This is an efficiency escalation: a named repair loop that starts at the lowest-impact entries is less likely to destabilize HIGH-severity rows as collateral.

**Pattern 2 — Inertia entry carries a dedicated Status-quo column.** V-05 Phase 1 adds a `Status-quo` column ("One sentence naming what the user does today without this feature and how well it serves them") as a structurally separate field from Likelihood. C-01 requires inertia to be first and required; it says nothing about decomposing the inertia entry into named sub-fields. The Status-quo field forces the model to characterize the competitor before stating the activation condition — separating *what exists today* from *when it beats the new feature*. This is a first-class competitor-profile pattern with no criterion to match it.

---

```json
{"top_score": 124, "all_essential_pass": true, "new_patterns": ["Repair loop revision ordering — when a repair loop triggers, the prompt specifies which entries to revise first (LOW/MEDIUM before HIGH) to minimize severity disruption as collateral", "Inertia entry carries a dedicated Status-quo column separate from Likelihood — forces characterization of what the user does today before stating the activation condition, treating inertia as a first-class named competitor"]}
```
