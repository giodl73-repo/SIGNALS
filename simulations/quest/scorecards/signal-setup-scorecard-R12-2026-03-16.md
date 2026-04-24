# Quest Score — signal-setup Round 12 (v11 Rubric)

## Scoring Baseline: R11 V-05 Under v11

Before scoring R12 variations, the R11 V-05 baseline must be recalibrated against v11. The stated "C-01..C-30 all PASS" was an optimistic pre-v11 estimate. C-32's cascade rule changes the calculus: GATE 6-Decline's fragment anchor ("The implementation phase — when you are writing.") **also fails C-21 and C-22** per C-32's explicit clause: "fails C-32 and also fails whichever of C-18/C-21/C-22 it was meant to satisfy."

Corrected R11 V-05 baseline under v11:

| Criterion | Status | Reason |
|-----------|--------|--------|
| C-21 | FAIL | GATE 6-Decline fragment → no assertable path-specific consequence |
| C-22 | FAIL | GATE 6-Decline fragment → phase vocabulary present but no extractable claim |
| C-31 | FAIL | Mixed: GATE 1A/1B/3A/6A letter-slot + GATE 1B-Abort/6-Decline word-suffix |
| C-32 | FAIL | GATE 6-Decline is "The implementation phase — when you are writing." — noun phrase + appositive |
| All others | PASS | Inherited from R10 V-05 + R11 structural work |

Corrected baseline score: 60 + 30 + (20/24 × 10) = **98.33**

---

## Variation Scoring

### V-01 — Axis A: C-31 Letter-Slot Uniform

**Axis**: Rename all word-suffix sub-gates to letter-slot only. GATE 1B-Abort → GATE 1C; GATE 6-Decline → GATE 6B. Consequence text unchanged.

**Spec Verification (provided text)**:

| Gate | Identifier | C-27 (heading)? | C-29 (routing block)? | Notes |
|------|-----------|-----------------|----------------------|-------|
| GATE 1 | `##` main gate | ✓ | ✓ — 3 explicit (condition, ID) pairs | Routes to 1A, 1B, or GATE 2 |
| GATE 1A | `###` sub-gate | ✓ | ✓ — Routes to GATE 3 or GATE 1C | |
| GATE 1B | `###` sub-gate | ✓ | — (EXIT path, no downstream routing needed) | Already-configured exit |
| GATE 1C | `###` sub-gate | ✓ | — (EXIT path) | Letter-slot ✓ |
| GATE 2 | `##` main gate | ✓ | n/a (PROCEED only) | |
| GATE 3 | `##` main gate | ✓ | ✓ — 2 explicit (condition, ID) pairs | |
| GATE 3A | `###` sub-gate | ✓ | — (PROCEED only) | |
| GATE 3B | `###` sub-gate | ✓ | — (EXIT path) | |
| GATE 4+ | inherited | ✓ (assumed) | ✓ (assumed from baseline) | GATE 6B fragment preserved |

**C-32 check — GATE 1C**: "Signal not configured. At the planning stage — before the next feature topic is named and the team decides whether to build — there will be no standing question in your context to ask 'why would teams do nothing instead?' Inertia has no named opponent here." → Subject + predicate + stated effect. **PASS.**

**C-32 check — GATE 3B**: "Signal not configured. At the planning stage — before the next feature topic is named and the spec is committed — there will be no standing instruction in Claude's context to ask 'why would teams do nothing instead?' Inertia remains unnamed in this workspace." → Complete sentence. **PASS.**

**C-32 check — GATE 6B**: Fragment preserved from R11. "The implementation phase — when you are writing." → Noun phrase + appositive. No predicate. No stated effect. **FAIL.** Cascades: **C-21 FAIL, C-22 FAIL.**

**C-23 check — GATE 6B**: "The implementation phase" is an explicit phase label even in the fragment. C-32 cascade covers C-18/C-21/C-22 only; C-23 is not in the cascade list. **PASS.**

**C-25 check**: All sub-gate identifiers now use letter-slot (1A, 1B, 1C, 3A, 3B, 6A, 6B). Each encodes parent gate number + branch slot. **PASS.**

**C-31 check**: Every sub-gate uses letter-slot. No word-suffix hyphen variants. **PASS.**

| Category | Criteria | Pass | Score |
|----------|----------|------|-------|
| Essential (C-01–C-05) | 5 | 5 | 60.00 |
| Recommended (C-06–C-08) | 3 | 3 | 30.00 |
| Aspirational (C-09–C-32) | 24 | 21 | 8.75 |
| **Total** | | | **98.75** |

FAIL: C-21, C-22, C-32

---

### V-02 — Axis B: C-31 Word-Suffix Uniform

**Axis**: Convert all sub-gate identifiers to pure word-suffix. GATE 1A → GATE 1-Missing, GATE 1B → GATE 1-Present, GATE 1C → GATE 1-Decline (or GATE 1-Abort), GATE 3A → GATE 3-Confirm, GATE 3B → GATE 3-Decline, GATE 6A → GATE 6-Present, GATE 6B → GATE 6-Decline. Fragment consequence text preserved.

**C-25 check**: Each identifier encodes the parent gate number (the digit before the hyphen) and a semantic branch descriptor. "A reader can determine which phase a sub-gate belongs to" — yes, the leading digit gives parent gate. "How many branches that phase has" — enumerable by counting identifiers with the same prefix. The rubric permits word-suffix when the scheme is uniform (C-31). **PASS.**

**C-31 check**: All word-suffix throughout. No letter-slot variants. **PASS.**

**C-32, C-21, C-22**: Same fragment at GATE 6-Decline as V-01. Same cascade failures. **FAIL (all three).**

| Category | Criteria | Pass | Score |
|----------|----------|------|-------|
| Essential | 5 | 5 | 60.00 |
| Recommended | 3 | 3 | 30.00 |
| Aspirational | 24 | 21 | 8.75 |
| **Total** | | | **98.75** |

FAIL: C-21, C-22, C-32

**Note on V-01 vs V-02**: Both score 98.75, confirming C-31 is scheme-agnostic — the uniformity constraint is satisfied equally by either convention. The choice between letter-slot and word-suffix has no rubric-visible consequence at this score level.

---

### V-03 — Axis C: C-32 Complete-Sentence Anchors (Subject-First)

**Axis**: Rewrite all consequence anchors as syntactically complete sentences with subject-first construction. Mixed identifier scheme preserved from R11 (GATE 1B-Abort word-suffix + GATE 6A letter-slot + GATE 6-Decline word-suffix).

**C-32 check — GATE 6 path**: Rewritten as complete sentence. Example construction: "Signal is not configured for Copilot interactions in this workspace; at the implementation stage — when Copilot is suggesting code — there is no inertia question present to challenge those suggestions before they are adopted." Subject + predicate + stated effect. **PASS.**

**C-21 check**: GATE 6 decline now carries a syntactically complete assertion with Copilot-specific future-moment framing. Path-specific, assertable. C-32 cascade no longer applies. **PASS.**

**C-22 check**: GATE 6 decline uses implementation-phase vocabulary ("implementation stage," "Copilot is suggesting code") while GATE 3B uses planning-phase vocabulary ("planning stage," "spec is committed"). Vocabulary sets non-overlapping. **PASS.**

**C-31 check**: Mixed scheme inherited from R11. GATE 1A/1B/3A/6A (letter-slot) coexist with GATE 1B-Abort/6-Decline (word-suffix). **FAIL.**

| Category | Criteria | Pass | Score |
|----------|----------|------|-------|
| Essential | 5 | 5 | 60.00 |
| Recommended | 3 | 3 | 30.00 |
| Aspirational | 24 | 23 | 9.58 |
| **Total** | | | **99.58** |

FAIL: C-31 only

---

### V-04 — A+C: Letter-Slot + Complete Sentences (Phase-First)

**Axis**: Both fixes applied. All sub-gate identifiers use letter-slot throughout. All consequence anchors rewritten as syntactically complete sentences using phase-first construction: "At the [phase], when [artifact condition], there is no [Signal capability] to [action]."

**C-31 check**: Uniform letter-slot throughout. **PASS.**

**C-32 check**: All anchors syntactically complete. Phase-first construction guarantees subject + predicate + stated effect. **PASS.**

**C-21 check**: GATE 6B decline carries complete Copilot-specific future-moment framing. Phase-first construction makes the path-specific anchor assertable. **PASS.**

**C-22 check**: Phase-first construction explicitly separates planning-phase vocabulary (GATE 3B: "At the planning stage, when the next specification is being drafted...") from implementation-phase vocabulary (GATE 6B: "At the implementation stage, when Copilot is proposing the first endpoint..."). Non-overlapping vocabulary sets confirmed by construction. **PASS.**

**C-23 check**: Phase label appears as the opening of each consequence anchor sentence, in subject/adverbial position. Explicit, not implied. **PASS.**

| Category | Criteria | Pass | Score |
|----------|----------|------|-------|
| Essential | 5 | 5 | 60.00 |
| Recommended | 3 | 3 | 30.00 |
| Aspirational | 24 | 24 | 10.00 |
| **Total** | | | **100.00** |

No FAIL criteria.

---

### V-05 — A+C+Adversary: Letter-Slot + Adversary-Named Complete Sentences + Routing Tables

**Axis**: Maximum combination. Uniform letter-slot identifiers. Consequence anchors name inertia as the active winning agent ("Inertia wins the next planning session; when a specification is committed..."). Explicit routing tables at GATE 1 and any multi-branch gates list every (condition, destination) pair in a single contiguous block.

**C-31 check**: Uniform letter-slot. **PASS.**

**C-32 check**: All anchors are complete sentences. "Inertia wins the next planning session; when a specification is committed in this workspace, there is no question standing in Claude's context to ask 'why would teams do nothing instead?'" — Subject (Inertia) + predicate (wins) + future-moment clause (complete). **PASS.**

**C-21 check**: "Inertia fills the next Copilot suggestion cycle; at the implementation stage, when code is being proposed in this workspace, there is no inertia question to challenge whether the feature is being built." Copilot-specific, path-local, assertable. **PASS.**

**C-22 check**: Planning-gate anchor vocabulary: "planning session," "specification is committed." Copilot-gate anchor vocabulary: "implementation stage," "code is being proposed," "Copilot suggestion cycle." Fully non-overlapping. **PASS.**

**C-29 check (reinforced)**: Routing tables at GATE 1 provide explicit structured enumeration:
```
| Condition                                         | Destination |
|---------------------------------------------------|-------------|
| CLAUDE.md does not exist                          | GATE 1A     |
| CLAUDE.md exists, Signal section present          | GATE 1B     |
| CLAUDE.md exists, no Signal section               | GATE 2      |
```
All branches named with conditions and gate IDs in a single contiguous block. C-29 was already PASS in baseline; V-05 maximizes the pattern. **PASS.**

**C-16 check (reinforced)**: Adversary-named anchors extend the preamble's framing into every consequence statement. Inertia is not only named as adversary in the preamble but appears as the grammatical subject winning at each decline. **PASS (reinforced).**

| Category | Criteria | Pass | Score |
|----------|----------|------|-------|
| Essential | 5 | 5 | 60.00 |
| Recommended | 3 | 3 | 30.00 |
| Aspirational | 24 | 24 | 10.00 |
| **Total** | | | **100.00** |

No FAIL criteria.

---

## Scoring Summary

| Variation | Essential | Recommended | Aspirational | Composite | All Essential? |
|-----------|-----------|-------------|--------------|-----------|----------------|
| V-01 (Letter-slot) | 5/5 | 3/3 | 21/24 | **98.75** | ✓ |
| V-02 (Word-suffix) | 5/5 | 3/3 | 21/24 | **98.75** | ✓ |
| V-03 (Complete sentences) | 5/5 | 3/3 | 23/24 | **99.58** | ✓ |
| V-04 (A+C phase-first) | 5/5 | 3/3 | 24/24 | **100.00** | ✓ |
| V-05 (A+C+Adversary) | 5/5 | 3/3 | 24/24 | **100.00** | ✓ |

**Ranking**: V-04 = V-05 (100.00) > V-03 (99.58) > V-01 = V-02 (98.75)

---

## Criterion Delta Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-21 | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-22 | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-31 | PASS | PASS | **FAIL** | PASS | PASS |
| C-32 | **FAIL** | **FAIL** | PASS | PASS | PASS |
| All others | PASS | PASS | PASS | PASS | PASS |

---

## Excellence Signals

**From V-04/V-05 (co-winners at 100.00)**:

1. **C-32 + C-21 + C-22 are entangled — fixing one fixes three.** The fragment anchor at GATE 6B failed three criteria simultaneously. Rewriting as a complete sentence unlocked all three. This confirms that C-32 is not an independent aspirational criterion — it is a prerequisite gate for C-21/C-22 on optional extension paths.

2. **C-31 carries less weight than C-32 (1 criterion vs. 3-criterion cascade).** V-03 (C-31 FAIL only) scores 99.58 while V-01/V-02 (C-32 FAIL cascading to C-21/C-22) score 98.75. A single fragment anchor cost more points than the entire identifier-uniformity failure.

3. **Adversary-win framing (V-05) is rubric-equivalent to phase-first framing (V-04) but qualitatively stronger.** Both achieve 100.00. V-05's "Inertia wins the next planning session; when..." gives the adversary grammatical agency as subject. V-04's "At the planning stage, when... there is no question..." leaves inertia unnamed in the sentence itself. The rubric's current criteria cannot distinguish them.

---

## New Patterns

**Pattern — Adversary-win framing in consequence anchors (C-16 extension gap)**

V-04 and V-05 both score 100. The distinguishing feature of V-05 — naming inertia as the grammatical subject that wins at decline gates — is not captured by any current criterion. C-16 requires inertia to be named as adversary in the preamble. C-14/C-18 require naming what is absent and anchoring it to a future moment. None require the adversary to appear as the active winning agent in the consequence anchor sentence itself.

"At the planning stage, when a specification is committed, there is no standing question..." (V-04) satisfies all criteria.
"Inertia wins the next planning session; when a specification is committed, there is no standing question..." (V-05) also satisfies all criteria — and delivers a measurably stronger consequence argument.

Candidate criterion: *Consequence anchors at decline gates name inertia as the grammatical subject winning the phase — not merely as an absent concept — so that every Signal-absent exit reinforces the adversarial framing established in the preamble.*

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Consequence anchors at decline gates should name inertia as the grammatical subject winning the phase ('Inertia wins the next planning session; when...') rather than merely noting absence ('there is no standing question'). C-16 requires adversary framing in the preamble; no criterion requires adversary-win framing in decline-path consequence anchors. V-04 and V-05 both score 100 but V-05's construction is measurably stronger. Candidate criterion: every Signal-absent decline anchor names inertia as the active winner, not only as the unnamed gap."]}
```
