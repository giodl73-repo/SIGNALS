import re

v4_path = "C:/src/sim/simulations/quest/rubrics/corps-build-rubric-v4-2026-03-16.md"
v5_path = "C:/src/sim/simulations/quest/rubrics/corps-build-rubric-v5-2026-03-16.md"

v4 = open(v4_path).read()

# --- new C-19 and C-20 blocks ---
c19_c20 = """
### C-19 -- TRANSCRIPTION-RECEIPT with per-artifact verdict and auto-correction
**Weight**: aspirational
**Category**: depth
**Source**: R4 excellence signal -- V-02 Signal on C-18 (highest-scoring variation in R4;
differentiates detect-drift from detect-and-correct-drift; a variation can pass C-18 by
asserting transcription occurred and fail C-19 by not emitting a per-artifact receipt with
a rewrite triggered on REVISED)
**Text**: At org-chart.md write time, the build emits a TRANSCRIPTION-RECEIPT that assigns
an explicit per-artifact VERBATIM/REVISED verdict to each contract artifact being
transcribed (at minimum: headcount table and analytic prose). If any artifact receives a
REVISED verdict -- indicating that content changed from the contract phase value -- a
rewrite step is triggered automatically before the phase completes. This makes transcription
self-correcting rather than merely drift-reporting: the phase cannot exit in a REVISED state.
**Pass condition**: The output step log or narrative contains a named TRANSCRIPTION-RECEIPT
or equivalent block at org-chart.md write time. Each contract artifact receives a stated
verdict (VERBATIM or REVISED). A REVISED verdict causes an explicit rewrite action to be
named -- not merely flagged. The phase output confirms no artifact remains in a REVISED
state when the phase closes. A variation that reports drift without correcting it fails
this criterion.

---

### C-20 -- BUILD-VERIFY as single-purpose phase with binary per-team verdict
**Weight**: aspirational
**Category**: correctness
**Source**: R4 excellence signal -- V-01 Signal on C-17 (differentiates phase isolation
from an embedded CROSS-REF subcheck; a variation can pass C-17 by checking IA lens inside
CROSS-REF and fail C-20 by not having a dedicated single-responsibility phase with one
binary verdict per team)
**Text**: The build-complete IA lens verification (C-17) is implemented as a dedicated,
single-purpose phase -- not embedded in CROSS-REF or any file-writing step. This phase has
exactly one responsibility: confirm each IA lens field matches its resistance profile phrase.
Each team in the org receives exactly one binary verdict (VERBATIM or DRIFT) in this phase
output. No file writes, structural integrity checks, summary generation, or other operations
occur within this phase. The phase gate closes only after all teams have received a verdict.
**Pass condition**: The output step log or narrative names a discrete phase whose stated
purpose is IA lens verification and nothing else. The phase produces one VERBATIM/DRIFT
verdict per team and no other outputs. The phase runs after all role files are written and
before any final output block (e.g., AMEND, summary, or CROSS-REF). A variation that
performs this check as a numbered subitem of CROSS-REF fails this criterion even if the
check itself is correct.

---

"""

v5 = v4

# 1. Title line
v5 = v5.replace(
    "Written to `simulations/quest/rubrics/corps-build-rubric-v4-2026-03-16.md`.",
    "# Corps Build Rubric -- v5"
)

# 2. What-changed block: replace everything from "**What changed in v4:**" through the double formula lines
old_changed = (
    "**What changed in v4:**\n"
    "\n"
    "Two new aspirational criteria extracted from R3 scorecard, both from V-05 signals:\n"
)
new_changed = (
    "**What changed in v5:**\n"
    "\n"
    "Two new aspirational criteria extracted from R4 scorecard, one from V-01 and one from V-02:\n"
)
v5 = v5.replace(old_changed, new_changed, 1)

# 3. Replace the source table rows
old_table = (
    "| C-17 | CROSS-REF IA lens-phrase verification at build-complete | V-05 Signal 3 -- fourth CROSS-REF check; closes C-16 derivation loop as post-write structural invariant |\n"
    "| C-18 | Contract verbatim transcription | V-05 Signals 1+2 -- table and prose written once in contract phase, transcribed unchanged to org-chart.md |"
)
new_table = (
    "| C-19 | TRANSCRIPTION-RECEIPT with per-artifact verdict and auto-correction | V-02 Signal on C-18 -- highest-scoring variation in R4; differentiates detect from detect-and-correct; a variation can pass C-18 by asserting transcription occurred and fail C-19 by not emitting a per-artifact receipt with rewrite triggered on REVISED |\n"
    "| C-20 | BUILD-VERIFY as single-purpose phase with binary per-team verdict | V-01 Signal on C-17 -- differentiates phase isolation from embedded CROSS-REF check; a variation can pass C-17 by checking IA lens inside CROSS-REF and fail C-20 by not having a dedicated single-responsibility phase with one binary verdict per team |"
)
v5 = v5.replace(old_table, new_table, 1)

# 4. Replace the structural relationships paragraph
old_struct = (
    "**Structural relationship between C-16, C-17, and C-18:**\n"
    "\n"
    "- **C-16** (v3): extract resistance profile *before* IA write -- derivation step\n"
    "- **C-17** (v4): verify lens phrase verbatim *after* all files written -- confirmation step\n"
    "- C-16 + C-17 form a construction-then-verification pair. A variation can pass C-16 by having a profile phase and fail C-17 by not closing the loop at build-complete.\n"
    "\n"
    "- **C-13** (v2): headcount table written before role files -- ordering\n"
    "- **C-18** (v4): headcount table and prose transcribed unchanged into org-chart.md -- fidelity\n"
    "- C-13 + C-18 form a contract-then-transcription pair. C-13 can be satisfied by early writes that are later revised; C-18 requires those values reach the final document unchanged.\n"
    "\n"
    "**Score formula:** `aspirational_pass / 10 * 10` (was `/8`). Aspirational pool remains 10 points.\n"
    "13 by writing the table early and then silently revising it before output.\n"
    "- No other new patterns emerged from R3 that are not covered by existing criteria or excluded on mechanism-vs-output grounds.\n"
    "\n"
    "**Score formula:** `aspirational_pass / 10 * 10` (was `/8`). Pool unchanged at 10 points."
)
new_struct = (
    "**Structural relationship between C-17, C-18, C-19, and C-20:**\n"
    "\n"
    "- **C-17** (v4): confirm IA lens matches profile at build-complete -- the check exists\n"
    "- **C-20** (v5): BUILD-VERIFY is a dedicated single-purpose phase -- the check is isolated\n"
    "- C-17 + C-20 form a check-existence then check-isolation pair. C-17 is satisfied by a CROSS-REF subitem; C-20 requires the check to be the only responsibility of its phase, with one VERBATIM/DRIFT output per team.\n"
    "\n"
    "- **C-18** (v4): contract artifacts transcribed verbatim to org-chart.md -- fidelity\n"
    "- **C-19** (v5): TRANSCRIPTION-RECEIPT emits per-artifact verdict; REVISED triggers rewrite -- self-correction\n"
    "- C-18 + C-19 form a transcription-fidelity then transcription-correction pair. C-18 is satisfied by stating the table was not changed; C-19 requires an explicit per-artifact receipt at write time and an automated rewrite path when drift is detected.\n"
    "\n"
    "**Score formula:** `aspirational_pass / 12 * 10` (was `/10`). Aspirational pool remains 10 points.\n"
    "\n"
    "- No other new patterns emerged from R4 that are not covered by existing criteria or excluded on mechanism-vs-output grounds."
)
v5 = v5.replace(old_struct, new_struct, 1)

# 5. Insert C-19 and C-20 before the Composite Score Formula section
v5 = v5.replace("## Composite Score Formula", c19_c20 + "## Composite Score Formula", 1)

# 6. Update formula denominator
v5 = v5.replace("aspirational_pass / 10 * 10)", "aspirational_pass / 12 * 10)")

# 7. Update summary table -- append C-19 and C-20
old_row = "| C-18 | Contract verbatim transcription                 | aspirational | depth       | v4    |"
new_rows = (
    "| C-18 | Contract verbatim transcription                 | aspirational | depth       | v4    |\n"
    "| C-19 | TRANSCRIPTION-RECEIPT with auto-correction      | aspirational | depth       | v5    |\n"
    "| C-20 | BUILD-VERIFY as single-purpose phase            | aspirational | correctness | v5    |"
)
v5 = v5.replace(old_row, new_rows, 1)

# 8. Update version history
old_hist = "| v4 | Added C-17 and C-18 from R3 excellence signals (both from V-05 perfect-score architecture); formula /8 -> /10 |"
new_hist = (
    "| v4 | Added C-17 and C-18 from R3 excellence signals (both from V-05 perfect-score architecture); formula /8 -> /10 |\n"
    "| v5 | Added C-19 and C-20 from R4 excellence signals (V-02 self-correcting transcription; V-01 phase isolation); formula /10 -> /12 |"
)
v5 = v5.replace(old_hist, new_hist, 1)

open(v5_path, "w").write(v5)
print("written: " + v5_path)
print("length:", len(v5))
