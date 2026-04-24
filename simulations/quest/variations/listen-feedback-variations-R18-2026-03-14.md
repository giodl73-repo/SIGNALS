---

# listen-feedback — Round 18 Variations (Rubric v16)

**Primary target:** A-29 — CI/variance annotation includes the computation formula

**Baseline preserved:** All R17 criteria, including A-28 (directional sensitivity separation).

---

## Variation Axes Selected

**Single-axis (3):**
- **Output format** — force CI into a two-part labeled structure (Formula: + Computed:)
- **Phrasing register** — fill-in template with formula as a required placeholder to populate
- **Lifecycle emphasis** — named statistical derivation phase, formula stated before numeric result

**Combined (2):**
- **V-04:** Format + Lifecycle + Numbered manifests — three independent enforcement mechanisms; positional auditability at card (count to 9), aggregate (count to A6), and CI (count lines)
- **V-05:** Lifecycle + Inertia sub-fields + Conjunctive field framing + Failure mode annotation — A-27 applied specifically to A-29: names why a bare CI is not auditable

---

## V-01 — Output Format: Formula-First Two-Part CI Block

**Axis:** Output format
**Hypothesis:** A bare interval fits on one line; a two-part structure requires two labeled lines (`Formula:` + `Computed:`). The omission is detectable by counting lines, not reading values.

**A-29 enforcement mechanism:**
```
**Statistical spread:**
- **Formula:** 95% CI = mean ± 1.96 · (SD / √12)
- **Computed:** SD = [X.XX]; 95% CI [lower, upper] (±1.96·[SD_value]/√12)
```
Both lines required. A bare interval without the `Formula:` line is structurally incomplete.

---

## V-02 — Phrasing Register: Fill-In Formula Template

**Axis:** Phrasing register
**Hypothesis:** A template that shows `95% CI [___] (±1.96·___/√12)` as the required output format cannot be satisfied by `95% CI [6.2, 7.8]` — the parenthetical placeholder is a fill-in, not optional commentary.

**A-29 enforcement mechanism:**
```
**95% confidence interval:** 95% CI [[lower], [upper]] (±1.96·[SD_value]/√12)

> Required output format: populate [SD_value] with the computed SD. A CI 
> reading only `95% CI [6.2, 7.8]` leaves a visible template gap.
> Correct form: `95% CI [6.2, 7.8] (±1.96·0.9/√12)`.
```

---

## V-03 — Lifecycle Emphasis: Named Statistical Derivation Phase

**Axis:** Lifecycle emphasis
**Hypothesis:** A named PHASE 4 (STATISTICAL DERIVATION) with four sequential sub-steps makes the formula the required *input* to the phase — not an annotation on the output. The evaluator must execute Step D.1 (state formula) before Step D.4 (write CI).

**A-29 enforcement mechanism:**
```
Step D.1 — State the CI formula: 95% CI = mean ± 1.96·(SD/√12)
Step D.2 — Compute SD
Step D.3 — Apply: CI lower = ...; CI upper = ...
Step D.4 — Report: 95% CI [lower, upper] (±1.96·[SD_value]/√12)
```
Phase cannot be exited without completing D.1. Formula is structurally prior.

---

## V-04 — Combination: Formula-First Block + Derivation Phase + Numbered Manifests

**Axes:** V-01 format + V-03 lifecycle + numbered field manifests (A-13/A-23, A-26)
**Hypothesis:** Two independent enforcement mechanisms on A-29 (output-level formula line, process-level derivation phase) plus positional verifiability on all fields (count to 9 for cards, count to A6 for aggregate). Any omission produces a structural gap detectable by counting.

**Key addition:** Aggregate manifest extends to A6:
```
| A6 | `**Statistical spread:**` | Two-part formula-first structure:
    (a) **Formula:** 95% CI = mean ± 1.96·(SD/√12) [labeled line]
    (b) **Computed:** SD = [value]; 95% CI [lower, upper] (±1.96·[SD_value]/√12) [labeled line]
    Both lines required. |
```

---

## V-05 — Combination: Derivation Phase + Inertia Sub-Fields + Conjunctive Enforcement + Failure Mode Annotation

**Axes:** V-03 lifecycle + inertia sub-fields (A-16/A-24) + conjunctive gains/losses framing (A-21) + A-27 failure mode annotation applied to A-29
**Hypothesis:** A-27 applied to A-29 closes the explanation gap: naming *why* a bare CI is unauditable ("a reader cannot confirm whether ±1.96·SD/√12 or a different method was used") makes the formula a principled requirement rather than an arbitrary format constraint. This is the same mechanism that made UX-before-PM a principled ordering in A-25.

**Key addition in Step S.1:**
> *Without the formula parenthetical `(±1.96·[SD_value]/√12)` alongside the interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method. The formula is not an annotation on the CI; it is the CI's derivation method, which must be transparent for the annotation to be auditable.*

---

Saved to: `simulations/quest/rubrics/listen-feedback-rubric-v16-variations-R18-2026-03-15.md`
