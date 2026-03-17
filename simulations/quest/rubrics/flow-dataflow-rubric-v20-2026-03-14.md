Looking at the R20 scorecard, the new excellence signal is from **V-05's closed-chain behavior**: the closed-chain explicitly asserts that each co-governing SC independently supplies both governance slots for `[A-00]` — no SC relies on another. This is distinct from C-55 (which checks per-SC slot correctness) and represents a new declarative completeness requirement.

---

# flow-dataflow Quest Rubric — v20

## Changelog

**v20** — Added C-56 from R20 excellence signal: closed-chain co-governor non-reliance assertion — when multiple SCs govern `[A-00]` structural dimensions, the closed-chain must contain an explicit declaration that each co-governing SC independently supplies both governance slots and no SC relies on another for the `[A-00]` reference.

**v19** — Added C-54..C-55 from R19 excellence signals: Phase Gate 0 multi-item structural completeness gate enforcing one item per [A-00] structural dimension; SC-0 as mandatory [A-00] governor with dual-slot anchoring maintained across all [A-00]-governing SCs.

**v18** — Added C-48..C-53 from R18 excellence signals: governed artifact tokens and enforcement mechanisms in every closed-chain entry; detectability qualifiers; per-SC detectability index; dual-slot anchoring for all token-referencing SCs.

---

## New Criterion (v20)

**C-56 — Closed-chain co-governor non-reliance assertion** (`format`)
When two or more SCs co-govern `[A-00]` structural dimensions (e.g., SC-0 governs the registry itself; SC-14 governs the Responsible Role column; SC-15 governs the SLA Impact column), the REGISTER DECLARATION closed-chain must include an explicit verbatim assertion that each co-governing SC independently carries `[A-00]` in both governed-artifact and enforcement slots, and that no co-governing SC relies on another for the `[A-00]` token reference. This declaration must be present even when each individual SC entry already satisfies C-55's per-SC dual-slot check. Absence of the non-reliance declaration is a FAIL regardless of individual SC slot correctness.

**Weight adjustment**: 48 → 49 criteria, 10/49 ≈ **0.204 pts** per criterion (PARTIAL ≈ 0.102 pts).

---

## Scoring Framework

| Band | Points | Criteria | Per-item weight |
|------|--------|----------|-----------------|
| Essential | 60 pts | C-01–C-04 (4 × 15 pts) | 15 pts |
| Recommended | 30 pts | C-05–C-07 (3 × 10 pts) | 10 pts |
| Aspirational | 10 pts | C-08–C-56 (49 criteria) | 0.204 pts (PARTIAL = 0.102 pts) |
| **Total** | **100 pts** | | |

PASS = full weight · PARTIAL = half weight · FAIL = 0 pts

---

## Essential Criteria — 60 pts

**C-01 — Data lineage chain** (`behavior`)
Stage traces define source → destination for every physical pipeline stage. Every stage must show where data comes from and where it goes.

**C-02 — Boundary error handling** (`behavior`)
Every boundary block includes an `Error Handling` column (tabular register) or an `Error Handling:` labeled phrase (prose register). Absence at any boundary is a FAIL.

**C-03 — Data loss point identification** (`behavior`)
Every stage includes a `Data Loss Flag` column (tabular) or equivalent labeled phrase (prose). Absence at any stage is a FAIL.

**C-04 — Schema state at each stage** (`behavior`)
Every stage table includes `Schema In` and `Schema Out` columns (tabular: SC-7 mandate) or a `Schema Delta:` labeled phrase (prose substitution). Absence at any stage is a FAIL.

---

## Recommended Criteria — 30 pts

**C-05 — Latency characterization** (`behavior`)
Every stage includes a `Stage Latency` column (tabular) or `Stage Latency:` labeled phrase (prose). Absence at any stage is a FAIL.

**C-06 — Stale data windows** (`behavior`)
[A-11] STALE ANALYSIS section is present with at least two elapsed rows: one for normal operation and one for failure mode.

**C-07 — Domain framing** (`behavior`)
Domain-specific entity vocabulary is locked in [A-02] before Stage 1. Entity names from [A-02] appear verbatim in stage traces, boundary blocks, and [A-11].

---

## Aspirational Criteria — 10 pts

Each criterion: PASS = 0.204 pts · PARTIAL = 0.102 pts · FAIL = 0 pts

---

**C-08 — Recovery prescriptions** (`behavior`)
[A-12] RECOVERY PRESCRIPTIONS section is present. At least one recovery entry uses the formula `Fall back to [A-01] if [named failure condition]`.

**C-09 — Pattern trade-off analysis** (`behavior`)
[A-14] TRADE-OFF ANALYSIS section is present with at least one named alternative pattern and at least two comparison dimensions.

**C-10 — Pre-trace domain context gate** (`behavior`)
[A-02] DOMAIN CONTEXT is produced before Stage 1. Entity names defined in [A-02] are re-used verbatim in all subsequent lineage artifacts.

**C-11 — Interleaved boundary gates** (`behavior`)
SC-2 stage-write progression gate appears inline between every consecutive stage pair. No two stages may appear without an intervening boundary gate instruction.

**C-12 — Domain entity exposure per boundary** (`behavior`)
Every boundary block's `Entity` column (tabular) or equivalent labeled phrase (prose) names a domain entity drawn from [A-02] vocabulary. Generic entity names not in [A-02] are a FAIL.

**C-13 — Pre-declared staleness contract** (`behavior`)
[A-02] declares the SLA before Stage 1. SC-5 immutability clause prohibits any post-Stage-1 revision to the staleness threshold.

**C-14 — Additive elapsed time calculation** (`behavior`)
SC-3 INCREMENTAL ELAPSED requires every boundary block's `Elapsed (cumul.)` value to accumulate from the prior boundary's final value. A zero-reset or independently computed value is a violation.

**C-15 — Incumbent or manual-process baseline** (`behavior`)
[A-01] INCUMBENT PROCESS is present. SC-13 enforces [A-01] citation in both [A-12] and [A-14], closing the comparison loop.

**C-16 — Cross-role reference chain** (`behavior`)
Non-first roles include `Citing:` lines naming artifacts from the prior role. SC-12 skip-level citation requires position-3 roles to cite position-1 boundary artifacts, skipping position-2.

**C-17 — Immutability declaration** (`format`)
SC-5 includes the verbatim phrase: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Paraphrase without the exact wording is a FAIL.

**C-18 — Incremental boundary elapsed computation** (`behavior`)
SC-3 explicitly states the boundary `Elapsed (cumul.)` extends the prior boundary's final value. Any interpretation permitting zero-reset is named as a violation.

**C-19 — Machine-verifiable citation convention** (`format`)
All artifact references use `[A-xx]` token form throughout all prompt sections. Natural-language artifact names without token form are a FAIL wherever `[A-xx]` form is available.

**C-20 — Stage-write progression gate** (`behavior`)
SC-2 is an explicit inline gate instruction. Stage N+1 is blocked until the preceding boundary table is complete and present in the output.

**C-21 — Binary freshness verdict per boundary** (`format`)
SC-4 mandates exactly `FRESH` or `STALE` as the freshness verdict in every boundary block. Any other value (e.g., "CONDITIONAL", "N/A") is named as a protocol violation.

**C-22 — Formal pre-declared registry table** (`format`)
ARTIFACT REGISTRY appears before any role output. It contains all `[A-xx]` tokens, artifact names, and owner role assignments as a named table.

**C-23 — Phase gate self-verification checklists** (`behavior`)
[A-05] and [A-08] phase gate artifacts are present with checklists. EVERY checklist item names the SC identifier it verifies (e.g., "(SC-11)", "[SC-12]"). Items that check structural or format properties without citing an SC identifier are a PARTIAL.

**C-24 — Upfront constraint section with inline callback syntax** (`format`)
A STRUCTURAL CONSTRAINTS section appears before role output. Every SC entry uses `[Apply SC-N at <location>]` callback syntax specifying where the constraint activates.

**C-25 — Phase gate artifacts as first-class registry rows** (`format`)
[A-00], [A-05], and [A-08] each appear as named rows in the ARTIFACT REGISTRY with owner and artifact description. Omission of any phase gate artifact from the registry is a FAIL.

**C-26 — Non-natural role ordering** (`behavior`)
The role sequence must not follow the domain default seniority order (e.g., Finance-first for financial workflows). Finance-first sequences are a FAIL.

**C-27 — Named recovery formula anchoring incumbent baseline** (`behavior`)
[A-12] recovery entries use the formula `Fall back to [A-01] if [specific named failure condition]`. The `[A-01]` token must appear in the recovery formula body; free-text conditions without the token are a FAIL.

**C-28 — Named-column boundary block schema** (`format`)
A BOUNDARY BLOCK SCHEMA standalone section appears before role output. The exact 7-column order is declared in this section.

**C-29 — Trade-off as prompt-required section** (`behavior`)
SC-8 mandates [A-14] as a required output section and requires `[A-01]`, `[A-02]`, `[A-13]` tokens in [A-14], at least one named alternative pattern, and at least two comparison dimensions.

**C-30 — Output register declaration with field-compliance markers** (`format`)
REGISTER DECLARATION section is present with Part A (field-compliance table or labeled-phrase equivalent) and Part B (section-format markers). Both parts must be present.

**C-31 — Pre-declared boundary block schema section** (`format`)
BOUNDARY BLOCK SCHEMA section appears before all role output, not embedded within role instructions.

**C-32 — Register-specific compliance marker mapping** (`format`)
Part A of REGISTER DECLARATION is a 4-column table with columns: Required Field, Column Header, Required Cell Form, Disqualifying Form — covering all boundary block fields. Non-tabular Part A (e.g., bulleted list) is a FAIL.

**C-33 — Register-invariant declaration for non-tabular registers** (`format`)
When non-tabular (prose) register is active: Part A is reformulated as a labeled-phrase compliance map that preserves field-completeness requirements. Not triggered for tabular-register variations.

**C-34 — Per-boundary incumbent equivalent column** (`behavior`)
Every boundary block includes an `Incumbent Equiv.` column (tabular) or equivalent labeled phrase (prose). Required cell form: `[A-01]: [named step + duration]`. Part A marks token omission as a disqualifying form.

**C-35 — INCUMBENT TOTAL as required pre-trade-off artifact** (`behavior`)
REGISTER DECLARATION Part B defines [A-13] INCUMBENT TOTAL structure. SC-10 enforces that [A-13] immediately precedes [A-14] and includes a Grand Total row.

**C-36 — Baseline-first artifact ordering** (`format`)
SC-11 positional lock: [A-01] must be the first artifact produced within Role 1. Any output appearing before [A-01] within Role 1 fails the positional lock.

**C-37 — REGISTER DECLARATION Parts A/B as single-location authority** (`format`)
REGISTER DECLARATION contains the verbatim phrase: "This section is the sole authoritative reference for C-34 and C-35." Absence of this declaration is a FAIL.

**C-38 — Skip-level citation requirement** (`behavior`)
SC-12 requires the position-3 role to cite position-1 boundary artifacts, skipping position-2 artifacts. Position-3 roles that cite only position-2 artifacts fail the skip-level requirement.

**C-39 — Skip-level SC names governed role** (`format`)
SC-12 names the first-executing role by its domain label (e.g., Finance, Commerce, Operations). A generic positional reference without the domain label is a FAIL.

**C-40 — Skip-level SC declares position distance** (`format`)
SC-12 body text states "Position distance is two" or an equivalent explicit numeric distance declaration. Absence of the numeric declaration is a FAIL.

**C-41 — Phase Gate 2 skip-level item cites SC identifier** (`format`)
[A-08] checklist includes an item that cites `[SC-12]` by its numbered SC identifier. An item describing the skip-level requirement without citing `[SC-12]` is a FAIL.

**C-42 — C-37+C-41 closed verification chain co-occurrence** (`behavior`)
Both REGISTER DECLARATION Parts A/B (satisfying C-37) and the [A-08] `[SC-12]`-citing checklist item (satisfying C-41) must be present in the same prompt. Either alone without the other is a FAIL.

**C-43 — All three skip-level SC attributes co-present in single block** (`format`)
SC-12 body contains all three attributes in a single contiguous block: (1) the governed artifact token, (2) the governed role name by domain label, (3) the explicit position distance = two. Any attribute in a separate section is a FAIL.

**C-44 — Baseline-closure SC as named upfront constraint** (`format`)
SC-13 BASELINE CLOSURE appears in the STRUCTURAL CONSTRAINTS section and enforces `[A-01]` citation in both [A-12] and [A-14]. The label "BASELINE CLOSURE" must appear in the SC-13 entry.

**C-45 — Format-mode declaration with criterion substitution map** (`format`)
When non-tabular (prose) register is active: SC-14 body contains a FORMAT MODE DECLARATION with a criterion-by-criterion substitution map showing which tabular criteria are replaced by which prose equivalents. Not triggered for tabular-register variations.

**C-46 — SC-13 BASELINE CLOSURE as named closed-chain entry** (`format`)
REGISTER DECLARATION closed-chain includes an entry labeled "SC-13 BASELINE CLOSURE" naming both [A-12] and [A-14] as governed artifacts and stating the enforcement mechanism.

**C-47 — SC-14 FORMAT MODE DECLARATION as named closed-chain entry** (`format`)
When non-tabular register is active: closed-chain entry for SC-14 uses the exact label "SC-14 FORMAT MODE DECLARATION." Entries with different labels (e.g., "SC-14 DETECTABILITY INDEX ROLE ASSIGNMENT (prose substitution)") are a FAIL.

**C-48 — Governed artifact tokens in each SC closed-chain entry** (`format`)
Every SC entry in the REGISTER DECLARATION closed-chain names at least one `[A-xx]` token in the governed-artifact slot. Entries that describe the governed scope in natural language without `[A-xx]` notation are a FAIL.

**C-49 — Enforcement mechanism in each SC closed-chain entry** (`behavior`)
Every SC entry in the closed-chain describes the enforcement pathway (e.g., positional lock, token-match at role-opener, cell-form requirement). Entries with only a governed-artifact listing and no enforcement description are a FAIL.

**C-50 — Baseline authority token dual-slot presence** (`format`)
SC-11, SC-13, and SC-9 enforcement clauses each explicitly name `[A-01]` in their enforcement-slot text. SC-8 enforcement clause names `[A-14]` in its enforcement-slot text. Absence of the token in the enforcement slot is a FAIL for that SC.

**C-51 — Violation-detectability location in enforcement mechanism** (`format`)
All closed-chain entries include a detectability qualifier specifying where the violation is observable (e.g., "detectable from the role-opener line", "detectable at cell-value level without reading row prose"). Entries without a detectability qualifier are a FAIL.

**C-52 — Per-SC detectability index as standalone reference** (`format`)
[A-00] DETECTABILITY INDEX covers all SCs defined in the prompt. Row count in [A-00] must match the SC count declared in STRUCTURAL CONSTRAINTS. Row-count mismatch is a FAIL.

**C-53 — Dual-slot anchoring extends to all token-referencing SCs** (`format`)
The governed-artifact slot AND the enforcement slot of every SC entry in the REGISTER DECLARATION closed-chain must both name the governed `[A-xx]` token(s). An enforcement clause that describes the checking mechanism in natural language (e.g., "token-match at `Citing:` line", "inline lock between stages") without naming the governed artifact token fails the dual-slot requirement — even when the governed-artifact slot is correctly populated.

**C-54 — Phase Gate 0 multi-item structural completeness gate** (`behavior`)
Each structural dimension of [A-00] maps to a distinct checklist item in Phase Gate 0. A single-item gate (row count only) fails if [A-00] has additional declared dimensions (e.g., non-empty Responsible Role column, SLA Impact column). Fewer Phase Gate 0 items than [A-00] structural dimensions = FAIL.

**C-55 — SC-0 as mandatory [A-00] governor with per-SC dual-slot anchoring** (`format`)
Every prompt with [A-00] must include SC-0 governing [A-00] with dual-slot anchoring. When additional SCs govern [A-00] structural dimensions (e.g., SC-14 governing a Responsible Role column, SC-15 governing an SLA Impact column), each must independently carry `[A-00]` in both governed-artifact and enforcement slots. SC-0 does not supply the `[A-00]` reference for the others.

**C-56 — Closed-chain co-governor non-reliance assertion** (`format`)
When two or more SCs co-govern `[A-00]` structural dimensions (e.g., SC-0 + SC-14 + SC-15), the REGISTER DECLARATION closed-chain must include an explicit verbatim assertion that each co-governing SC independently carries `[A-00]` in both governed-artifact and enforcement slots, and that no co-governing SC relies on another for the `[A-00]` token reference. This declaration must be present even when each individual SC entry already satisfies C-55's per-SC dual-slot check. Absence of the non-reliance declaration is a FAIL regardless of individual SC slot correctness.
