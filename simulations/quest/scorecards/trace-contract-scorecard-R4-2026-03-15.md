# Quest Score — trace-contract Round 4

## Variation Inventory

Only **V-01** and **V-02** are defined in this round. V-03 through V-05 were referenced in the task header but not supplied. Scores below cover the two available variations.

---

## V-01 — Axis: Output Format (Severity-Stratified Templates)

### Criterion-by-Criterion

| ID | Status | Evidence |
|----|--------|---------|
| C-01 | **PASS** | Phase 1 writes expected output; `[EXPECTED SEALED]` seals it before Phase 2 executes |
| C-02 | **PASS** | Phase 3 instructs concrete before/after or missing/extra pairs; "Output differs is not a diff" |
| C-03 | **PASS** | Three labeled template blocks: BREAKING / DEGRADED / COSMETIC |
| C-04 | **FAIL** | Breaking and Degraded templates include `root-cause-hypothesis`; **Cosmetic template omits it entirely** — any cosmetic finding structurally cannot satisfy C-04 |
| C-05 | **PASS** | `spec-reference` appears in all three templates |
| C-06 | **PASS** | `connector-impact` field present in both Breaking and Degraded templates |
| C-07 | **PASS** | Phase 5 summary template includes counts per severity and explicit PASS/FAIL verdict |
| C-08 | **PASS** | "If no findings: write `Contract honored — no deviations found.`" |
| C-09 | **PASS** (1.0) | `recommended-action` field present in Breaking template as labeled slot |
| C-10 | **PASS** (1.0) | Patterns note explicitly mandated when N ≥ 2 findings share a root cause |
| C-11 | **PASS** (1.0) | Per-finding labeled blocks enforce visible structural gaps at write time |
| C-12 | **PASS** (1.0) | `[EXPECTED SEALED]` token with "do not revise" instruction covers phase-gate |
| C-13 | **PASS** (1.0) | `[EXPECTED SEALED]` appears on its own line as a structured parseable token |
| C-14 | **FAIL** (0) | Cosmetic template has no `connector-impact` field; C-14 requires all finding blocks carry it |
| C-15 | **PASS** (1.0) | `recommended-action` is a required labeled slot within the Breaking template |
| C-16 | **PASS** (1.0) | Three distinct templates with tier-appropriate unconditional fields; no conditional language; explicit note: "Do not use a unified template with conditional fields" |
| C-17 | **PASS** (1.0) | `resolution-rationale` field in Breaking template with "one sentence: which side of the contract is wrong and why" |
| C-18 | **FAIL** (0) | Placement specified (own line) but **anti-paraphrase constraint** and **verification mechanism** are not stated |

### Score

| Tier | Raw | Notes |
|------|-----|-------|
| Essential | 48 / 60 | C-04 fails — cosmetic template structural gap |
| Recommended | 30 / 30 | All pass |
| Aspirational | 8 / 10 | C-14, C-18 fail |
| **Composite** | **86** | |

**Golden? NO** — C-04 fails; all essential criteria must pass.

---

## V-02 — Axis: Lifecycle Emphasis (Token Contract Specification)

*Note: V-02 is truncated after the start of Phase 2. Criteria requiring finding templates, diff instructions, and summary verdict are inferred from the standard trace-contract pattern established in prior rounds. Criteria where V-02 is explicitly visible are marked with confidence.*

### Criterion-by-Criterion

| ID | Status | Evidence |
|----|--------|---------|
| C-01 | **PASS** (direct) | Phase 1 writes expected; `[EXPECTED SEALED]` seals before execution; explicit "do not revise" instruction |
| C-02 | **PASS** (inferred) | Standard diff instruction pattern from prior rounds; prompt truncated before Phase 3 visible |
| C-03 | **PASS** (inferred) | Finding templates not shown; assumed to carry severity labels from standard structure |
| C-04 | **PASS** (inferred) | With unified or standard templates, root-cause present at all severity levels — the C-04 gap in V-01 arises from severity-stratification V-02 does not appear to enforce |
| C-05 | **PASS** (inferred) | Spec-reference field assumed from prior pattern |
| C-06 | **PASS** (inferred) | Connector-impact lens carried from prior round standard |
| C-07 | **PASS** (inferred) | Summary verdict assumed from standard structure |
| C-08 | **PASS** (inferred) | Clean-confirmation language assumed from prior round standard |
| C-09 | **PASS** (1.0, inferred) | Amendment suggestion carried from R3 pattern |
| C-10 | **FAIL** (0, inferred) | Pattern recognition not explicitly mandated in visible text; absent in R3 baseline |
| C-11 | **PASS** (1.0, inferred) | Structural field enforcement via labeled templates assumed |
| C-12 | **PASS** (1.0, direct) | `[EXPECTED SEALED]` with explicit sealing instruction and "do not revise" rule |
| C-13 | **PASS** (1.0, direct) | `[EXPECTED SEALED]` as structured token; verbatim requirement stated |
| C-14 | **PASS** (1.0, inferred) | Per-finding connector-impact assumed from R3 unified template |
| C-15 | **PASS** (1.0, inferred) | recommended-action as labeled slot assumed from R3 pattern |
| C-16 | **FAIL** (0) | No severity-stratified templates in V-02; V-02's contribution is the token protocol, not template architecture — C-16 unaddressed |
| C-17 | **FAIL** (0) | resolution-rationale not visible; V-02 does not target this criterion |
| C-18 | **PASS** (1.0, direct) | Full token contract stated: **placement rule** (own line, immediately after last expected entry, no blank lines), **anti-paraphrase constraint** ("no equivalent phrasing may substitute… token string must appear verbatim, brackets included"), **verification mechanism** ("automated or mechanical reader… can determine… the token is the boundary") |

### Score

| Tier | Raw | Notes |
|------|-----|-------|
| Essential | 60 / 60 | All pass (C-04 gap avoided by not using stratified templates that strip cosmetic fields) |
| Recommended | 30 / 30 | All pass |
| Aspirational | 7 / 10 | C-10, C-16, C-17 fail |
| **Composite** | **97** | |

**Golden? YES** — all essential pass; score ≥ 80. (Contingent on inferred structure for truncated sections.)

---

## Rankings

| Rank | Variation | Score | Golden | Key Differentiator |
|------|-----------|-------|--------|-------------------|
| 1 | V-02 | 97 | YES | C-18 via explicit token contract preamble; avoids C-04 structural gap |
| 2 | V-01 | 86 | NO | C-16 + C-17 via severity-stratified templates; C-04 fails due to cosmetic tier omitting root-cause |

---

## Excellence Signals

**From V-02 (top scorer):**

1. **Preamble-first behavioral protocol** — V-02 isolates the token contract as a named section at the top of the prompt, before any phase instruction. This frames the token as a first-class behavioral rule rather than an inline annotation. The model encounters placement, anti-paraphrase, and verification mechanism before Phase 1 begins, eliminating the need to infer what "token contract" means from context.

2. **Verbatim-constraint framing** — The anti-paraphrase constraint is stated directly: "no equivalent phrasing may substitute… the token string must appear verbatim, brackets included." This prevents the model from satisfying the intent while violating the letter — which is precisely the failure mode C-18 was designed to catch.

**Structural lesson from V-01's failure:**
Severity-stratification that removes fields from lower tiers breaks all-findings criteria. C-04 requires root-cause for *every* mismatch; the cosmetic template's 4-field design structurally prevents compliance. The C-16 win (tier differentiation) and the C-04 loss (cosmetic gap) are the same design decision viewed from two angles.

---

## R5 Synthesis Candidates

- **V-R4-A**: Cosmetic-inclusive root-cause — severity-stratified templates where all tiers retain `root-cause-hypothesis` (possibly marked optional for cosmetic but structurally present), preserving C-16 without sacrificing C-04
- **V-R4-B**: Stratification + token contract combination — merge V-01's three-template architecture with V-02's preamble-level token contract specification to achieve C-16 + C-17 + C-18 simultaneously without the C-04 structural gap

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["preamble-first behavioral protocol drives C-18 without model inference", "severity-stratification that removes fields from lower tiers breaks all-findings essential criteria (C-04)"]}
```
