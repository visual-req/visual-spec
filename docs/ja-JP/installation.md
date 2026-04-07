## Skill 対応 AI エディタへのインストール

推奨：skills.sh の公式インストーラ（skills CLI）を使って、Skill 対応の AI エディタ（Trae / Qwen / Kiro など）へインストールします。インストーラは利用可能な agent を自動検出し、`visual-spec-skill` を適切な `skills/` ディレクトリへ配置します。

### 前提条件

- Node.js >= 14

### インストール / 更新（推奨：skills.sh）

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```

### 次へ

- クイックスタート：`getting-started.md`
- 複数 AI プラットフォーム向けインストール：`ai-platform-installation.md`
