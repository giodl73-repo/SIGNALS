"""Build trace-permissions-rubric-v2 from v1 + R1 excellence signals."""

with open('C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v1-2026-03-16.md', 'r', encoding='utf-8') as f:
    v1 = f.read()

# Replace frontmatter version
v2 = v1.replace('version: 1', 'version: 2')

# Replace title line
v2 = v2.replace(
    '# Rubric: trace-permissions\n\nEvaluates',
    '# Rubric: trace-permissions\n\n## Changelog\n\n| Version | Date | Change |\n|---------|------|--------|\n| v1 | 2026-03-16 | Initial rubric (4 essential, 3 recommended, 2 aspirational) |\n| v2 | 2026-03-16 | Added C-10, C-11, C-12 from R1 excellence signals (V-05 top scorer, 95 pts) |\n\n---\n\nEvaluates'
)

# New aspirational criteria rows to append after C-09 row
C10_ROW = '| C-10 | **Blind-Spot-Labeled Tables** -- Each table or section names the specific failure mode it closes (e.g., "closes: silent FLS omission"), converting gap-hunting from a generic obligation into motivated closure against named failure modes. | aspirational | format | At least one table header, section title, or opening sentence names the specific blind spot or failure mode the section addresses -- not a generic label like "FLS Analysis" but a named risk like "closes: cumulative privilege via team membership". |'

C11_ROW = '| C-11 | **Data-Row Null-Case Mandate** -- The null case (e.g., "no FLS profile configured") appears as an explicit data row in the relevant table, not as a prose disclaimer before the table. | aspirational | correctness | At least one null or empty case appears as a data row -- e.g., a table row where FLS Profile = "Not Configured" or Gap Type = "CLEARED" -- rather than as prose commentary outside the table. Silent omission is structurally impossible when the null case is a required row. |'

C12_ROW = '| C-12 | **Escalation Risk Column in Closing Summary** -- The closing summary table includes an Escalation Risk column (HIGH / MEDIUM / LOW / NONE) populated for all traced operations or roles. | aspirational | format | The closing summary table contains an Escalation Risk column with an explicit scale (at minimum two levels) and every row populated. This column satisfies C-05 evidence and C-09 format simultaneously from a single column. |'

C09_ROW = '| C-09 | **Structured Summary Table** -- The output closes with a summary table: each operation row contains role, FLS verdict (pass/fail/partial), record scope, and gap flag. | aspirational | format | A table with at minimum three columns (operation or role, FLS status, record scope) is present and consistently populated for all traced operations. |'

assert C09_ROW in v2, 'C-09 row not found'

v2 = v2.replace(
    C09_ROW,
    C09_ROW + '\n' + C10_ROW + '\n' + C11_ROW + '\n' + C12_ROW
)

# Replace the Design Rationale section (inserted before Scoring Guide)
OLD_SCORING = '## Scoring Guide'
NEW_RATIONALE = '''## Design Rationale

- **C-04 is essential** -- an output that only confirms what is allowed without surfacing any risk has zero value for a permissions tracer.
- **C-05 is recommended, not essential** -- the skill may legitimately be called in a context where no escalation path exists; forcing a gap there would make valid clean outputs fail.
- **C-08 is aspirational** -- requires cross-entity schema knowledge that not every invocation context will have.
- **C-10 is aspirational** -- naming blind spots is a quality amplifier, not a correctness requirement; an output without labeled tables can still pass all essential and recommended bars.
- **C-11 is aspirational** -- the data-row null-case is a structural enforcement technique; prose null-case disclaimers satisfy the underlying C-02/C-04 intent even if they are easier to silently omit.
- **C-12 is aspirational** -- the escalation risk column is a bonus efficiency signal; an output can pass C-05 and C-09 separately without combining them into a single column.

---

## Scoring Guide'''

v2 = v2.replace(OLD_SCORING, NEW_RATIONALE, 1)

# Extend evaluator notes with C-10/C-11/C-12 guidance
OLD_LAST = '- "Placeholder" or stub outputs with no actual permission data fail all essential criteria.'
NEW_LAST = '''- "Placeholder" or stub outputs with no actual permission data fail all essential criteria.
- C-10, C-11, C-12 are scored independently -- an output can earn any combination of the three.
- C-12 requires a closing summary table to exist (C-09 pass condition) before it can be evaluated; if no summary table is present, C-12 fails automatically.'''

v2 = v2.replace(OLD_LAST, NEW_LAST)

out_path = 'C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v2-2026-03-16.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(v2)

print(f'Written: {out_path}')
print(f'v1 length: {len(v1)} chars')
print(f'v2 length: {len(v2)} chars')
print(f'Delta: +{len(v2) - len(v1)} chars')
