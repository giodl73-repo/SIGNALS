Reading the R4 scorecard to extract the new excellence patterns.

**R4 patterns:**

1. **V-03 finding**: Cross-surprise field-name uniformity is a distinct check from field completeness (C-13). C-13 enforces every field is populated; V-03's audit additionally enforces that the field names themselves are identical across all surprises. A reader scanning "Design Impact" across the full set finds the same label every time. This is C-15.

2. **V-02 finding**: The portability test is necessary but not sufficient for C-14. Without claim-only voice (C-12), surprises can pass the three-question portability test structurally while remaining hedged observations. "This may suggest X was unexpected" is portable but not an institutional claim. C-14 requires claim authority at the per-surprise level, not just document-level anti-hedging. This is C-16.

**Scoring update**: N goes 7 → 9. Aspirational budget increases to 12 pts. C-15 and C-16 earn 1 pt each (unproven). Proven criteria (C-10, C-11, C-12) stay at 2 pts each.

---

# topic-echo rubric — v4

---

**Two new aspirational criteria added:**

| ID | Name | Origin | Mechanism |
|----|------|--------|-----------|
| C-15 | Cross-surprise schema uniformity | R4, V-03 mechanism finding | Field names are identical across all surprises — same labels, same order, every time |
| C-16 | Per-surprise claim-authority coupling | R4, V-02 C-14 PARTIAL finding | Each surprise individually passes both stranger-reader AND no-hedging tests as a unit |

**Scoring table updated**: Aspirational N goes from 7 → 9. Aspirational budget increases from 10 → 12 pts. C-10, C-11, C-12 (proven by two rounds) earn 2 pts each; C-08, C-09, C-13, C-14, C-15, C-16 earn 1 pt each.

**Key design decision on C-15**: C-15 is aspirational (not recommended) because schema shape is variation-dependent — some echoes use extended schemas, some minimal. C-15 rewards cross-surprise uniformity-within-chosen-schema, not a specific schema shape. It is structurally distinct from C-13: C-13 asks "is every field populated?" while C-15 asks "do all surprises use exactly the same fields?" Both can pass independently; both can fail independently.

**Key design decision on C-16**: C-16 is aspirational because it requires C-12 and C-14 to converge at the per-surprise level, not just document-level. The R4 finding (V-02 PARTIAL) is that portability tests can be structurally satisfied while surprises remain observations rather than institutional claims. C-16 closes this gap by requiring each extracted surprise unit to individually carry authoritative, non-hedged voice. C-16 cannot pass if C-12 fails.

**v4 additions**: Round 4 scoring revealed two structural patterns. V-03 showed that schema uniformity audits catch a property (field-name consistency across surprises) that inline enforcement (V-01) does not address — both achieve C-13 PASS, but the audit-based mechanism surfaces a distinct sub-property worth aspirational credit. V-02 showed that the portability test is a necessary but not sufficient mechanism for C-14 — claim-only voice must co-occur at the per-surprise level, not just at document level. See "Round 4 Excellence Signals" section below.

**v3 additions**: Round 3 scoring revealed two structural patterns that consistently differentiated 100/100 from 94–99. These are codified as C-13 and C-14. See "Round 3 Excellence Signals" section below.

**v2 additions**: Round 1 scoring revealed three mechanisms that consistently differentiated 100/100 outputs from 85/100 outputs. These are codified as C-10, C-11, and C-12. See "Round 1 Excellence Signals" section below.

---

## Essential Criteria

> All must pass for the output to be considered a valid echo.

### C-01 — Surprise focus
- **Weight**: essential
- **Category**: correctness
- **Text**: Every item in the echo is a genuine surprise — something the team did not expect before gathering signals. Items that confirm prior assumptions, restate known requirements, or summarize what was planned do not belong in an echo.
- **Pass condition**: No item could appear unchanged in a standard research summary, findings doc, or project brief. If even one item is an expected finding dressed as a surprise, FAIL.

---

### C-02 — Surprise naming
- **Weight**: essential
- **Category**: format
- **Text**: Each surprise has a named label that captures the essence of the unexpected finding — not a generic header.
- **Pass condition**: Each surprise has a named label (e.g., "The Inverted Adoption Curve", "The Missing Middle", not "Finding 1" or "Surprise A"). Names must be specific to the content. Generic labels FAIL.

---

### C-03 — Signal traceability
- **Weight**: essential
- **Category**: correctness
- **Text**: Each surprise is traced to at least one source signal (namespace, skill, or artifact). The reader can locate where the surprise came from.
- **Pass condition**: Each surprise names its source (e.g., "from scout-feasibility", "surfaced by prove-interview"). Surprises with no traceable source FAIL this criterion.

---

### C-04 — Design impact assessment
- **Weight**: essential
- **Category**: depth
- **Text**: Each surprise includes an explicit assessment of how it changes, challenges, or confirms the design direction. Impact must be stated — not implied.
- **Pass condition**: Each surprise answers "so what for the design?" in at least one sentence. Surprises that describe the finding but omit design consequence FAIL.

---

## Recommended Criteria

> Output is better with these. Do not require for passing, but penalize absence.

### C-05 — Expectation contrast
- **Weight**: recommended
- **Category**: depth
- **Text**: Each surprise articulates what was expected going in, making the contrast explicit. The gap between hypothesis and reality is visible.
- **Pass condition**: At least two-thirds of surprises include a stated prior expectation ("We assumed X, but found Y"). Surprises that only describe the finding without the expected baseline are weaker.

---

### C-06 — Cross-signal synthesis
- **Weight**: recommended
- **Category**: coverage
- **Text**: At least one surprise is synthesized across multiple signals or namespaces — not derived from a single artifact alone. The echo captures something that only became visible when signals were read together.
- **Pass condition**: At least one surprise cites two or more distinct sources and explains why the combination produced the unexpected finding.

---

## Aspirational Criteria

> Criteria that distinguish excellent outputs from good ones. Each earns bonus credit. Budget: 12 pts.

| ID | Name | Points | Status |
|----|------|--------|--------|
| C-07 | Namespace diversity | 1 | Unproven |
| C-08 | Newcomer accessibility | 1 | Unproven |
| C-09 | Pattern recognition | 1 | Unproven |
| C-10 | Counterfactual gate | 2 | Proven (R1+R2) |
| C-11 | Word discipline | 2 | Proven (R1+R2) |
| C-12 | Claim-only voice | 2 | Proven (R1+R2) |
| C-13 | Schema field completeness | 1 | Unproven |
| C-14 | Surprise portability | 1 | Unproven |
| C-15 | Cross-surprise schema uniformity | 1 | Unproven |
| C-16 | Per-surprise claim-authority coupling | 1 | Unproven |

---

### C-07 — Namespace diversity
- **Weight**: aspirational (1 pt)
- **Category**: coverage
- **Text**: Surprises span at least three distinct namespaces. An echo drawing from only one or two namespaces reflects incomplete signal gathering, not genuine convergence.
- **Pass condition**: Source fields across the full surprise set name at least three distinct namespaces.

---

### C-08 — Newcomer accessibility
- **Weight**: aspirational (1 pt)
- **Category**: clarity
- **Text**: Every surprise is comprehensible to a stranger who has never seen the investigation — no project-specific jargon, unexplained acronyms, or implicit context. The echo is self-contained for any reader, not just the team that ran the signals.
- **Pass condition**: A new-hire with no prior exposure to the project reads the echo and understands each surprise without consulting source signals. Surprises that require background knowledge to decode FAIL this criterion.

---

### C-09 — Pattern recognition
- **Weight**: aspirational (1 pt)
- **Category**: synthesis
- **Text**: When two or more surprises share a root cause, the echo surfaces this as an explicit Patterns section. Convergent signals that point to the same underlying dynamic are named together, not left as isolated items.
- **Pass condition**: If any two surprises share a root cause, a Patterns section is present and names the shared dynamic. A single unique surprise set with no shared roots earns this by absence of counterexample.

---

### C-10 — Counterfactual gate
- **Weight**: aspirational (2 pts — proven R1+R2)
- **Category**: rigor
- **Text**: Each surprise passes a counterfactual test: a passive, attentive team tracking the feature would not have found this through normal observation. The finding required active signal gathering to surface. Each surprise schema includes a "Why passive observation missed this" field explaining the mechanism.
- **Pass condition**: Every surprise fails the counterfactual ("a passive team would have missed this"). Every "Why passive observation missed this" field is populated and names the specific mechanism — not a generic explanation. Surprises that could emerge from standard project tracking FAIL.

---

### C-11 — Word discipline
- **Weight**: aspirational (2 pts — proven R1+R2)
- **Category**: concision
- **Text**: Each surprise is stated within 120 words. The full echo is within 800 words. Discipline forces claim extraction over description — a surprise that cannot be stated in 120 words is usually a description, not a claim.
- **Pass condition**: No individual surprise exceeds 120 words (measured from the first schema field through the last). Full echo does not exceed 800 words. Overlong surprises FAIL even if content is otherwise strong.

---

### C-12 — Claim-only voice
- **Weight**: aspirational (2 pts — proven R1+R2)
- **Category**: authority
- **Text**: Every surprise is stated as a claim, not a hedged observation. Prohibited constructs: "may suggest", "appears to indicate", "seems like", "could mean", "it is possible that". Schema fields are labeled and populated as claims ("We found X", "This changes Y", "We assumed Z").
- **Pass condition**: No hedge constructs present anywhere in the echo. Every schema field reads as a direct statement. An echo that qualifies its surprises with uncertainty language FAIL, even if the underlying finding is strong.

---

### C-13 — Schema field completeness
- **Weight**: aspirational (1 pt)
- **Category**: completeness
- **Text**: Every schema field is populated for every surprise — no missing fields, no N/A, no placeholder text. Completeness is measured within the chosen schema: if the variation uses an extended schema, all extended fields must be populated; if minimal, all minimal fields must be populated. The criterion rewards completeness-within-chosen-schema, not a specific schema shape.
- **Pass condition**: Scanning every field of every surprise finds a populated value. Any N/A, blank, or "not applicable" entry FAILS this criterion, regardless of which schema the variation uses.

---

### C-14 — Surprise portability
- **Weight**: aspirational (1 pt)
- **Category**: self-containment
- **Text**: Each surprise stands alone as a self-contained institutional claim for any reader. Extracted individually and shared with someone who has never seen the investigation, the surprise communicates its finding, its unexpectedness, and its design consequence without any surrounding context. Portability requires both context independence (C-08 mechanism) and authoritative voice (C-12 mechanism) — a portable observation is not a portable institutional claim.
- **Pass condition**: Extract any single surprise as a standalone unit. A reader with no project context understands the finding, understands why it was unexpected, and understands what it means for the design — without reading source signals or the rest of the echo. Surprises that depend on surrounding context or are stated in uncertain voice FAIL.

---

### C-15 — Cross-surprise schema uniformity
- **Weight**: aspirational (1 pt)
- **Category**: consistency
- **Text**: All surprises in the echo use exactly the same field names in the same order. The schema shape is uniform across the full set — not just that each field is populated (C-13), but that the field names themselves are identical. A reader scanning any field across the complete surprise set finds the same label in the same position every time. This criterion is structurally distinct from C-13: C-13 asks "is every field populated?"; C-15 asks "do all surprises use exactly the same fields?" Both can pass independently; both can fail independently.
- **Pass condition**: Declare the schema before writing. After writing, audit: for each field name in the schema, read that field across every surprise in sequence. Every surprise uses the declared field names — no renamed fields, no added fields, no omitted fields relative to the declared schema. Any structural divergence between surprises FAILS, even if all fields are populated.

---

### C-16 — Per-surprise claim-authority coupling
- **Weight**: aspirational (1 pt)
- **Category**: authority × self-containment
- **Text**: Each surprise individually passes both the stranger-reader test (C-08 mechanism) and the no-hedging test (C-12 mechanism) as a unit. Document-level anti-hedging and document-level newcomer accessibility are insufficient — each extracted surprise must carry authoritative, non-hedged voice independently. A surprise that passes the portability test structurally ("a stranger can understand the structure") while remaining a hedged observation ("this may suggest X") fails this criterion. C-16 cannot pass if C-12 fails at the document level.
- **Pass condition**: For each surprise individually: (1) a stranger with no project context understands it without reading sources, AND (2) it is stated as a direct claim with no hedge constructs. Apply both tests to each surprise as a standalone unit, not as an aggregate across the echo. Any surprise that passes structural portability but uses uncertain voice FAILS.

---

## Round 4 Excellence Signals

**Signal 1 — Schema uniformity is distinct from schema completeness (V-03)**

V-01 achieves C-13 PASS via inline labeling: each field carries `[required — not N/A]` at write-time with a dedicated field-scan step. V-03 achieves C-13 PASS via a structurally distinct mechanism: a schema contract declared before writing ("Fields applied to every surprise: all required — none optional, none N/A") combined with a Step 6 uniformity audit that reads each field name across every surprise in sequence.

The V-03 audit surfaces a sub-property that V-01's inline mechanism does not address explicitly: cross-surprise field-name consistency. Both variations earn C-13 PASS, but V-03 additionally enforces that surprises cannot diverge structurally even if all fields are populated. The R4 finding: field completeness (C-13) and schema uniformity (C-15) are independent properties. An echo can populate all fields while using inconsistent field names across surprises; an echo can use consistent field names while leaving some fields blank. C-15 codifies the uniformity property as a separate aspirational target.

**Signal 2 — Portability test is necessary but not sufficient for C-14 (V-02)**

V-02 tests whether C-14 can be achieved via an explicit portability test independent of four-mechanism convergence (C-08 + C-10 + C-11 + C-12). Result: C-14 PARTIAL. The portability test — "a reader who has never seen this project reads only this section" — correctly verifies that all three structural components are present (finding, unexpectedness, design consequence) and tests context independence.

However, C-12 FAIL in V-02 means surprises can technically pass the portability test's three structural questions while stated in uncertain voice: "This may suggest X was unexpected" passes the structural test (stranger can parse the structure) but is not an institutional claim. C-14 PASS requires that the extracted unit function as an authoritative institutional claim, not just a portable observation. The R4 finding: portability test + claim-only voice must co-occur at the per-surprise level. Document-level anti-hedging (C-12) is necessary but not sufficient — each surprise must individually carry authoritative voice when extracted as a standalone unit. C-16 codifies this coupling.

---

## Round 3 Excellence Signals

**Signal 1 — Schema field completeness determines ceiling (sourced from V-04, C-10/C-11/C-12 mechanism)**

When all four core mechanism criteria (C-08, C-10, C-11, C-12) are fully present, the remaining differentiator between 94 and 100 is schema completeness. Outputs with populated schema fields across every surprise consistently outscored outputs with N/A or missing fields, even when content quality was otherwise comparable. The R3 finding: field completeness is not a formatting nicety — it is the final mechanism that converts strong-content echoes into full-credit echoes.

**Signal 2 — Surprise portability emerges from four-mechanism convergence (R3-V-05 first 100/100)**

The first 100/100 echo (R3-V-05) was not engineered for portability — portability emerged when C-08 (newcomer framing), C-10 (counterfactual gate), C-11 (word discipline), and C-12 (claim-only voice) converged simultaneously. Single-axis optimization — targeting one mechanism while neglecting others — reliably produced 94–99 but not 100. The R3 finding: surprise portability is a composite property, not an independent mechanism. An echo cannot engineer C-14 directly; it can only create the conditions (C-08 + C-10 + C-11 + C-12 all passing) from which portability follows.

---

## Round 1 Excellence Signals

**Signal 1 — Counterfactual gate separates discoveries from observations (C-10)**

Outputs that reached 100/100 in Round 1 consistently applied an implicit test: would a passive, attentive team have found this anyway? Items that survived this test were qualitatively different — they named mechanisms, not outcomes. Items that failed were often accurate summaries of what happened, not findings about what was hidden. Adding the counterfactual gate as an explicit schema field ("Why passive observation missed this") forced authors to name the mechanism rather than describe the result.

**Signal 2 — Word discipline forces claim extraction (C-11)**

The 120-word per-item cap was initially resisted as arbitrary. Round 1 scoring showed the opposite: overlong surprises were almost always descriptions disguised as findings. Enforcing the cap forced the author to extract the claim, discard the narrative scaffolding, and state the finding directly. The cap is a claim-extraction mechanism, not a length preference.

**Signal 3 — Hedged surprises are not surprises (C-12)**

Outputs using "may suggest", "appears to indicate", and similar constructions scored 10–15 points lower on average than outputs using direct claim voice. The finding: hedging is not epistemic caution — it is the author declining to commit to the finding. An echo that hedges its surprises is not reporting what the signals revealed; it is reporting what the signals might reveal. Claim-only voice is a commitment to the finding, and that commitment is what makes the echo actionable.
