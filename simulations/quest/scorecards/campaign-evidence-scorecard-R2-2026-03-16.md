## Scoring — campaign-evidence / Round 2

### Evaluation Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** All five stages executed | PASS | PASS | PARTIAL | PASS | PASS |
| **C-02** Per-finding confidence labels | PASS | PASS | PARTIAL | PASS | PASS |
| **C-03** Falsification status declared | PASS | PASS | PASS | PASS | PASS |
| **C-04** Self-contained evidence brief | PASS | PASS | PASS | PASS | PASS |
| **C-05** Source attribution ≥70% | PASS | PASS | PASS | PASS | PASS |
| **C-06** Consensus vs. conflict distinguished | PASS | PASS | PASS | PASS | PASS |
| **C-07** Calibrated confidence (not uniform) | PASS | PASS | PASS | PASS | PASS |
| **C-08** Gaps surfaced | PASS | PASS | PASS | PASS | PASS |
| **C-09** Decision readiness signal | PASS | PASS | PASS | PASS | PASS |
| **C-10** Hypotheses declared post-evidence | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-11** Anti-calibration guard explicit | PASS | PASS | PARTIAL | PASS | PASS |
| **C-12** Decision readiness one sentence | PASS | PASS | PASS | PASS | PASS |

---

### Per-Criterion Evidence Notes

**C-01**
- V-01: Explicit Stage 1–5 headers, each mapped to a named prove skill. PASS.
- V-02: All five stages present with schema. Standard sequence. PASS.
- V-03: Five numbered questions map implicitly to the five prove skills, but no labeled artifact block names the prove skill. "2. What does the public web say?" is not "prove-websearch." PARTIAL — stages are covered, not named.
- V-04: Five `### STAGE N — prove-[skill]` headers each with a gate check. PASS.
- V-05: Five stage headers, evidence-first ordering, all prove skills named. PASS.

**C-02**
- V-01: Format `[finding] — Stage [N] — [High / Medium / Low confidence]` per finding, built into the numbered list schema. PASS.
- V-02: Findings table has an explicit Confidence column per row. Forced by table structure. PASS.
- V-03: Q5 says "how confident are you" per finding — but conversational framing allows "fairly confident" prose rather than labeled High/Medium/Low. At least 3 labeled findings not guaranteed. PARTIAL.
- V-04: Findings table column `High / Medium / Low` per row. PASS.
- V-05: `[finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]` with minimum 5 findings. PASS.

**C-03**
- V-01: Stage 5 requires `Falsification outcome: [Supported / Refuted / Indeterminate] — [cite finding]`. PASS.
- V-02: Falsification status table with explicit Status and Evidence basis columns. PASS.
- V-03: Q5 explicitly asks for "falsification status: supported, refuted, or indeterminate? Name the finding." PASS.
- V-04: `Falsification status` + `Falsification basis` labeled fields in brief. PASS.
- V-05: FALSIFICATION RULE declared at preamble. `Falsification status` + `Basis` required fields. PASS.

**C-04**
- V-01: Stage 5 produces `Evidence Brief: {{topic}}` with all required sections. PASS.
- V-02: Titled, sectioned brief with self-contained narrative. PASS.
- V-03: Intro explicitly frames it as "a deliverable for someone who did not run the investigation." Strong rationale. PASS.
- V-04: Titled brief, date not present but sectioned structure is self-explanatory. PASS.
- V-05: Titled + dated brief with hypothesis, falsification, findings, gaps, and readiness. PASS.

**C-05**
- V-01: Attribution format `— Stage [N]` embedded per finding. Consensus and Divergence reference Stage 1/2 by number. PASS.
- V-02: Source stage column in findings table. Counter-evidence requires stage citation explicitly. PASS.
- V-03: Q5 says "say where it came from (which stage)" — stage attribution encouraged per finding. PASS.
- V-04: Source stage column in findings table. Consensus/Divergence labels name Stage 2 and Stage 3 directly. PASS.
- V-05: ATTRIBUTION RULE at preamble mandates `— Stage [N]` on every material claim. Strongest enforcement. PASS.

**C-06**
- All five variations have explicit Consensus and Divergence sections or equivalent questions distinguishing agreement from disagreement. PASS for all.

**C-07**
- V-01: "Note: Confidence levels must vary. If all findings carry the same level, you have not calibrated — revisit." PASS.
- V-02: `CALIBRATION CHECK`: "If every row carries the same rating, you have not calibrated — redistribute. A uniform column is a rubric failure." PASS.
- V-03: "Do not assign the same confidence level to every finding — if everything looks the same, your calibration is off." Instruction present but softer. PASS.
- V-04: `CALIBRATION GATE` requires "at least two distinct levels" before synthesis proceeds. PASS.
- V-05: `CALIBRATION RULE` at preamble + `CALIBRATION CHECK` reminder at Stage 5. PASS.

**C-08** All five variations require an explicit Open gaps section. PASS for all.

**C-09** All five variations require a Decision readiness field or question. PASS for all.

**C-10**
- V-01: Structural. Sequence = websearch (1) → intelligence (2) → hypothesis (3). Stage 3 is labeled "Now that you have seen what the web and internal sources say, declare the hypothesis." Design rationale explicit. PASS.
- V-02: Stage 1 = prove-hypothesis before any evidence. FAIL.
- V-03: Q1 asks for the hypothesis before Q2 (websearch). FAIL.
- V-04: Stage 1 = prove-hypothesis before websearch. FAIL.
- V-05: Structural. Stage 1 = websearch, Stage 2 = intelligence, Stage 3 = `prove-hypothesis [POST-EVIDENCE]` with design rationale: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." PASS.

**C-11**
- V-01: Stage 5 has "Note: Confidence levels must vary. If all findings carry the same level, you have not calibrated — revisit." Qualifies as a reviewer note with explicit anti-uniformity statement. PASS (weakest implementation).
- V-02: `CALIBRATION CHECK` named step in Stage 5 schema, "A uniform column is a rubric failure." PASS.
- V-03: "if everything looks the same, your calibration is off" embedded in Q5 instructions. Implicit anti-pattern warning, not a named rule or dedicated reviewer note. PARTIAL.
- V-04: `CALIBRATION GATE` at Stage 5, pre-synthesis mandatory check for two distinct levels. PASS.
- V-05: `CALIBRATION RULE` at preamble + `CALIBRATION CHECK (apply CALIBRATION RULE now)` at Stage 5. Named rule + invocation reference. Strongest implementation. PASS.

**C-12** All five variations specify one sentence for decision readiness ("one sentence", "Answer in one sentence", or "EXACTLY ONE SENTENCE" in V-05). PASS for all.

---

### Score Computation

| Variation | Essential (÷4 × 60) | Recommended (÷3 × 30) | Aspirational (÷5 × 10) | **Composite** | All Essential PASS |
|-----------|---------------------|----------------------|------------------------|---------------|-------------------|
| V-01 | 4.0/4 → 60 | 3/3 → 30 | 5.0/5 → 10 | **100** | YES |
| V-02 | 4.0/4 → 60 | 3/3 → 30 | 4.0/5 → 8 | **98** | YES |
| V-03 | 3.0/4 → 45 | 3/3 → 30 | 4.5/5 → 9 | **84** | NO (C-01, C-02 partial) |
| V-04 | 4.0/4 → 60 | 3/3 → 30 | 4.0/5 → 8 | **98** | YES |
| V-05 | 4.0/4 → 60 | 3/3 → 30 | 5.0/5 → 10 | **100** | YES |

*Partial = 0.5 credit. All-essential-pass requires PASS (not PARTIAL) on all four essential criteria.*

---

### Ranking

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | **V-05** — Evidence-First + Named Rules | 100 | Gold |
| 1 | **V-01** — Evidence-First | 100 | Gold |
| 3 | **V-02** — Per-Finding Table | 98 | Gold |
| 3 | **V-04** — Lifecycle Gates + Format | 98 | Gold |
| 5 | **V-03** — Conversational | 84 | Silver* |

*Silver band: all recommended pass, but two essential partials prevent Bronze/Gold threshold confirmation.*

**Predicted**: V-05 > V-04 > V-02 > V-01 > V-03
**Actual**: V-05 = V-01 > V-02 = V-04 > V-03

V-01 substantially outperformed its prediction (4th → 1st tie). The prediction assumed V-01's embedded anti-calibration note would fail C-11, but "Note: Confidence levels must vary. If all findings carry the same level, you have not calibrated — revisit" satisfies the rubric's "reviewer note" definition. The deviation is meaningful: the embedded note pattern was sufficient for C-11 — the named RULE label in V-05 adds enforcement robustness but the binary criterion already passes on V-01.

---

### Excellence Signals (V-05)

**1. Named rule contract before execution begins**
Declaring CALIBRATION RULE, FALSIFICATION RULE, ATTRIBUTION RULE at the preamble — before any stage starts — establishes a named contract the model can reference. Violations become named failures ("fails CALIBRATION RULE") rather than unnoticed omissions.

**2. Double-reinforcement: rule stated at preamble, invoked by name at the relevant stage**
`CALIBRATION CHECK (apply CALIBRATION RULE now)` at Stage 5 creates a two-point enforcement: the rule is registered once at the top, then explicitly triggered at the moment of application. The second invocation signals "this is where the rule actually fires."

**3. [POST-EVIDENCE] label with design rationale makes the sequence self-documenting**
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis" explains *why* Stage 3 comes third, not just *that* it does. A model reading this understands the behavioral intent of the ordering, not just the ordering. This increases the probability of behavioral compliance vs positional compliance.

**4. Minimum finding count as structural floor**
V-05 requires "minimum 5 findings" in the findings list. V-01 uses "continue as needed" with no floor. The minimum count prevents sparse outputs that technically satisfy C-02 with exactly 3 findings.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["evidence-first sequencing achieves C-10 structurally without behavioral compliance — the sequence IS the requirement, behavioral rationale optional", "inline anti-calibration note passes C-11 without named RULE label; named rules add enforcement robustness but binary criterion is met by a reviewer note", "double-reinforcement: state rule at preamble, invoke it by name at the stage where it fires — one mention is a contract, two is a trigger"]}
```
