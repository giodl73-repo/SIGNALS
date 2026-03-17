## Round 1 Scoring — quest-rubric

### Rubric v1 Reference

| ID | Weight | Short label |
|----|--------|-------------|
| C-01 | essential | All 5 criterion fields present |
| C-02 | essential | Essential count 3–5 |
| C-03 | essential | Pass conditions self-contained (two-scorer test) |
| C-04 | essential | Scoring formula with correct denominators |
| C-05 | essential | Golden threshold states both conditions |
| C-06 | recommended | All three tiers with correct counts |
| C-07 | recommended | Essential criteria skill-specific (not generic) |
| C-08 | recommended | Category variety across essential |
| C-09 | aspirational | Frontmatter complete and correct |
| C-10 | aspirational | Common failure modes section present |

---

### V-01 — Role Sequence: ANALYST → AUDITOR → DEFINER

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | DEFINER OUTPUT GATE explicitly requires "every criterion has all five fields: ID, text, weight, category, pass condition" before emission |
| C-02 | PASS | "Essential: 3–5 criteria" stated in DEFINER + output gate confirms count |
| C-03 | PASS | AUDITOR role applies two-scorer test to each behavior and rejects VAGUE ones before DEFINER receives them; output gate confirms all passed |
| C-04 | PASS | DEFINER says replace {E}, {R}, {A} with actual counts; output gate checks denominator match |
| C-05 | PASS | Output gate requires "all-essential AND composite >= 80" — both conditions named |
| C-06 | PASS | All three tiers defined with explicit count ranges in DEFINER |
| C-07 | PARTIAL | AUDITOR has a specificity test (marks GENERIC and returns); probe assessment is "Moderate" — ANALYST can write behaviors without contrast against foil, so some generic criteria may survive if AUDITOR judgment is soft |
| C-08 | PASS | "Essential criteria must span at least 2 distinct categories" stated in DEFINER |
| C-09 | PASS | EMIT FORMAT shows all four frontmatter fields in correct types |
| C-10 | PASS | DEFINER explicitly requires "a 'Common Failure Modes' section with an empty table" |

**Essential pass:** 5/5 → 60 pts
**Recommended pass:** 2.5/3 (C-07 partial) → 25 pts
**Aspirational pass:** 2/2 → 10 pts
**Composite: 95** | All essential: **YES**

---

### V-02 — Output Format: Per-Criterion Prose Blocks

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Prose block format labels all five fields: `**C-NN: title**`, Weight, Category, Pass condition (ID embedded in title header) |
| C-02 | PASS | "Essential (3–5): Non-negotiable behaviors" stated in WEIGHT RULES |
| C-03 | FAIL | Prose format gives space but no review gate; "Do not use 'should', 'generally'" is advisory only — a model can comply syntactically while still writing un-evaluable conditions |
| C-04 | PASS | Scoring section instructs to replace E, R, A with actual counts before emitting |
| C-05 | PASS | Template explicitly shows "**Golden threshold: all essential criteria pass AND composite >= 80.**" |
| C-06 | PASS | Sequence requirement: essential → recommended → aspirational; all three tiers |
| C-07 | FAIL | "must cover skill-specific behaviors" is a requirement statement with no enforcement; format has no specificity gate or prohibition on generic criteria |
| C-08 | PASS | "Essential criteria must span at least 2 distinct categories" stated |
| C-09 | PASS | FRONTMATTER section shows all four fields with correct type expectations |
| C-10 | PASS | FAILURE MODES SECTION explicitly required as "structural placeholder" |

**Essential pass:** 4/5 (C-03 fails) → 48 pts
**Recommended pass:** 2/3 (C-07 fails) → 20 pts
**Aspirational pass:** 2/2 → 10 pts
**Composite: 78** | All essential: **NO** (C-03 hard fail)

---

### V-03 — Lifecycle Emphasis: Failure-First Phase

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 3 table format shows all five columns: `| ID | Text | Weight | Category | Pass Condition |` |
| C-02 | PASS | Phase 2: "Weight counts: 3–5 essential" |
| C-03 | PARTIAL | Phase 2 self-check: "could two independent scorers evaluate this pass condition without consulting the skill spec? If not, sharpen by naming the specific field, count, label, or value." The guidance is directionally correct but there is no external gate — a model self-assessing may not catch its own vagueness |
| C-04 | PASS | Phase 4: "where E, R, A are the actual counts of criteria written above. Recompute after Phase 3." |
| C-05 | PASS | Phase 4 shows `"all essential criteria pass AND composite >= 80"` as the threshold statement |
| C-06 | PASS | All three tiers in Phase 2 with count requirements |
| C-07 | PASS | Phase 1 requires cataloging skill-specific failures before writing any criterion; criteria derived from named failure modes cannot be generic presence checks — the lifecycle forces specificity |
| C-08 | PASS | Phase 2: "Category variety: essential criteria must span at least 2 distinct categories" |
| C-09 | PASS | Phase 4 shows all four frontmatter fields |
| C-10 | PASS | Phase 4 shows "Common Failure Modes section — empty table, structural placeholder" |

**Essential pass:** 4/5 (C-03 partial treated as fail) → 48 pts
**Recommended pass:** 3/3 → 30 pts
**Aspirational pass:** 2/2 → 10 pts
**Composite: 88** | All essential: **NO** (C-03 partial fails golden gate)

---

### V-04 — Phrasing Register: Imperative DO/DO NOT

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "DO NOT emit a criterion missing any of these five fields" + explicit ordered list |
| C-02 | PASS | "DO write 3–5 essential criteria. DO NOT write fewer than 3. DO NOT write more than 5." — binary prohibitions |
| C-03 | PASS | Explicit prohibitions on hedging words ("DO NOT use 'should', 'generally', 'typically', 'usually', or 'appropriate'") + TWO-SCORER TEST with "DO NOT proceed with a condition that fails" — prohibition is checkable at a glance |
| C-04 | PASS | "DO NOT emit a formula whose denominators do not match the actual criterion counts" — hard prohibition |
| C-05 | PASS | "DO NOT omit either condition. DO NOT write only 'score >= 80' without the all-essential gate." |
| C-06 | PASS | "DO NOT omit any tier" + explicit count requirements per tier |
| C-07 | PARTIAL | "must cover the skill-specific behaviors of {skill} — not generic rubric structure" is stated as a requirement, not enforced with a prohibition; no foil or derivation step forces specificity; probe says "Moderate" |
| C-08 | PASS | "DO ensure essential criteria span at least 2 distinct categories. DO NOT write all essential criteria in the same category." |
| C-09 | PASS | Explicit prohibitions on wrong types: "DO NOT use prose date format... DO NOT use a string version" |
| C-10 | PASS | "DO write a 'Common Failure Modes' section... DO NOT omit this section." |

**Essential pass:** 5/5 → 60 pts
**Recommended pass:** 2/3 (C-07 partial treated as fail) → 20 pts
**Aspirational pass:** 2/2 → 10 pts
**Composite: 90** | All essential: **YES**

---

### V-05 — STATUS QUO RUBRIC Foil + Lifecycle Emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 2 table format with five columns; Phase 3 structure requirement |
| C-02 | PASS | "Essential (3–5): Derived from blocking failures" |
| C-03 | PASS | STATUS QUO failure 2 explicitly names "vague pass conditions" — Phase 1 contrast analysis requires "no hedging language... names exactly what passes and exactly what fails, in terms a scorer can check without consulting the skill spec." Foil derivation forces concrete language. |
| C-04 | PASS | STATUS QUO failure 5 explicitly names "formula with wrong denominators" — Phase 1 contrast requires immunity: "E, R, A are the actual counts above. Compute last; never assume a count." |
| C-05 | PASS | Phase 3 shows "**Golden threshold: all essential criteria pass AND composite >= 80.**" |
| C-06 | PASS | All three tiers in Phase 2 with count requirements |
| C-07 | PASS | STATUS QUO failure 1 explicitly names "generic presence checks" — Phase 1 contrast requires "pass condition names a specific value, count, or label — not a structural type"; foil example given: "'Contains criteria' fails. 'Each criterion row has exactly 5 columns in order: …' passes." |
| C-08 | PASS | "Essential criteria must span at least 2 distinct categories." |
| C-09 | PASS | Phase 3 shows all four frontmatter fields |
| C-10 | PASS | Phase 3 shows "Common Failure Modes section — empty table, structural placeholder" |

**Essential pass:** 5/5 → 60 pts
**Recommended pass:** 3/3 → 30 pts
**Aspirational pass:** 2/2 → 10 pts
**Composite: 100** | All essential: **YES**

---

### Round 1 Summary

| Rank | V | Composite | All Essential | C-03 | C-07 |
|------|---|-----------|---------------|------|------|
| 1 | V-05 | 100 | YES | PASS | PASS |
| 2 | V-01 | 95 | YES | PASS | PARTIAL |
| 3 | V-04 | 90 | YES | PASS | PARTIAL |
| 4 | V-03 | 88 | NO | PARTIAL | PASS |
| 5 | V-02 | 78 | NO | FAIL | FAIL |

---

### Excellence Signals — V-05

**Signal 1: Named foil with labeled failure modes addresses both C-03 and C-07 in one structure.**
The STATUS QUO RUBRIC's five named failures are each directly mapped to an immune criterion property. Generic presence checks (failure 1) and vague pass conditions (failure 2) are the two hardest criteria to close — V-05 addresses them not through prohibition or self-check, but through derivation. When a criterion must be the contrast of a named failure, it cannot remain generic.

**Signal 2: Foil-to-criterion immunity mapping makes specificity structural, not aspirational.**
V-03 asks for failure analysis first (improving C-07), V-04 prohibits hedging words (improving C-03), but only V-05 makes the connection explicit: each criterion must be immune to a specific, named foil failure. This means a builder cannot write a criterion without also naming the failure mode it defeats — and naming a failure forces concrete observables. The Phase 1 table (`Foil failure → what an immune essential criterion must do`) is the mechanism.

**Signal 3: Formula denominator failure named in the foil guarantees C-04 attention.**
V-05 is the only variation where the formula-with-wrong-denominators failure is called out as a known failure mode (STATUS QUO failure 5). The contrast instruction ("Compute last; never assume a count") directly addresses the substitution error. Other variations instruct replacement of placeholders but don't name the failure mode that causes the error.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named foil with explicit failure modes forces criteria to be derived as contrasts — simultaneously closes C-07 (generic checks) and C-03 (vague pass conditions) through derivation rather than prohibition", "Foil-to-criterion immunity mapping: requiring each criterion to be immune to a named foil failure produces specific verifiable pass conditions by construction, not by instruction"]}
```
