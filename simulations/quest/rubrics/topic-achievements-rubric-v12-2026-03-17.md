Now I have the full picture. The rubric in the prompt is for a different skill than `corps-achievements` (it uses PHASE BARRIERS / CLOSURE GATES / MANIFESTS). The excellence signals and open signals are self-contained in the prompt. Let me write the complete v12 rubric.

---

```markdown
# Quest Score Rubric — corps-achievements
**Version**: v12 (2026-03-17)

## What Changed in v12

**2 new aspirational criteria** extracted from Round 11 excellence signals (V-05):

- **C-33 (Per-section C-31 compliance declaration in SECTION INVENTORY)** — from V-05's
  SECTION INVENTORY pattern. C-30 requires a SECTION INVENTORY listing each C-27+ section by
  name; C-31 requires that section's checks be expressed as per-phase named pairs. The
  SECTION INVENTORY satisfying C-30 declares *that* each section exists; it does not declare
  *how many* [C-31] pairs each section contains. Without a pair count in the INVENTORY, a
  checker verifying C-31 compliance must read every section body individually, accumulate pair
  counts manually, and determine whether each section satisfies C-31 by structural
  interpretation rather than by an explicit claim. V-05's INVENTORY lists each C-27+ section
  with its declared [C-31] pair count per entry — e.g., "C-28 SECTION [C-30]: 3 pairs [C-31]"
  — converting per-section C-31 compliance into a string-match-verifiable fact. A checker
  locates the INVENTORY by name, reads the pair count for each section from the INVENTORY
  declaration, and flags any entry with zero pairs or no `[C-31]` annotation without
  reading section bodies. C-33 tests whether the SECTION INVENTORY, for each C-27+ criterion
  section it indexes, declares the [C-31] pair count of that section via a labeled annotation.
  **C-33 requires C-30 as a precondition** (no SECTION INVENTORY = no INVENTORY to annotate)
  **and C-31 as a precondition** (no per-phase pairs in sections = nothing to count). Does not
  require C-32; the C-32 section is one section among others in the INVENTORY, subject to the
  same pair-count declaration requirement. Closes the gap that C-30 alone leaves open: C-30
  confirms dedicated sections exist with granular checks; C-33 confirms the INVENTORY itself
  carries verifiable C-31 compliance evidence for each, enabling single-point audit without
  section-body traversal.

- **C-34 (Inline manifest digest in forward-binding assertion)** — from V-05's CLOSURE GATE
  self-application pattern. C-32 requires the CLOSURE GATE to include an explicit forward-
  binding constraint assertion: "Phase [N+1] inputs constrained to PHASE N MANIFEST" (or
  equivalent). This assertion is referential — it names the manifest but does not quantify it.
  A future reinterpretation that produces N+K artifacts can technically "reference" the Phase N
  manifest while expanding scope beyond it without directly contradicting any stated number.
  V-05's pattern embeds an inline digest alongside the constraint claim: "Phase [N+1] inputs
  constrained to PHASE N MANIFEST: [N] artifacts." The numerical claim converts the forward-
  binding assertion from a referential boundary (scope loosely anchored to a named document)
  into a falsifiable one (scope anchored to a specific count). Any Phase N+1 execution that
  produces or consumes a set of size ≠ N directly contradicts an explicit in-gate claim; no
  interpretation is required to detect the violation. C-34 tests whether the CLOSURE GATE's
  forward-binding assertion includes an inline manifest digest — a specific artifact count,
  contributor count, or equivalent quantified dimension — embedded within or immediately
  adjacent to the forward-binding constraint sentence. The digest must be a concrete value
  drawn from the Phase N manifest, not a variable reference. **C-34 requires C-28 as a
  precondition** (no manifest = no digest to inline) **and C-32 as a precondition** (no
  forward-binding assertion = no assertion to embed the digest in). Closes the gap that C-32
  alone does not close: C-32 asserts the constraint exists; C-34 tests whether the constraint
  is numerically grounded such that scope violations are directly contradictory rather than
  merely inconsistent.

**Scoring formula updated**: `aspirational_pass / 26 * 10` (was `/24`). Max composite
remains 100.

---

**Prior version notes (carried forward for traceability)**

*v11 added C-30, C-31, C-32 from Round 10 excellence signals (V-05).* C-30 tests whether the
STRUCTURAL AUDIT GATE contains a dedicated named section for each aspirational criterion
introduced at C-27 or later, with ≥2 individual checks per section. C-31 tests whether audit
checks for each such criterion are stated and verified independently per phase rather than as
single global assertions. C-32 tests whether the CLOSURE GATE, after verifying the manifest,
includes an explicit forward-binding constraint assertion tying Phase N+1 scope to the Phase N
manifest; requires C-28 as a precondition. Scoring formula updated in v11: `aspirational_pass
/ 24 * 10` (was `/21`).

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

### Essential (C-01–C-05) — 60 points

Each criterion worth 12 points. All five must pass for full essential score.

| ID | Criterion |
|----|-----------|
| C-01 | Glob scan gate present |
| C-02 | Topic coverage gate with every-topic check |
| C-03 | Team milestones table, ≥3 named rows |
| C-04 | Contributor leaderboard section |
| C-05 | Next actions: ≥3, namespace+topic explicit, unlock named |

### Recommended (C-06–C-08) — 30 points

Each criterion worth 10 points.

| ID | Criterion |
|----|-----------|
| C-06 | Achievement definitions present (First Signal, Signal Depth, Full Sweep, Solo Pioneer, Team Topic) |
| C-07 | Achievements grouped into Earned / Locked as named categories |
| C-08 | Sprint/date framing present ({{date}} in section headers) |

### Aspirational (C-09–C-34) — 10 points

Formula: `aspirational_pass / 26 * 10`. PARTIAL = 0.5 weight.

#### C-09–C-25: Baseline aspirational (carried forward from v8/v9)

| ID | Criterion |
|----|-----------|
| C-09 | "1-away" dedicated table with exact gap and count (4-column Almost There table) |
| C-10 | Cross-topic/contributor named insight, distinct from stagnation |
| C-11 | At least one inline pre-write self-test gate |
| C-12 | Anti-inertia format: `[Action] → Unlocks → Breaks [Pattern]` |
| C-13 | Insight as titled artifact `**TEAM INSIGHT — [name]:**` |
| C-14 | Stagnation patterns from named registry, label syntax enforced |
| C-15 | Gate failure names specific instance (topic/contributor/row) |
| C-16 | Weighted formula `Signals×1 + Topics×3 + Milestones×5` |
| C-17 | Semantic pattern labels (SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL, ORPHAN_TOPIC) |
| C-18 | 1-away table: 4 columns (topic, achievement, gap, exact action) |
| C-19 | Worked example calculation inline for Rank-1 contributor |
| C-20 | Gate labels carry criterion ID references `[C-XX]` |
| C-21 | Formula gate instructs table correction on mismatch |
| C-22 | Insight gate applies single-topic derivability test (per-topic YES/NO) |
| C-23 | Multi-condition gates use numbered sub-steps |
| C-24 | Cross-phase gate explicitly asks whether Phase 2 findings alter Phase 1 output. Requires C-22. |
| C-25 | Multi-criterion gate labels enumerate all covered IDs. Requires C-23. |

#### C-26: Added in v9

**C-26 — Lifecycle Phase Barrier Language.** Each phase boundary carries an explicit
declarative seal before the next phase's context is introduced. A barrier that merely says
"do not begin Phase N+1" operates as an instruction (model may ignore it); a seal that says
"PHASE N IS NOW SEALED" operates as a declarative fact the model must contradict to violate.
C-26 tests whether each phase boundary line is a declarative seal statement, not a conditional
instruction. Independent of C-22–C-25.

#### C-27–C-29: Added in v10

**C-27 — Structural barrier omission resistance via pre-printed elements.** Phase barrier
markers are embedded as pre-printed elements in the output template rather than as follow-on
instructions. Omitting a pre-printed marker requires the model to actively skip a named
template element; omitting an instructed marker only requires failing to add one. C-27 tests
whether each phase boundary marker is pre-printed in the template such that a checker can
verify its presence by string match without inferring compliance from instruction-following.
Structurally independent of C-26: pre-printed dividers without STOP instructions are valid.
C-27 does not prevent retroactive reframing via reinterpretation; that gap is addressed by
C-28.

**C-28 — Phase output-set manifest declared before closure seal.** At each phase boundary,
the prompt requires the model to enumerate and record the phase output set before writing the
closure seal. Manifest must include at minimum: artifact count PLUS at least one additional
dimension (contributor count, namespace count, or equivalent). A closure gate that seals
without recording counts fails C-28. Structurally independent of C-26 and C-27. Addresses
retroactive scope expansion via reinterpretation (not omission). C-26 + C-28 together: barrier
seals scope AND manifest records what scope was at sealing.

**C-29 — Dual-layer barrier redundancy.** Each phase boundary carries two distinct,
independently-implemented barrier mechanisms such that both must fail simultaneously for
barrier omission to occur. **C-29 requires C-26 and C-27 as preconditions.** Dual-layer
redundancy eliminates omission risk but does not add output-set enumeration; retroactive
reframing via reinterpretation remains possible unless C-28 is also satisfied.

#### C-30–C-32: Added in v11

**C-30 — Per-criterion dedicated audit sections with granular individual checks.** The
STRUCTURAL AUDIT GATE contains a dedicated named section for each aspirational criterion
introduced at C-27 or later. Each section has ≥2 granular individual checks — not a single
pass/fail assertion. A checker verifies compliance by string-matching the section name and
confirming each sub-check independently without scorer interpretation. C-30 tests whether
every such criterion has a dedicated named section in the STRUCTURAL AUDIT GATE with ≥2
individual checks. Structurally independent of C-31: granular sections can use global (non-
per-phase) checks (C-30 without C-31); per-phase granularity can exist within bundled sections
(C-31 without C-30).

**C-31 — Per-phase audit granularity — each check applied independently per phase.** Audit
checks for each aspirational criterion (C-27 and above) are stated and verified independently
per phase rather than as single global assertions. A global check ("MANIFEST block present")
cannot detect phase-specific failures — compliant Phase 1 gate does not prove Phase 2
compliance. C-31 tests whether each check within a C-27+ criterion's audit section is
expressed as a named per-phase pair, verifiable per-phase by string match on the pair label.
Requires multi-phase output structure. Structurally independent of C-30 (see above). Does
not address forward-binding of manifest scope — that gap is addressed by C-32.

**C-32 — Forward-binding manifest constraint assertion in CLOSURE GATE.** The CLOSURE GATE,
after verifying the Phase N manifest (C-28), includes an explicit forward-binding constraint
assertion tying Phase N+1 scope to the Phase N manifest. Without forward-binding language,
the manifest is on-record but its constraining role is implicit; retroactive scope expansion
via reinterpretation does not contradict an unlabeled list. With it: "Phase [N+1] inputs
constrained to PHASE N MANIFEST." Any Phase N+1 scope expansion must directly contradict an
explicit claim. C-32 tests whether the CLOSURE GATE contains such an assertion after the
manifest verification step. **C-32 requires C-28 as a precondition.** Addresses the
retroactive reframing gap that C-28 alone does not close: manifest recorded but not forward-
bound.

#### C-33–C-34: Added in v12

**C-33 — Per-section C-31 compliance declaration in SECTION INVENTORY.** The SECTION
INVENTORY in the STRUCTURAL AUDIT GATE lists each C-27+ criterion section with its declared
[C-31] pair count, enabling per-section C-31 compliance to be verified from the INVENTORY
alone without reading section bodies. A SECTION INVENTORY satisfying C-30 declares that each
section exists; C-33 requires that it also declare how many [C-31] pairs each section
contains — e.g., "C-28 SECTION [C-30]: 3 pairs [C-31]". A checker verifies C-31 compliance
by locating the INVENTORY, reading each section's declared pair count, and flagging entries
with zero pairs or missing `[C-31]` annotation by string match. **C-33 requires C-30**
(no SECTION INVENTORY = no inventory to annotate) **and C-31** (no per-phase pairs in
sections = nothing to count). Does not require C-32; the C-32 section is one section among
others in the INVENTORY, subject to the same pair-count declaration requirement. Closes
the gap that C-30 alone leaves open: C-30 confirms dedicated sections exist with granular
checks; C-33 confirms the INVENTORY carries verifiable C-31 compliance evidence per section,
enabling single-point audit without section-body traversal.

**C-34 — Inline manifest digest in forward-binding assertion.** The CLOSURE GATE's forward-
binding assertion (required by C-32) includes an inline manifest digest — a specific artifact
count, contributor count, or equivalent quantified dimension drawn from the Phase N manifest —
embedded within or immediately adjacent to the forward-binding constraint sentence. A C-32
assertion is referential: "Phase [N+1] inputs constrained to PHASE N MANIFEST." A C-34
assertion is falsifiable: "Phase [N+1] inputs constrained to PHASE N MANIFEST: [N] artifacts."
A Phase N+1 execution producing a set of size ≠ N directly contradicts an explicit in-gate
claim; no interpretation is required to detect the violation. C-34 tests whether the forward-
binding assertion contains a concrete quantified value drawn from the manifest, not a variable
reference or relative description. **C-34 requires C-28** (no manifest = no digest to inline)
**and C-32** (no forward-binding assertion = no assertion to embed the digest in). Closes
the gap that C-32 alone does not close: C-32 asserts the constraint exists; C-34 tests whether
the constraint is numerically grounded such that scope violations are directly contradictory
rather than merely inconsistent with an implicit boundary.

---

## Dependency Map

```
C-29 ← C-26, C-27
C-32 ← C-28
C-33 ← C-30, C-31
C-34 ← C-28, C-32
C-24 ← C-22
C-25 ← C-23
```

Precondition failure propagates: if C-28 FAIL then C-32 FAIL and C-34 FAIL regardless
of assertion content. If C-30 FAIL or C-31 FAIL then C-33 FAIL.

---

## Scoring Formula

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/26 * 10)
```

PARTIAL counts as 0.5. Max composite = 100.

Aspirational pass thresholds by version:

| Version | Aspirational Max | Formula |
|---------|-----------------|---------|
| v8 | 18 | /18 * 10 |
| v9 | 18 | /18 * 10 |
| v10 | 21 | /21 * 10 |
| v11 | 24 | /24 * 10 |
| **v12** | **26** | **/26 * 10** |

---

## Scoring Decision Guide

**C-33 PASS requires**: SECTION INVENTORY present (C-30); each C-27+ section entry in the
INVENTORY carries both `[C-30]` tag and an explicit pair count with `[C-31]` tag. String-
match verifiable: grep for INVENTORY block, verify each section line contains a numeric pair
count and `[C-31]`. Does not infer compliance from section content.

**C-33 FAIL**: SECTION INVENTORY present but entries list sections without pair counts
(C-30 satisfied, C-33 not). Or INVENTORY absent (C-30 FAIL implies C-33 FAIL). Or pair
counts present but not labeled `[C-31]` — structural presence ≠ declared compliance.

**C-34 PASS requires**: C-32 assertion present; that assertion or its immediately adjacent
line contains a concrete count or equivalent quantified value preceded or followed by a
manifest reference. "Phase 2 inputs constrained to PHASE 1 MANIFEST: 7 artifacts" satisfies.
"Phase 2 inputs constrained to PHASE 1 MANIFEST: {{count}} artifacts" does not satisfy
(variable reference, not a concrete value drawn from the executed manifest).

**C-34 FAIL**: C-32 assertion present but purely referential, no inline quantity. Or C-32
absent (C-34 FAIL by precondition). Or quantity present but not inline (e.g., embedded in
a separate prose paragraph after the closure seal).
```
