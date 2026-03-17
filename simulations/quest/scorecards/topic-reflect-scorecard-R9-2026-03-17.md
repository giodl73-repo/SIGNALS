## /quest:score — topic-reflect — Round 9 (Rubric v8)

> **Note**: V-02's code block appears truncated — only the opening paragraph and start of Vocabulary Rule are visible. V-02 is scored partially with inferences from axis description where text is unavailable.

---

### V-01 Full Scorecard

**Axis**: Build Risk sub-field — structural slot only (no calibration imitation, no COMMIT-ENTRY gate)

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Stage 4 rules: "At least one entry must contradict (not merely refine) a B-# belief." B-# reference required in each entry. |
| C-02 | **PASS** | Stage 1: opening model + epistemic profile table + B-# inventory (3+). Stage 6: verdict table with COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED + summary. |
| C-03 | **PASS** | Signal Source: "Name the specific artifact, skill run, or simulation file. Include namespace and date where available. Do not write 'multiple sources' or 'various signals.'" |
| C-04 | **PASS** | Design Impact: "Full sentence naming the specific component, API, flow, or architectural decision that must change or be reconsidered." |
| C-05 | **PASS** | Stage 3 five-check table present with VALID/INVALID per column, GATE-CONFIRMED/GATE-REJECTED verdict, COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED enforced. |

**Essential: 60 / 60**

---

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Vocabulary Rule: exactly the 5 canonical names, explicit "Do not substitute synonyms." |
| C-07 | **PASS** | "Minimum 2 entries (all GATE-CONFIRMED)." Stage 3 extension sweep enforced if fewer than 2. |
| C-08 | **PASS** | Stage 5: "At least one entry in Next Team / Skill must name a specific skill or role (e.g., `/flow-resilience`, `API designer`, `/prove-hypothesis`), not just 'investigate.'" |

**Recommended: 30 / 30**

---

#### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | COMMIT-STAGE-1 through COMMIT-STAGE-6 all present. COMMIT-ENTRY per entry in Stage 4. GATE-CONFIRMED/REJECTED in Stage 3. |
| C-10 | **PASS** | Stage 6: "Record CLEAR if no foreknowledge flags were issued in Stage 3, or FLAGGED if any beliefs were excluded, naming the beliefs responsible." |
| C-11 | **PASS** | "Do not use a table. Use labeled sub-fields in a prose block." Format demonstrated as numbered prose blocks with labeled sub-fields. |
| C-12 | **PASS** | "No single-word or two-word entries in any sub-field. Every field is a full phrase or sentence." |
| C-13 | **PASS** | Standalone "## Vocabulary Rule" section with substitution prohibition, not embedded in Stage 1 prose. |
| C-14 | **PASS** | Stage 3: binary COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED enforced; foreknowledge resolution is structural, not advisory. |
| C-15 | **FAIL** | No top-level gate sequence overview table before Stage 1. Tokens are defined only within individual stages. |
| C-16 | **FAIL** | Stage 4 shows the template (labeled sub-fields with placeholder instructions) but no filled-in example with a realistic artifact reference. |
| C-17 | **PASS** | Vocabulary Rule names 4 specific prohibited synonyms: Reliability, Performance, Complexity, Maintainability. |
| C-18 | **PASS** | Full mapping table: Reliability→Correctness, Performance→Scalability, Complexity→Feasibility or Correctness, Maintainability→Adoptability. 4 mappings. |
| C-19 | **FAIL** | Each stage has an exit emit token (COMMIT-STAGE-N) but no formal ENTER conditions (what must be true to begin the stage). Stages are instruction sequences, not pre/post-condition contracts. |
| C-20 | **FAIL** | No Surprise 0 / entry-zero calibration instance. |
| C-21 | **FAIL** | Vocabulary Rule contains "replace it with the closest canonical name before emitting" but this is a general instruction, not bound to any stage EXIT criterion. C-21 requires the repair instruction to be inside a stage exit gate. |
| C-22 | **PARTIAL** | Structural slot present. Framing distinction is explicit: "Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail." Specificity exclusion present: "not a general risk category such as 'complexity' or 'stability.'" Missing: "the field is modeled in the calibration example" — no calibration example exists. Slot + framing + specificity instruction = partial pass. **2.5 pts** |
| C-23 | **FAIL** | No Surprise 0. The dual-field anchoring pattern this criterion tests is entirely absent. |
| C-24 | **FAIL** | COMMIT-ENTRY is present after each entry but includes no Build Risk specificity check. No failure condition or corrective action for under-specific Build Risk values before token emission. Axis explicitly confirms this is absent. |
| C-25 | **FAIL** | No field achieves ≥2 mechanisms from the required set (a: Surprise 0 imitation / b: per-entry EXIT naming sub-field / c: repair instruction). Each sub-field has at most 1 mechanism (structural rule instruction). |

**Aspirational: 47.5 / 85**

---

**V-01 Total: 137.5 / 175**

---

### V-02 Partial Scorecard

**Axis**: Surprise 0 dual-field anchoring — calibration example embedded as Stage 4 entry 0 with explicitly distinct Design Impact and Build Risk values

**Scoring status**: Prompt text truncated after beginning of Vocabulary Rule. Assessment is based on (1) visible text and (2) axis description.

| Tier | Assessment |
|------|-----------|
| Essential C-01–C-05 | Likely PASS (axis implies full Stage 4 and Stage 3 structure; no structural reason to regress) — *inferred* |
| Recommended C-06–C-08 | C-06/C-13 vocabulary rule visible and starts correctly; remainder inferred PASS — *partial direct / partial inferred* |
| C-16 | **PASS (inferred)** — Axis: calibration example embedded as Stage 4 entry 0 |
| C-20 | **PASS (inferred)** — Axis: "entry 0" notation, positioned within Stage 4 sequence |
| C-22 | **PASS (inferred)** — Surprise 0 models Build Risk, satisfying "the field is modeled in the calibration example" |
| C-23 | **PASS (inferred)** — Axis: "explicitly distinct Design Impact and Build Risk values"; "what must change vs. what is implicated by that change" framing; non-redundant content |
| C-24 | **Status unknown** — Axis does not describe a COMMIT-ENTRY Build Risk gate; likely FAIL |
| C-25 | **Likely PARTIAL** — Surprise 0 provides mechanism (a) for all four sub-fields; whether mechanism (b) or (c) exists for each field is unknown |
| C-15, C-19, C-21 | **Status unknown** — prompt truncated before stages visible |

**Estimated V-02 score**: ~150 / 175 (V-01 base 137.5 + C-16 +5, C-22 upgrade +2.5, C-23 +5 = 150)
*Cannot confirm due to truncation. Estimated as lower bound if remaining stages preserve V-01's essential/recommended passes.*

---

### Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-02 | ~150 (estimated) | Yes (inferred) |
| 2 | V-01 | 137.5 | Yes |

---

### Excellence Signals — V-01

**Signal 1 — Framing distinction embedded in sub-field instruction**: V-01 articulates the Design Impact vs. Build Risk conceptual split directly in the instruction text: *"Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract."* This framing instruction alone prevents the conflation error (treating Build Risk as a restatement of Design Impact) without requiring a calibration example. The distinction is taught at point of instruction, not just modeled.

**Signal 2 — Specificity anti-pattern exclusion in structural instruction**: V-01's Build Risk instruction excludes by negative example: *"not a general risk category such as 'complexity' or 'stability.'"* This mirrors the vocabulary rule's named-exclusion pattern (C-17) applied to a structural sub-field — naming the most likely failure modes by type rather than relying on the positive requirement alone.

Neither signal is sufficient to pass C-22 fully (calibration example still required), but both reduce the quality floor relative to a bare structural slot.

---

```json
{"top_score": 137.5, "all_essential_pass": true, "new_patterns": ["framing-distinction-in-sub-field-instruction: articulating Design Impact vs Build Risk conceptual split inside the instruction text prevents conflation without requiring calibration example", "specificity-anti-pattern-exclusion: naming prohibited value types by category in structural sub-field instruction mirrors vocabulary named-exclusion pattern applied to output fields"]}
```
