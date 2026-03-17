Now I have the context I need. The Round 11 scorecard introduces V-03 with a three-part axis (VERDICT as inertia verb, per-signal confirmation/challenge ledger, Beat 5 inertia-to-final comparison) — none of these mechanisms are captured by existing criteria. Three new aspirational criteria: C-30, C-31, C-32. N_aspirational: 22 → 25.

# Quest Rubric — `topic-story` v11

**Version:** v11
**Source rounds:** R1–R11
**Rubric version history:**
- v10 → v11: +3 aspirational criteria (C-30, C-31, C-32); N_aspirational 22 → 25
- v9 → v10: +2 aspirational criteria (C-28, C-29); N_aspirational 20 → 22

**What changed from v10 to v11:**

| | v10 | v11 |
|--|-----|-----|
| Version | v10 | v11 |
| Source rounds | R1–R10 | R1–R11 |
| Aspirational count | 22 | 25 |
| Total criteria | 29 | 32 |
| Composite formula denominator | 22 | 25 |

**Three new aspirational criteria from R11 (V-03 axis):**

| C | Name | Axis | Category |
|---|------|------|----------|
| C-30 | VERDICT as falsifiable inertia recommendation verb | V-03 | correctness |
| C-31 | Per-signal confirmation/challenge ledger | V-03 | depth |
| C-32 | Beat 5 inertia-to-final comparison | V-03 | correctness |

---

## Essential Criteria

Output is not usable if any essential criterion fails.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Bottom Line Up Front** | correctness | essential | The recommendation or verdict appears in the opening paragraph or first named section — not buried at the end. A story that builds to a conclusion fails. A story where the first substantive sentence is hedging or context-setting fails. |
| C-02 | **Labeled sections present** | format | essential | The story contains the five named beats: *What we set out to understand / What the signals revealed / What the signals say together / What remains uncertain / The recommendation*. Any beat missing or renamed beyond recognition fails. |
| C-03 | **Cross-signal synthesis present** | correctness | essential | Beat 3 states a claim that references what two or more signals show *together* that no single signal shows alone. A sentence that could be derived from reading any single artifact fails. Restating artifact summaries side by side fails. |
| C-04 | **Pattern, not summary** | depth | essential | The synthesis claim names a relationship, tension, or gap across signals — not a collection of findings. A sentence equivalent to "Signal A said X and Signal B said Y" fails. The pattern must name a synthetic claim (e.g., "users want X but the technical cost is Y — the gap is the risk"). Restating individual findings side by side fails. |

---

## Recommended Criteria

Output is meaningfully better when these pass.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Signal coverage is grounded** | coverage | recommended | At least three distinct signal namespaces or artifact types are referenced to show what evidence base the story draws from. Not exhaustive enumeration — enough to make the synthesis credible. Fewer than three identifiable signal sources fails. |
| C-06 | **Uncertainty is specific** | depth | recommended | The "what remains uncertain" section names at least one specific open question that, if resolved, would change the recommendation. Generic hedges such as "more research may be needed" without naming what research or what it would change fail. |
| C-07 | **Recommendation proportionality** | correctness | recommended | The recommendation weight is consistent with the evidence described. Strong positive signals → proceed; mixed → pause; conflicting → pivot; weak or negative → abandon. A proceed recommendation following a story of conflicts and gaps fails; an abandon recommendation following a story of strong positive signals fails. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Narrative arc** | behavior | aspirational | The story has a discernible arc: intent (what we set out to learn), evidence building (signals adding up), resolution (recommendation). A reader unfamiliar with the topic can follow the reasoning from intent to recommendation without consulting the underlying signals. A flat list of findings with a tacked-on recommendation fails. |
| C-09 | **Delta surfacing** | depth | aspirational | At least one explicit "we expected X but found Y" or equivalent contrastive statement appears. The story calls out where the signals surprised or contradicted initial assumptions. Absence of any contrastive or discovery framing fails. Discovery language that requires inference from surrounding context — rather than a stated contrast — fails. |
| C-10 | **Pre-composition pattern artifact** | depth | aspirational | The cross-signal pattern is stated as a discrete, labeled claim that stands independently of the narrative prose — a named sentence or block (e.g., "The pattern: ...") that could be read without the surrounding story. The pattern must not exist only as an inference embedded in flowing text. This signals the pattern was identified analytically before writing, not arrived at during composition. Absence of a discrete pattern statement fails. |
| C-11 | **Pattern-to-recommendation traceability** | correctness | aspirational | The recommendation is visibly derived from the named cross-signal pattern. The story contains an explicit logical bridge: the pattern is cited as the stated reason for the recommendation verb chosen. A reader can identify the sentence or passage where the pattern produces the recommendation. Recommendation and pattern that are both present but not explicitly connected fail. |
| C-12 | **Decision-cost annotated uncertainty** | depth | aspirational | Each uncertainty item explicitly states what resolving it would change about the recommendation: whether the verb would shift and in which direction (e.g., "if X resolves to Y, this moves from pause to proceed"). General "this matters for the decision" framing without a stated direction fails. Uncertainty items with no decision-cost annotation fail. |
| C-13 | **Accountability-addressed recommendation** | correctness | aspirational | The recommendation beat names or clearly addresses the decision context — who is making the decision and under what constraint. A recommendation stated as a finding ("the signals suggest X") rather than a decision ("a team lead deciding Y should Z") fails. A recommendation with no named or implied decision-maker role fails. |
| C-14 | **Pattern block self-sufficiency** | depth | aspirational | The pre-composition pattern block (C-10) is self-contained: it conveys the full cross-signal claim without requiring the surrounding narrative to be read. Forward references ("as shown below"), backward references ("the above signals"), or incomplete claims that resolve only in the prose around the block all fail. |
| C-15 | **Delta pre-composition** | depth | aspirational | The contrastive discovery ("we expected X but found Y") is identified as a discrete analytic step before narrative prose begins — not arrived at during composition or appended as a closing observation. Parallel to C-10: the delta must exist as a named pre-writing output, not emerge organically from the writing. A delta statement that could have been written without prior comparative analysis fails. Absence of any evidence that the contrast was surfaced analytically before the story was composed fails. |
| C-16 | **Evidence-verb self-certification** | correctness | aspirational | The recommendation beat includes an explicit evidence posture statement — a sentence that names the overall signal posture (e.g., strong positive, mixed, conflicting, weak) and cites it as the direct basis for the verb chosen. A recommendation that states the verb without naming the posture that produced it fails. The posture statement must appear in the recommendation beat itself, not be inferred from the synthesis section. |
| C-17 | **Explicit pattern-to-recommendation bridge** | correctness | aspirational | The recommendation beat contains a sentence that names the cross-signal pattern by reference and identifies it as the stated reason for the verb chosen — not merely that both the pattern and the verb appear in the story. The bridge must be explicit: "Because [the named pattern], the recommendation is [verb]" or equivalent. A story where the pattern and the recommendation verb are present but connected only by implication or inference fails. The bridge sentence must appear in the recommendation beat, not in Beat 3. |
| C-18 | **Structural pre-composition gate** | depth | aspirational | Proof that analytic artifacts (pattern, delta) were produced before narrative writing is established by structural placement, not by instruction. A named Part 1 / Part 2 separator, a formally labeled block with a placement rule, or an equivalent structural device is required. Instructional language alone ("write the delta before writing the story") does not satisfy this criterion — the structure must make it verifiable. An output where pre-composition cannot be confirmed from structure alone fails. |
| C-19 | **Non-substitution constraint** | correctness | aspirational | The story explicitly states that an artifact produced in an earlier stage or section does not satisfy the requirement for its placement in a later stage or section. Each required placement must be independently satisfied — prior-stage presence is not credit. A prompt or template that allows the bridge sentence produced in the analysis block to serve as the bridge sentence required in the recommendation beat fails. The non-substitution rule must be stated explicitly for each placement requirement where early production could otherwise imply late satisfaction. |
| C-20 | **Multi-stage consistency enforcement** | correctness | aspirational | Critical claims — evidence posture, pattern statement, recommendation verb — appear at multiple designated positions in the output such that inconsistency between stages is self-revealing without requiring the reader to manually compare sections. A single-point certification (posture named once, in one place) fails. The required redundancy is structural: each critical claim must appear at a minimum of two named positions whose pairing is visible in the output. An output where a claim could change between an early stage and the recommendation beat without contradiction being structurally visible fails. |
| C-21 | **Falsifiable hypothesis as inertia baseline** | depth | aspirational | The initial hypothesis (Beat 1 / "What we set out to understand") is stated as a falsifiable claim — a specific proposition that the signals can confirm, refute, or modify. A vague intent statement ("we set out to understand X") fails; the hypothesis must be a claim that could be proven wrong ("we believed X" / "our hypothesis: X holds"). This creates the measurable inertia baseline against which the S0→S3 delta is computed — without a falsifiable starting position, the delta has no reference point and C-09's contrast collapses into a description rather than a measurement. |
| C-22 | **Anti-stagnation constraint** | depth | aspirational | The S0→S3 delta shows substantive mutation: the evolved hypothesis differs from the initial in a way that affects the recommendation's direction or confidence level. An output must demonstrate — not merely assert — how the signals shifted, strengthened, or undermined the initial hypothesis in a named way. A delta that amounts to "the signals confirmed what we already believed" without naming how confidence changed fails. S0 = S3 is a pattern failure regardless of how it is framed. The anti-stagnation check is not satisfied by a contrastive statement that could have been written before the signals were read. Depends on C-21: C-22 cannot pass if C-21 fails. |
| C-23 | **Prior-verdict override discipline** | correctness | aspirational | If a prior beat or stage produces a verdict — an adjudicated signal stance, a RESOLVED conflict determination, or an intermediate recommendation — the recommendation beat cannot contradict it without an explicit, named override reason. Silent contradiction fails: a recommendation verb inconsistent with a prior-stage verdict is a correctness error, not a stylistic choice. The override sentence must identify which verdict is being superseded and state the reason the final recommendation departs from it. A recommendation that is merely consistent with prior verdicts requires no additional action; this criterion applies only where a contradiction exists. |
| C-24 | **Role execution order as pre-composition gate** | depth | aspirational | Pre-composition is enforced by named role sequencing — a designated analytic role (e.g., ANALYST) that must complete all analytic blocks before a designated authoring role (e.g., AUTHOR) may begin any narrative beat. The role boundary must be explicit and one-directional: beats cannot be started until all blocks are marked complete, and completing blocks after beats have begun is a visible role violation. Structural placement alone (a separator between blocks and beats) does not satisfy this criterion — the one-way role transition must be named. An output where the analytic role could have been executed retroactively after beats were written, without that being structurally self-revealing, fails. Depends on C-18: C-24 cannot pass if C-18 fails. |
| C-25 | **Terminal verification checklist** | correctness | aspirational | The output includes a terminal self-audit section — a named checklist of binary pass/fail checks, one per structural requirement, that must be completed before submission. The checklist converts implicit compliance assumptions into explicit yes/no decisions: the author must affirm each criterion is satisfied by marking it, not by having written a compliant section. Absence of a terminal checklist fails. A checklist that is instructional only ("verify that you did X") rather than declarative ("[ ] Block B present and self-sufficient") fails. A checklist that is present but not required to be completed before the output is submitted fails — the checklist must be a gate, not an appendix. |
| C-26 | **Tri-role artifact extraction gate** | depth | aspirational | The pre-composition role sequence (C-24) is implemented with three distinct named roles: EXTRACTOR, ANALYST, and AUTHOR. The EXTRACTOR role reads signal artifacts and produces summaries or signal digests as its discrete output; the ANALYST role reads EXTRACTOR output — not the raw artifacts directly — and produces pattern, delta, and posture claims; the AUTHOR role reads ANALYST output and writes narrative beats. A two-role design that merges artifact reading into the ANALYST role blurs the boundary between "having read the signals" and "having synthesized them" — EXTRACTOR completion must be a named gate for ANALYST work to begin. An output where artifact reading and pattern analysis are performed by the same named role fails. Depends on C-24: C-26 cannot pass if C-24 fails. |
| C-27 | **Recommendation beat bridge independence** | correctness | aspirational | The non-substitution rule (C-19) is applied explicitly to the recommendation beat: the pattern-to-recommendation bridge sentence required in Beat 5 is an independently-placed requirement that cannot be discharged by the bridge sentence produced in the ANALYST pattern block, even when the two sentences are equivalent in content. The template must name Beat 5 as a distinct, independently-required bridge placement with an explicit non-substitution statement scoped to it — a general non-substitution rule (C-19) that does not specifically enumerate Beat 5 fails. A template where the analyst-stage bridge is referenced, copied, or forward-carried into Beat 5 rather than independently produced in Beat 5 fails. This is the mechanism by which C-11 and C-17 can achieve full PASS rather than PARTIAL: without independent placement in Beat 5, the bridge may exist analytically but remain unverified as a narrative commitment. Depends on C-17 and C-19. |
| C-28 | **Recommendation preview before analytic blocks** | correctness | aspirational | The template must place the recommendation verb in a named section or labeled block that precedes all analytic role work (EXTRACTOR, ANALYST) — not as a forward reference or placeholder, but as an independently stated verdict. This is the structural mechanism that satisfies C-01 when the five-beat epistemic sequence places the full recommendation argument in Beat 5 (last). The preview and Beat 5 are independent placements: the preview satisfies BLUF; Beat 5 completes the accountability-addressed, bridge-connected recommendation. A template where the first explicit recommendation verb appears in Beat 5 fails regardless of how strong the analytic blocks are. A preview that is conditional ("if the signals support it, the recommendation will be…") rather than declarative fails. Depends on C-01: C-28 converts C-01 from a criterion the author may satisfy into a structural guarantee. |
| C-29 | **Namespace enumeration as EXTRACTOR instruction** | coverage | aspirational | The template must include an explicit instruction — placed within the EXTRACTOR role block — to enumerate the signal namespaces or artifact types the story draws from, naming this enumeration as a required extraction output rather than an editorial option. C-05 requires three distinct signal sources to appear in the story; C-29 requires the template to mandate that enumeration as a named step. A template that leaves namespace coverage to authorial discretion rather than specifying it as a discrete EXTRACTOR deliverable fails. This converts C-05 from a pass/fail outcome that depends on the author's initiative into a pass/fail outcome that the template structure drives. Depends on C-05 and C-26: C-29 cannot pass if C-05 fails or if C-26 fails. |
| C-30 | **VERDICT as falsifiable inertia recommendation verb** | correctness | aspirational | The VERDICT block (C-28) must commit to a specific recommendation verb — one of: proceed / pause / pivot / abandon — as a falsifiable pre-signal inertia position that the ANALYST role will test against the gathered signals. A VERDICT block that states directional intent without naming a specific testable verb fails ("the signals will likely support proceeding" is not a falsifiable verb commitment). A VERDICT that hedges with conditionality ("likely proceed, pending signals") rather than declaring an entering verb fails. This converts C-28 from a placement requirement into a hypothesis-commitment mechanism: the recommendation verb is staked before evidence is read, making the signal journey auditable as a confirmation or refutation of the entering position. The VERDICT verb and the final Beat 5 verb may match (confirmed inertia) or differ (signal-driven revision); both outcomes satisfy C-30 as long as the entering verb was declaratively committed before analytic work began. Depends on C-28: C-30 cannot pass if C-28 fails. |
| C-31 | **Per-signal confirmation/challenge ledger** | depth | aspirational | The ANALYST role must produce a discrete, named ledger artifact — separate from the pattern block, delta block, and posture claim — in which each signal artifact or namespace examined is individually classified as *confirms* or *challenges* relative to the inertia recommendation verb declared in the VERDICT (C-30). Each ledger row must name the signal, state its stance (confirms / challenges / mixed), and provide a one-line rationale. An ANALYST output that produces aggregate synthesis claims without a per-signal stance record fails — the ledger is a precondition for auditable synthesis, not a summary of it. The ledger makes the path from individual signals to the final recommendation verb traceable at the signal level: reviewers can identify which signals drove confirmation and which drove revision without reconstructing the reasoning from prose. Depends on C-30 and C-26: C-31 cannot pass if C-30 fails or if C-26 fails. |
| C-32 | **Beat 5 inertia-to-final comparison** | correctness | aspirational | The recommendation beat (Beat 5) must contain an explicit inertia-to-final comparison: the entering verb (from the VERDICT / C-30) and the final verb are both named in the same structural location, with a stated reason for any change — or a stated reason for confirmation if the verbs match. A Beat 5 that states only the final verb without naming the entering verb fails. A Beat 5 where the entering and final verb match but the confirmation is stated only by implication ("the signals supported the initial assessment") rather than by explicit named comparison fails. When the verbs differ, the change reason must name which signals or ledger entries (C-31) drove the revision. This criterion is the structural mechanism that converts C-22 (anti-stagnation) from an assertion into an auditable before/after record: the delta between inertia and conclusion is visible in the output as a named comparison, not inferred from surrounding prose. Depends on C-30 and C-22: C-32 cannot pass if C-30 fails; a C-32 PASS also requires C-22 PASS. |

---

## Scoring Formula

```
composite = (essential_pass / 4 × 60)
          + (recommended_pass / 3 × 20)
          + (aspirational_pass / 25 × 20)

PARTIAL counts as 0.5 toward aspirational_pass.
Golden threshold: all 4 essential PASS AND composite ≥ 85.
```

---

## Summary Table

| Tier | Count | Max Points |
|------|-------|------------|
| Essential | 4 | 60 |
| Recommended | 3 | 20 |
| Aspirational | 25 | 20 |
| **Total** | **32** | **100** |

---

## What Changed v10 → v11

Three new aspirational criteria extracted from Round 11 V-03 axis ("VERDICT as inertia recommendation"):

**C-30 — VERDICT as falsifiable inertia recommendation verb**
The entering recommendation verb is committed declaratively before analytic work begins, making the VERDICT a testable hypothesis rather than a directional preview. Without this, C-28 enforces placement but not commitment — the VERDICT can state orientation without being falsifiable by the signals.

**C-31 — Per-signal confirmation/challenge ledger**
The ANALYST produces a per-signal stance record (confirms / challenges / mixed) with a one-line rationale per signal, before synthesizing the pattern. Without this, synthesis is an opaque claim — the signal-level reasoning is asserted, not shown.

**C-32 — Beat 5 inertia-to-final comparison**
Beat 5 names both the entering verb and the final verb in the same structural location, with an explicit stated reason for any change or confirmation. This is the structural mechanism that makes C-22 (anti-stagnation) auditable: the before/after recommendation is visible as a named comparison rather than inferred from surrounding prose.

**Dependency chain for the new R11 cluster:**

```
C-28 → C-30 → C-31 (also requires C-26)
              C-32 (also requires C-22, which requires C-21)
```
