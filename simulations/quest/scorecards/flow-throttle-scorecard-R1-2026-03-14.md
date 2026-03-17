## flow-throttle — Round 1 Scorecard

### Rankings

| Rank | Variation | Score | All essentials | Main gap |
|------|-----------|-------|----------------|----------|
| 1 | **V-05** | **100** | **Yes** | — |
| 2 | V-03 | 95 | No | C-05 single-pass only |
| 3 | V-01 | 91 | No | C-05 single-pass + C-08 ungated |
| 4 | V-04 | 89 | No | C-02 text-ordered + C-08 ungated + C-09 absent |
| 5 | V-02 | 84 | No | C-02 text-ordered + C-05 weakest + C-09 partial |

### Key findings

**C-05 is the discriminating criterion.** Every variation except V-04 and V-05 scores PARTIAL (7.2/12) on PA domain grounding. A single domain rule header catches intentional omission but not terminology drift. V-04 and V-05 are the only variations with a second-pass validation role — the "confirmed / corrected" column forces the PA expert to either affirm or flag each construct, making inaccuracy structurally visible.

**V-04 confirmed the wildcard prediction.** It produces the strongest single-mechanism C-05 (12/12 via ROLE 2.1), but loses on C-02 (no table ordering column) and C-09 (no risk register), landing at 89. The role sequence is a real mechanism but can't compensate for missing format structure.

**The V-03 → V-05 gap is 5 points, entirely from C-05.** The fix is one addition: a PA validation role with a correction column.

### Excellence signals (3 new patterns)

1. **Two-barrier essential enforcement** — gate catches missing constructs, validation role catches imprecise ones. Neither alone is sufficient for domain-grounding criteria.
2. **Pre-printed tables within gated phases** — table columns prevent prose shortcuts, gates prevent section skipping. Combining both locks criteria where both failure modes are plausible.
3. **Inertia framing as cross-phase cascade catalyst** — embedding "the naive assumption fails here because..." in the bottleneck statement seeds cascade reasoning before the cascade section fires, creating a causal thread across phases rather than an isolated checklist item.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["two-barrier essential enforcement: gate catches missing constructs, validation role catches imprecise ones -- neither alone sufficient for domain-grounding criteria", "pre-printed tables within gated phases: table columns prevent prose shortcuts, gates prevent section skipping -- combining both locks criteria where both failure modes are plausible", "inertia framing as cross-phase cascade catalyst: embedding naive-assumption language in the bottleneck statement seeds cascade reasoning before the cascade section fires"]}
```
ion — cascade could be provided without numeric load estimate or characterized shallowly. Score: 6/10 |
| C-09 Quantified throughput | 5 | **PASS** | QUANTIFIED RISK SUMMARY table with Limit / Projected volume / Status (SAFE/MARGINAL/OVER-LIMIT) / Headroom-deficit columns. Numeric comparison table is pre-printed. |
| C-10 PA-specific remediation | 5 | **PASS** | PA-SPECIFIC REMEDIATIONS section with explicit template: PA feature (exact name), Problem addressed, Configuration. "'Add retries' and 'reduce load' do not count" rule present. |

**Total: 12+12+12+12+7.2+10+10+6+5+5 = 91**

All essentials pass: **No** (C-05 is PARTIAL)

---

## V-02: Imperative Register — Score: 84

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | Step 3: "Write exactly: '[Specific component name] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] because...'" Plus explicit prohibition: "Do not say 'the system slows down.' Do not say 'the API.' Name the component." |
| C-02 Rate limit hit ordering | 12 | **PARTIAL** | Step 4 provides ordered format "Tier N: -- bottleneck first -- why before next tier:" but relies on text instruction rather than a table column that structurally enforces ordering. A model could enumerate tiers without the "why before next tier" explanation. Score: 7.2/12 |
| C-03 Backpressure propagation | 12 | **PASS** | Step 5 explicitly: "For each propagation hop, write: [Component A] emits [signal] / [Component B] receives it and responds by:". Hop-by-hop format enforced imperatively. |
| C-04 UX per throttle tier | 12 | **PASS** | Step 6 explicitly: "Not what the system does internally -- what the user's experience is." "Tier 2: [must differ from Tier 1]". Four UX categories listed as options to choose from. |
| C-05 PA domain grounding | 12 | **PARTIAL** | "Before you start" rule with PA construct types listed. But single-pass; no validation role or second check. Weakest C-05 enforcement of all variations -- the "Before you start" framing is easier for a model to satisfy with partial compliance than a structural gate. Score: 7.2/12 |
| C-06 Burst path detection | 10 | **PASS** | Step 7 provides explicit checklist of burst patterns (Apply to Each, parallel branches, high-frequency trigger). "For each burst path found: name construct, estimate peak rate, explain why it overwhelms tier-1." |
| C-07 Missing Retry-After | 10 | **PASS** | Step 8 explicitly asks for Retry-After assessment per consumer with behavior classification. "name the consequence (hammering / premature retry / extended outage)" |
| C-08 Cascade failure | 10 | **PARTIAL** | Step 9 has cascade format with Tier 1 / causal mechanism / Tier 2 / failure mode. But no gate before remediation (Step 10 combines quantification and remediation), and "Load added" field absent -- cascade could be qualitative only. Score: 6/10 |
| C-09 Quantified throughput | 5 | **PARTIAL** | Step 10: "For each tier, write: limit=[N/unit], projected=[N/unit], status=[SAFE / MARGINAL / OVER-LIMIT]". Format is there but no pre-printed table -- model might compress or skip tiers. Score: 3/5 |
| C-10 PA-specific remediation | 5 | **PASS** | Step 10 remediation: at least two, with PA feature exact name, addresses specific finding, configure what + value. "'Add retries' and 'reduce load' do not count." |

**Total: 12+7.2+12+12+7.2+10+10+6+3+5 = 84**

All essentials pass: **No** (C-02 and C-05 are PARTIAL)

---

## V-03: Explicit Gated Phases — Score: 95

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | PHASE 2, section 2A: "Bottleneck statement: '[Specific component] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario because [reason the ordering holds for this aggregate volume].'" Named component + volume in sentence template. |
| C-02 Rate limit hit ordering | 12 | **PASS** | PHASE 2, 2A: Pre-printed table with "Hit order" as first column, "Why this order" as last column. Row 1 labeled "1 (bottleneck)". Same structural enforcement as V-01 -- table column prevents unordered list. |
| C-03 Backpressure propagation | 12 | **PASS** | PHASE 2, 2B: "Hop 1: [Bottleneck component] emits [...] -> received by [...] -> response: [...]". Multi-hop chain required, gated by GATE 2. |
| C-04 UX per throttle tier | 12 | **PASS** | PHASE 2, 2C: UX table with "(Repeating the same UX category across two rows does not pass.)" Gated by GATE 2 which requires "UX mapping (at least two tiers with distinct UX categories)" to be complete. |
| C-05 PA domain grounding | 12 | **PARTIAL** | Domain rule header + PA construct column in PHASE 1 tiers table. GATE 1 checks "Each PA tier row has an exact PA construct name" which is a partial gate. But no second-pass validation role -- GATE 1 prevents missing PA constructs, not imprecise ones. Score: 7.2/12 |
| C-06 Burst path detection | 10 | **PASS** | PHASE 3, 3A: Gated sub-section with Construct / Peak rate / Exposure template. GATE 2 must fire first. "If none: explicit acknowledgment with guards listed." |
| C-07 Missing Retry-After | 10 | **PASS** | PHASE 3, 3B: Gated sub-section with full Retry-After behavior table. Consumer / Action / Behavior / Consequence columns. |
| C-08 Cascade failure | 10 | **PASS** | PHASE 3, 3C: Gated sub-section with full cascade template including Causal link, Load added, Failure mode, Duration. GATE 3 requires "at least one complete cascade chain" before PHASE 4 can begin. Strongest gated cascade enforcement of any single-mechanism variation. |
| C-09 Quantified throughput | 5 | **PASS** | PHASE 4, 4A: "QUANTIFIED RISK REGISTER" table with Limit / Projected volume / Status (SAFE / MARGINAL / OVER-LIMIT) / Headroom-deficit. Pre-printed with all comparison columns. |
| C-10 PA-specific remediation | 5 | **PASS** | PHASE 4, 4B: Named PA feature required, "'Add retries' and 'reduce load' do not count", Finding addressed links back to PHASES 2-3 labels. |

**Total: 12+12+12+12+7.2+10+10+10+5+5 = 95**

All essentials pass: **No** (C-05 is PARTIAL -- the only gap between V-03 and V-05)

---

## V-04: Role Sequence — Score: 89

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | ROLE 1.2: "Bottleneck declaration: '[Specific component name] saturates first under this scenario at [N req/unit]. It is the binding constraint because [reason].'" Named component + volume required. |
| C-02 Rate limit hit ordering | 12 | **PARTIAL** | ROLE 1.2 produces ordered tier list ("Tier 1 (bottleneck): -- Tier 2: -- why after Tier 1:") but it is text-formatted, not a pre-printed table with ordering column. Risk that ordering explanation is absent or tiers are listed out of sequence. Score: 7.2/12 |
| C-03 Backpressure propagation | 12 | **PASS** | ROLE 1.3: "Hop 1: [Bottleneck component] emits [...] -> [Receiving component] responds by: [...]". Multi-hop until terminal state. |
| C-04 UX per throttle tier | 12 | **PASS** | ROLE 2.2: Dedicated PA expert section with PA runtime behavior / User-visible experience / UX category columns. "(UX categories must differ across rows.)" Two-pass: Connectors expert owns tiers, PA expert owns UX -- role separation makes distinct-outcome enforcement more reliable. |
| C-05 PA domain grounding | 12 | **PASS** | ROLE 2.1: Dedicated "PA Construct Validation" section with "Confirmed / corrected" column. PA expert explicitly reviews each tier and consumer from ROLE 1, naming the exact PA construct and flagging imprecise terminology. Strongest single-variation C-05 mechanism (but V-05 adds GATE 1 on top). |
| C-06 Burst path detection | 10 | **PASS** | ROLE 1.4: Explicit checklist-style assessment for each burst pattern (Apply to Each concurrency control, parallel branches, high-frequency trigger, other loops). Each burst risk: Construct / Peak rate / Exposure. |
| C-07 Missing Retry-After | 10 | **PASS** | ROLE 2.3: PA runtime view table with Consumer / PA retry mechanism / Retry-After header behavior / Gap columns. PA expert perspective adds domain authority to the assessment. |
| C-08 Cascade failure | 10 | **PARTIAL** | ROLE 1.5 has cascade chain format (Tier 1 -> causal mechanism -> Tier 2, failure mode) but the template is less structured than V-03/V-05: no "Load added" field, no Duration, no cascade label for cross-referencing. No gating before remediation. Score: 6/10 |
| C-09 Quantified throughput | 5 | **PARTIAL** | No dedicated risk register table. Numbers are embedded in ROLE 1.2 tier list (limit + volume present) but no side-by-side comparison table with Status column. ROLE 2.4 may not explicitly compare volumes to limits. Score: 3/5 |
| C-10 PA-specific remediation | 5 | **PASS** | ROLE 2.4: Two remediations required, exact PA feature name, exact configuration, addresses specific finding from ROLE 1. |

**Total: 12+7.2+12+12+12+10+10+6+3+5 = 89**

All essentials pass: **No** (C-02 is PARTIAL)

---

## V-05: Full Synthesis — Score: 100

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 Bottleneck localization | 12 | **PASS** | PHASE 2.A: Pre-printed table Row 1 = bottleneck + Bottleneck statement template. Template extends the inertia link: "The naive assumption that limits are independent fails here because [one sentence linking to cascade or shared principal]." Embeds C-01 into cascade reasoning -- shallow declarations are functionally incomplete. |
| C-02 Rate limit hit ordering | 12 | **PASS** | PHASE 2.A: Pre-printed table with "Hit order" as first column, Row 1 labeled "1 (bottleneck)". Same pre-printed column enforcement as V-01/V-03. |
| C-03 Backpressure propagation | 12 | **PASS** | PHASE 2.B: Pre-printed hop table with From / Signal / Signal type / To / Response columns. Gated by GATE 2 alongside C-02/C-04. |
| C-04 UX per throttle tier | 12 | **PASS** | Two-pass enforcement: PHASE 2.C (Connectors expert view, gated by GATE 2) + PHASE 4.B (PA expert validates/corrects each 2.C entry). Same distinct-category rule applied both passes. Matches V-04's two-pass strength with added gate enforcement. |
| C-05 PA domain grounding | 12 | **PASS** | Two structural barriers: GATE 1 requires "All tier rows have named PA constructs" before PHASE 2 begins (catches missing constructs); PHASE 4.A PA expert validation table with "confirmed / corrected" column (catches imprecise constructs). Neither barrier alone is sufficient; together they close both gaps. |
| C-06 Burst path detection | 10 | **PASS** | PHASE 3.A: Pre-printed burst path table with Path / PA construct / Location / Peak rate / Why it bypasses tier-1 guard columns. Gated by GATE 2 -- pre-printed table columns + gate together. |
| C-07 Missing Retry-After | 10 | **PASS** | PHASE 3.B: Pre-printed Retry-After gap table. Gated. Consumer row in PHASE 1 also has "Retry-After read?" column (yes/no/N/A) that pre-seeds the 3.B assessment -- earlier capture of the gap makes 3.B analysis more specific. |
| C-08 Cascade failure | 10 | **PASS** | PHASE 3.C: Pre-printed cascade template with Mechanism / Load added to Tier 2 / Duration fields. Gated by GATE 3. Inertia framing (Rule 4: "find where that assumption breaks") reinforces cascade discovery as the prompt's primary objective, not just a checklist item. Three reinforcements: pre-printed template + gate + inertia framing. |
| C-09 Quantified throughput | 5 | **PASS** | PHASE 4.C: Pre-printed QUANTIFIED RISK REGISTER table with Limit / Projected volume / Status / Headroom-deficit. All tiers from PHASE 2 required to appear. Completes the PHASE 1 aggregate volume -> PHASE 2 tiers -> PHASE 4.C status chain. |
| C-10 PA-specific remediation | 5 | **PASS** | PHASE 4.D: Pre-printed remediation table with Finding addressed / PA feature (exact name) / Configuration / Effect on finding columns. Inertia verdict field at the end requires a one-sentence consequence statement -- forces synthesis across all findings. |

**Total: 12+12+12+12+12+10+10+10+5+5 = 100**

All essentials pass: **Yes** -- all five C-01 through C-05 are PASS.

---

## Rankings

| Rank | Variation | Score | All essentials | Gap from V-05 | Main gap |
|------|-----------|-------|----------------|---------------|----------|
| 1 | **V-05** | **100** | **Yes** | -- | -- |
| 2 | V-03 | 95 | No | 5 | C-05 single-pass only |
| 3 | V-01 | 91 | No | 9 | C-05 single-pass + C-08 ungated |
| 4 | V-04 | 89 | No | 11 | C-02 text-ordered + C-08 ungated + C-09 absent |
| 5 | V-02 | 84 | No | 16 | C-02 text-ordered + C-05 weakest + C-09 partial |

---

## Excellence Signals from V-05

Three patterns account for V-05's advantage over V-03 (second-best):

### Signal 1: Two-barrier essential enforcement
V-03's only C-05 mechanism is the domain rule header + PA construct column (one barrier). V-05 adds a GATE 1 check before PHASE 2 and a dedicated PHASE 4.A validation table. The gate catches **missing** PA constructs; the validation role catches **imprecise** ones. Neither alone is sufficient -- a model can satisfy a domain rule header with plausible-sounding PA terminology that isn't accurate. The "confirmed / corrected" column forces the PA expert to either affirm or flag the terminology, making inaccuracy structurally visible.

**Generalizable pattern:** For domain-grounding criteria, a single rule instruction catches intentional omission but not drift. Add a validation role with an explicit correction column to catch drift.

### Signal 2: Pre-printed tables within gated phases
V-01 has pre-printed tables (strong format enforcement) but no gating. V-03 has phase gates (strong coverage enforcement) but fewer pre-printed tables. V-05 combines both: the burst path table in 3.A has pre-printed columns AND is gated by GATE 2. The cascade template in 3.C has "Load added to Tier 2" as a pre-printed field AND is gated by GATE 3. Each criterion's hardest pass condition -- the one that a well-intentioned model would shortcut -- is locked behind both a table column and a gate.

**Generalizable pattern:** Format (table columns) prevents prose shortcuts. Gates prevent section skipping. The combination is needed for criteria where both prose shortcuts and section skipping are plausible failure modes.

### Signal 3: Inertia framing as cross-phase cascade catalyst
The bottleneck statement template in PHASE 2.A contains: "The naive assumption that limits are independent fails here because [one sentence linking to cascade or shared principal]." This embeds C-08 into C-01 -- the model cannot complete the bottleneck declaration without starting cascade reasoning. By the time PHASE 3.C arrives, the cascade hypothesis is already seeded in the bottleneck statement. V-05 is the only variation that creates this causal thread across phases rather than treating cascade as an isolated checklist item.

**Generalizable pattern:** For criteria with causal dependencies (cascade requires bottleneck reasoning to exist), embed a forward reference in the earlier criterion's template rather than relying on a standalone later section.

---

## Round 1 Findings

**Predicted vs. actual:** Pre-round predicted V-05 as golden, V-03 as closest competitor, V-04 as wildcard on C-05. This holds. V-04's role sequence does produce the strongest single-mechanism C-05 (12/12), confirming the wildcard hypothesis -- but V-04 loses on C-02 (no table ordering column) and C-09 (no risk register), dropping it below V-03.

**C-05 is the R1 discriminating criterion:** Every variation except V-04 and V-05 scores PARTIAL on C-05 (7.2/12). The 4.8-point gap explains V-03 vs. V-05 almost entirely. The fix is always the same: add a second-pass validation role with a "confirmed / corrected" column.

**Open question for R2:** Does the two-role structure in V-04 produce richer C-10 remediation specificity than V-05's pre-printed remediation table? V-04 gives the PA expert full autonomy to generate remediations; V-05 constrains output to table columns. Autonomy vs. structure for remediation quality -- test in R2 by comparing actual remediation specificity in scored outputs.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["two-barrier essential enforcement: gate catches missing constructs, validation role catches imprecise ones -- neither alone sufficient for domain-grounding criteria", "pre-printed tables within gated phases: table columns prevent prose shortcuts, gates prevent section skipping -- combining both locks criteria where both failure modes are plausible", "inertia framing as cross-phase cascade catalyst: embedding naive-assumption language in the bottleneck statement seeds cascade reasoning before the cascade section fires"]}
```
