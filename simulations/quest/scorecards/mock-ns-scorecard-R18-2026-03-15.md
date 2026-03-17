## mock-ns — Round 18 Scoring (Rubric v17)

---

### Rubric basis

All R18 variations are seeded from R17 V-05, which passes C-01 through C-47 (39/39). The three R18 axes are additive (each adds a property to the P-0 definition site or use-site echo row content) without removing any prior pass condition. The scoring question is therefore: does any addition cause regression, and what new patterns does the top variation seed?

---

### Per-variation evidence summary

**Properties tracked across C-01–C-47 that could be affected by R18 axes:**

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-39/C-43 dual-naming + protocol-failure close at P-0 | PASS (label prepended; text unchanged) | PASS (forward pointer appended; text unchanged) | PASS (P-0 unchanged) | PASS | PASS |
| C-45 use-site anti-bypass echo dual-naming in content cell | PASS | PASS | PASS ("Per P-0 anti-bypass declaration: " prefix + dual-named text intact) | PASS | PASS ("Per P-0, ABD: " prefix + dual-named text intact) |
| C-46 standalone imperative annotation block above template (both sites) | PASS ("**Executor: fill the Match field only. All other fields are pre-filled.**" at S-3 and A-1) | PASS | PASS | PASS | PASS |
| C-47 dedicated "Anti-bypass echo" row in chain table (both sites) | PASS | PASS | PASS | PASS | PASS |

No regression in any criterion across any variation. All five inherit the full 39-criterion pass set.

---

### V-01 — Output Format (ABD label at P-0; echo label = "(P-0, ABD)")

**Change**: P-0 anti-bypass clause gains label `Anti-bypass declaration (ABD):`. Use-site echo row labels become `(P-0, ABD)`.

| Criterion range | Verdict | Evidence |
|---|---|---|
| C-01–C-05 (essential) | PASS | Inherited |
| C-06–C-08 (recommended) | PASS | Inherited |
| C-09–C-45 (aspirational) | PASS | Inherited; P-0 text unchanged, only label prepended |
| C-46 | PASS | Both S-3 and A-1 carry standalone bold imperative block |
| C-47 | PASS | Dedicated "Anti-bypass echo" row at both sites; "(P-0, ABD)" label is clean |

**New aspirational property seeded**: Named anchor at P-0 — the use-site label "(P-0, ABD)" now matches a structural heading "Anti-bypass declaration (ABD):" rather than pointing to prose to scan.

**Score**: 39/39 × 10 = **10.0**

---

### V-02 — Lifecycle Emphasis (P-0 forward pointer naming S-3 and A-1)

**Change**: P-0 anti-bypass clause appends: "Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row." No label; echo row label stays "(P-0 anti-bypass declaration)".

| Criterion range | Verdict | Evidence |
|---|---|---|
| C-01–C-05 (essential) | PASS | Inherited |
| C-06–C-08 (recommended) | PASS | Inherited |
| C-09–C-45 (aspirational) | PASS | Inherited; forward pointer appended after existing dual-named text — does not disturb C-43 dual-naming or protocol-failure close |
| C-46 | PASS | Standalone bold block at both S-3 and A-1 |
| C-47 | PASS | Dedicated row at both sites; label "(P-0 anti-bypass declaration)" is a multi-line cell, still a first-class row |

**New aspirational property seeded**: Bidirectional navigation closure at P-0 — P-0 now knows its use sites (S-3, A-1), completing the P-0 → use-site forward arc to pair with the use-site → P-0 back-arc already present.

**Score**: 39/39 × 10 = **10.0**

---

### V-03 — Phrasing Register (Content cell attribution "Per P-0 anti-bypass declaration: ")

**Change**: Echo row content cell at S-3 and A-1 opens with "Per P-0 anti-bypass declaration: " prefix. P-0 unchanged; echo row label retains "(P-0 anti-bypass declaration)".

| Criterion range | Verdict | Evidence |
|---|---|---|
| C-01–C-05 (essential) | PASS | Inherited |
| C-06–C-08 (recommended) | PASS | Inherited |
| C-09–C-43 (aspirational) | PASS | Inherited; prefix appended before dual-named bypass text — both action-based and protocol-based descriptions remain present for C-43/C-45 pass |
| C-44 | PASS | Single-task annotation present |
| C-45 | PASS | Use-site echo content retains full dual-naming; attribution prefix is additive |
| C-46 | PASS | Standalone bold imperative block at both sites |
| C-47 | PASS | Dedicated row form at both sites |

**New aspirational property seeded**: Content-cell provenance attribution — an executor scanning the content cell alone (not reading the label) now encounters the source reference "Per P-0 anti-bypass declaration:" at the point of rule application, making the echo's identity as a protocol echo rather than a locally-defined constraint observable without requiring label + content to be read as a unit.

**Score**: 39/39 × 10 = **10.0**

---

### V-04 — Output Format + Lifecycle Emphasis (ABD label + P-0 forward pointer; no content attribution)

**Change**: Combines V-01 label at P-0 + V-02 forward pointer. Echo row labels become "(P-0, ABD)". No content cell attribution.

| Criterion range | Verdict | Evidence |
|---|---|---|
| C-01–C-05 (essential) | PASS | Inherited |
| C-06–C-08 (recommended) | PASS | Inherited |
| C-09–C-43 (aspirational) | PASS | Inherited; P-0 label prepended + forward pointer appended; dual-named text unchanged |
| C-44–C-45 | PASS | Single-task annotation present; echo content dual-naming intact |
| C-46 | PASS | Standalone bold block at both sites |
| C-47 | PASS | Dedicated row at both sites |

**New aspirational properties seeded**: Combines V-01 and V-02 properties — named structural anchor at P-0 (label-matchable from use sites) plus forward navigation (P-0 → use sites). Together they form a navigable named anchor: locatable from use sites by name match, discoverable from P-0 by forward enumeration. Neither alone guarantees both; V-04 establishes the complete structural address pair at the definition site.

**Score**: 39/39 × 10 = **10.0**

---

### V-05 — Full Convergence (ABD label + forward pointer + "Per P-0, ABD:" content attribution)

**Change**: All three axes combined. P-0: "Anti-bypass declaration (ABD): An executor who… Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row." Echo row labels: "(P-0, ABD)". Echo content cells: "Per P-0, ABD: processing this row without reading the Step and Row type cells, or without performing Phase 2, is a protocol failure."

| Criterion range | Verdict | Evidence |
|---|---|---|
| C-01–C-05 (essential) | PASS | Inherited |
| C-06–C-08 (recommended) | PASS | Inherited |
| C-09–C-43 (aspirational) | PASS | Inherited; all definition-site and use-site text changes are additive |
| C-44 | PASS | Standalone bold imperative annotation at both sites |
| C-45 | PASS | Echo content: "Per P-0, ABD: processing this row without reading the Step and Row type cells, or without performing Phase 2, is a protocol failure." — action-based bypass ("without reading the Step and Row type cells") + protocol-based bypass ("without performing Phase 2") + protocol-failure close ("is a protocol failure") all present |
| C-46 | PASS | "**Executor: fill the Match field only. All other fields are pre-filled.**" at both S-3 and A-1 as standalone block above template |
| C-47 | PASS | Dedicated "Anti-bypass echo" row immediately after CONFIRMATION REQUIRED at both sites; CONFIRMATION row stays clean; "(P-0, ABD)" label clearly separates the row |

**Excellence signals from V-05**:

1. **Labeled named anchor at the definition site** — "Anti-bypass declaration (ABD):" creates an element addressable by name. Use-site label "(P-0, ABD)" names the specific element, not the step generally; a reader arriving at P-0 confirms the match by finding the heading, making the reference verifiable on arrival rather than inferred from scanning prose.

2. **Bidirectional navigation closure at the definition site** — P-0 now knows its application points (S-3, A-1). The forward pointer closes the last open arc: the complete navigation chain is P-0 → {S-3, A-1} (forward by explicit enumeration) and S-3/A-1 → P-0 (backward by "(P-0, ABD)" label reference). A reader anywhere in the chain can reach any other node in one navigation step.

3. **Content-cell source attribution at every use site** — "Per P-0, ABD:" in the rule body makes provenance observable at the exact point of application, independent of which cell is read first. An executor auditing all protocol-failure conditions by scanning content cells only sees the source without needing to correlate the label column.

4. **Complete provenance chain for the anti-bypass layer** — Together: labeled anchor (definition site) + bidirectional pointers (both directions navigable from both ends) + content attribution (source visible in rule body). Every point where the anti-bypass constraint appears carries its complete derivation chain, seeding the v18 target of bracket token "[P-0:ABD]" entered in the P-0 resolution table.

**Score**: 39/39 × 10 = **10.0**

---

### Composite scores and ranking

| Variation | Score | New properties added | Rank |
|---|---|---|---|
| V-05 | 10.0 | Label + forward pointer + content attribution (all three) | 1 |
| V-04 | 10.0 | Label + forward pointer (definition-site pair) | 2 |
| V-01 | 10.0 | Label only | 3 |
| V-02 | 10.0 | Forward pointer only | 4 |
| V-03 | 10.0 | Content attribution only | 5 |

All five pass all 39 criteria. Ranking is by completeness of the provenance chain seeded, not by score differential.

---

### Excellence signals summary

The top-scoring variation (V-05) demonstrates that the three R18 axes are orthogonal and jointly load-bearing: each closes a distinct gap in the anti-bypass provenance chain that the others leave open. V-01 makes the back-reference verifiable (label match on arrival). V-02 makes the definition site self-aware of its application points (forward arc). V-03 makes the source observable at the rule body level (content attribution). V-04 confirms the two definition-site properties add independent value by combining them without V-03. V-05 establishes that all three together create a complete, redundantly-navigable provenance chain where the constraint's source is identifiable from every structural vantage point: the label cell, the content cell, the definition site, and both navigation directions.

The clear v18 target: bracket token "[P-0:ABD]" entered in the P-0 resolution table, extending the O(1) lookup protocol that covers [S-3:CS] and [A-1:FC] to also cover the protocol definition layer.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["labeled-named-anchor-at-P0-enables-verifiable-back-reference", "P0-forward-pointer-to-use-sites-completes-bidirectional-navigation", "content-cell-source-attribution-makes-provenance-observable-independent-of-label"]}
```
