## R12 Scoring — `draft-brainstorm` (v12 rubric, 165 pts max)

---

### Composite Scores

| Rank | Variation | Score | All-Ess | C-15 | C-35 | C-36 |
|------|-----------|-------|---------|------|------|------|
| 1 (tied) | **V-01** AMEND-first + Pre-Phase + Phase 0 | **165** | YES | PASS | PASS | PASS |
| 1 (tied) | **V-03** Maximal lifecycle gate verbosity | **165** | YES | PASS | PASS | PASS |
| 1 (tied) | **V-04** Conversational register | **165** | YES | PASS | PASS | PASS |
| 4 (tied) | **V-02** Prose-categories (C-15 FAIL intentional) | **162.5** | YES | FAIL | PASS | PASS |
| 4 (tied) | **V-05** Prose-categories + lifecycle (C-15 FAIL intentional) | **162.5** | YES | FAIL | PASS | PASS |

---

### Per-Variation Summaries

#### V-01 — AMEND-First + Pre-Phase Lenses + Phase 0 Inertia — **165/165**

Architecture: Pre-Phase (lenses) → `## Phase 0` (Do Nothing, 4 fields, explicit close "Phase 0 is now complete... Phase 1 opens below") → `## Phase 1` (pool, 6 mandatory `##` dimensions).

| Key criteria | Result | Evidence |
|---|---|---|
| C-35 Phase-0 Inertia Prefacing | **PASS** | Dedicated `## Phase 0` heading; close callout names "Phase 0 is now complete... Phase 1 opens below" before Phase 1 heading; `##` reserved for phases only |
| C-36 Net-Count Volume | **PASS** | "19-39 additional candidates...total of 20-40 ideas including the Phase 0 Do Nothing entry" |
| C-15 Structural Spine | PASS | 6 mandatory `##` sections named, "do not collapse" |
| C-01 through C-34 | All PASS | Inherited from V-03 R11 backbone |

**Diagnostic result**: Pre-Phase label + Phase 0 label is a valid C-35 architecture. An unnumbered "Pre-Phase" for lenses does not disqualify the subsequent "Phase 0" from satisfying C-35 — the inertia block retains its own dedicated phase with a hard boundary.

---

#### V-02 — Prose-Categories (C-15 FAIL intentional) — **162.5/165**

Architecture: `## Phase 0` → `## Phase 1` (bold category headers, not `##` sections for ideas) → `## Phase 2` → `## Phase 3`.

| Key criteria | Result | Evidence |
|---|---|---|
| C-35 Phase-0 Inertia Prefacing | **PASS** | `## Phase 0` closes "Phase 0 is complete. Phase 1 opens below." before `## Phase 1`; `##` phase headings remain unambiguous against `**bold**` idea categories |
| C-36 Net-Count Volume | **PASS** | "19-39 additional candidates...total pool of 20-40 including the Phase 0 Do Nothing entry" |
| C-15 Structural Spine | **FAIL** | Bold idea labels only; dimension names are examples ("e.g., scope, timing..."), not mandated `##` output sections |
| C-01 through C-34 (ex C-15) | All PASS | |

---

#### V-03 — Maximal Lifecycle Gate Verbosity — **165/165**

Architecture: `## Phase 0` (open tag "*Phase 0 opens now. No preconditions.*", 4 fields, close `> **Phase 0 is now complete.**...Phase 1 may begin.`) → `## Phase 1` → `## Phase 2` → `## Phase 3`. Every phase boundary doubly-marked: open tag + close blockquote.

| Key criteria | Result | Evidence |
|---|---|---|
| C-35 Phase-0 Inertia Prefacing | **PASS** | Doubly-marked hard boundary: close blockquote + `---` separator + `## Phase 1` heading; no ambiguity |
| C-36 Net-Count Volume | **PASS** | Two anchors: Phase 1b instruction "19-39 additional candidates...total pool of 20-40" AND Phase 1 close tag "19-39 net-new ideas + Do Nothing = 20-40 total" |
| C-15 Structural Spine | PASS | 6 mandatory `##` sections, "do not collapse...do not omit any" |
| C-33 Dual-Anchor Verbatim | PASS | Column rule + Phase 3 GATE callout; Phase 2 close tag provides additional redundant anchor |

**Excellence signal**: V-03 is the first to carry a second C-36 anchor inside the phase-close tag — the net-count formula appears at both instruction-time and completion-time, creating dual enforcement.

---

#### V-04 — Conversational Register — **165/165**

Architecture: Same phase structure, but second-person informal throughout ("don't mark top-5 yet", "Phase 0 is done", "Phase 1 opens now", "can't begin").

| Key criteria | Result | Evidence |
|---|---|---|
| C-35 Phase-0 Inertia Prefacing | **PASS** | `### Phase 0` close: "Phase 0 is done. The Do Nothing entry goes in the Status Quo section of Phase 1...Phase 1 opens now." Hard boundary before `### Phase 1` |
| C-36 Net-Count Volume | **PASS** | "19-39 additional ideas...for a total of 20-40 including Do Nothing from Phase 0" — net-count + total + relationship all explicit |
| C-15 Structural Spine | PASS | "You need these sections in your output -- each as a `##` heading" with 6 named sections |
| C-33 Dual-Anchor Verbatim | PASS | Conversational phrasing preserves schema element names (Selected?, all 5 rows, blank) verbatim in both anchors |

**Excellence signal**: Conversational register does not dilute precision criteria. C-36's net-count formula and C-33's verbatim schema element requirements both survive second-person informal phrasing without degrading to approximation ("around 20-40") or paraphrase.

---

#### V-05 — Prose-Categories + Lifecycle (C-15 FAIL intentional) — **162.5/165**

Architecture: `## Phase 0` with open/close lifecycle tags → `## Phase 1` (bold idea categories, 4-7 distinct, advisory dimension names) → `## Phase 2` → `## Phase 3`.

| Key criteria | Result | Evidence |
|---|---|---|
| C-35 Phase-0 Inertia Prefacing | **PASS** | `## Phase 0 -- Inertia Baseline` closes "> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens below." before `## Phase 1` |
| C-36 Net-Count Volume | **PASS** | Two anchors: Phase 1b "19-39 additional candidates...total pool of 20-40" AND Phase 1 close "Pool of 19-39 net-new ideas + Do Nothing (total 20-40) written" |
| C-15 Structural Spine | **FAIL** | Prose-categories with advisory dimension names; `##` reserved for phases only |

---

### Excellence Signals

**1. Pre-Phase + Phase 0 is a valid C-35 architecture**
V-01 confirms the diagnostic: an unnumbered "Pre-Phase" block for lenses, followed immediately by a numbered "Phase 0" dedicated exclusively to inertia, satisfies C-35. The criterion requires the inertia block to be in a dedicated pre-generation phase — it does not require Phase 0 to be the first thing in the prompt. This resolves R11's V-01 failure, where lenses were embedded inside Stage 0 alongside inertia, eliminating the hard boundary.

**2. Phase close tags as second C-36 anchor**
V-03 and V-05 demonstrate that echoing the net-count formula inside the phase-close blockquote ("Pool of 19-39 net-new ideas + Do Nothing (total 20-40) written") creates a second C-36 anchor at pool-completion time. This is additive — the model encounters the count constraint twice: once when receiving the generation instruction, once when it fires the completion signal.

**3. Conversational register is precision-safe**
V-04 confirms that informal second-person phrasing ("don't", "can't", "Phase 0 is done", "Phase 1 opens now") does not soften precision criteria. The net-count formula (C-36), schema element verbatim names (C-33: "Selected?", "all 5 rows", "blank"), and inversion framing (C-34: "so the comparison can pass") all survive register informality intact.

**4. Prose-category `**bold**` headers are categorically distinct from `## Phase N` headings**
V-02 and V-05 confirm that when ideas use bold-header prose grouping, the `##` phase headings remain unambiguous phase markers. The feared blurring of phase boundaries in prose-category format did not occur — heading level (`##`) vs inline bold (`**`) is a sufficient categorical distinction for C-35.

---

### R12 Conclusion

All five variations pass all five essential criteria. The R12 ceiling hypothesis is confirmed: C-35 and C-36 are structurally stable across all five variation axes — AMEND-first sequencing, prose-category output, maximal lifecycle verbosity, conversational register, and combinations. The Pre-Phase + Phase 0 architecture (V-01, V-04) successfully recovers C-35 for AMEND-first designs. The only cost is the intentional C-15 sacrifice in V-02 and V-05.

**The 165 ceiling is achievable by three independent structural paths**: (1) AMEND-first with Pre-Phase lenses + Phase 0, (2) maximal lifecycle open/close gate tags, (3) conversational register — any one of which, combined with `##`-based idea grouping and the net-count formula, achieves the maximum.

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["Pre-Phase label before Phase 0 is a valid C-35 architecture -- inertia block can be Phase 0 even when an unnumbered Pre-Phase precedes it for lenses", "Conversational second-person register does not dilute C-36 net-count precision or C-33 verbatim schema element requirements", "Phase close tags can carry a second C-36 anchor echoing the net-count formula at pool-completion time, creating redundant enforcement"]}
```
