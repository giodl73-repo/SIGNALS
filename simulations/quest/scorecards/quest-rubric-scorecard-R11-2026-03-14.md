each novel Contract element its own named row. V-04's merged row covers both elements with one pass/fail signal — the more salient element (role-definition phrase) can satisfy the row while the less salient element (DR sub-section labeling) silently drops.

**2. Phrase anchored at both structural layers (C-25/C-26/C-33 all PASS vs V-02's joint failure)**
V-01 places "or equivalent block" in the role definition text AND requires it there via Contract item 4. V-02 removes the role-definition anchor, producing C-25 PARTIAL + C-26 FAIL from one root cause — confirming that the output-state layer (Contract) and generation-behavior layer (role definition) are structurally independent propagation targets.

**3. Contract item 5 as C-27 load-bearing mechanism (PASS vs V-03 PARTIAL)**
V-03 retains Phase 3 ordering instruction for DR content but omits Contract item 5. The output DR has required items present but in unlabeled prose. Phase 3 co-location instruction alone is insufficient for labeled sub-section structure — the Contract enforcement is the load-bearing mechanism.

---

## New Patterns Confirmed in R11

**Pattern 1: role-definition-layer phrase is an independent propagation target from Contract output-state layer**
V-01 vs V-02 is the clean single-axis isolation. Contract item 4 in both versions achieves structural equivalence at the output-state layer. V-01 adds the phrase at the role-definition layer; V-02 does not. Result: V-01 scores C-25 PASS + C-26 PASS; V-02 scores C-25 PARTIAL + C-26 FAIL. The two structural layers are non-redundant — satisfying one does not satisfy the other. C-33 is confirmed.

**Pattern 2: AND-gate Contract item for co-presence does not propagate structural-label compliance to DR generation**
V-01 vs V-03 isolation: Contract item 1 (evolution hook AND-gate) satisfies C-32 in both variations. V-01 adds Contract item 5 for DR sub-section labeling; V-03 does not. Result: V-01 scores C-27 PASS; V-03 scores C-27 PARTIAL. The AND-gate contract for co-presence content does not carry the structural-label requirement — a separate Contract item is required. This confirms the v12 candidate `and-gate-contract-does-not-propagate-to-dr-sub-section-labeling`.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["role-definition-layer phrase is structurally independent from Contract output-state equivalence — satisfying Contract structural equivalence without anchoring the exact phrase at the role-definition layer produces joint C-25/C-26 failure from one root cause", "AND-gate Contract item for evolution-hook co-presence does not propagate DR sub-section labeling compliance — labeled sub-section structure requires a dedicated Contract item; Phase 3 ordering instruction alone is insufficient"]}
```
