## Theory（設計理念）

[English](../en-US/theory.md) | [中文](../zh-CN/theory.md) | [日本語](../ja-JP/theory.md)

本セクションでは、visual-spec Skill の設計理念を説明します。SDLC（ソフトウェア開発ライフサイクル）との対応関係、なぜコマンドを段階に分けているのか、なぜ「シナリオ一覧」を HTML で出力してプロトタイプと連動させるのか、そして `/vspec:new` が多面的に分析する理由を整理します。

また、承認/回付型のフローを 1 つの再利用可能な骨格（flows）に正規化し、分析出力を安定させるための抽象化も採用しています。

![visual-spec flows](../assets/ja-JP/visual-spec-flows.svg)

この図はプロンプトのチェックリストとして使います。業務を 1〜5 のステップに割り当て、取消/却下などの制御パスと、実行に必要な制約（検証・上限・冪等など）を明示することで、仕様と受入ケースを同じ構造で揃えられます。

### ワークフロー（可視化）
![visual-spec workflow](../assets/ja-JP/visual-spec-workflow.svg)

### ステージマップ

![visual-spec stage map](../assets/ja-JP/visual-spec-stage-map.svg)

この図は、分析のステージと典型的な入力/出力を対応付けたものです。レビューでは「今どの段階にいて、次に何を埋めるべきか」を合意しやすくなります。

### 目次

- SDLC 対応：段階設計の意図と SDLC とのマッピング  
  - [theory/sdlc.md](theory/sdlc.md)
- 計画と見積：要件分解・見積・排期の進め方と、ユーザーストーリーマップを HTML にする理由（`/vspec:plan`）  
  - [theory/plan.md](theory/plan.md)
- レビュー最適化：なぜ HTML のシナリオ一覧なのか、なぜプロトタイプ連動がレビューに効くのか  
  - [theory/prototype-review.md](theory/prototype-review.md)
- Verification & Validation：レビューの閉ループ（review → refine → 再検証）  
  - [theory/verification_and_validation.md](theory/verification_and_validation.md)
- `/vspec:new` が多くを分析する理由と、出力が後続ステップでどう再利用されるか  
  - [theory/new-analysis.md](theory/new-analysis.md)
- 分析思考：要件分析を再利用可能なモジュールとして分解する  
  - [theory/thinking-framework.md](theory/thinking-framework.md)

### 要約

visual-spec は、要件を「追跡可能でレビュー可能なデリバリーの鎖」に変換するために設計されています。シナリオを背骨として、ロール・ルール・データモデル・実行可能プロトタイプを接続し、実装前の合意形成と、変更時の下流成果物の同期更新を容易にします。
