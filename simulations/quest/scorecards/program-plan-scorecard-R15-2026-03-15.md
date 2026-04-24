Now I have enough to score. Let me evaluate all five variations systematically.

---

# program:plan — R15 Score Report
**Rubric**: v15 (C-01 through C-49 · 4 essential / 3 recommended / 42 aspirational · max 300)
**Date**: 2026-03-16 · **Round**: 15

---

## Baseline Assessment (Shared Across All Five)

All five R15 variations share the same template skeleton, BAD PLAN architecture, and correction table. The shared evaluation covers the large majority of criteria.

**Essential (shared): 4/4 PASS**

| C | Status | Evidence |
|---|--------|----------|
| C-01 | PASS | Valid YAML scaffold with `program:` top-level, `stages:` list, each stage has `name:` + `skills:` |
| C-02 | PASS | Echo pre-positioned at template end with `auto: true  # REQUIRED: must be true`, `skills: []  # REQUIRED: empty`, `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` |
| C-03 | PASS | Skill catalog (9 namespaces, 47 skills) provided; correction table maps every invented skill form to valid catalog entry |
| C-04 | PASS | Three-field gate structure (`gate_fail:`/`gate_pass:`/`gate:`) at every non-echo zone; compound `{stage-id}::{artifact-type} >= N AND {namespace}:{skill}` format enforced |

**Recommended (shared): 3/3 PASS**

| C | Status | Evidence |
|---|--------|----------|
| C-05 | PASS | `# requires: <artifact> from Zone: <name> (C-05)` at zone-header and skills: line; dep order violation in BAD PLAN (`review:design` before any `draft:spec`); correction table rows for C-05 |
| C-06 | PASS | Step 2 PASS/FAIL table: `discovery` vs `scout_and_draft_stage`; BAD PLAN names `# WRONG C-06`; correction table maps namespace-labels to intent-labels |
| C-07 | PASS | Opening: "the program is a plan, not an executor"; `strategy:` field pre-populated in YAML template; `# WRONG C-07` in BAD PLAN |

**Aspirational (shared) — C-08 through C-46:**

| C | Status | Evidence |
|---|--------|----------|
| C-08 | PASS | `>= N` in gate_pass: template; Step 5a explicitly: "At least one gate must include `>= N`" |
| C-09 | PASS | Step 2 forces breadth → depth → synthesis arc declaration before catalog opens; echo terminal consumer drives backward derivation |
| C-10 | PASS | BAD PLAN gate_fail: "done" / gate_pass: "discovery::scout-feasibility >= 2 ..." is a BAD/GOOD essential-criterion contrast pair |
| C-11 | PASS | Echo pre-positioned in YAML template (C-02 structural enforcement); three-field gate_fail:/gate_pass:/gate: structurally embedded (C-04) |
| C-12 | PASS | C-01: template + BAD PLAN structural failure; C-02: echo in template + BAD PLAN; C-03: catalog + correction table; C-04: gate_fail:/gate_pass: + BAD PLAN — all four essential have ≥2 independent anchors |
| C-13 | **PARTIAL** | Arc phases declared in Step 2 and embedded in YAML template; lifecycle zones described as bullet list under bold header — NOT as top-level `## Breadth` / `## Depth` structural headers. Document primary divisions are CONSTRUCTION ORDER, CORRECTION TABLE, protocol section — not arc phases. Partial credit: arc present in ordering rules and zone references but top-level structure is indexed/sectioned, not arc-navigated |
| C-14 | PASS | Echo slot: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` / `# REQUIRED: must be true` / `# REQUIRED: empty` — three co-located annotations naming prohibited actions |
| C-15 | PASS | Full multi-stage BAD PLAN block: two non-echo stages + wrong echo; structural failures across C-01 through C-07 |
| C-16 | PASS | `# WRONG C-04`, `# WRONG C-06`, `# WRONG C-03`, `# WRONG C-05`, `# WRONG C-02`, `# WRONG C-07` criterion tags in BAD PLAN block |
| C-17 | PASS | `gate_fail:`/`gate_pass:` as YAML template fields at every non-echo zone provides per-zone inline PASS/FAIL gate examples |
| C-18 | PASS | Correction table: 17 wrong-to-correct pairs (all five show >= 17 rows covering C-01 through C-07) |
| C-19 | PASS | BAD PLAN covers C-05 (`# WRONG C-05`) and C-06 (`# WRONG C-06`) and C-07 (`# WRONG C-07`) alongside essential-tier tags |
| C-20 | PASS | `# requires: <artifact> from Zone: <prior-zone-name> (C-05)` at skills: placeholder in dep zones |
| C-21 | PASS | `# check correction table: skill names` at skills: fields; `# check correction table: stage names` at name:; `# check correction table: gate values` at gate: |
| C-22 | PASS | BAD PLAN and correction table both cover C-05, C-06, C-07 |
| C-23 | PASS | Dual-position: `# requires: ...` at zone-header comment AND at skills: placeholder line, in uniform `# requires: <artifact> from Zone: <name> (C-05)` syntax |
| C-24 | PASS | `gate_fail:` and `gate_pass:` appear as actual YAML sibling keys (not comments) in YAML template at every non-echo zone |
| C-25 | PASS | Every `gate_fail:` carries `# WRONG C-04: Why: execution-history check, not artifact-verifiable` — `Why:` at each FAIL field |
| C-26 | PASS | `# WRONG C-04` inline at each `gate_fail:` field in YAML template |
| C-27 | PASS | Uniform `# requires: <artifact> from Zone: <prior-zone-name> (C-05)` syntax across all dep zones and both positions |
| C-28 | PASS | `gate:` as named sibling alongside `gate_fail:` / `gate_pass:` at each zone |
| C-29 | PASS | Correction table rows for C-05 (dep order), C-06 (namespace-label stage names), C-07 (executor framing) |
| C-30 | PASS | skills: line at dep zones carries both `# requires: <artifact> from Zone: <name> (C-05)` AND `# check correction table: skill names` independently |
| C-31 | PASS | BAD PLAN block header explicitly claims "all 7 criteria (C-01 through C-07)"; block body has `# WRONG C-0N` for all seven |
| C-32 | PASS | `gate:` sibling field carries `# check correction table: gate values` at every non-echo zone |
| C-33 | PASS | Every dep zone: three-field gate + C-26 tag (a), production gate + correction bridge (b), dual-position dep reminder in uniform syntax (c), independent dep+bridge at skills: (d) — all four mechanisms present |
| C-34 | PASS | `gate_fail: "..."  # WRONG C-04: Why: execution-history check, not artifact-verifiable` — criterion tag AND Why: both at `gate_fail:` field position |
| C-35 | PASS | BAD PLAN has `# WRONG C-05/C-06/C-07` (C-31 ✓) AND correction table has rows for C-05/C-06/C-07 (C-29 ✓) — dual format recommended coverage |
| C-36 | PASS | BAD PLAN header claims "all 7 criteria (C-01 through C-07)" — does not falsely restrict to essential-only |
| C-37 | PASS | Each wrong-format `name:` in BAD PLAN (`scout_and_draft`, `prove_and_review`) carries `# WRONG C-06` at the `name:` field itself |
| C-38 | PASS | BAD PLAN header: "All 7 criteria covered (C-01 through C-07) — essential and recommended violations" — affirmative full-scope claim |
| C-39 | PASS | Each invented/invalid skills entry (`gather-requirements`, `make-a-plan`, `run-analysis`) carries `# WRONG C-03` at the skills-list line |
| C-40 | PASS | C-34 PASS (compound gate_fail: annotation) + C-29 PASS (recommended-tier correction table) |
| C-41 | PASS | BAD PLAN header maps ≥3 of 4 annotation types (C-26/gate_fail:, C-37/name:, C-39/skills:, C-38/header) to criterion numbers |
| C-42 | PASS | "FIELD CO-LOCATION PRINCIPLE" (or equivalent named section) with structured table before BAD PLAN; three field types organized with criterion, required tag, co-location rule |
| C-43 | PASS | YAML template carries `strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"` — non-empty pre-populated string |
| C-44 | PASS | C-41 index entries state exact tag strings: `# WRONG C-04: Why: ...`, `# WRONG C-06`, `# WRONG C-03` per entry |
| C-45 | PASS | C-41 index entries back-reference the protocol/co-location section by name; C-42 section forward-references specific BAD PLAN entry numbers (`See entry (N) in BAD PLAN header below`) |
| C-46 | PASS | BAD PLAN block ends with explicit footer: `# [PROTOCOL] -- C3: exit verified` / `# ... exit OK` / `# ... Exit Verification complete` confirming co-location family present |

---

## Per-Variation Assessment: New Criteria C-47 / C-48 / C-49

### V-01 — Compact Table Protocol (SCAN PROTOCOL)

| C | Status | Evidence |
|---|--------|----------|
| C-47 | PASS | 4-column table C-41 entry: `C-26 \| gate_fail: \| # WRONG C-04: Why: execution-history check, not artifact-verifiable \| SCAN PROTOCOL decl. above` — full Why: text in table cell, not abbreviated |
| C-48 | PASS | C-41 direction: 4th column per row = `SCAN PROTOCOL decl. above` (per-entry). C-42 direction: FIELD CO-LOCATION PRINCIPLE table has "BAD PLAN entry" column: `Entry (1) in BAD PLAN header below` / `Entry (2)` / `Entry (3)` — per-row forward-refs to specific entry numbers |
| C-49 | PASS | Named protocol: `## SCAN PROTOCOL`; BAD PLAN header: `# SCAN PROTOCOL -- C1: Header Index`; footer: `# SCAN PROTOCOL -- C3: exit verified` — all three components labeled under shared protocol name |

**V-01 Aspirational: 41 PASS + 1 PARTIAL (C-13) = 205 + 2.5 = 207.5 pts**
**V-01 Composite: 60 + 30 + 207.5 = 297.5 / 300** — GOLDEN ✓

---

### V-02 — Protocol-First Structure (BOUNDED BLOCK PROTOCOL)

| C | Status | Evidence |
|---|--------|----------|
| C-47 | PASS | Prose-indented entry: `# C-26: gate_fail: carries # WRONG C-04: Why: execution-history check, not artifact-verifiable` — full Why: text in prose entry, followed by `(rule declared in BOUNDED BLOCK PROTOCOL above)` |
| C-48 | PASS | C-41 direction: each entry individually ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)` — per-entry back-refs. C-42 direction: FIELD CO-LOCATION PRINCIPLE table "BAD PLAN entry" column carries `See entry (1) in BAD PLAN header below` etc. per row |
| C-49 | PASS | Named protocol: `## BOUNDED BLOCK PROTOCOL` appears FIRST in document; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL -- Component 1: Header Entry Index`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification (C-46) complete` |

**V-02 Composite: 297.5 / 300** — GOLDEN ✓

*Distinguishing axis:* Protocol section appears before all construction content. Models encounter the bounded-unit architecture before any arc or catalog instructions, framing subsequent steps as filling out a known protocol rather than accumulating ad-hoc content.

---

### V-03 — Enumeration Format (BLOCK SCAN PROTOCOL)

| C | Status | Evidence |
|---|--------|----------|
| C-47 | PASS | Numbered list entry: `(1) gate_fail: → C-04 (C-26) → tag: # WRONG C-04: Why: execution-history check, not artifact-verifiable` — full Why: text in numbered item |
| C-48 | PASS | C-41 direction: each entry ends with `(rule #N in BLOCK SCAN PROTOCOL above)` — per-entry numbered back-refs. C-42 direction: FIELD CO-LOCATION PRINCIPLE numbered list carries `*(instance #N in BAD PLAN header below)*` per item |
| C-49 | PASS | Named protocol: `## BLOCK SCAN PROTOCOL`; BAD PLAN header: `# BLOCK SCAN PROTOCOL (P1) -- Header Entry Index`; footer: `# BLOCK SCAN PROTOCOL (P3): exit OK` |

**V-03 Composite: 297.5 / 300** — GOLDEN ✓

*Distinguishing axis:* Numbered-list format produces checklist orientation. C-41 entry `(1)` corresponds to C-42 item `*(instance #1)*` — the numbering creates a direct cross-reference path.

---

### V-04 — Fused Why/Navigation (BLOCK SPECIFICATION PROTOCOL)

| C | Status | Evidence |
|---|--------|----------|
| C-47 | PASS | Entry (1): `# C-26: gate_fail: carries # WRONG C-04: Why: execution-history check, not artifact-verifiable` with full Why: text embedded in the back-reference phrase |
| C-48 | PASS | C-41 direction: entry (1) ends with fused phrase: `(this Why: clause -- execution-history check, not artifact-verifiable -- is the rationale declared in BLOCK SPECIFICATION PROTOCOL above for the gate_fail: co-location rule)` — each entry has per-entry back-ref. C-42 direction: table "BAD PLAN header entry" column: `See entry (1)/(2)/(3) in BAD PLAN header below` per row |
| C-49 | PASS | Named protocol: `## BLOCK SPECIFICATION PROTOCOL`; BAD PLAN header: `# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Entry Specification`; footer: `# BLOCK SPECIFICATION PROTOCOL -- Component 3: Exit Verification (C-46)` |

**V-04 Composite: 297.5 / 300** — GOLDEN ✓

*Distinguishing axis:* Full Why: text is embedded INSIDE the per-entry back-reference phrase — the Why: clause IS the navigation phrase. Single uninterrupted annotation delivers criterion, tag form, rationale, and section pointer in one read.

---

### V-05 — Extended Protocol with Formal Sub-Specifications (BLOCK SPECIFICATION PROTOCOL)

| C | Status | Evidence |
|---|--------|----------|
| C-47 | PASS | Component 1 protocol section explicitly specifies as sub-requirement `(b)`: "For entries referencing an annotation that carries a Why: clause, the entry must include the complete Why: text verbatim: `Why: execution-history check, not artifact-verifiable`. The abbreviated form `Why: ...` fails this sub-requirement." Entry (1) in BAD PLAN satisfies this verbatim. |
| C-48 | PASS | Component 1 protocol section explicitly specifies as sub-requirement `(c)`: "Each individual entry ends with its own pointer to this section: `(rule declared in BLOCK SPECIFICATION PROTOCOL above)`. A single shared section-level pointer for all entries does not satisfy this sub-requirement." Each BAD PLAN entry individually ends with `(rule declared in BLOCK SPECIFICATION PROTOCOL above)`. C-42 table per-row forward-refs: `See entry (1)/(2)/(3) in BAD PLAN header below`. |
| C-49 | PASS | Named protocol: `## BLOCK SPECIFICATION PROTOCOL`; BAD PLAN header: `# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Entry Specification (C-41 + C-44 + C-47 + C-48)`; footer: `# BLOCK SPECIFICATION PROTOCOL -- Component 3: Exit Verification (C-46) / (a) Co-location complete / (b) C-47 verified: full Why: text present in entry (1)` |

**V-05 Composite: 297.5 / 300** — GOLDEN ✓

*Distinguishing axis:* C-47 and C-48 are named sub-requirements (b) and (c) within Component 1's formal protocol definition — a model encounters them as stated protocol obligations before reading any BAD PLAN entry. The exit footer verifies C-47 as a named item `(b)` alongside co-location completeness `(a)`, making Why: verification an explicit exit-check rather than an implicit property.

---

## Composite Scores and Ranking

| Variation | Essential | Recommended | Aspirational | Total | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 60 | 30 | 207.5 | **297.5** | YES |
| V-02 | 60 | 30 | 207.5 | **297.5** | YES |
| V-03 | 60 | 30 | 207.5 | **297.5** | YES |
| V-04 | 60 | 30 | 207.5 | **297.5** | YES |
| V-05 | 60 | 30 | 207.5 | **297.5** | YES |

**All five tie at 297.5/300. Sole deduction: C-13 PARTIAL across all five.**

C-13 PARTIAL rationale (consistent): Lifecycle zones described as bullet-list under bold header; document top-level structural headers are section titles (CONSTRUCTION ORDER, CORRECTION TABLE, protocol section, FIELD CO-LOCATION PRINCIPLE, BAD PLAN) — not arc phases. Arc is structurally enforced in Step 2 ordering and embedded in YAML template zones, satisfying the partial-credit condition ("arc present in ordering rules but top-level structure is indexed").

**Qualitative ranking** (identical scores, differentiated by architectural novelty):
1. **V-05** — C-47/C-48 as formal sub-requirements in protocol spec + dual-item footer verification (new patterns)
2. **V-04** — Why/Navigation fusion (new pattern)
3. **V-02** — Protocol-first structural sequence (novel placement, strongest framing effect)
4. **V-01** — Tabular compression (maximum density without loss)
5. **V-03** — Enumeration format (checklist orientation; closest to V-01 in novelty)

---

## Excellence Signals

Patterns from the top-ranked variations that are NOT yet captured in any rubric criterion (C-01 through C-49):

### Signal 1 — V-05: C-47/C-48 Declared as Named Sub-Requirements of Component 1 (Protocol-Obligation Elevation)

The Component 1 protocol section in V-05 explicitly names C-47 and C-48 as sub-requirements (b) and (c) within the Component 1 definition — not as rubric criteria a model might optionally honor, but as stated protocol obligations:

> "(b) Include the full unabbreviated Why: text where applicable (C-47) ... The abbreviated form `Why: ...` fails this sub-requirement."
> "(c) Include a per-entry back-reference to this section (C-48) ... A single shared section-level pointer does not satisfy this sub-requirement."

The distinction from C-49 (which requires components to be labeled under a shared protocol name): C-49 requires naming; this pattern requires C-47/C-48 to be explicitly specified as numbered sub-requirements within Component 1's definition. A model reading the protocol section encounters C-47/C-48 as hard obligations before encountering any BAD PLAN entry.

### Signal 2 — V-05: Dual-Item C-46 Footer (Co-Location + C-47 Verification)

V-05's exit footer verifies two named items rather than one:

> "(a) All annotation types from Component 1 confirmed present in block above.  
> (b) C-47 verified: full Why: text present in entry (1) — not truncated."

Current C-46 requires only co-location completeness verification. V-05 adds explicit C-47 verification as a named exit-check item, closing a second scan loop: a model filling the block can confirm not just that annotation types are present but that the Why: clause in entry (1) is unabbreviated.

### Signal 3 — V-04: C-47/C-48 Co-Satisfaction via Fused Annotation Unit

V-04 embeds the full Why: text (C-47) INSIDE the per-entry back-reference phrase (C-48):

> `(this Why: clause -- execution-history check, not artifact-verifiable -- is the rationale declared in BLOCK SPECIFICATION PROTOCOL above for the gate_fail: co-location rule)`

The Why: content IS the navigation pointer content. A model cannot include the C-48 back-ref without also including C-47's rationale — the two criteria share a single textual instantiation. This differs from all other variations where C-47 and C-48 are implemented as parallel independent elements on the same entry line.

---

```json
{"top_score": 297.5, "all_essential_pass": true, "new_patterns": ["V-05: C-47/C-48 declared as formal named sub-requirements (b) and (c) within Component 1 protocol definition — protocol-section elevation makes them stated obligations, not discoverable properties", "V-05: C-46 exit footer verifies C-47 full Why: presence as named item (b) alongside co-location completeness item (a) — dual-item exit verification", "V-04: full Why: text fused into per-entry back-reference phrase, making C-47 and C-48 co-satisfied by a single annotation unit — inseparable Why/navigation fusion"]}
```
