## Round 16 Scorecard — discover-competitors-alt

**Rubric:** v16 (35 aspirational criteria, C-09–C-43)
**Per-aspirational weight:** 10/35 = 0.2857 pts
**Max composite:** 100

---

## Scoring Key

| Band | Essential (C-01–05) | Recommended (C-06–08) | Aspirational (C-09–C-43) |
|------|--------------------|-----------------------|--------------------------|
| Weight | 12 pts each × 5 = 60 | 10 pts each × 3 = 30 | 0.2857 pts each × 35 = 10 |

---

## V-01 — Prose Architecture Block (R15 V-04 Form)

**Axis:** All four C-42 elements present in flowing prose. No checklist structure.

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | C0 section and description precede any competitor row — inherited from R15 V-05 baseline |
| C-02 | 3+ named competitors with threat levels | PASS | Three or more named competitors with HIGH/MEDIUM/LOW tags — inherited |
| C-03 | C0 at row 0 in competitive map | PASS | Native markdown table, C0 as first row — inherited |
| C-04 | Grounded findings | PASS | Each finding references a named competitor row by table label — inherited |
| C-05 | AMEND section present and non-empty | PASS | AMEND table with 3+ rows — inherited |

**Essential subtotal: 60 / 60**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Mechanism-level inertia reasoning | PASS | TOKEN mechanism tied to specific C0 behavior — inherited |
| C-07 | Web-verified competitive claim with inline citation | PASS | At least one inline WebSearch citation within a competitor entry — inherited |
| C-08 | AMEND with input-to-output pairs | PASS | 3+ rows, each naming input change and output effect — inherited |

**Recommended subtotal: 30 / 30**

### Aspirational Criteria

C-09 through C-42 all PASS — V-01 inherits the full R15 V-05 baseline, which established all 34 prior aspirational criteria. Only C-43 is new this round.

| ID | Score | Evidence |
|----|-------|----------|
| C-09 | PASS | Cross-dimensional whitespace finding references both competitive map and focus lens simultaneously |
| C-10 | PASS | Findings reference named competitor rows — duplicate of C-04 in aspirational slot |
| C-11 | PASS | TOKEN inertia mechanism referenced by name in downstream findings |
| C-12 | PASS | At least one AMEND entry addresses inertia stability |
| C-13 | PASS | Domain-adaptive TOKEN committed as portable identifier |
| C-14 | PASS | Every AMEND entry addresses stability |
| C-15 | PASS | TOKEN pre-declared before C0 description begins |
| C-16 | PASS | Every AMEND entry includes verdict + evidence |
| C-17 | PASS | TOKEN embeds at least one domain-specific term |
| C-18 | PASS | DOMAIN-TERMS artifact committed as separate step before TOKEN declaration |
| C-19 | PASS | TOKEN is literal first output — no conditionals precede it |
| C-20 | PASS | AMEND schema enumerates all four component names |
| C-21 | PASS | GATE-0 labeled unconditional; GATE-1 named as first conditional |
| C-22 | PASS | AMEND schema component names are domain-neutral |
| C-23 | PASS | Pre-execution gate manifest enumerates all gates with execution-mode labels |
| C-24 | PASS | Manifest is native markdown table outside code fence |
| C-25 | PASS | TOKEN named in every gate's output specification |
| C-26 | PASS | Each gate has dedicated REQUIRED OUTPUTS block |
| C-27 | PASS | REQUIRED OUTPUTS block replaces completion conditions entirely |
| C-28 | PASS | Each REQUIRED OUTPUTS block is native markdown table |
| C-29 | PASS | Each REQUIRED OUTPUTS table includes TOKEN-required column with committed value |
| C-30 | PASS | Bracket-notation `[TOKEN]` substitution rule declared for column headers |
| C-31 | PASS | GATE-0 REQUIRED OUTPUTS retains `[TOKEN] required?` template form with propagation declaration row |
| C-32 | PASS | Manifest includes TOKEN-propagation column declaring per-gate inheritance state |
| C-33 | PASS | Manifest TOKEN-propagation cells use "Declaration site" / "Substitution/inheritance site" verbatim |
| C-34 | PASS | TOKEN-PROPAGATION ARCHITECTURE block present before manifest table |
| C-35 | PASS | Manifest TOKEN-propagation column header uses `[TOKEN] propagation` bracket-notation |
| C-36 | PASS | Manifest column and GATE-0 REQUIRED OUTPUTS table each independently self-contained |
| C-37 | PASS | C-33 + C-34 + C-35 simultaneously satisfied |
| C-38 | PASS | Architecture block explicitly names both manifest column and GATE-0 table as targets |
| C-39 | PASS | Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim |
| C-40 | PASS | GATE-0 REQUIRED OUTPUTS contains dedicated propagation contract row distinct from TOKEN commitment row |
| C-41 | PASS | C-36 and C-37 simultaneously satisfied |
| C-42 | PASS | Architecture block contains all four C-42 elements: both artifact names and both verbatim phrases — readable from prose without consulting other artifacts |
| **C-43** | **FAIL** | Architecture block is a prose paragraph. All four C-42 elements are present and readable, but no checklist structure exists. A reader cannot verify completeness by item count — must parse prose to confirm all four elements are present. "Individually-itemized checklist entries" requires structural enumeration; prose sentences with enumerable content do not satisfy the form requirement. |

**Aspirational subtotal: 34 / 35 → 34 × 0.2857 = 9.714 pts**

### V-01 Composite: 60 + 30 + 9.714 = **99.714**

---

## V-02 — 3-Item Partial Checklist (Element 4 Collapsed into Item 1)

**Axis:** Numbered checklist with 3 items. Item 1 names the manifest column AND contains "Substitution/inheritance site" verbatim in its prose. Item 2 names GATE-0's REQUIRED OUTPUTS table. Item 3 supplies "Declaration site" verbatim. Count = 3.

### Essential and Recommended Criteria

Identical to V-01 — all PASS. **Subtotal: 90 / 90**

### Aspirational Criteria

C-09 through C-41 all PASS — inherited from R15 V-05 baseline.

| ID | Score | Evidence |
|----|-------|----------|
| C-42 | PASS | All four C-42 elements readable from the architecture block: item 1 supplies the manifest column name AND "Substitution/inheritance site" verbatim in its content prose; item 2 supplies the GATE-0 table name; item 3 supplies "Declaration site" verbatim. Operative test: all four elements confirmable without consulting other artifacts — passes. Content completeness is not conditioned on form. |
| **C-43** | **FAIL** | Checklist has 3 items, not 4. The fourth C-42 element ("Substitution/inheritance site") is embedded in item 1's prose rather than occupying a dedicated fourth item. A reader verifying completeness by item count finds 3 — the count test fails at 3 < 4. To confirm the fourth element is present, the reader must parse item 1's content prose. "Individually-itemized" requires one element per item; collapsing two elements into one item's prose violates this even when all four elements are content-present. This tests whether the "individually-itemized" requirement enforces element-per-item discipline — it does. C-43 FAIL on count. |

**Aspirational subtotal: 34 / 35 → 9.714 pts**

### V-02 Composite: 60 + 30 + 9.714 = **99.714**

---

## V-03 — 4 Unlabeled Bullet Points (Count = 4, No Per-Item Labels)

**Axis:** Architecture block uses four bullet points, each containing exactly one C-42 element. Count = 4. But no per-item label headers (e.g., "Named target 1 —", "Verbatim phrase 1 —"). Element identity is encoded in content, not structure.

### Essential and Recommended Criteria

Identical to V-01 — all PASS. **Subtotal: 90 / 90**

### Aspirational Criteria

C-09 through C-41 all PASS — inherited from R15 V-05 baseline.

| ID | Score | Evidence |
|----|-------|----------|
| C-42 | PASS | All four C-42 elements readable from the architecture block — four bullet items, each containing exactly one element. Content completeness is not conditioned on label presence. |
| **C-43** | **FAIL** | Count = 4 items ✓. Each item contains exactly one C-42 element ✓. But no per-item label headers are present. C-43 requires "explicitly labeled, individually-itemized checklist entries." "Explicitly labeled" is a distinct constraint from "individually-itemized": a reader cannot verify which element an item carries by consulting only the item's label — there is no label; the element identity is encoded in the content. To identify what each bullet carries, the reader must parse the bullet's prose. A reader scanning labels alone cannot verify completeness without reading content. V-03 satisfies count-verifiability but fails label-verifiability. The "explicitly labeled" requirement is independently enforced from "individually-itemized." C-43 FAIL on label. |

**Aspirational subtotal: 34 / 35 → 9.714 pts**

### V-03 Composite: 60 + 30 + 9.714 = **99.714**

---

## V-04 — Standard 4-Item Labeled Checklist (R15 V-05 Form Promoted)

**Axis:** Architecture block uses a 4-item numbered checklist with explicit per-item label headers: "Named target 1 — manifest TOKEN-propagation column:", "Named target 2 — GATE-0's REQUIRED OUTPUTS table:", "Verbatim phrase 1 — 'Declaration site':", "Verbatim phrase 2 — 'Substitution/inheritance site':". Count = 4. Labels are independent of content.

### Essential and Recommended Criteria

Identical to V-01 — all PASS. **Subtotal: 90 / 90**

### Aspirational Criteria

C-09 through C-42 all PASS — inherited from R15 V-05 baseline.

| ID | Score | Evidence |
|----|-------|----------|
| C-42 | PASS | All four C-42 elements present and readable from the architecture block. Each element occupies a dedicated labeled checklist item — content completeness and structural completeness both confirmed. |
| **C-43** | **PASS** | Count = 4 items ✓. Each item explicitly labeled with a header that identifies the element by category and role ("Named target 1 —", "Verbatim phrase 2 —") ✓. A reader can verify completeness by item count (4 = all four elements) and by label scan (labels identify which element each item carries without reading content). "Explicitly labeled" and "individually-itemized" both satisfied. Structural form is a checklist, not prose. C-43 PASS — maximum-reliability form of C-42. |

**Aspirational subtotal: 35 / 35 → 10.000 pts**

### V-04 Composite: 60 + 30 + 10.000 = **100.000**

---

## V-05 — 4-Item Labeled Checklist + Count Declaration Header

**Axis:** Identical to V-04 plus a bold `C-43 COMPLIANCE — 4 ITEMS` count declaration above the checklist. Count pre-declared in header before any item is read.

### Essential and Recommended Criteria

Identical to V-01 — all PASS. **Subtotal: 90 / 90**

### Aspirational Criteria

C-09 through C-42 all PASS — inherited from R15 V-05 baseline.

| ID | Score | Evidence |
|----|-------|----------|
| C-42 | PASS | All four C-42 elements present and readable from the architecture block — same as V-04. |
| **C-43** | **PASS** | All V-04 conditions satisfied: count = 4 ✓, per-item labels ✓, individually-itemized ✓. Additionally, the pre-declared count header `C-43 COMPLIANCE — 4 ITEMS` makes the 4-element requirement machine-verifiable from the header alone — a reader need not count items to confirm compliance. This does not create any new rubric criterion in v16, but provides a reliability increment over V-04: model-compliance probability is higher across multiple runs because the count is declared structurally, not inferred. No regression risk on adjacent criteria — the header is additive, not replacing any structural element. C-43 PASS. |

**Aspirational subtotal: 35 / 35 → 10.000 pts**

### V-05 Composite: 60 + 30 + 10.000 = **100.000**

---

## Rankings

| Rank | Variation | Aspirational | Composite |
|------|-----------|-------------|-----------|
| 1 (tie) | **V-04** — 4-item labeled checklist | 35/35 | **100.000** |
| 1 (tie) | **V-05** — 4-item labeled checklist + count header | 35/35 | **100.000** |
| 3 (tie) | V-01 — prose architecture block | 34/35 | 99.714 |
| 3 (tie) | V-02 — 3-item partial checklist | 34/35 | 99.714 |
| 3 (tie) | V-03 — 4 unlabeled bullets | 34/35 | 99.714 |

---

## Decisive Question Answers

**Q1: Do all three failure modes score identically at 99.714?**
Yes. V-01 (prose), V-02 (3-item count failure), and V-03 (4-item label failure) all score 99.714. C-43 is atomic — no partial credit for being "close" to the structural form. Prose with enumerable sentences, partial checklists, and unlabeled bullets each fail on a distinct axis, but the criterion score is binary: 0.2857 or 0.

**Q2: Does the rubric distinguish V-02's count failure from V-03's label failure?**
Yes — as distinct C-43 failure modes, not as different scores. Both fail C-43 and both score 99.714. The rubric does not assign partial credit within C-43. The operative distinction: V-02 fails on "individually-itemized" (element-per-item discipline — fourth element collapsed into another item's prose); V-03 fails on "explicitly labeled" (label-independent identification — unlabeled bullets require content parsing to identify elements). Two distinct requirements, two distinct failure modes, same criterion score outcome.

**Q3: Are V-04 and V-05 equivalent at 35/35?**
Equivalent at the criterion level — both score C-43 PASS and 100.000 composite. V-05's count pre-declaration header provides a model-compliance reliability advantage: the requirement is declared structurally before items are enumerated, reducing drift risk across repeated runs. This matters for robustness but is not a rubric-level differentiator in v16. No regression risk: the header is additive and does not conflict with any existing structural requirement.

---

## Excellence Signals (V-04 / V-05)

**What made the top-scoring form better:**

1. **Four-element completeness structurally enforced, not content-dependent.** V-04/V-05 use a labeled checklist where each C-42 element occupies exactly one independently-labeled item. Completeness is verifiable by item count (4) and label scan without reading any item's prose content. V-01's prose and V-03's unlabeled bullets both require prose parsing to confirm all four elements are present.

2. **"Explicitly labeled" and "individually-itemized" as independently satisfied constraints.** V-04 treats label presence and item-per-element discipline as two separate structural requirements, not one. The label identifies the element category; the item boundary separates elements. V-02 satisfies neither (count = 3, label absent for fourth element); V-03 satisfies one (count = 4) but not the other (no labels). V-04 satisfies both.

3. **V-05: Count pre-declaration as a reliability increment above the criterion floor.** The `C-43 COMPLIANCE — 4 ITEMS` header pre-declares the requirement before any item is enumerated, making compliance verifiable from the header alone. This does not create a new criterion but closes the drift path where a model satisfying C-43 in one run might produce 3 items in another. The count declaration is a self-enforcing structural contract.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Four-element checklist completeness is structurally enforced when each C-42 element occupies exactly one explicitly-labeled, independently-itemized checklist entry — count and label scan together make verification prose-free", "Explicitly-labeled and individually-itemized are independently satisfied constraints: label presence identifies element category by structure alone; item boundary separates elements from one another — both required simultaneously", "Count pre-declaration header above checklist commits the required item count as a structural artifact before enumeration begins, reducing model-compliance drift across runs without adding rubric overhead"]}
```
