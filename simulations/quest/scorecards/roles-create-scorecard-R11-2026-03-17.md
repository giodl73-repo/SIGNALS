Now I have all the data needed. Let me score systematically.

---

## roles-create R11 — Scorecard

### Scoring Formula
`(essential_passed × 12) + (recommended_passed × 15) + (aspirational_passed × 10/19)`

5 Essential @ 12 pt | 2 Recommended @ 15 pt | 19 Aspirational @ 0.526 pt each

---

### Criteria Reference (abbreviated)

| ID | Tier | What it governs |
|----|------|----------------|
| C-01 – C-05 | Essential | Path, frontmatter, routing, domain specificity, inertia surface |
| C-06 – C-07 | Recommended | Sharp lens.verify, domain table in body |
| C-08 – C-14 | Aspirational | Archetype, register, column vocab, companion file, interactive hold, self-cert, malformed-input guard |
| C-15 – C-22 | Aspirational | In-phase gates, pre-declaration, CONTRACT blocks, traceability, thin phases, thin checklist, coverage, self-doc header, quarantine prereqs |
| C-23 | Aspirational | Rule content only in three canonical locations |
| C-24 | Aspirational | Gate structural form homogeneous across all phases |
| C-25 | Aspirational | Phase bodies at minimum surface (citation + artifact only) |
| C-26 | Aspirational | CONTRACTS block ordered by unconditional first-citation sequence |

---

### V-01: C-24 + C-25 Combination

**Structure:** Phase 0 uses TABLE gate; Phases 1–4 use inline `->`. Phase bodies carry connector openers ("FRONTMATTER GENERATION -- with area and subrole confirmed, all 12 fields are generated") and fix-and-retry workflow text ("If any gate fails, correct the specific field... and re-run the failed gate before advancing"). CONTRACTS order is canonical (FIELD-REGISTER before COLUMN-HEADER).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | File written to `.craft/roles/{area}/{subrole}.md` |
| C-02 | PASS | All 12 frontmatter fields present |
| C-03 | PASS | Phase 0 → Phase 1 routing intact |
| C-04 | PASS | Domain-specific field values |
| C-05 | PASS | Inertia companion surfaced / generated |
| C-06 | PASS | Lens.verify items are boolean checks ≥ 4 |
| C-07 | PASS | Domain specializations table in body |
| C-08 | PASS | Archetype checked against area pattern |
| C-09 | PASS | frame first-person, serves names beneficiary |
| C-10 | PASS | Domain-named column headers |
| C-11 | PASS | Companion file generated with template |
| C-12 | PASS | Interactive hold gates all three answers |
| C-13 | PASS | Phase 5 pre-write confirmation present |
| C-14 | PASS | Malformed input guard in Phase 0 |
| C-15 | PASS | In-phase gates at each content-producing phase |
| C-16 | PASS | AUDIT-CHECKLIST declared in CONTRACTS before phases |
| C-17 | PASS | CONTRACTs are named blocks |
| C-18 | PASS | Forward (Gated At) and backward ([ID] citations) present |
| C-19 | PASS | No rule restatement in phase steps; connector prose is process narrative, not CONTRACT rule content |
| C-20 | PASS | AUDIT-CHECKLIST items thin (CONTRACT name + scope only) |
| C-21 | PASS | All cited CONTRACTs have checklist entries |
| C-22 | PASS | Checklist header declares "no rule enumeration" format constraint |
| C-23 | PASS | No preamble; connector openers contain process narrative, not CONTRACT rule content |
| **C-24** | **FAIL** | Phase 0 uses TABLE; Phases 1–4 use inline `->` — mixed structural forms |
| **C-25** | **FAIL** | Connector openers ("INPUT GUARD -- this phase runs before...") and fix-and-retry workflow text ("If Gate 0 fails, apply the correction action...") exceed citation + artifact minimum |
| C-26 | PASS | FIELD-REGISTER defined before COLUMN-HEADER in CONTRACTS, matching Phase 3 < Phase 4 unconditional citation order |

**Aspirational passed:** 17 / 19  
**Score:** 60 + 30 + (17 × 10/19) = 60 + 30 + 8.95 = **98.95**

---

### V-02: C-24 + C-26 Combination

**Structure:** Phase 0 TABLE gate; Phases 1–4 inline — same mixed form as V-01. Phase bodies are minimum surface (identical to V-05). CONTRACTS block swaps COLUMN-HEADER before FIELD-REGISTER, inverting the Phase 3 < Phase 4 unconditional citation order.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Same as V-01 |
| C-08–C-22 | PASS | Same structure; phase bodies thin per V-05; AUDIT-CHECKLIST unchanged |
| C-23 | PASS | No preamble |
| **C-24** | **FAIL** | Phase 0 TABLE; Phases 1–4 inline — mixed structural form |
| C-25 | PASS | Phase bodies are minimum surface: "CONTRACT: X applied. [artifact]." — no connector prose, no fix-and-retry |
| **C-26** | **FAIL** | CONTRACTS block order: INPUT → INTERACTIVE → COLUMN-HEADER → FIELD-REGISTER — COLUMN-HEADER (Phase 4) defined before FIELD-REGISTER (Phase 3), inverting unconditional first-citation sequence |

**Aspirational passed:** 17 / 19  
**Score:** 60 + 30 + (17 × 10/19) = **98.95**

---

### V-03: Triple C-24 + C-25 + C-26

**Structure:** Phase 0 TABLE gate (C-24). Phase bodies carry connector openers + fix-and-retry text identical to V-01 (C-25). CONTRACTS block has COLUMN-HEADER before FIELD-REGISTER identical to V-02 (C-26). All three axes simultaneously violated.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Same as other variations |
| C-08–C-22 | PASS | Structural skeleton unchanged; thin checklist; CONTRACT blocks present |
| C-23 | PASS | No preamble rule summaries |
| **C-24** | **FAIL** | Phase 0 TABLE; Phases 1–4 inline — mixed form (same as V-01/V-02) |
| **C-25** | **FAIL** | Connector openers + fix-and-retry workflow text in all content-producing phases (same as V-01) |
| **C-26** | **FAIL** | COLUMN-HEADER before FIELD-REGISTER in CONTRACTS (same as V-02) |

**Cascade check:** C-25 implies C-19; C-19 passes (process narrative ≠ rule restatement). C-26 implies C-17; C-17 passes. No cascade amplification. All three deductions are independent.

**Aspirational passed:** 16 / 19  
**Score:** 60 + 30 + (16 × 10/19) = 60 + 30 + 8.42 = **98.42**

---

### V-04: C-23 Preamble Rule Quarantine Violation

**Structure:** A "How This Skill Works" section is inserted before the CONTRACTS block. It covers all five CONTRACTs in prose: input classification patterns, interactive hold prohibitions, inertia companion generation, all five FIELD-REGISTER rules, and column header prohibitions. Phases are minimum-surface inline citations (identical to V-05). CONTRACTS order is canonical. No gate form mixing.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Unchanged |
| C-08–C-22 | PASS | Thin phases, thin checklist, bidirectional traceability, homogeneous inline gates, canonical CONTRACT order |
| **C-23** | **FAIL** | "How This Skill Works" restates INPUT-ROUTING-RULES classification patterns, INTERACTIVE-HOLD prohibitions, FIELD-REGISTER register rules, COLUMN-HEADER prohibition list — rule content outside the three canonical locations (CONTRACT definition, phase citation, checklist item) |
| C-24 | PASS | All gates inline throughout Phases 0–4 |
| C-25 | PASS | Phase bodies: "CONTRACT: X applied. [one artifact/action reference]." — minimum surface confirmed against V-05 |
| C-26 | PASS | FIELD-REGISTER before COLUMN-HEADER in CONTRACTS; unconditional main-flow pair in correct Phase 3 < Phase 4 order |

**C-23 isolation confirmed:** C-19 PASS (thin phases), C-20 PASS (thin checklist), C-25 PASS (minimum surface). Preamble violation is the sole failure — C-23 fires independently when prerequisites are met.

**Aspirational passed:** 18 / 19  
**Score:** 60 + 30 + (18 × 10/19) = 60 + 30 + 9.47 = **99.47**

---

### V-05: Full Ceiling (Canonical Form)

**Structure:** R10 V-05 reproduced. Homogeneous inline gates. Minimum-surface phase bodies. CONTRACTS in unconditional first-citation sequence (FIELD-REGISTER → COLUMN-HEADER before INERTIA-ADVOCATE-TEMPLATE, which is conditional). No preamble.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | All essential and recommended satisfied |
| C-08–C-22 | PASS | All structural criteria satisfied: named CONTRACTs, bidirectional traceability, thin phases, thin checklist, coverage, self-documenting header |
| C-23 | PASS | No preamble; rule content confined to CONTRACTS block, phase citations, and checklist items |
| C-24 | PASS | All phases use inline `-> **Gate N [ID]:**` — no TABLE gates |
| C-25 | PASS | Every phase body: one CONTRACT citation + one artifact/action reference. No bridging prose, no fix-and-retry text |
| C-26 | PASS | CONTRACTS order: INPUT → INTERACTIVE → FIELD-REGISTER → COLUMN-HEADER (unconditional main-flow pair in Phase 3 < Phase 4 order); INERTIA (conditional, Phase 2) and AUDIT (auxiliary) placed after — correct exemption of non-unconditional citations |

**Aspirational passed:** 19 / 19  
**Score:** 60 + 30 + 10 = **100**

---

### Summary Table

| Variation | C-23 | C-24 | C-25 | C-26 | Essential | Recommended | Aspirational | Score | Rank |
|-----------|------|------|------|------|-----------|-------------|--------------|-------|------|
| V-05 | PASS | PASS | PASS | PASS | 5/5 | 2/2 | 19/19 | **100** | 1 |
| V-04 | FAIL | PASS | PASS | PASS | 5/5 | 2/2 | 18/19 | **99.47** | 2 |
| V-01 | PASS | FAIL | FAIL | PASS | 5/5 | 2/2 | 17/19 | **98.95** | 3= |
| V-02 | PASS | FAIL | PASS | FAIL | 5/5 | 2/2 | 17/19 | **98.95** | 3= |
| V-03 | PASS | FAIL | FAIL | FAIL | 5/5 | 2/2 | 16/19 | **98.42** | 5 |

---

### Excellence Signals — V-05

**Signal 1 — Unconditional main-flow scoping of C-26:** V-05 places INERTIA-ADVOCATE-TEMPLATE (Phase 2, conditional) and AUDIT-CHECKLIST (auxiliary pre-declaration) after the unconditional main-flow pair FIELD-REGISTER → COLUMN-HEADER. V-04 uses identical ordering and also passes C-26. This confirms that C-26's first-citation ordering requirement applies only to unconditional main-flow CONTRACT citations; conditional citations and pre-declaration blocks are exempt. The criterion is about the reader's navigational experience through the unconditional execution path — not a strict lexical sort of all CONTRACT citations including conditional branches.

**Signal 2 — C-24 and C-25 are orthogonal (R11 confirmation):** R10 had confirmed C-24+C-26 (V-03) and C-25+C-26 (V-04) as independent axes. R11 V-01 confirms C-24+C-25 is exactly 2× deduction with no cascade. The gate structural form (inline vs table) and phase surface area (minimum vs expanded) have no structural dependency. A variation that mixes gate forms can still achieve minimum phase surface; a variation with maximum phase surface can still use a single gate form consistently.

**Signal 3 — C-23 fires on preamble even when all three implied prerequisites pass:** V-04 confirms that a skill can satisfy C-19 (thin phases), C-20 (thin checklist), and C-25 (minimum surface) while still failing C-23. The quarantine criterion is not derivable from phase or checklist structure alone — it requires inspecting the full skill surface for rule content outside the three canonical locations. Preamble sections are a distinct failure mode not caught by phase or checklist criteria.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-26 applies to unconditional main-flow CONTRACT pairs only — conditional citations (INERTIA-ADVOCATE-TEMPLATE) and pre-declaration blocks (AUDIT-CHECKLIST) are exempt from first-citation sequence ordering, confirming the ordering rule governs the reader's unconditional execution path, not a global lexical sort"]}
```
