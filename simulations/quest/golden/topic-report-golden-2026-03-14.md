# Round 6 Variations — `topic-report`

**Rubric version**: v6 (C-01 through C-22, aspirational_pass/14 * 10)
**Base**: R5 V-04 golden foundation (C-01--C-20, 12/14 under v6)
**New criteria**: C-21 (inertia framing at NEXT STEP), C-22 (explicit THREE-LAYER WRITE POINT header)

## Variation Axes Selected

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| C-21 inertia at NEXT STEP | YES | NO | YES | YES | YES |
| C-22 explicit THREE-LAYER header | NO | YES | YES | YES | YES |
| Inertia propagated to READINESS sentence | NO | NO | YES | NO | YES |
| Branch B own THREE-LAYER header | NO | NO | NO | NO | YES |
| G-9 stall-cost contract label | NO | NO | NO | NO | YES |

**Prediction:**
- V-01: 13/14 (misses C-22)
- V-02: 13/14 (misses C-21)
- V-03: 14/14 -- propagation tests whether broader inertia adds noise or signal
- V-04: 14/14 -- R6 minimal golden
- V-05: 14/14 -- ceiling with Branch B reliability extension

---

## V-01

**Axis**: C-21 inertia framing only
**Hypothesis**: Adding a stall-cost statement to [RULE NEXT-CONCRETE] converts a label into a commitment without requiring an explicit THREE-LAYER header. C-21 in isolation shows whether inertia framing is the primary reliability gain from the R5 ceiling.

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
[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Before writing the readiness sentence, run the G-7 verification scan:
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE NEXT-CONCRETE G-5]: Name the specific skill to run. Generic steps ("gather more signals", "run more scouts") fail G-5.
[RULE NEXT-CONCRETE C-21]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

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

Before writing the READINESS line: run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
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

**Expected score under v6**: 13/14
**Missing**: C-22 (no explicit THREE-LAYER WRITE POINT header at write point)
**Passes**: C-01 through C-21 (all prior + C-21 inertia framing)

---

## V-02

**Axis**: C-22 explicit THREE-LAYER header only
**Hypothesis**: The named recovery point (=== THREE-LAYER WRITE POINT ===) reduces attention-degradation failures at the readiness write step without requiring C-21 inertia framing at NEXT STEP. If live-run variance decreases with the header alone, C-22 is an independent reliability property, not dependent on the full V-05 ceiling.

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
[RULE NEXT-CONCRETE G-5]: Name the specific skill to run. Generic steps ("gather more signals", "run more scouts") fail G-5.
  correct: "Run /scout:feasibility (scout)."
  violation: "Run more scout signals." (no specific skill -- G-5 violation)
Write one sentence: the most critical open signal from BLOCKERS determines the skill.
(fulfills G-5)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

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

Before writing the READINESS line: execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN against the LOCKED BLOCKERS list from Phase 2 (LAYER 2 anchor):
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
+--------------------------------------------------------------+

(fulfills G-6, G-7, G-8)

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v6**: 13/14
**Missing**: C-21 (no stall-cost statement at NEXT STEP; [RULE NEXT-CONCRETE] names the skill but omits "Leaving this open holds the topic at Not Ready.")
**Passes**: C-01 through C-20, C-22

---

## V-03

**Axis**: Inertia propagation -- C-21 + C-22 extended to READINESS sentence level
**Hypothesis**: C-21 requires inertia framing at NEXT STEP. This variation extends the inertia framing upward: the [RULE] governing the readiness sentence also encodes the stall cost of the Not Ready state, making every Not Ready output explicitly communicate its persistence cost. If propagation is noise-free, this is a reliability gain with no rubric cost; if it introduces hallucination of costs, it shows as a C-04 failure in live runs.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4: Readiness statement is a single sentence calibrated to signal counts; states readiness and, if not ready, names the specific blocking signals.
G-5: One concrete next step naming the specific skill to run and the stall cost of deferring it.
G-6: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.

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

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence. The sentence must also communicate that the topic remains blocked until these signals are resolved.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review); topic stays here until both are resolved."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design and omits persistence framing -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review); topic stays here until both are resolved."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout); topic stays here." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}; topic stays here until all are resolved."
(fulfills G-4, G-7)

SLOT 4 -- Recommended next step
[RULE NEXT-CONCRETE G-5]: Name the specific skill to run. Generic steps ("gather more signals", "run more scouts") fail G-5.
[RULE NEXT-CONCRETE C-21]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.
(fulfills G-5)

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

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

Before writing the READINESS line: execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names}; topic holds here until resolved|
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

**Expected score under v6**: 14/14
**New pattern tested**: Inertia framing at READINESS sentence (beyond C-21's NEXT STEP scope)
**Live-run risk**: G-4 calibration may degrade if "topic stays here until all are resolved" introduces phrasing drift; watch for hallucinated persistence costs when BLOCKERS is empty.

---

## V-04

**Axis**: C-21 + C-22 combined -- R6 minimal golden candidate
**Hypothesis**: Adding inertia framing at NEXT STEP AND the explicit THREE-LAYER header to the V-04(R5) minimal golden achieves 14/14 at minimum structural overhead -- no new mechanism beyond the two additions. The contract label chain (G-7a/G-7b), worked examples, LOCK, and scan all carry forward unchanged.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4: Readiness statement is a single sentence calibrated to signal counts.
G-5: One concrete next step naming the specific skill to run and the stall cost of deferring it.
G-6: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.

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
[RULE SLOT1-SOURCE (fulfills G-2)]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE (fulfills G-3)]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN immediately below before writing.
Recovery: If attention has degraded, re-read this header to reconstruct the required layer sequence before proceeding.

[RULE G-7a COMPLETENESS (fulfills G-4, G-7)]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY (fulfills G-4, G-7)]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."

SLOT 4 -- Recommended next step
[RULE NEXT-CONCRETE (fulfills G-5)]: Name the specific skill to run. Generic steps ("gather more signals", "run more scouts") fail G-5.
[RULE NEXT-CONCRETE C-21]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- C-21 violation)
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE G-8 VERIFICATION (fulfills G-6, G-8)]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).
Maximum 40 lines. Maximum 80 characters per line.

Write the compact ASCII card:

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}                    |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

Before writing the READINESS line, execute the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  [RULE G-7a COMPLETENESS SCAN]: confirm each BLOCKERS name appears in the READINESS line.
    correct: line contains "prove/analysis" and "review/design" if both are in BLOCKERS.
    violation: line says "missing prove/analysis" when "review/design" is also in BLOCKERS.
  [RULE G-7b EXCLUSIVITY SCAN]: confirm no name in the READINESS line is absent from BLOCKERS.
    correct: line contains only names present in BLOCKERS.
    violation: line introduces "scout/market" when scout/market is not in BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v6**: 14/14 = 100 -- GOLDEN
**Design note**: Minimal overhead over V-04(R5). C-21 is a one-clause addition to [RULE NEXT-CONCRETE]. C-22 is the === THREE-LAYER WRITE POINT === header block inserted at SLOT 3 entry. No new mechanism; both additions slot into existing contract chain.

---

## V-05

**Axis**: Ceiling -- Branch B own THREE-LAYER header + G-9 stall-cost contract label + inertia propagation
**Hypothesis**: V-04 (R6) places the THREE-LAYER header only in Branch A SLOT 3. If Branch B is the primary live-run failure mode (--format teams is the common call), a second THREE-LAYER recovery point at Branch B Section 3 provides independent attention recovery without cross-branch lookup. G-9 formalizes the stall-cost invariant at the contract register level, making inertia framing chain-traceable the same way G-7a/G-7b chain COMPLETENESS/EXCLUSIVITY.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4: Readiness statement is a single sentence calibrated to signal counts.
G-5: One concrete next step naming the specific skill to run.
G-6: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9: Recommended next step enforces the stall-cost invariant:
  G-9 INERTIA: The next step sentence names both (a) the concrete skill invocation and (b) the readiness consequence of deferring it. A sentence naming only the skill fails G-9.

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
[RULE SLOT1-SOURCE (fulfills G-2)]: Use PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE (fulfills G-3)]: Use PHASE 1 CHECKPOINT values only.
List each open signal with namespace, skill-type, and owner:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by step 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN immediately below before writing.
Recovery: If attention has degraded, re-read this header to reconstruct the required layer sequence before proceeding.

[RULE G-7a COMPLETENESS (fulfills G-4, G-7)]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY (fulfills G-4, G-7)]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):
  G-7a COMPLETENESS SCAN: List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: List each name drafted in the sentence. Confirm each appears in the LOCKED BLOCKERS list from step 2b.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."

SLOT 4 -- Recommended next step
[RULE NEXT-CONCRETE (fulfills G-5)]: Name the specific skill to run. Generic steps ("gather more signals") fail G-5.
[RULE G-9 INERTIA (fulfills G-9)]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (names skill only, no stall cost -- G-9 violation)
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause per G-9.

--- BRANCH B: --format teams ---

[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]

[RULE G-8 VERIFICATION (fulfills G-6, G-8)]: Prohibited characters named by character: backtick (`), less-than (<), greater-than (>).
Backtick count must be zero -- scan every character; any backtick is a G-8 violation.
Angle-bracket count must be zero -- any < or > is a G-8 violation.
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).
Maximum 40 lines. Maximum 80 characters per line.

Section 1 -- Header
+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |

Section 2 -- Progress
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}                    |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |

Section 2b -- Open signals
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |

Section 3 -- Readiness

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the READINESS line.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (frozen by step 2d) is the canonical name set. Do not look up Branch A for this list.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN immediately below before writing.
Recovery: If attention has degraded, re-read this Branch B header to reconstruct the required layer sequence without referencing Branch A.

Before writing the READINESS line, execute the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  [RULE G-7a COMPLETENESS SCAN]: confirm each BLOCKERS name appears in the READINESS line.
    correct: line contains every name from BLOCKERS.
    violation: line omits any BLOCKERS name.
  [RULE G-7b EXCLUSIVITY SCAN]: confirm no name in the READINESS line is absent from BLOCKERS.
    correct: line contains only names present in BLOCKERS.
    violation: line introduces a name not in BLOCKERS.

+--[ READINESS ]-----------------------------------------------+
| Not ready -- missing {names from LOCKED BLOCKERS list}       |

Section 4 -- Next step
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
(fulfills G-1)
```

**Expected score under v6**: 14/14 = 100 -- GOLDEN
**New patterns tested**:
- G-9 contract label for stall-cost invariant: inertia framing is now chain-traceable (register -> [RULE G-9 INERTIA] annotation -> NEXT STEP output) matching the G-7a/G-7b pattern
- Branch B own THREE-LAYER header: independent recovery point for the --format teams path; model in Branch B can re-read the local header without cross-branch lookup
**Live-run prediction**: If Branch B compliance is the primary failure mode in R6 live runs, V-05's Branch B header should show lower variance than V-04's single-header design. If Branch A and Branch B fail at similar rates, the additional header is rubric-neutral (no new criteria) but reliability-positive.

---

## Design Summary

| Variation | C-21 | C-22 | New pattern | Expected score |
|-----------|------|------|-------------|----------------|
| V-01 Inertia only | YES | NO | Stall-cost clause at NEXT STEP; no named recovery header | 13/14 = 99.3 |
| V-02 Header only | NO | YES | THREE-LAYER header at Branch A write point; no inertia | 13/14 = 99.3 |
| V-03 Inertia propagated | YES | YES | Inertia framing at READINESS sentence too; persistence cost in Not Ready output | 14/14 = 100 |
| V-04 Minimal golden | YES | YES | C-21 + C-22 at minimum overhead over V-04(R5) | 14/14 = 100 |
| V-05 Ceiling | YES | YES | G-9 contract label for inertia; Branch B own THREE-LAYER header | 14/14 = 100 |

**Discriminator prediction**: V-01 and V-02 show which R6 criterion is the harder live-run target. V-03 tests whether inertia propagation to READINESS introduces G-04 calibration noise. V-04 and V-05 compete on Branch B reliability.
