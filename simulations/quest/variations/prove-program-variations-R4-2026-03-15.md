Written to `simulations/quest/golden/prove-program-variate-R4-2026-03-15.md`.

---

## prove-program — R4 Variations Summary

**What changed in v4**: C-17 (verbatim feed-forward quotation), C-18 (inter-phase GATE enforcement), C-19 (per-criterion FAIL conditions inline) — 15 pts new, pool 130→145.

### Five variations

| # | Axis | Primary target | Expected ceiling |
|---|------|---------------|-----------------|
| V-01 | Output format | C-17 — blockquote `>` format in every Input section + FAIL for paraphrase | ~143/145 |
| V-02 | Lifecycle emphasis | C-18 — GATE-α through GATE-ζ at every phase boundary with PASS/STOP per gate | ~128/145 |
| V-03 | Phrasing register | C-19 — inline FAIL condition after every enforced criterion, fixes R3 V-03's C-11 gap | ~125/145 |
| V-04 | C-17 + C-18 combined | Verbatim blockquote + named gate tokens together | ~143/145 |
| V-05 | All three over R3 V-05 | Full role sequence + verbatim + gates + FAIL conditions | ~145/145 |

### Key design decisions

**V-01** over V-02/V-03 on C-18 and C-19: V-01 incidentally satisfies both new criteria alongside its primary C-17 axis — GATE-A through GATE-D provide the inter-phase gates, and the FAIL conditions for the verbatim requirement and Phase 3C/3D are >=3 precise inline conditions. It projects as the strongest single-axis variation.

**V-03 trades C-18 for C-19**: The numbered-sections structure has no named GATE tokens, so C-18 FAIL is expected — but every criterion has a precise `FAIL: [specific failure mode]` embedded inline, which is what separates it from V-01/V-04 where FAIL conditions are present but secondary.

**V-05 closes all gaps**: EXPERIMENT N COMPLETE markers (fixing C-12 PARTIAL seen in V-01–V-04) + verbatim blockquotes (C-17) + six GATE tokens beyond GATE-0 (C-18) + >=3 FAIL conditions per role (C-19). The only reachable 145/145 candidate.
