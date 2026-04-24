Round 3 variations written to `simulations/quest/variations/topic-status-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — `topic-status`

### Summary

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | C-13 isolation — labeled ordering layers | Explicitly name all three gap-first layers (LAYER 1/2/3) so scorecard can unambiguously identify each one. R2 V-05 had them unlabeled. |
| **V-02** | C-15 + C-14 — assertion table in template | Pre-seed the PRESENT/NOT_PRESENT assertion table in the output template before execution. Model absorbs per-signal format before reading how to fill it. |
| **V-03** | C-16 — consequence saturation (deep frame) | Ship-risk vocabulary applied throughout: OPEN GAPS → COMMIT RISKS, READINESS → COMMIT DECISION, COVERAGE → EVIDENCE GATHERED. Tests vocabulary saturation depth. |
| **V-04** | C-13 + C-14 — template-first structural ordering | Template-first (C-14) as the structural anchor for LAYER 1 of triple-redundancy (C-13), combined as a paired guarantee. |
| **V-05** | Full synthesis — targeting 135/135 | All four simultaneously: assertion table in template (C-14+C-15 fused), three labeled layers (C-13), consequence sentence (C-16), full R2 floor. |

### Criteria coverage matrix (predicted)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-13 Triple-redundancy | **++** | NO | NO | **++** | **++** |
| C-14 Template-first | YES | **++** | NO | **++** | **++** |
| C-15 Per-signal assertion | YES | **++** | NO | YES | **++** |
| C-16 Consequence verdict | YES | YES | **++** | YES | **++** |
| **Predicted score** | **130** | **128** | **118** | **132** | **135** |

### Key divergence watches
- **V-03 C-03 risk:** "COMMIT RISKS" section title may not map cleanly to C-03's pass condition; scorecard reads for "gap section" by structure
- **V-02 C-13:** Only has LAYER 1 (template position) + partial LAYER 2 (NOTE block); no explicit LAYER 3 render sequence — C-13 likely fails
- **V-05 ceiling:** LAYER 2's [SEMANTIC] label and explanation is the structural hedge against a C-13 failure that drops 135 → 130
he differentiator.** Every variation bakes in the R2 structural floor (C-10/C-11/C-12) and targets all four new criteria. The primary axis determines which criteria are pushed hardest.

**C-15 + C-14 interaction (V-02/V-05):** Pre-seeding the ASSERTION TABLE format in the output template fuses both criteria — the template enforces the per-signal evaluation format (C-15 structural absorption) while being placed before execution instructions (C-14 positioning). The table can't be pre-populated per-topic, but the column structure (PRESENT/NOT_PRESENT headers, one-row-per-signal requirement) is pre-seeded.

**C-13 labeling strategy (V-01/V-04):** The three layers must be "structurally distinct" per rubric. Naming them LAYER 1 (template position) / LAYER 2 (semantic principle) / LAYER 3 (execution render sequence) makes them unambiguously distinguishable. This removes scorecard ambiguity about whether one mechanism "stated three times" versus three independent mechanisms.

**Predicted ranking:** V-05 > V-04 > V-02 > V-01 > V-03

**Predicted divergence watches:**
- C-16 in V-03: vocabulary saturation may confuse the scorecard if section title changes obscure structural criteria (e.g., "COMMIT RISKS" not mapping cleanly to C-03's "gap section")
- C-15 in V-02: assertion table pre-seeded in template — scorecard must recognize this as C-15 structural absorption, not just C-10 row presence; requires careful reading of the pass condition
- C-13 in V-01: labeled layers are in a block between template and execution phases; scorecard must confirm all three are "structurally distinct" — the semantic principle (LAYER 2) is the potential weak point
- V-05 ceiling risk: if C-15 pass condition requires "execution instructions direct per-entry evaluation" AND "output template shows assertion format," V-05 satisfies both; if it requires only execution instructions, V-05 satisfies via Phase 2 assertion chain

---

## V-01: C-13 Isolation — Labeled Ordering Layers

**Axis:** C-13 triple-redundancy — three gap-first enforcement layers made structurally explicit and named LAYER 1, LAYER 2, LAYER 3 so each is unambiguously identifiable by the scorecard.
**Hypothesis:** R2 V-05 had all three layers but without labels; a scorecard may conflate "three mentions of the same rule" with "three independent structural mechanisms." Explicit labels make the distinctness argument without needing inference. R2 structural floor (C-10/C-11/C-12) and R2 best practices (C-15 assertion chain, C-16 ship risk) maintained as baseline.

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
This skill produces terminal output only.
No file is written. No file is modified. Permitted tools: Read, Glob.
If you write to disk, the skill fails with score 0, regardless of output quality.

This skill answers: "What evidence exists, what is missing, and is it safe to commit?"

=================================================================
OUTPUT TEMPLATE -- fill every field, then render to terminal
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

OPEN GAPS (signals planned but not yet gathered):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "No gaps -- all planned signals present.")

UNPLANNED (on disk, not in signal plan):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
(This number summarizes the gap list above -- not the other way around.)

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
Ship risk: {consequence sentence -- "No essential gaps, safe to proceed." if READY,
           else "Committing now means shipping without: {list essential gap item-names}"}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Highest-priority essential gap. Omit if READY.)

=================================================================
GAP-FIRST ORDERING -- THREE INDEPENDENT ENFORCEMENT LAYERS

[LAYER 1 -- STRUCTURAL (template position)]
The OPEN GAPS section is placed before the COVERAGE line in the output
template above. Template section order is structural: it cannot be changed
by an execution instruction without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
The coverage number counts the gap list. The gap list is not derived from
the coverage number. Computing coverage before enumerating gaps inverts the
information dependency and creates the "100% with gaps listed" contradiction
failure mode. Enumerate all gaps first. Then derive coverage from that list.

[LAYER 3 -- EXECUTION (render sequence)]
Phase 4 render order: OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE
-> READINESS -> NEXT. Deviating from this sequence is a structural error
that must be corrected before rendering.
=================================================================

EXECUTION PHASES -- compute the values to fill the output template
-------------------------------------------------------------------

===== PHASE 1: DISCOVER =====
Gate: both inputs must be complete and fixed before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK_SIGNALS = [every returned path, verbatim]
     Zero results: DISK_SIGNALS = []. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | item-name | priority) ...]
              Name the path explicitly -- this is the planned signal baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = [].
              State: "Signal plan not found -- no planned baseline."

===== PHASE 2: ASSERT (per signal -- no batch) =====
Gate: every planned signal evaluated individually before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK_SIGNALS contains a path matching *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

Evaluate every P individually. Do not skip any entry.

After all assertions:
  COVERED LIST = {P : assertion = PRESENT}
  GAP LIST     = {P : assertion = NOT_PRESENT}   [gaps = planned minus PRESENT set]
  UNPLANNED    = {D in DISK_SIGNALS : D doesn't match any P.item-name}

GAP LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: COMPUTE =====
Gate: all calculations from Phase 2 results only. No re-globbing.

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: GAP LIST non-empty and percent = 100% -> assertion error. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns] for each.

  Readiness:
    READY        -- 0 essential entries in GAP LIST
    ALMOST READY -- 1-2 essential entries in GAP LIST
    NOT READY    -- 3+ essential entries in GAP LIST, or STRATEGY_STATUS = NOT FOUND

  Ship risk:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential gap item-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK_SIGNALS.
         Age = today minus date. > 30 days = STALE, record age in days.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES -> stop. Output: "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
Render order [LAYER 3]: OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order from the template [LAYER 1].
The coverage number summarizes the gap list -- not the other way around [LAYER 2].

Phase 4 complete. No file was written.
```

---

## V-02: C-15 + C-14 — Assertion Table Pre-Seeded in Template

**Axis:** Output format (template-first) fused with per-signal assertion (C-15). The ASSERTION TABLE itself -- with PRESENT and NOT_PRESENT columns and the requirement "one row per planned signal" -- is pre-seeded in the output template before any execution instruction. The model sees the per-signal evaluation format before it reads how to fill it.
**Hypothesis:** Pre-seeding the assertion table in the template is a tighter C-14+C-15 fusion than anything in R2. The template makes the per-signal format the default output shape -- the model must evaluate each signal to fill the table, not to satisfy an instruction. The OPEN GAPS section derives from NOT_PRESENT rows (making it visible in the template as a derived section). This enforces C-15 at absorption level rather than instruction level.

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
This skill produces terminal output only. No file is written. No file is modified.
Permitted tools: Read, Glob. Write and Edit are forbidden.
If you write to disk, the skill fails with score 0.

=================================================================
OUTPUT TEMPLATE -- placed before execution instructions so the model
absorbs the output shape before reading how to produce it.
Fill every section. Render to terminal.
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

ASSERTION TABLE (one row per planned signal; mark each individually):
| Namespace | Skill | Signal | Priority | PRESENT | NOT_PRESENT |
|-----------|-------|--------|----------|---------|-------------|
| {ns}      | {skill} | {item} | {P}   |    X    |             |
| {ns}      | {skill} | {item} | {P}   |         |      X      |
...
(Every planned signal receives exactly one mark. No row may be omitted.)

OPEN GAPS (= NOT_PRESENT rows from assertion table above):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All assertions return PRESENT. No gaps.")

UNPLANNED (on disk, not asserted against any planned entry):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
NOTE: Coverage = count of PRESENT marks. If OPEN GAPS is non-empty, percent < 100%.
These must be consistent. If they contradict, recheck the assertion table.

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
           (Highest-priority NOT_PRESENT essential entry. Omit if READY.)

=================================================================
SECTION ORDER: ASSERTION TABLE -> OPEN GAPS -> COVERAGE. The coverage
percentage is the count of PRESENT marks. The gap list is the NOT_PRESENT
rows. Both derive from the same assertion table. Do not reorder.
The percentage summarizes the table -- not the other way around.
=================================================================

EXECUTION PHASES -- gather values to fill the template above
------------------------------------------------------------

===== PHASE 1: LOAD =====
Gate: both inputs fixed before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. Fixed.
     Zero: DISK = {}. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   BASELINE = "simulations/{topic}/strategy.md"
              PLANNED = [(namespace | skill | item-name | priority) ...]
     Missing: BASELINE = NOT FOUND. PLANNED = {}.
              State: "Signal plan not found -- assertion baseline is empty."
     Name the path in output either way.

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

===== PHASE 3: AGGREGATE =====
Gate: from COVERED LIST and GAP LIST only. No re-globbing.

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: GAP LIST non-empty and percent = 100% -> assertion table error. Recheck Phase 2.

  Per namespace -- all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns] for each.

  Readiness:
    READY        -- GAP LIST has no essential entries
    ALMOST READY -- GAP LIST has 1-2 essential entries
    NOT READY    -- GAP LIST has 3+ essential entries, or BASELINE = NOT FOUND

  Ship risk:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential NOT_PRESENT item-names}"

  Stale: parse YYYY-MM-DD date suffix per path in DISK.
         > 30 days before today -> STALE, age = today minus date in days.

===== PHASE 4: DISPLAY =====
Pre-display contract check: has any file been written or modified?
  YES -> stop. Report "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
Render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order from the template. OPEN GAPS before COVERAGE.

Phase 4 complete. No file was written.
```

---

## V-03: C-16 — Consequence Saturation (Deep Frame)

**Axis:** Inertia framing -- consequence-framing vocabulary applied throughout the entire skill, not just the readiness verdict. OPEN GAPS → COMMIT RISKS, COVERAGE → EVIDENCE GATHERED, READINESS → COMMIT DECISION. The output is a "commit decision dashboard" rather than a status report.
**Hypothesis:** R2 V-04 added a single ship-risk sentence to an otherwise standard status output. V-03 tests whether making consequence framing the semantic backbone of the entire skill -- section titles, execution phase names, readiness structure -- produces a richer C-16 decision instrument or creates structural friction (section names less recognizable to scorecard criteria). If vocabulary saturation doesn't hurt C-01–C-12 scoring, V-03 may outperform on C-16 specifically. Risk: "COMMIT RISKS" may not map cleanly to C-03's "gap section" pass condition.

```
/topic:status -- Signal
Topic: {topic}

This skill answers: "Is it safe to commit this feature to users?"

DISPLAY CONTRACT
Terminal output only. No file written. No file modified.
Permitted: Read, Glob. Forbidden: Write, Edit.
If you write to disk, the skill fails with score 0.

=================================================================
OUTPUT TEMPLATE -- commit decision dashboard
=================================================================

FEATURE: {topic}
Evidence plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

COMMIT RISKS (planned evidence not yet gathered):
  [ ] {namespace}/{skill}  {signal-name}  ({priority})
  ...
  (none: "All planned evidence gathered. No commit risks.")

UNPLANNED EVIDENCE (on disk, not in evidence plan):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old -- may not reflect current state):
  ! {filepath}  ({N} days old)
  (omit section if none)

EVIDENCE GATHERED: {total_found} / {total_planned} planned signals  --  {percent}%

| Namespace | Gathered | Planned | % |
|-----------|----------|---------|---|
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

COMMIT DECISION: {COMMIT / PROCEED WITH CAUTION / DO NOT COMMIT}
Consequence: {
  COMMIT:               "Evidence complete. No essential risks identified."
  PROCEED WITH CAUTION: "Committing now means shipping without: {list essential missing signals}"
  DO NOT COMMIT:        "Committing now means shipping without: {list essential missing signals}.
                         Resolve before proceeding."
}

HIGHEST PRIORITY RISK: Run /{namespace}:{skill} to gather {signal-name}.
                       (Omit if COMMIT.)

=================================================================
SECTION ORDER: COMMIT RISKS appears before EVIDENCE GATHERED.
The percentage summarizes the risk list. The risk list is not derived from
the percentage. Compute risks first, then derive coverage from them.
Do not reorder. The evidence count is the complement of the risk count.
=================================================================

EXECUTION PHASES
----------------

===== PHASE 1: SURVEY =====
Gate: both inputs fixed before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     EVIDENCE = [every returned path]. Fixed.
     Zero: EVIDENCE = []. State "No evidence gathered yet." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   PLAN_PATH = "simulations/{topic}/strategy.md"
              PLAN = [(namespace | skill | signal-name | priority) ...]
              Name the path -- this is the commit evidence standard.
     Missing: PLAN_PATH = NOT FOUND. PLAN = [].
              State: "No evidence plan found -- commit risk cannot be assessed."

===== PHASE 2: IDENTIFY RISKS (before computing coverage) =====
Gate: enumerate every commit risk before computing the evidence percentage.

For each P in PLAN: is there a path in EVIDENCE matching *{topic}*{P.signal-name}*?
  YES -> GATHERED
  NO  -> MISSING (commit risk) -- record P.namespace | P.skill | P.signal-name | P.priority

For each E in EVIDENCE not matching any P.signal-name: UNPLANNED.

COMMIT RISK LIST is now fixed. Do not revise after this phase.

===== PHASE 3: COMPUTE =====
Gate: derived from Phase 2 only. No re-globbing.

  total_gathered = |GATHERED|
  total_planned  = |PLAN|
  percent        = total_gathered / total_planned * 100  (N/A if total_planned = 0)

  Consistency: COMMIT RISK LIST non-empty and percent = 100% -> recheck Phase 2.

  Per namespace -- all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_gathered[ns], ns_planned[ns] for each.

  Commit decision:
    COMMIT:               0 essential entries in COMMIT RISK LIST
    PROCEED WITH CAUTION: 1-2 essential entries in COMMIT RISK LIST
    NOT READY:            3+ essential entries in COMMIT RISK LIST, or plan not found

  Consequence sentence:
    COMMIT:               "Evidence complete. No essential risks identified."
    otherwise:            "Committing now means shipping without: {list essential missing signal-names}"

  Stale: parse YYYY-MM-DD date suffix for each E in EVIDENCE.
         > 30 days before today -> STALE, age = today minus date in days.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES -> stop. "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template. Render to terminal.
Render order: COMMIT RISKS -> UNPLANNED -> STALE -> EVIDENCE GATHERED -> TABLE
  -> COMMIT DECISION -> HIGHEST PRIORITY RISK.
Section order as defined in template: risks first, coverage after.

Phase 4 complete. No file was written.
```

---

## V-04: C-13 + C-14 Combination — Template-First Structural Ordering

**Axes:** Template-first (C-14) + explicitly labeled triple-redundancy ordering guard (C-13), combined as a paired structural guarantee. Per-signal assertion (C-15) and consequence framing (C-16) as floor.
**Hypothesis:** The two structural ordering criteria have a natural synergy: template-first (C-14) satisfies LAYER 1 (template position) of the triple-redundancy requirement, providing the structural anchor for C-13. The three layers are labeled in a dedicated block between template and execution phases, making the structural distinctness argument explicit. This combination tests whether C-14 + C-13 together produce a stronger ordering guarantee than either alone.

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
Terminal output only. No file written. No file modified.
Permitted tools: Read, Glob. If you write to disk, the skill fails (score 0).

=================================================================
OUTPUT TEMPLATE -- placed before execution instructions so the model
absorbs the output shape (section order, 9-row table, gap-first ordering)
before reading how to produce it.
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

OPEN GAPS (signals not yet gathered):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "No gaps -- all planned signals present.")

UNPLANNED (on disk, not in plan):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%

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
           else "Committing now means shipping without: {list essential gap item-names}"}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Highest-priority essential gap. Omit if READY.)

=================================================================
GAP-FIRST ORDERING -- THREE INDEPENDENT ENFORCEMENT LAYERS (all must hold)

[LAYER 1 -- STRUCTURAL (template position)]
The OPEN GAPS section is positioned before COVERAGE in the template above.
Template section order is the canonical output order. It is enforced by
physical placement -- it cannot be changed by an execution instruction
without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
The coverage number is a count of present signals. The gap list is the set
of absent signals. Both are derived from the same underlying signal set.
The gap list must be enumerated first because coverage is its complement.
Computing coverage before enumerating gaps inverts the information dependency
and creates the "100% with gaps" contradiction failure mode.

[LAYER 3 -- EXECUTION (render sequence)]
Phase 4 render order: OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE
-> READINESS -> NEXT. Any deviation from this sequence is a structural error
that must be corrected before finalizing output.
=================================================================

EXECUTION PHASES -- gather values to fill the template above
------------------------------------------------------------

===== PHASE 1: DISCOVER =====
Gate: both inputs complete and immutable before Phase 2.

1.1  Glob: simulations/**/{topic}-*
     DISK_SIGNALS = [every returned path, verbatim]
     Zero: DISK_SIGNALS = []. State "No signals found on disk." Continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | item-name | priority) ...]
              Name the path explicitly in output -- this is the signal plan baseline.
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = [].
              State: "Signal plan not found -- no planned baseline."

===== PHASE 2: ASSERT (per signal -- no batch) =====
Gate: every planned signal evaluated individually before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK_SIGNALS contains a path matching *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

All entries evaluated. No entry may be skipped.

  COVERED LIST = {P : assertion = PRESENT}
  GAP LIST     = {P : assertion = NOT_PRESENT}   [gaps = planned minus PRESENT set]
  UNPLANNED    = {D in DISK_SIGNALS : D doesn't match any P.item-name}

GAP LIST is now fixed. Do not revise in Phase 3 or 4.

===== PHASE 3: COMPUTE =====
Gate: from Phase 2 results only. No re-globbing.

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: GAP LIST non-empty and percent = 100% -> ERROR. Recheck Phase 2.

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns] for each.

  Readiness:
    READY        -- 0 essential entries in GAP LIST
    ALMOST READY -- 1-2 essential entries in GAP LIST
    NOT READY    -- 3+ essential entries in GAP LIST, or STRATEGY_STATUS = NOT FOUND

  Ship risk:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential gap item-names}"

  Stale: parse YYYY-MM-DD date suffix per path. > 30 days = STALE.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES -> stop. "SKILL FAILED: disk write detected."
  NO  -> proceed.

Fill the output template at the top of this prompt. Render to terminal.
Render order [LAYER 3]: OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE -> READINESS -> NEXT.
Section order defined by the template [LAYER 1]. Coverage summarizes the gap list [LAYER 2].

Phase 4 complete. No file was written.
```

---

## V-05: Full Synthesis — Targeting 135/135

**Axes:** All four new criteria simultaneously: template-first with pre-seeded assertion table (C-14 + C-15 fused), three explicitly labeled independent ordering layers (C-13), consequence-framed readiness verdict (C-16). Full R2 structural floor baked in (C-10/C-11/C-12). R3 ceiling candidate.
**Hypothesis:** Every structural guarantee aligned and independently enforced. Template is placed first and includes the assertion table format (model absorbs both output shape and per-signal evaluation format before reading execution steps). Three ordering layers are distinct and labeled. Each planned signal evaluated individually before aggregation. Readiness verdict names the cost of proceeding. No single layer failure can break the output contract. Predicted to score 135/135 if all pass conditions are met.

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
The only output this skill produces is a terminal display.
No file is written. No file is modified. Permitted tools: Read, Glob.
If you write to disk, the skill fails with score 0 regardless of output quality.

This skill answers: "What do we know, what are we missing, and is it safe to commit?"

=================================================================
OUTPUT TEMPLATE -- placed BEFORE execution instructions so the model
absorbs the output shape (section order, assertion format, 9 namespace rows)
before reading how to produce it. Fill every section. Render to terminal.
=================================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

ASSERTION TABLE (fill one row per planned signal; mark PRESENT or NOT_PRESENT):
| Namespace | Skill | Signal | Priority | PRESENT | NOT_PRESENT |
|-----------|-------|--------|----------|---------|-------------|
| {ns}      | {s}   | {item} | {P}      |    X    |             |
| {ns}      | {s}   | {item} | {P}      |         |      X      |
...
(Every planned signal receives exactly one mark. No row may be omitted.)

OPEN GAPS (= rows where NOT_PRESENT is marked in the assertion table above):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All assertions return PRESENT. No gaps.")

UNPLANNED (on disk, not in assertion table):
  + {filepath}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
(Derived from PRESENT marks in assertion table above. If OPEN GAPS is non-empty,
percent < 100%. If these contradict, recheck the assertion table.)

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
GAP-FIRST ORDERING -- THREE INDEPENDENT ENFORCEMENT LAYERS

[LAYER 1 -- STRUCTURAL (template position)]
ASSERTION TABLE and OPEN GAPS sections are positioned before COVERAGE in
this template. Template section order is structural and canonical. It is
enforced by physical placement: execution instructions cannot reorder
template sections without rewriting the template itself.

[LAYER 2 -- SEMANTIC (ordering principle)]
The coverage percentage is the count of PRESENT marks in the assertion table.
The gap list is the set of NOT_PRESENT marks. Both derive from the same
assertion table. Gaps must be enumerated first because coverage is their
mathematical complement. "The coverage number summarizes the gap list --
not the other way around."

[LAYER 3 -- EXECUTION (render sequence)]
Phase 4 render order: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE ->
COVERAGE -> TABLE -> READINESS -> NEXT.
Deviating from this sequence is a structural error. Correct before rendering.
=================================================================

EXECUTION PHASES -- compute the values to fill the output template above
------------------------------------------------------------------------

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
              State: "Signal plan not found -- assertion baseline is empty."
              Do not silently compute against zero.

===== PHASE 2: ASSERT (per signal -- no batch evaluation) =====
Gate: every entry in PLANNED receives exactly one verdict before Phase 3.

For each entry P in PLANNED, evaluate exactly one assertion:
  ASSERT: DISK contains a path matching *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

Do not skip any entry. Evaluate all planned signals individually.

After all assertions are complete:
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
Render order [LAYER 3]: ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE
  -> COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order defined in the template [LAYER 1].
The coverage number summarizes the gap list -- not the other way around [LAYER 2].

Phase 4 complete. No file was written.
```

---

### Criteria coverage matrix (v3 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Signal discovery | YES | YES | YES | YES | YES |
| C-02 Coverage percentage | YES | YES | YES | YES | YES |
| C-03 Gap identification | YES | YES | YES* | YES | YES |
| C-04 Display-only (stated) | YES | YES | YES | YES | YES |
| C-05 Readiness verdict | YES | YES | YES | YES | YES |
| C-06 Namespace breakdown | YES | YES | YES | YES | YES |
| C-07 Strategy cross-ref | YES | YES | YES | YES | YES |
| C-08 Recency awareness | YES | YES | YES | YES | YES |
| C-09 Actionable next step | YES | YES | YES | YES | YES |
| C-10 Structural table (template) | YES | YES | YES | YES | YES |
| C-11 Phase-gated disk-check | YES | YES | YES | YES | YES |
| C-12 Gap-first output ordering | YES+ | YES | YES | YES+ | YES |
| C-13 Triple-redundancy ordering | YES++ | NO | NO | YES++ | YES++ |
| C-14 Template-first absorption | YES | YES++ | NO | YES++ | YES++ |
| C-15 Per-signal assertion chain | YES | YES++ | NO | YES | YES++ |
| C-16 Consequence-framed verdict | YES | YES | YES++ | YES | YES++ |
| **Predicted score** | **130** | **128** | **118** | **132** | **135** |

`++` = primary axis treatment (strongest expression)
`+` = strong treatment, not the primary axis
`YES` = criterion met, floor-level treatment
`NO` = criterion absent or structurally ambiguous
`YES*` = C-03 may score partial -- "COMMIT RISKS" section title may or may not map to C-03 pass condition

---

### Predicted vs. actual divergence watch

**Most likely scoring surprises:**
- **C-03 in V-03:** The gap section is titled "COMMIT RISKS" not "OPEN GAPS". Pass condition requires "at least one gap section" with named namespace + signal type. If scorecard reads the title literally for section identification, V-03 may fail C-03. Risk is low but real.
- **C-13 in V-02:** V-02 does not have three labeled ordering layers. The NOTE block at the bottom of the template provides LAYER 2 (semantic), and the template position provides LAYER 1 (structural), but there is no explicit LAYER 3 (execution render sequence). C-13 likely fails for V-02.
- **C-14 in V-01:** V-01 puts the output template before the three-layer block and before the execution phases. Technically satisfies "template before execution instructions." But the three-layer block is between template and execution -- does it count as part of the template or part of the execution section? If scorecard reads the layer block as "execution-adjacent," V-01 still satisfies C-14. Low risk.
- **C-15 in V-03:** No per-signal assertion chain. Uses "For each P in PLAN: is there a path..." which is per-signal in behavior but not framed as an assertion chain with explicit NOT_PRESENT residual derivation. C-15 fails for V-03.
- **V-05 ceiling:** If all four `++` criteria hold, score = 135. Single failure on C-13 (if LAYER 2 -- the NOTE block -- is judged as "not a structurally distinct mechanism") drops to 130. The [LAYER 2 -- SEMANTIC] label and its explanation is the structural hedge.
