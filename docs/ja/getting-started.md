## クイックスタート

このパッケージは `/vspec:*` コマンド駆動の Skill を提供します。生の要件から、レビュー可能な成果物（spec、データモデル、実行可能プロトタイプ、詳細設計、受入用ケース、テスト、実装入力）へ変換します。

### 1. インストール

- インストール：`installation.md`

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```

### 2. 推奨フロー

- 初期 spec：`/vspec:new`
  - 実行中に要件口径（`/specs/background/original.md`）を生成し、確認質問を提示
  - まずチャットで回答し、その後「continue」と入力して `/vspec:new` を完了
- Q&A を要件へ反映：`/vspec:refine-q`（`/specs/background/questions.md` の回答済み項目を `original.md` に取り込む）
- 品質チェック：`/vspec:qc`（`/specs/qc_report.md` を出力）
- 詳細設計：`/vspec:detail`（RBAC/データ権限/画面のロード・操作・バリデーション等）
- 検証（モデル + 原型）：`/vspec:verify`（`/specs/details/` が必要）
- 受入ケース：`/vspec:accept`
- 自動テスト生成：`/vspec:append-test`
- 実装入力/統合コード：`/vspec:impl`
- 既存資産からのアップグレード：`/vspec:upgrade`
- 見積・スケジュール：`/vspec:plan`

### 3. 主要ディレクトリ

- `/docs/`：入力アーカイブ（legacy/current/refine/templates/texts/assets）
- `/specs/`：生成成果物
- `/scheme.yaml`：スタック選択（プロトタイプと実装が従う）

参照：

- `structure.md`
