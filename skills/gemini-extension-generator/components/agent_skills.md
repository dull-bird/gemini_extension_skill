### Agent Skills (`skills/`)
Agent skills expose domain knowledge logic directly to other agents in the user's workspace.
- They belong inside subdirectories of `skills/` (e.g. `skills/security-auditor/SKILL.md`).
- A skill MUST have a YAML frontmatter on the `.md` file with a `name` and `description` to be discovered correctly.
- Ensure the `name` is identical to the enclosing directory.
- For thorough documentation on exactly how skill files behave, refer to `docs/cli/skills.md` and `docs/cli/creating-skills.md`.
