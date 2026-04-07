# ディレクトリ構成

このドキュメントは、対象プロジェクトで使うディレクトリ構成（Skill が生成する `/specs/` ツリー等）を説明します。

## 典型構成

```text
<your-project>/
├─ docs/                                  # 入力アーカイブ（/vspec:new が作成）
│  ├─ legacy/                             # 既存/レガシー資料
│  ├─ current/                            # 今回の入力資料
│  │  └─ file_list.md                     # upgrade の入力一覧（/vspec:upgrade）
│  ├─ refine/                             # 追補資料（/vspec:refine）
│  │  └─ file_list.md                     # 任意の入力順序リスト
│  ├─ templates/                          # テンプレート（任意）
│  ├─ texts/                              # 文言（任意）
│  └─ assets/                             # 画像等（任意）
├─ scheme.yaml                            # スタック選択（/vspec:verify, /vspec:impl）
└─ specs/
   ├─ background/
   │  ├─ original.md
   │  ├─ stakeholders.md
   │  ├─ roles.md
   │  ├─ terms.md
   │  ├─ scenarios.md
   │  ├─ scenario_details/
   │  ├─ dependencies.md
   │  └─ questions.md
   ├─ flows/
   │  └─ *.puml
   ├─ functions/
   │  └─ *.md
   ├─ details/
   │  └─ <module_slug>/
   ├─ models/
   │  └─ *.md
   ├─ prototypes/
   │  └─ ...
   ├─ acceptance/
   │  ├─ index.md
   │  └─ ...
   ├─ qc_report.md
   └─ plan/
      ├─ plan_estimate.md
      └─ plan_schedule.html
```

補足：
- `scheme.yaml` はプロジェクトルートを優先し、なければ `/specs/scheme.yaml` を参照します。
