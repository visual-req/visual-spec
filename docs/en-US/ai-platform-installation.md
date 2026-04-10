# Multi-Agent Installation Guide

Recommended: use the official skills.sh installer (the skills CLI). It can install the same Skill to different AI platforms (Trae / Claude Code / Cursor / GitHub Copilot, etc.) by placing it into the correct skills directory.

## Option 1: skills.sh (Recommended)

The installer can auto-detect supported agents and prompt you for installation scope (project vs global).

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

Target a specific agent (examples):

```bash
# Trae (project scope)
npx skills add visual-req/visual-spec --skill visual-spec -a trae

# Claude Code (project scope)
npx skills add visual-req/visual-spec --skill visual-spec -a claude-code

# Cursor (project scope)
npx skills add visual-req/visual-spec --skill visual-spec -a cursor

# GitHub Copilot (project scope)
npx skills add visual-req/visual-spec --skill visual-spec -a github-copilot
```

Global install (available across all projects for the current user):

```bash
npx skills add visual-req/visual-spec --skill visual-spec -g
```

List skills in this repository:

```bash
npx skills add visual-req/visual-spec --list
```
