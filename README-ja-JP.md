# visual-spec（日本語）

[English](README.md) | [中文](README-zh-CN.md) | [日本語](README-ja-JP.md)

「一文要件」から実行可能プロトタイプと追跡可能な仕様へ。段階的な `/vspec:*` ワークフローで手戻りと齟齬を減らします。

バージョン：0.1.13（2026-04-12）· License: MIT（[LICENSE](LICENSE)）

## 30 秒でわかる価値

入力（生の要件）：

> 「チームのタスクボード。プロジェクト作成、タスク割当、個人別の進捗集計ができる。」

`/vspec:new` → `/vspec:verify` の後に得られるもの：

- 実行可能プロトタイプ + シナリオレビュー入口
- 構造化仕様：ロール/シナリオ/フロー/機能分解と詳細
- データモデル、および権限/バリデーション/ロジックをレビューするための仕様

## クイックスタート（3 ステップ）

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

2. `/vspec:new` を実行し、要件テキストを貼り付けます。
3. Open Questions に答えた後、`/vspec:verify` を実行して実行可能プロトタイプでレビューします。

初心者向け： [docs/ja-JP/getting-started.md](docs/ja-JP/getting-started.md)

## 想定ユーザー

| プロダクト / BA | 開発 | QA / 受入 |
| --- | --- | --- |
| 曖昧な要件をレビュー可能なシナリオと原型へ | 実装/テスト可能な詳細（権限/検証/ロジック）とモデル | 重要シナリオを受入ケースへ落とし込む |

## Overview

ワークフロー図（SVG）：

![visual-spec workflow](docs/assets/ja-JP/visual-spec-workflow.svg)

方法論 / theory（全体設計の考え方とコマンド分割の意図）：
- [docs/ja-JP/theory.md](docs/ja-JP/theory.md)

- 要件分析：背景、ステークホルダー、ロール、用語、フロー、シナリオ、詳細、依存関係、機能一覧、未解決質問を生成
- 方案検証：データモデル、実行可能プロトタイプ、シナリオレビュー用ページを生成
- プロトタイプ生成（高頻度）：`/vspec:verify` が `/scheme.yaml` に合わせて実行可能な Web プロトタイプを生成（`/specs/prototypes/`）。ロール別ダッシュボード（適切なチャート選定/配置）とシナリオレビュー用ページを含む
- 詳細設計：機能ごとに RBAC/データ権限/インタラクション/バリデーション/ログ/通知/MQ/入出力/定期実行 spec を生成
- 受入 & テスト：受入ケースと自動テストコードを生成
- 統合実装：リポジトリの実スタック/規約に合わせて backend + frontend の統合コード生成
- 計画：機能一覧に基づき見積とスケジュール（HTML）を生成

## Commands

| コマンド | 用途 | 主なメリット | 主な出力 |
| --- | --- | --- | --- |
| `/vspec:new` | ベースライン spec の生成 | 生の要件をレビュー可能な構造へ落とし込む | `/specs/`（background/functions/flows 等） |
| `/vspec:detail` | 機能ごとの詳細 spec | 実装/テスト可能な粒度へ展開する | `/specs/details/` |
| `/vspec:verify` | モデル + 実行可能プロトタイプ | 期待どおりの振る舞いか早期に確認できる | `/specs/models/`、`/specs/prototypes/` |
| `/vspec:qc` | 品質チェック | 漏れ/矛盾/テスト不能/追跡不足を早期に可視化する | `/specs/qc_report.json`、`/specs/qc_report.html` |
| `/vspec:refine` | 要件の修正と下流成果物の同期更新 | 変更時に成果物の整合を保つ | `original.md` 更新 + 影響範囲の同期更新 |
| `/vspec:accept` | 受入ケース生成 | シナリオを受入言語へ変換する | `/specs/acceptance/` |
| `/vspec:append-test` | 自動テストコード生成 | テスト自動化の導入コストを下げる | 既存テストディレクトリ or `/tests/` |
| `/vspec:impl` | 統合実装入力の生成 | スタック/規約に合わせた実装入力を出す | `/specs/backend/`（有効時）および関連コード |
| `/vspec:plan` | 見積・排期 | スコープをレビュー可能な計画にする | `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html` |
| `/vspec:upgrade` | 既存資料から specs を再生成/更新 | 既存資料から仕様を再構築/更新する | `/specs/` 更新 + 技術選定を `/scheme.yaml` に同期 |

品質チェック（QC）機能だけを単独で使いたい場合（visual-spec のフルワークフロー不要）は、こちらを利用してください： https://github.com/visual-req/spec-review

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

## FAQ

- 技術スタックに合わせられますか？  
  `/vspec:verify` のプロトタイプは Web 形態で、`/scheme.yaml` に従います。参考： [scheme.example.yaml](docs/en-US/scheme.example.yaml) と [docs/ja-JP/structure.md](docs/ja-JP/structure.md)。
- 成果物はどこに出力されますか？  
  主に `/specs/` 配下です（models、prototypes、details、qc report、plan）。参考： [docs/ja-JP/structure.md](docs/ja-JP/structure.md)。

## Contributing

- カスタマイズ： [docs/ja-JP/fork.md](docs/ja-JP/fork.md)
- 改善提案・不具合報告：GitHub Issues / Pull Requests
