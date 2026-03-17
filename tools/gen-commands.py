#!/usr/bin/env python
"""Generate COMMANDS.md from signal.skills.yaml"""
import yaml
from collections import defaultdict

with open('C:/src/sim/signal.skills.yaml', encoding='utf-8') as f:
    d = yaml.safe_load(f)

skills = d['skills']
ns_order = ['scout','draft','review','flow','trace','prove','listen','program',
            'topic','quest','mock','crew','corps','campaign']

by_ns = defaultdict(list)
for s in skills:
    by_ns[s.get('namespace','other')].append(s)

ns_desc = {
    'scout':    'Discovery & research — market, competition, feasibility, compliance',
    'draft':    'Specification — spec, proposal, pitch, brainstorm',
    'review':   'Validation — design, users, customers, code',
    'flow':     'Simulation — lifecycle, conversation, triggers, resilience',
    'trace':    'Verification — contracts, state, permissions, components',
    'prove':    'Evidence — hypothesis, research, analysis, synthesis',
    'listen':   'Adoption — feedback, support, adoption curves',
    'program':  'Planning — commitment and staging',
    'topic':    'Narrative — status, story, achievements, index',
    'quest':    'Quest loop — rubric, variate, score, golden prompt',
    'mock':     'Mock artifacts — preview signals before real runs',
    'crew':     'Crew reviews — team-level expert review',
    'corps':    'Corps governance — org chart, ROB, PR review',
    'campaign': 'Campaigns — orchestrated multi-skill workflows',
}

lines = [
    '# Signal — Command Index',
    '',
    f'**{len(skills)} skills** across 14 namespaces. Type `/signal` in Claude Code to see this index interactively.',
    '',
    'Quick start: `/decide` (full decision campaign) or `/competitors` (inertia-first competitive analysis)',
    '',
    '---',
    '',
    '## All commands — alphabetical (bare binding)',
    '',
    '| Bare command | Full name | Namespace | Description |',
    '|---|---|---|---|',
]

all_skills = sorted(skills, key=lambda s: s['id'].split('-',1)[1] if '-' in s['id'] else s['id'])
for s in all_skills:
    sid = s['id']
    stem = sid.split('-',1)[1] if '-' in sid else sid
    ns = s.get('namespace','?')
    desc = (s.get('description','') or '')[:65].rstrip().rstrip('.')
    golden = ' ✓' if s.get('golden') else ''
    lines.append(f'| `/{stem}` | `/{sid}` | {ns} | {desc}{golden} |')

lines += ['', '---', '', '## By namespace', '']

for ns in ns_order:
    ns_skills = by_ns.get(ns, [])
    if not ns_skills:
        continue
    lines.append(f'### {ns}')
    lines.append(f'*{ns_desc.get(ns,"")}*')
    lines.append('')
    lines.append('| Command | Bare | Description |')
    lines.append('|---|---|---|')
    for s in sorted(ns_skills, key=lambda x: x['id']):
        sid = s['id']
        stem = sid.split('-',1)[1] if '-' in sid else sid
        desc = (s.get('description','') or '')[:70].rstrip()
        lines.append(f'| `/{sid}` | `/{stem}` | {desc} |')
    lines.append('')

with open('C:/src/sim/docs/COMMANDS.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'COMMANDS.md: {len(lines)} lines, {len(skills)} skills')
