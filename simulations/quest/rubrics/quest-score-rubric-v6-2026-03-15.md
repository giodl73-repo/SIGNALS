Reading the three new patterns from the R5 scorecard JSON:

1. **Third-order priming ceiling** — AF-8/AF-9 produce no score differential over second-order once H+G floor is set
2. **Register equivalence** — imperative register achieves identical C-15–C-18 verdicts to specification register when H+G structure is present
3. **C-17/C-18 independence** — self-referential priming passes C-17 even when the scan it primes against fails C-15

These map to three new aspirational criteria. Here is the complete v6 rubric:

---

```markdown
# quest-score Rubric — v6

**Version:** v6
**Date:** 2026-03-16
**Prior version:** quest-score-rubric-v5-2026-03-16.md

---

## What changed v5 -> v6

**Three new aspirational criteria, sourced directly from R5 excellence signals:**

**C-19 — Priming-depth ceiling declaration** (from third-order priming ceiling signal)
- Root pattern in R5: V-05 added AF-8/AF-9 (anti-patterns that prime against the priming
  mechanisms themselves — third-order self-reference) and achieved identical score to V-03
  and V-04; the ceiling is at second-order self-reference (C-17); entries beyond that are
  architecturally correct but rubric-neutral; no variation exceeded 100 by including them
- The principle: a score report that awards extra aspirational credit for third-order priming
  entries misapplies the rubric; the scoring ceiling is fixed at C-17 (second-order
  self-reference); third-order entries are valid structural additions but do not open new
  rubric dimensions; a high-quality evaluator names the ceiling explicitly rather than
  searching for a way to award additional credit
- Pass condition: when a scored variation contains anti-pattern entries that prime against
  the priming mechanisms themselves (third-order), the score report correctly identifies
  these as beyond the C-17 ceiling and assigns no additional aspirational credit; the report
  may note third-order entries as architectural correctness signals while confirming they are
  rubric-neutral; PARTIAL if the report identifies the entries but does not state the ceiling
  explicitly; FAIL if the report awards additional aspirational credit for third-order entries
  or inflates composite score above the C-17 ceiling

**C-20 — Register-agnostic structural evaluation** (from imperative register equivalence signal)
- Root pattern in R5: V-03 used imperative register throughout (command-form anti-patterns,
  "CHECK:" / "VERIFY:" phrasing in the scan block) and achieved identical full-envelope
  compliance verdicts on C-15 through C-18 as V-04 and V-05, which used specification
  register; register choice produced no score differential when the structural elements
  (H+G) were present; the evaluator must credit structural presence, not prose form
- The principle: compliance evaluation must be based on structural presence alone, not on
  the prose register of the output being scored; penalizing imperative phrasing or inflating
  specification phrasing introduces evaluator bias that distorts verdicts on C-15 through
  C-18; both registers satisfy these criteria equally when the required structural elements
  are present; the rubric tests structure, not style
- Pass condition: the score report correctly evaluates C-15 through C-18 based on structural
  presence independent of register; a scan block using command-form phrasing ("CHECK: all
  required fields present") satisfies C-15 on equal terms with a declarative inventory
  ("The following fields were verified: ..."); a pre-execution block using imperative
  anti-pattern entries satisfies C-16 and C-17 on equal terms with specification-register
  entries; PARTIAL if the evaluator notes a register preference without penalizing the score;
  FAIL if the evaluator assigns reduced or partial credit based on register choice alone

**C-21 — C-17/C-18 independence tracking** (from V-02 decoupling signal)
- Root pattern in R5: V-02 achieved C-17 PASS (self-referential anti-pattern correctly
  placed in pre-execution section) and C-18 FAIL (no closing scan present), and C-15 FAIL
  (the mechanism C-17 primes against was absent); this decoupling case demonstrates that
  C-17 is structurally independent of both C-15 and C-18; C-18 requires both C-15 and C-16
  to pass; C-17 requires only that a self-referential entry appear in the pre-execution
  section — it does not require the mechanism it references to be present
- The principle: C-17 and C-18 share vocabulary (pre-execution section, self-referential
  priming, scan mechanism) but are independently satisfiable; conflating them produces
  systematic scoring errors — specifically, withholding C-17 credit because C-15 is absent,
  or inferring C-18 satisfaction from C-17 PASS; a high-quality evaluator tracks the two
  verdicts on fully independent structural evidence and explicitly notes when they decouple
- Pass condition: the score report assigns C-17 and C-18 verdicts on independent evidence;
  a C-17 PASS is credited whenever a self-referential anti-pattern appears in the
  pre-execution section, regardless of whether C-15 (the scan it primes against) passes
  or fails; C-18 FAIL is correctly assigned when C-15 is absent even if C-17 passed;
  PARTIAL if the verdicts are assigned correctly but no independence note appears and the
  relationship is left implicit; FAIL if C-17 credit is withheld because C-15 fails
  (conflating satisfaction of the two criteria)

**Formula update:** A_count denominator `/10` → `/13` (13 aspirational criteria now:
C-09 through C-21). Max score and golden threshold unchanged.

---

## Criterion Summary

| ID | Criterion | Tier | Category |
|----|-----------|------|----------|
| C-01 | Complete verdict matrix — one block or row per criterion for each output; no cell blank or omitted | essential | completeness |
| C-02 | Evidence per verdict — each verdict cell cites a specific structural reference from the output | essential | correctness |
| C-03 | Formula-correct composite score — formula, weights, tier counts, and arithmetic applied correctly | essential | correctness |
| C-04 | Ranked leaderboard — all N outputs in a single descending list by composite score | essential | format |
| C-05 | Failure patterns identified — criteria failing across ALL outputs surfaced; absence stated if none | essential | coverage |
| C-06 | Excellence signals — outlier-high criterion-output pairs identified with structural mechanism named | recommended | depth |
| C-07 | Regression signals — degraded criterion-output pairs flagged when prior-round data is available | recommended | depth |
| C-08 | Per-output summary note — 1–3 sentence structural differentiator or miss per output | recommended | depth |
| C-09 | Golden threshold declaration per output — explicit YES/NO field in each output block | aspirational | format |
| C-10 | Failure-pattern root-cause diagnosis — "rubric gap" vs "skill design issue" label on each universal failure | aspirational | depth |
| C-11 | Rubric-adaptive formula derivation — tier counts derived from active rubric, not hardcoded literals | aspirational | correctness |
| C-12 | Structured diagnosis template — failure entries follow a fixed labeled template enforcing parallel structure | aspirational | format |
| C-13 | Derivation-complete gate marker — explicit completion marker after derivation block proves derivation preceded scoring | aspirational | correctness |
| C-14 | Required fields in primary output block — Golden and summary note appear as labeled slots inside the per-output verdict block, not deferred to synthesis | aspirational | format |
| C-15 | Post-scoring completeness scan — explicit verification pass after all output blocks confirms required in-block fields are present before the report is sealed | aspirational | correctness |
| C-16 | Pre-execution failure mode priming — anti-patterns placed before Phase 1 so failure mode context loads before any structural work begins | aspirational | format |
| C-17 | Self-referential anti-pattern priming — at least one anti-pattern entry targets the enforcement mechanisms defined in C-15 or C-16 themselves, placed in the pre-execution priming section | aspirational | correctness |
| C-18 | Full-envelope structural coverage — both a pre-Phase-1 failure mode priming block (C-16) and a post-output named scan (C-15) are present in the same execution unit, closing both ends of the structural execution window | aspirational | format |
| C-19 | Priming-depth ceiling declaration — when a variation contains third-order priming entries (anti-patterns about the priming mechanisms), the score report correctly identifies these as beyond the C-17 ceiling and assigns no additional aspirational credit | aspirational | correctness |
| C-20 | Register-agnostic structural evaluation — C-15 through C-18 verdicts are assigned based on structural presence alone, independent of whether imperative or specification register is used | aspirational | correctness |
| C-21 | C-17/C-18 independence tracking — C-17 and C-18 verdicts are assigned on independent structural evidence; C-17 PASS is credited when a self-referential pre-execution entry is present regardless of C-15 outcome; conflation of the two criteria is absent | aspirational | correctness |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/13 * 10)`, max 100.
```

---

Three new criteria, denominator bumped to `/13`. The ceiling (C-19) and independence (C-21) criteria are both in the `correctness` category because they test evaluator accuracy against known failure modes. The register criterion (C-20) is also `correctness` — it guards against a systematic evaluator bias that would distort structural verdicts.
