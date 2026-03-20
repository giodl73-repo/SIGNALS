Written to `simulations/quest/variations/rhythm-track-variations-R2-2026-03-20.md`.

---

## Summary

5 variations for `rhythm-track` Round 2 targeting the v2 rubric (120 pts, 14 criteria):

| # | Axis | v2 Key Targets | Hypothesis |
|---|------|---------------|------------|
| **V-01** | Output format — column-enforced vocabulary | C-11 (reconciliation table), C-12 (IF-THEN derivation), C-13 (NOT ADDRESSED visible in column header), C-14 (P1=0 AMEND) | Allowed values in the column header enforce vocabulary at assignment time |
| **V-02** | Lifecycle emphasis — four locked checkpoints | C-11 (locked counts), C-12 (IF-THEN), C-13 (in block template), C-14 (explicit P1=0 branch) | "Locked" label removes the option to recount without contradiction |
| **V-03** | Phrasing register — vocabulary definitions block | C-13 (NOT ADDRESSED vs N/A defined upfront with critical distinction note), C-12 (derivation), C-14 | Defining vocabulary before use — model sees NOT ADDRESSED as the alternative to N/A at assignment time |
| **V-04** | Output format + lifecycle emphasis (combined) | All 4 new: C-11 (reconciliation table with locked column), C-12 (IF-THEN), C-13 (column rule), C-14 (P1=0 branch) | Widest structural defense — column enforcement + four checkpoints address all v2 aspirational criteria simultaneously |
| **V-05** | Role sequence + inertia framing (two-pass) | C-11/C-12 (final register + derivation), C-13 (in M-3 block template), C-14 (Challenge E probe + P1=0 branch) | Inertia framing makes the "assume track works" bias explicit; Skeptic adds Challenge D (modification without engagement) and Challenge E (clean track completeness) as new probes not in R1 |

**Key R2 delta over R1**: Every variation now encodes the NOT ADDRESSED three-way distinction (C-13) — the one criterion that only V-03 in R1 addressed. V-04 is designed to be the highest-scoring candidate. V-05 adds two new Skeptic probes targeting the v2 failure modes.
 PHASE 1 — MODULE SCAN

Read MODULE.md for {{topic}}.

| Check | Status |
|-------|--------|
| MODULE.md found and read | PASS / FAIL |
| At least one dependency edge documented | PASS / FAIL |
| Each edge has a named structural result | PASS / FAIL |

If any check is FAIL: state the reason and halt. Still produce a Phase 2 table — mark it empty with "No dependency edges found — see Phase 1 gate."

Extract from MODULE.md:
- Papers in dependency order: [list]
- Edges: [source -> target: what transfers per edge]

---

### PHASE 2 — DEPENDENCY MAP

One row per dependency edge. All cells required before proceeding.

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|
| D-01 | | | | |

Transfer type (one per row): **Definition** (term/formula used verbatim by all downstream papers) / **Structural** (mathematical framework constraining later formalism) / **Empirical** (number treated as a known quantity) / **Causal** (mechanism extended or applied)

**Row count recorded: [n].** This number locks Phase 3 coverage — Phase 3 must produce exactly [n] rows.

---

### PHASE 3 — VERIFICATION TABLE

One row per D-ID. Row count must equal Phase 2 row count. No row may be skipped.

| D-ID | Cited in target? [YES/NO/IMPLICITLY] | Correct form? [YES/NO/MODIFIED:desc] | Mod. justified? [YES/NO/NOT ADDRESSED/n/a] | Verdict [SATISFIED/PARTIAL/VIOLATED] | Gap (section + description) | Implicit note |
|------|--------------------------------------|--------------------------------------|--------------------------------------------|--------------------------------------|----------------------------|---------------|
| D-01 | | | | | | |

Column rules:
- **Cited in target?**: YES = source paper named at point of use; IMPLICITLY = result used, source not named; NO = absent
- **Correct form?**: YES = as defined in source; MODIFIED:[desc] = altered form, describe the change; NO = absent
- **Mod. justified?**: YES = paper explains the change; NO = modification undeclared; NOT ADDRESSED = paper neither confirms nor denies that the change is intentional or equivalent; n/a = only when Correct form? = YES (no modification occurred)
  — NOT ADDRESSED != n/a: use NOT ADDRESSED when modification occurred but the paper is silent about its justification
- **Verdict**: SATISFIED (cited + correct form) / PARTIAL (used but uncited, OR modified without justification) / VIOLATED (absent or contradicted)
- **Gap**: required for PARTIAL and VIOLATED; must name the section
- **Implicit note**: required when Cited = IMPLICITLY; one sentence: is implicit use sufficient for a reviewer or is an explicit citation needed?

**Completeness check: [n] rows filled. Must equal Phase 2 row count.**

---

### PHASE 4 — DEPENDENCY REGISTER

Derived directly from Phase 3 verdicts. No new judgments.

| D-ID | Verdict | Severity | Required change |
|------|---------|----------|----------------|
| D-01 | | | |

Severity: **P1** (structural break — target contradicts or ignores source result, breaking the causal chain) / **P2** (citation or form gap — used but uncited, or modified without disclosure) / **P3** (integration note — cited correctly but could be more explicitly integrated)

**Count reconciliation table (complete before writing Phase 5):**

| Severity | Row count | Carry to Phase 5 |
|----------|-----------|------------------|
| P1 | [n] | p1_violations = [n] |
| P2 | [n] | p2_gaps = [n] |
| P3 | [n] | p3_notes = [n] |

These counts are locked. Copy the values in the "Carry to Phase 5" column into Phase 5 and the artifact frontmatter exactly. Do not recount.

---

### PHASE 5 — TRACK HEALTH

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]    <- Phase 2 row count
P1 violations: [n]          <- reconciliation table P1 count (copied, not recounted)
P2 gaps: [n]                <- reconciliation table P2 count (copied, not recounted)
P3 notes: [n]               <- reconciliation table P3 count
Track integrity: [derive below]

Integrity derivation:
  Premise 1: P1 violations = [n]
  Premise 2: P2 gaps = [n]
  Rule: IF P1 > 0 THEN BROKEN
        ELSE IF P2 > 0 THEN PARTIAL
        ELSE SOUND
  Result: track integrity = [BROKEN / PARTIAL / SOUND]

Critical path to next submission:
  [D-IDs that must be resolved before the next paper can be submitted]
  [State "none" only when P1 = 0 and P2 = 0]
```

---

### PHASE 6 — AMEND

Three targeted fixes, highest severity first. Each fix must name: paper, section, exact change.

**Fix 1:**
[If P1 > 0]: In [paper], §[section]: [exact change — specific enough to act on without reading this report]
[If P1 = 0]: No P1 violations found. Fix 1 addresses highest-severity P2 gap.
In [paper], §[section]: [exact change]

**Fix 2:** In [paper], §[section]: [exact change]

**Fix 3:** In [paper], §[section]: [exact change]

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter required: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-02 — Lifecycle Emphasis: Four Write-Down Checkpoints

**Axis**: Lifecycle emphasis — four explicit "write-down checkpoints" at each phase boundary, each requiring the model to record a number before proceeding. Numbers are declared locked at the point of recording and may not be recounted in later phases.

**Hypothesis**: Count drift between Phase 4 and Phase 5 happens because the model recounts rather than carries. The "locked" label at each checkpoint removes the option to recount later without contradiction. Four independent locks (edge count, dependency count, P1/P2 locked, integrity locked) create a chain of carry-forward accountability that single reconciliation steps cannot fully provide.

---

You are running /rhythm-track for: {{topic}}

Verify the dependency chain across papers in a research track. This skill enforces four write-down checkpoints. At each checkpoint you record a number. That number is locked — it must appear unchanged in all later phases and in the artifact frontmatter.

---

### PHASE 1 — MODULE SCAN

Read MODULE.md for {{topic}}.

Extract:
1. Papers in dependency order
2. Dependency edges: which paper depends on which, and what structural result it depends on
3. Per-edge structural result: the specific formula, definition, quantity, or mechanism that must transfer

If MODULE.md contains no dependency annotations, output:
"TRACK INCOMPLETE — no dependency annotations found. Cannot proceed."

**=== CHECKPOINT 1: Edge count = [n] (locked) ===**

---

### PHASE 2 — DEPENDENCY MAP

One row per edge from Checkpoint 1. Row count must equal Checkpoint 1 value.

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Transfer types: Definition / Structural / Empirical / Causal

**=== CHECKPOINT 2: Dependency rows = [n] (locked) — Phase 3 must produce exactly this many verification blocks ===**

---

### PHASE 3 — VERIFICATION

For each D-ID from Checkpoint 2, produce one verification block. No block may be omitted. Total blocks must equal Checkpoint 2 value.

```
D-[NN]: [From] -> [To]: [what transfers]
  Cited in target?  YES / NO / IMPLICITLY
  Correct form?     YES / NO / MODIFIED: [describe alteration]
  Mod. justified?   YES (paper explains the change)
                  / NO (modification undeclared)
                  / NOT ADDRESSED (paper silent on whether change is intentional or equivalent)
                  / n/a (only when Correct form? = YES — no modification occurred)
  Verdict:          SATISFIED / PARTIAL / VIOLATED
  Gap:              [required for PARTIAL and VIOLATED — name section, describe deficiency]
  Implicit note:    [required when Cited = IMPLICITLY — sufficient for a reviewer, or explicit citation needed?]
```

Completeness: Blocks written = [n]. Must equal Checkpoint 2 value.

---

### PHASE 4 — DEPENDENCY REGISTER

Transfer verdicts and severity from Phase 3. No new judgments here.

| D-ID | Verdict | Severity | Required change |
|------|---------|----------|----------------|

Severity: P1 (structural break), P2 (citation/form gap), P3 (integration note)

**=== CHECKPOINT 3: Count now. Do not recount in Phase 5. ===**
- P1 count = [n] (locked)
- P2 count = [n] (locked)
- P3 count = [n] (locked)

These values travel unchanged to Phase 5 and the artifact frontmatter.

---

### PHASE 5 — TRACK HEALTH

Read locked values from Checkpoint 3. Do not recount.

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]    <- Checkpoint 2 value
P1 violations: [n]          <- Checkpoint 3 P1 (do not recount)
P2 gaps: [n]                <- Checkpoint 3 P2 (do not recount)
P3 notes: [n]               <- Checkpoint 3 P3

Integrity derivation (show work):
  P1 violations = [n]
  P2 gaps = [n]
  IF P1 > 0 THEN BROKEN
  ELSE IF P2 > 0 THEN PARTIAL
  ELSE SOUND
  -> track integrity = [BROKEN / PARTIAL / SOUND]

Critical path to next submission:
  D-IDs blocking submission: [list, or "none — track is ready"]
```

**=== CHECKPOINT 4: Track integrity = [BROKEN / PARTIAL / SOUND] (locked) ===**

---

### PHASE 6 — AMEND

Three targeted fixes, highest severity first. Each must name: (a) paper, (b) section, (c) exact change.

**Fix 1:**
[If P1 > 0]: In [paper], §[section]: [exact change — actionable without reading this report]
[If P1 = 0]: No P1 violations found — Fix 1 addresses highest-severity P2 gap.
In [paper], §[section]: [exact change]

**Fix 2:** In [paper], §[section]: [exact change]
**Fix 3:** In [paper], §[section]: [exact change]

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter required: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-03 — Phrasing Register: Vocabulary Definitions Block

**Axis**: Phrasing register — a formal vocabulary definitions block at the top specifies all allowed values for every field before any phase runs. The three-valued modification justification (YES / NO / NOT ADDRESSED) is defined with an explicit contrast against N/A. Phases run in formal technical register with pointer-back references to the vocabulary.

**Hypothesis**: When the vocabulary is defined before use, the model cannot default to N/A for ambiguous justification because NOT ADDRESSED is visible as the alternative at the time of assignment. Pointer-back references ("per vocabulary: NOT ADDRESSED") reinforce the distinction at the moment of application.

---

You are running /rhythm-track for: {{topic}}

Audit the dependency chain of a research track. All output must conform to the vocabulary definitions below. Vocabulary is defined once, before any phase, and governs every field throughout the artifact.

---

## VOCABULARY DEFINITIONS

**Transfer type** (Phase 2 column):
- `Definition` — a term, formula, or notation all later papers must use verbatim
- `Structural` — a mathematical framework that constrains how later papers set up their formalism
- `Empirical` — a measured or computed value that later papers treat as a known quantity
- `Causal` — a mechanism or explanation that later papers extend or apply

**Citation status** (Phase 3, field: Cited?):
- `YES` — source paper named at the point of use in the target paper
- `IMPLICITLY` — the result is used but the source paper is not named at the point of use
- `NO` — result is neither cited nor present

**Form status** (Phase 3, field: Correct form?):
- `YES` — transferred item appears exactly as defined in the source paper
- `MODIFIED:[description]` — appears in an altered form; the alteration must be described
- `NO` — item is absent

**Modification justification** (Phase 3, field: Mod. justified?):
Three values apply when Correct form? = MODIFIED:
- `YES` — the target paper explicitly states or justifies why the form was changed
- `NO` — the modification is present and undeclared by the paper
- `NOT ADDRESSED` — the paper neither confirms nor denies the change was intentional or equivalent; the justification question is not engaged

One value applies when Correct form? = YES or NO:
- `n/a` — modification did not occur (Correct form? = YES) or item is absent (Correct form? = NO)

**Critical distinction: NOT ADDRESSED is not N/A.** NOT ADDRESSED means a modification occurred and the paper is silent about its legitimacy. N/A means no modification occurred. Using N/A when NOT ADDRESSED is warranted collapses a third epistemic state (the paper neither denies nor justifies the change) into the no-modification case, which is false.

**Verdict** (Phase 3):
- `SATISFIED` — cited and used in correct form
- `PARTIAL` — used but uncited, OR modified without justification or disclosure
- `VIOLATED` — absent or contradicted

**Severity** (Phase 4):
- `P1` — structural break: the target paper contradicts or ignores a result the track's causal chain depends on
- `P2` — citation or form gap: result present but source uncited, or form modified without disclosure
- `P3` — integration note: cited correctly but could be integrated more explicitly

---

### PHASE 1 — MODULE SCAN

Read MODULE.md for {{topic}}.

Extract:
1. Ordered paper list
2. Dependency edges (source, target, what the target paper depends on)
3. Per-edge structural result: formula, definition, quantity, or mechanism that must appear in the target paper

If MODULE.md contains no dependency annotations: state this and halt. Produce an empty Phase 2 table with the note "No dependency edges found."

---

### PHASE 2 — DEPENDENCY MAP

One row per dependency edge. Assign transfer type per vocabulary.

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Row count recorded: [n] — Phase 3 must produce exactly [n] verification blocks.

---

### PHASE 3 — VERIFICATION

For each D-ID, read the target paper and produce one verification block. Blocks must total [Phase 2 row count]. No block may be skipped.

Apply vocabulary definitions at each field.

```
D-[NN]: [From] -> [To]: [what transfers]
  Cited?           [per vocabulary: YES / IMPLICITLY / NO]
  Correct form?    [per vocabulary: YES / MODIFIED:[desc] / NO]
  Mod. justified?  [per vocabulary: YES / NO / NOT ADDRESSED / n/a]
  Verdict:         [per vocabulary: SATISFIED / PARTIAL / VIOLATED]
  Gap:             [required for PARTIAL and VIOLATED — section name + deficiency description]
  Implicit note:   [required when Cited = IMPLICITLY — sufficient for a reviewer or explicit citation needed?]
```

---

### PHASE 4 — DEPENDENCY REGISTER

Summarize Phase 3 verdicts. Assign severity per vocabulary. No new judgments.

| D-ID | Verdict | Severity | Required change |
|------|---------|----------|----------------|

Count summary (derived from the table above; a reader may verify by counting rows):
- P1 rows: [n]
- P2 rows: [n]
- P3 rows: [n]

These counts carry to Phase 5 unchanged.

---

### PHASE 5 — TRACK HEALTH

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]    <- Phase 2 row count
P1 violations: [n]          <- Phase 4 P1 count
P2 gaps: [n]                <- Phase 4 P2 count
Track integrity: [derive below]

Derivation:
  Premises: P1 violations = [n]; P2 gaps = [n]
  IF P1 violations > 0 THEN track integrity = BROKEN
  ELSE IF P2 gaps > 0 THEN track integrity = PARTIAL
  ELSE track integrity = SOUND
  Result: [BROKEN / PARTIAL / SOUND]

Critical path to next submission:
  [D-IDs blocking submission; "none" only when P1 = 0 and P2 = 0]
```

---

### PHASE 6 — AMEND

Three targeted amendments in priority order. Each must identify: paper, section, and exact change.

**Amendment 1 (P1 priority):**
If P1 > 0: [paper], §[section] — [exact change — actionable without reading this report]
If P1 = 0: No P1 violations found. Amendment 1 targets the highest-severity P2 gap.
[paper], §[section] — [exact change]

**Amendment 2:** [paper], §[section] — [exact change]
**Amendment 3:** [paper], §[section] — [exact change]

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter required: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-04 — Combined: All-Table + Write-Down Protocol + Full v2 Aspirational Coverage

**Axes**: Output format (all-table, column-level vocabulary enforcement) + Lifecycle emphasis (four structural checkpoints with locked counts).

**Hypothesis**: Column-level vocabulary enforcement (C-13: NOT ADDRESSED visible as an option) and structural count locking (C-11: reconciliation table, C-12: IF-THEN derivation) are complementary defenses that address different failure modes. The table enforces vocabulary at the moment of assignment. The locked checkpoints prevent count drift between phases. Together they cover all four new v2 aspirational criteria (C-11 through C-14) simultaneously.

---

You are running /rhythm-track for: {{topic}}

Audit the dependency chain across papers in a research track. Read MODULE.md and the individual papers. Every phase outputs structured tables. Four locked checkpoints carry counts across phase boundaries without recounting.

---

### PHASE 1 — MODULE SCAN

Read MODULE.md for {{topic}}.

**Pre-flight gate:**

| Check | Status |
|-------|--------|
| MODULE.md found and read | PASS / FAIL |
| At least one dependency edge documented | PASS / FAIL |
| Each edge has a named structural result | PASS / FAIL |

If any FAIL: state the reason and halt. Produce an empty Phase 2 table (do not omit it) with the note "Gate failed — see Phase 1."

Extract:
- Papers in dependency order
- Dependency edges (source, target, what transfers, structural result)

---

### PHASE 2 — DEPENDENCY MAP

One row per dependency edge. Complete all cells before proceeding to Phase 3.

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Transfer types: **Definition** (term/formula used verbatim) / **Structural** (framework constraining formalism) / **Empirical** (number treated as known) / **Causal** (mechanism extended or applied)

**=== CHECKPOINT 1: Dependency rows = [n] (locked). Phase 3 must fill exactly [n] rows. ===**

---

### PHASE 3 — VERIFICATION TABLE

One row per D-ID. Row count must equal Checkpoint 1 value. Every cell required.

| D-ID | Cited? [YES/NO/IMPLICITLY] | Correct form? [YES/NO/MODIFIED:desc] | Mod. justified? [YES/NO/NOT ADDRESSED/n/a] | Verdict | Gap (section + description) | Implicit note |
|------|---------------------------|--------------------------------------|--------------------------------------------|---------|----------------------------|---------------|

Column rules:
- **Cited?**: YES = source named at point of use; IMPLICITLY = result used, source not named; NO = absent
- **Correct form?**: YES = as defined in source; MODIFIED:[desc] = altered form, describe; NO = absent
- **Mod. justified?**: YES = paper justifies the change; NO = change undeclared; NOT ADDRESSED = modification present, paper silent on its justification (neither confirms nor denies); n/a = Correct form? = YES (no modification)
  — NOT ADDRESSED != n/a: NOT ADDRESSED means modification occurred, justification unengaged; n/a means no modification
- **Verdict**: SATISFIED (cited + correct) / PARTIAL (used but uncited, OR modified without justification) / VIOLATED (absent or contradicted)
- **Gap**: required for PARTIAL and VIOLATED — section name + exact deficiency
- **Implicit note**: required when Cited = IMPLICITLY — sufficient for reviewer, or explicit citation needed?

**=== CHECKPOINT 2: Rows filled = [n]. Must equal Checkpoint 1 value. ===**

---

### PHASE 4 — DEPENDENCY REGISTER

Derived directly from Phase 3. No new judgments.

| D-ID | Verdict | Severity | Required change |
|------|---------|----------|----------------|

Severity: P1 (structural break) / P2 (citation/form gap) / P3 (integration note)

**Count reconciliation table (complete before writing Phase 5):**

| Severity | Count from table above | Locked value for Phase 5 |
|----------|------------------------|--------------------------|
| P1 | [n] | p1_violations = [n] |
| P2 | [n] | p2_gaps = [n] |
| P3 | [n] | p3_notes = [n] |

**=== CHECKPOINT 3: P1 = [n], P2 = [n], P3 = [n] (locked). Copy "Locked value" column to Phase 5 and frontmatter. Do not recount. ===**

---

### PHASE 5 — TRACK HEALTH

Read locked values from Checkpoint 3. Do not derive new counts.

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]    <- Checkpoint 1 value
P1 violations: [n]          <- Checkpoint 3 P1 locked value
P2 gaps: [n]                <- Checkpoint 3 P2 locked value
P3 notes: [n]               <- Checkpoint 3 P3 locked value
Track integrity: [derive below]

Integrity derivation:
  Premise: P1 violations = [n]
  Premise: P2 gaps = [n]
  Rule: IF P1 > 0 THEN BROKEN
        ELSE IF P2 > 0 THEN PARTIAL
        ELSE SOUND
  Result: track integrity = [BROKEN / PARTIAL / SOUND]

Critical path to next submission:
  D-IDs that must be resolved: [list, or "none — track is ready"]
```

**=== CHECKPOINT 4: Track integrity = [BROKEN / PARTIAL / SOUND] (locked for frontmatter). ===**

---

### PHASE 6 — AMEND

Three targeted fixes in severity order. Each fix must state: paper, section, exact change.

**Fix 1:**
[If P1 > 0]: In [paper], §[section]: [exact change — actionable without reading this report]
[If P1 = 0]: No P1 violations found. Fix 1 addresses highest-severity P2 gap.
In [paper], §[section]: [exact change]

**Fix 2:** In [paper], §[section]: [exact change]
**Fix 3:** In [paper], §[section]: [exact change]

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter required: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-05 — Combined: Two-Pass (Mapper + Skeptic) + Inertia Framing

**Axes**: Role sequence (two-pass adversarial: Mapper establishes baseline, Skeptic challenges it) + Inertia framing (the skill opens by naming the default assumption the audit is designed to challenge).

**Hypothesis**: A single-pass audit anchors to the author's framing and tends to confirm dependencies as satisfied unless evidence of failure is obvious. The inertia frame makes this bias explicit: "The default is that this track works. Find the evidence that it does not." The Skeptic pass then operationalizes this frame with three named probes (silent divergence, citation-without-use, terminology drift) plus two new v2-targeted probes (modification without engagement, clean-track completeness). The Skeptic also enforces NOT ADDRESSED for modification justification and handles the P1=0 AMEND edge case explicitly.

---

You are running /rhythm-track for: {{topic}}

Execute a two-pass dependency audit. The track's default state is assumed sound — papers cite each other, structural results transfer correctly. This audit exists to test that assumption.

**The Mapper pass** establishes the dependency structure and records initial verdicts.
**The Skeptic pass** challenges every SATISFIED and PARTIAL verdict. Its job is to find the case where the track is not as sound as it appears.

---

### PASS 1 — MAPPER

#### M-1: Module Scan

Read MODULE.md for {{topic}}.

Extract:
- Ordered paper list
- Dependency edges (source, target, what transfers)
- Per-edge structural result: specific formula, definition, quantity, or mechanism

Prerequisite: If MODULE.md contains no dependency annotations, output "AUDIT BLOCKED — no dependency structure documented." and halt.

#### M-2: Dependency Map

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Transfer types: Definition / Structural / Empirical / Causal

Row count: [n]

#### M-3: Initial Verification

For each D-ID, read the target paper and produce a verification block:

```
D-[NN]: [From] -> [To]: [what transfers]
  Cited?           YES / NO / IMPLICITLY
  Correct form?    YES / NO / MODIFIED: [describe alteration]
  Mod. justified?  YES / NO / NOT ADDRESSED / n/a
    (NOT ADDRESSED: paper neither confirms nor denies justification for the change)
    (n/a: only when Correct form? = YES)
  Initial verdict: SATISFIED / PARTIAL / VIOLATED
  Evidence:        [quote or section reference from target paper]
  Implicit note:   [if Cited = IMPLICITLY: sufficient for a reviewer or explicit citation needed?]
```

#### M-4: Mapper Register

| D-ID | Initial verdict | Severity | Notes |
|------|----------------|----------|-------|

---

### PASS 2 — SKEPTIC

The Skeptic reads the Mapper's output. The Skeptic's operating assumption: **the track has at least one dependency that is not as sound as the Mapper reported.** The Skeptic's job is to find it, or to confirm it is not there after an active search.

Apply five challenge probes to every D-ID. Record a finding or "none found" for each.

**Challenge A — Silent divergence**: When the target paper's formalism is evaluated, does it produce results numerically or structurally inconsistent with the source paper's result — even if it appears to cite correctly?

**Challenge B — Citation without use**: Is the source paper cited in related work or the introduction but absent from the sections where the structural result is actually applied?

**Challenge C — Terminology drift**: Does the target paper use different variable names, notation, or terminology for the same concept? If so, is the equivalence stated explicitly?

**Challenge D — Modification without engagement**: If the Mapper recorded Correct form? = MODIFIED and Mod. justified? = NOT ADDRESSED — is the modification severe enough to affect the paper's conclusions? If so, this should escalate to P1.

**Challenge E — Clean track completeness**: If the Mapper found no P1 violations, does the AMEND section still address the highest-severity P2 gap? (A clean track with no actionable fixes is incomplete.)

For each D-ID:

```
D-[NN] — Skeptic review:
  Challenge A (silent divergence):        [finding or "none found"]
  Challenge B (citation without use):     [finding or "none found"]
  Challenge C (terminology drift):        [finding or "none found"]
  Challenge D (modification engagement):  [finding or "none found" or "n/a — not MODIFIED"]
  Challenge E (clean track completeness): [applies to AMEND — addressed at end]
  Revised verdict:   SATISFIED / PARTIAL / VIOLATED
  Revision rationale: [why changed, or "unchanged — no new findings"]
```

---

### FINAL REGISTER

Use Skeptic-revised verdicts. Where Mapper and Skeptic disagree, the Skeptic verdict stands.

| D-ID | Mapper verdict | Skeptic verdict | Final verdict | Severity | Required change |
|------|---------------|-----------------|---------------|----------|----------------|

Severity: P1 (structural break) / P2 (citation/form gap) / P3 (integration note)

**Count reconciliation:**
- P1 count: [n] (locked — derived from Final verdict P1 rows above)
- P2 count: [n] (locked — derived from Final verdict P2 rows above)
- Skeptic escalations (Mapper SATISFIED → Skeptic PARTIAL/VIOLATED): [list D-IDs or "none"]

---

### TRACK HEALTH

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]    <- M-2 row count
P1 violations: [n]          <- Final Register P1 count (locked)
P2 gaps: [n]                <- Final Register P2 count (locked)
Track integrity: [derive below]

Integrity derivation:
  Premise: P1 violations = [n]
  Premise: P2 gaps = [n]
  IF P1 > 0 THEN BROKEN
  ELSE IF P2 > 0 THEN PARTIAL
  ELSE SOUND
  -> track integrity = [BROKEN / PARTIAL / SOUND]

Skeptic escalations: [D-IDs that changed verdict from Mapper to Skeptic, or "none"]

Critical path to next submission:
  [D-IDs blocking submission, or "none — track is ready"]
```

---

### AMEND

Three targeted fixes in severity order. Each must state: (1) paper, (2) section, (3) exact change.

**Fix 1:**
[If P1 > 0]: [paper], §[section] — [exact change, actionable without reading this report]
[If P1 = 0]: No P1 violations found. Fix 1 addresses highest-severity P2 gap (Challenge E resolved).
[paper], §[section] — [exact change]

**Fix 2:** [paper], §[section] — [exact change]
**Fix 3:** [paper], §[section] — [exact change]

If a fix requires coordinated changes across multiple papers (e.g., a P1 violation where both source and target must change), list all affected locations.

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter required: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN
