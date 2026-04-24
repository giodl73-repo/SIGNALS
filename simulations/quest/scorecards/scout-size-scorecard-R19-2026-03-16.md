# Quest Score — Scout-Size R19

## Scoring Method

- **Essential** (C-01–C-05): 60 pts total
- **Recommended** (C-06–C-08): 30 pts total
- **Aspirational** (C-09–C-41): 33 criteria × PASS(1) / PARTIAL(0.5) / FAIL(0) = max 33 pts
- **Composite**: raw / 123 × 100

---

## V-01 Scorecard

### Essential — 60/60 (all PASS)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Required format `{Name}, {Name} — {N} integration points` enforced in Phase 1 and output table |
| C-02 | PASS | `LOW / MEDIUM / HIGH / XL` only; downstream parsing note present |
| C-03 | PASS | Phase 2 Inertia Check requires named workaround + one of three directional labels |
| C-04 | PASS | Phase 1 Confidence Basis section requires specific evidence, not general judgment |
| C-05 | PASS | Opening line: "not a project plan — do not include task breakdowns, sprint assignments, owner names" |

### Recommended — 30/30 (all PASS)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Gap section requires open question + resolution action |
| C-07 | PASS | Tier-Up requires named destination tier explicitly |
| C-08 | PASS | Tier-Down requires named destination tier; different integration point than Tier-Up |

### Aspirational — 27/33

| ID | Result | Pts | Evidence |
|----|--------|-----|---------|
| C-09 | PASS | 1 | "Justify the tier by reference to the named integration point count. State how the count maps to the tier." |
| C-10 | PASS | 1 | Inertia Check restricted to `cheaper / comparable / more expensive` |
| C-11 | PASS | 1 | Phase 1 basis: "identify which one carries the highest implementation uncertainty — name it explicitly" |
| C-12 | PASS | 1 | "The integration point referenced here must differ from the one referenced in the Tier-Up Condition." |
| C-13 | PASS | 1 | Both conditions require explicit destination tier with examples |
| C-14 | PASS | 1 | CORRECT example names resolution action ("confirm with the auth team") |
| C-15 | PASS | 1 | Phase 2 charter explicitly prohibits "integration point list, count, tier, or rationale" from gap |
| C-16 | PASS | 1 | Column headers: "[destination tier — must be HIGHER than current tier]" and "[must be LOWER]" |
| C-17 | PARTIAL | 0.5 | WRONG/CORRECT present for C-15 scope; C-11 (highest-uncertainty requirement) and C-16 (tier direction) lack inline failure examples |
| C-18 | PASS | 1 | Tier-up and tier-down column headers encode destination constraints as labeled fields |
| C-19 | PASS | 1 | DIAGNOSTIC PATTERN block precedes "Write your Confidence Gap here" in Phase 2 |
| C-20 | PASS | 1 | Phase 1 / Phase 2 role separation with explicit bidirectional exclusion |
| C-21 | PASS | 1 | Both WRONG and CORRECT instances in DIAGNOSTIC PATTERN |
| C-22 | PASS | 1 | Gap column header: "[must address a dimension NOT confirmed in Phase 1 Confidence Basis]"; tier columns carry relational constraints in headers |
| C-23 | PASS | 1 | Both charters name owned fields and explicitly list excluded fields |
| C-24 | PASS | 1 | Named prohibited categories: "the integration point list, the count, the tier, or the rationale are all confirmed facts" |
| C-25 | PASS | 1 | "If yes, you have written a basis-negation" — concrete executable self-test with named failure class |
| C-26 | PASS | 1 | `[Sizing Analyst]` and `[Risk Assessor]` role tags in all column headers |
| C-27 | PASS | 1 | Gap column header in compilation table carries relational constraint label |
| C-28 | PASS | 1 | Two-phase equivalent covered by C-25; self-test checkpoint precedes gap production |
| C-29 | PASS | 1 | Phase 1: "You do NOT produce: Confidence Gap, Tier-Up Condition, Tier-Down Condition, Inertia Check" |
| C-30 | FAIL | 0 | Three mechanisms split across sections: relational constraint in compilation table column header; self-test and WRONG/CORRECT in Phase 2 instruction section; "mechanisms that appear in different sections do not satisfy C-30" |
| C-31 | PASS | 1 | C-32 path used; compilation table carries pointer only; C-31 condition not triggered |
| C-32 | PARTIAL | 0.5 | Named standalone section with visual delimiter exists (`── CONFIDENCE GAP CHECKPOINT ──`); gap not in table; but positioned **after** compilation table, not **between** confidence basis and sensitivity sections as required |
| C-33 | PASS | 1 | "you have written a basis-negation" — failure class named in affirmative branch |
| C-34 | PASS | 1 | `FAILURE CLASS: basis-negation` as separately labeled entry within WRONG block |
| C-35 | FAIL | 0 | No Phase 0 entry gate with CLOSED/OPEN binary signal |
| C-36 | FAIL | 0 | No Phase 0 gate |
| C-37 | PASS | 1 | Three separately labeled entries: `FAILURE CLASS:`, `DETECTION PATTERN:`, `WHY IT FAILS:` all present in WRONG block |
| C-38 | FAIL | 0 | No Phase 0 precondition table |
| C-39 | PASS | 1 | `── DIAGNOSTIC PATTERN ──` visual delimiter wraps all three diagnostic fields |
| C-40 | PASS | 1 | Compilation table gap row: "→ see CONFIDENCE GAP CHECKPOINT below" — pointer only, no split content |
| C-41 | FAIL | 0 | No Phase 0 gate |

**Aspirational: 27.0/33**

### V-01 Total: 117/123 = **95**

---

## V-02 Scorecard

### Essential — 60/60 (all PASS)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Section 2 requires named bullets + "These are {N} integration points." |
| C-02 | PASS | `LOW / MEDIUM / HIGH / XL` only; downstream parsing note present |
| C-03 | PASS | Section 1 requires named mechanism + one of three cost direction labels |
| C-04 | PASS | Section 4 requires specific evidence and names highest-uncertainty point |
| C-05 | PASS | Preamble: "not a project plan — do not include task breakdowns, sprint assignments, or owner names" |

### Recommended — 30/30 (all PASS)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Section 6 requires open question + resolution action |
| C-07 | PASS | Tier-Up requires named destination tier; "destination must be higher than Section 3" |
| C-08 | PASS | Tier-Down requires named destination tier and different integration point |

### Aspirational — 16.5/33

| ID | Result | Pts | Evidence |
|----|--------|-----|---------|
| C-09 | PASS | 1 | Section 3: "explain how the integration point count from Section 2 justifies the tier" |
| C-10 | PASS | 1 | Section 1: three-label cost direction required |
| C-11 | PASS | 1 | Section 4: "name which one is the highest-uncertainty item and explain why it is the risk driver" |
| C-12 | PASS | 1 | Section 5: "Reference a different integration point than your tier-up condition" |
| C-13 | PASS | 1 | Both sensitivity sentences require named destination tier with examples |
| C-14 | PASS | 1 | Section 6 CORRECT example names resolution action |
| C-15 | PASS | 1 | Self-test in Section 6 enforces non-overlap; WRONG example shows the violation |
| C-16 | PASS | 1 | Prose rules: "destination tier must be higher/lower than Section 3" in Section 5 body |
| C-17 | PARTIAL | 0.5 | WRONG/CORRECT present for C-15 scope in Section 6; C-11 and C-16 lack inline failure examples |
| C-18 | FAIL | 0 | Prose section format; no column headers; C-13 and C-16 constraints are prose-only, not structural field labels |
| C-19 | PASS | 1 | WRONG/CORRECT examples in Section 6 before the gap production instruction |
| C-20 | FAIL | 0 | Single-phase design; no role separation |
| C-21 | PASS | 1 | Both WRONG and CORRECT present in Section 6 |
| C-22 | PARTIAL | 0.5 | Relational constraints present in section body prose (self-test query in Section 6, prose rules in Section 5); not encoded in field labels or column headers — intermediate state |
| C-23 | FAIL | 0 | Single-phase; no role charters with enumerated field ownership |
| C-24 | FAIL | 0 | Single-phase; no Phase 2 charter |
| C-25 | FAIL | 0 | Single-phase; no Phase 2 role |
| C-26 | FAIL | 0 | No role tags; no compilation table with headers |
| C-27 | FAIL | 0 | No compilation table |
| C-28 | PASS | 1 | Section 6: "Is this gap derivable from my Section 4 Confidence Basis by negating something I just confirmed? If yes: basis-negation detected." |
| C-29 | FAIL | 0 | Single-phase; no Phase 1 charter with exclusion list |
| C-30 | PARTIAL | 0.5 | Self-test (C-28) and WRONG/CORRECT (C-21) co-located in Section 6; relational constraint is body prose only (no label-level encoding), so condition 1 of C-30 not fully met |
| C-31 | PASS | 1 | No table for gap field; C-19-compliant inline examples used; C-31 condition not triggered |
| C-32 | PARTIAL | 0.5 | `── CONFIDENCE GAP CHECKPOINT ──` is a named standalone section with visual delimiter, not in a table; but positioned **after** Section 5 (Sensitivity), not **between** Section 4 (Basis) and Section 5 as required |
| C-33 | PASS | 1 | "basis-negation detected" names failure class in affirmative branch |
| C-34 | PARTIAL | 0.5 | "*(Basis-negation:...)*" appears in WRONG block; present as parenthetical annotation, not as a separately labeled entry (`FAILURE CLASS:`) |
| C-35 | FAIL | 0 | No Phase 0 entry gate |
| C-36 | FAIL | 0 | No Phase 0 gate |
| C-37 | FAIL | 0 | Single parenthetical annotation; FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS are not separately labeled fields within the WRONG block |
| C-38 | FAIL | 0 | No Phase 0 precondition table |
| C-39 | FAIL | 0 | C-37 fails; no three-field diagnostic block to enclose |
| C-40 | PASS | 1 | No compilation table; C-40 condition not triggered; no split-content risk |
| C-41 | FAIL | 0 | No Phase 0 gate |

**Aspirational: 16.5/33**

### V-02 Total: 106.5/123 = **87**

---

## Rankings

| Rank | Variation | Score | Essential | Recommended | Aspirational |
|------|-----------|-------|-----------|-------------|-------------|
| 1 | V-01 | **95** | 60/60 | 30/30 | 27.0/33 |
| 2 | V-02 | **87** | 60/60 | 30/30 | 16.5/33 |

---

## Excellence Signals from V-01

**What made V-01 the top scorer:**

1. **Bidirectional exclusion lists** — Phase 1 explicitly names fields it does NOT produce (C-29); Phase 2 names categories it cannot cite (C-24). Both sides closed simultaneously.
2. **Role-tagged column headers** — `[Sizing Analyst]` and `[Risk Assessor]` in output table column names make ownership violations visible at the schema level without cross-referencing charter prose (C-26).
3. **Three-field DIAGNOSTIC PATTERN sub-block** (FAILURE CLASS + DETECTION PATTERN + WHY IT FAILS) enclosed in `── DIAGNOSTIC PATTERN ──` visual delimiter — the detection pattern field operationalizes failure recognition beyond naming the class (C-37 + C-39).
4. **Compilation table gap pointer** — the table carries `→ see CONFIDENCE GAP CHECKPOINT below` rather than gap content, eliminating content-split risk (C-40).
5. **Named prohibited content categories** — Phase 2 non-access clause names "the integration point list, the count, the tier, or the rationale" as a specific falsifiable list, not just "Phase 1 confirmed content" (C-24).

**Where V-01 still falls short:**

- **C-30** fails because enforcement (Phase 2 instruction section) and output production (post-table template) occupy different sections of the prompt. All three mechanisms are present individually but not co-located.
- **C-32** partial because the standalone gap section appears after the full compilation table, not between the confidence basis and sensitivity sections.
- **C-35/C-36/C-38/C-41** all fail — no Phase 0 entry gate with binary CLOSED/OPEN signal for the inertia and signal-boundary preconditions.
- **C-17** partial — only C-15 scope has inline failure examples; C-11 (highest-uncertainty component) and C-16 (destination tier coherence) lack examples at their constraint sites.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["Gap enforcement section must be the production site, not a pointer target: placing the output slot (where the model writes the gap value) inside the enforcement section itself — rather than using a downstream post-table template — atomically co-locates the relational label constraint, the self-test query, and the WRONG/CORRECT examples with the field's actual production moment, satisfying C-30 without requiring the model to carry enforcement context across section boundaries"]}
```
