Now I have the full rubric. Scoring V-01 and V-02 against all 14 criteria.

---

## crew-review — Quest Score — Round 2

**Rubric**: v2 (2026-03-16) | **Variations**: V-01, V-02 | **Max**: 120 | **Golden threshold**: 80 (all essential + composite)

---

### Scoring: V-01 — Output Format (Lens as 5th Column)

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | Schema column: "Must match a filename stem in `.roles/`. Zero fabricated names." Phase 1 builds pool from files found. |
| C-02 | essential | **PASS** | 5-column schema includes all 4 required columns (role, findings, severity, recommendation) plus Lens. All reviewers get rows. |
| C-03 | essential | **PASS** | Schema: "enum \| Exactly one of: HIGH, MEDIUM, LOW. No other labels." Semantic definitions for all three levels explicit. |
| C-04 | essential | **PASS** | Lens column requires "traceable to this role's domain — not the prior role's." Uniqueness rule enforced: "revise second if near-identical." |
| C-05 | essential | **PASS** | Recommendation constraint: "One action naming (1) what to do and (2) where in the artifact. Generic directives are invalid." |
| C-06 | recommended | **PASS** | Standard: "select 2–4 roles." Deep: "`--depth deep`: queue = all roles." Both branches defined. |
| C-07 | recommended | **PASS** | "cross-role synthesis block… required… name at least one convergence or one conflict." Escape hatch requires explicit "non-overlapping" declaration. |
| C-08 | recommended | **PASS** | AMEND section templated inline with 3 named options (add reviewer, full registry, restrict domain). |
| C-09 | recommended | **PARTIAL** | Challenger is guaranteed included ("always included in standard depth") and must produce a null hypothesis in Findings. But no explicit "appears first" ordering — Phase 3 iterates roles without ordering guarantee. Null hypothesis is free-form, not template. **7/10** |
| C-10 | recommended | **PASS** | Schema Findings constraint: "Names a specific artifact surface (section title, field, diagram element, named assumption). Generic observations without a named surface are invalid." |
| C-11 | aspirational | **FAIL** | Null hypothesis instruction: "what the team currently does instead, and why that alternative might be sufficient." Two conceptual elements, no named slots, no fill-in form structure. **0/2.5** |
| C-12 | aspirational | **PASS** | Lens column added as 5th schema column. Rule: "One sentence: 'As a [role], I care about [specific concern].' No generic restatements." Made correct-by-construction — a missing Lens entry is a visible column gap. **2.5/2.5** |
| C-13 | aspirational | **PARTIAL** | Schema table defines Column \| Type \| Constraint for all 5 columns. Phase 3: "Fill all five cells before writing the row." Types are declared but there is no explicit named validation pass or per-row gate instruction. **1.25/2.5** |
| C-14 | aspirational | **PASS** | Three-level halt: absent directory → ERROR, empty directory → ERROR, role file missing `lens.verify`/`expertise.relevance` → ERROR. All hard stops, no fallback. **2.5/2.5** |

**V-01 Composite:**

| Tier | Score | Max |
|------|-------|-----|
| Essential (5 × 12) | 60 | 60 |
| Recommended (C-06–C-10) | 47 | 50 |
| Aspirational (C-11–C-14) | 6.25 | 10 |
| **Total** | **113.25** | **120** |

All essential: **PASS** → Golden qualified.

---

### Scoring: V-02 — Inertia Framing (Named-Slot Form)

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | "Read every file in `.roles/`. Build the reviewer pool from what you find." Step 3 selects from that pool only. |
| C-02 | essential | **PASS** | Step 5 defines 4-column table. "Challenger row appears first." All reviewer types (challenger + domain) represented. |
| C-03 | essential | **PASS** | Step 4: "Severity: HIGH / MEDIUM / LOW only — no other labels." Step 2 applies "standard semantics" tied to credibility judgment. |
| C-04 | essential | **PASS** | Step 4: "Apply only that role's `lens.verify` perspective." "Do not repeat a finding already raised by a prior reviewer." |
| C-05 | essential | **PASS** | Step 4: "Recommendation: what to do + where in the artifact." |
| C-06 | recommended | **PASS** | Standard: "select 2–3 additional roles." Deep: "run every remaining role after the challenger bracket." Both branches covered. |
| C-07 | recommended | **PASS** | Step 6: convergence or conflict required; "No cross-role signal detected" only if genuinely non-overlapping. |
| C-08 | recommended | **PASS** | Step 7 AMEND section: 3 named options. |
| C-09 | recommended | **PASS** | "Before any domain review, run all roles with `archetype: challenger`." "Challenger row appears first" explicit. 4-slot null hypothesis form mandatory. **10/10** |
| C-10 | recommended | **PASS** | Step 4: "Name a specific artifact surface in each finding (section title, field, diagram, assumption)." |
| C-11 | aspirational | **PASS** | 4-slot form: current-alternative / cost-of-alternative / switching-cost / worth-proceeding-if. "All four blanks must be filled." Empty slot → `[not stated in artifact — HIGH finding]` + logged as HIGH. "Do not collapse multiple blanks into one sentence." **2.5/2.5** |
| C-12 | aspirational | **FAIL** | Domain reviewers told "Apply only that role's `lens.verify` perspective" but no per-role one-sentence lens declaration appears in output structure. No Lens column, no explicit "As a [role], I care about…" required. **0/2.5** |
| C-13 | aspirational | **FAIL** | 4-column table in Step 5 has no type annotations or validation gate. No column-level constraint specification. **0/2.5** |
| C-14 | aspirational | **PARTIAL** | Two-level halt: absent → ERROR + Stop, empty → ERROR + Stop. Missing third level: role file malformed/missing required fields. **1.25/2.5** |

**V-02 Composite:**

| Tier | Score | Max |
|------|-------|-----|
| Essential (5 × 12) | 60 | 60 |
| Recommended (C-06–C-10) | 50 | 50 |
| Aspirational (C-11–C-14) | 3.75 | 10 |
| **Total** | **113.75** | **120** |

All essential: **PASS** → Golden qualified.

---

### Rankings

| Rank | Variation | Score | Golden | Differentiators |
|------|-----------|-------|--------|-----------------|
| 1 | **V-02** | **113.75** | YES | C-09 PASS (10 vs 7), C-11 PASS (2.5 vs 0) |
| 2 | **V-01** | **113.25** | YES | C-12 PASS (2.5 vs 0), C-13 PARTIAL (1.25 vs 0), C-14 PASS (2.5 vs 1.25) |

V-02 wins by 0.5 pts. V-02 achieves a clean recommended sweep (50/50) by solving C-09 with explicit ordering and a structured null hypothesis form. V-01 compensates with stronger aspirational coverage on the lens/typing/halt axis but cannot recover the C-09 and C-11 gap.

---

### Excellence Signals

**From V-02 (top):**

1. **Challenger bracket as a named execution phase** — "Before any domain review, run all roles with `archetype: challenger`" with "Challenger row appears first" as an explicit output rule. Prior variations used an exception clause ("always included"). Naming it a phase gives it priority that an exception clause cannot guarantee.

2. **Slot-level failure escalation in null hypothesis template** — Empty form slot is not a warning; it becomes a `[not stated in artifact — HIGH finding]` that is logged as a HIGH finding. The template cannot be satisfied by silence. Forces the model to produce a finding even when the artifact is under-specified.

**From V-01 (close second, unique patterns worth carrying forward):**

3. **Lens as 5th schema column** — Making lens-lock visible in the output structure rather than relying on an instruction. A skipped lens is a missing column cell, detectable without reading the prose.

4. **Three-level registry halt including malformed-file case** — V-02 only covers absent/empty. V-01 adds "role file missing required fields" as a third halt level, covering the corruption case (registry present, file exists, but content is invalid).

---

### Notes for R3

- **C-11 + C-09 should be combined in a single design axis**: V-02 shows they solve together — a named execution phase for the challenger that includes a mandatory slot form is stronger than two separate instructions. R3 candidates should be measured on "does the challenger phase mandate a named-slot form?" as a single coherent test.
- **C-12 and C-13 remain uncombined**: V-01 achieves C-12 via schema, partial C-13 via pre-write instruction. A variation that adds an explicit "validate all five cells against schema before writing" step would complete C-13.
- **No variation yet achieves C-12 + C-13 together with full C-09**: That would be the R3 target.

---

```json
{"top_score": 113.75, "all_essential_pass": true, "new_patterns": ["slot-level failure escalation: empty null-hypothesis blank auto-elevates to HIGH finding, preventing template satisfaction by silence", "challenger bracket as named execution phase with explicit 'appears first' output rule, stronger than exception-clause inclusion"]}
```
