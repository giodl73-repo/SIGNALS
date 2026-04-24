I have all five variations fully read. Now I'll score them.

---

## trace-component · Round 11 Scorecard

**Rubric**: v11 · **Ceiling**: 148 pts · **Variations**: V-01 through V-05
**Ground truth**: placeholder (prompt-design evaluation — predicted compliance scoring)

---

### Scoring Architecture

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-37 | 2 | 58 |
| **Total** | | | **148** |

Partial scores (1 pt) apply when a criterion is structurally attempted but not fully closed. Binary fail = 0.

---

### Shared Baseline (applies to all five variations)

All variations build on the R10-winning template architecture. The following criteria pass identically across all five:

**Essential — PASS (12 pts each):** C-01, C-02, C-03, C-04, C-05
All five tables (TABLE-1 through TABLE-6) present with required blank-blocked columns. Framework Declaration gates analysis in all.

**Recommended — PASS (10 pts each):** C-06, C-07, C-08
TABLE-5 side effects explicit zero-row; TABLE-7 five mandatory rows with N/A prohibited; Framework Declaration + declared terms enforced.

**Aspirational — PASS (2 pts each):** C-09, C-10, C-11, C-13, C-14, C-15, C-16, C-17, C-18, C-20, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35

Notes on shared aspirational passes:
- **C-10**: `Re-renders? [Yes (N) / No]` co-locates count and verdict in the same cell — present in all TABLE-4 variants
- **C-11**: All have ≥ 3 phase-close gate statements; V-01/V-04 have 6, V-03/V-05 have 5, V-02 has 3 (GATE-3, GATE-7, plus "Invalid:" at TABLE-1 = 3 minimum satisfied)
- **C-14**: TABLE-4's `Re-renders? [Yes (N) / No]` and `Necessary? [Yes — reason / No — reason]` headers embed fill constraints in all variants; V-01/V-03/V-04/V-05 additionally embed in the Direction column header
- **C-17**: Triple lock passes via the Direction column (V-01/V-03/V-04/V-05: mandatory + header-embedded + GATE-2 names "blank Direction cell") or via TABLE-7's `Finding [finding or "none detected — [reason]"]` column (all variants: mandatory + header-embedded + GATE-7 names escape strings)
- **C-33**: All have per-phase manifests (MANIFEST-1 through MANIFEST-4+) with all three required fields (components in scope, state keys, side effects)
- **C-34**: INERT-HOP DECLARATION mandatory footer present in all

**Aspirational — FAIL (0 pts):**
- **C-12** — Mandatory Comparison Column: No variation includes a "What this adds vs. ad-hoc" or equivalent comparison column in any table. Consistent fail across all. This is the criterion that produced R10's -1 pt as a PARTIAL; in v11 it remains unaddressed and scores 0 (not PARTIAL) because there is no structural attempt at a comparison column in any variation.

**Aspirational — PARTIAL (1 pt):**
- **C-21** — Failure Mode Displacement: All variations intercept escape strings via [GATE-N:] blocks that name specific prohibited phrases. This creates structural prevention but not explicit output displacement text (the pass condition requires the OUTPUT to contain "NOT 'state updates' — Owner: CartStore, Key: items, Old: [], New: [...]"). Gates block the phrase without instructing the model to write the replacement format explicitly. 1/2 pts across all.

*Note on R10 V-03's 143/144: With C-12 at 0 and C-21 at 1, the pre-v11 baseline = 144 − 2 (C-12 fail) − 1 (C-21 partial) = 141. But R10 V-03 scored 143/144. Reconciliation: under the R10 rubric (ceiling 144 = 27 aspirational × 2 + 90), C-12 was likely PARTIAL (1 pt) rather than FAIL — some partial attempt via the Criteria Audit TABLE-8 structure could be argued as a comparison artifact. For v11 scoring I treat C-12 as FAIL (0) since no comparison column exists, but this 1-pt discrepancy with R10 is noted.*

---

### Variation-Specific Criteria

---

#### C-36 · Inert-as-Default Direction Schema

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| **V-01** | **PASS** (2) | Direction column header literally embeds: `Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide]`. Inert is first and labeled "(default)". Active hops replace by column-position, not instruction. C-14 triple-lock satisfied simultaneously — column header carries the enforcement at cell-write time. GATE-2 closes "blank Direction cell" and "inert noted only in Notes column." |
| **V-02** | **PASS** (2) | Numbered permitted-values list positions `<-> inert` first with "(default)" annotation. Column header is plain "Direction" but C-36 pass condition specifies "the traversal schema's Direction column lists `<-> inert` as the first and default permitted value" — the numbered list is the Direction column's value schema. Active-codes-first fails; inert-as-trailing fails. Neither applies. GATE-2 not visible in V-02 (no explicit [GATE-2:] block), but the rule block enforces blank-cell prohibition via "Direction required per row." PARTIAL risk avoided. |
| **V-03** | **PASS** (2) | SCHEMA CHARTER declares Organizational Principle 2: "Direction column defaults to `<-> inert`. Every hop is inert unless an active departure code is declared." Column header in TABLE-2 also embeds `Direction [<-> inert (default) \| ...]`. Dual enforcement: charter-level declaration + column-header enforcement. Strongest conceptual framing (model "authored" the principle). |
| **V-04** | **PASS** (2) | Column header embedding (identical to V-01) plus explicit rules block: "Direction header lists `<-> inert` first — this is the default, not an option. Departure codes are replacements." GATE-2 closes blank Direction cell and blank Role cell. Combines V-01's column-header mechanism with explicit prose reinforcement. |
| **V-05** | **PASS** (2) | TRAVERSAL-SCHEMA (Role 1 artifact) declares: "Default value: `<-> inert` / Rationale: Every traversal hop is inert until a departure is declared. This inverts the annotation burden..." Column header in TABLE-2 (Role 2) embeds `[<-> inert (default) \| ...]`. Author-vs.-follower mechanism: violating inert-default in Role 2 contradicts model's own TRAVERSAL-SCHEMA artifact. |

C-36 = **PASS (2 pts) for all five variations.**

---

#### C-37 · Manifest-Analysis Paired Block Structure

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| **V-01** | **PASS** (2) | Each MANIFEST close includes: `*(required gate — fill completely before writing TABLE-N; TABLE-N begins immediately below this block with no intervening content)*`. 4 MANIFEST-TABLE pairs (MANIFEST-1/TABLE-1 through MANIFEST-4/TABLE-4) with matching N labels. Instruction is embedded in every manifest, meeting ≥3 pairs. Compliance risk: instruction is in the manifest header (before the manifest content), not at the manifest CLOSE. A model might technically insert content between the manifest fields and the table. Risk: low but non-zero. |
| **V-02** | **PASS** (2) | `↓ TABLE-N begins immediately below. No content may appear between this line and the TABLE-N header.` embedded as the closing line of every MANIFEST (MANIFEST-1 through MANIFEST-5). This is the structural HIGH-WATER MARK for C-37: the prohibition is at the exact point where violation would occur — the moment the manifest closes. A model that inserts content after writing this line contradicts its own prior output. 5 pairs exceed ≥3 minimum. |
| **V-03** | **PARTIAL** (1) | SCHEMA CHARTER declares Organizational Principle 1: "MANIFEST-N / TABLE-N adjacent pairs. Each manifest immediately precedes its analysis table. No content appears between MANIFEST-N and TABLE-N." 4 pairs required by charter. However, individual manifest blocks in V-03 do NOT carry the adjacency marker (`↓ TABLE-N begins immediately below`) at their close — the constraint lives only in the charter preamble. A model following the charter correctly produces compliant output, but the charter is declared ONCE at document head; drift across phases is possible without point-of-production reinforcement. Compact 3-line manifests (`In scope: ___ | State keys: ___ | Side effects: ___`) compress the manifest→table gap, reducing but not eliminating drift risk. PARTIAL: criterion is structurally intended but enforcement mechanism is weaker than V-02's close-embedded marker. |
| **V-04** | **PASS** (2) | Combines V-01-style manifest header instruction + V-02-style `↓ TABLE-N begins immediately below` close marker. Every MANIFEST in V-04 opens with "(fill all three fields before proceeding)" AND closes with the `↓` marker. MANIFEST-1 through MANIFEST-4 each carry both enforcement points. Two independent mechanisms close two different escape paths: the header instruction signals the upcoming table, the close marker prohibits interstitial content at point of production. |
| **V-05** | **PARTIAL** (1) | TRAVERSAL-SCHEMA declares paired-block design in Role 1: "MANIFEST-N / TABLE-N adjacent pairs. No content may appear between MANIFEST-N and TABLE-N." Role 2 manifests reference the schema with `*(per TRAVERSAL-SCHEMA — TABLE-N follows MANIFEST-N immediately)*` at the TABLE open. However, MANIFEST blocks in Role 2 (MANIFEST-1 through MANIFEST-4) carry no `↓` close marker and no inline adjacency gate. Enforcement relies entirely on cross-referencing the Role 1 artifact — a 700-token gap. Role-drift risk: model may not maintain TRAVERSAL-SCHEMA constraints through all 4+ phases of Role 2 execution. The TABLE-N note `*(per TRAVERSAL-SCHEMA)` is a cue at table-open, not a prohibition at manifest-close. PARTIAL. |

---

#### C-19 · Gate-Block Formalism Not Substitutable by Imperative Prohibition

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| **V-01** | PASS (2) | All gates in [GATE-N: ...] bracketed format: GATE-1 through GATE-7 present. |
| **V-02** | **PARTIAL** (1) | TABLE-1 closes with: `Invalid: "the button", "a click", "the handler", "N/A", blank.` This is prose enumeration, not a [GATE-1:] block. C-19 requires ALL prohibited escape strings in gate-block format. GATE-3 and GATE-7 use correct formalism, but TABLE-1's prohibition uses imperative prose. Partial: most gates comply; one does not. |
| **V-03** | PASS (2) | GATE-1 through GATE-7 all in [GATE-N: Does not close on...] format. |
| **V-04** | PASS (2) | GATE-1 through GATE-7 all in [GATE-N: ...] format. |
| **V-05** | PASS (2) | GATE-1 through GATE-7 all in [GATE-N: ...] format. |

---

### Per-Variation Score Computation

#### V-01 — Inertia Framing (Direction Column Header)

| Criterion | Pts | Note |
|-----------|-----|------|
| C-01 through C-05 | 60/60 | All essential PASS |
| C-06 through C-08 | 30/30 | All recommended PASS |
| C-09–C-11, C-13–C-18 | 18/18 | Aspirational tier A PASS |
| **C-12** | **0/2** | No comparison column |
| **C-19** | **2/2** | All gates in [GATE-N:] format |
| C-20–C-20 | 2/2 | Framework Declaration PASS |
| **C-21** | **1/2** | Gates block phrases; no displacement text produced |
| C-22–C-35 | 28/28 | Aspirational tier B PASS |
| **C-36** | **2/2** | Column header embeds inert-as-default |
| **C-37** | **2/2** | Inline manifest instruction gates adjacency |
| **TOTAL** | **145/148** | |

---

#### V-02 — Lifecycle Emphasis (↓ Adjacency Marker Native)

| Criterion | Pts | Note |
|-----------|-----|------|
| C-01 through C-05 | 60/60 | All essential PASS |
| C-06 through C-08 | 30/30 | All recommended PASS |
| C-09–C-11, C-13–C-18 | 18/18 | Aspirational tier A PASS |
| **C-12** | **0/2** | No comparison column |
| **C-19** | **1/2** | TABLE-1 uses "Invalid:" prose; GATE-3/GATE-7 correct |
| C-20–C-20 | 2/2 | Framework Declaration PASS |
| **C-21** | **1/2** | PARTIAL — same as baseline |
| C-22–C-35 | 28/28 | Aspirational tier B PASS |
| **C-36** | **2/2** | Numbered list positions `<-> inert` first with "(default)" |
| **C-37** | **2/2** | `↓ TABLE-N begins immediately below` close marker — strongest C-37 mechanism |
| **TOTAL** | **144/148** | |

---

#### V-03 — Output Format (SCHEMA CHARTER as Organizational DNA)

| Criterion | Pts | Note |
|-----------|-----|------|
| C-01 through C-05 | 60/60 | All essential PASS |
| C-06 through C-08 | 30/30 | All recommended PASS |
| C-09–C-11, C-13–C-18 | 18/18 | Aspirational tier A PASS |
| **C-12** | **0/2** | No comparison column |
| **C-19** | **2/2** | GATE-1 through GATE-7 all gate-block format |
| C-20–C-20 | 2/2 | Framework Declaration PASS (SCHEMA CHARTER) |
| **C-21** | **1/2** | PARTIAL — same as baseline |
| C-22–C-35 | 28/28 | Aspirational tier B PASS |
| **C-36** | **2/2** | Charter principle 2 + column header embedding |
| **C-37** | **1/2** | Charter principle 1 only; no `↓` marker at manifest close — drift risk |
| **TOTAL** | **144/148** | |

---

#### V-04 — Combined: C-36 + C-37 Maximum Enforcement

| Criterion | Pts | Note |
|-----------|-----|------|
| C-01 through C-05 | 60/60 | All essential PASS |
| C-06 through C-08 | 30/30 | All recommended PASS |
| C-09–C-11, C-13–C-18 | 18/18 | Aspirational tier A PASS |
| **C-12** | **0/2** | No comparison column |
| **C-19** | **2/2** | All gates in [GATE-N:] format |
| C-20–C-20 | 2/2 | Framework Declaration PASS |
| **C-21** | **1/2** | PARTIAL — same as baseline |
| C-22–C-35 | 28/28 | Aspirational tier B PASS |
| **C-36** | **2/2** | Column header embedding (V-01 mechanism) + explicit rules block |
| **C-37** | **2/2** | Both V-01 manifest header instruction + V-02 `↓ TABLE-N` close marker — dual enforcement, non-redundant |
| **TOTAL** | **145/148** | |

---

#### V-05 — Combined: Role Sequence + Inertia Framing

| Criterion | Pts | Note |
|-----------|-----|------|
| C-01 through C-05 | 60/60 | All essential PASS |
| C-06 through C-08 | 30/30 | All recommended PASS |
| C-09–C-11, C-13–C-18 | 18/18 | Aspirational tier A PASS |
| **C-12** | **0/2** | No comparison column |
| **C-19** | **2/2** | All gates in [GATE-N:] format |
| C-20–C-20 | 2/2 | Framework Declaration PASS (TRAVERSAL-SCHEMA) |
| **C-21** | **1/2** | PARTIAL — same as baseline |
| C-22–C-35 | 28/28 | Aspirational tier B PASS |
| **C-36** | **2/2** | TRAVERSAL-SCHEMA author-declaration + column header embedding |
| **C-37** | **1/2** | TRAVERSAL-SCHEMA declaration only; Role 2 manifests lack `↓` close marker; role-drift gap |
| **TOTAL** | **144/148** | |

---

### Summary Score Table

| Rank | Variation | Score | C-36 | C-37 | C-19 | C-21 | C-12 | Delta from ceiling |
|------|-----------|-------|------|------|------|------|------|--------------------|
| 1 (tie) | **V-04** | **145/148** | PASS | PASS | PASS | PARTIAL | FAIL | −3 |
| 1 (tie) | **V-01** | **145/148** | PASS | PASS | PASS | PARTIAL | FAIL | −3 |
| 3 (tie) | **V-02** | **144/148** | PASS | PASS | PARTIAL | PARTIAL | FAIL | −4 |
| 3 (tie) | **V-03** | **144/148** | PASS | PARTIAL | PASS | PARTIAL | FAIL | −4 |
| 3 (tie) | **V-05** | **144/148** | PASS | PARTIAL | PASS | PARTIAL | FAIL | −4 |

---

### Point-Loss Analysis

| Criterion | Loss pattern | Pts lost |
|-----------|-------------|----------|
| C-12 (Comparison Column) | FAIL — all variations | 2 pts each |
| C-21 (Failure Mode Displacement) | PARTIAL — all variations | 1 pt each |
| C-19 (Gate-Block Formalism) | PARTIAL — V-02 only | 1 pt (V-02) |
| C-37 (Manifest-Analysis Paired) | PARTIAL — V-03, V-05 | 1 pt each |

V-04 and V-01 avoid C-19 and C-37 degradations, achieving 145. The 3-pt gap from ceiling = C-12 (2) + C-21 (1).

---

### Ranking

**V-04 = V-01 (145) > V-02 = V-03 = V-05 (144)**

V-04 is the structural bet's payout: the column-header mechanism (C-36, from V-01) and the `↓ TABLE-N` close-marker (C-37, from V-02) are provably non-redundant — the header closes the within-table escape path (blank Direction cell = inert by default), the close-marker closes the block-boundary escape path (content between manifest and table). Neither mechanism degrades C-19, so no regression.

V-01 ties V-04 because its inline manifest gating instruction is strong enough on C-37 to PASS (not merely PARTIAL) — "TABLE-N begins immediately below this block with no intervening content" is embedded in each MANIFEST, just not at the close line. It differs from V-04 only in not having the `↓` close-line marker, which keeps it at PASS but not maximum structural certainty.

V-03 drops to 144 because its SCHEMA CHARTER declares C-37 once at the document head — correct but distant. Without the `↓` marker in individual manifests, phase-level drift becomes a real compliance risk that earns PARTIAL on C-37. The R10 V-03 result (143/144) came from a different point-loss; in R11, V-03's base template is unchanged and the charter approach adds C-36 reliably but C-37 only partially.

---

### Excellence Signals from R11

**ES-1 · Non-redundant mechanism combination closes two independent escape paths without coherence cost**
V-04's bet pays: column-header embedding (C-36) and `↓ TABLE-N` close marker (C-37) target different failure modes — within-table cell escape vs. block-boundary decoupling. A model can silently omit the `↓` marker after satisfying the column header, and vice versa. Having both makes both escape paths structurally unavoidable. Coherence cost is zero because neither mechanism is an elaboration of the other.

**ES-2 · Point-of-production enforcement dominates preamble-level enforcement for structural criteria**
V-03's charter declares the paired-block principle once; V-02 and V-04 repeat it at every manifest close. The close-marker is at the point where violation would occur — a model that writes `↓ TABLE-N begins immediately below` and then inserts content is violating its own prior output. Charter declarations can drift; close-markers cannot. For C-37 compliance, the `↓` marker is the correct enforcement locus.

**ES-3 · Closing Mandate should reinforce both new criteria simultaneously**
V-04's CLOSING MANDATE explicitly names both: "Each MANIFEST-N closes with `↓ TABLE-N begins immediately below` and is followed by TABLE-N with no intervening content. Direction defaults to `<-> inert`; active hops declare departure codes." V-01's mandate covers only C-36 ("Direction cells default to `<-> inert`..."). A closing mandate that names both new criteria simultaneously serves as a final-pass reinforcement preventing late-document drift on either.

**ES-4 · C-12 is the persistent ceiling gap — three structural approaches all fail it**
C-12 (Mandatory Comparison Column) has now failed in every round through R11 without producing even a PARTIAL score. The criterion requires a "What this adds vs. ad-hoc" column populated per row. No TABLE in any variation includes this. The 3-point gap from ceiling (C-12=2 + C-21=1) is structurally consistent. R12 should target C-12 explicitly: adding a comparison column to TABLE-8 (Criteria Audit) mapping each criterion to "its structural enforcement vs. what ad-hoc analysis would miss" may satisfy both C-12 and strengthen C-35 simultaneously.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["non-redundant mechanism combination: column-header inertia default (C-36) paired with point-of-production close-marker (C-37) closes two independent escape paths without coherence cost", "point-of-production enforcement at manifest close dominates charter-level preamble declaration for C-37 compliance — the ↓ marker cannot drift, the charter can", "closing mandate should reinforce both new criteria simultaneously to prevent late-document regression on either"]}
```
