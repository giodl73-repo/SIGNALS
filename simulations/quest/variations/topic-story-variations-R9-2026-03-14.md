Written to `simulations/quest/rubrics/topic-story-rubric-v9-variations-R9-2026-03-15.md`.

---

# R9 Variations -- `topic-story` (Round 9, v9 Rubric)

**New criteria**: C-31, C-32, C-33
**R8 baseline**: All 5 variations scored 100 on C-01--C-30. All three new criteria were unmet across all R8 variations.

---

## Variation Map

| Variation | Axis | C-31 | C-32 | C-33 | Hypothesis |
|-----------|------|------|------|------|------------|
| **V-01** | Output format (C-31) | PASS | FAILS | FAILS | Promoting invariant from bold+blockquote to `### Checklist Design Invariant` heading with named `**Repair operation**:` formula satisfies C-31 by giving both a scan anchor and a quotable rewrite path |
| **V-02** | Output format (C-33) | FAILS | FAILS | PASS | Adding a "Structural constraint" column to the field inventory converts the table from a field registry into a constraint registry; anti-consolidation is auditable from the inventory alone |
| **V-03** | Phrasing register (C-32, lean imperative) | FAILS | PASS | FAILS | C-32 fires when the anti-consolidation directive is co-located with the fields in Section 4 -- register is orthogonal, lean throughout; extends R8 V-03's orthogonality proof to C-32 |
| **V-04** | Output format + lifecycle emphasis (C-31 + C-32) | PASS | PASS | FAILS | Heading-block invariant enforces at pre-checklist time; section directive enforces at field-entry time; two structurally distinct enforcement moments without conflict |
| **V-05** | Output format + inertia framing (C-31 + C-32 + C-33) | PASS | PASS | PASS | All three satisfied without conflict; C-33 and C-32 are not redundant -- C-33 enables inventory-only audit, C-32 enables at-write enforcement; V-05 is "full structural saturation" |

---

## Structural Changes Per Variation

**V-01 only** (C-31): `**Checklist Design Invariant**` bold block → `### Checklist Design Invariant` heading with `**Rule**:` + `**Repair operation**: Rewrite any failing item as: "Does [Section name] include the label \`**[field name]**:\`?"`

**V-02 only** (C-33): Axis table gains a third column; inertia-framing row annotated "Required separate in S4 (anti-consolidation -- C-29). Constraint auditable from this table alone."

**V-03 only** (C-32): Section 4 opens with explicit `**Anti-consolidation directive**:` block before the field list, naming the violation form (`**Position delta**:`) and stating it fails C-29.

**V-04** (C-31 + C-32): V-01's heading block + V-04's section directive in Section 4 before the fields. Deliberately no inventory annotation.

**V-05** (C-31 + C-32 + C-33): V-01's heading block + three-column inventory table + Section 4 directive that cross-references the inventory annotation ("see inventory Structural Constraint column for the authoritative rule").
