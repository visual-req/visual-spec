# 複数 AI プラットフォーム向けインストールガイド

推奨：skills.sh の公式インストーラ（skills CLI）を利用します。同一の Skill を、Trae / Claude Code / Cursor / GitHub Copilot など複数の AI プラットフォームに対して、それぞれの `skills/` ディレクトリへインストールできます。

## 方法 1：skills.sh（推奨）

インストーラは利用可能な agent を自動検出し、プロジェクト単位/グローバル単位のインストールも選択できます。

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

特定の agent を指定する例：

```bash
# Trae（プロジェクト単位）
npx skills add visual-req/visual-spec --skill visual-spec -a trae

# Claude Code（プロジェクト単位）
npx skills add visual-req/visual-spec --skill visual-spec -a claude-code

# Cursor（プロジェクト単位）
npx skills add visual-req/visual-spec --skill visual-spec -a cursor

# GitHub Copilot（プロジェクト単位）
npx skills add visual-req/visual-spec --skill visual-spec -a github-copilot
```

グローバルインストール（ユーザーの全プロジェクトで利用）：

```bash
npx skills add visual-req/visual-spec --skill visual-spec -g
```

このリポジトリ内の skills を一覧表示：

```bash
npx skills add visual-req/visual-spec --list
```
