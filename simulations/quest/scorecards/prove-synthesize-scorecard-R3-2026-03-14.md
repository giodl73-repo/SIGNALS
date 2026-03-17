## Round 3 Scoring — prove-synthesize

### Results

| Rank | Variation | Score | Result |
|------|-----------|-------|--------|
| 1 | **V-05** | **107.5** | Golden |
| 2 | V-04 | 105.0 | Golden |
| 3 (tie) | V-01 / V-02 / V-03 | 102.5 each | Golden |

All essential pass: **true**. All five variations Golden.

---

### Discrimination: Predictions vs Outcome — 5/5 correct

| Variation | Predicted new criteria | Actual | C-13 | C-14 | C-15 |
|-----------|----------------------|--------|------|------|------|
| V-01 | C-13 only | C-13 only | PASS | FAIL | FAIL |
| V-02 | C-14 only | C-14 only | FAIL | PASS | FAIL |
| V-03 | C-15 only | C-15 only | FAIL | FAIL | PASS |
| V-04 | C-13 + C-14 | C-13 + C-14 | PASS | PASS | FAIL |
| V-05 | C-13 + C-14 + C-15 | C-13 + C-14 + C-15 | PASS | PASS | PASS |

---

### Key R3 Findings

**C-15 discriminating question resolved**: V-03's structural pre-placement plus prose `NOT: this section is placed after the verdict...` satisfies C-15 without gate-item formatting. Structural pre-commitment is the mechanism; how it is announced (gate item vs prose instruction) is irrelevant.

**C-14 requires sentence-level register, not section header**: `## PHASE 2: VERDICT` does not satisfy C-14. "VERDICT" in a section title labels a container; it does not foreclose hedging at the commitment point. `**DETERMINATION: YES**` fires the mechanism; `**Answer: YES**` does not — V-01 and V-03 fail here.

**New patterns from V-05 (top scorer)**:
1. **Role labels as cognitive mode enforcement** — SURVEYOR/ADVERSARY/JUDGE assigns an identity that constrains what each section can produce, stronger than a section header that can be nominally satisfied
2. **Record-specific anti-pattern declaration** — ADVERSARY paragraph 3 requires naming the failure mode most likely given *this record's structure*, not a generic warning — C-11 as a diagnostic rather than a template
3. **C-14 fires at the declaration point** — register word must open the commitment sentence, not just the section
4. **Frontmatter booleans as machine-readable commitment declarations** — `adversary_pre_determination: true/false` requires the writer to declare at artifact output time whether the structural constraint was honored

```json
{"top_score": 107.5, "all_essential_pass": true, "new_patterns": ["role-labeled phases (SURVEYOR/ADVERSARY/JUDGE) enforce cognitive mode constraints stronger than section headers — a JUDGE that ignores the ADVERSARY challenge violates a procedural identity, not just a checklist item", "record-specific anti-pattern declaration in ADVERSARY: requiring the writer to name the failure mode most likely given THIS record's structure turns C-11 from template exercise into record-specific diagnostic", "C-14 requires register word at sentence-level commitment point, not section header — 'PHASE 2: VERDICT' label does not foreclose hedging; 'DETERMINATION: YES' does", "frontmatter boolean fields (adversary_pre_determination: true/false) encode structural constraints as machine-readable commitment declarations at artifact output time"]}
```
-04 | PASS | `CONFIDENCE: [N]/100` stated; DETERMINATION SEAL NOT: "CONFIDENCE notation lacks a rationale paragraph" |
| V-05 | PASS | `CONFIDENCE: [N]/100` stated; capped by ADVERSARY challenge explicitly named in confidence paragraph |

#### C-03 — Key evidence cited

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 3 names up to 3 signals; GATE 3 NOT: "any named signal is absent from the Phase 1 inventory" |
| V-02 | PASS | EVIDENCE BASIS up to 3 signals; EVIDENCE BASIS SEAL "All named signals exist in PRELIMINARY RECORD" |
| V-03 | PASS | Phase 4 names up to 3 signals; GATE 4 "All named signals exist in Phase 1 inventory" |
| V-04 | PASS | EVIDENCE BASIS up to 3 signals; EVIDENCE BASIS SEAL NOT: "any named signal is absent from PRELIMINARY RECORD" |
| V-05 | PASS | ADVOCATE names up to 3 signals; EVIDENCE GATE NOT: "any named signal is absent from the SURVEYOR record" |

#### C-04 — Counter-evidence present

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 4 required; GATE 4 NOT: "counter-evidence section is skipped or collapsed to 'none identified' without a paragraph" |
| V-02 | PASS | DISSENT section required; "This section cannot be empty or replaced with 'no opposition identified.'" |
| V-03 | PASS | Phase 2 (adversarial challenge) contains 3 required paragraphs of challenge before verdict |
| V-04 | PASS | DISSENT section required; DISSENT SEAL NOT: "dissent section is skipped or reduced to 'no opposition identified'" |
| V-05 | PASS | ADVERSARY section required before JUDGE; ADVERSARY GATE NOT: "adversarial challenge is absent or generic" |

#### C-05 — Synthesis supersedes signals

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "State your answer. This is a judgment, not a summary."; GATE 2 NOT: "verdict paragraph is a list of signal findings with a conclusion appended" |
| V-02 | PASS | "A DETERMINATION is a commitment, not an aggregation."; DETERMINATION SEAL NOT: "judgment paragraph is a list of record findings with a conclusion appended" |
| V-03 | PASS | GATE 3 "Answer is YES, NO, or MAYBE; MAYBE names the specific uncertainty" — verdict addresses the adversarial challenge, not just the signals |
| V-04 | PASS | "A DETERMINATION is a commitment — the register word forecloses hedging after it."; DETERMINATION SEAL NOT: "judgment paragraph is a list of record findings" |
| V-05 | PASS | JUDGE issues determination "against" the ADVERSARY's challenge; DETERMINATION SEAL NOT: "judgment paragraph fails to address the ADVERSARY's pre-determination challenge" |

#### C-06 — Principles extracted

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 5 "At least one declarative principle. 'X implies Y.' 'When Z, expect W.' Not a restatement of the verdict." |
| V-02 | PASS | Holdings "what this determination establishes beyond this case"; "Holdings that merely restate the DETERMINATION are not Holdings" |
| V-03 | PASS | Phase 5 "At least one declarative principle. 'X implies Y.' 'When Z, expect W.' Not a restatement of the verdict." |
| V-04 | PASS | Holdings declarative principle required; "Holdings that merely restate the DETERMINATION are not Holdings" |
| V-05 | PASS | SCHOLAR Holdings "at least one declarative principle"; "Holdings that merely restate the DETERMINATION are not Holdings" |

#### C-07 — Open questions identified

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 5 "at least one specific open question... Name the actual question... State the concrete next step: which prove sub-skill, or what external action" |
| V-02 | PASS | Open Record "At least one specific question still open. Name it. State why it remains undetermined... State the next investigative action" |
| V-03 | PASS | Phase 5 "at least one specific open question... Explain why it is still open. State the concrete next step" |
| V-04 | PASS | Open Record "at least one specific question still open... State the next investigative action" |
| V-05 | PASS | NAVIGATOR Open Record "at least one specific question still open... State the next investigative action: which prove sub-skill or concrete step" |

#### C-08 — Confidence is explained

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "A number without this paragraph fails."; GATE 2 NOT: "confidence is stated as a number only, without a rationale paragraph" |
| V-02 | PASS | "A CONFIDENCE notation without a rationale paragraph fails this section" |
| V-03 | PASS | "Confidence paragraph is present and explains the number" — explicit fail condition in GATE 3 |
| V-04 | PASS | DETERMINATION SEAL NOT: "CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot be interrogated" |
| V-05 | PASS | DETERMINATION SEAL NOT: "CONFIDENCE notation lacks a rationale paragraph"; confidence paragraph explicitly required to explain what drove number and what capped it |

#### C-09 — Evidence hierarchy is argued

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 3 "ranked argument, not a ranked list"; prose paragraphs per rank arguing comparative weight; GATE 3 NOT: "rank 1 justified only as 'it had the strongest support' without comparing to rank 2" |
| V-02 | PASS | EVIDENCE BASIS prose paragraphs arguing relative determinative weight; EVIDENCE BASIS SEAL "Comparative question answered for each rank: why this tier over the one below?" |
| V-03 | PASS | Phase 4 "ranked argument, not a ranked list"; GATE 4 "Each paragraph argues relative weight, not presence of support" |
| V-04 | PASS | EVIDENCE BASIS prose paragraphs; EVIDENCE BASIS SEAL NOT: "rank 1 justified as 'strongest support' without comparison to rank 2" |
| V-05 | PASS | ADVOCATE "ranked argument, not a ranked list"; EVIDENCE GATE NOT: "rank 1 justified as 'strongest support' without comparison to rank 2 — presence of support is not relative weight" |

#### C-10 — Synthesis is self-contained

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening paragraph." |
| V-02 | PASS | "This document stands alone: a reader with no prior knowledge of the investigation signals must understand the determination, the evidence basis, the dissent, and the open record from this document alone. State this requirement in your opening paragraph." |
| V-03 | PASS | "Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening paragraph." |
| V-04 | PASS | "This document stands alone: a reader with no prior knowledge of the investigation signals must understand the determination, the evidence basis, the dissent, and what to do next from this document alone. State this requirement in your opening paragraph." |
| V-05 | PASS | "This document stands alone: a reader with no access to the investigation signals must understand the determination, the evidence basis, the pre-determination challenge, and what to do next from this document alone. State this mandate in your opening paragraph." — adds "pre-determination challenge" as a standalone-required element |

#### C-11 — Anti-pattern gates named explicitly

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Every gate item is NOT:-first: GATE 2 "NOT: the answer is a hedge"; GATE 3 "NOT: evidence hierarchy is a table with a 'why' column"; GATE 4 "NOT: counter-evidence section is skipped" — failure modes named in every gate |
| V-02 | PASS | DETERMINATION SEAL: "Judgment paragraph issues a determination... not a list of record findings with a conclusion appended"; EVIDENCE BASIS SEAL: "Each entry argues relative weight, not presence of support" — failure modes named inline in seal items |
| V-03 | PASS | GATE 2 item "No answer word, verdict, or confidence score present in this phase" names the failure mode; GATE 3 "Verdict does not encounter the adversarial challenge for the first time" names what must not happen; Phase 2 prose "NOT: this section is placed after the verdict" names the C-15 failure mode explicitly |
| V-04 | PASS | All gates NOT:-first: RECORD GATE "NOT: evaluation language appears in this phase"; DETERMINATION SEAL "NOT: judgment paragraph is a list of record findings"; DISSENT SEAL "NOT: dissent section is skipped or reduced to 'no opposition identified'" |
| V-05 | PASS | All gates NOT:-first: RECORD GATE, ADVERSARY GATE, DETERMINATION SEAL, EVIDENCE GATE — each names failure mode before positive condition; ADVERSARY paragraph 3 requires naming a record-specific anti-pattern declaration |

**Note**: V-03 R3 differs from V-03 R2. R2 V-03 had no gates at all (continuous prose only), making C-11 impossible. R3 V-03 retains gate checklists, and its GATE 2 items name failure modes in negative form. C-11 PASS for V-03 R3.

#### C-12 — Argumentative sections are prose

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "Write argumentative sections — verdict, evidence hierarchy, confidence rationale — in prose paragraphs, not tables or bullet lists."; GATE 3 NOT: "evidence hierarchy is a table with a 'why' column" |
| V-02 | PASS | "Write argumentative sections — the determination, the evidence basis, the confidence rationale — in prose paragraphs. No tables in these sections." |
| V-03 | PASS | "Write argumentative sections in prose paragraphs."; GATE 4 "Each entry is a prose paragraph — not a table row or bullet" |
| V-04 | PASS | "Write argumentative sections — the determination, the evidence basis, the confidence rationale — in prose paragraphs. No tables in these sections."; EVIDENCE BASIS SEAL NOT: "evidence entries are table rows or bullets — a table is an annotated list, not an argument; cells can be filled without constructing a comparison" |
| V-05 | PASS | "Write argumentative sections in prose paragraphs, not tables or bullet lists."; EVIDENCE GATE NOT: "evidence hierarchy is a table with a 'why' column — a table is an annotated list, not an argument; filling cells requires no argument construction" |

#### C-13 — NOT:-first gate ordering (NEW)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Every gate item: `NOT: [failure mode] — [reason]. Positive condition: [pass condition]`. All four gates follow this format consistently. The prohibition is encountered before the positive check in every item. |
| V-02 | FAIL | Gates use standard checkbox format `- [ ] [success condition]`. DETERMINATION SEAL and EVIDENCE BASIS SEAL state success conditions first; failure modes appear inline as clarifications after, not before. |
| V-03 | FAIL | Gates use standard checkbox format `- [ ] [success condition]`. Phase 2 prose contains `NOT:` ordering but it's not a gate/checklist item. C-13 requires NOT:-first in the gate items themselves. |
| V-04 | **PASS** | RECORD GATE, DETERMINATION SEAL, EVIDENCE BASIS SEAL, DISSENT SEAL all use NOT:-first format. Every gate item: `NOT: [failure mode]. Positive condition: [pass condition]`. |
| V-05 | **PASS** | RECORD GATE, ADVERSARY GATE, DETERMINATION SEAL, EVIDENCE GATE all use NOT:-first format. Every gate item: `NOT: [failure mode]. Positive condition: [pass condition]`. |

#### C-14 — Formal verdict register (NEW)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | FAIL | Section header: `## PHASE 2: VERDICT`. Commitment sentence: `**Answer: [YES / NO / MAYBE]**`. "Answer:" is not a formal register term. Section header contains "VERDICT" but commitment sentence does not open with the register word — anti-hedging mechanism doesn't fire at the declaration point. |
| V-02 | **PASS** | `**DETERMINATION: [YES / NO / MAYBE]**` as sentence-level declaration in DETERMINATION section. DETERMINATION SEAL requires this explicitly. Register word at the commitment point; "DETERMINATION: MAYBE requires naming the specific uncertainty; it is a committed uncertainty, not a hedge." |
| V-03 | FAIL | Section header: `## PHASE 3: VERDICT`. Commitment sentence: `**Answer: [YES / NO / MAYBE]**`. Same pattern as V-01 — "Answer:" at declaration point, "VERDICT" only in section title. Anti-hedging mechanism doesn't fire at the sentence level. |
| V-04 | **PASS** | `**DETERMINATION: [YES / NO / MAYBE]**` as sentence-level declaration. DETERMINATION SEAL NOT: "judgment paragraph fails to open with DETERMINATION: [YES/NO/MAYBE] — the register word must commit before reasoning follows." |
| V-05 | **PASS** | JUDGE section: `**DETERMINATION: [YES / NO / MAYBE]**` as sentence-level declaration. DETERMINATION SEAL NOT: "DETERMINATION: is absent from the opening sentence of the judgment paragraph." The register word opens the commitment and explicitly forecloses post-verdict hedging. |

**C-14 finding**: "VERDICT" in a section header (`## PHASE 2: VERDICT`) does not satisfy C-14. The criterion requires the commitment word at the declaration point — the sentence where the answer is issued. A section header labels a container; the register word must appear in the commitment sentence to foreclose hedging at the moment of commitment.

#### C-15 — Pre-committed counter-evidence (NEW)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | FAIL | Counter-evidence in Phase 4, which follows Phase 2 (verdict). Adversarial challenge is post-verdict. |
| V-02 | FAIL | DISSENT section follows DETERMINATION. Counter-evidence (dissent) is post-verdict in document order. |
| V-03 | **PASS** | Phase 2 (ADVERSARIAL CHALLENGE) is placed before Phase 3 (VERDICT) in document order. Explicit NOT: in prose instruction: "NOT: this section is placed after the verdict and filled in post-determination. Counter-evidence selected after the position is formed is not a pre-commitment; it is post-hoc justification." Pre-commitment enforced by both structural ordering and explicit prohibition. |
| V-04 | FAIL | DISSENT section follows DETERMINATION. Counter-evidence is post-verdict in document order. |
| V-05 | **PASS** | ADVERSARY section (pre-determination challenge) is placed before JUDGE (determination) in document order. ADVERSARY prose instruction: "NOT: this section is placed after the DETERMINATION and filled in post-verdict — counter-evidence selected after the position is formed is not a pre-commitment; it is selection bias." Structural ordering plus explicit NOT: clause plus role architecture enforce pre-commitment at three levels. |

**C-15 discriminating question resolved**: V-03's structural pre-commitment (document order + prose NOT: clause) satisfies C-15. The criterion requires structural pre-placement, not gate-item formatting. A prose instruction that names the failure mode (`NOT: this section is placed after the verdict`) and enforces document order is sufficient. V-05 adds role architecture on top, but V-03's mechanism is genuine.

---

### Score Summary

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-06 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-09 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| C-10 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| C-11 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| C-12 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| C-13 | 2.5 | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| C-14 | 2.5 | FAIL | **PASS** | FAIL | **PASS** | **PASS** |
| C-15 | 2.5 | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| **Essential pts** | 60 | 60 | 60 | 60 | 60 | 60 |
| **Recommended pts** | 30 | 30 | 30 | 30 | 30 | 30 |
| **Aspirational pts** | 17.5 | 12.5 | 12.5 | 12.5 | 15.0 | 17.5 |
| **Composite** | 107.5 | **102.5** | **102.5** | **102.5** | **105.0** | **107.5** |
| **Result** | | Golden | Golden | Golden | Golden | Golden |

---

### Ranking

| Rank | Variation | Score | New criteria earned | Differentiator |
|------|-----------|-------|---------------------|----------------|
| 1 | V-05 | 107.5 | C-13 + C-14 + C-15 | Role architecture (SURVEYOR/ADVERSARY/JUDGE/ADVOCATE) enforces pre-commitment at three levels: document order, prose NOT: clause, and role identity constraint |
| 2 | V-04 | 105.0 | C-13 + C-14 | NOT:-first gate ordering plus DETERMINATION register; DISSENT seal enforces sourced opposition; leaves C-15 as live discriminator |
| 3 (tie) | V-01 | 102.5 | C-13 | NOT:-first gate structure throughout; "Answer:" at commitment point fails C-14 |
| 3 (tie) | V-02 | 102.5 | C-14 | DETERMINATION register + DISSENT vocabulary; standard checkbox gates fail C-13 |
| 3 (tie) | V-03 | 102.5 | C-15 | Structural pre-commitment confirmed sufficient for C-15; "Answer:" fails C-14; no NOT:-first in gate items fails C-13 |

**Separation**: V-05 is the sole maximum-score variation. V-04 is a clear second. V-01/V-02/V-03 tie at 102.5, each earning exactly one of the three new criteria.

---

### R3 Key Findings

**Finding 1 — C-15 mechanism confirmed**: Structural pre-placement of the adversarial challenge plus explicit prose NOT: clause ("NOT: this section is placed after the verdict and filled in post-determination") satisfies C-15. Gate-item formatting is not required. V-03 earns C-15 through document order alone (no NOT:-first gates, no formal register word). The criterion is about mechanism, not vocabulary.

**Finding 2 — C-14 requires sentence-level register, not section-header label**: "PHASE 2: VERDICT" as a section title does not satisfy C-14. "VERDICT" in the header labels a container; it does not foreclose hedging at the moment of commitment. C-14 fires only when the register word opens the commitment sentence — "DETERMINATION: YES" — because that is the point where hedging is foreclosed. V-01 and V-03 fail C-14 despite having "VERDICT" in section headers.

**Finding 3 — V-04 is the cleaner combo design**: V-04 combines NOT:-first gates (C-13) and DETERMINATION register (C-14) without the structural complexity of role labels. The DISSENT SEAL is V-04's strongest individual mechanism — it uses NOT:-first gate ordering on the counter-evidence section, requiring sourced opposition with a stated rebuttal or explicit "DISSENT UNRESOLVED." V-04 is the highest-scoring variation that does not require ADVERSARY pre-placement.

**Finding 4 — V-05 role labels as cognitive mode enforcement**: The SURVEYOR/ADVERSARY/JUDGE/ADVOCATE/SCHOLAR architecture enforces not just structure but cognitive mode. Each role identity constrains what the role can produce — a JUDGE that ignores the ADVERSARY's challenge is procedurally incomplete, which is a stronger enforcement than a gate check that can be ticked off. V-05's ADVERSARY paragraph 3 (record-specific anti-pattern declaration) is the most novel mechanism: it requires naming the failure mode most likely given this investigation's particular signal structure, not a generic warning.

---

### Excellence Signals from Round 3

**1. Role-labeled phases as cognitive mode enforcement (V-05)**
SURVEYOR/ADVERSARY/JUDGE architecture enforces more than document order — it assigns an identity that constrains what each section can produce. The JUDGE that ignores the ADVERSARY challenge is not just missing a checklist item; it has violated a procedural role constraint. This is structurally stronger than a gate check because the constraint is embedded in the role identity, not the checklist.

**2. Record-specific anti-pattern declaration in ADVERSARY (V-05)**
ADVERSARY paragraph 3 requires: "name one failure mode this determination must avoid, given the structure of this particular record. Form: 'This DETERMINATION must not [do X], because [what this record's structure makes likely].' Not a generic rule — specific to this investigation's signal set." This is C-11 at its maximum: not just naming a generic failure mode, but requiring the writer to identify the failure mode most likely given the current record's vulnerabilities. It turns anti-pattern gate naming from a template exercise into a record-specific diagnostic.

**3. NOT:-first gate ordering plus DETERMINATION register denies two independent hedging paths (V-04)**
V-04's design argument is precise: NOT:-first gates foreclose structural failure modes before the writer reaches the pass condition; DETERMINATION: register forecloses post-verdict hedging at the lexical level. Each mechanism closes a path the other leaves open. A variation satisfying only one axis can still hedge through the unclosed path. V-04 closes both without requiring role architecture.

**4. Frontmatter as machine-readable commitment declaration (V-05)**
`adversary_pre_determination (true/false)` in the artifact frontmatter requires the writer to declare at output time whether C-15 was honored. A writer who placed the adversarial challenge after the verdict cannot mark this true without lying. Frontmatter fields that encode structural constraints create a machine-checkable record of whether the mechanism fired.

---

### R3 Summary vs R1/R2

| Round | Rubric | Top score | Differentiator |
|-------|--------|-----------|----------------|
| R1 | v1 | 100 (V-05 only) | C-10 standalone mandate + "ranked argument, not ranked list" |
| R2 | v2 | 100 (4-way tie) | R1 fixes baked in; C-11/C-12 tension discriminated V-03 |
| R3 | v3 | 107.5 (V-05 only) | C-13/C-14/C-15 discriminate cleanly; V-05 earns all three; four-way tie at 102.5 below |

The rubric has discriminating power at 107.5. No saturation. The five variations span four distinct score tiers (107.5 / 105.0 / 102.5×3). R3 mechanism predictions were correct 5/5.

---

### What R4 Should Test

All five variations pass all essential criteria. The rubric is working. R4 should test mechanism durability under adversarial output conditions:

- **V-05 under genuinely MAYBE hypothesis**: Does DETERMINATION: MAYBE with a named specific uncertainty hold, or does the ADVERSARY pre-challenge create pressure toward false YES/NO commitment? Test whether the register word plus pre-commitment produces better MAYBE handling than standard format.
- **V-04 vs V-05 on thin signal set (N=1)**: Does the ADVERSARY generate meaningful challenge with a single signal, or does it produce generic warnings? V-04's DISSENT SEAL enforcement vs V-05's ADVERSARY role architecture — which produces better C-04 output quality when the record is minimally populated?
- **C-13 + C-14 combo (V-04) vs full combo (V-05) output quality**: Do NOT:-first gates plus formal register (V-04) produce equivalent output quality to role architecture (V-05)? The score difference is 2.5 pts (one C-15 criterion); the structural complexity difference is significant.

```json
{"top_score": 107.5, "all_essential_pass": true, "new_patterns": ["role-labeled phases (SURVEYOR/ADVERSARY/JUDGE) enforce cognitive mode constraints stronger than section headers — a JUDGE that ignores the ADVERSARY challenge violates a procedural identity, not just a checklist item", "record-specific anti-pattern declaration in ADVERSARY: requiring the writer to name the failure mode most likely given THIS record's structure turns C-11 from template exercise into record-specific diagnostic", "C-14 requires register word at sentence-level commitment point, not section header — 'PHASE 2: VERDICT' label does not foreclose hedging; 'DETERMINATION: YES' does", "frontmatter boolean fields (adversary_pre_determination: true/false) encode structural constraints as machine-readable commitment declarations at artifact output time"]}
```
