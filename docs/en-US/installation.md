## Install into Skill-Enabled AI Editors

This package uses a script to copy the built-in Skill directory into your AI editor configuration directory (Trae / Qwen / Kiro, etc.). The exact config path differs by editor, but the installation logic is the same: install `visual-spec-skill` into the target `skills/` directory.

### Prerequisites

- Node.js >= 14

### Install / Update (npm)

```bash
npm install -g visual-spec@latest
```

### Install / Update (pnpm)

```bash
pnpm add -g visual-spec@latest
```

### Install / Update (yarn)

Yarn Classic:

```bash
yarn global add visual-spec@latest
```

Yarn Berry (v2+):

```bash
yarn dlx -p visual-spec@latest vspec
```

### Install to a Custom Directory (`--target-skills-dir`)

By default, the install script copies the Skill into `.trae/skills/visual-spec-skill` under the current working directory. If you need to install into a custom `skills/` directory (for example, a shared editor config directory), run:

```bash
vspec --target-skills-dir /path/to/skills --force
```

Notes:
- `--target-skills-dir` should point to the `skills/` directory; the installer will append `visual-spec-skill/`.
- You can also pass a full target directory (including `visual-spec-skill`) via `--target-skill-dir`:

```bash
vspec --target-skill-dir /path/to/skills/visual-spec-skill --force
```

### Next

- Getting started: `getting-started.md`
