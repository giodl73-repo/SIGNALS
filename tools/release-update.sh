#!/usr/bin/env bash
# release-update.sh — Sync new/updated skills to release/ and craftworks-research
# Usage: bash tools/release-update.sh [--push] [--pr]
#
# What it does:
#   1. Syncs signals/*.md -> release/.claude/skills/ (canonical 59 + any new ones)
#   2. Regenerates release/.github/prompts/ from updated skills
#   3. Commits and pushes to signals repo (main)
#   4. Copies release/ to craftworks-research/toolkits/signal/
#   5. --push: pushes craftworks-research branch
#   6. --pr: creates a PR in craftworks-research

set -euo pipefail

SIGNALS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export SIGNALS_ROOT
CR_ROOT="${CR_ROOT:-C:/src/craftworks-research}"
BRANCH="release/signal-$(date +%Y-%m-%d)"
PUSH=false
CREATE_PR=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --push) PUSH=true; shift ;;
        --pr)   CREATE_PR=true; PUSH=true; shift ;;
        *) shift ;;
    esac
done

echo "=== Signal Release Update ==="
echo "  signals root   : $SIGNALS_ROOT"
echo "  craftworks-res : $CR_ROOT"
echo "  branch         : $BRANCH"
echo ""

# ── Step 1: Sync skills from sim-test to release/ ────────────────────────────

echo "--- Step 1: Sync skills to release/"
python << PYEOF
import os, re, shutil, sys

SIGNALS_ROOT = os.environ.get('SIGNALS_ROOT', os.getcwd())

with open(os.path.join(SIGNALS_ROOT, 'signal.skills.yaml')) as f:
    canonical = set(re.findall(r'^- id: (.+)$', f.read(), re.MULTILINE))
canonical.discard('quest-golden')
canonical.discard('quest-rubric')
canonical.discard('quest-score')
canonical.discard('quest-variate')
canonical.add('achievements')

# Also include any new research-* and validate-*/simulate-*/discover-* etc added to signals/
signals_dir = os.path.join(SIGNALS_ROOT, 'signals')
for f in os.listdir(signals_dir):
    if f.endswith('.md') and not f.startswith('README') and not f.startswith('copilot'):
        skill_id = f[:-3]
        canonical.add(skill_id)

src = os.path.join(SIGNALS_ROOT, 'release', '.claude', 'skills')
dst = os.path.join(SIGNALS_ROOT, 'release', '.claude', 'skills')
os.makedirs(dst, exist_ok=True)

updated = added = 0
for skill_id in sorted(canonical):
    src_dir = os.path.join(src, skill_id)
    dst_dir = os.path.join(dst, skill_id)

    # Prefer release/ source if it has newer content
    signals_body = os.path.join(SIGNALS_ROOT, 'signals', f'{skill_id}.md')

    if os.path.exists(signals_body):
        # Update release/ from signals/ source
        os.makedirs(dst_dir, exist_ok=True)
        with open(signals_body, 'r', encoding='utf-8') as f:
            body = f.read().strip()

        # Get frontmatter from existing SKILL.md if present
        existing = os.path.join(dst_dir, 'SKILL.md')
        if os.path.exists(existing):
            with open(existing, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            m = re.match(r'^(---\n.*?---\n.*?# deep.*?\n\n\n)', existing_content, re.DOTALL)
            header = m.group(1) if m else ''
        else:
            header = f'---\nname: {skill_id}\ndescription: ""\nallowed-tools: [Read, Write, Glob]\nparam_set: lean\n---\ndepth: standard\n# quick   -> fast\n# standard -> thorough (default)\n# deep    -> exhaustive\n\n\n'

        new_content = header + body + '\n'
        with open(existing if os.path.exists(existing) else os.path.join(dst_dir, 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write(new_content)

        if not os.path.exists(os.path.join(dst_dir, 'SKILL.md')):
            added += 1
        else:
            updated += 1
    elif os.path.exists(src_dir):
        # Copy from sim-test
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        shutil.copytree(src_dir, dst_dir)
        updated += 1

print(f'Release skills: {updated} updated, {added} added, {len(canonical)} total')
PYEOF

# ── Step 2: Regenerate .github/prompts ───────────────────────────────────────

echo "--- Step 2: Regenerate release/.github/prompts/"
python << PYEOF
import os, re, shutil

SIGNALS_ROOT = os.environ.get('SIGNALS_ROOT', os.getcwd())
skills_dir = os.path.join(SIGNALS_ROOT, 'release', '.claude', 'skills')
output_dir = os.path.join(SIGNALS_ROOT, 'release', '.github', 'prompts')
os.makedirs(output_dir, exist_ok=True)

def get_body(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    m = re.search(r'# deep.*?\n\n\n(.*)', content, re.DOTALL)
    if m: return m.group(1)
    m2 = re.search(r'^---\n.*?---\n(.*)', content, re.DOTALL)
    return m2.group(1) if m2 else content

def get_description(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        c = f.read()
    m = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', c, re.MULTILINE)
    return (m.group(1).rstrip('"\'')[:150] if m else '').replace('"', "'")

count = 0
for folder in sorted(os.listdir(skills_dir)):
    if folder.endswith('.t3'): continue
    skill_md = os.path.join(skills_dir, folder, 'SKILL.md')
    if not os.path.exists(skill_md): continue
    t3_md = os.path.join(skills_dir, f'{folder}.t3', 'SKILL.md')
    body = get_body(skill_md)
    if 't3/SKILL.md' in body and os.path.exists(t3_md):
        t3_body = get_body(t3_md)
        if len(t3_body.encode('utf-8')) <= 8000:
            body = t3_body
    desc = get_description(skill_md)
    with open(os.path.join(output_dir, f'{folder}.prompt.md'), 'w', encoding='utf-8') as f:
        f.write(f'---\nmode: agent\ndescription: "{desc}"\n---\n{body}')
    count += 1

print(f'Prompts: {count} generated')
PYEOF

# ── Step 3: Commit and push signals repo ─────────────────────────────────────

echo "--- Step 3: Commit and push signals repo"
cd "$SIGNALS_ROOT"
git add -A
git commit -m "release: sync skills and prompts $(date +%Y-%m-%d)" || echo "Nothing to commit in signals"
git push origin main

# ── Step 4: Copy to craftworks-research ──────────────────────────────────────

echo "--- Step 4: Copy to craftworks-research"
CR_SIGNAL="$CR_ROOT/toolkits/signal"

# Copy skills
rm -rf "$CR_SIGNAL/.claude/skills"
cp -r "$SIGNALS_ROOT/release/.claude/skills" "$CR_SIGNAL/.claude/"

# Copy prompts
rm -rf "$CR_SIGNAL/.github/prompts"
cp -r "$SIGNALS_ROOT/release/.github/prompts" "$CR_SIGNAL/.github/"

# Copy roles
rm -rf "$CR_SIGNAL/.craft/roles"
cp -r "$SIGNALS_ROOT/.craft/roles" "$CR_SIGNAL/.craft/"

# Copy install scripts
cp "$SIGNALS_ROOT/install/"*.sh "$CR_SIGNAL/install/"

echo "Copied to craftworks-research/toolkits/signal/"

# ── Step 5: Commit and push craftworks-research ──────────────────────────────

cd "$CR_ROOT"

if $PUSH; then
    git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"
    git add toolkits/signal/
    git commit -m "release: Signal toolkit update $(date +%Y-%m-%d)" || echo "Nothing to commit in craftworks-research"
    git push origin "$BRANCH"
    echo "Pushed branch: $BRANCH"

    if $CREATE_PR; then
        gh pr create \
            --title "release: Signal toolkit update $(date +%Y-%m-%d)" \
            --body "Sync Signal skills from signals repo. Run via tools/release-update.sh --pr" \
            --base main
    fi
else
    echo "Skipping push (run with --push to push, --pr to also create PR)"
    git status --short toolkits/signal/ | head -10
fi

echo "=== Release Update Complete ==="
