R5 variations written to `simulations/quest/variations/topic-status-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — `topic:status`

**Root cause fix:** R4 moved the output template after execution phases in all 5 variations — a single structural choice that cost C-14 for every variation and cascaded to C-17/C-18. R5 starts from the R3 V-05 base (135/135, template-first with correct labeled layers) and adds the three new Tier 4 criteria.

| Var | Axis | Targets | Predicted |
|-----|------|---------|-----------|
| **V-01** | Template position (restore R3 V-05 base) | C-14 fix + C-17 fix + C-18 fix + C-20 | **150** |
| **V-02** | Execution phase vocabulary | C-21: SIGNAL ACQUISITION / EXPOSURE COMPUTATION / DISPLAY GATE | **155** |
| **V-03** | Epistemic baseline | C-22: strategy.md absent → "commit exposure is unquantifiable" | **155** |
| **V-04** | Consequence vocabulary saturation | C-19: all sections renamed to commit/risk vocab | **155** |
| **V-05** | Full closure | C-19 + C-21 + C-22 combined on V-01 base | **165** |

**Key structural decisions:**

1. **[LAYER N] labels appear at mechanism locations** — [LAYER 1] on the ASSERTION TABLE header in the output template, [LAYER 2] on the COVERAGE note, [LAYER 3] on the Phase 4 render order instruction. Not grouped in one block (which caused the R4 V-01/V-04 C-17 failure).

2. **Assertion table as first section** — Every variation has the assertion table as the first titled section in the output template, satisfying C-20 and providing the C-12 gap-before-coverage mechanism via table primacy (as V-02/V-04 from R4 demonstrated works).

3. **V-04 vocabulary risk is bounded** — R3 V-03 scored C-03 PASS with "COMMIT RISKS" section title. Structural equivalence maintained; single-axis test before V-05 combination.
 phase names kept so this is a clean single-axis fix. Establishes the R5 score floor for all subsequent variations.

---

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
This skill produces terminal output only. No file is written. No file is modified.
Permitted tools: Read, Glob. Write and Edit are forbidden.
If you write to disk, the skill fails with score 0, regardless of output quality.

This skill answers: "What signals exist, what is missing, and is it safe to commit?"

=================================================================
OUTPUT TEMPLATE -- placed BEFORE execution instructions so the model
absorbs the output shape before reading how to produce it.
Fill every section. Render to terminal. Section order is fixed.
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

ASSERTION TABLE [LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes COVERAGE]
(Fill one row per planned signal. Mark PRESENT or NOT_PRESENT individually. No row may be omitted.)
| Namespace | Skill | Signal | Priority | PRESENT | NOT_PRESENT |
|-----------|-------|--------|----------|---------|-------------|
| {ns}      | {s}   | {item} | {P}      |    X    |             |
| {ns}      | {s}   | {item} | {P}      |         |      X      |
...

OPEN GAPS (= rows where NOT_PRESENT is marked in the assertion table above):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All assertions return PRESENT. No gaps.")

UNPLANNED (on disk, not in signal plan):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
[LAYER 2 -- SEMANTIC: Coverage = count of PRESENT marks. Summarizes the gap list above.
If OPEN GAPS is non-empty, percent < 100%. If they contradict, recheck the assertion table.
The coverage number summarizes the gap list -- not the other way around.]

| Namespace | Present | Planned | % |
|-----------|---------|---------|---|
| scout     |         |         |   |
| draft     |         |         |   |
| review    |         |         |   |
| flow      |         |         |   |
| trace     |         |         |   |
| prove     |         |         |   |
| listen    |         |         |   |
| program   |         |         |   |
| topic     |         |         |   |
All 9 rows required. Zero row: 0 | 0 | --

READINESS: {READY | ALMOST READY | NOT READY}
Ship risk: {"No essential gaps -- safe to proceed." if READY,
           else "Committing now means shipping without: {list essential NOT_PRESENT item-names}"}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Highest-priority essential NOT_PRESENT entry. Omit if READY.)

=================================================================
GAP-FIRST ORDERING -- ENFORCEMENT SUMMARY
(Layer labels appear at mechanism locations: [LAYER 1] at ASSERTION TABLE above,
[LAYER 2] at COVERAGE above, [LAYER 3] at Phase 4 render order below.)

[LAYER 1 -- STRUCTURAL (template position)]
ASSERTION TABLE is positioned first in this template, before OPEN GAPS and COVERAGE.
Template section order is structural and canonical: execution instructions cannot
reorder sections without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
Coverage = count of PRESENT marks. Gaps = set of NOT_PRESENT marks. Both derive from
the same assertion table. Gaps must be enumerated before coverage is computed; coverage
is their mathematical complement. Computing coverage before enumerating gaps inverts the
information dependency and creates the "100% with gaps listed" contradiction failure mode.

[LAYER 3 -- EXECUTION (render sequence)]
Phase 4 render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE ->
TABLE -> READINESS -> NEXT. Deviating from this sequence is a structural error.
=================================================================

EXECUTION PHASES -- compute values to fill the output template above
--------------------------------------------------------------------

===== PHASE 1: DISCOVER =====
Gate: both inputs complete and immutable before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. Fixed.
     Zero: DISK = {}. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | item-name | priority) ...]
              Name the path in output -- this is the signal plan baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = {}.
              State: "Signal plan not found -- no planned baseline."
              Do not silently compute against zero.

===== PHASE 2: ASSERT (per signal -- no batch evaluation) =====
Gate: every entry in PLANNED receives exactly one verdict before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK contains a path matching *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

Do not skip any entry. Evaluate all planned signals individually.

After all assertions:
  COVERED LIST = {P : assertion = PRESENT}
  GAP LIST     = {P : assertion = NOT_PRESENT}   [gaps = planned minus PRESENT set]
  UNPLANNED    = {D in DISK : D doesn't match any P.item-name}

GAP LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: COMPUTE =====
Gate: all calculations from Phase 2 results only. No re-globbing.

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: GAP LIST non-empty and percent = 100% -> assertion table error. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns] for each.

  Readiness:
    READY        -- 0 essential entries in GAP LIST
    ALMOST READY -- 1-2 essential entries in GAP LIST
    NOT READY    -- 3+ essential entries in GAP LIST, or STRATEGY_STATUS = NOT FOUND

  Ship risk sentence:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential NOT_PRESENT item-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK.
         Age = today minus date. > 30 days = STALE, record age in days.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES -> stop. Output: "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
[LAYER 3 -- EXECUTION] Render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE ->
  COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order defined in the template [LAYER 1 -- STRUCTURAL].
The coverage number summarizes the gap list -- not the other way around [LAYER 2 -- SEMANTIC].

Phase 4 complete. No file was written.
```

---

## V-02 — Consequence Phase Names

**Axis:** Execution phase vocabulary (single axis: C-21)
**Hypothesis:** Renaming execution phases from procedural labels (DISCOVER, COMPUTE, DISPLAY) to consequence vocabulary (SIGNAL ACQUISITION, EXPOSURE COMPUTATION, DISPLAY GATE) extends the decision frame from output sections into the execution architecture itself. C-21 requires the phase name shift to match the output framing — what each phase computes *toward*, not what operation it performs. On top of V-01's full C-01–C-20 baseline, adding C-21 requires only phase name changes with no structural risk to existing passing criteria.

---

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
This skill produces terminal output only. No file is written. No file is modified.
Permitted tools: Read, Glob. Write and Edit are forbidden.
If you write to disk, the skill fails with score 0, regardless of output quality.

This skill answers: "What signals exist, what is missing, and is it safe to commit?"

=================================================================
OUTPUT TEMPLATE -- placed BEFORE execution instructions so the model
absorbs the output shape before reading how to produce it.
Fill every section. Render to terminal. Section order is fixed.
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

ASSERTION TABLE [LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes COVERAGE]
(Fill one row per planned signal. Mark PRESENT or NOT_PRESENT individually. No row may be omitted.)
| Namespace | Skill | Signal | Priority | PRESENT | NOT_PRESENT |
|-----------|-------|--------|----------|---------|-------------|
| {ns}      | {s}   | {item} | {P}      |    X    |             |
| {ns}      | {s}   | {item} | {P}      |         |      X      |
...

OPEN GAPS (= rows where NOT_PRESENT is marked in the assertion table above):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All assertions return PRESENT. No gaps.")

UNPLANNED (on disk, not in signal plan):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
[LAYER 2 -- SEMANTIC: Coverage = count of PRESENT marks. Summarizes the gap list above.
If OPEN GAPS is non-empty, percent < 100%. If they contradict, recheck the assertion table.
The coverage number summarizes the gap list -- not the other way around.]

| Namespace | Present | Planned | % |
|-----------|---------|---------|---|
| scout     |         |         |   |
| draft     |         |         |   |
| review    |         |         |   |
| flow      |         |         |   |
| trace     |         |         |   |
| prove     |         |         |   |
| listen    |         |         |   |
| program   |         |         |   |
| topic     |         |         |   |
All 9 rows required. Zero row: 0 | 0 | --

READINESS: {READY | ALMOST READY | NOT READY}
Ship risk: {"No essential gaps -- safe to proceed." if READY,
           else "Committing now means shipping without: {list essential NOT_PRESENT item-names}"}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Highest-priority essential NOT_PRESENT entry. Omit if READY.)

=================================================================
GAP-FIRST ORDERING -- ENFORCEMENT SUMMARY
(Layer labels appear at mechanism locations: [LAYER 1] at ASSERTION TABLE above,
[LAYER 2] at COVERAGE above, [LAYER 3] at DISPLAY GATE render order below.)

[LAYER 1 -- STRUCTURAL (template position)]
ASSERTION TABLE is positioned first in this template, before OPEN GAPS and COVERAGE.
Template section order is structural and canonical: execution instructions cannot
reorder sections without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
Coverage = count of PRESENT marks. Gaps = set of NOT_PRESENT marks. Both derive from
the same assertion table. Gaps must be enumerated before coverage is computed; coverage
is their mathematical complement. Computing coverage before enumerating gaps inverts the
information dependency and creates the "100% with gaps listed" contradiction failure mode.

[LAYER 3 -- EXECUTION (render sequence)]
DISPLAY GATE render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE ->
TABLE -> READINESS -> NEXT. Deviating from this sequence is a structural error.
=================================================================

EXECUTION PHASES -- compute values to fill the output template above
--------------------------------------------------------------------

===== PHASE 1: SIGNAL ACQUISITION =====
Gate: both inputs complete and immutable before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. Fixed.
     Zero: DISK = {}. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | item-name | priority) ...]
              Name the path in output -- this is the signal plan baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = {}.
              State: "Signal plan not found -- no planned baseline."
              Do not silently compute against zero.

===== PHASE 2: PER-SIGNAL COMMITMENT ASSERTION (no batch evaluation) =====
Gate: every entry in PLANNED receives exactly one verdict before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK contains a path matching *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

Do not skip any entry. Evaluate all planned signals individually.

After all assertions:
  COVERED LIST = {P : assertion = PRESENT}
  GAP LIST     = {P : assertion = NOT_PRESENT}   [gaps = planned minus PRESENT set]
  UNPLANNED    = {D in DISK : D doesn't match any P.item-name}

GAP LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: EXPOSURE COMPUTATION =====
Gate: all calculations from Phase 2 results only. No re-globbing.

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: GAP LIST non-empty and percent = 100% -> assertion table error. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns] for each.

  Readiness:
    READY        -- 0 essential entries in GAP LIST
    ALMOST READY -- 1-2 essential entries in GAP LIST
    NOT READY    -- 3+ essential entries in GAP LIST, or STRATEGY_STATUS = NOT FOUND

  Ship risk sentence:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential NOT_PRESENT item-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK.
         Age = today minus date. > 30 days = STALE, record age in days.

===== PHASE 4: DISPLAY GATE =====
Pre-display gate: has any file been written or modified?
  YES -> stop. Output: "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
[LAYER 3 -- EXECUTION] Render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE ->
  COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order defined in the template [LAYER 1 -- STRUCTURAL].
The coverage number summarizes the gap list -- not the other way around [LAYER 2 -- SEMANTIC].

DISPLAY GATE passed. No file was written.
```

---

## V-03 — Epistemic Baseline

**Axis:** Epistemic framing for missing strategy.md (single axis: C-22)
**Hypothesis:** When strategy.md is absent, stating "No planned baseline -- commit exposure is unquantifiable" rather than "Signal plan not found" reframes the missing file as a decision-quality failure rather than a runtime error. C-22 requires the baseline absence to be framed as an epistemic consequence for the commit decision, not handled as a file-not-found case. On top of V-01's baseline, adding C-22 requires only a phrase change in the strategy.md missing-case handler — minimum structural change, maximum criterion gain.

---

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
This skill produces terminal output only. No file is written. No file is modified.
Permitted tools: Read, Glob. Write and Edit are forbidden.
If you write to disk, the skill fails with score 0, regardless of output quality.

This skill answers: "What signals exist, what is missing, and is it safe to commit?"

=================================================================
OUTPUT TEMPLATE -- placed BEFORE execution instructions so the model
absorbs the output shape before reading how to produce it.
Fill every section. Render to terminal. Section order is fixed.
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND -- if absent: commit exposure is unquantifiable]

ASSERTION TABLE [LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes COVERAGE]
(Fill one row per planned signal. Mark PRESENT or NOT_PRESENT individually. No row may be omitted.)
| Namespace | Skill | Signal | Priority | PRESENT | NOT_PRESENT |
|-----------|-------|--------|----------|---------|-------------|
| {ns}      | {s}   | {item} | {P}      |    X    |             |
| {ns}      | {s}   | {item} | {P}      |         |      X      |
...

OPEN GAPS (= rows where NOT_PRESENT is marked in the assertion table above):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All assertions return PRESENT. No gaps.")

UNPLANNED (on disk, not in signal plan):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
[LAYER 2 -- SEMANTIC: Coverage = count of PRESENT marks. Summarizes the gap list above.
If OPEN GAPS is non-empty, percent < 100%. If they contradict, recheck the assertion table.
The coverage number summarizes the gap list -- not the other way around.]

| Namespace | Present | Planned | % |
|-----------|---------|---------|---|
| scout     |         |         |   |
| draft     |         |         |   |
| review    |         |         |   |
| flow      |         |         |   |
| trace     |         |         |   |
| prove     |         |         |   |
| listen    |         |         |   |
| program   |         |         |   |
| topic     |         |         |   |
All 9 rows required. Zero row: 0 | 0 | --

READINESS: {READY | ALMOST READY | NOT READY}
Ship risk: {"No essential gaps -- safe to proceed." if READY,
           else "Committing now means shipping without: {list essential NOT_PRESENT item-names}"}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Highest-priority essential NOT_PRESENT entry. Omit if READY.)

=================================================================
GAP-FIRST ORDERING -- ENFORCEMENT SUMMARY
(Layer labels appear at mechanism locations: [LAYER 1] at ASSERTION TABLE above,
[LAYER 2] at COVERAGE above, [LAYER 3] at Phase 4 render order below.)

[LAYER 1 -- STRUCTURAL (template position)]
ASSERTION TABLE is positioned first in this template, before OPEN GAPS and COVERAGE.
Template section order is structural and canonical: execution instructions cannot
reorder sections without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
Coverage = count of PRESENT marks. Gaps = set of NOT_PRESENT marks. Both derive from
the same assertion table. Gaps must be enumerated before coverage is computed; coverage
is their mathematical complement. Computing coverage before enumerating gaps inverts the
information dependency and creates the "100% with gaps listed" contradiction failure mode.

[LAYER 3 -- EXECUTION (render sequence)]
Phase 4 render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE ->
TABLE -> READINESS -> NEXT. Deviating from this sequence is a structural error.
=================================================================

EXECUTION PHASES -- compute values to fill the output template above
--------------------------------------------------------------------

===== PHASE 1: DISCOVER =====
Gate: both inputs complete and immutable before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. Fixed.
     Zero: DISK = {}. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | item-name | priority) ...]
              Name the path in output -- this is the signal plan baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = {}.
              Output: "No planned baseline -- commit exposure is unquantifiable."
              Consequence: coverage cannot be computed against a known target.
              Do not silently compute against zero.

===== PHASE 2: ASSERT (per signal -- no batch evaluation) =====
Gate: every entry in PLANNED receives exactly one verdict before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK contains a path matching *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

Do not skip any entry. Evaluate all planned signals individually.

After all assertions:
  COVERED LIST = {P : assertion = PRESENT}
  GAP LIST     = {P : assertion = NOT_PRESENT}   [gaps = planned minus PRESENT set]
  UNPLANNED    = {D in DISK : D doesn't match any P.item-name}

GAP LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: COMPUTE =====
Gate: all calculations from Phase 2 results only. No re-globbing.

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: GAP LIST non-empty and percent = 100% -> assertion table error. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns] for each.

  Readiness:
    READY        -- 0 essential entries in GAP LIST
    ALMOST READY -- 1-2 essential entries in GAP LIST
    NOT READY    -- 3+ essential entries in GAP LIST, or STRATEGY_STATUS = NOT FOUND
                    (NOT FOUND case: commit exposure is unquantifiable -- treat as NOT READY)

  Ship risk sentence:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential NOT_PRESENT item-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK.
         Age = today minus date. > 30 days = STALE, record age in days.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES -> stop. Output: "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
[LAYER 3 -- EXECUTION] Render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE ->
  COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order defined in the template [LAYER 1 -- STRUCTURAL].
The coverage number summarizes the gap list -- not the other way around [LAYER 2 -- SEMANTIC].

Phase 4 complete. No file was written.
```

---

## V-04 — Consequence Vocabulary Saturation

**Axis:** Output section vocabulary (single axis: C-19)
**Hypothesis:** Recasting all major output section titles in commit/risk vocabulary (ASSERTION TABLE → COMMIT RISK REGISTER, OPEN GAPS → COMMIT RISKS, COVERAGE → EXPOSURE SUMMARY, READINESS → COMMIT DECISION, NEXT STEP → HIGHEST PRIORITY RISK) embeds the decision frame architecturally in the section taxonomy. The vocabulary shift must be consistent — no section reverts to status-reporting language. C-19 implies C-16 (consequence-framed verdict), which is already satisfied by the "Committing now means shipping without:" sentence. Risk vector: renaming OPEN GAPS to COMMIT RISKS or READINESS to COMMIT DECISION may destabilize C-03 or C-05 recognition — mitigated by maintaining structural equivalence (same content, different titles, as tested in R3 V-03 which scored C-03 and C-05 PASS).

---

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
Terminal output only. No file written. No file modified.
Permitted tools: Read, Glob. Forbidden: Write, Edit.
If you write to disk, the skill fails with score 0.

This skill answers: "Is it safe to commit? What commitment gaps remain?"

=================================================================
OUTPUT TEMPLATE -- placed BEFORE execution instructions so the model
absorbs the commit decision structure before reading how to produce it.
Fill every section. Render to terminal. Section order is fixed.
=================================================================

COMMIT READINESS AUDIT: {topic}
Commit baseline: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

COMMIT RISK REGISTER [LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
(Fill one row per planned signal. Mark VERIFIED or UNVERIFIED individually. No row may be omitted.)
| Namespace | Skill | Signal | Priority | VERIFIED | UNVERIFIED |
|-----------|-------|--------|----------|----------|------------|
| {ns}      | {s}   | {item} | {P}      |    X     |            |
| {ns}      | {s}   | {item} | {P}      |          |     X      |
...

COMMIT RISKS (= rows where UNVERIFIED is marked in the register above):
  [ ] {namespace}/{skill}  {signal-name}  ({priority})
  ...
  (none: "All commitments verified. No commit risks.")

UNPLANNED SIGNALS (on disk, not in commit baseline):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days -- commitment based on outdated evidence):
  ! {filepath}  ({N} days old)
  (omit section if none)

EXPOSURE SUMMARY: {total_verified} / {total_planned} commitments verified  --  {percent}%
[LAYER 2 -- SEMANTIC: Exposure = count of UNVERIFIED rows. Coverage = count of VERIFIED rows.
Both derive from the same register. Risks must be enumerated before coverage is computed.
The exposure percentage summarizes the commit risk register -- not the other way around.]

| Namespace | Verified | Planned | % |
|-----------|:--------:|:-------:|---|
| scout     |          |         |   |
| draft     |          |         |   |
| review    |          |         |   |
| flow      |          |         |   |
| trace     |          |         |   |
| prove     |          |         |   |
| listen    |          |         |   |
| program   |          |         |   |
| topic     |          |         |   |
All 9 rows required. Zero row: 0 | 0 | --

COMMIT DECISION: {SAFE TO COMMIT | COMMIT WITH KNOWN EXPOSURE | DO NOT COMMIT}
Consequence: {"No essential risks -- safe to proceed." if SAFE TO COMMIT,
             else "Committing now means shipping without: {list essential UNVERIFIED signal-names}"}

HIGHEST PRIORITY RISK: Run /{namespace}:{skill} to verify {signal-name}.
                       (Highest-priority essential UNVERIFIED entry. Omit if SAFE TO COMMIT.)

=================================================================
GAP-FIRST ORDERING -- ENFORCEMENT SUMMARY
(Layer labels appear at mechanism locations: [LAYER 1] at COMMIT RISK REGISTER above,
[LAYER 2] at EXPOSURE SUMMARY above, [LAYER 3] at Phase 4 render order below.)

[LAYER 1 -- STRUCTURAL (template position)]
COMMIT RISK REGISTER is positioned first in this template, before COMMIT RISKS and
EXPOSURE SUMMARY. Template section order is structural and canonical: execution
instructions cannot reorder sections without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
Exposure percentage = count of UNVERIFIED rows. Verified count = VERIFIED rows. Both derive
from the same register. Commit risks must be enumerated first because coverage is their
complement. "The exposure percentage summarizes the commit risk register -- not the other way around."

[LAYER 3 -- EXECUTION (render sequence)]
Phase 4 render order: COMMIT RISK REGISTER -> COMMIT RISKS -> UNPLANNED SIGNALS -> STALE ->
EXPOSURE SUMMARY -> TABLE -> COMMIT DECISION -> HIGHEST PRIORITY RISK.
Deviating from this sequence is a structural error.
=================================================================

EXECUTION PHASES -- compute values to fill the output template above
--------------------------------------------------------------------

===== PHASE 1: DISCOVER =====
Gate: both inputs complete and immutable before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. Fixed.
     Zero: DISK = {}. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | signal-name | priority) ...]
              Name the path in output -- this is the commit baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = {}.
              State: "Commit baseline not found -- no planned signals to verify."
              Do not silently compute against zero.

===== PHASE 2: ASSERT (per signal -- no batch evaluation) =====
Gate: every entry in PLANNED receives exactly one verdict before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK contains a path matching *{topic}*{P.signal-name}*
  TRUE  -> P.assertion = VERIFIED
  FALSE -> P.assertion = UNVERIFIED

Do not skip any entry. Evaluate all planned signals individually.

After all assertions:
  VERIFIED LIST   = {P : assertion = VERIFIED}
  UNVERIFIED LIST = {P : assertion = UNVERIFIED}   [commit risks = planned minus VERIFIED set]
  UNPLANNED       = {D in DISK : D doesn't match any P.signal-name}

UNVERIFIED LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: COMPUTE =====
Gate: all calculations from Phase 2 results only. No re-globbing.

  total_verified = |VERIFIED LIST|
  total_planned  = |PLANNED|
  percent        = total_verified / total_planned * 100  (N/A if total_planned = 0)

  Consistency: UNVERIFIED LIST non-empty and percent = 100% -> register error. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_verified[ns], ns_planned[ns] for each.

  Commit decision:
    SAFE TO COMMIT          -- 0 essential entries in UNVERIFIED LIST
    COMMIT WITH KNOWN EXPOSURE -- 1-2 essential entries in UNVERIFIED LIST
    DO NOT COMMIT           -- 3+ essential entries in UNVERIFIED LIST, or STRATEGY_STATUS = NOT FOUND

  Consequence sentence:
    SAFE:      "No essential risks -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential UNVERIFIED signal-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK.
         Age = today minus date. > 30 days = STALE, record age in days.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES -> stop. Output: "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
[LAYER 3 -- EXECUTION] Render order: COMMIT RISK REGISTER -> COMMIT RISKS -> UNPLANNED SIGNALS ->
  STALE -> EXPOSURE SUMMARY -> TABLE -> COMMIT DECISION -> HIGHEST PRIORITY RISK.
Do not change the section order defined in the template [LAYER 1 -- STRUCTURAL].
The exposure percentage summarizes the commit risk register -- not the other way around [LAYER 2 -- SEMANTIC].

Phase 4 complete. No file was written.
```

---

## V-05 — Full Structural Closure

**Axes:** All three Tier 4 additions combined (C-19 + C-21 + C-22)
**Hypothesis:** Combining consequence vocabulary saturation (C-19), consequence phase names (C-21), and epistemic baseline (C-22) on the V-01 structural foundation achieves complete structural closure against the v5 rubric. Every criterion addressed: template-first (C-14), assertion table in template as first section (C-18/C-20), labeled gap-first layers on C-13 mechanisms (C-13/C-17), per-signal assertion chain (C-15), consequence verdict with ship risk sentence (C-16/C-19), consequence phase names throughout execution architecture (C-21), and epistemic framing of missing baseline (C-22). Predicted 165/165. Primary risk: C-19 vocabulary saturation must not leave any major section using status-reporting language; confirmed by V-04 single-axis test.

---

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
Terminal output only. No file written. No file modified.
Permitted tools: Read, Glob. Forbidden: Write, Edit.
If you write to disk, the skill fails with score 0.

This skill answers: "Is it safe to commit? What commitment gaps remain?"

=================================================================
OUTPUT TEMPLATE -- placed BEFORE execution instructions so the model
absorbs the commit decision structure before reading how to produce it.
Fill every section. Render to terminal. Section order is fixed.
=================================================================

COMMIT READINESS AUDIT: {topic}
Commit baseline: simulations/{topic}/strategy.md
  [FOUND: commit exposure is quantifiable | NOT FOUND: commit exposure is unquantifiable]

COMMIT RISK REGISTER [LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
(Fill one row per planned signal. Mark VERIFIED or UNVERIFIED individually. No row may be omitted.)
| Namespace | Skill | Signal | Priority | VERIFIED | UNVERIFIED |
|-----------|-------|--------|----------|----------|------------|
| {ns}      | {s}   | {item} | {P}      |    X     |            |
| {ns}      | {s}   | {item} | {P}      |          |     X      |
...

COMMIT RISKS (= rows where UNVERIFIED is marked in the register above):
  [ ] {namespace}/{skill}  {signal-name}  ({priority})
  ...
  (none: "All commitments verified. No commit risks.")

UNPLANNED SIGNALS (on disk, not in commit baseline):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days -- commitment based on outdated evidence):
  ! {filepath}  ({N} days old)
  (omit section if none)

EXPOSURE SUMMARY: {total_verified} / {total_planned} commitments verified  --  {percent}%
[LAYER 2 -- SEMANTIC: Exposure = count of UNVERIFIED rows. Coverage = count of VERIFIED rows.
Both derive from the same register. Risks must be enumerated before coverage is computed.
The exposure percentage summarizes the commit risk register -- not the other way around.]

| Namespace | Verified | Planned | % |
|-----------|:--------:|:-------:|---|
| scout     |          |         |   |
| draft     |          |         |   |
| review    |          |         |   |
| flow      |          |         |   |
| trace     |          |         |   |
| prove     |          |         |   |
| listen    |          |         |   |
| program   |          |         |   |
| topic     |          |         |   |
All 9 rows required. Zero row: 0 | 0 | --

COMMIT DECISION: {SAFE TO COMMIT | COMMIT WITH KNOWN EXPOSURE | DO NOT COMMIT}
Consequence: {"No essential risks -- safe to proceed." if SAFE TO COMMIT,
             else "Committing now means shipping without: {list essential UNVERIFIED signal-names}"}

HIGHEST PRIORITY RISK: Run /{namespace}:{skill} to verify {signal-name}.
                       (Highest-priority essential UNVERIFIED entry. Omit if SAFE TO COMMIT.)

=================================================================
GAP-FIRST ORDERING -- ENFORCEMENT SUMMARY
(Layer labels appear at mechanism locations: [LAYER 1] at COMMIT RISK REGISTER above,
[LAYER 2] at EXPOSURE SUMMARY above, [LAYER 3] at DISPLAY GATE render order below.)

[LAYER 1 -- STRUCTURAL (template position)]
COMMIT RISK REGISTER is positioned first in this template, before COMMIT RISKS and
EXPOSURE SUMMARY. Template section order is structural and canonical: execution
instructions cannot reorder sections without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
Exposure percentage = count of UNVERIFIED rows. Verified count = VERIFIED rows. Both derive
from the same register. Commit risks must be enumerated first because coverage is their
complement. "The exposure percentage summarizes the commit risk register -- not the other way around."

[LAYER 3 -- EXECUTION (render sequence)]
DISPLAY GATE render order: COMMIT RISK REGISTER -> COMMIT RISKS -> UNPLANNED SIGNALS -> STALE ->
EXPOSURE SUMMARY -> TABLE -> COMMIT DECISION -> HIGHEST PRIORITY RISK.
Deviating from this sequence is a structural error.
=================================================================

EXECUTION PHASES -- compute values to fill the output template above
--------------------------------------------------------------------

===== PHASE 1: SIGNAL ACQUISITION =====
Gate: both inputs complete and immutable before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. Fixed.
     Zero: DISK = {}. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | signal-name | priority) ...]
              Record the path -- this is the commit baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = {}.
              Output: "No planned baseline -- commit exposure is unquantifiable."
              Consequence: coverage cannot be computed against a known target.
              Do not silently compute against zero.

===== PHASE 2: COMMITMENT ASSERTION (per signal -- no batch evaluation) =====
Gate: every entry in PLANNED receives exactly one verdict before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK contains a path matching *{topic}*{P.signal-name}*
  TRUE  -> P.assertion = VERIFIED
  FALSE -> P.assertion = UNVERIFIED

Do not skip any entry. Evaluate all planned signals individually.

After all assertions:
  VERIFIED LIST   = {P : assertion = VERIFIED}
  UNVERIFIED LIST = {P : assertion = UNVERIFIED}   [commit risks = planned minus VERIFIED set]
  UNPLANNED       = {D in DISK : D doesn't match any P.signal-name}

UNVERIFIED LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: EXPOSURE COMPUTATION =====
Gate: all calculations from Phase 2 results only. No re-globbing.

  total_verified = |VERIFIED LIST|
  total_planned  = |PLANNED|
  percent        = total_verified / total_planned * 100  (N/A if total_planned = 0)

  Consistency: UNVERIFIED LIST non-empty and percent = 100% -> register error. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_verified[ns], ns_planned[ns] for each.

  Commit decision:
    SAFE TO COMMIT          -- 0 essential entries in UNVERIFIED LIST
    COMMIT WITH KNOWN EXPOSURE -- 1-2 essential entries in UNVERIFIED LIST
    DO NOT COMMIT           -- 3+ essential entries in UNVERIFIED LIST, or STRATEGY_STATUS = NOT FOUND
                               (NOT FOUND case: commit exposure is unquantifiable)

  Consequence sentence:
    SAFE:      "No essential risks -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential UNVERIFIED signal-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK.
         Age = today minus date. > 30 days = STALE, record age in days.

===== PHASE 4: DISPLAY GATE =====
Pre-display gate: has any file been written or modified?
  YES -> stop. Output: "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
[LAYER 3 -- EXECUTION] Render order: COMMIT RISK REGISTER -> COMMIT RISKS -> UNPLANNED SIGNALS ->
  STALE -> EXPOSURE SUMMARY -> TABLE -> COMMIT DECISION -> HIGHEST PRIORITY RISK.
Do not change the section order defined in the template [LAYER 1 -- STRUCTURAL].
The exposure percentage summarizes the commit risk register -- not the other way around [LAYER 2 -- SEMANTIC].

DISPLAY GATE passed. No file was written.
```

---

## Criteria Coverage Matrix (predicted)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Signal discovery | YES | YES | YES | YES | YES |
| C-02 Coverage percentage | YES | YES | YES | YES | YES |
| C-03 Gap identification | YES | YES | YES | YES* | YES* |
| C-04 Display-only | YES | YES | YES | YES | YES |
| C-05 Readiness verdict | YES | YES | YES | YES* | YES* |
| C-06 Namespace breakdown | YES | YES | YES | YES | YES |
| C-07 Strategy cross-reference | YES | YES | YES | YES | YES |
| C-08 Recency awareness | YES | YES | YES | YES | YES |
| C-09 Actionable next step | YES | YES | YES | YES | YES |
| C-10 Structural completeness | YES | YES | YES | YES | YES |
| C-11 Phase-gated disk-check | YES | YES | YES | YES | YES |
| C-12 Gap-first output ordering | YES | YES | YES | YES | YES |
| C-13 Triple-redundancy guard | YES++ | YES++ | YES++ | YES++ | YES++ |
| C-14 Template-first absorption | YES++ | YES++ | YES++ | YES++ | YES++ |
| C-15 Per-signal assertion chain | YES++ | YES++ | YES++ | YES++ | YES++ |
| C-16 Consequence-framed verdict | YES | YES | YES | YES++ | YES++ |
| C-17 Labeled redundancy layers | YES++ | YES++ | YES++ | YES++ | YES++ |
| C-18 Assertion table pre-seeded in template | YES++ | YES++ | YES++ | YES++ | YES++ |
| C-19 Consequence vocabulary saturation | NO | NO | NO | YES++ | YES++ |
| C-20 Assertion table as primary gap artifact | YES++ | YES++ | YES++ | YES++ | YES++ |
| C-21 Consequence phase names | NO | YES++ | NO | NO | YES++ |
| C-22 Epistemic baseline | NO | NO | YES++ | NO | YES++ |
| **Predicted score / 165** | **150** | **155** | **155** | **155** | **165** |

`++` = primary axis treatment
`YES` = criterion met from base
`NO` = not targeted in this variation
`YES*` = consequence vocabulary rename (COMMIT RISKS, COMMIT DECISION) -- structural equivalence maintained; scorecard must recognize by structure not title

---

## Key Design Decisions

**Why [LAYER N] labels appear at mechanism locations, not only in a summary block:**
C-17 pass condition requires "labels are structurally distinct (not grouped in a single block)." R4 V-01/V-04 had [LAYER 1/2/3] in a summary block with labels on the wrong mechanisms. V-01–V-05 place labels at their mechanism locations ([LAYER 1] on the ASSERTION TABLE header in the output template; [LAYER 2] on the COVERAGE/EXPOSURE SUMMARY note; [LAYER 3] on the Phase 4 render order instruction) AND include a summary block for orientation. This satisfies "at the point where they appear" and "structurally distinct."

**Why assertion table is first in the output template (C-20):**
C-20 requires the PER-SIGNAL ASSERTION TABLE to be the first section. The header metadata (COMMIT READINESS AUDIT: {topic}, Commit baseline: ...) are single-line fields, not sections. The COMMIT RISK REGISTER / ASSERTION TABLE is the first titled section with content. V-02 and V-04 from R4 used this mechanism to satisfy C-12 via the assertion-table-first pattern — now C-20 makes it an explicit criterion.

**Why V-04 consequence vocabulary should not destabilize C-03:**
R3 V-03 (consequence saturation) scored C-03 PASS with a "COMMIT RISKS" section. C-03 pass condition reads for structural equivalence (a gap section exists, gaps are named, zero case explicit). "COMMIT RISKS" with `[ ] {namespace}/{skill} {signal-name} ({priority})` format satisfies this regardless of title.

**Single-axis tests before combining:**
V-02/V-03/V-04 isolate each new criterion. This ensures that if V-05 fails any criterion, we can identify which axis introduced the failure by checking the single-axis baseline. If V-04 shows a C-03 regression, V-05 inherits it; the fix is applied to V-04 before retrying V-05.
