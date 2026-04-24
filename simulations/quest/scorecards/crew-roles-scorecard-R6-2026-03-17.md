# Quest Score — crew-roles R6

**Rubric version:** v6 (17 aspirational criteria, C-09–C-25)
**Formula:** `aspirational_pass / 17 × 100` (each full PASS ≈ 5.88 pts; max = 100)
**Trace artifact:** None. Evaluated against skill specification text.

---

## Variations Available

| Variation | Content Status |
|-----------|---------------|
| V-01 | Complete (6-phase lifecycle) |
| V-02 | Incomplete — STEP 1 only; V-02 through V-05 body not provided |
| V-03–V-05 | Not provided |

Scoring proceeds for V-01 in full. V-02 is scored against visible content only, with unscoreable criteria marked `—`.

---

## V-01 — Lifecycle Emphasis

**Hypothesis:** Naming every phase as a discrete structural unit with an explicit entry precondition and named exit artifact makes blocking gates unavoidable at execution time, increasing pass rates on C-15, C-17, C-22, C-23, C-24, C-25.

### Essential (all 5 required)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | All 5 fields | **PASS** | Phase 5 lists all 5 fields as explicit required fields under "Required fields in every role file." |
| C-02 | Inertia-advocate present | **PASS** | Phase 5: "Minimum 3 roles total, including the inertia-advocate." Phase 5 specifies inertia-advocate requirements as a distinct subsection. |
| C-03 | Correct output path | **PASS** | Phase 5: "Write each role as a markdown file at `.roles/{area}/{role-name}.md`." |
| C-04 | Domain specificity | **PASS** | Phase 5: "`expertise.relevance` — must reference at least one vocabulary term from Phase 1." Phase 1 terms are domain-extracted, not generic. |
| C-05 | Minimum 3 roles | **PASS** | Phase 5: "Minimum 3 roles total, including the inertia-advocate." |

**Essential result: 5/5 PASS ✓**

---

### Recommended (partial credit 0.5 per PARTIAL)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-06 | Lens actionability | **PASS** | Phase 5: "`orientation.verify` — questions only; every item ends with `?`" and "`orientation.simplify` — imperatives only; every item is an action phrase." Both constraints stated as structural requirements, not suggestions. |
| C-07 | Collaborates_with resolves | **PASS** | Phase 6 CHECK 2 (Orphan Reference Check): "For every `collaborates_with` value across all role files: verify the referenced name matches a file in the registry… Any unresolved reference is a blocking error." |
| C-08 | Perspective diversity | **PASS** | Phase 5: "Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly." |

**Recommended result: 3/3 PASS**

---

### Aspirational (partial credit 0.5 per PARTIAL; denominator 17)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-09 | Scope gradient | **PASS** | Phase 4 (Pre-Write Scope Audit): "at least 2 distinct scope values must appear in the plan before writing begins." Gate blocks writing if all planned roles share one scope. |
| C-10 | Inertia domain-grounded | **PASS** | Phase 2 Q1 requires naming the specific Current-System Term. Phase 3 frame template requires Q1 content verbatim in `orientation.frame`. Domain specificity is structural, not advisory. |
| C-11 | Vocabulary-forced-field | **PASS** | Phase 1 produces named buckets; Phase 5 mandates `expertise.relevance` reference ≥1 Phase 1 term per role. Phase 6 CHECK 4 enforces this at the verification gate. |
| C-12 | Inertia pre-characterization | **PASS** | Phase 2 explicitly answers Q1 (current system), Q2 (migration cost), Q3 (user habit) before any role is written. Phase 5 requires inertia-advocate `orientation.verify` to reference ≥2 of these 3 dimensions. |
| C-13 | Registry summary table | **PASS** | Phase 6 CHECK 1 produces `Role \| Orientation Frame (excerpt) \| Scope \| Collaborates With` table. "Every written role must appear in this table." |
| C-14 | Scope-gradient-enforcement | **PASS** | Phase 4 is a structural gate (not a soft instruction): "Writing is blocked until the gate passes — this is a prevention step, not a post-write correction." Phase 6 CHECK 3 re-confirms at delivery. |
| C-15 | Verification-gate-phase | **PASS** | Phase 6 is explicitly named "VERIFICATION GATE." Bundles CHECK 1–4; "Delivery is blocked until every check shows PASS. A single FAIL blocks delivery regardless of other checks passing." |
| C-16 | Vocabulary-linked inertia Q&A | **PASS** | Phase 2 draws Q1 from Current-System bucket, Q2 from Migration-Cost bucket, Q3 from User-Habit bucket — all Phase 1 outputs. C-11 and C-12 are structurally wired through the bucket mechanism, not independently satisfied. |
| C-17 | Pre-write scope audit | **PASS** | Phase 4 is exactly this gate: surveys planned role set, assigns scope values, blocks writing until ≥2 distinct scopes appear. "this is a prevention step, not a post-write correction." |
| C-18 | Vocabulary check in verification gate | **PASS** | Phase 6 CHECK 4 (Vocabulary Coverage Check): "verify `expertise.relevance` references at least one Phase 1 vocabulary term… Any role without a vocabulary reference is a blocking error. Result: PASS / FAIL." Gate won't pass without CHECK 4 result. |
| C-19 | Inertia frame Q-slot template | **PASS** | Phase 3 supplies the verbatim template with `[Q1 current system]` and `[Q2 migration cost]` named placeholders: "Fill both slots from Phase 2 answers." Named placeholders must be filled, not soft-referenced. |
| C-20 | Q-domain-aligned vocabulary distribution | **PASS** | Phase 2 requires Q1 answer from Current-System bucket, Q2 from Migration-Cost bucket, Q3 from User-Habit bucket. Cross-bucket selection fails Phase 2 exit. Different buckets per Q structurally prevents same-term reuse across all three. |
| C-21 | Bucketed vocabulary extraction | **PASS** | Phase 1 produces three named buckets: Current-System Terms, Migration-Cost Terms, User-Habit Terms. "Each term is assigned to exactly one bucket at extraction time." Phase 2 Q-to-bucket mapping enforced per question. |
| C-22 | Domain-alignment audit table at Phase 2 exit | **PASS** | Phase 2 specifies the `Q-number \| Term Used \| Expected Bucket \| Match YES/NO` table. "Gate condition: all three rows must show YES simultaneously. Evaluating rows independently does not satisfy the gate." Table is a named structural artifact in the output. |
| C-23 | Frame Fill as dedicated phase | **PASS** | Phase 3 is explicitly "PHASE 3 — FRAME FILL" with an entry precondition (Phase 2 exit artifact present) and named exit artifact (completed frame string + slot-source binding record). Phase 4 does not begin until this artifact is present. |
| C-24 | Audit-table full re-evaluation after replacement | **PASS** | Phase 2: "Restart the audit table from row 1. Re-evaluate all three rows at once. The gate condition is evaluated against the full table, not against the replaced row alone. An incremental re-score of only the replaced row does not satisfy the gate — a replacement term may pass its own row while reusing a term already used in another row." Full restart logic is explicit and its rationale is stated. |
| C-25 | Frame-slot source citation in Frame Fill output | **PASS** | Phase 3 requires the slot-source binding record: "`Q1 slot ← Phase 2 Q1: [verbatim Q1 answer]` / `Q2 slot ← Phase 2 Q2: [verbatim Q2 answer]`." Includes slot-binding verification: "A mismatch in either binding is a blocking error." "A completed frame string without source citations does not satisfy the Frame Fill phase exit condition." |

**Aspirational result: 17/17 PASS**

**V-01 Score: 17/17 × 100 = 100.0**

---

## V-02 — Inertia Framing (Incomplete)

**Hypothesis:** Foregrounding the inertia-advocate as the anchor role increases C-10, C-12, C-16, C-19, C-20 pass rates.

Only STEP 1 (Domain Vocabulary) is present in the provided text. STEP 1 shows bucketed extraction (Bucket A: Current-System Terms visible before truncation). No inertia characterization, frame fill, scope audit, role writing, or verification gate content is present.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01–C-05 | Essential | `—` | Role writing phase not present in spec. |
| C-06–C-08 | Recommended | `—` | No role field constraints visible. |
| C-09 | Scope gradient | `—` | No scope audit step visible. |
| C-10 | Inertia domain-grounded | `—` | No Q&A phase visible. |
| C-11 | Vocabulary-forced-field | `—` | Phase 1 bucket extraction present, but no role-writing constraints visible to confirm linkage. |
| C-12–C-25 | Remaining aspirational | `—` | Steps not present in provided content. |
| C-21 | Bucketed vocabulary extraction | **PARTIAL** | STEP 1 names "Bucket A — Current-System Terms" with stated definition. Bucketing pattern is present; other two buckets and term-assignment logic not visible before truncation. |

**V-02 Score: Unscoreable (content incomplete)**

---

## V-03–V-05

Not provided. Cannot score.

---

## Rankings

| Rank | Variation | Score | Essential | Notes |
|------|-----------|-------|-----------|-------|
| 1 | V-01 | **100.0** | All PASS | Complete 6-phase specification; all 17 aspirational criteria met |
| — | V-02 | N/A | Unknown | Incomplete; STEP 1 visible only |
| — | V-03–V-05 | N/A | Unknown | Not provided |

---

## Excellence Signals — V-01

**ES-1: Full-table restart as a gate condition**
V-01 Phase 2 explicitly requires that after any term replacement, the audit table restarts from row 1 and all three rows are evaluated simultaneously. The spec states the rationale inline: "a replacement term may pass its own row while reusing a term already used in another row or drawing from an adjacent bucket, introducing a cross-row conflict that only a full pass detects." The gate condition is defined against the table as a unit, and incremental re-evaluation is explicitly named as insufficient. This is the architectural realization of C-24 — the criterion is not just listed but its failure mode is named in the gate text.

**ES-2: Phase exit requires provenance, not just shape**
V-01 Phase 3 requires the Frame Fill phase artifact to include slot-source binding citations alongside the completed frame string. The exit condition is stated in terms of what the artifact must carry, not what it must look like: "A completed frame string without source citations does not satisfy the Frame Fill phase exit condition." Slot-binding verification is a named blocking check. This is the architectural realization of C-25 — the gate is on provenance presence, not output correctness.

---

## Second-Order Observations

Both ES-1 and ES-2 share a structural property: **the gate condition is defined against a property of the artifact that is invisible in the artifact's surface form**. A completed audit table with all-YES rows looks identical whether or not row 1 was re-evaluated after a row-3 replacement. A completed frame string looks identical whether or not the Q1 slot came from the Q1 answer. V-01 closes both gaps by making the non-surface property (restart trace, source binding) an explicit required component of the exit artifact — not a verification instruction but a content requirement.

No new second-order gaps are visible from V-01 alone. A potential residual: Phase 6 CHECK 4 verifies vocabulary coverage per role but does not verify the Phase 1 term used in `expertise.relevance` is drawn from the correct bucket (a term could be used that was extracted but assigned to a different bucket than the role's domain context warrants). This is a weaker gap and may be out of scope for crew-roles.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Full-table restart gate: after any item replacement, re-evaluation must restart from row 1 and evaluate all items simultaneously as a unit — per-item re-scoring satisfies the local row but cannot detect cross-item conflicts introduced by the replacement term", "Provenance as phase exit condition: a phase output artifact must carry explicit source citations for each slot populated from a prior phase — a correctly-shaped output without citations cannot structurally verify correct slot-source binding before the next phase begins"]}
```
