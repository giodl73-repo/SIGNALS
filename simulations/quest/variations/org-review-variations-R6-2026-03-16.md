Written to `simulations/quest/variations/org-review-variations-R18-2026-03-16.md`.

---

## org-review -- Round 18 (v11 rubric Round 6)

### Round summary

R17 (Round 5) achieved a 225/225 structural candidate but had three identified failure modes that prevent mechanically verifiable C-33/C-34/C-35 pass. Round 18 targets each failure mode with a single structural addition.

---

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format | DOMAIN-ROLE COVERAGE MATRIX gains `MAX-APPLICABILITY` and `GAP-STATUS` computed columns. Domain gap detection becomes a cell read, not a row scan. ADVISORY-GAP items derive from `GAP-STATUS` column directly -- no prose inference required. |
| **V-02** | Phrasing register | BRACKET OPENING gains a `VERDICT TALLY TABLE` (count FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD from the dimension table VERDICT column) and an immutable `TALLY-TO-VERDICT LOOKUP TABLE`. `g_null(initial)` = lookup cell for dominant category. No formula interpretation; a pure table lookup. |
| **V-03** | Role sequence | §17a APPLICABILITY CERTIFICATION BLOCK is promoted to `APPLICABILITY CERTIFICATION GATE` with a `CERT STATUS: [CERT-PASS / CERT-FAIL]` field per entry and a `CERTIFICATION GATE VERDICT: [ALL-PASS / HAS-FAIL]` aggregate. Section order contract enforces: `HAS-FAIL = HALT`. Reviewer execution blocked until `ALL-PASS` is confirmed. |
| **V-04** | V-01 + V-02 | Computed gap columns + tally lookup. C-34 and C-35 target simultaneously. |
| **V-05** | V-01 + V-02 + V-03 | Full integration. All three criteria mechanically verifiable. 225/225 candidate. |

---

### Key structural changes vs R17 V-05

**V-01** adds to §17b contract: `MAX-APPLICABILITY = highest tier across row`, `GAP-STATUS = ADVISORY-GAP if MAX-APPLICABILITY != HIGH`. The Advisory items section in the register explicitly sources from the `GAP-STATUS` column.

**V-02** adds §9a contract: `VERDICT TALLY TABLE` + `TALLY-TO-VERDICT LOOKUP TABLE` (7-row lookup covering all dominant + tie cases). `GOpen` must equal the lookup result. §7 section order notes BRACKET OPENING "includes VERDICT TALLY + LOOKUP per §9a".

**V-03** adds `CERT STATUS` field to each §17a certification entry. `CERT-PASS` requires BOTH: (1) specific §1 domain label named, and (2) specific lens.verify entry quoted (not a generic capability claim). `CERTIFICATION GATE VERDICT` aggregates. §7 enforcement clause: `HAS-FAIL = HALT`.

**V-05** combines all three. The contract block has three pre-execution conditions in the header: §1 COMPLETE, CERTIFICATION GATE VERDICT = ALL-PASS, and DOMAIN-ROLE COVERAGE MATRIX COMPLETE.
