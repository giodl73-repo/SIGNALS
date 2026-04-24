I've now read all five variations completely. Let me score each against the v7 rubric.

---

# Scorecard — campaign-specify / Round 7

## Baseline Assessment

All five variations are built on the R6 V-05 base: 5/5 essential, 3/3 recommended, and 18/23 aspirational (C-09 through C-26 inherited, plus C-30 and C-31 from R6). The R7 question is: which of C-27 through C-31 does each variation earn?

---

## Essential Criteria (all variations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-01 | Three artifacts produced | PASS | PASS | PASS | PASS | PASS | Spec, proposal, pitch phases with write gates enforcing disk existence |
| C-02 | Spec has all six required sections | PASS | PASS | PASS | PASS | PASS | Phase 1 mandates Overview, User Problem, Proposed Solution, Constraints, Open Questions, Self-Review |
| C-03 | Proposal has 3+ options including do-nothing | PASS | PASS | PASS | PASS | PASS | Phase 2 requires three options minimum; Option 1 MUST be named Do Nothing |
| C-04 | Pitch covers three audience versions | PASS | PASS | PASS | PASS | PASS | Phase 3 requires Exec Version, Dev Version, Maker Version |
| C-05 | Cross-artifact consistency | PASS | PASS | PASS | PASS | PASS | Same Step 0a inertia costs propagate into spec User Problem, Phase 2 Defeating Do Nothing, Phase 3 pitch versions |

**Essential: 5/5 all variations.**

---

## Recommended Criteria (all variations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-06 | Spec self-review flags gaps | PASS | PASS | PASS | PASS | PASS | "At least one named gap. 'No gaps found' fails." |
| C-07 | Pitch anti-positioning section | PASS | PASS | PASS | PASS | PASS | Anti-Positioning section required, structurally separate from audience versions |
| C-08 | Proposal recommendation cites trade-off rationale | PASS | PASS | PASS | PASS | PASS | Defeating blocks require traceable trade-off — "specific trade-off traceable to a risk, effort, or cons field in the options analysis — not a preference statement" |

**Recommended: 3/3 all variations.**

---

## Aspirational Criteria — New (C-27 through C-31)

### C-27 — Voice gate audit row in COMPLETION INDEX as named section element

R6 V-05 has the bullet `Voice differentiation gate result: distinct / rewritten-to-distinct` in the Additional index — but R6 scoring showed V-05 did NOT earn C-27 with that bullet alone. C-27 requires the COMPLETION INDEX to formally classify its contents with the voice gate as a structurally named element.

| Variation | Structure | Verdict |
|-----------|-----------|---------|
| V-01 | Bullet-list Additional index, same preamble as R6 V-05: "post-execution existence record and unified compliance audit" — no section enumeration, no named Voice Compliance section | **FAIL** |
| V-02 | Same bullet-list COMPLETION INDEX structure as V-01 | **FAIL** |
| V-03 | Preamble explicitly names four sections: "The index has four named sections: Artifact Existence Record, Phase Gate Audit, Citation Audit, and Voice Compliance Audit." `### Voice Compliance Audit` header at same level as other sections. Voice gate result lives inside a formally classified section, not a bullet | **PASS** |
| V-04 | Bullet-list Additional index, same as R6 V-05 base (rubric targeting confirms: "preserved from R6 V-05"). Preamble does not enumerate sections | **FAIL** |
| V-05 | Formal four-section structure from V-03 plus C-28+C-29 from V-04. Preamble: "The index has four named sections: Artifact Existence Record, Phase Gate Audit, Citation Audit, and Voice Compliance Audit. Each section classifies a distinct category of compliance state." `### Voice Compliance Audit` with ### header | **PASS** |

### C-28 — Per-audience Pass/Fail in voice differentiation gate

Requires "Exec gate / Dev gate / Maker gate" labels with explicit parenthetical `Pass (...) / Fail (...)` criteria per audience, plus an independent-verdict framing.

| Variation | Gate Step 3 label | Parenthetical Pass/Fail | Independence | Verdict |
|-----------|-------------------|------------------------|--------------|---------|
| V-01 | "Exec gate / Dev gate / Maker gate" | ✓ `Pass (opening names a business cost...) / Fail (opens with product description...)` per audience | "each audience gate must independently pass" | **PASS** |
| V-02 | "Exec check / Dev check / Maker check" | Plain `Pass / Fail` only | "each must independently pass" | **FAIL** |
| V-03 | "Exec check / Dev check / Maker check" | Plain `Pass / Fail` only | "each must independently pass" | **FAIL** |
| V-04 | "Exec gate / Dev gate / Maker gate" | ✓ `Pass (opening names a business cost...) / Fail (opens with product description...)` per audience | "each audience gate must independently pass" | **PASS** |
| V-05 | Same as V-04 | Same as V-04 | Same as V-04 | **PASS** |

### C-29 — Contract-derived gate criteria with named rewrite anchor

Requires: (1) gate Step 3 criteria explicitly name "the Step 0c exec/dev/maker voice contract" as the criteria source, AND (2) gate Step 4 rewrite instruction names "the Step 0c contract for that audience" as the revision anchor. Both required.

| Variation | Step 3 contract naming | Step 4 rewrite anchor | Verdict |
|-----------|------------------------|----------------------|---------|
| V-01 | "exec contract's frame" — generic, no Step 0c | "using the **Step 0c contract** for that audience as the revision anchor" ✓ | **FAIL** — Step 3 missing; one location insufficient |
| V-02 | "frame of the **Step 0c exec voice contract**" ✓; "**Step 0c dev voice contract**" ✓; "**Step 0c maker voice contract**" ✓ | "Return to the **Step 0c voice contract** for that audience as the named revision anchor" ✓ | **PASS** |
| V-03 | "exec contract's frame" — same as R6 V-05 base | "using the Step 0c contract for that audience as the revision anchor" ✓ | **FAIL** — Step 3 missing Step 0c name |
| V-04 | "frame of the **Step 0c exec voice contract**" ✓; "**Step 0c dev voice contract**" ✓; "**Step 0c maker voice contract**" ✓ | "Return to the **Step 0c voice contract** for that audience as the named revision anchor" ✓ | **PASS** |
| V-05 | Same as V-04 ✓ | Same as V-04 ✓ | **PASS** |

### C-30 — Inline gate blocks carry step-pair annotation

Requires inline Phase 0 gate labels to include the step-pair (e.g., `--- GATE 1 (0a→0b): Do not advance...`), and COMPLETION INDEX gate audit row to match.

All five variations preserve R6 V-05's Phase 0 gate structure verbatim:
```
--- GATE 1 (0a→0b): Do not advance to Step 0b until all three inertia costs are complete. ---
--- GATE 2 (0b→0c): Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---
--- GATE 3 (0c→0d): Do not advance to Step 0d until all three voice contracts are written. ---
```
COMPLETION INDEX gate audit row: "Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)". Step-pair appears in both inline label and audit row.

**C-30: PASS all five variations.**

### C-31 — Doubly-anchored voice contract traceability

Requires Step 0c contracts referenced both (a) as production anchors in pitch writing instructions AND (b) as named enforcement criteria in the voice differentiation gate check.

All five variations preserve "Use Step 0c exec/dev/maker voice contract as anchor" in the pitch writing sections (production anchor). The gate in all five uses the Step 0c contracts as enforcement: Step 1 explicitly labels them "Step 0c exec/dev/maker voice contract"; Step 4 references "Step 0c contract for that audience." Even in V-02 and V-03 where Step 3 uses "exec contract's frame" (not naming Step 0c), the gate as a whole is anchored to Step 0c in Steps 1 and 4. R6 V-05 earned C-31 with this same structure.

**C-31: PASS all five variations.**

---

## Aspirational Criteria — Prior Rounds (C-09 through C-26)

All 18 criteria from C-09 through C-26 are inherited from R6 V-05 base unchanged. None of the R7 structural changes (gate label format, Step 0c naming, COMPLETION INDEX section headers) disturb any of these prior mechanisms. All pass.

**C-09 through C-26: PASS all five variations (18/18).**

---

## Score Summary

### New criteria grid (C-27 through C-31)

| Variation | C-27 | C-28 | C-29 | C-30 | C-31 | New earned |
|-----------|------|------|------|------|------|------------|
| V-01 | FAIL | PASS | FAIL | PASS | PASS | C-28 (+1 over base) |
| V-02 | FAIL | FAIL | PASS | PASS | PASS | C-29 (+1) |
| V-03 | PASS | FAIL | FAIL | PASS | PASS | C-27 (+1) |
| V-04 | FAIL | PASS | PASS | PASS | PASS | C-28 + C-29 (+2) |
| V-05 | PASS | PASS | PASS | PASS | PASS | All five (+3) |

### Composite scores

Formula: `(essential/5 × 60) + (rec/3 × 30) + (asp/23 × 10)`

| Variation | Essential | Rec | Asp | Composite |
|-----------|-----------|-----|-----|-----------|
| V-01 | 5/5 | 3/3 | 21/23 | 60 + 30 + 9.13 = **99.1** |
| V-02 | 5/5 | 3/3 | 21/23 | 60 + 30 + 9.13 = **99.1** |
| V-03 | 5/5 | 3/3 | 21/23 | 60 + 30 + 9.13 = **99.1** |
| V-04 | 5/5 | 3/3 | 22/23 | 60 + 30 + 9.57 = **99.6** |
| V-05 | 5/5 | 3/3 | 23/23 | 60 + 30 + 10.00 = **100.0** |

### Ranking

```
V-05 (100.0) > V-04 (99.6) > V-01 = V-02 = V-03 (99.1)
```

---

## C-27 Calibration Note

The V-04 prediction in the variations file was 23/23, assuming the bullet `Voice differentiation gate result: distinct / rewritten-to-distinct` earned C-27. However, R6 scoring showed V-05 R6 — which has the identical bullet — did NOT earn C-27, while R6 V-04 did. V-04 R7 is built on R6 V-05's COMPLETION INDEX structure (bullet-list), not R6 V-04's (whatever made it earn C-27). The V-03 axis was designed to test precisely this question. Formal section classification (V-03 / V-05) is the operative mechanism for C-27; bullet form alone is insufficient. V-04 therefore scores 22/23, not 23/23.

---

## Excellence Signals from V-05

V-05 is the top-scoring variation and the first to earn all 23 aspirational criteria simultaneously. Three patterns make it structurally superior to all R6 variations:

1. **Three-mechanism gate sentence** — The single Step 3 gate sentence "Does the [Audience] Version opening match the frame of the Step 0c [audience] voice contract ([register])? Pass (opening names...) / Fail (opens with...)" simultaneously carries C-28 (named-gate formalism + parenthetical verdicts), C-29 (Step 0c as named criteria source), and C-31 (contract as enforcement criterion). A single location in the skill text resolves three criteria; no additional structural overhead required.

2. **COMPLETION INDEX as four-section classified architecture** — Restructuring from an unclassified bullet list to four named `###` sections (Artifact Existence Record, Phase Gate Audit, Citation Audit, Voice Compliance Audit) elevates the COMPLETION INDEX from a checklist to an auditable state record. The Voice Compliance Audit section makes voice compliance a first-class element alongside artifact existence — C-27 earned via formal classification, not a buried bullet.

3. **Preamble enumeration as structural index map** — The COMPLETION INDEX preamble explicitly names all four sections before the body begins: "The index has four named sections: ... Each section classifies a distinct category of compliance state." This makes the scope of the post-execution audit inspectable from the preamble alone, without reading the body. The preamble functions as a contract for what the COMPLETION INDEX covers.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Three-mechanism gate sentence: single Step 3 sentence simultaneously carries C-28 named-gate formalism, C-29 Step 0c contract naming, and C-31 enforcement criterion — three criteria resolved at one structural location", "COMPLETION INDEX four-section classified architecture: named ### sections (Artifact Existence Record, Phase Gate Audit, Citation Audit, Voice Compliance Audit) elevate voice compliance to first-class audit element alongside artifact existence", "Preamble enumeration as structural index map: COMPLETION INDEX preamble explicitly names all four sections and classifies their category before the body begins, making audit scope inspectable from preamble alone"]}
```
