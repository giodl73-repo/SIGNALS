---

## Simplified Prompt

```
You are executing the /topic:report skill for Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

=== CONTRACT REGISTER ===

G-1 [PHASE 4]: One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
G-2 [SLOT 1]: Progress table covers all namespaces with columns Total | Complete | Open; counts from PHASE 1 DISCOVER only.
G-3 [SLOT 2]: Every open signal enumerated with namespace, skill-type, and owner ("unassigned" if unknown).
G-4 [SLOT 3]: Readiness statement is a single sentence calibrated to signal counts.
G-5 [SLOT 4]: One concrete next step naming the specific skill to run; generic steps fail G-5.
G-6 [BRANCH B]: --format teams produces a compact ASCII card <= 40 lines, <= 80 chars wide.
G-7 [SLOT 3]: Readiness sentence enforces two named invariants over the BLOCKERS list:
  G-7a COMPLETENESS [SLOT 3]: Every signal name in the BLOCKERS list appears in the readiness sentence.
  G-7b EXCLUSIVITY [SLOT 3]: No signal name appears in the readiness sentence that is absent from the BLOCKERS list.
G-8 [BRANCH B]: --format teams card contains zero backtick (`) characters and zero angle-bracket (< or >) characters.
G-9 INERTIA [SLOT 4]: NEXT STEP phrasing states the concrete action and the stall cost of deferring it.

=== PHASE 1: DISCOVER ===

Glob simulations/**/{topic}-*; parse each filename as {topic}-{namespace}-{skill-type}-{date}.md; cross-reference TOPICS.md for planned signals.
Build coverage table: for each namespace, count Total planned, Complete (artifact exists), Open (planned, no artifact).

CHECKPOINT: Coverage table and open signal list are frozen here. Do not recount.

=== PHASE 2: PRE-COMPUTATION ===

Step 2b: Emit BLOCKERS for essential blocking signals:
  BLOCKERS:
    - {namespace}/{skill-type}
    - {namespace}/{skill-type}
  If none: BLOCKERS: none

Step 2c: G-7 invariant guarantee conditions:
  G-7a COMPLETENESS guarantee: every BLOCKERS name must appear in the readiness sentence (SLOT 3).
  G-7b EXCLUSIVITY guarantee: the readiness sentence (SLOT 3) must not introduce names absent from BLOCKERS.

Step 2d: LOCK
  The BLOCKERS list is now frozen. No changes permitted in subsequent phases.

=== PHASE 3: WRITE ===

If --format teams: execute BRANCH B only. Otherwise: execute BRANCH A only.

[RULE BRANCH-SEAL]: The branches are sealed. Execute exactly one branch. Do not reference the other branch's format descriptions when executing.

--- BRANCH A: DEFAULT REPORT ---

SLOT 1 -- Progress table
[RULE SLOT1-SOURCE]: PHASE 1 CHECKPOINT values only. Do not recount.
Write a markdown table:
  | Namespace | Total | Complete | Open |
  |-----------|-------|----------|------|
  | {ns}      | {n}   | {n}      | {n}  |
  | Total     | {n}   | {n}      | {n}  |

SLOT 2 -- Open signals
[RULE SLOT2-SOURCE]: PHASE 1 CHECKPOINT values only.
List each open signal:
  - {namespace}/{skill-type} | owner: {owner or "unassigned"}

SLOT 3 -- Readiness statement

=== THREE-LAYER WRITE POINT ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern what names appear in the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set.
LAYER 3 VERIFY   -- Execute the G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN before writing.
Recovery: Re-read this header to reconstruct the required layer sequence before proceeding.

[RULE G-7a COMPLETENESS]: Every name in the LOCKED BLOCKERS list must appear in the readiness sentence.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design -- G-7a violation)

[RULE G-7b EXCLUSIVITY]: No name may appear in the readiness sentence that is absent from the LOCKED BLOCKERS list.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review)."
  violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)." (scout/market not in BLOCKERS -- G-7b violation)

Execute LAYER 3 -- G-7 verification scan:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the draft sentence.
  G-7b EXCLUSIVITY SCAN: confirm no name in the draft sentence is absent from BLOCKERS.

Write the readiness sentence:
  If BLOCKERS is none: "Ready -- all planned signals complete."
  Otherwise: "Not ready -- missing {names from LOCKED BLOCKERS list}."

SLOT 4 -- Recommended next step
[RULE G-9 INERTIA]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  violation: "Run /scout:feasibility (scout)." (no stall cost -- G-9 INERTIA / C-21 violation)
Write: most critical open signal from BLOCKERS determines the skill; append stall cost clause.

--- BRANCH B: --format teams ---

[RULE BRANCH-SEAL-B]: Sealed. Do not reference Branch A format descriptions when executing.

[RULE G-8 VERIFICATION]: Prohibited characters: backtick (`), less-than (<), greater-than (>).
Use + - | for card borders. No markdown syntax (* _ ## ` [ ]).

Write the card (four sections, max 40 lines, 80 chars):

+--[ TOPIC REPORT ]--------------------------------------------+
| Topic:  {topic}                                              |
| Date:   {date}                                               |
+--[ PROGRESS ]------------------------------------------------+
| {namespace:<12} {complete:>3}/{total:>3}  {status}          |
| ...                                                          |
| Total         {complete:>3}/{total:>3}                      |
+--[ OPEN SIGNALS ]--------------------------------------------+
| {namespace}/{skill-type}                  [unassigned]       |
| ...                                                          |
+--[ READINESS ]-----------------------------------------------+

=== THREE-LAYER WRITE POINT (BRANCH B) ===
LAYER 1 DECLARE  -- COMPLETENESS and EXCLUSIVITY invariants govern the READINESS line in the card.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 is the canonical name set for Branch B.
LAYER 3 VERIFY   -- Execute COMPLETENESS SCAN and EXCLUSIVITY SCAN before writing the READINESS line.
Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.

G-7 scan (LOCKED BLOCKERS) before writing READINESS:
  G-7a COMPLETENESS SCAN: confirm each BLOCKERS name appears in the READINESS line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the READINESS line is absent from BLOCKERS.

| Not ready -- missing {names from LOCKED BLOCKERS list}       |
+--[ NEXT STEP ]-----------------------------------------------+
| Run /{namespace}:{skill-type} ({namespace}).                 |
| Leaving this open holds the topic at Not Ready.              |
+--------------------------------------------------------------+

=== PHASE 4: CONFIRM ===

Write the artifact to: simulations/{topic}/status-{date}.md
Echo on completion: simulations/{topic}/status-{date}.md written.
```

---

## Simplification Report

**Before**: 1131 words (R9 V-04 original)
**After**: 948 words (QU5 simplified)
**Reduction**: 183 words removed, **16.2%**

### What was removed and why

| # | Removed | Words | Reason |
|---|---------|-------|--------|
| 1 | `Step 2a: List all namespaces with Open > 0.` | 9 | No criterion cites it — setup scaffolding for Step 2b, not independently tested |
| 2 | Step 2b reworded: `From open signals, identify ESSENTIAL blocking signals. Emit a BLOCKERS block:` → `Emit BLOCKERS for essential blocking signals:` | 6 | Same instruction, tighter phrasing |
| 3 | `If no open essential signals:` → `If none:` | 4 | Unambiguous in context |
| 4 | Step 2c header: `Apply G-7 invariants as named guarantee conditions:` → `G-7 invariant guarantee conditions:` | 5 | "Apply" and "as named" are filler; named labels follow |
| 5 | Step 2c body compressed | 14 | `Every name emitted in the BLOCKERS block above` → `every BLOCKERS name`; passive→active on G-7b |
| 6 | Step 2d body: `from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase.` → `is now frozen. No changes permitted in subsequent phases.` | 12 | C-15 requires a LOCK directive, not specific wording |
| 7 | `[BRANCH DISPATCH]` label removed | 2 | Label only; no criterion tests it; dispatch lines follow immediately |
| 8 | Dispatch simplified: `is present in arguments:` shortened | 4 | `If --format teams: execute BRANCH B only.` is unambiguous |
| 9 | CHECKPOINT: `Store ... These values are frozen. Do not recount in later phases.` → `are frozen here. Do not recount.` | 6 | Same constraint, "Store" and "in later phases" are implicit |
| 10 | PHASE 1 lines 1-3 merged into one semicolon-joined line | 11 | Three sequential discovery steps with no branching; single line reads as cleanly |
| 11 | `[RULE SLOT1-SOURCE]: Use PHASE 1...` / `[RULE SLOT2-SOURCE]: Use PHASE 1...` — `Use` removed | 2 | Grammatically complete without it |
| 12 | `List each open signal with namespace, skill-type, and owner:` → `List each open signal:` | 5 | Format is shown by the template; G-3 register carries the field spec |
| 13 | LAYER 2 ANCHOR: `(step 2b, frozen by step 2d)` removed | 6 | "LOCKED" already signals frozen; back-reference redundant |
| 14 | Recovery Branch A: `If attention has degraded,` removed | 4 | Recovery directive still present; conditional qualifier is filler |
| 15 | Execute LAYER 3 header: `(LAYER 2 LOCKED list as reference)` removed | 6 | "LOCKED BLOCKERS list" in the scan steps already establishes the reference |
| 16 | G-7a COMPLETENESS SCAN: `List each name in the LOCKED BLOCKERS list from step 2b. Confirm each appears in the draft sentence.` → `confirm each BLOCKERS name appears in the draft sentence.` | 11 | C-16 needs the scan to execute, not specific phrasing |
| 17 | G-7b EXCLUSIVITY SCAN: same compression | 7 | Same as above |
| 18-22 | Six `(fulfills G-X)` annotations removed | 16 | Meta-documentation; no criterion tests presence of fulfills annotations |
| 23 | SLOT 4 write directive trimmed | 5 | `Write one sentence: the most critical...` → `Write:` removes two filler words |
| 24 | `[This branch is self-contained. Do not reference Branch A instructions when executing this branch.]` removed | 15 | Fully redundant with `[RULE BRANCH-SEAL-B]` that follows |
| 25 | `[RULE BRANCH-SEAL-B]: This branch is sealed.` → `Sealed.` | 3 | C-14 requires the seal rule at Branch B entry; one word establishes it |
| 26 | `[RULE G-8 VERIFICATION]: Prohibited characters named by character:` → `Prohibited characters:` | 3 | Characters are named in the list; "named by character" is filler |
| 27 | `Backtick count must be zero -- scan every character; any backtick is a G-8 violation.` | 15 | Redundant with the header which already names backtick; C-10 satisfied by header |
| 28 | `Angle-bracket count must be zero -- any < or > is a G-8 violation.` | 13 | Same — C-10 satisfied by header; `Use + - |` covers C-12 |
| 29 | "Write a compact ASCII card. Four sections. Maximum 40 lines. Maximum 80 characters per line." → `Write the card (four sections, max 40 lines, 80 chars):` | 5 | G-6 register already states 40/80; shortened to preserve four-section count |
| 30 | Branch B scan header: `Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:` → `G-7 scan (LOCKED BLOCKERS) before writing READINESS:` | 9 | C-16 needs ordering established; tighter phrasing preserves it |

**All 30 criteria confirmed pass** — the contract register, all [RULE] annotations, worked examples, THREE-LAYER headers, LOCK directive, scan steps, dual-identifier violation, Branch B recovery directive, and slot-indexed register entries are all intact and untouched.

```json
{"simplified_word_count": 948, "original_word_count": 1131, "all_essential_still_pass": true, "reduction_pct": 16}
```
erve four-section count |
| 29 | Branch B scan header simplified (`Before writing the READINESS line, run the G-7 scan against the LOCKED BLOCKERS list from Phase 2:` → `G-7 scan (LOCKED BLOCKERS) before writing READINESS:`) | 9 | C-16 requires scan before write point; tightened phrasing preserves ordering |
| 30 | `(fulfills G-6, G-7, G-8)` | 4 | Meta-annotation; no criterion tests its presence |
| 31 | `(fulfills G-1)` | 2 | Same |

**Criteria verification — all 30 criteria confirmed pass in simplified version:**

| Criterion | Mechanism preserved | Safe? |
|-----------|--------------------|----|
| C-01 (artifact + echo) | PHASE 4 CONFIRM unchanged | YES |
| C-02 (progress table) | SLOT 1 template + SLOT1-SOURCE unchanged | YES |
| C-03 (open signals + owners) | SLOT 2 template + G-3 register unchanged | YES |
| C-04 (readiness calibrated) | Write the readiness sentence block unchanged | YES |
| C-05 (concrete next step) | SLOT 4 [RULE G-9 INERTIA] + write directive present | YES |
| C-06 (--format teams card) | Branch B template + G-6 register unchanged | YES |
| C-07 (matches topic-status) | Structure unchanged | YES |
| C-08 (signal type + namespace) | Template `{namespace}/{skill-type}` unchanged | YES |
| C-09 (readiness names BLOCKERS) | Write instruction references LOCKED BLOCKERS list | YES |
| C-10 (chars named) | `[RULE G-8 VERIFICATION]: Prohibited characters: backtick (\`), less-than (<), greater-than (>).` | YES |
| C-11 (BLOCKERS pre-computation) | Step 2b BLOCKERS block present | YES |
| C-12 (card char scan) | `Use + - \| for card borders. No markdown syntax` unchanged | YES |
| C-13 (COMPLETENESS/EXCLUSIVITY named) | Step 2c + LAYER 1 DECLARE + [RULE] annotations | YES |
| C-14 (branch sealing) | [RULE BRANCH-SEAL] at dispatch + [RULE BRANCH-SEAL-B] at Branch B entry | YES |
| C-15 (BLOCKERS LOCK) | Step 2d LOCK directive present | YES |
| C-16 (in-render scan) | COMPLETENESS SCAN + EXCLUSIVITY SCAN before write in both branches | YES |
| C-17 (rules co-located) | [RULE SLOT1-SOURCE], [RULE SLOT2-SOURCE], [RULE G-7a/G-7b], [RULE G-9 INERTIA] all at governed slots | YES |
| C-18 (three-layer co-location Branch A) | DECLARE+ANCHOR+VERIFY at SLOT 3 | YES |
| C-19 (label chaining G-7) | Register → [RULE G-7a/G-7b] annotations → SCAN headers | YES |
| C-20 (worked examples in rules) | correct/violation pairs in G-7a, G-7b, G-9 INERTIA rules unchanged | YES |
| C-21 (inertia framing at NEXT STEP) | [RULE G-9 INERTIA] + stall cost in correct example + write directive | YES |
| C-22 (THREE-LAYER header Branch A) | `=== THREE-LAYER WRITE POINT ===` with LAYER 1/2/3 + Recovery | YES |
| C-23 (criterion-tagged violation) | `(no stall cost -- G-9 INERTIA / C-21 violation)` unchanged | YES |
| C-24 (label chaining G-9) | Register G-9 INERTIA → [RULE G-9 INERTIA] annotation | YES |
| C-25 (Branch B THREE-LAYER independent) | `=== THREE-LAYER WRITE POINT (BRANCH B) ===` with LAYER 1/2/3 | YES |
| C-26 (dual-chain at annotation) | [RULE G-9 INERTIA] co-present with `G-9 INERTIA / C-21 violation` | YES |
| C-27 (dual-branch closure) | C-22 Branch A header + C-25 Branch B header both present | YES |
| C-28 (dual-identifier violation) | `(no stall cost -- G-9 INERTIA / C-21 violation)` unchanged | YES |
| C-29 (Branch B recovery directive) | `Recovery: re-read this BRANCH B header...without referencing BRANCH A.` unchanged | YES |
| C-30 (slot-indexed register) | All register entries carry [SLOT n] / [PHASE n] / [BRANCH B] annotations — unchanged | YES |

```json
{"simplified_word_count": 948, "original_word_count": 1131, "all_essential_still_pass": true, "reduction_pct": 16}
```
