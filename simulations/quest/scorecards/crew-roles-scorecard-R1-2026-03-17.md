## crew-roles Skill — Quest Score Results (Round 1)

### Scores

| Variation | Score | Golden |
|-----------|-------|--------|
| V-05 — Full integration | **100** | YES |
| V-03 — Discovery algorithm | 97.5 | YES |
| V-04 — Lifecycle + formal register | 97.5 | YES |
| V-02 — Explicit field template | 91.5 | NO (C-04 essential partial) |
| V-01 — Inertia framing first | 85 | YES |

---

### Key Findings

**V-02 is the only non-golden**: Scores highest on recommended/aspirational but C-04 is PARTIAL because the template enforces format without a discovery phase. Without a structured Phase 1, model fills expertise fields from memory rather than from input vocabulary — template alone cannot substitute for structured extraction.

**The shared gap across V-03 and V-04**: Both score 97.5 and both miss C-10 the same way — they establish domain vocabulary in Phase 1 but never explicitly require the inertia-advocate's lens verify questions to reference it. One sentence in V-05 closes this.

**V-05 wins by two additions over V-03/V-04**:
1. `"Every expertise field must reference at least one term from this list"` — vocabulary-forced-field pattern
2. `"inertia-advocate's verify must name a specific system, pattern, or artifact from Phase 1"` — closes C-10

---

### New Patterns (for PRINCIPLES.md)

1. **Vocabulary-forced-field** — Phase 1 produces a named vocabulary list; every expertise field is required to reference at least one term from it. Eliminates generic content without repeating specificity instructions per field.

2. **Inertia pre-characterization** — Dedicated 3-question sub-section before writing the inertia-advocate file (current system? migration costs? user habits?) produces domain-grounded lens content without per-field reminders.

3. **Registry summary table as self-verification** — Printing `Role | Orientation | Scope | Collaborates With` after writing forces cross-reference confirmation at execution time.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["vocabulary-forced-field: Phase 1 produces a named vocabulary list; every expertise field is required to reference at least one term from that list — eliminates generic content without repeating specificity instructions per field", "inertia pre-characterization: a three-question sub-section in Phase 2 characterizes current system costs and user habits before writing the inertia-advocate file — produces domain-grounded lens without an extra per-field instruction", "registry summary table as self-verification: printing Role|Orientation|Scope|Collaborates-With after writing forces cross-reference and path confirmation at execution time and surfaces orphan refs before user review"]}
```
it Field Template

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Template block shows all 5 fields with concrete syntax |
| C-02 | PASS | "Required roles: 1. inertia-advocate — always present" |
| C-03 | PASS | "Output path: .roles/{area}/ where {area} reflects the actual input domain" |
| C-04 | PARTIAL | Template depth field says "reference actual patterns, systems, or concerns from the input" — correct instruction, but no structured discovery phase to force vocabulary extraction; generic infill risk under model drift |
| C-05 | PASS | "At least 2 additional roles" → minimum 3 total |
| C-06 | PASS | Template shows verify as "falsifiable question ending in ?" with concrete `Remove X if Y is unused.` example for simplify |
| C-07 | PASS | "Resolve all references before writing" — explicit resolve mandate |
| C-08 | PASS | "Cover at least 3 of: technical / product / strategy / ops orientations" — requirement, not target |
| C-09 | PASS | "Assign distinct scope levels. Do not give every role the same scope. Use at least 2 different values" |
| C-10 | PARTIAL | Template verify placeholder: "Why is the existing {specific system or pattern in this domain} insufficient?" — correct pattern, but placeholder may be filled generically without a Phase 1 domain scan |

**Essential**: 4.5/5 → 54 (C-04 partial)
**Recommended**: 3/3 → 30
**Aspirational**: C-09 PASS (5) + C-10 PARTIAL (2.5) → 7.5
**Composite: 91.5** | All essential: **FAIL** (C-04 partial) | **Acceptable** (not Golden)

---

### V-03 — Discovery Algorithm First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 4 lists all 5 fields explicitly |
| C-02 | PASS | "Always include: inertia-advocate" in Phase 2 |
| C-03 | PASS | "Output path: .roles/{area}/" in Phase 4 |
| C-04 | PASS | Phase 1 creates vocabulary pool ("This list becomes the vocabulary pool for expertise and lens fields"); Phase 4 requires "domain-specific, from Phase 1 vocabulary" in expertise |
| C-05 | PASS | "Minimum 3 roles. Target 4-6." |
| C-06 | PASS | Phase 4: "verify — questions ending in ? that test falsifiable conditions; simplify — directives starting with an imperative verb" |
| C-07 | PASS | Phase 3 dedicated cross-reference audit: "List all collaborates_with pairs and verify both sides name real roles in the list" |
| C-08 | PASS | Phase 2 enumerates all 4 categories with subtypes: technical (architecture, reliability, security), product (PM, UX, customers), strategy (business case, go-to-market), ops (compliance, support, migration) |
| C-09 | PASS | Phase 3 audit: "Verify scope values span at least 2 distinct levels" |
| C-10 | PARTIAL | Phase 2 says inertia's "unique view is why the status quo is already sufficient" — generic framing. Phase 1 vocabulary is available but the inertia lens is not explicitly required to reference Phase 1 terms |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: C-09 PASS (5) + C-10 PARTIAL (2.5) → 7.5
**Composite: 97.5** | All essential: PASS | **GOLDEN**

---

### V-04 — Lifecycle + Formal Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 4 lists all 5 fields with per-field minimums (at least 2 verify, at least 2 simplify) |
| C-02 | PASS | Phase 2: "Include exactly one inertia-advocate" |
| C-03 | PASS | Phase 4: "write all files to .roles/{area}/"; non-generic area requirement explicit |
| C-04 | PASS | Phase 2 manifest requires "at least one domain term from Phase 1 that will appear in its expertise field" — strongest C-04 mechanism in the first four variations |
| C-05 | PASS | "Include at least 2 additional roles" (= minimum 3 total) |
| C-06 | PASS | Phase 4: "at least 2 questions, each ending in ?" and "at least 2 rules, each starting with an imperative verb" — most explicit lens format enforcement in set |
| C-07 | PASS | Phase 3 dedicated step — adjacency map audit: "Every name in the adjacency map must be a filename from the manifest. No orphans. Resolve before advancing." |
| C-08 | PASS | Phase 2: "Together, cover at least 3 orientation categories (technical, product, strategy, ops)" |
| C-09 | PASS | Phase 2: "Assign scope levels so at least 2 distinct levels appear across the manifest" — checked before file writing |
| C-10 | PARTIAL | Phase 2 orientation says "domain-specific reasons" for inertia, and Phase 1 vocabulary is available; but lens verify questions are not explicitly required to reference Phase 1 terms — same gap as V-03 |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: C-09 PASS (5) + C-10 PARTIAL (2.5) → 7.5
**Composite: 97.5** | All essential: PASS | **GOLDEN**

---

### V-05 — Full Integration

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 3 template block shows all 5 fields with concrete frontmatter syntax |
| C-02 | PASS | Phase 2: "Name the inertia-advocate first" — structural prominence |
| C-03 | PASS | Phase 4: `.roles/{area}/`; "Do not use 'roles', 'default', or any generic segment" |
| C-04 | PASS | "Every expertise field in Phase 3 must reference at least one term from this list" (Phase 1 vocabulary) — strongest C-04 enforcement; vocabulary is structurally pre-computed before writing begins |
| C-05 | PASS | "Minimum 3 roles total." |
| C-06 | PASS | Phase 3 template with `{question ending in ?}` and `{imperative verb phrase, e.g. "Collapse X and Y..."}` examples |
| C-07 | PASS | Phase 2: "Validate collaborates_with before writing: every name must match a filename in this list" — pre-validation before Phase 3 |
| C-08 | PASS | Phase 2 covers all 4 categories; "Target at least 3 orientation categories across the full registry" |
| C-09 | PASS | Phase 2: "use at least 2 distinct levels across the registry (component, service, cross-team, org-wide)" — explicit enumeration |
| C-10 | PASS | "The inertia-advocate's verify section must include at least one question naming a specific system, pattern, or artifact from Phase 1 — not generic 'why change?' language." — closes the gap that caused C-10 PARTIAL in V-03 and V-04 |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 2/2 → 10
**Composite: 100** | All essential: PASS | **GOLDEN**

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Score | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | P | P | P | P | P | P | ~ | ~ | F | P | 85 | YES |
| V-02 | P | P | P | ~ | P | P | P | P | P | ~ | 91.5 | NO |
| V-03 | P | P | P | P | P | P | P | P | P | ~ | 97.5 | YES |
| V-04 | P | P | P | P | P | P | P | P | P | ~ | 97.5 | YES |
| V-05 | P | P | P | P | P | P | P | P | P | P | **100** | YES |

P = PASS, ~ = PARTIAL (0.5), F = FAIL

**Ranking**: V-05 (100) > V-03 = V-04 (97.5) > V-02 (91.5) > V-01 (85)

---

## Excellence Signals — V-05 Patterns

**Pattern 1 — Vocabulary-forced-field**
Establishing a named vocabulary in Phase 1 and then requiring every expertise field to "reference at least one term from this list" eliminates generic content across all roles without repeating a "be specific" instruction per field. The domain scan produces the vocabulary; the field-level mandate consumes it. This is more reliable than per-field instructions because the vocabulary exists in working memory at write time.

**Pattern 2 — Inertia pre-characterization sub-section**
Giving the inertia-advocate a dedicated three-question sub-section in Phase 2 (what is currently in place? what are the migration costs? what user habits depend on it?) before any file writing forces domain-specific content into the lens without needing a separate instruction in Phase 3. The characterization becomes the input to the file, not an aspirational guideline.

**Pattern 3 — Registry summary table as self-verification**
Printing a registry summary table after writing (Role | Orientation | Scope | Collaborates With) forces the model to confirm output path and cross-reference integrity at execution time. This doubles as a user-visible signal that the skill completed correctly and surfaces orphan references before the user has to check files manually.

---

## Differential Analysis — V-03 vs V-04 vs V-05

V-03 and V-04 both score 97.5. They address the same criteria and share the same gap (C-10 PARTIAL). The difference is **mechanism strength**:

- V-03's Phase 3 cross-reference audit happens as a listing exercise; V-04's Phase 3 produces a formal adjacency map with an explicit orphan-resolution step — stronger C-07 mechanism.
- V-04's Phase 2 role manifest requires a domain term per role before writing — stronger C-04 mechanism.
- V-03 is less verbose and easier to follow; V-04 signals to the model that each phase has a defined output state, reducing late-phase drop.

Neither closes C-10. V-05 closes it with a single additional sentence.

---

## Hypotheses Confirmed / Refuted

| Variation | Hypothesis | Outcome |
|-----------|-----------|---------|
| V-01 | Inertia-first naming improves C-02 and C-10 | Confirmed for C-02, C-10. C-09 blind spot remains — shows inertia framing does not propagate to structural decisions |
| V-02 | Explicit template eliminates missing fields and format failures | Confirmed for C-01, C-06, C-07, C-08, C-09. Discovery phase absence creates reliable C-04/C-10 partial — template alone cannot substitute for structured extraction |
| V-03 | Discovery algorithm improves C-04 and C-08 | Confirmed. Also improves C-07 and C-09 via explicit audit phases. C-10 remains partial without explicit inertia-to-vocabulary binding |
| V-04 | Lifecycle phase contracts reduce late-phase drop | Confirmed for C-07, C-09. Phase outputs used as inputs to subsequent phases eliminates structural drift better than V-03's linear instructions |
| V-05 | Full integration addresses all 10 criteria | Confirmed. Only V-05 achieves 100. The key additions over V-03/V-04: vocabulary mandate per field and inertia pre-characterization sub-section |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["vocabulary-forced-field: Phase 1 produces a named vocabulary list; every expertise field is required to reference at least one term from that list — eliminates generic content without repeating specificity instructions per field", "inertia pre-characterization: a three-question sub-section in Phase 2 characterizes current system costs and user habits before writing the inertia-advocate file — produces domain-grounded lens without an extra per-field instruction", "registry summary table as self-verification: printing Role|Orientation|Scope|Collaborates-With after writing forces cross-reference and path confirmation at execution time and surfaces orphan refs before user review"]}
```
