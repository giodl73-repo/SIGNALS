| [ Yes / No ] | — | …every new claim is labeled `[intel]` | [ Yes / No ] |
| CALIBRATION | No | N/A — evidence stage | N/A | — | N/A confirmed | N/A |
| FALSIFICATION | No | N/A — no hypothesis yet | N/A | — | N/A confirmed | N/A |
| SEQUENCING | Yes | …producing only evidence, no hypotheses | [ Yes / No ] | — | …no hypothesis appears in Stage 2 output | [ Yes / No ] |
| PROVENANCE | No | N/A — not scope-restricted | N/A | — | N/A confirmed | N/A |

---

Apply expert judgment to ARTIFACT-S1. Characterize evidence patterns, contradictions, strength ratings (well-evidenced / thin / contested), and knowledge gaps. Label every new claim `[intel]`. Do not state hypotheses.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized; patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis in Stage 2 | [ Pass / Fail ] |
| All new claims carry `[intel]` | [ Pass / Fail ] |

**HANDOFF DECLARATION — S2 to S3:**

> **Role passes to: Stage 3 — Hypothesis Architect.**
> I am transferring: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2 (Intelligence Assessment).
> Hypothesis Architect authorized to read: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE: I confirm it IS activated at this boundary.** Obligations activated for ARTIFACT-S1 and ARTIFACT-S2. Every Stage 3 claim must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2}.

---

### Stage 3 — Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S2→S3 complete with PROVENANCE activation | [ Pass / Fail ] |

> **See CARD-S3 (preamble):** Fill COMMITMENT column of DUAL-PHASE-S3 BEFORE writing Stage 3 output. Fill VERIFICATION column AFTER.

#### DUAL-PHASE INVOCATION TABLE — Stage 3

| Rule | [S3 of 5] Applicable? | PRE: I commit to… | COMMITMENT | — | POST: I confirm that… | VERIFICATION |
|------|:--------------------:|------------------|-----------:|:-:|----------------------|:------------:|
| ATTRIBUTION | Yes | …labeling every claim `[hypothesis]` | [ Yes / No ] | — | …every claim is labeled `[hypothesis]` | [ Yes / No ] |
| CALIBRATION | No | N/A — hypothesis stage | N/A | — | N/A confirmed | N/A |
| FALSIFICATION | Yes | …writing a falsification condition for every hypothesis | [ Yes / No ] | — | …every hypothesis has an explicit falsification condition | [ Yes / No ] |
| SEQUENCING | Yes | …opening this stage only after S1 and S2 exits are confirmed | [ Yes / No ] | — | …all hypotheses are grounded in S1+S2 evidence, no pre-evidence assumptions | [ Yes / No ] |
| PROVENANCE | Yes | …tagging every claim `[source: Stage N -- Artifact]` where N ∈ {1,2} | [ Yes / No ] | — | …every claim carries a valid provenance tag | [ Yes / No ] |

---

Declare 3–5 hypotheses. Each: (1) testable claim; (2) prompting evidence cited as `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`; (3) explicit falsification condition; (4) preliminary confidence (High / Medium / Low). Label every claim `[hypothesis]`.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3–5 hypotheses with falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF DECLARATION — S3 to S4:**

> **Role passes to: Stage 4 — Evidence Analyst.**
> I am transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
> **PROVENANCE RULE: activated.** Obligations for ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3. Every Stage 4 claim must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3}.

---

### Stage 4 — Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S3→S4 complete | [ Pass / Fail ] |

> **See CARD-S4 (preamble):** Fill COMMITMENT column of DUAL-PHASE-S4 BEFORE writing Stage 4 output. Fill VERIFICATION column AFTER.

#### DUAL-PHASE INVOCATION TABLE — Stage 4

| Rule | [S4 of 5] Applicable? | PRE: I commit to… | COMMITMENT | — | POST: I confirm that… | VERIFICATION |
|------|:--------------------:|------------------|-----------:|:-:|----------------------|:------------:|
| ATTRIBUTION | Yes | …labeling every new claim `[analysis]` | [ Yes / No ] | — | …every new claim is labeled `[analysis]` | [ Yes / No ] |
| CALIBRATION | Yes | …varying confidence ratings — not all identical | [ Yes / No ] | — | …confidence ratings span at least 2 distinct levels | [ Yes / No ] |
| FALSIFICATION | No | N/A — analysis stage | N/A | — | N/A confirmed | N/A |
| SEQUENCING | No | N/A — post-evidence stage | N/A | — | N/A confirmed | N/A |
| PROVENANCE | Yes | …tagging every claim `[source: Stage N -- Artifact]` where N ∈ {1,2,3} | [ Yes / No ] | — | …every claim carries a valid provenance tag | [ Yes / No ] |

---

For each hypothesis: evaluate against ARTIFACT-S1 and ARTIFACT-S2; assign varied confidence (High / Medium / Low) with justification; note supporting and counter-evidence; label `[analysis]`; attach provenance tags.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses analyzed | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| All claims carry `[analysis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF DECLARATION — S4 to S5:**

> **Role passes to: Stage 5 — Synthesis Director.**
> I am transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4 (Evidence Analysis).
> **PROVENANCE RULE: activated.** Obligations for all four artifacts. Every Stage 5 claim must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3, 4}.

---

### Stage 5 — Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S4→S5 complete | [ Pass / Fail ] |

> **See CARD-S5 (preamble):** Fill COMMITMENT column of DUAL-PHASE-S5 BEFORE writing Stage 5 output. Fill VERIFICATION column AFTER.

#### DUAL-PHASE INVOCATION TABLE — Stage 5

| Rule | [S5 of 5] Applicable? | PRE: I commit to… | COMMITMENT | — | POST: I confirm that… | VERIFICATION |
|------|:--------------------:|------------------|-----------:|:-:|----------------------|:------------:|
| ATTRIBUTION | Yes | …labeling every claim `[synthesis]` | [ Yes / No ] | — | …every claim is labeled `[synthesis]` | [ Yes / No ] |
| CALIBRATION | Yes | …varying final confidence ratings | [ Yes / No ] | — | …final ratings span at least 2 distinct levels | [ Yes / No ] |
| FALSIFICATION | Yes | …giving every hypothesis a final Supported/Refuted/Indeterminate verdict | [ Yes / No ] | — | …every hypothesis has a final verdict | [ Yes / No ] |
| SEQUENCING | No | N/A — synthesis stage | N/A | — | N/A confirmed | N/A |
| PROVENANCE | Yes | …tagging every claim `[source: Stage N -- Artifact]` where N ∈ {1,2,3,4} | [ Yes / No ] | — | …every claim carries a valid provenance tag | [ Yes / No ] |

---

Synthesize: (1) Consensus findings — where web and intelligence agree; (2) Conflicting findings — where they diverge, with strength assessment; (3) Hypothesis verdicts — Supported/Refuted/Indeterminate with final varied confidence ratings; (4) Gaps and open questions; (5) Decision readiness — one sentence naming posture and, if not ready, the specific gap. Label all claims `[synthesis]`. Attach provenance tags.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final Supported/Refuted/Indeterminate verdicts | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| Gaps and open questions surfaced | [ Pass / Fail ] |
| Decision readiness in one sentence | [ Pass / Fail ] |

---

## Variation Axis Summary

| Variate | Primary Axis | Secondary Axes | C-37 Mechanism | C-38 Mechanism |
|---------|-------------|----------------|----------------|----------------|
| V-01 | Lifecycle emphasis | — | Named PRE/POST tables, execution content between | Full form library in preamble; timing directives reference form IDs |
| V-02 | Output format | — | 5 named per-rule cards PRE + 5 named per-rule cards POST | 50 named blank cards in preamble card library |
| V-03 | Phrasing register | — | Named PRE/POST per-rule mini-tables; interrogative column headers | Pre-declared governance questions (interrogative) in preamble |
| V-04 | Lifecycle emphasis | Role sequence (Intel→Web) | Named PRE/POST tables identical to V-01 | Full form library; stage-body directives; sequencing rationale in preamble |
| V-05 | Output format | Phrasing register, lifecycle, inertia framing | Dual-column single table; temporal separation enforced within-table | Reference cards in preamble + timing directives; inertia competitor named |

**C-37 structural property across all 5 variates:** Every variate places execution content physically between the PRE artifact and the POST artifact, making retroactive simultaneous filling structurally visible. V-01/V-04 use standard PRE/POST tables. V-02 uses per-rule cards. V-03 uses per-rule mini-tables. V-05 uses a split-column dual-phase table where commitment and verification columns are in the same table but execution content occupies the temporal space between the two fill events.

**C-38 structural property across all 5 variates:** Every variate pre-declares the invocation apparatus in the preamble as blank templates before Stage 1 executes, AND embeds timing directives in each stage body naming the specific form/card to fill and when. Both components are present in all five variates; the format of those components is what varies.
