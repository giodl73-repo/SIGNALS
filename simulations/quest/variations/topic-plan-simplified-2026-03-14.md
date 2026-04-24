Good. The simplified prompt looks clean. Now the verification + report:

---

## Simplification Report — `topic:plan` V-05 → Minimal

### What was removed and why

| Category | Removed | Words saved | Rationale |
|---|---|---|---|
| Rule "exists because" ×5 | Rationale paragraphs from Rules 1–5 | ~124 | Enforcement comes from PASS/FAIL examples + format spec; rationale is explanatory, not behavioral |
| Per-step schema-commitment checkpoints ×4 | "Schema-commitment checkpoint: I am about to produce X with columns Y..." in Steps 4a, 4b, 4c, 6 | ~115 | Columns are declared in the Upfront Schema section + enforced by table headers + "mandatory" lines; triple-listing was redundant |
| Step 3 anti-pattern checkpoint | "An inventory tells me what exists. A delta tells me what changed. I will not conflate them." | 19 | The step instruction (classify NEW vs PRIOR + SIGNAL READ-LOCK) already enforces the separation |
| D-01 sample row in Step 2 | `| D-01 | [element] | [argument] | ... |` | 9 | Column headers make the format self-evident |
| SIGNAL READ-LOCK verbosity | Original 29-word version → 17-word version | 12 | Same constraint, shorter form |
| Step 1 persona framing | "Then as the person responsible for delta detection, scan:" → "Scan:" | 9 | Role framing is implicit in the skill context |
| Step 1 STRATEGY DATE | "Record its last-modified date as the STRATEGY DATE" → "(STRATEGY DATE = last-modified date)" | 5 | Same information, inline |
| INERTIA-GATE preamble | 36 words → 18 words | 18 | Kept: "each [INERTIA-GATE] site", "do not abbreviate/paraphrase/omit", "presence required" — same enforcement |
| Rule 5 PASS example | Long specific example → "specific named signal with deferral consequence stated — not generic" | 10 | PASS + FAIL together: the generic-vs-specific contrast is preserved |
| Step 4b Inertia instruction | Removed redundant sentence "One sentence per row naming..." | 8 | Already stated in full in Step 4a; "identical schema to Step 4a (Rule 5)" carries the reference |
| Step 7 display list | Full names → "Step 3b / Step 4a / Step 4b / Step 4c (with calibration check) / Step 6" | 12 | Step numbers are unambiguous; no information lost |
| Step 6 brackets instruction | Verbose → "Include [evidence brackets] in each After cell and Proposal cross-refs (e.g., 'ADD-1') per row" | 7 | Same behavioral spec, shorter form |
| Step 4c Defense basis | "cite D-ID if pre-registered; write 'Newly constructed' if built after signal reading" → "D-ID if pre-registered; 'Newly constructed' if built after signal reading" | 7 | Same values, drop "cite"/"write" verbs |
| Step 4a null text | "ADDITIONS: none — inertia holds for all candidate additions" → "ADDITIONS: none — inertia holds" | 4 | REMOVALS/REPRIORITIZATIONS null text never had "for all candidate X" — standardized |
| Step 4b null label | "— each type independently declared" removed from label | 5 | Rule 3 definition already states "each absent change type must have its own independently labeled declaration" |
| Upfront commitment wording | "Schema-commitment checkpoint: I commit to these column sets before Step 1. I will not substitute prose for any table. I will not merge Step 4a and 4b." → "Pre-read commitment: columns above are fixed. No prose substitutes. No table merges. I will not merge Step 4a and 4b." | 11 | Pre-read framing preserved; anti-merge stated explicitly |
| Step 2 timing instruction | "Complete and output before reading any NEW artifact." → "Output before reading any NEW artifact." | 2 | "Complete and" is implied by "Output" |

### What was kept (and why it was kept)

- **Rule 3 failure condition**: "A single unlabeled 'No changes proposed'...fails Rule 3" — Pattern 2 from R20 excellence: rules must carry explicit failure conditions
- **Rule 5 "Why this beats NO CHANGE is not a valid substitute"** + "Both tables must carry the identical column or neither achieves C-64" — Pattern 1 anti-circumvention language
- **Note in upfront schema**: "Do not merge the two tables. Do not rename the column in either table." — Pattern 1 structural escapes closed
- **INERTIA-GATE box content intact**: Including "This block is reproduced verbatim at Steps 4, 4b, 6, and 7" (C-62 manifest)
- **All four [INERTIA-GATE] trigger sites**: Steps 4, 4b, 6, 7
- **All null texts verbatim**: All type-labeled null declarations preserved at all sites
- **Step 4 preamble**: "A proposal that cannot name a concrete consequence of deferral...is a preference, not a decision — structurally invalid, not merely incomplete"
- **SIGNAL READ-LOCK** constraint (shortened, not removed)
- **Pre-signal Defense Register** (Step 2) intact

### Essential criteria check

| Criterion | Still present in simplified prompt? |
|---|---|
| All required columns declared in upfront schema | YES — lines 61–87 |
| INERTIA-GATE block with site manifest (C-62) | YES — box contains "reproduced verbatim at Steps 4, 4b, 6, and 7" |
| INERTIA-GATE reproduced at all 4 sites | YES — triggers at Steps 4, 4b, 6, 7 |
| Type-labeled null declarations (C-63) | YES — all 6 null sites carry labeled text; Rule 3 states failure condition |
| Symmetric "Inertia Rejected Because [REQUIRED]" column (C-64) | YES — both tables in upfront schema + Note prohibiting merge/rename |
| Pre-read schema commitment | YES — "Pre-read commitment" block before Step 1 |
| Rule 4 two-hop Delta Finding format | YES — intact in Rule 4 and column headers |
| Calibration check in Step 4c | YES — intact |
| Confirmation gate verbatim format | YES — intact |
| Rule 3 explicit failure condition | YES — "A single unlabeled...fails Rule 3" preserved |

**All essential criteria: YES**

---

```json
{"simplified_word_count": 1601, "original_word_count": 2008, "all_essential_still_pass": true}
```
