Looking at the Round 3 scorecard, I can identify three distinct excellence patterns not yet captured in v3:

1. **V-01**: Explicitly **labeled** redundancy layers (`[LAYER 1 — STRUCTURAL]`, `[LAYER 2 — SEMANTIC]`, `[LAYER 3 — EXECUTION]`) — goes beyond C-13 (three layers present) by making them verifiable by inspection.
2. **V-02**: The **assertion table format pre-seeded in the template** — fuses C-14 + C-15: the per-signal evaluation structure is absorbed as output shape, not just described in execution instructions.
3. **V-03**: **Consequence vocabulary saturation** — entire section taxonomy recast in commitment terms (COMMIT RISKS, COMMIT DECISION, HIGHEST PRIORITY RISK), making the decision frame architectural rather than annotative. Goes beyond C-16 (one ship-risk sentence).

These become C-17, C-18, C-19 in a new Structural Tier 3. New max: 135 + 15 = **150**.

---

```markdown
# Rubric: `topic:status` — v4
**Updated:** 2026-03-14
**Max Score:** 150
**Passing Threshold:** All essential criteria pass + score >= 80

---

## Change History

| Version | Max | Notes |
|---------|-----|-------|
| v1 | 90 | Initial: essential + recommended |
| v2 | 115 | Added aspirational C-08–C-12 (structural completeness, phase gates, gap-first ordering) |
| v3 | 135 | Added aspirational-2 C-13–C-16 (triple redundancy, template-first, per-signal assertion, consequence framing) |
| v4 | 150 | Added aspirational-3 C-17–C-19 from R3 excellence signals: labeled redundancy layers, assertion table pre-seeded in template, consequence vocabulary saturation |

---

## v3 → v4 Changes

**Three new aspirational criteria (structural tier 3, 15 pts):**

| ID | Origin | Pattern |
|----|--------|---------|
| C-17 | V-01 R3 | **Labeled redundancy layers** — each of the three C-13 enforcement layers is explicitly labeled (e.g., `[LAYER 1 — STRUCTURAL]`, `[LAYER 2 — SEMANTIC]`, `[LAYER 3 — EXECUTION]`), making the mechanism verifiable by inspection rather than requiring inference about structural distinctness. Strengthens C-13. |
| C-18 | V-02 R3 | **Assertion table pre-seeded in template** — the per-signal assertion table *format* (one row per planned signal, PRESENT/NOT_PRESENT columns) is physically embedded in the output template before execution instructions, fusing C-14 (template-first absorption) and C-15 (per-signal evaluation) at the structural level. The evaluation structure is absorbed as output shape. Strengthens C-14 + C-15. |
| C-19 | V-03 R3 | **Consequence vocabulary saturation** — every major output section title uses consequence-framing vocabulary (e.g., `COMMIT RISKS`, `COMMIT DECISION`, `HIGHEST PRIORITY RISK`) rather than status-reporting vocabulary (`OPEN GAPS`, `READINESS`, `NEXT STEP`). The decision frame is architecturally embedded, not added as an annotation. Strengthens C-16. |

**Max score:** 135 → **150**. Passing threshold unchanged.

**Implication chain:**
- C-17 => C-13 (labeled layers implies triple-redundancy passes)
- C-18 => C-14 (pre-seeded template implies template-first absorption passes)
- C-18 => C-15 (pre-seeded assertion table implies per-signal assertion chain passes)
- C-19 => C-16 (vocabulary saturation implies consequence-framed verdict passes)

A variation earning all seven R2+R3 aspirational criteria (C-13–C-19) plus the full aspirational floor (C-10–C-12) achieves 150 and represents complete structural closure of every known failure mode with verified, labeled, pre-absorbed enforcement.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Signal discovery** — The skill scans the `simulations/` directory for existing signal files matching the topic, using a Glob pattern. The scan is explicit and disk-based, not inferred from memory. | 15 | coverage | A Glob or equivalent disk-scan instruction is present. Results are assigned to a named variable (e.g. `DISK_SIGNALS`). Zero-result case is handled: output states "no signals found" rather than silently computing 0%. |
| C-02 | **Coverage percentage** — Output reports a numeric coverage percentage derived from signals found on disk versus signals planned in `strategy.md`. The percentage is mathematically consistent with the gap list. | 15 | coverage | A percentage formula is present (`found / planned * 100` or equivalent). A consistency check guards against the contradiction failure mode: if the gap list is non-empty and percentage equals 100%, execution halts and recomputes. |
| C-03 | **Gap identification** — Signals planned in `strategy.md` but not yet present on disk are listed as open gaps. | 15 | coverage | At least one gap section exists. If all planned signals are present, output explicitly states "no gaps". Gaps are named (namespace + signal type), not just counted. |
| C-04 | **Display-only behavior** — The skill writes nothing to disk. No file is created or modified. | 15 | behavior | After execution, `git status` shows no new or modified files. Output is terminal-only. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Readiness verdict** — Output provides a clear readiness signal for the stated target outcome (e.g. "NOT READY — 3 essential gaps remain", "READY — all scout + draft signals present"). | 10 | depth | A readiness label or verdict is present and connected to the gap list. Not just a coverage number — a qualitative judgment. |
| C-06 | **Namespace breakdown** — Coverage is shown per namespace (scout, draft, review, flow, trace, prove, listen, program, topic), not only as a single aggregate. | 10 | format | At least namespace-level grouping visible in output. Namespaces with zero signals are shown as empty, not omitted. |
| C-07 | **Strategy cross-reference** — Output names the `strategy.md` file used as the planned-signal baseline and notes if `strategy.md` is missing or has no planned signals for this topic. | 10 | correctness | `strategy.md` reference appears in output. If missing, output says so explicitly rather than silently computing against zero. |

---

## Aspirational Criteria (25 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Recency awareness** — Output flags signals older than a configurable threshold (default: 30 days) as potentially stale, so coverage is not overstated by outdated evidence. | 5 | depth | At least one signal is annotated with its age, or a staleness summary is shown. Does not require every signal to be dated — a summary is sufficient. |
| C-09 | **Actionable next step** — Output recommends the single highest-priority gap to close next, with the skill invocation that would produce it (e.g. "Run `/scout:feasibility` to fill scout-feasibility gap"). | 5 | depth | A concrete "next step" line appears, naming a specific skill. Must match an open gap — not a generic suggestion. |
| C-10 | **Structural namespace completeness** — The 9-namespace table is pre-seeded so that empty rows are physically present in the output template, making omission structurally impossible rather than instruction-dependent. | 5 | format | All 9 namespace rows appear in output even when count is zero. Empty rows render as `0 / 0 — —` or equivalent — not absent. A "Show all 9" instruction alone does not satisfy this; the structure must enforce it. |
| C-11 | **Phase-gated execution with pre-display disk-check** — Execution is organized into named phases (e.g. DISCOVER → COMPUTE → DISPLAY) with an explicit gate before the display phase that confirms no writes have occurred or will occur. | 5 | behavior | Named phases are visible in skill instructions. A pre-display contract check is present (e.g. "If you write to disk, the skill fails regardless of output quality. Check before Phase 3."). Strengthens C-04 from a stated rule to a runtime-verified contract. |
| C-12 | **Gap-first output ordering** — Gaps are listed as the primary output section, appearing before the aggregate coverage number. This ordering structurally closes the "percentage contradicts gap list" failure mode: the math is anchored to an already-enumerated gap list rather than computed in isolation. | 5 | correctness | Gap section appears in output before the coverage percentage line. The coverage number is presented as a summary of the gap list, not the other way around. |

---

## Aspirational Criteria — Structural Tier 2 (20 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-13 | **Triple-redundancy ordering guard** — Gap-first ordering is enforced by three independent layers: (1) the output template or display section physically places gaps before coverage, (2) a semantic NOTE block states the principle ("the coverage number summarizes the gap list — not the other way around"), (3) a phase render-order instruction explicitly sequences GAPS before COVERAGE in the execution instructions. All three must be present. | 5 | correctness | Three structurally distinct enforcement layers for gap-first ordering are identifiable: structural (template/display section order), semantic (NOTE or principle statement explaining why), and execution (explicit render order in phase instructions). C-12 pass is implied and necessary but not sufficient. A single mechanism stated three times does not satisfy this — the layers must be structurally distinct. |
| C-14 | **Template-first structural absorption** — The complete output template (including all 9 pre-seeded namespace rows and gap section appearing before coverage) is placed at the top of the skill prompt, before any execution instruction. The model absorbs the target output shape before reading how to produce it, making structural omission and section reordering harder to rationalize away. | 5 | format | The output template appears before execution instructions in the prompt. Template includes pre-seeded 9-namespace rows and shows gap section before coverage. C-10 pass is implied. A template appearing after execution steps satisfies C-10 but not C-14 — the before-execution placement requirement is binding. |
| C-15 | **Per-signal assertion chain** — Rather than searching for gaps as a batch operation, each planned signal is individually evaluated as PRESENT or NOT_PRESENT. The gap list is derived as the NOT_PRESENT set — a mathematical residual — rather than assembled by lookup. A low-signal namespace cannot be skipped because every entry in the planned list must receive an individual verdict. | 5 | correctness | Execution instructions direct per-entry PRESENT/NOT_PRESENT evaluation for each planned signal. The gap list is explicitly derived as the NOT_PRESENT set (or equivalent: "gaps = planned minus present"). C-03 pass is implied. A "find all gaps" or "list missing signals" batch instruction does not satisfy this — evaluation must be per-signal and the derivation must be explicit. |
| C-16 | **Consequence-framed readiness verdict** — The readiness verdict includes a ship risk sentence that names the cost of proceeding with current coverage: "Committing now means shipping without: {list of essential gaps}". The consequence frame makes the decision visible rather than leaving it to inference. The verdict is a decision instrument, not a status label. | 5 | depth | Readiness output includes a consequence sentence naming specific signals or categories that will be absent if the team proceeds. Must name concrete missing items — not a generic risk statement ("some gaps remain"). C-05 pass is implied. A variation that only states "NOT READY" without naming the downstream consequence does not satisfy this criterion. |

---

## Aspirational Criteria — Structural Tier 3 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-17 | **Labeled redundancy layers** — Each of the three C-13 enforcement layers carries an explicit label (e.g., `[LAYER 1 — STRUCTURAL]`, `[LAYER 2 — SEMANTIC]`, `[LAYER 3 — EXECUTION]`) at its physical location in the prompt. Labels make the mechanism verifiable by inspection: a reviewer can confirm distinctness and completeness without inferring intent from content. | 5 | correctness | All three enforcement layers are labeled at the point where they appear. Labels are structurally distinct (not grouped in a single block) and identify the mechanism type. C-13 pass is implied — C-17 requires C-13 to be true and additionally requires explicit labeling. A skill that has three distinct layers but no labels does not satisfy C-17 even if C-13 passes. |
| C-18 | **Assertion table pre-seeded in template** — The per-signal assertion table *format* — one row per planned signal with PRESENT/NOT_PRESENT columns — is physically embedded in the output template before execution instructions. The evaluation structure is absorbed as output shape (C-14 level), not merely described as an execution directive (C-15 level). A skill satisfying C-18 fuses template-first absorption and per-signal evaluation into a single structural guarantee: the model cannot rationalize omitting a row because the row slot already exists in the template it absorbed. | 5 | format | The assertion table format (with PRESENT/NOT_PRESENT columns and a "one row per planned signal" constraint) appears in the output template section, physically before execution instructions. C-14 and C-15 passes are both implied. A skill that describes per-signal evaluation in execution instructions only (satisfying C-15 but not pre-seeding the table in the template) does not satisfy C-18. |
| C-19 | **Consequence vocabulary saturation** — Every major output section title uses consequence-framing vocabulary rather than status-reporting vocabulary. The mapping is systematic: gaps become commit risks (`COMMIT RISKS`), readiness becomes a commit decision (`COMMIT DECISION`), next step becomes highest priority risk (`HIGHEST PRIORITY RISK`). The decision frame is architectural — embedded in the section taxonomy — not added as an annotation to an otherwise status-structured output. | 5 | depth | All major output sections use consequence vocabulary throughout (section headers, verdict labels, next-step framing). The vocabulary shift is consistent — no section reverts to status-reporting language. C-16 pass is implied. A variation that adds a single ship-risk sentence to a status-vocabulary output (satisfying C-16) does not satisfy C-19 — the saturation requirement demands section-level reframing, not sentence-level addition. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 (15 each) |
| Recommended | C-05, C-06, C-07 | 30 (10 each) |
| Aspirational | C-08, C-09, C-10, C-11, C-12 | 25 (5 each) |
| Aspirational — Structural Tier 2 | C-13, C-14, C-15, C-16 | 20 (5 each) |
| Aspirational — Structural Tier 3 | C-17, C-18, C-19 | 15 (5 each) |
| **Total** | **C-01 – C-19** | **150** |

**Passing threshold:** All essential criteria (C-01–C-04) must pass AND total score >= 80.

---

## Implication Map

```
C-17 => C-13 => C-12
C-18 => C-14 => C-10
C-18 => C-15 => C-03
C-19 => C-16 => C-05
```

A variation earning all three Tier 3 criteria (C-17/C-18/C-19) necessarily earns all four Tier 2 criteria (C-13/C-14/C-15/C-16) plus the dependent aspirational criteria (C-10/C-12 implied by C-13, C-14; C-03 implied by C-15; C-05 implied by C-16). The minimum score achievable while earning all Tier 3 criteria is 135 (all essential + recommended + C-10/C-12 + C-03/C-05 implied). The maximum is 150.
```
```
