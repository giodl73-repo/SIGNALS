Written to `simulations/quest/golden/topic-status-golden-2026-03-14.md`.

**What made this golden (5 key patterns):**

1. **Preamble-first invariants** — All structural constraints declared as a contiguous block before execution, not buried in phase bodies
2. **ADVERSARY CHAIN with defeat forecast** — Each P-N-ADVERSARY entry carries a nested `DEFEAT CONDITION:` (C-51), closing the preamble→execution→STOP triad
3. **Dual-axis STOP predicates** — File-absent and topic-absent are structurally distinct stop conditions with separate trigger descriptions
4. **[LAYER N] labels tied to phase vocabulary** — `STRUCTURAL`, `SEMANTIC`, `EXECUTION` — not positional decorations but bindings to consequence vocabulary
5. **OUTPUT DECLARATION CHAIN independence made explicit** — PHASE 2 and PHASE 3 each declare output independently; no silent undeclared output

The score in the frontmatter is 300 (v17 basis); under v18 V-01 projects to 310 once C-50 and C-51 are formally scored.
 inertia toward empty-glob assumption (default when PHASE 1 is
    skipped: coverage computed from zero disk signals without verification);
    DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
    case handled explicitly before PHASE 2 commitment assertion executes.
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
    DEFEAT CONDITION: all planned signals individually asserted with explicit
    VERIFIED or UNVERIFIED state; no signal exits without assertion on record.
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification);
    DEFEAT CONDITION: percent computed with consistency guard applied;
    UNVERIFIED-non-empty and percent-100% contradiction halted before verdict.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]
COMMIT RISK BY NAMESPACE

  | Namespace | Planned | Found | Pct |
  |-----------|---------|-------|-----|
  | scout     | 0       | 0     | --  |
  | draft     | 0       | 0     | --  |
  | review    | 0       | 0     | --  |
  | flow      | 0       | 0     | --  |
  | trace     | 0       | 0     | --  |
  | prove     | 0       | 0     | --  |
  | listen    | 0       | 0     | --  |
  | program   | 0       | 0     | --  |
  | topic     | 0       | 0     | --  |

EXPOSURE SUMMARY
  Coverage: {found}/{planned} ({pct}%)

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]
```

---

## What Made It Golden

**1. Preamble-first structural invariants block**
All structural constraints are declared as a single contiguous block before any
execution or output template. The preamble is not part of the output -- it is a
meta-layer that governs the execution. This prevents constraint burial inside
phase bodies and makes the invariants reviewable in isolation.

**2. ADVERSARY CHAIN with three-part defeat forecast at each entry**
Each P-N-ADVERSARY entry carries its own nested `DEFEAT CONDITION:` sub-component
(C-51 pattern). The preamble does not just name adversaries -- it forecasts the
observable defeat property. This creates a closed triad: preamble forecast ->
execution-body assertion -> STOP gate verification.

**3. Dual-axis STOP predicates with structurally distinct messages**
File-absent and topic-absent are explicitly distinguished as separate stop
conditions with separate trigger descriptions. Prior versions collapsed them or
left the distinction implicit. The separation prevents the PHASE 2 gate from
silently swallowing topic-absent as a file error.

**4. [LAYER N] labels tied to phase vocabulary, not position**
Layer labels carry the name of the phase they enforce: `STRUCTURAL`, `SEMANTIC`,
`EXECUTION`. The label is not ornamental -- it binds each output section to the
consequence vocabulary of its governing phase. This makes the layer hierarchy
actionable, not decorative.

**5. OUTPUT DECLARATION CHAIN independence made explicit**
The preamble states that PHASE 2 and PHASE 3 each declare their output structure
independently and that neither implies the other. Without this explicit
declaration, execution-body phases were generating output without a committed
declaration site -- allowing undeclared output to ship silently.

---

## Final Rubric Criteria Summary (v18, max 310)

### Tier 1 -- Core Output Structure (C-01 to C-20)
Display-only enforcement. Four output sections: COMMIT RISK REGISTER, COMMIT RISK
BY NAMESPACE, EXPOSURE SUMMARY, COMMIT DECISION. All 9 namespaces in the coverage
table. strategy.md FOUND/NOT FOUND row. STALE EVIDENCE section. HIGHEST PRIORITY
RISK line.

### Tier 2-8 -- Phase and Layer Vocabulary (C-21 to C-38)
Consequence vocabulary in all phase names. [LAYER N] enforcement labels. PHASE 2
dual-axis exit (file-absent / topic-absent structurally distinct). OUTPUT
DECLARATION CHAIN independence. Per-signal VERIFIED / UNVERIFIED assertion.
Consistency guard applied before percent emission. ADVERSARY CHAIN block present.

### Tier 9-11 -- Output Declaration Form (C-39 to C-44)
PHASE 2 OUTPUT DECLARATION with INVARIANT / OUTPUT FORM / Trigger sub-components.
PHASE 3 OUTPUT DECLARATION with same sub-components. Neither phase's declaration
implies the other.

### Tier 12-13 -- Adversary Chain Three-Part Form (C-45 to C-46)
ADVERSARY CHAIN block present in preamble. Each execution-body adversary block
carries ADVERSARY: + DEFEAT CONDITION: three-part form.

### Tier 14 -- Preamble Labeled Adversary Entries (C-47)
Preamble ADVERSARY CHAIN carries P1-ADVERSARY:, P2-ADVERSARY:, P3-ADVERSARY:
labeled entries.

### Tier 15 -- PHASE 1 Adversary Block (C-48)
PHASE 1 execution body carries ADVERSARY: + DEFEAT CONDITION: block.

### Tier 16 -- STOP Predicate Adversary Gate (C-49)
PHASE 4 STOP CONDITION carries [P1-ADVERSARY DEFEAT:] predicate (non-vacuous when
C-48 is present).

### Tier 17 -- v18 Structural Additions (+10 pts)

**C-50 -- Phase-labeled STOP predicates (5 pts)**
STOP predicates (2)-(3)-(4) carry [P-N-ADVERSARY DEFEAT:] phase labels, closing
the three-site label isomorphism: preamble declaration -> execution-body assertion
-> STOP gate verification. Predicate (1) retains numbered form as structural guard.
Prerequisite: C-49 (conditional), C-47 (hard).

**C-51 -- Preamble adversary entry defeat forecast sub-components (5 pts)**
Each labeled P-N-ADVERSARY preamble entry carries a nested `DEFEAT CONDITION:`
sub-component forecasting the execution-body observable defeat property. All-or-
nothing: with C-48 present, all three entries must carry `DEFEAT CONDITION:`.
Partial satisfaction (any entry missing forecast) = FAIL. Prerequisite: C-47 (hard).
