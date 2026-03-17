## Round 12 Scoring — org:committee (v12 Rubric, 140 pts)

---

### Rubric Criteria Reference

**Essential** (C-01–C-05, 12 pts each = 60 pts): committee type declared, participants from charter, role-lens speaking, three required sections, at least one challenge.
**Recommended** (C-06–C-08, 10 pts each = 30 pts): agenda specificity, owned action items, dissents with resolution paths.
**Aspirational** (C-09–C-33, 2 pts each = 50 pts): 25 criteria; C-32 and C-33 are the new additions this round.

---

### V-01 — Lifecycle Emphasis — C-32 ENFORCE Only

**Axis**: Minimal diff from R11 V-05 skeleton; every `PHASE-N-COMMIT:` upgraded from `[locked]` to `[locked] | ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE`.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | Committee Type declared before simulation content |
| C-02 | PASS | LOAD charter from `.craft/roles/`; fallback disclosed |
| C-03 | PASS | Charter-documented orientation enforced per participant |
| C-04 | PASS | DECISIONS / ACTION ITEMS / DISSENTING OPINIONS all in skeleton |
| C-05 | PASS | VALIDATE at least one CONDITION or BLOCK; reopen Phase 2 if all-APPROVE |
| C-06 | PASS | Fill rules enforce specific agenda item throughout Phase 3 prose |
| C-07 | PASS | `[Owner Role] — [specific action] — [deadline]` with all-three-parts enforcement |
| C-08 | PASS | Dissents cite INERTIA-FINDING-* label + resolution path with named authority |
| C-09 | PASS | C-16 gate confirms non-obvious finding before proceeding |
| C-10 | PASS | OUTCOME derived from TALLY; re-entry Owner + Trigger if not APPROVED |
| C-11 | PASS | Tier 1 → Tier 2 → Tier 3 order enforced in skeleton and fill |
| C-12 | PASS | Investigation (INERTIA-FINDING-A through D) precedes participant voices |
| C-13 | PASS | `STANCE:` standalone line before prose; prose may not soften |
| C-14 | PASS | TALLY: standalone line after last voice block before Phase 5 |
| C-15 | PASS | `STANCE:` as structural labeled declaration |
| C-16 | PASS | GATE-1 with YES/NO + Basis field; intra-phase retry |
| C-17 | PASS | Tier 3 REQUIRE: fill CITE: grounded in named INERTIA-FINDING label |
| C-18 | PASS | All-APPROVE → reopen Phase 2 and reassign |
| C-19 | PASS | `RESPONDS-TO:` required for Tier 3; addresses named Tier 1/2 concern |
| C-20 | PASS | `CITE: INERTIA-FINDING-[A/B/C/D]` as labeled structural field |
| C-21 | PASS | `RESPONDS-TO: "[named concern]"` with quoted attribution, generic fails |
| C-22 | PASS | Gate NO → rewrite loop within Phase 1 |
| C-23 | PASS | Owner + Trigger both required when verdict not APPROVED |
| C-24 | PASS | Sequential attempt labels INVESTIGATION-ATTEMPT-N |
| C-25 | PASS | Named SORT-CHECK gate with Test: and Result: fields |
| C-26 | PASS | Phases 0–5 with labeled headers; skeleton + fill enforces sequence |
| C-27 | PASS | INERTIA-FINDING-A through D as named labels on each finding |
| C-28 | PASS | Full skeleton pre-declared in STEP 1 before any content fills |
| C-29 | PASS | Gate loops are intra-phase; Phase 2 unconditional once gate YES |
| C-30 | PASS | Fill rules: LOAD, WRITE, ENFORCE, REQUIRE, PRINT, VALIDATE, CONFIRM — verb-first |
| C-31 | PASS | PHASE-N-COMMIT: before every next-phase header |
| C-32 | **PASS** | Every PHASE-N-COMMIT: carries `\| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` — active blocking assertion present |
| C-33 | **FAIL** | PHASE-1-COMMIT says "INERTIA-FINDING-A through D active as citation anchors" — range phrase, not individual label enumeration with content anchors; no manifest structure |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 48/50 (C-33 fail = −2)
**V-01 Score: 138/140**

---

### V-02 — Output Format — Flat Command Sequence, No Skeleton

**Axis**: No skeleton STEP 1. Flat per-phase command blocks with COMMIT Phase N sections carrying ENFORCE assertions.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01–C-05 | PASS | All essential criteria satisfied in flat command format |
| C-06–C-08 | PASS | All recommended criteria satisfied |
| C-09–C-27 | PASS | All aspirational criteria through C-27 satisfied in flat structure |
| C-28 | **PARTIAL** | No pre-declared skeleton; structural labels appear inline as phase instructions are executed — explicit partial-pass per rubric definition |
| C-29 | PASS | Gate loop runs within Phase 1 block; IF NO → LABEL INVESTIGATION-ATTEMPT-2; Phase 2 unconditional |
| C-30 | **PARTIAL** | Mostly verb-first (LOAD, WRITE, PRINT, ENFORCE, CONFIRM) but `FOR EACH participant:` control structure and nested conditional blocks fall outside the named micro-instruction verbs |
| C-31 | PASS | PHASE-N-COMMIT: block present at end of each phase |
| C-32 | **PASS** | Each COMMIT Phase N section includes `ENFORCE: terminal position stated in Phase N — no Phase N content may follow this commit` — active blocking assertion within the commit section |
| C-33 | **FAIL** | PHASE-1-COMMIT: `INERTIA-FINDING-A through D active` — no manifest enumeration |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 46/50 (C-28 partial −1, C-30 partial −1, C-33 fail −2)
**V-02 Score: 136/140**

---

### V-03 — Phrasing Register — Conversational with Compact ENFORCE

**Axis**: Conversational register throughout; PHASE-N-COMMIT: blocks carry compact blocking assertions inline.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01–C-05 | PASS | All essential criteria met in conversational format |
| C-06–C-08 | PASS | All recommended criteria met |
| C-09–C-27 | PASS | C-09 through C-27 all satisfied (INERTIA-FINDING labels, SORT-CHECK gate, GATE-1 loop, STANCE:, CITE:, RESPONDS-TO: all explicitly named) |
| C-28 | **PARTIAL** | No skeleton print step; conversational format describes structure but never pre-declares it as a fillable container — partial pass per rubric |
| C-29 | PASS | "Do all of this within Phase 1 before moving forward" — gate loop explicitly scoped intra-phase |
| C-30 | **PARTIAL** | Descriptive prose dominates ("Here is how to run this simulation", "This is the most important phase", "Then close this phase") — not uniformly verb-first imperative; PRINT/WRITE/REQUIRE appear but framing prose is non-imperative |
| C-31 | PASS | Each phase closes with a quoted PHASE-N-COMMIT: line |
| C-32 | **PASS** | Every PHASE-N-COMMIT: block includes `ENFORCE: no Phase N content after this point` — compact but active blocking assertion within the marker |
| C-33 | **FAIL** | PHASE-1-COMMIT includes "INERTIA-FINDING-A through D active" but no manifest enumeration with content anchors per label |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 46/50 (C-28 partial −1, C-30 partial −1, C-33 fail −2)
**V-03 Score: 136/140**

---

### V-04 — Combined: Lifecycle + Inertia Framing — C-33 Manifest + C-32 ENFORCE

**Axis**: R11 V-05 skeleton + imperative fill rules + C-32 ENFORCE assertions + C-33 citation-anchor manifest in PHASE-1-COMMIT with per-label one-phrase anchors.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01–C-05 | PASS | All essential criteria satisfied |
| C-06–C-08 | PASS | All recommended criteria satisfied |
| C-09–C-31 | PASS | All prior aspirational criteria satisfied — R11 V-05 foundation preserved intact |
| C-28 | PASS | Full skeleton pre-declared in STEP 1 including manifest structure in PHASE-1-COMMIT slot |
| C-30 | PASS | Fill rules uniformly verb-first: LOAD, ASSIGN, ENFORCE, PRINT, VALIDATE, CONFIRM, WRITE, REQUIRE |
| C-31 | PASS | PHASE-N-COMMIT: markers at each phase boundary |
| C-32 | **PASS** | Every PHASE-N-COMMIT: in skeleton carries `\| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE`; every fill rule PRINT instruction repeats the assertion |
| C-33 | **PASS** | PHASE-1-COMMIT in skeleton: explicit multi-line manifest block enumerating INERTIA-FINDING-A through D as separate labeled fields with `[one-phrase anchor]` slots. Fill rule PRINT instruction reproduces the manifest with guidance per label. NOTE line explicitly states citation validity is restricted to manifest-listed labels |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 50/50 (all 25 criteria pass)
**V-04 Score: 140/140**

---

### V-05 — Full Synthesis — All Axes, Manifest with Downstream VALIDATE

**Axis**: Complete synthesis with STEP 1 skeleton + imperative fill rules + C-32 ENFORCE on all commits + C-33 manifest with restrictive validity language + downstream VALIDATE in Phase 3 and Phase 5 cross-referencing the manifest.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01–C-05 | PASS | All essential criteria satisfied |
| C-06–C-08 | PASS | All recommended criteria satisfied |
| C-09–C-31 | PASS | All prior aspirational criteria satisfied |
| C-28 | PASS | Full skeleton with manifest structure in PHASE-1-COMMIT slot pre-declared in STEP 1 |
| C-30 | PASS | Verb-first micro-instructions throughout; VALIDATE steps add WRITE/CONFIRM/VALIDATE verbs in Phase 5 with artifact-level precision |
| C-31 | PASS | PHASE-N-COMMIT: before every next-phase header; commit markers in both skeleton and fill |
| C-32 | **PASS** | Skeleton PHASE-N-COMMIT: blocks use `\| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` as a dedicated line in each commit block (multi-line commit structure makes assertion unmissable) |
| C-33 | **PASS** | Skeleton manifest: "Citation-anchor manifest — findings locked; downstream CITE: and RESPONDS-TO: valid **only** against labels listed here:" with four named fields. Fill rule PRINT instruction includes descriptive per-label hints driving accurate content anchoring. Phase 3 VALIDATE instruction cross-references manifest at execution time. Phase 5 DISSENTING OPINIONS fill rule includes `VALIDATE: cited INERTIA-FINDING-* labels in dissent text match labels enumerated in the Phase 1 citation-anchor manifest` — citation chain closed end-to-end |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 50/50 (all 25 criteria pass)
**V-05 Score: 140/140**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Rank |
|-----------|-----------|-------------|-------------|-------|------|
| V-04 | 60 | 30 | 50 | **140/140** | 1 (tie) |
| V-05 | 60 | 30 | 50 | **140/140** | 1 (tie) |
| V-01 | 60 | 30 | 48 | **138/140** | 3 |
| V-02 | 60 | 30 | 46 | **136/140** | 4 (tie) |
| V-03 | 60 | 30 | 46 | **136/140** | 4 (tie) |

---

### Excellence Signals — V-04 and V-05

**Pattern 1: Manifest uses restrictive validity language, not declarative**
V-04/V-05 write "downstream CITE: and RESPONDS-TO: **valid only against** labels listed here" rather than "findings locked" or "A through D active." This converts the manifest from an informational record into a citation constraint — the manifest defines the validity boundary, not just the completion state. This is the structural upgrade that makes C-33 meaningful beyond C-31's lock declaration.

**Pattern 2: Downstream VALIDATE instructions close the citation chain at execution time**
V-05 adds VALIDATE instructions in Phase 3 ("the cited label must appear in the Phase 1 citation-anchor manifest; an unlisted label fails C-33 downstream validation") and Phase 5 ("VALIDATE: cited INERTIA-FINDING-* labels in dissent text match labels enumerated in the Phase 1 citation-anchor manifest"). This means citation correctness is checked at each usage site, not just asserted at the manifest declaration — the chain runs Phase 1 lock → Phase 3 CITE check → Phase 5 dissent check.

**Pattern 3: Per-label content hints in the fill rule PRINT instruction**
V-05's manifest fill instruction annotates each finding slot with what content to summarize: "one-phrase locked anchor — **the specific workflow or artifact named in this finding**", "**the integration surface named in this finding**", etc. These per-label type hints drive accurate anchor content, preventing generic summaries from satisfying the form while missing the substance. The manifest becomes a precision instrument, not just a checklist.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Citation-anchor manifest uses restrictive validity language ('valid only against labels listed here') converting it from an informational record to an active citation constraint", "Downstream VALIDATE instructions in Phase 3 and Phase 5 cross-reference the manifest at execution time, closing the citation chain end-to-end rather than only at declaration", "Per-label content-type hints in the manifest fill rule PRINT instruction (e.g., 'the integration surface named in this finding') drive accurate anchor summarization rather than generic placeholder text"]}
```
