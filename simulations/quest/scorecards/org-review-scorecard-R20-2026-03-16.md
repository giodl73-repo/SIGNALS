# org-review — Quest Score: Round 20 (rubric v11)

## Scoring Basis

All five R20 variants inherit the V-05 R11 base (established as 210/225 in calibration), which passes C-09 through C-32 inclusive. R20 adds enforcement mechanisms for C-33, C-34, C-35 simultaneously.

---

## Per-Variation Scorecard

### C-01 through C-08 (shared baseline — all five identical)

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-01 Multi-voice Role Architecture | Named challenger + domain roles + bracket; no aggregation at collection time | PASS | 12 |
| C-02 Severity Commit-Gate Semantics | §1 DISPOSITION ALGEBRA: HIGH=blocks / MEDIUM=conditions / LOW=advisory; stated in preamble | PASS | 12 |
| C-03 Null Hypothesis Gate Before Domain | §3 NH DIMENSION COMPARISON TABLE at BRACKET OPENING; verdict before domain sections; distinct from domain findings | PASS | 12 |
| C-04 Commitment Disposition Emitted | §1 algebra produces READY/CONDITIONAL/BLOCKED labeled field; consistent with findings | PASS | 12 |
| C-05 Action Items Traceable | CH-ID registration + LOCAL GATE LEDGER + MASTER ACTION REGISTER; consolidated, not scattered | PASS | 12 |
| C-06 Artifact Scope Declared | SCOPE DECLARATION is step 1/2; declared before any reviewer section; OUT-OF-SCOPE surfaces named | PASS | 10 |
| C-07 Summary with Integrating Narrative | CROSS-ROLE SIGNALS (step 15): cross-role conflict/convergence, g_null progression all 3 stages, disposition explanation | PASS | 10 |
| C-08 Depth Parameter Honored | §19/§18/§20 INPUT VARIABLE CONTRACTS: deep/standard/quick behavior defined; acknowledgment block required | PASS | 10 |

**Essential + Recommended: 60 + 30 = 90 pts for all five.**

---

### C-09 through C-32 (aspirational baseline — all five identical, inherited from V-05 R11)

All criteria pass per the established R11 calibration (V-05 R11 = 210/225, proving C-09–C-32 all PASS). R20 adds no changes that break any of these. Summary table:

| Criteria | Notes | Verdict |
|----------|-------|---------|
| C-09 Adversarial Bracket | BRACKET OPENING + BRACKET CLOSING with override authority; two distinct challenger sections | PASS |
| C-10 Disposition Algebra Pre-committed | §1 formula covers all gate-verdict combinations in preamble | PASS |
| C-11 Override as Labeled Field | OVERRIDE INVOKED: YES\|NO in BRACKET CLOSING | PASS |
| C-12 Class Derived Mechanically | §2 CLASS DERIVATION CONTRACT: FAIL→BLOCKED / CONDITIONAL→CONDITIONAL / PASS→ADVISORY | PASS |
| C-13 Prompt Inputs as Template Variables | {{artifact\_id}}, {{depth}}, {{reviewer\_set}} declared; acknowledgment block required | PASS |
| C-14 Gate Verdict in Action Register | LOCAL GATE LEDGER ROWS carry Gate Verdict column; verbatim-copied to MASTER ACTION REGISTER | PASS |
| C-15 Reviewer Set Injectable | {{reviewer\_set}} template variable; overrides depth-based selection when non-auto | PASS |
| C-16 Alternatives Table as Bracket Anchor | NH DIMENSION COMPARISON TABLE at bracket opening; bracket closing re-populates B/C; g\_null derivable from table alone | PASS |
| C-17 All Three Contracts in Preamble | §1 DISPOSITION + §2 CLASS DERIVATION + §3 NH DERIVATION RULE all in preamble | PASS |
| C-18 Inline Gate Ledger at Origin | LOCAL GATE LEDGER ROW at end of every verdict-emitting section (bracket, domain, lifecycle) | PASS |
| C-19 Gate Ledger Protocol Pre-committed | §5 LOCAL GATE LEDGER PROTOCOL: syntax, timing, assembly rule all in preamble | PASS |
| C-20 Verbatim Assembly Prohibition | §6 VERBATIM ASSEMBLY PROHIBITION: copy only, re-derivation prohibited, local row is authority | PASS |
| C-21 Universal Gate Ledger Coverage | §5 names all archetypes: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING | PASS |
| C-22 Lifecycle Verdict Integration | LIFECYCLE (step 7/8) precedes BRACKET CLOSING (step 8/9); g\_lifecycle as labeled input | PASS |
| C-23 Multi-alternative NH Coverage | Three alternatives (A/B/C); derivation rule covers both Delta B-A and Delta B-C | PASS |
| C-24 Domain-Aggregate Formula | §14/§13/§15 G\_domain\_agg = median(DOMAIN verdicts); labeled input to BRACKET CLOSING | PASS |
| C-25 Non-verdict Section Excluded | §7 explicitly names excluded sections (SCOPE DECLARATION, PRE-REGISTRATION, CH-ID REG TABLE, etc.) | PASS |
| C-26 Section Order Contract | §8 SECTION ORDER CONTRACT [immutable]; 14-step sequence named; reordering is violation | PASS |
| C-27 CH-ID Saturation Pre-committed | §12/§11/§13 SATURATED + FULLY SATURATED tiers; CH-ID SATURATION CHECK section; BRACKET CLOSING blocked on UNSATURATED | PASS |
| C-28 NH Progression Formula 3-stage | §4 NULL HYPOTHESIS PROGRESSION CONTRACT: g\_null(initial)→g\_null(post-domain)→g\_null(final) derivation chain | PASS |
| C-29 Scope-to-Finding Coverage Gate | §16/§15/§17 SCOPE COVERAGE GATE PROTOCOL; post-BRACKET CLOSING reconciliation; ADVISORY-GAP for gaps | PASS |
| C-30 Per-Finding Severity Chain | §17/§16/§18 [IMMUTABLE]: Section Severity = worst(individual finding severities); no editorial assignment | PASS |
| C-31 Role Lens Exhaustion Pre-committed | §15/§14/§16 [IMMUTABLE] LENS COVERAGE TABLE with ADDRESSED/OPEN; OPEN → ADVISORY-OPEN-LENS | PASS |
| C-32 Primary Driver Derivation | §18/§17/§19 [IMMUTABLE]: 7-rule precedence formula; Primary Driver as labeled field at DISPOSITION | PASS |

**C-09 through C-32: 24 × 5 = 120 pts for all five.**

---

### C-33, C-34, C-35 — The Three R20-Differentiating Criteria

#### C-33 — Lens Applicability Rating Pre-committed (5 pts)

Pass condition: LENS COVERAGE TABLE rows carry explicit artifact-specific applicability rating; preamble states applicability determines coverage expectations.

| Variant | C-33 Mechanism | Verdict |
|---------|---------------|---------|
| V-01 | §9 LENS APPLICABILITY PRE-REGISTRATION [IMMUTABLE] + §10 APPLICABILITY INHERITANCE PROTOCOL: verbatim-copy from PRE-REGISTRATION; INHERITANCE-DEVIATION-ALERT for deviation; silent recalculation named as chain-of-custody error | **PASS** |
| V-02 | §10 LENS APPLICABILITY PRE-REGISTRATION [IMMUTABLE]: artifact-specific HIGH/MEDIUM/LOW; LENS COVERAGE TABLE "inherits these values"; HIGH governs ADVISORY-OPEN-LENS promotion | **PASS** |
| V-03 | §9 LENS APPLICABILITY PRE-REGISTRATION [IMMUTABLE]: artifact-specific; immutable after pre-registration; LENS COVERAGE TABLE inherits | **PASS** |
| V-04 | §10 PRE-REGISTRATION + §11 APPLICABILITY INHERITANCE PROTOCOL (verbatim-copy; INHERITANCE-DEVIATION-ALERT; silent recalculation named as error) — same strength as V-01 | **PASS** |
| V-05 | §10 + §11 identical to V-04; three-axis combination | **PASS** |

**Differentiator**: V-01/V-04/V-05 add the APPLICABILITY INHERITANCE PROTOCOL (§10/§11) with named INHERITANCE-DEVIATION-ALERT alert syntax, prohibiting silent recalculation. V-02/V-03 satisfy C-33 via PRE-REGISTRATION + "inherits" statement only — no chain-of-custody protection against silent re-derivation. Both approaches satisfy the rubric's pass condition; only V-01/V-04/V-05 are adversarially robust against the R20 target failure mode.

---

#### C-34 — ADVISORY-GAP Domain Coverage Pre-committed (5 pts)

Pass condition: domain gap-check pre-committed in preamble; identifies domains with no HIGH-applicability reviewer; ADVISORY-GAP classification; action register promotion.

| Variant | C-34 Mechanism | Verdict |
|---------|---------------|---------|
| V-01 | §15 ROLE LENS EXHAUSTION [IMMUTABLE]: "enumerate every artifact domain from the SCOPE DECLARATION"; gap-check in ORDER CONTRACT step 11; ADVISORY-GAP → MASTER ACTION REGISTER; pre-committed | **PASS** |
| V-02 | §9 SCOPE-DECLARATION DOMAIN ANNOTATION [IMMUTABLE]: domain tags at declaration time; §15 gap-check reads "unique Domain values from step 1 scope table as sole input"; UNDECLARED-DOMAIN flag for findings-derived domains | **PASS** |
| V-03 | §14 [IMMUTABLE]: "enumerate artifact domains from SCOPE DECLARATION; check HIGH Applicability per domain; ADVISORY-GAP"; pre-committed in ORDER CONTRACT | **PASS** |
| V-04 | §9 scope-declaration domain annotation + §16 reads "unique domain values from step 1 scope table" — same strength as V-02 | **PASS** |
| V-05 | §9 + §16 identical to V-04; UNDECLARED-DOMAIN flag | **PASS** |

**Differentiator**: V-02/V-04/V-05 add scope-declaration domain annotation (domain tags committed at step 1) and the UNDECLARED-DOMAIN flag for findings-derived domains. V-01/V-03 reference "from SCOPE DECLARATION" without tagging domains at declaration time — the domain set is committed by reference but not structurally anchored. Both satisfy C-34's pass condition; only V-02/V-04/V-05 close the R20 domain-drift failure mode.

---

#### C-35 — Null Hypothesis Challenger Dimension Comparison Table (5 pts)

Pass condition: structured dimension comparison table; >= 2 dimensions; current-state and proposed-state scores per dimension; per-dimension differentials; g_null derivable from table alone; table before domain sections.

| Variant | C-35 Mechanism | Verdict |
|---------|---------------|---------|
| V-01 | §3: NH DIMENSION COMPARISON TABLE (3+ dimensions, A/B/C, Delta B-A/B-C); g\_null formula; PRIMACY DEVIATION CASE (table governs prose); table at BRACKET OPENING | **PASS** |
| V-02 | §3: same as V-01; PRIMACY DEVIATION CASE | **PASS** |
| V-03 | §3: Two-phase construction — Phase 1 DIMENSION REGISTRY (dimension + measurement basis + scale; immutable); Phase 2 VALUE ASSIGNMENT (A/B/C scores + deltas); CONSTRUCTION DEVIATION CASE; PRIMACY DEVIATION CASE | **PASS** |
| V-04 | §3: same as V-01/V-02; PRIMACY DEVIATION CASE only | **PASS** |
| V-05 | §3: Two-phase construction identical to V-03; CONSTRUCTION DEVIATION CASE + PRIMACY DEVIATION CASE | **PASS** |

**Differentiator**: V-03/V-05 add two-phase construction (Phase 1 DIMENSION REGISTRY as immutable scaffold before Phase 2 VALUE ASSIGNMENT) and the CONSTRUCTION DEVIATION CASE. V-01/V-02/V-04 satisfy C-35 via the three-alternative table format + PRIMACY DEVIATION CASE, but the construction order is not pre-committed — back-filling dimensions after prose intent is not prohibited. Both approaches satisfy C-35's pass condition; only V-03/V-05 close the R20 back-fill failure mode.

---

## Composite Scores

| Variant | Essential | Recommended | C-09–C-32 | C-33 | C-34 | C-35 | **Total** |
|---------|-----------|-------------|-----------|------|------|------|-----------|
| V-01 | 60 | 30 | 120 | 5 | 5 | 5 | **225** |
| V-02 | 60 | 30 | 120 | 5 | 5 | 5 | **225** |
| V-03 | 60 | 30 | 120 | 5 | 5 | 5 | **225** |
| V-04 | 60 | 30 | 120 | 5 | 5 | 5 | **225** |
| V-05 | 60 | 30 | 120 | 5 | 5 | 5 | **225** |

All five: **225/225 — Gold band (all essential PASS, score >= 190).**

---

## Ranking by Structural Robustness (adversarial failure mode closure)

| Rank | Variant | C-33 Failure Mode Closed? | C-34 Failure Mode Closed? | C-35 Failure Mode Closed? |
|------|---------|--------------------------|--------------------------|--------------------------|
| 1 | **V-05** | YES — INHERITANCE PROTOCOL + INHERITANCE-DEVIATION-ALERT | YES — scope-declaration anchor + UNDECLARED-DOMAIN | YES — two-phase construction + CONSTRUCTION DEVIATION CASE |
| 2 | V-04 | YES — INHERITANCE PROTOCOL | YES — scope-declaration anchor | NO — PRIMACY DEVIATION CASE only |
| 3 | V-01 | YES — INHERITANCE PROTOCOL | NO — reference-only, no domain tags | NO — PRIMACY DEVIATION CASE only |
| 4 | V-02 | NO — "inherits" only, no alert syntax | YES — scope-declaration anchor | NO — PRIMACY DEVIATION CASE only |
| 5 | V-03 | NO — "inherits" only, no alert syntax | NO — reference-only, no domain tags | YES — two-phase construction |

V-05 is the top variant: only V-05 simultaneously closes all three R20 adversarial failure modes with structural protocols rather than behavioral mandates.

---

## Excellence Signals (from V-05)

### Signal 1: INHERITANCE-DEVIATION-ALERT chain-of-custody syntax
The Applicability column's verbatim-copy discipline is enforced by a named deviation alert (`INHERITANCE-DEVIATION-ALERT: Role=[r] / Dimension=[d] / Pre-Registered=[X] / Attempted=[Y] / Justification=[z]`), directly analogous to §7 VERBATIM ASSEMBLY PROHIBITION for gate ledger rows. Silent recalculation is explicitly named as a chain-of-custody error at the same severity as re-deriving a gate verdict. This closes the "inherits-but-actually-recalculates" failure mode.

### Signal 2: Scope-declaration domain annotation as read-only gap-check source
Domain tags are committed at SCOPE DECLARATION time (step 1 extended schema: `| Surface | Domain | In/Out of Scope | Note |`). The DOMAIN COVERAGE GAP-CHECK reads "unique Domain values from step 1 scope table as its sole input set." The UNDECLARED-DOMAIN flag handles domains appearing in reviewer findings but absent from step 1 — they are flagged in CROSS-ROLE SIGNALS but do not retroactively expand the gap-check input set. Commits the domain universe before any review evidence exists.

### Signal 3: Two-phase NH table construction with immutable Phase 1
Phase 1 DIMENSION REGISTRY (`| # | Dimension | Measurement Basis | Scale |`) must be complete before any scores are assigned. No dimensions may be added, removed, or renamed in Phase 2. This prevents the challenger from discovering the dimensions after forming prose intent — the measurement basis is locked before it can be rationalized. Phase 2 VALUE ASSIGNMENT is constrained to the committed scaffold.

### Signal 4: CONSTRUCTION DEVIATION CASE escape hatch
When Phase 2 values reveal a Phase 1 dimension was poorly specified, the challenger emits `NH-CONSTRUCTION-DEVIATION: Dimension=[d] / Phase-1-basis=[original] / Issue=[issue] / Proposed-revision=[revision]`. Phase 1 authority is maintained unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES. This pattern preserves Phase 1 immutability while providing a documented escape — the same strategy as INHERITANCE-DEVIATION-ALERT and §7 VERBATIM ASSEMBLY PROHIBITION in prior rounds.

### Signal 5: Three orthogonal chain-of-custody protocols
V-05 explicitly notes that §9 (domain source), §10/§11 (applicability inheritance), and §3 (NH construction) are orthogonal with no interaction points. Each protocol closes exactly one failure mode; they do not interact. This multi-axis orthogonality design — closing independent failure modes with independent protocols — is the structural pattern that enables 225/225 robustness. Prior rounds discovered this with C-17/C-19/C-24 (contractual contracts for the three algebraic layers); R20 extends it to the chain-of-custody layer.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["INHERITANCE-DEVIATION-ALERT chain-of-custody syntax prohibits silent Applicability recalculation at LENS COVERAGE TABLE time", "Scope-declaration domain annotation as read-only gap-check source with UNDECLARED-DOMAIN flag for post-review domain drift", "Two-phase NH table construction: Phase 1 DIMENSION REGISTRY (dimension name + measurement basis + scale) immutable before Phase 2 VALUE ASSIGNMENT prevents back-fill", "CONSTRUCTION DEVIATION CASE escape hatch maintains Phase 1 authority while providing documented revision path", "Three orthogonal chain-of-custody protocols (applicability inheritance, domain anchor, NH construction) each close independent failure modes with no interaction points"]}
```
