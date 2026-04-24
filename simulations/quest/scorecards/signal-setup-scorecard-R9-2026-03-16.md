Now I have everything needed to score all five variations.

---

# Quest Scorecard — signal-setup — Round 9

**Rubric**: v8 | **Denominator**: 16 (aspirational C-09–C-24) | **Date**: 2026-03-16
**Scoring formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/16 * 10)`

---

## Criterion Evaluation — All Variations

### Essential (C-01–C-05)

All five variations share the same core mechanism: read before write, preview, confirm, append with skill advertising, detect existing section.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | File detection before write | PASS | PASS | PASS | PASS | PASS |
| C-02 | Preview shown before writing | PASS | PASS | PASS | PASS | PASS |
| C-03 | Confirmation required | PASS | PASS | PASS | PASS | PASS |
| C-04 | Signal section appended with skill advertising | PASS | PASS | PASS | PASS | PASS |
| C-05 | Idempotent re-run | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variations** ✅

---

### Recommended (C-06–C-08)

All five variations include the inertia rule in the template, offer Copilot update, and produce a final status/summary output.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Inertia rule included | PASS | PASS | PASS | PASS | PASS |
| C-07 | Copilot instructions offered | PASS | PASS | PASS | PASS | PASS |
| C-08 | User feedback on outcome | PASS | PASS | PASS | PASS | PASS |

**Recommended: 3/3 all variations** ✅

---

### Aspirational (C-09–C-24)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Preview matches written output | PASS | PASS | PASS | PASS | PASS |
| C-10 | Handles missing CLAUDE.md gracefully | PASS | PASS | PASS | PASS | PASS |
| C-11 | Named gate checkpoints as explicit phase boundaries | PASS | PASS | PASS | PASS | PASS |
| **C-12** | **Edge-case paths promoted to first-class gates** | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| C-13 | Skill opens with motivational preamble | PASS | PASS | PASS | PASS | PASS |
| C-14 | Decline path names its consequence | PASS | PASS | PASS | PASS | PASS |
| C-15 | Already-configured path affirms positive consequence | PASS | PASS | PASS | PASS | PASS |
| C-16 | Inertia named as adversary, not concept | PASS | PASS | PASS | PASS | PASS |
| C-17 | Preamble explains temporal persistence of configuration | PASS | PASS | PASS | PASS | PASS |
| C-18 | Decline path anchors consequence to a future moment | PASS | PASS | PASS | PASS | PASS |
| C-19 | Key arguments threaded through all equivalent exit gates | PASS | PASS | PASS | PASS | PASS |
| C-20 | Already-configured gate names the persistence mechanism | PASS | PASS | PASS | PASS | PASS |
| C-21 | Secondary optional gates carry path-specific consequence anchors | PASS | PASS | PASS | PASS | PASS |
| C-22 | Consequence anchors are phase-indexed, not tool-indexed | PASS | PASS | PASS | PASS | PASS |
| C-23 | Explicit phase label at each decline anchor | PASS | PASS | PASS | PASS | PASS |
| C-24 | Secondary already-configured paths affirm tool-local consequence | PASS | PASS | PASS | PASS | PASS |

---

### C-12 Evidence Per Variation

**V-01 — PASS**: GATE 1A is a separate named sub-gate with its own `### GATE 1A — Missing CLAUDE.md (First-Class Gate)` header and complete treatment. GATE 2A similarly has `### GATE 2A — Already Configured (First-Class Gate)`. Edge cases are structurally equal to the happy path — not inline conditionals.

**V-02 — FAIL**: Missing CLAUDE.md is handled as `**If not found**:` — an inline conditional block inside Step 1, not a dedicated named step. Already-configured is handled as `**If Signal section already present**:` inside Step 2. Both edge cases are prose branches within a step, not promoted to first-class gates. C-12 explicitly requires "dedicated named gates (not inline conditionals inside the happy path)."

**V-03 — FAIL**: Step 1 handles the not-found case as `**Not found** — CLAUDE.md does not exist...` — inline bold heading within the step body. Step 2 handles already-configured as `**Already present**:` — inline block. Same structural failure as V-02. Neither edge case has its own numbered step or named gate.

**V-04 — PASS**: `### GATE 1A — No CLAUDE.md` is a dedicated section under GATE 1. `### GATE 2A — Already Configured` is a dedicated section under GATE 2. Each has complete, self-contained treatment including all consequence language. First-class gate structure.

**V-05 — PASS**: `### GATE 1A — Missing CLAUDE.md` and `### GATE 2A — Already Configured` are promoted to dedicated named sub-gates. V-05 additionally promotes the Copilot append confirmation to `### GATE 6A — Confirm Copilot Append` — the most thorough edge-case promotion of any variation.

---

## Score Computation

```
Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/16 * 10)
```

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 5/5 = 60.0 | 3/3 = 30.0 | 16/16 = 10.00 | **100.0** | YES |
| V-02 | 5/5 = 60.0 | 3/3 = 30.0 | 15/16 = 9.375 | **99.4** | YES |
| V-03 | 5/5 = 60.0 | 3/3 = 30.0 | 15/16 = 9.375 | **99.4** | YES |
| V-04 | 5/5 = 60.0 | 3/3 = 30.0 | 16/16 = 10.00 | **100.0** | YES |
| V-05 | 5/5 = 60.0 | 3/3 = 30.0 | 16/16 = 10.00 | **100.0** | YES |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | V-01 | 100.0 | Gate-named structure; concise preamble; does not provide a distinct Copilot template |
| 1 (tie) | V-04 | 100.0 | Phase labels + secondary gate coverage; distinct Copilot template with implementation-context framing; stage complementarity named |
| 1 (tie) | V-05 | 100.0 | Full threading + GATE 6A sub-gate; strongest C-20 formulation; most explicit stage-complementarity mapping |
| 4 (tie) | V-02 | 99.4 | C-12 FAIL: missing-CLAUDE.md and already-configured handled inline; strong adversary framing; explicit phase labels present |
| 4 (tie) | V-03 | 99.4 | C-12 FAIL: same inline structure failure; best explicit-phase-label discipline; clean "planning stage" / "while implementing" usage |

---

## Excellence Signals

The v8 rubric's three new criteria (C-22, C-23, C-24) were all passed by every variation in R9. The differentiator round-over-round shifted from phase-vocabulary distinctness (R7) to gate promotion (R9). Three structural choices separated the 100.0 group from the 99.4 group and within the 100.0 group:

**1. First-class gate promotion as structural commitment (C-12).** The structural difference between PASS and FAIL on C-12 is not a content difference — V-02 and V-03 have equally strong consequence language, phase labels, and adversary framing. The difference is architectural: whether the edge case is *visible as a gate* in the spec's structural outline. V-01/V-04/V-05 declare `### GATE 1A` as a named boundary; the reader knows an edge case was considered at design time. V-02/V-03 fold the edge case into a prose conditional; it reads as error handling appended to the happy path, not a first-class lifecycle state. C-12 is not primarily about output quality — it is about whether the spec *enforces consideration* of the edge case at the architectural level.

**2. Distinct Copilot template as implementation-context artifact (V-04, V-05 only).** Both V-04 and V-05 provide a named "Copilot Instructions Section (Implementation Context)" template alongside the "CLAUDE.md Section (Planning Context)" template. V-01 references "the Copilot Signal section" without defining it. This gap is not currently captured by any v8 criterion — C-24 scores the *affirm response* at the already-configured gate, but no criterion scores the *content* that gets written to copilot-instructions.md. V-04 and V-05's Copilot template uses implementation-phase vocabulary: `/trace`, `/flow`, `/review`, "before accepting a Copilot suggestion," "does this code assume adoption without evidence?" This is the only new structural pattern in R9 not yet formalized as a criterion.

**3. Stage complementarity mapping in the secondary affirm (V-04, V-05 only).** Both V-04 and V-05 name the relationship between the two tools in the GATE 6 already-configured response: *"That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning stage; Copilot instructions protect the implementation stage. Both are covered."* V-01's GATE 6 already-configured response affirms the Copilot benefit (C-24 PASS) but does not name how the two tools are complementary and non-overlapping. This is a stronger formulation than C-24 requires — it maps the full coverage picture, not just the tool-local benefit. Not yet a rubric criterion; first observed in R9.

---

## Carry-Forward Recommendation

**R10 candidate: V-04** — 100.0 with cleaner structure than V-05 (no GATE 6A complexity) while carrying the two new patterns (distinct Copilot template, stage complementarity mapping) that V-01 lacks. V-04 is the minimum-necessary carrier of R9's new patterns.

**V-05 as hedge**: If a new C-25 captures the distinct Copilot template and C-26 captures stage complementarity mapping, V-05 is already correct on both. It also has the strongest C-20 formulation ("not because you open it, but because Claude Code reads it before the first message") which may itself merit a criterion in R10.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["distinct implementation-context Copilot template: the skill spec should include a separate named template for copilot-instructions.md content framed in implementation-phase vocabulary (trace/flow/review, 'before accepting a suggestion', 'does this code assume adoption?') — not merely reference an undefined 'Copilot Signal section'; V-04 and V-05 have it, V-01 does not", "stage complementarity mapping in secondary affirm: the Copilot already-configured response gains structural completeness by naming how the two tools are non-overlapping ('CLAUDE.md protects the planning stage; Copilot instructions protect the implementation stage') rather than only affirming the Copilot-specific benefit; maps the full coverage picture rather than a single-tool advantage"]}
```
