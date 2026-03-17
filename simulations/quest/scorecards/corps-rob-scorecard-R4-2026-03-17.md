I now have full context on all 5 R4 variations and the complete v3 rubric. Let me score them.

---

# Scorecard — corps-rob R4 (rubric v3)

## Scoring Formula (v3)

| Band | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 – C-05 | 5 × 12 = 60 |
| Recommended | C-06 – C-08 | 3 × 10 = 30 |
| Aspirational | C-09 – C-15 | N/7 × 10 |

PARTIAL = 0.5 pass. Ceiling = 100.

---

## V-01 — Compressed Stage-Open Context

**Base**: V-04 R3 (100). Part 1 replaced with a 3-field Stage-Open Context (CONCERN, FORWARDED, INERTIA) + "Lens filter rule" instruction block. All other mechanisms preserved: global anchor, inertia check, cross-stage references in findings, handoff packet with explicit "Must add substance" anti-copy guard, cross-cutting themes.

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Canonical six stage headers + role title in each section. |
| C-02 | PASS | "Lens filter rule" instruction with role-specific examples (TPM → schedule, PM → adoption, Arch → coupling). Stage 2+ requires ≥1 finding addressing the forwarded concern through this role's lens. |
| C-03 | PASS | Stage header, role identity, numbered findings with HIGH/MED/LOW, explicit VERDICT token per stage. |
| C-04 | PASS | Minimum 2 findings per stage, each carries Owner + Resolution. |
| C-05 | PASS | Go/No-Go section in TPM stage with structured labeled statement + F-ID or R-ID rationale. |

All 5 essential: **PASS**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Risk Register table (≥3 entries, ≥1 HIGH/HIGH or HIGH/MED). |
| C-07 | PASS | Mission Cascade table with named mission, ALIGNED/PARTIAL/GAP verdict. |
| C-08 | PASS | Cross-Stage References (min 1 per stage, findings body) + CROSS-STAGE SYNTHESIS in handoff (min 5 entries for 6-stage run). |

All 3 recommended: **PASS**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER: YES/NO field in every handoff packet, naming F-ID + downstream stage + reason. |
| C-10 | PASS | Cross-Cutting Themes section (Section A) at end-of-run, min 2 themes with >=2 F-IDs from different stages. |
| C-11 | PASS | Dedicated Handoff Packet (PASSING TO NEXT STAGE + CROSS-STAGE SYNTHESIS + BLOCKER) at every stage close. |
| C-12 | PASS | BLOCKER field at each stage boundary. |
| C-13 | PASS | INERTIA ANCHOR before Stage 1. INERTIA CHECK (per-stage identity, Part 2) at all 6 stages. |
| C-14 | **PARTIAL** | Stage-Open Context block IS present before findings (structural location ✓, instruction to filter by lens ✓). Fails minimally: no explicit "Lens:" output field naming the orientation dimension in the output — the "Lens filter rule" describes how to filter but the output does not contain a dedicated lens-declaration field. The CONCERN entry (one F-ID) satisfies (2) minimally; (1) "names the reviewing role's lens explicitly" is only implied through the role title in the header and the filter rule instruction, not through a lens-declaration output. Compare V-04 R3's KEY CONCERNS multi-row table and V-04 R4's explicit "Lens:" fill field. |
| C-15 | PASS | "Must add substance not already stated in the Cross-Stage References section above." Explicit negative guard in handoff packet template. |

Aspirational: 6.5/7

### Composite

```
(5/5 × 60) + (3/3 × 30) + (6.5/7 × 10)
= 60 + 30 + 9.3
= 99.3
```

---

## V-02 — Structural Field Separation

**Base**: V-04 R3 (100). Keeps full 4-field briefing envelope (C-14 unchanged). Replaces field names: `### Prior-Stage Lens Impact` in findings (question: how does this role's orientation change the reading of a prior finding?) + `DOWNSTREAM RISK SHIFT:` in handoff packet (question: what failure mode or ownership gap becomes visible at this stage?). Adds "do not copy the lens impact into the risk shift" as negative constraint in PART 4 preamble.

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Six canonical stage headers + role title per stage. |
| C-02 | PASS | Full briefing envelope forces lens-directed key concerns selection. Per-stage lens impact section grounds findings in role orientation. |
| C-03 | PASS | All four structural elements per stage. |
| C-04 | PASS | Min 2 findings per stage with owner + resolution. |
| C-05 | PASS | Go/No-Go section in TPM stage. |

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Risk Register table ≥3 entries. |
| C-07 | PASS | Mission Cascade table with named mission. |
| C-08 | PASS | Prior-Stage Lens Impact (min 1 per stage, names source stage + F-ID + relationship) + DOWNSTREAM RISK SHIFT in packet (min 5 for 6-stage run). Both satisfy "names source stage, finding ID, confirms/escalates/contradicts." |

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER field at each stage close. |
| C-10 | PASS | Cross-Cutting Themes section present (Section A end-of-run). |
| C-11 | PASS | Handoff Packet (DOWNSTREAM RISK SHIFT entries) at every stage close. Min 5 entries for 6-stage run. |
| C-12 | PASS | BLOCKER: YES/NO at each stage boundary. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK per stage. |
| C-14 | PASS | Full 4-field briefing envelope: PRIOR STAGE SUMMARY, KEY CONCERNS (multi-row, lens-directed, "Generic selection fails"), OPEN QUESTION FORWARDED, INERTIA STATUS. Present at stage open before findings. Names role's lens in envelope header and KEY CONCERNS instruction. |
| C-15 | PASS | "Do not copy the lens impact into the risk shift" in PART 4 preamble. Explicit negative constraint. Structural field separation (different questions) supplements but does not replace the explicit guard. C-15 pass condition: "explicit anti-redundancy instruction or demonstrates non-redundant synthesis" — satisfied. |

Aspirational: 7/7

### Composite

```
(5/5 × 60) + (3/3 × 30) + (7/7 × 10)
= 60 + 30 + 10
= 100
```

---

## V-03 — Inertia Escalation Track

**Base**: V-04 R3 (100). Adds INERTIA EVOLUTION field to briefing envelope (how displacement posture has shifted since Stage 1, tied to specific F-ID); INERTIA STAGE READING to stage identity (how this role reads current posture given evolution state); new end-of-run SECTION B — INERTIA TRAJECTORY (6-row table: stage → hardened/softened/unchanged, NET DISPLACEMENT POSTURE, KEY TURNING POINT). Preserves all V-04 R3 mechanisms including full briefing envelope, Cross-Stage References + explicit "Must add substance" CROSS-STAGE SYNTHESIS, Cross-Cutting Themes.

### Essential Criteria

All 5: **PASS** (identical to V-04 R3 base; additions do not touch essential structure).

### Recommended

All 3: **PASS**
- C-08 PASS (strong): Cross-Stage References + CROSS-STAGE SYNTHESIS + briefing envelope chain — three independent coherence mechanisms.

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER field at each stage close. |
| C-10 | PASS | Cross-Cutting Themes section (Section A). |
| C-11 | PASS | Handoff Packet with CROSS-STAGE SYNTHESIS at every stage close. |
| C-12 | PASS | BLOCKER field at every stage boundary. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK + INERTIA STAGE READING per stage. Exceeds C-13 pass condition. |
| C-14 | PASS | Full 4-field briefing envelope preserved from V-04 R3 base; INERTIA EVOLUTION replaces INERTIA STATUS as 4th field. KEY CONCERNS multi-row with lens direction ✓. Stage-open position before findings ✓. |
| C-15 | PASS | "Must add substance not already stated in the Cross-Stage References section above" explicit instruction in CROSS-STAGE SYNTHESIS. Preserved from V-04 R3. |

Aspirational: 7/7

### Composite

```
= 100
```

---

## V-04 — V-05 R3 Base + Minimal C-14 + Structural C-15

**Base**: V-05 R3 (97.1 under v3 — fails C-14 and C-15). Minimal 3-section design upgraded with: (1) 4-field STAGE-OPEN FORWARD block prepended to Section 1 for Stage 2+ (CONCERN, FORWARDED, INERTIA, Lens); (2) `### Prior-Stage Reading` subsection in Section 2 findings; (3) `DOWNSTREAM SIGNIFICANCE:` in handoff packet + "Do not copy the Prior-Stage Reading into Downstream Significance" in OUTPUT RULE.

### Essential Criteria

All 5: **PASS**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Risk Register table. |
| C-07 | PASS | Mission Cascade table. |
| C-08 | PASS | Prior-Stage Reading (Section 2) provides backward cross-stage citations; DOWNSTREAM SIGNIFICANCE in packet (min 5 for 6-stage run) provides handoff entries. |

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER field in handoff packet. |
| C-10 | PASS | Cross-Cutting Themes section (Section A end-of-run). |
| C-11 | PASS | Handoff Packet (DOWNSTREAM SIGNIFICANCE entries) at every stage close. |
| C-12 | PASS | BLOCKER: YES/NO per stage. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK in Section 1 stage identity. |
| C-14 | PASS | STAGE-OPEN FORWARD has 4 fields: CONCERN (one role-filtered F-ID), FORWARDED (verbatim quote — allowed, same as V-04 R3's OPEN QUESTION FORWARDED), INERTIA (one clause), and crucially **Lens: [...]** — a mandatory output field that forces the model to declare which orientation dimension it will apply before findings begin. This satisfies C-14(1) "names the reviewing role's lens explicitly" via the Lens field output (unlike V-01's instruction-only form). C-14(2) one role-filtered concern present. C-14(3) explicit "Generic selection fails." guard ✓. Pass condition met minimally but fully. |
| C-15 | PASS | "Do not copy the Prior-Stage Reading into Downstream Significance" in OUTPUT RULE. Explicit negative constraint. C-15 applies because C-08 and C-11 both pass. |

Aspirational: 7/7

### Composite

```
= 100
```

---

## V-05 — Pre-Printed Envelope + Inertia Evolution

**Base**: V-04 R3 (100 under v3). Adds: (1) pre-printed fill-slot briefing envelope template ("fill all [FIELD] slots, do not omit any field or collapse to prose") with INERTIA EVOLUTION as 5th field; (2) INERTIA STAGE READING in Part 2 stage identity; (3) INERTIA TRAJECTORY end-of-run section (Section B). Preserves all V-04 R3 mechanisms verbatim.

### Essential Criteria

All 5: **PASS**

### Recommended

All 3: **PASS** (C-08 PASS strong — three coherence mechanisms: briefing envelope, Cross-Stage References, CROSS-STAGE SYNTHESIS)

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER field per stage. |
| C-10 | PASS | Cross-Cutting Themes section (Section A). |
| C-11 | PASS | Handoff Packet with CROSS-STAGE SYNTHESIS at every stage. |
| C-12 | PASS | BLOCKER field per stage boundary. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK + INERTIA STAGE READING. |
| C-14 | **PASS (strong)** | Pre-printed template with "fill all [FIELD] slots — do not omit any field or collapse to prose." Briefing Envelope has: PRIOR STAGE, ROLE THIS STAGE | ORIENTATION (explicit lens naming), KEY CONCERNS multi-row (minimum 1 row, lens-directed, "do not select generically"), OPEN QUESTION FORWARDED, INERTIA EVOLUTION. Pre-printing eliminates the entire failure class of field omission or collapse to prose. Strongest C-14 structural guarantee in any R4 variation. |
| C-15 | PASS | "Must add substance not already stated in the Cross-Stage References section above." Explicit instruction preserved from V-04 R3. |

Aspirational: 7/7

### Composite

```
= 100
```

---

## Summary Table

| Variation | Ess | Rec | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | Asp (N/7) | Score |
|-----------|-----|-----|------|------|------|------|------|------|------|-----------|-------|
| V-01 | 5/5 | 3/3 | P | P | P | P | P | **PARTIAL** | P | 6.5/7 | **99.3** |
| V-02 | 5/5 | 3/3 | P | P | P | P | P | P | P | 7/7 | **100** |
| V-03 | 5/5 | 3/3 | P | P | P | P | P | P | P | 7/7 | **100** |
| V-04 | 5/5 | 3/3 | P | P | P | P | P | P | P | 7/7 | **100** |
| V-05 | 5/5 | 3/3 | P | P | P | P | P | P (strong) | P | 7/7 | **100** |

Rank: V-02 = V-03 = V-04 = V-05 (100) > V-01 (99.3)

---

## Key Discriminator Findings

**C-14 form question answered**: V-01's 3-field Stage-Open Context (no explicit Lens output field) earns PARTIAL. V-04's 4-field STAGE-OPEN FORWARD with a mandatory `Lens: [...]` output declaration earns PASS. The discriminator is whether the role's orientation dimension is **named in the output** vs described only in the instruction. The full KEY CONCERNS multi-row table (V-02/V-03/V-05) earns PASS (strong). Bottom line: C-14 requires the reviewing role's lens to appear in the output, not just in an instruction to the model.

**C-15 mechanism question answered**: V-02's "do not copy the lens impact into the risk shift" is functionally equivalent to V-04 R3's "must add substance not already stated." Both are explicit negative constraints and both PASS. Structural field separation alone (different question names) would have been PARTIAL, but V-02 adds the explicit instruction anyway.

**Inertia thread depth**: V-03 and V-05 both surface INERTIA EVOLUTION per stage and INERTIA TRAJECTORY at end-of-run. This adds a qualitative dimension (which stage hardened vs softened the displacement picture) beyond what C-13 captures. Strong C-16 candidate.

---

## Excellence Signals (Top Scorers)

**V-05 (strongest C-14)**: Pre-printed fill-slot template eliminates the field-omission failure class. "Do not omit any field or collapse to prose" is a structural guarantee, not just an instruction. First variation to make the briefing envelope structurally obligatory rather than merely described. Pattern: `pre-printed-fill-slot-template`.

**V-03 + V-05 (C-16 candidate)**: INERTIA EVOLUTION tracking across stages + INERTIA TRAJECTORY synthesis reveals posture arc (which finding hardened/softened the displacement picture). This is qualitatively distinct from C-13's per-stage check — C-13 captures whether inertia is threatened at each stage; the evolution thread captures how the displacement posture changes over the course of the run. Pattern: `inertia-evolution-trajectory`.

**V-04 (minimal form ceiling)**: Proves that the V-05 R3 3-section minimal architecture can be upgraded to 100 under v3 with a 4-field STAGE-OPEN FORWARD block containing an explicit `Lens:` output declaration. The compressed form satisfies C-14 when it includes a mandatory lens-declaration output field. Pattern: `stage-open-lens-declaration`.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inertia-evolution-trajectory", "pre-printed-fill-slot-template", "stage-open-lens-declaration"]}
```
