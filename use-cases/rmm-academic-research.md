# Use Case: Academic Research Pipeline
## The Resonance Merge Model Program

**Domain:** Formal academic publication — theoretical physics/social science
**Duration:** 2 days (2026-03-19 to 2026-03-20)
**Papers processed:** P01 (recheck 3.1/4), P01b (recheck 3.3/4), P02 (recheck 3.3/4), P03 (pipeline in progress)
**Target journals:** Journal of Consciousness Studies, Journal of Theoretical Biology, Complexity
**Author:** Giovanni della-Libera
**Signal install:** flat binding (62 skills)

---

## What We Were Trying To Do

The RMM is a cross-domain theoretical framework with the formula τ = O × (1−R) — tension between consciousness threads scales with contact intensity and structural incompatibility. The program has 38 papers across 4 modules. We were trying to:

1. Write papers rigorously before submission rather than fixing problems during review
2. Use the signal pipeline as a pre-writing quality gate, not a post-writing check
3. Develop a reproducible methodology for academic papers across the program

The core question: **can Signal skills replace or frontload the work that reviewers currently do?**

Short answer: **yes, substantially** — with a specific pattern of failure modes and gaps documented below.

---

## The Methodology We Developed

We built a per-paper workflow that runs Signal skills *before* writing, not after. The final METHODOLOGY.md is at `C:\src\rmm\research\METHODOLOGY.md`.

### Phase 1 — Before Writing (7 skills)

| Step | Skill | What it caught |
|------|-------|----------------|
| 1 | `/discover-hypothesis` | Confirmation bias risks; falsification conditions; confidence calibration |
| 2 | `/discover-competitors` | Missing comparisons; inertia framing; key distinguishing tests |
| 3 | `/discover-inertia` | "Why would a reviewer not care?" — reframes hostile review productively |
| 4 | `/discover-causal` | Mechanism gaps; confounders; circular dependencies |
| 5 | `/discover-websearch` | Empirical claim verification; normalization errors; missing citations |
| 6 | `/simulate-argument` | Logical errors; broken inference chains; motivated reasoning |
| 7 | `/discover-coherence` | Cross-signal contradictions; blocking items |
| 8 | `/discover-synthesize` | PROCEED / PAUSE / PIVOT verdict |

### Phase 2 — Structure (2 skills)

| Step | Skill | What it caught |
|------|-------|----------------|
| 9 | `/specify-spec` | Paper outline from plan.md before writing |
| 9b | `/simulate-derivation` | *New — ODE/EM papers only.* Symbolic math traced step by step |

### Phase 3 — After Writing (3 validation skills)

| Step | Skill | What it caught |
|------|-------|----------------|
| 10 | `/validate-dimensional` | *New — math papers only.* Units consistency |
| 11 | `/validate-consistency` | Value mismatches across sections (7.4% vs 11.3%) |
| 12 | `/simulate-contract` | Claims vs. methodology delivery gap |

### Phase 4 — Before Submission (4 skills)

| Step | Skill | What it caught |
|------|-------|----------------|
| 13 | `/validate-design` | Multi-disciplinary expert review |
| 14 | `/validate-referee` | Journal-specific hostile review (JCS vs PNAS vs Complexity) |
| 15 | `/roles-check` | Board-member review (Chalmers, Haidt, Penrose, Taleb, etc.) |
| 16 | `/specify-abstract` | 6-part academic abstract in journal-specific register |

### Phase 5 — Post-Submission (2 skills)

| Step | Skill | Used for |
|------|-------|---------|
| 17 | `/discover-literature` | Systematic literature map for revision |
| 18 | `/rhythm-rebuttal` | Response-to-reviewers letter |

---

## What Worked Exceptionally Well

### 1. `discover-websearch` caught a paper-breaking error before submission

P01 reported τ_obs = 0.74 for the political polarization case (from ANES feeling thermometer data). The websearch found: "the average affective polarization score on the 2020 ANES was just north of 50 points." The paper was using the *in-party rating* (74/100), not the *differential* (own minus out-party ≈ 52/100).

Correct value: τ_obs ≈ 0.52. Error changes from 5.7% to 50.4%. Overall MAPE changes from 7.4% to 13.8% — still under the 15% threshold, but now a near-miss instead of a comfortable pass. The paper's framing of the polarization case had to be completely restructured.

**Without the websearch:** this error would have reached JCS reviewers who know the ANES data.

### 2. `simulate-argument` caught a logical error in the contact theory reconciliation

P01 claimed that RMM and the Pettigrew-Tropp contact hypothesis are "consistent for high-R pairs." `simulate-argument` traced this inference and found: **BROKEN**. The static formula always predicts O increase → τ increase for any R < 1. Contact theory predicts contact reduces tension. These are directly contradictory for the static case. The reconciliation requires the dynamic model (P03) and is not available in P01.

The paper had this logical error across 3 paragraphs. It was replaced with: "Directly contradictory in the static case; reconciled only via the dynamic model."

**Without simulate-argument:** a logically inconsistent claim would have appeared in three places in a paper submitted to a philosophy journal.

### 3. `discover-causal` exposed the mechanism gap that restructured P01b

The causal analysis for P01b showed that the UV channel reception mechanism in humans is not established — there is no known human sensory pathway that detects Blaschko's line UV-stripe patterns from another human. The paper had been built on this as the primary Pair B mechanism.

The causal analysis identified a secondary pathway: olfactory signals shaped by the full genetic background (via microbiome) are the actual mechanism. The "UV proxy" isn't a proxy for UV visual compatibility — it's a proxy for olfactory incompatibility across the full genetic signature.

This restructured the entire paper: the channel inventory was reorganized into 4 tiers (olfactory-primary, cross-species, fitness, identity), and "UV channel" was reclassified as a cross-species channel humans broadcast but cannot receive from each other. The paper is substantially stronger.

### 4. `validate-consistency` caught arithmetic inconsistencies in seconds

P01 had the MAPE value stated as 7.4% in the evaluation table, 7.4% in the abstract, but 11.3% in the Introduction contributions list. This was a stale number from an earlier version. `validate-consistency` surfaced it immediately as a value mismatch.

This class of error — same quantity with different values in different sections — is extremely common in papers that go through multiple revisions. The skill is designed exactly for this and it works.

### 5. The signal pipeline consistently identified the same issues from different angles

The most important finding: the same core problems appeared in 3-4 independent signals. The ANES error appeared in `discover-websearch` (factual), `simulate-argument` (broken inference chain C-30), and `discover-coherence` (blocking O-1). This convergence makes the problems hard to dismiss and gives the author confidence that the issues are real.

---

## What Didn't Work As Well

### 1. The pipeline was run after writing, not before — for P01

The methodology specifies: discover → specify-spec → author. We wrote P01 first, then ran the pipeline as a correction pass. This meant the pipeline was used as a debug pass rather than a design gate.

The cost: the ANES error, the contact theory logic error, and the Reformation τ inconsistency all made it into the paper. The pipeline caught them, but a pre-writing run would have prevented them.

**Lesson:** Discipline matters. The pipeline order is not optional.

### 2. `discover-websearch` only works for empirically grounded claims

For mathematical claims (is the ODE form correct? does the mean-field limit recover the static formula?), `discover-websearch` returns nothing useful. We needed `simulate-derivation` (ODE step-by-step tracing) and `validate-dimensional` (units consistency) — skills that didn't exist yet at the start of the session.

**The gap was identified and the skills were requested and built during the session.** This is the intended feedback loop.

### 3. The inertia skill was underused

`/discover-inertia` is in the methodology but we skipped it for most papers. For academic papers, "inertia" = "why would a reviewer use existing models instead of this framework?" This is exactly the question `discover-competitors` answers when it leads with the inertia competitor. We effectively merged the two.

**For future use:** run `discover-inertia` before `discover-competitors` to prime the competitor analysis with the specific inertia argument. For papers targeting paradigm-shift claims, this is the most important skill in the sequence.

---

## Gaps Identified — Skills Requested and Built During the Session

The following skills were requested during the session and built by the developer:

| Skill | Why requested | What it does |
|-------|--------------|--------------|
| `simulate-derivation` | P03 has an ODE with α/β rate constants; need step-by-step symbolic tracing | Traces symbolic manipulation EXACT/APPROX/DEFINITION/PHYSICAL steps; catches sign errors, missing terms, unstated approximations |
| `validate-dimensional` | P03 needs α in units of /year; P01b spectral overlap needs frequency units | Checks LHS = RHS units; exponential/log arguments dimensionless; critical for EM/physics papers |
| `validate-consistency` | P01 had 7.4% vs 11.3% MAPE mismatch — needed a dedicated value-consistency checker | Already existed; installed during session |
| `specify-abstract` | Academic abstracts are a specific 6-part genre; `specify-spec` doesn't know it | 250-word 6-part abstract with journal-specific variants (JCS, JTB, PNAS, Complexity) |
| `validate-referee` | JCS reviewer ≠ PNAS reviewer ≠ Complexity reviewer; need journal-specific simulation | 3 referee archetypes per journal; continuous I-NN issue IDs; P1/P2 blocking verdict |
| `discover-literature` | `discover-websearch` finds pages; needed structured prior-work map | 4-tier literature map: foundational / recent / contrary / methodological |
| `rhythm-rebuttal` | Review response letters after submission | Formal response-to-reviewers with R-IDs, AGREE/PARTLY/RESPECTFULLY, manuscript-change commitments |
| `simulate-argument` | Papers have logical inference chains; needed argument-specific tracing | Already existed; installed during session |

All 8 were either installed (pre-existing) or built (new) during the session.

---

## Discoveries That Changed the Papers

Several significant insights emerged from the signal pipeline that are now in the papers themselves:

**1. The Blaschko's lines / UV channel insight** emerged from a user question about birds seeing patterns on humans that humans can't see on themselves. This wasn't in any plan document. It led to P01b being created as a new paper in the research program.

**2. The "Reformation produces simultaneous Conflict AND Emergence"** finding emerged during the `discover-causal` run for P01 when analyzing the casus belli mechanism. It is now a theoretical contribution in P02's multi-outcome treatment.

**3. The Roman-Christian case as causal identification** for P02 emerged from the `discover-causal` patronage confounder analysis. The paper now leads with it in the Introduction as the paper's primary empirical contribution.

**4. R = inverse prediction error** — the insight that the Hasson PNAS 2010 neural coupling finding (anticipatory coupling predicts comprehension) is exactly the spectral overlap R formula applied to brains — emerged from reading the other session's biology.md source compilation. This is now in P01b as the primary R measurement instrument grounding.

**5. Sexual orientation, attraction types, and cross-population attraction patterns** as evidence for vector R — these emerged from the user asking "what about homosexuality?" and "what about women not dating short men?" They are now P01b theoretical contributions.

The pattern: **the most important insights came from conversation, not from the signal pipeline alone.** The pipeline catches errors and surfaces gaps; the interactive conversation generates the breakthroughs. The combination is the methodology.

---

## Metrics

| Metric | Value |
|--------|-------|
| Papers authored | 3 complete (P01, P01b, P02), 1 in pipeline (P03) |
| Review rounds run | P01: 2 rounds; P01b: 2 rounds; P02: 2 rounds |
| Score progression | P01: 2.7 → 3.1; P01b: 2.9 → 3.3; P02: 2.9 → 3.3 |
| Signal artifacts created | 47 (across all skills and papers) |
| Findings documented | P01: 21; P01b: 33; P02: 17; P03: 12 (in progress) |
| Errors caught before submission | 6 P1 errors across 3 papers |
| Papers restructured from signal findings | 2 (P01b: UV→olfactory; P02: rectangular→hyperbolic bounds) |
| New skills installed during session | 8 |
| New papers added to program | 1 (P01b — vector/matrix structure) |
| Sources created | 3 (biology.md, history.md + entries in CONCEPT-INDEX.md) |

---

## Recommended Workflow for Academic Research Programs

Based on this session, the recommended workflow for academic research programs using Signal:

1. **One paper at a time, interactively.** The user must be in the loop. The most valuable insights came from conversation between user and Claude, not from automated pipeline runs. The pipeline structures the conversation; the conversation generates the insights.

2. **Run the full pipeline before writing.** Do not write first and pipeline second. The discipline is worth it — the pipeline prevents structural errors that take multiple revision cycles to fix.

3. **Use agents for revision passes, pipeline interactively.** Once the signals are collected and the paper is written, use background agents for the revision passes (P1 fixes, P2 fixes). Keep the pipeline runs interactive — each skill produces findings that inform the next skill.

4. **The FINDINGS.md file is the core artifact.** Every finding gets a numbered entry, a section reference, and a source link. This is the document that guides revision agents and tracks what's been addressed. Without it, findings get lost.

5. **`discover-coherence` is the most diagnostic skill.** It surfaces contradictions across signals that no individual skill catches. The blocking items from coherence are always the most important fixes.

6. **Let conversations generate new insights; let skills catch errors.** The skills are error-detection infrastructure. The conversation is where the theoretical advances happen. Both are necessary.
