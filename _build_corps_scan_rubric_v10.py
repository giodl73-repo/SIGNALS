"""Build corps-scan-rubric-v10 from v9: add C-38, C-39, C-40."""

import re

SRC = 'C:/src/sim/simulations/quest/rubrics/corps-scan-rubric-v9-2026-03-16.md'
DST = 'C:/src/sim/simulations/quest/rubrics/corps-scan-rubric-v10-2026-03-16.md'

with open(SRC, encoding='utf-8') as f:
    text = f.read()

# ---------- 1. Replace header extraction block ----------

OLD_HEADER = """\
**Two criteria extracted from R9 V-01 excellence signal:**

**C-36 -- DARK SIGNALS structured negative evidence inventory** (depth)
A distinct named section after the positive schema documents absent repo signals by type, each entry naming which pivot mode(s) the absence rules out or weakens. Makes the repo analysis bidirectionally complete: schema rows = positive evidence; DARK SIGNALS entries = negative evidence with per-entry mode consequence. Pass requires mode impact named per entry, not just generic absence notation.

**C-37 -- Pivot deliberation and amend options cross-referenced to DARK SIGNALS labels** (behavior)
Builds on C-36 by requiring the section to be actively used: Evidence Against entries in the pivot deliberation cite DARK SIGNALS labels by name (not standalone "absent X" observations), AND at least one amend option cites a DARK SIGNALS entry as basis for the alternative mode recommendation. Both cross-references required; one alone does not pass.

**Scoring: 225 -> 235 pts** (29 aspirationals x 5 = 145 pts + 60E + 30R).

The extraction follows the established layering pattern: C-36 is the structural artifact (produce the section), C-37 is the integration test (reference it downstream in two places). The two criteria together make negative evidence a first-class traceability artifact -- the same lifecycle the positive schema underwent across C-11 -> C-21 -> C-22.
ration Evidence Against and amend options, making it a live traceability
artifact rather than a standalone inventory.

**Scoring change:** 225 -> 235 pts (29 aspirationals x 5 pts). Golden threshold stays at 80 pts.

**R9 under v8:** V-01 scores 225/225 under v8. V-01's DARK SIGNALS pattern introduces
bidirectionally-falsifiable pivot deliberation -- structured negative evidence that is produced
as a named section and then actively cross-referenced in Evidence Against entries and amend
options. V-02 full aspirational scorecard pending; C-36/C-37 status to be confirmed."""

NEW_HEADER = """\
**Three criteria extracted from R10 V-01/V-02 excellence signals:**

**C-38 -- Hypothesis declared in gate phase before repo scan** (behavior)
The output's first structural phase contains an explicit hypothesis about the repo's
organizational structure -- a testable prediction of what pivot mode the scan will confirm
(e.g., "hypothesis: repo will yield directory-mode signals; service-manifest and DDD-language
signals expected absent"). The hypothesis appears before any repo signal analysis begins, and
is revisable by the scan findings. Distinct from the compliance gate (C-20) -- C-38 requires
the gate to carry a predictive claim about repo structure, not only constraint acknowledgment.
A gate phase that runs a compliance pre-check without stating a structural hypothesis does not
pass.

**C-39 -- DARK SIGNALS entries carry per-entry hypothesis relation** (depth)
Extends C-36 by adding a second per-entry dimension: each entry in the DARK SIGNALS (or
equivalent negative evidence section) includes a "Hypothesis Relation" annotation indicating
whether the absent signal CONFIRMS, OVERTURNS, or is neutral toward the hypothesis declared
in the gate phase. The annotation must appear on the entry itself. A DARK SIGNALS section
with mode-impact annotations (C-36 baseline) but no hypothesis relation field does not pass.
Creates a traceable chain: gate prediction -> absent signal -> hypothesis status.

**C-40 -- Amend options carry hypothesis confirmation/overturn status** (behavior)
Extends C-37 by requiring at least one amend option to carry an annotation stating whether
accepting the alternative recommendation confirms or overturns the hypothesis declared in the
gate phase -- e.g., "DARK SIGNALS basis: [LABEL] -- rules out [mode]; hypothesis
[CONFIRMED/OVERTURNED]." An amend option that cites a DARK SIGNALS label (C-37 baseline) but
omits the hypothesis status does not pass. Closes the hypothesis lifecycle: gate declaration
-> DARK SIGNALS finding -> pivot selection -> amend recommendation with hypothesis outcome.

**Scoring change:** 235 -> 250 pts (32 aspirationals x 5 pts). Golden threshold stays at 80 pts.

**R10 under v9:** V-01 and V-02 both score 235/235 under v9. The R10 excellence pattern
introduces hypothesis lifecycle traceability across three layered criteria: C-38 pre-declares
a structural hypothesis at the gate, C-39 connects each negative evidence entry to the
hypothesis, C-40 closes the hypothesis lifecycle in the amend options. The three criteria
parallel the C-36/C-37 negative evidence pair: negative evidence is produced (C-36/C-39),
then actively referenced downstream (C-37/C-40), with the hypothesis gate (C-38) as the
precondition that makes the traceability chain meaningful."""

text = text.replace(OLD_HEADER, NEW_HEADER, 1)
assert NEW_HEADER in text, "header replacement failed"

# ---------- 2. Update aspirational count in section intro ----------
# "29 criteria x 5 pts = 145 pts available." -> "32 criteria x 5 pts = 160 pts available."
text = text.replace(
    "29 criteria x 5 pts = 145 pts available.",
    "32 criteria x 5 pts = 160 pts available.",
    1,
)

# ---------- 3. Append C-38, C-39, C-40 before the Criterion Summary ----------

NEW_CRITERIA = """
**C-38 -- Hypothesis declared in gate phase before repo scan**
- Weight: aspirational
- Category: behavior
- Pass condition: The output's first structural phase contains an explicit hypothesis about the
  repo's organizational structure -- a testable prediction of what pivot mode the scan will
  confirm (e.g., "hypothesis: repo will yield directory-mode signals; service-manifest and
  DDD-language signals expected absent"). The hypothesis must appear before any repo signal
  analysis begins, must be phrased as a falsifiable claim (not a goal statement or task
  summary), and must be referenced or resolved by the scan findings. A gate phase that runs
  only a compliance pre-check (C-20 baseline: constraint acknowledgment) without a structural
  prediction does not pass. Distinct from C-20 (compliance gate) -- C-38 requires the gate
  to carry a predictive claim about the repo, making the scan a hypothesis test rather than
  an open-ended search.
- R10 signal: V-01's GATE (Hypothesis Officer) stated the structural hypothesis as Role 1's
  primary output before the Repo Archaeologist began the SCAN phase. V-02's Phase 1 (GATE /
  Case File) opened with the investigative hypothesis before Phase 2 scanning began. Both
  variations independently placed hypothesis declaration as the gate phase's primary function,
  converging on the same structural choice across a role-sequenced and a phase-named variant.
  The hypothesis-first gate transforms the scan from evidence collection into a structured
  experiment: the model enters the scan already committed to a claim that the evidence will
  either confirm or overturn.

**C-39 -- DARK SIGNALS entries carry per-entry hypothesis relation**
- Weight: aspirational
- Category: depth
- Pass condition: Each entry in the DARK SIGNALS (or equivalent negative evidence section)
  includes a "Hypothesis Relation" annotation indicating whether the absent signal CONFIRMS,
  OVERTURNS, or is neutral toward the hypothesis declared in the gate phase (C-38 baseline).
  The annotation must appear on the entry itself, not only in the pivot deliberation section.
  A DARK SIGNALS section with mode-impact annotations (C-36 baseline) but no per-entry
  hypothesis relation field does not pass. The hypothesis relation field creates a traceable
  chain: gate prediction -> absent signal -> hypothesis status. Distinct from C-36 (per-entry
  mode impact) -- C-39 requires a second per-entry dimension connecting each negative finding
  to the hypothesis lifecycle, making the DARK SIGNALS section simultaneously a pivot evidence
  artifact and a hypothesis testing instrument.
- R10 signal: V-01's DARK SIGNALS entries each carried a "Hypothesis Relation:" field naming
  the hypothesis state (CONFIRMED or OVERTURNED) alongside the mode-impact annotation. Each
  entry contributes two dimensions: which pivot mode(s) the absence rules out (C-36), and
  whether the absence confirms or overturns the initial structural prediction (C-39). The
  dual-dimension entries make the negative evidence section self-contained: a reviewer can
  assess both pivot selection correctness and hypothesis validity from the DARK SIGNALS section
  alone, without cross-referencing the deliberation section.

**C-40 -- Amend options carry hypothesis confirmation/overturn status**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one amend option carries an annotation stating whether accepting the
  alternative recommendation confirms or overturns the hypothesis declared in the gate phase --
  e.g., "DARK SIGNALS basis: [LABEL] -- rules out [mode]; hypothesis [CONFIRMED/OVERTURNED]."
  The hypothesis status must appear on the amend option itself. An amend option that cites a
  DARK SIGNALS label (C-37 baseline) but omits the hypothesis status does not pass. Distinct
  from C-37 (DARK SIGNALS citation in amend options) -- C-40 requires each DARK SIGNALS-
  grounded amend option to carry the hypothesis conclusion, closing the hypothesis lifecycle:
  gate declaration (C-38) -> negative finding with mode impact (C-36/C-39) -> pivot selection
  -> amend recommendation with hypothesis outcome (C-40). The amend option becomes the last
  node in the hypothesis traceability chain.
- R10 signal: V-01's AMEND-A option carried "DARK SIGNALS basis: [LABEL] -- rules out [mode];
  hypothesis [CONFIRMED/OVERTURNED]" -- the hypothesis outcome was embedded in the amend option
  itself. A reader can understand not only what alternative is recommended and why (C-37
  baseline) but also whether the alternative path is consistent with the hypothesis or requires
  revising it, without returning to the gate or deliberation sections. The hypothesis lifecycle
  is fully auditable from three fixed artifacts: the gate (C-38), the DARK SIGNALS entries
  (C-39), and the amend options (C-40).

"""

SUMMARY_ANCHOR = "---\n\n## Criterion Summary"
text = text.replace(SUMMARY_ANCHOR, NEW_CRITERIA + SUMMARY_ANCHOR, 1)
assert "C-38" in text, "C-38 insertion failed"

# ---------- 4. Append three rows to Criterion Summary table ----------

OLD_LAST_ROW = "| C-37 | DARK SIGNALS cross-referenced in deliberation+amend | aspirational | behavior    |"
NEW_ROWS = """\
| C-37 | DARK SIGNALS cross-referenced in deliberation+amend | aspirational | behavior    |
| C-38 | Hypothesis declared in gate phase before repo scan  | aspirational | behavior    |
| C-39 | DARK SIGNALS entries carry per-entry hypothesis rel | aspirational | depth       |
| C-40 | Amend options carry hypothesis confirmation status  | aspirational | behavior    |"""

text = text.replace(OLD_LAST_ROW, NEW_ROWS, 1)
assert "C-40" in text, "summary table rows failed"

with open(DST, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Written: {DST}")
print(f"Length: {len(text)} bytes")

# Sanity checks
assert "C-38" in text
assert "C-39" in text
assert "C-40" in text
assert "32 criteria x 5 pts = 160 pts available." in text
assert "235 -> 250 pts" in text
print("All assertions passed.")
