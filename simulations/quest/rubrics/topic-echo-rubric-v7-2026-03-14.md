Here is the complete v7 rubric. Summary of changes:

---

**New criteria:**

| ID | Name | Structural relationship |
|----|------|------------------------|
| C-21 | Composability manifest causal depth | C-21 is to C-19 as C-20 is to C-18 — the quality dimension of the pre-write pair inspection. C-19 requires that pairs be inspected and mutual reinforcement declared. C-21 requires that each inspection articulate the directional causal mechanism, not just the conclusion. V-04(R7) demonstrates it: "NGT prerequisite for Check B," "structural portability prerequisite for coupled authority." |
| C-22 | Gate provenance traceability | C-22 is to C-20 as causal depth is to pair inspection — the verifiability dimension of gate motivation evidence. C-20 requires the structural removal test to be passed. C-22 requires the motivation claim to be backed by named round history: "introduced in V-05(R4)." V-04(R7) demonstrates it; V-05(R7) demonstrates the failure case (PGT's provenance confirms reactive motivation). |

**Promotions:**
- C-19, C-20: 1 pt (unproven) → 2 pts (proven R6+R7). C-19 PASS in V-04 and V-05 of R7; C-20 PASS in V-02 and V-04 of R7.

**Scoring:** N 13→15, base 84→82, budget 16→18. Ceiling 82+18=100.

---

**Key structural logic of C-21 and C-22:**

C-21 emerges from R7 Signals 1+2 combined. V-03 proved enumeration is insufficient for C-19; V-04 showed what sufficient inspection looks like. The gap between "pairs inspected" (C-19) and "causal direction stated" (C-21) is exactly the gap between "fields populated" (C-13) and "fields consistent" (C-15) — the stronger criterion doesn't replace the weaker one; it asks a more precise question about the same artifact.

C-22 emerges from R7 Signal 3. V-05's honest PGT rationale caused C-20 FAIL — and V-04's rationale shows what earns both C-20 and C-22: the same documentation that passes the structural removal test also names the round of introduction, making the motivation claim verifiable from history rather than merely asserted. Honesty of documentation is irrelevant to C-20; specificity of provenance is what C-22 rewards.
A establishes the property that B enforces" satisfies C-21. The causal statement is verifiable and generative: it predicts whether the pair would reinforce in novel compound configurations, not just in the current one. C-21 cannot pass if C-19 fails — causal depth requires that inspection occur at all.

- **C-22** captures the verifiability dimension of C-20's motivation claim. C-20 requires that each gate satisfying C-18 carry explicit rationale naming its criterion and passing the structural removal test. C-22 asks whether that rationale is backed by verifiable history — naming the variation and round where the gate was introduced. V-04(R7) demonstrated this: "Check B enforces per-surprise portability (C-14)... introduced in V-05(R4) as the primary mechanism." The round reference (V-05, R4) is an externally verifiable fact: C-18 did not exist in R4, so Check B's introduction predates the rubric criterion it would later satisfy under C-18. This converts motivation from an asserted property to a documented historical claim. V-05(R7) also demonstrated the failure case: PGT's rationale honestly documented its introduction in V-04(R6) specifically to fill a C-18 compliance gap — provenance traceability caused C-20 FAIL, not saved it. C-22 cannot pass if C-20 fails — provenance documentation is only meaningful once motivation integrity is established.

**Scoring update**: N goes 13 → 15. C-19 and C-20, confirmed across R6+R7, promoted to 2 pts each (proven). Base adjusted from 84 → 82 to maintain 100-pt ceiling with two new unproven criteria. C-21 and C-22 earn 1 pt each (unproven). Aspirational budget increases to 18 pts.

**v7 additions**: Round 7 scoring confirmed C-19 and C-20 as proven (C-19 PASS in V-04 and V-05; C-20 PASS in V-02 and V-04) and revealed two new structural patterns. V-04 showed that composability manifest pair inspections have a quality dimension: inspections that state the directional causal relationship between mechanisms ("A is a prerequisite for B") are structurally stronger than inspections that assert reinforcement without mechanism — the causal statement predicts composability in unseen configurations. V-04 and V-05 showed that gate motivation claims are verifiable from round history: a gate rationale that names the specific variation and round of introduction converts the structural removal test from a logical assertion to a historical fact. See "Round 7 Excellence Signals" section below.

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

> Criteria that distinguish excellent outputs from good ones. Each earns bonus credit. Base: 82. Budget: 18 pts.

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
| C-19 | Pre-write composability declaration | 2 | Proven (R6+R7) |
| C-20 | Gate design integrity | 2 | Proven (R6+R7) |
| C-21 | Composability manifest causal depth | 1 | Unproven |
| C-22 | Gate provenance traceability | 1 | Unproven |

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
- **Weight**: aspirational (2 pts — proven R6+R7)
- **Category**: structural intentionality
- **Text**: Before writing begins, the author produces a composability manifest as a discrete pre-write step — names every active enforcement mechanism, inspects each mechanism pair, and explicitly commits to mutual reinforcement before the first surprise is written. This converts C-17's output-level property (mechanisms observed to reinforce each other upon inspection) into a process-level commitment: the author has verified and declared alignment before any content is produced. C-19 rewards intentional composability design, not observed composability. C-19 cannot pass if C-17 fails — a manifest that declares composability about mechanisms that actually conflict is false evidence, not a satisfied criterion. C-19 is independent of C-18: producing a manifest does not install per-surprise gates, and installing per-surprise gates does not produce a manifest.
- **Pass condition**: A composability manifest exists as a discrete pre-write artifact: names every active enforcement mechanism in the variation, inspects each mechanism pair, and explicitly declares mutual reinforcement before any surprise writing begins. The manifest must precede the first written surprise — post-hoc composability documentation does not satisfy this criterion. Any active mechanism pair left uninspected in the manifest FAILS. C-17 must pass for C-19 to earn credit.

---

### C-20 — Gate design integrity
- **Weight**: aspirational (2 pts — proven R6+R7)
- **Category**: process architecture
- **Text**: Every per-surprise gate satisfying C-18 was designed as the primary enforcement mechanism for its criterion from the point of gate introduction — not installed reactively to fill a compliance gap that C-18 exposed. A gate designed to enforce C-14 exists because the variation required per-surprise portability enforcement; a gate installed because C-18 requires a named gate for C-14 exists because the rubric required it. The structural test: removing C-20 from the rubric evaluation does not change whether a gate-design-integrity gate exists, because the gate's motivation is criterion enforcement, not rubric compliance. C-20 cannot pass if C-18 fails — gate design integrity is only evaluable once all three per-surprise gates are present.
- **Pass condition**: For every named gate satisfying C-18: determine whether the gate was designed as the variation's primary mechanism for its criterion, independent of C-18's gating requirement. Evidence: (1) the gate's design rationale names the criterion it enforces, not "to satisfy C-18"; (2) removing C-18 from the rubric would not remove the motivation for the gate's existence. Any gate whose primary design motivation is C-18 compliance rather than per-criterion enforcement FAILS. C-18 must fully pass (3/3 gates) before C-20 is evaluable.

---

### C-21 — Composability manifest causal depth
- **Weight**: aspirational (1 pt)
- **Category**: structural analysis
- **Text**: Each pair inspection in the composability manifest (satisfying C-19) articulates the directional causal relationship of reinforcement — not merely asserting "A and B reinforce each other" but naming the causal mechanism: "A is a prerequisite for B," "A establishes the property that B enforces," "A and B target the same sub-property from complementary angles," or "A amplifies B's enforcement per-surprise." A conclusion-assertion pair inspection ("these reinforce") satisfies C-19; a causal-mechanism pair inspection ("these reinforce because A's output is B's required input") satisfies C-21. Causal depth makes the inspection generative: the stated mechanism predicts whether the pair would reinforce in novel compound configurations, not just in the current one. C-21 cannot pass if C-19 fails — causal depth requires that pair inspection occur at all.
- **Pass condition**: For each pair inspection in the composability manifest: locate an explicit statement of the causal mechanism of reinforcement — not just the conclusion. The causal statement must be specific enough that an external evaluator could predict the pair's behavior in a novel mechanism combination. Any pair that is inspected but whose analysis is limited to a reinforcement conclusion ("A and B reinforce") without a causal mechanism FAILS. C-19 must pass for C-21 to be evaluable.

---

### C-22 — Gate provenance traceability
- **Weight**: aspirational (1 pt)
- **Category**: motivation verifiability
- **Text**: For each gate satisfying C-20 (criterion-motivated design), the gate rationale names the specific variation and round in which the gate was introduced — making the motivation claim verifiable from round history rather than asserted from current-round documentation alone. A gate introduced before its associated rubric criterion existed (e.g., Check B introduced in V-05(R4) before C-18 was written) carries provenance-backed criterion-enforcement motivation: the timeline confirms the gate was not installed for rubric compliance. A gate introduced specifically to satisfy a rubric gap (e.g., PGT introduced in V-04(R6) to fill C-18's requirement) carries provenance-backed compliance motivation: the timeline confirms the reactive motivation. Provenance traceability converts the C-20 structural removal test from a logical claim to a documentarily verifiable historical fact. C-22 cannot pass if C-20 fails — provenance documentation is only meaningful once motivation integrity is established.
- **Pass condition**: For every named gate satisfying C-20: the gate rationale identifies the specific variation and round of introduction (e.g., "introduced in V-05(R4)"). This reference must be accurate — verifiable against the variation's history — and must enable an evaluator to determine whether the gate predates or postdates the C-18 rubric criterion. Any gate whose rationale names the criterion enforced and passes the structural removal test (C-20) but omits round provenance FAILS C-22. C-20 must fully pass before C-22 is evaluable.

---

## Round 7 Excellence Signals

**Signal 1 — C-19 has two independent failure dimensions: timing and inspection completeness (V-01, V-03)**

R7 reveals that C-19 can fail on either of two independent axes. V-01 demonstrates the timing failure: the composability audit is structurally complete (all 11 mechanisms named, each pair inspected, mutual reinforcement declared) but is placed after writing. C-19's temporal requirement is not a formalism — it is the structural property that distinguishes a pre-write commitment from a post-write record. A pre-write manifest commits to what mechanisms will do before any content is produced; a post-write audit records what mechanisms did. Only the former is a process-level commitment; the latter is retrospective documentation. The symmetry with C-18 is exact: C-18 requires gates to run during writing; C-19 requires the manifest to precede writing. Both criteria care about when in the process an action occurs, not just that it occurs at all.

V-03 demonstrates the content failure: the manifest is correctly placed (pre-write) but contains only mechanism enumeration — listing all 11 active mechanisms without inspecting any pair. Enumeration establishes awareness; inspection establishes commitment. An author who enumerates mechanisms knows what tools they are using; an author who inspects each pair has committed to their joint behavior. The distinction parallels C-13 (fields populated) vs. C-15 (fields consistent across surprises): enumeration is a prerequisite for the stronger property but does not satisfy it. C-19's pass condition requires three sequential acts — naming, inspecting, and declaring mutual reinforcement — and V-03 satisfies only the first.

V-04 and V-05 pass C-19 by satisfying all three acts with correct timing. V-04's pair inspections additionally demonstrate causal depth (Signal 1 → C-21): "NGT prerequisite for Check B," "structural portability prerequisite for coupled authority." These are not reinforcement conclusions — they are directional causal claims. Naming the causal mechanism makes the inspection generative: it predicts composability in configurations not yet tested. This quality dimension of C-19's pair inspection is not captured by C-19 itself, which requires inspection but not causal articulation.

**Signal 2 — Gate motivation is fixed at inception and immune to retroactive documentation; provenance names the historical fact (V-04, V-05)**

R7 provides the definitive C-20 boundary test via V-05. PGT was installed in V-04(R6) specifically to fill the C-14 gating gap that C-18 scoring exposed — V-04(R5)'s C-14 compliance was entirely emergent. V-05(R7) documents PGT's reactive origin with complete honesty: "PGT was added to satisfy C-18's requirement for a named C-14 gate, not because the variation's C-14 enforcement philosophy demanded a new gate." This documentation is accurate; it is also a C-20 FAIL. Gate motivation is a structural fact determined at the moment of introduction and unalterable by subsequent description. Honest documentation does not improve gate design integrity; it accurately records the absence of it.

V-04(R7) demonstrates the clean path and its quality elevation. All three gates carry complete dual-evidence rationale. Critically, V-04's rationale goes beyond asserting clean motivation to naming round provenance: "Check B: introduced in V-05(R4) as the primary mechanism." This round reference is externally verifiable — C-18 was introduced in v6 (after R5), so a gate introduced in R4 demonstrably predates the rubric criterion it would later satisfy. Provenance converts motivation from a logical assertion into a historical fact. V-05 also demonstrates provenance traceability — but in the failure direction: PGT introduced in V-04(R6), with C-18 existing since v6 (introduced at the R5+R6 boundary). The timeline confirms reactive motivation. Provenance documentation reveals gate motivation whether the motivation is clean or reactive; the motivation determines C-20; provenance determines C-22. C-22 codifies the verifiability property.

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
