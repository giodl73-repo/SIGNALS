## Scoring — topic-plan Variations Round 16

### Evidence extraction

**Structural sites under test** (three locations, one per new criterion):

| Site | Location | What changes across V-01…V-05 |
|------|----------|-------------------------------|
| §9 mutual necessity assertion | PROPOSAL BIAS AUDIT guard body | directional ("LEVEL 1 does not protect") vs co-requirement only |
| SECTION SCOPE navigation note | SECTION SCOPE DECLARATION | complete formal title citation vs enumeration-position only ("item 2") |
| CONTRACT B value spec | CONTRACT B block | exact literal `'Bias blocked by guard'` vs generic "value indicating both guard levels were applied" |

---

### C-37 Evidence per Variation

**V-01**: "LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1 satisfied) does not prevent motivated reasoning at the proposal decision surface (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied independently." → **FULL (2)** — explicit formulation co-located in guard body.

**V-02**: "Both LEVEL 1 and LEVEL 2 guards are required for complete bias protection. A proposal table that passed LEVEL 1 screening is not automatically protected against LEVEL 2 failure." → **PARTIAL (1)** — "not automatically protected against LEVEL 2 failure" identifies the directional gap implicitly; the word "automatically" softens the claim and does not produce the unequivocal "LEVEL 1 does not protect" formulation.

**V-03**: Same mutual necessity text as V-02 → **PARTIAL (1)**.

**V-04**: "LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1 satisfied) does not prevent motivated reasoning at the proposal decision surface (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied independently. Passing LEVEL 1 confers no LEVEL 2 protection." → **FULL (2)** — repeated and reinforced directional claim.

**V-05**: "LEVEL 1 does not protect against LEVEL 2. … The protection hierarchy is not transitive. Both guards must be applied independently. A LEVEL 1 pass confers zero LEVEL 2 protection." → **FULL (2)** — maximal formulation.

---

### C-38 Evidence per Variation

**V-01**: SECTION SCOPE says "the higher-order failure mode — motivated reasoning at the proposal decision surface — is item 2 in the guard." → Enumeration-position only; no formal label title → **FAIL (0)**.

**V-02**: "The more sophisticated failure mode addressed by this guard is **LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE**. A proposal row carrying a non-null Bias guard value has passed both guard levels, including **LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE**." → Complete formal title cited twice; auditor can traverse from scope to guard using label alone → **FULL (2)**.

**V-03**: SECTION SCOPE says "The higher-order failure mode is item 2 in the §9 guard." → Positional only → **FAIL (0)**.

**V-04**: "The more sophisticated failure mode protected against in Phase 5 is **LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE**. Note that **LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE** does not protect against **LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE**; both levels must be checked independently per §9." → Both formal titles cited in full → **FULL (2)**.

**V-05**: Same complete-title citation structure as V-04, augmented with `'Bias blocked by guard'` value reference in scope note → **FULL (2)**.

---

### C-39 Evidence per Variation

**V-01**: CONTRACT B: "Compliant state: column present with a value indicating both guard levels were applied." → Generic; no exact literal string → **FAIL (0)**.

**V-02**: CONTRACT B same as V-01 → **FAIL (0)**.

**V-03**: CONTRACT B: "Value compliance: the compliant column value is exactly `'Bias blocked by guard'`. A column that is present but does not contain this exact literal string is a CONTRACT B value violation. Approximate variants (`'bias blocked'`, `'guard applied'`, `'both levels passed'`) are not compliant; only the exact string `'Bias blocked by guard'` satisfies value compliance." → Exact literal quoted, approximate variants enumerated → **FULL (2)**.

**V-04**: CONTRACT B: "Compliant state: column present with a value indicating both guard levels were applied." → Generic → **FAIL (0)**.

**V-05**: CONTRACT B: "Value compliance: the compliant column value is exactly `'Bias blocked by guard'`. A scorer reading CONTRACT B alone can verify: (a) Column exists: structural compliance test. (b) Column contains `'Bias blocked by guard'`: value compliance test." Plus explicit listing of non-compliant variants → **FULL (2)**.

---

### Essential Criteria (C-01–C-08) — all variations

All five variations share the same phase structure (7 phases with gated entry conditions), INERTIA COMPETITOR concept established at document open ("The default outcome of this skill is NO CHANGE to strategy.md. Every proposal carries the burden of proof"), all §IDs present, Constraint Rules R-0 through R-4, Constraint Scope Index, Phase Authorization Index. **All essential criteria PASS** across all five variations.

---

### Aspirational Criteria C-09–C-36 — all variations

All five variations are built from the same structural foundation that achieved 56/56 on C-09–C-36 in R15. The R16 changes are strictly additive to three specific structural sites (§9 guard body, SECTION SCOPE, CONTRACT B) and do not remove or degrade any previously-satisfied criterion. C-34 (formal LEVEL 1/LEVEL 2 labels) FULL; C-35 (SECTION SCOPE navigation note with enumeration reference) FULL; C-36 (CONTRACT B column-absence violation detection) FULL — all present in all five variations. **C-09–C-36 = 56 points (28 × 2) for all five variations.**

---

### Composite Scores

| Variation | C-09–C-36 | C-37 | C-38 | C-39 | Total | Score |
|-----------|:---------:|:----:|:----:|:----:|:-----:|:-----:|
| V-01 | 56 | 2 | 0 | 0 | 58/62 | **9.35** |
| V-02 | 56 | 1 | 2 | 0 | 59/62 | **9.52** |
| V-03 | 56 | 1 | 0 | 2 | 59/62 | **9.52** |
| V-04 | 56 | 2 | 2 | 0 | 60/62 | **9.68** |
| V-05 | 56 | 2 | 2 | 2 | 62/62 | **10.00** |

**Ranking: V-05 > V-04 > V-02 = V-03 > V-01**

Unexpected finding: V-02 and V-03 outperform V-01 despite V-01 hitting its target criterion cleanly, because V-02/V-03 earn C-37=PARTIAL(1) from their "not automatically protected" language — a partial directional signal unintentionally present in the non-directional base text.

---

### Excellence Signals from V-05

Three patterns present in V-05 that are absent or weaker in V-04:

**Pattern 1 — CONTRACT B structural/value violation taxonomy split.** V-05 CONTRACT B defines two distinct violation categories with separate labels and detection logic: `STRUCTURAL` (column absent) and `VALUE` (column present but value ≠ exact literal). V-04 names only the structural violation. The taxonomy split makes each violation type independently referenceable and detectable from the contract block alone without inspecting phase content.

**Pattern 2 — §9 compliance obligation specifies exact column value.** V-05 §9 compliance line reads "every §6 proposal row must carry `'Bias blocked by guard'` in the Bias guard column" — the obligation inside the guard body itself names the required value string, not just "non-null Bias guard value." This means the guard and the contract are mutually reinforcing: the guard names the obligation, the contract governs compliance. V-04's §9 compliance line says "non-null Bias guard value" — generic, requiring the scorer to consult CONTRACT B to determine what value is correct.

**Pattern 3 — Explicit scorer self-sufficiency claim in CONTRACT B.** V-05 CONTRACT B includes "A scorer reading CONTRACT B alone can verify: (a) Column exists: structural compliance test. (b) Column contains `'Bias blocked by guard'`: value compliance test." This is a testability assertion — the contract explicitly claims it is self-contained for both verification modes. No other variation makes this claim. The claim itself becomes a machine-auditable property: a contract that makes the claim and fails to satisfy it is a detectable inconsistency.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["CONTRACT B structural/value violation taxonomy split: defines STRUCTURAL (column absent) and VALUE (column present but wrong string) as distinct labeled violation categories, each independently detectable from the contract block alone", "Guard-body compliance obligation specifies exact column value string: the §9 compliance line names 'Bias blocked by guard' directly, creating mutual reinforcement between guard obligation and contract governance — guard names the required value, contract governs compliance", "Scorer self-sufficiency assertion in CONTRACT B: explicit claim that a scorer reading CONTRACT B alone can verify both column existence and column value, making the contract's coverage testable as a declared property rather than inferred from content"]}
```
