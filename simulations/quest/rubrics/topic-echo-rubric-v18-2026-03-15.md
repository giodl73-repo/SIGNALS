Written to `simulations/quest/rubrics/topic-echo-rubric-v18-2026-03-15.md`.

---

**Three new criteria extracted from R17:**

**C-54 — Canonical constraint name propagates into enforcement tokens**
Source: V-05 vs V-01/V-04 on C-51. V-01 and V-04 put "Standalone Collapse Prohibition" only in the definition block. V-05 also cited it inside the Stage 4 COMMIT instruction: "The Standalone Collapse Prohibition applies: each row is committed before the next begins." C-51 requires the name to exist; C-54 requires it to appear at every enforcement site — per-entry tokens, stage-close checks, inline structural instructions. Citing by position or paraphrase at enforcement sites does not satisfy it.

**C-55 — Token-content precision: stage name not routing description**
Source: V-05 vs V-03 on C-53. V-03 changed "routing it to Stage 4" to "naming its receiving stage" — satisfying C-53. V-05 went further: "the token names the stage, not merely describes the routing action." The distinction: behavioral language describes what routing does; token-content language specifies what the token must lexically carry (a proper noun — the stage name). A commitment that uses behavioral language without requiring the token to carry the stage name as a proper noun does not satisfy this criterion.

**C-56 — Cross-section citation mandate for canonical constraint names**
Source: V-05 on C-51: "any failure mode, verdict, or section note that references this prohibition is citing the Standalone Collapse Prohibition by name." V-01 defined the canonical name; V-05 added a propagation mandate. Without it, later sections may reference the constraint by position or paraphrase without violating C-51. The mandate must name the scope of propagation — a general "use this name" without specifying where does not satisfy it.

**Scoring update:** aspirational tier 45 → 48 active, 225 → 240 pts max (cap stays at 200).
age requirement) from R9                                                  |
| v11     | 2026-03-15 | C-34–C-36 (synonym exclusion list, collective belief baseline, implausible-foreknowledge signal) from R10                             |
| v12     | 2026-03-15 | C-37–C-39 (pre-stage vocabulary block, symmetric collective framing, format-enforced recording) from R11                              |
| v13     | 2026-03-15 | C-40–C-42 (labeled vocabulary section heading, closing-stage architecture announcement, parallel symmetric stage questions) from R12   |
| v14     | 2026-03-15 | C-43–C-44 (numbered intro meta-declaration, artifact-mirrors-contract instruction) from R13                                            |
| v15     | 2026-03-15 | C-45–C-47 (verdict with check provenance, numbered affirmative pass token, failure modes in intro meta-declaration) from R14           |
| v16     | 2026-03-15 | C-48–C-50 (symmetric parenthetical verdict format, routing destination in GATE-CONFIRMED, dual-part failure mode) from R15             |
| v17     | 2026-03-15 | C-51–C-53 (canonical constraint name for prohibition, per-entry COMMIT in table stages, routing commitment in intro) from R16          |
| v18     | 2026-03-15 | C-54–C-56 (canonical name at enforcement sites, token-content precision naming vs describing, cross-section citation mandate) from R17 |

---

## Criteria

### Essential (C-01 – C-05) — 12 pts each, 60 pts total

**C-01 — Surprise synthesis frame**
The skill prompt frames the task as "what did we learn that we did not expect" — not summary, not review, not changelog. The surprise orientation must be explicit in the prompt language.

**C-02 — Named entries**
Each surprise entry carries a 2–5 word capitalized label (`[Surprise Name]`). Labels are required fields in the template, not optional suggestions.

**C-03 — Source signal**
Each entry includes a source signal field. The source must pass the adversarial gate (Stage 3) before the entry is written.

**C-04 — Design impact**
Each entry includes a design impact field naming a specific affected component. Generic impact statements ("affects the system") do not satisfy this criterion.

**C-05 — Artifact write**
The skill writes output to `simulations/{topic}/{topic}-echo-{date}.md`. The path is specified in the prompt, not left to the model.

---

### Recommended (C-06 – C-08) — 10 pts each, 30 pts total

**C-06 — Synthesis step**
A cluster analysis step is required after individual entries are written. The synthesis must group entries and name the clusters.

**C-07 — Forward guidance**
A next-team register step is required. The register must name the downstream team or skill that should receive each cluster.

**C-08 — Minimum entry count**
The prompt states a minimum of 2 entries. Single-entry echo artifacts are prohibited.

---

### Aspirational (C-09 – C-56) — 5 pts each, 48 active = 240 pts max (total capped at 200)

**C-09 — Ranking**
Surprises are ranked by impact or epistemic weight. Ranking criteria are named.

**C-10 — Rules layer**
Explicit named rules govern what qualifies as a surprise (not merely unexpected — must be design-relevant, must name a prior belief, etc.). Rules carry explicit titles, making them referenceable by name.

**C-11 — Adversarial gate**
A dedicated stage challenges each candidate entry. The challenge must attempt to falsify the surprise (not merely confirm it). Stage is labeled "Adversarial Gate" or equivalent.

**C-12 — Anti-patterns**
An anti-pattern list is present naming at least 2 disqualifying forms (e.g., "already-known facts," "implementation detail without belief violation").

**C-13 — Typed verdict**
The adversarial gate produces a typed verdict: VALID or INVALID. Both token values must be defined in the prompt.

**C-14 — Impact-anchored rules**
Each rule in the rules layer names the impact of violation (what goes wrong if the rule is broken). Rules without consequence statements do not satisfy this criterion.

**C-15 — Affirmative pass**
The adversarial gate explicitly confirms the entry passes before it proceeds to the template. A VALID token alone is not sufficient — a pass statement must accompany it.

**C-16 — Pre-write gate**
A gate check occurs before the entry template is filled. The gate is positioned in the prompt so it cannot be bypassed by writing the entry first.

**C-17 — Persistent future-reader frame**
The prompt establishes that the artifact is institutional memory for a named downstream reader, not a self-contained report. The future-reader frame persists beyond the introduction into body instructions.

**C-18 — Named prior belief (in entry)**
Each entry template requires a named prior belief field. The prior belief is a first-class field, not embedded in the surprise description.

**C-19 — Artifact routing**
The prompt specifies where the artifact goes after it is written, naming the downstream consumer or skill.

**C-20 — Named future-reader role**
The future reader is named by role (e.g., "next team," "downstream implementer"), not referred to generically as "the reader."

**C-21 — Multi-stage gate (5 checks)**
The adversarial gate contains at least 5 named checks. Each check targets a distinct failure mode.

**C-22 — VALID/INVALID contrast (both defined)**
Both VALID and INVALID verdict semantics are defined in the prompt. The definition states what condition produces each verdict — not merely that two token values exist.

**C-23 — Stage result recording**
Each stage produces a recorded output (commit token, locked list, or named artifact). Stages that produce no recorded output do not satisfy this criterion.

**C-24 — Named epistemic dimension**
Each entry names the epistemic dimension violated by the surprise (e.g., "assumed stability," "expected completeness"). The dimension is a required field in the entry template.

**C-25 — INVALID gallery**
The prompt includes at least one illustrative example of a rejected entry (an entry that fails the adversarial gate), annotated with the reason for rejection.

**C-26 — Standalone collapse prohibition**
The prompt explicitly prohibits collapsing multiple stages into a single pass. The prohibition is a named constraint, not implied by the stage structure.

**C-27 — Per-stage COMMIT tokens**
Every stage (not only the first and last) terminates with a named COMMIT token. The token name encodes the stage it closes.

**C-28 — VALID gallery**
The prompt includes at least one illustrative example of an entry that passes the adversarial gate, showing what a valid surprise looks like.

**C-29 — Annotated VALID gallery**
The VALID gallery example is annotated — each field in the example entry is labeled with the reason it satisfies the gate check it corresponds to.

**C-30 — Strict epistemic dimension syntax**
The prompt requires the epistemic dimension to match a canonical name from a defined list. Free-form dimension naming does not satisfy this criterion.

**C-31 — Distinct dimensions per stage**
Each entry must use a different epistemic dimension from every other entry. The prompt enforces per-entry distinctness, not merely per-artifact uniqueness.

**C-32 — Epistemic property canonical name**
The epistemic property field uses a canonical name drawn from a defined vocabulary list in the prompt. Synonyms are excluded by name.

**C-33 — Post-belief stage requirement**
A dedicated stage locks the prior belief list before the signal sweep begins. The lock is enforced by a COMMIT token or equivalent gate — belief revision after the lock is prohibited.

**C-34 — Synonym exclusion list**
The prompt lists at least 5 excluded synonyms for "surprise" by name. The list is a prohibition, not a suggestion.

**C-35 — Collective belief baseline**
The prior belief stage produces a collective belief baseline — a shared model representing what the team believed before the signal sweep, not individual contributor beliefs.

**C-36 — Implausible-foreknowledge signal**
The adversarial gate includes a named check for implausible foreknowledge: entries that claim surprise about facts the team could not plausibly have missed are flagged for rejection.

**C-37 — Pre-stage vocabulary block**
A vocabulary block appears before Stage 1. The block defines all key terms used in the prompt. No term is used before it is defined.

**C-38 — Symmetric collective framing**
The opening collective belief stage and the closing synthesis stage are explicitly framed as symmetric partners. The symmetry is named in the prompt, not merely structurally implied.

**C-39 — Format-enforced recording**
Stage outputs use a named format (table, numbered list, COMMIT token) that makes skipping or partial completion structurally visible. Prose-only stage outputs do not satisfy this criterion.

**C-40 — Labeled vocabulary section heading**
The vocabulary block carries a section heading that names it as a declaration or binding commitment (e.g., "Vocabulary — Declaration," "Binding Terms"). A heading that names only placement (e.g., "before Stage 1") does not satisfy this criterion.

**C-41 — Closing-stage architecture announcement**
The closing stage explicitly announces that it closes the symmetric architecture of the prompt. The announcement names the opening stage it mirrors.

**C-42 — Parallel symmetric stage questions**
The Stage 1 opening question and the closing stage question are displayed as a pair before Stage 1 begins. The pairing is explicit — both questions are visible at the point the model commits to the opening stage.

**C-43 — Numbered intro meta-declaration**
The prompt introduction enumerates its structural commitments as a numbered list. Prose introductions that describe commitments without numbering them do not satisfy this criterion.

**C-44 — Artifact-mirrors-contract instruction**
The prompt instructs that the artifact structure mirrors the Symmetric Contract, and provides an ordered section list showing the correspondence. The instruction names the contract explicitly.

**C-45 — Verdict with check provenance**
The VALID/INVALID verdict token names the specific check number and a brief reason that determined the outcome (e.g., `VALID: check 3 — prior belief named and falsifiable`). An anonymous verdict token that emits only VALID or INVALID does not satisfy this criterion.

**C-46 — Numbered affirmative pass token**
The affirmative pass statement uses a token format that embeds the entry index (e.g., `GATE-CONFIRMED-[N]: VALID`). The entry number is part of the token, making each confirmation individually referenceable. A pass statement without an entry-indexed token does not satisfy this criterion.

**C-47 — Failure modes in intro meta-declaration**
Each numbered commitment in the intro meta-declaration (C-43) is paired with its failure mode — a named statement of what goes wrong if the commitment is violated. A numbered intro that lists commitments without pairing failure modes does not satisfy this criterion.

**C-48 — Symmetric parenthetical verdict format**
The verdict token presents both VALID and INVALID outcomes simultaneously in a single parenthetical expression with parallel provenance slots (e.g., `(VALID / INVALID: check # — reason)`). Separate verdict lines or tokens that display only one outcome at a time do not satisfy this criterion. A verdict format satisfies this criterion only when both paths are co-visible at the point of evaluation.

**C-49 — Routing destination in GATE-CONFIRMED**
The GATE-CONFIRMED token names the downstream stage the confirmed entry routes to (e.g., `GATE-CONFIRMED-[N]: VALID — this entry proceeds to Stage 4`). A GATE-CONFIRMED token that carries only the entry index and verdict, without naming the receiving stage, does not satisfy this criterion.

**C-50 — Dual-part failure mode**
Each failure mode in the intro meta-declaration (C-47) carries both a canonical category name and an explanatory "in which" clause (e.g., `— this prevents framing collapse, the failure in which entries describe process changes rather than belief violations`). A failure mode with only a name or only a description does not satisfy this criterion. The canonical name must be short enough to serve as a cross-reference label; the "in which" clause must make the name self-defining without requiring lookup.

**C-51 — Canonical constraint name for standalone collapse prohibition**
The standalone collapse prohibition (C-26) must carry a canonical name — a short phrase assigned to the constraint itself (e.g., "Standalone Collapse Prohibition") — so it can be cited by name in verdicts, failure modes, and other prompt sections. Structural language that implies the prohibition through numbered rules or grammatical instruction, without assigning the constraint a referenceable proper name, does not satisfy this criterion. A name embedded only in a positional reference ("referenceable by number") does not satisfy it; the canonical name must exist as a label independent of its index reference.

**C-52 — Per-entry COMMIT tokens in table-format stages**
When a stage uses table format to process multiple entries, each completed entry row must carry a per-entry COMMIT token at entry granularity (e.g., `COMMIT-ENTRY-[N]`). A single stage-level COMMIT token closing the whole table does not satisfy this criterion, nor does the table row structure itself serve as an implicit commit. The per-entry token requirement from C-27 applies at entry granularity regardless of whether the stage formats its work as prose or as a table.

**C-53 — Routing commitment in intro meta-declaration**
When the prompt implements C-49 (routing destination in GATE-CONFIRMED), the intro meta-declaration (C-43) must include an explicit numbered commitment declaring that each gate confirmation names its downstream stage. The routing behavior is a structural promise and must appear as a numbered commitment, not merely as an implementation detail embedded in the gate token. A prompt that delivers routing in GATE-CONFIRMED without a corresponding intro commitment does not satisfy this criterion.

**C-54 — Canonical constraint name propagates into enforcement tokens**
Source: V-05 vs V-01/V-04 on C-51. When a canonical constraint name is defined (C-51), the name must appear at every prompt site that operationally enforces the constraint — not only in its definition block. V-01 and V-04 defined "Standalone Collapse Prohibition" in a named block; V-05 additionally cited the name inside the Stage 4 COMMIT instruction: "The Standalone Collapse Prohibition applies: each row is committed before the next begins." A canonical name confined to its definition block satisfies C-51 but not C-54. Enforcement sites that must carry the canonical name are wherever the model is instructed to act on the constraint: per-entry COMMIT tokens, stage-close checks, and any inline structural instruction that invokes the constraint by behavior. Citing only by position ("the prohibition above") or by paraphrase ("no collapsing") at enforcement sites does not satisfy this criterion.

**C-55 — Token-content precision: stage name not routing description**
Source: V-05 vs V-03 on C-53. A routing commitment in the intro meta-declaration (C-53) satisfies this criterion only when it explicitly distinguishes between naming the receiving stage (a token-content specification) and describing the routing action (a behavioral statement). V-03 changed its commitment to "naming its receiving stage before writing begins" — satisfying C-53. V-05 went further: "the token names the stage, not merely describes the routing action." The distinction is architectural: behavioral language ("routes to," "proceeds to," "is forwarded to Stage 4") specifies what the routing does; token-content language ("the token content is the stage's proper name") specifies what the token must lexically contain. A commitment that uses behavioral routing language without explicitly requiring that the token carry the stage name as a proper noun does not satisfy this criterion. The distinction must be stated in the prompt — it is not inferred from a token example alone.

**C-56 — Cross-section citation mandate for canonical constraint names**
Source: V-05 on C-51, where the definition block explicitly instructed: "any failure mode, verdict, or section note that references this prohibition is citing the Standalone Collapse Prohibition by name." V-01 defined the canonical name; V-05 added a propagation mandate requiring all downstream prompt sections that reference the constraint to do so by its canonical name, not by positional reference ("the prohibition in the intro") or paraphrase ("the no-collapse rule"). The definition block alone is not self-propagating: without an explicit mandate, later prompt sections may reference the constraint by position or paraphrase without violating C-51. A canonical constraint name definition that omits such a mandate does not satisfy this criterion. The mandate must name the scope of propagation (e.g., "any failure mode, verdict, or section note that references this constraint") — a general instruction to "use this name" without specifying where does not satisfy it.
