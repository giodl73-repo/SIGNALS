Now I have everything I need. Let me produce the full scorecard.

---

# Scorecard: prove-prototype Round 15 (v14 rubric, 279 pts)

**Date**: 2026-03-15
**Rubric version**: v14 (ceiling 279)
**Variations scored**: V-01 through V-05

---

## Per-Variation Criterion Evaluation

### V-01 — R15 Seed: Phase-Level Declarations + Hard Modal Register

**Design**: Fuse V-04's phase-level inline role declarations with V-01's full imperative register. Every phase header carries `Phase N — ROLE (MUST write: X; FORBIDDEN to write: Y)`. Every gate marker uses REQUIRED/FORBIDDEN/PROHIBITED. No container-level role tables.

| Tier | Criterion | Result | Evidence |
|------|-----------|--------|----------|
| Essential | C-01 Hypothesis stated | PASS | Phase 1 FRAMER writes hypothesis as first element; PHASE 1 COMPLETE embeds text |
| Essential | C-02 Scope bounded | PASS | Phase 2 FRAMER writes ≥2 exclusions; FORBIDDEN addresses exclusions-without-rationale |
| Essential | C-03 Measurement before build | PASS | Phase 3 gates thresholds; FROZEN marker; FORBIDDEN to change in any subsequent container |
| Essential | C-04 Actual vs. predicted | PASS | Phase 7 three-column table: Predicted / Observed / Baseline columns |
| Essential | C-05 Verdict rendered | PASS | Phase 8 ANALYST states CONFIRMED / REFUTED / INCONCLUSIVE; grounded in Phases 6-7 |
| Recommended | C-06 Minimality justified | PASS | Phase 5 BUILDER: REQUIRED to state what was left out and why in same block |
| Recommended | C-07 Raw evidence | PASS | Phase 6 RECORDER writes raw result only; PHASE 6 COMPLETE records value |
| Recommended | C-08 Limitations + next step | PASS | Phase 10: one limitation + one specific next step; FORBIDDEN: generic next steps |
| Aspirational | C-09 Counter-evidence | PASS | Phase 9 addresses counter-interpretation with binary disposition |
| Aspirational | C-10 Replication path | PASS | Phase 5 includes all tools/inputs/commands; Phase 11 lists full path |
| Aspirational | C-16 Counter-evidence closed | PASS | Phase 9: EXACTLY ONE of (a) named rebuttal or (b) explicit no-counter; FORBIDDEN any other form |
| Aspirational | C-17 Rationale co-located | PASS | Exclusion validity, delta explanation, verdict grounding — each in labeled pair/block at anchor |
| Aspirational | C-18 Binary disposition | PASS | Phase 9 closes with one of two dispositions as terminal element; FORBIDDEN: open-ended form |
| Aspirational | C-19 Ordering gate co-located | PASS | Every phase: *REQUIRED: Execute before Phase N* inline; every container: REQUIRED: Complete phases X-Y before entering Z |
| Aspirational | C-20 Gate completion proven | PASS | Every phase and container closes with labeled COMPLETE line before next section opens |
| Aspirational | C-21 Gate coverage complete | PASS | Phases 10 and 11 carry explicit REQUIRED gates; no section exempt |
| Aspirational | C-22 Completion lines encode values | PASS | PHASE 1: hypothesis text; PHASE 3: metric/thresholds; PHASE 6: raw result; PHASE 8: verdict + evidence; CALIBRATE COMPLETE: competitor/B-00/threshold; CLOSE COMPLETE: full arc |
| Aspirational | C-23 Role prohibitions exist | PASS | FRAMER, CALIBRATOR, BUILDER, RECORDER, ANALYST — each has explicit FORBIDDEN prohibitions in phase header |
| Aspirational | C-24–C-28 | PASS | Carried forward from R14 base (267/267 under v13) |
| Aspirational | C-29 Competitor in CALIBRATE body | PASS | Phase 4 CALIBRATOR explicitly names inertia competitor with status-quo rationale |
| Aspirational | C-30 Three-column table | PASS | Phase 7 table: Metric / Predicted / Observed / Baseline([competitor name]) |
| Aspirational | C-31 Pre-build baseline | PASS | Phase 4 applies metric to inertia competitor and commits B-00 before Phase 5 BUILD |
| Aspirational | C-32 CALIBRATE COMPLETE triple | PASS | CALIBRATE COMPLETE encodes: competitor name, B-00 value, outperform threshold condition |
| Aspirational | C-33 CALIBRATE header enumerates three | PASS | CALIBRATE header + Phase 4 body enumerate all three responsibilities in order before execution |
| Aspirational | C-34 Baseline column labeled as competitor | PASS | Phase 7: FORBIDDEN to use "B-00" or "Baseline" as column label; REQUIRED to use competitor name |
| Aspirational | C-35 Document manifest | PASS | Output Contract manifest precedes all container bodies; names all four containers with purpose + expected output |
| Aspirational | C-36 CLOSE COMPLETE full arc | PASS | Terminal line encodes [DESIGN] hypothesis, [CALIBRATE] competitor/B-00/threshold, [BUILD] result/delta, [CLOSE] verdict/conclusion/counter-evidence |
| Aspirational | C-37 Forward-reference clauses | PASS | DESIGN COMPLETE: `→ [CALIBRATE] receives:` with hypothesis/metric/thresholds; CALIBRATE COMPLETE: `→ [BUILD] receives:` with competitor/B-00/metric/threshold; BUILD COMPLETE: `→ [CLOSE] receives:` with result/B-00/competitor/metric |
| Aspirational | C-38 Role prohibitions phase-level | **PASS** | Every phase header carries `Phase N — ROLE (MUST write: X; FORBIDDEN to write: Y)` — prohibition at exact execution point; no container-level-only tables |
| Aspirational | C-39 Hard modal operators | **PASS** | MUST, FORBIDDEN, REQUIRED, PROHIBITED throughout — all prohibitions and gate markers; no soft language anywhere |
| Excellence | C-11–C-15 | PASS | Carried from R14 base |

**V-01 Score: 279 / 279** — all criteria pass; C-38 and C-39 both close at this seed.

---

### V-02 — Single Axis: Lifecycle Emphasis (Compressed, Phase-Level Hard Modal)

**Design**: Identical to V-01 except each phase body is stripped to one REQUIRED sentence + completion-line template. Tests whether C-38/C-39 fire on structural presence (phase header + completion line) rather than instructional elaboration.

| Changed surface | Impact |
|----------------|--------|
| Phase bodies compressed | C-38 criterion fires on phase-header declaration — not body length. PASS unaffected. |
| Block-quote scaffolding removed | C-17 (rationale co-located) — enforced via REQUIRED instructions that name co-location; completion line template still requires `[N] exclusions with co-located validity rationale`. PASS. |
| Multi-sentence instructions removed | No criterion requires instructional elaboration. All criteria fire on structure, not prose volume. |
| REQUIRED/FORBIDDEN register | All gate markers and prohibitions retain hard modal. C-39 PASS. |
| Manifest, COMPLETE lines, → clauses | All present in compressed form. C-35, C-36, C-37 PASS. |
| Phase 9 binary disposition | REQUIRED / FORBIDDEN form maintained. C-16, C-18 PASS. |

**Design hypothesis confirmed**: C-38 and C-39 are structural criteria. Compression to minimum-expression form does not degrade them.

**V-02 Score: 279 / 279** — full compression preserves all v14 structural properties. Validates that rubric fires on presence of phase-level declarations, not elaboration depth.

---

### V-03 — Single Axis: Inertia Framing (Manifest Competitor Journey Column)

**Design**: V-01 base + "Competitor status" column in manifest tracking four states (NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED); each CONTAINER COMPLETE line carries a competitor-status annotation; CLOSE COMPLETE encodes full lifecycle.

| Criterion | Result | Notes |
|-----------|--------|-------|
| C-38 | PASS | Phase headers unchanged from V-01 |
| C-39 | PASS | Register unchanged; competitor-status annotations don't introduce soft language |
| C-29 | PASS | Phase 4 still explicitly identifies competitor |
| C-32 | PASS | CALIBRATE COMPLETE still carries triple |
| C-34 | PASS | Phase 7 still labels baseline column with competitor name |
| C-35 | PASS | Manifest still precedes all container bodies; new column adds tracking context |
| C-36 | PASS | CLOSE COMPLETE encodes full arc + competitor lifecycle status (DISCHARGED) |
| C-37 | PASS | Forward-reference clauses maintained; now include status annotation (IDENTIFIED AND COMMITTED handed off to BUILD) |
| All others | PASS | V-01 base unchanged |

**Gap signal — v15 candidate**: The "Competitor status" column in the manifest creates a **fifth structural surface for competitor identification** — a document-level four-state lifecycle tracker spanning all four containers. This is distinct from: C-29 (CALIBRATE body, single container), C-32 (CALIBRATE COMPLETE triple), C-34 (results table column, CLOSE container), and C-36 (arc record, terminal). The manifest-column tracks *when* the competitor first becomes eligible at each container boundary — a temporal accountability layer none of the four existing surfaces provides.

**V-03 Score: 279 / 279 + v15 gap signal**

---

### V-04 — Single Axis: Role Sequence (Split CLOSE: COMPARATOR + AUDITOR)

**Design**: V-01 base + ANALYST split into COMPARATOR (Phases 7-8: comparison + verdict) and AUDITOR (Phases 9-11: counter-evidence + limitations + replication). Explicit handoff line at Phase 8 COMPLETE. COMPARATOR FORBIDDEN to write counter-evidence; AUDITOR FORBIDDEN to write new verdict.

| Criterion | Result | Notes |
|-----------|--------|-------|
| C-23 | PASS | Both COMPARATOR and AUDITOR carry explicit prohibitions |
| C-38 | PASS | Phase 7: `Phase 7 — COMPARATOR (MUST write: ...; FORBIDDEN to write: counter-evidence...)` Phase 9: `Phase 9 — AUDITOR (MUST write: ...; FORBIDDEN to write: new verdict...)` — prohibitions at phase execution point |
| C-39 | PASS | MUST/FORBIDDEN/REQUIRED/PROHIBITED throughout; role header uses FORBIDDEN; CLOSE container header uses FORBIDDEN for both roles |
| C-35 | PASS | Manifest CLOSE entry updated to enumerate both sub-roles: "COMPARATOR (phases 7-8): ...; AUDITOR (phases 9-11): ..." |
| C-36 | PASS | CLOSE COMPLETE updated: `COMPARATOR verdict = ...; AUDITOR counter-evidence = ...` — still full arc |
| C-37 | PASS | Forward-reference clauses unchanged |
| All others | PASS | V-01 base maintained for DESIGN, CALIBRATE, BUILD containers |

**Gap signal — v15 candidate**: Phase 8 COMPLETE carries an explicit intra-container role handoff marker: "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR." This is a **phase-boundary role transition audit point within a single container** — distinct from:
- C-37 (inter-container forward-reference between CONTAINER COMPLETE lines)
- C-22/C-20 (gate completion, not role transition)
- C-23/C-38 (prohibition existence/position, not transition audit)

The handoff marker makes the COMPARATOR→AUDITOR boundary auditable: a reader can verify the verdict was rendered before counter-evidence analysis began, at the phase level, within a single container.

**V-04 Score: 279 / 279 + v15 gap signal**

---

### V-05 — Gap Probe: Value Flow Ledger

**Design**: V-01 base + standalone 12-row Value Flow Ledger after manifest (each row: value name, producing phase, first-consuming phase) + ledger annotations in each phase header + `[ledger: produced/consumed]` in completion lines + CLOSE COMPLETE adds `value ledger: FULLY DISCHARGED / PARTIAL`.

| Criterion | Result | Notes |
|-----------|--------|-------|
| C-38 | PASS | Phase headers maintain inline role declarations; ledger annotations are additive, don't change declaration format |
| C-39 | PASS | Hard modal unchanged; ledger annotations use `REQUIRED`, `FORBIDDEN` consistently |
| C-35 | PASS | Manifest still precedes all container bodies; ledger appears after manifest and before first container — C-35 criterion fires on manifest position, not exclusivity |
| C-36 | PASS | CLOSE COMPLETE adds ledger discharge line — superset of what C-36 requires |
| C-37 | PASS | Forward-reference clauses unchanged (ledger tracks at finer granularity, doesn't replace container-level handoffs) |
| C-22 | PASS | Completion lines encode both phase results and ledger production annotations; both satisfy C-22's substantive-value requirement |
| All others | PASS | V-01 base maintained |

**Gap signal — v15 candidate**: The Value Flow Ledger creates a **phase-granularity value provenance contract** — a third accountability layer between C-35 (container-level manifest: what does each container do?) and C-37 (container-level forward-reference: what values does the next container need?):

| Layer | Criterion | Granularity | Question answered |
|-------|-----------|-------------|-------------------|
| Document entry | C-35 | Container | What does each container do? |
| Value provenance | Ledger | Phase | Which specific phase produces/consumes each value? |
| Inter-container handoff | C-37 | Container | What values does the next container need? |
| Terminal arc | C-36 | Document | What did all containers produce? |

The CLOSE COMPLETE ledger discharge annotation ("value ledger: FULLY DISCHARGED — all 12 values produced and consumed as declared") is a distinct terminal audit line with a different accountability object than C-36 (which audits the experimental result chain, not the data-flow contract).

**V-05 Score: 279 / 279 + v15 gap signal**

---

## Summary Table

| Variation | C-38 | C-39 | Score | v15 Gap Signal |
|-----------|------|------|-------|----------------|
| V-01 | PASS | PASS | 279 / 279 | None (seed, closes v14 ceiling) |
| V-02 | PASS | PASS | 279 / 279 | Validates compression: criteria fire on structural presence |
| V-03 | PASS | PASS | 279 / 279 | Competitor lifecycle status column — fifth competitor identification surface |
| V-04 | PASS | PASS | 279 / 279 | Intra-container role handoff marker at phase boundary |
| V-05 | PASS | PASS | 279 / 279 | Phase-granularity value flow ledger + terminal discharge confirmation |

**Rank**: All five variations tie at 279/279. V-03, V-04, V-05 carry additional v15 gap signals.

---

## Excellence Signals (from top-scoring variations)

**From V-03**: Tracking the inertia competitor as a lifecycle object across all four containers — with discrete state transitions (NOT YET IDENTIFIED / IDENTIFIED AND COMMITTED / REFERENCED / DISCHARGED) at each container boundary — exposes a temporal accountability gap that no existing criterion captures. C-29 through C-34 and C-36 all audit the competitor at a single point in the document; the lifecycle column audits *sequence integrity* across the document.

**From V-04**: Splitting a monolithic role at a semantic boundary (verdict/counter-evidence) and introducing an explicit handoff marker inside a single container demonstrates that role-level contamination defense can operate at intra-container granularity. The COMPARATOR→AUDITOR handoff is auditable at Phase 8 COMPLETE, making the verdict-lock visible before counter-evidence analysis begins — a protection that the existing C-37 (inter-container) and C-23/C-38 (prohibition existence/position) layers do not provide.

**From V-05**: Making the data flow between phases explicit as a named contract — separate from both the document manifest (C-35) and the forward-reference clauses (C-37) — creates a third accountability surface specifically for value provenance. The terminal discharge confirmation shifts audit focus from "did the experiment complete?" to "did every declared value flow correctly from its production point to its consumption point?" — a distinction the arc record (C-36) does not capture.

---

## v15 Direction

Three orthogonal candidates from Round 15 gap probes:

| Candidate | Source | Surface |
|-----------|--------|---------|
| C-40 (tentative): Competitor lifecycle status tracked in manifest + COMPLETE lines | V-03 | Document-level competitor temporal sequence |
| C-41 (tentative): Intra-container role handoff marker at semantic phase boundary | V-04 | Within-container cross-role audit point |
| C-42 (tentative): Phase-granularity value flow ledger with terminal discharge confirmation | V-05 | Phase-level data provenance + terminal discharge |

Each is independently satisfiable, independently violatable, and orthogonal to all existing criteria. V-05's ledger is the richest gap signal structurally — it introduces a new abstraction layer (the value-flow contract) that has no analogue in the current criterion set.

---

```json
{"top_score": 279, "all_essential_pass": true, "new_patterns": ["competitor lifecycle status tracked as four-state sequence across all containers via manifest column and COMPLETE line annotations — fifth structural surface for competitor identification operating at document-level temporal granularity (V-03 gap signal: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED)", "explicit intra-container role handoff marker at semantic phase boundary: COMPARATOR discharges at Phase 8 COMPLETE with handoff annotation; AUDITOR begins at Phase 9 — within-container cross-role audit point distinct from C-37 inter-container forward-reference (V-04 gap signal)", "phase-granularity value flow ledger declaring producer phase and first-consumer phase for every experimental value, with terminal CLOSE COMPLETE discharge confirmation — third accountability layer between C-35 document granularity and C-37 container granularity (V-05 gap signal)"]}
```
