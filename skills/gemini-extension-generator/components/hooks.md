### Hooks Lifecycle
Hooks allow extensions to seamlessly intercept CLI behavior (like pre/post run steps).
- Hooks must **strictly** output valid `JSON` only to `stdout`.
- All logging, debugging, or arbitrary strings must go to `stderr`, otherwise the CLI breaks.
- Identify the correct invocation structure for hooks by parsing `docs/hooks/index.md` and `docs/hooks/writing-hooks.md`.
