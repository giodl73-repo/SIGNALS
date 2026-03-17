Written to `simulations/quest/golden/org-chart-variate-R18-2026-03-17.md`.

---

# org-chart Variate -- Round 18

**Baseline:** R17 V-05 (C-47 count guard + C-48 format anchor + C-49 preamble prohibition all present as floor in every variation).

**Three new axes** -- all outside the CHECKPOINT-0 item (b) chain, exploring dimensions that R17 V-05 leaves unconstrained:

---

## Axis A -- FAIL-path consequence injection (phrasing register)

**What changes:** Three DO NOT prohibitions gain inline IF/THEN consequence statements at the violation site:
1. ROLE-LOAD-ORDER tier interleaving: "IF any tier-N entry appears before all tier-(N-1) entries are written, the ROLE-TYPE-CLASSIFICATION block is invalid -- re-emit in strict tier order"
2. Sub-section 1 mechanism row misplacement: "IF any mechanism row is written in Sub-section 2, the FLAT-CASE-CLOSED count is understated -- move all mechanism-typed rows to Sub-section 1 and recount"
3. Quorum field omission: "IF any charter is missing the Quorum field, that charter is incomplete -- add the Quorum field in N of M fraction form before emitting CHARTERS COMPLETE"

**Gap it closes:** Bare DO NOT prohibitions name what must not happen but leave no named consequence at the violation site. Recovery only fires at the gate CHECKPOINT, after the violation has already propagated through downstream sections. Inline FAIL-path statements convert each prohibition from a one-directional declaration into a bidirectional consequence chain with a named remediation step.

---

## Axis B -- STRUCTURING-COST FRAME before mechanism table (inertia framing)

**What changes:** A `STRUCTURING-COST FRAME` block is inserted before the mechanism evidence table in Sub-section 1. The block names two cost categories with observable anchors -- over-structuring overhead (committee formation, governance cadence, role-specialization tax) and under-coordination risk (decision latency, SLA exposure, knowledge silo formation, competing roadmap without arbitration owner) -- before any mechanism row is written.

**Gap it closes:** The baseline opens Sub-section 1 with the mechanism table directly; cost categories emerge from the VERDICT. This reverses the causal logic. Cost categories are the evaluative lens through which mechanisms are assessed -- they should precede the evidence, not follow it. Placing the frame before the table converts mechanism table construction from evidence-first to cost-lens-first.

---

## Axis C -- GATE-CONDITION-MET arrival acknowledgment at HEADCOUNT (lifecycle emphasis)

**What changes:** A three-field `GATE-CONDITION-MET` block is inserted at the start of HEADCOUNT BY AREA, before any row is written:
```
GATE-CONDITION-MET:
  SOURCE-GATE: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
  GATE-VERDICT: authorized to proceed -- org diagram artifact received from GATE 2->3
  ARRIVAL-COUNTERPART: Headcount by Area section
```
The SOURCE-GATE field must quote the exact departure gate line, not a paraphrase.

**Gap it closes:** Every gate is currently one-sided: the departure site declares, the arrival site begins. No arrival section actively confirms receipt of its upstream artifact. GATE 2->3 (org diagram -> headcount) is the highest-risk handoff because diagram drift directly corrupts area names, role placements, and Decides allocations. A structured arrival acknowledgment token converts the handoff into a two-sided contract and seeds the structural pattern that the v19 gate-condition-met criteria will formalize.

---

| V | Axes | Key addition vs R17 V-05 |
|---|------|--------------------------|
| V-01 | A only | IF/THEN at 3 violation sites |
| V-02 | B only | STRUCTURING-COST FRAME before mechanism table |
| V-03 | C only | GATE-CONDITION-MET 3-field arrival block at HEADCOUNT |
| V-04 | A + B | Consequence injection + cost frame (no arrival token) |
| V-05 | A + B + C | Maximum -- all three R18 axes active simultaneously |
