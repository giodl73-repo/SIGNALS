Now I have enough to score all variations. Let me perform the full evaluation.

---

## Scorecard: `topic:status` — Round 16 (Rubric v15, max 285)

---

### Evaluation Framework

All five variants share the same structural foundation through C-46. The R16-specific differentiators are:
- **C-47 (candidate):** Labeled `P1-ADVERSARY:` / `P2-ADVERSARY:` / `P3-ADVERSARY:` sub-components within the preamble `ADVERSARY CHAIN:` block
- **C-48 (candidate):** PHASE 1 execution-body `ADVERSARY:` + `DEFEAT CONDITION:` block, extending the adversary chain to signal acquisition

---

### V-01: Minimum delta — C-47 + C-48 in execution-prose form

**Axis:** Both C-47 and C-48 candidates added to R15 V-01 baseline.

| Tier | Criteria | Result | Evidence |
|------|----------|--------|---------|
| Essential | C-01–C-04 | PASS ×4 | Glob→DISK_SIGNALS, formula+guard, gap list, "Write no files" |
| Recommended | C-05–C-07 | PASS ×3 | Readiness verdict, 9-namespace table, strategy.md reference |
| Aspirational | C-08–C-11 | PASS ×4 | STALE EVIDENCE, HIGHEST PRIORITY RISK, all 9 rows, named phases + DISPLAY GATE |
| C-12 | Gap-first ordering | PASS | COMMIT RISK REGISTER precedes EXPOSURE SUMMARY in template |
| Tier 2 | C-13–C-16 | PASS ×4 | Triple-redundancy, template-first, per-signal assertion, "Committing now means..." |
| Tier 3 | C-17–C-19 | PASS ×3 | [LAYER 1--STRUCTURAL], [LAYER 2--SEMANTIC], [LAYER 3--EXECUTION]; consequence vocab saturation |
| C-20 | Primary gap artifact | PASS | Label: `primary gap artifact; first section; precedes EXPOSURE SUMMARY` |
| Tiers 4–7 | C-21–C-29 | PASS ×9 | Full compressed phase names, cross-layer vocab, field annotations, multi-site chain |
| Tier 7 | C-30–C-31 | PASS ×2 | Exit B topic-absent; per-row "ships without...on commit" |
| Tier 8 | C-32–C-34 | PASS ×3 | Named exits, preamble invariant, axis-enumerated with triggers |
| Tiers 9–10 | C-35–C-38 | PASS ×4 | Per-axis triggers in preamble+GUARD+OUTPUT DECLARATION; phase-resident OUTPUT DECLARATION |
| Tiers 11–12 | C-39–C-42 | PASS ×4 | Trigger chars in OUTPUT DECLARATION; labeled sub-components; PHASE 3 OUTPUT DECLARATION; PHASE 2 adversary body |
| Tier 13 | C-43–C-44 | PASS ×2 | PHASE 3 adversary body; `OUTPUT DECLARATION CHAIN:` in preamble |
| Tier 14 | C-45–C-46 | PASS ×2 | `ADVERSARY CHAIN:` block (3-element); DEFEAT CONDITION at P2 + P3 |
| **C-47 candidate** | Labeled preamble sub-components | **PASS** | `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries — each independently addressable by phase label |
| **C-48 candidate** | PHASE 1 adversary body | **PASS** | PHASE 1 body opens with `ADVERSARY: inertia toward empty-glob assumption` + `DEFEAT CONDITION: DISK_SIGNALS populated from live glob result...` |

**Score: 285/285**

---

### V-02: C-47 withheld — inertia framing axis (prose ADVERSARY CHAIN)

**Axis:** ADVERSARY CHAIN in preamble names all three adversaries in running prose — no labeled `PN-ADVERSARY:` sub-components. PHASE 1 body retains full three-part adversary block (C-48 PASS).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-11 | PASS ×11 | Same foundation as V-01 |
| C-12 | PASS | COMMIT RISK REGISTER before EXPOSURE SUMMARY |
| C-13–C-44 | PASS ×32 | Full structural chain intact |
| C-45 | PASS | `ADVERSARY CHAIN:` block present in preamble; names P1, P2, P3 adversaries in prose — P2 and P3 named as chain with independence assertion. Prose form satisfies the naming requirement. |
| C-46 | PASS | DEFEAT CONDITION at P2, P3 (and P1 via C-48 presence) |
| **C-47 candidate** | **FAIL** | Preamble `ADVERSARY CHAIN:` block is running prose: `"PHASE 1 adversary -- inertia toward empty-glob assumption (...); PHASE 2 adversary -- ...; PHASE 3 adversary -- ..."` — no `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries. Adversaries not independently addressable by phase label without prose scanning. |
| **C-48 candidate** | **PASS** | PHASE 1 body: `ADVERSARY: inertia toward empty-glob assumption...` + `DEFEAT CONDITION: DISK_SIGNALS populated from live glob result...` |

**Score: 285/285** (C-47 not yet a criterion under v15)

---

### V-03: C-48 withheld — readiness-first output format axis

**Axis:** PHASE 1 body has no adversary block (C-48 FAIL). Preamble carries labeled `P2-ADVERSARY:` + `P3-ADVERSARY:` sub-components (C-47 PASS). Output template reordered: READINESS VERDICT first, then COMMIT RISK REGISTER.

**⚠ Design contamination detected.** The readiness-first reordering violates two established criteria, introducing confounds beyond the intended C-48 isolation.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-11 | PASS ×11 | Glob, coverage formula, gap list, display-only, readiness verdict, all namespaces, strategy ref, STALE EVIDENCE, HIGHEST PRIORITY RISK, all 9 namespace rows, named phases |
| **C-12** | **FAIL** | Template section 1 is `READINESS VERDICT -- {topic}` containing `Coverage: {found}/{planned} ({pct}%)` and `Readiness: READY | PARTIAL | NOT READY` — the rolled-up aggregate appears **before** the COMMIT RISK REGISTER (section 2). Pass condition explicitly requires gap register to precede aggregate; "Gaps are seen before the rolled-up percentage" is directly violated. |
| C-13–C-19 | PASS ×7 | All three layer types labeled at mechanism locations (`[LAYER 1 -- SEMANTIC]`, `[LAYER 2 -- STRUCTURAL]`, `[LAYER 3 -- EXECUTION]`) — types correctly assigned to their mechanisms, ordinal swap does not prevent identification; template before execution; consequence vocabulary present |
| **C-20** | **FAIL** | COMMIT RISK REGISTER is **not** the first output section (READINESS VERDICT is first). Label reads `[LAYER 2 -- STRUCTURAL: primary gap artifact; follows verdict]` — contains "primary gap artifact" but substitutes "follows verdict" for "precedes EXPOSURE SUMMARY"; positional requirement ("It is the first output section") explicitly not met. C-12 also required and fails. |
| C-21–C-44 | PASS ×24 | Phase names, cross-layer vocab, field annotations, multi-site chains, named exits, preamble invariant, trigger characterization, OUTPUT DECLARATIONs, adversary chain at P2+P3, preamble OUTPUT DECLARATION CHAIN — all present and intact |
| C-45 | PASS | `ADVERSARY CHAIN:` in preamble with labeled `P2-ADVERSARY:` and `P3-ADVERSARY:` entries, independence assertion present |
| C-46 | PASS | DEFEAT CONDITION at P2 and P3 adversary blocks |
| **C-47 candidate** | **PASS** | Preamble `ADVERSARY CHAIN:` carries `P2-ADVERSARY:` and `P3-ADVERSARY:` labeled sub-components — two-element labeled chain satisfies the structural requirement; absence of P1-ADVERSARY: is because C-48 (P1 adversary body) is withheld, not a C-47 violation |
| **C-48 candidate** | **FAIL** | PHASE 1 body opens directly with `Glob: simulations/**/{topic}-*` — no `ADVERSARY:` clause, no `DEFEAT CONDITION:` sub-component at PHASE 1 entry |

**Score: 275/285** (−5 C-12, −5 C-20)

> **Design issue:** The readiness-first template reordering is a contaminating axis. V-01 vs V-03 is intended to cleanly isolate C-48, but the actual delta is 10 points (285 − 275), of which 10 points are from C-12/C-20 violations unrelated to C-48. If C-48 were formalized as a 5-point criterion in v16, V-03 would score 270 (C-12 − 5, C-20 − 5, C-48 − 5 = −15). The clean isolation of C-48 is broken — V-03 needs redesign with an output format axis that preserves C-12/C-20 compliance (e.g., template column reordering, not sectional reordering).

---

### V-04: Lifecycle GUARD contract form — C-47 + C-48

**Axis:** All execution phases use `+-- PHASE N --+` contract boxes (INPUT / GUARD / OUTPUT fields) with adversary declarations in execution prose appended below each box.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-11 | PASS ×11 | Standard foundation |
| C-12 | PASS | Template section order: COMMIT RISK REGISTER [LAYER 1 STRUCTURAL] first, EXPOSURE SUMMARY after namespace table |
| C-13–C-19 | PASS ×7 | Labels at mechanism locations, template-first |
| C-20 | PASS | `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]` at COMMIT RISK REGISTER |
| C-21–C-44 | PASS ×24 | Phase names, cross-layer vocab, EXIT A/B labeled in GUARD fields, OUTPUT DECLARATION in prose below GUARD boxes, full adversary chain at P2+P3 |
| C-45 | PASS | `ADVERSARY CHAIN:` with labeled P1/P2/P3-ADVERSARY: in preamble |
| C-46 | PASS | DEFEAT CONDITION in prose below PHASE 2 and PHASE 3 GUARD boxes |
| **C-47 candidate** | **PASS** | Preamble `ADVERSARY CHAIN:` carries `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries — form-agnostic; labeled sub-components present regardless of GUARD contract format in execution body |
| **C-48 candidate** | **PASS** | PHASE 1 execution prose below GUARD box: `ADVERSARY: inertia toward empty-glob assumption...` + `DEFEAT CONDITION: DISK_SIGNALS populated from live glob result...` — adversary declaration present in PHASE 1 execution body; form-agnosticism of lifecycle-contract format confirmed |

**Score: 285/285**

---

### V-05: Elevated titled adversary-declaration blocks — C-47 + C-48

**Axis:** All three active phases (PHASE 1, 2, 3) receive `+-- PHASE N ADVERSARY DECLARATION --+` titled boxes with `ADVERSARY:`, `TRIGGER:`, `DEFEAT CONDITION:` fields at phase entry.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-11 | PASS ×11 | Standard foundation |
| C-12 | PASS | COMMIT RISK REGISTER first in template |
| C-13–C-44 | PASS ×32 | Full structural chain; titled adversary boxes at P2+P3 satisfy C-42/C-43; OUTPUT DECLARATIONs present in execution prose sections |
| C-45 | PASS | `ADVERSARY CHAIN:` with labeled P1/P2/P3-ADVERSARY: in preamble |
| C-46 | PASS | DEFEAT CONDITION field present in P2 and P3 titled adversary declaration boxes |
| **C-47 candidate** | **PASS** | Preamble `ADVERSARY CHAIN:` carries `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries |
| **C-48 candidate** | **PASS** | `+-- PHASE 1 ADVERSARY DECLARATION --+` titled box with `ADVERSARY:`, `TRIGGER:`, `DEFEAT CONDITION:` fields at PHASE 1 entry — three-phase adversary chain complete in titled-block form; form-agnosticism of elevated titled blocks confirmed |

**Score: 285/285**

---

## Score Summary

| Variant | C-12 | C-20 | C-45 | C-46 | C-47 (cand.) | C-48 (cand.) | Score (v15) |
|---------|------|------|------|------|--------------|--------------|-------------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | **285** |
| V-02 | PASS | PASS | PASS | PASS | FAIL | PASS | **285** |
| V-03 | **FAIL** | **FAIL** | PASS | PASS | PASS | FAIL | **275** |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | **285** |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | **285** |

**Ranking:** V-01 / V-02 / V-04 / V-05 tied at 285 → V-03 at 275.

---

## Excellence Signals (from V-01, V-04, V-05)

**Pattern 1 — Labeled preamble adversary chain sub-components.** The preamble `ADVERSARY CHAIN:` block carries `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries, making each adversary independently addressable by phase label without scanning running prose. Parallel to how C-40 extended OUTPUT DECLARATION from undifferentiated prose to labeled `INVARIANT:` / `OUTPUT FORM:` sub-components. The preamble now carries three architectural invariant blocks each with labeled sub-components: exits (C-34), output declarations (C-44 + C-40-parallel labeling), adversary chain (C-45 + labeled sub-components).

**Pattern 2 — Three-phase adversary chain completion at signal acquisition.** PHASE 1 execution body gains a full three-part adversary block (`ADVERSARY: inertia toward empty-glob assumption` + `DEFEAT CONDITION: DISK_SIGNALS populated from live glob result...`), extending the adversary chain from two-phase (P2+P3 established by C-42/C-43/C-46) to three-phase (P1+P2+P3). The PHASE 1 adversary is structurally distinct from P2 and P3 — it fires at the disk-access gate, before any commitment assertion or coverage computation runs.

**Pattern 3 — Form-agnosticism of both candidates confirmed.** V-04 (lifecycle GUARD contract) and V-05 (elevated titled adversary blocks) both satisfy C-47 and C-48 at the same score as V-01 (execution-prose). Both labeled preamble sub-components and PHASE 1 adversary body are form-agnostic, consistent with R11–R15 form-agnosticism confirmations.

**Anti-pattern (V-03 contamination finding).** The readiness-first output template reordering violates C-12 (gap-first ordering — aggregate Coverage % precedes COMMIT RISK REGISTER) and C-20 (COMMIT RISK REGISTER not first output section; label says "follows verdict" not "precedes EXPOSURE SUMMARY"), introducing a −10 penalty unrelated to C-48. V-01 vs V-03 delta is 10 pts under v15, not 0, breaking the intended C-48 isolation. A future V-03 for C-48 isolation should use an output format axis that preserves gap-first ordering (e.g., column reordering within the register table, or date format changes) rather than sectional reordering.

---

```json
{"top_score": 285, "all_essential_pass": true, "new_patterns": ["Labeled per-phase sub-components in preamble ADVERSARY CHAIN block (P1-ADVERSARY:, P2-ADVERSARY:, P3-ADVERSARY:) making each adversary independently addressable by phase label without prose scanning — extends preamble block from prose-form chain to labeled-form chain", "PHASE 1 execution-body adversary declaration with DEFEAT CONDITION extending the adversary chain from two-phase (P2+P3) to three-phase (P1+P2+P3) at signal acquisition entry before any commitment assertion or coverage computation runs"]}
```
