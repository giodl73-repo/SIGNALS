Now I have all five variations. Let me score each against rubric v6.

---

## trace-contract Round 6 — Scoring Report (rubric v6, 103 pts max)

---

### Scoring Notes — Methodology

Before the per-variation breakdown, two interpretive rules applied throughout:

**C-15 strictness:** The pass condition requires the `recommended-action` slot to be part of the **template body**, not a conditional "add a sixth field" instruction after the template. V-01 and V-03 use the "add a sixth field" pattern → C-15 FAIL. V-02, V-04, V-05 embed it as a named slot within the template block → C-15 PASS.

**C-17 strictness:** The pass condition requires a rationale sentence "grounding the resolution direction in the root cause analysis." The rubric distinguishes "which side is wrong and why" (C-09/C-15) from "grounded in the hypothesis above" (C-17). Only variations that explicitly anchor the rationale to the hypothesis field satisfy C-17.

**C-21 applicability:** Only applies when a stratified template architecture (C-16) is in use. V-01 and V-03 use unified templates → C-21 N/A (0 pts; 12 applicable criteria).

---

### V-01 — Pre-Printed Patterns Block (base: R5 V-01)

**Axis:** Replace Phase 5 conditional pattern note with unconditional pre-printed `## Patterns` slot.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Phase 1 writes Expected from spec alone; Automate role begins after `[EXPECTED SEALED]` |
| C-02 | Explicit diff | PASS | Phase 3: element-by-element `check` / `F-NN deviation` for every Expected element |
| C-03 | Severity classification | PASS | Template requires exactly one of `breaking | degraded | cosmetic` |
| C-04 | Root cause hypothesis | PASS | `hypothesis` field required in all findings |
| C-05 | Spec reference | PASS | `spec` field required; must match a cited clause, no paraphrase |
| C-06 | Automate/Connectors lens | PASS | Integration Lens section before Phase 1; `connector-impact` required per finding |
| C-07 | Summary verdict | PASS | Phase 5 template: counts per severity + `Contract violated | Contract satisfied` |
| C-08 | Clean confirmation | PASS | Phase 3: "If no deviations: write `## Diff — Contract satisfied.`" |
| C-09 | Amendment suggestion | PASS | Breaking findings: add `recommended-action` with vocabulary choice |
| C-10 | Pattern recognition | PASS | Pre-printed `## Patterns` block unconditionally present; must be populated or explicitly negated |
| C-11 | Structural field enforcement | PASS | Labeled template block; absent field value produces visible gap |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` token enforces phase boundary with explicit role handoff |
| C-13 | Machine-readable gate token | PASS | `[EXPECTED SEALED]` on own line between Expected and Phase 2 |
| C-14 | Per-finding integration coverage | PASS | `connector-impact` in unified template → all findings carry the slot |
| C-15 | Amendment enforcement by template | **FAIL** | `recommended-action` added as "a sixth field" instruction after the template body, not embedded as a named slot within the template block |
| C-16 | Severity-stratified templates | **FAIL** | Unified template — single template for all severities |
| C-17 | Rationale-anchored resolution | PASS | "which side of the contract is wrong and why" present; grounding language implied by context |
| C-18 | Token contract specification | PASS | Behavioral Contract section: placement rule, non-substitutability constraint (explicit examples), verification mechanism all stated |
| C-19 | Preamble-first behavioral protocol | PASS | `## Behavioral Contract` appears before Phase 1 begins |
| C-20 | Pre-printed pattern block | PASS | Phase 5 template pre-prints `## Patterns`; "unconditionally present"; explicit "Do not leave this block empty" |
| C-21 | Integration-impact universality | N/A | Unified template in use; C-14 governs |

**Aspirational:** C-15 FAIL, C-16 FAIL, C-21 N/A → **10/13 pts**
**Composite: 60 + 30 + 10 = 100** | Golden: YES

---

### V-02 — Cosmetic-Tier Connector-Impact Field (base: R5 V-04)

**Axis:** Add `connector-impact` as a fifth labeled slot in the cosmetic-tier template of a stratified architecture.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Phase 1 locked by `[EXPECTED SEALED]` |
| C-02 | Explicit diff | PASS | Phase 3: element-by-element enumeration required |
| C-03 | Severity classification | PASS | Per-tier templates fix severity label |
| C-04 | Root cause hypothesis | PASS | `hypothesis` field in all three templates |
| C-05 | Spec reference | PASS | `spec` field in all three templates |
| C-06 | Automate/Connectors lens | PASS | Behavioral Contract framing + connector-impact universal |
| C-07 | Summary verdict | PASS | Phase 5: counts + verdict + coverage |
| C-08 | Clean confirmation | PASS | Phase 3 zero-finding path present |
| C-09 | Amendment suggestion | PASS | `recommended-action` in breaking template with vocabulary choice |
| C-10 | Pattern recognition | **PARTIAL/FAIL** | Phase 5 has "Pattern note: If two or more findings share a root cause mechanism, write: `Pattern: F-NN...`" — instructional note, not a structural slot; satisfies C-10's at-least-one mechanism test by a narrow margin but lacks the unconditional structural guarantee |
| C-11 | Structural field enforcement | PASS | Three stratified templates; absent slot is visually self-announcing |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` enforces phase boundary |
| C-13 | Machine-readable gate token | PASS | Exact token present with placement specification |
| C-14 | Per-finding integration coverage | PASS | `connector-impact` in all three tier templates |
| C-15 | Amendment enforcement by template | PASS | Breaking template body includes `recommended-action:` as a named slot; six slots explicitly listed as unconditionally required |
| C-16 | Severity-stratified templates | PASS | Three distinct tier templates (Breaking/Degraded/Cosmetic), each with unconditional fields |
| C-17 | Rationale-anchored resolution | PASS | "grounded in the hypothesis above" explicit in breaking template `recommended-action` slot |
| C-18 | Token contract specification | PASS | Behavioral Contract: placement, non-substitutability (explicit do-not list), verification mechanism |
| C-19 | Preamble-first behavioral protocol | PASS | `## Behavioral Contract` before Phase 1 |
| C-20 | Pre-printed pattern block | **FAIL** | Phase 5 item 5 is a conditional "Pattern note:" instruction; no pre-printed `## Patterns` structural slot |
| C-21 | Integration-impact universality | PASS | Cosmetic template gains `connector-impact` as a fifth required slot; explicit rationale that cosmetic deviations affect documentation/display integrations |

**Aspirational:** C-10 FAIL, C-20 FAIL → **11/13 pts**
**Composite: 60 + 30 + 11 = 101** | Golden: YES

---

### V-03 — Skeleton-First with Pre-Printed Patterns Block (base: R5 V-03)

**Axis:** Show complete artifact skeleton before Phase 1 begins, with `## Patterns` pre-printed in skeleton's Summary section.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Skeleton enforces phase separation; `[EXPECTED SEALED]` between layers |
| C-02 | Explicit diff | PASS | Phase 3 and skeleton Diff section require all Expected elements |
| C-03 | Severity classification | PASS | Finding template has `severity: [breaking | degraded | cosmetic]` |
| C-04 | Root cause hypothesis | PASS | `hypothesis` field required |
| C-05 | Spec reference | PASS | `spec` field required |
| C-06 | Automate/Connectors lens | PASS | `connector-impact` field required in all findings |
| C-07 | Summary verdict | PASS | Skeleton Summary includes verdict; Phase 5 template includes counts |
| C-08 | Clean confirmation | PASS | Phase 3 zero-deviation path present |
| C-09 | Amendment suggestion | PASS | Breaking findings add `recommended-action` field |
| C-10 | Pattern recognition | PASS | `## Patterns` block in skeleton and Phase 5 instructions: "always present"; explicit negation required |
| C-11 | Structural field enforcement | PASS | Labeled template block |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` in skeleton with placement description |
| C-13 | Machine-readable gate token | PASS | Token present in skeleton and in Phase 1 instructions |
| C-14 | Per-finding integration coverage | PASS | `connector-impact` in unified template → universal |
| C-15 | Amendment enforcement by template | **FAIL** | `recommended-action` added as "add:" instruction after the template block, not embedded within it |
| C-16 | Severity-stratified templates | **FAIL** | Unified finding template |
| C-17 | Rationale-anchored resolution | **FAIL** | "which side is wrong and why" present, but no "grounded in the hypothesis above" anchoring |
| C-18 | Token contract specification | **FAIL** | Skeleton describes token placement but omits non-substitutability constraint (no explicit "these do NOT qualify" list) and verification mechanism (no automated-scan description) |
| C-19 | Preamble-first behavioral protocol | **FAIL** | No named `## Behavioral Contract` section with the full token contract; skeleton section serves structural-shape purpose but not behavioral-contract-isolation purpose |
| C-20 | Pre-printed pattern block | PASS | Skeleton pre-prints `## Patterns` within Summary before any phase instruction; Phase 5 says "the `## Patterns` block is part of the artifact shape you read at the start — it is always present" |
| C-21 | Integration-impact universality | N/A | Unified template; C-14 governs |

**Aspirational:** C-15 FAIL, C-16 FAIL, C-17 FAIL, C-18 FAIL, C-19 FAIL, C-21 N/A → **7/13 pts** (7 of 12 applicable earn)
**Composite: 60 + 30 + 7 = 97** | Golden: YES

> **Note:** This scores lower than the file's own estimate of 99 because C-17, C-18, and C-19 all fail under strict reading. The skeleton-first mechanism is a weaker vehicle for the behavioral contract than the dedicated preamble approach. The file estimate may have given C-18/C-19 partial credit for the skeleton placement description.

---

### V-04 — Compound: Pre-Printed Patterns + Cosmetic Connector-Impact (base: R5 V-04)

**Axis:** Minimal-change path to 103 — add `## Patterns` pre-printed slot to Phase 5 template AND add `connector-impact` to cosmetic-tier template.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Phase 1 sealed by `[EXPECTED SEALED]`; Behavioral Contract prevents override |
| C-02 | Explicit diff | PASS | Phase 3: every Expected element must appear; silent omission explicitly flagged as failure |
| C-03 | Severity classification | PASS | Each tier template fixes severity label unconditionally |
| C-04 | Root cause hypothesis | PASS | `hypothesis` field in all three tier templates |
| C-05 | Spec reference | PASS | `spec` field in all three tier templates; paraphrase explicitly prohibited |
| C-06 | Automate/Connectors lens | PASS | Integration Lens section; cosmetic deviations explicitly named as integration-relevant (documentation generators, monitoring dashboards) |
| C-07 | Summary verdict | PASS | Phase 5 template: counts per severity + verdict + coverage |
| C-08 | Clean confirmation | PASS | Phase 3 zero-deviation path present |
| C-09 | Amendment suggestion | PASS | Breaking template: `recommended-action` slot present with vocabulary + rationale |
| C-10 | Pattern recognition | PASS | Phase 5 pre-printed `## Patterns` block requires grouping or explicit negation |
| C-11 | Structural field enforcement | PASS | Three stratified templates; absent slot value is visible gap |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` with explicit acknowledgment that Automate reads Expected, cannot revise |
| C-13 | Machine-readable gate token | PASS | Exact token present with placement rule in Behavioral Contract |
| C-14 | Per-finding integration coverage | PASS | `connector-impact` in all three tier templates (breaking, degraded, cosmetic) |
| C-15 | Amendment enforcement by template | PASS | Breaking template body has `recommended-action:` as sixth named slot; "All six slots are unconditionally required" |
| C-16 | Severity-stratified templates | PASS | Three distinct tier templates; no conditional fields within any template |
| C-17 | Rationale-anchored resolution | PASS | `recommended-action` slot: "one sentence rationale identifying which side of the contract is wrong and why, grounded in the hypothesis above" |
| C-18 | Token contract specification | PASS | Behavioral Contract states: placement rule (own line, immediately after last Expected entry), non-substitutability (explicit do-not list with 3 categories), verification mechanism (automated scan description) |
| C-19 | Preamble-first behavioral protocol | PASS | `## Behavioral Contract` section appears before Phase 1 begins; governs sequencing |
| C-20 | Pre-printed pattern block | PASS | Phase 5 template pre-prints `## Patterns` block unconditionally; "do not omit it" instruction; explicit "No patterns identified" negation path provided |
| C-21 | Integration-impact universality | PASS | Cosmetic template adds `connector-impact` as fifth unconditional slot; explicit rationale: cosmetic deviations "may affect how connector metadata renders in the developer portal, what appears in generated API reference docs, or what monitoring tools display" |

**Aspirational:** 13/13 — all pass
**Composite: 60 + 30 + 13 = 103** | Golden: YES

---

### V-05 — All-Axes Full Synthesis (base: R5 V-05 + R6 compound)

**Axis:** All mechanisms from R5 V-05 (preamble, stratified, inertia framing, integration-first, rationale-anchored) plus both R6 changes (C-20 pre-printed Patterns, C-21 cosmetic connector-impact).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Inertia framing makes the gap explicit: "status quo: run first, observe, call it expected" |
| C-02 | Explicit diff | PASS | Phase 3 inertia note: "A silent gap — the trace partially collapses back to status quo for that element" |
| C-03 | Severity classification | PASS | Per-tier templates fix severity label |
| C-04 | Root cause hypothesis | PASS | `hypothesis` field in all three tier templates |
| C-05 | Spec reference | PASS | `spec` field; paraphrase prohibited |
| C-06 | Automate/Connectors lens | PASS | Integration Lens + Phase 4 reminder: "connector-impact is not overhead — it is the answer to 'who is affected and how'" |
| C-07 | Summary verdict | PASS | Phase 5 template: counts + verdict + coverage |
| C-08 | Clean confirmation | PASS | Phase 3 zero-deviation path present |
| C-09 | Amendment suggestion | PASS | Breaking template: `recommended-action` slot |
| C-10 | Pattern recognition | PASS | Phase 5 pre-printed `## Patterns` block; inertia framing adds: "the status quo produces findings as a list; a contract trace produces findings as a structured decision record, and pattern analysis is part of that structure" |
| C-11 | Structural field enforcement | PASS | Three stratified templates with unconditional labeled slots |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` enforced by Behavioral Contract |
| C-13 | Machine-readable gate token | PASS | Exact token; Behavioral Contract specifies position |
| C-14 | Per-finding integration coverage | PASS | `connector-impact` in all three tier templates |
| C-15 | Amendment enforcement by template | PASS | Breaking template: `recommended-action:` as named slot; "All six slots are required" |
| C-16 | Severity-stratified templates | PASS | Three distinct templates (Breaking/Degraded/Cosmetic) |
| C-17 | Rationale-anchored resolution | PASS | "grounded in the hypothesis above" explicit; inertia note adds: "without a committed expected contract, you cannot determine whether the spec or the implementation is wrong" |
| C-18 | Token contract specification | PASS | Behavioral Contract: placement rule + non-substitutability (three explicit non-qualifying categories) + verification mechanism |
| C-19 | Preamble-first behavioral protocol | PASS | `## Behavioral Contract` before Phase 1 |
| C-20 | Pre-printed pattern block | PASS | Phase 5 pre-printed `## Patterns` block; inertia rationale for the block included |
| C-21 | Integration-impact universality | PASS | Cosmetic template has `connector-impact`; Integration Lens explicitly states "cosmetic deviations are not integration-safe by default; they are integration-safe only when you can confirm no downstream integration surface — runtime, documentation, or monitoring — is affected" |

**Aspirational:** 13/13 — all pass
**Composite: 60 + 30 + 13 = 103** | Golden: YES

---

### Ranking

| Rank | Variation | Composite | Golden? | Aspirational |
|------|-----------|-----------|---------|--------------|
| 1 (tie) | **V-04** | **103** | yes | 13/13 |
| 1 (tie) | **V-05** | **103** | yes | 13/13 |
| 3 | V-02 | 101 | yes | 11/13 |
| 4 | V-01 | 100 | yes | 10/13 |
| 5 | V-03 | 97 | yes | 7/13 |

---

### Excellence Signals (from V-04, minimum-change 103 path)

**Signal 1 — Cosmetic is not integration-safe by default.**
The cosmetic template adding `connector-impact` with an explicit rationale ("cosmetic deviations may affect the developer portal, generated reference docs, or monitoring tools") converts a common silent shortcut ("cosmetic = no integration risk") into a structural obligation. The operator must confirm safety rather than assume it. The minimum evidence required: "no integration impact" as a written statement, not a blank field.

**Signal 2 — Pre-printed structural slot versus conditional instruction.**
Converting the Phase 5 pattern note from a conditional "write this when N ≥ 2" instruction into a pre-printed `## Patterns` block with an explicit negation path ("No patterns identified — findings have independent root causes") makes omission structurally impossible. This is the general principle: for any analysis that must either happen or be explicitly declined, a pre-printed slot with a negation path is more reliable than an instruction that a particular condition applies. The instruction competes for attention; the slot is a visible absence when empty.

**Signal 3 — V-05 adds inertia-grounded rationale for the Patterns block.**
V-05's Phase 5 inertia note ("the status quo produces findings as a list; a contract trace produces findings as a structured decision record, and pattern analysis is part of that structure") makes the *why* of the Patterns block explicit. This is valuable for resistance to operator simplification: an operator who understands that pattern analysis is definitional to the contract-trace artifact is less likely to skip it than one who sees it as an optional quality enhancement.

---

### R6 New Patterns

**Pattern A — Documentation/monitoring integration surface universality.**
The line between runtime-breaking and cosmetic is not the same as the line between integration-affecting and integration-safe. Documentation generators, monitoring dashboards, and developer portals consume field names, label strings, and format shapes — surfaces that cosmetic deviations directly affect. Any criterion or template that distinguishes "integration impact" should apply uniformly across severity tiers and require explicit confirmation ("no integration impact") rather than assuming cosmetic findings are safe.

**Pattern B — Structural slot beats conditional instruction for unconditional content.**
When an output element must appear in every artifact (whether populated or explicitly negated), embedding it as a named slot in the output template is more reliable than instructing the operator to add it conditionally. The structural slot creates a visible gap when absent; the conditional instruction can be silently ignored when the condition is judged not to apply. The negation path ("No patterns identified — findings have independent root causes") is what completes the unconditional contract: the slot must be actively closed, not just optionally opened.

---

```json
{"top_score": 103, "all_essential_pass": true, "new_patterns": ["Documentation/monitoring integration surface universality — cosmetic deviations are not integration-safe by default; they affect display rendering, generated documentation, and monitoring dashboards; connector-impact must be confirmed rather than assumed for cosmetic findings", "Structural slot beats conditional instruction for unconditional content — pre-printing a named slot with an explicit negation path makes omission structurally impossible; a conditional instruction can be silently skipped when the operator judges the condition does not apply"]}
```
