Now I have what I need. R7 established C-01..C-22 at ceiling 160/160. R8 adds C-23 (5 pts) for a new ceiling of 165. All five R8 variations should carry the R7 ceiling architecture; the only variable is how the Arc Signal references the Incumbent Coupling Table per-factor data.

Variation design:
- **V-01** — Inertia framing: Arc Signal uses aggregate switching-friction prose, no coupling factor named by row → C-23 FAIL
- **V-02** — Output format: Prose Arc Signal names friction magnitude but not the source coupling factor row → C-23 PARTIAL
- **V-03** — Lifecycle emphasis: Explicit per-factor mandate in the Arc Signal synthesis step → C-23 PASS minimal
- **V-04** — Role sequence + lifecycle: Incumbent-first transcript ordering as structural gate + per-factor Arc Signal mandate → C-23 PASS
- **V-05** — Output format + inertia framing: Arc Signal rendered as a per-factor table with explicit Coupling Factor / Magnitude / Inertia Component columns → C-23 PASS maximum

---

# prove-interview — Round 8 Variations

## V-01

**Variation axis:** Inertia framing — Arc Signal characterizes incumbent switching friction in aggregate prose without tracing any named coupling factor from the Incumbent Coupling Table.

**Hypothesis:** Even when C-22 is fully satisfied (Incumbent Coupling Table present, Switch Cost column with explicit attribution, lifecycle gate), C-23 fails at 0 pts when the Arc Signal synthesis describes switching friction in aggregate terms ("embedded workflows create high switching costs") without identifying a specific coupling factor by its table row name. The friction observation is present; the coupling factor provenance is absent.

**Predicted score:** 160/165 (C-23: 0)

---

```
Simulate a stakeholder interview session for the topic: {{topic}}.

You are a skilled interviewer. This simulation is grounded in each persona's
documented domain knowledge and plausible role-based concerns. The interview
is not real but the signals it extracts are treated as behavioral evidence.

---

## STEP 0: COMPLIANCE DECLARATIONS

Establish both named compliance blocks before declaring any subjects or
transcripts.

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Evidence Pull table with Confidence and Rationale but no Quote | Verbatim source-verification column | FAILS C-14, FAILS C-16 |
| Evidence Pull table with Quote and Confidence but no Rationale | Signal-interpretation column | FAILS C-10, FAILS C-16 |
| Evidence Pull table with Quote and Rationale but no Confidence | Strength-marker column | FAILS C-10 |
| Added structural column displaces Quote or Rationale from any existing row | Non-substitutability violated — column additions are additive, not substitutive | FAILS C-16 |
| Switch Cost column added to Inertia Verdict Matrix without a corresponding named Incumbent Coupling Table | Derived propagation present, source artifact absent | FAILS C-22 |
| Switch Cost column supplements Inertia Verdict Matrix while Evidence Pull columns remain unchanged | Additive supplementation confirmed — Switch Cost column does not displace required Evidence Pull columns; C-16 violations in Evidence Pull tables remain independent of C-22 status | COMPLIANT — additive-only |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Roster entry with no Disposition value | Per-subject disposition label required before transcript begins | FAILS C-17 |
| Synthesis arc with no SKEPTIC voice | At least one explicit skeptic or resistant voice required | FAILS C-11 |
| Synthesis arc with no CHAMPION voice | At least one explicit advocate or supporter voice required | FAILS C-11 |
| CHAMPION is roster position S-01 (declared first) | SKEPTIC must be S-01; skeptic resistance is the prior signal, not a counterpoint | FAILS C-18 |
| SKEPTIC-first roster present but Arc Signal uses symmetric two-voice comparison | Structural ordering condition met, framing derivation absent — Arc Signal synthesis must derive from skeptic-resistance-as-prior-signal | FAILS C-18 |
| Disposition labels appear only as synthesis inferences, not in pre-transcript roster | Per-subject labels must be declared in the roster table before any transcript begins | FAILS C-17 |

---

## STEP 1: INCUMBENT BASELINE INTERVIEW (S-00)

Interview the incumbent first. This establishes the switching-cost baseline.
The Incumbent Coupling Table is populated ONLY from S-00 answers and MUST be
completed before any human-subject interview begins.

### S-00 Prior Knowledge Block

- **Identity:** [The current-practice system, tool, or workflow being evaluated]
- **Embedded depth:** [How long users have relied on it; degree of workflow integration]
- **Coupling factors:** [At minimum two named factors — data gravity, training investment,
  integration surface, workflow dependency, organizational process coupling]
- **Switching friction:** [What makes replacement costly in this context]

### S-00 Transcript

**Q1 (Current-practice anchor):** "Walk me through what today looks like — what
does this workflow involve from your perspective before any new capability is
considered?"

**A1:** [In the incumbent's voice: specific, domain-grounded, concrete about
current practices. Vocabulary from the Prior Knowledge Block. No feature framing.]

**Q2:** [Open-ended follow-up probing the first coupling factor from the Prior
Knowledge Block. Do not lead toward a conclusion.]

**A2:** [Role-grounded answer. Reference S-00's HE designation in the Evidence
Pull when extracting signals.]

**Q3:** [Probing the depth of a second coupling factor — how difficult would
removal be?]

**A3:** [Answer quantifying or contextualizing the switching cost of that factor.]

**Surprise (one sentence):** [One element from S-00 that complicates or deepens
the switching-cost picture — something the Q1/Q2/Q3 framing did not anticipate.]

### S-00 Evidence Pull

Apply COLUMN POLICY to every row. If a row is missing a column, name the
criterion violated before proceeding to the next row.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-1 | [Exact words from S-00 A1, A2, or A3 — not paraphrased] | [Insight, concern, or switching-cost signal] | High / Medium / Low | [Why this signal matters to the topic decision — not a restatement of the quote] |
| HE-2 | [Exact words from S-00] | [Second signal] | High / Medium / Low | [Rationale] |

### Incumbent Coupling Table

LIFECYCLE GATE: Populate this table now from S-00 interview answers. Do not
add rows, revise ratings, or populate any cell after human-subject interviews
begin. The coupling factors and ratings must be locked from the S-00 baseline
before S-01 is declared.

| Coupling Factor | Description | Switching-Cost Rating | Sourced from |
|----------------|-------------|----------------------|--------------|
| [Factor name from S-00 domain] | [What creates this coupling] | High / Medium / Low | S-00 [HE-#] |
| [Second factor] | [Description] | High / Medium / Low | S-00 [HE-#] |

CONFIRM GATE: The Incumbent Coupling Table has at least one named coupling
factor with a switching-cost rating and an S-00 HE-# attribution. Proceed to
Step 2.

---

## STEP 2: HUMAN SUBJECT INTERVIEWS

SKEPTIC-FIRST REQUIREMENT: S-01 is the SKEPTIC. The skeptic's resistance is
the prior signal — the existing belief to be tested. S-02 is the CHAMPION.
The Arc Signal synthesis assesses whether champion testimony confirms, moderates,
or overturns the prior signal. This framing is asymmetric by design.

### Human Subjects Roster

| ID | Role / Title | Domain | Disposition | Prior Knowledge Summary |
|----|-------------|--------|-------------|------------------------|
| S-01 | [Role] | [Domain] | SKEPTIC | [What they know, what they resist, what their threshold is, what prior experience grounds their resistance] |
| S-02 | [Role] | [Domain] | CHAMPION | [What they know, why they advocate, what their use case is, what assumptions underlie their support] |

---

### S-01 Interview (SKEPTIC)

**Prior Knowledge Block:** [Role-specific background — domain expertise,
current workflow, specific concerns, what evidence would change their position.
Resistance must be role-grounded, not generic change-aversion.]

**Q1 (Current-practice anchor):** "Describe your current workflow — what does
your day-to-day look like before this topic enters the picture?"

**A1:** [In S-01's voice: specific vocabulary from their domain, actual workflow
described, resistance grounded in what they do today, not in abstract principle.]

**Q2:** [Probe the specific concern or risk raised in A1. Open-ended, not leading.]

**A2:** [Deepen the resistance with domain-specific detail. Reference threshold
or condition for change if plausible for this persona.]

**Q3 (Contrast note):** [Name a specific claim from S-00 or anticipate S-02's
likely advocacy position. Ask S-01 to address it explicitly. Do not refer
generically to "others who support this."]

**A3:** [S-01 addresses the named claim. May partially acknowledge merit while
maintaining resistance, or reject it with domain-grounded rationale.]

**Surprise (one sentence):** [One unexpected element from S-01 — tension,
concession, or reveal the questions did not predict.]

### S-01 Evidence Pull

Apply COLUMN POLICY to every row.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-3 | [Exact words from S-01] | [Signal type] | High / Medium / Low | [Why this matters to the topic decision] |
| HE-4 | [Exact words from S-01] | [Signal type] | High / Medium / Low | [Rationale] |

---

### S-02 Interview (CHAMPION)

**Prior Knowledge Block:** [Role-specific background — domain expertise,
use case, what problem they experience today, what assumptions drive their
advocacy, what would invalidate their position.]

**Q1 (Current-practice anchor):** "Before we discuss what's new — what is
your situation today? What does your current approach involve?"

**A1:** [In S-02's voice: specific to their domain, describes actual pain or
opportunity in current workflow, not advocacy abstract.]

**Q2:** [Probe the specific value or opportunity S-02 sees. Follow up on A1.]

**A2:** [Specific about the mechanism of value — what changes, for whom,
in what situation.]

**Q3 (Contrast note):** [Name S-01's specific resistance point. Ask S-02 to
address it. Cite S-01's domain or concern explicitly.]

**A3:** [S-02 addresses the named resistance. May partially acknowledge validity
or argue that S-01's concern is addressable.]

**Surprise (one sentence):** [Unexpected element — concession, nuance, or
reveal.]

### S-02 Evidence Pull

Apply COLUMN POLICY to every row.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-5 | [Exact words from S-02] | [Signal type] | High / Medium / Low | [Why this matters] |
| HE-6 | [Exact words from S-02] | [Signal type] | High / Medium / Low | [Rationale] |

---

## STEP 3: SYNTHESIS

Synthesize across all subjects. Do not summarize individual interviews.
If a synthesis claim references only one subject, it is not a synthesis — revise
before filing.

### Pattern

[One sentence: what cross-subject pattern emerges — convergence, divergence,
or structured tension.]

### Critical Contradiction Table

Identify the single most significant contradiction between subjects. Rank it
by evidential weight. Name both sides verbatim.

| Contradiction | S-01 position (verbatim) | S-02 position (verbatim) | Evidential weight | Stakes if unresolved |
|---------------|--------------------------|--------------------------|-------------------|---------------------|
| [Name the contradiction — what the two subjects disagree about] | [HE-# exact quote] | [HE-# exact quote] | [Why this contradiction matters most — what it confirms, undermines, or leaves unresolved] | [What is at risk if this tension persists into implementation] |
| [Second contradiction, if present] | [HE-# verbatim] | [HE-# verbatim] | [Why secondary to the first — explain the ranking] | [Stakes] |

### Inertia Verdict Matrix

| Subject | Adoption Signal | Resistance Source | Inertia Verdict | Switch Cost (sourced from Incumbent Coupling Table) |
|---------|----------------|-------------------|----------------|-----------------------------------------------------|
| S-01 | [Signal from S-01 Evidence Pull] | [Named resistance source from S-01 domain] | High / Medium / Low | [Coupling factor name] — [Rating] (sourced from Incumbent Coupling Table) |
| S-02 | [Signal from S-02 Evidence Pull] | [Source if any] | High / Medium / Low | [Coupling factor name] — [Rating] (sourced from Incumbent Coupling Table) |

### Arc Signal

**Prior signal (SKEPTIC S-01):** [What S-01's resistance tells us as the prior
signal — not a position summary but an evidential interpretation. Ground in HE-#.]

**Subsequent evidence (CHAMPION S-02):** [Does S-02's testimony confirm, moderate,
or overturn the prior signal? Ground in HE-#. State which direction explicitly.]

**Incumbent baseline context:** The S-00 baseline establishes that switching costs
are present in this domain. The incumbent's embedded workflows and dependencies
create meaningful friction for any transition. The prior signal must be
interpreted in the context of this switching friction: the champion's enthusiasm
may reflect genuine value that overrides these costs, or it may underestimate
how deeply the incumbent is coupled into existing practices. The aggregate
switching-cost picture informs how much weight to assign to the prior signal.

**Dominant arc:** [Convergence despite skepticism is a strong signal. Skeptic
confirming champion without role-grounded resistance is a red flag. State what
the arc means for the topic decision — one sentence.]

**Arc verdict:** [Composite signal for the topic decision, grounded in all three
subjects' evidence.]

### Prior Assumption Revisited

[One assumption the simulation corrected, complicated, or confirmed. Specific
and testable.]

---

END OF SIMULATION
```

---

## V-02

**Variation axis:** Output format — Arc Signal is structured as flowing prose. The incumbent friction section names the switching-cost magnitude ("high friction due to deep workflow embedding") but does not identify the source coupling factor by its Incumbent Coupling Table row name.

**Hypothesis:** Prose-format Arc Signal that describes friction magnitude without tracing to a named coupling factor row produces C-23 PARTIAL (2–3 pts). The magnitude is present; the coupling factor provenance is absent. The friction is described but its structural source is anonymous.

**Predicted score:** 162–163/165 (C-23: PARTIAL, 2–3 pts)

---

```
Simulate a stakeholder interview session for the topic: {{topic}}.

You are a skilled interviewer. The simulation is grounded in each persona's
documented domain knowledge and plausible role-based concerns.

---

## STEP 0: COMPLIANCE DECLARATIONS

Both named compliance blocks are required before any subject or transcript.

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Evidence Pull table has Confidence and Rationale but no Quote | Source-verification column — verbatim text required for traceability | FAILS C-14, FAILS C-16 |
| Evidence Pull table has Quote and Confidence but no Rationale | Interpretation column — signal-strength rationale required | FAILS C-10, FAILS C-16 |
| Evidence Pull table has Quote and Rationale but no Confidence | Strength-marker column — explicit High/Medium/Low required | FAILS C-10 |
| Any architectural column (Switch Cost, Coupling Factor, or other) displaces Quote or Rationale from any row | Non-substitutability violated — all column additions are additive; no existing column may be dropped | FAILS C-16 |
| Switch Cost column present in Inertia Verdict Matrix but no named Incumbent Coupling Table exists as a source artifact | Source artifact absent — column asserts without structural grounding | FAILS C-22 |
| Switch Cost column in Inertia Verdict Matrix supplementing Evidence Pull tables that retain all required columns | Additive supplementation — Switch Cost does not displace Quote, Rationale, or Confidence; C-16 violations in Evidence Pull tables are independent of C-22 status | COMPLIANT |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Any roster entry has no Disposition field value | Per-subject label required before that subject's transcript begins | FAILS C-17 |
| Synthesis arc names no SKEPTIC voice | At least one explicitly resistant voice required | FAILS C-11 |
| Synthesis arc names no CHAMPION voice | At least one explicitly supportive voice required | FAILS C-11 |
| S-01 (first roster position) is declared as CHAMPION rather than SKEPTIC | SKEPTIC must hold S-01; prior signal framing derives from skeptic-first position | FAILS C-18 |
| SKEPTIC is S-01 in roster but Arc Signal synthesis presents a symmetric two-voice comparison | Framing condition unmet — synthesis must derive from skeptic-resistance-as-prior-signal, not from equal-voice balance | FAILS C-18 |
| Disposition characterization appears only in synthesis conclusion, not in pre-transcript roster table | Roster-level declaration required; post-transcript inference does not satisfy this requirement | FAILS C-17 |

---

## STEP 1: INCUMBENT BASELINE INTERVIEW (S-00)

Interview the incumbent first. The Incumbent Coupling Table is populated
exclusively from this interview. It must be complete and locked before any
human-subject interview proceeds.

### S-00 Prior Knowledge Block

- **Identity:** [Current system, tool, process, or workflow being displaced]
- **Depth of integration:** [Years in use, workflow dependencies, organizational
  embedding]
- **Coupling factors (name at least two):** [Training investment, data gravity,
  workflow integration, integration surface, org-process dependency]
- **Switching friction character:** [What type of cost dominates — retraining,
  migration, integration refactoring, political, contractual]

### S-00 Transcript

**Q1 (Current-practice anchor):** "Take me through your current workflow — what
does this look like in practice today, before any alternative enters the picture?"

**A1:** [In the incumbent's voice: concrete, specific, workflow-grounded, no
feature framing. Vocabulary from the Prior Knowledge Block.]

**Q2:** [Probe the first coupling factor. Open-ended. Ask how deeply embedded
it is, not whether it is embedded.]

**A2:** [Domain-grounded answer with specific workflow details.]

**Q3:** [Probe the second coupling factor. Focus on what would break if the
incumbent were removed.]

**A3:** [Specific answer describing the breaking-point scenario from the
incumbent's perspective.]

**Surprise (one sentence):** [One unexpected coupling dimension or depth of
integration the Q1–Q3 framing did not anticipate.]

### S-00 Evidence Pull

Apply COLUMN POLICY. If any row is missing a required column, name the
criterion violated before continuing.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-1 | [Exact words from S-00 A1, A2, or A3] | [Coupling signal or switching-cost insight] | High / Medium / Low | [Why this matters to the topic decision] |
| HE-2 | [Exact words from S-00] | [Second signal] | High / Medium / Low | [Rationale] |

### Incumbent Coupling Table

LIFECYCLE GATE: Populate this table from S-00 transcript answers now.
Lock it. Do not add rows, change ratings, or populate any cell after
proceeding to human-subject interviews.

| Coupling Factor | Description | Switching-Cost Rating | Sourced from |
|----------------|-------------|----------------------|--------------|
| [Factor A — name from S-00 domain vocabulary] | [What creates this coupling and how deep it runs] | High / Medium / Low | S-00 [HE-#] |
| [Factor B] | [Description] | High / Medium / Low | S-00 [HE-#] |

GATE CONFIRMED: Table has at least one named factor with a rating and HE-#
attribution. Proceed to Step 2.

---

## STEP 2: HUMAN SUBJECT INTERVIEWS

SKEPTIC-FIRST: S-01 is the SKEPTIC. Skeptic resistance is the prior signal.
S-02 is the CHAMPION. Arc Signal derives from prior-signal testing, not from
symmetric comparison.

### Human Subjects Roster

| ID | Role / Title | Domain | Disposition | Prior Knowledge Summary |
|----|-------------|--------|-------------|------------------------|
| S-01 | [Role and title] | [Domain] | SKEPTIC | [Expertise, current workflow, specific resistance, threshold for change] |
| S-02 | [Role and title] | [Domain] | CHAMPION | [Expertise, use case, advocacy rationale, underlying assumptions] |

---

### S-01 Interview (SKEPTIC)

**Prior Knowledge Block:** [Role background — domain expertise, current workflow,
what specifically grounds this resistance. Not generic change-aversion. Named
concerns tied to the role.]

**Q1 (Current-practice anchor):** "Before we discuss any new approach — what
does your current workflow look like? Walk me through what you do today."

**A1:** [S-01's voice: domain-specific, workflow-concrete, resistance visible
in the answer not just in a disclaimer. Vocabulary from their Prior Knowledge Block.]

**Q2:** [Follow-up probing the specific concern surface in A1.]

**A2:** [Deepens the resistance. Names a specific failure mode, cost, or risk
from their domain perspective.]

**Q3 (Contrast note):** [Name a specific claim from S-00 or from the CHAMPION's
anticipated position. Ask S-01 to respond to it directly. Name the claim, not
a generic "some supporters argue."]

**A3:** [S-01 responds to the named claim. May acknowledge partial validity
while maintaining core resistance, or reject it with domain-grounded rationale.]

**Surprise (one sentence):** [An unexpected element — tension, nuance, or
concession the Q1–Q3 structure did not predict.]

### S-01 Evidence Pull

Apply COLUMN POLICY.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-3 | [Exact words from S-01 — not paraphrased] | [Signal type] | High / Medium / Low | [Why this matters to the decision] |
| HE-4 | [Exact words from S-01] | [Signal type] | High / Medium / Low | [Rationale] |

---

### S-02 Interview (CHAMPION)

**Prior Knowledge Block:** [Role background — domain expertise, use case,
what problem they experience today, what mechanism of value they expect,
what would invalidate their position.]

**Q1 (Current-practice anchor):** "Before we get into what you'd like to see —
what does your current situation look like? What are you dealing with today?"

**A1:** [S-02's voice: domain-specific, current pain or gap concrete, advocacy
grounded in what they do now not in what they imagine. Vocabulary from Prior
Knowledge Block.]

**Q2:** [Follow-up probing the specific mechanism of value S-02 expects.]

**A2:** [Specific about what changes, for whom, in what workflow context.]

**Q3 (Contrast note):** [Name S-01's specific resistance point. Ask S-02 to
address it. Reference S-01's domain explicitly.]

**A3:** [S-02 addresses S-01's concern. May partially grant validity, explain
why it doesn't apply in their context, or argue the concern is addressable.]

**Surprise (one sentence):** [Unexpected nuance, concession, or constraint
S-02 introduces.]

### S-02 Evidence Pull

Apply COLUMN POLICY.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-5 | [Exact words from S-02] | [Signal type] | High / Medium / Low | [Rationale] |
| HE-6 | [Exact words from S-02] | [Signal type] | High / Medium / Low | [Rationale] |

---

## STEP 3: SYNTHESIS

Synthesize across all subjects. A conclusion referencing only one subject
is not a synthesis — revise before filing.

### Pattern

[One sentence stating the cross-subject pattern: convergence, divergence,
or structured tension.]

### Critical Contradiction Table

| Contradiction | S-01 position (verbatim) | S-02 position (verbatim) | Evidential weight | Stakes if unresolved |
|---------------|--------------------------|--------------------------|-------------------|---------------------|
| [Name the contradiction] | [HE-# exact quote] | [HE-# exact quote] | [Why this matters most — what it confirms, undermines, or leaves unresolved] | [Risk if tension persists] |
| [Secondary contradiction] | [HE-# verbatim] | [HE-# verbatim] | [Why secondary — explain ranking explicitly] | [Stakes] |

### Inertia Verdict Matrix

| Subject | Adoption Signal | Resistance Source | Inertia Verdict | Switch Cost (sourced from Incumbent Coupling Table) |
|---------|----------------|-------------------|----------------|-----------------------------------------------------|
| S-01 | [Signal from S-01 Evidence Pull] | [Named resistance source] | High / Medium / Low | [Factor name] — [Rating] (sourced from Incumbent Coupling Table) |
| S-02 | [Signal from S-02 Evidence Pull] | [Source if any] | High / Medium / Low | [Factor name] — [Rating] (sourced from Incumbent Coupling Table) |

### Arc Signal

Write the Arc Signal as flowing narrative prose. Do not use headers or
sub-bullets within this section.

The prior signal is the SKEPTIC's resistance (S-01). [Characterize what S-01's
resistance tells us as an evidential reading, grounded in HE-3 or HE-4. State
what the skeptic believes to be true about the topic and why that reading
deserves prior-signal weight.]

The CHAMPION's testimony (S-02) is the evidence against this prior. [State
whether S-02's evidence confirms, moderates, or overturns the prior signal,
grounded in HE-5 or HE-6. Be specific about which direction the evidence points
and why.]

The incumbent baseline (S-00) establishes that the switching costs associated
with this domain are real and substantial. The prior signal carries additional
weight because transition away from the incumbent is not frictionless — the
high switching friction documented in the S-00 interview means that champion
enthusiasm must be measured against the cost of actual displacement. Any
transition plan must account for the depth of incumbent embedding and the
friction magnitude documented in the baseline.

The dominant arc signal is [convergence / divergence / inconclusive]. [State
what this means for the topic decision — one sentence. Ground in all three
subjects.]

### Prior Assumption Revisited

[One assumption the simulation corrected, complicated, or confirmed. Specific.]

---

END OF SIMULATION
```

---

## V-03

**Variation axis:** Lifecycle emphasis — the Arc Signal synthesis step includes an explicit per-factor mandate: at least one coupling factor from the Incumbent Coupling Table must be named by its Factor Name, with switching friction magnitude and inertia verdict connection stated explicitly.

**Hypothesis:** An explicit structural mandate in the Arc Signal synthesis step — naming the per-factor requirement as a lifecycle obligation — drives C-23 PASS at minimum. The mandate creates a checklist item the synthesis step cannot skip without violating an instruction.

**Predicted score:** 165/165 (C-23: PASS, 5 pts)

---

```
Simulate a stakeholder interview session for the topic: {{topic}}.

You are a skilled interviewer. The simulation is grounded in each persona's
documented domain knowledge and plausible role-based concerns.

---

## STEP 0: COMPLIANCE DECLARATIONS

Both named compliance blocks must appear before any subject declaration.

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Evidence Pull table has Confidence and Rationale but no Quote | Verbatim source-verification required | FAILS C-14, FAILS C-16 |
| Evidence Pull table has Quote and Confidence but no Rationale | Interpretation rationale required | FAILS C-10, FAILS C-16 |
| Evidence Pull table has Quote and Rationale but no Confidence | Explicit strength marker required | FAILS C-10 |
| Any column addition displaces Quote or Rationale from an existing row | Non-substitutability violated — additive rule is unconditional | FAILS C-16 |
| Switch Cost column in Inertia Verdict Matrix references no named Incumbent Coupling Table | Derived column without source grounding | FAILS C-22 |
| Switch Cost column entry lacks an explicit "sourced from Incumbent Coupling Table" attribution | Coexistence without attribution is PARTIAL, not PASS | FAILS C-22 (PARTIAL, not PASS) |
| Switch Cost column supplements Inertia Verdict Matrix while Evidence Pull columns retain Quote, Rationale, and Confidence | Additive supplementation — C-16 violations in Evidence Pull tables are independent of C-22 architecture | COMPLIANT |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Roster entry missing Disposition value | Per-subject disposition label before transcript | FAILS C-17 |
| No SKEPTIC voice in synthesis | At least one explicit resistant voice | FAILS C-11 |
| No CHAMPION voice in synthesis | At least one explicit supportive voice | FAILS C-11 |
| CHAMPION declared as S-01 | SKEPTIC must be S-01; prior-signal framing derived from skeptic-first | FAILS C-18 |
| SKEPTIC is S-01 but Arc Signal uses symmetric comparison framing | Structural condition met; framing derivation absent | FAILS C-18 |
| Disposition labels only in synthesis inference | Roster-level declaration required before transcripts | FAILS C-17 |

---

## STEP 1: INCUMBENT BASELINE INTERVIEW (S-00)

Interview the incumbent first. Populate the Incumbent Coupling Table from
this interview only. The table must be fully populated and locked before
any human-subject interview begins.

### S-00 Prior Knowledge Block

- **Identity:** [System, tool, or workflow being displaced]
- **Integration depth:** [How long in use, how deeply embedded in workflow]
- **Coupling factors (name at least two explicitly):** [List factors with names —
  e.g., "Data Gravity," "Training Investment," "Integration Surface Depth"]
- **Switching friction type:** [What kind of cost dominates the switching picture]

### S-00 Transcript

**Q1 (Current-practice anchor):** "Describe your current role in the workflow —
what does a typical interaction look like before any change is introduced?"

**A1:** [S-00's voice: concrete, workflow-specific, no feature framing.
Coupling factors visible in the answer.]

**Q2:** [Probe the first named coupling factor from the Prior Knowledge Block.
Open-ended — ask about depth and consequence, not existence.]

**A2:** [Specific answer. Use Factor A vocabulary from S-00's domain.]

**Q3:** [Probe the second named coupling factor. Ask what would happen if this
coupling were broken.]

**A3:** [Specific answer about breaking-point cost.]

**Surprise (one sentence):** [One coupling dimension the Q1–Q3 structure
did not anticipate.]

### S-00 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-1 | [Exact words from S-00] | [Coupling or switching-cost signal] | High / Medium / Low | [Why this matters] |
| HE-2 | [Exact words from S-00] | [Second signal] | High / Medium / Low | [Rationale] |

### Incumbent Coupling Table

LIFECYCLE GATE: Populate now from S-00 only. This table is locked after
this step. No row may be added, revised, or populated after S-01 interview
begins.

| Coupling Factor | Description | Switching-Cost Rating | Sourced from |
|----------------|-------------|----------------------|--------------|
| [Factor A name — use the exact name from S-00's vocabulary] | [What creates this coupling] | High / Medium / Low | S-00 [HE-#] |
| [Factor B name] | [Description] | High / Medium / Low | S-00 [HE-#] |

GATE CONFIRMED. Proceed to Step 2.

---

## STEP 2: HUMAN SUBJECT INTERVIEWS

SKEPTIC-FIRST: S-01 is the SKEPTIC. Skeptic resistance is the prior signal.
S-02 is the CHAMPION.

### Human Subjects Roster

| ID | Role / Title | Domain | Disposition | Prior Knowledge Summary |
|----|-------------|--------|-------------|------------------------|
| S-01 | [Role] | [Domain] | SKEPTIC | [Background, current workflow, specific resistance, threshold] |
| S-02 | [Role] | [Domain] | CHAMPION | [Background, use case, advocacy rationale, assumptions] |

---

### S-01 Interview (SKEPTIC)

**Prior Knowledge Block:** [Role-grounded background. Resistance tied to
specific domain experience, not generic.]

**Q1 (Current-practice anchor):** "Take me through what your current workflow
looks like — what are you doing today before this topic enters the picture?"

**A1:** [S-01's voice: domain-specific, current-practice concrete, resistance
visible in the framing of the answer.]

**Q2:** [Probe the concern raised in A1.]

**A2:** [Domain-specific deepening of the resistance.]

**Q3 (Contrast note):** [Name a specific S-00 coupling claim or S-02's
anticipated position. Ask S-01 to address it directly.]

**A3:** [S-01 responds to the named claim with domain-grounded rationale.]

**Surprise (one sentence):** [Unexpected element from S-01.]

### S-01 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-3 | [Exact words from S-01] | [Signal] | High / Medium / Low | [Why it matters] |
| HE-4 | [Exact words from S-01] | [Signal] | High / Medium / Low | [Rationale] |

---

### S-02 Interview (CHAMPION)

**Prior Knowledge Block:** [Role-grounded background. Advocacy tied to
specific use case and current-practice pain, not generic enthusiasm.]

**Q1 (Current-practice anchor):** "Before we discuss what you'd like to see
changed — what does your current situation look like?"

**A1:** [S-02's voice: domain-specific, current-practice concrete.]

**Q2:** [Probe the specific mechanism of value S-02 expects.]

**A2:** [Specific about what changes and for whom.]

**Q3 (Contrast note):** [Name S-01's specific resistance. Ask S-02 to address
it directly.]

**A3:** [S-02 responds to S-01's named concern.]

**Surprise (one sentence):** [Unexpected nuance from S-02.]

### S-02 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-5 | [Exact words from S-02] | [Signal] | High / Medium / Low | [Rationale] |
| HE-6 | [Exact words from S-02] | [Signal] | High / Medium / Low | [Rationale] |

---

## STEP 3: SYNTHESIS

### Pattern

[One sentence: cross-subject pattern — convergence, divergence, or tension.]

### Critical Contradiction Table

| Contradiction | S-01 position (verbatim) | S-02 position (verbatim) | Evidential weight | Stakes if unresolved |
|---------------|--------------------------|--------------------------|-------------------|---------------------|
| [Name] | [HE-# exact quote] | [HE-# exact quote] | [Why most significant] | [Risk] |
| [Secondary] | [HE-# verbatim] | [HE-# verbatim] | [Why secondary] | [Stakes] |

### Inertia Verdict Matrix

| Subject | Adoption Signal | Resistance Source | Inertia Verdict | Switch Cost (sourced from Incumbent Coupling Table) |
|---------|----------------|-------------------|----------------|-----------------------------------------------------|
| S-01 | [Signal] | [Named source] | High / Medium / Low | [Factor name] — [Rating] (sourced from Incumbent Coupling Table) |
| S-02 | [Signal] | [Source if any] | High / Medium / Low | [Factor name] — [Rating] (sourced from Incumbent Coupling Table) |

### Arc Signal

**Prior signal (SKEPTIC S-01):** [What S-01's resistance tells us as an
evidential reading. Ground in HE-3 or HE-4.]

**Subsequent evidence (CHAMPION S-02):** [Does S-02's testimony confirm,
moderate, or overturn the prior signal? Ground in HE-5 or HE-6.]

**Per-factor incumbent friction — REQUIRED:** Identify at least one coupling
factor from the Incumbent Coupling Table by its exact Factor Name as it appears
in the table. State its switching-cost rating from that table row. Connect this
friction claim to an inertia verdict component: does this factor's friction
confirm the inertia signal, moderate it, or provide grounds for overturn? All
three elements must be explicit: (1) Factor Name as it appears in the Incumbent
Coupling Table, (2) switching-cost magnitude from the table rating, (3) inertia
verdict connection — state confirm, moderate, or overturn and explain why.

Arc Signal prose that characterizes switching friction in general terms without
naming a specific coupling factor from the Incumbent Coupling Table fails this
step. Revise before proceeding if no coupling factor is named by its table row
name.

**Dominant arc:** [State what the arc means for the topic decision — one
sentence. Ground in all three subjects.]

**Arc verdict:** [Composite signal. One sentence.]

### Prior Assumption Revisited

[One assumption corrected, complicated, or confirmed. Specific.]

---

END OF SIMULATION
```

---

## V-04

**Variation axes:** Role sequence + lifecycle emphasis — incumbent interview (S-00) occupies the first roster position and appears first in transcript order, making the lifecycle gate structural through ordering rather than through a prose gate instruction. The Arc Signal synthesis step includes the same per-factor mandate as V-03. Combined effect: incumbent-first ordering enforces the gate by architecture; the Arc Signal step names the per-factor obligation.

**Hypothesis:** When the incumbent occupies S-00 in the roster and appears first in transcript order, the coupling table population lifecycle is enforced by document structure — an author cannot write S-01's transcript before S-00's because S-00 comes first on the page. The gate instruction shifts from a behavioral reminder to a structural fact. Combined with the V-03 Arc Signal mandate, C-23 PASS at minimum. The role-sequence axis is scoring-neutral for C-01..C-22 (confirmed by R7 V-03 incumbent-last finding) but the ordering-as-gate architecture offers a stronger mechanical enforcement of the lifecycle separation.

**Predicted score:** 165/165 (C-23: PASS, 5 pts)

---

```
Simulate a stakeholder interview session for the topic: {{topic}}.

You are a skilled interviewer. The simulation is grounded in each persona's
documented domain knowledge and plausible role-based concerns.

This simulation runs in four ordered phases. Each phase must be complete
before the next begins. Do not skip ahead.

---

## STEP 0: COMPLIANCE DECLARATIONS

Both named compliance blocks appear here before any subject or transcript.

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Evidence Pull table has Confidence and Rationale but no Quote | Verbatim source-verification column | FAILS C-14, FAILS C-16 |
| Evidence Pull table has Quote and Confidence but no Rationale | Signal-interpretation column | FAILS C-10, FAILS C-16 |
| Evidence Pull table has Quote and Rationale but no Confidence | Explicit strength-marker column | FAILS C-10 |
| Any column addition displaces Quote or Rationale | Non-substitutability violated — all additions are additive | FAILS C-16 |
| Switch Cost column entry in Inertia Verdict Matrix lacks explicit "sourced from Incumbent Coupling Table" attribution | Coexistence without attribution = C-22 PARTIAL, not PASS | FAILS C-22 (PARTIAL) |
| Switch Cost column supplements Inertia Verdict Matrix; Evidence Pull columns unchanged | Additive supplementation confirmed — C-16 violations in Evidence Pull tables remain independent of C-22 status | COMPLIANT |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Roster entry missing Disposition value | Per-subject label before transcript | FAILS C-17 |
| No SKEPTIC voice in synthesis | At least one resistant voice required | FAILS C-11 |
| No CHAMPION voice in synthesis | At least one supportive voice required | FAILS C-11 |
| CHAMPION declared as S-01 | SKEPTIC must be S-01 in roster; prior-signal framing derived from this | FAILS C-18 |
| SKEPTIC is S-01 but Arc Signal framing is symmetric | Structural condition met; framing derivation absent | FAILS C-18 |
| Disposition labels only in synthesis inference | Pre-transcript roster declaration required | FAILS C-17 |

---

## PHASE 1: INCUMBENT BASELINE (S-00)

The incumbent is interviewed first. This ordering is structural: the Incumbent
Coupling Table is populated from the S-00 transcript before any human-subject
roster entry is declared. Because S-00 appears before S-01 in this document,
the coupling table is structurally prior to all human-subject interviews.

### Full Subject Roster (all subjects declared in order)

| ID | Role / Title | Domain | Disposition | Phase |
|----|-------------|--------|-------------|-------|
| S-00 | [Incumbent identity] | [Domain] | INCUMBENT BASELINE | Phase 1 |
| S-01 | [Role] | [Domain] | SKEPTIC | Phase 2 |
| S-02 | [Role] | [Domain] | CHAMPION | Phase 2 |

SKEPTIC-FIRST REQUIREMENT (human subjects): Among the human subjects, S-01
is the SKEPTIC. The skeptic's resistance is the prior signal. S-02 is the
CHAMPION. Arc Signal synthesis derives from skeptic-resistance-as-prior-signal
framing, not from symmetric comparison.

---

### S-00 Prior Knowledge Block

- **Identity:** [System, tool, workflow, or solution being displaced]
- **Integration depth:** [How embedded; years in use, workflow dependency degree]
- **Coupling factors (name explicitly — at minimum two):** [Factor A: name and
  nature; Factor B: name and nature. Use names that will appear in the
  Incumbent Coupling Table below.]
- **Switching-friction type:** [What kind of cost dominates transition]

### S-00 Transcript

**Q1 (Current-practice anchor):** "Walk me through what your current workflow
involves — what does this look like in practice today?"

**A1:** [S-00's voice: domain-specific, workflow-concrete, coupling factors
surfaced naturally in the answer. No feature framing.]

**Q2:** [Probe coupling Factor A from the Prior Knowledge Block. Ask about
depth and consequence, not existence.]

**A2:** [Specific answer. Factor A vocabulary from S-00's domain.]

**Q3:** [Probe coupling Factor B. Ask what breaking Factor B would cost.]

**A3:** [Specific answer about Factor B switching cost.]

**Surprise (one sentence):** [Unexpected coupling depth or dimension not
anticipated by Q1–Q3.]

### S-00 Evidence Pull

Apply COLUMN POLICY.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-1 | [Exact words from S-00 A1–A3] | [Coupling or switching-cost signal] | High / Medium / Low | [Why this matters] |
| HE-2 | [Exact words from S-00] | [Second signal] | High / Medium / Low | [Rationale] |

### Incumbent Coupling Table

This table is populated from the S-00 transcript. Because S-00 is Phase 1
and the human-subject interviews are Phase 2, this table is complete before
any human subject appears. No row may be added after Phase 1 closes.

| Coupling Factor | Description | Switching-Cost Rating | Sourced from |
|----------------|-------------|----------------------|--------------|
| [Factor A — exact name from S-00 vocabulary] | [Coupling mechanism] | High / Medium / Low | S-00 [HE-#] |
| [Factor B — exact name] | [Coupling mechanism] | High / Medium / Low | S-00 [HE-#] |

PHASE 1 COMPLETE. The Incumbent Coupling Table is populated and locked.
Proceed to Phase 2.

---

## PHASE 2: HUMAN SUBJECT INTERVIEWS

The human subjects are S-01 (SKEPTIC) and S-02 (CHAMPION). SKEPTIC appears
first in the Phase 2 roster and first in Phase 2 transcript order.

---

### S-01 Interview (SKEPTIC)

**Prior Knowledge Block:** [Role background — domain expertise, current
workflow, specific concerns grounded in role experience, threshold for change.
Not generic resistance.]

**Q1 (Current-practice anchor):** "Before we talk about any new approach —
what does your current workflow look like?"

**A1:** [S-01's voice: domain-specific language, current-practice concrete,
resistance visible in the framing.]

**Q2:** [Probe the concern from A1. Open-ended.]

**A2:** [Deepens resistance with domain-specific detail.]

**Q3 (Contrast note):** [Name a specific S-00 coupling observation or S-02's
anticipated advocacy. Ask S-01 to respond directly to the named claim.]

**A3:** [S-01 responds to the named claim with domain-grounded rationale.]

**Surprise (one sentence):** [Unexpected element.]

### S-01 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-3 | [Exact words from S-01] | [Signal] | High / Medium / Low | [Why it matters] |
| HE-4 | [Exact words from S-01] | [Signal] | High / Medium / Low | [Rationale] |

---

### S-02 Interview (CHAMPION)

**Prior Knowledge Block:** [Role background — domain expertise, use case,
current pain or gap, advocacy rationale grounded in current practice.
Not generic enthusiasm.]

**Q1 (Current-practice anchor):** "What does your current situation look like —
before anything new is in the picture?"

**A1:** [S-02's voice: domain-specific, current-practice concrete.]

**Q2:** [Probe the mechanism of value S-02 expects.]

**A2:** [Specific about what changes and for whom.]

**Q3 (Contrast note):** [Name S-01's specific resistance. Ask S-02 to address
it directly.]

**A3:** [S-02 responds to S-01's named concern.]

**Surprise (one sentence):** [Unexpected element.]

### S-02 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-5 | [Exact words from S-02] | [Signal] | High / Medium / Low | [Rationale] |
| HE-6 | [Exact words from S-02] | [Signal] | High / Medium / Low | [Rationale] |

---

## PHASE 3: SYNTHESIS

Synthesize across all subjects. A conclusion referencing only one subject
is not a synthesis — revise before filing.

### Pattern

[One sentence: cross-subject pattern.]

### Critical Contradiction Table

| Contradiction | S-01 position (verbatim) | S-02 position (verbatim) | Evidential weight | Stakes if unresolved |
|---------------|--------------------------|--------------------------|-------------------|---------------------|
| [Name] | [HE-# quote] | [HE-# quote] | [Why most significant] | [Risk] |
| [Secondary] | [HE-# verbatim] | [HE-# verbatim] | [Why secondary] | [Stakes] |

### Inertia Verdict Matrix

| Subject | Adoption Signal | Resistance Source | Inertia Verdict | Switch Cost (sourced from Incumbent Coupling Table) |
|---------|----------------|-------------------|----------------|-----------------------------------------------------|
| S-01 | [Signal] | [Named source] | High / Medium / Low | [Factor name from Incumbent Coupling Table] — [Rating] (sourced from Incumbent Coupling Table) |
| S-02 | [Signal] | [Source if any] | High / Medium / Low | [Factor name from Incumbent Coupling Table] — [Rating] (sourced from Incumbent Coupling Table) |

### Arc Signal

**Prior signal (SKEPTIC S-01):** [What S-01's resistance tells us as the prior
signal. Ground in HE-3 or HE-4. Not a position summary — an evidential
interpretation.]

**Subsequent evidence (CHAMPION S-02):** [Does S-02's testimony confirm,
moderate, or overturn the prior signal? Ground in HE-5 or HE-6. State direction
explicitly.]

**Per-factor incumbent friction:** Name at least one coupling factor from the
Incumbent Coupling Table by its exact Factor Name from the table. State the
switching-cost magnitude from that row's Rating column. Connect it to an
inertia verdict component: does this factor's friction confirm, moderate, or
overturn the inertia signal? State all three elements explicitly: (1) Factor
Name, (2) switching-cost magnitude from the Incumbent Coupling Table rating,
(3) inertia verdict connection with direction and brief rationale.

If no coupling factor is named by its table row name in this section, revise
before filing the synthesis.

**Dominant arc:** [What the arc means for the topic decision. One sentence.]

**Arc verdict:** [Composite signal. One sentence.]

---

## PHASE 4: PRIOR ASSUMPTION REVISITED

[One assumption the simulation corrected, complicated, or confirmed. Specific.]

---

END OF SIMULATION
```

---

## V-05

**Variation axes:** Output format + inertia framing — the Arc Signal synthesis section is rendered as a structured per-factor table where each row corresponds to one coupling factor from the Incumbent Coupling Table. Columns: Coupling Factor | Friction Magnitude | Inertia Verdict Component | Signal Direction (Confirms / Moderates / Overturns) | Composite Arc Claim. This tabular format structurally prevents writing an Arc Signal without naming coupling factors — the table forces compliance by design.

**Hypothesis:** When Arc Signal is a structured per-factor table, C-23 compliance is architectural: every row forces the author to identify a coupling factor by name, state the friction magnitude, and connect it to an inertia verdict component. The structural format makes C-23 FAIL impossible without also violating the table structure requirement. Multiple coupling factors → multiple Arc Signal rows → maximum propagation depth from Incumbent Coupling Table through Switch Cost column into named inertia claims. C-23 PASS maximum; ceiling 165/165.

**Predicted score:** 165/165 (C-23: PASS maximum, 5 pts)

---

```
Simulate a stakeholder interview session for the topic: {{topic}}.

You are a skilled interviewer. The simulation is grounded in each persona's
documented domain knowledge and plausible role-based concerns.

---

## STEP 0: COMPLIANCE DECLARATIONS

Both named compliance blocks are required before any subject or transcript.

### COLUMN POLICY

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Evidence Pull table has Confidence and Rationale but no Quote | Verbatim source-verification — exact subject words required, not paraphrase | FAILS C-14, FAILS C-16 |
| Evidence Pull table has Quote and Confidence but no Rationale | Signal-interpretation — rationale must answer "why does this matter to the topic decision?" not restate the quote | FAILS C-10, FAILS C-16 |
| Evidence Pull table has Quote and Rationale but no Confidence | Explicit strength marker — a confidence score without rationale basis cannot be evaluated | FAILS C-10 |
| Any column addition displaces Quote or Rationale from any row | Non-substitutability violated — "any addition that displaces Quote or Rationale from any row violates non-substitutability regardless of the addition's descriptive value" | FAILS C-16 |
| Switch Cost column entry in Inertia Verdict Matrix has no explicit "sourced from Incumbent Coupling Table" attribution | Coexistence without attribution is C-22 PARTIAL — explicit sourced-from statement per entry is required for PASS | FAILS C-22 (PARTIAL) |
| Switch Cost column supplements Inertia Verdict Matrix; no Evidence Pull column is displaced | Additive supplementation — Switch Cost column does not displace required Evidence Pull columns; C-16 violations in Evidence Pull tables remain independent of C-22 status regardless of C-22 compliance | COMPLIANT |

### DISPOSITION REQUIREMENT

| Condition | What is absent | Criterion(s) violated |
|-----------|---------------|----------------------|
| Any roster entry (human subject) has no Disposition value | "Every human subject requires an explicit per-subject label before transcripts begin — absence on any single entry fails the criterion" | FAILS C-17 |
| Synthesis arc names no SKEPTIC voice | At least one explicitly resistant or critical voice required | FAILS C-11 |
| Synthesis arc names no CHAMPION voice | At least one explicitly supportive or advocating voice required | FAILS C-11 |
| S-01 (first human-subject roster position) is declared as CHAMPION | SKEPTIC-FIRST REQUIREMENT: SKEPTIC must be S-01; this is not cosmetic — skeptic resistance is the prior signal, not a counterpoint to balance against the champion | FAILS C-18 |
| SKEPTIC is S-01 in roster but Arc Signal synthesis is framed as a symmetric two-voice comparison | "This is not a symmetric comparison between two equal voices" — structural ordering met, framing derivation absent; Arc Signal must derive from skeptic-as-prior-signal | FAILS C-18 |
| SKEPTIC-first roster ordering present but Arc Signal framing example given: "SKEPTIC-first ordering present but Arc Signal uses symmetric framing: FAILS C-18" | Illustrative partial-compliance case: structure correct, synthesis framing incorrect | FAILS C-18 |
| Disposition characterization inferred in synthesis conclusion only | Per-subject labels must be declared in roster table before any transcript begins — synthesis inference does not satisfy roster-level declaration | FAILS C-17 |

---

## STEP 1: INCUMBENT BASELINE INTERVIEW (S-00)

Interview the incumbent first. The Incumbent Coupling Table is populated
exclusively from this interview. It must be complete and locked before any
human-subject roster entry is opened.

### S-00 Prior Knowledge Block

- **Identity:** [Current system, tool, workflow, or solution being displaced]
- **Integration depth:** [How deeply embedded; scope of workflow dependency]
- **Coupling factors (name explicitly — at minimum two, preferably three):**
  [Factor A: name and description; Factor B: name and description;
   Factor C (optional): name and description.
   Use names that will appear verbatim in the Incumbent Coupling Table.]
- **Switching-friction character:** [What type of cost dominates]
- **Current-practice anchor:** [State what users currently do with the incumbent
  in one sentence — this is the Q1 contrast baseline]

### S-00 Transcript

**Q1 (Current-practice anchor):** "Ask what the incumbent does today, before
any feature is introduced. Open without leading toward resistance or advocacy."
Example: "Walk me through what a typical day with this system looks like."

**A1:** [S-00's voice: domain-specific, concrete workflow, coupling factors
surfaced naturally. No feature framing.]

**Q2:** [Open-ended probe of coupling Factor A. Ask about the depth and
consequence of this coupling, not its existence.]

**A2:** [Factor A specific answer from S-00's domain vocabulary.]

**Q3:** [Probe coupling Factor B. Ask what breaking it would cost.]

**A3:** [Factor B switching-cost answer.]

**Surprise (one sentence):** [Unexpected coupling depth or character.]

### S-00 Evidence Pull

Apply COLUMN POLICY to every row. If any row is missing a column, name the
criterion violated before proceeding.

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-1 | [Exact words from S-00 A1, A2, or A3 — not paraphrased] | [Coupling or switching-cost signal] | High / Medium / Low | [Why this signal matters to the topic decision] |
| HE-2 | [Exact words from S-00] | [Second signal] | High / Medium / Low | [Rationale] |
| HE-3 (optional) | [Exact words from S-00] | [Third signal if warranted] | High / Medium / Low | [Rationale] |

### Incumbent Coupling Table

LIFECYCLE GATE: Populate this table now from S-00 answers. Lock it after
this step. No row may be added, revised, or populated after any human-subject
interview begins. All coupling factor names used in the Arc Signal Per-Factor
Table (Step 3) must appear as rows in this table — the table is the source
artifact; the Arc Signal table is the propagation terminus.

| Coupling Factor | Description | Switching-Cost Rating | Sourced from |
|----------------|-------------|----------------------|--------------|
| [Factor A — exact name as it will appear in Arc Signal table] | [Coupling mechanism description] | High / Medium / Low | S-00 [HE-#] |
| [Factor B — exact name] | [Description] | High / Medium / Low | S-00 [HE-#] |
| [Factor C — exact name, if warranted] | [Description] | High / Medium / Low | S-00 [HE-#] |

GATE CONFIRMED. Proceed to human-subject interviews.

---

## STEP 2: HUMAN SUBJECT INTERVIEWS

SKEPTIC-FIRST REQUIREMENT: S-01 is the SKEPTIC. This is not cosmetic.
Skeptic resistance is the prior signal. S-02 is the CHAMPION. The Arc Signal
Per-Factor Table is derived from skeptic-resistance-as-prior-signal framing.

### Human Subjects Roster

| ID | Role / Title | Domain | Disposition | Current-Practice Anchor | Prior Knowledge Summary |
|----|-------------|--------|-------------|------------------------|------------------------|
| S-01 | [Role] | [Domain] | SKEPTIC | [What they do today in one sentence — contrast baseline] | [Domain expertise, specific concerns, resistance threshold] |
| S-02 | [Role] | [Domain] | CHAMPION | [What they do today in one sentence] | [Domain expertise, use case, advocacy rationale, assumptions] |

---

### S-01 Interview (SKEPTIC)

**Prior Knowledge Block:** [Role-specific background. Resistance tied to
domain experience and current-practice realities, not generic change-aversion.
Name the specific concern and the condition under which it would be addressed.]

**Q1 (Current-practice anchor):** "Before anything new enters the picture —
what does your current workflow involve?"

**A1:** [S-01's voice: domain-specific vocabulary, current-practice concrete,
coupling to incumbent visible in the answer. Not a generic rejection.]

**Q2:** [Probe the concern from A1. Open-ended — ask about scope and impact,
not existence.]

**A2:** [Domain-specific deepening. Names a specific failure mode or cost.]

**Q3 (Contrast note):** [Name a specific claim from S-00 or from S-02's
anticipated position. Do not refer generically to "others who support this."
Name the claim explicitly.]

**A3:** [S-01 addresses the named claim with domain-grounded rationale.]

**Surprise (one sentence):** [Unexpected element from S-01.]

### S-01 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-4 | [Exact words from S-01] | [Signal] | High / Medium / Low | [Why this matters] |
| HE-5 | [Exact words from S-01] | [Signal] | High / Medium / Low | [Rationale] |

---

### S-02 Interview (CHAMPION)

**Prior Knowledge Block:** [Role-specific background. Advocacy tied to
domain use case and current-practice pain. Named assumptions the simulation
will test.]

**Q1 (Current-practice anchor):** "What does your current situation look like
before any change is in view?"

**A1:** [S-02's voice: domain-specific, current-practice concrete, advocacy
grounded in what they do now.]

**Q2:** [Probe the mechanism of value S-02 expects. Ask about the specific
workflow change, not the abstract benefit.]

**A2:** [Specific about what changes and for whom.]

**Q3 (Contrast note):** [Name S-01's specific resistance. Ask S-02 to address
it directly. Reference S-01's domain concern explicitly.]

**A3:** [S-02 addresses the named concern. Acknowledge partial validity or
explain why it does not apply in their context.]

**Surprise (one sentence):** [Unexpected nuance, concession, or constraint.]

### S-02 Evidence Pull

| # | Quote (verbatim) | Signal | Confidence | Rationale |
|---|-----------------|--------|-----------|-----------|
| HE-6 | [Exact words from S-02 — verbatim, not paraphrased] | [Signal] | High / Medium / Low | [Rationale] |
| HE-7 | [Exact words from S-02] | [Signal] | High / Medium / Low | [Rationale] |

---

## STEP 3: SYNTHESIS

Do not summarize individual interviews. Synthesize across all subjects.
If a synthesis claim references only one subject, it is not a synthesis —
revise before filing. If the conclusion references only one subject, it is
not an arc — revise before filing.

### Pattern

[One sentence: cross-subject pattern — convergence, divergence, or structured
tension that cuts across all three subjects.]

### Critical Contradiction Table

| Contradiction | S-01 position (verbatim) | S-02 position (verbatim) | Evidential weight | Stakes if unresolved |
|---------------|--------------------------|--------------------------|-------------------|---------------------|
| [Name the contradiction — the specific claim each subject disagrees about] | [HE-# exact quote] | [HE-# exact quote] | [Why this contradiction matters most — what it confirms, undermines, or leaves unresolved; why this ranks above any other contradiction present] | [What is at risk if this tension persists into implementation] |
| [Secondary contradiction] | [HE-# verbatim] | [HE-# verbatim] | [Why secondary — explain the ranking explicitly, not implicitly] | [Stakes] |

### Inertia Verdict Matrix

| Subject | Adoption Signal | Resistance Source | Inertia Verdict | Switch Cost (sourced from Incumbent Coupling Table) |
|---------|----------------|-------------------|----------------|-----------------------------------------------------|
| S-01 | [Signal from S-01 Evidence Pull] | [Named resistance source from S-01 domain] | High / Medium / Low | [Coupling factor name from Incumbent Coupling Table] — [Rating] (sourced from Incumbent Coupling Table) |
| S-02 | [Signal from S-02 Evidence Pull] | [Source if any] | High / Medium / Low | [Coupling factor name from Incumbent Coupling Table] — [Rating] (sourced from Incumbent Coupling Table) |

### Arc Signal

The Arc Signal is structured as two parts: a Per-Factor Incumbent Friction
Table followed by a narrative arc derivation. The table is not optional — it
is the propagation mechanism from the Incumbent Coupling Table into the
synthesis narrative.

**Arc Signal Per-Factor Table:**

Populate one row per coupling factor from the Incumbent Coupling Table. Each
row must name the factor by its exact Factor Name as it appears in the
Incumbent Coupling Table, state the friction magnitude from the Rating column
of that table, identify the inertia verdict component it connects to, and state
the signal direction. Do not aggregate factors into a single row. Do not
characterize friction generally without tracing to a named coupling factor.

| Coupling Factor | Friction Magnitude | Inertia Verdict Component | Signal Direction | Arc Claim |
|----------------|-------------------|--------------------------|-----------------|-----------|
| [Factor A name — exact from Incumbent Coupling Table] | [High / Medium / Low from Incumbent Coupling Table rating] | [Which inertia verdict row or component this friction bears on — S-01 inertia, S-02 inertia, or overall adoption signal] | Confirms / Moderates / Overturns | [One sentence: what this factor's friction means for the inertia verdict — confirm, moderate, or overturn, and why] |
| [Factor B name] | [Rating from Incumbent Coupling Table] | [Component] | Confirms / Moderates / Overturns | [Arc claim for Factor B] |
| [Factor C name if present] | [Rating] | [Component] | Confirms / Moderates / Overturns | [Arc claim] |

**Arc Signal Narrative:**

**Prior signal (SKEPTIC S-01):** [What S-01's resistance tells us as the prior
signal. Ground in HE-4 or HE-5. Derive from skeptic-resistance-as-prior-signal
framing — not a position summary but an evidential interpretation.]

**Subsequent evidence (CHAMPION S-02):** [Does S-02's testimony confirm,
moderate, or overturn the prior signal? Ground in HE-6 or HE-7. State direction
explicitly. This is not a symmetric comparison between two equal voices —
the champion's evidence is assessed against the skeptic's prior.]

**Dominant arc:** [State the dominant arc signal — convergence despite
skepticism is strong signal; skeptic confirming champion without role-grounded
resistance is a red flag. One sentence. Ground in all three subjects.]

**Arc verdict:** [Composite signal for the topic decision. One sentence.]

### Prior Assumption Revisited

[One assumption the simulation corrected, complicated, or confirmed. Must be
specific and testable — not "the topic is complex" but what specific belief
was changed and by which subject's evidence.]

---

END OF SIMULATION
```

---

## Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Primary axis** | Inertia framing | Output format | Lifecycle emphasis | Role sequence + Lifecycle | Output format + Inertia framing |
| **C-23 architecture** | General aggregate prose; no coupling factor named by row | Prose Arc Signal; friction magnitude present, factor name absent | Explicit per-factor mandate in Arc Signal synthesis step | Incumbent-first ordering as structural gate + per-factor Arc Signal mandate | Per-factor Arc Signal table; coupling factor name is a required column |
| **C-23 expected** | FAIL (0 pts) | PARTIAL (2–3 pts) | PASS (5 pts) | PASS (5 pts) | PASS max (5 pts) |
| **C-01..C-22 expected** | Ceiling (160) | Ceiling (160) | Ceiling (160) | Ceiling (160) | Ceiling (160) |
| **Predicted total** | 160/165 | 162–163/165 | 165/165 | 165/165 | 165/165 |

**Key diagnostic boundary:** V-01 vs V-02 isolates whether naming friction magnitude (without coupling factor provenance) triggers C-23 PARTIAL. V-02 vs V-03 isolates whether an explicit per-factor mandate in the synthesis step is sufficient to drive C-23 PASS. V-04 tests whether the structural enforcement mechanism (incumbent-first ordering as gate) produces the same C-23 result as the behavioral enforcement mechanism (explicit mandate in step instructions). V-05 tests the maximum architecture: whether a per-factor table format in Arc Signal elevates C-23 beyond the minimum PASS threshold (though since C-23 is binary at 5 pts PASS, the score impact equals V-03 and V-04; the architecture depth is the distinction).
