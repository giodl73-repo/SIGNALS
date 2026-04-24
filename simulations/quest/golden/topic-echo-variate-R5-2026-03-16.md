---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 5
rubric: v5
---

# Variations: `topic:echo` — Round 5

**Rubric:** v5 | **Date:** 2026-03-16

---

## Design Context

R4 scorecard produced two new excellence patterns that became C-17 and C-18 in v5:

- **C-17: Correction-Register Schema Design** — V-02 from R4 received PARTIAL on C-06
  (differential framing) specifically because its schema field names used
  discovery-register vocabulary ("Expected," "Finding"). V-01, V-03, V-04, V-05 from
  R4 all pass because their field names encode correction vocabulary ("Inherited
  assumption," "What the next team would build wrong"). The mechanism: framing is won
  or lost at schema design time. Discovery-register field names impose a ceiling on
  future-team framing that rules cannot fully compensate — rules must work harder to
  achieve what correction-register vocabulary provides structurally. C-17 PASS requires
  every schema field to be defined in correction vocabulary.

- **C-18: Verification Audit Layer** — V-05 from R4 uniquely achieves triple-enforcement
  because the portability audit creates a third structural layer: field definitions
  prohibit bad vocabulary, rules prohibit bad constructs, and the audit scan catches
  drift after entry production. Two-enforcement (field definition + rules) prohibits
  bad output at production time; three-enforcement (+ audit) catches drift after the
  fact. The audit loop is structurally distinct from prohibition because it fires post-
  production, requires the model to re-read each entry against named failure patterns,
  and its results are visible in the output. C-18 PASS requires a named phrase-trigger
  audit layer that executes after entry production and before synthesis.

**R5 structural goal:** Three single-axis variations test one new mechanism each above
the R4 V-04 base (which already achieves C-15, C-16, C-17). Two combined variations
test pairwise and full-set interaction. All five must maintain C-01 through C-18 without
degradation.

**Variation axes selected:**

1. **Output format** — Section-level correction-register vocabulary. R4 V-04 uses
   correction-register field names but neutral section headers ("SCHEMA", "FILTER",
   "RULES"). V-01 renames every section header in correction vocabulary. Tests whether
   the section-level mental frame matters beyond field-level vocabulary. Targets a
   potential C-19: Section-Frame Alignment.

2. **Lifecycle emphasis** — Explicit PASS/FAIL gate per entry. R4 V-05's portability
   audit scans against a phrase list. V-02 adds a formal gate: the model must declare
   a verdict token (PASS / FAIL) for every field of every entry, and gate results are
   visible in the output. Tests whether commitment-declaration produces stronger C-18
   compliance than phrase-detection alone. Targets a potential C-20: Gate-Cleared
   Commitment.

3. **Phrasing register** — Paired-contrast audit format. R4 V-05's audit lists
   prohibited phrases. V-03 replaces the prohibition list with discovery/correction
   paired transformations: "Discovery: 'signals may suggest X' → Correction: 'X
   [namespace:skill:artifact]'". Tests whether the register-shift teaching catches
   novel failure patterns that the phrase list does not cover. Targets whether C-18
   mechanism is phrase-detection or register-shift.

**Predicted score map (v5 rubric, max 100):**

| Variant | C-17 | C-18 | Predicted |
|---------|------|------|-----------|
| V-01    | PASS | FAIL | moderate gain over V-04 R4 if section frame matters |
| V-02    | PASS | PASS+ | higher than V-05 R4 if gate commitment outperforms phrase scan |
| V-03    | PASS | PASS+ | higher than V-05 R4 if paired contrast catches novel drift |
| V-04    | PASS | PASS+ | highest of singles if section frame + gate reinforce |
| V-05    | PASS | PASS++ | max if all three mechanisms compound |

The key differential: if V-01 scores similarly to V-04 from R4, section-level headers
add nothing (field vocabulary is sufficient). If V-02 or V-03 outscores V-05 from R4
on C-18, the respective audit mechanism is stronger than phrase-list scanning. The
V-04 vs V-05 differential tests whether the paired-contrast audit adds to gate scoring,
or whether gate scoring already catches what the contrast format would catch.

**What C-19 / C-20 would require:**

If section-level correction vocabulary matters, C-19 (Section-Frame Alignment) would
require: every section header uses correction vocabulary ("CORRECTION RECORD" not
"SCHEMA", "CORRECTION ENFORCEMENT" not "RULES") so that the model's frame for the
section matches the register of the fields. A section called "SYNTHESIS" creates a
discovery/assembly frame that competes with correction-register field vocabulary; a
section called "PATTERN OF INHERITED ERRORS" reinforces it.

If gate-cleared commitment matters, C-20 (Gate-Cleared Commitment) would require: the
model declares explicit PASS/FAIL per field per entry, the declarations are visible in
the output, and the gate is not cleared until all fields pass. The gate is structurally
distinct from C-18's audit because: (1) it produces a visible, auditable verdict record,
(2) it requires re-reading each field against a specific criterion — not scanning against
a pattern list — and (3) it blocks synthesis progression until cleared.

---

## V-01 — Single-axis: Output format — Section-level correction-register vocabulary

**Variation axis:** Output format — Every section header uses correction-register
vocabulary. "SCHEMA" → "CORRECTION RECORD". "FILTER" → "STILL-LIVE FILTER".
"RULES" → "CORRECTION ENFORCEMENT". "SYNTHESIS" (pattern section) → "PATTERN OF
INHERITED ERRORS". "BLIND SPOT MAP" is retained (already correction-register).
"FORWARD GUIDANCE" → "CORRECTION FORWARD STATEMENT". "SCOPE NEGATION" → "WHAT THIS
CORRECTION RECORD EXCLUDES". "OUTPUT" → "ARTIFACT STRUCTURE". No other content
changes from R4 V-04.

**Hypothesis:** R4 V-04 achieves C-17 via field names ("Inherited assumption,"
"Consequence if missing") but uses neutral section headers that do not carry a
correction frame. When the section is called "SCHEMA", the model's cognitive frame for
the section is inventory-completion — a discovery/assembly operation. When it is called
"CORRECTION RECORD", the frame for the entire section is corrective before a single
field is filled. If section headers are the primary frame and field vocabulary is a
secondary constraint, neutral section headers impose a ceiling on C-17 compliance. If
field vocabulary alone is sufficient (as R4 V-04 suggests), section-level renaming
adds nothing detectable. C-18 is not added — this variation tests section-level
vocabulary in isolation.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Correction A".]

  Source:          [namespace:skill:artifact — e.g., prove:interview:signal-interview-
                   2026-03-14.md. Not "signals indicated" / "research showed" /
                   "the data suggested".]

  Inherited assumption:
                   [The belief a new team would carry into this design today, reading
                   only the current spec, proposal, and design documents. State as:
                   "Today's materials imply..." or "A new team reading the current
                   spec would assume..."
                   Test: "If a new engineer joined tomorrow and read only the current
                   design docs, would they hold this assumption?" If no, rewrite.
                   Degree variants fail: name the assumption the finding overturns,
                   not a magnitude of the same direction.]

  What the signals showed instead:
                   [The correction — directly contradicts the inherited assumption.
                   Direct claim. No hedges. Prohibited: "may suggest" / "appears to
                   indicate" / "seems like" / "could mean" / "might be" / "it is
                   possible that".]

  Consequence if missing:
                   [The specific design error the next team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the consequence.]

  Before proceeding, the next team must:
                   [The specific action or blocking question. Not "further investigation
                   needed" / "keep an eye on this" / "monitor this".]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry, apply the still-live filter:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES → correction is load-bearing. Draft the entry.
  NO  → the current materials have absorbed this finding. Exclude it. Absorbed
        findings belong in topic-story, not topic-echo.

This filter is not optional — it is the primary selection criterion. Apply before
writing any field.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 — Correction framing:
  Every entry is written for the next team, not narrated from the original team's
  experience. "We found that X" is discovery framing — rewrite as "Today's materials
  imply X; they should not, because the signals showed Y." The Inherited assumption
  field has no "we" — it has only "today's materials" and "a new team."

Rule 2 — Claim-only voice:
  State every correction as a direct claim. The prohibited constructs from "What the
  signals showed instead" apply to every field. Uncertainty is a rewrite instruction.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials imply, what they should imply instead, and what the next
  team would build wrong without this correction. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one correction must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which the original team corrected in [A]+[B] together."
Co-citation without a named gap statement fails this requirement.

== INHERITED ASSUMPTION ORDERING ===============================================

Order all entries HIGH → MEDIUM → LOW by Severity. Unordered lists fail.

== PATTERN OF INHERITED ERRORS =================================================

After all entries, write one section: "Pattern of inherited errors."

Do two or more corrections share a structural origin — a family of things today's
materials systematically lead new readers to assume wrongly? Write 2-4 sentences.
Name any pattern; if none exists, state that explicitly: "The corrections address
independent inherited assumptions with no shared structural origin in today's materials."

== BLIND SPOT MAP ==============================================================

After the pattern section, write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking that produced multiple independent corrections.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

Category names must characterize the *type* of wrong thinking, not the subject matter.

  PASS: "Sequence inversion — materials assumed X precedes Y; signals showed Y precedes
         X, invalidating the commit ordering assumption"
  PASS: "Actor misidentification — materials assumed friction originates from end users;
         signals showed it originates from platform infrastructure"
  FAIL: "State management" — labels a domain, not a type of wrong thinking
  FAIL: "User behavior issues" — labels a topic, not a structural error

A category label that could appear unchanged in an echo about a different topic fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

If a correction shares no blind spot type with any other, list it as "Unclassified"
and state in one sentence why it does not fit any named category.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences.

NON-DERIVABILITY CONSTRAINT: The synthesis must state something not visible from
reading individual corrections or from tallying category assignments. Do not tally
assignments. State what the *pattern of blind spots* reveals about the original
materials as a system — a claim that requires seeing the full map to make.

If no pattern exists: "The corrections address independent blind spots with no shared
structural origin in today's materials."

== CORRECTION FORWARD STATEMENT ================================================

Write 1-3 sentences addressed directly to the next team. Register: "Before you build
{topic}, the correction record requires you to know that..." or "Today's design
materials do not warn you that..." Specific to these corrections — not generic.

== WHAT THIS CORRECTION RECORD EXCLUDES =========================================

Name at least two excluded categories with counts:
  e.g., "Absorbed corrections: [N] findings the current materials already reflect"
       "Discovery narratives: excluded as past-team experience, not next-team corrections"
Implicit exclusion (simply not including non-corrections) does not satisfy this.

== ARTIFACT STRUCTURE ==========================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Pattern of inherited errors
  3. Blind Spot Map
  4. Correction forward statement
  5. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-02 — Single-axis: Lifecycle emphasis — Explicit PASS/FAIL gate per entry

**Variation axis:** Lifecycle emphasis — After drafting all entries, the model runs a
formal ENTRY GATE: it declares a PASS or FAIL verdict for every field of every entry,
in visible output. The gate blocks all synthesis sections until every entry is CLEARED.
Gate declarations appear in the artifact output.

**Hypothesis:** C-18 established that an audit layer with named phrase triggers catches
drift post-production. R4 V-05's portability audit requires the model to scan each field
against a list of named failure patterns and rewrite on match. This is passive detection —
the model reads, checks, rewrites. A PASS/FAIL gate is structurally different: the model
must produce a verdict token for each field, the token is visible in the output, and the
gate verdict is auditable by a reviewer. Two structural properties emerge that phrase-list
scanning lacks: (1) the model commits to a quality judgment before proceeding — not just
scanning for known patterns but evaluating whether the field meets its criterion, and
(2) the verdict record is externally reviewable. If gate scoring produces stronger C-18
compliance than phrase-list scanning, the load-bearing component is the commitment
mechanism, not the phrase detection. If they score equivalently, phrase-list scanning is
sufficient. C-19 (Section-Frame Alignment) is not tested — section headers remain neutral.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption.

== SCHEMA =====================================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Surprise A".]

  Source:          [namespace:skill:artifact — e.g., prove:interview:signal-interview-
                   2026-03-14.md. Not "signals indicated" / "research showed" /
                   "the data suggested".]

  Inherited assumption:
                   [The belief a new team would carry into this design today, reading
                   only the current spec, proposal, and design documents. State as:
                   "Today's materials imply..." or "A new team reading the current
                   spec would assume..."
                   Test: "If a new engineer joined tomorrow and read only the current
                   design docs, would they hold this assumption?" If no, rewrite.
                   Degree variants fail: name the assumption the finding overturns,
                   not a magnitude of the same direction.]

  What the signals showed instead:
                   [The correction — directly contradicts the inherited assumption.
                   Direct claim. No hedges. Prohibited: "may suggest" / "appears to
                   indicate" / "seems like" / "could mean" / "might be" / "it is
                   possible that".]

  Consequence if missing:
                   [The specific design error the next team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the consequence.]

  Before proceeding, the next team must:
                   [The specific action or blocking question. Not "further investigation
                   needed" / "keep an eye on this" / "monitor this".]

  Severity:        [HIGH / MEDIUM / LOW]

== FILTER =====================================================================

Before drafting any entry, apply the still-consequential filter:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES → correction is load-bearing. Draft the entry.
  NO  → the current materials have absorbed this finding. Exclude it. Absorbed
        findings belong in topic-story, not topic-echo.

== RULES ======================================================================

Rule 1 — Correction framing:
  Every entry is written for the next team, not narrated from the original team's
  experience. "We found that X" is discovery framing — rewrite as "Today's materials
  imply X; they should not." The Inherited assumption field has no "we."

Rule 2 — Claim-only voice:
  Direct claims only. No hedges. The prohibited constructs from "What the signals
  showed instead" apply to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials imply, what they should imply instead, and what the next
  team would build wrong. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one correction must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which the original team corrected in [A]+[B] together."

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW. Unordered lists fail.

== ENTRY GATE =================================================================

After drafting all entries, run the ENTRY GATE before proceeding to any synthesis
section. The gate produces visible output — declarations appear in the artifact.
Do not internalize or skip.

For each entry, produce a gate block in this format:

  GATE: [entry Name]
    Source             [PASS: namespace:skill:artifact format confirmed]
                       [FAIL: vague attribution — rewrite to namespace:skill:artifact]
    Inherited assumption
                       [PASS: future-team framing confirmed — "Today's materials imply..."
                        or "A new team reading the current spec would assume..."]
                       [FAIL: original-team narration — "We found / We expected / The team
                        believed" — rewrite to state what today's materials still imply]
    Signals showed     [PASS: direct claim, no prohibited hedge constructs confirmed]
                       [FAIL: hedge construct found — identify and rewrite]
    Consequence        [PASS: specific component, flow, or decision named]
                       [FAIL: severity statement or generic impact — rewrite to name the
                        specific wrong design]
    Next move          [PASS: specific action or blocking decision confirmed]
                       [FAIL: deferral language — rewrite to a specific decision point]
  STATUS: CLEARED / NOT CLEARED

Gate criteria:
  Source PASS: namespace:skill:artifact format. Any vague attribution fails.
  Inherited assumption PASS: explicitly states what today's materials imply, in future-
    team register. "The team expected..." or "We found..." fails.
  Signals showed PASS: zero prohibited hedge constructs in the field. One fails.
  Consequence PASS: a specific component, flow, or decision named. Any prohibited
    softener ("worth noting," "has implications") fails.
  Next move PASS: a specific decision point or blocking open question. "Further
    investigation" or "keep an eye on" fails.

STATUS NOT CLEARED: rewrite every FAIL field. Re-run the gate block. Repeat until
STATUS: CLEARED.

Do not proceed to the Blind Spot Map until every entry gate shows STATUS: CLEARED.

== BLIND SPOT MAP ==============================================================

After all gates are CLEARED, write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking that produced multiple independent corrections.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

Category names must characterize the *type* of wrong thinking, not the subject matter.

  PASS: "Sequence inversion — materials assumed X precedes Y; signals showed Y precedes
         X, invalidating the commit ordering assumption"
  PASS: "Actor misidentification — materials assumed friction originates from end users;
         signals showed it originates from platform infrastructure"
  FAIL: "State management" — labels a domain, not a type of wrong thinking
  FAIL: "User behavior issues" — labels a topic, not a structural error

A category label that could appear unchanged in an echo about a different topic fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

If a correction shares no blind spot type with any other, list it as "Unclassified"
and state in one sentence why it does not fit any named category.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences.

NON-DERIVABILITY CONSTRAINT: The synthesis must state something not visible from
reading individual corrections or from tallying category assignments. Do not tally.
State what the *pattern of blind spots* reveals about the original materials as a
system — a claim that requires seeing the full map to make.

If no pattern exists: "The corrections address independent blind spots with no shared
structural origin in today's materials."

== META-REFLECTION ============================================================

"What the surprise distribution reveals."

Where did corrections concentrate (namespace, phase, signal type)? Prescribe:
"For topics like this one, run [X] before [Y] to surface [Z class of correction]
earlier." Prescribe — do not only observe.

== SCOPE NEGATION =============================================================

"What this artifact excludes."
Name at least two excluded categories with counts.
Implicit exclusion does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Entry Gate blocks (one per entry, all showing STATUS: CLEARED)
  3. Blind Spot Map
  4. What the surprise distribution reveals
  5. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-03 — Single-axis: Phrasing register — Paired-contrast register audit

**Variation axis:** Phrasing register — The audit section replaces the phrase-prohibition
list with paired transformations: for each field type, a discovery-register version is
shown alongside its correction-register rewrite. The audit teaches the register shift
rather than listing prohibited patterns.

**Hypothesis:** C-18's audit layer (R4 V-05) catches drift by listing specific prohibited
phrases ("signals indicated", "may suggest"). A model that produces semantically equivalent
drift using unlisted phrasing is not caught. A paired-contrast audit teaches the register
distinction itself: when the audit shows "Discovery: 'The data appears to indicate X'
→ Correction: 'X [namespace:skill:artifact]'", the model can generalize the shift to
novel failure patterns the prohibition list does not name. Two structural properties
differ from R4 V-05: (1) the audit is generative, not enumerative — it teaches a
transformation rule rather than a pattern match, and (2) the contrast is visible in the
output, making the register distinction explicit and inspectable. If paired-contrast
catches more drift types, the mechanism is register-shift teaching. If phrase-list and
paired-contrast score equivalently on C-18, enumerative detection is sufficient and
teaching adds no structural benefit. C-19 (Section-Frame Alignment) is not tested —
section headers remain neutral.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption without this artifact.

== SCHEMA =====================================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Surprise A".]

  Source:          [namespace:skill:artifact — e.g., scout:feasibility:signal-
                   feasibility-2026-03-14.md. Not "signals indicated" / "research
                   showed" / "the data suggested".]

  What today's materials imply:
                   [What a new team reading only the current spec, proposal, and
                   design documents would assume. Write as: "Today's materials imply
                   that..." or "A new team reading the current spec would assume..."
                   Degree variants fail: name the assumption the finding factually
                   overturns, not a magnitude of the same direction.
                   Generic-material-critique language fails: "Materials tend to
                   underspecify concurrency behavior" describes a category, not what
                   today's specific materials imply to a new reader of this topic.]

  What the signals showed instead:
                   [The correction — directly contradicts what today's materials imply.
                   Direct claim. Prohibited: "may suggest" / "appears to indicate" /
                   "seems like" / "could mean" / "might be" / "it is possible that".]

  What the next team would build wrong:
                   [The specific design error a new team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the specific wrong design.]

  What the next team must decide before proceeding:
                   [Specific question or action. Not "further investigation needed" /
                   "keep an eye on this" / "monitor this". A specific blocking
                   decision or open question.]

  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Still-live filter:
  Before drafting any entry: "Does today's design material still imply the false
  assumption this finding corrects?" If the current materials have already absorbed
  this correction, exclude it. Apply as a discard filter.

Rule 2 — Claim-only voice:
  State every correction as a direct claim. No hedges. Apply prohibited constructs
  from "What the signals showed instead" to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials lead them to assume, what they should assume instead, and
  what they would build wrong. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries. Order HIGH → MEDIUM → LOW by Severity.
Do not write synthesis sections yet.

== PHASE 2: REGISTER AUDIT ====================================================

Before writing the Blind Spot Map, execute the REGISTER AUDIT against every entry.

The audit applies the discovery/correction register contrast to every non-Name field.
For each field, the question is: "Is this written from the original team's discovery
perspective, or from the next team's correction-need perspective?"

Apply these paired transformations field by field. Any field in discovery register
must be rewritten in correction register before proceeding.

  Source field:
    DISCOVERY: "signals indicated X" / "research showed X" / "the data suggested X"
               / "analysis revealed X" / "our investigation found X"
    CORRECTION: "namespace:skill:artifact"
    Transformation: Remove attribution prose. Identify the specific artifact that
    produced this finding. Write only the path: namespace:skill:artifact.

  What today's materials imply:
    DISCOVERY: "We found that adoption would be high" / "The team expected X"
               / "We learned that the flow does not X" / "Our assumption was X"
    CORRECTION: "Today's materials imply that..." / "A new team reading the current
                 spec would assume..."
    Transformation: Remove the original team as subject. The subject is "today's
    materials" or "a new team reading today's materials." State only what those
    materials still lead a reader to assume.

    DISCOVERY: "Materials tend to underspecify X" / "Specs rarely address Y"
               / "Teams typically assume Z" / "It is common to overlook Y"
    CORRECTION: "Today's spec implies X will behave as [specific claim] — it will not"
    Transformation: Remove the category observation. State the specific assumption
    this specific topic's materials produce. Generic-category critique could appear
    in any echo — rewrite to the inherited assumption a new reader of this topic holds.

  What the next team would build wrong:
    DISCOVERY: "This finding is worth noting" / "This bears watching"
               / "This has implications for design" / "This is important to keep in mind"
    CORRECTION: "[Component/flow/decision] would be built as [wrong design] because
                 today's materials imply [wrong assumption] — and [wrong design] fails
                 when [condition]"
    Transformation: Remove the severity statement. Name the concrete wrong design.
    One team member should be able to read this field and know exactly what they would
    have built incorrectly and why.

  What the next team must decide before proceeding:
    DISCOVERY: "Further investigation needed" / "Keep an eye on this"
               / "Monitor this" / "Investigate further" / "More research required"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"
               / "[Specific question: does [component] guarantee [property] when [condition]?]"
    Transformation: Remove the deferral. Name the decision the next team must actually
    make, or the open question they must answer, before they can proceed. A rewritten
    action field is blocking — it stops work until resolved.

The register audit is complete when every non-Name field of every entry is in
correction register. Proceed to Phase 3 only when audit is complete.

== PHASE 3: BLIND SPOT MAP ====================================================

After the register audit: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking, not a topic area.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

Category names must characterize the *type* of wrong thinking:

  PASS: "Ownership inversion — materials assumed the caller owns X; signals showed
         the callee owns X, reversing the allocation model"
  PASS: "Actor scope underestimation — materials bounded the problem to internal
         consumers; signals showed external consumers are the primary failure surface"
  FAIL: "State management" — labels a domain
  FAIL: "Unexpected behavior" — labels that something happened, not what was wrong

A category label transferable to a different topic without rewriting fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences.

NON-DERIVABILITY CONSTRAINT: The synthesis must state something not visible from
reading individual entries or from reading the category assignments. Do not tally.
State what the *pattern of blind spots* reveals about the original materials as a whole.

If no pattern: "The corrections address independent blind spots; the map reveals no
shared structural origin in today's materials."

== PHASE 4: META-REFLECTION ===================================================

"What the surprise distribution reveals."

Where did corrections concentrate? Prescribe: "For topics like this one, run [X]
before [Y] to surface [Z class of correction] earlier." Prescribe — do not only observe.

== PHASE 5: SCOPE NEGATION ====================================================

"What this artifact excludes."
Name at least two excluded categories with counts.
Implicit exclusion does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Blind Spot Map
  3. What the surprise distribution reveals
  4. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-04 — Combined: Output format + Lifecycle emphasis (Section-level vocabulary + PASS/FAIL gate)

**Axes combined:** V-01's section-level correction-register vocabulary + V-02's explicit
PASS/FAIL gate per entry.

**Hypothesis:** The two mechanisms address non-overlapping phases of production. Section
headers fire at frame-setting time — before a single field is filled, the model's
cognitive frame for what it is doing is established by the section name. The PASS/FAIL
gate fires after all entries are drafted — it creates an explicit commitment record.
No interaction surface exists between them: the section frame does not constrain how
the gate evaluates fields; the gate does not depend on section vocabulary. Together
they provide coverage at both ends of entry production: section-level framing sets
the register before production; gate scoring enforces it after. The combination does
not add cognitive overhead beyond V-01 and V-02 individually because the framing phase
and the gate phase are sequentially separated. Predicted differential from V-05: V-05
adds the paired-contrast register audit (V-03). If the combination of section framing
and gate scoring already catches all register drift, V-03's audit adds nothing.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Correction A".]

  Source:          [namespace:skill:artifact — e.g., prove:interview:signal-interview-
                   2026-03-14.md. Not "signals indicated" / "research showed" /
                   "the data suggested".]

  Inherited assumption:
                   [The belief a new team would carry into this design today, reading
                   only the current spec, proposal, and design documents. State as:
                   "Today's materials imply..." or "A new team reading the current
                   spec would assume..."
                   Test: "If a new engineer joined tomorrow and read only the current
                   design docs, would they hold this assumption?" If no, rewrite.
                   Degree variants fail: name the assumption the finding overturns,
                   not a magnitude of the same direction.]

  What the signals showed instead:
                   [The correction — directly contradicts the inherited assumption.
                   Direct claim. No hedges. Prohibited: "may suggest" / "appears to
                   indicate" / "seems like" / "could mean" / "might be" / "it is
                   possible that".]

  Consequence if missing:
                   [The specific design error the next team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the consequence.]

  Before proceeding, the next team must:
                   [The specific action or blocking question. Not "further investigation
                   needed" / "keep an eye on this" / "monitor this".]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry, apply the still-live filter:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES → correction is load-bearing. Draft the entry.
  NO  → the current materials have absorbed this finding. Exclude it. Absorbed
        findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 — Correction framing:
  Every entry is written for the next team, not narrated from the original team's
  experience. "We found that X" is discovery framing — rewrite as "Today's materials
  imply X; they should not." The Inherited assumption field has no "we."

Rule 2 — Claim-only voice:
  Direct claims only. No hedges. The prohibited constructs from "What the signals
  showed instead" apply to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials imply, what they should imply instead, and what the next
  team would build wrong. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one correction must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which the original team corrected in [A]+[B] together."

== INHERITED ASSUMPTION ORDERING ===============================================

Order all entries HIGH → MEDIUM → LOW. Unordered lists fail.

== ENTRY GATE =================================================================

After drafting all entries, run the ENTRY GATE before proceeding to any synthesis
section. Gate declarations appear in the artifact — do not skip or internalize.

For each entry, produce a gate block:

  GATE: [entry Name]
    Source             [PASS: namespace:skill:artifact format confirmed]
                       [FAIL: {specific problem} — rewrite required]
    Inherited assumption
                       [PASS: future-team framing confirmed — "Today's materials imply..."
                        format or equivalent]
                       [FAIL: original-team narration found — rewrite to state what
                        today's materials still imply]
    Signals showed     [PASS: direct claim, no prohibited hedges]
                       [FAIL: {hedge construct identified} — rewrite required]
    Consequence        [PASS: specific component, flow, or decision named]
                       [FAIL: {softener or generic impact} — rewrite to name the wrong design]
    Next move          [PASS: specific action or blocking question confirmed]
                       [FAIL: {deferral language} — rewrite to specific decision point]
  STATUS: CLEARED / NOT CLEARED

STATUS NOT CLEARED: rewrite every FAIL field. Re-run the gate block. Repeat until
STATUS: CLEARED. Do not proceed to the Pattern of Inherited Errors until every entry
shows STATUS: CLEARED.

== PATTERN OF INHERITED ERRORS =================================================

After all gates CLEARED, write one section: "Pattern of inherited errors."

Do two or more corrections share a structural origin — a family of false assumptions
today's materials systematically produce? Write 2-4 sentences. Name any pattern; if
none, state that explicitly.

== BLIND SPOT MAP ==============================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking, not a topic area.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

  PASS: "Sequence inversion — materials assumed X precedes Y; signals showed Y precedes
         X, invalidating the commit ordering assumption"
  FAIL: "State management" — labels a domain, not a type of wrong thinking

A category label that could appear unchanged in an echo about a different topic fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: state something not visible from
reading individual corrections or tallying category assignments. Do not tally.

If no pattern: "The corrections address independent blind spots with no shared
structural origin in today's materials."

== CORRECTION FORWARD STATEMENT ================================================

Write 1-3 sentences to the next team. Register: "Before you build {topic}, the
correction record requires you to know that..." Specific to these corrections.

== WHAT THIS CORRECTION RECORD EXCLUDES =========================================

Name at least two excluded categories with counts. Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ==========================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Entry Gate blocks (all STATUS: CLEARED)
  3. Pattern of inherited errors
  4. Blind Spot Map
  5. Correction forward statement
  6. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-05 — Combined: All three axes (Section vocabulary + PASS/FAIL gate + Paired-contrast audit)

**Axes combined:** V-01's section-level correction-register vocabulary + V-02's explicit
PASS/FAIL gate + V-03's paired-contrast register audit.

**Hypothesis:** The three mechanisms target three distinct failure modes at three
different production stages: (1) section-level framing sets the cognitive register
before any field is filled; (2) the paired-contrast audit catches register drift after
entry production by teaching the transformation rule, not just listing violations;
(3) the PASS/FAIL gate forces an explicit commitment declaration after the audit, making
the quality judgment visible and auditable. Each mechanism fires at a non-overlapping
execution point. The predicted interaction: correction-register section framing (V-01)
primes the model toward correction vocabulary throughout; the paired-contrast audit
(V-03) catches drift using transformation rules rather than pattern lists, handling
novel failure patterns; the gate (V-02) creates a final commitment record. If V-05
outscores V-04 on C-18, the paired-contrast audit catches drift that section framing
and gate scoring miss together. The three mechanisms are hypothesized to be additive
without interference.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption without this artifact.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Correction A".]

  Source:          [namespace:skill:artifact — e.g., scout:feasibility:signal-
                   feasibility-2026-03-14.md. Not "signals indicated" / "research
                   showed" / "the data suggested".]

  What today's materials imply:
                   [What a new team reading only the current spec, proposal, and
                   design documents would assume. Write as: "Today's materials imply
                   that..." or "A new team reading the current spec would assume..."
                   Degree variants fail: name the assumption the finding factually
                   overturns, not a magnitude of the same direction.
                   Generic-material-critique language fails: "Materials tend to
                   underspecify X" describes a category, not what today's specific
                   materials imply to a new reader of this topic.]

  What the signals showed instead:
                   [The correction — directly contradicts what today's materials imply.
                   Direct claim. Prohibited: "may suggest" / "appears to indicate" /
                   "seems like" / "could mean" / "might be" / "it is possible that".]

  What the next team would build wrong:
                   [The specific design error a new team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the specific wrong design.]

  What the next team must decide before proceeding:
                   [Specific question or action. Not "further investigation needed" /
                   "keep an eye on this" / "monitor this". A specific blocking
                   decision or open question.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry, apply the still-live filter:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES → correction is load-bearing. Draft the entry.
  NO  → excluded. Absorbed findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 — Correction framing:
  Every entry is written for the next team. Discovery framing ("We found that X") is
  prohibited — rewrite as "Today's materials imply X; they should not." No "we" in
  the "What today's materials imply" field.

Rule 2 — Claim-only voice:
  Direct claims only. No hedges. Prohibited constructs from "What the signals showed
  instead" apply to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials lead them to assume, what they should assume instead, and
  what they would build wrong. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries. Order HIGH → MEDIUM → LOW by Severity.
Do not write synthesis sections yet.

== PHASE 2: REGISTER AUDIT ====================================================

Before writing the Blind Spot Map, execute the REGISTER AUDIT. Apply these paired
transformations field by field to every entry. Rewrite any field in discovery register
before proceeding to Phase 3.

  Source field:
    DISCOVERY: "signals indicated X" / "research showed X" / "analysis revealed X"
    CORRECTION: namespace:skill:artifact
    → Any attribution prose fails. Replace with the artifact path.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X" / "We assumed X"
    CORRECTION: "Today's materials imply that..." / "A new team reading the current
                 spec would assume..."
    → Original-team narration fails. Rewrite to future-team framing.

    DISCOVERY: "Materials tend to underspecify X" / "Specs rarely address Y"
               / "It is common to overlook Y"
    CORRECTION: "Today's spec implies X will behave as [specific claim] — it will not"
    → Generic-category critique fails. Rewrite to the specific inherited assumption.

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching" / "Has implications" / "Important
                to keep in mind"
    CORRECTION: "[Component/flow/decision] would be built as [wrong design] because
                 today's materials imply [wrong assumption]"
    → Severity statements fail. Rewrite to the specific wrong design.

  What the next team must decide before proceeding:
    DISCOVERY: "Further investigation needed" / "Keep an eye on" / "Monitor this"
               / "Investigate further"
    CORRECTION: "[Specific decision: choose X or Y before building Z]" / "[Specific
                 question: does [component] guarantee [property] when [condition]?]"
    → Deferrals fail. Rewrite to a specific blocking decision or open question.

Register audit complete when every non-Name field of every entry is in correction register.

== PHASE 3: ENTRY GATE ========================================================

After the register audit, run the ENTRY GATE. Gate declarations appear in the artifact.

For each entry, produce a gate block:

  GATE: [entry Name]
    Source             [PASS: namespace:skill:artifact confirmed]
                       [FAIL: {problem} — rewrite required]
    Materials imply    [PASS: future-team framing confirmed]
                       [FAIL: original-team narration or generic critique — rewrite]
    Signals showed     [PASS: direct claim, no hedges]
                       [FAIL: {hedge} — rewrite required]
    Wrong design       [PASS: specific component/flow/decision named]
                       [FAIL: softener found — rewrite to specific wrong design]
    Next decision      [PASS: specific blocking decision or question confirmed]
                       [FAIL: deferral — rewrite to specific decision point]
  STATUS: CLEARED / NOT CLEARED

STATUS NOT CLEARED: rewrite FAIL fields. Re-run. Repeat until CLEARED.
Proceed to Phase 4 only when all entries show STATUS: CLEARED.

== PHASE 4: PATTERN OF INHERITED ERRORS =========================================

After all gates CLEARED, write one section: "Pattern of inherited errors."

Do two or more corrections share a structural origin — a family of false assumptions
today's materials systematically produce? Write 2-4 sentences. Name any pattern; if
none, state that explicitly.

== PHASE 5: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking, not a topic area.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

Category names must characterize the *type* of wrong thinking:

  PASS: "Ownership inversion — materials assumed the caller owns X; signals showed
         the callee owns X, reversing the allocation model"
  FAIL: "State management" — labels a domain, not a type of wrong thinking

A category label transferable to a different topic without rewriting fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: state something not visible from
reading individual corrections or tallying category assignments. State what the
*pattern of blind spots* reveals about the original materials as a system.

If no pattern: "The corrections address independent blind spots; the map reveals no
shared structural origin in today's materials."

== PHASE 6: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. Register: "Before you build {topic}, the
correction record requires you to know that..." or "Today's design materials do not
warn you that..." Specific to these corrections — not generic.

== PHASE 7: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.
Implicit exclusion does not satisfy this.

== ARTIFACT STRUCTURE ==========================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Entry Gate blocks (all STATUS: CLEARED)
  3. Pattern of inherited errors
  4. Blind Spot Map
  5. Correction forward statement
  6. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## Round 5 Design Notes

**Why these three axes:**

- **Output format** (V-01) tests whether section-level correction vocabulary adds
  structural enforcement beyond field-level vocabulary. R4 V-04 uses neutral section
  headers; V-01 renames every section in correction register. If section headers are
  the primary cognitive frame for what the model is doing (not just field labels), then
  "CORRECTION RECORD" vs "SCHEMA" changes the production mode before a single field
  is written. If field vocabulary is sufficient, V-01 scores identically to V-04 from R4.

- **Lifecycle emphasis** (V-02) tests whether a formal PASS/FAIL gate with visible
  verdict declarations produces stronger C-18 compliance than phrase-list scanning. The
  structural difference: the gate requires an explicit commitment to each field's quality,
  visible in the output. Phrase-list scanning is passive detection; gate scoring is active
  evaluation. If the commitment mechanism is load-bearing, V-02 outscores R4 V-05 on C-18.

- **Phrasing register** (V-03) tests whether a paired-contrast audit catches novel drift
  patterns that a prohibition list misses. The structural difference: the paired contrast
  teaches the transformation rule, not the violation. A model that reads
  "DISCOVERY: 'We found X' → CORRECTION: 'Today's materials imply X'" can apply the rule
  to "Our investigation showed X" — an unlisted discovery-register phrase. If the
  generalization is load-bearing, V-03 outscores R4 V-05 on C-18 for novel drift patterns.

**Predicted interaction in V-04:**

Section headers (V-01) and gate scoring (V-02) fire at non-overlapping points: headers
fire before production; gate fires after. The only potential interaction: do
correction-register section headers produce entries that are easier to gate-pass? If
the section frame reduces production-time drift, V-04 may show shorter gate correction
cycles than V-02 alone. If not, V-04 scores as V-01 + V-02 independently.

**Predicted interaction in V-05:**

V-05 adds paired-contrast audit (V-03) between draft and gate. The predicted interaction:
the audit cleans discovery-register drift before the gate, so the gate in V-05 runs
against cleaner entries than in V-02 or V-04. If the audit is effective, V-05's gate
should show a higher initial CLEARED rate than V-04's gate. The observable: count of
NOT CLEARED verdicts before rewrite. If V-05 produces fewer NOT CLEARED verdicts, the
paired-contrast audit is doing advance cleaning that reduces gate failures.

**What R5 cannot tell us:**

If V-01 and V-04 from R4 score identically, section-level vocabulary adds nothing —
but this only tells us that for models that already achieve C-17 via field vocabulary,
section headers are redundant. For models that fail C-17, section headers may be
necessary. R5 tests the marginal case (already-passing base + added section frame);
it does not test section headers as a standalone recovery mechanism for C-17-failing
variations.
