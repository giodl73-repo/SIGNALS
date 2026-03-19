"""Build scout-risk-rubric-v20 from v19 by inserting C-58..C-61 and updating scoring."""

with open('C:/src/sim/simulations/quest/rubrics/scout-risk-rubric-v19-2026-03-17.md', encoding='utf-8') as f:
    content = f.read()

# Header
content = content.replace('# Scout-Risk Rubric \u2014 v19', '# Scout-Risk Rubric \u2014 v20')

# Aspirational section header
content = content.replace(
    '## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL each, 98 pts max)',
    '## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL each, 106 pts max)'
)

# New criteria rows
C58 = (
    '| C-58 | **Ordering rule block is positioned before the first governed closure block executes** | depth | '
    'C-57 requires the ordering rule to be declared at global scope naming all closure instances. R20 evidence '
    '(V-01/V-04/V-05 axis -- "rule-before-governed placement": ordering rule hoisted to a dedicated block '
    'positioned before Phase 0, the first governed block) demonstrates a positionally stricter form: the rule '
    'is declared in a structural preamble that executes before any governed block appears, not embedded within '
    'a governed block even if that block names itself in a global scope claim. When the global rule resides '
    'inside a governed block (e.g., declared within Phase 0c while governing Phase 0 and Phase 0c), a reader '
    'encountering Phase 0 cannot verify canonical order requirements without reading ahead to Phase 0c where the '
    'rule appears -- a forward-reference dependency. When the rule block is positioned before all governed '
    'blocks, the rule is visible before any governed closure appears, eliminating the forward-reference '
    'dependency: canonical-order requirements are established at the point a reader first encounters a governed '
    'block. Position-before-governed also strengthens single-point-of-truth: the rule cannot be read as "local '
    'to Phase 0c with incidental broader scope" -- its structural placement outside and before any governed '
    'block makes global intent unambiguous from document position alone. Raises C-57 from "global scope '
    'declared somewhere in the prompt" to "global scope block positioned before the first governed closure '
    'block, eliminating the forward-reference dependency for any reader traversing in document order." Pass if '
    'the ordering rule appears in a dedicated block whose document position precedes Phase 0 (or whichever '
    'governed closure block executes first), rather than being embedded within any of the blocks it governs. |'
)

C59 = (
    '| C-59 | **Ordering rule scope explicitly covers all three pre-phase reference blocks including Phase 0b** | depth | '
    'C-57 requires the global ordering rule to name all closure instances it governs. R20 evidence (V-02/V-04/V-05 '
    'axis -- "complete closure scope coverage": scope extended to "Phase 0, Phase 0b, and Phase 0c closures" from '
    'baseline "Phase 0 and Phase 0c closures") demonstrates that the R19 V-05 scope was incomplete: Phase 0b (the '
    'risk anatomy schema block) is also a pre-phase reference block with a closure sentence, but was excluded from '
    'the ordering rule scope. When the scope excludes Phase 0b, the schema block closure is not governed by the '
    'canonical-order rule -- it can deviate from canonical order without triggering a detectable C-57 violation '
    'because Phase 0b is simply not in the named set. When the scope includes Phase 0b, any canonical-order '
    'violation in Phase 0b closure is a detectable mismatch against the global rule stated scope -- a reviewer '
    'can verify Phase 0b conformance by checking it against the enumerated list. This extends the same '
    'closed-contract logic from C-57 to the full set of pre-phase reference blocks: Phase 0 (mitigation '
    'taxonomy), Phase 0b (risk anatomy schema), and Phase 0c (violation taxonomy) are all named, and any new '
    'pre-phase reference block not added to the scope is a detectable coverage gap. Raises C-57 from "scope '
    'names Phase 0 and Phase 0c (two pre-phase reference blocks)" to "scope names all three pre-phase reference '
    'blocks including Phase 0b, making the ordering rule coverage contract closed across all pre-phase '
    'schema-type blocks." Pass if the prompt global ordering rule scope explicitly names Phase 0b (or equivalent '
    'risk anatomy schema declaration block) alongside Phase 0 and Phase 0c, covering all three pre-phase '
    'reference blocks in its named scope. |'
)

C60 = (
    '| C-60 | **Closure sentences self-name their source block by full title rather than using implicit deictic references** | depth | '
    'C-57 requires the global ordering rule to cover all closure instances. R20 evidence (V-03/V-05 axis -- '
    '"self-identifying closure sentences": Phase 0 closure changes from "No type-class label outside this set '
    'may be used in any Mitigation cell" to "No type-class label outside the Phase 0 Mitigation Type Taxonomy '
    'may be used in any Mitigation cell"; Phase 0c closure changes from "No violation category outside this '
    'list may be named at any prohibition site" to "No violation category outside the Phase 0c Violation '
    'Taxonomy may be named at any prohibition site") demonstrates that the reference form of closure sentences '
    'matters: naming the source block by full title rather than using a deictic reference ("this set", "this '
    'list") converts a context-dependent claim to a context-independent one. When closure sentences use deictic '
    'references, verifying which set or list is referenced requires scanning upward to find the block the '
    'deictic points to -- a positional lookup that must be re-executed each time the closure is encountered. '
    'When closure sentences name the source block by full title, the reference is verifiable by block title '
    'lookup alone: the named block either exists in the document or it does not, independent of reading '
    'position. This is the same count-vs-enumeration escalation that produced C-56, applied to the closure '
    'sentence reference to its own governed block rather than to the list of prohibition sites. Raises C-57 '
    'from "canonical closure order declared globally (content of individual closure sentences unconstrained)" '
    'to "each closure sentence self-identifies its source block by full title, making the governed-block '
    'reference verifiable by title lookup rather than by deictic resolution." Pass if every pre-phase closure '
    'sentence (Phase 0, Phase 0b, Phase 0c) names its source block by its full block heading string rather '
    'than using a deictic reference such as "this set," "this list," or "this taxonomy." |'
)

C61 = (
    '| C-61 | **Phase 0b uses the full 2-sentence canonical closure form matching its pre-phase siblings** | depth | '
    'C-59 requires the ordering rule scope to include Phase 0b. R20 evidence (V-02/V-04/V-05 axis -- "symmetric '
    'canonical closure across all three pre-phase blocks": Phase 0b closure upgraded from single-sentence '
    'state-only form to 2-sentence canonical form with state sentence first and use-site constraint sentence '
    'second) demonstrates that Phase 0b must carry the same structural closure form as Phase 0 and Phase 0c to '
    'be a valid member of the ordering rule governed set. When Phase 0b has a single-sentence state closure '
    '("This schema is complete and closed."), it cannot conform to the canonical 2-sentence ordering rule -- the '
    'rule nominally covers Phase 0b but Phase 0b has no second sentence to order, making the scope claim '
    'unverifiable. When Phase 0b carries the full 2-sentence canonical form, the ordering rule is mechanically '
    'verifiable at Phase 0b: it has a closed-world sentence and a use-site constraint sentence, and their '
    'relative order can be checked. This extends the structural symmetry achieved by C-51 (Phase 0c two-sentence '
    'closure) to Phase 0b, completing the symmetric canonical closure pattern across all three pre-phase '
    'reference blocks. Without C-61, C-59 creates a nominal coverage claim that cannot be mechanically '
    'satisfied -- Phase 0b is listed in scope but structurally cannot conform. With C-61, Phase 0b gains the '
    'minimum structure required for scope inclusion to be meaningful. Raises C-59 from "Phase 0b named in '
    'ordering rule scope (coverage claim)" to "Phase 0b carries the full 2-sentence canonical closure form, '
    'making its inclusion in the ordering rule scope mechanically verifiable." Pass if Phase 0b closure '
    'consists of exactly two syntactically independent sentences in canonical order: a closed-world declaration '
    '("This schema is closed.") followed by a use-site constraint sentence prohibiting any risk anatomy field '
    'name outside the declared schema from appearing in any risk row. |'
)

new_criteria_block = '\n'.join([C58, C59, C60, C61])

# Find end of C-57 row and insert new criteria after it
marker = '| C-57 | **Closure sentence ordering rule is declared at global scope, naming all closure instances**'
c57_start = content.index(marker)
pos = c57_start + len(marker)
while True:
    nl = content.index('\n', pos)
    if content[nl-2:nl] == ' |':
        c57_end = nl
        break
    pos = nl + 1

content = content[:c57_end] + '\n' + new_criteria_block + content[c57_end:]

# Scoring reference
content = content.replace(
    '| Golden | 182-188 | Exemplary -- suitable as a reference prompt |',
    '| Golden | 190-196 | Exemplary -- suitable as a reference prompt |'
)
content = content.replace(
    '| Strong | 167-181 | High-quality with minor gaps |',
    '| Strong | 175-189 | High-quality with minor gaps |'
)
content = content.replace(
    '**Max composite: 188** (60 essential + 30 recommended + 98 aspirational across 49 criteria)',
    '**Max composite: 196** (60 essential + 30 recommended + 106 aspirational across 53 criteria)'
)

# Escalation ladder
old_c57_ladder = (
    '| C-57 | C-54 | Canonical closure sentence order enforced per-block (implicit per closure) -> '
    'ordering rule declared globally with explicit named scope covering all closure instances, making '
    'canonical order a single-point-of-truth constraint rather than a per-block replication requirement |'
)
new_ladder_entries = '\n'.join([
    old_c57_ladder,
    '| C-58 | C-57 | Global scope declared somewhere in the prompt -> global scope block positioned before the first governed closure block, eliminating the forward-reference dependency for any reader traversing in document order |',
    '| C-59 | C-57 | Scope names Phase 0 and Phase 0c (two pre-phase reference blocks) -> scope names all three pre-phase reference blocks including Phase 0b, making the ordering rule coverage contract closed across all pre-phase schema-type blocks |',
    '| C-60 | C-57 | Canonical closure order declared globally (content of individual closure sentences unconstrained) -> each closure sentence self-identifies its source block by full title, making the governed-block reference verifiable by title lookup rather than by deictic resolution |',
    '| C-61 | C-59 | Phase 0b named in ordering rule scope (coverage claim) -> Phase 0b carries the full 2-sentence canonical closure form, making its inclusion in the ordering rule scope mechanically verifiable |',
])
content = content.replace(old_c57_ladder, new_ladder_entries)

out_path = 'C:/src/sim/simulations/quest/rubrics/scout-risk-rubric-v20-2026-03-17.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done. Lines:', content.count('\n') + 1, '| Size:', len(content))
print('Written:', out_path)
