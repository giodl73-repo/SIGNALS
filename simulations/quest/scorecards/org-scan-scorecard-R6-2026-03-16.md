# org-scan Round 6 — Scoring (rubric v6)

## V-01: Lifecycle Emphasis

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | ANTI-FABRICATION in GROUP A: "traceable to a cited file path or named source type" |
| C-02 | PASS | 7-item Source Coverage list, scan 3+ required |
| C-03 | PASS | "State headcount as a range (e.g., 4–7). Justify from distinct expertise domains" |
| C-04 | PASS | Cross-Cutting Concerns table with Boundary Note column |
| C-05 | PASS | Preamble constraint + restatement in GROUP B |
| C-06 | PASS | Team Boundary Candidates table with Seam Rationale |
| C-07 | PASS | Org Shape section with justification requirement |
| C-08 | PASS | Evidence Gaps section present |
| C-09 | PASS | FILE PATH FLOOR requires 5 specific paths |
| C-10 | PASS | Current State / Recommended State as distinct labeled sections |
| C-11 | PASS | GROUP A anti-fab block + GROUP B synthesis anti-fab: "applies equally to seam candidates, headcount estimates, and org shape" |
| C-12 | PASS | PHASE 1 → PHASE 2 GATE section with blocking instruction |
| C-13 | PASS | "OUTPUT CONSTRAINT (preamble)" + "OUTPUT CONSTRAINT (restatement)" in GROUP B |
| C-14 | PASS | Numbered checklist items 1–4 + "if all four conditions pass, write the PASS TOKEN" |
| C-15 | PASS | Explicit GROUP A: CURRENT STATE / GROUP B: RECOMMENDED STATE headers |
| C-16 | PASS | "This is a gate condition — fewer than 5 paths blocks Phase 2" |
| C-17 | PASS | SCAN GATE CLEAR token format defined in GATE TOKEN PROTOCOL |
| C-18 | PASS | "PATH FLOOR NOT MET — halt" defined as fail token |
| C-19 | PASS | Inertia Match column present in scan table |
| C-20 | PASS | GATE TOKEN PROTOCOL block in preamble before Phase 1 |
| C-21 | PASS | OUTPUT SCHEMA with Status column: "REQUIRED. Empty cells in REQUIRED columns are structural gaps visible in the table" |
| C-22 | **PASS+** | Phase 1 postcondition + Phase 2 precondition as separate blocks with "These two statements name the same contract from both sides. Both must hold." — lead mechanism |
| C-23 | PASS | INERTIA PATTERN REFERENCE with enumerated labels; "*Inertia Match accepts only labels from the INERTIA PATTERN REFERENCE above*" |
| C-24 | PASS | Token format: "[N] sources scanned, [N] paths cited, dominant pattern: [PATTERN_LABEL]" + "making it self-reporting about the conditions it asserts" |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 16/16 × 2 = 32 → capped at 10  
**Composite: 100**

---

## V-02: Inertia Framing

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | ANTI-FABRICATION in Phase 1 |
| C-02 | PASS | 7-item source list, scan 3+ |
| C-03 | PASS | Headcount range from domain count |
| C-04 | PASS | Cross-Cutting Concerns table present |
| C-05 | PASS | Preamble + restatement in Phase 2 header |
| C-06 | PASS | Team Boundary Candidates with Seam Rationale |
| C-07 | PASS | Org Shape section |
| C-08 | PASS | Evidence Gaps section |
| C-09 | PASS | FILE PATH FLOOR: 5 paths before Phase 2 |
| C-10 | PASS | Current State / Recommended State as distinct sections |
| C-11 | PASS | Phase 1 anti-fab + Phase 2: "Seam candidates, headcount, and org shape must be grounded in Phase 1 evidence — not pattern familiarity" |
| C-12 | PASS | GATE section blocks Phase 2 |
| C-13 | PASS | Preamble constraint + Phase 2 restatement |
| C-14 | PASS | Numbered items 1–4 + confirmation sentence |
| **C-15** | **FAIL** | Uses PHASE 1 / PHASE 2 labels, not GROUP A / GROUP B discrete group labels |
| C-16 | PASS | "If fewer than 5 paths are found, output the FAIL TOKEN and stop" |
| C-17 | PASS | SCAN GATE CLEAR token format |
| C-18 | PASS | PATH FLOOR NOT MET — halt |
| C-19 | **PASS+** | Inertia Match column placed before File Path Evidence; "Pattern identification precedes citation" — strongest column-order enforcement |
| C-20 | PASS | GATE TOKEN PROTOCOL block present |
| C-21 | PASS | "Required columns (empty cells in required columns are visible structural gaps):" before table; Inertia Match explicitly tagged "REQUIRED column" |
| C-22 | PASS | "Phase 1 postcondition / Phase 2 precondition: … Both sides of this contract must hold." — compact bidirectional contract |
| C-23 | **PASS+** | INERTIA PATTERN DICTIONARY; "Free text is structurally invalid — unconstrained values make pattern comparison across runs unverifiable" — lead mechanism, strongest rationale |
| C-24 | **PASS+** | "Include the actual source count, path count, and the most frequent Inertia Match label — making the token self-documenting about what it asserts" |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 15/16 × 2 = 30 → capped at 10  
**Composite: 100**

---

## V-03: Output Format / Schema-First

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | ANTI-FABRICATION in Phase 1: "Every row in Schema A must be traceable to a cited file path" |
| C-02 | PASS | Source types list, 3+ required |
| C-03 | PASS | Headcount range from Schema A domain count |
| C-04 | PASS | Schema C — Cross-Cutting Concerns with REQUIRED columns |
| C-05 | PASS | Preamble constraint + restatement in Output Schema section |
| C-06 | PASS | Schema B — Team Boundary Candidates with REQUIRED Seam Rationale |
| C-07 | PASS | Org Shape section in Phase 2 |
| C-08 | PASS | Evidence Gaps section |
| C-09 | PASS | FILE PATH FLOOR gate condition |
| C-10 | PASS | Current State / Recommended State declared as "distinct labeled sections" before GROUP A |
| C-11 | PASS | Phase 1 anti-fab + Phase 2 anti-fab covering all synthesis outputs |
| C-12 | PASS | GATE CHECK section with blocking instruction |
| C-13 | PASS | Preamble OUTPUT CONSTRAINT + restatement in Output Schema |
| C-14 | PASS | Numbered checklist items 1–5 + confirmation sentence |
| **C-15** | **FAIL** | PHASE 1 / PHASE 2 labels; no GROUP A / GROUP B discrete structural labels |
| C-16 | PASS | "This is a gate condition — not an output expectation." |
| C-17 | PASS | SCAN GATE CLEAR token format |
| C-18 | PASS | PATH FLOOR NOT MET — halt |
| C-19 | PASS | Inertia Match column in Schema A |
| C-20 | PASS | GATE TOKEN PROTOCOL block |
| C-21 | **PASS+** | Full OUTPUT SCHEMA with Status column (REQUIRED / optional) for every column in Schema A — lead mechanism; "Empty cells in REQUIRED columns are structural gaps visible in the table" |
| C-22 | PASS | "Phase 1 postcondition / Phase 2 precondition: Schema A is complete… Both sides name the same conditions." |
| C-23 | PASS | INERTIA PATTERN DICTIONARY embedded with enumerated labels; "Free text is not a valid Inertia Match entry" |
| C-24 | **PASS+** | Token includes source count, path count, dominant pattern; "making the token self-documenting about what it asserts" |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 15/16 × 2 = 30 → capped at 10  
**Composite: 100**

---

## V-04: Lifecycle + Inertia Combined

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | GROUP A ANTI-FABRICATION |
| C-02 | PASS | 7-item source list |
| C-03 | PASS | Headcount range with GROUP A domain count rationale |
| C-04 | PASS | Cross-Cutting Concerns table in GROUP B |
| C-05 | PASS | Preamble + GROUP B restatement |
| C-06 | PASS | Team Boundary Candidates table |
| C-07 | PASS | Org Shape section |
| C-08 | PASS | Evidence Gaps section |
| C-09 | PASS | FILE PATH FLOOR gate precondition |
| C-10 | PASS | Current State / Recommended State as distinct sections in GROUP B |
| C-11 | PASS | GROUP A anti-fab + GROUP B: "Seam candidates must cite… Headcount must derive… Org shape must be justified by Phase 1 evidence — not convention, pattern familiarity, or assumption" |
| C-12 | PASS | GATE CHECK section with blocking |
| C-13 | PASS | Preamble + GROUP B restatement |
| C-14 | PASS | Numbered checklist 1–5 + confirmation sentence |
| C-15 | PASS | Explicit GROUP A: CURRENT STATE / GROUP B: RECOMMENDED STATE headers |
| C-16 | PASS | "This is a precondition for Phase 2. If fewer than 5 paths are found, output the FAIL TOKEN and stop." |
| C-17 | PASS | SCAN GATE CLEAR token |
| C-18 | PASS | PATH FLOOR NOT MET — halt |
| C-19 | **PASS+** | Inertia Match column before File Path Evidence; "Column order places Inertia Match before evidence — pattern identification precedes citation" |
| C-20 | PASS | GATE TOKEN PROTOCOL block |
| C-21 | **PASS+** | OUTPUT SCHEMA with Status + Constraint columns; "empty cells in REQUIRED columns are visible structural gaps" |
| C-22 | **PASS+** | Full Phase 1 postcondition + Phase 2 precondition blocks with identical condition lists; "These two statements name the same contract from both sides. Both must hold." |
| C-23 | **PASS+** | INERTIA PATTERN DICTIONARY defined before Phase 1; "Free text is invalid" |
| C-24 | **PASS+** | "The token is self-documenting: it names source count, path count (asserting path floor status), and dominant pattern name — making it self-reporting about the three key conditions it verifies" |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 16/16 × 2 = 32 → capped at 10  
**Composite: 100**

---

## V-05: All Axes — Maximum Coverage

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | GROUP A ANTI-FABRICATION: "Do not populate Area without File Path Evidence" |
| C-02 | PASS | 7-item source list, 3+ required |
| C-03 | PASS | Headcount range from Schema A domain count; "Derive from Schema A domain count only. Do not extrapolate." |
| C-04 | PASS | Schema C — Cross-Cutting Concerns with REQUIRED columns; "Concern, Areas Affected, and Inertia Pattern must be traceable to Schema A evidence" |
| C-05 | PASS | Preamble + GROUP B restatement |
| C-06 | PASS | Schema B — Team Boundary Candidates with REQUIRED Seam Rationale |
| C-07 | PASS | Org Shape section |
| C-08 | PASS | Evidence Gaps section |
| C-09 | PASS | FILE PATH FLOOR gate condition |
| C-10 | PASS | Current State / Recommended State declared as distinct labeled sections in preamble before GROUP A begins |
| C-11 | **PASS+** | Symmetric anti-fabrication: GROUP A has evidence anti-fab; GROUP B names every synthesis output type individually: seam candidates, boundary notes, headcount, org shape — broadest per-section coverage of any variation |
| C-12 | PASS | GATE CHECK section |
| C-13 | PASS | Preamble + GROUP B restatement |
| C-14 | PASS | Numbered checklist 1–5 + confirmation sentence |
| C-15 | PASS | GROUP A: CURRENT STATE / GROUP B: RECOMMENDED STATE headers |
| C-16 | PASS | "This is a gate condition — not merely an output expectation." |
| C-17 | PASS | SCAN GATE CLEAR token |
| C-18 | PASS | PATH FLOOR NOT MET — halt |
| C-19 | **PASS+** | Inertia Match before File Path Evidence in Schema A column order |
| C-20 | PASS | GATE TOKEN PROTOCOL block |
| C-21 | **PASS+** | OUTPUT SCHEMA declares REQUIRED columns for all three schemas (A, B, and C) — only variation extending enforcement to downstream synthesis schemas |
| C-22 | **PASS+** | Full Phase 1 postcondition + Phase 2 precondition blocks; "These two statements name the same contract from both sides. Both must hold." |
| C-23 | **PASS+** | INERTIA PATTERN DICTIONARY; "Free text is structurally invalid — unconstrained values make the column unverifiable and cross-run pattern comparison impossible" — adds longitudinal verifiability rationale |
| C-24 | **PASS+** | "it asserts source count, path floor status (via path count), and dominant inertia pattern name — naming the three key conditions it verifies" — explicit three-condition enumeration |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 16/16 × 2 = 32 → capped at 10  
**Composite: 100**

---

## Ranking

| Rank | Variation | Composite | C-15 | PASS+ count |
|---|---|---|---|---|
| 1 (tied) | V-05 | 100 | PASS | 6 (C-19, C-21, C-22, C-23, C-24, C-11) |
| 1 (tied) | V-04 | 100 | PASS | 5 (C-19, C-21, C-22, C-23, C-24) |
| 1 (tied) | V-01 | 100 | PASS | 1 (C-22) |
| 4 (tied) | V-02 | 100 | FAIL | 3 (C-19, C-23, C-24) |
| 4 (tied) | V-03 | 100 | FAIL | 2 (C-21, C-24) |

All five variations clear the golden threshold (all 5 essential pass, composite ≥ 80). The cap design absorbs the C-15 misses in V-02 and V-03 — 15 aspirationals × 2 = 30, still capped at 10. Composite is invariant to single-criterion misses at this aspirational density.

**V-05 leads qualitatively**: it is the only variation where multi-schema REQUIRED enforcement covers all three schemas (A, B, C) and where GROUP B anti-fabrication names each synthesis output type individually as a grounding target. These go beyond any current criteria.

---

## Excellence Signals (V-05)

**Signal 1 — Multi-schema REQUIRED enforcement extends to downstream schemas**
V-05 declares `[REQUIRED]` column status for Schema A (scan table), Schema B (boundary candidates), and Schema C (cross-cutting concerns). All other variations declare REQUIRED only for Schema A. Extending structural gap-visibility to synthesis schemas means an empty Seam Rationale or Boundary Note is a visible structural omission — not a silent prose gap. This goes beyond C-21, which specifies evidence columns; the pattern is: every schema that produces evidence for downstream decisions should carry REQUIRED enforcement.

**Signal 2 — Per-output-type grounding in synthesis-phase anti-fabrication**
V-05's GROUP B ANTI-FABRICATION names every synthesis output type explicitly: seam candidates → cite Supporting Paths; boundary notes → reference Schema A finding; headcount → derive from Schema A domain count only; org shape → justified by Phase 1 evidence, not convention or assumption. Other variations use general anti-fabrication language in GROUP B that applies to "synthesis" in aggregate. The pattern is: anti-fabrication notes in synthesis phases are stronger when they enumerate each inferred output type rather than relying on the agent to extend the constraint transitively.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Multi-schema REQUIRED enforcement: extending [REQUIRED] column declarations to all synthesis schemas (boundary candidates, cross-cutting concerns), not only the Phase 1 scan table, makes structural omissions visible in downstream outputs without prose inspection", "Per-output-type synthesis anti-fabrication: naming each synthesis output type individually (seam candidates, headcount, org shape, boundary notes) in the GROUP B anti-fabrication note is stronger than general synthesis-level language, which leaves transitivity to the agent"]}
```
