Written to `simulations/quest/rubrics/flow-dataflow-rubric-v16-R16-2026-03-15.md`.

---

# flow-dataflow — Round 16 Variations

## Variation design rationale

**R15 gap**: The closed-chain paragraph listed SC-12 and SC-13 as named navigation entries, but didn't annotate every SC with governed artifact tokens and enforcement mechanisms. C-48 and C-49 generalize this to all SCs — the paragraph must be an exhaustive self-describing authority map.

**R16 design commitment**: Every variation contains an exhaustive closed-chain paragraph listing SC-1 through SC-13 (plus SC-14 when non-tabular is active), where each entry names the governed `[A-xx]` tokens and the enforcement mechanism. This makes every structural failure mode navigable from the register index by token match, without reading any SC body or role instruction.

---

## V-01 — Natural role sequence, tabular, universal closed-chain (C-48 + C-49)

**Axis**: Baseline — Finance → Operations → Commerce  
**Hypothesis**: Finance → Operations → Commerce; retail e-commerce order-to-cash pipeline. An exhaustive closed-chain paragraph naming governed tokens and enforcement mechanisms for all SC-1 through SC-13 makes REGISTER DECLARATION a complete self-describing authority map. Commerce (pos 3) cites Finance [A-04] skip-level (SC-12). Tabular.

**Scenario**: Customer order capture → payment authorization → fraud detection → payment settlement → AR ledger → revenue recognition → Commerce BI. Finance establishes the revenue recognition SLA and manual order-processing baseline.

**Artifact registry** (`[A-01]` INCUMBENT BASELINE through `[A-14]` TRADE-OFF ANALYSIS):
- `[A-01]` INCUMBENT BASELINE — Finance; ≥3 manual steps with durations
- `[A-02]` DOMAIN CONTEXT — entity vocabulary, SLA, cadence  
- `[A-03/04]` Stage trace / Boundary checks — Finance
- `[A-05]` PHASE GATE 1
- `[A-06/07]` Stage trace / Boundary checks — Operations  
- `[A-08]` PHASE GATE 2 (SC-12 item verifies Commerce includes `[A-04]`)
- `[A-09/10]` Stage trace / Boundary checks — Commerce
- `[A-11]` STALE ANALYSIS, `[A-12]` RECOVERY PRESCRIPTIONS, `[A-13]` INCUMBENT TOTAL, `[A-14]` TRADE-OFF ANALYSIS

**Closed-chain paragraph**: All SC-1 through SC-13 entries. Each entry names governed artifact tokens and enforcement mechanism. Example entries:
- SC-9 governs `[A-04]`, `[A-07]`, `[A-10]` (`Incumbent Equiv.` column); enforced by Part A cell-form requirement — `[A-01]` token required; bare duration without token fails by token-match without inspecting surrounding prose.
- SC-13 governs `[A-12]` and `[A-14]`; enforced by inline callbacks at both section headers verifying `[A-01]` citation by token match without output-prose inspection.

---

## V-02 — Non-natural Finance-last, tabular, exhaustive closed-chain (C-48 + C-49)

**Axis**: Role sequence — Commerce → Operations → Finance  
**Hypothesis**: Healthcare claims adjudication pipeline. Finance-last ordering stresses skip-level citation. SC-12's closed-chain entry names `[A-04]` (Commerce's boundary checks) as the governed artifact token and the Phase Gate 2 enforcement by SC number — making Finance's skip-level obligation discoverable from the register index alone. Position distance is two: Finance = pos 3, Commerce = pos 1.

**Scenario**: Claim submission portal → intake validator → duplicate detection → clinical adjudication engine → payment authorization → EOB generation → EFT settlement → Finance ledger.

**Key variations from V-01**:
- Role order: Commerce (intake) → Operations (adjudication) → Finance (settlement)
- SC-12 governs `[A-04]` (Commerce's boundary checks) via Finance's `Citing:` line; enforced by Phase Gate 2 item citing `[SC-12]` by number
- All other SCs apply identically with same governed-token + enforcement-mechanism structure

---

## V-03 — Prose register, SC-14 active, exhaustive closed-chain (C-48 + C-49 + C-47)

**Axis**: Output format — non-tabular prose register  
**Hypothesis**: SaaS subscription recurring billing pipeline. SC-14 FORMAT MODE DECLARATION is active and its closed-chain entry names all non-tabular role output artifacts as governed tokens and names the criterion substitution map check as its enforcement mechanism — making format-mode compliance failures navigable from the register index. Commerce (pos 3) cites Finance `[A-04]` skip-level.

**Key variations from V-01**:
- Prose register throughout; all boundary checks use labeled paragraph format (7 required labels)
- REGISTER DECLARATION includes a **criterion substitution map** for C-28, C-30, C-32, C-34, C-37
- **SC-14 FORMAT MODE DECLARATION** added to closed-chain paragraph: governs `[A-03]`, `[A-04]`, `[A-06]`, `[A-07]`, `[A-09]`, `[A-10]`, `[A-13]`; enforced by substitution map completeness check — absent label sequence in any boundary paragraph fails by the substitution map's prescribed form
- C-49 for SC-14 is: the enforcement mechanism is the criterion substitution map check, not output-prose inspection

---

## V-04 — Maximum inertia framing, tabular, exhaustive closed-chain (C-48 + C-49)

**Axis**: Inertia framing — `[A-01]` anchors every SC that touches it  
**Hypothesis**: Manufacturing MRO procurement-to-pay pipeline. `[A-01]` requires ≥5 named manual steps (vs. the standard ≥3). Every SC whose governed artifacts or enforcement mechanism references `[A-01]` names it explicitly in the closed-chain entry. SC-13's entry places maximum emphasis on the dual-callback enforcement, naming `[A-01]` as the procurement baseline authority at both enforcement sites. Tests whether heavy incumbent framing amplifies C-48/C-49 by making `[A-01]` the visible anchor of the entire closed chain.

**Key variations from V-01**:
- `[A-01]` requires ≥5 steps (not ≥3); registry description notes this explicitly
- Closed-chain entries for SC-8, SC-9, SC-11, SC-13 explicitly name `[A-01]` in both the governed-token declaration and the enforcement mechanism  
- SC-13 entry states: "enforced by inline callbacks at both `[A-12]` and `[A-14]` headers that verify `[A-01]` citation by token match without output-prose inspection — `[A-01]` is the procurement baseline authority; its absence is a protocol violation detectable from the header line alone"

---

## V-05 — Combined: non-natural Operations-first + lifecycle depth, tabular (C-48 + C-49)

**Axis**: Role sequence + Lifecycle emphasis  
**Hypothesis**: Digital advertising spend reporting pipeline; Operations → Commerce → Finance. Finance (pos 3) cites Operations `[A-04]` skip-level. A **Phase Gate 0** (`[A-00]`) is added as a pre-role setup verification gate — it verifies the ARTIFACT REGISTRY, REGISTER DECLARATION, BOUNDARY BLOCK SCHEMA, and STRUCTURAL CONSTRAINTS are complete before any role begins. SC-6 governs `[A-00]`, `[A-05]`, `[A-08]` (all three phase gates); its closed-chain entry names all three governed tokens and the gating callback enforcement mechanism. Tests whether C-48/C-49 compliance scales to deeper lifecycle scaffolding.

**Key variations from V-01**:
- `[A-00]` PHASE GATE 0 added to registry; SC-6's closed-chain entry governs `[A-00]`, `[A-05]`, `[A-08]`
- Role order: Operations → Commerce → Finance (Finance-last, skip-level)
- SC-12 governs `[A-04]` (Operations' boundary checks) via Finance's `Citing:` line; position distance two: Finance = pos 3, Operations = pos 1
- Phase Gate 0 checklist includes explicit item: "REGISTER DECLARATION closed-chain paragraph lists all SC-1 through SC-13 with governed tokens and enforcement mechanisms (C-48, C-49)"

---

**Saved**: `simulations/quest/rubrics/flow-dataflow-rubric-v16-R16-2026-03-15.md`
