Written to `simulations/quest/variations/prove-interview-variations-R6-2026-03-14.md`.

---

## Round 6 Variations — prove-interview (R6)

**Ceiling: 155 · 5 variations · targeting C-20 + C-21**

### Variation Map

| V | Axis | C-20 | C-21 | Absent | Predicted |
|---|------|------|------|--------|-----------|
| V-01 | Role sequence — prose + partial-compliance variants | YES | NO | C-21 | 150/155 |
| V-02 | Output format — tabular, no 6th DISPOSITION row | PARTIAL | YES | C-20 full | ~150/155 |
| V-03 | Both fixes, minimal | YES | YES | — | 155/155 |
| V-04 | Phrasing register (imperative enforcement) | YES | YES | — | 155/155 |
| V-05 | All five axes + maximum enforcement | YES | YES | — | 155/155 |

### Key structural changes

**C-20** — requires two things simultaneously:
- **DISPOSITION** 6th condition (new): `"SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18"` — the partial-compliance case where structure is correct but framing is absent
- **COLUMN POLICY** explicit partial-compliance framing: `"Quote present but Rationale absent: FAILS C-10, FAILS C-16"` (was implicitly present in R5 V-03+ as "Table has Quote + Confidence but no Rationale"; V-01/V-03+ make it explicit)

**C-21** — both blocks in three-column tabular format (`Condition | What is absent | Criterion(s) violated`). V-02 had this from R5 V-04 ancestry; V-03+ are the first to combine it with C-20.

### Isolation logic

- V-01 vs V-02: tests C-20 and C-21 independently. If both score ~150, each is satisfiable without the other.
- V-02 is C-20 PARTIAL (not FAIL) — COLUMN POLICY table row 1 ("Quote + Confidence, no Rationale") implicitly covers the partial-compliance condition; DISPOSITION lacks the 6th row. Expected ~150 (C-21 full 5pts, C-20 partial 2-3pts).
- V-03 is the minimal proof: if 155/155, no additional axes needed.
- V-04/V-05 confirm register and structural variation are scoring-neutral.
ently satisfiable. C-20 PARTIAL expected because COLUMN POLICY table rows implicitly cover partial-compliance (Quote present, Rationale absent = row 1 in table), but DISPOSITION lacks the 6th row.
V-03: minimal combination. If 155, no further axes required.

### Key structural changes that fix C-20

6th DISPOSITION REQUIREMENT condition (prose form):
```
R5 V-03/V-04: 5 conditions — missing the partial-compliance case

R6 fix: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18
  (C-18 requires both structural ordering AND skeptic-prior Arc framing simultaneously;
  structural ordering alone satisfies only half the criterion)"
```

6th DISPOSITION REQUIREMENT condition (tabular form):
```
| SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18 (requires both structural ordering AND skeptic-prior framing simultaneously) |
```

COLUMN POLICY partial-compliance explicit framing (V-01 prose, sectioned):
```
Partial-compliance failure conditions (one column present, complementary column absent):
- Quote present but Rationale absent: FAILS C-10, FAILS C-16
- Rationale present but Quote absent: FAILS C-14, FAILS C-16
```

COLUMN POLICY partial-compliance (V-03+ tabular, row framing):
```
| Quote present but Rationale absent | Interpretive rationale per row | C-10, C-16 |
| Rationale present but Quote absent | Verbatim SUBJECT source turn | C-14, C-16 |
```

### Key structural changes that fix C-21

Both compliance blocks must use three-column tabular format. R5 V-04 already demonstrated this format satisfies C-19 itemized requirement equivalently to prose bullets. R6 promotes the format as its own structural ceiling.

---

## V-01: Role Sequence — C-20 Only (Prose Compliance Blocks)

**Axis:** Role sequence (SKEPTIC-first) with C-20 partial-compliance variants in prose compliance blocks.
**Hypothesis:** Adding the 6th DISPOSITION condition (partial-compliance: SKEPTIC-first without skeptic-prior framing) and explicitly labeling partial-compliance conditions in COLUMN POLICY achieves C-20 PASS independently of tabular format. C-21 absent by design (prose blocks). C-18 and C-19 present. Target: 150/155.

```
PROVE-INTERVIEW PROMPT — V-01 (C-20 only; prose compliance blocks; C-21 absent)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 155. Target: 150 (C-20 present via prose blocks; C-21 absent by design).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 0: ROSTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject 0 — Incumbent (AI)

| Field | Value |
|-------|-------|
| Role | [Incumbent role — internal domain expert] |
| Knowledge basis | [What the incumbent knows about TOPIC from prior work] |
| Blind spots | [What the incumbent cannot see due to proximity] |
| Expected bias | [Direction the incumbent will lean] |

Human Subjects — Interview Roster

SKEPTIC-FIRST REQUIREMENT: S-01 must be the SKEPTIC. S-02 must be the CHAMPION. The SKEPTIC
interview establishes resistance as the prior signal. The CHAMPION interview is the evidence
against or for that prior. Inverting this order removes the causal structure of the arc.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value (SKEPTIC or
CHAMPION) declared before any transcript begins. Inferred disposition is not sufficient. Both
structural ordering (S-01 = SKEPTIC) and Arc Signal framing (skeptic-prior) are required
simultaneously for C-18 compliance — either condition alone is insufficient.

Per-condition failure statements:
- No SKEPTIC label in roster: FAILS C-11 (Disposition arc structured — arc requires both poles
  declared) and FAILS C-17 (Roster-level disposition labels — every human subject requires an
  explicit per-subject label before transcripts begin)
- No CHAMPION label in roster: FAILS C-11 (Disposition arc structured) and FAILS C-17
  (Roster-level disposition labels — every human subject requires an explicit per-subject label
  before transcripts begin)
- Roster entry with no Disposition column value: FAILS C-17 (every human subject requires
  explicit per-subject label before transcripts begin — absence on any single entry fails the
  criterion regardless of whether other entries have labels)
- Disposition inferred from synthesis-level arc analysis but absent from this table: FAILS C-17
  (C-11 is the floor — arc may appear in synthesis; C-17 is the ceiling — per-subject label
  must appear at roster level before any transcript begins)
- CHAMPION declared as S-01: FAILS C-18 (Skeptic-first roster ordering — SKEPTIC must appear
  as S-01 to establish resistance as the prior signal)
- SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18 (C-18
  requires both structural ordering AND skeptic-prior Arc framing simultaneously; structural
  ordering alone satisfies only half the criterion — skeptic-prior framing must derive from
  the structural ordering to complete compliance)

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
Quote = verbatim subject turn (not summarized, not paraphrased). Rationale = interpretive
statement explaining why this signal matters (not a restatement of the quote). Confidence =
rated 1-5. All four columns must coexist simultaneously in every row.

Full-absence failure conditions:
- Table has Confidence only — neither Quote nor Rationale present: FAILS C-10 (Evidence
  confidence rated — no rationale basis), FAILS C-14 (Arc claims quote-anchored — no source
  grounding), and FAILS C-16 (Evidence columns non-substitutable — both base columns absent)

Partial-compliance failure conditions (one column present, complementary column absent):
- Quote present but Rationale absent: FAILS C-10 (Evidence confidence rated — confidence score
  without accompanying rationale cannot be evaluated for basis) and FAILS C-16 (Evidence
  columns non-substitutable — Quote does not substitute for Rationale; both must coexist
  simultaneously in the same row)
- Rationale present but Quote absent: FAILS C-14 (Arc claims quote-anchored — rationale
  claims must be grounded in verbatim subject language) and FAILS C-16 (Evidence columns
  non-substitutable — Rationale does not substitute for Quote; both must coexist
  simultaneously in the same row)

Interpretive quality failure conditions:
- Rationale restates the Quote: FAILS C-10 (Rationale must answer "why does this signal
  matter to the feature decision?" — paraphrasing the quote does not constitute interpretation)
- Architectural addition placed in position that removes Quote or Rationale: FAILS C-16
  (adding a column such as Phase, Theme, or Category is permitted only if it supplements the
  four required columns; any addition that displaces Quote or Rationale violates the
  non-substitutability rule regardless of the addition's descriptive value)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW (AI-conducted, prior to human sessions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete before transcript):
- Current assumption about TOPIC: [state explicitly — this will be revisited in Step 3]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition — specific, not generic]

Transcript (minimum 3 turns — Q from interviewer, A from incumbent):

Q1: [Opening question probing incumbent's core assumption about TOPIC]
A1: [Incumbent response — full, role-grounded]

Q2: [Follow-up targeting the named blind spot from roster]
A2: [Incumbent response — reveals internal tension or confirms assumption]

Q3: [Pressure question — what evidence would change their position?]
A3: [Incumbent response — surfaces the threshold condition]

Surprise (one sentence): [What emerged in the incumbent interview that was not anticipated?]

Incumbent Evidence Pull:

| IE-# | Claim | Quote | Confidence | Rationale |
|------|-------|-------|------------|-----------|
| IE-1 | [Claim extracted from incumbent] | "[Verbatim quote from A1, A2, or A3]" | [1-5] | [Why this claim matters as signal] |
| IE-2 | [Second claim] | "[Verbatim quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG (derived from incumbent evidence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension between two incumbent claims or between claim and external signal] | IE-1: "[exact quote matching IE table]" |
| T-2 | [Second tension] | IE-2: "[exact quote matching IE table]" |

Tension source quotes must match the Quote column of the referenced IE row exactly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — SKEPTIC-FIRST SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Interview subjects in declared roster order: S-01 (SKEPTIC) before S-02 (CHAMPION).
The SKEPTIC interview establishes the prior signal. Do not reorder.

--- S-01 (SKEPTIC) ---

Prior knowledge block:
- What S-01 knows about TOPIC: [domain-grounded]
- S-01's expected resistance point: [named before transcript]
- What would shift S-01: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing of TOPIC without leading toward resistance]
A1: [S-01 response — role-grounded resistance or concern]

Q2: [Probe the specific resistance point named above]
A2: [S-01 response — deepens or qualifies resistance]

Q3: [Contrast question — reference incumbent assumption from Step 1 and ask S-01 to react]
Q3 contrast note: This Q3 contrast references the incumbent assumption stated in Step 1.
A3: [S-01 response — direct tension with incumbent position]

Surprise (one sentence): [What S-01 said that was not anticipated from their declared disposition?]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal from S-01] | "[Verbatim S-01 quote]" | [1-5] | [Why this signal matters] |
| HE-2 | [Second signal] | "[Verbatim S-01 quote]" | [1-5] | [Interpretive rationale] |

--- S-02 (CHAMPION) ---

Prior knowledge block:
- What S-02 knows about TOPIC: [domain-grounded]
- S-02's expected advocacy point: [named before transcript]
- What would complicate S-02's position: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing of TOPIC without leading toward advocacy]
A1: [S-02 response — role-grounded advocacy or enthusiasm]

Q2: [Probe the specific advocacy point named above]
A2: [S-02 response — deepens or qualifies advocacy]

Q3: [Contrast question — reference a specific claim from S-01's transcript above]
Q3 contrast note: This Q3 contrast references a named specific claim from S-01's transcript.
A3: [S-02 response — direct engagement with the named SKEPTIC claim]

Surprise (one sentence): [What S-02 said that was not anticipated from their declared disposition?]

S-02 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal from S-02] | "[Verbatim S-02 quote]" | [1-5] | [Why this signal matters] |
| HE-4 | [Second signal] | "[Verbatim S-02 quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-synthesis gate: All HE-# rows must contain Signal, Quote, Confidence, and Rationale per
Column Policy. Do not proceed if any row is missing any column.

Pattern (2-3 sentences): [What pattern emerges across incumbent + S-01 + S-02 evidence?]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent claim vs. subject claim — named specifically] | IE-#, HE-# | [Stakes if unresolved] |
| [S-01 SKEPTIC claim vs. S-02 CHAMPION claim] | HE-#, HE-# | [Stakes] |

Tension Resolution:
T-1: [How human interviews resolved or deepened T-1]
T-2: [How human interviews resolved or deepened T-2]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1] | [HE-# or IE-# reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 2] | [HE-# or IE-# reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 3] | [HE-# or IE-# reference] | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing — required):
Skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence.

Prior signal (SKEPTIC S-01): [Role-grounded resistance established by S-01 — what they
resisted and why, stated as the prior that CHAMPION must respond to]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned
relative to the SKEPTIC prior stated above]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence naming what SKEPTIC
established and how CHAMPION responded to it]

Prior Assumption Revisited:
Before: [Restate incumbent assumption from Step 1 exactly]
After: [Revised assumption given all evidence]
Delta: [One sentence naming what changed and why]
```

---

## V-02: Output Format — C-21 Only (Tabular Blocks, No Partial-Compliance 6th Row)

**Axis:** Output format (three-column tabular compliance blocks). C-21 present. C-20 absent by design — DISPOSITION table has 5 rows (omits the partial-compliance 6th condition). COLUMN POLICY table rows implicitly cover partial-compliance scenarios (C-20 PARTIAL expected for that block).
**Hypothesis:** Three-column tabular format for both compliance blocks satisfies C-21 independently of C-20. DISPOSITION missing 6th row → C-20 fails for DISPOSITION block → C-20 PARTIAL overall. C-21 PASS because both blocks are tabular. C-18 and C-19 present. Target: ~150/155.

```
PROVE-INTERVIEW PROMPT — V-02 (C-21 only; tabular blocks; C-20 absent — no 6th DISPOSITION row)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 155. Target: 150 (C-21 present via tabular blocks; C-20 absent by design — DISPOSITION
table has 5 rows, partial-compliance 6th condition omitted).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 0: ROSTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject 0 — Incumbent (AI)

| Field | Value |
|-------|-------|
| Role | [Incumbent role] |
| Knowledge basis | [Prior knowledge basis] |
| Blind spots | [Named blind spots] |
| Expected bias | [Direction] |

Human Subjects — Interview Roster

SKEPTIC-FIRST: S-01 must be SKEPTIC. S-02 must be CHAMPION.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value declared
before any transcript begins. Inferred disposition is not sufficient.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| No SKEPTIC label in roster | Explicit skeptic disposition before any transcript | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| No CHAMPION label in roster | Explicit advocate disposition before any transcript | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| Roster entry with no Disposition column value | Per-subject disposition label | C-17 (every human subject requires explicit per-subject label before transcripts begin) |
| Disposition inferred from synthesis only | Roster-level declaration before transcripts | C-17 (C-11 floor — arc in synthesis; C-17 ceiling — per-subject label at roster level) |
| CHAMPION declared as S-01 | SKEPTIC-first structural ordering | C-18 (Skeptic-first roster ordering — SKEPTIC must appear as S-01) |

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
All four must coexist simultaneously. No column substitutes for another.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Quote + Confidence present, no Rationale | Interpretive rationale per row | C-10 (Evidence confidence rated), C-16 (Evidence columns non-substitutable) |
| Rationale + Confidence present, no Quote | Verbatim source turn | C-14 (Arc claims quote-anchored), C-16 (Evidence columns non-substitutable) |
| Confidence only — neither Quote nor Rationale | Both base columns | C-10, C-14, C-16 |
| Rationale restates Quote | Interpretive content distinct from quote | C-10 (Rationale must answer "why does this signal matter?") |
| Architectural column replaces Quote or Rationale | Non-substitutable base column | C-16 (Phase/Theme/Category columns do not substitute for Quote or Rationale) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block:
- Current assumption about TOPIC: [state explicitly]
- Confidence: [1-5]
- What would change this assumption: [named condition]

Transcript (minimum 3 turns):

Q1: [Opening question probing incumbent's core assumption]
A1: [Incumbent response]

Q2: [Follow-up targeting blind spot]
A2: [Incumbent response]

Q3: [Pressure question — what evidence would change their position?]
A3: [Incumbent response]

Surprise (one sentence): [Unanticipated emergence from incumbent interview]

Incumbent Evidence Pull:

| IE-# | Claim | Quote | Confidence | Rationale |
|------|-------|-------|------------|-----------|
| IE-1 | [Claim] | "[Verbatim quote]" | [1-5] | [Why this matters] |
| IE-2 | [Claim] | "[Verbatim quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension] | IE-1: "[exact quote matching IE table]" |
| T-2 | [Tension] | IE-2: "[exact quote matching IE table]" |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — SKEPTIC-FIRST SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Interview subjects in declared roster order: S-01 (SKEPTIC) first, S-02 (CHAMPION) second.

--- S-01 (SKEPTIC) ---

Prior knowledge block:
- What S-01 knows: [domain-grounded]
- Expected resistance point: [named]
- What would shift S-01: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing]
A1: [S-01 response — resistance grounded]

Q2: [Probe resistance point]
A2: [S-01 response]

Q3: [Contrast with incumbent assumption]
Q3 contrast note: References incumbent assumption from Step 1.
A3: [S-01 response]

Surprise (one sentence): [Unanticipated from S-01]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal] | "[Verbatim S-01 quote]" | [1-5] | [Why this matters] |
| HE-2 | [Signal] | "[Verbatim S-01 quote]" | [1-5] | [Interpretive rationale] |

--- S-02 (CHAMPION) ---

Prior knowledge block:
- What S-02 knows: [domain-grounded]
- Expected advocacy point: [named]
- What would complicate S-02: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing]
A1: [S-02 response — advocacy grounded]

Q2: [Probe advocacy point]
A2: [S-02 response]

Q3: [Contrast with S-01 resistance]
Q3 contrast note: References a specific claim from S-01's transcript above.
A3: [S-02 response]

Surprise (one sentence): [Unanticipated from S-02]

S-02 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal] | "[Verbatim S-02 quote]" | [1-5] | [Why this matters] |
| HE-4 | [Signal] | "[Verbatim S-02 quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-synthesis gate: All HE-# rows must contain Signal, Quote, Confidence, and Rationale.

Pattern (2-3 sentences): [Pattern across all evidence]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent vs. subject claim] | IE-#, HE-# | [Stakes] |
| [S-01 vs. S-02] | HE-#, HE-# | [Stakes] |

Tension Resolution:
T-1: [Resolution or deepening]
T-2: [Resolution or deepening]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1] | [Reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 2] | [Reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 3] | [Reference] | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing):
Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence.

Prior signal (SKEPTIC S-01): [What S-01 resisted and why]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence]

Prior Assumption Revisited:
Before: [Exact restatement of incumbent assumption]
After: [Revised assumption]
Delta: [What changed and why]
```

---

## V-03: Both Fixes, Minimal (C-20 + C-21, tabular blocks with partial-compliance)

**Axis:** Both C-20 and C-21 applied. Minimal delta from R5 V-04 (add 6th DISPOSITION row + explicit partial-compliance framing in COLUMN POLICY rows).
**Hypothesis:** Three-column tabular blocks (C-21) with 6th DISPOSITION row and partial-compliance-explicit COLUMN POLICY rows (C-20) achieves 155/155. No other axis changes required.

```
PROVE-INTERVIEW PROMPT — V-03 (C-20 + C-21; tabular blocks with partial-compliance variants; minimal combination)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 155. Target: 155 (both C-20 and C-21 present — tabular compliance blocks with
partial-compliance failure variants in both blocks).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 0: ROSTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject 0 — Incumbent (AI)

| Field | Value |
|-------|-------|
| Role | [Incumbent role] |
| Knowledge basis | [Prior knowledge basis] |
| Blind spots | [Named blind spots] |
| Expected bias | [Direction] |

Human Subjects — Interview Roster

SKEPTIC-FIRST: S-01 must be SKEPTIC. S-02 must be CHAMPION.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value declared
before any transcript begins. Inferred disposition is not sufficient.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| No SKEPTIC label in roster | Explicit skeptic disposition before any transcript | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| No CHAMPION label in roster | Explicit advocate disposition before any transcript | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| Roster entry with no Disposition column value | Per-subject disposition label | C-17 (every human subject requires explicit per-subject label before transcripts begin) |
| Disposition inferred from synthesis only | Roster-level declaration before transcripts | C-17 (C-11 floor — arc in synthesis; C-17 ceiling — per-subject label at roster level) |
| CHAMPION declared as S-01 | SKEPTIC-first structural ordering | C-18 (Skeptic-first roster ordering — SKEPTIC must appear as S-01) |
| SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18 (C-18 requires both structural ordering AND skeptic-prior framing simultaneously — structural ordering alone satisfies only half the criterion) |

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
All four must coexist simultaneously. No column substitutes for another.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Quote present but Rationale absent | Interpretive rationale per row | C-10 (Evidence confidence rated — confidence without interpretive basis), C-16 (Evidence columns non-substitutable) |
| Rationale present but Quote absent | Verbatim SUBJECT source turn | C-14 (Arc claims quote-anchored), C-16 (Evidence columns non-substitutable) |
| Neither Quote nor Rationale present | Both base columns | C-10, C-14, C-16 |
| Rationale restates Quote | Interpretive content distinct from quote | C-10 (Rationale must answer "why does this signal matter?") |
| Architectural column displaces Quote or Rationale | Non-substitutable base column | C-16 (Phase/Theme/Category columns supplement but do not replace Quote or Rationale) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete before transcript):
- Current assumption about TOPIC: [state explicitly — this will be revisited in Step 3]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition]

Transcript (minimum 3 turns):

Q1: [Opening question probing incumbent's core assumption]
A1: [Incumbent response]

Q2: [Follow-up targeting blind spot]
A2: [Incumbent response]

Q3: [Pressure question — what evidence would change position?]
A3: [Incumbent response]

Surprise (one sentence): [Unanticipated emergence]

Incumbent Evidence Pull:

| IE-# | Claim | Quote | Confidence | Rationale |
|------|-------|-------|------------|-----------|
| IE-1 | [Claim] | "[Verbatim quote]" | [1-5] | [Why this matters] |
| IE-2 | [Claim] | "[Verbatim quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension] | IE-1: "[exact quote matching IE table]" |
| T-2 | [Tension] | IE-2: "[exact quote matching IE table]" |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — SKEPTIC-FIRST SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Interview subjects in declared roster order: S-01 (SKEPTIC) before S-02 (CHAMPION).

--- S-01 (SKEPTIC) ---

Prior knowledge block:
- What S-01 knows: [domain-grounded]
- Expected resistance point: [named]
- What would shift S-01: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing]
A1: [S-01 response — resistance grounded]

Q2: [Probe resistance]
A2: [S-01 response]

Q3: [Contrast with incumbent assumption]
Q3 contrast note: References incumbent assumption from Step 1.
A3: [S-01 response]

Surprise (one sentence): [Unanticipated from S-01]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal] | "[Verbatim S-01 quote]" | [1-5] | [Why this matters] |
| HE-2 | [Signal] | "[Verbatim S-01 quote]" | [1-5] | [Interpretive rationale] |

--- S-02 (CHAMPION) ---

Prior knowledge block:
- What S-02 knows: [domain-grounded]
- Expected advocacy point: [named]
- What would complicate S-02: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing]
A1: [S-02 response — advocacy grounded]

Q2: [Probe advocacy]
A2: [S-02 response]

Q3: [Contrast with S-01 resistance]
Q3 contrast note: References a specific claim from S-01's transcript above.
A3: [S-02 response]

Surprise (one sentence): [Unanticipated from S-02]

S-02 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal] | "[Verbatim S-02 quote]" | [1-5] | [Why this matters] |
| HE-4 | [Signal] | "[Verbatim S-02 quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-synthesis gate: All HE-# rows must contain Signal, Quote, Confidence, and Rationale per
Column Policy. Do not proceed if any row is missing any column.

Pattern (2-3 sentences): [Pattern across all evidence]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent vs. subject claim] | IE-#, HE-# | [Stakes] |
| [S-01 vs. S-02] | HE-#, HE-# | [Stakes] |

Tension Resolution:
T-1: [Resolution or deepening]
T-2: [Resolution or deepening]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1] | [Reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 2] | [Reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 3] | [Reference] | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing):
Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence.

Prior signal (SKEPTIC S-01): [What S-01 resisted and why — stated as the prior]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned
relative to the SKEPTIC prior]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence]

Prior Assumption Revisited:
Before: [Exact restatement of incumbent assumption]
After: [Revised assumption]
Delta: [What changed and why]
```

---

## V-04: Phrasing Register — Imperative Enforcement (C-20 + C-21)

**Axis:** Phrasing register (imperative second-person throughout; phase-gate language explicit at every step boundary).
**Hypothesis:** Imperative enforcement phrasing is register-neutral to scoring — same functional content as V-03 but more directive tone achieves 155/155. Tests whether register affects compliance block interpretation.

```
PROVE-INTERVIEW PROMPT — V-04 (C-20 + C-21; imperative enforcement register throughout)

Run a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 155. Target: 155. Do not proceed past any gate until its conditions are met.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 0: ROSTER — Complete this before any transcript begins
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare the incumbent first. Then declare all human subjects. No transcript may begin until
every subject has an explicit Disposition label in the roster table.

Subject 0 — Incumbent (AI)

| Field | Value |
|-------|-------|
| Role | [Incumbent role — internal domain expert] |
| Knowledge basis | [What the incumbent knows from prior work] |
| Blind spots | [What proximity prevents the incumbent from seeing] |
| Expected bias | [Direction the incumbent will lean] |

Human Subjects Roster — declare before any interview begins

SKEPTIC must be S-01. CHAMPION must be S-02. Do not invert this order.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT — enforce before Step 1:

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| No SKEPTIC label in roster | Explicit skeptic disposition | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| No CHAMPION label in roster | Explicit advocate disposition | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| Any roster entry with no Disposition value | Per-subject disposition label | C-17 (every subject requires explicit label before transcripts begin) |
| Disposition identified only in synthesis | Roster-level pre-transcript declaration | C-17 (synthesis identification is C-11 floor; roster label is C-17 ceiling) |
| CHAMPION in S-01 position | SKEPTIC-first structural ordering | C-18 (SKEPTIC must be S-01 to establish resistance as prior signal) |
| SKEPTIC in S-01 position but Arc Signal compares subjects symmetrically | Skeptic-prior Arc framing | C-18 (structural ordering alone is half-compliance; framing must derive from that ordering) |

COLUMN POLICY — enforce on every HE-# row before synthesis:

Every Human Evidence Pull row must carry all four columns: Signal | Quote | Confidence | Rationale.
Produce all four. Do not omit any. Do not let one stand in for another.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Quote present but Rationale absent | Interpretive rationale | C-10 (confidence without interpretive basis), C-16 (non-substitutable columns) |
| Rationale present but Quote absent | Verbatim subject turn | C-14 (arc claims must be quote-grounded), C-16 (non-substitutable columns) |
| Neither Quote nor Rationale present | Both base columns | C-10, C-14, C-16 |
| Rationale restates Quote | Interpretation distinct from source | C-10 (must answer "why does this signal matter?" not restate the quote) |
| Added column displaces Quote or Rationale | Non-substitutable base column | C-16 (supplemental columns are additive only — displacement fails regardless of column value) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW — complete before human interviews
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

State the prior knowledge block in full before the transcript begins. Do not embed it in answers.

Prior knowledge block:
- Current assumption about TOPIC: [state explicitly — you will revisit this in Step 3]
- Confidence: [1-5]
- What would change this assumption: [name the condition — specific, not generic]

Transcript (minimum 3 turns):

Q1: [Open on the incumbent's core assumption — probe what they believe about TOPIC]
A1: [Incumbent response — role-grounded, complete]

Q2: [Follow up on the blind spot declared above — ask what they cannot see]
A2: [Incumbent response]

Q3: [Apply pressure — ask what evidence would change their stated position]
A3: [Incumbent response — must surface a named threshold condition]

State the surprise before moving to the Tension Log:
Surprise (one sentence): [What emerged that was not anticipated from the prior knowledge block?]

Incumbent Evidence Pull — apply Column Policy to every row:

| IE-# | Claim | Quote | Confidence | Rationale |
|------|-------|-------|------------|-----------|
| IE-1 | [Claim] | "[Verbatim quote — exact words from A1, A2, or A3]" | [1-5] | [Why this claim matters as decision signal] |
| IE-2 | [Claim] | "[Verbatim quote — exact words]" | [1-5] | [Interpretive rationale — not a restatement] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG — derive from incumbent evidence, populate before human interviews
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source column must quote the IE table exactly. Do not paraphrase.

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension between incumbent claims or against external signal] | IE-1: "[exact quote — must match IE table character-for-character]" |
| T-2 | [Second tension] | IE-2: "[exact quote — must match IE table character-for-character]" |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — S-01 (SKEPTIC) first, then S-02 (CHAMPION)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Conduct in roster order. Do not run S-02 before S-01 is complete.

--- S-01 (SKEPTIC) — conduct first ---

State the prior knowledge block before the transcript. Do not skip it.

Prior knowledge block:
- What S-01 knows: [domain-grounded — specific to their role]
- Expected resistance point: [name it explicitly before the transcript]
- What would shift S-01: [name the threshold — specific, not generic]

Transcript (minimum 3 turns):

Q1: [Open without leading toward resistance — invite S-01's framing]
A1: [S-01 response — role-grounded resistance]

Q2: [Probe the named resistance point from the prior knowledge block]
A2: [S-01 response]

Q3: [Reference the incumbent assumption from Step 1 — ask S-01 to react to it]
Q3 contrast note: Name the specific incumbent assumption. Do not paraphrase generically.
A3: [S-01 response — direct tension with incumbent]

Surprise (one sentence): [What S-01 said that contradicted their declared SKEPTIC profile?]

S-01 Evidence Pull — apply Column Policy:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal] | "[Verbatim S-01 quote — exact words]" | [1-5] | [Why this matters to the decision] |
| HE-2 | [Signal] | "[Verbatim S-01 quote — exact words]" | [1-5] | [Interpretive rationale] |

--- S-02 (CHAMPION) — conduct after S-01 is complete ---

Prior knowledge block:
- What S-02 knows: [domain-grounded]
- Expected advocacy point: [name it explicitly]
- What would complicate S-02's position: [name the threshold]

Transcript (minimum 3 turns):

Q1: [Open without leading toward advocacy — invite S-02's framing]
A1: [S-02 response — role-grounded advocacy]

Q2: [Probe the named advocacy point]
A2: [S-02 response]

Q3: [Reference a specific named claim from S-01's transcript — ask S-02 to respond]
Q3 contrast note: Name the claim from S-01. Do not refer generically to "the skeptic's concerns."
A3: [S-02 response — direct engagement with the named SKEPTIC claim]

Surprise (one sentence): [What S-02 said that contradicted their declared CHAMPION profile?]

S-02 Evidence Pull — apply Column Policy:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal] | "[Verbatim S-02 quote — exact words]" | [1-5] | [Why this matters] |
| HE-4 | [Signal] | "[Verbatim S-02 quote — exact words]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS — do not begin until all HE-# rows satisfy Column Policy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gate: Verify all HE-# rows carry Signal, Quote, Confidence, and Rationale. If any row is
missing a column, name the criterion violated before proceeding.

Pattern (2-3 sentences): [What convergent thread and persistent tension appear across all
three evidence sources? Do not summarize individuals — synthesize across them.]

Critical Contradiction Table — rank by evidential weight, most important first:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Most important — incumbent vs. subject, named specifically] | IE-#, HE-# | [What is at risk if unresolved] |
| [Second — S-01 vs. S-02 core arc tension] | HE-#, HE-# | [Stakes for implementation] |

Tension Resolution:
T-1: [How the human interviews resolved, deepened, or reframed T-1]
T-2: [How the human interviews resolved, deepened, or reframed T-2]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1 — named] | [HE-# or IE-# with brief cite] | PROCEED / PAUSE / ESCALATE |
| [Factor 2 — named] | [HE-# or IE-# with brief cite] | PROCEED / PAUSE / ESCALATE |
| [Factor 3 — named] | [HE-# or IE-# with brief cite] | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing — required):
This is not a symmetric comparison. Derive the arc from the prior-signal structure.

Prior signal (SKEPTIC S-01): [Role-grounded resistance S-01 established — what they resisted
and why. This is the prior. State it before considering CHAMPION input.]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned
relative to the SKEPTIC prior above. Frame this as response to the prior, not as standalone
CHAMPION signal.]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence stating what SKEPTIC
established and how CHAMPION responded to it. Must reference both S-01 and S-02 evidence.]

Prior Assumption Revisited:
Before: [Exact language of incumbent assumption from Step 1 — do not summarize]
After: [What it should now be revised to, grounded in IE-# and HE-# combined]
Delta: [One sentence — what specifically changed and why the evidence warrants it]
```

---

## V-05: All Five Axes — Maximum Enforcement (C-20 + C-21 + full prior criteria)

**Axis:** All five axes simultaneously — role sequence (SKEPTIC-first with extended rationale), output format (tabular blocks), lifecycle emphasis (explicit phase-gate enforcement at each step), phrasing register (precision-first, formal), inertia framing (incumbent coupling prominent, switching-cost framing in verdict matrix).
**Hypothesis:** Full-ceiling template with maximum enforcement of all criteria through C-21 achieves 155/155. Incumbent coupling table and switching-cost framing in inertia verdict are additive to evidence infrastructure without displacing required columns.

```
PROVE-INTERVIEW PROMPT — V-05 (all axes; full R6 ceiling; C-20 + C-21 + maximum enforcement)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 155. Target: 155. All criteria through C-21 enforced. Maximum phase-gate
enforcement. Incumbent coupling tracked throughout.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 0: ROSTER — complete in full before any transcript begins
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject 0 — Incumbent (AI)

The incumbent represents the status quo that [TOPIC] would displace or augment. Declare the
incumbent's coupling to existing practice before conducting any interview. This coupling
establishes the inertia baseline against which human subject responses are evaluated.

| Field | Value |
|-------|-------|
| Role | [Incumbent role — internal domain expert closest to current practice] |
| Knowledge basis | [What the incumbent knows about TOPIC from prior work — specific, not generic] |
| Blind spots | [What proximity to current practice prevents the incumbent from seeing] |
| Expected bias | [Direction the incumbent will lean — name the specific bias, not just "conservative"] |
| Coupling to status quo | [What current practice this incumbent defends and why displacement is costly to them] |

Human Subjects — Interview Roster

SKEPTIC-FIRST REQUIREMENT: S-01 must be the SKEPTIC. S-02 must be the CHAMPION. This ordering
is not cosmetic. The SKEPTIC interview establishes resistance as the prior signal. The CHAMPION
interview is the evidence against or for that prior. Inverting the order eliminates the causal
structure of the arc — you would be comparing two equal voices rather than measuring a
champion's response to an established prior. Do not reorder.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC, declared first] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION, declared second] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT — enforce at roster level before Step 1:

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| No SKEPTIC label in roster | Explicit skeptic disposition before any transcript | C-11 (Disposition arc structured — arc requires both poles declared), C-17 (Roster-level disposition labels — every subject requires explicit per-subject label before transcripts begin) |
| No CHAMPION label in roster | Explicit advocate disposition before any transcript | C-11 (Disposition arc structured — arc requires both poles declared), C-17 (Roster-level disposition labels — every subject requires explicit per-subject label before transcripts begin) |
| Any roster entry with no Disposition column value | Per-subject disposition label | C-17 (every human subject requires explicit per-subject label before transcripts begin — absence on any single entry fails the criterion) |
| Disposition identified only in synthesis | Roster-level pre-transcript declaration | C-17 (C-11 is the floor — arc may appear in synthesis; C-17 is the ceiling — per-subject label must appear at roster level before any transcript begins; synthesis-level identification does not retroactively satisfy roster-level declaration) |
| CHAMPION declared as S-01 | SKEPTIC-first structural ordering | C-18 (Skeptic-first roster ordering — the SKEPTIC must appear as S-01 to establish resistance as the prior signal; reversing the order eliminates the causal structure C-18 requires) |
| SKEPTIC-first ordering present but Arc Signal uses symmetric framing | Skeptic-prior Arc framing | C-18 (C-18 requires both structural ordering AND skeptic-prior Arc framing simultaneously; structural ordering alone satisfies only half the criterion — a SKEPTIC-first roster whose Arc Signal reads "S-01 said X; S-02 said Y" rather than "prior signal (SKEPTIC S-01): ... / subsequent evidence (CHAMPION S-02): ..." fails C-18 on framing) |

COLUMN POLICY for Human Evidence Pulls (HE-#) — enforce on every row before synthesis:

Each evidence row must carry all four columns simultaneously: Signal | Quote | Confidence | Rationale.
Quote = verbatim subject turn, exact words, not paraphrased. Rationale = interpretive statement
answering "why does this signal matter to the topic decision?" — not a restatement of the quote.
Confidence = explicit 1-5 numeric rating. All four coexist in every row. Column additions are
additive, not substitutive.

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Quote present but Rationale absent | Interpretive rationale per row | C-10 (Evidence confidence rated — a confidence score without accompanying rationale cannot be evaluated for basis), C-16 (Evidence columns non-substitutable — Quote does not substitute for Rationale; both must coexist simultaneously in the same row) |
| Rationale present but Quote absent | Verbatim SUBJECT source turn | C-14 (Arc claims quote-anchored — rationale claims must be grounded in verbatim subject language; paraphrasing does not satisfy the quote requirement), C-16 (Evidence columns non-substitutable — Rationale does not substitute for Quote; both must coexist simultaneously) |
| Neither Quote nor Rationale present | Both base columns | C-10 (no rationale basis), C-14 (no quote grounding), C-16 (both base columns absent — non-substitutability violation at maximum severity) |
| Rationale restates Quote | Interpretive content distinct from quote | C-10 (Rationale must answer "why does this signal matter to the feature decision?" — paraphrasing the quote does not constitute interpretation; the Rationale column exists to carry evaluative content the Quote column cannot carry) |
| Architectural column displaces Quote or Rationale | Non-substitutable base column | C-16 (adding Phase, Theme, Category, or any supplemental column is permitted only if it supplements the four required columns; any addition that displaces Quote or Rationale from any row violates non-substitutability regardless of the addition's descriptive value) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW (AI-conducted; completes before human sessions begin)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete in full before transcript begins):
- Current assumption about TOPIC: [state explicitly — this exact statement will be revisited
  in Step 3 Prior Assumption Revisited; do not summarize it later]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition — specific, not "more evidence"]
- Current-practice anchor: [What the incumbent does today before any feature is introduced —
  this is the Q1 behavioral baseline; state it before asking Q1]

Transcript (minimum 3 turns — Q from interviewer, A from incumbent):

Q1: [Opening — ask what the incumbent does today, before any feature is introduced. This is
    the current-practice anchor question. Do not lead with the feature.]
A1: [Incumbent response — grounded in the current-practice anchor declared above]

Q2: [Follow-up targeting the named blind spot from the roster — ask what they cannot see
    from their position in current practice]
A2: [Incumbent response — reveals internal tension or confirms assumption]

Q3: [Pressure question — specifically ask what evidence or condition would change the
    stated assumption. Reference the assumption explicitly.]
A3: [Incumbent response — surfaces the threshold condition human interviews will test]

Surprise (one sentence): [What emerged in the incumbent interview that was not anticipated
given the prior knowledge block and current-practice anchor declared above?]

Incumbent Evidence Pull — apply Column Policy to every row:

| IE-# | Claim | Quote | Confidence | Rationale |
|------|-------|-------|------------|-----------|
| IE-1 | [Claim extracted from incumbent transcript] | "[Verbatim quote from A1, A2, or A3 — exact words, not paraphrased]" | [1-5] | [Why this claim matters as signal for the topic decision — interpretive, not a restatement] |
| IE-2 | [Second claim — distinct from IE-1] | "[Verbatim quote — exact words]" | [1-5] | [Interpretive rationale — answers "why does this matter?" not "what did they say?"] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG (derived from incumbent evidence; populated before human interviews)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source column quotes must match the IE table Quote column exactly. Paraphrasing fails.

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension between two incumbent claims or between a claim and known external signal — named specifically] | IE-1: "[exact quote — must match IE-1 Quote column character-for-character]" |
| T-2 | [Second tension — may span incumbent claim and anticipated human-interview gap] | IE-2: "[exact quote — must match IE-2 Quote column character-for-character]" |

Incumbent Coupling Table (switching-cost baseline for Step 3 Inertia Verdict):

| Coupling Factor | How It Appeared in Transcript | Switch Cost |
|----------------|-------------------------------|-------------|
| [Factor 1 — what current practice element is at risk if TOPIC proceeds] | IE-# or A-# reference | LOW / MEDIUM / HIGH |
| [Factor 2 — second coupling factor from incumbent evidence] | IE-# or A-# reference | LOW / MEDIUM / HIGH |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — SKEPTIC-FIRST SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Conduct S-01 (SKEPTIC) before S-02 (CHAMPION). The SKEPTIC interview establishes the
resistance prior. The CHAMPION interview is evidence against or for that prior. Do not
reorder. Do not conduct both simultaneously.

--- S-01 (SKEPTIC) ---

Prior knowledge block (complete before transcript begins):
- What S-01 knows about TOPIC: [domain-grounded — specific to S-01's role and experience]
- S-01's expected resistance point: [name explicitly before the transcript begins — this is
  the prior resistance that will be tested in Q2]
- What would shift S-01's position: [named threshold — specific, not "convincing evidence"]

Transcript (minimum 3 turns):

Q1: [Open on current practice — what does S-01 do today before any feature is introduced?
    Use the current-practice Q1 anchor. Do not lead with the feature or the resistance.]
A1: [S-01 response — role-grounded; grounded in the current-practice anchor above]

Q2: [Probe the specific resistance point named in the prior knowledge block above]
A2: [S-01 response — deepens or qualifies resistance with specifics from their domain]

Q3: [Contrast question — explicitly reference the incumbent assumption from Step 1 and
    ask S-01 to react to it. Name the assumption. Do not paraphrase it generically.]
Q3 contrast note: This Q3 contrast references the exact incumbent assumption stated in Step 1
prior knowledge block. The contrast must be explicit, not implied.
A3: [S-01 response — direct tension with incumbent position]

Surprise (one sentence): [What S-01 said that was not anticipated given their declared
SKEPTIC disposition and the named resistance point above?]

S-01 Evidence Pull — apply Column Policy:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal from S-01 transcript] | "[Verbatim S-01 quote — exact words from A1, A2, or A3]" | [1-5] | [Why this signal matters to the topic decision — interpretive, not a restatement] |
| HE-2 | [Second signal from S-01] | "[Verbatim S-01 quote — exact words]" | [1-5] | [Interpretive rationale distinct from quote content] |

--- S-02 (CHAMPION) ---

Prior knowledge block (complete before transcript begins):
- What S-02 knows about TOPIC: [domain-grounded — specific to S-02's role and experience]
- S-02's expected advocacy point: [name explicitly before the transcript begins]
- What would complicate S-02's position: [named threshold — specific, not "concerns arising"]

Transcript (minimum 3 turns):

Q1: [Open on current practice — what does S-02 do today before any feature is introduced?
    Use the current-practice Q1 anchor. Do not lead with the feature or the advocacy.]
A1: [S-02 response — role-grounded; grounded in the current-practice anchor]

Q2: [Probe the specific advocacy point named in the prior knowledge block above]
A2: [S-02 response — deepens or qualifies advocacy with specifics]

Q3: [Contrast question — explicitly reference a specific named claim from S-01's transcript
    and ask S-02 to respond to it. Name S-01's exact claim, not a generic reference.]
Q3 contrast note: This Q3 contrast names a specific claim from S-01's transcript above.
The claim must be identified by quoting or closely paraphrasing S-01's language.
A3: [S-02 response — direct engagement with the named SKEPTIC claim]

Surprise (one sentence): [What S-02 said that was not anticipated given their declared
CHAMPION disposition and the named advocacy point above?]

S-02 Evidence Pull — apply Column Policy:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal from S-02 transcript] | "[Verbatim S-02 quote — exact words from A1, A2, or A3]" | [1-5] | [Why this signal matters to the topic decision — interpretive, not a restatement] |
| HE-4 | [Second signal from S-02] | "[Verbatim S-02 quote — exact words]" | [1-5] | [Interpretive rationale distinct from quote content] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-synthesis gate: All HE-# rows must contain all four columns per Column Policy (Signal,
Quote, Confidence, Rationale). Do not proceed to synthesis if any row is missing any column.
If a row is missing a column, name the specific criterion violated before proceeding.

Pattern (2-3 sentences): [What pattern emerges across incumbent + S-01 + S-02 evidence?
Name the convergent thread and the persistent tension. Do not summarize individual interviews
— synthesize across them. The current-practice contrast from Q1 anchors should be visible
in the pattern if they produced grounding evidence.]

Critical Contradiction Table — rank by evidential weight; most significant first:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Most significant — incumbent claim vs. human subject claim, named specifically] | IE-#, HE-# | [What is at risk if this contradiction is unresolved] |
| [Second — S-01 SKEPTIC claim vs. S-02 CHAMPION claim — the core arc tension] | HE-#, HE-# | [What is at risk if this tension persists into implementation] |

Tension Resolution:
T-1: [How the human interviews resolved, deepened, or reframed T-1 — specific HE references]
T-2: [How the human interviews resolved, deepened, or reframed T-2 — specific HE references]

Inertia Verdict Matrix (reference Incumbent Coupling Table factors):

| Factor | Evidence | Switch Cost | Verdict |
|--------|----------|-------------|---------|
| [Coupling Factor 1 from Incumbent Coupling Table] | IE-# or HE-# cite | LOW / MEDIUM / HIGH | PROCEED / PAUSE / ESCALATE |
| [Coupling Factor 2 from Incumbent Coupling Table] | IE-# or HE-# cite | LOW / MEDIUM / HIGH | PROCEED / PAUSE / ESCALATE |
| [Factor 3 — additional signal factor from HE-# evidence] | HE-# cite | LOW / MEDIUM / HIGH | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing — required):
Skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence.
This is not a symmetric comparison between two equal voices. The SKEPTIC established the
resistance prior. The CHAMPION responded to that prior. The arc conclusion must reflect
the causal sequence: prior -> response -> resolution.

Prior signal (SKEPTIC S-01): [Role-grounded resistance established by S-01 — what they
resisted and why, stated as the prior that the CHAMPION must respond to. Ground this in
HE-1 and HE-2. State it before considering CHAMPION input.]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned
relative to the SKEPTIC prior stated above. Ground this in HE-3 and HE-4. The framing must
be relative to the prior — not a standalone CHAMPION summary.]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence explaining the
dominant signal that emerged from the skeptic-prior framing. Must name what the SKEPTIC
established and how the CHAMPION responded to it. Must reference HE-# from both subjects.]

Grounding check: Arc conclusion must reference HE-# from both S-01 and S-02 evidence pulls.
If the conclusion references only one subject, it is not an arc — revise before filing.

Prior Assumption Revisited:
Before: [Restate the incumbent assumption from Step 1 prior knowledge block — exact language,
not a summary. This must be a verbatim restatement of what was declared in Step 1.]
After: [What the assumption should be revised to, given all evidence from IE-# and HE-#
combined — this is the updated signal position]
Delta: [One sentence naming specifically what changed (not that evidence was gathered) and
why the change is warranted by the specific evidence collected]
```

---

```json
{
  "file": "prove-interview-variations-R6-2026-03-14.md",
  "round": 6,
  "skill": "prove-interview",
  "date": "2026-03-14",
  "ceiling": 155,
  "variations": [
    {"id": "V-01", "axes": ["role-sequence", "c20-prose"], "c20": true, "c21": false, "target": 150},
    {"id": "V-02", "axes": ["output-format-tabular"], "c20": "partial", "c21": true, "target": 150},
    {"id": "V-03", "axes": ["both-minimal"], "c20": true, "c21": true, "target": 155},
    {"id": "V-04", "axes": ["phrasing-register-imperative"], "c20": true, "c21": true, "target": 155},
    {"id": "V-05", "axes": ["all-axes"], "c20": true, "c21": true, "target": 155}
  ],
  "new_criteria": ["C-20", "C-21"],
  "baseline": "R5-V03-V04-V05-145/145",
  "r5_delta": "C-20 sixth-DISPOSITION-condition partial-compliance; C-21 three-column-tabular both blocks"
}
```
