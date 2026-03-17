Now I have all five variations fully read. I have enough to score all 26 criteria across each variation.

---

## Quest Scorecard — campaign-brief / Round 8

**Rubric:** v8 — 26 criteria, 260 pts max
**Date:** 2026-03-16
**Variations:** V-01 through V-05

---

### Scoring Conventions

| Result | Points |
|--------|--------|
| PASS | 10 |
| PARTIAL | 5 |
| FAIL | 0 |

**Baseline assumption:** All five variations are built on the R7 best base (V-02 and V-05 tied at 230/260 under v7). That means C-01 through C-23 all passed in R7 and carry forward unmodified. The three R8 axes are the sole differentiators.

---

### C-01 through C-20 — Carry Forward from v6

All five variations reproduce the R7 best base body verbatim except for the three targeted axes. No v6/v7 structure is disturbed. Confirmed: C-01–C-20 **PASS** in all variations, 200/200 baseline.

---

### C-21 — Sparse-Coverage Synthesis Protection

**V-01:** Sparse clause present in STORY rules: "if found contains signals from only 1-2 namespaces, do not default to a coverage disclaimer — synthesize on the available signals." **PASS**

**V-02:** Same clause present, and zero-signal rule references the distinction ("This rule is distinct from the sparse-coverage rule"). **PASS**

**V-03:** Same clause present in STORY rules. **PASS**

**V-04:** Same clause present. STORY references the standalone zero-signal rule for zero coverage, sparse-coverage handled by in-block rule. **PASS**

**V-05:** Same clause present. **PASS**

---

### C-22 — Zero-Signal Synthesis Mandate

**V-01:** Embedded in STORY rules: "Zero coverage: if found is empty, uniform absence is itself evidence; question 1 must characterize what uniform absence implies — not report absence as a non-answer." Clause form. **PASS**

**V-02:** Promoted to standalone ZERO-SIGNAL SYNTHESIS RULE with two numbered clauses. Clause (1) bars omission, clause (2) mandates characterization of uniform absence. STORY rule defers to it: "Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE above." The mandate is present in stronger form than embedded clause — C-22 satisfied. **PASS**

**V-03:** Same embedded form as V-01. **PASS**

**V-04:** Standalone named rule present (same as V-02). STORY defers to it. **PASS**

**V-05:** Standalone named rule present (same as V-02/V-04). **PASS**

---

### C-23 — Bounded/Unbounded Inertia Classification at Verdict Level

**V-01:** VERDICT `inertia_cost` declares `bounded: <residual risk and why the team can detect and correct post-commit> OR unbounded: <failure class and why irreversible once committed>`. No action sub-labels — classification present without posture naming. Meets C-23. **PASS**

**V-02:** Same VERDICT form. **PASS**

**V-03:** VERDICT `inertia_cost` has bounded/unbounded plus `action:` sub-labels. Classification still present — C-23 satisfied (C-26 also satisfied, scored below). **PASS**

**V-04:** Same as V-01/V-02 form (bounded/unbounded, no action sub-labels). **PASS**

**V-05:** Bounded/unbounded present with action sub-labels. C-23 satisfied. **PASS**

---

### C-24 — Timestamp Isolation Dual-Location Mandate *(R8 new)*

**C-24 criterion:** Rule must appear at two structural locations — (1) within `found` entry format definition, (2) in STATUS or STORY execution note — so it survives COMPRESSED regardless of which location is elided.

**V-01:**
- Location 1 (inline on `found` field, lines 146–149): `← timestamp is structurally separate from blocking entries; this date field is NOT part of the blocking entry format and must NOT be abbreviated, collapsed, or omitted regardless of which format branch is active` ✓
- Location 2 (STATUS execution note, lines 173–179): `TIMESTAMP ISOLATION: per-signal dates in the 'found' section are structurally separate from blocking entries and must be preserved at item level. COMPRESSED format applies only to blocking entry verbosity — 'found' timestamps must not be collapsed or summarized regardless of blocking gap count.` ✓
Two distinct structural locations confirmed. **PASS**

**V-02:**
- STATUS has only one note (execution note): "Per-signal timestamps in the `found` section are structurally separate from blocking entries and must appear at item level regardless of blocking gap count." No inline annotation on the `found` format field. Single location.
**FAIL**

**V-03:**
- Same single-location form as V-02. STATUS execution note only, no inline annotation.
**FAIL**

**V-04:**
- Location 1 (inline on `found` field, lines 814–817): `← timestamp is structurally separate from blocking entries; must NOT be abbreviated or omitted under any format branch — COMPRESSED applies to blocking entries only, not to found item dates` ✓
- Location 2 (STATUS execution note, lines 844–846): `TIMESTAMP ISOLATION: per-signal dates in the 'found' section are structurally separate from blocking entries. COMPRESSED format governs blocking entry verbosity only — found timestamps must appear at item level regardless of blocking gap count.` ✓
**PASS**

**V-05:**
- Location 1 (inline on `found` field, lines 1052–1055): `← timestamp is structurally separate from blocking entries; this field is NOT subject to COMPRESSED abbreviation — found dates must appear at item level regardless of blocking gap count` ✓
- Location 2 (STATUS execution note, lines 1082–1086): `TIMESTAMP ISOLATION: per-signal dates in the 'found' section are structurally separate from blocking entries. COMPRESSED format applies only to blocking entry verbosity — 'found' timestamps must not be collapsed, summarized, or omitted regardless of blocking gap count. This restatement is the second structural location for this rule; the first is the inline annotation on the date field above.` ✓ — explicitly self-labels as the second structural location.
**PASS**

---

### C-25 — Zero-Signal Mandate as Standalone Named Execution Rule *(R8 new)*

**C-25 criterion:** Standalone named rule (not embedded in STORY execution note) with two explicitly numbered operational clauses, placed outside either block's execution note.

**V-01:**
- Zero-signal handling embedded inside STORY rules block: "Zero coverage: if found is empty, uniform absence is itself evidence; question 1 must characterize what uniform absence implies — not report absence as a non-answer." One clause, no name, inside STORY block. C-22 form only.
**FAIL**

**V-02:**
- Standalone `ZERO-SIGNAL SYNTHESIS RULE` block placed between `[CONFIDENCE]` and `[STORY]` (lines 426–448). Two numbered clauses: (1) empty `found` not grounds for omitting STORY, (2) Q1 must characterize uniform absence. Basis line explains the reasoning. Structurally separate from STORY execution note. **PASS**

**V-03:**
- Same embedded form as V-01. **FAIL**

**V-04:**
- Standalone `ZERO-SIGNAL SYNTHESIS RULE` block (lines 881–903), same two numbered clauses as V-02. STORY defers: "Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE above." **PASS**

**V-05:**
- Standalone `ZERO-SIGNAL SYNTHESIS RULE` block (lines 1121–1143), same two numbered clauses. V-05 adds a closing sentence that makes the structural distinction explicit: "Both boundary conditions require synthesis. Neither permits disclaimer substitution for the synthesis obligation." **PASS**

---

### C-26 — Action-Posture Sub-Labels on Bounded/Unbounded *(R8 new)*

**C-26 criterion:** `action: commit with monitoring` on bounded, `action: do not commit until resolved` on unbounded, as required sub-labels in VERDICT `inertia_cost` field.

**V-01:**
- VERDICT `inertia_cost`: `bounded: <...> OR unbounded: <...>`. No action sub-labels.
**FAIL**

**V-02:**
- Same form. No action sub-labels.
**FAIL**

**V-03:**
- VERDICT `inertia_cost` (lines 691–697):
  ```
  bounded: <residual risk...>
    action: commit with monitoring
  OR
  unbounded: <failure class...>
    action: do not commit until resolved
  ```
  Both sub-labels present. Execution note at lines 708–714 states: "Declare bounded or unbounded with its action sub-label. The action sub-label is what makes the VERDICT self-contained — the team must be able to derive their commit posture from this block alone without re-reading STORY or item-level gap entries." **PASS**

**V-04:**
- VERDICT `inertia_cost`: `bounded: <...> OR unbounded: <...>`. No action sub-labels.
**FAIL**

**V-05:**
- VERDICT `inertia_cost` (lines 1175–1182):
  ```
  bounded: <residual risk...>
    action: commit with monitoring
  OR
  unbounded: <failure class...>
    action: do not commit until resolved
  ```
  Execution note (lines 1193–1199) explicitly states: "The action sub-label makes VERDICT self-contained: the team must be able to derive their commit posture from this block alone without re-reading STORY or item-level gap fields." **PASS**

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| **C-24** | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| **C-25** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-26** | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| **Score** | **240** | **240** | **240** | **250** | **260** |
| **/ 260** | 92% | 92% | 92% | 96% | **100%** |

---

### Ranking

| Rank | Variation | Score | Criteria passed |
|------|-----------|-------|-----------------|
| 1 | **V-05** | 260/260 | All 26 |
| 2 | V-04 | 250/260 | C-24 + C-25; C-26 absent |
| 3 (tied) | V-01 | 240/260 | C-24 only |
| 3 (tied) | V-02 | 240/260 | C-25 only |
| 3 (tied) | V-03 | 240/260 | C-26 only |

Single-axis variations are structurally independent and non-conflicting: each adds exactly 10pts to the 230 baseline. Additivity confirmed: V-04 = 250 = V-01 + V-02 – 230 baseline. V-05 = 260 = V-04 + 10. No structural interaction degradation detected.

---

### Excellence Signals — V-05

Three patterns in V-05 that made it better than V-04 and distinguished it from prior R7 top variations:

**Pattern 1 — Self-labeling dual-location architecture (C-24)**
V-05's second timestamp isolation location (STATUS execution note) explicitly states: *"This restatement is the second structural location for this rule; the first is the inline annotation on the date field above."* This self-referential labeling makes the dual-location mechanism legible to the model — rather than relying on the model to recognize two independent instructions as serving the same invariant, V-05 tells the model the architecture is intentional and the two instances are structurally coordinated. The model cannot interpret the second instance as redundant noise; it is framed as a deliberate failsafe.

**Pattern 2 — Named rule that declares its own boundary conditions (C-25)**
V-05's ZERO-SIGNAL SYNTHESIS RULE closes with: *"Both boundary conditions require synthesis. Neither permits disclaimer substitution for the synthesis obligation."* This explicitly maps the rule's relationship to C-21 (sparse coverage) and C-22 (embedded clause) by naming both as *boundary conditions* — framing the rule family as a complete partition of coverage states rather than two independent rules. The model receives a categorical statement: for any coverage level (including zero), the synthesis obligation is non-waivable.

**Pattern 3 — Self-contained verdict with embedded rationale for the sub-label (C-26)**
V-05's VERDICT execution note explicitly explains *why* the action sub-label is required: *"The action sub-label makes VERDICT self-contained: the team must be able to derive their commit posture from this block alone without re-reading STORY or item-level gap fields."* The instruction embeds the purpose, not just the syntax. This means the model is not just told to produce `action: commit with monitoring` — it understands that the sub-label is the mechanism for self-containment. A model that understands the purpose of a field is more likely to preserve it under compression than one that only knows the field exists.

---

### R9 Investigation Candidate (Carried Forward)

Whether C-26's `action:` sub-label syntax survives when COMPRESSED abbreviates the STATUS block at high token pressure, pushing the VERDICT block to the end of the output where token budget pressure is highest. V-05 passed C-26 at the structural level; R9 should stress-test the runtime survival of `action:` sub-labels in VERDICT when STATUS has >4 blocking gaps and the COMPRESSED branch was triggered.

---

```json
{"top_score": 260, "all_essential_pass": true, "new_patterns": ["Self-labeling dual-location architecture: second structural location explicitly identifies itself as a failsafe for the first, making the two-location mechanism legible to the model rather than appearing as redundant noise", "Named synthesis rule declares its own boundary conditions: zero-signal rule closes by naming both sparse-coverage and zero-coverage as boundary conditions requiring synthesis, framing the rule family as a complete partition that permits no disclaimer substitution at any coverage level", "Self-contained verdict with embedded sub-label rationale: VERDICT execution note explains why the action sub-label is required (self-containment), not just what it is — a model that understands the purpose of a field preserves it under compression better than one that only knows the field exists"]}
```
