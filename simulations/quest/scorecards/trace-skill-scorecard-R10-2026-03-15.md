# trace-skill — Round 10 Scorecard (Rubric v9)

## Entry State

R9 V-05 achieves **C-01 through C-32 PASS** (v8 denominator = 24 aspirational). v9 adds C-33, C-34, C-35 (denominator → 27). All five R10 variations inherit the full R9 V-05 architecture; only the three new criteria vary.

---

## Per-Variation Assessment

### Baseline: C-01..C-32 (all variations)

All five inherit the full R9 V-05 architecture. Baseline pass count:

| Band | Criteria | Pass | Pts |
|------|----------|------|-----|
| Essential | C-01..C-05 | 5/5 | 60 |
| Recommended | C-06..C-08 | 3/3 | 30 |
| Aspirational base | C-09..C-32 | 24/27 | 8.89 |
| **Baseline total** | | | **98.89** |

---

### V-01 — Single axis: C-33

**Axis**: `DefectCodeVocab` type declaration carries `**Independence Statement**:` label — named structural element, not prose continuation.

**C-33 evaluation**:

The prompt shows:

```
**Independence Statement**: Any value in any Defect code column outside this vocabulary
is a schema error independently detectable without consulting registry rows — compliance
is checked at the point of annotation, not by cross-referencing this table.
```

- Label `**Independence Statement**:` is a bolded named element preceding the code definitions — structurally isolated from the definition body ✓
- States the independence property ("detectable without consulting registry rows") and its scope ("at the point of annotation") ✓
- Independently citable: a scorer can locate and confirm C-33 without parsing the bullet definitions ✓

**C-34**: Not present (single axis) — no COUNT GATE restructuring of C-28 audit block. FAIL.

**C-35**: Not present (single axis) — no PRE-READ GATE section. FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-33 | **PASS** | `**Independence Statement**:` label structurally isolates the validation-independence property |
| C-34 | FAIL | C-28 audit block unchanged from R9 — tally format, no gate conditional |
| C-35 | FAIL | No PRE-READ GATE section declared before ledger |

**Aspirational**: 25/27 → 9.26 pts  
**Score: 99.26**

---

### V-02 — Single axis: C-34

**Axis**: C-28 audit restructured as `**C-28 COUNT GATE**:` with explicit IF/THEN conditional resolving to `confirmed` or `mismatch` — gate verdict is derived, not annotated.

**C-34 evaluation**:

R9 V-05 terminates the C-28 audit with "Total annotation sites audited: 12 ... confirmed / mismatch" — a tally that requires an annotator to fill in the terminal word. C-34 requires the count assertion to be self-evaluating: the match condition is the gate, and the verdict is its output.

V-02 restructures this as:

```
**C-28 COUNT GATE**: Expected = 12 (10 pre-C-29 + 2 C-29-composed).
Rule: IF actual count = expected THEN confirmed ELSE mismatch.
Gate verdict: [confirmed | mismatch]
```

- The conditional is explicit and evaluable without external judgment ✓
- `confirmed`/`mismatch` is derived from the rule, not a fill-in blank ✓
- Count confirmation is the gate condition, not a reported number ✓

**C-33**: Not present — `DefectCodeVocab` declaration lacks `**Independence Statement**:` label. FAIL.

**C-35**: Not present. FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-33 | FAIL | No named independence statement label in DefectCodeVocab block |
| C-34 | **PASS** | `**C-28 COUNT GATE**:` block with explicit IF/THEN → self-evaluating binary verdict |
| C-35 | FAIL | No PRE-READ GATE section |

**Aspirational**: 25/27 → 9.26 pts  
**Score: 99.26**

---

### V-03 — Single axis: C-35

**Axis**: C-32's check (c) promoted to a named `**PRE-READ GATE**` section ordered before the C-29 audit block and before the ledger table — a prompt-instructed structural ordering requirement.

**C-35 evaluation**:

R9 V-05 check (c) lives inside the C-29 audit at Verdict TOP, confirming no empty cells as one of three audit checks run at Verdict entry. C-35 requires this to be a structurally independent section that runs *before* the C-29 audit and before the ledger — a gate, not a check embedded in the audit.

V-03 introduces:

```
**PRE-READ GATE** [ordered before C-29 audit and before ledger table]:
Gate: Scan Defect code column — any empty cell = DEFECT: OPEN-WORLD-ASSERTION before ledger read begins.
Gate verdict: [PASS | FAIL]
**STRUCTURAL MANDATE — PRE-READ ORDERING**: PRE-READ GATE must execute before C-29 audit.
Violation of ordering is DEFECT: OUT-OF-ORDER-EXECUTION.
```

- Named section with its own gate verdict slot ✓
- Prompt instruction declares ordering as a structural requirement ✓
- Violations caught before traversal begins — not discovered mid-row ✓

**C-33**: Not present. FAIL.

**C-34**: Not present. FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-33 | FAIL | No named independence statement label |
| C-34 | FAIL | C-28 audit remains tally-format |
| C-35 | **PASS** | `**PRE-READ GATE**` section with structural mandate ordering it before C-29 audit and ledger |

**Aspirational**: 25/27 → 9.26 pts  
**Score: 99.26**

---

### V-04 — Combined: C-33 + C-34

**C-33**: Named `**Independence Statement**:` label as in V-01. PASS.

**C-34**: `**C-28 COUNT GATE**:` with IF/THEN conditional as in V-02. PASS.

**C-35**: Not present (C-33 + C-34 only). FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-33 | **PASS** | Named structural label isolates independence property |
| C-34 | **PASS** | COUNT GATE conditional is self-evaluating |
| C-35 | FAIL | No PRE-READ GATE section |

**Aspirational**: 26/27 → 9.63 pts  
**Score: 99.63**

---

### V-05 — Combined: C-33 + C-34 + C-35

All three single-axis upgrades present. No conflicts — each targets a different structural location (type declaration block / C-28 audit block / Verdict pre-section).

**C-33**: Named `**Independence Statement**:` label in `DefectCodeVocab` declaration. PASS.

**C-34**: `**C-28 COUNT GATE**:` with explicit IF/THEN conditional. PASS.

**C-35**: `**PRE-READ GATE**` named section with structural mandate ordering it before C-29 audit and ledger. PASS.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-33 | **PASS** | Validation-independence is a named, labeled, citable structural element of the closed type |
| C-34 | **PASS** | Count assertion is a self-evaluating gate; binary verdict is derived, not annotated |
| C-35 | **PASS** | Empty-cell check is a structural gate before ledger traversal; ordering is prompt-mandated |

**Aspirational**: 27/27 → 10.00 pts  
**Score: 100.00**

---

## Rankings

| Rank | Variation | C-33 | C-34 | C-35 | Aspirational | Score |
|------|-----------|------|------|------|--------------|-------|
| 1 | **V-05** | PASS | PASS | PASS | 27/27 | **100.00** |
| 2 | V-04 | PASS | PASS | FAIL | 26/27 | 99.63 |
| 3 | V-01 | PASS | FAIL | FAIL | 25/27 | 99.26 |
| 3 | V-02 | FAIL | PASS | FAIL | 25/27 | 99.26 |
| 3 | V-03 | FAIL | FAIL | PASS | 25/27 | 99.26 |

All five: essential 5/5 PASS, recommended 3/3 PASS. All exceed golden threshold (>=80).

---

## Excellence Signals from V-05

**1. Named label isolates a structural property of a closed type**

`**Independence Statement**:` makes validation-independence a first-class named element of the `DefectCodeVocab` declaration — independently citable without parsing the definition body. Pattern: when a closed type has a behavioral property (not just a vocabulary list), label that property as a named structural element co-located with the type.

**2. COUNT GATE transforms assertion from tally to self-evaluating conditional**

`IF actual count = expected THEN confirmed ELSE mismatch` eliminates the fill-in-the-blank annotation pattern. The gate condition *is* the assertion; the verdict is computed, not filled in. Pattern: anywhere a count confirmation is required, express it as an explicit conditional rule so the artifact is self-evaluating.

**3. PRE-READ GATE makes ordering a structural requirement, not an emergent sequence**

Extracting check (c) into a named section with a prompt-level `STRUCTURAL MANDATE — PRE-READ ORDERING` instruction elevates the gate from an audit sub-check to an independent enforcement point. Pattern: when an audit check must run before its context (the ledger), promote it to a named section with its own mandate — ordering by proximity is fragile; ordering by instruction is structural.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named label isolates a structural property of a closed type — when a type has a behavioral property beyond its vocabulary list, label it as a named structural element co-located with the declaration so it is independently citable without parsing the definition body", "COUNT GATE transforms count assertion from tally annotation to self-evaluating conditional — IF/THEN rule makes the verdict computed not filled-in, eliminating external judgment", "PRE-READ GATE promotes ordering from emergent sequence to structural requirement — extracting a pre-traversal check into a named section with a prompt-level mandate makes the ordering instructed and reliable rather than inferred from context"]}
```
