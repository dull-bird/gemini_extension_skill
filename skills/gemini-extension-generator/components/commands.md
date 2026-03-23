### Custom Commands (`commands/*.toml`)
Shortcuts and macros are created via `.toml` files located cleanly in the `commands/` directory.
- `prompt` multiline strings are strictly required in the TOML definition.
- `description` fields are optional but recommended.
- To execute host binaries, explicitly use `!{...}` block syntax.
- User input arguments are accessible through the `{{args}}` binding.
- Read `docs/cli/custom-commands.md` carefully to see exactly how arguments and injections are escaped.
