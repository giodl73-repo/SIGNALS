I have all five variations fully read. Now I'll evaluate each against the rubric criteria.

---

## Scorecard — mock-accept R6 (Rubric v6)

### Scoring Framework Recap

- **Essential** (C-01–C-05): 12 pts each, max 60. Single FAIL caps at 55; two FAILs cap at 43.
- **Recommended** (C-06–C-08): 10 pts each, max 30.
- **Aspirational** (C-09–C-28): `(passes / 20) × 10`. If C-09 absent → C-15, C-20, C-23, C-26 all N/A → denominator = 15. C-24, C-25, C-27, C-28 always in denominator.

---

### Essential Criteria

#### C-01 — Auto-flag rules (artifact-as-subject form, no "I found…")

All five carry the same Rule A/B/C templates:
- `"The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."`
- `"The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."`
- `"The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."`

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-02 — Forbidden triad

All five have the three-rule summary line and "A two-of-three set does not satisfy this gate."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-03 — Status writeback + Canary

All five have CANARY ASSERTION, CANARY-FALSE-POSITIVE, and CANARY SUPPRESSED branch defined in STEP 5.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-04 — Review artifact structure

All five write Coverage table (4 cols), Structural records, Risk (3 cols + urgency labels), Next Steps under a single STEP 8 Write block. No orphaned sections. V-02 has GATE F inline in STEP 8 after the Write sections but the Write block contains all four sections intact.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-05 — MOCK-ACCEPTED positive argument

All five have STEP 6 with Slot 1 and Slot 2 structurally labeled and separate, exact-token constraints on both slots, and "Paraphrase is a violation in both slots."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

**Essential result: all five 5/5 → 60 pts.**

---

### Recommended Criteria

#### C-06 — Entity-naming in roles

All five have "Required artifact citation: ___" with CONSTRAINT `"Write 'The mock artifact's [namespace] section [field: X, token: Y, slot: Z]' verbatim."` in both STEP 3 and STEP 4.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-07 — Step sequencing and guard compliance

All five have `Initialize: Arch-blocked: []` / `Strategy-blocked: []`, VERDICT-ECHO for each REAL-REQUIRED, and explicit "Arch-blocked: none" / "Strategy-blocked: none" empty-list acknowledgment.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-08 — Eval-driven REAL-REQUIRED template

All five carry the 5-field template per role evaluation (Namespace / Required artifact citation / SQ / Artifact state / Verdict + Reason + Required action) and VERDICT-ECHO.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

**Recommended result: all five 3/3 → 30 pts.**

---

### Aspirational Criteria (C-09–C-28)

#### C-09 — Artifact-as-subject grammar (Standing Rule)

All five open with the STANDING RULE block naming the PASS form and four specific FAIL forms. Rule is active throughout all steps.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

C-09 PASS in all five → C-15, C-20, C-23, C-26 remain in denominator for all.

#### C-10 — Tier sourcing

All five have `CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.`

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-11 — Inline completeness gate

GATE A: `Count: ___ present + ___ absent = ___` / CONSTRAINT: Expected 9. GATE B: flags partition summing to 9. Named gates with count assertions before phase transitions.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-12 — Reason-code enforcement at point of use

All five co-locate `CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.` immediately after the Reason field in STEP 3, STEP 4, and STEP 5 (not preamble only).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-13 — Phase exit assertions

All five have GATE A through GATE F with explicit named headers, N+M count assertions, and `"Do not proceed to STEP N until GATE X is written."` blocking language.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-14 — Blank-line failure signal

All five use `___` fill-in notation throughout all fields (not bracket notation).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-15 — Forbidden-form enumeration

All five enumerate four specific forbidden forms in the Standing Rule: `"I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"` alongside the positive PASS form.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-16 — Written-gate blocking language

All five use `"Do not proceed to STEP N until GATE X is written."` in every gate block (GATE A through GATE E explicitly; GATE F has "Do not claim completion until GATE F is written.").

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-17 — Named gate registry

All five carry GATE A, GATE B, GATE C, GATE D, GATE E, GATE F as stable sequential IDs.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-18 — Adjacent framed CONSTRAINT co-location

All five have `CONSTRAINT:` as a visually distinct line immediately following each constrained field — not embedded inline in template description prose.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-19 — Universal blank-slot enforcement

All five use `___` in auto-flag Count A/B/C fields, CANARY ASSERTION, and role evaluation fields. No `[bracket]` placeholder notation anywhere.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-20 — Halt-on-violation instruction

All five Standing Rules include `"HALT. Delete the violating line. Rewrite in PASS form."` — explicit stop action named, not diagnostic enumeration only.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-21 — Per-section CONSTRAINT in review Write block

All five have per-section CONSTRAINT blocks inside STEP 8 for each of the four named sections (Coverage, Structural records, Risk, Next Steps).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-22 — Slot 1 paraphrase violation examples in revert instruction

All five: `Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase violations.` Two quoted concrete forms.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-23 — Three-step halt sequence

All five Standing Rules: `"HALT. Delete the violating line. Rewrite in PASS form."` — three atomic imperatives (HALT / Delete / Rewrite) as sequential steps.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-24 — Gate-to-section traceability in Phase 6 gate

- V-01 STEP 9: per-field confirmation checks for Coverage / Structural records / Risk / Next Steps by name, plus final `"All four sections confirmed: Coverage / Structural records / Risk / Next Steps"`. PASS.
- V-02 GATE F in STEP 8: `"Coverage: ___ / Structural records: ___ / Risk: ___ / Next Steps: ___"` with constraint naming all four. PASS.
- V-03/V-04/V-05: STEP 9 GATE F names all four sections. PASS.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-25 — Slot 2 paraphrase violation examples in revert instruction

All five have the SLOT 2 VIOLATION TABLE with three quoted near-miss rows: `"I found the section covers…"` / `"Coverage demonstrates that…"` / `"The namespace appears domain-consistent"`.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

#### C-26 — Halt co-location at each CONSTRAINT site

The decisive criterion for this round.

- **V-01**: Standing Rule carries the three-step halt; CONSTRAINT blocks in STEP 1 through STEP 8 have no adjacent HALT instruction. MA-24 failure mode. **FAIL**.
- **V-02**: Every CONSTRAINT block is followed by `"HALT. Delete [field]. Rewrite [correct form]."` — per-site halt present at every constrained field. **PASS**.
- **V-03**: Carries full V-05 baseline — per-CONSTRAINT halt at every site throughout all phases. **PASS**.
- **V-04**: V-02 output-format axis applied — halt at every CONSTRAINT block. **PASS**.
- **V-05**: Full combination — per-CONSTRAINT halt at every site. **PASS**.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| FAIL | PASS | PASS | PASS | PASS |

#### C-27 — GATE F as standalone dedicated numbered step

The other decisive criterion for this round.

- **V-01**: GATE F is `STEP 9 — GATE F COMPLETENESS CHECK` — own header, own step number, structurally separate from STEP 8 Write call. **PASS**.
- **V-02**: GATE F is embedded inside `STEP 8 — REVIEW ARTIFACT WRITE AND GATE F` — no separate step number. MA-25 failure mode. **FAIL**.
- **V-03**: GATE F is `STEP 9 — GATE F COMPLETENESS CHECK` — dedicated step, full baseline. **PASS**.
- **V-04**: GATE F is `STEP 9 — GATE F COMPLETENESS CHECK`. **PASS**.
- **V-05**: GATE F is `STEP 9 — GATE F COMPLETENESS CHECK`. **PASS**.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | FAIL | PASS | PASS | PASS |

#### C-28 — Slot 2 violation table

All five present the SLOT 2 VIOLATION TABLE as a structured two-column markdown table (Quoted near-miss form / Violation type) with three rows. Not prose.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

---

### Aspirational Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| **C-26** | **FAIL** | PASS | PASS | PASS | PASS |
| **C-27** | PASS | **FAIL** | PASS | PASS | PASS |
| C-28 | PASS | PASS | PASS | PASS | PASS |
| **Passes** | **19/20** | **19/20** | **20/20** | **20/20** | **20/20** |
| **Asp score** | **9.5** | **9.5** | **10.0** | **10.0** | **10.0** |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 9.5 | **99.5** |
| V-02 | 60 | 30 | 9.5 | **99.5** |
| V-03 | 60 | 30 | 10.0 | **100.0** |
| V-04 | 60 | 30 | 10.0 | **100.0** |
| V-05 | 60 | 30 | 10.0 | **100.0** |

---

### Ranking

**Tier 1 — 100.0**: V-03, V-04, V-05 (three-way tie)

**Tier 2 — 99.5**: V-01, V-02 (symmetric single-axis failures on opposite poles)

**Independence confirmed**: V-01 (C-27 PASS / C-26 FAIL) and V-02 (C-26 PASS / C-27 FAIL) demonstrate that the two criteria are structurally non-overlapping — each can be targeted and missed in isolation without affecting the other.

**Minimal path to 100.0 confirmed**: V-04 (lifecycle + output-format only) closes both R5 V-04 gaps with no additional overhead. The two axes combine without interference — halt proliferation in V-04 does not obscure the STEP 8 / STEP 9 step boundary.

---

### Excellence Signals from Top-Scoring Variations

**Signal 1 — DEFAULT DECISION POSITION as pre-phase inertia anchor** (V-03, V-05)

The block placed before STEP 1 names a structural starting position: every namespace begins REAL-REQUIRED. MOCK-ACCEPTED is described as "earned against inertia" and "the absence of a disqualification is not a positive argument." This is the first variation to name an epistemic default for the evaluation — shifting from "evaluate and decide" to "start blocked, earn release." Structurally distinct from C-05 (positive argument in STEP 6) because it governs the evaluation phase (STEP 3, STEP 4) rather than the post-verdict documentation phase.

**Signal 2 — Cost-of-MOCK as a structurally independent third verdict field** (V-03, V-05)

The `Cost-of-MOCK:` field appears in STEP 3 and STEP 4 evaluation records as a dedicated labeled field — sixth in the per-namespace template, after `Reason:`, with its own CONSTRAINT and HALT. The constrained format `"Without real data for [namespace], [specific type] remains unvalidated by production evidence at Tier [N]."` produces a per-namespace statement that is:

- Structurally separate from Slot 1 (exact token only) and Slot 2 (artifact-as-subject coverage basis)
- Scoped to the evaluation phase (STEP 3/4) not the positive argument phase (STEP 6)
- Forward-facing (names what real data would validate) rather than backward-facing (names what coverage was found)

This is the C-29 candidate. The independence test passes structurally: the field does not collapse into Slot 2 Basis because it names a counterfactual cost rather than a coverage description.

**Signal 3 — Halt density under three-axis combination does not degrade step boundary** (V-04, V-05)

V-04 and V-05 combine per-CONSTRAINT halt blocks (C-26, adds ~15–20 HALT lines per STEP) with STEP 9 elevation (C-27). No axis interference observed: the STEP 9 header creates a clean structural break after the Write call; the HALT density in STEP 8 does not pull STEP 9 content back into the Write block. Confirms the axes are safe to combine in production prompts without length-pressure degradation risk on the step boundary.

---

### Failure Mode Notes

**V-01 (MA-24)**: Three-step halt in Standing Rule only. The eleven CONSTRAINT blocks in STEP 3 and STEP 4 carry no halt. A model detecting a Required artifact citation violation must scroll to the Standing Rule to find the stop action — the cross-reference is not structurally forced.

**V-02 (MA-25)**: GATE F in `STEP 8 — REVIEW ARTIFACT WRITE AND GATE F`. Under context compression, the step label reads as a combined unit; GATE F may be treated as a summary annotation on the Write call rather than an independent blocking gate. Step number `8` references both the Write call and the gate — not independently referenceable by step number alone.

---

### v7 Rubric Update Trigger

V-03 and V-05 produce a `Cost-of-MOCK:` field with the structural properties needed for C-29:
- Dedicated labeled field in the evaluation record
- Distinct format (counterfactual statement) from Slot 1 (exact token) and Slot 2 (coverage basis)
- Constrained at point of use with HALT
- Not absorbed into Slot 2 Basis in the model's output template

**C-29 candidate pattern**: *Per-namespace inertia cost field in evaluation record* — `Cost-of-MOCK:` names the epistemic cost of accepting mock data for each MOCK-ACCEPTED verdict, producing a three-part verdict structure: Slot 1 (reason code token) / Slot 2 (coverage basis) / Cost-of-MOCK (unvalidated domain risk). The cost field is forward-facing (what real data would prove) while Slot 2 is backward-facing (what coverage exists). The two are structurally and semantically orthogonal.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["DEFAULT DECISION POSITION block inverts evaluation starting position — every namespace begins REAL-REQUIRED; MOCK-ACCEPTED is earned against named inertia, not confirmed by absence of disqualification; governs STEP 3 and STEP 4 evaluation phase separately from STEP 6 positive argument phase", "Cost-of-MOCK field as structurally independent third verdict output in evaluation records — named counterfactual cost per MOCK-ACCEPTED namespace in STEP 3/STEP 4 template, distinct from Slot 1 exact token and Slot 2 coverage basis; C-29 candidate confirmed structurally independent"]}
```
