---

# Round 7 Variations — `topic-report`

**Rubric version**: v7 (C-01 through C-25, aspirational_pass/17 * 10)
**Base**: Neutral base at 14/17 — R6 V-04 with C-23 criterion tag removed from NEXT STEP violation
**New criteria**: C-23 (criterion-tagged violation), C-24 (G-9 register-linked annotation), C-25 (Branch B independent THREE-LAYER header)

## Variation Axes Selected

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| C-23 criterion-tagged violation (names C-21) | YES | NO | NO | YES | YES |
| C-24 G-9 register-linked annotation | NO | YES | NO | YES | YES |
| C-25 Branch B independent THREE-LAYER header | NO | NO | YES | NO | YES |

**Predictions:**
- V-01: 15/17 = 98.8 — C-23 in isolation; control for C-24 and C-25
- V-02: 15/17 = 98.8 — C-24 in isolation; register chain without criterion tag
- V-03: 15/17 = 98.8 — C-25 in isolation; Branch B recovery point without annotation changes
- V-04: 16/17 = 99.4 — C-23 + C-24 combined; R7 minimal golden candidate
- V-05: 17/17 = 100 — ceiling; all three new criteria

---

## V-01

**Axis**: C-23 only — criterion-tagged violation at NEXT STEP
**Hypothesis**: The only change from the 14/17 neutral base is appending the rubric criterion ID to the NEXT STEP violation example: `(no stall cost)` becomes `(no stall cost -- C-21 violation)`. If this single tag reduces stall-cost omission rate in live runs, C-23 is an independently effective mechanism. A model encountering the violation knows which invariant (C-21) is at stake rather than just which output form is wrong. C-24 (no G-9 register entry) and C-25 (no Branch B header) are absent to isolate the C-23 effect.

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
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

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

**Expected score under v7**: 15/17 = 98.8
**Passes**: C-01 through C-22 (all prior), C-23
**Missing**: C-24 (no G-9 register entry; annotation uses `[RULE NEXT-CONCRETE C-21]`, not a register-linked label), C-25 (no Branch B THREE-LAYER header)
**C-23 mechanism**: `[RULE NEXT-CONCRETE C-21]` violation appends `(no stall cost -- C-21 violation)` — the criterion ID C-21 is embedded in the violation text, making the failure mode criterion-recoverable. Contrast: the neutral base says `(no stall cost)` only, naming the output defect but not the invariant.

---

## V-02

**Axis**: C-24 only — G-9 register-linked annotation for single-position invariant
**Hypothesis**: Assigning `G-9 INERTIA` as a named contract register entry and propagating that exact label to the inline `[RULE G-9 INERTIA]` annotation makes the stall-cost invariant chain-traceable at two structural levels (register → annotation) without requiring a scan step. The violation text says `(-- G-9 violation)` not `(-- C-21 violation)` — naming the register label, not the rubric criterion ID — so C-23 is absent and C-24 is isolated. If G-9 register linkage reduces stall-cost omission rate beyond an annotation-local label alone, C-24 is an independent reliability contribution.

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
G-9 INERTIA: The recommended next step names both (a) the concrete skill invocation and (b) the readiness consequence of deferring it. A sentence naming only the skill fails G-9.

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
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause per G-9 INERTIA.

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
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

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

**Expected score under v7**: 15/17 = 98.8
**Passes**: C-01 through C-22 (all prior), C-24
**Missing**: C-23 (violation text says `(-- G-9 violation)` naming the register label, not the rubric criterion ID C-21), C-25 (no Branch B THREE-LAYER header)
**C-24 mechanism**: Contract register contains `G-9 INERTIA: ...`; annotation says `[RULE G-9 INERTIA (fulfills G-9)]` — exact label propagated from register to annotation, two-level chain. Compare V-01: annotation label `[RULE NEXT-CONCRETE C-21]` references a rubric criterion ID directly, which is locally correct but not register-linked, failing C-24.

---

## V-03

**Axis**: C-25 only — Branch B independent THREE-LAYER WRITE POINT header
**Hypothesis**: The BRANCH-SEAL directive prevents Branch B from referencing Branch A's THREE-LAYER WRITE POINT header. A model executing `--format teams` has no local recovery point; if attention degrades at the READINESS section, it must reconstruct the G-7 enforcement sequence from surrounding spec context — a cross-branch lookup. A self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header at Branch B Section 3 enumerates LAYER 1/2/3 independently, so the model never needs to look outside Branch B. C-23 and C-24 are absent to isolate the C-25 effect.

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
  violation: "Run /scout:feasibility (scout)." (no stall cost)
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause.

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
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (frozen by step 2d) is the canonical name set. Do not reference Branch A for this list.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN immediately below before writing.
Recovery: If attention has degraded, re-read this Branch B header to reconstruct the required layer sequence without referencing Branch A.

Before writing the READINESS line, execute the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

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

**Expected score under v7**: 15/17 = 98.8
**Passes**: C-01 through C-22 (all prior), C-25
**Missing**: C-23 (NEXT STEP violation says `(no stall cost)` without criterion tag), C-24 (no G-9 register entry; annotation uses `[RULE NEXT-CONCRETE C-21]`)
**C-25 mechanism**: Branch B Section 3 carries `=== THREE-LAYER WRITE POINT (BRANCH B) ===` with LAYER 1/2/3 enumerated independently of Branch A's header. The `LAYER 2 ANCHOR` explicitly says "Do not reference Branch A for this list." A model in Branch B can re-read the local header and reconstruct the enforcement sequence without any cross-branch lookup. Contrast V-01 and V-02: Branch B carries only the inline scan step, not a named layer header.

---

## V-04

**Axis**: C-23 + C-24 — R7 minimal golden candidate
**Hypothesis**: Combining G-9 INERTIA in the contract register (C-24) with the criterion-tagged violation `(-- C-21 violation)` (C-23) makes the stall-cost invariant independently recoverable at three reference points: (1) the register entry G-9 INERTIA defines the semantic invariant, (2) the `[RULE G-9 INERTIA]` annotation at SLOT 4 links the write point back to the register, (3) the violation text names the rubric criterion ID C-21 so a model seeing a failing output can trace back to the governing rule. C-25 is absent. If V-04 achieves 16/17, it confirms C-23+C-24 are the primary yield additions for R7 and C-25 is the remaining single-criterion discriminator.

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
G-9 INERTIA: The recommended next step names both (a) the concrete skill invocation and (b) the readiness consequence of deferring it. A sentence naming only the skill fails G-9.

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
  violation: "Run /scout:feasibility (scout)." (names skill only, no stall cost -- C-21 violation)
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause per G-9 INERTIA.

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
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

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

**Expected score under v7**: 16/17 = 99.4
**Passes**: C-01 through C-24 (all prior + C-23 + C-24)
**Missing**: C-25 (no Branch B THREE-LAYER header; a model executing `--format teams` must locate Branch A's header across the branch boundary or reconstruct from context)
**Design note**: The `[RULE G-9 INERTIA]` annotation label (register-linked, satisfies C-24) and the `(-- C-21 violation)` criterion tag (rubric ID, satisfies C-23) operate on different reference planes and both fire simultaneously. G-9 is the semantic/contract name; C-21 is the rubric criterion ID. A model encountering a non-compliant NEXT STEP output can trace it back via either path independently.

---

## V-05

**Axis**: C-23 + C-24 + C-25 — ceiling
**Hypothesis**: V-04 plus a self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header in Branch B achieves all three new criteria. The Branch B header provides an independent recovery point for the `--format teams` execution path, closing the only gap V-04 leaves open. With all three new criteria in place: G-9 INERTIA chains register to annotation (C-24), the C-21 criterion tag makes failure criterion-recoverable (C-23), and the Branch B header eliminates cross-branch attention loss on the Teams path (C-25). Expected 17/17 = 100.

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
G-9 INERTIA: The recommended next step names both (a) the concrete skill invocation and (b) the readiness consequence of deferring it. A sentence naming only the skill fails G-9.

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
  violation: "Run /scout:feasibility (scout)." (names skill only, no stall cost -- C-21 violation)
  form: "{skill invocation} ({namespace}). Leaving this open {readiness consequence}."
Write one sentence: the most critical open signal from BLOCKERS determines the skill. Append the stall cost clause per G-9 INERTIA.

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
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (frozen by step 2d) is the canonical name set. Do not reference Branch A for this list.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN immediately below before writing.
Recovery: If attention has degraded, re-read this Branch B header to reconstruct the required layer sequence without referencing Branch A.

Before writing the READINESS line, execute the G-7 scan against the LOCKED BLOCKERS list from Phase 2:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

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

**Expected score under v7**: 17/17 = 100 — GOLDEN
**Passes**: C-01 through C-25 (all criteria)
**New patterns relative to V-04**:
- Branch B own `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header with LAYER 1/2/3 enumerated independently, `LAYER 2 ANCHOR` explicitly says "Do not reference Branch A for this list" — closes the cross-branch attention loss gap that V-04 leaves open on the `--format teams` path
- All other mechanisms carry forward from V-04 unchanged
**Live-run prediction**: If `--format teams` is the higher-frequency call path, V-05 should show lower readiness-line violation rates than V-04. If Branch A and Branch B fail at similar rates, the additional header is rubric-neutral for this round (no R8 criteria yet) but reliability-positive for both paths.

---

## Design Summary

| Variation | C-23 | C-24 | C-25 | New pattern | Predicted score |
|-----------|------|------|------|-------------|-----------------|
| V-01 C-23 only | YES | NO | NO | Criterion ID embedded in violation text; annotation stays `[RULE NEXT-CONCRETE C-21]` | 15/17 = 98.8 |
| V-02 C-24 only | NO | YES | NO | G-9 INERTIA in register; annotation becomes `[RULE G-9 INERTIA]`; violation names G-9 not C-21 | 15/17 = 98.8 |
| V-03 C-25 only | NO | NO | YES | Branch B own THREE-LAYER header; no annotation changes | 15/17 = 98.8 |
| V-04 Minimal golden | YES | YES | NO | G-9 register + `[RULE G-9 INERTIA]` + `(-- C-21 violation)` tag; three reference planes on stall-cost invariant | 16/17 = 99.4 |
| V-05 Ceiling | YES | YES | YES | V-04 + Branch B independent THREE-LAYER header; both execution paths have local recovery | 17/17 = 100 |

**Key discriminator pairs for scoring**:
- C-23 vs C-20: V-01 (tagged) vs neutral base (untagged) — does naming C-21 in violation reduce live omission?
- C-24 vs C-21: V-02 (register-linked) vs V-01 (annotation-local) — does G-9 register chain reduce stall-cost drift?
- C-25 vs C-22: V-03 (Branch B header) vs V-01 (main header only) — does branch-local recovery reduce Teams path failures?
