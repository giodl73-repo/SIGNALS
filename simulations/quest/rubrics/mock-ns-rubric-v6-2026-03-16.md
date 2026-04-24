Written to `simulations/quest/rubrics/mock-ns-rubric-v6-2026-03-16.md`.

---

**v6 summary: 2 new criteria, 3 new failure traps**

| ID | Text | Source |
|----|------|--------|
| C-23 | Preamble gate is the opening sentence of S-0, preceding all resolution logic including the parameter table | R5 V-03 position signal |
| C-24 | CONSTRAINT names 5+ prohibited op types, adding artifact path construction or file write to the C-21 minimum | R5 V-01 phase-completeness signal |

**Extracted patterns:**

- **C-23** (from V-03): When only a terminal gate is present, a reader scanning S-0 top-to-bottom encounters resolution logic before any constraint. The fix is not just "put the preamble gate before the bullets" (C-19) but "make it the *opening sentence* with zero pre-gate surface area." C-19 allows an introductory sentence before the gate; C-23 does not.

- **C-24** (from V-01): A 4-op CONSTRAINT (passing C-21) still leaves the artifact-write phase uncovered. A model could defer lookup/selection/generation/body-gen but begin constructing the output path or writing the file before S-0 completes. The 5-op form closes this by naming path construction / file write as the fifth prohibited phase. This completes a full phase-ordered chain: discovery → decision → generation → content → output.

**Three new failure traps** encoding R5 implication errors:
- "C-11 awarded as C-22" (V-02): functional coverage ≠ structural row separation
- "C-17 awarded as C-19" (V-03): single gate ≠ dual gate
- "C-15 count satisfies C-21" (V-01): 3-op minimum ≠ 4-op requirement

**Scoring**: max rises from 108 to **112** (16 aspirational x 2 pts = 32). V-05 (R4) now scores 108/112; a R5-convergent variate scores 112/112. All three R5 boundary variates score 110/112 (lose 1 criterion each, −2 pts).

Also added R5 discriminator notes to C-11, C-15, C-17, C-19, C-21, and C-22 pass conditions, encoding "C-X passing does not imply C-Y passing" for each adjacent pair.
NSTRAINT-embedded sentence naming S-1 satisfies C-17; a CONSTRAINT naming only op-types without naming S-1 does not.

**Scoring**: max rises from 100 to **108** (14 aspirational x 2 pts = 28). This correctly separates V-04 (100/108) from V-05 (108/108) — previously tied. The two new failure traps ("CONSTRAINT step-prohibition loses op-type naming" and "Single-consumer carry") document the R4 V-03 and V-01 trap patterns respectively.
V-05 5-row FLAG table -- "explicit critical tier-1 row makes the case documented rather than collapsed" |

**C-17 clarified** -- R4 V-03 canary result encoded: C-17 is content-based, not form-based. A CONSTRAINT-embedded sentence that names S-1 and makes the TOPICS.md emit a hard precondition satisfies C-17 just as a standalone terminal sentence does. What fails C-17 is a CONSTRAINT that names only operation types without referencing S-1 by label. V-03 swapped a C-15 pass for a C-17 pass by rewriting the CONSTRAINT -- the two criteria require separate sentences to satisfy both simultaneously.

**Scoring update**: With 22 criteria total -- 5 essential (50) + 3 recommended (30) + 14 aspirational (28, at 2 pts each) -- max score increases to **108**. V-04 (minimal 100 under v4) now scores 100/108; V-05 (convergent) now scores 108/108. The increase correctly differentiates what were previously tied perfect scores.

**Two new failure traps** added: "CONSTRAINT step-prohibition loses op-type naming" (passes C-17 by naming S-1 in CONSTRAINT, but fails C-15 because op-type names are replaced with step names) and "Single-consumer carry" (fails C-18 because only one downstream step is named, even when combined with a gate sentence).

---

### v4 (2026-03-16) -- R3 patterns promoted to aspirational criteria

**Two new criteria from R3:**

| ID | Source | What it captures |
|----|--------|-----------------|
| C-17 | V-03 C-12 evidence | S-0 advancement gate sentence -- names S-1 and makes the TOPICS.md emit line a hard precondition. Distinguishes enforced ordering from labeled ordering. A C-12-passing skill can still fail C-17. |
| C-18 | V-02 + V-03 C-12 evidence | S-0 tier-carry handoff names S-2 and S-3 as consumers. Distinguishes documented propagation from implied propagation. A C-12-passing skill can still fail C-18. |

**Scoring update**: aspirational drops from 2.5 to 2 pts each (10 x 2 = 20; max remains 100).

**Two new failure traps** added: "Gate language missing" (passes C-12, fails C-17) and "Tier-carry implies propagation" (passes C-12, fails C-18).

---

### v3 (2026-03-16) -- R2 patterns promoted to aspirational criteria

**Three new aspirational criteria** (C-14, C-15, C-16) extracted from R2 V-05 excellence signals:

| ID | Text | Source signal |
|----|------|---------------|
| C-14 | Assembly expressed as discrete named steps A-1 through A-5 | "separated assembly steps make each output responsibility a discrete verifiable unit" |
| C-15 | CONSTRAINT block names prohibited S-0 operations by type (no category lookup, no skill selection, no mock generation) | "CONSTRAINT keyword names prohibited operations by type, not just by ordering" |
| C-16 | Wildcard patterns `trace-*`, `listen-*` appear in the FLAG table condition column cell, not only in footnotes | "wildcard notation in FLAG table condition column -- directly in the case match cell" |

**C-12 clarified** -- R2 canary result encoded: step-labeled separation satisfies C-12; CONSTRAINT block (C-15) is defense-in-depth only and does not move the C-12 score.

**C-13 clarified** -- meta-instruction format satisfies C-13; R2 Pattern 2 result encoded in the pass condition.

**Two new failure traps** added: "C-13 via meta-instruction only" (passes C-13, misses C-14) and "Wildcard in footnote only" (passes C-11, fails C-16).

---

### v2 (2026-03-16) -- R1 patterns promoted to aspirational criteria

**C-05 strengthened** -- pass condition now explicitly says "without reading the header."

**C-06 tightened** -- ordering requirement called out (TOPICS.md line first); half-credit not granted.

**C-10 clarified** -- bold statement that no compliance tags = default pass.

**Three new aspirational criteria from R1:**

| ID | Text | Source |
|----|------|--------|
| C-11 | FLAG rule names critical namespaces explicitly (`trace-*`, `scout-feasibility`, `listen-*`) and covers all 5 cases | R1 Pattern 2 -- tier-conditional completeness |
| C-12 | S-0 TOPICS.md step resolves tier before S-1 skill selection begins | R1 Pattern 1 -- S-0 as structural anchor |
| C-13 | Category lookup halts with error on unrecognized skill-id | R1 V-05 only -- error-stop on unknown skill |

---

### v1 (2026-03-16) -- initial rubric

Baseline from first golden construction.

---

## Scoring

| Weight | Criteria | Points each | Max |
|--------|----------|-------------|-----|
| Essential | C-01--C-05 | 10 | 50 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-24 | 2 | 32 |
| **Total** | | | **112** |

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

*Raise the bar once essential and recommended are stable. Each criterion is worth 2 pts (16 x 2 = 32; max score = 112).*

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
- **Pass condition**: The FLAG computation is expressed as a complete table or enumerated case list covering all 5 category/tier/skill-condition combinations: (1) HIGH-STRUCTURE non-critical any tier, (2) HIGH-STRUCTURE critical tier 1, (3) HIGH-STRUCTURE critical tier >= 2, (4) EVIDENCE-HEAVY, (5) MIXED. Critical namespaces are named explicitly as `trace-*`, `scout-feasibility`, and `listen-*` -- a generic description like "critical skills" without enumeration is not sufficient. This goes beyond C-03 (which only checks the output flag value) to the completeness of the rule that produces it. Cases 1 and 2 may be collapsed into a single row when they share the same flag value; completeness is functional, not structural. **Note (R5 discriminator):** C-11 passing (functional 5-case coverage) does not imply C-22 passing (structural row separation). A 4-row table that collapses HS-critical-tier=1 into the non-critical catch-all satisfies C-11 but fails C-22. Source: R1 Pattern 2 -- tier-conditional completeness in V-03/V-04/V-05 required explicit name enumeration to fire correctly.

### C-12
- **Text**: TOPICS.md step resolves tier before skill selection begins.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The S-0 TOPICS.md step completes -- emitting the status line with tier -- before the S-1 skill selection step begins. This ordering is what allows the tier value to propagate into the tier-conditional FLAG rule in S-3. A prompt that reads TOPICS.md and emits the status line but within the same step as skill selection (rather than prior to it) does not satisfy this criterion. **Note (R2 canary):** Step-labeled separation with an explicit "carry tier into S-2 and S-3" handoff sentence satisfies this criterion -- a CONSTRAINT block is not required. The CONSTRAINT block (C-15) adds adversarial robustness but does not move the C-12 score. **Note (R3 discriminator):** C-17 (gate sentence) and C-18 (named consumers) further strengthen C-12-passing implementations but are not required for C-12 itself. Source: R1 Pattern 1 -- S-0 as structural anchor that enables tier-conditional firing.

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
- **Pass condition**: A labeled CONSTRAINT section (or equivalent explicit prohibition block) appears at or within the S-0 step definition and names at minimum three prohibited operation types: no category lookup, no skill selection, no mock generation. The prohibition must name the operation types, not merely restate the ordering rule. A prompt that only says "complete S-0 before S-1" without naming what is prohibited does not satisfy this criterion. **Note (R4 trap):** A CONSTRAINT rewritten to name steps ("Do not begin S-1, S-2, or S-3") rather than operation types loses C-15 even when C-17 is gained -- naming S-1 in the CONSTRAINT satisfies C-17 but the op-type requirement of C-15 is unmet. The two criteria require separate sentences to satisfy both simultaneously. **Note (R5 discriminator):** C-15 passing (3 op types named) does not imply C-21 passing (4 op types including body generation). C-15 is a necessary but not sufficient precondition for C-21. Source: R2 V-05 excellence signal -- "CONSTRAINT keyword as explicit step gate names prohibited operations by type, not just by ordering."

### C-16
- **Text**: Wildcard patterns for critical namespaces appear directly in the FLAG table condition column.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: In the FLAG computation table, the condition cell for the critical HIGH-STRUCTURE case contains the wildcard patterns `trace-*` and `listen-*` directly in the match expression (e.g., "HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-*"). Listing `trace-*` and `listen-*` only in a footnote or expansion block below the table -- while the condition cell reads "critical skill" or similar -- does not satisfy this criterion. C-11 requires enumeration somewhere in the rule; C-16 requires that enumeration to appear in the condition column cell itself. Source: R2 V-05 excellence signal -- "wildcard notation in FLAG table condition column -- `trace-*`, `listen-*` appear directly in the case match cell, not only in the expansion footnote."

### C-17
- **Text**: S-0 contains an explicit advancement gate sentence that names S-1 and prohibits proceeding before the TOPICS.md emit line is produced.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: Within the S-0 step body, a sentence explicitly names S-1 (or equivalent next step) and states that it must not begin until the TOPICS.md status line has been emitted. Equivalent forms: "Do not begin S-1 until this line is emitted," "Before any other step begins, emit the TOPICS.md status line," or any phrasing that names the prohibited next step and makes the emit line a required precondition. A step that is correctly labeled and ordered (satisfying C-12) but contains no such gate sentence does not satisfy this criterion. The gate sentence converts a labeling convention into an enforcement mechanism. **Note (R4 V-03 confirmation):** C-17 is content-based, not form-based. A CONSTRAINT-embedded sentence that names S-1 and makes the TOPICS.md emit a hard precondition satisfies C-17 just as a standalone terminal sentence does -- the CONSTRAINT block is within the S-0 step body. What fails C-17 is a CONSTRAINT that names only operation types without referencing S-1 by label (V-02 form). **Note (R5 discriminator):** C-17 passing (terminal gate names S-1) does not imply C-19 passing (dual-gate form). A terminal-gate-only skill satisfies C-17 but fails C-19 because the reader encounters resolution logic before any gate language. Source: R3 V-03 C-12 evidence -- "S-0 has 'Before any other step begins... Do not begin S-1 until this line is emitted'" was the distinguishing factor between labeled ordering and enforced ordering.

### C-18
- **Text**: S-0 tier-carry handoff sentence names the downstream consuming steps by label.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 includes an explicit handoff sentence that (a) names the tier value as the carried artifact and (b) names at least two downstream steps by label that will consume it (e.g., "Carry the resolved tier into S-2 and S-3"). A prompt that carries the tier implicitly -- by having S-2 and S-3 reference tier without an explicit carry statement -- does not satisfy this criterion. A prompt that says "carry tier forward" without naming the consumers does not satisfy this criterion. The named-consumer form makes the propagation contract explicit and verifiable by inspection. Source: R3 V-02 and V-03 C-12 evidence -- "'Carry the resolved tier into S-2 and S-3' handoff present before S-1 begins" appeared in both high-scoring variates and is absent from variates that satisfy C-12 minimally.

### C-19
- **Text**: S-0 contains both a preamble gate and a terminal gate for the TOPICS.md emit requirement.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: S-0 contains two independent gate expressions addressing the same emit requirement: (1) a preamble gate, placed before the resolution bullets, in the form "Before any other step begins, emit the TOPICS.md status line" (or equivalent early-position sentence naming the emit as the first action); and (2) a terminal gate, placed after the resolution bullets, in the form "Do not begin S-1 until this line is emitted" (or equivalent closing enforcement sentence naming S-1). Both must be present. A step with only one gate form satisfies C-17 but not C-19. Belt-and-suspenders coverage eliminates scorer ambiguity by stating the constraint at both the entry and exit of the step. **Note (R5 discriminator):** C-17 pass does not imply C-19 pass. See C-23 for a further tightening of preamble gate position. Source: R4 V-05 excellence signal -- dual-gate form covers both C-17 equivalents simultaneously.

### C-20
- **Text**: Tier-carry appears in both a structured table downstream-use column and as a standalone terminal sentence.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The tier-carry contract is expressed in two independent registers: (1) within a structured parameter or resolution table, the tier row's downstream-use column explicitly states "Carry into S-2 and S-3" (or equivalent table cell naming both consumers); and (2) as a standalone terminal sentence in S-0 prose, "Carry the resolved tier into S-2 and S-3" (or equivalent naming both consumers). Both must be present. A prompt with only a standalone sentence (satisfying C-18) or only a table column entry does not satisfy C-20. The dual-register form makes the propagation contract visible in both structured and prose scanning. Source: R4 V-05 excellence signal -- "named-consumer carry in the downstream-use table column AND as standalone terminal sentence -- redundant C-18 coverage."

### C-21
- **Text**: CONSTRAINT block names 4 or more prohibited operation types, including body generation.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The CONSTRAINT block (required for C-15) names at minimum 4 prohibited operation types: no category lookup, no skill selection, no mock generation, and no body generation. The C-15 minimum of 3 types is necessary but not sufficient. Body generation must be named explicitly as a fourth prohibited type. A CONSTRAINT with only the C-15 minimum 3 does not satisfy this criterion. This closes an adversarial gap where a model might defer category and skill selection but begin generating artifact body content before S-0 is complete. **Note (R5 discriminator):** C-15 passing (3 op types) does not imply C-21 passing (4 op types). See C-24 for an extension requiring a 5th op type (artifact write phase). Source: R4 V-05 excellence signal -- "4-op CONSTRAINT (adding body generation) tightens adversarial robustness beyond the 3-op minimum."

### C-22
- **Text**: FLAG table separates HIGH-STRUCTURE critical tier=1 from HIGH-STRUCTURE non-critical as distinct rows.
- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Pass condition**: The FLAG computation table contains a dedicated row for HIGH-STRUCTURE critical skills at tier=1 (flag: none) and a separate row for HIGH-STRUCTURE non-critical skills (flag: none), even though both rows produce the same flag value. The explicit separation makes the tier-1 critical case a documented state rather than a collapsed one. C-11 passes when cases 1 and 2 are functionally covered (even collapsed); C-22 requires explicit row separation. The tier-1 critical row must name the critical namespaces in its condition cell (consistent with C-16). **Note (R5 confirmation):** A 4-row FLAG table that absorbs HS-critical-tier=1 into the non-critical catch-all satisfies C-11 (functional coverage) but fails C-22 (structural separation). C-11 passing is a necessary but not sufficient condition for C-22. Source: R4 V-05 excellence signal -- "5-row FLAG table separates HS critical tier-1 from non-critical explicitly."

### C-23
- **Text**: Preamble gate is the opening sentence of S-0, preceding all resolution logic including the parameter table.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The preamble gate sentence (required for C-19) appears as the absolute first sentence in the S-0 step body -- before any resolution bullets, parameter rows, or introductory prose. A preamble gate that appears after one or more lines of context-setting or introductory text does not satisfy this criterion, even if it precedes the resolution table (satisfying C-19). The distinction: C-19 requires the preamble gate to be before the resolution bullets; C-23 requires it to be the first content of the step with no pre-gate surface area. A reader or model scanning S-0 top-to-bottom must encounter the constraint before any logic framing. A prompt with a one-sentence introduction followed by the preamble gate satisfies C-19 but fails C-23. Source: R5 V-03 canary -- when the preamble gate is absent, "a reader scanning S-0 encounters the resolution table before any gate language." The natural defense is to make the preamble gate the opening content of the step, eliminating all pre-gate surface area.

### C-24
- **Text**: CONSTRAINT names 5 or more prohibited operation types, adding artifact path construction or file write to the C-21 minimum.
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Pass condition**: The CONSTRAINT block (required for C-15; extended by C-21 to 4 types) names at minimum 5 prohibited operation types, where the fifth closes the artifact-write phase: no artifact path construction, no artifact file write, or equivalent language prohibiting any A-4 WRITE phase activity during S-0. The C-21 minimum of 4 ops (lookup, selection, mock generation, body generation) is necessary but not sufficient. A complete adversarial-coverage CONSTRAINT must close all production phases in sequence: discovery (lookup), decision (selection), output generation (mock generation), content production (body generation), and artifact output (path construction / file write). A CONSTRAINT with only the C-21 minimum 4 does not satisfy this criterion. Source: R5 V-01 boundary -- a 4-op CONSTRAINT (passing C-21) still leaves an adversarial path where artifact path construction or file writing begins before S-0 completes. The 5-op form closes this final phase gap by prohibiting all phases of artifact production, not only the generation phases.


---

## Common Failure Modes

| Failure | Criterion | Description |
|---------|-----------|-------------|
| EVIDENCE-HEAVY flagged as `none` | C-03 | listen-support or prove-interview assigned FLAG = `none` instead of `REAL-REQUIRED` |
| Generic body | C-05 | Artifact body uses paragraph prose with no skill-specific tables or verdict line |
| Skill-id in filename | C-07 | Path uses `{topic}-{skill-id}-mock-{date}.md` instead of `{topic}-{namespace}-mock-{date}.md` |
| Category/Flag mismatch | C-02 + C-03 | CATEGORY assigned correctly but FLAG computed for a different category |
| Missing fidelity warning | C-04 | Header present but no warning block before body content |
| Partial C-06 setup | C-06 | Generating emit present with tier field, but TOPICS.md status line absent. Half-credit is not granted -- C-06 requires both lines. V-02 (R1) hit this trap: scored 90 instead of 100. |
| C-10 default-pass not modeled | C-10 | Predictors mark C-10 as fail when no compliance tags are present. The rubric grants a default pass in this case. The criterion only fires when compliance tags exist. |
| C-13 via meta-instruction only | C-13 | Error guard stated as meta-instruction rather than a literal template with `{skill-id}` placeholder. Passes C-13 (content requirements met) but misses C-14's assembly-step standard. |
| Wildcard in footnote only | C-16 | `trace-*`, `listen-*` appear in an expansion note below the FLAG table but the condition cell reads "critical skill." Passes C-11 (enumeration present) but fails C-16 (must be in condition cell). |
| Gate language missing | C-17 | S-0 is correctly labeled and ordered (C-12 passes) but contains no sentence naming S-1 and forbidding early advancement. The step boundary is a labeling convention, not an enforcement mechanism. |
| Tier-carry implies propagation | C-18 | S-0 emits the tier value and S-2/S-3 reference it correctly, but no handoff sentence names S-2 and S-3 as consumers. Propagation works in practice but the contract is not inspectable. |
| CONSTRAINT step-prohibition loses op-type naming | C-15 | Rewriting CONSTRAINT to "Do not begin S-1, S-2, or S-3" satisfies C-17 (names S-1 by label, enforces emit gate) but fails C-15 (skill-selection op type not named by type). Cannot substitute step names for operation types -- C-15 and C-17 require separate sentences to satisfy both simultaneously. V-03 (R4) hit this trap: swapped a C-15 pass for a C-17 pass, net score unchanged. |
| Single-consumer carry | C-18 | "Carry into S-3" or similar with only 1 named consumer fails C-18, even when combined with a gate sentence. Must name at least 2 downstream steps. V-01 (R4) hit this trap: C-17 pass + C-18 fail = 98/108. |
| C-11 awarded as C-22 | C-22 | FLAG table has 4 rows that functionally cover all 5 cases (C-11 passes) but no dedicated row separates HS-critical-tier=1 from the non-critical catch-all (C-22 fails). C-11 functional coverage is a necessary but not sufficient condition for C-22 structural row separation. Scorer who reads C-11 as sufficient proof of C-22 makes an implication error. V-02 (R5) confirmed this trap: 4-row table with wildcard-in-cell passes C-11 and C-16 but fails C-22. |
| C-17 awarded as C-19 | C-19 | S-0 has a terminal gate naming S-1 (C-17 passes) but the preamble gate at entry position was removed (C-19 fails). Scorer who reads C-17 as sufficient for C-19 makes an implication error -- a single gate form satisfies C-17 but not C-19. The reader scanning S-0 top-to-bottom still encounters the resolution table before any gate language. V-03 (R5) confirmed this trap. |
| C-15 count satisfies C-21 | C-21 | CONSTRAINT names exactly 3 op types satisfying the C-15 minimum (lookup, selection, mock generation), but body generation is absent (C-21 fails). C-15 is a necessary but not sufficient precondition for C-21 -- op count is the discriminator. V-01 (R5) confirmed this trap: C-15 pass + C-21 fail = 106/112. |
