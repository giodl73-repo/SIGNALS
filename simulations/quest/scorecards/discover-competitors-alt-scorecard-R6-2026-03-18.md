# discover-competitors-alt — Round 6 Scorecard

## Rubric v6 — Criteria Reference

**New in v6:** C-21 (pre-phase declares both unconditional nature AND conditional successor), C-22 (AMEND schema component names are domain-neutral / naive-reader consultable). Aspirational tier expands to 14 criteria, 0.714 pts each.

---

## V-01 Scorecard — Lifecycle / Direct V-05 R5 Evolution

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | GATE-2 opens with C0 section explicitly before any competitor row |
| C-02 | 3+ named competitors with threat levels | PASS | "Minimum 3 named external competitors… every row: HIGH/MEDIUM/LOW" |
| C-03 | C0 at row 0 in competitive map | PASS | Table template shows row 0 = C0 |
| C-04 | Whitespace identified | PASS | GATE-3 has labeled whitespace gap with specific uncontested dimension |
| C-05 | Auto-detect topic without prompting | PASS | GATE-1: "Read the repo context. Do not ask the user for topic, competitor names, or market category." |
| C-06 | Mechanism-level inertia reasoning | PASS | GATE-2 C0 template: `[TOKEN]: [mechanism type] → [specific behavior tied to C0]` |
| C-07 | Web-verified competitive claim with inline citation | PASS | "Run a WebSearch… at least one Source cell with inline citation — not a footnote block" |
| C-08 | AMEND with input-to-output pairs | PASS | GATE-4 table has `Input change` and `Output effect` columns, min 3 rows |
| C-09 | Cross-dimensional whitespace | PASS | GATE-3: "If FOCUS is ACTIVE: gap must be uncontested across both competitive and focus dimensions simultaneously" |
| C-10 | Grounded findings | PASS | "Each finding references at least one named competitor row by its table label" |
| C-11 | Inertia reference propagates downstream | PASS | `vs [TOKEN]` required in every finding line; TOKEN appears in AMEND verdict column |
| C-12 | AMEND evaluates inertia stability | PASS | Stability verdict column present; C-08 passes |
| C-13 | Inertia mechanism assigned portable token | PASS | TOKEN declared in GATE-0 as a "copyable identifier" |
| C-14 | Stability addressed in every AMEND entry | PASS | "Verdict and evidence required in every row" |
| C-15 | Token pre-declared before C0 description | PASS | TOKEN in GATE-0; C0 in GATE-2 — structurally prior |
| C-16 | Stability verdict + evidence in every entry | PASS | "Evidence: reasoning distinct from the verdict. 'Stable.' alone fails." |
| C-17 | Token encodes domain context | PASS | "Must include at least one term from DOMAIN-TERMS line" |
| C-18 | DOMAIN-TERMS as extraction artifact before token | PASS | DOMAIN-TERMS line written and closed before TOKEN line — two-step output |
| C-19 | TOKEN before any conditional logic | PASS | GATE-0 is unconditional first output; no focus detection, no headers before TOKEN |
| C-20 | AMEND schema enumerates all 4 components by name | PASS | Column headers: `Input change \| Output effect \| Stability verdict \| Evidence` |
| C-21 | Pre-phase declares both unconditional nature AND conditional successor | PASS | GATE-0 header: `[unconditional — GATE-1 is the first conditional operation]` — both conditions in one sentence |
| C-22 | AMEND schema names pass naive-reader consultability | PASS | All four headers are domain-neutral; naive reader can match each to rubric-standard function |

**Essential:** 5/5 = 60 pts  
**Recommended:** 3/3 = 30 pts  
**Aspirational:** 14/14 × 10 = 10.000 pts  
**Composite: 100.000** ✦ Grade: A+

---

## V-02 Scorecard — Pre-Execution Phase Manifest

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | GATE-2 (compact body) follows standard structure — C0 before competitor rows |
| C-02 | 3+ named competitors | PASS | Standard gate body requirement carries forward |
| C-03 | C0 at row 0 | PASS | Standard |
| C-04 | Whitespace identified | PASS | Standard |
| C-05 | Auto-detect topic | PASS | GATE-1 handles focus detection without prompting |
| C-06 | Mechanism-level inertia | PASS | TOKEN declared with domain-context identifier in GATE-0; GATE-2 mechanism description standard |
| C-07 | Web-verified citation | PASS | Standard GATE-2 WebSearch requirement |
| C-08 | AMEND with input-to-output pairs | PASS | GATE-4 compact body inherits schema |
| C-09 | Cross-dimensional whitespace | PASS | Standard GATE-3 requirement |
| C-10 | Grounded findings | PASS | Standard per-finding competitor reference |
| C-11 | Inertia propagates downstream | PASS | TOKEN declared in GATE-0; downstream gates reference it |
| C-12 | AMEND evaluates stability | PASS | Standard; C-08 passes |
| C-13 | Portable token | PASS | GATE-0 declares TOKEN with domain term from DOMAIN-TERMS |
| C-14 | Stability in every AMEND entry | PASS | Standard row requirement |
| C-15 | Token before C0 description | PASS | GATE-0 precedes GATE-2 structurally |
| C-16 | Verdict + evidence per entry | PASS | Standard |
| C-17 | Token encodes domain context | PASS | "Must include at least one term from DOMAIN-TERMS" |
| C-18 | DOMAIN-TERMS artifact before token | PASS | Two-line output: DOMAIN-TERMS closed, then TOKEN |
| C-19 | TOKEN before conditional logic | PASS | GATE-0 is unconditional first output; manifest is pre-execution instruction, not conditional logic |
| C-20 | AMEND schema enumerates 4 components | PASS | Compact gate bodies inherit schema headers |
| C-21 | Pre-phase declares unconditional nature + conditional successor | PASS | Manifest table: `GATE-0 = UNCONDITIONAL \| GATE-1 = CONDITIONAL (first)`; narrative: "GATE-0 is the only unconditional gate. GATE-1 is the first gate where conditional logic executes." Both conditions architecturally declared in the manifest before execution begins |
| C-22 | AMEND schema names domain-neutral | PASS | Inherited domain-neutral headers |

**Essential:** 5/5 = 60 pts  
**Recommended:** 3/3 = 30 pts  
**Aspirational:** 14/14 × 10 = 10.000 pts  
**Composite: 100.000** ✦ Grade: A+

---

## V-03 Scorecard — Conversational Steps

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Step structure preserves C0-first ordering |
| C-02 | 3+ named competitors | PASS | Standard |
| C-03 | C0 at row 0 | PASS | Standard |
| C-04 | Whitespace identified | PASS | Standard |
| C-05 | Auto-detect topic | PASS | Step 2 (first conditional) handles detection from repo context |
| C-06 | Mechanism-level inertia | PASS | TOKEN declared in Step 1 with mechanism specificity |
| C-07 | Web-verified citation | PASS | Standard |
| C-08 | AMEND with input-to-output pairs | PASS | Numbered AMEND with bold domain-neutral component labels |
| C-09 | Cross-dimensional whitespace | PASS | Standard |
| C-10 | Grounded findings | PASS | Standard competitor reference per finding |
| C-11 | Inertia propagates downstream | PASS | TOKEN required downstream |
| C-12 | AMEND evaluates stability | PASS | Stability in AMEND; C-08 passes |
| C-13 | Portable token | PASS | TOKEN declared in Step 1 |
| C-14 | Stability in every AMEND entry | PASS | Every row requires verdict |
| C-15 | Token before C0 description | PASS | Step 1 (TOKEN) precedes Step 3+ (C0) |
| C-16 | Verdict + evidence per entry | PASS | Standard |
| C-17 | Token encodes domain context | PASS | Domain term from DOMAIN-TERMS required |
| C-18 | DOMAIN-TERMS artifact before token | PASS | Two-step output in Step 1 |
| C-19 | TOKEN before conditional logic | PASS | Step 1 is unconditional; TOKEN precedes Step 2 |
| C-20 | AMEND schema enumerates 4 components | PASS | Bold domain-neutral component labels in numbered AMEND |
| C-21 | Pre-phase declares unconditional nature + conditional successor | **FAIL** | "Step 1 is unconditional. Step 2 is the first conditional step." — both conditions present in content, but in conversational prose without structural/architectural markers. No gate header, manifest table, or schema notation. C-21 requires "architecturally declared" — plain prose statements do not constitute architectural declaration even when both conditions are stated. |
| C-22 | AMEND schema names domain-neutral | PASS | Bold labels are domain-neutral |

**Essential:** 5/5 = 60 pts  
**Recommended:** 3/3 = 30 pts  
**Aspirational:** 13/14 × 10 = 9.286 pts  
**Composite: 99.286** — Grade: A+

---

## V-04 Scorecard — TOKEN Propagation Emphasis

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | V-01 architecture; C0 section before competitor rows |
| C-02 | 3+ named competitors | PASS | Standard |
| C-03 | C0 at row 0 | PASS | Standard |
| C-04 | Whitespace identified | PASS | `[TOKEN] exposure:` field in whitespace section |
| C-05 | Auto-detect topic | PASS | GATE-1 conditional |
| C-06 | Mechanism-level inertia | PASS | Same as V-01 |
| C-07 | Web-verified citation | PASS | Standard |
| C-08 | AMEND with input-to-output pairs | PASS | AMEND verdict column explicitly names TOKEN |
| C-09 | Cross-dimensional whitespace | PASS | `[TOKEN] exposure:` field forces intersection |
| C-10 | Grounded findings | PASS | TOKEN by name in every finding line → every finding is anchored |
| C-11 | Inertia propagates downstream | PASS | Strongest C-11 signal: `vs [TOKEN]` column header mandatory; TOKEN in every finding line; whitespace has TOKEN field; AMEND verdict names TOKEN |
| C-12 | AMEND evaluates stability | PASS | AMEND verdict column names TOKEN explicitly; C-08 passes |
| C-13 | Portable token | PASS | Declared GATE-0 |
| C-14 | Stability in every AMEND entry | PASS | Every AMEND row has TOKEN-named verdict |
| C-15 | Token before C0 description | PASS | GATE-0 before GATE-2 |
| C-16 | Verdict + evidence per entry | PASS | Standard |
| C-17 | Token encodes domain context | PASS | Domain term required |
| C-18 | DOMAIN-TERMS artifact before token | PASS | Two-line extraction artifact |
| C-19 | TOKEN before conditional logic | PASS | Same GATE-0 architecture as V-01 |
| C-20 | AMEND schema enumerates 4 components | PASS | Same column headers as V-01 |
| C-21 | Pre-phase declares unconditional nature + conditional successor | PASS | GATE-0 header: `[unconditional — GATE-1 is the first conditional operation]` — identical to V-01 |
| C-22 | AMEND schema names domain-neutral | PASS | Column headers remain domain-neutral; TOKEN propagation requirements appear in cell-level instructions, not schema component names |

**Essential:** 5/5 = 60 pts  
**Recommended:** 3/3 = 30 pts  
**Aspirational:** 14/14 × 10 = 10.000 pts  
**Composite: 100.000** ✦ Grade: A+

---

## V-05 Scorecard — Combined (Manifest + Gates + TOKEN Propagation + Explicit Schema)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Both manifest and gate bodies enforce C0-first |
| C-02 | 3+ named competitors | PASS | Standard |
| C-03 | C0 at row 0 | PASS | Standard |
| C-04 | Whitespace identified | PASS | TOKEN propagation includes whitespace field |
| C-05 | Auto-detect topic | PASS | GATE-1 conditional |
| C-06 | Mechanism-level inertia | PASS | Full mechanism description in GATE-2 |
| C-07 | Web-verified citation | PASS | Standard |
| C-08 | AMEND with input-to-output pairs | PASS | Schema declaration block explicitly enumerates all components |
| C-09 | Cross-dimensional whitespace | PASS | TOKEN propagation forces intersection evidence |
| C-10 | Grounded findings | PASS | TOKEN in every finding line anchors all findings |
| C-11 | Inertia propagates downstream | PASS | Maximum propagation: TOKEN in every gate section |
| C-12 | AMEND evaluates stability | PASS | C-08 passes with full schema |
| C-13 | Portable token | PASS | GATE-0 declaration |
| C-14 | Stability in every AMEND entry | PASS | Schema enforces per-row stability |
| C-15 | Token before C0 description | PASS | GATE-0 before GATE-2 |
| C-16 | Verdict + evidence per entry | PASS | Schema requires evidence column distinct from verdict |
| C-17 | Token encodes domain context | PASS | Domain term from DOMAIN-TERMS |
| C-18 | DOMAIN-TERMS artifact before token | PASS | Explicit extraction step before TOKEN |
| C-19 | TOKEN before conditional logic | PASS | GATE-0 is unconditional first execution |
| C-20 | AMEND schema enumerates 4 components | PASS | AMEND schema declaration block "quotes all four rubric-standard component names" |
| C-21 | Pre-phase declares unconditional nature + conditional successor | PASS | Strongest signal: manifest table + GATE-0 gate header both declare unconditional/conditional boundary |
| C-22 | AMEND schema names domain-neutral | PASS | "Explicitly matched to rubric-standard terminology" — Input change, Output effect, Stability verdict, Evidence |

**Essential:** 5/5 = 60 pts  
**Recommended:** 3/3 = 30 pts  
**Aspirational:** 14/14 × 10 = 10.000 pts  
**Composite: 100.000** ✦ Grade: A+

---

## Rankings

| Rank | Variation | Composite | Grade |
|------|-----------|-----------|-------|
| 1 (tied) | V-01 | 100.000 | A+ |
| 1 (tied) | V-02 | 100.000 | A+ |
| 1 (tied) | V-04 | 100.000 | A+ |
| 1 (tied) | V-05 | 100.000 | A+ |
| 5 | V-03 | 99.286 | A+ |

---

## Excellence Signals

**From V-01/V-04 (gate-header declaration):**
GATE-0 bracket header encoding both conditions in one sentence — `[unconditional — GATE-1 is the first conditional operation]` — is the minimal architectural form for C-21. The condition boundary is co-located with the gate it describes, making it impossible to misread execution order.

**From V-02 (manifest-level declaration):**
A phase manifest table that pre-declares all gate conditions before any gate body executes satisfies C-21 at the schema level. The manifest is itself an architectural artifact — it frames the entire execution contract before TOKEN output begins. This is structurally equivalent to (and arguably stronger than) gate-header labels.

**From V-05 (combined):**
Stacking manifest + gate headers produces the highest C-21 confidence — two independent structural markers both declaring the same boundary. Neither can be misread in isolation, and they reinforce each other. Combined with explicit rubric-standard AMEND schema component names, V-05 leaves no ambiguity on C-21 or C-22.

**Decisive R6 finding (V-03):**
Prose stating both C-21 conditions is not architecturally equivalent to structural declaration. "Step 1 is unconditional. Step 2 is the first conditional step." is semantically complete but architecturally absent — no gate header, manifest table, or schema notation. C-21 FAIL confirms that "architecturally declared" is not satisfied by in-line prose, even correct prose.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Manifest-level phase declaration satisfies C-21 architecturally declared requirement — a pre-execution table pre-declaring gate conditions is structurally equivalent to per-gate bracket headers for C-21 purposes", "Conversational prose stating both C-21 conditions fails architecturally declared — structural markers (gate headers, manifest tables, schema notation) are required regardless of semantic completeness"]}
```
