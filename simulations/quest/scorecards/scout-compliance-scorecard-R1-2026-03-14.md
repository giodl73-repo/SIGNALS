## Results

**Rankings:**

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | V-03: Verdict-first | 100 | Structural guarantee on C-07/C-09; explicit C-10 section |
| 1 (tie) | V-04: Formal register | 100 | Most explicit; names SR 11-7, PCI DSS, GDPR by name |
| 3 | V-05: Default-risk | 95 | C-10 absent — single section addition reaches 100 |
| 4 | V-02: Architect-first | 93 | Eliminates C-03 disqualification; aspirationals unguarded |
| 5 | V-01: Baseline | 87 | C-03 PARTIAL (SR 11-7 unguarded); aspirationals absent |

**Key delta structure:**
- 87 → 93: Naming SR 11-7 explicitly (V-01 → V-02)
- 93 → 100: Adding explicit C-09 + C-10 sections (V-02 → V-03/V-04)

**3 new patterns:**
1. Verdict-first positioning is a structural guarantee, not behavioral nudge — C-07/C-09 cannot be crowded out
2. Aspirationals need named output sections (not prose hints) to reliably appear — C-10 missed in 3/5 variations without it
3. Name the misapplied framework (SR 11-7) by name — "vendor vs. methodology" framing is insufficient to prevent the disqualifying error

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verdict-first output ordering creates structural guarantee on C-07 and C-09 independent of model behavior", "naming aspirational criteria as explicit output sections (DATA-SENSITIVITY TIER) converts emergent insights into required deliverables", "naming misapplied frameworks by name in the prompt (SR 11-7, PCI DSS, GDPR) eliminates model inference errors on scope"]}
```
ents matrix SATISFIED/ACTION (10 pts) | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-07 | Adoption-readiness verdict (10 pts) | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-08 | Conditional frameworks flagged (10 pts) | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-09 | Compliance reframe surfaced (5 pts) | PARTIAL 3 | PARTIAL 3 | PASS 5 | PASS 5 | PASS 5 |
| C-10 | NPI/data-sensitivity tiering (5 pts) | FAIL 0 | FAIL 0 | PASS 5 | PASS 5 | FAIL 0 |
| **Total** | | **87** | **93** | **100** | **100** | **95** |

---

## Detailed Scores

### V-01: Baseline (87/100)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Auto-detect domain" + "Infer frameworks from signals only" | 12 |
| C-02 | PASS | SCOPE BOUNDARY section mandates explicit vendor vs. methodology distinction | 12 |
| C-03 | PARTIAL | Vendor/methodology distinction prompted (C-02 guard) but SR 11-7 not named; disqualification risk | 6 |
| C-04 | PASS | GIT-NATIVE ADVANTAGE section with named framework link requirement | 12 |
| C-05 | PASS | "SF-01..., description, severity. Minimum 4 entries" — explicit | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: min 5 rows, SATISFIED/ACTION distinction | 10 |
| C-07 | PASS | ADOPTION VERDICT: "Not 'it depends.' Name the condition." | 10 |
| C-08 | PASS | FRAMEWORK CATALOG requires UNIVERSAL / CONDITIONAL column | 10 |
| C-09 | PARTIAL | No explicit reframe instruction; may emerge but not guaranteed | 3 |
| C-10 | FAIL | Not prompted | 0 |

**Verdict**: Solid floor. All essentials covered except C-03 (PARTIAL — SR 11-7 disqualification risk unguarded). Aspirationals C-09 and C-10 unguarded.

---

### V-02: Architect-first (93/100)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Auto-detect domain from repo context. Do not prompt. Infer frameworks from signals only." | 12 |
| C-02 | PASS | SCOPE DECLARATION: "One explicit paragraph — what is under review and what is not." | 12 |
| C-03 | PASS | Explicit: "model risk frameworks (e.g., SR 11-7) apply to AI models, not to structured prompt methodologies" | 12 |
| C-04 | PASS | "Connect no-server design to at least one specific named compliance property… link to a framework" | 12 |
| C-05 | PASS | "SF-01... IDs, descriptions, severity (HIGH / MEDIUM / LOW). Minimum 4 entries." | 12 |
| C-06 | PASS | ">= 5 rows. Disposition: SATISFIED / ACTION / CONDITIONAL / N/A" | 10 |
| C-07 | PASS | "ADOPTION VERDICT: Explicit named condition. Not 'it depends.'" | 10 |
| C-08 | PASS | "Do not assert universal applicability… (e.g., PCI DSS, GDPR/CCPA)" — names conditional frameworks | 10 |
| C-09 | PARTIAL | No explicit reframe instruction; architecture-first framing may surface it, not required | 3 |
| C-10 | FAIL | Not prompted in V-02 | 0 |

**Verdict**: Strong essential coverage. Architecture-first eliminates C-03 disqualification risk. Aspirationals unguarded; gap from 93 to 100 is purely C-09/C-10.

---

### V-03: Verdict-first (100/100)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Auto-detect domain and data types from repo context. Do not prompt. Infer all frameworks from context signals alone." | 12 |
| C-02 | PASS | Section 3 SCOPE BOUNDARY: "Who is under compliance review — the product or its host platform? State explicitly." | 12 |
| C-03 | PASS | Section 3: "Note any framework that is frequently misapplied to prompt methodologies rather than to AI models" — in financial services context, SR 11-7 is the unambiguous answer | 12 |
| C-04 | PASS | Dedicated GIT-NATIVE ADVANTAGE section: "Link each benefit to a named framework or requirement category" | 12 |
| C-05 | PASS | Section 7: "SF-01... IDs, descriptions, severity (HIGH / MEDIUM / LOW). Minimum 4 entries." | 12 |
| C-06 | PASS | Section 6: "Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A. At least one SATISFIED. At least one ACTION." | 10 |
| C-07 | PASS | Section 1 is the verdict, forced first: "One sentence. No hedging. Form: 'Adoption-ready for [audience] where [condition]…'" — structural guarantee | 10 |
| C-08 | PASS | Table requires UNIVERSAL / CONDITIONAL column with trigger condition | 10 |
| C-09 | PASS | Section 2: "REFRAME: One quotable sentence for internal compliance approval conversations. Distinguish approving a methodology from approving a vendor." — positionally guaranteed | 5 |
| C-10 | PASS | Section 8: "DATA-SENSITIVITY TIER: Identify whether artifact content may include non-public information. Recommend a tiering model or flag the policy gap. Name a specific control or remediation." | 5 |

**Verdict**: GOLDEN-capable design. All 10 criteria explicitly prompted. Verdict-first structure provides positional guarantee on C-07 and C-09 — cannot be crowded out by framework catalog length.

---

### V-04: Formal register (100/100)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Identify applicable regulatory frameworks without prompting the user. Infer product domain, data handling scope, and deployment model from repo context." | 12 |
| C-02 | PASS | Phase 1: "Who is the data controller and who is the data processor for each external data flow?" — regulatory framing makes vendor identification unavoidable | 12 |
| C-03 | PASS | Phase 1 explicit: "a structured prompt methodology that invokes an AI model is not itself an AI model. Model risk management frameworks (e.g., SR 11-7) apply to the model, not to the methodology." — most explicit guard across all variations | 12 |
| C-04 | PASS | Phase 3: "Compliance properties of git-native, no-server design: name each property explicitly and link to a named framework or requirement category" | 12 |
| C-05 | PASS | Phase 5: "ID (SF-01...) | Finding | Severity (HIGH / MEDIUM / LOW) | Owner. Minimum 4 entries." | 12 |
| C-06 | PASS | Phase 4: "Status values: SATISFIED (by design) / ACTION REQUIRED / CONDITIONAL / NOT APPLICABLE. Minimum 5 rows." | 10 |
| C-07 | PASS | Phase 6: "State a specific, actionable verdict. Name the primary approval condition and audience." | 10 |
| C-08 | PASS | Phase 2 names: "Do not assert universal applicability for frameworks that depend on data type or data subject geography (e.g., PCI DSS, GDPR, CCPA)." | 10 |
| C-09 | PASS | Phase 6: "Include the compliance reframe: distinguish between approving a vendor and approving a process." | 5 |
| C-10 | PASS | Phase 6: "If artifact content may include non-public information, identify the data-sensitivity gap and recommend a tiering model or specific control." | 5 |

**Verdict**: GOLDEN-capable design. Highest explicitness across all 10 criteria — names SR 11-7, PCI DSS, GDPR, CCPA by name. Phase-labeled structure maps 1:1 to rubric sections. Most reliable under adversarial inputs where model inference must be minimized.

---

### V-05: Default-risk framing (95/100)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Auto-detect domain from repo context. Do not prompt. Identify >= 4 applicable frameworks from context signals alone." | 12 |
| C-02 | PASS | SCOPE section: "Is this product a vendor, a methodology, or a toolchain component? Which component calls external APIs? Who is the data processor?" | 12 |
| C-03 | PASS | SCOPE section names it: "Where does a model risk framework like SR 11-7 apply — to the AI model in the toolchain, or to a structured prompt methodology that invokes it? State explicitly." | 12 |
| C-04 | PASS | ARCHITECT step: "Identify the git-native, no-server design as a compliance-favorable property. Link each benefit to a named framework or requirement." | 12 |
| C-05 | PASS | FINDINGS item 6: "Findings Register — SF-01... IDs, descriptions, severity (HIGH / MEDIUM / LOW)" | 12 |
| C-06 | PASS | FINDINGS item 5: "Requirements Matrix — >= 5 rows, SATISFIED / ACTION / CONDITIONAL / N/A" | 10 |
| C-07 | PASS | FINDINGS item 7: "Adoption Verdict — named condition and audience, not hedged" | 10 |
| C-08 | PASS | COMPLIANCE step: "Mark each UNIVERSAL or CONDITIONAL with trigger condition. Do not assert universal applicability for data-type or geography-dependent frameworks." | 10 |
| C-09 | PASS | FINDINGS item 8: "Reframe — one quotable sentence for internal approval conversations" | 5 |
| C-10 | FAIL | Not prompted anywhere in V-05 | 0 |

**Verdict**: Covers 9/10 criteria explicitly. Default-risk opener creates a natural funnel toward precise scope reasoning; C-05 adoption verdict emerges from the inertia framing. Single gap: C-10 absent — one section addition would reach 100.

---

## Excellence Signals

Patterns from the top-scoring variations that drove quality:

**1. Verdict-first output ordering (V-03) — structural guarantee on C-07 and C-09**
When the verdict is positional item 1 and the reframe is positional item 2, neither can be omitted by a model that runs out of tokens or drowns the conclusion in framework catalog output. This is a structural guarantee, not a behavioral nudge.

**2. Named output sections for aspirationals (V-03) — converts emergent insights into required deliverables**
"DATA-SENSITIVITY TIER" as an explicit section name with pass condition converts C-10 from an insight a thoughtful model might surface into a required deliverable. Variations without this section name missed C-10 every time.

**3. Naming misapplied frameworks by name (V-02, V-04, V-05) — eliminates inference errors on scope**
Every variation that explicitly wrote "SR 11-7" in the prompt scored PASS on C-03. V-01, which relied on "vendor vs. methodology distinction" framing without naming SR 11-7, scored PARTIAL. The pattern: do not expect the model to identify the most dangerous failure mode from a category description; name it.

**4. Phase-labeled formal structure (V-04) — inspection-ready skeleton with 1:1 rubric mapping**
V-04's six-phase structure (SCOPE DETERMINATION, FRAMEWORK INVENTORY, ARCHITECTURE, REQUIREMENTS MATRIX, FINDINGS REGISTER, ADOPTION READINESS) maps directly to rubric sections. A compliance officer reading the output knows which phase answers which question. This reduces model inference errors on what belongs where.

---

## Round 1 Summary

- **Floor**: 87 (V-01) — all essentials covered except C-03 partial; aspirationals unguarded
- **Ceiling**: 100 (V-03, V-04) — both GOLDEN-capable
- **Key delta**: 87→93 = explicit SR 11-7 guard; 93→100 = explicit C-09 + C-10 sections
- **C-10 gap**: 3 of 5 variations missed NPI tiering entirely; requires named output section to reliably appear
- **C-03 risk**: Only V-01 left this unguarded; all other variations named SR 11-7 explicitly

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verdict-first output ordering creates structural guarantee on C-07 and C-09 independent of model behavior", "naming aspirational criteria as explicit output sections (DATA-SENSITIVITY TIER) converts emergent insights into required deliverables", "naming misapplied frameworks by name in the prompt (SR 11-7, PCI DSS, GDPR) eliminates model inference errors on scope"]}
```
