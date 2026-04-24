Rubric written to `simulations/quest/rubrics/mock-ns-rubric-v1-2026-03-16.md`.

**5 essential criteria:**
- **C-01** (format): MOCK ARTIFACT header complete with all 6 fields in correct position
- **C-02** (correctness): CATEGORY matches canonical registry for selected skill
- **C-03** (correctness): FLAG computed from correct case rules and written verbatim
- **C-04** (correctness): Fidelity warning present and matches CATEGORY
- **C-05** (depth): Artifact body is skill-specific -- not generic prose

**3 recommended:**
- **C-06** (behavior): S-1 setup emit lines present (TOPICS.md status + skill selection)
- **C-07** (behavior): Artifact written to correct path (`{namespace}` not `{skill-id}`)
- **C-08** (format): Next-step line is the final line of the artifact

**2 aspirational:**
- **C-09** (correctness): `topic` namespace defaults to `topic-plan`, not excluded `topic-status`
- **C-10** (correctness): Compliance override fires when compliance tags are present

**Key failure traps captured at the bottom:** C-03 (EVIDENCE-HEAVY flagged as `none`), C-05 (generic prose body), C-07 (skill-id embedded in filename instead of namespace), and the C-02/C-03 category-flag mismatch pattern.
