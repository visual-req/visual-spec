# visual-spec（日本語）

[English](README.md) | [中文](README-zh-CN.md) | [日本語](README-ja-JP.md)

このリポジトリは、要件分析とデリバリー支援の Skill を提供します。`/vspec:*` のコマンド駆動ワークフローで、生の要件をレビュー可能かつ実装可能な成果物（spec、データモデル、実行可能プロトタイプ、詳細設計、受入ケース、テスト、統合実装入力）へ変換します。

本 Skill は、独立した知的財産に基づく「可視化要件分析（visualized requirements analysis）」の方法論をベースに設計しています。目的は、要件の明確化 → 設計 → 検証のプロセスを標準化・可視化・再利用可能にし、コミュニケーションコストと手戻りを減らすことです。

バージョン：0.1.13（2026-04-12）

## Quick Installation

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

Docs:
- [Installation](docs/en-US/installation.md)
- [Multi-agent installation](docs/en-US/ai-platform-installation.md)
- Fork guide: [docs/ja-JP/fork.md](docs/ja-JP/fork.md)

## Overview

- 要件分析：背景、ステークホルダー、ロール、用語、フロー、シナリオ、詳細、依存関係、機能一覧、未解決質問を生成
- 方案検証：データモデル、実行可能プロトタイプ、シナリオレビュー用ページを生成
- 詳細設計：機能ごとに RBAC/データ権限/インタラクション/バリデーション/ログ/通知/MQ/入出力/定期実行 spec を生成
- 受入 & テスト：受入ケースと自動テストコードを生成
- 統合実装：リポジトリの実スタック/規約に合わせて backend + frontend の統合コード生成
- 計画：機能一覧に基づき見積とスケジュール（HTML）を生成

## Commands

| コマンド | 用途 | 主な入力 | 主な出力 |
| --- | --- | --- | --- |
| `/vspec:new` | ベースライン spec の生成 | 生要件テキスト +（任意）`/docs/current/*` | `/specs/`（background/functions/flows 等） |
| `/vspec:refine` | 要件の修正と下流成果物の同期更新 | `/docs/refine/refine.md` または貼り付け変更内容/引数 | `/specs/background/original.md` 更新 + `/specs/details/`・`/specs/prototypes/`・既存 `/specs/backend/` 同期更新 |
| `/vspec:refine-q` | 回答済み質問を要件へ取り込み | `/specs/background/questions.md`（回答済み） | `original.md` 更新 + `questions.md` に回答マーク |
| `/vspec:detail` | 機能ごとの詳細 spec | `/specs/functions/*` + 関連成果物 | `/specs/details/` |
| `/vspec:verify` | モデル + 実行可能プロトタイプ | `/scheme.yaml` + 非空 `/specs/details/` | `/specs/models/`、`/specs/prototypes/` |
| `/vspec:accept` | 受入ケース生成 | functions + scenarios + details + models | `/specs/acceptance/` |
| `/vspec:append-test` | 自動テストコード生成 | 受入ケース + 既存テストフレームワーク | 既存テストディレクトリ or `/tests/` |
| `/vspec:impl` | 統合実装入力の生成 | details + models + dependencies | `/specs/backend/`（有効時）および関連コード |
| `/vspec:upgrade` | 既存資料から specs を再生成/更新 | `/docs/legacy/*` + `/docs/current/*` | `/specs/` 更新 + 技術選定を `/scheme.yaml` に同期 |
| `/vspec:qc` | 品質チェック | `/specs/` + 標準 | `/specs/qc_report.json`、`/specs/qc_report.html` |
| `/vspec:plan` | 見積・排期 | functions + details + `/specs/qc_report.json` | `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html` |

## Documentation

| Doc | 説明 | Link |
| --- | --- | --- |
| Getting started | ワークフローを通しで実行 | [docs/ja-JP/getting-started.md](docs/ja-JP/getting-started.md) |
| Commands | `/vspec:*` の参照 | [docs/ja-JP/commands.md](docs/ja-JP/commands.md) |
| Structure | ディレクトリ構成と成果物 | [docs/ja-JP/structure.md](docs/ja-JP/structure.md) |
| Workflows | ワークフロー概要 | [docs/ja-JP/workflows.md](docs/ja-JP/workflows.md) |
| Installation | インストール（英語） | [docs/en-US/installation.md](docs/en-US/installation.md) |
| Fork guide | fork 後のカスタマイズ | [docs/ja-JP/fork.md](docs/ja-JP/fork.md) |

## upgrade と refine の違い

- `upgrade`：遺留システムのアップグレード/刷新向け。`/docs/legacy/` と `/docs/current/`（および templates/texts/assets）を入力として、アップグレード後の target spec と技術選定を生成/更新する。
- `refine`：visual-spec で分析済みで、visual-spec の構造で保存されている要件（遺留/新規を問わない）を継続的に修正し、下流成果物（details/プロトタイプ/backend 実装があれば）との整合を保つ。

## Directory Structure

- `skills/visual-spec/SKILL.md`：Skill 定義
- `skills/visual-spec/prompts/`：各コマンドのプロンプト

## Licensing / Plans

- `prompts/harness/*`（実行後の追加検証コマンド）は Pro 版の有償機能です。
- Pro 版はより広範な品質チェック（例：プロトタイプのスタック検証、クリック無反応検出、モバイル UX 検証、価格フォーマット検証、バックエンド MVC/テストカバレッジ検証など）を提供します。

## Quick Start

1. Skillのインストール：`npx skills add visual-req/visual-spec --skill visual-spec`
2. `/vspec:new` を実行し、生の要件テキストを入力します
3. 指示に従って「Open Questions（未解決質問）」に答え、要件の方向性と前提条件を収束させます
4. 順を追ってコマンドを実行し、最終成果物を生成します：
   - `/vspec:detail`：詳細 spec を生成（`/specs/details/`）
   - `/vspec:verify`：データモデルと実行可能プロトタイプを生成（`/specs/models/`、`/specs/prototypes/`）
   - `/vspec:qc`：品質レポートを生成（`/specs/qc_report.json`、`/specs/qc_report.html`）
   - `/vspec:plan`（任意）：見積とスケジュールを生成（`/specs/plan/`）
5. 要件に変更がある場合：変更内容を `/docs/refine/refine.md` に記載（または対話ウィンドウに貼り付け）し、`/vspec:refine` を実行して下流の成果物と同期更新します
