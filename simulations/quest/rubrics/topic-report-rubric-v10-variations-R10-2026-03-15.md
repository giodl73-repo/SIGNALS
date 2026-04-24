# Round 10 Variations -- `topic-report`

**Rubric version**: v10 (C-01 through C-33, aspirational_pass/25 * 10)
**Base**: R9 V-04 triple (C-01--C-33, 25/25 under v10 -- fails candidate C-34, C-35)
**Discriminator targets**: C-34 (main-branch recovery directive) and C-35 (branch-qualified slot indexing) -- two asymmetric properties that break the R9 pairwise tie (V-01 = V-02 = V-03 = 22/25 = 98.8 under v10, each satisfying exactly one of C-31, C-32, C-33).

## Variation Axes Selected

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| A: main-branch recovery directive (C-34) | Branch A THREE-LAYER WRITE POINT header names BRANCH A, states recovery action + prohibited alternative, cross-references CONTRACT REGISTER by label | YES | NO | YES | YES | NO |
| B: branch-qualified slot indexing (C-35) | CONTRACT REGISTER slot annotations carry branch qualifier: `[SLOT n / BRANCH A]` and dual mapping for branch-applicable entries | NO | YES | YES | YES | NO |
| C: explicit temporal coordination (C-36 candidate) | Branch A THREE-LAYER header names the planning-to-recovery temporal property: C-35 map established before write point; C-34 fires against that map at write point | NO | NO | NO | YES | NO |

**Neutral base (V-05)**: R9 V-04 triple -- satisfies C-01 through C-33 (25/25 under v10). Fails candidate C-34 (Branch A header has generic recovery line, no BRANCH A name, no register cross-reference), C-35 (register slot annotations are unqualified: `[SLOT 3]` not `[SLOT 3 / BRANCH A]`), C-36 (no temporal coordination statement).

**Predictions under v10 (before v11 criteria added):**
- All variations score 25/25 = 100.0 under v10 (C-34, C-35, C-36 are not yet rubric criteria)
- Predictions under v11 (with C-34, C-35, C-36 added, formula `asp/28 * 10`):
  - V-01 (A): 26/28 = 99.3 -- C-34 YES, C-35 NO, C-36 NO
  - V-02 (B): 26/28 = 99.3 -- C-34 NO, C-35 YES, C-36 NO
  - V-03 (A+B): 27/28 = 99.6 -- C-34 YES, C-35 YES, C-36 NO (pairwise composite not yet scored -- C-36 requires explicit coordination statement)
  - V-04 (A+B+C): 28/28 = 100.0 -- C-34 YES, C-35 YES, C-36 YES
  - V-05 (neutral): 25/28 = 98.2 -- C-34 NO, C-35 NO, C-36 NO

**Design rationale for R10 axis selection:**

C-34 and C-35 are asymmetric over the R9 pairwise variations because:
- C-35 (branch-qualified slot indexing) extends C-30 (Axis C in R9). A prompt without C-30 cannot satisfy C-35 by definition. R9 V-01 (axes A+B, no C-30) cannot satisfy C-35 even if C-35 were added to a re-scoring.
- C-34 (main-branch recovery directive) does not require C-30. It is independent of the slot indexing mechanism; a prompt with C-34 but no C-30 can still satisfy C-34.

This asymmetry creates a dependency edge that breaks R9 pairwise symmetry under v11:
- R9 V-01 (A+B, satisfies C-31): can gain C-34 but not C-35 in R10 -- gap = 1 criterion under v11
- R9 V-02 (A+C, satisfies C-32): can gain both C-34 and C-35 in R10 -- gap = 0 under v11 (if both added)
- R9 V-03 (B+C, satisfies C-33): can gain both C-34 and C-35 in R10 -- gap = 0 under v11 (if both added)

C-36 is the pairwise composite of C-34 + C-35, analogous to C-33 (C-29 + C-30) for Branch B:
- C-33 coordinated C-30 (slot map at register read) with C-29 (recovery at Branch B entry)
- C-36 coordinates C-35 (branch-qualified slot map at register read) with C-34 (recovery at Branch A write point)
- The temporal property: C-35 is established during PHASE 1 / CONTRACT REGISTER reading (planning phase); C-34 fires at the Branch A SLOT 3 write point (recovery phase). Together they create a planning-to-recovery chain for Branch A parallel to C-33's chain for Branch B.

---

## V-01

**Axis**: A -- main-branch recovery directive (C-34)
**Hypothesis**: The Branch A THREE-LAYER WRITE POINT header currently carries a generic recovery line: "If attention has degraded, re-read this header." This line fails at attention-recovery because it does not name the header as BRANCH A (a model in Branch A cannot distinguish this header from a hypothetical Branch B header using the instruction alone), does not name the prohibited alternative (referencing Branch B instructions), and does not cross-reference the CONTRACT REGISTER by label (recovery requires a spec-level search to find the governing invariant names). C-34 converts this generic line into an explicit named recovery directive modeled on C-29's contribution to Branch B: it names the header as BRANCH A, names the recovery action (re-read this BRANCH A header), names the prohibited alternative (do not cross-reference Branch B), and provides a register cross-reference by label (G-7a COMPLETENESS, G-7b EXCLUSIVITY govern SLOT 3; G-9 INERTIA governs SLOT 4). The hypothesis: C-34 closes the same attention-degradation failure mode for Branch A that C-29 closed for Branch B. If C-34 independently reduces Branch A SLOT 3 write errors in live runs, the criterion is real. Key asymmetry from V-02: V-01 lacks branch-qualified slot indices (C-35 absent) -- the CONTRACT REGISTER still uses `[SLOT 3]` without branch annotation. A model reading the register before encountering the write point has an unqualified forward map; C-34's recovery directive at the write point must stand alone without a branch-qualified planning phase behind it.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

=== PHASE 1: DISCOVER ===

Glob simulations/**/{topic}-* to discover all signal artifacts.
Parse namespace and skill-type from each filename: {topic}-{namespace}-{skill-type}-{date}.md
Cross-reference simulations/TOPICS.md for planned signals.
Build coverage table: for each namespace, count Total planned, Complete (artifact exists), Open (planned, no artifact).

CHECKPOINT: Store coverage table and open signal list. These values are frozen. Do not recount in later phases.

=== PHASE 2: PRE-COMPUTATION ===

Step 2a: List all namespaces with Open > 0.

Step 2b: From open signals, identify ESSENTIAL blocking signals.
Emit a BLOCKERS block:
  BLOCKERS:
    - {namespace}/{skill-type}
    - {namespace}/{skill-type}
  If no open essential signals: BLOCKERS: none

Step 2c: Apply G-7 invariants as named guarantee conditions:
  G-7a COMPLETENESS guarantee: Every name emitted in the BLOCKERS block above must appear in the readiness sentence at SLOT 3.
  G-7b EXCLUSIVITY guarantee: The readiness sentence at SLOT 3 must not introduce any name absent from the BLOCKERS block above.

Step 2d: LOCK
  The BLOCKERS list from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase.

=== PHASE 3: WRITE ===

[BRANCH DISPATCH]
If --format teams is present in arguments: execute BRANCH B only.
Otherwise: execute BRANCH A only.

[RULE BRANCH-SEAL]: The branches are sealed. Execute exactly one branch. Do not reference the other branch's format descriptions when executing.

--- BRANCH A: DEFAULT REPORT ---

SLOT 1 -- Progress table
[RULE SLOT1-SOURCE]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |
(fulfills G-2)

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}
(fulfills G-3)

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT (BRANCH A) ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN before writing.
Recovery: re-read this BRANCH A header to reconstruct the required layer sequence. Prohibited: cross-reference Branch B instructions from this path. If governing invariants are not immediately recoverable, navigate to CONTRACT REGISTER: G-7a COMPLETENESS and G-7b EXCLUSIVITY govern this slot; G-9 INERTIA governs SLOT 4.

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE G-9 INERTIA]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- G-9 INERTIA / C-21 violation)
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5, G-9)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE BRANCH-SEAL-B]: This branch is sealed. Do not reference Branch A format descriptions when executing.

[RULE G-8 VERIFICATION]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).

Write a compact ASCII card. Four sections. Maximum 40 lines. Maximum 80 characters per line.

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}  {status}          |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- COMPLETENESS and EXCLUSIVITY invariants govern the READINESS line in the card.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set for Branch B.
LAYER 3 VERIFY   -- Execute COMPLETENESS SCAN and EXCLUSIVITY SCAN before writing the READINESS line.
Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.

Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

(fulfills G-6, G-7, G-8)

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v10**: 25/25 = 100.0
**Candidate criteria satisfied**: C-34 (Branch A THREE-LAYER header named BRANCH A, recovery directive names action + prohibited alternative + register cross-reference)
**Candidate criterion absent**: C-35 (CONTRACT REGISTER slot annotations unqualified -- `[SLOT 3]` not `[SLOT 3 / BRANCH A]`), C-36 (no explicit temporal coordination statement)
**Key difference from V-05**: The `=== THREE-LAYER WRITE POINT ===` header is renamed `=== THREE-LAYER WRITE POINT (BRANCH A) ===` and its recovery line changes from a generic "re-read this header" to a named directive that states the recovery action, names the prohibited alternative (cross-reference Branch B), and names the register labels for the governed slots. This closes the failure mode C-29 closes for Branch B: a model entering Branch A with depleted attention encounters an explicit procedural instruction rather than a generic recovery suggestion.

---

## V-02

**Axis**: B -- branch-qualified slot indexing (C-35)
**Hypothesis**: The CONTRACT REGISTER currently uses C-30 slot annotations: `G-7a COMPLETENESS [SLOT 3]`, `G-9 INERTIA [SLOT 4]`. These annotations establish forward navigation from register to output slot, but the slot numbers are unqualified: "SLOT 3" refers to Branch A's readiness slot, but the register does not say so. Branch B has an equivalent output position (the READINESS LINE in the ASCII card) that has no slot number -- it is rendered inside the card structure, not as a numbered output slot. When a model reads the CONTRACT REGISTER before branch dispatch, it builds a slot map that is Branch A-specific without knowing it. A model that encounters Branch B may attempt to map `[SLOT 3]` to the Branch B READINESS LINE and find no numbered slot, creating a forward-navigation failure that C-35 prevents. Branch-qualifying the slot annotations -- `[SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]` -- makes each register entry's branch scope explicit at read time, before any branch-specific context is encountered. Hypothesis: C-35 reduces Branch B READINESS compliance failures that arise not from attention degradation (covered by C-29) but from incorrect forward-map construction during register reading. Key asymmetry from V-01: V-02 lacks the Branch A named recovery directive (C-34 absent) -- the Branch A THREE-LAYER header retains the generic recovery line. A model executing Branch A that loses enforcement context has no register-cross-referenced recovery path; it must re-read the header and search the spec for the governing labels.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A | NEXT STEP LINE / BRANCH B]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

=== PHASE 1: DISCOVER ===

Glob simulations/**/{topic}-* to discover all signal artifacts.
Parse namespace and skill-type from each filename: {topic}-{namespace}-{skill-type}-{date}.md
Cross-reference simulations/TOPICS.md for planned signals.
Build coverage table: for each namespace, count Total planned, Complete (artifact exists), Open (planned, no artifact).

CHECKPOINT: Store coverage table and open signal list. These values are frozen. Do not recount in later phases.

=== PHASE 2: PRE-COMPUTATION ===

Step 2a: List all namespaces with Open > 0.

Step 2b: From open signals, identify ESSENTIAL blocking signals.
Emit a BLOCKERS block:
  BLOCKERS:
    - {namespace}/{skill-type}
    - {namespace}/{skill-type}
  If no open essential signals: BLOCKERS: none

Step 2c: Apply G-7 invariants as named guarantee conditions:
  G-7a COMPLETENESS guarantee: Every name emitted in the BLOCKERS block above must appear in the readiness sentence at SLOT 3 / BRANCH A (or READINESS LINE / BRANCH B).
  G-7b EXCLUSIVITY guarantee: The readiness output must not introduce any name absent from the BLOCKERS block above.

Step 2d: LOCK
  The BLOCKERS list from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase.

=== PHASE 3: WRITE ===

[BRANCH DISPATCH]
If --format teams is present in arguments: execute BRANCH B only.
Otherwise: execute BRANCH A only.

[RULE BRANCH-SEAL]: The branches are sealed. Execute exactly one branch. Do not reference the other branch's format descriptions when executing.

--- BRANCH A: DEFAULT REPORT ---

SLOT 1 -- Progress table
[RULE SLOT1-SOURCE]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |
(fulfills G-2)

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}
(fulfills G-3)

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN before writing.
Recovery: If attention has degraded, re-read this header to reconstruct the required layer sequence before proceeding.

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE G-9 INERTIA]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- G-9 INERTIA / C-21 violation)
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5, G-9)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE BRANCH-SEAL-B]: This branch is sealed. Do not reference Branch A format descriptions when executing.

[RULE G-8 VERIFICATION]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).

Write a compact ASCII card. Four sections. Maximum 40 lines. Maximum 80 characters per line.

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}  {status}          |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- COMPLETENESS and EXCLUSIVITY invariants govern the READINESS line in the card.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set for Branch B.
LAYER 3 VERIFY   -- Execute COMPLETENESS SCAN and EXCLUSIVITY SCAN before writing the READINESS line.
Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.

Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

(fulfills G-6, G-7, G-8)

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v10**: 25/25 = 100.0
**Candidate criteria satisfied**: C-35 (CONTRACT REGISTER slot annotations carry branch qualifier: `[SLOT n / BRANCH A]` and dual mapping for G-7, G-9 -- `[SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]`, `[SLOT 4 / BRANCH A | NEXT STEP LINE / BRANCH B]`)
**Candidate criterion absent**: C-34 (Branch A THREE-LAYER header uses generic recovery line, not a named BRANCH A directive), C-36 (no temporal coordination statement)
**Key difference from V-05**: Every CONTRACT REGISTER entry that governs a template output slot carries a branch qualifier. Entries exclusive to Branch A carry `[SLOT n / BRANCH A]`. Entries that govern equivalent positions in both branches carry the dual mapping: `[SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]`. This makes the forward-navigation map branch-disambiguated at register-read time: a model reading the register before branch dispatch knows exactly which output position each register entry governs, in both branches, without encountering any branch-specific context first.

---

## V-03

**Axes**: A+B -- main-branch recovery directive + branch-qualified slot indexing (C-34 + C-35)
**Hypothesis**: V-01 (Axis A alone) and V-02 (Axis B alone) address independent failure points on the Branch A execution arc. Axis B (C-35) reduces forward-map ambiguity at register-read time (planning phase, before branch dispatch). Axis A (C-34) reduces attention-degradation errors at the Branch A SLOT 3 write point (recovery phase, mid-execution). If both failure points are independent -- as they were for the analogous C-29/C-30 pairing -- V-03 should score 27/28 under v11 (missing C-36, the explicit temporal coordination composite). Key structural prediction: V-03 achieves C-36's underlying coordination property (register establishes branch-qualified plan before Branch A write; recovery directive fires at the write point) without naming it. Whether the rubric scores this as C-36 YES or NO determines if an explicit coordination statement is a distinct scoring criterion or just a documentation note. If V-03 scores 28/28 = 100.0 under v11 (C-36 YES), C-36 is not a distinguishable criterion from C-34 + C-35. If V-03 scores 27/28 (C-36 NO), C-36 requires an explicit coordination statement and V-04 is the minimal design satisfying it.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A | NEXT STEP LINE / BRANCH B]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

=== PHASE 1: DISCOVER ===

Glob simulations/**/{topic}-* to discover all signal artifacts.
Parse namespace and skill-type from each filename: {topic}-{namespace}-{skill-type}-{date}.md
Cross-reference simulations/TOPICS.md for planned signals.
Build coverage table: for each namespace, count Total planned, Complete (artifact exists), Open (planned, no artifact).

CHECKPOINT: Store coverage table and open signal list. These values are frozen. Do not recount in later phases.

=== PHASE 2: PRE-COMPUTATION ===

Step 2a: List all namespaces with Open > 0.

Step 2b: From open signals, identify ESSENTIAL blocking signals.
Emit a BLOCKERS block:
  BLOCKERS:
    - {namespace}/{skill-type}
    - {namespace}/{skill-type}
  If no open essential signals: BLOCKERS: none

Step 2c: Apply G-7 invariants as named guarantee conditions:
  G-7a COMPLETENESS guarantee: Every name emitted in the BLOCKERS block above must appear in the readiness sentence at SLOT 3 / BRANCH A (or READINESS LINE / BRANCH B).
  G-7b EXCLUSIVITY guarantee: The readiness output must not introduce any name absent from the BLOCKERS block above.

Step 2d: LOCK
  The BLOCKERS list from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase.

=== PHASE 3: WRITE ===

[BRANCH DISPATCH]
If --format teams is present in arguments: execute BRANCH B only.
Otherwise: execute BRANCH A only.

[RULE BRANCH-SEAL]: The branches are sealed. Execute exactly one branch. Do not reference the other branch's format descriptions when executing.

--- BRANCH A: DEFAULT REPORT ---

SLOT 1 -- Progress table
[RULE SLOT1-SOURCE]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |
(fulfills G-2)

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}
(fulfills G-3)

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT (BRANCH A) ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN before writing.
Recovery: re-read this BRANCH A header to reconstruct the required layer sequence. Prohibited: cross-reference Branch B instructions from this path. If governing invariants are not immediately recoverable, navigate to CONTRACT REGISTER: G-7a COMPLETENESS and G-7b EXCLUSIVITY govern this slot; G-9 INERTIA governs SLOT 4.

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE G-9 INERTIA]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- G-9 INERTIA / C-21 violation)
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5, G-9)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE BRANCH-SEAL-B]: This branch is sealed. Do not reference Branch A format descriptions when executing.

[RULE G-8 VERIFICATION]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).

Write a compact ASCII card. Four sections. Maximum 40 lines. Maximum 80 characters per line.

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}  {status}          |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- COMPLETENESS and EXCLUSIVITY invariants govern the READINESS line in the card.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set for Branch B.
LAYER 3 VERIFY   -- Execute COMPLETENESS SCAN and EXCLUSIVITY SCAN before writing the READINESS line.
Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.

Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

(fulfills G-6, G-7, G-8)

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v10**: 25/25 = 100.0
**Candidate criteria satisfied**: C-34 (Branch A named recovery directive), C-35 (branch-qualified slot indices)
**Candidate criterion absent**: C-36 (no explicit temporal coordination statement -- the coordination is structural but unnamed)
**Mechanism**: Pairs C-35's planning-phase contribution (branch-qualified forward map established at register read, before any branch is entered) with C-34's recovery-phase contribution (named recovery directive fires at Branch A SLOT 3 write point against the pre-established map). The temporal coordination property exists structurally but is not explicitly named in the prompt -- analogous to how R9 V-03 (B+C) carried C-33's temporal coordination structurally before C-33 was a named criterion. Whether C-36 scores YES on V-03 determines if explicit naming is required for the criterion.

---

## V-04

**Axes**: A+B+C -- main-branch recovery directive + branch-qualified slot indexing + explicit temporal coordination statement (C-34 + C-35 + C-36 candidate)
**Hypothesis**: V-03 (A+B) carries C-34 and C-35 and achieves their coordination structurally without naming it. V-04 extends V-03 with an explicit temporal coordination statement in the Branch A THREE-LAYER WRITE POINT header that names the planning-to-recovery property: "The branch-qualified slot annotations in CONTRACT REGISTER (established at execution start, planning phase) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence; SLOT 4 / BRANCH A = next step." This converts the implicit C-33-analog into a named invariant, exactly as C-33 converted the implicit B+C structural coordination into a scored property in R9. If V-03 scores C-36 YES (coordination scored structurally), V-04 adds no rubric points but demonstrates that explicit naming is redundant -- and the temporal coordination statement is merely documentation overhead. If V-03 scores C-36 NO, V-04 is the minimal design satisfying C-36 and becomes the R10 ceiling. The V-04 design is identical to V-03 in all structural positions; the single addition is the Coordination line in the Branch A THREE-LAYER WRITE POINT header.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A | NEXT STEP LINE / BRANCH B]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

=== PHASE 1: DISCOVER ===

Glob simulations/**/{topic}-* to discover all signal artifacts.
Parse namespace and skill-type from each filename: {topic}-{namespace}-{skill-type}-{date}.md
Cross-reference simulations/TOPICS.md for planned signals.
Build coverage table: for each namespace, count Total planned, Complete (artifact exists), Open (planned, no artifact).

CHECKPOINT: Store coverage table and open signal list. These values are frozen. Do not recount in later phases.

=== PHASE 2: PRE-COMPUTATION ===

Step 2a: List all namespaces with Open > 0.

Step 2b: From open signals, identify ESSENTIAL blocking signals.
Emit a BLOCKERS block:
  BLOCKERS:
    - {namespace}/{skill-type}
    - {namespace}/{skill-type}
  If no open essential signals: BLOCKERS: none

Step 2c: Apply G-7 invariants as named guarantee conditions:
  G-7a COMPLETENESS guarantee: Every name emitted in the BLOCKERS block above must appear in the readiness sentence at SLOT 3 / BRANCH A (or READINESS LINE / BRANCH B).
  G-7b EXCLUSIVITY guarantee: The readiness output must not introduce any name absent from the BLOCKERS block above.

Step 2d: LOCK
  The BLOCKERS list from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase.

=== PHASE 3: WRITE ===

[BRANCH DISPATCH]
If --format teams is present in arguments: execute BRANCH B only.
Otherwise: execute BRANCH A only.

[RULE BRANCH-SEAL]: The branches are sealed. Execute exactly one branch. Do not reference the other branch's format descriptions when executing.

--- BRANCH A: DEFAULT REPORT ---

SLOT 1 -- Progress table
[RULE SLOT1-SOURCE]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |
(fulfills G-2)

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}
(fulfills G-3)

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT (BRANCH A) ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN before writing.
Recovery: re-read this BRANCH A header to reconstruct the required layer sequence. Prohibited: cross-reference Branch B instructions from this path. If governing invariants are not immediately recoverable, navigate to CONTRACT REGISTER: G-7a COMPLETENESS and G-7b EXCLUSIVITY govern this slot; G-9 INERTIA governs SLOT 4.
Coordination: The branch-qualified slot annotations in CONTRACT REGISTER ([SLOT 3 / BRANCH A], [SLOT 4 / BRANCH A]) were established at execution start (planning phase). This recovery directive fires at the Branch A write point against that pre-established map (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA.

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE G-9 INERTIA]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- G-9 INERTIA / C-21 violation)
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5, G-9)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE BRANCH-SEAL-B]: This branch is sealed. Do not reference Branch A format descriptions when executing.

[RULE G-8 VERIFICATION]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).

Write a compact ASCII card. Four sections. Maximum 40 lines. Maximum 80 characters per line.

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}  {status}          |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- COMPLETENESS and EXCLUSIVITY invariants govern the READINESS line in the card.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set for Branch B.
LAYER 3 VERIFY   -- Execute COMPLETENESS SCAN and EXCLUSIVITY SCAN before writing the READINESS line.
Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.

Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

(fulfills G-6, G-7, G-8)

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v10**: 25/25 = 100.0
**Candidate criteria satisfied**: C-34, C-35, C-36 (explicit temporal coordination statement names planning-phase slot map + recovery-phase directive, converting the implicit structural property of V-03 into a named invariant)
**Candidate criterion absent**: none under the three R10 candidates
**Design note**: V-04 is structurally identical to V-03 in every position except the Coordination line appended to the Branch A THREE-LAYER WRITE POINT header. This line does four things: (1) names C-35's contribution as the planning phase -- branch-qualified slot map established at execution start; (2) names C-34's contribution as the recovery phase -- directive fires at the Branch A write point; (3) makes the temporal sequence explicit -- planning before recovery, in that order; (4) names the governed slots at recovery time, so a model reading the Coordination line can reconstruct the full recovery path without searching any other position. The Coordination line is the only text addition required to distinguish V-04 from V-03 on a structural scoring criterion. If the criterion C-36 is defined as "explicit temporal coordination statement naming planning phase and recovery phase at the Branch A write point," V-04 is the minimal satisfying design. If C-36 is defined as "structural coordination of C-35 and C-34 without requiring explicit naming," V-03 already satisfies it and V-04 is redundant. The V-03/V-04 scoring split resolves this definitional question.

---

## V-05

**Axes**: none (neutral base / control)
**Hypothesis**: V-05 is the R9 V-04 triple, unchanged. It satisfies C-01 through C-33 (25/25 under v10) and fails candidate C-34, C-35, and C-36. Its role in R10 is to anchor the baseline: every variation scoring above V-05 under v11 has added a recoverable criterion; any variation scoring the same as V-05 has additions that do not pass independently. V-05 also re-verifies the R9 V-04 ceiling is stable under v10: confirming 25/25 holds when the same prompt text is re-scored in a new round context.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

=== PHASE 1: DISCOVER ===

Glob simulations/**/{topic}-* to discover all signal artifacts.
Parse namespace and skill-type from each filename: {topic}-{namespace}-{skill-type}-{date}.md
Cross-reference simulations/TOPICS.md for planned signals.
Build coverage table: for each namespace, count Total planned, Complete (artifact exists), Open (planned, no artifact).

CHECKPOINT: Store coverage table and open signal list. These values are frozen. Do not recount in later phases.

=== PHASE 2: PRE-COMPUTATION ===

Step 2a: List all namespaces with Open > 0.

Step 2b: From open signals, identify ESSENTIAL blocking signals.
Emit a BLOCKERS block:
  BLOCKERS:
    - {namespace}/{skill-type}
    - {namespace}/{skill-type}
  If no open essential signals: BLOCKERS: none

Step 2c: Apply G-7 invariants as named guarantee conditions:
  G-7a COMPLETENESS guarantee: Every name emitted in the BLOCKERS block above must appear in the readiness sentence at SLOT 3.
  G-7b EXCLUSIVITY guarantee: The readiness sentence at SLOT 3 must not introduce any name absent from the BLOCKERS block above.

Step 2d: LOCK
  The BLOCKERS list from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase.

=== PHASE 3: WRITE ===

[BRANCH DISPATCH]
If --format teams is present in arguments: execute BRANCH B only.
Otherwise: execute BRANCH A only.

[RULE BRANCH-SEAL]: The branches are sealed. Execute exactly one branch. Do not reference the other branch's format descriptions when executing.

--- BRANCH A: DEFAULT REPORT ---

SLOT 1 -- Progress table
[RULE SLOT1-SOURCE]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |
(fulfills G-2)

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}
(fulfills G-3)

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN before writing.
Recovery: If attention has degraded, re-read this header to reconstruct the required layer sequence before proceeding.

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE G-9 INERTIA]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- G-9 INERTIA / C-21 violation)
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5, G-9)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE BRANCH-SEAL-B]: This branch is sealed. Do not reference Branch A format descriptions when executing.

[RULE G-8 VERIFICATION]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).

Write a compact ASCII card. Four sections. Maximum 40 lines. Maximum 80 characters per line.

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}  {status}          |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- COMPLETENESS and EXCLUSIVITY invariants govern the READINESS line in the card.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set for Branch B.
LAYER 3 VERIFY   -- Execute COMPLETENESS SCAN and EXCLUSIVITY SCAN before writing the READINESS line.
Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.

Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

(fulfills G-6, G-7, G-8)

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v10**: 25/25 = 100.0
**Candidate criteria satisfied**: none (C-34 NO, C-35 NO, C-36 NO)
**Candidate criteria absent**:
- C-34: Branch A THREE-LAYER WRITE POINT has generic recovery line ("re-read this header") -- not named BRANCH A, no prohibited alternative named, no register cross-reference by label
- C-35: CONTRACT REGISTER slot annotations are unqualified -- `[SLOT 3]`, `[SLOT 4]`, not `[SLOT 3 / BRANCH A]`; no Branch B output position mapped in the register
- C-36: No temporal coordination statement at any position

**Design note**: V-05 is R9 V-04 verbatim. The Branch A recovery line fails C-34 on three sub-properties: (1) does not name the header as BRANCH A; (2) does not name the prohibited alternative; (3) does not cross-reference the register by label. The register entries fail C-35 because `[SLOT 3]` is branch-unqualified -- a model reading this register before branch dispatch builds a Branch A-specific slot map without knowing it is Branch A-specific. These are the two failure modes R10 targets. V-05 functions as the control: if any variation fails to score above 25/28 under v11, the candidate criterion added by that variation is not independently verifiable.

---

## Score Summary

| Variation | C-34 | C-35 | C-36 | v10 asp | v10 score | v11 predicted asp | v11 predicted score |
|-----------|------|------|------|---------|-----------|-------------------|---------------------|
| V-01 (A) | YES | NO | NO | 25/25 | **100.0** | 26/28 | **99.3** |
| V-02 (B) | NO | YES | NO | 25/25 | **100.0** | 26/28 | **99.3** |
| V-03 (A+B) | YES | YES | NO* | 25/25 | **100.0** | 27/28 | **99.6** |
| V-04 (A+B+C) | YES | YES | YES | 25/25 | **100.0** | 28/28 | **100.0** |
| V-05 (neutral) | NO | NO | NO | 25/25 | **100.0** | 25/28 | **98.2** |

*C-36 for V-03 is annotated NO (structural property present but no explicit coordination statement) -- this is the live-run question. If the rubric scores C-36 structurally, V-03 scores 28/28 and V-04 is redundant. If the rubric requires explicit naming, V-03 scores 27/28 and V-04 is the minimal ceiling.

**R10 discriminator structure**: Under v10, all five variations score 25/25 = 100.0 (C-34, C-35, C-36 are not yet criteria). The discriminator structure only activates under v11. Once v11 adds C-34, C-35, C-36, the predicted ordering is V-04 (100.0) >= V-03 (99.6) > V-01 = V-02 (99.3) > V-05 (98.2). The V-03/V-04 split resolves the C-36 definitional question; the V-01 = V-02 tie is expected (C-34 and C-35 are orthogonal single-axis additions with no asymmetry between them at the single-axis level).

**Candidate C-37 prediction paths for R11**:
- If V-03 and V-04 show identical live-run error rates despite V-04 carrying the explicit Coordination line: explicit temporal coordination naming adds no measurable reliability gain over structural co-presence -- C-36 is not a real criterion and R11 should target a different property.
- If V-01 shows higher Branch A SLOT 3 errors than V-02 despite identical v11 scores: the forward-map ambiguity (C-35 absent in V-01) creates more generation errors than the missing recovery directive (C-34 absent in V-02). Asymmetric error rates at identical rubric scores name a candidate C-37: "planning-phase slot map dominates recovery-phase directive for Branch A reliability."
- If V-02 shows higher Branch A write errors than V-01: the recovery directive (C-34) is the primary reliability mechanism; the forward map (C-35) is secondary. Candidate C-37: "recovery directive is the binding constraint for Branch A SLOT 3 compliance."
