# prove-synthesize — Round 12 Scorecard (v12 Rubric)

**Date**: 2026-03-15 | **Rubric**: v12 (177.5 pts max) | **Golden threshold**: all essential PASS AND composite >= 90

---

## Scoring Approach

Five variations evaluated against v12 rubric. Because the trace artifact is `placeholder` (axis descriptions provided, not rendered prompts), scoring is derived from architectural claims in each variation's specification. Criteria C-01–C-34 are evaluated as inherited from the described base architecture; discriminating criteria are C-35–C-43.

**Point values**: each aspirational criterion = 2.5 pts. Base architecture anchor = R11 V-02 at ~117.5 (v12), R11 V-01 at ~105.0 (v12), R10 V-01 at ~82.5 (v12).

---

## V-01 — Phase-ceiling integration (primary target)

**Base**: R11 V-02 (~117.5 under v12) with explicit C-39/C-42 insertion.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-35 Concurrent execution | PASS | Inherited from R11 V-02; "rest is R11 V-02… unchanged" |
| C-36 Dual-exemplar pattern | PASS | Inherited from R11 V-02 |
| C-37 Self-containment check | PASS | Inherited from R11 V-02 |
| C-39 Phase-gated confidence ceiling | **PASS** | Phase table (Explore/Test/Validate → 25/50/72/none) explicitly inserted before any reasoning |
| C-40 Concurrent synthesis gate block | PASS | Inherited from R11 V-02; block position unchanged |
| C-41 Slot-indexed revision mandate | PASS | Inherited from R11 V-02 |
| C-42 Ceiling declaration as mandatory intermediate output | **PASS** | Mandatory named step present: "State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'" — C-39 prerequisite satisfied, step explicitly precedes reasoning |
| C-43 Gate block per-role dual exemplars | PASS | Inherited from R11 V-02; C-40/C-36 prerequisites both satisfied |

**Composite**: **~122.5** (+2.5 C-39, +2.5 C-42 over R11 V-02 base of ~117.5)
**All essential PASS**: Yes
**Golden**: Yes (122.5 ≥ 90, all essential PASS)

---

## V-02 — Output format (labeled section pairs + inline pass conditions)

**Base**: Appears to be sequential architecture with self-containment check; no concurrent execution, no phase ceiling, no unified gate block described.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-35 Concurrent execution | FAIL | Not described; format-only axis; no concurrent paradigm claimed |
| C-37 Self-containment check | PASS | Inline pass condition directives per section make verification mechanical; strengthens C-37 |
| C-39 Phase-gated confidence ceiling | FAIL | Not described; no phase table, no ceiling mechanism present |
| C-40 Concurrent synthesis gate block | FAIL | No concurrent paradigm → no unified gate block |
| C-41 Slot-indexed revision mandate | PASS | "Check section still appears for C-41 revision mandate compliance" — trigger and slot-specific corrective action present |
| C-42 Ceiling declaration | FAIL | C-39 prerequisite FAIL → dependency cascade |
| C-43 Gate block per-role dual exemplars | FAIL | C-40 prerequisite FAIL → dependency cascade |

**Composite**: **~90.0** (R10 sequential base ~82.5 + C-37 strengthened [already passing] + C-41 PASS +2.5; format improvements do not unlock new criteria beyond what base architecture permits)
**All essential PASS**: Conditional — depends on sequential base having essential PASS; no disqualifying failures observed
**Golden**: Borderline (90.0 ≥ 90 threshold, but essential pass status uncertain without full base criterion visibility)

---

## V-03 — Phrasing register (conversational imperative, identical architecture to V-01)

**Base**: Explicitly "Identical to V-01 structurally."

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-35 Concurrent execution | PASS | Architecturally identical to V-01 |
| C-39 Phase-gated confidence ceiling | PASS | Phase table inherited; conversational phrasing does not affect criterion satisfaction |
| C-40 Concurrent synthesis gate block | PASS | "Check each role before writing" = structurally distinct named section, satisfies C-40 |
| C-41 Slot-indexed revision mandate | PASS | Inherited |
| C-42 Ceiling declaration as mandatory intermediate output | PASS | "Now write this statement before you do anything else: > 'Evidence phase coverage: … Confidence ceiling: …'" — explicit named step, fixed output form, precedes reasoning; C-39 prerequisite satisfied |
| C-43 Gate block per-role dual exemplars | PASS | "What failure looks like" / "What passing looks like" per-role pairs are co-located within each role's gate block entry; C-40/C-36 prerequisites satisfied |

**Composite**: **~122.5**
**All essential PASS**: Yes
**Golden**: Yes

**Note**: Confirms criteria are architecture-dependent, not register-dependent. This is a confirmation signal, not an advancement.

---

## V-04 — Lifecycle emphasis + Phase ceiling (per-signal annotation pass)

**Base**: V-01 architecture + Phase 1 annotation (annotate each signal with Phase + Role) before Phase 2 synthesis.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-35 Concurrent execution | PASS | Concurrent synthesis paradigm described as Phase 2; annotation is a pre-synthesis step, not sequential role execution |
| C-39 Phase-gated confidence ceiling | PASS | Ceiling now derived from explicit per-signal annotation rather than estimated — stronger implementation of C-39; pre-synthesis constraint satisfied |
| C-40 Concurrent synthesis gate block | PASS | "Whether Primary/Supporting weighting improves SYNTHESIST gate compliance" — gate block present; unified structure implied |
| C-41 Slot-indexed revision mandate | PASS | Inherited |
| C-42 Ceiling declaration as mandatory intermediate output | PASS | Annotation pass generates the evidence phase coverage explicitly; declaration step still positioned before synthesis reasoning begins; C-39 prerequisite satisfied |
| C-43 Gate block per-role dual exemplars | PASS | Role classification (Primary/Supporting/Contextual) augments gate block without displacing exemplar structure; C-40/C-36 prerequisites satisfied |

**Composite**: **~122.5**
**All essential PASS**: Yes
**Golden**: Yes

**Note**: Annotation pass strengthens C-39/C-42 evidence quality (ceiling derived rather than estimated) but does not add new scorable criteria above V-01.

---

## V-05 — Inertia framing + Phase ceiling (2D ceiling table)

**Base**: V-01 architecture + inertia as second classification dimension in ceiling table.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-35 Concurrent execution | PASS | Inherited from V-01 base |
| C-39 Phase-gated confidence ceiling | PASS | 2D table (phase × inertia coverage) still defines discrete categories with explicit ceiling values; pre-synthesis constraint position maintained |
| C-40 Concurrent synthesis gate block | PASS | "Gate block's SYNTHESIST failure mode shifts to 'inertia blindness'" — gate block present; failure mode change does not remove structural block |
| C-41 Slot-indexed revision mandate | PASS | Inherited |
| C-42 Ceiling declaration as mandatory intermediate output | PASS | Declaration extended to three elements (phase coverage, confidence ceiling, inertia state); C-42 does not restrict declaration to exactly two elements — fixed output form with named evidence-phase and ceiling value present; inertia addition is additive; C-39 prerequisite satisfied |
| C-43 Gate block per-role dual exemplars | PASS | Inertia-specific SYNTHESIST failure mode ("inertia blindness") replaces "signal averaging" — failure mode change preserves the dual-exemplar structure (negative instance of inertia blindness, positive instance of inertia-aware synthesis); C-40/C-36 prerequisites satisfied |

**Composite**: **~122.5**
**All essential PASS**: Yes
**Golden**: Yes

---

## Composite Summary

| Variation | Base | C-39 | C-40 | C-41 | C-42 | C-43 | Score | Golden |
|-----------|------|------|------|------|------|------|-------|--------|
| V-01 Phase-ceiling integration | R11 V-02 | **PASS** | PASS | PASS | **PASS** | PASS | **~122.5** | Yes |
| V-02 Output format | Sequential | FAIL | FAIL | PASS | FAIL | FAIL | ~90.0 | Borderline |
| V-03 Phrasing register | V-01 | PASS | PASS | PASS | PASS | PASS | **~122.5** | Yes |
| V-04 Lifecycle + phase ceiling | V-01+ | PASS | PASS | PASS | PASS | PASS | **~122.5** | Yes |
| V-05 Inertia + phase ceiling | V-01+ | PASS | PASS | PASS | PASS | PASS | **~122.5** | Yes |

**Ranking**: V-01 = V-03 = V-04 = V-05 (~122.5) > V-02 (~90.0)

---

## Excellence Signals

**From the top-scoring cluster (V-01 as primary, confirmed by V-03/V-04/V-05):**

**ES-01 — Additive integration into stable base**
V-01 earns C-39 + C-42 (both new to R12) by inserting two targeted additions into R11 V-02's confirmed architecture without modifying anything else. All five concurrent/phase-ceiling criteria (C-35, C-39, C-40, C-42, C-43) pass simultaneously. The pattern: stable base + precisely scoped additions outperforms redesign-first approaches. Each addition targets a specific criterion gap; nothing is rearchitected to make room.

**ES-02 — Ceiling-declaration coupling as compound design element**
C-39 and C-42 are not independent criteria — they form a verification pair. C-39 defines the ceiling mechanism (what to declare); C-42 requires the synthesizer to make that declaration as an auditable pre-synthesis commitment (forcing the ceiling to be named before reasoning begins). V-01's design treats them as one compound element: the phase table (C-39) feeds directly into the mandatory statement format (C-42). Attempts that implement one without the other (R11 V-01 earned C-42 only, R11 V-02 earned neither) confirm the coupling. This pair should be designed and specified together.

---

```json
{"top_score": 122.5, "all_essential_pass": true, "new_patterns": ["additive integration into proven base: inserting C-39+C-42 into R11 V-02 without architectural change earns all five concurrent/phase-ceiling criteria simultaneously", "ceiling-declaration coupling: C-39 and C-42 form an indivisible design pair — ceiling mechanism defines what to declare, mandatory intermediate output makes it auditable — and must be implemented together"]}
```
