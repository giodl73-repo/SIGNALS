---
name: signal
description: Show the Signal command index. Lists all available skills organized by namespace with one-line descriptions. Type /signa
allowed-tools: [Read]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Signal — Feature Decision Intelligence
68 skills across 9 namespaces

CAMPAIGNS (start here):
  /rhythm-decide          Full pre-commitment decision campaign
  /rhythm-behavior        Technical simulation campaign
  /rhythm-qa              Design validation campaign
  /evidence               Full evidence campaign
  /blueprint              Complete specification package
  /brief                  Topic narrative campaign

DISCOVERY:
  /discover-competitors   /discover-inertia      /discover-feasibility
  /discover-risk          /discover-brainstorm   /discover-hypothesis
  /discover-websearch     /discover-synthesize   /discover-compare
  /discover-coherence     /discover-orchestrate  /discover-causal

SPECIFICATION:
  /specify-spec  /specify-proposal  /specify-pitch  /specify-commitment

VALIDATION:
  /validate-design  /validate-code  /validate-users  /validate-customers

EVIDENCE:
  /discover-hypothesis  /discover-websearch  /discover-analysis  /discover-synthesize
  /discover-causal      /discover-coherence  /discover-compare   /discover-orchestrate

SIMULATION:
  /simulate-lifecycle  /simulate-request  /simulate-state  /simulate-contract
  /simulate-conversation  /simulate-permissions  /simulate-stress

ADOPTION:
  /validate-adoption  /validate-adoption-blocker  /validate-feedback  /validate-support

NARRATIVE:
  /rhythm-status  /rhythm-story  /rhythm-decide  /rhythm-qa  /rhythm-brief
  /topic-new  /topic-story  /topic-echo  /topic-report  /signal (this)

GOVERNANCE:
  /roles-scan  /roles-build  /roles-chart  /roles-create  /roles-check
  /roles-product-review  /roles-pull-request  /roles-committee  /roles-leaderboard

TOOLS:
  /signal-setup  /signal-health  /signal-layout  /tools-coverage  /tools-preview  /tools-accept

Type /signal <namespace> for skills in that namespace.
Type /signal --bare for the full alphabetical command list.

Note: /scout-compliance scans regulatory constraints before design begins.
/discover-compliance does not exist as a separate skill. For GDPR/SOC2/HIPAA risk
analysis, use /discover-risk -- it includes a COMPLIANCE DIMENSION section that expands
automatically when compliance risk is HIGH or MEDIUM. Use AMEND option 1 ("Focus on
compliance dimension only") to get a compliance-focused risk register.