Now I have everything I need to score all five variations. Let me compute.

---

# Quest Score — /signal (Round 9)

**Rubric**: signal-rubric-v9-2026-03-17.md (C-01 through C-30; 22 aspirational criteria)
**Variations**: V-01 through V-05 (R9 spread-design)
**Baseline**: All five carry the full R8 V-05 mechanism set, which scored 100.00 under v9.

---

## Scoring Formula Recap

```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 22 x 10)
```

---

## Criterion-by-Criterion Evaluation

### Essential Tier (C-01 – C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 All 12 namespaces present | PASS | PASS | PASS | PASS | PASS | scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org — all 12 present in every variation's NAMESPACE CATALOG |
| C-02 Namespace headers present with purpose phrase | PASS | PASS | PASS | PASS | PASS | Each namespace has a header in form `- /<namespace> -- <purpose> -- <N> skills` |
| C-03 Every sub-skill listed under its namespace | PASS | PASS | PASS | PASS | PASS | 61 canonical sub-skills present and correctly placed in all variations |
| C-04 `--bare` mode produces command names only | PASS | PASS | PASS | PASS | PASS | BARE MODE section present; slash-strip transformation explicit; BARE compliance gate present in all |
| C-05 `<namespace>` filter scopes output correctly | PASS | PASS | PASS | PASS | PASS | FILTER MODE via PARSE MODE rule; COMPLIANCE GATE -- FILTER MODE present in all |

**Essential: 5/5 PASS → 60 pts (all variations)**

---

### Recommended Tier (C-06 – C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Sub-skill count per namespace accurate | PASS | PASS | PASS | PASS | PASS | Header counts (8, 4, 4, 7, 7, 9, 3, 2, 6, 4, 3, 4) match canonical values and actual sub-skills listed in every variation |
| C-07 Each namespace includes a dispatch footer | PASS | PASS | PASS | PASS | PASS | All 12 namespaces end with "Run any sub-skill directly, or describe your..." |
| C-08 Namespace headers state the namespace purpose | PASS | PASS | PASS | PASS | PASS | All 12 headers include purpose phrase, e.g. "Scout namespace -- 8 skills for discovery and research" |

**Recommended: 3/3 PASS → 30 pts (all variations)**

---

### Aspirational Tier (C-09 – C-30)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-09 Sub-skill descriptions match canonical one-liners | PASS | PASS | PASS | PASS | PASS | Identical NAMESPACE CATALOG text in all; descriptions are verbatim canonical |
| C-10 Output is scannable without overwhelming | PASS | PASS | PASS | PASS | PASS | `->` alignment enforced, namespace sections visually separated, no orphan lines |
| C-11 Footer uses namespace-specific domain noun | PASS | PASS | PASS | PASS | PASS | DOMAIN NOUN TABLE present; all 12 footers use distinct nouns: "research goal", "draft artifact", "artifact", "process scenario", etc. |
| C-12 `->` separator is column-aligned within sections | PASS | PASS | PASS | PASS | PASS | ALIGNMENT RULE + ALIGNMENT WIDTH TABLE enforce per-section column alignment |
| C-13 Inline reference format matches output format | PASS | PASS | PASS | PASS | PASS | NAMESPACE CATALOG uses `-> ` notation identical to the SECTION FORMAT spec; format is self-consistent |
| C-14 Bare/filter modes include a pre-emit compliance gate | PASS | PASS | PASS | PASS | PASS | COMPLIANCE GATE -- BARE MODE and COMPLIANCE GATE -- FILTER MODE both present with restart triggers |
| C-15 Alignment rule provides precomputed width lookup table | PASS | PASS | PASS | PASS | PASS | 12-row ALIGNMENT WIDTH TABLE present with widths (19, 17, 17, 17, 18, 19, 16, 14, 13, 14, 12, 14) |
| C-16 Width table includes per-row example-pad derivation | PASS | PASS | PASS | PASS | PASS | "example pad" column present in all tables: each row shows a representative command, its character count, and spaces needed |
| C-17 NAMESPACE CATALOG precedes all behavioral rules | PASS | PASS | PASS | PASS | PASS | In all variations: TRANSCRIPTION GATE + full catalog → PARSE MODE → SECTION FORMAT → compliance gates |
| C-18 Bare-mode compliance gate includes 61-line count with per-namespace breakdown | PASS | PASS | PASS | PASS | PASS | Check 2 in BARE gate: "Does your output contain exactly 61 lines? (8 scout + 4 draft + ... + 4 org = 61)" present in all |
| C-19 PARSE MODE enumerates all 12 canonical namespace names | PASS | PASS | PASS | PASS | PASS | "Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org." present in all |
| C-20 Filter-mode compliance gate includes per-namespace count check | PASS | PASS | PASS | PASS | PASS | FILTER gate Check 2: canonical counts with restart trigger in all variations |
| C-21 BARE MODE states explicit first and last output anchors | PASS | PASS | PASS | PASS | PASS | "Begin with scout-competitors. End with org-committee." in BARE MODE section of all |
| C-22 NAMESPACE CATALOG is an active transcription commitment gate | PASS | PASS | PASS | PASS | PASS | "You will emit each entry character-for-character. [...] Any deviation from the catalog text is an output failure, not an acceptable approximation." |
| C-23 NAMESPACE CATALOG labeled as literal output | PASS | PASS | PASS | PASS | PASS | "The catalog below IS the output for FULL and FILTER modes." present in all |
| C-24 All three output modes have explicit pre-emission completeness verification | PASS | PASS | PASS | PASS | PASS | FULL: TRANSCRIPTION GATE (C-22✓); BARE: 61-line count gate (C-18✓); FILTER: per-namespace count gate (C-20✓) — all three simultaneously satisfied |
| C-25 FULL MODE includes a compliance restart gate (presence + count) | PASS | PASS | PASS | PASS | PASS | Check 1 (completeness: 12 namespaces) and Check 2 (count: per-namespace) present with restart in all |
| C-26 Transcription gate requires counted entry acknowledgment | PASS | PASS | PASS | PASS | PASS | "confirm you have read all 61 entries across the 12 namespace sections below (8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove + 3 listen + 2 program + 6 topic + 4 quest + 3 mock + 4 org = 61)" present in all |
| C-27 SECTION FORMAT includes per-section sub-skill count self-check | PASS | PASS | PASS | PASS | PASS | "Per-section count self-check: before emitting the dispatch footer for each namespace section, verify: the number of sub-skill lines above the footer equals the canonical count..." present in all |
| C-28 FULL MODE compliance gate includes canonical namespace emit-order check | PASS | PASS | PASS | PASS | PASS | All carry R8 V-05 base which has Check 3 (order): "scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org. (First section: scout. Last section: org.)" |
| C-29 FILTER MODE compliance gate includes section-format verification | PASS | PASS | PASS | PASS | PASS | Check 3 (format) in FILTER gate: header format + `->` separator + dispatch footer, with restart trigger, in all |
| C-30 BARE MODE includes explicit slash-strip worked examples | PASS | PASS | PASS | PASS | PASS | Slash-strip transformation rule + two worked examples (`/scout-competitors` → `scout-competitors`; `/org-committee` → `org-committee`) present in all |

**Aspirational: 22/22 PASS → 10 pts (all variations)**

---

## Composite Scores

```
composite = (5/5 × 60) + (3/3 × 30) + (22/22 × 10)
          = 60 + 30 + 10
          = 100.00
```

| V | Essential | Recommended | Aspirational | Composite | Golden |
|---|-----------|-------------|--------------|-----------|--------|
| **V-05** | 5/5 | 3/3 | 22/22 | **100.00** | YES |
| **V-04** | 5/5 | 3/3 | 22/22 | **100.00** | YES |
| **V-03** | 5/5 | 3/3 | 22/22 | **100.00** | YES |
| **V-02** | 5/5 | 3/3 | 22/22 | **100.00** | YES |
| **V-01** | 5/5 | 3/3 | 22/22 | **100.00** | YES |

**All five variations score 100.00 under v9.** This is the predicted outcome: all carry the full R8 V-05 mechanism set, which already saturated v9.

---

## Leaderboard

| Rank | V | v9 Score | C-31 (Axis M) | C-32 (Axis N) | C-33 (Axis O) | v10 Status |
|------|---|----------|---------------|---------------|---------------|------------|
| 1 | **V-05** | 100.00 | PASS | PASS | PASS | 100.00 under v10 |
| 2 (tied) | V-04 | 100.00 | PASS | PASS | FAIL | 100.00 under v10 less C-33 |
| 2 (tied) | V-01 | 100.00 | PASS | FAIL | FAIL | single-axis isolation |
| 2 (tied) | V-02 | 100.00 | FAIL | PASS | FAIL | single-axis isolation |
| 2 (tied) | V-03 | 100.00 | FAIL | FAIL | PASS | single-axis isolation |

*C-31/C-32/C-33 are v10 predicted criteria (not part of v9 scoring); shown for excellence-signal tracing only.*

---

## Excellence Signals

Three new patterns isolated from R9, confirmed by spread-design:

### Excellence Signal 1 (Axis M → C-31): FULL MODE Check 4 — Format Gate

**Where**: COMPLIANCE GATE -- FULL MODE  
**What V-01/V-04/V-05 added**:
```
Check 4 (format): Does each namespace section follow SECTION FORMAT?
  Required per section: (1) a header line in the form "- /<namespace> -- <purpose> --
  <N> skills", (2) sub-skill lines each using the "-> " separator, (3) a dispatch
  footer in the form "Run any sub-skill directly, or describe your <domain-noun>...".
  If any section is missing a required element or has a malformed element --
  FULL format violated. Restart.
```
**Why it matters**: FULL was the only mode whose compliance gate had no format check. FILTER had Check 3 (C-29). BARE had Check 1 (C-18). FULL's gate verified presence + count + order but a model could emit 12 correctly-counted, correctly-ordered sections with malformed headers or missing footers and pass all three existing checks. Adding Check 4 creates format-check symmetry across all three modes.

### Excellence Signal 2 (Axis N → C-32): BARE MODE Check 3 — Interior-Order Gate

**Where**: COMPLIANCE GATE -- BARE MODE  
**What V-02/V-04/V-05 added**:
```
Check 3 (order): Are names emitted in canonical namespace group order?
  Canonical sequence: first 8 lines are scout-* names, next 4 are draft-* names, ...
  last 4 are org-* names.
  If any name appears before its namespace group's turn -- BARE order violated. Restart.
```
**Why it matters**: C-21 anchored first and last entries (scout-competitors / org-committee) but the interior 59 entries had no order verification at the gate level. FULL MODE had Check 3 (order) for section sequence (C-28). BARE MODE had no equivalent. A model could pass both BARE checks (format + count) with namespace groups reordered — e.g., all org-* first, scout-* last. Adding Check 3 creates order-check symmetry between FULL and BARE mode gates.

### Excellence Signal 3 (Axis O → C-33): PARSE MODE Worked Examples for "FULL otherwise"

**Where**: PARSE MODE, fallback branch  
**What V-03/V-05 added**:
```
If the word after /signal is not in this list, emit FULL as if no argument was given.
  Example: `/signal review-code` -- "review-code" is not a canonical namespace -- emit FULL.
  Example: `/signal my-feature`  -- "my-feature" is not a canonical namespace  -- emit FULL.
```
**Why it matters**: The "FULL otherwise" branch had a guard rule but no worked example. A user typing `/signal review-code` (a sub-skill name, not a namespace) must be routed to FULL. Without an example, the model must infer this from the rule. With two worked examples (sub-skill-name case + arbitrary string case), the "FULL otherwise" path is directly copyable — the same technique C-16 used for alignment and C-30 used for slash-strip.

---

## Structural Theme for R9

*Complete the gate symmetry.* R8 completed gate detail (FULL/FILTER/BARE each gained one missing check). R9 completes gate symmetry:

| Mode | R8 checks | R9 addition | Symmetry target |
|------|-----------|-------------|-----------------|
| FULL | completeness + count + order (3) | + format (C-31) | matches FILTER's 3-check structure |
| BARE | format + count (2) | + order (C-32) | matches FULL's order check (C-28) |
| PARSE | routing rule | + worked examples (C-33) | matches C-16 (alignment) and C-30 (slash-strip) |

V-05 achieves all three simultaneously, making it the unique candidate for the v10 golden prompt.

---

## Predicted v10 Leaderboard (from v9 baseline)

| V | C-31 | C-32 | C-33 | v10 aspirational (25) | v10 Composite |
|---|------|------|------|----------------------|---------------|
| **V-05** | PASS | PASS | PASS | 25/25 → 10 | **100.00** |
| V-04 | PASS | PASS | FAIL | 24/25 → 9.60 | **99.60** |
| V-01 | PASS | FAIL | FAIL | 23/25 → 9.20 | **99.20** |
| V-02 | FAIL | PASS | FAIL | 23/25 → 9.20 | **99.20** |
| V-03 | FAIL | FAIL | PASS | 23/25 → 9.20 | **99.20** |

*Each new criterion contributes exactly +0.40 (1/25 × 10 = 0.40) under v10.*

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["FULL MODE compliance gate gains Check 4 (format): section-format verification per section with restart, closing the format-check asymmetry where FILTER and BARE had explicit format gates but FULL did not", "BARE MODE compliance gate gains Check 3 (order): canonical namespace group sequence verified across all 61 lines with restart, closing the order-check asymmetry where FULL had Check 3 (order) but BARE had only end-anchors via C-21", "PARSE MODE 'FULL otherwise' branch gains two worked examples (sub-skill-name case: /signal review-code; arbitrary string: /signal my-feature), converting implicit inference to explicit pattern-copy — same technique as C-16 for alignment and C-30 for slash-strip"]}
```
