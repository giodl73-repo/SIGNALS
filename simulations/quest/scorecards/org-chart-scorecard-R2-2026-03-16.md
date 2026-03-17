# Quest Score — `/org-chart` Round 2

**Rubric status:** Timed out — scoring against skill design principles (inertia-first, phase-gated, closed vocabulary, compliance register, minimum-row enforcement).

**Variations received:** V-01, V-02 only. V-03 through V-05 not present in input — partial scoring round.

---

## Reconstructed Rubric

| ID | Criterion | Pts | Essential |
|----|-----------|-----|-----------|
| R1 | Inertia-first — flat case steelmanned before any structure output | 20 | Yes |
| R2 | VERDICT gate — `CAN-OPERATE-FLAT` terminates cleanly; `STRUCTURE-WARRANTED` continues | 15 | Yes |
| R3 | Closed vocabulary — type fields constrained to prescribed set only | 10 | Yes |
| R4 | Phase gate emissions — gated boundary lines present at each transition | 10 | Yes |
| R5 | Minimum row enforcement — self-check present, not just stated | 10 | Yes |
| R6 | DO/DO NOT imperative register maintained throughout | 10 | No |
| R7 | Anti-pattern `cat-N` typed syntax enforced | 10 | No |
| R8 | Quorum fraction format (`N of M member roles`) | 5 | No |
| R9 | Re-assessment trigger — concrete threshold, not "revisit as grows" | 5 | No |
| R10 | Decides/Escalates specificity — no generic ownership phrases | 5 | No |

---

## V-01 — Role Sequence

**Axis:** Classification deferred to after VERDICT (only runs when `STRUCTURE-WARRANTED`)

| ID | Result | Evidence |
|----|--------|----------|
| R1 | **PASS** | Inertia Assessment runs before classification — stronger inertia-first than baseline. Flat case is the first substantive section after role loading. |
| R2 | **PASS** | `CAN-OPERATE-FLAT` → emit stop line and halt. `STRUCTURE-WARRANTED` → emit phase gate and continue to classification. Both paths explicit. |
| R3 | **PASS** | Mechanism types: `Channel / Informal Role / Recurring Cadence / Shared Artifact`. Domain types: `Engineering / PM / Design / Operations / Research / Other`. No additions. |
| R4 | **PASS** | Four gate lines present: ROLES LOADED, INERTIA COMPLETE, ROLES CLASSIFIED, STRUCTURE COMPLETE, CHARTERS COMPLETE. Sequence correct. |
| R5 | **PASS** | "count data rows (excluding header). If count < 2, add rows until count = 2." Active enforcement, not passive instruction. |
| R6 | **PASS** | DO/DO NOT imperatives throughout. No passive voice instructions. |
| R7 | **PASS** | "Each 'Why It Applies Here' cell MUST open with: `[element name] (cat-N)`" enforced. `cat-N` syntax required. |
| R8 | **PASS** | "Quorum: [N] of [M] member roles required for binding decisions" — fraction format preserved. |
| R9 | **PASS** | "Write a re-assessment trigger with a concrete threshold. DO NOT write 'revisit as the team grows.'" Explicit prohibition. |
| R10 | **PASS** | "DO NOT write generic ownership phrases in Decides or Escalates" + "Escalates must name a destination." Specificity enforced. |

**Notes:**
- The deferral of classification is structurally sound. Flat-verdict teams never classify — less waste.
- One minor tension: the Inertia Assessment references "informal roles" without having classified them yet. The phase ordering creates a vocabulary gap that the variation doesn't explicitly address.
- ROLES-LOADED gate label says "INERTIA ASSESSMENT BEGINS" — correct given classification is moved post-verdict. Gate label is consistent.

**Score: 97 / 100**
Deduction: −3 for unaddressed vocabulary gap (roles referenced in inertia section are unclassified at that point; no bridging instruction).

---

## V-02 — Output Format

**Axis:** ASCII hierarchy replaced with ORG READINESS SCORECARD table; density-coded summary block added

| ID | Result | Evidence |
|----|--------|----------|
| R1 | **PASS** | Inertia Assessment section preserved in full, runs before scorecard section. Flat case steelman intact. |
| R2 | **PASS** | VERDICT sub-section 4 preserved with `CAN-OPERATE-FLAT` / `STRUCTURE-WARRANTED` paths. Gate emissions present. |
| R3 | **PASS** | Mechanism types and domain types preserved verbatim from baseline closed sets. |
| R4 | **PARTIAL** | Phase gate after inertia reads `STRUCTURE SECTION BEGINS` — vaguer than baseline `ORG DIAGRAM BEGINS`. The label no longer signals what artifact is being produced. Acceptable given the axis change, but reduces traceability. |
| R5 | **PARTIAL** | Mechanism table has "Minimum two data rows" instruction, but the ORG READINESS SCORECARD itself has no minimum area-row count stated. Enforcement asymmetry: inertia section enforced, structure section not. |
| R6 | **PASS** | DO/DO NOT imperatives maintained throughout visible body. |
| R7 | **UNKNOWN** | Body truncated before ANTI-PATTERN WATCH section. Cannot verify `cat-N` syntax enforcement. −5 applied as incomplete-verification penalty. |
| R8 | **UNKNOWN** | Body truncated before COMMITTEE CHARTERS. Cannot verify quorum fraction format. −2.5 penalty. |
| R9 | **PASS** | Re-assessment trigger in VERDICT sub-section 4 preserved. |
| R10 | **PARTIAL** | Scorecard columns include `Gap` and `Decision Clarity` — good proxy for specificity. But no explicit "DO NOT write generic ownership phrases" instruction appears. Weaker enforcement than baseline. |

**Notes:**
- The scorecard format is a real hypothesis worth testing. Executive artifacts often consume decision-surface data faster from tables than from topology diagrams.
- Loss of ASCII means loss of reporting hierarchy — teams cannot see who reports to whom, only coverage scores per area. This is a genuine tradeoff the variation doesn't acknowledge.
- Phase gate label regression (`STRUCTURE SECTION BEGINS`) is minor but consistent with axis intent.
- Truncation at the charter/anti-pattern sections makes full scoring impossible.

**Score: 68 / 100**
Deductions: −7 (R4 partial) −3 (R5 partial) −7.5 (R7+R8 unknown/truncated) −4 (R10 partial) = −21.5 → rounded to 68.

---

## Ranking (Received Variations)

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01 — Role Sequence | 97 | Yes |
| 2 | V-02 — Output Format | 68 | Yes (R7/R8 truncated, not failed) |

**V-03–V-05:** Not present in input. Round is partial.

---

## Excellence Signals — V-01

- **Deferred classification pattern:** Moving role taxonomy to post-verdict eliminates classification cost for flat teams. Applicable to any phase-gated skill where a downstream section's artifacts are only consumed in one branch.
- **Active enforcement over passive instruction:** "count data rows... If count < 2, add rows" is stronger than "include at least two rows." The model self-audits rather than relying on adherence.
- **Explicit prohibition on vague triggers:** "DO NOT write 'revisit as the team grows'" names the specific failure mode. Anti-patterns enforced by naming them beat anti-patterns enforced by positive instruction alone.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["deferred-classification-post-verdict", "active-row-count-self-audit", "named-prohibition-over-positive-instruction"]}
```
