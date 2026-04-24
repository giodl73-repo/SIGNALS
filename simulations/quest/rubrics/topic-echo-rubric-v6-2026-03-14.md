Here is the complete v6 rubric. Summary of changes:

---

**New criteria:**

| ID | Name | Structural relationship |
|----|------|------------------------|
| C-19 | Pre-write composability declaration | C-19 is to C-17 as C-18 is to C-16 — the process-level deliberate commitment layered on top of the output-level property. C-17 can pass via output inspection (V-01, V-03). C-19 requires a manifest declared before writing begins (V-02, V-05). They are orthogonal: V-02 achieves C-19 but fails C-18. |
| C-20 | Gate design integrity | Quality dimension of C-18. Check B in V-03/V-05 was designed as a portability gate from V-05(R4) inception — it exists for criterion enforcement. PGT in V-04 was installed in R6 to fill the C-14 compliance gap C-18 exposed — it exists for rubric compliance. Removing C-20 from the rubric does not change whether Check B exists; it may change whether PGT exists. |

**Promotions:**
- C-17, C-18: 1 pt (unproven) → 2 pts (proven R5+R6). C-17 PASS in all five R6 variations; C-18 PASS in V-03, V-04, V-05.

**Scoring:** N 11→13, base 86→84, budget 14→16. Ceiling 84+16=100.
e each other?" and can be satisfied by output inspection. C-19 asks "was mechanism alignment declared before writing began?" A composability manifest is a pre-write audit artifact — it names all active mechanisms, inspects each pair, and commits to mutual reinforcement before the first word is written. V-02 achieves C-19 (manifest) but fails C-18 (no per-surprise gates), confirming that C-19 is independent of C-18. V-01 and V-03 achieve C-17 PASS from output evidence but lack a manifest, so C-19 FAIL. The criterion cannot pass if C-17 fails — a manifest that declares composability about mechanisms that actually conflict is false evidence.

- **C-20** captures the quality dimension of C-18's gate set. C-18 is a count criterion (3/3 named per-surprise gates). C-20 asks whether each gate was designed as the primary enforcement mechanism for its criterion from the point of gate introduction, or installed after the fact because C-18 requires a gate. The R6 finding: Check B in V-03/V-05 was designed as a portability gate in V-05(R4) — removing C-20 from the rubric does not remove Check B, because Check B serves C-14 enforcement, not C-20 compliance. PGT in V-04 was installed in R6 specifically to fill the C-14 gating gap exposed by C-18 scoring. Removing C-20 from V-04's rubric evaluation would remove the motivation for PGT's existence. A gate that serves its criterion is structurally permanent; a gate that serves a rubric requirement is contingent on that rubric remaining.

**Scoring update**: N goes 11 → 13. C-17 and C-18, confirmed across R5+R6, promoted to 2 pts each (proven). Base adjusted from 86 → 84 to maintain 100-pt ceiling with two new unproven criteria. C-19 and C-20 earn 1 pt each (unproven). Aspirational budget increases to 16 pts.

---

# topic-echo rubric — v6

---

**Two new aspirational criteria added:**

| ID | Name | Origin | Mechanism |
|----|------|--------|-----------|
| C-19 | Pre-write composability declaration | R6, V-02/V-05 manifest finding | The author produces a composability manifest as a discrete pre-write step — names all active mechanisms, inspects each mechanism pair, and commits to mutual reinforcement before writing begins |
| C-20 | Gate design integrity | R6, V-03 vs V-04 gate lineage finding | Every per-surprise gate satisfying C-18 was designed as the primary enforcement mechanism for its criterion from inception — not installed reactively to satisfy C-18's gating requirement |

**Scoring table updated**: N goes from 11 → 13. Base adjusted from 86 → 84. Aspirational budget increases from 14 → 16 pts. C-17 and C-18 promoted to 2 pts each (proven R5+R6). C-19 and C-20 earn 1 pt each (unproven).

**Key design decision on C-19**: C-19 is aspirational because a composability manifest requires intentional pre-write architectural thinking that is absent in most variations. C-19 does not reward the manifest as a formatting artifact — it rewards the manifest as evidence of deliberate composability reasoning before any surprise is written. The R6 finding: V-01 and V-03 achieve C-17 PASS from output inspection (mechanisms observed to reinforce), but produce no manifest. V-02 and V-05 produce a manifest that declares alignment explicitly. Both paths satisfy C-17; only the manifest path satisfies C-19. The relationship to C-17 is precise: C-19 cannot pass if C-17 fails (a manifest that falsely declares composability does not earn the criterion), and C-17 can pass without C-19 (output inspection is sufficient for C-17). C-19 is the process-level complement to C-17's output-level property, following the same structural relationship that C-18 has to C-16.

**Key design decision on C-20**: C-20 is aspirational because gate design integrity requires that the variation's process architecture predate the C-18 rubric requirement — a condition that only variations with deep gate lineage satisfy. C-20 does not reward any particular gate or gate count; it rewards the structural fact that each gate exists for criterion-enforcement reasons, not rubric-compliance reasons. The test: remove C-20 from the rubric. Does each gate still exist? A gate designed to enforce C-14 (Check B) survives — C-14 enforcement motivated it. A gate installed to fill C-18's gating gap (PGT) may not survive — C-18 compliance motivated it. C-20 cannot pass if C-18 fails, because C-18 must be fully satisfied before gate design integrity can be evaluated. A 2/3 gate set that has clean lineage does not satisfy C-20 — the missing gate remains a C-18 failure, and C-20 is not evaluable until all three gates are present.

**v6 additions**: Round 6 scoring confirmed C-17 and C-18 as proven (C-17 PASS in all five R6 variations; C-18 PASS in V-03, V-04, V-05) and revealed two new structural patterns. V-02 and V-05 showed that a composability manifest is a distinct excellence mechanism from output-level composability evidence — C-17 can be satisfied by inspection, but the manifest makes composability intent explicit as a pre-write artifact, creating a deliberate process commitment analogous to C-18's relationship to C-16. The V-03 vs V-04 comparison showed that C-18 PASS has two quality levels: gates designed as primary enforcement mechanisms from inception (Check B, CAT) versus gates installed to fill compliance gaps (PGT). Gate design integrity is a distinct property from gate presence. See "Round 6 Excellence Signals" section below.

**v5 additions**: Round 5 scoring confirmed C-15 and C-16 as proven (both PASS in V-04 and V-05) and revealed two new structural patterns. V-03 showed that mechanism composability is a distinct excellence property — two mechanisms can independently achieve their target criteria while mutually degrading each other in compound configurations. V-04 showed that per-surprise enforcement quality divides into deliberate (named gate, discrete step) and emergent (side effect) — deliberate gating survives variation changes; emergent compliance does not. See "Round 5 Excellence Signals" section below.

**v4 additions**: Round 4 scoring revealed two structural patterns. V-03 showed that schema uniformity audits catch a property (field-name consistency across surprises) that inline enforcement (V-01) does not address — both achieve C-13 PASS, but the audit-based mechanism surfaces a distinct sub-property worth aspirational credit. V-02 showed that the portability test is a necessary but not sufficient mechanism for C-14 — claim-only voice must co-occur at the per-surprise level, not just at document level. See "Round 4 Excellence Signals" section below.

**v3 additions**: Round 3 scoring revealed two structural patterns that consistently differentiated 100/100 from 94-99. These are codified as C-13 and C-14. See "Round 3 Excellence Signals" section below.

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

> Criteria that distinguish excellent outputs from good ones. Each earns bonus credit. Base: 84. Budget: 16 pts.

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
| C-15 | Cross-surprise schema uniformity | 2 | Proven (R4+R5) |
| C-16 | Per-surprise claim-authority coupling | 2 | Proven (R4+R5) |
| C-17 | Mechanism composability | 2 | Proven (R5+R6) |
| C-18 | Deliberate enforcement gating | 2 | Proven (R5+R6) |
| C-19 | Pre-write composability declaration | 1 | Unproven |
| C-20 | Gate design integrity | 1 | Unproven |

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
- **Weight**: aspirational (2 pts — proven R4+R5)
- **Category**: consistency
- **Text**: All surprises in the echo use exactly the same field names in the same order. The schema shape is uniform across the full set — not just that each field is populated (C-13), but that the field names themselves are identical. A reader scanning any field across the complete surprise set finds the same label in the same position every time. This criterion is structurally distinct from C-13: C-13 asks "is every field populated?"; C-15 asks "do all surprises use exactly the same fields?" Both can pass independently; both can fail independently.
- **Pass condition**: Declare the schema before writing. After writing, audit: for each field name in the schema, read that field across every surprise in sequence. Every surprise uses the declared field names — no renamed fields, no added fields, no omitted fields relative to the declared schema. Any structural divergence between surprises FAILS, even if all fields are populated.

---

### C-16 — Per-surprise claim-authority coupling
- **Weight**: aspirational (2 pts — proven R4+R5)
- **Category**: authority x self-containment
- **Text**: Each surprise individually passes both the stranger-reader test (C-08 mechanism) and the no-hedging test (C-12 mechanism) as a unit. Document-level anti-hedging and document-level newcomer accessibility are insufficient — each extracted surprise must carry authoritative, non-hedged voice independently. A surprise that passes the portability test structurally ("a stranger can understand the structure") while remaining a hedged observation ("this may suggest X") fails this criterion. C-16 cannot pass if C-12 fails at the document level.
- **Pass condition**: For each surprise individually: (1) a stranger with no project context understands it without reading sources, AND (2) it is stated as a direct claim with no hedge constructs. Apply both tests to each surprise as a standalone unit, not as an aggregate across the echo. Any surprise that passes structural portability but uses uncertain voice FAILS.

---

### C-17 — Mechanism composability
- **Weight**: aspirational (2 pts — proven R5+R6)
- **Category**: structural coherence
- **Text**: All enforcement mechanisms active in the variation reinforce each other without mutual degradation. In compound configurations — where multiple mechanisms are layered to achieve multiple criteria — no mechanism introduced for one criterion creates structural friction for another. Two mechanisms can each achieve their target criteria in the final output while still failing C-17 if one mechanism constrains the other's effectiveness. Composability is a property of the mechanism combination, not of the criteria achieved.
- **Pass condition**: Inspect every enforcement mechanism in the variation. For each mechanism, verify: does activating this mechanism degrade any other criterion's mechanism, even if the target criterion ultimately passes? Any mechanism that achieves C-X while structurally conflicting with C-Y's enforcement path FAILS this criterion — even if both C-X and C-Y pass in the output. Mutual reinforcement must be present, not just mutual non-interference.

---

### C-18 — Deliberate enforcement gating
- **Weight**: aspirational (2 pts — proven R5+R6)
- **Category**: process intentionality
- **Text**: Each criterion requiring per-surprise enforcement (C-08, C-14, C-16) is enforced via an explicitly named gate that runs as a discrete step in the writing process — not as a side effect of other mechanisms. Compliance is intentional: the author consciously invokes the gate; the criterion cannot fail silently. Emergent compliance — where a per-surprise criterion passes because other mechanisms happen to imply it — does not satisfy this criterion, even if the output would have passed anyway. C-18 cannot pass if C-16 fails, because C-16 is the canonical per-surprise coupling criterion.
- **Pass condition**: For each per-surprise criterion (C-08, C-14, C-16): locate a named, explicitly documented gate in the variation's process — not inferred from output. The gate runs as a distinct step (not embedded as a sub-test within another criterion's enforcement). Any per-surprise criterion whose compliance depends on another mechanism passing rather than on an explicit gate FAILS this criterion.

---

### C-19 — Pre-write composability declaration
- **Weight**: aspirational (1 pt)
- **Category**: structural intentionality
- **Text**: Before writing begins, the author produces a composability manifest as a discrete pre-write step — names every active enforcement mechanism, inspects each mechanism pair, and explicitly commits to mutual reinforcement before the first surprise is written. This converts C-17's output-level property (mechanisms observed to reinforce each other upon inspection) into a process-level commitment: the author has verified and declared alignment before any content is produced. C-19 rewards intentional composability design, not observed composability. C-19 cannot pass if C-17 fails — a manifest that declares composability about mechanisms that actually conflict is false evidence, not a satisfied criterion. C-19 is independent of C-18: producing a manifest does not install per-surprise gates, and installing per-surprise gates does not produce a manifest.
- **Pass condition**: A composability manifest exists as a discrete pre-write artifact: names every active enforcement mechanism in the variation, inspects each mechanism pair, and explicitly declares mutual reinforcement before any surprise writing begins. The manifest must precede the first written surprise — post-hoc composability documentation does not satisfy this criterion. Any active mechanism pair left uninspected in the manifest FAILS. C-17 must pass for C-19 to earn credit.

---

### C-20 — Gate design integrity
- **Weight**: aspirational (1 pt)
- **Category**: process architecture
- **Text**: Every per-surprise gate satisfying C-18 was designed as the primary enforcement mechanism for its criterion from the point of gate introduction — not installed reactively to fill a compliance gap that C-18 exposed. A gate designed to enforce C-14 exists because the variation required per-surprise portability enforcement; a gate installed because C-18 requires a named gate for C-14 exists because the rubric required it. The structural test: removing C-20 from the rubric evaluation does not change whether a gate-design-integrity gate exists, because the gate's motivation is criterion enforcement, not rubric compliance. C-20 cannot pass if C-18 fails — gate design integrity is only evaluable once all three per-surprise gates are present.
- **Pass condition**: For every named gate satisfying C-18: determine whether the gate was designed as the variation's primary mechanism for its criterion, independent of C-18's gating requirement. Evidence: (1) the gate's design rationale names the criterion it enforces, not "to satisfy C-18"; (2) removing C-18 from the rubric would not remove the motivation for the gate's existence. Any gate whose primary design motivation is C-18 compliance rather than per-criterion enforcement FAILS. C-18 must fully pass (3/3 gates) before C-20 is evaluable.

---

## Round 6 Excellence Signals

**Signal 1 — Composability manifest is a distinct excellence mechanism from output-level composability evidence (V-02, V-05)**

R6 reveals that C-17 can be satisfied via two structurally distinct paths. V-01 and V-03 achieve C-17 PASS through output inspection: the inspector examines the active mechanisms, verifies that each mechanism pair reinforces rather than degrades, and finds mutual reinforcement present in the final output. No pre-write artifact is produced; composability is verified retrospectively.

V-02 and V-05 achieve C-17 PASS through a composability manifest: before writing begins, the author names all active mechanisms, inspects each pair, and declares mutual reinforcement as a pre-write commitment. The manifest is then observable as an artifact; V-05's ranking above V-03 (same gate structure, different composability documentation) reflects this additional excellence layer.

The R6 finding: the composability manifest is not merely a documentation mechanism for C-17 — it is a distinct process-level commitment that makes composability intent explicit before any surprise is written. V-02 confirms this independence: V-02 achieves C-19 (manifest present) but fails C-18 (no per-surprise gates added), demonstrating that C-19 and C-18 are orthogonal. C-19 codifies the pre-write declaration property. The relationship mirrors the C-16/C-18 pair exactly: as C-18 is to C-16, C-19 is to C-17.

**Signal 2 — Gate design integrity is a distinct quality dimension of C-18 PASS (V-03 vs V-04)**

R6 confirms C-18 PASS in three variations (V-03, V-04, V-05), but the mechanism quality differs. V-03 achieves C-18 PASS via NGT (new) + Check B (inherited from V-05(R4)) + CAT (inherited from V-05(R5)). Check B was designed as a portability gate at V-05(R4)'s inception — it exists because the V-05 variation required per-surprise portability enforcement. Removing C-20 from V-03's evaluation does not change whether Check B exists.

V-04 achieves C-18 PASS via NGT (new) + PGT (new, installed R6) + CAT (inherited from V-04(R5)). PGT was installed specifically to fill the C-14 gating gap that V-04(R5)'s emergent C-14 compliance left exposed once C-18 was scored. The V-04 scorecard note names this directly: "confirming that V-04(R5)'s C-14 compliance was entirely emergent (no gate at all)." PGT's existence is attributable to C-18 compliance pressure; Check B's existence is attributable to portability enforcement design.

The R6 finding: C-18 PASS has two quality levels — gates designed for criterion enforcement versus gates installed for rubric compliance. Both achieve the gating count; only the former achieves gate design integrity. V-03 ranks above V-04 despite V-04's larger mechanism set (manifest + four per-surprise checks vs. no manifest + three per-surprise checks), partly reflecting this quality distinction. C-20 codifies the gate design integrity property.

---

## Round 5 Excellence Signals

**Signal 1 — Mechanism composability is a distinct excellence property (V-03)**

V-03's tabular schema format achieves C-15 PASS and C-13 PASS via structural mechanisms stronger than V-01's manifest+audit path: row headers prevent field-name drift by construction (C-15), and empty cells are immediately visible during writing (C-13). Structurally, V-03 is locally excellent on these two criteria.

However, V-03 fails C-10 — and the R5 finding explains why: the tabular format risks degrading C-10's "information-dense mechanism explanation" field in compound configurations. The table cell format constrains prose depth. C-15 PASS and C-13 PASS do not imply the combination is compositionally safe. The R5 finding: mechanism composability is a distinct property from criterion achievement. A variation can earn PASS on individual criteria while installing mechanisms that conflict with each other in compound form. C-17 codifies this property — not to reward the absence of conflict, but to reward the presence of mutual reinforcement.

**Signal 2 — Deliberate enforcement is structurally stronger than emergent compliance (V-04)**

V-04(R5) adds the Coupled Authority Test (CAT) to V-04(R4). The V-04(R4) variation already achieved the conditions for C-16 to pass (C-12 PASS, per-surprise voice present, stranger-reader accessible). But C-16 in V-04(R4) was emergent — it arose because four other mechanisms happened to converge, not because a gate was installed for it.

V-04(R5) installs the CAT as a named gate. "C-16 becomes deliberate, not emergent." The structural difference: in V-04(R4), removing C-12 would not surface a C-16 gate failure — the gate does not exist. In V-04(R5), removing C-12 causes the CAT to fail explicitly. Deliberate gating creates a failure surface; emergent compliance does not. The R5 finding: the quality of enforcement (deliberate vs. emergent) is a distinct excellence property from whether the criterion is met. C-18 codifies this property.

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

The first 100/100 echo (R3-V-05) was not engineered for portability — portability emerged when C-08 (newcomer framing), C-10 (counterfactual gate), C-11 (word discipline), and C-12 (claim-only voice) converged simultaneously. Single-axis optimization — targeting one mechanism while neglecting others — reliably produced 94-99 but not 100. The R3 finding: surprise portability is a composite property, not an independent mechanism. An echo cannot engineer C-14 directly; it can only create the conditions (C-08 + C-10 + C-11 + C-12 all passing) from which portability follows.

---

## Round 1 Excellence Signals

**Signal 1 — Counterfactual gate separates discoveries from observations (C-10)**

Outputs that reached 100/100 in Round 1 consistently applied an implicit test: would a passive, attentive team have found this anyway? Items that survived this test were qualitatively different — they named mechanisms, not outcomes. Items that failed were often accurate summaries of what happened, not findings about what was hidden. Adding the counterfactual gate as an explicit schema field ("Why passive observation missed this") forced authors to name the mechanism rather than describe the result.

**Signal 2 — Word discipline forces claim extraction (C-11)**

The 120-word per-item cap was initially resisted as arbitrary. Round 1 scoring showed the opposite: overlong surprises were almost always descriptions disguised as findings. Enforcing the cap forced the author to extract the claim, discard the narrative scaffolding, and state the finding directly. The cap is a claim-extraction mechanism, not a length preference.

**Signal 3 — Hedged surprises are not surprises (C-12)**

Outputs using "may suggest", "appears to indicate", and similar constructions scored 10-15 points lower on average than outputs using direct claim voice. The finding: hedging is not epistemic caution — it is the author declining to commit to the finding. An echo that hedges its surprises is not reporting what the signals revealed; it is reporting what the signals might reveal. Claim-only voice is a commitment to the finding, and that commitment is what makes the echo actionable.
