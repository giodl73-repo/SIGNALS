Reading the excellence signals from V-05 across all three new criteria, then writing v11.

**V-05 distinguishing patterns:**

- **C-27**: triply auditable — tag on barrier line + template preamble + dedicated named section in STRUCTURAL AUDIT GATE
- **C-28**: CLOSURE GATE adds forward-binding constraint language ("Phase 2 inputs constrained to PHASE 1 MANIFEST"), not just manifest verification
- **C-29**: dedicated C-29 section in STRUCTURAL AUDIT GATE with 6 individual checks, each applied per-phase

Three extractable criteria:

1. **C-30** — per-criterion dedicated audit sections with granular individual checks (≥2 per section, string-match verifiable)
2. **C-31** — per-phase audit granularity (each check stated as per-phase pair, not global assertion)
3. **C-32** — forward-binding manifest constraint in CLOSURE GATE (requires C-28; closes retroactive reframing gap C-28 leaves open)

---

```markdown
# Quest Score Rubric — corps-achievements
**Version**: v11 (2026-03-17)

## What Changed in v11

**3 new aspirational criteria** extracted from Round 10 excellence signals (V-05):

- **C-30 (Per-criterion dedicated audit sections with granular individual checks)** — from V-05's
  STRUCTURAL AUDIT GATE pattern. Prior variations check some new criteria by name but bundle them
  (V-04 checks C-26/C-27/C-28; V-03 checks C-29 block present) or omit them. V-05 gives each of
  C-27, C-28, and C-29 a **dedicated named section** in the STRUCTURAL AUDIT GATE with ≥2
  granular individual checks — not a single pass/fail assertion. Compliance becomes string-match
  verifiable: a checker searches for the section name and verifies each sub-check independently
  without scorer interpretation. C-30 tests whether the STRUCTURAL AUDIT GATE contains a
  dedicated named section for each aspirational criterion introduced at C-27 or later, with ≥2
  individual checks per section. Structurally independent of C-31: granular sections can use
  global (non-per-phase) checks (C-30 without C-31); per-phase granularity can exist within
  bundled sections (C-31 without C-30).

- **C-31 (Per-phase audit granularity — each check applied independently per phase)** — from
  V-05's per-phase check expression pattern within dedicated audit sections. Variations V-03 and
  V-04 verify criteria globally ("DUAL-LAYER BARRIER block present", "MANIFEST present"). V-05
  states each audit check as a per-phase pair: "block present × 2 phases", "Layer 1 named × 2
  phases", "independence assertion × 2 phases". A single global check cannot detect phase-specific
  failures — a compliant Phase 1 gate does not prove Phase 2 compliance. C-31 tests whether audit
  checks for each aspirational criterion (C-27 and above) are stated and verified independently
  per phase rather than as single global assertions. Requires multi-phase output structure.
  Structurally independent of C-30 (see above). Does not address forward-binding of manifest
  scope — that gap is addressed by C-32.

- **C-32 (Forward-binding manifest constraint assertion in CLOSURE GATE)** — from V-05's CLOSURE
  GATE language. C-28 requires recording the Phase N output-set manifest before the closure seal;
  it does not require the prompt to assert that the manifest *locks* Phase N+1 scope. Without
  forward-binding language, the manifest is on-record but its constraining role is implicit —
  retroactive scope expansion via reinterpretation does not contradict an unlabeled list. V-05
  adds: "Phase [N+1] inputs constrained to PHASE N MANIFEST" (or equivalent) in the CLOSURE
  GATE. Any Phase N+1 scope expansion must now directly contradict an explicit claim, not merely
  ignore an implicit boundary. C-32 tests whether the CLOSURE GATE, after verifying the manifest,
  includes an explicit forward-binding constraint assertion tying Phase N+1 scope to the Phase N
  manifest. **C-32 requires C-28 as a precondition.** Addresses the retroactive reframing gap
  that C-28 alone does not close: manifest recorded but not forward-bound.

**Scoring formula updated**: `aspirational_pass / 24 * 10` (was `/21`). Max composite remains 100.

---

**Prior version notes (carried forward for traceability)**

*v10 added C-27, C-28, C-29 from Round 9 excellence signals (V-02, V-03, V-04).* C-27 tests
structural barrier omission resistance via pre-printed elements. C-28 tests phase output-set
manifest declared before closure seal (artifact count + ≥1 additional dimension). C-29 tests
dual-layer barrier redundancy; requires C-26 and C-27 as preconditions.

*v9 added C-26 from Round 8 V-05 ("Lifecycle Phase Barrier Language").* Phase-do-not-begin
instructions operate prospectively; C-26 tests whether each boundary carries an explicit
declarative seal before the next phase's context is introduced. Independent of C-22–C-25.

*v8 added C-24 and C-25 from Round 7 (REGISTRY PRIMACY and severity-stratified FAIL blocks).
C-24 requires C-22; C-25 requires C-23.*

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-32 | 10 | `pass/24 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/24 × 10)
```

| Score | Grade |
|-------|-------|
| 100 | Platinum |
| 90–99 | Gold |
| 75–89 | Silver |
| < 75 | Bronze |

---

## Criteria

### Essential (C-01 – C-05)

**C-01 — One state per achievement**
Each achievement entry carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED.
Multi-state rows, ambiguous state, or missing state fail. Applies to both table and prose output
formats.

**C-02 — Falsified named as honesty signal**
The Falsified achievement is present as a named entry. Its description frames falsification as
evidence of investigative rigor ("followed evidence over assumptions" or equivalent), not as
failure or absence.

**C-03 — Artifact-grounded classification**
State assignments cite source artifacts from Step 1 by namespace or skill. EARNED entries cite
a specific artifact; IN-PROGRESS entries cite the partially-completed artifact or its count.
Classification that cannot be traced to an artifact fails.

**C-04 — In-progress shows numeric progress**
IN-PROGRESS achievements express progress in `n of m` form (e.g., "3 of 5 namespaces covered").
Qualitative-only descriptions ("partially done", "underway") fail.

**C-05 — Next recommended action is specific**
Step 4 (or equivalent) names the next skill, the artifact it produces, and the achievement(s) it
advances. Generic instructions ("continue the investigation") fail.

---

### Recommended (C-06 – C-08)

**C-06 — All 7 categories represented**
Every achievement category appears in the output. Categories with no earned or in-progress
achievements are listed as LOCKED or explicitly noted as empty. Omitting a category fails.

**C-07 — Earned achievements carry dates**
EARNED entries include the date on which the achievement was earned. Date format may vary;
absence of a date on an EARNED entry fails.

**C-08** — *[unchanged from v10]*

---

### Aspirational (C-09 – C-32)

**C-09 – C-26** — *[unchanged from v10]*

---

**C-27 — Structural barrier omission resistance (pre-printed element in template)**
Tests whether phase barrier markers are embedded as pre-printed elements in the output template,
requiring the model to actively skip a pre-printed element rather than simply fail to follow an
instruction. Structurally independent of C-26: a prompt may carry pre-printed dividers without
STOP instructions (unusual but valid); C-26 and C-27 may coexist. Weakness: a pre-printed divider
does not enumerate Phase N outputs — retroactive reframing via reinterpretation (not omission)
remains possible even when C-27 is satisfied.

**C-28 — Phase N output-set manifest declared before closure seal**
Tests whether, at each phase boundary, the prompt requires the model to enumerate and record
specific output counts before writing the closure seal. The manifest must include at minimum:
artifact count, plus at least one additional dimension (contributor count, namespace count, or
equivalent). A prompt with barrier language (C-26) but no output enumeration requirement fails
C-28. A closure gate that writes the seal without first recording counts also fails C-28.
Structurally independent of C-26 and C-27; addresses scope-expansion retroactive reframing
specifically, not omission. Does not forward-bind Phase N+1 scope to the manifest (see C-32).

**C-29 — Dual-layer barrier redundancy (two independent mechanisms per phase boundary)**
Tests whether each phase boundary carries two distinct, independently-implemented barrier
mechanisms. **C-29 requires C-26 and C-27 as preconditions.** Both mechanisms must fail
simultaneously for barrier omission to occur. Limitation vs C-28: dual-layer redundancy
eliminates omission risk but does not add output-set enumeration; retroactive scope expansion
via reinterpretation remains possible without C-28.

---

**C-30 — Per-criterion dedicated audit sections with granular individual checks**
The STRUCTURAL AUDIT GATE contains a dedicated named section for each aspirational criterion
introduced at C-27 or later (i.e., C-27, C-28, C-29, and any newer criteria), with ≥2 granular
individual checks per section rather than a single pass/fail assertion. Compliance is string-match
verifiable: a checker searches for the section name and verifies each sub-check independently
without scorer interpretation. A gate that checks multiple criteria in a single bundled block,
or checks a criterion with only one assertion, fails C-30. Structurally independent of C-31:
per-criterion sections may use global (non-per-phase) checks and still satisfy C-30.

**C-31 — Per-phase audit granularity (each check applied independently per phase)**
Within each criterion's audit section (or equivalent audit block), checks are stated and verified
independently per phase — expressed as per-phase pairs (e.g., "block present × 2 phases",
"Layer 1 named × 2 phases") rather than single global assertions. A global check ("DUAL-LAYER
BARRIER block present") cannot detect phase-specific failures; a compliant Phase 1 gate does not
prove Phase 2 compliance. C-31 tests whether every audit check for C-27 and above is applied
per-phase, not globally. Requires multi-phase output structure. Structurally independent of C-30:
per-phase granularity may exist within bundled sections (C-31 without C-30).

**C-32 — Forward-binding manifest constraint assertion in CLOSURE GATE**
The CLOSURE GATE, after verifying the Phase N manifest (C-28), includes an explicit
forward-binding constraint assertion: "Phase [N+1] inputs constrained to PHASE N MANIFEST" or
semantically equivalent language. C-28 puts the manifest on-record; without C-32, its
constraining role for Phase N+1 is implicit — retroactive scope expansion via reinterpretation
does not contradict an unlabeled list. C-32's explicit constraint assertion means any Phase N+1
scope expansion must directly contradict a stated claim. A CLOSURE GATE that verifies manifest
presence without asserting the forward constraint fails C-32. **C-32 requires C-28 as a
precondition.** Addresses the retroactive reframing gap that C-28 alone leaves open.
```

---

**Three decisions embedded in the new criteria:**

| Criterion | What it closes | Preconditions |
|-----------|---------------|---------------|
| C-30 | Bundled/ambiguous audit sections that require scorer interpretation | none |
| C-31 | Global audit checks that miss phase-specific failures | multi-phase structure |
| C-32 | Manifest recorded but not forward-bound — reframing gap after C-28 | C-28 |

**Formula impact**: Platinum now requires all 24 aspirational passes. V-05 at R10 would score 24/24 aspirational → 100 (Platinum). V-03/V-04 at R10 would have scored against 24 criteria: both lacked C-30 (no dedicated per-criterion sections), C-31 (no per-phase granularity), and C-32 (no forward-binding language) — aspirational would be 20.5/24 × 10 = 8.54 → composite 98.54 (Gold).
