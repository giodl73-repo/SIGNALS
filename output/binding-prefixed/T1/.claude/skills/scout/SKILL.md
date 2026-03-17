---
name: scout
description: "Scout namespace -- 8 skills for discovery and research.

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your topic and the most relevant scout skill will run.
"
allowed-tools: [Read, Write, Glob, Grep, WebSearch, WebFetch]
param_set: standard
---
Auto-detect domain from repo context. Do not prompt unless context absent. THE PRIMARY COMPETITOR: assess "none / status quo" first -- why do teams do nothing? Score threat always HIGH. Inertia is the primary competitor. Named competitors (5-8): feature overlap, positioning, technical moat, distribution, overall threat (HIGH/MEDIUM/LOW each). Use WebSearch to verify at least one claim per major competitor, cite source inline. FINDINGS as a brief: (1) The Primary Competitor -- why inertia is the real threat, (2) The Whitespace -- what no competitor owns, (3) The Table Stakes -- what any entrant must have, (4) The Competitive Matrix -- supporting evidence, (5) --mode risk -- cost of not acting, for exec audiences. AMEND: 3 specific adjustments each with what changes in the output.

Write artifact to: simulations/scout/competitors/{topic}-competitors-{date}.md
