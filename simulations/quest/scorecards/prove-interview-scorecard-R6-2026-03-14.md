## prove-interview R6 Scorecard — Complete

**Written to:** `simulations/quest/scorecards/prove-interview-scorecard-R6-2026-03-14.md`

---

### Results

| Rank | Variation | Score | C-20 | C-21 | Golden |
|------|-----------|-------|------|------|--------|
| 1 | V-03 Both fixes, minimal | **155/155** | PASS | PASS | YES |
| 1 | V-04 Phrasing register | **155/155** | PASS | PASS | YES |
| 1 | V-05 All axes, maximum | **155/155** | PASS | PASS | YES |
| 4 | V-02 Tabular, no 6th DISPOSITION row | **152/155** | PARTIAL | PASS | YES |
| 5 | V-01 Prose + partial-compliance | **150/155** | PASS | FAIL | YES |

**Prediction accuracy: 4/5.** V-02 predicted ~150; actual 152 — C-20 PARTIAL earned 2 pts (not 0) because COLUMN POLICY rows 1-2 implicitly cover the partial-compliance conditions even without explicit labeling.

---

### Key findings

**C-20 and C-21 independence confirmed.** V-01 proves C-20 without C-21 (150). V-02 proves C-21 without full C-20 (152). Each independently worth exactly 5 pts.

**C-20 is block-specific.** COLUMN POLICY: implicit row coverage (rows ARE the partial-compliance conditions) scores 2 pts PARTIAL. Explicit framing required for full PASS. DISPOSITION: requires the explicit 6th row — no implicit path.

**Minimal combination sufficient.** V-03 = R5 V-04 + 6th DISPOSITION row + explicit partial-compliance COLUMN POLICY rows. 155/155 with no other changes. V-04/V-05 confirm register and enforcement depth are scoring-neutral at ceiling.

**V-05 architecture investment identified.** Incumbent Coupling Table (switching-cost baseline → Inertia Verdict Matrix Switch Cost column) is the pre-C-22 pattern — additive, non-displacing, cross-interview structural artifact.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["C-20 and C-21 are orthogonally independent and additively score exactly 5 pts each -- V-01 achieves 150 (C-20 PASS + C-21 FAIL); V-02 achieves 152 (C-20 PARTIAL 2pts + C-21 PASS); V-03 achieves 155 (both PASS); each criterion independently worth exactly 5 pts at ceiling", "C-20 is block-specific: COLUMN POLICY rows implicitly covering partial-compliance conditions score 2 pts PARTIAL; explicit framing ('Quote present but Rationale absent | ...' as named row with criterion IDs) required for PASS; DISPOSITION requires the explicit 6th row regardless of COLUMN POLICY status", "Minimal combination confirmed: 6th DISPOSITION row + explicit COLUMN POLICY partial-compliance rows added to R5 V-04 tabular baseline achieves 155/155 with no other changes; phrasing register (V-04) and enforcement depth (V-05) are scoring-neutral at ceiling", "Incumbent Coupling Table (V-05 exclusive) is the pre-C-22 architecture investment: switching-cost baseline per coupling factor feeds Inertia Verdict Matrix Switch Cost column; additive to evidence infrastructure without displacing required columns"]}
```
sent but Rationale absent | Interpretive rationale | C-10, C-16" and "Rationale present but Quote absent | Verbatim subject turn | C-14, C-16". Phase-gate language at step boundaries and "Do not proceed" enforcement language do not change criterion-level scoring.

**V-05 (155):** Maximum enforcement with Incumbent Coupling Table and switching-cost framing in Inertia Verdict. DISPOSITION: 6-row table with most detailed 6th condition (includes illustrative failure example — "a SKEPTIC-first roster whose Arc Signal reads 'S-01 said X; S-02 said Y' rather than 'prior signal (SKEPTIC S-01): ... / subsequent evidence (CHAMPION S-02): ...' fails C-18 on framing"). COLUMN POLICY: rows 1-2 carry most complete rationale explanations. Incumbent Coupling Table is additive — adds Switch Cost column to Inertia Verdict Matrix without displacing required evidence columns. Architecture depth above V-03 baseline: zero score impact at R6 ceiling.

---

## V-01: Role Sequence — C-20 Only (Prose Compliance Blocks)

*C-21 absent by design: both compliance blocks are prose-bullet format.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table: ID/Role-Title/Domain/Disposition. Subject 0 field table. All subjects declared before transcripts. |
| C-02 | PASS | 12 | Prior knowledge block per subject before transcript. Incumbent: assumption + confidence + threshold. S-01/S-02: domain knowledge + named stance + named threshold. |
| C-03 | PASS | 12 | A-turn instructions: "[S-01 response — role-grounded resistance]"; "[S-02 response — role-grounded advocacy]". |
| C-04 | PASS | 12 | Evidence Pull tables mandatory per subject. Signal/Quote/Confidence/Rationale schema enforced by COLUMN POLICY. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. COLUMN POLICY: "Rationale must answer 'why does this signal matter to the feature decision?'" |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject, three instances (Incumbent, S-01, S-02). |
| C-07 | PASS | 10 | Min 3 turns per subject. Q2 probes named stance from prior knowledge block. Q3 contrast note references prior-subject content. |
| C-08 | PASS | 10 | S-01 labeled SKEPTIC, S-02 labeled CHAMPION. Distinct domains and prior knowledge profiles. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: Pattern, Critical Contradiction Table, Tension Resolution, Inertia Verdict Matrix, Arc Signal, Prior Assumption Revisited. |
| C-10 | PASS | 5 | COLUMN POLICY: "Quote present but Rationale absent: FAILS C-10 (Evidence confidence rated — confidence score without accompanying rationale cannot be evaluated for basis)." |
| C-11 | PASS | 5 | Roster: SKEPTIC + CHAMPION. DISPOSITION REQUIREMENT: "No SKEPTIC: FAILS C-11 and FAILS C-17"; "No CHAMPION: FAILS C-11 and FAILS C-17." Arc Signal: "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):" |
| C-12 | PASS | 5 | Critical Contradiction Table: two rows, IE/HE source pairs, Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1: "[Opening — invite S-01's framing of TOPIC without leading toward resistance]". Prior knowledge block grounds subject before Q1. Consistent with R5 baseline C-13 PASS standard. |
| C-14 | PASS | 5 | COLUMN POLICY: "Rationale present but Quote absent: FAILS C-14 (Arc claims quote-anchored — rationale claims must be grounded in verbatim subject language)." |
| C-15 | PASS | 5 | Critical Contradiction Table: "S-01 SKEPTIC claim vs. S-02 CHAMPION claim" row cites "HE-#, HE-#" — one per side. |
| C-16 | PASS | 5 | COLUMN POLICY: "Quote present but Rationale absent: FAILS C-16 (Evidence columns non-substitutable — Quote does not substitute for Rationale; both must coexist simultaneously)." Non-substitutability with criterion IDs. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "Roster entry with no Disposition column value: FAILS C-17 (every human subject requires explicit per-subject label before transcripts begin — absence on any single entry fails the criterion)." Per-subject labels with criterion ID. |
| C-18 | PASS | 5 | S-01=SKEPTIC first. "SKEPTIC-FIRST REQUIREMENT: S-01 must be the SKEPTIC." Arc Signal: "Skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence." "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". DISPOSITION REQUIREMENT 6th condition: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18 (C-18 requires both structural ordering AND skeptic-prior Arc framing simultaneously; structural ordering alone satisfies only half the criterion)." Both structural and framing conditions present. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + 6 criterion-ID conditions. COLUMN POLICY: named block with full-absence, partial-compliance, and interpretive quality failure sections, all citing criterion IDs. Both blocks fully compliant with named-block + criterion-ID requirement. |
| C-20 | PASS | 5 | DISPOSITION: 6th condition present — "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18" ✓. COLUMN POLICY: explicit "Partial-compliance failure conditions (one column present, complementary column absent):" section with "Quote present but Rationale absent: FAILS C-10, FAILS C-16" and "Rationale present but Quote absent: FAILS C-14, FAILS C-16" ✓. Both blocks enumerate their respective partial-compliance variants. |
| C-21 | FAIL | 0 | **Absent by design.** Both compliance blocks use prose-bullet format. DISPOSITION REQUIREMENT: prose-list per-condition failure statements. COLUMN POLICY: prose-sectioned failure conditions. Neither block uses three-column tabular format. A C-19-compliant prose-bullet block fails C-21 by definition. |

**Composite: 150/155**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 60/65 (C-21 fail: 0)
All C-01..C-05 pass: YES | Golden: YES

---

## V-02: Output Format — C-21 Only (Tabular Blocks, No 6th DISPOSITION Row)

*C-20 PARTIAL by design: DISPOSITION table has 5 rows (no partial-compliance 6th row); COLUMN POLICY rows 1-2 implicitly cover partial-compliance.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table declared. All subjects have explicit ID, Role, Domain, Disposition before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. Incumbent: assumption + confidence + threshold. Subjects: domain knowledge + named stance + threshold. |
| C-03 | PASS | 12 | A-turn instructions specify role-grounded responses per disposition. |
| C-04 | PASS | 12 | Evidence Pull tables mandatory: IE-# (Incumbent), HE-1/HE-2 (S-01 SKEPTIC), HE-3/HE-4 (S-02 CHAMPION). |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. COLUMN POLICY: Rationale = "interpretive statement explaining why this signal matters." |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note cross-references prior subject. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION, distinct domains and prior knowledge. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set including pre-synthesis gate. |
| C-10 | PASS | 5 | COLUMN POLICY table: "Quote + Confidence present, no Rationale | Interpretive rationale per row | C-10 (Evidence confidence rated), C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT table: "No SKEPTIC | Explicit skeptic disposition | C-11, C-17"; "No CHAMPION | Explicit advocate disposition | C-11, C-17." Arc Signal (SKEPTIC-prior): "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):" |
| C-12 | PASS | 5 | Critical Contradiction Table: two named contradictions with source pairs and Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY table: "Rationale + Confidence present, no Quote | Verbatim source turn | C-14, C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table: "S-01 vs. S-02" row cites HE-# from both subjects. |
| C-16 | PASS | 5 | COLUMN POLICY table: five rows, all citing C-16. "Architectural column replaces Quote or Rationale | Non-substitutable base column | C-16." |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT table: "Roster entry with no Disposition column value | Per-subject disposition label | C-17"; "Disposition inferred from synthesis only | Roster-level declaration before transcripts | C-17." |
| C-18 | PASS | 5 | S-01=SKEPTIC first. "SKEPTIC-FIRST: S-01 must be SKEPTIC." DISPOSITION table row 5: "CHAMPION declared as S-01 | SKEPTIC-first structural ordering | C-18." Arc Signal: "Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence." "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". Both structural and framing conditions present. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + 5 criterion-ID tabular rows. COLUMN POLICY: named block + 5 criterion-ID tabular rows. Both blocks fully compliant. Tabular rows satisfy "itemized per-condition failure statements that name exactly what is absent and which criterion it violates." |
| C-20 | PARTIAL | 2 | COLUMN POLICY: rows 1-2 ARE the partial-compliance conditions — "Quote + Confidence present, no Rationale" = "Quote present but Rationale absent" ✓; "Rationale + Confidence present, no Quote" = "Rationale present but Quote absent" ✓. COLUMN POLICY block covers its partial-compliance variant. DISPOSITION: 5 rows only; row 5 is the full-absence condition ("CHAMPION as S-01"). Missing row 6: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18" ✗. One block covers partial-compliance (implicitly), the other does not. PARTIAL per rubric: "one of the two required blocks includes its respective partial-compliance failure variant; the other covers full-absence conditions only." Score: 2 pts. |
| C-21 | PASS | 5 | **Present by design.** DISPOSITION REQUIREMENT: Condition / What is absent / Criterion(s) violated three-column table ✓. COLUMN POLICY: same three-column table schema ✓. Both blocks use tabular format. |

**Composite: 152/155**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 62/65 (C-20 partial: 2 pts)
All C-01..C-05 pass: YES | Golden: YES

**Isolation finding:** C-21 PASS without full C-20 scores 152 (not 150 as predicted). The 2-pt C-20 PARTIAL contribution from COLUMN POLICY implicit coverage raises the floor above the predicted estimate. C-21 independently worth exactly 5 pts confirmed.

---

## V-03: Both Fixes, Minimal (C-20 + C-21)

*Minimal combination: 6th DISPOSITION row (C-20) + three-column tabular blocks (C-21).*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table: ID/Role-Title/Domain/Disposition. Subject 0 field table. All declared before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. |
| C-03 | PASS | 12 | A-turn instructions: "resistance grounded" (S-01), "advocacy grounded" (S-02). |
| C-04 | PASS | 12 | Evidence Pull tables required: IE-#, HE-1/HE-2 (S-01), HE-3/HE-4 (S-02). Pre-synthesis gate enforces completeness. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. Rationale requires interpretive content distinct from quote. |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note explicit. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION, distinct domains and prior knowledge. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set. |
| C-10 | PASS | 5 | COLUMN POLICY table: "Quote present but Rationale absent | Interpretive rationale per row | C-10 (Evidence confidence rated — confidence without interpretive basis), C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT table: "No SKEPTIC | Explicit skeptic disposition | C-11, C-17"; "No CHAMPION | Explicit advocate disposition | C-11, C-17." Arc Signal (SKEPTIC-prior) addresses both dispositions. |
| C-12 | PASS | 5 | Critical Contradiction Table: two rows, source pairs, Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY table: "Rationale present but Quote absent | Verbatim SUBJECT source turn | C-14 (Arc claims quote-anchored), C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table cites HE-# from both subjects per contradiction row. |
| C-16 | PASS | 5 | COLUMN POLICY table: "Quote present but Rationale absent" and "Architectural column displaces Quote or Rationale" both cite C-16. Non-substitutability with criterion ID in tabular form. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT table: "Roster entry with no Disposition column value | Per-subject disposition label | C-17"; "Disposition inferred from synthesis only | Roster-level declaration | C-17." |
| C-18 | PASS | 5 | S-01=SKEPTIC first. "SKEPTIC-FIRST: S-01 must be SKEPTIC. S-02 must be CHAMPION." DISPOSITION table row 6: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18 (C-18 requires both structural ordering AND skeptic-prior framing simultaneously — structural ordering alone satisfies only half the criterion)." Arc Signal: "Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence." "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". Both structural and framing conditions. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + 6 criterion-ID tabular rows. COLUMN POLICY: named block + 5 criterion-ID tabular rows. Both blocks fully compliant. |
| C-20 | PASS | 5 | DISPOSITION: 6th row present — "SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18 (requires both structural ordering AND skeptic-prior framing simultaneously — structural ordering alone satisfies only half the criterion)" ✓. COLUMN POLICY: row 1 = "Quote present but Rationale absent | Interpretive rationale per row | C-10, C-16" ✓; row 2 = "Rationale present but Quote absent | Verbatim SUBJECT source turn | C-14, C-16" ✓. Both blocks enumerate their respective partial-compliance variants explicitly. |
| C-21 | PASS | 5 | Both blocks use three-column tabular structure. DISPOSITION REQUIREMENT: Condition / What is absent / Criterion(s) violated schema, 6 rows ✓. COLUMN POLICY: same schema, 5 rows ✓. |

**Composite: 155/155**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 65/65
All C-01..C-05 pass: YES | Golden: YES

**Minimal-fix finding:** V-03 is the minimal change from R5 V-04 (tabular baseline) to achieve 155/155. Two targeted changes: (1) add 6th DISPOSITION table row for partial-compliance condition (C-20); (2) COLUMN POLICY rows 1-2 explicitly framed as "Quote present but Rationale absent" / "Rationale present but Quote absent" (C-20 COLUMN POLICY condition). Tabular format already present from R5 V-04 ancestry (C-21 cost = 0 additional work).

---

## V-04: Phrasing Register — Imperative Enforcement (C-20 + C-21)

*Same functional content as V-03; imperative register throughout.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. Explicit "Declare the incumbent first. Then declare all human subjects." No transcript before every subject has a Disposition label. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject. "State the prior knowledge block in full before the transcript begins. Do not embed it in answers." |
| C-03 | PASS | 12 | A-turn instructions: role-grounded responses per disposition. |
| C-04 | PASS | 12 | Evidence Pull tables required per subject: Signal/Quote/Confidence/Rationale. "Apply Column Policy to every row" enforced at each evidence section. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. COLUMN POLICY: "Rationale must answer 'why does this signal matter to the feature decision?'" |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q3 contrast note: "Name the specific incumbent assumption. Do not paraphrase generically." |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION, distinct domains. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set. Gate: "If any row is missing a column, name the criterion violated before proceeding." |
| C-10 | PASS | 5 | COLUMN POLICY table: "Quote present but Rationale absent | Interpretive rationale | C-10 (confidence without interpretive basis), C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT table: "No SKEPTIC | Explicit skeptic disposition | C-11, C-17"; "No CHAMPION | Explicit advocate disposition | C-11, C-17." Arc Signal (SKEPTIC-prior). |
| C-12 | PASS | 5 | Critical Contradiction Table: "rank by evidential weight, most important first." Two rows with source pairs and Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY table: "Rationale present but Quote absent | Verbatim subject turn | C-14 (arc claims must be quote-grounded), C-16." "[Verbatim quote — exact words from A1, A2, or A3]" in evidence table schema. |
| C-15 | PASS | 5 | Critical Contradiction Table cites HE-# from both subjects. |
| C-16 | PASS | 5 | COLUMN POLICY table: "Added column displaces Quote or Rationale | Non-substitutable base column | C-16 (supplemental columns are additive only — displacement fails regardless of column value)." |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT table: "Any roster entry with no Disposition value | Per-subject disposition label | C-17"; "Disposition identified only in synthesis | Roster-level pre-transcript declaration | C-17." |
| C-18 | PASS | 5 | "SKEPTIC must be S-01. CHAMPION must be S-02. Do not invert this order." DISPOSITION table row 6: "SKEPTIC in S-01 position but Arc Signal compares subjects symmetrically | Skeptic-prior Arc framing | C-18 (structural ordering alone is half-compliance; framing must derive from that ordering)." Arc Signal: "This is not a symmetric comparison. Derive the arc from the prior-signal structure." "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". Both conditions. |
| C-19 | PASS | 5 | Both named blocks with tabular criterion-ID failure conditions. |
| C-20 | PASS | 5 | DISPOSITION: 6th row = "SKEPTIC in S-01 position but Arc Signal compares subjects symmetrically | Skeptic-prior Arc framing | C-18" ✓. COLUMN POLICY: row 1 = "Quote present but Rationale absent | Interpretive rationale | C-10, C-16" ✓; row 2 = "Rationale present but Quote absent | Verbatim subject turn | C-14, C-16" ✓. Both blocks enumerate their partial-compliance variants. |
| C-21 | PASS | 5 | Both blocks use three-column tabular format. DISPOSITION REQUIREMENT: 6 rows ✓. COLUMN POLICY: 5 rows ✓. |

**Composite: 155/155**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 65/65
All C-01..C-05 pass: YES | Golden: YES

**Register finding:** Imperative enforcement phrasing is scoring-neutral at 155 ceiling. Phase-gate language ("Do not proceed past any gate"), second-person instructions ("Produce all four. Do not omit any."), and explicit cross-reference requirements ("Name the claim from S-01. Do not refer generically") add enforcement clarity without changing criterion-level outcomes. Pre-next-criterion architecture value only.

---

## V-05: All Axes — Maximum Enforcement (C-20 + C-21 + Full Prior Criteria)

*All five axes: SKEPTIC-first, tabular blocks, lifecycle enforcement, imperative register, incumbent coupling.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. "SKEPTIC-FIRST REQUIREMENT: This is not cosmetic." Explicit rationale for why ordering matters in roster header. |
| C-02 | PASS | 12 | Most specific prior knowledge instructions. Incumbent: "named condition — specific, not 'more evidence'". Human subjects: "domain-grounded — specific to their role and experience." |
| C-03 | PASS | 12 | A-turn instructions specify role-grounded full responses. |
| C-04 | PASS | 12 | Evidence Pull tables required. Pre-synthesis gate: "If a row is missing a column, name the specific criterion violated before proceeding." |
| C-05 | PASS | 12 | COLUMN POLICY: "Rationale must answer 'why does this signal matter to the topic decision?' — not a restatement of the quote." Most explicit grounding requirement. |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. "Open without leading toward resistance/advocacy" reduces interviewer-lead contamination. |
| C-07 | PASS | 10 | Min 3 turns. Q3 contrast note: "Name the claim from S-01. Do not refer generically to 'the skeptic's concerns.'" Most specific cross-subject referencing. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION. Most explicit knowledge-basis differentiation. |
| C-09 | PASS | 5 | Arc Signal: "Pattern: Do not summarize individual interviews — synthesize across them." Grounding check: "If the conclusion references only one subject, it is not an arc — revise before filing." |
| C-10 | PASS | 5 | COLUMN POLICY: "a confidence score without accompanying rationale cannot be evaluated for basis" — most explicit rationale-basis statement. |
| C-11 | PASS | 5 | Arc Signal explicitly grounds each voice in HE-#: "Prior signal (SKEPTIC S-01): [... Ground this in HE-1 and HE-2]." |
| C-12 | PASS | 5 | Critical Contradiction Table: "[S-01 SKEPTIC claim vs. S-02 CHAMPION claim — the core arc tension]" with "[What is at risk if this tension persists into implementation]" — forward-looking stakes framing. |
| C-13 | PASS | 5 | Most explicit current-practice Q1: "Opening — ask what the incumbent does today, before any feature is introduced. This is the current-practice anchor question. Do not lead with the feature." Prior knowledge block adds "Current-practice anchor" field. |
| C-14 | PASS | 5 | "[Verbatim quote — exact words from A1, A2, or A3 — not paraphrased]" — most explicit verbatim requirement. |
| C-15 | PASS | 5 | Critical Contradiction Table cites HE-# from both subjects. Grounding check enforces both-sides citation a second time at Arc conclusion level. |
| C-16 | PASS | 5 | COLUMN POLICY: "adding Phase, Theme, Category, or any supplemental column is permitted only if it supplements the four required columns; any addition that displaces Quote or Rationale from any row violates non-substitutability regardless of the addition's descriptive value." Most complete non-substitutability statement. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "Any roster entry with no Disposition column value | Per-subject disposition label | C-17 (every human subject requires explicit per-subject label before transcripts begin — absence on any single entry fails the criterion)." Most specific per-entry enforcement. |
| C-18 | PASS | 5 | "SKEPTIC-FIRST REQUIREMENT: This is not cosmetic." DISPOSITION table row 6: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18 (C-18 requires both structural ordering AND skeptic-prior Arc framing simultaneously; structural ordering alone satisfies only half the criterion — a SKEPTIC-first roster whose Arc Signal reads 'S-01 said X; S-02 said Y' rather than 'prior signal (SKEPTIC S-01): ... / subsequent evidence (CHAMPION S-02): ...' fails C-18 on framing)." Illustrative failure example unique to V-05. Arc Signal: "This is not a symmetric comparison between two equal voices." |
| C-19 | PASS | 5 | Both named blocks with the most detailed tabular criterion-ID conditions and explanatory parentheticals. |
| C-20 | PASS | 5 | DISPOSITION: 6th row with most detailed explanation including illustrative failure example ✓. COLUMN POLICY: rows 1-2 = "Quote present but Rationale absent | Interpretive rationale per row | C-10 (...a confidence score without accompanying rationale cannot be evaluated for basis), C-16 (...Quote does not substitute for Rationale; both must coexist simultaneously in the same row)" and "Rationale present but Quote absent | Verbatim SUBJECT source turn | C-14 (...rationale claims must be grounded in verbatim subject language; paraphrasing does not satisfy the quote requirement), C-16 (...Rationale does not substitute for Quote; both must coexist simultaneously)" ✓. Both blocks enumerate partial-compliance variants with maximum explanatory depth. |
| C-21 | PASS | 5 | Both blocks use three-column tabular format. DISPOSITION REQUIREMENT: 6 rows ✓. COLUMN POLICY: 5 rows ✓. |

**Composite: 155/155**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 65/65
All C-01..C-05 pass: YES | Golden: YES

**Excellence signals above V-03 baseline (zero score impact; architecture depth only):**
1. Illustrative failure example in DISPOSITION 6th row: explicit contrast between failing framing ("S-01 said X; S-02 said Y") and compliant framing ("prior signal (SKEPTIC S-01): ... / subsequent evidence (CHAMPION S-02): ...") — prevents misinterpretation without changing scoring
2. Incumbent Coupling Table: new structural artifact tracking switching-cost baseline per coupling factor, fed into Inertia Verdict Matrix Switch Cost column — additive to evidence infrastructure, no column displacement
3. "Current-practice anchor" field in prior knowledge block + explicit Q1 instruction — most structural C-13 enforcement; other variations satisfy C-13 via open-ended Q1 alone
4. Grounding check at Arc conclusion level: "If the conclusion references only one subject, it is not an arc — revise before filing." — enforces both-sides citation at synthesis output, not just at table-population level
5. Most detailed COLUMN POLICY rationale explanations (parentheticals explaining WHY each criterion applies) — self-documenting compliance block

---

## Cross-Variation Summary

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 | 12 | 12 | 12 | 12 | 12 |
| C-02 | 12 | 12 | 12 | 12 | 12 |
| C-03 | 12 | 12 | 12 | 12 | 12 |
| C-04 | 12 | 12 | 12 | 12 | 12 |
| C-05 | 12 | 12 | 12 | 12 | 12 |
| C-06 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 10 | 10 | 10 | 10 | 10 |
| C-09 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 5 | 5 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 |
| C-19 | 5 | 5 | 5 | 5 | 5 |
| C-20 | **5** | **2** | **5** | **5** | **5** |
| C-21 | **0** | **5** | **5** | **5** | **5** |
| **Total** | **150** | **152** | **155** | **155** | **155** |

All 5 variations: Golden. Prediction accuracy: 4/5 (V-02 off by ~2 pts — C-20 PARTIAL contribution higher than estimated).

---

## Excellence Signals (from top-scoring variations)

**Pattern 1: C-20 and C-21 are orthogonally independent and additively score exactly 5 pts each**
V-01 demonstrates C-20 PASS without C-21 (150). V-02 demonstrates C-21 PASS with C-20 PARTIAL (152). V-03 demonstrates both PASS (155). Independence confirmed. Each criterion independently worth exactly 5 pts at ceiling.

**Pattern 2: C-20 is block-specific — COLUMN POLICY and DISPOSITION partial-compliance are separately required**
V-02 shows COLUMN POLICY rows implicitly covering the partial-compliance condition (rows 1-2 ARE "Quote present but Rationale absent" and "Rationale present but Quote absent") while DISPOSITION lacks the 6th row. Result: C-20 PARTIAL (2 pts). Both blocks must explicitly enumerate their respective partial-compliance variants for C-20 PASS. Implicit coverage in COLUMN POLICY scores 2 pts; explicit framing (V-03+) is required for full PASS.

**Pattern 3: Minimal combination is sufficient — V-03 confirms 155/155 with minimal delta from R5 V-04**
Adding the 6th DISPOSITION row and explicitly framing COLUMN POLICY rows 1-2 as "Quote present but Rationale absent" / "Rationale present but Quote absent" to R5 V-04 (already tabular) achieves 155/155. No other changes required. Register (V-04) and full enforcement depth (V-05) add zero score impact.

**Pattern 4: Incumbent Coupling Table is the V-05 architecture investment for next-generation criteria**
V-05 adds a new structural artifact (Incumbent Coupling Table with switching-cost ratings per coupling factor) that feeds into the Inertia Verdict Matrix as a Switch Cost column. This is additive to the four required evidence columns — no displacement. The pattern is: cross-interview structural artifacts that bridge the incumbent baseline to human subject evidence and synthesize at verdict level. Candidate for future C-22 extraction.

**Pattern 5: C-13 satisfies at two levels — open-ended Q1 (all variations) vs. explicit current-practice anchor (V-05 only)**
All variations pass C-13 through open-ended Q1 + prior knowledge block (consistent with R5 baseline). V-05 uniquely adds an explicit "Current-practice anchor" field in the prior knowledge block and changes Q1 instruction to "ask what the incumbent does today, before any feature is introduced." This creates a structural two-level C-13: behavioral anchor declared pre-transcript (C-13 enhancement) vs. open-ended Q1 post-transcript (C-13 floor). Not promoted to a new criterion because all variations already pass C-13; V-05's approach is enforcement-depth only.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["C-20 and C-21 are orthogonally independent and additively score exactly 5 pts each -- V-01 achieves 150 (C-20 PASS + C-21 FAIL); V-02 achieves 152 (C-20 PARTIAL 2pts + C-21 PASS); V-03 achieves 155 (both PASS); each criterion independently worth exactly 5 pts at ceiling", "C-20 is block-specific: COLUMN POLICY rows implicitly covering partial-compliance conditions score 2 pts PARTIAL; explicit framing ('Quote present but Rationale absent | ...' as named row with criterion IDs) required for PASS; DISPOSITION requires the explicit 6th row regardless of COLUMN POLICY status", "Minimal combination confirmed: 6th DISPOSITION row + explicit COLUMN POLICY partial-compliance rows added to R5 V-04 tabular baseline achieves 155/155 with no other changes; phrasing register (V-04) and enforcement depth (V-05) are scoring-neutral at ceiling", "Incumbent Coupling Table (V-05 exclusive) is the pre-C-22 architecture investment: switching-cost baseline per coupling factor feeds Inertia Verdict Matrix Switch Cost column; additive to evidence infrastructure without displacing required columns"]}
```
