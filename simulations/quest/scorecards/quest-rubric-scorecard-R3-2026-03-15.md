# Quest Score — quest-rubric / Round 3

**Rubric version**: v3 | **Date**: 2026-03-15
**Note**: V-03 through V-05 not present in prompt — scoring V-01 and V-02 only. C-15 referenced in structure table but not defined in rubric body; omitted from scoring.
**Trace artifact**: placeholder (no ground truth artifact — scoring prompt behavior only)

---

## Scoring Formula Used

| Tier | Weight | Rule |
|------|--------|------|
| Essential (C-01–C-05) | Gate | All must be PASS; PARTIAL = gate fail, base capped at 40 |
| Recommended (C-06–C-08) | 30 pts | PASS = 10, PARTIAL = 5, FAIL = 0 |
| Aspirational (C-09–C-14) | 10 pts | PASS = 1.67, PARTIAL = 0.83, FAIL = 0 |
| Essential gate pass | +60 base | Unlocks full scoring |

---

## V-01 — Role Sequence (Failure Analyst First)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Skill identity declared | PASS | Frontmatter template has `skill: <target skill name>` — output will always name the skill |
| C-02 | Criteria are testable | PASS | Category closed-list + "must/contains/states/lists" requirement prevents ambiguous pass conditions |
| C-03 | Pass condition enforced | PASS | Prohibitions block explicitly bans "should", "ideally", "aims to", "attempts to" |
| C-04 | Scoring formula explicit | PASS | Role 3 (Score Formula Writer) is a required phase; output template has `## Scoring Formula` section |
| C-05 | Tier structure present | PASS | Three tiers named in output template with separate sections |

**Essential gate**: PASS

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Failure modes cataloged | PASS | Role 1 mandates minimum 6 failure modes before any criteria are written; F-ID format required |
| C-07 | Specificity test included | PARTIAL | Prohibition blocks generic criteria ("equally true for a completely different skill"), but no explicit specificity *criterion* appears in the output rubric itself — mechanism is a prohibition, not a scoreable criterion |
| C-08 | Version and date stamped | PASS | Frontmatter template has `date:` and `version:` fields |

**Recommended**: 2.5 / 3 → **25 pts**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Coverage of all output sections | PARTIAL | Output template defines tier sections; Role 2 links criteria to failure modes — but no explicit requirement that every *target skill* output section gets at least one criterion |
| C-10 | Scoring formula includes partial credit | PASS | Role 3 explicitly requires "whether partial credit exists and how it is defined" |
| C-11 | External enforcement gate | PASS | `## Prohibitions` section is a named, enumerated enforcement checklist (3 items) |
| C-12 | Failure-first derivation | PASS | Role 1 runs before Role 2 by strict sequencing — this is the core hypothesis; no criteria can be written until F-IDs exist |
| C-13 | Generic-vs-specific foil pair | FAIL | No before/after example appears near the specificity prohibition; the prohibition is stated but not illustrated |
| C-14 | Explicit category enumeration in field rules | PASS | `Category: one of: correctness / depth / format / coverage / behavior` is a closed enumeration in the criteria-writing instructions |

**Aspirational**: 4.5 / 6 → **7.5 pts**

### V-01 Total: 60 + 25 + 7.5 = **92.5**

---

## V-02 — Output Format (Table-First, Closed-Column Schema)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Skill identity declared | PARTIAL | Output schema is purely table-based ("No prose criterion blocks"); no frontmatter or header block shown in the output spec — skill identity declaration is unanchored |
| C-02 | Criteria are testable | PASS | Closed column schema with `Fail signal` column makes every criterion machine-checkable |
| C-03 | Pass condition enforced | PASS | Step 2 and Step 3 both mandate "must/contains/states/lists" only; `Fail signal` column provides a second enforcement signal |
| C-04 | Scoring formula explicit | PARTIAL | "Step 5 — Write the scoring formula" is present but body is truncated in the prompt; formula spec is unverifiable |
| C-05 | Tier structure present | PASS | Tier quotas table names Essential / Recommended / Aspirational with minimum/maximum row counts |

**Essential gate**: FAIL (C-01 PARTIAL, C-04 PARTIAL)
**Base capped at 40**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Failure modes cataloged | FAIL | No failure analyst phase; no F-ID requirement; table-first schema skips failure cataloging entirely |
| C-07 | Specificity test included | PARTIAL | Step 1 asks "What distinguishes a specific output for this input from a generic template?" but this is an input-analysis question, not a scoreable criterion in the output rubric |
| C-08 | Version and date stamped | FAIL | No frontmatter block defined; table schema has no version/date column or header field |

**Recommended**: 0.5 / 3 → **5 pts**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Coverage of all output sections | PARTIAL | Step 1 extracts named sections from the target skill spec; table rows could cover them, but no rule enforces it |
| C-10 | Scoring formula includes partial credit | PASS | Step 3 explicitly distinguishes FAIL vs PARTIAL with separate observable signals |
| C-11 | External enforcement gate | FAIL | No prohibitions block, no named review role; the table schema is structural but not a named enforcement gate |
| C-12 | Failure-first derivation | FAIL | No failure analyst phase; Step 1 is "identify output contract", not "catalog failure modes" |
| C-13 | Generic-vs-specific foil pair | FAIL | No before/after example |
| C-14 | Explicit category enumeration in field rules | PASS | Category column in table schema uses closed list: `correctness / depth / format / coverage / behavior` |

**Aspirational**: 2.5 / 6 → **4.2 pts**

### V-02 Total: 40 + 5 + 4.2 = **49.2**

---

## Ranking (V-01 and V-02)

| Rank | Variation | Score | Essential Gate |
|------|-----------|-------|----------------|
| 1 | V-01 (Role sequence) | **92.5** | PASS |
| 2 | V-02 (Table-first) | **49.2** | FAIL |

---

## Excellence Signals (V-01)

**Signal 1 — Failure-first role sequencing closes C-12 structurally**
By making the failure analyst a named Role that must complete before Role 2 is permitted to begin, V-01 satisfies C-12 without needing an explicit "failure-first criterion" — the sequence itself is the gate. V-02 omits this entirely.

**Signal 2 — Prohibitions block doubles as enforcement gate (C-11)**
The `## Prohibitions` section at the end of V-01 is a named, enumerated checklist of three explicit bans. This satisfies C-11 without requiring a separate review role. V-02 has no equivalent structure.

**Persistent gap — C-13 absent in both**
Neither variation includes a generic-vs-specific foil pair near the specificity guidance. Every round that receives C-07 PARTIAL traces back to this missing foil. V-01 gets C-07 PARTIAL because its specificity enforcement is a prohibition, not a criterion — adding a foil pair would convert this to PASS.

**V-03–V-05 note**
These variations were not included in the prompt. If they exist, they should be scored before finalizing Round 3 rankings.

---

```json
{"top_score": 92.5, "all_essential_pass": true, "new_patterns": ["failure-analyst-first role sequence satisfies C-12 structurally without a dedicated specificity criterion", "named prohibitions block serves as C-11 enforcement gate without requiring a separate review role"]}
```
