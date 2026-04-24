## validate-referee — Round 5 Scorecard

**Rubric**: v4 | **Ceiling**: 135 | All predictions confirmed.

---

### Results

| Variation | Score | Notes |
|-----------|-------|-------|
| V-01 R5 — Compression | **135/135** | All mechanisms intact; compression is lossless |
| V-02 R5 — Front-loaded preamble | **132/135** | C-16: 4/5, C-17: 3/5 — preamble placement insufficient |
| V-03 R5 — REQUIRED-first ordering | **134/135** | C-17: 4/5 — label change ("NOT THIS" vs. "FORBIDDEN") is the reduction |
| V-04 R5 — Phase-end INTEGRITY CHECK | **134/135** | C-16: 4/5 — removal tests at end-of-phase arrive too late |
| V-05 R5 — Canonical production | **135/135** | Deployment candidate |

---

### Key Experimental Results

**V-02 confirms the critical question**: FORBIDDEN spatial proximity is load-bearing. Front-loading all enforcement to a preamble degrades C-17 at Phase 4 and Phase 6 (3/5) because the default generation path is not blocked at the moment it would be taken. Phase 5 holds (well-internalized across rounds). A front-loaded gallery is not equivalent to in-situ vaccination.

**V-03 isolates label vs. ordering**: Ordering is not the load-bearing feature. The C-17 reduction comes from changing the label to "NOT THIS" — the FORBIDDEN label carries independent weight.

**V-04 reveals a proximity distinction**: Phase-end INTEGRITY CHECK blocks preserve C-17 (phase-level proximity is sufficient for FORBIDDEN) but reduce C-16 (removal tests must be proximate inline to catch non-compliance before the dependent output is drafted). FORBIDDEN examples are pre-generation path blockers; removal tests are generation-time checks. Different temporal requirements.

**Three-tier C-17 proximity hierarchy confirmed**: inline = end-of-phase (5/5) >> front-loaded preamble (3/5).

---

### Deployment Decision

- **V-05 R5** — canonical production form, deploy
- **V-01 R5** — compressed alternative (~30% fewer tokens), same compliance, deploy when token budget matters
- **V-02 R5** — negative control, do not deploy

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": []}
```
12 | PASS -- signals/validate/referee/{topic}-referee-{date}.md; all frontmatter fields named |
| C-06 | Journal-specific language | 10/10 | PASS -- PNAS/JCS/CogSci journal standards retained |
| C-07 | Differentiated recommendations | 10/10 | PASS -- "Convergence is a simulation failure" |
| C-08 | Fixes ordered P1->P2->journal | 10/10 | PASS -- Fix 1/2/3 structure preserved |
| C-09 | Strongest referee reflects editorial dynamics | 5/5 | PASS -- "[cite specific fact from their character brief -- reviewing history, not journal policy]" |
| C-10 | Contrarian referee | 5/5 | PASS -- divergence commitment locked in Phase 2 |
| C-11 | Diverger committed before reports | 5/5 | PASS -- Phase 2 DIVERGENCE COMMITMENT block with Brief anchor |
| C-12 | Issue Registry verifiable Done When | 5/5 | PASS -- FORBIDDEN (vague) / REQUIRED (specific) pair inline; self-verification test retained |
| C-13 | Archetype in concrete event | 5/5 | PASS -- FORBIDDEN (disposition) / REQUIRED (event) pair inline; self-verification retained |
| C-14 | Sketch seeds character brief | 5/5 | PASS -- SEED/EXPAND format; FORBIDDEN (new-premise EXPAND) / REQUIRED inline; self-verification retained |
| C-15 | Rationale grounded in brief | 5/5 | PASS -- FORBIDDEN (policy form) / REQUIRED (persona form) inline; self-verification retained |
| C-16 | Self-verification tests embedded | 5/5 | PASS -- all 4 removal tests inline at point of instruction: non-diverger brief, EXPAND, Phase 5 rationale, Done When |
| C-17 | FORBIDDEN with plausible example | 5/5 | PASS -- all 4 FORBIDDEN examples in-situ; examples are fluent-but-wrong (not obviously bad) |

**Total: 135/135**

**Assessment**: Hypothesis confirmed. Compression is lossless when all FORBIDDEN/REQUIRED pairs and self-verification tests are preserved verbatim. The framing commentary around them does not contribute to compliance -- the mechanisms themselves are the entire load-bearing structure.

---

### V-02 R5 -- Front-Loaded Enforcement: Unified Structural Integrity Preamble

**Axis**: Front-loaded enforcement -- all FORBIDDEN examples and removal tests extracted to a STRUCTURAL INTEGRITY RULES preamble; phases reference rule numbers without in-situ enforcement
**Hypothesis**: If C-17 requires spatial proximity to the failure site, Phase 4 and Phase 6 compliance will degrade; Phase 5 will hold (well-internalized across rounds).

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Three complete referee reports | 12/12 | PASS -- format template intact |
| C-02 | Archetypes match journal | 12/12 | PASS -- journal profiles present in Phase 3 |
| C-03 | Final verdict all fields | 12/12 | PASS -- decision, confidence, P1, P2, strongest referee |
| C-04 | Major concerns specific | 12/12 | PASS -- I-NN IDs, journal standards in Phase 4 |
| C-05 | Artifact with frontmatter | 12/12 | PASS -- correct path and frontmatter fields |
| C-06 | Journal-specific language | 10/10 | PASS -- journal standards present |
| C-07 | Differentiated recommendations | 10/10 | PASS -- divergence commitment enforced |
| C-08 | Fixes ordered P1->P2->journal | 10/10 | PASS -- Fix 1/2/3 structure present |
| C-09 | Strongest referee reflects editorial dynamics | 5/5 | PASS -- Phase 5 template includes "[persona form per RULE 4]" |
| C-10 | Contrarian referee | 5/5 | PASS -- Phase 2 commitment intact |
| C-11 | Diverger committed before reports | 5/5 | PASS -- DIVERGENCE COMMITMENT block with Brief anchor |
| C-12 | Issue Registry verifiable Done When | 5/5 | PASS -- RULE 3 explicitly referenced in Phase 6; "[specific criterion per RULE 3]" in template |
| C-13 | Archetype in concrete event | 5/5 | PASS -- RULE 1 specifies event form; Phase 4 directive "write a character brief per RULE 1" is clear |
| C-14 | Sketch seeds character brief | 5/5 | PASS -- RULE 2 specifies SEED/EXPAND; Phase 4 directive explicit |
| C-15 | Rationale grounded in brief | 5/5 | PASS -- RULE 4 has FORBIDDEN (policy) / REQUIRED (persona) pair; Phase 5 rationale confirmed well-internalized across rounds |
| C-16 | Self-verification tests embedded | 4/5 | PARTIAL -- removal tests exist in STRUCTURAL INTEGRITY RULES preamble but not proximate to the instructions they govern; Phase 4 and 6 instructions reference rules by number without repeating the removal-test form; tests are in the prompt but not inline at the structural dependency site |
| C-17 | FORBIDDEN with plausible example | 3/5 | PARTIAL -- FORBIDDEN examples exist and are fluent-but-wrong; front-loading removes proximity to the failure site; Phase 5 holds (prediction confirmed: well-internalized); Phase 4 non-diverger brief and Phase 6 Done When locations are less reliably blocked when FORBIDDEN label is spatially separated from the instruction that triggers the default generation path |

**Total: 132/135**

**Key finding**: V-02 is the decisive experiment. Front-loading enforcement to a preamble degrades C-17 effectiveness at Phase 4 and Phase 6 -- where the model's default path (disposition form, vague Done When) is most fluent. Phase 5 holds because the policy-form failure mode has been vaccinated across multiple rounds and is internalized. The label and the location are both necessary; a front-loaded gallery is not equivalent to in-situ vaccination.

---

### V-03 R5 -- REQUIRED-First Ordering: Correct Form Shown Before FORBIDDEN

**Axis**: Inversion -- every pair shows REQUIRED (example labeled) first, then NOT THIS (wrong form) after
**Hypothesis**: If ordering is not the load-bearing feature, REQUIRED-first will produce equal compliance; if the FORBIDDEN label itself removes the lower-friction path, relabeling to "NOT THIS" will reduce C-17 slightly.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Three complete referee reports | 12/12 | PASS -- format template intact |
| C-02 | Archetypes match journal | 12/12 | PASS -- all journal profiles present |
| C-03 | Final verdict all fields | 12/12 | PASS -- all fields present |
| C-04 | Major concerns specific | 12/12 | PASS -- I-NN IDs, journal standard examples |
| C-05 | Artifact with frontmatter | 12/12 | PASS -- correct path and fields |
| C-06 | Journal-specific language | 10/10 | PASS -- journal standards present |
| C-07 | Differentiated recommendations | 10/10 | PASS -- convergence explicitly prohibited |
| C-08 | Fixes ordered P1->P2->journal | 10/10 | PASS -- Fix 1/2/3 with P1/P2 mapping |
| C-09 | Strongest referee reflects editorial dynamics | 5/5 | PASS -- persona-form instruction in Phase 5 |
| C-10 | Contrarian referee | 5/5 | PASS -- Phase 2 commitment |
| C-11 | Diverger committed before reports | 5/5 | PASS -- DIVERGENCE COMMITMENT with Brief anchor |
| C-12 | Issue Registry verifiable Done When | 5/5 | PASS -- REQUIRED (specific) shown first, "NOT THIS" (vague) after; self-verification inline |
| C-13 | Archetype in concrete event | 5/5 | PASS -- REQUIRED (event) shown first, "NOT THIS" (disposition) after; self-verification inline |
| C-14 | Sketch seeds character brief | 5/5 | PASS -- REQUIRED (SEED-derived EXPAND) shown first, "NOT THIS" (new-premise) after; self-verification inline |
| C-15 | Rationale grounded in brief | 5/5 | PASS -- REQUIRED (persona form) shown first, "NOT THIS" (policy form) after; self-verification inline |
| C-16 | Self-verification tests embedded | 5/5 | PASS -- all 4 removal tests inline; consistent "Self-verification: drop X; if Y still stands alone, rewrite" form |
| C-17 | FORBIDDEN with plausible example | 4/5 | PARTIAL -- examples are plausible-looking and in-situ; "NOT THIS" label departs from the "FORBIDDEN" convention established across R1-R4; C-17 pass condition specifies "labeled FORBIDDEN"; ordering is not the reduction -- label change is |

**Total: 134/135**

**Assessment**: REQUIRED-first ordering is not a significant degradation. The C-17 reduction is attributable to the label change ("NOT THIS" vs. "FORBIDDEN") rather than ordering -- this confirms the FORBIDDEN label itself carries weight independent of example content and ordering. Ordering is not the load-bearing feature; label convention is.

---

### V-04 R5 -- Phase-End Compliance Blocks: Integrity Checks After Each Phase

**Axis**: End-of-phase enforcement collocation -- FORBIDDEN examples and removal tests collected into per-phase INTEGRITY CHECK blocks at the end of each phase
**Hypothesis**: If FORBIDDEN proximity works at the phase level, end-of-phase placement holds C-17; if removal tests must immediately follow the structural dependency instruction, end-of-phase placement reduces C-16.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Three complete referee reports | 12/12 | PASS -- format template intact |
| C-02 | Archetypes match journal | 12/12 | PASS -- journal profiles present |
| C-03 | Final verdict all fields | 12/12 | PASS -- all fields present |
| C-04 | Major concerns specific | 12/12 | PASS -- I-NN IDs, journal standards |
| C-05 | Artifact with frontmatter | 12/12 | PASS -- correct path and fields |
| C-06 | Journal-specific language | 10/10 | PASS -- journal standards present |
| C-07 | Differentiated recommendations | 10/10 | PASS -- convergence prohibited |
| C-08 | Fixes ordered P1->P2->journal | 10/10 | PASS -- Fix 1/2/3 structure |
| C-09 | Strongest referee reflects editorial dynamics | 5/5 | PASS -- "[cite specific fact from their character brief -- reviewing history, not journal policy]" |
| C-10 | Contrarian referee | 5/5 | PASS -- Phase 2 commitment |
| C-11 | Diverger committed before reports | 5/5 | PASS -- DIVERGENCE COMMITMENT with Brief anchor |
| C-12 | Issue Registry verifiable Done When | 5/5 | PASS -- Phase 6 INTEGRITY CHECK has FORBIDDEN (vague) / REQUIRED (specific) with removal test; in-phase proximity holds |
| C-13 | Archetype in concrete event | 5/5 | PASS -- Phase 4 INTEGRITY CHECK has FORBIDDEN (disposition form) labeled; in-phase proximity holds |
| C-14 | Sketch seeds character brief | 5/5 | PASS -- Phase 4 INTEGRITY CHECK has FORBIDDEN (new-premise EXPAND) and removal test; in-phase |
| C-15 | Rationale grounded in brief | 5/5 | PASS -- Phase 5 INTEGRITY CHECK has FORBIDDEN (policy form) and removal test |
| C-16 | Self-verification tests embedded | 4/5 | PARTIAL -- all 4 removal tests present and in-phase; end-of-phase placement means the removal test follows after the structural dependency instruction has been processed; model may draft non-compliant EXPAND before encountering the drop-SEED check in the INTEGRITY CHECK |
| C-17 | FORBIDDEN with plausible example | 5/5 | PASS -- all FORBIDDEN examples in-phase; prediction confirmed: "C-17 intact since FORBIDDEN stays in-phase"; phase-level proximity is sufficient for vaccination |

**Total: 134/135**

**Assessment**: Phase-end INTEGRITY CHECK blocks preserve C-17 (FORBIDDEN at phase level is sufficient) but reduce C-16 (removal tests need to be proximate to the structural dependency instruction). This isolates a meaningful distinction: FORBIDDEN examples are pre-generation path blockers (phase-level proximity sufficient); removal tests are generation-time compliance checks (inline proximity required). The two enforcement mechanisms have different temporal requirements.

---

### V-05 R5 -- Canonical Production Form: Clean Editorial Pass of V-05 R4

**Axis**: Canonical production -- V-05 R4 with consistent FORBIDDEN typography, unified removal-test verb, normalized phase headers, no redundant commentary
**Hypothesis**: Editorial normalization produces 135/135 in cleaner, maintainable form. Deployment candidate.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Three complete referee reports | 12/12 | PASS -- format template: summary, >=2 major, >=1 minor, recommendation |
| C-02 | Archetypes match journal | 12/12 | PASS -- all five journal profiles with full parenthetical characterizations |
| C-03 | Final verdict all fields | 12/12 | PASS -- decision, confidence, divergence check, P1 blockers (reject conditions), P2 conditions (major revision requirements), strongest referee |
| C-04 | Major concerns specific | 12/12 | PASS -- I-NN IDs; most precise journal standard examples across all R5 variations ("Without this, practical significance cannot be assessed"; "in Figure 2 is described but never formally specified") |
| C-05 | Artifact with frontmatter | 12/12 | PASS -- "Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict:" |
| C-06 | Journal-specific language | 10/10 | PASS -- journal standards enforced with fullest formulations |
| C-07 | Differentiated recommendations | 10/10 | PASS -- "Convergence is a simulation failure"; two distinct levels required |
| C-08 | Fixes ordered P1->P2->journal | 10/10 | PASS -- Fix 1/2/3 with addresses, action, done when; P1/P2 explicitly mapped |
| C-09 | Strongest referee reflects editorial dynamics | 5/5 | PASS -- "cite a specific fact from their character brief or EXPAND -- reviewing history, not journal policy" |
| C-10 | Contrarian referee | 5/5 | PASS -- Phase 2 divergence commitment locked |
| C-11 | Diverger committed before reports | 5/5 | PASS -- DIVERGENCE COMMITMENT with all fields including Brief anchor |
| C-12 | Issue Registry verifiable Done When | 5/5 | PASS -- FORBIDDEN (vague) / REQUIRED (specific) inline; self-verification: "drop the specific table number, section identifier, or threshold" |
| C-13 | Archetype in concrete event | 5/5 | PASS -- FORBIDDEN (disposition) / REQUIRED (event) inline; self-verification: "drop the brief; if at least one Major Concern below it would be phrased or weighted identically without it, the brief is not load-bearing -- rewrite it so the report depends on it" |
| C-14 | Sketch seeds character brief | 5/5 | PASS -- SEED/EXPAND; FORBIDDEN (new-premise EXPAND) / REQUIRED inline; self-verification: "drop SEED; if EXPAND still stands alone, it introduced a new premise -- rewrite EXPAND so it depends on SEED" |
| C-15 | Rationale grounded in brief | 5/5 | PASS -- FORBIDDEN (policy form) / REQUIRED (persona form) inline; self-verification: "drop all character briefs; if this rationale is still legible, rewrite it so it depends on a specific fact from the brief" |
| C-16 | Self-verification tests embedded | 5/5 | PASS -- all 4 removal tests inline; unified removal-test verb consistent throughout |
| C-17 | FORBIDDEN with plausible example | 5/5 | PASS -- all 4 FORBIDDEN examples in-situ; consistent bold FORBIDDEN/REQUIRED typography throughout; examples are fluent-but-wrong |

**Total: 135/135**

**Assessment**: Hypothesis confirmed. Editorial normalization produces 135/135 with zero compliance cost. Consistent label typography, unified verb forms, and removal of restatement commentary improve maintainability without affecting mechanism effectiveness. Deployment candidate.

---

### Round 5 Summary

| Variation | Score | Predicted | Delta |
|-----------|-------|-----------|-------|
| V-01 R5 -- Compression | **135/135** | 135 | 0 |
| V-02 R5 -- Front-loaded preamble | **132/135** | 131-133 | on target |
| V-03 R5 -- REQUIRED-first ordering | **134/135** | 134-135 | on target |
| V-04 R5 -- Phase-end INTEGRITY CHECK | **134/135** | 133-135 | on target |
| V-05 R5 -- Canonical production | **135/135** | 135 | 0 |

All essential criteria pass across all five variations. Score differential is entirely in C-16 and C-17.

All predictions confirmed. No surprises.

---

### Experimental Results

**V-02 confirms the key question**: FORBIDDEN spatial proximity is load-bearing. Front-loading all enforcement to a preamble degrades C-17 effectiveness at Phase 4 and Phase 6 (C-17: 3/5) because the model's default generation path (fluent-but-wrong form) is not blocked at the moment it would be generated. Phase 5 holds (well-internalized across rounds). A front-loaded gallery is not equivalent to in-situ vaccination.

**V-03 isolates label vs. ordering**: REQUIRED-first ordering does not degrade compliance (ordering is not the load-bearing feature). The C-17 reduction comes from the label change ("NOT THIS" vs. "FORBIDDEN"), not from showing the correct form first. The FORBIDDEN label carries independent weight.

**V-04 isolates removal-test timing vs. FORBIDDEN timing**: Phase-end INTEGRITY CHECK blocks preserve C-17 (phase-level proximity is sufficient for FORBIDDEN vaccination) but reduce C-16 (removal tests need inline proximity to catch non-compliance before the dependent output is drafted). The two enforcement mechanisms have different temporal requirements: C-16 removal tests are generation-time checks; C-17 FORBIDDEN examples are pre-generation path blockers.

**Three-tier proximity hierarchy for C-17 vaccination** (from V-02, V-04, V-01/V-03/V-05):
1. Inline at point of instruction -- 5/5 (V-01, V-03, V-05)
2. End-of-phase in INTEGRITY CHECK -- 5/5 (V-04, in-phase is sufficient)
3. Front-loaded preamble -- 3/5 (V-02, insufficient for Phase 4 and 6)

---

### Excellence Signals -- Round 5

No new criteria emerge. Round 5 is structural confirmation.

**Signal 1 -- Compression is lossless**: FORBIDDEN/REQUIRED pairs and removal tests are the entire compliance mechanism. Framing prose, explanatory sentences, and redundant reminders do not contribute. Minimum-overhead prompts perform identically to full-commentary prompts when mechanisms are preserved verbatim.

**Signal 2 -- Canonical form normalizes without cost**: Consistent label typography (FORBIDDEN/REQUIRED throughout), unified removal-test verb, removal of explanatory commentary -- zero compliance cost, improved maintainability.

**Signal 3 -- Phase-level vs. inline proximity distinction** (C-16 vs. C-17): FORBIDDEN vaccination works at phase level (in-phase is sufficient); self-verification removal tests work only inline (must be proximate to the structural dependency instruction). These are mechanistically different enforcement types with different proximity requirements.

---

### Deployment Decision

**V-05 R5** is the deployment candidate: 135/135, consistent typography, unified verb forms, no redundant commentary.

**V-01 R5** is a viable compressed alternative: 135/135, approximately 30% fewer tokens, identical mechanism coverage. Use when token budget matters.

**V-02 R5** is the negative control: confirms in-situ placement is required for C-17. Do not deploy.
