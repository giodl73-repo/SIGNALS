# Quest Score — prove-prototype (Round 3)

**Rubric**: v3 (120 pts) | **New criteria**: C-16, C-17

---

## Results

| Rank | Variation | Score | Verdict |
|------|-----------|-------|---------|
| 1 | V-01 (Table-Driven) | **120 / 120** | Golden |
| — | V-02 (Phase Gates) | 80–119 / 120 | Cannot determine (prompt cut off) |
| — | V-03–V-05 | — | Not provided |

---

## V-01: 120 / 120 — Full Golden

All 17 criteria PASS. The two new criteria were already satisfied by design:

- **C-16** (counter-evidence closed): Section 6 mandates one of exactly two dispositions — named counter + rebuttal, OR explicit "no counter + reason." Forced-branch eliminates any open exit.
- **C-17** (rationale co-located): Tables in Sections 2, 5, and 7 put rationale in the same row as its anchor. All four required rationale types are structurally co-located.

---

## V-02: 80 confirmed / 120 (Phase 6+ cut off)

4/5 essentials confirmed PASS (C-05 unconfirmed). The labeled-pair block format in Phase 5 satisfies C-17 without tables — `**Why the delta is what it is**` is in the same block as `**Delta**`. C-11 is PARTIAL (no blanket cell-population declaration). C-16 and C-09 unconfirmable due to cutoff.

---

## New Patterns

1. **`explicit-two-path-closure-enforces-c16`** — forcing a binary disposition (counter exists / counter does not exist) structurally closes optional sections; generalizes beyond counter-evidence
2. **`phase-execute-marker-as-inline-temporal-lock`** — V-02's "*Execute before Phase X*" labels enforce ordering at the point of construction, vs. V-01's end-of-document output contract
3. **`labeled-pair-block-achieves-c17-without-tables`** — V-02 demonstrates C-17 compliance via labeled-pair field blocks, not tables; co-location doesn't require tabular format
 with a rationale cell; >=2 rows enforced; column header directly asks the test-validity question. |
| C-07 | Raw evidence included | **PASS** | Section 5 "Include at least one concrete data point (a number, a time, a count, an output)" -- explicit enumeration of acceptable evidence forms. |
| C-08 | Limitations and next step | **PASS** | Section 8 table: Limitation | Next Step; table structure enforces one populated row minimum. |
| C-09 | Counter-evidence addressed | **PASS** | Section 6 requires either (a) named counter-interpretation + evidence-grounded rebuttal, or (b) explicit no-counter statement + reason. Rebuttal case fully covered. |
| C-10 | Replication path clear | **PASS** | Section 9: "List every tool, input, command, or step needed to reproduce this prototype. Use a numbered list. No implicit steps." Named-file requirement for configs. |
| C-11 | No sections left blank | **PASS** | Structural Rules block: "Every table cell must be populated. Write 'N/A' only if the cell genuinely does not apply and state why inline." Blanket header-level declaration before any step. |
| C-12 | Measurement ordering explicit | **PASS** | "Section 3 must appear in the output before Section 4" in Structural Rules. Both a step-level and output-contract-level gate enforce the temporal sequence. |
| C-13 | Delta computed, not co-reported | **PASS** | Section 5: Delta is a mandatory fourth column distinct from Predicted and Actual. "If predicted and actual match, write '0 -- prediction confirmed.'" Computation enforced by the format itself. |
| C-14 | Verdict rationale distinct | **PASS** | Section 7 rationale cell requirement; rationale must appear in a separate section from results -- structural separation prevents evidence restatement. Verdict table decoupled from results table. |
| C-15 | Each exclusion answers test-validity | **PASS** | Section 2 column header is verbatim the test-validity question; per-row enforcement via >=2 row requirement. Bare-label rows structurally incomplete without the fourth cell populated. |
| C-16 | Counter-evidence question explicitly closed | **PASS** | Section 6 closes with one of two mandatory dispositions: named counter + rebuttal, OR "No plausible counter-interpretation was identified" + one-sentence reason. The no-counter case is explicitly required, not implied. Neither path leaves the section open. |
| C-17 | Rationale co-located with anchor | **PASS** | Scope exclusion: rationale in same row as exclusion (Section 2 table). Delta explanation: in same row as delta (Section 5 table). Verdict rationale: same row as verdict (Section 7 table). Counter-rebuttal: inline in same labeled section. All four required rationale types are structurally co-located by table-row enforcement. |

**Composite: 120 / 120 -- Golden**

---

## V-02 -- Phase Gates, Lifecycle Emphasis (PARTIAL PROMPT -- cut off after Phase 6 opening line)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Hypothesis restated | **PASS** | PHASE 1: "*Execute before anything else.*" + "Restate the hypothesis in your own words. One to two sentences." + `> H: [restatement here]` label. First element gate with positional anchor. |
| C-02 | Prototype scope defined | **PASS** | PHASE 2: "Name what the prototype will do and what it will not do." Minimum two exclusions required. "Bare labels without rationale fail this phase." Per-exclusion test-validity question: "Without this, can the prototype still test the hypothesis? Why?" |
| C-03 | Measurement defined before building | **PASS** | PHASE 3: "*Execute before any build activity. This phase establishes the evidentiary standard the result will be held to.*" + "Do not proceed to Phase 4 until every success and failure condition is written down." Double enforcement: phase label and explicit gate. |
| C-04 | Actual vs. predicted reported | **PASS** | PHASE 5: Labeled-pair block includes Predicted, Actual, Delta fields. "Delta: [gap as a signed quantity -- do not merge this into either Predicted or Actual]." Distinct labeled field required. |
| C-05 | Verdict rendered | **UNKNOWN** | Phase 7+ not visible due to cutoff. Verdict section presumably follows counter-evidence. Cannot confirm enforcement mechanism. |
| C-06 | Minimality justified | **PASS** | PHASE 2 test-validity framing ("Without this, can the prototype still test the hypothesis? Why?") operationalizes minimality per exclusion. At minimum 2 exclusions required. |
| C-07 | Raw evidence included | **PASS** | PHASE 5: "Report the raw evidence that produced the actual value. Include at least one concrete data point (a number, a time, a count, an output)." Enumeration explicit. |
| C-08 | Limitations and next step | **UNKNOWN** | Phase 7+ not visible. Cannot confirm. |
| C-09 | Counter-evidence addressed | **UNKNOWN** | PHASE 6 opening line visible ("Consider whether the results could be explained by something other than the hypothesis being true or false") but body cut off before enforcement mechanism is visible. |
| C-10 | Replication path clear | **UNKNOWN** | Phase 7+ not visible. Cannot confirm. |
| C-11 | No sections left blank | **PARTIAL** | Phase execute-markers and gate checks enforce section-level presence. Phase 4 word budget (50-150 words) creates a content floor for one section. No blanket header-level "every field must be populated" declaration visible. Table-cell population guarantee absent -- structural enforcement weaker than V-01. |
| C-12 | Measurement ordering explicit | **PASS** | PHASE 3 is labeled "*Execute before any build activity*"; phase numbering makes the temporal gate legible by structure alone. Gate explicitly prevents Phase 4 start until all conditions written. |
| C-13 | Delta computed, not co-reported | **PASS** | PHASE 5 Delta is a distinct labeled field in the labeled-pair block, with explicit instruction: "do not merge this into either Predicted or Actual." |
| C-14 | Verdict rationale distinct | **UNKNOWN** | Phase 7+ not visible. Cannot confirm. |
| C-15 | Each exclusion answers test-validity | **PASS** | PHASE 2: per-exclusion bullet format is "Item excluded: Why the test remains valid without it." "Bare labels without rationale fail this phase." Structural rejection of empty rationale. |
| C-16 | Counter-evidence question explicitly closed | **UNKNOWN** | PHASE 6 body cut off. From the opening line, the phase may produce a closure disposition -- but the enforcement mechanism is not visible. Cannot confirm C-16 compliance. |
| C-17 | Rationale co-located with anchor | **PASS** (visible phases) | PHASE 2 bullet format: `[Item excluded]: [rationale]` -- co-located per bullet. PHASE 5 labeled-pair block: `**Why the delta is what it is**: [explanation]` in same block as `**Delta**`. PHASE 3 labeled-pair block: success/failure conditions in same block as metric. C-17 pass condition explicitly permits "labeled pair" format, which V-02's block structure satisfies for all visible anchors. |

**Confirmed composite: 80 / 120**
*(C-01 12 + C-02 12 + C-03 12 + C-04 12 + C-06 10 + C-07 10 + C-11 1 + C-12 2 + C-13 2 + C-15 2 + C-17 5)*
**Unknown criteria: C-05 (12) + C-08 (10) + C-09 (5) + C-10 (5) + C-14 (2) + C-16 (5) = 39 pts potential**
**Score range: 80 to 119 / 120**
**Essential verdict: UNKNOWN -- C-05 (verdict rendered) not confirmable from visible phases; 4/5 essentials confirmed PASS**

*Note: V-02's Phase Gates architecture is strong throughout the visible phases. All observed enforcement mechanisms are explicit -- gate labels, per-item rationale requirements, labeled-pair co-location. The 80-pt confirmed floor is high; the cutoff, not the design, limits this assessment.*

---

## V-03, V-04, V-05

**Not provided.** Cannot score.

---

## Ranking (scorable variations)

| Rank | Variation | Score | Essential Pass | Verdict |
|------|-----------|-------|----------------|---------|
| 1 | V-01 (Table-Driven, Rationale Co-Located) | 120 / 120 | All 5 confirmed | Golden |
| -- | V-02 (Phase Gates, Lifecycle Emphasis) | 80-119 / 120 | 4/5 confirmed | Cannot determine (prompt incomplete) |
| -- | V-03, V-04, V-05 | -- | -- | Not provided |

---

## Excellence Signals from V-01

**Signal 1 -- Explicit two-path closure enforces C-16 naturally**
Section 6 does not ask "address any counter-evidence." It requires one of exactly two dispositions. The forced-branch structure eliminates any exit path that leaves the section open. This pattern generalizes: any section with a nullable outcome (counter-evidence may or may not exist; limitation may or may not apply) can be closed structurally by naming both possible states and requiring one to be selected.

**Signal 2 -- Column header as per-row criterion enforcer**
Section 2's fourth column is titled verbatim the test-validity question. The model must answer that exact question in every Out-of-Scope row. V-01 deploys this mechanism in three sections (scope, results, verdict). Column headers are load-bearing criterion enforcement, not decorative labels.

**Signal 3 -- Output contract block at end functions as a closing gate**
The Structural Rules block at the end restates ordering, population, and delta requirements after all section instructions. This creates a second enforcement pass after all content is generated -- the model verifies its own output against the contract. V-02's phase markers fire at point-of-construction only; V-01's contract fires both during and after.

**Signal 4 -- Format-first design pre-satisfies criteria not yet written**
V-01 did not require new Section 6 text to satisfy C-16 -- the two-path disposition language was already present in the original design. It did not require a C-17 reminder -- the tables already co-located rationale by construction. Well-designed structural formats satisfy rubric criteria before those criteria exist. This is a meta-signal about format-first prompt design.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["explicit-two-path-closure-enforces-c16", "phase-execute-marker-as-inline-temporal-lock", "labeled-pair-block-achieves-c17-without-tables"]}
```
