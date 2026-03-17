Written to `simulations/quest/rubrics/flow-resilience-rubric-v11-variate-R12-2026-03-15.md`.

---

# flow-resilience — Round 12 Variations (Rubric v11)

**Rubric**: v11 · 29 aspirational criteria · Ceiling entering R12: 21/29 → 97.24 (R11 V-03/V-05)
**R12 objective**: Crack C-09 through C-16 — 8 criteria unaddressed across all prior rounds.

---

## Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | **D only — Chaos Co-Location** | Embedding a chaos block inside each row descriptor forces runnable test specs at scenario granularity; co-location prevents deferral to a standalone section where chaos blocks are routinely compressed or dropped |
| V-02 | **E only — Per-Finding Observability + Completeness Checklist** | `Metric/Alert/Owner` adjacent to each finding transforms the Gap Register from narrative to structured spec; the in-artifact checklist makes finding omission visible as a count failure |
| V-03 | **F only — Recovery Specificity Upgrade** | Actor-chain prefixes (`client →`, `operator →`) and canonical conflict vocabulary (`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`) replace free-text descriptions with template-fill constraints; eliminates the paraphrase escape route |
| V-04 | **D + E** | Orthogonal sections — chaos blocks target scenario rows; observability hooks target Gap Register findings; no structural interference expected |
| V-05 | **D + E + F** | Three axes target three distinct structural slots; should compose without conflict |

---

## Projected Coverage

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Chaos scenarios | D | — | — | D | D |
| C-10 Observability hooks | — | E | — | E | E |
| C-11 Actor chain | — | — | F | — | F |
| C-12 Conflict vocabulary | — | — | F | — | F |
| C-13 Gap-merge prevention | — | E | — | E | E |
| C-14 Chaos co-located | D | — | — | D | D |
| C-15 Per-finding inline hook | — | E | — | E | E |
| C-16 Completeness checklist | — | E | — | E | E |
| C-17–C-37 (inherited) | all | all | all | all | all |

**Projected composites (all targeted criteria pass)**:

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Aspirational | 23/29 | 25/29 | 23/29 | 27/29 | 29/29 |
| Composite | 97.93 | 98.62 | 97.93 | 99.31 | **100.00** |

---

## Key Design Decisions Per Axis

**Axis D (Chaos Co-Location)**:
- Chaos block specification added as a standalone meta-table (Inject / Expected Behavior / Pass Signal / Fail Signal)
- Row descriptors carry a co-located chaos fill block *after* the main row gate — the advance inhibitor is extended to include chaos block completion
- Section Order Requirement updated: "all 3 rows + chaos blocks before Gap Register"
- Anti-boundary instruction explicitly negates a standalone chaos section as a structural escape route

**Axis E (Observability + Completeness)**:
- Gap Register format upgraded: each finding carries `Metric:` / `Alert:` / `Owner:` inline — not a separate observability section
- Completeness Checklist appears as output content after the Inertia Verdict: `[ ] / [ ] / [ ] — Finding types present: ___ of 3`
- Anti-boundary instruction explicitly negates a separate observability section
- Satisfies C-13 (gap-merge prevention via labeled checklist), C-15 (per-finding inline hooks), C-16 (checklist as output content)

**Axis F (Recovery Specificity)**:
- Stage sub-specifications updated: each Mechanism must begin with `client →`, `server →`, `operator →`, or `user →` (at least 3 of 4 stages per row)
- Conflict vocabulary constraint added as a Column Contract note applying globally to all columns
- Data at Risk fill requirement for Class 3 rows requires canonical strategy name + adequacy judgment
- Row 3 advance inhibitor extended to include the canonical vocabulary requirement
