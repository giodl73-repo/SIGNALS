## R15 Scorecard — topic:plan (v15 Rubric)

### Scoring Approach

R15 variations are built on the R14-V-05 ceiling (all C-09–C-47 established). The exercise isolates C-48/C-49 phrasing forms. Evaluation proceeds: verify essential+recommended pass uniformly, confirm C-43–C-47 inheritance, then score the two new axes.

---

## Per-Variation Evaluation

### V-01 — Lifecycle axis | inline halt | flat AND-conjunction

| Band | Criteria | Result | Note |
|------|----------|--------|------|
| Essential | C-01–C-05 | 5/5 PASS | All present; read strategy.md, full signal inventory, delta detection, typed proposals, visible gate |
| Recommended | C-06–C-08 | 3/3 PASS | Evidence citation, before/after diff, inertia justification all present |
| Aspirational C-09–C-42 | 34 criteria | 34 PASS | Inherited from R14-V-05 baseline |
| C-43 | Cell-exhaustive gate | PASS | Each mandatory column named in pass condition |
| C-44 | Numbered Gate-0 label | PASS | Header carries "Gate-0" identifier |
| C-45 | Schema-gate checklist atomicity | PASS | Each schema block is a separate labeled check item |
| C-46 | Pass-threshold annotation | PASS | "Gate-0 passes when all 11 confirmed" present |
| C-47 | Condition-line exhaustive cross-ref | PASS | Flat AND-conjunction names all 11 items individually |
| **C-48** | **Halt declaration** | **PASS** | Inline: "one STOP result halts Phase 1" |
| **C-49** | **Condition-line self-containment attestation** | **FAIL** | Condition line names all items but does not explicitly prohibit range inference or attest its own completeness |

**Aspirational pass: 40/41**
**Score: (5/5 × 60) + (3/3 × 30) + (40/41 × 10) = 60 + 30 + 9.76 = 99.76**

---

### V-02 — Output format axis | inline halt | grouped + attestation suffix

| Band | Criteria | Result | Note |
|------|----------|--------|------|
| Essential | C-01–C-05 | 5/5 PASS | All present |
| Recommended | C-06–C-08 | 3/3 PASS | All present |
| Aspirational C-09–C-42 | 34 criteria | 34 PASS | Inherited baseline |
| C-43 | Cell-exhaustive gate | PASS | Columns named |
| C-44 | Numbered Gate-0 label | PASS | Header carries "Gate-0" |
| C-45 | Schema-gate checklist atomicity | PASS | Per-schema items |
| C-46 | Pass-threshold annotation | PASS | Inline threshold + halt declared |
| C-47 | Condition-line exhaustive cross-ref | PASS | Grouped format still individually enumerates all 11 labels (cf. C-47 example: `schemas [A1]...[A8] all present + [B] + [C] + [D]`) |
| **C-48** | **Halt declaration** | **PASS** | Inline: "one STOP result halts Phase 1" |
| **C-49** | **Condition-line self-containment attestation** | **PASS** | Attestation suffix explicitly prohibits range inference and declares completeness |

**Aspirational pass: 41/41**
**Score: (5/5 × 60) + (3/3 × 30) + (41/41 × 10) = 60 + 30 + 10 = 100**

---

### V-03 — Phrasing register axis | labeled THRESHOLD field | grouped, no attestation

| Band | Criteria | Result | Note |
|------|----------|--------|------|
| Essential | C-01–C-05 | 5/5 PASS | All present |
| Recommended | C-06–C-08 | 3/3 PASS | All present |
| Aspirational C-09–C-42 | 34 criteria | 34 PASS | Inherited baseline |
| C-43 | Cell-exhaustive gate | PASS | Columns named |
| C-44 | Numbered Gate-0 label | PASS | Header carries "Gate-0" |
| C-45 | Schema-gate checklist atomicity | PASS | Per-schema items |
| C-46 | Pass-threshold annotation | PASS | `GATE-0 PASS THRESHOLD:` field present with N-item count |
| C-47 | Condition-line exhaustive cross-ref | PASS | Grouped form names all items individually |
| **C-48** | **Halt declaration** | **PASS** | Labeled field: "blocked by any single STOP result" |
| **C-49** | **Condition-line self-containment attestation** | **FAIL** | Items are individually named, but no explicit attestation that the line is self-contained or that range inference is prohibited |

**Aspirational pass: 40/41**
**Score: (5/5 × 60) + (3/3 × 30) + (40/41 × 10) = 60 + 30 + 9.76 = 99.76**

---

### V-04 — Combined LC+OF axis | labeled THRESHOLD field | grouped + attestation suffix

| Band | Criteria | Result | Note |
|------|----------|--------|------|
| Essential | C-01–C-05 | 5/5 PASS | All present |
| Recommended | C-06–C-08 | 3/3 PASS | All present |
| Aspirational C-09–C-42 | 34 criteria | 34 PASS | Inherited baseline |
| C-43 | Cell-exhaustive gate | PASS | Columns named |
| C-44 | Numbered Gate-0 label | PASS | Header carries "Gate-0" |
| C-45 | Schema-gate checklist atomicity | PASS | Per-schema items |
| C-46 | Pass-threshold annotation | PASS | `GATE-0 PASS THRESHOLD:` with N-count and halt trigger |
| C-47 | Condition-line exhaustive cross-ref | PASS | Grouped + attestation suffix; all items individually named |
| **C-48** | **Halt declaration** | **PASS** | Labeled field: "blocked by any single STOP result" |
| **C-49** | **Condition-line self-containment attestation** | **PASS** | Attestation suffix explicitly states no item may be inferred by range; completeness declared as structural invariant |

**Aspirational pass: 41/41**
**Score: (5/5 × 60) + (3/3 × 30) + (41/41 × 10) = 60 + 30 + 10 = 100**

---

### V-05 — Full ceiling | inline halt | flat AND + attestation suffix

| Band | Criteria | Result | Note |
|------|----------|--------|------|
| Essential | C-01–C-05 | 5/5 PASS | All present |
| Recommended | C-06–C-08 | 3/3 PASS | All present |
| Aspirational C-09–C-42 | 34 criteria | 34 PASS | Inherited baseline |
| C-43 | Cell-exhaustive gate | PASS | Columns named |
| C-44 | Numbered Gate-0 label | PASS | Header carries "Gate-0" |
| C-45 | Schema-gate checklist atomicity | PASS | Per-schema items |
| C-46 | Pass-threshold annotation | PASS | Inline threshold stated |
| C-47 | Condition-line exhaustive cross-ref | PASS | Flat AND-conjunction names all 11 labels individually |
| **C-48** | **Halt declaration** | **PASS** | Inline: "one STOP result halts Phase 1" |
| **C-49** | **Condition-line self-containment attestation** | **PASS** | Explicit attestation suffix: "reading this condition line enumerates all 11 items required; no item may be inferred by range" |

**Aspirational pass: 41/41**
**Score: (5/5 × 60) + (3/3 × 30) + (41/41 × 10) = 60 + 30 + 10 = 100**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Score | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 5/5 | 3/3 | 40/41 | **99.76** | YES |
| V-02 | 5/5 | 3/3 | 41/41 | **100** | YES |
| V-03 | 5/5 | 3/3 | 40/41 | **99.76** | YES |
| V-04 | 5/5 | 3/3 | 41/41 | **100** | YES |
| V-05 | 5/5 | 3/3 | 41/41 | **100** | YES |

**Rank**: V-02 = V-04 = V-05 (100) > V-01 = V-03 (99.76)

---

## Excellence Signals (from ceiling variations)

**From V-02, V-04, V-05 — the three distinguishing properties:**

1. **C-48 surface form is symmetric** — V-04 uses labeled-field (`GATE-0 PASS THRESHOLD: ... blocked by any single STOP result`) while V-02 and V-05 use inline annotation ("one STOP result halts Phase 1"). Both reach the ceiling. C-48 is satisfied by the presence of an explicit halt declaration, regardless of whether it appears as a labeled structural field or an inline clause in the annotation text. The two forms are interchangeable at the ceiling.

2. **C-49 attestation is independent of C-47 condition form** — V-02 reaches the ceiling with grouped item layout; V-05 with flat AND-conjunction. The attestation suffix ("reading this condition line enumerates all N items required; no item may be inferred by range") applies to both layouts. C-49 is not sensitive to whether items are presented in a single flat chain or grouped by type — it only requires the explicit self-containment declaration to be present in the condition line.

3. **The only remaining discriminator at this rubric level is the attestation suffix** — once halt declaration (C-48) is established, C-49 is the sole criterion separating 99.76 from 100. The gap is a single sentence in the condition line. Both V-01 and V-03 enumerate all items correctly (C-47 PASS, C-48 PASS) but omit the attestation, leaving completeness as an observable property rather than a declared invariant.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-48 surface form is symmetric: inline halt clause and labeled THRESHOLD field are equivalent for halt declaration — both reach the ceiling; the criterion tests presence not form", "C-49 attestation suffix is layout-independent: grouped and flat AND-conjunction condition lines both satisfy C-49 when the self-containment attestation is present — C-49 is not a layout property but a declared invariant property"]}
```
