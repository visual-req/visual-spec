# 日本語（README）

このリポジトリは、SDD（Specification-Driven Development）に基づく Skill を提供します。生の要件から、レビュー可能な成果物（spec、データモデル、実行可能プロトタイプ、詳細設計、受入ケース、テスト、統合実装）へ変換し、動作するシステムの形に落とし込みます。

## 概要

- 要件分析：背景、ステークホルダー、ロール、用語、フロー、シナリオ、依存関係、機能一覧、未解決質問を生成
- 検証：データモデル、実行可能プロトタイプ、シナリオ確認ページを生成
- 詳細設計：RBAC/データ権限/操作・バリデーション/ログ/通知/MQ/入出力/定期実行などの spec を生成
- 受入 & テスト：受入ケースと自動テストコードを生成
- 統合実装：バックエンド + フロントエンドの統合コードを生成（リポジトリの規約に合わせる）
- 見積・排期：機能一覧をもとに見積とスケジュール（HTML）を生成

## コマンド

- `/vspec:new`：ベースライン spec の生成（`/specs/`）
- `/vspec:refine`：追補資料の反映（`/docs/refine/`）
- `/vspec:refine-q`：Q&A を要件へ取り込み（`questions.md` → `original.md`）
- `/vspec:detail`：機能ごとの詳細 spec（`/specs/details/`）
- `/vspec:verify`：モデル + プロトタイプ（`/specs/models/`、`/specs/prototypes/`）
- `/vspec:accept`：受入ケース（`/specs/acceptance/`）
- `/vspec:append-test`：自動テストコード（既存テストディレクトリ、なければ `/tests/`）
- `/vspec:impl`：統合実装コード（`/specs/` 配下）
- `/vspec:upgrade`：既存資料から specs を再生成/更新（`/docs/legacy` + `current`）
- `/vspec:qc`：品質チェック（`/specs/qc_report.md`）
- `/vspec:plan`：見積・排期（`/specs/plan/`）

## ディレクトリ

- `skills/visual-spec-skill/SKILL.md`：Skill 定義
- `skills/visual-spec-skill/prompts/`：各コマンドのプロンプト
- `docs/`：ドキュメント

## ライセンス / プラン

- `prompts/harness/*`（実行後の追加検証コマンド）は Pro 版の有償機能です。
- Pro 版はより広範な品質チェック（例：プロトタイプのスタック検証、クリック無反応検出、モバイル UX 検証、価格フォーマット検証、バックエンド MVC/テストカバレッジ検証など）を提供します。
