Written to `simulations/quest/golden/flow-resilience-variate-R3-2026-03-15.md`.

---

## flow-resilience — Round 3 Variations (Rubric v3)

### Design notes

R3 has four changes to address. Each requires a structural enforcement mechanism, not a soft instruction:

| Change | Failure mode being fixed | Structural solution |
|--------|--------------------------|---------------------|
| C-14 (new) | CR section and DCV section are independent silos; inadequate strategies never appear in gap tally | Retroactive DCV Amendment Gate — a lifecycle phase that reopens the DCV section after CR analysis and either adds linked DCV entries or records explicit confirmation |
| C-15 (new) | Impossibility arguments cite description absence ("topic doesn't mention X") not architecture | "DS Primitive cited:" as a required named field in the impossibility template — field label explicitly rejects topic-scope arguments |
| C-11 (strengthened) | Low-confidence entries flagged but still enter the table | Hard bar with gate language: disposition is BARRED (not "Flagged"), gate has explicit lift conditions, flagging alone is invalid |
| C-12 (strengthened) | Nil findings are bare "none found" without scope rationale | Scope rationale is a required field in the nil-finding template — bare statement cannot be inserted without completing the rationale |

---

### V-01 — Lifecycle emphasis: Retroactive DCV Amendment Gate
**Targets C-14.** A lifecycle phase after CR analysis forces reopening the DCV section. The model must count entries where Adequate = "no" or Strategy = "undefined" and either write the linked DCV entries (citing the CR source) or write an explicit CLOSED confirmation. Neither outcome is optional — the artifact is not complete until the gate executes.

### V-02 — Output format: DS-Primitive-Anchored Impossibility Template
**Targets C-15.** The impossibility argument template contains a required `DS Primitive cited:` field with in-template text that specifies what is valid (CAP guarantee, deployment topology, synchronous consistency guarantee) and what is invalid (description absence). A reviewer can scan for this field and reject any entry where the content is topic-scope rather than architectural.

### V-03 — Phrasing register: Hard Gate Language
**Targets C-11 strengthened.** Uses GATE OPEN / GATE CLOSED framing with explicit entry/exit conditions per phase. Low-confidence entries have disposition `GATE OPEN — LOW CONFIDENCE` (not "Flagged"), gate has named lift conditions, and "Flagged" is explicitly listed as a non-existent disposition. Combines the Amendment Gate (C-14) and DS-primitive template (C-15) at their R2 levels while adding the hard-gate register vocabulary throughout.

### V-04 — Combination: Lifecycle emphasis + Output format
**Targets C-14 + C-15.** The §4 Amendment Gate and the DS-Primitive impossibility template in §0 are compatible and non-conflicting: the format axis applies at coverage time (§0) and confidence triage (§1); the lifecycle axis applies at CR analysis time (§4). The R2 mechanisms (nil-finding with scope rationale, low-confidence bar) are included at v3 strength.

### V-05 — Combination: Lifecycle + Output format + Phrasing register + **Inertia framing**
**Targets all four R3 changes plus explores a new axis.** Inertia framing adds a mandatory "What the current design does in this condition" field to every scenario analysis. This surfaces the status-quo gap explicitly — the difference between what the current design does and what it should do is the finding. For C-14, the inertia frame also appears in Step 4's split-brain analysis: "what does the current design do in a conflict" makes inadequate strategies visible as a contrast between current behavior and required invariant, not just an abstract adequacy verdict.
