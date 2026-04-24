## org:committee Round 13 — Scoring

### Rubric v13 Recap

**35 criteria**: 5 essential (12 pts each = 60), 3 recommended (10 pts each = 30), 27 aspirational (2 pts each = 54). Composite max = **144**.

New in v13: **C-34** (PHASE-1-COMMIT manifest entries carry content-anchor suffixes per label) and **C-35** (PHASE-3-COMMIT enumerates per-participant stance tokens as a vote-anchor manifest).

---

## V-01 — Lifecycle Emphasis

**Axis**: Minimal diff from R12 V-05. Two surgical additions: (1) C-34 VALIDATE rule in PHASE-1 fill rules; (2) PHASE-3-COMMIT skeleton + fill rule upgraded from Boolean to per-participant stance manifest.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | VALIDATE: Committee Type declared before any content; PHASE-0-COMMIT prints it. |
| C-02 | PASS | LOAD from `.roles/`; fallback to Signal defaults with disclosure. |
| C-03 | PASS | Fill rules require charter-documented orientation per participant. |
| C-04 | PASS | Skeleton includes DECISIONS / ACTION ITEMS / DISSENTING OPINIONS in Phase 5. |
| C-05 | PASS | VALIDATE: at least one CONDITION or BLOCK; all-APPROVE triggers Phase 2 reopen. |
| C-06 | PASS | Agenda Item slot; fill rules reference "specific agenda item." |
| C-07 | PASS | `[Owner Role] — [specific action] — [deadline]`; all three parts required. |
| C-08 | PASS | Dissent fill rules require concrete trigger + named authority per resolution path. |
| C-09 | PASS | INERTIA-FINDING-D targets non-obvious cost "author would say I missed that." |
| C-10 | PASS | Owner + Trigger slots in DECISIONS Re-entry path; VALIDATE both present. |
| C-11 | PASS | Tier 1 → Tier 2 → Tier 3 enforced; ENFORCE clause in fill rules. |
| C-12 | PASS | Phase 1 investigation precedes all participant voices by structural phase order. |
| C-13 | PASS | `STANCE: [BLOCK/CONDITION/APPROVE]` as standalone line before prose; VALIDATE no softening. |
| C-14 | PASS | PHASE 4 TALLY as standalone line before PHASE 5 MINUTES. |
| C-15 | PASS | PRINT: STANCE: as explicit labeled declaration; structural, not embedded in prose. |
| C-16 | PASS | GATE-1 with Question / Answer / Basis; YES/NO before proceeding. |
| C-17 | PASS | REQUIRE (Tier 3): CITE: must reference named INERTIA-FINDING-* label. |
| C-18 | PASS | VALIDATE: all-APPROVE triggers Phase 2 reopen + tier reassignment. |
| C-19 | PASS | RESPONDS-TO: required for Tier 3 before endorsement prose. |
| C-20 | PASS | CITE: as explicit labeled subfield; named label is first element after CITE:. |
| C-21 | PASS | RESPONDS-TO: REQUIRE with ACCEPTABLE (named concern) / FAILS (generic attribution). |
| C-22 | PASS | IF GATE-N NO → INCREMENT N → rewrite → re-gate; loop until YES. |
| C-23 | PASS | Owner (named role) + Trigger (concrete event); VALIDATE both present. |
| C-24 | PASS | REQUIRE sequential label increments; label must appear in output. |
| C-25 | PASS | SORT-CHECK with Test: + Result: as discrete labeled gate. |
| C-26 | PASS | PHASE 0–5 headers; phase-labeled sequential structure throughout. |
| C-27 | PASS | INERTIA-FINDING-A through D as named labels; parenthesized letters fail. |
| C-28 | PASS | STEP 1: PRINT THIS SKELETON pre-declared before any content generation. |
| C-29 | PASS | `[GATE-1 NO → fill INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]` — intra-phase. |
| C-30 | PASS | LOAD / ENFORCE / PRINT / VALIDATE / WRITE / REQUIRE — verb-first throughout. |
| C-31 | PASS | PHASE-N-COMMIT: [locked] terminal block at the end of each phase. |
| C-32 | PASS | `| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE.` per commit. |
| C-33 | PASS | Citation-anchor manifest enumerates INERTIA-FINDING-A through D individually. |
| C-34 | PASS | VALIDATE rule added: "each manifest entry carries a content anchor...a bare-label entry fails C-34." Skeleton shows `[one-phrase locked anchor]` per entry. |
| C-35 | PASS | PHASE-3-COMMIT skeleton shows `[___] ___` per participant; fill rule: `PRINT: Stance manifest (one entry per participant...format: [Role Name] STANCE-TOKEN]`; VALIDATE: TALLY derived from manifest, re-parsing prose not permitted. |

**Score: 144/144** — All 35 criteria pass.

---

## V-02 — Output Format (Flat Command Sequence)

**Axis**: No skeleton pre-declaration (no STEP 1/STEP 2 split). Tests whether C-34 and C-35 are satisfiable outside the skeleton architecture.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 through C-05 | PASS | All essential structural requirements present in flat command form. |
| C-06 through C-08 | PASS | All recommended format and behavior criteria preserved. |
| C-09 through C-27 | PASS | All pre-v8 and v8–v12 aspirational criteria satisfied: INERTIA-FINDING labels, SORT-CHECK gate, intra-phase loops, PHASE-N-COMMIT blocks with ENFORCE assertions. |
| C-28 | **FAIL** | Intentionally omitted — flat format has no STEP 1 skeleton pre-declaration. No pre-printed empty container before content fills. |
| C-29 through C-33 | PASS | Intra-phase gate loops, imperative phrasing (LOAD/PRINT/ENFORCE/WRITE), commit markers with ENFORCE assertions, citation-anchor manifest with keyword anchors per entry. |
| C-34 | PASS | `VALIDATE: each manifest entry carries a content anchor readable without Phase 1 prose; bare label with no following text fails C-34.` PRINT instruction uses `[keyword or title identifying this finding's claim]` per entry. |
| C-35 | PASS | PRINT: PHASE-3-COMMIT with `[Role Name] STANCE-TOKEN` per participant; `VALIDATE: Phase 4 TALLY derived from this manifest by counting tokens; manifest is authoritative; re-parsing Phase 3 prose for the tally is not permitted.` |

**Score: 142/144** — C-28 FAIL (−2). All others pass.

---

## V-03 — Phrasing Register (Conversational)

**Axis**: Conversational/descriptive framing throughout. Structural labels (STANCE:, CITE:, RESPONDS-TO:, PHASE-N-COMMIT:) mandatory; fill rules written in descriptive rather than verb-first imperative.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 through C-05 | PASS | Essential criteria met — committee type, participants, role lens, sections, challenge. |
| C-06 through C-08 | PASS | Recommended criteria met — specificity, owned action items, dissent resolution paths. |
| C-09 through C-27 | PASS | INERTIA-FINDING labels, self-check gate, SORT-CHECK, intra-phase loops, per-phase commit blocks, citation manifest with anchors. |
| C-28 | **FAIL** | No skeleton pre-declaration step. V-03 begins directly with Phase 0 narrative instructions. |
| C-29 | PASS | "Keep going, incrementing the attempt number each time, until you can honestly answer YES. Phase 2 always follows once you've answered YES." — intra-phase scope preserved. |
| C-30 | **FAIL** | Fill rules use descriptive imperative: "Start by identifying...", "Then look up...", "After writing all four, check yourself." Not verb-first micro-instructions. Some commit blocks use ENFORCE but general register fails C-30. |
| C-31 through C-33 | PASS | PHASE-N-COMMIT: blocks with ENFORCE assertions; citation-anchor manifest with identifying keyword/title per entry. |
| C-34 | PASS | Manifest section: "filling in one-phrase content anchors per finding — a keyword or title that identifies each finding's claim without requiring a reader to go back and read the full Phase 1 text." Note: "a bare label with nothing after it fails." **PASS** (descriptive register can still enforce the content requirement) |
| C-35 | PASS | "End Phase 3 with this commit block — it must list every participant's role name and their locked stance token individually" with skeleton showing `[Role Name] BLOCK/CONDITION/APPROVE` per participant; "The tally in Phase 4 is computed from this manifest, not from re-reading the voices above." |

**Score: 140/144** — C-28 FAIL (−2), C-30 FAIL (−2). All others pass.

---

## V-04 — Combined: Lifecycle + Inertia Framing

**Axis**: Skeleton architecture preserved; INERTIA RECORD and STANCE MANIFEST elevated as named first-class parallel artifacts; explicit C-34 VALIDATE with ACCEPTABLE/FAILS worked examples; PHASE-3-COMMIT gains per-participant vote-anchor manifest.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 through C-05 | PASS | All essential criteria preserved. |
| C-06 through C-08 | PASS | All recommended criteria preserved. |
| C-09 through C-27 | PASS | All pre-v13 aspirational criteria satisfied. Phase 1 labeled "INERTIA RECORD" throughout; skeleton pre-declared with both manifests in STEP 1. |
| C-28 | PASS | STEP 1 prints complete skeleton including both manifest structures before any content. Instruction: "Print every section header, every field label, every ___ placeholder, and every PHASE-N-COMMIT: block including both artifact manifests." |
| C-29 through C-32 | PASS | Intra-phase loops; imperative fill rules (LOAD/ENFORCE/PRINT/VALIDATE/CONFIRM/IF); commit markers with ENFORCE terminal assertions. |
| C-33 | PASS | INERTIA RECORD citation-anchor manifest enumerates INERTIA-FINDING-A through D individually with keyword/title per entry. |
| C-34 | PASS | Explicit VALIDATE with worked examples: `ACCEPTABLE: INERTIA-FINDING-A: workflow-disruption`, `ACCEPTABLE: INERTIA-FINDING-B: API-contract-breakage`, `FAILS: INERTIA-FINDING-A: with no following anchor text`, `FAILS: comma-separated bare labels with no per-entry anchor`. Strongest C-34 VALIDATE alongside V-05. |
| C-35 | PASS | PHASE-3-COMMIT skeleton: `STANCE MANIFEST (one entry per participant — derived from locked STANCE: declarations above): [___] ___`. Fill rules: per-participant `[Role Name] BLOCK/CONDITION/APPROVE`; VALIDATE: every Phase 0 participant has exactly one entry; Phase 4 TALLY counts derived from this manifest; divergence from manifest is a C-35 violation. |

**Score: 144/144** — All 35 criteria pass.

---

## V-05 — Full Synthesis

**Axis**: All axes combined — skeleton, imperative fill rules, ENFORCE assertions, inertia framing, C-34 VALIDATE with multi-example ACCEPTABLE/FAILS, C-35 per-participant stance manifest with derivation prohibition.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 through C-05 | PASS | All essential criteria met. |
| C-06 through C-08 | PASS | All recommended criteria met. |
| C-09 through C-27 | PASS | Full R12 V-05 foundation preserved; all pre-v13 aspirational criteria pass. |
| C-28 | PASS | STEP 1 pre-prints complete skeleton including both manifest structures. |
| C-29 through C-32 | PASS | Intra-phase gate loops; verb-first micro-instructions (LOAD/ENFORCE/PRINT/VALIDATE/WRITE/REQUIRE/CONFIRM/COUNT); PHASE-N-COMMIT with ENFORCE terminal assertions. |
| C-33 | PASS | Citation-anchor manifest with `[keyword or title that identifies this finding without reading Phase 1 prose]` per label. |
| C-34 | PASS | Most complete VALIDATE: `ACCEPTABLE: INERTIA-FINDING-A: workflow-disruption / API-contract-breakage / ops-team / rollback-habit`; `FAILS: bare label with no anchor`; `FAILS: comma-separated bare labels with no per-entry anchor` (adds the comma-list failure case that V-04 omits). Derivable-without-prose test articulated: "A manifest entry that cannot be verified against a downstream CITE: label without reading Phase 1 prose fails C-34 regardless of C-33 compliance." |
| C-35 | PASS | PHASE-3-COMMIT skeleton: `[___] ___ [repeat per participant — format: [Role Name] BLOCK / CONDITION / APPROVE]`. Fill rules: per-participant enumeration; VALIDATE: every Phase 0 participant appears exactly once; VALIDATE: "re-parsing Phase 3 voice prose for the tally is not permitted" — active prohibition. PHASE-4-COMMIT confirms: "TALLY derived from Phase 3 stance manifest." |

**Score: 144/144** — All 35 criteria pass.

---

## Rankings

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| 1 | V-05 Full Synthesis | 144/144 | — |
| 1 | V-04 Lifecycle + Inertia | 144/144 | — |
| 1 | V-01 Lifecycle Emphasis | 144/144 | — |
| 4 | V-02 Output Format | 142/144 | C-28 |
| 5 | V-03 Phrasing Register | 140/144 | C-28, C-30 |

**Tie-break (all at 144):** V-05 > V-04 > V-01

- V-05 carries the most complete C-34 enforcement: adds the comma-list failure case and the articulated "cannot be verified without reading Phase 1 prose" test that V-04 omits. It also combines every prior axis at maximum depth.
- V-04 introduces the named artifact architecture (INERTIA RECORD / STANCE MANIFEST) — a structural clarity upgrade not in V-01 or V-05.
- V-01 is the minimal-diff approach: surgical additions only, highest signal-to-noise ratio for the specific C-34/C-35 gaps.

---

## Excellence Signals from Top-Scoring Variations

**1. VALIDATE-with-examples pattern (V-04, V-05)** — A VALIDATE rule that carries worked ACCEPTABLE/FAILS pairs converts a constraint declaration into a self-specifying format test. V-01 passes C-34 with a VALIDATE rule alone; V-04/V-05 add `ACCEPTABLE: INERTIA-FINDING-A: workflow-disruption` and `FAILS: INERTIA-FINDING-A: — bare label with no anchor`. This makes the enforcement unambiguous without referencing the rubric. The upgrade pattern: rule-only → rule-plus-examples, same as C-21 applied to C-19.

**2. Named artifact elevation (V-04)** — Renaming the PHASE-1-COMMIT manifest "INERTIA RECORD" and the PHASE-3-COMMIT manifest "STANCE MANIFEST" creates parallel named artifacts. Both manifests are now citable by artifact name in downstream fill rules (`CITE: from INERTIA RECORD`, `TALLY derived from STANCE MANIFEST`) rather than by positional convention ("the Phase 1 manifest"). Named artifacts make accidental omission structurally harder: a CITE: that can't name its source artifact fails a named test.

**3. Manifest-is-authoritative prohibition (V-01, V-04, V-05)** — The VALIDATE rule "re-parsing Phase 3 prose for the tally is not permitted" adds an active prohibition alongside the positive derivation rule. Previous rounds established that PHASE-3-COMMIT must enumerate stances; R13 adds the prohibition against bypassing the manifest. The upgrade pattern: "must derive from X" → "must derive from X; re-reading prose is not permitted" — parallel to how C-32 added "NO PHASE N CONTENT MAY FOLLOW" alongside C-31's commit marker.

---

```json
{"top_score": 144, "all_essential_pass": true, "new_patterns": ["VALIDATE-with-examples: adding ACCEPTABLE/FAILS worked pairs to a VALIDATE rule converts it from a constraint declaration into a self-specifying format test, removing ambiguity about what constitutes a passing entry", "named-artifact elevation: treating phase manifests as named first-class artifacts (INERTIA RECORD, STANCE MANIFEST) makes cross-phase citation traceable by artifact name rather than positional convention", "manifest-is-authoritative prohibition: pairing the positive derivation rule with an explicit prohibition against re-parsing phase prose converts manifest authority from an implied structural property into an active enforcement rule"]}
```
