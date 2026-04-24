Three new excellence signals from the Round 3 scorecard (all sourced from V-01's perfect score):

1. **V-01 gate modification prohibition** — C-10 passes when a gate *exists*. V-01 goes further: "No modifications may be made to this section after this gate" is stated explicitly, and the Expert/Automate/Analyst role separation means a role transition is required to retroactively alter Expected. A gate without a prohibition is a traffic cone; a gate with a prohibition and role identity is a lock.

2. **V-01 element-level diff granularity** — C-12 passes when the diff has one block per surface with a "no deviations" acknowledgment for clean surfaces. V-01 goes further: each element gets an explicit pass acknowledgment or a finding block. A surface-level pass can mask unexamined fields; element-level enumeration cannot.

3. **V-01 full-coverage amendment recommendations** — C-09 passes when every breaking/degraded finding has a `recommendation:` line. V-01's scorecard notes "present on every finding, satisfying the breaking/degraded requirement and more." Cosmetic findings also carry explicit disposition.

Three new criteria: C-15, C-16, and C-17.

---

```markdown
# trace-contract Rubric — v4

## Essential Criteria (weight: 60 pts total)

Output is not a contract trace without all four present.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Expected-before-actual discipline** — The Expected Output section is written from the spec before any operation is executed. No actual output, logs, or runtime results appear in the Expected section. | correctness | Expected section contains only spec-derived content. Any runtime artifact appearing in Expected = fail. |
| C-02 | **Explicit diff present** — The artifact contains a dedicated diff or findings section that explicitly compares expected vs. actual, element by element. An implicit "everything looked fine" summary = fail. | correctness | A diff or findings section exists and names both sides (expected value, actual value) for every deviation. |
| C-03 | **Severity classification** — Every finding carries exactly one severity label: `breaking`, `degraded`, or `cosmetic`. No other values. | classification | Every finding has a severity field with one of the three permitted values. A finding with no severity, a blank severity, or a non-standard label = fail. |
| C-04 | **Spec-anchored findings** — Every finding cites the specific spec clause, contract section, or field definition it violates. | coverage | Every finding includes a `spec:` or `ref:` anchor. Findings without a reference = fail. |

---

## Recommended Criteria (weight: 30 pts total)

Output is materially better with these present.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Root cause hypothesis** — Each finding includes a hypothesis about why the deviation occurred (e.g., missing field mapping, incorrect enum value, serialization bug). | depth | Every finding has a `hypothesis:` or equivalent prose explaining the likely cause. A finding that only describes the symptom = fail. |
| C-06 | **Contract identity and scope** — The operation under test, the connector or Automate context, and the input fixture are stated upfront. | format | Opening section names: operation (e.g., `GET /items`), connector/flow context, and input state. Scope must be derivable without reading external files. |
| C-07 | **Complete boundary coverage** — The diff covers all contract surfaces: success path, error path, and at least one edge case (empty, null, overflow, auth failure). | coverage | At least three distinct contract surfaces are exercised. A trace that only covers the happy path = fail. |

---

## Aspirational Criteria (weight: 10 pts total)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Severity distribution summary** — A summary table or count of findings by severity tier (breaking / degraded / cosmetic) appears at the top or bottom of the artifact. | format | A findings summary with counts per severity tier is present. Bonus: total finding count and contract-satisfied vs. contract-violated verdict. |
| C-09 | **Amendment or fix recommendation** — For every `breaking` or `degraded` finding, the artifact recommends whether the spec should be amended or the implementation should be fixed, and states why. | depth | Every breaking/degraded finding has a `recommendation:` line with one of: `amend-spec`, `fix-impl`, or `needs-discussion` plus a one-sentence rationale. |
| C-10 | **Phase commitment gate** — The artifact contains an explicit phase marker (e.g., `[EXPECTED COMMITTED]`, `[CONTRACT COMMITTED — Automate begins here]`) that separates the Expected commitment from the Actual capture phase. | correctness | A gate label is present between the Expected and Actual sections. Its position makes backward inference (writing expected after seeing actual) structurally visible as a violation rather than an invisible shortcut. |
| C-11 | **Hypothesis anti-loophole** — The root cause hypothesis for each finding states a causal mechanism, not a symptom restatement. | depth | No `hypothesis:` entry begins with or reduces to a symptom restatement. Each hypothesis names a mechanism: a missing mapping, a wrong enum, a serialization path, a missing guard, or a logic branch. A hypothesis that could be generated by substituting the finding's own diff into a template = fail. |
| C-12 | **Diff-surface mirroring** — The diff or findings phase contains one explicit block per expected surface (success, error, edge), even if a block contains no deviations. | coverage | The diff section is structured to mirror the surfaces declared in the Expected section. A surface with no deviations carries an explicit "no deviations" or "contract satisfied" acknowledgment rather than being silently omitted. A diff that folds all surfaces into a single flat list without surface attribution = fail. |
| C-13 | **Mechanism taxonomy enforcement** — The template or rubric declares a formal set of named mechanism categories (e.g., missing-field-mapping, wrong-enum-value, serialization-error, missing-guard, logic-branch, schema-mismatch, auth-gap). Each `hypothesis:` must select one category from the taxonomy. `other` is prohibited as a selection. | depth | A named taxonomy is declared upfront. Every hypothesis cites a taxonomy category. Any hypothesis that uses free-form causal language without a taxonomy selection, or that selects `other`, = fail. |
| C-14 | **Mechanism distribution summary** — The synthesis section reports findings grouped by mechanism category (from the C-13 taxonomy), alongside the per-severity counts from C-08. | format | The synthesis section includes a mechanism distribution table or count (e.g., `missing-field-mapping: 2 \| wrong-enum-value: 1 \| ...`). Bonus: a dominant mechanism call (\"the primary failure mode in this trace is...\"). A synthesis section that reports only severity counts without mechanism distribution = partial. |
| C-15 | **Gate modification prohibition** — The commit gate (C-10) includes an explicit written prohibition on post-gate modifications to the Expected section, and the Expected phase is assigned a distinct role or identity from the Analyst/diff phase so that a role transition is required to retroactively alter Expected. | correctness | The gate contains a "No modifications may be made to this section after this gate" statement or equivalent. The Expected section is labeled with a distinct role identity (e.g., Expert, Spec-Author, Contract-Writer). A gate that marks phase separation without a modification prohibition = partial. |
| C-16 | **Element-level diff granularity** — Within each surface block in the diff section, every individual field or element declared in Expected receives explicit treatment: either an explicit pass acknowledgment (`[field] — contract satisfied`) or a finding block. Fields are not summarized as a group. | coverage | Every field or element named in the Expected section appears by name in the corresponding diff surface block with an explicit pass or finding disposition. A surface-level "no deviations" without field-level enumeration = partial. A diff that names only deviating elements and silently omits passing elements = fail. |
| C-17 | **Full-coverage amendment recommendations** — Amendment or fix recommendations are provided for ALL findings regardless of severity, including cosmetic findings, not just breaking and degraded. | depth | Every finding of any severity has a `recommendation:` line with one of: `amend-spec`, `fix-impl`, or `needs-discussion` plus a one-sentence rationale. C-09 is satisfied by breaking/degraded coverage alone; C-17 requires cosmetic findings to also carry explicit disposition. A trace that provides recommendations only on breaking/degraded while leaving cosmetic findings without disposition = partial. |

---

## Design Rationale

- **C-01/C-02** enforce the three-directory discipline — expected before actual, diff explicit. Without both, it's not a contract trace, it's just a description.
- **C-03/C-04** are the classification core. Severity without a spec anchor is opinion; a spec anchor without severity is incomplete.
- **C-05** (root cause) is recommended not essential because a first-pass trace can be useful before hypotheses are formed — but it's the thing that makes findings actionable.
- **C-07** (boundary coverage) guards against traces that only exercise the happy path and miss the error/edge contracts entirely.
- **C-08/C-09** reward traces that synthesize across findings (summary table, amend-vs-fix call) rather than just enumerating them.
- **C-10** (phase gate) upgrades C-01 from a content check to a structural check. A commitment gate makes phase discipline visible in the artifact; without it, a trace can comply with C-01 on inspection while still having been written in the wrong order. Source: V-01 R2 excellence signal — `[CONTRACT COMMITTED — Automate begins here]` makes backward inference structurally impossible.
- **C-11** (hypothesis anti-loophole) closes the escape hatch in C-05. "A finding that only describes the symptom = fail" is not enough because a symptom can be dressed up in causal language. The explicit prohibition on restatement patterns catches the most common failure mode. Source: V-04 R2 excellence signal — "DO NOT write a hypothesis that begins 'The output did not match.'"
- **C-12** (diff-surface mirroring) is a structural complement to C-07. C-07 enforces breadth in the Expected section; C-12 enforces that the diff phase mirrors that breadth explicitly. A trace can pass C-07 by listing three surfaces in Expected and then silently fold all findings into a flat list. C-12 closes that gap. Source: V-03 R2 excellence signal — three mandatory diff blocks required even with no findings; "If you exercise only one surface, the trace fails C-07 regardless of finding quality."
- **C-13** (mechanism taxonomy enforcement) upgrades C-11 from a prohibition to a structural requirement. C-11 says "don't restate symptoms." C-13 says "select from a declared taxonomy." The distinction matters: a prohibition can be satisfied by any causal-sounding phrase; a taxonomy forces commitment to a named mechanism category. The `other` prohibition closes the escape hatch within the taxonomy itself. Source: V-04 R2 excellence signal — 7-category taxonomy with explicit prohibition on `other`; V-01/V-02/V-03 all scored PARTIAL on C-11 precisely because they had prohibition gates but no taxonomy.
- **C-14** (mechanism distribution) extends C-08's synthesis pattern from severity to mechanism. A severity distribution tells you how bad the findings are; a mechanism distribution tells you where the contract is systematically fragile. These are complementary views. Source: V-04 R2 bonus signal — mechanism distribution in Step 6 synthesis.
- **C-15** (gate modification prohibition) upgrades C-10 from "gate exists" to "gate is architecturally enforced." C-10 checks that a phase separator is present and structurally visible. C-15 requires two additional properties: (1) an explicit written prohibition on retroactive modification, and (2) role or identity separation between the Expected and Analyst phases so that a role transition is required to alter Expected. A gate without a prohibition is a traffic cone; a gate with a prohibition and role separation is a lock. Source: V-01 R3 excellence signal — "No modifications may be made to this section after this gate" plus Expert/Automate/Analyst role separation making backward inference architecturally impossible rather than merely structurally visible.
- **C-16** (element-level diff granularity) upgrades C-12 from surface-level acknowledgment to element-level acknowledgment. C-12 requires one block per surface; C-16 requires one disposition per field within each surface. The gap: a trace can pass C-12 by writing "no deviations — contract satisfied for this surface" while leaving individual fields unexamined. C-16 closes that gap by requiring every field declared in Expected to appear by name in the diff with an explicit pass or finding. Source: V-01 R3 excellence signal — "each element gets a pass acknowledgment or a finding block."
- **C-17** (full-coverage amendment recommendations) upgrades C-09 from breaking/degraded coverage to full-spectrum coverage. C-09's rationale is that cosmetic findings don't block shipping; C-17's rationale is that cosmetic findings still represent contract drift and deserve an explicit disposition — even if that disposition is "accept" or "defer." The distinction between "no recommendation given" and "disposition: defer — cosmetic drift tracked for future cleanup" is the difference between an incomplete trace and a deliberate one. Source: V-01 R3 excellence signal — "recommendation present on every finding, satisfying the breaking/degraded requirement and more."

---

## Criterion Count Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 4 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 10 | 10 |
| **Total** | **17 criteria** | **100** |

*Aspirational points: 10 pts / 10 criteria = 1 pt each. PARTIAL = 0.5 pt.*

---

## Scoring Examples

**Minimal passing (golden threshold)**
- All 4 essential pass -> 60 pts
- 2/3 recommended pass -> 20 pts
- 0/10 aspirational pass -> 0 pts
- Total: 80 -- passes golden threshold

**Round 3 V-03 (best pre-taxonomy variant, re-scored against v4)**
- All 4 essential pass -> 60 pts
- All 3 recommended pass -> 30 pts
- C-08 PASS + C-09 PASS + C-10 PASS + C-11 PARTIAL + C-12 PASS + C-13 FAIL + C-14 FAIL + C-15 PARTIAL + C-16 unknown + C-17 unknown
- Aspirational (known): ~4 pts
- Total: ~94 (bounded; C-16/C-17 require inspection of diff and synthesis sections)

**Perfect v4 score**
- All 4 essential pass -> 60 pts
- All 3 recommended pass -> 30 pts
- All 10 aspirational pass -> 10 pts
- Total: 100
```

---

**What changed in v4 and why:**

- **C-15** closes the gap between C-10 (gate exists) and V-01 R3's architectural enforcement (gate is locked). A commit gate makes backward inference *structurally visible*; a gate with a modification prohibition and role separation makes it *structurally impossible*. The distinction is the same as C-11 to C-13: from a prohibition to a structural requirement. V-01 R3 was the first trace to demonstrate both the prohibition text and role-based enforcement in the same artifact.

- **C-16** closes the gap between C-12 (surface-level acknowledgment) and V-01 R3's element-level enumeration. C-12 prevents silent surface omission; C-16 prevents silent field omission within a surface. A trace can pass C-12 with a single "no deviations" line for a surface that has ten fields. C-16 requires each of those ten fields to be named with an explicit disposition. This is the element-granularity upgrade V-01 R3 demonstrated.

- **C-17** closes the gap between C-09 (breaking/degraded coverage) and V-01 R3's full-spectrum coverage. C-09's threshold is binary: recommendations present on actionable findings. C-17's threshold is complete: every finding including cosmetic carries explicit disposition. A cosmetic finding without a recommendation is an unresolved question; a cosmetic finding with "defer — tracked for future cleanup" is a deliberate choice. V-01 R3 demonstrated this by applying the recommendation field to every finding block regardless of severity.

- **Aspirational tier** grows from 7 to 10 criteria. The 10-point pool normalizes to exactly 1 pt per criterion (vs. ~1.43 in v3). PARTIAL = 0.5 pt.
