# topic-plan Scorecard — Round 9 (Commitment-Phase Track) (2026-03-15)

Rubric: v9 (C-01–C-32, max composite 114)
New criteria: C-30 (Skill Execution Contract), C-31 (Phases execute against declared contract),
C-32 (Enforcement reproduction linked to contract declaration)
Golden threshold: >= 80

---

## Scoring Summary

| Variation | Axis | Essential | Rec | Asp | Composite | Golden |
|-----------|------|-----------|-----|-----|-----------|--------|
| V-01 | Lifecycle emphasis — phase headers carry contract ref | 5/5 | 3/3 | 23/24 | **113** | Yes |
| V-02 | Output format — numbered section registry (§1–§5) | 5/5 | 3/3 | 23/24 | **113** | Yes |
| V-03 | Phrasing register — "Authority: SEC §..." in phase headers | 5/5 | 3/3 | 23/24 | **113** | Yes |
| V-04 | Role sequence + inertia — null hypothesis as first contract term | 5/5 | 3/3 | 23/24 | **113** | Yes |
| V-05 | Full combination — maximum attribution depth + conflict audit | 5/5 | 3/3 | 24/24 | **114** | Yes |

**Top score: V-05 at 114/114 (ceiling)**
All essential criteria pass across all variations.

---

## Per-Criterion Scores

### Essential (all must pass; any failure caps composite at ≤ 72)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Read strategy.md | PASS | PASS | PASS | PASS | PASS |
| C-02 | Signal inventory | PASS | PASS | PASS | PASS | PASS |
| C-03 | Delta detection | PASS | PASS | PASS | PASS | PASS |
| C-04 | Typed change proposals | PASS | PASS | PASS | PASS | PASS |
| C-05 | Confirmation gate | PASS | PASS | PASS | PASS | PASS |

Evidence: Phase 1 reads strategy.md and records STRATEGY DATE. Phase 3 assesses all 9
namespaces with NEW/PRIOR classification. Phase 5 (Proposals) uses typed Schema F rows
(ADD/REMOVE/REPRIORITIZE). Phase 6 is a named confirmation gate with PENDING CONFIRMATION
block; strategy.md is not modified until user replies.

### Recommended (2/3 needed alongside all essential to reach golden threshold)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Evidence citation | PASS | PASS | PASS | PASS | PASS |
| C-07 | Before/after diff | PASS | PASS | PASS | PASS | PASS |
| C-08 | Inertia justification | PASS | PASS | PASS | PASS | PASS |

Evidence: Schema F has Evidence artifact column (C-06); before/after diff table at Phase 5
exit (C-07); "DEFAULT OUTCOME: NO CHANGE — burden of proof rests on change" in contract
header + "vs. NO CHANGE" column in every proposal row (C-08).

### Aspirational (denominator /24)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Type-labeled null declarations | PASS | PASS | PASS | PASS | PASS | Typed null declarations block (ADDITIONS/REMOVALS/REPRIORITIZATIONS) in Phase 5, each with labeled inertia note |
| C-10 | Conflict detection | FAIL | FAIL | FAIL | FAIL | PASS | V-01–V-04 have delta detection only; V-05 adds explicit conflict audit table before Phase 5 with null declared when empty |
| C-11 | Phase-gated lifecycle | PASS | PASS | PASS | PASS | PASS | Named phases with [PHASE N EXIT: PASS/STOP] gates throughout |
| C-12 | Pre-scan commitment | PASS | PASS | PASS | PASS | PASS | Phase 1 locks Schema A before Phase 3 signal inventory |
| C-13 | Commitment reference integrity | PASS | PASS | PASS | PASS | PASS | SEALED BLOCK re-read prohibition; Before values sourced from Schema A |
| C-14 | Self-documenting gate conditions | PASS | PASS | PASS | PASS | PASS | GC-1 and GC-2 name specific conditions checked before emitting PASS |
| C-15 | Temporal boundary attestation | PASS | PASS | PASS | PASS | PASS | "Commitment table complete. No signal artifacts read yet." in SEALED BLOCK temporal attestation |
| C-16 | Verbatim strategy.md quotation | PASS | PASS | PASS | PASS | PASS | VERBATIM BLOCK template with === delimiters and exact quoted sentence |
| C-17 | Per-namespace quantified inventory | PASS | PASS | PASS | PASS | PASS | Phase 3: "[total] total | [new] new" for all 9 namespaces |
| C-18 | Re-read prohibition marker | PASS | PASS | PASS | PASS | PASS | SEALED BLOCK "Re-read prohibition:" labeled field |
| C-19 | Source-anchored verbatim quotation | PASS | PASS | PASS | PASS | PASS | "Source dimension: D-N" labeled field in VERBATIM BLOCK |
| C-20 | Change-pressure proposal filter | PASS | PASS | PASS | PASS | PASS | HIGH-PRESSURE namespaces listed in Phase 3; PROPOSAL SCOPE restricts Phase 5 to them |
| C-21 | SEAL violation as named output category | PASS | PASS | PASS | PASS | PASS | "SEAL violation: A Before value containing text not present in Schema A at seal time is a SEAL violation and must be dropped." |
| C-22 | SCOPE violation as named output category | PASS | PASS | PASS | PASS | PASS | "A proposal row citing any excluded namespace is a SCOPE violation and must be dropped." in PROPOSAL SCOPE |
| C-23 | Source enforcement note | PASS | PASS | PASS | PASS | PASS | "Enforcement note: A Source dimension field that does not match a D-N label fails this block." |
| C-24 | Commitment-phase compound gate | PASS | PASS | PASS | PASS | PASS | GC-1 has Check [1] Schema A, Check [2] VERBATIM BLOCK, Check [3] SEALED BLOCK as separate named lines |
| C-25 | Gate 1 audits enforcement note as named sub-requirement | PASS | PASS | PASS | PASS | PASS | Check [2c]: "Enforcement note present as named, labeled sub-field" |
| C-26 | PROPOSAL SCOPE reproduced at Phase 5 enforcement point | PASS | PASS | PASS | PASS | PASS | SCOPE ENFORCEMENT RULE in Skill Execution Contract mandates reproduction at proposal sub-step; Phase 5 reproduces the full three-line block |
| C-27 | Scope gate audits violation condition presence | PASS | PASS | PASS | PASS | PASS | GC-2: "Check: PROPOSAL SCOPE violation condition present as named output category / Result: PASS / STOP" |
| C-28 | Enforcement note as labeled template field | PASS | PASS | PASS | PASS | PASS | "Enforcement note: ..." is a named labeled field in VERBATIM BLOCK template, parallel to "Source dimension:" |
| C-29 | Gate sub-requirements use identifier labels | PASS | PASS | PASS | PASS | PASS | [2a] delimiters / [2b] Source dimension / [2c] Enforcement note — each carries its own alphanumeric label in both the contract gate chain and Phase 2 execution |
| C-30 | Skill Execution Contract | PASS | PASS | PASS | PASS | PASS | Named "SKILL EXECUTION CONTRACT" block before Phase 1 pre-declares all templates (VERBATIM BLOCK, SEALED BLOCK, PROPOSAL SCOPE), all constraint rules (SCOPE ENFORCEMENT RULE, SEAL violation, re-read prohibition), and PHASE SEQUENCE + GATE CHAIN |
| C-31 | Phases execute against declared contract | PASS | PASS | PASS | PASS | PASS | V-01: "(per Skill Execution Contract)" in every phase header; V-02: "per §N" section IDs; V-03: "Authority: Skill Execution Contract §..." field; V-04: "per contract null hypothesis" referencing the declared contract term; V-05: full authority tokens |
| C-32 | Enforcement reproduction linked to contract declaration | PASS | PASS | PASS | PASS | PASS | All five: PROPOSAL SCOPE reproduced at Phase 5 sub-step with explicit attribution "(reproduced from Skill Execution Contract)" per the SCOPE ENFORCEMENT RULE |

---

## Fail Analysis

### C-10 (Conflict Detection) — persistent gap across V-01 through V-04

**Why it fails**: Delta detection (Phase 4 / Phase 7 in earlier tracks) applies a two-condition
novelty gate per finding: is the artifact NEW, and is the finding absent from strategy.md? This
identifies new-to-strategy information but does not compare NEW artifacts against each other.
If artifact A says "prioritize namespace X" and artifact B says "deprioritize namespace X", both
are NEW, both pass delta detection, and both generate proposals — but no gate asks whether they
contradict each other before either enters Phase 5.

**V-05 fix**: An explicit conflict audit phase is inserted between delta detection and proposals,
producing a table of same-dimension conflicts across NEW artifacts. The table is required even
when empty (null declared: "Conflict audit: no cross-artifact contradictions found"). This closes
the gap: a reader verifying the proposal table can check whether contradicting signals were
identified before the proposal was written.

**Failure mode C-10 enables**: Without conflict detection, two contradictory NEW artifacts can
each generate a proposal for the same dimension. The confirmation gate (C-05) then presents both
proposals to the user without surfacing the contradiction. The user must detect the conflict
manually, which is the work the skill was supposed to do.

---

## Variation Analysis

### V-01 — Lifecycle Emphasis (113)

**Primary mechanism**: Gate Chain IDs (GC-1, GC-2) in the Skill Execution Contract. Each gate
is declared as a named entry in the Gate Chain; Phase 2 runs "per Gate Chain entry GC-1." This
creates a typed reference: the phase names an ID, the contract defines that ID, and a reader can
match them directly. Contract authority is demonstrated by structural parallelism — every phase
header echoes the contract's phase list; every gate invokes a declared gate chain entry.

**C-31 note**: Phase headers carry "(per Skill Execution Contract)" as a consistent annotation.
Gate chain IDs provide an additional layer: phase invokes GC-1, contract declares GC-1 — the
reference is bidirectional.

**Gap**: No conflict detection phase. Score: 113.

### V-02 — Output Format (113)

**Primary mechanism**: Section registry (§1–§5). The Skill Execution Contract is organized as
numbered sections; phases cite "per §3 VERBATIM BLOCK" or equivalent. Citations are terse
(§ID rather than "Skill Execution Contract") and independently resolvable. The section structure
also pre-declares Schema F as a numbered template, making slot-filling the default operation.

**C-31 note**: "per §3" satisfies C-31's "as declared in contract §VERBATIM BLOCK" example.
Each §ID is a reference to the contract by section, not by free text.

**Gap**: No conflict detection phase. Score: 113.

### V-03 — Phrasing Register (113)

**Primary mechanism**: "Authority: Skill Execution Contract §..." as a labeled header field
in every phase. The authority declaration is a first-class labeled element of each phase's
structure, not a parenthetical. A reader scanning only labeled fields can confirm every phase
names its authority.

**C-31 note**: The "Authority:" field is structurally analogous to C-28's "Enforcement note:"
field — both promote an assertion from inline prose to a named, labeled output element. The
parallel design makes C-31 compliance as visible as C-28 compliance.

**Gap**: No conflict detection phase. Score: 113.

### V-04 — Role Sequence + Inertia (113)

**Primary mechanism**: Null hypothesis as first contract term. The Skill Execution Contract
opens with: "NULL HYPOTHESIS: strategy.md is correct and should not change. Every proposal
is a claim that the null hypothesis is wrong about something." This makes DEFAULT OUTCOME
the first declared element of the contract — not a footnote. Phases reference "per contract
null hypothesis," grounding inertia justification (C-08) and typed null declarations (C-09)
in the contract's opening premise.

**C-31 note**: "per contract null hypothesis" references the contract via a specific declared
term. The "e.g." in C-31's definition allows references to specific contract elements rather
than requiring the full name at every invocation.

**C-09 note**: The null hypothesis framing produces natural typed null declarations: each
change type whose null hypothesis holds produces "ADDITIONS: none — null hypothesis held for
all ADD candidates."

**Gap**: No conflict detection phase. Score: 113.

### V-05 — Full Combination (114 — CEILING)

**Primary mechanism**: All four axes combined plus conflict audit. Section registry (§1–§5)
from V-02; authority tokens from V-03 ("Authority: Skill Execution Contract §..."); null
hypothesis as first contract term from V-04; maximum attribution depth — every phase cites
both §ID and name; conflict audit phase between delta detection and proposals.

**C-10 pass mechanism**: After Phase 4 (delta detection), an explicit Conflict Audit phase
produces a table of cross-artifact contradictions. The table is required even when empty:
"Conflict audit: no cross-artifact contradictions found on any dimension." Proposals in Phase 5
may not proceed until the conflict audit gate shows PASS.

**C-32 note**: V-05's PROPOSAL SCOPE reproduction at Phase 5 reads:
"PROPOSAL SCOPE (reproduced from Skill Execution Contract §5)" — attributing both by name
and by §ID, making the canonical source doubly addressable.

**Score: 114/114 — first ceiling reached in the Commitment-Phase Track.**

---

## Excellence Signals (V-05)

Three patterns from V-05 that are candidates for R10 criteria:

**1. Conflict audit null declaration**
V-05 produces "Conflict audit: no cross-artifact contradictions found" even when no conflicts
exist. This matches the pattern of C-09 (typed null declarations for proposals) and C-27
(gate that confirms violation condition presence). A null-declared conflict audit is
independently verifiable; its absence is visible as an omission. Candidate R10 criterion:
"Conflict audit null explicitly declared when no contradictions found — parallel to typed
null declarations for change types."

**2. Double-anchored attribution (§ID + name)**
V-05's "(reproduced from Skill Execution Contract §5)" attributes the reproduction to both the
contract by name AND the specific section by ID. This makes the canonical source doubly
addressable: by human reading (name) and by automated matching (§ID). The §ID creates a
checkable equality: does the reproduced block match §5 in the contract? Candidate R10
criterion: "Contract-attributed reproduction includes §ID in addition to contract name, making
the match independently verifiable by section."

**3. Phase authorization index in contract**
V-05's contract includes a table mapping each §ID to the phases authorized to execute it:
§3 VERBATIM BLOCK → authorized in Phase 1, verified in Phase 2. A phase using a contract
template not authorized for it is structurally detectable. Candidate R10 criterion: "Skill
Execution Contract declares an authorization index mapping each template to the phases
permitted to execute it."

---

## Round Result

**R9 closes the C-32 gap** identified at the end of R8: PROPOSAL SCOPE reproduced at Phase 5
now carries "(reproduced from Skill Execution Contract)" attribution, closing the
declare → reproduce → attribute-back chain. All five variations achieve this.

**V-05 closes the C-10 gap** that has persisted since Round 1 of this track: explicit conflict
audit before proposals, null-declared when empty, with a named gate.

**R10 target**: The three V-05 excellence signals above are candidates for new criteria.
The strongest one is the conflict audit null declaration — it completes the C-10 enforcement
loop the same way C-09 completed the proposal-type loop: declare, produce, null-declare when
absent.

---

## Score Table (v9 formula: 60 + rec×10 + asp)

| Variation | Essential | Rec | Asp | Score | Golden |
|-----------|-----------|-----|-----|-------|--------|
| V-01 | 5/5 | 3/3 | 23/24 | 113 | Yes |
| V-02 | 5/5 | 3/3 | 23/24 | 113 | Yes |
| V-03 | 5/5 | 3/3 | 23/24 | 113 | Yes |
| V-04 | 5/5 | 3/3 | 23/24 | 113 | Yes |
| V-05 | 5/5 | 3/3 | 24/24 | **114** | Yes |

**Top variation: V-05 (114)**
**All essential pass: YES**
**Golden threshold met: ALL FIVE**
