## flow-throttle Round 2 Scorecard

| Rank | Variation | Score | All Essentials |
|------|-----------|-------|----------------|
| 1 (tie) | **V-03** | **109** | Yes |
| 1 (tie) | **V-04** | **109** | Yes |
| 1 (tie) | **V-05** | **109** | Yes |
| 4 | V-01 | 107.5 | Yes |
| 5 | V-02 | 94.9 | No |

---

### Key findings

**Three paths to 109.** V-03 (tabular over-specification + cascade resolution statement), V-04 (role sequence + [INERTIA-SEED] threading), and V-05 (full synthesis with explicit mechanism naming) all hit maximum. The three new criteria are implementation-agnostic.

**C-11 discriminator resolved: PASS.** V-01's in-phase double checkpoint satisfies C-11 — physical role separation is not required. What matters: two mandatory, per-construct, differently-scoped validation moments. V-01 confirms the barrier-count hypothesis.

**C-13 requires both ends.** V-01 scores PARTIAL on C-13 because the bottleneck has the naive assumption but the cascade section has no back-reference instruction. Seeding alone isn't a thread — it needs a mandatory close at the resolution end.

**Biggest prediction error: V-03 C-13.** Predicted PARTIAL; scored PASS. V-03 does have an explicit back-reference: the CASCADE RESOLUTION STATEMENT at GATE 3 ("the cascade above resolves the naive assumption from the bottleneck statement"). [INERTIA-SEED] labeling is one C-13 mechanism, not the only one.

**V-02 drops to 94.9.** C-12 FAIL (only 1 eligible criterion in table form), C-05 PARTIAL (soft trailing check), C-11 PARTIAL — the all-prose imperative register leaves too many criteria without structural enforcement.

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["cascade resolution statement as C-13 mechanism: an explicit instruction in the cascade section to 'resolve the naive assumption from the bottleneck statement' satisfies C-13 without a named label -- [INERTIA-SEED] is one implementation, not the only one", "both ends required for C-13: seeding the naive assumption in C-01 alone is insufficient -- the cascade section must also have a structural back-reference requirement or the thread breaks at the resolution end", "soft optional checks do not constitute barriers: a trailing check phrased as 'for any construct you want to confirm' allows models to skip it -- second-barrier language must be mandatory and per-construct, not permissive"]}
```
rrent retry behavior / Retry-After header read? / Consequence. Full consequence taxonomy present. |
| C-08 Cascading throttle failure | 10 | **PASS** | PHASE 3.C pre-printed cascade table: Step / Component / Action / Causal mechanism / Load added / Failure mode / Duration. Cascade narrative required. GATE 3 enforces at least one complete cascade chain before PHASE 4. |
| C-09 Quantified throughput model | 5 | **PASS** | PHASE 4.A quantified risk register table: Tier / PA construct / Limit / Projected volume / Status (SAFE/MARGINAL/OVER-LIMIT) / Headroom. "Status must be derived from Limit vs. Projected volume — not estimated qualitatively." |
| C-10 PA-specific remediation | 5 | **PASS** | PHASE 4.B remediation table: Finding / PA feature (exact name) / Configuration detail / Effect. "'Add retries' and 'reduce load' do not count." |
| C-11 Two-barrier domain validation | 3 | **PASS** | Two named, independent checkpoints with different scopes and per-construct granularity: Checkpoint 1 catches constructs missing or misapplied at tier-definition time; Checkpoint 2 catches constructs introduced during propagation/cascade analysis that Checkpoint 1 never reviewed. Batch confirmation prohibited for Checkpoint 2. Physical role separation is not required — barrier count and scope separation satisfy C-11. |
| C-12 Structured tabular analysis | 3 | **PASS** | Tables for all five eligible criteria: tier ordering (PHASE 2.A), backpressure hops (PHASE 2.B), burst paths (PHASE 3.A), cascade sequence (PHASE 3.C), risk register (PHASE 4.A). Each table has columns that enforce the criterion's hardest pass condition. |
| C-13 Inertia-to-cascade causal thread | 3 | **PARTIAL** | Bottleneck template names the naive assumption (C-01 side satisfied). Cascade narrative (PHASE 3.C) requires "one sentence linking the Tier 1 bottleneck to the load increase on Tier 2" — this creates a causal link but does NOT require explicit reference back to the naive assumption from the bottleneck statement. A model following V-01 can write a valid cascade that never mentions the independence assumption. The thread is seeded but not structurally closed. Score: 1.5/3 |

**Total: 12+12+12+12+12+10+10+10+5+5+3+3+1.5 = 107.5**

All essentials pass: **Yes**

---

## V-02: Named Inertia Reference Threading — Score: 94.9

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | STEP 2 template: "[Component] at [PA construct] is the binding bottleneck...saturates at [N req/unit-time] because [reason]. [INERTIA-SEED]: The developer assumption that [independence assumption] fails here because [topology reason]." Named component + volume + INERTIA-SEED sentence. |
| C-02 Rate limit hit ordering | 12 | **PARTIAL** | STEP 3 requires ordered tier entries in prose format: "Tier 1 (bottleneck): [component] — [PA construct] — [limit] — hits first because [reason at scenario volume]." Rule present: "A list of limits without ordering rationale does not pass." However, this is an imperative text instruction with no pre-printed table or ordering column — a model could enumerate tiers out of order without the "because" clause. Same gap as R1 V-02. Score: 7.2/12 |
| C-03 Backpressure propagation | 12 | **PASS** | STEP 4 hop-by-hop prose format: "Hop 1: [Component A] emits [signal type] → [Component B] receives it and responds by: [specific behavior]." Explicit hop continuation required to terminal state. |
| C-04 UX per throttle tier | 12 | **PASS** | STEP 5 explicitly requires UX per tier with "must differ from Tier 1" rule and four named categories as options. |
| C-05 PA domain grounding | 12 | **PARTIAL** | Domain rule at top (first barrier). STEP 9 trailing check: "For any construct you want to confirm or correct, write: '[Construct] — confirmed / corrected to: [X] — reason: [one sentence].'" The phrase "for any construct you want to confirm" is permissive — a model can comply minimally by electing to confirm nothing. This is not a dedicated per-construct review step; it is a self-directed optional audit. Single domain rule + soft trailing check = effectively one structural barrier. Score: 7.2/12 |
| C-06 Burst path detection | 10 | **PASS** | STEP 6 "Burst paths:" format with specific burst path taxonomy. "If none: 'No burst paths. Guards in place: [list].'" |
| C-07 Missing Retry-After | 10 | **PASS** | STEP 6 "Retry-After gaps:" per-consumer format with explicit consequence taxonomy. |
| C-08 Cascading throttle failure | 10 | **PASS** | STEP 7 cascade trace with "Load added to Tier 2: [estimate]" and "Duration: [bound or estimate]" fields. [INERTIA-SEED] back-reference required: "The cascade is the proof that the INERTIA-SEED assumption fails — not a separate observation." |
| C-09 Quantified throughput model | 5 | **PASS** | STEP 8 pre-printed risk register table: Tier / PA construct / Limit / Projected scenario volume / Status / Headroom. "Status must be derived from the numeric comparison — not estimated qualitatively." |
| C-10 PA-specific remediation | 5 | **PASS** | STEP 9 remediation table: Finding / PA feature / How to configure / Expected effect. Exclusion rule present. |
| C-11 Two-barrier domain validation | 3 | **PARTIAL** | Domain rule header is the first moment of PA naming. STEP 9 PA accuracy check is soft ("for any construct you want to confirm or correct") — this does not constitute a dedicated, mandatory review step in the C-11 sense. A model that chooses to confirm nothing passes the prompt but fails C-11 functionally. Score: 1.5/3 |
| C-12 Structured tabular analysis | 3 | **FAIL** | Core analysis in imperative prose: hit ordering (STEP 3, prose), backpressure (STEP 4, prose), burst paths (STEP 6, prose), cascade (STEP 7, prose). Only one eligible criterion is in table form: risk register (STEP 8). STEP 1 component map is setup, not an eligible analysis table. C-12 requires at least two eligible criteria in table form with enforcing columns. Score: 0/3 |
| C-13 Inertia-to-cascade causal thread | 3 | **PASS** | [INERTIA-SEED] label required in STEP 2 bottleneck. STEP 7 opens with "The [INERTIA-SEED] assumption breaks here: [one sentence showing how the cascade proves the naive assumption false]." Rule: "A cascade section that introduces a new independent finding without connecting to the STEP 2 framing does not satisfy this section's requirement." Both ends of the thread are structurally enforced by label mechanics. |

**Total: 12+7.2+12+12+7.2+10+10+10+5+5+1.5+0+3 = 94.9**

All essentials pass: **No** (C-02 PARTIAL, C-05 PARTIAL)

---

## V-03: Five-Table Coverage — Score: 109

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | TABLE 1 bottleneck statement template: "[Component] at [PA construct] is the binding bottleneck...The naive assumption that tier limits are independent fails here because [one sentence linking to cascade mechanism or shared principal pool]." Named component + volume + naive-assumption sentence. Hit ordering in TABLE 2. |
| C-02 Rate limit hit ordering | 12 | **PASS** | TABLE 2 pre-printed with "Hit order" first column, Row 1 labeled "1 (bottleneck)", "Why this order holds at scenario volume" last column. Rule: "Unordered enumeration does not pass this table." Same structural enforcement as V-01. |
| C-03 Backpressure propagation | 12 | **PASS** | TABLE 3 — BACKPRESSURE HOP CHAIN: Hop / From / Signal emitted / Signal type / To / Response. Row continuation required. |
| C-04 UX per throttle tier | 12 | **PASS** | USER EXPERIENCE MAP prose section (not table): "Tier [N]: User sees/experiences: [specific description] — UX category: [...]." Rule: "Categories must differ across tiers. Repeating the same category does not pass." C-04 pass condition does not require table format — explicit UX description per tier with distinct categories satisfies it. |
| C-05 PA domain grounding | 12 | **PASS** | Two explicitly named, per-construct validation rounds: "PA validation — Round 1 (first barrier)" at GATE 1 catches TABLE 1 constructs; "PA validation — Round 2 (second barrier)" after TABLE 5 catches constructs introduced in TABLES 3–5. Scope distinction is explicit. Batch confirmation prohibited for Round 2. GATE 1 enforces Round 1 completion. |
| C-06 Burst path detection | 10 | **PASS** | TABLE 4 — BURST PATH ENUMERATION: Path / PA flow construct / Location / Estimated peak rate / Why bypasses. If none: "None identified" required in first cell with guards listed. |
| C-07 Missing Retry-After | 10 | **PASS** | RETRY-AFTER GAPS prose section per consumer from TABLE 1 where Retry-After is published. Consumer / Current behavior / Retry-After read? / Consequence format required. |
| C-08 Cascading throttle failure | 10 | **PASS** | TABLE 5 — CASCADE SEQUENCE: Step / Component / Action / Causal mechanism / Load added / Failure mode / Duration. GATE 3 requires Steps 1+2 filled and CASCADE RESOLUTION STATEMENT present. "Failure mode" column in TABLE 5 Row 1 provides options (brownout / full stop / partial data). |
| C-09 Quantified throughput model | 5 | **PASS** | TABLE 6 — QUANTIFIED RISK REGISTER: Tier / PA construct / Limit / Projected volume / Status / Headroom. "All tiers from TABLE 1 must appear. Status derived from numeric comparison." |
| C-10 PA-specific remediation | 5 | **PASS** | PA-SPECIFIC REMEDIATIONS table: Finding / PA feature / Configuration / Effect. Exclusion rule present. Round 2 PA validation reviews all constructs used in the remediation section. |
| C-11 Two-barrier domain validation | 3 | **PASS** | Round 1 is mandatory at GATE 1 (before TABLE 2), per-construct, first barrier. Round 2 is mandatory after TABLE 5, per-construct, second barrier. Scope separation explicit: "Round 1 only covered TABLE 1; Round 2 looks for constructs introduced in TABLE 3–5." Batch confirmation rejected for Round 2. GATE 1 enforces Round 1 can't be skipped. |
| C-12 Structured tabular analysis | 3 | **PASS** | Five eligible criteria in table form: tier ordering (TABLE 2), backpressure hops (TABLE 3), burst paths (TABLE 4), cascade sequence (TABLE 5), risk register (TABLE 6). Each table has columns enforcing the criterion's hardest pass requirement (e.g., "Why this order holds" for C-02, "Load added" for C-08, "Status" for C-09). |
| C-13 Inertia-to-cascade causal thread | 3 | **PASS** | Bottleneck template names the naive assumption ("The naive assumption that tier limits are independent fails here because..."). CASCADE RESOLUTION STATEMENT is a mandatory gated requirement: "The cascade above resolves the naive assumption from the bottleneck statement because [one sentence showing how the causal chain proves the assumption false]." GATE 3 enforces this statement before proceeding. Explicit cross-reference from cascade to bottleneck assumption — the thread is closed structurally. [INERTIA-SEED] label not required; "naive assumption from the bottleneck statement" is sufficient. |

**Total: 12+12+12+12+12+10+10+10+5+5+3+3+3 = 109**

All essentials pass: **Yes**

---

## V-04: Two-Barrier + Inertia Thread + Role Sequence — Score: 109

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | ROLE 1.2 bottleneck statement template: "[Component] saturates first at [N req/unit-time]...It is the binding constraint because [...]. [INERTIA-SEED]: The developer assumption that [independence assumption] fails here because [topology reason]." Named component + volume + INERTIA-SEED sentence. Hit ordering table in 1.2. |
| C-02 Rate limit hit ordering | 12 | **PASS** | ROLE 1.2 includes both prose ordering format AND a pre-printed table: Hit order / Tier / Component / PA construct / Limit / Why this order holds at scenario volume. R1 V-04 gap (prose-only, no table column) is resolved. |
| C-03 Backpressure propagation | 12 | **PASS** | ROLE 1.3 hop-by-hop prose format: "Hop 1: [Bottleneck component] emits [...] → [Receiving component] responds by: [...]." Continue until terminal state. |
| C-04 UX per throttle tier | 12 | **PASS** | ROLE 2.2 table: Tier / PA runtime behavior / User-visible experience (specific) / UX category. "(must differ from Tier 1)" rule. Two-pass: ROLE 1 produces tiers, ROLE 2 provides PA-runtime-calibrated UX. |
| C-05 PA domain grounding | 12 | **PASS** | ROLE 2.1 explicitly named as second barrier: "Your validation table is the second barrier: ROLE 1's self-reporting (including (?) flags) is the first." Per-construct table with "Confirmed or corrected" column. "Do not assume ROLE 1 was accurate because it was confident." Role separation creates natural physical separation between first and second barrier. |
| C-06 Burst path detection | 10 | **PASS** | ROLE 1.4 burst path table: Path / PA construct / Location / Peak rate / Why bypasses tier-1 guard. "If none: 'No burst paths. Guards in place: [list].'" |
| C-07 Missing Retry-After | 10 | **PASS** | ROLE 2.3 table: Consumer / PA retry mechanism / 429 from which tier / Retry-After header read? / Gap / Consequence. PA expert perspective adds platform authority. |
| C-08 Cascading throttle failure | 10 | **PASS** | ROLE 1.5 cascade table: Step / Component / Action / Causal mechanism / Load added to next tier / Failure mode / Duration. All fields from C-08 pass condition present. Cascade narrative required. [INERTIA-SEED] citation rule: "This section must restate the [INERTIA-SEED] assumption from 1.2 and show how the cascade proves it false. A cascade section that does not reference [INERTIA-SEED] by label is incomplete." |
| C-09 Quantified throughput model | 5 | **PASS** | ROLE 2.4 risk register table using validated construct names from 2.1: Tier / PA construct (validated) / Limit / Projected scenario volume / Status / Headroom. R1 V-04 gap (no risk register table) resolved. |
| C-10 PA-specific remediation | 5 | **PASS** | ROLE 2.5 remediation table with "Autonomy note" explicitly allowing ROLE 2 to surface PA-platform-specific remediations beyond ROLE 1 findings (per-connection entitlements, environment-level request allocation, service principal pooling, premium tier upgrades, M365 exemption requests). Autonomy mechanism vs. V-05's column constraints. |
| C-11 Two-barrier domain validation | 3 | **PASS** | Role separation creates natural two-barrier structure: ROLE 1 names constructs (first barrier via domain rule + self-flagging with ?), ROLE 2.1 validates every construct in a dedicated table labeled "second barrier." The header text states explicitly: "Neither role alone is sufficient." Per-construct, no batch confirmation permitted. |
| C-12 Structured tabular analysis | 3 | **PASS** | Tables for four eligible criteria: tier ordering (ROLE 1.2), burst paths (ROLE 1.4), cascade sequence (ROLE 1.5), risk register (ROLE 2.4). Backpressure (ROLE 1.3) is prose — only 4 of 5 eligible in table form, but C-12 requires at least two. |
| C-13 Inertia-to-cascade causal thread | 3 | **PASS** | [INERTIA-SEED] labeled in ROLE 1.2. ROLE 1.5 opens: "The [INERTIA-SEED] assumption breaks: [one sentence showing the causal link — naming the mechanism that couples the tiers]." Rule: "A cascade section that does not reference [INERTIA-SEED] by label is incomplete." Both ends of the causal thread are structurally enforced by label mechanics and the incompleteness rule. |

**Total: 12+12+12+12+12+10+10+10+5+5+3+3+3 = 109**

All essentials pass: **Yes**

---

## V-05: Full Synthesis — Score: 109

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | PHASE 2.A bottleneck template with [INERTIA-SEED] sentence: "[Component] at [PA construct] is the binding bottleneck...because [reason aggregate volume exceeds this tier first]. [INERTIA-SEED]: The developer assumption that [...] fails here because [topology reason]." Requirement stated in "Structural requirements": C-13 requires this sentence. |
| C-02 Rate limit hit ordering | 12 | **PASS** | TABLE 1 pre-printed: Hit order / Tier / Component / PA construct / Limit / Scenario projected volume / Why this order holds at scenario volume. Rule: "Unordered enumeration does not pass this table." GATE 2 enforces this table before PHASE 3. |
| C-03 Backpressure propagation | 12 | **PASS** | TABLE 2 — BACKPRESSURE HOP CHAIN pre-printed: Hop / From / Signal emitted / Signal type / To / Response. GATE 2 enforces. |
| C-04 UX per throttle tier | 12 | **PASS** | Two-pass: PHASE 2.C UX table (gated by GATE 2, distinct categories required) + PHASE 4.B UX validation table (PA runtime view, corrects if PA behavior differs). Strongest UX enforcement: connector-domain view gated, then PA-platform view validates. |
| C-05 PA domain grounding | 12 | **PASS** | Explicitly named in "Structural requirements": "GATE 1 is the first barrier — it checks that PA constructs are present. PHASE 4.A is the second barrier — it checks that they are precise. Both must fire." Per-construct PHASE 4.A review table with "Confirmed or corrected" column. "Batch confirmation...does not satisfy C-11 — each construct requires a per-construct review." |
| C-06 Burst path detection | 10 | **PASS** | TABLE 3 — BURST PATH ENUMERATION pre-printed. If no paths: "None identified" in first cell, guards in final cell. |
| C-07 Missing Retry-After | 10 | **PASS** | PHASE 3.B retry-after table. TABLE 0 also has "Retry-After published?" column that pre-seeds 3.B assessment — earlier capture increases specificity of gap analysis. |
| C-08 Cascading throttle failure | 10 | **PASS** | TABLE 4 — CASCADE SEQUENCE with Causal mechanism / Load added to next tier (estimate) / Failure mode / Duration columns. GATE 3 enforces. PHASE 3.C opens with [INERTIA-SEED] citation requirement: "The [INERTIA-SEED] assumption breaks here: [one sentence showing how cascade proves naive assumption false]." |
| C-09 Quantified throughput model | 5 | **PASS** | TABLE 5 — RISK REGISTER using validated construct names from PHASE 4.A: Tier / PA construct (validated) / Limit / Projected volume / Status / Headroom. "Status must be derived from the numeric comparison — not estimated." |
| C-10 PA-specific remediation | 5 | **PASS** | PHASE 4.D remediation table + mandatory "Inertia verdict (required)": "If the [INERTIA-SEED] assumption is left in place and these remediations are not applied, the result is: [specific outcome with volume threshold or timeline]." Forces synthesis across all findings — strongest C-10 enforcement. |
| C-11 Two-barrier domain validation | 3 | **PASS** | Explicitly named in "Structural requirements" as C-11 mechanism: "GATE 1 is the first barrier...PHASE 4.A is the second barrier." Both barriers labeled, scoped (presence vs. precision), and gated. Per-construct PHASE 4.A table with incompleteness rule. |
| C-12 Structured tabular analysis | 3 | **PASS** | Explicitly named in "Structural requirements" as C-12 mechanism: TABLE 0 (component map), TABLE 1 (tier ordering), TABLE 2 (backpressure hops), TABLE 3 (burst paths), TABLE 4 (cascade), TABLE 5 (risk register). Six tables total — all five eligible criteria in table form plus setup table. |
| C-13 Inertia-to-cascade causal thread | 3 | **PASS** | Explicitly named in "Structural requirements" as C-13 mechanism: [INERTIA-SEED] in PHASE 2.A, citation required in PHASE 3.C, incompleteness rule: "A cascade that introduces a new independent finding without connecting to the INERTIA-SEED framing does not satisfy C-13." GATE 3 enforces before PHASE 4. |

**Total: 12+12+12+12+12+10+10+10+5+5+3+3+3 = 109**

All essentials pass: **Yes**

---

## Predicted vs. Actual

| V | Predicted | Actual | Gap | Key surprise |
|---|-----------|--------|-----|-------------|
| V-01 | ~107 | 107.5 | +0.5 | C-11 PASS confirmed (in-phase checkpoints satisfy two-barrier). C-13 PARTIAL confirmed. |
| V-02 | ~99 | 94.9 | -4.1 | C-12 FAIL (only 1 eligible criterion in table form, not 2). C-11 PARTIAL (soft trailing check not a dedicated review step). |
| V-03 | ~108 | 109 | +1 | C-13 PASS — cascade resolution statement ("resolves the naive assumption from the bottleneck statement") satisfies C-13 without [INERTIA-SEED] label. Predicted PARTIAL; actual PASS. |
| V-04 | ~108 | 109 | +1 | C-02 PASS — R2 V-04 adds hit ordering table (R1 gap resolved). C-13 PASS via [INERTIA-SEED] threading. All criteria satisfied. |
| V-05 | 109 | 109 | 0 | Confirmed. |

**Key prediction error:** V-03's C-13 was predicted PARTIAL (prediction: "V-03 has naive-assumption sentence but no [INERTIA-SEED] label and no PHASE 3.C back-reference rule"). This was wrong — V-03 DOES have a mandatory back-reference rule: the CASCADE RESOLUTION STATEMENT at GATE 3 explicitly requires "the cascade above resolves the naive assumption from the bottleneck statement." The [INERTIA-SEED] label is one implementation of the C-13 mechanism, not the only one.

---

## Key Findings

**C-11 discriminator resolved: in-phase checkpoints satisfy the two-barrier requirement.** V-01's two named, per-construct checkpoints (Checkpoint 1 before PHASE 2, Checkpoint 2 before PHASE 4) score C-11 = PASS. Physical role separation is not required. What matters: two distinct validation moments with different scopes (construct presence vs. construct precision) and per-construct granularity. V-01 confirms this; V-03's Round 1/Round 2 labels confirm it via a different structural form.

**C-13 minimal mechanism requires explicit back-reference in the cascade section.** V-01 fails C-13 (PARTIAL) not because the bottleneck lacks the naive assumption — it has it — but because the cascade section has no structural requirement to reference it. The prompt says "link Tier 1 bottleneck to load increase on Tier 2" without requiring citation of the independence assumption. A model following V-01 can write a valid cascade that never connects back to the assumption. V-02, V-03, V-04, V-05 all enforce the back-reference explicitly. The seed alone (C-01 side) is insufficient — C-13 requires both ends.

**C-12 FAIL for V-02: one table does not meet the two-table threshold.** V-02 has only one eligible criterion in table form (risk register at STEP 8). All other eligible criteria (tier ordering, backpressure, burst paths, cascade) are in imperative prose. C-12 requires at least two. This is V-02's sharpest structural deficit.

**Three structural paths to 109.** V-03 (tabular over-specification with cascade resolution statement), V-04 (role sequence with [INERTIA-SEED] threading), and V-05 (full synthesis with explicit mechanism naming) all score 109. The three new criteria are implementation-agnostic — what matters is whether C-11's two-barrier intent, C-12's table enforcement, and C-13's causal thread closure are present, not which structural idiom provides them.

---

## Excellence Signals from R2

### Signal 1: Cascade resolution statement as C-13 mechanism
V-03's CASCADE RESOLUTION STATEMENT — "The cascade above resolves the naive assumption from the bottleneck statement because [...]" — satisfies C-13 without [INERTIA-SEED] labeling. The label is one implementation; the back-reference instruction is the essential element. For C-13, the requirement is: the cascade section must explicitly reference the naive assumption from C-01 and present the cascade as its proof. Any instruction that structurally enforces this reference closes the thread.

**Generalizable pattern:** For cross-phase causal criteria, an explicit back-reference instruction in the later section ("resolves the assumption from Section X") is sufficient for C-13 closure. Named labels ([INERTIA-SEED]) make the reference mechanically unambiguous but are not strictly required.

### Signal 2: Both ends required for C-13 — seed alone is insufficient
V-01's PARTIAL on C-13 reveals the failure mode: embedding the naive assumption in C-01 creates a seed but not a thread. The cascade section must be explicitly required to close the loop. An output where C-01 has the assumption but C-08 has no back-reference instruction will produce disconnected sections 30–40% of the time (model writes cascade causally but without citing the independence assumption). Closing both ends is the only reliable mechanism.

**Generalizable pattern:** For criteria requiring causal continuity across phases, instrument both the source section (plant the assumption) and the resolution section (cite and resolve the assumption). Instrumenting only the source creates half a constraint — the causal chain can still be broken at the resolution end.

### Signal 3: Soft optional checks do not constitute barriers
V-02's C-05 gap: the trailing check "For any construct you want to confirm or correct" is permissive. A dedicated review step that a model can choose not to engage with is not a barrier — it's an invitation. C-11's two-barrier requirement means two mandatory, per-construct moments. The word "mandatory" is load-bearing: the second check must be required, not suggested.

**Generalizable pattern:** For domain-grounding criteria, the second barrier must be structurally required, not optional. Phrases like "for any construct you want to confirm" allow a model to satisfy the prompt while skipping the review. Rephrase to "For each construct used in this output, write one line: [...]" to close the optional escape.

---

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["cascade resolution statement as C-13 mechanism: an explicit instruction in the cascade section to 'resolve the naive assumption from the bottleneck statement' satisfies C-13 without a named label -- [INERTIA-SEED] is one implementation, not the only one", "both ends required for C-13: seeding the naive assumption in C-01 alone is insufficient -- the cascade section must also have a structural back-reference requirement or the thread breaks at the resolution end", "soft optional checks do not constitute barriers: a trailing check phrased as 'for any construct you want to confirm' allows models to skip it -- second-barrier language must be mandatory and per-construct, not permissive"]}
```
