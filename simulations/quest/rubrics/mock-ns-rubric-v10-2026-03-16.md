Written to `simulations/quest/rubrics/mock-ns-rubric-v10-2026-03-16.md`. 338 lines, C-01 through C-32 all present.

---

**v10 summary: 2 new criteria, 2 new failure traps**

| ID | Text | Source |
|----|------|--------|
| C-31 | Gate declarative must use indicative mood, not deontic/modal-obligation form -- "This step must emit first" fails because modal "must" is deontic, converting the sentence from a pipeline role-declaration to a behavioral prescription; deontic form causes simultaneous failure of C-25 and C-28 | R9 V-02 |
| C-32 | C-18 (explicit handoff, any position) and C-20 (standalone terminal sentence, closing position) are structurally independent and cannot be satisfied by the same sentence when that sentence is the gate opener -- a compound-predicate declarative encoding tier-carry in the opening gate satisfies C-18 but not C-20 | R9 V-03/V-04 |

**Key structural result:** V-02 (R9) reveals the deontic failure class -- a single word ("must") triggers C-25, C-28, and C-31 simultaneously. The three criteria remain independent because C-25 tests sentence type, C-28 tests subject-predicate structure, and C-31 tests mood. V-03 and V-04 (R9) confirm C-18 and C-20 are position-sensitive and independent: the compound-predicate opener cannot serve as the S-0 terminal without losing C-20 and C-32.

**Scoring:** max rises from 124 to **128** (24 aspirational x 2 = 48). V-01 and V-05 score 128/128. V-03 and V-04 score 124/128 (fail C-20 + C-32 from same structural choice). V-02 scores 122/128 (fails C-25 + C-28 + C-31 from one modal word).

**Existing criteria updated:**
- **C-18**: R9 discriminator note added -- C-18 has no position constraint; satisfying it via compound opener does not imply C-32 passing
- **C-20**: R9 discriminator note added -- the compound-predicate gate opener is not a terminal sentence; position matters
- **C-25**: R9 discriminator note added -- deontic "must emit" fails C-25, simultaneously failing C-28 and C-31
- **C-28**: R9 discriminator note added -- modal-obligation form fails C-28 even when the step is grammatical subject
e same structural choice (removing the terminal standalone sentence), scoring 124/128. V-02 fails C-25, C-28, and C-31 from a single modal word, scoring 122/128.

---

### v9 (2026-03-16) -- R8 patterns promoted to aspirational criteria

**Two new criteria (C-29, C-30) from R8.** Two new failure traps. Scoring max rises from 120 to **124** (22 aspirational x 2 = 44).

| ID | Text | Source |
|----|------|--------|
| C-29 | Declarative sentence must have the step as direct nominative subject -- possessive-nominal form ("This step's [noun]") fails because the nominalization becomes subject and the step is demoted to genitive modifier | R8 V-02 |
| C-30 | Declarative sentence must not promote an artifact to nominative subject in active voice -- "The TOPICS.md status line is the first output of this step" fails because the artifact is subject and the step appears only as oblique modifier "of this step" | R8 V-01 |

---

### v8 (2026-03-16) -- R7 patterns promoted to aspirational criteria

**Two new criteria (C-27, C-28) from R7.** Two new failure traps. Scoring max rises from 116 to **120**.

---

### v7 (2026-03-16) -- R6 patterns promoted to aspirational criteria

**Two new criteria (C-25, C-26) from R6.** Two new failure traps. Scoring max rises from 112 to **116**.

---

### v6 (2026-03-16) -- R5 patterns promoted to aspirational criteria

**Two new criteria (C-23, C-24) from R5.** Three new failure traps. Scoring max rises from 108 to **112**.

---

### v5 (2026-03-16) -- R4 patterns promoted to aspirational criteria

**Four new criteria (C-19, C-20, C-21, C-22) from R4.** C-17 clarified (content-based, not form-based). Scoring max rises from 100 to **108**.

---

### v4 (2026-03-16) -- R3 patterns promoted to aspirational criteria

**Two new criteria (C-17, C-18) from R3.** Aspirational drops from 2.5 to 2 pts each (max remains 100).

---

### v3 (2026-03-16) -- R2 patterns promoted to aspirational criteria

**Three new aspirational criteria (C-14, C-15, C-16) from R2 V-05 excellence signals.**

---

### v2 (2026-03-16) -- R1 patterns promoted to aspirational criteria

**Three new aspirational criteria (C-11, C-12, C-13) from R1.** C-05/C-06/C-10 clarified.

---

### v1 (2026-03-16) -- initial rubric

Baseline from first golden construction.

---

## Scoring

| Weight | Criteria | Points each | Max |
|--------|----------|-------------|-----|
| Essential | C-01--C-05 | 10 | 50 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-32 | 2 | 48 |
| **Total** | | | **128** |

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

*Raise the bar once essential and recommended are stable. Each criterion is worth 2 pts (24 x 2 = 48; max score = 128).*

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
- **Text**: CONSTRAINT names 5 or more prohibited operation types, adding artifact path construction or file write to the C-21 minimum.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The CONSTRAINT block (required for C-15; extended by C-21 to 4 types) names at minimum 5 prohibited operation types, where the fifth closes the artifact-write phase: no artifact path construction, no artifact file write, or equivalent language prohibiting any A-4 WRITE phase activity during S-0. A complete adversarial-coverage CONSTRAINT closes all production phases in sequence: discovery (lookup), decision (selection), output generation (mock generation), content production (body generation), and artifact output (path construction / file write). Synonym vocabulary for the 5th prohibition is acceptable (e.g., "No artifact path assembly or file output"). **Note (R6 discriminator):** C-24 passing (5-op CONSTRAINT with artifact write) does not imply C-26 passing (synonym-vocabulary CONSTRAINT). V-02 and V-03 (R6) use canonical 5-op phrases -- pass C-24, fail C-26. Source: R5 V-01 boundary; R6 V-05 confirmed synonym equivalence.

### C-25
- **Text**: S-0 preamble gate uses two-sentence form: a declarative identity assertion followed by an imperative emit instruction.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The S-0 preamble gate (required for C-23) consists of two sentences: (1) a declarative identity sentence asserting the step's emit primacy as a statement of the step's ROLE -- "This step emits first," "S-0 is the emit step," or equivalent present-tense declaration that names the step's defining function; and (2) an imperative instruction naming what must be emitted and when -- "Write the TOPICS.md status line before any other work begins," or equivalent command. Both sentences must be present at S-0 opening. A single-sentence imperative gate (satisfying C-23) does not satisfy this criterion -- it provides the command but not the identity declaration. The declarative sentence establishes that the emit is the step's definitional behavior, not merely a conditional precondition; the imperative sentence provides the operational directive. The two-layer form eliminates ambiguity about whether the gate is enforced vs. advisory by asserting the step's identity before issuing the command. **Note (R6 discriminator):** C-23 passing is a necessary but not sufficient condition for C-25. V-01 (R6) uses single-imperative form -- passes C-23, fails C-25. **Note (R7 discriminator):** C-25 passing does not imply C-27 passing -- a three-sentence elaborated gate may satisfy C-25 on a type-coverage reading while failing C-27's count-strict requirement. C-25 passing does not imply C-28 passing -- an output-primacy declarative ("The first observable output...") may be judged to satisfy C-25's role-assertion language while failing C-28's grammatical-subject test. **Note (R9 discriminator):** A gate declarative using deontic/modal-obligation form ("This step must emit first") fails C-25 because "must emit" prescribes behavior rather than asserting the step's role; the sentence is a requirement-imposition, not a role-declaration; deontic form simultaneously fails C-28 and C-31. See C-31 for the standalone deontic-mood criterion. Source: R6 V-05 only.

### C-26
- **Text**: CONSTRAINT uses synonym vocabulary for each prohibited operation type, not canonical phrase repetition.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: Each prohibition in the CONSTRAINT block is expressed using vocabulary that is semantically equivalent to but lexically distinct from the canonical op-type label used elsewhere in the skill spec. All op-type prohibitions must use distinct vocabulary -- e.g., "No lookup of skill categories" instead of "No category lookup"; "No skill-id resolution" instead of "No skill selection"; "No mock content generation" instead of "No mock generation"; "No artifact body construction" instead of "No body generation"; "No artifact path assembly or file output" instead of "No artifact path construction or file write." A CONSTRAINT that repeats the canonical op-type phrases verbatim (satisfying C-15/C-21/C-24) does not satisfy this criterion. The synonym form demonstrates that each prohibition is understood at the concept level -- the spec author cannot rely on exact-match phrase enforcement and must understand what each phrase means to paraphrase it correctly. A CONSTRAINT with even one op-type in canonical phrase form does not satisfy this criterion; all op-type prohibitions must use distinct vocabulary. **Note (R6 discriminator):** C-24 passing (5-op CONSTRAINT) does not imply C-26 passing. V-02 and V-03 (R6) use canonical phrases throughout -- pass C-24, fail C-26. Source: R6 V-05 only.

### C-27
- **Text**: S-0 preamble gate is count-strict exactly two sentences -- no elaborative or expository sentences inserted between, before, or after the declarative identity sentence and the imperative instruction.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The S-0 preamble gate (required for C-25) consists of exactly two sentences and no more: sentence 1 is the declarative identity assertion, sentence 2 is the imperative emit instruction. Any additional sentence of any type -- elaborative ("Its single obligation before advancing is..."), enforcement ("No other step may begin before this emission completes."), parenthetical, expository, or transitional -- inserted before, between, or after the required pair causes the gate to exceed the two-sentence form and fails this criterion. **C-27 is content-agnostic:** the count requirement is not waived by sentence utility or operational value. A third sentence that restates enforcement logic, names a prohibited action, or provides gate rationale still counts toward the gate sentence total and still fails C-27. The count-strict requirement is independent of the type-coverage requirement (C-25): a gate that contains all required sentence types but adds a third sentence passes C-25 on a type-coverage reading and fails C-27. The two-sentence count is not incidental -- the compact form ensures the gate cannot be misread as optional preamble; a three-sentence opening reads as a paragraph, and the imperative risks being lost as one of three. **Note (R7 discriminator):** C-25 passing is a necessary but not sufficient condition for C-27. V-03 (R7) demonstrates elaborative failure: "This step emits first. Its single obligation before advancing is to report TOPICS.md status. Write the TOPICS.md status line before any other work begins." V-03 (R8) demonstrates enforcement failure: "This step emits first. Write the TOPICS.md status line before any other work begins. No other step may begin before this emission completes." Both are three-sentence failures; the third sentence's utility is irrelevant. Source: R7 V-03 vs V-05; R8 V-03 content-agnostic confirmation.

### C-28
- **Text**: The declarative sentence in the two-sentence gate asserts the step's functional ROLE with the step as grammatical subject of its own emission action -- not an output-position assertion naming what the first output is.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The declarative identity sentence (required for C-25) must use the step as its grammatical subject asserting its defining function in the pipeline: "This step emits first," "S-0 is the emit step," or equivalent forms where the step is agent of its own role. A declarative sentence that instead positions an artifact in output sequence -- "The first observable output of this step is X," "The first thing written is X," "Output 1 is the TOPICS.md status line" -- does not satisfy this criterion regardless of sentence position or length. The distinction is functional: a step-role declaration specifies what the step IS in the pipeline architecture; an output-primacy declaration specifies what appears in position 1 of the output stream. An implementation satisfying a step-role declaration must model the step's structural purpose; an implementation satisfying an output-primacy declaration need only sequence artifacts correctly. The step-role form is the stronger constraint because step identity cannot be satisfied by output reordering alone. **Note (R7 discriminator):** C-25 passing is a necessary but not sufficient condition for C-28. V-04 (R7) demonstrates the output-primacy failure: "The first observable output of this step is the TOPICS.md status line." **Note (R8 discriminator):** C-28 passing does not imply C-29 passing -- a possessive-nominal subject ("This step's defining action is to emit first") may be judged to satisfy C-28's role-assertion language while failing C-29's nominative-subject test. C-28 passing does not imply C-30 passing -- an artifact-as-subject active construction ("The TOPICS.md status line is the first output of this step") is a third failure mode distinct from both output-primacy (C-28 canonical) and possessive-nominal (C-29). **Note (R9 discriminator):** A deontic declarative ("This step must emit first") fails C-28 because "must emit" is modal-obligation form -- the step is grammatical subject but does not assert its defining function in indicative form; C-28 requires the step as "agent of its own role" in indicative assertion, not as subject of a behavioral norm; deontic form simultaneously fails C-25 and C-31. Source: R7 V-04 vs V-05.

### C-29
- **Text**: The declarative sentence must have the step as direct nominative subject -- not a nominalization or abstraction derived from the step appearing in subject position while the step is demoted to a possessive/genitive modifier.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The declarative identity sentence (required for C-25, qualified by C-28) must have the step itself as the direct nominative head of the subject noun phrase. Possessive-nominal constructions fail this criterion: "This step's defining action is to emit first" -- here "defining action" is the grammatical subject and "This step" occupies a genitive modifier position; the sentence assigns the agent role to a nominalized abstraction rather than to the step. The test: substitute "It" for the subject noun phrase. If "It" refers to an abstraction derived from the step ("the defining action," "the step's function," "the role") rather than to the step itself, the step is not the grammatical subject. Any construction of the form "This step's [noun phrase] is [predicate]" fails regardless of how accurately the predicate captures the step's role. **Note (R8 permissive):** A compound predicate does not fail C-29 -- "This step emits first and resolves the tier variable" keeps the step as direct nominative subject with multiple predicates and satisfies C-28, C-29, and C-30 simultaneously. **Note (R8 discriminator):** C-28 passing is a necessary but not sufficient condition for C-29. V-02 (R8) demonstrates the possessive-nominal failure: "This step's defining action is to emit first" -- the intent is correct; the syntax demotes the step. Source: R8 V-02 vs V-04.

### C-30
- **Text**: The declarative sentence must not promote an output artifact to nominative subject position in active voice, even when the step appears in the predicate as a possessive modifier.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The declarative identity sentence (required for C-25, qualified by C-28 and C-29) must not place an output artifact as its grammatical subject. An artifact-as-subject active construction -- "The TOPICS.md status line is the first output of this step" -- fails this criterion: the artifact is nominative subject, and the step appears only as "of this step," an oblique possessive modifier in the predicate. This failure mode is distinct from C-28's output-sequence form ("The first observable output of this step is X," where an output-position abstraction is subject) and from C-29's possessive-nominal form (where a nominalization derived from the step is subject). In C-30, the artifact itself is directly in subject position. Together C-28, C-29, and C-30 enumerate the three tested declarative failure modes: output-sequence-subject, nominalization-subject, and artifact-subject. **Note (R8 permissive):** A compound predicate does not fail C-30 -- "This step emits first and resolves the tier variable" satisfies C-28, C-29, and C-30 simultaneously because the step is the direct nominative agent of all conjoined predicates. **Note (R8 discriminator):** C-28 and C-29 passing are necessary but not sufficient conditions for C-30. V-01 (R8) demonstrates the artifact-as-subject failure: "The TOPICS.md status line is the first output of this step" -- the semantic content describes the step's output correctly, but the artifact is the grammatical subject. Source: R8 V-01 vs V-04.

### C-31
- **Text**: The declarative sentence in the two-sentence gate must use indicative mood -- not deontic/modal-obligation form -- to assert the step's role.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The declarative identity sentence (required for C-25, qualified by C-28, C-29, C-30) must be in indicative present tense: "This step emits first," "S-0 is the emit step," "This step emits first and carries tier into S-2 and S-3." A sentence using a modal verb of obligation -- "must," "shall," "should," "is required to" -- is deontic: it prescribes a behavioral norm rather than asserting a structural fact about the step's role in the pipeline. Deontic form converts the sentence from a role-declaration ("the step IS the emitter") to a requirement-imposition ("the step MUST emit"), which changes its epistemic status from description to prescription. The test: replace the modal with simple present indicative -- if this transforms the sentence from a norm ("must emit" = "the step is required to emit") to a statement of fact ("emits" = "the step emits"), the original was deontic and fails. A deontic gate declarative fails C-31 and simultaneously fails C-25 (prescribes behavior, does not assert role) and C-28 (modal-obligation form is not indicative role-assertion); these three failures share a single cause. **Note (R9 discriminator):** The deontic failure is a compound-criterion failure -- one word ("must") triggers C-25, C-28, and C-31 simultaneously. The three criteria remain independent because C-25 tests sentence type (role-assertion vs. prescription), C-28 tests subject-predicate structure (step as agent in indicative form), and C-31 tests mood (indicative vs. deontic); all three properties must be satisfied, and a single modal word violates all three. Canonical passing forms: "This step emits first" (simple indicative); "S-0 is the emit step" (identity predicate); "This step emits first and carries tier into S-2 and S-3" (indicative compound predicate). V-02 (R9) demonstrates the deontic failure: "This step must emit first" -- the step is grammatical subject but the modal "must" makes the predicate a norm, not a fact; C-25, C-28, and C-31 all fail. Source: R9 V-02 vs V-01 and V-05.

### C-32
- **Text**: The C-18 tier-carry handoff and the C-20 standalone terminal sentence are structurally independent -- when C-18 is satisfied by the compound-predicate opening declarative, a separate standalone sentence in terminal position is still required for C-20; the two requirements cannot be collapsed into the gate opener.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: C-18 (any explicit handoff sentence naming tier and both consumers) and C-20 (standalone terminal sentence in closing position of S-0) are independent requirements. A compound-predicate opening declarative that encodes tier-carry -- e.g., "This step emits first and carries tier into S-2 and S-3" -- satisfies C-18 because C-18 has no position constraint. It does not satisfy C-20 because C-20 requires a standalone sentence in the terminal position of S-0, after the resolution bullets. The gate-opening declarative is structurally the gate opener, not the S-0 terminal; using it to carry tier collapses two independent obligations into one structural slot and loses the closing register required by C-20. The independence check: remove the tier-carry content from the opening declarative and ask whether a standalone terminal sentence still appears at the end of S-0. If no separate terminal sentence remains, C-32 fails. When C-20 fails because the standalone terminal sentence was removed, C-32 co-fails by the same structural choice; the two criteria test different properties -- C-20 tests register content (standalone sentence naming both consumers) and C-32 tests structural independence (C-18 and C-20 requirements expressed in two distinct sentences at two distinct positions). **Note (R9 discriminator):** C-18 passing is a necessary but not sufficient condition for C-32. V-03 and V-04 (R9) demonstrate the compound-opener failure: the opening declarative satisfies C-18 but the standalone terminal sentence was removed; C-20 and C-32 both fail from the same structural choice. V-01 and V-05 (R9) demonstrate the correct dual-register form: compound declarative in opening position satisfies C-18; standalone "Carry the resolved tier into S-2 and S-3 before any further action." in terminal position satisfies C-20 and C-32 independently. Source: R9 V-03 and V-04 vs V-01 and V-05.

---

## Common Failure Modes

| Failure | Criterion | Description |
|---------|-----------|-------------|
| EVIDENCE-HEAVY flagged as `none` | C-03 | listen-support or prove-interview assigned FLAG = `none` instead of `REAL-REQUIRED` |
| Generic body | C-05 | Artifact body uses paragraph prose with no skill-specific tables or verdict line |
| Skill-id in filename | C-07 | Path uses `{topic}-{skill-id}-mock-{date}.md` instead of `{topic}-{namespace}-mock-{date}.md` |
| Category/Flag mismatch | C-02 + C-03 | CATEGORY assigned correctly but FLAG computed for a different category |
| Missing fidelity warning | C-04 | Header present but no warning block before body content |
| Partial C-06 setup | C-06 | Generating emit present with tier field, but TOPICS.md status line absent. Half-credit is not granted -- C-06 requires both lines. |
| C-10 default-pass not modeled | C-10 | Predictors mark C-10 as fail when no compliance tags are present. The rubric grants a default pass in this case. The criterion only fires when compliance tags exist. |
| C-13 via meta-instruction only | C-13 | Error guard stated as meta-instruction rather than a literal template. Passes C-13 (content requirements met) but misses C-14 assembly-step standard. |
| Wildcard in footnote only | C-16 | `trace-*`, `listen-*` appear in an expansion note below the FLAG table but the condition cell reads "critical skill." Passes C-11 (enumeration present) but fails C-16 (must be in condition cell). |
| Gate language missing | C-17 | S-0 is correctly labeled and ordered (C-12 passes) but contains no sentence naming S-1 and forbidding early advancement. The step boundary is a labeling convention, not an enforcement mechanism. |
| Tier-carry implies propagation | C-18 | S-0 emits the tier value and S-2/S-3 reference it correctly, but no handoff sentence names S-2 and S-3 as consumers. Propagation works in practice but the contract is not inspectable. |
| CONSTRAINT step-prohibition loses op-type naming | C-15 | Rewriting CONSTRAINT to "Do not begin S-1, S-2, or S-3" satisfies C-17 (names S-1 by label) but fails C-15 (skill-selection op type not named by type). C-15 and C-17 require separate sentences. V-03 (R4) hit this trap. |
| Single-consumer carry | C-18 | "Carry into S-3" or similar with only 1 named consumer fails C-18, even when combined with a gate sentence. Must name at least 2 downstream steps. V-01 (R4) hit this trap. |
| C-11 awarded as C-22 | C-22 | FLAG table has 4 rows that functionally cover all 5 cases (C-11 passes) but no dedicated row separates HS-critical-tier=1 from the non-critical catch-all (C-22 fails). C-11 passing is necessary but not sufficient for C-22. V-02 (R5) confirmed this trap. |
| C-17 awarded as C-19 | C-19 | S-0 has a terminal gate naming S-1 (C-17 passes) but the preamble gate was removed (C-19 fails). Single gate satisfies C-17 but not C-19. V-03 (R5) confirmed this trap. |
| C-15 count satisfies C-21 | C-21 | CONSTRAINT names exactly 3 op types (C-15 minimum), but body generation is absent (C-21 fails). C-15 is necessary but not sufficient for C-21 -- op count is the discriminator. V-01 (R5) confirmed this trap. |
| CONSTRAINT before gate | C-23 | CONSTRAINT block appears as the first content of S-0 -- before the preamble gate sentence. Fails C-23 even when C-15/C-21/C-24 all pass and the preamble gate appears later. CONSTRAINT is defense-in-depth and must follow the gate; placing it first inverts the logical structure (defense before barrier). V-02 and V-04 (R6) confirmed this trap. |
| One-sentence gate satisfies C-23, misses C-25 | C-25 | A single imperative sentence at S-0 opening passes C-23 (zero pre-gate surface) but fails C-25 (requires declarative identity sentence preceding the imperative). The command is necessary but the identity declaration is also required. V-01 (R6) confirmed this boundary. |
| Canonical CONSTRAINT satisfies C-24, misses C-26 | C-26 | CONSTRAINT names 5 op types in canonical phrase form (satisfying C-24) but repeats the same vocabulary rather than paraphrasing each prohibition in synonym vocabulary (fails C-26). Canonical phrases demonstrate correct coverage; synonym forms demonstrate conceptual mastery. The two criteria are orthogonal. V-02 and V-03 (R6) confirmed this boundary. |
| Elaborative three-sentence gate | C-27 | A third sentence is inserted in the preamble gate -- e.g., "This step emits first. Its single obligation before advancing is to report TOPICS.md status. Write the TOPICS.md status line before any other work begins." C-27 is content-agnostic: an enforcement sentence ("No other step may begin before this emission completes.") also fails, even though it restates the gate logic. Both required sentence types may be present (C-25 type-coverage reading passes) but the count exceeds two (C-27 fails). V-03 (R7) confirmed elaborative failure; V-03 (R8) confirmed enforcement-sentence failure. |
| Output-primacy declarative | C-28 | Declarative sentence names the first output artifact rather than the step's role: "The first observable output of this step is the TOPICS.md status line." Grammatical subject is an output-position abstraction, not the step. C-25 structural requirements may appear satisfied but C-28 fails. V-04 (R7) confirmed this boundary. |
| Possessive-nominal declarative | C-29 | Declarative sentence demotes the step to genitive modifier: "This step's defining action is to emit first." Subject is a nominalization ("defining action"); "This step" is a possessive modifier. The predicate may correctly capture the step's role, but the step is not the grammatical subject. C-28 may be satisfied (no output-primacy or artifact-subject form) while C-29 fails. V-02 (R8) confirmed this boundary. |
| Artifact-as-subject active declarative | C-30 | Declarative sentence promotes an output artifact to nominative subject in active voice: "The TOPICS.md status line is the first output of this step." The artifact is subject; the step appears only as oblique modifier "of this step." Distinct from C-28's output-sequence form and from C-29's possessive-nominal form. C-28 and C-29 may be satisfied while C-30 fails. V-01 (R8) confirmed this boundary. |
| Deontic modal declarative | C-31 | Declarative sentence uses modal-obligation form: "This step must emit first." The modal "must" makes the sentence a behavioral prescription rather than a role-assertion, simultaneously failing C-25 (not a role-declaration), C-28 (modal predicate is not indicative role-assertion), and C-31 (deontic mood). One word ("must") triggers three criterion failures. The grammatical subject ("This step") is correct but the modal disqualifies the sentence from all three criteria. V-02 (R9) confirmed this boundary. |
| Compound-opener collapses tier-carry registers | C-32 | Compound-predicate opening declarative encodes tier-carry (C-18 satisfied) but the standalone terminal sentence is removed. C-20 fails (no standalone terminal statement) and C-32 fails (C-18 and C-20 requirements collapsed into one sentence at one position). The declarative is the gate opener, not the S-0 terminal; encoding tier-carry in the gate opener does not satisfy the closing-position register required by C-20. V-03 and V-04 (R9) confirmed this boundary. |
