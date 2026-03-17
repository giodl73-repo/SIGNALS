Written to `simulations/quest/rubrics/mock-ns-rubric-v16-2026-03-17.md`.

---

## Summary of changes

**Two new aspirational criteria (C-42, C-43) extracted from R15 excellence signals. Max rises from 146 to 150.**

### C-42 -- C-28 step-scope displacement (R15 V-01)
> "Only this step emits the TOPICS.md status line" -- grammatically correct form, present in S-1, not S-0.

C-28 requires the emission sentence to appear within S-0 or its gates. When S-0 does not exist as a discrete step (collapsed into S-1 or merged), no emission sentence can satisfy C-28 regardless of grammatical correctness. A sentence in S-1 that satisfies C-28's grammatical form (step as nominative subject, emission as main predicate) is displaced -- it is in the wrong step scope. Grammatical form is necessary but not sufficient; step scope is independently required and cannot be satisfied by proxy. C-42 names this displacement as a distinct failure mode: an emission sentence that is grammatically correct but located in a step other than S-0 or its gates.

**Failure chain: C-28, C-42** -- C-28 fails from S-0 absence; C-42 adds the named displacement. When S-0 exists and the emission sentence is correctly placed, C-42 passes by default.

### C-43 -- C-32 lifecycle-annotation closing-position displacement (R15 V-02)
> V-02 projection: "If lifecycle exit state block appears after the tier-carry terminal sentence rather than displacing it -> 146/146. If exit state replaces the standalone terminal sentence -> 144/146."

Lifecycle entry/exit state annotations appended to S-0 interact with C-32 in two ways: (1) supplementation -- the lifecycle annotation follows the tier-carry terminal sentence; C-32 passes because the sentence is present as a discrete prose sentence even if the annotation is the final token; (2) replacement -- the lifecycle annotation takes the position of the tier-carry terminal sentence, eliminating it; C-32 fails because the standalone terminal sentence is absent. C-43 names the replacement form as a distinct failure mode. Evaluators must check whether the standalone tier-carry sentence exists as a discrete prose sentence, not merely whether it is the absolute final line when lifecycle annotations are appended.

**Failure chain: C-32, C-43** -- when lifecycle annotation replaces the terminal sentence, both C-32 (terminal sentence absent) and C-43 (replacement displacement named) fire.

### Discriminator notes updated

| Criterion | Update |
|-----------|--------|
| C-28 | R15: Step-scope boundary confirmed. A grammatically correct emission sentence in S-1 (when S-0 is absent) does not satisfy C-28. Grammatical form + correct step scope are both required. V-01 canonical: "Only this step emits the TOPICS.md status line" in S-1 -- C-28 fails, C-42 fires. |
| C-32 | R15: Lifecycle annotation interaction. Exit-state blocks that supplement (follow) the terminal sentence do not displace it; C-32 passes. Exit-state blocks that replace (eliminate) the terminal sentence fail both C-32 and C-43. V-02 boundary: supplementation -> pass; replacement -> fail. |

### Scoring

| Version | Aspirational max | Total max |
|---------|-----------------|-----------|
| v15 | 66 (33 x 2) | 146 |
| **v16** | **70 (35 x 2)** | **150** |

**R15 under v16:**
- V-01 (decision table, no S-0): fails C-12, C-13, C-15/C-17-C-28/C-32 (S-0 dependent), C-42 (step-scope displacement); C-43 PASS (no lifecycle annotations) -- **118/150**
- V-02 (lifecycle entry/exit states): C-42 PASS (S-0 discrete); C-43 supplementation -> **150/150**; C-43 replacement -> **148/150**

---

## Version History with Discriminators

### v16 summary (2026-03-17) -- R15 patterns

Two new criteria. C-42: C-28 step-scope displacement -- a grammatically correct emission sentence in S-1 (or any step other than S-0) does not satisfy C-28. R15 V-01 canonical: "Only this step emits the TOPICS.md status line" appears in S-1 (S-0 is absent, collapsed into S-1). The sentence satisfies C-28's grammatical form but fails C-28 because S-0 does not exist as a discrete step. Grammatical form is necessary but not sufficient; step scope is independently required. C-42 names this as the twelfth declarative-placement failure mode: correct grammar in wrong step scope.

C-43: C-32 lifecycle-annotation closing-position displacement -- lifecycle entry/exit state annotations appended to S-0 can interact with C-32 in two ways. Supplementation: the annotation follows the tier-carry terminal sentence; C-32 passes (sentence is present as discrete prose). Replacement: the annotation eliminates the terminal sentence; C-32 fails and C-43 additionally fires. R15 V-02 projected boundary: supplementation -> 150/150; replacement -> 148/150.

Discriminator notes added: C-28 (step-scope boundary -- grammatical form + correct step scope both required; V-01 confirms sentence in S-1 fails C-28); C-32 (lifecycle annotation interaction -- supplementation passes, replacement fails; V-02 boundary confirmed).

Scoring: max rises from 146 to **150** (35 aspirational x 2 = 70).

---

### v15 summary (2026-03-17) -- R14 patterns

Two new criteria. C-40: existential-there negation ordering prohibition -- "There is no step that precedes this step's TOPICS.md status line emission." Expletive `There` is the grammatical subject; the step (`this step`) is demoted to genitive possessor in the object phrase. The sentence describes ordering relationally by negating predecessors, not by stating the step's emission identity in nominative-subject position. C-38 does not fire (existential-there, not equative-copula it-cleft). C-39 does not fire (no wh-action nominalization). Failure chain: C-25, C-28, C-40. Eleventh declarative failure mode.

C-41: C-35 by-PP scope boundary -- passive artifact-as-subject with step-agent in a by-PP fires C-33 only; C-35 (relative-clause-agent displacement) does not apply. C-35 requires the step to appear as agent inside a subordinate relative clause or equivalent subordinate clause. A by-PP is a phrase-level adjunct, not a clause. R14 V-01 canonical: "The TOPICS.md status line is emitted by this step before any other step begins" -- C-33 fires, C-35 passes.

Discriminator notes added: C-28 (focus-particle scoping passes -- "Only this step emits..." satisfies C-28; V-03 142/146 confirmation); C-31 (fires independently when C-25+C-28 satisfied -- "This step must emit..." fails C-31 alone; V-04 canonical); C-33 (passive + by-PP -> C-33 not C-35; V-01 boundary); C-35 (by-PP is phrase-level adjunct, not subordinate clause; V-01 boundary).

Scoring: max rises from 142 to **146** (33 aspirational x 2 = 66).

---

### v14 summary (2026-03-16) -- R13 patterns

Two new criteria. C-38: expletive-subject it-cleft displacement -- "It is this step that first emits the TOPICS.md status line." The formal subject is expletive `It`; `this step` is the cleft-focus NP; emission is in the restrictive relative clause `that first emits...`. C-29 does not fire (expletive is not a step-derived nominalization). C-35 does not fire (artifact is not main-clause subject). C-36 does not fire (main predicate is equative copula `is`, not an ordering verb). Failure chain: C-25, C-28, C-38.

C-39: wh-pseudo-cleft with emission in predicate complement -- "What this step does first is emit the TOPICS.md status line." Wh-action nominalization `What this step does first` is the grammatical subject; emission `emit...` is predicate complement. C-29's substitution test extends to wh-action-nominalizations: `It` = the wh-nominalization, not the step. C-36 passes (copula main predicate). Failure chain: C-25, C-28, C-29, C-39.

Discriminator note added to C-36: coordinate-clause confinement does NOT fire C-36. R13 V-03 ("This step runs first; it emits...") places emission in a second independent coordinate clause, not a relative clause. C-36 requires relative-clause confinement; the compound-sentence-split pattern fails C-25 and C-28 only.

Scoring: max rises from 138 to **142** (31 aspirational x 2 = 62).

---

### v13 summary (2026-03-16) -- R12 patterns

Two new criteria. C-36: ordering-predicate displacement -- step as main-clause subject with ordering verb (e.g., `runs`) does not satisfy C-25 or C-28 when emission is confined to a relative clause. Three-criterion failure chain C-25, C-28, C-36 from R12 V-01: "S-0, which emits the TOPICS.md status line first, runs before all other steps." Evaluator trap inverse to C-35: C-35 fires when artifact is main-clause subject; C-36 fires when step is main-clause subject but emission is not the main predicate.

C-37: possessive-NP action-abstraction subject with gerundive emission complement. In v12, the R12 V-03 construction ("This step's first action is emitting the TOPICS.md status line") fired C-35 "by extension" -- C-37 names the form explicitly so all eight declarative failure modes are enumerated in the rubric. C-34 passes (gerundive is predicate complement, not subject). C-35 and C-36 pass (artifact not subject; no ordering predicate). Failure chain: C-25, C-28, C-29, C-30, C-37 (-10 pts). Scoring: max rises from 134 to **138** (29 aspirational x 2 = 58).

---

### v12 summary (2026-03-16) -- R11 patterns

New criterion C-35 (relative-clause-agent displacement). R11 V-01: "TOPICS.md is the first artifact this step emits." The step is grammatically active as agent of `emits` within a restrictive relative clause, but the artifact `TOPICS.md` is the main-clause subject. This closes the evaluator trap of crediting C-28 because "the step is doing something." C-35 names the rule: the step must be the main-clause nominative subject; subordinate-clause activity does not satisfy C-25 or C-28. Five-criterion failure chain: C-25, C-28, C-29, C-30, C-35. Scoring: max rises from 132 to **134** (27 aspirational x 2 = 54).

---

**v11 summary** (2026-03-16) -- R10 patterns

Two new criteria. C-33 (passive artifact-as-subject): four-criterion failure chain C-25, C-28, C-29, C-33. C-34 (gerundive-as-subject): three-criterion failure chain C-28, C-29, C-34. Scoring: max rises from 128 to **132** (26 aspirational x 2 = 52).

---

**v10 summary** (2026-03-16) -- R9 patterns

Two new criteria (C-31, C-32). C-31: deontic/modal-obligation form fails. C-32: C-18 and C-20 are structurally independent. Scoring: max rises from 124 to **128** (24 aspirational x 2 = 48).

---

**v9 summary** (2026-03-16) -- R8 patterns

Two new criteria (C-29, C-30). C-29: possessive-nominal form demotes step to genitive modifier. C-30: artifact-as-subject in active voice. Scoring: max rises from 120 to **124** (22 aspirational x 2 = 44).

---

**v8 summary** (2026-03-16) -- R7 patterns

Two new criteria (C-27, C-28). Scoring: max rises from 116 to **120**.

---

**v7 summary** (2026-03-16) -- R6 patterns

Two new criteria (C-25, C-26). Scoring: max rises from 112 to **116**.

---

**v6 summary** (2026-03-16) -- R5 patterns

Two new criteria (C-23, C-24). Scoring: max rises from 108 to **112**.

---

**v5 summary** (2026-03-16) -- R4 patterns

Four new criteria (C-19, C-20, C-21, C-22). C-17 clarified (content-based, not form-based). Scoring: max rises from 100 to **108**.

---

**v4 summary** (2026-03-16) -- R3 patterns

Two new criteria (C-17, C-18). Aspirational drops from 2.5 to 2 pts each (max remains 100).

---

**v3 summary** (2026-03-16) -- R2 patterns

Three new aspirational criteria (C-14, C-15, C-16) from R2 V-05 excellence signals.

---

**v2 summary** (2026-03-16) -- R1 patterns

Three new aspirational criteria (C-11, C-12, C-13). C-05/C-06/C-10 clarified.

---

**v1 summary** (2026-03-16) -- initial rubric

Baseline from first golden construction.

---

## Scoring

| Weight | Criteria | Points each | Max |
|--------|----------|-------------|-----|
| Essential | C-01--C-05 | 10 | 50 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-43 | 2 | 70 |
| **Total** | | | **150** |

---

## Essential Criteria

*All must pass for golden.*

### C-01
- **Text**: Artifact header contains all 6 required fields.
- **Weight**: essential
- **Category**: format
- **Pass condition**: Header block contains exactly: `skill`, `topic`, `tier`, `category`, `flag`, `date`. All fields are present, non-empty, and in the standard header format. Any missing or misnamed field is a fail.

### C-02
- **Text**: CATEGORY is correctly assigned for the selected skill-id.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: HIGH-STRUCTURE skills (mock-ns, mock-all, mock-review, flow-lifecycle, flow-throttle, flow-trigger, flow-resilience, flow-dataflow, flow-conversation, flow-integration, trace-component, trace-contract, trace-deployment, trace-migration, trace-request, trace-permissions, trace-state, trace-skill, org-chart, org-committee, org-review, org-roles, scout-compliance, scout-requirements, scout-stakeholders, scout-naming, scout-positioning, scout-market, draft-brainstorm, draft-pitch, draft-spec, draft-proposal, program-plan, etc.) produce `HIGH-STRUCTURE`. EVIDENCE-HEAVY skills (prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption) produce `EVIDENCE-HEAVY`. MIXED skills (scout-competitors, prove-hypothesis, review-customers, review-users) produce `MIXED`. Any mismatch is a fail.

### C-03
- **Text**: FLAG is correctly computed from CATEGORY and tier, and written verbatim into the header.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: Flag value matches the S-3 case that applies: HIGH-STRUCTURE non-critical = `none (structural coverage reliable)`; HIGH-STRUCTURE critical at tier >= 2 = `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)`; EVIDENCE-HEAVY = `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)`; MIXED = `REVIEW-FOR-PLAUSIBILITY`. Compliance override applied when compliance tags are present for scout-compliance or trace-permissions. Any deviation from the case rules is a fail.

### C-04
- **Text**: Fidelity warning block is present and matches the assigned CATEGORY.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: A fidelity warning section appears between the header and the artifact body, delimited by `---`. The warning text matches the CATEGORY: EVIDENCE-HEAVY warning states the content is evidentially fabricated and a real run is required; MIXED warning distinguishes reliable structural elements from potentially fabricated specific claims; HIGH-STRUCTURE warning describes structural reliability and tier escalation. A generic or missing warning is a fail.

### C-05
- **Text**: Artifact body is skill-specific -- not generic prose.
- **Weight**: essential
- **Category**: depth
- **Pass condition**: A reader familiar with the target skill can identify which skill was mocked from the section headings, tables, and enforcement mechanisms alone -- without reading the header. The body includes all required section headings for the selected skill, at least one skill-specific table or scored list in its expected position, and a gate or verdict line where the real skill produces one. A body that could belong to any skill is a fail.

---

## Recommended Criteria

*Output is better with these. Failing one lowers the score but does not block golden.*

### C-06
- **Text**: S-1 setup emit lines are present: TOPICS.md status line and skill selection line.
- **Weight**: recommended
- **Category**: behavior
- **Pass condition**: Output contains a dedicated line in the form `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` and a second line `> Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...`. Both lines appear before the artifact header. The TOPICS.md line must appear first (S-0 before S-1). Having only the generating line -- even with tier present -- is a fail. Having only the TOPICS.md line is a fail. Both are required.

### C-07
- **Text**: Artifact is written to the correct path and the write confirmation is emitted.
- **Weight**: recommended
- **Category**: behavior
- **Pass condition**: Output contains `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`. The filename uses the namespace (not the skill-id), the topic matches the input, and the date matches the run date. A path using skill-id in place of namespace is a fail.

### C-08
- **Text**: Next-step line is the final line of the artifact.
- **Weight**: recommended
- **Category**: format
- **Pass condition**: The artifact ends with `Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md`. Omission is acceptable only when the skill was called from within a mock-review session to regenerate a thin namespace (the skill spec permits this); otherwise absence is a fail.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable. Each criterion is worth 2 pts (35 x 2 = 70; max score = 150).*

### C-09
- **Text**: Default skill selection follows the exclusion constraint for the `topic` namespace.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: When namespace=`topic` and no `--skill` flag is provided, the selected skill is `topic-plan`, not `topic-status`. `topic-status` is explicitly excluded as meta-structural. Selecting `topic-status` as default is a fail.

### C-10
- **Text**: Compliance override is applied when compliance tags are present.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: When TOPICS.md contains compliance tags and the selected skill is `scout-compliance` or `trace-permissions`, FLAG is overridden to `REAL-REQUIRED (compliance-sensitive)` regardless of CATEGORY or tier. If compliance tags are present and the override is not applied, the criterion fails. **If no compliance tags are present, the criterion passes by default** -- the absence of compliance tags is not a failure state.

### C-11
- **Text**: FLAG computation rule names critical skill namespaces explicitly and covers all 5 cases.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: The FLAG computation is expressed as a complete table or enumerated case list covering all 5 category/tier/skill-condition combinations: (1) HIGH-STRUCTURE non-critical any tier, (2) HIGH-STRUCTURE critical tier 1, (3) HIGH-STRUCTURE critical tier >= 2, (4) EVIDENCE-HEAVY, (5) MIXED. Critical namespaces are named explicitly as `trace-*`, `scout-feasibility`, and `listen-*` -- a generic description like "critical skills" without enumeration is not sufficient. Cases 1 and 2 may be collapsed into a single row when they share the same flag value; completeness is functional, not structural. **Note (R5 discriminator):** C-11 passing (functional 5-case coverage) does not imply C-22 passing (structural row separation). A 4-row table that collapses HS-critical-tier=1 into the non-critical catch-all satisfies C-11 but fails C-22. Source: R1 Pattern 2.

### C-12
- **Text**: TOPICS.md step resolves tier before skill selection begins.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The S-0 TOPICS.md step completes -- emitting the status line with tier -- before the S-1 skill selection step begins. A prompt that reads TOPICS.md and emits the status line but within the same step as skill selection does not satisfy this criterion. **Note (R2 canary):** Step-labeled separation with an explicit "carry tier into S-2 and S-3" handoff sentence satisfies this criterion -- a CONSTRAINT block is not required. The CONSTRAINT block (C-15) adds adversarial robustness but does not move the C-12 score. **Note (R3 discriminator):** C-17 and C-18 further strengthen C-12-passing implementations but are not required for C-12 itself. Source: R1 Pattern 1.

### C-13
- **Text**: Category lookup halts with a clear error on unrecognized skill-ids.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: When a skill-id is provided that does not exist in the canonical registry, the skill emits an error and stops -- it does not silently assign a fallback category or produce a mock with a guessed CATEGORY. The error message names the unrecognized skill-id and directs the user to the registry. A meta-instruction ("emit an error that names the skill-id and points to the registry") satisfies this criterion -- content requirements (name skill-id + registry pointer) are what matter, not template format. Source: R1 V-05; R2 Pattern 2 confirmed meta-instruction equivalence.

### C-14
- **Text**: Artifact assembly is expressed as discrete named steps, each a separate verifiable unit.
- **Weight**: aspirational (2 pts)
- **Category**: structure
- **Pass condition**: The prompt names at least 5 discrete assembly steps in sequence: A-1 HEADER (emit the 6-field header block), A-2 FIDELITY WARNING (emit the category-matched warning), A-3 BODY (emit the skill-specific sections and tables), A-4 WRITE (write the artifact to the correct path and emit the write confirmation), A-5 NEXT-STEP (emit the next-step line as the final output). Each step is labeled and addresses a single output responsibility. A prompt that produces the same outputs in prose sequence without discrete step labels does not satisfy this criterion. Source: R2 V-05 excellence signal -- "separated artifact assembly steps make each output responsibility a discrete verifiable unit."

### C-15
- **Text**: A CONSTRAINT block explicitly names the operations prohibited during S-0.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: A labeled CONSTRAINT section (or equivalent explicit prohibition block) appears at or within the S-0 step definition and names at minimum three prohibited operation types: no category lookup, no skill selection, no mock generation. The prohibition must name the operation types, not merely restate the ordering rule. **Note (R4 trap):** A CONSTRAINT rewritten to name steps ("Do not begin S-1, S-2, or S-3") rather than operation types loses C-15 even when C-17 is gained -- C-15 and C-17 require separate sentences to satisfy both simultaneously. **Note (R5 discriminator):** C-15 passing (3 op types) does not imply C-21 passing (4 op types including body generation). Source: R2 V-05.

### C-16
- **Text**: Wildcard patterns for critical namespaces appear directly in the FLAG table condition column.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: In the FLAG computation table, the condition cell for the critical HIGH-STRUCTURE case contains the wildcard patterns `trace-*` and `listen-*` directly in the match expression (e.g., "HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-*"). Listing these only in a footnote or expansion block while the condition cell reads "critical skill" does not satisfy this criterion. C-11 requires enumeration somewhere in the rule; C-16 requires that enumeration to appear in the condition column cell itself. Source: R2 V-05.

### C-17
- **Text**: S-0 contains an explicit advancement gate sentence that names S-1 and prohibits proceeding before the TOPICS.md emit line is produced.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: Within the S-0 step body, a sentence explicitly names S-1 (or equivalent next step) and states that it must not begin until the TOPICS.md status line has been emitted. Equivalent forms: "Do not begin S-1 until this line is emitted," "Before any other step begins, emit the TOPICS.md status line," or any phrasing that names the prohibited next step and makes the emit line a required precondition. **Note (R4 V-03 confirmation):** C-17 is content-based, not form-based. A CONSTRAINT-embedded sentence that names S-1 satisfies C-17 just as a standalone terminal sentence does. **Note (R5 discriminator):** C-17 passing (terminal gate names S-1) does not imply C-19 passing (dual-gate form). Source: R3 V-03.

### C-18
- **Text**: S-0 tier-carry handoff sentence names the downstream consuming steps by label.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 includes an explicit handoff sentence that (a) names the tier value as the carried artifact and (b) names at least two downstream steps by label that will consume it (e.g., "Carry the resolved tier into S-2 and S-3"). A prompt that carries the tier implicitly -- by having S-2 and S-3 reference tier without an explicit carry statement -- does not satisfy this criterion. A prompt that says "carry tier forward" without naming the consumers does not satisfy this criterion. **Note (R9 discriminator):** C-18 passing does not imply C-32 passing -- C-18 has no position constraint and is satisfied by any explicit handoff sentence including the compound-predicate opening declarative; C-32 requires that the C-20 standalone terminal sentence be in closing position independently of where C-18 is satisfied. V-03 and V-04 (R9) demonstrate this independence: the compound declarative satisfies C-18 but removal of the terminal standalone sentence fails both C-20 and C-32. Source: R3 V-02 and V-03.

### C-19
- **Text**: S-0 contains both a preamble gate and a terminal gate for the TOPICS.md emit requirement.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 contains two independent gate expressions addressing the same emit requirement: (1) a preamble gate, placed before the resolution bullets, in the form "Before any other step begins, emit the TOPICS.md status line" (or equivalent early-position sentence naming the emit as the first action); and (2) a terminal gate, placed after the resolution bullets, in the form "Do not begin S-1 until this line is emitted" (or equivalent closing enforcement sentence naming S-1). Both must be present. A step with only one gate form satisfies C-17 but not C-19. **Note (R5 discriminator):** C-17 pass does not imply C-19 pass. See C-23 for a further tightening of preamble gate position. Source: R4 V-05.

### C-20
- **Text**: Tier-carry appears in both a structured table downstream-use column and as a standalone terminal sentence.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The tier-carry contract is expressed in two independent registers: (1) within a structured parameter or resolution table, the tier row's downstream-use column explicitly states "Carry into S-2 and S-3" (or equivalent table cell naming both consumers); and (2) as a standalone terminal sentence in S-0 prose naming both consumers. Both must be present. A prompt with only a standalone sentence (satisfying C-18) or only a table column entry does not satisfy C-20. **Note (R9 discriminator):** A compound-predicate opening declarative that carries tier is not a standalone terminal sentence; position matters -- the terminal sentence must appear after the resolution logic, not co-located with the gate opening. V-03 and V-04 (R9) confirm: removing the standalone terminal sentence fails C-20 even when the compound declarative encodes tier-carry (C-18 satisfied). C-20 failing from this structural choice also fails C-32. Source: R4 V-05.

### C-21
- **Text**: CONSTRAINT block names 4 or more prohibited operation types, including body generation.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The CONSTRAINT block (required for C-15) names at minimum 4 prohibited operation types: no category lookup, no skill selection, no mock generation, and no body generation. The C-15 minimum of 3 types is necessary but not sufficient. Body generation must be named explicitly as a fourth prohibited type. **Note (R5 discriminator):** C-15 passing (3 op types) does not imply C-21 passing (4 op types). See C-24 for an extension requiring a 5th op type (artifact write phase). Source: R4 V-05.

### C-22
- **Text**: FLAG table separates HIGH-STRUCTURE critical tier=1 from HIGH-STRUCTURE non-critical as distinct rows.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: The FLAG computation table contains a dedicated row for HIGH-STRUCTURE critical skills at tier=1 (flag: none) and a separate row for HIGH-STRUCTURE non-critical skills (flag: none), even though both rows produce the same flag value. C-11 passes when cases 1 and 2 are functionally covered (even collapsed); C-22 requires explicit row separation. The tier-1 critical row must name the critical namespaces in its condition cell (consistent with C-16). **Note (R5 confirmation):** C-11 passing is a necessary but not sufficient condition for C-22. Source: R4 V-05.

### C-23
- **Text**: Preamble gate is the opening sentence of S-0, preceding all resolution logic including the parameter table.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The preamble gate sentence (required for C-19) appears as the absolute first sentence in the S-0 step body -- before any resolution bullets, parameter rows, or introductory prose. C-19 requires the preamble gate to be before the resolution bullets; C-23 requires it to be the first content of the step with no pre-gate surface area. A one-sentence introduction followed by the preamble gate satisfies C-19 but fails C-23. A CONSTRAINT block that precedes the preamble gate fails C-23 even when all other gate criteria are met -- CONSTRAINT is defense-in-depth, not the primary barrier, and must follow the gate, not precede it. **Note (R6 discriminator):** C-23 passing (gate as opening sentence) does not imply C-25 passing (declarative identity sentence preceding the imperative). V-01 (R6) uses single-imperative form at S-0 opening -- passes C-23, fails C-25. Source: R5 V-03 canary; R6 V-02/V-04 CONSTRAINT-first pattern.

### C-24
- **Text**: CONSTRAINT block names 5 or more prohibited operation types, including artifact-write operations.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The CONSTRAINT block (required for C-21) names at minimum 5 prohibited operation types: no category lookup, no skill selection, no mock generation, no body generation, and no artifact-write operations (no path assignment, no directory creation, no file write until A-4 WRITE begins). Body generation and write-phase operations must each be named explicitly. **Note (R5 discriminator):** C-21 passing (4 op types) does not imply C-24 passing (5 op types). C-24 extends the operation set from "body" to explicit write-phase operations naming the delayed-write constraint. Source: R5 V-05.

### C-25
- **Text**: S-0 opens with a declarative identity sentence preceding all imperative resolution bullets.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 begins with a declarative sentence (not an imperative) that identifies what the step is or does, such as "This step resolves the tier." or "S-0's role is to read TOPICS.md." The sentence must precede the first imperative bullet; it answers "What is this step?" before the bullets answer "How?". A step that opens with imperative bullets ("Read TOPICS.md...") without a declarative preamble fails C-25. A step that opens with a gate sentence (C-17, C-19) instead of a declarative identity sentence fails C-25 -- gates are enforcement, not identity. **Note (R6 discriminator):** C-23 passing (gate as opening sentence) does not imply C-25 passing (declarative identity sentence before the gate). R6 V-01 demonstrates: single-imperative opening passes C-23 but fails C-25; C-25 requires a declarative sentence that establishes identity before the gates appear. The identity sentence and the gate are separate and both necessary for the full sequence. **Note (R12 discriminator):** C-25 order-strict: step identity sentence (what-is-this-step) must precede gates (no, never, stop). C-25 also fails when order predicate appears as the main predicate in S-0's role declaration. R12 V-01 ("S-0, which emits TOPICS.md first, runs before all other steps") uses step as main-clause subject of an ordering verb -- the main predicate is the ordering verb, not the emit action. This violates C-25's requirement that the role-declaration sentence make the step's PRIMARY function clear, not its ordering. V-03 ("This step's first action is emitting...") also fails because step appears as possessor in the subject NP, not as nominative subject; the true subject is "first action". Source: R5 V-03; R6 V-02, V-04; R12 V-01, V-03.

### C-26
- **Text**: Declarative identity sentence explicitly names the step output (tier or other artifact resolved by S-0).
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The declarative identity sentence (required for C-25) names the artifact resolved by S-0. For S-0 reading TOPICS.md, it must name tier explicitly: "This step resolves the tier" or "S-0 determines the tier value from TOPICS.md." Naming the step's action in isolation ("This step reads TOPICS.md") without naming the output does not satisfy C-26. **Note (R6 discriminator):** C-26 is content-based (what artifact does the step output?) while C-25 is structural (does identity precede gates?). Both are necessary; both can be satisfied simultaneously. Source: R5 V-03; R6 V-02 canary.

### C-27
- **Text**: S-1 skill selection begins only after S-0 TOPICS.md read completes and tier is available.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-1 contains an opening statement that references the tier resolved by S-0, such as "Using the tier from S-0..." or "Now that tier is resolved, select the skill...". The tier must appear as available input to S-1, not as an incidental detail. A step S-1 that selects skill without acknowledging the tier input from S-0 does not satisfy C-27. **Note (R7 discriminator):** C-27 is advancement acknowledgment (S-1 confirms S-0 output is available). C-28 is emission discipline (S-0 must emit the status line first). Both are necessary. Source: R6 V-02/V-04; R7 patterns.

### C-28
- **Text**: S-0 grammatically positions the step as nominative subject of the emission action.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: Within S-0 or its gates, a sentence exists in which the step is the grammatical nominative subject and the emission action is the main predicate: "This step emits the TOPICS.md status line" or "S-0 produces the TOPICS.md status line." The grammar must position the step-subject and the emission-predicate in the main clause (not subordinated). **Note (R7 discriminator):** Passivization passes: "The TOPICS.md status line is emitted by this step." Agent position satisfies the C-28 requirement for step agency. Superlatives with step-subject and infinitival emission pass: "This step is the first to emit the TOPICS.md status line." Control structure (step as controller of to-emit) is equivalent to nominative-subject + active-predicate. Relative clauses with step as agent but artifact as main-clause subject fail: "TOPICS.md, which this step emits, is the first artifact." Step is agent in a subordinate clause, not the main-predicate subject. **Note (R12 discriminator):** Step as main-clause subject with ordering verb fails when emission is confined to relative clause (R12 V-01). Superlative-equative + infinitival-control passes (R12 V-04): step is main-clause subject and controller of emission-infinitival. **Note (R14 discriminator):** Focus-particle adverbs (only, just, even) scoped over the step-subject NP do not displace the step from nominative subject position. "Only this step emits the TOPICS.md status line" satisfies C-28: the step is the grammatical nominative subject, the emission is the main predicate, and the focus particle is a scope operator on the subject NP, not a displacement mechanism. No declarative-form criterion (C-29--C-43) fires for focus-particle scoping. R14 V-03 142/146 confirmation. **Note (R15 discriminator):** Step-scope boundary confirmed. C-28 requires the emission sentence to appear within S-0 or its gates -- not in any other step. A grammatically correct emission sentence (nominative step-subject + emission predicate) that appears in S-1 or a later step does not satisfy C-28. When S-0 does not exist as a discrete step (collapsed into S-1), no emission sentence can satisfy C-28 regardless of grammatical form; the sentence is in the wrong step scope. Grammatical form is necessary but not sufficient; step scope is independently required. C-42 names the displacement as a co-firing criterion. R15 V-01 canonical: "Only this step emits the TOPICS.md status line" in S-1 (S-0 absent) -- C-28 fails, C-42 fires. Source: R6 V-02/V-04; R7 patterns; R12 V-01, V-04; R14 V-03; R15 V-01.

### C-29
- **Text**: Possessive-nominal subject form in emission description is prohibited.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence describes S-0's emission action using a possessive-nominal subject form, such as "This step's action is emitting..." or "S-0's responsibility is producing...". The step must be the nominative subject, not a possessor modifier. A substitution test applies: if substituting "It" for the subject NP (e.g., "It is emitting...") the referent shifts from the step to a deverbal noun or abstraction (action, responsibility, role), then the criterion fails. **Note (R8 discriminator):** This passes: "This step emits the TOPICS.md status line" (step is subject). This fails: "This step's action is emitting the TOPICS.md status line" (action is subject; step is possessor). Possessive-nominal subject demotes the agent to a modifier. **Note (R13 discriminator):** C-29's substitution test extends to wh-action-nominalizations. "What this step does first is emit..." -- substituting `It` gives "It is emit..." where `It` = the wh-nominalization `What this step does first`, not the step itself. C-39 names this wh-pseudo-cleft form; C-29 remains the trigger criterion. Source: R7 V-05; R8 patterns; R13 V-02.

### C-30
- **Text**: Artifact-as-subject form in emission description must not appear in active voice.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence describes S-0's emission using the artifact as the active-voice main-clause subject, such as "The TOPICS.md status line is the first thing this step emits." The artifact may appear as subject in passive voice ("The TOPICS.md status line is emitted by this step") or in other grammatical positions. The prohibition applies specifically to artifact-as-subject in active voice with step as oblique agent. **Note (R8 discriminator):** Active-voice artifact-subject form is distinct from passivization and must be named. Passivization is explicitly permitted; active artifact-subject is not. A step-relative-clause variant ("TOPICS.md is the artifact this step emits") also violates this criterion -- artifact remains the main-clause subject with step as oblique agent in a subordinate clause. Source: R8 patterns.

### C-31
- **Text**: Modal-obligation forms (must, shall, should, is required to) are prohibited in S-0 role declaration.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The S-0 role-declaration sentence (C-25, C-26) does not use modal-obligation forms: no "must", "shall", "should", or "is required to". Deontic forms impose an obligation tone that is inconsistent with declarative identity. A sentence like "This step must emit the TOPICS.md status line" uses deontic form and fails C-31. Prescriptive sentences in CONSTRAINT blocks (C-15) may use deontic forms; C-31 applies specifically to the S-0 identity sentence and gates. **Note (R9 discriminator):** C-31 targets deontic form in the wrong discourse register. Identity sentences are declarative; obligations are prescriptive. A single word (must/shall/should) can trigger C-25+C-28+C-31 failure if the sentence structure is wrong, or trigger only C-31 if C-25/C-28 are otherwise satisfied. **Note (R14 discriminator):** C-31 fires independently of C-25 and C-28. When the role-declaration sentence is structurally correct (step as nominative subject, emission as main predicate -- satisfying C-25 and C-28) but uses a modal-obligation form, C-31 fires alone. "This step must emit the TOPICS.md status line before any other step may proceed" -- C-25 passes (declarative, step as subject), C-28 passes (step + emission in main clause), C-31 fires (modal "must"). R14 V-04 canonical: hypothesis 142/146 incorrect; correct score 144/146. Source: R8 V-05; R9 patterns; R14 V-04.

### C-32
- **Text**: Tier-carry standalone terminal sentence appears in closing position within S-0.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 contains a standalone sentence in closing position that explicitly carries the tier to downstream consumers, such as "Carry the resolved tier into S-2 and S-3" or "The tier determined in this step will be used by S-2 and S-3." Position matters: the sentence must appear after the resolution bullets, not co-located with the opening gate or declarative identity. A compound-predicate sentence that opens S-0 ("This step resolves tier and carries it to S-2 and S-3") satisfies C-18 but does not satisfy C-32 without a separate closing sentence. **Note (R9 discriminator):** C-18 and C-20 satisfaction does not guarantee C-32. C-18 requires a handoff sentence naming consumers (any position); C-20 requires both a table entry and a standalone sentence (any position for the sentence, as long as both exist); C-32 requires the standalone terminal sentence specifically in closing position. V-03 and V-04 (R9) confirm: removing the standalone closing sentence fails C-32 even when C-18 and C-20 are satisfied through other means. **Note (R15 discriminator):** Lifecycle annotation interaction. When lifecycle entry/exit state blocks are appended to S-0, C-32 passes if the tier-carry terminal sentence remains present as a discrete prose sentence (even if a lifecycle annotation follows it). C-32 fails if the lifecycle annotation replaces the terminal sentence -- the sentence must exist as a standalone prose sentence, not be subsumed into or displaced by a lifecycle state block. C-43 names the replacement form as a co-firing criterion: lifecycle-annotation replacement -> C-32 fails, C-43 fires. Supplementation (annotation follows sentence) -> C-32 passes, C-43 passes. R15 V-02 boundary: supplementation -> 150/150; replacement -> 148/150. Source: R9 V-03, V-04; R15 V-02.

### C-33
- **Text**: Passive artifact-as-subject form in emission description is prohibited in S-0.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 describes emission using passive artifact-as-subject form, such as "The TOPICS.md status line is the first artifact emitted by this step." The artifact may be the object of an active-voice emission verb or appear in other positions, but not as the subject (active or passive) of an emission verb. Step must be the nominative subject; this criterion closes the passive-voice loophole. **Note (R10 discriminator):** C-30 prohibits artifact as active-voice subject; C-33 prohibits artifact as passive-voice subject. Both are necessary because passive is sometimes mistaken for neutrality. Passivization is permitted when artifact is NOT the main-clause subject: "The TOPICS.md status line is emitted" (no agent explicit; artifact is just complement). But "The TOPICS.md status line is emitted by this step" (artifact = subject, step = agent) is still prohibited because the sentence structure privileges the artifact. **Clarification (R10 V-04):** This passes: "This step emits the TOPICS.md status line." This fails: "The TOPICS.md status line is emitted by this step" if it appears as the main emission description. C-33 names the passive artifact-subject form as a named failure mode, distinct from C-30's active form. **Note (R11 discriminator):** C-30 (active) and C-33 (passive) together close both voices for artifact-as-subject. C-35 adds the relative-clause-agent variant (step as agent in a relative clause modifying the artifact-subject). **Note (R14 discriminator):** Passive artifact-as-subject with step-agent in a by-PP fires C-33 and does not additionally trigger C-35. The step appears in a prepositional phrase ("by this step"), not in a subordinate relative clause. C-41 names this scope boundary explicitly: by-PP -> C-33 only. R14 V-01 canonical: "The TOPICS.md status line is emitted by this step before any other step begins" -- fails C-33, passes C-35. Source: R9 V-05; R10 patterns; R11 patterns; R14 V-01.

### C-34
- **Text**: Gerundive-as-subject form is prohibited in S-0 role description.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 uses a gerundive (verbal noun ending in -ing) as the nominative subject of the emission description, such as "Emitting the TOPICS.md status line is this step's first action." The step must be the subject of the emission verb; the gerundive must be embedded as a complement or in another role, not promoted to subject position. **Note (R10 discriminator):** Gerundive as subject fails C-34. Gerundive as object or predicate complement passes: "This step performs emitting the TOPICS.md status line" (object) or "This step's action is emitting..." (predicate complement -- although the latter may fail C-29). Promotion to subject position is the failure mode. Gerundive-as-subject with infinitival emission passes: "Resolving the tier precedes emitting the TOPICS.md status line" -- the gerundives are subjects of their respective clauses, but neither is the main S-0 emission description; the structure describes ordering, not S-0's own emission. Source: R10 V-03; R11 patterns.

### C-35
- **Text**: Artifact as main-clause subject with step as relative-clause agent is prohibited.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 uses the artifact as the nominative main-clause subject with the step as the grammatical agent in a subordinate (relative or other) clause, such as "TOPICS.md is the first artifact this step emits." The step must be the nominative main-clause subject. If the artifact appears as subject, the step must not be the agent (as in passive voice where agent is oblique and the artifact is just a subject). **Note (R11 discriminator):** This structure is the relative-clause-agent displacement: artifact is the main-clause subject; step is demoted to an agent-role within a subordinate clause, not the nominative subject of the main clause. C-35 names this as a failure mode, distinct from C-30/C-33 which prohibit artifact-as-subject when step appears as active/passive agent in the same main clause. **Note (R12 discriminator):** C-35 covers artifact-subject / step-relative-clause-agent; it does NOT cover ordering-predicate displacement (C-36) or possessive-NP action-abstraction displacement (C-37). Evaluators must not extend C-35 to V-01-type or V-03-type R12 constructions. **Note (R14 discriminator):** C-35 requires the step to appear as agent inside a subordinate relative clause or equivalent subordinate clause -- not in a by-PP. A by-PP ("by this step" in a passive construction) is a phrase-level adjunct and does not contain a verb; it is structurally distinct from a relative clause ("that this step emits", "which this step produces"). When the artifact is the passive main-clause subject and the step appears in a by-PP, C-33 is the applicable criterion and C-35 does not fire. C-41 names this boundary explicitly. R14 V-01 canonical boundary: passive + by-PP -> C-33 fires, C-35 passes. Source: R11 patterns; R12 context; R14 V-01.

### C-36
- **Text**: Ordering predicate (runs, begins, precedes) as main clause verb is prohibited when step is subject.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 uses the step as the nominative main-clause subject with an ordering verb (e.g., "runs", "begins", "precedes", "first", "follows") as the main predicate. Ordering verbs express sequencing, not emission. If the step is the main-clause subject, the main predicate must be the emission verb itself or a verb that establishes identity/role. An ordering verb may appear in a subordinate clause ("S-0, which emits the status line first, comes before S-1") but not as the main predicate when step is subject. **Note (R12 discriminator):** This is the inverse pattern to C-35: C-35 has artifact as main-clause subject with step subordinated; C-36 has step as main-clause subject but ordering verb (not emission) as the main predicate. Both demote the emission description below the main clause. The evaluator trap for C-36 is crediting "the step is the main-clause subject" without checking whether the main predicate is emission or ordering. C-28 requires main-clause step-subject with emission main predicate; C-36 prohibits ordering as the main predicate. **Note (R13 discriminator):** C-36 applies specifically when emission is relegated to a restrictive relative clause. Compound-sentence-split form ("This step runs first; it emits the TOPICS.md status line") does NOT fire C-36 -- emission is in a second independent coordinate clause, not a relative clause. The compound-sentence-split pattern fails C-25 and C-28 only; C-36 does not apply (R13 V-03 boundary). Source: R12 V-01; R13 V-03.

### C-37
- **Text**: Possessive-NP action-abstraction subject with gerundive emission is prohibited.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 uses the form "This step's {abstraction-noun} is {gerundive}...", such as "This step's first action is emitting the TOPICS.md status line." The step appears as a possessor modifier, not a nominative subject. The true subject is the abstraction (action, task, responsibility). The gerundive appears as a predicate complement. This is a compound failure combining possessive-nominal subject (C-29) with gerundive-as-predicate-complement (C-34-adjacent), and oblique step positioning (C-30). **Note (R12 discriminator):** C-37 is the eighth declarative failure mode, distinct from C-29 (possessive-nominal with infinitival predicate like "...is to emit") and C-34 (gerundive-as-subject like "Emitting...is S-0's action"). In R12 V-03, this pattern fired C-35 "by extension" because no proper named criterion existed; C-37 closes the gap. C-34 passes (gerundive is predicate complement, not subject). C-35 and C-36 pass (artifact not subject; no ordering predicate). Source: R12 V-03; eight declarative failure modes fully enumerated.

### C-38
- **Text**: Expletive-subject it-cleft with step as cleft-focus NP and emission in relative clause is prohibited.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 uses an it-cleft construction in which the grammatical subject is expletive `It`, the step appears only as the cleft-focus NP (e.g., "It is this step that..."), and emission is confined to the restrictive relative clause (e.g., "...that first emits the TOPICS.md status line"). In this form `this step` is not the grammatical nominative subject -- expletive `It` is the formal subject, and the main predicate is the equative/presentational copula `is`. The evaluator trap: `this step` appears prominently and the emission verb is present, but both are displaced from main-clause subject and main-predicate positions. C-29 does not fire (expletive `It` is not a nominalization derived from the step -- it is a formal placeholder with no referential content). C-35 does not fire (the artifact is not the main-clause subject; expletive `It` is). C-36 does not fire (the main predicate is copula `is`, not an ordering verb). C-38 names this ninth declarative failure mode. **Note (R13 discriminator):** C-38 is distinct from C-39 (wh-pseudo-cleft): in C-38 the formal subject is expletive `It` with no referential content; in C-39 the subject is a wh-nominalization that embeds the step as an internal referent and C-29 fires. Failure chain: C-25, C-28, C-38 (-6 pts). Source: R13 V-01.

### C-39
- **Text**: Wh-pseudo-cleft with step embedded in subject nominalization and emission in predicate complement is prohibited.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 uses a wh-pseudo-cleft construction in which the grammatical subject is a wh-action nominalization (e.g., "What this step does first"), the main predicate is the equative copula `is`, and emission appears as predicate complement (e.g., "...is emit the TOPICS.md status line"). In this form the step is not the main-clause nominative subject -- it is embedded as an internal referent inside the wh-clause subject. C-29's substitution test fires: substituting `It` for the subject NP yields "It is emit the TOPICS.md status line" where `It` = the wh-action nominalization `What this step does first`, not the step itself. C-39 extends C-29's coverage from possessive-NP action-abstractions to wh-action-nominalizations, and names this tenth declarative failure mode. C-36 passes (main predicate is copula, not ordering verb). C-37 passes (no possessive-NP construction). **Note (R13 discriminator):** C-39 is distinct from C-38 (it-cleft with expletive subject): in C-39 the subject is a content-bearing wh-clause that contains the step as an embedded referent, and C-29 fires via the substitution test; in C-38 the subject is a formal expletive with no content, and C-29 does not fire. Failure chain: C-25, C-28, C-29, C-39 (-8 pts). Source: R13 V-02; ten declarative failure modes enumerated.

### C-40
- **Text**: Existential-there negation as ordering statement is prohibited in S-0.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: No sentence in S-0 describes the step's primacy using an existential-there negation in which expletive `There` is the grammatical subject and the step appears only as genitive possessor inside the object phrase. The canonical failure form is "There is no step that precedes this step's TOPICS.md status line emission": expletive `There` is subject; "no step" is the postponed nominal; the step (`this step`) is demoted to genitive possessor in "this step's TOPICS.md status line emission." Neither the step nor the emission action occupies nominative-subject + main-predicate position. The evaluator trap: the sentence asserts that this step is first (by negating any predecessor), which might be mistaken for a declarative identity statement. It is not -- it describes ordering relationally, not the step's own emission identity. C-38 does not fire (C-38 requires equative-copula `It`-cleft with a cleft-focus NP; C-40 addresses existential-there with a different structure). C-39 does not fire (no wh-action nominalization subject). C-40 names this eleventh declarative failure mode. **Distinction from C-38:** C-38 has expletive `It` as subject with equative copula `is` and a cleft-focus NP; C-40 has expletive `There` as subject with existential `is` and a postponed nominal. Both displace the step from nominative subject position through different formal mechanisms. Failure chain: C-25, C-28, C-40 (-6 pts). Source: R14 V-02; eleven declarative failure modes enumerated.

### C-41
- **Text**: C-35 (relative-clause-agent displacement) scope is restricted to subordinate-clause agent confinement; by-PP agent in passive construction does not trigger C-35.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: When evaluating S-0 for C-35, the criterion applies only when the step appears as grammatical agent inside a subordinate relative clause or equivalent subordinate clause (a clause with a verb, such as "that this step emits" or "which this step produces"). A by-PP ("by this step") in a passive construction is a phrase-level adjunct -- it contains no verb and does not constitute subordinate-clause confinement. Passive artifact-as-subject with step-agent in a by-PP is evaluated against C-33 (passive artifact-as-subject prohibited) and passes C-35. Evaluators must not extend C-35 to by-PP constructions or compound the C-33 failure by additionally applying C-35. The by-PP form is a phrase-level constituent; C-35 requires a clause-level constituent. **Canonical R14 V-01 boundary:** "The TOPICS.md status line is emitted by this step before any other step begins" -- fails C-33 (passive artifact = subject), passes C-35 (step is in a by-PP, not a relative clause), passes all other declarative-form criteria. Failure chain for passive + by-PP: C-33 only (-2 pts). **Distinction from C-35:** C-35's canonical failure form is "TOPICS.md is the first artifact this step emits" -- step is agent in the relative clause "this step emits" (verb present). C-41's boundary form is "...is emitted by this step" -- step is in a prepositional phrase "by this step" (no verb). Source: R14 V-01; C-35 scope boundary confirmed.

### C-42
- **Text**: C-28 step-scope boundary -- a grammatically correct emission sentence in a step other than S-0 does not satisfy C-28.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: When evaluating S-0 for C-28, the emission sentence must appear within S-0 or S-0's gates. A sentence in S-1, S-2, or any other step that satisfies C-28's grammatical requirements (step as nominative subject, emission as main predicate) does not retroactively satisfy C-28 -- it is in the wrong step scope. When S-0 does not exist as a discrete step (collapsed into S-1 or merged with another step), C-28 cannot be satisfied regardless of grammatical form anywhere in the output. C-42 names step-scope displacement as a distinct failure mode: the emission sentence is grammatically correct but located outside S-0 or its gates. Evaluators must not credit C-28 based on grammatical form alone; step scope is independently required. C-42 passes by default when the output either (a) contains a grammatically correct emission sentence within S-0 or its gates, or (b) contains no displaced emission sentence. C-42 fires when a grammatically correct emission sentence exists in a step other than S-0. **Canonical R15 V-01 boundary:** "Only this step emits the TOPICS.md status line" appears in S-1 (S-0 is absent, collapsed into S-1). Grammatical form: satisfies C-28 requirements (focus-particle step-subject + emission predicate). Step scope: S-0 does not exist; the sentence is in S-1. Result: C-28 fails, C-42 fires. Failure chain for step-scope displacement: C-28, C-42 (-4 pts). **Distinction from C-28:** C-28 requires the grammatical form + step-scope together; C-42 names the isolated case where the grammatical form is correct but step scope fails. The two criteria co-fire when a correctly-formed emission sentence appears outside S-0. Source: R15 V-01; C-28 step-scope boundary confirmed.

### C-43
- **Text**: Lifecycle entry/exit state annotations must not replace the standalone tier-carry terminal sentence in S-0.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: When lifecycle annotations (entry/exit state declarations per step boundary) are added to S-0, the standalone tier-carry terminal sentence (required for C-32) must remain present as a discrete prose sentence. Two interaction forms: (1) supplementation -- the lifecycle exit-state annotation appears after the tier-carry terminal sentence; C-32 passes (sentence is present as discrete prose, annotation is supplementary); C-43 passes; (2) replacement -- the lifecycle exit-state annotation takes the structural position of the tier-carry terminal sentence, eliminating it; C-32 fails (standalone sentence absent); C-43 fires (replacement displacement named). Evaluators must check for the presence of the tier-carry sentence as a discrete standalone sentence, not merely check whether it is the absolute final token in S-0; a lifecycle annotation that follows the sentence does not negate the sentence's existence. **Canonical R15 V-02 boundary:** If lifecycle exit-state block appears after the tier-carry terminal sentence (supplementation) -> C-32 PASS, C-43 PASS -> **150/150**. If lifecycle exit-state block replaces the tier-carry terminal sentence (replacement) -> C-32 FAIL, C-43 FAIL -> **148/150**. **Distinction from C-32:** C-32 requires the standalone terminal sentence to exist in closing position; C-43 names the specific lifecycle-annotation replacement as the co-firing cause when C-32 fails in a lifecycle-annotation context. In non-lifecycle contexts, C-43 passes by default. Source: R15 V-02; C-32 lifecycle-annotation interaction boundary confirmed.
