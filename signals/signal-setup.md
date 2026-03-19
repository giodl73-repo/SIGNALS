You are running /signal-setup.

Add Signal context to CLAUDE.md so every session knows Signal is installed and how to use it.

---

## STEP 1 -- CHECK FOR EXISTING CLAUDE.MD

Read CLAUDE.md if it exists. Check if Signal context is already present (look for "Signal" or "/discover-competitors" or "signals/").

If Signal context already exists:
  Display: "Signal context already in CLAUDE.md -- no changes needed."
  Stop.

---

## STEP 2 -- WRITE SIGNAL CONTEXT BLOCK

Append the following block to CLAUDE.md (create CLAUDE.md if it does not exist):

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Available namespaces**:
- discover: /discover-competitors, /discover-feasibility, /discover-inertia, /discover-hypothesis, /discover-risk
- specify: /specify-spec, /specify-proposal, /specify-pitch, /specify-commitment
- validate: /validate-design, /validate-users, /validate-customers, /validate-code
- simulate: /simulate-lifecycle, /simulate-request, /simulate-state, /simulate-contract
- prove: (via discover-hypothesis, discover-websearch, discover-synthesize, discover-analysis)
- listen: /validate-adoption, /validate-feedback, /validate-support
- rhythm: /rhythm-status, /rhythm-decide, /rhythm-story, /rhythm-qa, /rhythm-brief
- roles: /roles-scan, /roles-build, /roles-check, /roles-product-review, /roles-pull-request

**Inertia rule**: Inertia wins the default choice. Every /discover-competitors run assesses
"none / status quo" first. If you cannot explain why inertia loses, the feature does not have
a clear value case.

**Artifacts**: All skills write to signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Use /tools-coverage {topic} to check coverage gaps.
Use /signal-health to check workspace health.
```

---

## STEP 3 -- CONFIRM

Display:
```
Signal context added to CLAUDE.md.

First commands to try:
  /discover-competitors <your-feature>   Scout inertia and named competitors
  /specify-spec <your-feature>           Write a spec from intent
  /tools-coverage <your-feature>         Check what signals are missing
  /signal-health                         Check workspace health
```
