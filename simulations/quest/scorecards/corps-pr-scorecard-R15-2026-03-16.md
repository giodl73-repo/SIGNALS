## corps-pr — Round 15 Scoring (v13 Rubric)

### Baseline Context

R14 V-04 scores 33/36 aspirational against v13: all essential (5/5) and recommended (3/3) pass; C-42 already passes; C-43 and C-44 fail. All five R15 variations inherit the same essential/recommended baseline, so the differential is entirely in C-42/C-43/C-44.

---

## Per-Variation Evaluation

### C-42 Audit (all variations)

All five variations share an identical C2 RESULT block template:

```
[derive terminal verdict from per-field lines above -- write exactly one:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]
```

Both named conditional antecedents ("All five PRESENT" and "Any ABSENT") are present as distinct lines — the failure-path verdict form is pre-committed in the template. **C-42: PASS for all five.**

---

### V-01 — Output Format: Prohibition Directive

**C-43 audit — PASS**

Format rules (lines 335–344):
```
Prohibition [C-43]: the inline-cell-label path (inline labels within a single Description
cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
```

All four required elements:
- (a) Closed path named by structural description: "inline labels within a single Description cell" ✓
- (b) Lower criterion named: "satisfies C-38" ✓
- (c) Superseding criterion named: "C-40 noncompliant" ✓
- (d) Explicit "do not use" directive: "do not use it" ✓

**C-44 audit — FAIL**

The format rules still offer the path before prohibiting it:
```
Alternative form (C-38 compliant): "[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
Description cell -- both labels independently matchable.
Prohibition [C-43]: the inline-cell-label path ... do not use it.
```

C-44 requires the template to *eliminate* alternative paths satisfying only a lower structural level. Describing the path as an "Alternative form (C-38 compliant)" — even immediately before a prohibition — means the path is offered, then taken away by note. The template has not eliminated it; it has labeled it forbidden while still showing it as an option. **C-44: FAIL.**

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-44) | 34/36 | 9.44 |
| **Composite** | | **99.44** |

---

### V-02 — Lifecycle Emphasis: Template Path Elimination (No Prohibition Text)

**C-43 audit — FAIL**

Format rules contain no prohibition text. The "Alternative form" entry is gone, but no cross-criterion prohibition replaces it — no closed-path description, no criterion IDs, no "do not use" directive. C-43 requires all four elements to be present in the template. Absence of the path is not the same as an explicit prohibition. **C-43: FAIL.**

**C-44 audit — PASS**

The structural enforcement levels section states: "no inline-cell alternative path" for C-40. The format rules offer only the column-header form; no alternative path for C-40's table-column level criterion remains. The declaration (C-41) correctly assigns C-40 at table-column level, and the template is now consistent with that declaration. **C-44: PASS.**

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-44) | 34/36 | 9.44 |
| **Composite** | | **99.44** |

---

### V-03 — Phrasing Register: CLOSED PATHS in Structural Declaration

**C-43 audit — PASS**

Pipeline declaration carries an explicit CLOSED PATHS block:
```
Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
```

All four elements:
- (a) Closed path: "inline-cell-label 'or' path ... in a single Description cell" ✓
- (b) Lower criterion: "satisfies C-38" ✓
- (c) Superseding criterion: "C-40 (table-column level) supersedes C-38" ✓
- (d) "do not use it" ✓

**C-43: PASS.**

**C-44 audit — FAIL**

Despite the declaration prohibition, the format rules still offer the alternative path:
```
Alternative form (C-38 compliant): "[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
Description cell -- both labels independently matchable.
Note: the alternative form satisfies C-38 but does not satisfy C-40...
See pipeline declaration CLOSED PATHS for the prohibition.
```

C-44 tests *declaration-to-template consistency*, not whether a prohibition exists. The declaration declares C-40 at table-column level (C-41 satisfied); the template still offers the C-38-level path and merely points to the declaration for the prohibition. That is inconsistency, not elimination. **C-44: FAIL.**

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-44) | 34/36 | 9.44 |
| **Composite** | | **99.44** |

---

### V-04 — Combination: Inline Prohibition + Template Elimination

**C-43 audit — PASS**

Format rules:
```
  Prohibition [C-43]: the "or" path (inline labels within a single Description cell)
  satisfies C-38 but is C-40 noncompliant -- do not use it.
```

All four elements present: (a) path by structural description ✓, (b) C-38 ✓, (c) C-40 ✓, (d) "do not use it" ✓. **C-43: PASS.**

**C-44 audit — PASS**

The "Alternative form" entry is gone from the format rules — only the column-header form is offered. The structural enforcement levels section explicitly notes "no inline-cell 'or' path" for C-40, and adds:
```
Declaration-template consistency [C-44]: no alternative path satisfying only a lower
structural level is offered in the template for any criterion family declared above.
```

C-41 declares C-40 at table-column level; the template no longer offers the C-38-level alternative. Declaration and template are consistent. **C-44: PASS.**

Phase C exit item (6) is updated to name both C-43 and C-44 as gate requirements, making violations Phase C exit failures. Phase D entry explicitly cites C-43 and C-44. The compliance chain is traceable.

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-44) | 36/36 | 10.00 |
| **Composite** | | **100.00** |

---

### V-05 — Combination: CLOSED PATHS in Declaration + Template Elimination

**C-43 audit — PASS**

Pipeline declaration CLOSED PATHS section:
```
Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form...satisfies the table-column level requirement.
```

All four elements: (a) closed path named ✓, (b) C-38 ✓, (c) C-40 ✓, (d) "do not use it" ✓. **C-43: PASS.**

**C-44 audit — PASS**

Pipeline declaration has an explicit Declaration-template consistency section:
```
Declaration-template consistency [C-44]:
  C-40 is declared at the table-column level above. The template offers only the
  column-header form for F-01 Description schema -- no alternative path satisfying only
  C-38's block level remains in the template. Declaration and template are consistent.
```

Format rules offer only the column-header form; the alternative path is absent. C-41 declaration (table-column level for C-40) is consistent with the template. **C-44: PASS.**

Key structural difference from V-04: both C-43 and C-44 are auditable from the pipeline declaration block alone — a reviewer does not need to read format rules to verify either criterion. The CLOSED PATHS section covers C-43; the Declaration-template consistency section covers C-44. Both are named structural properties of the declaration.

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-44) | 36/36 | 10.00 |
| **Composite** | | **100.00** |

---

## Summary Scorecard

| Var | C-42 | C-43 | C-44 | Asp Pass | Asp Score | Composite |
|-----|------|------|------|----------|-----------|-----------|
| V-01 | PASS | PASS | FAIL | 34/36 | 9.44 | 99.44 |
| V-02 | PASS | FAIL | PASS | 34/36 | 9.44 | 99.44 |
| V-03 | PASS | PASS | FAIL | 34/36 | 9.44 | 99.44 |
| V-04 | PASS | PASS | PASS | 36/36 | 10.00 | **100.00** |
| V-05 | PASS | PASS | PASS | 36/36 | 10.00 | **100.00** |

**Rank**: V-04 = V-05 > V-01 = V-03 > V-02

---

## Differential Analysis: V-04 vs V-05

Both score 100. The structural difference:

| Property | V-04 | V-05 |
|----------|------|------|
| C-43 prohibition location | Inline in format rules | Pipeline declaration CLOSED PATHS block |
| C-44 compliance location | Format rules (path gone) + structural levels note | Declaration-template consistency section |
| Auditing C-43 | Must read format rules | Read declaration only |
| Auditing C-44 | Must read format rules + structural levels | Read declaration only |
| Prohibition and enforcement co-located | Yes, at format-rules level | Yes, at declaration level |

V-05 is the more structurally elevated form — both C-43 and C-44 are auditable from the pipeline declaration without reading format rules. This represents one additional degree of audibility, though the rubric v13 does not assign a score differential for it.

---

## Excellence Signals

From V-04 and V-05 (the 36/36 variations):

**1. Prohibition co-located with enforcement** (V-04 pattern): When the C-43 prohibition appears in the same section that eliminates the path, a single read verifies both the prohibition's presence (C-43) and the path's absence (C-44) without cross-section navigation.

**2. Structural elevation of prohibition** (V-05 pattern): Moving the C-43 prohibition into the pipeline declaration as a named CLOSED PATHS block makes it auditable from the declaration alone — the same read that verifies C-41 structural levels also verifies C-43 closed paths and C-44 consistency. Structural compliance becomes a property of the declaration rather than a property of format rules.

**3. Named Declaration-template consistency section** (both): Adding an explicit "Declaration-template consistency [C-44]" subsection names the alignment requirement as a first-class structural element — not inferrable from individual output elements, but declared. This transforms C-44 from an inferred property into a stated invariant.

**4. Phase C exit item updated to gate C-43 and C-44** (both): By naming C-43 and C-44 in Phase C exit condition (6), their violation becomes a phase-gate failure, not only a format issue — the same enforcement mechanism used for C-36 (ordering violation blocks Phase D) now applies to prohibition presence and template consistency.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["prohibition co-located with enforcement at the same structural level makes C-43 and C-44 verifiable in a single read without cross-section navigation", "structural elevation of prohibition into the pipeline declaration as a named CLOSED PATHS block makes both C-43 and C-44 auditable from the declaration alone without reading format rules", "explicit Declaration-template consistency subsection in structural enforcement levels transforms C-44 from an inferred output property into a stated declaration invariant"]}
```
