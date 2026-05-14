## Install into Skill-Enabled AI Editors

[English](../en-US/installation.md) | [中文](../zh-CN/installation.md) | [日本語](../ja-JP/installation.md)

Recommended: use the official skills.sh installer (the skills CLI) to install into a Skill-enabled AI editor (Trae / Qwen / Kiro, etc.). The installer can auto-detect available agents and place `visual-spec` into the correct `skills/` directory.

### Prerequisites

- Node.js >= 14

### Install / Update (Recommended: skills.sh)

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

### Alternative: `vspec` CLI (manual target)

If you want to install into a specific directory without the skills.sh installer, use the built-in CLI:

```bash
npx visual-spec --help
npx visual-spec install --target /path/to/your/project --force
```

By default, it installs to: `<project>/.trae/skills/visual-spec`.

### Next

- Getting started: `getting-started.md`
- Multi-agent installation: `ai-platform-installation.md`
