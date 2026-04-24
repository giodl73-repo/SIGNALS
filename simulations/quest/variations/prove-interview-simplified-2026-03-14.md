**1787 → 1420 words = 367 removed = 20.5% reduction.** Now in target range.

---

## Simplified Prompt

```
# prove-interview

---

## STEP 0 — ROSTER

Declare the complete roster before beginning any interview.

**Subject 0 — The Incumbent**
| Field | Value |
|-------|-------|
| Role | Incumbent: {{incumbent_name}} — the solution currently in place |
| Prior knowledge | Speaks in the vocabulary of teams that have built workflows around it: reliability claims, integration arguments, switching-cost calculations, institutional familiarity, ecosystem lock-in |
| Stakeholder type | Non-human baseline |

**Subject 1**
| Field | Value |
|-------|-------|
| Role | [job title or stakeholder type] |
| Prior knowledge | [state this person's current relationship with the Incumbent: how long used, what function relied on, prior experience with alternatives, disposition toward switching] |
| Stakeholder type | [technical / business / buyer / user — pick one] |

**Subject 2**
| Field | Value |
|-------|-------|
| Role | [job title or stakeholder type — non-overlapping with Subject 1] |
| Prior knowledge | [state this person's current relationship with the Incumbent: how long used, what function relied on, prior experience with alternatives, disposition toward switching] |
| Stakeholder type | [technical / business / buyer / user — must differ from Subject 1] |

Minimum 2 human subjects from non-overlapping stakeholder types.

---

## STEP 1 — INCUMBENT INTERVIEW

**Prior knowledge block** (required immediately before the first INTERVIEWER turn — not inline, not merged with Q&A):
{{incumbent_name}} has been in place since [time]. Teams that depend on it justify it with: [claim 1], [claim 2], [claim 3]. Primary switching-cost argument: [argument]. Rough edge sometimes acknowledged internally: [limitation].

**Transcript:**

INTERVIEWER: [question — invite the Incumbent to state its primary claim for {{topic}}]
SUBJECT: [Incumbent answers — reliability language, switching-cost framing, integration justifications, institutional memory; first-person as the voice of teams that trust it; specific claims, not abstract reassurances]

INTERVIEWER: [question — probe a specific claimed strength with a concrete scenario]
SUBJECT: [Incumbent defends or qualifies in-voice; word choice distinguishable from any human subject]

INTERVIEWER: [question — ask what would need to be true for a team to move away from it]
SUBJECT: [switching-cost framing required; reveal at least one team assumption being carried without examination]

Minimum 3 INTERVIEWER turns. The Incumbent voice must be distinguishable from all human subjects without reading the role label.

**Surprise — Incumbent:**
One SUBJECT turn where the Incumbent's answer revealed a team assumption being carried without examination. Quote the SUBJECT turn verbatim. State what assumption was surfaced.

**Evidence Pull — Incumbent:**
| IE-# | Claim | Quote from SUBJECT turn | Confidence |
|------|-------|-------------------------|------------|
| IE-1 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW |
| IE-2 | [claim label] | "[verbatim Incumbent SUBJECT quote — not paraphrased, not summarized]" | HIGH / MEDIUM / LOW |

Minimum 2 rows. Confidence required on every row. Quote column must contain verbatim SUBJECT text.

---

## STEP 1b — TENSION LOG

Promote minimum 2 rows from the Incumbent Evidence Pull to the Tension Log. The Source quote in each Tension Log entry IS the verbatim Incumbent SUBJECT turn already captured in the corresponding Evidence Pull row — do not re-extract, do not paraphrase, do not rephrase.

| T-# | IE-# | Tension item (the claim to be tested by human subjects) | Source quote (verbatim — must match IE-# Quote column character for character) | Status |
|-----|------|----------------------------------------------------------|--------------------------------------------------------------------------------|--------|
| T-1 | IE-1 | [tension framing of IE-1 claim — phrased as a testable proposition human subjects can confirm or dispute] | "[verbatim Incumbent SUBJECT quote — identical to IE-1 Quote column]" | OPEN |
| T-2 | IE-2 | [tension framing of IE-2 claim] | "[verbatim Incumbent SUBJECT quote — identical to IE-2 Quote column]" | OPEN |

Do not begin Step 2 until the Tension Log has at least 2 entries and every Source quote matches its IE-# row.

---

## STEP 2 — HUMAN INTERVIEWS

For each subject:

**Prior knowledge block** (required immediately before the first INTERVIEWER turn):
[Subject role] has [used / evaluated / observed] the Incumbent {{incumbent_name}} for [time]. Current disposition: [positive / skeptical / neutral / pragmatic]. Primary use case: [function]. What they rely on the Incumbent for that they could not easily replicate: [specific dependency]. Primary concern about switching: [concern].

**Transcript:**

INTERVIEWER: [opening question grounded in this subject's role and prior knowledge — references at least one detail from the prior knowledge block]
SUBJECT: [answer in this role's voice — word choice, concerns, workflow references, and domain artifacts must reflect this specific role; the answer must be distinguishable from the Incumbent and from all other human subjects without reading the role label]

INTERVIEWER: [follow-up that probes or challenges]
SUBJECT: [answer — role-specific vocabulary and concerns required]

INTERVIEWER: [question that directly names at least one Tension Log entry] "T-[N] — the current approach claims [tension item]. Does that match what you actually encounter in your context?"
SUBJECT: [answer — addresses T-N by name; may confirm, dispute, or qualify the claim]

[TENSION LOG UPDATE: after this interview, record the verbatim SUBJECT turn for each T-entry addressed; update Status to ADDRESSED. Leave OPEN entries that were not addressed. Do not advance to the next subject until updates are recorded.]

Minimum 3 INTERVIEWER turns per subject. At least one turn must directly name a Tension Log entry by T-number — referencing the tension thematically without the T-number does not satisfy this requirement.

**Surprise — [Subject role]:**
One SUBJECT turn that contradicted the prior assumption stated in the Roster for this subject. Quote the SUBJECT turn verbatim. State what was assumed (cite the Roster entry) and what was revealed.

**Evidence Pull — [Subject role]:**
| HE-# | Claim | Quote from SUBJECT turn | Confidence |
|------|-------|-------------------------|------------|
| HE-1 | [claim label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW |
| HE-2 | [claim label] | "[verbatim SUBJECT quote]" | HIGH / MEDIUM / LOW |

Minimum 2 rows. Confidence required on every row. Quote column must contain verbatim SUBJECT text.

---

## STEP 3 — SYNTHESIS

Do not begin synthesis until: (a) all human interviews are complete, (b) all Tension Log entries have been updated, and (c) all Evidence Pulls are populated with Confidence on every row.

Every synthesis item — every pattern, contradiction, tension resolution entry, Inertia Verdict Matrix row, and assumption update — must cite a direct quote from a SUBJECT turn. No synthesis claim without a source.

### Pattern
At least one signal that appeared across two or more subjects. For each pattern, cite a verbatim SUBJECT turn per subject that evidences it. The Incumbent is eligible as a subject.

### Contradiction
At least one direct conflict between two subjects. Cite both SUBJECT turns verbatim. State the conflict explicitly.

### Tension Resolution

| T-# | IE-# | Final status | Resolution (verbatim SUBJECT turn or explicit declaration) |
|-----|------|-------------|-----------------------------------------------------------|
| T-1 | IE-1 | RESOLVED / OPEN | "[verbatim human SUBJECT turn that resolved this]" or "No human subject addressed T-1 directly" |
| T-2 | IE-2 | RESOLVED / OPEN | "[verbatim human SUBJECT turn that resolved this]" or "No human subject addressed T-2 directly" |

### Inertia Verdict Matrix
Process each Incumbent Evidence Pull row by IE-number. Adjudicate each Incumbent claim against human subject testimony row-by-row.

| IE-# | Incumbent claim | Verdict | Human SUBJECT turn (verbatim) |
|------|----------------|---------|-------------------------------|
| IE-1 | [claim label from Incumbent Evidence Pull IE-1] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote evidencing verdict]" or "No human subject spoke to IE-1 — UNADDRESSED" |
| IE-2 | [claim label from Incumbent Evidence Pull IE-2] | SURVIVED / CONTRADICTED / UNADDRESSED | "[verbatim human SUBJECT quote evidencing verdict]" or "No human subject spoke to IE-2 — UNADDRESSED" |

Column rules:
- **IE-#**: the exact row identifier from the Incumbent Evidence Pull
- **Incumbent claim**: the claim label from the Evidence Pull — not paraphrased
- **Verdict**: exactly one of SURVIVED / CONTRADICTED / UNADDRESSED — no other values permitted
- **Human SUBJECT turn**: verbatim quote from a human SUBJECT turn for SURVIVED or CONTRADICTED; for UNADDRESSED, the explicit declaration "No human subject spoke to IE-# — UNADDRESSED" — no cell may be blank, no row may be omitted

Every Incumbent Evidence Pull row must appear in the Inertia Verdict Matrix.

### Prior Assumption Revisited
One assumption from the Roster that was revised by the interviews. Quote the SUBJECT turn that caused the revision. State what the Roster assumed and what is now understood instead.
```

---

## Simplification Report

### Essential criteria verification

| Criterion | Mechanism preserved | Pass? |
|-----------|-------------------|-------|
| C-01 Role declaration | ROSTER tables with Role row per subject, declared before any transcript | YES |
| C-02 Prior knowledge framing | "Prior knowledge block (required immediately before first INTERVIEWER turn)" in both STEP 1 and STEP 2 | YES |
| C-03 Persona-voiced answers | SUBJECT turn instructions ("reliability language… institutional memory; first-person as the voice of teams"; "word choice, concerns, workflow references and domain artifacts must reflect this specific role; distinguishable without reading the role label") | YES |
| C-04 Evidence extraction | Evidence Pull tables with minimum 2 rows and verbatim quote column, both Incumbent and human subjects | YES |
| C-05 Questions explicit | INTERVIEWER: [question…] format with full template text for all 3 minimum turns in both interview phases | YES |

**All essential criteria still pass: YES**

---

### What was removed and why

| # | Removed text | Why |
|---|-------------|-----|
| 1 | YAML frontmatter block (`---/skill:/topic:/date:…`) | No criterion depends on YAML metadata; all subject information is in the ROSTER |
| 2 | Entire opening description paragraph (73 words) | Pure summary of what the sections below already enforce; C-15/C-16/C-13 architecture described there is fully enforced by STEP 1b and STEP 3 structure |
| 3 | "Every field is required." (STEP 0) | Not a criterion; each table field is self-describing; the individual sections carry their own constraints |
| 4 | "Subject 0 (the Incumbent) does not count toward the human subject minimum." | Redundant — Subject 0 is labeled "Non-human baseline" and "Minimum 2 human subjects" already implies non-human subjects don't count |
| 5 | "The institutional voice: teams frame their work around its strengths; switching carries [specific cost]." | C-03 already covered by the three SUBJECT turn templates directly below, which explicitly require switching-cost framing and institutional memory vocabulary |
| 6 | "— something the team believes is true but has not verified" (3rd SUBJECT turn) | Redundant elaboration of "assumption being carried without examination" already stated in the same clause |
| 7 | "Specific reliability claims, integration arguments, switching-cost calculations, and institutional knowledge references are required." (STEP 1 closing) | The three SUBJECT turn templates above already require these vocabulary categories; this closing sentence restates them without adding constraint |
| 8 | "and why it was not previously examined" (Surprise — Incumbent) | C-06 pass condition requires only that the surprise is "specific and linked to a Q&A pair"; this extra clause is beyond the criterion |
| 9 | "These rows are the structural spine of the Tension Log (Step 1b) and the Inertia Verdict Matrix (Step 3 synthesis)." | Explanatory meta-commentary; the sections themselves enforce the coupling — this sentence describes architecture but adds no constraint |
| 10 | "Structural requirement: the Source quote column must match the Quote column of the referenced IE-# row verbatim. Any deviation fails the promotion requirement." (STEP 1b) | Fully covered by the table header: "Source quote (verbatim — must match IE-# Quote column character for character)"; sentence repeats the table constraint in prose |
| 11 | "The IE-# column is required; it makes the promotion traceable." (STEP 1b) | The preceding sentence already requires the Source quote IS the verbatim Incumbent SUBJECT turn; the table column itself enforces traceability structurally |
| 12 | "this block appears before the INTERVIEWER: line, not inline with Q&A, not merged with answers" (STEP 2 parenthetical) | Restates "required immediately before the first INTERVIEWER turn" in three different words; the first phrase is sufficient for C-02 positioning |
| 13 | "Do not begin Step 1 until all subjects are declared." | Redundant with "Declare the complete roster before beginning any interview" — the Incumbent interview IS an interview |
| 14 | "Run each human subject in sequence." | Not required by any criterion; the step structure and "For each subject:" template imply sequential execution |
| 15 | "No inference without a turn." (STEP 3 preamble) | Restatement of "No synthesis claim without a source" two clauses earlier in the same sentence |
| 16 | "— do not describe it as 'tension' without quoting both sides" (Contradiction) | Redundant — "Cite both SUBJECT turns verbatim" + the global C-12 requirement above already enforces this |
| 17 | "The IE-# column traces each tension back to the Incumbent Evidence Pull row it was promoted from." (Tension Resolution) | Explanatory; the IE-# column header and STEP 1b structure already establish the linkage |
| 18 | "— this is the same row set that seeded the Tension Log" (Inertia Verdict Matrix) | C-17 requires this coupling annotation at Evidence Pull construction time, not in synthesis; the annotation here is misplaced redundancy |
| 19 | "This section is structurally distinct from the Pattern and Contradiction sections — it adjudicates the Incumbent's specific claims, not general cross-subject signals." | Meta-commentary; the section name "Inertia Verdict Matrix" plus the table structure make the distinction self-evident |
| 20 | "The structural coupling: Evidence Pull IE-# rows → Tension Log T-# entries… The Evidence Pull is built once and propagates through both downstream artifacts." (47 words at end of IVM) | Architectural summary restating what STEP 1b, STEP 1b table headers, and STEP 3 IVM instructions already constrain; adds no new requirement |
| 21 | "— the two tables share the same IE-# space" (column rules) | Explanatory aside; "the exact row identifier from the Incumbent Evidence Pull" already specifies origin; the IE-# sharing is implied by using the same identifiers |
| 22 | "Produce a verdict for every row." (IVM preamble) | Covered by "Every Incumbent Evidence Pull row must appear in the Inertia Verdict Matrix" two paragraphs later |

---

### Word count summary

| Metric | Value |
|--------|-------|
| Original word count | 1787 |
| Simplified word count | 1420 |
| Words removed | 367 |
| Reduction | **20.5%** |
| All essential criteria pass | **YES** |

The reduction stays at the conservative end of the target range by design: every retained sentence serves at least one criterion (including recommended C-06 through C-08 and aspirational C-09 through C-18). Nothing with criterion coverage was removed — only text that restates, summarizes, or explains what the structural templates already enforce.

```json
{"simplified_word_count": 1420, "original_word_count": 1787, "all_essential_still_pass": true}
```
