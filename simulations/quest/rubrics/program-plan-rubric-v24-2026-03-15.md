---
skill: quest-rubric
skill_target: program-plan
date: 2026-03-15
version: 24
---

# Rubric: program-plan

**Skill**: `/program:plan`
**What it does**: Sequences Signal plugin skills into a staged program plan with named stages, ordered skills, gate conditions, and topic tracking. Produces `program.yaml`. Final stage is always `echo` (auto, no skills). Program is a plan, not an executor.

---

## Scoring Formula

```
composite = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 pts total — 4 criteria, 15 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Valid YAML structure** — Output is parseable YAML with a top-level `program` or `stages` key. Each stage is a mapping with `name`, `skills`, and `gate` fields present. | format | YAML parses without error; every stage has all three required fields |
| C-02 | **Echo final stage contract** — The last stage is named `echo`, has an empty skills list, and is marked `auto: true`. No stage appears after echo; no other stage is named echo. | correctness | Last stage: `name: echo`, `skills: []`, `auto: true`; no stages follow it |
| C-03 | **All skills are valid Signal namespaces** — Every skill named in any stage belongs to Signal's 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic). No invented, misspelled, or out-of-namespace skill names. | correctness | Zero skills outside Signal's 9 namespaces; no hallucinated names |
| C-04 | **Non-echo gates are non-trivial** — Every stage except echo has a `gate` field expressing a real evidence condition — not `"done"`, `"complete"`, empty string, or missing. Gate states what signals or artifacts must exist before advancing. | correctness | Every non-echo gate references a named artifact type, signal, or measurable condition |

---

## Recommended Criteria (30 pts total — 3 criteria, 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Skills ordered by namespace dependency** — Scout-namespace skills appear before draft; draft before review/prove; review/prove before topic. The sequence does not require artifacts that no prior stage has produced. | depth | No stage's skills depend on artifacts that a later stage produces; scout precedes draft precedes review/prove |
| C-06 | **Stage names are descriptive phase labels** — Stage names are human-readable phase labels (e.g., `discovery`, `validation`, `synthesis`) — not generic (`stage1`, `step2`) and not skill names reused as stage labels. | format | All stage names (except `echo`) are meaningful phase labels communicating work intent |
| C-07 | **Plan-not-executor framing explicit** — Output includes a note (YAML comment or preamble) stating the program is a plan, not an executor. Skills remain independently runnable; the program is optional scaffolding. | behavior | Explicit statement (comment or prose) that skills run standalone and the program does not auto-execute them |

---

## Aspirational Criteria (10 pts total — 20 criteria, 0.50 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Evidence arc is deliberate** — Stages form a coherent investigation strategy: early stages produce breadth signals (scout/draft), middle stages produce depth signals (prove/review/trace), late stages synthesize (topic/listen). Not merely a namespace alphabetical sort. | depth | At least 3 distinct phases identifiable (breadth → depth → synthesis) across non-echo stages |
| C-09 | **At least one gate is quantified** — At least one non-echo gate specifies a numeric threshold or minimum signal count (e.g., `">=2 scout signals and draft-spec present"`). Quantified gates are machine-checkable in principle and signal deliberate design. | behavior | One or more non-echo gates contain a numeric threshold or count expression |
| C-10 | **Inertia contrast present** — Output shows a BAD ad-hoc plan (or BAD gate examples) before or alongside the GOOD gated plan, making the purpose of each gate concrete rather than abstract. The contrast does not need to be a full plan — a bad-vs-good gate pair suffices. | pedagogy | At least one explicit BAD/GOOD contrast is present, labeled or clearly implied; the contrast is gate-specific, not generic advice |
| C-11 | **Self-verification checklist included** — Output provides a binary checklist the model (or user) uses to audit the plan before finalizing: each item is a yes/no question corresponding to a hard requirement (echo last, skills valid, gates non-trivial, etc.). | behavior | A checklist of >= 4 binary items is present; each item maps to a verifiable property of the output, not a process step |
| C-12 | **Not-executor as opening identity** — The plan-not-executor concept is introduced as the skill's opening framing — defining *why the skill exists* — not buried as a footnote, rule, or comment. The first substantive prose or preamble establishes this identity before any structural instructions. | behavior | "Not an executor" (or equivalent framing) appears in the first paragraph or top-of-file preamble; not exclusively in a rule list, comment, or footer |
| C-13 | **Template-locked verification** — The self-verification checklist is pre-printed in the required output template (not merely instructed as something the model should add), making omission require active deviation from the scaffold. The template contains the `## Plan Verification` section with empty checkboxes or fill-in placeholders. | behavior | Checklist is part of a pre-printed output template section the model is told to reproduce verbatim or with checkboxes checked; omitting it requires overriding the template. Distinct from C-11: C-11 passes if the checklist is present anywhere; C-13 requires it to be structurally pre-printed. |
| C-14 | **Arc structure scaffolded in template** — The evidence arc's layer divisions are labeled as named section comments within the YAML template body (e.g., `# ---- Layer 1: Breadth ----`), so the arc is architecturally embedded rather than described only in instructional prose. A model filling in the template inherits the arc without reconstructing it from rules. | depth | At least 2 named layer or phase dividers appear as YAML comments inside the pre-printed template structure, separating stages by arc role (breadth, depth, synthesis, or equivalent). Distinct from C-08: C-08 passes if 3 phases are identifiable; C-14 requires the phases to be structurally labeled inside the template YAML. |
| C-15 | **Not-executor dual-site anchoring** — Plan-not-executor framing is anchored in two distinct locations: (1) opening prose (satisfying C-12) AND (2) a required preserve-comment inside the YAML template (e.g., `# REQUIRED: preserve this comment — this program is a plan, not an executor`). Belt-and-suspenders coverage prevents accidental omission from either site. | behavior | Not-executor framing present in both opening prose and a labeled preserve-required YAML comment within the template; neither site alone satisfies C-15. Depends on C-12 passing (opening prose already established). |
| C-16 | **Contrast-grounded identity** — The not-executor claim is established *through* the opening BAD/GOOD contrast rather than asserted cold. The BAD example opens the output, demonstrates what the skill exists to replace, and the not-executor identity emerges as the conclusion of that contrast (e.g., "**`/program:plan` exists to replace this pattern.**"), rather than being stated as a standalone first-person assertion. | pedagogy | Opening sequence is: BAD example → diagnosis of what's wrong → "this is what this skill exists to replace" as identity-via-contrast. Both C-10 and C-12 must pass. Distinct from each: C-10 = contrast present anywhere; C-12 = not-executor as opening; C-16 = contrast IS the opening identity mechanism. |
| C-17 | **Explicit dependency narration** — The output includes at least one prose sentence that explicitly names a cross-stage artifact dependency — narrating WHY stages are ordered the way they are, not just structurally ordering them. (e.g., "Layer 1 produces scout signals that Layer 2's review and prove stages require before they can run.") | depth | At least one prose statement explicitly names an artifact or signal produced by an earlier stage that a later stage depends on; structural ordering alone does not pass; the causal link must be stated in prose. |
| C-18 | **YAML-embedded dependency map** — The layer divider comments inside the YAML template body include inline artifact-flow sub-labels annotating what each layer produces and what the next layer requires (e.g., `# ---- Layer 2: Depth ---- | draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*`). The dependency map is embedded structurally in the template scaffold rather than stated only in prose or external tables. | depth | At least one layer divider comment inside the template YAML explicitly annotates artifact producers and consumers in a structured inline notation; layer labels alone (C-14) do not pass C-18; prose narration alone (C-17) does not pass C-18. |
| C-19 | **Pre-template reference tables** — The output includes at least two structured reference tables appearing before the YAML template body: one covering the evidence arc (phases, namespaces, arc role) and at least one additional table covering gate design principles, gate BAD/GOOD examples, or skill catalog by namespace. The tables make arc logic, gate design, and skill inventory scannable without reading the template. | pedagogy | At least 2 distinct reference tables present before the template YAML; each table covers a different structural concern (arc, gates, or skills); a single combined table does not pass. Distinct from C-08 (arc phases identifiable in any form) and C-14 (arc labeled inside template YAML): C-19 requires tabular format and pre-template placement. |
| C-20 | **Per-layer arc narration** — The output dedicates a prose paragraph to each arc layer (Layer 1/Breadth, Layer 2/Depth, Layer 3/Synthesis or equivalent phases), narrating what that layer produces, what it requires from prior layers, and what it unlocks for the next. A single sentence naming a dependency (C-17 minimum) does not pass; three paragraph-level narrations are required. | depth | At least 3 layer-specific prose paragraphs present, each addressing a distinct arc layer's artifact scope and handoff role; a combined summary paragraph does not pass even if it names all three layers; C-17 must also pass. |
| C-21 | **Echo stage narrated in prose** — The echo stage's architectural role (auto-closing synthesizer, no new evidence skills, `auto: true` contract) is explained in a dedicated prose paragraph before the YAML template, making echo's purpose legible to a reader of the skill definition rather than only to a reader of the YAML. C-02 (echo present in YAML) does not pass C-21; prose explanation of echo's role is required. | depth | At least one prose paragraph (before the template) explains why echo is auto, why it carries no skills, and how it closes the evidence arc; a parenthetical or inline mention does not pass. |
| C-22 | **BAD/GOOD gate contrast as reference table** — The BAD/GOOD contrast (satisfying C-10) takes the specific form of a structured reference table with BAD and GOOD columns, presenting gate examples as rows. A labeled example pair in prose, a block-quote comparison, or a bullet list before/after does not pass; the columns must be a table's structural columns. | pedagogy | A reference table with BAD and GOOD (or equivalent) columns for gate examples is present before the template; C-10 must also pass. Distinct from C-10: C-10 passes with any contrast in any form; C-22 requires tabular column structure specifically. Distinct from C-19: C-19 counts any 2 pre-template tables; a gate table without BAD/GOOD columns passes C-19 but not C-22; a BAD/GOOD gate table counts toward C-19's table count. |
| C-23 | **Tabular skill catalog** — The skill catalog (skills by namespace) is rendered as a structured reference table with at minimum a namespace column and skill column (or equivalent structured columns), making it parallel in format to the evidence arc and gate design tables. A bullet list or prose enumeration of skills does not pass regardless of how complete it is. | pedagogy | A table presenting skills organized by namespace is present before the template YAML; bullet or prose enumeration does not substitute; C-19 does not require this specifically — C-23 is satisfied independently of whether C-19 passes. |
| C-24 | **Layer paragraph headers** — Each per-layer arc narration paragraph (required by C-20) begins with an explicit bold or formatted header that names both the layer (by number, name, or both) and its structural role in the arc (e.g., "**Layer 2 (Depth) — artifact scope and handoff contract:**"). Paragraphs without headers, or headers naming only the layer without a role description, do not pass. | depth | All three layer narration paragraphs open with an explicit labeled header stating layer identity and arc role; C-20 must pass. Distinct from C-20: C-20 requires three layer paragraphs; C-24 requires each to open with a role-labeled header — paragraphs satisfying C-20 in plain prose without headers do not pass C-24. |
| C-25 | **Echo paragraph enumerated** — The echo stage prose explanation (required by C-21) organizes its structural points as explicitly numbered sub-items (at minimum three, corresponding to: skill-free contract rationale, `auto: true` semantics, and arc closure function), making each architectural claim individually citable rather than embedded in flowing prose. | depth | Echo paragraph contains numbered or labeled sub-items covering all three required topics; a prose-only paragraph satisfying C-21 without enumeration does not pass; C-21 must pass. Distinct from C-21: C-21 requires a dedicated paragraph; C-25 requires that paragraph to use enumerated structural points. |
| C-26 | **Layer header cross-layer dependency reference** — At least one per-layer arc narration header (required by C-24) explicitly names an adjacent layer by number or identity within its role descriptor, creating a visible cross-layer dependency pointer in the header text itself. The canonical form is naming the receiving or providing layer: "produces the foundational signals **Layer 2** requires" names Layer 2 as the artifact recipient. A role descriptor that describes the layer's own function ("handles validation", "evidence breadth phase") without naming an adjacent layer does not pass. | depth | At least one of the three layer narration headers names an adjacent layer by number or identity in a dependency flow statement; C-24 must pass. Distinct from C-24: C-24 requires all three headers to have arc role descriptors; C-26 requires at least one of those descriptors to name a specific adjacent layer — a header with a generic role label passes C-24 but not C-26. |
| C-27 | **Terminal layer header states context dependency** — The Layer 3 / Synthesis arc narration header (required by C-24) explicitly includes a dependency statement for the synthesis layer — not merely labeling it "synthesis" or "final phase" but stating what prior context it requires (e.g., "requires the full validated context" or "requires review-validated artifacts from prior layers"). A terminal layer header that only names the phase function without stating what it depends on does not pass. | depth | The Layer 3 (or equivalent terminal layer) narration header contains a dependency statement indicating that this layer requires prior validated context; C-24 must pass. Distinct from C-26: C-26 requires at least one header to name an adjacent layer by number; C-27 requires specifically the terminal layer to include a dependency statement — it passes C-27 even if it does not name the source layer by number, and it passes C-26 only if it additionally names "Layer 2" or equivalent. |

---

## Score Card

```
C-01 valid YAML structure:              PASS / FAIL
C-02 echo final stage contract:         PASS / FAIL
C-03 valid Signal skill names:          PASS / FAIL
C-04 non-trivial gates:                 PASS / FAIL

C-05 namespace dependency order:        PASS / FAIL
C-06 descriptive stage names:           PASS / FAIL
C-07 plan-not-executor framing:         PASS / FAIL

C-08 deliberate evidence arc:           PASS / FAIL
C-09 quantified gate:                   PASS / FAIL
C-10 inertia contrast:                  PASS / FAIL
C-11 self-verification checklist:       PASS / FAIL
C-12 not-executor as opening identity:  PASS / FAIL
C-13 template-locked verification:      PASS / FAIL
C-14 arc structure in template:         PASS / FAIL
C-15 not-executor dual-site:            PASS / FAIL
C-16 contrast-grounded identity:        PASS / FAIL
C-17 explicit dependency narration:     PASS / FAIL
C-18 YAML-embedded dependency map:      PASS / FAIL
C-19 pre-template reference tables:     PASS / FAIL
C-20 per-layer arc narration:           PASS / FAIL
C-21 echo stage narrated in prose:      PASS / FAIL
C-22 BAD/GOOD gate contrast as table:   PASS / FAIL
C-23 tabular skill catalog:             PASS / FAIL
C-24 layer paragraph headers:           PASS / FAIL
C-25 echo paragraph enumerated:         PASS / FAIL
C-26 layer header cross-layer ref:      PASS / FAIL
C-27 terminal layer context dep:        PASS / FAIL

essential_pass  = ___ / 4   -> ___ * 15   = ___ pts  (of 60)
recommended_pass = ___ / 3  -> ___ * 10   = ___ pts  (of 30)
aspirational_pass = ___ / 20 -> ___ * 0.50 = ___ pts  (of 10)

composite = ___

golden = all essential PASS AND composite >= 80  ->  YES / NO
```

---

## Scorer Notes

- **C-01**: If YAML is invalid, C-01 fails. Score remaining criteria as best-effort from intent, noting the YAML failure.
- **C-02**: Echo stage is a hard plugin design contract. Missing, misplaced (not last), or lacking `auto: true` fails C-02 regardless of otherwise valid structure.
- **C-03**: Authority for valid skill names is `plugin-plan.md` (9 namespaces, ~47 skills). Namespace-qualified (`scout:feasibility`) and unqualified (`feasibility`) both pass if unambiguous. Partial matches that clearly identify a real skill pass.
- **C-04**: Gates expressing execution state (`"all skills complete"`, `"stage done"`) fail C-04. Gates must express evidence state (`"scout-feasibility signal exists"`, `"draft-spec artifact present"`).
- **C-05**: Dependency ordering is by namespace layer (scout -> draft -> review/prove -> topic), not alphabetically. A stage placing `review:design` before `draft:spec` fails because the design review requires a spec artifact. An explicit prose dependency chain (C-17) clarifies co-placement decisions.
- **C-07**: The framing note does not need to be elaborate — a single YAML comment (`# program is a plan; run each skill standalone`) suffices.
- **C-08**: "Deliberate arc" distinguishes from a flat dump of skills across stages. Look for breadth-first early stages (multiple namespaces explored) narrowing to depth and synthesis stages.
- **C-10**: The contrast can appear in instructions, comments, a before/after example pair, or as labeled BAD/GOOD columns within a reference table. A checklist item saying "avoid 'stage complete'" is not sufficient — needs a labeled good/bad juxtaposition.
- **C-11**: Checklist must be binary (checkbox or yes/no) and property-verifying, not a "did you remember to think about X" process prompt. Minimum 4 items. A single block comment with rules does not qualify. Checklist may be a bullet list or a structured table — either passes C-11.
- **C-12**: Elevation distinguishes from C-07 (which only requires the concept appears somewhere). C-12 passes only if the not-executor framing is the *opening identity* of the output — the lens through which all subsequent structure is read. An output that opens with a BAD example and resolves to "this is what this skill replaces" qualifies: the entire BAD+diagnosis+identity block forms a coherent opening unit.
- **C-13**: Pre-printing is what distinguishes C-13 from C-11. A checklist added via instruction ("include a verification section") passes C-11 but not C-13. C-13 requires the template skeleton itself to contain the section — the model fills in checkboxes, it does not compose the section from scratch.
- **C-14**: A prose instruction naming layers ("use three phases: breadth, depth, synthesis") does not pass C-14. The layer labels must appear as structural comments *inside* the YAML template body, creating visual separation between stage groups. C-14 requires C-08 to pass (the arc must be identifiable, and now also structurally labeled).
- **C-15**: C-15 requires C-12 to pass (opening prose is one of the two required sites). The YAML comment site must be marked as required or preserve-required — an incidental comment does not qualify. The intent is belt-and-suspenders: even if the model skips the opening prose, the template comment survives; even if the model strips comments, the prose survives.
- **C-16**: C-16 requires both C-10 and C-12 to pass. The key distinction: in C-10 the contrast can appear anywhere and serve any purpose; in C-12 the not-executor claim can appear at the opening without contrast. C-16 is their intersection in a specific structural order — contrast-as-identity-foundation. An output that states not-executor first and then shows a contrast does *not* pass C-16; the BAD example must precede and motivate the identity claim.
- **C-17**: Structural ordering alone (scout before draft) does not pass C-17. The narrator must explicitly state a causal link: what artifact stage N produces and why stage N+1 requires it. A single sentence suffices. Co-placement of skills within a stage that share dependency relationships may also qualify if the prose explains why they co-reside.
- **C-18**: C-18 requires C-14 to pass (layer dividers must already be present as the base structure). The inline annotation format does not need to be machine-parseable — a human-readable notation (`draft:* produced here | review:* requires draft-spec`) suffices. An annotation appearing only in prose instructions outside the template does not pass C-18; it must be structurally embedded in the YAML template comments. Distinct from C-17: C-17 is prose narration in any location; C-18 is structural notation inside template YAML comments.
- **C-19**: Tables placed after the YAML template do not pass C-19 — pre-template placement is required. A single table combining arc + gate design does not pass — two distinct tables covering distinct concerns are required. Prose lists or inline examples do not substitute for tabular format. C-19 is independent of C-08 and C-14: an output can embed arc labels in the template (C-14) without providing pre-template reference tables (C-19), and vice versa.
- **C-20**: C-20 requires C-17 to pass (per-layer narration is a stricter form of the same dependency narration requirement). A lifecycle overview paragraph naming all three layers in aggregate does not pass — each layer must receive its own paragraph-level treatment. The paragraphs may appear as a continuous section or interleaved with other content, but each must address a single named layer's artifact scope and handoff role. An output with two layer paragraphs (e.g., Breadth + Depth combined, then Synthesis) does not pass.
- **C-21**: C-21 is independent of C-02 (echo in YAML) — both can pass independently. The prose must appear before the template. An explanatory parenthetical inline in the skill catalog (`echo — auto-closing, no skills`) does not pass; a dedicated paragraph is required. The paragraph must address at minimum: why echo carries no skills, what `auto: true` means architecturally, and how echo signals arc closure. Mentioning echo in a lifecycle framing paragraph alongside other stages does not pass if echo is not the dedicated subject of that passage.
- **C-22**: C-22 requires C-10 to pass. The distinguishing feature is column structure — BAD and GOOD must be column headers (or equivalent row-level structural labels in a table), not prose labels on paragraphs or code blocks. A table where rows are gate examples and columns are BAD/GOOD is the canonical form. A table with a "Notes" column that includes "(bad)" or "(good)" inline does not pass — the column structure itself must encode the polarity.
- **C-23**: C-23 is independent of C-19 — an output can have a tabular skill catalog without meeting C-19's 2-table minimum (e.g., if it only has the skill table and no arc/gate tables), and C-19 can pass without a tabular skill catalog (if the second table is a gate design table). In practice they co-occur in high-scoring outputs. A table with only namespace names and no skill names does not pass C-23; the table must enumerate individual skills (or skill patterns) per namespace.
- **C-24**: C-24 requires C-20 to pass. "Layer identity and arc role" means the header must convey both which layer it is (e.g., "Layer 1", "Breadth", "Layer 1 (Breadth)") and what structural function it serves in the arc (e.g., "artifact scope and handoff contract", "evidence breadth phase", "dependency origin layer"). A header naming only the layer number without the role (e.g., "**Layer 1**" alone) does not pass. The header must be visually distinct — bold, a heading level, or equivalent — not a sentence fragment that begins the paragraph.
- **C-25**: C-25 requires C-21 to pass. The three required sub-item topics are: (1) why echo carries no skills / what skill-free contract means, (2) what `auto: true` means architecturally (does not wait for human review, no gate condition), (3) how echo signals arc closure (what it means for the program when echo closes). Items may be numbered (1/2/3), lettered (a/b/c), or use consistent bullet formatting — the key requirement is that each topic is a structurally separate, individually labeled point rather than a clause in flowing prose. An echo paragraph with two enumerated points does not pass even if it covers all three topics across two items.
- **C-26**: C-26 requires C-24 to pass. The cross-layer reference must name the adjacent layer by a specific identity — "Layer 2", "Depth layer", "the next layer" with a number qualifier — not a generic statement like "downstream stages" or "subsequent work". A single header satisfying this is sufficient; not all three are required. The canonical evidence form is "produces the foundational signals **Layer 2** requires" or "requires **Layer 1**'s scout artifacts". Distinct from C-17: C-17 is prose narration outside headers; C-26 is a cross-layer reference embedded in the bold header itself.
- **C-27**: C-27 requires C-24 to pass. The dependency statement in the Layer 3 header must be forward-facing about what the synthesis layer *requires*, not only about what it produces. "Produces the final synthesis artifact set" alone does not pass — the header must acknowledge this layer's dependence on prior context (e.g., "requires the full validated context", "requires review-validated artifact set from prior layers"). An output where Layer 3's header only states its output role (synthesizer) without stating its input dependency does not pass. Distinct from C-20: C-20 requires the paragraph body to address each layer's dependencies; C-27 requires the dependency acknowledgment to appear in the header itself.

---

## Changes from v23

**Aspirational tier expanded: 18 → 20 criteria, scoring adjusted to 0.50 pts each**

| New ID | Pattern | Source signal | Distinction |
|--------|---------|---------------|-------------|
| C-26 | **Layer header cross-layer dependency reference** — at least one layer narration header names an adjacent layer by number or identity within its role descriptor, creating a visible cross-layer dependency pointer in the header text | V-01/V-03 C-24 evidence: "**Layer 1 (Breadth) -- dependency origin; produces the foundational signals **Layer 2** requires:**" — "Layer 2" named explicitly in the header role descriptor | C-24 = all three headers have any arc role descriptor; C-26 = at least one descriptor names an adjacent layer by identity; a generic role label ("breadth phase", "validation layer") passes C-24 but not C-26 |
| C-27 | **Terminal layer header states context dependency** — the Layer 3 / Synthesis narration header includes a dependency statement for what the synthesis layer requires from prior layers, not merely labeling it as the final phase | V-01/V-03 C-24 evidence: "**Layer 3 (Synthesis) -- produces the synthesis artifact set; **requires the full validated context**:**" — the "requires the full validated context" clause is a dependency acknowledgment in the header itself | C-24 = terminal header has any role descriptor; C-27 = the descriptor must include a statement about what this layer requires (input dependency), not only what it produces; a synthesis label without a dependency clause passes C-24 but not C-27 |

**Dependency chain for new criteria:**
- C-26 requires C-24 PASS (cross-layer reference is a stricter form of the layer header requirement)
- C-27 requires C-24 PASS (context dependency statement is a stricter form of the terminal layer header requirement)
- C-26 and C-27 are independent of each other: a header can name "Layer 2" explicitly (C-26) without stating what it requires (C-27), and the terminal header can state "requires the full validated context" (C-27) without naming "Layer 2" by number (C-26)

**Scoring arithmetic**: 20 criteria × 0.50 pts = 10.00 pts total. The formula `aspirational_pass/20 * 10` yields exact values.

**Re-scoring Round 7 at v24:**

| Variation | C-26 | C-27 | Aspirational | Composite |
|-----------|------|------|-------------|-----------|
| V-01 | PASS ("Layer 2" named in Layer 1 header) | PASS ("requires the full validated context" in Layer 3 header) | 19/20 (C-25 FAIL) | 99.50 |
| V-02 | requires re-run (Layer 2 header: "artifact scope and internal handoff contracts" — no layer number named; Layer 1: requires re-run) | requires re-run (Layer 3 header: requires re-run to check for dependency clause) | TBD | TBD |
| V-03 | PASS (inherits V-01 headers) | PASS (inherits V-01 headers) | 20/20 | 100.00 |
