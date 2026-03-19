## validate-inertia Round 7 — Scorecard

### R7 Context

**Baseline entering R7:** V-30 scored 265/270. C-24, C-25, C-27 already pass. The sole gap: **C-26 links 3 and 4** (Phase 5(3) produces no named lever artifact; AMEND(d) uses phase reference "Phase 5(3)" instead of a named anchor).

**R7 target:** Close C-26 completely. Max = 270/270.

---

### Per-Variation Criterion Matrix

**Inherited from V-30 (all five variations):** C-01–C-25, C-27 = PASS. C-26 = PARTIAL (5 pts).

Only C-26 is in play for all five. Relevant sub-analysis below.

---

#### V-31 — Named Lever Artifact at Phase 5(3)

**C-26 analysis:**
- Link 1: Phase 1 "SCORING INFRASTRUCTURE DECLARED" → **PASS** (inherited V-30)
- Link 2: Phase 4 instruction: "Cite Phase 1 by reference -- the SCORING INFRASTRUCTURE DECLARED there is the named source" → **PASS** (inherited V-30)
- Link 3: Phase 5(3) requires "**LEVER POINT: [exact label]**" written on its own line → **PASS** (V-31 adds named artifact)
- Link 4: AMEND(d) requires "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3)]" → **PASS** (V-31 closes this link)

**C-26: PASS** (+5 over V-30 PARTIAL)

**C-27:** Rejection clause present: "Replace Part (3) with a more specific mechanism, rewrite the lever label, and repeat the falsifiability test." → **PASS** (preserved)

| Criterion | Score | Note |
|-----------|-------|------|
| C-01–C-05 (Essential) | 50/50 | All PASS |
| C-06–C-08 (Recommended) | 30/30 | All PASS |
| C-09–C-25 (Aspirational) | 170/170 | All PASS |
| C-26 | 10/10 | PASS — both links named with exact-copy artifacts |
| C-27 | 10/10 | PASS — rejection clause present |

**V-31 Total: 270/270**

---

#### V-32 — AMEND Lever Citation by Mechanism Name

**C-26 analysis:**
- Link 3: Phase 5(3) has no "LEVER POINT: [label]" requirement — produces prose only → chain link has no named artifact → **PARTIAL**
- Link 4: AMEND(d) requires naming the mechanism by description ("The absence of [lever mechanism name -- not 'Phase 5(3)']..."). Mechanism is named but drawn from prose, not from a formal named artifact → paraphrase chain → **PARTIAL**

**C-26: PARTIAL** (5 pts — same as V-30; the AMEND-side requirement alone does not close link 3)

**C-27:** Rejection clause: "Replace Part (3) with a more specific mechanism and repeat the falsifiability test." → **PASS**

| Criterion | Score | Note |
|-----------|-------|------|
| C-01–C-05 | 50/50 | PASS |
| C-06–C-08 | 30/30 | PASS |
| C-09–C-25 | 170/170 | PASS |
| C-26 | 5/10 | PARTIAL — link 3 has no named artifact; AMEND description is a paraphrase chain |
| C-27 | 10/10 | PASS |

**V-32 Total: 265/270**

---

#### V-33 — Citation Chain Verification Step

**C-26 analysis:**
- Link 3: Phase 5(3) still has no "LEVER POINT: [label]" requirement — produces prose. Verification table asks for "Phase 5(3) lever mechanism: [write the specific lever point]" — this retroactively names the mechanism in a verification record, but Phase 5(3) itself still produces no named artifact → the source is unnamed prose → **PARTIAL**
- Link 4: AMEND(d) instruction: "Name the mechanism from the chain verification, not reference Phase 5(3)" — the mechanism is named by copy from the verification table, not from a formal Phase 5(3) artifact. Correct content, but the upstream "artifact" is a verification slot, not a produced label → paraphrase chain at origin → **PARTIAL**

V-33 converts the chain requirement into a structural self-check, which improves detectability significantly — but the source link (Phase 5(3)) still has no named artifact, so any model completing the verification step correctly produces a paraphrase chain rather than a reference chain.

**C-26: PARTIAL** (5 pts)

**C-27:** "Replace Part (3) with a more specific mechanism and repeat the falsifiability test." → **PASS**

| Criterion | Score | Note |
|-----------|-------|------|
| C-01–C-05 | 50/50 | PASS |
| C-06–C-08 | 30/30 | PASS |
| C-09–C-25 | 170/170 | PASS |
| C-26 | 5/10 | PARTIAL — verification step retroactively names but Phase 5(3) has no produced named artifact |
| C-27 | 10/10 | PASS |

**V-33 Total: 265/270**

---

#### V-34 — Named Lever + AMEND Lever Citation (C-26 Full Chain)

**C-26 analysis:**
- Link 1: Phase 1 "SCORING INFRASTRUCTURE DECLARED" → **PASS**
- Link 2: Phase 4 trace cites "SCORING INFRASTRUCTURE DECLARED" by name → **PASS**
- Link 3: Phase 5(3) requires "**LEVER POINT: [exact label]**" → named artifact produced → **PASS**
- Link 4: AMEND(d) "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3)]" → exact label copied → **PASS**

All four links have named anchors. **C-26: PASS** (+5 over V-30)

**C-27:** Rejection clause present. → **PASS**

| Criterion | Score | Note |
|-----------|-------|------|
| C-01–C-05 | 50/50 | PASS |
| C-06–C-08 | 30/30 | PASS |
| C-09–C-25 | 170/170 | PASS |
| C-26 | 10/10 | PASS — both production requirements close both C-26 links |
| C-27 | 10/10 | PASS |

**V-34 Total: 270/270**

---

#### V-35 — Full Integration (All 19 Aspirationals)

**C-26 analysis:**
- Link 1: "SCORING INFRASTRUCTURE DECLARED" → **PASS**
- Link 2: Phase 4 traces cite it by name → **PASS**
- Link 3: Phase 5(3) produces "**LEVER POINT: [exact label]**" → **PASS**
- Link 4: AMEND(d) "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3) -- confirmed in Citation Chain Verification step (3)]" → **PASS**

Additionally: Citation Chain Verification step before AMEND requires all four links to be named explicitly, with a gate blocking AMEND if any link uses a phase reference. This is the strongest structural guarantee: a model that silently paraphrases at any link will fail the verification gate before AMEND is written.

**C-26: PASS** (strongest form — production + verification gate)

**C-27:** Rejection clause present → **PASS**

| Criterion | Score | Note |
|-----------|-------|------|
| C-01–C-05 | 50/50 | PASS |
| C-06–C-08 | 30/30 | PASS |
| C-09–C-25 | 170/170 | PASS |
| C-26 | 10/10 | PASS — named label + exact-copy citation + pre-AMEND verification gate |
| C-27 | 10/10 | PASS |

**V-35 Total: 270/270**

---

### Summary Table

| Variation | C-26 | Score | Rank |
|-----------|------|-------|------|
| V-31 | PASS | 270/270 | T-1 |
| V-34 | PASS | 270/270 | T-1 |
| V-35 | PASS | 270/270 | T-1 (structural ceiling) |
| V-32 | PARTIAL | 265/270 | 4 |
| V-33 | PARTIAL | 265/270 | 4 |

**Tiebreak among 270/270 variations:**
- **V-35** is the ceiling variation: three independent failure detection points (Phase 5(3) label, verification gate, AMEND anchor). A model that silently paraphrases at any link encounters the verification gate before AMEND.
- **V-34** = production requirements only; closes C-26 without the redundant confirmation gate.
- **V-31** closes C-26 via the same mechanism as V-34 but is framed as a single-axis test (the AMEND lever anchor was implicit, not the primary axis).

---

### Excellence Signals from V-35 (and shared by V-31/V-34)

**1. Named artifact label propagation via exact-copy requirement**
The phrase "copy the exact LEVER POINT label" is structurally different from "reference the lever mechanism." Exact copying is binary: the string either matches or it doesn't. A paraphrase is structurally visible as "not the exact label," making C-26 chain breaks detectable without requiring rubric judgment about whether content is "the same."

**2. Citation chain verification table as pre-terminal choke point**
Rather than distributing citation requirements across five phases (where any one can be silently violated), V-35 concentrates all four chain links into a single table that the model must complete before AMEND is unlocked. A failure at any link surfaces in one place. This converts a distributed auditing problem into a local gate — the model self-audits the entire chain in one pass.

**3. Self-rejection gate embedded between production and continuation**
The rejection clause in the falsifiability test ("If you cannot complete this sentence... replace Part (3)") forces mechanism specificity to be evaluated at write time rather than retrospectively. This pattern (write the test → can't complete it → replace what you wrote) is stronger than any external rubric check because it is structurally embedded in the output sequence.

---

### R7 Findings

- **AMEND-side citation alone (V-32) does not close C-26.** Without a named artifact at Phase 5(3), AMEND's mechanism-by-description produces a paraphrase chain, not a reference chain. Link 3 must be closed at production time.
- **Verification-step alone (V-33) does not close C-26.** The verification table names the mechanism retroactively, but Phase 5(3) still produces no formal artifact. A verification record is not an artifact.
- **Both sides must be closed simultaneously (V-31/V-34).** When Phase 5(3) produces a named label AND AMEND(d) copies that exact label, the citation chain becomes a reference chain at both links. Neither side alone is sufficient.
- **V-35 is the ceiling: production + verification guarantees both detectability and correctability.** A model that drifts at any chain link will self-diagnose in the verification step before writing AMEND.

```json
{"top_score": 270, "all_essential_pass": true, "new_patterns": ["Named artifact label propagation via exact-copy requirement makes paraphrase breaks structurally visible without rubric judgment", "Citation chain verification table as pre-terminal choke point concentrates distributed citation requirements into a single correctable gate"]}
```
