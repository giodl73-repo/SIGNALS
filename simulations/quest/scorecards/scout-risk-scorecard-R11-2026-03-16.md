## Scout-Risk R11 — Scoring Report

### Baseline State

R10 V-03 scored 136/136 on v10. Against v11 rubric:
- C-01 through C-31: All PASS (full typed-column three-table structure, named repair loops A/B/C/D, Decision Window, row floor ≥7, standalone Phase 2b, complete Phase 0 taxonomy)
- C-32: PASS — "Trigger Condition" named as discrete column in Table 3 (V-01: "discrete field" in prose; V-02–V-05: column in Table 3)
- C-33: PASS — "Dimension: exactly one of {Technical | Market | Compliance | Dependency | Timeline}" stated in column rules in all variations
- C-34: **Targeted by all five variations**

Baseline on v11 rubric before R11 additions: **140/142**

---

### Criterion-by-Criterion Scoring

#### C-01 through C-31 (all variations)

All five variations preserve the full R10 V-03 structural baseline. Pass condition for each:

| Cluster | Criterion | All Variations |
|---------|-----------|---------------|
| Essential C-01–C-05 | Inertia mandatory/first; dimensional coverage; complete anatomy; severity scale; specific mitigations | PASS all |
| Recommended C-06–C-08 | Dimension labels; qualified likelihoods; severity ordering | PASS all |
| Aspirational C-09–C-31 | Dedicated interdependency section; AMEND base; prohibition enumeration; IF-THEN likelihoods; typed mitigations; sub-field inline rendering; pre-phase taxonomy; inertia anatomy fields (status-quo, condition, decision window); isolated inertia schema; row floor gate; named repair loops; diversity audit isolated; downstream repair loops; type portfolio | PASS all |

No regression: V-01's prose-format output still passes C-30 (separate labeled sub-sections with independent field sets), C-26 (inline sub-field values required), and C-32 (Trigger Condition named as "discrete field" separate from From-Severity/To-Severity).

---

#### C-32 per variation

**C-32**: Interdependency table rows carry a dedicated Trigger Condition field as named column/field separate from From/To severity.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Phase 3: "Trigger Condition (discrete field): … state the activation event as a standalone field, not embedded in the severity transition" — named and isolated | PASS |
| V-02 | Table 3 column schema: "Trigger Condition — Names the specific activation event for this pair as a dedicated column field … separate from From-Severity and To-Severity" | PASS |
| V-03 | Same Table 3 column schema as V-02 | PASS |
| V-04 | Same Table 3 column schema as V-02 | PASS |
| V-05 | Table 3: "Trigger Condition — Activation event as a dedicated column — IF [From-Risk activates by its named condition]; this field is separate from From-Severity and To-Severity" | PASS |

---

#### C-33 per variation

**C-33**: Dimension column vocabulary-constrained to closed {Technical, Market, Compliance, Dependency, Timeline} at cell level.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Phase 2 rules: "Dimension: exactly one of {Technical, Market, Compliance, Dependency, Timeline} — unlabeled values or compound values ('Technical/Dependency') fail" | PASS |
| V-02 | Table 2 column rule: "Dimension: Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline" with "compound or unlabeled values are format violations" | PASS |
| V-03 | Same column rule as V-02 | PASS |
| V-04 | Same column rule as V-02 | PASS |
| V-05 | Table 2: "Dimension: Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline" — explicitly named closed set | PASS |

---

#### C-34 per variation

**C-34**: AMEND confirmation is a structured header block naming both active and suppressed dimensions explicitly — parseable structural element, not prose note.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| **V-01** | AMEND Behavior section requires: `AMEND Scope Declaration / Active Dimensions: [list — only from: Technical, Market, Compliance, Dependency, Timeline] / Suppressed Dimensions: [list — only from: ...]` + completeness rule (all five dimensions in exactly one field) + positioned "as the first output element — before Phase 1" | PASS |
| **V-02** | Same named block structure as V-01; positioned before Table 1; completeness rule + "no omissions, no duplicates across the two fields" | PASS |
| **V-03** | Phase 0a table: `Active Dimensions` and `Suppressed Dimensions` as named fields with cell constraints; completeness rule stated explicitly; Phase 0a is the literal first output — produced before Phase 0 taxonomy. Strongest structural position. | PASS |
| **V-04** | AMEND Scope Declaration block with field-level vocabulary constraints: "each value must be exactly one of {Technical, Market, Compliance, Dependency, Timeline} — invented, compound, or unlabeled dimension names are format violations" on both Active and Suppressed fields. C-34 plus defensive vocabulary mirroring. | PASS |
| **V-05** | Phase 0a table with per-field vocabulary constraints (`Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted.`) + completeness constraint in table row + Phase 0a as mandatory named phase before taxonomy. All axes combined. | PASS |

---

### Composite Scores

| Variation | C-01–C-05 (60) | C-06–C-08 (30) | C-09–C-31 (44) | C-32 (2) | C-33 (2) | C-34 (2) | **Total** |
|-----------|----------------|----------------|----------------|----------|----------|----------|-----------|
| V-01 | 60 | 30 | 44 | 2 | 2 | 2 | **142** |
| V-02 | 60 | 30 | 44 | 2 | 2 | 2 | **142** |
| V-03 | 60 | 30 | 44 | 2 | 2 | 2 | **142** |
| V-04 | 60 | 30 | 44 | 2 | 2 | 2 | **142** |
| V-05 | 60 | 30 | 44 | 2 | 2 | 2 | **142** |

All five variations reach 142/142. C-34 is satisfied by every variation — the AMEND Scope Declaration pattern is robust across both prose (V-01) and table formats (V-02–V-05), trailing sections and first-class phases.

---

### Ranking

All variations tie at 142/142. Structural confidence ordering (for selection purposes):

1. **V-05** — All axes combined: Phase 0a + vocabulary-constrained AMEND fields + imperative phrasing. Highest-confidence; closes all conditional framing gaps.
2. **V-04** — Table format + vocabulary-constrained AMEND fields. C-34 plus defensive constraint mirroring on AMEND header.
3. **V-03** — Phase 0a as dedicated execution phase. AMEND scope is the literal first output; no trailing ambiguity.
4. **V-02** — Minimal delta from R10 V-03. Clean confirmation that the AMEND Scope Declaration block alone is sufficient.
5. **V-01** — Prose format. Confirms C-34 is format-independent; useful for lightweight deployments.

---

### Excellence Signals from V-05

**1. Uniform closed-vocabulary contract**: The same `exactly one of {set}` cell-level constraint that governs the Dimension column in Table 2 is now applied to the Active Dimensions and Suppressed Dimensions fields in the AMEND Scope Declaration. One constraint pattern spans the entire output — both the main register and the scope declaration use the same enforcement language. This eliminates a residual ambiguity: without this, a model could write an AMEND header saying "Operational" (not in the closed set) and pass C-34 textually while violating C-33 semantics.

**2. Phase-position AMEND resolution**: Structuring AMEND as Phase 0a — a mandatory named execution phase before the taxonomy — means scope is declared before any content generation begins. A trailing AMEND section (V-01, V-02) is encountered last; a leading Phase 0a is encountered first. The model resolves what to generate before it generates anything, not retroactively. This is a stronger behavioral guarantee than positional prose ("produce the block as the first element").

**3. Imperative phrasing register**: Rewriting every instruction as a command ("Produce a single-row table", "Count rows after generating", "Return to Phase 2") rather than conditional framing removes model discretion about whether each step is required. The resulting prompt reads as an execution contract — every phase is unconditionally mandatory, every repair loop is a procedure to execute, not a suggestion to consider.

---

```json
{"top_score": 142, "all_essential_pass": true, "new_patterns": ["uniform closed-vocabulary contract: the same 'exactly one of {set}' cell-level constraint applied to the Dimension column is mirrored onto AMEND Scope Declaration field values, creating one constraint language across the full output and making out-of-scope dimension labels violations in both register and AMEND header", "phase-position AMEND resolution: structuring AMEND as Phase 0a before the taxonomy block ensures scope is declared before any content is generated — stronger behavioral guarantee than a trailing section instructed to appear first", "imperative phrasing register: rewriting all phase instructions as unconditional commands removes conditional framing and model discretion, making every step mechanically required rather than judgment-dependent"]}
```
