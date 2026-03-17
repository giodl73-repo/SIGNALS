Written to `simulations/quest/rubrics/prove-synthesize-rubric-v5-2026-03-14.md`.

---

**What changed from v4 — summary:**

**C-16 clarified (not new — tightened pass condition):**
V-03 exposed that the v4 criterion text had no rubric basis for partial credit — labels-only earned ad hoc 1.25 pts. v5 closes this: a second NOT: condition makes it explicit that role labels without prohibition statements do not satisfy C-16. V-03's score drops from 113.75 to 112.5 retroactively.

**Three new aspirational criteria (C-20, C-21, C-22):**

| ID | Name | Extends | Mechanism |
|----|------|---------|-----------|
| C-20 | Phase-sequenced frontmatter completion | C-19 | Each boolean is filled at its individual structural moment — not batch-filled at start or end. Sequential determinability enforces phase order: `adversary_pre_determination` becomes truthfully fillable only *after* ADVERSARY and *before* JUDGE. |
| C-21 | SURVEYOR-traceable anti-pattern diagnosis | C-17 | The cited structural properties must appear in the SURVEYOR inventory. Turns "derived from the record" (C-17, evaluable) into "verifiable by cross-reference" (C-21, falsifiable). |
| C-22 | Dual-layer register-word enforcement | C-18 | Output format alone satisfies C-18. C-22 requires the additional explicit NOT: gate at the instruction level — defense-in-depth against prompt drift. |

**Scoring delta:**

| | v4 | v5 |
|-|----|----|
| Aspirational | 27.5 pts / 11 | 35 pts / 14 |
| Max composite | 117.5 | 125 |
| Golden threshold | >= 90 | >= 90 (unchanged) |
bility (cross-referenceable to the inventory). |
| C-22 | Dual-layer register-word enforcement | The register-word-first constraint is enforced at both output level (DETERMINATION: format) and instruction level (explicit NOT: gate). C-18 fires on output format alone; C-22 requires the instruction-level gate as a second enforcement layer. Defense-in-depth against prompt drift toward register-word-after-introductory-language. |

**Scoring:**

| Tier | v4 | v5 |
|------|----|----|
| Aspirational | 27.5 pts / 11 criteria | 35 pts / 14 criteria |
| Max composite | 117.5 | 125 |
| Golden threshold | >= 90 | >= 90 |

Golden threshold unchanged. Aspirational tier now spans 90-125; top score requires all 14 aspirational.

---

**Scoring update summary:**

| Tier | v4 | v5 |
|------|----|----|
| Essential | 60 pts / 5 criteria | 60 pts / 5 criteria |
| Recommended | 30 pts / 3 criteria | 30 pts / 3 criteria |
| Aspirational | 27.5 pts / 11 criteria | 35 pts / 14 criteria |
| Max composite | 117.5 | 125 |
| Golden threshold | >= 90 | >= 90 |

**Golden threshold interpretation (v5)**: Baseline (all essential + all recommended) = 90. Golden requires full recommended compliance. Aspirational criteria differentiate above golden. Top score of 125 requires all 14 aspirational.

**C-16 clarification**: R4 resolved the partial-credit ambiguity. Labels alone (SURVEYOR/ADVERSARY/JUDGE without prohibition statements) do not satisfy C-16. Full pass requires both identity labels and explicit prohibition statements. The criterion now states this as a NOT: condition.

**C-11/C-12 tension**: Confirmed across R2, R3, R4. Both criteria remain; the tension is a feature.

**C-17/C-21 relationship**: C-17 requires the failure mode be *derived from* the record's structural properties. C-21 requires those properties be *traceable to* the SURVEYOR phase inventory -- verifiable by cross-reference, not merely plausible. Both can be satisfied independently; the highest-quality artifacts satisfy both.

**C-18/C-22 relationship**: C-18 fires when the register word opens the commitment sentence at the output level. C-22 requires an explicit NOT: gate at the instruction level. C-18 is necessary but not sufficient for C-22.

**C-19/C-20 relationship**: C-19 requires the frontmatter block exist and prohibits retroactive completion. C-20 requires each field be filled at its individually correct structural moment -- phase-sequenced, not batch-filled at start or end.

**Round 4 calibration**: All 5 R4 variations were Golden (112.5-117.5 under v4). V-05 achieved maximum 117.5. New criteria predicted from V-05 excellence signals (3/3). C-16 partial-credit resolution: labels-only earns no credit under v5 (V-03 scores 112.5 not 113.75). C-18 calibration resolved: output format alone satisfies C-18; explicit NOT: gate required only for C-22.

---

## Essential Criteria (weight: 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Answer-first** | format | The synthesis opens with a direct answer to the hypothesis before any evidence or reasoning. The answer is a complete declarative sentence, not a hedge or a restatement of the question. |
| C-02 | **Confidence score present and calibrated** | correctness | A numeric confidence score (0-100) is stated. It is calibrated: high confidence (>=75) only when evidence strongly converges; low confidence (<=40) when evidence is mixed or thin. |
| C-03 | **Key evidence cited** | coverage | Exactly or up to 3 signals are named as key evidence. Each named signal is traceable to an artifact produced during the investigation (not invented). Each signal is explained in terms of *why* it influenced the answer. |
| C-04 | **Counter-evidence present** | correctness | At least one piece of evidence arguing *against* the answer is explicitly named. If none exists, the output states "no counter-evidence found" with a brief rationale. Omitting this section entirely is a fail. |
| C-05 | **Synthesis supersedes signals** | behavior | The synthesis takes a position -- it does not merely restate or list the investigation signals. The answer and confidence together constitute a judgment call, not a summary. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Principles extracted** | depth | At least one principle is stated -- something learned beyond this specific hypothesis that generalizes to future investigations. Principles are declarative ("X implies Y") not restatements of the finding. |
| C-07 | **Open questions identified** | coverage | At least one question the investigation did not resolve is named. Questions are specific and actionable, not generic ("more research needed"). |
| C-08 | **Confidence is explained** | depth | The confidence score is accompanied by a brief rationale (1-3 sentences) explaining what drove it up or down. Score alone without rationale is a partial pass (counts as fail for this criterion). |

---

## Aspirational Criteria (weight: 35 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top signals outweighed the others -- not just what they are. A comparative question is present for each rank: "why this signal over the one below it?" A ranked argument is present, not a ranked list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure. |
| C-11 | **Anti-pattern gates named explicitly** | behavior | At least one gate or checklist item names the failure mode by name rather than only naming the success condition. Example: "This is a ranked argument, not a ranked list" is stronger than "Evidence hierarchy is argued." A gate that names what *not* to do forecloses compliant-but-wrong outputs that pass presence checks. |
| C-12 | **Argumentative sections are prose** | depth | Evidence ranking, synthesis judgment, and confidence rationale are written as prose paragraphs, not tables or bullet lists. Tables are permitted only for enumerative sections (e.g., open questions list, principles list). Prose is a structural enforcement mechanism: it requires argument construction and cannot be satisfied by filling cells. |
| C-13 | **NOT:-first gate ordering** | behavior | Gates that enforce anti-patterns list the failure mode *before* the success condition. NOT: "[failure mode]" precedes the positive pass condition in each gate item. A gate that names the failure mode after the pass condition allows the writer to satisfy the presence check before encountering the prohibition. NOT:-first ordering forecloses the failure mode before the pass condition is reached. |
| C-14 | **Formal verdict register** | behavior | The synthesis uses a dedicated lexical register for its judgment -- a term (RULING, VERDICT, DETERMINATION, FINDING, or equivalent) that signals commitment rather than summary. The register word appears as a sentence-level declaration (not as a section header or container label). Register-level commitment enforces anti-hedging independent of gate structure: a RULING cannot be followed by hedging language in a way that "Based on the evidence..." can. NOT: the register word appears only as a section header; `## VERDICT` labels a container and does not foreclose hedging at the commitment point. |
| C-15 | **Pre-committed counter-evidence** | behavior | The adversarial challenge (counter-evidence obligation) is issued structurally *before* the verdict section, not as a post-hoc reflection section after the determination. Pre-commitment forces the synthesis to issue its judgment against the best opposing case already on the table. NOT: counter-evidence section follows the verdict and is selected after the position is formed. C-04 requires counter-evidence present; C-15 requires it structurally precede the verdict. |
| C-16 | **Role-labeled cognitive phases** | behavior | Each phase is assigned a procedural identity label (SURVEYOR, ADVERSARY, JUDGE, SCHOLAR, or equivalent) AND explicit prohibition statements foreclose what that identity cannot produce: "A JUDGE cannot hedge. Violation is a procedural breach." / "An ADVERSARY cannot advocate." Labels name who the writer is in that phase; prohibition statements foreclose what that identity cannot produce. One without the other is insufficient -- identity without foreclusion creates a role name without a constraint; prohibition without identity creates a rule without a subject. NOT: phase labels are descriptive titles (OVERVIEW, VERDICT, PRINCIPLES) that do not foreclose output type. NOT: role labels are present without accompanying prohibition statements -- labels alone do not satisfy this criterion. |
| C-17 | **Record-specific anti-pattern declaration** | behavior | The adversarial challenge names the failure mode most likely given *this record's specific structure* -- not a generic anti-pattern that could appear in any synthesis. The declaration is derived from the record at hand: "given this record's thin signal set, the most likely failure mode is confidence inflation" passes; "do not list signals instead of synthesizing" does not. C-11 requires a failure mode be named; C-17 requires it be diagnosed from the record under review. NOT: the adversarial challenge names a generic anti-pattern that does not reference the record's signal composition or structural properties. |
| C-18 | **Register word opens the commitment sentence** | behavior | The formal verdict register word (RULING, VERDICT, DETERMINATION, FINDING, or equivalent from C-14) is the first word of the judgment sentence: `DETERMINATION: YES` or `VERDICT: the hypothesis is supported`. A register word that appears mid-sentence or after introductory language allows hedging to precede it. C-14 requires the register word appear in a sentence-level declaration; C-18 requires it open that sentence. NOT: the register word appears in a section header, parenthetical, or after introductory language ("Our final determination is..."). |
| C-19 | **Frontmatter commitment declarations** | behavior | The artifact opens with machine-readable boolean declarations recording whether each structural constraint was honored at output time: `adversary_pre_determination: true`, `register_word_used: true`, `record_specific_antipattern: true`, or equivalent fields. Frontmatter booleans require the writer to commit before the prose begins and cannot be retroactively satisfied. NOT: structural compliance is implicit, undeclared, or detectable only by reading the full artifact. |
| C-20 | **Phase-sequenced frontmatter completion** | behavior | Each frontmatter boolean is filled at the structural moment its corresponding phase becomes determinable -- not all at the artifact's start before phases are written, and not all at the end after the prose is complete. `adversary_pre_determination: true` can only be truthfully filled after the ADVERSARY phase content is written and before the JUDGE phase begins; filling it earlier is a false declaration, filling it later is retroactive completion. Sequential determinability enforces phase order: a writer who fills phase-sequenced booleans correctly must complete each structural phase before its boolean becomes truthfully fillable. C-19 requires the frontmatter block exist and prohibits retroactive completion; C-20 requires each field be individually sequenced to its phase. NOT: all frontmatter fields are filled at the artifact's start before any phases are written. NOT: all fields are filled at the artifact's end after full prose completion. |
| C-21 | **SURVEYOR-traceable anti-pattern diagnosis** | correctness | The failure mode diagnosis in the adversarial challenge cites structural properties that are traceable to values stated in the SURVEYOR phase inventory. A reader can falsify the diagnosis by checking whether the cited property -- record count N, method diversity, signal concentration, or equivalent -- appears in the SURVEYOR output. The diagnosis is reader-falsifiable, not merely reader-evaluable. C-17 requires the failure mode be derived from the record's structure; C-21 requires the derivation be verifiable by cross-reference to the SURVEYOR inventory. NOT: the failure mode diagnosis cites a structural property that does not correspond to a value stated in the SURVEYOR phase. NOT: the diagnosis is stated without reference to a specific inventoried structural property. |
| C-22 | **Dual-layer register-word enforcement** | behavior | The register-word-first constraint (C-18) is enforced at both output level and instruction level. Output level: the commitment sentence format (`DETERMINATION: [YES/NO/MAYBE]`) structurally produces the register word as the first word. Instruction level: an explicit NOT: gate forecloses the failure mode by name ("NOT: the register word appears in a section header, parenthetical, or after introductory language in the commitment sentence"). C-18 fires on output-level enforcement alone; C-22 requires the additional instruction-level gate as a second enforcement layer. Defense-in-depth: the gate forecloses prompt drift toward register-word-after-introductory-language before the commitment sentence is reached. NOT: the commitment sentence format produces correct behavior but no explicit prohibition gate names the register-word-placement failure mode. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 90 |
| Passing | All essential pass, composite < 90 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 35 points total (14 criteria, 2.5 points each)
- Max composite: 125

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 3/14 pass -> 3/14 * 35 = 7.5
- **Composite = 75.5** -- fails golden (essential incomplete), failing overall

### Round 1 calibration (under v2 rubric)

All 5 Round 1 variations were Golden (90-100). Differentiation was entirely in the aspirational tier:

| Score | Variations | Pattern |
|-------|-----------|---------|
| 100 | V-05 | Standalone mandate in opening sentence + explicit "ranked argument, not ranked list" distinction |
| 95 | V-02, V-03, V-04 | Argued hierarchy (C-09 pass) but standalone not explicitly mandated (C-10 fail) |
| 90 | V-01 | Table-based hierarchy (C-09 fail) + no standalone mandate (C-10 fail) |

### Round 2 calibration (under v2 rubric)

All 5 Round 2 variations were Golden (97.5-100). Differentiation narrowed to C-11/C-12 structural tension:

| Score | Variation | Pattern |
|-------|-----------|---------|
| 100 | V-01, V-02, V-04, V-05 | R1 fixes baked in; C-11 and C-12 both satisfied |
| 97.5 | V-03 | Continuous prose design maximized C-12; eliminating gates made C-11 structurally impossible |

C-13, C-14, C-15 derived from R2 winning mechanisms.

### Round 3 calibration (under v3 rubric)

All 5 Round 3 variations were Golden (102.5-107.5). New criteria perfectly predicted (5/5):

| Score | Variation | New criteria passed |
|-------|-----------|---------------------|
| 107.5 | V-05 | C-13, C-14, C-15 |
| 105.0 | V-04 | C-13, C-14 |
| 102.5 | V-01 | C-13 only |
| 102.5 | V-02 | C-14 only |
| 102.5 | V-03 | C-15 only |

C-16, C-17, C-18, C-19 derived from R3 V-05 winning mechanisms: role-labeled phases, record-specific anti-pattern diagnosis, register-word-first commitment, frontmatter boolean declarations.

### Round 4 calibration (under v4 rubric)

All 5 Round 4 variations were Golden (112.5-117.5). V-05 achieved maximum 117.5. New criteria predicted from V-05 excellence signals (3/3):

| Score (v4) | Score (v5) | Variation | v4 new criteria passed | v5 delta |
|------------|------------|-----------|------------------------|----------|
| 117.5 | 125.0 | V-05 | C-16, C-17, C-18, C-19 | +7.5 (C-20, C-21, C-22 all pass) |
| 115.0 | 122.5 | V-04 | C-16, C-17, C-18 | +7.5 (C-21, C-22 pass; C-20 pass) |
| 113.75 | 112.5 | V-03 | C-18, C-19 (partial C-16) | -1.25 (C-16 partial removed; C-20/C-21/C-22 fail) |
| 112.5 | 115.0 | V-01 | C-16, C-18 | +2.5 (C-22 pass; C-20/C-21 fail) |
| 112.5 | 115.0 | V-02 | C-17, C-18 | +2.5 (C-21 pass; C-20/C-22 fail) |

C-16 partial-credit removal: V-03's ad hoc 1.25 partial (labels only, no prohibition) is no longer credited under v5's clarified pass condition. V-03 drops from 113.75 to 112.5. C-20, C-21, C-22 derived from R4 V-05 excellence signals: phase-sequenced frontmatter completion, SURVEYOR-traceable failure mode diagnosis, dual-layer register-word enforcement.
