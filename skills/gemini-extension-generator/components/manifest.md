### Extension Manifests (`gemini-extension.json`)
All extension folders must contain a `gemini-extension.json` manifest file at the root.
- The `name` should be dash-cased and perfectly match the directory name.
- It can define custom tools, MCP servers, and context file routing via `contextFileName`.
- You MUST fetch `docs/extensions/writing-extensions.md` or `docs/extensions/reference.md` to see the exact valid JSON structure before you write it.
