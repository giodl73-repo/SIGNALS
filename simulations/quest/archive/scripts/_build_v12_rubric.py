"""Build listen-support-rubric-v12-2026-03-15.md from v11 + three new criteria."""
import os
os.chdir('C:/src/sim')

with open('simulations/quest/rubrics/listen-support-rubric-v11-2026-03-15.md') as f:
    v11 = f.read()

c04_start = v11.find('### C-04')
sum_start = v11.find('## Scoring Summary')

mid = v11[c04_start:sum_start].replace(
    'normalized across 24 criteria)\n\nEach full pass = 10/24 pts (~0.417). Each partial = 10/48 pts (~0.208).',
    'normalized across 27 criteria)\n\nEach full pass = 10/27 pts (~0.370). Each partial = 10/54 pts (~0.185).'
)

old_sum = v11[sum_start:]
new_sum = old_sum.replace(
    '| C-32 | SRE-first structural priority ordering | aspirational | depth |',
    '| C-32 | SRE-first structural priority ordering | aspirational | depth |\n'
    '| C-33 | Bound-variable bracket-token propagation | aspirational | behavior |\n'
    '| C-34 | Propagation chain pre-declaration | aspirational | behavior |\n'
    '| C-35 | SRE-write-first enforcement gate | aspirational | correctness |'
).replace(
    '**Dependency stacks**:',
    '**C-33 dependency**: only scoreable when C-31 passes.\n\n'
    '**C-34 dependency**: only scoreable when C-31 passes.\n\n'
    '**C-35 dependency**: only scoreable when C-32 passes.\n\n'
    '**C-33 vs C-31**: C-31 requires the declared competitor name to be referenced by variable in at least'
    ' one step instruction (prose acceptable); C-33 requires the reference to use literal bracket-variable'
    ' token syntax embedded in table headers or step instruction action clauses, making propagation'
    ' detectable by bracket-pattern scan rather than prose interpretation.'
    ' Prose variable reference vs. bracket-token embedding.\n\n'
    '**C-34 vs C-31**: C-31 requires the preamble to declare the bound variable and requires three'
    ' checkpoints to exist in the output; C-34 requires the preamble to additionally enumerate all three'
    ' checkpoint labels as a named PROPAGATION CHAIN sub-block, creating a pre-declared contract against'
    ' which output completeness can be verified by comparison rather than traversal.'
    ' Checkpoint existence in output vs. checkpoint contract in preamble before generation.\n\n'
    '**C-35 vs C-32**: C-32 requires SRE-first position in both core tables, an advisory write-first'
    ' directive, and a post-hoc VALIDATION TRACE ordering check; C-35 requires a named gate block at the'
    ' table-to-body boundary that produces a binary verdict and blocks body writing until SRE-first'
    ' position is verified.'
    ' Advisory ordering commitment plus retrospective check vs. between-step enforcement gate.\n\n'
    '**Dependency stacks**:'
).replace(
    '`C-09 -> C-15 -> C-31`\n- `C-12',
    '`C-09 -> C-15 -> C-31 -> C-33`\n- `C-09 -> C-15 -> C-31 -> C-34`\n- `C-12'
).replace(
    '- `C-32` (independent)',
    '- `C-32 -> C-35`\n- `C-32` (independent)'
)

HEADER = (
    '# listen-support Rubric v12\n'
    '**Skill**: `listen:support`\n'
    '**Version**: 12\n'
    '**Date**: 2026-03-15\n'
    '**Criteria count**: 35 (5 essential, 3 recommended, 27 aspirational)\n'
    '**Changes from v11**: Added C-33 (Bound-Variable Bracket-Token Propagation),'
    ' C-34 (Propagation Chain Pre-Declaration), C-35 (SRE-Write-First Enforcement Gate)'
    ' from Round 11 excellence signals.\n'
    '\n'
    '---\n'
    '\n'
    '## Essential Criteria (weight = 50 pts total, 10 pts each)\n'
    '\n'
    '### C-01 -- Ticket Structural Completeness\n'
    '- **Category**: correctness\n'
    '- **Weight**: essential\n'
    '- **Text**: Each predicted ticket contains all required structural fields: a title, a category'
    ' (from the defined set), a severity level, a volume estimate, an assigned persona, and a sample'
    ' body. Missing any of these fields in any ticket constitutes a structural failure for that ticket.\n'
    '- **Pass condition**: All tickets in the predicted set contain all six required fields: title,'
    ' category, severity, volume, persona, sample body. A ticket missing any required field fails this'
    ' criterion for the full set -- the criterion requires the entire predicted ticket set to be'
    ' structurally complete, not just a subset.\n'
    '\n'
    '---\n'
    '\n'
    '### C-02 -- Valid Category/Severity/Volume Values\n'
    '- **Category**: correctness\n'
    '- **Weight**: essential\n'
    '- **Text**: Each ticket uses only values from the defined controlled vocabularies:'
    ' category from `{how-to, bug, feature-request, config, integration}`,'
    ' severity from `{P0, P1, P2, P3}`, volume from `{low, medium, high}`.'
    ' Values outside these sets indicate unconstrained generation.\n'
    '- **Pass condition**: Every ticket uses valid values from the controlled vocabulary sets for all'
    ' three enumerated fields. Any invalid, missing, or invented value -- including synonyms not in the'
    ' set (e.g., "critical" for P0) -- constitutes a failure.\n'
    '\n'
    '---\n'
    '\n'
    '### C-03 -- Persona Grounding from Stock Set\n'
    '- **Category**: correctness\n'
    '- **Weight**: essential\n'
    '- **Text**: Each ticket is assigned to a persona from the defined stock persona set'
    ' (SRE, PM, Developer, Support Engineer, Data Engineer, or equivalents named in the'
    " skill's persona registry). Invented personas, unlabeled entries, or role labels not"
    ' in the stock set fail this criterion.\n'
    '- **Pass condition**: All persona assignments match entries in the defined stock persona set.'
    ' No invented or unlabeled personas appear in the ticket set. A set where any persona label'
    ' cannot be traced to the stock registry fails.\n'
    '\n'
    '---\n'
    '\n'
)

NEW_CRITERIA = (
    '\n'
    '### C-33 -- Bound-Variable Bracket-Token Propagation\n'
    '- **Category**: behavior\n'
    '- **Weight**: aspirational\n'
    '- **Source**: Round 11 excellence signal -- V-01 literal `[INERTIA COMPETITOR]` bracket-variable'
    ' token embedded in table column header and step instruction body; advancement over C-31'
    " prose-reference checkpoint (b)\n"
    '- **Text**: C-31 requires at least one step instruction to reference the declared competitor name'
    ' "by variable" -- a prose reference like "use the name declared in the INERTIA COMPETITOR preamble"'
    ' satisfies C-31 checkpoint (b). C-33 advances this by requiring the declared competitor name to'
    ' appear as a literal bracket-variable token (e.g., `[INERTIA COMPETITOR]`) embedded directly in'
    ' at least one table column header or step instruction text body. With bracket-token syntax,'
    ' propagation is detectable by scanning for the bracket pattern -- any column header or instruction'
    ' that should reference the competitor but instead contains only prose or a hardcoded name is'
    ' immediately visible without interpreting prose meaning. Without bracket-token syntax, detecting'
    ' whether propagation occurred requires reading and interpreting the prose of each instruction;'
    ' with it, token presence is mechanically verifiable. The advancement is structurally analogous to'
    ' C-18 advance over C-16: C-16 requires markers named (prose list acceptable); C-18 requires'
    ' markers dimension-labeled (structurally classifying). C-31 requires the variable referenced'
    ' (prose acceptable); C-33 requires the variable referenced using token syntax'
    ' (structurally scannable by bracket pattern).\n'
    '- **Pass condition**: The literal token `[INERTIA COMPETITOR]` (or equivalent bracket-variable'
    ' form whose bracket syntax matches the preamble declaration format) appears in at least one table'
    ' column header or step instruction text body -- not only in a framing sentence before the'
    ' instruction, but embedded in the instruction action clause or the column label itself'
    ' (e.g., as a table column header, or as the subject within a step action). The token must match'
    ' the preamble declaration form. A prose instruction that names the variable without bracket syntax'
    ' satisfies C-31 checkpoint (b) but fails C-33 -- bracket-token embedding is the distinguishing'
    ' requirement.\n'
    '- **Anti-pattern**: Prose reference to "the competitor declared in the preamble" or "the INERTIA'
    ' COMPETITOR name" in step instructions satisfies C-31 checkpoint (b) but not C-33. A bracket token'
    ' appearing only in the preamble declaration itself without embedding in downstream step instructions'
    ' also fails -- the test is downstream token propagation, not declaration token syntax. A bracket'
    ' token in a post-generation confirmation block without embedding in step instructions also fails'
    ' -- confirmation reference is not step-level propagation.\n'
    '- **Dependency**: Only scoreable if C-31 passes. If C-31 fails, C-33 scores 0.\n'
    '\n'
    '---\n'
    '\n'
    '### C-34 -- Propagation Chain Pre-Declaration\n'
    '- **Category**: behavior\n'
    '- **Weight**: aspirational\n'
    '- **Source**: Round 11 excellence signal -- V-01 PROPAGATION CHAIN block in the labeled preamble'
    ' before Step 1 names all three downstream checkpoint labels (A, B, C) before any step executes;'
    ' creates a checkpoint contract that makes missing checkpoints detectable by'
    ' declaration-against-output comparison rather than discovery-by-traversal\n'
    '- **Text**: C-31 requires the preamble to declare the competitor name as a bound variable and'
    ' requires three downstream checkpoints to exist in the output. C-31 does not require the preamble'
    ' to enumerate the checkpoint labels -- the three checkpoints can exist in the output without being'
    ' contracted in advance. C-34 requires the preamble to additionally contain a PROPAGATION CHAIN'
    ' sub-block that names all three checkpoint labels before Step 1 executes. With the chain contract'
    ' in place, the complete checkpoint structure is committed before any step runs: a reviewer can'
    ' confirm chain completeness by comparing the declared checkpoint labels against the output in a'
    ' single traversal, and any missing checkpoint is a visible deviation from the declared contract.'
    ' Without the contract, checkpoint completeness requires discovering each one by traversal without'
    ' a reference list -- completeness is inferred, not declared. The pattern is structurally analogous'
    ' to C-29 advance over C-27: C-27 requires the floor to be achieved (detected post-generation);'
    ' C-29 requires the floor to be committed before generation begins (declared pre-generation).'
    ' C-31 requires the checkpoints to exist in the output; C-34 requires the checkpoints to be'
    ' contracted before generation, shifting verification from traversal-based discovery to'
    ' declaration-against-contract comparison.\n'
    '- **Pass condition**: The labeled preamble block (required by C-31 before Step 1) includes a'
    ' PROPAGATION CHAIN sub-block or equivalent named structure that enumerates all three checkpoint'
    ' labels (labeled as a/b/c, as A/B/C, or with equivalent explicit identifiers) before any'
    ' generation step executes. The chain declaration must name the checkpoints individually -- a prose'
    ' statement without labeling each checkpoint identifier fails because it declares count without'
    ' making each checkpoint individually matchable by label. The checkpoint labels in the declaration'
    ' must correspond to checkpoints that are verifiably present in the output.\n'
    '- **Anti-pattern**: A preamble that declares the competitor variable and asserts propagation will'
    ' occur through three checkpoints without naming individual checkpoint identifiers fails -- count'
    ' assertion without label contract does not provide the pre-declaration property. A post-generation'
    ' confirmation block (C-31 checkpoint c) that lists the three checkpoints retrospectively satisfies'
    ' C-31 but fails C-34 because the contract was not established before generation. Naming the'
    ' checkpoints in a post-section summary rather than the preamble also fails -- the contract must'
    ' appear before Step 1, not after. Satisfying the three checkpoint labels in the output body'
    ' without a matching declaration in the preamble satisfies C-31 but fails C-34.\n'
    '- **Dependency**: Only scoreable if C-31 passes. If C-31 fails, C-34 scores 0.\n'
    '\n'
    '---\n'
    '\n'
    '### C-35 -- SRE-Write-First Enforcement Gate\n'
    '- **Category**: correctness\n'
    '- **Weight**: aspirational\n'
    '- **Source**: Round 11 excellence signal -- V-02 SRE-WRITE-FIRST GATE block between PERSONA VOICE'
    ' TABLE step (Step 5) and body-writing step (Step 6); structural enforcement gate that blocks'
    ' forward progress until SRE-first position is verified; advancement over C-32 advisory write-first'
    ' directive plus post-hoc VALIDATION TRACE check\n'
    '- **Text**: C-32 requires SRE-first position in both core persona-indexed tables, an explicit'
    ' write-first directive before body writing, and a VALIDATION TRACE ordering check. The write-first'
    ' directive states intent before the table is built; the trace verifies ordering after all content'
    ' is complete. Neither blocks body writing if the SRE row was placed second or third in the table.'
    ' C-35 introduces a structural enforcement gate between the table-construction step and the'
    ' body-writing step: a named gate block that checks whether the SRE row is first in the PERSONA'
    ' VOICE TABLE and explicitly halts body writing until the check passes. With the enforcement gate,'
    ' SRE-first position in the table is a pre-condition for advancing to body writing -- a table'
    ' generated with a different persona first cannot proceed to body writing without a visible gate'
    ' failure. Without the gate, a table built with the wrong ordering can proceed silently to body'
    ' writing, with the error discovered only in the post-hoc VALIDATION TRACE (or not at all). The'
    ' pattern is structurally analogous to C-22 advance over C-20: C-20 requires the bidirectional'
    ' verification to occur; C-22 requires it to be binding -- MISMATCH must halt before proceeding.'
    ' C-32 requires the write-first directive and ordering check to exist; C-35 requires the'
    ' write-first check to be binding -- SRE-not-first must halt before body writing begins.\n'
    '- **Pass condition**: A named gate block appears in the output at the boundary between the PERSONA'
    ' VOICE TABLE generation step and the body-writing step (or between any persona-indexed'
    ' table-construction step and the next generation step that depends on ordering). The gate block'
    ' must: (a) explicitly name what it is checking (SRE-first position in the PERSONA VOICE TABLE or'
    ' equivalent persona-indexed table), (b) produce a binary PASS/FAIL or PROCEED/HALT verdict, and'
    ' (c) include an explicit gate instruction that requires correction and re-verification before'
    ' advancing if the SRE row is not first (e.g., "if SRE is not first: reorder before proceeding'
    ' to Step 6"). The gate must be a named structural element -- not embedded as a sentence in'
    ' body-prose -- and must appear between steps, not after all content is generated. A VALIDATION'
    ' TRACE ordering check appearing after body writing satisfies C-32 but fails C-35 -- post-hoc'
    ' verification is not a pre-body enforcement gate.\n'
    '- **Anti-pattern**: A write-first directive in step instructions satisfies C-32 write-first'
    ' directive requirement but fails C-35 -- a directive is advisory: it states the intended order'
    ' but does not gate forward progress on confirmation that the order was followed. A VALIDATION'
    ' TRACE ordering check appearing anywhere after body writing satisfies C-32 but fails C-35 because'
    ' the check is retrospective rather than a structural barrier before body writing. An ordering'
    ' check embedded in C-11 pre-generation validation trace also fails C-35 because it does not'
    ' constitute a between-step gate at the table-to-body boundary.\n'
    '- **Dependency**: Only scoreable if C-32 passes. If C-32 fails, C-35 scores 0.\n'
    '\n'
    '---\n'
    '\n'
)

# Remove stale aspirational scoring note from v11 tail if present
new_sum = new_sum.replace(
    '\n\n**Aspirational scoring**: 24 criteria. Full pass = 10/24 pts (~0.417). Partial = 10/48 pts (~0.208). Max aspirational = 10 pts.\n',
    '\n'
)

v12 = HEADER + mid + NEW_CRITERIA + new_sum

with open('simulations/quest/rubrics/listen-support-rubric-v12-2026-03-15.md', 'w') as f:
    f.write(v12)

print(f'Written {len(v12)} bytes')

checks = [
    '# listen-support Rubric v12',
    '### C-01 -- Ticket Structural Completeness',
    '### C-03 -- Persona Grounding from Stock Set',
    'normalized across 27 criteria',
    '### C-33 -- Bound-Variable Bracket-Token Propagation',
    '### C-34 -- Propagation Chain Pre-Declaration',
    '### C-35 -- SRE-Write-First Enforcement Gate',
    'C-33 | Bound-variable bracket-token propagation',
    'C-35 | SRE-write-first enforcement gate',
    'C-33 dependency**: only scoreable when C-31 passes',
    'C-35 dependency**: only scoreable when C-32 passes',
    'C-31 -> C-33',
    'C-32 -> C-35',
]
all_ok = True
for c in checks:
    ok = c in v12
    if not ok:
        all_ok = False
    print('OK  ' if ok else 'MISS', repr(c[:65]))
print('ALL OK:', all_ok)
