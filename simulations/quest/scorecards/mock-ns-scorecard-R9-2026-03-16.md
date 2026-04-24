## mock-ns Round 9 -- Scorecard (rubric v9, max 124)

### Scoring Setup

All 5 variations share identical structure for S-1 through A-5 and the full CONSTRAINT block. Differences are confined to S-0: the preamble gate sentences and whether a standalone tier-carry terminal sentence is present.

**Shared baseline (all variations):**
All essential criteria C-01 through C-05 PASS. All recommended C-06 through C-08 PASS. Aspirational C-09 through C-17, C-19, C-21 through C-24, C-26 are identical across all five and evaluated once below.

| Shared criteria | Verdict | Evidence |
|----------------|---------|----------|
| C-01 header 6 fields | PASS | All: skill, topic, category, date, status, flag present (R8 precedent) |
| C-02 CATEGORY assignment | PASS | S-2 logic identical; HIGH-STRUCTURE/EVIDENCE-HEAVY/MIXED correct |
| C-03 FLAG computation | PASS | 5-row table + compliance override identical in all |
| C-04 fidelity warning | PASS | A-2 category-matched warning in all |
| C-05 skill-specific body | PASS | A-3 instruction produces skill-identifiable output |
| C-06 S-1 emit lines | PASS | TOPICS.md line (S-0) + generating line (S-1) both present |
| C-07 write confirmation | PASS | A-4: correct namespace-based path in all |
| C-08 next-step line final | PASS | A-5 identical in all |
| C-09 topic default exclusion | PASS | topic-status EXCLUDED in S-1 table |
| C-10 compliance override | PASS | Compliance override in S-3; no tags present = default pass |
| C-11 FLAG 5-case coverage | PASS | 5-row table with trace-*, scout-feasibility, listen-* named |
| C-12 tier resolves before selection | PASS | S-0 before S-1; step-labeled separation |
| C-13 error on unrecognized skill | PASS | "emit error naming the skill-id and direct user to registry" |
| C-14 discrete assembly steps | PASS | A-1 through A-5 labeled |
| C-15 CONSTRAINT 3+ op types | PASS | 5 op types in CONSTRAINT |
| C-16 wildcards in condition cell | PASS | trace-*, scout-feasibility, listen-* in FLAG table condition column |
| C-17 terminal gate names S-1 | PASS | "Do not begin S-1 until the TOPICS.md status line above is emitted." |
| C-19 both preamble + terminal gate | PASS | Opening declarative+imperative = preamble; "Do not begin S-1" = terminal |
| C-21 CONSTRAINT 4+ including body gen | PASS | 5 op types; body construction explicitly named |
| C-22 HS-critical tier=1 separate row | PASS | Tier=1 and tier>=2 rows distinct in all |
| C-23 preamble gate is opening sentence | PASS | Declarative is absolute first content of S-0 in all |
| C-24 CONSTRAINT 5+ including write | PASS | "No artifact path assembly or file output" is 5th op type |
| C-26 synonym vocabulary in CONSTRAINT | PASS | All 5 prohibition lines use paraphrased vocabulary vs canonical labels |
| C-29 step as direct nominative | PASS | No possessive-nominal form in any variation's declarative |
| C-30 no artifact as subject | PASS | No artifact in subject position in any variation |

Baseline for all: 80 (essential+recommended) + 2×24 shared aspirational passing = 80 + 48... 

Wait -- let me recount carefully. 22 aspirational criteria total (C-09 through C-30). Of those, 24 shared above includes C-29 and C-30. Variable criteria are: **C-18, C-20, C-25, C-27, C-28**. That is 5 variable criteria. Shared and consistently passing: 22 - 5 = 17 criteria = 34 pts. Plus essential 50 + recommended 30 = 80. Variable criteria contribute up to 10 pts. Max = 80 + 34 + 10 = 124. Check.

---

### Variable Criterion Analysis

#### C-25 -- Two-sentence gate: declarative + imperative

| Variate | Gate text | Verdict | Reason |
|---------|-----------|---------|--------|
| V-01 | "S-0 is the emit step. Write the TOPICS.md status line before any other work begins." | PASS | C-25 lists "S-0 is the emit step" as an explicit equivalent form; identity predicate asserts the step's pipeline role |
| V-02 | "This step must emit first. Write..." | **FAIL** | "Must emit" is modal-obligation mood -- prescribes a norm rather than declares what the step IS; C-25 requires "present-tense declaration asserting the step's ROLE"; deontic "must" converts the sentence from role-assertion to requirement-imposition |
| V-03 | "This step emits first and carries tier into S-2 and S-3. Write..." | PASS | Indicative declarative; compound predicate keeps it as role assertion |
| V-04 | "S-0 is the emit step and carries tier into S-2 and S-3. Write..." | PASS | Identity compound; "is the emit step" is role-asserting; compound extension doesn't change C-25 status |
| V-05 | "This step emits first and carries tier into S-2 and S-3. Write..." | PASS | Same as V-03 |

#### C-27 -- Count-strict exactly two sentences in gate

All five variates: **PASS**. Each gate is exactly two sentences (declarative + imperative). No third sentence inserted. The standalone tier-carry sentence in V-01, V-02, V-05 appears AFTER the resolution bullets, outside the gate boundary.

#### C-28 -- Step as grammatical subject asserting functional role (not output-position form)

| Variate | Declarative | Verdict | Reason |
|---------|-------------|---------|--------|
| V-01 | "S-0 is the emit step." | PASS | "S-0" is grammatical subject; identity predicate names the step's structural role in the pipeline |
| V-02 | "This step must emit first." | **FAIL** | "This step" is grammatical subject but "must emit" does not assert the step's defining function -- it prescribes behavior; C-28 requires the step as "agent of its own role," which requires indicative not deontic form |
| V-03 | "This step emits first and carries tier into S-2 and S-3." | PASS | Same compound-predicate pattern as R8 V-04 (confirmed 124/124) |
| V-04 | "S-0 is the emit step and carries tier into S-2 and S-3." | PASS | Step label as subject; identity compound satisfies role-assertion requirement |
| V-05 | "This step emits first and carries tier into S-2 and S-3." | PASS | Same as V-03 |

#### C-18 -- Tier-carry handoff sentence names downstream steps by label

| Variate | Handoff evidence | Verdict | Reason |
|---------|-----------------|---------|--------|
| V-01 | Standalone: "Carry the resolved tier into S-2 and S-3 before any further action." | PASS | Names tier and both consumers by label |
| V-02 | Same standalone sentence | PASS | Same |
| V-03 | No standalone; declarative: "...and carries tier into S-2 and S-3" | PASS | The declarative IS an explicit prose sentence naming tier and S-2/S-3 as consumers; C-18 requires "an explicit handoff sentence" without position constraint |
| V-04 | No standalone; declarative: "S-0 is the emit step and carries tier into S-2 and S-3." | PASS | Same reasoning; "carries tier into S-2 and S-3" in compound explicitly names tier and consumers |
| V-05 | Declarative compound + table + standalone sentence | PASS | Three independent registers; C-18 satisfied multiply |

#### C-20 -- Tier-carry in BOTH table column AND standalone terminal sentence

| Variate | Table cell | Standalone sentence | Verdict | Reason |
|---------|------------|--------------------|---------|----|
| V-01 | "Carry into S-2 (category) and S-3 (flag)" | "Carry the resolved tier into S-2 and S-3 before any further action." | PASS | Both registers present |
| V-02 | Same | Same | PASS | Both registers present |
| V-03 | "Carry into S-2 (category) and S-3 (flag)" | **Absent** | **FAIL** | C-20 requires "a standalone terminal sentence in S-0 prose naming both consumers" -- the declarative opening is not a standalone terminal sentence; position matters; the declarative is the gate opening, not a terminal statement |
| V-04 | Same | **Absent** | **FAIL** | Same C-20 failure as V-03; removing the standalone sentence is the deliberate discriminator; the declarative compound satisfies C-18 but not C-20 |
| V-05 | "Carry into S-2 (category) and S-3 (flag)" | "Carry the resolved tier into S-2 and S-3 before any further action." | PASS | Both registers present; standalone sentence retained specifically for C-20 dual-register requirement |

---

### Per-Variate Score Table

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | ess | PASS | PASS | PASS | PASS | PASS |
| C-02 | ess | PASS | PASS | PASS | PASS | PASS |
| C-03 | ess | PASS | PASS | PASS | PASS | PASS |
| C-04 | ess | PASS | PASS | PASS | PASS | PASS |
| C-05 | ess | PASS | PASS | PASS | PASS | PASS |
| C-06 | rec | PASS | PASS | PASS | PASS | PASS |
| C-07 | rec | PASS | PASS | PASS | PASS | PASS |
| C-08 | rec | PASS | PASS | PASS | PASS | PASS |
| C-09 | asp | PASS | PASS | PASS | PASS | PASS |
| C-10 | asp | PASS | PASS | PASS | PASS | PASS |
| C-11 | asp | PASS | PASS | PASS | PASS | PASS |
| C-12 | asp | PASS | PASS | PASS | PASS | PASS |
| C-13 | asp | PASS | PASS | PASS | PASS | PASS |
| C-14 | asp | PASS | PASS | PASS | PASS | PASS |
| C-15 | asp | PASS | PASS | PASS | PASS | PASS |
| C-16 | asp | PASS | PASS | PASS | PASS | PASS |
| C-17 | asp | PASS | PASS | PASS | PASS | PASS |
| **C-18** | asp | PASS | PASS | PASS | PASS | PASS |
| C-19 | asp | PASS | PASS | PASS | PASS | PASS |
| **C-20** | asp | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-21 | asp | PASS | PASS | PASS | PASS | PASS |
| C-22 | asp | PASS | PASS | PASS | PASS | PASS |
| C-23 | asp | PASS | PASS | PASS | PASS | PASS |
| C-24 | asp | PASS | PASS | PASS | PASS | PASS |
| **C-25** | asp | PASS | **FAIL** | PASS | PASS | PASS |
| C-26 | asp | PASS | PASS | PASS | PASS | PASS |
| **C-27** | asp | PASS | PASS | PASS | PASS | PASS |
| **C-28** | asp | PASS | **FAIL** | PASS | PASS | PASS |
| C-29 | asp | PASS | PASS | PASS | PASS | PASS |
| C-30 | asp | PASS | PASS | PASS | PASS | PASS |
| **Score** | | **124/124** | **120/124** | **122/124** | **122/124** | **124/124** |

---

### Rankings

| Rank | Variate | Score | Failures |
|------|---------|-------|----------|
| 1 | V-01 (Identity declarative) | 124/124 | none |
| 1 | V-05 (Synthesis: compound + dual-register) | 124/124 | none |
| 3 | V-03 (Tier-carry compound, no terminal) | 122/124 | C-20 |
| 3 | V-04 (Identity + tier-carry, no terminal) | 122/124 | C-20 |
| 5 | V-02 (Modal-obligation) | 120/124 | C-25, C-28 |

---

### Discriminator Verdicts

**Discriminator 1 -- C-25/C-28 mood-sensitivity (V-02 vs V-01/V-05):**
CONFIRMED. "This step must emit first" fails both C-25 and C-28. The modal "must" converts the sentence from a role-declaration (describing what S-0 IS in the pipeline) to an obligation-imposition (prescribing what S-0 must do). C-25 requires a declarative identity sentence asserting the step's role; a deontic sentence imposes a norm rather than declaring a fact about the step's nature. C-28 requires the step as "agent of its own role" -- modal-obligation form does not assert the step's function, it mandates compliance. New failure trap confirmed.

**Discriminator 2 -- C-20 terminal-position sensitivity (V-03/V-04 vs V-05):**
CONFIRMED POSITION-SENSITIVE. C-20 fails when the standalone terminal sentence is removed, even when the declarative compound explicitly names tier and both consumers. The declarative opening sentence is not a "standalone terminal sentence" by position -- it is the gate preamble. C-20 requires a dedicated prose sentence that terminates the S-0 resolution sequence; the compound declarative opening fills a different structural role and does not satisfy C-20's dual-register second register. C-18 and C-20 are confirmed independent: the declarative compound satisfies C-18 (explicit handoff sentence, position-agnostic) while failing C-20 (requires terminal position).

**Discriminator 3 -- C-18 identity-form acceptance (V-04 vs V-03):**
CONFIRMED equivalent. "S-0 is the emit step and carries tier into S-2 and S-3" satisfies C-18 at the same level as V-03's action-predicate compound. The identity-compound form's "carries tier into S-2 and S-3" conjunct explicitly names the carried artifact and both consumers by label; C-18 is satisfied. No additional failure from the identity predicate. V-04 and V-03 fail C-20 for the same reason (no standalone terminal sentence), confirming the failure is position-based, not form-based.

---

### Excellence Signals from Top-Scoring Variates (V-01, V-05)

**Signal 1 (V-01): Step-label identity declarative is the most discriminator-robust form.**
"S-0 is the emit step" uses a named step label as the direct nominative subject in an identity predicate. This form:
- Passes C-25 (explicitly listed as equivalent form)
- Passes C-28 (step-label as subject asserting its pipeline role -- the clearest possible role declaration)
- Passes C-29 (step label is a direct nominative, not a nominalization; "It is the emit step" refers to S-0)
- Passes C-30 (no artifact in subject position)

The step-label form is marginally stronger than the pronoun form "This step emits first" because the label name removes any ambiguity about referent. For compound predicates, "S-0 is the emit step and carries tier into S-2 and S-3" extends naturally without displacing the step from subject position.

**Signal 2 (V-05): Triple-register tier-carry achieves C-18+C-20 position-independence.**
Encoding the tier-carry obligation in three independent registers -- declarative compound opening, table downstream-use column, standalone terminal sentence -- achieves maximum coverage redundancy. The preamble gate remains count-strict at two sentences because the standalone tier-carry sentence appears AFTER the resolution bullets (outside the gate boundary). This is the structural key: the gate and the tier-carry terminal sentence occupy different positions in S-0 prose, so C-27 (count-strict gate) and C-20 (terminal sentence required) do not compete. The declarative compound in the gate additionally satisfies C-18, making the tier-carry obligation visible at three distinct locations for inspection.

**Signal 3 (V-02, failure trap): Modal-obligation mood is a new category of declarative failure.**
"Must emit" is a distinct failure mode from C-28's output-sequence form, C-29's possessive-nominal, and C-30's artifact-subject. None of those three criteria fire for "This step must emit first" -- the step is direct nominative, no artifact in subject position, no nominalization. The failure is at C-25 and C-28: the mood itself is wrong. A complete set of declarative failure modes now covers four patterns:
- Output-sequence subject (C-28): "The first observable output of this step is..." -- R7
- Nominalization subject (C-29): "This step's defining action is to emit first" -- R8
- Artifact subject (C-30): "The TOPICS.md status line is the first output..." -- R8
- Modal-obligation mood (C-25, C-28): "This step must emit first." -- **R9** (new)

---

### New Patterns for v10

| ID | Pattern | Source | Proposed criterion |
|----|---------|--------|-------------------|
| P-R9-1 | Modal-obligation declarative ("must emit") fails C-25 and C-28 -- mood-obligation imposes a norm rather than declaring the step's role; a declarative identity sentence must use indicative mood to assert what the step IS, not deontic mood to prescribe what it must do | V-02 | New criterion targeting indicative-mood requirement |
| P-R9-2 | C-20 is position-sensitive -- the opening declarative compound (even when it explicitly names tier and consumers, satisfying C-18) does not satisfy C-20's standalone terminal sentence requirement; the two registers are position-distinct: C-18 is position-agnostic (any explicit handoff sentence), C-20 requires a terminal prose sentence after the resolution bullets | V-03, V-04 | Clarification note to C-18 vs C-20, or new criterion requiring the terminal sentence to appear after resolution bullets |

---

```json
{"top_score": 124, "all_essential_pass": true, "new_patterns": ["Modal-obligation declarative ('This step must emit first') fails C-25 and C-28 -- indicative mood required to assert what the step IS; deontic mood prescribes behavior rather than declaring role identity", "C-20 is position-sensitive -- declarative compound opening satisfies C-18 (position-agnostic explicit handoff sentence) but not C-20 (requires standalone terminal sentence after resolution bullets, not the gate preamble)"]}
```
