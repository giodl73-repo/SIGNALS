Now I have both files. Let me score all five variations.

---

# Quest Score — corps-pr Round 3

**Rubric**: v3 (14 criteria: 5 essential / 3 recommended / 6 aspirational)
**Scoring formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/6 * 10)`
**PARTIAL = 0.5 criterion value**

---

## Criterion Reference

| ID | Weight | Category |
|----|--------|----------|
| C-01 | essential | Routing traceable to org.yaml |
| C-02 | essential | Severity labels on all findings |
| C-03 | essential | Cross-role consensus synthesis |
| C-04 | essential | Explicit GO/NO-GO decision |
| C-05 | essential | Role-domain-specific findings |
| C-06 | recommended | Coverage gap notice |
| C-07 | recommended | Per-role finding count + severity summary |
| C-08 | recommended | AMEND scope disclosure block |
| C-09 | aspirational | Root cause synthesis for divergent findings |
| C-10 | aspirational | GO WITH CONDITIONS names sign-off role |
| C-11 | aspirational | Inertia Advocate sequenced first |
| C-12 | aspirational | Divergence names mechanism, not perspective label |
| C-13 | aspirational | Ban list enumerated >=3 phrases, self-auditable |
| C-14 | aspirational | Each technical section anchors against IA verdict |

---

## V-01 — Role Sequence: Mandatory IA-Anchor Slot

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | Step 1 routing table with explicit `org.yaml Scope Reason` column; every file required; inferred-from-filename explicitly disallowed |
| C-02 | PASS | `[P1/P2/P3]` present in IA and all technical role finding templates |
| C-03 | PASS | Step 4 Consensus Analysis: Agreement + Divergence + Critical sections required |
| C-04 | PASS | "Exactly one decision. Delegated or hedged decisions fail." |
| C-05 | PASS | Validity check: "would only this role raise this finding given their domain lens? If any generic reviewer could write the same sentence, revise it." — explicit domain-lens test |
| C-06 | PASS | "COVERAGE GAP: [file] — no scope pattern matches this path." |
| C-07 | PASS | `Summary: [N] findings — [x] P1, [y] P2, [z] P3` in both IA and technical role templates |
| C-08 | PASS | Structured AMEND SCOPE block with What was amended / Roles added / Roles removed / Prior findings superseded |
| C-09 | PASS | `Mechanism: [specific property of the code — what makes one role see P1 and the other see P3, stated as a code or architectural fact, not a role attribute]` |
| C-10 | PASS | `sign-off: [role who confirms resolution before merge]` in conditions template |
| C-11 | PASS | "The Inertia Advocate section is the first review section in the output." |
| C-12 | PASS | "For every divergence: name the structural or architectural mechanism... Perspective labels are not mechanisms." |
| C-13 | PASS | 5-phrase enumerated checklist with `[ ]` boxes in Step 4 consensus section — each independently checkable. All 5 phrases distinct surface forms. |
| C-14 | PASS | "The **IA anchor** field is mandatory — fill it before writing any findings. A technical section with an unfilled IA anchor is incomplete." — explicit mandatory + incompleteness declaration |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 6/6 → 10

**Composite: 100** | Golden: YES

---

## V-02 — Output Format: Table-Centric with IA Anchor Row

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | TABLE 1 with org.yaml Scope Pattern column; coverage gap table defined |
| C-02 | PASS | Severity column in findings tables; column contract defines P1/P2/P3 |
| C-03 | PASS | TABLE N+1 CONSENSUS with Signal / Finding Area / Roles / Mechanism columns, Agreement + Divergence + Critical rows |
| C-04 | PASS | TABLE N+2 RECOMMENDATION; "One decision value only. Hedged decisions fail." |
| C-05 | **PARTIAL** | Column contract enforces specific code surface naming ("Auth concern fails; `auth/middleware.ts:88` passes") but has no explicit domain-lens validity check — no "would only this role raise this?" instruction. Specificity ≠ domain-specificity; a finding naming a specific location but generic to any reviewer would pass the column contract |
| C-06 | PASS | Coverage gap table format defined |
| C-07 | PASS | TOTAL row required in every role table with `[N] findings: [x] P1, [y] P2, [z] P3`; "A section without a TOTAL row fails." |
| C-08 | PASS | Structured AMEND SCOPE block before TABLE 1 |
| C-09 | PASS | Divergence rows: "structural property of the code causing the difference" in Mechanism column |
| C-10 | PASS | "Sign-off Role must name the role that confirms resolution before merge." |
| C-11 | PASS | "Inertia Advocate runs first. Their findings table appears before all technical role tables." |
| C-12 | PASS | Divergence Mechanism column requires structural code property |
| C-13 | PASS | "Divergence Mechanism — self-audit ban list:" with 5-phrase `[ ]` checklist in TABLE N+1 instructions |
| C-14 | PASS | "IA anchor field: required for every technical role table. A section without a filled IA anchor field is incomplete regardless of findings quality." — explicit incompleteness declaration |

**Essential**: 4.5/5 → 54 | **Recommended**: 3/3 → 30 | **Aspirational**: 6/6 → 10

**Composite: 94** | Golden: NO (C-05 PARTIAL fails essential-all-pass gate)

---

## V-03 — Phrasing Register: Convince the Skeptic

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | Step 1 "Who reviews this PR" block with org.yaml scope reason required per role |
| C-02 | PASS | `F-01 [P1/P2/P3]` in both IA and technical role templates |
| C-03 | PASS | Step 4 "What the room decided" with Agreed on / Disagreed on / Biggest risk |
| C-04 | PASS | Step 5 "The call" — "No hedging. No 'the team should weigh.' The PR merges, does not merge, or merges after named conditions." |
| C-05 | PASS | "Finding check: does this finding carry this reviewer's voice? Could only they have raised it given their domain? A finding that any reviewer could write regardless of role — rewrite it." |
| C-06 | PASS | "No one in org.yaml covers [path] — coverage gap." |
| C-07 | PASS | `[N] findings — [x] P1, [y] P2, [z] P3` closing line in each role template |
| C-08 | **PARTIAL** | AMEND section uses "Say: what role was added, which files triggered the addition, which earlier findings (if any) are superseded" — the three required elements are named but no structured output block template is provided; a model could format the disclosure inconsistently. Other variations define an explicit AMEND SCOPE block |
| C-09 | PASS | "Why: [specific code property, system boundary, or architectural fact causing the difference — not a reviewer attribute]" |
| C-10 | PASS | "Before merge (if applicable): 1. [what must be fixed] — confirmed by: [role]" |
| C-11 | PASS | "Before anyone else speaks, the Inertia Advocate states their case." Step 2 precedes Step 3 structurally |
| C-12 | PASS | "When explaining why two reviewers disagree, say what causes it in the code, not in the people." |
| C-13 | PASS | 5-phrase ban list in Step 4 with explicit "check your output against all of them before finishing" — the 5th phrase "it comes down to their focus area" is a distinct surface form not present in other variations. Independently checkable. |
| C-14 | **PARTIAL** | "Responding to the skeptic:" prose field IS in the technical role template and does name IA's assessment. However no mandatory enforcement language: no "this field is mandatory" or "a section without this is incomplete." Other variations (V-01, V-02, V-05) explicitly declare the field incomplete if missing; V-03's field is in the template but could be skipped without triggering an explicit failure condition |

**Essential**: 5/5 → 60 | **Recommended**: 2.5/3 → 25 | **Aspirational**: 5.5/6 → 9.17

**Composite: 94.17** | Golden: YES (all essential pass; composite 94.17 ≥ 80)

---

## V-04 — Lifecycle Emphasis + Phase-Gated IA Anchor

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | PHASE 1 routing table; R3–R6 explicitly map every file; coverage gap format defined |
| C-02 | PASS | `[P1/P2/P3]` in IA and Sub-phase 2B templates |
| C-03 | PASS | PHASE 3 SYNTHESIZE: A (inertia baseline) + B (agreement/divergence) + C (critical finding) |
| C-04 | PASS | PHASE 4 DECIDE: "Exactly one decision value. Delegated decisions fail." |
| C-05 | PASS | "Validity check per finding: is this finding specific to this role's domain? If a generic reviewer could write the same sentence regardless of their role, revise it." |
| C-06 | PASS | "COVERAGE GAP: [file] — no org.yaml scope pattern covers this path." |
| C-07 | PASS | `Summary: [N] findings — [x] P1, [y] P2, [z] P3` in both sections |
| C-08 | PASS | AMEND SCOPE block defined before Phase 1; `--amend add` / `--amend scope` behavior specified |
| C-09 | PASS | "Mechanism: [structural or architectural property of the code causing this difference — names a code surface, system boundary, or contract — not a reviewer attribute]" |
| C-10 | PASS | `sign-off: [role who confirms resolution before merge]` |
| C-11 | PASS | "Sub-phase 2A — Inertia Advocate: must be written and complete before any technical role section begins. Sub-phase 2B may not begin until this section is done." — strongest structural gate of all variations |
| C-12 | PASS | "For every divergence: name the structural or architectural mechanism causing the rating difference." |
| C-13 | **PARTIAL** | 5-phrase ban list with `[ ]` boxes is present but positioned as a Phase 3 **self-audit exit condition** — located after the `## Consensus Analysis` template block rather than within it. C-13 requires "The skill's consensus template contains an explicit, enumerated ban list." V-04's consensus template block ends before the ban list begins; the list is a phase-level check adjacent to the template, not inside it |
| C-14 | PASS | "Entry condition for each role section within 2B: IA anchor filled before any findings are written. Do not write F-01 until the IA anchor field is complete." — structural entry condition is the strongest C-14 enforcement mechanism of all five variations |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5.5/6 → 9.17

**Composite: 99.17** | Golden: YES

---

## V-05 — Formal/Terse Register + Ban List as Named Artifact

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | SECTION 1 ROUTING table with Scope Pattern column; Inertia Advocate as default always-included row |
| C-02 | PASS | `F-01 [P1|P2|P3]` format in all templates |
| C-03 | PASS | SECTION 4 CONSENSUS with Agreement + Divergence + Critical |
| C-04 | PASS | SECTION 5 RECOMMENDATION: "One decision value. Hedged or delegated decisions are protocol failures." |
| C-05 | PASS | "Finding validity: a finding that any reviewer could write regardless of domain fails. Rewrite until only this role's domain lens produces it." |
| C-06 | PASS | "COVERAGE GAP: [file] — no org.yaml scope pattern." |
| C-07 | PASS | `Summary: [N] findings — [x]P1 [y]P2 [z]P3` |
| C-08 | PASS | Structured AMEND block before SECTION 1 with Amended / Roles added / Roles removed / Findings superseded |
| C-09 | PASS | "Mechanism: [structural code property causing the difference — must not match BL-01 through BL-05. A passing mechanism names a code property, system boundary, or architectural constraint — not a reviewer attribute.]" |
| C-10 | PASS | `C-01: [what must be resolved] — sign-off: [role]` |
| C-11 | PASS | "Inertia Advocate output precedes all technical role sections. Ordering is structural — not configurable." |
| C-12 | PASS | Mechanism line must not match BL-01 through BL-05 — ban list integration forces structural naming |
| C-13 | PASS | Named artifact BL-01 through BL-05 table at the top of the prompt — each entry has ID + banned phrase + failure reason column. 5 phrases, all independently auditable by ID. Consensus section says "BL audit: scan the Mechanism line against BL-01 through BL-05. Each ID is independently checkable." The ban list is a first-class protocol component referenced throughout the run |
| C-14 | PASS | "IA ANCHOR field is mandatory. A technical section without a completed IA ANCHOR field is incomplete regardless of findings quality." + cross-reference to BL-01 through BL-05 in the anchor requirement itself |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 6/6 → 10

**Composite: 100** | Golden: YES

---

## Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Essential | Rec | Asp | Composite | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|-----|-----|-----------|--------|
| V-01 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 60 | 30 | 10 | **100** | YES |
| V-02 | P | P | P | P | PA | P | P | P | P | P | P | P | P | P | 54 | 30 | 10 | **94** | NO |
| V-03 | P | P | P | P | P | P | P | PA | P | P | P | P | P | PA | 60 | 25 | 9.2 | **94** | YES |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | PA | P | 60 | 30 | 9.2 | **99** | YES |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 60 | 30 | 10 | **100** | YES |

P = PASS | PA = PARTIAL | F = FAIL

**Ranking**: V-01 = V-05 (100) > V-04 (99) > V-03 ≈ V-02 (94)

---

## PARTIAL Analysis

**V-02 / C-05** (essential — disqualifies golden): Column contract enforces specific code-surface naming but has no domain-lens validity check. The instruction "must name a specific function, module, interface, or changed line" prevents category findings but does not prevent role-generic specific findings. A security-architect section writing "inconsistent naming convention at `auth/middleware.ts:88`" passes V-02's column contract but fails C-05. All other variations include an explicit "would only this role raise this?" test.

**V-03 / C-08** (recommended): AMEND guidance names all three required elements (what amended, roles changed, findings superseded) but provides no structured output block template. Models receiving "Say: what role was added..." may format the disclosure inconsistently or omit elements. V-01, V-02, V-04, V-05 all define named AMEND SCOPE / AMEND block templates.

**V-03 / C-14** (aspirational): "Responding to the skeptic:" field is present in the technical role template and does name the IA assessment. Missing: mandatory enforcement language. No statement that a section without this field is incomplete. V-01/V-02/V-05 all include explicit "incomplete regardless of findings quality" language; V-03's field is in the template but unsupported by a failure condition.

**V-04 / C-13** (aspirational): The 5-phrase ban list is present, enumerated, and checkable. However it is positioned as a Phase 3 self-audit exit condition — after the `## Consensus Analysis` template block, not within it. C-13 requires "The skill's consensus template contains an explicit, enumerated ban list." V-04's template block ends before the ban list begins; the list is a phase-level audit step adjacent to the template.

---

## Excellence Signals — V-01 and V-05

**Signal 1 — Failure-reason annotation per ban phrase (V-05)**

V-05's ban list is not just a prohibition — each entry includes a "Failure Reason" column that names *why* the phrase fails structurally:

| ID | Banned Phrase | Failure Reason |
|----|---------------|----------------|
| BL-01 | "they have different perspectives" | Names role identity, not code mechanism |
| BL-02 | "they prioritize differently" | Attributes divergence to preference, not property |

This annotation teaches the model the structural principle behind the prohibition, not just the surface form. A model that understands "names role identity, not code mechanism" can generalize to novel perspective-label phrases not in the list. This is strictly stronger than an enumerated list without reasons — the list closes known surface forms; the reason column closes unknown ones. C-13 requires enumeration; V-05 adds reasoning that pushes toward comprehension rather than compliance.

**Signal 2 — Named numbered artifact for cross-run reuse (V-05)**

BL-01 through BL-05 as a named table at the top of the prompt creates a referenceable contract component. The consensus section says "must not match BL-01 through BL-05" and "scan against BL-01 through BL-05" — compact references rather than repeated prose. This pattern generalizes: any prohibition or constraint appearing in multiple sections of a complex prompt can be extracted as a named numbered artifact, maintaining a single source of truth. The AMEND protocol, the technical role IA anchor requirement, and the ban list all gain from ID references when the prompt is long.

**Signal 3 — Explicit incompleteness declaration with scope (V-01, V-05)**

"A technical section with an unfilled IA anchor is **incomplete**" — not "invalid" or "wrong" or "fails the check." Declaring a section incomplete rather than just flagging a missing element is stronger enforcement: incompleteness implies the section cannot be accepted as output, whereas a missing check implies a finding to flag. Both V-01 and V-05 use this language; V-03 uses a template field without the incompleteness declaration, which contributed to its PARTIAL on C-14.

---

## Golden Verdict

**4 of 5 variations pass golden** (V-01, V-03, V-04, V-05).
V-02 fails: C-05 PARTIAL on an essential criterion disqualifies.

V-01 and V-05 represent the ceiling at 100. Their shared pattern — explicit mandatory field + incompleteness declaration + ban list within the consensus production section — fully satisfies C-13 and C-14 simultaneously. V-04 comes within 1 point; its phase-gate C-14 enforcement is architecturally the strongest, but its ban-list placement outside the consensus template block cost it C-13 fully.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["failure-reason annotation per ban phrase — each banned phrase entry includes a structural reason column explaining why the phrase fails (e.g., 'Names role identity, not code mechanism'), enabling a model to generalize the prohibition to novel surface forms beyond the enumerated list", "named numbered artifact for cross-prompt reference — ban list as BL-01..BL-05 table extracted as a first-class protocol component at the top of the prompt, referenced by ID in consensus and technical role sections, creating a single source of truth across a complex multi-section prompt"]}
```
