# Scorecard: listen-adoption — Round 8

**Rubric:** v8 | **Max:** 175 | **Golden threshold:** 80

---

## Final Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01–C-05 | 12 ea | P | P | P | P | P |
| C-06 | 10 | **X** | P | **X** | P | **X** |
| C-07 | 10 | P | **X** | P | P | P |
| C-08 | 10 | P | P | P | P | P |
| C-09 | 5 | X | X | X | X | X |
| C-10 | 5 | X | P | P | X | P |
| C-11 | 5 | X | P | P | P | X |
| C-12 | 5 | X | X | X | X | X |
| C-13–C-14 | 5 ea | X | X | X | X | X |
| C-15 | 5 | X | P | X | P | X |
| C-16–C-24 | 5 ea | X | X | X | X | X |
| C-25 | 5 | P | P | P | P | P |
| **Total** | **175** | **85** | **100** | **95** | **105** | **90** |

---

## Ranking

| Rank | Variation | Score | Distinguishing Property |
|------|-----------|-------|------------------------|
| 1 | **V-04** | 105 | Only variation to pass all three recommended criteria (C-06+C-07+C-08); incumbent-first framing propagates inertia as narrative lens |
| 2 | **V-02** | 100 | Numeric readiness matrix (C-10 PASS); churn register (C-06+C-15 PASS); per-role blockers (C-11 PASS); misses C-07 |
| 3 | **V-03** | 95 | Entry/exit gate structure (C-10 PASS); per-role blocking belief (C-11 PASS); misses C-06 |
| 4 | **V-05** | 90 | Bridge artifact labeling (C-07 PASS); measurable majority threshold (C-10 PASS); misses C-06, C-11 |
| 5 | **V-01** | 85 | Reference baseline; passes C-07/C-08; missing churn register and per-role inertia |

---

## Critical Finding: H/I/J Regression

All five R8 variations dropped the H/I/J sections from R7 that audited C-13/C-14/C-15 by criterion pass condition. SECTION K checks structural completeness (roles, sequence, chasm) but not the aspirational depth criteria. This causes a **45-point cascade** (C-16 fails → C-17 through C-24 all auto-fail). R9 must re-integrate this audit layer into the new content structures.

**Exception worth noting:** every R8 variation successfully incorporated the C-24 falsification-invariant pattern into SECTION K — the "Failure mode: a Fail row whose CORRECTION BLOCK..." phrasing appears in all five. The pattern was absorbed; it just needs to be pointed at the right terminal section.

---

## Excellence Signals (V-04)

**1. Incumbent-first framing as simulation lens** — naming THE INCUMBENT before archetype assignment runs the entire simulation as a displacement story. All phase bodies ask "what does this do to THE INCUMBENT's position?" rather than "what does this do for {{topic}}?" This surfaces role-specific inertia and reversion risk without requiring named ID cross-references, and is the structural reason V-04 alone passes C-06, C-07, and C-11 simultaneously.

**2. Concrete-action constraint in structural field label** — "Retention intervention: [one concrete action that reduces reversion probability]" embeds the C-15 constraint in the field label itself. The model must write an action because that's what fits the slot — the constraint is enforced at generation time rather than caught by a downstream audit.

---

```json
{"top_score": 105, "all_essential_pass": true, "new_patterns": ["Incumbent-first framing as simulation lens: before archetype assignment, name the current workflow or tool being displaced (THE INCUMBENT); run all phase bodies through the displacement lens so every role is defined by what it is protecting rather than what it is adopting; surfaces role-specific inertia and reversion risk without named ID cross-references, and propagates through chasm diagnosis, champion rationale, churn triggers, and interventions", "Concrete-action constraint in structural field labels: when a criterion prohibits a class of responses (e.g., surveillance-only mitigations), embed the positive constraint directly in the field label (e.g., 'Retention intervention: [one concrete action that reduces reversion probability]') rather than adding a prohibition in a separate instruction or downstream audit; the label shapes the model's completion frame before generation begins"]}
```
 described.
V-04: Phase 2 champion network (3 roles) most actively pulling others; follows from displacement
analysis.
V-05: CHAMPION NETWORK SUMMARY table with bridge contribution and adoption delta enabled per
champion.

---

### C-06 — Churn risk per archetype (10 pts)

**Pass condition:** >=2 archetypes; each entry names a trigger and at least one mitigation.

**V-01: FAIL**

PHASE 5 asks "Churn risk if mandate absent: HIGH/MEDIUM/LOW" — names risk level but no
explicit trigger beyond "mandate absent" and no mitigation slot. PHASE 6 asks "Permanent churn
risk: YES/NO" — binary, no trigger, no mitigation. No dedicated churn register.

**V-02: PASS**

TABLE 5 — CHURN RISK REGISTER: columns include "Churn Driver" (explicit trigger) and "Recovery
Intervention" (explicit mitigation). Instruction: "Include all roles with churn risk MEDIUM or
higher." Structural trigger + mitigation requirement enforced by column schema.

**V-03: FAIL**

PHASE 5 asks "Churn risk if mandate is later rescinded: HIGH/MEDIUM/LOW" — trigger implied
(mandate rescinded) but no mitigation slot. PHASE 6 asks for conversion path and permanent churn
risk — no churn register with mitigation. FAIL.

**V-04: PASS**

PART 3 — CHURN RISK REGISTER: explicit "Reversion trigger: [what specific event would send
them back to THE INCUMBENT]" + "Retention intervention: [one concrete action that reduces
reversion probability]." Both trigger and concrete mitigation are structurally required per
entry. Strongest C-06 implementation among the five.

**V-05: FAIL**

PHASE 5 asks "Reversion risk: HIGH/MEDIUM/LOW" — risk level only, no trigger named, no
mitigation. No dedicated churn register.

---

### C-07 — Spread mechanism named per transition (10 pts)

**Pass condition:** Each major transition annotated with a spread mechanism label; at least one
feature-specific mechanism.

**V-01: PASS**

PHASE 1 "Signal they generate: what observable behavior signals their adoption" covers
innovator→early-adopter propagation. PHASE 2 "Spread mechanism: how they share adoption with
peers" is an explicit spread mechanism slot per early-adopter role. PHASE 4 "Proof format:
case study / metric / mandate / default-on / other" names the EA→EM crossing mechanism. PASS.

**V-02: FAIL**

Entirely tabular. TABLE 2 tracks readiness scores per phase per role. No spread mechanism
column. TABLE 4 champions have "Bridge Leverage" but that describes position, not the spread
mechanism format. No transition is annotated with a mechanism label.

**V-03: PASS**

PHASE 2 "Network effect — who they actively pulled toward adoption" names the spread mechanism
for the early-adopter propagation. PHASE 2 EXIT GATE: "early-adopter champions have produced
peer-facing artifacts (case studies, metrics, live demos)" — artifact type is the mechanism.
PHASE 4 "Peer signal that unlocked them — which PHASE 2 champion's evidence they acted on"
names the EA→EM crossing mechanism. PASS.

**V-04: PASS**

PHASE 2 "How does their adoption change what THE INCUMBENT looks like to people who haven't
switched yet?" — the spread mechanism is displacement visibility. PHASE 4 "Which bridge
condition landed for them specifically?" connects EA evidence to EM crossing. The incumbent
framing names the mechanism concretely (showing THE INCUMBENT is becoming the exception). PASS.

**V-05: PASS**

PHASE 2 "Bridge artifact produced: [what they created that GROUP 3 could use]" is an explicit
spread mechanism field per early-adopter role. Champion network: "why their specific artifact
format works for GROUP 3 where GROUP 1 signals did not" — feature-specific mechanism comparison.
PASS.

---

### C-08 — Tabular or structured month view (10 pts)

**All variations: PASS**

V-01: Named phase section headers with explicit month ranges (M1–2 through M15+); scannable
without reading prose. V-02: TABLE 2 is a complete role × phase matrix with month ranges as
column headers — strongest C-08 implementation. V-03: Named phase sections with time windows
and explicit entry/exit gates. V-04: Named phase headers with time windows. V-05: Named phase
section headers with time windows referencing BLOCK A groups.

---

### C-09 — Sensitivity analysis on chasm width (5 pts)

**All variations: FAIL**

Pass condition requires two named scenarios (optimistic/pessimistic) with different adoption
velocities or champion counts.

V-03 and V-04 each have a one-direction analysis ("what happens if the chasm isn't crossed by
Month 8") — this addresses the pessimistic scenario only. The optimistic scenario (what changes
if champion count doubles or bridge condition met early) is absent from all variations. No
variation presents two named scenarios with explicit velocity or count levers.

---

### C-10 — Feedback loop into signal readiness (5 pts)

**Pass condition:** At least 2 measurable adoption signals indicating readiness to proceed.

**V-01: FAIL**

No measurable readiness signals stated. Phase close states are qualitative descriptions, not
trackable thresholds.

**V-02: PASS**

TABLE 2 defines "7+ = active adoption" and "below 4 = resistance/non-adoption" as numeric
thresholds. TABLE 3 "Aggregate readiness at PHASE 2 close" and "Aggregate readiness at PHASE 3
close" are explicitly numeric. Two measurable signals present. PASS.

**V-03: PASS**

PHASE 1 EXIT GATE: "at least one innovator role has generated a public signal (shared finding,
demo, written note) that early-adopter roles can observe." PHASE 4 EXIT GATE: "more than half
of early-majority roles have adopted and at least one has produced a visible normalization
signal." Two measurable gate conditions. PASS.

**V-04: FAIL**

Bridge conditions in PHASE 3 are qualitative ("at least one early-majority-adjacent role has
made public contact with {{topic}}"). No numeric threshold or countable signal. Closest to
measurable: "What happens if the chasm isn't crossed by Month 8" — but this is a risk question,
not a measurable readiness signal. FAIL.

**V-05: PASS**

PHASE 4 close state: "Majority threshold reached: YES / NO (majority = >50% of all 16 roles)"
— explicit numeric threshold. PHASE 3 bridge conditions are explicitly marked MET/UNMET with
responsible roles. Two trackable signals. PASS.

---

### C-11 — Named inertia per archetype (5 pts)

**Pass condition:** At least 3 archetypes have named, feature-specific inertia (not generic).

**V-01: FAIL**

Phase bodies ask about "failure mode" (what would cause abandonment) rather than status-quo
inertia. PHASE 3 has 5 chasm drivers but these are system-level, not per-archetype inertia.
No per-role blocking belief field.

**V-02: PASS**

TABLE 1 includes "Adoption Blocker" per role — covers all 16 roles across all archetypes. The
column structure requires feature-specific answers (generic answers would leave the blocker
field indistinguishable from the archetype definition, which the evaluation design penalizes).
PASS.

**V-03: PASS**

PRELIMINARY table includes "Blocking belief (what they currently believe that prevents
adoption)" per role — explicitly named per-role blocking belief. Covers all archetypes. PASS.

**V-04: PASS**

PART 1 includes "Belief that creates inertia" per role — all 16 roles, all archetypes. The
incumbent framing ("what they'd have to give up") forces feature-specific answers. PASS.

**V-05: FAIL**

BLOCK A has "one-sentence adoption driver" per group member but no blocking belief or inertia
field. PHASE 3 has 5 structural chasm drivers but they are system-level, not per-archetype.

---

### C-12 — No orphan or conditional sections (5 pts)

**All variations: FAIL**

Pass condition requires all 10 criteria (C-01 through C-10) to have a corresponding,
unconditional output section. No variation has a dedicated C-09 section (sensitivity analysis)
or C-10 section (signal readiness feedback loop). All fail C-12 for the same two missing
structural slots.

---

### C-13 — Named inertia as downstream backbone (5 pts)

**Pass condition:** Specific named inertia entries from C-11 cited in >=3 of {C-03, C-04,
C-05, C-06}.

**All variations: FAIL**

V-01, V-05: C-11 fails (no per-archetype inertia), so C-13 fails by dependency.

V-02: TABLE 1 "Adoption Blocker" entries are present but not cross-referenced by name in
TABLE 3 (chasm), TABLE 4 (champions), TABLE 5 (churn), or TABLE 6 (interventions). The tables
are structurally independent with no named citation links. FAIL.

V-03: PRELIMINARY "Blocking belief" entries are not named or cross-referenced in PHASE 3
chasm drivers, the champion network, or interventions. The content may echo the beliefs but
without direct named citation. FAIL.

V-04: PHASE 3 explicitly references "what the early majority roles from Part 1 currently
believe" — this is a reference to the inertia entries from C-11, satisfying C-13 for C-03
(chasm). However, PART 4 interventions reference "THE INCUMBENT's position" (not specific Part
1 beliefs), the champion section (PHASE 2) does not cite Part 1 beliefs, and PART 3 churn
register references THE INCUMBENT (not specific Part 1 entries). Only 1 of 4 downstream
sections makes a named reference. C-13 requires >=3 of 4. FAIL.

---

### C-14 — Champion rationale double-anchored (5 pts)

**Pass condition:** Each champion entry states archetype position reason AND names at least one
EM inertia entry the champion is positioned to overcome.

**All variations: FAIL**

V-01: SECTION 3 "Bridge leverage: [why this role's advocacy unlocks EARLY MAJORITY]" — covers
archetype position but does not require citing a specific EM inertia entry. Single anchor.

V-02: TABLE 4 "Bridge Leverage" — covers archetype position; no EM inertia cross-reference
from TABLE 1 required. Single anchor.

V-03: Champion network requires describing "specific bridge behavior" but does not require
citing the PRELIMINARY table's blocking beliefs. Single anchor.

V-04: PHASE 2 champion network asks "which 3 roles are now most actively pulling others toward
{{topic}}?" — no structural requirement to name the specific EM belief the champion overcomes.
The displacement framing approximates double anchoring but does not require citing a specific
Part 1 inertia entry per champion. Single anchor.

V-05: CHAMPION NETWORK SUMMARY "Bridge Contribution" — archetype position; no BLOCK A
blocking-belief reference required. Single anchor.

---

### C-15 — Churn mitigations are concrete actions, not surveillance (5 pts)

**V-01: FAIL** — No mitigation slot (C-06 fails, no churn register).

**V-02: PASS** — TABLE 5 "Recovery Intervention" column. The table structure requires an
intervention entry per churn risk. "Recovery Intervention" implies action rather than monitoring.
PASS.

**V-03: FAIL** — No churn register with mitigation. FAIL.

**V-04: PASS** — PART 3 "Retention intervention: [one concrete action that reduces reversion
probability]" — the phrase "one concrete action" is embedded in the field label, precluding
surveillance-only entries at design time. Strongest C-15 design: the constraint is in the
prompt structure, not in a downstream audit instruction. PASS.

**V-05: FAIL** — No churn register with mitigation.

---

### C-16 — Self-audit pre-commit for C-13, C-14, C-15 (5 pts)

**All variations: FAIL**

Pass condition: "dedicated self-audit or verification block with at least one check per
criterion among {C-13, C-14, C-15}; each check confirms the specific pass condition or flags
a deficiency."

All five R8 variations contain a SECTION K that audits structural completeness criteria (all
16 roles present, Rogers sequence correct, PHASE 3 non-adoption, chasm drivers present,
champions named, interventions ranked). None of the SECTION K criteria check C-13 (inertia
cited in >=3 downstream sections), C-14 (champion double-anchored to EM inertia), or C-15
(no surveillance-only mitigations). The audit does not reach the aspirational criteria it would
need to reach for C-16 to pass.

This is the structural regression from R7: R7 variations had SECTIONS H/I/J explicitly
checking C-13/C-14/C-15 before SECTION K. R8 variations dropped H/I/J when exploring new
content axes.

---

### C-17 — Dedicated structural slot per aspirational criterion (5 pts)

**All variations: FAIL**

C-17 requires each of C-13, C-14, and C-15 to have a separate, visually separable structural
element. No variation structures itself around C-13/C-14/C-15 as distinct structural slots.
C-17 would require the H/I/J sections (or equivalent) to be reintroduced.

---

### C-18 — Revision obligation on self-audit deficiency (5 pts)

**All variations: FAIL** — auto-fail because C-16 fails.

---

### C-19 — Correction transaction content visible in output (5 pts)

**All variations: FAIL** — auto-fail because C-18 fails.

---

### C-20 — Single named terminal section consolidates gate states (5 pts)

**All variations: FAIL** — auto-fail because C-16 fails.

The SECTION K audit table in each variation is a correctness check (pass/fail per structural
criterion) with a CORRECTION BLOCK mechanism. It does not consolidate "initial audit result,
whether a revision was performed, and final result" for C-13/C-14/C-15. The terminal section
requirement in C-20 is specifically about those three aspirational criteria, not general
structural criteria.

---

### C-21 — Correction content not co-located with gate state (5 pts)

**All variations: FAIL** — auto-fail because C-20 fails.

---

### C-22 — Terminal section contains self-verifying cross-reference invariant (5 pts)

**All variations: FAIL** — auto-fail because C-20 fails.

Note: the SECTION K INVARIANT in each R8 variation is the falsification-aware invariant from
R7 V-04's excellence signal (now C-24). It appears in SECTION K as a correctness invariant
over the correction block mechanism. However, SECTION K in R8 variations is not the "terminal
section" in C-20's sense (which must record initial/revision/final state for C-13/C-14/C-15).
The SECTION K invariant satisfies the structural pattern of C-22 but is applied to the wrong
terminal section — C-20 fails, so C-22 auto-fails.

---

### C-23 — Named verification boundary separates content from audit stage (5 pts)

**All variations: FAIL** — auto-fail because C-16 fails.

V-01 and V-03 use "## SECTION K — AUDIT GATE" as the section header marking the boundary
between content and verification. This is a named marker. However, C-23 fails automatically
if C-16 fails.

---

### C-24 — Self-verifying invariant names its own falsification condition (5 pts)

**All variations: FAIL** — auto-fail because C-22 fails.

Note of interest: every R8 variation includes an INVARIANT in SECTION K that names the
falsification condition. V-01 and V-03 (PHASE 1–6 structure): "Failure mode: a Fail row whose
CORRECTION BLOCK Location references a section that contains no CORRECTION BLOCK, or a
CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant." V-02: "An evaluator
can confirm this invariant by finding a BEFORE field for every Fail row, or refute it by finding
any Fail row whose referenced section is empty or whose CORRECTION BLOCK lacks a BEFORE field."
V-04 and V-05 include similar dual-path statements. The pattern from R7's excellence signal
2 (now C-24) has been successfully incorporated into the audit gate design for all five R8
variations. However, C-24 auto-fails because C-22 fails.

---

### C-25 — Named phase structure architecturally enforces Rogers adoption sequence (5 pts)

**All variations: PASS**

Pass condition: named phase boundaries for Rogers archetypes; chasm explicitly named as
non-adoption interstitial.

V-01: PHASE 1 (INNOVATORS) through PHASE 6 (LAGGARDS) as section headers. PHASE 3 (CHASM)
explicitly: "This is a non-adoption interstitial. No new roles adopt in this phase."

V-02: TABLE 2 column headers: PHASE 1 INNOVATORS (M1–2), PHASE 2 EARLY ADOPTERS (M2–4),
PHASE 3 CHASM (M4–6), PHASE 4 EARLY MAJORITY (M6–9), PHASE 5 LATE MAJORITY (M9–15),
PHASE 6 LAGGARDS (M15+). Column headers are distinct structural elements. PHASE 3 AGGREGATE
rule enforces chasm numerically. PASS.

V-03: PHASE 1 through PHASE 6 with full gate structure. PHASE 3: "THIS IS A NON-ADOPTION
PHASE. No new roles adopt during PHASE 3." Explicit ENTRY GATE and EXIT GATE prevent bypassing
the chasm.

V-04: PHASE 1 through PHASE 6 headers. PHASE 3 (CHASM): "Nobody new is moving. This is not a
delay — it's a different kind of resistance."

V-05: BLOCK B PHASE 1 through PHASE 6 headers as structural gates. PHASE 3: "NON-ADOPTION
PHASE. No roles from any group adopt during PHASE 3."

---

## Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-02 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-04 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-05 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 | 10 | **0** | 10 | **0** | 10 | **0** |
| C-07 | 10 | 10 | **0** | 10 | 10 | 10 |
| C-08 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-10 | 5 | 0 | 5 | 5 | 0 | 5 |
| C-11 | 5 | 0 | 5 | 5 | 5 | 0 |
| C-12 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-13 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-14 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-15 | 5 | 0 | 5 | 0 | 5 | 0 |
| C-16 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-17 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-18 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-19 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-20 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-21 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-22 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-23 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-24 | 5 | 0 | 0 | 0 | 0 | 0 |
| C-25 | 5 | 5 | 5 | 5 | 5 | 5 |
| **Total** | **175** | **85** | **100** | **95** | **105** | **90** |

---

## Ranking

| Rank | Variation | Score | Distinguishing Property |
|------|-----------|-------|------------------------|
| 1 | **V-04** | 105 | Only variation to pass all three recommended criteria (C-06+C-07+C-08); incumbent framing propagates inertia as structural narrative lens; strongest C-15 (concrete-action constraint in field label) |
| 2 | **V-02** | 100 | Numeric readiness matrix (C-10 PASS); dedicated churn register (C-06+C-15 PASS); per-role adoption blockers (C-11 PASS); misses C-07 (no spread mechanism per transition) |
| 3 | **V-03** | 95 | Entry/exit gate structure yields measurable C-10 signals; per-role blocking belief (C-11 PASS); spread mechanism per transition (C-07 PASS); misses C-06 (no churn trigger+mitigation) |
| 4 | **V-05** | 90 | Bridge artifact per early-adopter role (C-07 PASS); measurable majority threshold (C-10 PASS); combined BLOCK A + phase architecture; misses C-06 and C-11 |
| 5 | **V-01** | 85 | Reference baseline; clean phase structure; passes C-07 and C-08; missing churn register (C-06) and per-role inertia (C-11) |

---

## V-01 Gap Analysis

Misses C-06 (no dedicated churn register), C-10 (no measurable readiness thresholds), and
C-11 (no per-role blocking belief or inertia field). The phase structure is sound for sequence
and coverage; the gaps are in churn modeling and inertia depth. Closest to a lean reference
baseline — complete for C-01 through C-08 except C-06.

---

## Shared Gap: C-16 Cascade (all five variations)

All five R8 variations dropped the H/I/J verification architecture from R7. The SECTION K
audit in each variation checks structural completeness (roles, sequence, chasm, champions,
interventions) but not the aspirational criteria C-13/C-14/C-15. This causes a 40-point
cascade failure (C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24 = 45 pts unavailable).

The fix is architectural: R9 variations must either:
(a) Re-integrate H/I/J sections checking C-13/C-14/C-15 by criterion ID within the new content
    structure, or
(b) Expand SECTION K criteria to include C-13/C-14/C-15 explicitly, with named pass conditions
    and correction block instructions for each.

---

## Shared Gap: C-09 (all five variations)

No variation models two named scenarios (optimistic/pessimistic) for chasm crossing with
different velocity or champion count levers. V-03 and V-04 approach a pessimistic scenario
("what if the chasm isn't crossed by Month 8") but not the full two-scenario structure. C-09
requires both directions.

---

## Excellence Signals (V-04)

**1. Incumbent-first framing propagates inertia as a structural narrative lens**

V-04 requires naming THE INCUMBENT before any archetype assignment: "Every role on this team
is already doing something. That something has inertia. The adoption story is really the
displacement story." All six phase bodies then run through the displacement lens:

- PHASE 1: "What specifically pulls them away from THE INCUMBENT this early?"
- PHASE 2: "How does their adoption change what THE INCUMBENT looks like to people who haven't
  switched yet?"
- PHASE 3: "About THE INCUMBENT: [why it still feels safer]"
- PHASE 5: "What made THE INCUMBENT feel unsafe to stick with?"
- PHASE 6: "What's actually keeping them on THE INCUMBENT at this point?"
- PART 3 churn: "Reversion trigger: [what specific event would send them back to THE INCUMBENT]"

This produces role-specific inertia throughout the output without requiring named ID
cross-references. It also makes the chasm visible as a legitimacy gap (THE INCUMBENT retains
perceived legitimacy) rather than as a scheduling gap between phases. V-04 passes C-06, C-07,
and C-11 — the three content-depth criteria that others struggle with — and is the only
variation to pass all three simultaneously.

This pattern generalizes: for any adoption simulation, naming the incumbent workflow before
archetype assignment foregrounds displacement inertia throughout the output. Roles become
defined by what they're protecting rather than what they're adopting. The entire simulation
becomes a displacement narrative, which is more analytically honest than framing adoption as
a positive-only process.

**2. Concrete-action constraint embedded in structural field label**

V-04's PART 3 churn register specifies: "Retention intervention: [one concrete action that
reduces reversion probability]." The phrase "one concrete action" is part of the field label,
not a post-generation audit instruction. This prevents surveillance-only entries at design time
— the model must write an action, not a monitoring instruction, because the label frame
constrains what syntactically fits the slot.

Compare V-02's "Recovery Intervention" (neutral — admits monitoring responses) vs. V-04's
"one concrete action that reduces reversion probability" (prescriptive — shapes response
frame before generation begins). V-04 is the only variation that satisfies C-15 structurally
rather than relying on a downstream audit to catch surveillance-only mitigations.

This pattern generalizes: when a criterion prohibits a class of responses (e.g., "no
surveillance-only mitigations"), embedding the positive constraint ("one concrete action") in
the field label is stronger than adding a prohibition in a separate instruction or audit, because
the label shapes the model's completion frame before generation begins.

---

```json
{"top_score": 105, "all_essential_pass": true, "new_patterns": ["Incumbent-first framing as simulation lens: before archetype assignment, name the current workflow or tool being displaced (THE INCUMBENT); run all phase bodies through the displacement lens so every role is defined by what it is protecting rather than what it is adopting; this surfaces role-specific inertia and reversion risk without requiring named ID cross-references, and naturally propagates through chasm diagnosis (THE INCUMBENT retains legitimacy), champion rationale (advocacy changes how THE INCUMBENT looks to non-adopters), churn triggers (what sends roles back to THE INCUMBENT), and interventions (what weakens THE INCUMBENT's position)", "Concrete-action constraint in structural field labels: when a criterion prohibits a class of responses (e.g., surveillance-only mitigations), embed the positive constraint directly in the field label (e.g., 'Retention intervention: [one concrete action that reduces reversion probability]') rather than adding a prohibition in a separate instruction or downstream audit; the label shapes the model's completion frame before generation begins, making the constraint structurally enforced rather than audited after the fact"]}
```
