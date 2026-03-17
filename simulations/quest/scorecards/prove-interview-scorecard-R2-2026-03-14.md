Scorecard written to `simulations/quest/scorecards/prove-interview-scorecard-R2-2026-03-14.md`.

---

## prove-interview Round 2 Scores

| Rank | Variation | Score | Golden | Essential |
|------|-----------|-------|--------|-----------|
| 1 | **V-05** Full ceiling candidate | **110/110** | YES | ALL PASS |
| 2 | **V-04** Disposition arc + current-practice Q1 | **110/110** | YES | ALL PASS |
| 3 | **V-01** Arc Diagnosis checkpoint | 106/110 | NO | C-05 partial |
| 4 | **V-03** Two-phase synthesis | 106/110 | NO | C-05 partial |
| 5 | **V-02** Ranked contradiction inventory | 101/110 | NO | C-05+C-08 partial, C-11 partial |

---

### Why V-04 and V-05 both hit 110

The root of the C-05 partial in V-01/V-03 is structural: profile declarations can sound role-appropriate without being behaviorally grounded. The **current-practice Q1 anchor** closes this — a Q1 answer that ignores declared current practice is immediately visible as a violation. V-04 and V-05 both carry this mechanism. Same gap, same fix.

V-05 ranks first over V-04 (both 110) for one structural innovation: **quote-anchored arc synthesis**. Every C-11/C-12 claim must cite a SUBJECT turn verbatim. This converts aspirational criteria from asserted conclusions into source-verified claims — the same shift that made C-04/C-10 reliable (evidence table with required source reference), now applied to synthesis.

### Three new patterns

1. **Current-practice Q1 anchor** — neutral current-practice question before any feature question forces behavioral grounding. The contrast between Q1 and feature reaction is where the C-05 evidence lives.

2. **Quote-anchored arc synthesis** — requiring verbatim SUBJECT turn citations for every arc claim makes C-11/C-12 structurally gradable rather than asserted. Generalizes across all prove-* skills for aspirational synthesis criteria.

3. **Both-sides SUBJECT quotes at Rank 1** — requiring both sides of the critical contradiction to be cited verbatim makes C-12 source-verifiable, not just named and ranked. V-02 proved the floor (column asymmetry); V-05 establishes the ceiling.

### R2 research question verdicts

- **Q1** (Arc Diagnosis vs. Phase 4B): Both produce C-11 PASS. V-01 is more reliable for false-convergence prevention; V-03 produces deeper reasoning. Failure-mode dependent.
- **Q2** (Column asymmetry alone for C-12): **Confirmed.** V-02 hits C-12 PASS without disposition ordering. C-11 and C-12 are architecturally independent.
- **Q3** (Quote-anchoring for gradability): **Confirmed.** V-05 C-11/C-12 strongest in the round. Pattern should migrate to canonical spec.

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Current-practice Q1 anchor: neutral current-practice question before feature question forces behavioral grounding that makes C-05 violations structurally visible", "Quote-anchored arc synthesis: requiring verbatim SUBJECT turn citations for every C-11/C-12 claim converts aspirational criteria from asserted conclusions to source-verified claims", "Both-sides SUBJECT quotes at Rank 1: requiring verbatim quotes from both sides of the critical contradiction makes C-12 source-verifiable not just named and ranked"]}
```
eanest single-mechanism C-11 enforcement in the round: binary forced before synthesis, rationale must cite specific exchange, red-flag check explicit. Synthesis must be consistent with Arc Diagnosis or correct the inconsistency. |
| C-12 | PASS | 5 | `Critical contradiction:` synthesis field requires naming the contradiction, citing which E-IDs are in tension, and explaining evidential weight (confirm / undermine / leave unresolved). |

**Composite: 106/110**
Essential: 56/60 (C-05 partial) | Recommended: 30/30 | Aspirational: 20/20
All C-01..C-05 pass: **NO** (C-05 = 8/12)
Golden: NO

---

## V-02: Output Format -- Ranked Contradiction Inventory

**Axis:** Minimal structural change: one new section (Contradiction Inventory) inserted between
evidence extraction and synthesis. Rank 1 has a required `Evidential weight` column absent from
lower ranks. Column asymmetry forces ranking to be structural rather than advisory.
Disposition labels optional -- isolation test for C-12 independence from disposition ordering.

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Subject profiles table with Role/Title column required before interviews. |
| C-02 | PASS | 12 | "Prior knowledge (what they know)" and "Knowledge gaps" columns in profiles table. |
| C-03 | PASS | 12 | "If S-01's and S-02's answers are interchangeable, the persona declarations failed." Evidence items must be "specific enough that it could not have come from a persona with different declared knowledge." |
| C-04 | PASS | 12 | Evidence table required per subject, minimum one row. |
| C-05 | PARTIAL | 8 | No behavioral anchor, no Skeptic resistance taxonomy. Evidence specificity grounding test ("could this item have come from a persona with different declared knowledge?") is the only structural C-05 enforcement. Weakest C-05 coverage in the round. |
| C-06 | PASS | 10 | `Surprising moment:` field per interview. |
| C-07 | PASS | 10 | Open-ended requirement, labeled FOLLOW-UP required. |
| C-08 | PARTIAL | 7 | Disposition column marked "champion / neutral / skeptic / unspecified" -- optional. No enforcement that subjects have meaningfully different roles beyond the "interchangeable answers" check. Minimum two subjects required but differentiation is advisory. |
| C-09 | PASS | 5 | Synthesis section with convergence, critical contradiction, dominant arc signal, strongest signal, open question. |
| C-10 | PASS | 5 | Confidence + Rationale columns in evidence tables. |
| C-11 | PARTIAL | 3 | Disposition column optional. Synthesis "Dominant arc signal" field is conditional: "If dispositions declared... If no dispositions declared: N/A." C-11 is structurally skippable. When dispositions are declared, the field is present but shallow compared to V-01/V-03 mechanisms. |
| C-12 | PASS | 5 | Ranked Contradiction Inventory with Rank 1 requiring `Evidential weight` column absent from lower ranks. Column asymmetry is clean structural enforcement. "Why does it matter more than the others? Which E-IDs from each side are load-bearing?" C-12 isolation test: PASS confirmed without disposition ordering. |

**Composite: 101/110**
Essential: 56/60 (C-05 partial) | Recommended: 27/30 (C-08 partial) | Aspirational: 18/20 (C-11 partial)
All C-01..C-05 pass: **NO** (C-05 = 8/12)
Golden: NO

**Key finding:** C-12 PASS confirmed without disposition ordering. C-11 and C-12 are architecturally
independent. The gap from C-09 to C-12 is a structural ranking column -- column asymmetry drives
compliance; content quality of "evidential weight" framing also matters per the Rank 1 field
instructions. R2 research question 2 directionally confirmed.

---

## V-03: Lifecycle -- Two-Phase Synthesis

**Axis:** Synthesis lifecycle separation: Phase 4A covers evidence patterns (C-09 content),
Phase 4B covers arc analysis (C-11/C-12 content). Phase gates prevent arc analysis from
merging with evidence summary. Phase 4B questions are explicitly unanswerable by restating
Phase 4A content. No role-sequence enforcement -- tests lifecycle separation alone.

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Phase 1 roster with Role/Title column. Phase 1 gate: "at least two subjects declared with role, prior knowledge, gaps, concern, and disposition." |
| C-02 | PASS | 12 | Phase 1 roster has "Prior knowledge" and "Knowledge gaps" columns. Phase 1 gate checks these explicitly. |
| C-03 | PASS | 12 | "Answers must stay in declared persona voice. Phase 1 profiles are locked -- do not modify prior knowledge or disposition here. Generic answers that could come from any persona are a Phase 1 lock violation." Strongest C-03 phase discipline in the round. |
| C-04 | PASS | 12 | Phase 3 dedicated entirely to evidence extraction. Phase 3 gate: "at least one evidence row per subject," "each evidence item is specific (not 'Subject had concerns' -- name the concern)," "no new interview content introduced in Phase 3." |
| C-05 | PARTIAL | 8 | Phase 1 lock prevents answers from introducing undeclared knowledge, making C-05 violations structurally visible post-hoc. But no behavioral Q1 forcing -- a persona with generic role-appropriate-sounding prior knowledge can still produce plausible-but-hollow Q1 answers. Same structural gap as V-01. |
| C-06 | PASS | 10 | Surprising moment field in Phase 2, with "Do not extract evidence here" keeping discovery and extraction in separate phases. |
| C-07 | PASS | 10 | Minimum 3 exchanges per subject, labeled FOLLOW-UP required. Phase 2 gate checks labeled follow-ups explicitly. |
| C-08 | PASS | 10 | Phase 1 roster requires 2+ subjects with distinct declared profiles. Disposition field present even if optionally unspecified. Role declarations enforce differentiation. |
| C-09 | PASS | 5 | Phase 4A dedicated: convergence (with E-IDs), strongest signal (with E-ID + rationale), evidence gap. Phase gate prevents arc analysis contamination. |
| C-10 | PASS | 5 | Phase 3 gate explicitly: "Confidence level declared with one-line rationale for each item." Strongest C-10 gate enforcement in the round. |
| C-11 | PASS | 5 | Phase 4B comprehensive: arc present (YES/NO/PARTIAL), dominant signal (CONVERGENCE/CONTRADICTION/INCONCLUSIVE), red flag check, critical contradiction, arc meaning synthesis. Phase 4B questions explicitly unanswerable by Phase 4A restatement -- best reasoning-depth C-11 mechanism in the round. Risk: disposition is technically optional, making Phase 4B skippable if unspecified. |
| C-12 | PASS | 5 | Phase 4B `Critical contradiction:` field with "single most significant contradiction... state which E-IDs are in tension... explain its evidential weight... A synthesis that names multiple contradictions in parallel without ranking them fails this field." Rubric language incorporated directly. |

**Composite: 106/110**
Essential: 56/60 (C-05 partial) | Recommended: 30/30 | Aspirational: 20/20
All C-01..C-05 pass: **NO** (C-05 = 8/12)
Golden: NO

**Tie with V-01 at 106.** Differentiator: V-03 has stronger C-04 (Phase 3 gate) and C-10
(Phase 3 gate), stronger C-11 reasoning depth (Phase 4B unanswerable-by-restatement constraint).
V-01 has cleaner C-11 binary commitment and Skeptic resistance taxonomy. Both fail C-05 PASS
for the same structural reason: no behavioral Q1 anchor.

---

## V-04: Disposition Arc + Current-Practice Q1

**Axes:** Disposition ordering (Champion/Neutral/Skeptic) + declared current-practice field per
subject + current-practice Q1 mandatory for every interview. Direct test of R1 open research
question: does behavioral anchoring per disposition close both C-05 and C-11 gaps simultaneously?

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Explicit S-01/S-02/S-03 profiles with title and domain required before interviews. |
| C-02 | PASS | 12 | Prior knowledge + Gaps fields per profile declared before any interview. |
| C-03 | PASS | 12 | Q1 answer must reference "declared current practice." Answers that ignore declared current practice are structurally visible as violations. "Not interchangeable with S-01's or S-02's Q1 answer." |
| C-04 | PASS | 12 | Evidence tables per subject with grounding test: "Could this item have been said by a persona with a different declared current practice? If yes, not grounded enough." Minimum rows required. |
| C-05 | PASS | 12 | Current-practice Q1 anchor is a full C-05 solution. Behavioral baseline forces role-specific answers at Q1. Skeptic current practice describes "what they are defending, what failed before, or the constraint they are enforcing" -- not a stance, a behavior. Evidence grounding test explicitly references current practice. Generic answers have nowhere to hide. |
| C-06 | PASS | 10 | Surprising moment field per interview with specific framing: "Did S-01's current-practice description reveal a constraint the opening did not suggest?" Current-practice frame creates more specific surprising-moment detection than profile-only approaches. |
| C-07 | PASS | 10 | Minimum 3 exchanges for Champion/Neutral, Skeptic gets Q4 (conditions-for-satisfaction) making 4 exchanges minimum for the most important interview. |
| C-08 | PASS | 10 | Three distinct dispositions + "Must differ meaningfully from Champion's" for Neutral current practice + Skeptic domain differentiated. |
| C-09 | PASS | 5 | Synthesis with 5 cross-interview dimensions: current-practice comparison, feature-reaction contrast, dominant arc signal, critical contradiction, what current-practice anchoring revealed. |
| C-10 | PASS | 5 | Evidence tables with confidence + rationale per item. |
| C-11 | PASS | 5 | Disposition ordering + behavioral current-practice grounding makes disposition authenticity harder to fake. Synthesis `Dominant arc signal:` asks "Did the Skeptic's current-practice grounding make their resistance more or less surmountable than a stance-only Skeptic?" -- addresses C-11's core question with behavioral evidence. |
| C-12 | PASS | 5 | `Critical contradiction:` synthesis field: "Name which E-IDs are in tension. Explain its evidential weight... Why is this the most evidentially consequential contradiction -- not the most dramatic, but the one that most changes the answer to the interview question?" The "not the most dramatic" distinction is the sharpest C-12 framing in the round. |

**Composite: 110/110**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 20/20
All C-01..C-05 pass: **YES**
Golden: **YES**

---

## V-05: Full R2 Ceiling Candidate

**Axes:** All R2 primary mechanisms: disposition ordering + current-practice Q1 + INTERVIEWER:/SUBJECT:
transcript format + EVIDENCE PULL with verbatim Quote column + ranked Contradiction Inventory with
both-sides SUBJECT quotes at Rank 1 + quote-required arc synthesis (every C-11/C-12 claim must
cite a SUBJECT turn verbatim).

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Explicit disposition-labeled profiles (S-01 CHAMPION / S-02 NEUTRAL / S-03 SKEPTIC) with title and domain required. Profile lock enforced. "A Champion with no real enthusiasm or a Skeptic with no role-grounded resistance is a profile failure, not a finding." |
| C-02 | PASS | 12 | Prior knowledge + Gaps + Stakes + `Assumption to test` fields per profile. "Assumption to test" makes a verifiable claim per persona -- strongest C-02 declaration structure in the round. |
| C-03 | PASS | 12 | INTERVIEWER:/SUBJECT: format makes persona voice visible and auditable per turn. "The answer is not interchangeable with any other subject's Q1 answer." Transcript format makes C-03 failures identifiable at the turn level. |
| C-04 | PASS | 12 | EVIDENCE PULL with verbatim Quote column (not paraphrase). Minimum 2 rows per subject. Quote column provides turn-level verification of each evidence item. |
| C-05 | PASS | 12 | Current-practice Q1 anchor + INTERVIEWER:/SUBJECT: format makes generic answers visible at the turn level + evidence rationale must reference "declared current practice or prior knowledge" + Skeptic current practice is "most important current-practice declaration in the session." Strongest C-05 structural enforcement in the round. |
| C-06 | PASS | 10 | SURPRISE field requires verbatim quote of surprising turn + "Assumed: [profile assumption]. Revealed: [what the answer showed instead]." Strongest C-06 structure in the round -- contradiction with declared assumption is explicit and auditable. |
| C-07 | PASS | 10 | INTERVIEWER:/SUBJECT: format with labeled FOLLOW-UPs. Minimum 3 INTERVIEWER turns per subject. Format makes question quality auditable at the turn level. |
| C-08 | PASS | 10 | Three distinct dispositions with behavioral grounding. Different domains required per subject. |
| C-09 | PASS | 5 | Synthesis section present with current-practice comparison, dominant arc signal, critical contradiction, what current practice revealed. |
| C-10 | PASS | 5 | EVIDENCE PULL Confidence + Rationale columns per item. Verbatim Quote column adds an additional verifiability layer beyond confidence marker. |
| C-11 | PASS | 5 | Quote-required arc synthesis: "Every arc synthesis claim must cite a direct SUBJECT turn verbatim. No arc claim without a source quote." Arc dominant signal field requires verbatim Skeptic SUBJECT turn citation. Arc red flag check requires SUBJECT turn citation. Makes C-11 structurally gradable -- claims are source-verified, not asserted. Strongest C-11 mechanism in the round. |
| C-12 | PASS | 5 | Contradiction Inventory Rank 1 requires Evidential Weight + Quote A + Quote B (both-sides SUBJECT turns verbatim). C-12 synthesis field references Inventory Rank 1. "What this contradiction *means* for the interview question -- not just which subjects disagreed, but what it changes about the answer." Both-sides quotes make C-12 source-verifiable. Strongest C-12 mechanism in the round. |

**Composite: 110/110**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 20/20
All C-01..C-05 pass: **YES**
Golden: **YES**

---

## Round 2 Rankings

| Rank | Variation | Score | Essential | Golden | Key differentiator |
|------|-----------|-------|-----------|--------|-------------------|
| 1 | V-05 (Full ceiling candidate) | 110/110 | ALL PASS | YES | Quote-anchored arc synthesis makes C-11/C-12 structurally gradable rather than asserted |
| 2 | V-04 (Disposition arc + current-practice Q1) | 110/110 | ALL PASS | YES | Current-practice Q1 closes C-05 gap; sharpest C-12 framing ("not the most dramatic") |
| 3 | V-01 (Arc Diagnosis checkpoint) | 106/110 | C-05 PARTIAL | NO | Cleanest C-11 binary mechanism; Skeptic taxonomy strong; no behavioral anchor |
| 4 | V-03 (Two-phase synthesis) | 106/110 | C-05 PARTIAL | NO | Best C-11 reasoning depth (unanswerable-by-restatement); strongest Phase gate discipline |
| 5 | V-02 (Ranked contradiction inventory) | 101/110 | C-05 PARTIAL | NO | C-12 isolation test confirmed; C-11 structurally optional; C-08 weakest |

V-05 ranked above V-04 (both 110) on structural innovation: quote-anchored arc synthesis is the
R2 architectural contribution with highest generalization value across prove-* skills. V-04 ranked
second for achieving full criteria pass with lower structural complexity.

---

## Excellence Signals (from V-04 + V-05)

### Signal 1: Current-practice Q1 anchor closes the C-05 gap

V-01 and V-03 scored PARTIAL on C-05 despite strong profile declaration requirements. The
structural gap: declared knowledge can sound role-appropriate without being behaviorally grounded.
V-04 and V-05 close this by opening every interview with a neutral question about current practice
before any feature question is asked. The behavioral constraint is structural: a Q1 answer that
ignores declared current practice is a visible C-05 violation. The grounding test ("Could this
item have come from a persona with a different declared current practice?") is the diagnostic the
Q1 anchor enables.

**Implication:** Current-practice Q1 should be the default opening structure for any prove-interview
session where C-05 grounding matters. The pattern applies across prove-* skills where persona
behavior (not just knowledge) is the evidence source.

### Signal 2: Quote-anchored arc synthesis makes aspirational criteria structurally gradable

V-01's Arc Diagnosis checkpoint and V-03's Phase 4B both produce C-11 PASS -- but the claims
they require are assertions. "The arc was convergence-dominant because the Skeptic named conditions"
is a conclusion, not a citation. V-05 changes this: every arc claim must cite a SUBJECT turn
verbatim. The same shift that made C-04/C-10 reliable (evidence table with required source
reference) applied to synthesis claims.

**Implication:** Quote-anchoring is the generalizable mechanism for converting aspirational criteria
from asserted to structurally gradable. The pattern applies to any aspirational criterion whose
pass condition is a synthesis claim. Candidate for migration into the canonical prove-interview
spec and into other prove-* skills as the standard mechanism for C-11/C-12 equivalents.

### Signal 3: Both-sides SUBJECT quotes at Rank 1 makes C-12 source-verifiable

V-02 proved C-12 can be achieved with column asymmetry alone (Rank 1 requires Evidential Weight
field). V-05 extends this: Rank 1 also requires verbatim quotes from both sides of the
contradiction. This changes C-12 from "named and ranked" to "named, ranked, and source-verified."
Without both-sides quotes, a synthesis can claim a critical contradiction without providing the
turn-level evidence. V-05's requirement prevents this.

**Implication:** V-02 column asymmetry is the C-12 floor. V-05 both-sides quotes are the C-12
ceiling. The v3 rubric should consider whether C-12 pass condition should require source citation
(current v2 pass condition does not explicitly require it).

---

## R2 Research Questions -- Verdicts

**Q1: Arc Diagnosis checkpoint (V-01) vs. Phase 4B arc phase (V-03)?**

Both produce C-11 PASS at 106/110. V-01's binary commitment is faster to satisfy correctly;
V-03's Phase 4B produces deeper arc reasoning (unanswerable-by-restatement constraint forces
genuine analysis rather than conclusion restatement). For production reliability, V-01's binary
is more predictable. For reasoning depth, V-03 is stronger. Verdict: depends on failure mode.
V-01 for false-convergence prevention. V-03 for shallow-arc prevention.

**Q2: Does Rank 1 column asymmetry alone produce C-12 PASS (V-02)?**

Yes -- V-02 scores C-12 PASS (5/5). C-11 and C-12 are architecturally independent. The gap
from C-09 to C-12 is a structural ranking column. Content quality instruction for "evidential
weight" also matters, but column presence drives compliance. Verdict: confirmed, C-12 is
format-neutral for disposition ordering.

**Q3: Does SUBJECT quote requirement on arc synthesis make C-11/C-12 structurally gradable (V-05)?**

Yes -- V-05 scores C-11/C-12 PASS with the strongest mechanism in the round. Quote-anchoring
converts aspirational criteria from assertions to source-verified claims. Verdict: confirmed.
The pattern should migrate into v-next canonical spec as the standard mechanism for all
aspirational synthesis claims across prove-* skills.
