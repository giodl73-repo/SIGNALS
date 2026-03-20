Now I have everything I need. Let me score the variations.

## discover-literature Scorecard R18

**Rubric**: v18 (ceiling 230) | **Criterion under test**: C-36

---

### Quick Summary

All five variations inherit the full R17 V-05 baseline: C-01 through C-35 all PASS (225 points). C-36 is the sole differentiator. C-36 has three binding sub-clauses:
- **(a)** names C-34/C-33 as the current pair
- **(b)** names C-25/C-23 as the reference pair
- **(c)** appears within the C-34 labeled sub-section boundary

---

### Per-Variation Analysis

---

#### V-01 — Analogy outside sub-section boundary

**C-34 labeled sub-section content:**
- All four C-33 per-element confirmations present with designators ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete` ✓
- `[End of C-33 Compliance Declaration sub-section]` marks the boundary

**Analogy location:** In prose AFTER the sub-section closes: "Note on recursive design logic: C-34 is to C-33 what C-25 is to C-23 — just as C-25 adds N-of-4 counter annotations..."

Both pairs are named correctly, but the statement appears in surrounding prose after the sub-section boundary. Sub-clause (c) fails.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R17 V-05 baseline |
| C-34 | PASS | Labeled `#### C-33 Compliance Declaration` with four per-element attestations and C-33 PASS |
| C-35 | PASS | `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete` — all links present, correct terminal |
| C-36 | **FAIL** | Both pairs named correctly but analogy appears outside sub-section boundary (after `[End of C-33 Compliance Declaration sub-section]`); sub-clause (c) fails |

**Score: 225/230**

---

#### V-02 — Analogy inside sub-section, current pair only

**C-34 labeled sub-section content:**
- Analogy statement: "C-34 is the per-element annotation upgrade to C-33" — names C-34 and C-33 only
- All four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> ... -> C-33 complete` ✓

Analogy is inside the sub-section boundary (sub-clause (c) satisfied), and names C-34/C-33 as current pair (sub-clause (a) satisfied). But the reference pair C-25/C-23 is absent. Sub-clause (b) fails: the analogy is an assertion without the structural equivalence anchor.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R17 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Full chain through C-33 complete — all links present |
| C-36 | **FAIL** | Analogy inside sub-section names only C-34/C-33; reference pair C-25/C-23 absent; sub-clause (b) fails |

**Score: 225/230**

---

#### V-03 — Analogy inside sub-section, reference pair only

**C-34 labeled sub-section content:**
- Analogy statement: "This follows the same structural pattern as C-25 is to C-23 — C-25 adds per-token N-of-4 counter annotations..." — names C-25/C-23 only
- All four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> ... -> C-33 complete` ✓

Analogy is inside the sub-section (sub-clause (c) satisfied), and names the reference pair C-25/C-23 (sub-clause (b) satisfied). But the current pair C-34/C-33 is absent as a named subject. The statement describes the reference pattern without identifying which criterion is having the pattern applied to it. Sub-clause (a) fails.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R17 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Full chain through C-33 complete |
| C-36 | **FAIL** | Analogy inside sub-section names only C-25/C-23; current pair C-34/C-33 absent as named subject; sub-clause (a) fails |

**Score: 225/230**

---

#### V-04 — Combination: outside sub-section AND only reference pair named

**C-34 labeled sub-section content:**
- No analogy statement within the sub-section
- All four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> ... -> C-33 complete` ✓
- `[End of C-33 Compliance Declaration sub-section]` marks the boundary

**Design note after sub-section:** "this labeled sub-section follows the same pattern as C-25 is to C-23" — outside boundary, names only C-25/C-23.

Two independent failure modes: sub-clause (a) fails (C-34/C-33 not named) AND sub-clause (c) fails (outside sub-section boundary). Either alone would fail C-36.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R17 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Full chain through C-33 complete |
| C-36 | **FAIL** | Analogy outside sub-section AND names only C-25/C-23; sub-clauses (a) and (c) both fail — two independent failure modes |

**Score: 225/230**

---

#### V-05 — Full synthesis: both pairs named inside sub-section

**C-34 labeled sub-section content:**
- Analogy statement (opening): "C-34 is to C-33 what C-25 is to C-23: just as C-25 adds per-token N-of-4 counter annotations to the four lifecycle tokens required by C-23 (making four-token completeness verifiable from any single token without reading all four), C-34 adds per-element designator confirmations to the four C-33 elements required within this closing declaration..."
- All four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain extended: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete`

All three C-36 sub-clauses satisfied:
- (a): C-34/C-33 named as current pair ✓
- (b): C-25/C-23 named as reference pair ✓
- (c): statement appears within `#### C-33 Compliance Declaration` sub-section boundary ✓

Additionally: the chain-completion statement is extended to the new ceiling (C-36), making the chain self-describing at the current depth. This is additive — the required C-33 link is present and ordered; extending to C-36 does not omit any link.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R17 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Full chain through C-33 present and ordered; extended to C-36 — no link omitted |
| C-36 | **PASS** | "C-34 is to C-33 what C-25 is to C-23" inside sub-section; both current pair (C-34/C-33) and reference pair (C-25/C-23) named; all three sub-clauses satisfied |

**Score: 230/230**

---

### Ranking

| Rank | V | Score | C-36 | Failure mode |
|------|---|-------|------|--------------|
| 1 | **V-05** | **230/230** | PASS | — full ceiling |
| 2 | V-01 | 225/230 | FAIL | Analogy outside sub-section boundary |
| 2 | V-02 | 225/230 | FAIL | Reference pair C-25/C-23 absent |
| 2 | V-03 | 225/230 | FAIL | Current pair C-34/C-33 absent as subject |
| 2 | V-04 | 225/230 | FAIL | Two failure modes: outside boundary + current pair absent |

---

### Excellence Signals from V-05

**Excellence Signal 1 — Sub-section boundary is binding**
The analogy statement must appear *within* the `#### C-33 Compliance Declaration` labeled sub-section. V-01 proves that correctly-stated analogy in trailing prose after the sub-section closes fails C-36. The labeled container boundary, not the surrounding content, is the enforcement unit. The C-33/C-36 pattern is exact: C-33 required the closing declaration to be within the C-30 block; C-36 requires the analogy statement to be within the C-34 sub-section.

**Excellence Signal 2 — Both analogy pairs are required; neither substitutes for the other**
V-02 (current pair only) and V-03 (reference pair only) are symmetric failures. Naming C-34/C-33 without C-25/C-23 leaves the analogy as an assertion without a structural anchor. Naming C-25/C-23 without C-34/C-33 describes a pattern without a subject. The structural equivalence is only self-evident when both pairs are named: "X is to Y what A is to B" requires all four terms.

**Excellence Signal 3 — Chain-completion statement tracks the actual current ceiling**
V-05's chain extends to `-> C-34 -> C-35 -> C-36 complete`, reflecting R18's new ceiling. V-01–V-04 stop at `-> C-33 complete` (correct for their 225-ceiling design). The extension to C-36 in V-05 is additive: C-33 remains a link in the correct position, and the chain's terminal reflects the current criterion depth. This pattern — the chain extending to the criterion being introduced — is a new form of self-describing design: the terminal position announces which criterion is newest.

---

### All Essential Criteria

All five variations PASS all essential criteria (C-01 through C-05). The shared baseline from R17 V-05 guarantees this.

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["Structural analogy statement must be embedded within the C-34 labeled sub-section boundary -- trailing prose after the sub-section closes does not satisfy C-36 even when both pairs are named correctly", "Both analogy pairs required simultaneously: current pair C-34/C-33 AND reference pair C-25/C-23 must be named -- naming only one pair leaves the structural equivalence either unanchored (current only) or without a subject (reference only)", "Chain-completion statement extends to the new ceiling criterion (C-36) rather than stopping at C-33 -- the terminal position of the chain tracks the actual current depth, making the chain self-describing about which criterion is newest"]}
```
