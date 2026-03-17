## Quest Score — prove-publish R1

### Scoring Methodology

Each variation scored on 10 criteria. Essential = 12 pts each (60 total), Recommended = 10 pts each (30 total), Aspirational = 5 pts each (10 total). Max = 100.

Note: V-01 has full prompt text; V-02 through V-05 are evaluated from summaries — scores reflect design intent, not observed output.

---

### V-01: Skeptic-First Role Sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Phase 3 lists all 8 sections in order with explicit requirements per section |
| C-02 | Hypothesis resolved | **PASS** (12/12) | `HYPOTHESIS VERDICT: [Confirmed / Refuted / Partially confirmed...]` required before findings list; evasion-proof phrasing |
| C-03 | Evidence traceable | **PASS** (12/12) | Citation format `[Claim] [source: artifact-name.md, section]` required; uncitable claims routed to Limitations |
| C-04 | Findings synthesized | **PASS** (12/12) | Explicit: "answer 'what does this mean?' not 'what happened?'" — minimum 3 findings, numbered |
| C-05 | Principles actionable | **PASS** (12/12) | Accepted forms listed (`Always X`, `When Y, do Z`); vague summaries named as failing; numbered P-01, P-02 |
| C-06 | Panel review, 2+ roles | **PASS** (10/10) | Domain Expert + Practitioner, each with substantive critique and 1–10 score |
| C-07 | Abstract standalone | **PASS** (10/10) | Must state (a) question, (b) method, (c) finding; <200 words; "as if it's the only thing a future researcher reads" |
| C-08 | Future Work concrete | **PASS** (10/10) | Min 2 items; failing vs passing form examples given; "specific enough a team could start without clarification" |
| C-09 | Principles cross-referenced | **PASS** (5/5) | "Link each to the finding(s) that produced it: `[from F-02]`" — explicit traceability chain |
| C-10 | Cold-start readable | **PARTIAL** (3/5) | Artifact disclosure (Phase 1) orients new readers; no explicit jargon-definition requirement |

**V-01 Total: 96/100**

---

### V-02: Pre-Printed Skeleton

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Structural form — filling it forces completeness by construction |
| C-02 | Hypothesis resolved | **PARTIAL** (8/12) | Likely has a verdict field but no explicit forced-sentence described in summary |
| C-03 | Evidence traceable | **PARTIAL** (8/12) | "Inline minimum-item requirements" implies citation anchors; unconfirmed depth |
| C-04 | Findings synthesized | **PARTIAL** (7/12) | Template enforces structure, not interpretation quality; no synthesis gate described |
| C-05 | Principles actionable | **PARTIAL** (8/12) | Numbered slots likely; format enforcement (rule vs summary) unclear from summary |
| C-06 | Panel review, 2+ roles | **PARTIAL** (7/10) | Review block presumably in template; reviewer roles and critique depth unspecified |
| C-07 | Abstract standalone | **PASS** (10/10) | Word-count constraint structural; section slot ensures presence |
| C-08 | Future Work concrete | **PASS** (10/10) | Minimum-count slots enforce quantity; specificity unguarded |
| C-09 | Principles cross-referenced | **PARTIAL** (3/5) | Cross-reference fields possible in skeleton; not confirmed |
| C-10 | Cold-start readable | **PARTIAL** (2/5) | No cold-start framing described |

**V-02 Total: 75/100**

---

### V-03: Evidence-First Lifecycle

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PARTIAL** (7/12) | No section-completeness enforcement; lifecycle focus only |
| C-02 | Hypothesis resolved | **PARTIAL** (8/12) | Sequential gate before Findings helps but no explicit verdict sentence |
| C-03 | Evidence traceable | **PASS** (12/12) | "Citation-audited before Findings begins" — strongest single enforcement of C-03 across all variations |
| C-04 | Findings synthesized | **PASS** (12/12) | "Cite-before-conclude" ordering structurally separates evidence from conclusion; eliminates rationalization drift |
| C-05 | Principles actionable | **PARTIAL** (6/12) | No principles format guidance in summary |
| C-06 | Panel review, 2+ roles | **FAIL** (0/10) | Not mentioned in summary |
| C-07 | Abstract standalone | **PARTIAL** (5/10) | No abstract guidance |
| C-08 | Future Work concrete | **PARTIAL** (5/10) | No future work guidance |
| C-09 | Principles cross-referenced | **PARTIAL** (2/5) | No cross-reference mechanism described |
| C-10 | Cold-start readable | **PARTIAL** (2/5) | No cold-start guidance |

**V-03 Total: 59/100**

---

### V-04: Conversational Transcript

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PARTIAL** (7/12) | Sections not structurally enforced; conversational drift risk |
| C-02 | Hypothesis resolved | **PASS** (12/12) | "Hypothesis verdict is a literal committed sentence the Lead Author must speak before any finding" — strongest C-02 phrasing across V-02/V-04/V-05 |
| C-03 | Evidence traceable | **PARTIAL** (7/12) | Conversational format makes citation anchors awkward; no explicit citation format |
| C-04 | Findings synthesized | **PARTIAL** (8/12) | First-person narration can express conclusions; not explicitly enforced |
| C-05 | Principles actionable | **PARTIAL** (7/12) | Rules in first-person register can still be action-oriented; format unguarded |
| C-06 | Panel review, 2+ roles | **PARTIAL** (6/10) | Roles present (Skeptic, Lead Author) but no panel review section described |
| C-07 | Abstract standalone | **PARTIAL** (6/10) | No standalone-utility guidance; word count unguarded |
| C-08 | Future Work concrete | **PARTIAL** (6/10) | Specificity unguarded in conversational format |
| C-09 | Principles cross-referenced | **PARTIAL** (2/5) | No cross-reference mechanism |
| C-10 | Cold-start readable | **PARTIAL** (3/5) | First-person narration naturally explains context; jargon not explicitly flagged |

**V-04 Total: 64/100**

---

### V-05: Role Sequence + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PARTIAL** (9/12) | Skeptic-first implies structure; non-standard `## Status Quo` section adds 9th section risk |
| C-02 | Hypothesis resolved | **PARTIAL** (9/12) | Skeptic pre-flight + NEW SIGNAL tagging implies tracking; no explicit verdict sentence |
| C-03 | Evidence traceable | **PARTIAL** (9/12) | Skeptic watches evidence tracing; no citation format specified |
| C-04 | Findings synthesized | **PASS** (12/12) | BASELINE MATCH vs NEW SIGNAL tagging is a forced interpretation classifier per finding |
| C-05 | Principles actionable | **PARTIAL** (7/12) | No explicit principles format guidance |
| C-06 | Panel review, 2+ roles | **PARTIAL** (7/10) | Skeptic + implied roles; explicit panel review not described |
| C-07 | Abstract standalone | **PARTIAL** (7/10) | Status Quo section aids orientation; abstract not specifically guided |
| C-08 | Future Work concrete | **PARTIAL** (6/10) | Not specifically addressed |
| C-09 | Principles cross-referenced | **PARTIAL** (2/5) | No cross-reference mechanism |
| C-10 | Cold-start readable | **PASS** (5/5) | Explicitly stated: "Status Quo section gives new readers the context they'd otherwise have to infer" |

**V-05 Total: 73/100**

---

### Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01: Skeptic-First Role Sequence | **96/100** | Yes |
| 2 | V-02: Pre-Printed Skeleton | 75/100 | No (C-02, C-04 partial) |
| 3 | V-05: Role Sequence + Inertia | 73/100 | No (C-02, C-05 partial) |
| 4 | V-04: Conversational Transcript | 64/100 | No (C-01, C-03 partial) |
| 5 | V-03: Evidence-First Lifecycle | 59/100 | No (C-06 fail) |

---

### Excellence Signals from V-01

These patterns drove the performance gap:

1. **Artifact inventory disclosure gate** — Phase 1 forces enumeration of what was loaded before writing begins. Prevents papers built from memory with post-hoc evidence. No other variation does this.

2. **Forced hypothesis verdict sentence** — `HYPOTHESIS VERDICT: [Confirmed / Refuted / Partially confirmed under X but not Y]` required as a literal line before the findings list. Grammatically eliminates verdict-evasion; "the evidence is mixed" fails the format check.

3. **Skeptic pre-flight as risk naming, not gating** — Skeptic predicts failure before authoring. This is not a block but a structural alert; it primes the author to address the predicted gap. The prediction remains visible during writing.

4. **Citation format with routing rule** — Uncitable claims are routed to Limitations, not deleted. This prevents evidence-laundering (moving weak claims to Findings when they should be qualified) while keeping the paper honest.

5. **Principles linked to finding IDs** — `[from F-02]` creates a traceability chain: evidence → finding → principle. No other variation closes this loop. This is what earns C-09 (the hardest aspirational criterion).

---

```json
{"top_score": 96, "all_essential_pass": true, "new_patterns": ["artifact-inventory-disclosure-before-authoring", "forced-hypothesis-verdict-sentence-before-findings", "uncitable-claims-routed-to-limitations-not-deleted"]}
```
