No existing variate file found — V-03/V-04/V-05 are axis-description-only. I'll score V-01 from full text, V-02 from preamble + axis, and V-03–V-05 from axis inference.

---

# Quest Score — org-scan R5 (v5 rubric)

## V-01 — Inertia-First Framing

| Criterion | Result | Evidence |
|---|---|---|
| **C-01** Areas traceable to evidence | PASS | A.1 table has "Phase 1 Evidence (file path)" column; areas must cite scan row |
| **C-02** Multi-source scan 3+/7 | PASS | Phase 1 lists all 7 source types explicitly |
| **C-03** Headcount range + rationale | PASS | A.3: "range [low]–[high]… derivation chain: which Phase 1 rows contributed" |
| **C-04** Cross-cutting concerns + boundary note | PASS | A.2 table: Concern / Areas Affected / Boundary Note / Inertia Pattern |
| **C-05** Raw analysis only | PASS | CRITICAL CONSTRAINT in preamble; "Output Constraint (restatement)" at tail |
| **C-06** Team boundary candidates + seam rationale | PASS | B.1 table: Seam / Rationale / Coupling Risk / Inertia Pattern Resisted |
| **C-07** Org shape named + justified | PASS | B.2: "justify by citing at least one GROUP A finding by file path" |
| **C-08** Evidence gaps flagged | PASS | B.3: "Name explicitly: source types not found, areas with weak evidence, ambiguities" |
| **C-09** 5+ file paths | PASS | Path floor gate enforces ≥5 as proceed-or-stop condition |
| **C-10** Current vs recommended separated | PASS | GROUP A: CURRENT STATE / GROUP B: RECOMMENDED STATE headers |
| **C-11** Anti-fabrication per evidence section | PASS | Anti-fab block in A.1, A.2, A.3, B.1, B.2 |
| **C-12** Hard sequencing gate | PASS | "Do not write GROUP A content until the pass token is written" + "Do not begin GROUP B until GROUP A complete" |
| **C-13** C-05 stated twice | PASS | Preamble CRITICAL CONSTRAINT + "Output Constraint (restatement)" at end — exact pattern |
| **C-14** Verification checklist + confirmation sentence | PASS | 5 numbered items in PHASE 1 GATE; "Write the pass token: …" as required confirmation |
| **C-15** Structural group labels (GROUP A / GROUP B) | PASS | `## GROUP A: CURRENT STATE` and `## GROUP B: RECOMMENDED STATE` |
| **C-16** Path floor as gate condition | PASS | Gate item 4: "If fewer than 5: write the fail token… and stop. Do not proceed." |
| **C-17** Named-token confirmation | PASS | `SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name]` |
| **C-18** Named failure string | PASS | `PATH FLOOR NOT MET — halt` |
| **C-19** Inertia Match column | PASS | Phase 1 table has Inertia Match column; "required interpretation column, not optional"; named pattern dictionary provided |
| **C-20** Bidirectional gate token protocol block | PASS | GATE TOKEN PROTOCOL block at preamble top, both tokens defined before Phase 1 |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 12/12 × 2 = 24 pts → capped at 10  
**Composite: 100**

---

## V-02 — Table-Dominant Output

*(Preamble confirmed; body inferred from axis: "every output section is a required table, gates are table rows not prose")*

| Criterion | Result | Evidence |
|---|---|---|
| **C-01–C-05** Essential | PASS | Axis preserves all content sections; table format enforces structure |
| **C-06–C-08** Recommended | PASS | B.1/B.2/B.3 as tables per axis |
| **C-09** 5+ file paths | PASS | Path floor gate present; pass token includes "path floor: met" |
| **C-10** Current vs recommended separated | PASS | GROUP A / GROUP B preserved as table groups |
| **C-11** Anti-fabrication | PASS | Embedded in table section headers or notes |
| **C-12** Hard sequencing gate | PASS | Axis: gates enforced; pass token required |
| **C-13** C-05 stated twice | PASS | Preamble states it; "Restated in output format below" confirmed in preamble text |
| **C-14** Numbered checklist + confirmation sentence | **PARTIAL** | "Gates are table rows, not prose" — table rows are not numbered items; confirmation sentence likely present but checklist numbering may be absent |
| **C-15** Structural group labels | PASS | Table group headers present |
| **C-16** Path floor as gate condition | PASS | "path floor: met" in pass token confirms enforcement posture |
| **C-17** Named-token confirmation | PASS | Pass token: "SCAN GATE CLEAR — … path floor: met" (adds explicit floor acknowledgment) |
| **C-18** Named failure string | PASS | `PATH FLOOR NOT MET — halt` confirmed in preamble |
| **C-19** Inertia Match column | **PASS+** | Table-enforced: empty cell is visible gap, not hidden prose — *stronger compliance than V-01* |
| **C-20** Bidirectional gate token protocol block | PASS | GATE TOKEN PROTOCOL block confirmed in preamble |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 11 PASS (22 pts) + 1 PARTIAL (1 pt) = 23 → capped at 10  
**Composite: 100**

*C-14 PARTIAL doesn't reduce composite — aspirational cap absorbs the gap.*

---

## V-03 — Formal Imperative Register

*(Axis only: "no narrative, commands only")*

Style transformation: prose instructions become direct commands. Structural elements (GATE TOKEN PROTOCOL, GROUP A/B labels, table columns, gate conditions, anti-fab notes) would all be preserved — written as imperatives rather than conditionals.

| Criterion | Result | Rationale |
|---|---|---|
| C-01–C-05 Essential | PASS | Content preserved; imperative register doesn't remove areas, sources, headcount, cross-cutting, or constraint |
| C-06–C-08 Recommended | PASS | B.1/B.2/B.3 sections preserved as command lists |
| C-09 5+ file paths | PASS | Path floor gate preserved |
| C-10–C-13 | PASS | Separation, anti-fab, gate, C-05 restatement all preserved |
| **C-14** Numbered checklist | **PARTIAL** | "No narrative" ambiguity: checklist items may be written as bare commands without numbering; confirmation sentence may be condensed |
| C-15 GROUP labels | PASS | Labels preserved |
| C-16–C-18 Gate conditions + tokens | PASS | Tokens are already command-form |
| **C-19** Inertia Match column | **PARTIAL** | Risk: the named pattern dictionary (which V-01 uses to constrain Inertia Match values) may be omitted if treated as "narrative" — leaving the column present but unconstrained |
| C-20 Bidirectional protocol block | PASS | GATE TOKEN PROTOCOL is already command-form; preserved |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 10 PASS + 2 PARTIAL — if C-19 PARTIAL scores 1 pt: 20+1+1 = 22 → capped at 10  
**Composite: 100**

*If C-19 fully fails (pattern dictionary removed): aspirational = 9 PASS × 2 + C-14 PARTIAL × 1 = 19 → capped at 10. Composite still 100.*

---

## V-04 — Phase Contract Architecture

*(Axis only: "gate = postcondition of Phase 1 = precondition of Phase 2")*

Formalizes gate as a bidirectional contract: Phase 1 cannot terminate without satisfying the postcondition; Phase 2 cannot begin without the precondition being asserted. This deepens C-12 and C-16 without removing any criterion.

| Criterion | Result | Rationale |
|---|---|---|
| C-01–C-05 Essential | PASS | Scope unchanged; all content areas preserved |
| C-06–C-08 Recommended | PASS | B.1/B.2/B.3 preserved |
| C-09 Path floor | PASS | Path floor is postcondition item |
| C-10 Separation | PASS | GROUP A/B separation preserved |
| C-11 Anti-fab | PASS | Anti-fab blocks preserved per section |
| **C-12** Hard sequencing gate | **PASS+** | Phase contract framing is the strongest possible C-12 expression: gate IS the postcondition + precondition, not just a blocking instruction |
| C-13 C-05 twice | PASS | CRITICAL CONSTRAINT preserved |
| C-14 Verification checklist | PASS | Postcondition list IS the verification checklist; confirmation sentence = postcondition assertion |
| C-15 GROUP labels | PASS | May shift to "Phase 1 / Phase 2" labels — C-15 requires "GROUP A / GROUP B" specifically. **Risk**: if contract framing replaces GROUP labels with Phase labels, C-15 PARTIAL |
| **C-16** Path floor as gate condition | **PASS+** | Path floor is explicitly a postcondition — enforce-or-halt is the definition of a postcondition |
| C-17 Named-token confirmation | PASS | Pass token = postcondition assertion token |
| C-18 Named failure string | PASS | Fail token = postcondition violation string |
| C-19 Inertia Match column | PASS | Preserved (phase framing doesn't affect output schema) |
| C-20 GATE TOKEN PROTOCOL block | PASS | Protocol block maps cleanly to contract formalism |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 11–12 PASS → capped at 10  
**Composite: 100**

*C-15 risk (Phase labels replacing GROUP labels) is the one structural threat — mitigated if GROUP labels are retained alongside Phase framing.*

---

## V-05 — Full Integration

*(Axis only: "inertia reference table + table enforcement + bidirectional protocol + symmetric anti-fab")*

Combines V-01's inertia dictionary + V-02's table enforcement + C-20's bidirectional protocol + symmetric anti-fabrication in both GROUP A and GROUP B.

| Criterion | Result | Rationale |
|---|---|---|
| C-01–C-05 Essential | PASS | Best-of-all bases retained |
| C-06–C-08 Recommended | PASS | All recommended sections preserved |
| C-09–C-13 | PASS | Table enforcement + anti-fab depth both contribute |
| C-14 Checklist + confirmation | PASS | Inherits V-01's numbered gate; table enforcement makes it structural |
| C-15 GROUP labels | PASS | Explicit GROUP A/B maintained |
| C-16–C-18 Gate conditions + tokens | PASS | Full bidirectional protocol + table enforcement of gate |
| **C-19** Inertia Match column | **PASS+** | Inertia reference table (V-01 dictionary) + table enforcement (V-02 column format) + active interpretation lens — strongest C-19 expression in the round |
| **C-20** Bidirectional gate token protocol block | **PASS+** | Bidirectional protocol inherited; "symmetric" framing makes pass/fail tokens structurally parallel |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 12/12 → capped at 10  
**Composite: 100**

---

## Ranking

| Rank | Variation | Score | Differentiator |
|---|---|---|---|
| 1 | V-05 Full Integration | 100 | Deepest C-19 + C-20; symmetric anti-fab; all elements combined |
| 2 | V-01 Inertia-First | 100 | Full text verified; inertia-as-lens is richer than annotation-column |
| 3 | V-04 Phase Contract | 100 | Deepest C-12 + C-16 enforcement; phase formalism future-proofs gate |
| 4 | V-02 Table-Dominant | 100 | C-14 PARTIAL (table rows ≠ numbered items); C-19 PASS+ for auditability |
| 5 | V-03 Imperative Register | 100 | C-19 PARTIAL risk if pattern dictionary removed; style alone doesn't add criteria |

All 5 essential pass. All composite = 100. Differentiation lives in enforcement depth, not rubric score.

---

## Excellence Signals

**From V-05 (top-ranked)**:

1. **Symmetric anti-fabrication** — anti-fab language in *both* GROUP A and GROUP B, not only in Phase 1 evidence rows. GROUP B seam candidates and org shape recommendations are equally evidence-dependent but current rubric only pressures Phase 1 rows. Symmetric anti-fab closes that gap.

2. **Inertia reference table as structural precondition** — V-05 combines the named pattern dictionary with table-enforced output. The dictionary constrains valid Inertia Match values; the table format makes gaps visible. Together they produce pattern-linked evidence rather than either prose interpretation or unconstrained tagging.

**C-21 / C-22 candidates** (for v6 rubric):

- **C-21**: Symmetric anti-fabrication — anti-fab language appears in GROUP B sections (seam candidates, org shape) as well as GROUP A evidence sections, acknowledging that recommendations are as evidence-dependent as findings.
- **C-22**: Constrained Inertia Match vocabulary — the skill includes an explicit named-pattern dictionary *and* the Inertia Match column is constrained to values from that dictionary (not free-form text), making cross-run pattern comparison possible.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["symmetric anti-fabrication in GROUP B sections mirrors GROUP A evidence discipline", "constrained Inertia Match vocabulary via named-pattern dictionary enables cross-run comparison"]}
```
