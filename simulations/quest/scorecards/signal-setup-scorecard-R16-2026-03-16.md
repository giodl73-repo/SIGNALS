# Round 16 Scorecard — signal-setup (v14 rubric, A=35)

**Scoring model**: score = (passes + 0.5 × partials) / 35 × 100

---

## V-01 Detailed Scoring

**Axis**: C-35 (Route: label + one-branch-per-line)

**Essential** (5/5 — all PASS)
C-01 PASS | C-02 PASS | C-03 PASS | C-04 PASS | C-05 PASS

**Recommended** (3/3 — all PASS)
C-06 PASS | C-07 PASS | C-08 PASS

**Aspirational**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | GATE 5: "exactly as shown in GATE 3" |
| C-10 | PASS | GATE 1A handles missing CLAUDE.md |
| C-11 | PASS | 6 named top-level gates + sub-gates |
| C-12 | PASS | GATE 1A and GATE 2A are `####`-delimited |
| C-13 | PARTIAL | Preamble explains why setup matters but frames inertia as "rule governs when a topic is ready" — concept, not adversary |
| C-14 | PASS | GATE 1A / 4B: "Inertia wins the planning stage: every session starts without a Signal reminder…" |
| C-15 | PASS | GATE 2A: "the inertia question is present in Claude's context without you having to remember it. The configuration does that work persistently" |
| C-16 | **FAIL** | Preamble says "The inertia rule governs when a topic is ready" — rule/concept framing, not named adversary |
| C-17 | PASS | "present in every session without anyone having to remember it" — persistence argument in preamble |
| C-18 | PASS | "before the next feature commitment" — named future moment |
| C-19 | PASS | GATE 1A Decline and GATE 4B carry identical future-moment language |
| C-20 | PASS | GATE 2A explicitly names CLAUDE.md auto-loading mechanism |
| C-21 | PASS | GATE 6B: "At the implementation stage, Copilot wins the default suggestion…" — Copilot-specific |
| C-22 | PASS | Planning-stage vocabulary (1A/4B) vs. implementation-stage vocabulary (6B) — non-overlapping |
| C-23 | PASS | "planning stage" and "implementation stage" are explicit phase labels |
| C-24 | PASS | GATE 6A scans for `## Signal` heading (not just file existence); already-configured affirmation is Copilot-native |
| C-25 | PASS | 1A, 2A, 4A, 4B, 6A, 6B — all encode parent gate and branch slot |
| C-26 | PASS | GATE 6A and GATE 6B are dedicated named sub-gates for optional Copilot step |
| C-27 | PASS | All gates delimited by `###`/`####` headings |
| C-28 | PASS | Primary paths promoted (GATE 1A, 2A); secondary inline with annotation |
| C-29 | PASS | All Route: blocks enumerate both branches with destination identifiers |
| C-30 | PASS | GATE 6A annotation: "No sub-gate needed for file-existence detection…" |
| C-31 | PASS | All sub-gates use letter-slot: 1A, 2A, 4A, 4B, 6A, 6B — uniform |
| C-32 | PASS | All decline anchors are syntactically complete sentences |
| C-33 | **FAIL** | GATE 6B: "Copilot wins the default suggestion" — Copilot named as winner, not inertia; C-33 requires adversary (inertia or equivalent) as winning party at every decline gate |
| C-34 | PASS | All decline anchors express two-step chains: spec committed [step 1] → question never asked [step 2] |
| C-35 | PASS | Route: label + one-branch-per-line at GATE 1, 1A, 2, 4, 6, 6A |

**Aspirational**: 24.5/27 (1 PARTIAL C-13, 2 FAIL C-16/C-33)

**V-01 Score: 32.5/35 = 92.9%**

---

## V-02 Detailed Scoring

**Axis**: C-33/C-34 (adversary-as-victor + two-step causal chain)

**Essential** (5/5) | **Recommended** (3/3) — all PASS

**Aspirational**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-12 | PASS | Standard |
| C-13 | PASS | Preamble: "**Inertia wins the default choice.**…inertia collects the default.…inertia has a named opponent" — adversary-first motivation |
| C-14–C-15 | PASS | Decline names consequence; GATE 2A affirms positive consequence with opponent framing |
| C-16 | PASS | Preamble frames inertia as named opponent winning the default; teams choose a side |
| C-17 | PASS | "Setup writes the reminder once, permanently, so inertia has a named opponent in every session that follows" |
| C-18–C-20 | PASS | "before the feature direction is locked" (future moment); all exit gates carry it; GATE 2A names loading mechanism |
| C-21–C-23 | PASS | GATE 6B Copilot-specific implementation-stage consequence; phase vocabulary non-overlapping; explicit labels |
| C-24 | PASS | GATE 6A scans for `## Signal`; already-configured affirmation: "At the implementation stage, Copilot has the inertia question in context when it suggests code" |
| C-25 | PASS | All sub-gates encode parent: 1A, 2A, 4A, 4B, 6A, 6B |
| C-26 | PASS | GATE 6A and 6B are named sub-gates |
| C-27 | **FAIL** | GATE 1A routes to `**GATE 1A-Decline:**` (bold label in prose, not a `####` heading) — C-27 requires heading-level delimiters for all gates and sub-gates |
| C-28–C-30 | PASS | Primary promoted; secondary inline with annotation |
| C-31 | **FAIL** | GATE 1A-Decline uses word-suffix identifier; all other sub-gates use letter-slot — mixed convention |
| C-32–C-34 | PASS | All decline anchors: complete sentences; inertia as grammatical subject winning; two-step chains present at all decline gates including GATE 6B |
| C-35 | PASS | Route: blocks at all branching gates including GATE 6A |

**Aspirational**: 25/27 (2 FAIL: C-27, C-31)

**V-02 Score: 33/35 = 94.3%**

---

## V-03 Detailed Scoring

**Axis**: C-24 (Copilot content detection)

**Essential** (5/5) | **Recommended** (3/3) — all PASS

**Aspirational**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-12 | PASS | Standard |
| C-13 | PASS | "Teams commit feature directions without asking why users would change behavior. Signal names the question…" — equivalent inertia concept as reason to configure |
| C-14–C-15 | PASS | Decline names consequence; GATE 2A affirms persistence |
| C-16 | **FAIL** | Preamble names the behavioral pattern without naming inertia as adversary — inertia is absent as a named entity in the preamble |
| C-17 | PASS | "Setup happens once, but the reminder lives in every session that follows" |
| C-18–C-20 | PASS | "before the feature direction is locked" at all decline gates; GATE 2A names loading mechanism |
| C-21–C-23 | PASS | GATE 6B: "At the implementation stage, inertia wins the Copilot suggestion" — Copilot-specific; phase vocabulary non-overlapping; explicit labels |
| C-24 | PASS | GATE 6A two-step: file-existence (Step 1) then `## Signal` content scan (Step 2); already-configured affirmation: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context — the adoption question surfaces during the build" |
| C-25–C-26 | PASS | All letter-slot sub-gates; GATE 6A/6B named sub-gates for optional step |
| C-27 | PASS | All gates delimited by `###`/`####` headings |
| C-28–C-30 | PASS | Primary promoted; secondary inline with annotation |
| C-31 | PASS | All sub-gates: 1A, 2A, 4A, 4B, 6A, 6B — uniform letter-slot |
| C-32–C-34 | PASS | All decline anchors are complete propositions; inertia as winning subject at all decline gates; two-step chains |
| C-35 | PASS | Route: blocks at GATE 1, 1A, 2, 4, 6; GATE 6A branches to inline text (not sub-gates), passes vacuously |
| C-29 | PASS | All routing blocks complete; GATE 6A's inline-text branches are terminal exits |

**Aspirational**: 26/27 (1 FAIL: C-16)

**V-03 Score: 34/35 = 97.1%**

---

## V-04 Detailed Scoring

**Axes**: C-35 + C-31 + C-24 (Route: blocks + uniform identifiers + Copilot content detection)

**Essential** (5/5) | **Recommended** (3/3) — all PASS

**Aspirational**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-12 | PASS | Standard |
| C-13 | PASS | Preamble: "**Inertia wins the default choice.**…inertia collects the default because no one thought to name it" — adversary-first motivational opening |
| C-14 | PASS | GATE 1B: "Inertia wins the planning stage: the spec gets committed without a Signal reminder…"; GATE 4B same; GATE 6B: "inertia wins the build suggestion…adoption assumptions get locked…before anyone asks" |
| C-15 | PASS | GATE 2A: "Inertia already has a named opponent here. Your CLAUDE.md loads automatically every session…" |
| C-16 | PASS | Preamble names inertia as the entity that wins and collects the default — opponent framing present |
| C-17 | PASS | "Setup writes the reminder once; your CLAUDE.md loads it automatically every session, so the question is present without you having to remember it" |
| C-18 | PASS | "before the feature direction is locked" at GATE 1B and GATE 4B; implementation-stage anchoring at GATE 6B |
| C-19 | PASS | GATE 1B and GATE 4B carry identical future-moment consequence language |
| C-20 | PASS | GATE 2A names CLAUDE.md auto-loading mechanism explicitly |
| C-21 | PASS | GATE 6B consequence anchors to implementation stage / Copilot-specific vocabulary |
| C-22 | PASS | GATE 1B/4B: "planning stage" vocabulary; GATE 6B: "implementation stage / build suggestion / Copilot" — non-overlapping |
| C-23 | PASS | "the planning stage" and "the implementation stage" are explicit labels at all decline gates |
| C-24 | PASS | GATE 6A: "Check whether `.github/copilot-instructions.md` exists and, if it does, scan for `## Signal` heading" — two-step detection; already-configured affirmation: "While Copilot is suggesting implementation code, the inertia question is already present in Copilot's context — adoption assumptions surface during the build, not only at the planning stage" |
| C-25 | PASS | 1A/1B (parent 1), 2A (parent 2), 4A/4B (parent 4), 6A/6B (parent 6) — all encode parent and branch slot |
| C-26 | PASS | GATE 6A and GATE 6B are dedicated named sub-gates for the optional Copilot extension step |
| C-27 | PASS | Every gate and sub-gate delimited by `###`/`####` headings |
| C-28 | PASS | GATE 1A (primary detection) and GATE 2A (primary detection) promoted; GATE 6A file-existence detection inline with annotation — C-28 scope boundary correctly applied |
| C-29 | PASS | All Route: blocks enumerate both branches with destination identifiers; GATE 6A routes to inline exit actions (terminal), satisfies completeness |
| C-30 | PASS | GATE 6A annotation: "No sub-gate for file-existence detection — file creation is part of the confirmed write action; no separate confirmation point is required" |
| C-31 | PASS | Sub-gates throughout: 1A, 1B, 2A, 4A, 4B, 6A, 6B — all letter-slot, no word-suffix identifiers at any level |
| C-32 | PASS | All decline anchors are syntactically complete, assertable propositions |
| C-33 | PASS | GATE 1B/4B: "Inertia wins the planning stage"; GATE 6B: "inertia wins the build suggestion" — inertia is grammatical subject at all decline gates |
| C-34 | PASS | GATE 1B/4B: "spec committed without Signal [step 1] → question never asked before direction locked [step 2]"; GATE 6B: "Copilot writes assuming adoption [step 1] → assumptions locked before anyone asks [step 2]" |
| C-35 | PASS | Route: label + one-branch-per-line at GATE 1, 1A, 2, 4, 6, 6A |

**Aspirational**: 27/27

**V-04 Score: 35/35 = 100.0%**

---

## V-05 Detailed Scoring

**Axes**: Full synthesis (C-16 + C-27 + C-24 + C-29/C-35 + C-31 + C-32 + C-33 + C-34)

**Essential** (5/5) | **Recommended** (3/3) — all PASS

**Aspirational**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-16 | PASS | Preamble: "**Inertia wins the default choice.**…inertia has a named opponent without you having to remember to name it" — adversary framing passes C-16 |
| C-17–C-20 | PASS | Persistence argument in preamble; future-moment anchors at GATE 1B/4B; GATE 2A names loading mechanism |
| C-21–C-24 | PASS | GATE 6B Copilot-specific; phase vocabulary non-overlapping; GATE 6A two-step detection with GATE 6A-Found providing Copilot-native affirmation |
| C-25 | PASS | 6A-Found encodes parent (6A) and branch (Found) — lineage present |
| C-26–C-30 | PASS | Optional step promoted to named sub-gates; all headings; C-28 scope applied; C-29 complete routing; C-30 annotation present |
| C-31 | **FAIL** | GATE 6A-Found and GATE 6A-Write use word-suffix identifiers while all other sub-gates (1A, 1B, 2A, 4A, 4B, 6A, 6B) use letter-slot. C-31 is explicit: "Mixed-convention specs score FAIL regardless of which convention dominates." The synthesis notes in V-05 itself flag this as requiring scorer adjudication — the adjudication is FAIL |
| C-32–C-35 | PASS | All decline anchors complete; inertia as subject at all decline gates including GATE 6B; two-step chains throughout; Route: blocks at all branching gates |

**Aspirational**: 26/27 (1 FAIL: C-31)

**V-05 Score: 34/35 = 97.1%**

---

## Rankings

| Rank | Variation | Score | Fails |
|------|-----------|-------|-------|
| 1 | **V-04** | **100.0% (35/35)** | none |
| 2 | V-03 | 97.1% (34/35) | C-16 |
| 2 | V-05 | 97.1% (34/35) | C-31 |
| 4 | V-02 | 94.3% (33/35) | C-27, C-31 |
| 5 | V-01 | 92.9% (32.5/35) | C-16, C-33, C-13 partial |

---

## Excellence Signals from V-04

**1. Inline-action Route: blocks eliminate the sub-gate naming-tier problem**
V-04's GATE 6A routes to inline text actions (affirmation message, write action) rather than to named sub-gates. This keeps the Route: label and one-entry-per-line format (satisfying C-35) without creating a deeper tier of sub-gate identifiers that would require naming conventions. V-05 promoted those same targets to GATE 6A-Found and GATE 6A-Write, which added structural clarity but introduced the word-suffix tier that defeated C-31. V-04's pattern: *let terminal actions be inline text inside a Route: block, not promoted gates*.

**2. Single-tier letter-slot scheme throughout, zero exceptions**
V-04 never introduces a gate identifier that deviates from the `GATE NA` / `GATE NB` format. By handling GATE 6A's content-detection branches as Route: → inline text rather than Route: → named sub-gates, there is no occasion to name anything at a deeper tier. C-31 uniformity is trivially satisfied because there is only one identifier tier.

**3. Inertia-as-victor preamble coexists cleanly with navigational heading labels**
V-04 confirms the architectural insight from R15: adversary framing in the preamble body ("inertia wins the default choice") and navigational heading labels ("GATE 1 — Detect CLAUDE.md") occupy different document layers. The heading is structural; the adversary language is semantic. No tension exists between C-16 (adversary framing) and C-27 (heading-level gates). Both pass simultaneously.

**4. Consequence chain precision at secondary gates**
GATE 6B's decline anchor uses Copilot-native vocabulary for a full two-step chain: "Copilot writes code that assumes adoption without the inertia question in context [step 1], and adoption assumptions get locked into the implementation before anyone asks whether they are warranted [step 2]." Inertia is the grammatical subject ("inertia wins the build suggestion"), satisfying C-33. The chain is explicit and phase-indexed (implementation stage), satisfying C-22 and C-34 simultaneously.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inline-action Route: blocks satisfy C-35 without requiring named sub-gate promotion: routes to terminal inline text rather than named sub-gates keep C-31 clean by avoiding deeper identifier tiers entirely", "Single-tier letter-slot sub-gate scheme with zero exceptions: keeping all sub-gates at GATE NA/NB format and routing optional-extension content-detection branches to inline text (not named sub-gates) eliminates every occasion for mixed-convention failure"]}
```
