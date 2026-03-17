## Round 1 Scorecard — prove-analysis

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (10) | Score | Golden? |
|------|-----------|----------------|------------------|-------------------|-------|---------|
| 1 | V-02 Per-source 5-column table | 60/60 | 30/30 | 7/10 | **97** | Candidate |
| 1 | V-05 Table + null column | 60/60 | 30/30 | 7/10 | **97** | Candidate |
| 3 | V-04 Gated phase lifecycle | 60/60 | 25/30 | 10/10 | **95** | No |
| 4 | V-01 Inventory-first | 60/60 | 25/30 | 7/10 | **92** | No |
| 5 | V-03 Imperative register | 60/60 | 20/30 | 7/10 | **87** | No |

---

### Key Findings

**All five pass all essential criteria.** The per-source template pattern (named field per obligation) is sufficient to guarantee C-01 through C-05 in every structural form tested. There is no essential-criteria differentiation in Round 1.

**Differentiation is entirely in recommended/aspirational:**

| Gap | Cause | Variation(s) affected |
|-----|-------|-----------------------|
| C-06 (multiple sources) | No inventory phase + no explicit minimum | V-03 |
| C-08 (quantified claims) | Strength field allows tier-only answers; no dedicated [Required] numeric section | V-01, V-03, V-04 |
| C-09 (causal mechanism) | No variation explicitly prompts "No causal mechanism is apparent because..." on correlation labels | All except V-04 |

**The single discriminator between V-02 (97) and V-04 (95):** V-04 wins C-09 via Phase 5 mechanism forcing but loses 5 points on C-08 — no dedicated QUANTIFIED CLAIMS section. The hybrid design that adds a [Required] numeric section to V-04's structure would score 100.

**V-05 vs V-02 tie:** V-05 is the richer structural candidate — "Null met" rows structurally are counter-patterns, doubling the C-07 guarantee. V-02 is the simpler baseline. Round 2 should test which null-framing overhead cost is worth the gain.

---

### Excellence Signals

1. **Pre-printed [Required] sections close recommended gaps** — the structural mechanism that separates 97 from 92/87
2. **Table columns eliminate criteria bleeding** — named columns prevent two criteria satisfied in one sentence
3. **Null hypothesis column makes disconfirmation unavoidable** (V-05) — "Null met" rows cannot appear without acknowledging disconfirmation
4. **Fixed three-option C-04 vocabulary** — "Correlation only / Association / Causal (basis:...)" eliminates hedged non-answers
5. **Explicit minimum row count** — "Minimum two rows required" is a structural floor that instruction-based encouragement cannot match

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["pre-printed [Required] sections for counter-patterns and quantified claims convert optional-feeling supplementary content into mandatory completion events -- the structural mechanism that closes C-07 and C-08 gaps", "null hypothesis column makes disconfirmation structurally unavoidable: Null met rows are counter-patterns by definition and cannot be reported without acknowledging disconfirmation", "table columns eliminate criteria bleeding by forcing each criterion into a named slot -- visible blank cell is a stronger failure signal than any instruction-based prompt"]}
```
Causal" is selected, but none explicitly require a mechanism sentence when labeling a finding as "Correlation only." The C-09 pass condition requires: "A plausible cause is...", "This could be explained by...", or "No causal mechanism is apparent because..." Only V-04 creates conditions where this naturally fires via Phase 5's "State why causation cannot be inferred from this source" instruction -- which produces "No causal mechanism is apparent because..." phrasing when the model labels correlation.

- **C-09 V-04 PASS (5/5)**: Phase 5 is dedicated solely to causal labeling across all sources. For correlation claims: "State why causation cannot be inferred from this source" -- this naturally produces mechanism-ruling-out language. For causal claims: "State the basis: logical necessity, temporal precedence, experimental isolation" -- these are mechanism-level justifications. The combination makes mechanism-level content the default output of Phase 5 regardless of label chosen.

- **C-10 all PASS**: Every variation includes an explicit Scope field in Synthesis/Verdict with boundary-condition language ("population, time window, platform, or configuration").

---

### The V-02 / V-05 Tie at 97

Both earn 60/60 essential + 30/30 recommended + 7/10 aspirational.

| Structural dimension | V-02 | V-05 |
|---------------------|------|------|
| C-04 guarantee | Fixed `Correlation or causal?` column | Fixed `Correlation or causal?` column |
| C-07 mechanism | Pre-printed COUNTER-PATTERNS section [Required] | "Null met" rows ARE counter-patterns by definition + COUNTER-PATTERN SUMMARY [Required] |
| C-08 mechanism | Pre-printed QUANTIFIED SUMMARY [Required] | Pre-printed QUANTIFIED CLAIMS [Required] |
| C-09 reach | Causal basis in column but no mechanism prompt | Same |
| Null/falsification | Not present | Null expectation pre-stated before any row; per-row "Null met / Null not met / Ambiguous" |
| Counter-pattern depth | Supplementary section detached from table | Counter-patterns structurally embedded in table rows (Null met = disconfirming evidence) |
| Template overhead | 5 columns | 6 columns + null expectation setup |

**V-05 is the richer candidate** despite the tie score. The null-column framing makes disconfirmation a first-class table event rather than a supplementary obligation. "Null met" rows cannot be left blank, cannot be empty, and explicitly signal disconfirmation -- C-07 is guaranteed twice (table structure + required summary section). This is the structural analogue of the feasibility skill's "Do-nothing cost" column.

**V-02 is the simpler golden baseline**: lower template overhead, same score, same essential and recommended guarantees. Preferable if null framing proves cognitively expensive (model spends output tokens on null setup before any data is examined).

**Neither wins C-09**: the causal mechanism gap persists in both. V-04's phase-gated approach is the only current path to reliable C-09 coverage, at the cost of C-08 (5/10).

---

### Why V-04 Doesn't Crack the Top

V-04 achieves the only C-09 PASS across all five variations -- and is the only structure that produces mechanism-level reasoning for every source. But it pays 5 points on C-08: the phase structure has no dedicated QUANTIFIED CLAIMS section, and Phase 6's "number, rate, count, or logical argument" allows logical-argument-only answers across all sources.

A hybrid of V-04's Phase 5 mechanism forcing + V-02's QUANTIFIED CLAIMS section would likely score 100. That is the Round 2 design target.

---

### Excellence Signals (from V-02 and V-05)

1. **Pre-printed [Required] sections for recommended criteria** -- attaching [Required] to COUNTER-PATTERNS and QUANTIFIED CLAIMS converts them from optional-feeling supplementary content into mandatory completion events. This pattern is the structural mechanism that closed the C-07 and C-08 gaps.

2. **Table columns eliminate criteria bleeding** -- when each criterion occupies a named column, the model cannot satisfy two criteria in one sentence without leaving the other column blank. The visible blank-cell failure mode is stronger than any instruction-based prompt.

3. **Null hypothesis column makes disconfirmation structurally unavoidable** (V-05) -- "Null met" rows are counter-patterns by definition. The model cannot report a "Null met" row without acknowledging disconfirmation. C-07 becomes impossible to miss without also violating the table format.

4. **Fixed three-option vocabulary for C-04** -- pre-printing "Correlation only / Association / Causal (basis: ...)" as the only acceptable cell values eliminates hedged non-answers. The model must pick one; it cannot write "relationship" or leave the type implicit.

5. **Explicit minimum row count** -- "Minimum two rows required" as a pre-printed constraint prevents single-source collapse. Structural floor > instruction-based encouragement.

---

### Open Research Questions Resolved by Round 1

1. **Does V-03 imperative register produce direct outputs or satisfy criteria by implication?** -- PARTIAL: imperative phrasing succeeds on all essentials but without structural floors for C-06 (no inventory phase) and C-08 (no numeric section), register alone is insufficient. Register is a necessary but not sufficient condition for recommended criteria.

2. **Does V-05 null-column cause over-reporting of "Null met" rows?** -- Cannot be determined from structural analysis alone. Actual execution required. Key open question for R2.

3. **Does V-04 phase separation produce richer per-phase depth or cross-phase repetition?** -- Cannot be determined structurally. Likely produces repetition in practice (Phase 3 pattern described again in Phase 4 connection, again in Phase 5 label). The 5-point C-08 gap suggests phase overhead is a real cost.

---

### Round 2 Design Target

A hybrid variation combining:
- V-04's Phase 5 dedicated causal labeling (mechanism forcing for C-09)
- V-02/V-05's pre-printed [Required] QUANTIFIED CLAIMS section (numeric floor for C-08)
- V-05's null hypothesis pre-statement (falsification discipline before analysis begins)
- V-02's compact table structure (avoid phase-repetition overhead)

Candidate: table-first structure with a pre-stated null expectation, fixed 6 columns (V-05), and a QUANTIFIED CLAIMS + MECHANISM section at verdict that explicitly requires: (a) at least one numeric value, and (b) at least one mechanism sentence per pattern.

Predicted R2 ceiling: 100/100.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["pre-printed [Required] sections for counter-patterns and quantified claims convert optional-feeling supplementary content into mandatory completion events -- the structural mechanism that closes C-07 and C-08 gaps", "null hypothesis column makes disconfirmation structurally unavoidable: Null met rows are counter-patterns by definition and cannot be reported without acknowledging disconfirmation", "table columns eliminate criteria bleeding by forcing each criterion into a named slot -- visible blank cell is a stronger failure signal than any instruction-based prompt"]}
```
