## Scoring: mock-all Variate R6

### Rubric Reference (v6)

12 criteria — Essential (C-01–05, 60%), Recommended (C-06–08, 30%), Aspirational (C-09–18, 10%, denom=12).

---

### V-01 — Role Sequence: Identity Constraint Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | ROLE 2 template produces MOCK ARTIFACT header block for all nine namespaces in table order |
| C-02 | PASS | Classification table assigns EVIDENCE-HEAVY (prove, listen), HIGH-STRUCTURE (trace, flow), MIXED (rest) correctly |
| C-03 | PASS | REAL-REQUIRED = YES for prove, listen; conditional YES for compliance-tagged namespaces |
| C-04 | PASS | Coverage summary with Namespace / Category / Flag / Recommended Next Step columns, ROLE 3 |
| C-05 | PASS | `Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md` as final output of ROLE 4 |
| C-06 | PASS | Flag rules include TIER-CRITICAL for trace-*, scout-feasibility, listen-* at tier >= 2 |
| C-07 | PASS | Template body placeholder is vocabulary-constrained; ROLE 2 produces one section per namespace |
| C-08 | PASS | REAL-REQUIRED rationale preamble covers compliance-active namespaces (scout-compliance, trace-permissions) |
| C-09 | PASS | Tier conditional in classification table; TIER-CRITICAL flag applied at tier >= 2 in ROLE 3 |
| C-10 | PASS | Recommended Next Step explicitly formatted as `/namespace:skill {topic}` — no generic advice |
| C-11 | PASS | ROLE 1 (classification table) structurally precedes ROLE 2 (artifact generation) |
| C-12 | PASS | `#### HANDOFF` is a dedicated, labelled ROLE 4 block; `DO NOT write {this-file} as a literal placeholder` present |
| C-13 | PASS | Preamble rationale in ROLE 1 ("A synthetic artifact cannot substitute for real signal…") + per-instance rationale in ROLE 2 template |
| C-14 | PASS | "ROLE 1 STOP", "ROLE 2 STOP", "ROLE 3 STOP" each include explicit "Do not activate ROLE N+1 until…" sentence |
| C-15 | PASS | MUST use and DO NOT use as separate columns in classification table; DO NOT prohibitions explicit per category |
| C-16 | PASS | ROLE 1 STOP enumerates all six required fields by name: Category, MUST-use, DO NOT-use, Tier 2/3 Critical, Compliance-Tagged, REAL-REQUIRED |
| C-17 | PASS | MUST use / DO NOT use vocabulary is columns in the classification table, co-located with category row |
| C-18 | PASS | CLASSIFIER / GENERATOR / SUMMARIZER / HANDOFF WRITER; "the moment you write an artifact body here, you are acting as ROLE 2 — GENERATOR, which you are not yet" — identity violation framing at ontological level |

**Score: 12/12 aspirational → 100**

---

### V-02 — Output Format: Co-located Template Depth Anchor

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Template in ROLE 2 specifies MOCK ARTIFACT header blocks for all nine namespaces |
| C-02 | PASS | Classification table assigns categories correctly |
| C-03 | PASS | REAL-REQUIRED = YES for prove, listen; conditional for compliance-active |
| C-04 | PASS | Coverage summary with correct columns in ROLE 3 |
| C-05 | PASS | Handoff line in dedicated ROLE 4 HANDOFF section |
| C-06 | PASS | Flag rules include TIER-CRITICAL |
| C-07 | PASS | `{3-5 sentence artifact body…}` co-located in template placeholder; depth anchor at generation point |
| C-08 | PASS | Compliance namespaces covered in REAL-REQUIRED rationale preamble |
| C-09 | PASS | Tier conditional present |
| C-10 | PASS | Specific skill calls required in Recommended Next Step |
| C-11 | PASS | ROLE 1 (classification) precedes ROLE 2 (generation) |
| C-12 | PASS | `#### HANDOFF` in dedicated ROLE 4 block; `DO NOT leave any placeholder as a literal string` covers `{this-file}` |
| C-13 | PASS | Rationale preamble in ROLE 1; per-instance rationale in template |
| C-14 | PASS | ROLE 1/2/3 STOP with explicit "Do not activate" phrases |
| C-15 | PASS | MUST / DO NOT vocabulary both present in template placeholder; explicit per-category prohibitions |
| C-16 | PASS | ROLE 1 STOP names 4 table fields; ROLE 2 STOP enumerates header block, inertia statement, body, REAL-REQUIRED statement |
| C-17 | **FAIL** | Vocabulary rules in ROLE 2 template placeholder, NOT as columns in the classification table. C-17 requires "co-located with the category assignment row" in the table itself; template placement is downstream generation, not pre-classification. Confirms template co-location ≠ table-column co-location for C-17. |
| C-18 | PASS | Named roles present; "Producing output that belongs to a later role is a role violation" frames identity violation; per-role "You are the CLASSIFIER / GENERATOR..." |

**Score: 11/12 aspirational → ~91.7**

---

### V-03 — Inertia Framing Upgraded

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | ROLE 2 template produces MOCK ARTIFACT header blocks for all nine namespaces |
| C-02 | PASS | Classification table with correct category assignments |
| C-03 | PASS | REAL-REQUIRED = YES for prove, listen; conditional for compliance-active |
| C-04 | PASS | Coverage summary with correct columns in ROLE 3 |
| C-05 | PASS | Handoff line in dedicated ROLE 4 HANDOFF section |
| C-06 | PASS | Flag rules include TIER-CRITICAL |
| C-07 | PASS | Inertia question ("Without this signal, {topic}'s feature story would be missing:") forces body to be topically grounded, not merely vocabulary-compliant; "a body that could have been written without the inertia answer is too generic and must be revised" |
| C-08 | PASS | Compliance namespaces covered in REAL-REQUIRED rationale preamble |
| C-09 | PASS | Tier conditional present |
| C-10 | PASS | Recommended next step "should address the specific gap named in the inertia statement for this namespace" — inertia-derived next steps are gap-specific above and beyond category assignment |
| C-11 | PASS | ROLE 1 classification precedes ROLE 2 generation |
| C-12 | PASS | `#### HANDOFF` dedicated ROLE 4 block; `DO NOT write {this-file} as a literal placeholder` |
| C-13 | PASS | Preamble rationale + per-instance rationale in ROLE 2 template |
| C-14 | PASS | ROLE 1/2/3 STOP with explicit "Do not activate" sentences |
| C-15 | PASS | MUST use / DO NOT use as columns in the classification table; prohibitions explicit per category |
| C-16 | PASS | ROLE 1 STOP enumerates all six fields; ROLE 2 STOP enumerates header block, inertia statement, body, REAL-REQUIRED statement |
| C-17 | PASS | MUST use / DO NOT use vocabulary columns present in classification table (R5 V-03 miss fixed) |
| C-18 | PASS | "Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet" — identity violation framing; per-role named identities throughout |

**Score: 12/12 aspirational → 100**

---

### V-04 — Role Sequence + Lifecycle Emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Template specifies MOCK ARTIFACT header blocks for all nine namespaces |
| C-02 | PASS | Classification table with correct assignments |
| C-03 | PASS | REAL-REQUIRED = YES for prove, listen |
| C-04 | PASS | Coverage summary with correct columns |
| C-05 | PASS | Handoff line in dedicated ROLE 4 section |
| C-06 | PASS | Flag rules include TIER-CRITICAL |
| C-07 | PASS | Vocabulary-constrained template body; ROLE 2 generates all nine sections |
| C-08 | PASS | Compliance namespaces flagged REAL-REQUIRED in rationale preamble |
| C-09 | PASS | Tier conditional present |
| C-10 | PASS | ROLE 3 STOP explicitly prohibits generic next steps: "DO NOT write generic advice. DO NOT write 'gather more signals.'" |
| C-11 | PASS | ROLE 1 classification precedes ROLE 2 generation |
| C-12 | PASS | Dedicated `#### HANDOFF` in ROLE 4; `DO NOT write {this-file} as a literal placeholder` |
| C-13 | PASS | Rationale preamble + per-instance in ROLE 2 template |
| C-14 | PASS | Explicit stop-gate phrases at every phase boundary |
| C-15 | PASS | MUST use / DO NOT use as table columns; explicit per-category prohibitions |
| C-16 | PASS | Most complete enumeration of any variation — ROLE 1 STOP: numbered conditions (1)–(6) naming every field; ROLE 2 STOP: numbered conditions (1)–(4); ROLE 3 STOP: numbered conditions (1)–(4). "A table row with an empty Flag cell or a generic next step does not satisfy this gate." |
| C-17 | PASS | Vocabulary columns in classification table |
| C-18 | PASS | Strongest identity framing: "You are the CLASSIFIER. You classify." + "Writing an artifact body in this section means you are ROLE 2 — GENERATOR, which you are not yet. Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet." Both wrong-phase output types named explicitly. |

**Score: 12/12 aspirational → 100**

---

### V-05 — Full Combination (Role + Template + Inertia)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Template specifies MOCK ARTIFACT header blocks for all nine namespaces |
| C-02 | PASS | Classification table with correct assignments |
| C-03 | PASS | REAL-REQUIRED = YES for prove, listen |
| C-04 | PASS | Coverage summary with correct columns |
| C-05 | PASS | Handoff line in dedicated ROLE 4 HANDOFF section |
| C-06 | PASS | Flag rules include TIER-CRITICAL |
| C-07 | PASS | Co-located template depth anchor + inertia framing both active; "a body that could exist without the inertia answer is too generic" |
| C-08 | PASS | Compliance namespaces covered in REAL-REQUIRED rationale |
| C-09 | PASS | Tier conditional present |
| C-10 | PASS | Recommended next steps "should address the specific gap named in the inertia statement" — gap-derived specificity |
| C-11 | PASS | ROLE 1 classification precedes ROLE 2 generation |
| C-12 | PASS | Dedicated HANDOFF block; `DO NOT write {this-file} as a literal placeholder` |
| C-13 | PASS | Rationale preamble + per-instance in template |
| C-14 | PASS | ROLE 1/2/3 STOP with explicit "Do not activate" sentences |
| C-15 | PASS | MUST / DO NOT vocabulary both present in template placeholder with explicit per-category prohibitions |
| C-16 | PASS | ROLE 1 STOP names 4 table fields (all fields in table); ROLE 2 STOP enumerates header block, inertia statement, body, REAL-REQUIRED statement |
| C-17 | **FAIL** | Same as V-02: vocabulary rules in generation-time template placeholder, not in classification table columns. Confirms the C-17 open question: template co-location does NOT satisfy C-17's "co-located with the category assignment row" requirement. |
| C-18 | PASS | Named roles; "Writing an artifact body here is a role violation — you are not yet ROLE 2" |

**Score: 11/12 aspirational → ~91.7**

---

### Composite Rankings

| Rank | Variation | Aspirational | Score | Differentiator |
|------|-----------|-------------|-------|----------------|
| 1 (tie) | **V-01** | 12/12 | **100** | Minimal but complete: identity framing + vocab columns + field-enumerated gates |
| 1 (tie) | **V-03** | 12/12 | **100** | V-01 + inertia framing elevates C-07/C-10 quality above structural compliance |
| 1 (tie) | **V-04** | 12/12 | **100** | V-01 + numbered-condition gates (strongest C-16 of all variations) |
| 4 (tie) | **V-02** | 11/12 | **~91.7** | Template co-location passes C-15/C-07 but fails C-17; confirms template ≠ table-column |
| 4 (tie) | **V-05** | 11/12 | **~91.7** | Full-combination ceiling for C-07/C-10 quality; same C-17 failure as V-02 |

---

### Excellence Signals (from V-01 / V-03 / V-04)

1. **Role-identity as ontological constraint, not procedural step** — "You are the CLASSIFIER. You classify." with explicit wrong-phase output named by role ("the moment you write a coverage summary, you are acting as ROLE 3") makes cross-phase contamination an identity contradiction. V-04 goes furthest by naming both wrong-phase directions in ROLE 1 ("Writing an artifact body…means ROLE 2. Writing a coverage summary…means ROLE 3.").

2. **Inertia framing elevates C-10 quality above vocabulary rules** (V-03) — "The next step should address the specific gap named in the inertia statement for this namespace" forces Recommended Next Steps to be derived from the topic's actual coverage gap, not from category assignment. V-03 produces higher C-10 output quality than V-01 at zero additional criteria cost.

3. **Numbered-condition stop-gates are unambiguous** (V-04) — Writing gate conditions as enumerated numbered lists ("(1) all nine namespaces present; (2) each has Category assigned as…; (3)…") with explicit failure statements ("A table row with an empty Flag cell does not satisfy this gate") removes every ambiguous partial-completion path.

4. **C-17 open question resolved: template co-location ≠ table-column co-location** — V-02 and V-05 confirm that vocabulary rules in the generation-time template placeholder serve C-07/C-15 (depth and register at generation moment) but fail C-17 strictly. Pre-classification vocabulary lookup in the table is a distinct enforcement mechanism from in-template vocabulary delivery.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inertia-grounded next steps: C-10 quality is higher when Recommended Next Step is explicitly derived from the per-namespace inertia gap statement rather than from category assignment alone", "template co-location confirmed non-equivalent to table-column co-location for C-17: vocabulary rules in the generation-time body placeholder enforce C-07/C-15 but do not satisfy C-17 pre-classification lookup requirement"]}
```
