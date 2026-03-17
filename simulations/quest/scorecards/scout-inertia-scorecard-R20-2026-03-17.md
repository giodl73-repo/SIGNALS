# scout-inertia Scorecard — Round 20

**Rubric**: v20 | **Denominator**: 52 | **Formula**: `aspirational_pass / 52 * 10`

---

## Score Summary

| V | Prior (50) | C-59 | C-60 | R20 Score |
|---|------------|------|------|-----------|
| **V-04** | 50/50 | PASS | PASS | **10.00** |
| **V-01** | 50/50 | FAIL | PASS | 9.81 |
| **V-02** | 50/50 | FAIL | PASS | 9.81 |
| **V-03** | 50/50 | PASS | FAIL | 9.81 |
| V-05 | 50/50 | FAIL | FAIL | 9.62 |

---

## Evaluation Notes

**V-01 (9.81) — C-59 FAIL**: `[BRIDGE COMMAND]:` appears identically at both Q3 and Q4 authoring positions — no Q-ID in either label. C-41 and C-58 pass (bridge-command form, positional segregation maintained). C-59 fails: same label at both positions, author cannot identify which artifact the label governs from the notation alone. C-60 passes: `[A-31]`/`[A-16]`/`[A-19]` citations unchanged.

**V-02 (9.81) — C-59 FAIL**: `[BRIDGE ACTOR COMMAND]:` at Q3, `[BRIDGE TRIGGER COMMAND]:` at Q4 — per-artifact, distinct, bridge-command form (C-41/C-58 pass). C-59 fails: `ACTOR` is the class-discriminating vocabulary from `FM->ACTOR BRIDGE`, not the artifact Q-ID `Q3`. Author must perform external class→Q-ID mapping; Q-ID absent from the authoring-point label. Second named C-59 failure form.

**V-03 (9.81) — C-60 FAIL**: `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:` intact (C-59 PASS). Domain-prefix labels stripped to `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` / `INERTIA THREAT CITATION RULE:` — no trailing `[A-NN]` citations. C-42/C-46/C-58 pass (vocabulary threading and positional segregation intact). C-60 fails: labels name structural roles but cite no specific rules; no bracket citation to scan without reading the label body.

**V-04 (10.00)** — R19 V-04 carried unchanged. Both C-59 and C-60 pass. Q-ID coherence loop fully closed at every structural position (authoring site via C-59 + interrogation via C-45/C-49 + conditional key via C-53 + return target via C-56). Domain-prefix labels fully audit-traceable via distinct trailing citations.

**V-05 (9.62) — C-59 FAIL + C-60 FAIL**: Generic `[BRIDGE COMMAND]:` at both bridge positions (C-59 FAIL — same mechanism as V-01) plus absent trailing citations on all three domain-prefix labels (C-60 FAIL — same mechanism as V-03). Both deductions apply independently; no precondition relationship between them. Double-fail floor confirmed at 50/52.

---

## Key Findings

**First three-way tie at 9.81** — V-01, V-02, V-03 score identically despite distinct failure mechanisms. Score alone cannot discriminate the two C-59 failure forms (generic vs class-vocab) from each other or from C-60 failure. Direct label inspection is required to identify mechanism.

**C-59 and C-60 additive independence confirmed** — V-05's 50/52 = two points below V-04, matching the sum of V-01's single-point deduction and V-03's single-point deduction. No interaction effect.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Three-way 9.81 tie (V-01, V-02, V-03) is the first round where three variations with distinct failure mechanisms score identically — two C-59 failure forms (generic label, class-vocab label) and one C-60 failure form (absent citations) each produce exactly one point deduction; score alone cannot discriminate the failure mechanism within each tied variation, requiring direct label inspection", "C-59 and C-60 confirmed as structurally independent — they address disjoint document positions (bridge authoring labels vs non-bridge domain-prefix labels) with no precondition relationship in either direction; V-05's 50/52 double-fail confirms both deductions apply additively with no interaction effect"]}
```
sing the Q-ID coherence loop.

---

### V-02 — C-59 fail via class-vocabulary bridge-command label

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-57 | PASS (carried) | R19 V-04 base; gate body unchanged |
| **C-41** | **PASS** | Two distinct per-artifact bracket commands: `[BRIDGE ACTOR COMMAND]:` at Q3 authoring position, `[BRIDGE TRIGGER COMMAND]:` at Q4 authoring position. One per artifact, labels are distinct. |
| **C-42** | **PASS** | `INERTIA THREAT` domain vocabulary threads through three non-bridge labels unchanged. |
| **C-46** | **PASS** | Compound domain-axis vocabulary unchanged. |
| **C-58** | **PASS** | `[BRIDGE ACTOR COMMAND]:` / `[BRIDGE TRIGGER COMMAND]:` use bridge-command vocabulary (BRIDGE prefix, not domain-prefix) at bridge positions. Domain-prefix labels confined to non-bridge positions. Positional segregation maintained. |
| **C-59** | **FAIL** | `[BRIDGE ACTOR COMMAND]:` at Q3 authoring position uses `ACTOR` — the class-discriminating vocabulary from the artifact type annotation `FM->ACTOR BRIDGE` — rather than the artifact Q-identifier `Q3`. `[BRIDGE TRIGGER COMMAND]:` at Q4 uses `TRIGGER` rather than `Q4`. Labels are per-artifact and distinct (satisfying C-41 and making each authoring point identifiable by class), but the Q-ID coherence chain is broken: Q3 appears in the gate interrogative, conditional key, and return target, but not in the authoring-point bracket label. An author scanning for `Q3` must perform an external mapping (`ACTOR` class corresponds to Q3) rather than recognizing Q3 directly from the label. This is the second named C-59 failure form: class-vocabulary labels distinguish artifacts by class but not by Q-ID. |
| **C-60** | **PASS** | Distinct trailing citations `[A-31]` / `[A-16]` / `[A-19]` on three vocabulary-threaded domain-prefix labels. Unchanged from R19 V-04. |

**Score: 51/52 × 10 = 9.81**

**C-59 failure mode isolated**: class-vocab form — `ACTOR`/`TRIGGER` are the discriminating class nouns but not the artifact Q-identifiers. Distinguished from V-01: V-01 labels are identical at both positions (author cannot even distinguish the two artifacts); V-02 labels are distinct (author can distinguish the artifacts by class) but Q-ID identity is absent. Both fail C-59 by a single point — the mechanism differs but the score impact is equal.

---

### V-03 — C-60 fail via absent trailing citations on domain-prefix labels

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-57 | PASS (carried) | R19 V-04 base; gate body and bridge-command labels unchanged |
| **C-41** | **PASS** | `[BRIDGE Q3 COMMAND]:` at Q3 section, `[BRIDGE Q4 COMMAND]:` at Q4 section. Unchanged from R19 V-04. |
| **C-42** | **PASS** | `INERTIA THREAT` vocabulary threads through three non-bridge domain-prefix labels: `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` / `INERTIA THREAT CITATION RULE:`. Citations removed but vocabulary threading intact — C-42 evaluates threading, not trailing citations. |
| **C-46** | **PASS** | Compound domain-axis vocabulary present: `INERTIA THREAT` (domain prefix) + structural-role axis. Citations are not a component of C-46's compound-vocabulary requirement. |
| **C-58** | **PASS** | Domain-prefix labels at non-bridge positions; `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:` at bridge authoring positions. Positional segregation unchanged. C-58 evaluates positional confinement and vocabulary class separation — the trailing citations on domain-prefix labels are not a component of C-58. |
| **C-59** | **PASS** | `[BRIDGE Q3 COMMAND]:` at Q3 authoring position incorporates `Q3`; `[BRIDGE Q4 COMMAND]:` at Q4 authoring position incorporates `Q4`. Q-IDs present in respective labels — authoring-point coherence confirmed. Cross-document Q-ID loop closed at authoring positions. |
| **C-60** | **FAIL** | Domain-prefix labels: `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` / `INERTIA THREAT CITATION RULE:` — trailing `[A-NN]` bracket citations are absent from all three labels. Labels are structurally coherent role indicators (vocabulary threads, compound domain-axis vocabulary present, positions correct) but are not audit-traceable to specific rules. An evaluator scanning for the rule governing FM identifier assignment sees `INERTIA THREAT RULE:` and must read the label body to determine which annotation is being enforced; no bracket citation is present in the label notation itself. Three distinct citations would be required — `[A-31]`, `[A-16]`, `[A-19]` — and must be distinct across all three labels. None are present. |

**Score: 51/52 × 10 = 9.81**

**C-60 failure mode isolated**: absent trailing citations — vocabulary threading and positional segregation are intact (C-42, C-46, C-58 all pass), but the domain-prefix labels are structural-role indicators rather than audit-traceable rule references. The sole discriminant between V-03 (9.81) and V-04 (10.00) is C-60: the presence or absence of `[A-31]` / `[A-16]` / `[A-19]` in the three non-bridge label brackets.

---

### V-04 — C-59 + C-60 combined pass — R19 V-04 carried unchanged

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Domain-prefix templates present for all five essential elements |
| C-34 through C-58 | PASS (carried) | R19 V-04 = 50/50; carried unchanged into R20 |
| **C-59** | **PASS** | `[BRIDGE Q3 COMMAND]:` at Q3 authoring section — `Q3` present in label. `[BRIDGE Q4 COMMAND]:` at Q4 authoring section — `Q4` present in label. Q-IDs incorporated in the bracket-command labels at both bridge authoring positions. Cross-document Q-ID coherence loop fully closed: Q3/Q4 appear at gate interrogative (C-45/C-49), gate body conditional key (C-53), gate body return target (C-56), and — via C-59 — authoring-point bracket-command label. Every structural position where the artifact is referenced now carries its Q-ID. |
| **C-60** | **PASS** | Non-bridge domain-prefix labels: `INERTIA THREAT FAIL-FIRST RULE [A-31]` / `INERTIA THREAT RULE [A-16]` / `INERTIA THREAT CITATION RULE [A-19]`. Three distinct trailing bracket citations on three vocabulary-threaded labels — `[A-31]`, `[A-16]`, `[A-19]` are distinct across all three. Evaluator can locate each specific governing rule from the label bracket alone without reading the label body. The label set is vocabulary-coherent (C-42), role-specific (C-46), positionally segregated (C-58), and audit-traceable (C-60). |

**Score: 52/52 × 10 = 10.00**

**V-04 is the sole 10.00 form in R20** — confirmed as the reference form satisfying all 60 criteria. C-59 and C-60 are simultaneously satisfied by the two-population structural design: `INERTIA THREAT` domain-prefix labels at non-bridge positions (satisfying C-42/C-46/C-58/C-60) and `[BRIDGE Qn COMMAND]:` labels at bridge authoring positions (satisfying C-41/C-58/C-59). The four criteria C-42 + C-46 + C-58 + C-60 define the fully specified domain-prefix label structure; C-41 + C-58 + C-59 define the fully specified bridge-command label structure.

---

### V-05 — C-59 fail (generic) + C-60 fail (absent citations) combined

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-57 | PASS (carried) | R19 V-04 base; gate body unchanged |
| **C-41** | **PASS** | `[BRIDGE COMMAND]:` at Q3 section, `[BRIDGE COMMAND]:` at Q4 section. Two bracket commands at bridge authoring positions — one per artifact. |
| **C-42** | **PASS** | `INERTIA THREAT` vocabulary threads through three non-bridge labels: `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` / `INERTIA THREAT CITATION RULE:`. Citations removed but threading intact. |
| **C-46** | **PASS** | Compound domain-axis vocabulary present at non-bridge positions. |
| **C-58** | **PASS** | `[BRIDGE COMMAND]:` at bridge positions is bridge-command vocabulary. Domain-prefix labels confined to non-bridge positions. Positional segregation maintained. |
| **C-59** | **FAIL** | `[BRIDGE COMMAND]:` at both Q3 and Q4 authoring positions — generic form, identical at both positions, no Q-ID in either label. Same failure form as V-01. Q-ID coherence chain broken at authoring-point labels. |
| **C-60** | **FAIL** | `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` / `INERTIA THREAT CITATION RULE:` — no trailing `[A-NN]` citations on any of the three domain-prefix labels. Same failure form as V-03. Labels are structurally coherent but not audit-traceable to specific rules. |

**Score: 50/52 × 10 = 9.62**

**Double-fail reference confirmed**: C-59 and C-60 address structurally independent positions — bridge authoring labels (C-59) vs non-bridge domain-prefix labels (C-60) — with no precondition relationship between them in either direction. Both fail independently, and the score deduction is additive: 2 points lost (one per criterion), landing at 50/52 = 9.62. V-05 is the lowest-scoring variation in R20, two points below V-04.

---

## Composite Scores

| Variation | Prior (R19 v19/50) | C-59 | C-60 | R20 Score | Notes |
|-----------|--------------------|------|------|-----------|-------|
| **V-04** | 50/50 | PASS | PASS | **52/52 = 10.00** | All 60 criteria pass; confirmed 10.00 reference |
| **V-01** | 50/50 | FAIL | PASS | 51/52 = 9.81 | C-59 fail: generic `[BRIDGE COMMAND]:` — no Q-ID, label identical at both positions |
| **V-02** | 50/50 | FAIL | PASS | 51/52 = 9.81 | C-59 fail: class-vocab `[BRIDGE ACTOR COMMAND]:` — per-artifact but Q-ID absent |
| **V-03** | 50/50 | PASS | FAIL | 51/52 = 9.81 | C-60 fail: absent trailing citations on all three domain-prefix labels |
| V-05 | 50/50 | FAIL | FAIL | 50/52 = 9.62 | Both fail; generic bridge label + absent citations; additive two-point deduction |

---

## Rankings

1. **V-04** — 52/52 = **10.00**
2. **V-01, V-02, V-03** — 51/52 = **9.81** (three-way tie; distinct failure mechanisms)
3. **V-05** — 50/52 = **9.62**

---

## Excellence Signals

**V-04 (10.00) — structural properties enabling C-59 and C-60:**

1. **C-59 closes the Q-ID coherence loop at the authoring site**: Q-IDs Q3 and Q4 now appear at every structural position where each artifact is referenced — gate interrogative (C-45/C-49), gate body conditional key (C-53), gate body return target (C-56), and authoring-point bracket-command label (C-59). The chain: where the artifact is authored (`[BRIDGE Q3 COMMAND]:`), where it is interrogated (gate table heading), where its failure is keyed (`IF Q3 SHOWS N`), and where return routing terminates (`THE Q3 SECTION`). No structural position that references Q3 is Q-ID-free. The authoring site was the final open link.

2. **The three-way 9.81 tie confirms score equivalence across mechanistically distinct failure modes**: V-01 (C-59 fail via generic label identical at both positions), V-02 (C-59 fail via class-vocab label per-artifact but Q-ID absent), and V-03 (C-60 fail via absent trailing citations) all score 51/52. These are three structurally distinct failure modes — two C-59 variants and one C-60 variant — that produce the same single-point deduction. Score alone cannot discriminate them; the failure mechanism must be identified by inspecting the label structure directly. V-01 and V-02 are indistinguishable by R20 score despite failing by different C-59 mechanisms.

3. **C-59 and C-60 additive independence confirmed by V-05**: V-05 combines the V-01 C-59 failure form with the V-03 C-60 failure form. The score is 50/52 — exactly two points below V-04. No precondition relationship between C-59 and C-60: they fail at structurally independent positions (bridge authoring labels vs non-bridge domain-prefix labels), and both deductions apply simultaneously without interaction. V-05's 9.62 establishes the double-fail floor for R20.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Three-way 9.81 tie (V-01, V-02, V-03) is the first round where three variations with distinct failure mechanisms score identically — two C-59 failure forms (generic label, class-vocab label) and one C-60 failure form (absent citations) each produce exactly one point deduction; score alone cannot discriminate the failure mechanism within each tied variation, requiring direct label inspection", "C-59 and C-60 confirmed as structurally independent — they address disjoint document positions (bridge authoring labels vs non-bridge domain-prefix labels) with no precondition relationship in either direction; V-05's 50/52 double-fail confirms both deductions apply additively with no interaction effect"]}
```
