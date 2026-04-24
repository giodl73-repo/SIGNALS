## trace-contract R9 Scorecard

### Composite Results

| Variation | Essential | Recommended | Aspirational | Total | Essential Pass |
|-----------|-----------|-------------|--------------|-------|----------------|
| V-05 | 60 | 30 | 19 | **109** | YES |
| V-04 | 60 | 30 | 16 | **106** | YES |
| V-01 | 60 | 30 | 13 | **103** | YES |
| V-02 | 60 | 30 | 12 | **102** | YES |
| V-03 | 60 | 30 | 12 | **102** | YES |

**Ranking:** V-05 > V-04 > V-01 > V-02 = V-03

---

### Key Decisions

**C-20 regression in V-05 (the one miss):** R8 V-05 embedded Patterns as a sub-block within Phase 5. R9 V-05 splits the skeleton into S5 (Findings), S6 (Summary), and S7 (Patterns) — Patterns is now a standalone top-level section after Summary. The rubric is explicit: "standalone top-level section outside Phase 5 does not satisfy C-20." One-point structural regression → 109 not 110.

**C-26 isolation (V-01) adds one point vs. R8 V-01:** 102 → 103. Clean additive carry.

**V-02 and V-03 tied:** Both add exactly one new point to their R8 bases (V-02: C-27, V-03: C-28). V-03 doesn't carry C-13 (gate token not upgraded in its R8 base), losing one vs. V-02; but V-02 doesn't carry C-25 (no self-test), also losing one. Net tie at 102.

---

### Excellence Signals

1. **`mechanism-type-shared:` in Patterns branches** — propagates taxonomy into synthesis layer; same-class groupings signal systemic fixes, mixed-class groupings signal coincident symptoms.

2. **Taxonomy distribution line in Summary** — converts per-finding `mechanism-type:` tokens into a document-level class distribution aggregate, enabling cross-session failure-class comparison.

---

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["Taxonomy-aligned Patterns synthesis: mechanism-type-shared field in Singleton and Multi-pattern branch templates propagates mechanism taxonomy into the synthesis layer, enabling automated detection of same-class vs. mixed-class groupings and distinguishing systemic fixes from coincident-symptom groupings", "Taxonomy distribution line in Summary: Mechanism taxonomy distribution aggregate at document close converts per-finding type tokens into a document-level class distribution, enabling cross-session comparison of failure-class prevalence by mechanism type"]}
```
t the system under test — only from reading the deviation line — it is a symptom restatement, not a mechanism." |
| C-06 | PASS | `connector-impact:` on BREAKING and DEGRADED tiers |
| C-07 | PASS | Summary section with severity count table, verdict, and coverage line |
| C-08 | PASS | "If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6." |
| C-09 | PASS | Established; `recommendation:` slot on BREAKING |
| C-10 | PASS | Established; Step 7 Patterns groups findings |
| C-11 | PASS | Established; per-finding block format with labeled fields |
| C-12 | PASS | Established; "Do not run or simulate the operation before writing this token." |
| C-13 | PASS | Carried from R8 V-01; `[EXPECTED-SEALED | clauses:N | date: | author:contract-expert | phase:1-complete]` correctly positioned |
| C-14 | FAIL | Not targeted; COSMETIC tier lacks `connector-impact:` slot |
| C-15 | PASS | Established; `recommendation:` labeled slot on BREAKING |
| C-16 | FAIL | Not targeted; COSMETIC template omits integration-impact field — tier stratification incomplete |
| C-17 | PASS | Established; `rationale:` one-sentence field alongside `recommendation:` on BREAKING |
| C-18 | PASS | Established; `spec: [specific clause from Expected Output — rule number, named constraint, or sub-clause path]` |
| C-19 | PASS | Established (R5+); behavioral protocol block present in R8 V-01 base |
| C-20 | PASS | Established (R5+); Patterns embedded in Phase 5 in R8 V-01 base |
| C-21 | PASS | Established (R6+); named phase-role headings in R8 V-01 base |
| C-22 | FAIL | Not targeted; "without structural overhead" framing confirms no full skeleton pre-declaration |
| C-23 | PASS | Carried from R8 V-01; structured gate manifest with `clauses:N` + identity fields |
| C-24 | FAIL | Not targeted; Step 7 collapses zero/singleton into one condition — three distinct branches absent |
| C-25 | FAIL | Not targeted; self-test rule not embedded in finding template |
| C-26 | PASS | `[FINDINGS-RESOLVED | gate-clauses:{N} | clauses-resolved:{M} | phase:5-complete]` placed immediately after last finding block, before Summary; echoes opening `clauses:N` and adds resolved count; `CLAUSE-GAP` path for divergence |
| C-27 | FAIL | Not targeted; Step 7 has procedural instructions only, no pre-printed structural slots per branch |
| C-28 | FAIL | Not targeted; no mechanism taxonomy type token field |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 13/20
**Total: 103/110**

---

#### V-02 — C-27 isolation (branch-conditional Patterns template slots)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Role assignment and boundary statement present |
| C-02 | PASS | Coverage obligation explicit |
| C-03 | PASS | One-finding-per-deviation enforced via three tier templates |
| C-04 | PASS | Spec-anchored expected output; invalid-without-citation declared |
| C-05 | PASS | Hypothesis rule present with self-test question |
| C-06 | PASS | `connector-impact:` on BREAKING and DEGRADED |
| C-07 | PASS | Summary section with verdict and counts |
| C-08 | PASS | Zero-finding affirmation present |
| C-09 | PASS | Established |
| C-10 | PASS | Established |
| C-11 | PASS | Established |
| C-12 | PASS | Established; "Do not proceed to Step 3 before writing this line." |
| C-13 | FAIL | Not reworked; `[CONTRACT COMMITTED]` is a bracket label only, no clause count or identity fields |
| C-14 | FAIL | Not targeted; COSMETIC lacks `connector-impact:` |
| C-15 | PASS | Established |
| C-16 | FAIL | Not targeted |
| C-17 | PASS | Established |
| C-18 | PASS | Established |
| C-19 | PASS | Established |
| C-20 | PASS | Established |
| C-21 | PASS | Established |
| C-22 | FAIL | Not targeted |
| C-23 | FAIL | `[CONTRACT COMMITTED]` lacks `clauses:N` and identity fields — binary label, not manifest |
| C-24 | PASS | Carried from R8 V-02; three named branch templates with per-branch instructions (Zero/Singleton/Multi-pattern) |
| C-25 | FAIL | Not targeted |
| C-26 | FAIL | Not targeted; no post-findings closure token |
| C-27 | PASS | Zero branch: `no-pattern-confirmation:` slot with fill requirement; Singleton branch: `single-finding-ref:`, `root-cause:`, `attribution:`, `single-fix:` labeled slots; Multi branch: `pattern-N: root-cause: findings:[] single-fix:` + `patterns-summary:` — structural slots enforce field completion at write time |
| C-28 | FAIL | Not targeted |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 12/20
**Total: 102/110**

---

#### V-03 — C-28 isolation (mechanism taxonomy constraint)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Role assignment and boundary statement present |
| C-02 | PASS | Coverage obligation explicit |
| C-03 | PASS | Three tier templates; one finding per deviation |
| C-04 | PASS | Spec citation requirement; invalid-without-citation declared |
| C-05 | PASS | Symptom-restatement disqualifier present |
| C-06 | PASS | `connector-impact:` on BREAKING and DEGRADED |
| C-07 | PASS | Summary section with verdict |
| C-08 | PASS | Zero-finding skip instruction |
| C-09 | PASS | Established |
| C-10 | PASS | Established |
| C-11 | PASS | Established |
| C-12 | PASS | Established |
| C-13 | FAIL | `[CONTRACT COMMITTED]` only; not reworked |
| C-14 | FAIL | Not targeted; COSMETIC lacks `connector-impact:` |
| C-15 | PASS | Established |
| C-16 | FAIL | Not targeted |
| C-17 | PASS | Established |
| C-18 | PASS | Established |
| C-19 | PASS | Established; taxonomy declaration is domain vocabulary, not behavioral protocol rules — however behavioral protocol carries from R8 V-03 base |
| C-20 | PASS | Established |
| C-21 | PASS | Established |
| C-22 | FAIL | Not targeted |
| C-23 | FAIL | Not targeted |
| C-24 | FAIL | Not targeted; Step 7 collapses zero/singleton without three distinct branches |
| C-25 | PASS | Carried from R8 V-03; four-step hypothesis protocol: `hypothesis-draft:` → `self-test:` (necessary-information binary) → `mechanism-type:` → `mechanism:`; YES gate blocks progression |
| C-26 | FAIL | Not targeted |
| C-27 | FAIL | Not targeted; Step 7 uses procedural instructions only |
| C-28 | PASS | Pre-Phase-1 taxonomy table with five named type tokens; `mechanism-type:` required field on all three severity tiers; `TAXONOMY-GAP` escape path with explanation requirement; taxonomy declared once, not redeclared per finding |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 12/20
**Total: 102/110**

---

#### V-04 — C-26 x C-27 (post-findings closure token + branch template slots, skeleton combination)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "### Phase 1 -- Connectors Contract Expert: Expected Output" heading + role statement: "You are the Connectors contract expert. You have not run the operation. You write from the spec alone." |
| C-02 | PASS | "Every element must appear. Missing elements fail C-02." |
| C-03 | PASS | Three severity-tier templates in skeleton; "For each deviation, select the matching tier template" |
| C-04 | PASS | "An element without a spec citation is not a valid contract entry." |
| C-05 | PASS | "The hypothesis names the causal mechanism — not a restatement of the deviation." |
| C-06 | PASS | BREAKING and DEGRADED carry `connector-impact:` |
| C-07 | PASS | S6 Summary with severity counts, verdict, and coverage line |
| C-08 | PASS | Zero-finding path: replace S5 with "Findings — none. Contract satisfied." |
| C-09 | PASS | Established |
| C-10 | PASS | Established |
| C-11 | PASS | Established |
| C-12 | PASS | Established; skeleton structure enforces gate before execution |
| C-13 | PASS | Carried from R8 V-04; skeleton pre-declares `[EXPECTED-SEALED | clauses:N | ...]` token format |
| C-14 | FAIL | Not targeted; COSMETIC template has only three fields (deviation, spec, hypothesis) — no `connector-impact:` |
| C-15 | PASS | Established; `recommendation:` slot in BREAKING template |
| C-16 | FAIL | Not targeted; COSMETIC template stripped relative to BREAKING/DEGRADED |
| C-17 | PASS | Established; `rationale:` alongside `recommendation:` on BREAKING |
| C-18 | PASS | Established; `spec: [specific clause from S2 — rule number, named constraint, or sub-clause path]` |
| C-19 | PASS | 6-rule Behavioral Protocol before Phase 1: skeleton immutability, phase-separation, role-boundary, coverage obligation, gate manifest invariant, Patterns non-omission |
| C-20 | FAIL | S7 Patterns is a standalone section after S6 Summary; C-20 requires Patterns embedded within the Phase 5/Summary template — standalone top-level section does not satisfy |
| C-21 | PASS | "### Phase 1 -- Connectors Contract Expert: Expected Output" and "### Phase 2 -- Automate: Execute, Diff, and Findings" both carry phase number + role name |
| C-22 | PASS | Carried from R8 V-04; complete artifact skeleton (S1–S7) with all section headers, template slots, finding templates, and both gate tokens pre-declared before Phase 1 |
| C-23 | PASS | `[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]` with clause count and identity fields |
| C-24 | PASS | Three branch templates in S7 skeleton: ZERO (with apply-when condition), SINGLETON (with `single-finding-ref:`, `root-cause:`, `attribution:`, `single-fix:`), MULTI-PATTERN (with `pattern-N:` block + `patterns-summary:`) |
| C-25 | FAIL | Not targeted; no self-test decision procedure or hypothesis-draft/mechanism split |
| C-26 | PASS | `[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]` pre-declared in skeleton immediately after finding templates; Phase 2 instructions specify exact fill protocol including CLAUSE-GAP path |
| C-27 | PASS | All three Patterns branches carry pre-printed labeled slots: zero has `no-pattern-confirmation:` (with fill enforcement statement), singleton has `single-finding-ref:` + `root-cause:` + `attribution:` + `single-fix:`, multi has `pattern-N: root-cause: findings:[] single-fix:` + `patterns-summary:` |
| C-28 | FAIL | Not targeted; no mechanism taxonomy type token |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 16/20
**Total: 106/110**

---

#### V-05 — Full R9 ceiling (C-26 x C-27 x C-28 + R8 platinum base)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "### Phase 1 -- Connectors Contract Expert: Expected Output" + "You are the Connectors contract expert. You have not run the operation. You have not observed implementation output. You write from the spec alone. Your role ends when the gate token is placed." |
| C-02 | PASS | "Every element must appear. Missing elements fail C-02 regardless of finding quality." |
| C-03 | PASS | Three tier templates; "For each deviation from S4, select the matching severity tier template from the skeleton and fill all fields." |
| C-04 | PASS | "An expected element without a spec citation is not a valid contract entry. If a surface is not defined in the spec, write: `[surface]: not specified in spec`." |
| C-05 | PASS | "The hypothesis names a causal mechanism. It does not restate the deviation." in hypothesis self-test preamble |
| C-06 | PASS | `connector-impact:` on all three tiers (COSMETIC explicitly: "field always present") |
| C-07 | PASS | S6 Summary with severity counts, verdict, recommendations, coverage line, and taxonomy distribution |
| C-08 | PASS | Zero-finding path: "replace S5 with `## 5. Findings -- none. Contract satisfied.`"; all-zero S6 counts; Zero branch template in S7 |
| C-09 | PASS | `recommendation:` labeled slot on BREAKING and DEGRADED; `rationale:` on BREAKING |
| C-10 | PASS | S7 Patterns groups findings by root cause |
| C-11 | PASS | Three severity-tier block templates with labeled fields; absent field produces visible gap |
| C-12 | PASS | Phase-separation invariant (rule 2) and skeleton gate token position enforce "do not execute before gate" |
| C-13 | PASS | `[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]` — distinct bracket token correctly positioned |
| C-14 | PASS | COSMETIC template includes `connector-impact:` with "write 'none' if not applicable; field always present" — unconditional across all three tiers |
| C-15 | PASS | `recommendation: [amend-spec | fix-impl | needs-discussion]` as labeled slot on BREAKING; vocabulary-constrained |
| C-16 | PASS | Three distinct templates with explicit unconditional field counts: BREAKING (9 fields), DEGRADED (8 fields), COSMETIC (7 fields) — no conditional field language |
| C-17 | PASS | BREAKING: `recommendation:` (vocabulary choice) + `rationale:` (one sentence grounded in mechanism); both required |
| C-18 | PASS | `spec: [specific clause from S2 — rule number, named constraint, or sub-clause path; not a section heading alone]` — clause-precise anchor on all three tiers |
| C-19 | PASS | 10-rule Behavioral Protocol before Phase 1: skeleton immutability, phase-separation, role-boundary, coverage obligation, gate manifest invariant, tier-stratified template invariant, self-test invariant, taxonomy invariant, post-findings closure invariant, Patterns non-omission |
| C-20 | FAIL | S7 Patterns is a standalone top-level section (## 7) positioned after S6 Summary (## 6) — structural separation regresses from R8 V-05 where Patterns was embedded within Phase 5; rubric pass condition: "standalone top-level section outside Phase 5 does not satisfy C-20" |
| C-21 | PASS | "### Phase 1 -- Connectors Contract Expert: Expected Output" and "### Phase 2 -- Automate: Execute, Diff, Findings, and Closure" — both carry phase number + role name |
| C-22 | PASS | Complete artifact skeleton (S1–S7) pre-declared before Phase 1 with all section headers, three severity-tier finding templates (with self-test + taxonomy), both gate tokens, and all three Patterns branch templates |
| C-23 | PASS | `[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]` — clause count + date + author + phase fields |
| C-24 | PASS | Three Patterns branches in skeleton with per-branch conditions; zero/singleton/multi-pattern with apply-when selectors |
| C-25 | PASS | Four-field hypothesis protocol: `hypothesis-draft:` → `self-test: [YES — rewrite; NO — proceed]` → `mechanism-type:` → `mechanism:` — YES answer is a structural blocking condition |
| C-26 | PASS | `[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]` pre-declared in skeleton immediately after last finding template; echoes opening clause count + adds resolved count; CLAUSE-GAP path specified for divergence |
| C-27 | PASS | Zero branch: `no-pattern-confirmation:` slot; Singleton branch: `single-finding-ref:` + `root-cause:` + `mechanism-type-shared:` + `attribution:` per finding + `single-fix:`; Multi branch: `pattern-N: root-cause: mechanism-type-shared: findings: single-fix:` + `patterns-summary:` — pre-printed slots enforce field completion across all three cardinality cases |
| C-28 | PASS | Five-token taxonomy table (field-mapping / serialization-path / conditional-branch / lifecycle-event / schema-contract) declared Pre-Phase-1; `mechanism-type:` required field on all three severity tiers in skeleton; TAXONOMY-GAP escape path; taxonomy distribution line in S6 Summary |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 19/20
**Total: 109/110**

---

### Composite Summary

| Variation | Essential | Recommended | Aspirational | **Total** | Essential Pass |
|-----------|-----------|-------------|--------------|-----------|----------------|
| V-05 | 60 | 30 | 19 | **109** | YES |
| V-04 | 60 | 30 | 16 | **106** | YES |
| V-01 | 60 | 30 | 13 | **103** | YES |
| V-02 | 60 | 30 | 12 | **102** | YES |
| V-03 | 60 | 30 | 12 | **102** | YES |

**Ranking:** V-05 > V-04 > V-01 > V-02 = V-03

---

### Excellence Signals from V-05

**1. Taxonomy-aligned synthesis: `mechanism-type-shared:` in Patterns branch templates.**
C-27 requires pre-printed structural slots per Patterns branch. V-05 extends those slots with a
`mechanism-type-shared:` field in both the Singleton and Multi-pattern branches. When findings
are grouped, the analyst must declare whether the grouped findings share a mechanism-type token
or have mixed types. This propagates the finding-level taxonomy vocabulary into the synthesis
layer — cross-group mechanism class identification becomes a structural obligation, not an
optional annotation. A single-class grouping signals a systemic fix; a mixed-class grouping
signals independent mechanisms that happen to share a surface symptom.

**2. Taxonomy distribution line in Summary converts per-finding tokens into aggregate signal.**
V-05's Summary carries `Mechanism taxonomy distribution: field-mapping:{N} | serialization-path:{N}
| conditional-branch:{N} | lifecycle-event:{N} | schema-contract:{N} | TAXONOMY-GAP:{N}`. This
converts per-finding `mechanism-type:` tokens from individual annotations into a document-level
class distribution. Two findings of `field-mapping` class in one trace vs. one `field-mapping`
and one `serialization-path` carry different systemic implications — the aggregate line makes
this visible at close time without re-reading individual findings.

**3. Post-findings closure invariant as behavioral protocol rule (rule 9).**
C-26 adds the `[FINDINGS-RESOLVED]` token. V-05 goes further: it declares the post-findings
closure as a named invariant in the 10-rule behavioral protocol — the obligation is visible at
document open, not only when the analyst reaches S5. Pairing a new structural mechanism with
a corresponding behavioral protocol rule converts a template slot into a session-level commitment,
making the mechanism harder to bypass under write-time cognitive pressure.

**4. V-05 = V-04 + self-test + taxonomy + connector-impact on all tiers.**
V-04 reaches 106 by combining skeleton pre-declaration of C-26 and C-27. V-05's three
additional points come from C-25 (self-test procedure), C-28 (taxonomy constraint), and
C-14 (unconditional connector-impact including COSMETIC). The C-14 fix is the simplest: adding
`connector-impact: [... write "none" if not applicable; field always present]` to the COSMETIC
template converts a conditional integration-impact obligation into an unconditional structural
field. The "write 'none' if not applicable" escape valve is what makes the unconditional
requirement cost-free on cosmetic findings while enforcing the field's presence.

---

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["Taxonomy-aligned Patterns synthesis: mechanism-type-shared field in Singleton and Multi-pattern branch templates propagates mechanism taxonomy into the synthesis layer, enabling automated detection of same-class vs. mixed-class groupings and distinguishing systemic fixes from coincident-symptom groupings", "Taxonomy distribution line in Summary: Mechanism taxonomy distribution aggregate at document close converts per-finding type tokens into a document-level class distribution, enabling cross-session comparison of failure-class prevalence by mechanism type"]}
```
