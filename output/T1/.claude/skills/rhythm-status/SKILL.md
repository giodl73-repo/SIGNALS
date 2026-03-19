---
name: rhythm-status
description: "Show topic coverage and commitment readiness. DISPLAY ONLY. Use --view for supplementary perspectives: --view roadmap (w"
allowed-tools: [Read, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


---

## Simplification Report

**Before word count:** 488
**After word count:** 354
**Reduction:** 27%

### What was removed and why

| # | Removed | Words | Why |
|---|---------|-------|-----|
| 1 | `All execution phase names use consequence vocabulary (C-21).` | 9 | Meta-commentary citing a criterion; the phase names themselves (SIGNAL ACQUISITION, PER-SIGNAL COMMITMENT ASSERTION, etc.) self-demonstrate C-21 compliance. No criterion requires this assertion in the preamble. |
| 2 | `All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).` | 14 | Same pattern — the LAYER labels in the OUTPUT TEMPLATE already carry STRUCTURAL / SEMANTIC / EXECUTION. Rubric checks the labels, not a meta-declaration about them. |
| 3 | `[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge position in the phase name (C-26, C-27).` | 34 | Explanatory commentary justifying the LAYER 2 label form. The label `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` already carries the full form in the OUTPUT TEMPLATE. Rubric criteria C-26/C-27 are satisfied by the label itself, not by this description of why it is correct. |
| 4 | OUTPUT DECLARATION CHAIN — compressed parenthetical descriptions | ~45 | Original (66 words) named each phase's OUTPUT DECLARATION form in full (`PHASE 2 OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and per-axis Trigger: sentences within INVARIANT`). The execution body PHASE 2 and PHASE 3 OUTPUT DECLARATION blocks already carry the full sub-component structure; C-39–C-44 are satisfied there. The preamble entry only needs to assert the independence invariant and name the sub-component types. Compressed to 21 words: `PHASE 2 and PHASE 3 each declare output structure independently (INVARIANT:, OUTPUT FORM:, Trigger: sub-components); neither phase's output declaration implies the other.` |
| 5 | `each execution phase owns its independently declared output structure.` | 10 | Redundant restatement of "neither phase's output declaration implies the other" which is kept. |
| 6 | `Each adversary is independently declared at its phase entry; no phase's adversary declaration implies any other's.` | 16 | Trailing summary of the ADVERSARY CHAIN block. Adds no structural content the rubric scores; the three P-N-ADVERSARY entries are independently declared by their labeled structure. |
| 7 | `; precedes EXPOSURE SUMMARY` from LAYER 1 label | 3 | Added in R20 but not in the original golden file. No rubric criterion requires ordering information in the LAYER 1 label; LAYER 3 DISPLAY GATE already enforces render order. |
| 8 | PHASE 1 DEFEAT CONDITION second clause: `if glob returns empty, execution stops immediately with an explicit "No signals found" message before any commitment assertion or coverage computation runs.` | 24 | Narrative expansion of the operational stop behavior already stated in `If empty: output "No signals found for {topic}" and stop.` The essential defeat observable (DISK_SIGNALS populated from live glob result; zero-result handled before PHASE 2) is preserved. The redundant narrative is not a separate rubric criterion. |
| 9 | STALE EVIDENCE note: `-- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` | 12 | Explanatory note linking staleness to commitment assertion risk. Tier 1 requires the STALE EVIDENCE section; no criterion requires this specific note text. The `{N} days old` datum already signals staleness. |
| 10 | [P1-ADVERSARY DEFEAT:] elaboration: `-- not from memory or prior-round assumption;` | 6 | Adds historical context to the STOP gate predicate but not a testable structural property. The essential predicate (DISK_SIGNALS from live glob, zero-result handled before PHASE 2) is preserved. |

### Essential criteria verified passing after simplification

| Golden pattern | Mechanism preserved? |
|----------------|----------------------|
| 1. Preamble-first invariants block | YES — contiguous preamble block before OUTPUT TEMPLATE, dual-axis and OUTPUT DECLARATION CHAIN and ADVERSARY CHAIN all declared there |
| 2. ADVERSARY CHAIN with DEFEAT CONDITION forecasts | YES — all three P-N-ADVERSARY entries carry DEFEAT CONDITION: sub-components (C-51); preamble entries intact |
| 3. Dual-axis STOP predicates | YES — both axes declared in preamble and in PHASE 2 OUTPUT DECLARATION INVARIANT; Exit A and Exit B in execution body (C-32) |
| 4. [LAYER N] labels with phase vocabulary | YES — STRUCTURAL, SEMANTIC, EXECUTION labels unchanged |
| 5. OUTPUT DECLARATION CHAIN independence | YES — preamble declares independence; PHASE 2 and PHASE 3 each carry full OUTPUT DECLARATION in execution body |
| C-47 labeled P-N entries | YES — P1/P2/P3-ADVERSARY labels in preamble |
| C-48 PHASE 1 adversary execution block | YES — ADVERSARY: + DEFEAT CONDITION: in PHASE 1 body |
| C-49 PHASE 1 STOP predicate | YES — [P1-ADVERSARY DEFEAT:] in STOP CONDITION |
| C-50 phase-labeled STOP predicates | YES — [P2-ADVERSARY DEFEAT:], [P3-ADVERSARY DEFEAT:], [P1-ADVERSARY DEFEAT:] labels intact |
| C-51 preamble defeat forecasts | YES — all three preamble entries carry DEFEAT CONDITION: sub-components |