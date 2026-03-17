Written to `simulations/quest/golden/quest-golden-variate-R2-2026-03-16.md`.

---

## quest-golden -- Round 2 Variations (V-01 through V-05)

**Rubric:** v2 (13 criteria) | **Primary gap from R1:** C-02 and C-03 universally PARTIAL, C-10 universally FAIL

---

### V-01 -- Output Contract *(single-axis)*

**axis:** output-contract
**hypothesis:** Replacing the implicit GOLDEN OUTPUT section with an explicit verbatim-contract checklist will convert C-02 and C-03 from universally PARTIAL to PASS. Every R1 variation implied "write the full prompt" but none said "not a summary, not a label, not a reference to a prior variation." The checklist is the only new structure; the rest is V-03-R1 lifecycle phases unchanged.

**Base:** V-03-R1 lifecycle phases + GOLDEN OUTPUT replaced with artifact contract

Key addition to GOLDEN OUTPUT:
```
Required contents -- each item must be present:
- Complete prompt body verbatim: every line of the deployed skill body, not a summary,
  not a label, not "see V-03," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: ... Minimum 2 mechanisms with
  explicit round citations.

...
- File is standalone: not embedded inside Artifact 1; navigable without opening the golden
  prompt file
```

---

### V-02 -- Contrast-Delta Notation *(single-axis)*

**axis:** contrast-delta notation (output-format variant: structured field pair in QU2 step)
**hypothesis:** A named delta block with "TOP HAD" and "SECOND LACKED" as paired required fields structurally prevents the extractor from filling the signal with a property both variations shared. Directly targets C-12 (new in v2). V-02-R1 was the only R1 variation to PASS C-07, solely because its contrast column forced gap-stating. This moves that mechanism into the skill body itself.

**Base:** V-03-R1 lifecycle phases + QU2 step replaced with delta block

Key addition to PHASE 3:
```
TOP VARIATION:  [ID]
SECOND-RANKED:  [ID]
TOP HAD:        [element present in TOP]
SECOND LACKED:  [the same element stated as an absence -- "no X" or "missing X"]
SIGNAL NAME:    SIGNAL-R{N}: [name] | none
```

Rules: TOP HAD and SECOND LACKED must describe the same element from opposite sides. If both variations had it, it is not the signal.

---

### V-03 -- Rationale-Reinforced Sequencing *(single-axis)*

**axis:** rationale-grounded sequencing (phrasing-register variant: "because" clauses on role-sequence backbone)
**hypothesis:** V-04-R1 earned PASS on C-04 via "because..." language but scored lowest (56) because conversational register weakened structural gates. This variation puts rationale clauses on a structural backbone (V-01-R1 roles), targeting C-13 without degrading C-01/C-05.

**Base:** V-01-R1 six-role sequence + rationale clauses at RUBRIC KEEPER, CRITERION AUTHOR, CONVERGENCE JUDGE

Key rationale insertions:
- **RUBRIC KEEPER:** *"...because variation rankings without a grounded objective function are not comparable..."*
- **CRITERION AUTHOR:** *"QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial guess: it reflects the author's priors rather than what the loop actually measured..."*
- **CONVERGENCE JUDGE:** *"Both conditions must be true before the loop exits -- trial convergence alone means the rubric stopped evolving before all patterns were found; quest convergence alone means signals ran out before variations reached the essential bar..."*

---

### V-04 -- Combination: V-05-R1 + Output Contract *(combination)*

**axis:** inertia-framing + lifecycle-emphasis + output-contract
**hypothesis:** V-05-R1 scored 78 with PASS on C-01, C-04, C-05, C-06, C-07, C-09. Only C-02 and C-03 were PARTIAL. Adding the output contract checklist to PHASE 4 GOLDEN OUTPUT should convert both essentials to PASS without disturbing any other result. Expected composite: >= 90.

**Base:** V-05-R1 complete + GOLDEN OUTPUT section replaced with artifact contract (same contract as V-01)

---

### V-05 -- Full Synthesis *(combination)*

**axis:** inertia + lifecycle + output-contract + contrast-delta + rationale (full combination)
**hypothesis:** Each axis targets a distinct criterion gap. No two mechanisms touch the same step. Combined:

| Mechanism | Source | Targets |
|-----------|--------|---------|
| Inertia framing + PHASE 0-4 | V-05-R1 | C-01, C-04, C-05, C-06, C-07, C-09, C-11 |
| Output contract checklist | V-01-R2 | C-02, C-03, C-10 |
| Contrast-delta block | V-02-R2 | C-12 |
| Rationale clauses | V-03-R2 | C-13 |

Expected composite: > 90. Any criterion that still fails identifies which mechanism was insufficient.

Key synthesis in PHASE 3 QU2 step -- combines inertia contrast with delta notation:
```
TOP HAD / SECOND LACKED: [element absent from second -- stated as absence]
TOP HAD / INERTIA LACKED:[element absent from inertia -- this is the discovery]
SIGNAL NAME:             SIGNAL-R{N}: [name] | none
```

With rationale: *"QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial guess, not a discovery..."*

---

**Next step:** `/quest:score` against rubric v2 with these 5 variations.
