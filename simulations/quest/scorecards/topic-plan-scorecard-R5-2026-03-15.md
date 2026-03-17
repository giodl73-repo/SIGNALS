## Round 5 — topic:plan Scorecard (rubric v5, C-01–C-23)

---

### Variation Scoring

#### V-01 — Named-violation vocabulary contract (C-21 target)

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | Phase 1 reads TOPICS.md to find strategy file; Schema A records Strategy file + date |
| C-02 | PASS | Schema C has all 9 namespace rows as required table |
| C-03 | PASS | Schema B NEW/PRIOR column; Phase 3 delta partition sentence; "PRIOR artifacts may not drive proposals" |
| C-04 | PASS | Schema E (Additions), Schema F (Removals/Reprioritizations); typed null declarations per type |
| C-05 | PASS | Phase 6 PENDING CONFIRMATION block; "Stop. Write nothing further until the user replies." |
| C-06 | PASS | "Evidence artifact" column in Schemas E and F |
| C-07 | PASS | Schema G (Before/after diff) present with Before/After/Proposal ref columns |
| C-08 | PASS | "vs. NO CHANGE: mandatory column; name a specific consequence" — per-row inertia justification |
| C-09 | PASS | Null declarations: ADDITIONS / REMOVALS / REPRIORITIZATIONS labeled separately |
| C-10 | PARTIAL | Schema H present but not in its own numbered phase; no "CONFLICT DETECTION — NULL" typed null |
| C-11 | PASS | All phases use pre-committed table schemas; VOCABULARY CONTRACT check at each gate |
| C-12 | PASS | Each phase: "Do not advance to Phase N without Gate N STATUS: PASS" |
| C-13 | PARTIAL | "vs. NO CHANGE: mandatory column" stated in Phase 5 prose, not in column header itself |
| C-14 | PASS | VOCABULARY CONTRACT defines `??` and `--`; "VIOLATION-1: blank cell" enforces sentinel filling |
| C-15 | PASS | Phase 3: exact template "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR." |
| C-16 | PASS | "'No change needed' is not an acceptable entry in this column" — named and banned |
| C-17 | PASS | Two-tier tokens defined: `??` (open obligation, unknown) vs `--` (closed decision, absent/NA) |
| C-18 | FAIL | No Phase 0; no pre-signal defense register |
| C-19 | PASS | "Writing 'a few', 'several', 'some', or any non-integer value is a gate failure, not a quality concern" |
| C-20 | PASS | Gate 1→Phase 2, Gate 2→Phase 3 … Gate 5→Phase 6: sequential numbered linkage throughout |
| C-21 | PASS | VOCABULARY CONTRACT enumerates VIOLATION-1 (blank), VIOLATION-2 (?? for confirmed zero), VIOLATION-3 (-- in required cell) |
| C-22 | FAIL | No Schema DR; no "Defense defeated: Row D-R-N" column; no row-number citation requirement |
| C-23 | PARTIAL | One verbatim-quoted phrase ("No change needed") — satisfies quoting but not a comprehensive list |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 10 + 1.5 (3 partial) = 11.5/15 → 7.67
**V-01 total: 97.67**

---

#### V-02 — Defense register with row-number anchors (C-22 target)

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | Phase 0 reads strategy file from TOPICS.md; Schema A filled before any artifact read |
| C-02 | PASS | Schema C 9 rows; "NEVER write ABSENT"; zero-counts as 0 |
| C-03 | PASS | Delta sentence; "PRIOR artifacts may not drive proposals" |
| C-04 | PASS | Schemas E + F; null declarations per type |
| C-05 | PASS | Phase 6 PENDING CONFIRMATION; "Stop. Write nothing further…" |
| C-06 | PASS | "Evidence artifact" column in Schemas E and F |
| C-07 | PASS | Schema G (Before/after diff) |
| C-08 | PASS | "vs. NO CHANGE: name a specific consequence of leaving the strategy unchanged" |
| C-09 | PASS | Null declarations labeled per type |
| C-10 | PARTIAL | Schema H present; not in own phase; no typed null form |
| C-11 | PASS | Pre-committed table schemas for all phases |
| C-12 | PASS | "Do not advance to Phase N without Gate N STATUS: PASS" — Gate 0 through Gate 5 |
| C-13 | PARTIAL | "Defense defeated (Row D-R-N): MANDATORY" stated in Phase 5 prose but not in column header |
| C-14 | PARTIAL | "ABSENT not used" and zero-count rules present; no VOCABULARY CONTRACT; no `??`/`--` formally defined |
| C-15 | PASS | Exact count sentence template with integer-only enforcement |
| C-16 | PASS | "vs. NO CHANGE: name a specific consequence" — disqualifies generic entries |
| C-17 | FAIL | No VOCABULARY CONTRACT; `??` and `--` not formally defined with distinct semantics |
| C-18 | PASS | Phase 0 pre-signal defense register; Schema DR locked before Phase 2 (before any artifact read) |
| C-19 | PASS | "'a few', 'several', 'some', or any non-integer value is a gate failure" |
| C-20 | PASS | Sequential: Gate 0→Phase 1 … Gate 5→Phase 6 |
| C-21 | FAIL | No VOCABULARY CONTRACT; no named violation conditions |
| C-22 | PASS | Schema DR with D-R-N row numbers; "Defense defeated: Row D-R-[N]" mandatory; "A named defense without a row number does not satisfy this requirement" |
| C-23 | PARTIAL | "A defense argument of 'no reason to change' is not acceptable" — one verbatim-quoted banned form; no comprehensive list |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 9 + 2.0 (4 partial) = 11/15 → 7.33
**V-02 total: 97.33**

---

#### V-03 — Verbatim-quoted banned forms everywhere (C-23 target)

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | Reads TOPICS.md + strategy.md; Schema A |
| C-02 | PASS | Schema C 9 rows |
| C-03 | PASS | NEW/PRIOR delta; PRIOR excluded |
| C-04 | PASS | Schemas E + F; labeled null declarations |
| C-05 | PASS | Phase 6 PENDING CONFIRMATION; Stop instruction |
| C-06 | PASS | Evidence artifact column in Schemas E + F |
| C-07 | PASS | Schema G Before/after diff |
| C-08 | PASS | "vs. NO CHANGE: MANDATORY — name a specific consequence" with BANNED FORMS check |
| C-09 | PASS | Null declarations per type with BANNED FORMS applied to reasons |
| C-10 | PARTIAL | Schema H present; no own phase; no typed null |
| C-11 | PASS | Pre-committed table schemas |
| C-12 | PASS | Sequential phase-linked stop gates |
| C-13 | PARTIAL | "vs. NO CHANGE: MANDATORY" in Phase 5 prose; column header unlabeled |
| C-14 | PARTIAL | Anti-blank rules present; no `??`/`--` VOCABULARY CONTRACT |
| C-15 | PASS | Exact count sentence; integer enforcement |
| C-16 | PASS | BANNED FORMS listed explicitly with "Check cell against BANNED FORMS list before presenting. Any banned form disqualifies the row" |
| C-17 | FAIL | No VOCABULARY CONTRACT; no two-tier sentinel |
| C-18 | FAIL | No Phase 0 defense register |
| C-19 | PASS | "BANNED COUNT FORMS: writing 'a few', 'several', 'some', 'multiple', 'many'… is a gate failure" |
| C-20 | PASS | Sequential phase-linked gates |
| C-21 | FAIL | No VOCABULARY CONTRACT; no named violation conditions |
| C-22 | FAIL | No Schema DR; no row-number citation |
| C-23 | PASS | Comprehensive lists: 5 verbatim-quoted strings in Schema E/F; 4 in null declaration reasons; 5 in count sentence — all exact quoted form |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 8 + 1.5 (3 partial) = 9.5/15 → 6.33
**V-03 total: 96.33**

---

#### V-04 — Combination C-21 + C-22

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | Phase 0 reads strategy.md; Schema A |
| C-02 | PASS | Schema C 9 rows with VOCABULARY CONTRACT check |
| C-03 | PASS | Delta partition; PRIOR excluded |
| C-04 | PASS | Schemas E + F; typed null declarations |
| C-05 | PASS | Phase 6 PENDING CONFIRMATION; Stop |
| C-06 | PASS | Evidence artifact column |
| C-07 | PASS | Schema G Before/after diff |
| C-08 | PASS | "vs. NO CHANGE: specific consequence of leaving strategy unchanged" mandatory |
| C-09 | PASS | Null declarations labeled per type |
| C-10 | PARTIAL | Schema H present; not in own phase; no typed null |
| C-11 | PASS | Pre-committed table schemas; VOCABULARY CONTRACT enforced at every gate |
| C-12 | PASS | Gate 0 through Gate 5 each with phase-linked stop gate |
| C-13 | PARTIAL | "Defense defeated column: MANDATORY" stated in post-schema labeled block; column header says "Defense defeated (Row D-R-N)" not "MANDATORY" |
| C-14 | PASS | VOCABULARY CONTRACT defines `??` and `--`; VIOLATION-1 applied to every schema cell |
| C-15 | PASS | Exact count sentence; "'A few', 'several', 'some', or any non-integer is a gate failure" |
| C-16 | PASS | "'No change needed' is not an acceptable entry in vs. NO CHANGE" — named and banned |
| C-17 | PASS | VOCABULARY CONTRACT: `??` (open obligation) vs `--` (closed decision) with distinct semantics |
| C-18 | PASS | Phase 0 pre-signal defense register; Schema DR locked; all D-R arguments from strategy.md |
| C-19 | PASS | Integer enforcement named as gate failure condition |
| C-20 | PASS | Gate 0→Phase 1 … Gate 5→Phase 6: sequential numbered linkage |
| C-21 | PASS | VOCABULARY CONTRACT: VIOLATION-1, VIOLATION-2, VIOLATION-3 enumerated with specific misuse conditions |
| C-22 | PASS | Schema DR D-R-N rows; "Defense defeated (Row D-R-N): MANDATORY row number from Schema DR"; "A named defense without a row number does not satisfy this column" |
| C-23 | PARTIAL | "'No change needed' is not an acceptable entry" — one verbatim form; no comprehensive verbatim list |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 12 + 1.5 (2 partial) = 13.5/15 → 9.0
**V-04 total: 99.0**

---

#### V-05 — Full combination C-21 + C-22 + C-23

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | Phase 0 reads strategy.md; Schema A |
| C-02 | PASS | Schema C 9 rows; VOCABULARY CONTRACT: confirmed zeros as 0, not `??`, not ABSENT |
| C-03 | PASS | Delta partition; PRIOR excluded |
| C-04 | PASS | Schemas E + F; null declarations with banned forms embedded inline in templates |
| C-05 | PASS | Phase 6 PENDING CONFIRMATION with integer counts; Stop |
| C-06 | PASS | Evidence artifact column |
| C-07 | PASS | Schema G Before/after diff |
| C-08 | PASS | vs. NO CHANGE mandatory column + banned forms list enforcement at Gate 5 |
| C-09 | PASS | Null declarations labeled per type; banned forms applied to each reason inline |
| C-10 | PARTIAL | Schema H present; not in dedicated numbered phase; no "CONFLICT DETECTION — NULL" typed null |
| C-11 | PASS | Pre-committed table schemas; VOCABULARY CONTRACT enforced at every gate |
| C-12 | PASS | Gate 0 through Gate 5 with "Do not advance to Phase N" sequential linkage |
| C-13 | PARTIAL | "MANDATORY: Defense defeated must cite exact Schema DR row number" stated as labeled paragraph below schema; column header unlabeled as MANDATORY |
| C-14 | PASS | VOCABULARY CONTRACT defines `??` and `--`; VIOLATION-1/2/3 enforce sentinel use over blanks |
| C-15 | PASS | Exact count sentence template; BANNED COUNT FORMS with integer-only enforcement |
| C-16 | PASS | Unified "Banned output forms" block explicitly lists and bans strings; Gate 5 checks both vs. NO CHANGE and null reasons |
| C-17 | PASS | VOCABULARY CONTRACT: `??` (open obligation) vs `--` (closed decision) with distinct semantics and violation conditions |
| C-18 | PASS | Phase 0 pre-signal defense register; Schema DR locked; non-generic defense arguments required |
| C-19 | PASS | BANNED COUNT FORMS: "a few", "several", "some", "multiple", "many" listed verbatim as gate failures |
| C-20 | PASS | Sequential: Gate 0→Phase 1, Gate 1→Phase 2 … Gate 5→Phase 6 — full named, numbered chain |
| C-21 | PASS | VOCABULARY CONTRACT: VIOLATION-1, VIOLATION-2, VIOLATION-3 enumerated — violations as explicitly defined as the tokens |
| C-22 | PASS | Schema DR with D-R-N row IDs; "Defense defeated: Row D-R-[N]" mandatory; "A named defense without a row number does not satisfy this column" |
| C-23 | PASS | Comprehensive verbatim-quoted lists: 7 strings in vs. NO CHANGE/inertia cells; 5 in null declaration reasons; 5 in delta count — all exact quoted form, categorized by output context |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 13 + 1.0 (2 partial) = 14/15 → 9.33
**V-05 total: 99.33**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 | 60 | 30 | 7.67 | **97.67** | YES |
| V-02 | 60 | 30 | 7.33 | **97.33** | YES |
| V-03 | 60 | 30 | 6.33 | **96.33** | YES |
| V-04 | 60 | 30 | 9.00 | **99.00** | YES |
| **V-05** | **60** | **30** | **9.33** | **99.33** | **YES** |

**Rank**: V-05 > V-04 > V-01 > V-02 > V-03

V-03 is the weakest because it targets C-23 alone — without the VOCABULARY CONTRACT (C-17/C-21) or the defense register (C-18/C-22), it leaves four aspirational criteria FAIL. V-01 and V-02 each trade off C-18 vs C-17 but both achieve near-identical totals. V-04 closes both gaps and reaches 99.0; V-05 adds C-23 to push to 99.33.

---

### Excellence Signals — V-05

Two patterns appear in V-05 PASS cells with no matching criterion in C-01–C-23:

**1. Preamble-level banned-forms registry with categorical separation**
The "Banned output forms" block appears before the pre-committed schemas — co-located with the VOCABULARY CONTRACT as a top-level standing reference, organized by output context category (vs. NO CHANGE column, null declaration reasons, delta count sentence). C-23 requires verbatim quoting and C-16 requires naming and banning, but neither criterion requires co-location of all banned forms at the preamble level or categorical organization by context. The preamble placement makes the list visible when schemas are being filled, not only when the instruction is encountered mid-phase.

**2. Template-embedded inline violation prevention in null declarations**
In V-05's null declaration templates, the banned forms appear inline at the point of use: `"ADDITIONS: none -- [specific reason, not 'no new signals' or 'nothing to add']"`. The output template itself signals the violation condition, rather than relying on a separate phase-level check. C-09 covers labeled null declarations and C-23 covers verbatim quoting, but no criterion captures the pattern of embedding violation-prevention strings inside the output template format itself — making the template self-constraining.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Preamble-level banned-forms registry with categorical separation — co-locating verbatim banned forms in a top-level reference block organized by output context category (column, null reasons, count sentence), making the list visible at schema-fill time rather than only at phase instruction", "Template-embedded inline violation prevention — banned forms embedded within null declaration output templates at point-of-use (e.g., 'none -- [reason, not \"no new signals\"]'), making the template itself self-constraining without relying on a separate phase-level check"]}
```
