## roles-create R8 Scorecard

**Rubric:** v7 | **Formula:** 5 Essential @ 12pt + 2 Recommended @ 15pt + 16 Aspirational @ 0.625pt

---

### Scores

| Variation | Failures | Composite | Band |
|-----------|----------|-----------|------|
| V-05 Full Ceiling | none | **100.00** | Golden |
| V-01 Missing Header | C-22 | **99.38** | Golden |
| V-02 Preamble Restatement | C-23 | **99.38** | Golden |
| V-03 Double Adversarial | C-22 + C-23 | **98.75** | Golden |
| V-04 C-22+C-21 Compound | C-21 + C-22 | **98.75** | Golden |

**Ranking:** V-05 > V-01 = V-02 > V-03 = V-04

---

### Criterion-by-Criterion (R8 focus criteria only)

**C-22 — AUDIT-CHECKLIST header declares its own format constraint**
- V-01, V-03, V-04: **FAIL** — Header reads "Pre-declared obligations. ... Fully bidirectional." The sentence "Items name the CONTRACT block and validation scope only -- no rule enumeration" is absent. Items are thin (C-20 P) but the format rule is not self-declared. The structure is opaque about whether thin format is intentional or accidental.
- V-02, V-05: **PASS** — Full declaration present.

**C-23 — Rule content quarantined to three canonical locations**
- V-02, V-03: **FAIL** — "Constraint Overview" preamble section before the CONTRACTS block restates `orientation.frame` register requirements, `orientation.serves` beneficiary-naming rule, `lens.verify` sharpness criteria, and the generic-header prohibition in prose. Thin phases (C-19 P) and thin checklist items (C-20 P) do not shield the preamble surface — it is a fourth location outside the canonical three.
- V-01, V-04, V-05: **PASS** — No preamble, no summaries, no explanatory asides.

---

### Rubric Separation Confirmed

1. V-01 = V-02 (99.38): C-22 and C-23 are equally weighted, independent single-criterion failures.
2. V-03 = V-04 (98.75): Two-criterion penalty is additive regardless of which pair fails (both new R8, or one new + one R7 carry-forward).
3. V-05 sole 100: The checklist format declaration (C-22) is meta-commentary about the checklist's own convention — not CONTRACT rule content — so it satisfies C-22 without triggering C-23.

---

### Excellence Signals (V-05)

1. **Self-documenting checklist** — any structural convention that is intentional and non-obvious should be declared within the structure that follows it, not just followed implicitly.
2. **Three-location quarantine** — the full skill surface must be scanned for rule content outside CONTRACT blocks, phase citations, and checklist items. Preamble sections are a fourth surface that C-19 and C-20 do not cover.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["self-documenting checklist: any structural convention that is intentional and non-obvious should be declared within the structure that follows it -- not just followed implicitly", "three-location quarantine: the full skill surface must be scanned for rule content outside CONTRACT blocks, phase citations, and checklist items -- preamble sections and structural overviews are a fourth surface that C-19 and C-20 do not cover"]}
```
C-15 | Audit checks distributed as in-phase gates | PASS | Gates at Phases 0, 2, 3 (3a-3e), 4 (4a-4c); Phase 5 confirms rather than initiates. |
| C-16 | Audit obligations pre-declared before generation | PASS | CONTRACT: AUDIT-CHECKLIST declared at skill header before Phase 0. |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | Five named CONTRACT blocks cover all key invariants. |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | Each checklist item names its gate (forward); each gate cites its item ID in brackets (backward). |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | Each phase step applies a named CONTRACT block; no rule restatement in phase prose. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | All items name CONTRACT block + validation scope only; no rule enumeration. |
| C-21 | Every phase-cited CONTRACT block has checklist item | PASS | All 8 items (A-H) present; all phase-cited blocks covered. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | **FAIL** | Header reads "Pre-declared obligations. ... Fully bidirectional." The format-constraint sentence is absent. Items are thin but the format rule is not self-declared. Structure is opaque about whether thin format is intentional. |
| C-23 | Rule content quarantined to three canonical locations | PASS | No preamble, no structural summaries, no inline explanatory asides. Rule content appears only in CONTRACT blocks, phase citations, and checklist items. |

**Scoring:**
- Essential: 5/5 = 60.00
- Recommended: 2/2 = 30.00
- Aspirational: 15/16 * 10 = 9.375
- **Composite: 99.38**

---

### V-02 -- Full R7 V-05 + Preamble Restatement (C-23 adversarial)

**Axis:** Single C-23 failure. The AUDIT-CHECKLIST header carries the full format declaration (C-22 P). All phases are thin single-line CONTRACT citations (C-19 P). All checklist items name CONTRACT block and scope only (C-20 P). All phase-cited blocks have checklist items (C-21 P). The sole defect: a "Constraint Overview" section inserted before the CONTRACTS block restates rule content from CONTRACT: FIELD-REGISTER (frame register, serves beneficiary naming, lens.verify sharpness) and CONTRACT: COLUMN-HEADER (generic header prohibition) in prose.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | File written to correct path | PASS | Phases direct write to `.roles/{area}/{subrole}.md` at Phase 6. |
| C-02 | All required frontmatter fields present | PASS | All 12 fields enforced via CONTRACT: FIELD-REGISTER + Gate 3a. |
| C-03 | Mode detection routes correctly | PASS | Three clean modes + Phase 0 input guard handle all input classifications. |
| C-04 | Frontmatter content is domain-specific | PASS | CONTRACT: FIELD-REGISTER gates domain-specific content at 3b, 3c, 3d. |
| C-05 | Inertia-advocate surfaced when absent | PASS | Phase 2 + CONTRACT: INERTIA-ADVOCATE-TEMPLATE handle companion generation. |
| C-06 | Lens.verify items are sharp and actionable | PASS | CONTRACT: FIELD-REGISTER enforces boolean artifact/state/config checks, >= 4. |
| C-07 | Body section includes domain specializations table | PASS | Phase 4 requires domain specializations table with >= 3 rows. |
| C-08 | Archetype calibrated to area tier pattern | PASS | CONTRACT: FIELD-REGISTER instructs checking existing roles before applying archetype. |
| C-09 | Orientation register matches stated audience | PASS | CONTRACT: FIELD-REGISTER specifies first-person observational frame, third-person recipient serves. |
| C-10 | Body table uses domain-named column headers | PASS | CONTRACT: COLUMN-HEADER enforces domain vocabulary; generic headers listed as FAIL examples. |
| C-11 | Inertia-advocate companion generated when absent | PASS | Phase 2 generates complete companion file from CONTRACT: INERTIA-ADVOCATE-TEMPLATE. |
| C-12 | Interactive mode holds for all inputs before writing | PASS | CONTRACT: INTERACTIVE-HOLD contains categorical prohibitions; all three answers required. |
| C-13 | Pre-write self-certification phase executed | PASS | Phase 5 runs explicit YES/NO confirmation against all checklist items before Phase 6 write. |
| C-14 | Malformed inputs routed before mode detection | PASS | Phase 0 + CONTRACT: INPUT-ROUTING-RULES handle BARE AREA, EXTRA COLONS, VAGUE PHRASE, EMPTY. |
| C-15 | Audit checks distributed as in-phase gates | PASS | Gates at Phases 0, 2, 3, 4; Phase 5 confirms only. |
| C-16 | Audit obligations pre-declared before generation | PASS | CONTRACT: AUDIT-CHECKLIST declared at skill header before Phase 0. |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | Five named CONTRACT blocks cover all key invariants. |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | Each checklist item names its gate (forward); each gate cites its item ID in brackets (backward). |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | Each phase step applies a named CONTRACT block; no rule restatement in phase prose. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | All items name CONTRACT block + validation scope only; no rule enumeration. |
| C-21 | Every phase-cited CONTRACT block has checklist item | PASS | All 8 items (A-H) present; all phase-cited blocks covered. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | PASS | Header explicitly states: "Items name the CONTRACT block and validation scope only -- no rule enumeration." Format constraint self-declared. |
| C-23 | Rule content quarantined to three canonical locations | **FAIL** | "Constraint Overview" preamble section restates `orientation.frame` register requirements, `orientation.serves` beneficiary-naming rule, `lens.verify` sharpness criteria, and the generic-header prohibition in prose. These are rule content from CONTRACT: FIELD-REGISTER and CONTRACT: COLUMN-HEADER appearing outside their canonical locations. C-19 P and C-20 P do not shield this: phases and checklist are thin, but preamble is a fourth surface. |

**Scoring:**
- Essential: 5/5 = 60.00
- Recommended: 2/2 = 30.00
- Aspirational: 15/16 * 10 = 9.375
- **Composite: 99.38**

---

### V-03 -- Missing Checklist Header + Preamble Restatement (double adversarial)

**Axis:** C-22 + C-23 combined failure. AUDIT-CHECKLIST header omits the format-constraint declaration (C-22 fail). A "Constraint Overview" preamble section restates FIELD-REGISTER and COLUMN-HEADER rule content in prose (C-23 fail). All other criteria pass: bidirectional annotation, thin phase citations, thin checklist items, complete block coverage. C-22 and C-23 fail independently; neither cascades into the other.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | File written to correct path | PASS | Phases direct write to `.roles/{area}/{subrole}.md` at Phase 6. |
| C-02 | All required frontmatter fields present | PASS | All 12 fields enforced via CONTRACT: FIELD-REGISTER + Gate 3a. |
| C-03 | Mode detection routes correctly | PASS | Three clean modes + Phase 0 input guard handle all input classifications. |
| C-04 | Frontmatter content is domain-specific | PASS | CONTRACT: FIELD-REGISTER gates domain-specific content at 3b, 3c, 3d. |
| C-05 | Inertia-advocate surfaced when absent | PASS | Phase 2 + CONTRACT: INERTIA-ADVOCATE-TEMPLATE handle companion generation. |
| C-06 | Lens.verify items are sharp and actionable | PASS | CONTRACT: FIELD-REGISTER enforces boolean artifact/state/config checks, >= 4. |
| C-07 | Body section includes domain specializations table | PASS | Phase 4 requires domain specializations table with >= 3 rows. |
| C-08 | Archetype calibrated to area tier pattern | PASS | CONTRACT: FIELD-REGISTER instructs checking existing roles before applying archetype. |
| C-09 | Orientation register matches stated audience | PASS | CONTRACT: FIELD-REGISTER specifies first-person observational frame, third-person recipient serves. |
| C-10 | Body table uses domain-named column headers | PASS | CONTRACT: COLUMN-HEADER enforces domain vocabulary; generic headers listed as FAIL examples. |
| C-11 | Inertia-advocate companion generated when absent | PASS | Phase 2 generates complete companion file from CONTRACT: INERTIA-ADVOCATE-TEMPLATE. |
| C-12 | Interactive mode holds for all inputs before writing | PASS | CONTRACT: INTERACTIVE-HOLD contains categorical prohibitions; all three answers required. |
| C-13 | Pre-write self-certification phase executed | PASS | Phase 5 runs explicit YES/NO confirmation against all checklist items before Phase 6 write. |
| C-14 | Malformed inputs routed before mode detection | PASS | Phase 0 + CONTRACT: INPUT-ROUTING-RULES handle BARE AREA, EXTRA COLONS, VAGUE PHRASE, EMPTY. |
| C-15 | Audit checks distributed as in-phase gates | PASS | Gates at Phases 0, 2, 3, 4; Phase 5 confirms only. |
| C-16 | Audit obligations pre-declared before generation | PASS | CONTRACT: AUDIT-CHECKLIST declared at skill header before Phase 0. |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | Five named CONTRACT blocks cover all key invariants. |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | Each checklist item names its gate (forward); each gate cites its item ID in brackets (backward). |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | Each phase step applies a named CONTRACT block; no rule restatement in phase prose. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | All items name CONTRACT block + validation scope only; no rule enumeration. |
| C-21 | Every phase-cited CONTRACT block has checklist item | PASS | All 8 items (A-H) present; all phase-cited blocks covered. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | **FAIL** | Header reads "Pre-declared obligations. ... Fully bidirectional." -- format-constraint sentence absent. Same defect as V-01. The presence of a preamble (C-23 failure) does not contribute to this failure; each fires independently. |
| C-23 | Rule content quarantined to three canonical locations | **FAIL** | "Constraint Overview" preamble restates FIELD-REGISTER and COLUMN-HEADER rule content in prose. Same defect as V-02. The absence of the checklist header declaration (C-22 failure) does not contribute to this failure. |

**Scoring:**
- Essential: 5/5 = 60.00
- Recommended: 2/2 = 30.00
- Aspirational: 14/16 * 10 = 8.75
- **Composite: 98.75**

---

### V-04 -- Missing Checklist Header + Missing COLUMN-HEADER Declaration (C-22 + C-21 compound)

**Axis:** C-22 (new R8) + C-21 (carried from R7) compound failure. AUDIT-CHECKLIST header omits the format-constraint declaration (C-22 fail). Item F (COLUMN-HEADER compliance) is absent from the checklist while Phase 4 still cites CONTRACT: COLUMN-HEADER at Gate 4b (C-21 fail). Gate 4b notation carries no [F] suffix since F is undeclared. Items that ARE present are thin (C-20 P). No preamble restatement (C-23 P). Bidirectional annotation is intact for all declared items (C-18 P scoped to present items; coverage gap captured by C-21).

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | File written to correct path | PASS | Phases direct write to `.roles/{area}/{subrole}.md` at Phase 6. |
| C-02 | All required frontmatter fields present | PASS | All 12 fields enforced via CONTRACT: FIELD-REGISTER + Gate 3a. |
| C-03 | Mode detection routes correctly | PASS | Three clean modes + Phase 0 input guard handle all input classifications. |
| C-04 | Frontmatter content is domain-specific | PASS | CONTRACT: FIELD-REGISTER gates domain-specific content at 3b, 3c, 3d. |
| C-05 | Inertia-advocate surfaced when absent | PASS | Phase 2 + CONTRACT: INERTIA-ADVOCATE-TEMPLATE handle companion generation. |
| C-06 | Lens.verify items are sharp and actionable | PASS | CONTRACT: FIELD-REGISTER enforces boolean artifact/state/config checks, >= 4. |
| C-07 | Body section includes domain specializations table | PASS | Phase 4 requires domain specializations table with >= 3 rows. |
| C-08 | Archetype calibrated to area tier pattern | PASS | CONTRACT: FIELD-REGISTER instructs checking existing roles before applying archetype. |
| C-09 | Orientation register matches stated audience | PASS | CONTRACT: FIELD-REGISTER specifies first-person observational frame, third-person recipient serves. |
| C-10 | Body table uses domain-named column headers | PASS | CONTRACT: COLUMN-HEADER enforces domain vocabulary; generic headers listed as FAIL examples. |
| C-11 | Inertia-advocate companion generated when absent | PASS | Phase 2 generates complete companion file from CONTRACT: INERTIA-ADVOCATE-TEMPLATE. |
| C-12 | Interactive mode holds for all inputs before writing | PASS | CONTRACT: INTERACTIVE-HOLD contains categorical prohibitions; all three answers required. |
| C-13 | Pre-write self-certification phase executed | PASS | Phase 5 runs explicit YES/NO confirmation against all declared checklist items before Phase 6 write. |
| C-14 | Malformed inputs routed before mode detection | PASS | Phase 0 + CONTRACT: INPUT-ROUTING-RULES handle BARE AREA, EXTRA COLONS, VAGUE PHRASE, EMPTY. |
| C-15 | Audit checks distributed as in-phase gates | PASS | Gates at Phases 0, 2, 3, 4; Phase 5 confirms only. |
| C-16 | Audit obligations pre-declared before generation | PASS | CONTRACT: AUDIT-CHECKLIST declared at skill header before Phase 0. |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | Five named CONTRACT blocks cover all key invariants. |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | For the 7 items that ARE declared (A, B, C, D, E, G, H): each names its gate (forward); each gate cites its item ID in brackets (backward). Bidirectionality is intact on present items; coverage gap (missing F) is a C-21 failure, not C-18. |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | Each phase step applies a named CONTRACT block; no rule restatement in phase prose. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | All 7 present items name CONTRACT block + validation scope only; no rule enumeration. |
| C-21 | Every phase-cited CONTRACT block has checklist item | **FAIL** | Item F (COLUMN-HEADER compliance) is absent from the AUDIT-CHECKLIST. Phase 4 cites CONTRACT: COLUMN-HEADER at Gate 4b. CONTRACT: COLUMN-HEADER is an active block with a phase citation but no declaration entry -- unannounced check. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | **FAIL** | Header reads "Pre-declared obligations. ... Fully bidirectional." -- format-constraint sentence absent. Independent structural defect from C-21: C-21 catches the coverage gap (missing item F), C-22 catches the documentation gap (undeclared format constraint). |
| C-23 | Rule content quarantined to three canonical locations | PASS | No preamble, no structural summaries, no inline explanatory asides. Rule content appears only in CONTRACT blocks, phase citations, and checklist items. |

**Scoring:**
- Essential: 5/5 = 60.00
- Recommended: 2/2 = 30.00
- Aspirational: 14/16 * 10 = 8.75
- **Composite: 98.75**

---

### V-05 -- Full Ceiling (C-22 + C-23 both pass)

**Axis:** R8 ceiling. R7 V-05 carried forward without modification. AUDIT-CHECKLIST header carries the format-constraint declaration. No preamble, no introductory summaries, no inline explanatory asides. Rule content appears only in CONTRACT blocks, phase citations, and checklist items. All criteria pass.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | File written to correct path | PASS | Phases direct write to `.roles/{area}/{subrole}.md` at Phase 6. |
| C-02 | All required frontmatter fields present | PASS | All 12 fields enforced via CONTRACT: FIELD-REGISTER + Gate 3a. |
| C-03 | Mode detection routes correctly | PASS | Three clean modes + Phase 0 input guard handle all input classifications. |
| C-04 | Frontmatter content is domain-specific | PASS | CONTRACT: FIELD-REGISTER gates domain-specific content at 3b, 3c, 3d. |
| C-05 | Inertia-advocate surfaced when absent | PASS | Phase 2 + CONTRACT: INERTIA-ADVOCATE-TEMPLATE handle companion generation. |
| C-06 | Lens.verify items are sharp and actionable | PASS | CONTRACT: FIELD-REGISTER enforces boolean artifact/state/config checks, >= 4. |
| C-07 | Body section includes domain specializations table | PASS | Phase 4 requires domain specializations table with >= 3 rows. |
| C-08 | Archetype calibrated to area tier pattern | PASS | CONTRACT: FIELD-REGISTER instructs checking existing roles before applying archetype. |
| C-09 | Orientation register matches stated audience | PASS | CONTRACT: FIELD-REGISTER specifies first-person observational frame, third-person recipient serves. |
| C-10 | Body table uses domain-named column headers | PASS | CONTRACT: COLUMN-HEADER enforces domain vocabulary; generic headers listed as FAIL examples. |
| C-11 | Inertia-advocate companion generated when absent | PASS | Phase 2 generates complete companion file from CONTRACT: INERTIA-ADVOCATE-TEMPLATE. |
| C-12 | Interactive mode holds for all inputs before writing | PASS | CONTRACT: INTERACTIVE-HOLD contains categorical prohibitions; all three answers required. |
| C-13 | Pre-write self-certification phase executed | PASS | Phase 5 runs explicit YES/NO confirmation against all checklist items before Phase 6 write. |
| C-14 | Malformed inputs routed before mode detection | PASS | Phase 0 + CONTRACT: INPUT-ROUTING-RULES handle BARE AREA, EXTRA COLONS, VAGUE PHRASE, EMPTY. |
| C-15 | Audit checks distributed as in-phase gates | PASS | Gates at Phases 0, 2, 3, 4; Phase 5 confirms only. |
| C-16 | Audit obligations pre-declared before generation | PASS | CONTRACT: AUDIT-CHECKLIST declared at skill header before Phase 0. |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | Five named CONTRACT blocks cover all key invariants. |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | Each checklist item names its gate (forward); each gate cites its item ID in brackets (backward). |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | Each phase step applies a named CONTRACT block; no rule restatement in phase prose. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | All items name CONTRACT block + validation scope only; no rule enumeration. |
| C-21 | Every phase-cited CONTRACT block has checklist item | PASS | All 8 items (A-H) present; all phase-cited blocks covered. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | PASS | Header explicitly states: "Items name the CONTRACT block and validation scope only -- no rule enumeration." Format constraint self-declared within the structure. |
| C-23 | Rule content quarantined to three canonical locations | PASS | No preamble section, no structural summaries, no inline explanatory asides. The C-22 format declaration in the checklist header is meta-commentary about the checklist itself -- not a restatement of CONTRACT rule content -- and does not trigger C-23. |

**Scoring:**
- Essential: 5/5 = 60.00
- Recommended: 2/2 = 30.00
- Aspirational: 16/16 * 10 = 10.00
- **Composite: 100.00**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 Full Ceiling | 5/5 (60) | 2/2 (30) | 16/16 (10.00) | **100.00** | Golden |
| V-01 Missing Header | 5/5 (60) | 2/2 (30) | 15/16 (9.375) | **99.38** | Golden |
| V-02 Preamble Restatement | 5/5 (60) | 2/2 (30) | 15/16 (9.375) | **99.38** | Golden |
| V-03 Double Adversarial | 5/5 (60) | 2/2 (30) | 14/16 (8.75) | **98.75** | Golden |
| V-04 C-22+C-21 Compound | 5/5 (60) | 2/2 (30) | 14/16 (8.75) | **98.75** | Golden |

**Ranking:** V-05 (100) > V-01 = V-02 (99.38) > V-03 = V-04 (98.75)

---

## Rubric Separation Check

**C-22 and C-23 are equally weighted, single-criterion, independent failures.**
V-01 (C-22 fail only) and V-02 (C-23 fail only) tie at 99.38 -- confirms each criterion costs exactly 0.625 points (1/16 * 10) and neither cascades into the other.

**The two-criterion penalty is additive regardless of which criteria pair fails.**
V-03 (C-22 + C-23) and V-04 (C-21 + C-22) both score 98.75 -- confirms two failed aspirational criteria cost exactly 1.25 points whether both are new R8 criteria (V-03) or one is a carry-forward from R7 (V-04).

**V-05 is the sole 100.** The checklist format declaration (C-22) and the preamble absence (C-23) are simultaneously satisfiable without conflict: the format declaration in the checklist header is meta-commentary about the checklist itself, not a restatement of CONTRACT rule content, and does not trigger C-23.

---

## Failure Analysis

### C-22 failure signature (V-01, V-03, V-04)

The AUDIT-CHECKLIST CONTRACT header reads:

> "Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional."

The missing sentence: "Items name the CONTRACT block and validation scope only -- no rule enumeration."

**Why this matters:** A reader encountering the checklist cannot determine from the structure itself whether the thin-reference format is intentional design or accidental brevity. The constraint is followed but not announced. C-22 requires the format rule to be stated within the structure that uses it.

### C-23 failure signature (V-02, V-03)

The "Constraint Overview" preamble appears before the CONTRACTS block and contains:

> "**Field register.** `orientation.frame` uses first-person observational language... `orientation.serves` names a specific beneficiary in third-person... `lens.verify` items are boolean checks naming a specific artifact, state, or config..."
>
> "**Column headers.** Every column header in the body table uses domain vocabulary. Generic terms -- Component, Purpose, Item, Description, Notes, Value, Entity, Consideration -- are not permitted..."

This reproduces rule content from CONTRACT: FIELD-REGISTER and CONTRACT: COLUMN-HEADER outside their canonical locations. Phases are thin (C-19 P). Checklist items are thin (C-20 P). Neither guards against the preamble surface. C-23 is the only criterion that catches this fourth location.

**Why this matters:** The preamble pattern is adversarial precisely because it appears helpful. It looks like documentation. It does not violate C-19 or C-20. It passes C-22 (in V-02). Only C-23 -- which governs the full skill surface, not just phases and checklist items -- detects the quarantine violation.

---

## Excellence Signals (V-05)

**1. Self-documenting checklist format declaration**
The AUDIT-CHECKLIST header contains: "Items name the CONTRACT block and validation scope only -- no rule enumeration." This sentence is:
- A meta-statement about the checklist's own format constraint
- Not a restatement of any CONTRACT rule (so C-23 safe)
- Present within the structure that uses the format (so C-22 pass)
The pattern: any structural convention that is intentional and non-obvious should be declared within the structure that follows it.

**2. Three-location quarantine with no fourth surface**
V-05 has no preamble, no structural overview, no inline commentary, no introductory summary. The discipline is total: rule content exists only in (1) CONTRACT blocks, (2) phase citation lines, (3) checklist items. Every other part of the skill is structural scaffolding (headings, gate labels, procedural connectives) with no rule content. The test: scan the entire skill outside CONTRACT blocks for any sentence that could appear in a CONTRACT block. In V-05, there are none.

**3. C-22 and C-23 do not conflict**
The format declaration in the checklist header satisfies C-22 without violating C-23 because it is a meta-statement about the checklist's own constraint -- not a restatement of rule content from any CONTRACT block. The distinction is: commentary about a structural convention vs. reproduction of a domain rule. V-05 demonstrates that both can pass simultaneously without tension.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["self-documenting checklist: any structural convention that is intentional and non-obvious should be declared within the structure that follows it -- not just followed implicitly", "three-location quarantine: the full skill surface must be scanned for rule content outside CONTRACT blocks, phase citations, and checklist items -- preamble sections and structural overviews are a fourth surface that C-19 and C-20 do not cover"]}
```
