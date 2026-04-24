Now I have everything I need. Let me score each variation against the rubric.

---

# Quest Score: `topic-echo` — Round 1

**Rubric:** v1 | **Scoring Formula:** `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/2 × 10)`
**PARTIAL counts as 0.5 pass toward formula; FULL PASS required for "all_essential_pass" boolean.**

---

## Scoring Scale

| Tier | Criteria | Max Pts | PASS | PARTIAL | FAIL |
|------|----------|---------|------|---------|------|
| Essential | C-01–C-04 | 60 | 15 ea | 7.5 ea | 0 |
| Recommended | C-05–C-07 | 30 | 10 ea | 5 ea | 0 |
| Aspirational | C-08–C-09 | 10 | 5 ea | 2.5 ea | 0 |

---

## V-01 — Output Format (Sparse Template)

*Mechanism: Minimal slots (Name, Source, Prior Assumption, Finding, Design Impact) + single negative gate rule. "Could this have been written before the signals?" Cross-Signal Pattern block required but unfenced.*

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| **C-01 Surprise Orientation** | PARTIAL | Single embedded negative gate ("could this have been written before the signals?") is present but zero prose explanation of the confirmation/surprise boundary. A model without internalized knowledge of the distinction can rationalize confirmations past this gate. |
| **C-02 Source Signal Tracing** | PASS | Source field is a required slot in the template. Structurally impossible to omit. |
| **C-03 Design Impact Assessment** | PARTIAL | Design Impact field present but no explicit "vague not permitted" prohibition (no counterpart to V-02's "this is worth noting" forbidden list). Sparse template allows "this changes the design" to pass. |
| **C-04 Named and Countable** | PASS | Template requires named entries; Cross-Signal Pattern block structurally implies 2+ surprises preceding it. |
| **C-05 Surprise Diversity** | PARTIAL | Reads across all namespaces implicitly, but no explicit diversity requirement in the slots. Two surprises from the same root cause would not be rejected. |
| **C-06 Future-Team Framing** | PARTIAL | "Zero prose instruction" (per hypothesis) means no future-team register instruction. Field completeness creates standalone readability, but durable register is not instructed. |
| **C-07 Impact Specificity** | PARTIAL | Slot structure creates pressure toward specificity, but without a forbidden-phrase prohibition, vague impact ("this matters for the design") survives. |
| **C-08 Cross-Signal Synthesis** | PARTIAL | Cross-Signal Pattern block required and unfenced. Structure invites synthesis but does not require multi-signal evidence. |
| **C-09 Counterfactual Awareness** | FAIL | No counterfactual slot. |

**Formula:** (3.0/4 × 60) + (1.5/3 × 30) + (0/2 × 10) = **45 + 15 + 0 = 60**

**Band: Bronze** | All essential PASS: **NO** (C-01 PARTIAL, C-03 PARTIAL)

---

## V-02 — Phrasing Register (Formal Two-Condition Definition)

*Mechanism: Explicit two-condition definition, "if in doubt, classify CONFIRMATION" strict dominance, sufficiency check forbids relaxing definition to hit count, forbidden phrase list for Design Impact.*

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| **C-01 Surprise Orientation** | PASS | Strongest definitional enforcement of any variation. Two-condition formal gate + strict dominance rule ("if in doubt → CONFIRMATION") + sufficiency check that explicitly forbids softening the definition to hit the minimum count. Eliminates boundary ambiguity through constraint language. |
| **C-02 Source Signal Tracing** | PASS | Source field required; template structure enforces presence. |
| **C-03 Design Impact Assessment** | PASS | Explicit forbidden phrase list: "Not permitted: 'this is worth noting,' 'this matters,' 'consider this carefully.'" Makes specificity a pass/fail gate on the field itself. |
| **C-04 Named and Countable** | PASS | Sufficiency check prevents relaxing the gate to produce a count, which paradoxically enforces the named-and-countable requirement with higher integrity than a simple "minimum 2" rule. |
| **C-05 Surprise Diversity** | PARTIAL | No explicit namespace or concern-type diversity requirement. Two surprises from the same throttle timing issue would pass. |
| **C-06 Future-Team Framing** | PARTIAL | Technical-precise register is durable (not personal reflection), but no explicit "for the next team" framing instruction. Fields provide standalone completeness but register is formal-definitional, not institutional-memory. |
| **C-07 Impact Specificity** | PASS | Forbidden phrase list makes vague impact structurally disqualifying, not just discouraged. |
| **C-08 Cross-Signal Synthesis** | PARTIAL | Synthesis asks "do the surprises share a root violation of the two-condition definition?" — cross-surprise but not cross-signal. Individual entries are single-signal. |
| **C-09 Counterfactual Awareness** | FAIL | No counterfactual field or instruction. |

**Formula:** (4/4 × 60) + (2/3 × 30) + (0.5/2 × 10) = **60 + 20 + 2.5 = 82.5**

**Band: Gold** | All essential PASS: **YES**

---

## V-03 — Lifecycle Emphasis (Three-Gate, Gate 2 Front-Loaded)

*Mechanism: Gate 1 inventory → Gate 2 full first-person internal monologue challenge (quoted, not abbreviatable) → Gate 3 documentation. Gate 2 carries 60% of instruction weight.*

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| **C-01 Surprise Orientation** | PASS | Gate 2 is the most experientially vivid C-01 enforcement of any variation. The first-person monologue ("I am standing before this investigation began... If someone told me this finding right now, would I be surprised?") is quoted in full with the explicit instruction "do not abbreviate it." The "CONFIRMATION → Release it" path routes to `topic-story`, not to omission. |
| **C-02 Source Signal Tracing** | PASS | Gate 3: "Source: {artifact slug or skill slug. Traceable. Specific.}" — structural requirement with specificity label. |
| **C-03 Design Impact Assessment** | PASS | Gate 3: "Design impact: {the specific component, flow, or decision this forces to change}." |
| **C-04 Named and Countable** | PASS | "You need a minimum of 2 SURPRISE CANDIDATES to proceed." Gate 2 explicitly prevents both under-counting (re-examine if fewer) and over-counting (do not relax the challenge to make the count). |
| **C-05 Surprise Diversity** | PARTIAL | Gate 1 inventories namespaces explicitly (slug + namespace noted per artifact), creating awareness of coverage — but no diversity requirement in Gate 3. |
| **C-06 Future-Team Framing** | PARTIAL | Pattern Note at end asks about root cause/blind spot. No dedicated future-team guidance or register instruction. Entries are complete but not explicitly framed for handoff. |
| **C-07 Impact Specificity** | PASS | "The specific component, flow, or decision this forces to change" — specificity embedded in the field descriptor. |
| **C-08 Cross-Signal Synthesis** | PARTIAL | Pattern Note asks "do the SURPRISE CANDIDATES share a root cause? Reveal the same design blind spot?" — synthesis across surprises but no requirement for individual entries to cite 2+ signals. |
| **C-09 Counterfactual Awareness** | FAIL | No counterfactual instruction across any of the three gates. |

**Formula:** (4/4 × 60) + (2/3 × 30) + (0.5/2 × 10) = **60 + 20 + 2.5 = 82.5**

**Band: Gold** | All essential PASS: **YES**

---

## V-04 — Role Sequence + Lifecycle (Archaeologist → Chronicler)

*Mechanism: Archaeologist surfaces (artifact, investigation question, prior assumption) for every signal before gate runs. Chronicler receives explicit ledger; applies gate against prepared assumptions; writes table with optional Counterfactual field.*

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| **C-01 Surprise Orientation** | PASS | Gate is applied against explicit prior assumptions surfaced by Archaeologist — not self-generated in the moment. The challenge: "Did the signal's finding contradict, substantially extend, or overturn the prior assumption?" Enforcement is structural via role handoff: Chronicler cannot apply the gate without the Archaeologist's work, making the phase non-skippable. |
| **C-02 Source Signal Tracing** | PASS | Chronicler table requires "Source Signal: {artifact slug or skill slug}." |
| **C-03 Design Impact Assessment** | PASS | Chronicler table requires "Design Impact: {specific component, decision, or flow that must change}." |
| **C-04 Named and Countable** | PASS | "You need at least 2 surprises. If fewer survive the gate, flag it — do not produce padding entries." Anti-padding language is the strongest version of this criterion: it prevents low-quality entries from filling the count. |
| **C-05 Surprise Diversity** | PARTIAL | Archaeologist reads "each signal artifact" comprehensively, but no namespace diversity requirement in the output table. |
| **C-06 Future-Team Framing** | PARTIAL | Synthesis section explicitly asks "what do the surprises tell the next team collectively?" — only variation where "next team" appears in the execution prompt. But next-team language is confined to the synthesis; individual table entries are not instructed to use durable register. |
| **C-07 Impact Specificity** | PASS | "Specific component, decision, or flow that must change" — identical specificity framing to V-03. |
| **C-08 Cross-Signal Synthesis** | PARTIAL | Synthesis asks "Is there a shared assumption the design was wrong about?" — cross-surprise synthesis present. Individual entries are one-signal-to-one-assumption. True cross-signal emergent insight is possible but not required. |
| **C-09 Counterfactual Awareness** | PARTIAL | Only variation with an explicit Counterfactual field in the output table: `Counterfactual | {optional — "Without this signal, we would have [specific wrong path]"}`. Optional designation means at least one entry is likely to contain it; full requirement would guarantee it. |

**Formula:** (4/4 × 60) + (2/3 × 30) + (1/2 × 10) = **60 + 20 + 5 = 85**

**Band: Gold** | All essential PASS: **YES**

---

## V-05 — Inertia Framing + Fenced Template

*Mechanism: Labeled wrong-output example + failure mode named ("finding-as-surprise substitution") + fenced code template that structurally excludes narrative. Forbidden additions listed: no introduction, no summary, no narrative between entries.*

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| **C-01 Surprise Orientation** | PASS | Strongest negative-example-based C-01 enforcement. Wrong output is shown, labeled, and dissected — "it buries one genuine surprise in a sentence alongside confirmations." The failure mode is named: "finding-as-surprise substitution." A model can hold this labeled example against its own draft. The fenced code template has no structural slot for confirmation-shaped content. |
| **C-02 Source Signal Tracing** | PASS | Template has `Source: {artifact slug}` as a required field. |
| **C-03 Design Impact Assessment** | PASS | Template has `Consequence: {what specifically changes in the design — name the thing}` — "name the thing" is the clearest impact specificity instruction of any variation. |
| **C-04 Named and Countable** | PASS | "Minimum 2 surprises must survive the prediction test." Template's header-per-surprise structure (`## {Surprise Name}`) enforces named, discrete entries. |
| **C-05 Surprise Diversity** | PARTIAL | "Read the signal artifacts from `simulations/{topic}/` across all namespaces" — explicit namespace coverage in the read instruction, but no output diversity requirement. |
| **C-06 Future-Team Framing** | PARTIAL | Motivation section states "A reader should be able to read the echo and know, in under two minutes, what assumptions to discard before they begin" — future-reader purpose is stated. But execution steps contain no next-team register instruction, and the fenced template has no forward guidance slot. The Pattern block is about clustering, not handoff. |
| **C-07 Impact Specificity** | PASS | `Consequence: {what specifically changes in the design — name the thing}` is the most direct specificity instruction across all 5 variations. |
| **C-08 Cross-Signal Synthesis** | PARTIAL | Pattern block required: "Do the surprises cluster? Name the pattern if yes. State absence if no." — synthesis invoked, but individual `## {Surprise Name}` entries are single-signal. |
| **C-09 Counterfactual Awareness** | FAIL | Fenced template has no Counterfactual field. Forbidden-additions list (no introduction, no summary, no narrative) reduces the surface area where a model might organically add a counterfactual. |

**Formula:** (4/4 × 60) + (2/3 × 30) + (0.5/2 × 10) = **60 + 20 + 2.5 = 82.5**

**Band: Gold** | All essential PASS: **YES**

---

## Rankings

| Rank | Variation | Score | Band | All Essential | Differentiator |
|------|-----------|-------|------|---------------|----------------|
| 1 | **V-04** Archaeologist + Chronicler | **85** | Gold | YES | Only variation with C-09 partial credit (optional Counterfactual field) |
| 2 | **V-02** Formal Two-Condition | **82.5** | Gold | YES | Strongest C-01 definitional precision; C-03 forbidden phrase list |
| 2 | **V-03** Three-Gate | **82.5** | Gold | YES | Strongest C-01 experiential enforcement; first-person monologue |
| 2 | **V-05** Inertia Framing | **82.5** | Gold | YES | Strongest C-01 via negative example; "name the thing" best C-07 |
| 5 | **V-01** Sparse Template | **60** | Bronze | NO | C-01 and C-03 PARTIAL; single gate rule insufficient without boundary explanation |

---

## Excellence Signals from V-04

**Pattern 1 — Assumption pre-surfacing as a distinct phase.**
V-04's Archaeologist produces an explicit (artifact → prior assumption) ledger before any gate runs. This means the Prior Assumption field in the output is *researched and externalized*, not inferred at the moment of writing. Every other variation infers the prior assumption during the gate check, which collapses two cognitively distinct steps into one. Pre-surfacing separates evidence-gathering (Archaeologist) from surprise-testing (Chronicler), improving the accuracy of the assumption that gets written into the entry.

**Pattern 2 — Optional named slots as the minimum viable path to aspirational criteria.**
V-04 achieves C-09 PARTIAL not through a required instruction but through a named optional field: `Counterfactual | {optional — "Without this signal, we would have..."}`. None of the other four variations has any structural hook for counterfactual content. Naming the field and providing the sentence template is the minimal intervention needed to increase C-09 yield — mandatory status would raise the floor but also risk padding.

---

```json
{"top_score": 85, "all_essential_pass": true, "new_patterns": ["assumption pre-surfacing as a distinct role/phase before gate testing separates evidence-gathering from surprise-testing, improving Prior Assumption field accuracy and unlocking counterfactual awareness", "optional named structural slots with sentence-starter templates are the minimum viable intervention for aspirational criteria — sufficient for partial credit without mandating padding"]}
```
