Written to `simulations/quest/rubrics/flow-integration-rubric-v13-variations-R13-2026-03-15.md`.

---

## R13 Variations — flow-integration (v13 rubric, 232 pt ceiling)

### Axes selected

| Variation | Single/Combined | Axis | Key probe |
|-----------|----------------|------|-----------|
| V-01 | Single | C-36 minimal framing content | Q1 lower-bound: one-sentence WHY block, no obligation refs |
| V-02 | Single | C-35 + C-36 count-agnostic framing | Q2 probe: five-row table, WHY block ignores cold-start/fifth category |
| V-03 | Single | Phrasing register | Structural neutrality: imperative → declarative throughout |
| V-04 | Combined | C-35 + C-36 extended-set-aware framing | Q1+Q2 upper bound: five-row table, WHY block names all five categories |
| V-05 | Combined | Inertia framing + register + minimal C-36 | Structural neutrality of three combined axes |

---

### Score predictions

| Variation | Ceiling | C-36 predicts | Full prediction |
|-----------|---------|---------------|-----------------|
| V-01 | 212 canonical | PASS if presence+position only; FAIL (−5) if obligation-aware content required | 212/212 or 207/212 |
| V-02 | 232 full | PASS if count-agnostic framing satisfies C-36; FAIL (−5) if extended categories must be named | 232/232 or 227/232 |
| V-03 | 212 canonical | PASS (register is structurally neutral) | 212/212 |
| V-04 | 232 full | PASS regardless of Q1/Q2 resolution | 232/232 |
| V-05 | 212 canonical | PASS if V-01 resolves minimal framing as sufficient; FAIL (−5) if contrast prose is not a valid purpose statement | 212/212 or 207/212 |

---

### Diagnostic logic

**Q1 (C-36 content specificity)** is settled by V-01: if it passes, presence+position is the criterion; if it fails, V-03's obligation-aware framing establishes the lower content bound.

**Q2 (C-35 + C-36 interaction)** is settled by V-02: if it passes, obligation-count-agnostic framing always satisfies C-36; if it fails, V-04 establishes the safe pattern (extended-set-aware framing required when C-35 is in play).

**Inertia framing + register neutrality** is confirmed or refuted by V-05, cross-checking whether the R12 V-03 inertia pattern composes cleanly with V-01's minimal C-36 boundary.

### Key structural decisions per variation

- **V-01 vs V-03**: V-01's WHY block = one sentence, no obligation names. V-03's WHY block = obligation-aware (names all four categories). Both use canonical terms and descriptive/imperative variants respectively — clean Q1 isolation.
- **V-02 vs V-04**: Both use the five-row extended obligation set (trace-call / silent-pass / unverified-system / delegation-chain / cold-start) and the three-token YOU MUST NOT block (forgotten-call, assumed-to-work, unknown-system). The only difference is V-02's WHY block references only the canonical four; V-04's names all five including cold-start.
- **V-03 + V-05 register pattern**: Section exclusions rephrased from "*(this section: X only — Y, Z... each have their own sections below)*" to "*(X only — the other four concerns each occupy a dedicated section)*". Gates rephrased from "Do not open CALL-[N+1] until..." to "CALL-[N+1] opens only after...". Coda rephrased from "fires unconditionally" to "is present regardless of output." All gate conditions remain explicit — no criterion drops below the pass threshold.
