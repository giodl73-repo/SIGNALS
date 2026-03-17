# Round 9 Variations -- `topic-report`

**Rubric version**: v9 (C-01 through C-30, aspirational_pass/22 * 10)
**Base**: R8 neutral base (C-01--C-27, 19/22 under v9 -- fails C-28, C-29, C-30)
**Discriminator targets**: Pairwise and triple combinations of C-28, C-29, C-30 -- the three R8 single-axis variations tied at 20/22 under v9; their pairwise interactions are the live R9 discriminators.

## Variation Axes Selected

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| A: dual-identifier violation | violation text carries both G-9 INERTIA and C-21 simultaneously | YES | YES | NO | YES | NO |
| B: recovery directive in Branch B header | explicit re-read instruction in Branch B THREE-LAYER header | YES | NO | YES | YES | NO |
| C: slot-indexed contract register | register entries carry `[SLOT n]` / `[PHASE n]` forward indices | NO | YES | YES | YES | NO |

**Neutral base (V-05)**: R8 neutral base -- satisfies C-01 through C-27 (19/22 under v9). Fails C-28 (violation text carries only C-21, no G-9 INERTIA label), C-29 (Branch B THREE-LAYER header has no recovery directive), C-30 (register entries carry no slot annotations).

**Predictions under v9:**
- V-01 (A+B): 21/22 = 99.5 -- C-28 YES, C-29 YES, C-30 NO
- V-02 (A+C): 21/22 = 99.5 -- C-28 YES, C-29 NO, C-30 YES
- V-03 (B+C): 21/22 = 99.5 -- C-28 NO, C-29 YES, C-30 YES
- V-04 (A+B+C): 22/22 = 100.0 -- C-28 YES, C-29 YES, C-30 YES
- V-05 (neutral): 19/22 = 95.5 -- C-28 NO, C-29 NO, C-30 NO

**Design rationale for R9 axis selection:**
R8 produced three single-axis variations (Axis A, Axis B, Axis C) that tied at 20/22 under v9 because C-28, C-29, and C-30 are mutually orthogonal -- no v9 criterion differentiates them. R9 tests whether pairwise combinations score higher than the v9 ceiling (22/22) or expose new candidate criteria. If all three pairwise combinations score 21/22 without differentiation, the finding confirms orthogonality holds at the pairwise level and no candidate C-31 has yet been identified that distinguishes A+C from A+B or B+C. If a live-run error pattern appears only in one pairwise combination, the asymmetry names the candidate. V-04 (ceiling) confirms A+B+C remains at 22/22 and no R9 mechanism has pushed beyond it. V-05 (control) anchors the 19/22 baseline.

---

## V-01

**Axes**: A+B -- dual-identifier violation + recovery directive in Branch B header
**Hypothesis**: R8 V-01 (Axis A alone) and R8 V-02 (Axis B alone) tied at 20/22. V-01 combines them. Axis A closes the output-to-invariant recovery gap: a model that produces incorrect NEXT STEP output reads the violation fragment and reaches both G-9 INERTIA (register path) and C-21 (rubric path) from one text position. Axis B closes the Branch-B layer-sequence recovery gap: a model mid-Branch-B generation that loses track of the enforcement layers encounters an explicit re-read instruction naming the recovery action and the prohibition. The two failure modes are orthogonal -- one is triggered by wrong output, one by generation-flow degradation. If independent, V-01 should score 21/22 (one above single-axis). If a live run shows either axis alone could have closed both failure modes, the combination shows no gain over single-axis.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4: Readiness statement is a single sentence calibrated to signal counts.
G-5: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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

**Expected score under v9**: 21/22 = 99.5
**Candidate criteria satisfied**: C-28 (dual-identifier violation, Axis A), C-29 (recovery directive in Branch B header, Axis B)
**Candidate criterion absent**: C-30 (no slot-indexed register entries)
**Mechanism isolated**: Combines the two annotation-level additions from R8. Axis A addresses a failure mode at output-time: a model generating wrong NEXT STEP output reads the violation fragment and reaches both recovery chains simultaneously without a second scan. Axis B addresses a failure mode at generation-time: a model executing Branch B that loses the enforcement layer sequence encounters an explicit procedural instruction before the enforcement layers, naming both what to do (re-read this header) and what is forbidden (reference Branch A). The failure modes are structurally separated -- Axis A fires at output slots, Axis B fires at branch entry. If live runs confirm independence, V-01 scores above R8 single-axis variations. If Branch B and NEXT STEP errors are correlated (same underlying attention failure), V-01 offers no gain over single-axis.

---

## V-02

**Axes**: A+C -- dual-identifier violation + slot-indexed contract register
**Hypothesis**: R8 V-01 (Axis A alone) and R8 V-03 (Axis C alone) tied at 20/22. V-02 combines them. Axis A anchors the violation text as a dual-entry-point for register-path and rubric-path recovery. Axis C adds forward-navigation from the register: each register entry names its governed output slot so a model reading the register before encountering the template can plan its execution path without a scan. The two mechanisms operate in opposite directions: Axis A lets a model navigate backward from bad output to governing invariants; Axis C lets a model navigate forward from register entries to governed slots. If the two navigation directions address independent failure modes, V-02 scores 21/22. If slot-indexed register entries make the violation text's dual-identifier redundant (a model that can navigate forward from the register already knows where to apply each invariant), the combination shows no gain.

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

**Expected score under v9**: 21/22 = 99.5
**Candidate criteria satisfied**: C-28 (dual-identifier violation, Axis A), C-30 (slot-indexed register, Axis C)
**Candidate criterion absent**: C-29 (no recovery directive in Branch B header)
**Mechanism isolated**: Pairs backward recovery (Axis A: violation text is the dual entry point for register-path and rubric-path navigation) with forward planning (Axis C: register entries name governed slots so execution path is visible at register-read time). These two mechanisms close failure modes at opposite ends of the execution arc: Axis C helps a model plan before writing; Axis A helps a model recover after writing incorrectly. If the failure modes are end-point-independent, V-02 scores 21/22. Key asymmetry from V-01: V-02 lacks the Branch B recovery directive (C-29) but adds slot-indexed register entries (C-30). If Branch B layer-sequence errors are common in live runs and NEXT STEP inertia errors are rare, V-02 will show higher error rates than V-01 despite identical v9 scores -- a finding that would name a candidate C-31.

---

## V-03

**Axes**: B+C -- recovery directive in Branch B header + slot-indexed contract register
**Hypothesis**: R8 V-02 (Axis B alone) and R8 V-03 (Axis C alone) tied at 20/22. V-03 combines them. Axis B provides a procedural recovery instruction at Branch B entry before the enforcement layers. Axis C provides forward-navigation from register entries to governed slots at execution start. Both operate early in the generation arc: Axis C at register-read time (before any output slot is reached), Axis B at branch-entry time (before the enforcement layer sequence in Branch B). If both early-arc mechanisms independently reduce generation errors, V-03 should score 21/22. Key asymmetry from V-01 and V-02: V-03 lacks the dual-identifier violation (C-28 absent). A model that produces incorrect NEXT STEP output has no compound fragment to recover from -- only the annotation label and criterion tag at their respective positions. If the dual-identifier is the primary recovery mechanism for NEXT STEP errors, V-03 will show higher SLOT 4 error rates than V-01 or V-02 despite identical v9 scores.

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
  violation: "Run /scout:feasibility (scout)." (no stall cost -- C-21 violation)
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

**Expected score under v9**: 21/22 = 99.5
**Candidate criteria satisfied**: C-29 (recovery directive in Branch B header, Axis B), C-30 (slot-indexed register, Axis C)
**Candidate criterion absent**: C-28 (violation text carries only C-21, no G-9 INERTIA label)
**Mechanism isolated**: Pairs two early-arc mechanisms: Axis C positions obligations before the template (register-to-slot forward navigation at execution start) and Axis B positions a recovery procedure before the Branch B enforcement layers (generation-flow recovery at branch entry). Both reduce error probability before a wrong output is produced, rather than after. Key asymmetry from V-01: SLOT 4 violation text carries only `(no stall cost -- C-21 violation)` -- the G-9 INERTIA register label is absent from the violation fragment. If a model produces incorrect NEXT STEP output in a live run, the recovery path requires two hops: violation text -> C-21 -> rubric criterion definition -> register lookup. V-01 collapses that to one hop via the dual-identifier. If V-03 shows higher SLOT 4 error rates than V-01 in live runs at identical v9 scores, the asymmetry surfaces a candidate C-31: violation-text single-hop vs. two-hop recovery distinguishability.

---

## V-04

**Axes**: A+B+C -- all three (ceiling)
**Hypothesis**: V-04 combines all three R9 axes. Axis A (dual-identifier violation) closes the output-to-invariant recovery gap at SLOT 4. Axis B (recovery directive in Branch B header) closes the layer-sequence recovery gap at Branch B entry. Axis C (slot-indexed register) closes the register-to-slot forward-navigation gap at execution start. All three mechanisms are confirmed orthogonal by R8 finding. V-04 should score 22/22 = 100.0 under v9, matching R8 V-05. The comparison is V-04 vs. the three pairwise combinations (V-01, V-02, V-03): if all three pairwise combinations score 21/22 and V-04 scores 22/22, the one-criterion gap is confirmed as C-30 (V-01 lacks C-30), C-29 (V-02 lacks C-29), or C-28 (V-03 lacks C-28) respectively. V-04 also functions as a ceiling re-verification: confirming R8 V-05's 22/22 score is stable under identical prompt text.

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

**Expected score under v9**: 22/22 = 100.0
**Candidate criteria satisfied**: C-28 (dual-identifier violation), C-29 (recovery directive in Branch B header), C-30 (slot-indexed register)
**Candidate criterion absent**: none -- this is the ceiling
**Design note**: V-04 is structurally identical to R8 V-05. Its role in R9 is threefold: (1) confirm the 22/22 ceiling is stable when the same prompt text is re-scored under v9; (2) provide a comparison point against the three pairwise combinations -- each pairwise variation should score exactly one criterion below V-04 (V-01 lacks C-30, V-02 lacks C-29, V-03 lacks C-28); (3) anchor the ceiling for any candidate C-31 that emerges from live-run asymmetries. If a live run reveals a failure mode that appears in V-01 or V-02 but not V-03, or in V-03 but not V-01, the asymmetry names the candidate and V-04 tests whether the combination already closes it. The ceiling design carries all three at minimal text overhead: Axis A adds a compound fragment to one violation example; Axis B adds one sentence to the Branch B header; Axis C adds one `[SLOT n]` or `[PHASE n]` tag per register entry. No structural additions beyond existing positions.

---

## V-05

**Axes**: none (neutral base / control)
**Hypothesis**: V-05 is the R8 neutral base, scoring 19/22 under v9. It satisfies C-01 through C-27 and fails C-28, C-29, and C-30. Its role is to anchor the baseline and confirm that the R9 pairwise combinations each add exactly two criteria above it. If a pairwise combination (V-01, V-02, or V-03) scores only 20/22 instead of 21/22, the second criterion in that pair is not independently verifiable and the hypothesis of orthogonality for that pair is falsified. V-05 provides the reference gap: any variation scoring higher has added recoverable criteria; any variation scoring the same as V-05 has candidate additions that do not pass independently.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4: Readiness statement is a single sentence calibrated to signal counts.
G-5: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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
  violation: "Run /scout:feasibility (scout)." (no stall cost -- C-21 violation)
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

**Expected score under v9**: 19/22 = 95.5
**Candidate criteria satisfied**: none (C-28 NO, C-29 NO, C-30 NO)
**Candidate criteria absent**: C-28 (violation text carries only C-21, no G-9 INERTIA label), C-29 (Branch B THREE-LAYER header has no recovery directive), C-30 (register entries carry no slot annotations)
**Design note**: This is the R8 neutral base, unchanged. The SLOT 4 violation text carries `(no stall cost -- C-21 violation)` -- single identifier, rubric-path only. The Branch B THREE-LAYER header enumerates LAYER 1/2/3 (satisfying C-25) but carries no recovery instruction (C-29 absent). The CONTRACT REGISTER has no slot-index annotations (C-30 absent). Scores 19/22 under v9 because C-01 through C-27 pass and C-28, C-29, C-30 fail. Functions as the R9 control: if any pairwise combination fails to score above 19/22, the failing candidate criterion is not independently verifiable.

---

## Score Summary

| Variation | C-28 | C-29 | C-30 | v9 asp | v9 score | Gap from ceiling |
|-----------|------|------|------|--------|---------|-----------------|
| V-01 (A+B) | YES | YES | NO | 21/22 | **99.5** | -0.5 (C-30) |
| V-02 (A+C) | YES | NO | YES | 21/22 | **99.5** | -0.5 (C-29) |
| V-03 (B+C) | NO | YES | YES | 21/22 | **99.5** | -0.5 (C-28) |
| V-04 (A+B+C) | YES | YES | YES | 22/22 | **100.0** | -- |
| V-05 (neutral) | NO | NO | NO | 19/22 | **95.5** | -4.5 |

**R9 discriminator structure**: If predictions hold, V-01 = V-02 = V-03 = 99.5. No v9 criterion differentiates the three pairwise combinations from each other because C-28, C-29, and C-30 are mutually orthogonal. The pairwise combinations are distinguishable only by live-run error rates -- not by rubric score. A finding that one pairwise combination shows higher live-run error rates despite identical rubric scores is the signal that names a candidate C-31.

**Candidate C-31 prediction paths**:
- If V-02 shows higher Branch-B READINESS errors than V-01: C-29 (recovery directive) is doing work that C-30 alone cannot substitute -- candidate: "single-arc recovery mechanism at Branch B entry is not substitutable by register-level forward indexing."
- If V-03 shows higher SLOT 4 inertia errors than V-01 or V-02: C-28 (dual-identifier) is the primary recovery mechanism for NEXT STEP errors -- candidate: "violation-text dual-identifier reduces SLOT 4 error rate independent of register forward-navigation."
- If all three pairwise combinations show identical live-run error rates: no C-31 candidate is surfaced; R9 confirms that pairwise combinations are not live-run distinguishable and the rubric has reached its current ceiling.
