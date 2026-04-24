## Quest Score — corps-achievements — Round 10 (Rubric v10)

**Date**: 2026-03-17 | **Rubric**: v10 | **Aspirational count**: 21 (C-09–C-29)

---

### Shared Baseline (C-01–C-26)

All five variations carry the complete v9 baseline. C-01 through C-26 evaluated once; result applies to all.

| Tier | Criteria | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|----------|------|------|------|------|------|
| Essential | C-01 through C-05 | 5/5 PASS | 5/5 PASS | 5/5 PASS | 5/5 PASS | 5/5 PASS |
| Recommended | C-06 through C-08 | 3/3 PASS | 3/3 PASS | 3/3 PASS | 3/3 PASS | 3/3 PASS |
| Aspirational C-09–C-26 | 18 criteria | 18/18 PASS | 18/18 PASS | 18/18 PASS | 18/18 PASS | 18/18 PASS |

**Essential notes**: Output schema defines exactly one state per row [C-01]; Falsified row present with rigor framing [C-02]; evidence column cites PHASE 1 STATE [C-03]; IN-PROGRESS uses `n of m` form [C-04]; next action names skill + artifact + advancement chain [C-05]. All PASS for all variations — template carries these pre-printed, no variation breaks them.

**C-26 note**: All variations include `STOP. Phase N complete. [C-26]` + CLOSURE GATE with explicit pass confirmation before the next phase begins. PASS for all.

---

### New Criteria — C-27, C-28, C-29

These three criteria are the sole differentiators in R10.

---

#### C-27 — Structural barrier omission resistance (pre-printed element in template)

Criterion tests whether barrier markers are **embedded as pre-printed elements** requiring the model to actively skip them to omit.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | `--- PHASE N SEALED [C-26][C-27] ---` carries explicit `[C-27]` tag; template preamble declares barriers as pre-printed elements; STRUCTURAL AUDIT GATE checks `[C-27] tag present` by name — string-match verifiable |
| V-02 | **PARTIAL** | `--- PHASE N SEALED [C-26] ---` is pre-printed (structural property present); no `[C-27]` tag; template preamble says "do not modify pre-printed elements" but does not label this the C-27 mechanism; STRUCTURAL AUDIT GATE confirms C-26 barrier but does NOT check C-27 by name — scorer must infer from template format |
| V-03 | **PASS** | `--- PHASE N SEALED [C-26] ---` is pre-printed (structural property present); DUAL-LAYER BARRIER block explicitly names it "Layer 2: Pre-printed divider (structure-enforced -- model transcribes, not generates) [C-27]" — C-27 auditable via DUAL-LAYER declaration even without tag on barrier line; audit checks C-29 block which cites C-27 |
| V-04 | **PASS** | `--- PHASE N SEALED [C-26][C-27] ---` explicit tag; audit explicitly checks `[C-27] tag present` by name |
| V-05 | **PASS** | `[C-27]` tag on barrier line + template preamble declaration + Layer 2 citation in DUAL-LAYER block + dedicated C-27 section in STRUCTURAL AUDIT GATE — triply auditable |

---

#### C-28 — Phase N output-set manifest declared before closure seal

Criterion tests whether the prompt requires enumeration and recording of specific output counts (artifact count + ≥1 additional dimension) before the closure seal.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL** | Closure gate sub-steps enumerate counts before STOP: "(1) Count Phase 1 items: [N] namespace entries, [M] contributors, [K] artifact paths" — three dimensions, satisfies spirit; embedded in gate prose, not a standalone named block; STRUCTURAL AUDIT GATE checks C-26/C-27 but does NOT check C-28 by name — scorer must interpret gate pass confirmation |
| V-02 | **PASS** | Standalone `PHASE N MANIFEST [C-28]:` block with `Artifact count: [K]` + `Namespace count: [N]` appears before STOP; labeled `[C-28]`; CLOSURE GATE explicitly verifies "PHASE N MANIFEST [C-28] is recorded above"; audit checks MANIFEST present, two dimensions present, CLOSURE GATE references manifest — string-match verifiable |
| V-03 | **PARTIAL** | Same as V-01: closure gate sub-steps enumerate counts before STOP; no standalone MANIFEST block; audit checks C-29 but not C-28 by name |
| V-04 | **PASS** | Standalone `PHASE N MANIFEST [C-28]:` block (artifact count + namespace count); CLOSURE GATE references manifest; audit checks both MANIFEST dimensions and CLOSURE GATE reference |
| V-05 | **PASS** | Standalone MANIFEST block + CLOSURE GATE references manifest ("Manifest verified ([K] artifacts, [N] namespaces). Phase 2 inputs constrained to PHASE 1 MANIFEST.") + dedicated C-28 section in STRUCTURAL AUDIT GATE with 4 individual checks (block present × 2 phases, two-dimension verified × 2 phases) |

---

#### C-29 — Dual-layer barrier redundancy (two independent mechanisms per boundary)

Criterion tests whether each phase boundary carries two distinct, independently-implemented barrier mechanisms. **Requires C-26 and C-27 as preconditions.**

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL** | STOP (Layer 1, C-26) + `--- PHASE N SEALED [C-26][C-27] ---` (Layer 2, C-27 tagged) = two distinct mechanisms; preconditions C-26 ✓ C-27 ✓ (explicit tag); structurally satisfies C-29; no explicit DUAL-LAYER BARRIER declaration; audit checks C-26/C-27 but not C-29 by name — compliance inferred from structure |
| V-02 | **PARTIAL** | STOP + pre-printed `--- PHASE N SEALED [C-26] ---`; precondition C-26 ✓; precondition C-27 PARTIAL (pre-printed but unlabeled); no explicit DUAL-LAYER declaration; audit does not check C-29 — C-27 precondition weakness compounds C-29 evidence weakness |
| V-03 | **PASS** | Explicit `DUAL-LAYER BARRIER [C-26/C-27][C-29]:` block after each seal; names Layer 1 (STOP, instruction-enforced), Layer 2 (pre-printed, structure-enforced); independence assertion: "Both must fail simultaneously for barrier omission [C-29]"; audit explicitly verifies declaration + Layer 1 named + Layer 2 named + independence assertion present (both phases) |
| V-04 | **PARTIAL** | STOP + [C-27]-tagged pre-printed = two explicitly labeled independent layers; preconditions C-26 ✓ C-27 ✓ (strong); C-27 tag makes Layer 2 explicitly identified; no DUAL-LAYER BARRIER declaration; audit checks C-26/C-27/C-28 but not C-29 by name — strong structural evidence, no named architectural claim |
| V-05 | **PASS** | Explicit DUAL-LAYER BARRIER block (same as V-03); C-26 ✓ and C-27 ✓ (tagged) as named preconditions in the declaration; dedicated C-29 section in STRUCTURAL AUDIT GATE with 6 individual checks (Layer 1 named × 2, Layer 2 named × 2, independence assertion × 2) |

---

### Aspirational Pass Counts (PARTIAL = 0.5)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09–C-26 (18) | 18 | 18 | 18 | 18 | 18 |
| C-27 | 1.0 | 0.5 | 1.0 | 1.0 | 1.0 |
| C-28 | 0.5 | 1.0 | 0.5 | 1.0 | 1.0 |
| C-29 | 0.5 | 0.5 | 1.0 | 0.5 | 1.0 |
| **Total / 21** | **20.0** | **20.0** | **20.5** | **20.5** | **21.0** |

---

### Composite Score Computation

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/21 × 10)`

| Variation | Essential | Recommended | Aspirational | **Composite** | **Grade** |
|-----------|-----------|-------------|--------------|---------------|-----------|
| V-01 | 5/5 × 60 = 60 | 3/3 × 30 = 30 | 20.0/21 × 10 = 9.52 | **99.52** | Gold |
| V-02 | 60 | 30 | 20.0/21 × 10 = 9.52 | **99.52** | Gold |
| V-03 | 60 | 30 | 20.5/21 × 10 = 9.76 | **99.76** | Gold |
| V-04 | 60 | 30 | 20.5/21 × 10 = 9.76 | **99.76** | Gold |
| V-05 | 60 | 30 | 21/21 × 10 = 10.00 | **100.00** | Platinum |

**Rankings**: V-05 (1st, 100) > V-03 = V-04 (tied 2nd, 99.76) > V-01 = V-02 (tied 4th, 99.52)

---

### Excellence Signals from V-05

**Signal 1 — Partitioned audit gate by criterion**
V-05's STRUCTURAL AUDIT GATE is sectioned into labeled groups: `-- C-26 checks --`, `-- C-27 checks --`, `-- C-28 checks --`, `-- C-29 checks --`. Prior rounds used a flat list where items for different criteria were interleaved. Partitioning means a scorer can verify any single criterion by reading its labeled section without scanning the full audit. The summary line enumerates per-criterion counts: "[2] STOP barriers (C-26). [2] closure gate confirmations (C-26). [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks... (C-28). [2] dual-layer declarations... (C-29)."

**Signal 2 — Triply auditable C-27 evidence**
V-05 is the only variation where C-27 compliance is verifiable from three independent locations: (1) `[C-27]` tag on the barrier line itself, (2) template preamble declaration naming the `[C-26][C-27]` barriers as pre-printed structural elements, (3) Layer 2 citation in the DUAL-LAYER BARRIER block. Any one of these alone satisfies C-27; all three together mean C-27 evidence survives any single omission without becoming unverifiable.

**Signal 3 — Closure gate cross-references manifest (creates temporal chain)**
V-05's closure gate pass confirmation reads: "Manifest verified ([K] artifacts, [N] namespaces). Phase N+1 inputs constrained to PHASE N MANIFEST." The gate explicitly names the manifest it verified, creating a traceable record that the seal was written after the manifest was populated. This closes the gap identified in the v10 open-signals list: a scorer can confirm not only that the manifest exists but that the gate acknowledged it before writing the STOP.

**Open excellence signals (C-30+ candidates)**

- **Typed failure-mode contract** (not yet present in V-05): The DUAL-LAYER block describes how each layer can fail ("Layer 1 fails if model omits STOP; Layer 2 fails if model skips pre-printed element") but does not distinguish the two distinct failure modes at risk: *omission* (blocked by dual-layer redundancy) vs. *retroactive reinterpretation* (blocked only by manifest). Naming this distinction explicitly — "Layer 1+2 together block omission; manifest blocks reinterpretation; this prompt addresses both" — would be a C-30 typed failure-mode contract.

- **Manifest-to-audit cross-reference ID** (partially present): V-05's audit says "Phase 1 MANIFEST artifact count + namespace count recorded [C-28]: [confirmed]" but does not cite the line where the manifest appears. A criterion requiring the audit confirmation to include a locator ("MANIFEST at line N of Phase 1 output") would make seal-after-manifest temporal ordering mechanically verifiable.

---

### Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| [C-27] tag on barrier | YES | — | — | YES | YES |
| Standalone MANIFEST [C-28] | — | YES | — | YES | YES |
| DUAL-LAYER BARRIER [C-29] | — | — | YES | — | YES |
| C-27 string-match auditable | YES | no | via C-29 block | YES | YES |
| C-28 string-match auditable | no | YES | no | YES | YES |
| C-29 string-match auditable | no | no | YES | no | YES |
| Composite | 99.52 | 99.52 | 99.76 | 99.76 | 100 |

**Winner: V-05** — only variation where all three new criteria (C-27, C-28, C-29) have named, directly addressable evidence points each verifiable by string match without interpretation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Partitioned audit gate with per-criterion labeled sections (C-26 / C-27 / C-28 / C-29 each have their own check group and per-criterion count in the summary line) makes each new criterion independently verifiable without scanning the full audit list", "C-27 compliance triply evidenced in V-05: tag on barrier line, template preamble declaration, and Layer 2 citation in DUAL-LAYER block — any one location independently confirms C-27; three-location redundancy means C-27 evidence survives a single omission"]}
```
