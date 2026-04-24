```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["C-22 PARTIAL is source-asymmetric: named Incumbent Coupling Table without Switch Cost column (source present, derived absent) scores 3 pts PARTIAL; Switch Cost column without named Incumbent Coupling Table (derived present, source absent) scores 2 pts PARTIAL -- the table is the grounding artifact with structural content; the column is derived propagation; source completeness > derived propagation in PARTIAL band", "Minimum C-22 PASS requires explicit attribution, not coexistence: one coupling factor + one rating + explicit sourced-from statement in Switch Cost column entry + lifecycle gate preventing post-hoc population of coupling table; gate is the structural enforcement mechanism distinguishing minimum PASS from PARTIAL", "COLUMN POLICY additive-only row extends named compliance infrastructure to C-22 domain: V-05 adds a row stating Switch Cost column supplements without displacing Evidence Pull columns; C-16 violations in Evidence tables remain independent of C-22 status; self-documenting compliance block that explicitly enforces the C-22/C-16 boundary", "Maximum C-22 architecture propagates to Arc Signal narrative: Incumbent Coupling Table -> Switch Cost column -> per-factor incumbent friction claim in Arc Signal is the V-05 terminus; candidate for C-23 extraction as per-factor incumbent friction named in synthesis narrative"]}
```

---

**R7 Summary**

| Rank | Variation | Score | C-22 |
|------|-----------|-------|------|
| 1 | V-04 Minimal PASS | **160/160** | PASS (5) |
| 1 | V-05 Maximum PASS | **160/160** | PASS (5) |
| 3 | V-02 Table, no Switch Cost | **158/160** | PARTIAL (3) |
| 4 | V-03 Switch Cost, no table | **157/160** | PARTIAL (2) |
| 5 | V-01 C-22 absent | **155/160** | FAIL (0) |

**Prediction accuracy: 4/5.** V-02 was predicted ~157; actual 158 — source > derived asymmetry resolves the PARTIAL band at 3 not 2 for the table-present case. All others exact.

**Key finding:** C-22 PARTIAL is source-asymmetric. The Incumbent Coupling Table (source artifact with per-factor structural data) without the Switch Cost column scores 3 pts. The Switch Cost column (derived artifact) without the table scores 2 pts. The rubric didn't specify asymmetry explicitly, but the grounding principle resolves it: structural content > propagation in PARTIAL credit. This is the primary new pattern for R7.
ent, source absent) scores 2 pts PARTIAL -- the table is the grounding artifact with structural content; the column is derived propagation; source completeness > derived propagation in PARTIAL band", "Minimum C-22 PASS requires explicit attribution, not coexistence: one coupling factor + one rating + explicit sourced-from statement in Switch Cost column entry + lifecycle gate preventing post-hoc population of coupling table; gate is the structural enforcement mechanism distinguishing minimum PASS from PARTIAL", "COLUMN POLICY additive-only row extends named compliance infrastructure to C-22 domain: V-05 adds a row stating Switch Cost column supplements without displacing Evidence Pull columns; C-16 violations in Evidence tables remain independent of C-22 status; self-documenting compliance block that explicitly enforces the C-22/C-16 boundary", "Maximum C-22 architecture propagates to Arc Signal narrative: Incumbent Coupling Table -> Switch Cost column -> per-factor incumbent friction claim in Arc Signal is the V-05 terminus; candidate for C-23 extraction as per-factor incumbent friction named in synthesis narrative"]}
```

---

## Baseline

R6 established 155/155 as the ceiling for C-01..C-21. R7 adds C-22 (5 pts), raising the ceiling to 160. All R7 variations carry C-01..C-21 at ceiling; the only variable is C-22 architecture.

**C-22 floor prerequisite check (all variations):**
- C-09: PASS in all variations — synthesis section with Inertia Verdict Matrix present.
- C-13: PASS in all variations — incumbent interview opens with neutral current-practice Q1 within its own block regardless of transcript ordering. C-22 is gradable in all five.

---

## V-01: C-22 Absent

*C-22 absent by design. Full ceiling on C-01..C-21.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table: ID/Role-Title/Domain/Disposition. All subjects declared before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. Incumbent baseline + named stance/threshold per human subject. |
| C-03 | PASS | 12 | A-turn instructions: role-grounded resistance (S-01), advocacy (S-02). |
| C-04 | PASS | 12 | Evidence Pull tables mandatory per subject; COLUMN POLICY enforced. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. Rationale answers "why does this signal matter." |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject; three instances. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note references prior-subject content. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION; distinct domains and prior knowledge profiles. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: Pattern, Critical Contradiction Table, Tension Resolution, Inertia Verdict Matrix, Arc Signal, Prior Assumption Revisited. |
| C-10 | PASS | 5 | COLUMN POLICY: "Quote present but Rationale absent: FAILS C-10, C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT: SKEPTIC + CHAMPION rows. Arc Signal: "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". |
| C-12 | PASS | 5 | Critical Contradiction Table: two named contradictions ranked by evidential weight, source pairs, Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1: "what do you do today, before any feature is introduced." Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY: "Rationale present but Quote absent: FAILS C-14, C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table cites HE-# from both subjects per contradiction row. |
| C-16 | PASS | 5 | COLUMN POLICY: "Added column displaces Quote or Rationale: FAILS C-16." Non-substitutability with criterion ID. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "Roster entry with no Disposition value: FAILS C-17." Per-subject labels before transcripts. |
| C-18 | PASS | 5 | SKEPTIC = S-01. DISPOSITION row 6: partial-compliance C-18 condition. Arc Signal skeptic-prior framing. Both structural and framing conditions. |
| C-19 | PASS | 5 | Both named blocks (COLUMN POLICY + DISPOSITION REQUIREMENT) with tabular criterion-ID failure statements. |
| C-20 | PASS | 5 | DISPOSITION: 6th row present. COLUMN POLICY: rows 1-2 explicitly "Quote present but Rationale absent" / "Rationale present but Quote absent." Both PASS. |
| C-21 | PASS | 5 | Both blocks three-column tabular format: Condition / What is absent / Criterion(s) violated. |
| C-22 | FAIL | 0 | **Absent by design.** No Incumbent Coupling Table. No Switch Cost column in Inertia Verdict Matrix. C-09 + C-13 floor met but neither conjunction element present. |

**Composite: 155/160**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 65/70 (C-22 fail: 0)
All C-01..C-05 pass: YES | Golden: YES

---

## V-02: C-22 PARTIAL-A — Named Table, No Switch Cost Column

*C-22 PARTIAL-A: Incumbent Coupling Table present with per-factor ratings; Switch Cost column in Inertia Verdict Matrix absent.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table declared. All subjects with ID/Role/Domain/Disposition before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. Incumbent baseline fields present. |
| C-03 | PASS | 12 | A-turn instructions specify role-grounded responses per disposition. |
| C-04 | PASS | 12 | Evidence Pull tables mandatory. COLUMN POLICY enforced. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. Rationale = interpretive statement. |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note cross-references prior subject. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION. Distinct domains and prior knowledge. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set including Inertia Verdict Matrix. |
| C-10 | PASS | 5 | COLUMN POLICY table: partial-compliance row: "Quote + Confidence, no Rationale: C-10, C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT table: SKEPTIC + CHAMPION rows; 6th row for C-18. Arc Signal skeptic-prior. |
| C-12 | PASS | 5 | Critical Contradiction Table: two named contradictions ranked, source pairs, Stakes column. |
| C-13 | PASS | 5 | Open-ended current-practice Q1 for incumbent. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY table: "Rationale + Confidence, no Quote: C-14, C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table cites source pairs from both subjects per contradiction. |
| C-16 | PASS | 5 | COLUMN POLICY table: "Architectural column displaces Quote or Rationale: C-16." Additive-only rule enforced. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT table: "Roster entry with no Disposition value: C-17." Per-subject labels. |
| C-18 | PASS | 5 | SKEPTIC = S-01. 6th DISPOSITION row: partial-compliance framing for C-18. Arc Signal skeptic-prior. Both conditions. |
| C-19 | PASS | 5 | Both named blocks, tabular, criterion-ID failure statements. |
| C-20 | PASS | 5 | DISPOSITION: 6th row present. COLUMN POLICY: rows 1-2 explicitly enumerate partial-compliance variants. Both PASS. |
| C-21 | PASS | 5 | Both blocks three-column tabular format. |
| C-22 | PARTIAL | 3 | **Source artifact present; derived artifact absent.** Named Incumbent Coupling Table with per-factor switching-cost ratings is present — the structural grounding artifact. Switch Cost column in Inertia Verdict Matrix is absent — per-factor data exists but does not propagate to synthesis verdict. Source > derived in PARTIAL band: the table containing per-factor ratings is the substantive completion; the Switch Cost column is the propagation step. PARTIAL at 3 pts. |

**Composite: 158/160**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 68/70 (C-22 partial: 3 pts)
All C-01..C-05 pass: YES | Golden: YES

---

## V-03: C-22 PARTIAL-B — Switch Cost Column, No Named Table; Incumbent Last

*C-22 PARTIAL-B: Switch Cost column in Inertia Verdict Matrix, no named Incumbent Coupling Table. Role sequence: S-01 → S-02 → S-00 (incumbent last).*

**C-22 floor check:** C-09 PASS. C-13: incumbent interview (S-00, last) opens with neutral current-practice Q1 within its own block — within-interview Q1 anchor criterion satisfied regardless of cross-interview ordering. C-22 gradable.

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. S-01 → S-02 → S-00 ordering does not change per-subject declaration requirement. All declared before their own transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject. Incumbent declared before its own transcript even if last in overall ordering. |
| C-03 | PASS | 12 | A-turn instructions: role-grounded resistance (S-01 first), advocacy (S-02), incumbent baseline (S-00 last). |
| C-04 | PASS | 12 | Evidence Pull tables per subject. COLUMN POLICY enforced across all three. |
| C-05 | PASS | 12 | Prior knowledge blocks ground all subjects including incumbent (interviewed last). |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION + S-00 incumbent. Meaningfully distinct profiles. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set. Inertia Verdict Matrix present with Switch Cost column. |
| C-10 | PASS | 5 | COLUMN POLICY: partial-compliance row for Quote/Rationale absence. |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT: SKEPTIC + CHAMPION rows; 6th row for C-18. Arc Signal skeptic-prior. |
| C-12 | PASS | 5 | Critical Contradiction Table: two named contradictions ranked, source pairs, Stakes column. |
| C-13 | PASS | 5 | Incumbent interview (S-00, last) opens with current-practice Q1 within its own block. Within-interview Q1 anchor satisfied regardless of cross-interview ordering. |
| C-14 | PASS | 5 | COLUMN POLICY: verbatim quote requirement with criterion IDs. |
| C-15 | PASS | 5 | Critical Contradiction Table cites both subjects per contradiction. |
| C-16 | PASS | 5 | COLUMN POLICY: non-substitutability rule with criterion ID. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT table: per-subject labels before transcripts. |
| C-18 | PASS | 5 | SKEPTIC = S-01. DISPOSITION 6th row: partial-compliance C-18 condition. Arc Signal skeptic-prior. |
| C-19 | PASS | 5 | Both named blocks, tabular, criterion-ID failure statements. |
| C-20 | PASS | 5 | DISPOSITION: 6th row. COLUMN POLICY: explicit partial-compliance rows. Both PASS. |
| C-21 | PASS | 5 | Both blocks three-column tabular format. |
| C-22 | PARTIAL | 2 | **Derived artifact present; source artifact absent.** Switch Cost column in Inertia Verdict Matrix present — coupling data reaches synthesis verdict. Named Incumbent Coupling Table absent — no structural grounding artifact provides per-factor switching-cost ratings. The column asserts switch costs without a sourcing table; assertion without structural grounding is less complete than grounded data without propagation. Derived < source in PARTIAL band: 2 pts. |

**Composite: 157/160**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 67/70 (C-22 partial: 2 pts)
All C-01..C-05 pass: YES | Golden: YES

**Incumbent-last finding:** Role sequence inversion (S-01 → S-02 → S-00) does not affect C-09 or C-13 floor behavior. C-13 grades the within-interview Q1 position; C-09 grades whether a synthesis section exists. Both floors pass regardless of cross-interview sequencing. Variation axis is scoring-neutral for all C-01..C-21 criteria.

---

## V-04: C-22 PASS Minimal — One Factor, One Rating, Explicit Sourcing, Lifecycle Gate

*Minimum C-22 PASS: one named coupling factor with one switching-cost baseline rating; Inertia Verdict Matrix Switch Cost column explicitly sourced from Incumbent Coupling Table. Post-Step-1 lifecycle gate enforces coupling table completion before human-subject interviews proceed.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. All subjects with disposition labels before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject. "State the prior knowledge block in full before the transcript begins." |
| C-03 | PASS | 12 | A-turn instructions: role-grounded responses per disposition. |
| C-04 | PASS | 12 | Evidence Pull tables per subject. "Apply Column Policy to every row" enforced at each evidence section. |
| C-05 | PASS | 12 | Prior knowledge blocks ground all subjects. |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q3 contrast note specific. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION. Distinct domains. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set with post-synthesis gate: "If any row is missing a column, name the criterion violated before proceeding." |
| C-10 | PASS | 5 | COLUMN POLICY table: "Quote present but Rationale absent: C-10, C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT table: SKEPTIC + CHAMPION rows; 6th row for partial-compliance C-18. Arc Signal skeptic-prior. |
| C-12 | PASS | 5 | Critical Contradiction Table: ranked by evidential weight, source pairs, Stakes column. |
| C-13 | PASS | 5 | Incumbent opens with neutral current-practice Q1. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY: "Rationale present but Quote absent: C-14, C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table cites HE-# from both subjects. |
| C-16 | PASS | 5 | COLUMN POLICY: displacement row with criterion ID. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT table: per-subject labels. |
| C-18 | PASS | 5 | SKEPTIC = S-01. 6th DISPOSITION row. Arc Signal skeptic-prior. Both structural and framing conditions. |
| C-19 | PASS | 5 | Both named blocks, tabular, criterion-ID conditions. |
| C-20 | PASS | 5 | DISPOSITION: 6th row. COLUMN POLICY: explicit partial-compliance rows. Both PASS. |
| C-21 | PASS | 5 | Both blocks three-column tabular format. |
| C-22 | PASS | 5 | **Minimum PASS architecture.** Named Incumbent Coupling Table: one coupling factor with one switching-cost baseline rating derived from incumbent Q1 interview — structural grounding artifact present. Inertia Verdict Matrix Switch Cost column: entry explicitly attributed "sourced from Incumbent Coupling Table." Both conjunction elements present with explicit sourcing connection. Post-Step-1 lifecycle gate ("before proceeding to human-subject interviews, confirm the Incumbent Coupling Table is complete") prevents post-hoc population. Minimum threshold satisfied. |

**Composite: 160/160**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 70/70
All C-01..C-05 pass: YES | Golden: YES

---

## V-05: C-22 PASS Maximum — Multi-Factor, Per-Row Attribution, COLUMN POLICY Additive-Only Row

*Maximum C-22: multi-factor Incumbent Coupling Table; Switch Cost column with per-row coupling-factor attribution; COLUMN POLICY additive-only row enforces C-22 non-displacement; incumbent switching friction in Arc Signal.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. "SKEPTIC-FIRST REQUIREMENT: This is not cosmetic." Explicit rationale for ordering. |
| C-02 | PASS | 12 | Most specific prior knowledge instructions. "Current-practice anchor" field in incumbent prior knowledge block. |
| C-03 | PASS | 12 | A-turn instructions specify role-grounded full responses per disposition. |
| C-04 | PASS | 12 | Evidence Pull tables required. Pre-synthesis gate: "If a row is missing a column, name the specific criterion violated before proceeding." |
| C-05 | PASS | 12 | COLUMN POLICY: "Rationale must answer 'why does this signal matter to the topic decision?' — not a restatement of the quote." |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. "Open without leading toward resistance/advocacy" reduces interviewer-lead contamination. |
| C-07 | PASS | 10 | Min 3 turns. Q3 contrast note: "Name the claim from S-01. Do not refer generically." |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION. Most explicit knowledge-basis differentiation. |
| C-09 | PASS | 5 | Arc Signal: "Do not summarize individual interviews — synthesize across them." Grounding check: "If the conclusion references only one subject, it is not an arc — revise before filing." |
| C-10 | PASS | 5 | COLUMN POLICY: "a confidence score without accompanying rationale cannot be evaluated for basis" — most explicit rationale-basis statement. |
| C-11 | PASS | 5 | Arc Signal explicitly grounds each voice in HE-#. |
| C-12 | PASS | 5 | Critical Contradiction Table with forward-looking stakes: "What is at risk if this tension persists into implementation." |
| C-13 | PASS | 5 | Most explicit current-practice Q1: "ask what the incumbent does today, before any feature is introduced." "Current-practice anchor" field in prior knowledge block. |
| C-14 | PASS | 5 | "[Verbatim quote — exact words from A1, A2, or A3 — not paraphrased]" — most explicit verbatim requirement. |
| C-15 | PASS | 5 | Critical Contradiction Table + grounding check both enforce both-sides citation at synthesis level. |
| C-16 | PASS | 5 | COLUMN POLICY: "any addition that displaces Quote or Rationale from any row violates non-substitutability regardless of the addition's descriptive value." COLUMN POLICY additive-only row for Incumbent Coupling Table explicitly states "Switch Cost column supplements; does not displace required columns." Most complete non-substitutability + C-22/C-16 boundary statement. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "every human subject requires explicit per-subject label before transcripts begin — absence on any single entry fails the criterion." Most specific per-entry enforcement. |
| C-18 | PASS | 5 | "SKEPTIC-FIRST REQUIREMENT: This is not cosmetic." DISPOSITION 6th row with illustrative failure example. Arc Signal: "This is not a symmetric comparison between two equal voices." Both conditions. |
| C-19 | PASS | 5 | Both named blocks, most detailed tabular criterion-ID conditions with explanatory parentheticals. |
| C-20 | PASS | 5 | DISPOSITION: 6th row with illustrative failure example. COLUMN POLICY: rows 1-2 with maximum explanatory depth. Both PASS. |
| C-21 | PASS | 5 | Both blocks three-column tabular format. |
| C-22 | PASS | 5 | **Maximum PASS architecture.** Named Incumbent Coupling Table: multiple coupling factors, each with switching-cost baseline rating from incumbent Q1 interview. Inertia Verdict Matrix Switch Cost column: per-row coupling-factor attribution from Incumbent Coupling Table — not a single aggregate entry. COLUMN POLICY additive-only row: "Incumbent Coupling Table adds Switch Cost column to Inertia Verdict Matrix; additive supplementation — does not displace Quote or Rationale from any Evidence Pull row; C-16 violations in Evidence tables are independent of C-22 status." Incumbent switching friction surfaced in Arc Signal narrative. Both conjunction elements present, explicitly connected, additive-only rule enforced in named compliance block. Architecture investment for C-23 extraction. |

**Composite: 160/160**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 70/70
All C-01..C-05 pass: YES | Golden: YES

**Excellence signals above V-04 minimum (zero score impact; architecture depth only):**
1. Multi-factor Incumbent Coupling Table with per-row Switch Cost attribution — scales the C-22 architecture from one coupling factor to a structural multi-factor matrix
2. COLUMN POLICY additive-only row — explicitly documents the C-22/C-16 boundary in the named compliance block, preventing future refactoring from conflating the two domains
3. Arc Signal terminus — per-factor incumbent friction claim in Arc Signal narrative; maximum propagation depth: table → verdict column → synthesis narrative
4. "Current-practice anchor" field in prior knowledge block — structural two-level C-13: declared anchor field (pre-transcript) + open-ended Q1 (within-transcript); V-04 satisfies C-13 floor through Q1 alone

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
| C-20 | 5 | 5 | 5 | 5 | 5 |
| C-21 | 5 | 5 | 5 | 5 | 5 |
| C-22 | **0** | **3** | **2** | **5** | **5** |
| **Total** | **155** | **158** | **157** | **160** | **160** |

All 5 variations: Golden. Prediction accuracy: 4/5 (V-02 off by 1 pt — source > derived PARTIAL asymmetry resolved at 3 not 2).

---

## Excellence Signals (from 160/160 variations)

**Pattern 1: Minimum C-22 PASS is one-factor-one-rating-explicit-sourcing with lifecycle gate**
V-04 confirms: one named coupling factor + one switching-cost baseline rating from the incumbent Q1 interview + explicit "sourced from Incumbent Coupling Table" statement in the Switch Cost column entry + post-Step-1 lifecycle gate. The gate is the structural mechanism distinguishing minimum PASS from PARTIAL — without it, the coupling table risks post-hoc population after human-subject interviews contaminate the baseline.

**Pattern 2: COLUMN POLICY additive-only row self-documents the C-22/C-16 boundary**
V-05 demonstrates that the COLUMN POLICY compliance block can host a C-22 enforcement row alongside C-16 non-substitutability rows: "Switch Cost column is additive supplementation — C-16 violations in Evidence Pull tables are independent of C-22 status." This row prevents future refactoring from conflating the two domains and makes the compliance block's scope explicit.

**Pattern 3: Arc Signal is the C-22 propagation terminus**
V-05 propagates incumbent switching friction from Incumbent Coupling Table → Switch Cost column → Arc Signal narrative. Per-factor incumbent friction is named in the synthesis ("prior signal carries switching-cost weight from [coupling factor]"). Maximum propagation depth for C-22: table → verdict column → narrative synthesis. Candidate for C-23 extraction as per-factor incumbent friction claim in Arc Signal.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["C-22 PARTIAL is source-asymmetric: named Incumbent Coupling Table without Switch Cost column (source present, derived absent) scores 3 pts PARTIAL; Switch Cost column without named Incumbent Coupling Table (derived present, source absent) scores 2 pts PARTIAL -- the table is the grounding artifact with structural content; the column is derived propagation; source completeness > derived propagation in PARTIAL band", "Minimum C-22 PASS requires explicit attribution, not coexistence: one coupling factor + one rating + explicit sourced-from statement in Switch Cost column entry + lifecycle gate preventing post-hoc population of coupling table; gate is the structural enforcement mechanism distinguishing minimum PASS from PARTIAL", "COLUMN POLICY additive-only row extends named compliance infrastructure to C-22 domain: V-05 adds a row stating Switch Cost column supplements without displacing Evidence Pull columns; C-16 violations in Evidence tables remain independent of C-22 status; self-documenting compliance block that explicitly enforces the C-22/C-16 boundary", "Maximum C-22 architecture propagates to Arc Signal narrative: Incumbent Coupling Table -> Switch Cost column -> per-factor incumbent friction claim in Arc Signal is the V-05 terminus; candidate for C-23 extraction as per-factor incumbent friction named in synthesis narrative"]}
```
