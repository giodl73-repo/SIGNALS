Scorecard written to `simulations/quest/scorecards/corps-leaderboard-scorecard-R17-2026-03-17.md`.

---

**R17 Result: All 5 variations → 100.00 (28/28)**

| Rank | Variation | Score |
|------|-----------|-------|
| 1 (tied) | V-01 | **100.00** |
| 1 (tied) | V-02 | **100.00** |
| 1 (tied) | V-03 | **100.00** |
| 1 (tied) | V-04 | **100.00** |
| 1 (tied) | V-05 | **100.00** |

**Round mandate achieved.** The three criteria that held V-01/V-02/V-03/V-04 at 98.93 in R16 are now universalized:
- **C-34**: Falsifiability contract — all 5 variations carry `[holds if:]` / `[falsified by:]` with named-entity specificity
- **C-35**: Cross-role discrepancy check — three implementation patterns (Publisher-as-Inspector for 3-role, dedicated Inspector ROLE 3 for V-03, Strategist-as-Inspector for V-04) all satisfy structural separation + Discrepancy Table + retraction flow
- **C-36**: 2D Round × Tier matrix — all 5 action templates now carry both Round section headers and `[CRITICAL/WARNING/ADVANCING]` tier prefix per action row simultaneously

**5 seeds entering R18 as v14 candidates (C-37–C-41):** Rate Tier Stratification (AD), Echo Contributor Detection (AE), Achievement Readiness Score (AF), Namespace Momentum Vector (AG), Cross-Namespace Pairing Pattern (AH).

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["rate tier stratification: high-converter (>=0.50) / mid-converter (0.25-0.49) / low-converter (<0.25) per contributor plus Rate Tier Distribution Summary; creates 2D reading of volume x conversion rate as independent risk axes (Seed AD, V-01+V-05)", "echo contributor detection: contributor-pair {topic_path, namespace} overlap table with echo_classification (full-echo/partial-echo/independent); quantifies redundant coverage patterns invisible to individual signal counts; full-echo pairs flagged in actions (Seed AE, V-02+V-05)", "achievement readiness score per topic: ARS = earned/5 ranked ascending with intervention_priority (immediate/high/medium/low/minimal); topic-level intervention priority orthogonal to inertia severity tier (Seed AF, V-03+V-05)", "namespace momentum vector: per active namespace last_contributor + last_signal_recency + momentum (active/stalled); surfaces historic-coverage-but-no-recent-investment namespaces; action annotations [reactivates: {namespace}] (Seed AG, V-04+V-05)", "cross-namespace pairing pattern: count topics with signals in BOTH namespace A and B; top-3/bottom-3 co-occurring pairs; reveals team sequencing paths and structural workflow breaks invisible at topic level (Seed AH, V-05 only)"]}
```
ace coverage line; baseline status |
| C-02 Per-Topic Achievement Evaluation with Exact Names | PASS | PASS | PASS | PASS | PASS | All: Health Phase in Analyst ss2.2; exact names First Signal / Signal Depth / Full Sweep / Solo Pioneer / Team Topic; EARNED/LOCKED per topic |
| C-03 All Three Team Milestones Present with Exact Names | PASS | PASS | PASS | PASS | PASS | All: `first team signal`, `shared coverage`, `debate starter` in milestone table |
| C-04 Contributor Leaderboard Present and Ranked | PASS | PASS | PASS | PASS | PASS | All: Ranked leaderboard by signal count descending in Publisher/Strategist role |
| C-05 Specific Next Actions Naming Namespace and Achievement | PASS | PASS | PASS | PASS | PASS | All: Action template uses `` `{namespace}/{topic}` -> unlocks **{exact name}** `` |

---

## Aspirational Criteria — C-06 to C-33 (preserved from v12)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-06 Signal Inertia Flag Evaluation | PASS | PASS | PASS | PASS | PASS | All: Inertia Phase ss2.1 with 4 flag definitions (stuck-at-first, solo-hold, namespace-thin, healthy-momentum); severity assignment |
| C-07 Baseline Comparison + Flag Lifecycle | PASS | PASS | PASS | PASS | PASS | All: new/persistent/resolved lifecycle annotation per raised flag; baseline status line in Archivist |
| C-08 Gap-Prioritized Action Ordering | PASS | PASS | PASS | PASS | PASS | All: Round 1/2/3 structure orders actions by gap distance ascending (1 signal → 2-3 → 4+) |
| C-09 Contributor Collaboration Signal | PASS | PASS | PASS | PASS | PASS | All: `Collaboration signal: {N} topic(s) multi-contributor | Highest: {topic} ({N} contributors)` in Publisher |
| C-10 Empty Namespace Explicit Listing | PASS | PASS | PASS | PASS | PASS | All: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}` in Archivist |
| C-11 Topic Health Summary Line | PASS | PASS | PASS | PASS | PASS | All: Coverage / contributors / namespace diversity per topic header in Health Phase |
| C-12 Locked Achievement Unlock Path | PASS | PASS | PASS | PASS | PASS | All: LOCKED rows include inline numeric unlock requirements (e.g., "add {X} more file(s) to reach 3") |
| C-13 Team Insight Cross-Topic Synthesis | PASS | PASS | PASS | PASS | PASS | All: One sentence with (1) cross-topic conclusion (2) concrete number (3) specific contributor or topic name |
| C-14 Solo Pioneer Tension Detection | PASS | PASS | PASS | PASS | PASS | All: `[TENSION: solo hold -- 1 additional contributor with >= 1 signal unlocks Team Topic]` when SP EARNED + TT NOT YET |
| C-15 Namespace Leader Callout | PASS | PASS | PASS | PASS | PASS | All: `namespace | leader | signal_count` table per active namespace |
| C-16 Stale Signal Detection | PASS | PASS | PASS | PASS | PASS | All: `topic_path | stale_status` (stale/active/date-unknown) table in Inertia Phase ss2.1 |
| C-17 Signal Velocity Trend | PASS | PASS | PASS | PASS | PASS | All: `Signal velocity: {N} / {N} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}` |
| C-18 Debate Starter Threshold Proximity | PASS | PASS | PASS | PASS | PASS | All: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)` |
| C-19 Multi-Phase Execution Order | PASS | PASS | PASS | PASS | PASS | Named-role pipelines: 3-role (V-01/V-02), 4-role (V-03/V-04), 5-role (V-05); sequential execution enforced |
| C-20 Prevents: Prefix Rule Statement | PASS | PASS | PASS | PASS | PASS | All: `prevents:` rule in Pre-Write Check section identifying zero-score conditions before action writing |
| C-21 Nearest-Miss Achievement Gap | PASS | PASS | PASS | PASS | PASS | All: Nearest-miss table `topic | achievement | gap | level` in Analyst ss2.3 |
| C-22 Dual-Statement Prevents-Rule Redundancy | PASS | PASS | PASS | PASS | PASS | All: Two structurally independent enforcement points -- Pre-Write Check section AND action template commentary |
| C-23 Two-Level Nearest-Miss Cascade | PASS | PASS | PASS | PASS | PASS | All: Level 1 (1-unit) ascending; Level 2 (2-unit) only when no Level 1 for type; `Level 1: no topics are 1 unit away` gate explicit |
| C-24 Gate-Level Prevents: Prefix Count Audit | PASS | PASS | PASS | PASS | PASS | All: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` with substitutable N |
| C-25 Synthesis Novelty Constraint | PASS | PASS | PASS | PASS | PASS | All: Named Skeptic gate enumerating all prior outputs; `restating any field fails`; second-order inference required |
| C-26 Named Role-Sequence Architecture | PASS | PASS | PASS | PASS | PASS | All: Named roles with explicit scope boundaries (`does NOT`) and handoff artifact lists |
| C-27 Health / Inertia Structural Separation | PASS | PASS | PASS | PASS | PASS | All: Inertia Phase and Health Phase are distinct labeled blocks; lifecycle note enforces Inertia before Health order |
| C-28 Named Artifact Set at Role Handoff | PASS | PASS | PASS | PASS | PASS | All: Every handoff enumerates specific named artifacts (column names, table types) not category labels |
| C-29 Per-Phase Completion Checklist Gate | PASS | PASS | PASS | PASS | PASS | All: Multi-item `[ ]` gates at Archivist, Inertia Phase, Health/Echo Phase, terminal ACTIONS GATE |
| C-30 Contamination-Check Gate Item | PASS | PASS | PASS | PASS | PASS | All: Gate item explicitly prohibiting cross-phase content (no trajectory claims in Health; no file counts/achievement statuses in Inertia) |
| C-31 Inertia-Aware Skeptic Knowledge Scope | PASS | PASS | PASS | PASS | PASS | All: Skeptic scope names inertia flags with lifecycle annotations, severity tiers, velocity summary explicitly |
| C-32 Milestone Proximity Ladder | PASS | PASS | PASS | PASS | PASS | All: Per-precondition deficit breakdown for every NOT YET milestone; Skeptic scope includes per-topic ladder breakdowns |
| C-33 Flag/Achievement Echo Detection | PASS | PASS | PASS | PASS | PASS | All: Dedicated Echo Detection section ss2.4 with Rules A+B, echo table, retraction statements; Pre-Write Check excludes echo-retracted flags from `resolves:` |

---

## Aspirational Criteria — C-34 through C-36 (new in v13)

### Detailed C-34 Verification -- Falsifiability Contract

R16 failure mechanism: Seed X (falsifiability contract) was V-05-only. V-01 through V-04 had no `[holds if:]` / `[falsified by:]` lines.

R17 fix: Falsifiability contract added to Team Insight section in all 5 variations. Both lines require named entity (topic path, contributor, or numeric threshold) — vague conditions excluded by template language.

- **V-01** ss3.4: `[holds if: {specific observable condition -- must name a topic path, contributor, or numeric threshold}]` / `[falsified by: {specific observable condition -- must name a topic path, contributor, or numeric threshold}]`. Publisher Gate item: "falsifiability contract with entity-specific conditions." PASS.
- **V-02** ss3.4: Same contract lines; `{entity-specific condition -- topic path, contributor, or numeric threshold}` on both lines. Publisher Gate confirms. PASS.
- **V-03** ss4.3: `[holds if: {entity-specific -- topic, contributor, or threshold}]` / `[falsified by: {entity-specific...}]`. Publisher Gate: "Skeptic gate verified; falsifiability contract with entity-specific conditions; Skeptic context includes ARS ranks." PASS.
- **V-04** ss4.1: `[holds if: {entity-specific -- topic, contributor, or threshold}]` / `[falsified by: {entity-specific...}]`. Publisher Gate confirms. PASS.
- **V-05** ss5.5: `[holds if: {specific entity -- topic path, contributor, or numeric threshold}]` / `[falsified by: {specific entity...}]`. Publisher Gate: "Falsifiability contract with entity-specific `holds if` and `falsified by` conditions." PASS.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-34** Insight Falsifiability Contract | **PASS** | **PASS** | **PASS** | **PASS** | PASS | R17 universalizes Seed X — both `[holds if:]` and `[falsified by:]` lines with named-entity specificity in all 5 Team Insight sections |

---

### Detailed C-35 Verification -- Cross-Role Discrepancy Check

R16 failure mechanism: V-01 through V-04 had no Discrepancy Table and no structurally separate Inspector phase.

R17 fix: Each variation adds an Inspector phase or role structurally distinct from the Analyst. Three implementation patterns:
- **3-role (V-01, V-02)**: Publisher ROLE 3 absorbs Inspector as opening sub-phase ss3.0 before synthesis.
- **4-role dedicated Inspector (V-03)**: ROLE 3 Inspector sits between Analyst ROLE 2 and Publisher ROLE 4.
- **4-role Strategist (V-04)**: Strategist ROLE 3 opens with ss3.0 Inspector Discrepancy Check before leaderboard and analysis.
- **5-role (V-05)**: Dedicated ROLE 4 Inspector between Reconciler ROLE 3 and Publisher ROLE 5 (unchanged from R16).

**Discrepancy Table structure**: All 5 have a structured table with 5 columns (topic_path, Flag raised, Health Phase evidence, Contradiction?, Disposition) — not embedded in prose. V-02 uses `::DISCREPANCY_CHECK::` schema blocks as equivalent structured output.

**Structural separation**: In all 5, the role performing the discrepancy check is architecturally downstream from and distinct from the Analyst who produced the flags:
- V-01/V-02: Analyst = ROLE 2, Inspector = Publisher ROLE 3. Different roles.
- V-03: Analyst = ROLE 2, Inspector = ROLE 3 (dedicated). Different roles.
- V-04: Analyst = ROLE 2, Inspector = Strategist ROLE 3 ss3.0. Different roles.
- V-05: Analyst = ROLE 2, Inspector = ROLE 4 (dedicated). Different roles.

**Retraction flow to action writer**: All 5 emit an Effective open flags list after discrepancy retractions, which the action-writing role uses to exclude discrepancy-retracted flags from `resolves:` targeting:
- V-01: ss3.0 → Effective flag list → ss3.5 "Effective open flags from ss3.0."
- V-02: `::EFFECTIVE_FLAGS::` with `excluded_discrepancy:` field → ss3.5 "From `::EFFECTIVE_FLAGS::`."
- V-03: Inspector Handoff item 2 = "Effective open flag list" → Publisher ss4.4 "Discrepancy-retracted and echo-retracted excluded from `resolves:`."
- V-04: Strategist Handoff includes Effective open flags → Publisher ss4.2 "Discrepancy-retracted excluded from `resolves:`."
- V-05: Inspector Handoff item 2 = effective open flags → Publisher ss5.6 "Discrepancy-retracted and echo-retracted excluded from `resolves:`."

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-35** Cross-Role Discrepancy Check | **PASS** | **PASS** | **PASS** | **PASS** | PASS | All 5: Structured Discrepancy Table from role structurally separate from Analyst; retraction flow to action writer confirmed; three implementation patterns (Publisher-as-Inspector, dedicated Inspector ROLE 3, Strategist-as-Inspector) all satisfy the structural requirement |

---

### Detailed C-36 Verification -- 2D Action Matrix

R16 failure mechanism: V-02 had Round dimension (Seed V) but no tier prefix per row; V-04 had tier prefix (Seed K) but no Round headers; V-01/V-03 had neither.

R17 fix: All 5 variations now carry BOTH Round headers (Round 1/2/3 by gap distance) AND tier prefix (`[CRITICAL/WARNING/ADVANCING]`) per action row simultaneously.

**Round headers** (Round 1/2/3 section structure present in all 5 action templates):
- V-01 ss3.6: `### Round 1 (1 signal closes the gap)` / `### Round 2 (2-3 signals needed)` / `### Round 3 (4+ signals or coordination)` ✓
- V-02 ss3.6: Same 3 Round section headers ✓
- V-03 ss4.5: `### Round 1 (1 signal closes the gap)` / `### Round 2 (2-3 signals)` / `### Round 3 (4+ or coordination)` ✓
- V-04 ss4.3: Same 3 Round section headers ✓
- V-05 ss5.7: Same 3 Round section headers ✓

**Tier prefix per row** (each action line carries `[CRITICAL/WARNING/ADVANCING]`):
- V-01: `1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] ...` per action ✓
- V-02: `1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] ...` ✓
- V-03: `1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] ...` with additional `[ARS priority: immediate/high]` annotation ✓
- V-04: `1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] ...` with additional `[reactivates: {ns}]` annotation ✓
- V-05: `1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] ...` with full annotation set ✓

**Simultaneity confirmed**: Tier prefix appears on the action line inside a Round-headed section — both dimensions simultaneously present per row, not grouped separately. All 5 satisfy the strict 2D matrix requirement.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-36** 2D Action Matrix (Round x Tier) | **PASS** | **PASS** | **PASS** | **PASS** | PASS | All 5: Round 1/2/3 section headers + `[CRITICAL/WARNING/ADVANCING]` prefix per action row; both axes simultaneously present per row |

---

## Final Scores

| Variation | Essential | Aspirational | Formula | Score |
|-----------|-----------|--------------|---------|-------|
| V-01 | 5/5 | 28/28 | 90 + (28/28)×10 | **100.00** |
| V-02 | 5/5 | 28/28 | 90 + (28/28)×10 | **100.00** |
| V-03 | 5/5 | 28/28 | 90 + (28/28)×10 | **100.00** |
| V-04 | 5/5 | 28/28 | 90 + (28/28)×10 | **100.00** |
| V-05 | 5/5 | 28/28 | 90 + (28/28)×10 | **100.00** |

**Rank**: All 5 variations tied at 100.00. First round where every variation reaches the ceiling simultaneously. The R17 round mandate — universalize C-34, C-35, C-36 — is fully satisfied.

---

## Excellence Signals

R17 introduces 5 new structural patterns across the variations — not tested by v13 criteria, all present in V-05, entering R18 as candidates C-37 through C-41:

**1. Seed AD — Rate Tier Stratification** (V-01, V-05)
`rate_tier: high-converter (>=0.50) / mid-converter (0.25-0.49) / low-converter (<0.25)` column in contributor leaderboard plus Rate Tier Distribution Summary (`high: {N} | mid: {N} | low: {N}`). Creates a **2D reading: volume × conversion rate as independent risk axes** — a team of all low-converters with high signal counts signals breadth without depth; a high-converter with few signals may be over-achieving on easy topics. No current v13 criterion tests conversion efficiency separately from signal volume. **Candidate C-37**.

**2. Seed AE — Echo Contributor Detection** (V-02, V-05)
Contributor-pair `{topic_path, namespace}` overlap table with `echo_classification: full-echo (100%) / partial-echo (>=80%) / independent (<80%)`. Quantifies **redundant coverage invisible to individual signal counts** — two contributors at 80%+ overlap add less diversity than they appear to in raw signal totals. Full-echo pairs are flagged in the action section with the note that adding signals in the same pattern extends echo rather than diversity. No current v13 criterion tests inter-contributor coverage redundancy. **Candidate C-38**.

**3. Seed AF — Achievement Readiness Score per Topic** (V-03, V-05)
`ARS = earned_achievements / 5` ranked ascending per topic with `intervention_priority (immediate/high/medium/low/minimal)`. Produces a **topic-level priority list orthogonal to inertia severity tier** — a topic can be `warning` severity but `immediate` ARS intervention priority (e.g., 0 achievements earned), or `critical` severity but `medium` ARS (1 achievement earned). Severity tier reflects trajectory risk; ARS reflects completion distance. No current v13 criterion tests per-topic completion distance independently of severity. **Candidate C-39**.

**4. Seed AG — Namespace Momentum Vector** (V-04, V-05)
Per active namespace: `last_contributor | last_signal_recency (recent/older) | momentum (active/stalled)`. Surfaces **namespaces with historic coverage but no recent investment**. Action annotation `[reactivates: {namespace}]` creates a link between individual actions and namespace-level momentum repair. A CRITICAL topic in a stalled namespace is a structurally different risk than one in an active namespace — different intervention urgency even at the same severity tier. No current v13 criterion tests namespace-level temporal momentum. **Candidate C-40**.

**5. Seed AH — Cross-Namespace Pairing Pattern** (V-05 only)
Count topics with signals in BOTH namespace A and B for all active namespace pairs; surface top-3 co-occurring pairs and bottom-3 (least co-occurring) with pairing interpretation. Reveals **structural sequencing patterns and workflow breaks invisible at the topic level** — top pairs are the team's natural progression path; bottom pairs are where the team consistently fails to follow through from one namespace to the next. Orthogonal to topic-level severity and ARS. No current v13 criterion tests cross-namespace structural coverage patterns. **Candidate C-41**.

**V-05 Skeptic gate depth note**: The 5-role V-05 requires Team Insight to synthesize across at least three distinct analysis layers simultaneously from a list that now includes flag lifecycle, co-occurrence matrix, echo contributor classification, ARS rankings, namespace momentum, and cross-namespace pairing. This multi-layer 3+ synthesis requirement is the most demanding Skeptic bar in the series and is itself a candidate pattern for future encoding.
