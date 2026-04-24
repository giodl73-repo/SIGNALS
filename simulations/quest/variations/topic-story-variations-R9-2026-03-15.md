Saved to `simulations/quest/golden/topic-story-variate-R9-v9-2026-03-15.md`.

---

# Variations — topic-story (Round 9, rubric v8 / C-24+C-25 track)

## Design context

**C-24 gap (from prior track)**: Every prior variation enforced pre-composition via structural separators (OPEN/CLOSED, phase stamps, Part 1/2). These satisfy C-18 but not C-24. Separators only verify document order — an author who writes a beat first, then fills in the analytic block above, satisfies the separator while violating the intent. C-24 closes this by requiring named roles (ANALYST/AUTHOR) with an explicit one-way marker (`[ANALYST COMPLETE — AUTHOR MAY BEGIN]`). Retroactive block-writing becomes a visible named role violation, not a silently permitted reorder.

**C-25 gap (from prior track)**: No variation required the author to explicitly confirm each requirement at output's end. Compliance was assumed from having written compliant sections. C-25 closes this with a terminal declarative checklist — one binary `[ ]→[x]` item per structural requirement, requiring quoted evidence per item, gating submission on all items checked.

---

## Axes chosen

| Variation | Primary axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | Role sequence | Named ANALYST/AUTHOR + one-way marker satisfies C-24 |
| V-02 | Output format | Terminal declarative audit section satisfies C-25 |
| V-03 | Role sequence (phase vocabulary) | Named phases with completion stamps satisfy C-24 without actor-role vocabulary |
| V-04 | Combination V-01+V-02 | Role gate + terminal checklist compose cleanly; checklist audits the role marker |
| V-05 | Full combination | Three-role (EXTRACTOR/ANALYST/AUTHOR) + all mechanisms; tests composite scoring |

---

## V-01 — Role Sequence (C-24 primary)

Two named roles: **ANALYST** (all analytic blocks) and **AUTHOR** (all beats). Explicit one-way completion marker required before Beat 1. Mid-prose conflict triggers named ANALYST re-entry with a `[ANALYST RE-COMPLETE — AUTHOR MAY RESUME]` stamp.

Key mechanisms added:
- `[ANALYST COMPLETE — AUTHOR MAY BEGIN]` as structural gate
- Role boundary prohibition: no beat vocabulary in ANALYST phase, no analytic blocks after beats begin
- Reopen path: halt → ANALYST adds row → re-close register → resume

No terminal checklist (single axis).

---

## V-02 — Terminal Declarative Checklist (C-25 primary)

Keeps prior-track V-01 analytic structure (OPEN/CLOSED lifecycle, pre-story gate, mutation ledger). Adds a **Submission Audit** section with 10 binary items:

- `[ ] S0 FALSIFIABLE` — quote S0, confirm falsifiable
- `[ ] LEDGER COMPLETE` — artifact count
- `[ ] S3 PRESENT` — quote S3
- `[ ] ANTI-STAGNATION` — directional shift confirmed
- `[ ] REGISTER LIFECYCLE` — OPEN+CLOSED stamps present, quote closure stamp
- `[ ] PRE-STORY GATE` — closure confirmed before Beat 1
- `[ ] PATTERN BLOCK PRESENT` — quote pattern claim, confirm not single-artifact
- `[ ] UNRESOLVED VERBATIM` — count matches stamp
- `[ ] RECOMMENDATION VERB` — verb + posture named
- `[ ] RISK FLOOR NAMED` — quote the sentence

Gate rule: artifact not complete until all items are `[x]`.

No named ANALYST/AUTHOR roles (single axis).

---

## V-03 — Named Phase Sequencing (C-24 via phases, not roles)

Four phases — **EVIDENCE / CONFLICT / PATTERN / STORY** — each with a named entry gate requiring the prior phase stamp and a mandatory completion stamp:

```
[PHASE I COMPLETE — {N} artifacts processed; S3: {...}]
[PHASE II COMPLETE — register closed: N rows, R RESOLVED, U UNRESOLVED]
[PHASE III COMPLETE — pattern: {...}; posture: {...}]
```

STORY phase entry gate requires PHASE III COMPLETE. Non-substitution enforced: Phase III pattern block does not satisfy Beat 3's placement requirement — Beat 3 must earn the pattern through prose.

Tests whether phase vocabulary achieves C-24's structural verifiability without actor-role naming.

---

## V-04 — Role Gate + Terminal Checklist (C-24+C-25 combined)

Builds on prior-track V-01 (OPEN/CLOSED lifecycle + domain falsifier). Adds:

1. ANALYST/AUTHOR roles with one-way `[ANALYST COMPLETE]` marker (V-01 mechanism)
2. ANALYST phase includes a **Pattern Block** with domain falsifier field
3. Terminal Submission Audit with 11 items including `[ ] ANALYST COMPLETE MARKER` — first time the checklist audits the role gate itself
4. Non-substitution rule: Beat 3 pattern stated independently from ANALYST PATTERN BLOCK

---

## V-05 — Full Combination

Three-role architecture: **EXTRACTOR** (reads artifacts, produces Signal Extract section) → **ANALYST** (ledger, register, pattern block) → **AUTHOR** (beats). Each role terminates with a named completion marker.

Mechanisms present:
- Named three-role sequence with completion markers (C-24)
- Terminal Submission Audit with four sections: Role Boundary Compliance, Analytic Completeness, Non-Substitution, Multi-Stage Consistency (C-25)
- Domain falsifier field (C-23)
- Reopen protocol (C-22)
- Non-substitution at Beat 3 and Beat 5 (C-19)
- Multi-stage consistency: evidence posture + recommendation verb appear in both ANALYST PATTERN BLOCK and Beat 5; inconsistency is structurally self-revealing (C-20)
- Submission Audit requires quoted evidence for every item (not assertion)
