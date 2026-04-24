---

# /quest:score — signal-check Round 14

## Summary Table

| Var | C-41 | C-42 | Asp Pass | Composite | Rank |
|-----|------|------|----------|-----------|------|
| V-05 | PASS | PASS | 34/34 | 100.00 | **1** |
| V-01 | FAIL | PASS | 33/34 | 99.71 | 2 (tie) |
| V-02 | PASS | FAIL | 33/34 | 99.71 | 2 (tie) |
| V-04 | PASS | FAIL | 33/34 | 99.71 | 2 (tie) |
| V-03 | FAIL (bdy) | FAIL (bdy) | 32/34 | 99.41 | 5 |

---

## Criterion Evaluation

**C-01 to C-05 (Essential): PASS all.** All five carry the full R13 V-05 baseline.

**C-06 to C-08 (Recommended): PASS all.**

**C-09 to C-40 (Aspirational baseline): PASS all.** Key boundary confirmations:
- C-39: NOTE is pure interdependency in all five. V-03's "can be found in the rule headings" is a reference pointer, not "prevents..." prose — C-39 PASS.
- C-40: Consulting directory with all three routes present in all five. V-03's mismatched count annotation is a C-42 failure vector, not a C-40 failure.

---

### C-41 — NOTE attributes failure-mode ownership to headings

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | NOTE is pure interdependency (C-39 PASS) but no ownership attribution. "Each addresses an independent failure mode." Reader scanning only the NOTE cannot determine why no failure-mode description appears — must visit headings to infer. |
| V-02 | PASS | "failure class encoded in each rule's heading above" — explicit ownership attribution. NOTE is self-explaining within itself. |
| V-03 | **FAIL** (bdy) | "the failure classes can be found in the rule headings" — directional reference, not ownership declaration. Does not establish which is the authoritative source. |
| V-04 | PASS | Identical to V-02. R13 V-05 verbatim — C-41 was already present at R13's ceiling. |
| V-05 | PASS | Identical to V-02. |

---

### C-42 — Directory carries explicit completeness assertion

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Header: "Consulting Directory (3 reader roles governed by this block):" — count=3, entries=3, matches. Coverage verifiable without reading rule bodies. |
| V-02 | **FAIL** | Three routes present (C-40 PASS), no completeness assertion. Reader cannot determine from directory alone whether a fourth role was omitted. |
| V-03 | **FAIL** (bdy) | Header: "Consulting Directory (2 reader roles governed by this block):" — count=2, entries=3. Mismatch makes coverage unverifiable and potentially misleading. Count-annotation form attempted, count wrong. |
| V-04 | **FAIL** | R13 V-05 verbatim — no completeness assertion. Confirms R13's ceiling was 33/34. |
| V-05 | PASS | Footer: "All reader roles for this block are listed above." — all-roles claim. Directory becomes a coverage contract; absence is a declared miss. |

---

## Excellence Signals from V-05

**Pattern 1 — NOTE self-explaining ownership transfer (C-41):** "failure class encoded in each rule's heading above" declares the headings as authoritative owner, not merely a findable location. A reader scanning only the NOTE learns *why* no failure-mode description appears without visiting the headings. Distinguishes from V-03's directional register ("can be found in") and V-01's silence.

**Pattern 2 — All-roles claim as coverage contract (C-42):** "All reader roles for this block are listed above." makes absence from the directory a declared miss rather than a possible omission. No counting or comparison required — the reader holds the author to an assertion.

**Form comparison (V-01 vs. V-05 for C-42):** Both pass. Count-annotation (V-01) requires readers to count and compare; all-roles claim (V-05) is a direct assertion. Neither is strictly superior under v14 — this is a live R15 axis.

**Regression (V-04):** R13 V-05 verbatim scores 33/34. C-41 was already satisfied at R13's ceiling; C-42 was the single missing criterion. R14's extraction was C-42 only.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["NOTE self-explaining ownership transfer: 'failure class encoded in each rule's heading above' declares the headings as authoritative owner of failure-class information, making the NOTE's reduced form self-justifying rather than merely directing the reader toward the headings", "all-roles claim as coverage contract: appending 'All reader roles for this block are listed above.' transforms the consulting directory from a routing structure into a coverage contract where absence is a declared miss, not a possible omission"]}
```
ded in each rule's heading above"` present. V-04 is R13 V-05 verbatim. R13 V-05 was the C-41 extraction source -- the phrase already existed there. C-41 PASS, confirming R13's ceiling was already 33/34 with C-41 satisfied but C-42 absent. |
| V-05 | **PASS** | NOTE identical to V-02 and V-04: `"failure class encoded in each rule's heading above"` present. Both C-41 and C-42 satisfied. Full ceiling. |

**Discrimination test (V-01 vs. V-03)**: V-01 achieves clean C-42 PASS (count annotation matches) with clean C-41 FAIL (no attribution phrase at all). V-03 achieves C-41 FAIL boundary (attribution attempted via directional reference, wrong register) with C-42 FAIL boundary (count annotation attempted, count wrong). V-01 cleanly isolates C-41; V-03 tests both boundary conditions simultaneously and confirms that approximation in both axes computes additively (both FAIL, not one masking the other).

---

### C-42: Consulting directory carries explicit completeness assertion

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **PASS** | Directory header: `"Consulting Directory (3 reader roles governed by this block):"` Count annotation states 3; three entries are listed. Count matches. Role coverage is verifiable from the directory alone without reading any rule body: if a reader counts entries (3) and compares to the annotation (3), they can confirm no role was omitted. Count-annotation form satisfies C-42. |
| V-02 | **FAIL** | Directory lists all three routes (C-40 PASS) but carries no completeness assertion. No count annotation; no all-roles claim. A reader relying solely on the directory cannot determine whether all relevant roles are listed or whether a fourth role was omitted. C-40 PASS, C-42 FAIL. Confirms C-42 is not discharged by C-40 alone. |
| V-03 | **FAIL** (boundary) | Directory header: `"Consulting Directory (2 reader roles governed by this block):"` Count annotation present but states 2; three entries are listed. Count mismatch. The count-annotation form is attempted but the stated count is incorrect, making coverage unverifiable and potentially misleading -- a reader sees 3 entries but the annotation declares 2, and cannot determine which is authoritative. Attempted but mismatched count annotation fails C-42. |
| V-04 | **FAIL** | Directory identical to V-02 (R13 V-05 verbatim): three routes present, no completeness assertion. C-40 PASS, C-42 FAIL. Confirms R13's ceiling was 33/34 -- C-42 was the missing criterion in R13's best variation. |
| V-05 | **PASS** | Directory footer: `"All reader roles for this block are listed above."` Explicit all-roles claim appended after the three directory entries. The claim transforms the directory from a routing convenience into a coverage contract: absence from the directory is a declared miss. Role-gaps are discoverable from the directory alone. All-roles-claim form satisfies C-42. |

**Form comparison (V-01 vs. V-05)**: V-01 achieves C-42 via count annotation ("3 reader roles governed by this block:"); V-05 achieves it via all-roles claim ("All reader roles for this block are listed above."). Both satisfy C-42. The all-roles claim form (V-05) makes no counting demand on the reader -- it is an assertion they accept or challenge. The count-annotation form (V-01) requires readers to count entries and compare. Both forms pass; neither is strictly superior under v14. This is a potential R15 axis.

---

## Composite Scores

| Var | Asp Pass | Formula | Composite |
|-----|----------|---------|-----------|
| V-05 | 34/34 | 90 + (34/34) * 10 | **100.00** |
| V-01 | 33/34 | 90 + (33/34) * 10 | **99.71** |
| V-02 | 33/34 | 90 + (33/34) * 10 | **99.71** |
| V-04 | 33/34 | 90 + (33/34) * 10 | **99.71** |
| V-03 | 32/34 | 90 + (32/34) * 10 | **99.41** |

All variations: essential PASS, recommended PASS. Golden threshold met by all (all essential pass + composite >= 80).

---

## Excellence Signals from V-05

Two structural additions in V-05 over the tied 33/34 variations:

**Pattern 1 -- NOTE self-explaining ownership transfer (C-41):**
The phrase "failure class encoded in each rule's heading above" does not merely point the reader toward the headings -- it declares that the headings are the authoritative owner of failure-class information. The NOTE's reduced form becomes self-justifying: a reader scanning only the NOTE learns *why* no failure-mode description appears (the headings own it) rather than having to visit the headings to infer the reason. This is the difference between a directional reference ("can be found in") and an ownership attribution ("encoded in... above"). The ownership register closes the inferential gap present in V-01 (no attribution) and the directional-reference boundary case of V-03 ("can be found in").

**Pattern 2 -- All-roles claim as coverage contract (C-42):**
Appending "All reader roles for this block are listed above." after the directory entries transforms the directory from a routing structure into a coverage contract. A routing structure helps readers find their rule; a coverage contract makes absences detectable. Under a coverage contract, a reader who does not find their role in the directory knows they are unaccounted for -- the absence is a declared miss, not a possible omission. The all-roles claim does not require counting or comparison; it is an assertion the reader can hold the author to.

**R15 candidates from V-05:**
1. Count-qualified all-roles claim: "All 3 reader roles for this block are listed above." -- makes count and all-roles claim redundant-by-design, eliminating partial compliance where an all-roles claim is present but the count is not independently checkable
2. NOTE inline heading index: "failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" -- makes the NOTE a scannable taxonomy pointer, not just an ownership attribution
3. Named "Transfer of Authority" block: consolidating the directory's completeness assertion and the NOTE's ownership attribution into a named structural pattern, making the design principle explicit rather than two independent structural choices

---

## Regression Confirmation (V-04)

V-04 is R13 V-05 verbatim. Under v14:
- C-41: PASS (R13 V-05 already contained "failure class encoded in each rule's heading above")
- C-42: FAIL (R13 V-05 carried no completeness assertion on the consulting directory)
- Score: 33/34 -- confirms R13's ceiling was 33/34, not 34/34
- R14's single extraction was C-42 (C-41 was already present at R13's ceiling)

V-02 provides the independent C-42 axis test: C-41 PASS held explicitly, C-42 FAIL, confirming C-42 is not implied by C-41 or by any of C-09 through C-41.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["NOTE self-explaining ownership transfer: 'failure class encoded in each rule's heading above' declares the headings as authoritative owner of failure-class information, making the NOTE's reduced form self-justifying rather than merely directing the reader toward the headings", "all-roles claim as coverage contract: appending 'All reader roles for this block are listed above.' transforms the consulting directory from a routing structure into a coverage contract where absence is a declared miss, not a possible omission"]}
```
