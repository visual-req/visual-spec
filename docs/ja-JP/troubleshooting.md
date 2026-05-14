## Troubleshooting（よくある問題と対処）

### エディタで [`/vspec:*`](../../README.md#commands) が見つからない

- skill がエディタの skills ディレクトリへインストールされているか確認します。
- Trae の場合、デフォルトは通常プロジェクト配下：`.trae/skills/visual-spec/` です。
- 上書き再インストール：

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

または内蔵 CLI（インストール先を明示）：

```bash
npx visual-spec install --target /path/to/your/project --force
```

### インストール済みだが動かない

- Node.js バージョンを確認：Node.js >= 14
- エディタ側で Skill 機能が有効で、正しい skills ディレクトリを参照しているか確認
- dry-run でインストール先を確認（ファイルは書き込みません）：

```bash
npx visual-spec --dry-run --target /path/to/your/project
```

### 間違ったディレクトリへ入れてしまった

- 誤った場所のフォルダを削除して、正しいプロジェクトへ入れ直します：
  - 削除：`<project>/.trae/skills/visual-spec/`
  - インストール：`npx visual-spec install --target <project> --force`

### 成果物はどこに出力される？

- 成果物は基本 `/specs/` 配下（models、prototypes、details、qc report、plan）です。
- `docs/` は入力資料と修正指示（refine）を置く場所です。
