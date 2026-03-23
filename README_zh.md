# Gemini Extension Generator 插件

[English Documentation](README.md)

这是一个功能强大、高度模块化的 Gemini CLI 插件，专为自动化搭建、配置和生成完整的 Gemini CLI 扩展、模型上下文协议 (MCP) 服务器、自定义命令、钩子 (Hooks) 以及专属的 Agent 技能而设计。

## ✨ 核心亮点与特性

*   **极致模块化的组件架构：**
    摈弃了传统庞大且脆弱的单文件提示词 (Prompt)，生成逻辑被精准拆分为多个高度专业的执行组件（如 `manifest.md`, `commands.md`, `hooks.md` 等）。这些组件通过 Gemini 原生的 `@file.md` 语法动态注入到主代理技能中，不仅保证了逻辑的干净独立，更彻底杜绝了 AI 幻觉问题。
    
*   **自带纯原生同步知识库 (`/extension:sync`)：**
    该扩展自带一个零外部依赖的 Python 后台脚本，利用 `git clone` 机制，完美绕过了严苛的 GitHub API 下载限流和代理阻隔。只需执行 `/extension:sync` 命令，插件就能毫无障碍地更新自身的 `docs/` 数据库，确保与官方 Gemini CLI 最新文档绝对同步。

*   **注入顶级 Anthropic "Skill Creator" 思想：**
    本插件全面消化并实施了 Anthropic 官方 Claude `skill-creator` 的标准。凡是通过本扩展生成的 Agent 技能，都会天然具备业界顶尖的提示词工程原则，比如：**攻击性描述 (Pushy Descriptions)**（防止模型漏触发），**渐进式目录展开 (Progressive Disclosure)**（节约上下文并支持动态扩展），以及**基础心智理论风格 (Theory-of-Mind Styling)** 取代生硬指令。

*   **快捷的双宏命令系统：**
    *   `/extension:generate [具体需求]`: 瞬间唤醒代理，严格对照本地经过验证的最新文档结构，为你完美构建所需的扩展组件。
    *   `/extension:sync`: 完全依靠本地 shell 钩子原生触发知识库刷新管道，并将更新状态直接输出回对话界面。

## 🚀 快速开始

1. **在本地链接此扩展：**
   将终端导航至该项目根目录，并将插件注册到你本地的 Gemini CLI 环境中：
   ```bash
   gemini extensions link .
   ```

2. **生成你的第一个组件：**
   开启一个新的 Gemini CLI 会话，使用内置宏构建复杂的插件：
   ```bash
   /extension:generate 创建一个新的扩展，使用自定义钩子来总结 git commit diffs
   ```

3. **永远保持框架为最新版本：**
   每当上游的 Gemini CLI 发布了结构性更新时，只需运行：
   ```bash
   /extension:sync
   ```
   这个代码库就会静默刷新其整个知识库，确保你生成的组件时刻使用最新的 CLI 能力。
