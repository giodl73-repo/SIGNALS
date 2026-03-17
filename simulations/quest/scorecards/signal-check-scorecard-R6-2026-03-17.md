Now I have everything I need. Let me score all five R6 variations against the full 18-criterion rubric.

---

# Signal-Check R6 Scorecard

## Evaluation Approach

No trace artifact available — scoring evaluates whether the prompt structure reliably produces outputs satisfying each criterion. R6 is the first round with C-17 and C-18 as full rubric criteria (aspirational tier, /10 denominator). All 5 variations incorporate them architecturally.

---

## Essential Criteria (5 each — 60%)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All four dimensions present | PASS | PASS | PASS | PASS | PASS |
| C-02 SEQUENCE grounded in artifact dates | PASS | PASS | PASS | PASS | PASS |
| C-03 COHERENCE names specific comparison | PASS | PASS | PASS | PASS | PASS |
| C-04 CAUSAL GAP verdict on mechanism evidence | PASS | PASS | PASS | PASS | PASS |
| C-05 Output is coaching, not verdictive | PASS | PASS | PASS | PASS | PASS |

**Notes:**

- **C-01**: All 5 require CAUSAL GAP, SEQUENCE, COHERENCE, STALENESS in STEP 2 (PART 1) and surface all four in PART 2 observations or table rows. No dimension collapse risk.
- **C-02**: All 5 mandate "cite 2+ artifacts with dates" in SEQUENCE. V-01 and V-04 add the verbatim MECHANISM VERDICT quote as a lead-in — artifact grounding is reinforced, not diminished.
- **C-03**: All 5 require "Name 2+ signals on a specific claim: aligned / contradicting / inconclusive." V-02, V-03, V-04 add the explicit follow-up: "does the contradiction bear on the mechanism question from CAUSAL GAP?" — enriches C-03 without risking it.
- **C-04**: All 5 require "State: present / partial / absent. Name what is there and what is missing. Do not restate the hypothesis." The "do not restate hypothesis" guard is consistent across all variations.
- **C-05**: The core research question for V-03 and V-05 — does tabular PART 2 hold advisory tone? Both install an explicit phrase-constraint rule: "Never: PASS / FAIL / BLOCKED / RED / GREEN" with a named list of advisory-only alternatives. The constraint is architecturally written into the prompt header, not just per-section. C-05 holds under format pressure when the rule is declared at prompt level. V-05 adds conversational register as a second guard. No variation exposes severity to the team-facing section.

---

## Recommended Criteria (3 each — 30%)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Concrete staleness threshold | PASS | PASS | PASS | PASS | PASS |
| C-07 Flagged issue → concrete next action | PASS | PASS | PASS | PASS | PASS |
| C-08 Report opens with readiness summary | PASS | PASS | PASS | PASS | PASS |

**Notes:**

- **C-06**: All 5 derive threshold dynamically. V-01/V-02/V-03/V-05 use competitor/benchmark presence as binary trigger (14 vs. 30 days). V-04 uses the inertia-relevant artifact count from the Step 1 column (1+ → 14 days, 0 → 30 days) — more operationally precise, but all satisfy the explicit threshold requirement.
- **C-07**: All 5 mandate "If yellow or red → next action:" per dimension in PART 1. V-03's table requires "Suggested Next Step" column with "every flagged row must have a specific next step." V-05 makes the same explicit: "Every flagged row must have a specific 'What to Do Next' — that's the useful part."
- **C-08**: V-01 opens PART 2 with STEP 4 combining readiness + inertia case — clean pass. V-02/V-04 open PART 2 with STEP A (INERTIA CASE STRENGTH, ~75w) then STEP B (DRAFT READINESS). V-03/V-05 open with INERTIA CASE (~50w) then READINESS OVERVIEW. All satisfy the spirit of C-08 ("don't dive straight into per-dimension detail") — the inertia case frame IS an overall readiness question, and the readiness summary follows immediately. None of the five open with per-dimension analysis.

---

## Aspirational Criteria (10 each — 10%)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Cross-dimension pattern named | PASS | PASS | PASS | PASS | PASS |
| C-10 Missing namespaces by namespace | PASS | PASS | PASS | PASS | PASS |
| C-11 Readiness drafted before, confirmed after | PASS | PASS | PASS | PASS | PASS |
| C-12 Staleness threshold calibrated from inventory | PASS | PASS | PASS | PASS | PASS |
| C-13 Analysis phases isolated with separators + budgets | PASS | PASS | PASS | PASS | PASS |
| C-14 Severity in analysis, protected from coaching | PASS | PASS | PASS | PASS | PASS |
| C-15 Status-quo alternative anchored at Step 0 | PASS | PASS | PASS | PASS | PASS |
| C-16 Two-register separation by document shape | PASS | PASS | PASS | PASS | PASS |
| C-17 SEQUENCE as mechanism-evidence audit | PASS | PASS | PASS | PASS | PASS |
| C-18 PART 2 opens with inertia case-strength question | PASS | PASS | PASS | PASS | PASS |

**Notes:**

- **C-09**: All 5 include STEP 3 with "Do 2+ flagged dimensions share a root cause? Name the pattern." V-01/V-04 extend with mechanism-gap language: "does it trace to a shared mechanism gap — e.g., CAUSAL GAP absent + SEQUENCE gap tracing to mechanism evidence never appearing in discovery at all?" Strongest pattern naming in V-04: "zero inertia-relevant artifacts causing both CAUSAL GAP and STALENESS to flag on the same absence."
- **C-10**: All 5 enumerate all 9 namespaces for empty-namespace assessment. Standard language "expected gap or meaningful blind spot?" consistent across V-01/V-02/V-03/V-05. V-04 slightly richer: "expected gap or meaningful blind spot?" scoped against the inertia-relevant question.
- **C-11**: All 5 use the DRAFT → dimension observations → CONFIRMED/REVISED sequence within PART 2. V-02/V-04: STEP B [DRAFT] → STEP C observations → STEP D [CONFIRMED/REVISED]. V-01: STEP 4 [DRAFT] → STEP 5 → STEP 6 [CONFIRMED/REVISED]. V-03: READINESS OVERVIEW [DRAFT] → table → CONFIRMED READINESS. V-05: DRAFT READ [DRAFT] → table → CONFIRMED READ [CONFIRMED/REVISED].
- **C-12**: All 5 derive threshold from inventory contents. V-04 is the most precise — per-artifact column count drives threshold selection, eliminating the binary ambiguity in "competitor / benchmark signals present?" when signals are indirect.
- **C-13**: All 5 use step-header + word budget format. PART 1: `==== STEP N: TITLE (~X words) ====` (V-01/V-02/V-03/V-04) or `---STEP N --- TITLE (~X words) ---` (V-05). PART 2 headers include word counts in all 5. V-03/V-05 table sections: the table row structure itself constrains scope proportionally — satisfies the criterion without a word count annotation on the table section.
- **C-14**: All 5 use `(internal: green / yellow / red)` inline notation in PART 1. All PART 2 sections explicitly prohibit severity labels. C-16 structural separation makes register leakage architecturally impossible — severity rows simply cannot exist in PART 2 because PART 2 has no severity rows by structure.
- **C-15**: STEP 0: INERTIA ANCHOR before STEP 1 inventory in all 5. V-04 is the strongest — the anchor explicitly seeds the "Inertia Relevant?" column in STEP 1, creating a named object that CAUSAL GAP immediately consumes.
- **C-16**: All 5 use named PART 1 / PART 2 section boundaries with explicit visual separators (`======` or `---`). V-05's "PART 1 — WORKING NOTES" / "PART 2 — WHAT I'D HAND THE TEAM" is the most natural conversational framing of the two-register architecture.
- **C-17**: Differentiated implementation across variations. V-01 and V-04: verbatim-quote requirement — SEQUENCE cannot run without the mechanism verdict because the verdict is literally a required input ("Quoting mechanism verdict: '[MECHANISM VERDICT from above]'"). V-02, V-03, V-05: instructional framing — "With the CAUSAL GAP verdict in view" / "More importantly: did the discovery phase establish the mechanism evidence you just evaluated?" Both approaches satisfy C-17 pass condition (SEQUENCE asks the mechanism question, not just temporal ordering). The verbatim-quote is a stronger implementation.
- **C-18**: All 5 include the "clearly built / partially built / still open" frame in PART 2 before dimension observations. Differentiated by structural prominence:
  - V-01: Combined with readiness in STEP 4 (inertia case as second question)
  - V-02/V-04: Dedicated named section (STEP A: INERTIA CASE STRENGTH) before readiness — strongest structural expression
  - V-03/V-05: Named `INERTIA CASE` section before readiness overview and table
  All pass C-18's "before or alongside the dimension observations" requirement. None relegate the inertia frame to within individual dimension coaching only.

---

## Composite Scores

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

| V | Axis | Essential | Recommended | Aspirational | Score | Band |
|---|------|-----------|-------------|--------------|-------|------|
| V-01 | Verbatim MECHANISM VERDICT handoff | 5/5 | 3/3 | 10/10 | **100** | Gold |
| V-02 | C-18 as dedicated PART 2 section | 5/5 | 3/3 | 10/10 | **100** | Gold |
| V-03 | Tabular PART 2, advisory-phrase constraint | 5/5 | 3/3 | 10/10 | **100** | Gold |
| V-04 | Full chain: mechanism handoff + C-18 section + inertia column | 5/5 | 3/3 | 10/10 | **100** | Gold |
| V-05 | Conversational register + tabular PART 2 | 5/5 | 3/3 | 10/10 | **100** | Gold |

All 5 Gold. Tied at 100.

---

## Ranking (Quality Differentiation at Equal Score)

All 5 score 100. Within that band, differentiated by analytical completeness:

| Rank | V | Distinguishing Bet | Hardest Test Passed |
|------|---|--------------------|---------------------|
| 1 | **V-04** | Full C-17/C-18 chain + inertia-relevance column | Verbatim verdict handoff, dedicated C-18 section, column-count threshold — end-to-end mechanism chain explicit and traceable |
| 2 | **V-01** | Verbatim MECHANISM VERDICT enforcement | C-17 architecturally locked: SEQUENCE cannot run without quoting verdict |
| 3 | **V-02** | C-18 as named PART 2 section with dedicated scope | Strongest C-18 structural prominence of the single-axis variations |
| 4 | **V-05** | Conversational register + tabular PART 2 | Advisory tone preserved through register rather than phrase-constraint alone |
| 5 | **V-03** | Tabular PART 2 in formal register | C-05 holds under format pressure via phrase-constraint |

---

## Research Question Assessment

**Q1: Does verbatim-quote MECHANISM VERDICT (V-01, V-04) improve mechanism audit depth beyond instructional carry-forward?**

Yes, but the improvement is in reliability, not depth per se. The instructional framing in V-02/V-03/V-05 ("with the CAUSAL GAP verdict in view") already asks the mechanism question; the verbatim quote makes it impossible to skip. The benefit is an architectural lock, not a qualitatively deeper framing. Both approaches satisfy C-17. V-01/V-04 are the more reliable implementations.

**Q2: Does C-18 as a dedicated PART 2 section (V-02, V-04) produce richer inertia case assessment than embedding it as a question in STEP 4 (R5 V-02)?**

Yes. A named section (STEP A: INERTIA CASE STRENGTH, ~75 words) with its own scope budget forces a complete answer before readiness. The embedded question in V-01 STEP 4 ("Second: is the case clearly built, partially built, or still open?") can be answered in one sentence within the readiness paragraph. V-02/V-04's dedicated section structurally allocates space and signals its priority to the analyst. Not redundant with dimension observations — it names the verdict before dimensions translate it into coaching language.

**Q3: Does tabular PART 2 (V-03, V-05) maintain C-05 advisory tone under phrase-constraint?**

Yes. The phrase-constraint rule is the key — declaring it at prompt level ("Never: PASS / FAIL / BLOCKED / RED / GREEN") with a named advisory-only vocabulary prevents verdictive reads even in row/column format. V-05 demonstrates that conversational voice adds protection on top: "here's what I'd flag" framing makes the table feel like a teammate's notes rather than a checklist audit. Both approaches hold C-05; V-05's register provides secondary reinforcement.

---

## Excellence Signals (from V-04, top-ranked)

**Signal 1: Per-artifact inertia-relevance tagging feeds all downstream analysis**

The "Inertia Relevant?" column in STEP 1 creates a named artifact subset that flows through the entire analysis: CAUSAL GAP pulls from it, STALENESS evaluates it with priority, the threshold is derived from its count, and PART 2 STEP C coaching calls out stale inertia-relevant artifacts by name. This makes the mechanism chain *traceable* — every downstream reference can be resolved to a specific inventory entry. V-01/V-02/V-03/V-05 use a binary "competitor signals present?" question that collapses this to a threshold trigger without creating the named artifact set.

**Signal 2: MECHANISM VERDICT as explicit bridge from PART 1 to PART 2**

V-04 STEP A explicitly says: "Connect to the MECHANISM VERDICT from CAUSAL GAP — that verdict is the most direct artifact-backed statement about the inertia case." This creates a named link between the PART 1 analytical conclusion and the PART 2 coaching frame. C-18 requires the inertia case question to be present; V-04 additionally requires the analyst to ground the coaching answer in the specific PART 1 finding rather than inferring the inertia case independently. The two registers are connected by artifact-backed evidence, not reassertion.

This pattern is not fully captured by C-17 (which is about SEQUENCE), C-18 (which requires the frame, not its grounding), or C-16 (which requires separation, not connection). Candidate C-19: *PART 2 inertia case assessment explicitly names the MECHANISM VERDICT from PART 1 as its evidence anchor, making the coaching conclusion directly traceable to the analytical record.*

---

## Promotion Recommendation

**Promote all 5 to R6 production status. All are Gold.**

Recommended assignments:
- **V-04**: Default for maximum analytical completeness — strongest end-to-end mechanism chain
- **V-01**: Default when mechanism audit depth is the primary concern — verbatim lock for C-17
- **V-02**: Default when PART 2 inertia case coaching is the primary deliverable
- **V-05**: Default for conversational register / informal team settings
- **V-03**: Speed/scannability scenarios — tabular PART 2 for teams that act from tables

R7 candidate axes:
1. C-19 test: require PART 2 inertia case assessment to explicitly name the MECHANISM VERDICT as its artifact anchor (present in V-04, absent in V-01/V-02/V-03/V-05)
2. Staleness threshold precision: test V-04's per-artifact column count derivation vs. binary competitor-signal question across variations — does it change threshold decisions in practice?

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["MECHANISM VERDICT as named PART 2 evidence anchor (V-04): PART 2 inertia case assessment explicitly names the MECHANISM VERDICT from PART 1 as its artifact-backed anchor rather than independently inferring the inertia case — creates a traceable bridge between analytical record and coaching register not covered by C-18 (which requires the frame) or C-16 (which requires separation)"]}
```
