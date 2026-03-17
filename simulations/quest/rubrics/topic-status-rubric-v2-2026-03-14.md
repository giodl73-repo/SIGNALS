Written to `simulations/quest/rubrics/topic-status-rubric-v2-2026-03-14.md`.

---

## What changed

**Three new aspirational criteria** extracted from Round 1 excellence signals:

| ID | Source | What it captures |
|----|--------|-----------------|
| **C-10** | V-01 pre-printed table | Structural namespace completeness — empty rows enforced by template structure, not instruction. "Show all 9" alone doesn't pass. |
| **C-11** | V-03 CONTRACT block | Phase-gated execution with pre-display disk-check — named phases (DISCOVER → COMPUTE → DISPLAY) with "Check before Phase 3" gate. Converts C-04 from a passive rule to a runtime-verified contract. |
| **C-12** | V-04 gap-first ordering | Gap-first output — gaps appear before the aggregate number, making the C-02 contradiction failure mode unreachable by design. |

**Scoring change**: Max bumps from 100 → 115. The three structural criteria are split into their own sub-tier (15 pts) to distinguish them from the depth-oriented C-08/C-09. Passing threshold (all essential + >=80) is unchanged.

**Implication relationships** are called out explicitly: C-10 ⊃ C-06, C-11 ⊃ C-04, C-12 ⊃ C-02 second fail condition. A V-05 synthesis that earns all three structural bonuses gets 115 and closes every known failure mode.
icts the visible gap list also fails (e.g. "100%" when gaps are listed). |
| C-03 | **Gap identification** — Signals planned in strategy.md but not yet present on disk are listed as open gaps. | essential | coverage | At least one gap section exists. If all planned signals are present, output explicitly states "no gaps". Gaps are named (namespace + signal type), not just counted. |
| C-04 | **Display-only behavior** — The skill writes nothing to disk. No file is created or modified. | essential | behavior | After execution, `git status` shows no new or modified files. Output is terminal-only. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Readiness verdict** — Output provides a clear readiness signal for the stated target outcome (e.g. "NOT READY — 3 essential gaps remain", "READY — all scout + draft signals present"). | recommended | depth | A readiness label or verdict is present and connected to the gap list. Not just a coverage number — a qualitative judgment. |
| C-06 | **Namespace breakdown** — Coverage is shown per namespace (scout, draft, review, flow, trace, prove, listen, program, topic), not only as a single aggregate. | recommended | format | At least namespace-level grouping visible in output. Namespaces with zero signals are shown as empty, not omitted. |
| C-07 | **Strategy cross-reference** — Output names the strategy.md file used as the planned-signal baseline and notes if strategy.md is missing or has no planned signals for this topic. | recommended | correctness | strategy.md reference appears in output. If missing, output says so explicitly rather than silently computing against zero. |

---

## Aspirational Criteria (25 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Recency awareness** — Output flags signals older than a configurable threshold (default: 30 days) as potentially stale, so coverage is not overstated by outdated evidence. | aspirational | depth | At least one signal is annotated with its age, or a staleness summary is shown. Does not require every signal to be dated — a summary is sufficient. |
| C-09 | **Actionable next step** — Output recommends the single highest-priority gap to close next, with the skill invocation that would produce it (e.g. "Run /scout:feasibility to fill scout-feasibility gap"). | aspirational | depth | A concrete "next step" line appears, naming a specific skill. Must match an open gap — not a generic suggestion. |
| C-10 | **Structural namespace completeness** — The 9-namespace table is pre-seeded so that empty rows are physically present in the output template, making omission structurally impossible rather than instruction-dependent. | aspirational | format | All 9 namespace rows appear in output even when count is zero. Empty rows render as `0 / 0 — —` or equivalent — not absent. A "Show all 9" instruction alone does not satisfy this; the structure must enforce it. |
| C-11 | **Phase-gated execution with pre-display disk-check** — Execution is organized into named phases (e.g. DISCOVER -> COMPUTE -> DISPLAY) with an explicit gate before the display phase that confirms no writes have occurred or will occur. | aspirational | behavior | Named phases are visible in skill instructions. A pre-display contract check is present (e.g. "If you write to disk, the skill fails regardless of output quality. Check before Phase 3."). Strengthens C-04 from a stated rule to a runtime-verified contract. |
| C-12 | **Gap-first output ordering** — Gaps are listed as the primary output section, appearing before the aggregate coverage number. This ordering structurally closes the "percentage contradicts gap list" failure mode: the math is anchored to an already-enumerated gap list rather than computed in isolation. | aspirational | correctness | Gap section appears in output before the coverage percentage line. The coverage number is presented as a summary of the gap list, not the other way around. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 (15 each) |
| Recommended | C-05, C-06, C-07 | 30 (10 each) |
| Aspirational | C-08, C-09 | 10 (5 each) |
| Aspirational (structural) | C-10, C-11, C-12 | 15 (5 each) |
| **Maximum** | | **115** |

**Minimum passing**: all 4 essential pass + composite >= 80.

**Automatic fail conditions**:
- C-04 fails (file written to disk): skill violates its own contract, score = 0
- Coverage percentage present but visibly wrong (e.g. 100% when gaps are listed): C-02 fails regardless of other scores

---

## Excellence Pattern Notes (from Round 1)

These notes explain the origin of C-10, C-11, C-12 and how they interact with the base criteria.

**C-10 origin — V-01 (Table-centric)**
V-01 pre-printed the 9-row namespace table with explicit placeholder cells per row. The scorecard noted V-02's weakness: "empty-namespace display depends on 'Show all 9' instruction holding rather than structural impossibility." C-10 formalizes the stronger structural approach.

**C-11 origin — V-03 (Lifecycle / 3-Phase)**
V-03 received the highest C-04 praise despite being truncated: "If you write to disk, the skill fails regardless of output quality. Check before Phase 3." Named phases convert the display-only contract from a passive rule into an active execution gate the model checks at runtime.

**C-12 origin — V-04 (Gap-first ordering)**
The scorecard noted V-04 as having "the strongest C-02 correctness guarantee of any single-axis variation." When gaps are enumerated first, the coverage percentage is computed as a summary of a known list — the contradiction failure mode is closed structurally rather than caught after the fact.

**Interaction with base criteria**
- C-10 strengthens C-06: a C-10 pass implies C-06 pass, but not vice versa.
- C-11 strengthens C-04: a C-11 pass implies C-04 pass, but not vice versa.
- C-12 strengthens C-02: a C-12 pass makes the C-02 second fail condition unreachable by design.
