Now I have everything I need. Let me score all five variations.

---

## roles-create Scorecard — R9 (2026-03-17)

**Rubric:** v8 | **Denominator:** 16 aspirational | **Formula:** 5×12 + 2×15 + (n/16)×10

---

### Criterion-by-Criterion Evaluation

#### C-01 — Role file written to correct path
All 5 variations: Phase 6 writes to `.roles/{area}/{subrole}.md` explicitly. **PASS all.**

#### C-02 — All required frontmatter fields present
All 5 variations: Phase 3 generates all 12 fields under CONTRACT: FIELD-REGISTER. **PASS all.**

#### C-03 — Mode detection routes correctly
All 5 variations: Phase 1 explicitly handles NAME-ONLY, DESCRIPTION, INTERACTIVE paths. **PASS all.**

#### C-04 — Frontmatter content is domain-specific
All 5 variations: CONTRACT: FIELD-REGISTER enforces domain-specific orientation.frame, orientation.serves, lens.verify, expertise.depth. **PASS all.**

#### C-05 — Inertia-advocate surfaced when absent
All 5 variations: Phase 2 checks the path and generates the companion when absent. **PASS all.**

#### C-06 — Lens.verify questions sharp and actionable
All 5 variations: FIELD-REGISTER requires boolean checks naming specific artifact/state/config, ≥4 items. **PASS all.**

#### C-07 — Body section includes domain specializations table
All 5 variations: Phase 4 produces `## {Subrole} Domain` heading + table, minimum 3 rows. **PASS all.**

#### C-08 — Archetype calibrated to area tier pattern
All 5 variations: FIELD-REGISTER table says "Check existing roles in the area first; use their value." **PASS all.**

#### C-09 — Orientation register matches stated audience
All 5 variations: FIELD-REGISTER explicitly separates first-person observational (frame) from third-person recipient (serves). **PASS all.**

#### C-10 — Body table uses domain-named column headers
All 5 variations: CONTRACT: COLUMN-HEADER defines the domain vocabulary requirement with explicit FAIL/PASS examples. **PASS all.**

#### C-11 — Inertia-advocate companion file generated when absent
All 5 variations: Phase 2 ABSENT branch generates full companion via CONTRACT: INERTIA-ADVOCATE-TEMPLATE. **PASS all.**

#### C-12 — Interactive mode holds for all inputs before writing
All 5 variations: CONTRACT: INTERACTIVE-HOLD is categorical — "Do not proceed until all three answers are confirmed." **PASS all.**

#### C-13 — Pre-write self-certification phase executed
All 5 variations: Phase 5 (Pre-Write Confirmation) runs explicit `[A]–[H]` checklist with YES/NO requirement before write. **PASS all.**

#### C-14 — Malformed inputs routed before mode detection
All 5 variations: Phase 0 (Input Guard) applies CONTRACT: INPUT-ROUTING-RULES to classify BARE AREA, EXTRA COLONS, VAGUE PHRASE, EMPTY before routing. **PASS all.**

#### C-15 — Audit checks distributed as in-phase gates
- **V-01/V-02/V-03/V-05:** `-> Gate N [ID]: ... PASS / FAIL` annotations embedded in each phase. **PASS.**
- **V-04:** Gate tables (Gate / [ID] / Criterion / Verdict) appear within each respective phase section — not consolidated at Phase 5. **PASS.** Placement-based criterion; format-neutral.

#### C-16 — Audit obligations pre-declared before generation
All 5 variations: CONTRACT: AUDIT-CHECKLIST appears in the CONTRACTS block, before any PHASE section. **PASS all.**

#### C-17 — Hard constraints extracted into named CONTRACT sections
All 5 variations: Six named CONTRACT blocks (INPUT-ROUTING-RULES, INTERACTIVE-HOLD, FIELD-REGISTER, COLUMN-HEADER, INERTIA-ADVOCATE-TEMPLATE, AUDIT-CHECKLIST) at top level. **PASS all.**

#### C-18 — Declaration-to-gate traceability is bidirectional
- **V-01/V-02/V-03/V-05:** Forward: AUDIT-CHECKLIST "Gated At" column names the gate phase. Backward: gate annotations include `[ID]` suffix matching checklist row. **PASS.**
- **V-04:** Forward: same "Gated At" column. Backward: `[ID]` column in each gate table provides the backward reference (e.g., `| 0 | [G] | ...`). The column satisfies the criterion as a structural identifier — not required to be inline prose. **PASS.** This is R9's highest-risk question, resolved affirmatively.

#### C-19 — Content-producing phases are thin CONTRACT citations
- **V-01 (declarative):** "CONTRACT: FIELD-REGISTER governs all 12 required fields." — declarative register, but no rule restatement. Equivalent to "Apply CONTRACT: FIELD-REGISTER" in content. C-19 is register-neutral. **PASS.**
- **V-02 (compact):** "CONTRACT: FIELD-REGISTER applied. All 12 frontmatter fields generated for `.roles/{area}/{subrole}.md`." — maximum compaction; still a thin citation. **PASS.**
- **V-03:** Phase structure matches V-05. **PASS.**
- **V-04:** Phase bodies are single-sentence CONTRACT citations ("Apply CONTRACT: FIELD-REGISTER. Generate all 12 required frontmatter fields..."). Gate tables are structural scaffolding, not rule content. **PASS.**
- **V-05:** Proven. **PASS.**

#### C-20 — AUDIT-CHECKLIST items are thin CONTRACT references
All 5 variations: items follow the form "FIELD-REGISTER compliance -- frontmatter field completeness" — CONTRACT name + scope, no rule enumeration. **PASS all.**

#### C-21 — Every phase-cited CONTRACT block has ≥1 AUDIT-CHECKLIST item
All 5 variations: All content-producing CONTRACT citations (FIELD-REGISTER → B/C/D/E, INERTIA-ADVOCATE-TEMPLATE → H, COLUMN-HEADER → F, INPUT-ROUTING-RULES → G) have checklist items. INTERACTIVE-HOLD is cited only in Phase 1 (a routing step, not content-producing) — exempt, confirmed by V-05 being proven 100 with the same pattern. **PASS all.**

#### C-22 — AUDIT-CHECKLIST header declares its own format constraint
All 5 R9 variations include the declaration sentence: **"Items name the CONTRACT block and validation scope only -- no rule enumeration."** This is the key R8 lesson incorporated into all R9 variations. **PASS all.**

#### C-23 — Rule content quarantined to three canonical locations
- **V-01:** Declarative phase phrases name CONTRACT categories (BARE AREA, VAGUE PHRASE) in routing instructions — same as V-05 ("If input is BARE AREA or VAGUE PHRASE"). No additional rule surface. No preamble. **PASS.**
- **V-02:** Most compact phases of any variation — least surface area. No preamble. **PASS.**
- **V-03:** Same phase content as V-05 (only ordering changed). No preamble. **PASS.**
- **V-04:** Gate table rows contain criteria labels ("INPUT-ROUTING-RULES applied; input classified as clean or resolved") — structural labels, not rule definitions. No preamble. **PASS.**
- **V-05:** Proven. **PASS.**

---

### Score Matrix

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | Score |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 Declarative | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-02 Compact Phases | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-03 Front-Loaded Inertia | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-04 Tabular Gate Blocks | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-05 Full Ceiling | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |

**Composite (all):** 5×12 + 2×15 + 16/16×10 = 60 + 30 + 10 = **100.00**

---

### Ranking

All 5 variations: **100 / 100 — tied.**

R9 design intent achieved. All variations cleared all 16 criteria. No discrimination within the passing space.

---

### Excellence Signals

**What made every variation succeed:**

1. **C-22 adoption is universal.** All 5 R9 variations incorporated the R8 lesson — the AUDIT-CHECKLIST header explicitly declares its format constraint ("Items name the CONTRACT block and validation scope only -- no rule enumeration."). This was the single most important carry-forward from R8.

2. **C-19 is register-neutral (V-01 confirmation).** Declarative phrasing ("CONTRACT: X governs this phase") is equivalent to imperative ("Apply CONTRACT: X") for thin-citation compliance. Register is a presentation property; restatement is the violation. V-01 proves the criterion binds on *whether rules are restated*, not *how the citation is phrased*.

3. **C-15 and C-18 are format-neutral (V-04 confirmation).** Tabular gate blocks satisfy both distributed-in-phase (C-15) and bidirectionality (C-18). The `[ID]` column in a gate table is a valid backward reference — criterion requires the annotation to *exist*, not to appear as an inline suffix. This opens a legitimate structural variant for skills where table-based gate summaries are preferable.

4. **C-21 is order-neutral (V-03 confirmation).** CONTRACT block ordering and AUDIT-CHECKLIST row ordering have no effect on any criterion. Coverage is the invariant; sequence is a presentation choice.

5. **Phase compaction is safe (V-02 confirmation).** Single-sentence CONTRACT citations (maximum compaction) preserve all structural properties. Narrative richness and fix-and-retry prose in phase bodies are optional — the minimum viable form is a one-line CONTRACT name + gate annotation.

---

### R9 Finding

**All 5 variations score 100.** The passing space is structurally diverse: declarative register, compact phases, reordered CONTRACTs, tabular gates, and canonical form all achieve the ceiling. The criteria govern what is present and absent, not how it is expressed. R9 maps the *equivalence class* of valid skill structures — any form that quarantines rule content, pre-declares obligations, carries the AUDIT-CHECKLIST format header, and distributes bidirectional gates will score 100.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-19 is register-neutral: declarative phase phrasing satisfies thin-citation as well as imperative", "C-15 and C-18 are format-neutral: tabular gate blocks with an [ID] column satisfy distributed-in-phase and bidirectionality requirements", "C-21 is order-neutral: CONTRACT block ordering and checklist row ordering have no effect on coverage compliance", "Maximum phase compaction (single-sentence citation + gate) preserves all structural criteria — narrative richness in phases is optional"]}
```
