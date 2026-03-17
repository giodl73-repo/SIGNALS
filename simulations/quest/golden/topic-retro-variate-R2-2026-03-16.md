# topic-retro — Variations R2
**Date:** 2026-03-16
**Rubric:** v2 (C-01 through C-12; aspirational denominator = 4)
**R1 top scorers:** V-01 (Table-First, 100), V-03 (Echo-First, 100)
**New criteria to target:** C-11 (explicit numeric formula per namespace), C-12 (Echo before accuracy)

R1 analysis showed C-07 as sole discriminating criterion — V-04/V-05 collected per-namespace evidence but did not produce a labeled per-namespace score. R2 variations all embed the formula structurally (not optionally) and all place Echo before accuracy. Single-axis variations test whether the mechanism survives different stylistic and structural frames.

---

## V-01 — Phrasing Register: Imperative/Technical

**Axis:** Phrasing register — formal, imperative, engineering-spec style. Every instruction is a command with an explicit pass/fail output condition.

**Hypothesis:** Imperative register with checkable output conditions makes C-11 and C-12 compliance structural rather than stylistic. Each step has a named output artifact; missing the artifact is a visible failure, not a stylistic shortcut.

---

```
You are running a post-commitment retrospective on topic: $ARGUMENTS

PRECONDITION: Confirm a ship date or post-ship status exists for this topic. If the topic has not shipped, halt: "topic-retro cannot run on an unshipped topic."

AMEND: If $ARGUMENTS contains a scope constraint, output this before Phase A:
SCOPE APPLIED: [constraint]
All phases honor this constraint.

---

PHASE A — ECHO IDENTIFICATION
Execute before Phase B. Output must be committed before accuracy scoring begins.

Search simulations/{namespace}/ for all signal artifacts associated with this topic.

Identify THE ECHO: the single post-ship observable that satisfies all three conditions:
  (1) No artifact in the signal set predicted it
  (2) It was not a named risk or acknowledged unknown at commit time
  (3) It is only observable post-ship

Selection procedure:
  Step 1: List every post-ship outcome.
  Step 2: Cross each against signal predictions. Eliminate any that were predicted (even partially).
  Step 3: Eliminate any that were named unknowns or known risks.
  Step 4: From remaining candidates, select the one with highest decision impact.
  Step 5: If no candidates remain after elimination, state "No Echo — all post-ship outcomes were within signal bounds."

Echo record — required output:
  ECHO: [one sentence describing the unexpected finding]
  NEAREST SIGNAL: [artifact name, or "none"]
  DESIGN CHANGE: [one of — new skill: [name] | rubric amendment: [rubric + change] | threshold adjustment: [metric + new value] | new signal type not in catalog: [description]]

LOCK PHASE A. The Echo record must not be revised after Phase B runs.

---

PHASE B — SIGNAL INVENTORY

Produce the following table. Every row is a real artifact; no placeholder rows.

| Namespace | Artifact | Date | Signal Type | Prediction Summary |
|-----------|----------|------|-------------|-------------------|
| [name] | [filename] | [YYYY-MM-DD] | [type] | [one phrase] |

After the table:
  Total signals: N
  Empty namespaces (from: scout, draft, review, flow, trace, prove, listen, program, topic):
    [list each namespace with zero artifacts]

Failure condition: "No signals found" ends the retro. Signal inventory is not recoverable from memory.

---

PHASE C — PREDICTED VS ACTUAL

For each namespace with at least one artifact, produce:

  Namespace: [name]
  Predicted: [what the namespace's signals collectively claimed would happen post-ship]
  Actual: [what was observed post-ship in this domain]
  Match: CORRECT | PARTIAL | WRONG | NO-DATA

Rules:
  - Both Predicted and Actual must be explicitly stated. A match verdict without both sides fails.
  - CORRECT: prediction matched outcome in direction and magnitude.
  - PARTIAL: directionally correct but scope, timing, or magnitude was wrong.
  - WRONG: prediction did not match outcome.
  - NO-DATA: post-ship data not yet available.

---

PHASE D — GAP ANALYSIS

For each namespace that scored WRONG or PARTIAL in Phase C, and for each empty namespace from Phase B where absence is material:

  Gap: [signal type that was absent]
  Namespace: [which namespace should have produced it]
  Skill: [exact skill name — e.g., /listen-adoption, /flow-resilience — not generic advice]
  Would have caught: [one sentence — specific finding the signal would have surfaced]
  Commit impact: YES — would have changed the commit decision | NO — would have added context only

If no gaps exist: "No gaps — signal coverage was sufficient for this topic."

---

PHASE E — ACCURACY SCORING

Apply this formula to every namespace with match verdicts from Phase C:
  Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)
  Exclude NO-DATA entries from the denominator.
  If denominator is zero (all NO-DATA), leave Score blank.

Required output — produce this table:

| Namespace | Correct | Partial | Wrong | NO-DATA | Score (0-100) |
|-----------|---------|---------|-------|---------|---------------|
| [name]    |         |         |       |         | [formula]     |
| TOTAL     |         |         |       |         | [weighted avg]|

Overall verdict:
  STRONG: total score >= 75
  ADEQUATE: total score 50-74
  WEAK: total score < 50

State: "Signal accuracy for [topic]: [score]/100 — [STRONG/ADEQUATE/WEAK]"

Calibration trend:
  If prior retro exists for this topic or team: "[prior score] -> [current score]: [improving / degrading / stable]"
  If no prior retro: "First retro for this topic — no calibration baseline."
```

---

## V-02 — Output Format: Pure Table-Driven

**Axis:** Output format — every section is a table; no prose sections; column headers carry all structural requirements.

**Hypothesis:** Forcing all output into table format ensures per-namespace accuracy is always a labeled row (C-11 compliant by column header) and the Echo table precedes the accuracy table purely by document order (C-12 compliant by position). No narrative register can suppress a required column.

---

```
Run a topic-retro for: $ARGUMENTS

Every output section is a table. No prose sections, no narrative summaries. Column headers carry the requirements; cells carry the values. Output the tables in the order shown.

AMEND: If $ARGUMENTS contains a scope constraint, output this first before Table 1:
| Applied Scope |
|---------------|
| [AMEND constraint] |

---

TABLE 1 — ECHO
Output this table before any other table. Identifies the one post-ship finding no signal predicted.

Search all signal artifacts in simulations/{namespace}/ for this topic before completing this table.

| Echo (one post-ship finding not predicted by any signal and not a named unknown at commit time) | Nearest Signal | Commit Relevance: HIGH=would have stopped commit / MEDIUM=would have added conditions / LOW=informational | Design Change (exact skill name / rubric amendment + detail / threshold metric + new value / new signal type description) |
|--------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [finding, OR: "No Echo — all post-ship outcomes were within signal bounds"] | [artifact name or "none"] | HIGH / MEDIUM / LOW / N/A | [specific change, or "N/A" if no Echo] |

This table is locked. Do not revise it based on findings in Table 3 or Table 4.

---

TABLE 2 — SIGNAL INVENTORY
One row per artifact found in simulations/{namespace}/ for this topic.

| Namespace | Artifact | Date | Signal Type | Prediction Summary |
|-----------|----------|------|-------------|-------------------|
| [name] | [filename] | [YYYY-MM-DD] | [type] | [one phrase] |

| Coverage Summary |
|-----------------|
| Namespaces with signals: [list] |
| Empty namespaces: [list from scout, draft, review, flow, trace, prove, listen, program, topic] |
| Total signals: N |

---

TABLE 3 — PREDICTED VS ACTUAL
One row per namespace with signals. Both "Predicted" and "Actual" cells must be non-empty for every row.

| Namespace | Predicted (what signals said would happen post-ship) | Actual (what was observed post-ship) | Match: CORRECT / PARTIAL / WRONG / NO-DATA |
|-----------|------------------------------------------------------|--------------------------------------|--------------------------------------------|
| [name] | [required — cannot be blank] | [required — cannot be blank] | [verdict] |

---

TABLE 4 — ACCURACY BY NAMESPACE
Formula: Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)
NO-DATA entries are excluded from the denominator. Leave Score blank if denominator = 0.

| Namespace | Correct | Partial | Wrong | NO-DATA | Score: (C*100+P*50)/(C+P+W) |
|-----------|---------|---------|-------|---------|------------------------------|
| [name] | | | | | |
| TOTAL | | | | | [weighted avg] |

| Verdict | Prior Retro Score | Calibration Trend |
|---------|-------------------|-------------------|
| STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50) | [score or "N/A — first retro"] | [improving / degrading / stable / "N/A — first retro"] |

---

TABLE 5 — GAPS
One row per missing signal that would have changed a match verdict in Table 3, or per empty namespace where absence is material.
If no gaps: one row with "No gaps — coverage was sufficient" in the Gap column; remaining cells blank.

| Gap (signal type that was absent) | Namespace | Skill (exact name e.g. /listen-adoption) | Would Have Caught (one sentence) | Changed Commit Decision? YES / NO |
|-----------------------------------|-----------|------------------------------------------|----------------------------------|-----------------------------------|
| [type or "No gaps — coverage was sufficient"] | | | | |

---

Output only these five tables in order (Table 1 through Table 5). No text before Table 1 (except Applied Scope if AMEND is present). No text after Table 5.
```

---

## V-03 — Lifecycle Emphasis: Strict Phase Gates

**Axis:** Lifecycle emphasis — heavy phase boundary enforcement with explicit COMMIT gates and revision prohibitions at each boundary.

**Hypothesis:** COMMIT gates at each phase boundary prevent late-phase findings from contaminating early-phase outputs. The Echo-commit gate (after Phase 2, before Phase 3) structurally enforces C-12; the formula mandate in Phase 5 structurally enforces C-11. Testing whether explicit gate language produces higher C-11/C-12 compliance than structural position alone (V-01, V-02).

---

```
Topic retrospective for: $ARGUMENTS

This retro runs in five phases with commit gates. Each phase must be completed before the next begins. Output each phase block in sequence, gate line included.

AMEND: If $ARGUMENTS contains a scope constraint, state it before Phase 1:
>> SCOPE APPLIED: [constraint]
All phases operate within this scope.

---

[PHASE 1 — SIGNAL INVENTORY]

Search simulations/{namespace}/ for all artifacts associated with this topic.

Produce:
  Artifact list: [namespace] / [artifact filename] / [date] / [one-phrase prediction summary]

Then produce coverage summary:
  Namespaces with at least one artifact: [list]
  Namespaces with no artifacts (from: scout, draft, review, flow, trace, prove, listen, program, topic): [list]
  Total artifacts: N

>> COMMIT PHASE 1. The inventory is now fixed. Do not add or remove artifacts in later phases.

---

[PHASE 2 — ECHO IDENTIFICATION]

Using only the artifacts listed in Phase 1, identify THE ECHO.

The Echo is the single post-ship observable that:
  - Appears in no prediction from any Phase 1 artifact
  - Was not a named risk or known unknown at commit time
  - Is only observable after shipping

Step 1 — List every post-ship outcome for this topic.
Step 2 — Cross each against Phase 1 predictions. Mark each as: Predicted | Partial | Unpredicted.
Step 3 — From Unpredicted outcomes, eliminate any that were named risks or known unknowns.
Step 4 — From remaining candidates, select exactly one with the highest decision impact as the Echo.
  If no candidates remain: "No Echo — all post-ship outcomes were within signal bounds."

Echo record:
  ECHO: [one sentence describing the finding]
  NEAREST SIGNAL: [Phase 1 artifact name that came closest, or "none"]
  DESIGN CHANGE: [one of: new skill [name] | rubric amendment [rubric + specific change] | threshold adjustment [metric + new value] | new signal type not in namespace catalog [description]]

>> COMMIT PHASE 2. The Echo record is locked. Do not revise it after Phase 3 runs. If Phase 3 analysis would change the Echo, note the tension but preserve the Phase 2 record.

---

[PHASE 3 — PREDICTED VS ACTUAL]

For each namespace from Phase 1 that has at least one artifact:

  Namespace: [name]
  Predicted: [what this namespace's artifacts collectively predicted would happen post-ship]
  Actual: [what was observed post-ship in this domain]
  Match: CORRECT | PARTIAL | WRONG | NO-DATA

Both Predicted and Actual must be explicitly stated for every namespace. A match verdict without both sides is a failure of this phase.

>> COMMIT PHASE 3. Match verdicts are fixed. Do not revise them based on Phase 4 analysis.

---

[PHASE 4 — GAP ANALYSIS]

Review every namespace that scored WRONG or PARTIAL in Phase 3.
Also review each namespace listed as "no artifacts" in Phase 1 where absence is material.

For each gap:
  Gap: [signal type that was absent]
  Namespace: [which of the nine namespaces should have produced it]
  Skill: [exact skill name, e.g., /scout-compliance, /trace-state — not generic advice such as "run more tests"]
  Would have caught: [one sentence — what the signal would have surfaced]
  Commit impact: YES — would have changed the commit decision | NO — would have added context only

If there are no gaps: "No gaps — signal coverage was sufficient for this topic."

>> COMMIT PHASE 4. Gap list is fixed.

---

[PHASE 5 — ACCURACY SCORING]

Apply this formula to every namespace with match verdicts from Phase 3:
  Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)
  NO-DATA entries are excluded from the denominator.
  If denominator = 0 (all NO-DATA), leave Score blank.

C = Correct count, P = Partial count, W = Wrong count, N = NO-DATA count

Required table:
  | Namespace | C | P | W | N | Score: (C*100+P*50)/(C+P+W) |
  |-----------|---|---|---|---|-----------------------------|
  | [name]    |   |   |   |   | [apply formula]             |
  | TOTAL     |   |   |   |   | [weighted average]          |

Overall verdict:
  STRONG: total score >= 75
  ADEQUATE: total score 50-74
  WEAK: total score < 50

State: "Signal accuracy for [topic]: [score]/100 — [STRONG/ADEQUATE/WEAK]"

Calibration trend:
  If prior retro data exists for this topic or team:
    "Prior retro score: [N]. Current: [N]. Trend: [improving / degrading / stable]."
  If this is the first retro:
    "First retro for this topic — this score becomes the baseline."

>> COMMIT PHASE 5. Retro complete.
```

---

## V-04 — Role Sequence: Three-Voice Protocol

**Variation axes combined:** Role sequence + lifecycle emphasis

**Hypothesis:** Three named roles with strict handoff contracts — Archivist (inventory only), Echo Finder (surprise only), Scorer (accuracy + verdict) — compound role-sequence and phase-gate axes. The Scorer receiving a locked Echo record from the Echo Finder structurally enforces C-12 at the role boundary. The Scorer's formula-only accuracy method enforces C-11. Testing whether role-as-persona framing sustains the structural constraints more reliably than phase-as-step framing.

---

```
Run topic-retro for: $ARGUMENTS

Three roles execute in sequence. Each role receives only what prior roles produced. Roles cannot revise each other's output.

AMEND: If $ARGUMENTS contains a scope constraint, state it before Role 1:
SCOPE: [constraint]
All three roles operate within this scope.

---

ROLE 1 — THE ARCHIVIST

The Archivist records. The Archivist does not interpret, assess, or predict.

Task: Search simulations/{namespace}/ for all artifacts associated with this topic. Produce a complete and accurate inventory.

Signal Registry:
| Namespace | Artifact | Date | Prediction Summary (one phrase) |
|-----------|----------|------|---------------------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

Coverage:
  Namespaces with at least one artifact: [list]
  Namespaces with no artifacts (from: scout, draft, review, flow, trace, prove, listen, program, topic): [list]
  Total artifacts in registry: N

The Archivist's output is the Signal Registry. Hand off to Role 2.

---

ROLE 2 — THE ECHO FINDER

The Echo Finder receives: Signal Registry (from Role 1).
The Echo Finder identifies what the signals collectively failed to predict.
The Echo Finder does not compute accuracy. The Echo Finder does not assess gaps.

Task:
  Step 1 — Read the Signal Registry. For each namespace, compile the full set of predictions made.
  Step 2 — Identify post-ship observable outcomes for this topic.
  Step 3 — Find THE ECHO: the single post-ship observable that:
    (a) Appears in no prediction from Step 1
    (b) Was not a named risk or known unknown at commit time
    (c) Is only observable after shipping
  Step 4 — If multiple candidates, select the one with highest decision impact.
  Step 5 — If no candidates qualify, state "No Echo — all post-ship outcomes were within signal bounds."

Echo Record (locked before Role 3 runs):
  ECHO: [one sentence describing the unexpected finding]
  NEAREST SIGNAL: [artifact name from the Signal Registry that came closest, or "none"]
  COMMIT RELEVANCE: HIGH (would have stopped the commit) | MEDIUM (would have added conditions) | LOW (informational)
  DESIGN CHANGE: [one specific change — skill: [name] | rubric amendment: [rubric + change detail] | threshold adjustment: [metric + new value] | new signal type: [description]]

The Echo Record is final. Role 3 may not revise it. If Role 3 analysis would change the Echo, note the tension in Role 3 output but preserve the Echo Record as stated.

Hand off to Role 3: Signal Registry (from Role 1) + Echo Record (from Role 2).

---

ROLE 3 — THE SCORER

The Scorer receives: Signal Registry (from Role 1) + Echo Record (from Role 2).
The Scorer may not revise the Echo Record.

Step A — Predicted vs Actual
For each namespace with artifacts in the Signal Registry:
  Namespace: [name]
  Predicted: [what this namespace's signals collectively said would happen post-ship]
  Actual: [what was observed post-ship in this domain]
  Match: CORRECT | PARTIAL | WRONG | NO-DATA
Both Predicted and Actual must be explicitly stated. A match verdict without both sides is not acceptable.

Step B — Gap Analysis
For each namespace that scored WRONG or PARTIAL in Step A, and for each namespace with no artifacts where absence is material:
  Gap: [signal type that was missing]
  Namespace: [which namespace should have produced it]
  Skill: [exact skill name, e.g., /listen-adoption, /flow-resilience — not generic advice]
  Would have caught: [one sentence — specific finding the skill would have surfaced]
  Commit impact: YES — would have changed the decision | NO — would have added context only
If no gaps: "No gaps — signal coverage was sufficient."

Step C — Accuracy Table
Apply formula: Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)
Exclude NO-DATA from denominator. Leave Score blank if denominator = 0.

| Namespace | Correct | Partial | Wrong | NO-DATA | Score: (C*100+P*50)/(C+P+W) |
|-----------|---------|---------|-------|---------|------------------------------|
| [name]    |         |         |       |         | [apply formula]              |
| TOTAL     |         |         |       |         | [weighted average]           |

Step D — Verdict
Overall: STRONG (>=75) | ADEQUATE (50-74) | WEAK (<50)
State: "Signal accuracy for [topic]: [score]/100 — [verdict]"

Calibration:
  Prior retro data available: "[prior score] -> [current score]: [improving / degrading / stable]"
  No prior retro: "No prior retro for comparison — this score becomes the baseline."

---

Final output order: Echo Record (Role 2) then Signal Registry (Role 1) then Step A through Step D (Role 3).
```

---

## V-05 — Inertia Framing: Commit-Decision Anchor

**Variation axes combined:** Inertia framing + echo-first + explicit formula

**Hypothesis:** Anchoring every section to the commit-decision counterfactual ("would this have changed the commit?") naturally enforces Echo-before-accuracy (C-12) because a truly unexpected post-ship finding is definitionally outside the commit frame and must be named before the commit frame is assessed. The commit-confidence framing also forces formula-based per-namespace scoring (C-11) because namespace reliability maps directly to decision confidence — a qualitative verdict is insufficient when commit impact must be quantified. Tests whether the decision-impact anchor alone is a sufficient structural generator for C-11 and C-12, or requires additional explicit gates.

---

```
Post-commitment retrospective for topic: $ARGUMENTS

Central question: "Given what we learned after shipping, how well did our signals prepare us for the commit decision?"

AMEND: If $ARGUMENTS specifies a scope constraint, output this as the first line:
APPLIED SCOPE: [constraint]
All sections stay within that scope.

---

SECTION 0 — THE THING WE DIDN'T SEE COMING

Before scoring what we predicted correctly, name what we completely missed.

The Echo is the post-ship observable that satisfies all three tests:
  Test 1: No gathered signal predicted it (not even partially)
  Test 2: It was not a named risk or acknowledged unknown at commit time
  Test 3: It could only be known after shipping — not beforehand

Search simulations/{namespace}/ for all signal artifacts for this topic. Then:
  Step 1: List every post-ship outcome for this topic.
  Step 2: Apply the three tests. Eliminate any outcome that fails any test.
  Step 3: From qualifying outcomes, select exactly one — the highest commit-impact finding — as the Echo.
  Step 4: If no outcome passes all three tests, state "No Echo — all post-ship outcomes were anticipated or within known risk bounds."

Echo entry:
  WHAT: [one sentence describing the unexpected finding]
  NEAREST SIGNAL: [which signal came closest to predicting it, or "none"]
  COMMIT RELEVANCE: HIGH (would have stopped the commit) | MEDIUM (would have added conditions) | LOW (informational only)
  DESIGN CHANGE: [one specific, typed change — skill: [exact name] | rubric amendment: [rubric + change detail] | threshold adjustment: [metric + new value] | new signal type not in namespace catalog: [description]]

This Echo entry is final. Do not revise it after Section 2 runs.

---

SECTION 1 — WHAT WE HAD AT COMMIT TIME

List all signal artifacts gathered for this topic, grouped by namespace.

For each namespace with artifacts:
  [Namespace] (N signals)
    - [artifact filename] — [date] — [one-phrase prediction summary]

Empty namespaces (none of the nine — scout, draft, review, flow, trace, prove, listen, program, topic — should be unlisted; name all that have zero artifacts):
  [list]

Signal coverage tier:
  SIGNAL-RICH: 6 or more namespaces with artifacts
  ADEQUATE: 4-5 namespaces
  SPARSE: 1-3 namespaces
  DARK: 0 namespaces

State: "Coverage tier: [tier] ([N] of 9 namespaces with signals)"

---

SECTION 2 — DID OUR SIGNALS TELL US THE TRUTH?

For each namespace with at least one artifact, assess prediction accuracy.

Namespace: [name]
The signals predicted: [what they collectively claimed would happen post-ship — required, must be explicit]
What actually happened: [post-ship observation — required, must be explicit]
Match: CORRECT | PARTIAL | WRONG | NO-DATA
Commit relevance: [was this namespace's prediction load-bearing for the commit decision? YES / NO]

Then compute per-namespace accuracy using this formula:
  Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)
  NO-DATA entries are excluded from the denominator.
  Leave Score blank if all entries in a namespace are NO-DATA.

Accuracy table:
  | Namespace | Correct | Partial | Wrong | NO-DATA | Score: (C*100+P*50)/(C+P+W) | Commit-Load-Bearing |
  |-----------|---------|---------|-------|---------|------------------------------|---------------------|
  | [name]    |         |         |       |         | [apply formula]              | YES / NO            |
  | TOTAL     |         |         |       |         | [weighted average]           |                     |

Overall verdict:
  STRONG: total score >= 75
  ADEQUATE: total score 50-74
  WEAK: total score < 50

State: "Signal accuracy for [topic]: [score]/100 — [STRONG/ADEQUATE/WEAK]"

Calibration:
  If prior retro data exists: "[prior score] -> [current score]: [improving / degrading / stable]"
  If first retro: "First retro for this topic — this score is the baseline."

---

SECTION 3 — WHAT WE SHOULD HAVE RUN

For each namespace that was empty at commit time, and for each namespace that scored WRONG or PARTIAL in Section 2, assess the gap.

Gap: [signal type that was absent]
Namespace: [which of the nine namespaces]
Skill to run: [exact skill name — e.g., /listen-adoption, /scout-compliance — not "gather more data"]
Would have surfaced: [one sentence — specific finding]
Commit impact: YES — would have changed the commit decision | NO — would have added context only
Inertia check: Given actual team capacity at commit time, was skipping this signal reasonable? YES / NO + one sentence.

Tier the gaps by commit impact:
  Tier 1 — Commit-blockers (Commit impact = YES): [list]
  Tier 2 — Confidence builders (Commit impact = NO): [list]

If no gaps exist: "No gaps identified — signal coverage was sufficient for this commit decision."

---

Output order: Section 0 (Echo) -> Section 1 (Inventory) -> Section 2 (Accuracy) -> Section 3 (Gaps)
```

---

## Summary Table

| ID | Axis | Primary Mechanism for C-11 | Primary Mechanism for C-12 | Hypothesis Tested |
|----|------|----------------------------|----------------------------|--------------------|
| V-01 | Phrasing register (imperative/technical) | Formula stated in Phase E instruction as required output | Phase A = first phase; "LOCK PHASE A" before Phase B | Imperative commands with explicit pass/fail conditions prevent formula and ordering shortcuts |
| V-02 | Output format (pure table-driven) | Formula in Table 4 column header; column enforces computation | Table 1 (Echo) precedes Table 4 (Accuracy) by document position | Table-only format makes per-namespace score a required column; position enforces ordering |
| V-03 | Lifecycle emphasis (strict phase gates) | Formula mandated in Phase 5 instruction | COMMIT gate after Phase 2 before Phase 3; revision prohibition explicit | COMMIT gates at each boundary prevent inter-phase contamination and enforce ordering |
| V-04 | Role sequence (three-voice protocol) + lifecycle | Scorer's formula-only accuracy method in Step C | Echo Finder role completes before Scorer role; "Role 3 may not revise" | Role-as-persona framing sustains structural constraints as reliably as phase-as-step framing |
| V-05 | Inertia framing (commit-decision anchor) + formula + echo-first | Formula in Section 2 accuracy table; commit-confidence framing requires quantification | Section 0 (Echo) explicitly before Section 2 (Accuracy); "do not revise after Section 2 runs" | Decision-impact anchor naturally generates Echo-first and formula-accuracy without needing phase gates |
