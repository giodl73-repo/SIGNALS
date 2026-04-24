Looking at the three excellence signals, I'll extract them as C-23, C-24, and C-25, bump to v8, and recompute the formula.

---

## Rubric: `topic-echo` — v8

**Skill**: `topic:echo`
**Version**: v8
**Date**: 2026-03-16
**Criteria count**: 25 (4 essential / 3 recommended / **18** aspirational)

**Formula**: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/18 × 10)`

Each full aspirational pass ≈ **0.56 pts** (down from 0.67 in v7, denominator grew 15 → 18).

---

### Essential (4) — 60 pts total

| # | Criterion | Category |
|---|-----------|----------|
| C-01 | Minimum Entry Count | structure |
| C-02 | Signal Attribution | structure |
| C-03 | Surprise Framing | structure |
| C-04 | Actionability | structure |

**Pass condition**: All 4 required. Failure on any essential → score capped at 59 regardless of other criteria.

---

### Recommended (3) — 30 pts total

| # | Criterion | Category |
|---|-----------|----------|
| C-05 | Namespace Diversity Enforcement | enforcement |
| C-06 | Correction Register | schema |
| C-07 | Impact Double-Enforcement | enforcement |

---

### Aspirational (18) — 10 pts total

| # | Criterion | Category |
|---|-----------|----------|
| C-08 | Cross-Signal Synthesis | synthesis |
| C-09 | Counterfactual Awareness | epistemic |
| C-10 | Epistemic Delta Tracing | epistemic |
| C-11 | Non-Derivability Verification | epistemic |
| C-12 | Root-Cause Grouping | synthesis |
| C-13 | Signal Coverage Assessment | meta |
| C-14 | Redundancy Elimination | enforcement |
| C-15 | Structural Counterfactual Induction | schema |
| C-16 | Misunderstanding-Category Synthesis | synthesis |
| C-17 | Correction-Register Schema Design | schema |
| C-18 | Verification Audit Layer | enforcement |
| C-19 | Synthesis-Section Independence | meta |
| C-20 | Audit Scope Differentiation | enforcement |
| C-21 | Enforcement Pipeline Staging | enforcement |
| C-22 | Synthesis Verdict Commitment | meta |
| C-23 | Pre-Investigation Belief Inventory | epistemic |
| C-24 | Confidence-Weighted Triage | triage |
| C-25 | Surviving Belief Handover | synthesis |

---

### Three new criteria added

---

**C-23 | Pre-Investigation Belief Inventory** (aspirational, epistemic)

Encodes the R7 V-05 finding that C-12 (Root-Cause Grouping) had never been passed in seven rounds because triage ordering is not failure-mode categorization. V-05 solved it structurally by requiring a **Belief Inventory** before the investigation gate: a fixed set of falsifiable Competitor Beliefs, each with source and confidence level (HIGH/MEDIUM/LOW). Once beliefs are declared pre-gate, every surprise becomes the defeat of a named knowledge gap, and grouping by defeated belief is grouping by root-cause — no separate categorization step is required. The inventory is the precondition that makes C-12 achievable without post-hoc annotation.

Pass condition: ≥3 Competitor Beliefs declared before the entry gate in falsifiable form; each belief carries an explicit source and a confidence level (HIGH/MEDIUM/LOW); every surprise entry references the defeated belief by ID (e.g., `defeats: CB-{n}`). PARTIAL if beliefs are declared but confidence levels are absent or entries do not reference belief IDs. FAIL if no pre-gate belief inventory exists, or if beliefs are declared after entry collection begins.

Cross-reference: **C-23 PASS is the structural prerequisite for C-12 PASS** — root-cause grouping requires pre-declared beliefs to anchor. **C-23 PASS → C-14 strengthened**: redundancy check gains a tighter gate (two entries defeating the same belief ID are structurally redundant regardless of surface content). **C-23 PASS → C-11 tightened**: the non-derivability gate now tests against the fixed Competitor Set, not against an implicit prior.

---

**C-24 | Confidence-Weighted Triage** (aspirational, triage)

Encodes the R7 V-05 Signal 2 finding that triage ordering was previously calibrated solely to downstream consequence (what breaks if this surprise is ignored). V-05 introduced a second ranking axis: the epistemic weight of the defeated belief. Overturning a HIGH-confidence belief generates higher triage pressure than overturning a LOW-confidence belief, even when downstream consequence is equivalent. The mechanism decouples "importance of surprise" from "magnitude of impact" — a team that was certain about something and was wrong has a larger calibration debt than one that held a tentative belief. Without confidence weighting, triage systematically underranks surprises that expose structural overconfidence.

Pass condition: the triage step names Competitor Belief confidence as an explicit ranking modifier; the step spec states that HIGH-confidence defeat elevates triage priority relative to LOW-confidence defeat when downstream consequence is otherwise equal; the modifier is applied before the final triage ordering is produced. PARTIAL if confidence weighting is mentioned in narrative but not encoded as a step input to the triage decision. FAIL if triage ordering depends only on downstream consequence and does not reference belief confidence.

Cross-reference: **C-24 PASS requires C-23 PASS** — confidence weighting requires confidence levels declared in the pre-gate inventory. **C-24 and C-10 (Epistemic Delta Tracing) are additive**: C-10 traces what changed; C-24 weights how much the change matters given prior certainty.

---

**C-25 | Surviving Belief Handover** (aspirational, synthesis)

Encodes the R7 V-05 Signal 3 finding that the verdict section produced two output streams — defeated beliefs and surviving beliefs — but prior rubrics only scored the defeated stream. Surviving beliefs (those not contradicted by any entry) carry information: "we looked, found no signal, and this belief still stands." Without explicit surviving-belief output, the next team must rediscover which beliefs have already been stress-tested and found stable. The handover artifact converts surviving beliefs from a null result into a carry-forward asset. Omitting it creates epistemic waste proportional to the Competitor Set size — every belief that survived has to be re-declared and re-tested in the next round.

Pass condition: the synthesis section explicitly enumerates beliefs not defeated; each surviving belief is formatted as a carry-forward entry with status annotation (`SURVIVES: {belief} — no contradicting signal found across {n} entries`); the verdict distinguishes BELIEFS DEFEATED and BELIEFS SURVIVE as two separate output streams, each with its own list. PARTIAL if surviving beliefs are acknowledged in narrative but not formatted as a carry-forward artifact. FAIL if the verdict section reports only defeated beliefs, treats surviving beliefs as a null result with no output, or omits the surviving-belief category entirely.

Cross-reference: **C-25 and C-22 (Synthesis Verdict Commitment) are additive** — C-22 requires binary terminal states; C-25 requires that the BELIEFS SURVIVE state produces a named output artifact, not just a verdict label. **C-25 FAIL does not penalize C-22** — a binary verdict can still commit to DEFEATED/SURVIVE states even if the surviving stream is empty or unformatted. **C-25 PASS requires C-23 PASS** — a carry-forward artifact presupposes a pre-declared belief set to carry forward.

---

### Cross-Reference Summary (new dependencies added in v8)

| Dependency | Type | Effect |
|------------|------|--------|
| C-23 PASS → C-12 achievable | enabler | C-12 cannot reach PASS without pre-gate beliefs; C-23 FAIL → C-12 capped at PARTIAL |
| C-24 PASS requires C-23 PASS | prerequisite | Confidence weighting requires confidence levels from the inventory |
| C-25 PASS requires C-23 PASS | prerequisite | Surviving beliefs presuppose a pre-declared belief set |
| C-22 FAIL → C-13 cannot exceed PARTIAL | cap (from v7) | Hedged completeness language fails both C-22 and C-13 |
| C-21 and C-20 orthogonal | scope note (from v7) | Pipeline position vs. audit scope are independent dimensions |

---

### Scoring Reference

| Band | Score Range |
|------|-------------|
| Gold | ≥ 97.00 |
| Silver | 90.00–96.99 |
| Bronze | 80.00–89.99 |
| Below threshold | < 80.00 |

**V-05 score under v8 formula**:
- Essential: 60
- Recommended: 30
- Aspirational: C-23 PASS + C-24 PASS + C-25 status TBD; prior 14.5/15 → denominator now 18
- If V-05 passes all three new criteria: 17.5/18 × 10 = **9.72** → total **99.72**
- If C-25 PARTIAL (surviving beliefs acknowledged but not formatted): 17.0/18 × 10 = **9.44** → total **99.44**
