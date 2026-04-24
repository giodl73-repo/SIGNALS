# Round 8 Variations -- `topic-report`

**Rubric version**: v8 (C-01 through C-27, aspirational_pass/19 * 10)
**Base**: R7 V-05 ceiling (C-01--C-27, 19/19 under v8)
**Discriminator targets**: R8 discriminator candidates from rubric v8 table (recovery directive, dual-identifier violation, slot-indexed register)

## Variation Axes Selected

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| A: dual-identifier violation | violation text carries both G-9 INERTIA and C-21 simultaneously | YES | NO | NO | YES | YES |
| B: recovery directive in Branch B header | explicit re-read instruction named in Branch B THREE-LAYER header | NO | YES | NO | YES | YES |
| C: slot-indexed contract register | register entries name their governed output slot | NO | NO | YES | NO | YES |

**Neutral base**: R7 V-05 modified to fail all three candidate criteria -- SLOT 4 violation carries only C-21 (no G-9 INERTIA label), Branch B THREE-LAYER header has no recovery directive, register entries carry no slot annotations. Scores 19/19 under v8.

**Predictions (all under v8 current rubric -- candidates not yet scored):**
- V-01: 19/19 = 100.0 -- candidate C-28 YES, C-29 NO, C-30 NO
- V-02: 19/19 = 100.0 -- candidate C-28 NO, C-29 YES, C-30 NO
- V-03: 19/19 = 100.0 -- candidate C-28 NO, C-29 NO, C-30 YES
- V-04: 19/19 = 100.0 -- candidate C-28 YES, C-29 YES, C-30 NO
- V-05: 19/19 = 100.0 -- candidate C-28 YES, C-29 YES, C-30 YES

**Design rationale for neutral base construction:**
The R8 neutral base strips two properties that R7 V-05 carried but that are not captured by any C-01--C-27 pass condition:
1. The recovery directive ("re-read this Branch B header without referencing Branch A") in the Branch B THREE-LAYER header -- C-25 only requires LAYER 1/2/3 enumeration, not a recovery instruction.
2. The G-9 register label in the violation text -- C-23 only requires the rubric criterion ID (C-21) to appear; C-24 only requires the register label to appear in the annotation, not in the violation text itself.
The slot-indexed register (Axis C) is a new mechanism not present in any prior design.

---

## V-01

**Axis**: A -- dual-identifier violation
**Hypothesis**: When the violation example at SLOT 4 carries both the register label (G-9 INERTIA) and the rubric criterion ID (C-21) simultaneously -- `(no stall cost -- G-9 INERTIA / C-21 violation)` -- a model encountering bad output can trace to either the contract register or the rubric without a separate scan. C-23 alone (C-21 only) enables rubric-path recovery; C-24 alone (G-9 at annotation) enables register-path recovery; dual-identifier in the violation text closes both paths from a single point. Isolates whether the violation is the failure-mode entry point or whether the annotation label alone is sufficient.

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

**Expected score under v8**: 19/19 = 100.0
**Candidate criterion satisfied**: C-28 (dual-identifier violation -- G-9 INERTIA and C-21 co-present in violation text)
**Mechanism isolated**: The violation text `(no stall cost -- G-9 INERTIA / C-21 violation)` carries both the register label and the rubric criterion ID at the same position. A model reading the violation knows: (a) G-9 INERTIA is the contract register entry to look up for the full obligation, and (b) C-21 is the rubric criterion governing the failure mode. C-23 alone provides path (b); C-24 alone provides path (a) at the annotation label but not in the violation text. Dual-identifier makes both paths available from the violation entry point without any additional scan.

---

## V-02

**Axis**: B -- recovery directive in Branch B header
**Hypothesis**: C-25 requires the Branch B `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header to enumerate LAYER 1/2/3. This structural requirement closes the cross-branch attention gap. A model executing Branch B can reconstruct the layer sequence from the header. The question is whether adding an explicit recovery instruction -- "re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A" -- reduces live-run layer-omission rate beyond structural self-containment alone. If the recovery directive is the active mechanism (not just the layer enumeration), it is independently verifiable and becomes C-29.

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

**Expected score under v8**: 19/19 = 100.0
**Candidate criterion satisfied**: C-29 (recovery directive in Branch B header -- explicit instruction to re-read without cross-branch reference)
**Mechanism isolated**: C-25 requires LAYER 1/2/3 in Branch B. The recovery directive ("re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A") is an active instruction that names both the recovery action (re-read this header) and the prohibition (without referencing BRANCH A). The directive makes recovery behavior explicit and prescriptive rather than latent. If live-run variance for Branch B decreases with V-02 vs. V-01 (which has LAYER 1/2/3 but no directive), the recovery note is the mechanism that activates the structural guarantee.

---

## V-03

**Axis**: C -- slot-indexed contract register entries
**Hypothesis**: The contract register assigns labels (G-7a, G-7b, G-9 INERTIA) to invariants. C-19 and C-24 chain those labels through annotation and scan headers. But the register itself does not state which output slot each entry governs. A model reading the register must cross-reference the template to find where G-9 INERTIA is enforced. Adding explicit slot annotations to register entries -- `G-9 INERTIA [SLOT 4]: ...` and `G-7a COMPLETENESS [SLOT 3]: ...` -- creates a forward-navigation path from register label to governed output slot without a template scan. This is orthogonal to C-19/C-24 (which chain label from register to annotation) because it addresses navigation direction: register-to-slot rather than annotation-to-register.

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

**Expected score under v8**: 19/19 = 100.0
**Candidate criterion satisfied**: C-30 (slot-indexed contract register -- each entry names its governed output slot as `[SLOT n]` or `[BRANCH B]` or `[PHASE 4]`)
**Mechanism isolated**: The `[SLOT 4]` annotation in `G-9 INERTIA [SLOT 4]` creates a forward-navigation link from the register entry to the output slot it governs. C-19 and C-24 establish a backward-navigation path: annotation label traces back to register. Slot-indexing establishes the forward-navigation complement: register entry directly names the output slot without a template scan. The two directions are structurally independent -- a spec can satisfy C-19/C-24 (backward chain) without slot-indexing, and can slot-index without C-19/C-24 chains. V-03 tests whether forward-navigation from the register reduces attention overhead at register read time.

---

## V-04

**Axes**: A + B -- dual-identifier violation + recovery directive in Branch B header
**Hypothesis**: V-01 (Axis A) makes the violation text the entry point for both register-path and rubric-path recovery. V-02 (Axis B) makes the Branch B header recovery action explicit. Combined, V-04 closes the attention-loss gap at two different failure entry points: a model that produces incorrect output (V-01 path) and a model that loses track of the layer sequence mid-Branch-B execution (V-02 path). The combination is additive if the failure modes are independent -- one is output-driven, one is generation-flow-driven. If they saturate (the same model failures trigger both), V-04 shows no reliability gain over V-01 or V-02 alone.

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

**Expected score under v8**: 19/19 = 100.0
**Candidate criteria satisfied**: C-28 YES, C-29 YES, C-30 NO
**Design note**: V-04 combines the two annotation-level additions (Axis A: dual-identifier violation, Axis B: recovery directive) without touching the register structure. The two mechanisms address orthogonal failure entry points: Axis A helps a model that produces wrong output navigate back to the governing invariant; Axis B helps a model mid-Branch-B generation recover the enforcement sequence. If their failure modes are independent, V-04 should show lower Branch-B error rate than V-01 (which lacks Axis B) and lower NEXT STEP inertia error rate than V-02 (which lacks Axis A).

---

## V-05

**Axes**: A + B + C -- dual-identifier violation + recovery directive + slot-indexed register (ceiling)
**Hypothesis**: V-05 combines all three single-axis mechanisms. Axis A (dual-identifier violation) closes the output-to-invariant recovery gap. Axis B (recovery directive) closes the Branch-B layer-sequence recovery gap. Axis C (slot-indexed register) closes the register-to-slot forward-navigation gap. If all three failure modes are independent, V-05 should show lower error rates than V-04 on register-lookup failures (Axis C). If Axis C is redundant with C-19/C-24 backward chaining (models that already know how to navigate from annotation to register can also navigate forward), V-05 and V-04 score identically in live runs. The comparison V-04 vs. V-05 directly tests whether forward-navigation from the register is an independent reliability property.

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

**Expected score under v8**: 19/19 = 100.0
**Candidate criteria satisfied**: C-28 YES, C-29 YES, C-30 YES
**Design note -- Axis C interaction with C-19/C-24**: C-19 and C-24 establish backward-chaining: `[RULE G-9 INERTIA]` at the annotation traces back to the `G-9 INERTIA` register entry. Slot-indexing (`G-9 INERTIA [SLOT 4]`) establishes forward-navigation: the register entry points forward to SLOT 4. The two are directionally orthogonal. A model reading the register before seeing the template can locate the governed slot without scanning; a model at the annotation can trace back to the register without scanning. V-05 closes both navigation directions at every governed position.
**Design note -- ceiling structure**: V-05 carries all three candidate additions at minimal overhead. Axis A adds three tokens to the violation text. Axis B adds one sentence to the Branch B header. Axis C adds one `[SLOT n]` tag per register entry. No new phases, no new branches, no new structural sections. The candidate ceiling is annotation-level in the same way V-04 R7 was the minimal golden: all additions are text-level edits within existing structural positions.

---

## Design Summary

| Variation | Axis A (dual-ID violation) | Axis B (Branch B recovery note) | Axis C (slot-indexed register) | C-28? | C-29? | C-30? | v8 score |
|-----------|--------------------------|--------------------------------|-------------------------------|-------|-------|-------|---------|
| Neutral base | NO | NO | NO | NO | NO | NO | 19/19 = 100.0 |
| V-01 | YES | NO | NO | YES | NO | NO | 19/19 = 100.0 |
| V-02 | NO | YES | NO | NO | YES | NO | 19/19 = 100.0 |
| V-03 | NO | NO | YES | NO | NO | YES | 19/19 = 100.0 |
| V-04 | YES | YES | NO | YES | YES | NO | 19/19 = 100.0 |
| V-05 Ceiling | YES | YES | YES | YES | YES | YES | 19/19 = 100.0 |

**R8 discriminator note**: All 5 variations score identically under v8 because C-28, C-29, C-30 are not yet rubric criteria. The ordering resolves only under a potential v9 rubric. R8 live runs will test which mechanisms reduce actual failure rates and whether the candidates are independently verifiable.

**Prediction for v9 formula** (if C-28 + C-29 + C-30 added, aspirational_pass/22 * 10):
- Neutral base: 19/22 = 86.4
- V-01: 20/22 = 90.9
- V-02: 20/22 = 90.9
- V-03: 20/22 = 90.9
- V-04: 21/22 = 95.5
- V-05 Ceiling: 22/22 = 100.0
