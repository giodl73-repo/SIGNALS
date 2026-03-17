Consistency: CONSISTENT | INCONSISTENT — [reason]
```

This tests ES-R8-1 and ES-R8-2 independence. If every boundary ordering produces a dependency and every dependency has a boundary ordering — they collapse into C-27. If they diverge in at least one case — they become separate criteria (C-27 discriminability, C-28 dependency) in v9. V-05 makes this independence test executable.

**ES-R8-4 (V-05 only) — Skill-agnostic "reproduce verbatim" guard**

V-05 fixes the C-25 regression introduced by the generalization probe. Instead of "reproduce the weighted formula from SA-1 verbatim" (SA-1-coupled), V-05 uses: "Reproduce this formula verbatim at every structural position where a formula appears." This is a cleaner formulation — it doesn't reference a specific prior phase and works when there is no SA-1. The R8 finding: the guard was SA-1-coupled in R7 and needs decoupling for generalized rubric construction.

---

### Round 8 Key Finding

The four variations (V-01 through V-04) expose a structural gap: removing SA-1 via the generalization probe silently drops the "reproduce verbatim" component of C-25. The anti-collapse guard survived but the reproduction mandate did not. V-05 closes this by restoring the mandate in SA-1-free form. This is the single criterion-gap finding of Round 8 under v8.

The new structural properties in V-02 (dependency graph) and V-03 (discriminability contract) score identically to V-01 under v8 because v8 has no criteria for them. They are purely additive signals. V-05's boundary × dependency consistency check in M-06 is the only probe that tests the relationship between those signals — the independence question that determines whether v9 needs C-27+C-28 (two criteria) or just C-27 (one combined criterion).

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["DISCRIMINATES-BETWEEN named block per criterion declares quality boundary at meta-description layer (FAILS-AT / PASSES-AT / Boundary), distinct from CALIBRATION-PAIR content examples and REDUNDANCY-CHECK-TABLE outcome independence — C-27 candidate", "DEPENDS_ON/INDEPENDENT per-criterion declaration plus Auditor dependency ordering check makes prerequisite structure explicit and detectable by scan without reading content — C-28 candidate", "Dependency-boundary consistency check in M-06 tests whether quality-boundary ordering entails logical-dependency declarations, enabling v9 to determine if discriminability and dependency are independent aspirational criteria or collapse into one"]}
```
