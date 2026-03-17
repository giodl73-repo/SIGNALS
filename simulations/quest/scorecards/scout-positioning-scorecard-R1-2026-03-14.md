Scorecard written to `simulations/quest/scorecards/scout-positioning-scorecard-R1-2026-03-14.md`.

---

**Rankings:**

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Lifecycle + findings-first | **95** | YES |
| 2 | V-03 Matrix-dominant | **92** | YES |
| 3 | V-04 Inertia-primary + conversational | **87** | YES |
| 4 | V-02 GTM-leads | **84** | YES |
| 5 | V-01 Baseline | **78** | NO |

**V-01 fails all_essential_pass** — C-04 is PARTIAL because "contrast form **preferred**" is too weak. Every other variation strengthens this to required or operationalizes it (V-04 best: two-level contrast vs inertia then named competitor).

**V-05 wins on structural enforcement.** Its key move: FINDINGS section numbers map directly to rubric criteria. Omission becomes visible by inspection. The other distinguishing moves are `STOP and emit` (vs conditional language) for C-01, and the citation obligation for whitespace (C-10).

**V-03 is a strong #2** — matrix-dominant format produces the most grounded anti-positioning (C-05: every "NOT X" must correspond to a matrix row) and operationalizes whitespace via matrix cells. Best approach if the goal is defensibility of claims over prose clarity.

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["findings-section structure mirrors rubric criteria — numbered FINDINGS sections map one-to-one to rubric criteria, making omission visible by inspection", "STOP enforcement verb for prior-run handling — stronger than conditional emit; prevents silent continuation with degraded output", "dedicated degradation-note section in FINDINGS — separates diagnostic from positioning output, ensures the note survives LLM compression of setup prose", "citation obligation for whitespace — require citing specific matrix dimensions, making the whitespace claim falsifiable"]}
```
| 8 | PASS | "hierarchy must be explicit — flat lists fail this step" |
| C-09 | Degradation quant. | 8 | PASS | FINDINGS: named example "primary competitor is likely inertia, but without scout:competitors…" |
| C-10 | Whitespace ID | 8 | PASS | "one uncontested space… grounded in competitor data" |

**Total: 78/100 · All essential pass: NO (C-04 PARTIAL)**

---

## V-02: GTM-leads (role sequence axis)

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | SETUP provides exact degradation warning text as inline example; explicit fallback to 3–5 inline competitors |
| C-02 | Per-audience statements | 9 | PASS | "Do not write a generic statement then vary the vocabulary — each statement should emphasize a different dimension" — strongest audience-differentiation rule |
| C-03 | Category definition | 8 | PASS | Strategy extracts from GTM, must be ownable, inconsistency-flagging mechanic added |
| C-04 | Core differentiator | 9 | PASS | "If no single differentiator threads through, flag the inconsistency rather than inventing one" — explicit integrity check |
| C-05 | Anti-positioning | 8 | PASS | "grounded in the category definition from Strategy, plausible confusion categories only" — adds grounding constraint |
| C-06 | PM reality check | 8 | PASS | "Flag claims that are ahead of the spec" explicit; standard otherwise |
| C-07 | Comp. matrix | 8 | PASS | Tabular, 2+ competitors, 3+ dimensions; same minimum as V-01 |
| C-08 | Messaging hierarchy | 9 | PASS | "Mark the hierarchy structure explicitly — not just ordering" — names the anti-pattern |
| C-09 | Degradation quant. | 8 | PASS | SETUP has exact example degradation text |
| C-10 | Whitespace ID | 8 | PASS | "grounded in competitor data" |

**Total: 84/100 · All essential pass: YES**

---

## V-03: Matrix-dominant (output format axis)

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | SETUP handles it; FINDINGS adds "state exactly which matrix columns cannot be reliably scored" — two-level degradation specificity |
| C-02 | Per-audience statements | 8 | PASS | Per-audience with matrix citation requirement — grounded but adds friction |
| C-03 | Category definition | 10 | PASS | Derived from matrix: "supported by at least 2 matrix dimensions where Signal is H and no competitor is H" — operationalized, not asserted |
| C-04 | Core differentiator | 9 | PASS | "single dimension where Signal's position is most distinctive… plain language contrasting with nearest competitor" — matrix-backed |
| C-05 | Anti-positioning | 10 | PASS | "Each must correspond to a matrix row where a competitor is H and Signal is L or M" — fully data-grounded; strongest |
| C-06 | PM reality check | 9 | PASS | "Trace each claim back to its matrix cell" — explicit traceability requirement |
| C-07 | Comp. matrix | 10 | PASS | 5+ dimensions required (vs 3 elsewhere); matrix is structural anchor of entire prompt |
| C-08 | Messaging hierarchy | 8 | PASS | Standard hierarchy; no stronger enforcement |
| C-09 | Degradation quant. | 9 | PASS | SETUP + FINDINGS: "state exactly which matrix columns cannot be reliably scored" — most specific |
| C-10 | Whitespace ID | 10 | PASS | "matrix cells where no competitor is H and Signal is H or could be H" — operationalized via matrix; verifiable |

**Total: 92/100 · All essential pass: YES**

---

## V-04: Inertia-primary + conversational register (combined axes)

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | "Say so explicitly and name the specific gap" with inline example |
| C-02 | Per-audience statements | 9 | PASS | Language signals per audience named explicitly ("Developers hear about technique and workflow. PMs hear about evidence and decisions.") |
| C-03 | Category definition | 9 | PASS | "can't be 'AI coding assistant' or 'testing framework' — those are taken" — explicit category exclusions |
| C-04 | Core differentiator | 10 | PASS | Two-level contrast: "vs inertia first (why change at all?), then vs nearest competitor (why this instead of that?)" — strongest; inertia-first makes differentiator work harder |
| C-05 | Anti-positioning | 8 | PASS | "not obvious negations" — names the anti-pattern; 2+ minimum |
| C-06 | PM reality check | 8 | PASS | "whether it's ahead of spec or just unsupported" — two-category PARTIAL distinction |
| C-07 | Comp. matrix | 8 | PASS | "table, Signal plus 2+ competitors, 3+ columns" — standard minimum |
| C-08 | Messaging hierarchy | 9 | PASS | "Make the hierarchy visible — label the primary message, label the secondary messages" — explicit label requirement |
| C-09 | Degradation quant. | 9 | PASS | "name the specific gap" with example; "running inline to fill the gap" keeps momentum |
| C-10 | Whitespace ID | 8 | PASS | "grounded in what you found above" — light |

**Total: 87/100 · All essential pass: YES**

---

## V-05: Lifecycle-explicit + findings-first (combined axes)

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 10 | PASS | "STOP and emit a degradation note before proceeding. The note must name the specific positioning risk (not just 'quality may vary')" — strongest enforcement verb; dedicated FINDINGS section 8 ensures it survives to output |
| C-02 | Per-audience statements | 9 | PASS | FINDINGS section 2: "the 1–2 audience framing signals that make it distinct from the other statements" — uniqueness must be named |
| C-03 | Category definition | 9 | PASS | FINDINGS section 1: structured output slot `Category: [ownable category name]` — explicit, checklist-able |
| C-04 | Core differentiator | 9 | PASS | FINDINGS section 1: `Core differentiator: [one sentence]` + EXECUTE STRATEGY requires contrast form — double-specified |
| C-05 | Anti-positioning | 9 | PASS | FINDINGS section 5: `Signal is NOT [X] — [why this confusion is plausible]` — rationale required per item |
| C-06 | PM reality check | 10 | PASS | FINDINGS section 7: dedicated `Claim | Verdict | Reason` table; section is numbered and cannot be skipped |
| C-07 | Comp. matrix | 9 | PASS | FINDINGS section 4: "H/M/L scale" specified; Signal + 2+ competitors, 3+ dimensions; section anchor |
| C-08 | Messaging hierarchy | 10 | PASS | EXECUTE DESIGN: "label the hierarchy structure explicitly with labels (PRIMARY / SECONDARY)"; FINDINGS section 3: `PRIMARY: [one message]` — double-enforced |
| C-09 | Degradation quant. | 10 | PASS | "STOP", "not just 'quality may vary'" — names the anti-pattern; dedicated section 8 in FINDINGS guarantees it surfaces |
| C-10 | Whitespace ID | 10 | PASS | FINDINGS section 6: "Must be grounded in the matrix above — cite the dimensions that support the claim" — citation obligation |

**Total: 95/100 · All essential pass: YES**

---

## Composite Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Lifecycle + findings-first | **95** | YES |
| 2 | V-03 Matrix-dominant | **92** | YES |
| 3 | V-04 Inertia-primary + conversational | **87** | YES |
| 4 | V-02 GTM-leads | **84** | YES |
| 5 | V-01 Baseline | **78** | NO (C-04 partial) |

---

## Excellence Signals from V-05

**1. FINDINGS section structure mirrors rubric criteria.**
V-05 has 8 numbered FINDINGS sections (Category/Differentiator, Per-Audience, Hierarchy, Matrix, Anti-Positioning, Whitespace, PM Reality Check, Degradation). Each maps directly to a rubric criterion. When the output's structure IS the rubric checklist, omission is visible by inspection.

**2. "STOP and emit" outperforms "if not found, emit".**
V-01–V-04 use conditional language ("if not found, emit"). V-05 uses "STOP and emit before proceeding." The verb "STOP" prevents quiet continuation with degraded output. The rubric's auto-fail for silent skip makes this enforcement verb load-bearing.

**3. Dedicated DEGRADATION NOTE section (8) separates diagnostic from positioning.**
Other variations mix the degradation note into SETUP prose, where the LLM may compress it. V-05 gives it a named FINDINGS section, ensuring it survives to the deliverable.

**4. Citation requirements elevate verifiability.**
V-05 C-10: "cite the dimensions that support the claim." V-03 C-10: "matrix cells where no competitor is H." Both operationalize whitespace via matrix, but V-05 adds a citation obligation that makes the whitespace claim falsifiable by a reviewer.

**5. Double-enforcement on messaging hierarchy (EXECUTE + FINDINGS).**
V-05 enforces C-08 in EXECUTE DESIGN (label requirement) and again in FINDINGS section 3 (structured slot). Single-point enforcement leaves room for the hierarchy to be mentioned but not labeled.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["findings-section structure mirrors rubric criteria — numbered FINDINGS sections map one-to-one to rubric criteria, making omission visible by inspection", "STOP enforcement verb for prior-run handling — stronger than conditional emit; prevents silent continuation with degraded output", "dedicated degradation-note section in FINDINGS — separates diagnostic from positioning output, ensures the note survives LLM compression of setup prose", "citation obligation for whitespace — require citing specific matrix dimensions, making the whitespace claim falsifiable"]}
```
