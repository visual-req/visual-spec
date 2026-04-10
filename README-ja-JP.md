# README（日本語）

このリポジトリは、要件分析とデリバリー支援の Skill を提供します。`/vspec:*` のコマンド駆動ワークフローで、生の要件をレビュー可能な成果物（spec、データモデル、実行可能プロトタイプ、詳細設計、受入ケース、テスト、統合実装入力）へ変換します。

## Installation

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

Docs:
- Installation: `docs/en-US/installation.md`
- Multi-agent installation: `docs/en-US/ai-platform-installation.md`

## Overview

- 要件分析：背景、ステークホルダー、ロール、用語、フロー、シナリオ、詳細、依存関係、機能一覧、未解決質問を生成
- 方案検証：データモデル、実行可能プロトタイプ、シナリオレビュー用ページを生成
- 詳細設計：機能ごとに RBAC/データ権限/インタラクション/バリデーション/ログ/通知/MQ/入出力/定期実行 spec を生成
- 受入 & テスト：受入ケースと自動テストコードを生成
- 統合実装：リポジトリの実スタック/規約に合わせて backend + frontend の統合コード生成
- 計画：機能一覧に基づき見積とスケジュール（HTML）を生成

## Commands

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

## Directory Structure

- `skills/visual-spec/SKILL.md`：Skill 定義
- `skills/visual-spec/prompts/`：各コマンドのプロンプト

## Licensing / Plans

- `prompts/harness/*`（実行後の追加検証コマンド）は Pro 版の有償機能です。
- Pro 版はより広範な品質チェック（例：プロトタイプのスタック検証、クリック無反応検出、モバイル UX 検証、価格フォーマット検証、バックエンド MVC/テストカバレッジ検証など）を提供します。
