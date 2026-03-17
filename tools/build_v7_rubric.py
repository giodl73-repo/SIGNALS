import re

src = open('C:/src/sim/simulations/quest/rubrics/draft-proposal-rubric-v6-2026-03-14.md').read()

# ── 1. Replace header block (everything before "## Essential Criteria") ──────
header = """\
Written to `simulations/quest/rubrics/draft-proposal-rubric-v7-2026-03-14.md`.

---

**v7 changes summary:**

Three new aspirational criteria extracted from R6 excellence patterns:

| ID | Criterion | Parent | Signal |
|----|-----------|--------|--------|
| C-25 | **Sentinel-first trigger ordering** | C-23 | Pattern 1 -- T-GUARD listed first in trigger table shifts enforcement direction from backstop to frontline; unenumerated gaps route to catch-all before specific triggers are consulted |
| C-26 | **COMPLETION STATUS as Phase 0 typed initialization slot** | C-24 | Pattern 2 -- completion declaration is a live mandatory field (PENDING) from document creation, not a prose instruction appended at Phase 13; vocabulary-constrained by its own initialization definition |
| C-27 | **INERTIA COST / INERTIA OFFSET quantification** | C-16/C-20 | Pattern 3 -- do-nothing option gets P*I per sprint (INERTIA COST); each alternative names its sprint crossover point (INERTIA OFFSET); PREREQUISITE GATE extended with inertia-axis binary item; converts do-nothing from qualitative benchmark to computable cost curve |

**Denominator:** `/17` -> `/20`. Scoring formula updated accordingly.

**Why these are criteria, not evaluative notes:**
- C-25 is structurally testable: position 1 in the trigger table is either T-GUARD or it is not. A reviewer confirms or falsifies it by reading the first trigger entry -- no table scan required.
- C-26 is structurally testable: either a COMPLETION STATUS typed slot appears in the Phase 0 initialization block (with an initial value of "PENDING" or equivalent), or it does not. C-24 requires the declaration to exist at completion; C-26 requires it to be a prospectively-defined live field from initialization.
- C-27 is structurally testable: either the do-nothing option carries a numeric INERTIA COST field and each alternative carries an INERTIA OFFSET field, or they do not. The PREREQUISITE GATE binary item makes the inertia axis machine-checkable independently of C-16 content.

The R6 discriminator pattern confirmed C-23 and C-24 structural decoupling -- V-01 (exact C-24, generic C-23 scope) and V-02 (exact C-23 scope, no C-24 declaration) tying at 99.41 with independent failure axes is the empirical demonstration.

---

"""

# ── 2. Three new criteria rows ────────────────────────────────────────────────
new_criteria_rows = """\
| C-25 | **Sentinel-first trigger ordering** | behavior | The T-GUARD sentinel trigger must appear as the first entry in the trigger definition table at Phase 0 initialization -- before T-01, T-02, and all other named triggers. When T-GUARD is listed first, unenumerated gaps route to the catch-all before any specific trigger is consulted; enforcement direction shifts from backstop to frontline. Satisfying C-23 (T-GUARD defined at initialization with the required scope vocabulary) does not satisfy C-25 -- C-23 requires T-GUARD's presence and scope; C-25 requires T-GUARD's position as the first entry in the trigger table. A table that defines T-GUARD after T-01 through T-NN fails C-25 even if T-GUARD's scope vocabulary is correct. The sentinel-first ordering is independently verifiable: a reviewer reads position 1 in the trigger table and confirms or falsifies C-25 without scanning the remainder of the table. |
| C-26 | **COMPLETION STATUS as Phase 0 typed initialization slot** | behavior | The amendment tracking table is initialized in Phase 0 (or equivalent front-load phase) with a COMPLETION STATUS typed slot pre-populated with a vocabulary-constrained initial value -- the canonical initial value is "PENDING" or an equivalent that signals the table is active but document writing is not yet complete. At document completion, the COMPLETION STATUS slot is updated to a vocabulary-constrained terminal value whose canonical form is "T-GUARD enforced all requirements successfully -- no violations detected" (or a vocabulary-pinned equivalent). Satisfying C-24 (explicit completion-state declaration at document end) does not satisfy C-26 -- C-24 requires the declaration to exist at completion; C-26 requires the COMPLETION STATUS slot to be structurally present in the Phase 0 initialization table as a live mandatory field, not appended as a prose instruction at Phase 13. A document that adds a completion declaration in the final phase without a Phase 0 COMPLETION STATUS slot passes C-24 but fails C-26. The distinction mirrors C-18 vs C-24: C-18 requires the table to be initialized prospectively; C-26 requires the completion semantic itself to be a prospectively-defined mandatory field that is live from document creation. |
| C-27 | **INERTIA COST / INERTIA OFFSET quantification** | depth | The do-nothing or status-quo option carries a per-sprint INERTIA COST expressed as a numeric P*I value using the same 1-5 scoring scale defined for C-16. Each non-do-nothing alternative names its sprint crossover point (INERTIA OFFSET) -- the sprint at which cumulative implementation cost equals the cumulative inertia cost of not acting. The PREREQUISITE GATE block (C-20) is extended with an inertia-axis binary item confirming: (1) INERTIA COST is present on the do-nothing option, and (2) at least one alternative names an INERTIA OFFSET. Satisfying C-16 (numeric P*I risk scoring with project-specific anchors) does not satisfy C-27 -- C-16 requires the risk register to use numeric P*I per risk entry; C-27 requires the do-nothing option itself to carry a computable per-sprint inertia cost and each alternative to name a sprint-indexed crossover point. A proposal that scores risks numerically but treats do-nothing as a qualitative baseline fails C-27. The INERTIA OFFSET converts do-nothing from a descriptive benchmark into a computable cost curve: the decision frames as "act by sprint N or pay INERTIA COST per sprint thereafter." |
"""

# ── 3. New failure modes ──────────────────────────────────────────────────────
new_failures = """\
- T-GUARD is defined in the trigger table but appears after T-01 through T-NN -- enforcement direction is backstop not frontline; a gap that matches no specific trigger is only caught after all specific triggers are consulted (fails C-25; satisfies C-23 if T-GUARD scope vocabulary is correct)
- COMPLETION STATUS declaration appears as a prose instruction in Phase 13 but no COMPLETION STATUS typed slot exists in the Phase 0 initialization block -- completion semantics are instruction-only, not structurally enforced from document creation (fails C-26; satisfies C-24 if the declaration text is present at document end)
- Do-nothing option described qualitatively as a cost baseline but carries no numeric INERTIA COST per sprint, and alternatives name no INERTIA OFFSET crossover point -- inertia argument is rhetorical rather than computable (fails C-27; satisfies C-16 if risk register uses numeric P*I for risk entries)
"""

# ── 4. Round 6 discriminator notes section ────────────────────────────────────
r6_notes = """\
---

## Round 6 Discriminator Notes

Round 6 produced five complete variation scorecards. All five Golden. V-04 and V-05
scored 100; V-01 and V-02 tied at 99.41; V-03 scored 98.82. Delta between predicted and
actual was 0 across all five variations -- the v6 rubric predicted all scores exactly.

**Three new excellence patterns identified in R6, each refining an element of the
amendment table lifecycle.**

**C-25: Sentinel-first ordering shifts amendment enforcement from backstop to frontline.**
R5's C-23 requires T-GUARD to be defined at initialization with correct scope vocabulary.
V-05 placed T-GUARD as the first entry in the trigger table, before T-01. This changes
enforcement direction: when T-GUARD is listed last, it is a backstop -- only fires after
all specific triggers fail to match. When T-GUARD is listed first, unenumerated gaps route
to it immediately; specific triggers handle the cases that T-GUARD would route too
broadly. The structural analogy: C-20's PREREQUISITE GATE converts C-17's ordering
requirement from a sequence-scan to a single-block audit; C-25 converts C-23's sentinel
from a last-resort catch to a first-routed catch. The improvement is verifiable from
position 1 in the trigger table alone.

**C-26: COMPLETION STATUS as a Phase 0 typed slot makes enforcement lifecycle complete.**
R5's C-24 requires an explicit completion-state declaration at document end. V-05
implemented this as a COMPLETION STATUS typed slot in the Phase 0 initialization block,
pre-populated with "PENDING." At document completion the slot is updated to the canonical
terminal value. The structural improvement: a prose instruction at Phase 13 to "write a
completion declaration" can be followed or skipped silently. A Phase 0 typed slot that
is initialized to "PENDING" is a live mandatory field from document creation -- the model
cannot reach Phase 13 without addressing it. The pattern is identical to how C-18
improved C-09: C-09 required amend items at the end; C-18 required the table to be
initialized at the start. C-26 applies the same prospective initialization logic to the
completion declaration itself.

**C-27: INERTIA COST / INERTIA OFFSET converts do-nothing from qualitative to computable.**
R4's V-03 introduced inertia-forward framing as an evaluative lens; the R4 notes
explicitly declined to encode it as a criterion. R6 V-04 operationalized the pattern
with three changes that make it structurally testable: (1) the do-nothing option carries
a numeric INERTIA COST per sprint using the C-16 P*I scale, (2) each alternative names
its INERTIA OFFSET sprint crossover point, and (3) the PREREQUISITE GATE block (C-20)
is extended with an inertia-axis binary item. The third change is the deciding factor:
a PREREQUISITE GATE item makes inertia-axis completeness machine-checkable in the same
way C-20 made register ordering machine-checkable. Without the gate item, INERTIA fields
are evaluative depth signals like V-03. With the gate item, they are structurally
required and auditability is preserved.

**C-23/C-24 structural decoupling confirmed.** V-01 (exact C-24 declaration, generic
T-GUARD scope) and V-02 (exact C-23 scope vocabulary, no completion declaration) tied at
99.41 with independent failure axes. V-03 (neither C-23 nor C-24) scored 98.82 -- each
criterion contributes exactly 0.50 points independently. No criterion subsumes the other.

**Variation ranking by structural value beyond rubric (R6):**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | Sentinel-first (C-25) + COMPLETION STATUS slot (C-26); strongest amendment lifecycle integration |
| 2 | V-04 | INERTIA COST / INERTIA OFFSET + PREREQUISITE GATE extension (C-27); orthogonal quantification axis |
| 3 | V-01 | Exact C-24 declaration; C-23 fails by design; single-axis clean C-24 demonstration |
| 4 | V-02 | Exact C-23 scope vocabulary; C-24 fails by design; single-axis clean C-23 demonstration |
| 5 | V-03 | R5 V-05 machinery complete; neither R6 criterion addressed; lower bound confirmation |

"""

# ── 5. New trace notes ────────────────────────────────────────────────────────
new_trace = """\
- **C-25**: Not demonstrated in trace -- no trigger table present; sentinel-first position cannot be verified without a trigger table; C-18 and C-23 already fail
- **C-26**: Not demonstrated in trace -- no Phase 0 initialization block present; COMPLETION STATUS typed slot cannot exist without C-18 table initialization; C-18, C-23, and C-24 already fail
- **C-27**: Not demonstrated in trace -- do-nothing option (D: CREST) carries no INERTIA COST field; no alternative carries an INERTIA OFFSET; PREREQUISITE GATE not present; C-16 and C-20 already fail in trace
"""

# ════════════════════════════════════════════════════════════════════════════
# Transform src -> v7
# ════════════════════════════════════════════════════════════════════════════
v7 = src

# Step 1: replace header
essential_marker = '\n## Essential Criteria'
essential_pos = v7.find(essential_marker)
v7 = header + v7[essential_pos+1:]   # drop the leading \n

# Step 2: insert C-25/26/27 after C-24 row (before the closing blank line of the table)
c24_start = v7.find('\n| C-24 |')
c24_row_end = v7.find('\n', c24_start + 1)
v7 = v7[:c24_row_end+1] + new_criteria_rows + v7[c24_row_end+1:]

# Step 3: update scoring formula denominator
v7 = v7.replace('(aspirational_pass / 17 * 10)', '(aspirational_pass / 20 * 10)')

# Step 4: append new failure modes before "## Round 1"
r1_marker = '\n## Round 1 Discriminator Correction'
r1_pos = v7.find(r1_marker)
# find end of last failure-mode bullet before r1_pos
last_nl = v7.rfind('\n', 0, r1_pos)
v7 = v7[:last_nl+1] + new_failures + v7[last_nl+1:]

# Step 5: insert Round 6 notes before "## Trace Alignment Notes"
trace_marker = '\n## Trace Alignment Notes'
trace_pos = v7.find(trace_marker)
# find the preceding ---
sep_pos = v7.rfind('\n---\n', 0, trace_pos)
v7 = v7[:sep_pos+1] + r6_notes + v7[sep_pos+5:]   # skip \n---\n

# Step 6: append C-25/26/27 trace notes at end
v7 = v7.rstrip('\n') + '\n' + new_trace

out = 'C:/src/sim/simulations/quest/rubrics/draft-proposal-rubric-v7-2026-03-14.md'
open(out, 'w').write(v7)
print('written', len(v7), 'bytes')
