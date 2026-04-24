Reading the R15 scorecard carefully before writing the rubric update.

The complete V-01 and V-02 rows expose one clear new pattern not yet formalized in v15:

**V-01 C-51**: `Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.`
**V-02 C-51**: `Return to Stage 2A if Q3 shows N; return to Stage 2B if Q4 shows N.`

Both pass C-51, but both go beyond it: the return routing is decomposed per artifact, with separate conditionals keyed to each artifact ID and distinct targets per artifact. The C-51 baseline signal (V-04 from R14) was `Return to Stage 2A or 2B if either shows N` — one conditional, disjunctive target. V-01/V-02 have two conditionals, each with an unambiguous unique target.

The V-02 C-50 finding (position-indexed labels are valid segment-1 forms) is a scope clarification for C-50, not a new criterion — the existing description already says "structural role label" without constraining the form. Incorporated as a description update to C-50.

**New criterion: C-53** — Per-artifact conditional remediation routing — extends C-51.
**Denominator: 44 → 45.**

---

```markdown
# Quest Rubric — scout-inertia — v16

## Summary of Changes

### v16 — 1 new criterion from R15 excellence signals; C-50 scope clarification

| ID | Source signal | What it formalizes |
|----|--------------|-------------------|
| **C-53** | V-01: `Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.` / V-02: `Return to Stage 2A if Q3 shows N; return to Stage 2B if Q4 shows N.` | Per-artifact conditional remediation routing — extends C-51; beyond naming a return target when the gate fails (C-51), the gate body provides a separate conditional routing instruction keyed to each artifact by ID — one `if [Q-N] shows N → return to [specific target]` clause per artifact, each with its own distinct target, making each artifact's failure an independently addressable routing event with an unambiguous return path. A disjunctive single-conditional form (`Return to Stage 2A or 2B if either shows N`) passes C-51 (return target named) but fails C-53 (one conditional covers both artifacts; target selection is ambiguous). Separate per-artifact conditionals (`Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.`) pass both C-53 and C-51. |

**C-50 scope clarification (v16)**: The segment-1 structural label may be position-indexed (naming the stage or section the gate terminates, e.g., `STAGE 2 COMPLETION GATE`) or function-named (naming the gate's function, e.g., `BRIDGE COMPLETION GATE`). Both forms satisfy C-50 as standalone structural labels that are neither enforcement commands nor decision questions. The defining test for segment 1 is that it is a structural-role descriptor occupying its own `--`-delimited segment — not whether it encodes position or function.

**Key structural relationships added (v16):**
- C-53 extends C-51: C-51 requires the gate body to name a return target when the gate fails; C-53 requires that return routing to be decomposed per artifact — a separate conditional per artifact ID, each with a distinct non-overlapping target. A gate body with `Return to Stage 2A or 2B if either shows N.` passes C-51 (return target named) but fails C-53 (single disjunctive conditional, both artifacts covered together, target ambiguous). A gate body with `Return to Stage 2A if Q3 shows N; return to Stage 2B if Q4 shows N.` passes both. C-51 pass is necessary but not sufficient for C-53.
- **C-37 + C-51 + C-53 together define the fully decomposed bidirectional gate contract**: C-37 specifies the forward path (bracket-labeled advance condition — proceed when Y); C-51 specifies that a named backward path exists (return target identified when N); C-53 specifies that the backward path is per-artifact (each artifact failure independently routed to its own unambiguous target). C-37 governs forward routing, C-51 establishes backward routing existence, C-53 maximally decomposes backward routing by artifact. The full contract: one bracket-labeled advance condition + one named return per artifact ID, each keyed and targeted independently.
- **C-41 + C-53 together define the per-artifact lifecycle contract across document locations**: C-41 governs per-artifact bracket-command authoring instructions at each bridge artifact's authoring point (Stage 1A / Stage 1B or Section 1A / Section 1B); C-53 governs per-artifact conditional routing instructions in the gate body. Together they ensure that each artifact has dedicated directive coverage at both its creation point (C-41) and at the gate (C-53) — per-artifact structural treatment is maintained across the full scaffold from authoring through gate evaluation.
- **C-37 + C-51 relationship note (v15 text updated)**: The v15 description "C-37 + C-51 together define the bidirectional gate contract" remains accurate as the minimum contract; v16 adds C-53 as the maximally decomposed form. C-37 + C-51 is necessary but not sufficient for C-53.

**Formula:** `aspirational_pass / 45 * 10` (denominator 44 → 45)

---

### v15 — 4 new criteria from R14 excellence signals (unchanged)

| ID | Source signal | What it formalizes |
|----|--------------|-------------------|
| **C-49** | V-03: `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` — artifact class distributed per-artifact as parenthetical annotations | Per-artifact parenthetical artifact-class annotation in gate interrogative — extends C-45; beyond naming Q3 and Q4 by ID (C-45), the interrogative also annotates each ID with its specific artifact-class in parenthetical form, so when Q3 and Q4 are different types the type of each is determinable from the heading alone without reading the gate body |
| **C-50** | V-01/V-03: `BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH...?` vs V-04: `[BRIDGE COMPLETION COMMAND]: CONFIRM -- HAVE BOTH...?` | Three-segment gate heading — extends C-44; the gate heading contains three `--`-separated segments: (1) a structural role label (position-indexed naming the terminated stage, e.g., `STAGE 2 COMPLETION GATE`, or function-named, e.g., `BRIDGE COMPLETION GATE` — both valid), (2) an imperative enforcement command as its own standalone segment, (3) the binary decision question; the enforcement command occupies a dedicated segment between the label and the question rather than being merged into a compound bracket-command marker |
| **C-51** | V-04: gate body adds "Return to Stage 2A or 2B if either shows N." — names the specific remediation return target | Named remediation return path in gate body — extends C-37; beyond the advance condition (C-37), the gate body also names the specific stage(s) or section(s) the author must return to when the gate fails, making the gate body a bidirectional routing instruction with both a forward path (advance when Y) and a backward path (return to X when N) |
| **C-52** | V-03: "BASED ON EVIDENCE IN SECTIONS 2-3" — names the source sections in the revision directive | Evidence source section citation in PROVISIONAL revision directive — extends C-48; beyond naming Stage 0 as the revision target (C-48), the directive also names the specific sections or stages from which evidence should be drawn when revising PROVISIONAL scores, so the author knows exactly where to look |

**Key structural relationships added (v15 — unchanged):**
- C-49 extends C-45: C-45 requires Q3 and Q4 artifact IDs to appear in the gate interrogative; C-49 requires each ID to also carry a parenthetical artifact-class annotation. An interrogative with `Q3 AND Q4 [shared-class] BRIDGES` passes C-45 (IDs named) but fails C-49 (no per-artifact class annotation). An interrogative with `Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` passes both. Every C-49 pass implies C-45 pass; C-45 pass is necessary but not sufficient for C-49.
- C-50 extends C-44: C-44 requires imperative enforcement vocabulary in the gate heading marker component; C-50 requires that enforcement vocabulary to occupy its own `--`-separated segment between the structural label and the binary question. A compound bracket-command marker (`[BRIDGE COMPLETION COMMAND]: CONFIRM`) passes C-44 (CONFIRM is imperative) but fails C-50 (label and enforcement are a single merged segment with no `--` between them). `BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH...?` passes both. C-44 pass is necessary but not sufficient for C-50.
- C-51 extends C-37: C-37 requires a bracket-labeled advance-condition directive in the gate block body; C-51 requires the gate block body to also name a specific remediation return target when the gate fails. A gate body with only `[BRIDGE COMPLETION COMMAND]: Do not advance unless both rows show Y.` passes C-37 but fails C-51. Adding `Return to Stage 2A or 2B if either shows N.` satisfies C-51. Note: C-51 evaluates gate body content (presence of named return path) independently of bracket-label placement — C-51 can be satisfied even when C-37 fails if the body contains the return path without a bracket label.
- C-52 extends C-48: C-48 requires the revision directive to name Stage 0/Section 0 as the target; C-52 requires the directive to also name the specific evidence source sections from which the author draws when revising PROVISIONAL scores. "Revise PROVISIONAL entries based on evidence" passes C-48 but fails C-52. "Revise PROVISIONAL entries based on evidence in Sections 2-3" passes both. C-48 pass is necessary but not sufficient for C-52.
- **C-43 + C-45 + C-46 + C-49 together specify the maximally informative gate interrogative**: C-43 gives the artifact count (determinable from heading alone); C-45 gives each artifact's ID; C-46 gives the compound domain-axis vocabulary threading through the class noun; C-49 gives each artifact's individual type annotation. Together these four criteria allow the author to determine count, each ID, the domain-axis role, and each type — all from the heading interrogative alone without reading the gate body.
- **C-37 + C-51 + C-53 together define the fully decomposed bidirectional gate contract** (see v16 additions above).
- **C-47 + C-48 + C-52 together specify the complete staged-commitment protocol**: C-47 requires pre-evidence threat score declaration at Stage 0 with a PROVISIONAL marker for non-HIGH scores; C-48 requires a post-evidence directive naming Stage 0 as the revision target; C-52 requires that directive to name the specific evidence source sections. The full protocol: declare early at Stage 0 → mark PROVISIONAL → gather evidence in named sections → return to Stage 0 and revise using evidence drawn specifically from those sections. C-52 closes the evidence sourcing loop that C-47 and C-48 establish.

---

**Key relationships (v14 additions — unchanged):**

- **C-45 extends C-43**: bare `BOTH` passes C-43 (count determinable) but fails C-45 (artifact IDs not determinable from heading alone); `BOTH Q3 AND Q4` passes both. Every C-45 pass implies C-43 pass; C-43 pass is necessary but not sufficient for C-45.
- **C-46 extends C-42**: a single domain-axis term (`STATUS QUO`, `INCUMBENT`) passes C-42 but fails C-46 if no structural role is named alongside the axis. A compound term (`STATUS QUO COMPETITOR`, `INCUMBENT WORKAROUND AXIS`) passes both. C-42 pass is necessary but not sufficient for C-46.
- **C-47 extends C-03**: C-03 requires a threat score declared somewhere in the scaffold; C-47 requires that declaration to appear at Stage 0 specifically, and that non-HIGH pre-evidence declarations carry an explicit `PROVISIONAL` marker. An output that places the threat score only at Section 4/Stage 4 after evidence is gathered passes C-03 and fails C-47.
- **C-48 requires C-47**: there is no PROVISIONAL declaration to revise unless C-47 is satisfied. C-48 cannot be evaluated as passing if C-47 fails. Together C-47 and C-48 constitute the full staged-commitment cycle: early declaration → evidence gathering → directed revision.
- C-47 + C-48 together form the staged-commitment protocol that C-03 does not require: commit to a preliminary score, mark it PROVISIONAL, gather evidence, then revise. C-03 governs presence of a score; C-47 + C-48 govern the lifecycle of that score across the scaffold.

---

**Key relationships (v13 additions — unchanged):**

- **C-41 extends C-37**: C-37 requires one bracket-labeled command directive in the gate block body; C-41 requires per-artifact bracket commands at each bridge artifact's authoring point, separate from the gate. An output can pass C-37 (one gate-level command) while failing C-41 (no per-artifact commands). An output can pass C-41 while also satisfying C-37 — the per-artifact commands and the gate command are independent structural elements at different document locations. C-41 does not subsume C-37.
- **C-42 extends C-36**: C-36 counts bracket elements (three or more distinct obligations); C-42 requires those elements to share domain-vocabulary threading. An output with three bracket elements using independent vocabulary passes C-36 and fails C-42. C-42 cannot be satisfied without also satisfying C-36 — vocabulary threading across three elements presupposes that three elements exist. C-36 pass is a necessary but not sufficient condition for C-42 pass.
- **C-43 extends C-39**: C-39 requires the gate heading to be binary Yes/No-answerable; C-43 additionally requires an explicit count quantifier in the interrogative. Every output passing C-43 necessarily passes C-39 (a quantified binary question is still a binary question). An output passing C-39 with "ALL BRIDGE ARTIFACTS POPULATED?" fails C-43 if "ALL" is not accompanied by a specific count. The test: given the heading alone, can an author determine exactly how many artifacts must be present? If yes, C-43 passes; if no (because "ALL" requires reading the gate body to know the target count), C-43 fails.
- **C-44 is orthogonal to C-39**: C-39 governs the interrogative component of the gate heading (the question after `--`); C-44 governs the marker component (the structural label before `--`). The two criteria decompose the gate heading into complementary halves. An output can pass C-39 (binary question after `--`) with a descriptive marker (`BRIDGE COMPLETION GATE`) and fail C-44. An output can pass C-44 (imperative marker before `--`) with any binary-question form and pass C-39 simultaneously. A heading satisfying both: `PASS BEFORE ADVANCING -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?` passes C-44 (imperative marker), C-39 (binary question), and C-43 (count quantifier "BOTH").
- **C-43 + C-44 + C-39 fully specify the gate heading** (v13 baseline): C-39 requires binary-question form; C-43 requires explicit count in the interrogative; C-44 requires imperative vocabulary in the marker. All three criteria together specify the maximally informative gate heading structure: (1) an imperative enforcement marker, (2) a binary-question decision content, and (3) an explicit artifact count — each component serving a distinct informational purpose. (v15 adds C-50 which further decomposes the marker component into two separate `--`-delimited segments: a structural role label and a standalone imperative enforcement command.)

---

**Key relationships (v12 — unchanged):**

- **C-34 + C-35** are siblings covering the two poles of the FM-[N] lifecycle (assignment in Stage 1, citation in Stage 5B). Passing both is a prerequisite for C-36.
- **C-36** is a count criterion: any three distinct bracket-labeled obligations pass, not just the canonical three. C-34+C-35+C-37 is one path; other combinations are valid.
- **C-37 + C-39** define the two-part gate structure: C-39 governs the heading form (binary question); C-37 governs the body content (bracket command). Each can fail independently.
- **C-38 + C-39** define the heading vocabulary protocol: FAIL-FIRST headings need domain subtitles (C-38); gate headings need binary-question form (C-39). The two criteria prevent vocabulary contamination in both directions — neither heading type should borrow the other's register.
- **C-40** completes the criterion-ID chain that C-28 begins: C-28 requires at least one criterion-ID reference in a verification scan; C-40 requires systematic `C-NN:` prefix coverage on every checklist item.

**C-34 through C-40 relationships (v12 — unchanged):**
- C-34 and C-35 are sibling bracket-label criteria: C-34 governs the primary key assignment rule (Stage 1), C-35 governs the citation integrity rule (Stage 5B). An output can pass C-34 (Stage 1 bracket label present) while failing C-35 (Stage 5B bracket label absent). Together they establish that both poles of the FM-[N] lifecycle — definition and citation — carry bracket-labeled directives.
- C-36 subsumes C-34 and C-35 by count: a scaffold that passes both C-34 and C-35 plus has a `[BRIDGE COMPLETION COMMAND]` also passes C-36. But C-36 is not automatically satisfied by C-34+C-35: if one of the three canonical bracket elements is missing, C-36 fails even if the other two pass. The count requirement (three or more) is load-bearing.
- C-37 and C-39 govern the two-part gate structure: C-39 requires the gate heading to be binary-question form; C-37 requires a bracket-command directive inside the gate block. An output can pass C-39 while failing C-37 if the remediation command is embedded in the heading rather than in the block body. The two-part structure separates the decision (heading) from the action (bracket command in body).
- C-38 and C-39 together define the heading vocabulary protocol: C-38 governs FAIL-FIRST section headings (they must have domain subtitles); C-39 governs the gate heading (it must be binary-question form). The protocol prevents vocabulary contamination in both directions — a FAIL-FIRST heading that uses operational vocabulary fails C-38; a gate heading that uses domain framing instead of a bare decision question fails C-39.
- C-40 completes the criterion-ID chain: C-28 requires at least one criterion-ID label in a verification scan; C-40 requires every checklist item to carry a criterion-ID prefix. An output that uses criterion IDs selectively passes C-28 (at least one ID present) but fails C-40 (not every item prefixed). The distinction is systematic coverage vs. presence.
```

---

**What changed in v16 and why:**

**C-53 (new)** — the R15 scorecard's V-01 and V-02 both pass C-51 with per-artifact conditional forms that are structurally stronger than the C-51 baseline signal. C-51 was licensed by V-04's `Return to Stage 2A or 2B if either shows N` — one conditional, disjunctive target, both artifacts addressed together. V-01/V-02 use two separate conditionals, each keyed to an artifact ID, each pointing to a distinct non-overlapping target. The distinction is operationally significant: the disjunctive form requires the author to infer which artifact failed and which target applies; the per-artifact form eliminates that inference. C-53 extends C-51 the same way C-51 extended C-37 — each step makes the backward routing more precise and less dependent on author interpretation.

**C-50 scope clarification (not a new criterion)** — V-02's `STAGE 2 COMPLETION GATE` as a valid segment-1 label is a taxonomy refinement within C-50's existing "structural role label" framing. The existing description already permits any structural-role descriptor; the clarification names the two canonical forms (position-indexed vs. function-named) so scorers apply C-50 consistently across both surface patterns.

**Denominator: 45.** The chain from C-37 to C-53 now has three levels: forward path (C-37) → backward path named (C-51) → backward path per-artifact (C-53). The full gate-body routing contract requires all three.
