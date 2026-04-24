# scout-size — Quest Score R2

**Rubric**: v2 (12 criteria) | **Variations**: V-01 through V-05

---

## Scoring Method

These are skill-body prompts evaluated for structural guarantee strength — how reliably each prompt forces an output that satisfies each criterion. PASS = mechanism enforces the criterion. PARTIAL = the rule is stated but the mechanism leaves a gap the model can slip through. FAIL = criterion not covered.

---

## V-01 — Confidence Anatomy Split

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | STEP 2 requires individual named integration points and a "Total: N" count; failure condition stated explicitly |
| C-02 | PASS | STEP 3 lists exact vocabulary; names "MODERATE", "3/5", "significant" as failures |
| C-03 | PASS | STEP 1 requires workaround name + exactly `cheaper / comparable / more expensive`; "It depends" and "unclear" explicitly rejected |
| C-04 | PASS | STEP 6 HALF 1 requires confidence level AND named basis ("specific evidence, verified reasoning, or prior work") |
| C-05 | PASS | STEP 7 enumerates four exclusion classes with removal instruction |
| C-06 | PASS | STEP 4 requires specialist types + FTE fractions; "3 engineers" named as failing form |
| C-07 | PASS | STEP 4 requires sprint range; "Q3 2026" and "4 sprints" named as failing forms |
| C-08 | PASS | STEP 3 requires naming "one or two factors most responsible" |
| C-09 | PASS | STEP 5 requires both tier UP and tier DOWN, each a single named condition |
| C-10 | PASS | STEP 6 requires "What would raise it" field explicitly |
| C-11 | PASS | STEP 6 HALF 2 labeled "GAP (what is NOT known)"; "different question from the Basis" instruction; restatement guard present |
| C-12 | **PARTIAL** | STEP 5 requires "one named condition" and gives the offline-sync example — but the template does not include `[LEVEL]`, so the tier consequence may be implied rather than stated. An output saying "if offline sync is required" (no level) passes the prompt but misses C-12's "direct tier consequence stated" requirement. |

**Essential**: 5/5 PASS → 60  
**Recommended**: 3/3 PASS → 30  
**Aspirational**: 3.5/4 (C-12 = 0.5) → 8.75  
**Composite: 98.75** | All essential pass: YES

---

## V-02 — Single-Condition Naming Template

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Section 2 requires individual listed points + "Surface area total: N" |
| C-02 | PASS | Section 3 uses exact vocabulary only |
| C-03 | PASS | Section 1 has three-word constraint; "choose one" enforces vocabulary |
| C-04 | PASS | Section 6 has Confidence + Basis fields |
| C-05 | PASS | SIGNAL BOUNDARY section lists four exclusion classes |
| C-06 | PASS | Section 5 names specialist disciplines + FTE fractions; failure form named |
| C-07 | PASS | Section 5 requires sprint range; "4 sprints" (point estimate) named as failing |
| C-08 | PASS | Section 3 requires primary driver |
| C-09 | PASS | Section 4 requires both tier UP and DOWN directions |
| C-10 | PASS | Section 6 has "What would raise it" field |
| C-11 | PASS | Section 6 has explicit Gap field: "the specific thing NOT yet verified — what limits confidence" — distinct from Basis wording |
| C-12 | PASS | Fill-in-the-blank template `Tier rises to [LEVEL] if [single named condition]` forecloses hedges; four named failing forms listed with reasons; testability criterion stated |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 4/4 → 10  
**Composite: 100** | All essential pass: YES

---

## V-03 — Inertia-as-Anchor

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Table format requires individual rows + bold Total row |
| C-02 | PASS | Section uses exact vocabulary; stated as required |
| C-03 | PASS | Strongest inertia enforcement: structural anchor, mandatory Maintenance cost row, three-word verdict with "It depends / Unclear" explicitly rejected and fallback instruction given |
| C-04 | PASS | CONFIDENCE section requires Level + Basis; "specific, not generic" constraint |
| C-05 | PASS | SIGNAL BOUNDARY section with four-line exclusion list |
| C-06 | PASS | TEAM AND TIMELINE requires specialist disciplines + FTE fractions |
| C-07 | PASS | TEAM AND TIMELINE requires sprint range, not calendar date, not single number |
| C-08 | PASS | COMPLEXITY requires primary driver field |
| C-09 | PASS | Tier sensitivity section uses `Rises to [LEVEL] if: [one named condition]` template for both directions |
| C-10 | PASS | CONFIDENCE requires "What would raise it" field |
| C-11 | PASS | Separate Gap field; "Basis names what IS known. Gap names what IS NOT known. They are different." + restatement guard |
| C-12 | PASS | Template `Rises to [LEVEL] if: [one named condition — one specific scenario]` requires both level AND named condition; "Several factors is not a condition" stated |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 4/4 → 10  
**Composite: 100** | All essential pass: YES

---

## V-04 — Combined (Anatomy Split + Template + Table Base)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | TABLE 1 format; Total row declared required; "specific number" required |
| C-02 | PASS | TABLE 2 Complexity tier row: "Exactly this vocabulary — no other values" |
| C-03 | PASS | INERTIA table is structurally first; three-word Cost direction column with instruction |
| C-04 | PASS | TABLE 3 Confidence level row + Basis row as distinct table entries |
| C-05 | PASS | SIGNAL BOUNDARY section with four exclusion types |
| C-06 | PASS | TABLE 2 Team signal row: "specialist types + FTE fractions"; failure form named in notes |
| C-07 | PASS | TABLE 2 Timeline signal row: "no calendar dates, no point estimate" in Notes |
| C-08 | PASS | TABLE 2 Primary driver row: "Not a list — the main thing" |
| C-09 | PASS | TABLE 2 has Tier UP condition and Tier DOWN condition as required rows |
| C-10 | PASS | TABLE 3 "What would raise it" row required |
| C-11 | PASS | TABLE 3 Basis and Gap are distinct rows; "these are different questions" stated explicitly; "Do not answer both with the same information" |
| C-12 | PASS | TABLE 2 tier rows contain the exact template `Tier rises to [LEVEL] if [single named condition]`; "Several factors fails" stated in both rows |

Plus: 7-item SELF-CHECK covering essential and C-11/C-12 before artifact write.

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 4/4 → 10  
**Composite: 100** | All essential pass: YES

---

## V-05 — Full Integration (all axes + anti-patterns + 12-criterion self-check)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | TABLE with Total row; "Several integration points is not an enumeration" |
| C-02 | PASS | Exact vocabulary listed; "MODERATE/3/5/complex/non-trivial" all named as failing |
| C-03 | PASS | MANDATORY OPENING before all sizing; three-word constraint; fallback instruction; "One of the three words is always defensible" |
| C-04 | PASS | HALF 1 BASIS requires confidence level + "specific evidence, prior work, or reasoning" |
| C-05 | PASS | SIGNAL BOUNDARY CHECK is a dedicated pre-artifact scan step with four items; opening paragraph also states the signal boundary |
| C-06 | PASS | Passing and failing examples shown side by side |
| C-07 | PASS | Passing ("3–5 sprints") and failing ("Q3 2026", "4 sprints") forms shown side by side |
| C-08 | PASS | "Not a list. The main thing." constraint |
| C-09 | PASS | Both tier UP and DOWN required; covered in self-check C-09 item |
| C-10 | PASS | HALF 2 requires "What would raise it" field; self-check C-10 item |
| C-11 | PASS | HALF 2 labeled "GAP (what is NOT known)"; failing form shown (one-sentence blend); passing form shown (split); C-11 in self-check |
| C-12 | PASS | Fill-in-the-blank template; 4-row failing-forms table with named failure reasons; C-12 in self-check; highest enforcement redundancy of any variation |

Plus: 12-criterion self-check covers ALL rubric items; SIGNAL BOUNDARY CHECK is a dedicated scan gate.

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 4/4 → 10  
**Composite: 100** | All essential pass: YES

---

## Ranking

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| 1 | **V-05** | 100 | YES | Highest redundancy per criterion; anti-pattern tables + before/after examples + 12-item self-check |
| 2 | **V-04** | 100 | YES | Table schema enforces completeness structurally; 7-item self-check |
| 3 | **V-02** | 100 | YES | Cleanest C-12 enforcement via 4-row failing-forms table; no self-check |
| 4 | **V-03** | 100 | YES | Strongest C-03 enforcement (structural anchor + maintenance cost row) |
| 5 | V-01 | 98.75 | YES | C-12 PARTIAL — template omits `[LEVEL]`, tier consequence can be implicit |

**V-05** is top by enforcement depth. V-02, V-03, V-04 are co-equal on the rubric; differentiation is mechanism, not score.

---

## Excellence Signals from V-05

**Two new patterns not present in R1:**

**Pattern 1: Failing-forms table for sensitivity** — V-05 adds a 4-row table showing what failing sensitivity output looks like ("Several factors could push this to XL" / "If requirements expand" / "If integration proves complex" / "If the timeline slips") with a why-it-fails column. R1 V-04 used "What SINGLE condition?" question form; R1 V-05 used "Required" annotation. R2 V-05 makes the failure modes visible at generation time, not just after — the model can match its output against the table before writing. This is a fundamentally different enforcement mechanism.

**Pattern 2: Before/after contrast for confidence anatomy** — V-05 shows the failing form ("Confidence: MEDIUM — surface area is clear but the auth layer behavior is unverified" — one sentence blending both) alongside the passing form (Basis and Gap as separate labeled fields). R1 addressed C-11 through field naming alone. Showing the wrong structure concretely reduces the probability of producing it. The contrast doubles as a C-11 anti-pattern and a C-12-adjacent clarity signal on what structural separation means.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Failing-forms table for sensitivity: showing 4 named failing forms with why-they-fail column makes C-12 failure visible at generation time, not just after — the model can match its draft against the table before writing", "Before/after contrast for confidence anatomy: showing the blended failing form (one sentence mixing basis and gap) alongside the split passing form (labeled Basis + Gap fields) makes the C-11 failure mode structurally visible rather than just rule-stated"]}
```
