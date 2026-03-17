## Quest Scorecard — org-pr — Round 3

**Rubric**: v3 | **Date**: 2026-03-16 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 8

---

### Scoring Matrix

| Criterion | Category | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-01 Multi-role coverage | Essential | PASS | PASS† | PASS† | PASS† | PASS† |
| C-02 P1/P2/P3 on every finding | Essential | PASS | PASS† | PASS† | PASS† | PASS† |
| C-03 File-based role selection | Essential | PASS | PASS† | PASS† | PASS | PASS† |
| C-04 Explicit go/no-go | Essential | PASS | PASS† | PASS† | PASS† | PASS† |
| C-05 Per-role structure / no bleeding | Essential | PASS | PASS† | PASS† | PASS† | PASS† |
| C-06 Projection-aware consensus | Recommended | FAIL | FAIL | PASS† | FAIL | PASS† |
| C-07 Conflict analysis | Recommended | PASS | PASS† | PASS† | PASS† | PASS† |
| C-08 Locator self-correction | Recommended | PASS | PASS† | FAIL | FAIL | PASS† |
| C-09 Phase / lifecycle gating | Recommended | PARTIAL | PARTIAL | PARTIAL | PASS | PASS† |
| C-10 Downstream risk field | Recommended | PASS | FAIL | FAIL | PASS† | PASS† |
| C-11 Formula lock declaration | Aspirational | PASS | FAIL | FAIL | FAIL | PASS† |
| C-12 Named invalid forms | Aspirational | PASS | PASS† | FAIL | FAIL | PASS† |
| C-13 Inertia / if-stays-in framing | Aspirational | FAIL | FAIL | PASS† | FAIL | PASS† |
| C-14 Verdict escape closure | Aspirational | PASS | FAIL | FAIL | FAIL | PASS† |
| C-15 Projection convergence/divergence | Aspirational | FAIL | FAIL | PASS† | FAIL | PASS† |
| C-16 Self-correction gate (pre-commit) | Aspirational | PASS | PASS† | FAIL | FAIL | PASS† |
| C-17 (pre-v3, inferred) | Aspirational | PARTIAL | FAIL | FAIL | PARTIAL | PARTIAL |
| C-18 (pre-v3, inferred) | Aspirational | FAIL | FAIL | FAIL | FAIL | PARTIAL |

† projected from stated axis — no prompt text available for confirmation

---

### Per-Variation Scores

**V-01** — Phrasing Register: Property Declarations Throughout *(full prompt)*

```
Essential:    5.0/5  × 60 = 60.00
Recommended:  3.5/5  × 30 = 21.00   (C-06 FAIL, C-09 PARTIAL)
Aspirational: 4.5/8  × 10 =  5.63
─────────────────────────────────
Composite: 86.6  →  87
Golden: YES (all essential pass, composite ≥ 80) ✓
```

**V-02** — Per-Role Headings with Embedded Self-Correction Gate *(prompt cut off at STEP 2)*

```
Essential:    5.0/5  × 60 = 60.00   (projected — essential structure intended)
Recommended:  2.0/5  × 30 = 12.00   (C-06 FAIL, C-09 PARTIAL, C-10 FAIL)
Aspirational: 2.0/8  × 10 =  2.50   (C-11/C-14 absent without phrasing register)
─────────────────────────────────
Composite: 74.5  →  75
Golden: NO — prompt incomplete; C-11/C-14 likely absent
```

Note: V-02's incompleteness is the primary reliability risk. The embedded gate (C-16) target is stated but unverifiable without the section template.

**V-03** — Inertia Framing *(axis only)*

```
Essential:    5.0/5  × 60 = 60.00
Recommended:  2.5/5  × 30 = 15.00   (C-06 PASS, C-07 PASS, C-08/C-10 FAIL)
Aspirational: 2.0/8  × 10 =  2.50   (C-13 PASS, C-15 PASS; locks absent)
─────────────────────────────────
Composite: 77.5  →  78
Golden: NO — cracked C-13/C-15 but left C-11/C-14/C-16 unaddressed
```

**V-04** — Role Sequence + Lifecycle Emphasis *(axis only)*

```
Essential:    5.0/5  × 60 = 60.00
Recommended:  3.5/5  × 30 = 21.00   (C-09 PASS, C-10 PASS†; C-06 FAIL)
Aspirational: 1.5/8  × 10 =  1.88   (aspirational locks absent)
─────────────────────────────────
Composite: 82.9  →  83
Golden: YES (projected) — thin margin, C-06 miss is the gap
```

**V-05** — Full Integration *(axis only — projection with integration discount)*

```
Essential:    5.0/5  × 60 = 60.00
Recommended:  4.5/5  × 30 = 27.00   (C-06 PASS†, C-08 PASS†, C-09 PASS†;
                                       C-10 PARTIAL — integration tension risk)
Aspirational: 5.5/8  × 10 =  6.88   (C-11/C-12/C-13/C-14/C-15/C-16 PASS†;
                                       C-17/C-18 PARTIAL — structural overcrowding risk)
─────────────────────────────────
Composite: 93.9 raw → 88 with 6pt integration discount
Golden: YES (projected) — caution: five-axis prompts historically dilute register consistency
```

---

### Variation Ranking

| Rank | Variation | Composite | Golden | Confidence |
|------|-----------|-----------|--------|------------|
| 1 | V-05 Full Integration | 88 | YES† | Low (projected only) |
| 2 | V-01 Phrasing Register | 87 | YES | High (full prompt) |
| 3 | V-04 Lifecycle Emphasis | 83 | YES† | Medium (axis projection) |
| 4 | V-03 Inertia Framing | 78 | NO | Medium (axis projection) |
| 5 | V-02 Embedded Gate | 75 | NO | Low (incomplete prompt) |

**Most reliable golden**: V-01 at 87 — only fully-formed prompt, all criteria verifiable.

---

### Excellence Signals from V-01

Three patterns not captured by existing criteria:

**1. Output-object phrasing register (meta-pattern)**
Every field constraint in V-01 uses the form `[FIELD NAME] PROPERTY: ... is required / is not editable / is invalid.` This is not a criterion but the mechanism behind C-11, C-14, C-16, and C-02/C-03 all being satisfied simultaneously. The phrasing treats the output as an *object with typed fields*, making compliance about output correctness rather than reviewer instruction-following. Criterion candidates address specific properties; the register is the *why those properties hold*.

**2. Section-state declaration as a named output class**
`NO-FINDINGS PROPERTY: "No findings. No issues identified..." This is not a finding row. It is a section state declaration.` — naming the zero-findings case as a distinct class with a named form prevents the model from generating weak findings to avoid empty sections. Not currently a criterion; directly addresses a common failure mode.

**3. Forward-looking downstream risk as a semantic field constraint**
`DOWNSTREAM RISK PROPERTY: describes what degrades... if this finding merges without remediation. A value of "none," "N/A," or a restatement of the concern is invalid.` — this is a *semantic type constraint* on a field value, not a format constraint. It bans the most common form of low-quality risk content by name. This is a new class of criterion beyond format/presence checks.

---

```json
{"top_score": 87, "all_essential_pass": true, "new_patterns": ["output-object phrasing register: stating all field constraints as PROPERTY declarations makes compliance structural, not behavioral — the mechanism behind C-11/C-14/C-16 holding simultaneously", "section-state declaration: naming the zero-findings case as a distinct output class with a fixed form prevents spurious padding findings", "semantic field constraint: banning named invalid content forms (restatements, N/A) from a field by name is a new criterion class beyond format and presence checks"]}
```
