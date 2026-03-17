content = r"""# mock-ns Rubric -- v7

## Changelog

### v7 (2026-03-16) -- R6 patterns promoted to aspirational criteria

**Two new criteria from R6:**

| ID | Text | Source |
|----|------|--------|
| C-25 | S-0 preamble gate uses two-sentence form: declarative identity assertion + imperative emit instruction | R6 V-05 two-layer gate signal |
| C-26 | CONSTRAINT vocabulary uses synonym forms for each prohibited op type, not canonical phrase repetition | R6 V-05 synonym-CONSTRAINT signal |

**Extracted patterns:**

- **C-25** (from V-05 vs V-01): Both V-01 and V-05 pass C-23 (gate as opening sentence, zero pre-gate surface). V-01 uses a single-sentence imperative: "Before any other step begins, emit the TOPICS.md status line below." V-05 uses a two-sentence form: "This step emits first. Write the TOPICS.md status line before any other work begins." The declarative identity sentence ("This step emits first") asserts the step's emit-primacy as a statement of ROLE, independently of the command. The imperative sentence provides the behavioral directive. The two-layer form eliminates the question of whether the emit is a conditional requirement or the step's defining function -- the declarative makes it definitional.

- **C-26** (from V-05 vs V-02/V-03): All three pass C-24 (5 ops including artifact write phase). V-02 and V-03 use canonical phrase forms: "No category lookup. No skill selection. No mock generation. No body generation. No artifact path construction or file write." V-05 uses synonym forms throughout: "No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. No artifact path assembly or file output." The synonym form demonstrates that each prohibition is understood by concept, not by phrase. A CONSTRAINT expressed in synonym vocabulary cannot be satisfied by exact-match phrase compliance -- it requires the model to recognize the prohibitions semantically.

**Two new failure traps** encoding R6 implication errors:
- "CONSTRAINT before gate" (V-02/V-04 pattern): CONSTRAINT-first inverts the logical structure; CONSTRAINT is defense-in-depth, not the primary barrier -- placing it first displaces the gate and fails C-23
- "One-sentence gate satisfies C-23, misses C-25" (V-01 boundary): single imperative at S-0 opening passes C-23 (zero pre-gate surface) but fails C-25 (requires declarative identity sentence preceding the imperative)

**Two new discriminator notes** added to C-23 and C-24 pass conditions:
- C-23: "C-23 passing does not imply C-25 passing" -- single-imperative form (V-01) satisfies C-23 but not C-25
- C-24: "C-24 passing does not imply C-26 passing" -- canonical 5-op CONSTRAINT (V-02/V-03) satisfies C-24 but not C-26

**Scoring**: max rises from 112 to **116** (18 aspirational x 2 pts = 36). V-05 (R6) scores 116/116; R6 boundary variates V-01/V-02/V-03 each score 110/116 (fail C-25 and C-26, -4 pts vs 112 ceiling); V-04 scores 108/116 (fails C-23, C-24, C-25, C-26).

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
| Aspirational | C-09--C-26 | 2 | 36 |
| **Total** | | | **116** |

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

*Raise the bar once essential and recommended are stable. Each criterion is worth 2 pts (18 x 2 = 36; max score = 116).*

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
- **Pass condition**: S-0 includes an explicit handoff sentence that (a) names the tier value as the carried artifact and (b) names at least two downstream steps by label that will consume it (e.g., "Carry the resolved tier into S-2 and S-3"). A prompt that carries the tier implicitly -- by having S-2 and S-3 reference tier without an explicit carry statement -- does not satisfy this criterion. A prompt that says "carry tier forward" without naming the consumers does not satisfy this criterion. Source: R3 V-02 and V-03.

### C-19
- **Text**: S-0 contains both a preamble gate and a terminal gate for the TOPICS.md emit requirement.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 contains two independent gate expressions addressing the same emit requirement: (1) a preamble gate, placed before the resolution bullets, in the form "Before any other step begins, emit the TOPICS.md status line" (or equivalent early-position sentence naming the emit as the first action); and (2) a terminal gate, placed after the resolution bullets, in the form "Do not begin S-1 until this line is emitted" (or equivalent closing enforcement sentence naming S-1). Both must be present. A step with only one gate form satisfies C-17 but not C-19. **Note (R5 discriminator):** C-17 pass does not imply C-19 pass. See C-23 for a further tightening of preamble gate position. Source: R4 V-05.

### C-20
- **Text**: Tier-carry appears in both a structured table downstream-use column and as a standalone terminal sentence.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The tier-carry contract is expressed in two independent registers: (1) within a structured parameter or resolution table, the tier row's downstream-use column explicitly states "Carry into S-2 and S-3" (or equivalent table cell naming both consumers); and (2) as a standalone terminal sentence in S-0 prose naming both consumers. Both must be present. A prompt with only a standalone sentence (satisfying C-18) or only a table column entry does not satisfy C-20. Source: R4 V-05.

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
- **Pass condition**: The S-0 preamble gate (required for C-23) consists of two sentences: (1) a declarative identity sentence asserting the step's emit primacy as a statement of the step's ROLE -- "This step emits first," "S-0 is the emit step," or equivalent present-tense declaration that names the step's defining function; and (2) an imperative instruction naming what must be emitted and when -- "Write the TOPICS.md status line before any other work begins," or equivalent command. Both sentences must be present at S-0 opening. A single-sentence imperative gate (satisfying C-23) does not satisfy this criterion -- it provides the command but not the identity declaration. The declarative sentence establishes that the emit is the step's definitional behavior, not merely a conditional precondition; the imperative sentence provides the operational directive. The two-layer form eliminates ambiguity about whether the gate is enforced vs. advisory by asserting the step's identity before issuing the command. **Note (R6 discriminator):** C-23 passing is a necessary but not sufficient condition for C-25. V-01 (R6) uses single-imperative form -- passes C-23, fails C-25. Source: R6 V-05 only -- "This step emits first. Write the TOPICS.md status line before any other work begins." contrasted with V-01 single-sentence "Before any other step begins, emit the TOPICS.md status line below."

### C-26
- **Text**: CONSTRAINT uses synonym vocabulary for each prohibited operation type, not canonical phrase repetition.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: Each prohibition in the CONSTRAINT block is expressed using vocabulary that is semantically equivalent to but lexically distinct from the canonical op-type label used elsewhere in the skill spec. All op-type prohibitions must use distinct vocabulary -- e.g., "No lookup of skill categories" instead of "No category lookup"; "No skill-id resolution" instead of "No skill selection"; "No mock content generation" instead of "No mock generation"; "No artifact body construction" instead of "No body generation"; "No artifact path assembly or file output" instead of "No artifact path construction or file write." A CONSTRAINT that repeats the canonical op-type phrases verbatim (satisfying C-15/C-21/C-24) does not satisfy this criterion. The synonym form demonstrates that each prohibition is understood at the concept level -- the spec author cannot rely on exact-match phrase enforcement and must understand what each phrase means to paraphrase it correctly. A CONSTRAINT with even one op-type in canonical phrase form does not satisfy this criterion; all op-type prohibitions must use distinct vocabulary. **Note (R6 discriminator):** C-24 passing (5-op CONSTRAINT) does not imply C-26 passing. V-02 and V-03 (R6) use canonical phrases throughout -- pass C-24, fail C-26. Source: R6 V-05 only -- sole variate to use synonym forms throughout all 5 prohibition phrases.

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
"""

with open(r"C:/src/sim/simulations/quest/rubrics/mock-ns-rubric-v7-2026-03-16.md", "w", encoding="utf-8") as f:
    f.write(content.lstrip())

print("Written successfully")
