Written to `simulations/quest/rubrics/prove-interview-rubric-v4-2026-03-14.md`.

---

**What changed from v3 -> v4:**

Two new aspirational criteria extracted from R3 excellence patterns, both sourced from V-05's two misses (121/125):

---

**C-16 -- Evidence columns non-substitutable** (5 pts)
V-01, V-04, and V-05 all dropped the Rationale column when adding the verbatim Quote column, regressing on C-10 (partial, 3/5). V-02 and V-03 kept Confidence + Rationale and scored C-10 PASS. Quote and Rationale serve different purposes: Quote is source-verification (C-14); Rationale is signal interpretation (C-10). Neither column substitutes for the other. Column additions are additive. The canonical spec must carry both regardless of architecture.

**C-17 -- Roster-level disposition labels** (5 pts)
V-05 dropped explicit CHAMPION/SKEPTIC labels from the Human Subjects roster when refactoring. Arc Signal synthesis was strong at synthesis level -- but C-11's "explicit" requirement means per-subject roster labeling, not synthesis inference. A disposition inferrable from arc analysis but absent from the roster is not structurally declared. C-11 is the floor (arc addressed in synthesis); C-17 is the ceiling (disposition structurally declared per-subject at roster level, before any transcript begins).

---

**Point accounting:** Aspirational 35 -> 45 pts, ceiling 125 -> 135. Golden threshold stays at 80.

**New ladder entries added:**
- `C-11 -> C-17`: C-11 requires arc addressed in synthesis; C-17 requires labels in the roster.
- `C-10 + C-14 -> C-16`: C-10 requires Rationale; C-14 requires Quote; C-16 requires both to coexist.
-subject
in the roster (or equivalent pre-interview declaration), independent of whether synthesis
correctly characterizes the arc. C-11 is the floor (arc addressed in synthesis); C-17 is the
ceiling (disposition structurally declared per-subject at roster level). Synthesis that
identifies the arc correctly without roster-level labels passes C-11 but fails C-17.

**Point accounting:** Aspirational section 35 -> 45 pts, ceiling 125 -> 135. Golden threshold
stays at 80 -- still reachable without any aspirational points.

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

## Aspirational Criteria (45 points total)

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

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Passing essential, weak recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite score |

Note: composite ceiling is 135 in v4 (45 aspirational pts). Golden threshold is still 80 --
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
- C-11, C-12 added in v2 from V-03 (R1, 94/110). C-13, C-14, C-15 added in v3 from V-04 and V-05 (R2, both 110/110). C-16, C-17 added in v4 from R3 V-05 regressions (121/125 -- four points missed: C-10 partial from Rationale column drop, C-11 partial from roster label drop).
