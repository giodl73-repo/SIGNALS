**R12 variates written** to `simulations/quest/golden/campaign-evidence-variate-R12-2026-03-17.md`.

---

## Summary

Five complete variates for `campaign-evidence` Round 12, incorporating C-34 and C-35.

**Key structural change across all variates:** PROVENANCE RULE is promoted to a 5th peer governance rule, shifting the coverage map from 4x5=20 to 5x5=**25 invocation artifacts**. The checksum and audit table update automatically because count is derived from the map, satisfying C-29 (extensible without static updates).

---

### Variation axes

| Variate | Single/Combined | Axis | Hypothesis |
|---------|----------------|------|-----------|
| **V-01** | Single | Output format | Provenance tags as scannable annotation blocks -- C-34 compliance is a visual scan, not prose interpretation |
| **V-02** | Single | Lifecycle emphasis | Delivery gate (C-35) positioned first in preamble -- executor encounters enforcement before rules |
| **V-03** | Single | Phrasing register | Full interrogative-imperative throughout -- every invocation compels a binary decision, not a stamp |
| **V-04** | Combined | Provenance + delivery gate | C-34 and C-35 declared as interlocked -- gate cannot pass until structured blocks are present; blocks are what make the gate checkable |
| **V-05** | Combined | Role sequence + provenance in handoffs | Provenance obligation declared at the moment of artifact transfer -- the handoff declaration names the authorized `[source: ...]` values the receiving role may use |

### C-34 implementation pattern (scope-restricted stages = S3, S4, S5):
```
[source: Stage N -- Artifact Name]
```
Each claim must carry this block. Out-of-scope artifact name = visible charter violation.

### C-35 delivery gate language (consistent across all variates):
> "This brief SHALL NOT be closed or delivered until invocation artifact count = 25. A count != 25 is a delivery blocker."
