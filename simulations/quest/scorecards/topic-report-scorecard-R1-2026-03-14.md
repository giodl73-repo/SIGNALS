**Round 1 Scorecard — topic-report**

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 Combined | 5/5 | 3/3 | 2/2 | **100** | YES |
| 2 | V-02 Section-locked | 5/5 | 3/3 | 1/2 | **95** | YES |
| 2 | V-03 Lifecycle | 5/5 | 3/3 | 1/2 | **95** | YES |
| 2 | V-04 Question-framed | 5/5 | 3/3 | 1/2 | **95** | YES |
| 5 | V-01 Baseline | 5/5 | 3/3 | 0/2 | **90** | YES |

**The single discriminator: C-09.** Only V-05 passes it. The BLOCKERS phase forces essential OPEN signals to be named as a locked list before the readiness statement is written — SLOT 3 then requires the sentence to reference that list by name. No other variation achieves this.

**C-10** further splits V-01 from the cluster: V-01 only prohibits headers and fenced code; the others explicitly enumerate backticks and angle brackets (V-02, V-04, V-05) or use a catch-all "no markdown syntax" (V-03).

**All five variations are golden** — the essential structure (write + echo, table + counts, open list + owners, readiness, concrete next step) is fully specified even in the baseline. The variations improve *reliability* of those criteria in live runs, not rubric score.

**Recommended golden: V-05.** Two new patterns surface for the broader rubric library:

1. **BLOCKERS phase before readiness** — pre-computing a named list and requiring the readiness sentence to cite it is the necessary and sufficient design pattern for C-09 across any skill that has a readiness statement.
2. **Explicit character enumeration vs. catch-all** — "no backticks, no angle brackets" outperforms "no markdown syntax" for Teams paste-readiness because models may interpret catch-alls narrowly.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["BLOCKERS phase before readiness is the only reliable path to C-09 — pre-computing and naming essential OPEN signals as a locked list before the readiness statement is written, then requiring the sentence to reference that list by name, is the necessary and sufficient design pattern", "Explicit character enumeration (no backticks, no angle brackets) outperforms catch-all prohibition (no markdown syntax) for Teams card paste-readiness — models may interpret catch-alls narrowly while still emitting inline code fences or angle-bracket variable notation"]}
```
" — both fields required |
| C-09 | Readiness names blocking signals | FAIL | Readiness is "one sentence of justification" — no instruction to name specific blocking signals |
| C-10 | Teams card paste-ready | FAIL | Prohibits "markdown headers" and "fenced code blocks" only; backticks and angle brackets not enumerated |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 0/2

```
composite = (5/5 * 60) + (3/3 * 30) + (0/2 * 10)
          = 60 + 30 + 0
          = 90
```

**Score: 90 / 100 — GOLDEN**

---

### V-02: Section-locked template

Hard SLOT 1–4 structure with explicit acceptance criteria per slot. Adds verification pause and complete Teams prohibition list.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction + "PHASE 3: CONFIRM" echo |
| C-02 | Progress table with accurate counts | PASS | "Pause. Verify your counts once before writing. Recount if uncertain." + SLOT 1 Total row |
| C-03 | Open signals listed with owners | PASS | SLOT 2: "Each item must include: namespace, skill type, owner (e.g., unassigned)" |
| C-04 | Readiness statement calibrated | PASS | SLOT 3 consistency rule: "if total_open > 0 for any essential signal, status cannot be 'Ready'" |
| C-05 | Recommended next step present | PASS | SLOT 4: "Name the specific skill to run and the namespace. Generic next steps fail this slot." |
| C-06 | --format teams compact ASCII | PASS | Explicit rules: "No markdown headers (#, ##, ###)", "No fenced code blocks (no backtick sequences)", "No angle brackets", max 40 lines / 80 chars |
| C-07 | Matches topic-status output | PASS | Same discovery logic; no parity note but process is identical |
| C-08 | Open signals include namespace + type | PASS | SLOT 2: "namespace (e.g., prove), skill type (e.g., prove-analysis)" — canonical examples given |
| C-09 | Readiness names blocking signals | FAIL | SLOT 3 "Then one sentence" has no requirement to name specific signal types |
| C-10 | Teams card paste-ready | PASS | "No fenced code blocks (no backtick sequences)", "No angle brackets" — explicit enumeration passes C-10 |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/2 (C-10 passes, C-09 fails)

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Score: 95 / 100 — GOLDEN**

---

### V-03: Lifecycle emphasis (discover-then-render)

Strongest C-02/C-04 mechanism through explicit CHECKPOINT gate before any prose. C-10 relies on "no markdown syntax" catch-all rather than enumeration.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | "Default format — write simulations/{topic}/status-{date}.md" + "PHASE 3: CONFIRM" |
| C-02 | Progress table with accurate counts | PASS | Step 1.4 CHECKPOINT forces count statement before PHASE 2 begins; "Using only the locked counts from PHASE 1" |
| C-03 | Open signals listed with owners | PASS | "List each OPEN signal. Include: namespace, skill type, owner. Use 'unassigned' if unknown." |
| C-04 | Readiness statement calibrated | PASS | "Derive directly from locked counts — do not re-evaluate from scratch." + essential-open rule |
| C-05 | Recommended next step present | PASS | "One concrete action: skill name + namespace. Prioritize by: essential OPEN first." |
| C-06 | --format teams compact ASCII | PASS | "No markdown syntax. Max 40 lines / 80 chars. Use plain pipes and dashes." |
| C-07 | Matches topic-status output | PASS | Same discovery logic; locked counts from PHASE 1 are ground truth |
| C-08 | Open signals include namespace + type | PASS | "Include: namespace, skill type, owner" |
| C-09 | Readiness names blocking signals | FAIL | Readiness "Derive directly from locked counts" — no instruction to name specific signals |
| C-10 | Teams card paste-ready | PASS* | "No markdown syntax" is a catch-all that covers backticks and angle brackets; less explicit than V-02/V-04/V-05 but sufficient for PASS |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/2 (C-10 passes, C-09 fails)

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Score: 95 / 100 — GOLDEN**

Note: V-03's CHECKPOINT (Step 1.4) is the strongest count-accuracy mechanism among all five variations. C-02/C-04 failure probability is lowest here. However, "no markdown syntax" is a broader prohibition than V-02's explicit enumeration — in live model runs, V-02's enumeration may be more reliable for C-10.

---

### V-04: Phrasing register (question-framed)

Q1–Q5 self-check framing. Explicit backtick + angle bracket prohibition in teams branch. No blocker-naming instruction.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | "Write simulations/{topic}/status-{date}.md using your answers above." + "Finish with: 'Report written to...'" |
| C-02 | Progress table with accurate counts | PASS | Q3 requires explicit count statement before writing; table structure uses Q2/Q3 answers as source |
| C-03 | Open signals listed with owners | PASS | Q3: "list each open signal: namespace, skill type, owner" — three fields required |
| C-04 | Readiness statement calibrated | PASS | Q4 reasoning: "If yes: the topic is not ready (or conditionally ready if close). State your readiness label." Calibration is forced through Q4 logic |
| C-05 | Recommended next step present | PASS | Q5: "Name the skill and namespace." File section: "One sentence. Specific skill and namespace." |
| C-06 | --format teams compact ASCII | PASS | "No backticks, no # headers, no angle brackets. Max 40 lines. Max 80 chars per line." |
| C-07 | Matches topic-status output | PASS | Same discovery logic through Q1–Q2 |
| C-08 | Open signals include namespace + type | PASS | Q3: "namespace, skill type, owner" — same three fields |
| C-09 | Readiness names blocking signals | FAIL | Q4 "State your readiness label and one sentence justification" — no instruction to name specific signal types |
| C-10 | Teams card paste-ready | PASS | "No backticks, no # headers, no angle brackets" — explicit enumeration matches C-10 requirement |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/2 (C-10 passes, C-09 fails)

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Score: 95 / 100 — GOLDEN**

---

### V-05: Combined (section-locked + discover-first + blocker-naming)

Three-phase execution: DISCOVER → BLOCKERS → RENDER. The BLOCKERS phase names essential OPEN signals explicitly; SLOT 3 is required to reference that list by name.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | PHASE 3 writes file + "PHASE 4: CONFIRM" echos path |
| C-02 | Progress table with accurate counts | PASS | 1d CHECKPOINT: "state before continuing: 'DISCOVER: {total_done}/{total_planned}'" + SLOT 1: "Values from PHASE 1 only — do not re-derive" |
| C-03 | Open signals listed with owners | PASS | SLOT 2: "Each entry: namespace/skill (owner)" with owner="unassigned" if unknown |
| C-04 | Readiness statement calibrated | PASS | SLOT 3 consistency enforced through BLOCKERS list: "If BLOCKERS is empty: 'Ready — all essential signals are present.'" Cannot say Ready if BLOCKERS is non-empty |
| C-05 | Recommended next step present | PASS | SLOT 4: "Must name skill and namespace. Source: highest-priority entry from SLOT 2. Generic steps are not acceptable." |
| C-06 | --format teams compact ASCII | PASS | "No markdown headers, no fenced code, no backticks, no angle brackets. Max 40 lines / 80 chars. Table borders: + - | only." Most explicit prohibition list of all five variations. |
| C-07 | Matches topic-status output | PASS | Same discovery logic; CHECKPOINT-locked counts are ground truth |
| C-08 | Open signals include namespace + type | PASS | SLOT 2: "namespace/skill (owner)" — namespace and skill combined in format |
| C-09 | Readiness names blocking signals | PASS | SLOT 3: "The sentence must reference the BLOCKERS list from PHASE 2 by name. Example: 'Not ready — missing prove-analysis (prove) and review-design (review).'" Explicit instruction + example. |
| C-10 | Teams card paste-ready | PASS | "No markdown headers, no fenced code, no backticks, no angle brackets" — explicit enumeration + "Table borders: + - | only" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2

```
composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-09 mechanism | C-10 mechanism |
|------|-----------|-----------|-------------|--------------|-----------|---------|----------------|----------------|
| 1 | V-05 Combined | 5/5 | 3/3 | 2/2 | **100** | YES | BLOCKERS phase + "must reference by name" | explicit enumeration (backticks + angle brackets) |
| 2 | V-02 Section-locked | 5/5 | 3/3 | 1/2 | **95** | YES | none | explicit enumeration |
| 2 | V-03 Lifecycle | 5/5 | 3/3 | 1/2 | **95** | YES | none | catch-all ("no markdown syntax") |
| 2 | V-04 Question-framed | 5/5 | 3/3 | 1/2 | **95** | YES | none | explicit enumeration |
| 5 | V-01 Baseline | 5/5 | 3/3 | 0/2 | **90** | YES | none | incomplete (headers+code only) |

**C-09 is the sole full-point discriminator.** Only V-05 passes it, through the BLOCKERS phase design. All other variations leave blocker-naming as implicit.

**C-10 further separates V-01 from the cluster.** V-01 only prohibits headers and fenced code; V-02, V-04, and V-05 explicitly enumerate backticks and angle brackets; V-03 uses "no markdown syntax" as a catch-all.

---

## Excellence Signals — Round 1

### E-1: BLOCKERS phase is the only reliable path to C-09

V-05 introduces a dedicated PHASE 2 (BLOCKERS) between discover and render. The model must enumerate essential OPEN signals by name as a separate step *before* writing the readiness statement, and SLOT 3 explicitly requires citing that list. No other variation achieves this — all others produce readiness statements from reasoning alone, not from a named list. **BLOCKERS phase design is the necessary condition for C-09.**

### E-2: Explicit character enumeration outperforms catch-all for Teams card safety

V-02, V-04, and V-05 explicitly name the prohibited characters (backticks, angle brackets) rather than issuing a catch-all ("no markdown syntax"). V-03's catch-all is analytically sufficient but carries higher runtime risk: models may interpret "no markdown syntax" narrowly (e.g., no bold, no headers) while still emitting backtick fences or angle-bracket variable notation. Explicit enumeration eliminates that ambiguity.

### E-3: All essentials pass across all five variations — the baseline is already solid

Unlike more complex skills (scout-feasibility, review-design), topic-report's essential structure is simple enough that even V-01 satisfies all five essential criteria. The baseline has: write + echo, table + counts, open list + owners, readiness label + calibration, concrete next step. This is fully specified in V-01. Variations that add structure (V-02, V-03, V-05) improve *reliability* of those criteria in live runs, not their rubric score.

---

## C-09 Design Analysis

C-09 is the sharpest discriminator in this rubric because it requires the readiness statement to *name* blocking signals rather than describe their count or category. Four of five variations fail this criterion:

| Variation | Readiness instruction | Why C-09 fails |
|-----------|----------------------|----------------|
| V-01 | "one sentence of justification" | No requirement to name specific signals |
| V-02 | SLOT 3 "Then one sentence" | Sentence content is unconstrained |
| V-03 | "Derive directly from locked counts" | Count-based derivation doesn't require naming |
| V-04 | Q4 "State your readiness label and one sentence justification" | Justification can be count-only |
| V-05 | "must reference the BLOCKERS list from PHASE 2 by name" | PASS — specific signals named in example |

The BLOCKERS phase is what makes V-05 pass: by forcing the model to produce a named list *before* the readiness statement, and explicitly requiring that list to appear in the sentence, V-05 closes the gap structurally rather than relying on model judgment.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- Achieves 100/100 — the only variation to pass C-09
- BLOCKERS phase structurally guarantees blocker-naming in the readiness statement
- CHECKPOINT in PHASE 1 locks counts before any prose (same mechanism as V-03, strongest for C-02/C-04)
- Most explicit Teams card prohibition list (C-10 via enumeration)
- SLOT structure prevents section omissions (C-03/C-05)

**V-03** is the strongest alternative for C-02/C-04 accuracy due to its CHECKPOINT gate. If blocker-naming is not the priority, V-03 and V-02 are equivalent at 95.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["BLOCKERS phase before readiness is the only reliable path to C-09 — pre-computing and naming essential OPEN signals as a locked list before the readiness statement is written, then requiring the sentence to reference that list by name, is the necessary and sufficient design pattern", "Explicit character enumeration (no backticks, no angle brackets) outperforms catch-all prohibition (no markdown syntax) for Teams card paste-readiness — models may interpret catch-alls narrowly while still emitting inline code fences or angle-bracket variable notation"]}
```
