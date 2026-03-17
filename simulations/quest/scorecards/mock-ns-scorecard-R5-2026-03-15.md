## mock-ns — Round 5 Scoring

**Rubric**: v5 (C-01–C-20) | **Variants**: V-01 through V-05

---

## Criterion-by-Criterion Evaluation

### Essential (5 criteria, 60 pts)

All five variants carry the full header structure, category registry lookup, skill-specific body instruction, Flag field referencing the computed variable, and correct path convention.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Header block complete | PASS | PASS | PASS | PASS | PASS |
| C-02 Category assignment correct | PASS | PASS | PASS | PASS | PASS |
| C-03 Body follows golden rubric structure | PASS | PASS | PASS | PASS | PASS |
| C-04 Flag present and matches category | PASS | PASS | PASS | PASS | PASS |
| C-05 Path convention correct | PASS | PASS | PASS | PASS | PASS |
| **Essential score** | **5/5** | **5/5** | **5/5** | **5/5** | **5/5** |

---

### Recommended (3 criteria, 30 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Representative skill selection | PASS — exclusion note in table column | PASS — exclusion constraint in column | PASS — exclusion language in inline note (C-12 evidence, strong) | PASS — Notes column with exclusion | PASS — exclusion constraint column |
| C-07 Fidelity warning present with full qualifier | PASS — all three variants; HIGH-STRUCTURE includes "REAL-REQUIRED at Tier 2+" | PASS | PASS | PASS — table format includes all three types with qualifier | PASS |
| C-08 Next-step line at end | PASS — A-5 present | PASS | PASS | PASS | PASS |
| **Recommended score** | **3/3** | **3/3** | **3/3** | **3/3** | **3/3** |

---

### Aspirational (12 criteria, 10 pts)

**C-09 — Tier-conditional flag refinement**
All variants: `FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"` case is explicitly enumerated in S-3. PASS all.

**C-10 — TOPICS.md consultation emit**
All variants: dedicated `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` line. PASS all.

**C-11 — FLAG computed as named step before header**
All variants: S-3 is a discrete named step for FLAG, sequenced before A-1. FLAG referenced by name in header. PASS all.

**C-12 — topic-status exclusion documented with default table**
- V-01: "Do NOT use topic-status (excluded — meta-structural)" in Exclusion note column. PASS
- V-02: "topic-status is excluded (meta-structural). Do NOT use topic-status as a mock-ns default at any tier." in Exclusion constraint column. PASS
- V-03: "(topic-status is excluded as meta-structural; never use it as the mock-ns default, even if it appears first alphabetically)" as parenthetical in list. Language is strong; satisfies C-12 threshold. PASS
- V-04: "Do NOT use topic-status (meta-structural)" in Notes column. PASS
- V-05: "topic-status is EXCLUDED — meta-structural, never default" in Exclusion constraint column. PASS

**C-13 — Fidelity warning as lead section before mock body**
All variants instruct the fidelity warning as the first section before mock content, separated by `---` delimiters. PASS all.

**C-14 — FLAG immutability at BOTH compute site AND consumption site**
All variants carry prohibition language at S-3 (compute) and A-1 (consumption). PASS all.

**C-15 — Dedicated structural column for exclusion constraints**

| Variant | Analysis | Verdict |
|---------|----------|---------|
| V-01 | 3-column table: Namespace \| Default skill \| **Exclusion note**. Labeled column carries constraint. | PASS |
| V-02 | 3-column table: Namespace \| Default skill \| **Exclusion constraint**. Labeled column, multi-line entry. | PASS |
| V-03 | List format with parenthetical inline annotation — equivalent to bracket annotation pattern the rubric calls out. No table column. | FAIL |
| V-04 | 3-column table: Namespace \| Default \| **Notes**. Labeled column carries exclusion constraint. | PASS |
| V-05 | 3-column table: Namespace \| Default skill \| **Exclusion constraint**. Labeled column with EXCLUDED. | PASS |

**C-16 — FLAG prohibition is run-scoped, not step-sequential**

| Variant | Key language | Verdict |
|---------|-------------|---------|
| V-01 | "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context, including paths that do not pass through prior steps in normal order." Run-scoped. | PASS |
| V-02 | "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, or any regeneration sequence. This prohibition covers every execution path, including paths that bypass the normal step order." Run-scoped. | PASS |
| V-03 | "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, or any regeneration sequence. Every execution path — including paths that enter header assembly without passing through S-3 in normal order — is covered." Run-scoped. | PASS |
| V-04 | "Do not re-evaluate or modify it **in any subsequent step** of this run." — exact pattern the rubric marks as step-sequential. Fails C-16 per rubric definition. | **FAIL** |
| V-05 | "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context, including paths that do not pass through prior steps in normal order. Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." | PASS |

> **Note**: V-04 was predicted to carry C-16 ("run-scoped declaration"), but the actual S-3 text uses step-sequential language. Scored as written.

**C-17 — FLAG prohibition is FIRST stated rule at consumption site**

V-04 passes C-14, so C-17 is evaluated independently of C-16.

- V-01: "The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it." — first instruction. PASS
- V-02: "The first rule of this step: copy FLAG from S-3 verbatim. Do not rederive it." — first instruction. PASS
- V-03: "RULE 1 — Do not compute a new FLAG value here." — explicitly numbered as Rule 1, first instruction. PASS
- V-04: "The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it." — first instruction. PASS
- V-05: "The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it." — first instruction. PASS

**C-18 — Named path class enumeration at compute site** (auto-fails if C-16 fails)

| Variant | Named classes | Verdict |
|---------|--------------|---------|
| V-01 | conditional branches, fallback paths, regeneration sequences, "any other execution context" (catch-all), "paths that do not pass through prior steps in normal order" (bypass clarifier) | PASS — exceeds minimum |
| V-02 | conditional branches, fallback paths, regeneration sequences, bypass clarifier | PASS |
| V-03 | conditional branches, fallback paths, regeneration sequences, bypass clarifier | PASS |
| V-04 | None — step-sequential language only; C-16 fails, C-18 auto-fails | **FAIL** |
| V-05 | conditional branches, fallback paths, regeneration sequences, "any other execution context," bypass clarifier, + "No path is exempt" affirmative closure | PASS — strongest enumeration |

**C-19 — Anti-displacement closure at consumption site** (requires C-17 pass)

| Variant | Analysis | Verdict |
|---------|----------|---------|
| V-01 | "This rule is first — it applies before any field is listed, before any category lookup, before any formatting instruction in this step. No instruction in A-1 precedes this rule." Names: field-listing, category lookup, formatting. Declarative closure present. | PASS |
| V-02 | "The first rule of this step: copy FLAG from S-3 verbatim. Do not rederive it." No competing types named. No declarative closure. | **FAIL** |
| V-03 | "RULE 1 — Do not compute a new FLAG value here. Copy FLAG from S-3 exactly as emitted." Consequence follows immediately, but no competing instruction types named, no declarative closure. | **FAIL** |
| V-04 | "The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it." No competing types named. No closure. | **FAIL** |
| V-05 | "This rule is first — it applies before any field is listed, before any category lookup, before any formatting instruction in this step. No instruction in A-1 precedes this rule." Identical pattern to V-01. | PASS |

**C-20 — Failure-consequence framing at consumption site** (requires C-17 pass)

| Variant | Analysis | Verdict |
|---------|----------|---------|
| V-01 | No consequence statement — variant design explicitly omits C-20. | **FAIL** |
| V-02 | No consequence statement. | **FAIL** |
| V-03 | "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier. The failure cannot be caught by automated review because the header category and flag fields are not cross-checked by any downstream process other than mock-review, which may not run before the artifact is consumed." — names failure mechanism (category mismatch) + multiple danger dimensions. | PASS |
| V-04 | No consequence statement. | **FAIL** |
| V-05 | "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier. The artifact will carry an incorrect Flag field, downstream mock-review will flag the wrong namespaces as REAL-REQUIRED, and the corruption is undetectable without manual header inspection." — names failure mechanism + three downstream effects. Strongest consequence statement in this round. | PASS |

---

## Full Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | **F** | P | P |
| C-16 | P | P | P | **F** | P |
| C-17 | P | P | P | P | P |
| C-18 | P | P | P | **F** | P |
| C-19 | P | **F** | **F** | **F** | P |
| C-20 | **F** | **F** | P | **F** | P |
| **Pass count** | **11/12** | **10/12** | **10/12** | **8/12** | **12/12** |

---

## Composite Scores

```
Formula: (essential/5 * 60) + (recommended/3 * 30) + (aspirational/12 * 10)
```

| Variant | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|---------|---------------|-----------------|------------------|-----------|
| V-01 | 60.00 | 30.00 | 11/12 × 10 = **9.17** | **99.17** |
| V-02 | 60.00 | 30.00 | 10/12 × 10 = **8.33** | **98.33** |
| V-03 | 60.00 | 30.00 | 10/12 × 10 = **8.33** | **98.33** |
| V-04 | 60.00 | 30.00 | 8/12 × 10 = **6.67** | **96.67** |
| V-05 | 60.00 | 30.00 | 12/12 × 10 = **10.00** | **100.00** |

**Rank**: V-05 (100) > V-01 (99.17) > V-02 = V-03 (98.33) > V-04 (96.67)

---

## Prediction vs. Actual

| Variant | Predicted | Actual | Delta | Note |
|---------|-----------|--------|-------|------|
| V-01 | ~98.3 | 99.17 | +0.87 | C-19 fully passes; no partial needed |
| V-02 | ~97.5 | 98.33 | +0.83 | Predicted formula was pre-v5 |
| V-03 | ~97.5 | 98.33 | +0.83 | C-15 fail offsets C-20 gain |
| V-04 | ~97.5 | 96.67 | **-0.83** | Actual S-3 text is step-sequential — fails C-16 |
| V-05 | 100 | 100.00 | 0.00 | |

V-04 is the anomaly: the variant description says it carries C-16 ("run-scoped declaration"), but the written S-3 closure uses "in any subsequent step of this run" — exactly the step-sequential pattern the rubric disqualifies. The hypothesis is untestable as written because C-16 was never achieved.

---

## Discriminant Analysis

**V-01 vs V-05 (isolates C-20)**
V-01 scores 99.17; V-05 scores 100.00. Delta: 0.83 points. C-20 (consequence framing) adds independent value even after C-19 (anti-displacement closure) is already present. The consequence statement converts a prohibition into a self-contained argument: the executor knows not just what to do but why the violation is dangerous.

**V-02 vs V-01 (isolates C-19)**
V-02 scores 98.33; V-01 scores 99.17. Delta: 0.83 points. Anti-displacement closure (C-19) adds independent value over path class enumeration (C-18) alone. The compute-site enumeration closes the re-entry gap; the consumption-site closure anchors the instruction against the specific competitors most likely to displace it.

**V-03 vs V-01 (isolates C-19 vs C-20 as sole addition to C-18 base)**
Both score 98.33 — identical composites. The two variants trade C-15 (V-03 loses the table column) for C-20 (V-03 gains consequence framing). When adding only one criterion to C-18: C-19 (V-01) and C-20 (V-03) have equal weight in the formula, but V-03's C-15 failure reveals a structural regression introduced by switching from a table to a list for the default skill selection.

**V-04 baseline**
Scores 96.67, not the predicted ~97.5, because the step-sequential language in S-3 fails C-16 (which auto-fails C-18). The R3 high-water mark is lower than estimated once the rubric's strict C-16 definition is applied.

---

## Excellence Signals (V-05)

Three new patterns in V-05 not captured by the rubric:

**1. CATEGORY immutability declaration**
After S-2 assigns CATEGORY, V-05 adds: "CATEGORY is now assigned. Do not modify it." This extends the immutability pattern from FLAG to CATEGORY. If CATEGORY drifts between S-2 and the header assembly, FLAG (derived from CATEGORY) would be correct but the `Category:` field would be wrong — a distinct corruption vector. No other variant protects CATEGORY with explicit immutability language.

**2. Consequence cascade specificity**
V-05's C-20 statement traces the failure through multiple downstream stages: "The artifact will carry an incorrect Flag field, downstream mock-review will flag the wrong namespaces as REAL-REQUIRED, and the corruption is undetectable without manual header inspection." V-03 names the immediate failure (category mismatch); V-05 names the full chain (incorrect field → wrong downstream flags → undetectable). Cascade-specific consequence statements are harder to deprioritize under pressure than single-failure statements.

**3. "No path is exempt" affirmative closure after enumeration**
After enumerating excluded path classes, V-05 adds: "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." The enumeration (C-18) says what is prohibited; the affirmative closure says what is guaranteed. This positive/negative pairing eliminates the gap where an executor might ask "so what value does A-1 actually use?" — the answer is stated explicitly in the same sentence block as the prohibition.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["CATEGORY immutability declaration at compute site — extend the immutability pattern from FLAG to CATEGORY with explicit 'Do not modify it' language after CATEGORY is assigned, preventing a distinct corruption vector where the Category field and the Flag value diverge", "Consequence cascade specificity — trace the failure through multiple downstream stages (incorrect field → wrong downstream flags → undetectable without manual inspection) rather than naming only the immediate failure mechanism; cascade chains are harder to deprioritize under execution pressure", "Affirmative containment closure after path class enumeration — follow the 'MUST NOT be recomputed in...' prohibition with a positive declarative: 'Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt.' The positive/negative pairing eliminates the residual question of what value A-1 uses"]}
```
