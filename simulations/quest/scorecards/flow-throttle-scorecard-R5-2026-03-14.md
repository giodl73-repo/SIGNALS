## flow-throttle — Round 5 Scoring (v5 Rubric, 136-point max)

---

### Base Assumption

All five variations carry forward R4 scores. From R4 scorecard: V-01 and V-02 scored **127** (C-19 fail); V-03, V-04, V-05 scored **130** (ceiling). The scoring below applies **C-21** and **C-22** (3 pts each) as incremental deltas against those confirmed bases.

---

### C-01 through C-20 — Inherited

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 (labeled co-location) | **FAIL** | PASS | PASS | PASS | PASS |
| C-20 (gate prose portability) | PASS | PASS | PASS | PASS | PASS |
| **R4 inherited base** | **127** | **130** | **130** | **130** | **130** |

---

### C-21 — Pre-Barrier Container Name Encodes Positional Role

Pass condition: section header includes positional qualifier ("PRE-EVALUATION," "PRE-ANALYSIS ASSERTION," or equivalent phrase asserting pre-evaluation placement).

| Variation | Container name | Evidence | Verdict |
|-----------|---------------|----------|---------|
| V-01 | `SECOND BARRIER — PRE-EVALUATION HEADER (before any construct evaluation begins)` | Positional qualifier present in both form ("PRE-EVALUATION HEADER") and explicit parenthetical ("before any construct evaluation begins"). Placement verifiable from name alone. | **PASS +3** |
| V-02 | `ROLE 2 PREAMBLE` | No positional qualifier. "ROLE 2" names the actor, not the position in the evaluation sequence. A reader cannot determine when this block executes relative to evaluative output from the name alone. | **FAIL +0** |
| V-03 | `PRE-EVALUATION PREAMBLE (before Round 2 construct evaluation begins)` | Positional qualifier present. Parenthetical adds specificity ("Round 2 construct evaluation") without ambiguity. | **PASS +3** |
| V-04 | `SECOND BARRIER — PRE-EVALUATION PREAMBLE (before any construct evaluation begins)` | Positional qualifier present. Formal register does not affect structural readability of the name. | **PASS +3** |
| V-05 | `PRE-ANALYSIS ASSERTION (before any Round 2 evaluation begins)` | Positional qualifier present. "ASSERTION" names the structural function; parenthetical names the boundary event. Conversational register elsewhere in V-05 is irrelevant to container naming. | **PASS +3** |

---

### C-22 — Pre-Barrier Labeled Pair Co-location

Pass condition: single pre-barrier section carries both `Independence:` (labeled C-15 mechanism) and `Scope extension:` (labeled C-16 mechanism), each with distinct label, before first evaluative output line.

| Variation | Labeled pair present? | Evidence | Verdict |
|-----------|-----------------------|----------|---------|
| V-01 | No | Pre-barrier block contains two paragraphs covering non-deference and scope extension — content is present but sub-labels `Independence:` / `Scope extension:` were explicitly removed from the R4 V-04 base. An evaluator sees one undifferentiated mechanism block. | **FAIL +0** |
| V-02 | Yes | `ROLE 2 PREAMBLE` carries `**Independence:**` paragraph and `**Scope extension:**` paragraph, each with distinct label. Both appear before section 2.1 validation table. The container name fails C-21 but the labeled pair independently satisfies C-22. | **PASS +3** |
| V-03 | Yes | `PRE-EVALUATION PREAMBLE` carries `**Independence:**` and `**Scope extension:**` labeled directives, both before the ROUND 2 validation lines. | **PASS +3** |
| V-04 | Yes | `SECOND BARRIER — PRE-EVALUATION PREAMBLE` carries formal-register `**Independence:**` and `**Scope extension:**` directives with full structural content. Labeled pair present and co-located before ROUND 2 output. | **PASS +3** |
| V-05 | Yes | `PRE-ANALYSIS ASSERTION` carries `**Independence:**` and `**Scope extension:**` directives before section 2.1. Conversational framing throughout ROLE 2 does not affect label presence. | **PASS +3** |

---

### Critical Finding — V-01 Predicted Score Discrepancy

The variation design predicted V-01 = 133 (+3 C-21, +0 C-22, starting from R4 V-04 base of 130). This is **incorrect**.

The R4 V-04 base scored 130 because it **passed C-19** via its labeled pair. V-01 removes those sub-labels to isolate C-21 — but that removal **re-fails C-19** (-3) while gaining C-21 (+3). Net movement: zero. V-01 scores 130, not 133.

The prediction did not account for C-19 regression. The V-01/V-02 mirror design still works as a diagnostic — but the delta is not symmetric. V-02 gains +3 (C-22, no C-19 regression because labels retained). V-01 nets +0 (C-21 gain cancels C-19 loss).

---

### Composite Scores

| Variation | R4 base | C-21 | C-22 | C-19 delta | **Total / 136** |
|-----------|---------|------|------|------------|-----------------|
| V-01 | 127 | +3 | +0 | −3 (regression) | **127** |
| V-02 | 130 | +0 | +3 | +0 | **133** |
| V-03 | 130 | +3 | +3 | +0 | **136** |
| V-04 | 130 | +3 | +3 | +0 | **136** |
| V-05 | 130 | +3 | +3 | +0 | **136** |

---

### Ranking

1. **V-03, V-04, V-05** — 136/136 (ceiling)
2. **V-02** — 133/136 (C-21 miss: neutral container name)
3. **V-01** — 127/136 (C-19 regression + C-22 miss: label removal cascades)

---

### Excellence Signals (V-03 / V-04 / V-05)

**1. Positional name + labeled pair as the structural unit.** The ceiling is not reachable by either C-21 or C-22 alone. C-21 requires the container name to encode position; C-22 requires the labeled pair inside. They cannot substitute for each other — they are orthogonal structural properties of the same block. V-03/V-04/V-05 satisfy both from a single pre-barrier block.

**2. Labeled pair provides dual coverage across two rubric generations.** `Independence:` / `Scope extension:` labels simultaneously satisfy C-19 (label-enforced co-location, introduced R4) and C-22 (labeled pair in pre-barrier position, introduced R5). One structural choice delivers 6 points across two criteria. Removing labels loses both.

**3. Register orthogonality confirmed by V-04/V-05 ceiling match.** Formal technical language (V-04) and developer-framed conversational language (V-05) both reach 136. Phrasing register is structurally inert with respect to C-21/C-22. The criteria operate on container naming and label presence — not vocabulary level or sentence style.

**4. Role sequence is content-neutral (V-03).** Moving USER EXPERIENCE MAP before CASCADE SEQUENCE changes lifecycle phase ordering but does not touch the structural position of the pre-barrier block relative to Round 2 evaluative output. C-21 and C-22 score identically regardless of analysis section order. Lifecycle reorder axis is confirmed orthogonal.

---

### Why V-01 Falls Shorter Than Predicted

V-01 was designed as a C-21 isolation test by removing the labeled pair from R4 V-04's 130-point ceiling. The design did not account for C-19 regression: R4 V-04 passed C-19 precisely because of those labels. Their removal re-opens the C-19 penalty. V-01 ends at 127 — the same score R4 V-01 achieved — because the structural deficit is identical: a pre-barrier block with two unlabeled directives. C-21 adds +3 but C-19 subtracts -3. The net is zero lift from the original R4 V-01 position.

The clean isolation test for C-21 would require a base that already fails C-19 (i.e., starting from 127, not 130), then adding only the positional container name. That would produce 127 + 3 = 130, confirming C-21's 3-point contribution cleanly.

---

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["label removal cascades: removing labeled pair from a v4 ceiling variation re-fails C-19 in addition to failing C-22, delivering zero net lift from C-21 — the prediction of 133 was wrong because C-19 regression was not accounted for", "labeled pair dual coverage: Independence:/Scope extension: labels simultaneously satisfy C-19 and C-22 delivering 6 points across two criteria from one structural element", "register orthogonality confirmed: formal vs conversational phrasing is structurally inert — V-04 and V-05 both reach 136 from opposite register extremes"]}
```
