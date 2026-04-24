# Round 11 Variations -- `topic-report`

**Rubric version**: v11 (C-01 through C-39, aspirational_pass/31 * 10)
**Base**: R10 V-04 triple (C-01--C-39, 31/31 under v11 -- fails candidate C-40, C-41, C-42)
**Discriminator targets**: C-40 (criterion-tagged SLOT 3 contamination consequence at Branch A recovery directive) and C-41 (structural format-type annotations in Branch B dual-mapped register entries) -- two asymmetric properties targeting the R10 single-axis tie (V-01 = V-02 = 26/31 = 98.4 under v11, each satisfying exactly one of C-34 or C-35 without C-36).

## Variation Axes Selected

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| D: criterion-tagged SLOT 3 contamination consequence (C-40) | Branch A THREE-LAYER WRITE POINT recovery directive adds a SLOT 3 contamination consequence line: names the criterion IDs violated if Branch B card template is applied at this position | YES | NO | YES | YES | NO |
| E: structural format-type annotations in Branch B register entries (C-41) | CONTRACT REGISTER dual-mapped entries carry format-type qualifiers for Branch B positions: `(one card row, no markdown)` and `(two card rows, no markdown)` | NO | YES | YES | YES | NO |
| F: temporal-role declaration on CONTRACT REGISTER header (C-42) | CONTRACT REGISTER section header carries explicit temporal-role annotation naming it as the planning-phase artifact: `[TEMPORAL ROLE: planning phase -- read before branch dispatch]` | NO | NO | NO | YES | NO |

**Neutral base (V-05)**: R10 V-04 triple -- satisfies C-01 through C-39 (31/31 under v11). Fails candidate C-40 (recovery directive has no contamination-consequence line), C-41 (register Branch B entries have no format-type qualifiers), C-42 (register header has no temporal-role annotation).

**Predictions under v11 (before v12 criteria added):**
- All variations score their R10 base score under v11 (C-40, C-41, C-42 are not yet criteria):
  - V-01 (D): 26/31 = 98.4 (R10 V-01 base, C-34 only)
  - V-02 (E): 26/31 = 98.4 (R10 V-02 base, C-35 only)
  - V-03 (D+E): 28/31 = 99.0 (R10 V-03 base, C-34+C-35)
  - V-04 (D+E+F): 31/31 = 100.0 (R10 V-04 base, C-34+C-35+C-36)
  - V-05 (neutral): 31/31 = 100.0 (R10 V-04 unchanged)

**Design rationale for R11 axis selection:**

Axis D (C-40) and Axis E (C-41) are asymmetric over the R10 single-axis designs:
- Axis D extends C-34 (Branch A recovery directive) by adding a criterion-tagged contamination consequence at the write point. A model encountering the recovery directive now learns not just the recovery procedure but what specific criteria would be violated if contamination occurs. This property requires C-34 as a precondition; a design without a recovery directive at the Branch A write point cannot embed a contamination consequence there.
- Axis E extends C-35 (branch-qualified slot indexing) by annotating the Branch B output positions with structural format types. A model reading the register before branch dispatch now knows the structural format of the Branch B output position -- not just its name (`READINESS LINE / BRANCH B`) but its format constraint (`one card row, no markdown`). This property requires C-35 as a precondition; a design without branch-qualified dual-mapped entries cannot extend those entries with format types.

The tie-breaking hypothesis: Axis D creates a natural composite C-43 with C-16 (in-render verification scan) because both C-40 and C-16 address the same write-point (SLOT 3 / BRANCH A) at adjacent temporal positions: the contamination consequence fires at the recovery directive (before any enforcement layer), and the scan executes immediately before writing. Their conjunction creates a SLOT 3 double-gate: contamination warning → scan → write, covering both the cross-branch contamination failure mode (C-40) and the list-integrity failure mode (C-16) at the same position. Axis E's natural composite C-44 pairs C-41 with C-25 (Branch B independent header): format-type-qualified register entries (planning phase) + Branch B self-contained recovery header (recovery phase) = a format-type-consistent Branch B recovery arc. Whether C-43 (same-position double-gate) and C-44 (temporal-coordination arc) are symmetric composites is a live-run question. If same-position double-gate is a structurally stronger property than a temporal-coordination arc, V-01 > V-02. If they score equivalently, the tie remains and R12 must find the asymmetric discriminator.

Axis F (C-42) provides a third axis orthogonal to D and E: it names the CONTRACT REGISTER as a temporal artifact (planning phase) at the section header level, converting C-36's write-point temporal coordination declaration into a register-level temporal invariant visible at the start of execution. Composite C-45 = C-42 + C-36: dual temporal declaration -- register header names planning phase; write-point coordination statement names the planning-to-recovery relationship. V-04 (A+B+C in R10) carries C-36 and gains C-45 when Axis F is added.

---

## V-01

**Axis**: D -- criterion-tagged SLOT 3 contamination consequence at Branch A recovery directive (C-40)
**Hypothesis**: C-34 requires the Branch A THREE-LAYER WRITE POINT recovery directive to name the recovery action ("re-read this BRANCH A header") and the prohibited alternative ("cross-reference Branch B instructions"). The current V-01 (R10) recovery directive provides this plus a register cross-reference: "G-7a COMPLETENESS and G-7b EXCLUSIVITY govern this slot; G-9 INERTIA governs SLOT 4." However, naming labels is not the same as naming consequences: a model that ignores the prohibited-alternative warning and applies Branch B's template at SLOT 3 does not know from the recovery directive alone which criterion the contamination violates. Axis D adds a SLOT 3 contamination-consequence line immediately after the register cross-reference: it names the specific structural substitution that contamination produces (READINESS LINE instead of markdown sentence) and the criterion IDs that substitution violates (G-4/C-04, G-7a/C-13, C-16). The hypothesis: criterion-tagged contamination consequences at the recovery point convert the prohibited-alternative warning from a procedural instruction into a criterion-linked failure-mode declaration, making contamination avoidance independently verifiable at the write point without a spec search. Key asymmetry from V-02: V-01 lacks branch-qualified slot annotations (C-35 absent) -- the CONTRACT REGISTER still uses `[SLOT 3]` without branch qualification, and Branch B register entries carry no format-type annotations. The contamination consequence at the write point must compensate for the absence of format-type disambiguation at planning time.

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
SLOT 3 contamination consequence: if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates G-4 (C-04 readiness calibration), replaces LAYER 1 [RULE G-7a COMPLETENESS] (C-13) with the card format, and bypasses the LAYER 3 G-7a COMPLETENESS SCAN (C-16).

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

**Expected score under v11**: 26/31 = 98.4 (same as R10 V-01 -- C-40 is not yet a v11 criterion)
**Candidate criteria satisfied**: C-40 (SLOT 3 contamination consequence names structural substitution and criterion IDs violated)
**Candidate criteria absent**: C-41 (register Branch B entries have no format-type qualifiers), C-42 (register header has no temporal-role annotation)
**Key difference from V-05**: The `=== THREE-LAYER WRITE POINT (BRANCH A) ===` recovery directive gains a `SLOT 3 contamination consequence:` line that names (1) the structural substitution that Branch B contamination produces at this slot, (2) the specific criterion IDs violated by that substitution. C-34 already named the prohibited alternative ("cross-reference Branch B instructions"); C-40 names the OUTPUT CONSEQUENCE of following that prohibited path and the criteria that consequence breaks. The system property created by C-40: a model encountering the recovery directive now has criterion-traceable failure-mode information for SLOT 3 contamination without any spec search.
**Key difference from R10 V-01**: R10 V-01 carried C-34 (recovery directive with recovery action + prohibited alternative + register cross-reference). R11 V-01 adds the criterion-tagged contamination consequence line. The recovery directive now performs four functions: (1) recovery action naming, (2) prohibited alternative naming, (3) register cross-reference, (4) criterion-tagged contamination consequence. R10 V-01 performed only the first three.

---

## V-02

**Axis**: E -- structural format-type annotations in Branch B dual-mapped register entries (C-41)
**Hypothesis**: C-35 requires the CONTRACT REGISTER to carry branch-qualified slot annotations: `G-7 [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]`. This establishes branch-specific forward navigation -- a model following the BRANCH A entry arrives at the BRANCH A write point without cross-path ambiguity. However, knowing the position name (`READINESS LINE / BRANCH B`) does not tell the model what structural format that position requires. A model that knows it must write to `READINESS LINE / BRANCH B` but has not yet entered Branch B may apply markdown formatting to that position -- the register tells it WHERE to write but not in WHAT FORMAT. Axis E extends each Branch B dual-mapped entry with a structural format-type qualifier in parentheses: `(one card row, no markdown)` for the READINESS LINE and `(two card rows, no markdown)` for the NEXT STEP LINE. The hypothesis: format-type disambiguation at register-read time (planning phase) reduces Branch B format violations that arise not from attention degradation at the write point (covered by C-29) but from incorrect format assumptions established during the pre-dispatch planning phase. Key asymmetry from V-01: V-02 lacks the criterion-tagged contamination consequence (C-40 absent) -- the Branch A THREE-LAYER WRITE POINT header retains the recovery directive without a contamination consequence line. A model executing Branch A that applies Branch B's template at SLOT 3 receives no criterion-linked consequence warning at the recovery point.

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

**Expected score under v11**: 26/31 = 98.4 (same as R10 V-02 -- C-41 is not yet a v11 criterion)
**Candidate criteria satisfied**: C-41 (CONTRACT REGISTER Branch B dual-mapped entries carry structural format-type annotations in parentheses)
**Candidate criteria absent**: C-34 (Branch A THREE-LAYER WRITE POINT header uses generic recovery line, no BRANCH A name, no contamination consequence), C-40 (no criterion-tagged contamination consequence), C-42 (register header has no temporal-role annotation)
**Key difference from V-05**: Every CONTRACT REGISTER entry that dual-maps a Branch A slot to a Branch B position carries a structural format-type qualifier for the Branch B position. `READINESS LINE / BRANCH B` becomes `READINESS LINE / BRANCH B (one card row, no markdown)`. `NEXT STEP LINE / BRANCH B` becomes `NEXT STEP LINE / BRANCH B (two card rows, no markdown)`. The system property created by C-41: a model reading the register at execution start knows not just where each invariant governs on each branch but what structural output format is expected at that position. Format ambiguity at planning time is reduced before any branch-specific template context is encountered.
**Key difference from R10 V-02**: R10 V-02 carried C-35 (branch-qualified slot annotations without format-type qualifiers). R11 V-02 adds format-type qualifiers to Branch B entries only: the Branch A positions retain plain slot annotations (`[SLOT 3 / BRANCH A]`) while the Branch B positions gain format-type annotations (`READINESS LINE / BRANCH B (one card row, no markdown)`). The asymmetry is intentional: Branch A's structural format is implied by being the default markdown path; Branch B's format is non-default (ASCII card, no markdown) and benefits from explicit annotation.

---

## V-03

**Axes**: D+E -- criterion-tagged SLOT 3 contamination consequence + structural format-type annotations (C-40 + C-41)
**Hypothesis**: V-01 (Axis D alone) and V-02 (Axis E alone) address independent failure modes at different temporal positions on the execution arc. Axis E (C-41) reduces format-assumption errors at register-read time (planning phase, before branch dispatch). Axis D (C-40) adds criterion-linked consequence information at the Branch A write point (recovery phase, at SLOT 3). If both failure modes are independent -- as they are for the analogous C-34/C-35 pairing -- V-03 should score 28+2=30/new_N under v12 (gaining C-40 and C-41), plus pairwise composite C-43 (C-40+C-16) and C-44 (C-41+C-25), totaling 32/new_N. Key structural prediction: V-03 achieves C-43 (because C-40 and C-16 both address SLOT 3 / BRANCH A in adjacent positions: contamination warning fires at recovery header, scan executes before write) and C-44 (because C-41's format-type annotations are consistent with C-25's Branch B independent header, creating a format-type-consistent Branch B self-containment arc). Whether C-43's same-position double-gate is a stronger property than C-44's temporal-coordination arc will be resolved by live-run scoring.

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

**Expected score under v11**: 28/31 = 99.0 (same as R10 V-03 -- C-40 and C-41 are not yet v11 criteria)
**Candidate criteria satisfied**: C-40 (criterion-tagged SLOT 3 contamination consequence), C-41 (format-type annotations in Branch B register entries)
**Candidate criterion absent**: C-42 (register header has no temporal-role annotation); C-43 and C-44 depend on whether composites are scored independently
**Mechanism**: V-03 combines Axis D's write-point contamination warning (fires at SLOT 3 recovery phase) with Axis E's format-type-qualified register entries (established at planning phase, before branch dispatch). The temporal coordination property exists structurally: format-type annotations at planning phase reduce Branch B format ambiguity before execution; contamination consequence at recovery phase reduces Branch A contamination risk at the write point. Whether this coordination creates a composite C-43 or C-44 that scores independently under v12 will be determined by live-run analysis.

---

## V-04

**Axes**: D+E+F -- criterion-tagged SLOT 3 contamination consequence + structural format-type annotations + temporal-role declaration on register header (C-40 + C-41 + C-42)
**Hypothesis**: V-03 (D+E) achieves C-40 and C-41 and their structural coordination without naming the register's temporal role. V-04 extends V-03 with Axis F: an explicit temporal-role annotation on the CONTRACT REGISTER section header -- `[TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins]`. This converts the register from an unlabeled structural element into a named temporal artifact, consistent with C-36's temporal coordination statement at the write point. The hypothesis: declaring the register's temporal role at the section header makes the planning-to-recovery temporal chain visible at two structural levels -- register (planning phase declaration) and write point (recovery phase coordination statement via C-36) -- creating a dual temporal declaration that neither C-36 alone nor Axis F alone achieves. Composite C-45 = C-42 (Axis F) + C-36 (temporal coordination statement): both declare temporal roles, but at different positions in the execution arc. Their conjunction makes the full temporal chain (register = planning → write point = recovery) explicitly declared at both its endpoints.

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

**Expected score under v11**: 31/31 = 100.0 (same as R10 V-04 -- C-40, C-41, C-42 are not yet v11 criteria)
**Candidate criteria satisfied**: C-40, C-41, C-42 (all three R11 base axes), plus candidate composites C-43 (C-40+C-16), C-44 (C-41+C-25), C-45 (C-42+C-36)
**Candidate criteria absent**: none under R11 candidates
**Design note**: V-04 is structurally identical to V-03 except for two additions: (1) the `=== CONTRACT REGISTER [TEMPORAL ROLE: ...]===` temporal-role annotation on the register section header (Axis F / C-42); (2) the `Coordination:` line in the Branch A THREE-LAYER WRITE POINT header now explicitly references the temporal-role declaration: "established before execution begins per the temporal-role declaration." This cross-reference creates the C-45 composite: the write-point coordination statement (C-36) explicitly cites the register temporal-role declaration (C-42), creating a bidirectional link between the planning-phase declaration (register header) and the recovery-phase coordination statement (write-point header). Candidate C-45 system property: both temporal endpoints of the planning-to-recovery chain carry explicit temporal-role declarations AND each declaration references the other, making the chain navigable from either endpoint without spec search.

---

## V-05

**Axes**: none (neutral base / control)
**Hypothesis**: V-05 is R10 V-04 verbatim -- unchanged. It satisfies C-01 through C-39 (31/31 under v11) and fails all three R11 candidate axes (C-40 NO, C-41 NO, C-42 NO). Its role in R11 is identical to its role in R10: anchor the baseline and verify that the R10 ceiling is stable when re-scored in a new round context. If V-05 fails to score 31/31 under v11 in a live run, the R10 champion is not stable and R11 analysis is invalid; if it scores 31/31, the baseline holds and the candidate axes are independently attributable.

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

**Expected score under v11**: 31/31 = 100.0
**Candidate criteria satisfied**: none (C-40 NO, C-41 NO, C-42 NO)
**Candidate criteria absent**:
- C-40: Branch A THREE-LAYER WRITE POINT has no contamination-consequence line; recovery directive names the prohibited alternative but does not enumerate the criterion IDs violated if contamination occurs
- C-41: CONTRACT REGISTER Branch B dual-mapped entries carry no format-type qualifiers; `READINESS LINE / BRANCH B` not annotated with `(one card row, no markdown)`
- C-42: CONTRACT REGISTER section header has no temporal-role annotation; header reads `=== CONTRACT REGISTER ===` not `=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase ...] ===`

**Design note**: V-05 is R10 V-04 verbatim. The three candidate axes fail on distinct properties: (1) C-40 fails because the recovery directive enumerates recovery procedure and register labels but not the consequence of ignoring the prohibited alternative; (2) C-41 fails because branch-qualified annotations name position labels but not structural format types; (3) C-42 fails because the register section header carries no temporal-role declaration, making its temporal function implicit rather than declared. These three failure modes are structurally independent: a design can satisfy any subset without the others.

---

## Score Summary

| Variation | C-40 | C-41 | C-42 | v11 asp | v11 score | v12 predicted asp | v12 predicted score |
|-----------|------|------|------|---------|-----------|-------------------|---------------------|
| V-01 (D) | YES | NO | NO | 26/31 | **98.4** | 28/37* | **97.6*** |
| V-02 (E) | NO | YES | NO | 26/31 | **98.4** | 28/37* | **97.6*** |
| V-03 (D+E) | YES | YES | NO | 28/31 | **99.0** | 32/37* | **98.6*** |
| V-04 (D+E+F) | YES | YES | YES | 31/31 | **100.0** | 37/37* | **100.0*** |
| V-05 (neutral) | NO | NO | NO | 31/31 | **100.0** | 31/37* | **98.4*** |

*v12 predictions assume 6 new criteria: C-40, C-41, C-42 (base axes) and C-43 (C-40+C-16), C-44 (C-41+C-25), C-45 (C-42+C-36). Denominator 37 = 31 + 6. Predicted asp counts assume all six criteria are independently verifiable.

**V-01 = V-02 predicted tie under v12**: Both single-axis variations gain two criteria each (base axis + one composite). The tie-breaking question is whether C-43 (same-position double-gate: C-40+C-16, both at SLOT 3 / BRANCH A) is a stronger composite than C-44 (temporal-coordination arc: C-41+C-25, register planning phase + Branch B recovery header). If the rubric scores them symmetrically, V-01 = V-02 at 28/37. If same-position double-gate is a structurally distinct composite class from temporal-coordination arc (as C-18's three-layer co-location was a different class from C-22's named checklist), the composites may score asymmetrically, breaking the tie. This is the live-run question R11 must resolve.

**R11 discriminator structure**: Under v11, V-01 = V-02 = 26/31 (tie preserved, new axes not yet criteria). The discriminator structure activates under v12. If v12 confirms C-40, C-41, C-42, C-43, C-44, C-45, the predicted ordering is V-04 (100.0) > V-03 (98.6) > V-01 = V-02 (97.6 if tie persists) > V-05 (98.4... but V-05 scores 31/37 which is 97.6 as well). V-05 at 31/37 = 97.6 would tie with V-01/V-02, which would mean R11's single-axis extensions are not independently verifiable above the neutral base -- the candidate criteria do not score. If V-01 and V-02 score above V-05 (31/37 = 97.6), at least the base axes are real. If V-01 > V-02 or V-02 > V-01, the tie is broken and R12 can proceed to triple combinations.

**Candidate C-43, C-44, C-45 prediction paths for R12**:
- If V-01 and V-02 score identically and both score above V-05: C-40 and C-41 are real base axes but their composites (C-43, C-44) may not be independently verifiable -- R12 should test whether same-position double-gate is a real criterion by isolating C-43 in a single-axis variation
- If V-01 > V-02: C-43 (same-position double-gate) scores while C-44 (temporal-coordination arc) does not -- or C-43 creates more composites; R12 champion includes C-43 + C-44 + C-45 as the new base
- If V-05 scores equally with V-01/V-02: the candidate axes are absorbed into v11 criteria without independent scoring contribution; R11 extraction fails and the tie-breaking mechanism requires a fundamentally different axis type
