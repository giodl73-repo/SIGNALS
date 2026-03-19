#!/usr/bin/env python
"""
Generate skill body files in C:\src\sim\signals\{skill-id}.md.
Sources (in priority order):
  1. C:\src\craftworks\.claude\skills\{id}.md  -- strip header through first ---
  2. signal.skills.yaml description field       -- fallback
"""

import os
import yaml
import re
import sys

SIM_ROOT = r"C:\src\sim"
CRAFTWORKS_SKILLS = r"C:\src\craftworks\.claude\skills"
SIGNALS_DIR = os.path.join(SIM_ROOT, "signals")
SKILLS_YAML = os.path.join(SIM_ROOT, "signal.skills.yaml")

os.makedirs(SIGNALS_DIR, exist_ok=True)

def extract_body_from_craftworks(path):
    """Strip header comment block and Usage section, return body after first --- separator."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    # Find the first '---' that is a separator (not YAML frontmatter)
    # The header has: # title, blank, > comment, blank, ## Usage, ```, ..., ```, blank, ---
    # We want everything after the first '---' line
    first_sep = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            first_sep = i
            break
    if first_sep is None:
        # No separator found, return full content stripped of header comment lines
        return content.strip()
    # Return everything after the separator
    body = "\n".join(lines[first_sep + 1:]).strip()
    return body

def description_to_body(desc, skill_id, skill_info):
    """Convert a YAML description field to a minimal skill body."""
    if not desc:
        return None
    desc = desc.strip()
    namespace = skill_info.get("namespace", "")
    artifact = skill_info.get("artifact", "")
    return f"{desc}\n\nWrite artifact to: {artifact}"

def main():
    with open(SKILLS_YAML, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    skills = data.get("skills", [])
    written = []
    from_craftworks = []
    from_description = []
    missing = []

    for skill in skills:
        skill_id = skill.get("id")
        if not skill_id:
            continue

        out_path = os.path.join(SIGNALS_DIR, f"{skill_id}.md")

        # Source 1: craftworks flat skill file
        craftworks_path = os.path.join(CRAFTWORKS_SKILLS, f"{skill_id}.md")
        if os.path.exists(craftworks_path):
            body = extract_body_from_craftworks(craftworks_path)
            with open(out_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(body + "\n")
            written.append(skill_id)
            from_craftworks.append(skill_id)
            print(f"  [craftworks] {skill_id}")
            continue

        # Source 2: description field from signal.skills.yaml
        desc = skill.get("description", "")
        if desc and desc.strip():
            body = description_to_body(desc.strip(), skill_id, skill)
            with open(out_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(body + "\n")
            written.append(skill_id)
            from_description.append(skill_id)
            print(f"  [description] {skill_id}")
            continue

        # No body available
        missing.append(skill_id)
        print(f"  [MISSING] {skill_id}")

    print(f"\n=== Summary ===")
    print(f"Total skills: {len(skills)}")
    print(f"Written: {len(written)}")
    print(f"  From craftworks skills: {len(from_craftworks)}")
    print(f"  From description:       {len(from_description)}")
    print(f"Missing:                  {len(missing)}")
    if missing:
        print(f"  Missing IDs: {missing}")

if __name__ == "__main__":
    main()
