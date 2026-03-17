Written to `simulations/quest/golden/org-review-variate-R10-2026-03-17.md`.

---

# org-review -- Variate R10

5 complete prompt body variations targeting C-33, C-34, C-35 simultaneously for the first time. All variants carry V-05 R11 (210/225) as base.

---

## R10 Design Target

V-05 R11 scores 210/225 under v11 — perfect through C-32, missing all three new criteria.

| Gap | What's missing |
|-----|---------------|
| C-33 | LENS COVERAGE TABLE has ADDRESSED/OPEN columns but no per-row Applicability rating |
| C-34 | Vacuous (C-33 absent → no HIGH-applicability tier for domain gap-check) |
| C-35 | Challenger uses prose null hypothesis; no structured dimension comparison table |

---

## Variation Axes

| Variant | Axes | New criteria | Predicted |
|---------|------|-------------|-----------|
| V-01 | **Inertia framing** | C-35 only | 215/225 |
| V-02 | **Output format** | C-33 + C-34 only | 220/225 |
| V-03 | **Lifecycle emphasis** | C-35 + §9 Stage-1 binding | 215/225 |
| V-04 | **Inertia + Output format** | C-33 + C-34 + C-35 | **225/225** |
| V-05 | **Inertia + Output format + Lifecycle** | C-33 + C-34 + C-35 + dependency chain | **225/225** |

---

## New Structural Elements

**§0 CHALLENGER NULL HYPOTHESIS DIMENSION TABLE** (C-35): Pre-bracket protocol. Challenger opens BRACKET OPENING with a `Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict` table (min 2 rows). `BUILD-WINS / STATUS-QUO-WINS / TIED` per dimension. g_null(initial) derivable from majority count without reading prose. GOpen must equal the table majority or declare a named override. Distinct from C-16 (bracket-wide scaffold re-scored by domain) — §0 is challenger-only, pre-domain.

**§17 LENS APPLICABILITY PROTOCOL** (C-33): Adds a 4th `Applicability` column to the §5.7 LENS COVERAGE TABLE. Rating is `HIGH / MEDIUM / LOW`, artifact-specific (not inherited from role definition). Coverage expectation by tier: HIGH-applicability OPEN → ADVISORY-OPEN-LENS; MEDIUM-applicability OPEN → ADVISORY-LOW; LOW-applicability OPEN → no penalty.

**§18 DOMAIN COVERAGE GAP-CHECK** (C-34): After §5.7, a §5.8 section reads the §17 Applicability tiers and identifies every artifact domain (from §1) with no HIGH-applicability reviewer. Each such domain → ADVISORY-GAP in ACTION ITEM REGISTER (domain name, max tier found, reason). Excluded from gate ledger. §18 depends on §17 complete.

---

## Excellence Signals for v12

**C-36 candidate** (V-05 only): *Dependency Chain Declaration Pre-committed as Named Preamble Block.* A `DEPENDENCY CHAIN DECLARATION [IMMUTABLE]` block enumerates all inter-protocol bindings (§17→§18, §0→§9) and phase assignments before any reviewer runs. Pipeline auditable at declaration time.

**C-37 candidate** (V-03, V-05): *§9 Stage 1 Structural Source Binding.* §9 NULL HYPOTHESIS PROGRESSION CONTRACT explicitly names the §0 table as the structural source for `g_null(initial)`. Stage 1 is derivable from table data alone — not just "consistent with" the table but mechanically bound to its majority verdict.
