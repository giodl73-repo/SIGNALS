"""Build trace-state-rubric-v4 from v3 + Round 3 excellence signals."""

with open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v3-2026-03-15.md', 'r', encoding='utf-8') as f:
    v3 = f.read()

# v4 header block (replaces the v3 header up to the Criteria Table)
header = """\
# trace-state Quest Rubric -- v4

**Skill**: trace-state | **Skill family**: trace | **Version**: v4
**Date**: 2026-03-15 | **Criterion count**: 18 (5 essential, 3 recommended, 10 aspirational)

---

## What changed in v4

**2 new aspirational criteria** (C-17, C-18), one per named excellence pattern from Round 3:

| ID | Pattern | Output property |
|----|---------|----------------|
| C-17 | predicate-source-citation-inline | Every predicate field carries an inline `[->DECL: EntityName.fieldName]` annotation naming its declaration source. The annotation is co-located with the predicate -- the cross-reference is verifiable at the point of use without a document-level scan. C-11 and C-14 are prerequisites. Correct vocabulary throughout without inline citations does not pass. |
| C-18 | phase-boundary-completion-gate | Each major structural section of the trace ends with an explicit completion gate -- a checklist or gate table that enumerates required output elements for that section and marks each as produced. The gate appears in the output (not as a prompt comment) before the next section begins. An end-of-document checklist covering all sections at once does not satisfy C-18 -- gates must be per-section. |

**Scoring formula**: aspirational denominator updated from `/8` to `/10`.

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)
```

**Retroactive R3 scores under v4** (C-17 and C-18 applied; V-01 gains C-18 FAIL; V-02 gains C-17 FAIL + C-18 PASS; V-03 gains C-17 PASS + C-18 FAIL):

| Variation | v3 aspirational | v4 aspirational | v3 composite | v4 composite | Golden? |
|-----------|----------------|----------------|--------------|--------------|---------|
| V-01 | 5/8 | 5/10 | 96.25 | 95.00 | yes |
| V-02 | 7/8 | 8/10 | 98.75 | 98.00 | yes |
| V-03 | 6/8 | 7/10 | 97.50 | 97.00 | yes |

No golden status changes. The aspirational weight floor (10 points at /10 denominator) degrades gracefully.

"""

# Criteria table (full, replacing v3's partial/truncated table)
criteria_table = """\
## Criteria Table

| Tier | ID | Summary |
|------|----|---------|
| Essential | C-01 | State transition chain (before/op/after triples, unbroken) |
| Essential | C-02 | Preconditions specified per operation |
| Essential | C-03 | Postconditions specified per operation |
| Essential | C-04 | At least one invalid transition identified |
| Essential | C-05 | Invariants documented (min 2) |
| Recommended | C-06 | Missing precondition checks flagged |
| Recommended | C-07 | Domain vocabulary consistent with role |
| Recommended | C-08 | Race condition analysis present |
| Aspirational | C-09 | Invariant violation severity classification |
| Aspirational | C-10 | Alternate/error path traced |
| Aspirational | C-11 | Predicate notation -- `entity.field OPERATOR value`, not prose |
| Aspirational | C-12 | Concurrent interleaving expressed as T0/T1 two-column table (min 4 rows) |
| Aspirational | C-13 | Invalid transitions framed as baseline deltas -- `(baseline_state, attempted_delta, failure_reason)` |
| Aspirational | C-14 | Pre-trace vocabulary declaration block |
| Aspirational | C-15 | Post-trace vocabulary audit (enumerated mapping table, not checkbox list) |
| Aspirational | C-16 | Predicate-vocabulary cross-reference |
| Aspirational | C-17 | Per-predicate source citation -- `[->DECL: EntityName.fieldName]` inline annotations |
| Aspirational | C-18 | Per-section completion gate markers |

"""

# Two new criterion definitions to append before the Score Sheet
c17 = """\
### C-17 - Per-Predicate Source Citation

- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every predicate field in the output carries an inline citation annotation of the form `[->DECL: EntityName.fieldName]` naming the declaration entry it was drawn from. The annotation is co-located with the predicate, not deferred to a separate cross-reference section. This makes each predicate independently verifiable against the declaration without a document-level scan.
- **Pass condition**: At least 80% of predicate fields carry a `[->DECL: EntityName.fieldName]` annotation naming their declaration source. The annotation names the exact entity and field from the C-14 declaration section. An output where all predicate fields happen to match the declaration but carry no annotations does not satisfy C-17 -- the annotation is the artifact, not just the match. C-11 and C-14 are prerequisites; C-17 strengthens C-16 by moving the evidence to the point of use.
- **Excellence source**: V-03 (Cross-Reference Annotation) -- the `[->DECL: EntityName.fieldName]` annotation syntax was the specific design that moved C-16 from PARTIAL to PASS in V-03 while V-01 and V-02 remained PARTIAL with instruction-only enforcement ("all field names match Phase 0"). The distinction: C-16 checks whether the names match (a global property requiring a document scan); C-17 checks whether the match is annotated in-line (a local, point-of-use property). V-03 satisfied both; V-01 and V-02 satisfied neither with structural guarantees.

### C-18 - Per-Section Completion Gate Markers

- **Weight**: aspirational
- **Category**: structure
- **Text**: Each major structural section of the trace output -- at minimum the vocabulary declaration section and the main trace section -- ends with an explicit completion gate. The gate is a checklist or gate table that enumerates required output elements for that section and confirms each was produced before the next section begins. The gate appears in the output; a single end-of-document compliance checklist covering all sections at once does not satisfy this criterion.
- **Pass condition**: At least two distinct sections in the output end with a completion gate (checklist or gate table) that: (a) enumerates specific required elements for that section by name, (b) marks each as present or absent, (c) appears between that section and the next. An end-of-document assertion ("all requirements met") without per-section enumeration does not pass. A gate that lists section headings without enumerating specific required elements within each section does not pass.
- **Excellence source**: V-02 (Lifecycle Emphasis + Gate Architecture) -- per-phase gate checklists in V-02 were the specific mechanism that drove C-12 from PARTIAL to PASS. V-01 and V-03 both produced T0/T1 tables but without a gate specifying "at least 4 rows," their templates defaulted to 3 rows. V-02's phase gate checklist embedded the minimum-depth requirement as a section-level completion condition: the gate did not pass unless the table had at least 4 rows. Gate markers convert quantitative requirements from prompt instructions into section-boundary exit criteria, forcing compliance at the point where the section closes rather than relying on the model to remember a requirement from elsewhere in the prompt.

"""

# Updated score sheet (v4 adds C-17 and C-18 rows, updates formula)
score_sheet = """\
## Score Sheet Template

| ID    | Criterion                                             | Tier         | Pass? |
|-------|-------------------------------------------------------|--------------|-------|
| C-01  | State transition chain (before/op/after triples)      | essential    |       |
| C-02  | Preconditions per operation                           | essential    |       |
| C-03  | Postconditions per operation                          | essential    |       |
| C-04  | At least one invalid transition identified            | essential    |       |
| C-05  | Invariants documented (min 2)                         | essential    |       |
| C-06  | Missing precondition checks flagged                   | recommended  |       |
| C-07  | Domain vocabulary consistent with role                | recommended  |       |
| C-08  | Race condition analysis present                       | recommended  |       |
| C-09  | Invariant violation severity classification           | aspirational |       |
| C-10  | Alternate/error path traced                           | aspirational |       |
| C-11  | Predicate notation for pre/postconditions             | aspirational |       |
| C-12  | Concurrent interleaving as T0/T1 table (min 4 rows)   | aspirational |       |
| C-13  | Invalid transitions framed as baseline deltas         | aspirational |       |
| C-14  | Pre-trace vocabulary declaration block                | aspirational |       |
| C-15  | Post-trace vocabulary audit (enumerated table)        | aspirational |       |
| C-16  | Predicate-vocabulary cross-reference                  | aspirational |       |
| C-17  | Per-predicate source citation [->DECL: E.field]       | aspirational |       |
| C-18  | Per-section completion gate markers                   | aspirational |       |

```
essential_pass    = count of C-01..C-05 that pass  (max 5)
recommended_pass  = count of C-06..C-08 that pass  (max 3)
aspirational_pass = count of C-09..C-18 that pass  (max 10)

composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)

golden = all_essential_pass AND composite >= 80
```

"""

# Updated changelog
changelog = """\
## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | 2026-03-15 | Added C-11, C-12, C-13 from Round 1 excellence signals; aspirational weight formula updated to /5 |
| v3 | 2026-03-15 | Added C-14, C-15, C-16 from Round 2 excellence signals (role-vocabulary-declaration-gate, in-prompt self-correction mandate, role-formal-notation-orthogonality); aspirational weight formula updated to /8 |
| v4 | 2026-03-15 | Added C-17, C-18 from Round 3 excellence signals (predicate-source-citation-inline, phase-boundary-completion-gate); aspirational weight formula updated to /10 |
"""

# -----------------------------------------------------------------------
# Assemble v4 from v3 parts + new material
# -----------------------------------------------------------------------

# Extract the Design Notes section through end of C-16 from v3
# v3 structure after the criteria table fragment:
#   "## Design Notes" ... "## Score Sheet Template" ... "## Changelog"
design_start = v3.index('\n## Design Notes\n')
score_start  = v3.index('\n## Score Sheet Template\n')

# Body = Design Notes through end of C-16 (everything before Score Sheet)
# We need to insert C-17 and C-18 between C-16 and Score Sheet
body_design_through_c16 = v3[design_start:score_start].rstrip('\n')

# Update Design Notes in v3 to add C-17 / C-18 bullets
old_last_note = '- Aspirational criteria raise the bar once essential and recommended are stable; absence does not block golden if composite >= 80'
new_last_notes = (
    '- C-17 is the point-of-use evidence for C-16: citation annotations make cross-reference verifiable at the predicate rather than requiring a document-level scan\n'
    '- C-18 is the structural discipline behind C-12: per-section gates force quantitative requirements (minimum row counts, required fields) to be met section-by-section rather than potentially deferred or silently omitted\n'
    '- Aspirational criteria raise the bar once essential and recommended are stable; absence does not block golden if composite >= 80'
)
body_design_through_c16 = body_design_through_c16.replace(old_last_note, new_last_notes)

v4 = (
    header
    + '---\n\n'
    + criteria_table
    + '---\n'
    + body_design_through_c16
    + '\n\n'
    + c17
    + '---\n\n'
    + score_sheet
    + '---\n\n'
    + changelog
)

out_path = 'C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v4-2026-03-15.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(v4)

lines = v4.count('\n')
chars = len(v4)
print(f'Written. Lines: {lines}, chars: {chars}')
