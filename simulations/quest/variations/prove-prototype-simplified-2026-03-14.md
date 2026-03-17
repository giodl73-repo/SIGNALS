Hits the 20% floor. Here's the complete output:

---

## Simplified Prompt Body

Written to `simulations/quest/golden/prove-prototype-QU5-simplified-2026-03-15.md` — the full text is the file above.

---

## Simplification Report

### What was removed and why

| Removed | Location | Criterion impact |
|---------|----------|-----------------|
| "The following two threads propagate through every CONTAINER COMPLETE boundary..." (intro sentence) | MANIFEST PREAMBLE | None — the thread table is self-explanatory |
| "Declare them as rows in the table below. Both rows MUST carry equivalent depth in every column — a row with single-phrase entries where the other row has multi-clause entries does not satisfy construction-enforced co-equality." | Thread declarations lead-in | Kept "Both rows MUST carry equivalent depth" — the elaboration adds no new constraint |
| "Tracks the inertia competitor across all container boundaries, with identification gated at CALIBRATE and discharge confirmed at CLOSE COMPLETE. Lifecycle state tracked in the manifest Competitor Status column at every container." | Thread 1 Scope column | Both facts are covered by CLF and the manifest table |
| "with symmetric structure" / "with hard modal operators" / "model-written" | Thread 2 Scope column | Descriptive qualifiers; the role FORBIDDEN clauses and gate lines enforce this |
| "each named separately from Thread 1 lifecycle chain and the C-36 arc record" | Thread 2 terminal discharge | Informative but no criterion requires naming the C-36 arc record in the discharge column |
| Thread key markers: detailed parenthetical elaborations within each surface item | Thread 1 + 2 Key markers columns | Condensed each bullet to label + criterion reference; 5-item lists maintain C-49 depth parity |
| "This section appears before any container body executes. It catalogs every structural marker required by C-43, C-44, and C-45, establishing C-48 compliance as a verifiable document property before a reader encounters any container." | Structural Marker Inventory intro | Section heading is self-explanatory; no criterion requires this framing sentence |
| "**Why each transition is gated at a specific container boundary:**" | Competitor Lifecycle Framing | Rhetorical header; bullets contain the required C-46 rationale regardless |
| "CALIBRATE names the competitor, measures its baseline (B-00), and commits an outperform threshold." | CALIBRATE lifecycle bullet | Duplicates the CALIBRATE entry contract and manifest; the contamination rationale is what C-46 requires |
| "Both sub-transitions are REQUIRED before BUILD begins." | CALIBRATE lifecycle bullet | Covered by "All three REQUIRED before BUILD" in the entry contract |
| "Competitor baseline is FROZEN at CALIBRATE COMPLETE;" | BUILD lifecycle bullet | The preceding "MUST NOT alter it" already establishes the freeze |
| Expected output column | Document Manifest | No criterion requires this column; each container body specifies its deliverables |
| "Gate markers enforce this ordering; Phase 7 REQUIRED to precede Phase 8 by IMPLEMENTER COMPLETE handoff; Phase 10 REQUIRED to precede Phase 11 by COMPARATOR handoff." | Value Flow Ledger trailing sentence | Gate ordering is already explicit in the IMPLEMENTER COMPLETE and COMPARATOR COMPLETE sections |
| "The claim must be falsifiable: a result that would confirm it and a result that would refute it must both be statable." | Phase 1 body | Phase 1 already asks for confirming and refuting results; falsifiability is implicit |
| "This is the committed baseline — it cannot be revised after CALIBRATE COMPLETE." | Phase 5 body | Stated in lifecycle framing (BUILD boundary) and CALIBRATE COMPLETE; third repetition |
| "The artifact must be sufficiently described that a reader could reproduce it." | Phase 7 body | Replication covered by Phase 13; Phase 7's key components + decisions instruction is sufficient |
| "The verdict MUST follow from the results table —" | Phase 10 body | Citing the delta implies table derivation; kept the operative constraint |
| "Neither sub-role may perform the other's function." | BUILD entry contract | The FORBIDDEN clauses on each sub-role enforce this more precisely |
| "Cross-prohibitions enforced with hard modal operators throughout." | CLOSE entry contract | The FORBIDDEN clauses are the enforcement; this sentence annotates the mechanism without adding to it |
| "- Competitor lifecycle: DISCHARGED" | CLOSE COMPLETE | Redundant with "Thread 1 lifecycle chain (verbatim): ... → DISCHARGED" above it |
| "→ CALIBRATE receives: ..." / "→ BUILD receives: ..." / "→ CLOSE receives: ..." | DESIGN/CALIBRATE/BUILD COMPLETE sections | Container-to-container forward-reference summaries; the Value Flow Ledger is the authoritative transfer document. Note: the intra-BUILD "→ MEASURER receives:" line was **kept** — it is the Thread 2 Phase 7 handoff declaration required by C-51 |
| "(for REFERENCED state)" / "(pass criterion)" | CALIBRATE COMPLETE → BUILD receives (removed) | With the line removed, moot |
| "(from DESIGN thresholds)" | Phase 8 body | The Value Flow Ledger establishes this origin |

### Criteria verification

All essential criteria C-01 through C-52 still pass:

| Criterion | Element preserved |
|-----------|------------------|
| C-29 | Phase 4 asks for competitor name + rationale |
| C-32 | CALIBRATE COMPLETE has `competitor name \| B-00 value \| outperform threshold` triple |
| C-34 | Phase 9 says "MUST be labeled with the inertia competitor name, not a generic 'Baseline' label" |
| C-36 | CLOSE COMPLETE arc record: `[name] \| B-00: [value] \| outperform threshold \| prototype result \| delta` |
| C-40 | Manifest NOT YET IDENTIFIED row for DESIGN |
| C-43 | CLF standalone section + per-container incoming-state header annotations |
| C-44 | `REQUIRED: Confirm Phase 10 COMPARATOR handoff marker present before executing Phase 11` standalone gate |
| C-45 | `Thread 1: [state] \| Thread 2: [status]` on every CONTAINER COMPLETE line |
| C-46 | CLF has gate + contamination risk + isolation purpose for each of four boundaries |
| C-48 | All four SMI marker types as standalone labeled elements |
| C-49 | Thread table: both rows are ~5-item bullet lists at equivalent depth across all columns |
| C-50 | Structural Marker Inventory with REQUIRED closure |
| C-51 | BUILD has IMPLEMENTER/MEASURER split; Phase 7 IMPLEMENTER COMPLETE handoff + Phase 8 MEASURER REQUIRED gate; Thread 2 has 5 structural markers |
| C-52 | "voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section" in REQUIRED closure |

---

**All essential criteria still pass: YES**

```json
{"simplified_word_count": 2059, "original_word_count": 2594, "all_essential_still_pass": true}
```
