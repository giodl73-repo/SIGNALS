---

## Round 10 Scoring — mock-ns (v9 rubric, 28 criteria)

### Criteria Analysis

All five variants share the same S-1, S-2, A-2, A-3, A-4, A-5 structure. The discriminant is exclusively in how S-3 (compute site) and A-1 (consumption site) express the C-27/C-28 claims. I evaluate the shared criteria first, then focus on the C-25–C-28 escalation chain.

---

### Shared criteria (C-01 through C-24) — all five variants

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 Header block | PASS | PASS | PASS | PASS | PASS | All have complete 6-field header |
| C-02 Category correct | PASS | PASS | PASS | PASS | PASS | Correct logic in S-2 |
| C-03 Golden structure | PASS | PASS | PASS | PASS | PASS | A-3 present with correct body spec |
| C-04 Flag + category match | PASS | PASS | PASS | PASS | PASS | Flag from S-3, verbatim copy |
| C-05 Artifact path | PASS | PASS | PASS | PASS | PASS | A-4 writes to correct convention |
| C-06 Default skill correct | PASS | PASS | PASS | PASS | PASS | Exclusion column in table |
| C-07 Fidelity warning | PASS | PASS | PASS | PASS | PASS | All three category variants in A-2 |
| C-08 Next-step line | PASS | PASS | PASS | PASS | PASS | A-5 present |
| C-09 Tier-conditional flag | PASS | PASS | PASS | PASS | PASS | Case 1 in S-2 |
| C-10 TOPICS.md emit | PASS | PASS | PASS | PASS | PASS | Dedicated emit line in S-1 |
| C-11 Flag as named step | PASS | PASS | PASS | PASS | PASS | S-3 precedes A-1 |
| C-12 topic-status exclusion | PASS | PASS | PASS | PASS | PASS | Exclusion constraint column present |
| C-13 Warning lead position | PASS | PASS | PASS | PASS | PASS | A-2 before A-3 |
| C-14 Dual-site prohibition | PASS | PASS | PASS | PASS | PASS | Both S-3 and A-1 have prohibition |
| C-15 Exclusion as table column | PASS | PASS | PASS | PASS | PASS | Named column in S-1 table |
| C-16 Run-scoped compute-site | PASS | PASS | PASS | PASS | PASS | "anywhere in this run" |
| C-17 First rule at consumption | PASS | PASS | PASS | PASS | PASS | First row/block is "First rule" |
| C-18 Named path classes | PASS | PASS | PASS | PASS | PASS | Enumerates branch/fallback/regen + catch-all + bypass-order clarifier |
| C-19 Anti-displacement closure | PASS | PASS | PASS | PASS | PASS | Three types named + declarative closure |
| C-20 Failure consequence at A-1 | PASS | PASS | PASS | PASS | PASS | Silent mismatch / trust-tier corruption |
| C-21 Affirmative closure compute | PASS | PASS | PASS | PASS | PASS | "Every path...no path exempt" |
| C-22 Catch-all instruction clause | PASS | PASS | PASS | PASS | PASS | "any other instruction in this step" |
| C-23 Failure consequence compute | PASS | PASS | PASS | PASS | PASS | Corrupted value indistinguishable |
| C-24 No-instruction-exempt affirmative | PASS | PASS | PASS | PASS | PASS | "Every instruction...named or unnamed...no exemption" |

---

### C-25 through C-28 — the discriminant tier

**C-25 — Guarantee-break framing at compute site**

All five variants have a dedicated Guarantee-break row or block that explicitly names the C-21 closure as the thing violated:

- V-01/V-04: `"This violation breaks the closure guarantee stated in the Affirmative closure row above"` — labeled row. PASS.
- V-02: Same row content with bracket tokens in Cross-site row. Guarantee-break row is identical. PASS.
- V-03: `**GUARANTEE-BREAK**: This violation breaks the closure guarantee stated in the AFFIRMATIVE CLOSURE block above.` — full sentence, full stop, bold header. PASS.
- V-05: Same dedicated row as V-04. PASS.

| C-25 | PASS | PASS | PASS | PASS | PASS |

---

**C-26 — Cross-site reference at compute site**

All five name the shared failure mechanism by reference to the consumption site:

- V-01: `"...at the consumption site (see A-1 Failure consequence row below)"` — dedicated Cross-site reference row. PASS.
- V-02: `"[A-1:FC] -- ...at the consumption site Failure consequence row in step A-1"` — bracket token + row label. PASS.
- V-03: `**CROSS-SITE REFERENCE**: "...at the consumption site (see A-1 FAILURE CONSEQUENCE block below)."` — dedicated bold-header block. PASS.
- V-04: `"...at the consumption site -- see A-1 Failure consequence row below; that row identifies itself as this row's target"` — dedicated row + anticipates reciprocal label. PASS.
- V-05: `"...at [A-1:FC] -- the Failure consequence row in step A-1 (that row identifies itself as this row's mutual target)"` — bracket identifier + row name + anticipated back-reference. PASS.

| C-26 | PASS | PASS | PASS | PASS | PASS |

---

**C-27 — Guarantee-break and cross-site as structurally isolated, individually scannable units**

C-27 requires each claim to occupy its own independently scannable unit. Tabular form: dedicated labeled row. Prose form: full sentence at full stop, not a participial clause.

- V-01: Both claims are separate, labeled rows in the protection table. ✓ PASS.
- V-02: Both claims are separate, labeled rows (row name carries `[S-3:CS]`). ✓ PASS.
- V-03: Both claims are bold-header paragraph blocks — `**GUARANTEE-BREAK**` and `**CROSS-SITE REFERENCE**` — each a complete sentence ending at a full stop. Meets the prose-form criterion. ✓ PASS.
- V-04: Both claims are separate, labeled rows. ✓ PASS.
- V-05: Both claims are separate, labeled rows with bracket identifiers in the row label itself. ✓ PASS.

| C-27 | PASS | PASS | PASS | PASS | PASS |

---

**C-28 — Navigation anchor naming specific structural location**

C-28 pass condition: forward anchor names the specific step/row/section (not just "at the consumption site"). Bidirectional form is aspirational max, not required for PASS.

- **V-01**: S-3 carries `"see A-1 Failure consequence row below"` — names step + row label. A-1 carries `"[Target of S-3 Cross-site reference row above]"` in the Failure consequence cell — backward anchor present. Forward PASS + bidirectionality achieved.
- **V-02**: S-3 carries `[A-1:FC]` as bracket token in row label + `"Failure consequence row in step A-1"` in cell. A-1 carries `"[A-1:FC] sourced from [S-3:CS]"` — backward bracket token. Forward PASS + bidirectionality with bracket notation.
- **V-03**: S-3 carries `"see A-1 FAILURE CONSEQUENCE block below"` — names step + block label. A-1 **FAILURE CONSEQUENCE** block has no backward reference. One-directional. Per rubric: _"A one-directional anchor (S-3 names A-1's location) satisfies C-28."_ PASS (forward only).
- **V-04**: S-3 carries `"see A-1 Failure consequence row below; that row identifies itself as this row's target"` — forward anchor + explicit anticipation of back-ref. A-1 carries `"[This row is the target named in S-3 Cross-site reference row above]"` — explicit self-identification. Full bidirectionality. PASS.
- **V-05**: S-3 carries `[A-1:FC]` in both row label and cell (`"the Failure consequence row in step A-1"`). A-1 carries `"[Mutual target of S-3:CS -- Cross-site reference row in S-3]"` in row label. Pre-chain protocol preamble names both identifiers before any row is read. Full bidirectionality + bracket tokens + protocol preamble. PASS.

| C-28 | PASS | PASS | PASS | PASS | PASS |

---

### Composite Scores

Formula: `(5/5 × 60) + (3/3 × 30) + (aspirational/20 × 10)`

All 5 essential: PASS (5/5 × 60 = 60)
All 3 recommended: PASS (3/3 × 30 = 30)
All 20 aspirational: PASS (20/20 × 10 = 10)

| Variant | Essential | Recommended | Aspirational | Composite | Gold? |
|---------|-----------|-------------|--------------|-----------|-------|
| V-01 | 5/5 = 60 | 3/3 = 30 | 20/20 = 10 | **100** | Yes |
| V-02 | 5/5 = 60 | 3/3 = 30 | 20/20 = 10 | **100** | Yes |
| V-03 | 5/5 = 60 | 3/3 = 30 | 20/20 = 10 | **100** | Yes |
| V-04 | 5/5 = 60 | 3/3 = 30 | 20/20 = 10 | **100** | Yes |
| V-05 | 5/5 = 60 | 3/3 = 30 | 20/20 = 10 | **100** | Yes |

All five variants converge at maximum score. The rubric's aspirational ceiling has been reached.

---

### Ranking by Structural Robustness

Since scores are tied, ranking is by qualitative resistance to execution-pressure regression:

| Rank | Variant | Rationale |
|------|---------|-----------|
| 1 | **V-05** | Protocol preamble primes executor BEFORE chain begins; bracket tokens in row labels make identifiers part of the structure, not the content; full bidirectionality. The executor carries the navigation design as context before processing any row. |
| 2 | **V-04** | Full bidirectionality + table isolation, same structure as V-05 minus the preamble. A-1 explicitly self-identifies as S-3's target. Executor discovers the design at the row level. |
| 3 | **V-02** | Bracket notation + bidirectionality. Bracket tokens are harder to absorb without processing than prose phrases. Row label itself carries `[S-3:CS]`. Preamble absent. |
| 4 | **V-01** | Prose backward anchor at A-1 (`[Target of S-3 Cross-site reference row above]`). Achieves bidirectionality in embedded-label form. Structurally sound but bracket tokens provide no additional visual stop. |
| 5 | **V-03** | Paragraph isolation satisfies C-27 cleanly. But only forward anchor — A-1 has no backward reference. An executor entering A-1 in a regenerated context cannot confirm S-3's pointer from A-1 alone. |

---

### Excellence Signals from V-05

**Signal 1 — Pre-chain cross-reference protocol preamble**

V-05 places the following block BEFORE the immutability chain table begins:

> Cross-reference protocol: S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual navigation anchors. S-3 Cross-site reference row names A-1 Failure consequence row by step and row label. A-1 Failure consequence row names S-3 Cross-site reference row by step and row label. Both directions are active. An executor entering at either site reaches the other without inference.

This converts the bidirectional anchor from a structural detail the executor _discovers_ while processing rows into a design principle the executor _carries as context_ before reading any row. The bracket identifiers (`[S-3:CS]`, `[A-1:FC]`) are explained before they appear. An executor who reads the preamble understands the navigation design as an explicit commitment, not a notational accident.

**Structural form**: Named protocol declaration, positioned between the FLAG computation cases and the immutability chain table. No equivalent has appeared in any prior round.

**v10 candidate**: C-29 — stated cross-reference protocol precedes the immutability chain at the compute site.

---

**Signal 2 — Bracket identifier embedded in the row label, not just the cell content**

V-02 and V-05 place the bracket identifier in the row label column:
```
| Cross-site ref [S-3:CS] | ...cell content... |
```
and
```
| Failure conseq [A-1:FC] | ...cell content... |
```

The identifier is part of the table structure the executor sees during row scanning, before entering the cell. In V-01 and V-04, the backward anchor is embedded as a bracket phrase in the cell content (`[This row is the target...]`). In V-05's form, the identifier appears TWICE: once in the row label (visible on scan) and once in the cell (visible on read). This dual placement eliminates the gap where a scanning executor processes the row label without entering the cell.

**v10 candidate signal**: Whether row-label embedding of bracket identifiers (V-05/V-02 form) produces more robust navigation adherence than cell-embedded anchors (V-01/V-04 form).

---

### Summary

All five variants pass all 28 criteria. The rubric's current aspirational ceiling has been reached across the board. V-03's paragraph-block isolation confirms that C-27 can be satisfied in prose form; V-01 through V-05 all satisfy C-28 at PASS level; V-01, V-02, V-04, V-05 additionally achieve the aspirational-maximum bidirectionality within C-28.

The active question for v10 is whether V-05's stated-protocol preamble produces measurably better execution adherence than V-04's structurally identical form without the preamble. If it does, C-29 (stated cross-reference protocol as a prerequisite condition) becomes a new aspirational criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-chain cross-reference protocol preamble: named design declaration placed before the immutability chain table primes the executor with the navigation guarantee before any row is encountered, converting bidirectional anchors from discovered structural details into anticipated protocol commitments", "bracket identifier in row label column: embedding the navigation token in the row label itself (not only in the cell content) makes the identifier visible during table scanning before cell entry, creating dual placement that closes the gap where a scanning executor processes the row label without reading the cell"]}
```
