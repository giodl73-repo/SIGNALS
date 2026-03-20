---
name: specify-abstract
description: "Writes a structured academic abstract (200-250 words): Background / Gap / Claim / Method / Result / Implication. Supports journal variants (--for journal:pnas, --for journal:jcs, etc.)"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with four pre-execution commitment sub-protocols -- Protocol I (four canonical cheap paths including phase bundling), Protocol V (source-gate dependency registry pre-commitment with completeness verification: all inter-gate input dependencies locked and audited for completeness before Phase 0), Protocol II (complete nine-sub-phase sequence lock with per-gate completion conditions, all-transition anti-bundling rationale, and Protocol V citations), and Protocol III (self-diagnosis framework pre-commitment) -- all closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories targeting Protocol III pre-committed positive search space targets, with per-excluded-category verification using Protocol III committed format and a standalone rationale block naming and closing both shortcut forms. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. All eleven v15 ceiling criteria active (C-36 through C-46). Above-ceiling probe: Protocol V completeness verification block creates bidirectional referenceability between Protocol V and Protocol II.

---

**Pre-execution commitment protocol -- four sub-protocols closed before Phase 0.**

---

**Protocol I -- Cheap paths (four canonical paths)**

A nominal execution of this skill has exactly four escape routes. Name each one, confirm it, and close all four by canonical name.

**Signal-skip**: Running Phase 1 without executing the glob -- producing content disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim rather than naming the specific unresolved question whose resolution is this paper's contribution.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

**Phase bundling**: Executing multiple phases as a single undifferentiated step -- e.g., treating Phase 3 (merge) and Phase 3b (integration verification) as one event; filling all four boundary quality card columns in a single pre-merge pass; merging Phase 2a and Phase 2b into one pass; treating Phase 4 and Phase 5 as a combined sweep. Phase bundling is structurally distinct from the three execution-quality shortcuts: it defeats the sequence lock by preventing individually named phase gates from being established at all.
> Confirm you will NOT bundle phases: [I will treat each named phase and sub-phase as an individually gated execution unit. I will not begin Phase 3b until Phase 3 is complete and the merged paragraph exists. I will not fill the Integrated? column until after the merge has produced text to quote from.]

> Protocol I: complete. Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. Phase bundling: closed.

---

**Protocol V -- Source-Gate Dependency Registry pre-commitment with completeness verification**

Before Phase 0, commit the complete inter-gate input dependency structure as a named pre-committed registry, then verify that the registry is exhaustive against the known nine-gate Protocol II structure. Both steps are performed before Phase 0, when no draft exists.

**Step V-A: Pre-committed source-gate dependency registry:**

| Consuming phase | Required input | Source gate |
|-----------------|----------------|-------------|
| Phase 2a -- Coverage draft | Extracted claim, method, and key result | Phase 1 output |
| Phase 2b -- Pass 1: coupling status | All six drafted sections as fixed objects | Phase 2a output |
| Phase 2c -- Pass 2: bridge type and phrase | Section content (semantic type assignment) + confirmed COUPLED status at each boundary | Phase 2a output + Phase 2b output |
| Phase 3 -- Merge and count | All five committed bridge phrases as connectives + all six section texts as content | Phase 2c output + Phase 2a output |
| Phase 3b -- Pass 3: integration status | The merged paragraph as the source of all verbatim extracts | Phase 3 output |
| Phase 4 -- Journal variant | The Phase 3b-verified (and N-revised) paragraph | Phase 3b output |
| Phase 5 -- Five-amendment pass | The journal-variant paragraph + pre-committed self-diagnosis framework | Phase 4 output + Protocol III |

*Why Phase 3b's CANNOT-exist constraint is the critical dependency:* Verbatim quoted extracts from the merged paragraph CANNOT exist before Phase 3 produces that paragraph. This is the entry in Protocol V where the pre-commitment creates the most auditable temporal constraint: the text quoted in Phase 3b literally does not exist at the time Protocol V is committed.

**Step V-B: Protocol V completeness verification against Protocol II gate structure:**

The nine Protocol II gates are: Phase 0, Phase 1, Phase 2a, Phase 2b, Phase 2c, Phase 3, Phase 3b, Phase 4, Phase 5.

For each gate, confirm whether it has an entry in Protocol V's dependency registry:

| Protocol II gate | Has Protocol V entry? | Verification |
|------------------|-----------------------|--------------|
| Phase 0 | No | Phase 0 has no prior-phase input dependency: it is the initiation gate (paper type declared from external input only). No Protocol V entry required. |
| Phase 1 | No | Phase 1 has no prior-phase input dependency: it consumes the topic parameter, not a prior phase's output. No Protocol V entry required. |
| Phase 2a | Yes | Protocol V entry present: consumes Phase 1 output. |
| Phase 2b | Yes | Protocol V entry present: consumes Phase 2a output. |
| Phase 2c | Yes | Protocol V entry present: consumes Phase 2a + Phase 2b output. |
| Phase 3 | Yes | Protocol V entry present: consumes Phase 2c + Phase 2a output. |
| Phase 3b | Yes | Protocol V entry present: consumes Phase 3 output. CANNOT-exist reasoning applies. |
| Phase 4 | Yes | Protocol V entry present: consumes Phase 3b output. |
| Phase 5 | Yes | Protocol V entry present: consumes Phase 4 + Protocol III. |

*Completeness result:* All seven output-dependent phases (Phase 2a through Phase 5) have Protocol V entries. Two phases (Phase 0 and Phase 1) have no prior-phase dependency and require no entry. Protocol V is exhaustive. No output-dependent gate has been omitted from the registry.

*Why the completeness verification matters -- the gap C-46 leaves open:* C-46's pass condition requires at minimum the Phase 3b -> Phase 3 dependency and at least two additional inter-gate dependencies. A registry that satisfies C-46's minimum (three dependencies named) while omitting four others is incomplete but technically C-46-passing. A completeness verification block requires Protocol V to account for every Protocol II gate -- either by providing a registry entry or by stating explicitly why no entry is required. This closes the incompleteness gap: a reader can verify not only that Protocol V cites Protocol II correctly but that Protocol II cites Protocol V exhaustively.

*Why pre-committing the completeness verification matters:* The completeness audit in Step V-B is performed before Phase 0, when no draft exists. An audit performed after Phase 0 would be post-hoc -- the dependency structure could have been assembled by reading the Phase structure forward. Pre-commitment creates a verifiable temporal constraint: the completeness verification is part of the pre-Phase-0 commitment, not a post-hoc rationalization.

> Protocol V: complete. Source-gate dependency registry locked (Step V-A). Completeness verification against Protocol II gate structure complete (Step V-B): all seven output-dependent phases have registry entries; two initiation phases require none. Registry is exhaustive. Protocol II completion conditions will cite `(Source gate: Phase X per Protocol V.)` for all output-dependent gates.

---

**Protocol II -- Complete sub-phase sequence lock with per-gate completion conditions, Protocol V dependency citations, and all-transition anti-bundling rationale**

Before Phase 0 begins, declare the nine-sub-phase canonical execution sequence. Each sub-phase is individually named with an explicit completion condition. Source-gate dependencies are per Protocol V committed registry (verified complete in Protocol V Step V-B). No sub-phase may begin before its predecessor satisfies its named completion condition.

1. **Phase 0** -- Paper type declaration. *Complete when:* paper type declared and confirmed. Must complete before Phase 1.

2. **Phase 1** -- Signal acquisition. *Complete when:* glob executed, artifacts read, claim/method/result extracted. Must complete before Phase 2a.

3. **Phase 2a** -- Coverage draft. *Complete when:* all six sections drafted and labeled. Must complete before Phase 2b. *(Source gate: Phase 1 per Protocol V.)*

4. **Phase 2b** -- Pass 1: coupling status. *Complete when:* all five boundaries assigned COUPLED/WEAK/REVISE; all WEAK/REVISE revision directives resolved; Coupling column fully populated; all other columns blank. Must complete before Phase 2c. *(Source gate: Phase 2a per Protocol V.)*

5. **Phase 2c** -- Pass 2: bridge type and phrase. *Complete when:* all five boundaries have type from constrained vocabulary and 3-8 word bridge phrase; Bridge type/phrase columns populated; Integrated? blank. Must complete before Phase 3. *(Source gates: Phase 2a + Phase 2b per Protocol V.)*

6. **Phase 3** -- Merge and count. *Complete when:* merged paragraph exists in standard sequence (Background-Gap-Claim-Method-Result-Implication), bridge phrases used as connectives, word count confirmed in range. Must complete before Phase 3b. *(Source gates: Phase 2c + Phase 2a per Protocol V.)*

7. **Phase 3b** -- Pass 3: integration status. *Complete when:* all five boundaries have verbatim quoted extract (3-10 words in quotation marks) from the Phase 3 merged paragraph confirming bridge phrase incorporation, or N with revised paragraph. Must complete before Phase 4. *(Source gate: Phase 3 per Protocol V. Extracts CANNOT be written before Phase 3 produces the merged text.)*

8. **Phase 4** -- Journal variant. *Complete when:* journal flag applied if present, or vacuously complete. Must complete before Phase 5. *(Source gate: Phase 3b per Protocol V.)*

9. **Phase 5** -- Five-amendment pass. *Terminal phase.* *(Source gates: Phase 4 + Protocol III per Protocol V.)*

*Why each phase boundary is a separately committed gate -- anti-bundling rationale for all transitions:*

**Phase 0 -> Phase 1**: Paper type declaration must precede signal acquisition. Paper type governs the epistemic register of all six sections. Executing Phase 1 without a committed paper type produces undifferentiated signal acquisition that cannot distinguish which artifacts are structurally relevant.

**Phase 1 -> Phase 2a**: Signal acquisition must precede drafting. Every section must be grounded in extracted signals. A draft written before signal acquisition produces topic-generic filler.

**Phase 2a -> Phase 2b**: All six sections must be drafted before coupling is assessed. Coupling assessment requires both adjacent sections to exist as fixed objects. Assessing coupling while drafting collapses the distinction between writing and structural revision.

**Phase 2b -> Phase 2c**: All WEAK/REVISE directives must be resolved before bridge phrase composition begins. A bridge phrase composed for a section that subsequently changes becomes semantically invalid.

**Phase 2c -> Phase 3**: All five bridge phrases must be committed before the merge begins. Composing bridges during the merge collapses the type-constrained planning pass (Phase 2c) into the construction pass (Phase 3), making bridge type adherence unverifiable.

**Phase 3 -> Phase 3b**: The merged paragraph must exist before integration can be verified. *(C-36 canonical rationale)* Per Protocol V Step V-B: Phase 3b's completeness audit confirmed this dependency. Verbatim quoted extracts CANNOT be written before the merge is executed -- the text does not yet exist.

**Phase 3b -> Phase 4**: Integration verification must be complete before the journal variant is applied. Unresolved N entries create an ambiguous base for journal variant transformation.

**Phase 4 -> Phase 5**: The journal variant must be finalized before the amendment pass begins. If journal variant adjustments and amendment pass execute concurrently, amendment non-triviality criteria become unauditable.

*Why per-gate completion conditions and Protocol V citations matter:* Completion conditions specify what is true when each gate closes; Protocol V citations (verified complete in Step V-B) specify which pre-committed registry entry governs the required input. The bidirectional referenceability -- Protocol II cites Protocol V; Protocol V's completeness audit covers Protocol II -- makes the full dependency structure auditable from either document.

> Confirm you will NOT execute sub-phases out of declared canonical order: [I will complete each sub-phase's named completion condition before beginning the next. Phase 3 must produce the merged paragraph before Phase 3b can quote from it per Protocol V committed registry (completeness verified in Step V-B).]

> Protocol II: complete. Sub-phase sequence: Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. All nine gates individually named with completion conditions, all-transition anti-bundling rationale, and Protocol V dependency citations (completeness verified). Locked.

---

**Protocol III -- Self-diagnosis framework pre-commitment**

Before Phase 0, commit the four positive search space targets and the per-category verification format for Amendment 1. This commitment is made when no draft exists.

**Pre-committed positive search space targets:**
- **Background epistemic register**: mismatch between declared paper type and the Background's language register
- **Claim scope relative to Method**: Claim stronger than what Method and Result can establish; overclaiming that survives all four fixed amendments
- **Contribution incrementality framing**: Claim reads as "more of something" rather than "resolution of something prior work could not resolve"
- **Method scope adequacy**: stated scope insufficient to support the Claim's strength; Result uninterpretable regardless of quantification

**Pre-committed per-category verification format:**
> [Category]: N -- [one sentence naming the diagnosed weakness and stating why it does not fall in this category]
(Self-contained and independently auditable. First-order `[confirmed]` shortcut prohibited. Second-order category-mirroring shortcut prohibited.)

*Why pre-committing matters -- structural asymmetry:* A framework introduced at Amendment 1 runtime CAN be constructed after reading the draft. A pre-committed framework CANNOT: Protocol III appears before Phase 0, when no draft exists.

> Protocol III: complete. Positive search space targets locked. Per-category verification format locked.

---

> Unified gate: Protocol I (four cheap paths) closed. Protocol V (source-gate dependency registry with completeness verification against Protocol II gate structure) pre-committed. Protocol II (complete nine-gate sequence lock with per-gate completion conditions, all-transition anti-bundling rationale, and Protocol V citations) locked. Protocol III (self-diagnosis framework) pre-committed. Proceed to Phase 0.

---

**Phase 0 -- Paper type declaration.**
- **Empirical**: Past tense claim. Background: domain condition making measurement urgent. Gap: specific untested question. Implication: practitioner decision.
- **Theoretical**: Present tense claim. Background: conceptual tensions. Gap: unresolved construct. Implication: what framework makes tractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read: paper draft, specify-spec, discover-hypothesis. Extract central claim, method, key result, target journal.

---

**Phase 2a -- Coverage draft (gap-first order).** Gap first, then Background, Claim, Method, Result, Implication. No self-correction. Label each section.

**Gap** (write first -- 1 sentence): "X remains unresolved" / "it is unknown whether X."
> [Gap sentence]

**Background** (1-2 sentences): Conditions making Gap inevitable. End where Gap begins.
> [Background text]

**Claim** (1 sentence): Correct tense for declared paper type.
> Paper type: [confirmed from Phase 0 -- do not change]
> [Claim sentence]

**Method** (1-2 sentences): Named method with scope.
> [Method text]

**Result** (1-2 sentences): Finding first. Number, percentage, or qualitative strength word.
> [Result text]

**Implication** (1 sentence): One concrete enabling action.
> [Implication sentence]

---

**Boundary quality card -- Phase 2b / Pass 1: Coupling status.** Fill Coupling column only.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? ("quoted extract" or N) |
|----------|-----------------------------------|-------------|---------------------------|--------------------------------------|
| Background -> Gap | [fill now] | -- | -- | -- |
| Gap -> Claim | [fill now] | -- | -- | -- |
| Claim -> Method | [fill now] | -- | -- | -- |
| Method -> Result | [fill now] | -- | -- | -- |
| Result -> Implication | [fill now] | -- | -- | -- |

For WEAK or REVISE: Boundary / Deficient section / Deficiency / Before / After / Re-verify. Proceed when all COUPLED.

---

**Boundary quality card -- Phase 2c / Pass 2: Bridge type and phrase.** Type first: contrast / causation / resolution / escalation / application. No more than two consecutive same type.

---

**Phase 3 -- Merge and count.** Standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication. Bridge phrases as connectives. Count words. Compress if OVER.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

---

**Boundary quality card -- Phase 3b / Pass 3: Integration status.** Per Protocol V (completeness verified in Step V-B): source gate is Phase 3 output. Fill Integrated? column with verbatim quoted extracts (3-10 words, in quotation marks) from the Phase 3 merged paragraph. N if bridge dropped.

*Why quoted evidence rather than Y/N -- structural asymmetry:* A Y/N integration status CAN be assigned before the merge is executed. A verbatim extract CANNOT be written before the merge: the text does not yet exist. This CAN-CANNOT asymmetry is pre-committed in Protocol V Step V-A and verified in Step V-B.

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? ("quoted extract" or N) |
|----------|----------|-------------|---------------|--------------------------------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from Phase 3 merged text, or N] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from Phase 3 merged text, or N] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from Phase 3 merged text, or N] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from Phase 3 merged text, or N] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from Phase 3 merged text, or N] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase. Show revised paragraph with word count.

---

**Phase 4 -- Journal variant.** Apply profile if flag present. Pass vacuously if no flag.

---

**Phase 5 -- Five-amendment pass (diagnosis-first).**

**Amendment 1 -- Self-diagnosis (Protocol III committed targets; standalone rationale naming both shortcut forms)**
Diagnose from Protocol III committed positive search space targets. Verify per excluded category using Protocol III committed format.

> Weakness category: [name -- OUTSIDE fixed categories; drawn from Protocol III targets: Background epistemic register / Claim scope relative to Method / Contribution incrementality framing / Method scope adequacy]

*Per-excluded-category verification (Protocol III committed format -- one specific sentence per row):*
> Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]
> Result quantification: N -- [one sentence naming the diagnosed weakness and stating why it is not about adding or strengthening numeric evidence in the Result]
> Implication tightening: N -- [one sentence naming the diagnosed weakness and stating why it is not about removing modal hedges or narrowing the enabling action]
> Prose coherence: N -- [one sentence naming the diagnosed weakness and stating why it is not about transition quality or paragraph flow]

*Why specific per-row sentences matter -- named shortcut closure:* Two shortcut paths defeat the auditable-reasoning requirement and are both prohibited by Protocol III committed format. The **first-order shortcut** is `[confirmed / explain if uncertain]` -- the parenthetical describes the exclusion criterion without applying it to the specific weakness. The **second-order shortcut** is category-mirroring: a sentence that restates the category label without naming what about the diagnosed weakness makes it non-qualifying. Both are prohibited: the required form names the diagnosed weakness concretely and states why that specific weakness does not fall in this slot -- independently auditable.

*Where to look instead -- positive search space (Protocol III committed targets):*
- **Background epistemic register**: register mismatch with declared paper type
- **Claim scope relative to Method**: overclaiming that survives all four fixed amendments
- **Contribution incrementality framing**: claim reads as "more of" rather than "resolution of"
- **Method scope adequacy**: scope insufficient to support the Claim's strength

> Diagnosis: [one sentence] / Before: [...] / After: [...] / Non-trivial: Y / N

**Amendment 2 -- Gap sharpening**
> Before: [original Gap] / After: [specific unresolved question] / Non-trivial: Y / N

**Amendment 3 -- Result quantification**
> Before: [original Result] / After: [quantified] / Non-trivial: Y / N

**Amendment 4 -- Implication tightening**
> Before: [original Implication] / After: [one concrete action, no modal hedges] / Non-trivial: Y / N

**Amendment 5 -- Prose coherence**
> Before: [two sentences with weakest transition] / After: [rewritten for flow] / Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]
