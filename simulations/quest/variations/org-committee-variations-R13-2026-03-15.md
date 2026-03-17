Written to `simulations/quest/golden/org-committee-variate-R13-2026-03-16.md`.

---

## Round 13 — org:committee Variations Summary

**Baseline**: R12 V-05 at 140/140 (v12 rubric). Against v13, it scores ~142/144 — C-34 likely passes via the `[one-phrase locked anchor]` placeholders but has no enforcement rule; C-35 definitely fails because PHASE-3-COMMIT only asserts "at least one CONDITION or BLOCK confirmed" rather than enumerating per-participant stances.

---

### Variation axes used

| V | Primary axis | Gap targeted | Hypothesis |
|---|---|---|---|
| V-01 | Lifecycle emphasis | C-35 + C-34 | Minimal diff from R12 V-05: add vote-anchor manifest to PHASE-3-COMMIT skeleton + fill rule; add VALIDATE for C-34 anchor specificity in PHASE-1 fill rules → 144/144 |
| V-02 | Output format | C-35 + C-34 | Flat command sequence (no skeleton pre-declaration). Tests whether C-35's per-participant manifest is satisfiable without C-28; likely scores ~142/144 — misses C-28 by design |
| V-03 | Phrasing register | C-35 | Conversational register. Describes structural requirements in natural language; all labels (STANCE:, PHASE-N-COMMIT:) remain mandatory. Likely misses C-28 + C-30; tests register-independence of C-35 → ~140/144 |
| V-04 | Lifecycle + Inertia framing | C-34 + C-35 | Elevates INERTIA RECORD and STANCE MANIFEST as named parallel artifacts; explicit C-34 VALIDATE with ACCEPTABLE/FAILS worked examples; skeleton + fill rules preserved → 144/144 |
| V-05 | Full synthesis (all axes) | C-34 + C-35 | R12 V-05 + explicit C-34 VALIDATE with worked examples + C-35 vote-anchor manifest in both skeleton slot and fill rule + TALLY derivation pinned to manifest → 144/144 |

### The two structural additions in every variation

**C-34 closure** — VALIDATE rule with format examples added to PHASE-1 fill rules:
> `VALIDATE: each manifest entry carries a content anchor readable without Phase 1 prose; ACCEPTABLE: INERTIA-FINDING-A: workflow-disruption; FAILS: bare label with no anchor`

**C-35 closure** — PHASE-3-COMMIT skeleton slot and fill rule upgraded from Boolean assertion to per-participant manifest:
> `PHASE-3-COMMIT: [locked] — Stance manifest: [Role Name] BLOCK / [Role Name] CONDITION / [Role Name] APPROVE — one line per participant`
> Plus: `VALIDATE: Phase 4 TALLY derived from this manifest; re-parsing Phase 3 prose for the tally is not permitted`
