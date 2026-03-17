Written to `simulations/quest/rubrics/prove-synthesize-rubric-v4-2026-03-14.md`.

---

**What changed from v3:**

Four new aspirational criteria from R3 V-05 patterns. One tightened existing criterion.

**C-14 tightened**: "section label or sentence-level declaration" → "sentence-level declaration only." R3 showed `## PHASE 2: VERDICT` labels a container and does not foreclose hedging; the old pass condition was wrong.

**New criteria:**

| ID | Name | Mechanism |
|----|------|-----------|
| C-16 | Role-labeled cognitive phases | Procedural identity (SURVEYOR/ADVERSARY/JUDGE) forecloses output type — a JUDGE cannot hedge, an ADVERSARY cannot advocate. Stronger than descriptive section titles. |
| C-17 | Record-specific anti-pattern declaration | Adversarial challenge names the failure mode most likely for *this record's structure*, not a generic warning. Turns C-11 from template exercise into record-specific diagnostic. |
| C-18 | Register word opens the commitment sentence | Register word is the *first* word of the judgment sentence (`DETERMINATION: YES`), not mid-sentence or post-introductory. C-14 requires the word present; C-18 requires it first. |
| C-19 | Frontmatter commitment declarations | Machine-readable booleans (`adversary_pre_determination: true`) declared before prose begins. Cannot be retroactively satisfied by reading the artifact. |

**Scoring:**

| Tier | v3 | v4 |
|------|----|----|
| Aspirational | 17.5 pts / 7 criteria | 27.5 pts / 11 criteria |
| Max composite | 107.5 | 117.5 |
| Golden threshold | >= 85 | >= 90 |

Golden threshold closes to baseline (all-essential + all-recommended = 90). Aspirational now differentiates above golden rather than enabling golden from below.
 that could appear in any synthesis. The writer diagnoses from the record at hand: "given this record's thin signal set, the most likely failure mode is confidence inflation" is record-specific; "do not list signals instead of synthesizing" is not. C-11 requires a failure mode be named; C-17 requires it be derived from the record under review. NOT: the adversarial challenge names a generic anti-pattern that does not reference the record's signal composition or structural properties.

**C-18 — Register word opens the commitment sentence** (`behavior`)
The formal verdict register word (RULING, VERDICT, DETERMINATION, FINDING, or equivalent from C-14) is the first word of the judgment sentence — `DETERMINATION: YES` or `VERDICT: the hypothesis is supported` — not a mid-sentence appearance or a section header. A register word that appears mid-sentence or as a label allows hedging to precede or follow it. Register-word-first forecloses hedging at the lexical point of commitment. C-14 requires the register word appear in a sentence-level declaration; C-18 requires it open that sentence. NOT: the register word appears in a section header, parenthetical, or after introductory language in the commitment sentence.

**C-19 — Frontmatter commitment declarations** (`behavior`)
The artifact opens with machine-readable boolean declarations recording whether each structural constraint was honored at output time: `adversary_pre_determination: true`, `register_word_used: true`, `record_specific_antipattern: true`, or equivalent fields. Frontmatter booleans require the writer to declare compliance before the prose begins; they cannot be retroactively satisfied by reading the full text. The declaration is a commitment artifact, not a formatting convention. NOT: structural compliance is implicit, undeclared, or detectable only by reading the full artifact.

---

**Scoring update summary:**

| Tier | v3 | v4 |
|------|----|----|
| Essential | 60 pts / 5 criteria | 60 pts / 5 criteria |
| Recommended | 30 pts / 3 criteria | 30 pts / 3 criteria |
| Aspirational | 17.5 pts / 7 criteria | 27.5 pts / 11 criteria |
| Max composite | 107.5 | 117.5 |
| Golden threshold | >= 85 | >= 90 |

**Golden threshold interpretation (v4)**: Baseline (all essential + all recommended) = 90. Golden now requires effective full recommended compliance; aspirational criteria push scores above golden rather than enabling golden from below. Top score of 117.5 requires all 11 aspirational.

**C-11/C-12 tension**: Confirmed R2 and R3. Both criteria remain; the tension is a feature distinguishing designs that solve both from designs that maximize one at the cost of the other.

**C-14 refinement**: R3 confirmed section headers do not satisfy C-14. Pass condition updated; "section label" removed as a valid form.

**Round 3 calibration**: All 5 R3 variations were Golden (102.5–107.5 under v3). New criteria were perfectly predicted (5/5). C-15 discriminating question resolved: structural pre-placement satisfies C-15 without gate-item formatting. C-14 mechanism clarified: fires at sentence-level declaration, not section header.

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

## Aspirational Criteria (weight: 27.5 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top signals outweighed the others -- not just what they are. A comparative question is present for each rank: "why this signal over the one below it?" A ranked argument is present, not a ranked list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure. |
| C-11 | **Anti-pattern gates named explicitly** | behavior | At least one gate or checklist item names the failure mode by name rather than only naming the success condition. Example: "This is a ranked argument, not a ranked list" is stronger than "Evidence hierarchy is argued." A gate that names what *not* to do forecloses compliant-but-wrong outputs that pass presence checks. |
| C-12 | **Argumentative sections are prose** | depth | Evidence ranking, synthesis judgment, and confidence rationale are written as prose paragraphs, not tables or bullet lists. Tables are permitted only for enumerative sections (e.g., open questions list, principles list). Prose is a structural enforcement mechanism: it requires argument construction and cannot be satisfied by filling cells. |
| C-13 | **NOT:-first gate ordering** | behavior | Gates that enforce anti-patterns list the failure mode *before* the success condition. NOT: "[failure mode]" precedes the positive pass condition in each gate item. A gate that names the failure mode after the pass condition allows the writer to satisfy the presence check before encountering the prohibition. NOT:-first ordering forecloses the failure mode before the pass condition is reached. |
| C-14 | **Formal verdict register** | behavior | The synthesis uses a dedicated lexical register for its judgment -- a term (RULING, VERDICT, DETERMINATION, FINDING, or equivalent) that signals commitment rather than summary. The register word appears as a sentence-level declaration (not as a section header or container label). Register-level commitment enforces anti-hedging independent of gate structure: a RULING cannot be followed by hedging language in a way that "Based on the evidence..." can. NOT: the register word appears only as a section header; `## VERDICT` labels a container and does not foreclose hedging at the commitment point. |
| C-15 | **Pre-committed counter-evidence** | behavior | The adversarial challenge (counter-evidence obligation) is issued structurally *before* the verdict section, not as a post-hoc reflection section after the determination. Pre-commitment forces the synthesis to issue its judgment against the best opposing case already on the table. NOT: counter-evidence section follows the verdict and is selected after the position is formed. C-04 requires counter-evidence present; C-15 requires it structurally precede the verdict. |
| C-16 | **Role-labeled cognitive phases** | behavior | Each phase is assigned a procedural identity label (SURVEYOR, ADVERSARY, JUDGE, SCHOLAR, or equivalent) that forecloses what the phase can produce. A section titled ADVERSARY cannot produce advocacy; a section titled JUDGE cannot produce hedging. Violating the role is a procedural breach, not a checklist omission. NOT: phase labels are descriptive titles (OVERVIEW, VERDICT, PRINCIPLES) that do not foreclose the output type of the section. |
| C-17 | **Record-specific anti-pattern declaration** | behavior | The adversarial challenge names the failure mode most likely given *this record's specific structure* -- not a generic anti-pattern that could appear in any synthesis. The declaration is derived from the record at hand: "given this record's thin signal set, the most likely failure mode is confidence inflation" passes; "do not list signals instead of synthesizing" does not. C-11 requires a failure mode be named; C-17 requires it be diagnosed from the record under review. NOT: the adversarial challenge names a generic anti-pattern that does not reference the record's signal composition or structural properties. |
| C-18 | **Register word opens the commitment sentence** | behavior | The formal verdict register word (RULING, VERDICT, DETERMINATION, FINDING, or equivalent from C-14) is the first word of the judgment sentence: `DETERMINATION: YES` or `VERDICT: the hypothesis is supported`. A register word that appears mid-sentence or after introductory language allows hedging to precede it. C-14 requires the register word appear in a sentence-level declaration; C-18 requires it open that sentence. NOT: the register word appears in a section header, parenthetical, or after introductory language ("Our final determination is..."). |
| C-19 | **Frontmatter commitment declarations** | behavior | The artifact opens with machine-readable boolean declarations recording whether each structural constraint was honored at output time: `adversary_pre_determination: true`, `register_word_used: true`, `record_specific_antipattern: true`, or equivalent fields. Frontmatter booleans require the writer to commit before the prose begins and cannot be retroactively satisfied. NOT: structural compliance is implicit, undeclared, or detectable only by reading the full artifact. |

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
- Aspirational: 27.5 points total (11 criteria, 2.5 points each)
- Max composite: 117.5

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 3/11 pass -> 3/11 * 27.5 = 7.5
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
