## corps-scan R11 — Quest Score (Rubric v11)

**480 pts max | 48 criteria | 10 pts each**

---

### Scoring Method

Criteria C-01–C-42 are assessed as a group (prior-round invariants). The task preamble states all five variations preserve these invariants. I verified structural presence of key anchors in each prompt:

| Anchor | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| CONSTRAINT MANIFEST + TOTAL row (C-28, C-34) | ✓ | ✓ | ✓ | ✓ | ✓ |
| PHASE CONTRACT TABLE + count column (C-32, C-37) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Blockquote predicates (C-33, C-35) | ✓ | ✓ | ✓ | ✓ | ✓ |
| VIOLATION column in manifest (C-36) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Cross-manifest arithmetic match (C-38) | 15=15 ✓ | 16=16 ✓ | 14=14 ✓ | 15=15 ✓ | 18=18 ✓ |
| Pre-execution verification block (C-39) | ✓ | ✓ | ✓ | ✓ | ✓ |
| PASS/FAIL gate token protocol (C-40) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Numbered 4-step scan protocol (C-41) | ✓ detail | ✓ anchored | ✓ anchored | ✓ by-ref | ✓ detail |
| Dual gate + category labels (C-19, C-21) | ✓ | ✓ | ✓ | ✓ | ✓ |
| ENTRY/EXIT paired all phases (C-29) | ✓ | ✓ | ✓ | ✓ | ✓ |

**Note on V-04 C-41**: Phase 2 says "identical 4-step numbered protocol to V-01" rather than reproducing steps. The task preamble asserts all prior invariants are preserved; I accept this and mark PASS, but flag it as a production-use weakness.

C-30 (completion infrastructure): V-03/V-05 use typed assertions which the C-46 criterion explicitly blesses as a passing C-30 alternative.

**Result: All 42 baseline criteria (C-01–C-42) PASS for all five variations.**

---

### New v11 Criteria (C-43–C-48) — Per-Variation

#### C-43 — Role Architecture Block

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Standalone ROLE ARCHITECTURE table before phases; Signal Surveyor (rows only) / Org Architect (pivot only) hard split; typed `ROLE-HANDOFF: Signal-Surveyor → Org-Architect \| type: intra-P2 \| state: inventory-frozen \| rows: {N}` emit line; IVR-P2-R labeled triple; handoff distinguished from gate tokens by type tag |
| V-02 | **FAIL** | No ROLE ARCHITECTURE block; no ROLE-HANDOFF emit; no IVR-P2-R in manifest (TOTAL=16, no P2-R entry) |
| V-03 | **FAIL** | No ROLE ARCHITECTURE block; no handoff emit; manifest TOTAL=14 with no P2-R |
| V-04 | **FAIL** | No ROLE ARCHITECTURE block; scan protocol references V-01 but no role split; IVR-P2-A through P2-E only |
| V-05 | **PASS** | Standalone ROLE ARCHITECTURE block with full table; Signal Surveyor / Org Architect separation; typed handoff line identical format to V-01; IVR-P2-R in manifest; FORBIDDEN-STATES in ENTRY-P3 explicitly names "ROLE-HANDOFF emit absent from Phase 2 body" |

#### C-44 — Signal-Strength Provenance Propagation

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | No `signal-strength:` field on Phase 3 YAML entries; no IVR-P3-G; YAML template has only `detected-from:` |
| V-02 | **PASS** | IVR-P3-G states derivation rule explicitly: "signal-strength value is the Phase 2 Org Relevance rating for the row that generated this team"; YAML template shows `signal-strength: "[H\|M\|L -- derived from Phase 2 Org Relevance for this row]"` on every team entry; derivation rule not merely implied |
| V-03 | **FAIL** | No `signal-strength:` field; YAML template identical to V-01 |
| V-04 | **FAIL** | No `signal-strength:` field; V-04 axis is C-47/C-48 only |
| V-05 | **PASS** | IVR-P3-G states derivation rule; Phase 3 YAML shows `signal-strength: "[H\|M\|L -- Phase 2 Org Relevance for this row]"` on every team entry; P3 incompleteness predicate includes `signal-strength:` requirement; ENTRY-P3 REQUIRED-INPUTS names "pivot mode declared by Org Architect" reinforcing provenance chain |

#### C-45 — Amend Consequence Column

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Phase 4 uses bullet list (AMEND A/B/C with commands); no table; no Consequence column |
| V-02 | **PASS** | IVR-P4-B labeled triple with explicit VIOLATION (3-column table); 4-column table present: Option / Action / Command / Consequence; Consequence entries are phase-specific ("Phase 2 re-runs with new pivot; group structure regenerated from same inventory", "exec-office: name field updated; no phase re-run; groups unchanged", "Phase 3 re-runs with new grouping instruction; inventory unchanged") |
| V-03 | **FAIL** | Bullet list format (identical to V-01); no IVR-P4-B |
| V-04 | **FAIL** | Bullet list format (identical to V-01) |
| V-05 | **PASS** | IVR-P4-B present; 4-column table with Consequence column naming phase-specific downstream effects including ROLE-HANDOFF and Signal Surveyor inventory unchanged for AMEND C — more precise than V-02 |

#### C-46 — Typed Assertion Completion Format

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | YES/NO format throughout; no Assert:/Execute:/Verify:/Emit: prefixes |
| V-02 | **FAIL** | YES/NO format throughout |
| V-03 | **PASS** | Phrasing register declared at prompt top: "All completion test items in this prompt use typed assertion format: `{prefix}: {statement} -- PASS / FAIL`." Register internally consistent across all phases (P1: Emit:/Assert:, P2: Assert:/Verify:, P3: Verify:/Assert:/Emit:, P4: Assert:). No YES/NO items in any block. PASS/FAIL tokens at gate boundaries confirm vocabulary unification with C-40 |
| V-04 | **FAIL** | YES/NO format; no typed assertion register declaration |
| V-05 | **PASS** | PHRASING REGISTER block declared before phases; all completion test blocks use typed assertions; consistent with gate token vocabulary; no YES/NO mixing confirmed across all 4 phases |

#### C-47 — 3-Part ENTRY Block with FORBIDDEN-STATES

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Flat ENTRY blocks ("ENTRY-P1: No prerequisites. Phase 1 is the unconditional start." etc.); no REQUIRED-INPUTS / REQUIRED-STATES / FORBIDDEN-STATES sections |
| V-02 | **FAIL** | Flat ENTRY blocks |
| V-03 | **FAIL** | Flat ENTRY blocks |
| V-04 | **PASS** | All 4 phases have 3-part ENTRY blocks. P1: None/None/None (appropriate for unconditional start). P2: REQUIRED-INPUTS (Phase 1 all YES), REQUIRED-STATES (no YAML before this point), FORBIDDEN-STATES ("Phase 3 YAML template already written; pivot mode already selected outside Phase 2; inventory table already produced before Phase 1 EXIT"). P3: FORBIDDEN-STATES ("GATE-1 FAIL TOKEN present; pivot mode undeclared; inventory table absent"). P4: FORBIDDEN-STATES ("GATE-2 FAIL TOKEN present; draft org.yaml not yet produced"). Concrete, not placeholder |
| V-05 | **PASS** | All 4 phases have 3-part ENTRY blocks; P2 FORBIDDEN-STATES adds "ROLE-HANDOFF emit already present before Phase 2 begins"; P3 FORBIDDEN-STATES adds "ROLE-HANDOFF emit absent from Phase 2 body"; most precise FORBIDDEN-STATES of either variation — cross-references other structural elements (C-43) making the precondition surface richer |

#### C-48 — Inertia Framing

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | No inertia framing in opening; no `replaces:` in YAML header |
| V-02 | **FAIL** | No inertia framing |
| V-03 | **FAIL** | No inertia framing |
| V-04 | **PASS** | Opening names concrete failure mode: "The inertia competitor is tribal knowledge: org structure that is real but undocumented -- teams, roles, and group boundaries that exist only in people's heads, enforced only through institutional memory." YAML header carries `# replaces: undocumented tribal org structure`. IVR-P3-G triple explicitly requires both elements simultaneously; VIOLATION statement names failure modes for each element independently |
| V-05 | **PASS** | Opening identical inertia framing; YAML header has `# replaces: undocumented tribal org structure`; IVR-P3-H (separate triple from IVR-P3-G/signal-strength) covers the inertia framing as a distinct labeled constraint; Phase 3 incompleteness predicate explicitly lists `replaces:` among requirements; GATE-2 PASS token text includes "signal-strength + replaces: present" making both provenance and inertia frame gate-visible |

---

### Composite Scores

| Variation | C-01–C-42 | C-43 | C-44 | C-45 | C-46 | C-47 | C-48 | Total | % |
|-----------|-----------|------|------|------|------|------|------|-------|---|
| V-01 | 420 | +10 | — | — | — | — | — | **430** | 89.6% |
| V-02 | 420 | — | +10 | +10 | — | — | — | **440** | 91.7% |
| V-03 | 420 | — | — | — | +10 | — | — | **430** | 89.6% |
| V-04 | 420 | — | — | — | — | +10 | +10 | **440** | 91.7% |
| V-05 | 420 | +10 | +10 | +10 | +10 | +10 | +10 | **480** | 100% |

**Ranking**: V-05 > V-02 = V-04 > V-01 = V-03

---

### Excellence Signals from V-05

V-05 is the only variation to hit the maximum score (480/480). Patterns that differentiated it:

**1. Audit surface orthogonality — five independent compliance paths**
Each of C-39 (count arithmetic), C-43 (role boundary), C-44 (P2→P3 provenance chain), C-46 (typed assertions), C-48 (inertia frame in opening+YAML) covers a different failure mode class. No single omission collapses multiple audit paths. Compare V-02 (C-44+C-45 are correlated output-format criteria) — V-05 spreads coverage across pre-execution, intra-phase, output format, completion test, and framing layers.

**2. C-47 FORBIDDEN-STATES reference other structural elements**
V-05's ENTRY-P3 FORBIDDEN-STATES names "ROLE-HANDOFF emit absent from Phase 2 body" — a concrete cross-reference to C-43 structure. This means the 3-part ENTRY block (C-47) does dual duty: it enforces negative preconditions AND cross-validates C-43 compliance. V-04 has good FORBIDDEN-STATES but without the C-43 cross-reference.

**3. GATE-2 token text as multi-criterion convergence point**
V-05 GATE-2 PASS token: `"GATE-2 PASS -- all teams traced, signal-strength + replaces: present, org.yaml ready"` encodes both C-44 (signal-strength) and C-48 (replaces:) into the gate token text. A model scan of gate tokens alone surfaces the two Phase 3 provenance criteria without reading the phase body.

**4. Typed assertion vocabulary unification with gate tokens (C-46 × C-40 synergy)**
V-03 demonstrates C-46 in isolation. V-05 combines C-46 with C-40's existing PASS/FAIL vocabulary, so completion test assertions and gate boundary tokens share one evaluation register. This eliminates the register discontinuity that exists in V-01/V-02/V-04 (YES/NO in completion tests, PASS/FAIL at gates).

**5. IVR triple split for separate Phase 3 provenance concerns (IVR-P3-G and IVR-P3-H)**
V-05 gives signal-strength (C-44) its own IVR-P3-G and inertia framing (C-48) its own IVR-P3-H. V-04 assigns inertia framing to IVR-P3-G (conflating it with signal-strength in the labeling namespace). The split in V-05 means each criterion has an independent labeled triple, making each independently detectable via manifest scan.

---

```json
{"top_score": 480, "all_essential_pass": true, "new_patterns": ["Gate token text encodes multiple criterion requirements (signal-strength + replaces:) making Phase 3 compliance surface visible from gate scan alone", "FORBIDDEN-STATES cross-references other structural criteria (C-43 role handoff) creating inter-criterion precondition coupling that tightens compliance without adding new triples", "Separate IVR triple per Phase 3 provenance concern (IVR-P3-G for signal-strength, IVR-P3-H for inertia framing) keeps each criterion independently detectable via manifest scan"]}
```
