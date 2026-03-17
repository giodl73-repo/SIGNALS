## Scorecard: campaign-evidence (Round 7)

### Scoring Legend

| Symbol | Meaning |
|--------|---------|
| ✓ | PASS |
| ~ | PARTIAL |
| ✗ | FAIL |

---

### V-01 — Lifecycle Emphasis (Gate as First-Class Artifact)

**Essential (60 pts)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All five prove skills executed | ✓ | All five stages present (websearch, intelligence, hypothesis, analysis, synthesize) with named sections |
| C-02 | Confidence level per finding | ✓ | Stage 4 assigns H/M/L per hypothesis with explicit basis; exit gate checks "at least two distinct confidence levels" |
| C-03 | Falsification status declared | ✓ | Hypothesis Register table has Status column (Supported/Refuted/Indeterminate) at Stage 5 |
| C-04 | Self-contained brief | ✓ | Output section specifies: title, topic context, gate record summary, executive summary, hypothesis register, evidence record, synthesis, gaps, decision readiness |

Essential: 4/4 → **60 pts**

**Recommended (30 pts)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-05 | Source attribution per claim | ✓ | ATTRIBUTION RULE mandates `[web search]`, `[intelligence]`, source-label at S1/S2/S4; exit gates enforce "every finding labeled" |
| C-06 | Synthesis distinguishes consensus/conflict | ✓ | Stage 5 has explicit **Consensus** and **Conflict** sections with literal prompt to name divergences |
| C-07 | Confidence calibrated, not uniform | ✓ | CALIBRATION RULE preamble + "Calibration checkpoint: If confidence ratings are uniform -- recalibrate explicitly" in Stage 4 body + exit gate checks two distinct levels |

Recommended: 3/3 → **30 pts**

**Aspirational (10 pts / 17 criteria)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-08 | Gaps and open questions surfaced | ✓ | Explicit "Gaps and Open Questions" section in Stage 5 |
| C-09 | Decision readiness signal | ✓ | "Decision Readiness (one sentence)" in Stage 5; exit gate checks it |
| C-10 | Hypotheses declared post-evidence | ✓ | Stage 3 entry gate requires S1+S2 exit all-Pass; SEQUENCING RULE enforces; rationale stated |
| C-11 | Calibration anti-pattern guard | ✓ | "Uniform confidence is a calibration failure" in CALIBRATION RULE + inline checkpoint in S4 |
| C-12 | Decision readiness one sentence | ✓ | "(one sentence)" label; S5 exit gate checks "Decision readiness expressed in one sentence" |
| C-13 | Named rules declared + invoked at point of use | ✓ | SEQUENCING, ATTRIBUTION, CALIBRATION, FALSIFICATION all bold-named in preamble and invoked by identifier at every applicable stage |
| C-14 | Hypothesis reordering rationale | ✓ | "A hypothesis anchored before evidence gathering is a bias, not a hypothesis" in SEQUENCING RULE and Stage 3 body |
| C-15 | Evidence-first as named rule | ✓ | SEQUENCING RULE is a first-class named rule in preamble with `[invoked at: Stage 1…5]` |
| C-16 | Zero-gap invocation coverage | ✓ | Coverage map vs. actual invocations: SEQUENCING at S1–S5, ATTRIBUTION at S1/S2/S4, CALIBRATION at S4/S5, FALSIFICATION at S3/S5 — all match |
| C-17 | Coverage map declared prospectively | ✓ | Coverage table appears in preamble before Stage 1 |
| C-18 | All rules at peer tier | ✓ | SEQUENCING, ATTRIBUTION, CALIBRATION, FALSIFICATION all bold headers at identical indentation; none demoted |
| C-19 | Coverage map immutability declared | ✓ | "Finalized before Stage 1 begins. Immutable — cannot be modified after any stage executes. This is a commitment, not a record." |
| C-20 | Rule scope inline in declaration | ✓ | Each rule carries `[invoked at: Stage X, Stage Y…]` within the rule declaration body |
| C-21 | Interrogative invocation at critical rules | ✓ | CALIBRATION and FALSIFICATION invocations all carry `[ Yes / No ]` interrogative form |
| C-22 | Universal binary invocation format | ✓ | SEQUENCING, ATTRIBUTION, CALIBRATION, FALSIFICATION all use `[ Yes / No ]` at every invocation site — no passive tags |
| C-23 | Stage-indexed invocation trail | ✓ | Every invocation carries `[Stage N of 5]` suffix |
| C-24 | Per-stage entry and exit conditions | ✓ | Every stage has a formal gate **table** (Pass/Fail rows) for both entry and exit — the gate record is a required output artifact |

Aspirational: 17/17 → **10 pts**

**V-01 Total: 100/100** | All essential: ✓

---

### V-02 — Output Format (Running Invocation Audit Table)

**Essential (60 pts)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All five prove skills executed | ✓ | All five stages named and sequenced |
| C-02 | Confidence per finding | ✓ | Stage 4 assigns H/M/L per hypothesis |
| C-03 | Falsification status | ✓ | Hypothesis Register with Status at Stage 5 |
| C-04 | Self-contained brief | ✓ | Output section mandates title, topic context, executive summary, hypothesis register, evidence, synthesis, gaps, decision readiness, plus 12-row audit table |

Essential: 4/4 → **60 pts**

**Recommended (30 pts)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-05 | Source attribution per claim | ✓ | ATTRIBUTION RULE + stage-labeled findings enforced |
| C-06 | Synthesis consensus/conflict | ✓ | Stage 5 explicitly separates Consensus from Conflict |
| C-07 | Calibrated confidence | ✓ | CALIBRATION RULE + anti-uniformity check in S4 + two invocations at S4 enforce variation |

Recommended: 3/3 → **30 pts**

**Aspirational (10 pts / 17 criteria)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-08–C-24 | (same framework as V-01) | ✓ all | SEQUENCING RULE, ATTRIBUTION RULE, CALIBRATION RULE, FALSIFICATION RULE all named, scoped inline, peer-tier, prospective coverage map with immutability, universal binary, stage-indexed, entry/exit per stage |

**Note**: V-02 generates more than 12 invocations (multiple invocations per stage at S3/S4/S5), but the coverage map states "expected: 12." This creates a minor internal inconsistency in the audit table row count. No rubric criterion fails on this — C-23 requires indexing, not an exact count — but an executor running V-02 will produce a delta ≠ 0 at final audit check. Flagged as a design defect, not a rubric failure.

Aspirational: 17/17 → **10 pts**

**V-02 Total: 100/100** | All essential: ✓

---

### V-03 — Phrasing Register (Minimal-Token Binary)

**Essential (60 pts)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All five stages | ✓ | All five present |
| C-02 | Confidence per finding | ✓ | H/M/L per hypothesis in Stage 4 |
| C-03 | Falsification status | ✓ | H# table with S/R/I column |
| C-04 | Self-contained brief | ✓ | Output section specifies single document with invocation markers visible |

Essential: 4/4 → **60 pts**

**Recommended (30 pts):** 3/3 → **30 pts** (same as V-01; all attribution, synthesis, calibration criteria met)

**Aspirational (10 pts / 17 criteria)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-08–C-21 | (core governance) | ✓ all | All rules named, scoped, prospective, immutable, peer-tier |
| C-22 | Universal binary | ✓ | All invocations across all rules use `[ Yes / No ]` — V-03 has the highest invocation density per stage |
| C-23 | Stage-indexed | ✓ | Every invocation carries `[Stage N of 5]` |
| C-24 | Per-stage entry/exit | ✓ | Every stage has explicit `Entry:` and `Exit:` prose conditions (terse but complete); all 10 gate declarations present |

Aspirational: 17/17 → **10 pts**

**V-03 Total: 100/100** | All essential: ✓

**Distinctive feature**: V-03 has the highest invocation frequency per stage (Stage 4 has 6 binary invocations; Stage 5 has 6). Maximum governance, minimum token overhead per invocation.

---

### V-04 — Combined: Lifecycle + Inertia Framing

**Essential (60 pts):** 4/4 → **60 pts**

**Recommended (30 pts):** 3/3 → **30 pts**

**Aspirational (10 pts / 17 criteria)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-08 | Gaps | ✓ | "Gaps and Open Questions" in Stage 5 |
| C-09 | Decision readiness | ✓ | One-sentence verdict |
| C-10 | Hypotheses post-evidence | ✓ | Stage 3 entry requires S1+S2 exit Pass |
| C-11 | Anti-uniformity guard | ✓ | CALIBRATION RULE + "Anti-uniformity check mandatory at every invocation" |
| C-12 | Decision readiness compressed | ✓ | One sentence format enforced |
| C-13 | Named rules at preamble + point of use | ✓ | Five named rules (SEQUENCING, ATTRIBUTION, CALIBRATION, FALSIFICATION, INERTIA) |
| C-14 | Reordering rationale | ✓ | "A hypothesis anchored before evidence is an anchor, not a hypothesis. Rationale: pre-committed hypotheses distort evidence weighting." |
| C-15 | Evidence-first as named rule | ✓ | SEQUENCING RULE formally named and scoped |
| C-16 | Zero-gap invocation | ✓ | Coverage map matched; INERTIA RULE invoked at S5 |
| C-17 | Coverage map prospective | ✓ | Declared in preamble before Stage 1 |
| C-18 | All rules peer-tier | ✓ | Five rules at identical bold-header tier — INERTIA RULE added as peer, not footnote |
| C-19 | Immutability declared | ✓ | "Finalized before Stage 1. Immutable — cannot be modified after any stage executes." |
| C-20 | Rule scope inline | ✓ | `[invoked at: Stage N…]` in every rule declaration |
| C-21 | Interrogative at critical rules | ✓ | CALIBRATION and FALSIFICATION use `[ Yes / No ]` |
| C-22 | Universal binary | ✓ | All five rules including INERTIA use binary form |
| C-23 | Stage-indexed | ✓ | All invocations carry `[Stage N of 5]` |
| C-24 | Per-stage entry/exit | ✓ | Every stage has `**Entry condition**: ... | Verify: [ Pass / Fail ]` and `**Exit condition**: ... Verify: [ Pass / Fail ]` |

Aspirational: 17/17 → **10 pts**

**V-04 Total: 100/100** | All essential: ✓

**Distinctive feature**: INERTIA RULE — a fifth governance rule not in the current rubric. Campaign initializes at "do not proceed"; evidence must win; "status quo holds" is a first-class valid output. This is the only variate that names the null hypothesis as an explicit competitor.

---

### V-05 — Combined: Output Format + Role Sequence (Evidence Matrix)

**Essential (60 pts)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All five stages | ✓ | All five stages present, each contributing rows to the Evidence Matrix |
| C-02 | Confidence per finding | ✓ | Evidence Matrix has a Confidence column populated at Stage 4; Hypothesis Table has Final Confidence column at Stage 5 |
| C-03 | Falsification status | ✓ | Hypothesis Table Status column populated at Stage 5; C-24 exit condition checks "All hypothesis Status and Final Confidence cells populated" |
| C-04 | Self-contained brief | ✓ | Output = assembled Evidence Matrix + Hypothesis Table + synthesis section; governance compliance readable by four-column inspection |

Essential: 4/4 → **60 pts**

**Recommended (30 pts):** 3/3 → **30 pts**

- C-05: ATTRIBUTION enforced structurally — blank Stage column = unattributed row that "fails the rule" (not just a warning) ✓
- C-06: Synthesis has Consensus (matching Row#s) and Conflict (conflicting Row#s named) ✓
- C-07: Calibration anti-uniformity check: "scan the Confidence column — if all values are identical, recalibrate before proceeding" ✓

**Aspirational (10 pts / 17 criteria)**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-08–C-21 | (core governance) | ✓ all | All four named rules, prospective coverage map, immutability, peer-tier, inline scope, interrogative invocations |
| C-22 | Universal binary | ✓ | All rule invocations use `[ Yes / No ]` |
| C-23 | Stage-indexed | ✓ | All invocations carry `[Stage N of 5]` |
| C-24 | Per-stage entry/exit | ✓ | Every stage has `**Entry condition**:` and `**Exit condition**:` explicitly; conditions reference matrix state (e.g., "Matrix contains S1:Web rows only") making them structurally verifiable |

Aspirational: 17/17 → **10 pts**

**V-05 Total: 100/100** | All essential: ✓

**Distinctive feature**: SEQUENCING proof is structural — the Evidence Matrix Stage column sort order (S1:Web → S2:Intel → S4:Analysis) is the proof. Any sequence violation appears as an out-of-order value detectable by sort. Stage 5 includes explicit sort verification: "Sort the Evidence Matrix by Stage column. Any deviation indicates a sequence violation." No prose-reading required.

---

### Rankings

| Rank | Variate | Score | Axis | Distinctive Contribution |
|------|---------|-------|------|--------------------------|
| 1 (tied) | V-01 | 100 | Gate as artifact | Gates are fillable tables; blank = visible compliance failure |
| 1 (tied) | V-02 | 100 | Audit table | 12-row expected count; completeness by arithmetic (minor count inconsistency noted) |
| 1 (tied) | V-03 | 100 | Minimal-token | One-line invocations; governance friction approaches zero |
| 1 (tied) | V-04 | 100 | Lifecycle + Inertia | INERTIA RULE; "do not proceed" as named initial posture |
| 1 (tied) | V-05 | 100 | Matrix + Sequence | Stage column sort = structural SEQUENCING proof |

---

### Excellence Signals

All five variates reach the ceiling (100/100, all essential pass) because C-22, C-23, and C-24 are now baseline requirements and all previous criteria are fully encoded. The distinguishing value lies in patterns that exceed the current rubric and are candidates for C-25+:

**From V-01**: **Gate-as-artifact** — exit conditions are tables the executor must fill in before advancing; the filled gate record is included in the output brief. Compliance is presence/absence of a filled cell, not a prose assertion. A blank gate is as visible as a missing section.

**From V-02**: **Invocation audit table with arithmetic verification** — all invocations are captured as rows in a running table with an expected row count (12). Completeness is verifiable by one count operation. *Design defect noted*: multiple invocations per stage-rule pair in the prompt body cause the actual row count to exceed 12, producing a false delta. The pattern is sound; the implementation needs count reconciliation.

**From V-04**: **Inertia framing / INERTIA RULE** — campaign initializes at "do not proceed" posture; evidence must affirmatively clear a stated threshold; "status quo holds" is a first-class, equally-specified output. Eliminates optimism bias by making the null outcome as well-structured as the action outcome.

**From V-05**: **Structural sequence proof via column sort** — the Evidence Matrix Stage column sort order (S1 → S2 → S4) is the SEQUENCING proof. Violation is detectable by sorting one column without reading prose. Hypothesis table Grounded In references must point to S1/S2 rows only — sequence violation appears as a disallowed row reference.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate-as-artifact: exit conditions are fillable tables included in output brief; blank cell is structural evidence of non-compliance", "inertia-rule: campaign posture initializes to do-not-proceed; evidence must clear explicit threshold; status-quo-holds is a first-class valid output not a fallback", "structural-sequence-proof: evidence matrix stage column sort order is the sequencing proof; violation detectable by sort without reading prose"]}
```
