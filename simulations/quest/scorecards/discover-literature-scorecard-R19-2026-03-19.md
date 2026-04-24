Now I have everything. Producing the scorecard.

---

## discover-literature Scorecard R19

**Rubric**: v19 (ceiling 235) | **Criterion under test**: C-37 (Chain-Completion Statement Extended to C-36 as Current Terminal)

---

### Quick Summary

All five variations inherit the full R18 V-05 baseline: C-01 through C-36 all PASS (230 points). C-37 is the sole differentiator. C-37 has two binding failure modes:

- **Wrong-terminal failure**: chain ends at a prior ceiling (`C-33 complete`) rather than being extended to include C-34, C-35, C-36
- **Interior-gap failure**: chain reaches C-36 as terminal but skips one or both of the intermediate links (C-34, C-35)

C-37 pass condition: chain reads `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete` — all links enumerated in order, terminal at C-36.

---

### Per-Variation Analysis

---

#### V-01 — Wrong-terminal: chain ends at C-33 complete

**Axis**: Chain-completion statement is the C-35 canonical form — the terminal was not updated when C-34, C-35, or C-36 were added. Chain reads `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete`.

**C-33 Compliance Declaration sub-section content:**
- Structural analogy "C-34 is to C-33 what C-25 is to C-23" present inside sub-section boundary ✓ (C-36 PASS)
- Four C-33 per-element confirmations with designators ✓
- C-33 PASS declared ✓
- Chain terminal: `C-33 complete` — stops before C-34, C-35, C-36

The chain-completion statement was never extended beyond C-33 when C-34, C-35, and C-36 were introduced in R16-R18. Wrong-terminal failure: the statement declares the chain complete at a prior ceiling. C-37 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R18 V-05 baseline |
| C-34 | PASS | Labeled `#### C-33 Compliance Declaration` with four per-element attestations and C-33 PASS |
| C-35 | PASS | Chain-completion statement present and correctly ordered through C-33 |
| C-36 | PASS | "C-34 is to C-33 what C-25 is to C-23" placed inside sub-section, names both current pair (C-34/C-33) and reference pair (C-25/C-23) |
| C-37 | **FAIL** | Chain ends at `C-33 complete` — wrong-terminal failure; C-34, C-35, C-36 not appended; chain not updated from C-35 canonical form |

**Score: 230/235**

---

#### V-02 — Interior-gap: C-34 skipped

**Axis**: Chain reaches C-36 as terminal but omits the C-34 link (added in R16). Chain reads `... -> C-33 -> C-35 -> C-36 complete`.

**C-33 Compliance Declaration sub-section content:**
- Structural analogy present inside sub-section boundary ✓ (C-36 PASS)
- Four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-35 -> C-36 complete` — C-34 absent between C-33 and C-35

The chain reaches C-36 as terminal but skips C-34. Interior-gap failure: the link representing "C-33 compliance declaration structured as a named sub-section with per-element attestations" (the criterion C-34 itself encodes) is missing from the enumerated chain. C-37 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R18 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Chain-completion statement present; terminal reaches C-36 (the extended form attempted) |
| C-36 | PASS | Structural analogy correctly placed inside sub-section boundary with both pairs named |
| C-37 | **FAIL** | Interior-gap failure — chain reads `... -> C-33 -> C-35 -> C-36 complete`; C-34 omitted between C-33 and C-35; any skipped interior link fails C-37 independently |

**Score: 230/235**

---

#### V-03 — Interior-gap: C-35 skipped

**Axis**: Chain reaches C-36 as terminal but omits the C-35 link (added in R17). Chain reads `... -> C-33 -> C-34 -> C-36 complete`.

**C-33 Compliance Declaration sub-section content:**
- Structural analogy present inside sub-section boundary ✓ (C-36 PASS)
- Four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-36 complete` — C-35 absent between C-34 and C-36

The chain reaches C-36 as terminal and correctly includes C-34, but C-35 is skipped. Interior-gap failure: the link representing "terminal dependency chain completion statement" (C-35's contribution) is absent. C-37 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R18 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Chain-completion statement present; includes C-34 as a link |
| C-36 | PASS | Structural analogy correctly placed inside sub-section boundary with both pairs named |
| C-37 | **FAIL** | Interior-gap failure — chain reads `... -> C-33 -> C-34 -> C-36 complete`; C-35 omitted between C-34 and C-36; failure is symmetric to V-02's C-34 omission; either interior gap is independently sufficient to fail |

**Score: 230/235**

---

#### V-04 — Double interior-gap: both C-34 and C-35 skipped

**Axis**: Chain reaches C-36 as terminal but skips both C-34 and C-35. Chain reads `... -> C-33 -> C-36 complete`. Two independent interior-gap failures; either alone sufficient.

**C-33 Compliance Declaration sub-section content:**
- Structural analogy present inside sub-section boundary ✓ (C-36 PASS)
- Four C-33 per-element confirmations present ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-36 complete` — both C-34 and C-35 absent

The chain jumps directly from C-33 to C-36, omitting both intermediate links. This variation confirms that the two interior-gap failures (C-34 absent, C-35 absent) are independent of each other: either alone would fail C-37 for the same reason as V-02 and V-03 respectively. The double-gap form is not a novel failure mode — it combines both interior-gap conditions simultaneously. C-37 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R18 V-05 baseline |
| C-34 | PASS | Labeled sub-section with four per-element attestations and C-33 PASS |
| C-35 | PASS | Chain-completion statement present; reaches C-36 as terminal |
| C-36 | PASS | Structural analogy correctly placed inside sub-section boundary with both pairs named |
| C-37 | **FAIL** | Double interior-gap failure — chain reads `... -> C-33 -> C-36 complete`; both C-34 and C-35 absent; the V-02 failure (C-34 absent) and V-03 failure (C-35 absent) are both present simultaneously; either alone is sufficient to fail |

**Score: 230/235**

---

#### V-05 — Full synthesis: chain correctly extended to C-36

**Axis**: Chain-completion statement extended to include all three new terminal links: C-34, C-35, and C-36. Chain reads `... -> C-33 -> C-34 -> C-35 -> C-36 complete`.

**C-33 Compliance Declaration sub-section content:**
- Structural analogy "C-34 is to C-33 what C-25 is to C-23" present inside sub-section boundary ✓ (C-36 PASS)
- Four C-33 per-element confirmations with designators ✓
- C-33 PASS declared ✓
- Chain: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete`

All links enumerated in order. C-34 appears after C-33 (correct), C-35 after C-34 (correct), C-36 as terminal (correct). No interior gaps. No wrong-terminal failure. C-37 PASS.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 through C-33 | PASS | Identical to R18 V-05 baseline |
| C-34 | PASS | Labeled `#### C-33 Compliance Declaration` with all four per-element attestations and C-33 PASS |
| C-35 | PASS | Chain-completion statement present; all prior links (C-27 through C-33) correctly enumerated |
| C-36 | PASS | Structural analogy "C-34 is to C-33 what C-25 is to C-23" inside sub-section boundary; both current pair and reference pair named |
| C-37 | **PASS** | Chain reads `... -> C-33 -> C-34 -> C-35 -> C-36 complete`; all three new links present in order; terminal at C-36; neither wrong-terminal nor interior-gap failure |

**Score: 235/235**

---

### Ranking

| Rank | Variation | Score | C-37 | Failure mode |
|------|-----------|-------|------|-------------|
| 1 | V-05 | **235/235** | PASS | — full ceiling |
| 2 (tied) | V-01 | 230/235 | FAIL | Wrong-terminal: chain stops at C-33 |
| 2 (tied) | V-02 | 230/235 | FAIL | Interior-gap: C-34 absent |
| 2 (tied) | V-03 | 230/235 | FAIL | Interior-gap: C-35 absent |
| 2 (tied) | V-04 | 230/235 | FAIL | Double interior-gap: both C-34 and C-35 absent |

V-01 through V-04 are exactly tied at 230/235 — each fails C-37 on a distinct and independent failure mode, none of which is more severe than another.

---

### Boundary Confirmations (from R19 failures)

**Wrong-terminal failure confirmed (V-01):** A chain-completion statement that was correct at the C-35 round (ending at `C-33 complete`) remains a C-37 FAIL even if the sub-section is otherwise fully compliant (C-34 PASS, C-36 PASS). The chain terminal must be updated each round as new criteria are added.

**Interior-gap C-34 confirmed independently (V-02):** Reaching C-36 as terminal does not satisfy C-37 if any intermediate link is absent. C-34's absence between C-33 and C-35 fails C-37 even though C-35 and C-36 are present in sequence.

**Interior-gap C-35 confirmed independently (V-03):** Symmetric to V-02. C-35's absence between C-34 and C-36 fails C-37 even though C-34 is correctly included and C-36 is the terminal. Neither interior gap can substitute for the other.

**Double interior-gap confirmed as two independent failures (V-04):** Skipping both C-34 and C-35 produces two simultaneous independent failures. This confirms that each interior-gap failure from V-02 and V-03 is independently sufficient — their coexistence in V-04 does not compound into a different failure mode; it simply confirms both individually.

---

### Excellence Signals (V-05)

**Pattern 1 — Chain-terminal update obligation per round:** Each new criterion added to the dependency chain requires the chain-completion statement to be updated before the round closes. The R19 pattern is exact parallel to C-35/R17: a chain that stopped at `C-32 complete` when C-33 was added became a wrong-terminal failure; a chain that stops at `C-33 complete` when C-34, C-35, and C-36 are added is the same failure one layer deeper. V-05 extends the terminal systematically rather than copying the prior round's formulation.

**Pattern 2 — All intermediate links must be enumerated in order:** The pass condition is not merely "terminal is C-36" — it is "every link from C-14 + C-23 through C-36 appears in sequential order." V-05 demonstrates that C-34 and C-35 must each appear as named intermediate nodes; they cannot be implied by their terminal neighbor appearing correctly. This mirrors the both-or-nothing patterns established throughout the criterion set (C-28, C-29, C-31, C-32, C-33): partial satisfaction of a sequential requirement fails the requirement.

**Pattern 3 — C-36 and C-37 are orthogonal:** C-36 (structural analogy inside sub-section) and C-37 (chain-completion extended to C-36) measure independent structural properties of the same sub-section. All five variations pass C-36; only V-05 passes C-37. A sub-section can be structurally well-formed (analogy correctly placed) while failing the chain-terminal extension obligation, and vice versa. V-05 satisfies both independently.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": []}
```
