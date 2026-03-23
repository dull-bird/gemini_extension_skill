### Agent Skills (`skills/`)
Agent skills expose domain knowledge logic directly to other agents in the user's workspace.
- They belong inside subdirectories of `skills/` (e.g. `skills/security-auditor/SKILL.md`).
- A skill MUST have a YAML frontmatter on the `.md` file with a `name` and `description` to be discovered correctly.

#### Anthropic Official Skill Building Philosophies
When crafting the inner content of any `SKILL.md`, you must closely adhere to Anthropic's proven framework (which you should locate at `docs/references/anthropic-skill-creator.md`). Key rules to enforce on the generated skills:
1. **Pushy Descriptions**: Make the YAML description aggressive and heavily loaded with keywords. Define EXACTLY when the skill should trigger so language models do not "undertrigger" the capability.
2. **Progressive Disclosure**: Keep the generated `SKILL.md` under 500 lines. Delegate heavy static assets or massive code templates to a sibling `references/` folder internally for the skill to read dynamically.
3. **Imperative, Explain-Why Styling**: Avoid overwhelming repetitive "MUSTs" in the generated prompt. Use theory of mind, explain *why* instructions are structured that way, and supply exact, rigid `Expected Output` formatting templates.

For authoritative structural mapping of how Gemini CLI inherently parses these agent directories, always refer back strictly to `docs/cli/skills.md` and `docs/cli/creating-skills.md`.
