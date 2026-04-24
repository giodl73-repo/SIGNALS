Now I have everything I need. All R8 variations scored at ceiling (165/165 = C-01..C-23). R9 adds C-24, C-25, C-26 (5 pts each, ceiling 180). I'll isolate one new criterion per single-axis variation, then combine.

---

# prove-interview — Round 9 Variations (V-01 through V-05)

**R8 baseline carried:** C-01..C-23 all PASS = 165 pts. The only variable across R9 variations is whether C-24, C-25, and C-26 are structurally present.

**Variation axes chosen:**
- **Role Sequence** → C-25 (Incumbent as S-00 with transcript-first ordering)
- **Output Format** → C-24 (Tabular Arc Signal with three explicit columns)
- **Lifecycle Emphasis** → C-26 (ARC SIGNAL POLICY named compliance block)

**Predicted scores:**

| Variation | Axis | C-24 | C-25 | C-26 | Total |
|-----------|------|------|------|------|-------|
| V-01 | Role Sequence | FAIL | PASS | FAIL | 170/180 |
| V-02 | Output Format | PASS | FAIL | FAIL | 170/180 |
| V-03 | Lifecycle Emphasis | FAIL | FAIL | PASS | 170/180 |
| V-04 | Combination: C-24 + C-25 | PASS | PASS | FAIL | 175/180 |
| V-05 | Full ceiling: C-24 + C-25 + C-26 | PASS | PASS | PASS | 180/180 |

---

## V-01 — Role Sequence axis: Incumbent as S-00 with transcript-first ordering

**Hypothesis:** Declaring the Incumbent as S-00 (position zero, before S-01) in the Human Subjects roster and enforcing transcript-first ordering makes the lifecycle provenance guarantee structural rather than authorial — no human-subject interview can appear before the Incumbent Coupling Table is written, by construction. Arc Signal remains prose (C-24 absent). No ARC SIGNAL POLICY block (C-26 absent).

**Expected:** C-25 PASS (+5), C-24 FAIL (0), C-26 FAIL (0) → **170/180**

---

```markdown
You are running the **prove-interview** skill for Signal.

**Topic**: {TOPIC}
**Signal**: {SIGNAL}
**Date**: {DATE}

Simulate a stakeholder and customer interview series using persona-driven methodology.
The interview is a simulation — it is not real, but it is grounded in each persona's
documented knowledge, role-specific concerns, and plausible domain behavior.

Output artifact: `simulations/prove/investigations/{topic}-interview-{date}.md`

---

## COMPLIANCE INFRASTRUCTURE

### COLUMN POLICY

The Evidence Pull table for each subject requires four columns. The following failure
conditions are declared here and apply to every Evidence Pull row without exception.
Column additions are additive — they do not discharge any existing required column.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Quote present but Rationale absent | Interpretive signal context — why this signal matters to the topic decision | FAILS C-10, C-16 |
| Rationale present but Quote absent | Source turn verification — verbatim evidence of what was actually said | FAILS C-14, C-16 |
| Any added column displaces Quote or Rationale from any row | Non-substitutability — column additions are additive regardless of descriptive value | FAILS C-16 |
| Switch Cost column added to Inertia Verdict Matrix | Not absent — additive supplementation; Switch Cost supplements Evidence Pull columns without displacing them; C-16 violations in Evidence Pull tables are independent of C-22 status | Additive rule — no violation |
| Quote + Confidence present, Rationale absent | Interpretive basis for confidence rating | FAILS C-10, C-16 |
| Rationale + Confidence present, Quote absent | Source turn verification | FAILS C-14, C-16 |

### DISPOSITION REQUIREMENT

The Human Subjects roster requires per-subject disposition labels before any transcript
begins. The following failure conditions apply to roster construction and Arc Signal framing.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Roster entry with no Disposition value | Per-subject stance declaration before interview transcript | FAILS C-17 |
| SKEPTIC absent from roster | Skeptic voice — resistance or friction grounded in role-based concerns | FAILS C-11, C-17 |
| CHAMPION absent from roster | Advocate voice — adoption or validation grounded in role-based opportunity | FAILS C-11, C-17 |
| CHAMPION declared before SKEPTIC in roster order | Skeptic-first roster ordering — SKEPTIC must be S-01, CHAMPION must be S-02 | FAILS C-18 |
| SKEPTIC-first roster present but Arc Signal uses symmetric two-voice comparison | Prior-signal framing — Arc Signal must derive from skeptic resistance as epistemic prior, not equal-weight comparison | FAILS C-18 |
| SKEPTIC-first roster present but Arc Signal does not frame SKEPTIC as the prior signal | Skeptic-as-prior framing derivation in Arc Signal synthesis | FAILS C-18 |

---

## HUMAN SUBJECTS ROSTER

Declare all subjects before any transcript begins. S-00 is the Incumbent — the existing
tool, practice, or vendor being displaced. S-00 appears first in the roster and first in
transcript order. This is a structural ordering constraint: the Incumbent Coupling Table
(populated from S-00) must be complete before S-01 or S-02 transcripts begin.

S-01 is the SKEPTIC (first human subject). S-02 is the CHAMPION. This order is not
cosmetic — it encodes the epistemic structure: skeptic resistance is the prior signal;
champion confirmation or overturn is the evidence.

| ID | Role-Title | Domain | Disposition |
|----|-----------|--------|-------------|
| S-00 | [Current incumbent — existing tool, vendor, or practice being evaluated for displacement] | [Domain] | INCUMBENT — baseline for switching-cost coupling; appears first in transcript order |
| S-01 | [Role of skeptic stakeholder] | [Domain] | SKEPTIC — resistance or friction grounded in role-specific concerns, not generic change-aversion |
| S-02 | [Role of champion stakeholder] | [Domain] | CHAMPION — advocacy or adoption enthusiasm grounded in role-specific opportunity |

**SKEPTIC-FIRST REQUIREMENT:** S-01 is the prior signal. If S-01 resistance is not role-grounded
(C-05 check: generic "change is hard" framing fails regardless of SKEPTIC label), the
arc synthesis has no valid prior. S-02 confirmation of an ungrounded SKEPTIC is not signal.

**S-00 LIFECYCLE CONSTRAINT:** S-00 transcript and Incumbent Coupling Table must be complete
before S-01 appears in the output. This makes provenance structural — the coupling factor
names and switching-cost ratings in the Inertia Verdict Matrix Switch Cost column are
provenance-verified by construction (they existed before the human-subject interviews ran).

---

## STEP 0 — CONTEXT

Before running any interview, read prior signal artifacts for this topic if they exist:
`simulations/{namespace}/.../{topic}-*-{date}.md`

Note any signals already gathered. Note the feature or decision under investigation.
State the topic and the question this interview series is designed to answer.

---

## STEP 1 — INCUMBENT BASELINE (S-00)

**S-00 is the incumbent.** The incumbent is not a human stakeholder — it is the existing
system, tool, vendor, workflow, or practice that would be displaced or supplemented by
the feature under investigation.

### Prior Knowledge Block — S-00

Before the transcript begins, declare:
- **Identity**: What is the incumbent? Name it specifically.
- **Current-practice anchor**: What does it do today that would be displaced? (This is
  the foundation for Q1.)
- **Domain footprint**: What workflows, integrations, or user habits depend on it?
- **Switching-cost basis**: What categories of friction would switching entail?
  (Data migration, retraining, contract obligations, workflow disruption, etc.)

### S-00 Transcript — Incumbent Baseline Interview

Open with a neutral current-practice question: ask what the incumbent does today,
before any feature is introduced. This is Q1. The Q1 answer establishes the
behavioral baseline the Incumbent Coupling Table draws from.

Minimum 3 turns. Q2 probes one specific coupling dimension raised in Q1.
Q3 asks about switching — what would the incumbent lose if displaced?

Format each turn as:
```
**INTERVIEWER:** [Question]
**S-00 (INCUMBENT):** [Answer in the incumbent's framing — not a human voice, but a
structured account of what the incumbent currently provides, grounded in its actual
capability domain. Answers reference specific features, integrations, or behaviors the
incumbent is known for. Generic "we provide value" answers fail C-05.]
```

**Surprise (one sentence):** [One specific answer from S-00 that reveals a coupling
dimension the interviewer's questions did not anticipate. Label it explicitly.]

### Incumbent Coupling Table

After the S-00 transcript is complete, extract all switching-cost coupling factors
into a named table. This table is the structural source for the Switch Cost column
in the Inertia Verdict Matrix.

| Coupling Factor | Switching-Cost Rating | Basis (HE-# from S-00 transcript) |
|-----------------|----------------------|-----------------------------------|
| [Named factor — workflow dependency, data format lock-in, integration contract, etc.] | HIGH / MEDIUM / LOW | [S-00 turn that grounds this rating] |

Minimum one factor required. Each factor must be named specifically — not "general friction"
or "switching cost." The factor name is what subsequent Arc Signal claims must cite.

**LIFECYCLE GATE:** The Incumbent Coupling Table is now structurally locked. Per-factor names
and switching-cost ratings are final. The S-01 and S-02 transcripts that follow cannot
retroactively change the coupling factor names or ratings. The Arc Signal is authored after
the transcripts complete, but the coupling data it draws from was locked here at Step 1.

### Evidence Pull — S-00

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim turn from S-00 — exact words, not paraphrased] | [Why does this signal matter to the topic decision? Not a restatement of the quote.] | HIGH / MEDIUM / LOW | [Signal type: coupling factor, switching barrier, integration dependency, workflow anchor] |

Apply COLUMN POLICY to every row. If a row is missing Quote or Rationale, name the
criterion violated before continuing.

---

## STEP 2 — HUMAN SUBJECT INTERVIEWS

S-01 (SKEPTIC) is interviewed first. S-02 (CHAMPION) is interviewed second.
This ordering is structural: skeptic resistance is the prior signal.

For each subject, follow this structure:

### Prior Knowledge Block

Before the transcript begins, declare:
- **Role and title**: Specific enough that vocabulary and concerns are predictable
- **Domain background**: What they know about the incumbent and the proposed feature
- **Knowledge gaps**: What they don't know — blind spots that may affect their signal
- **Primary concern**: The thing they care most about in this decision
- **Current-practice anchor field**: What they do today that intersects with this feature

### Interview Transcript

Q1 must be a neutral current-practice question — ask what the subject does today,
before any feature is introduced. This establishes the behavioral baseline for
subsequent feature-reaction contrast.

Q2 probes the named stance declared in the Prior Knowledge Block.
Q3 references something specific from a prior subject's interview (cross-subject contrast).
Minimum 3 turns.

Format:
```
**INTERVIEWER:** [Question]
**[SUBJECT LABEL]:** [Answer in persona voice — vocabulary, concerns, and framing
match the declared role. Generic answers that could come from any persona fail C-03.
Answers reference role-specific constraints or domain knowledge from the Prior Knowledge Block.]
```

**Surprise (one sentence):** [Something the interviewer did not anticipate — label it explicitly.]

### Evidence Pull — [Subject Label]

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim subject turn — not paraphrased] | [Why this signal matters to the topic decision] | HIGH / MEDIUM / LOW | [insight / concern / requirement / contradiction] |

Apply COLUMN POLICY to every row.

---

## STEP 3 — SYNTHESIS

### Pattern

One paragraph. Note the dominant pattern across all subjects — not a summary of
each interview, but an observation about what the signals say together.

### Critical Contradiction Table

Identify the single most significant contradiction between interview subjects.
Name it. Explain its evidential weight — what it confirms, undermines, or leaves unresolved.
Rank contradictions by evidential weight; do not merely enumerate them.

| Contradiction | Side A — [Subject] (HE-# verbatim quote) | Side B — [Subject] (HE-# verbatim quote) | Stakes |
|---------------|------------------------------------------|------------------------------------------|--------|
| [Name the contradiction] | "[Verbatim quote from S-01 or S-02]" | "[Verbatim quote from the opposing subject]" | [What is at risk if this tension persists into implementation] |

Both sides must be sourced verbatim. Naming the contradiction without quoting both sides
leaves the opposing position asserted on the unsourced side.

### Tension Resolution

One paragraph. Does the evidence resolve the critical contradiction, or does it persist?
What follow-on signal would resolve it?

### Inertia Verdict Matrix

| Subject | Verdict | Switch Cost | Rationale |
|---------|---------|-------------|-----------|
| S-01 [Role] | ADOPT / DEFER / RESIST | [Switching-cost assessment sourced from Incumbent Coupling Table — cite the table by name] | [Role-grounded rationale] |
| S-02 [Role] | ADOPT / DEFER / RESIST | [Switching-cost assessment sourced from Incumbent Coupling Table — cite the table by name] | [Role-grounded rationale] |

Switch Cost column entries must cite the Incumbent Coupling Table by name.
Coexistence without attribution does not satisfy the sourcing requirement.

### Arc Signal

**Prior signal (SKEPTIC S-01):** "[Verbatim quote from S-01's most resistance-anchored turn]"
**Subsequent evidence (CHAMPION S-02):** "[Verbatim quote from S-02's most confirmation-anchored turn]"

This is not a symmetric comparison between two equal voices. S-01 resistance is the
epistemic prior; S-02 confirmation or overturn is the evidence. The arc derives from
this asymmetry.

**Per-factor incumbent friction:** For each coupling factor in the Incumbent Coupling Table,
state the following:
1. Identify the coupling factor by its row name in the Incumbent Coupling Table
2. State the switching friction magnitude from the coupling table rating
3. Connect it to an inertia verdict component — explain whether the friction confirms,
   moderates, or overturns the inertia signal

Do not describe switching friction without naming the specific coupling factor by its
row name in the Incumbent Coupling Table. Magnitude without coupling factor row name
citation = incomplete — the coupling factor name is the provenance link.

**Dominant arc:** [Convergence despite skeptic resistance (strong signal — skeptic concern
confirmed present, then overturned by champion evidence) / Skeptic resistance
unconfirmed by champion (insufficient evidence — revisit framing) / Skeptic resistance
confirmed by champion silence (cautionary signal — surface for follow-on investigation)]

### Prior Assumption Revisited

What did the interviewer assume before running this series? What did the interviews
confirm? What did they overturn? One paragraph.

---

## OUTPUT FORMAT

Write to: `simulations/prove/investigations/{topic}-interview-{date}.md`

Before filing, verify:
- S-00 transcript appears before S-01 transcript in the output (structural gate — C-25 check)
- Incumbent Coupling Table is present and populated from S-00 content
- Every Evidence Pull row passes Column Policy (Quote + Rationale + Confidence + Signal)
- Roster disposition labels present for all human subjects (S-01, S-02) before transcripts
- SKEPTIC = S-01, CHAMPION = S-02 in roster ordering
- Arc Signal cites each coupling factor by its row name in the Incumbent Coupling Table
- Critical Contradiction Table has verbatim quotes from both sides
- Inertia Verdict Matrix Switch Cost column cites Incumbent Coupling Table by name
```

---

## V-02 — Output Format axis: Tabular Arc Signal with three explicit columns

**Hypothesis:** Rendering the Arc Signal as a three-column table with explicit headers (Coupling Factor / Friction Magnitude / Inertia Component) — one row per coupling factor — makes each per-factor C-23 condition independently verifiable without sentence-level ambiguity. The structural argument is parallel to C-21: tabular format eliminates the possibility of a multi-condition sentence that satisfies two conditions for one factor while leaving a second factor untraced. Incumbent is not declared as S-00 (prose lifecycle gate only, C-25 absent). No ARC SIGNAL POLICY block (C-26 absent).

**Expected:** C-24 PASS (+5), C-25 FAIL (0), C-26 FAIL (0) → **170/180**

---

```markdown
You are running the **prove-interview** skill for Signal.

**Topic**: {TOPIC}
**Signal**: {SIGNAL}
**Date**: {DATE}

Simulate a stakeholder and customer interview series using persona-driven methodology.
The interview is a simulation — not real, but grounded in each persona's documented
knowledge, role-specific concerns, and plausible domain behavior.

Output artifact: `simulations/prove/investigations/{topic}-interview-{date}.md`

---

## COMPLIANCE INFRASTRUCTURE

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Quote present but Rationale absent | Interpretive signal context — why this signal matters to the topic decision | FAILS C-10, C-16 |
| Rationale present but Quote absent | Source turn verification — verbatim evidence of what was actually said | FAILS C-14, C-16 |
| Any added column displaces Quote or Rationale from any row | Non-substitutability — additive-only rule applies regardless of addition's descriptive value | FAILS C-16 |
| Switch Cost column in Inertia Verdict Matrix | Not absent — additive supplementation; C-16 violations in Evidence Pull tables remain independent of C-22 status | Additive rule — no violation |
| Quote + Confidence present, Rationale absent | Interpretive basis for confidence rating | FAILS C-10, C-16 |
| Rationale + Confidence present, Quote absent | Source turn verification | FAILS C-14, C-16 |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Roster entry with no Disposition value | Per-subject stance declaration before transcript | FAILS C-17 |
| SKEPTIC absent from roster | Skeptic voice grounded in role-specific resistance | FAILS C-11, C-17 |
| CHAMPION absent from roster | Advocate voice grounded in role-specific opportunity | FAILS C-11, C-17 |
| CHAMPION declared before SKEPTIC in roster | Skeptic-first ordering | FAILS C-18 |
| SKEPTIC-first roster with symmetric Arc Signal framing | Skeptic-as-prior-signal framing derivation | FAILS C-18 |
| SKEPTIC-first roster, Arc Signal does not derive from skeptic resistance as prior | Prior-signal framing absent | FAILS C-18 |

---

## HUMAN SUBJECTS ROSTER

Declare all subjects before any transcript begins.
The Incumbent is the existing tool, vendor, or practice being evaluated for displacement.
Declare it in the roster before S-01 and S-02, using whatever position label is appropriate.

S-01 is the SKEPTIC. S-02 is the CHAMPION. SKEPTIC appears first.

| ID | Role-Title | Domain | Disposition |
|----|-----------|--------|-------------|
| S-00 | [Incumbent — existing tool, vendor, or practice] | [Domain] | INCUMBENT — switching-cost baseline |
| S-01 | [Skeptic role] | [Domain] | SKEPTIC |
| S-02 | [Champion role] | [Domain] | CHAMPION |

**SKEPTIC-FIRST REQUIREMENT:** S-01 resistance is the prior signal. S-02 confirmation or
overturn is the evidence. This asymmetry drives the Arc Signal framing.

**LIFECYCLE RULE:** Populate the Incumbent Coupling Table from the incumbent interview
before proceeding to human-subject interviews. The coupling factor names and
switching-cost ratings must be established from the incumbent baseline — not inferred
retroactively from the Inertia Verdict Matrix.

---

## STEP 0 — CONTEXT

Read prior signal artifacts for this topic if they exist.
State the topic, the feature or decision under investigation, and the question this
interview series is designed to answer.

---

## STEP 1 — INCUMBENT BASELINE

The incumbent interview establishes the switching-cost baseline. The Incumbent Coupling
Table is the structural output of this step. It feeds the Switch Cost column in the
Inertia Verdict Matrix.

### Prior Knowledge Block — Incumbent

- **Identity**: Name the incumbent specifically
- **Current-practice anchor**: What it does today that would be displaced
- **Domain footprint**: Workflows, integrations, user habits that depend on it
- **Switching-cost basis**: Categories of friction switching would entail

### Incumbent Transcript

Q1: Neutral current-practice question — what does the incumbent provide today, before
any feature is introduced?
Q2: Probe one specific coupling dimension raised in Q1.
Q3: What would the incumbent lose if displaced?
Minimum 3 turns.

```
**INTERVIEWER:** [Question]
**INCUMBENT:** [Answer grounded in actual incumbent capability — not generic value claims.
References specific features, integrations, or behaviors the incumbent is known for.]
```

**Surprise (one sentence):** [Unexpected coupling dimension revealed in the transcript.]

### Incumbent Coupling Table

| Coupling Factor | Switching-Cost Rating | Basis (S-00 turn reference) |
|-----------------|----------------------|-----------------------------|
| [Specific named factor — not generic "switching costs"] | HIGH / MEDIUM / LOW | [S-00 turn that grounds the rating] |

Minimum one factor. Each factor must be named — this name is what the Arc Signal table
rows must cite.

### Evidence Pull — Incumbent

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim S-00 turn] | [Why this matters to the topic decision] | HIGH / MEDIUM / LOW | [coupling factor / switching barrier / integration dependency] |

---

## STEP 2 — HUMAN SUBJECT INTERVIEWS

S-01 (SKEPTIC) first. S-02 (CHAMPION) second.

For each subject:

### Prior Knowledge Block

- Role and title (specific)
- Domain background
- Knowledge gaps
- Primary concern
- Current-practice anchor field (what they do today)

### Interview Transcript

Q1: Neutral current-practice question (before any feature introduced).
Q2: Probe the named stance from the Prior Knowledge Block.
Q3: Cross-subject contrast — name the specific claim from a prior subject. Do not refer generically.
Minimum 3 turns.

```
**INTERVIEWER:** [Question]
**[SUBJECT LABEL]:** [Answer in persona voice — vocabulary, concerns, and framing match
the declared role. Generic AI-sounding answers that could belong to any persona fail C-03.]
```

**Surprise (one sentence):** [Label explicitly.]

### Evidence Pull — [Subject]

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim subject turn] | [Why this matters] | HIGH / MEDIUM / LOW | [type] |

---

## STEP 3 — SYNTHESIS

### Pattern

One paragraph. What do the signals say together — not a per-subject summary.

### Critical Contradiction Table

| Contradiction | Side A (HE-# verbatim quote) | Side B (HE-# verbatim quote) | Stakes |
|---------------|------------------------------|------------------------------|--------|
| [Named contradiction — ranked by evidential weight] | "[Verbatim quote]" | "[Verbatim quote from opposing subject]" | [What is at risk] |

Both sides verbatim. Ranking required — enumerating contradictions without ranking them
fails this section.

### Tension Resolution

Does the evidence resolve the critical contradiction, or does it persist? One paragraph.

### Inertia Verdict Matrix

| Subject | Verdict | Switch Cost | Rationale |
|---------|---------|-------------|-----------|
| S-01 [Role] | ADOPT / DEFER / RESIST | [Sourced from Incumbent Coupling Table — cite by name] | [Role-grounded] |
| S-02 [Role] | ADOPT / DEFER / RESIST | [Sourced from Incumbent Coupling Table — cite by name] | [Role-grounded] |

### Arc Signal

**Prior signal (SKEPTIC S-01):** "[Verbatim quote from S-01's most resistance-anchored turn]"
**Subsequent evidence (CHAMPION S-02):** "[Verbatim quote from S-02's most confirmation-anchored turn]"

This is not a symmetric two-voice comparison. S-01 resistance is the epistemic prior.

**Incumbent Switching Friction:**

Render the following as a structured table — one row per coupling factor from the
Incumbent Coupling Table. Each row must independently identify the coupling factor
by its table row name, state the friction magnitude from the coupling table rating,
and connect it to an inertia verdict component.

| Coupling Factor | Friction Magnitude | Inertia Component |
|-----------------|-------------------|-------------------|
| [Exact row name from Incumbent Coupling Table] | [Switching-cost rating from coupling table: HIGH / MEDIUM / LOW] | [confirms / moderates / overturns the inertia signal — one sentence explaining the connection] |

One row per coupling factor. Column headers must be exactly: Coupling Factor /
Friction Magnitude / Inertia Component. Each row independently satisfies all three
per-factor conditions: (1) coupling factor named by table row, (2) friction magnitude
from coupling table rating stated, (3) inertia verdict connection explained.
Do not merge factors across rows. Do not substitute prose for the table.

**Dominant arc:** [Convergence despite skeptic resistance (strong signal) /
Unconfirmed skeptic resistance (insufficient evidence) /
Skeptic resistance confirmed by champion silence (cautionary signal)]

### Prior Assumption Revisited

What did the interviewer assume before running this series? What was confirmed?
What was overturned? One paragraph.

---

## OUTPUT FORMAT

Write to: `simulations/prove/investigations/{topic}-interview-{date}.md`

Pre-filing checklist:
- Every Evidence Pull row: Quote + Rationale + Confidence + Signal (Column Policy)
- Roster: SKEPTIC = S-01, CHAMPION = S-02, disposition labels before transcripts
- Incumbent Coupling Table: complete, sourced from incumbent transcript content
- Inertia Verdict Matrix Switch Cost column: cites Incumbent Coupling Table by name
- Arc Signal table: three columns (Coupling Factor / Friction Magnitude / Inertia Component),
  one row per coupling factor, each row independently satisfying all three C-23 conditions
- Critical Contradiction Table: both sides verbatim, ranked by evidential weight
```

---

## V-03 — Lifecycle Emphasis axis: ARC SIGNAL POLICY named compliance block

**Hypothesis:** A named ARC SIGNAL POLICY compliance block with the magnitude-without-name PARTIAL discriminator declared as condition (2) makes the most common C-23/C-24 failure mode structurally visible during output review — prose that correctly characterizes switching friction magnitude without tracing it to a named Incumbent Coupling Table row is the C-23 PARTIAL/PASS boundary failure, and it requires a named declared condition to be caught during structural review rather than relying on criterion text inspection. Arc Signal remains prose (C-24 FAIL — the ARC SIGNAL POLICY block itself flags this failure mode). No S-00 structural ordering (C-25 absent).

**Expected:** C-26 PASS (+5), C-24 FAIL (0), C-25 FAIL (0) → **170/180**

---

```markdown
You are running the **prove-interview** skill for Signal.

**Topic**: {TOPIC}
**Signal**: {SIGNAL}
**Date**: {DATE}

Simulate a stakeholder and customer interview series using persona-driven methodology.
The interview is a simulation — not real, but grounded in each persona's documented
knowledge, role-specific concerns, and plausible domain behavior.

Output artifact: `simulations/prove/investigations/{topic}-interview-{date}.md`

---

## COMPLIANCE INFRASTRUCTURE

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Quote present but Rationale absent | Interpretive signal context | FAILS C-10, C-16 |
| Rationale present but Quote absent | Source turn verification | FAILS C-14, C-16 |
| Any added column displaces Quote or Rationale | Non-substitutability — additive-only rule unconditional | FAILS C-16 |
| Switch Cost column in Inertia Verdict Matrix | Additive supplementation — no displacement; C-16 violations in Evidence tables are independent of C-22 status | Additive rule — no violation |
| Quote + Confidence present, Rationale absent | Interpretive basis for confidence rating | FAILS C-10, C-16 |
| Rationale + Confidence present, Quote absent | Source turn verification | FAILS C-14, C-16 |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Roster entry with no Disposition value | Per-subject stance declaration | FAILS C-17 |
| SKEPTIC absent from roster | Skeptic voice grounded in role-specific concerns | FAILS C-11, C-17 |
| CHAMPION absent from roster | Advocate voice grounded in role-specific opportunity | FAILS C-11, C-17 |
| CHAMPION declared before SKEPTIC | Skeptic-first ordering | FAILS C-18 |
| SKEPTIC-first roster with symmetric Arc Signal framing | Prior-signal framing derivation | FAILS C-18 |
| SKEPTIC-first roster, Arc Signal treats both voices as equal weight | Skeptic-as-prior epistemic asymmetry | FAILS C-18 |

### ARC SIGNAL POLICY

Compliance artifact for the C-23/C-24 chain. These conditions are declared here so that
per-factor friction failures are structurally visible during output review — not only
detectable through criterion inspection. Condition (2) is the key discriminating entry:
friction magnitude present but coupling factor row name absent is the most common failure
mode at the C-23 PARTIAL/PASS boundary.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Per-factor friction claim absent from Arc Signal | Named coupling factor from Incumbent Coupling Table in synthesis narrative | FAILS C-23 |
| Friction magnitude present in Arc Signal but coupling factor not cited by its Incumbent Coupling Table row name | Coupling factor row name — magnitude-without-name is the discriminating condition: friction described at correct magnitude without provenance to a named table row earns PARTIAL regardless of accuracy | C-23 PARTIAL |
| Arc Signal rendered in prose form without tabular structure | Three-column table with Coupling Factor / Friction Magnitude / Inertia Component headers | FAILS C-24 |
| Arc Signal table present but fewer than three required column headers | One or more column headers from the set {Coupling Factor, Friction Magnitude, Inertia Component} absent or unlabeled | C-24 PARTIAL |

---

## HUMAN SUBJECTS ROSTER

Declare all subjects before any transcript begins.

| ID | Role-Title | Domain | Disposition |
|----|-----------|--------|-------------|
| S-00 | [Incumbent — existing tool, vendor, or practice] | [Domain] | INCUMBENT — switching-cost baseline |
| S-01 | [Skeptic role] | [Domain] | SKEPTIC |
| S-02 | [Champion role] | [Domain] | CHAMPION |

**SKEPTIC-FIRST REQUIREMENT:** S-01 is the prior signal. This ordering is not cosmetic —
the Arc Signal synthesis derives from skeptic resistance as the epistemic prior.

**LIFECYCLE RULE:** Populate the Incumbent Coupling Table from the incumbent baseline
interview before proceeding to human-subject interviews (S-01, S-02). Per-factor coupling
factor names and switching-cost ratings are established from the incumbent content —
not inferred retroactively from synthesis. This lifecycle rule is enforced by authorial
discipline; the Incumbent Coupling Table must be visibly complete before the first
S-01 question appears in the output.

---

## STEP 0 — CONTEXT

Read prior signals for this topic. State the topic, the feature under investigation,
and the question this interview series is designed to answer.

---

## STEP 1 — INCUMBENT BASELINE

### Prior Knowledge Block — Incumbent

- **Identity**: Name the incumbent specifically
- **Current-practice anchor**: What it provides today that would be displaced
- **Domain footprint**: Workflows, integrations, habits that depend on it
- **Switching-cost basis**: Categories of friction switching would entail

### Incumbent Transcript

Q1: Neutral — what does the incumbent provide today, before any feature introduced?
Q2: Probe one specific coupling dimension from Q1.
Q3: What would be lost if displaced?
Minimum 3 turns.

```
**INTERVIEWER:** [Question]
**INCUMBENT:** [Answer grounded in actual incumbent capability. Not generic value claims.]
```

**Surprise (one sentence):** [Unexpected coupling dimension — label explicitly.]

### Incumbent Coupling Table

| Coupling Factor | Switching-Cost Rating | Basis (S-00 turn reference) |
|-----------------|----------------------|-----------------------------|
| [Named factor — specific, not generic] | HIGH / MEDIUM / LOW | [S-00 turn that grounds the rating] |

Each factor must be named. The name is what Arc Signal prose must cite.
Lifecycle rule: this table is complete at end of Step 1. Do not revise after S-01 or S-02 interviews.

### Evidence Pull — Incumbent

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim S-00 turn] | [Why this matters to the topic decision] | HIGH / MEDIUM / LOW | [type] |

---

## STEP 2 — HUMAN SUBJECT INTERVIEWS

S-01 (SKEPTIC) first. S-02 (CHAMPION) second.

### Prior Knowledge Block (per subject)

Role and title / Domain background / Knowledge gaps / Primary concern / Current-practice anchor field.

### Interview Transcript (per subject)

Q1: Neutral current-practice question.
Q2: Probe named stance from Prior Knowledge Block.
Q3: Name a specific claim from a prior subject — do not refer generically.
Minimum 3 turns. Persona voice throughout.

```
**INTERVIEWER:** [Question]
**[SUBJECT LABEL]:** [Persona-voice answer — role vocabulary, role concerns, role framing.
Answers that could come from any persona fail C-03.]
```

**Surprise (one sentence):** [Labeled explicitly.]

### Evidence Pull (per subject)

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim turn] | [Why this matters] | HIGH / MEDIUM / LOW | [type] |

---

## STEP 3 — SYNTHESIS

### Pattern

One paragraph — what the signals say together, not per-subject summaries.

### Critical Contradiction Table

| Contradiction | Side A (verbatim quote) | Side B (verbatim quote) | Stakes |
|---------------|------------------------|------------------------|--------|
| [Named contradiction — ranked by evidential weight, not merely enumerated] | "[Verbatim from one subject]" | "[Verbatim from opposing subject]" | [What is at risk] |

### Tension Resolution

One paragraph. Does the evidence resolve the contradiction? One follow-on signal that
would resolve it if not.

### Inertia Verdict Matrix

| Subject | Verdict | Switch Cost | Rationale |
|---------|---------|-------------|-----------|
| S-01 [Role] | ADOPT / DEFER / RESIST | [Sourced from Incumbent Coupling Table — cite by name] | [Role-grounded] |
| S-02 [Role] | ADOPT / DEFER / RESIST | [Sourced from Incumbent Coupling Table — cite by name] | [Role-grounded] |

### Arc Signal

**Prior signal (SKEPTIC S-01):** "[Verbatim quote from S-01's most resistance-anchored turn]"
**Subsequent evidence (CHAMPION S-02):** "[Verbatim quote from S-02's most confirmation-anchored turn]"

This is not a symmetric two-voice comparison. S-01 resistance is the epistemic prior;
S-02 evidence either confirms the prior (strong incumbent inertia signal) or overturns
it (weak incumbent inertia signal — feature has genuine displacement potential).

**Per-factor incumbent friction:** For each coupling factor in the Incumbent Coupling Table:
(1) Identify the coupling factor by its row name in the Incumbent Coupling Table.
(2) State the switching friction magnitude from the coupling table rating.
(3) Connect to an inertia verdict component — explain whether the friction confirms,
    moderates, or overturns the inertia signal.

Note: prose friction description at the correct magnitude but without naming the specific
coupling factor by its Incumbent Coupling Table row name = C-23 PARTIAL (see ARC SIGNAL
POLICY, condition 2). The row name citation is the provenance link. Prose Arc Signal
without tabular structure = C-24 absent (see ARC SIGNAL POLICY, condition 3).

**Dominant arc:** [Convergence despite skeptic resistance / Unconfirmed / Cautionary]

### Prior Assumption Revisited

What was assumed before this series? What was confirmed? What was overturned? One paragraph.

---

## OUTPUT FORMAT

Write to: `simulations/prove/investigations/{topic}-interview-{date}.md`

Pre-filing:
- Every Evidence Pull row: Quote + Rationale + Confidence + Signal
- Roster: SKEPTIC = S-01, CHAMPION = S-02, disposition labels before transcripts
- Incumbent Coupling Table: complete from Step 1 content, not revised after S-01/S-02
- Arc Signal: cites each coupling factor by its row name (see ARC SIGNAL POLICY condition 2)
- Inertia Verdict Matrix Switch Cost: cites Incumbent Coupling Table by name
- Critical Contradiction: both sides verbatim, ranked by evidential weight
```

---

## V-04 — Combination: C-24 (Output Format) + C-25 (Role Sequence)

**Hypothesis:** Combining tabular Arc Signal (C-24) with Incumbent-as-S-00 structural ordering (C-25) produces a provenance chain that is verified by construction at two levels: S-00 position ensures the coupling factor names and ratings exist structurally before any human-subject interview runs; the tabular Arc Signal format ensures each coupling factor row satisfies all three C-23 conditions without sentence-level ambiguity. No ARC SIGNAL POLICY block (C-26 absent — the compliance infrastructure for the C-24/C-23 chain is not yet named).

**Expected:** C-24 PASS (+5), C-25 PASS (+5), C-26 FAIL (0) → **175/180**

---

```markdown
You are running the **prove-interview** skill for Signal.

**Topic**: {TOPIC}
**Signal**: {SIGNAL}
**Date**: {DATE}

Simulate a stakeholder and customer interview series using persona-driven methodology.
The interview is a simulation — not real, but grounded in each persona's documented
knowledge, role-specific concerns, and plausible domain behavior.

Output artifact: `simulations/prove/investigations/{topic}-interview-{date}.md`

---

## COMPLIANCE INFRASTRUCTURE

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Quote present but Rationale absent | Interpretive signal context | FAILS C-10, C-16 |
| Rationale present but Quote absent | Source turn verification | FAILS C-14, C-16 |
| Any added column displaces Quote or Rationale | Non-substitutability — additive-only rule unconditional | FAILS C-16 |
| Switch Cost column in Inertia Verdict Matrix | Additive supplementation — not displacement; C-16 violations in Evidence tables remain independent of C-22 status | Additive rule — no violation |
| Quote + Confidence present, Rationale absent | Interpretive basis for confidence rating | FAILS C-10, C-16 |
| Rationale + Confidence present, Quote absent | Source turn verification | FAILS C-14, C-16 |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Roster entry with no Disposition value | Per-subject stance declaration | FAILS C-17 |
| SKEPTIC absent from roster | Skeptic voice | FAILS C-11, C-17 |
| CHAMPION absent from roster | Advocate voice | FAILS C-11, C-17 |
| CHAMPION declared before SKEPTIC | Skeptic-first ordering | FAILS C-18 |
| SKEPTIC-first roster with symmetric Arc Signal framing | Prior-signal framing derivation | FAILS C-18 |
| SKEPTIC-first roster, Arc Signal uses equal-weight two-voice comparison | Skeptic-as-prior epistemic asymmetry | FAILS C-18 |

---

## HUMAN SUBJECTS ROSTER

S-00 is the Incumbent. S-00 is declared at position zero in the roster — before S-01 and
S-02. S-00 appears first in transcript order. This is a structural ordering constraint:
the Incumbent Coupling Table, populated from S-00, is provenance-verified by construction
before any human-subject interview begins. No human-subject turn can precede the Incumbent
Coupling Table in the output.

| ID | Role-Title | Domain | Disposition |
|----|-----------|--------|-------------|
| S-00 | [Incumbent — existing tool, vendor, or practice being evaluated for displacement] | [Domain] | INCUMBENT — S-00 structural position; first in transcript order; switching-cost baseline |
| S-01 | [Skeptic role] | [Domain] | SKEPTIC |
| S-02 | [Champion role] | [Domain] | CHAMPION |

**S-00 STRUCTURAL CONSTRAINT:** S-00 transcript and Incumbent Coupling Table appear before
any S-01 or S-02 content in the output. This is enforced by construction — the roster
position S-00 (before S-01) signals that the coupling data source must precede its consumers.
Incumbent S-00 is not a human subject. It does not receive a Disposition label of
SKEPTIC or CHAMPION. It receives the INCUMBENT label at position S-00.

**SKEPTIC-FIRST REQUIREMENT:** S-01 is the prior signal. S-02 is the subsequent evidence.
The Arc Signal synthesis is not a symmetric comparison — it derives from skeptic
resistance as the epistemic prior. Structural skeptic-first ordering in the roster enforces
the epistemic asymmetry at the output level.

---

## STEP 0 — CONTEXT

Read prior signals for this topic. State the topic, the feature under investigation,
and the question this interview series is designed to answer.

---

## STEP 1 — INCUMBENT BASELINE (S-00)

**S-00 appears first in the output.** The Incumbent Coupling Table must be complete
before Step 2 begins. This is the structural provenance guarantee: per-factor names
and switching-cost ratings are locked from S-00 content before any human-subject
interview is written.

### Prior Knowledge Block — S-00

- **Identity**: Name the incumbent specifically
- **Current-practice anchor**: What it provides today that would be displaced
- **Domain footprint**: Workflows, integrations, user habits that depend on it
- **Switching-cost basis**: Categories of friction switching would entail
  (data migration, retraining costs, contract lock-in, workflow disruption, etc.)

### S-00 Transcript

Q1: Neutral current-practice question — what does the incumbent provide today,
before any feature is introduced?
Q2: Probe one specific coupling dimension raised in Q1.
Q3: What would the incumbent lose if displaced?
Minimum 3 turns.

```
**INTERVIEWER:** [Question]
**S-00 (INCUMBENT):** [Answer grounded in actual incumbent capability. References specific
features, integrations, or behaviors the incumbent is known for. Not generic value claims.]
```

**Surprise (one sentence):** [Unexpected coupling dimension revealed in transcript. Label explicitly.]

### Incumbent Coupling Table

| Coupling Factor | Switching-Cost Rating | Basis (S-00 turn reference) |
|-----------------|----------------------|-----------------------------|
| [Specific named factor — this exact name is cited by Arc Signal table rows] | HIGH / MEDIUM / LOW | [S-00 turn that grounds the rating] |

Each factor must be named specifically. The factor name in this table is the provenance
anchor for Arc Signal table rows. Minimum one factor.

**STEP 1 GATE:** The Incumbent Coupling Table is complete. Per-factor names and ratings
are structurally locked. S-01 and S-02 interviews that follow cannot change these values.
The Arc Signal table that draws from this table will cite these exact row names.

### Evidence Pull — S-00

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim S-00 turn] | [Why this matters to the topic decision] | HIGH / MEDIUM / LOW | [coupling factor / barrier / dependency] |

Apply Column Policy to every row. If a row is missing Quote or Rationale, name the
criterion violated before continuing.

---

## STEP 2 — HUMAN SUBJECT INTERVIEWS

S-01 (SKEPTIC) first. S-02 (CHAMPION) second. S-00 content from Step 1 is now
structurally locked.

### Prior Knowledge Block (per subject)

- Role and title (specific)
- Domain background
- Knowledge gaps
- Primary concern
- Current-practice anchor field

### Interview Transcript (per subject)

Q1: Neutral current-practice question — what does the subject do today?
Q2: Probe the named stance from the Prior Knowledge Block.
Q3: Name a specific claim from a prior subject. Do not refer generically.
Minimum 3 turns. Persona voice throughout.

```
**INTERVIEWER:** [Question]
**[SUBJECT LABEL]:** [Persona-voice answer — role vocabulary, role concerns, role framing.]
```

**Surprise (one sentence):** [Labeled explicitly.]

### Evidence Pull (per subject)

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim turn] | [Why this matters] | HIGH / MEDIUM / LOW | [type] |

---

## STEP 3 — SYNTHESIS

### Pattern

One paragraph — what the signals say together.

### Critical Contradiction Table

| Contradiction | Side A (verbatim quote) | Side B (verbatim quote) | Stakes |
|---------------|------------------------|------------------------|--------|
| [Named — ranked by evidential weight] | "[Verbatim from one subject]" | "[Verbatim from opposing subject]" | [At risk] |

### Tension Resolution

One paragraph. Resolution state or follow-on signal needed.

### Inertia Verdict Matrix

| Subject | Verdict | Switch Cost | Rationale |
|---------|---------|-------------|-----------|
| S-01 [Role] | ADOPT / DEFER / RESIST | [Sourced from Incumbent Coupling Table — cite by name] | [Role-grounded] |
| S-02 [Role] | ADOPT / DEFER / RESIST | [Sourced from Incumbent Coupling Table — cite by name] | [Role-grounded] |

Switch Cost column entries must name the Incumbent Coupling Table as the source.
Coexistence without attribution does not satisfy the sourcing requirement.

### Arc Signal

**Prior signal (SKEPTIC S-01):** "[Verbatim quote from S-01's most resistance-anchored turn]"
**Subsequent evidence (CHAMPION S-02):** "[Verbatim quote from S-02's most confirmation-anchored turn]"

This is not a symmetric two-voice comparison. S-01 resistance is the epistemic prior.

**Incumbent Switching Friction — tabular:**

Render as a structured table. One row per coupling factor from the Incumbent Coupling Table.
Column headers must be exactly: **Coupling Factor / Friction Magnitude / Inertia Component**.
Each row must independently satisfy all three per-factor conditions:
(1) Coupling factor identified by its exact row name in the Incumbent Coupling Table
(2) Friction magnitude stated from the coupling table rating (HIGH / MEDIUM / LOW)
(3) Inertia verdict component explained — whether friction confirms, moderates, or overturns
    the inertia signal (one sentence per row)

Do not merge factors across rows. Do not substitute prose for the table.
Do not add a row without naming a coupling factor from the Incumbent Coupling Table.

| Coupling Factor | Friction Magnitude | Inertia Component |
|-----------------|-------------------|-------------------|
| [Exact row name from Incumbent Coupling Table] | [HIGH / MEDIUM / LOW from coupling table rating] | [confirms / moderates / overturns — one sentence] |

**Dominant arc:** [Convergence despite skeptic resistance (strong signal) /
Unconfirmed skeptic resistance (insufficient evidence) /
Skeptic resistance confirmed by champion silence (cautionary signal)]

### Prior Assumption Revisited

What was assumed? What was confirmed? What was overturned? One paragraph.

---

## OUTPUT FORMAT

Write to: `simulations/prove/investigations/{topic}-interview-{date}.md`

Pre-filing checklist:
- S-00 transcript and Incumbent Coupling Table appear before S-01 transcript (structural gate — verify S-00 is first in output)
- S-00 declared as S-00 in roster (position-zero declaration present)
- Every Evidence Pull row: Quote + Rationale + Confidence + Signal
- Roster: SKEPTIC = S-01, CHAMPION = S-02, disposition labels before transcripts
- Arc Signal table: three explicit columns (Coupling Factor / Friction Magnitude / Inertia Component), one row per coupling factor, each row independently satisfying all three C-23 conditions
- Inertia Verdict Matrix Switch Cost: cites Incumbent Coupling Table by name per row
- Critical Contradiction: both sides verbatim, ranked by evidential weight
```

---

## V-05 — Full ceiling: C-24 + C-25 + C-26

**Hypothesis:** Maximum R9 architecture. Structural ceilings for C-23, C-22, and C-19 active simultaneously: (1) tabular Arc Signal with three explicit columns enforces per-factor C-23 condition isolation one row at a time — no sentence-level ambiguity; (2) Incumbent-as-S-00 with transcript-first ordering makes the lifecycle provenance guarantee structural rather than authorial; (3) ARC SIGNAL POLICY named compliance block with the magnitude-without-name PARTIAL discriminator declared as condition (2) makes the most common C-23/C-24 failure mode structurally visible during output review. All three structural ceilings (C-21 analog for Arc Signal, C-25 analog for lifecycle, C-26 as compliance infrastructure extension) are active and independently gradable.

**Expected:** C-24 PASS (+5), C-25 PASS (+5), C-26 PASS (+5) → **180/180**

---

```markdown
You are running the **prove-interview** skill for Signal.

**Topic**: {TOPIC}
**Signal**: {SIGNAL}
**Date**: {DATE}

Simulate a stakeholder and customer interview series using persona-driven methodology.
The interview is a simulation — not real, but grounded in each persona's documented
knowledge, role-specific concerns, and plausible domain behavior.

Output artifact: `simulations/prove/investigations/{topic}-interview-{date}.md`

---

## COMPLIANCE INFRASTRUCTURE

### COLUMN POLICY

Named compliance artifact for Evidence Pull table column requirements. Each failure
condition names what is absent and which criterion is violated by ID. Column additions
are additive — they do not discharge any existing required column under any circumstance.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Quote present but Rationale absent | Interpretive signal context — a confidence score without accompanying rationale cannot be evaluated for basis | FAILS C-10, C-16 |
| Rationale present but Quote absent | Source turn verification — any addition that displaces Quote violates non-substitutability regardless of descriptive value | FAILS C-14, C-16 |
| Any added column displaces Quote or Rationale from any row | Non-substitutability — unconditional; architectural column additions are additive, not substitutive | FAILS C-16 |
| Switch Cost column added to Inertia Verdict Matrix | Additive supplementation — Switch Cost supplements Evidence Pull without displacing Quote or Rationale from any Evidence Pull row; C-16 violations in Evidence Pull tables are independent of C-22 status regardless of the COLUMN POLICY block's presence | Additive rule — no violation; independent C-16 enforcement still applies |
| Quote + Confidence present, Rationale absent | Interpretive basis for confidence rating | FAILS C-10, C-16 |
| Rationale + Confidence present, Quote absent | Source turn verification | FAILS C-14, C-16 |

### DISPOSITION REQUIREMENT

Named compliance artifact for roster disposition label requirements. Per-subject labels
must appear in the roster before any transcript begins — not as synthesis conclusions.
The roster is the structural pre-interview declaration; synthesis characterization after
transcripts fails C-17 regardless of accuracy.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Roster entry with no Disposition value | Per-subject stance declaration before interview transcript — absence on any single entry fails the criterion | FAILS C-17 |
| SKEPTIC absent from roster | Skeptic voice grounded in role-specific resistance — generic change-aversion without role grounding fails C-05 regardless of SKEPTIC label | FAILS C-11, C-17 |
| CHAMPION absent from roster | Advocate voice grounded in role-specific opportunity | FAILS C-11, C-17 |
| CHAMPION declared before SKEPTIC in roster order | Skeptic-first ordering — SKEPTIC must be S-01, CHAMPION must be S-02; this is not cosmetic | FAILS C-18 |
| SKEPTIC-first roster present but Arc Signal uses symmetric two-voice comparison | Prior-signal framing — Arc Signal synthesis must derive from skeptic resistance as epistemic prior, not equal-weight comparison between two voices | FAILS C-18 |
| SKEPTIC-first roster present but Arc Signal framing does not name S-01 as the prior signal | Skeptic-as-prior derivation — "prior signal (SKEPTIC S-01)" framing required in Arc Signal | FAILS C-18 |

### ARC SIGNAL POLICY

Named compliance artifact for the C-23/C-24 chain. Parallel to COLUMN POLICY and
DISPOSITION REQUIREMENT. These conditions are declared as named entries so that
per-factor friction failures are structurally visible during output review rather than
requiring criterion text inspection. Condition (2) is the key discriminating entry:
prose that correctly characterizes switching friction magnitude without tracing it to
a named Incumbent Coupling Table row is the most common failure mode at the
C-23 PARTIAL/PASS boundary. It must be a declared named condition — not implied.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|-----------------------|
| Per-factor friction claim absent from Arc Signal entirely | Named coupling factor from Incumbent Coupling Table in synthesis narrative | FAILS C-23 |
| Friction magnitude present in Arc Signal but coupling factor not cited by its exact Incumbent Coupling Table row name | Coupling factor row name — magnitude-without-name is the PARTIAL discriminator: prose at correct magnitude without row name citation = PARTIAL regardless of how accurately the magnitude is described; the row name is the provenance link | C-23 PARTIAL |
| Arc Signal rendered in prose form without tabular structure | Three-column table with Coupling Factor / Friction Magnitude / Inertia Component headers; prose form satisfies C-23 but fails C-24 regardless of per-factor condition accuracy | FAILS C-24 |
| Arc Signal table present but fewer than three required column headers from the set {Coupling Factor, Friction Magnitude, Inertia Component} | One or more column headers absent or unlabeled; two-of-three-column table = PARTIAL structural form | C-24 PARTIAL |

---

## HUMAN SUBJECTS ROSTER

S-00 is the Incumbent. S-00 is declared at position zero in the roster — before S-01 and
S-02. S-00 appears first in transcript order. This structural ordering is the provenance
guarantee for the C-23/C-24 Arc Signal chain: the Incumbent Coupling Table (populated
from S-00) is structurally locked before any human-subject interview begins, so Arc Signal
table row citations of coupling factor names are provenance-verified by construction rather
than by authorial discipline.

| ID | Role-Title | Domain | Disposition |
|----|-----------|--------|-------------|
| S-00 | [Incumbent — existing tool, vendor, or practice being evaluated for displacement] | [Domain] | INCUMBENT — S-00 position-zero; first in transcript order; switching-cost baseline from which Incumbent Coupling Table is drawn |
| S-01 | [Skeptic role — specific enough that vocabulary and resistance framing are predictable] | [Domain] | SKEPTIC — role-grounded resistance; generic change-aversion without domain basis fails C-05 |
| S-02 | [Champion role — specific enough that vocabulary and advocacy framing are predictable] | [Domain] | CHAMPION — role-grounded advocacy; enthusiasm without domain basis fails C-05 |

**S-00 STRUCTURAL CONSTRAINT:** S-00 is position zero. The Incumbent Coupling Table is
completed during Step 1. No S-01 or S-02 content appears in the output before the
Incumbent Coupling Table is written and complete. This makes the lifecycle guarantee
structural — the coupling factor row names cited by the Arc Signal table already existed
when the Arc Signal was authored.

**SKEPTIC-FIRST REQUIREMENT:** This is not cosmetic. S-01 is the prior signal. The Arc Signal
synthesis derives from skeptic resistance as the epistemic prior, not from a symmetric
comparison between S-01 and S-02. CHAMPION-first ordering fails C-18 at the roster level
before any transcript is examined.

---

## STEP 0 — CONTEXT

Read any prior signal artifacts for this topic:
`simulations/{namespace}/.../{topic}-*-{date}.md`

Note signals already gathered. State the topic, the feature or decision under
investigation, and the question this interview series is designed to answer.

---

## STEP 1 — INCUMBENT BASELINE (S-00)

**S-00 appears first in the output.** S-00 is not a human stakeholder — it is the
existing system, tool, vendor, workflow, or practice that would be displaced or
supplemented by the feature under investigation.

### Prior Knowledge Block — S-00

Before the transcript begins, declare:
- **Identity**: Name the incumbent specifically — enough specificity that coupling factors can be named
- **Current-practice anchor**: What it provides today that would be displaced by the feature
- **Domain footprint**: Workflows, integrations, user habits that depend on it
- **Switching-cost basis**: Categories of friction switching would entail (data migration, retraining, contract lock-in, workflow disruption, integration replacement, etc.)

### S-00 Transcript — Current-Practice Baseline

Q1 is the current-practice anchor: ask what the incumbent does today, before any feature
is introduced. Q1 establishes the behavioral baseline the Incumbent Coupling Table draws from.
Q2 probes one specific coupling dimension raised in Q1.
Q3 asks what would be lost if displaced — names specific consequences, not generic value.
Minimum 3 turns.

```
**INTERVIEWER:** [Question — Q1 opens with neutral current-practice framing]
**S-00 (INCUMBENT):** [Answer grounded in actual incumbent capability domain. References
specific features, integrations, or behaviors the incumbent is known for. Not generic
value claims. Vocabulary and framing match what a structured account of this incumbent
would actually surface.]
```

**Surprise (one sentence):** [One specific coupling dimension the Q1-Q3 sequence did not
anticipate. Label it explicitly.]

### Incumbent Coupling Table

Extract all switching-cost coupling factors revealed by the S-00 transcript.
This table is the structural source for the Switch Cost column in the Inertia Verdict
Matrix and for the Coupling Factor column in the Arc Signal table.

| Coupling Factor | Switching-Cost Rating | Basis (S-00 turn reference) |
|-----------------|----------------------|-----------------------------|
| [Specific named factor — workflow dependency, data format lock-in, integration contract, retraining requirement, etc.] | HIGH / MEDIUM / LOW | [S-00 turn that grounds this rating — not paraphrased] |

Each factor must be named specifically. This exact name is what the Arc Signal table
rows must cite in their Coupling Factor column. Generic "switching cost" or "switching
friction" as a coupling factor name = fails Arc Signal provenance requirement.
Minimum one factor.

**STEP 1 GATE:** Incumbent Coupling Table is now structurally locked. Per-factor names
and switching-cost ratings are final. S-01 and S-02 transcripts that follow cannot change
these values. The Arc Signal table draws from this table — coupling factor citations in
Arc Signal rows are provenance-verified from this point.

### Evidence Pull — S-00

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim S-00 turn — exact words, not paraphrased] | [Why does this signal matter to the topic decision? Not a restatement of the quote. Answer the question: what does this signal tell the decision-maker?] | HIGH / MEDIUM / LOW | [coupling factor / switching barrier / integration dependency / workflow anchor] |

Apply COLUMN POLICY to every row before filing. If a row is missing Quote or Rationale,
name the criterion violated (FAILS C-10, C-16 or FAILS C-14, C-16) before continuing.

---

## STEP 2 — HUMAN SUBJECT INTERVIEWS

S-01 (SKEPTIC) is interviewed first. S-02 (CHAMPION) is interviewed second.
S-00 content from Step 1 is structurally locked. These subjects are human stakeholders
with roles, concerns, and domain knowledge that shape how they engage with the feature.

### Prior Knowledge Block (per subject)

Before the transcript begins, declare:
- **Role and title**: Specific enough that vocabulary and concerns are predictable
- **Domain background**: What they know about the incumbent and the proposed feature
- **Knowledge gaps**: Blind spots that may affect their signal
- **Primary concern**: The single thing they care most about in this decision
- **Current-practice anchor field**: What they do today that intersects with this feature — the Q1 question draws from this

### Interview Transcript (per subject)

Q1 must be a neutral current-practice question: ask what the subject does today, before
any feature is introduced. The Q1 answer establishes the behavioral baseline for
subsequent feature-reaction contrast. A subject whose Q1 answer ignores their declared
current-practice background is a C-05 violation — the Q1 anchor makes this visible.

Q2 probes the named stance from the Prior Knowledge Block.
Q3 names a specific claim from a prior subject — "You said X in the last interview" or
"The incumbent noted Y." Do not refer to prior subjects generically.
Minimum 3 turns.

```
**INTERVIEWER:** [Question]
**[SUBJECT LABEL]:** [Persona-voice answer — vocabulary, concerns, and framing match the
declared role. Generic AI-sounding answers that could belong to any persona fail C-03.
Answers reference role-specific constraints, domain knowledge, or concerns from the
Prior Knowledge Block. "Change is hard" as the sole resistance framing for a SKEPTIC
fails C-05 regardless of SKEPTIC label.]
```

**Surprise (one sentence):** [Something the interviewer's questions did not anticipate.
Label it explicitly. Describe why it is unexpected given the Prior Knowledge Block.]

### Evidence Pull (per subject)

| Quote | Rationale | Confidence | Signal |
|-------|-----------|------------|--------|
| [Verbatim subject turn — exact words; "not paraphrased" is insufficient — include the actual quoted text] | [Why does this signal matter to the topic decision? Rationale must answer: what does this tell the decision-maker about whether to proceed? Not a restatement of the quote.] | HIGH / MEDIUM / LOW | [insight / concern / requirement / contradiction / signal type] |

Apply COLUMN POLICY to every row. Pre-synthesis gate: if any row is missing Quote or
Rationale, name the criterion violated before proceeding to synthesis.

---

## STEP 3 — SYNTHESIS

Do not summarize individual interviews — synthesize across them. If the synthesis
references only one subject, it is not an arc — revise before filing.

### Pattern

One paragraph. The dominant pattern across all subjects — what the signals say together
about the feature's likelihood of adoption, the incumbent's inertia, and the evidential
weight of convergence or contradiction.

### Critical Contradiction Table

Identify the single most significant contradiction between interview subjects.
Name it. Rank it. Explain its evidential weight — what it confirms, undermines, or
leaves unresolved. A synthesis that lists contradictions without ranking them fails.

| Contradiction | Side A (HE-# verbatim quote) | Side B (HE-# verbatim quote) | Stakes |
|---------------|------------------------------|------------------------------|--------|
| [Named contradiction — the most evidentially significant; "most significant" must be justified in Stakes] | "[Verbatim quote from one subject — exact words]" | "[Verbatim quote from opposing subject — exact words]" | [What is at risk if this tension persists into implementation — forward-looking, not descriptive] |

Both sides verbatim. Naming the contradiction without quoting both sides leaves the
opposing position asserted without source verification.

### Tension Resolution

One paragraph. Does the evidence resolve the critical contradiction, or does it persist
into implementation risk? What single follow-on signal (interview, prototype test,
or archival search) would resolve the most significant remaining tension?

### Inertia Verdict Matrix

| Subject | Verdict | Switch Cost | Rationale |
|---------|---------|-------------|-----------|
| S-01 [Role] | ADOPT / DEFER / RESIST | [Switching-cost assessment sourced from Incumbent Coupling Table — cite the table by name; do not assert switch cost without citing the source table] | [Role-grounded rationale connecting verdict to role-specific concerns and domain knowledge] |
| S-02 [Role] | ADOPT / DEFER / RESIST | [Switching-cost assessment sourced from Incumbent Coupling Table — cite the table by name] | [Role-grounded rationale] |

### Arc Signal

**Prior signal (SKEPTIC S-01):** "[Verbatim quote from S-01's most resistance-anchored turn — the turn that best captures the epistemic prior]"
**Subsequent evidence (CHAMPION S-02):** "[Verbatim quote from S-02's most confirmation-anchored or overturn turn — the evidence against the prior]"

This is not a symmetric comparison between two equal voices. S-01 resistance is the
epistemic prior; S-02 evidence either confirms the prior (strong incumbent inertia —
skeptic concern validated) or overturns it (weak incumbent inertia — feature has
genuine displacement potential). The arc derives from this asymmetry.

**Incumbent Switching Friction:**

Render as a structured table. This is the C-24 structural ceiling for per-factor
coupling propagation. Each coupling factor from the Incumbent Coupling Table occupies
its own row. Each row independently satisfies all three per-factor conditions without
sentence-level ambiguity. Column headers must be exactly as stated.

| Coupling Factor | Friction Magnitude | Inertia Component |
|-----------------|-------------------|-------------------|
| [Exact row name from Incumbent Coupling Table — not paraphrased, not generalized] | [Switching-cost rating from coupling table: HIGH / MEDIUM / LOW — from the table rating, not re-assessed here] | [confirms / moderates / overturns the inertia signal — one sentence explaining whether this friction level makes the skeptic prior stronger or weaker] |

Rules:
- One row per coupling factor from the Incumbent Coupling Table
- Do not merge two coupling factors into one row
- Do not substitute prose for this table — see ARC SIGNAL POLICY, condition (3)
- Do not add a row for a coupling factor not in the Incumbent Coupling Table
- Coupling factor name must match the exact row name in the Incumbent Coupling Table —
  paraphrasing the factor name = magnitude-without-name-match, see ARC SIGNAL POLICY condition (2)

**Dominant arc:** [Convergence despite skeptic resistance — strong signal: skeptic
identified a real concern, champion evidence overturns the specific friction claim; /
Skeptic resistance unconfirmed — insufficient evidence: champion validation does not
address the specific coupling factor the skeptic named; /
Skeptic and champion both surface high switching cost — cautionary signal: convergence
on friction rather than adoption; revisit feature framing]

### Prior Assumption Revisited

What did the interviewer assume before running this series? What did the interviews
confirm? What did they overturn? What would the next interview session investigate
differently given what the signals revealed? One paragraph.

---

## OUTPUT FORMAT

Write to: `simulations/prove/investigations/{topic}-interview-{date}.md`

Pre-filing checklist (verify each before writing the file):

**Structural ordering (C-25 check):**
- S-00 declared as S-00 in roster (position-zero roster declaration present)
- S-00 transcript and Incumbent Coupling Table appear before S-01 transcript in output
- Both conditions must be satisfied simultaneously; one without the other = C-25 PARTIAL

**Evidence Pull compliance (C-16 check):**
- Every Evidence Pull row across all subjects: Quote + Rationale + Confidence + Signal
- No row uses Quote as a substitute for Rationale or vice versa
- If any row is missing a required column, name the criterion violated

**Roster compliance (C-17/C-18 check):**
- All human subjects (S-01, S-02) have Disposition labels in the roster before transcripts
- SKEPTIC = S-01 (first human subject), CHAMPION = S-02 (second)
- Arc Signal is framed from skeptic-as-prior, not symmetric comparison

**Arc Signal table compliance (C-24 check — see ARC SIGNAL POLICY):**
- Table present with exactly three column headers: Coupling Factor / Friction Magnitude / Inertia Component
- One row per coupling factor from Incumbent Coupling Table
- Each row: coupling factor named by exact table row name (not paraphrased)
- Each row: friction magnitude from coupling table rating (not re-assessed)
- Each row: inertia component explains confirms / moderates / overturns in one sentence
- If Arc Signal is prose without this table: FAILS C-24 (see ARC SIGNAL POLICY condition 3)
- If table has only two columns: C-24 PARTIAL (see ARC SIGNAL POLICY condition 4)

**Inertia Verdict Matrix (C-22 check):**
- Switch Cost column entries cite Incumbent Coupling Table by name per entry
- Coexistence without attribution does not satisfy sourcing requirement

**Critical Contradiction (C-15 check):**
- Both sides sourced verbatim — one quote per position
- Contradiction ranked by evidential weight (not merely enumerated)
```

---

## Summary Table

| Variation | Axis | C-24 | C-25 | C-26 | Predicted Total |
|-----------|------|------|------|------|-----------------|
| V-01 | Role Sequence | FAIL (prose Arc Signal) | PASS (S-00 roster + transcript-first) | FAIL | 170/180 |
| V-02 | Output Format | PASS (3-col table) | FAIL (prose gate, no S-00 declaration) | FAIL | 170/180 |
| V-03 | Lifecycle Emphasis | FAIL (prose Arc Signal) | FAIL (prose gate) | PASS (ARC SIGNAL POLICY with condition 2) | 170/180 |
| V-04 | C-24 + C-25 | PASS | PASS | FAIL | 175/180 |
| V-05 | C-24 + C-25 + C-26 | PASS | PASS | PASS | **180/180** |

**Discriminating design decisions:**

- V-01 vs V-02 isolates the C-25/C-24 split: both score 170 but through different structural mechanisms — ordering vs. format. Neither cross-contaminates the other's criterion.

- V-03 is the only variation where C-26 PASS coexists with C-24 FAIL. This verifies that C-26 (compliance block for the chain) is independently gradable from C-24 (tabular Arc Signal format) — the ARC SIGNAL POLICY block can declare C-24's failure condition without itself satisfying C-24.

- V-04 vs V-05 isolates C-26: everything else equal, V-04 shows what the ceiling looks like before the compliance infrastructure for the C-23/C-24 chain is named — structurally correct but not self-documenting.

- V-05 closes the loop: S-00 structural ordering proves per-factor names existed before human interviews ran; the tabular Arc Signal proves each row satisfies all three C-23 conditions independently; the ARC SIGNAL POLICY block names the magnitude-without-name discriminator so it is structurally visible during review rather than requiring criterion text inspection.
