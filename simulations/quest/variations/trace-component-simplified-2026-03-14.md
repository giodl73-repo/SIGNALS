**Simplified: 2,303 words. Original: 3,847 words. Reduction: 40.1%.**

---

## Simplification Report

### Word counts
| Version | Words | Change |
|---------|-------|--------|
| Original V-05 body | 3,847 | — |
| QU5 simplified body | 2,303 | −1,544 (−40.1%) |

### Essential criteria: all pass ✓

| Criterion | Mechanism preserved |
|-----------|---------------------|
| C-01 Event Anchor | TABLE-1 + GATE-1 ✓ |
| C-02 Component Tree Traversal | TABLE-2 + GATE-2 ✓ |
| C-03 State Update Map | TABLE-3 + GATE-3 ✓ |
| C-04 Re-render Inventory | TABLE-4 + GATE-4 ✓ |
| C-05 Final UI State | TABLE-6 + GATE-6 ✓ |
| C-06–C-08 (Recommended) | TABLE-5/7/8 + schema Area 1 ✓ |
| C-58 | Area 3 enforcement table + rules ✓ |
| C-59 | NHQ-3 + Enforcement Rationale rules ✓ |
| C-60 | GATE-N: TYPE: brackets + Area 5 ✓ |
| C-61 | PHASE VOCABULARY in all 5 manifests ✓ |
| C-62 | Area 5 schema vocabulary table ✓ |
| C-63 | NHQ-3 epistemics ground schema-declared vs. ad-hoc ✓ |
| C-64 | PHASE VOCABULARY + REQUIREMENT gates → citation chain ✓ |

### What was removed and why

**1. Close-marker prose (−29 words)**
`"NULL REGISTER complete. DEPARTURE REGISTER begins."` and its two siblings deleted. The bold close headers immediately precede the next section header — the prose was fully redundant with position.

**2. ROLE 1 intro bloat (−20 words)**
`"This role has two sequential phases."` deleted (implied by what follows). Schema-bleeding prohibition compressed from `"No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind"` to `"No schema structure, placeholder templates, or format cues"`.

**3. CAUSAL PHASE intro redundancies (−18 words)**
`"No schema artifact is written here."` deleted (already stated in ROLE 1). `"The phase contains two named registers."` deleted (registers immediately follow). Register sequencing condensed.

**4. SCHEMA PHASE intro framing (−23 words)**
`"a named artifact a reader can reference to verify the trace that follows"` deleted — descriptive but not operational. `"Do not reproduce any language from this prompt."` deleted — implied by `"in your own words"`.

**5. Schema template scaffolding (−18 words)**
`"[Author the complete schema here. Areas 1 through 5 in full."` → `"[Areas 1 through 5 in full."`. `"Every principle must derive from your CAUSAL PHASE answers."` deleted — already stated in schema intro sentence.

**6. Schema Area compression (−107 words total)**
- Area 2: derivation reference condensed (`NQ-1 through NQ-2 and DQ-1` inline format)
- Area 3 rationale instructions: three `"Author the rationale for..."` sentences → one bulleted line
- Area 4: manifest structure description tightened; removed `"The PHASE VOCABULARY field enumerates the framework-specific terms...scoped to the phase's analytical content."` (already captured in parenthetical)
- Area 5 DIRECTIVE/REQUIREMENT cells: `"[author: when to apply -- gates that enforce a mandatory structural or syntactic form; the output must use a specific format, table structure, column arrangement, or row count pattern]"` → `"[author: applies to gates enforcing mandatory structural or syntactic form -- format, structure, or row count]"` (18 words saved per cell, ×2)
- Area 5 guidance: condensed from 53 words to 20 words

**7. ROLE 2 intro (−95 words)**
The paragraph compressed from ~215 to ~120 words. Back-references (`"you derived from NHQ-1 and NHQ-2"`, `"you articulated why in DQ-3 and DQ-4"`, `"verify your NHQ-3 reasoning holds"`) deleted — they name the source of knowledge already applied; the behavioral rule is what matters. `"in this trace"` implied. `"using only the types defined in your schema"` covered by `"from your Area 5 vocabulary"`.

**8. FRAMEWORK DECLARATION gate (−9 words)**
`"Do not begin MANIFEST-1 until this header is complete."` deleted — sequencing is implied by document structure.

**9. Manifest close-line instructions (−85 words)**
Five instances of `"*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-N as successor.]*"` (24 words each) → `"*[Area 3 close-line, verbatim -- successor TABLE-N.]*"` (7 words each). ROLE 2 intro already establishes the full instruction; the per-manifest placeholder just needs to mark the slot and name the specific successor.

**10. TABLE-2 intro paragraph (−33 words)**
`"Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default."` deleted entirely — ROLE 2 intro already says `"Apply the Direction default from Area 2 at every traversal hop"`.

**11. PHASE VOCABULARY hint framing (−50 words)**
`"[framework-specific terms valid for event-anchor analysis -- e.g., SyntheticEvent, addEventListener, dispatchEvent, event.target; minimum two terms]"` → `"[event-anchor terms -- e.g., SyntheticEvent, addEventListener; minimum two]"`. Framing phrase cut; example list trimmed to 2 terms (enough to anchor the type); `"terms"` on end redundant with `"minimum two"`. Repeated across 5 manifests.

**12. Table example rows (−75 words)**
Hint rows removed from TABLE-1, TABLE-2, TABLE-3, TABLE-4. Column headers establish expected content; Area 2/4 schema defines the format. The example rows were guidance scaffolding, not requirements. GATE blocks enforce the substantive constraints.

**13. Minor structural cuts (−32 words)**
- `"Minimum two rows."` in TABLE-2 deleted (GATE-2 already enforces this)
- INERT-HOP DECLARATION condensed (`"mandatory -- present regardless of count"` → `"mandatory"`)
- Zero-effects row shortened (`"No API calls, timers, subscriptions, or navigation triggered."` → `"No effects triggered."`)
- Mutation direct/inherited definitions condensed

---

**Simplified prompt written to**: `simulations/quest/golden/trace-component-QU5-simplified-2026-03-15.md`

```json
{"simplified_word_count": 2303, "original_word_count": 3847, "all_essential_still_pass": true}
```
