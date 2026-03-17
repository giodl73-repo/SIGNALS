Here is the complete v14 rubric:

---

## Changes v13 → v14

**Promotions (four simultaneous — rubric-history first):**
- **C-26 → Proven (R13+R14)** — Archetype constraint vocabulary specification
- **C-27 → Proven (R13+R14)** — Composability manifest synthesis claim separation
- **C-28 → Proven (R13+R14)** — Manifest pre-populated baseline pair inspection
- **C-30 → Proven (R13+R14)** — Baseline entry template completeness

**Status update:**
- **C-31** — Unproven (first confirmed R14) — second confirmation required for proven promotion

**Scoring model:**
- v13: Proven 25 pts = 100 (budget exactly exhausted)
- v14: Proven 29 pts, budget 25 pts, ceiling 100 — proven criteria now exceed the budget by 4 pts; ceiling is reachable with up to 4 proven-criteria-pts failing

**Three new aspirational criteria:**

| ID | Name | Pts | Status | Source |
|----|------|-----|--------|--------|
| C-32 | Coherence audit verbatim-restate depth | 1 | Unproven | R14/V-01 — canonical reference at full documentary depth; V-05 compressed directive passes C-31, not C-32 |
| C-33 | Coherence audit gate-order independence | 1 | Unproven | R14/V-02 — gate reordering cannot suppress the audit; independence must be explicit in template structure |
| C-34 | Pre-inspection domain failure mode taxonomy | 1 | Unproven | R14/V-03 — preamble names "silent antagonism" + "archetype drift"; increases C-21/C-17 depth additively, no structural friction |

---

### New criterion rationale

**C-32 — Coherence audit verbatim-restate depth**
R14/V-01 is the canonical reference implementation: the coherence audit section explicitly restates all three layers' synthesis claims side-by-side (named with layer identifiers) before running the COHERENT/INCOHERENT verdict gate. R14/V-05 compresses this to directive form — a conditional rewrite instruction encoding the check without elaborating the comparison protocol. Both pass C-31. Only V-01 passes C-32. The boundary is audit portability: a verbatim-restate audit is self-sufficient (the author can execute the comparison without consulting the original claim locations); a directive audit is memory-dependent. C-32 is distinct from C-31: C-31 requires the audit section, three named layers, verdict gate, and blocking instruction; C-32 additionally requires the verbatim-restate instruction at full documentary elaboration.

**C-33 — Coherence audit gate-order independence**
R14/V-02 reorders per-surprise gates (Check B → CAT → NGT) while holding all other structure constant. The coherence audit passes unchanged — it does not interleave with the resequenced gates. Gate-order independence is confirmed as a structural property. C-33 requires that independence to be explicit in the template rather than emergent from the current gate order: the audit section must be structurally marked as post-inspection (by header, boundary instruction, or entry gate) so that any gate reordering cannot suppress or embed the audit within a per-gate step. C-33 is distinct from C-31: C-31 requires the audit to exist; C-33 requires its post-inspection isolation to be architecturally declared.

**C-34 — Pre-inspection domain failure mode taxonomy**
R14/V-03 adds a preamble block naming two domain failure modes — "silent antagonism" (mechanisms that each achieve their target criteria in isolation while degrading each other in compound configurations) and "archetype drift" (pair archetype classification shifts across rounds as new pairs are added). The block precedes all pair inspections. It increases C-21 analytical depth and C-17 composability rigor without structural friction with C-26 or the manifest template. V-04 confirms the V-02+V-03 combination is fully parallel and additive. C-34 is distinct from C-26 (per-archetype vocabulary constraints within a single inspection) and from inertia framing (generic phase prevention labels): C-34 names cross-pair mechanism patterns discoverable only across the inspection set, not within a single archetype's constraint class.

---

### Updated symmetric architecture

| Layer | Analytical (proven) | Synthetic |
|-------|---------------------|-----------|
| Live inspection | C-21 (mechanism field) | C-27 (synthesis claim field — **Proven R13+R14**) |
| Illustration | C-25 (mechanism in example) | C-29 (synthesis claim in example — Proven R12+R13) |
| Baseline | C-28 (mechanism in pre-populated entry) | C-30 (synthesis claim in pre-populated entry — **Proven R13+R14**) |
| Cross-layer | — | C-31 (coherence across layers — Unproven, first confirmed R14) |
| Cross-layer depth | — | C-32 (verbatim-restate depth — Unproven) |
| Cross-layer structure | — | C-33 (gate-order independence — Unproven) |
| Pre-inspection | — | C-34 (failure mode taxonomy — Unproven) |

The file is written to `simulations/quest/rubrics/topic-echo-rubric-v14-2026-03-15.md` (full document with all 34 criteria, scoring model, and Round 14 + prior excellence signals sections).
