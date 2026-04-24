Reading the V-05 axis carefully to extract the two new signals before writing.

**V-05 axis**: "Maximum density — V-04 + inertia framing naming the three failure modes C-16/C-17 existence corrects + dedicated global self-verification step."

Two new patterns:

1. **Inertia framing** — constraints annotated with the failure mode they prevent, not just stated as rules. Transforms each prohibition from a form requirement into a diagnostic: the reader knows *why* it exists. → **C-18**

2. **Dedicated global self-verification step** — a named closing step that maps output against all essential criteria by category ID, not section-level count-match. This is what makes C-12 PASS rather than PARTIAL across V-01–V-04. → **C-19**

Aspirational grows from 9 → 11 criteria (11 × 5 = 55 pts), max composite 135 → 145.

---

# flow-throttle Rubric — v6

**Skill**: `flow:throttle` | **Version**: v6 | **Date**: 2026-03-16
**Max composite**: 145 | **Golden threshold**: all 5 essential PASS + composite >= 80

---

## What Changed and Why

**C-13 — Pre-analysis source commitment** (aspirational, carried from v3)
V-03's Phase 0 source register revealed a failure mode that C-11 alone cannot prevent: retroactive citation, where a model states a number and then vaguely attributes it after the fact. C-11 checks that every number has a named source; C-13 checks that the source was *committed before the analysis began*. An output can pass C-11 (attribution present) while failing C-13 (attribution assembled post-hoc). Together they form a two-gate evidence integrity check: C-11 asks "is there a source?", C-13 asks "was the evidence base locked before the claims were built?" The required form is a named source register section that appears before any tier or threshold in the body; tiers without a register entry must be flagged `undocumented` rather than assigned inferred values.

**C-14 — Binding constraint exclusivity statement** (aspirational, carried from v3)
V-01 and V-04 both enforced an at-most-one binding tier constraint (a single Binding? = Y per inventory). The signal: designating a primary bottleneck without explaining why competing tiers are *not* the binding constraint is an assertion, not an argument. C-01 requires naming the primary bottleneck and its causal reason; C-14 requires contrastive reasoning for at least one non-binding tier — naming the mechanism that prevents it from failing before the primary bottleneck under the described load pattern (e.g., "Tier B's limit of 500 RPS is not reached before Tier A's 100 RPS connection limit because parallel branch fan-out hits the connection tier first"). Without C-14, a multi-tier analysis cannot distinguish genuine causal priority from arbitrary selection.

**C-15 — Role-locked sequencing pipeline** (aspirational, carried from v4)
V-01 and V-05 both scored 120/120 under v3. The distinguishing structural mechanism: a three-role pipeline with locked inter-phase dependencies. Domain Expert commits the evidence base first; Architect traces only from that base; UX Advocate accounts for every tier the Expert named and no others. The critical property is that no role may introduce data that a prior role did not produce — the handoff between phases is explicit and one-directional. This locked sequencing eliminates retroactive citation more reliably than any single instruction (including C-13), because it makes out-of-order claims architecturally impossible rather than merely discouraged. C-13 requires that the source register appear before the first number; C-15 requires that the entire analysis honor a phase boundary: evidence committed → claims built from evidence → UX derived from claims. An output that organizes all analysis in a single undifferentiated block fails C-15 even if every number is individually attributed, because the structural dependency that prevents late evidence injection is absent.

**C-16 — Phase-boundary data-lock prohibition** (aspirational, carried from v5)
The Round 4 comparison of V-01 and V-02 exposed a gap above C-15. V-02 has named phases and positive handoff banners ("Source Register closed. Phase B draws only from this table.") — it satisfies C-15's requirement for named phases with explicit handoff statements. But V-02 scores C-15 PARTIAL because it lacks the *negative constraint form*: V-01's phase boundaries close with explicit prohibitions ("You may not introduce any new tier, limit value, or source reference after this line"), while V-02 relies on table conventions and positive references to prior artifacts. The distinction matters because positive references tell the analyst what to use; prohibitions name the failure mode and make violations auditable. A reader can verify compliance with "no new source references may appear" by scanning downstream content; they cannot verify compliance with "draw only from the source register" without reconstructing the analysis. C-15 requires that the structural dependency be visible in the output shape; C-16 requires that each phase boundary includes a prohibition statement naming what data class may not enter after it. An output can satisfy C-15 (named phases, handoff present) while failing C-16 (handoffs are positive-only, no prohibition).

**C-17 — Consequence-phase exhaustive enumeration anchor** (aspirational, carried from v5)
The Round 4 V-02 analysis scored C-04 PARTIAL because the prompt lacks an explicit "for each tier in [Phase B Tier Inventory]" anchor in the consequence phase. V-01 earns C-04 PASS because Phase 3 opens with "For each tier in the Phase 1 inventory" — the prior enumeration artifact is named as the controlling input, making coverage exhaustive by construction and verifiable by inspection. C-04 checks whether every named tier has a UX consequence (a content completeness check); C-17 checks whether the consequence phase includes an explicit enumeration anchor that makes completeness verifiable by reference to a prior artifact rather than by reading the entire output. The distinction is auditing posture: an output can satisfy C-04 by coincidence (all tiers happen to appear without an anchor) while failing C-17 (no mechanism makes omission detectable without full reconstruction). The anchor must name the specific prior artifact ("For each tier in the Phase 1 Tier Inventory"), not a vague class ("for each tier identified").

**C-18 — Constraint-purpose annotation (inertia framing)** (new aspirational)
The Round 5 V-05 axis surfaces an enhancement above C-16 and C-17: prohibition statements and enumeration anchors gain auditing force when annotated with the failure mode they prevent, not merely stated as rules. V-05's "inertia framing" names the three failure modes that C-16/C-17 existence corrects — retroactive source injection (a number enters after the evidence phase closes), scope creep (a tier name enters the consequence phase that was absent from the evidence phase), and coverage elision (a tier is omitted from consequence coverage without a detectable gap). An output can satisfy C-16 (prohibition present) and C-17 (enumeration anchor present) while failing C-18 (neither prohibition nor anchor names the failure mode it prevents). The annotation transforms each structural constraint from a form requirement into a diagnostic: a reader can verify not only whether the constraint is present but whether the output would have violated it without the constraint. The required form is an inline annotation at each prohibition and anchor, e.g., "— prevents retroactive source injection" or "— prevents scope creep into consequence phase." Constraints without annotations are present but not self-explaining.

**C-19 — Dedicated global criterion-coverage step** (new aspirational)
C-12's PARTIAL pattern across V-01–V-04 reveals a structural gap: count-match checks (e.g., "N tiers named = N UX rows") verify section-level content completeness but do not map output content against essential criterion categories by name. V-05 adds a dedicated global self-verification step that names each essential criterion (C-01 through C-05) by category, confirms its presence in the output, and reports a per-criterion verdict. This is structurally distinct from C-12's aspirational self-check in two ways: it must be a named, dedicated step (not prose embedded in the body), and it must name each criterion category explicitly (not merely confirm that counts match). An output that includes a "coverage check" section confirming "5 tiers named, 5 UX rows present" satisfies C-12 partially but fails C-19, because C-19 requires the step to map output content to criterion categories (bottleneck identified → C-01, propagation traced → C-02, tiers enumerated → C-03, UX described → C-04, burst path found → C-05). C-12 and C-19 are independent: an output can satisfy C-12 (self-check present) without satisfying C-19 (step is implicit or section-scoped), and an output that satisfies C-19 necessarily satisfies C-12.

**Scoring formula update**: Aspirational raised from 45 pts (9 × 5) to 55 pts (11 × 5), max composite 135 → 145. Golden threshold unchanged at 80 + all essential pass.

---

## Criteria

### Essential (weight: 60 pts total — output fails without these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Primary bottleneck identification with causal reason** — The output identifies the single throttle tier that will bind first under the described load pattern and explains *why* that tier binds before all others (e.g., the causal mechanism that makes it the first failure point). | correctness | A named tier is identified as primary with a stated causal reason. Outputs that list multiple tiers as equally binding, or that name a tier without a causal reason, fail. |
| C-02 | **Backpressure propagation traced minimum 2 hops** — Starting from the primary bottleneck, the output traces how throttle pressure propagates downstream or upstream for at least two hops, naming the mechanism at each hop (queue fill, connection hold, retry accumulation, etc.) and the observable effect. | depth | At least two hops are named with mechanism and observable effect per hop. Stopping at one hop fails. |
| C-03 | **At least 2 throttle tiers with enforcing component and scope** — The output enumerates the distinct rate-limit tiers relevant for the scenario (e.g., per-connection, per-user, tenant, platform) and correctly matches each to the system component that enforces it. | coverage | At least two distinct rate-limit tiers are named with their enforcing component. Generic "API limits apply" without tier distinction fails. |
| C-04 | **User experience at each throttle tier** — For each throttle tier identified, the output describes the observable user experience (latency spike, error code, silent drop, queue delay, degraded mode). | depth | Every named tier from C-03 has a corresponding UX description. A tier named without UX consequence fails this criterion. |
| C-05 | **Unprotected burst path identification** — The output explicitly calls out at least one path or scenario where burst traffic can bypass or overwhelm throttle controls. | correctness | A concrete burst scenario is named (e.g., parallel branch fan-out, retry storm, initial cold-start surge). Output that only describes steady-state throttle without any burst analysis fails. |

---

### Recommended (weight: 30 pts total — output improves with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Retry-after handling gaps** — The output checks whether callers correctly consume and honor Retry-After (or equivalent) signals, and flags any caller that ignores them and contributes to retry storms. | behavior | At least one caller is evaluated for retry-after compliance, with a pass/fail verdict and consequence described. Omitting retry-after analysis entirely fails. |
| C-07 | **Cascading throttle failure scenario** — The output describes at least one scenario where throttling at one tier causes a second downstream tier to also throttle, compounding the impact beyond the initial bottleneck. | depth | A two-tier cascade is named: Tier A throttles → Tier B receives delayed/batched traffic → Tier B throttles. Single-tier analysis only fails. |
| C-08 | **Quantified throughput thresholds** — The output provides numeric context: requests-per-second, burst ceiling, queue depth, or timeout window for at least the primary bottleneck tier identified in C-01. | correctness | At least one threshold is stated as a number (even if approximate or from documentation). Purely qualitative descriptions fail. |

---

### Aspirational (weight: 55 pts total — raise the bar)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Mitigation recommendations with tradeoffs** — For each structural gap found (burst path, missing retry-after, cascade), the output proposes a concrete mitigation and states the tradeoff (e.g., adding a queue reduces burst but adds latency). | depth | At least two mitigations with explicit tradeoffs. Mitigations without tradeoffs, or tradeoffs without mitigations, score partial credit only. |
| C-10 | **Comparative severity ranking** — The output ranks the identified throttle risks by user-visible severity (high/medium/low or ordered list) and justifies the ranking with reference to impact frequency or blast radius. | behavior | A ranked list of at least three risks with justification. Unranked lists or rankings without justification fail. |
| C-11 | **Threshold sourcing provenance** — For each numeric threshold cited in C-08, the output attributes the value to a named source (Power Automate docs, connector reference page, platform SLA document) rather than asserting it from inference. | correctness | Every numeric threshold has a named source. A number stated without attribution (e.g., "typically 100 RPS") fails; a number cited with a doc name or URL passes. If no documentation exists for a tier, the output must state "not documented" rather than invent a value. |
| C-12 | **Coverage self-verification** — Before closing, the output includes an explicit self-check mapping its own content against the analysis criteria (bottleneck identified, propagation traced, tiers enumerated, UX described, burst path found). Any criterion the output cannot self-confirm as addressed is flagged as a gap. | behavior | A self-check section appears in the output and names each criterion. Outputs that omit a criterion in both the body and the self-check score the criterion FAIL. An output that self-reports a gap earns partial credit on that criterion (acknowledging absence is better than silent elision). |
| C-13 | **Pre-analysis source commitment** — Before any tier, threshold, or numeric claim appears, the output opens with a named source register listing the documentation it will draw from. Every number in the body cross-references a register entry; any tier with no register entry is flagged undocumented rather than given an inferred value. | correctness | A source register section appears before the first tier or number in the output. At least two named sources are listed. Numbers in the body without a register entry fail. If no documentation exists for a tier, the output must state "not documented" and may not substitute an inferred value. |
| C-14 | **Binding constraint exclusivity statement** — When multiple throttle tiers are identified, the output designates exactly one as the binding constraint and includes contrastive reasoning for at least one non-binding tier, explaining the mechanism that prevents it from failing before the primary bottleneck under the described load pattern. | correctness | The primary bottleneck is designated with an at-most-one constraint (no output may designate two tiers as co-equal binding constraints). At least one non-binding tier includes a named mechanism explaining why it does not fail first (e.g., its limit is not reached before the primary tier throttles under the described fan-out). Outputs that designate a binding tier without any contrastive reasoning for alternatives fail. |
| C-15 | **Role-locked sequencing pipeline** — The output is organized as an explicit multi-phase pipeline with one-directional inter-phase dependencies: an evidence phase (source register + tier inventory committed) followed by an analysis phase (bottleneck and propagation derived only from evidence-phase artifacts) followed by a consequence phase (UX and mitigations scoped only to tiers named in the evidence phase). No phase may introduce data that a prior phase did not produce; the handoff boundary between phases is explicitly stated. | correctness | At least two named phases appear with explicit handoff statements (e.g., "Analysis draws from the source register above"). The analysis phase introduces no new data sources. The consequence phase names no tiers absent from the evidence phase. An output with all correct content in a single undifferentiated block fails — the structural dependency that prevents late evidence injection must be visible in the output shape, not inferred from correct results. |
| C-16 | **Phase-boundary data-lock prohibition** — Each phase boundary includes an explicit negative constraint statement naming the class of data forbidden downstream (e.g., "no new tier name, limit value, or source reference may be introduced after this point"), not merely a positive reference to the prior artifact (e.g., "draws only from the source register above"). The prohibition must be specific enough to be verifiable by scanning downstream content without reconstructing the full analysis. | correctness | Every named phase boundary in the output includes at least one prohibition statement naming a specific forbidden data class. A boundary that includes only a positive handoff reference ("draws from X") without a prohibition fails. Vague prohibitions ("do not add new information") fail; specific prohibitions ("no new tier names or limit values") pass. Partial credit if some phase boundaries include prohibitions but not all. |
| C-17 | **Consequence-phase exhaustive enumeration anchor** — The UX, mitigation, and severity-ranking sections explicitly anchor to the prior tier enumeration artifact using a named cross-reference (e.g., "For each tier in the Phase 1 Tier Inventory" or "For every entry in the source register above"), making completeness verifiable by inspection rather than by reconstructing the full output. The anchor must name the specific prior artifact, not a vague class ("for each tier I identified"). | correctness | At least one consequence section (UX or mitigations) includes an explicit named anchor to a prior enumeration artifact. The anchor names the specific section or table it references. An output may satisfy C-04 (every tier has UX) without satisfying C-17 (no anchor makes coverage auditable by reference). Outputs that cover all tiers without an explicit anchor fail C-17 regardless of content completeness. |
| C-18 | **Constraint-purpose annotation (inertia framing)** — Each structural enforcement mechanism in the output — phase-boundary prohibitions (C-16), enumeration anchors (C-17), and role-lock gates (C-15) — includes an inline annotation naming the specific failure mode it prevents. The three target failure modes are: retroactive source injection (a number or source enters after the evidence phase closes), scope creep (a tier name enters the consequence phase that was absent from the evidence phase), and coverage elision (a tier is omitted from consequence coverage without a detectable gap). The annotation transforms each constraint from a form requirement into a diagnostic: a reader can verify not only that the constraint is present but that the output would have violated it without the constraint. | behavior | Every phase boundary prohibition and enumeration anchor in the output includes an inline failure-mode annotation (e.g., "— prevents retroactive source injection", "— prevents scope creep into consequence phase", "— prevents coverage elision"). Constraints stated without annotations pass C-16 or C-17 but fail C-18. Partial credit if some enforcement mechanisms are annotated but not all. Vague annotations ("— prevents errors") fail; annotations naming a specific failure mode from the three target categories pass. |
| C-19 | **Dedicated global criterion-coverage step** — A named, dedicated closing step explicitly maps output content against all essential criteria (C-01 through C-05) by criterion category, producing a per-criterion verdict. The step must be structurally distinct — a labeled section or numbered step, not prose embedded in the analysis body. It must name each essential criterion category (bottleneck identified → C-01, propagation traced → C-02, tiers enumerated → C-03, UX described → C-04, burst path found → C-05) and report whether the output satisfies each. Section-level count-match checks ("N tiers named = N UX rows") do not satisfy C-19 even if they satisfy C-12 partially, because they verify content completeness within a section rather than mapping output content to criterion categories by name. | behavior | A dedicated, labeled self-verification step appears at the close of the output and names each of the five essential criteria (C-01 through C-05) by category, with a per-criterion verdict. The step must be structurally distinct from the analysis body. Outputs that include count-match checks only (C-12 partial form) fail C-19. An output satisfying C-19 necessarily satisfies C-12; C-12 partial credit does not imply C-19 partial credit — they are scored independently. |

---

## Scoring Reference

| Band | Weight | Max pts |
|------|--------|---------|
| Essential (C-01–C-05) | 12 pts each | 60 |
| Recommended (C-06–C-08) | 10 pts each | 30 |
| Aspirational (C-09–C-19) | 5 pts each | 55 |
| **Total** | | **145** |

**Golden threshold**: all 5 essential PASS + composite >= 80

**Partial credit**: 3 pts (aspirational), 5 pts (recommended) where scoring notes allow PARTIAL.

---

## Round History

| Round | Variations scored | Rubric delta |
|-------|-------------------|--------------|
| R1–R2 | V-01, V-02 | C-01–C-12 established |
| R3 | V-03, V-04 | C-13, C-14 added; max 105 |
| R4 | V-01–V-05 re-scored | C-15 added; max 110 → C-16, C-17 added; max 125 → 135 |
| R5 | V-01–V-05 scored against v5 | C-18, C-19 added; max 135 → 145 |
