---

## QU5 Simplification Report — campaign-evidence (V-05, Round 20)

**File written:** `simulations/quest/golden/campaign-evidence-variate-R20-QU5-simplified-2026-03-17.md`

---

### Simplified Prompt Body

*(See file for full runnable prompt — excerpt of structure below)*

```
You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE
Finalized before Stage 1 begins. Immutable...

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture
[6-row IB fixture with ID, Name, Rule, Detection, Consequence]

HOMOGENEITY INVARIANT (C-50): All cell tiers (PRE binary, POST binary, N/A) cite IB-IDs uniformly...

#### Rule Registry
[6 rules — invocation signatures + excluded antipatterns, no principle quotes]

#### Role Roster / Coverage Map (immutable) / Gate Record Template / Form Templates
[all 10 PRE/POST forms with C-48/C-50 cells intact]

### Stage 1–5 [Intel-first; lean entry/exit/handoff blocks]

### Final Output [Section 1–3 + FK-typed audit table]
```

---

### What was removed and why

| Removed | ~Words | Reason |
|---------|--------|--------|
| Rule Registry extensibility note | 22 | C-36 only; not essential |
| Principle quotes (FALSIFICATION + SEQUENCING-HYPO, 3 occurrences) | 37 | Motivational framing; structural rule is already stated |
| Checksum decomposition history ("Architectural history: prior monolithic...") | 90 | Historical narrative; formula + total is all that executes |
| N/A parenthetical elaborations in 5 PRE forms | 60 | "antipattern not applicable" elaboration trimmed to bare reason code |
| Handoff "Artifacts transferred" + "authorized reads" lines | 100 | Exact duplicates of Role Roster table |
| Timing directive verbosity per stage | 40 | C-48/C-50 check condensed to one line; "(from preamble)" removed |
| Preamble stage ordering note | 19 | Fully redundant with SEQUENCING-ORDER rule and Stage 1 header |
| Column contracts footer | 20 | Condensed to single line; structural content preserved |
| Stage 1/2 "Include:" execution guidance detail | 30 | Quality hints; no essential criterion requires them |
| Label verbose suffixes | 40 | Coverage Map, Gate Record, Form Templates, Role Roster labels trimmed |

---

### Essential Criteria Verification

| Criterion | Pass? | Basis |
|-----------|-------|-------|
| C-01 Multi-stage campaign (5 stages) | **YES** | Stages 1–5 with named roles, gates, artifacts intact |
| C-02 Evidence before hypothesis | **YES** | SEQUENCING-HYPO rule + S3 blocked by S2 exit gate |
| C-03 Hypotheses with falsification conditions | **YES** | FALSIFICATION RULE + `[IB-FALS]` guard in Stage 3 execution |
| C-04 Output is self-contained | **YES** | Final Output Section 1 = Evidence Brief in full; campaign summary required |
| C-48 Binary cells typed-ID-only | **YES** | Cell format contract + all 10 form tables use `[IB-XXX]`-only |
| C-49 Audit table FK-typed column | **YES** | `Antipattern (IB-ID FK)` column present; column contracts enforce IB-IDs |
| C-50 Three-tier homogeneity | **YES** | HOMOGENEITY INVARIANT declared; N/A cells carry `[IB-XXX]`; C-50 contract present |

---

```json
{"simplified_word_count": 2452, "original_word_count": 3070, "all_essential_still_pass": true}
```
