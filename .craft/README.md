# .craft/

Signal plugin configuration and expert role registry.

## roles/

206 expert role files organized by domain. Each role file defines a named expert persona — title, domain, perspective, and review heuristics. Roles are used by `/crew-review` and `/corp-*` skills to run multi-perspective reviews.

Domain organization:

```
roles/
  engineering/     backend, frontend, infrastructure, security, data
  product/         PM, UX, research, growth, analytics
  leadership/      CTO, CPO, VP Eng, EM, Director
  legal/           compliance, privacy, IP, contracts
  finance/         CFO, FP&A, commercial
  operations/      DevOps, SRE, support, customer success
  ...
```

## Installing roles

```bash
# Install all 206 roles into the current project
./install/install-roles.sh

# Install a domain subset
./install/install-roles.sh --domain engineering
./install/install-roles.sh --domain product
./install/install-roles.sh --domain leadership
```

Roles are installed to `.craft/roles/` in the target project directory.

## Creating new roles

Use the `/roles-create` skill to generate new role files from a title and domain:

```
/roles-create "Principal Security Architect" --domain engineering
```

## Plugin configuration

- **`compiler.yaml`** — forge compiler configuration for Signal
- **`craft.json`** — Signal plugin registration manifest
