# Quest Score Rubric — corps-achievements
**Version**: v10 (2026-03-17)

## What Changed in v10

**3 new aspirational criteria** extracted from Round 9 excellence signals (V-02, V-03, V-04):

- **C-27 (Structural barrier omission resistance — pre-printed phase barrier in output template)** — from V-02's template skeleton pattern. C-26 tests whether barrier language appears at each phase boundary; it does not constrain *how* the barrier arrives. V-02 embeds the barrier as a pre-printed element (`--- PHASE N SEALED [C-26] ---`) that the model transcribes rather than generates. Omission requires the model to actively skip a pre-printed element rather than simply fail to follow an instruction. C-27 tests whether phase barrier markers are embedded as pre-printed elements in the output template. Structurally independent of C-26: a prompt could carry pre-printed dividers without STOP instructions (unusual but valid); C-26 and C-27 may coexist. Weakness: a pre-printed divider is present but does not enumerate Phase N outputs — retroactive reframing via reinterpretation (not omission) remains possible even when C-27 is satisfied.

- **C-28 (Phase N output-set manifest declared before closure seal)** — from V-03's formal Closure Gate pattern. C-26 seals the phase at completion; it does not constrain what the model has declared about Phase N contents at the moment of sealing. V-03 requires enumeration sub-steps before writing the closure seal: the model counts and records specific Phase N outputs (namespace entries, contributors, artifact paths) prior to writing "STOP. Phase N complete." This creates an on-record manifest. Phase N+1 context cannot silently expand Phase N scope without contradicting explicitly stated counts. C-28 tests whether, at each phase boundary, the prompt requires the model to enumerate and record specific output counts before writing the closure seal. The manifest must include at minimum: artifact count, plus at least one additional dimension (contributor count, namespace count, or equivalent). A prompt with barrier language (C-26) but no output enumeration requirement fails C-28. A closure gate that writes the seal without first recording counts also fails C-28. C-28 is structurally independent of C-26 and C-27; it addresses scope-expansion retroactive reframing specifically, not omission.

- **C-29 (Dual-layer barrier redundancy — two independent mechanisms per phase boundary)** — from V-04's combination pattern. V-04 combines terse STOP declaration (C-26 layer) with pre-printed template divider (C-27 layer) at each phase boundary. The two mechanisms are structurally independent: one is instruction-generated, one is template-transcribed. Both must fail simultaneously to miss the barrier — instruction non-compliance alone is insufficient when a pre-printed divider is also present. C-29 tests whether each phase boundary carries two distinct, independently-implemented barrier mechanisms. C-29 requires C-26 and C-27 as preconditions; a prompt cannot pass C-29 without passing both. Limitation vs V-03: C-29 does not add output-set enumeration (C-28); a prompt passing C-29 but not C-28 eliminates omission risk but not retroactive scope expansion via reinterpretation.

**Scoring formula updated**: `aspirational_pass / 21 * 10` (was `/18`). Max composite remains 100.

---

**Prior version notes (carried forward for traceability)**

*v9 added C-26 from Round 8 excellence signal from V-05 ("Lifecycle Phase Barrier Language"):*

- **C-26** — from V-05's phase barrier pattern. Phase-do-not-begin instructions operate prospectively (prevent premature advancement but do not lock Phase N outputs). C-26 tests whether each phase boundary carries explicit barrier language ("STOP. Phase N complete." or equivalent declarative seal) at the point of phase completion, before the next phase's inputs are introduced. Structurally independent of C-22 through C-25.

*v8 added C-24 and C-25 from Round 7 excellence signals:*

- **C-24** — from V-02/V-04's REGISTRY PRIMACY declaration. C-22 tests schema co-location and self-sufficiency; C-24 tests whether the registry is explicitly declared the sole authoritative gate contract, with phase instructions subordinate to it. C-24 requires C-22 as a precondition.

- **C-25** — from V-03's severity-stratified FAIL block architecture. C-23 tests presence of at least one specific FAIL mode per gate; C-25 tests whether FAIL modes are stratified into Tier 1 (structural), Tier 2 (completeness), Tier 3 (semantic bypass) with explicit tier labels. Tier 3 is the most consequential: all required fields present, intent circumvented. C-25 requires C-23 as a precondition.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-29 | 10 | `pass/21 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/21 × 10)
```

| Score | Grade |
|-------|-------|
| 100 | Platinum |
| 90–99 | Gold |
| 75–89 | Silver |
| < 75 | Bronze |

---

## Criteria

### Essential (C-01 – C-05)

**C-01 — One state per achievement**
Each achievement entry carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED. Multi-state rows, ambiguous state, or missing state fail. Applies to both table and prose output formats.

**C-02 — Falsified named as honesty signal**
The Falsified achievement is present as a named entry. Its description frames falsification as evidence of investigative rigor ("followed evidence over assumptions" or equivalent), not as failure or absence.

**C-03 — Artifact-grounded classification**
State assignments cite source artifacts from Step 1 by namespace or skill. EARNED entries cite a specific artifact; IN-PROGRESS entries cite the partially-completed artifact or its count. Classification that cannot be traced to an artifact fails.

**C-04 — In-progress shows numeric progress**
IN-PROGRESS achievements express progress in `n of m` form (e.g., "3 of 5 namespaces covered"). Qualitative-only descriptions ("partially done", "underway") fail.

**C-05 — Next recommended action is specific**
Step 4 (or equivalent) names the next skill, the artifact it produces, and the achievement(s) it advances. Generic instructions ("continue the investigation") fail.

---

### Recommended (C-06 – C-08)

**C-06 — All 7 categories represented**
Every achievement category appears in the output. Categories with no earned or in-progress achievements are listed as LOCKED or explicitly noted as empty. Omitting a category fails.

**C-07 — Earned achievements carry dates**
EARNED entries include the date on which the achievement was earned. Date format may vary; absence of a date on an EARNED entry fails.

**C-08 — Frontmatter includes state counts**
Output includes a frontmatter or summary block with numeric counts for earned, in_progress, and locked achievements. Missing any of the three counts fails.

---

### Aspirational (C-09 – C-29)

**C-09 through C-21 — Established patterns (carried forward from prior rounds, unchanged)**
These thirteen criteria encode structural, formatting, and behavioral patterns established in Rounds 1–6. They cover gate architecture, phase ordering, schema completeness, cross-reference integrity, and output determinism. See v7 for full definitions.

**C-22 — Gate schemas co-located in a preamble registry**
All gate schemas (both SCAN GATE and CLASSIFY GATE) appear together in a single preamble registry block before Phase 1 begins. The registry entry for each gate is self-sufficient for inspection: it contains the complete schema without requiring cross-reference to the phase instruction that uses it. A gate schema that must be reconstructed by reading a phase instruction fails C-22.

**C-23 — Each gate pairs PASS schema with at least one specific FAIL mode**
Each gate definition includes both a PASS schema and a FAIL block listing at least one concrete output form that does not clear the gate. Generic FAIL descriptions ("output is insufficient") fail. FAIL modes must be specific enough that an example of failing output could be constructed from them.

**C-24 — Registry primacy declaration — registry is sole authoritative gate contract**
The prompt contains an explicit declaration that the registry is the sole authoritative source for gate contracts and that phase instructions implement these contracts without redefining, qualifying, or supplementing them. C-22 is a precondition: a registry without complete schemas cannot carry contractual authority over them. A prompt where the registry has complete schemas but phase instructions could plausibly be treated as parallel definitions passes C-22 but fails C-24. V-04 evidence: "REGISTRY PRIMACY: These schemas are the sole authoritative gate contracts. Phase instructions implement these contracts. They do not redefine, qualify, or supplement achievement conditions."

**C-25 — Severity-stratified FAIL blocks — three tiers with explicit semantic-bypass tier**
Each gate's FAIL block organizes failure modes into at least three severity tiers with explicit tier labels: Tier 1 (structural — required labels or fields absent), Tier 2 (completeness — required fields present but insufficiently populated), Tier 3 (semantic bypass — all required fields present but intent is circumvented). The Tier 3 (semantic-bypass) tier is the most consequential and must be named explicitly; a flat FAIL list that mixes structural and semantic failures without tier labels fails C-25 even if it enumerates the same failure modes. C-23 is a precondition: ungrouped FAIL modes cannot be stratified.

**C-26 — Explicit lifecycle phase barrier language — "STOP. Phase N complete." seals prior-phase outputs**
Each phase boundary carries an explicit declarative seal ("STOP. Phase N complete." or equivalent) at the point of phase completion, before the next phase's inputs or context are introduced. This is architecturally distinct from phase-do-not-begin instructions: the barrier closes the prior phase's output set at phase completion, preventing retroactive reframing by subsequent context. A prompt that uses only phase-do-not-begin instructions (gating Phase N+1 entry on Phase N completion) satisfies phase-ordering criteria but fails C-26, because it does not seal Phase N's outputs before Phase N+1 context arrives. C-26 is structurally independent of C-22 through C-25; it addresses a separate failure class (retroactive reframing) rather than gate-contract definition or FAIL-mode coverage. V-05 evidence: explicit "STOP. Phase N complete." at each phase boundary; V-04 uses phase-do-not-begin instructions without barrier seals.

**C-27 — Structural barrier omission resistance — phase barrier embedded as pre-printed output template element**
Phase barrier markers are embedded in the output template skeleton as pre-printed elements that the model transcribes rather than generates from instructions. A pre-printed barrier (e.g., `--- PHASE N SEALED [C-26] ---`) structurally blocks omission: the model must actively skip a visible element to miss it, rather than merely fail to follow an instruction. C-27 tests whether at least one phase boundary barrier is pre-printed in the template rather than generated. Structurally independent of C-26: a prompt could embed pre-printed dividers without also including STOP instructions, and C-26 and C-27 may coexist. Limitation: a pre-printed divider prevents omission but does not enumerate Phase N outputs — retroactive scope expansion via reinterpretation (not omission) remains possible even when C-27 is satisfied. V-02 evidence: `--- PHASE 1 SEALED [C-26] ---` and `--- PHASE 2 SEALED [C-26] ---` as pre-printed template elements; V-01 uses instruction-generated STOP declarations and does not pass C-27.

**C-28 — Phase N output-set manifest declared before closure seal**
At each phase boundary, the prompt requires the model to enumerate and record specific Phase N output counts before writing the closure seal. The manifest must include at minimum: artifact count, plus at least one additional dimension (contributor count, namespace count, or equivalent). This creates an on-record manifest: Phase N+1 context cannot silently expand Phase N scope without contradicting explicitly stated counts. A prompt with barrier language (C-26) but no output enumeration requirement fails C-28. A closure gate that writes the seal without first recording counts also fails C-28. Structurally independent of C-26 and C-27; addresses scope-expansion retroactive reframing specifically, not omission. C-28 does not require C-26 as a precondition: a prompt could require output-set enumeration at phase boundaries without using STOP barrier language, though in practice both would normally coexist. V-03 evidence: Closure Gate sub-steps (1)–(2) require counting and declaring namespace entries, contributors, and artifact paths before sub-step (4) writes the closure seal; V-01, V-02, and V-04 use barrier language without prior enumeration and do not pass C-28.

**C-29 — Dual-layer barrier redundancy — two independent barrier mechanisms per phase boundary**
Each phase boundary carries two distinct, structurally independent barrier mechanisms: one instruction-generated (C-26 layer — model writes the STOP declaration) and one template-transcribed (C-27 layer — model copies a pre-printed divider). Both must fail simultaneously to miss the barrier, eliminating the single-point-of-failure risk present in either mechanism alone. C-29 requires C-26 and C-27 as preconditions; a prompt cannot pass C-29 without satisfying both. Limitation: dual-layer redundancy eliminates omission risk but does not add output-set enumeration (C-28); a prompt passing C-29 but not C-28 still lacks a declared output manifest, leaving retroactive scope expansion via reinterpretation possible. V-04 evidence: each phase boundary carries both "STOP. Phase N complete. [C-26]" (generated) and `--- PHASE N SEALED [C-26] ---` (pre-printed), with the structural audit gate separately confirming all four barrier elements (2 STOP + 2 pre-printed); V-01 (STOP only) and V-02 (pre-printed only) are single-layer and do not pass C-29.
