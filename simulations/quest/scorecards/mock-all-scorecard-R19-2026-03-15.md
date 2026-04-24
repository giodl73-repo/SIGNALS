## Quest Scorecard — mock-all, Round 19 (Rubric v19)

**Rubric:** v19 | **Denominator:** 30 (C-09 through C-38) | **Formula:** `(E/5 × 60) + (R/3 × 30) + (A/30 × 10)`

---

### Per-Criterion Evaluation

#### Essential Criteria (5) — All Variations

All five variations share the same structural scaffold for ROLE 1 setup: TOPICS.md lookup + tier state line, complete classification table with correct headers, 9 namespace rows, gated sequential roles, and REAL-REQUIRED block structure.

| Criterion | E-01 | E-02 | E-03 | E-04 | E-05 |
|-----------|------|------|------|------|------|
| All V-01 through V-05 | PASS | PASS | PASS | PASS | PASS |

**Evidence:**
- **E-01:** All versions open with `Read TOPICS.md. Record tier and compliance tags` + `State: Tier: {N}` before any role header. PASS across all.
- **E-02:** Classification table column headers (`Category`, `MUST use`, `DO NOT use`, `Tier 2/3 Critical`, `Compliance-Tagged`, `REAL-REQUIRED`, `Inertia gap skeleton`) present and correct in all versions.
- **E-03:** Nine namespace rows (scout, draft, review, flow, trace, prove, listen, program, topic) in every version.
- **E-04:** ROLE 1 STOP → STAGE 1 STOP → STAGE 2 STOP → ROLE 2 STOP → ROLE 3 STOP chain present in all; phases cannot be skipped.
- **E-05:** REAL-REQUIRED block structure present in Stage 2 (prove, listen always REAL-REQUIRED=YES); at least one entry in all versions.

**Essential: 5/5 all variations.**

---

#### Recommended Criteria (3)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| R-01 | PASS | PASS | PASS | PASS | PASS |
| R-02 | PASS | PASS | PASS | PASS | PASS |
| R-03 | FAIL | PASS | PASS | PASS | PASS |

**Evidence:**
- **R-01:** All versions: every namespace row has `MUST use` and `DO NOT use` columns populated with vocabulary directives. PASS across all.
- **R-02:** All versions: artifact body instructions specify vocabulary compliance inline ("specification language; state/contract/boundary vocabulary; DO NOT use interview language", etc.) in each stage template. PASS across all.
- **R-03 — V-01 FAIL:** Stage 1 STOP reads "Do not proceed to Stage 2 until Stage 1 artifact sections are present and complete." No classification-derived condition (vocabulary register, compliance flag, tier condition) referenced. Stage 2 STOP identical. The bare gates check artifact presence only.
- **R-03 — V-02 through V-05 PASS:** Stage 1 STOP gates all include condition (4): "each body is 3-5 sentences with HIGH-STRUCTURE vocabulary" — a classification-table-derived register condition. Stage 2 STOP gates reference "EVIDENCE-HEAVY vocabulary." Classification table is the source of these register labels; the gates derive their conditions from it.

---

#### Aspirational Criteria — V-01 Detail

| Criterion | Pass/Fail | Evidence note |
|-----------|-----------|---------------|
| C-09 | PASS | TOPICS.md lookup + tier state line before ROLE 1 |
| C-10 | PASS | Column headers present and correctly named |
| C-11 | PASS | Nine namespace rows present |
| C-12 | PASS | Sequential gated phases; cannot skip ROLE 1 STOP |
| C-13 | PASS | REAL-REQUIRED block structure present in Stage 2 |
| C-14 | PASS | MUST/DO NOT vocabulary in all namespace rows |
| C-15 | PASS | Artifact body templates contain vocabulary compliance instructions |
| C-16 | FAIL | Stage gates reference only artifact count/section presence; no classification-derived conditions (same failure as R-03) |
| C-17 | PASS | Inertia extension instruction present: "Before generating each artifact in this skill, extend the inertia skeleton" in ROLE 2 preamble |
| C-18 | PASS | Named roles (CLASSIFIER, GENERATOR, etc.) + "That is a category error" ontological violation mechanism |
| C-19 | PASS | Depth-anchored seed phrases list present (scout: "directional market signals and competitor positioning", etc.) |
| C-20 | PASS | Body-grounding instructions in each stage artifact template |
| C-21 | PASS | Inertia gap skeleton column pre-seeded in classification table |
| C-22 | PASS | "That is a category error" — explicit vocabulary used |
| C-23 | PASS | "You ARE the CLASSIFIER", "You ARE the GENERATOR", "You ARE the SUMMARIZER", "You ARE the HANDOFF WRITER" |
| C-24 | PASS | Affirmation is syntactically first sentence at each role activation header |
| C-25 through C-33 | PASS | No axis variation touches these criteria; all structurally present |
| C-34 | FAIL | No canonical REAL-REQUIRED identifier declaration sentence in preamble. The REAL-REQUIRED Rationale section begins "For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored here" without naming the canonical identifier. |
| C-35 | FAIL | Stage gates do not enforce per-stage inertia independently; inertia instruction lives in ROLE 2 preamble as cross-stage; Stage 1/2 STOP gates are bare with no inertia check |
| C-36 | FAIL | No "Declaration A" or "Declaration B" labels; declarations exist as unlabeled prose in no explicit authority structure |
| C-37 | FAIL | Trivially fails; no labels exist to cite |
| C-38 | FAIL | Inertia instruction lives in ROLE 2 preamble: "Apply this instruction to all artifacts across Stage 1, Stage 2, and Stage 3" — explicit cross-stage delegation. Stage bodies contain no independent per-stage instruction. |

**V-01 aspirational: 24/30** (C-16, C-34, C-35, C-36, C-37, C-38 fail)

---

#### Aspirational Criteria — V-02 Detail

| Criterion | Pass/Fail | Evidence note |
|-----------|-----------|---------------|
| C-09–C-24 | PASS | Same as V-01 |
| C-25–C-33 | PASS | No axis variation |
| C-34 | PASS | Preamble declares: `"REAL-REQUIRED" is the canonical identifier for the rationale section in this template.` |
| C-35 | PASS | Stage 1 STOP gate condition (3): "each has an extended inertia statement with the skeleton phrase and a topic-specific instance" — per-stage enforcement. Stage 2 STOP identical. |
| C-36 | FAIL | No Declaration A / Declaration B labels; C-34 declaration is unlabeled canonical sentence |
| C-37 | FAIL | Trivially; no labels to cite |
| C-38 | FAIL | ROLE 2 preamble contains: "This inertia extension applies to every artifact across Stage 1, Stage 2, and Stage 3." — explicit cross-stage architectural delegation. Stage bodies execute from the preamble instruction, not from independent stage-local instructions. |
| C-16 | PASS | Stage 1 STOP condition (4): "HIGH-STRUCTURE vocabulary (specification language; state/contract/boundary vocabulary)" — classification-derived |

**V-02 aspirational: 27/30** (C-36, C-37, C-38 fail)

---

#### Aspirational Criteria — V-03 Detail

| Criterion | Pass/Fail | Evidence note |
|-----------|-----------|---------------|
| C-09–C-24 | PASS | Same as V-02 |
| C-25–C-33 | PASS | No axis variation |
| C-34 | PASS | Preamble: `"REAL-REQUIRED" is the canonical identifier for the rationale section in this template.` |
| C-35 | PASS | Stage 1/2/3 each contain per-stage inertia instruction in the stage body |
| C-36 | FAIL | Preamble contains unlabeled declarative sentences about REAL-REQUIRED and per-stage firing; no "Declaration A" / "Declaration B" labels assigned |
| C-37 | FAIL | Trivially; no labels exist |
| C-38 | PASS | Per-stage instruction present independently in Stage 1 body ("For each artifact in this stage, extend the inertia skeleton"), Stage 2 body (same), Stage 3 body (same). ROLE 2 preamble does NOT contain a cross-stage "Apply this instruction to all stages" statement. Inertia architecturally lives per-stage. |
| C-16 | PASS | Stage gates retain classification-derived vocabulary conditions (HIGH-STRUCTURE, EVIDENCE-HEAVY) |

**V-03 aspirational: 28/30** (C-36, C-37 fail)

---

#### Aspirational Criteria — V-04 Detail

| Criterion | Pass/Fail | Evidence note |
|-----------|-----------|---------------|
| C-09–C-24 | PASS | |
| C-25–C-33 | PASS | |
| C-34 | PASS | Declaration A explicitly named in preamble: `**Declaration A -- Rationale identifier authority:** "REAL-REQUIRED" is the canonical identifier...` |
| C-35 | PASS | Stage bodies each contain per-stage inertia: "Per Declaration B: extend the inertia skeleton for each artifact in this stage" |
| C-36 | PASS | Both `**Declaration A**` and `**Declaration B**` labeled in template preamble before any role activates |
| C-37 | FAIL | Stage 1 STOP gate condition (3): "each has an extended inertia statement with the skeleton phrase and a topic-specific instance" — no "per Declaration B" citation. Condition (5): "REAL-REQUIRED block with pre-authored rationale copied verbatim" — no "per Declaration A" citation. Inline restatement only. |
| C-38 | PASS | "Per Declaration B: extend the inertia skeleton for each artifact in this stage" appears independently in Stage 1, Stage 2, Stage 3 bodies. Each stage executes locally; preamble is authority, not delegate. |
| C-16 | PASS | Gates reference HIGH-STRUCTURE / EVIDENCE-HEAVY vocabulary register |

**V-04 aspirational: 29/30** (C-37 only fails)

---

#### Aspirational Criteria — V-05 Detail

| Criterion | Pass/Fail | Evidence note |
|-----------|-----------|---------------|
| C-09–C-24 | PASS | |
| C-25–C-33 | PASS | |
| C-34 | PASS | Declaration A: canonical REAL-REQUIRED identifier authority |
| C-35 | PASS | "Per Declaration B: extend the inertia skeleton" in each stage body |
| C-36 | PASS | Declaration A + Declaration B labeled in preamble |
| C-37 | PASS | Stage 1 STOP: "...per Declaration B" (inertia) + "...per Declaration A" (REAL-REQUIRED). Stage 2 STOP: same. ROLE 2 STOP: "per Declaration B -- verified at Stage 1, Stage 2, and Stage 3 individually" + "per Declaration A". Closed reference loop: preamble → body → gate. |
| C-38 | PASS | "Per Declaration B" in each stage body is stage-local; references template-level authority, not a cross-stage preamble delegation |
| C-16 | PASS | Gates reference classification-derived register conditions |

**V-05 aspirational: 30/30** (no failures)

---

### Score Summary

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 (60) | 2/3 (20) | 24/30 (8.0) | **88.0** |
| V-02 | 5/5 (60) | 3/3 (30) | 27/30 (9.0) | **99.0** |
| V-03 | 5/5 (60) | 3/3 (30) | 28/30 (9.33) | **99.33** |
| V-04 | 5/5 (60) | 3/3 (30) | 29/30 (9.67) | **99.67** |
| V-05 | 5/5 (60) | 3/3 (30) | 30/30 (10.0) | **100.0** |

**Rank:** V-05 > V-04 > V-03 > V-02 > V-01

---

### Discrimination Analysis

The V-01→V-02 step is the only double-digit jump in the ladder (+11.0 pts), driven entirely by R-03 (+10 pts) with C-34 and C-35 contributing the remaining ~0.67 pts. V-02 through V-05 compress into a 1.0-point band (99.0–100.0). Under v19's formula, gate completeness (Recommended tier, 10 pts/criterion) outweighs architectural compliance (Aspirational tier, 0.33 pts/criterion) by 30:1. C-38 is a correctness criterion, not a high-value scoring discriminator.

---

### Excellence Signals from V-05

1. **Closed reference loop:** Template preamble establishes authority (`Declaration A`, `Declaration B`) → stage bodies execute by citation (`Per Declaration B`) → gates verify by citation (`per Declaration B` / `per Declaration A`). A scorer confirms compliance by reading the preamble declaration plus the gate clause alone, without tracing prose intent.

2. **Stage-local architecture as independent from gate enforcement:** C-38 PASS and C-35 PASS are logically independent. V-02 demonstrates a template can enforce per-stage inertia via gate checks (C-35 PASS) while architecturally delegating the instruction cross-stage (C-38 FAIL). Moving the instruction from ROLE 2 preamble into each stage body is a pure structural change — zero effect on gate text, zero effect on runtime behavior.

3. **Declaration labels make compliance auditable at reading time:** V-04 and V-05 are functionally identical in what they enforce; V-05 is verifiably correct from a shorter reading path. The "per Declaration X" gate citations make the verification chain local — no prose tracing required to audit compliance.

4. **R-03 is the highest-value single criterion under v19:** A template that passes all 30 aspirational criteria but fails R-03 scores 97.33. A template that passes only R-03 among the new architectural criteria scores 99.0. Gate completeness is structurally more valuable than any single aspirational criterion.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Stage-local instruction placement (C-38) is an architectural criterion independent of gate enforcement (C-35): a template can enforce per-stage inertia via gate checks while delegating the instruction cross-stage in the ROLE 2 preamble", "Closed reference loop via declaration labels: preamble authority (Declaration A/B) + stage body citation (Per Declaration X) + gate citation (per Declaration X) makes compliance auditable at reading time without prose tracing", "Under the v19 three-tier formula, R-03 (Recommended, 10 pts) dominates C-38 (Aspirational, 0.33 pts) by 30:1 -- gate completeness is structurally more valuable than architectural purity in composite scoring"]}
```
