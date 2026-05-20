## Fork 後のカスタマイズ方法

[English](../en-US/fork.md) | [中文](../zh-CN/fork.md) | [日本語](../ja-JP/fork.md)

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

見積の標準値は JSON で管理します：

- `skills/visual-spec/prompts/vspec_plan/estimation_standards.json`

閲覧用（単一 HTML、EN/中文/日本語の切替対応）：

- `skills/visual-spec/prompts/vspec_plan/estimation_standards_reader.html`

`/vspec:plan` の見積フェーズは、この JSON を Story Points の共通口径として参照します（許可される点数は `0/0.5/1/2/3/5/8/13` のみ）。

fork 後に JSON を拡張/修正する方法：
- `allowedStoryPoints` は基本的に固定（変更する場合は見積運用全体を合わせないと点数が漂流します）
- `scalePoints` を調整して、各 SP の意味（範囲/説明）をチームに合わせて明確化
- `workItemBenchmarks` に自組織で頻出する作業カテゴリを追加（安定した `key` を推奨）し、`en/zh-CN/ja` の三言語テキストを必ず埋める
- 監査・追跡のため `version` と `updatedAt` を更新

### 3) “間違い集” を再利用・継続保守

組み込み品質標準は、以下から整備されています：

- `skills/visual-spec/prompts/vspec_qc/需求分析错题本.xlsx`（元データ）
- `skills/visual-spec/prompts/vspec_qc/quality_standard.md`（スキャン可能な形式に転記）

推奨：
- 自組織の “間違い集” を継続更新し、再利用可能なチェックポイントを `domain_quality_standard.md` に蓄積
