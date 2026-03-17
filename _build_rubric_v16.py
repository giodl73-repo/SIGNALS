import re

with open('C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v15-2026-03-16.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace the summary header
text = text.replace(
    "**org-chart-rubric-v15-2026-03-16.md** — 1110 lines, written to `simulations/quest/rubrics/`.",
    "**org-chart-rubric-v16-2026-03-16.md** — written to `simulations/quest/rubrics/`.",
    1
)

# 2. Replace the "Three new" table block (find by the v15 content)
old_table_start = "**Three new aspirational criteria added from R15 excellence signals:**"
old_table_end = "**Formula updated:** `/36 \u2192 /39`\n**Composite:** `(essential_pass/5 \u00d7 60) + (recommended_pass/3 \u00d7 30) + (aspirational_pass/39 \u00d7 10)`"

# Find and replace the full block
idx_start = text.find(old_table_start)
idx_end = text.find(old_table_end) + len(old_table_end)
assert idx_start != -1 and idx_end > idx_start, f"idx_start={idx_start} idx_end={idx_end}"

new_table = """**Three new aspirational criteria added from R17 excellence signals:**

| ID | Pattern | Block | Closes gap in |
|----|---------|-------|---------------|
| A-40 | `trigger-type-accounting-block` | `TRIGGER-TYPE-ACCOUNTING:` | A-39: aggregate type-diversity count with no per-type PRESENT/ABSENT row for closed-set types |
| A-41 | `register-roadmap-correspondence-block` | `REGISTER-ROADMAP-CORRESPONDENCE:` | A-38 + A-39: register category population and roadmap signal diversity each confirmed in isolation, with no cross-domain alignment check |
| A-42 | `roadmap-type-vocabulary-declaration` | `ROADMAP-TYPE-VOCABULARY:` | A-39: named-closed-set parenthetical with no standalone declared vocabulary block before the roadmap |

**Formula updated:** `/39 \u2192 /42`
**Composite:** `(essential_pass/5 \u00d7 60) + (recommended_pass/3 \u00d7 30) + (aspirational_pass/42 \u00d7 10)`"""

text = text[:idx_start] + new_table + text[idx_end:]

# 3. Replace the derivation rationale paragraph
# Find from "All three follow the established round pattern:" through the last sentence of the rationale
old_rationale_start = "All three follow the established round pattern: A-37 is the bidirectional"
old_rationale_end = "A-39 converts implicit signal variety into an explicit type-diversity constraint."
idx_s = text.find(old_rationale_start)
idx_e = text.find(old_rationale_end) + len(old_rationale_end)
assert idx_s != -1 and idx_e > idx_s

new_rationale = """All three follow the established round pattern: A-40 is the trigger-type-accounting parallel to A-34
(ROLE-TIER-ACCOUNTING) and A-38 (REGISTER-POPULATION-AUDIT) -- the same per-item PRESENT/ABSENT row
structure applied to the roadmap trigger-type domain. A-41 is the cross-domain correspondence parallel
to A-37 (CHARTER-RHYTHM-PARITY) -- a bidirectional mapping that neither A-38 nor A-39 can enforce
alone, since each audits its own domain without checking alignment between them. A-42 is the vocabulary
declaration parallel to A-36 (REGISTER-CATEGORY-CONTRACT) -- a pre-artifact closed-set block that
promotes the implicit "named closed set" parenthetical in A-39 into an explicitly declared, structurally
detectable contract.

**Derivation rationale:** Each R17 variation isolated one refinement axis. V-01 introduced a
`TRIGGER-TYPE-ACCOUNTING:` block immediately after the `ROADMAP-TRIGGER-DIVERSITY:` block (A-39) and
before the Anti-Pattern Watch section. The block emits one row per trigger type in the declared closed
set, with each row stating the type name, the count of roadmap tier signals assigned that type, and a
TYPE-REPRESENTED (count >= 1) or TYPE-ABSENT (count = 0) verdict. This closes the per-type coverage
gap: A-39 counts distinct types present across all tiers and requires at least two, but emits no
per-type row for types in the declared set with zero assignments. A reviewer confirming A-39 sees that
diversity is achieved; a reviewer confirming A-40 additionally sees which specific types are absent.
The pattern is the direct roadmap-trigger-type parallel to A-34 (ROLE-TIER-ACCOUNTING emits
TIER-ABSENT per zero-count tier) and A-38 (REGISTER-POPULATION-AUDIT emits CATEGORY-EMPTY per
zero-count category). V-02 introduced a `REGISTER-ROADMAP-CORRESPONDENCE:` block after
`ROADMAP-TRIGGER-DIVERSITY:` and before Anti-Pattern Watch. The block presents a correspondence table
mapping each register category (from the A-36 REGISTER-CATEGORY-CONTRACT) to the roadmap tier whose
Observable Signal is most directly activated by changes in that category's population or composition,
naming the tier and the linking signal. Coverage gaps (register category with no corresponding tier
signal) and unanchored triggers (roadmap tier with no corresponding register category) are flagged as
constraint violations. This closes the cross-domain alignment gap: A-38 confirms per-category
population within the register domain and A-39 confirms type diversity within the roadmap domain, but
neither confirms that the register category structure and the roadmap tier signals are in alignment.
The correspondence block is the cross-domain parallel to A-37 (CHARTER-RHYTHM-PARITY maps charters to
rhythm rows bidirectionally): where A-37 closes the correspondence gap between two structural
sub-sections, A-41 closes the correspondence gap between two distinct artifact domains (register and
roadmap) that are each internally consistent but may be externally misaligned. V-03 introduced a
`ROADMAP-TYPE-VOCABULARY:` block immediately before the Org Evolution Roadmap table, pushing the
roadmap to the step after. This closes the implicit-vocabulary gap: A-39 references a "named closed
set" of trigger types but that set is declared only parenthetically within the ROADMAP-TRIGGER-DIVERSITY
block description, not as a standalone pre-artifact contract. Under generation pressure the set boundary
can expand silently (new type labels can appear in the roadmap before the ROADMAP-TRIGGER-DIVERSITY
block audits them). A named vocabulary block whose absence is structurally detectable closes this
expansion gap. The displacement analysis confirmed that ROADMAP-TYPE-VOCABULARY at step 19 (V-03) does
not break A-38 (REGISTER-POPULATION-AUDIT remains immediately after register body at step 18 and
before roadmap at step 20) or A-12 (COST-DELTA CALIBRATION can occupy any position between register
and roadmap without conflict). All five R17 variations scored 100.00/100 against v15."""

text = text[:idx_s] + new_rationale + text[idx_e:]

# 4. Prepend the v16 changelog entry before the v15 entry
old_cl = "  v15 -- added A-37/A-38/A-39 from R15 excellence signals:"
new_cl = """  v16 -- added A-40/A-41/A-42 from R17 excellence signals:
  trigger-type-accounting-block (V-01 axis: TRIGGER-TYPE-ACCOUNTING: block immediately after
  ROADMAP-TRIGGER-DIVERSITY: block and before Anti-Pattern Watch; one row per trigger type in
  the declared closed set; each row emits type name, tier signal count, and TYPE-REPRESENTED/
  TYPE-ABSENT verdict; zero-assignment type emits TYPE-ABSENT making coverage gap a directly
  scannable row; additive to A-39 aggregate diversity count; parallel to A-34 ROLE-TIER-ACCOUNTING
  and A-38 REGISTER-POPULATION-AUDIT pattern),
  register-roadmap-correspondence-block (V-02 axis: REGISTER-ROADMAP-CORRESPONDENCE: block after
  ROADMAP-TRIGGER-DIVERSITY: and before Anti-Pattern Watch; correspondence table mapping each A-36
  register category to the roadmap tier Observable Signal most directly linked to that category's
  population or composition; coverage gaps -- register category with no corresponding tier signal --
  and unanchored triggers -- roadmap tier with no corresponding register category -- flagged as
  constraint violations; additive to A-38 category population audit and A-39 trigger diversity;
  closes cross-domain alignment gap between register structure and roadmap tier signals; parallel to
  A-37 CHARTER-RHYTHM-PARITY cross-domain correspondence pattern),
  roadmap-type-vocabulary-declaration (V-03 axis: ROADMAP-TYPE-VOCABULARY: block immediately before
  the Org Evolution Roadmap table; enumerates each valid trigger type label as a separate line item;
  declares unlisted labels a constraint violation; roadmap Observable Signal entries and
  ROADMAP-TRIGGER-DIVERSITY type assignments verifiable against declared vocabulary without consulting
  implicit schema; additive to A-39 named-closed-set parenthetical; parallel to A-36
  REGISTER-CATEGORY-CONTRACT pattern).
  Aspirational denominator updated from /39 to /42.
  v15 -- added A-37/A-38/A-39 from R15 excellence signals:"""

text = text.replace(old_cl, new_cl, 1)

# 5. Update the aspirational denominator header
text = text.replace(
    "## Aspirational Criteria (10 pts total, 1 pt each, denominator /39)",
    "## Aspirational Criteria (10 pts total, 1 pt each, denominator /42)",
    1
)

# 6. Add A-40/A-41/A-42 + new formula, replacing the old formula footer
old_footer = "**Formula:** `aspirational_pass/39 * 10`\n\n**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/39 * 10)`\n\n**Golden threshold:** All 5 essential pass AND composite >= 80."

new_criteria = """### A-40 -- TRIGGER-TYPE-ACCOUNTING per-type verdict block
**Category:** correctness | **Weight:** aspirational

When A-39 (ROADMAP-TRIGGER-DIVERSITY signal type diversity block) is active, a standalone
`TRIGGER-TYPE-ACCOUNTING:` block appears immediately after the `ROADMAP-TRIGGER-DIVERSITY:`
block and before the Anti-Pattern Watch section (or equivalent next section). The block must
emit one row per trigger type in the declared closed set used by the ROADMAP-TRIGGER-DIVERSITY
block (or enumerated by a ROADMAP-TYPE-VOCABULARY block when A-42 is active). Each row states
the trigger type name, the count of roadmap tier signals assigned that type, and a verdict of
`TYPE-REPRESENTED` (count >= 1) or `TYPE-ABSENT` (count = 0). A trigger type in the declared
closed set with zero tier signal assignments emits `TYPE-ABSENT`, making the coverage gap a
directly scannable row rather than a silent absence detectable only by scanning type labels
across the ROADMAP-TRIGGER-DIVERSITY enumeration.

A-39 requires a type-diversity count and confirms that at least two distinct types are present
across all tiers -- diversity is confirmed at the aggregate level. A-40 closes the per-type
coverage gap: A-39 is satisfied by counting distinct types across the tiers actually present,
but emits no per-type row for types in the declared closed set with zero assignments. A reviewer
confirming A-39 sees that diversity is achieved; a reviewer confirming A-40 additionally sees
exactly which types in the declared vocabulary are absent from all tier signals. The block is
the direct roadmap-trigger-type parallel to A-34 (ROLE-TIER-ACCOUNTING emits TIER-ABSENT per
zero-count tier declared in ROLE-LOAD-ORDER) and A-38 (REGISTER-POPULATION-AUDIT emits
CATEGORY-EMPTY per zero-count category declared in REGISTER-CATEGORY-CONTRACT): each of those
blocks converts a silent-absence gap into a directly scannable per-item row, and A-40 applies
the same structural pattern to trigger type coverage across the roadmap's declared type
vocabulary. The block is positioned immediately after ROADMAP-TRIGGER-DIVERSITY so that it
reflects the completed type assignment state from that block's enumeration.

**Pass condition:** A-39 active; a labeled `TRIGGER-TYPE-ACCOUNTING:` block appears immediately
after the `ROADMAP-TRIGGER-DIVERSITY:` block and before the Anti-Pattern Watch section (or
equivalent next section); block contains one row per trigger type in the declared closed set;
each row names the trigger type, states the count of tier signals assigned that type, and emits
`TYPE-REPRESENTED` (count >= 1) or `TYPE-ABSENT` (count = 0); all types in the declared closed
set are represented in the block -- no declared type is omitted; or criterion is N/A if A-39 is
not active.

---

### A-41 -- REGISTER-ROADMAP-CORRESPONDENCE cross-domain mapping block
**Category:** correctness | **Weight:** aspirational

When A-38 (REGISTER-POPULATION-AUDIT category entry count block) and A-39 (ROADMAP-TRIGGER-DIVERSITY
signal type diversity block) are both active, a `REGISTER-ROADMAP-CORRESPONDENCE:` block (or
equivalent labeled block) appears after the ROADMAP-TRIGGER-DIVERSITY block and before the
Anti-Pattern Watch section (or equivalent next section). The block presents a correspondence
table mapping each register category declared in the A-36 REGISTER-CATEGORY-CONTRACT to the
roadmap tier whose Observable Signal is most directly activated by changes in that category's
population or composition. For each register category, the block must name the corresponding
roadmap tier and the Observable Signal that constitutes the activation link. Any register category
with no corresponding roadmap tier signal is flagged as a coverage gap. Any roadmap tier with no
corresponding register category is flagged as an unanchored trigger. Both gap types are constraint
violations that must be resolved before the document is accepted.

A-38 confirms register category population: which categories have entries and which are empty.
A-39 confirms roadmap signal diversity: how many distinct trigger types are represented across
tier signals. Neither criterion confirms that the register's organizational categories and the
roadmap's tier progression are in alignment -- a register can be fully populated across all
categories while the roadmap tiers are triggered by signals entirely unrelated to the register's
category structure, and vice versa. A-41 closes this cross-domain alignment gap: the
correspondence table makes the intended linkage between register-category structure and roadmap
tier signals an explicit, independently verifiable property of the document rather than an
assumed alignment. The block is the cross-domain parallel to A-37 (CHARTER-RHYTHM-PARITY maps
charters to rhythm rows bidirectionally): where A-37 closes the correspondence gap between two
structural sub-sections of the same document, A-41 closes the correspondence gap between two
distinct artifact domains (the register and the roadmap) that are each internally consistent
but may be externally misaligned.

**Pass condition:** A-38 and A-39 both active; a labeled `REGISTER-ROADMAP-CORRESPONDENCE:`
block appears after the ROADMAP-TRIGGER-DIVERSITY block and before the Anti-Pattern Watch section
(or equivalent next section); block presents a correspondence table with one row per register
category declared in the A-36 REGISTER-CATEGORY-CONTRACT; each row names the register category,
the corresponding roadmap tier, and the Observable Signal constituting the activation link;
register categories with no corresponding tier signal are flagged as coverage gaps; roadmap tiers
with no corresponding register category are flagged as unanchored triggers; both coverage gaps
and unanchored triggers are constraint violations; or criterion is N/A if A-38 or A-39 is not
active.

---

### A-42 -- ROADMAP-TYPE-VOCABULARY closed-set trigger type declaration
**Category:** correctness | **Weight:** aspirational

When A-39 (ROADMAP-TRIGGER-DIVERSITY signal type diversity block) is active, a
`ROADMAP-TYPE-VOCABULARY:` block (or equivalent labeled block) appears immediately before the
Org Evolution Roadmap table. The block must enumerate each valid trigger type label as a separate
line item and declare that any trigger type label not in the enumerated set is a constraint
violation. The Org Evolution Roadmap's Observable Signal type assignments, the ROADMAP-TRIGGER-DIVERSITY
block's type enumerations, and the TRIGGER-TYPE-ACCOUNTING block (when A-40 is active) are all
then verifiable against the declared vocabulary without consulting an implicit or embedded schema.

Without a named vocabulary block, the trigger type classification schema is embedded implicitly
within the ROADMAP-TRIGGER-DIVERSITY block's description as a "named closed set" parenthetical.
The boundary of that set is implicit: new type labels can appear in the roadmap table's Observable
Signal entries or in the ROADMAP-TRIGGER-DIVERSITY enumeration without detection, and the schema
can expand silently under generation pressure. A named vocabulary block whose absence is
structurally detectable (the block is either present or not) closes this implicit-expansion gap.
The vocabulary block also enables count-based completeness verification for TRIGGER-TYPE-ACCOUNTING
(A-40): the accounting block's row count can be confirmed against the vocabulary enumeration rather
than inferred from the ROADMAP-TRIGGER-DIVERSITY output. The ROADMAP-TYPE-VOCABULARY block is the
direct roadmap-trigger-type parallel to A-36 (REGISTER-CATEGORY-CONTRACT for register categories):
both convert an implicit classification schema into an explicit, independently verifiable closed-set
declaration positioned before the artifact body that uses it.

**Pass condition:** A-39 active; a labeled `ROADMAP-TYPE-VOCABULARY:` block (or equivalent)
appears immediately before the Org Evolution Roadmap table; block enumerates each valid trigger
type label as a separate line item; block declares that any label not in the enumerated set is a
constraint violation; Observable Signal trigger type assignments in the roadmap table and trigger
type labels in the ROADMAP-TRIGGER-DIVERSITY block use only labels from the enumerated set; each
label appears as a standalone line item (not embedded in prose); or criterion is N/A if A-39 is
not active.

---

**Formula:** `aspirational_pass/42 * 10`

**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/42 * 10)`

**Golden threshold:** All 5 essential pass AND composite >= 80."""

idx_footer = text.find(old_footer)
assert idx_footer != -1, "Footer not found"
# Find the separator "---" just before the formula footer
sep_before_footer = text.rfind("---\n\n**Formula:**", 0, idx_footer + 20)
assert sep_before_footer != -1

text = text[:sep_before_footer] + "---\n\n" + new_criteria

out_path = "C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v16-2026-03-16.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(text)

lines = text.count("\n") + 1
print("Written:", len(text), "bytes,", lines, "lines")

checks = [
    ("v16 header", "org-chart-rubric-v16-2026-03-16.md"),
    ("A-40 criterion", "### A-40 --"),
    ("A-41 criterion", "### A-41 --"),
    ("A-42 criterion", "### A-42 --"),
    ("denominator /42", "denominator /42"),
    ("formula /42", "aspirational_pass/42 * 10"),
    ("v16 changelog", "v16 -- added A-40/A-41/A-42"),
    ("TRIGGER-TYPE-ACCOUNTING block", "TRIGGER-TYPE-ACCOUNTING:` block appears immediately"),
    ("REGISTER-ROADMAP-CORRESPONDENCE block", "REGISTER-ROADMAP-CORRESPONDENCE:`"),
    ("ROADMAP-TYPE-VOCABULARY block", "ROADMAP-TYPE-VOCABULARY:` block"),
    ("v15 criteria preserved A-39", "### A-39 --"),
    ("A-01 preserved", "### A-01 --"),
    ("golden threshold", "Golden threshold"),
]
for name, s in checks:
    status = "OK" if s in text else "MISSING"
    print(f"  {status}: {name}")
