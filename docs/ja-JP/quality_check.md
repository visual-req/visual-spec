## 要件品質チェック（単独利用）

[English](../en-US/quality_check.md) | [中文](../zh-CN/quality_check.md) | [日本語](../ja-JP/quality_check.md)

このページでは、[/vspec:qc](../../README.md#commands) に依存せずに要件ドキュメントの品質チェックを行う方法を説明します。内蔵の品質標準ファイルを使い、Word/Markdown/ドキュメント庫など任意形式の要件をスキャンして、指摘事項の表を生成できます。

品質チェック（QC）だけを単独で使いたい場合（visual-spec のフルワークフロー不要）は、こちらも利用できます： https://github.com/visual-req/spec-review

QC の設計意図、チェック観点、修正までの閉ループの詳細は、こちらを参照してください： [theory/quality_check.md](theory/quality_check.md)

### 準備

- 品質標準ファイル（環境に存在する方を使用）：
  - Skill ルート：`/prompts/vspec_qc/quality_standard.md`
  - リポジトリ：`skills/visual-spec/prompts/vspec_qc/quality_standard.md`
- 要件ドキュメント（PRD/仕様など）。Word/PDF/Markdown などに対応

### 使い方（DeepSeek のチャットを例に）

1. 次の 2 ファイルをアップロードします：
   - `quality_standard.md`（品質標準）
   - 要件ドキュメント（Word/PDF/Markdown など）
2. 依頼文を入力します：

   品質標準に基づいて要件ドキュメントの品質チェックを行い、結果を表で出力してください。

3. 表を構造化したい場合は、列を指定します（例）：
   - 番号
   - 分類/タイトル
   - 判定（Yes/No/Partial）
   - 問題要約
   - 位置（章/段落/ページ）
   - 修正提案

### コツ

- 抜けやすい観点（上下限、時間口径、式の精度、権限/データ権限、外部依存の失敗時戦略など）は、境界/例外/冪等/ロールバック/監査/照合を重点的に見るよう明示すると効果的です。
- ドメイン固有の高頻度指摘がある場合は、プロジェクトルートに `domain_quality_standard.md` として追記標準を分離し、[/vspec:qc](../../README.md#commands) がマージして使えるようにします。
