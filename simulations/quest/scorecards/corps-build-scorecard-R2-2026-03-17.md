## Quest Score — corps-build Round 2

### Rubric Reference

| ID | Short text | Weight | Max pts |
|----|-----------|--------|---------|
| C-01 | Role file completeness | essential | 12 |
| C-02 | org-chart.md with ASCII hierarchy | essential | 12 |
| C-03 | Inertia Advocate in every team | essential | 12 |
| C-04 | org.yaml structural fidelity | essential | 12 |
| C-05 | Role file typed fields present | essential | 12 |
| C-06 | Headcount by group table + levels | recommended | 10 |
| C-07 | Standard vs specialized distinction | recommended | 10 |
| C-08 | AMEND section with three options | recommended | 10 |
| C-09 | Inertia Advocate team-contextualized | aspirational | 5 |
| C-10 | Cross-reference integrity chart/roles | aspirational | 5 |

Composite formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
PARTIAL = 0.5 pass weight.

---

### V-01 — Scaffold-First

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Skeleton team list establishes iteration order; Step 4 finalizes with count check: "Total must equal the count of files written in Step 3; identify discrepancy before AMEND" |
| C-02 | **PASS** | Step 2 writes org-chart.md skeleton with full ASCII hierarchy (+-- and \|, names verbatim, 2+ levels) before any role files |
| C-03 | **PASS** | Step 3 per-team sequence: "3. Inertia Advocate (mandatory — one per team, no exceptions)" |
| C-04 | **PASS** | Skeleton is the contract: "Any area in the diagram must exist as a subdirectory; any area not in the diagram must not exist" |
| C-05 | **PASS** | Five fields enumerated in Step 3 with explicit "non-empty" constraint; no TBD |
| C-06 | **PASS** | Step 4 updates table with Standard/Specialized/Inertia-Adv/Total/Levels columns per area |
| C-07 | **PASS** | Frontmatter `role-type: [standard | specialized | inertia-advocate]` required; per-category write order enforces at write time |
| C-08 | **PASS** | Step 5 AMEND with three named options: area from org.yaml, level term, team + parent |
| C-09 | **PARTIAL** | Instruction present ("lens and expertise must be drawn from this specific team's declared domain") but no pre-profiling mechanism to enforce before writing; no IA differentiation check |
| C-10 | **PASS** | Step 4: "Verify: the Total in this table must equal the count of files written in Step 3" — explicit cross-reference check |

**Essential pass:** 5/5 → 60
**Recommended pass:** 3/3 → 30
**Aspirational pass:** 0.5 + 1 = 1.5/2 → 7.5
**Composite: 97.5**
All essential: YES | Golden: YES

---

### V-02 — Coverage Audit Loop

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Audit [A]: "Expected: [total declared role slots] — Actual: [count written] — Status: PASS \| FAIL — list missing or phantom files"; explicit count gate before org-chart.md |
| C-02 | **PASS** | org-chart.md written after audit passes; Section 1 ASCII Hierarchy uses +-- and \|, verbatim names, 2+ levels |
| C-03 | **PASS** | Audit [B]: per-team "PRESENT at .roles/{area}/inertia-advocate.md \| MISSING" for every team; FAIL blocks org-chart.md |
| C-04 | **PASS** | Audit [C]: "For each area in org.yaml: [EXISTS \| MISSING]. Extra directories not in org.yaml: [list or none]" — bidirectional check |
| C-05 | **PASS** | Write instruction: "non-empty, non-TBD body text" for all five fields; Audit [D] spot-checks first file, last file, one IA file |
| C-06 | **PASS** | Headcount table in org-chart.md with per-area counts and Levels column; "Total must match audit check [A] Actual count" |
| C-07 | **PASS** | `role-type` frontmatter required on every file; per-team write sequence orders standard/specialized/IA categorically |
| C-08 | **PASS** | AMEND section with three specific named options: area, level term, team + new parent |
| C-09 | **PARTIAL** | "Identical IA content across two teams is a defect" adds anti-duplication rule but no pre-profiling phase; no audit check for IA vocabulary differentiation |
| C-10 | **PASS** | Headcount Total explicitly linked to audit [A] Actual count; org-chart.md Total = file count by construction |

**Essential pass:** 5/5 → 60
**Recommended pass:** 3/3 → 30
**Aspirational pass:** 0.5 + 1 = 1.5/2 → 7.5
**Composite: 97.5**
All essential: YES | Golden: YES

---

### V-03 — Schema-as-Contract

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PARTIAL** | Categorical write passes (Steps 2–4) by type across all teams; no count verification step; no checklist; a skipped team has no structural catch |
| C-02 | **PASS** | Step 6 Section A: "Use +-- and \|. All names verbatim from org.yaml. Minimum two nesting levels" |
| C-03 | **PASS** | Step 4 "WRITE INERTIA ADVOCATES" is a dedicated categorical pass: "For each team in declaration order, write the Inertia Advocate file" with explicit constraint |
| C-04 | **PASS** | Frontmatter `area: {area-slug matching org.yaml}` enforces naming; no audit but schema-level constraint |
| C-05 | **PASS** | Schema contract (F-1..F-5) defined upfront with specific content requirements per field; "TBD, empty bodies, or placeholder text fails the schema contract on any field" — strongest C-05 instruction |
| C-06 | **PASS** | Step 6 Section B: headcount table with Standard/Specialized/Inertia-Adv/Total/Levels; "Count from actual files written, not from org.yaml declaration" |
| C-07 | **PASS** | Schema specifies `role-type: standard \| specialized \| inertia-advocate \| shared-group \| exec-office`; specialized Step 3 instruction: "F-2 and F-3 must name domain-specific systems that distinguish this role from standard roles on the same team" |
| C-08 | **PASS** | Step 7 AMEND with three named options: area (with regenerate scope), level term, team + new parent |
| C-09 | **PARTIAL** | Step 4: anti-duplication rule "No two IA files may share identical F-2 or F-3 body text. If reuse detected, differentiate before proceeding." Stronger than V-01/V-02 instructions, but still no pre-profiling mechanism |
| C-10 | **PARTIAL** | "Count from actual files written" in headcount table; no explicit equality verification step between chart Total and .roles/ count |

**Essential pass:** 4.5/5 → 54
**Recommended pass:** 3/3 → 30
**Aspirational pass:** 0.5 + 0.5 = 1/2 → 5
**Composite: 89.0**
All essential: NO (C-01 PARTIAL) | Golden: NO | Status: PARTIAL PASS (composite ≥ 60, 3/3 recommended)

---

### V-04 — Scaffold-First + Coverage Audit Loop

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Step 2 TEAM CHECKLIST has per-team expected file counts: "[ ] [team name] — [n] role files expected at .roles/{area-slug}/"; audit [A] verifies "list any team with wrong count"; strongest C-01 in this round |
| C-02 | **PASS** | Step 2 skeleton Section 1 writes ASCII hierarchy upfront: "+-- and \|, all names verbatim, minimum two nesting levels, every team declared in org.yaml must appear" |
| C-03 | **PASS** | Audit [B]: per-team "PRESENT \| MISSING — .roles/{area}/inertia-advocate.md" for every team in skeleton checklist; FAIL blocks Step 5 |
| C-04 | **PASS** | Audit [C]: "For each area in skeleton: [EXISTS \| MISSING as .roles/{area-slug}/]. Directories present but not in skeleton: [list or none]" — bidirectional fidelity check against the pre-committed scaffold |
| C-05 | **PASS** | Write instruction: "five required fields with non-empty, non-TBD body text"; audit [D] spot-check: first file per area + one IA file |
| C-06 | **PASS** | Step 5 replaces PENDING with actual counts; level distribution section; "Total must equal audit [A] Actual" |
| C-07 | **PASS** | `role-type: standard/specialized/inertia-advocate` frontmatter; per-team categorical write sequence (standard → specialized → IA) |
| C-08 | **PASS** | Step 6 AMEND with three named options: area (with re-audit scope), level term, team + parent + update paths and chart |
| C-09 | **PARTIAL** | "Inertia Advocate's `lens` and `expertise` must reference this specific team's domain vocabulary. No cross-team boilerplate." Instruction present but no resistance profile pre-phase and no audit check for IA vocabulary against a reference set |
| C-10 | **PASS** | Step 5: "Verify: Total in updated table equals audit [A] Actual. If they differ, identify the discrepancy before writing the AMEND section" |

**Essential pass:** 5/5 → 60
**Recommended pass:** 3/3 → 30
**Aspirational pass:** 0.5 + 1 = 1.5/2 → 7.5
**Composite: 97.5**
All essential: YES | Golden: YES

---

### V-05 — Schema + Scaffold + Audit + Resistance Profile

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 1 TEAM CHECKLIST with per-team expected counts → Phase 3 marks [x] per team as files written → Phase 4 audit [A] verifies actual against checklist — triple-layer coverage |
| C-02 | **PASS** | Phase 1 skeleton Skeleton A: "Use +-- and \|. All names verbatim from org.yaml. Minimum two nesting levels. Every team from the parse manifest must appear." Phase 5 confirms hierarchy still accurate |
| C-03 | **PASS** | "Category C — Inertia Advocate (mandatory — one per team, no exceptions)" in Phase 3; Phase 4 audit [B] explicit PRESENT/MISSING per team |
| C-04 | **PASS** | Phase 4 audit [C]: "For each area in scaffold: [EXISTS \| MISSING]. Extra directories not in scaffold: [list or none]" — scaffold is the ground truth for fidelity |
| C-05 | **PASS** | Schema contract (F-1..F-5) defined at top with specific content requirements per field + "TBD or empty body on any F-1..F-5 fails the schema contract" + Phase 4 audit [D] spot-checks standard + specialized + IA files |
| C-06 | **PASS** | Phase 5 replaces all PENDING with actual counts; explicit "Level distribution section: if levels declared, show breakdown"; table includes Standard/Specialized/IA/Total/Levels |
| C-07 | **PASS** | Schema requires `role-type` in frontmatter; Phase 3 Category B specialized: "F-2 and F-3 must name domain-specific systems that distinguish this role from standard roles" |
| C-08 | **PASS** | Phase 6 AMEND with three named options; regenerate option includes "re-derive resistance profile (Phase 2)" — most complete AMEND scope of all variations |
| C-09 | **PASS** | Phase 2 resistance profiles derive per-team vocabulary; Phase 3 IA fields anchored to profile by field (F-1 ← rational objection, F-2 ← domain vocabulary term, F-3 ← status-quo investment); Phase 4 audit [E]: "Verify that each IA F-2 contains at least one term from its Phase 2 vocabulary set. Status: PASS \| FAIL" — only variation with audited C-09 enforcement |
| C-10 | **PASS** | Phase 5 exit check: "Total in table must equal Phase 4 [A] actual. If different, identify the discrepancy before writing Phase 6"; explicit halt condition |

**Essential pass:** 5/5 → 60
**Recommended pass:** 3/3 → 30
**Aspirational pass:** 2/2 → 10
**Composite: 100**
All essential: YES | Golden: YES

---

### Rankings

| Rank | Variation | Composite | All Essential | Golden |
|------|-----------|-----------|---------------|--------|
| 1 | V-05 Schema+Scaffold+Audit+Resistance | **100** | YES | YES |
| 2 | V-04 Scaffold+Audit | **97.5** | YES | YES |
| 3 | V-01 Scaffold-First | **97.5** | YES | YES |
| 4 | V-02 Audit Loop | **97.5** | YES | YES |
| 5 | V-03 Schema-as-Contract | **89.0** | NO | PARTIAL PASS |

*V-04 > V-01 > V-02 at 97.5: V-04 has per-team expected counts in the checklist + bidirectional directory audit, giving stronger structural verification than V-01's skeleton-total-only check or V-02's post-write audit without pre-commitment.*

---

### Excellence Signals from V-05

**1. Scaffold-as-structural-contract with per-team expected counts**
Phase 1 writes org-chart.md with a TEAM CHECKLIST listing exactly `[n] role files expected at .roles/{area-slug}/` per team. This is not a placeholder table — it is a per-team commitment before any file is written. Phase 3 marks [x] per team when files are written. Phase 4 [A] verifies actual against checklist total AND names any team with wrong count. The pre-commitment makes per-team gaps visible rather than only a total mismatch.

**2. Schema-ID reference contract**
Defining F-1..F-5 once at the top of the prompt and referencing them by ID throughout (not by name) means every subsequent instruction that says "populate F-1..F-5" carries the full schema by reference. There is a single authoritative definition; field descriptions are not repeated, abbreviated, or paraphrased in later steps. This structural reduction removes the surface area for field-omission by treating the schema as a closed enumeration rather than an inline list.

**3. Audit check [E]: IA vocabulary verification**
The only mechanism in this round that achieves C-09 PASS by construction. Phase 2 derives per-team vocabulary (4–6 distinct terms). Phase 3 anchors IA F-2 to at least one vocabulary term. Phase 4 [E] verifies "each IA F-2 contains at least one term from its Phase 2 vocabulary set" and blocks finalization on FAIL. Because the vocabulary sets must be distinct at the end of Phase 2 (reviewed before writing begins), two IA files cannot share F-2 content and also pass audit [E]. The resistance profile → IA field → vocabulary audit chain is the pattern that closes the C-09 loop.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["scaffold-as-structural-contract-with-per-team-counts: writing org-chart.md skeleton with explicit per-team expected file counts before any role files creates a pre-commitment checklist that is both marked during writing and audited after — stronger than total-count-only verification", "schema-ID-reference-contract: defining F-1..F-5 once at prompt top and referencing by ID throughout treats the schema as a closed enumeration, reducing field-omission surface area without repeating or paraphrasing requirements in each step", "IA-vocabulary-audit: deriving per-team resistance-profile vocabulary sets before writing, anchoring IA F-2 to at least one vocabulary term, then verifying this in a named audit check [E] is the only mechanism that achieves C-09 PASS by construction — closes the IA-differentiation loop structurally rather than instructionally"]}
```
