"""Build trace-state-rubric-v8 from v7 + Round 9 excellence signals (C-22, C-23, C-24)."""

with open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v7-2026-03-15.md', 'r', encoding='utf-8') as f:
    v7 = f.read()

# Split at the Essential Criteria section -- replace everything before it
essential_start = v7.index('## Essential Criteria')
body = v7[essential_start:]

# Update aspirational point value in section header
body = body.replace(
    '## Aspirational Criteria (10 pts total -- 0.71 pts each)',
    '## Aspirational Criteria (10 pts total -- 0.59 pts each)'
)

HEADER = """`trace-state-rubric-v8-2026-03-15.md` written.

---

## What changed in v8

**Three new aspirational criteria extracted from Round 9:**

**C-22 . Explicit handoff declaration** -- from V-01 (Role Sequence: HANDOFF DECLARATION)
V-01's defining structural feature: a HANDOFF DECLARATION section explicitly marks the transition
from the inventory role ([D]) to the trace operator role ([T]). The section names the transferring
role, the receiving role, the artifacts being transferred (STATE DECLARATIONS, OPERATION
DECLARATIONS), and the acceptance conditions [T] must confirm before proceeding. This is distinct
from C-17 (role-differentiated constraints, which assigns duties) and from C-10/C-20 (gates, which
block sections): the HANDOFF DECLARATION is a formal transfer-of-ownership event, not a checkpoint
or a duty assignment. V-02 and V-03 do not include this section and fail C-22.

**C-23 . Numbered prose inventory declarations** -- from V-02 (Output Format: Numbered Prose Inventories)
V-02's defining structural feature: each state and operation in the inventory phase is declared as
a numbered prose entry with an inline definitional clause ("1. OPEN -- The initial state entered on
ticket creation..."), not as a bare table row. The definition accompanies the declaration at the
inventory site rather than requiring the reader to infer meaning from the name alone. The transition
trace itself remains tabular (C-08 is preserved); the innovation applies only to the declaration
phase. This is distinct from C-01/C-02 (which require inventory completeness) and C-14 (which
requires binding): C-23 requires each declared item to carry an inline prose definition at the
declaration site. V-01 and V-03 do not use numbered prose inventories and fail C-23.

**C-24 . Uniform declarative IS-phrasing register** -- from V-03 (Phrasing Register: Declarative IS Framing)
V-03's defining structural feature: every prohibition, gate condition, vocabulary closure, and
violation binding uses a consistent IS / IS NOT / ARE NOT declarative register throughout the
document ("TRANSITION TABLE IS BLOCKED", "prose IS NOT VALID primary output", "vocabulary IS
FROZEN", "prohibition IS NOT WAIVABLE", "blank response IS a C7 violation"). The declarative
register frames every constraint as a positive assertion about the state of the document rather
than an imperative directed at a recipient. This is distinct from C-12 (hard-stop phrasing, which
requires specific forward-blocking language in at least two sections) and C-13 (prose prohibition,
which requires an explicit ban on narrative output): C-24 requires the IS/IS NOT register to be
applied consistently across ALL constraint phrasing in the document -- not just in selected
sections. V-01 and V-02 use standard imperative register and fail C-24.

---

## Scoring update (17 aspirational criteria)

| | C-22 | C-23 | C-24 | Aspirational | Composite |
|--|------|------|------|-------------|-----------|
| R9 V-01 | PASS | FAIL | FAIL | 15/17 x 10 = 8.82 | 98.82 |
| R9 V-02 | FAIL | PASS | FAIL | 15/17 x 10 = 8.82 | 98.82 |
| R9 V-03 | FAIL | FAIL | PASS | 15/17 x 10 = 8.82 | 98.82 |

All three Golden under v8. New ceiling is 100.00 -- requires all 17 aspirational criteria
simultaneously; not yet achieved by any variant.

**Scoring changes:**
- 17 aspirational criteria, 0.59 pts per PASS, 0.29 pts per PARTIAL (~10 pts total)
- Formula: `aspirational_pass/17 x 10`
- New ceiling: 17/17 = 10.00 pts aspirational, composite 100.00 -- not yet achieved
- R9 V-01, V-02, V-03 all score 15/17 (98.82)

**New ceiling:** No variant achieves all 17 aspirational criteria simultaneously.
A synthesis variant must combine C-22 (HANDOFF DECLARATION) + C-23 (numbered prose
inventories) + C-24 (IS-phrasing register) alongside all 14 prior aspirational criteria.

---

## Scoring verification against Round 9

Aspirational criteria use 0.59 pts per PASS, 0.29 pts per PARTIAL (rounding to 2dp).
Exact formula: `aspirational_pass/17 x 10`.

| Variant | C-22 | C-23 | C-24 | Aspirational (v8) | Composite |
|---------|------|------|------|-------------------|-----------|
| R9 V-01 | PASS | FAIL | FAIL | 15/17 x 10 = 8.82 | 98.82 |
| R9 V-02 | FAIL | PASS | FAIL | 15/17 x 10 = 8.82 | 98.82 |
| R9 V-03 | FAIL | FAIL | PASS | 15/17 x 10 = 8.82 | 98.82 |

R9 V-01 full (v8): C-08 PASS, C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS,
C-14 PASS, C-15 PASS, C-16 PASS, C-17 PASS, C-18 PASS, C-19 PASS, C-20 PASS,
C-21 PASS, C-22 PASS, C-23 FAIL, C-24 FAIL = 15 PASS. 15/17 x 10 = 8.82. Composite: 98.82. Golden.

R9 V-02 full (v8): C-08 PASS, C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS,
C-14 PASS, C-15 PASS, C-16 PASS, C-17 PASS, C-18 PASS, C-19 PASS, C-20 PASS,
C-21 PASS, C-22 FAIL, C-23 PASS, C-24 FAIL = 15 PASS. 15/17 x 10 = 8.82. Composite: 98.82. Golden.

R9 V-03 full (v8): C-08 PASS, C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS,
C-14 PASS, C-15 PASS, C-16 PASS, C-17 PASS, C-18 PASS, C-19 PASS, C-20 PASS,
C-21 PASS, C-22 FAIL, C-23 FAIL, C-24 PASS = 15 PASS. 15/17 x 10 = 8.82. Composite: 98.82. Golden.

All three variants are Golden under v8. No variant achieves 100.00.

---

"""

C22_C23_C24 = """
### C-22 . Explicit handoff declaration
- **Weight**: aspirational
- **Category**: accountability
- **Text**: A named HANDOFF DECLARATION section explicitly marks the transition
  from the inventory role ([D]) to the trace operator role ([T]). The section
  names the transferring role, the receiving role, the artifacts being
  transferred (STATE DECLARATIONS, OPERATION DECLARATIONS, or equivalent), and
  the acceptance conditions [T] must confirm before proceeding. R9 V-01 achieves
  this as a distinct section positioned after the inventories and before the
  first gate. The HANDOFF DECLARATION is a formal transfer-of-ownership event:
  not a gate (which blocks a section), not a ROLES assignment (which assigns
  duties), but a named moment at which accountability shifts from the declaring
  role to the executing role and is explicitly acknowledged.
- **Pass condition**: A HANDOFF DECLARATION section (or equivalently named block)
  is present. It names the transferring role, the receiving role, and the
  artifacts transferred. It requires an explicit acceptance or confirmation from
  the receiving role before the trace phases begin. A ROLES block that assigns
  duties without marking the transfer event does not satisfy this criterion
  (that is C-17). A gate that blocks a section without naming roles or artifacts
  does not satisfy this criterion (that is C-10 / C-20).

---

### C-23 . Numbered prose inventory declarations
- **Weight**: aspirational
- **Category**: structure
- **Text**: Each state and operation in the inventory phase is declared as a
  numbered prose entry with an inline definitional clause, not as a bare name
  in a table row or a name-only bullet. The inline definition accompanies the
  declaration at the inventory site, making each item self-documenting without
  reference to any other section. R9 V-02 achieves this with entries of the
  form "1. OPEN -- The initial state entered on ticket creation when all required
  fields are populated." The transition trace itself remains tabular (C-08 is
  preserved); the prose declarations apply only to the inventory phase.
  This is distinct from C-01/C-02 (which require completeness of the inventory)
  and C-14 (which requires binding between inventory and later tables): C-23
  requires each declared item to carry an inline definitional clause at its
  declaration site.
- **Pass condition**: Every state and every operation in the inventory sections
  has a numbered entry with at least one inline definitional clause (not just a
  name). The clause distinguishes the item from others by meaning, not merely
  by name. A table of names with no inline definition does not satisfy this
  criterion. A glossary appended after the inventory does not satisfy this
  criterion; the definition must appear at the declaration site.

---

### C-24 . Uniform declarative IS-phrasing register
- **Weight**: aspirational
- **Category**: format
- **Text**: All prohibitions, gate conditions, vocabulary closures, and violation
  bindings throughout the document use a consistent IS / IS NOT / ARE NOT
  declarative register. The declarative register frames every constraint as a
  positive assertion about the state of the document ("TRANSITION TABLE IS
  BLOCKED", "prose IS NOT VALID primary output", "vocabulary IS FROZEN",
  "prohibition IS NOT WAIVABLE", "blank response IS a C7 violation") rather
  than an imperative directed at a recipient. R9 V-03 achieves this by applying
  IS-framing uniformly across CONSTRAINT MATRIX entries, gate language,
  VOCABULARY CLOSED, and the INVENTORY CHALLENGE violation binding.
  This is distinct from C-12 (hard-stop phrasing, which requires at least two
  forward-blocking phrases but does not require a uniform register) and C-13
  (prose prohibition, which requires an explicit ban on narrative output but
  not a uniform register): C-24 requires IS / IS NOT phrasing to be applied
  consistently across ALL constraint and gate language in the document.
- **Pass condition**: Every gate condition, every prohibition in the constraint
  registry, the vocabulary closure declaration, and the violation binding at the
  INVENTORY CHALLENGE all use IS / IS NOT / ARE NOT declarative phrasing. At
  least five structurally distinct sites in the document exhibit IS-register
  phrasing. A document that uses IS-framing in some sections but imperative
  phrasing in others is PARTIAL. A document that applies IS-framing exclusively
  throughout all constraint-bearing sections is PASS.
"""

v8 = HEADER + body + C22_C23_C24

with open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v8-2026-03-15.md', 'w', encoding='utf-8') as f:
    f.write(v8)

lines = len(v8.splitlines())
print(f'v8 written: {len(v8)} chars, {lines} lines')
print('C-22 present:', '### C-22' in v8)
print('C-23 present:', '### C-23' in v8)
print('C-24 present:', '### C-24' in v8)
print('formula 0.59:', '0.59 pts each' in v8)
print('scoring table:', '15/17 x 10 = 8.82' in v8)
