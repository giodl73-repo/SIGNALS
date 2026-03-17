## Scoring — org-build R2 (Rubric v2)

---

### V-01 — Inertia Framing

| ID | PASS/PARTIAL/FAIL | Evidence |
|----|-------------------|----------|
| C-01 | PASS | Turn 5 Section 1: "minimum two levels. Committees as distinct labeled nodes." |
| C-02 | PASS | Turn 4: "Every role file MUST contain all five fields: orientation, lens, expertise, scope, collaborates_with" |
| C-03 | PASS | Turn 3: "INERTIA-ADVOCATE ROLE (always required): MUST appear in ROLES-LOADED or ROLES-NOTE." |
| C-04 | PASS | "Standard depth: 20-30 role files. If below lower bound, add missing roles." |
| C-05 | PASS | "Decides and Escalates are ALWAYS separate columns. Do not merge into 'Decision Scope.'" |
| C-06 | PASS | "Role files MUST be grouped under area subdirectories. Minimum 2 area subdirectories." |
| C-07 | PASS | Section 3: "Minimum three distinct rows." Section 4: "Quorum uses full fraction format." |
| C-08 | PASS | Turn 1 Sub-section 4: FLAT-CASE-PRESSURE with closed-set rating; VERDICT with single-verdict guard. |
| C-09 | PASS | Section 6: "Row 2: workload signal, structural symptom, or milestone event (not another headcount)" |
| C-10 | PASS | "ANTI-PATTERN WATCH MUST CONSTRAINT: Each cell MUST open with typed citation syntax. MUST: do not write a cell without the (cat-N) typed syntax." Imperative MUST present. |
| C-11 | PASS | Turn 2 provides 5 rating-keyed templates; Turn 4: "MUST use the exact text from IA-SCOPE-TEMPLATE-APPLIED. The scope field is derived, not composed." |
| C-12 | PASS | Turn 5 ANTI-PATTERN CATEGORY DERIVATION: IF CAN-OPERATE-FLAT → cat-3/cat-2; IF STRUCTURE-WARRANTED → cat-1/cat-4. Explicitly before diagram. |
| C-13 | PASS | "Only one verdict. Both is an error. Neither is an error." Exact error framing. |

**essential=5/5, recommended=3/3, aspirational=5/5 → composite = 100**

---

### V-02 — Phrasing Register

| ID | PASS/PARTIAL/FAIL | Evidence |
|----|-------------------|----------|
| C-01 | PASS | "MUST draw... MUST show minimum two hierarchy levels. FORBIDDEN: flat list of names." |
| C-02 | PASS | "FORBIDDEN: writing any role file without all five fields present." |
| C-03 | PASS | "INERTIA-ADVOCATE: REQUIRED. If absent, MUST add it." |
| C-04 | PASS | "Standard depth: MUST produce 20-30 role files. FORBIDDEN: producing fewer files than lower bound." |
| C-05 | PASS | "MUST use columns: Area | Headcount | Key Roles | Decides | Escalates. FORBIDDEN: merging Decides and Escalates." |
| C-06 | PASS | "MUST group role files under area subdirectories. REQUIRED: minimum 2 area subdirectories." |
| C-07 | PASS | "MUST include minimum three distinct rows." "MUST use full fraction format. FORBIDDEN: short form." |
| C-08 | PASS | Phase 1: FLAT-CASE-PRESSURE line MUST be first sentence; verdict guard present. |
| C-09 | PASS | "FORBIDDEN: two rows both typed as headcount threshold." |
| C-10 | PASS | "MUST open each 'Why It Applies Here' cell with: [element name] (cat-N). FORBIDDEN: writing any cell without the (cat-N) typed syntax. FORBIDDEN: descriptive format guidance in Mitigation cells." Strongest MUST/FORBIDDEN coverage. |
| C-11 | PASS | Phase 2: 5 templates; "FORBIDDEN: writing the inertia-advocate scope field with any text other than the template." |
| C-12 | PASS | Phase 5: IF CAN-OPERATE-FLAT → MUST set cat-3/cat-2, FORBIDDEN cat-1/cat-4; IF STRUCTURE-WARRANTED → MUST set cat-1/cat-4, FORBIDDEN cat-2/cat-3. |
| C-13 | PASS | "Only one verdict. Both is an error. Neither is an error. FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts." |

**essential=5/5, recommended=3/3, aspirational=5/5 → composite = 100**

---

### V-03 — Lifecycle Emphasis

| ID | PASS/PARTIAL/FAIL | Evidence |
|----|-------------------|----------|
| C-01 | PASS | Section 1: "ASCII Org Diagram: minimum two levels, committees as distinct nodes." |
| C-02 | PASS | Phase 3: "Five fields required in every file: orientation, lens, expertise, scope, collaborates_with." |
| C-03 | PASS | Phase 3: "INERTIA-ADVOCATE: Must appear in ROLES-LOADED or ROLES-NOTE. Add if absent." |
| C-04 | PASS | Phase 3: "Role count: Standard 20-30 files." Gate output records ROLE-FILE-COUNT. |
| C-05 | PASS | Section 2: "Separate Decides and Escalates columns required." |
| C-06 | PASS | "Group under area subdirectories: .craft/roles/{area}/{role}.md (minimum 2 subdirs)." |
| C-07 | PASS | Section 3: 3+ distinct rows. Section 4: "Quorum [N of M member roles required]." |
| C-08 | PASS | Phase 1: FLAT-CASE-PRESSURE with rating and verdict. "Only one verdict. Both is an error." Recorded in PHASE 1 GATE output. |
| C-09 | PASS | Section 6: "Row 1: headcount threshold. Row 2: workload signal, symptom, or milestone." |
| C-10 | PASS | Section 7: "Each 'Why It Applies Here' cell MUST open with: [element name] (cat-N). Any cell that names an element without (cat-N) typed syntax fails this binding." MUST imperative present. |
| C-11 | PASS | Phase 2 explicitly named "IA SCOPE TEMPLATE SELECTION" with input contract consuming FLAT-CASE-PRESSURE; Phase 3: "scope is not composed at this phase — it is read from Phase 2 output." |
| C-12 | PASS | Phase 4 "ANTI-PATTERN CATEGORY DERIVATION: Input contract: consumes VERDICT from Phase 1 gate." Explicit structural derivation with reasoning for each verdict path. |
| C-13 | PASS | "Only one verdict. Both is an error. Neither is an error." |

**essential=5/5, recommended=3/3, aspirational=5/5 → composite = 100**

---

### V-04 — Inertia Framing + Lifecycle Emphasis

| ID | PASS/PARTIAL/FAIL | Evidence |
|----|-------------------|----------|
| C-01 | PASS | Step 4b: "ASCII Org Diagram (two levels minimum, committees as distinct nodes)" |
| C-02 | PASS | Turn 4: "Required fields: orientation, lens, expertise, scope, collaborates_with" |
| C-03 | PASS | Turn 4: "Inertia-advocate MUST be present. If absent, add." |
| C-04 | PASS | "Standard: 20-30 files. Deep: 50+ files." |
| C-05 | PASS | "columns: Area | Headcount | Key Roles | Decides | Escalates. Decides and Escalates always separate." |
| C-06 | PASS | "Min 2 area subdirs." |
| C-07 | PASS | Section 3: "(ROB + shiproom/gate + governance, minimum 3 rows)." Section 4: "Quorum [N of M member roles required]." |
| C-08 | PASS | Turn 1: FLAT-CASE-PRESSURE, verdict with "Only one verdict. Both is an error." T1 output record. |
| C-09 | PASS | Section 6: "Row 1: headcount threshold. Row 2: workload signal, symptom, or milestone." |
| C-10 | PASS | Step 4b: "DERIVATION BINDING: Each 'Why It Applies Here' MUST open with: [element name] (cat-N). Only cat codes in T3-CATEGORIES-SET are valid." MUST imperative present. |
| C-11 | PASS | Turn 2: template table keyed on T1-PRESSURE; "The inertia-advocate scope field in the role file is T2-IA-SCOPE. Not paraphrased. Not adapted. The template text, verbatim." |
| C-12 | PASS | Turn 3: "T1-VERDICT drives anti-pattern category selection. This derivation must happen before the Anti-Pattern Watch table is written." Typed T3-CATEGORIES-SET output. |
| C-13 | PASS | "Only one verdict. Both is an error. Neither is an error." |

**essential=5/5, recommended=3/3, aspirational=5/5 → composite = 100**

---

### V-05 — Phrasing Register + Role Sequence

| ID | PASS/PARTIAL/FAIL | Evidence |
|----|-------------------|----------|
| C-01 | PASS | "MUST show minimum two hierarchy levels. FORBIDDEN: flat name list without visual hierarchy." |
| C-02 | PASS | Step 5: "REQUIRED fields in every role file (FORBIDDEN: any role file missing any field): orientation, lens, expertise, scope, collaborates_with" |
| C-03 | PASS | "INERTIA-ADVOCATE: MUST appear in ROLES-LOADED or ROLES-NOTE. MUST add if absent." |
| C-04 | PASS | "Standard: MUST produce 20-30 files. Deep: MUST produce 50+. FORBIDDEN: producing fewer than the lower bound." |
| C-05 | PASS | "MUST use: Area | Headcount | Key Roles | Decides | Escalates. FORBIDDEN: single Decision Scope column." |
| C-06 | PASS | "MUST group under area subdirs. REQUIRED: minimum 2. FORBIDDEN: all roles in a flat directory with no area grouping." |
| C-07 | PASS | "MUST include minimum three distinct rows. FORBIDDEN: combining two cadences." "FORBIDDEN: short Quorum form. FORBIDDEN: any charter missing a Quorum field." |
| C-08 | PASS | Step 1: FLAT-CASE-PRESSURE with rating; SINGLE-VERDICT GUARD with "Only one verdict. Both is an error." STRUCTURAL-DECISION record. |
| C-09 | PASS | "MUST include two rows from DISTINCT trigger categories. FORBIDDEN: two rows both typed as headcount threshold." |
| C-10 | PASS | Section 7: "MUST open each 'Why It Applies Here' cell with: [element name] (cat-N). FORBIDDEN: any cell without (cat-N) typed syntax. FORBIDDEN: cat-N codes outside ANTI-PATTERN-CATEGORIES-SET." Full MUST + FORBIDDEN coverage. |
| C-11 | PASS | Step 3: "MUST select IA scope template using STRUCTURAL-DECISION PRESSURE as key. FORBIDDEN: writing inertia-advocate scope from scratch." Step 5: "MUST set scope = IA-SCOPE-SELECTED text (exact). FORBIDDEN: using any other text." |
| C-12 | PASS | Step 2 is immediately after Step 1 verdict — "MUST derive before any role is written or diagram drawn." ANTI-PATTERN DERIVATION with DERIVATION-RATIONALE and FORBIDDEN for out-of-category use. |
| C-13 | PASS | "Only one verdict. Both is an error. Neither is an error. FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts." |

**essential=5/5, recommended=3/3, aspirational=5/5 → composite = 100**

---

## Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|-----------|---------------|-------------------|-------------------|-----------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

All five variations clear the golden threshold. The R2 variate fully closed all four v2 gaps across every axis. Ranking within the 100 tier: **V-05 ≈ V-02 > V-04 > V-03 > V-01**, based on strength of constraint enforcement — FORBIDDEN guards for every violation path, explicit derivation prerequisites, and upfront register declarations.

---

## Excellence Signals

**From V-05 (top by qualitative margin):**

1. **Derivation-before-creation sequencing** — Steps 2 and 3 (anti-pattern derivation + IA scope selection) execute immediately after the verdict, before any role file or diagram work begins. C-12 and C-11 become structural prerequisites, not instructions embedded in later steps.

2. **Cross-derivation gate guard** — "FORBIDDEN: proceeding to Step 4 without both ANTI-PATTERN-CATEGORIES-SET and IA-SCOPE-SELECTED recorded above" captures the dependency between two separate derivations as a single gating condition.

3. **DERIVATION-RATIONALE field** — Each anti-pattern derivation rule includes an explicit rationale sentence ("flat org primary failure modes are headcount drift and meeting proliferation") that makes the category-to-structure mapping an explained rule, not a lookup table.

**From V-02:**

4. **Upfront CONSTRAINT REGISTER declaration** — "All rules below use MUST (required), FORBIDDEN (prohibited), and REQUIRED (mandatory field). 'Should' and 'consider' do not appear." This primes every subsequent section to be read at binary compliance level, removing interpretive slack.

**From V-04:**

5. **Named typed turn outputs** — T1-PRESSURE, T1-VERDICT, T2-IA-SCOPE, T3-CATEGORIES-SET as explicit named variables make derivation chains trackable: each downstream section can cite the exact input it consumed, making derivation-binding verifiable.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["derivation-before-creation sequencing — anti-pattern and IA scope derivations execute immediately after verdict, before any role or diagram work, making C-11/C-12 structural prerequisites not embedded instructions", "cross-derivation gate guard — single FORBIDDEN gate captures both derivation outputs as a combined pre-condition for role sequence", "named typed turn outputs (T1-PRESSURE, T2-IA-SCOPE, T3-CATEGORIES-SET) make derivation chains trackable and verifiable by downstream steps"]}
```
