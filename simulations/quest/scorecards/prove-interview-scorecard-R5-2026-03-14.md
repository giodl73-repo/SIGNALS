## prove-interview Round 5 Scorecard

| Rank | Variation | Score | C-18 | C-19 | Golden |
|------|-----------|-------|------|------|--------|
| 1 | V-03 Both fixes, minimal | **145/145** | PASS | PASS | YES |
| 1 | V-04 Output format (tabular blocks) | **145/145** | PASS | PASS | YES |
| 1 | V-05 All axes, maximum enforcement | **145/145** | PASS | PASS | YES |
| 4 | V-01 Role sequence (C-18 only) | 140/145 | PASS | FAIL | YES |
| 4 | V-02 Lifecycle emphasis (C-19 only) | 140/145 | FAIL | PASS | YES |

**All five variations Golden. Prediction accuracy: 5/5.**

---

### Scoring notes per variation

**V-01 (140):** C-18 PASS — SKEPTIC-first roster with `Prior signal (SKEPTIC S-01):` / `Subsequent evidence (CHAMPION S-02):` Arc framing satisfies both the structural and framing conditions simultaneously. C-19 FAIL — both named blocks present with itemized conditions, but failure statements say "fails the structural requirement" rather than citing criterion IDs. Two blocks + non-criterion-citing statements = 0 pts; the PARTIAL band requires one-block structural incompleteness, not statement-quality failure.

**V-02 (140):** C-19 PASS — both DISPOSITION REQUIREMENT and COLUMN POLICY blocks carry per-condition failure statements with explicit criterion IDs (FAILS C-11, FAILS C-17, FAILS C-10, FAILS C-14, FAILS C-16). C-18 FAIL — CHAMPION declared S-01, symmetric Arc Signal framing.

**V-03 (145):** Minimal-fix confirmed. Two changes from R4 V-04: SKEPTIC-first + criterion IDs in both compliance blocks. Sufficient and minimal for ceiling.

**V-04 (145):** Tabular failure condition format (Condition / What is absent / Criterion(s) violated) satisfies C-19 equivalently to prose bullets. Format is not material; criterion-ID citation is.

**V-05 (145):** Adds 6th DISPOSITION REQUIREMENT failure condition closing the half-C-18 loophole: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18." No score impact over V-03/V-04 — architecture depth only.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["C-18 and C-19 are orthogonally independent -- V-01 and V-02 each score 140/145 with one criterion absent; each adds exactly 5 pts independently", "Tabular per-condition failure conditions satisfy C-19 equivalently to prose-itemized bullets -- V-04 tabular format scores 145/145 identically to V-03 prose bullets; format is not material to C-19 compliance", "C-19 FAIL boundary is criterion-ID citation not block count -- two named blocks with itemized conditions but without criterion IDs = FAIL (0 pts); PARTIAL requires one-block structural incompleteness; non-criterion-citing statements do not earn partial credit"]}
```
esign: both named blocks present with itemized conditions but no criterion IDs.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table: ID/Role-Title/Domain/Disposition. Subject 0 field table. All subjects declared before transcripts. |
| C-02 | PASS | 12 | Prior knowledge block per subject before transcript. Incumbent: current assumption + confidence + threshold. S-01/S-02: domain knowledge + named stance + named threshold. |
| C-03 | PASS | 12 | A-turn instructions: "[S-01 response -- role-grounded resistance]"; "[S-02 response -- role-grounded advocacy]". |
| C-04 | PASS | 12 | Evidence Pull tables mandatory per subject. Signal/Quote/Confidence/Rationale schema enforced by COLUMN POLICY. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. Expected bias declared for Incumbent. Domain-grounded instruction per human subject. |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject, three instances (Incumbent, S-01, S-02). |
| C-07 | PASS | 10 | Min 3 turns per subject. Q2 probes named stance from prior knowledge block. Q3 contrast note references prior-subject content. |
| C-08 | PASS | 10 | S-01 labeled SKEPTIC, S-02 labeled CHAMPION. Distinct domains and prior knowledge profiles. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: Pattern, Critical Contradiction Table, Tension Resolution, Inertia Verdict Matrix, Arc Signal, Prior Assumption Revisited. |
| C-10 | PASS | 5 | COLUMN POLICY: "Each evidence row must contain exactly four columns: Signal/Quote/Confidence/Rationale." Confidence + Rationale simultaneously required. |
| C-11 | PASS | 5 | Roster: SKEPTIC + CHAMPION. DISPOSITION REQUIREMENT enforces both poles. Arc Signal: "Prior signal (SKEPTIC S-01)" + "Subsequent evidence (CHAMPION S-02)" -- both dispositions in causal arc. |
| C-12 | PASS | 5 | Critical Contradiction Table: two rows, Stakes column, "S-01 claim vs. S-02 claim -- the core skeptic/champion tension" labeled. |
| C-13 | PASS | 5 | Open-ended Q1: "[Opening -- invite S-01's framing of TOPIC]". Prior knowledge block grounds subject before Q1. Consistent with R4 baseline C-13 PASS. |
| C-14 | PASS | 5 | COLUMN POLICY: "Quote = verbatim subject turn." Evidence Pull Quote column required. |
| C-15 | PASS | 5 | Critical Contradiction Table: "S-01 claim vs. S-02 claim" row cites "HE-#, HE-#" -- one per side. |
| C-16 | PASS | 5 | COLUMN POLICY: "A table with Quote + Confidence but no Rationale is incomplete and fails the column policy. Adding an architectural column does not substitute for Quote or Rationale." |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT block: explicit Disposition column in roster. "A roster entry with no Disposition label fails the structural requirement." Per-subject labels before transcripts. |
| C-18 | PASS | 5 | Roster: S-01=SKEPTIC first, S-02=CHAMPION second. "SKEPTIC-FIRST SEQUENCE: This ordering is required." Step 2 header: "HUMAN INTERVIEWS -- SKEPTIC-FIRST SEQUENCE." Arc Signal: "Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence." "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):" format. Both structural ordering AND prior-signal framing present. |
| C-19 | FAIL | 0 | **Absent by design.** DISPOSITION REQUIREMENT: named block + itemized conditions, but failure statements say "fails the structural requirement" -- no criterion IDs. COLUMN POLICY: named block + itemized conditions, but says "is incomplete and fails the column policy" -- no C-10/C-16 citations. Two blocks with non-criterion-citing statements = FAIL (0 pts). PARTIAL band requires one-block structural incompleteness; this is a statement-quality failure, not a block-count failure. |

**Composite: 140/145**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 50/55 (C-19 fail: 0)
All C-01..C-05 pass: YES | Golden: YES

---

## V-02: Lifecycle Emphasis -- C-19 Only (CHAMPION-first, no C-18)

*C-18 absent by design: CHAMPION declared S-01; symmetric Arc Signal framing.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table declared. All subjects have explicit ID, Role, Domain, Disposition. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. Incumbent: assumption + confidence + threshold. Subjects: domain knowledge + named stance + threshold. |
| C-03 | PASS | 12 | A-turn instructions specify "role-grounded advocacy" (S-01 CHAMPION) and "role-grounded resistance" (S-02 SKEPTIC). |
| C-04 | PASS | 12 | Evidence Pull tables mandatory: IE-# (Incumbent), HE-1/HE-2 (CHAMPION), HE-3/HE-4 (SKEPTIC). |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. COLUMN POLICY requires interpretive Rationale. |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note references prior-subject content. |
| C-08 | PASS | 10 | S-01=CHAMPION, S-02=SKEPTIC with different dispositions, domains, and prior knowledge profiles. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set. |
| C-10 | PASS | 5 | COLUMN POLICY criterion-ID: "Table has Quote + Confidence but no Rationale: FAILS C-10 (Evidence confidence rated) and FAILS C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT: "No CHAMPION label: FAILS C-11 and FAILS C-17"; "No SKEPTIC label: FAILS C-11 and FAILS C-17". Arc Signal (symmetric): S-01 CHAMPION + S-02 SKEPTIC arc addressed in synthesis. |
| C-12 | PASS | 5 | Critical Contradiction Table: two rows with IE/HE source pairs and Stakes column. |
| C-13 | PASS | 5 | Neutral open-ended Q1. Prior knowledge block grounds current context before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY criterion-ID: "Table has Rationale + Confidence but no Quote: FAILS C-14 (Arc claims quote-anchored) and FAILS C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table: "S-01 vs. S-02" row cites "HE-#, HE-#" -- one per disposition. |
| C-16 | PASS | 5 | COLUMN POLICY: five failure conditions all cite C-16. "Quote does not substitute for Rationale; both must coexist simultaneously." |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "Roster entry with no Disposition column value: FAILS C-17 (every human subject requires explicit per-subject label before transcripts begin)." |
| C-18 | FAIL | 0 | **Absent by design.** CHAMPION declared S-01 (first). Arc Signal labeled "symmetric -- C-18 absent by design." Two-voice symmetric framing. Both structural ordering and framing conditions fail. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + 4 itemized criterion-ID conditions. COLUMN POLICY: named block + 5 itemized criterion-ID conditions. Both blocks with full criterion-ID itemization. |

**Composite: 140/145**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 50/55 (C-18 fail: 0)
All C-01..C-05 pass: YES | Golden: YES

**Isolation finding:** C-18 and C-19 are orthogonally independent. V-01 passes C-18 without C-19 at 140. V-02 passes C-19 without C-18 at 140. Each criterion independently adds exactly 5 pts.

---

## V-03: Both Fixes, Minimal (C-18 + C-19)

*Minimal combination: SKEPTIC-first (C-18) + criterion-ID failure statements in both blocks (C-19).*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster table: ID/Role-Title/Domain/Disposition. Subject 0 field table. All declared before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. |
| C-03 | PASS | 12 | A-turn instructions: "resistance grounded in role" (S-01), "advocacy grounded in role" (S-02). |
| C-04 | PASS | 12 | Evidence Pull tables required: IE-#, HE-1/HE-2 (S-01), HE-3/HE-4 (S-02). |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. Rationale requires interpretive content. |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 probes named stance. Q3 contrast note explicit. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION, distinct domains and prior knowledge. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set. |
| C-10 | PASS | 5 | COLUMN POLICY: "Quote + Confidence no Rationale: FAILS C-10 and FAILS C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT: "No SKEPTIC: FAILS C-11 and FAILS C-17"; "No CHAMPION: FAILS C-11 and FAILS C-17." Arc Signal (SKEPTIC-prior) addresses both dispositions. |
| C-12 | PASS | 5 | Critical Contradiction Table: two rows, source pairs, Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY: "Rationale + Confidence no Quote: FAILS C-14 and FAILS C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table: "S-01 vs. S-02" row cites HE-# from each subject. |
| C-16 | PASS | 5 | COLUMN POLICY: "Quote + Confidence no Rationale: FAILS C-16 (Evidence columns non-substitutable)." Non-substitutability with criterion ID. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "Roster entry no Disposition: FAILS C-17." Per-subject labels with criterion ID. |
| C-18 | PASS | 5 | S-01=SKEPTIC first. "SKEPTIC-FIRST:" enforced. Arc Signal: "Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence." "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". DISPOSITION REQUIREMENT adds: "CHAMPION declared as S-01: FAILS C-18." Both structural and framing conditions present. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + 5 criterion-ID conditions (including C-18 failure for CHAMPION-first). COLUMN POLICY: named block + 5 criterion-ID conditions. Both blocks fully compliant. |

**Composite: 145/145**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 55/55
All C-01..C-05 pass: YES | Golden: YES

**Minimal-fix finding:** V-03 is the minimal change from R4 V-04 to achieve 145/145. Two targeted changes: (1) SKEPTIC as S-01 + skeptic-prior Arc framing; (2) criterion IDs in both compliance block failure statements.

---

## V-04: Output Format -- Tabular Failure Conditions (C-18 + C-19, tabular blocks)

*Both fixes applied. Failure conditions as Condition/What-is-absent/Criterion-violated tables.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. All subjects have ID, Role/Title, Domain, Disposition before transcripts. |
| C-02 | PASS | 12 | Prior knowledge blocks per subject before transcript. |
| C-03 | PASS | 12 | A-turn instructions specify role-grounded responses per disposition. |
| C-04 | PASS | 12 | Evidence Pull tables required per subject: Signal/Quote/Confidence/Rationale. Pre-synthesis gate enforces column completeness. |
| C-05 | PASS | 12 | Prior knowledge blocks ground each subject. Required schema: "[Verbatim subject turn] / [1-5] / [Why this signal matters -- interpretive]". |
| C-06 | PASS | 10 | "Surprise (one sentence)" required per subject. |
| C-07 | PASS | 10 | Min 3 turns. Q2 follows named stance. Q3 contrast note cross-references prior subject. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION, distinct domains and prior knowledge. |
| C-09 | PASS | 5 | STEP 3 SYNTHESIS: full component set including pre-synthesis gate. |
| C-10 | PASS | 5 | COLUMN POLICY failure table: "Quote + Confidence present, no Rationale | Interpretive rationale per row | C-10, C-16." |
| C-11 | PASS | 5 | DISPOSITION REQUIREMENT failure table: "No SKEPTIC | Explicit skeptic disposition | C-11, C-17"; "No CHAMPION | Explicit advocate disposition | C-11, C-17." Arc Signal (SKEPTIC-prior) addresses both. |
| C-12 | PASS | 5 | Critical Contradiction Table: two named contradictions with source pairs and Stakes column. |
| C-13 | PASS | 5 | Open-ended Q1. Prior knowledge block before Q1. |
| C-14 | PASS | 5 | COLUMN POLICY failure table: "Rationale + Confidence present, no Quote | Verbatim SUBJECT source turn | C-14, C-16." |
| C-15 | PASS | 5 | Critical Contradiction Table: "S-01 vs. S-02" row cites HE-# from both dispositions. |
| C-16 | PASS | 5 | COLUMN POLICY failure table: five rows, all addressing C-16. "Architectural column replaces Quote or Rationale | Non-substitutable base column | C-16." |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT failure table: "Roster entry no Disposition value | Per-subject label | C-17"; "Disposition inferred from synthesis | Roster-level declaration | C-17." |
| C-18 | PASS | 5 | S-01=SKEPTIC first. "SKEPTIC-FIRST: S-01 must be SKEPTIC." DISPOSITION REQUIREMENT table: "CHAMPION declared as S-01 | SKEPTIC-first ordering | C-18." Arc Signal (SKEPTIC-prior): "Prior signal (SKEPTIC S-01):" / "Subsequent evidence (CHAMPION S-02):". Both structural and framing conditions present. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + failure conditions as Condition/What-is-absent/Criterion-violated table, all rows cite criterion IDs. COLUMN POLICY: named block + failure conditions as same table schema, all rows cite criterion IDs. Tabular rows satisfy "itemized per-condition failure statements that name exactly what is absent and which criterion it violates." Format (table vs. prose) is not material; criterion-ID citation is. |

**Composite: 145/145**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 55/55
All C-01..C-05 pass: YES | Golden: YES

**Format finding:** V-04 tabular failure conditions score 145/145 identically to V-03 prose bullets. C-19 "itemized per-condition failure statements" is satisfied by table rows equivalently to prose bullets.

---

## V-05: All Axes -- Full Ceiling (C-18 + C-19, maximum enforcement)

*All five axes: SKEPTIC-first, skeptic-prior Arc framing, prose criterion-ID failure statements, maximum enforcement, half-C-18 loophole closure.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Roster declared. "SKEPTIC-FIRST REQUIREMENT" header names subject roles before roster table. |
| C-02 | PASS | 12 | Most specific prior knowledge instructions: "named condition -- specific, not generic" (Incumbent); "domain-grounded -- specific to subject's role" + "named explicitly before transcript begins" (human subjects). |
| C-03 | PASS | 12 | A-turn instructions: "[response -- role-grounded, full response]." "Full response" unique to V-05 -- prevents abbreviated persona answers. |
| C-04 | PASS | 12 | Evidence Pull tables required. Pre-synthesis gate: "If a row is missing a column, name the specific criterion violated before proceeding." |
| C-05 | PASS | 12 | COLUMN POLICY: "Rationale must answer 'why does this signal matter to the feature decision?'" -- most explicit grounding requirement. |
| C-06 | PASS | 10 | "Surprise (one sentence)" per subject. Q1: "without leading toward resistance/advocacy" -- reduces interviewer-lead contamination. |
| C-07 | PASS | 10 | Min 3 turns. Q3 contrast note: "The claim must be identified by quoting or closely paraphrasing S-01's language" -- most specific cross-subject referencing. |
| C-08 | PASS | 10 | S-01 SKEPTIC + S-02 CHAMPION. Most explicit knowledge-basis differentiation. |
| C-09 | PASS | 5 | Pattern: "Do not summarize individual interviews -- synthesize across them." Grounding check after Arc Signal: "If the conclusion references only one subject, it is not an arc -- revise before filing." |
| C-10 | PASS | 5 | COLUMN POLICY: "a confidence score without accompanying rationale cannot be evaluated for basis" -- most explicit rationale-basis statement. |
| C-11 | PASS | 5 | Arc Signal: "Prior signal (SKEPTIC S-01): [... grounded in HE-1 and HE-2]." Most explicit HE-# grounding reference in Arc Signal. |
| C-12 | PASS | 5 | Critical Contradiction Table: "[S-01 SKEPTIC claim vs. S-02 CHAMPION claim -- the core arc tension]" with "[What is at risk if this tension persists into implementation]" -- forward-looking stakes framing. |
| C-13 | PASS | 5 | Q1: "without leading toward resistance/advocacy" -- most neutral Q1 instruction of all variations. |
| C-14 | PASS | 5 | "[Verbatim quote -- exact words from A1, A2, or A3]" -- most explicit verbatim requirement. |
| C-15 | PASS | 5 | Critical Contradiction Table cites HE-# from both subjects. Grounding check enforces both-sides citation a second time. |
| C-16 | PASS | 5 | COLUMN POLICY: "adding a column such as Phase, Theme, or Category is permitted only if it supplements the four required columns; any architectural addition that displaces Quote or Rationale from any row violates the non-substitutability rule regardless of the addition's descriptive value." Most complete non-substitutability statement. |
| C-17 | PASS | 5 | DISPOSITION REQUIREMENT: "absence of label on any single entry fails the criterion regardless of whether other entries have labels." Most specific per-entry enforcement. |
| C-18 | PASS | 5 | S-01=SKEPTIC first. "SKEPTIC-FIRST REQUIREMENT: This is not cosmetic." Arc Signal: "This is not a symmetric comparison between two equal voices." "Prior signal (SKEPTIC S-01): [... grounded in HE-1 and HE-2]." DISPOSITION REQUIREMENT 6th condition: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18 (C-18 requires both structural ordering and prior-signal framing simultaneously; structural ordering without skeptic-prior Arc framing satisfies only half the criterion)." Closes the half-C-18 loophole. |
| C-19 | PASS | 5 | DISPOSITION REQUIREMENT: named block + 6 criterion-ID conditions with explanatory parentheticals. COLUMN POLICY: named block + 5 criterion-ID conditions with explanatory parentheticals. Most detailed failure condition descriptions of all variations. Both blocks fully compliant. |

**Composite: 145/145**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 55/55
All C-01..C-05 pass: YES | Golden: YES

**Excellence signals above V-03 baseline (zero score impact, enforcement depth):**
1. 6th DISPOSITION REQUIREMENT failure condition closes the half-C-18 loophole
2. "Full response" A-turn instruction prevents abbreviated persona answers
3. Arc Signal Grounding check enforces both-sides citation at conclusion level

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
| C-18 | **5** | **0** | **5** | **5** | **5** |
| C-19 | **0** | **5** | **5** | **5** | **5** |
| **Total** | **140** | **140** | **145** | **145** | **145** |

All 5 variations: Golden. Prediction accuracy: 5/5.
