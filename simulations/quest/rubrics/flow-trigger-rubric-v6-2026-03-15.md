**flow-trigger-rubric-v6** written to `simulations/quest/rubrics/flow-trigger-rubric-v6-2026-03-16.md`.

---

**Two new aspirational criteria (C-23–C-24), N_aspirational: 14 → 16, max: 100 → 105:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-23 | Signal 1 — V-01 artifact sequencing | Named ARTIFACT MANIFEST before enumeration assigns reference IDs (ART-NN) to every structural artifact; CLOSURE CHECK resolves counters against manifest IDs rather than scanning for artifact presence — makes closure formally verifiable rather than descriptively asserted | C-20 (CLOSURE CHECK it anchors) |
| C-24 | Signal 2 — V-01 breach markers | Named breach token (`[PROHIBITION BREACH: Role N \| {prohibition}]`) defined alongside PROHIBITION CONTRACTS; inserted inline when a role violates its contract; a reader finds all violations by scanning for the token, without rubric re-evaluation — closes the enforcement asymmetry between compliance (no marker) and violation (marker) | C-21 (prohibition contracts it enforces in the artifact) |

**Structural relationship:** C-23 is the sequencing complement to C-20 — it ensures the artifacts that C-20 counts against were locked before enumeration, making counters resolvable by reference rather than by scan. C-24 is the runtime enforcement complement to C-21 — it ensures that prohibition contracts produce observable signals in the output when violated, not just in the scoring rubric. Together they represent the difference between V-01 and all other Round 8 variations: V-01's artifacts are first-class named objects with citable IDs and breach-visible enforcement; V-03's equivalent structures emerge during execution, which means their closure counters are descriptive and their enforcement is rubric-side only.
