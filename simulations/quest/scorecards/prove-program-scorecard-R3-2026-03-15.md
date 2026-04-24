## prove-program R3 — Variation Scoring

### Scoring Schema

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-16 | 5 | 40 |
| **Total** | | | **130** |

Threshold: 100. PASS/PARTIAL/FAIL → full/half/zero.

---

### V-01 — Lifecycle (3-phase COMMIT/EXECUTE/VERIFY)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Hypothesis pre-commitment | **PASS** | Phase 1 COMMIT opens with Hypothesis + Falsification; GATE blocks Phase 1B until complete |
| C-02 ≥2 distinct types | **PASS** | 1B Contract table requires ≥2 types by name with explicit Rationale column |
| C-03 Feed-forward | **PASS** | Phase 2 mandates `Input: quote the specific output content from the previous block — not "see above."` |
| C-04 Synthesis contrast | **PASS** | Phase 3C has `What we thought: [hypothesis verbatim]` / `What we actually learned: [must differ]` |
| C-05 Qx.md format + path | **PASS** | Artifact section: `simulations/prove/research/{topic}-research-{date}.md` + frontmatter |
| C-06 Principles labeled | **PASS** | 3D Principles table: Label / Principle / Source; "≥2, no generic truisms" enforced |
| C-07 Findings confidence | **PASS** | 3B Findings table: Finding / Source / Confidence / Evidence basis |
| C-08 Cross-namespace note | **PASS** | 3C: "Name the downstream Signal artifact this research should update... State what finding it receives." |
| C-09 | **PASS** | |
| C-10 | **PASS** | |
| C-11 Feed-forward audit ledger | **PASS** | 3A Feed-Forward Audit = standalone table cross-referencing committed vs delivered outputs |
| C-12 COMPLETE marker | **PARTIAL** | No explicit COMPLETE marker per block; Contract delivery line present but no terminal status token |
| C-13 Inertia gap declaration | **PASS** | Phase 0 GATE: "Inertia gap REQUIRED before Phase 1. If prove-topic is sufficient, stop." |
| C-14 Plan-level output routing | **PASS** | 1B table has `Output label` + `Consumed by` columns filled before Phase 2 begins |
| C-15 Per-block delivery boolean | **PASS** | `Contract delivery: output label = "..." = "...", consumed by = "..." — delivered? Yes / No` inside each E-NN block |
| C-16 Gap-to-plan column | **PASS** | 1B table has `Closes gap?` column; ≥1 row Yes required |

**Score: 60 + 30 + 38 = 128 / 130**
Essential all PASS ✓

---

### V-02 — Output Format (unified evolving table)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Hypothesis | **PASS** | Hypothesis section required before Program Table; GATE stated |
| C-02 ≥2 types | **PASS** | Program Table rules: "≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)" |
| C-03 Feed-forward | **PARTIAL** | `Consumed by (actual)` column implies threading but no per-block Input citation rule; experiment block prose unenforced |
| C-04 Synthesis contrast | **PASS** | Synthesis section exists; inertia gap closure check implied |
| C-05 Qx.md format | **PASS** | Artifact write required |
| C-06 Principles | **PASS** | Synthesis section expected to include principles |
| C-07 Findings confidence | **PARTIAL** | Table format does not explicitly require confidence levels in experiment blocks |
| C-08 Cross-namespace note | **PARTIAL** | Not explicitly required in template; synthesis section underspecified |
| C-09 | **PASS** | |
| C-10 | **PASS** | |
| C-11 Feed-forward audit ledger | **PARTIAL** | `Contract met?` column approximates a ledger; inline, not standalone — cannot be read independently |
| C-12 COMPLETE marker | **PARTIAL** | Audit column serves a closing function but no explicit status token |
| C-13 Inertia gap declaration | **PASS** | Inertia Check + GATE required |
| C-14 Plan-level output routing | **PASS** | PLAN columns (Output label, Consumed by) required complete before experiments |
| C-15 Per-block delivery boolean | **FAIL** | Table cell updated after execution ≠ boolean inside experiment block prose; the boolean is in the wrong place |
| C-16 Gap-to-plan column | **PASS** | `Closes gap?` column in Program Table |

**Score: 54 + 20 + 33 = 107 / 130**
Essential not all PASS (C-03 PARTIAL) ✗

---

### V-03 — Imperative Procedural + FAIL conditions

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Hypothesis | **PASS** | FAIL gate blocks execution until hypothesis stated |
| C-02 ≥2 types | **PASS** | FAIL condition: plan does not name ≥2 distinct types |
| C-03 Feed-forward | **PASS** | FAIL condition per experiment block: "next experiment does not cite output from this block" |
| C-04 Synthesis contrast | **PASS** | FAIL gate at synthesis: "what we actually learned" must differ from hypothesis |
| C-05 Qx.md format | **PASS** | Artifact required; FAIL if path incorrect |
| C-06 Principles | **PASS** | FAIL: synthesis contains <2 labeled principles |
| C-07 Findings confidence | **PASS** | FAIL gate at findings table |
| C-08 Cross-namespace note | **PARTIAL** | FAIL register enforces local structure; cross-namespace downstream routing may not be gated |
| C-09 | **PASS** | |
| C-10 | **PASS** | |
| C-11 Feed-forward audit ledger | **FAIL** | No standalone ledger; FAIL gates replace the post-execution audit table entirely |
| C-12 COMPLETE marker | **PARTIAL** | FAIL gate at each block provides a terminal check; no explicit COMPLETE token |
| C-13 Inertia gap declaration | **PASS** | FAIL: proceed without declaring inertia gap |
| C-14 Plan-level output routing | **PASS** | Plan table with Output label + Consumed by required pre-execution |
| C-15 Per-block delivery boolean | **PASS** | FAIL condition triggers if delivery boolean absent from block |
| C-16 Gap-to-plan column | **PASS** | Gap column in plan table; FAIL: no Closes gap? row = Yes |

**Score: 60 + 25 + 33 = 118 / 130**
Essential all PASS ✓

---

### V-04 — Contract Loop, minimal (output format + lifecycle)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Hypothesis | **PASS** | Phase 1 COMMIT; GATE before 1B |
| C-02 ≥2 types | **PASS** | 1B contract table; ≥2 distinct types enforced |
| C-03 Feed-forward | **PASS** | Phase 2 Input: citation requirement per block |
| C-04 Synthesis contrast | **PASS** | Phase 3C synthesis contrast present |
| C-05 Qx.md format | **PASS** | Artifact section present |
| C-06 Principles | **PASS** | 3D principles table |
| C-07 Findings confidence | **PASS** | 3B findings with confidence |
| C-08 Cross-namespace note | **PARTIAL** | Present in some forms; not the primary focus of this minimal variation |
| C-09 | **PASS** | |
| C-10 | **PASS** | |
| C-11 Feed-forward audit ledger | **PASS** | 3A standalone audit table |
| C-12 COMPLETE marker | **PARTIAL** | Contract delivery line present; no terminal COMPLETE token |
| C-13 Inertia gap declaration | **FAIL** | Minimum structure omits inertia gap gate |
| C-14 Plan-level output routing | **PASS** | 1B table output routing pre-commitment |
| C-15 Per-block delivery boolean | **PASS** | Contract delivery boolean in each E-NN block |
| C-16 Gap-to-plan column threading | **FAIL** | Closes gap? column absent; minimal structure does not include gap-closing assignment |

**Score: 60 + 25 + 28 = 113 / 130**
Essential all PASS ✓

---

### V-05 — Role Sequence + All 8 Aspirational

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Hypothesis | **PASS** | Role sequence opens with hypothesis stage; role cannot advance until stated |
| C-02 ≥2 types | **PASS** | Plan stage enforces ≥2 types with role-indexed rationale |
| C-03 Feed-forward | **PASS** | Explicit per-block input citation rule; role sequence enforces ordering |
| C-04 Synthesis contrast | **PASS** | Synthesis role: "what we thought vs. what we actually learned" required |
| C-05 Qx.md format | **PASS** | Artifact write with frontmatter |
| C-06 Principles | **PASS** | Principles role: ≥2 labeled, actionable, distinct |
| C-07 Findings confidence | **PASS** | Findings role with confidence levels |
| C-08 Cross-namespace note | **PASS** | Synthesis explicitly requires downstream Signal artifact routing |
| C-09 | **PASS** | |
| C-10 | **PASS** | |
| C-11 Feed-forward audit ledger | **PASS** | Standalone audit table: committed vs delivered, all rows |
| C-12 COMPLETE marker | **PASS** | "One line per COMPLETE block: `Contract delivery: ... delivered? Yes/No`" — explicit token per R2 V-05 extension |
| C-13 Inertia gap declaration | **PASS** | Inertia gap gate pre-commitment; role cannot proceed without it |
| C-14 Plan-level output routing | **PASS** | Plan stage: Output label + Consumed by columns committed before any experiment |
| C-15 Per-block delivery boolean | **PASS** | `Contract delivery:` line INSIDE each block prose, not table cell — the critical C-15 compliance form |
| C-16 Gap-to-plan column threading | **PASS** | Closes gap? column in plan table threads inertia gap to execution assignment |

**Score: 60 + 30 + 40 = 130 / 130**
Essential all PASS ✓

---

### Summary Table

| Variation | Essential | Recommended | Aspirational | Total | Essential all PASS |
|-----------|-----------|-------------|--------------|-------|--------------------|
| V-05 Role+All8 | 60/60 | 30/30 | 40/40 | **130** | ✓ |
| V-01 Lifecycle | 60/60 | 30/30 | 38/40 | **128** | ✓ |
| V-03 Imperative+FAIL | 60/60 | 25/30 | 33/40 | **118** | ✓ |
| V-04 Contract minimal | 60/60 | 25/30 | 28/40 | **113** | ✓ |
| V-02 Unified table | 54/60 | 20/30 | 33/40 | **107** | ✗ |

---

### Excellence Signals from V-05

**1. Contract delivery boolean must live inside block prose, not in a table cell.**
V-02 demonstrates the failure mode: updating a `Delivered?` column after execution satisfies the ledger (C-11) but not C-15. V-05 requires `Contract delivery: output label = "..." — delivered? Yes/No` as an inline line *within* each experiment block. Placement is the criterion.

**2. Role sequence + lifecycle together close all 8 aspirational gaps where neither alone does.**
V-01 (lifecycle alone) reaches 38/40 but cannot fully satisfy C-12 without a named COMPLETE marker per block — role sequence supplies the explicit terminal token. V-03 (FAIL gates alone) reaches 33/40 but loses C-11 because FAIL gates replace rather than supplement the audit ledger. Only layering role stage sequencing over the lifecycle phases delivers both simultaneously.

**3. Inertia gap declaration must thread from Phase 0 into the plan table (C-13 + C-16 are co-dependent).**
V-04 omits both and loses 10 aspirational points. V-05 shows they are a coupled pair: declaring the inertia gap (C-13) without a `Closes gap?` column (C-16) leaves the gap-closing assignment unverifiable pre-execution; having the column without the gap declaration leaves it meaningless. Both must be present.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["contract delivery boolean must appear inside block prose not in a post-hoc table cell — placement is the C-15 compliance gate", "role sequence layered over lifecycle phases satisfies both COMPLETE marker (C-12) and standalone audit ledger (C-11) where each axis alone fails one", "inertia gap declaration (C-13) and gap-to-plan column (C-16) are co-dependent — omitting either makes both unverifiable"]}
```
