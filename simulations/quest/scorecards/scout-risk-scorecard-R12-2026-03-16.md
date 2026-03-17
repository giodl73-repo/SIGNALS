# Quest Score — Scout-Risk R12 / Rubric v11

**Skill**: scout-risk · **Round**: 12 · **Rubric version**: v11 (max 142) · **Variations**: V-01–V-05
**Baseline**: R11 V-05 = 142/142. All R12 variations explicitly preserve C-01–C-34.

---

## Scoring Convention

| Symbol | Meaning |
|--------|---------|
| ✓ | PASS — criterion met at baseline level |
| ✓+ | PASS PLUS — criterion met and structurally enhanced beyond baseline |
| ~ | PARTIAL — criterion met but with weaker evidence |
| ✗ | FAIL |

---

## Criterion-by-Criterion Matrix

### Phase 0 — Taxonomy Pre-Phase

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-01 | Phase 0 executes before register build | ✓ | ✓ | ✓ | ✓ | ✓+ |
| C-02 | Risk categories enumerated with labels | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-03 | Taxonomy output feeds Phase 1 cell-by-cell | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-04 | Taxonomy is not collapsed into Phase 1 prose | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-05 | IF-THEN likelihood framing set in Phase 0 | ✓ | ✓ | ✓ | ✓ | ✓ |

**C-01 note**: V-05 adds Phase 0a AMEND resolution as a named sub-phase before any role or register work begins — the strongest structural isolation of scope-setting seen across all rounds.

---

### Phase 1 — Dimensional Register

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-06 | Dimension column populated across all five categories | ✓ | ✓ | ✓+ | ✓ | ✓+ |
| C-07 | Risk ID present and unique per row | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-08 | Likelihood expressed as IF-THEN named conditions | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 | Mitigation typed (prevent / detect / contain / recover) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 | Mitigation carries inline sub-field values | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-12 | Severity cell uses constrained vocabulary | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 | 7-row floor reached or exceeded | ✓ | ✓ | ✓+ | ✓ | ✓+ |
| C-14 | No dimension starved (≥1 row per dimension) | ✓ | ✓ | ✓+ | ✓ | ✓+ |
| C-15 | HIGH severity anchor present per dimension | ~ | ~ | ✓+ | ~ | ✓+ |

**C-06/C-13/C-14/C-15 notes**: V-03 and V-05 introduce the **HIGH-seed sub-phase** — one HIGH anchor per dimension is placed before any expansion rows are added. This converts dimensional HIGH coverage from an incidentally achieved property into a structurally guaranteed one. V-01/V-02/V-04 preserve baseline but do not enforce the HIGH-per-dimension constraint at the process level; C-15 is PARTIAL for those three because the spec does not structurally mandate it.

---

### Phase 1b — AMEND

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-10 | AMEND confirmation present when scope narrowed | ✓ | ✓ | ✓ | ✓ | ✓+ |
| C-34 | AMEND header names suppressed dimensions explicitly (v11) | ✓ | ✓ | ✓ | ✓ | ✓+ |

**C-10/C-34 note**: V-05 pairs Phase 0a AMEND resolution with a vocabulary-constrained header block that enumerates both active and suppressed dimensions by name before roles activate. This satisfies C-34 at maximum structural rigor — compliance is column-verifiable, not read-the-prose. V-01–V-04 pass C-34 at baseline (structured header present) but the AMEND work is not separated from role activation.

---

### Phase 2 — Interdependency Table

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-16 | Standalone Phase 2 table present | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-17 | From/To columns typed by Risk ID | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-18 | Cascade effect cell populated per row | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-19 | ≥3 interdependency rows | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-32 | Trigger Condition is a named schema column (v11) | ✓ | ✓ | ✓ | ✓ | ✓ |

---

### Phase 2b — Diversity Audit

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-20 | Diversity audit is standalone (not embedded in Phase 1) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-21 | Per-dimension coverage check executed | ✓ | ✓ | ✓+ | ✓ | ✓+ |
| C-22 | Severity distribution assessed across LOW/MED/HIGH | ✓ | ✓ | ✓+ | ✓ | ✓+ |
| C-23 | Audit Step 3 present and isolated | ✓ | ✓ | ✓ | ✓ | ✓ |

**C-21/C-22 note**: V-03/V-05 HIGH-seed sub-phase means the diversity audit at Phase 2b is verifying coverage that was structurally seeded, not discovering gaps retrospectively. The audit's work becomes confirmation rather than repair — stronger pattern.

---

### Phase 3 — Competitive Landscape / Inertia

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-24 | Competitive profile section present | ✓ | ✓+ | ✓ | ✓+ | ✓+ |
| C-25 | Named competitors with ≥3 anatomy fields each | ✓ | ✓+ | ✓ | ✓+ | ✓+ |
| C-26 | Status quo / inertia modeled | ✓ | ✓+ | ✓ | ✓+ | ✓+ |
| C-27 | Competitor anatomy uses consistent schema | ✓ | ✓+ | ✓ | ✓+ | ✓+ |
| C-28 | Competitor-00 / inertia treated as first-class competitor | ✓ | ✓+ | ✓ | ✓+ | ✓+ |
| C-29 | Switching cost or lock-in risk addressed | ✓ | ✓+ | ✓ | ✓+ | ✓+ |
| C-30 | Adoption friction modeled | ✓ | ✓+ | ✓ | ✓+ | ✓+ |

**C-26–C-30 note**: V-02/V-04/V-05 introduce **Competitor-00** as a formal 9-column schema row for the status quo, adding `User-Adoption-Estimate`, `Switching-Cost`, and `Lock-in-Mechanism` as format-violation-enforced fields. Vague hedges fail enforcement. This pushes C-28/C-29/C-30 past what the rubric can currently discriminate — the spec probes v12 territory ("competitive depth" criterion). On v11, all three score PASS+ with super-criterion signal; the rubric does not penalize richness.

---

### Vocabulary Constraints

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-31 | Severity column uses exactly {LOW, MED, HIGH} | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-33 | Dimension column uses exactly {Technical, Market, Compliance, Dependency, Timeline} (v11) | ✓ | ✓ | ✓+ | ✓ | ✓+ |

**C-33 note**: V-03/V-05 HIGH-seed sub-phase requires the author to explicitly name a dimension for each seed row before expansion — vocabulary discipline is enforced at the seed-placement moment, not retrospectively corrected by audit.

---

### Role Protocol (R12 addition — V-01/V-04/V-05 only)

No rubric criterion directly scores role structure (a v12 probe), but role protocol bears on execution quality for several existing criteria:

| Criterion affected | V-01 | V-04 | V-05 |
|-------------------|------|------|------|
| C-08 (IF-THEN likelihood) | Challenge A specifically targets likelihood conditions | ✓+ | ✓+ | ✓+ |
| C-09/C-11 (typed mitigation + sub-fields) | Challenge B targets mitigation type accuracy | ✓+ | ✓+ | ✓+ |
| C-12/C-31 (severity vocabulary) | Challenge C targets severity calibration | ✓+ | ✓+ | ✓+ |
| C-25/C-28/C-29/C-30 (competitor anatomy) | Challenge C in V-04/V-05 targets the three new Competitor-00 fields | — | ✓+ | ✓+ |
| Repair loops (C-07 through C-19) | All four loops (A–D) owned by Audit Controller | ✓+ | ✓+ | ✓+ |

---

## Composite Scores

| Criterion | Points | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01–C-05 (Phase 0) | 20 | 20 | 20 | 20 | 20 | 20 |
| C-06 (dimension vocabulary) | 4 | 4 | 4 | 4 | 4 | 4 |
| C-07–C-14 (register structure) | 32 | 32 | 32 | 32 | 32 | 32 |
| C-15 (HIGH anchor per dimension) | 4 | **2** | **2** | **4** | **2** | **4** |
| C-10 + C-34 (AMEND) | 10 | 10 | 10 | 10 | 10 | 10 |
| C-16–C-19 (interdependency) | 16 | 16 | 16 | 16 | 16 | 16 |
| C-32 (Trigger Condition column) | 6 | 6 | 6 | 6 | 6 | 6 |
| C-20–C-23 (diversity audit) | 16 | 16 | 16 | 16 | 16 | 16 |
| C-24–C-30 (competitive landscape) | 28 | 28 | 28 | 28 | 28 | 28 |
| C-31 + C-33 (vocabulary) | 6 | 6 | 6 | 6 | 6 | 6 |
| **TOTAL** | **142** | **140** | **140** | **142** | **140** | **142** |

> **C-15 reasoning**: The rubric criterion for HIGH-per-dimension coverage awards full points only when the spec structurally guarantees the property. V-01/V-02/V-04 preserve baseline behavior where HIGH coverage is incidentally achieved and retrospectively audited (Phase 2b catches it). The spec for these variations does not enforce the guarantee at build time — Phase 2b repair is available but not blocked. V-03 and V-05 introduce the HIGH-seed sub-phase as a structural gate, converting the guarantee from incidental to necessary. Full 4 points awarded to V-03/V-05; 2 points (PARTIAL) for V-01/V-02/V-04.

---

## Variation Rankings

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 (tie) | **V-05** | **142/142** | All axes + Phase 0a + HIGH-seed + Competitor-00 + vocabulary AMEND — most comprehensive excellence profile |
| 1 (tie) | **V-03** | **142/142** | HIGH-seed sub-phase produces structural C-15/C-33 guarantee; simpler but achieves full score via the right structural constraint |
| 3 | **V-01** | 140/142 | Role protocol adds adversarial challenge excellence (C-08/C-09/C-12 PASS+) but C-15 remains incidental |
| 3 | **V-02** | 140/142 | Competitor-00 9-column anatomy pushes C-28–C-30 past rubric resolution; v12 probe confirmed — but C-15 incidental |
| 3 | **V-04** | 140/142 | Role + competitive inertia dual-axis: Devil's Advocate Challenge C targets richest anatomy, best adversarial precision — C-15 still incidental |

---

## Excellence Signals (from V-05, highest composite + richest profile)

**E-01 — Phase 0a as a structural firewall**
AMEND scope resolution is placed in a named sub-phase *before* any role or register work begins. This prevents scope contamination: no role can activate until the declared register boundary is column-verifiable. V-01–V-04 resolve AMEND inline or as a pre-condition note, not as a named sub-phase gate.

**E-02 — HIGH-seed sub-phase converts dimensional coverage from incidental to necessary**
Forcing one HIGH anchor per dimension before any expansion rows guarantees that Phase 2b diversity audit is confirmatory, not corrective. This structural guarantee is absent in V-01/V-02/V-04; their diversity audit can still fail to find a dimension with no HIGH and trigger repair — the guarantee is retrospective.

**E-03 — Three-role adversarial protocol structurally mandates challenge**
Risk Strategist (generate) → Devil's Advocate (challenge) → Audit Controller (gate) creates role-level ownership separation. Challenge is not incidental to quality gates; it is a named role's sole function. This pattern prevents "generate-and-audit" collapse where a single agent is both producer and verifier.

**E-04 — Cross-axis Devil's Advocate targeting at Challenge C**
In V-05, Devil's Advocate Challenge C specifically targets the three new Competitor-00 fields (`User-Adoption-Estimate`, `Switching-Cost`, `Lock-in-Mechanism`). The adversarial pressure is applied where the anatomical richness is greatest — the most likely location for soft hedges and format violations. Challenge specificity > Challenge generality.

**E-05 — Vocabulary-constrained AMEND header as column-verifiable compliance**
V-05's AMEND confirmation names suppressed dimensions in a structured header block with explicit enumeration, not prose. A reviewer does not need to read prose to confirm compliance; they scan the header columns. C-34 is satisfied at maximum structural resolution.

---

## v12 Probe Findings (informational, not scored)

V-02/V-04/V-05 reveal that **C-28/C-29/C-30 cannot discriminate between a 7-column and a 9-column Competitor-00 schema**. The rubric treats inertia as present/absent and vagueness-checked. A "competitive depth" criterion would be needed to capture:
- `User-Adoption-Estimate` as a format-violation-enforced field (not just populated)
- `Lock-in-Mechanism` requiring a named mechanism class, not behavioral description

This is the first round where inertia anatomy exceeds rubric resolution.

---

```json
{"top_score": 142, "all_essential_pass": true, "new_patterns": ["Phase 0a scope resolution as a named structural sub-phase before role activation creates a scope firewall — AMEND is column-verifiable before any register or challenge work begins", "HIGH-seed sub-phase (one HIGH anchor per dimension before expansion) converts per-dimension HIGH coverage from an incidentally achieved, audit-correctable property into a structurally guaranteed pre-condition — Phase 2b becomes confirmatory not corrective", "Three-role adversarial protocol (Risk Strategist → Devil's Advocate → Audit Controller) structurally mandates challenge as a named role function, preventing generate-and-audit collapse", "Cross-axis Challenge C: Devil's Advocate targeting is most valuable when aimed at the anatomy with the richest new fields — adversarial specificity beats adversarial generality"]}
```
