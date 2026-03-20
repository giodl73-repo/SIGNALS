Scorecard written to `simulations/quest/scorecards/discover-literature-scorecard-R17-2026-03-20.md`.

---

## R17 Score Results

**Top score: 225/225 (V-05)** | All essential: PASS

---

### Summary

All five variations are identical on C-01 through C-33 (all PASS, identical to R16 V-05 baseline of 215). C-34 and C-35 are the sole differentiators.

| V | Score | C-34 | C-35 | Failure mode |
|---|-------|------|------|--------------|
| V-05 | **225** | PASS | PASS | -- full ceiling |
| V-02 | 220 | PASS | FAIL | no terminal chain statement |
| V-03 | 220 | PASS | FAIL | chain truncated at C-32 -- C-33 link absent |
| V-04 | 220 | PASS | FAIL | chain with gap -- C-30 skipped |
| V-01 | 215 | FAIL | FAIL | no labeled sub-section -- C-33 elements in scattered inline prose |

---

### Per-Variation Analysis

---

#### V-01 -- C-33 PASS via scattered inline prose, no labeled sub-section

**C-33 content (exact):**

After the C-32 PASS declaration, the block closes with:
> "C-33(a) confirmed -- C-32(a) named by sub-clause designator... C-33(b) confirmed -- C-32(b) named by sub-clause designator... C-33(c) confirmed -- both-or-nothing property stated explicitly... C-33(d) confirmed -- C-32 PASS declared within this block. C-33 PASS: all four C-33 elements present in the preceding C-32 PASS declaration; C-32 compliance is self-announcing from the block's closing. A reviewer can confirm C-33 PASS from the scattered per-element confirmations above."

**C-33 verdict: PASS.** All four elements present as a closing statement within the block. C-33 pass condition allows "labeled sub-section or final statement within the block" -- this is a final statement. (a) C-32(a) named, (b) C-32(b) named, (c) both-or-nothing stated, (d) C-32 PASS declared. C-33 PASS.

**C-34 verdict: FAIL.** No `#### C-33 Compliance Declaration` heading or equivalent labeled sub-section. The C-33 elements are present but as inline prose following the C-32 PASS paragraph -- "scattered per-element confirmations" is the variation's own description. C-34 requires a labeled sub-section DISTINCT from surrounding C-33-declaring text. A reviewer cannot grep a single structural element to confirm all four per-element attestations in one target. C-34 FAIL implies C-35 FAIL (C-34 FAIL blocks C-35).

**C-35 verdict: FAIL** (blocked by C-34 FAIL; also no chain statement present).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-32 | PASS | Identical to R16 V-05 baseline |
| C-33 | PASS | All four elements in closing statement within block |
| C-34 | **FAIL** | No labeled sub-section -- C-33 elements in scattered inline prose |
| C-35 | **FAIL** | C-34 FAIL blocks C-35; no chain statement present |

**Score: 215/225**

---

#### V-02 -- Labeled sub-section with 4 per-element confirmations, no C-35 chain statement

**C-34 sub-section (exact):**
```
#### C-33 Compliance Declaration
- C-33(a): C-32(a) named by sub-clause designator -- confirmed.
- C-33(b): C-32(b) named by sub-clause designator -- confirmed.
- C-33(c): both-or-nothing property stated explicitly -- confirmed.
- C-33(d): C-32 PASS declared within this block -- confirmed.
C-33 PASS. A reviewer reading only this labeled sub-section can confirm all four C-33 elements
without reading PLACEMENT and CELL-SOURCE fields individually -- C-33 compliance is self-auditing
from this named element. C-34 PASS: each C-33 element named by designator with per-element
confirmed attestation within this labeled sub-section.
```

No chain statement follows C-33 PASS.

**C-34 verdict: PASS.** `#### C-33 Compliance Declaration` is the labeled sub-section. C-33(a)(b)(c)(d) each named by designator with "confirmed" attestation. C-33 PASS declared within the sub-section. All four per-element confirmations and the C-33 PASS declaration appear within the labeled sub-section. C-34 PASS.

**C-35 verdict: FAIL.** No terminal chain-completion statement anywhere in the sub-section. After "C-34 PASS" the sub-section ends. The canonical `C-14 + C-23 -> ... -> C-33 complete` is absent. C-35 requires the statement to be within the C-34 sub-section boundary -- absence is C-35 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R16 V-05 baseline + C-34 sub-section satisfies C-33 |
| C-34 | **PASS** | Labeled `#### C-33 Compliance Declaration` with four per-element attestations |
| C-35 | **FAIL** | No chain statement -- sub-section ends after "C-34 PASS" |

**Score: 220/225**

---

#### V-03 -- Labeled sub-section + chain truncated at C-32, terminal link omitted

**C-34 sub-section (exact):**
```
#### C-33 Compliance Declaration
- C-33(a): confirmed.
- C-33(b): confirmed.
- C-33(c): confirmed.
- C-33(d): confirmed.
C-33 PASS. C-34 PASS: each C-33 element named by designator with per-element confirmed
attestation within this labeled sub-section.
Dependency chain: C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 complete.
```

**C-34 verdict: PASS.** Labeled sub-section with all four C-33 per-element attestations present. C-33 PASS declared within the sub-section. C-34 PASS.

**C-35 verdict: FAIL.** Chain statement present but truncated: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 complete`. The final `-> C-33 complete` link is absent. C-35 requires the full chain through C-33 as the terminal element -- stopping at C-32 omits C-33, which is the current chain terminal. C-35 FAIL.

**Diagnosis:** This is the off-by-one truncation failure. The chain lists every link that was in the R16 dependency chain (which ended at C-32), but fails to add the new C-33 terminal. The chain's own declared terminal (`C-32 complete`) contradicts the enclosing sub-section's claim (`C-33 PASS`).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Baseline |
| C-34 | **PASS** | Labeled sub-section with per-element attestations |
| C-35 | **FAIL** | Chain ends `C-32 complete` -- C-33 terminal link absent |

**Score: 220/225**

---

#### V-04 -- Labeled sub-section + chain with gap (C-30 skipped)

**C-34 sub-section (exact):**
```
#### C-33 Compliance Declaration
- C-33(a): confirmed.
- C-33(b): confirmed.
- C-33(c): confirmed.
- C-33(d): confirmed.
C-33 PASS. C-34 PASS: each C-33 element named by designator with per-element confirmed
attestation within this labeled sub-section.
Dependency chain: C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-31 -> C-32 -> C-33 complete.
```

**C-34 verdict: PASS.** Labeled sub-section, four per-element attestations, C-33 PASS within sub-section. C-34 PASS.

**C-35 verdict: FAIL.** Chain present and reaches C-33: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-31 -> C-32 -> C-33 complete`. However C-30 is absent -- the chain jumps from C-29 directly to C-31. C-35 requires every link named in order. A gap at any position is C-35 FAIL. The "both-or-nothing" structure extends to the chain: no link may be omitted regardless of how many others are present.

**Diagnosis:** This is the interior-gap failure. The chain reaches the correct terminal (C-33) but skips an intermediate link (C-30). Symmetric to C-28's both-or-nothing: a contiguous chain that arrives at the right destination via an incomplete path does not satisfy C-35.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Baseline |
| C-34 | **PASS** | Labeled sub-section with per-element attestations |
| C-35 | **FAIL** | Chain skips C-30: `... C-29 -> C-31 -> ...` -- interior gap |

**Score: 220/225**

---

#### V-05 -- Full synthesis -- labeled sub-section + complete chain

**C-34 sub-section (exact):**
```
#### C-33 Compliance Declaration
- C-33(a): C-32(a) named by sub-clause designator -- confirmed. (PLACEMENT field carries
  embedded grep instruction declared as C-32(a).)
- C-33(b): C-32(b) named by sub-clause designator -- confirmed. (CELL-SOURCE field carries
  embedded grep instruction declared as C-32(b).)
- C-33(c): both-or-nothing property stated explicitly -- confirmed. (One field operationalized
  and one self-declaring fails C-32; both fields must carry embedded grep instructions.)
- C-33(d): C-32 PASS declared within this block -- confirmed.
C-33 PASS. C-34 PASS: each C-33 element named by designator with per-element confirmed
attestation within this labeled sub-section -- C-34 is to C-33 what C-25 is to C-23: the
four-element compliance requirement is now self-auditing from this labeled sub-section alone
without reading the aggregate C-32 PASS declaration.
C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete.
```

**C-34 verdict: PASS.** `#### C-33 Compliance Declaration` is a labeled sub-section distinct from surrounding prose. Each C-33 element named by designator ((a)(b)(c)(d)) with individual "confirmed" attestation. C-33 PASS declared within the sub-section. All pass conditions met.

**C-35 verdict: PASS.** Terminal chain-completion statement: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete`. Every link present in order: C-14+C-23 (dual root), C-27, C-28, C-29, C-30, C-31, C-32, C-33. Sequential notation (-->) used throughout. Declared complete at C-33. The statement appears as the sub-section's terminal line -- within the C-34 sub-section boundary. C-35 PASS.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Baseline |
| C-34 | **PASS** | Labeled sub-section with four per-element attestations |
| C-35 | **PASS** | Complete contiguous chain through C-33 as terminal element |

**Score: 225/225**

---

### Full Score Table

| Criterion | Weight | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|-----|------|------|------|------|------|
| C-01 through C-05 | essential | 60 | PASS | PASS | PASS | PASS | PASS |
| C-06 through C-08 | recommended | 30 | PASS | PASS | PASS | PASS | PASS |
| C-09 through C-33 | aspirational | 125 | PASS | PASS | PASS | PASS | PASS |
| **C-34** | aspirational | 5 | **FAIL** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-35** | aspirational | 5 | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| **TOTAL** | | | **215** | **220** | **220** | **220** | **225** |

**Ranking:** V-05 (225) > V-02 = V-03 = V-04 (220) > V-01 (215).

---

### Predictions vs. Actuals

| V | Predicted | Actual | Match |
|---|-----------|--------|-------|
| V-01 | 215/225 | 215/225 | YES |
| V-02 | 220/225 | 220/225 | YES |
| V-03 | 220/225 | 220/225 | YES |
| V-04 | 220/225 | 220/225 | YES |
| V-05 | 225/225 | 225/225 | YES |

5/5 predictions correct.

---

### Key Structural Insights

**V-01 is the most important failure** -- and confirms the structural gap C-34 closes. The C-33 elements are all present (as inline confirmations), C-33 PASS is declared, yet C-34 FAIL because there is no labeled sub-section heading. The variation even self-diagnoses: "A reviewer can confirm C-33 PASS from the scattered per-element confirmations above" -- "scattered" is the precise failure mode. C-34 is designed to close this gap: compliance must be auditable from a single named element, not by aggregating across inline prose. The C-24/C-25/C-34 pattern holds: the structural fact (C-33 elements present; four lifecycle tokens present) gains a labeled container making the count verifiable from one grep target.

**V-03 reveals the terminal-link omission failure** -- the chain is complete and sequential up to C-32 but declares "C-32 complete" as the terminal state. This is the off-by-one failure: the chain was copied from the R16 formulation (where C-32 was the terminal) without extending to include C-33. Within the C-33 Compliance Declaration sub-section, the chain terminating at C-32 directly contradicts the sub-section's own C-33 PASS declaration.

**V-04 reveals the interior-gap failure** -- the chain reaches C-33 as the terminal but skips C-30. C-35 requires contiguous ordering of every link. A gap at any position fails C-35 regardless of terminal correctness.

**The two C-35 failure modes (V-03/V-04) are symmetric to two prior both-or-nothing failures:** V-03's terminal-omission parallels V-02/V-03 R11 (Phase-1-only or Phase-4-only C-28 annotation -- one boundary absent). V-04's interior-gap parallels C-29's both-or-nothing requirement -- all elements must be present, not a subset.

---

### Excellence Signals from V-05

1. **C-34 labeled sub-section as the self-auditing container**: `#### C-33 Compliance Declaration` creates a single grep target for all four C-33 per-element attestations. A reviewer scanning the C-30 block need not aggregate across inline text -- the heading marks the boundary; everything within is a complete compliance proof.

2. **Explicit analogy declaration**: V-05 names the design pattern in the C-34 PASS line: "C-34 is to C-33 what C-25 is to C-23 -- the four-element compliance requirement is now self-auditing from this labeled sub-section alone." This makes the recursive structural logic self-evident: annotating each element by designator is exactly what C-25 does for the N-of-4 lifecycle tokens.

3. **Chain-completion statement as the sub-section's terminal line**: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete` appears after the C-33 PASS declaration, making it the final element the reviewer encounters. Two facts are simultaneously self-evident: (1) C-33 is the current chain terminal -- no further criterion extends the chain; (2) the full dependency path is visible in one line without traversing distributed criterion annotations. The additive property holds: the chain statement does not displace any C-34 required element (per-element attestations + C-33 PASS remain present).

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["C-34 requires a labeled sub-section heading (e.g., '#### C-33 Compliance Declaration') distinct from surrounding prose -- C-33 elements present in scattered inline closing text satisfies C-33 but not C-34; the labeled container is what makes compliance self-auditing in a single grep target (V-01 failure pattern)", "C-35 chain must be complete and contiguous -- omitting the terminal C-33 link (V-03: stops at 'C-32 complete') and skipping any interior link (V-04: C-30 absent) each independently fail C-35; both failure modes are symmetric to prior both-or-nothing patterns in the criterion set", "C-34/C-25 structural analogy: adding per-element designator confirmations to the C-33 closing declaration follows the same pattern as C-25 adding N-of-4 counter annotations to the lifecycle tokens -- the four-element requirement becomes self-auditing at the element level from a single named structural container"]}
```
