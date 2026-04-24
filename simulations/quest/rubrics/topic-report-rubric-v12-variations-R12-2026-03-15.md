# Round 12 Variations -- `topic-report`

**Rubric version**: v12 (C-01 through C-45, aspirational_pass/37 * 10)
**Base**: R11 V-04 triple (D+E+F, all C-01--C-45, 37/37 under v12 -- fails candidate C-46, C-47, C-48)
**Discriminator targets**: C-46 (criterion tag on contamination consequence line), C-47 (Branch A format-type-qualified register entries), C-48 (named contamination-format-vector linking C-34 recovery directive to C-41 format-type constraints)

## Variation Axes Selected

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| G: criterion-tagged contamination consequence label (C-46) | Branch A THREE-LAYER WRITE POINT contamination consequence line gains a `[C-40]` tag appended to the label: `SLOT 3 contamination consequence [C-40]:` | YES | NO | YES | YES | NO |
| H: Branch A format-type-qualified register entries (C-47) | CONTRACT REGISTER entries for G-2, G-3, G-4, G-5 (Branch A positions) gain format-type qualifiers: `(markdown table, four columns)`, `(markdown list, one item per signal)`, `(markdown sentence, prose)` | NO | YES | YES | YES | NO |
| I: named contamination format-vector declaration (C-48) | Branch A THREE-LAYER WRITE POINT recovery directive gains an explicit contamination-format-vector line naming the Branch B format-type constraints (from C-41) as the structural contamination mechanism, linking C-34's prohibition to C-41's declared format types | NO | NO | NO | YES | NO |

**Neutral base (V-05)**: R11 V-04 -- satisfies C-01 through C-45 (37/37 under v12). Fails candidate C-46 (contamination consequence line has no criterion tag), C-47 (Branch A register entries for G-2/G-3 have no format-type qualifiers), C-48 (recovery directive names the prohibited action but not the Branch B format-type constraints as the contamination mechanism).

**Axis rationale**:
- Axis G extends C-40 (contamination consequence line) by adding `[C-40]` as a criterion tag. C-40 names the failure mode; C-46 makes that named failure mode criterion-recoverable at the consequence line itself. A model tracing from the consequence text can reach C-40's definition without a rubric search. This is the consequence-line analogue of C-23 (criterion-tagged violation example at `[RULE]` annotations). Requires C-40 as precondition.
- Axis H extends C-41 (Branch B format-type qualifiers) to Branch A register entries. C-41 tells the model the structural format of Branch B output positions at register-read time (planning phase); Axis H symmetrically tells the model the structural format of Branch A output positions at the same time. G-2 (markdown table), G-3 (markdown list) currently carry no format-type annotations -- they tell the model WHAT to write but not WHAT STRUCTURE it requires. Requires C-41 as precondition.
- Axis I targets the C-48 joint property of C-34+C-41. Both are present in the neutral base but only structurally co-present, not linked by name. Axis I adds a contamination-format-vector line that cites the Branch B format-type constraints from C-41 as the specific mechanism by which the contamination prohibition in C-34 fires: the model learns not just "don't cross-reference Branch B" but "the Branch B format-type constraints are what would contaminate your output type if applied at Branch A positions." This converts co-presence into a named joint property. Requires both C-34 and C-41 as preconditions.

**Expected scores under v12 (denominator /37)**:
- V-04 (G+H+I): 37/37 + C-46 + C-47 + C-48 = 40/40* (under v13 if criteria confirmed)
- V-03 (G+H): 37/37 + C-46 + C-47 = 39/40* (fails C-48)
- V-01 (G only): 37/37 + C-46 = 38/40* (fails C-47, C-48)
- V-02 (H only): 37/37 + C-47 = 38/40* (fails C-46, C-48)
- V-05 (neutral): 37/37 (fails C-46, C-47, C-48)

*Denominator expands to /40 only if v13 confirms all three candidates. Under v12 all five score 37/37.

**The V-01 = V-02 tie prediction**: Both gain one new criterion above neutral. If C-46 and C-47 are structurally independent (no composite), V-01 = V-02 at 38/40. Composite candidates: C-46+C-47 = "format-type-qualified register with criterion-tagged contamination consequence" (format-pre-delivery at planning phase + criterion-recoverable consequence at recovery phase = planning-to-recovery traceability closure for format contamination). If this composite scores independently, V-03 gains an additional point and V-01=V-02 pair may tie below V-03 while V-03 ties below V-04.

---

## V-01

**Axis**: G -- criterion-tagged contamination consequence label (C-46)
**Hypothesis**: C-40 requires the Branch A THREE-LAYER WRITE POINT recovery directive to carry a named consequence line that states the specific structural substitution and criterion IDs violated by SLOT 3 contamination. The current neutral base (R11 V-04) provides this: `SLOT 3 contamination consequence: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).` However, the label itself ("SLOT 3 contamination consequence:") is not criterion-tagged -- a model tracing from the consequence line to C-40's rubric definition requires a spec search. Axis G appends `[C-40]` to the label, making the consequence line self-identifying as a C-40 artifact: `SLOT 3 contamination consequence [C-40]:`. This is the consequence-level analogue of C-23 (criterion-tagged violation in `[RULE]` annotations): C-23 makes violation examples criterion-recoverable at the write-point annotation; C-46 makes the contamination consequence criterion-recoverable at the recovery-directive line. The hypothesis: tagging the consequence line with its criterion ID creates a three-level contamination-traceability chain -- (1) register prohibition in G-7/G-9 entries (planning phase), (2) named consequence text (C-40, recovery phase), (3) criterion tag `[C-40]` on the consequence label -- so that a model encountering the consequence line can reach C-40's definition without a spec search, independently of the criterion IDs cited within the consequence text. Key asymmetry from V-02: V-01 lacks Branch A format-type qualifiers on G-2 and G-3 (C-47 absent) -- register entries for progress table and open signals list carry no format-type annotations beyond position labels.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A (markdown paragraph) | NEXT STEP LINE / BRANCH B (two card rows, no markdown)]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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
SLOT 3 contamination consequence [C-40]: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).
Coordination: The branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins per the temporal-role declaration) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA.

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

**Expected score under v12**: 37/37 = 100.0 (same as neutral -- C-46, C-47, C-48 are not yet v12 criteria)
**Candidate criteria satisfied**: C-40, C-41, C-42 (inherited), C-43 through C-45 (inherited), C-46 (criterion tag `[C-40]` on contamination consequence label)
**Candidate criteria absent**: C-47 (G-2/G-3 Branch A entries carry no format-type qualifiers), C-48 (recovery directive names prohibited action but not Branch B format-type constraints as contamination vector)
**Key difference from V-05**: The `SLOT 3 contamination consequence:` label gains `[C-40]` appended: `SLOT 3 contamination consequence [C-40]:`. The consequence text is identical to V-05. The system property: a model encountering the consequence line sees both the consequence text (which names criterion IDs embedded in prose: "C-04", "C-13", "C-16") and the label tag `[C-40]`, making the consequence line itself criterion-recoverable -- a model that traces the label knows it is reading a C-40 artifact, independently of parsing the embedded criterion citations in the prose.

---

## V-02

**Axis**: H -- Branch A format-type-qualified register entries (C-47)
**Hypothesis**: C-41 extends each Branch B register entry with a structural format-type qualifier in parentheses: `(one card row, no markdown)` for the READINESS LINE and `(two card rows, no markdown)` for the NEXT STEP LINE. This tells the model the structural format of Branch B output positions at register-read time (planning phase), before any branch-specific template content is encountered. The current neutral base extends G-7 and G-9 entries for Branch B only; Branch A entries G-2, G-3, G-4, G-5 carry branch-qualified position labels (e.g., `[SLOT 1 / BRANCH A]`) but no format-type annotations. A model reading G-2 at planning time knows it governs SLOT 1 / BRANCH A but does not learn from the register that SLOT 1 requires a markdown table with four columns -- that structural constraint appears only when the model enters Branch A SLOT 1 at write time. Axis H adds format-type qualifiers to G-2, G-3, G-4, and G-5 Branch A register entries, symmetrically extending C-41's Branch B format pre-delivery to the default execution path. The hypothesis: format-type disambiguation at register-read time (planning phase) reduces Branch A format errors that arise from incorrect format assumptions established during pre-dispatch planning -- not from attention degradation at the write point (addressed by C-34's recovery directive) but from format-ambiguity before branch dispatch. Key asymmetry from V-01: V-02 lacks the criterion tag on the contamination consequence line (C-46 absent) -- the `SLOT 3 contamination consequence:` label carries no `[C-40]` tag, so the consequence line is not criterion-recoverable at the label level.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A (markdown table, four columns: Namespace|Total|Complete|Open)]: Progress table covers all namespaces; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A (markdown list, one item per signal)]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A (markdown sentence, prose)]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A (markdown sentence, prose)]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A (markdown paragraph) | NEXT STEP LINE / BRANCH B (two card rows, no markdown)]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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
SLOT 3 contamination consequence: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).
Coordination: The branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins per the temporal-role declaration) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA.

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

**Expected score under v12**: 37/37 = 100.0
**Candidate criteria satisfied**: C-40 through C-45 (inherited), C-47 (G-2/G-3/G-4/G-5 Branch A entries carry format-type qualifiers)
**Candidate criteria absent**: C-46 (contamination consequence label carries no `[C-40]` tag), C-48 (recovery directive does not name Branch B format-type constraints as contamination vector)
**Key differences from V-05**: G-2 gains `(markdown table, four columns: Namespace|Total|Complete|Open)`; G-3 gains `(markdown list, one item per signal)`; G-4 gains `(markdown sentence, prose)`; G-5 gains `(markdown sentence, prose)`. These qualifiers are appended to the existing branch-qualified slot annotations, creating complete format-type pre-delivery for all Branch A positions at register-read time. The system property: a model reading the register before branch dispatch now knows both WHERE it will write (slot annotation, established by C-30/C-35) and IN WHAT STRUCTURAL FORMAT for every Branch A and Branch B position.

---

## V-03

**Axes**: G+H -- criterion-tagged contamination consequence + Branch A format-type qualifiers (C-46 + C-47)
**Hypothesis**: V-01 (Axis G alone) and V-02 (Axis H alone) address independent failure modes at different temporal positions on the execution arc. Axis H (C-47) reduces format-assumption errors at register-read time (planning phase, before branch dispatch): the model learns the structural format of each Branch A output position before it encounters any write-point content. Axis G (C-46) adds criterion-traceability at the recovery-phase consequence line (SLOT 3, recovery point within Branch A): the `[C-40]` tag on the consequence label makes the contamination consequence criterion-recoverable without a spec search. If both failure modes are independent -- as they are for the analogous C-41/C-40 pairing that motivated C-43 -- V-03 should score 37/37 + C-46 + C-47 = 39/40* (under v13 if confirmed), plus candidate composite C-49 (C-46+C-47): format-type-qualified planning phase + criterion-recoverable contamination consequence at recovery phase = a closed format-contamination arc where the planning-phase format map and the recovery-phase consequence tag are independently recoverable from each other's position. Key structural prediction: composite C-49 would require C-46 and C-47 as preconditions and the system property would be "a model that has established format-type expectations at register-read time (C-47) and encounters a criterion-tagged contamination consequence (C-46) can verify at the consequence line that the contamination would violate the format-type expectations established at planning time -- both endpoints of the format-contamination arc are independently criterion-labeled."

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A (markdown table, four columns: Namespace|Total|Complete|Open)]: Progress table covers all namespaces; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A (markdown list, one item per signal)]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A (markdown sentence, prose)]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A (markdown sentence, prose)]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A (markdown paragraph) | NEXT STEP LINE / BRANCH B (two card rows, no markdown)]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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
SLOT 3 contamination consequence [C-40]: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).
Coordination: The branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins per the temporal-role declaration) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA.

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

**Expected score under v12**: 37/37 = 100.0
**Candidate criteria satisfied**: C-40 through C-45 (inherited), C-46 (criterion tag), C-47 (Branch A format-type qualifiers), candidate composite C-49 if confirmed
**Candidate criteria absent**: C-48 (recovery directive does not name Branch B format-type constraints as contamination vector)
**Key difference from V-05**: Both Axes G and H applied. The system properties: (1) format-type qualifiers on all Branch A register entries close the planning-phase format-ambiguity gap for the default path; (2) the `[C-40]` tag on the contamination consequence label makes the consequence criterion-recoverable; (3) together they create a format-contamination arc where both the planning-phase format map (C-47) and the recovery-phase consequence tag (C-46) are independently labeled and criterion-traceable.

---

## V-04

**Axes**: G+H+I -- criterion-tagged contamination consequence + Branch A format-type qualifiers + named contamination format-vector (C-46 + C-47 + C-48)
**Hypothesis**: V-03 (G+H) achieves C-46 and C-47 and their structural coordination without naming the joint property of C-34+C-41. V-04 extends V-03 with Axis I: an explicit contamination-format-vector line in the Branch A THREE-LAYER WRITE POINT recovery directive that names the Branch B format-type constraints (from C-41, established at register-read time) as the specific structural mechanism by which cross-branch contamination produces format-type errors at Branch A positions. C-34 tells the model "don't cross-reference Branch B"; C-41 tells the model "Branch B positions use one card row / two card rows, no markdown"; Axis I tells the model that the contamination prohibited by C-34 is specifically the contamination-by-format-type: applying Branch B's format-type constraints at Branch A positions produces format substitutions that violate G-4, G-7a/G-7b, and G-9 INERTIA. This converts C-34+C-41 from structural co-presence into a named joint property: the recovery prohibition is grounded in the specific format-type declarations from the planning phase. The hypothesis: declaring the contamination format-vector -- naming Branch B's format-type constraints as the contamination mechanism -- creates a three-point arc: (1) planning-phase format-type declarations for Branch B (C-41, CONTRACT REGISTER); (2) recovery-phase prohibition against cross-branch reference (C-34, THREE-LAYER WRITE POINT header); (3) named joint property: "the Branch B format-type constraints are the contamination vector" (C-48, Axis I). This arc is navigable from all three positions without spec search, and the contamination failure mode is criterion-traceable at its source (format-type declaration), its prohibition (recovery directive), and its consequence (C-40 contamination consequence line).

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A (markdown table, four columns: Namespace|Total|Complete|Open)]: Progress table covers all namespaces; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A (markdown list, one item per signal)]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A (markdown sentence, prose)]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A (markdown sentence, prose)]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A (markdown paragraph) | NEXT STEP LINE / BRANCH B (two card rows, no markdown)]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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
Contamination format-vector [C-48]: the Branch B format-type constraints declared in CONTRACT REGISTER (READINESS LINE / BRANCH B: one card row, no markdown; NEXT STEP LINE / BRANCH B: two card rows, no markdown) govern Branch B output positions only; applying these constraints at SLOT 3 / BRANCH A (markdown sentence, prose) or SLOT 4 / BRANCH A (markdown sentence, prose) produces a format-type substitution -- this is the structural mechanism by which cross-branch reference produces contamination. The contamination consequence is named below.
SLOT 3 contamination consequence [C-40]: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).
Coordination: The branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins per the temporal-role declaration) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA.

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

**Expected score under v12**: 37/37 = 100.0
**Candidate criteria satisfied**: C-40 through C-45 (inherited), C-46 (criterion tag on consequence label), C-47 (Branch A format-type qualifiers), C-48 (contamination format-vector naming Branch B format-type constraints as the contamination mechanism), candidate composite C-49 (C-46+C-47) if confirmed
**Candidate criteria absent**: none under R12 candidates
**Key difference from V-03**: The `Contamination format-vector [C-48]:` line is added immediately before the contamination consequence line in the Branch A THREE-LAYER WRITE POINT header. This line explicitly cites the Branch B format-type constraints from CONTRACT REGISTER (one card row / two card rows, no markdown) as the structural contamination mechanism, naming the specific format-type values that would be erroneously applied at Branch A positions if cross-branch reference occurs. The system property created by C-48: the recovery directive's prohibition (C-34) is now grounded in the specific format declarations from the planning phase (C-41), making the joint property of C-34+C-41 structurally declared as a named contamination arc with a `[C-48]` tag for criterion recovery.

---

## V-05

**Axes**: none (neutral base / control)
**Hypothesis**: V-05 is R11 V-04 (D+E+F) verbatim -- unchanged. It satisfies C-01 through C-45 (37/37 under v12) and fails all three R12 candidate axes (C-46 NO: contamination consequence label has no criterion tag; C-47 NO: Branch A entries G-2/G-3 have no format-type qualifiers; C-48 NO: recovery directive does not name Branch B format-type constraints as contamination vector). Its role in R12 is identical to R11 V-05's role in R11: anchor the baseline and verify that the R11 ceiling is stable when re-scored in a new round context. If V-05 fails to score 37/37 under v12 in a live run, the R11 champion is not stable and R12 analysis is invalid; if it scores 37/37, the baseline holds and the candidate axes are independently attributable.

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1 / BRANCH A]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2 / BRANCH A]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3 / BRANCH A]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4 / BRANCH A]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B / ASCII CARD]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B / ASCII CARD]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4 / BRANCH A (markdown paragraph) | NEXT STEP LINE / BRANCH B (two card rows, no markdown)]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

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
SLOT 3 contamination consequence: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).
Coordination: The branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins per the temporal-role declaration) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA.

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

**Expected score under v12**: 37/37 = 100.0 (R11 V-04 unchanged)
**Candidate criteria satisfied**: C-40 through C-45 (all inherited from R11 V-04)
**Candidate criteria absent**: C-46 (contamination consequence label has no `[C-40]` tag), C-47 (G-2/G-3 Branch A entries have no format-type qualifiers), C-48 (recovery directive does not name Branch B format-type constraints as contamination vector)
**Design note**: V-05 is R11 V-04 verbatim. The three candidate axes fail on distinct properties: (1) C-46 fails because the consequence label reads `SLOT 3 contamination consequence:` without `[C-40]` -- the criterion ID appears only in the consequence prose text, not as a label tag; (2) C-47 fails because G-2 and G-3 carry branch-qualified slot annotations but no format-type qualifiers (G-7 and G-9 are exceptions because C-41 specifically extended those entries with Branch B format types); (3) C-48 fails because the recovery directive names the prohibited action ("cross-reference Branch B instructions") but not the specific structural mechanism by which that cross-reference produces contamination -- the Branch B format-type constraints are not named as the contamination vector. These three failure modes are structurally independent: a design can satisfy any subset without the others.

---

## Predicted R12 Ordering Under v13 (if C-46, C-47, C-48 confirmed as criteria)

| Variation | C-46 | C-47 | C-48 | v12 score | v13 score | Notes |
|-----------|------|------|------|-----------|-----------|-------|
| V-04 (G+H+I) | YES | YES | YES | 37/37 | 40/40 | All three confirmed |
| V-03 (G+H) | YES | YES | NO | 37/37 | 39/40 | Fails C-48 |
| V-01 (G only) | YES | NO | NO | 37/37 | 38/40 | Fails C-47, C-48 |
| V-02 (H only) | NO | YES | NO | 37/37 | 38/40 | Fails C-46, C-48 |
| V-05 (neutral) | NO | NO | NO | 37/37 | 37/40 | Baseline |

**V-01=V-02 tie prediction**: Both single-axis variations gain one new criterion above neutral. If C-46 and C-47 are structurally independent (no joint composite C-49), V-01 = V-02 at 38/40 under v13. This would be the R12 analogue of the R10 V-01=V-02 tie and the R11 V-05=V-02 tie. R13 must then find the asymmetric discriminator between C-46 (consequence-level criterion tag, recovery phase) and C-47 (register-level format annotation, planning phase). If composite C-49 (C-46+C-47: format-type-qualified planning phase + criterion-recoverable recovery-phase consequence) scores independently, V-03 gains one additional point above V-01/V-02, breaking the two-way tie at the pairwise level.

**R12 tie-break hypothesis for V-01 vs V-02**: C-46 (criterion tag on consequence label) requires C-40 as precondition and extends a recovery-phase element. C-47 (Branch A format-type qualifiers) requires C-41 as precondition and extends a planning-phase element. If same-phase extensions are more likely to create composites with each other than cross-phase extensions, and if the rubric has more criteria in the recovery-phase region (where most of the enforcement mechanism layers reside), then V-01's C-46 may generate a composite with C-40's existing write-point criteria while V-02's C-47 creates a new composite class (planning-phase format completeness). Whether this asymmetry is scoreable is the live-run question R12 must resolve.
