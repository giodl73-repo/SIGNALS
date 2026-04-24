Scorecard written to `simulations/quest/scorecards/prove-hypothesis-scorecard-R1-2026-03-14.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Skeptic role creates explicit PASS/REWRITE verdict per falsification condition -- stronger C-02 enforcement than observable column alone", "Hard phase gate checklist with read-only constraint on prior phase is the strongest structural enforcement for C-05 (no goalpost movement)", "Status-quo interrogated as a competing hypothesis in a challenge phase produces deeper inertia evaluation than F-00 as a falsification condition", "Risk-rationale column alongside rank column satisfies C-10 pass condition; rank-only columns fail the 'with rationale' requirement"]}
```

---

**Summary:**

All 5 variations are golden. C-10 is the only discriminator between the groups:

- **V-04 and V-05 (score 100):** Both have a rationale column alongside rank. V-04's differentiator is the Skeptic role — the most rigorous structural gate for C-02. V-05's differentiator is the hard GATE 2 checklist — the strongest structural enforcement for C-05.
- **V-01 and V-03 (score 95):** Both miss C-10 because they have rank columns but no rationale column. V-03 adds inertia value beyond the rubric (richer C-08 requirement) but it doesn't change the score.
- **V-02 (score 90):** Question-driven prose achieves all 5 essential + all 3 recommended criteria with no tables. It only fails C-09 and C-10, confirming conversational format is sufficient for the core skill — just not the aspirational bar.

**R2 hypothesis:** Combine V-04's Skeptic gate (strongest C-02) with V-05's phase checklist (strongest C-05) and status-quo-as-competing-hypothesis framing into a single variation to test whether stacking the top mechanisms produces live-run quality gains or friction from complexity.
ication conditions after the HYPOTHESIS DECLARED gate" |
| C-06 | PASS | Dedicated "SETUP: PRIOR SIGNALS" section; must list files or "None -- starting fresh" |
| C-07 | PASS | "CONFIRMATION CONDITIONS" section with CF-01 row required |
| C-08 | PASS | Rationale must "cite at least one specific prior signal, trace finding, or known friction point"; prior-free note required if absent |
| C-09 | PASS | Pre-printed "Falsification conditions tested" column in experiment table with F-ID references |
| C-10 | PARTIAL | Rank column + "Rank 1 = highest falsification risk" present; no rationale column -- pass condition requires "with rationale" -- scored FAIL |

**essential 5/5 -> 60 | recommended 3/3 -> 30 | aspirational 1/2 -> 5**
**Composite: 95** | Golden: YES

---

## V-02: Phrasing Register (Conversational)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Step 2: "Write one sentence that could, in principle, turn out to be false. Avoid hedged language." |
| C-02 | PASS | "Each condition should describe an observable outcome... if it depends on opinion, rewrite it." No structural gate but instruction is explicit |
| C-03 | PASS | "Give a number from 0 to 100." Explicit |
| C-04 | PASS | Valid sub-skills enumerated; 2-item template minimum; "each experiment should name one of the prove sub-skills" |
| C-05 | PASS | Opening: "Before looking at any evidence, write down what you believe and commit to it. The claim and falsification conditions are locked." Behavioral framing -- weakest structural enforcement of the five |
| C-06 | PASS | Step 1 requires explicit note: "list files or 'None found -- confidence below is prior-free.'" |
| C-07 | PASS | Step 4: "Name at least one condition that would confirm the claim if observed." |
| C-08 | PASS | "reference at least one specific anchor -- prior finding, trace result, or named friction point. If none: 'No prior signals -- this confidence is based on...'" -- friction point anchor covers zero-prior-artifact scenario |
| C-09 | FAIL | No structural element mapping experiments to F-IDs; pure prose listing |
| C-10 | FAIL | "Start with the experiment most likely to falsify the claim" -- ordering hint only, no rationale required or column present |

**essential 5/5 -> 60 | recommended 3/3 -> 30 | aspirational 0/2 -> 0**
**Composite: 90** | Golden: YES

---

## V-03: Inertia Framing (Status-Quo as F-00)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "HYPOTHESIS DECLARED" gate; "Use 'is' or 'will'. No hedging." |
| C-02 | PASS | "Observable test" column on all rows including F-00; no binary yes/no gate -- weaker than V-01 but structurally guided |
| C-03 | PASS | "Value: [N]/100"; rationale requires two sub-questions -- richer calibration requirement than V-01 |
| C-04 | PASS | Rank table with prove sub-skill column; 2-row minimum; "include at least one experiment that tests F-00" |
| C-05 | PASS | "HYPOTHESIS DECLARED" before FALSIFICATION CONDITIONS; section ordering same strength as V-01 |
| C-06 | PASS | "SETUP: PRIOR SIGNALS" section required |
| C-07 | PASS | "CONFIRMATION CONDITIONS" with CF-01 required |
| C-08 | PASS | Rationale requires both F-00 calibration ("why does status quo NOT already satisfy the need?") and prior signal/friction anchor -- richer than V-01 on this criterion |
| C-09 | PASS | Pre-printed "Falsification conditions tested" column with F-ID references |
| C-10 | PARTIAL | Rank column present + "highest falsification risk first"; no rationale column -- scored FAIL |

**essential 5/5 -> 60 | recommended 3/3 -> 30 | aspirational 1/2 -> 5**
**Composite: 95** | Golden: YES

---

## V-04: Role Sequence + Output Format (Claimant / Skeptic / Navigator)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "CLAIMANT: DECLARE" section; "One sentence. Use 'is' or 'will'." |
| C-02 | PASS | Strongest enforcement: Skeptic writes explicit PASS/REWRITE verdict per condition before confidence is written; subjective conditions cannot silently pass |
| C-03 | PASS | "CLAIMANT: CONFIDENCE" section after Skeptic gate; "Value: [N]/100" |
| C-04 | PASS | "NAVIGATOR: EXPERIMENTS" table; prove sub-skill column; 2-row minimum |
| C-05 | PASS | Phase gate: "Do not adjust the Claimant's claim or falsification conditions after the Skeptic gate." |
| C-06 | PASS | Prior signals check in CLAIMANT: DECLARE; list files or "None -- starting fresh" |
| C-07 | PASS | "SKEPTIC: CONFIRM" dedicated section; CF-01 row required |
| C-08 | PASS | "Reference at least one specific prior signal, trace finding, or known friction point... Do not omit the prior-evidence note." |
| C-09 | PASS | Navigator table "Falsification conditions tested" column with F-ID references; "Cover all falsification conditions across the experiment set" |
| C-10 | PASS | Navigator table has both Rank and "Why this risk rank" columns -- only variation with rationale column alongside rank |

**essential 5/5 -> 60 | recommended 3/3 -> 30 | aspirational 2/2 -> 10**
**Composite: 100** | Golden: YES

---

## V-05: Lifecycle Emphasis + Inertia Framing

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | PHASE 2: "One sentence. Use 'is' or 'will'. No hedging." GATE 2 checklist item: "Claim is one sentence with no hedging" -- two-layer enforcement |
| C-02 | PASS | GATE 2 checklist: "Each condition describes an observable outcome." PHASE 3 has per-F-ID observability check table. GATE 3 requires all F-IDs observability-checked. Multi-gate enforcement |
| C-03 | PASS | PHASE 2: "Confidence: [N]/100"; GATE 2 checklist item confirms numeric + rationale required |
| C-04 | PASS | PHASE 4 PLAN table with prove sub-skill column; "Every falsification condition must be covered by at least one experiment" |
| C-05 | PASS | Strongest enforcement: GATE 2 checklist "No evidence from future phases referenced here." PHASE 3 read-only on PHASE 2 output; observability failures logged as amendments, not retroactive edits |
| C-06 | PASS | PHASE 1 SETUP: prior signals required with one-line summaries; GATE 1 checklist item |
| C-07 | PASS | PHASE 2 DECLARE includes "The claim is confirmed if ANY of: CF-01" |
| C-08 | PASS | "Cite at least one anchor from SETUP prior signals or status-quo baseline. Do not omit an explicit anchor statement." Status-quo baseline is always available even with zero prior artifacts |
| C-09 | PASS | PHASE 4 PLAN table "Falsification conditions tested" column; "Every falsification condition must be covered" |
| C-10 | PASS | PHASE 4 PLAN table has Rank + "Risk rationale" column |

**essential 5/5 -> 60 | recommended 3/3 -> 30 | aspirational 2/2 -> 10**
**Composite: 100** | Golden: YES

---

## Rankings

| Rank | Variation | Score | Golden | Key differentiator |
|------|-----------|-------|--------|--------------------|
| 1 | V-04 Role Sequence + Output Format | 100 | YES | Skeptic role (C-02) + risk-rationale column (C-10) |
| 1 | V-05 Lifecycle Emphasis + Inertia Framing | 100 | YES | Hardest C-05 gate + status-quo as competing hypothesis |
| 3 | V-01 Output Format (Table-Structured) | 95 | YES | Strong C-02 binary gate; C-10 lacks rationale column |
| 3 | V-03 Inertia Framing | 95 | YES | Richer C-08 rationale; C-10 lacks rationale column |
| 5 | V-02 Conversational | 90 | YES | All essentials + recommended pass; C-09/C-10 structurally absent |

C-10 is the primary discriminator. V-04 and V-05 include rationale columns alongside rank; V-01
and V-03 have rank-only; V-02 has an ordering hint only.

All five variations are golden (all 5 essential pass, composite >= 80). V-02 confirms that
question-driven prose achieves full essential + recommended coverage without tables -- the gap
is exclusively at the aspirational level.

---

## Excellence Signals

**ES-01 -- Skeptic role as explicit observability gate (V-04)**
The Skeptic writes a named PASS/REWRITE verdict per falsification candidate before confidence is
written. Subjective conditions cannot silently pass -- they require a written verdict. Column-based
approaches (V-01/V-03) depend on the model self-policing the "Observable?" column; the Skeptic
role makes the check a named act with a visible record.

**ES-02 -- Hard gate checklist for C-05 (V-05)**
GATE 2 has explicit checklist item "No evidence from future phases referenced here" and PHASE 3
is declared read-only on DECLARE output. This converts the no-goalpost-movement guarantee from
a section-ordering convention into a structural constraint auditable in the output. V-04
approximates with a phase gate instruction; V-01/V-03 rely on section ordering alone.

**ES-03 -- Status-quo as competing hypothesis, not just a falsification condition (V-05)**
PHASE 3 interrogates inertia as "The team gets equivalent value by doing nothing" -- a
first-class alternative hypothesis requiring an explicit yes/no verdict before experiment
planning begins. V-03's F-00 is a list row; V-05's framing forces active evaluation of
status-quo plausibility, producing richer experiment rationale.

**ES-04 -- Risk-rationale column alongside rank (V-04, V-05)**
Both top variations add "Why this risk rank" / "Risk rationale" columns to the experiment table,
satisfying C-10's "with rationale" pass condition. V-01 and V-03 have rank-only columns, dropping
one aspirational point. The rationale column also produces richer artifacts for downstream skills.

---

## Open Questions for R2

1. Does the Skeptic role in V-04 materially improve falsification condition quality on live runs
   relative to V-01's binary "Observable?" column? Both enforce observability structurally but
   the Skeptic creates a challenge posture that may surface edge cases the column approach leaves
   silent.

2. Does V-05's PHASE 3 read-only gate produce cleaner C-05 compliance on live runs than V-04's
   phase gate instruction? The checklist item is structurally strongest but the behavioral
   difference may be small in practice.

3. Does V-03's F-00 (status-quo as pre-printed falsification condition) raise experiment
   selection quality relative to V-01? Both score 95 on the rubric but the qualitative
   difference in confidence rationale depth may be worth preserving in a combination variation.

---

## R2 Candidate

Combine V-04's Skeptic role (strongest C-02 enforcement) with V-05's hard gate checklist
(strongest C-05 enforcement) and V-05's status-quo-as-competing-hypothesis framing (deepest
inertia interrogation). That combination covers all four excellence signals in one variation
and tests whether stacking the strongest mechanisms produces higher live-run quality or
introduces friction from complexity.
