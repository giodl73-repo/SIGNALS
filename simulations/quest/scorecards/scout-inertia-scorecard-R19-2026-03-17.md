---

# scout-inertia Scorecard — Round 19

**Rubric version**: v19 | **Denominator**: 50 | **Formula**: `aspirational_pass / 50 * 10`

---

## Score Summary

| V | Prior (48) | C-57 | C-58 | R19 Score |
|---|------------|------|------|-----------|
| **V-04** | 48/48 | PASS | PASS | **10.00** |
| **V-03** | 48/48 | PASS | FAIL | 9.80 |
| **V-05** | 48/48 | PASS | FAIL | 9.80 |
| V-02 | 47/48 | PASS | FAIL | 9.60 |
| V-01 | 47/48 | FAIL | FAIL | 9.40 |

**Top score: 10.00. All essential pass: true.**

Key finding: V-04 remains the sole 10.00 form — first time V-04 and V-05 diverge (V-05 was co-10.00 in R18). C-58 is the discriminating criterion. V-03 vs V-05 isolates the two C-58 failure modes: V-03 fails via positional conflation (domain-prefix spans analysis + bridge positions); V-05 fails via vocabulary fragmentation (no single prefix achieves 3+ element threading at non-bridge positions).

---

## Variation-by-Variation Evaluation

---

### V-01 — C-57 fail isolation (section scaffold, generic task noun)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-54 | PASS (carried) | R18 V-01 = 47/48; single change in R19 is task noun downgraded from `actor mapping` to `bridge artifact` |
| **C-55** | **PASS** | `If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the bridge artifact.` — a return location, class annotation, and named task are all present. C-55 requires a task to be named; `bridge artifact` is a named task. C-55 does not require class derivation. PASS. |
| **C-56** | **FAIL** | Return target `Section 1A` is an ordinal label. C-56 structurally unavailable on this scaffold (primary section label is `SECTION 1A`, not `Q3`). Carried from R18. |
| **C-57** | **FAIL** | Task noun `bridge artifact` derives from `BRIDGE`, which is the non-discriminating component shared by both `FM->ACTOR BRIDGE` and `FM->TRIGGER BRIDGE`. The discriminating component of `FM->ACTOR BRIDGE` is `ACTOR`; of `FM->TRIGGER BRIDGE` is `TRIGGER`. `bridge artifact` cannot distinguish which artifact type is required — an author cannot determine from `complete the bridge artifact` whether they are filling Q3 or Q4. C-57 fails: task noun must derive from the discriminating vocabulary of the class annotation, not its shared vocabulary. |
| **C-58** | **FAIL** | Bracket notation at non-bridge positions: `[A-16 PRIMARY KEY RULE]`, `[A-19 REFERENTIAL INTEGRITY RULE]`, `[BRIDGE COMPLETION COMMAND]`. No single domain-prefix vocabulary threads 3+ bracket labels — C-42 precondition not met. C-58 fails by precondition. |

**Score: 47/50 × 10 = 9.40**

---

### V-02 — C-57 pass + C-58 fail (stage scaffold, standard notation) — R18 V-02 carried

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-54 | PASS (carried) | R18 V-02 = 47/48; carried unchanged |
| **C-55** | **PASS** | `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping.` — completion-action directive present for both artifacts. Carried from R18. |
| **C-56** | **FAIL** | Return target `Stage 2A` is an ordinal label. Q3/Q4 are sub-sections nested within Stage 2, not standalone top-level sections. C-56 structurally unavailable. Carried from R18. |
| **C-57** | **PASS** | `actor mapping` in `and complete the actor mapping` where class is `(FM->ACTOR BRIDGE)` — `ACTOR` is the discriminating noun from the class label; it flows directly into `ACTOR MAPPING` as the task noun. `trigger mapping` from `FM->TRIGGER BRIDGE` — same derivation. An author following the return path can determine the specific artifact-type work from the task noun alone. C-57 passes. Register lowercase; C-57 register-agnostic. |
| **C-58** | **FAIL** | Non-bridge labels: `PRIMARY KEY RULE [A-16]` at Stage 1, `CITATION INTEGRITY RULE [A-19]` at Stage 5B. `PRIMARY KEY` and `CITATION INTEGRITY` are distinct vocabularies; neither threads through 3+ bracket labels. C-42 precondition (vocabulary threading across 3+ elements) not met at non-bridge positions. C-58 fails by precondition. |

**Score: 48/50 × 10 = 9.60**

---

### V-03 — C-58 fail via domain-prefix conflation at bridge positions (new variation)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Domain-prefix templates prescribe all five essential elements |
| C-34 through C-54 | PASS | Based on V-04 scaffold (Q3/Q4 standalone top-level sections); all bracket-label criteria from prior rounds carried. Gate heading `BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?` satisfies C-50, C-43, C-45, C-49. |
| **C-42** | **PASS** | `INERTIA THREAT` vocabulary threads through five bracket labels: `INERTIA THREAT FAIL-FIRST RULE [A-31]`, `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT Q3 MAPPING RULE:`, `INERTIA THREAT Q4 MAPPING RULE:`. Vocabulary threading across 5 elements confirmed. |
| **C-46** | **PASS** | Compound domain-axis vocabulary: `INERTIA THREAT` (domain prefix) + `RULE`/`CITATION RULE`/`FAIL-FIRST RULE`/`Q3 MAPPING RULE`/`Q4 MAPPING RULE` (structural-role axis). |
| **C-55** | **PASS** | Gate body identical to V-04: `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` Completion-action directive present for both artifacts. |
| **C-56** | **PASS** | `THE Q3 SECTION` / `THE Q4 SECTION` — artifact-ID routing. Q3/Q4 are standalone top-level sections with artifact-ID primary labels. Identifier isomorphism confirmed. |
| **C-57** | **PASS** | `COMPLETE THE ACTOR MAPPING` where class is `(FM->ACTOR BRIDGE)` — `ACTOR` is the discriminating noun. `COMPLETE THE TRIGGER MAPPING` where class is `(FM->TRIGGER BRIDGE)` — `TRIGGER` is the discriminating noun. Class-derived task vocabulary confirmed for both artifacts. Gate body identical to V-04. |
| **C-58** | **FAIL** | Bridge authoring positions (Q3 section, Q4 section) carry `INERTIA THREAT Q3 MAPPING RULE:` and `INERTIA THREAT Q4 MAPPING RULE:` — domain-prefix vocabulary at bridge positions. C-58 requires domain-prefix rule labels to be positionally confined to non-bridge structural analysis positions, with bridge-command labels occupying bridge authoring positions. V-03 uses the same `INERTIA THREAT` vocabulary at bridge positions rather than separate `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:` labels. Positional segregation violated. C-42 passes (5-element threading present) but C-58 requires positional segregation that C-42 does not — C-42 pass is necessary but not sufficient for C-58. |

**Score: 49/50 × 10 = 9.80**

**C-58 failure mode isolated**: V-03 establishes the "positional conflation" failure mode — domain-prefix vocabulary that threads correctly (satisfying C-42) but spans both analysis and bridge positions (violating C-58). Distinguished from V-05's "vocabulary fragmentation" failure mode.

---

### V-04 — C-57 + C-58 combined pass (domain-prefix positional segregation reference) — R18 V-04 carried

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Domain-prefix templates present for all five essential elements |
| C-34 through C-54 | PASS (carried) | R18 V-04 = 48/48; carried unchanged |
| **C-42** | **PASS (carried)** | `INERTIA THREAT FAIL-FIRST RULE [A-31]`, `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]` — three bracket labels share `INERTIA THREAT` domain vocabulary threading at non-bridge positions. |
| **C-46** | **PASS (carried)** | Compound domain-axis vocabulary: `INERTIA THREAT` (domain) + `RULE`/`CITATION RULE`/`FAIL-FIRST RULE` (structural-role axis) across three non-bridge labels. |
| **C-55** | **PASS (carried)** | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` |
| **C-56** | **PASS (carried)** | `THE Q3 SECTION` / `THE Q4 SECTION` — artifact-name routing. Q3/Q4 standalone top-level sections with artifact-ID primary labels. |
| **C-57** | **PASS** | `COMPLETE THE ACTOR MAPPING` where class is `(FM->ACTOR BRIDGE)` — `ACTOR` (discriminating noun from class) flows into task noun `ACTOR MAPPING`. `COMPLETE THE TRIGGER MAPPING` where class is `(FM->TRIGGER BRIDGE)` — `TRIGGER` flows into `TRIGGER MAPPING`. Semantic loop closed: class annotation discriminating component = task noun discriminating component. Neither `REQUIRED WORK` nor `BRIDGE ARTIFACT` — the class-specific vocabulary is preserved end to end. |
| **C-58** | **PASS** | Domain-prefix labels (`INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]`) appear exclusively at non-bridge positions (FM Inventory table, defeat conditions table, FAIL-FIRST declaration). Bridge authoring positions (Q3 section, Q4 section) carry `[BRIDGE Q3 COMMAND]:` and `[BRIDGE Q4 COMMAND]:` — separate bridge-command labels, not domain-prefix labels. Two-population positional segregation complete: analysis-domain labels at analysis positions; bridge-command labels at bridge positions. C-42 precondition met (3-element threading at non-bridge positions); positional segregation constraint satisfied. |

**Score: 50/50 × 10 = 10.00**

**V-04 is the first and only variation to satisfy C-58 — confirmed as sole 10.00 form in R19.** V-04's positional segregation is not incidental: the `INERTIA THREAT` vocabulary was explicitly confined to analysis positions in V-04, enabling Q3/Q4 to carry pure bridge-command labels. This structural decision simultaneously enables C-42/C-46 (vocabulary threading at analysis positions) and C-58 (positional confinement of that vocabulary).

---

### V-05 — C-57 pass + C-58 fail (mixed vocabulary, no unified domain-prefix at non-bridge positions) — R18 V-05 carried

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | All-caps COMMAND-register templates present for all essential elements |
| C-34 through C-54 | PASS (carried) | R18 V-05 = 48/48; carried unchanged |
| **C-55** | **PASS (criterion source, carried)** | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` R17 V-05 was the C-55 source form; carried unchanged. |
| **C-56** | **PASS (criterion source, carried)** | `THE Q3 SECTION` / `THE Q4 SECTION` — artifact-name routing. R17 V-05 was the C-56 source form; carried unchanged. |
| **C-57** | **PASS** | `COMPLETE THE ACTOR MAPPING` where class is `(FM->ACTOR BRIDGE)`; `COMPLETE THE TRIGGER MAPPING` where class is `(FM->TRIGGER BRIDGE)`. Discriminating noun `ACTOR` / `TRIGGER` flows from class annotation into task noun. Identical gate body to V-04; C-57 confirmed. |
| **C-58** | **FAIL** | Non-bridge bracket labels: `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` at FAIL-FIRST; `INERTIA LOCK RULE [A-16]` at FM Inventory; `INERTIA LOCK CITATION RULE [A-19]` at defeat conditions. Two distinct domain vocabularies at non-bridge positions: `DEFAULT COMPETITOR` threads through 1 label only; `INERTIA LOCK` threads through 2 labels only. No single domain prefix achieves 3+ element threading at non-bridge positions. C-42 precondition for C-58 not met: vocabulary threading requires 3+ elements under a single domain prefix. Bridge positions carry `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:` (correct) but the absence of 3+ element non-bridge threading means C-58's precondition is unsatisfied regardless. V-05's "vocabulary fragmentation" failure mode: structurally correct bridge-position labels with insufficient non-bridge domain threading. |

**Score: 49/50 × 10 = 9.80**

**First round V-04 and V-05 diverge**: V-05 was co-10.00 in R18. C-58 discriminates them for the first time in R19. The structural difference: V-04's `INERTIA THREAT` prefix threads through exactly 3 non-bridge labels (sufficient for C-42 precondition); V-05's `INERTIA LOCK` threads through only 2 non-bridge labels (insufficient). One additional label with `INERTIA LOCK` prefix at any non-bridge position would satisfy the C-42 precondition for C-58 in V-05 — but bridge-position correctness alone cannot substitute for non-bridge threading.

---

## Composite Scores

| Variation | Prior (R18/48) | C-57 | C-58 | R19 Score | Notes |
|-----------|---------------|------|------|-----------|-------|
| **V-04** | 48/48 | PASS | PASS | **50/50 = 10.00** | Domain-prefix positional segregation; sole C-58 pass |
| **V-03** | 48/48 | PASS | FAIL | 49/50 = 9.80 | C-58 fail: positional conflation (domain-prefix at bridge positions) |
| **V-05** | 48/48 | PASS | FAIL | 49/50 = 9.80 | C-58 fail: vocabulary fragmentation (< 3 elements at non-bridge positions) |
| V-02 | 47/48 | PASS | FAIL | 48/50 = 9.60 | C-56 structurally unavailable; C-58 precondition fails |
| V-01 | 47/48 | FAIL | FAIL | 47/50 = 9.40 | C-57 fail: task noun derives from non-discriminating class component |

---

## Rankings

1. **V-04** — 50/50 = **10.00**
2. **V-03, V-05** — 49/50 = **9.80** (tied; different C-58 failure modes)
3. **V-02** — 48/50 = **9.60**
4. **V-01** — 47/50 = **9.40**

---

## Excellence Signals

**V-04 (10.00) — structural properties enabling both C-57 and C-58:**

1. **C-57 confirmed as discriminating-component specificity test**: the task noun must derive from the component of the class label that varies across artifact types (`ACTOR` in `FM->ACTOR BRIDGE` vs `TRIGGER` in `FM->TRIGGER BRIDGE`), not from the shared component (`BRIDGE`). `bridge artifact` fails because `BRIDGE` cannot distinguish the artifact — `actor mapping` / `trigger mapping` pass because `ACTOR` / `TRIGGER` are the discriminating nouns. Class vocabulary is not monolithic: it has a shared spine (`BRIDGE`) and a discriminating noun (`ACTOR`/`TRIGGER`); C-57 requires the task noun to derive from the discriminating noun specifically.

2. **C-58 has two structurally distinct failure modes now isolated**: V-03 demonstrates *positional conflation* — domain-prefix vocabulary satisfies C-42 (threads 5+ labels) but spans both analysis and bridge positions; C-58 fails because the vocabulary domain is not confined to non-bridge positions. V-05 demonstrates *vocabulary fragmentation* — bridge positions carry correct bridge-command labels, but non-bridge positions have split domain prefixes (`DEFAULT COMPETITOR` + `INERTIA LOCK`), neither of which threads 3+ elements; C-58 fails because C-42's precondition is not met at non-bridge positions. The two failure modes are structurally independent: V-03 satisfies C-42 globally but violates positional confinement; V-05 violates C-42 locally (at non-bridge positions). Both produce C-58 fail, but by different mechanisms.

3. **V-04's enabling design principle for C-58**: the `INERTIA THREAT` domain prefix was explicitly allocated to the three analysis-structure positions (FAIL-FIRST declaration, FM Inventory, defeat conditions), with bridge artifact authoring positions receiving a separate vocabulary domain (`[BRIDGE Qn COMMAND]`). This two-vocabulary allocation — one domain for analysis, one for bridge authoring — is the structural decision C-58 formalizes. The key number: exactly 3 `INERTIA THREAT` labels at non-bridge positions satisfies C-42's minimum threshold; the bridge positions carry 0 `INERTIA THREAT` labels, satisfying positional confinement.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["C-57 requires derivation from the discriminating component of the class annotation — the noun that varies across artifact types (ACTOR, TRIGGER) — not from the shared spine (BRIDGE); BRIDGE fails C-57 because it appears in every class label and cannot identify which artifact type is required", "C-58 has two structurally independent failure modes: positional conflation (V-03 — domain-prefix vocabulary threads 5+ labels via C-42 but spans bridge positions, violating confinement) and vocabulary fragmentation (V-05 — bridge positions correct but non-bridge domain prefix threads fewer than 3 labels, failing C-42 precondition); both fail C-58 by different mechanisms", "V-04 vs V-05 diverge for the first time in R19: V-05 was co-10.00 in R18; C-58 discriminates them — V-04 has 3 INERTIA THREAT labels at non-bridge positions (C-42 precondition met, positional confinement satisfied); V-05 has INERTIA LOCK threading only 2 non-bridge labels (C-42 precondition not met); one additional INERTIA LOCK label at a non-bridge position would close the gap"]}
```
