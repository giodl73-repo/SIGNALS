## Quest Score — `topic:echo` Round 4 (rubric v4)

**Rubric:** v4 | **Max:** 130 | **New criteria:** C-15, C-16

**Baseline:** All 5 variations inherit R3 V-05 full structure. C-01 through C-14 were all PASS at 120/120. The only live question is C-15 and C-16.

---

### Criterion Scoring by Variation

#### Essential (C-01 – C-05): All PASS across all variations

All 5 variations preserve the R3 V-05 role-sequence structure without modification to the surprise entry content or synthesis requirements. C-01 through C-05 are structurally unchanged.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Named surprises | PASS | PASS | PASS | PASS | PASS |
| C-02 Signal tracing | PASS | PASS | PASS | PASS | PASS |
| C-03 Design impact | PASS | PASS | PASS | PASS | PASS |
| C-04 Synthesis not summary | PASS | PASS | PASS | PASS | PASS |
| C-05 Surprise specificity | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 for all five.**

---

#### Recommended (C-06 – C-08): All PASS across all variations

No variation touches the recommended criteria — counterfactual structure, institutional framing, and cross-signal patterns are all inherited from R3 V-05.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Expectation counterfactual | PASS | PASS | PASS | PASS | PASS |
| C-07 Institutional framing | PASS | PASS | PASS | PASS | PASS |
| C-08 Cross-signal pattern | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 for all five.**

---

#### Aspirational (C-09 – C-16)

C-09 through C-14 are inherited unchanged from R3 V-05. Scoring focuses on C-15 and C-16.

**C-15 — Pre-commitment enforcement mechanism declaration** (gate: C-11)

| Variation | Mechanism structure | Verdict | Evidence |
|-----------|-------------------|---------|---------|
| V-01 | Freeze label: "Mechanism: structural provenance (role-scope exclusion) -- the Archivist role operated with no access to signal artifacts; PBI entries were produced from domain knowledge only." | **PASS** | Matches rubric's pass example verbatim: "PBI produced by Archivist role with no access to signal artifacts." Explicitly names the mechanism type. A reviewer can calibrate without content analysis. |
| V-02 | Freeze unchanged: "Archivist complete. PBI frozen. Signal Reader begins." — no mechanism label. | **FAIL** | No mechanism declaration. Reviewer must infer provenance type from role structure alone — exactly the gap C-15 was designed to close. |
| V-03 | Dedicated `## Pre-Commitment Provenance` section with mechanism type, mechanism description, strength hierarchy (structural > temporal), and reviewer calibration statement. | **PASS** | Exceeds pass bar. Mechanism type declared, strength category named, reviewer implication stated. Eliminates reviewer obligation to reason about strength tier. |
| V-04 | Same freeze label as V-01. | **PASS** | Same evidence as V-01. |
| V-05 | Same provenance section as V-03, with full vocabulary and "The information boundary is structural: it is enforced by role sequencing, not by instruction." | **PASS** | Same evidence as V-03, with additional precision. |

**C-16 — Production-time per-entry verification attestation** (gate: C-14)

| Variation | Attestation structure | Verdict | Evidence |
|-----------|----------------------|---------|---------|
| V-01 | Self-check: "A reviewer reading only this entry must be able to verify..." — reviewer-obligation framing, no Verified field. | **FAIL** | Reviewer-framed, not producer-framed. The rubric requires the producer to state what was verified; this shifts the obligation to the reviewer. C-16 explicitly targets this gap from R3 V-05. |
| V-02 | `Verified:` field: "(1) Handle '{handle}' confirmed in Handle Ledger... (2) PBI-Ref 'PB-NN' confirmed... (3) Source '{artifact}' confirmed... All three checks performed at production time before writing this entry." | **PASS** | Names each check individually in declaration language. Rubric pass condition: "an attestation that names each check explicitly is a pass." All three checks are named. |
| V-03 | Self-check unchanged from V-01 — reviewer-framed, no Verified field. | **FAIL** | Same gap as V-01. V-03 addresses C-15 not C-16. |
| V-04 | Same Verified field as V-02. | **PASS** | Same evidence as V-02. |
| V-05 | Verified field with evidentiary quoting: "(2) PBI-Ref 'PB-NN' confirmed; entry reads: '...'; (3) Source '{artifact}' confirmed; finding reads: '...' Audit burden: producer." | **PASS** | Exceeds pass bar. Names checks and quotes actual values. Reviewer can confirm correctness from the Verified field alone without navigating to PBI or Signal Findings. |

**Aspirational subtotal:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Surprise hierarchy | PASS | PASS | PASS | PASS | PASS |
| C-10 Riskiest surprise flagged | PASS | PASS | PASS | PASS | PASS |
| C-11 Pre-committed PBI | PASS | PASS | PASS | PASS | PASS |
| C-12 Named handles | PASS | PASS | PASS | PASS | PASS |
| C-13 Dual phase-locked integrity | PASS | PASS | PASS | PASS | PASS |
| C-14 Single-entry audit trail | PASS | PASS | PASS | PASS | PASS |
| **C-15** Mechanism declaration | **PASS** | **FAIL** | **PASS** | **PASS** | **PASS** |
| **C-16** Per-entry attestation | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **Subtotal (5 pts each)** | **35** | **35** | **35** | **40** | **40** |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** | Golden? |
|-----------|-----------|-------------|--------------|---------------|---------|
| V-01 | 60 | 30 | 35 | **125** | Yes |
| V-02 | 60 | 30 | 35 | **125** | Yes |
| V-03 | 60 | 30 | 35 | **125** | Yes |
| V-04 | 60 | 30 | 40 | **130** | Yes (max) |
| V-05 | 60 | 30 | 40 | **130** | Yes (max) |

---

### Ranking

**Rank 1 (tied): V-04 and V-05 — 130/130**

Both satisfy all 16 criteria. V-04 achieves this with minimal overhead (freeze label + named Verified field). V-05 achieves the same score with richer provenance vocabulary and evidentiary quoting — stronger quality but no additional score within the current rubric.

**Rank 2 (three-way tie): V-01, V-02, V-03 — 125/130**

Each satisfies exactly one of the two new criteria. They are structurally equivalent in score but qualitatively different in which criterion they miss.

---

### Discriminating Question Resolutions

**C-15: Is a freeze label sufficient for PASS, or does the rubric require a provenance section?**

Resolution: **The freeze label (V-01/V-04) satisfies C-15.** The rubric's pass condition is "The artifact declares how its PBI was isolated from signal knowledge." V-01's label "Mechanism: structural provenance (role-scope exclusion) -- the Archivist role operated with no access to signal artifacts" matches the rubric's own example. The provenance section (V-03/V-05) exceeds the pass bar but does not add score — it addresses reviewer calibration burden, which is valuable but not measured by a separate criterion.

**C-16: Does "names each check explicitly" require quoting actual values (V-05) or is naming the check type sufficient (V-02/V-04)?**

Resolution: **Naming the check type is sufficient for PASS (V-02/V-04).** The rubric: "An attestation that names each check explicitly is a pass; a generic 'verified' statement without naming what was verified fails." V-02/V-04 name each of the three checks individually. V-05's evidentiary quoting is stronger (no reviewer inference required) but does not cross a rubric threshold that exists. Both satisfy PASS.

---

### Excellence Signals (V-05 — top-scoring, richest implementation)

**Pattern 1: Evidentiary attestation as self-contained verification record.** V-05's Verified field quotes the actual PBI entry text and Signal Findings text alongside each check name. A reviewer reading only the Verified field can confirm correctness without navigating to either the PBI or Signal Findings sections. This is qualitatively stronger than V-04's named checks, even though both score PASS on C-16.

**Pattern 2: Strength hierarchy as reviewer calibration tool.** V-03/V-05's provenance section explicitly names the two mechanism types and their relative strength ("structural provenance eliminates the contamination path that temporal provenance only sequences"). This eliminates a class of reviewer reasoning — they no longer need to derive the implication of "structural provenance" from first principles.

**Pattern 3: Audit burden attribution.** V-05's "Audit burden: producer" tag in the Verified field makes explicit what C-16 is trying to achieve: the audit chain is the producer's responsibility, not the reviewer's. This label is not required by the rubric but is the most compressed expression of C-16's design intent.

**Pattern 4: Freeze label vs. provenance section as a cost/benefit trade.** V-04 achieves 130/130 with significantly less structural overhead than V-05. The freeze label handles C-15; the Verified field handles C-16. If the goal is full rubric compliance with minimal prompt complexity, V-04 is the efficient choice. If the goal is maximum reviewer confidence with maximum provenance legibility, V-05 is the right choice. Both tie numerically — the choice is an artifact design question, not a rubric question.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["evidentiary-attestation-quotes-actual-values", "provenance-section-explains-strength-hierarchy", "audit-burden-producer-tag", "freeze-label-sufficient-for-C15-pass"]}
```
