Now I have all five variation texts. Let me score them against the full rubric.

---

# signal-check Scorecard — R7 (2026-03-18)

**Rubric version**: v7 | **Criteria under test**: C-24 (validity framing), C-25 (proximate scope pointer)
**Aspirational denominator**: 17 | **Formula**: `composite = 90 + (asp_pass / 17) * 10`

---

## Shared baseline

All variations use the identical output structure — same GATHERING section, four-item PREFLIGHT CHECK, CROSS-ITEM PATTERNS, MISSING SIGNAL GUIDE, frontmatter. The only structural difference across variations is the wording of **Rule 3**. Criteria C-01 through C-21 are evaluated once and noted as shared.

| Criterion block | Status (all variations) | Evidence |
|----------------|------------------------|----------|
| **C-01** Structured four-item preflight | PASS | CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE items present in all |
| **C-02** STATUS field with three states | PASS | OK / FLAG / OPEN defined and used |
| **C-03** Advisory framing declared | PASS | "preflight check... does not decide whether to fly" |
| **C-04** Not-a-verdict framing in readiness summary | PASS | "Frame as pilot briefing -- not a verdict. The team decides." |
| **C-05** Advisory register | PASS | Declared at top; framing maintained |
| **C-06 to C-08** Recommended | PASS | All three satisfied in all variations |
| **C-09** Named STANDING RULES block | PASS | Block present, precedes all analysis (C-14 subsumed) |
| **C-10** Block contains Rule 1 and Rule 2 | PASS | Both present in all |
| **C-11** Readiness summary section | PASS | Present in all |
| **C-12** Four specific dimensions | PASS | All four named and structured |
| **C-13** MISSING SIGNAL GUIDE section | PASS | Present in all |
| **C-14** STANDING RULES block precedes inventory | PASS | Rules appear before `=== GATHER YOUR SIGNALS ===` |
| **C-15** Each dimension specifies verbatim absence phrases | PASS | All four items carry required verbatim phrases |
| **C-16** Every constraint enumerates output locations | PASS | Rule 1, Rule 2, Rule 3 all have `Applies to:` lines |
| **C-17** Verbatim phrases embedded at point of use | PASS | Each dimension item carries its phrase inline, not only in a reference table |
| **C-18** Advisory register carried structurally | PASS | "preflight", "pilot briefing", "clearance" vocabulary in section heads and framing |
| **C-19** Triple enforcement stack declared as unit | PASS | ENFORCEMENT STACK NOTE present and names interdependency in all |
| **C-20** Location-enumeration as named meta-rule | PASS | Rule 3 in all variations self-applies to all Rule declarations |
| **C-21** Each rule assigned named failure class | PASS | ENFORCEMENT STACK NOTE assigns: absence drift / reference ambiguity / constraint scope gaps |

---

## Per-variation Rule 3 analysis (C-22 through C-25)

### V-01 — Validity gate / no proximate pointer

**Rule 3 body (key excerpt):**
> "A Rule that has not declared its scope is not operative -- it does not exist as an active rule until its scope is discharged. This requirement self-applies: Rule 3 declares its scope in the accompanying Applies-to annotation."

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-22 | Temporal activation gate | PASS | "until its scope is discharged" — temporal condition present; also auto-satisfied via C-24 (per rubric) |
| C-23 | Self-application in rule body | PASS | "This requirement self-applies: Rule 3 declares its scope in the accompanying Applies-to annotation" — body-level declaration |
| C-24 | Validity framing | **PASS** | "is not operative -- it does not exist as an active rule" — explicit validity condition; not obligation language |
| C-25 | Proximate scope pointer | **FAIL** | "in the accompanying Applies-to annotation" — no directional anchor ("below" or equivalent); location is named but not positionally bound |

**Asp pass**: 16 / 17 | **Composite**: 90 + (16/17) × 10 = **99.41**

---

### V-02 — Obligation gate / proximate pointer (R6 V-04 verbatim)

**Rule 3 body (key excerpt):**
> "Every Rule in this STANDING RULES block must declare all output locations it governs before becoming active. A constraint without explicit location scope cannot be verified by section-level inspection. This requirement self-applies: Rule 3 itself declares its scope below."

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-22 | Temporal activation gate | PASS | "before becoming active" — standard obligation gate |
| C-23 | Self-application in rule body | PASS | "This requirement self-applies: Rule 3 itself declares its scope below" |
| C-24 | Validity framing | **FAIL** | "before becoming active" is obligation language — rule exists and requires compliance. No "not operative" / "does not exist" language present |
| C-25 | Proximate scope pointer | **PASS** | "Rule 3 itself declares its scope below" — "below" commits Applies-to to co-location; pointer is directional |

**Asp pass**: 16 / 17 | **Composite**: 90 + (16/17) × 10 = **99.41**

---

### V-03 — Obligation gate / no proximate pointer (v7 floor)

**Rule 3 body (key excerpt):**
> "Every Rule in this STANDING RULES block must declare all output locations it governs before becoming active. This requirement self-applies: Rule 3 declares its scope explicitly."

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-22 | Temporal activation gate | PASS | "before becoming active" — temporal gate present |
| C-23 | Self-application in rule body | PASS | "This requirement self-applies: Rule 3 declares its scope explicitly" |
| C-24 | Validity framing | **FAIL** | Obligation language only ("must declare... before becoming active"). No validity condition. |
| C-25 | Proximate scope pointer | **FAIL** | "declares its scope explicitly" — "explicitly" is a quality modifier, not a positional anchor. No "below" or directional pointer. |

**Asp pass**: 15 / 17 | **Composite**: 90 + (15/17) × 10 = **98.82**

---

### V-04 — Validity gate + proximate pointer (minimal ceiling diff)

**Rule 3 body (key excerpt):**
> "Every Rule in this STANDING RULES block must declare all output locations it governs before becoming active. A Rule that has not declared its scope is not operative -- it does not exist as an active rule until its scope is discharged. This requirement self-applies: Rule 3 itself declares its scope below."

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-22 | Temporal activation gate | PASS | "before becoming active" + "until its scope is discharged" — both forms present; auto-satisfied via C-24 |
| C-23 | Self-application in rule body | PASS | "This requirement self-applies: Rule 3 itself declares its scope below" |
| C-24 | Validity framing | **PASS** | "not operative -- it does not exist as an active rule until its scope is discharged" — validity-conditional language; non-compliance is rule-existence failure |
| C-25 | Proximate scope pointer | **PASS** | "Rule 3 itself declares its scope below" — directional pointer present; co-location contract encoded |

**Asp pass**: 17 / 17 | **Composite**: 90 + (17/17) × 10 = **100.00**

---

### V-05 — Rule name encodes validity class; forward-scoping Applies-to

**Rule 3 body (key excerpt):**
> "Rule 3 -- RULES ARE INVALID WITHOUT DECLARED SCOPE: Every Rule in this STANDING RULES block must declare all output locations it governs before becoming active. A rule that has not discharged its scope declaration is not operative -- it does not exist as a valid rule until the Applies-to annotation has been written. Non-compliance is a rule-existence failure, not a rule-compliance failure. This requirement self-applies: Rule 3 itself declares its scope below."
> Applies to: all Rule declarations in this STANDING RULES block, including Rule 3 itself and any rule added in the future.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-22 | Temporal activation gate | PASS | "before becoming active" + "until the Applies-to annotation has been written" |
| C-23 | Self-application in rule body | PASS | "This requirement self-applies: Rule 3 itself declares its scope below" |
| C-24 | Validity framing | **PASS** | "not operative -- it does not exist as a valid rule until the Applies-to annotation has been written. Non-compliance is a rule-existence failure, not a rule-compliance failure." — strongest validity framing of any variation |
| C-25 | Proximate scope pointer | **PASS** | "Rule 3 itself declares its scope below" |

**Asp pass**: 17 / 17 | **Composite**: 90 + (17/17) × 10 = **100.00**

---

## Composite scores and ranking

| Rank | Variation | Asp | Composite | C-24 | C-25 | Notes |
|------|-----------|-----|-----------|------|------|-------|
| 1 (tie) | **V-04** | 17/17 | **100.00** | PASS | PASS | Minimal diff from V-03 ceiling; compact and complete |
| 1 (tie) | **V-05** | 17/17 | **100.00** | PASS | PASS | Rule name encodes class; forward-scoped Applies-to; explicit taxonomy |
| 3 (tie) | V-01 | 16/17 | 99.41 | PASS | FAIL | Validity framing present; proximate pointer absent |
| 3 (tie) | V-02 | 16/17 | 99.41 | FAIL | PASS | Proximate pointer present; obligation framing only |
| 5 | V-03 | 15/17 | 98.82 | FAIL | FAIL | v7 floor — gates without validity framing or positional anchor |

All essential criteria: PASS (all 5, all variations). **Golden threshold met** by all variations (composite >= 80, all essential pass).

---

## Excellence signals

**Signals from V-04 (minimal ceiling)**:

- **C-24 minimal form**: `"not operative -- it does not exist as an active rule until its scope is discharged"` is the shortest valid validity-framing construction. Two clauses: non-operative state + non-existence condition. Both are required — "not operative" alone may read as a policy state; "does not exist as an active rule" makes it an ontological claim.
- **C-25 minimal form**: `"Rule 3 itself declares its scope below"` — four words beyond bare self-application. "Below" is the differentiator from V-01's "accompanying" and V-03's "explicitly"; it creates a verifiable layout contract.
- **Additive independence confirmed**: V-04 is exactly V-03 + validity gate + proximate pointer. The two additions are orthogonal — either can be removed independently to produce V-01 (drop C-25) or V-02 (drop C-24).

**Signals from V-05 (potential R8 surface)**:

- **Rule name as failure-class declaration**: `"RULES ARE INVALID WITHOUT DECLARED SCOPE"` — the heading encodes the failure class. A reviewer scanning the rule block can classify the rule's function from the name alone without reading the body. This is a new pattern not captured by any current criterion.
- **Explicit failure-mode taxonomy in body**: `"Non-compliance is a rule-existence failure, not a rule-compliance failure"` — the rule body itself names the two-class taxonomy and assigns this rule to the stronger class. C-24 is satisfied by stating non-operative status; V-05 additionally names what class that non-operative status belongs to.
- **Forward-scoping Applies-to**: `"including Rule 3 itself and any rule added in the future"` — extends the scope annotation to explicitly govern future rules. The existing Applies-to in all other variations uses `"all Rule declarations in this STANDING RULES block"` which is implicitly forward-scoped; V-05 makes it explicit. Potential R8 signal: is implicit forward-scope (via universal quantifier) equivalent to explicit forward-scope?

---

## Isolation test results (C-24 vs C-25 independence)

| Axis | Evidence |
|------|----------|
| C-24 without C-25 | V-01 — validity framing passes; no positional pointer. 16/17. |
| C-25 without C-24 | V-02 — proximate pointer passes; obligation framing only. 16/17. |
| Neither | V-03 — 15/17 floor. |
| Both | V-04, V-05 — 100.00. |

**Independence confirmed.** The two criteria address structurally different properties: C-24 is semantic (what kind of failure non-compliance produces), C-25 is positional (where the scope annotation must appear). Neither implies the other.

---

## R8 candidate signals (from V-05)

| Signal | Pattern | What it would test |
|--------|---------|-------------------|
| Rule name = function declaration | Heading encodes failure class | Is the failure class recoverable from the rule name alone? |
| Forward-scoping Applies-to | "any rule added in the future" explicit | Does explicit future-scope improve on implicit universal-quantifier coverage? |
| In-body failure-mode taxonomy | "rule-existence failure, not a rule-compliance failure" | Does naming the two-class taxonomy in the body add verifiability beyond validity-state assertion alone? |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["rule name encodes failure class -- heading declares 'RULES ARE INVALID WITHOUT DECLARED SCOPE', making the failure type recoverable from the name alone without reading the body", "explicit failure-mode taxonomy in body -- 'Non-compliance is a rule-existence failure, not a rule-compliance failure' names the two-class distinction and assigns this rule to the stronger class", "forward-scoping Applies-to -- 'any rule added in the future' makes implicit universal-quantifier scope explicit, testing whether stated forward-scope adds verifiability over inferred coverage"]}
```
