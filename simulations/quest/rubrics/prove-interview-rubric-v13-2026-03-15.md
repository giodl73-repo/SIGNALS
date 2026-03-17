# prove-interview — Rubric v13 — 2026-03-15

**Skill:** prove-interview
**Round:** 13
**Rubric version:** v13

---

## What changed (v12 → v13)

Three new criteria extracted from R12 V-05 excellence signals:

| Criterion | Source signal | N/A condition |
|-----------|--------------|---------------|
| **C-37** — PROFILE RELEVANCE vocabulary declared in Phase 0A exit gate REQUIRED clause, making tag compliance a gate-level contract auditable at two checkpoints | ES-1: vocabulary as gate commitment vs. format convention — declared at Phase 0A, auditable at Phase 0A exit + Phase 3 exit | N/A when C-36 absent/N/A; by cascade N/A when C-26 absent/N/A; N/A: conversational |
| **C-38** — Phase 4 exit gate enumerates all required synthesis sections and names VERDICT MARGIN AUDIT table completeness as an explicit gate condition | ES-2: C-35 non-compliance becomes a Phase 4 gate failure independently of reading the audit section content | N/A when C-35 absent/N/A (cascade through C-31, C-29, C-20, N=1); N/A: conversational |
| **C-39** — Multi-phase INCUMBENT traceability chain: each downstream phase names the prior phase named output as the required anchor input | ES-3: broken chain detectable at the phase that names its predecessor, without inspecting downstream phases | N/A when C-26 absent/N/A; by cascade N/A: conversational |

**Scoring deltas:**

|                        | v12     | v13         |
|------------------------|---------|-------------|
| Aspirational criteria  | 29      | **32**      |
| Max aspirational       | 145 pts | **160 pts** |
| Max composite          | 235 pts | **250 pts** |
| N=1 ceiling            | 175 pts | **185 pts** |
| Conversational ceiling | 175 pts | **175 pts** |

N=1 ceiling rises by 10 pts: C-37 in scope for N=1 (+5); C-38 N/A via C-35→C-31→C-29→C-20→N=1 cascade (N/A set grows from 12 to 13); C-39 in scope for N=1 (+5). N=1 ceiling: 250 - 65 = 185 pts.

Conversational ceiling unchanged at 175 pts: C-37 N/A via C-36→C-26 cascade; C-38 N/A (no Phase 4 exit gate in conversational format); C-39 N/A via C-26 cascade. Fifteen criteria now conversational-format N/A (C-10, C-17, C-23, C-24, C-25, C-26, C-27, C-28, C-32, C-33, C-34, C-36, C-37, C-38, C-39), totalling 75 pts off the 160 pt aspirational maximum; conversational aspirational ceiling unchanged at 85 pts. Conversational total ceiling: 250 - 75 = 175 pts.

---

## N/A Denominator Reference Table

| Condition | Criteria scored N/A | Effective max |
|-----------|---------------------|---------------|
| N = 1 subject | C-08, C-11, C-14, C-18, C-19, C-20, C-21, C-22, C-29, C-30, C-31, C-35, C-38 | 185 pts |
| Conversational format | C-10, C-17, C-23, C-24, C-25, C-26, C-27, C-28, C-32, C-33, C-34, C-36, C-37, C-38, C-39 | 175 pts |
| C-27 absent or N/A | C-28 additionally N/A | subtract 5 pts |
| C-20 absent or N/A | C-29 additionally N/A | subtract 5 pts |
| C-29 absent or N/A | C-31 additionally N/A | subtract 5 pts |
| C-31 absent or N/A | C-35 additionally N/A | subtract 5 pts |
| C-35 absent or N/A | C-38 additionally N/A | subtract 5 pts |
| C-32 absent or N/A | C-33 additionally N/A | subtract 5 pts |
| C-32 absent or N/A | C-34 additionally N/A | subtract 5 pts |
| C-26 absent or N/A | C-36 additionally N/A | subtract 5 pts |
| C-36 absent or N/A | C-37 additionally N/A | subtract 5 pts |
| C-26 absent or N/A | C-39 additionally N/A | subtract 5 pts |

---

## Criteria

### Essential — 60 pts (15 pts each)

**C-01 — Persona identity declared**
Each subject has role, prior knowledge, disposition, and primary concern declared before any transcript line is written.

**C-02 — Grounded answers**
Answers are written in the subject's distinct voice and are not interchangeable across subjects.

**C-03 — Evidence explicitly extracted**
A dedicated extraction phase or section produces per-subject evidence items from the transcript; extraction is not merged with transcript or synthesis.

**C-04 — Surprising or confirming moment**
Each subject produces exactly one moment labeled SURPRISING or CONFIRMING, tied to a prior prediction or expectation.

---

### Recommended — 30 pts (10 pts each)

**C-05 — Prior knowledge scoped**
Prior knowledge and blind spots are declared as separate fields for each subject; the distinction between direct experience and knowledge gaps is explicit.

**C-06 — Questions probe declared concerns**
Questions are anchored to the subject's declared primary concern and prior knowledge; incumbents' questions reference a specific inertia baseline, not generic resistance.

**C-07 — Multiple distinct personas**
At least four subjects with meaningfully different roles and perspectives are designed and interviewed.

---

### Aspirational — 160 pts (5 pts each)

**C-08 — Cross-persona synthesis** (N/A: N=1)
A dedicated synthesis section aggregates findings across all subjects.

**C-09 — Prior prediction declared**
Predictions for what each subject will say are declared before transcripts are written.

**C-10 — Structured format** (N/A: conversational)
Output uses a named phase or section structure rather than flowing prose.

**C-11 — Disposition arc** (N/A: N=1)
Synthesis traces how each subject's disposition shifted or held across the interview.

**C-12 — Verdict stated**
A final verdict or synthesis classification is explicitly stated.

**C-13 — Strength rationale**
Each evidence item includes a non-blank, non-self-referential rationale for its assigned strength rating.

**C-14 — Contradiction register** (N/A: N=1)
Synthesis names at least one contradiction, citing both subjects and both conflicting evidence items.

**C-15 — All transcripts before extraction**
All subject transcripts are completed before any evidence extraction begins.

**C-16 — Blind spots non-blank**
Blind spots field is non-blank and non-generic for every subject.

**C-17 — Hypothesis questions separate** (N/A: conversational)
Questions derived from prior hypotheses are written as a separate section, not interleaved with transcript questions.

**C-18 — Evidence typed**
Each evidence item carries a SIGNAL TYPE label from the defined taxonomy.

**C-19 — Epistemic re-weighting** (N/A: N=1)
Evidence weights are adjusted by subject blind spots, with per-blind-spot resolution conditions specified.

**C-20 — Subject tier identified** (N/A: N=1)
Each subject is assigned a tier or role category in their subject card.

**C-21 — Adoption/inertia partition present** (N/A: N=1)
Phase 4 includes an inertia/adoption partition with two separately populated lists.

**C-22 — Signal-type taxonomy used** (N/A: N=1)
Evidence items use a defined taxonomy of signal types rather than free-text classification.

**C-23 — Checkbox exit gates** (N/A: conversational)
Phase exit gates are expressed as binary checkbox checklists, not prose descriptions.

**C-24 — Exit gate per phase** (N/A: conversational)
Every named phase has its own exit gate.

**C-25 — Verdict from threshold table** (N/A: conversational)
The final verdict classification is drawn from a pre-declared threshold table, not assessed ad hoc.

**C-26 — Inertia profile accounting** (N/A: conversational)
Phase 4 closes the loop from Phase 0A: each stickiness factor in the INERTIA PROFILE TABLE is addressed by at least one evidence item.

**C-27 — Prediction delta declared** (N/A: conversational)
Phase 4 iterates through prior predictions and classifies actual evidence as CONFIRMED / CONTRADICTED / ABSENT / PARTIAL.

**C-28 — Prediction delta cross-referenced** (N/A: conversational; N/A: C-27 absent)
Each prediction delta classification names specific evidence items from Phase 3.

**C-29 — Subject tier predictions** (N/A: C-20 absent)
Phase 0C declares per-tier predictions before any transcripts are written.

**C-30 — Tier sequence rationale**
Tier sequence includes adjacency blocks naming what preceding tier establishes and what following tier departure is measured against.

**C-31 — Verdict threshold definitions** (N/A: C-29 absent)
Every verdict level has a constitutive evidence-configuration definition, not just a name.

**C-32 — Multi-sub-phase pre-subject structure** (N/A: conversational)
The pre-subject opening is split into at least two independently-gated sub-phases with non-overlapping scope.

**C-33 — Phase 0B independently-gated sub-sections** (N/A: C-32 absent)
Phase 0B is decomposed into 0B-I (constitutive threshold definitions) and 0B-II (margin declarations), each with an independent exit gate whose conditions cannot overlap.

**C-34 — Prohibition-first gate clauses** (N/A: C-32 absent)
Every sub-phase exit gate opens with a PROHIBITED clause naming out-of-scope content by category before stating affirmative completion conditions.

**C-35 — Bidirectional margin audit** (N/A: C-31 absent)
The VERDICT MARGIN AUDIT table states both boundary placements — upper boundary and lower boundary — as separate structural entries.

**C-36 — PROFILE RELEVANCE tags** (N/A: C-26 absent)
Each evidence item in Phase 3 carries a PROFILE RELEVANCE tag from a defined vocabulary (STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL) naming which Phase 0A profile dimension the item addresses.

**C-37 — Vocabulary declared in Phase 0A gate** (N/A: C-36 absent; by cascade N/A: C-26 absent; N/A: conversational)
The PROFILE RELEVANCE tag vocabulary is declared inside the Phase 0A exit gate REQUIRED clause as a gate-level contract, making it auditable at Phase 0A exit and Phase 3 exit.

**C-38 — Phase 4 synthesis exit gate** (N/A: C-35 absent, cascade through C-31, C-29, C-20, N=1; N/A: conversational)
Phase 4 has an exit gate that enumerates all required synthesis sections and names VERDICT MARGIN AUDIT table completeness (both boundary rows populated) as an explicit gate condition.

**C-39 — Multi-phase INCUMBENT traceability chain** (N/A: C-26 absent; by cascade N/A: conversational)
Each downstream phase (0C, Phase 1, Phase 2) names the prior phase's named INCUMBENT anchor output as its required input; a broken chain is detectable at the phase that names its predecessor.
