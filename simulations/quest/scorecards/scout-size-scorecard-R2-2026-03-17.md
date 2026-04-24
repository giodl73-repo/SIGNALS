## quest:score — scout-size R2 Results

**Rubric:** v2 (C-11 ownership, C-12 named unknowns, C-13 synthesis)
**Scoring model:** essential (60) + recommended (30) + aspirational (10 @ 2 pts each)

---

### Scorecard

| Rank | Variation | Score | C-11 | C-12 | C-13 | Band |
|------|-----------|-------|------|------|------|------|
| 1 | **V-05** Full Aspirational Stack | **100** | PASS | PASS | PASS | Gold |
| 2 | **V-04** Hypothesis-Revision | **100** | PASS | PASS | PASS | Gold |
| 3 | **V-01** Synthesis Template | **99** | PASS | PARTIAL | PASS | Gold |
| 4 | **V-02** Unknowns-as-Section | **98** | PASS | PASS | FAIL | Gold |
| 5 | **V-03** Ownership Table | **98** | PASS | PASS | FAIL | Gold |

All 5 variations pass all essential criteria. The differentiator is purely aspirational depth.

---

### V-05 vs V-04 (tied at 100)

V-05 ranks first on **execution reliability**:
- Table-first redundancy means C-11/C-12/C-13 enforcement is structurally doubled
- Explicit `Rules:` sub-sections with named negative examples are harder to silently violate than conversational prose
- Proven base (V-05 R1 = 98/100) vs novel lifecycle (V-04) with acknowledged execution risk

V-04 has the theoretically **strongest C-13 mechanism** — a hypothesis the model must confirm or revise cannot produce juxtaposition. But it sacrifices the table enforcement layer that makes gaps detectable.

---

### Prediction accuracy

4/5 ranks matched. The miss: predictor placed V-01 above V-04. On design analysis, V-04 achieves full C-11/C-12/C-13 coverage — execution risk is real but post-run, not a structural gap.

---

### 4 new excellence signals captured

1. **Rules: sub-sections** — negative examples + hard mandates prevent silent omission on aspirational criteria
2. **Unknowns as own section** (V-02 pattern) — structural separation makes missing entries visually detectable
3. **Hypothesis-revision lifecycle** (V-04 pattern) — prior commitment forces C-13 cross-dimensional reasoning
4. **AMEND cascade to synthesis** — amendment must re-evaluate synthesis when the amended dimension changes the cross-signal conclusion

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["rules-sub-sections", "unknowns-as-first-class-section", "hypothesis-revision-lifecycle", "amend-cascade-to-synthesis"]}
```
| AMEND requires revising table cell + corresponding section; content change enforced. |
| C-09 | **PASS** | SCOPE EXCLUSIONS section present; at least one exclusion required. |
| C-10 | **PASS** | Section 1 break-even required; "if blocked, state the blocking condition." |
| C-11 | **PASS** | Section 4 TEAM OWNERSHIP with `Role:` / `Owns:` sub-structure explicitly required. |
| C-12 | **PARTIAL** | Section 5 includes Unknown-movement format but co-located with confidence basis — predicted failure mode: "unknowns movement may not surface" when confidence is stated first. Structural separation (as in V-02) not present. |
| C-13 | **PASS** | Section 6 SYNTHESIS: mandatory anchor template "[Dimension A] combined with [Dimension B] [argues for/cautions against] [recommendation]"; anti-juxtaposition language explicit ("Restating each section in sequence is not synthesis — it is juxtaposition"). |

**Aspiration subtotal:** C-09(2) + C-10(2) + C-11(2) + C-12(1) + C-13(2) = **9**
**Composite: 60 + 30 + 9 = 99**

---

## V-02 — Unknowns-as-Section

**Axis:** C-12 (unknowns elevated to own section). **Base:** V-02 R1. **Deliberately no synthesis section.**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 3 "Rate complexity: LOW / MEDIUM / HIGH / XL" with canonical label set. |
| C-02 | **PASS** | Step 4 "sprint range with both bounds (e.g., 2-4 sprints). A single number fails." |
| C-03 | **PASS** | Step 2 "Count and name the integration points... List them. If the count is 0-1, explain why." |
| C-04 | **PASS** | Step 1 opens the prompt: "Before estimating anything, name the competition." Highest C-04 structural position. |
| C-05 | **PASS** | Step 6: confidence level + primary reason required. |
| C-06 | **PASS** | Step 5 "'1 backend + 1 infra' not '2 engineers'. For each specialization, state what they own during the build." |
| C-07 | **PASS** | Step 3 "State the primary driver in one sentence immediately after the rating." |
| C-08 | **PASS** | "Do not only acknowledge the amendment; change the output." Explicit content-change enforcement. |
| C-09 | **PASS** | Step 8 SCOPE NOTE: "out-of-scope sub-systems, deferred work, assumptions that could invalidate the estimate." |
| C-10 | **PASS** | Step 1 break-even required; fallback clause prevents evasion. |
| C-11 | **PASS** | Step 5 explicitly: "For each specialization, state what they own during the build: what specific artifact, layer, or sub-system is theirs to deliver." |
| C-12 | **PASS** | Step 7 OPEN UNKNOWNS is a structurally separate section with `Unknown:` / `Impact:` / `Movement:` fields required. "List at least one unknown." HIGH-confidence fallback: "No open unknowns — confidence is stable. The following would lower it: [X]." Omission is structurally visible. |
| C-13 | **FAIL** | No synthesis section by design. Single-axis variation deliberately excludes C-13 to isolate C-12 behavior. |

**Aspiration subtotal:** C-09(2) + C-10(2) + C-11(2) + C-12(2) + C-13(0) = **8**
**Composite: 60 + 30 + 8 = 98**

---

## V-03 — Ownership-Contract Table

**Axis:** C-11 (ownership contract table). **Base:** V-01 R1. **C-12 partial; no synthesis.**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Sizing summary table Complexity row: "LOW / MEDIUM / HIGH / XL". |
| C-02 | **PASS** | Timeline row "N-M sprints" — "Range required, not a point." |
| C-03 | **PASS** | Surface Area row "N integration points" + SURFACE AREA expansion enumeration. |
| C-04 | **PASS** | INERTIA CHECK section present with workaround + cost + break-even. (Note: placed after CONFIDENCE BASIS in section order — rubric requires presence, not position.) |
| C-05 | **PASS** | Confidence row in table + CONFIDENCE BASIS expansion. |
| C-06 | **PASS** | Team Signal row "Specializations, not headcount." |
| C-07 | **PASS** | COMPLEXITY DRIVER section: "one sentence naming what pushed the complexity to that tier. 'HIGH because X'... This must appear." |
| C-08 | **PASS** | "AMEND: modify the affected table cell and the corresponding expansion section. The table must reflect the amendment." |
| C-09 | **PASS** | SCOPE section: bullet list of what sizing does NOT cover. |
| C-10 | **PASS** | INERTIA CHECK requires break-even signal; "If break-even cannot be assessed, say why." |
| C-11 | **PASS** | TEAM OWNERSHIP TABLE: three-column table `Role \| Owns (during implementation) \| Dependency`. "Owns: backend work fails. Owns: event schema + storage migration passes." Empty Owns cell is visually detectable. Strongest C-11 enforcement of R2 variations. |
| C-12 | **PASS** | CONFIDENCE BASIS: "Name at least one specific unknown that, if resolved, would change the confidence rating. Format: 'Unknown: [X] — resolution would move confidence from [level] to [level].'" Explicit format + at-least-one requirement. |
| C-13 | **FAIL** | No synthesis section by design. Scope limited to C-11 plus C-12 partial coverage. |

**Aspiration subtotal:** C-09(2) + C-10(2) + C-11(2) + C-12(2) + C-13(0) = **8**
**Composite: 60 + 30 + 8 = 98**

---

## V-04 — Synthesis-First with Hypothesis Revision

**Axis:** C-13 (hypothesis-revision lifecycle) + C-11 + C-12. **Base:** Novel — no R1 ancestor.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | COMPLEXITY section: "Assign a tier: LOW / MEDIUM / HIGH / XL." |
| C-02 | **PASS** | TIMELINE: "State a sprint range — lower bound and upper bound. A single number fails; it implies false precision. Calendar dates fail." Anti-pattern callout present. |
| C-03 | **PASS** | SURFACE AREA: "Enumerate integration points... Name each one. Count the total. If the count is 0-1, explain." |
| C-04 | **PASS** | INERTIA CHECK: workaround + cost + break-even + blocking unknown fallback. Positioned as second section after opening hypothesis. |
| C-05 | **PASS** | CONFIDENCE: "State a confidence level: LOW / MED / HIGH or a percentage. Give the primary basis." |
| C-06 | **PASS** | TEAM SIGNAL: "'1 backend + 1 infra' not '2 engineers'." Anti-pattern callout present. |
| C-07 | **PASS** | COMPLEXITY: "State the single driver that determined the tier." |
| C-08 | **PASS** | AMEND cascade: "reopen the affected section and revise it, then re-evaluate whether the closing synthesis still holds or needs updating. The amendment is complete only when both the section and the synthesis reflect the change." Strongest AMEND contract of R2 variations. |
| C-09 | **PASS** | SCOPE: "List what this sizing does NOT cover: out-of-scope sub-systems, deferred complexity, assumptions that could change the estimate." |
| C-10 | **PASS** | INERTIA CHECK: break-even required; "name the blocking unknown" fallback. |
| C-11 | **PASS** | TEAM SIGNAL: "For each specialization, state what they own during the build — the specific artifact, layer, or sub-system this role delivers." |
| C-12 | **PASS** | CONFIDENCE: "name at least one specific unknown that, if resolved, would move the rating. Format: 'Unknown: [X] — would move confidence from [level] to [level] once resolved.' If confidence is HIGH, name what could lower it." HIGH-confidence dodge handled. |
| C-13 | **PASS** | CLOSING SYNTHESIS: "Return to the opening hypothesis. Either confirm it or revise it — produce one synthesis paragraph that cross-references at least two signal dimensions by name." Anti-juxtaposition: "A closing that merely restates the sections in order is not synthesis — it is a summary. The synthesis must produce a conclusion that could not be read directly from any single section." Hypothesis-revision lifecycle creates the strongest theoretical forcing function for C-13. |

**Aspiration subtotal:** C-09(2) + C-10(2) + C-11(2) + C-12(2) + C-13(2) = **10**
**Composite: 60 + 30 + 10 = 100**

**Execution risk note:** The opening hypothesis mechanism is the most novel forcing function for C-13 but introduces a single failure mode: the model may treat the opening hypothesis as a throw-away rather than a binding commitment, collapsing opening and closing into a single pass. No structural redundancy (table-first) to catch silent omission.

---

## V-05 — Full Aspirational Stack

**Axis:** C-11 + C-12 + C-13 all layered on V-05 R1 (98/100). **Base:** V-05 R1 — highest R1 score.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Sizing summary table Complexity row: "LOW / MEDIUM / HIGH / XL" — structurally enforced by table cell. |
| C-02 | **PASS** | Table Timeline row "N-M sprints" + "Derived from complexity + surface." |
| C-03 | **PASS** | Table Surface Area row "N points (list follows)" + Section 3 named enumeration. |
| C-04 | **PASS** | Section 1 INERTIA CHECK mandatory, runs before all sizing — strongest inertia-first position. Workaround + cost + break-even + blocking-condition fallback. |
| C-05 | **PASS** | Table Confidence row + Section 5 basis; redundant enforcement. |
| C-06 | **PASS** | Table Team Signal row "Specializations, not headcount." |
| C-07 | **PASS** | Table Complexity row "One sentence naming the driver." |
| C-08 | **PASS** | AMEND HANDLING: revise table cell + corresponding section + re-evaluate Section 6 synthesis if dimension changes cross-signal conclusion. Two-step cascade. |
| C-09 | **PASS** | Section 7 SCOPE EXCLUSIONS: "At least one exclusion is required." Hard mandate. |
| C-10 | **PASS** | Section 1 break-even as explicit threshold; blocking condition required when blocked. |
| C-11 | **PASS** | Section 4 TEAM OWNERSHIP: `Role:` / `Owns:` / `Hands off:` structure. Explicit rules: "Do not list a role without an Owns line." "At least one role must have both Owns and Hands off populated." "Owns: implementation is not acceptable. Name the specific thing." |
| C-12 | **PASS** | Section 5 CONFIDENCE AND OPEN UNKNOWNS: `Unknown:` / `Affects:` / `Movement:` format. "At minimum, one unknown must appear." HIGH fallback: "No remaining unknowns. The following would lower confidence: [X]." Stating confidence without unknowns engagement is declared incomplete. |
| C-13 | **PASS** | Section 6 SYNTHESIS: anchor structure "[Dimension A] combined with [Dimension B] [argues for / supports / cautions against] [recommendation]." Anti-juxtaposition: "The conclusion must be derivable only by reasoning across dimensions, not from reading any single section in isolation." |

**Aspiration subtotal:** C-09(2) + C-10(2) + C-11(2) + C-12(2) + C-13(2) = **10**
**Composite: 60 + 30 + 10 = 100**

**Structural reliability note:** Table-first + section expansion produces redundant enforcement on C-01 through C-10. Explicit "Rules:" sub-sections (not just instructions) prevent silent omission on C-11. C-11/C-12/C-13 are integrated into the existing structural skeleton rather than added as new conversational layers, reducing execution risk relative to V-04.

---

## Rankings

| Rank | Variation | Score | All Essentials | C-11 | C-12 | C-13 | Structural Risk |
|------|-----------|-------|----------------|------|------|------|-----------------|
| 1 | V-05 Full Stack | **100** | PASS | PASS | PASS | PASS | Low — table redundancy + explicit Rules |
| 2 | V-04 Hypothesis-Revision | **100** | PASS | PASS | PASS | PASS | Medium — novel lifecycle, no table enforcement |
| 3 | V-01 Synthesis Template | **99** | PASS | PASS | PARTIAL | PASS | Low — inherits V-05 R1 base |
| 4 | V-02 Unknowns-as-Section | **98** | PASS | PASS | PASS | FAIL | Low — deliberate single-axis |
| 5 | V-03 Ownership Table | **98** | PASS | PASS | PASS | FAIL | Low — deliberate single-axis |

V-05 and V-04 are tied on composite. V-05 ranks first because:
- V-05 R1 base scored 98/100 — proven structural reliability across all essential/recommended criteria
- Table-first redundancy (summary row + section expansion) makes compliance gaps doubly detectable
- Explicit "Rules:" sub-sections (C-11) and "at minimum" mandates (C-12) are harder to silently violate than prose instructions in conversational flow
- AMEND cascade in V-05 mirrors V-04's but also updates synthesis — same coverage, stronger structural anchor

V-04 ranks second. Its hypothesis-revision mechanism is the theoretically strongest C-13 forcing function — a model cannot produce juxtaposition when it must confirm or revise a prior commitment. But it trades structural redundancy for conversational elegance, introducing execution risk on the new criteria.

---

## Leaderboard vs Prediction

| Rank | Predicted (from variations file) | Actual | Delta |
|------|----------------------------------|--------|-------|
| 1 | V-05 | V-05 | Match |
| 2 | V-01 | V-04 | Miss — V-04 full-coverage beats V-01 C-12 partial |
| 3 | V-04 | V-01 | Off-by-one |
| 4 | V-02 | V-02 | Match |
| 5 | V-03 | V-03 | Match |

**Prediction miss analysis:** The predictor ranked V-01 above V-04 without accounting for V-04 achieving full C-11/C-12/C-13 coverage. V-04's conversational structure made it look execution-risky, but on design-criterion analysis it meets all three aspirational criteria explicitly. The execution risk is real but post-run, not a design gap.

---

## Excellence Signals from Top Variations (R2)

**Signal 1 — Rules: sub-sections prevent silent omission on aspirational criteria**
V-05's explicit `Rules:` block under Section 4 TEAM OWNERSHIP ("Do not list a role without an Owns line", "Owns: implementation is not acceptable") gives negative examples and hard mandates. This is stronger than positive instruction alone — the model cannot satisfy "name the specific thing" with "backend implementation" when the negative example is explicitly named.

**Signal 2 — Structural separation of unknowns from confidence (V-02 pattern)**
Elevating unknowns to a first-class section (Step 7, separate from Step 6) makes a missing entry visually detectable rather than silently omittable. When unknowns are a sub-bullet inside the confidence paragraph, the model can satisfy confidence while skipping unknowns. When unknowns have their own section header with required fields, omission is structurally obvious.

**Signal 3 — Hypothesis-revision lifecycle as C-13 forcing function (V-04 pattern)**
An opening hypothesis that names two dimensions before sizing — and a closing that must confirm or revise it — forces cross-dimensional reasoning by construction. The model cannot produce juxtaposition in the closing because it must actively compare against a prior claim. This is more cognitively binding than an anchor template (V-05/V-01 approach), though it sacrifices table-enforced reliability.

**Signal 4 — AMEND cascade to synthesis re-evaluation**
Both V-04 and V-05 extend AMEND handling to require synthesis re-evaluation when the amended dimension changes a cross-signal conclusion. This prevents the anti-pattern where an AMEND correctly updates one section but leaves a now-stale synthesis in place.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["rules-sub-sections: explicit Rules: blocks with named negative examples ('Owns: implementation is not acceptable') enforce aspirational criteria more reliably than positive instructions alone", "unknowns-as-first-class-section: structurally separating open unknowns from the confidence basis makes missing entries visually detectable — omission cannot be silent when fields have section headers", "hypothesis-revision lifecycle: opening with a named hypothesis and requiring the closing to confirm or revise it forces cross-dimensional reasoning by creating a prior commitment the model must return to", "amend-cascade-to-synthesis: requiring AMEND to re-evaluate synthesis when the amended dimension changes a cross-signal conclusion prevents stale synthesis artifacts"]}
```
