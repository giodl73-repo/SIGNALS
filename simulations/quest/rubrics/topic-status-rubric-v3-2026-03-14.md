`topic-status-rubric-v3-2026-03-14.md` written. Here's the summary of what changed:

---

## v2 -> v3 changes

**Four new aspirational criteria (structural tier 2, 20 pts):**

| ID | Origin | Pattern |
|----|--------|---------|
| C-13 | V-05 R2 | **Triple-redundancy ordering guard** — gap-first enforced by 3 independent layers: template structure + semantic NOTE + phase render order. One layer failing can't break the contract. Strengthens C-12. |
| C-14 | V-02 R2 | **Template-first structural absorption** — full output template placed *before* execution instructions. Model absorbs the output shape before reading behavior. Distinct from C-10 (physical presence) — this is about prompt-level positioning. Strengthens C-10 + C-12. |
| C-15 | V-03 R2 | **Per-signal assertion chain** — each planned signal evaluated individually as PRESENT/NOT_PRESENT; gap list = NOT_PRESENT set (mathematical residual, not search result). Eliminates batch-omission structurally. Strengthens C-03. |
| C-16 | V-04 R2 | **Consequence-framed readiness verdict** — "Committing now means shipping without: X" names the cost of proceeding, converting a status label into a decision instrument. Strengthens C-05. |

**Max score**: 115 → **135**. Passing threshold unchanged (all essential + >= 80).

**Implication chain**: C-13 => C-12, C-14 => C-10 (+C-12), C-15 => C-03, C-16 => C-05. A variation earning all four R3 criteria plus all three R2 structural criteria achieves 135 and closes every known failure mode with multiple independent structural layers.
om 115 -> 135. The four new criteria form a second aspirational sub-tier (20 pts) that captures structural sophistication above the R2 floor.

**Implication relationships**:
- C-13 => C-12 (triple-redundancy implies gap-first ordering passes)
- C-14 => C-10 (template-first implies structural completeness passes; also strengthens C-12)
- C-15 => C-03 (per-signal assertion implies gap identification passes)
- C-16 => C-05 (consequence framing implies readiness verdict passes)

A skill that earns all four R3 criteria (C-13/C-14/C-15/C-16) plus the full R2 floor (C-10/C-11/C-12) achieves 135 and closes every known failure mode with multiple independent structural layers.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Signal discovery** -- The skill scans the `simulations/` directory for existing signal files matching the topic, using a Glob pattern. The scan is explicit and disk-based, not inferred from memory. | essential | coverage | A Glob or equivalent disk-scan instruction is present. Results are assigned to a named variable (e.g. DISK_SIGNALS). Zero-result case is handled: output states "no signals found" rather than silently computing 0%. |
| C-02 | **Coverage percentage** -- Output reports a numeric coverage percentage derived from signals found on disk versus signals planned in strategy.md. The percentage is mathematically consistent with the gap list. | essential | coverage | A percentage formula is present (`found / planned * 100` or equivalent). A consistency check guards against the contradiction failure mode: if the gap list is non-empty and percentage equals 100%, execution halts and recomputes. |
| C-03 | **Gap identification** -- Signals planned in strategy.md but not yet present on disk are listed as open gaps. | essential | coverage | At least one gap section exists. If all planned signals are present, output explicitly states "no gaps". Gaps are named (namespace + signal type), not just counted. |
| C-04 | **Display-only behavior** -- The skill writes nothing to disk. No file is created or modified. | essential | behavior | After execution, `git status` shows no new or modified files. Output is terminal-only. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Readiness verdict** -- Output provides a clear readiness signal for the stated target outcome (e.g. "NOT READY -- 3 essential gaps remain", "READY -- all scout + draft signals present"). | recommended | depth | A readiness label or verdict is present and connected to the gap list. Not just a coverage number -- a qualitative judgment. |
| C-06 | **Namespace breakdown** -- Coverage is shown per namespace (scout, draft, review, flow, trace, prove, listen, program, topic), not only as a single aggregate. | recommended | format | At least namespace-level grouping visible in output. Namespaces with zero signals are shown as empty, not omitted. |
| C-07 | **Strategy cross-reference** -- Output names the strategy.md file used as the planned-signal baseline and notes if strategy.md is missing or has no planned signals for this topic. | recommended | correctness | strategy.md reference appears in output. If missing, output says so explicitly rather than silently computing against zero. |

---

## Aspirational Criteria (25 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Recency awareness** -- Output flags signals older than a configurable threshold (default: 30 days) as potentially stale, so coverage is not overstated by outdated evidence. | aspirational | depth | At least one signal is annotated with its age, or a staleness summary is shown. Does not require every signal to be dated -- a summary is sufficient. |
| C-09 | **Actionable next step** -- Output recommends the single highest-priority gap to close next, with the skill invocation that would produce it (e.g. "Run /scout:feasibility to fill scout-feasibility gap"). | aspirational | depth | A concrete "next step" line appears, naming a specific skill. Must match an open gap -- not a generic suggestion. |
| C-10 | **Structural namespace completeness** -- The 9-namespace table is pre-seeded so that empty rows are physically present in the output template, making omission structurally impossible rather than instruction-dependent. | aspirational | format | All 9 namespace rows appear in output even when count is zero. Empty rows render as `0 / 0 -- --` or equivalent -- not absent. A "Show all 9" instruction alone does not satisfy this; the structure must enforce it. |
| C-11 | **Phase-gated execution with pre-display disk-check** -- Execution is organized into named phases (e.g. DISCOVER -> COMPUTE -> DISPLAY) with an explicit gate before the display phase that confirms no writes have occurred or will occur. | aspirational | behavior | Named phases are visible in skill instructions. A pre-display contract check is present (e.g. "If you write to disk, the skill fails regardless of output quality. Check before Phase 3."). Strengthens C-04 from a stated rule to a runtime-verified contract. |
| C-12 | **Gap-first output ordering** -- Gaps are listed as the primary output section, appearing before the aggregate coverage number. This ordering structurally closes the "percentage contradicts gap list" failure mode: the math is anchored to an already-enumerated gap list rather than computed in isolation. | aspirational | correctness | Gap section appears in output before the coverage percentage line. The coverage number is presented as a summary of the gap list, not the other way around. |

---

## Aspirational Criteria -- Structural Tier 2 (20 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-13 | **Triple-redundancy ordering guard** -- Gap-first ordering is enforced by three independent layers: (1) the output template or display section physically places gaps before coverage, (2) a semantic NOTE block states the principle ("the coverage number summarizes the gap list -- not the other way around"), (3) a phase render-order instruction explicitly sequences GAPS before COVERAGE in the execution instructions. All three must be present. | aspirational-2 | correctness | Three structurally distinct enforcement layers for gap-first ordering are identifiable: structural (template/display section order), semantic (NOTE or principle statement explaining why), and execution (explicit render order in phase instructions). C-12 pass is implied and necessary but not sufficient. A single mechanism stated three times does not satisfy this -- the layers must be structurally distinct. |
| C-14 | **Template-first structural absorption** -- The complete output template (including all 9 pre-seeded namespace rows and gap section appearing before coverage) is placed at the top of the skill prompt, before any execution instruction. The model absorbs the target output shape before reading how to produce it, making structural omission and section reordering harder to rationalize away. | aspirational-2 | format | The output template appears before execution instructions in the prompt. Template includes pre-seeded 9-namespace rows and shows gap section before coverage. C-10 pass is implied. A template appearing after execution steps satisfies C-10 but not C-14 -- the before-execution placement requirement is binding. |
| C-15 | **Per-signal assertion chain** -- Rather than searching for gaps as a batch operation, each planned signal is individually evaluated as PRESENT or NOT_PRESENT. The gap list is derived as the NOT_PRESENT set -- a mathematical residual -- rather than assembled by lookup. A low-signal namespace cannot be skipped because every entry in the planned list must receive an individual verdict. | aspirational-2 | correctness | Execution instructions direct per-entry PRESENT/NOT_PRESENT evaluation for each planned signal. The gap list is explicitly derived as the NOT_PRESENT set (or equivalent: "gaps = planned minus present"). C-03 pass is implied. A "find all gaps" or "list missing signals" batch instruction does not satisfy this -- evaluation must be per-signal and the derivation must be explicit. |
| C-16 | **Consequence-framed readiness verdict** -- The readiness verdict includes a ship risk sentence that names the cost of proceeding with current coverage: "Committing now means shipping without: {list of essential gaps}". The consequence frame makes the decision visible rather than leaving it to inference. The verdict is a decision instrument, not a status label. | aspirational-2 | depth | Readiness output includes a consequence sentence naming specific signals or categories that will be absent if the team proceeds. Must name concrete missing items -- not a generic risk statement ("some gaps remain"). C-05 pass is implied. A variation that only states "NOT READY" without naming the downstream consequence does not satisfy this criterion. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 (15 each) |
| Recommended | C-05, C-06, C-07 | 30 (10 each) |
| Aspirational | C-08, C-09 | 10 (5 each) |
| Aspirational (structural tier 1) | C-10, C-11, C-12 | 15 (5 each) |
| Aspirational (structural tier 2) | C-13, C-14, C-15, C-16 | 20 (5 each) |
| **Maximum** | | **135** |

**Minimum passing**: all 4 essential pass + composite >= 80.

**Automatic fail conditions**:
- C-04 fails (file written to disk): skill violates its own contract, score = 0
- Coverage percentage present but visibly wrong (e.g. 100% when gaps are listed): C-02 fails regardless of other scores

---

## Excellence Pattern Notes (from Round 1)

**C-10 origin -- V-01 R1 (Table-centric)**
V-01 pre-printed the 9-row namespace table with explicit placeholder cells per row. The scorecard noted V-02's weakness: "empty-namespace display depends on 'Show all 9' instruction holding rather than structural impossibility." C-10 formalizes the stronger structural approach.

**C-11 origin -- V-03 R1 (Lifecycle / 3-Phase)**
V-03 received the highest C-04 praise despite being truncated: "If you write to disk, the skill fails regardless of output quality. Check before Phase 3." Named phases convert the display-only contract from a passive rule into an active execution gate the model checks at runtime.

**C-12 origin -- V-04 R1 (Gap-first ordering)**
The scorecard noted V-04 as having "the strongest C-02 correctness guarantee of any single-axis variation." When gaps are enumerated first, the coverage percentage is computed as a summary of a known list -- the contradiction failure mode is closed structurally rather than caught after the fact.

**Round 1 implication chain**:
- C-10 strengthens C-06: a C-10 pass implies C-06 pass, but not vice versa.
- C-11 strengthens C-04: a C-11 pass implies C-04 pass, but not vice versa.
- C-12 strengthens C-02: a C-12 pass makes the C-02 second fail condition unreachable by design.

---

## Excellence Pattern Notes (from Round 2)

**C-13 origin -- V-05 R2 (Full synthesis, triple-layer C-12)**
V-05 was the only variation with three independent enforcement layers for gap-first ordering: (1) TARGET OUTPUT template shows OPEN GAPS before COVERAGE, (2) a NOTE block reads "Do not reorder. The coverage number summarizes the gap list -- not the other way around," (3) Phase 4 render order: "OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE -> READINESS -> NEXT." Scorecard: "The NOTE block articulates the semantic principle behind the ordering, making the constraint harder to rationalize away." C-12 requires the result; C-13 requires three independent mechanisms producing it.

**C-14 origin -- V-02 R2 (Template-first declaration)**
V-02 placed the full 9-row output template at the top of the prompt, before Phase 1. Scorecard: "model absorbs the output shape (gap-first, all-9-rows) before reading execution instructions. Template-first declaration is the sharpest structural bet in Round 2." This is distinct from C-10 (rows physically present) -- placement-before-execution changes the model's cognitive sequencing. A template appearing after execution steps satisfies C-10 but not C-14.

**C-15 origin -- V-03 R2 (Per-signal assertion chain)**
V-03 replaced "find gaps" with per-entry PRESENT/NOT_PRESENT evaluation. Scorecard: "The assertion-chain logic for C-03 makes the gap list self-consistent by construction -- NOT_PRESENT set IS the gap list, eliminating any batch-omission risk. C-02 consistency is guaranteed structurally rather than checked retrospectively." A namespace with three planned signals cannot be silently omitted because all three must receive individual verdicts. The residual derivation (gaps = planned minus PRESENT set) is mathematically exact.

**C-16 origin -- V-04 R2 (Inertia framing / ship risk)**
V-04's readiness verdict: `Ship risk: Committing now means shipping without: {list essential unknowns}`. Scorecard: "Strongest C-05 treatment: ship risk sentence converts the readiness verdict from status label to decision instrument. 'Committing now means shipping without: X' names the bet being made -- qualitatively richer than any other variation's readiness line. Vocabulary shift (unknowns/ship risk) is not cosmetic; it changes the semantic frame of the entire output."

**Round 2 implication chain**:
- C-13 strengthens C-12: a C-13 pass implies C-12 pass. C-13 additionally requires two more independent structural layers.
- C-14 strengthens C-10: a C-14 pass implies C-10 pass. C-14 additionally requires pre-execution placement.
- C-14 also strengthens C-12: a template placed before execution that shows gaps before coverage makes C-12 absorption-level rather than instruction-level.
- C-15 strengthens C-03: a C-15 pass implies C-03 pass. C-15 additionally requires per-entry evaluation and explicit residual derivation.
- C-16 strengthens C-05: a C-16 pass implies C-05 pass. C-16 additionally requires a consequence sentence naming specific missing items.
