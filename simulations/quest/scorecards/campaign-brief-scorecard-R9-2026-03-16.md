## campaign-brief / Round 9 — Quest Score

---

### Evaluation Method

R9 is a **stress test** round, not a structural addition round. The rubric is unchanged at v8 (26 criteria, 260 pts). Evaluation context is the R9 stress scenario: high token pressure, many `found` signals, COMPRESSED active, VERDICT as last block processed. Criteria are evaluated for *execution reliability under stress*, not nominal presence.

**Scoring scale:** PASS = 10, PARTIAL = 5, FAIL = 0

**Baseline assumption:** All five variations inherit R8 V-05 structure. C-01–C-23 are structurally intact in all variations — all PASS at 10 pts each (230 pts base). Differentiation is on C-24, C-25, C-26.

---

### C-24 — Timestamp isolation dual-location mandate

**All variations:** PASS (10 pts each)

Every variation has both required locations:
1. Inline annotation on the `found` date field: `<- timestamp is structurally separate from blocking entries; this field is NOT subject to COMPRESSED abbreviation...`
2. STATUS execution note: `TIMESTAMP ISOLATION: per-signal dates in the found section are structurally separate from blocking entries. COMPRESSED format applies only to blocking entry verbosity...`

Both locations are identical across V-01–V-05. C-24 is fully satisfied under stress in all five.

---

### C-25 — Zero-signal synthesis mandate as standalone named execution rule

**V-01 — PASS (10 pts)**
Rule is mid-document (between CONFIDENCE and STORY), standalone named, two clauses, plus TOKEN-PRESSURE GUARD: *"This rule does not suspend when `found` is non-empty. It fires unconditionally at any token budget."* The guard explicitly names the conditional-context suppression failure mode and declares it a "structural firewall." Under R9 stress (large `found`), the model cannot infer dormancy — the guard prevents it.

**V-02 — PARTIAL (5 pts)**
Rule is mid-document, standalone named, two clauses — R8 V-05 baseline form, no guard. Under R9 stress, the model processes this rule in a context where `found` is large and non-empty. The rule's conditional trigger ("when `found` contains zero signals") is the dominant framing; with no unconditional-firing declaration, the model may treat the rule as dormant. The structural requirement is met but the stress-survival architecture is absent.

**V-03 — PASS (10 pts)**
Rule is elevated to **preamble position** (before "Run the phases in order"), labeled as "global execution constraint — applies to every run," two clauses, plus closing note: *"This rule is stated here, before phase execution begins, so that it is processed as a global constraint rather than as a block-local note."* Preamble position means the model reads this rule before forming any synthesis context — no block-execution-mode suppression possible.

**V-04 — PASS (10 pts)**
Mid-document + TOKEN-PRESSURE GUARD (same as V-01). No preamble placement, but the unconditional-firing declaration is the active guard mechanism. Same reliability as V-01 for C-25.

**V-05 — PASS (10 pts)**
Preamble position + TOKEN-PRESSURE GUARD (V-03 axis + V-01 axis). Strongest form: processed as global constraint before execution begins AND declares unconditional firing. Belt-and-suspenders — if preamble position is compressed, the guard clause remains; if the guard clause is skipped, the preamble position has already set the constraint.

---

### C-26 — Action-posture sub-labels on bounded/unbounded inertia field

**V-01 — PARTIAL (5 pts)**
`action:` sub-labels present in VERDICT format spec. Execution note: *"Declare bounded or unbounded with the action sub-label."* No VERDICT COMPRESSION GUARD. Under R9 stress — COMPRESSED active, VERDICT is last block with depleted token budget — the model preserves primary content (`bounded:`/`unbounded:` classification, satisfying C-23) but may elide the `action:` sub-label as optional format extension. Structural presence confirmed; compression-survival architecture absent.

**V-02 — PASS (10 pts)**
`action:` sub-labels + VERDICT COMPRESSION GUARD: *"The `action:` sub-label on `inertia_cost` is required regardless of COMPRESSED format state and regardless of token pressure. VERDICT is never abbreviated. The action sub-label is not optional format — it is the field that makes VERDICT self-contained."* Explicitly names the COMPRESSED x last-block failure mode. The guard elevates the sub-label from "format extension" to "mandatory field" — the model cannot elide it without violating a named invariant.

**V-03 — PARTIAL (5 pts)**
`action:` sub-labels present. No VERDICT COMPRESSION GUARD. Same vulnerability as V-01 — C-26 reliable under nominal conditions, at risk under COMPRESSED + last-block token depletion. Execution note is R8 V-05 baseline.

**V-04 — PASS (10 pts)**
VERDICT COMPRESSION GUARD present (same as V-02). C-26 reliable under R9 stress.

**V-05 — PASS (10 pts)**
VERDICT COMPRESSION GUARD present (same as V-02). C-26 reliable under R9 stress.

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-20 (each 10) | 200 | 200 | 200 | 200 | 200 |
| C-21 | 10 | 10 | 10 | 10 | 10 |
| C-22 | 10 | 10 | 10 | 10 | 10 |
| C-23 | 10 | 10 | 10 | 10 | 10 |
| **C-24** | **10** | **10** | **10** | **10** | **10** |
| **C-25** | **10** | **5** | **10** | **10** | **10** |
| **C-26** | **5** | **10** | **5** | **10** | **10** |
| **TOTAL** | **255** | **255** | **255** | **260** | **260** |

---

### Ranking

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| 1 (tied) | **V-05** | 260 | Preamble + token-pressure guard + VERDICT guard |
| 1 (tied) | **V-04** | 260 | Token-pressure guard + VERDICT guard (mid-doc) |
| 3 (tied) | V-01 | 255 | C-25 hardened, C-26 unguarded |
| 3 (tied) | V-02 | 255 | C-26 hardened, C-25 unguarded |
| 3 (tied) | V-03 | 255 | C-25 preamble, C-26 unguarded |

**Single-axis results:** Every single-axis variation (V-01, V-02, V-03) scores 255 — each guards one axis and leaves the other exposed. No single mechanism is sufficient; both guards are required.

**V-04 vs V-05 at ceiling:** Both achieve 260. V-05's preamble placement adds belt-and-suspenders on C-25 but produces no additional rubric credit (C-25 was already PASS in V-04 via token-pressure guard). The preamble mechanism in V-05 may matter in scenarios where token pressure is extreme enough to suppress mid-document rules before the guard clause is processed — but this is not distinguishable within the current rubric.

---

### Excellence Signals (from V-05)

**Signal 1 — Dual mechanism (positional + declarative) for edge-case rules**
V-05 applies two structurally independent hardening mechanisms to the same rule: (a) preamble position, which ensures the rule is processed as a global execution constraint before any block-execution context forms; (b) TOKEN-PRESSURE GUARD clause, which names the specific failure mode (conditional dormancy when `found` is large) and declares unconditional firing. The two mechanisms have different failure modes — position can be overridden by instruction budget effects; the declarative guard can be skipped if not reached. Applied together, if one mechanism fails, the other compensates. This is a generalizable pattern for any edge-case rule that fires on boundary conditions not triggered in the majority of runs.

**Signal 2 — Named block-level invariant in execution note**
V-02/V-04/V-05's VERDICT COMPRESSION GUARD introduces a meta-pattern: rather than specifying what a field should contain (the existing approach), it declares the block as *structurally non-abbreviatable* and names the specific failure mode it guards against. "VERDICT is never abbreviated" is a block-level invariant. "The action sub-label is not optional format — it is the field that makes VERDICT self-contained" elevates the sub-label's semantic role. This approach — naming the invariant, naming the failure mode, naming the semantic role — is more reliable than passive format spec because it forecloses the model's rationale for elision rather than just stating the desired output.

---

```json
{"top_score": 260, "all_essential_pass": true, "new_patterns": ["Dual mechanism (preamble position + unconditional-firing declaration) for edge-case synthesis rules creates belt-and-suspenders compression survival — each mechanism has independent failure modes, so their combination survives scenarios where either alone would not", "Named block-level invariant guard in execution note — declaring a block structurally non-abbreviatable and naming the COMPRESSED x last-block failure mode — is more reliable than passive format spec because it forecloses the model's rationale for sub-label elision rather than just specifying the desired output"]}
```
