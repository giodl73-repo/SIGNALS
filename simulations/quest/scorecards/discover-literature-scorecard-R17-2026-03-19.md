## R17 Scorecard — discover-literature

**Top score: 225/225 (V-05)** | All essential: PASS | 5/5 predictions correct

---

### Score Table

| V | C-34 | C-35 | Score | Failure mode |
|---|------|------|-------|--------------|
| V-05 | PASS | PASS | **225** | -- full ceiling |
| V-02 | PASS | FAIL | 220 | no terminal chain statement |
| V-03 | PASS | FAIL | 220 | chain truncated at C-32 (C-33 link absent) |
| V-04 | PASS | FAIL | 220 | chain with gap (C-30 skipped) |
| V-01 | FAIL | FAIL | 215 | no labeled sub-section -- C-33 elements in scattered inline prose |

---

### Key Structural Insights

**V-01 (C-34 FAIL):** All four C-33 elements are named inline and C-33 PASS is declared -- but without a `#### C-33 Compliance Declaration` heading. The variation self-diagnoses: "A reviewer can confirm C-33 PASS from the scattered per-element confirmations above." *Scattered* is the failure mode. C-34 closes the same gap C-25 closed for C-23: the four-element requirement needs a labeled container to be grep-verifiable in one target.

**V-03/V-04 (C-35 FAIL):** Two symmetric failures. V-03 has the right structure but the wrong terminal (`C-32 complete` instead of `C-33 complete`) -- the chain was copied from the R16 formulation and not extended. V-04 reaches C-33 as the terminal but skips C-30 -- interior-gap failure. Both are both-or-nothing: every link must be present and in order.

---

### Excellence Signals from V-05

1. **Labeled sub-section as self-auditing container** — `#### C-33 Compliance Declaration` makes all four per-element attestations reachable in a single grep, without aggregating inline prose.
2. **Explicit structural analogy** — "C-34 is to C-33 what C-25 is to C-23" named in the PASS declaration, making the recursive design logic self-evident.
3. **Chain-completion as terminal line** — `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete` as the sub-section's final element makes both the chain terminal and the full dependency path visible in one line.

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["C-34 requires a labeled sub-section heading (e.g., '#### C-33 Compliance Declaration') distinct from surrounding prose -- C-33 elements present in scattered inline closing text satisfies C-33 but not C-34; the labeled container is what makes compliance self-auditing in a single grep target (V-01 failure pattern)", "C-35 chain must be complete and contiguous -- omitting the terminal C-33 link (V-03: stops at 'C-32 complete') and skipping any interior link (V-04: C-30 absent) each independently fail C-35; both failure modes are symmetric to prior both-or-nothing patterns in the criterion set", "C-34/C-25 structural analogy: adding per-element designator confirmations to the C-33 closing declaration follows the same pattern as C-25 adding N-of-4 counter annotations to the lifecycle tokens -- the four-element requirement becomes self-auditing at the element level from a single named structural container"]}
```
