import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

v14_path = 'C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v14-2026-03-16.md'
v15_path = 'C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v15-2026-03-16.md'

v14 = open(v14_path, 'r', encoding='utf-8').read()
v15 = v14

# 1. File header
v15 = v15.replace(
    'Written to `simulations/quest/rubrics/org-chart-rubric-v14-2026-03-16.md`.',
    'Written to `simulations/quest/rubrics/org-chart-rubric-v15-2026-03-16.md`.',
    1
)

# 2. Summary block (uses Unicode arrow)
old_summary_start = '**Summary of changes v13 \u2192 v14:**'
old_summary_end = 'V-05 scored full pass with all three combined. All three follow the same structural logic as prior rounds: A-34 converts implicit tier-count property into explicit per-tier accounting, A-35 converts per-charter field verification into a cross-charter completeness sweep, A-36 converts an embedded implicit category schema into an explicit named closed-set contract.'

new_summary = (
    '**Summary of changes v14 \u2192 v15:**\n'
    '\n'
    '| ID | Pattern | Block | Position | Additive to |\n'
    '|----|---------|-------|----------|--------------|\n'
    '| A-37 | `charter-rhythm-parity-verification` | `CHARTER-RHYTHM-PARITY:` | Between CHARTER-COMPLETENESS-AUDIT and CHARTERS COMPLETE gate | A-35 |\n'
    '| A-38 | `register-population-audit` | `REGISTER-POPULATION-AUDIT:` | After register body, before Org Evolution Roadmap | A-36 |\n'
    '| A-39 | `roadmap-trigger-diversity-verification` | `ROADMAP-TRIGGER-DIVERSITY:` | After Org Evolution Roadmap table, before Anti-Pattern Watch | A-11 |\n'
    '\n'
    '**Formula:** `/36 -> /39`\n'
    '\n'
    '**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/39 * 10)`\n'
    '\n'
    'All three follow the round pattern: implicit structural property promoted to an explicitly named verifiable contract. A-37 closes the bidirectional parity gap left open by A-35\'s field-completeness sweep: a charter can be field-complete while having no corresponding rhythm row, and a rhythm governance row can exist with no charter, neither violation surfaced by A-35. A-38 closes the category-population gap left open by A-36\'s closed-set declaration: a declared category with zero entries satisfies A-36 (no unlisted labels) but produces a silent empty slot invisible without counting category-grouped entries. A-39 closes the signal-type homogeneity gap left open by A-11\'s Observable Signal column requirement: three structurally present signals can all share a single trigger type, producing a formally passing but informationally redundant roadmap.\n'
    '\n'
    '**Derivation rationale:** Each R15 variation isolated one refinement axis. V-01 introduced a `CHARTER-RHYTHM-PARITY:` block between the CHARTER-COMPLETENESS-AUDIT block and the CHARTERS COMPLETE gate. The block presents a two-column charter-to-rhythm-row mapping confirming bidirectional correspondence: every charter names a rhythm table governance row, and every governance row has a charter. This closes the parity gap: A-35 confirms field completeness of each charter present but does not confirm that charters and rhythm rows are in 1:1 correspondence -- a governance meeting in the rhythm table without a charter, or a charter naming a meeting absent from the rhythm table, escapes A-35. V-02 introduced a `REGISTER-POPULATION-AUDIT:` block immediately after the register body, emitting one CATEGORY-POPULATED/CATEGORY-EMPTY row per category declared in the A-36 REGISTER-CATEGORY-CONTRACT block. This closes the population gap: A-36 prohibits unlisted category labels but is satisfied even when a declared category has zero entries; CATEGORY-EMPTY makes empty category slots a directly scannable row rather than a silent absence. The pattern is the direct register-domain parallel to A-34\'s TIER-ABSENT accounting. V-03 introduced a `ROADMAP-TRIGGER-DIVERSITY:` block after the Org Evolution Roadmap table, enumerating each Observable Signal with a declared trigger type from a closed set and emitting a type-diversity count with a minimum-two-distinct-types constraint. This closes the homogeneity gap: A-11 requires an Observable Signal column but not signal-type diversity; a roadmap with three tiers all signaled by capacity metrics satisfies A-11 while providing no discriminative trigger coverage. The diversity constraint promotes breadth from an implicit quality expectation to a count-verifiable structural requirement. V-05 scored full pass with all three combined. All three follow the same structural logic as prior rounds: A-37 converts implicit rhythm-charter correspondence into an explicit bidirectional parity contract, A-38 converts implicit category population into an explicit per-category accounting (parallel to A-34 for role tiers), A-39 converts implicit signal variety into an explicit type-diversity constraint.'
)

idx_start = v15.find(old_summary_start)
idx_end = v15.find(old_summary_end) + len(old_summary_end)
assert idx_start != -1, 'old_summary_start not found'
assert v15.find(old_summary_end) != -1, 'old_summary_end not found'
v15 = v15[:idx_start] + new_summary + v15[idx_end:]

# 3. Changelog: insert v15 entry before v14 entry
old_cl = '  v14 -- added A-34/A-35/A-36 from R14 excellence signals:'
new_cl_prefix = (
    '  v15 -- added A-37/A-38/A-39 from R15 excellence signals:\n'
    '  charter-rhythm-parity-verification (V-01 axis: CHARTER-RHYTHM-PARITY: block between\n'
    '  CHARTER-COMPLETENESS-AUDIT and CHARTERS COMPLETE gate; two-column table mapping each\n'
    '  charter to its rhythm table governance row; bidirectional -- every charter has a rhythm\n'
    '  row and every governance rhythm row has a charter; any missing correspondence blocks the\n'
    '  gate; additive to A-35 field-completeness sweep),\n'
    '  register-population-audit (V-02 axis: REGISTER-POPULATION-AUDIT: block immediately after\n'
    '  register body and before Org Evolution Roadmap; one row per category declared in A-36\n'
    '  REGISTER-CATEGORY-CONTRACT block; each row emits entry count and CATEGORY-POPULATED/\n'
    '  CATEGORY-EMPTY verdict; zero-entry category emits CATEGORY-EMPTY making population gap\n'
    '  a directly scannable row; additive to A-36 closed-set declaration; parallel to A-34\n'
    '  ROLE-TIER-ACCOUNTING pattern),\n'
    '  roadmap-trigger-diversity-verification (V-03 axis: ROADMAP-TRIGGER-DIVERSITY: block\n'
    '  after Org Evolution Roadmap table and before Anti-Pattern Watch; enumerates each\n'
    '  Observable Signal by tier with declared trigger type from named closed set; emits\n'
    '  type-diversity count; minimum two distinct trigger types required across all tier signals;\n'
    '  roadmap with fewer than two distinct trigger type labels is a constraint violation;\n'
    '  additive to A-11 Observable Signal column requirement).\n'
    '  Aspirational denominator updated from /36 to /39.\n'
    '  v14 -- added A-34/A-35/A-36 from R14 excellence signals:'
)
v15 = v15.replace(old_cl, new_cl_prefix, 1)

# 4. Aspirational header line
v15 = v15.replace(
    '## Aspirational Criteria (10 pts total, 1 pt each, denominator /36)',
    '## Aspirational Criteria (10 pts total, 1 pt each, denominator /39)',
    1
)

# 5. Append A-37/A-38/A-39 before footer
a37_39 = (
    '\n'
    '### A-37 -- CHARTER-RHYTHM-PARITY bidirectional correspondence block\n'
    '**Category:** correctness | **Weight:** aspirational\n'
    '\n'
    'When A-35 (CHARTER-COMPLETENESS-AUDIT cross-charter field sweep) is active, a\n'
    '`CHARTER-RHYTHM-PARITY:` block appears between the CHARTER-COMPLETENESS-AUDIT block and the\n'
    'CHARTERS COMPLETE phase gate. The block presents a two-column table -- charter name and\n'
    'corresponding rhythm table governance row -- confirming bidirectional parity: every charter\n'
    'entry has a matching governance row in the C-02 operating rhythm table, and every governance\n'
    'row in the C-02 rhythm table has a corresponding charter. Any charter without a rhythm table\n'
    'row, or any governance rhythm row without a charter, is a constraint violation that blocks the\n'
    'gate.\n'
    '\n'
    'A-35 confirms that each charter present in the document is field-complete. A-37 closes the\n'
    'parity gap: A-35 can be fully satisfied while rhythm table governance rows are missing charters\n'
    '(a governance meeting listed in C-02 with no charter document), or while charters name\n'
    'committees absent from the rhythm table (a charter with no corresponding meeting cadence).\n'
    'Neither failure mode is detectable by A-35\'s per-charter field inspection. The parity block\n'
    'promotes the rhythm-to-charter correspondence from an implicit structural expectation into an\n'
    'explicit bidirectional constraint whose absence is structurally detectable -- the block is\n'
    'either present and complete, or absent, with no intermediate state.\n'
    '\n'
    '**Pass condition:** A-35 active; a labeled `CHARTER-RHYTHM-PARITY:` block appears after the\n'
    'CHARTER-COMPLETENESS-AUDIT block and before the CHARTERS COMPLETE phase gate; block presents a\n'
    'two-column table mapping each charter to its corresponding rhythm table governance row; every\n'
    'governance row in the C-02 rhythm table has an entry in the table; every charter has a\n'
    'corresponding governance rhythm row; any charter-to-row or row-to-charter mismatch is flagged\n'
    'as a constraint violation; or criterion is N/A if A-35 is not active.\n'
    '\n'
    '---\n'
    '\n'
    '### A-38 -- REGISTER-POPULATION-AUDIT category entry count block\n'
    '**Category:** correctness | **Weight:** aspirational\n'
    '\n'
    'When A-36 (REGISTER-CATEGORY-CONTRACT closed-set declaration) is active, a\n'
    '`REGISTER-POPULATION-AUDIT:` block appears immediately after the register body and before the\n'
    'Org Evolution Roadmap (or equivalent next section). The block must emit one row per category\n'
    'label declared in the A-36 REGISTER-CATEGORY-CONTRACT block. Each row states the category\n'
    'name, the actual count of register entries using that category label, and a verdict of\n'
    '`CATEGORY-POPULATED` (count >= 1) or `CATEGORY-EMPTY` (count = 0). A category with zero\n'
    'entries emits `CATEGORY-EMPTY`, making the population gap a directly scannable row rather than\n'
    'a silent absence detectable only by counting category-grouped entries across the register body.\n'
    '\n'
    'A-36 declares the valid category set and prohibits unlisted labels. A-38 closes the population\n'
    'gap: A-36 is satisfied even when a declared category has zero entries, because zero entries\n'
    'produce no label violation. The population audit makes category population an explicit verifiable\n'
    'property that is the direct register-domain parallel to A-34\'s ROLE-TIER-ACCOUNTING pattern: a\n'
    'reviewer scans the CATEGORY-EMPTY rows rather than counting category-grouped entries across the\n'
    'full register body. The block is positioned after the register body so the count it emits\n'
    'reflects the completed register state.\n'
    '\n'
    '**Pass condition:** A-36 active; a labeled `REGISTER-POPULATION-AUDIT:` block appears\n'
    'immediately after the register body and before the Org Evolution Roadmap (or equivalent next\n'
    'section); block contains one row per category label declared in the A-36\n'
    'REGISTER-CATEGORY-CONTRACT block; each row names the category, states the entry count, and\n'
    'emits `CATEGORY-POPULATED` (count >= 1) or `CATEGORY-EMPTY` (count = 0); all categories\n'
    'declared in A-36 are represented -- no declared category is omitted from the audit; or criterion\n'
    'is N/A if A-36 is not active.\n'
    '\n'
    '---\n'
    '\n'
    '### A-39 -- ROADMAP-TRIGGER-DIVERSITY signal type diversity block\n'
    '**Category:** correctness | **Weight:** aspirational\n'
    '\n'
    'When A-11 (three-tier evolution roadmap with WATCH-FIRST trigger) is active, a\n'
    '`ROADMAP-TRIGGER-DIVERSITY:` block appears immediately after the Org Evolution Roadmap table\n'
    'and before the Anti-Pattern Watch section (or equivalent next section). The block must enumerate\n'
    'each Observable Signal from the roadmap\'s Observable Signal column, assign each signal a\n'
    'declared trigger type from a named closed set (e.g., Capacity / Process / Strategic / Cultural /\n'
    'External), and emit a type-diversity count across all tier signals. The minimum diversity\n'
    'requirement is that at least two distinct trigger types must be represented across all roadmap\n'
    'tier signals. A roadmap where all Observable Signal entries share the same trigger type fails\n'
    'the diversity requirement even if all other roadmap criteria (A-11) are satisfied.\n'
    '\n'
    'A-11 requires an Observable Signal column and a WATCH-FIRST declaration naming a specific signal.\n'
    'A-39 closes the homogeneity gap: A-11 is satisfiable with three Observable Signals that all\n'
    'describe the same class of trigger (e.g., all three tiers signaled by headcount metrics), which\n'
    'produces a roadmap that is structurally present but informationally redundant -- the roadmap\n'
    'cannot discriminate between trigger conditions if all signals share the same underlying type.\n'
    'The diversity block promotes signal-type breadth from an implicit quality expectation into an\n'
    'explicit count-verifiable structural constraint: a reviewer confirms diversity by counting\n'
    'distinct trigger type labels against the declared minimum of two, not by qualitatively assessing\n'
    'signal descriptions for variety.\n'
    '\n'
    '**Pass condition:** A-11 active; a labeled `ROADMAP-TRIGGER-DIVERSITY:` block appears immediately\n'
    'after the Org Evolution Roadmap table and before the Anti-Pattern Watch section (or equivalent);\n'
    'block enumerates each Observable Signal by tier with a declared trigger type from a named closed\n'
    'set; block emits a type-diversity count; at least two distinct trigger types are represented\n'
    'across all tier signals; a roadmap with fewer than two distinct trigger type labels across all\n'
    'tiers is a constraint violation; or criterion is N/A if A-11 is not active.\n'
    '\n'
    '---\n'
    '\n'
)

old_footer_anchor = '\n**Formula:** `aspirational_pass/36 * 10`'
assert v15.count(old_footer_anchor) == 1, f'expected 1 match, got {v15.count(old_footer_anchor)}'
v15 = v15.replace(old_footer_anchor, a37_39 + '**Formula:** `aspirational_pass/39 * 10`', 1)

# 6. Composite footer
v15 = v15.replace(
    '**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/36 * 10)`\n\n**Golden threshold:**',
    '**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/39 * 10)`\n\n**Golden threshold:**',
    1
)

open(v15_path, 'w', encoding='utf-8').write(v15)
print('Written:', v15_path)
print('v14 size:', len(v14), '| v15 size:', len(v15))

# Sanity checks
assert 'A-37' in v15
assert 'A-38' in v15
assert 'A-39' in v15
assert 'denominator /39' in v15
assert 'aspirational_pass/39' in v15
assert 'Summary of changes v14' in v15
assert 'v15 -- added A-37' in v15
assert 'CHARTER-RHYTHM-PARITY' in v15
assert 'REGISTER-POPULATION-AUDIT' in v15
assert 'ROADMAP-TRIGGER-DIVERSITY' in v15
print('All assertions passed.')
