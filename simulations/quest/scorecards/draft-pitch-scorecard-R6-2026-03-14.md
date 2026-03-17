Now I have all five variations. Let me score them against the full v6 rubric.

---

## Scorecard: draft-pitch — Round 6 (v6 Rubric)

**Date**: 2026-03-14
**Rubric version**: v6 (denominator 17 aspirational)
**Base context**: R5 V-05 retroscores 98.24 against v6. R5 V-04 retroscores 99.41.

---

### Scoring Formula

```
Score = (essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/17)*10
```

---

### Criteria Evaluation — All Variations

#### Essential Criteria (C-01 through C-04)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All three versions present | PASS | PASS | PASS | PASS | PASS |
| C-02 | Each version has all four elements | PASS | PASS | PASS | PASS | PASS |
| C-03 | Exec version outcome-first / ROI framing | PASS | PASS | PASS | PASS | PASS |
| C-04 | Anti-positioning section present | PASS | PASS | PASS | PASS | PASS |

All variations: **4/4 essential** → 60 points.

**Evidence C-03**: Phase 4 binary gate enforces "names a cost, risk, or productivity consequence... without mentioning a feature, tool, or product" before EXEC OPENING SENTENCE is locked. All variations inherit this gate.
**Evidence C-04**: Phase 6 produces `## What Signal Is NOT` in all variations.

---

#### Recommended Criteria (C-05 through C-07)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-05 | Dev version shows the tool | PASS | PASS | PASS | PASS | PASS |
| C-06 | Maker version jargon-free | PASS | PASS | PASS | PASS | PASS |
| C-07 | Prior signals consulted | PASS | PASS | PASS | PASS | PASS |

All variations: **3/3 recommended** → 30 points.

**Evidence C-05**: Dev *What It Does* requires "at least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers 'what would I actually type?'"
**Evidence C-06**: Maker Hook instruction: "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology."
**Evidence C-07**: Phase 1 SIGNAL INTAKE checks three prior signal paths; active values table produced before Phase 2.

---

#### Aspirational Criteria (C-08 through C-24)

**C-08 through C-21** — uniform across all variations (all inherit from R5 V-05 baseline which passed 14/17 under v6):

| ID | Criterion | All Variations | Evidence |
|----|-----------|---------------|----------|
| C-08 | Specific traceable proof points | PASS | Phase 7 proof audit: `[source: {artifact-path}]` / `[source: prior signal]` / `[UNVERIFIED]` + Proof fallback in DEFAULTS |
| C-09 | Inertia as primary competitor | PASS | POSITIONING LOCK uses "teams doing nothing — the review that never happened"; Competitor = "not a named tool" |
| C-10 | Exec self-check at generation time | PASS | Phase 4 binary gate: write EOS → gate → rewrite until YES. Not a post-draft checklist. |
| C-11 | Positioning locked in writing before prose | PASS | Phase 3 POSITIONING LOCK and Phase 4 EXEC OPENING SENTENCE both locked before Phase 5 begins |
| C-12 | Default fallbacks for missing signals | PASS | SIGNAL DEFAULTS table with all required fields; Phase 1 waives to DEFAULTS when no signals found |
| C-13 | DEFAULTS TABLE loaded unconditionally before intake | PASS | SIGNAL DEFAULTS at skill top, before Phase 1; "These apply unconditionally to all runs." |
| C-14 | Gate output named and cited by downstream instruction | PASS | AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE all named in *Produces* and cited by exact name in Phase 5 *Consumes* |
| C-15 | Audience belief mapping precedes argument construction | PASS | Phase 2 AUDIENCE BELIEF MAP complete and locked before Phase 5 drafts |
| C-16 | Multi-node named dependency chain | PASS | Three named outputs form forward chain: ABM (P2) → POSITIONING LOCK (P3) → EXEC OPENING SENTENCE (P4) → all consumed by P5 by exact name. Readable from structure alone. |
| C-17 | Belief mapping includes per-audience failure modes | PASS | Failure Mode column: "Name a pitch outcome failure — what the pitch cannot accomplish for this audience." Restatement example explicitly excluded. |
| C-18 | Per-audience inertia fields with structural CTA template | PASS | SIGNAL DEFAULTS has Exec/Dev/Maker inertia fields; CTA uses "Instead of [inertia], [counter]" per audience |
| C-19 | Definitional instruction with embedded named negative example | PASS | Failure Mode definition includes both a passing example ("Exec won't authorize the demo slot") and a named prohibited form ("Exec won't believe the ROI argument — this restates the belief and is not a Failure Mode") |
| C-20 | Structural template placeholder names source artifact | PASS | All variations have at least one CTA placeholder that names AUDIENCE BELIEF MAP within the placeholder text |
| C-21 | Structural template placeholder cites dynamic gate output | PASS | `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` (or stronger form) — AUDIENCE BELIEF MAP is a Phase 2 gate output, not a static block |

---

#### C-22: All CTA placeholders cite same dynamic gate output

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | CTA: `"Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."` Both slots cite AUDIENCE BELIEF MAP. Absorption declared in Inertia Excuse column definition: "These cells absorb SIGNAL DEFAULTS inertia values into AUDIENCE BELIEF MAP and become the single authoritative source for Phase 5 CTA construction. Phase 5 CTA references AUDIENCE BELIEF MAP, not SIGNAL DEFAULTS directly." |
| V-02 | **FAIL** | CTA: `"Instead of [active [audience] inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."` First placeholder cites SIGNAL DEFAULTS static block directly. C-22 explicitly fails when any placeholder cites a static block. |
| V-03 | **FAIL** | CTA: `"Instead of [active [audience] inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]."` First placeholder cites SIGNAL DEFAULTS. Same structural failure as V-02. |
| V-04 | **PASS** | CTA: `"Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."` Both slots cite AUDIENCE BELIEF MAP. BINDING DECLARATION enforces: "Phase 5 CTA construction reads from AUDIENCE BELIEF MAP, not from SIGNAL DEFAULTS directly. AUDIENCE BELIEF MAP is the single authoritative source for Phase 5 CTA inertia slots." |
| V-05 | **PASS** | CTA: `"Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]."` Both slots cite AUDIENCE BELIEF MAP with explicit gate-output provenance embedded inside placeholder syntax. Strongest form: provenance and single-source combined. |

---

#### C-23: Formal BINDING DECLARATION at top of Phase 2

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | No BINDING DECLARATION table at top of Phase 2. Absorption note is embedded inside the Inertia Excuse column definition paragraph: "These cells absorb SIGNAL DEFAULTS inertia values..." — readable only after reading column definitions in sequence, not as a leading auditable map. |
| V-02 | **PASS** | Formal **PHASE 2 BINDING DECLARATION** table appears at the top of Phase 2, before column definitions. Three-row table maps Exec inertia → Inertia Excuse/Exec row, Dev inertia → Inertia Excuse/Dev row, Maker inertia → Inertia Excuse/Maker row. Followed by: "No other DEFAULTS fields are directly bound to BELIEF MAP columns." Full DEFAULTS→BELIEF MAP data flow is auditable without reading column definitions. |
| V-03 | **FAIL** | No BINDING DECLARATION table at top of Phase 2. Inertia Excuse column definition has per-audience fill templates but no formal binding table. Data flow auditable only through column definitions. |
| V-04 | **PASS** | Formal **PHASE 2 BINDING DECLARATION** table at top of Phase 2. Three-row binding table, plus enforcement sentence: "These bindings transfer SIGNAL DEFAULTS inertia values into AUDIENCE BELIEF MAP at fill time. Phase 5 CTA construction reads from AUDIENCE BELIEF MAP, not from SIGNAL DEFAULTS directly." Auditable from skill structure before any column definition. |
| V-05 | **PASS** | Formal **PHASE 2 BINDING DECLARATION** table at top of Phase 2. Three-row binding table. Meta-purpose statement: "This declaration makes the full DEFAULTS→BELIEF MAP data flow auditable from skill structure alone." Closing prohibition: "After binding, AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references. Phase 5 does not read SIGNAL DEFAULTS inertia fields directly." Strongest form: declaration + purpose statement + explicit prohibition on direct DEFAULTS access in Phase 5. |

---

#### C-24: Inline provenance at each gate-output citation in Phase 5

Pass condition: at *Consumes*, at Hook, at What/Why, and inside CTA placeholder syntax — not just at *Produces* declaration.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | *Consumes*: "AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4)" — names phases but no output type or lock confirmation. Hook: "(from Phase 4, locked, exact)" — partial (origin + lock, no type). What/Why: "POSITIONING LOCK Outcome answer" / "POSITIONING LOCK Competitor named explicitly" — no provenance. CTA: `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` — names source, no phase/type/lock. No bracket notation. |
| V-02 | **FAIL** | Identical Phase 5 structure to V-01. C-24 not targeted in V-02. Same failure pattern. |
| V-03 | **PASS** | *Consumes* (with provenance): `AUDIENCE BELIEF MAP [Phase 2 gate output \| named table \| locked before Phase 5 begins]`, `POSITIONING LOCK [Phase 3 gate output \| named block \| locked before Phase 5 begins]`, `EXEC OPENING SENTENCE [Phase 4 gate output \| named sentence \| binary-gate verified \| locked before Phase 5 begins]`. Per-version citations: Core Belief has `[Phase 2 gate output, locked before Phase 5 begins]`. Hook has `[Phase 4 gate output \| binary-gate verified \| locked before Phase 5 begins]`. What/Why have `[Phase 3 gate output \| locked before Phase 5 begins]`. CTA gate-output placeholder: `[Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]` — provenance inside placeholder syntax. First CTA slot cites SIGNAL DEFAULTS (static block, not a gate-output citation — no gate-output provenance required there). All gate-output citations in Phase 5 carry provenance. |
| V-04 | **FAIL** | *Consumes*: "AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4)" — origin phases named but no output type or lock confirmation. Version body citations: Hook "(from Phase 4, locked, exact)" — partial. What/Why have no provenance. CTA: `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` — names source, no phase/type/lock annotation. No bracket notation at individual cites. |
| V-05 | **PASS** | *Consumes* (with provenance): same full bracket notation as V-03 for all three outputs. Per-version: Core Belief `[Phase 2 gate output, locked before Phase 5 begins]`. Hook `[Phase 4 gate output \| binary-gate verified \| locked before Phase 5 begins]`. What/Why `[Phase 3 gate output \| locked before Phase 5 begins]`. CTA: **both placeholders** carry `[Phase 2 gate output, locked before Phase 5 begins]` inside the placeholder syntax — `[Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]` and `[Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]`. Provenance is embedded inside placeholder syntax at every gate-output cite in Phase 5. Strongest form: resolves the diagnostic question — inline placeholder provenance is definitively complete; instruction-line annotation (V-03) is sufficient but leaves the first CTA slot citing SIGNAL DEFAULTS. |

**Diagnostic question resolution**: Both V-03 and V-05 pass C-24. V-03 uses bracket notation at instruction lines and inside the gate-output placeholder; V-05 embeds provenance inside all absorbed placeholder slots. The structural difference is C-22 coupling: V-03 fails C-22 because its first CTA slot still cites SIGNAL DEFAULTS (making provenance inside that placeholder not applicable); V-05 passes both C-22 and C-24 because the absorption step moves the inertia value into AUDIENCE BELIEF MAP, making provenance inside both placeholder slots consistent and complete.

---

### Aspirational Criteria Summary

| ID | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | **C-22** | **C-23** | **C-24** | Total |
|----|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **F** | **F** | 15/17 |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | **P** | **F** | 15/17 |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | **F** | **P** | 15/17 |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **F** | 16/17 |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **P** | 17/17 |

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|-----------|---------------|-----------------|-------------------|-----------|
| V-01 | 60.00 | 30.00 | (15/17)*10 = 8.82 | **98.82** |
| V-02 | 60.00 | 30.00 | (15/17)*10 = 8.82 | **98.82** |
| V-03 | 60.00 | 30.00 | (15/17)*10 = 8.82 | **98.82** |
| V-04 | 60.00 | 30.00 | (16/17)*10 = 9.41 | **99.41** |
| V-05 | 60.00 | 30.00 | (17/17)*10 = 10.00 | **100.00** |

---

### Ranking

| Rank | Variation | Score | Key Achievement |
|------|-----------|-------|----------------|
| 1 | **V-05** | **100.00** | C-22 + C-23 + C-24. All three axes. Provenance inside both absorbed CTA placeholder slots. Single-source architecture with auditable BINDING DECLARATION and per-cite bracket notation throughout Phase 5. |
| 2 | **V-04** | **99.41** | C-22 + C-23. Two-axis synthesis. BINDING DECLARATION table at Phase 2 top + both CTA slots cite AUDIENCE BELIEF MAP. Missing per-cite provenance bracket notation. |
| 3 | **V-01** | **98.82** | C-22 only. CTA absorption into AUDIENCE BELIEF MAP correct. Missing binding declaration and per-cite provenance. |
| 3 | **V-02** | **98.82** | C-23 only. BINDING DECLARATION table correct. CTA still cites SIGNAL DEFAULTS on first slot. Missing per-cite provenance. |
| 3 | **V-03** | **98.82** | C-24 only. Per-cite bracket notation throughout Phase 5 (including inside gate-output placeholder). CTA first slot still cites SIGNAL DEFAULTS. Missing binding declaration. |

V-01/V-02/V-03 are structurally equal at 98.82 — each solves exactly one axis.

---

### Excellence Signals from V-05

**E-01: C-22 and C-24 are structurally coupled through absorption**
The cleanest architecture for C-22 (all CTA placeholders cite the same dynamic gate output) simultaneously enables C-24 (provenance inside all placeholder syntax) without redundancy. When DEFAULTS inertia is absorbed into AUDIENCE BELIEF MAP at Phase 2, Phase 5's CTA can carry full gate-output provenance on both slots. V-03 can achieve C-24 with bracket notation while the first CTA slot still cites SIGNAL DEFAULTS — but the provenance in that slot is meaningless because it's not a gate-output citation. V-05's three-axis synthesis reveals that C-22 absorption is a prerequisite for C-24 completeness inside CTA placeholders.

**E-02: BINDING DECLARATION closing prohibition pattern**
V-05's BINDING DECLARATION ends with: "After binding, AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references. Phase 5 does not read SIGNAL DEFAULTS inertia fields directly." The negative constraint ("does not read directly") is as important as the positive binding declaration. A binding table that only asserts what IS the source leaves the prohibition implicit. The explicit prohibition makes the single-source architecture auditable from one location: you do not need to check Phase 5 to verify compliance; the BINDING DECLARATION self-declares the downstream constraint. This pattern may generalize: binding declarations for gate outputs should include a negative clause naming what the consuming phase is NOT allowed to access directly.

**E-03: Provenance-annotated *Consumes* block as structural pattern**
V-05 labels the *Consumes* block "*Consumes* (with provenance):" — explicitly distinguishing this from the standard *Consumes* declaration. This labeling signals that the block serves a dual purpose: dependency listing AND provenance chain. The pattern generalizes to any skill where multiple gate outputs feed a complex synthesis phase. A provenance-annotated *Consumes* block is a single readable artifact that answers "what inputs does this phase use, where did they come from, and are they locked?" without tracing backwards through phase definitions.

---

### Predicted vs. Actual Comparison

| Variation | Predicted | Actual | Match |
|-----------|-----------|--------|-------|
| V-01 | 98.82 | 98.82 | ✓ |
| V-02 | 98.82 | 98.82 | ✓ |
| V-03 | 98.82 | 98.82 | ✓ |
| V-04 | 99.41 | 99.41 | ✓ |
| V-05 | 100.00 | 100.00 | ✓ |

All predictions confirmed. Round 6 closes with V-05 as Platinum (100/100). The C-22/C-23/C-24 rubric additions correctly identified the R5 V-05 structural gaps and V-05 addresses all three.

**Golden**: V-05 — `simulations/quest/golden/draft-pitch-golden-2026-03-14.md` candidate.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-22 and C-24 are structurally coupled through absorption — absorbed CTA placeholders enable consistent gate-output provenance on all slots; single-source architecture is prerequisite for complete per-cite provenance", "BINDING DECLARATION closing prohibition pattern — declaration should include explicit negative constraint naming what consuming phases are NOT allowed to access directly, not just positive assertion of the authoritative source", "Provenance-annotated *Consumes* block as structural pattern — label *Consumes* (with provenance) to signal dual-purpose: dependency listing AND provenance chain readable from one location"]}
```
