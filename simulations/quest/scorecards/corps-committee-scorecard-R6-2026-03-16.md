# corps-committee R6 — Quest Score Report

## Rubric v6 Scoring Matrix

**Scoring model:** 7 essential criteria (pass/fail disqualifier) + 15 aspirational criteria × 0.67 pts each = 10.00 pt pool. Base (all essentials pass, 0 aspirational) ≈ 87.83. Full (all 15 aspirational) = 97.83.

---

### Essential Criteria Evaluation (all variations)

All five R6 variations build on the R5 V-05 foundation. Essential criteria are structurally present and intact across the board:

| Criterion | Basis | All 5 Variations |
|-----------|-------|-----------------|
| C-01 — Typed Agenda Item Declaration | `Committee Type: ___` and `Agenda Item: ___` appear before Phase 0 content in all 5 skeletons | PASS |
| C-02 — Five-Phase Structure with Terminal Commits | Phases 0–5 in sequence, each closed by `PHASE-N-COMMIT: [locked]` as terminal line; no content follows any commit within its phase | PASS |
| C-03 — (inherited v5) | Structural phase content requirements intact | PASS |
| C-04 — (inherited v5) | Intact | PASS |
| C-05 — (inherited v5) | Intact | PASS |
| C-06 — (inherited v5) | Intact | PASS |
| C-07 — (inherited v5) | Intact | PASS |

**All essential criteria: PASS across all 5 variations. No variation is disqualified.**

---

### Aspirational Criteria Evaluation

#### C-08 through C-12 — R1–R3 Pool (inherited from v5)

All variations retain the full R1–R3 structural skeleton: INVESTIGATION-ATTEMPT-N labeling, INERTIA RECORD with one-phrase anchors, INERTIA INVARIANT with both elements (`sealed at PHASE-1-COMMIT` + modification prohibition), GATE-N loop, REWRITE PROTOCOL, TIER SORT with SORT-CHECK, coupling integrity on both PHASE-1-COMMIT and PHASE-3-COMMIT.

**C-08 through C-12: PASS — all 5 variations.**

#### C-13 through C-16 — R4 Pool (inherited from v5)

SYMMETRY CHECK block with three checkboxes at Phase 3→4 boundary; SYMMETRY DECLARATION with COUPLING PAIR A and B both defined; STANCE INVARIANT with both elements (`sealed at PHASE-3-COMMIT` + modification prohibition); INERTIA CONTINUITY BRIDGE with BRIDGE RESULT declared and halt declaration.

All 5 variations carry these intact.

**C-13 through C-16: PASS — all 5 variations.**

---

#### C-17 — Phase 5 Completeness Skeleton Gate (MINUTES INTEGRITY CHECK)

- **Pass condition:** `## MINUTES INTEGRITY CHECK` block between `PHASE-4-COMMIT` and Phase 5 header; three named Phase 5 sections as checkboxes; halting declaration present.

All 5 variations have the MINUTES INTEGRITY CHECK block at the correct position:
- V-01: 5 checkboxes (lines 295–305), halt: "All five boxes ticked before Phase 5 content is generated." ✓
- V-02: 5 checkboxes (lines 776–786), halt present. ✓
- V-03: 6 checkboxes (lines 1264–1277) — adds DISSENT INERTIA LINKAGE as 6th; original 5 intact, halt present. ✓
- V-04: 6 checkboxes (lines 1758–1771) — same as V-03. ✓
- V-05: 6 checkboxes (lines 2161–2174) — same pattern. ✓

The addition of a 6th checkbox in V-03/V-04/V-05 does not break C-17; the three required Phase 5 section checkboxes remain and the halt declaration is present.

**C-17: PASS — all 5 variations.**

---

#### C-18 — Phase 3 Named Correction Protocol (TIER SEQUENCE PROTOCOL)

- **Pass condition:** Named protocol block with `***` delimiters inside Phase 3 fill rules. Restart instruction invokes protocol by name.

All 5 variations carry `*** TIER SEQUENCE PROTOCOL ***` / `*** END TIER SEQUENCE PROTOCOL ***` in Phase 3 fill rules, with restart clause: "Execute TIER SEQUENCE PROTOCOL again from the top." (V-01: lines 459–471; V-02: 934–945; V-03: 1412–1422; V-04: 1872–1877 condensed form; V-05: 2311–2323.)

Note: V-04's TIER SEQUENCE PROTOCOL is condensed but retains the named delimiters and self-referencing restart.

**C-18: PASS — all 5 variations.**

---

#### C-19 — Inertia Citation Audit Block

- **Pass condition:** `## INERTIA CITATION AUDIT` block between `## STANCE MANIFEST` and `PHASE-3-COMMIT`; per-finding entries; halting declaration.

All 5 skeletons contain the INERTIA CITATION AUDIT block with INERTIA-FINDING-A through -D entries, `PHASE-3-COMMIT halts until AUDIT RESULT is COMPLETE` declaration, and AUDIT RESULT field. Correct position in all cases.

**C-19: PASS — all 5 variations.**

---

#### C-20 — Phase 0 Committee Type Gate

- **Pass condition:** Named gate block between typed agenda declarations and `PHASE-0-COMMIT`; both `Committee Type:` and `Agenda Item:` fields ticked against vocabulary; halting declaration.

All 5 skeletons have `## COMMITTEE TYPE GATE` with two `[ ]` checkboxes at the correct position. PHASE-0-COMMIT includes "COMMITTEE TYPE GATE ticked." in commit body. Halt declaration: "Any unticked box halts Phase 0." Vocabulary list (ROB / shiproom / arch-board) present.

**C-20: PASS — all 5 variations.**

---

#### C-21 — Structured Bridge Completeness Gate

- **Pass condition:** Completeness-gate block at Phase 2→3 boundary; phase-entry criteria; halt declaration.

All 5 variations have the `## INERTIA CONTINUITY BRIDGE` block positioned between PHASE-2-COMMIT and `## PHASE 3` header. The block enumerates phase-entry criteria (Inspection complete, Decision, BRIDGE RESULT) and carries an explicit halt declaration: "Undeclared BRIDGE RESULT halts Phase 3." This is the R5 V-02 pattern the criterion captures.

Evidence note: The bridge uses `___` fill fields rather than `[ ]` checkboxes, which is a format variant. However, the structural gate function is fully present and the halt declaration is explicit. Consistent with the claim that "all three R5 mechanisms already present."

**C-21: PASS (with note on fill-field vs. checkbox format) — all 5 variations.**

---

#### C-22 — Phase 4 Tally Ledger Protocol

- **Pass condition:** Named protocol block inside Phase 4 before `PHASE-4-COMMIT`; voting outcomes enumerated; result declaration (`QUORUM MET` or equivalent); halting declaration.

All 5 skeletons have `## TALLY LEDGER PROTOCOL` inside Phase 4 with: participant count field, per-participant STANCE MANIFEST entry enumeration, APPROVE/CONDITION/BLOCK counts, Total cross-check, `TALLY RESULT: ___ [QUORUM MET / COUNT MISMATCH -- halt]`, and "PHASE-4-COMMIT may not proceed until TALLY RESULT is declared." All commits include "TALLY LEDGER PROTOCOL complete, TALLY RESULT declared."

**C-22: PASS — all 5 variations.**

---

### Composite Score Computation

All 5 variations pass all 7 essential criteria and all 15 aspirational criteria (C-08 through C-22):

```
Base score (all essentials, 0 aspirational) = 87.83
Aspirational pool: 15 × 0.667 = 10.00
Total: 87.83 + 10.00 = 97.83
```

| Variation | Essentials | C-08–C-22 | Composite |
|-----------|-----------|-----------|-----------|
| V-01 | 7/7 PASS | 15/15 | **97.83** |
| V-02 | 7/7 PASS | 15/15 | **97.83** |
| V-03 | 7/7 PASS | 15/15 | **97.83** |
| V-04 | 7/7 PASS | 15/15 | **97.83** |
| V-05 | 7/7 PASS | 15/15 | **97.83** |

All five variations are tied at the rubric ceiling. The R6 additions operate beyond the current rubric's measurement horizon — they are excellence signals, not scorable criteria under v6.

---

### Ranking

All variations: **97.83 (tied)**. Tie-break by excellence signal count (beyond rubric):

| Rank | Variation | Excellence signals carried | Notes |
|------|-----------|--------------------------|-------|
| 1 | **V-05** | 3 (VOICE COMPLETENESS CHECK + CONSTRAINT REGISTRY + DISSENT INERTIA LINKAGE) | Full R6 candidate |
| 2 | **V-04** | 2 (VOICE COMPLETENESS CHECK + DISSENT INERTIA LINKAGE) | Closes both P3-exit and P5 gaps |
| 3 | **V-01** | 1 (VOICE COMPLETENESS CHECK) | P3 voice-element gate |
| 3 | **V-03** | 1 (DISSENT INERTIA LINKAGE) | P1→P5 traceability gate |
| 5 | **V-02** | 1 (CONSTRAINT REGISTRY table) | Format change only, no new phase gate |

---

### Excellence Signals (from V-05, top variation)

**Signal 1 — VOICE COMPLETENESS CHECK skeleton block (V-01 pattern)**
Per-tier checklist block embedded in the Phase 3 skeleton after participant voices and before `## STANCE MANIFEST`. Tier 1 boxes: STANCE label + INERTIA-FINDING-* citation. Tier 2 boxes: STANCE label + specific condition. Tier 3 boxes: STANCE label + CITE field + RESPONDS-TO field. Any unticked box halts Phase 3 — `## STANCE MANIFEST` may not be written until all applicable boxes are ticked. The Phase 3 fill rules and PHASE-3-COMMIT both confirm: "VOICE COMPLETENESS CHECK ticked." Extends the per-finding enumeration pattern of INERTIA CITATION AUDIT to voice structural completeness at the same phase boundary.

**Signal 2 — Phase-tagged CONSTRAINT REGISTRY table (V-02 pattern)**
The flat numbered CONSTRAINTS list is replaced by a `## CONSTRAINT REGISTRY` table with columns: Gate Name / Governs / Halt Trigger. One row per gate; the governing phase(s) are explicit in-cell. Models filling a phase can look up phase-keyed rows directly rather than scanning 12–14 numbered items. V-05 includes a VOICE COMPLETENESS CHECK row and a DISSENT INERTIA LINKAGE row alongside all prior gates, making the full v6 gate inventory scannable by phase.

**Signal 3 — DISSENT INERTIA LINKAGE 6th checkbox in MINUTES INTEGRITY CHECK (V-03 pattern)**
A 6th checkbox requires that at least one DISSENTING OPINIONS entry explicitly cites an INERTIA-FINDING-* label by token form — OR that "No dissent" is declared with an explicit `No inertia linkage required -- [justification]` clause. The Phase 5 fill rules instruct revision of the most relevant dissent entry if no citation exists before ticking this box. PHASE-5-COMMIT must include "DISSENT INERTIA LINKAGE ticked." This closes the Phase 1→Phase 5 traceability gap that INERTIA CITATION AUDIT closes for Phase 1→Phase 3: findings that survive into Phase 3 voices can now be confirmed present in the Phase 5 record.

---

```json
{"top_score": 97.83, "all_essential_pass": true, "new_patterns": ["VOICE COMPLETENESS CHECK skeleton block: per-tier checkboxes gate between participant voices and STANCE MANIFEST; any unticked box halts Phase 3; extends INERTIA CITATION AUDIT enumeration pattern to voice element completeness", "Phase-tagged CONSTRAINT REGISTRY table: replaces flat numbered list with gate-name/governs/halt-trigger rows; decouples constraint from sequential scan; enables phase-keyed constraint lookup during fill", "DISSENT INERTIA LINKAGE 6th checkbox in MINUTES INTEGRITY CHECK: requires explicit INERTIA-FINDING-* token citation in at least one dissent entry or declared-absent with inertia linkage justification; closes Phase 1 to Phase 5 inertia traceability gap"]}
```
