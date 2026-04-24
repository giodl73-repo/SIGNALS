---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 8
rubric: v8
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v8-2026-03-16.md
rubric_max: 185
---

# Variations: `topic:echo` -- Round 8 (2026-03-16)

**Rubric:** v8 (2026-03-16) | **Criteria count:** 27 (5 essential / 3 recommended / 19 aspirational)

---

## Design Context

Three new criteria were added to the v8 rubric from Round 7 variations:

**C-25 -- CHAIN-FLAG resolution protocol with named repair action per flag type** (gate: C-22).
C-22 makes CHAIN-FLAG a hard production stop. C-25 makes the stop deterministically
reparable -- exactly one named repair action per flag type. Without a resolution protocol
a reviewer who encounters a CHAIN-FLAG knows to stop but not how to fix the failure. Two
reviewers may take different actions, both of which clear the flag without resolving the
underlying chain inconsistency. With a named protocol, clearing the gate proves the
inconsistency was fixed. First appeared in R7 V-02's CHAIN INTEGRITY AUDIT specification.

**C-26 -- NO-ECHO COST declaration in head-position enforcement section** (gate: C-24).
C-24 makes the ENFORCEMENT MECHANISM section primary (position 1). C-26 makes it
consequential -- the reviewer encounters mechanism classification AND institutional stakes
before any entries. Without a NO-ECHO COST declaration the head-position section tells a
reviewer what enforcement mechanism is in use; with it, it also tells the reviewer what is
lost by skipping. First appeared in R7 V-03's ENFORCEMENT MECHANISM section.

**C-27 -- Forward Statement names the specific avoided failure** (gate: C-07).
C-07 makes the artifact forward-facing. C-27 makes the forward claim verifiable -- the
institutional purpose stated at the start is confirmed at completion. The Forward Statement
must name the specific failure prevented, not summarize findings. When C-26 is present,
C-27 also closes the loop opened by the NO-ECHO COST declaration. First appeared in R7 V-03.

**Round 7 scoring under v8:**

| Variation | C-25 | C-26 | C-27 | Asp (v8) | Composite |
|-----------|------|------|------|----------|-----------|
| V-01 | FAIL | FAIL | FAIL | 12/19 = 60 | 150 |
| V-02 | PASS | FAIL | FAIL | 13/19 = 65 | 175 |
| V-03 | FAIL | PASS | PASS | 15/19 = 75 | 180 |
| V-04 | PASS | FAIL | PASS | 15/19 = 75 | 180 |
| V-05 | PASS | FAIL | PASS | 15/19 = 75 | 180 |

No R7 variation reaches 185. The gap is C-26: every variation that passes C-25 fails C-26,
and the one variation that passes C-26 (V-03) fails C-25.

**R8 primary target:** C-25 + C-26 + C-27 all PASS in a single variation = composite 185.

**R8 isolated target:** RULES-ANCHORED-COMPLETE closure token -- a named token emitted
when the RULES-ANCHORED traceability check confirms all rules show ALIGNED, closing the
distillation phase auditably in the same way CHAIN-COMPLETE closes the chain audit.
No R7 variation seeds this pattern. This is the C-28 candidate for v9.

**R8 variation plan -- three single-axis, two combined:**

| Variation | Primary axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | Lifecycle emphasis (RULES-ANCHORED-COMPLETE) | Adds positive-state closure token to distillation phase; base is R7 V-04 (C-25+C-27); C-26 still absent |
| V-02 | Phrasing register (formal declaration blocks + standalone RESOLUTION PROTOCOL block) | Formal block phrasing for PHASE 3B forces RESOLUTION PROTOCOL to be named explicitly; base is R7 V-03 (C-26+C-27); adds C-25 |
| V-03 | Role sequence (Enforcement Framer at Step 0 with NO-ECHO COST) | Dedicated role at head writes the enforcement section with institutional cost; base is R7 V-04 (C-25+C-27); adds C-26 |
| V-04 | Lifecycle + role sequence | RULES-ANCHORED-COMPLETE + Enforcement Framer + NO-ECHO COST; targets 185 + R8 isolated pattern |
| V-05 | Full synthesis: all three axes | Formal blocks + Enforcement Framer + RULES-ANCHORED-COMPLETE; maximal coverage |

**Discriminating pairs:**
- V-01 vs V-02: isolates whether RULES-ANCHORED-COMPLETE (no C-26) or formal blocks + C-25 (no R8 target) is more reliable
- V-02 vs V-03: isolates whether phrasing register or role sequence is the more reliable vehicle for C-26
- V-03 vs V-04: isolates whether RULES-ANCHORED-COMPLETE degrades C-26 when combined with EF role
- V-04 vs V-05: isolates whether adding formal block phrasing register helps or conflicts with the three-role structure

---

## V-01 -- Single-axis: Lifecycle emphasis (RULES-ANCHORED-COMPLETE closure token)

**Variation axis:** Lifecycle emphasis -- PHASE 4B emits RULES-ANCHORED-COMPLETE (or
RULES-ANCHORED-FAIL) after the RULES-ANCHORED traceability check passes. No other
changes from R7 V-04.

**Hypothesis:** The RULES-ANCHORED check (C-20) and its blocking condition (C-23) prevent
the distillation phase from closing with misaligned tier annotations. But no positive-state
token is emitted -- a reviewer reading the output knows the check existed but must re-derive
pass/fail from the per-rule aligned/misaligned statements. RULES-ANCHORED-COMPLETE closes
this gap: it makes the distillation phase close with the same auditable semantics as
CHAIN-COMPLETE closes the chain audit (C-19). An external reviewer reads
RULES-ANCHORED-COMPLETE and knows the traceability check passed externally, not merely
that the writer stated it passed. This is the v9 criterion candidate seeded by R8.

**Base:** R7 V-04 (C-25 PASS via RESOLUTION PROTOCOL in PHASE 3B; C-27 PASS via Forward
Statement naming specific avoided failure; C-26 FAIL -- no NO-ECHO COST).

**New element:** RULES-ANCHORED-COMPLETE / RULES-ANCHORED-FAIL token after the
RULES-ANCHORED traceability check in PHASE 4B.

**Expected v8 score:**
- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 18/19 -> 90 (C-26 FAIL; C-25 PASS, C-27 PASS, all prior v7 criteria PASS)
- **Composite: 180** + RULES-ANCHORED-COMPLETE seeded as R8 isolated target

---

Topic: {topic}

Synthesize what was unexpected. This is not a summary. Every correction must be something
a new team would carry as a false assumption from today's design materials -- invisible
without this artifact.

== ENFORCEMENT MECHANISM =========================================================

Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion. The PBI-writing role cannot access signal
artifacts regardless of instruction. Phase sequencing orders phases but does not block
cross-phase reasoning; role-scope exclusion does.
Reviewer implication: Independence is enforced by role boundary, not by instruction.
C-13 content analysis (PBI belief language vs. HL finding language separation) is
confirmatory rather than probative.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ==========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory.
Write one entry per assumption the design materials currently imply. Each entry:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from their
corresponding surprise entries. PBI entries use belief language; Handle Ledger
entries use finding language.

== HANDLE LEDGER =================================================================

After reading signals, produce a Handle Ledger before writing entries. Each entry:

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief
              language. Must not echo the corresponding PBI entry verbatim.]

Independence test: no PBI entry names its handle label; no HL entry echoes a PBI
entry verbatim.

== CORRECTION RECORD =============================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [HL-[NN] label. Encode the correction: "The Cascade Inversion"
                   not "Unexpected Cascade Behavior".]
  PBI-Ref:         [PB-[NN] -- identifier of the prior belief this corrects.]
  Source:          [namespace:skill:artifact. No attribution prose.]
  What today's materials imply:
                   ["Today's materials imply that..." or "A new team would assume..."
                   Degree variants fail. Generic-category critique fails.]
  What the signals showed instead:
                   [Direct claim. No hedges.]
  What the next team would build wrong:
                   [Specific component, flow, or decision. No softeners.]
  What the next team must decide before proceeding:
                   [Specific blocking decision or question. No deferrals.]
  Verified:        [Actual text of PB-[NN] AND key sentence from source artifact.
                   Identifiers alone fail.]
  Severity:        [HIGH / MEDIUM / LOW]

== STILL-LIVE FILTER =============================================================

Before drafting any entry: "Would a new team reading only today's design materials
carry this as a false assumption going in?"
YES -> draft the entry. NO -> exclude; route to topic-story.

== CORRECTION ENFORCEMENT ========================================================

Rule 1: Every entry written for the next team. Discovery narration fails.
Rule 2: Direct claims only. No hedges in any field.
Rule 3: Each entry self-contained. Domain terms defined within.

== PHASE 1: DRAFT ALL ENTRIES ====================================================

Write all entries HIGH -> MEDIUM -> LOW by Severity. No synthesis sections yet.

== PHASE 2: REGISTER AUDIT =======================================================

Field by field. Rewrite any field in discovery register before Phase 3.

  Source: "signals indicated X" -> namespace:skill:artifact.
  Materials imply: "We found X" -> "Today's materials imply X".
  Wrong design: "worth noting" -> "[component] would be built as [wrong design]
    because today's materials imply [wrong assumption]".
  Next decision: "further investigation needed" -> "[specific blocking decision]".
  Verified: identifiers only -> quote actual text of both PBI entry and source finding.

== PHASE 3: ENTRY GATE ===========================================================

For each entry:

  GATE: [entry Name]
    PBI-Ref          [PASS: identifier confirmed in PBI] / [FAIL: {problem}]
    Source           [PASS: namespace:skill:artifact confirmed] / [FAIL: {problem}]
    Materials imply  [PASS: future-team framing] / [FAIL: {narration type}]
    Signals showed   [PASS: direct claim, no hedges] / [FAIL: {hedge construct}]
    Wrong design     [PASS: specific component named] / [FAIL: softener found]
    Next decision    [PASS: specific blocking decision] / [FAIL: deferral found]
    Verified         [PASS: actual text quoted for both] / [FAIL: identifiers only]
  STATUS: CLEARED / NOT CLEARED

STATUS NOT CLEARED: rewrite every FAIL field. Re-run gate block. Repeat until
STATUS: CLEARED. Do not proceed to PHASE 3B until every entry shows STATUS: CLEARED.

== PHASE 3B: CHAIN INTEGRITY AUDIT ===============================================

Structurally distinct from PHASE 3:
  - ENTRY GATE: each field in correction register (format + framing)
  - CHAIN INTEGRITY AUDIT: evidentiary chain internally consistent

For each entry, independently re-verify four chain elements:

  CHAIN: [entry Name]
    [1] PBI-Ref: PB-[NN] points to belief described in "What today's materials imply"?
        Quote PBI text.
    [2] Handle: entry Name matches HL-[NN] in Handle Ledger? Quote HL title.
    [3] Source: namespace:skill:artifact resolvable in this signal set?
    [4] Verified quotation: quoted text accurately represents cited content (not paraphrase)?

  Token:
    CHAIN-COMPLETE: [entry Name] -- all four elements verified
    CHAIN-FLAG: [entry Name] -- [element N]: {description of inconsistency}

CHAIN-FLAG IS A HARD GATE: any CHAIN-FLAG halts artifact completion until resolved.
Do not proceed to PHASE 4 until every entry shows CHAIN-COMPLETE.

RESOLUTION PROTOCOL:
  PBI-Ref mismatch (element 1): replace PBI-Ref with the PB identifier whose text
    matches the belief stated in "What today's materials imply". Do not alter the
    belief statement to fit the cited PB entry.
  Handle mismatch (element 2): update entry Name to match HL label exactly, or update
    the HL entry to match the intended label -- not both. Resolve in Handle Ledger
    first; then propagate to entry Name.
  Source absent (element 3): replace Source with namespace:skill:artifact of an
    artifact actually in the signal set. If no qualifying artifact exists, demote
    entry to the discard log with typed route reason.
  Verified quotation inaccurate (element 4): re-quote actual text from both PBI entry
    and source artifact. Paraphrase is not acceptable -- character-accurate quotation.

== PHASE 4: SURPRISE HIERARCHY ===================================================

Rank all entries by design impact with argued rationale:

  1. [entry Name] -- [why highest design impact: names decision at risk; what cannot
     proceed without correction]
  2. [entry Name] -- [rationale at same standard]

Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ======================================================

Distill HIGH and MEDIUM entries as quotable rules. LOW entries excluded.

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED traceability check:
For each rule, confirm tier annotation matches Severity from the corresponding entry.
  "[rule] -> tier [HIGH|MEDIUM] matches entry [Name] Severity [HIGH|MEDIUM]: ALIGNED"
  "[rule] -> tier [X] does not match entry [Name] Severity [Y]: MISALIGNED"

RULES-ANCHORED BLOCKS: any MISALIGNED rule halts progression. Correct tier annotation
before proceeding to PHASE 5.

After all rules show ALIGNED, emit one token:
  RULES-ANCHORED-COMPLETE -- all rules ALIGNED; distillation phase closed
  RULES-ANCHORED-FAIL: [rule] -- {tier mismatch description}

RULES-ANCHORED-COMPLETE closes the distillation phase with the same auditable
semantics as CHAIN-COMPLETE closes the chain audit: a reviewer reading
RULES-ANCHORED-COMPLETE knows tier alignment was externally confirmed, not merely
that the writer stated it was confirmed.

== PHASE 5: PATTERN OF INHERITED ERRORS ==========================================

One section: "Pattern of inherited errors." Do two or more corrections share a
structural origin? 2-4 sentences. Name the pattern; if none, state explicitly.

== PHASE 6: BLIND SPOT MAP =======================================================

Section: "Blind Spot Map." Name blind spot categories as types of wrong thinking,
not topic areas. Assign each correction to one category. Synthesis: 2-3 sentences,
non-derivable from individual corrections alone.

== PHASE 7: CORRECTION FORWARD STATEMENT =========================================

1-3 sentences to the next team. Register: "Before you build {topic}, the correction
record requires you to know that..."

Name the specific failure this artifact prevented. Identify the concrete false
assumption the next team would have carried without it and the specific investigation
path that assumption would have misdirected.

PASS: "This echo prevented the next team from inheriting the assumption that X, which
would have directed [specific investigation] toward Y; signals showed Z instead."
FAIL: advisory framing, summary of findings, or "the next team should investigate X"
without naming the specific failure avoided.

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES =================================

Name at least two excluded categories with counts. Implicit exclusion does not satisfy.

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM section
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE)
  7. Rules of Thumb table with RULES-ANCHORED-COMPLETE token
  8. Surprise hierarchy (ranked with rationale)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction Forward Statement (names specific avoided failure)
  12. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

---

## V-02 -- Single-axis: Phrasing register (formal declaration blocks + standalone RESOLUTION PROTOCOL)

**Variation axis:** Phrasing register -- every gate, audit, and protocol in the prompt is
written as a named formal declaration block (ALL-CAPS header, rule-lines, typed fields,
explicit gate-return specification). RESOLUTION PROTOCOL appears as its own headed
declaration block within PHASE 3B, not as bulleted continuation of the CHAIN-FLAG
description.

**Hypothesis:** R7 V-03 passes C-26 (NO-ECHO COST in enforcement section) and C-27
(Forward Statement names avoided failure) but fails C-25 -- no RESOLUTION PROTOCOL is
present. The formal block phrasing axis tests whether making RESOLUTION PROTOCOL a
standalone named block with its own ALL-CAPS header reliably produces C-25 compliance.
The pattern is proven: GATEKEEPER FUNCTION DECLARATION and ENFORCEMENT MECHANISM work
because their constraints are visually distinct from surrounding text. Applying the same
pattern to RESOLUTION PROTOCOL makes it as discoverable as the gate itself -- a reviewer
scanning for gate specifications finds the repair protocol in the same visual register.

**Base:** R7 V-03 (C-26 PASS via NO-ECHO COST in ENFORCEMENT MECHANISM; C-27 PASS via
Forward Statement naming avoided failure; C-25 FAIL -- no RESOLUTION PROTOCOL).

**New element:** RESOLUTION PROTOCOL as a standalone headed declaration block in PHASE 3B.

**Expected v8 score:**
- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 19/19 -> 95 (C-25 PASS from RESOLUTION PROTOCOL block; C-26 PASS retained;
  C-27 PASS retained; all prior criteria maintained)
- **Composite: 185**

---

Topic: {topic}

Synthesize what was unexpected. This is not a summary. Every correction must be something
a new team would carry as a false assumption from today's design materials -- invisible
without this artifact.

== ENFORCEMENT MECHANISM =========================================================

Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion. The PBI-writing role cannot access signal
artifacts regardless of instruction. Phase sequencing orders phases but does not block
cross-phase reasoning; role-scope exclusion does. Structural provenance is enforced by
role boundary, not instruction compliance.
Reviewer implication: Independence is enforced, not instructed. C-13 content analysis
is confirmatory rather than probative.

NO-ECHO COST: If this artifact is absent, the next team inherits the team's pre-signal
belief set as if it were validated design knowledge. They cannot distinguish beliefs that
were pre-committed (and potentially falsified by signals) from beliefs formed after signal
reading. Every false assumption embedded in today's materials propagates invisibly into the
next team's design decisions, with no artifact marking where the investigation diverged
from expectation.

== PRE-COMMITTED BELIEF INVENTORY (PBI) ==========================================

Before reading any signal artifacts, produce a Pre-committed Belief Inventory:

  PB-[NN]:   [Belief statement -- future-team framing: "Today's materials imply
              that X will behave as Y." No signal knowledge permitted.]

Freeze the PBI before PHASE 1. PBI entries must not use handle labels from the
Handle Ledger. PBI entries use belief language; HL entries use finding language.

== HANDLE LEDGER =================================================================

After reading signals, produce a Handle Ledger before writing entries:

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief
              language. Must not echo the corresponding PBI entry verbatim.]

== CORRECTION RECORD =============================================================

Apply to every correction. All fields required.

  Name / PBI-Ref / Source / What today's materials imply / What signals showed
  instead / What next team would build wrong / What next team must decide /
  Verified (actual text of PBI entry AND source finding) / Severity (HIGH/MEDIUM/LOW)

Still-Live Filter: "Would a new team reading only today's materials carry this as a
false assumption?" YES -> draft. NO -> exclude; route to topic-story.

Correction Enforcement:
  Rule 1: Correction register only. "We found X" -> "Today's materials imply X."
  Rule 2: Direct claims in all fields. No hedges.
  Rule 3: Each entry self-contained.

== PHASE 1: DRAFT ALL ENTRIES ====================================================

Write all entries HIGH -> MEDIUM -> LOW. No synthesis sections yet.

== PHASE 2: REGISTER AUDIT =======================================================

Field by field. Rewrite any field in discovery register before Phase 3.

== PHASE 3: ENTRY GATE ===========================================================

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:     Per-entry field validation. Confirms format + framing.
             Does not verify internal chain consistency (PHASE 3B).
Scope:       One entry at a time. Cannot detect cross-entry or
             collection-level failures.
Fields:      PBI-Ref / Source / Materials imply / Signals showed /
             Wrong design / Next decision / Verified
Status:      STATUS: CLEARED -- all fields PASS
             STATUS: NOT CLEARED -- rewrite all FAIL fields; re-run
Gate:        STATUS: NOT CLEARED halts progression.
             Proceed to PHASE 3B only after all entries CLEARED.
----------------------------------------------------------------------
```

  GATE: [entry Name]
    PBI-Ref          [PASS / FAIL: {problem}]
    Source           [PASS / FAIL: {problem}]
    Materials imply  [PASS / FAIL: {narration type}]
    Signals showed   [PASS / FAIL: {hedge construct}]
    Wrong design     [PASS / FAIL: softener]
    Next decision    [PASS / FAIL: deferral]
    Verified         [PASS / FAIL: identifiers only]
  STATUS: CLEARED / NOT CLEARED

== PHASE 3B: CHAIN INTEGRITY AUDIT ===============================================

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Purpose:     Post-gate chain consistency verification. Confirms the
             four chain elements are internally consistent -- distinct
             from ENTRY GATE which confirmed field register.
Elements:
  [1] PBI-Ref points to correct belief (quote PBI text)
  [2] Handle matches HL title (quote HL entry)
  [3] Source resolvable in this signal set
  [4] Verified quotation is actual text, not paraphrase
Token:
  CHAIN-COMPLETE: [entry Name] -- all four verified
  CHAIN-FLAG: [entry Name] -- [element N]: {inconsistency description}
Gate:        CHAIN-FLAG IS A HARD GATE. Any CHAIN-FLAG halts artifact
             completion until the flagged element is repaired via the
             RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type:

  PBI-Ref mismatch (element 1):
    Replace PBI-Ref with the PB identifier whose text matches the
    belief stated in "What today's materials imply". The belief
    statement is ground truth; the identifier must map to it.
    Do not alter the belief statement to fit the cited PB entry.

  Handle mismatch (element 2):
    Resolve in Handle Ledger first -- determine whether HL-[NN] title
    or entry Name is authoritative, then propagate from source to
    dependent. Do not update both independently.

  Source absent (element 3):
    Replace Source with namespace:skill:artifact of an artifact
    actually in the signal set. If no qualifying artifact exists,
    demote the entry to the discard log with typed route reason.

  Verified quotation inaccurate (element 4):
    Re-quote actual text from both PBI entry and source artifact.
    Paraphrase is not acceptable. If source cannot be located,
    apply element 3 protocol first.
----------------------------------------------------------------------
```

Do not proceed to PHASE 4 until every entry shows CHAIN-COMPLETE.

== PHASE 4: SURPRISE HIERARCHY ===================================================

Rank by design impact with argued rationale. Names decision at risk per entry.
Assertion without argument fails.

== PHASE 4B: RULES OF THUMB ======================================================

HIGH and MEDIUM entries only, <=20 words each, tier-annotated. LOW excluded.

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED traceability check: each rule's tier matches entry Severity.
  "[rule] -> ALIGNED / MISALIGNED"
RULES-ANCHORED BLOCKS on MISALIGNED. Correct before proceeding.

== PHASE 5: PATTERN OF INHERITED ERRORS ==========================================

"Pattern of inherited errors" -- 2-4 sentences. Named structural origin or stated absent.

== PHASE 6: BLIND SPOT MAP =======================================================

Categories as types of wrong thinking. Assign each correction. Synthesis 2-3 sentences,
non-derivable from individual corrections alone.

== PHASE 7: CORRECTION FORWARD STATEMENT =========================================

1-3 sentences to the next team. "Before you build {topic}, the correction record
requires you to know that..."

Name the specific failure this artifact prevented. Identify the concrete false assumption
the next team would have inherited without it and the specific investigation path that
assumption would have misdirected.

When NO-ECHO COST is declared at head position, this Forward Statement confirms it:
the cost declared prospectively must be confirmed or denied at completion. If the echo
prevented the specific failure class named in NO-ECHO COST, state so explicitly.

PASS: "This echo prevented the next team from inheriting the assumption that X, which
would have directed [specific investigation] toward Y; signals showed Z."
FAIL: advisory framing; summary of findings; "the next team should investigate X."

== PHASE 8: WHAT THIS CORRECTION RECORD EXCLUDES =================================

At least two excluded categories with counts.

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM section (with NO-ECHO COST)
  2. Pre-committed Belief Inventory (PBI)
  3. Handle Ledger
  4. Corrections -- HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (ENTRY GATE DECLARATION; all STATUS: CLEARED)
  6. Chain Integrity Audit (CHAIN INTEGRITY AUDIT DECLARATION; all CHAIN-COMPLETE)
  7. Resolution Protocol trace (RESOLUTION PROTOCOL DECLARATION; flags resolved)
  8. Rules of Thumb with RULES-ANCHORED check
  9. Surprise hierarchy (ranked)
  10. Pattern of inherited errors
  11. Blind Spot Map
  12. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  13. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

---

## V-03 -- Single-axis: Role sequence (Enforcement Framer at Step 0 with NO-ECHO COST)

**Variation axis:** Role sequence -- A dedicated Enforcement Framer (EF) role is introduced
at Step 0, running before BC and IA. The EF's sole function: write the ENFORCEMENT
MECHANISM section at head position. The EF derives the NO-ECHO COST from pre-investigation
materials only and is role-scope-excluded from signal artifacts and from all steps after 0.

**Hypothesis:** C-26 requires the NO-ECHO COST declaration in the head-position enforcement
section. If a single role (EF) owns both the enforcement classification and the cost
declaration, and that role is structurally excluded from all other phases, the NO-ECHO COST
cannot be constructed retrospectively from entry content -- it must be derived from design
materials alone. This creates stronger C-26 compliance than inline addition: the role
boundary enforces the prospective nature of the cost declaration structurally. EF is the
cost authority; BC is the belief authority; IA is the correction authority. Three distinct
roles at three exclusive phase boundaries.

**Base:** R7 V-04 (C-25 PASS via RESOLUTION PROTOCOL; C-27 PASS via Forward Statement
naming avoided failure; C-26 FAIL).

**New element:** Enforcement Framer (EF) role at Step 0, writing the ENFORCEMENT MECHANISM
section including NO-ECHO COST from design materials only. EF excluded from Steps 1-7.

**Expected v8 score:**
- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 19/19 -> 95 (C-25 PASS retained; C-26 PASS from EF + NO-ECHO COST;
  C-27 PASS retained; all prior v7 criteria maintained)
- **Composite: 185**

---

Topic: {topic}

Synthesize what was unexpected. Three roles operate at distinct phase boundaries with
exclusive scope. This is not a summary. Every correction is something a new team would
carry as a false assumption without this artifact.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Write the ENFORCEMENT MECHANISM section at position 1.
              Derive the NO-ECHO COST declaration from pre-investigation
              materials only: which false assumptions propagate if no
              echo is produced? The cost declaration is prospective --
              derived before any signals are read, not constructed from
              entry content after the fact.
Input:        Design materials only (specs, PRDs, briefs, prior art).
              Signal artifacts are outside EF scope regardless of
              instruction. This exclusion is what makes the NO-ECHO
              COST claim genuinely prospective.
Out-of-scope: PBI production (BC domain). Entry authoring (IA domain).
              Chain verification. Synthesis. Any step after Step 0.
Gate return:  ENFORCEMENT MECHANISM section complete with provenance
              tier, distinguishing property, reviewer implication,
              and NO-ECHO COST before Step 1 begins.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Frame every correction as what a future team would carry
              without this artifact.
Orienting:    "What would the next team build wrong because they did
              not know what the investigation revealed?"
Out-of-scope: PBI authorship (frozen at Step 1). Enforcement section
              (EF domain; immutable after Step 0).
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section

EF produces from design materials only:

== ENFORCEMENT MECHANISM =========================================================

Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries. EF writes
the cost declaration before signals are read. BC writes PBI before signals are read.
IA writes corrections from signals and cannot alter the frozen PBI or enforcement
section. No cross-phase reasoning is possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary, not by instruction.
Content analysis (PBI belief language vs. HL finding language) is confirmatory rather
than probative.

NO-ECHO COST: [EF derives from design materials only. Name the specific failure class
that propagates if this artifact is not produced: which beliefs embedded in today's
materials would the next team inherit as validated design knowledge? What category of
design error follows from carrying them? Generic statement ("this is important") fails.
Named failure class required: "The next team inherits the assumption that [specific
belief from today's spec], with no artifact marking it as falsified by investigation."]

---

### Step 1 -- [BC] Pre-committed Belief Inventory

From design materials only. No signal artifacts.

  PB-[NN]:   [Belief statement -- "Today's materials imply that X." No signal knowledge.]

PBI frozen at end of Step 1. BC excluded from Steps 2-7.

---

### Step 2 -- [IA] Handle Ledger

After reading signals, produce Handle Ledger before writing entries.

  HL-[NN]:   [Finding-specific label -- 2-5 words. Finding language, not belief language.
              Must not echo the corresponding PBI entry verbatim.]

Independence: no PBI entry names its handle; no HL entry echoes a PBI entry verbatim.

---

### Step 3 -- [IA] Draft All Corrections

Schema (all fields required):

  Name / PBI-Ref / Source / What today's materials imply / What signals showed instead /
  What next team would build wrong / What next team must decide / Verified (actual text
  of PBI entry AND source finding) / Severity (HIGH/MEDIUM/LOW)

Still-Live Filter: "Would a new team reading only today's materials carry this as a
false assumption?" YES -> draft. NO -> exclude; route to topic-story.

Correction Enforcement:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in all fields. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.

---

### Step 4 -- Register Audit

Field by field. Rewrite any field in discovery register before Step 5.

---

### Step 5 -- Entry Gate

  GATE: [entry Name]
    PBI-Ref / Source / Materials imply / Signals showed / Wrong design /
    Next decision / Verified
    [PASS / FAIL: {problem} for each]
  STATUS: CLEARED / NOT CLEARED

Do not proceed to Step 6 until every entry shows STATUS: CLEARED.

---

### Step 6 -- Chain Integrity Audit

  CHAIN: [entry Name]
    [1] PBI-Ref -> correct belief? Quote PBI text.
    [2] Handle matches HL? Quote HL title.
    [3] Source resolvable in signal set?
    [4] Verified quotation accurate (not paraphrase)?

  CHAIN-COMPLETE: [entry Name] -- all four verified
  CHAIN-FLAG: [entry Name] -- [element N]: {inconsistency}

CHAIN-FLAG IS A HARD GATE.

RESOLUTION PROTOCOL:
  PBI-Ref mismatch (element 1): replace PBI-Ref with matching identifier. Do not
    alter belief statement.
  Handle mismatch (element 2): resolve in Handle Ledger first; propagate to entry Name.
  Source absent (element 3): replace with resolvable artifact, or demote to discard log.
  Verified quotation inaccurate (element 4): re-quote actual text; paraphrase fails.

Do not proceed to Step 7 until every entry shows CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Rank by design impact with argued rationale. Names decision at
risk per entry. Assertion without argument fails.

**Rules of Thumb:** HIGH and MEDIUM entries only, <=20 words, tier-annotated. LOW excluded.

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule}             | {SURPRISE NAME} |
| [MEDIUM] | {rule}             | {SURPRISE NAME} |

RULES-ANCHORED traceability check: each rule's tier matches entry Severity.
  "[rule] -> ALIGNED / MISALIGNED"
RULES-ANCHORED BLOCKS on MISALIGNED. Correct before proceeding.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Types of wrong thinking (not topic areas). Assign each correction.
Synthesis: 2-3 sentences, non-derivable from individual corrections alone.

**Correction Forward Statement:**

1-3 sentences: "Before you build {topic}, the correction record requires you to know that..."

Name the specific failure this artifact prevented. Identify the concrete false assumption
the next team would have inherited and the specific investigation path it would have
misdirected.

This Forward Statement confirms the NO-ECHO COST declared by EF at Step 0: the
prospective cost claim must be confirmed or denied at completion. If the echo prevented
the specific failure class named in NO-ECHO COST, name it explicitly.

PASS: "This echo prevented the next team from inheriting [specific assumption], which
would have directed [specific investigation/skill] toward [Y]; signals showed [Z]."
FAIL: advisory framing; recommendations; summary without naming specific avoided failure.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM section (EF-authored; position 1; includes NO-ECHO COST)
  2. Pre-committed Belief Inventory (BC-authored)
  3. Handle Ledger (IA-authored)
  4. Corrections -- HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE; RESOLUTION PROTOCOL applied)
  7. Rules of Thumb with RULES-ANCHORED check
  8. Surprise hierarchy (ranked with rationale)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction Forward Statement (confirms EF's NO-ECHO COST; names specific avoided failure)
  12. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

---

## V-04 -- Combination: Lifecycle emphasis + Role sequence

**Variation axis:** Combination -- lifecycle emphasis (RULES-ANCHORED-COMPLETE closure
token) + role sequence (Enforcement Framer at Step 0 with NO-ECHO COST).

**Hypothesis:** V-01 adds RULES-ANCHORED-COMPLETE without C-26 (composite 180 + R8 target).
V-03 adds C-26 via EF role without RULES-ANCHORED-COMPLETE (composite 185). The combination
tests whether these two mechanisms interact. They operate at orthogonal positions: EF at
Step 0 (pre-investigation, writes enforcement frame with cost declaration) vs.
RULES-ANCHORED-COMPLETE in the distillation step (post-hierarchy, closes Rules of Thumb
phase). They share no mechanism and cannot conflict. If both pass, V-04 reaches composite
185 AND seeds the R8 isolated target -- the only R8 variation that satisfies all three
v8 criteria plus the v9 candidate in one prompt.

**Base:** V-03 (C-25 PASS, C-26 PASS, C-27 PASS; composite 185).
**New element:** RULES-ANCHORED-COMPLETE token in Rules of Thumb distillation step.

**Expected v8 score:**
- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 19/19 -> 95 (all v8 criteria PASS; RULES-ANCHORED-COMPLETE seeded for v9)
- **Composite: 185** + R8 isolated target seeded

---

Topic: {topic}

Synthesize what was unexpected. Three roles at distinct phase boundaries. Every correction
is something a new team would carry as a false assumption without this artifact.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Write the ENFORCEMENT MECHANISM section at artifact head
              position (position 1). Derive the NO-ECHO COST from
              design materials only before any signals are read.
              Cost declaration is prospective: declared before the
              investigation reveals what the surprises are.
Input:        Design materials only. Signal artifacts excluded.
Out-of-scope: PBI (BC domain). Entry authoring. Chain verification.
Phase scope:  Step 0 only. Excluded from Steps 1-7.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     PBI production from design materials only.
Phase scope:  Step 1 only. PBI frozen at end of Step 1.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Every output framed as what a future team would carry
              without this artifact.
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7. Cannot alter frozen PBI or EF's section.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section

EF writes from design materials only:

== ENFORCEMENT MECHANISM =========================================================

Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries. EF writes
the cost declaration before signals are read -- the claim is prospective. BC writes
the PBI before signals are read -- handles cannot contaminate beliefs. IA writes
corrections from signals and cannot alter the frozen PBI or enforcement section.
No cross-phase reasoning is possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. Content analysis
is confirmatory rather than probative.

NO-ECHO COST: [EF derives from design materials -- name the specific failure class
that propagates if this artifact is absent. Which beliefs in today's materials would
the next team inherit as validated design knowledge? What category of design error
follows? Named failure class required. Generic statements fail.]

---

### Step 1 -- [BC] PBI

From design materials only.

  PB-[NN]:   ["Today's materials imply that X." No signal knowledge.]

PBI frozen at end of Step 1.

---

### Step 2 -- [IA] Handle Ledger

  HL-[NN]:   [Finding-specific label -- finding language, not belief language.]

Independence: no PBI entry names its handle; no HL entry echoes a PBI entry verbatim.

---

### Step 3 -- [IA] Draft All Corrections

All fields required: Name / PBI-Ref / Source / What today's materials imply /
What signals showed instead / What next team would build wrong / What next team
must decide / Verified (actual text of PBI entry AND source finding) / Severity.

Still-Live Filter: "Would a new team carry this as a false assumption?" YES -> draft.
Correction Enforcement: correction register only; direct claims; self-contained.

---

### Step 4 -- Register Audit

Rewrite any field in discovery register before Step 5.

---

### Step 5 -- Entry Gate

  GATE: [entry Name]
    [all seven fields: PASS / FAIL: {problem}]
  STATUS: CLEARED / NOT CLEARED

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

  CHAIN: [entry Name]
    [1] PBI-Ref correct? Quote PBI text.
    [2] Handle matches HL? Quote HL title.
    [3] Source resolvable?
    [4] Verified quotation accurate?

  CHAIN-COMPLETE / CHAIN-FLAG per entry. CHAIN-FLAG IS A HARD GATE.

RESOLUTION PROTOCOL:
  PBI-Ref mismatch (element 1): replace PBI-Ref with matching identifier; do not
    alter belief statement.
  Handle mismatch (element 2): resolve in Handle Ledger first; propagate.
  Source absent (element 3): replace with resolvable artifact or demote to discard log.
  Verified inaccurate (element 4): re-quote actual text; paraphrase fails.

Do not proceed to Step 7 until all CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact with argued rationale. Names decision
at risk per entry. Assertion without argument fails.

**Rules of Thumb:** HIGH and MEDIUM entries only, <=20 words, tier-annotated. LOW excluded.

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule}             | {SURPRISE NAME} |
| [MEDIUM] | {rule}             | {SURPRISE NAME} |

RULES-ANCHORED traceability check: each rule's tier matches entry Severity.
  "[rule] -> tier [X] matches entry [Name] Severity [X]: ALIGNED"
  "[rule] -> tier [X] does not match entry Severity [Y]: MISALIGNED"

RULES-ANCHORED BLOCKS on MISALIGNED. Correct tier annotation before proceeding.

After all rules show ALIGNED, emit one token:
  RULES-ANCHORED-COMPLETE -- all rules ALIGNED; distillation phase closed
  RULES-ANCHORED-FAIL: [rule] -- {mismatch description}

RULES-ANCHORED-COMPLETE closes the distillation phase auditably: a reviewer reading
this token knows tier alignment was externally confirmed, not merely stated. This
mirrors CHAIN-COMPLETE's function in the chain audit.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Types of wrong thinking. Assign each correction. Synthesis:
2-3 sentences, non-derivable from individual corrections alone.

**Correction Forward Statement:**

1-3 sentences: "Before you build {topic}, the correction record requires you to know that..."

Name the specific failure this artifact prevented. Identify the concrete false assumption
the next team would have inherited and the investigation path it would have misdirected.

This statement closes two loops:
  1. Confirms the NO-ECHO COST declared by EF at Step 0 (prospective cost claim -> verified
     outcome: was the declared failure class avoided or incurred?).
  2. Makes the artifact's institutional purpose falsifiable: the artifact committed to
     preventing a specific failure class; completion must confirm it did.

PASS: "This echo prevented the next team from inheriting [specific assumption], which
would have directed [specific investigation] toward [Y]; signals showed [Z] instead."
FAIL: advisory framing; summary without naming specific avoided failure.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM section (EF; position 1; NO-ECHO COST)
  2. Pre-committed Belief Inventory (BC)
  3. Handle Ledger (IA)
  4. Corrections -- HIGH -> MEDIUM -> LOW
  5. Entry Gate blocks (all CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE; RESOLUTION PROTOCOL applied)
  7. Rules of Thumb with RULES-ANCHORED-COMPLETE token
  8. Surprise hierarchy (ranked)
  9. Pattern of inherited errors
  10. Blind Spot Map
  11. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  12. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

---

## V-05 -- Full synthesis: all three axes

**Variation axis:** Full combination -- lifecycle emphasis (RULES-ANCHORED-COMPLETE) +
phrasing register (formal declaration blocks throughout) + role sequence (Enforcement
Framer with NO-ECHO COST at Step 0).

**Hypothesis:** V-04 combines lifecycle + role sequence and targets 185 + R8 isolated
target. V-05 adds the phrasing register axis: every gate, audit, and protocol is written
as a named formal declaration block. This tests whether uniform formal register across all
three roles and all phases produces higher execution fidelity, or whether the added
structural weight conflicts with the three-role architecture. The discriminating question
between V-04 and V-05: does formal block phrasing add clarity (reinforcing gate semantics
through consistent visual register) or add noise (redundant formalism when role boundaries
already provide structure)?

**Base:** V-04 (all three v8 criteria PASS + RULES-ANCHORED-COMPLETE seeded).
**New element:** All gates, audits, and protocols written as titled formal declaration
blocks with ALL-CAPS headers, typed fields, and explicit gate-return specifications --
same visual register as ENFORCEMENT FRAMER and BELIEF CARTOGRAPHER declarations.

**Expected v8 score:**
- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 19/19 -> 95
- **Composite: 185** + RULES-ANCHORED-COMPLETE (R8 isolated target seeded)

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural constraint is a named formal protocol. This is not a summary.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section at artifact
              head position. Derive NO-ECHO COST from pre-investigation
              materials only -- before any signal reading begins.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section complete with provenance
              tier, distinguishing property, reviewer implication, and
              NO-ECHO COST before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective, not constructed from entry content. BC writes PBI
  before signals are read -- PBI entries cannot be contaminated by HL
  labels. IA writes corrections from signals and cannot alter the
  frozen PBI or enforcement section. No cross-phase reasoning is
  possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. C-13
  content analysis is confirmatory rather than probative.
NO-ECHO COST: [EF derives from design materials -- name the specific
  failure class that propagates if this artifact is not produced.
  Which beliefs in today's materials would the next team inherit as
  validated design knowledge? What category of design error follows?
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI entry
          verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name:     HL-[NN] label. Correction register: "The Cascade Inversion"
            not "Unexpected Cascade Behavior".
  PBI-Ref:  PB-[NN].
  Source:   namespace:skill:artifact.
  Implies:  "Today's materials imply that..." Degree variants fail.
  Showed:   Direct claim. No hedges.
  Wrong:    Specific component/flow/decision. No softeners.
  Decide:   Specific blocking decision. No deferrals.
  Verified: Actual text of PB-[NN] AND key sentence from source.
            Identifiers alone fail.
  Severity: HIGH / MEDIUM / LOW.

STILL-LIVE FILTER: "Would a new team carry this as a false assumption?"
  YES -> draft. NO -> exclude; route to topic-story.

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific
wrong component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only. Does
          not verify chain consistency (Step 6).
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide /
          Verified
Result:   PASS: {confirmed} / FAIL: {problem description}
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression. Rewrite FAIL fields; re-run.
----------------------------------------------------------------------
```

  GATE: [entry Name]
    PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
    [PASS / FAIL for each]
  STATUS: CLEARED / NOT CLEARED

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Purpose:  Post-gate chain consistency verification. Distinct from
          ENTRY GATE (register) -- confirms four chain elements are
          internally consistent.
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type:

  PBI-Ref mismatch (element 1): replace PBI-Ref with identifier
    matching belief in "What today's materials imply". Belief
    statement is ground truth; do not alter it.

  Handle mismatch (element 2): determine authoritative label
    (HL-[NN] or entry Name), then propagate from source to dependent.
    Do not update both independently.

  Source absent (element 3): replace with resolvable artifact, or
    demote to discard log with typed route reason.

  Verified inaccurate (element 4): re-quote actual text from both
    PBI entry and source. If source unlocatable, apply element 3
    protocol first.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule. Correct before
        proceeding to Pattern of Inherited Errors.
Token:  After all rules ALIGNED:
          RULES-ANCHORED-COMPLETE -- distillation phase closed;
            tier alignment externally confirmed
          RULES-ANCHORED-FAIL: [rule] -- {mismatch description}
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check: "[rule] -> ALIGNED / MISALIGNED" per rule.
Emit: RULES-ANCHORED-COMPLETE or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis: non-derivable from individual corrections.

**Correction Forward Statement:**

1-3 sentences: "Before you build {topic}, the correction record requires you to know that..."

Name the specific failure this artifact prevented. Identify the false assumption the next
team would have inherited and the investigation path it would have misdirected.

Closes two loops:
  1. Confirms EF's NO-ECHO COST (prospective cost claim -> verified outcome at completion).
  2. Makes the artifact's institutional purpose falsifiable (commitment honored or denied).

PASS: "This echo prevented the next team from inheriting [specific assumption], which
would have directed [specific investigation] toward [Y]; signals showed [Z] instead,
and the [specific wrong design] was thereby avoided."
FAIL: advisory framing; summary of findings; avoided-failure absent.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. PBI PRODUCTION PROTOCOL output (BC)
  3. HANDLE LEDGER PROTOCOL output (IA)
  4. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  5. Entry Gate blocks (ENTRY GATE DECLARATION; all STATUS: CLEARED)
  6. Chain Integrity Audit (CHAIN INTEGRITY AUDIT DECLARATION; all CHAIN-COMPLETE)
  7. Resolution Protocol trace (RESOLUTION PROTOCOL DECLARATION; flags resolved)
  8. Rules of Thumb (RULES OF THUMB DECLARATION; RULES-ANCHORED-COMPLETE token)
  9. Surprise hierarchy (ranked with rationale)
  10. Pattern of inherited errors
  11. Blind Spot Map
  12. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  13. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Predicted v8 Scores

| Variation | Axis | C-25 | C-26 | C-27 | Asp | Composite | R8 target |
|-----------|------|------|------|------|-----|-----------|-----------|
| V-01 | Lifecycle | PASS | FAIL | PASS | 18/19 | 180 | RULES-ANCHORED-COMPLETE seeded |
| V-02 | Phrasing reg. | PASS | PASS | PASS | 19/19 | 185 | -- |
| V-03 | Role seq. | PASS | PASS | PASS | 19/19 | 185 | -- |
| V-04 | Lifecycle + role seq. | PASS | PASS | PASS | 19/19 | 185 | RULES-ANCHORED-COMPLETE seeded |
| V-05 | All three axes | PASS | PASS | PASS | 19/19 | 185 | RULES-ANCHORED-COMPLETE seeded |

**V-01** fails C-26 intentionally -- clean single-axis test for the R8 isolated target.

**V-02 and V-03** each target 185 via different axes: if both pass, multiple structural
paths to the new ceiling are confirmed. If one drops below 185, the dropped criterion
identifies which v8 pass condition is more demanding than expected.

**V-04 and V-05** both target 185 + R8 isolated target. Discriminant: V-05 adds formal
block phrasing to V-04; if V-05 scores identically, formal blocks are neutral. If V-05
drops a criterion, the formal block structure interferes with the three-role architecture
in a way that single-axis phrasing (V-02) did not.

---

## RULES-ANCHORED-COMPLETE: the R8 isolated pattern

The pattern mirrors the CHAIN audit's positive-state semantics:

| Chain audit | Distillation | Layer |
|---|---|---|
| C-19: CHAIN-COMPLETE / CHAIN-FLAG tokens | C-20: RULES-ANCHORED check | Positive + flag emission |
| C-22: CHAIN-FLAG gates production | C-23: RULES-ANCHORED gates production | Blocking condition |
| C-25: RESOLUTION PROTOCOL (one repair per flag type) | (no R7 analog; R8 seeds this) | Repair protocol |
| CHAIN-COMPLETE token | RULES-ANCHORED-COMPLETE token | Positive-state closure |

V-01, V-04, and V-05 introduce RULES-ANCHORED-COMPLETE. If the pattern holds under scoring:

- v9 gains C-28: the distillation phase closes with a named positive-state token, making
  the RULES-ANCHORED traceability check auditable from output rather than self-reported.
- The progression across rounds: visibility -> navigability -> primacy -> repairability /
  stakes / verifiability (v8) -> **auditable closure** (v9 candidate).

Each layer converts a verification step from a self-reported declaration into a token-backed
commitment: the reviewer no longer must re-derive whether the check ran -- they read the token.
