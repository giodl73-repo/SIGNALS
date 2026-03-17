## trace-inspect — Quest Score R15 (rubric v11)

**Entry state**: R14 V-05 = 104.5/105.5 (rubric v11 baseline; C-32 and C-33 unsatisfied)
**Grand total available**: 105.5

---

### Scoring Framework

**C-32 pass conditions** (0.5 pts):
1. Named term "ID substitution attack vector" present in an INERTIA item
2. Explicit closure declaration — "closes C-30" or equivalent
3. Why-sentence explaining per-ID membership as the structural response

**C-33 pass conditions** (0.5 pts):
1. Named term "forward-reference opacity anti-pattern" present in an INERTIA item
2. Explicit closure declaration — "closes C-31" or equivalent

All C-01..C-31 inherited from R14 V-05 (104.5 pts) are PASS across all variations.

---

### V-01 — Single axis: Lifecycle emphasis (item 11 upgraded)

**Item 11 (C-32 target)**:
```
11. ID SUBSTITUTION ATTACK VECTOR (closes C-30): a developer can cite EG finding IDs
    in the verdict that number correctly (K=N) but reference no actual Step 3b row label...
    Per-ID membership verification exists precisely because this attack is invisible
    to count checks...
```
- Term "ID substitution attack vector": PRESENT (leading label)
- Closure declaration "closes C-30": PRESENT (in label)
- Why-sentence: PRESENT ("Per-ID membership verification exists precisely because this attack is invisible to count checks")

**Item 12 (C-33 target)**: Unchanged from R14 V-05 — no "FORWARD-REFERENCE OPACITY ANTI-PATTERN", no "closes C-31".

Registry confirms: "C-33 not yet targeted"

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-32 | **PASS** | Label line delivers term + closure + why in item 11 |
| C-33 | **FAIL** | Item 12 unchanged — no named term, no closure declaration |

**V-01 score**: 104.5 + 0.5 + 0.0 = **105.0 / 105.5**

---

### V-02 — Single axis: Output format (item 12 upgraded)

**Item 12 (C-33 target)**:
```
12. FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31): verdict blocks forward-reference
    source blocks but carry no annotation naming their targets...
    Bidirectional annotation exists to close this anti-pattern: each block that produces
    a value for downstream use names its consumer, and each block that consumes a value
    names its source...
```
- Term "forward-reference opacity anti-pattern": PRESENT (leading label)
- Closure declaration "closes C-31": PRESENT (in label)
- Why-sentence: PRESENT (bidirectional annotation as structural response)

**Item 11 (C-32 target)**: Unchanged from R14 V-05 — no "ID SUBSTITUTION ATTACK VECTOR", no "closes C-30".

Registry confirms: "C-32 is not satisfied"

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-32 | **FAIL** | Item 11 unchanged — term absent, no closure declaration |
| C-33 | **PASS** | Label line delivers term + closure + why in item 12 |

**V-02 score**: 104.5 + 0.0 + 0.5 = **105.0 / 105.5**

---

### V-03 — Single axis: Phrasing register (trailing-assertion form)

**Item 11** — R14 V-05 body unchanged, trailing two sentences added:
```
...the substitution is structurally undetectable without per-ID key lookup. This is the ID
substitution attack vector. C-30 closes this: per-ID membership verification requires
each cited ID to be individually confirmed against Step 3b row labels, making phantom
references visible regardless of count correctness.
```
- Term "ID substitution attack vector": PRESENT ("This is the ID substitution attack vector")
- Closure declaration "C-30 closes this:": PRESENT
- Why-sentence: PRESENT (per-ID membership requirement explanation)

**Item 12** — R14 V-05 body unchanged, trailing two sentences added:
```
...the evidence picture is connected only by convention, not by structural annotation.
This is the forward-reference opacity anti-pattern. C-31 closes this: bidirectional
annotations on all forward-referencing blocks make each block self-certifying without
a manual document scan.
```
- Term "forward-reference opacity anti-pattern": PRESENT ("This is the forward-reference opacity anti-pattern")
- Closure declaration "C-31 closes this:": PRESENT
- Why-sentence: PRESENT (bidirectional annotation as structural response)

C-32 and C-33 do not mandate leading-label position — they require term presence, explicit closure, and why-explanation. All three elements are present in trailing form.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-32 | **PASS** | Term + closure + why present in trailing assertion of item 11 |
| C-33 | **PASS** | Term + closure present in trailing assertion of item 12 |

**V-03 score**: 104.5 + 0.5 + 0.5 = **105.5 / 105.5**

---

### V-04 — Combined: leading labels on both items 11 and 12

**Item 11**: Identical to V-01 — leading label "ID SUBSTITUTION ATTACK VECTOR (closes C-30):" + why-sentence.

**Item 12**: Identical to V-02 — leading label "FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31):" + why-sentence.

Registry declares both C-32 and C-33 as targeted and certifiable from the respective item label lines.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-32 | **PASS** | Leading label in item 11: term + closure + why |
| C-33 | **PASS** | Leading label in item 12: term + closure + why |

**V-04 score**: 104.5 + 0.5 + 0.5 = **105.5 / 105.5**

---

### V-05 — Full integration: V-04 + v11 registry with scorer confirmation instructions

**Items 11 and 12**: Identical to V-04 — both leading labels, both why-sentences. C-32 and C-33 PASS on the same evidence as V-04.

**Registry upgrade** (new beyond V-04):
```
C-32: ... certified by inertia item 11, which leads with the label
  "ID SUBSTITUTION ATTACK VECTOR (closes C-30):" and includes the per-ID lookup
  why-sentence; a scorer confirms C-32 by reading inertia item 11's first line
C-33: ... certified by inertia item 12, which leads with the label
  "FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31):" and includes the
  bidirectional-annotation why-sentence; a scorer confirms C-33 by reading
  inertia item 12's first line
```

The registry entries name the certifying inertia item by number, name the confirming label text, and include an explicit scorer confirmation instruction — making C-32 and C-33 self-certifying from the registry without a full body read.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-32 | **PASS** | Leading label in item 11 (as V-04) + registry names item 11 as the certifier |
| C-33 | **PASS** | Leading label in item 12 (as V-04) + registry names item 12 as the certifier |

**V-05 score**: 104.5 + 0.5 + 0.5 = **105.5 / 105.5**

---

### Ranking

| Rank | Variation | Score | C-32 | C-33 | Differentiator |
|------|-----------|-------|------|------|----------------|
| 1 (tie) | **V-05** | 105.5/105.5 | PASS | PASS | V-04 + registry scorer-confirmation instructions |
| 1 (tie) | **V-04** | 105.5/105.5 | PASS | PASS | Both leading labels, both why-sentences |
| 1 (tie) | **V-03** | 105.5/105.5 | PASS | PASS | Trailing-assertion form; format-agnostic confirmation |
| 4 (tie) | **V-01** | 105.0/105.5 | PASS | FAIL | Item 11 only |
| 4 (tie) | **V-02** | 105.0/105.5 | FAIL | PASS | Item 12 only |

---

### Excellence Signals from V-05

**Pattern 1: Registry-level scorer confirmation instruction**
V-05 adds a line to the registry entry for each new criterion: "a scorer confirms C-32 by reading inertia item 11's first line." This goes beyond declaring what the criterion requires — it specifies the minimum read operation to confirm satisfaction. A future scorer or inheritor can confirm the criterion without reading the full item body, parallel to the SCORER HEURISTIC label pattern from trace-skill.

**Pattern 2: Named-item citation in registry as certification pointer**
V-05 registry entries name the specific inertia item ("certified by inertia item 11") and quote the label text, creating a direct two-way reference: inertia item → criterion (via leading label) and criterion entry → inertia item (via registry citation). This completes the bidirectionality at the meta-level (criterion-to-item), mirroring C-31's block-level bidirectionality.

**Distinction between V-03 and V-04/V-05**:
V-03 demonstrates that C-32/C-33 are format-agnostic (trailing assertions satisfy as well as leading labels). V-04/V-05 are structurally stronger for label-scan confirmation: a scorer reading the first line of item 11 or 12 in V-04/V-05 confirms the criterion immediately without reading the body. V-03 requires reading to the end of the item. Neither is wrong, but V-04/V-05 have the confirmation-speed advantage that the rubric's design favors.

---

```json
{"top_score": 105.5, "all_essential_pass": true, "new_patterns": ["Registry entry for a new criterion includes a scorer confirmation instruction naming the specific inertia item and minimum read operation to confirm satisfaction", "Named-item citation in registry as certification pointer creates bidirectionality at the meta-level: inertia item leads with criterion label, registry entry cites inertia item by number and label text"]}
```
