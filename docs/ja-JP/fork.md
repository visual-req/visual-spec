## Fork 後のカスタマイズ方法

本リポジトリのデフォルト挙動は、汎用的な要件分析とデリバリーを対象にしています。特定の業界/ドメイン向け、または社内チーム向けに本リポジトリを fork して運用する場合は、以下のカスタマイズを行うことで `/vspec:*` の出力を組織の標準に合わせやすくなります。

### 1) ドメイン/業界の品質標準を追加（推奨）

プロジェクトのルート直下に以下を作成します：

- `domain_quality_standard.md`

用途：
- 業界/ドメイン固有のチェックポイントを補完（例：コンプライアンス、監査、保管/保持、会計口径など）
- `/vspec:qc` 実行時は次を併せて参照し、優先度に従って統合します：
  - 組み込み標準：`skills/visual-spec/prompts/vspec_qc/quality_standard.md`
  - ドメイン標準：`domain_quality_standard.md`
  - プロジェクト標準：`quality_standard.md`（存在する場合は最優先）

推奨フォーマット：
- 「チェック項目 + 判定基準 + よくある誤り + 修正案」
- 具体的な成果物に落とす必要がある場合は、対象パスを明記（例：`/specs/background/original.md`、`/specs/models/*.md`、`/specs/details/**`）

### 2) 見積の基準をカスタマイズ（推奨）

見積基準は以下にあります：

- `skills/visual-spec/prompts/vspec_plan/estimate.md`

このファイルには、fork 後に調整できる参照表が含まれています：
- Story Points の標準スケール
- 代表的な作業項目の見積参考（CRUD、入出力、承認/状態機械、RBAC、データ権限、外部連携、定期実行など）

推奨アプローチ：
- チームの生産性、コード生成比率、テスト強度、リリース運用に合わせて SP の目安を調整
- 自組織で頻出する作業カテゴリを追加（例：チケット/工単、レポート、決済、CMS、設定配信など）

### 3) “間違い集” を再利用・継続保守

組み込み品質標準は、以下から整備されています：

- `skills/visual-spec/prompts/vspec_qc/需求分析错题本.xlsx`（元データ）
- `skills/visual-spec/prompts/vspec_qc/quality_standard.md`（スキャン可能な形式に転記）

推奨：
- 自組織の “間違い集” を継続更新し、再利用可能なチェックポイントを `domain_quality_standard.md` に蓄積
