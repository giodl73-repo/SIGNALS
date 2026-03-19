import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('/tmp/rubric_v16.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# ---- 1. Find insertion point for new criteria rows (before Scoring Summary) ----
insert_at = content.find('\n\n---\n\n## Scoring Summary')

# ---- 2. New criteria rows ----
c42 = (
    '| C-42 | **Audit block field for inventory gate compliance** '
    '\u2014 The Role 3 audit block must contain a named field that explicitly checks the inventory gate mechanism (C-41) reached its cleared state before Step 1A opened. '
    'The prior audit contract (Fields 1\u20134: T-NN threading, registry gap, load-shape classification, annotation dropout) verifies the body-construction output but does not confirm that the C-41 gate was used correctly \u2014 the gate state is invisible to Fields 1\u20134 without re-reading Phase 1\'s entry condition. '
    'C-42 extends the audit contract to make gate compliance a first-class audit target: the gate outcome (GATE CLEARED, ACTIVATION STATUS = PROCEED, INVENTORY VERIFIED, or equivalent) must be stated in the audit block as an independently checkable record, not inferred from the absence of body-content gaps. '
    'This parallels Field 1 (T-NN threading confirmed in audit without re-reading each body section) applied to the C-41 gate: C-41 requires the gate to block Phase 1 when the count is below the declared value; C-42 requires evidence of that gate\'s cleared outcome to appear in Role 3, making gate compliance verifiable without traversing the Phase 1 entry section. '
    '| structure | '
    'The Role 3 audit block contains a named field (Field 5 or equivalent) that explicitly checks C-41 gate compliance \u2014 confirming that the inventory gate reached CLEARED / PROCEED / INVENTORY VERIFIED (or equivalent) before Step 1A began. '
    'The field must state a PASS or FAIL verdict based on the gate outcome, not infer compliance from downstream output quality. '
    'A Role 3 audit with Fields 1\u20134 but no gate-compliance field fails this criterion. '
    'An audit that states "C-41 PASS" without referencing the gate mechanism\'s outcome also fails. |'
)

c43 = (
    '| C-43 | **Two-signal handoff chain for inventory verification** '
    '\u2014 The inventory verification step uses two distinct named signals \u2014 one received from Role 1 (FORMAT CONTRACT COMPLETE or equivalent) and one emitted to Role 2 (INVENTORY VERIFIED or equivalent) \u2014 rather than a single gate status field embedded in Role 2\'s entry condition. '
    'The structural necessity: FORMAT CONTRACT COMPLETE confirms that Role 1\'s sections are present; it does not verify that the annotation inventory is complete to its declared count. '
    'A single signal cannot distinguish "sections present" from "count verified." '
    'The two-signal chain resolves this conflation by assigning single responsibility to the intermediate verification step: its activation signal is FORMAT CONTRACT COMPLETE (section presence confirmed); its handoff signal is INVENTORY VERIFIED (count completeness confirmed); its only function is to confirm count = declared count. '
    'Role 2\'s entry condition checks the handoff signal by name \u2014 a Role 2 that activates on FORMAT CONTRACT COMPLETE alone bypasses count verification. '
    'This parallels C-36 (C-34 count stated at path labels \u2192 C-36 count as Role 3 activation condition) applied to the verification role\'s signal design: C-41 requires a Phase 1 gate; C-43 requires that gate to manifest as a dedicated verification step whose activation and handoff signals are named distinctly, making the "sections present vs. count verified" distinction structurally visible in the role sequence. '
    '| structure | '
    'An intermediate verification role or step (Role 1.5, INVENTORY VERIFIER, or equivalent) is present with: (a) a named activation signal received from Role 1 (FORMAT CONTRACT COMPLETE or equivalent), (b) a distinct named handoff signal emitted to Role 2 (INVENTORY VERIFIED or equivalent) on count success, (c) a return signal (INVENTORY INCOMPLETE or equivalent) that prevents Role 2 activation when count fails, and (d) a stated single responsibility (count verification only \u2014 no analysis output). '
    'Role 2\'s entry condition checks the handoff signal by name. '
    'An output where a single FORMAT CONTRACT COMPLETE signal both closes Role 1 and opens Role 2\'s entry condition (no intermediate verification role with its own signals) fails this criterion. '
    'An output that passes C-41 using a gate status field inside Role 2\'s PHASE ENTRY CONDITION without a dedicated verification role also fails C-43. |'
)

c44 = (
    '| C-44 | **Inertia-frame rejection at the inventory verification boundary** '
    '\u2014 The inventory verification gate must name the bypass failure mode \u2014 the "looks complete" framing or equivalent \u2014 and provide a structural proof that the bypass is self-defeating. '
    'The bypass temptation: because FORMAT CONTRACT COMPLETE has been stated and analysis tables are scaffolded, proceeding directly to Role 2 without verification appears to miss no required steps. '
    'The proof that the bypass fails: (1) FORMAT CONTRACT COMPLETE confirms that Role 1\'s sections are present; (2) it does not verify that Section C is complete to its declared count; (3) a partial Section C (e.g., 6 of 7 annotations) satisfies section presence while failing count verification; (4) bypassing the gate converts the Section C count from a verifiable gate into an unverified assertion \u2014 a discrepancy is detectable only after Role 2 has produced output, not before. '
    'This is structurally parallel to C-26 (escape-route frame at Step 1B: naming the "STATUS tracks volume thresholds" deferral temptation and proving it creates a circular dependency). '
    'C-26 converts load-shape classification from a deferrable step to a logical necessity by showing that Step 2G depends on the per-tier verdicts that Step 1B supplies; C-44 converts inventory count verification from a policy gate to a logical necessity by showing that FORMAT CONTRACT COMPLETE\'s section-presence guarantee does not subsume count completeness. '
    'An output that includes the gate mechanism (C-41 PASS) but states only that count must equal declared count \u2014 without naming the bypass temptation or providing the proof that FORMAT CONTRACT COMPLETE \u2260 count completeness \u2014 fails C-44. '
    '| structure | '
    'The inventory verification gate or role includes: (a) a named bypass failure mode (the "looks complete" framing, "FORMAT CONTRACT COMPLETE implies completeness," or equivalent) and (b) a structural proof that the bypass is self-defeating, distinguishing section presence (what FORMAT CONTRACT COMPLETE confirms) from count completeness (what the gate verifies), and stating that a partial Section C satisfies section presence while failing count verification. '
    'The proof must make the logical necessity of the gate explicit \u2014 not just assert that count must be verified, but show why bypassing produces a weaker guarantee. '
    'An output that passes C-41 (gate present) but omits the inertia-frame proof fails C-44. |'
)

new_rows = '\n' + c42 + '\n' + c43 + '\n' + c44

# Insert new rows before the scoring summary separator
content_v17 = content[:insert_at] + new_rows + content[insert_at:]

# ---- 3. Header updates ----
content_v17 = content_v17.replace(
    '# flow-throttle Rubric \u2014 v16',
    '# flow-throttle Rubric \u2014 v17'
)
content_v17 = content_v17.replace(
    '**Skill**: `flow:throttle` | **Version**: v16 | **Date**: 2026-03-16\n**Max composite**: 255 | **Golden threshold**: all 5 essential PASS + composite >= 80',
    '**Skill**: `flow:throttle` | **Version**: v17 | **Date**: 2026-03-16\n**Max composite**: 270 | **Golden threshold**: all 5 essential PASS + composite >= 80'
)

# ---- 4. Update old scoring formula line ----
content_v17 = content_v17.replace(
    '**Scoring formula update**: Aspirational raised from 160 pts (32 \xd7 5) to 165 pts (33 \xd7 5), max composite 250 \u2192 255. Golden threshold unchanged at 80 + all essential PASS.',
    '**Scoring formula update**: Aspirational raised from 165 pts (33 \xd7 5) to 180 pts (36 \xd7 5), max composite 255 \u2192 270. Golden threshold unchanged at 80 + all essential PASS.'
)

# ---- 5. Insert new What Changed entries for C-42, C-43, C-44 before the scoring formula line ----
new_wc_entries = (
    '**C-42 \u2014 Audit block field for inventory gate compliance** (new aspirational, from v17)\n'
    'All five R16 variations add a named Audit Field 5 to the Role 3 audit block that explicitly checks the C-41 gate mechanism: Field 5 confirms that the inventory gate reached its CLEARED / PROCEED / INVENTORY VERIFIED state before Step 1A began. '
    'V-01: "Field 5 \u2014 INVENTORY GATE compliance (C-41): The INVENTORY GATE was reached before Phase 1 opened. GATE STATUS was explicitly set to CLEARED before Step 1A began." '
    'V-02: ACTIVATION STATUS = PROCEED. V-03 and V-05: Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED. V-04: PHASE 1 ENTRY CONDITION STATUS = CLEARED. '
    'The pattern: C-41 requires the gate to block Phase 1 when the count is below the declared value; C-42 requires the gate\'s outcome to be independently verifiable in the audit block \u2014 a Role 3 audit limited to Fields 1\u20134 (T-NN threading, registry gap, load-shape, annotation dropout) cannot confirm that the gate was used correctly without re-reading the gate section. '
    'C-42 makes gate compliance a first-class audit target: the gate state must be stated, not inferred. '
    'The structural parallel: Field 1 (T-NN threading confirmed in Role 3 without re-reading each body section) applied to the C-41 gate mechanism \u2014 C-41 requires the gate to exist and block; C-42 requires the gate\'s cleared state to be explicitly recorded in Role 3.\n\n'
    '**C-43 \u2014 Two-signal handoff chain for inventory verification** (new aspirational, from v17)\n'
    'V-03 and V-05 both use a dedicated intermediate role (Role 1.5 \u2014 INVENTORY VERIFIER) that creates a two-signal handoff chain: FORMAT CONTRACT COMPLETE (Role 1 \u2192 Role 1.5) and INVENTORY VERIFIED (Role 1.5 \u2192 Role 2). '
    'The insight from V-05\'s inertia frame makes the structural necessity explicit: FORMAT CONTRACT COMPLETE confirms that Role 1\'s sections are present \u2014 it does not verify that the annotation inventory is complete to its declared count. '
    'A partial Section C (e.g., 6 of 7 annotations) satisfies section presence while failing count verification. '
    'When a single gate status field embedded in Role 2\'s entry condition (C-41\'s minimum pass form) serves as the only transition, the signal that closes Role 1 and the signal that opens Role 2 are conflated \u2014 "sections present" and "count verified" are indistinguishable. '
    'The two-signal chain resolves this conflation: Signal 1 (FORMAT CONTRACT COMPLETE) confirms Role 1 completion; Signal 2 (INVENTORY VERIFIED) confirms count correctness. '
    'Role 1.5 has single responsibility \u2014 its only job is to confirm count = declared; it "has no other responsibility and produces no analysis output." '
    'Role 2\'s entry condition checks Signal 2 by name; a Role 2 that activates on Signal 1 alone bypasses count verification. '
    'This parallels the C-34\u2192C-36 structural argument applied to the verification role\'s signal design: C-41 requires a Phase 1 gate; C-43 requires that gate to use a distinct verification role whose activation signal is separate from Role 1\'s completion signal.\n\n'
    '**C-44 \u2014 Inertia-frame rejection at the inventory verification boundary** (new aspirational, from v17)\n'
    'V-05 names and rejects the bypass failure mode at the inventory verification gate \u2014 the "looks complete" framing \u2014 with a structural proof that the bypass is self-defeating. '
    'The proof has four steps: (1) FORMAT CONTRACT COMPLETE confirms that Role 1\'s sections are present; (2) it does not verify that Section C is complete to its declared count; (3) a partial Section C satisfies Role 1\'s section presence check while failing the count declared in Section C\'s header; (4) bypassing the gate converts the Section C count from a verifiable gate into an unverified assertion \u2014 a discrepancy is detectable only after Role 2 has produced output, not before. '
    'This is structurally parallel to C-26 (escape-route frame at Step 1B proving that load-shape classification cannot be deferred without creating a circular dependency). '
    'C-26 names the "STATUS tracks volume thresholds" deferral temptation and proves it is self-defeating because Step 2G depends on per-tier verdicts that Step 1B is supposed to supply; '
    'C-44 names the "looks complete / FORMAT CONTRACT COMPLETE implies completeness" bypass temptation and proves it is self-defeating because FORMAT CONTRACT COMPLETE confirms section presence, not count completeness. '
    'Both proofs convert a policy prohibition into a logical necessity: you cannot satisfy the downstream requirement by skipping the intermediate step. '
    'An output that passes C-41 (gate mechanism present) but omits the inertia-frame proof fails C-44.\n\n'
)

content_v17 = content_v17.replace(
    '**Scoring formula update**: Aspirational raised from 165 pts (33 \xd7 5) to 180 pts (36 \xd7 5), max composite 255 \u2192 270. Golden threshold unchanged at 80 + all essential PASS.',
    new_wc_entries + '**Scoring formula update**: Aspirational raised from 165 pts (33 \xd7 5) to 180 pts (36 \xd7 5), max composite 255 \u2192 270. Golden threshold unchanged at 80 + all essential PASS.'
)

# ---- 6. Scoring Summary update ----
content_v17 = content_v17.replace(
    '| Aspirational | C-09 \u2013 C-41 | 5 pts each | 165 |\n| **Total** | | | **255** |',
    '| Aspirational | C-09 \u2013 C-44 | 5 pts each | 180 |\n| **Total** | | | **270** |'
)

# ---- 7. Structural Progression Table: add 7th column ----
old_header = (
    '| Instructional layer | Contract-lock layer | Count-closed layer | Closure-declared layer | Prohibition-enforced layer | Role-gate layer |\n'
    '|---------------------|---------------------|--------------------|------------------------|----------------------------|-----------------|'
)
new_header = (
    '| Instructional layer | Contract-lock layer | Count-closed layer | Closure-declared layer | Prohibition-enforced layer | Role-gate layer | Audit-covered layer |\n'
    '|---------------------|---------------------|--------------------|------------------------|----------------------------|-----------------|--------------------|'
)
content_v17 = content_v17.replace(old_header, new_header)

content_v17 = content_v17.replace(
    '| C-33 field-count declared | C-35 field-count contract-locked | \u2014 | \u2014 | \u2014 | \u2014 |',
    '| C-33 field-count declared | C-35 field-count contract-locked | \u2014 | \u2014 | \u2014 | \u2014 | \u2014 |'
)
content_v17 = content_v17.replace(
    '| C-34 observable-count at path labels | C-36 observable-count as role-activation condition | \u2014 | \u2014 | \u2014 | \u2014 |',
    '| C-34 observable-count at path labels | C-36 observable-count as role-activation condition | \u2014 | \u2014 | \u2014 | \u2014 | \u2014 |'
)
content_v17 = content_v17.replace(
    '| C-18 annotation required at anchor | C-37 annotation inventory contract-locked | C-38 count declared | C-39 inventory closed | C-40 dropout PROHIBITED + annotation | **C-41** count as Phase 1 role-activation gate |',
    '| C-18 annotation required at anchor | C-37 annotation inventory contract-locked | C-38 count declared | C-39 inventory closed | C-40 dropout PROHIBITED + annotation | C-41 count as Phase 1 role-activation gate | **C-42** gate compliance in audit block |'
)

# ---- 8. Append C-43 / C-44 note after the structural table ----
table_end_marker = '| C-18 annotation required at anchor | C-37 annotation inventory contract-locked | C-38 count declared | C-39 inventory closed | C-40 dropout PROHIBITED + annotation | C-41 count as Phase 1 role-activation gate | **C-42** gate compliance in audit block |'
table_end_pos = content_v17.find(table_end_marker) + len(table_end_marker)

c43_c44_note = (
    '\n\n'
    '**C-43 and C-44** extend the C-41 gate design and do not add a new progression column:\n'
    '- **C-43** (two-signal handoff chain) requires the gate to manifest as a dedicated verification role with distinct activation and handoff signals, making "sections present" vs. "count verified" structurally distinguishable.\n'
    '- **C-44** (inertia-frame rejection) requires the gate to include a named bypass failure mode with a structural proof that FORMAT CONTRACT COMPLETE confirms section presence but not count completeness \u2014 parallel to C-26 (escape-route frame at Step 1B).'
)

content_v17 = content_v17[:table_end_pos] + c43_c44_note + content_v17[table_end_pos:]

# ---- Write output ----
with open('/tmp/rubric_v17.md', 'w', encoding='utf-8') as f:
    f.write(content_v17)

print('Done. Length:', len(content_v17))
checks = [
    ('v17 header', '# flow-throttle Rubric \u2014 v17'),
    ('Max composite 270', '**Max composite**: 270'),
    ('C-42 What Changed', '**C-42 \u2014 Audit block field'),
    ('C-43 What Changed', '**C-43 \u2014 Two-signal'),
    ('C-44 What Changed', '**C-44 \u2014 Inertia-frame'),
    ('Scoring formula 180', 'Aspirational raised from 165 pts (33'),
    ('C-42 criteria row', '| C-42 | **Audit block field'),
    ('C-43 criteria row', '| C-43 | **Two-signal handoff'),
    ('C-44 criteria row', '| C-44 | **Inertia-frame rejection'),
    ('Scoring summary 270', '| **Total** | | | **270** |'),
    ('Structural table 7 cols', 'Audit-covered layer'),
    ('C-43 C-44 note in table', 'C-43 and C-44** extend'),
]
for name, text in checks:
    found = text in content_v17
    print('  %s: %s' % ('OK' if found else 'FAIL', name))
