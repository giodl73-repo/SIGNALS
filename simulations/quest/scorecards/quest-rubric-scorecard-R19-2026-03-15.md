I now have all the information needed to score all five variations. Let me analyze each variation systematically.

---

# Round 19 Scoring — quest-rubric (v19)

**Rubric:** v19 (C-01–C-50, formula `(E/5 × 60) + (R/3 × 30) + (A/42 × 10)`)
**Baseline:** R18 V-04 passes all C-01–C-48 (40/42 for A component: C-49 FAIL, C-50 FAIL)
**Target criteria:** C-49 (FORMAT TEMPLATE with mandatory `[C-NN]` slot in Phase 8.5), C-50 (full per-span enumeration in STATUS QUO foil items)

---

## Criteria Reference (Target Zone)

| C-NN | Requirement |
|------|-------------|
| C-47 | Phase 8.5 failure-mode clause names at least one criterion ID (prose OK) |
| C-48 | STATUS QUO foil item names both passing and failing criteria (pass/fail pair) |
| C-49 | Phase 8.5 failure-mode clause governed by FORMAT TEMPLATE with mandatory `[C-NN]` slot — omission visible as unfilled placeholder, not silent prose gap |
| C-50 | Each STATUS QUO foil item enumerates **every** passing criterion in the per-span between consecutive failure points — no range notation, no partial subset |

---

## Per-Variation Evaluation

### V-01 — Lifecycle Emphasis (C-49 probe, C-50 ablated)

**Phase 8.5 analysis:**
The skill prompt installs `PER-NOTE FORMAT TEMPLATE` with the mandatory `[C-NN]` slot:
```
Absent this path, [C-NN] is unenforced at [gate name] entry.
```
A STOP condition blocks forward progress if the `[C-NN]` slot is omitted. The criterion ID is structurally enforced by the template slot — omission leaves a visible bracket.

**STATUS QUO analysis:**
Cumulative range notation preserved from R18 V-04. Foil items:
- `passes C-01 and C-02 while failing C-03` — span {C-01, C-02}: ✓ full-span (only 2 criteria in span)
- `passes C-01 through C-05 while failing C-06` — span should be {C-04, C-05}; cumulative range includes C-01–C-03: FAIL C-50
- `passes C-01 through C-08 while failing C-09` — span should be {C-07, C-08}: cumulative range: FAIL C-50
- `passes C-01 through C-12 while failing C-13` — span should be {C-10, C-11, C-12}: cumulative range: FAIL C-50

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-47 | PASS | Architecture A/B path notes name criterion IDs (C-43, C-44) in template output |
| C-48 | PASS | Foil items name both passing (range) and failing criteria |
| C-49 | **PASS** | FORMAT TEMPLATE with `[C-NN]` slot present; STOP blocks notes without slot filled |
| C-50 | **FAIL** | Three of four foil items use cumulative-from-start range notation, not per-span enumeration |
| C-01–C-46 | PASS | R18 V-04 baseline mechanisms preserved |

**A component:** 41/42 × 10 = **9.76**
**Composite:** 60 + 30 + 9.76 = **99.76**

---

### V-02 — Inertia Framing (C-50 probe, C-49 ablated)

**Phase 8.5 analysis:**
NON-REDUNDANCY DECLARATION written as prose paragraphs naming criterion IDs inline (`C-43 is unenforced`, `C-44 is unenforced`). No `PER-NOTE FORMAT TEMPLATE` heading. No `[C-NN]` slot structure. Criterion IDs present via prose instruction only.

**STATUS QUO analysis:**
Foil items use per-span explicit enumeration with inline span annotations:
- `passes C-01 and C-02 while failing C-03` (span from START to C-03: C-01, C-02) ✓
- `passes C-04 and C-05 while failing C-06` (span from C-03 to C-06: C-04, C-05) ✓
- `passes C-07, C-08, and C-09 while failing C-10` (span from C-06 to C-10: C-07, C-08, C-09) ✓
- `passes C-11 and C-12 while failing C-13` (span from C-10 to C-13: C-11, C-12) ✓

All foil items enumerate every criterion in the span, no gaps on the pass side.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-47 | PASS | Prose criterion IDs in Phase 8.5 notes (C-43, C-44 named) |
| C-48 | PASS | All foil items name both passing and failing criteria |
| C-49 | **FAIL** | No FORMAT TEMPLATE structure; criterion ID present in prose only, omission would be a silent prose gap |
| C-50 | **PASS** | All four foil items enumerate every criterion in the per-span; inline span annotations confirm completeness |
| C-01–C-46 | PASS | R18 V-04 baseline preserved |

**A component:** 41/42 × 10 = **9.76**
**Composite:** 60 + 30 + 9.76 = **99.76**

---

### V-03 — Output Format (C-50 via SPAN DEFINITION pre-step, C-49 ablated)

**Phase 8.5 analysis:**
Same as V-02 — criterion IDs named in prose, no FORMAT TEMPLATE. C-49 FAIL by the same logic.

**STATUS QUO analysis:**
A `SPAN DEFINITION` slot precedes each foil item. The builder must compute:
```
SPAN DEFINITION:
  Previous failure: [C-NN or START]
  Current failure:  [C-NN]
  Pass side (enumerate every criterion in span): [C-NN, C-NN, ...]
```
The foil item is then transcribed from the SPAN DEFINITION pass-side list. All four SPAN DEFINITION slots in the prompt show correct per-span computation:
- span {C-01, C-02} → `passes C-01 and C-02 while failing C-03` ✓
- span {C-04, C-05} → `passes C-04 and C-05 while failing C-06` ✓
- span {C-07, C-08, C-09} → `passes C-07, C-08, and C-09 while failing C-10` ✓
- span {C-11, C-12} → `passes C-11 and C-12 while failing C-13` ✓

SPAN DEFINITION forces span computation as a visible intermediate step — foil item omission is detectable as a SPAN DEFINITION gap, not just a foil-item content gap.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-47 | PASS | Criterion IDs in prose Phase 8.5 notes |
| C-48 | PASS | Foil items name both passing and failing criteria |
| C-49 | **FAIL** | No FORMAT TEMPLATE; criterion ID in prose only; same as V-02 for Phase 8.5 |
| C-50 | **PASS** | SPAN DEFINITION pre-step forces full-span computation; foil items transcribed from pass-side list; all spans correct |
| C-01–C-46 | PASS | R18 V-04 baseline preserved |

**A component:** 41/42 × 10 = **9.76**
**Composite:** 60 + 30 + 9.76 = **99.76**

---

### V-04 — Combined (Lifecycle + Inertia)

**Phase 8.5 analysis:**
FORMAT TEMPLATE from V-01 installed:
```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation...]
```
STOP blocks notes without `[C-NN]` slot filled. Template slot is structurally mandatory — omission produces visible bracket.

**STATUS QUO analysis:**
Per-span explicit enumeration from V-02 installed with inline span annotations. All four foil items:
- `passes C-01 and C-02 while failing C-03` (span: C-01, C-02) ✓
- `passes C-04 and C-05 while failing C-06` (span: C-04, C-05) ✓
- `passes C-07, C-08, and C-09 while failing C-10` (span: C-07, C-08, C-09) ✓
- `passes C-11 and C-12 while failing C-13` (span: C-11, C-12) ✓

Two mechanisms govern structurally distinct sections — no interference.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-47 | PASS | Template output names criterion IDs |
| C-48 | PASS | All foil items bidirectional |
| C-49 | **PASS** | FORMAT TEMPLATE with mandatory `[C-NN]` slot; STOP present |
| C-50 | **PASS** | Per-span enumeration with inline span annotations; all four spans complete |
| C-01–C-46 | PASS | R18 V-04 baseline preserved |

**A component:** 42/42 × 10 = **10.00**
**Composite:** 60 + 30 + 10.00 = **100.00**

---

### V-05 — Combined + Phrasing Register (ceiling form)

**Phase 8.5 analysis:**
FORMAT TEMPLATE present (same as V-04). Additionally, a **SLOT-FILL STOP** names two structurally distinct defect classes:
1. Unfilled `[C-NN]` bracket — template-production failure, detectable by string scan
2. Prose-only criterion-ID omission — criterion-ID omission failure, not bracket-visible

STOP enumerates compliant form: "Absent this path, C-43 is unenforced at Phase 9 entry."
Per-note STOP conditions co-located with each Architecture A/B note.

**STATUS QUO analysis:**
Per-span explicit enumeration present (same as V-04). Additionally, a **FULL-SPAN STOP** names two non-compliant forms:
1. Range notation (`C-04 through C-09 while failing C-10`) — fails because span completeness is not verifiable without counting
2. Partial subset (`C-04 and C-07 while failing C-10`) — fails because span has gaps

Compliant form example provided inline. STOP appears before foil items, not deferred to audit.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-47 | PASS | Template output names criterion IDs |
| C-48 | PASS | All foil items bidirectional; compliant form example confirms pair framing |
| C-49 | **PASS** | FORMAT TEMPLATE + SLOT-FILL STOP; two distinct defect classes named; higher defect-detection specificity than V-04 |
| C-50 | **PASS** | Per-span enumeration + FULL-SPAN STOP; range notation named as non-compliant form; subset named as non-compliant form; compliant form example inline |
| C-01–C-46 | PASS | R18 V-04 baseline preserved |

**A component:** 42/42 × 10 = **10.00**
**Composite:** 60 + 30 + 10.00 = **100.00**

---

## Ranking

| Rank | Variation | C-49 | C-50 | A component | Composite |
|------|-----------|------|------|-------------|-----------|
| 1 (ceiling) | **V-05** Combined + Phrasing register | PASS | PASS | 42/42 × 10 | **100.00** |
| 1 | **V-04** Combined | PASS | PASS | 42/42 × 10 | **100.00** |
| 3 | V-01 Lifecycle emphasis | PASS | FAIL | 41/42 × 10 | 99.76 |
| 3 | V-02 Inertia framing | FAIL | PASS | 41/42 × 10 | 99.76 |
| 3 | V-03 Output format | FAIL | PASS | 41/42 × 10 | 99.76 |

V-04 and V-05 tie at 100.00. V-05 is the ceiling form: SLOT-FILL STOP and FULL-SPAN STOP add defect-class declarations that V-04 lacks, enabling a reviewer to distinguish distinct failure modes without inferring them from the template structure alone.

---

## Excellence Signals

From V-05 (ceiling) vs V-04 (joint satisfiability) vs single-axis variations:

**ES-R19-1 (C-49 ceiling mechanism):** SLOT-FILL STOP names two structurally distinct failure modes — unfilled bracket (template-production failure, string-scannable) and prose-only omission (criterion-ID omission failure, content-readable only). Previous variations either had no template (C-49 FAIL) or had a template with a single STOP (V-04). The SLOT-FILL STOP makes the distinction between these two failure modes explicit in the prompt, allowing a reviewer to route a non-compliant note to the correct defect class without re-reading surrounding context.

**ES-R19-2 (C-50 ceiling mechanism):** FULL-SPAN STOP names two non-compliant forms by category — range notation and partial subset — with a compliant-form example inline. V-02 and V-03 achieve C-50 via instruction ("enumerate every criterion in the span") or intermediate computation step (SPAN DEFINITION). V-05 adds defect-class declaration: the non-compliant forms are identified by name before the foil items are written, converting the requirement from a behavioral instruction into a criterion-indexed verification claim.

**ES-R19-3 (orthogonality confirmation via V-04):** FORMAT TEMPLATE (Phase 8.5) and per-span enumeration (STATUS QUO) govern structurally and positionally distinct sections — joint activation in V-04 shows no interference. The two mechanisms can be installed independently (V-01 for C-49 only, V-02 for C-50 only) or jointly (V-04/V-05) without one suppressing the other. The single-axis variations confirm that each mechanism is individually load-bearing for its target criterion.

**ES-R19-4 (SPAN DEFINITION intermediate step, V-03):** V-03 demonstrates that a named intermediate computation step (SPAN DEFINITION) yields equivalent C-50 pass rates to V-02's direct instruction. The SPAN DEFINITION makes span computation a visible output artifact — omission is a SPAN DEFINITION gap, not just a foil-item content gap. This is structurally stronger than V-02's prose instruction but weaker than V-05's FULL-SPAN STOP (which names the non-compliant form, not just the compliant procedure). For practitioners: either mechanism achieves C-50; the FULL-SPAN STOP adds defect-detection specificity at the ceiling.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SLOT-FILL STOP names two structurally distinct C-49 defect classes — unfilled bracket (template-production failure, string-scannable) vs prose-only criterion-ID omission failure — reviewer can distinguish failure modes without re-reading prose context", "FULL-SPAN STOP names range notation and partial subset as non-compliant form categories by name with a compliant-form example inline — C-50 requirement expressed as defect-class declaration rather than behavioral instruction"]}
```
