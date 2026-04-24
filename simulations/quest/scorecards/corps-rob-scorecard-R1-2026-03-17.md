Scorecard written to `simulations/quest/scorecards/corps-rob-scorecard-R1-2026-03-17.md`.

---

```json
{"top_score": 97.5, "all_essential_pass": true, "new_patterns": ["handoff-packet-at-stage-close", "stage-boundary-blocker-detection", "inertia-anchor-per-stage-check"]}
```
----------|--------|-----------|-----|-----|
| V-04 Inertia + Lifecycle | 97.5 | YES | 5/5 | 3/3 | 1.5/2 |
| V-05 Scorecard + Ledger | 95.0 | YES | 5/5 | 3/3 | 1/2 |
| V-02 Compact Single-Line | 90.0 | YES | 5/5 | 3/3 | 0/2 |
| V-01 Bottom-Up Sequence | 85.0 | YES | 5/5 | 2.5/3 | 0/2 |
| V-03 Workshop Facilitation | 85.0 | YES | 5/5 | 2.5/3 | 0/2 |

All 5 variations pass golden threshold (all essential pass, composite >= 80).

---

## Criterion Scores by Variation

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Stage identity | PASS | PASS | PASS | PASS | PASS |
| C-02 | Role-loaded perspective | PASS | PASS | PASS | PASS | PASS |
| C-03 | ROB document format | PASS | PASS | PASS | PASS | PASS |
| C-04 | Actionable findings | PASS | PASS | PASS | PASS | PASS |
| C-05 | TPM go/no-go | PASS | PASS | PASS | PASS | PASS |
| C-06 | Risk register structure | PASS | PASS | PASS | PASS | PASS |
| C-07 | Exec-office mission cascade | PASS | PASS | PASS | PASS | PASS |
| C-08 | Cross-stage coherence | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-09 | Inter-stage blocker detection | FAIL | FAIL | FAIL | PASS | FAIL |
| C-10 | Cross-cutting theme elevation | FAIL | FAIL | FAIL | PARTIAL | PASS |

---

## Detailed Evidence

### V-01 -- Role Sequence: Bottom-Up

- **C-08 PARTIAL**: Leadership stage mandates 1 upstream reference by ID (confirms/escalates/resolves). No mechanism for a second reference. Rubric requires 2+.
- **C-09 FAIL**: No blocker detection mechanism at stage boundaries.
- **C-10 FAIL**: No document-level theme section.

Score: E=60 + R=(2.5/3 * 30)=25 + A=0 = **85**

### V-02 -- Output Format: Compact Single-Line

- **C-08 PASS**: Explicit "at least 2 findings across the full run must reference a prior stage by name and finding ID" requirement. Count specified, format specified.
- **C-09 FAIL**: No blocker detection mechanism.
- **C-10 FAIL**: No document-level theme section.

Score: E=60 + R=30 + A=0 = **90**

### V-03 -- Phrasing Register: Workshop Facilitation

- **C-08 PARTIAL**: "When a later reviewer's finding confirms, escalates, or contradicts something from an earlier stage, say so" -- conditional language ("may have heard about", "when"). No minimum count. Not structurally guaranteed.
- **C-09 FAIL**: No blocker detection mechanism.
- **C-10 FAIL**: No document-level theme section.

Score: E=60 + R=(2.5/3 * 30)=25 + A=0 = **85**

### V-04 -- Inertia Framing + Lifecycle Emphasis

- **C-08 PASS**: STEP 3 (Cross-Stage References) is a mandatory section from Stage 2 onward; minimum 2 cross-stage references required. Structurally guaranteed in a full run.
- **C-09 PASS**: BLOCKER: YES/NO field in HANDOFF PACKET at every stage close; names F-ID, downstream stage, and reason. Satisfies all 4 C-09 pass elements. Located at stage boundary, not retroactively.
- **C-10 PARTIAL**: ROB Summary consolidates INERTIA STATUS and BLOCKERS RAISED at document level. No explicit "Cross-Cutting Themes" section naming recurrence patterns with elevated-severity explanation. Approaches C-10 but does not structurally guarantee it.

Score: E=60 + R=30 + A=(1.5/2 * 10)=7.5 = **97.5**

### V-05 -- Per-Stage Scorecard + Escalation Ledger

- **C-08 PASS**: Escalation Ledger after all stages; minimum 2 threads; cross-references specific finding IDs across stages; requires explanation of why multi-stage recurrence increases severity.
- **C-09 FAIL**: Escalation Ledger is post-hoc (document end). C-09 requires "identified at the stage boundary where they arise, not discovered retroactively." Ledger pattern field (escalating/stable/mixed) does not structurally distinguish blocking from non-blocking threads.
- **C-10 PASS**: Escalation Ledger is document-level (not inside any stage), cites 2+ stages per thread, requires severity-elevation explanation -- matches C-10 pass condition.

Score: E=60 + R=30 + A=(1/2 * 10)=5 = **95**

---

## Excellence Signals -- V-04

V-04 achieves the highest score by being the only variation to cleanly satisfy C-09 (inter-stage blocker detection) while maintaining full essential and recommended coverage.

**Pattern 1 -- Handoff packet at stage close (C-08 generator)**
STEP 3 (Cross-Stage References) is a mandatory section from Stage 2 onward. Every stage must scan prior findings and write explicit confirm/escalate/contradict entries. C-08 is no longer dependent on model recall -- the structure produces it. Guarantees 5+ cross-stage references in a full 6-stage run.

**Pattern 2 -- Stage-boundary blocker detection (C-09 satisfaction)**
BLOCKER: YES/NO field in HANDOFF PACKET at every stage close. Named at the stage boundary where the blocker arises, satisfying C-09's "not retroactively" requirement. No other variation places a blocker-detection mechanism at this point.

**Pattern 3 -- Inertia anchor + per-stage check (C-02 enrichment)**
INERTIA ANCHOR before Stage 1 establishes what the topic displaces and who bears the cost. Each INERTIA CHECK (STEP 1 of every stage) forces the role to articulate the status-quo pressure from their own perspective before writing findings. Grounds C-02 in role-specific context without requiring additional findings.

**Why V-05 finishes second**
The Escalation Ledger is the cleanest C-10 mechanism in the set and achieves full recommended tier. V-05 fails only C-09 (post-hoc ledger vs. stage-boundary detection). Adding a per-stage BLOCKER field to V-05 would challenge V-04 for top position.

**Why V-02 finishes third**
Compact format is the most reliable for C-03/C-04 structural compliance and the only single-axis variation to guarantee C-08 (explicit count requirement). Zero aspirational coverage -- the format leaves no room for cross-document mechanisms.

---

## New Patterns for Golden Candidate

| Pattern | Mechanism | Criterion Unlocked |
|---------|-----------|-------------------|
| Handoff packet at stage close | STEP 4: PASSING TO + BLOCKER: YES/NO | C-08 (guaranteed), C-09 (stage-boundary) |
| Stage-boundary blocker detection | BLOCKER field in HANDOFF PACKET | C-09 |
| Inertia anchor + per-stage check | INERTIA ANCHOR block + INERTIA CHECK in STEP 1 | C-02 enrichment |
