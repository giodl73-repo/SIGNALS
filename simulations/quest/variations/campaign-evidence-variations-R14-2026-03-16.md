Five complete variations written to `simulations/quest/golden/campaign-evidence-variate-R14-2026-03-17.md`.

---

## What's in R14

**C-35 implementation** — every variation splits applicable invocations into two temporally separated checkpoints:
- **PRE-EXECUTION COMMITMENT**: answered before any stage content is written
- **POST-EXECUTION VERIFICATION**: answered after the stage closes

This produces a **checksum of 40** artifacts: (15 positive cells × 2 phases) + (10 negative cells × 1) = 30 + 10.

**C-36 implementation** — every handoff declaration (not just scope-restricted ones) now enumerates each transferred artifact by name and explicitly states the PROVENANCE RULE activation status at that boundary — even S1→S2, which reads "NOT activated — Stage 2 not scope-restricted."

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|-----------|
| **V-01** | Role sequence — temporal boundary markers (`-- PRE --` / `-- EXECUTION --` / `-- POST --`) as zone delimiters | Zone boundaries make the temporal gap between pre/post physically visible in the document; simultaneous filling produces an anachronistic structure detectable by layout |
| **V-02** | Output format — separate named PRE and POST invocation tables per stage; evidence as stage-indexed master table with foreign-key provenance | Separate tables enforce temporal separation mechanically; sequencing compliance becomes sort-verifiable |
| **V-03** | Lifecycle emphasis — all 10 invocation tables (2 phases × 5 stages) pre-declared as blank forms in the preamble; stage bodies only reference them | Pre-declared blank cells convert compliance from creative recall to mechanical cell-fill; unfilled cells are visible before the affected stage's output exists |
| **V-04** | Role sequence + phrasing register — imperative second-person throughout; commitments framed as personal obligations assumed before acting | Direct address ("I, the Hypothesis Architect, commit...") activates a personal-record posture; answering "Yes" becomes a public declaration, not a checkbox |
| **V-05** | Output format + lifecycle emphasis + inertia framing — table-heavy, pre-declared templates, each stage names what a naive single-pass synthesis would skip | Inertia framing converts governance from compliance burden to quality guarantee; the gap between naive and governed approaches is evidence the campaign earned its overhead |
