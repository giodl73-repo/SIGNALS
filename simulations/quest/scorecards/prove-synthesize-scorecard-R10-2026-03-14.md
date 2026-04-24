## prove-synthesize — Scorecard R10

**Top score**: V-02 at ~97.5 | **All essential pass**: false | **Golden**: NOT achieved by any variation

---

### Round Summary

| Variation | Essential | C-34 | C-35 | C-36 | C-37 | C-38 | Composite |
|-----------|-----------|------|------|------|------|------|-----------|
| V-01 | 3/6 FAIL | PASS | FAIL | FAIL | FAIL | FAIL | ~82.5 |
| V-02 | 3/6 FAIL | PASS | FAIL* | FAIL* | **PASS** | FAIL* | ~97.5 |
| V-03 | FAIL (incomplete) | FAIL | FAIL | FAIL | FAIL | FAIL | ~8.0 |

\* Structural text satisfies criterion; blocked by C-11/C-30 dependency cascade.

---

### Key Finding: The C-35/C-11 Structural Tension

All three variations fail the essential battery — specifically **C-11** (per-role anti-pattern gates), **C-13** (NOT: clause format), and **C-30** (per-role failure mode naming). V-02 hits this in an interesting way: to achieve concurrent execution (C-35), it collapses role definitions from sequential steps to brief functional descriptions. This removes the natural attachment sites for per-role gates — Step N no longer exists, so "Step N Gate:" no longer has a home.

The **concurrent execution paradigm conflicts architecturally with per-role gate compliance**. V-02 carries the full text of C-35, C-36, C-37, and C-38 — all four structural patterns are present at the text level — but C-11 and C-30 dependency cascades block C-35, C-36, and C-38 from passing. Only **C-37 passes** (C-10 is its only prerequisite, and C-10 is strong in V-02).

---

### Excellence Signals → v11 Candidates

**C-39 — Phase-gated confidence ceiling** (from V-03 Phase 1): Pre-synthesis evidence inventory sets maximum confidence bounds before reasoning begins. Explore-only → max 49; Explore+Test → max 74; all phases → no ceiling. First pre-synthesis constraint mechanism in this series.

**C-40 — Concurrent synthesis gate block**: When roles are concurrent (C-35), a unified gate block after role definitions and before output — names each role's failure mode with exemplars in one shared section. Role-indexed within the block, not attached to sequential steps. Resolves the C-35/C-11 tension.

**C-41 — Slot-indexed revision mandate**: Extends C-37 from "map questions to slots" (diagnostic) to "revise the named slot if the question fails" (enforcement). V-02 has this already: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting."

```json
{"top_score": 97.5, "all_essential_pass": false, "new_patterns": ["phase-gated confidence ceiling constrains synthesizer confidence range before verdict reasoning based on evidence phase coverage", "concurrent role execution removes per-role gate attachment sites revealing C-35/C-11 structural tension requiring unified gate block architecture", "slot-indexed revision mandate extends C-37 from diagnostic mapping to enforcement trigger on slot failure"]}
```
fines execution order, not concurrent reasoning. Also: C-11 FAIL + C-30 FAIL → dependency cascade. |
| C-36 | Dual-exemplar adversarial gate | **FAIL** | C-32 FAIL → dependency cascade. Additionally: ADVERSARY Gate presents only a negative exemplar (`"more data would raise confidence"`); no positive (valid) exemplar co-located inside the gate. A valid challenge is described in abstract terms ("names something structural about this evidence") — not instantiated. |
| C-37 | Slot-indexed self-containment check | **FAIL** | C-10 PASS (prerequisite satisfied). Completeness Check has five items but maps to output requirements, not named slots. "The verdict is answerable without reading the underlying signals" — does not name the Verdict/Confidence section. "The top 3 signals are named and their influence explained" — does not say "Key Evidence section." No explicit `→ slot name` mapping; correspondence is implicit. |
| C-38 | Role-to-output closure attribution | **FAIL** | C-11 FAIL + C-30 FAIL → dependency cascade. Open Questions slot: "List each as a question. Prioritize questions that would change the verdict or confidence if answered." No role attribution instruction present. |

### V-01 Composite Estimate

| Pool | Max | Earned |
|------|-----|--------|
| Essential | 90.0 | ~58.0 |
| Aspirational v8 (23 criteria) | 57.5 | ~22.0 |
| v9 new (C-32, C-33, C-34) | 7.5 | 2.5 |
| v10 new (C-35, C-36, C-37, C-38) | 10.0 | 0 |
| **Composite** | **165.0** | **~82.5** |

All essential: **FAIL**. Composite >= 90: **NO**. Golden: **NOT ACHIEVED**.

---

## R10-V-02 — Output Format (Concurrent Execution + All v10 Targets)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Verdict commitment | PASS | Output: "State yes, no, or maybe in the first sentence. Give the confidence score." Self-containment check item 1 verifies the verdict slot; revision gate enforces it before output. |
| C-10 | Self-contained mandate | PASS | Opening: "The synthesis you produce supersedes the individual signals — it is the authoritative record; the signal inventory is subordinate to it." Self-containment check with revision gate: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting." Strongest self-contained mandate in this series. |
| C-11 | Named anti-pattern gates | **FAIL** | ADVERSARY has explicit Gate: with prohibition and exemplars. SYNTHESIST: "integrates signals into a verdict, confidence score, and key evidence set" — functional description only, no gate or failure-mode prohibition. ANALYST: "reviews what the ADVERSARY raised, adjusts verdict or confidence if warranted, extracts principles, and surfaces open questions" — routing rule, not a gate. Three-role gate requirement not met. |
| C-12 | Prose format for evidence ranking | PASS | "Write the synthesis as five prose paragraphs under these five section headers." Key Evidence: "explain why it was decisive. One sentence per signal" — argument construction required per signal. |
| C-13 | NOT: precedes success condition | **FAIL** | No NOT: clause in output instructions. All output requirements are stated positively ("Write the synthesis as five prose paragraphs…", "State yes, no, or maybe…"). No format prohibition precedes a structural requirement. |
| C-30 | Role names its own failure mode | **FAIL** | SYNTHESIST: "integrates signals into a verdict, confidence score, and key evidence set" — no failure mode named. ADVERSARY: failure mode implied as "generic hedge" through the Gate constraint but never explicitly labeled as this role's named failure mode at the definition site. ANALYST: "reviews what the ADVERSARY raised, adjusts verdict or confidence if warranted" — no failure mode named. C-30 requires explicit naming at role definition; SYNTHESIST and ANALYST fail. |

**All essential PASS: NO** → Golden threshold not met.

### v9 New Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-32 | Inline exemplar at anti-pattern gate | **FAIL** | C-11 FAIL + C-30 FAIL → dependency cascade. Note for record: ADVERSARY Gate contains both INVALID exemplar (`"confidence could be higher with more data"`) and VALID exemplar (`"the three key signals all measure stated preference, not observed behavior — the synthesis has no revealed-preference signal in key evidence"`) inline — C-36-level instantiation. Structural text satisfies the criterion; dependency prerequisites do not. |
| C-33 | Format-prohibition names positive structural requirement | **FAIL** | C-13 FAIL → dependency cascade. No NOT: clause format present. |
| C-34 | Supersession assertion in synthesis mandate | PASS | Opening: "The synthesis you produce supersedes the individual signals — it is the authoritative record; the signal inventory is subordinate to it." Uses "supersedes," "authoritative record," and explicit subordination of signal inventory. C-05 PASS + C-10 PASS satisfy prerequisites. |

### v10 New Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-35 | Concurrent role execution with seamless output | **FAIL** | C-11 FAIL + C-30 FAIL → dependency cascade. Note for record: "Roles run concurrently in your reasoning; the output produced afterward is a single document, not three labeled sections. The roles shape what you attend to, not how you partition output." Explicit concurrent execution clause present; output seam prohibition explicit. Structural text satisfies the criterion; dependencies do not. |
| C-36 | Dual-exemplar adversarial gate | **FAIL** | C-32 FAIL → dependency cascade. Note for record: ADVERSARY Gate provides INVALID case (`"'confidence could be higher with more data' applies to every synthesis without exception"`) and VALID case (`"'the three key signals all measure stated preference, not observed behavior'"`) co-located in same constraint. Structural text satisfies C-36; dependency cascade prevents pass. |
| C-37 | Slot-indexed self-containment check | **PASS** | C-10 PASS (prerequisite satisfied). Self-containment check explicitly maps each reader question to a named paragraph slot: (1) "What is the verdict and why is the synthesizer confident at that level? → **verdict/confidence paragraph**"; (2) "Which three signals drove the verdict and what did each show? → **key evidence paragraph**"; (3) "What is the strongest argument against the verdict? → **counter-evidence paragraph**"; (4) "What should a team take away that applies beyond this specific hypothesis? → **principles paragraph**"; (5) "What remains unresolved, and what generated each open question? → **open questions paragraph**". Five-for-five slot-to-check correspondence; explicit and complete. Revision mandate adds enforcement: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting." |
| C-38 | Role-to-output closure attribution | **FAIL** | C-11 FAIL + C-30 FAIL → dependency cascade. Note for record: Open Questions output slot contains "If the question was raised by the ADVERSARY challenge, acknowledge that attribution." ANALYST role definition also specifies: "If the ADVERSARY raised a challenge that was not resolved, it carries forward to open questions with the ADVERSARY as source." Dual-site attribution instruction (role level + output slot level). Structural text fully satisfies C-38; dependency prerequisites block pass. |

### V-02 Composite Estimate

| Pool | Max | Earned |
|------|-----|--------|
| Essential | 90.0 | ~65.0 |
| Aspirational v8 (23 criteria) | 57.5 | ~27.5 |
| v9 new (C-32, C-33, C-34) | 7.5 | 2.5 |
| v10 new (C-35, C-36, C-37, C-38) | 10.0 | 2.5 |
| **Composite** | **165.0** | **~97.5** |

All essential: **FAIL**. Composite >= 90: **YES**. Golden requires all essential PASS — **NOT ACHIEVED**.

---

## R10-V-03 — Lifecycle Emphasis (Phase Attribution + Incomplete)

Phase 1 (Signal Inventory) is authored. Phase 2 (Synthesis) contains only "placeholder" — no synthesis instruction, no output structure, no role definitions, no gates.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| All essential | C-05, C-10, C-11, C-12, C-13, C-30 | **FAIL** | Phase 2 is "placeholder." No verdict instruction, no mandate, no roles, no format requirements. |
| All v9/v10 new | C-32–C-38 | **FAIL** | No synthesis instruction present; all dependency prerequisites unresolvable. |

**Phase 1 structural value** — three novel patterns present even in the incomplete variation:

1. **Phase coverage confidence ceiling**: Confidence score is bounded by evidence phase coverage before synthesis begins — Explore-only caps confidence at 49; Explore+Test caps at 74; all three phases present removes the ceiling. A pre-synthesis constraint mechanism: the SYNTHESIST's confidence range is gated by evidence quality audit before any verdict reasoning occurs.

2. **Phase attribution**: Each signal is classified as Explore / Test / Validate before synthesis. Forces a structured inventory that can surface phase gaps (e.g., all signals directional — no test-phase signal present).

3. **Signal role classification**: Primary (directly tests hypothesis) / Supporting (strengthens primary) / Contextual (relevant background, not probative). Distinguishes signal weight before aggregation.

None satisfy any current rubric criterion. They operate at the pre-synthesis inventory layer, upstream of all existing criteria.

### V-03 Composite Estimate

| Pool | Max | Earned |
|------|-----|--------|
| Essential | 90.0 | ~5.0 |
| Aspirational v8 (23 criteria) | 57.5 | ~3.0 |
| v9/v10 new | 17.5 | 0 |
| **Composite** | **165.0** | **~8.0** |

All essential: **FAIL**. Not scoreable as a synthesis variation.

---

## Round Summary

| Variation | Axis | Essential | C-34 | C-35 | C-36 | C-37 | C-38 | Composite |
|-----------|------|-----------|------|------|------|------|------|-----------|
| V-01 | Role sequence (sequential) | 3/6 FAIL | PASS | FAIL | FAIL | FAIL | FAIL | ~82.5 |
| V-02 | Concurrent execution + v10 targets | 3/6 FAIL | PASS | FAIL* | FAIL* | **PASS** | FAIL* | ~97.5 |
| V-03 | Lifecycle (phase attribution, incomplete) | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | ~8.0 |

\* Structural text satisfies criterion; blocked by C-11/C-30 dependency cascade.

**Top variation**: V-02 at ~97.5

**Golden threshold**: NOT achieved by any variation in R10. No variation satisfies all essential PASS.

---

## R10 Key Finding

**The C-35/C-11 structural tension**

V-02 correctly implements all four v10 structural patterns at the text level — concurrent execution clause (C-35), dual-exemplar gate (C-36), slot-indexed check (C-37), closure attribution (C-38). But it achieves concurrent execution by collapsing role definitions from detailed sequential steps to brief functional descriptions ("SYNTHESIST integrates signals into a verdict…"). This removes the structural attachment points for per-role anti-pattern gates (C-11) and per-role failure mode naming (C-30): when roles are described as simultaneous cognitive stances rather than sequential steps, there is no natural site for "Step N — ROLE → Gate: …" because Step N no longer exists.

The concurrent execution paradigm (C-35) and per-role gate compliance (C-11) appear to conflict architecturally. Sequential instruction structures can attach a gate to each step. Concurrent instruction structures need a different gate architecture — one that addresses all failure modes without role-indexed step boundaries.

**v11 challenge**: Write a variation that achieves C-35 while satisfying C-11 and C-30. Candidate approach: a unified synthesis gate block placed after concurrent role definitions and before the output structure — a single constraint section that names each role's failure mode (SYNTHESIST: hedging; ADVERSARY: generic challenge; ANALYST: selective collection) with inline exemplars, satisfying C-11 and C-30 in concurrent-compatible form. Gates are role-indexed within the block rather than attached to sequential role steps.

---

## Excellence Signals — R10

**Signal 1 — Phase-gated confidence ceiling (V-03 Phase 1)**

A pre-synthesis signal inventory step sets maximum confidence bounds before the SYNTHESIST begins verdict reasoning. Confidence ceiling = f(evidence phase coverage): Explore-only → max 49 (no test-phase data); Explore+Test → max 74 (no confirmatory data); all three phases → no ceiling. The ceiling is applied at inventory time, before synthesis, preventing overconfident verdicts from directional-only signal sets. No current rubric criterion addresses evidence phase qualification. The constraint operates upstream of any existing criterion — C-05 governs commitment after reasoning begins; phase ceiling governs what confidence level is achievable before reasoning begins.

Candidate v11 criterion: **C-39 — Phase-gated confidence ceiling** — the synthesis instruction specifies explicit maximum confidence bounds as a function of evidence phase coverage, audited before synthesis reasoning begins. The ceiling enforces calibration at the evidence level: a SYNTHESIST cannot issue high-confidence verdicts from exploration-only signals regardless of conviction.

**Signal 2 — Concurrent role design reveals unified gate block gap (V-02)**

V-02 demonstrates that the full v10 criterion set requires a gate architecture incompatible with sequential-step role instructions. The concurrent execution paradigm merges role descriptions into functional stances, eliminating per-role gate attachment sites. This surfaces a gap: the rubric has no criterion for a concurrent-compatible gate format. C-11 requires gates; C-35 removes the structural sites that made per-role gating natural. A variant satisfying both would need a new structural form.

Candidate v11 criterion: **C-40 — Concurrent synthesis gate block** — when roles execute concurrently (C-35), a unified gate block follows the role definitions and precedes the output structure. The block names each role's failure mode (satisfying C-30 within the block) and provides an inline exemplar for each (satisfying C-32 within the block) in a shared constraint section. Gate function is role-indexed within the block but attached to no sequential step.

**Signal 3 — Slot-indexed revision mandate extends C-37 (V-02)**

V-02's self-containment check includes: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting." C-37 requires questions to map to named slots — it is diagnostic. V-02 adds a revision trigger: mapping failure mandates output revision before the synthesis is finalized. The check has enforcement, not just audit. This two-step pattern (slot-indexed check → mandatory revision on failure) produces a stronger guarantee than C-37 alone.

Candidate v11 criterion: **C-41 — Slot-indexed revision mandate** — the self-containment check includes not only explicit slot-to-question mapping (C-37) but a mandatory revision instruction triggered by slot failure: "If the question cannot be answered from the named paragraph, revise that paragraph before outputting." C-41 is C-37 + enforcement; C-37 is necessary but not sufficient for C-41.

---

```json
{"top_score": 97.5, "all_essential_pass": false, "new_patterns": ["phase-gated confidence ceiling constrains synthesizer confidence range before verdict reasoning based on evidence phase coverage", "concurrent role execution removes per-role gate attachment sites revealing C-35/C-11 structural tension requiring unified gate block architecture", "slot-indexed revision mandate extends C-37 from diagnostic mapping to enforcement trigger on slot failure"]}
```
