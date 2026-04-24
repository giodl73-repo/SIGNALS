Written to `simulations/quest/rubrics/prove-interview-rubric-v7-2026-03-14.md`.

---

**What changed v6 -> v7:**

One new aspirational criterion extracted from R6 Pattern 4 (the only promotable pattern -- Pattern 5 was explicitly excluded as enforcement-depth only):

---

**C-22 -- Incumbent Coupling Table with switch-cost baseline** (5 pts)
Sourced from V-05. A named Incumbent Coupling Table enumerates per-coupling-factor switching-cost ratings from the incumbent baseline interview and feeds a Switch Cost column in the Inertia Verdict Matrix. Both are required for PASS: the named table with at least one per-factor rating, and the Inertia Verdict Matrix Switch Cost column explicitly sourced from it. The table is additive-only -- it cannot displace Evidence Pull columns (C-16 violations remain independent). C-22 PARTIAL: one element present without the other.

**Floor prerequisites: C-09 + C-13.** C-09 (synthesis exists with Inertia Verdict Matrix) and C-13 (current-practice Q1 anchor establishes the incumbent baseline the coupling factors draw from). C-22 is N/A if either floor fails.

---

**Point accounting:** Aspirational 65 -> 70 pts, ceiling 155 -> 160. Golden threshold stays at 80.

**New ladder entry:**
- `C-09 + C-13 -> C-22`: synthesis with Inertia Verdict Matrix + incumbent current-practice baseline -> switching-cost baseline structured as named coupling table feeding Switch Cost column into synthesis verdict.
-09 + C-13 are the floor prerequisites; C-22 is the ceiling where the
incumbent switching-cost baseline is structurally grounded in a named coupling table that propagates
into the synthesis verdict.

---

**Point accounting:** Aspirational 65 -> 70 pts, ceiling 155 -> 160. Golden threshold stays at 80.

**New ladder entry:**
- `C-09 + C-13 -> C-22`: C-09 requires a synthesis section with an Inertia Verdict Matrix; C-13
  requires a current-practice Q1 anchor that establishes the incumbent baseline; C-22 requires the
  incumbent switching-cost baseline to be structured as a named Incumbent Coupling Table that feeds
  a Switch Cost column into the Inertia Verdict Matrix. Both floor criteria must pass for C-22 to
  be gradable.

**Note on relationship to evidence columns:** C-22 is additive-only. The Incumbent Coupling Table
adds a Switch Cost column to the Inertia Verdict Matrix; it does not modify Evidence Pull tables.
Column-displacement failure in Evidence Pull tables remains a C-16 violation regardless of whether
an Incumbent Coupling Table is present. C-22 PARTIAL: Incumbent Coupling Table present but not
connected to a Switch Cost column in the Inertia Verdict Matrix (or vice versa: Switch Cost column
in synthesis without a named Incumbent Coupling Table sourcing it). C-22 PASS: both the named
table and the Switch Cost column are present and the column is explicitly sourced from the table.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Persona identity declared** | correctness | essential | Each interview subject has an explicit role, title, or identity stated before the interview begins. Anonymous or role-free subjects fail. |
| C-02 | **Prior knowledge scoped** | correctness | essential | Each subject's prior knowledge or background context is stated (what they know, what they don't know, what they care about) before answers are given. |
| C-03 | **Answers in persona voice** | behavior | essential | Answers read as coming from the declared persona -- vocabulary, concerns, and framing match the role. Generic AI-sounding answers that could belong to any persona fail. |
| C-04 | **Evidence extracted** | coverage | essential | At least one concrete evidence item (insight, concern, requirement, contradiction, or signal) is explicitly extracted per interview subject -- not left implicit in the dialogue. |
| C-05 | **Grounded, not invented** | correctness | essential | Answers reference the persona's documented domain knowledge or plausible role-based concerns. Answers that invent facts outside the persona's plausible knowledge domain fail. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Surprising moment present** | depth | recommended | At least one interview subject produces an unexpected answer, tension, or reveal -- something the interviewer's questions did not anticipate. The moment is labeled or called out. |
| C-07 | **Question quality** | depth | recommended | Questions are open-ended and probing, not leading or yes/no. At least one follow-up question appears in response to a prior answer within a single interview. |
| C-08 | **Multiple distinct personas** | coverage | recommended | The simulation includes at least two interview subjects with meaningfully different roles, knowledge levels, or concerns -- not minor variations of the same profile. |

---

## Aspirational Criteria (70 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-interview synthesis** | depth | aspirational | After all interviews, the output includes a synthesis section noting patterns, contradictions, or convergences across subjects -- connecting the individual evidence items into a composite signal. |
| C-10 | **Evidence confidence rated** | depth | aspirational | Each extracted evidence item carries an explicit confidence or signal-strength marker (e.g., strong/weak, high/low, confirmed/suspected) with a one-line rationale. |
| C-11 | **Disposition arc structured** | depth | aspirational | Personas include at least one explicit advocate (champion or supporter) and at least one explicit skeptic (critic or resistant voice). The synthesis addresses whether agreement or contradiction between dispositions was the dominant arc signal -- convergence despite skepticism is strong signal; skeptic confirming champion without role-grounded resistance is a red flag. |
| C-12 | **Critical contradiction named** | depth | aspirational | The synthesis section does not merely list contradictions -- it identifies and names the single most significant contradiction between interview subjects and explains its evidential weight (what it confirms, undermines, or leaves unresolved). A synthesis that enumerates contradictions without ranking them fails this criterion. |
| C-13 | **Current-practice Q1 anchor** | behavior | aspirational | At least one interview opens with a neutral current-practice question (what the subject does today, before any feature is introduced). The contrast between the Q1 answer and subsequent feature-reaction answers is used as behavioral grounding evidence. A subject whose Q1 answer ignores their declared current-practice background is a C-05 violation on its face; the Q1 anchor makes this structurally visible. |
| C-14 | **Arc claims quote-anchored** | depth | aspirational | Every convergence or contradiction claim in the arc synthesis (C-11 dominant arc signal, C-12 critical contradiction) cites at least one verbatim SUBJECT turn per claim. A synthesis that asserts convergence or contradiction without sourcing the claim to a quoted subject turn fails this criterion. Applies equally to C-11 and C-12 content. |
| C-15 | **Contradiction both-sides sourced** | depth | aspirational | The critical contradiction named in C-12 has both sides cited verbatim -- one SUBJECT turn from each position in the contradiction. Naming and ranking the contradiction (C-12) without quoting both sides remains asserted on the unsourced side. C-12 is the floor (name + rank + evidential weight); C-15 is the ceiling (both sides source-verified). A single-sided citation fails C-15 even if C-12 passes. |
| C-16 | **Evidence columns non-substitutable** | depth | aspirational | Evidence Pull tables must carry both a verbatim Quote column and a Rationale column simultaneously. Quote provides source-verification (C-14); Rationale provides signal interpretation (C-10). Adding Quote does not discharge Rationale. A table with Quote and Confidence but no Rationale fails C-10 and fails C-16. A table with Rationale and Confidence but no Quote fails C-14 and fails C-16. Both columns must be present regardless of architecture; column additions are additive, not substitutive. |
| C-17 | **Roster-level disposition labels** | depth | aspirational | The advocate and skeptic dispositions required by C-11 must appear as explicit per-subject labels in the Human Subjects roster (or equivalent pre-interview declaration table) -- not only as inferences in synthesis-level arc analysis. A roster entry that names a subject and their role without a disposition label fails C-17 even if the synthesis correctly characterizes the advocate/skeptic arc. C-11 is the floor (arc addressed in synthesis); C-17 is the ceiling (disposition structurally declared per-subject at roster level). |
| C-18 | **Skeptic-first roster ordering** | depth | aspirational | The SKEPTIC subject is declared as S-01 (first position) in the roster and appears first in interview transcript order. The Arc Signal synthesis is framed as "skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence" -- not as a symmetric comparison between two equal voices. C-11 and C-17 require at least one explicit SKEPTIC and CHAMPION with per-subject labels; C-18 requires SKEPTIC declared first with Arc Signal synthesis derived from skeptic-as-prior-signal framing. A CHAMPION-first roster that satisfies C-11 and C-17 fails C-18. A SKEPTIC-first roster without the prior-signal framing in Arc Signal synthesis also fails C-18. Both the structural ordering and the framing derivation are required simultaneously. |
| C-19 | **Named compliance blocks with explicit failure conditions** | structure | aspirational | Structural compliance mechanisms for Evidence Pull table columns (C-10/C-16 requirements) and roster disposition labels (C-11/C-17 requirements) appear as named titled blocks -- e.g., COLUMN POLICY, DISPOSITION REQUIREMENT -- with itemized per-condition failure statements. Each failure condition names exactly what is absent and which criterion it violates by ID (e.g., "FAILS C-17", not "fails the structural requirement"). A template that satisfies C-16 through embedded prose fails C-19; one that satisfies it through a titled COLUMN POLICY block with explicit per-condition failure statements passes C-19 for that block. Both the column compliance block and the disposition compliance block must be present for C-19 PASS; one present without the other is PARTIAL. Named blocks are required because embedded prose rules are refactoring-vulnerable: they can be silently dropped during structural revision; a titled named block cannot be removed without being noticed. Two named blocks with itemized conditions but without criterion IDs = FAIL (0 pts); PARTIAL requires one-block structural incompleteness, not statement-quality failure. |
| C-20 | **Compliance blocks enumerate partial-compliance failure variants** | structure | aspirational | Named compliance blocks required by C-19 must additionally enumerate partial-structural-compliance failure conditions -- cases where one structural element is present but its complementary condition is absent. Required: DISPOSITION REQUIREMENT block must include "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18" as a named failure condition (structure met, framing absent). COLUMN POLICY block must include equivalent partial-compliance conditions for column coexistence failures (e.g., "Quote present but Rationale absent: FAILS C-10, FAILS C-16"). C-19 covers full-absence conditions; C-20 covers partial-presence conditions where the architecture is structurally complete on one axis but functionally incomplete on the complementary axis. A C-19-compliant block that enumerates only full-absence conditions fails C-20. Both blocks must cover their respective partial-compliance scenarios for PASS; one block covering partial-compliance without the other is PARTIAL. |
| C-21 | **Compliance blocks use three-column tabular structure** | structure | aspirational | Both compliance blocks required by C-19 (COLUMN POLICY and DISPOSITION REQUIREMENT) are formatted as three-column tables with explicit column headers covering: (1) the condition or case being evaluated, (2) what is absent or violated, and (3) the criterion(s) violated by ID. C-19 accepts any format -- prose bullets or tables -- as long as criterion IDs are cited; format is not material to C-19. C-21 is the structural ceiling: tabular format makes each failure condition machine-parseable, eliminates ambiguous multi-condition prose sentences, and enforces one-condition-to-one-criterion-row isolation that prose cannot guarantee. A prose-bullet block that satisfies C-19 fails C-21. Both blocks must be tabular for C-21 PASS; one tabular and one prose is PARTIAL. |
| C-22 | **Incumbent Coupling Table with switch-cost baseline** | depth | aspirational | A named Incumbent Coupling Table appears as a cross-interview structural artifact enumerating per-coupling-factor switching-cost ratings derived from the incumbent baseline interview. The table feeds a Switch Cost column in the Inertia Verdict Matrix synthesis. Required: (1) Incumbent Coupling Table present with at least one named coupling factor and a switching-cost baseline rating per factor; (2) Inertia Verdict Matrix includes a Switch Cost column whose entries are sourced from the Incumbent Coupling Table. The table is additive -- it supplements Evidence Pull tables without displacing the four required columns (Signal, Quote, Confidence, Rationale) from any row. C-09 is the floor (synthesis with Inertia Verdict Matrix exists); C-13 is the co-floor (current-practice Q1 anchor establishes the incumbent baseline that coupling factors draw from); C-22 is the ceiling (switching-cost baseline structured as a named coupling table that propagates into the synthesis verdict). A synthesis characterizing switching friction in prose without a named coupling table with per-factor ratings fails C-22. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Passing essential, weak recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite score |

Note: composite ceiling is 160 in v7 (70 aspirational pts). Golden threshold is still 80 --
achievable without any aspirational points.

---

## Partial Credit Reference

| Band | PASS | PARTIAL | FAIL |
|------|------|---------|------|
| Essential (12 pts each) | 12 | 8 | 0 |
| Recommended (10 pts each) | 10 | 3-7 | 0 |
| Aspirational (5 pts each) | 5 | 2-3 | 0 |

---

## Criterion Ladders

The aspirational section contains ladders where lower criteria are the floor and higher criteria
are the ceiling. Passing the ceiling without passing the floor is not possible by construction
(ceiling criteria require floor criterion content to be present first):

- **C-09 -> C-12**: C-09 is enumerating contradictions; C-12 is ranking them by evidential weight.
- **C-12 -> C-15**: C-12 is naming + ranking the critical contradiction; C-15 is sourcing both sides verbatim.
- **C-11 + C-14**: C-11 requires an arc synthesis claim; C-14 requires that claim to be quote-anchored.
- **C-11 -> C-17**: C-11 requires advocate/skeptic voices present and arc addressed in synthesis; C-17 requires per-subject disposition labels at roster level before synthesis begins.
- **C-10 + C-14 -> C-16**: C-10 requires Rationale; C-14 requires Quote; C-16 requires both columns to coexist in the same Evidence Pull table.
- **C-11/C-17 -> C-18**: C-11/C-17 require at least one SKEPTIC and one CHAMPION with per-subject roster labels; C-18 requires SKEPTIC declared as S-01 in roster order with Arc Signal synthesis framed as skeptic-resistance-as-prior-signal.
- **C-10/C-11/C-16/C-17 -> C-19**: All four require structural compliance for columns and dispositions; C-19 requires those compliance mechanisms appear as named titled blocks with explicit per-condition criterion-ID failure statements, not embedded prose.
- **C-19 -> C-20**: C-19 requires named compliance blocks with criterion-ID failure statements for full-absence conditions; C-20 requires those same blocks to additionally enumerate partial-structural-compliance failure variants (one structural condition present, complementary condition absent).
- **C-19 -> C-21**: C-19 accepts any format (prose or tabular) as long as criterion IDs are cited; C-21 requires both blocks use three-column tabular structure (Condition / What is absent / Criterion(s) violated).
- **C-09 + C-13 -> C-22**: C-09 requires a synthesis section with an Inertia Verdict Matrix; C-13 requires a current-practice Q1 anchor establishing the incumbent baseline; C-22 requires the incumbent switching-cost baseline to be structured as a named Incumbent Coupling Table that feeds a Switch Cost column into the Inertia Verdict Matrix. Both floor criteria must pass for C-22 to be gradable.

---

## Notes

- A "persona" in this skill is a simulated human, not a UI persona. The distinction matters for C-03: the answer must reflect the simulated human's perspective, not a product feature walkthrough.
- C-05 (grounded) is the hardest criterion to satisfy automatically. Evidence of grounding: the answer references the persona's industry, role-specific constraints, or documented concerns. Evidence of failure: the answer is universally applicable platitudes with no role-specific color. A Skeptic whose resistance is "change is hard" fails C-05 regardless of persona labeling.
- C-09 synthesis is only gradable when N >= 2 interview subjects exist. For single-subject interviews, C-09 is scored N/A (excluded from aspirational denominator).
- C-11 is only gradable when N >= 2 interview subjects exist with declared stances. If no disposition labels are present, score C-11 based on whether a structural advocate/skeptic contrast is present in the roles themselves (e.g., sponsor vs. end-user resistance). For single-subject runs, C-11 is N/A.
- C-12 requires the synthesis to explicitly rank contradictions, not merely enumerate them. A synthesis that says "Subject A said X; Subject B said Y" without evaluating which contradiction matters more fails C-12 even if C-09 passes.
- C-13 (current-practice Q1 anchor) is independent of C-05: it is possible to open with a Q1 anchor and still produce hollow Q1 answers (C-05 FAIL), or to achieve C-05 PASS without a Q1 anchor through dense prior-knowledge declaration. C-13 measures the structural mechanism, not its outcome.
- C-13 requires a within-interview Q1 position anchor. Cross-interview mechanisms (tension logs, traceability tables, incumbent coupling) create grounding infrastructure across subjects but do not satisfy the within-interview Q1 contrast requirement. C-13 FAIL if the interview opening question is grounded in prior knowledge and concerns but is not a neutral "what do you do today" question before any feature is introduced.
- C-14 requires a verbatim SUBJECT turn -- a turn that begins with the subject name or label, not the interviewer question. Paraphrasing a subject position does not satisfy C-14. Direct quotation does.
- C-15 is N/A when C-12 fails (no critical contradiction is named). Score C-15 only when C-12 PASS or PARTIAL is confirmed.
- C-16 is scored against the Evidence Pull table structure, not the synthesis section. An Evidence table is the per-subject extraction artifact (C-04 vehicle). If the output uses a different structural artifact for evidence extraction, apply the same column coexistence rule to that artifact.
- C-16 applies regardless of architecture. Incumbent-framing, coupling, and baseline architectures all add structural columns; none of these additions excuse removing Rationale. The additive rule is unconditional.
- C-17 requires roster-level labeling, meaning the label must appear before any interview transcript begins -- not as a synthesis conclusion. A synthesis that identifies "Subject A functioned as the skeptic" after the transcripts fails C-17. A roster row with an explicit SKEPTIC or equivalent disposition column before transcripts begin passes C-17.
- C-14 and C-15 now default to compliance in any well-structured C-12 implementation: all five R3 variations satisfied C-14 and C-15 through their Contradiction section cite-both-SUBJECT-turns-verbatim language, including variations designed to exclude them. C-14/C-15 isolation is no longer achievable without explicitly weakening the Contradiction structure.
- C-18 requires both the structural condition (SKEPTIC = S-01 in roster) and the framing condition (Arc Signal synthesis framed from skeptic-as-prior-signal). Neither alone is sufficient. A SKEPTIC-first roster with a symmetric two-voice Arc Signal comparison fails C-18 on framing. A CHAMPION-first roster with skeptic-prior framing in synthesis fails C-18 on structure (and also fails C-17 if roster labels are absent).
- C-19 PARTIAL: one named compliance block present (either COLUMN POLICY or DISPOSITION REQUIREMENT) but not both. C-19 PASS: both named blocks present with itemized per-condition criterion-ID failure statements. Named blocks that are present but lack itemized per-condition failure statements -- e.g., a titled section with only a prose description -- score PARTIAL regardless of completeness. Two named blocks with itemized conditions that cite "fails the structural requirement" instead of criterion IDs = FAIL (0 pts); PARTIAL requires one-block structural incompleteness, not statement-quality failure.
- C-19 and C-18 are orthogonally independent: a template can pass C-18 without C-19 (140/155) or pass C-19 without C-18 (140/155). Each criterion independently adds exactly 5 pts. Confirmed by R5 V-01 (C-18 PASS, C-19 FAIL) and V-02 (C-19 PASS, C-18 FAIL).
- C-20 PARTIAL: one of the two required blocks includes its respective partial-compliance failure variant; the other covers full-absence conditions only. C-20 PASS: both blocks enumerate their respective partial-compliance failure variants. C-20 requires C-19 PASS as a structural prerequisite -- partial-compliance conditions must appear within named titled blocks that already satisfy C-19.
- C-21 PARTIAL: one compliance block is formatted as a three-column table; the other remains prose-itemized. C-21 PASS: both blocks use three-column tabular structure with explicit column headers. C-21 requires C-19 PASS as a structural prerequisite -- tabular structure applies to named titled blocks, not to embedded prose compliance. Format is not material to C-19; tabular three-column structure is the sole distinguishing condition for C-21.
- C-20 and C-21 are independent of each other: a template can enumerate partial-compliance variants in prose bullets (C-20 PASS, C-21 FAIL) or use tabular format without partial-compliance variants (C-20 FAIL, C-21 PASS). Both are C-19-dependent floors. Confirmed by R6 V-01 (150, C-20 PASS + C-21 FAIL) and V-02 (152, C-20 PARTIAL + C-21 PASS).
- C-22 PARTIAL: Incumbent Coupling Table present without a Switch Cost column in the Inertia Verdict Matrix (coupling identified but not propagated to synthesis), or Switch Cost column in Inertia Verdict Matrix without a named Incumbent Coupling Table sourcing it (synthesis column without structural grounding). C-22 PASS: named Incumbent Coupling Table with at least one per-factor switching-cost rating, AND Inertia Verdict Matrix Switch Cost column explicitly sourced from the table. C-22 is N/A when C-09 fails (no synthesis exists) or C-13 fails (no incumbent current-practice baseline established). C-22 is additive-only: its presence cannot change Evidence Pull table column requirements; C-16 violations in Evidence tables are independent of C-22 status.
- C-11, C-12 added in v2 from V-03 (R1, 94/110). C-13, C-14, C-15 added in v3 from V-04 and V-05 (R2, both 110/110). C-16, C-17 added in v4 from R3 V-05 regressions (121/125 -- Rationale column drop, roster label drop). C-18, C-19 added in v5 from R4 excellence patterns: three perfect-ceiling 135/135 scores (V-03, V-04, V-05); SKEPTIC-first narrative superiority confirmed neutral to compliance but architecturally superior for evidential framing; named policy block refactoring-resistance confirmed by minimal-fix V-04 (only COLUMN POLICY + DISPOSITION REQUIREMENT added to R3 V-05 unchanged = 135/135). C-20, C-21 added in v6 from R5 excellence patterns: V-05 partial-compliance failure enumeration (6th DISPOSITION REQUIREMENT condition closing the half-C-18 loophole); V-04 tabular three-column format (format not material to C-19 but extractable as its own structural ceiling); R5 confirmed C-18/C-19 orthogonal independence with V-01 (140/145, C-19 FAIL) and V-02 (140/145, C-18 FAIL). C-22 added in v7 from R6 excellence patterns: V-05 Incumbent Coupling Table (switching-cost baseline per coupling factor feeding Inertia Verdict Matrix Switch Cost column); identified as pre-C-22 architecture investment -- additive, non-displacing, cross-interview structural artifact bridging incumbent baseline (C-13) and synthesis verdict (C-09); V-05 sole carrier at R6 ceiling; zero score impact in R6 because rubric did not yet include C-22.
