## Troubleshooting

### [`/vspec:*`](../../README.md#commands) commands do not show up in my editor

- Confirm the skill is installed into your editor’s skills directory.
- If you are using Trae, the default location is usually: `.trae/skills/visual-spec/` under your project.
- Reinstall with overwrite:

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

Or with the built-in CLI (explicit target):

```bash
npx visual-spec install --target /path/to/your/project --force
```

### Installed, but it still does not work

- Check Node.js version: Node.js >= 14
- Make sure your editor has Skill support enabled and is reading the correct skills directory
- Verify the resolved install path without writing files:

```bash
npx visual-spec --dry-run --target /path/to/your/project
```

### I installed into the wrong directory

- Remove the folder you installed, then install again into the correct project directory:
  - remove: `<project>/.trae/skills/visual-spec/`
  - install: `npx visual-spec install --target <project> --force`

### Where are the outputs generated?

- The workflow generates artifacts under `/specs/` (models, prototypes, detailed specs, QC report, plan).
- The `docs/` directory is used for business inputs and refinement instructions.
