import re

v5 = open('C:/src/sim/simulations/quest/rubrics/mock-ns-rubric-v5-2026-03-16.md', encoding='utf-8').read()
split = v5.index('## Scoring')
v5_body = v5[split:]

# 1. Update scoring table and count line
v5_body = v5_body.replace(
    '| Aspirational | C-09--C-22 | 2 | 28 |',
    '| Aspirational | C-09--C-24 | 2 | 32 |'
).replace(
    '| **Total** | | | **108** |',
    '| **Total** | | | **112** |'
).replace(
    'Each criterion is worth 2 pts (14 x 2 = 28; max score = 108).',
    'Each criterion is worth 2 pts (16 x 2 = 32; max score = 112).'
)

# 2. Splice R5 discriminator notes into C-11
v5_body = v5_body.replace(
    'Cases 1 and 2 may be collapsed into a single row when they share the same flag value; completeness is functional, not structural. Source: R1 Pattern 2',
    'Cases 1 and 2 may be collapsed into a single row when they share the same flag value; completeness is functional, not structural. **Note (R5 discriminator):** C-11 passing (functional 5-case coverage) does not imply C-22 passing (structural row separation). A 4-row table that collapses HS-critical-tier=1 into the non-critical catch-all satisfies C-11 but fails C-22. Source: R1 Pattern 2'
)

# C-15: after the R4 trap note, before Source
v5_body = v5_body.replace(
    'The two criteria require separate sentences to satisfy both simultaneously. Source: R2 V-05',
    'The two criteria require separate sentences to satisfy both simultaneously. **Note (R5 discriminator):** C-15 passing (3 op types named) does not imply C-21 passing (4 op types including body generation). C-15 is a necessary but not sufficient precondition for C-21. Source: R2 V-05'
)

# C-17: fix apostrophe variant and add note
v5_body = v5_body.replace(
    "What fails C-17 is a CONSTRAINT that names only operation types without referencing S-1 by label (V-02's form). Source: R3 V-03",
    'What fails C-17 is a CONSTRAINT that names only operation types without referencing S-1 by label (V-02 form). **Note (R5 discriminator):** C-17 passing (terminal gate names S-1) does not imply C-19 passing (dual-gate form). A terminal-gate-only skill satisfies C-17 but fails C-19 because the reader encounters resolution logic before any gate language. Source: R3 V-03'
)

# C-19: add note before Source
v5_body = v5_body.replace(
    'Belt-and-suspenders coverage eliminates scorer ambiguity by stating the constraint at both the entry and exit of the step. Source: R4 V-05 excellence signal -- dual-gate form covers both C-17 equivalents simultaneously.',
    'Belt-and-suspenders coverage eliminates scorer ambiguity by stating the constraint at both the entry and exit of the step. **Note (R5 discriminator):** C-17 pass does not imply C-19 pass. See C-23 for a further tightening of preamble gate position. Source: R4 V-05 excellence signal -- dual-gate form covers both C-17 equivalents simultaneously.'
)

# C-21: add note before Source
v5_body = v5_body.replace(
    'A CONSTRAINT with only the C-15 minimum 3 does not satisfy this criterion. This closes an adversarial gap where a model might defer category and skill selection but begin generating artifact body content before S-0 is complete. Source: R4 V-05',
    'A CONSTRAINT with only the C-15 minimum 3 does not satisfy this criterion. This closes an adversarial gap where a model might defer category and skill selection but begin generating artifact body content before S-0 is complete. **Note (R5 discriminator):** C-15 passing (3 op types) does not imply C-21 passing (4 op types). See C-24 for an extension requiring a 5th op type (artifact write phase). Source: R4 V-05'
)

# C-22: add note before Source
v5_body = v5_body.replace(
    'The tier-1 critical row must name the critical namespaces in its condition cell (consistent with C-16). Source: R4 V-05 excellence signal -- "5-row FLAG table separates HS critical tier-1 from non-critical explicitly -- strengthens C-11 above minimum."',
    'The tier-1 critical row must name the critical namespaces in its condition cell (consistent with C-16). **Note (R5 confirmation):** A 4-row FLAG table that absorbs HS-critical-tier=1 into the non-critical catch-all satisfies C-11 (functional coverage) but fails C-22 (structural separation). C-11 passing is a necessary but not sufficient condition for C-22. Source: R4 V-05 excellence signal -- "5-row FLAG table separates HS critical tier-1 from non-critical explicitly."'
)

# 3. Append C-23 and C-24 before the Common Failure Modes section
c23_c24 = """
### C-23
- **Text**: Preamble gate is the opening sentence of S-0, preceding all resolution logic including the parameter table.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The preamble gate sentence (required for C-19) appears as the absolute first sentence in the S-0 step body -- before any resolution bullets, parameter rows, or introductory prose. A preamble gate that appears after one or more lines of context-setting or introductory text does not satisfy this criterion, even if it precedes the resolution table (satisfying C-19). The distinction: C-19 requires the preamble gate to be before the resolution bullets; C-23 requires it to be the first content of the step with no pre-gate surface area. A reader or model scanning S-0 top-to-bottom must encounter the constraint before any logic framing. A prompt with a one-sentence introduction followed by the preamble gate satisfies C-19 but fails C-23. Source: R5 V-03 canary -- when the preamble gate is absent, "a reader scanning S-0 encounters the resolution table before any gate language." The natural defense is to make the preamble gate the opening content of the step, eliminating all pre-gate surface area.

### C-24
- **Text**: CONSTRAINT names 5 or more prohibited operation types, adding artifact path construction or file write to the C-21 minimum.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The CONSTRAINT block (required for C-15; extended by C-21 to 4 types) names at minimum 5 prohibited operation types, where the fifth closes the artifact-write phase: no artifact path construction, no artifact file write, or equivalent language prohibiting any A-4 WRITE phase activity during S-0. The C-21 minimum of 4 ops (lookup, selection, mock generation, body generation) is necessary but not sufficient. A complete adversarial-coverage CONSTRAINT must close all production phases in sequence: discovery (lookup), decision (selection), output generation (mock generation), content production (body generation), and artifact output (path construction / file write). A CONSTRAINT with only the C-21 minimum 4 does not satisfy this criterion. Source: R5 V-01 boundary -- a 4-op CONSTRAINT (passing C-21) still leaves an adversarial path where artifact path construction or file writing begins before S-0 completes. The 5-op form closes this final phase gap by prohibiting all phases of artifact production, not only the generation phases.

"""

v5_body = v5_body.replace(
    '\n---\n\n## Common Failure Modes',
    c23_c24 + '\n---\n\n## Common Failure Modes'
)

# 4. Append 3 new failure trap rows at end of table
new_traps = (
    '| C-11 awarded as C-22 | C-22 | FLAG table has 4 rows that functionally cover all 5 cases (C-11 passes) but no dedicated row separates HS-critical-tier=1 from the non-critical catch-all (C-22 fails). C-11 functional coverage is a necessary but not sufficient condition for C-22 structural row separation. Scorer who reads C-11 as sufficient proof of C-22 makes an implication error. V-02 (R5) confirmed this trap: 4-row table with wildcard-in-cell passes C-11 and C-16 but fails C-22. |\n'
    '| C-17 awarded as C-19 | C-19 | S-0 has a terminal gate naming S-1 (C-17 passes) but the preamble gate at entry position was removed (C-19 fails). Scorer who reads C-17 as sufficient for C-19 makes an implication error -- a single gate form satisfies C-17 but not C-19. The reader scanning S-0 top-to-bottom still encounters the resolution table before any gate language. V-03 (R5) confirmed this trap. |\n'
    '| C-15 count satisfies C-21 | C-21 | CONSTRAINT names exactly 3 op types satisfying the C-15 minimum (lookup, selection, mock generation), but body generation is absent (C-21 fails). C-15 is a necessary but not sufficient precondition for C-21 -- op count is the discriminator. V-01 (R5) confirmed this trap: C-15 pass + C-21 fail = 106/112. |\n'
)

v5_body = v5_body.rstrip() + '\n' + new_traps

# 5. Build v6 header
v6_header = """# mock-ns Rubric

---

### v6 (2026-03-16) -- R5 boundary patterns promoted to aspirational criteria

**Two new criteria from R5:**

| ID | Text | Source |
|----|------|--------|
| C-23 | Preamble gate is the opening sentence of S-0, preceding all resolution logic including the parameter table | R5 V-03 position signal |
| C-24 | CONSTRAINT names 5+ prohibited op types, adding artifact path construction or file write to the C-21 minimum | R5 V-01 phase-completeness signal |

**Three new failure traps** encoding R5 canary results:
- "C-11 awarded as C-22" -- V-02 (R5): C-11 passes (5 cases functionally covered in 4-row table) but C-22 fails (dedicated tier=1 row absent). C-11 functional coverage is a necessary but not sufficient condition for C-22 structural coverage.
- "C-17 awarded as C-19" -- V-03 (R5): C-17 passes (terminal gate names S-1) but C-19 fails (preamble gate absent). A scorer reading C-17 as sufficient proof of C-19 makes an implication error.
- "C-15 count satisfies C-21" -- V-01 (R5): C-15 passes (3 op types named) but C-21 fails (body generation absent). C-15 is a necessary but not sufficient precondition for C-21.

**Scoring**: max rises from 108 to **112** (16 aspirational x 2 pts = 32; 50 + 30 + 32 = 112). V-05 (R4, previously 108/108) now scores 108/112; a R5-convergent variate with both new criteria scores 112/112.

---

"""

# 6. Get the prior version history from v5 (everything before ## Scoring)
v5_history = v5[:split]
# Strip the "Written to..." artifact line at the very top of v5 (it's not real history)
# v5 starts with "Written to `simulations/quest/rubrics/mock-ns-rubric-v5-2026-03-16.md`."
# We want the version history blocks only
# Find first "### v5" line
history_start = v5_history.index('**v5 summary')
v5_history_clean = v5_history[history_start:]

full_v6 = v6_header + v5_history_clean + v5_body

with open('C:/src/sim/simulations/quest/rubrics/mock-ns-rubric-v6-2026-03-16.md', 'w', encoding='utf-8') as f:
    f.write(full_v6)

print('Written OK')
print('Length:', len(full_v6))
print('C-23 present:', '### C-23' in full_v6)
print('C-24 present:', '### C-24' in full_v6)
print('trap C-11/C-22:', 'C-11 awarded as C-22' in full_v6)
print('trap C-17/C-19:', 'C-17 awarded as C-19' in full_v6)
print('trap C-15/C-21:', 'C-15 count satisfies C-21' in full_v6)
print('scoring 112:', '**112**' in full_v6)
print('R5 discriminator notes in C-11:', 'R5 discriminator' in full_v6)
