Written to `simulations/quest/variations/prove-interview-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — prove-interview

Five complete prompts targeting **C-16** and **C-17**, the two new v4 criteria. Ceiling: 135.

---

### Variation Map

| V | Axis | C-16 fix | C-17 fix | Absent by design | Predicted |
|---|------|----------|----------|-----------------|-----------|
| V-01 | Phrasing register | NO | YES | C-16 | 128/135 |
| V-02 | Lifecycle emphasis | YES | NO | C-17 | 128/135 |
| V-03 | Role sequence | YES | YES | — | 135/135 |
| V-04 | Phrasing register + lifecycle | YES | YES | — | 135/135 |
| V-05 | All five axes | YES | YES | — | 135/135 |

---

### What each variation does

**V-01 (phrasing register — C-17 only):** Adds a formal `DISPOSITION REQUIREMENT` block to the Human Subjects roster. Requires at least one `CHAMPION` and one `SKEPTIC` label per-subject before any transcript begins. Evidence Pull tables deliberately retain `Quote + Confidence` only — the Rationale column regression from R3 V-05 is preserved to isolate C-17.

**V-02 (lifecycle emphasis — C-16 only):** Adds an explicit `COLUMN POLICY` gate before the Evidence Pull instruction, stating the additive rule verbatim: adding Quote does not discharge Rationale; both are required simultaneously. Human Subjects roster uses freeform `positive/skeptical/neutral` only — no `CHAMPION`/`SKEPTIC` structural requirement.

**V-03 (role sequence — both fixes, SKEPTIC-first):** Both fixes applied. `S-01 = SKEPTIC`, `S-02 = CHAMPION`. SKEPTIC interviews before CHAMPION. Synthesis Arc Signal is restructured: skeptic resistance is the prior signal; champion confirmation-or-overturn is the evidence. Tests whether C-17 labels work sequence-independently.

**V-04 (phrasing register + lifecycle — both fixes, standard order):** The two R3 V-05 regressions corrected with two named blocks only — `DISPOSITION REQUIREMENT` (C-17) + `COLUMN POLICY` (C-16) — applied to the R3 V-05 architecture unchanged. Standard `CHAMPION → SKEPTIC` order. The minimal-fix hypothesis: if V-04 scores 135, no sequence change is needed.

**V-05 (all five axes — full R4 ceiling):** All fixes + SKEPTIC-first + Column Policy + Disposition Requirement + SKEPTIC-first Arc Signal framing + explicit phase-gate enforcement on every transition.

---

### Key structural changes across all variations that fix C-16

Evidence Pull schema changes from R3 V-05:
```
R3 V-05:  IE-# | Claim  | Quote | Confidence
R4 fixed: IE-# | Claim  | Quote | Confidence | Rationale
R4 fixed: HE-# | Signal | Quote | Confidence | Rationale
```

### Key structural changes across all variations that fix C-17

Human Subjects roster changes from R3 V-05:
```
R3 V-05:  | Subject | Role | Prior knowledge | ... | Stakeholder type | Current practice |
R4 fixed: | Subject | Role | Prior knowledge | ... | Stakeholder type | Current practice | Disposition |
```
Plus a named `DISPOSITION REQUIREMENT` block requiring ≥1 `CHAMPION` and ≥1 `SKEPTIC` before any interview begins.
ve.
2. **Does SKEPTIC-first ordering change synthesis arc dynamics?** V-03 inverts sequence. Does the
   Arc Signal section correctly reframe when skeptic resistance precedes champion advocacy?
3. **Is the two-regression fix (V-04) sufficient to reach 135/135 from R3 V-05?** V-04 applies only
   the two targeted corrections with no other changes. If V-04 scores 135, the fixes are sufficient
   and minimal.
4. **Does combining all five axes add measurable robustness or only complexity?** V-05 vs V-04 —
   if both score 135, all-axes integration provides no additional criterion coverage at the ceiling.

---

## V-01: Phrasing Register — Explicit Disposition Declaration (C-17 fix only)

**Axis:** Phrasing register (single-axis).
**Hypothesis:** A named DISPOSITION REQUIREMENT block in the Human Subjects roster section, requiring
at least one CHAMPION and one SKEPTIC label declared per-subject before any interview begins, is
sufficient for C-17 PASS independently of Evidence table structure. Evidence Pull tables retain the
R3 V-05 column regression (Quote + Confidence, no Rationale) to isolate the C-17 fix. C-16 absent by
design — C-17 single-axis isolation.

---

```
# prove-interview

---

## STEP 0 — ROSTER

Declare the complete roster before beginning any interview.

**Subject 0 — The Incumbent**
| Field | Value |
|-------|-------|
| Role | Incumbent: {{incumbent_name}} — the solution currently in place |
| Prior knowledge | Speaks in the vocabulary of teams that have built workflows around it: reliability claims, integration arguments, switching-cost calculations, institutional familiarity, ecosystem lock-in |
| Stakeholder type | Non-human baseline |
| Current practice | [The specific daily function teams invoking {{incumbent_name}} rely on — not "it works well" but the actual workflow step that would need a replacement path before switching becomes viable] |

**Human Subjects**
| Subject | Role / Title | Prior knowledge | Knowledge gaps | Stakeholder type | Current practice with Incumbent | Disposition |
|---------|-------------|----------------|----------------|-----------------|----------------------------------|-------------|
| S-01 | [job title] | [what they know about the domain and {{topic}}] | [what they don't know] | [technical / business / buyer / user] | [what they use {{incumbent_name}} for, how long, how embedded — specific function, not general disposition] | **CHAMPION** |
| S-02 | [job title — non-overlapping with S-01] | [what they know] | [what they don't know] | [must differ from S-01] | [current practice with {{incumbent_name}} — must differ meaningfully from S-01's] | **SKEPTIC** |

---

**DISPOSITION REQUIREMENT:**

The Disposition column must be filled for every human subject before any interview begins. Labels
are permanent — they reflect the declared stance going in, not the outcome.

- At least one subject must be labeled **CHAMPION** (advocate, supporter, or positive adopter of
  the proposed approach — not of {{incumbent_name}}).
- At least one subject must be labeled **SKEPTIC** (critic, resistor, or doubter of the proposed
  approach).
- NEUTRAL is permitted for additional subjects only when at least one CHAMPION and one SKEPTIC are
  already declared.
- A roster with no explicit CHAMPION label fails the structural requirement.
- A roster with no explicit SKEPTIC label fails the structural requirement.
- Disposition inferrable from synthesis-level arc analysis but absent from this roster table does
  not satisfy this requirement.

---

Minimum 2 human subjects from non-overlapping stakeholder types. Subject 0 (The Incumbent) does
not count toward the human subject minimum. Declare all roster entries before beginning any
interview.

---

## STEP 1 — INCUMBENT INTERVIEW

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
{{incumbent_name}} has been in place since [time]. Teams that depend on it justify it with:
[claim 1], [claim 2], [claim 3]. Primary switching-cost argument: [argument]. Rough edge sometimes
acknowledged internally: [limitation].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "What does a team that depends on {{incumbent_name}}
actually do in their workflow that would require a replacement path before moving away? Walk me
through the specific daily function." This is a neutral question about current practice — not about
features, not about evaluation.]
SUBJECT: [The Incumbent describes the actual daily workflow dependency — specific, grounded in what
teams do rather than what the Incumbent claims to offer; switching-cost language rooted in workflow
interruption; first-person as the voice of teams that trust it; vocabulary distinguishable from any
human subject without the role label]

INTERVIEWER: [question — probe a specific claimed strength that surfaced in Q1 with a concrete
scenario]
SUBJECT: [Incumbent defends or qualifies in-voice; word choice must be distinguishable from all
human subjects]

INTERVIEWER: [question — ask what would need to be true for a team to move away from it]
SUBJECT: [switching-cost framing required; at least one team assumption being carried without
examination should surface here]

Minimum 3 INTERVIEWER turns. Q1 must come before any feature or evaluation question. The Incumbent
voice must be distinguishable from all human subjects without the role label.

**Surprise — Incumbent:**
One SUBJECT turn where the Incumbent's answer revealed a team assumption being carried without
examination. Quote the SUBJECT turn verbatim. State what assumption was surfaced.

**Evidence Pull — Incumbent:**
| IE-# | Claim | Quote from SUBJECT turn | Confidence |
|------|-------|------------------------|------------|
| IE-1 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW |
| IE-2 | [claim label] | "[verbatim Incumbent SUBJECT quote]" | HIGH / MEDIUM / LOW |

Minimum 2 rows. Confidence required on every row. Quote column must contain verbatim SUBJECT text —
not paraphrase, not summary.

---

## STEP 1b — TENSION LOG

Promote minimum 2 rows from the Incumbent Evidence Pull to the Tension Log. The Source quote in
each entry IS the verbatim Incumbent SUBJECT turn already captured in the corresponding IE-# row —
do not re-extract, do not paraphrase, do not rephrase.

| T-# | IE-# | Tension item (the claim to be tested) | Source quote (verbatim — must match IE-# Quote column) | Status |
|-----|------|---------------------------------------|--------------------------------------------------------|--------|
| T-1 | IE-1 | [tension framing of IE-1 — phrased as a testable proposition human subjects can confirm or dispute] | "[verbatim Incumbent SUBJECT quote — identical to IE-1 Quote column]" | OPEN |
| T-2 | IE-2 | [tension framing of IE-2] | "[verbatim Incumbent SUBJECT quote — identical to IE-2 Quote column]" | OPEN |

Do not begin Step 2 until the Tension Log has at least 2 entries and every Source quote matches
its IE-# row.

---

## STEP 2 — HUMAN INTERVIEWS

For each human subject in the roster, in roster order (CHAMPION before SKEPTIC unless otherwise
declared):

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
[Subject role] has [used / evaluated / observed] {{incumbent_name}} for [time]. Current practice:
[the specific workflow function from the Roster]. Disposition: [CHAMPION / SKEPTIC / NEUTRAL]
because [grounded reason — a constraint, past experience, or workflow dependency — not a stance].
Primary concern about switching: [concern].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "Walk me through what you actually do with
{{incumbent_name}} in a typical workflow cycle. I want to understand what you do today, before we
talk about anything else." This is a neutral question about current practice — not about features,
not about evaluation.]
SUBJECT: [answer — describes actual workflow, specific enough that another role with a different
current practice could not give the same Q1 answer; references the Current practice declared in
the Roster; vocabulary and domain artifacts reflect this specific role]

INTERVIEWER: [follow-up that probes or builds on a specific detail from the Q1 answer — grounded
in the workflow the subject just described]
SUBJECT: [answer — role-specific vocabulary and concerns; distinguishable from the Incumbent and
from all other human subjects without the role label]

INTERVIEWER: [question that directly names at least one Tension Log entry: "T-[N] — the current
approach claims [tension item]. Does that match what you actually encounter in your context?"]
SUBJECT: [answer — addresses T-N by name; confirms, disputes, or qualifies the claim; grounded in
their actual current practice from Q1]

[TENSION LOG UPDATE: after this interview, record the verbatim SUBJECT turn for each T-entry
addressed. Update Status to ADDRESSED. Leave OPEN entries not addressed. Do not advance to the
next subject until updates are recorded.]

Minimum 3 INTERVIEWER turns per subject. Q1 must be the opening question — a current-practice
question before any feature or evaluation question. At least one subsequent turn must directly name
a Tension Log entry by T-number.

**Q1 contrast note** (written after the interview transcript, before Surprise):
State whether the subject's Q1 answer is consistent with their Roster current practice declaration.
A Q1 answer that ignores or contradicts the declared current practice is a grounding failure —
flag it explicitly here.

**Surprise — [Subject role]:**
One SUBJECT turn that contradicted the prior assumption stated in the Roster for this subject.
Quote the SUBJECT turn verbatim. State what was assumed (cite the Roster entry) and what was
revealed.

**Evidence Pull — [Subject role]:**
| HE-# | Signal | Quote from SUBJECT turn | Confidence |
|------|--------|------------------------|------------|
| HE-1 | [signal label] | "[verbatim SUBJECT quote — not paraphrased]" | HIGH / MEDIUM / LOW |
| HE-2 | [signal label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW |

Minimum 2 rows. Confidence required on every row. Quote column must contain verbatim SUBJECT text.

---

## STEP 3 — SYNTHESIS

Do not begin synthesis until: (a) all human interviews complete, (b) all Tension Log entries
updated, (c) all Evidence Pulls populated with Confidence on every row.

Every synthesis item — every pattern claim, Critical Contradiction claim, Tension resolution entry,
Inertia Verdict Matrix row, Arc Signal claim, and assumption update — must cite a direct quote from
a SUBJECT turn. No synthesis claim without a source. No inference without a turn.

### Pattern
At least one signal that appeared across two or more subjects. Cite a verbatim SUBJECT turn per
subject. The Incumbent is eligible.

### Critical Contradiction
The single most significant contradiction in this session. Not the most dramatic disagreement —
the one whose resolution most changes the answer to the interview question. Both sides must be
cited verbatim.

| Field | Value |
|-------|-------|
| Subject A | [role] |
| Subject A position | [what Subject A asserted] |
| Quote A | "[verbatim SUBJECT turn from Subject A — not paraphrased, not summarized]" |
| Subject B | [role] |
| Subject B position | [what Subject B asserted — the position in conflict with Subject A] |
| Quote B | "[verbatim SUBJECT turn from Subject B — not paraphrased, not summarized]" |
| Evidential weight | [What this contradiction confirms, undermines, or leaves unresolved about the interview question. Why does it outrank other contradictions? Not the most dramatic — the most consequential for the answer.] |

Additional contradictions (no Quote A / Quote B requirement):
- [Contradiction 2: subjects and claim in tension]
- [Contradiction 3: subjects and claim in tension]

### Tension Resolution
| T-# | IE-# | Final status | Resolution quote (verbatim SUBJECT turn) |
|-----|------|-------------|------------------------------------------|
| T-1 | IE-1 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-1 directly — OPEN" |
| T-2 | IE-2 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-2 directly — OPEN" |

### Inertia Verdict Matrix
Adjudicate each Incumbent Evidence Pull row against human subject testimony.

| IE-# | Incumbent claim | Verdict | Human SUBJECT turn (verbatim) |
|------|----------------|---------|-------------------------------|
| IE-1 | [claim label from IE-1] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-1 — UNADDRESSED" |
| IE-2 | [claim label from IE-2] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-2 — UNADDRESSED" |

Every Incumbent Evidence Pull row must appear. No row may be blank or omitted.

### Arc Signal
State whether convergence or contradiction was the dominant arc signal across this session.

- **Dominant signal**: CONVERGENCE / CONTRADICTION / INCONCLUSIVE
- **Evidence per subject** (cite one verbatim SUBJECT turn per subject that evidences the
  dominant signal):
  - Subject 0 (Incumbent): "[verbatim SUBJECT turn]"
  - S-01 (CHAMPION): "[verbatim SUBJECT turn]"
  - S-02 (SKEPTIC): "[verbatim SUBJECT turn]"
- **CHAMPION/SKEPTIC arc**: Did the CHAMPION and SKEPTIC dispositions converge or remain in
  contradiction? Convergence despite SKEPTIC resistance is strong signal — cite the SKEPTIC turn
  that shows role-grounded, not positional, resistance. A SKEPTIC whose concern is "change is
  hard" without grounding in declared current practice is a grounding failure — flag it.
- **Skeptic assessment**: Did the SKEPTIC subject's resistance appear role-grounded (rooted in
  declared current practice and domain constraints) or positional (generic resistance not grounded
  in workflow)? Cite one SUBJECT turn.

### Prior Assumption Revisited
One Roster assumption that the interviews revised. Quote the SUBJECT turn that caused the revision.
State what the Roster assumed and what is now understood.
```

---

## V-02: Lifecycle Emphasis — Column Policy Gate (C-16 fix only)

**Axis:** Lifecycle emphasis (single-axis).
**Hypothesis:** An explicit COLUMN POLICY gate, stated as a named section before the Evidence Pull
instruction, enforces the additive rule (both Quote and Rationale required simultaneously) reliably
enough to produce C-16 PASS without any change to the roster disposition structure. Human Subjects
table retains freeform disposition field ("positive/skeptical/neutral") without CHAMPION/SKEPTIC
requirement — C-17 absent by design.

---

```
# prove-interview

---

## STEP 0 — ROSTER

Declare the complete roster before beginning any interview.

**Subject 0 — The Incumbent**
| Field | Value |
|-------|-------|
| Role | Incumbent: {{incumbent_name}} — the solution currently in place |
| Prior knowledge | Speaks in the vocabulary of teams that have built workflows around it: reliability claims, integration arguments, switching-cost calculations, institutional familiarity, ecosystem lock-in |
| Stakeholder type | Non-human baseline |
| Current practice | [The specific daily function teams invoking {{incumbent_name}} rely on — not "it works well" but the actual workflow step that would need a replacement path before switching becomes viable] |

**Human Subjects**
| Subject | Role / Title | Prior knowledge | Knowledge gaps | Stakeholder type | Current practice with Incumbent | Disposition |
|---------|-------------|----------------|----------------|-----------------|----------------------------------|-------------|
| S-01 | [job title] | [what they know about the domain and {{topic}}] | [what they don't know] | [technical / business / buyer / user] | [what they use {{incumbent_name}} for, how long, how embedded — specific function] | [positive / skeptical / neutral] |
| S-02 | [job title — non-overlapping with S-01] | [what they know] | [what they don't know] | [must differ from S-01] | [current practice — must differ meaningfully from S-01's] | [positive / skeptical / neutral] |

Minimum 2 human subjects from non-overlapping stakeholder types. Subject 0 (The Incumbent) does
not count toward the human subject minimum. Declare all roster entries before beginning any
interview.

---

## STEP 1 — INCUMBENT INTERVIEW

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
{{incumbent_name}} has been in place since [time]. Teams that depend on it justify it with:
[claim 1], [claim 2], [claim 3]. Primary switching-cost argument: [argument]. Rough edge sometimes
acknowledged internally: [limitation].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "What does a team that depends on {{incumbent_name}}
actually do in their workflow that would require a replacement path before moving away? Walk me
through the specific daily function." This is a neutral question about current practice — not about
features, not about evaluation.]
SUBJECT: [The Incumbent describes the actual daily workflow dependency — specific, grounded in what
teams do; switching-cost language rooted in workflow interruption; first-person as the voice of
teams that trust it; vocabulary distinguishable from any human subject without the role label]

INTERVIEWER: [question — probe a specific claimed strength that surfaced in Q1 with a concrete
scenario]
SUBJECT: [Incumbent defends or qualifies in-voice; word choice must be distinguishable from all
human subjects]

INTERVIEWER: [question — ask what would need to be true for a team to move away from it]
SUBJECT: [switching-cost framing required; at least one team assumption being carried without
examination should surface here]

Minimum 3 INTERVIEWER turns. Q1 must come before any feature or evaluation question.

**Surprise — Incumbent:**
One SUBJECT turn where the Incumbent's answer revealed a team assumption being carried without
examination. Quote the SUBJECT turn verbatim. State what assumption was surfaced.

---

### COLUMN POLICY — Evidence Pull Tables

The following policy applies to every Evidence Pull table in this skill output, including the
Incumbent Evidence Pull, all Human Subject Evidence Pulls, and any supplemental evidence tables:

1. **Required columns**: Every Evidence Pull table must carry all four columns simultaneously:
   `Signal / Quote / Confidence / Rationale`
   (or `Claim / Quote / Confidence / Rationale` for the Incumbent table).

2. **Quote and Rationale are non-substitutable.** Adding the Quote column does not remove the
   Rationale requirement. Adding the Rationale column does not remove the Quote requirement.
   Both serve different purposes: Quote is source-verification (the verbatim SUBJECT turn the
   signal was extracted from); Rationale is signal interpretation (why this signal matters for
   the interview question). A table with Quote and Confidence but no Rationale is incomplete.
   A table with Rationale and Confidence but no Quote is incomplete.

3. **Column additions are additive.** Architectural changes (Incumbent framing, coupling,
   baseline framing) may add structural columns. No architectural change removes the Quote or
   Rationale columns. Additional columns are added alongside the four required columns, not
   in place of them.

4. **Rationale format**: one sentence per row answering "why does this signal matter for
   [interview question]?" — not a paraphrase of the Quote.

This policy applies unconditionally. It cannot be satisfied at the synthesis level. Apply it at
the individual table level.

---

**Evidence Pull — Incumbent:**
| IE-# | Claim | Quote from SUBJECT turn | Confidence | Rationale |
|------|-------|------------------------|------------|-----------|
| IE-1 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW | [one-line rationale — why this claim matters for the interview question] |
| IE-2 | [claim label] | "[verbatim Incumbent SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All four columns required on every row per Column Policy.

---

## STEP 1b — TENSION LOG

Promote minimum 2 rows from the Incumbent Evidence Pull to the Tension Log. The Source quote in
each entry IS the verbatim Incumbent SUBJECT turn already captured in the corresponding IE-# row —
do not re-extract, do not paraphrase, do not rephrase.

| T-# | IE-# | Tension item (the claim to be tested) | Source quote (verbatim — must match IE-# Quote column) | Status |
|-----|------|---------------------------------------|--------------------------------------------------------|--------|
| T-1 | IE-1 | [tension framing of IE-1 — phrased as a testable proposition human subjects can confirm or dispute] | "[verbatim Incumbent SUBJECT quote — identical to IE-1 Quote column]" | OPEN |
| T-2 | IE-2 | [tension framing of IE-2] | "[verbatim Incumbent SUBJECT quote — identical to IE-2 Quote column]" | OPEN |

Do not begin Step 2 until the Tension Log has at least 2 entries and every Source quote matches
its IE-# row.

---

## STEP 2 — HUMAN INTERVIEWS

For each human subject in the roster:

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
[Subject role] has [used / evaluated / observed] {{incumbent_name}} for [time]. Current practice:
[the specific workflow function from the Roster]. Disposition: [positive / skeptical / neutral]
because [grounded reason — a constraint, past experience, or workflow dependency — not a stance].
Primary concern about switching: [concern].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "Walk me through what you actually do with
{{incumbent_name}} in a typical workflow cycle. I want to understand what you do today, before we
talk about anything else." This is a neutral question about current practice — not about features,
not about evaluation.]
SUBJECT: [answer — describes actual workflow, specific enough that another role with a different
current practice could not give the same Q1 answer; vocabulary and domain artifacts reflect this
specific role]

INTERVIEWER: [follow-up that probes or builds on a specific detail from the Q1 answer — grounded
in the workflow the subject just described]
SUBJECT: [answer — role-specific vocabulary and concerns; distinguishable from the Incumbent and
from all other human subjects without the role label]

INTERVIEWER: [question that directly names at least one Tension Log entry: "T-[N] — the current
approach claims [tension item]. Does that match what you actually encounter in your context?"]
SUBJECT: [answer — addresses T-N by name; confirms, disputes, or qualifies the claim; grounded in
their actual current practice from Q1]

[TENSION LOG UPDATE: after this interview, record the verbatim SUBJECT turn for each T-entry
addressed. Update Status to ADDRESSED. Leave OPEN entries not addressed. Do not advance to the
next subject until updates are recorded.]

Minimum 3 INTERVIEWER turns per subject. Q1 must be the opening question. At least one subsequent
turn must directly name a Tension Log entry by T-number.

**Q1 contrast note** (written after the interview transcript, before Surprise):
State whether the subject's Q1 answer is consistent with their Roster current practice declaration.
A Q1 answer that ignores or contradicts the declared current practice is a grounding failure —
flag it explicitly here.

**Surprise — [Subject role]:**
One SUBJECT turn that contradicted the prior assumption stated in the Roster for this subject.
Quote the SUBJECT turn verbatim. State what was assumed (cite the Roster entry) and what was
revealed.

**Evidence Pull — [Subject role]:**
| HE-# | Signal | Quote from SUBJECT turn | Confidence | Rationale |
|------|--------|------------------------|------------|-----------|
| HE-1 | [signal label] | "[verbatim SUBJECT quote — not paraphrased]" | HIGH / MEDIUM / LOW | [one-line rationale — why this signal matters for the interview question] |
| HE-2 | [signal label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All four columns required on every row per Column Policy.

---

## STEP 3 — SYNTHESIS

Do not begin synthesis until: (a) all human interviews complete, (b) all Tension Log entries
updated, (c) all Evidence Pulls populated with all four columns on every row.

Every synthesis item — every pattern claim, Critical Contradiction claim, Tension resolution entry,
Inertia Verdict Matrix row, Arc Signal claim, and assumption update — must cite a direct quote from
a SUBJECT turn. No synthesis claim without a source. No inference without a turn.

### Pattern
At least one signal that appeared across two or more subjects. Cite a verbatim SUBJECT turn per
subject. The Incumbent is eligible.

### Critical Contradiction
The single most significant contradiction in this session. Not the most dramatic disagreement —
the one whose resolution most changes the answer to the interview question. Both sides must be
cited verbatim.

| Field | Value |
|-------|-------|
| Subject A | [role] |
| Subject A position | [what Subject A asserted] |
| Quote A | "[verbatim SUBJECT turn from Subject A — not paraphrased, not summarized]" |
| Subject B | [role] |
| Subject B position | [what Subject B asserted — the position in conflict with Subject A] |
| Quote B | "[verbatim SUBJECT turn from Subject B — not paraphrased, not summarized]" |
| Evidential weight | [What this contradiction confirms, undermines, or leaves unresolved about the interview question. Why does it outrank other contradictions?] |

Additional contradictions (no Quote A / Quote B requirement):
- [Contradiction 2: subjects and claim in tension]
- [Contradiction 3: subjects and claim in tension]

### Tension Resolution
| T-# | IE-# | Final status | Resolution quote (verbatim SUBJECT turn) |
|-----|------|-------------|------------------------------------------|
| T-1 | IE-1 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-1 directly — OPEN" |
| T-2 | IE-2 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-2 directly — OPEN" |

### Inertia Verdict Matrix
| IE-# | Incumbent claim | Verdict | Human SUBJECT turn (verbatim) |
|------|----------------|---------|-------------------------------|
| IE-1 | [claim label from IE-1] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-1 — UNADDRESSED" |
| IE-2 | [claim label from IE-2] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-2 — UNADDRESSED" |

Every Incumbent Evidence Pull row must appear. No row may be blank or omitted.

### Arc Signal
State whether convergence or contradiction was the dominant arc signal across this session.

- **Dominant signal**: CONVERGENCE / CONTRADICTION / INCONCLUSIVE
- **Evidence per subject** (cite one verbatim SUBJECT turn per subject that evidences the
  dominant signal):
  - Subject 0 (Incumbent): "[verbatim SUBJECT turn]"
  - S-01: "[verbatim SUBJECT turn]"
  - S-02: "[verbatim SUBJECT turn]"
- **Skeptic assessment**: Did any subject's resistance appear role-grounded (rooted in their
  declared current practice) or positional (claiming resistance without behavioral grounding)?
  Cite one SUBJECT turn. A SUBJECT turn claiming skepticism that ignores the subject's declared
  current practice is a grounding failure — flag it.

### Prior Assumption Revisited
One Roster assumption that the interviews revised. Quote the SUBJECT turn that caused the revision.
State what the Roster assumed and what is now understood.
```

---

## V-03: Role Sequence — SKEPTIC-First Interview Order (both fixes)

**Axis:** Role sequence (single-axis on sequence; both C-16 and C-17 fixes applied as baseline).
**Hypothesis:** When the SKEPTIC subject interviews before the CHAMPION (S-01 = SKEPTIC, S-02 =
CHAMPION), the synthesis arc frames skeptic resistance as the prior signal and champion confirmation
as the revealing evidence. C-17 roster labels work correctly regardless of sequence direction.
C-16 column additive rule does not interact with sequence. Tests whether SKEPTIC-first ordering
changes Arc Signal dynamics compared to the standard CHAMPION-first order.

---

```
# prove-interview

---

## STEP 0 — ROSTER

Declare the complete roster before beginning any interview.

**Subject 0 — The Incumbent**
| Field | Value |
|-------|-------|
| Role | Incumbent: {{incumbent_name}} — the solution currently in place |
| Prior knowledge | Speaks in the vocabulary of teams that have built workflows around it: reliability claims, integration arguments, switching-cost calculations, institutional familiarity, ecosystem lock-in |
| Stakeholder type | Non-human baseline |
| Current practice | [The specific daily function teams invoking {{incumbent_name}} rely on — not "it works well" but the actual workflow step that would need a replacement path before switching becomes viable] |

**Human Subjects — SKEPTIC FIRST**
| Subject | Role / Title | Prior knowledge | Knowledge gaps | Stakeholder type | Current practice with Incumbent | Disposition |
|---------|-------------|----------------|----------------|-----------------|----------------------------------|-------------|
| S-01 | [job title — the SKEPTIC] | [what they know about the domain and {{topic}}] | [what they don't know] | [technical / business / buyer / user] | [what they use {{incumbent_name}} for — specific function] | **SKEPTIC** |
| S-02 | [job title — the CHAMPION, non-overlapping with S-01] | [what they know] | [what they don't know] | [must differ from S-01] | [current practice — must differ meaningfully from S-01's] | **CHAMPION** |

---

**DISPOSITION REQUIREMENT:**

The Disposition column must be filled for every human subject before any interview begins.

- At least one subject must be labeled **SKEPTIC** and must appear first in roster order (S-01).
- At least one subject must be labeled **CHAMPION**.
- Disposition labels are permanent — declared going in, not assigned at synthesis.
- A roster with no explicit SKEPTIC label fails the structural requirement.
- A roster with no explicit CHAMPION label fails the structural requirement.
- SKEPTIC-first ordering is required: the SKEPTIC subject must be S-01. This sets the
  resistance baseline that CHAMPION evidence must overcome or confirm.

---

Minimum 2 human subjects from non-overlapping stakeholder types. Subject 0 (The Incumbent) does
not count toward the human subject minimum. Declare all roster entries before beginning any
interview.

---

## STEP 1 — INCUMBENT INTERVIEW

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
{{incumbent_name}} has been in place since [time]. Teams that depend on it justify it with:
[claim 1], [claim 2], [claim 3]. Primary switching-cost argument: [argument]. Rough edge sometimes
acknowledged internally: [limitation].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "What does a team that depends on {{incumbent_name}}
actually do in their workflow that would require a replacement path before moving away? Walk me
through the specific daily function." This is a neutral question about current practice — not about
features, not about evaluation.]
SUBJECT: [The Incumbent describes the actual daily workflow dependency — specific, grounded in what
teams do; switching-cost language rooted in workflow interruption; first-person as the voice of
teams that trust it; vocabulary distinguishable from any human subject without the role label]

INTERVIEWER: [question — probe a specific claimed strength that surfaced in Q1 with a concrete
scenario]
SUBJECT: [Incumbent defends or qualifies in-voice; word choice must be distinguishable from all
human subjects]

INTERVIEWER: [question — ask what would need to be true for a team to move away from it]
SUBJECT: [switching-cost framing required; at least one team assumption being carried without
examination should surface here]

Minimum 3 INTERVIEWER turns. Q1 must come before any feature or evaluation question.

**Surprise — Incumbent:**
One SUBJECT turn where the Incumbent's answer revealed a team assumption being carried without
examination. Quote the SUBJECT turn verbatim. State what assumption was surfaced.

**Evidence Pull — Incumbent:**
| IE-# | Claim | Quote from SUBJECT turn | Confidence | Rationale |
|------|-------|------------------------|------------|-----------|
| IE-1 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW | [one-line rationale] |
| IE-2 | [claim label] | "[verbatim Incumbent SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All four columns (Claim, Quote, Confidence, Rationale) required on every row.
Quote and Rationale are both required simultaneously — adding Quote does not discharge Rationale.

---

## STEP 1b — TENSION LOG

Promote minimum 2 rows from the Incumbent Evidence Pull to the Tension Log.

| T-# | IE-# | Tension item (the claim to be tested) | Source quote (verbatim — must match IE-# Quote column) | Status |
|-----|------|---------------------------------------|--------------------------------------------------------|--------|
| T-1 | IE-1 | [tension framing of IE-1] | "[verbatim Incumbent SUBJECT quote — identical to IE-1 Quote column]" | OPEN |
| T-2 | IE-2 | [tension framing of IE-2] | "[verbatim Incumbent SUBJECT quote — identical to IE-2 Quote column]" | OPEN |

Do not begin Step 2 until the Tension Log has at least 2 entries.

---

## STEP 2 — HUMAN INTERVIEWS (SKEPTIC-FIRST SEQUENCE)

Interview subjects in roster order: S-01 (SKEPTIC) first, then S-02 (CHAMPION).

The SKEPTIC interview establishes the resistance baseline. The CHAMPION interview that follows
must be evaluated against that baseline — convergence between a role-grounded SKEPTIC and a
CHAMPION is strong signal; CHAMPION confirmation that does not account for the SKEPTIC's declared
resistance is a synthesis red flag.

For each human subject, in S-01 (SKEPTIC) then S-02 (CHAMPION) order:

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
[Subject role] has [used / evaluated / observed] {{incumbent_name}} for [time]. Current practice:
[the specific workflow function from the Roster]. Disposition: [SKEPTIC / CHAMPION] because
[grounded reason — a constraint, past experience, or workflow dependency — not a stance]. Primary
concern about switching: [concern].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "Walk me through what you actually do with
{{incumbent_name}} in a typical workflow cycle. I want to understand what you do today, before we
talk about anything else." This is a neutral question about current practice — not about features,
not about evaluation.]
SUBJECT: [answer — describes actual workflow, specific enough that another role with a different
current practice could not give the same Q1 answer; vocabulary and domain artifacts reflect this
specific role]

INTERVIEWER: [follow-up that probes or builds on a specific detail from the Q1 answer — grounded
in the workflow the subject just described]
SUBJECT: [answer — role-specific vocabulary and concerns; distinguishable from the Incumbent and
from all other human subjects without the role label]

INTERVIEWER: [question that directly names at least one Tension Log entry: "T-[N] — the current
approach claims [tension item]. Does that match what you actually encounter in your context?"]
SUBJECT: [answer — addresses T-N by name; confirms, disputes, or qualifies the claim; grounded in
their actual current practice from Q1]

[TENSION LOG UPDATE: after this interview, record the verbatim SUBJECT turn for each T-entry
addressed. Update Status to ADDRESSED. Do not advance to the next subject until updates are
recorded.]

Minimum 3 INTERVIEWER turns per subject. Q1 must be the opening question. At least one subsequent
turn must directly name a Tension Log entry by T-number.

**Q1 contrast note** (written after the interview transcript, before Surprise):
State whether the subject's Q1 answer is consistent with their Roster current practice declaration.
For the SKEPTIC (S-01): does Q1 ground the resistance in declared current practice, or is it
generic? A SKEPTIC whose Q1 answer applies to anyone is a C-05 grounding failure — flag explicitly.
A Q1 answer that ignores or contradicts the declared current practice is a grounding failure.

**Surprise — [Subject role]:**
One SUBJECT turn that contradicted the prior assumption stated in the Roster. Quote verbatim.
State what was assumed (cite the Roster entry) and what was revealed.

**Evidence Pull — [Subject role]:**
| HE-# | Signal | Quote from SUBJECT turn | Confidence | Rationale |
|------|--------|------------------------|------------|-----------|
| HE-1 | [signal label] | "[verbatim SUBJECT quote — not paraphrased]" | HIGH / MEDIUM / LOW | [one-line rationale] |
| HE-2 | [signal label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All four columns required on every row.

---

## STEP 3 — SYNTHESIS

Do not begin synthesis until: (a) all human interviews complete, (b) all Tension Log entries
updated, (c) all Evidence Pulls populated with all four columns on every row.

Every synthesis item must cite a direct quote from a SUBJECT turn. No synthesis claim without a
source. No inference without a turn.

### Pattern
At least one signal that appeared across two or more subjects. Cite a verbatim SUBJECT turn per
subject. The Incumbent is eligible.

### Critical Contradiction
The single most significant contradiction in this session. Not the most dramatic — the most
consequential for the interview question. Both sides must be cited verbatim.

| Field | Value |
|-------|-------|
| Subject A | [role] |
| Subject A position | [what Subject A asserted] |
| Quote A | "[verbatim SUBJECT turn from Subject A — not paraphrased, not summarized]" |
| Subject B | [role] |
| Subject B position | [what Subject B asserted — the position in conflict with Subject A] |
| Quote B | "[verbatim SUBJECT turn from Subject B — not paraphrased, not summarized]" |
| Evidential weight | [What this contradiction confirms, undermines, or leaves unresolved. Why does it outrank other contradictions?] |

### Tension Resolution
| T-# | IE-# | Final status | Resolution quote (verbatim SUBJECT turn) |
|-----|------|-------------|------------------------------------------|
| T-1 | IE-1 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-1 directly — OPEN" |
| T-2 | IE-2 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-2 directly — OPEN" |

### Inertia Verdict Matrix
| IE-# | Incumbent claim | Verdict | Human SUBJECT turn (verbatim) |
|------|----------------|---------|-------------------------------|
| IE-1 | [claim label] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" |
| IE-2 | [claim label] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" |

### Arc Signal
State whether convergence or contradiction was the dominant arc signal across this session.
Frame from SKEPTIC-first perspective: the SKEPTIC (S-01) was encountered first; did the CHAMPION's
(S-02) perspective confirm, overturn, or complicate the prior skeptical signal?

- **Dominant signal**: CONVERGENCE / CONTRADICTION / INCONCLUSIVE
- **SKEPTIC-first arc framing**: [state what the SKEPTIC interview established as the resistance
  signal; then state what the CHAMPION interview added — confirmation, complication, or overturn]
- **Evidence per subject** (cite one verbatim SUBJECT turn per subject):
  - Subject 0 (Incumbent): "[verbatim SUBJECT turn]"
  - S-01 (SKEPTIC — prior signal): "[verbatim SUBJECT turn]"
  - S-02 (CHAMPION — subsequent evidence): "[verbatim SUBJECT turn]"
- **Grounding assessment**: Is the SKEPTIC's resistance grounded in declared current practice
  (strong skepticism) or positional (weak skepticism that ignores workflow)? Cite one SUBJECT turn.
  Convergence between a role-grounded SKEPTIC and a CHAMPION is the strongest signal this skill
  can produce.

### Prior Assumption Revisited
One Roster assumption that the interviews revised. Quote the SUBJECT turn that caused the revision.
State what the Roster assumed and what is now understood.
```

---

## V-04: Phrasing Register + Lifecycle — Both Fixes Applied (standard order)

**Axes:** Phrasing register + lifecycle emphasis (combination).
**Hypothesis:** Both R3 V-05 regressions (C-10 Rationale column drop, C-11 disposition label drop)
can be corrected with two named additions to the R3 V-05 architecture: a DISPOSITION REQUIREMENT
block (C-17) and a COLUMN POLICY block (C-16). No other architectural changes. Standard
CHAMPION-before-SKEPTIC interview order. If V-04 scores 135/135, the fixes are minimal and
sufficient — no sequence change or additional axis required.

---

```
# prove-interview

---

## STEP 0 — ROSTER

Declare the complete roster before beginning any interview.

**Subject 0 — The Incumbent**
| Field | Value |
|-------|-------|
| Role | Incumbent: {{incumbent_name}} — the solution currently in place |
| Prior knowledge | Speaks in the vocabulary of teams that have built workflows around it: reliability claims, integration arguments, switching-cost calculations, institutional familiarity, ecosystem lock-in |
| Stakeholder type | Non-human baseline |
| Current practice | [The specific daily function teams invoking {{incumbent_name}} rely on — not "it works well" but the actual workflow step that would need a replacement path before switching becomes viable] |

**Human Subjects**
| Subject | Role / Title | Prior knowledge | Knowledge gaps | Stakeholder type | Current practice with Incumbent | Disposition |
|---------|-------------|----------------|----------------|-----------------|----------------------------------|-------------|
| S-01 | [job title] | [what they know about the domain and {{topic}}] | [what they don't know] | [technical / business / buyer / user] | [what they use {{incumbent_name}} for, how long, how embedded — specific function] | **CHAMPION** |
| S-02 | [job title — non-overlapping with S-01] | [what they know] | [what they don't know] | [must differ from S-01] | [current practice — must differ meaningfully from S-01's] | **SKEPTIC** |

---

**DISPOSITION REQUIREMENT:**

The Disposition column must be filled for every human subject before any interview begins.
Labels are permanent — declared going in, not assigned at synthesis-level arc analysis.

Required structure:
- At least one subject must be labeled **CHAMPION** (advocate or positive adopter of the proposed
  approach — not of {{incumbent_name}}).
- At least one subject must be labeled **SKEPTIC** (critic, resistor, or doubter of the proposed
  approach).
- NEUTRAL is permitted for additional subjects only when at least one CHAMPION and one SKEPTIC are
  already present.
- A roster entry that names a subject and their role without a Disposition label fails this
  requirement, regardless of what synthesis says about their arc.
- Disposition inferrable from synthesis-level arc analysis but absent from this table does not
  satisfy this requirement.

---

**COLUMN POLICY — Evidence Pull Tables:**

The following policy governs every Evidence Pull table in this skill output (Incumbent and all
Human Subjects):

Required columns: `Claim / Quote / Confidence / Rationale` (Incumbent)
                   `Signal / Quote / Confidence / Rationale` (Human Subjects)

The additive rule: columns are cumulative. Adding the Quote column does not remove the Rationale
requirement. Adding the Rationale column does not remove the Quote requirement. Quote provides
source-verification (the verbatim SUBJECT turn the signal was drawn from). Rationale provides
signal interpretation (why the signal matters for the interview question). Neither substitutes for
the other. A table with Quote + Confidence but no Rationale is incomplete. A table with
Rationale + Confidence but no Quote is incomplete.

Architectural additions (Incumbent framing, coupling columns, baseline columns) are added
alongside the four required columns — never in place of them.

Rationale format: one sentence per row answering "why does this signal matter for [interview
question]?" A Rationale that restates the Quote in different words is not a Rationale.

---

Minimum 2 human subjects from non-overlapping stakeholder types. Subject 0 (The Incumbent) does
not count toward the human subject minimum. Declare all roster entries before beginning any
interview.

---

## STEP 1 — INCUMBENT INTERVIEW

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
{{incumbent_name}} has been in place since [time]. Teams that depend on it justify it with:
[claim 1], [claim 2], [claim 3]. Primary switching-cost argument: [argument]. Rough edge sometimes
acknowledged internally: [limitation].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "What does a team that depends on {{incumbent_name}}
actually do in their workflow that would require a replacement path before moving away? Walk me
through the specific daily function." This is a neutral question about current practice — not about
features, not about evaluation.]
SUBJECT: [The Incumbent describes the actual daily workflow dependency — specific, grounded in what
teams do; switching-cost language rooted in workflow interruption; first-person as the voice of
teams that trust it; vocabulary distinguishable from any human subject without the role label]

INTERVIEWER: [question — probe a specific claimed strength that surfaced in Q1 with a concrete
scenario]
SUBJECT: [Incumbent defends or qualifies in-voice; word choice must be distinguishable from all
human subjects]

INTERVIEWER: [question — ask what would need to be true for a team to move away from it]
SUBJECT: [switching-cost framing required; at least one team assumption being carried without
examination should surface here]

Minimum 3 INTERVIEWER turns. Q1 must come before any feature or evaluation question. The Incumbent
voice must be distinguishable from all human subjects without the role label.

**Surprise — Incumbent:**
One SUBJECT turn where the Incumbent's answer revealed a team assumption being carried without
examination. Quote the SUBJECT turn verbatim. State what assumption was surfaced.

**Evidence Pull — Incumbent:**
| IE-# | Claim | Quote from SUBJECT turn | Confidence | Rationale |
|------|-------|------------------------|------------|-----------|
| IE-1 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW | [one-line rationale — why this claim matters for the interview question] |
| IE-2 | [claim label] | "[verbatim Incumbent SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All four columns required on every row per Column Policy.

---

## STEP 1b — TENSION LOG

Promote minimum 2 rows from the Incumbent Evidence Pull to the Tension Log. The Source quote in
each entry IS the verbatim Incumbent SUBJECT turn already captured in the corresponding IE-# row —
do not re-extract, do not paraphrase, do not rephrase.

| T-# | IE-# | Tension item (the claim to be tested) | Source quote (verbatim — must match IE-# Quote column character for character) | Status |
|-----|------|---------------------------------------|--------------------------------------------------------------------------------|--------|
| T-1 | IE-1 | [tension framing of IE-1 — phrased as a testable proposition human subjects can confirm or dispute] | "[verbatim Incumbent SUBJECT quote — identical to IE-1 Quote column]" | OPEN |
| T-2 | IE-2 | [tension framing of IE-2] | "[verbatim Incumbent SUBJECT quote — identical to IE-2 Quote column]" | OPEN |

Do not begin Step 2 until the Tension Log has at least 2 entries and every Source quote matches
its IE-# row.

---

## STEP 2 — HUMAN INTERVIEWS

For each human subject in the roster, in declared roster order:

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
[Subject role] has [used / evaluated / observed] {{incumbent_name}} for [time]. Current practice:
[the specific workflow function from the Roster]. Disposition: [CHAMPION / SKEPTIC] because
[grounded reason — a constraint, past experience, or workflow dependency — not a stance]. Primary
concern about switching: [concern].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "Walk me through what you actually do with
{{incumbent_name}} in a typical workflow cycle. I want to understand what you do today, before we
talk about anything else." This is a neutral question about current practice — not about features,
not about evaluation.]
SUBJECT: [answer — describes actual workflow, specific enough that another role with a different
current practice could not give the same Q1 answer; references the Current practice declared in
the Roster; vocabulary and domain artifacts reflect this specific role]

INTERVIEWER: [follow-up that probes or builds on a specific detail from the Q1 answer — grounded
in the workflow the subject just described]
SUBJECT: [answer — role-specific vocabulary and concerns; distinguishable from the Incumbent and
from all other human subjects without the role label]

INTERVIEWER: [question that directly names at least one Tension Log entry: "T-[N] — the current
approach claims [tension item]. Does that match what you actually encounter in your context?"]
SUBJECT: [answer — addresses T-N by name; confirms, disputes, or qualifies the claim; grounded in
their actual current practice from Q1]

[TENSION LOG UPDATE: after this interview, record the verbatim SUBJECT turn for each T-entry
addressed. Update Status to ADDRESSED. Leave OPEN entries not addressed. Do not advance to the
next subject until updates are recorded.]

Minimum 3 INTERVIEWER turns per subject. Q1 must be the opening question. At least one subsequent
turn must directly name a Tension Log entry by T-number. Referencing the tension thematically
without the T-number does not satisfy this requirement.

**Q1 contrast note** (written after the interview transcript, before Surprise):
State whether the subject's Q1 answer is consistent with their Roster current practice declaration.
A Q1 answer that ignores or contradicts the declared current practice is a grounding failure —
flag it explicitly here.

**Surprise — [Subject role]:**
One SUBJECT turn that contradicted the prior assumption stated in the Roster for this subject.
Quote the SUBJECT turn verbatim. State what was assumed (cite the Roster entry) and what was
revealed.

**Evidence Pull — [Subject role]:**
| HE-# | Signal | Quote from SUBJECT turn | Confidence | Rationale |
|------|--------|------------------------|------------|-----------|
| HE-1 | [signal label] | "[verbatim SUBJECT quote — not paraphrased]" | HIGH / MEDIUM / LOW | [one-line rationale — why this signal matters for the interview question] |
| HE-2 | [signal label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All four columns required on every row per Column Policy.

---

## STEP 3 — SYNTHESIS

Do not begin synthesis until: (a) all human interviews complete, (b) all Tension Log entries
updated, (c) all Evidence Pulls populated with all four columns on every row.

Every synthesis item — every pattern claim, Critical Contradiction claim, Tension resolution entry,
Inertia Verdict Matrix row, Arc Signal claim, and assumption update — must cite a direct quote from
a SUBJECT turn. No synthesis claim without a source. No inference without a turn.

### Pattern
At least one signal that appeared across two or more subjects. Cite a verbatim SUBJECT turn per
subject. The Incumbent is eligible.

### Critical Contradiction
The single most significant contradiction in this session. Not the most dramatic disagreement —
the one whose resolution most changes the answer to the interview question. Both sides must be
cited verbatim.

| Field | Value |
|-------|-------|
| Subject A | [role] |
| Subject A position | [what Subject A asserted] |
| Quote A | "[verbatim SUBJECT turn from Subject A — not paraphrased, not summarized]" |
| Subject B | [role] |
| Subject B position | [what Subject B asserted — the position in conflict with Subject A] |
| Quote B | "[verbatim SUBJECT turn from Subject B — not paraphrased, not summarized]" |
| Evidential weight | [What this contradiction confirms, undermines, or leaves unresolved about the interview question. Why does it outrank other contradictions? Not the most dramatic — the most consequential for the answer.] |

Additional contradictions (no Quote A / Quote B requirement):
- [Contradiction 2: subjects and claim in tension]
- [Contradiction 3: subjects and claim in tension]

### Tension Resolution
| T-# | IE-# | Final status | Resolution quote (verbatim SUBJECT turn) |
|-----|------|-------------|------------------------------------------|
| T-1 | IE-1 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-1 directly — OPEN" |
| T-2 | IE-2 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-2 directly — OPEN" |

### Inertia Verdict Matrix
Adjudicate each Incumbent Evidence Pull row against human subject testimony.

| IE-# | Incumbent claim | Verdict | Human SUBJECT turn (verbatim) |
|------|----------------|---------|-------------------------------|
| IE-1 | [claim label from IE-1] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-1 — UNADDRESSED" |
| IE-2 | [claim label from IE-2] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-2 — UNADDRESSED" |

Every Incumbent Evidence Pull row must appear. No row may be blank or omitted.

### Arc Signal
State whether convergence or contradiction was the dominant arc signal across this session.

- **Dominant signal**: CONVERGENCE / CONTRADICTION / INCONCLUSIVE
- **Evidence per subject** (cite one verbatim SUBJECT turn per subject that evidences the
  dominant signal):
  - Subject 0 (Incumbent): "[verbatim SUBJECT turn]"
  - S-01 (CHAMPION): "[verbatim SUBJECT turn]"
  - S-02 (SKEPTIC): "[verbatim SUBJECT turn]"
- **CHAMPION/SKEPTIC arc**: Was convergence reached despite SKEPTIC resistance (strong signal) or
  did the SKEPTIC confirm the CHAMPION without role-grounded resistance (weak signal — flag it)?
  Cite the SKEPTIC turn. A SKEPTIC whose resistance is "change is hard" without grounding in
  declared current practice is a grounding failure — flag it.
- **Skeptic assessment**: Did the SKEPTIC subject's resistance appear role-grounded (rooted in
  their declared current practice and domain constraints) or positional? Cite one SUBJECT turn.

### Prior Assumption Revisited
One Roster assumption that the interviews revised. Quote the SUBJECT turn that caused the revision.
State what the Roster assumed and what is now understood.
```

---

## V-05: Full R4 Ceiling Candidate — All Five Axes

**Axes:** All five — phrasing register, lifecycle emphasis, output format, role sequence, inertia
framing.
**Hypothesis:** Full R4 ceiling is achievable by combining the two targeted fixes (DISPOSITION
REQUIREMENT block for C-17, COLUMN POLICY block for C-16) with SKEPTIC-first interview sequence,
explicit enforcement language in each phase gate, and a restructured Arc Signal section that
accounts for SKEPTIC-first arc framing. All five variation axes engaged simultaneously.
Predicted 135/135.

---

```
# prove-interview

---

## STEP 0 — ROSTER

Declare the complete roster before beginning any interview. No interview may begin until the
roster is complete.

**Subject 0 — The Incumbent**
| Field | Value |
|-------|-------|
| Role | Incumbent: {{incumbent_name}} — the solution currently in place |
| Prior knowledge | Speaks in the vocabulary of teams that have built workflows around it: reliability claims, integration arguments, switching-cost calculations, institutional familiarity, ecosystem lock-in |
| Stakeholder type | Non-human baseline |
| Current practice | [The specific daily function teams invoking {{incumbent_name}} rely on — not "it works well" but the actual workflow step that would need a replacement path before switching becomes viable] |

**Human Subjects — SKEPTIC FIRST**
| Subject | Role / Title | Prior knowledge | Knowledge gaps | Stakeholder type | Current practice with Incumbent | Disposition |
|---------|-------------|----------------|----------------|-----------------|----------------------------------|-------------|
| S-01 | [job title — the SKEPTIC] | [what they know about the domain and {{topic}}] | [what they don't know] | [technical / business / buyer / user] | [what they use {{incumbent_name}} for, how long, how embedded — specific function, not general disposition] | **SKEPTIC** |
| S-02 | [job title — the CHAMPION, non-overlapping with S-01] | [what they know] | [what they don't know] | [must differ from S-01] | [current practice with {{incumbent_name}} — must differ meaningfully from S-01's current practice] | **CHAMPION** |

---

**DISPOSITION REQUIREMENT:**

The Disposition column must be filled for every human subject before any interview begins.
Labels are structural declarations — permanent, assigned going in, not derived from synthesis.

- **SKEPTIC-first rule**: The SKEPTIC subject must be S-01 (first human interview after the
  Incumbent). CHAMPION must be S-02 or later. SKEPTIC-first positions role-grounded resistance as
  the prior signal; CHAMPION confirmation or qualification of that resistance becomes the evidence.
- At least one subject must be labeled **SKEPTIC** (critic or doubter of the proposed approach —
  resistance must be grounded in declared current practice, not generic positional skepticism).
- At least one subject must be labeled **CHAMPION** (advocate or positive adopter of the proposed
  approach).
- A roster entry that names a subject and their role without a Disposition label fails this
  requirement — even if synthesis correctly characterizes the advocate/skeptic arc.
- NEUTRAL is permitted only when at least one SKEPTIC and one CHAMPION are already declared.

---

**COLUMN POLICY — Evidence Pull Tables:**

This policy governs every Evidence Pull table in this skill output. It cannot be satisfied at the
synthesis level — apply it table by table.

Required column schema:
- Incumbent Evidence Pull: `IE-# | Claim | Quote | Confidence | Rationale`
- Human Subject Evidence Pull: `HE-# | Signal | Quote | Confidence | Rationale`

The additive rule is unconditional:
- Quote provides source-verification: the verbatim SUBJECT turn the signal was extracted from.
  Adding Quote does not discharge Rationale.
- Rationale provides signal interpretation: one sentence per row answering "why does this signal
  matter for [interview question]?" Adding Rationale does not discharge Quote.
- A table with Quote + Confidence but no Rationale fails the Column Policy.
- A table with Rationale + Confidence but no Quote fails the Column Policy.
- Architectural additions (coupling columns, verdict columns, T-# columns) are added alongside
  the four required columns — never in place of them.

Rationale format: one sentence per row. It must be interpretive — not a paraphrase of the Quote.

---

Minimum 2 human subjects from non-overlapping stakeholder types. Subject 0 (The Incumbent) does
not count toward the human subject minimum.

---

## STEP 1 — INCUMBENT INTERVIEW

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
{{incumbent_name}} has been in place since [time]. Teams that depend on it justify it with:
[claim 1], [claim 2], [claim 3]. Primary switching-cost argument: [argument]. Rough edge sometimes
acknowledged internally: [limitation].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "What does a team that depends on {{incumbent_name}}
actually do in their workflow that would require a replacement path before moving away? Walk me
through the specific daily function. This is a neutral question about current practice — not about
features, not about evaluation."]
SUBJECT: [The Incumbent describes the actual daily workflow dependency — specific, grounded in what
teams do rather than what the Incumbent claims to offer; switching-cost language rooted in workflow
interruption, not positioning; first-person as the voice of teams that trust it; vocabulary
distinguishable from any human subject without the role label]

INTERVIEWER: [question — probe a specific claimed strength that surfaced in Q1 with a concrete
scenario]
SUBJECT: [Incumbent defends or qualifies in-voice; word choice must be distinguishable from all
human subjects]

INTERVIEWER: [question — ask what would need to be true for a team to move away from it]
SUBJECT: [switching-cost framing required; at least one team assumption being carried without
examination should surface here]

Minimum 3 INTERVIEWER turns. Q1 must come before any feature or evaluation question. The Incumbent
voice must be distinguishable from all human subjects without the role label.

**Surprise — Incumbent:**
One SUBJECT turn where the Incumbent's answer revealed a team assumption being carried without
examination. Quote the SUBJECT turn verbatim. State what assumption was surfaced.

**Evidence Pull — Incumbent:**
| IE-# | Claim | Quote from SUBJECT turn | Confidence | Rationale |
|------|-------|------------------------|------------|-----------|
| IE-1 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW | [one-line rationale — why this claim matters for the interview question; not a restatement of the quote] |
| IE-2 | [claim label] | "[verbatim Incumbent SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All five columns required per Column Policy. Quote and Rationale both required
simultaneously — adding one does not discharge the other.

---

## STEP 1b — TENSION LOG

Promote minimum 2 rows from the Incumbent Evidence Pull to the Tension Log. The Source quote in
each entry IS the verbatim Incumbent SUBJECT turn already captured in the corresponding IE-# row —
do not re-extract, do not paraphrase, do not rephrase.

| T-# | IE-# | Tension item (the claim to be tested by human subjects) | Source quote (verbatim — must match IE-# Quote column character for character) | Status |
|-----|------|---------------------------------------------------------|--------------------------------------------------------------------------------|--------|
| T-1 | IE-1 | [tension framing of IE-1 — phrased as a testable proposition human subjects can confirm or dispute] | "[verbatim Incumbent SUBJECT quote — identical to IE-1 Quote column]" | OPEN |
| T-2 | IE-2 | [tension framing of IE-2] | "[verbatim Incumbent SUBJECT quote — identical to IE-2 Quote column]" | OPEN |

Do not begin Step 2 until the Tension Log has at least 2 entries and every Source quote matches
its IE-# row character for character.

---

## STEP 2 — HUMAN INTERVIEWS (SKEPTIC-FIRST SEQUENCE)

Interview subjects in roster order: S-01 (SKEPTIC) first, then S-02 (CHAMPION).

The SKEPTIC interview establishes the role-grounded resistance signal. The CHAMPION interview that
follows must be evaluated against it. Convergence between a role-grounded SKEPTIC and a CHAMPION
is the strongest signal this skill can produce. A CHAMPION who confirms without accounting for the
SKEPTIC's declared resistance is a synthesis red flag.

For each human subject, in S-01 (SKEPTIC) then S-02 (CHAMPION) order:

**Prior knowledge block** (required before the first INTERVIEWER turn — not inline, not merged
with Q&A):
[Subject role] has [used / evaluated / observed] {{incumbent_name}} for [time]. Current practice:
[the specific workflow function from the Roster — what they actually do, not a general stance].
Disposition: [SKEPTIC / CHAMPION] because [grounded reason rooted in workflow dependency, past
experience, or domain constraint — not a generic stance]. Primary concern about switching:
[concern].

**Transcript:**

INTERVIEWER: [Q1 — current-practice anchor: "Walk me through what you actually do with
{{incumbent_name}} in a typical workflow cycle. I want to understand what you do today, before we
talk about anything else." This is a neutral question about current practice — not about features,
not about evaluation.]
SUBJECT: [answer — describes actual workflow, specific enough that another role with a different
current practice could not give the same Q1 answer; references the Current practice declared in
the Roster; vocabulary and domain artifacts reflect this specific role]

INTERVIEWER: [follow-up that probes or builds on a specific detail from the Q1 answer — grounded
in the workflow the subject just described, not a general feature question]
SUBJECT: [answer — role-specific vocabulary and concerns; distinguishable from the Incumbent and
from all other human subjects without the role label]

INTERVIEWER: [question that directly names at least one Tension Log entry: "T-[N] — the current
approach claims [tension item]. Does that match what you actually encounter in your context?"]
SUBJECT: [answer — addresses T-N by name; confirms, disputes, or qualifies the claim; grounded in
their actual current practice from Q1]

[TENSION LOG UPDATE: after this interview, record the verbatim SUBJECT turn for each T-entry
addressed. Update Status to ADDRESSED. Leave OPEN entries not addressed. Do not advance to the
next subject until updates are recorded.]

Minimum 3 INTERVIEWER turns per subject. Q1 must be the opening question — a current-practice
question before any feature or evaluation question. At least one subsequent turn must directly name
a Tension Log entry by T-number. Referencing the tension thematically without the T-number does
not satisfy this requirement.

**Q1 contrast note** (written after the interview transcript, before Surprise):
State whether the subject's Q1 answer is consistent with their Roster current practice declaration.
For S-01 (SKEPTIC): does the Q1 answer ground the resistance in declared current practice, or is
it generic skepticism that could apply to any persona? A SKEPTIC whose Q1 answer would be
identical if their role were replaced is a C-05 grounding failure — flag it explicitly.
A Q1 answer that ignores or contradicts the declared current practice is a grounding failure —
flag it explicitly.

**Surprise — [Subject role]:**
One SUBJECT turn that contradicted the prior assumption stated in the Roster for this subject.
Quote the SUBJECT turn verbatim. State what was assumed (cite the Roster entry) and what was
revealed.

**Evidence Pull — [Subject role]:**
| HE-# | Signal | Quote from SUBJECT turn | Confidence | Rationale |
|------|--------|------------------------|------------|-----------|
| HE-1 | [signal label] | "[verbatim SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW | [one-line rationale — why this signal matters for the interview question; not a restatement of the quote] |
| HE-2 | [signal label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW | [one-line rationale] |

Minimum 2 rows. All five columns required per Column Policy. Quote and Rationale both required
simultaneously on every row.

---

## STEP 3 — SYNTHESIS

Do not begin synthesis until: (a) all human interviews complete in SKEPTIC-first order,
(b) all Tension Log entries updated, (c) all Evidence Pulls populated with all five columns on
every row per Column Policy.

Every synthesis item — every pattern claim, Critical Contradiction claim, Tension resolution entry,
Inertia Verdict Matrix row, Arc Signal claim, and assumption update — must cite a direct quote from
a SUBJECT turn. No synthesis claim without a source. No inference without a turn.

### Pattern
At least one signal that appeared across two or more subjects. Cite a verbatim SUBJECT turn per
subject. The Incumbent is eligible.

### Critical Contradiction
The single most significant contradiction in this session. Not the most dramatic disagreement —
the one whose resolution most changes the answer to the interview question. Both sides must be
cited verbatim.

| Field | Value |
|-------|-------|
| Subject A | [role] |
| Subject A position | [what Subject A asserted] |
| Quote A | "[verbatim SUBJECT turn from Subject A — not paraphrased, not summarized]" |
| Subject B | [role] |
| Subject B position | [what Subject B asserted — the position in conflict with Subject A] |
| Quote B | "[verbatim SUBJECT turn from Subject B — not paraphrased, not summarized]" |
| Evidential weight | [What this contradiction confirms, undermines, or leaves unresolved about the interview question. Why does it outrank other contradictions? Not the most dramatic — the most consequential for the answer.] |

Additional contradictions (no Quote A / Quote B requirement):
- [Contradiction 2: subjects and claim in tension]
- [Contradiction 3: subjects and claim in tension]

### Tension Resolution
| T-# | IE-# | Final status | Resolution quote (verbatim SUBJECT turn) |
|-----|------|-------------|------------------------------------------|
| T-1 | IE-1 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-1 directly — OPEN" |
| T-2 | IE-2 | RESOLVED / OPEN | "[verbatim human SUBJECT turn]" or "No human subject addressed T-2 directly — OPEN" |

### Inertia Verdict Matrix
Adjudicate each Incumbent Evidence Pull row against human subject testimony.

| IE-# | Incumbent claim | Verdict | Human SUBJECT turn (verbatim) |
|------|----------------|---------|-------------------------------|
| IE-1 | [claim label from IE-1] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-1 — UNADDRESSED" |
| IE-2 | [claim label from IE-2] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote]" or "No human subject spoke to IE-2 — UNADDRESSED" |

Every Incumbent Evidence Pull row must appear. No row may be blank or omitted.

### Arc Signal
State whether convergence or contradiction was the dominant arc signal across this session.
Frame from SKEPTIC-first perspective: the SKEPTIC (S-01) was encountered first; state what that
established as the prior resistance signal; then state what the CHAMPION (S-02) interview added.

- **Dominant signal**: CONVERGENCE / CONTRADICTION / INCONCLUSIVE
- **SKEPTIC-first arc framing**:
  - Prior signal (from SKEPTIC): [what the SKEPTIC interview established as the resistance basis —
    role-grounded or positional]
  - Subsequent evidence (from CHAMPION): [what the CHAMPION interview confirmed, complicated, or
    overturned about the SKEPTIC's signal]
  - Arc conclusion: [convergence despite SKEPTIC resistance = strong signal; CHAMPION confirmation
    that ignores SKEPTIC's declared resistance = weak signal — flag it]
- **Evidence per subject** (cite one verbatim SUBJECT turn per subject):
  - Subject 0 (Incumbent): "[verbatim SUBJECT turn]"
  - S-01 (SKEPTIC — prior signal): "[verbatim SUBJECT turn]"
  - S-02 (CHAMPION — subsequent evidence): "[verbatim SUBJECT turn]"
- **Grounding check**: Is the SKEPTIC's resistance role-grounded (rooted in declared current
  practice and domain constraints) or positional (generic resistance without workflow grounding)?
  Cite one SUBJECT turn. A SKEPTIC claiming resistance that ignores declared current practice is
  a grounding failure — flag it. A SKEPTIC who says "change is hard" without connecting to their
  declared workflow dependency fails C-05 on its face.

### Prior Assumption Revisited
One Roster assumption that the interviews revised. Quote the SUBJECT turn that caused the revision.
State what the Roster assumed and what is now understood.
```

---

```json
{"round": 4, "rubric_version": "v4", "ceiling": 135, "target_criteria": ["C-16", "C-17"], "variations": [{"id": "V-01", "axis": "phrasing_register", "target": ["C-17"], "absent_by_design": ["C-16"], "predicted_score": "128/135", "hypothesis": "Named DISPOSITION REQUIREMENT block with explicit CHAMPION/SKEPTIC label requirement produces C-17 PASS independently of Evidence table structure; C-16 regression preserved by design (Quote+Confidence only, no Rationale)"}, {"id": "V-02", "axis": "lifecycle_emphasis", "target": ["C-16"], "absent_by_design": ["C-17"], "predicted_score": "128/135", "hypothesis": "Named COLUMN POLICY gate with additive rule stated explicitly produces C-16 PASS independently of roster disposition structure; freeform positive/skeptical/neutral field only, no CHAMPION/SKEPTIC structural requirement"}, {"id": "V-03", "axis": "role_sequence", "target": ["C-16", "C-17"], "absent_by_design": [], "predicted_score": "135/135", "hypothesis": "SKEPTIC-first interview order inverts Arc Signal framing — skeptic resistance is the prior, champion confirmation is the signal to explain; both C-16 and C-17 fixes applied; C-17 roster labels function correctly regardless of sequence direction"}, {"id": "V-04", "axis": "phrasing_register+lifecycle", "target": ["C-16", "C-17"], "absent_by_design": [], "predicted_score": "135/135", "hypothesis": "Both R3 V-05 regressions corrected with two named additions (DISPOSITION REQUIREMENT + COLUMN POLICY) applied to R3 V-05 architecture; standard CHAMPION-before-SKEPTIC sequence; tests whether minimal targeted fixes produce full ceiling without sequence change"}, {"id": "V-05", "axis": "all_five", "target": ["C-16", "C-17"], "absent_by_design": [], "predicted_score": "135/135", "hypothesis": "Full R4 ceiling candidate — all five axes + SKEPTIC-first sequence + Column Policy + Disposition Requirement + SKEPTIC-first Arc Signal framing + explicit enforcement gates on every phase transition"}]}
```
