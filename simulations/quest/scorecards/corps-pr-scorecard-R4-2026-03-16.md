## corps-pr Round 4 — Quest Score

### Rubric v4 Summary

| ID | Weight | Category |
|----|--------|----------|
| C-01 through C-05 | 12 pts each (60 total) | Essential |
| C-06 through C-08 | 10 pts each (30 total) | Recommended |
| C-09 through C-16 | 1.25 pts each (10 total) | Aspirational |

Golden threshold: all 5 essential pass AND composite ≥ 80.

---

### V-01 — Domain-lens gate as named two-step procedure

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Baseline routing behavior assumed; no contradiction. |
| C-02 | PASS | Severity labeling is baseline. |
| C-03 | PASS | Consensus synthesis is baseline. |
| C-04 | PASS | GO/NO-GO is baseline. |
| C-05 | PASS | Two-step procedure (Step A: binary test; Step B: rewrite consequence) directly satisfies the explicit-validity-check requirement. |
| C-06 | FAIL | No coverage gap notice addressed. |
| C-07 | FAIL | Per-role severity summaries not addressed. |
| C-08 | FAIL | AMEND template not the focus; no structured disclosure. |
| C-09 | FAIL | No root cause synthesis specified. |
| C-10 | FAIL | GO WITH CONDITIONS sign-off roles not addressed. |
| C-11 | FAIL | IA sequencing not addressed. |
| C-12 | FAIL | Architectural mechanism in divergence not addressed. |
| C-13 | FAIL | Ban list not addressed; phrasing register is V-03's axis. |
| C-14 | FAIL | IA anchoring by technical roles not addressed. |
| C-15 | PASS | Step A + Step B named explicitly; rewrite consequence stated with reason specificity ≠ fidelity. |
| C-16 | FAIL | No AMEND template structure. |

**Essential:** 5/5 → 60  
**Recommended:** 0/3 → 0  
**Aspirational:** 1/8 → 1.25  
**Composite: 61.25** — NOT GOLDEN

---

### V-02 — Every block a named-field schema; AMEND as Field: Value slots; Domain-Lens as two-cell column

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Baseline. |
| C-02 | PASS | Baseline. |
| C-03 | PASS | Baseline. |
| C-04 | PASS | Baseline. |
| C-05 | PASS | Two-cell Domain-Lens column (binary result + revision note) satisfies explicit validity check. |
| C-06 | FAIL | Coverage gap notice not described. |
| C-07 | FAIL | Named-field schema covers structure but per-role severity summary slot not explicitly included. |
| C-08 | PASS | AMEND uses Field: Value slots — the three required disclosure elements (amended, roles, superseded) can be mapped to named fields. |
| C-09 | FAIL | Not addressed. |
| C-10 | FAIL | Not addressed. |
| C-11 | FAIL | Not addressed. |
| C-12 | FAIL | Not addressed. |
| C-13 | FAIL | Ban list not the focus of V-02. |
| C-14 | FAIL | Not addressed. |
| C-15 | PASS | Two-cell Domain-Lens: binary result cell + revision note cell = Step A + Step B inline. |
| C-16 | PASS | AMEND uses Field: Value slots — structured block with named fields, not prose instructions. |

**Essential:** 5/5 → 60  
**Recommended:** 1/3 → 10  
**Aspirational:** 2/8 → 2.5  
**Composite: 72.5** — NOT GOLDEN

---

### V-03 — Imperative steps; ban list as substitution table

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Baseline. |
| C-02 | PASS | Baseline. |
| C-03 | PASS | Baseline. |
| C-04 | PASS | Baseline. |
| C-05 | PARTIAL | "Imperative steps" as phrasing register does not confirm an explicit binary test + rewrite consequence. The axis is phrasing, not validity-check inclusion. No two-step procedure described. |
| C-06 | FAIL | Not addressed. |
| C-07 | FAIL | Not addressed. |
| C-08 | FAIL | AMEND not addressed; no structured template. |
| C-09 | FAIL | Not addressed. |
| C-10 | FAIL | Not addressed. |
| C-11 | FAIL | Not addressed. |
| C-12 | FAIL | Not addressed. |
| C-13 | PASS | Substitution table pairs each banned phrase with its required replacement form — exceeds the >=3 enumeration requirement and makes the list a repair protocol. |
| C-14 | FAIL | Not addressed. |
| C-15 | FAIL | No explicit Step A + Step B; C-15 requires the binary test and rewrite consequence to be named procedure elements, not derivable from imperative phrasing. |
| C-16 | FAIL | AMEND not addressed. |

**Essential:** 4/5 (C-05 PARTIAL → 0) → 48  
**Recommended:** 0/3 → 0  
**Aspirational:** 1/8 → 1.25  
**Composite: 49.25** — NOT GOLDEN (essential criterion failure)

---

### V-04 — IA as "status-quo budget authority"; five phase gates; C-15 as Phase C exit gate

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Baseline. |
| C-02 | PASS | Baseline. |
| C-03 | PASS | Baseline. |
| C-04 | PASS | Baseline. |
| C-05 | PASS | C-15 enforced as Phase C exit gate implies the domain-lens validity check is present and gated; the phase exit condition is the explicit check C-05 requires. |
| C-06 | FAIL | Not addressed. |
| C-07 | FAIL | Phase gates structure the lifecycle but do not describe per-role severity summaries. |
| C-08 | FAIL | AMEND not addressed; no structured disclosure template. |
| C-09 | FAIL | Not explicitly required; root cause synthesis could emerge from budget framing but is not specified. |
| C-10 | FAIL | Not addressed. |
| C-11 | PASS | IA as "status-quo budget authority" is a structural reference role — technical roles argue against the budget, which implies IA is sequenced first as the baseline object. Phase gate structure reinforces reference-object sequencing. |
| C-12 | PARTIAL | Budget-authority framing encourages code-surface anchoring, but the criterion requires naming a structural/architectural mechanism explicitly. "Budget" is a framing device, not an architectural mechanism name. |
| C-13 | FAIL | Ban list not addressed. |
| C-14 | PASS | "Technical roles argue the PR's benefit exceeds the budget" — each technical role section is structurally required to engage the IA's verdict as the counterpoint. |
| C-15 | PASS | C-15 enforced as Phase C exit gate — binary test (does the finding survive?) and rewrite consequence (Phase C blocks progression) are both present. |
| C-16 | FAIL | AMEND not addressed. |

**Essential:** 5/5 → 60  
**Recommended:** 0/3 → 0  
**Aspirational:** C-11 PASS, C-14 PASS, C-15 PASS → 3/8 → 3.75  
**Composite: 63.75** — NOT GOLDEN

---

### V-05 — All blocks as fill-or-fail named-field templates; ban-to-fix substitution table; two-cell domain-lens column

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Baseline. |
| C-02 | PASS | Baseline. |
| C-03 | PASS | Baseline. |
| C-04 | PASS | Baseline. |
| C-05 | PASS | Two-cell domain-lens column (revision slot = rewrite consequence) satisfies the explicit validity check. |
| C-06 | FAIL | Not addressed. |
| C-07 | FAIL | Named-field templates cover structure broadly but per-role severity summary is not an explicitly named template slot. |
| C-08 | PASS | "All blocks as fill-or-fail named-field templates" — the AMEND block is a block; the fill-or-fail frame covers it without a conditional. Three required fields (what amended, roles, superseded) map to named slots. |
| C-09 | FAIL | Not addressed. |
| C-10 | FAIL | Not addressed. |
| C-11 | FAIL | IA sequencing not addressed. |
| C-12 | FAIL | Architectural mechanism in divergence not addressed. |
| C-13 | PASS | "Ban-to-fix substitution table" — each banned phrase is paired with its replacement, making the list a self-auditable substitution protocol. Exceeds the >=3 enumeration floor. |
| C-14 | FAIL | Not addressed. |
| C-15 | PASS | Two-cell domain-lens column with revision slot: cell 1 = binary test result, cell 2 = revision note. Both required elements (test + consequence) present inline. |
| C-16 | PASS | "All blocks as fill-or-fail named-field templates" — AMEND block is a named-field template by definition; the scope of "all blocks" removes the need for a special case. |

**Essential:** 5/5 → 60  
**Recommended:** 1/3 → 10  
**Aspirational:** C-13 PASS, C-15 PASS, C-16 PASS → 3/8 → 3.75  
**Composite: 73.75** — NOT GOLDEN

---

### Rankings

| Rank | Variation | Composite | Essential | Recommended | Aspirational |
|------|-----------|-----------|-----------|-------------|--------------|
| 1 | **V-05** | **73.75** | 5/5 | 1/3 (C-08) | 3/8 (C-13, C-15, C-16) |
| 2 | V-02 | 72.5 | 5/5 | 1/3 (C-08) | 2/8 (C-15, C-16) |
| 3 | V-04 | 63.75 | 5/5 | 0/3 | 3/8 (C-11, C-14, C-15) |
| 4 | V-01 | 61.25 | 5/5 | 0/3 | 1/8 (C-15) |
| 5 | V-03 | 49.25 | 4/5 (C-05 PARTIAL) | 0/3 | 1/8 (C-13) |

---

### Excellence Signals from V-05

**Signal 1 — "All blocks" scope eliminates conditional coverage.**  
V-05's "fill-or-fail named-field templates" applies to *every* block, not just AMEND or findings. This means AMEND compliance is achieved as a structural consequence of the global template rule rather than a mode-specific carve-out. No conditional logic, no forgetting to apply the template in a specific mode.

**Signal 2 — Fill-or-fail framing makes missing fields structurally visible.**  
Prior variations described what fields should be present. V-05's fill-or-fail frame shifts the enforcement model: a blank slot is evidence of failure, not silence. This makes output review a scan for empties rather than a check for presence.

**Signal 3 — Substitution table converts prohibition into repair protocol.**  
V-03 introduced the substitution table but V-05 applies it alongside the template frame. A ban list that provides the replacement form gives the skill model an action, not just a constraint — "use X instead of Y" is executable; "do not say Y" is not.

---

### Gap Analysis: Why No Golden

V-05 reaches 73.75. To cross 80, it needs one more recommended pass:

- **C-07** (per-role severity summaries, 10 pts): Would push V-05 to 83.75. This criterion has gone unaddressed in all four rounds — it's the single highest-leverage gap. A named-field template that includes a `findings-summary` slot per role would satisfy it without adding structural complexity.
- **C-06** (coverage gap notice, 10 pts): Also 10 pts; requires explicit unmatched-file handling.

No variation combined IA framing (V-04: C-11, C-14) with the template + substitution approach (V-05: C-13, C-16). A V-06 that merges these two axes — budget-authority IA + fill-or-fail templates — would add C-11 and C-14 to V-05's aspirational set (5/8 → 6.25 pts aspirational) and potentially reach golden if C-07 is also addressed.

---

```json
{"top_score": 73.75, "all_essential_pass": true, "new_patterns": ["fill-or-fail template frame makes missing fields structurally visible as empty slots rather than absent assertions", "ban-to-fix substitution table converts each prohibited phrase into an executable repair instruction not just a constraint"]}
```
