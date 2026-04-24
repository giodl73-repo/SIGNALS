## discover-literature — Round 3 Scorecard

### Scores

| Rank | Variation | Raw | Golden | C-09 | C-15 | C-16 |
|------|-----------|-----|--------|------|------|------|
| 1 | **V-05** Full Synthesis | **130** | YES | PASS | PASS | PASS (full) |
| 2 | **V-03** Depth Mode Threshold | 125 | YES | **PASS** | PARTIAL | PASS (min+) |
| 3 | **V-04** Preamble + Tokens | 125 | YES | FAIL | **PASS** | PASS (full) |
| 4 | **V-01** Hardened Preamble | 125 | YES | FAIL | **PASS** | PASS (min) |
| 5 | **V-02** Full Token Expansion | 120 | YES | FAIL | PARTIAL | PASS (full) |

**V-05 = 130/130 — ceiling of the v3 rubric.** All five pass the golden bar.

### Key finding: V-02 scored no higher than the baseline

C-16 was already PASS (min) = 5 pts for the R2 baseline (inertia tokens existed). V-02 upgrades C-16 quality to full token coverage — a real improvement — but scoring is binary; the minimum bar was already met. No new criterion closed = no score gain.

### Sub-ranking within 125 group

V-03 ranks above V-04 and V-01 because C-09 was the **explicitly stated R2 remaining gap** ("the open target for V-06 candidate"). Closing it validates the threshold mechanism hypothesis from R2. V-04 ranks above V-01 because OBLIGATION B directly specifies the TIER EMPTY: token format — contract and token spec are one instruction.

### New patterns (V-05 excellence signals)

1. **Contract-to-token binding** — OBLIGATION B specifies the exact `TIER EMPTY:` format inside the contract text. Compliance with the contract produces the observable token. The gap between "declared obligation" and "verifiable output" disappears.

2. **Multi-criterion token reuse** — `THRESHOLD NOT MET:` satisfies C-09 (threshold failure observable) and extends C-16 (adds a third named gate token) simultaneously. One design decision, two criteria covered.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Contract-to-token binding: when the enforcement contract specifies the exact output token format (not just the obligation), contract compliance produces the observable token — the contract and the token spec are the same instruction, removing the gap between declared obligation and verifiable output", "Multi-criterion token reuse: a threshold-gate token (THRESHOLD NOT MET:) satisfies both the coverage criterion (C-09) and the checkability criterion (C-16) — single mechanism with dual criterion coverage"]}
```
r-source 7-Q block + OBLIGATION A/B contract explicitly names unacceptable answers |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A lists unacceptable values (blank, "n/a", "Author et al.", "TBD") + per-field embedded recovery questions |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B specifies "NONE FOUND -- [reason] -- [what additional search]" format for empty tiers |
| C-14 | Inertia guard on PROCEED | PASS | Inertia gate block with INERTIA SCENARIO: / INERTIA RISK: / RECOMMENDATION: template labels |
| C-15 | Dual-domain obligation preamble | **PASS** | Formal ENFORCEMENT CONTRACT with "OBLIGATION A -- Anti-Placeholder Recovery" and "OBLIGATION B -- Empty-Tier Acknowledgment"; both labeled "non-optional", "cannot be waived by phase, by brevity, or by the difficulty of the topic" |
| C-16 | Template-label checkability | PASS (min) | INERTIA SCENARIO: / INERTIA RISK: / RECOMMENDATION: template labels in Phase 4; Phase 3 tiers use prose two-question gate without TIER ENTRY:/TIER EMPTY: tokens |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 6/8 = 30
**Raw score: 120 + 5 (C-15) = 125** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-02 -- Full Template-Label Expansion

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table; RECOVERY NOTE: token for any secondary search cell |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY: / TIER EMPTY: tokens on all four tiers -- structural gate compliance is grep-verifiable |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate + recommendation keyword |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies path + 6 required fields |
| C-06 | Contrary evidence mapped to claims | PASS | Per-source Q "Which Claim # does this bear on?" + TIER ENTRY: CONTRARY includes "Claim # [n]" in token format + Phase 5 Q2 |
| C-07 | WebSearch evidence visible | PASS | Per-field "if unknown" recovery enforcement |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate explicit |
| C-09 | Depth mode source threshold met | FAIL | No depth mode, no source threshold check |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL token includes "[year confirmation: predates current work]" field |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + prose preamble forbids "Blank", "N/A", "see above" |
| C-12 | Anti-placeholder recovery executed | PASS | Per-source embedded recovery Q + RECOVERY NOTE: token after any secondary search; token makes recovery step observable |
| C-13 | Empty-tier acknowledgment present | PASS | TIER EMPTY: token required for any empty tier across all four tiers |
| C-14 | Inertia guard on PROCEED | PASS | Inertia gate with INERTIA SCENARIO: / INERTIA RISK: template labels (inherited) |
| C-15 | Dual-domain obligation preamble | PARTIAL | Prose preamble: "Questions that include 'if unknown' require you to perform the follow-up action... Questions that include 'if none found' require an explanation -- they cannot be answered with silence." Covers both domains and frames both as non-optional. However not a named, labeled contract (no OBLIGATION A / OBLIGATION B structure). PARTIAL per rubric: covers both obligations in substance but not in formal contract form. |
| C-16 | Template-label checkability | PASS (full) | TIER ENTRY: / TIER EMPTY: on all four tiers + RECOVERY NOTE: for Phase 2 + INERTIA SCENARIO: / INERTIA RISK: for Phase 4. Full structural gate token coverage; compliance grep-verifiable at every gate. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 6/8 = 30
**Raw score: 120** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Note**: V-02 does not improve score over V-05 R2 baseline. C-16 was already PASS (min) at 5 pts for the baseline; PASS (full) earns the same 5 pts. C-15 remains PARTIAL = 0. V-02's quality improvement to C-16 is real but scoring is binary -- the minimum bar was already met.

---

### V-03 -- Depth Mode Source Threshold

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table with per-source Q block |
| C-03 | Four-tier literature map built | PASS | Two-question prose tier gate; NONE FOUND required; TIER EMPTY not a named token but OBLIGATION-style rule enforces acknowledgment |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies path + 7 fields (adds mode:) |
| C-06 | Contrary evidence mapped to claims | PASS | Per-source Q "Which Claim # does this bear on?" + CONTRARY tier Q requires Claim # + Phase 5 Q2 |
| C-07 | WebSearch evidence visible | PASS | Per-field recovery queries + up to 6 search angles when threshold not met |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | **PASS** | "Depth mode: {{mode | default: standard}}" declared at top; thresholds 5/15/25 explicit; Phase 2 instructs to continue until threshold met or all angles exhausted; "THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]" token if threshold unreachable; mode: added to frontmatter; sources_found in frontmatter -- C-09 pass condition: sources_found >= threshold for active mode. |
| C-10 | Methodological precedent chain | PASS | Per-source year Q + METHODOLOGICAL tier Q requires year confirmation |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + prose preamble enforces no-blank answers |
| C-12 | Anti-placeholder recovery executed | PASS | Per-source embedded recovery Q with exact follow-up query format |
| C-13 | Empty-tier acknowledgment present | PASS | Prose two-question gate: "If none found -- why not, and what additional search would address this gap?" is required Q, not optional rule |
| C-14 | Inertia guard on PROCEED | PASS | Inertia gate with INERTIA SCENARIO: / INERTIA RISK: tokens (inherited) |
| C-15 | Dual-domain obligation preamble | PARTIAL | Same prose preamble as V-05 R2: "Questions that include 'if unknown'... Questions that include 'if none found'..." -- substance covers both but no named OBLIGATION A / OBLIGATION B contract |
| C-16 | Template-label checkability | PASS (min+) | INERTIA SCENARIO: / INERTIA RISK: inherited; THRESHOLD NOT MET: token adds a third named gate token in Phase 2; Phase 3 tiers still prose. PASS at minimum bar; THRESHOLD NOT MET: is a bonus token that extends coverage beyond the inertia gate. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 6/8 = 30
**Raw score: 120 + 5 (C-09) = 125** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-04 -- Hardened Preamble + Full Token Coverage

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table + RECOVERY NOTE: for secondary searches |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY: / TIER EMPTY: tokens on all four tiers (OBLIGATION B specifies exact TIER EMPTY: format) |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies path + 6 fields (no mode:) |
| C-06 | Contrary evidence mapped to claims | PASS | TIER ENTRY: CONTRARY format includes "Claim # [n]" in the token spec; Phase 5 Q2 response strategy |
| C-07 | WebSearch evidence visible | PASS | Per-field "if unknown after WebSearch" enforcement |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | FAIL | No depth mode, no source count threshold, no mode: in frontmatter |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL includes "[year confirmation: predates current work]" |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + ENFORCEMENT CONTRACT declares both obligations non-optional |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A lists unacceptable values explicitly + per-field embedded recovery + RECOVERY NOTE: token |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B specifies "TIER EMPTY: [tier name] -- [reason] -- [what search]" as exact required format |
| C-14 | Inertia guard on PROCEED | PASS | Inertia gate with INERTIA SCENARIO: / INERTIA RISK: tokens (inherited) |
| C-15 | Dual-domain obligation preamble | **PASS** | Formal ENFORCEMENT CONTRACT: "OBLIGATION A -- Anti-Placeholder Recovery" and "OBLIGATION B -- Empty-Tier Acknowledgment"; both labeled non-optional; OBLIGATION B even specifies the TIER EMPTY: token format directly, binding the contract to an observable output token. |
| C-16 | Template-label checkability | PASS (full) | TIER ENTRY: / TIER EMPTY: on all four tiers + RECOVERY NOTE: in Phase 2 + INERTIA SCENARIO: / INERTIA RISK: in Phase 4. Full structural gate coverage. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 6/8 = 30
**Raw score: 120 + 5 (C-15) = 125** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-05 -- Full Synthesis (C-15 + C-16 + C-09)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table + RECOVERY NOTE: for secondary searches |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY: / TIER EMPTY: tokens on all four tiers (OBLIGATION B specifies exact TIER EMPTY: format in the contract) |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate + recommendation keyword |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies path + 7 fields (adds mode:) |
| C-06 | Contrary evidence mapped to claims | PASS | TIER ENTRY: CONTRARY includes "Claim # [n]"; per-source Q "Which Claim # does this bear on?"; Phase 5 Q2 response strategy |
| C-07 | WebSearch evidence visible | PASS | Per-field recovery enforcement; up to 6 search angles until threshold met |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | **PASS** | Depth mode declared at top with thresholds 5/15/25; Phase 2 target stated; 2 extra search angles if threshold not met; THRESHOLD NOT MET: token if unreachable; mode: added to frontmatter alongside sources_found -- C-09 pass condition satisfied. |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL + per-source year Q + year confirmation in token spec |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + ENFORCEMENT CONTRACT names both obligations; preamble closes "if unknown" and "if none found" escape hatches simultaneously |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A with explicit unacceptable list + per-field embedded recovery + RECOVERY NOTE: token |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B specifies TIER EMPTY: as exact required output token for any empty tier |
| C-14 | Inertia guard on PROCEED | PASS | Inertia gate with INERTIA SCENARIO: / INERTIA RISK: / RECOMMENDATION: / Reason: template labels |
| C-15 | Dual-domain obligation preamble | **PASS** | Formal ENFORCEMENT CONTRACT with labeled OBLIGATION A and OBLIGATION B; both named non-optional; preamble reinforced in closing line: "Questions that include 'if unknown' require you to perform the follow-up action... Questions that include 'if none found' require a TIER EMPTY label -- they cannot be answered with silence." |
| C-16 | Template-label checkability | **PASS (full)** | TIER ENTRY: / TIER EMPTY: on all four tiers + RECOVERY NOTE: in Phase 2 + THRESHOLD NOT MET: in Phase 2 + INERTIA SCENARIO: / INERTIA RISK: in Phase 4. Four distinct named tokens covering every structural gate. Maximum token coverage. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 8/8 = 40
**Raw score: 130** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### Ranking

| Rank | Variation | Raw | Composite | Golden | C-09 | C-15 | C-16 | Differentiator |
|------|-----------|-----|-----------|--------|------|------|------|----------------|
| 1 | **V-05** Full Synthesis | **130** | 100 | YES | PASS | PASS | PASS (full) | Only variation closing all three R3 gaps; theoretical ceiling of v3 rubric |
| 2 | **V-03** Depth Mode Threshold | 125 | 100 | YES | **PASS** | PARTIAL | PASS (min+) | Closes C-09 -- the R2 stated remaining gap; THRESHOLD NOT MET: token extends C-16 without extra work |
| 3 | **V-04** Preamble + Tokens | 125 | 100 | YES | FAIL | **PASS** | PASS (full) | Closes C-15; OBLIGATION B contract directly specifies TIER EMPTY: token -- contract and token are the same mechanism |
| 4 | **V-01** Hardened Preamble | 125 | 100 | YES | FAIL | **PASS** | PASS (min) | Closes C-15 with formal contract; Phase 3 uses prose tier gates without TIER ENTRY:/TIER EMPTY: tokens (C-16 min only) |
| 5 | **V-02** Full Token Expansion | 120 | 100 | YES | FAIL | PARTIAL | PASS (full) | C-16 upgrades from min to full -- quality gain with no score change; C-15 remains PARTIAL; no new criteria closed |

Sub-ranking within 125 group (V-03 vs V-04 vs V-01): V-03 ranks above V-04/V-01 because it closes C-09 -- the criterion explicitly called out in the R2 scorecard as "the open target" with no variation having attempted it. V-04 ranks above V-01 because OBLIGATION B directly specifies the TIER EMPTY: token (single mechanism closes C-15 and extends C-16 quality simultaneously); V-01 closes C-15 but leaves Phase 3 in prose only.

---

### What changed from R2 to R3

| Criterion | R2 winner (V-05 R2) | R3 winner (V-05) | Change |
|-----------|--------------------|--------------------|--------|
| C-09 | FAIL | PASS | Depth mode threshold + THRESHOLD NOT MET: token |
| C-15 | PARTIAL (prose) | PASS | Formal OBLIGATION A/OBLIGATION B labeled contract |
| C-16 | PASS (min) | PASS (full) | TIER ENTRY:/TIER EMPTY: + RECOVERY NOTE: + THRESHOLD NOT MET: |

Score ceiling: 115 (v2) -> 120 (v3 with baseline) -> 130 (v3 fully satisfied).

---

### Excellence Signals

**From V-05 -- the top scorer:**

1. **Contract-to-token binding**: V-05's OBLIGATION B directly specifies the output token format inside the contract text ("use this exact format: 'TIER EMPTY: [tier name]...'"). The enforcement contract and the token specification are the same instruction -- compliance with the contract produces the observable token. This removes the gap between "declared obligation" and "verifiable output" that exists when they are written separately. New pattern not present in any R2 variation.

2. **Multi-criterion token reuse**: The THRESHOLD NOT MET: token satisfies C-09 (makes threshold failure observable in the output) and simultaneously extends C-16 (adds a third named gate token beyond inertia and tier tokens). One design decision contributes to two rubric criteria. Pattern: threshold-gate tokens cost nothing additional when C-16 is already being addressed.

---

### C-09 Validation

V-03 and V-05 both close C-09 with the depth mode mechanism. This confirms the R2 hypothesis: "A V-06 candidate should add a Phase 2 check: if fewer than [threshold for active depth mode], continue searching before advancing to Phase 3." The mechanism works. V-03 validates it as a single-axis change (no other variables changed vs V-05 R2).

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Contract-to-token binding: when the enforcement contract specifies the exact output token format (not just the obligation), contract compliance produces the observable token — the contract and the token spec are the same instruction, removing the gap between declared obligation and verifiable output", "Multi-criterion token reuse: a threshold-gate token (THRESHOLD NOT MET:) satisfies both the coverage criterion (C-09) and the checkability criterion (C-16) — single mechanism with dual criterion coverage"]}
```
