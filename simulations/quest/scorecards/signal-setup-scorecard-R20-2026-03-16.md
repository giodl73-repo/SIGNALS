## signal-setup — Round 20 Scorecard (v18 rubric)

**Skill**: signal-setup | **Rubric**: v18 | **Date**: 2026-03-17
**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/45 × 10)`
**Golden threshold**: all 5 essentials PASS AND composite ≥ 80

---

## V-01 — Asymmetric inline annotation in parallel extension gates (C-43 failure axis)

**Structure**: Two-integration word-suffix spec (Copilot + VS Code). GATE 6-Copilot carries annotation; GATE 6-VSCode does not.

### Essential (C-01–C-05)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | GATE 1 reads CLAUDE.md before any write |
| C-02 | PASS | GATE 3 displays preview content |
| C-03 | PASS | GATE 4 requires explicit confirmation |
| C-04 | PASS | Signal section with nine namespace list appended |
| C-05 | PASS | GATE 2 detects existing section and skips |

**Essential: 5/5**

### Recommended (C-06–C-08)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Inertia rule included in appended section body |
| C-07 | PASS | GATE 6 menu offers Copilot, VS Code, skip |
| C-08 | PASS | GATE 5 outputs explicit outcome report |

**Recommended: 3/3**

### Aspirational (C-09–C-45)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | GATE 3 preview is byte-equivalent to GATE 5 write note |
| C-10 | PASS | GATE 1-Miss handles missing CLAUDE.md as named sub-gate |
| C-11 | PASS | GATE 1–6 + all sub-gates as named checkpoints; no phase implicitly skipped |
| C-12 | PASS | GATE 1-Miss and GATE 2-Found are `####`-delimited first-class sub-gates |
| C-13 | PASS | Preamble opens with inertia framing before any procedure |
| C-14 | PASS | GATE 1-Decline and GATE 4-Decline name what remains unaddressed |
| C-15 | PASS | GATE 2-Found: "inertia already has a named opponent here" |
| C-16 | PASS | "Inertia wins the default choice" — adversary framing |
| C-17 | PASS | "Setup happens once; your CLAUDE.md loads it automatically, so the choice holds" |
| C-18 | PASS | "never gets asked before the feature direction is locked" — named future moment |
| C-19 | PASS | GATE 1-Decline and GATE 4-Decline carry identical future-moment framing |
| C-20 | PASS | GATE 2-Found names persistence mechanism: "loads automatically every session" |
| C-21 | PASS | GATE 6-Decline (skip) names implementation-stage consequence; no per-tool decline gates exist, so no tool-specific anchor required |
| C-22 | PASS | GATE 4-Decline: "spec gets committed / planning stage"; GATE 6-Decline: "build suggestion / implementation stage" — non-overlapping vocabulary |
| C-23 | PASS | GATE 1-Decline/GATE 4-Decline: "planning stage" explicit; GATE 6-Decline: "At the implementation stage" explicit |
| C-24 | PASS | GATE 6Cop-Found affirms Copilot vocabulary; GATE 6VS-Found affirms VS Code vocabulary ("workspace annotation layer," "editor") |
| C-25 | PASS | All sub-gate IDs encode parent lineage (GATE 1-Miss/GATE 1-Decline → parent 1; GATE 6Cop-Found → parent 6-Copilot; GATE 6VS-Found → parent 6-VSCode) |
| C-26 | PASS | GATE 6-Copilot, GATE 6-VSCode, GATE 6-Decline are `####`-headed first-class optional-extension gates |
| C-27 | PASS | Every gate delimited by `###` or `####`; no bold-label pseudo-gates |
| C-28 | PASS | Primary paths (GATE 1-Miss, GATE 2-Found) promoted; secondary detection in GATE 6-Copilot and GATE 6-VSCode intentionally inline |
| C-29 | PASS | All routing blocks complete: every branch listed with (condition → GATE ID) |
| C-30 | PASS | GATE 6-Copilot carries annotation; C-43 is the criterion that catches the cross-gate consistency failure, not C-30 |
| C-31 | PASS | Consistent word-suffix scheme throughout: -Miss, -Decline, -Found, -Confirm, -Copilot, -VSCode, 6Cop-, 6VS- |
| C-32 | PASS | All consequence anchors are syntactically complete sentences with subject + predicate + stated outcome |
| C-33 | PASS | "Inertia wins the planning stage" (GATE 1/4-Decline); "inertia wins the build suggestion" (GATE 6-Decline) — inertia as grammatical subject |
| C-34 | PASS | GATE 4-Decline: "spec gets committed… AND question never gets asked." GATE 6-Decline: "inertia wins… signal absent… so assumptions get written in." Two-step chains present |
| C-35 | PASS | All routing blocks use "Route:" label and one-branch-per-line format |
| C-36 | PASS | "Inertia wins the default choice" — active dominance verb |
| C-37 | PASS | "You are choosing a side" — explicit agency-choice claim |
| C-38 | PASS (vacuous) | No per-tool decline gates; GATE 6-Decline is a collective skip path |
| C-39 | PASS | "You are not just enabling a plugin. You are choosing a side." — refutation then assertion |
| C-40 | PASS | GATE 2-Found: "You chose a side" — past-tense echo of preamble's choice-claim |
| C-41 | PASS | GATE 6Cop-Found/GATE 6Cop-Write extend GATE 6-Copilot (6 + Cop + branch); GATE 6VS-Found/GATE 6VS-Write extend GATE 6-VSCode (6 + VS + branch) |
| C-42 | PASS | "Cop" vs "VS" — non-colliding depth-2 abbreviations |
| C-43 | **FAIL** | GATE 6-Copilot: annotation present. GATE 6-VSCode: no annotation. Identical architectural choice (inline detection, bundled creation) treated asymmetrically. Second gate is indeterminate |
| C-44 | PASS (vacuous) | No per-tool decline gates |
| C-45 | PASS | GATE 6Cop-Found: "While Copilot is suggesting…" (concurrent). GATE 6VS-Found: "While VS Code is open and the workspace annotation layer is active…" (concurrent) |

**Aspirational passing: 36/37 (C-43 fails)**

### V-01 Composite

```
Essential:    5/5   × 60  =  60.00
Recommended:  3/3   × 30  =  30.00
Aspirational: 36/45 × 10  =   8.00
                            -------
                              98.00
```

---

## V-02 — Copilot decline names inertia as winner but omits the artifact (C-44 failure axis)

**Structure**: Single-Copilot letter-slot spec. GATE 6B has "inertia wins the build suggestion through Copilot — Signal is absent… adoption assumptions get locked" but no artifact clause.

### Essential: 5/5 | Recommended: 3/3

### Aspirational (selective — deviates from R19 V-04 only at GATE 6B)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-42 | PASS (all) | Identical to R19 V-04 on all primary and secondary paths; no structural changes |
| C-43 | PASS (vacuous) | Single optional-extension gate; no parallel inline-detection paths |
| C-44 | **FAIL** | GATE 6B: "inertia wins the build suggestion through Copilot — Signal is absent from the implementation context, and adoption assumptions get locked into the build before anyone asks whether they are warranted." Inertia is winner (C-38 PASS); two-step chain present (C-34 PASS); but no artifact named — "code that assumes adoption gets generated" absent. Force named; channel named; output of channel not named |
| C-45 | PASS | GATE 6AA: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context" — concurrent-moment construction unchanged |

**Aspirational passing: 36/37 (C-44 fails)**

### V-02 Composite

```
Essential:    5/5   × 60  =  60.00
Recommended:  3/3   × 30  =  30.00
Aspirational: 36/45 × 10  =   8.00
                            -------
                              98.00
```

---

## V-03 — Already-configured affirmation uses archival/future framing (C-45 failure axis)

**Structure**: Single-Copilot word-suffix spec. GATE 6CP-Found: "When the team reaches the build phase, the inertia question will be in Copilot's context…" — future conditional.

### Essential: 5/5 | Recommended: 3/3

### Aspirational (selective — deviates from R19 V-05 only at GATE 6CP-Found)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-23 | PASS (all) | Identical to R19 V-05 on all primary-path gates |
| C-24 | PASS | "inertia has a named opponent at the implementation stage. When the team reaches the build phase, the inertia question will be in Copilot's context" — affirms tool-local consequence in Copilot vocabulary. C-24 requires tool-local framing; it is satisfied even with future tense |
| C-25–C-42 | PASS (all) | Structural and behavioral criteria unchanged from R19 V-05 |
| C-43 | PASS (vacuous) | Single optional-extension gate |
| C-44 | PASS | GATE 6-Decline: "inertia wins the build suggestion through Copilot: code that assumes adoption gets generated without the inertia question in context" — artifact named |
| C-45 | **FAIL** | GATE 6CP-Found: "When the team reaches the build phase, the inertia question *will be* in Copilot's context before implementation assumptions get locked in." Future-conditional construction describes a coming state; does not place Signal as co-present *during* active tool operation. The "while [tool] is [active]" construction required by C-45 is absent. C-24 passes (tool-local consequence present); C-45 fails (temporal register wrong — future vs. concurrent) |

**Aspirational passing: 36/37 (C-45 fails)**

### V-03 Composite

```
Essential:    5/5   × 60  =  60.00
Recommended:  3/3   × 30  =  30.00
Aspirational: 36/45 × 10  =   8.00
                            -------
                              98.00
```

---

## V-04 — R19 V-04 confirmed under v18 (letter-slot golden candidate)

**Structure**: Single-Copilot letter-slot spec, text unchanged from R19 V-04.

### Essential: 5/5 | Recommended: 3/3

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-42 | PASS (all) | All satisfied in R18/R19; text unchanged |
| C-43 | PASS (vacuous) | Only GATE 6A as optional-extension gate; no parallel inline-detection paths exist; consistency requirement has nothing to enforce |
| C-44 | PASS | GATE 6B: "inertia wins the build suggestion through Copilot: code that assumes adoption gets generated without the inertia question in context" — inertia as winner (C-38), artifact named (C-44) |
| C-45 | PASS | GATE 6AA: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context" — concurrent-moment construction; Signal shown as operationally co-present, not merely installed |

**Aspirational passing: 37/37**

### V-04 Composite

```
Essential:    5/5   × 60  =  60.00
Recommended:  3/3   × 30  =  30.00
Aspirational: 37/45 × 10  =   8.22
                            -------
                              98.22
```

---

## V-05 — R19 V-05 confirmed under v18 (word-suffix golden candidate)

**Structure**: Single-Copilot word-suffix spec, text unchanged from R19 V-05.

### Essential: 5/5 | Recommended: 3/3

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-42 | PASS (all) | All satisfied in R18/R19; text unchanged |
| C-43 | PASS (vacuous) | Only GATE 6-Copilot as optional-extension gate; no parallel inline-detection pair |
| C-44 | PASS | GATE 6-Decline: "inertia wins the build suggestion through Copilot: code that assumes adoption gets generated without the inertia question in context" — artifact named |
| C-45 | PASS | GATE 6CP-Found: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context — adoption assumptions surface during the build, not only at the planning stage." Concurrent-moment; Signal shown active at the moment the tool acts |

**Aspirational passing: 37/37**

### V-05 Composite

```
Essential:    5/5   × 60  =  60.00
Recommended:  3/3   × 30  =  30.00
Aspirational: 37/45 × 10  =   8.22
                            -------
                              98.22
```

---

## Ranking

| Rank | Variation | Score | Axis | Failing |
|------|-----------|-------|------|---------|
| 1 (tie) | V-04 | 98.22 | Golden — letter-slot | none |
| 1 (tie) | V-05 | 98.22 | Golden — word-suffix | none |
| 3 (tie) | V-01 | 98.00 | C-43 failure | C-43 |
| 3 (tie) | V-02 | 98.00 | C-44 failure | C-44 |
| 3 (tie) | V-03 | 98.00 | C-45 failure | C-45 |

**Score gap between golden and failing**: 0.22 points per missed aspirational criterion (1 criterion = 1/45 × 10 = 0.22).

---

## Excellence Signals from V-04/V-05

**Pattern 1 — Single-integration vacuity eliminates the C-43 surface.** Both golden candidates use a single optional-extension gate. C-43's cross-gate consistency requirement only activates when two or more parallel inline-detection gates exist. Single-integration specs pass C-43 vacuously — not by satisfying the consistency requirement but by never creating the situation it governs. This is not a shortcut: adding a second integration would immediately require consistent annotation on both. The lesson is structural: each optional-extension gate added creates a C-43 obligation on every gate in the group.

**Pattern 2 — The C-38 → C-44 causal chain must reach the artifact, not stop at force + channel.** V-02 demonstrates the boundary: "inertia wins through Copilot" satisfies C-38 (force named, not tool) and begins the chain, but C-44 requires one more step: what the tool *produces* under inertia's control. "Code that assumes adoption gets generated" names the artifact concretely and tool-specifically. The chain is: force (inertia) → channel (Copilot) → output (adoption-assuming code). Stopping at two links fails C-44.

**Pattern 3 — Concurrent-moment construction vs. archival-state or future-conditional description.** V-03 demonstrates the boundary: "when the team reaches the build phase, the inertia question *will be* in Copilot's context" satisfies C-24 (tool-local consequence affirmed) but fails C-45. The construction "While Copilot is *suggesting* implementation code, the inertia question is *already* in Copilot's context" uses present progressive + "already" to assert co-presence at the moment of action. The temporal register is operational, not archival or prospective. A reader learns Signal is present *now when the tool acts*, not that it will be present eventually or that it was installed in the past.

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Score | Golden? |
|-----------|-----------|-------------|--------------|-------|---------|
| V-01 | 5/5 | 3/3 | 36/37 (C-43 FAIL) | 98.00 | No |
| V-02 | 5/5 | 3/3 | 36/37 (C-44 FAIL) | 98.00 | No |
| V-03 | 5/5 | 3/3 | 36/37 (C-45 FAIL) | 98.00 | No |
| **V-04** | **5/5** | **3/3** | **37/37** | **98.22** | **Yes** |
| **V-05** | **5/5** | **3/3** | **37/37** | **98.22** | **Yes** |

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": []}
```
