All 18 checks pass. The file is written and complete.

---

## Round 5 Variations — `prove-interview-variations-R5-2026-03-14.md`

**54,892 chars · 5 complete variations · targeting C-18 + C-19 · ceiling 145**

### Variation Map

| V | Axis | C-18 | C-19 | Absent | Predicted |
|---|------|------|------|--------|-----------|
| V-01 | Role sequence | YES | NO | C-19 | 140/145 |
| V-02 | Lifecycle emphasis | NO | YES | C-18 | 140/145 |
| V-03 | Both fixes, minimal | YES | YES | — | 145/145 |
| V-04 | Output format (tabular blocks) | YES | YES | — | 145/145 |
| V-05 | All five axes | YES | YES | — | 145/145 |

### What's new in R5

**C-18 fix** — two things required simultaneously, and V-01 gives you both:
- Structure: `S-01 = SKEPTIC` in roster
- Framing: Arc Signal uses `Prior signal (SKEPTIC S-01):` / `Subsequent evidence (CHAMPION S-02):` not symmetric two-voice

**C-19 fix** — the narrow delta from R4: same named blocks (`DISPOSITION REQUIREMENT`, `COLUMN POLICY`), but each failure condition now names the absent element AND cites the criterion:
- `"Roster entry with no Disposition value: FAILS C-17 (Roster-level disposition labels)"` — not `"fails the structural requirement"`
- `"Table has Quote + Confidence but no Rationale: FAILS C-10 and FAILS C-16"` — not `"is incomplete"`

### Isolation experiments

V-01 and V-02 are true single-axis isolations — each applies exactly one new criterion while holding the other absent. If both score 140/145, the criteria are independently satisfiable. If either drops below 140 despite the targeted fix, the fix is incomplete.

V-03 tests the **minimal combination**: just the two targeted changes to R4 V-04. If V-03 scores 145, no further axes are needed.

V-04 tests whether **tabular failure conditions** satisfy C-19 equivalently to prose-itemized bullets. If V-03 = 145 and V-04 < 145, the scorer treats tabular rows as weaker than prose bullets for "itemized per-condition failure statements."
whether tabular format satisfies C-19 itemized requirement equivalently to prose bullets.

**V-05 (all five axes — full R5 ceiling):** All five axes. SKEPTIC-first with full prior-signal
Arc framing. Both blocks carry prose-itemized criterion-ID failure statements. Maximum phase-gate
enforcement. Based on R4 V-05 with C-19 upgrade throughout.

---

### What R4 established (baseline for R5 delta)

R4 V-03 and V-05 were SKEPTIC-first and had skeptic-prior Arc framing — already satisfying C-18
structurally and in framing. R4 V-04 was CHAMPION-first (fails C-18). All three scored 135/135.

R4 compliance blocks had named titled sections and some failure conditions but used "fails the
structural requirement" language — no criterion IDs. C-19 requires: each failure condition names
exactly what is absent AND which criterion it violates. The R4-to-R5 delta for C-19 is narrow:
same block structure, same two blocks required, but each failure statement must now cite the
criterion.

---

### Key structural changes that fix C-18

Roster ordering change (from R4 CHAMPION-first to SKEPTIC-first):
```
R4 V-04: | S-01 | [job title] | ... | CHAMPION |
          | S-02 | [job title] | ... | SKEPTIC  |

R5 fix:  | S-01 | [job title — the SKEPTIC]  | ... | SKEPTIC  |
          | S-02 | [job title — the CHAMPION] | ... | CHAMPION |
```

Arc Signal framing change (from symmetric to skeptic-prior):
```
R4 V-04: "State whether convergence or contradiction was the dominant arc signal."
          "CHAMPION/SKEPTIC arc: Was convergence reached despite SKEPTIC resistance?"

R5 fix:  "Skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence."
          "Prior signal (SKEPTIC S-01): [role-grounded resistance established]"
          "Subsequent evidence (CHAMPION S-02): [what CHAMPION confirmed, complicated, or overturned]"
```

### Key structural changes that fix C-19

Block failure statement language change (from structural-requirement to criterion-ID):
```
R4 any:  "A roster entry with no Disposition label fails the structural requirement."

R5 fix:  "Roster entry with no Disposition column value: FAILS C-17 (Roster-level disposition
          labels — every human subject requires an explicit per-subject label before any
          transcript begins)."

R4 any:  "A table with Quote + Confidence but no Rationale is incomplete."

R5 fix:  "Table has Quote + Confidence but no Rationale: FAILS C-10 (Evidence confidence rated)
          and FAILS C-16 (Evidence columns non-substitutable — Quote does not substitute for
          Rationale; both must coexist simultaneously)."
```

---

## V-01: Role Sequence — SKEPTIC-First Ordering (C-18 only)

**Axis:** Role sequence (single-axis).
**Hypothesis:** SKEPTIC declared as S-01 with Arc Signal synthesis framed as skeptic-resistance-as-prior-signal is sufficient for C-18 PASS independently of compliance block failure statement quality. Both compliance blocks present but failure statements use "fails the structural requirement" language without criterion IDs. C-19 absent by design to isolate C-18.

```
PROVE-INTERVIEW PROMPT — V-01 (C-18 only, SKEPTIC-first roster, no criterion IDs in compliance blocks)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 145. Target: 140 (C-18 present; C-19 absent by design).

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

SKEPTIC-FIRST SEQUENCE: The SKEPTIC must be declared as S-01. The CHAMPION must be declared
as S-02. This ordering is required. The sequence is not cosmetic — it establishes that SKEPTIC
resistance is the prior signal and CHAMPION confirmation is the subsequent evidence.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value (SKEPTIC or
CHAMPION). The SKEPTIC must appear as S-01. A roster entry with no Disposition label fails the
structural requirement. A roster with CHAMPION declared as S-01 fails the structural requirement.
Disposition inferred from synthesis-level arc analysis but absent from this table fails the
structural requirement.

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
Quote = verbatim subject turn. Rationale = interpretive statement explaining why this signal
matters. Confidence = rated 1-5. All four columns must coexist simultaneously. A table with
Quote + Confidence but no Rationale is incomplete and fails the column policy. A table with
Rationale + Confidence but no Quote fails the column policy. A table with Confidence only
fails the column policy. A Rationale that merely restates the Quote fails the column policy.
Adding an architectural column (e.g., Phase, Theme) does not substitute for Quote or Rationale.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW (AI-conducted, prior to human sessions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete before transcript):
- Current assumption about TOPIC: [state explicitly]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition]

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
| IE-1 | [Claim extracted from incumbent transcript] | "[Verbatim quote from A1, A2, or A3]" | [1-5] | [Why this claim matters as signal] |
| IE-2 | [Second claim] | "[Verbatim quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG (derived from incumbent evidence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension between two incumbent claims or between claim and known external signal] | IE-1: "[exact quote from IE table]" |
| T-2 | [Second tension — may span incumbent + external knowledge] | IE-2: "[exact quote from IE table]" |

Tension source quotes must exactly match the Quote column of the referenced IE row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — SKEPTIC-FIRST SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Interview subjects in declared roster order: S-01 (SKEPTIC) before S-02 (CHAMPION).
The SKEPTIC interview establishes the resistance prior. The CHAMPION interview is evidence
against or for that prior. Do not reorder.

For each human subject in roster order (S-01 then S-02):

--- S-01 (SKEPTIC) ---

Prior knowledge block:
- What S-01 knows about TOPIC: [domain-grounded]
- S-01's expected resistance point: [named before transcript]
- What would shift S-01: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing of TOPIC]
A1: [S-01 response — role-grounded resistance or concern]

Q2: [Probe the specific resistance point named above]
A2: [S-01 response — deepens or qualifies resistance]

Q3: [Contrast question — reference incumbent assumption, ask S-01 to react]
Q3 contrast note: The Q3 contrast references the incumbent assumption stated in Step 1.
A3: [S-01 response — direct tension with incumbent position]

Surprise (one sentence): [What S-01 said that was not anticipated from their declared disposition?]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal from S-01 transcript] | "[Verbatim S-01 quote]" | [1-5] | [Why this signal matters] |
| HE-2 | [Second signal] | "[Verbatim S-01 quote]" | [1-5] | [Interpretive rationale] |

--- S-02 (CHAMPION) ---

Prior knowledge block:
- What S-02 knows about TOPIC: [domain-grounded]
- S-02's expected advocacy point: [named before transcript]
- What would complicate S-02's position: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing of TOPIC]
A1: [S-02 response — role-grounded advocacy or enthusiasm]

Q2: [Probe the specific advocacy point named above]
A2: [S-02 response — deepens or qualifies advocacy]

Q3: [Contrast question — reference S-01's resistance, ask S-02 to react]
Q3 contrast note: The Q3 contrast references a specific claim from S-01's transcript above.
A3: [S-02 response — direct engagement with SKEPTIC position]

Surprise (one sentence): [What S-02 said that was not anticipated from their declared disposition?]

S-02 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal from S-02 transcript] | "[Verbatim S-02 quote]" | [1-5] | [Why this signal matters] |
| HE-4 | [Second signal] | "[Verbatim S-02 quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-synthesis gate: All HE-# rows must contain Signal, Quote, Confidence, and Rationale columns.
Do not proceed to synthesis if any row is missing a column.

Pattern (2-3 sentences): [What pattern emerges across incumbent + S-01 + S-02 evidence?]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent claim vs. S-01 or S-02 claim] | IE-#, HE-# | [What is at risk if unresolved] |
| [S-01 claim vs. S-02 claim — the core skeptic/champion tension] | HE-#, HE-# | [Stakes] |

Tension Resolution:
T-1: [How the human interviews resolved or deepened T-1]
T-2: [How the human interviews resolved or deepened T-2]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1] | [HE or IE reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 2] | [HE or IE reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 3] | [HE or IE reference] | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing):
Skeptic resistance is the prior signal. Champion confirmation-or-overturn is the evidence.

Prior signal (SKEPTIC S-01): [Role-grounded resistance established by S-01 — what they resisted
and why, stated before considering CHAMPION input]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned relative
to the SKEPTIC prior — the arc conclusion depends on this response to the prior]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — with one sentence explaining the
dominant signal that emerged from skeptic-prior framing]

Prior Assumption Revisited:
Before: [Restate the incumbent assumption from Step 1 exactly]
After: [What the assumption should be revised to, given all evidence]
Delta: [One sentence naming what changed and why]
```

---

## V-02: Lifecycle Emphasis — C-19 Only (CHAMPION-first, no C-18)

**Axis:** Lifecycle emphasis (single-axis C-19 upgrade).
**Hypothesis:** Both compliance blocks upgraded with per-condition failure statements explicitly citing criterion IDs (C-11, C-17 for DISPOSITION; C-10, C-14, C-16 for COLUMN POLICY) is sufficient for C-19 PASS independently of roster ordering. CHAMPION declared as S-01 (C-18 absent by design). Arc Signal uses symmetric framing (no skeptic-prior). C-18 absent to isolate C-19.

```
PROVE-INTERVIEW PROMPT — V-02 (C-19 only, CHAMPION-first roster, criterion IDs in compliance blocks)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 145. Target: 140 (C-19 present; C-18 absent by design — CHAMPION-first roster).

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

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the CHAMPION] | [Domain] | CHAMPION |
| S-02 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value (SKEPTIC or
CHAMPION) declared before any transcript begins. Inferred disposition is not sufficient.

Per-condition failure statements:
- No CHAMPION label in roster: FAILS C-11 (Disposition arc structured) and FAILS C-17
  (Roster-level disposition labels — every human subject requires an explicit per-subject
  label before transcripts begin)
- No SKEPTIC label in roster: FAILS C-11 (Disposition arc structured) and FAILS C-17
  (Roster-level disposition labels — every human subject requires an explicit per-subject
  label before transcripts begin)
- Roster entry with no Disposition column value: FAILS C-17 (every human subject requires
  explicit per-subject label before transcripts begin)
- Disposition inferred from synthesis-level arc analysis but absent from this table: FAILS
  C-17 (C-11 is the floor — arc appears in synthesis; C-17 is the ceiling — per-subject label
  must appear at roster level before any transcript begins)

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
Quote = verbatim subject turn. Rationale = interpretive statement explaining why this signal
matters. Confidence = rated 1-5. All four columns must coexist simultaneously.

Per-condition failure statements:
- Table has Quote + Confidence but no Rationale: FAILS C-10 (Evidence confidence rated) and
  FAILS C-16 (Evidence columns non-substitutable — Quote does not substitute for Rationale;
  both must coexist simultaneously)
- Table has Rationale + Confidence but no Quote: FAILS C-14 (Arc claims quote-anchored) and
  FAILS C-16 (Evidence columns non-substitutable — Rationale does not substitute for Quote;
  both must coexist simultaneously)
- Table has Confidence only: FAILS C-10 (Evidence confidence rated), FAILS C-14 (Arc claims
  quote-anchored), and FAILS C-16 (Evidence columns non-substitutable)
- Rationale restates the Quote: FAILS C-10 (Rationale must answer "why does this signal
  matter?" — not paraphrase the quote)
- Architectural addition placed in position that removes Quote or Rationale: FAILS C-16
  (adding a column such as Phase or Theme does not substitute for Quote or Rationale)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW (AI-conducted, prior to human sessions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete before transcript):
- Current assumption about TOPIC: [state explicitly]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition]

Transcript (minimum 3 turns):

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
| IE-1 | [Claim] | "[Verbatim quote]" | [1-5] | [Why this claim matters] |
| IE-2 | [Second claim] | "[Verbatim quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension between incumbent claims or against external signal] | IE-1: "[exact quote]" |
| T-2 | [Second tension] | IE-2: "[exact quote]" |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For each human subject in roster, in declared order (CHAMPION before SKEPTIC).

--- S-01 (CHAMPION) ---

Prior knowledge block:
- What S-01 knows about TOPIC: [domain-grounded]
- S-01's expected advocacy point: [named before transcript]
- What would complicate S-01's position: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing of TOPIC]
A1: [S-01 response — role-grounded advocacy]

Q2: [Probe the specific advocacy point named above]
A2: [S-01 response — deepens or qualifies advocacy]

Q3: [Contrast question — reference incumbent assumption, ask S-01 to react]
Q3 contrast note: The Q3 contrast references the incumbent assumption stated in Step 1.
A3: [S-01 response]

Surprise (one sentence): [What S-01 said that was not anticipated?]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal from S-01] | "[Verbatim S-01 quote]" | [1-5] | [Why this signal matters] |
| HE-2 | [Second signal] | "[Verbatim S-01 quote]" | [1-5] | [Interpretive rationale] |

--- S-02 (SKEPTIC) ---

Prior knowledge block:
- What S-02 knows about TOPIC: [domain-grounded]
- S-02's expected resistance point: [named before transcript]
- What would shift S-02: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing of TOPIC]
A1: [S-02 response — role-grounded resistance]

Q2: [Probe the specific resistance point named above]
A2: [S-02 response — deepens or qualifies resistance]

Q3: [Contrast question — reference S-01's advocacy, ask S-02 to react]
Q3 contrast note: The Q3 contrast references a specific claim from S-01's transcript above.
A3: [S-02 response — direct engagement with CHAMPION position]

Surprise (one sentence): [What S-02 said that was not anticipated?]

S-02 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-3 | [Signal from S-02] | "[Verbatim S-02 quote]" | [1-5] | [Why this signal matters] |
| HE-4 | [Second signal] | "[Verbatim S-02 quote]" | [1-5] | [Interpretive rationale] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: SYNTHESIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-synthesis gate: All HE-# rows must contain Signal, Quote, Confidence, and Rationale.

Pattern (2-3 sentences): [What pattern emerges across all evidence?]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent vs. subject claim] | IE-#, HE-# | [Stakes] |
| [S-01 claim vs. S-02 claim] | HE-#, HE-# | [Stakes] |

Tension Resolution:
T-1: [How human interviews resolved or deepened T-1]
T-2: [How human interviews resolved or deepened T-2]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1] | [HE or IE reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 2] | [HE or IE reference] | PROCEED / PAUSE / ESCALATE |
| [Factor 3] | [HE or IE reference] | PROCEED / PAUSE / ESCALATE |

Arc Signal (symmetric — C-18 absent by design):
Evidence per subject:
- S-01 (CHAMPION): [Core signal from CHAMPION — what they confirmed or advocated]
- S-02 (SKEPTIC): [Core signal from SKEPTIC — what they resisted or questioned]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — with one sentence describing the
dominant signal that emerged from the two-voice comparison]

Prior Assumption Revisited:
Before: [Restate the incumbent assumption from Step 1 exactly]
After: [Revised assumption given all evidence]
Delta: [One sentence naming what changed and why]
```

---

## V-03: Both Fixes, Minimal (C-18 + C-19, SKEPTIC-first, criterion IDs)

**Axis:** Both fixes applied, minimal combination.
**Hypothesis:** SKEPTIC-first roster (C-18) combined with criterion-ID failure statements in both compliance blocks (C-19) is sufficient for 145/145. No additional axes required. Minimal change from R4 V-04 baseline.

```
PROVE-INTERVIEW PROMPT — V-03 (C-18 + C-19, SKEPTIC-first, criterion IDs, minimal combination)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 145. Target: 145 (both C-18 and C-19 present).

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

SKEPTIC-FIRST: S-01 must be the SKEPTIC. S-02 must be the CHAMPION.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value (SKEPTIC or
CHAMPION) declared before any transcript begins.

Per-condition failure statements:
- No SKEPTIC label in roster: FAILS C-11 (Disposition arc structured) and FAILS C-17
  (Roster-level disposition labels)
- No CHAMPION label in roster: FAILS C-11 (Disposition arc structured) and FAILS C-17
  (Roster-level disposition labels)
- Roster entry with no Disposition column value: FAILS C-17 (every human subject requires
  explicit per-subject label before transcripts begin)
- Disposition inferred from synthesis-level arc analysis but absent from this table: FAILS
  C-17 (C-11 is floor — arc in synthesis; C-17 is ceiling — per-subject label at roster level)
- CHAMPION declared as S-01: FAILS C-18 (Skeptic-first roster ordering — SKEPTIC must appear
  as S-01 to establish resistance as the prior signal)

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
Quote = verbatim subject turn. Rationale = interpretive statement explaining why this signal
matters. Confidence = rated 1-5. All four columns must coexist simultaneously.

Per-condition failure statements:
- Table has Quote + Confidence but no Rationale: FAILS C-10 (Evidence confidence rated) and
  FAILS C-16 (Evidence columns non-substitutable — Quote does not substitute for Rationale)
- Table has Rationale + Confidence but no Quote: FAILS C-14 (Arc claims quote-anchored) and
  FAILS C-16 (Evidence columns non-substitutable — Rationale does not substitute for Quote)
- Table has Confidence only: FAILS C-10, FAILS C-14, and FAILS C-16
- Rationale restates the Quote: FAILS C-10 (Rationale must answer "why does this signal
  matter?" — not paraphrase)
- Architectural addition placed in position that removes Quote or Rationale: FAILS C-16

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete before transcript):
- Current assumption about TOPIC: [state explicitly]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition]

Transcript (minimum 3 turns):

Q1: [Opening question probing incumbent's core assumption]
A1: [Incumbent response]

Q2: [Follow-up targeting blind spot]
A2: [Incumbent response]

Q3: [Pressure question — what evidence would change position?]
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

Interview subjects in declared roster order: S-01 (SKEPTIC) before S-02 (CHAMPION).

--- S-01 (SKEPTIC) ---

Prior knowledge block:
- What S-01 knows about TOPIC: [domain-grounded]
- S-01's expected resistance point: [named]
- What would shift S-01: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing]
A1: [S-01 response — resistance grounded in role]

Q2: [Probe resistance point]
A2: [S-01 response — deepens resistance]

Q3: [Contrast with incumbent assumption]
Q3 contrast note: References incumbent assumption from Step 1.
A3: [S-01 response — direct tension with incumbent]

Surprise (one sentence): [Unanticipated from S-01]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal] | "[Verbatim S-01 quote]" | [1-5] | [Why this matters] |
| HE-2 | [Signal] | "[Verbatim S-01 quote]" | [1-5] | [Interpretive rationale] |

--- S-02 (CHAMPION) ---

Prior knowledge block:
- What S-02 knows about TOPIC: [domain-grounded]
- S-02's expected advocacy point: [named]
- What would complicate S-02: [named threshold]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing]
A1: [S-02 response — advocacy grounded in role]

Q2: [Probe advocacy point]
A2: [S-02 response — deepens advocacy]

Q3: [Contrast with S-01's resistance]
Q3 contrast note: References a specific claim from S-01's transcript above.
A3: [S-02 response — direct engagement with SKEPTIC]

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
| [Incumbent vs. subject] | IE-#, HE-# | [Stakes] |
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

Prior signal (SKEPTIC S-01): [What S-01 resisted and why — stated as prior]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence]

Prior Assumption Revisited:
Before: [Exact restatement of incumbent assumption from Step 1]
After: [Revised assumption]
Delta: [What changed and why]
```

---

## V-04: Output Format — Tabular Failure Conditions (C-18 + C-19, tabular blocks)

**Axis:** Output format (tabular failure condition tables).
**Hypothesis:** Both fixes applied. SKEPTIC-first (C-18). Per-condition failure statements presented as structured tables with Condition | What is absent | Criterion(s) violated columns satisfies C-19 itemized requirement equivalently to prose bullets.

```
PROVE-INTERVIEW PROMPT — V-04 (C-18 + C-19, SKEPTIC-first, tabular failure condition blocks)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 145. Target: 145 (both C-18 and C-19 present; tabular format for C-19 blocks).

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

Rules:
1. Roster must contain at least one SKEPTIC and one CHAMPION.
2. SKEPTIC must be declared as S-01.
3. Disposition column value must appear in roster table — not in synthesis.

Failure conditions:

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| No SKEPTIC label in roster | Explicit skeptic disposition | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| No CHAMPION label in roster | Explicit advocate disposition | C-11 (Disposition arc structured), C-17 (Roster-level disposition labels) |
| Roster entry with no Disposition column value | Per-subject disposition label | C-17 (every human subject requires explicit per-subject label before transcripts begin) |
| Disposition inferred from synthesis only | Roster-level declaration | C-17 (C-11 is floor — arc in synthesis; C-17 is ceiling — per-subject label at roster level) |
| CHAMPION declared as S-01 | SKEPTIC-first ordering | C-18 (Skeptic-first roster ordering — SKEPTIC must appear as S-01) |

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
All four columns must coexist simultaneously. No column substitutes for another.

Required schema:
Signal | Quote | Confidence | Rationale
[Label] | [Verbatim subject turn] | [1-5] | [Why this signal matters — interpretive]

Failure conditions:

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Quote + Confidence present, no Rationale | Interpretive rationale per row | C-10 (Evidence confidence rated), C-16 (Evidence columns non-substitutable) |
| Rationale + Confidence present, no Quote | Verbatim SUBJECT source turn | C-14 (Arc claims quote-anchored), C-16 (Evidence columns non-substitutable) |
| Confidence only | Both Quote and Rationale | C-10, C-14, C-16 |
| Rationale restates Quote | Interpretive content distinct from quote | C-10 (Rationale must answer "why does this signal matter?") |
| Architectural column replaces Quote or Rationale | Non-substitutable base column | C-16 (Phase/Theme columns do not substitute for Quote or Rationale) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block:
- Current assumption about TOPIC: [state explicitly]
- Confidence: [1-5]
- What would change this assumption: [named condition]

Transcript (minimum 3 turns):

Q1: [Opening question]
A1: [Incumbent response]

Q2: [Follow-up targeting blind spot]
A2: [Incumbent response]

Q3: [Pressure question]
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
| T-1 | [Tension] | IE-1: "[exact quote]" |
| T-2 | [Tension] | IE-2: "[exact quote]" |

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

Q1: [Opening]
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

Q1: [Opening]
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
Column Policy. Do not proceed if any column is missing from any row.

Pattern (2-3 sentences): [Pattern across all evidence]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent vs. subject] | IE-#, HE-# | [Stakes] |
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

Prior signal (SKEPTIC S-01): [Role-grounded resistance established by S-01]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned
relative to the SKEPTIC prior]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — one sentence]

Prior Assumption Revisited:
Before: [Exact restatement of incumbent assumption]
After: [Revised assumption]
Delta: [What changed and why]
```

---

## V-05: All Axes — Full Ceiling (C-18 + C-19, maximum enforcement)

**Axis:** All five axes simultaneously.
**Hypothesis:** All five axes combined with SKEPTIC-first ordering, skeptic-prior Arc framing, prose-itemized criterion-ID failure statements in both blocks, maximum phase-gate enforcement, and the additional failure condition for symmetric Arc framing with SKEPTIC-first structure achieves 145/145.

```
PROVE-INTERVIEW PROMPT — V-05 (all axes, full R5 ceiling — C-18 + C-19 + maximum enforcement)

You are running a structured stakeholder interview to surface signal about [TOPIC].
Ceiling: 145. Target: 145 (all axes; maximum enforcement of all criteria through C-19).

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

SKEPTIC-FIRST REQUIREMENT: S-01 must be the SKEPTIC. S-02 must be the CHAMPION. This is not
cosmetic. The SKEPTIC interview establishes resistance as the prior signal. The CHAMPION
interview is the evidence against or for that prior. Inverting this order eliminates the
causal structure of the arc.

| ID | Role / Title | Domain | Disposition |
|----|-------------|--------|-------------|
| S-01 | [Role — the SKEPTIC] | [Domain] | SKEPTIC |
| S-02 | [Role — the CHAMPION] | [Domain] | CHAMPION |

DISPOSITION REQUIREMENT:
Every human subject roster entry must include an explicit Disposition column value (SKEPTIC or
CHAMPION) declared before any transcript begins. Inferred disposition is not sufficient.

Per-condition failure statements:
- No SKEPTIC label in roster: FAILS C-11 (Disposition arc structured — arc requires both
  poles declared) and FAILS C-17 (Roster-level disposition labels — every human subject
  requires an explicit per-subject label before transcripts begin)
- No CHAMPION label in roster: FAILS C-11 (Disposition arc structured — arc requires both
  poles declared) and FAILS C-17 (Roster-level disposition labels — every human subject
  requires an explicit per-subject label before transcripts begin)
- Roster entry with no Disposition column value: FAILS C-17 (every human subject requires
  explicit per-subject label before transcripts begin — absence of label on any single entry
  fails the criterion regardless of whether other entries have labels)
- Disposition inferred from synthesis-level arc analysis but absent from this table: FAILS
  C-17 (C-11 is the floor — the arc may appear in synthesis; C-17 is the ceiling — the
  per-subject label must appear at roster level before any transcript begins; synthesis-level
  inference does not retroactively satisfy roster-level declaration)
- CHAMPION declared as S-01: FAILS C-18 (Skeptic-first roster ordering — the SKEPTIC must
  appear as S-01 to establish resistance as the prior signal; reversing the order eliminates
  the causal structure that C-18 requires)
- SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18 (C-18
  requires both structural ordering and prior-signal framing simultaneously; structural
  ordering without skeptic-prior Arc framing satisfies only half the criterion)

COLUMN POLICY for Human Evidence Pulls (HE-#):
Each evidence row must contain exactly four columns: Signal | Quote | Confidence | Rationale.
Quote = verbatim subject turn (not summarized, not paraphrased). Rationale = interpretive
statement explaining why this signal matters to the topic decision (not a restatement of the
quote). Confidence = rated 1-5 with explicit numeric value. All four columns must coexist
simultaneously in every row.

Per-condition failure statements:
- Table has Quote + Confidence but no Rationale: FAILS C-10 (Evidence confidence rated —
  a confidence score without accompanying rationale cannot be evaluated for basis) and FAILS
  C-16 (Evidence columns non-substitutable — Quote does not substitute for Rationale; both
  must coexist simultaneously in the same row)
- Table has Rationale + Confidence but no Quote: FAILS C-14 (Arc claims quote-anchored —
  rationale claims must be grounded in verbatim subject language) and FAILS C-16 (Evidence
  columns non-substitutable — Rationale does not substitute for Quote; both must coexist
  simultaneously in the same row)
- Table has Confidence only: FAILS C-10 (no rationale basis), FAILS C-14 (no quote
  grounding), and FAILS C-16 (both Quote and Rationale absent — the non-substitutability
  criterion is violated at maximum severity when both base columns are absent)
- Rationale restates the Quote: FAILS C-10 (Rationale must answer "why does this signal
  matter to the feature decision?" — paraphrasing the quote does not constitute interpretation;
  the Rationale column exists to carry evaluative content that the Quote column cannot carry)
- Architectural addition placed in position that removes Quote or Rationale: FAILS C-16
  (adding a column such as Phase, Theme, or Category is permitted only if it supplements the
  four required columns; any architectural addition that displaces Quote or Rationale from
  any row violates the non-substitutability rule regardless of the addition's descriptive value)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: INCUMBENT INTERVIEW (AI-conducted, prior to all human sessions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prior knowledge block (complete in full before transcript begins):
- Current assumption about TOPIC: [state explicitly — this will be revisited in Step 3]
- Confidence in assumption: [1-5]
- What would change this assumption: [named condition — specific, not generic]

Transcript (minimum 3 turns — Q from interviewer, A from incumbent):

Q1: [Opening question probing incumbent's core assumption about TOPIC — grounded in the
    assumption stated above]
A1: [Incumbent response — full, role-grounded, not a summary]

Q2: [Follow-up targeting the named blind spot from the roster — asks what the incumbent
    cannot see from their position]
A2: [Incumbent response — reveals internal tension or confirms assumption]

Q3: [Pressure question — specifically asks what evidence or condition would change their
    stated position]
A3: [Incumbent response — surfaces the threshold condition that human interviews will test]

Surprise (one sentence): [What emerged in the incumbent interview that was not anticipated
given the prior knowledge block stated above?]

Incumbent Evidence Pull:

| IE-# | Claim | Quote | Confidence | Rationale |
|------|-------|-------|------------|-----------|
| IE-1 | [Claim extracted from incumbent transcript] | "[Verbatim quote from A1, A2, or A3 — exact words]" | [1-5] | [Why this claim matters as signal for the topic decision] |
| IE-2 | [Second claim — distinct from IE-1] | "[Verbatim quote — exact words]" | [1-5] | [Interpretive rationale — not a restatement of the quote] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1b: TENSION LOG (derived from incumbent evidence — populated before human interviews)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| T-# | Tension | Source |
|-----|---------|--------|
| T-1 | [Tension between two incumbent claims or between a claim and known external signal — named specifically] | IE-1: "[exact quote — must match IE-1 Quote column character-for-character]" |
| T-2 | [Second tension — may span incumbent claim and anticipated human-interview gap] | IE-2: "[exact quote — must match IE-2 Quote column character-for-character]" |

Tension source quotes must match the Quote column of the referenced IE row exactly.
Paraphrasing in the Source column fails the traceability requirement.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: HUMAN INTERVIEWS — SKEPTIC-FIRST SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Interview subjects in declared roster order: S-01 (SKEPTIC) before S-02 (CHAMPION).
The SKEPTIC interview establishes the prior signal. The CHAMPION interview is the evidence
against or for that prior. Do not reorder. Do not conduct both simultaneously.

--- S-01 (SKEPTIC) ---

Prior knowledge block (complete before transcript):
- What S-01 knows about TOPIC: [domain-grounded — specific to S-01's role]
- S-01's expected resistance point: [named explicitly before transcript begins]
- What would shift S-01's position: [named threshold — specific, not generic]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-01's framing of TOPIC without leading toward resistance]
A1: [S-01 response — role-grounded resistance or concern, full response]

Q2: [Probe the specific resistance point named in the prior knowledge block above]
A2: [S-01 response — deepens or qualifies resistance with specifics]

Q3: [Contrast question — explicitly reference the incumbent assumption from Step 1 and
    ask S-01 to react to it]
Q3 contrast note: This Q3 contrast references the incumbent assumption stated in Step 1
prior knowledge block. The contrast must be explicit, not implied.
A3: [S-01 response — direct tension with incumbent position, full response]

Surprise (one sentence): [What S-01 said that was not anticipated given their declared
SKEPTIC disposition and named resistance point?]

S-01 Evidence Pull:

| HE-# | Signal | Quote | Confidence | Rationale |
|------|--------|-------|------------|-----------|
| HE-1 | [Signal from S-01 transcript] | "[Verbatim S-01 quote — exact words from A1, A2, or A3]" | [1-5] | [Why this signal matters to the topic decision — interpretive, not a restatement] |
| HE-2 | [Second signal from S-01] | "[Verbatim S-01 quote — exact words]" | [1-5] | [Interpretive rationale distinct from quote content] |

--- S-02 (CHAMPION) ---

Prior knowledge block (complete before transcript):
- What S-02 knows about TOPIC: [domain-grounded — specific to S-02's role]
- S-02's expected advocacy point: [named explicitly before transcript begins]
- What would complicate S-02's position: [named threshold — specific, not generic]

Transcript (minimum 3 turns):

Q1: [Opening — invite S-02's framing of TOPIC without leading toward advocacy]
A1: [S-02 response — role-grounded advocacy or enthusiasm, full response]

Q2: [Probe the specific advocacy point named in the prior knowledge block above]
A2: [S-02 response — deepens or qualifies advocacy with specifics]

Q3: [Contrast question — explicitly reference a specific claim from S-01's transcript
    and ask S-02 to respond to it]
Q3 contrast note: This Q3 contrast references a named specific claim from S-01's transcript
above (not a generic reference to "the skeptic's concerns"). The claim must be identified
by quoting or closely paraphrasing S-01's language.
A3: [S-02 response — direct engagement with the named SKEPTIC claim, full response]

Surprise (one sentence): [What S-02 said that was not anticipated given their declared
CHAMPION disposition and named advocacy point?]

S-02 Evidence Pull:

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
Name the convergent thread and the persistent tension. Do not summarize individual interviews —
synthesize across them.]

Critical Contradiction Table:

| Contradiction | IE/HE source | Stakes |
|---------------|-------------|--------|
| [Incumbent claim vs. human subject claim — named specifically] | IE-#, HE-# | [What is at risk if this contradiction is unresolved] |
| [S-01 SKEPTIC claim vs. S-02 CHAMPION claim — the core arc tension] | HE-#, HE-# | [What is at risk if this tension persists into implementation] |

Tension Resolution:
T-1: [How the human interviews resolved, deepened, or reframed T-1 — specific to HE references]
T-2: [How the human interviews resolved, deepened, or reframed T-2 — specific to HE references]

Inertia Verdict Matrix:

| Factor | Evidence | Verdict |
|--------|----------|---------|
| [Factor 1 — named specifically] | [HE-# or IE-# reference with brief quote] | PROCEED / PAUSE / ESCALATE |
| [Factor 2 — named specifically] | [HE-# or IE-# reference with brief quote] | PROCEED / PAUSE / ESCALATE |
| [Factor 3 — named specifically] | [HE-# or IE-# reference with brief quote] | PROCEED / PAUSE / ESCALATE |

Arc Signal (SKEPTIC-prior framing — required):
Skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence.
This is not a symmetric comparison between two equal voices. The SKEPTIC established the
resistance prior. The CHAMPION responded to that prior. The arc conclusion must reflect
the causal sequence: prior -> response -> resolution.

Prior signal (SKEPTIC S-01): [Role-grounded resistance established by S-01 — what they
resisted and why, stated as the prior that the CHAMPION must respond to. This is grounded
in HE-1 and HE-2.]

Subsequent evidence (CHAMPION S-02): [What S-02 confirmed, complicated, or overturned
relative to the SKEPTIC prior stated above. This is grounded in HE-3 and HE-4. The
framing must be relative to the prior — not a standalone CHAMPION summary.]

Arc conclusion: [CONVERGENCE / CONTRADICTION / PARTIAL — with one sentence explaining the
dominant signal that emerged from the skeptic-prior framing. The conclusion must name what
the SKEPTIC established and how the CHAMPION responded to it.]

Grounding check: Arc conclusion references HE-# from both S-01 and S-02 evidence pulls.
If the conclusion references only one subject, it is not an arc — revise before filing.

Prior Assumption Revisited:
Before: [Restate the incumbent assumption from Step 1 prior knowledge block — exact
language, not a summary]
After: [What the assumption should be revised to, given all evidence from IE-# and HE-#
combined — this is the updated signal position]
Delta: [One sentence naming specifically what changed (not that evidence was gathered) and
why the change is warranted by the evidence]
```

---

```json
{
  "file": "prove-interview-variations-R5-2026-03-14.md",
  "round": 5,
  "skill": "prove-interview",
  "date": "2026-03-14",
  "ceiling": 145,
  "variations": [
    {"id": "V-01", "axes": ["role-sequence"], "c18": true, "c19": false, "target": 140},
    {"id": "V-02", "axes": ["lifecycle-emphasis"], "c18": false, "c19": true, "target": 140},
    {"id": "V-03", "axes": ["both-minimal"], "c18": true, "c19": true, "target": 145},
    {"id": "V-04", "axes": ["output-format-tabular"], "c18": true, "c19": true, "target": 145},
    {"id": "V-05", "axes": ["all-axes"], "c18": true, "c19": true, "target": 145}
  ],
  "new_criteria": ["C-18", "C-19"],
  "baseline": "R4-V03-V05-135/135",
  "r4_delta": "C-18 structural+framing; C-19 criterion-ID failure statements in both compliance blocks"
}
```
