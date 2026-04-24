The existing R7 file uses a different criterion numbering (from a mismatched rubric lineage). Here are the fresh Round 7 variations based on the current v7 rubric:

---

```markdown
---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 7
rubric: v7
---

# Variations: `topic:echo` -- Round 7

**Rubric:** v7 | **Date:** 2026-03-16

---

## Design Context

R6 V-03 and V-05 both reached 170/170 under v7 -- the current gold ceiling.
Their winning mechanisms:

- **C-22**: CHAIN-FLAG blocks progression (explicit halt in PHASE 3B specification)
- **C-23**: RULES-ANCHORED is a named gate ("Do not proceed to Phase 5 until all
  rules show ALIGNED")
- **C-24**: ENFORCEMENT MECHANISM section at position 1 (before PBI, before Handle
  Ledger, before any entries)

The three R6 criteria follow the same structural pattern:
- C-19 made the chain audit visible -> C-22 made CHAIN-FLAG a gate (not a token)
- C-20 made the distillation traceable -> C-23 made RULES-ANCHORED a gate (not a check)
- C-21 made the mechanism navigable -> C-24 made the section primary (not just findable)

R7 asks: what comes after primacy? Three unexplored axes remain:

1. **Phrasing register**: Phase specs currently mix imperative commands with
   explanatory rationale. Does imperative-only phrasing reduce interpretation
   variance and produce more consistent gate compliance?

2. **Lifecycle emphasis -- resolution protocol**: C-22 makes CHAIN-FLAG a gate.
   But the gate says "requires correction before proceeding" without specifying
   what a valid correction looks like. Does a named resolution protocol per flag
   type (exact repair steps, not just "fix it") convert the gate from
   stop-only to stop+repair?

3. **Inertia framing**: The no-echo cost (next team inherits all false assumptions
   in today's design materials) is implicit in the current prompts. Does naming it
   explicitly in the ENFORCEMENT MECHANISM section -- before the reviewer reads
   any entry -- produce stronger C-07 compliance and potentially reveal a new
   criterion about institutional purpose declaration?

**Candidate new criteria for R7:**

- **C-25 (candidate)**: CHAIN-FLAG gate includes a named resolution protocol
  specifying the exact repair action required per flag type. Without it,
  "correct the flagged element" is interpretable as any change -- including
  removing the flag without fixing the underlying inconsistency. With a named
  protocol, CHAIN-FLAG is reparable in only one valid way.

- **C-26 (candidate)**: RULES-ANCHORED gate emits a named closure token
  (RULES-ANCHORED-COMPLETE: all [N] rules ALIGNED) when all checks pass,
  making Phase 4B gate passage as positively auditable from output as Phase 3B
  (CHAIN-COMPLETE tokens). Without it, gate passage is inferred from absence
  of MISALIGNED entries rather than a positive terminal signal.

- **C-27 (candidate)**: Enforcement mechanism section includes an explicit
  inertia frame -- a named statement of what is lost if this artifact is not
  produced. C-24 makes the enforcement frame primary (first encountered); C-27
  makes that frame also declare the institutional cost of not producing the
  artifact. A reviewer who opens the artifact first reads both the enforcement
  mechanism and the no-echo cost.

**Variation axes selected:**

1. **Phrasing register** (V-01): All phase specifications converted to
   imperative-only short commands. Explanatory prose removed from phase blocks.
   ENFORCEMENT MECHANISM section retains full declaration text (structural,
   not procedural). All R6 V-03 mechanisms retained otherwise.

2. **Lifecycle emphasis** (V-02): PHASE 3B extended with a named RESOLUTION
   PROTOCOL specifying the exact repair action for each of the four chain
   elements. Repair must produce a visible RE-RUN result before CHAIN-COMPLETE
   can be emitted. All R6 V-03 mechanisms retained otherwise.

3. **Inertia framing** (V-03): ENFORCEMENT MECHANISM section expanded with an
   explicit NO-ECHO COST declaration before the provenance statement. Forward
   Statement (Phase 7) required to close the loop by naming the specific
   avoided failure. All R6 V-03 mechanisms retained otherwise.

**Predicted score map (v7, max 170):**

All five predicted at 170/170 under the current rubric -- all retain C-22, C-23,
C-24 mechanisms from R6 V-03. New criteria impact if v8 confirms C-25/C-27:

| Variant | C-25? | C-26? | C-27? | Asp (v7) | Composite (v7) |
|---------|-------|-------|-------|----------|----------------|
| V-01 | FAIL | FAIL | FAIL | 16/16 = 80 | 170 |
| V-02 | PASS | FAIL | FAIL | 16/16 = 80 | 170 |
| V-03 | FAIL | FAIL | PASS | 16/16 = 80 | 170 |
| V-04 | PASS | FAIL | PASS | 16/16 = 80 | 170 |
| V-05 | PASS | FAIL | PASS | 16/16 = 80 | 170 |

C-26 (RULES-ANCHORED-COMPLETE closure token) is not satisfied by any R7 variation.
It becomes the isolated target for R8.

---

## V-01 -- Single-axis: Phrasing register -- Imperative-only phase specifications

**Variation axis:** Phrasing register. Every phase specification is rewritten to
imperative-only commands (5-10 words per sentence). Explanatory prose is removed
from all phase blocks. The ENFORCEMENT MECHANISM section retains its full text
(structural declaration, not procedural instruction). All gate specifications from
R6 V-03 are preserved: ENFORCEMENT MECHANISM at position 1, PHASE 3B CHAIN-FLAG
hard gate, PHASE 4B RULES-ANCHORED named gate.

**Hypothesis:** Current phase specs mix commands with rationale. "This audit is
structurally distinct from the ENTRY GATE: gate checks register quality; audit
checks chain consistency" mixes instruction with explanation. A reviewer must
decide which parts are binding. Imperative-only removes that choice: "Run CHAIN
INTEGRITY AUDIT after all gates CLEARED. Check chain consistency only. Do not
repeat register checks." If rationale is irrelevant to execution, V-01 scores
identically to R6 V-03. If some explanatory prose is load-bearing for C-18/C-19
(the distinction between attestation and audit is conveyed via explanation), V-01
will degrade those criteria -- revealing which prose is actually instructional
and which is contextual.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== ENFORCEMENT MECHANISM =======================================================

This artifact uses STRUCTURAL PROVENANCE for its Pre-committed Belief Inventory.

Tier: STRUCTURAL (not temporal).

Distinguishing property: the PBI-writing role operates under role-scope exclusion
and cannot access signal artifacts regardless of instruction. Temporal provenance
sequences phases (PBI written before signals read) but does not prevent cross-phase
reasoning -- a model with access to both phases can reason across them even if
instructed not to. Structural provenance removes that access at role-scope level:
the PBI role has no signal-read permission. The boundary is architectural, not
behavioral.

Reviewer implication: independence is enforced, not instructed. C-13 content
analysis (PBI belief language vs Handle Ledger finding language) is confirmatory
rather than probative -- it verifies that enforced independence produced independent
content; it cannot by itself prove independence was maintained.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Write before reading any signal artifacts.
Write one entry per assumption the design materials imply.
Use belief language only. No signal knowledge permitted.

Format:
  PB-[NN]:   [Belief statement: "Today's materials imply that X will behave as Y."]

Freeze the PBI before PHASE 1.
PBI entries must not use handle labels.
PBI entries use belief language; Handle Ledger entries use finding language.

== HANDLE LEDGER ===============================================================

Read all signal artifacts first.
Write one Handle Ledger entry per surprise before drafting entries.

Format:
  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language only.]

Confirm independence: no PBI entry names its handle label.
No HL entry echoes a PBI entry verbatim.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [HL-[NN] label. Encode the correction: "The Cascade Inversion"
                   not "Unexpected Cascade Behavior".]

  PBI-Ref:         [PB-[NN]. The prior belief this entry corrects.]

  Source:          [namespace:skill:artifact. No attribution prose.]

  What today's materials imply:
                   ["Today's materials imply that..." or "A new team reading the
                   current spec would assume..."
                   Degree variants fail. Generic-material-critique fails.]

  What the signals showed instead:
                   [Direct claim only. No hedges. Prohibited: "may suggest" /
                   "appears to indicate" / "seems like" / "could mean" /
                   "might be" / "it is possible that".]

  What the next team would build wrong:
                   [Specific component, flow, or decision. Prohibited: "worth noting"
                   / "bears watching" / "important to keep in mind".]

  What the next team must decide before proceeding:
                   [Specific blocking question or action. No deferrals.]

  Verified:        [Quote actual text of PB-[NN]. Quote key sentence from source
                   artifact. Not identifiers -- actual text of both.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Apply before drafting each entry:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"
  YES -> draft the entry.
  NO  -> excluded.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 -- Correction framing:
  Write every entry for the next team. Prohibit "We found that X".
  Rewrite to "Today's materials imply X". No "we" in "What today's materials imply".

Rule 2 -- Claim-only voice:
  Direct claims only. No hedges. Prohibited constructs apply to every field.

Rule 3 -- Entry completeness:
  Each entry is self-contained. Name assumption, correction, wrong design, and
  blocking decision. Define domain terms within the entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Name both source artifacts.
Emit the convergence gap:
  "Neither [A] nor [B] alone revealed this -- their intersection showed that
   today's materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Draft all entries. Order HIGH -> MEDIUM -> LOW. Do not write synthesis sections.

== PHASE 2: REGISTER AUDIT ====================================================

Run field by field for every entry. Rewrite every discovery-register field.

  Source:
    FAIL: prose attribution. FIX: namespace:skill:artifact.

  What today's materials imply:
    FAIL: "We found X" / "The team expected X". FIX: "Today's materials imply..."
    FAIL: "Materials tend to underspecify X". FIX: specific implied claim.

  What the next team would build wrong:
    FAIL: "Worth noting" / "Bears watching". FIX: specific wrong design.

  What the next team must decide:
    FAIL: deferrals. FIX: specific blocking decision.

  Verified:
    FAIL: identifiers only. FIX: verbatim text of PB-[NN] and source sentence.

Complete when every non-Name field is in correction register.

== PHASE 3: ENTRY GATE ========================================================

Run for every entry. Gate blocks appear in the artifact.

  GATE: [entry Name]
    PBI-Ref          [PASS / FAIL: {problem} -- rewrite required]
    Source           [PASS / FAIL: {problem} -- rewrite required]
    Materials imply  [PASS / FAIL: narration or generic critique -- rewrite]
    Signals showed   [PASS / FAIL: {hedge construct} -- rewrite required]
    Wrong design     [PASS / FAIL: softener -- rewrite]
    Next decision    [PASS / FAIL: deferral -- rewrite]
    Verified         [PASS / FAIL: identifier-only -- quote actual text]
  STATUS: CLEARED / NOT CLEARED

Rewrite all FAIL fields. Re-run. Repeat until CLEARED.
Block Phase 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ============================================

Run after all gates CLEARED. Check chain consistency only.
Do not repeat register checks.

For each entry:

  CHAIN: [entry Name]
    [1] PBI-Ref: does PB-[NN] describe the belief in "What today's materials
        imply"? Quote PBI entry text to confirm.
    [2] Handle: does entry Name match HL-[NN] in Handle Ledger exactly?
    [3] Source: does Source artifact exist in $ARGUMENTS signal set?
    [4] Verified quotation: is the Verified text verbatim from cited sources?
        Not paraphrase -- actual text.

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

Any CHAIN-FLAG blocks further production.
Block Phase 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale.
Name the design decision at risk for each entry. Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ===================================================

Produce RULES OF THUMB table. HIGH and MEDIUM only. Exclude LOW.

| Rule | Tier | Entry | Statement (<=20 words) |
|------|------|-------|------------------------|
| R-01 | [HIGH] | [entry Name] | [statement] |
| R-02 | [MEDIUM] | [entry Name] | [statement] |

Rules citable without context:
  PASS: "Do not allocate X until Y confirms ownership -- callee owns X, not caller."
  FAIL: "Ownership assumptions need re-examination."

Run RULES-ANCHORED after the table:

  RULES-ANCHORED:
    R-01: tier [HIGH] confirmed against [Name] Severity: [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against [Name] Severity: [MEDIUM] -- ALIGNED
    [MISALIGNED: correct tier annotation before proceeding]

Block Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write "Pattern of inherited errors" section. 2-4 sentences.
Name any structural origin shared by two or more corrections.
If none: state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write "Blind Spot Map" section.
A blind spot is a type of wrong thinking, not a topic area.

STEP 1: Name blind spot categories.
  PASS: "Sequence inversion -- materials assumed X precedes Y; signals showed Y
         precedes X, invalidating the commit ordering assumption"
  FAIL: "State management" -- domain label, not type of wrong thinking.
  Labels transferable to a different topic without rewriting fail.

STEP 2: Assign each correction to exactly one category.
  Unclassified entries: one-sentence explanation required.

STEP 3: Write "What the blind spot map reveals" -- 2-3 sentences.
  NON-DERIVABILITY CONSTRAINT: state something not visible from reading individual
  corrections or tallying category assignments.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team.
Register: "Before you build {topic}, the correction record requires you to know..."
Specific to these corrections. No generic advice.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.
Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (headed section -- navigable from headers, position 1)
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- ordered HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE)
  7. Surprise hierarchy (ranked with rationale)
  8. Rules of Thumb (table + RULES-ANCHORED)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction forward statement
  12. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-02 -- Single-axis: Lifecycle emphasis -- CHAIN-FLAG resolution protocol

**Variation axis:** Lifecycle emphasis. PHASE 3B is extended with a named
RESOLUTION PROTOCOL. When any entry receives CHAIN-FLAG, the protocol specifies
the exact repair action required per flag type -- one of four named procedures
(PBI-Ref repair, Handle repair, Source repair, Verified-quotation repair). After
repair, the CHAIN: block for that entry is re-run. The re-run must produce a
visible CHAIN-COMPLETE token before Phase 4 may proceed. All other mechanisms
from R6 V-03 are retained unchanged.

**Hypothesis:** C-22 makes CHAIN-FLAG a hard gate. The current specification
says "CHAIN-FLAG requires correction before proceeding" but does not define
what a valid correction looks like. An AI reviewer encountering CHAIN-FLAG on
element [4] (Verified quotation inaccurate) might satisfy the gate by rewriting
the Verified field with a slightly closer paraphrase rather than quoting verbatim.
The gate is satisfied (CHAIN-COMPLETE emitted) but the evidentiary chain is not
repaired. A named resolution protocol removes this gap: "element [4] flag:
open source artifact, locate sentence, copy verbatim." With the protocol,
CHAIN-FLAG is reparable in only one valid way. This may surface C-25: CHAIN-FLAG
gate includes a named resolution protocol specifying the required repair per flag
type.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== ENFORCEMENT MECHANISM =======================================================

This artifact uses STRUCTURAL PROVENANCE for its Pre-committed Belief Inventory.

Tier: STRUCTURAL (not temporal).

Distinguishing property: the PBI-writing role operates under role-scope exclusion
and cannot access signal artifacts regardless of instruction. Temporal provenance
sequences phases (PBI written before signals read) but does not prevent cross-phase
reasoning -- a model with access to both phases can reason across them even if
instructed not to. Structural provenance removes that access at role-scope level:
the PBI role has no signal-read permission. The boundary is architectural, not
behavioral.

Reviewer implication: independence is enforced, not instructed. C-13 content
analysis (PBI belief language vs Handle Ledger finding language) is confirmatory
rather than probative.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries. PBI entries use belief language; Handle Ledger
entries use finding language.

== HANDLE LEDGER ===============================================================

After reading signals, produce a Handle Ledger before writing entries. Each entry:

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief
              language. Must not echo the corresponding PBI entry verbatim.]

Independence test: no PBI entry names its handle label; no HL entry echoes a PBI
entry verbatim.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [Cite the Handle Ledger entry: HL-[NN] label. Encode the
                   correction: "The Cascade Inversion" not "Unexpected Cascade
                   Behavior".]

  PBI-Ref:         [Identifier: PB-[NN]. Points to the prior belief corrected.]

  Source:          [namespace:skill:artifact. No attribution prose.]

  What today's materials imply:
                   [Future-team framing: "Today's materials imply that..." or
                   "A new team reading the current spec would assume..."
                   Degree variants fail. Generic-material-critique fails.]

  What the signals showed instead:
                   [Direct claim. Prohibited: "may suggest" / "appears to indicate"
                   / "seems like" / "could mean" / "might be" / "it is possible
                   that".]

  What the next team would build wrong:
                   [Specific component, flow, or decision. Prohibited: "worth noting"
                   / "bears watching" / "important to keep in mind".]

  What the next team must decide before proceeding:
                   [Specific blocking question or action. Not deferrals.]

  Verified:        [Quote actual text of PB-[NN] and key sentence from source
                   artifact. Not identifiers only -- actual text of both.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES -> draft the entry.
  NO  -> excluded. Absorbed findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 -- Correction framing:
  Every entry written for the next team. "We found that X" is prohibited. Rewrite
  to "Today's materials imply X". No "we" in "What today's materials imply".

Rule 2 -- Claim-only voice:
  Direct claims. No hedges. Prohibited constructs apply to every field.

Rule 3 -- Entry completeness:
  Each entry self-contained: assumption, correction, wrong design, decision.
  Define domain terms within the entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this -- their intersection showed that
   today's materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries. Order HIGH -> MEDIUM -> LOW by Severity.
Do not write synthesis sections yet.

== PHASE 2: REGISTER AUDIT ====================================================

Apply paired transformations field by field. Rewrite any discovery-register field.

  Source field:
    DISCOVERY: "signals indicated X" / "research showed X" / "analysis revealed X"
    CORRECTION: namespace:skill:artifact -> Prose attribution fails.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X" / "We assumed X"
    CORRECTION: "Today's materials imply that..." -> Original-team narration fails.

    DISCOVERY: "Materials tend to underspecify X" / "Specs rarely address Y"
    CORRECTION: "Today's spec implies X will behave as [specific claim]"
    -> Generic-category critique fails.

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching" / "Important to keep in mind"
    CORRECTION: "[Component/flow/decision] would be built as [wrong design]"
    -> Severity statements fail.

  What the next team must decide:
    DISCOVERY: "Further investigation needed" / "Monitor this"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"
    -> Deferrals fail.

  Verified field:
    DISCOVERY: "PB-02 confirmed" / "source confirmed" (identifier only)
    CORRECTION: "[Actual quoted text of PB-02] / [Actual sentence from source]"
    -> Identifier-only fails.

Register audit complete when every non-Name field is in correction register.

== PHASE 3: ENTRY GATE ========================================================

Run ENTRY GATE after register audit. Gate blocks appear in the artifact.

For each entry:

  GATE: [entry Name]
    PBI-Ref          [PASS: identifier confirmed in PBI section]
                     [FAIL: {problem} -- rewrite required]
    Source           [PASS: namespace:skill:artifact confirmed]
                     [FAIL: {problem} -- rewrite required]
    Materials imply  [PASS: future-team framing confirmed]
                     [FAIL: narration or generic critique -- rewrite]
    Signals showed   [PASS: direct claim, no hedges]
                     [FAIL: {hedge construct} -- rewrite required]
    Wrong design     [PASS: specific component/flow/decision named]
                     [FAIL: softener -- rewrite]
    Next decision    [PASS: specific blocking decision or question confirmed]
                     [FAIL: deferral -- rewrite]
    Verified         [PASS: actual text quoted for both PBI entry and source]
                     [FAIL: identifier-only -- quote actual text]
  STATUS: CLEARED / NOT CLEARED

STATUS NOT CLEARED: rewrite FAIL fields. Re-run. Repeat until CLEARED.
Do not proceed to Phase 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ============================================

After all gates CLEARED, run the CHAIN INTEGRITY AUDIT.

Distinct from ENTRY GATE: gate checks register quality (format and framing);
audit checks chain consistency (do cited identifiers point to the right content).
Each check is independent -- do not use gate results as chain evidence.

For each entry, independently re-verify all four chain elements:

  CHAIN: [entry Name]
    [1] PBI-Ref: does PB-[NN] describe the belief in "What today's materials
        imply"? Quote the PBI entry text to confirm.
    [2] Handle: does entry Name match HL-[NN] in the Handle Ledger exactly?
        Confirm HL-[NN] title and entry Name are the same label.
    [3] Source: does the Source artifact exist in the signal set for $ARGUMENTS?
        Confirm namespace, skill, and artifact name are resolvable.
    [4] Verified quotation: does the Verified field quote text that accurately
        represents the PBI entry and source finding at the cited identifiers?
        Must be verbatim, not a paraphrase.

  Emit one token per entry:
    CHAIN-COMPLETE: [entry Name] -- all four elements verified
    CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

Any CHAIN-FLAG blocks further production. Before re-running the CHAIN: block for
a flagged entry, apply the RESOLUTION PROTOCOL for the flagged element:

== RESOLUTION PROTOCOL =========================================================

CHAIN-FLAG on element [1] PBI-Ref -- belief does not match "What today's
materials imply":
  Step 1: Re-read the PBI section. Locate PB-[NN] at the identifier named in
          PBI-Ref.
  Step 2: Copy the PBI belief statement verbatim into the Verified field (PBI half).
  Step 3: Compare the PBI belief statement to "What today's materials imply."
          If they match: proceed to re-run.
          If they do not match: update PBI-Ref to the correct identifier, then
          repeat Steps 1-2 with the corrected identifier.
  Step 4: Re-run the CHAIN: block for this entry. Do not proceed until
          CHAIN-COMPLETE.

CHAIN-FLAG on element [2] Handle -- entry Name does not match HL-[NN]:
  Step 1: Re-read the Handle Ledger. Locate the HL entry whose label corresponds
          to this surprise.
  Step 2: Copy the HL-[NN] title character-for-character into entry Name.
  Step 3: If no HL entry exists for this surprise: add the correct HL-[NN]
          entry to the Handle Ledger before proceeding.
  Step 4: Re-run the CHAIN: block for this entry. Do not proceed until
          CHAIN-COMPLETE.

CHAIN-FLAG on element [3] Source -- artifact not resolvable in signal set:
  Step 1: Re-read the signal artifact list for $ARGUMENTS.
  Step 2: Locate the artifact by namespace, skill, and filename.
  Step 3: Update Source to the exact path: namespace:skill:artifact.
  Step 4: If the artifact cannot be located in the signal set for $ARGUMENTS:
          exclude this entry. An entry without a traceable source cannot be
          audited by the next team and fails the still-live test.
  Step 5: Re-run the CHAIN: block for this entry. Do not proceed until
          CHAIN-COMPLETE.

CHAIN-FLAG on element [4] Verified quotation -- text is paraphrase or does not
correspond to cited identifiers:
  Step 1: Re-open the source artifact at the path named in Source.
  Step 2: Locate the sentence that most directly contradicts the prior belief
          named in PBI-Ref.
  Step 3: Copy that sentence verbatim. Replace the source-half of the Verified
          field with the verbatim text.
  Step 4: Re-read PB-[NN] at the identifier named in PBI-Ref.
  Step 5: Copy the PBI belief statement verbatim. Replace the PBI-half of the
          Verified field with the verbatim text.
  Step 6: Re-run the CHAIN: block for this entry. Do not proceed until
          CHAIN-COMPLETE.

Do not proceed to Phase 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale:

  1. [entry Name] -- [why this has highest design impact: names the design decision
     at risk and what must be redesigned before other work can proceed]
  2. [entry Name] -- [rationale at the same standard]
  ...

Assertion without argument fails. "This is most critical" without naming what
becomes uncorrectable if missed fails.

== PHASE 4B: RULES OF THUMB ===================================================

After the hierarchy, write the RULES OF THUMB table. HIGH and MEDIUM entries only.
LOW entries excluded.

| Rule | Tier | Entry | Statement (<=20 words) |
|------|------|-------|------------------------|
| R-01 | [HIGH] | [entry Name] | [statement] |
| R-02 | [MEDIUM] | [entry Name] | [statement] |

Rules must be citable without context:
  PASS: "Do not allocate X until Y confirms ownership -- callee owns X, not caller."
  FAIL: "Ownership assumptions need re-examination."

After the table, run RULES-ANCHORED:

  RULES-ANCHORED:
    R-01: tier [HIGH] confirmed against entry [Name] Severity: [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against entry [Name] Severity: [MEDIUM] -- ALIGNED
    [MISALIGNED: correct tier annotation before proceeding]

Do not proceed to Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write one section: "Pattern of inherited errors."

Two or more corrections sharing a structural origin? Write 2-4 sentences. Name any
pattern; if none, state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem -- a type of wrong thinking, not a topic area.

STEP 1 -- NAME THE BLIND SPOT CATEGORIES.

  PASS: "Ownership inversion -- materials assumed the caller owns X; signals showed
         the callee owns X, reversing the allocation model"
  FAIL: "State management" -- domain label, not type of wrong thinking.

A category label transferable to a different topic without rewriting fails.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: state something not visible from
reading individual corrections or tallying category assignments.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. Register: "Before you build {topic}, the
correction record requires you to know that..." Specific to these corrections.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts. Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (headed section -- navigable from headers, position 1)
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- ordered HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE; entries that required Resolution
     Protocol show RE-RUN: CHAIN-COMPLETE after repair)
  7. Surprise hierarchy (ranked with rationale)
  8. Rules of Thumb (table + RULES-ANCHORED)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction forward statement
  12. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-03 -- Single-axis: Inertia framing -- No-echo cost declared in ENFORCEMENT MECHANISM

**Variation axis:** Inertia framing. The ENFORCEMENT MECHANISM section is expanded
to open with an explicit NO-ECHO COST declaration before the provenance statement.
The declaration names the inertia competitor: proceeding without a topic:echo
leaves every false assumption in today's design materials as inherited knowledge
for the next team. Phase 7 (Forward Statement) is required to close the loop --
it must name the specific assumption the next team would have inherited without
this artifact, converting the no-echo cost from a general warning into a specific
avoided failure. All other mechanisms from R6 V-03 are retained unchanged.

**Hypothesis:** C-07 (institutional framing) requires the artifact to be explicitly
addressed to a future team. Current artifacts satisfy C-07 via "What the next team
would build wrong" fields and the Forward Statement. But they do not name the
scenario they prevent. Naming the no-echo cost in the first section the reviewer
encounters frames every subsequent entry as a prevented failure rather than a
documented surprise. This may produce stronger C-07 compliance -- and may reveal
C-27: the enforcement mechanism section declares what is lost if this artifact is
not produced. C-24 (head position) ensures the reviewer reads both the provenance
claim and the no-echo cost before any entry is encountered.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== ENFORCEMENT MECHANISM =======================================================

NO-ECHO COST:

Without this artifact, the next team inherits every false assumption embedded in
today's design materials. Signal gathering transforms those assumptions into
discoveries -- but without a topic:echo, discoveries remain owned by the current
team and never reach the next. The next team re-encounters the same assumptions,
runs the same signals, and arrives at the same corrections. The echo is the only
mechanism by which signal-generated knowledge outlives the team that gathered it.

This artifact's institutional function: prevent the next team from carrying
assumptions that today's signals have already disproved.

ENFORCEMENT MECHANISM -- STRUCTURAL PROVENANCE:

This artifact uses STRUCTURAL PROVENANCE for its Pre-committed Belief Inventory.

Tier: STRUCTURAL (not temporal).

Distinguishing property: the PBI-writing role operates under role-scope exclusion
and cannot access signal artifacts regardless of instruction. Temporal provenance
sequences phases (PBI written before signals read) but does not prevent cross-phase
reasoning -- a model with access to both phases can reason across them even if
instructed not to. Structural provenance removes that access at role-scope level:
the PBI role has no signal-read permission. The boundary is architectural, not
behavioral.

Reviewer implication: independence is enforced, not instructed. C-13 content
analysis (PBI belief language vs Handle Ledger finding language) is confirmatory
rather than probative.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries. PBI entries use belief language; Handle Ledger
entries use finding language.

== HANDLE LEDGER ===============================================================

After reading signals, produce a Handle Ledger before writing entries. Each entry:

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief
              language. Must not echo the corresponding PBI entry verbatim.]

Independence test: no PBI entry names its handle label; no HL entry echoes a PBI
entry verbatim.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [Cite the Handle Ledger entry: HL-[NN] label. Encode the
                   correction: "The Cascade Inversion" not "Unexpected Cascade
                   Behavior".]

  PBI-Ref:         [Identifier: PB-[NN]. Points to the prior belief corrected.]

  Source:          [namespace:skill:artifact. No attribution prose.]

  What today's materials imply:
                   [Future-team framing: "Today's materials imply that..." or
                   "A new team reading the current spec would assume..."
                   Degree variants fail. Generic-material-critique fails.]

  What the signals showed instead:
                   [Direct claim. Prohibited: "may suggest" / "appears to indicate"
                   / "seems like" / "could mean" / "might be" / "it is possible
                   that".]

  What the next team would build wrong:
                   [Specific component, flow, or decision. Prohibited: "worth noting"
                   / "bears watching" / "important to keep in mind".]

  What the next team must decide before proceeding:
                   [Specific blocking question or action. Not deferrals.]

  Verified:        [Quote actual text of PB-[NN] and key sentence from source
                   artifact. Not identifiers only -- actual text of both.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES -> draft the entry. It prevents one instance of the no-echo cost.
  NO  -> excluded. Absorbed findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 -- Correction framing:
  Every entry written for the next team. "We found that X" is prohibited. Rewrite
  to "Today's materials imply X". No "we" in "What today's materials imply".

Rule 2 -- Claim-only voice:
  Direct claims. No hedges. Prohibited constructs apply to every field.

Rule 3 -- Entry completeness:
  Each entry self-contained: assumption, correction, wrong design, decision.
  Define domain terms within the entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this -- their intersection showed that
   today's materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries. Order HIGH -> MEDIUM -> LOW by Severity.
Do not write synthesis sections yet.

== PHASE 2: REGISTER AUDIT ====================================================

Apply paired transformations field by field. Rewrite any discovery-register field.

  Source field:
    DISCOVERY: "signals indicated X" / "research showed X" / "analysis revealed X"
    CORRECTION: namespace:skill:artifact -> Prose attribution fails.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X" / "We assumed X"
    CORRECTION: "Today's materials imply that..." -> Original-team narration fails.

    DISCOVERY: "Materials tend to underspecify X" / "Specs rarely address Y"
    CORRECTION: "Today's spec implies X will behave as [specific claim]"
    -> Generic-category critique fails.

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching" / "Important to keep in mind"
    CORRECTION: "[Component/flow/decision] would be built as [wrong design]"
    -> Severity statements fail.

  What the next team must decide:
    DISCOVERY: "Further investigation needed" / "Monitor this"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"
    -> Deferrals fail.

  Verified field:
    DISCOVERY: "PB-02 confirmed" (identifier only)
    CORRECTION: "[Actual quoted text of PB-02] / [Actual sentence from source]"
    -> Identifier-only fails.

Register audit complete when every non-Name field is in correction register.

== PHASE 3: ENTRY GATE ========================================================

Run ENTRY GATE after register audit. Declarations appear in the artifact.

For each entry:

  GATE: [entry Name]
    PBI-Ref          [PASS: identifier confirmed in PBI section]
                     [FAIL: {problem} -- rewrite required]
    Source           [PASS: namespace:skill:artifact confirmed]
                     [FAIL: {problem} -- rewrite required]
    Materials imply  [PASS: future-team framing confirmed]
                     [FAIL: narration or generic critique -- rewrite]
    Signals showed   [PASS: direct claim, no hedges]
                     [FAIL: {hedge construct} -- rewrite required]
    Wrong design     [PASS: specific component/flow/decision named]
                     [FAIL: softener -- rewrite]
    Next decision    [PASS: specific blocking decision or question confirmed]
                     [FAIL: deferral -- rewrite]
    Verified         [PASS: actual text quoted for both PBI entry and source]
                     [FAIL: identifier-only -- quote actual text]
  STATUS: CLEARED / NOT CLEARED

STATUS NOT CLEARED: rewrite FAIL fields. Re-run. Repeat until CLEARED.
Do not proceed to Phase 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ============================================

After all gates CLEARED, run the CHAIN INTEGRITY AUDIT.

Distinct from ENTRY GATE: gate checks register quality; audit checks chain
consistency.

For each entry, independently re-verify all four chain elements:

  CHAIN: [entry Name]
    [1] PBI-Ref: does PB-[NN] describe the belief in "What today's materials
        imply"? Quote the PBI entry text to confirm.
    [2] Handle: does entry Name match HL-[NN] in the Handle Ledger?
    [3] Source: does the Source artifact exist in the signal set for $ARGUMENTS?
    [4] Verified quotation: does the Verified field quote text accurately
        representing the cited PBI entry and source finding? Not a paraphrase.

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

Any CHAIN-FLAG blocks further production.
Do not proceed to Phase 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale:

  1. [entry Name] -- [why: names the design decision at risk]
  2. [entry Name] -- [rationale at the same standard]
  ...

Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ===================================================

After the hierarchy, write the RULES OF THUMB table. HIGH and MEDIUM entries only.
LOW entries excluded.

| Rule | Tier | Entry | Statement (<=20 words) |
|------|------|-------|------------------------|
| R-01 | [HIGH] | [entry Name] | [statement] |
| R-02 | [MEDIUM] | [entry Name] | [statement] |

Rules citable without context:
  PASS: "Do not allocate X until Y confirms ownership -- callee owns X, not caller."
  FAIL: "Ownership assumptions need re-examination."

After the table, run RULES-ANCHORED:

  RULES-ANCHORED:
    R-01: tier [HIGH] confirmed against entry [Name] Severity: [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against entry [Name] Severity: [MEDIUM] -- ALIGNED
    [MISALIGNED: correct tier annotation before proceeding]

Do not proceed to Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write one section: "Pattern of inherited errors."

Two or more corrections sharing a structural origin? Write 2-4 sentences. Name any
pattern; if none, state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem -- a type of wrong thinking, not a topic area.

STEP 1 -- NAME THE BLIND SPOT CATEGORIES.

  PASS: "Ownership inversion -- materials assumed the caller owns X; signals showed
         the callee owns X, reversing the allocation model"
  FAIL: "State management" -- domain label, not type of wrong thinking.

A category label transferable to a different topic without rewriting fails.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: state something not visible from
reading individual corrections or tallying category assignments.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. Register: "Before you build {topic}, the
correction record requires you to know that..."

The Forward Statement must close the loop with the NO-ECHO COST declared in the
ENFORCEMENT MECHANISM section. Name the single assumption the next team would have
inherited without this artifact that would have caused the greatest design error.
This converts the no-echo cost from a general warning into a specific avoided
failure: the statement that completes the institutional purpose declaration.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts. Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (position 1: no-echo cost + structural provenance)
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- ordered HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE)
  7. Surprise hierarchy (ranked with rationale)
  8. Rules of Thumb (table + RULES-ANCHORED)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction forward statement (closes the loop with no-echo cost)
  12. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-04 -- Combined: Lifecycle emphasis + Inertia framing (V-02 + V-03)

**Axes combined:** V-02's CHAIN-FLAG resolution protocol + V-03's no-echo cost
framing in ENFORCEMENT MECHANISM and Forward Statement. Tests whether the two
mechanisms interact. Specifically: does naming the no-echo cost change how a
reviewer applies the resolution protocol? The protocol's Step 4 for element [3]
(Source not found: exclude the entry) is grounded in the no-echo cost: "An entry
without a traceable source is not a prevented failure -- it is an unsubstantiated
claim." In V-02, this reasoning must be inferred; in V-04, it is stated in the
ENFORCEMENT MECHANISM section the reviewer read first. If framing the institutional
purpose before the gate specifications produces more diligent protocol compliance
(reviewers are more motivated to complete repairs because they understand what is
lost if an entry is excluded), V-04 would show higher entry-completion rates than
V-02 alone.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== ENFORCEMENT MECHANISM =======================================================

NO-ECHO COST:

Without this artifact, the next team inherits every false assumption embedded in
today's design materials. Signal gathering transforms those assumptions into
discoveries -- but without a topic:echo, discoveries remain owned by the current
team and never reach the next. The next team re-encounters the same assumptions,
runs the same signals, and arrives at the same corrections. The echo is the only
mechanism by which signal-generated knowledge outlives the team that gathered it.

This artifact's institutional function: prevent the next team from carrying
assumptions that today's signals have already disproved.

ENFORCEMENT MECHANISM -- STRUCTURAL PROVENANCE:

This artifact uses STRUCTURAL PROVENANCE for its Pre-committed Belief Inventory.

Tier: STRUCTURAL (not temporal).

Distinguishing property: the PBI-writing role operates under role-scope exclusion
and cannot access signal artifacts regardless of instruction. Temporal provenance
sequences phases but does not prevent cross-phase reasoning. Structural provenance
removes access at role-scope level: the PBI role has no signal-read permission.
The boundary is architectural, not behavioral.

Reviewer implication: independence is enforced, not instructed. C-13 content
analysis is confirmatory rather than probative.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels. PBI entries
use belief language; Handle Ledger entries use finding language.

== HANDLE LEDGER ===============================================================

After reading signals, produce a Handle Ledger before writing entries. Each entry:

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief
              language. Must not echo the corresponding PBI entry verbatim.]

Independence test: no PBI entry names its handle label; no HL entry echoes a PBI
entry verbatim.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [HL-[NN] label. Encode the correction: "The Cascade Inversion"
                   not "Unexpected Cascade Behavior".]

  PBI-Ref:         [PB-[NN]. The prior belief this entry corrects.]

  Source:          [namespace:skill:artifact. No attribution prose.]

  What today's materials imply:
                   ["Today's materials imply that..." or "A new team would assume..."
                   Degree variants fail. Generic-material-critique fails.]

  What the signals showed instead:
                   [Direct claim. Prohibited: "may suggest" / "appears to indicate"
                   / "seems like" / "could mean" / "might be" / "it is possible that".]

  What the next team would build wrong:
                   [Specific component, flow, or decision. Prohibited: "worth noting"
                   / "bears watching" / "important to keep in mind".]

  What the next team must decide before proceeding:
                   [Specific blocking question or action. Not deferrals.]

  Verified:        [Quote actual text of PB-[NN] and key sentence from source
                   artifact. Not identifiers only -- actual text of both.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES -> draft the entry. It prevents one instance of the no-echo cost.
  NO  -> excluded.

== CORRECTION ENFORCEMENT ======================================================

Rule 1: Every entry written for the next team. "We found that X" prohibited.
  Rewrite to "Today's materials imply X". No "we" in "What today's materials imply".

Rule 2: Direct claims. No hedges. Prohibited constructs apply to every field.

Rule 3: Each entry self-contained. Define domain terms within the entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this -- their intersection showed that
   today's materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries. Order HIGH -> MEDIUM -> LOW by Severity.
Do not write synthesis sections yet.

== PHASE 2: REGISTER AUDIT ====================================================

Apply paired transformations field by field. Rewrite any discovery-register field.

  Source:
    DISCOVERY: "signals indicated X" / "research showed X"
    CORRECTION: namespace:skill:artifact -> Prose attribution fails.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X"
    CORRECTION: "Today's materials imply that..."
    DISCOVERY: "Materials tend to underspecify X"
    CORRECTION: "Today's spec implies X will behave as [specific claim]"

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching"
    CORRECTION: "[Component/flow/decision] would be built as [wrong design]"

  What the next team must decide:
    DISCOVERY: "Further investigation needed" / "Monitor this"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"

  Verified:
    DISCOVERY: "PB-02 confirmed" (identifier only)
    CORRECTION: "[Actual quoted text of PB-02] / [Actual sentence from source]"

Register audit complete when every non-Name field is in correction register.

== PHASE 3: ENTRY GATE ========================================================

Run ENTRY GATE after register audit. Declarations appear in the artifact.

For each entry:

  GATE: [entry Name]
    PBI-Ref          [PASS: identifier confirmed] [FAIL: {problem} -- rewrite]
    Source           [PASS: namespace:skill:artifact] [FAIL: {problem} -- rewrite]
    Materials imply  [PASS: future-team framing] [FAIL: narration -- rewrite]
    Signals showed   [PASS: direct claim] [FAIL: {hedge} -- rewrite]
    Wrong design     [PASS: specific named] [FAIL: softener -- rewrite]
    Next decision    [PASS: specific blocking] [FAIL: deferral -- rewrite]
    Verified         [PASS: actual text quoted] [FAIL: identifier-only -- quote]
  STATUS: CLEARED / NOT CLEARED

Rewrite all FAIL fields. Re-run. Repeat until CLEARED.
Do not proceed to Phase 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ============================================

After all gates CLEARED, run the CHAIN INTEGRITY AUDIT.

Distinct from ENTRY GATE: gate checks register quality; audit checks chain
consistency. Each check is independent.

For each entry, independently re-verify all four chain elements:

  CHAIN: [entry Name]
    [1] PBI-Ref: does PB-[NN] describe the belief in "What today's materials
        imply"? Quote the PBI entry text to confirm.
    [2] Handle: does entry Name match HL-[NN] in the Handle Ledger exactly?
    [3] Source: does the Source artifact exist in the signal set for $ARGUMENTS?
    [4] Verified quotation: does the Verified field quote text that accurately
        represents the cited PBI entry and source finding? Must be verbatim.

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

Any CHAIN-FLAG blocks further production. Apply the RESOLUTION PROTOCOL before
re-running the CHAIN: block for any flagged entry:

== RESOLUTION PROTOCOL =========================================================

CHAIN-FLAG on element [1] PBI-Ref:
  Step 1: Re-read PBI section. Locate PB-[NN] at identifier named in PBI-Ref.
  Step 2: Copy belief statement verbatim into Verified field (PBI half).
  Step 3: Compare belief statement to "What today's materials imply."
          Match: proceed to re-run.
          No match: update PBI-Ref to correct identifier, repeat Steps 1-2.
  Step 4: Re-run CHAIN: block. Do not proceed until CHAIN-COMPLETE.

CHAIN-FLAG on element [2] Handle:
  Step 1: Re-read Handle Ledger. Locate HL entry for this surprise.
  Step 2: Copy HL-[NN] title character-for-character into entry Name.
  Step 3: If no HL entry exists: add it to Handle Ledger before proceeding.
  Step 4: Re-run CHAIN: block. Do not proceed until CHAIN-COMPLETE.

CHAIN-FLAG on element [3] Source:
  Step 1: Re-read signal artifact list for $ARGUMENTS.
  Step 2: Locate artifact by namespace, skill, filename.
  Step 3: Update Source to exact path: namespace:skill:artifact.
  Step 4: If artifact not in signal set: exclude this entry. An entry without
          a traceable source is not a prevented failure -- it is an
          unsubstantiated claim. The no-echo cost requires entries to be
          verifiable by the next team.
  Step 5: Re-run CHAIN: block. Do not proceed until CHAIN-COMPLETE.

CHAIN-FLAG on element [4] Verified quotation:
  Step 1: Re-open source artifact at path named in Source.
  Step 2: Locate sentence most directly contradicting the PBI belief.
  Step 3: Copy that sentence verbatim. Replace source-half of Verified field.
  Step 4: Re-read PB-[NN] at identifier named in PBI-Ref.
  Step 5: Copy belief statement verbatim. Replace PBI-half of Verified field.
  Step 6: Re-run CHAIN: block. Do not proceed until CHAIN-COMPLETE.

Do not proceed to Phase 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale:

  1. [entry Name] -- [why: names the design decision at risk]
  2. [entry Name] -- [rationale at the same standard]
  ...

Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ===================================================

After the hierarchy, write the RULES OF THUMB table. HIGH and MEDIUM only.

| Rule | Tier | Entry | Statement (<=20 words) |
|------|------|-------|------------------------|
| R-01 | [HIGH] | [entry Name] | [statement] |
| R-02 | [MEDIUM] | [entry Name] | [statement] |

Rules citable without context.
  PASS: "Do not allocate X until Y confirms ownership -- callee owns X, not caller."
  FAIL: "Ownership assumptions need re-examination."

After the table, run RULES-ANCHORED:

  RULES-ANCHORED:
    R-01: tier [HIGH] confirmed against [Name] Severity: [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against [Name] Severity: [MEDIUM] -- ALIGNED
    [MISALIGNED: correct tier annotation before proceeding]

Do not proceed to Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write one section: "Pattern of inherited errors." 2-4 sentences.
Name any structural origin shared by two or more corrections; if none, state it.

== PHASE 6: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."
A blind spot is a type of wrong thinking, not a topic area.

STEP 1 -- Name blind spot categories.
  Labels transferable to a different topic without rewriting fail.

STEP 2 -- Assign each correction to exactly one category.
  Unclassified entries: one-sentence explanation.

STEP 3 -- "What the blind spot map reveals." 2-3 sentences.
  NON-DERIVABILITY CONSTRAINT: state something not visible from individual
  corrections or category tallies.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team.
Register: "Before you build {topic}, the correction record requires you to know..."

Close the loop with the NO-ECHO COST. Name the specific assumption the next team
would have inherited without this artifact that would have caused the greatest
design error. This converts the no-echo cost declaration from a general warning
into a specific, named avoided failure.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (position 1: no-echo cost + structural provenance)
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- ordered HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE; flagged entries show RE-RUN
     after Resolution Protocol was applied)
  7. Surprise hierarchy (ranked with rationale)
  8. Rules of Thumb (table + RULES-ANCHORED)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction forward statement (closes the loop with no-echo cost)
  12. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-05 -- Combined: All three axes (V-01 + V-02 + V-03)

**Axes combined:** Imperative-only phase specifications (V-01) + CHAIN-FLAG
resolution protocol (V-02) + no-echo cost framing (V-03). The critical interaction
surface: can imperative-only phrasing convey the resolution protocol's multi-step
repair procedures at the required specificity? The protocol requires "copy verbatim"
and "character-for-character" precision -- whether imperative sentences can carry
that precision without explanatory context determines whether V-01's register
reduction helps or hurts V-02's protocol compliance. The inertia frame adds a
grounding rationale for the protocol's exclusion rule (element [3] Source not
found) that does not rely on explanatory prose within the phase block.

**Hypothesis:** If the resolution protocol is structurally robust (the steps are
precise enough as imperative commands without explanatory rationale), V-05 is the
tightest possible specification: every phase is a command, every gate is reparable,
and the institutional purpose precedes all content. If imperative phrasing loses
precision on the repair steps -- producing CHAIN-COMPLETE tokens after paraphrase
repairs rather than verbatim repairs -- V-05 reveals that the resolution protocol's
explanatory prose is load-bearing and cannot be safely converted to imperative
commands without degrading protocol compliance.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== ENFORCEMENT MECHANISM =======================================================

NO-ECHO COST:

Without this artifact, the next team inherits every false assumption embedded in
today's design materials. Signal gathering transforms those assumptions into
discoveries -- but without a topic:echo, discoveries remain owned by the current
team and never reach the next. The next team re-encounters the same assumptions,
runs the same signals, and arrives at the same corrections. The echo is the only
mechanism by which signal-generated knowledge outlives the team that gathered it.

This artifact's institutional function: prevent the next team from carrying
assumptions that today's signals have already disproved.

ENFORCEMENT MECHANISM -- STRUCTURAL PROVENANCE:

Tier: STRUCTURAL (not temporal).

Distinguishing property: the PBI-writing role operates under role-scope exclusion.
Access to signal artifacts is removed at role-scope level. Temporal provenance
sequences phases but does not prevent cross-phase reasoning. Structural provenance
removes access architecturally. The boundary is enforced, not instructed.

Reviewer implication: C-13 content analysis is confirmatory rather than probative.
Independence is enforced; content analysis verifies that enforcement held.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Write before reading any signal artifacts. One entry per implied assumption.

Format:
  PB-[NN]:   [Belief statement: "Today's materials imply that X will behave as Y."]

Use belief language only. No signal knowledge. Freeze before PHASE 1.
Do not anticipate handle labels. Entries use belief language only.

== HANDLE LEDGER ===============================================================

Read all signal artifacts first. Write one entry per surprise.

Format:
  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language only.]

Confirm independence: no PBI entry names its handle label.
No HL entry echoes a PBI entry verbatim.

== CORRECTION RECORD ===========================================================

All fields required. No blank or N/A.

  Name:            [HL-[NN] label. Encode the correction, not the event.]
  PBI-Ref:         [PB-[NN]. The prior belief corrected.]
  Source:          [namespace:skill:artifact. No prose.]

  What today's materials imply:
                   ["Today's materials imply that..." or "A new team would assume..."
                   Degree variants fail. Generic-material-critique fails.]

  What the signals showed instead:
                   [Direct claim. No hedges. Prohibited: "may suggest" / "appears
                   to indicate" / "seems like" / "could mean" / "might be" /
                   "it is possible that".]

  What the next team would build wrong:
                   [Specific component, flow, or decision. No softeners.]

  What the next team must decide before proceeding:
                   [Specific blocking question or action. No deferrals.]

  Verified:        [Verbatim text of PB-[NN]. Verbatim sentence from source.
                   Not identifiers. Not paraphrase. Actual text of both.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Apply before drafting each entry:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"
  YES -> draft the entry. It prevents one instance of the no-echo cost.
  NO  -> excluded.

== CORRECTION ENFORCEMENT ======================================================

Rule 1: Write every entry for the next team. Prohibit "We found that X".
  Rewrite to "Today's materials imply X". Prohibit "we" in materials-imply field.

Rule 2: Direct claims only. No hedges. Prohibited constructs apply to every field.

Rule 3: Each entry self-contained. Name assumption, correction, wrong design,
  and blocking decision. Define domain terms within the entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Name both source artifacts.
Emit: "Neither [A] nor [B] alone revealed this -- their intersection showed that
today's materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Draft all entries. Order HIGH -> MEDIUM -> LOW. Do not write synthesis sections.

== PHASE 2: REGISTER AUDIT ====================================================

Run field by field for every entry. Rewrite every discovery-register field.

  Source: Prohibit prose. Fix to namespace:skill:artifact.

  What today's materials imply:
    Prohibit "We found X" / "The team expected X". Fix to "Today's materials imply..."
    Prohibit "Materials tend to underspecify X". Fix to specific implied claim.

  What the next team would build wrong:
    Prohibit "Worth noting" / "Bears watching". Fix to specific wrong design.

  What the next team must decide:
    Prohibit deferrals. Fix to specific blocking decision.

  Verified: Prohibit identifier-only. Fix: verbatim PB-[NN] text and verbatim
  source sentence.

Complete when every non-Name field is in correction register.

== PHASE 3: ENTRY GATE ========================================================

Run for every entry. Gate blocks appear in the artifact.

  GATE: [entry Name]
    PBI-Ref          [PASS / FAIL: {problem} -- rewrite]
    Source           [PASS / FAIL: {problem} -- rewrite]
    Materials imply  [PASS / FAIL: narration or generic -- rewrite]
    Signals showed   [PASS / FAIL: {hedge} -- rewrite]
    Wrong design     [PASS / FAIL: softener -- rewrite]
    Next decision    [PASS / FAIL: deferral -- rewrite]
    Verified         [PASS / FAIL: identifier-only -- quote actual text]
  STATUS: CLEARED / NOT CLEARED

Rewrite all FAIL fields. Re-run. Repeat until CLEARED.
Block Phase 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ============================================

Run after all gates CLEARED. Check chain consistency only.
Do not repeat register checks.

For each entry:

  CHAIN: [entry Name]
    [1] PBI-Ref: does PB-[NN] describe the belief in "What today's materials
        imply"? Quote PBI entry text to confirm.
    [2] Handle: does entry Name match HL-[NN] title exactly?
    [3] Source: does Source artifact exist in $ARGUMENTS signal set?
    [4] Verified quotation: is the Verified text verbatim? Not paraphrase.

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

Any CHAIN-FLAG blocks further production.
Apply RESOLUTION PROTOCOL before re-running any flagged entry.

== RESOLUTION PROTOCOL =========================================================

CHAIN-FLAG on element [1] PBI-Ref:
  1. Re-read PBI. Locate PB-[NN] at identifier in PBI-Ref.
  2. Copy belief statement verbatim into Verified field (PBI half).
  3. If belief statement does not match materials-imply field: update PBI-Ref
     to the correct identifier. Repeat steps 1-2.
  4. Re-run CHAIN: block. Block Phase 4 until CHAIN-COMPLETE.

CHAIN-FLAG on element [2] Handle:
  1. Re-read Handle Ledger. Locate HL entry for this surprise.
  2. Copy HL-[NN] title character-for-character into entry Name.
  3. If no HL entry exists: add it to Handle Ledger first.
  4. Re-run CHAIN: block. Block Phase 4 until CHAIN-COMPLETE.

CHAIN-FLAG on element [3] Source:
  1. Re-read signal artifact list for $ARGUMENTS.
  2. Locate artifact by namespace, skill, filename.
  3. Update Source to exact path: namespace:skill:artifact.
  4. If artifact not in signal set: exclude this entry. An entry without a
     traceable source is not a prevented failure -- it is unsubstantiated.
     The no-echo cost requires entries to be verifiable.
  5. Re-run CHAIN: block. Block Phase 4 until CHAIN-COMPLETE.

CHAIN-FLAG on element [4] Verified quotation:
  1. Re-open source artifact at cited Source path.
  2. Locate sentence most directly contradicting the PBI belief.
  3. Copy that sentence verbatim. Replace source-half of Verified field.
  4. Re-read PB-[NN] at identifier in PBI-Ref.
  5. Copy belief statement verbatim. Replace PBI-half of Verified field.
  6. Re-run CHAIN: block. Block Phase 4 until CHAIN-COMPLETE.

Block Phase 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale.
Name the design decision at risk for each entry. Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ===================================================

Produce RULES OF THUMB table. HIGH and MEDIUM only. Exclude LOW.

| Rule | Tier | Entry | Statement (<=20 words) |
|------|------|-------|------------------------|
| R-01 | [HIGH] | [entry Name] | [statement] |
| R-02 | [MEDIUM] | [entry Name] | [statement] |

Rules citable without context:
  PASS: "Do not allocate X until Y confirms ownership -- callee owns X, not caller."
  FAIL: "Ownership assumptions need re-examination."

Run RULES-ANCHORED after the table:

  RULES-ANCHORED:
    R-01: tier [HIGH] confirmed against [Name] Severity: [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against [Name] Severity: [MEDIUM] -- ALIGNED
    [MISALIGNED: correct tier annotation. Block Phase 5 until ALIGNED.]

Block Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write "Pattern of inherited errors" section. 2-4 sentences.
Name any structural origin shared by two or more corrections.
If none: state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write "Blind Spot Map" section.

STEP 1: Name blind spot categories. Each is a type of wrong thinking, not a
  topic area. Labels transferable to a different topic without rewriting fail.

STEP 2: Assign each correction to exactly one category.
  Unclassified entries: one-sentence explanation.

STEP 3: Write "What the blind spot map reveals" -- 2-3 sentences.
  NON-DERIVABILITY CONSTRAINT: state something not visible from individual
  corrections or category tallies alone.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team.
Register: "Before you build {topic}, the correction record requires you to know..."
Close the loop with the NO-ECHO COST. Name the assumption the next team would have
inherited without this artifact that would have caused the greatest design error.
Convert the general no-echo warning into a specific avoided failure.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.
Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (position 1: no-echo cost + structural provenance)
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- ordered HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE; flagged entries show RE-RUN
     after Resolution Protocol was applied)
  7. Surprise hierarchy (ranked with rationale)
  8. Rules of Thumb (table + RULES-ANCHORED)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction forward statement (closes the loop with no-echo cost)
  12. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## Round 7 differential summary

**Under v7 (max 170):** All five predicted at 170/170. All retain C-22, C-23,
C-24 intact from R6 V-03 baseline. No degradation expected.

**What each variation probes that R6 didn't:**

| Dimension | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| Imperative-only phase register | YES | no | no | no | YES |
| CHAIN-FLAG resolution protocol | no | YES | no | YES | YES |
| No-echo cost in ENFORCEMENT MECHANISM | no | no | YES | YES | YES |
| Inertia-grounded exclusion rule (element [3]) | no | no | no | YES | YES |

**C-26 remains untested:** No R7 variation adds a RULES-ANCHORED-COMPLETE closure
token to Phase 4B. All five retain the current Phase 4B gate structure: blocking
condition named, MISALIGNED halts production, but no positive terminal signal
when all rules pass. C-26 is the isolated target for R8:

> RULES-ANCHORED-COMPLETE: all [N] rules ALIGNED -- Phase 4B gate closed.

This would make Phase 4B's gate passage auditable by positive token (parallel to
CHAIN-COMPLETE in Phase 3B) rather than by absence of MISALIGNED entries, completing
symmetric gate semantics across all three production gates.
```

---

**Key design decisions across the 5 variations:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| Axis | Phrasing register | Lifecycle: resolution protocol | Inertia framing | V-02+V-03 | V-01+V-02+V-03 |
| Phase spec style | Imperative-only | Full prose | Full prose | Full prose | Imperative-only |
| CHAIN-FLAG gate | Hard stop (baseline) | Hard stop + named repair | Hard stop (baseline) | Hard stop + named repair | Hard stop + named repair |
| ENFORCEMENT MECHANISM position 1 | YES | YES | YES | YES | YES |
| No-echo cost declared | No | No | YES | YES | YES |
| Phase 7 closes loop | No | No | Required | Required | Required |
| New criterion probed | (none, tests register) | C-25 (resolution protocol) | C-27 (no-echo cost) | C-25 + C-27 | C-25 + C-27 + register |

**The critical R7 diagnostic:** V-01 is the risk case. If explanatory prose in phase specs is load-bearing for C-18/C-19 compliance (the "structurally distinct from ENTRY GATE" rationale tells the reviewer *what* the audit is checking vs what it is not), V-01 may drop below 170. V-02 through V-05 all use full prose in their phase specs, so if V-01 drops while V-02 holds, that identifies exactly which prose is instructional.
