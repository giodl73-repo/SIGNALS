Now I have all five variations. Let me perform the full rubric evaluation.

---

# flow-ratelimit — Quest Score R14

**Rubric:** v14 (C-01 through C-35, 27 aspirational) | **Scoring denominator:** /27 aspirational

---

## Baseline Assessment

All five variations are built on the R12 V-05 baseline, which passed C-01 through C-33 under v14. The only open criteria are C-34 and C-35. Per the dependency rule (C-35 requires C-34), a C-34 failure renders C-35 N/A without a second penalty — so each failing variation loses exactly one criterion position.

---

## C-34 and C-35 Evidence Per Variation

### V-01 — Role sequence (R12 V-05 baseline carry, no NMI)

**C-34 — Three explicit behavioral declarations in check (a):**
Check (a) reads: *"This check is pure verification — Role 9 has already inserted all missing markers."*
- Declaration (i) VERIFICATION-ONLY: implied by "pure verification" — not explicitly labeled
- Declaration (ii) no REVISED insertion: inferred from "Role 9 has already inserted" — not stated
- Declaration (iii) zero count: **absent** — not stated in any form

VERDICT: **FAIL** — zero-count declaration absent; none of the three declarations are explicitly produced as distinct named items.

**C-35 — Named pre-terminal non-modification invariant:**
No NMI section exists anywhere in the document. C-34 also fails.

VERDICT: **N/A** (C-34 dependency unmet)

---

### V-02 — NMI inside Role 10 body

**C-34 — Three explicit behavioral declarations in check (a):**
Check (a) is labeled "NMI-01 COMPLIANCE CONFIRMATION" and contains:
- Behavioral declaration (i): "This role is in VERIFICATION-ONLY mode." — **explicit**
- Behavioral declaration (ii): "This role does not insert REVISED markers." — **explicit**
- Behavioral declaration (iii): "REVISED marker insertion count for this role: zero." — **explicit**

VERDICT: **PASS** — all three declarations produced from within reconciler body, explicitly labeled.

**C-35 — Named pre-terminal non-modification invariant:**
The NMI-01 block appears at lines 390–394, after the `## ROLE 10 — TERMINAL RECONCILER` header. Structure:

```
## ROLE 10 — TERMINAL RECONCILER
[gate language]
**FORMAL NON-MODIFICATION INVARIANT — NMI-01**   ← inside Role 10 body
```

C-35 pass condition states: *"An invariant declared inside the reconciler body... does not pass."* Despite the NMI-01 block having all four required content components and check (a) referencing it by name, the structural position is disqualifying.

VERDICT: **FAIL** — invariant declared inside Role 10 body, not before it opens.

---

### V-03 — Standalone NMI section, no name reference in check (a)

**C-34 — Three explicit behavioral declarations in check (a):**
Check (a) reads: *"This check is pure verification — Role 9 has already inserted all missing markers."* Identical to V-01: no explicit declarations, zero-count absent.

VERDICT: **FAIL** — zero-count declaration absent; three declarations remain implicit.

**C-35 — Named pre-terminal non-modification invariant:**
A standalone `## PRE-TERMINAL INVARIANT — NMI-01` section appears between Role 9 and Role 10 — correctly positioned. The NMI-01 block has all four required components. Gate 9→PRE-TERMINAL INVARIANT requires the block. Gate PRE-TERMINAL INVARIANT → Role 10 confirms it.

However, check (a) inside Role 10 says only *"This check is pure verification — Role 9 has already inserted all missing markers."* — no reference to "NMI-01" by name.

C-35 pass condition: *"The reconciler's check (a) must reference the invariant by its declared name."*

VERDICT: **N/A** (C-34 fails; even if assessed independently, C-35 fails — check (a) does not name NMI-01).

---

### V-04 — Standalone NMI + explicit three declarations + name reference

**C-34 — Three explicit behavioral declarations in check (a):**
Check (a) is labeled "NMI-01 COMPLIANCE CONFIRMATION" and contains:
- Behavioral declaration (i): "This role is in VERIFICATION-ONLY mode." — **explicit**
- Behavioral declaration (ii): "This role does not insert REVISED markers." — **explicit**
- Behavioral declaration (iii): "REVISED marker insertion count for this role: zero." — **explicit**

VERDICT: **PASS**

**C-35 — Named pre-terminal non-modification invariant:**
`## PRE-TERMINAL INVARIANT — NMI-01` is a standalone section between Role 9 and Role 10 — structurally before Role 10 opens. NMI-01 block has all four components:
- (a) self-named: "this block is NMI-01, the Pre-Terminal Non-Modification Invariant" ✓
- (b) non-modification: "Role 10 does not insert REVISED markers" ✓
- (c) zero count: "count of REVISED markers inserted by Role 10 is zero" ✓
- (d) violation condition by invariant name: "NMI-01 VIOLATION" ✓

Check (a) inside Role 10: *"Referencing NMI-01: the three declarations above confirm compliance with the pre-declared constraint NMI-01."* — references NMI-01 by declared name ✓

Gate PRE-TERMINAL INVARIANT → Role 10: gates on all four NMI components being complete.

VERDICT: **PASS**

---

### V-05 — Full integration (V-04 + explicit "deferred from Role N — [reason]" annotation + NMI-01 in gate name)

**C-34:** Identical check (a) structure to V-04. All three explicit declarations present. **PASS**

**C-35:** Identical NMI-01 standalone section and check (a) name reference as V-04. Additionally:
- Gate 9→PRE-TERMINAL INVARIANT is named "Gate 9→PRE-TERMINAL INVARIANT (NMI-01)" — NMI-01 identified as a deliverable by identifier in the gate transition itself
- Role 10's gate-in condition: "NMI-01 block confirmed complete per Gate PRE-TERMINAL INVARIANT → Role 10"
- The NMI-01 block explicitly notes: *"It is a structural antecedent: the constraint is named here so that the reconciler's check (a) confirms compliance with a pre-declared rule rather than issuing its own claim."*

VERDICT: **PASS** (meets all C-35 pass conditions; adds auditability beyond minimum)

---

## Full Criterion Scorecard

### Essential (C-01–C-05) — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Throttle tier classification | PASS | PASS | PASS | PASS | PASS |
| C-02 Multi-limit architecture | PASS | PASS | PASS | PASS | PASS |
| C-03 Observable UX per throttle tier | PASS | PASS | PASS | PASS | PASS |
| C-04 Unprotected burst path | PASS | PASS | PASS | PASS | PASS |
| C-05 Retry-After handling gap | PASS | PASS | PASS | PASS | PASS |

Essential score: **5/5** all variations.

### Recommended (C-06–C-08) — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Cascading throttle scenario | PASS | PASS | PASS | PASS | PASS |
| C-07 Numeric rate limit specificity | PASS | PASS | PASS | PASS | PASS |
| C-08 Volume-to-behavior mapping | PASS | PASS | PASS | PASS | PASS |

Recommended score: **3/3** all variations.

### Aspirational (C-09–C-35) — Key criteria (C-09 through C-33 PASS all; differentiating criteria shown)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 Per-bottleneck mitigations | PASS | PASS | PASS | PASS | PASS |
| C-10 Quantified impact at load spike | PASS | PASS | PASS | PASS | PASS |
| C-11 Burst gap classification | PASS | PASS | PASS | PASS | PASS |
| C-12 Dual-state volume mapping | PASS | PASS | PASS | PASS | PASS |
| C-13 Verdict-before-evidence | PASS | PASS | PASS | PASS | PASS |
| C-14 Baseline-delta mitigation | PASS | PASS | PASS | PASS | PASS |
| C-15 Document-head global Verdict | PASS | PASS | PASS | PASS | PASS |
| C-16 Format Contract Preamble | PASS | PASS | PASS | PASS | PASS |
| C-17 Cascading section gate enforcement | PASS | PASS | PASS | PASS | PASS |
| C-18 Bidirectional Verdict revision marking | PASS | PASS | PASS | PASS | PASS |
| C-19 Four-field UX tier template | PASS | PASS | PASS | PASS | PASS |
| C-20 Arithmetic trace explicitness | PASS | PASS | PASS | PASS | PASS |
| C-21 Full gate chain closure | PASS | PASS | PASS | PASS | PASS |
| C-22 Gate-checkpoint Verdict currency | PASS | PASS | PASS | PASS | PASS |
| C-23 Schema-column arithmetic enforcement | PASS | PASS | PASS | PASS | PASS |
| C-24 Terminal Document-Close Reconciler | PASS | PASS | PASS | PASS | PASS |
| C-25 Two-tier violation taxonomy | PASS | PASS | PASS | PASS | PASS |
| C-26 Explicit UX Role gated four-field | PASS | PASS | PASS | PASS | PASS |
| C-27 UX Template as Named Schema | PASS | PASS | PASS | PASS | PASS |
| C-28 UX Completeness as Named Verdict Claim | PASS | PASS | PASS | PASS | PASS |
| C-29 Six-item UX gate | PASS | PASS | PASS | PASS | PASS |
| C-30 Schema B Content Rejection Clause | PASS | PASS | PASS | PASS | PASS |
| C-31 Gate item (e) analytical independence | PASS | PASS | PASS | PASS | PASS |
| C-32 *(prior round)* | PASS | PASS | PASS | PASS | PASS |
| C-33 *(prior round)* | PASS | PASS | PASS | PASS | PASS |
| **C-34 Three behavioral declarations** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-35 Named pre-terminal invariant** | **N/A** | **FAIL** | **N/A** | **PASS** | **PASS** |

*C-35 marked N/A for V-01 and V-03 because C-34 dependency fails. Dependency failure counted as single criterion loss per dependency chain.*

---

## Composite Score Calculation

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 27 * 30)
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 = 60 | 3/3 = 30 | 26/27 = 28.89 | **118.89** |
| V-02 | 5/5 = 60 | 3/3 = 30 | 26/27 = 28.89 | **118.89** |
| V-03 | 5/5 = 60 | 3/3 = 30 | 26/27 = 28.89 | **118.89** |
| V-04 | 5/5 = 60 | 3/3 = 30 | 27/27 = 30.00 | **120.00** |
| V-05 | 5/5 = 60 | 3/3 = 30 | 27/27 = 30.00 | **120.00** |

*V-01 and V-03 lose C-34; C-35 is N/A (dependency blocked — counts as one position lost). V-02 passes C-34 but fails C-35 — also one position lost.*

---

## Ranking

| Rank | Variation | Score | Delta |
|------|-----------|-------|-------|
| 1 (tied) | **V-04** | 120/120 | — |
| 1 (tied) | **V-05** | 120/120 | — |
| 3 (tied) | V-01 | 118.89 | -1.11 |
| 3 (tied) | V-02 | 118.89 | -1.11 |
| 3 (tied) | V-03 | 118.89 | -1.11 |

**V-04 and V-05 are the recommended variations.** V-05 is the stronger canonical form for production use due to explicit deferred-marker annotation format and NMI-01 named in gate identifiers, though neither difference affects the rubric score.

---

## Single-Axis Question Answers

**Q1 (V-01 vs V-02): Do explicit three declarations satisfy C-34 without any NMI?**
**Confirmed YES.** V-02 passes C-34 purely via three explicitly labeled behavioral declarations in check (a), with no correctly-positioned NMI required. C-34 is about the reconciler body producing explicit declarations — NMI position is orthogonal.

**Q2 (V-02 vs V-04): Does NMI position alone determine C-35 compliance regardless of declaration quality?**
**Confirmed YES.** V-02 has perfect NMI content and correct name reference in check (a), but fails C-35 solely because the NMI-01 block appears after the "## ROLE 10" header. Structural position is the only differentiator.

**Q3 (V-03 vs V-04): Does absent NMI name reference in check (a) alone cause C-35 failure when NMI is correctly positioned?**
**Confirmed YES** (though moot for V-03 since C-34 also fails). V-03 has correct NMI position and all four content components, but check (a) does not say "NMI-01" — it says "pure verification only." The pass condition requires name reference; V-03 fails on that requirement alone.

---

## Excellence Signals

**V-04/V-05 patterns that produced 120/120:**

**Signal 1 — Two-phase invariant declaration pattern (C-35):**
The NMI is split into two structurally separated acts: (1) declaration phase — a standalone section before the reconciler header that names the constraint and its violation condition, and (2) conformance phase — check (a) inside the reconciler that references the pre-declared constraint by name rather than asserting its own claim. This converts check (a) from a self-referential behavioral declaration ("I am in verification mode") into a compliance confirmation against an externally declared rule ("I confirm compliance with NMI-01"). An outside evaluator can inspect the constraint without reading the reconciler body.

**Signal 2 — NMI as named gate deliverable (V-05):**
Gate 9→PRE-TERMINAL INVARIANT (NMI-01) names NMI-01 as a required deliverable by identifier in the gate condition itself. This makes the NMI a first-class artifact that C-24's check (b) — which audits all gated transitions — automatically verifies. The NMI block cannot be silently omitted; its absence would be flagged during the gate deliverable audit without requiring a dedicated NMI-specific reconciler check.

**Signal 3 — Explicit structural antecedent framing (V-05):**
V-05's NMI-01 block includes a prose declaration: *"It is a structural antecedent: the constraint is named here so that the reconciler's check (a) confirms compliance with a pre-declared rule rather than issuing its own claim."* This language makes the pattern's purpose explicit rather than leaving it implicit in the structural layout. Evaluators scanning for C-35 compliance can identify the two-phase pattern without reconstructing it from position analysis.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Two-phase invariant declaration: pre-declare constraint in standalone section before reconciler header so check (a) confirms compliance with an external rule rather than self-asserting verification mode", "NMI as named gate deliverable: naming the invariant by identifier in the gate transition makes it auditable by the terminal reconciler's gate deliverable check without a dedicated NMI-specific reconciler check"]}
```
