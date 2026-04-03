## Install into Skill-Enabled AI Editors

This package uses a script to copy the built-in Skill directory into your AI editor configuration directory (Trae / Qwen / Kiro, etc.). The exact config path differs by editor, but the installation logic is the same: install `visual-spec-skill` into the target `skills/` directory.

### Prerequisites

- Node.js >= 14

### Install / Update (npm)

```bash
npm install -g visual-spec
```

### Install / Update (pnpm)

```bash
pnpm add -g visual-spec
```

### Install / Update (yarn)

Yarn Classic:

```bash
yarn global add visual-spec
```

Yarn Berry (v2+):

```bash
yarn dlx -p visual-spec vspec
```

### Next

- Getting started: `docs/getting-started.md`
