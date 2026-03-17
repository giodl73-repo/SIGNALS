---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 6
rubric: v6
---

# Variations: `topic:echo` -- Round 6

**Rubric:** v6 | **Date:** 2026-03-16

---

## Design Context

R5 V-05 achieved 155/155 under v6 -- the current gold ceiling. The three new v6
criteria (C-19, C-20, C-21) are satisfied by R5 V-05 via mechanisms that emerge
from its structure: the ENTRY GATE partially satisfies C-19's chain verification
requirement; the BLIND SPOT MAP + FORWARD STATEMENT partially satisfy C-20's
distillation requirement; the CORRECTION ENFORCEMENT section partially satisfies
C-21's navigability requirement.

R6 tests whether EXPLICIT mechanisms for each criterion produce more reliable output
than the implicit emergence seen in R5 V-05. Three single-axis variations each make
one mechanism maximally explicit. Two combined variations test pairwise and full-set
interaction. All five must maintain C-01 through C-21 without degradation.

**New criteria targeted by R6:**

- **C-19** -- Post-production chain integrity audit emitting CHAIN-COMPLETE tokens
  per entry, re-verifying all four chain elements [PBI-Ref, Handle, Source, Verified
  quotation] independently after the ENTRY GATE. R5 V-05 satisfies C-19 via gate
  checks but does not emit discrete CHAIN-COMPLETE tokens from a named audit phase.
  V-01 adds an explicit PHASE 3B that fires post-gate and produces visible tokens.

- **C-20** -- Rules of Thumb section encoding HIGH/MEDIUM surprises in <=20-word
  quotable form, tier-annotated, with a named RULES-ANCHORED traceability check. R5
  V-05 satisfies C-20 via the CORRECTION FORWARD STATEMENT but without a structured
  table or named traceability check. V-02 adds an explicit PHASE 4B that fires
  post-hierarchy and produces a titled table with RULES-ANCHORED verification.

- **C-21** -- Enforcement mechanism declaration in a headed section findable without
  full-artifact reading, including tier label, distinguishing property, and reviewer
  implication. R5 V-05 satisfies C-21 via the CORRECTION ENFORCEMENT section but
  the declaration is rules-focused; a reviewer must read Rule 1 to find the framing
  claim. V-03 places the declaration FIRST in its own headed section before entries.

**Variation axes selected:**

1. **Lifecycle emphasis** (V-01) -- Explicit CHAIN INTEGRITY AUDIT phase. Fires
   after PHASE 3 (ENTRY GATE). Emits CHAIN-COMPLETE or CHAIN-FLAG per entry.
   Tests whether a named post-production audit produces stronger C-19 compliance
   than gate-embedded verification.

2. **Output format** (V-02) -- Rules of Thumb as a structured table with
   RULES-ANCHORED traceability check. Fires after the surprise hierarchy. Tests
   whether a titled, tier-annotated distillation table produces stronger C-20
   compliance than a narrative forward statement.

3. **Role sequence** (V-03) -- Enforcement mechanism declaration placed FIRST,
   before entries. A dedicated headed section before CORRECTION RECORD declares
   tier, distinguishing property, and reviewer implication. Tests whether
   first-position placement produces stronger C-21 compliance than embedded
   declaration.

**Predicted score map (v6, max 155):**

| Variant | C-19 | C-20 | C-21 | Asp (v6) | Composite | vs R5 V-05 |
|---------|------|------|------|-----------|-----------|------------|
| V-01 | PASS (explicit phase, 4-element tokens) | PASS (R5 level) | PASS (R5 level) | 13/13 | 155 | = |
| V-02 | PASS (R5 level) | PASS (table + RULES-ANCHORED) | PASS (R5 level) | 13/13 | 155 | = |
| V-03 | PASS (R5 level) | PASS (R5 level) | PASS (first headed section) | 13/13 | 155 | = |
| V-04 | PASS (explicit phase) | PASS (table + check) | PASS (R5 level) | 13/13 | 155 | = |
| V-05 | PASS (explicit phase) | PASS (table + check) | PASS (first headed section) | 13/13 | 155 | = |

Key differential: if all five score 155/155, multiple structural forms achieve the
ceiling. If any single-axis variation drops below 155, R5 V-05's implicit mechanism
for that criterion was load-bearing and the rubric's PASS was generous. This would
trigger v7 refinement of the PASS condition for the dropped criterion.

---

## V-01 -- Single-axis: Lifecycle emphasis -- Explicit chain integrity audit phase

**Variation axis:** Lifecycle emphasis -- A named PHASE 3B: CHAIN INTEGRITY AUDIT
fires after the ENTRY GATE and before synthesis phases. All four chain elements are
re-verified per entry: [1] PBI-Ref identifier points to the correct prior belief,
[2] Handle matches the Handle Ledger, [3] Source artifact exists in the signal set,
[4] Verified quotation accurately represents cited content. Each entry receives a
visible CHAIN-COMPLETE or CHAIN-FLAG token. No other changes from R5 V-05 structure.

**Hypothesis:** R5 V-05's ENTRY GATE checks correction-register quality (field
format, framing, hedge-free language) but does not independently confirm that cited
identifiers point to the correct content. A PBI-Ref that is formally valid (e.g.,
"PB-02") may point to the wrong prior belief. A Verified quotation that is
syntactically present may not accurately represent the cited source. C-19 requires
post-production re-verification structurally distinct from the gate. If the gate
already catches all chain failures through register-quality checking, V-01 scores
identically to R5 V-05. If chain failures exist beyond register failures, V-01's
explicit audit makes C-19 compliance auditable from output via token emission where
R5 V-05's implicit compliance requires reviewer re-derivation.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries -- both sections are produced independently. PBI
entries use belief language; Handle Ledger entries use finding language.

This artifact uses STRUCTURAL PROVENANCE: the PBI-writing role operates under
role-scope exclusion and cannot access signal artifacts regardless of instruction.
Independence is enforced by role-scope exclusion, not by phase sequencing alone.
C-13 content analysis is confirmatory rather than probative.

== HANDLE LEDGER ===============================================================

After reading signals, produce a Handle Ledger before writing entries. Each entry:

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief
              language. Must not echo the corresponding PBI entry verbatim.]

Independence test: no PBI entry names its handle label; no HL entry echoes a PBI
entry verbatim.

== CORRECTION RECORD ===========================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [Cite the Handle Ledger entry: HL-[NN] label. Encode the
                   correction: "The Cascade Inversion" (what changed) over
                   "Unexpected Cascade Behavior" (something happened).]

  PBI-Ref:         [Identifier of the prior belief this entry corrects: PB-[NN].
                   Must point to the PBI entry that held this assumption before
                   signals were read.]

  Source:          [namespace:skill:artifact. Not "signals indicated" / "research
                   showed" / "the data suggested".]

  What today's materials imply:
                   [Future-team framing only: "Today's materials imply that..." or
                   "A new team reading the current spec would assume..."
                   Degree variants fail. Generic-material-critique fails.]

  What the signals showed instead:
                   [Direct claim contradicting the implied assumption. Prohibited:
                   "may suggest" / "appears to indicate" / "seems like" / "could
                   mean" / "might be" / "it is possible that".]

  What the next team would build wrong:
                   [Specific design error if they carry the inherited assumption.
                   Name the component, flow, or decision. Prohibited: "worth noting"
                   / "bears watching" / "important to keep in mind".]

  What the next team must decide before proceeding:
                   [Specific blocking question or action. Not "further investigation
                   needed" / "keep an eye on this" / "monitor this".]

  Verified:        [Quote the actual text of PB-[NN] (the belief statement) and the
                   key sentence from the source artifact that overturns it. Not
                   identifiers only -- actual text of both, sufficient to confirm
                   cited identifiers point to the right content.]

  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER ===========================================================

Before drafting any entry, apply:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES -> correction is load-bearing. Draft the entry.
  NO  -> excluded. Absorbed findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 -- Correction framing:
  Every entry is written for the next team. Discovery framing ("We found that X")
  is prohibited -- rewrite as "Today's materials imply X; they should not." No
  "we" in the "What today's materials imply" field.

Rule 2 -- Claim-only voice:
  Direct claims only. No hedges. Prohibited constructs from "What the signals
  showed instead" apply to every field.

Rule 3 -- Entry completeness:
  Write each entry so a new team member reading only that entry can understand what
  today's materials lead them to assume, what they should assume instead, and what
  they would build wrong. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this -- their intersection showed that
   today's materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries. Order HIGH -> MEDIUM -> LOW by Severity.
Do not write synthesis sections yet.

== PHASE 2: REGISTER AUDIT ====================================================

Execute the REGISTER AUDIT field by field. Rewrite any field in discovery register
before proceeding to Phase 3.

  Source field:
    DISCOVERY: "signals indicated X" / "research showed X" / "analysis revealed X"
    CORRECTION: namespace:skill:artifact
    -> Any attribution prose fails. Replace with the artifact path.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X" / "We assumed X"
    CORRECTION: "Today's materials imply that..." / "A new team would assume..."
    -> Original-team narration fails. Rewrite to future-team framing.

    DISCOVERY: "Materials tend to underspecify X" / "Specs rarely address Y"
    CORRECTION: "Today's spec implies X will behave as [specific claim]"
    -> Generic-category critique fails. Rewrite to specific inherited assumption.

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching" / "Has implications"
    CORRECTION: "[Component/flow/decision] would be built as [wrong design] because
                 today's materials imply [wrong assumption]"
    -> Severity statements fail. Rewrite to specific wrong design.

  What the next team must decide:
    DISCOVERY: "Further investigation needed" / "Keep an eye on" / "Monitor this"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"
    -> Deferrals fail. Rewrite to specific blocking decision or open question.

  Verified field:
    DISCOVERY: "PB-02 confirmed / source confirmed" (identifiers only)
    CORRECTION: "[Actual quoted text of PB-02] / [Actual quoted sentence from source]"
    -> Identifier-only attestation fails. Quote the actual text of both.

Register audit complete when every non-Name field of every entry is in correction
register.

== PHASE 3: ENTRY GATE ========================================================

After register audit, run the ENTRY GATE. Gate declarations appear in the artifact.

For each entry, produce a gate block:

  GATE: [entry Name]
    PBI-Ref          [PASS: identifier confirmed in PBI section]
                     [FAIL: {problem} -- rewrite required]
    Source           [PASS: namespace:skill:artifact confirmed]
                     [FAIL: {problem} -- rewrite required]
    Materials imply  [PASS: future-team framing confirmed]
                     [FAIL: original-team narration or generic critique -- rewrite]
    Signals showed   [PASS: direct claim, no hedges]
                     [FAIL: {hedge construct} -- rewrite required]
    Wrong design     [PASS: specific component/flow/decision named]
                     [FAIL: softener found -- rewrite to specific wrong design]
    Next decision    [PASS: specific blocking decision or question confirmed]
                     [FAIL: deferral -- rewrite to specific decision point]
    Verified         [PASS: actual text quoted for both PBI entry and source finding]
                     [FAIL: identifier-only -- quote actual text of both]
  STATUS: CLEARED / NOT CLEARED

STATUS NOT CLEARED: rewrite every FAIL field. Re-run the gate block. Repeat until
STATUS: CLEARED. Do not proceed to Phase 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ============================================

After all ENTRY GATE blocks show STATUS: CLEARED, run the CHAIN INTEGRITY AUDIT.

This audit is structurally distinct from the ENTRY GATE:
  - ENTRY GATE: confirms each field is in correction register (format and framing)
  - CHAIN INTEGRITY AUDIT: confirms the evidentiary chain is internally consistent

For each entry, independently re-verify all four chain elements:

  CHAIN: [entry Name]
    [1] PBI-Ref: does PB-[NN] point to the belief that "What today's materials
        imply" describes? Confirm by quoting the PBI entry text.
    [2] Handle: does entry Name match HL-[NN] in the Handle Ledger? Confirm HL
        title and entry Name are the same label.
    [3] Source: does the Source artifact exist in the signal set for $ARGUMENTS?
        Confirm namespace, skill, and artifact name are resolvable.
    [4] Verified quotation: does the Verified field quote text that accurately
        represents the PBI entry and source finding at the cited identifiers?
        Confirm the quoted text is not a paraphrase -- it is the actual text.

  Emit one token per entry:
    CHAIN-COMPLETE: [entry Name] -- all four elements verified
    CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

A CHAIN-FLAG requires correction of the flagged element before proceeding.
Do not proceed to Phase 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Produce a numbered list with argued rationale:

  1. [entry Name] -- [why this has highest design impact: names the design decision
     at risk and what must be redesigned before other work can proceed]
  2. [entry Name] -- [rationale at the same standard]
  ...

Assertion without argument fails. "This is most critical" without naming what
becomes uncorrectable if missed fails.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write one section: "Pattern of inherited errors."

Do two or more corrections share a structural origin -- a family of false assumptions
today's materials systematically produce? Write 2-4 sentences. Name any pattern; if
none, state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem -- a type of wrong thinking, not a topic area.

STEP 1 -- NAME THE BLIND SPOT CATEGORIES.

  PASS: "Ownership inversion -- materials assumed the caller owns X; signals showed
         the callee owns X, reversing the allocation model"
  FAIL: "State management" -- labels a domain, not a type of wrong thinking

A category label transferable to a different topic without rewriting fails.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: state something not visible from
reading individual corrections or tallying category assignments. State what the
pattern of blind spots reveals about the original materials as a system.

If no pattern: "The corrections address independent blind spots; the map reveals no
shared structural origin in today's materials."

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. Register: "Before you build {topic}, the
correction record requires you to know that..." Specific to these corrections.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts. Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ==========================================================

  1. Pre-committed Belief Inventory (PBI)
  2. Handle Ledger
  3. Corrections -- ordered HIGH -> MEDIUM -> LOW
  4. Entry Gate blocks (all STATUS: CLEARED)
  5. Chain Integrity Audit (all CHAIN-COMPLETE)
  6. Surprise hierarchy (ranked with rationale)
  7. Pattern of inherited errors
  8. Blind Spot Map
  9. Correction forward statement
  10. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-02 -- Single-axis: Output format -- Rules of Thumb structured table with RULES-ANCHORED check

**Variation axis:** Output format -- After the surprise hierarchy (PHASE 4), a
distinct PHASE 4B: RULES OF THUMB produces a titled table encoding HIGH and MEDIUM
surprises as <=20-word quotable rules with tier annotations. A named RULES-ANCHORED
traceability check follows the table, confirming tier alignment between each rule
and its parent entry. LOW entries are excluded. The chain audit from V-01 is
retained. C-21 is satisfied at R5 V-05 level. V-02 tests the C-20 axis in isolation
against V-01's baseline.

**Hypothesis:** R5 V-05's CORRECTION FORWARD STATEMENT produces a distillation
(1-3 sentences to the next team) but without a structured table, tier annotations,
or a named traceability check. A future team citing a forward statement cannot verify
its tier without re-reading the full entry. C-20 requires: (a) the distillation layer
exists as a distinct section, (b) rules are tier-annotated, (c) a named traceability
check confirms alignment. If the FORWARD STATEMENT already satisfies C-20, V-02
scores identically to V-01. If the structured table + RULES-ANCHORED check adds
C-20 compliance, the titled form is the load-bearing mechanism for auditable
distillation.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries. PBI entries use belief language; Handle Ledger
entries use finding language.

This artifact uses STRUCTURAL PROVENANCE: the PBI-writing role operates under
role-scope exclusion and cannot access signal artifacts regardless of instruction.
Independence is enforced by role-scope exclusion, not phase sequencing alone.
C-13 content analysis is confirmatory rather than probative.

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

  PBI-Ref:         [Identifier of the prior belief this entry corrects: PB-[NN].]

  Source:          [namespace:skill:artifact. No attribution prose.]

  What today's materials imply:
                   [Future-team framing: "Today's materials imply that..." or
                   "A new team reading the current spec would assume..."
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

  YES -> draft the entry.
  NO  -> excluded. Absorbed findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 -- Correction framing:
  Every entry written for the next team. "We found that X" is prohibited -- rewrite
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
    CORRECTION: namespace:skill:artifact
    -> Any attribution prose fails. Replace with the artifact path.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X" / "We assumed X"
    CORRECTION: "Today's materials imply that..." / "A new team would assume..."
    -> Original-team narration fails.

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
    CORRECTION: "[Actual quoted text of PB-02] / [Actual quoted sentence from source]"
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
                     [FAIL: original-team narration or generic critique -- rewrite]
    Signals showed   [PASS: direct claim, no hedges]
                     [FAIL: {hedge construct} -- rewrite required]
    Wrong design     [PASS: specific component/flow/decision named]
                     [FAIL: softener -- rewrite to specific wrong design]
    Next decision    [PASS: specific blocking decision or question confirmed]
                     [FAIL: deferral -- rewrite]
    Verified         [PASS: actual text quoted for both PBI entry and source finding]
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
    [1] PBI-Ref: does PB-[NN] point to the belief "What today's materials imply"
        describes? Quote the PBI entry text to confirm.
    [2] Handle: does entry Name match HL-[NN] in the Handle Ledger?
    [3] Source: does the Source artifact exist in the signal set for $ARGUMENTS?
    [4] Verified quotation: does the Verified field quote text accurately
        representing the cited PBI entry and source finding? Not a paraphrase.

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

CHAIN-FLAG requires correction before proceeding. Do not proceed to Phase 4
until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale:

  1. [entry Name] -- [why this has highest design impact: names the decision at risk]
  2. [entry Name] -- [rationale at the same standard]
  ...

Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ===================================================

After the hierarchy, write the RULES OF THUMB table. Encode every HIGH and MEDIUM
entry as a <=20-word quotable rule. LOW entries are excluded.

| Rule | Tier | Entry | Statement (<=20 words) |
|------|------|-------|------------------------|
| R-01 | [HIGH] | [entry Name] | [statement] |
| R-02 | [MEDIUM] | [entry Name] | [statement] |

Rules must be citable without context:
  PASS: "Do not allocate X until Y confirms ownership -- callee owns X, not caller."
  FAIL: "Ownership assumptions need re-examination based on the signals."

After the table, run RULES-ANCHORED:

  RULES-ANCHORED:
    R-01: tier [HIGH] confirmed against entry [Name] Severity: [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against entry [Name] Severity: [MEDIUM] -- ALIGNED
    [Any misalignment: MISALIGNED -- correct tier annotation before proceeding]

Do not proceed to Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write one section: "Pattern of inherited errors."

Two or more corrections sharing a structural origin? Write 2-4 sentences. If none,
state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem -- a type of wrong thinking, not a topic area.

STEP 1 -- NAME THE BLIND SPOT CATEGORIES.

  PASS: "Sequence inversion -- materials assumed X precedes Y; signals showed Y
         precedes X, invalidating the commit ordering assumption"
  FAIL: "State management" -- labels a domain, not a type of wrong thinking

Category labels transferable to a different topic without rewriting fail.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: state something not visible from
reading individual corrections or tallying categories.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. "Before you build {topic}, the correction
record requires you to know that..." Specific to these corrections.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.

== ARTIFACT STRUCTURE ==========================================================

  1. Pre-committed Belief Inventory (PBI)
  2. Handle Ledger
  3. Corrections -- ordered HIGH -> MEDIUM -> LOW
  4. Entry Gate blocks (all STATUS: CLEARED)
  5. Chain Integrity Audit (all CHAIN-COMPLETE)
  6. Surprise hierarchy (ranked with rationale)
  7. Rules of Thumb (table + RULES-ANCHORED)
  8. Pattern of inherited errors
  9. Blind Spot Map
  10. Correction forward statement
  11. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-03 -- Single-axis: Role sequence -- Enforcement mechanism as first navigable section

**Variation axis:** Role sequence -- The enforcement mechanism declaration is moved
to the FIRST section of the artifact, before the CORRECTION RECORD schema. The
section is titled "ENFORCEMENT MECHANISM" and contains all three C-21 elements: (a)
tier label (structural provenance), (b) the distinguishing property (role-scope
exclusion vs phase sequencing), and (c) reviewer implication ("independence is
enforced, not instructed; C-13 content analysis is confirmatory rather than
probative"). The chain audit and Rules of Thumb from V-02 are retained. V-03 tests
the C-21 axis against V-02's baseline.

**Hypothesis:** R5 V-05's CORRECTION ENFORCEMENT section is rules-focused (Rule 1,
Rule 2, Rule 3). A reviewer navigating by section headers sees "CORRECTION
ENFORCEMENT" and must read the rules to locate C-17 content. C-21 requires the
enforcement claim to be findable from section headers alone. If "CORRECTION
ENFORCEMENT" is sufficient for C-21 navigability, V-03 scores identically to V-02.
If the section title must signal enforcement mechanism classification (not enforcement
rules), and first-position placement ensures the section is encountered before any
entry, then V-03's explicit "ENFORCEMENT MECHANISM" section title is the load-bearing
mechanism and V-02 fails C-21 despite satisfying C-17.

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
content; it cannot by itself prove independence was maintained. With structural
provenance, content analysis confirms; without it, content analysis is the only
evidence.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries.

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
    DISCOVERY: "signals indicated X" / "research showed X"
    CORRECTION: namespace:skill:artifact -> Prose attribution fails.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X"
    CORRECTION: "Today's materials imply that..." -> Original-team narration fails.

    DISCOVERY: "Materials tend to underspecify X"
    CORRECTION: "Today's spec implies X will behave as [specific claim]"
    -> Generic-category critique fails.

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching"
    CORRECTION: "[Component] would be built as [wrong design]" -> Severity fails.

  What the next team must decide:
    DISCOVERY: "Further investigation needed" / "Monitor this"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"
    -> Deferrals fail.

  Verified field:
    DISCOVERY: "PB-02 confirmed" (identifier only)
    CORRECTION: "[Actual quoted text of PB-02] / [Actual quoted sentence from source]"
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
        representing the cited PBI entry and source finding?

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

CHAIN-FLAG requires correction before proceeding. Do not proceed to Phase 4
until every entry shows CHAIN-COMPLETE.

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

Category names must characterize type of wrong thinking. A label transferable to
a different topic without rewriting fails.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: something not visible from reading
individual corrections or tallying categories.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. "Before you build {topic}, the correction
record requires you to know that..." Specific to these corrections.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (headed section -- navigable from headers)
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

## V-04 -- Combined: Lifecycle emphasis + Output format (Chain audit + Rules of Thumb)

**Axes combined:** V-01's explicit CHAIN INTEGRITY AUDIT phase + V-02's RULES OF
THUMB table with RULES-ANCHORED check. No change to enforcement mechanism placement
from R5 V-05 (C-21 satisfied at R5 level via CORRECTION ENFORCEMENT section).

**Hypothesis:** The chain audit and Rules of Thumb phases address non-overlapping
production stages: the audit fires after PHASE 3 (ENTRY GATE) to verify chain
consistency; the Rules of Thumb fires after PHASE 4 (SURPRISE HIERARCHY) to distill
the top-impact findings. No interaction surface exists -- the audit does not affect
distillation; the distillation does not affect audit. Together they provide explicit
structural coverage for C-19 and C-20. Predicted 155/155. V-04 vs V-05 differential:
V-05 adds first-position enforcement mechanism section. If V-04 = V-05, enforcement
placement adds nothing above embedded declaration for C-21 scoring.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a
correction the next team needs before they begin -- something today's design
materials do not contain, and that a new team would carry as a false assumption
without this artifact.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries. PBI entries use belief language; Handle Ledger
entries use finding language.

This artifact uses STRUCTURAL PROVENANCE: the PBI-writing role operates under
role-scope exclusion and cannot access signal artifacts regardless of instruction.
Independence is enforced by role-scope exclusion, not phase sequencing alone.
C-13 content analysis is confirmatory rather than probative.

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

  YES -> draft the entry.
  NO  -> excluded.

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
    DISCOVERY: "signals indicated X" / "research showed X"
    CORRECTION: namespace:skill:artifact -> Prose attribution fails.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X"
    CORRECTION: "Today's materials imply that..."
    -> Original-team narration fails.

    DISCOVERY: "Materials tend to underspecify X"
    CORRECTION: "Today's spec implies X will behave as [specific claim]"
    -> Generic-category critique fails.

  What the next team would build wrong:
    DISCOVERY: "Worth noting" / "Bears watching"
    CORRECTION: "[Component] would be built as [wrong design]"
    -> Severity statements fail.

  What the next team must decide:
    DISCOVERY: "Further investigation needed" / "Monitor this"
    CORRECTION: "[Specific decision: choose X or Y before building Z]"
    -> Deferrals fail.

  Verified field:
    DISCOVERY: identifier-only
    CORRECTION: actual quoted text of both PBI entry and source finding
    -> Identifier-only fails.

Register audit complete when every non-Name field is in correction register.

== PHASE 3: ENTRY GATE ========================================================

Run ENTRY GATE after register audit. Declarations appear in the artifact.

For each entry:

  GATE: [entry Name]
    PBI-Ref          [PASS / FAIL: {problem}]
    Source           [PASS / FAIL: {problem}]
    Materials imply  [PASS / FAIL: narration or generic critique]
    Signals showed   [PASS / FAIL: {hedge construct}]
    Wrong design     [PASS / FAIL: softener found]
    Next decision    [PASS / FAIL: deferral found]
    Verified         [PASS / FAIL: identifier-only]
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
        imply"? Quote the PBI entry text.
    [2] Handle: does entry Name match HL-[NN] in the Handle Ledger?
    [3] Source: does the Source artifact exist in the signal set for $ARGUMENTS?
    [4] Verified quotation: does the Verified field quote text accurately
        representing the cited PBI entry and source finding? Not a paraphrase.

  CHAIN-COMPLETE: [entry Name] -- all four elements verified
  CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

CHAIN-FLAG requires correction before proceeding. Do not proceed to Phase 4
until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale:

  1. [entry Name] -- [why: names the design decision at risk]
  2. [entry Name] -- [rationale]
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
    R-01: tier [HIGH] confirmed against [Name] Severity [HIGH] -- ALIGNED
    R-02: tier [MEDIUM] confirmed against [Name] Severity [MEDIUM] -- ALIGNED
    [MISALIGNED: correct tier before proceeding]

Do not proceed to Phase 5 until all rules show ALIGNED.

== PHASE 5: PATTERN OF INHERITED ERRORS =========================================

Write one section: "Pattern of inherited errors."

Two or more corrections sharing a structural origin? Write 2-4 sentences. If none,
state that explicitly.

== PHASE 6: BLIND SPOT MAP ====================================================

Write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem -- a type of wrong thinking, not a topic area.

STEP 1 -- NAME THE BLIND SPOT CATEGORIES.

Category names must characterize type of wrong thinking. A label transferable to a
different topic without rewriting fails.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: something not visible from reading
individual corrections or tallying categories.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. "Before you build {topic}, the correction
record requires you to know that..." Specific to these corrections.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.

== ARTIFACT STRUCTURE ==========================================================

  1. Pre-committed Belief Inventory (PBI)
  2. Handle Ledger
  3. Corrections -- ordered HIGH -> MEDIUM -> LOW
  4. Entry Gate blocks (all STATUS: CLEARED)
  5. Chain Integrity Audit (all CHAIN-COMPLETE)
  6. Surprise hierarchy (ranked with rationale)
  7. Rules of Thumb (table + RULES-ANCHORED)
  8. Pattern of inherited errors
  9. Blind Spot Map
  10. Correction forward statement
  11. What this correction record excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-05 -- Combined: All three axes (Chain audit + Rules of Thumb + First-position enforcement)

**Axes combined:** V-01's CHAIN INTEGRITY AUDIT + V-02's RULES OF THUMB table +
V-03's first-position ENFORCEMENT MECHANISM section.

**Hypothesis:** The three mechanisms target C-19, C-20, and C-21 at their highest
explicit level. Each fires at a non-overlapping artifact position: ENFORCEMENT
MECHANISM declares provenance before any entry is written (C-21 navigability);
CHAIN INTEGRITY AUDIT re-verifies chain consistency after all gates clear (C-19
tokens); RULES OF THUMB distills the hierarchy into citable form and verifies tier
alignment (C-20 traceability). A reviewer reading section headers can navigate
directly to all three v6 mechanisms without reading entry content: "ENFORCEMENT
MECHANISM" (C-21), "CHAIN INTEGRITY AUDIT" (C-19 tokens), "RULES OF THUMB" (C-20
distillation). Predicted 155/155. The three phases compose without interference --
provenance declaration primes correction register before entries; chain audit
confirms chain correctness independently after gate; Rules of Thumb extracts
auditable distillation after hierarchy.

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
reasoning. Structural provenance removes that access at role-scope level: the PBI
role has no signal-read permission. The boundary is architectural, not behavioral.

Reviewer implication: independence is enforced, not instructed. C-13 content
analysis (PBI belief language vs Handle Ledger finding language) is confirmatory
rather than probative. With structural provenance, content analysis confirms;
without it, content analysis is the only evidence.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries.

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

  YES -> draft the entry.
  NO  -> excluded. Absorbed findings belong in topic-story, not topic-echo.

== CORRECTION ENFORCEMENT ======================================================

Rule 1 -- Correction framing:
  Every entry written for the next team. "We found that X" is prohibited -- rewrite
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
    CORRECTION: namespace:skill:artifact
    -> Any attribution prose fails. Replace with the artifact path.

  What today's materials imply:
    DISCOVERY: "We found X" / "The team expected X" / "We assumed X"
    CORRECTION: "Today's materials imply that..." / "A new team would assume..."
    -> Original-team narration fails.

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
    CORRECTION: "[Actual quoted text of PB-02] / [Actual quoted sentence from source]"
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
                     [FAIL: original-team narration or generic critique -- rewrite]
    Signals showed   [PASS: direct claim, no hedges]
                     [FAIL: {hedge construct} -- rewrite required]
    Wrong design     [PASS: specific component/flow/decision named]
                     [FAIL: softener -- rewrite to specific wrong design]
    Next decision    [PASS: specific blocking decision or question confirmed]
                     [FAIL: deferral -- rewrite]
    Verified         [PASS: actual text quoted for both PBI entry and source finding]
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

CHAIN-FLAG requires correction before proceeding. Do not proceed to Phase 4
until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ================================================

Rank all entries by design impact. Numbered list with argued rationale:

  1. [entry Name] -- [why: names the design decision at risk and what cannot
     proceed until this correction is absorbed]
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
    [Any misalignment: MISALIGNED -- correct tier annotation before proceeding]

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

  PASS: "Ownership inversion -- materials assumed caller owns X; signals showed
         callee owns X, reversing the allocation model"
  FAIL: "State management" -- labels a domain, not wrong thinking

A label transferable to a different topic without rewriting fails.

STEP 2 -- ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 -- SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences. NON-DERIVABILITY CONSTRAINT: something not visible from reading
individual corrections or tallying categories.

== PHASE 7: CORRECTION FORWARD STATEMENT ========================================

Write 1-3 sentences to the next team. "Before you build {topic}, the correction
record requires you to know that..." Specific to these corrections.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES ================================

Name at least two excluded categories with counts.

== ARTIFACT STRUCTURE ==========================================================

  1. Enforcement Mechanism (headed section -- navigable from headers)
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

## Round 6 Design Notes

**Why these three axes:**

- **Lifecycle emphasis** (V-01) tests whether an explicit named phase for chain
  integrity audit produces more auditable C-19 compliance than gate-embedded chain
  checking. The structural difference: PHASE 3B fires post-gate and emits
  CHAIN-COMPLETE tokens as first-class output elements. A reviewer reading only the
  artifact output can verify that all four chain elements were independently re-
  verified. R5 V-05's gate verifies format and framing but a reviewer cannot
  distinguish "gate confirmed chain consistency" from "gate confirmed register
  quality" without re-analyzing gate blocks. With PHASE 3B, chain integrity is
  auditable from output alone.

- **Output format** (V-02) tests whether a structured distillation table with a
  named traceability check produces more reliable C-20 compliance than a narrative
  forward statement. The structural difference: the RULES OF THUMB table is titled
  and cell-citable; a future signal artifact can reference "R-01" without embedding
  the rule text. RULES-ANCHORED makes tier alignment auditable in the output rather
  than implicit in forward statement phrasing. A reviewer can verify C-20 by
  reading the table header and RULES-ANCHORED block without re-reading full entries.

- **Role sequence** (V-03) tests whether first-position placement of the enforcement
  mechanism declaration changes C-21 compliance. The structural difference: a
  reviewer using section headers finds "ENFORCEMENT MECHANISM" as the first listed
  section -- before CORRECTION RECORD, before PBI, before entries. The section title
  signals enforcement mechanism classification (not enforcement rules). R5 V-05's
  CORRECTION ENFORCEMENT section is primarily rules-focused; C-17 content is embedded
  within the rules rather than declared as the section's primary purpose.

**Predicted interaction in V-04:**

Chain audit and Rules of Thumb fire at non-overlapping stages. Audit fires after
PHASE 3; Rules of Thumb fires after PHASE 4. No shared mechanism means no
interference. V-04 is predicted 155/155 by explicit coverage of C-19 and C-20,
with C-21 satisfied at R5 V-05 level via the CORRECTION ENFORCEMENT section.

**Predicted interaction in V-05:**

V-05 adds first-position ENFORCEMENT MECHANISM section to V-04. If V-05 = V-04,
first-position placement does not add C-21 compliance beyond embedded declaration.
If V-05 > V-04, the navigability test fails for V-04's embedded declaration -- a
reviewer cannot find the enforcement claim from section headers alone in V-04.

**What R6 cannot tell us:**

If all five variations score 155/155, R6 confirms multiple structural forms achieve
the ceiling but does not reveal which form is most robust across different input
types (well-specified signals vs sparse signals). A follow-on round testing these
variations against signals of varying density would answer that question.

If single-axis variations (V-01, V-02, V-03) score below 155, R6 reveals that R5
V-05's implicit satisfaction of the corresponding criterion was weaker than the
rubric's PASS indicated, and would trigger v7 refinement of the PASS condition for
the dropped criterion.
