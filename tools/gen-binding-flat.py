#!/usr/bin/env python
"""
gen-binding-flat.py -- Generate binding-flat.program.yaml from signal.skills.yaml
Reads golden prompt bodies from signal.skills.yaml and writes the flat binding
program.yaml where each skill is a separate command with its golden prompt body.
"""
import yaml
from pathlib import Path
from datetime import date

REPO = Path(__file__).parent.parent
SKILLS_YAML = REPO / "signal.skills.yaml"
OUTPUT_YAML = REPO / "binding-flat.program.yaml"
QUEST_GOLDEN_DIR = REPO / "simulations" / "quest" / "golden"

def get_golden_body(skill: dict) -> str:
    """Read the golden prompt body from the golden file, or use the description."""
    golden_path = skill.get("golden", "")
    if golden_path:
        full_path = REPO / golden_path
        if full_path.exists():
            content = full_path.read_text()
            # Extract the prompt body section
            if "## The Prompt Body" in content:
                body = content.split("## The Prompt Body")[1]
                body = body.split("## What Made It Golden")[0].strip()
                # Trim to 1024 chars for program.yaml compat (known limitation CF-03)
                if len(body) > 1020:
                    body = body[:1020] + "..."
                return body
    # Fall back to description
    return skill.get("description", "").strip()

def main():
    with open(SKILLS_YAML) as f:
        data = yaml.safe_load(f)

    skills = [s for s in data.get("skills", []) if s.get("namespace") != "meta"]

    golden_count = sum(1 for s in skills if s.get("quest_status", "").startswith("GOLDEN"))
    stub_count = len(skills) - golden_count
    print(f"Skills: {len(skills)} total, {golden_count} golden, {stub_count} stubs")

    commands = []
    for skill in skills:
        body = get_golden_body(skill)
        is_golden = skill.get("quest_status", "").startswith("GOLDEN")
        commands.append({
            "name": skill["id"],
            "description": body,
            "tier": "T1",
            "tools": skill.get("tools", ["Read", "Write", "Glob"]),
            "inputs": skill.get("inputs", ["Topic"]),
            "outputs": skill.get("outputs", ["Signal"]),
            "dependencies": [],
            "_golden": is_golden,
            "_namespace": skill["namespace"],
        })

    output = {
        "version": 1,
        "plugin": "signal",
        "model": "claude-sonnet-4-6",
        "workspace": "signal",
        "target_platform": "claude-code",
        "_generated": date.today().isoformat(),
        "_golden_count": golden_count,
        "_stub_count": stub_count,
        "agents": {"emit": True, "model": "claude-sonnet-4-6", "orchestration": False},
        "tiers": [{"id": "root", "path": ".claude/", "parent": None}],
        "commands": commands,
    }

    # Load entities/workers/roles/state from the base program.yaml
    base_yaml = REPO / "program.yaml"
    if base_yaml.exists():
        with open(base_yaml) as f:
            base = yaml.safe_load(f)
        for key in ["entities", "workers", "roles", "state"]:
            if key in base:
                output[key] = base[key]

    with open(OUTPUT_YAML, "w") as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=120)

    print(f"Written: {OUTPUT_YAML}")
    print(f"Golden skills: {golden_count}/{len(skills)}")
    if stub_count > 0:
        print(f"WARNING: {stub_count} skills still have stub bodies (not GOLDEN yet)")
        print("Run quest-run-all.sh to find golden prompts, then re-run this script.")
    else:
        print("All skills are GOLDEN. Ready to run: craft generate --stage program")

if __name__ == "__main__":
    main()
