import re

v8 = open('C:/src/sim/simulations/quest/rubrics/corps-build-rubric-v8-2026-03-16.md').read()
idx = v8.find('## Essential Criteria')
rubric_body = v8[idx:]

c27_c28_c29 = """### C-27 -- AMEND-RECEIPT with type-tagged amendment options
**Weight**: aspirational
**Category**: behavior
**Source**: R9 excellence signal -- V-02/V-04/V-05 AMEND-RECEIPT axis (C-08 note confirms
these variations add type tags and AMEND-RECEIPT on top of three concrete options; C-08
requires three concrete options referencing specific org.yaml elements; C-27 goes further:
each option carries an explicit amendment type tag classifying the nature of the change, and
the AMEND section closes with a machine-readable receipt confirming option count and type
coverage, making the amendment menu structurally auditable without re-reading each option)
**Text**: Each amendment option in the AMEND section carries an explicit type tag -- such as
ADD-ROLES, ADJUST-LEVELS, RESTRUCTURE-GROUP, or equivalent -- that classifies the amendment
class independently of the option prose description. After listing all three options, the
AMEND section emits an AMEND-RECEIPT that names the count of options and lists their type
tags. This makes the amendment menu machine-readable: an observer can verify option count
and type coverage from the receipt alone without parsing each option prose. The type tags
must be distinct across the three options -- three identically typed options fail this
criterion even if the prose descriptions differ.
**Pass condition**: The output AMEND section assigns a named type tag to each of the three
amendment options. A closing AMEND-RECEIPT (or equivalent named block) states the option
count and lists all three type tags explicitly. Type tags are distinct -- no two options
share the same tag. A variation that lists three concrete options (satisfying C-08) without
type-tagging them and without emitting a receipt fails this criterion. A variation that emits
a receipt but does not tag individual options also fails.

---

### C-28 -- BUILD-VERIFY two-field IA verification
**Weight**: aspirational
**Category**: correctness
**Source**: R9 excellence signal -- V-03/V-05 two-field BUILD-VERIFY axis (C-20 note
confirms BUILD-VERIFY extends to two-field verification for these variations; C-17 and C-20
require lens-phrase verification as a single-purpose phase with one binary verdict per team;
C-28 is orthogonal: the verification covers both the lens field and the expertise field of
each IA role file, each receiving an explicit named verdict, so a team passes BUILD-VERIFY
only when both fields confirm VERBATIM against the resistance profile, closing derivation
across both identity-bearing fields rather than the opening phrase alone)
**Text**: The BUILD-VERIFY phase verifies both the lens field and the expertise field of
each Inertia Advocate role file against their corresponding resistance profile entries. Each
team receives two named verdicts in BUILD-VERIFY output: one for the lens field
(VERBATIM-LENS / DRIFT-LENS or equivalent) and one for the expertise field
(VERBATIM-EXPERTISE / DRIFT-EXPERTISE or equivalent). A team achieves a PASS verdict only
when both fields receive a VERBATIM outcome. A single-field DRIFT on either lens or
expertise causes the team-level verdict to be DRIFT regardless of the other field. This
closes the resistance profile derivation loop across both identity-bearing IA role file
fields, not only the lens phrase captured by C-17 and C-20.
**Pass condition**: The BUILD-VERIFY output names two explicit verdicts per team -- one for
lens, one for expertise -- not a single combined verdict. At least one team entry in the
output shows both field-level verdicts labeled distinctly. The phase-level gate confirms
all teams achieve VERBATIM on both fields before BUILD-VERIFY exits. A variation that checks
only the lens phrase (satisfying C-17/C-20) but does not separately verify the expertise
field against the resistance profile fails this criterion. A variation that performs both
checks but emits a single merged verdict per team without labeling each field also fails.

---

### C-29 -- SECTIONS-COMPLETE declarative correctness rule
**Weight**: aspirational
**Category**: depth
**Source**: R9 excellence signal -- V-01/V-04/V-05 SECTIONS-COMPLETE axis (C-23 note
confirms these variations add a declarative correctness rule for SECTIONS-COMPLETE beyond
the two-block minimum required by C-23; C-23 requires at least two named structural blocks
to carry declarative rules; C-29 specifically requires the aggregation block that confirms
all named section outputs -- SECTIONS-COMPLETE, ROLES-COMPLETE, BUILD-COMPLETE, or
equivalent -- to carry its own declarative rule, making section coverage structurally
self-describing rather than asserted as a behavioral count)
**Text**: The SECTIONS-COMPLETE (or ROLES-COMPLETE, BUILD-COMPLETE, or equivalent named
aggregation block) carries an explicit declarative correctness rule that states what a
structurally complete instance of that block contains: the minimum required section receipts,
what named section references must be present, and what constitutes a structurally incomplete
instance. The rule is stated in output-forward terms ("a correct SECTIONS-COMPLETE names
receipts for PASS-EXEC, PASS-SHARED, and PASS-TEAM") rather than procedural terms ("the
block should list all passes"). A SECTIONS-COMPLETE that omits any named section receipt is
structurally incomplete under its own declared rule -- not merely behaviorally deficient.
This extends the declarative-block pattern of C-23 to the aggregation block that closes the
build, making build-completeness itself structurally auditable.
**Pass condition**: The output step log or narrative contains a named aggregation block
(SECTIONS-COMPLETE or equivalent) with an associated declarative correctness rule. The rule
names the specific section receipts or phase outputs that must be present for the block to
be structurally complete. The rule names at least one structural invalidity condition by
form (e.g., "a SECTIONS-COMPLETE that omits the PASS-TEAM receipt is structurally
incomplete"). The rule uses declarative framing. A variation that emits SECTIONS-COMPLETE
with a correct count but no associated correctness rule fails this criterion. A variation
that covers SECTIONS-COMPLETE only under the two-block minimum of C-23 (without a rule
specific to the aggregation block completeness shape) also fails.

---

"""

# Insert new criteria before the formula section
new_body = rubric_body.replace(
    '## Composite Score Formula',
    c27_c28_c29 + '## Composite Score Formula'
)

# Update formula denominator
new_body = new_body.replace(
    '          + (aspirational_pass / 18 * 10)',
    '          + (aspirational_pass / 21 * 10)'
)

# Append new rows to criterion summary table (insert before version history)
new_rows = (
    '| C-27 | AMEND-RECEIPT with type-tagged options     | aspirational | behavior    | v9    |\n'
    '| C-28 | BUILD-VERIFY two-field IA verification     | aspirational | correctness | v9    |\n'
    '| C-29 | SECTIONS-COMPLETE declarative rule         | aspirational | depth       | v9    |\n'
    '\n'
)
new_body = new_body.replace('## Version History', new_rows + '## Version History')

# Append v9 line to version history
v8_line = ('| v8 | Added C-24, C-25, and C-26 from R8 excellence signals '
           '(V-01/V-04/V-05 phase lifecycle boundary markers; '
           'V-02/V-04/V-05 resistance landscape as named contract artifact; '
           'V-03/V-05 named write passes with per-pass receipts); formula /15 -> /18. |')
v9_line = ('| v9 | Added C-27, C-28, and C-29 from R9 excellence signals '
           '(V-02/V-04/V-05 AMEND-RECEIPT with type-tagged options; '
           'V-03/V-05 BUILD-VERIFY two-field IA verification; '
           'V-01/V-04/V-05 SECTIONS-COMPLETE declarative rule); formula /18 -> /21. |')
new_body = new_body.replace(v8_line, v8_line + '\n' + v9_line)

header = (
    '# corps-build rubric v9\n\n'
    'Extracted from R9 scorecard. Three new criteria (C-27, C-28, C-29) from excellence signals\n'
    'in the R9 variation notes. Formula updated from /18 to /21. Max aspirational points\n'
    'unchanged at 10.\n\n'
    '---\n\n'
)

out = header + new_body
with open('C:/src/sim/simulations/quest/rubrics/corps-build-rubric-v9-2026-03-16.md', 'w') as f:
    f.write(out)
print('done, lines:', len(out.splitlines()))
