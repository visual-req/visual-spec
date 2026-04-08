import re
from pathlib import Path


def parse_md(text: str):
    heading_re = re.compile(r"^####\s+(\d+)\.\s+(.*)\s*$")
    lines = text.splitlines()
    preamble = []
    sections = []
    cur = None

    for ln in lines:
        m = heading_re.match(ln)
        if m:
            if cur is not None:
                sections.append(cur)
            cur = {"num": int(m.group(1)), "title": m.group(2).strip(), "raw": []}
            continue
        if cur is None:
            preamble.append(ln)
        else:
            cur["raw"].append(ln)

    if cur is not None:
        sections.append(cur)

    return preamble, sections


def extract_fields(raw_lines):
    fields = {}
    passthrough = []
    for ln in raw_lines:
        s = ln.strip()
        if s.startswith("- "):
            body = s[2:]
            if "：" in body:
                k, v = body.split("：", 1)
                k = k.strip()
                v = v.strip()
                if not k or not v:
                    continue
                if k in fields and v not in fields[k]:
                    fields[k] = fields[k] + "；" + v
                else:
                    fields.setdefault(k, v)
            else:
                if body.strip():
                    passthrough.append(body.strip())
        else:
            if s:
                passthrough.append(ln)
    return fields, passthrough


def join_nonempty(parts):
    out = []
    for p in parts:
        if p is None:
            continue
        s = str(p).strip()
        if s:
            out.append(s)
    return "；".join(out)


def ensure(fields, key, value):
    if not (fields.get(key) or "").strip():
        fields[key] = value


def infer_title(fields):
    for k in ("问题描述", "错误问题示例", "解决方案", "解决方案示例", "关键词", "问题分类"):
        v = (fields.get(k) or "").strip()
        if v:
            return v[:40]
    return "规则"


def merge_section_into(target_fields, sources, into_key, prefix=None):
    additions = []
    for src in sources:
        if src is None:
            continue
        sf, sp = extract_fields(src["raw"])
        for k in ("解决方案示例", "解决方案", "问题描述", "错误问题示例"):
            if (sf.get(k) or "").strip():
                additions.append(sf[k])
        for x in sp:
            if str(x).strip():
                additions.append(str(x).strip())
    if not additions:
        return
    base = (target_fields.get(into_key) or "").strip()
    addon = join_nonempty(additions)
    if prefix:
        addon = prefix + addon
    target_fields[into_key] = join_nonempty([base, addon]) if base else addon


def set_fields(section, fields):
    ordered = [
        "问题分类",
        "英文1",
        "英文2",
        "英文标识",
        "关键词",
        "补充说明",
        "问题描述",
        "错误问题示例",
        "解决方案",
        "解决方案示例",
        "方案收益",
        "应用场景",
        "关联质量标准",
    ]
    raw = []
    for k in ordered:
        v = (fields.get(k) or "").strip()
        if v:
            raw.append(f"- {k}：{v}")
    for k in sorted(fields.keys()):
        if k in ordered:
            continue
        v = (fields.get(k) or "").strip()
        if v:
            raw.append(f"- {k}：{v}")
    section["raw"] = raw


def transform(md_path: Path):
    preamble, sections = parse_md(md_path.read_text(encoding="utf-8"))
    by_num = {s["num"]: s for s in sections}

    remove_nums = {58, 104, 35, 36, 37, 64, 65, 67, 68, 69, 87}

    kept = []
    for s in sections:
        if s["num"] in remove_nums:
            continue
        f, _ = extract_fields(s["raw"])
        if s["title"].strip() == "Rule" and not f:
            continue
        kept.append(s)

    def idx_after(num):
        for i, s in enumerate(kept):
            if s["num"] == num:
                return i + 1
        return None

    insert_idx = idx_after(47)
    if insert_idx is not None:
        extra = [
            {
                "num": -1,
                "title": "数量上下限（含0/负数/超大值）",
                "raw": [
                    "- 问题分类：上下限遗漏",
                    "- 关键词：数量上限/下限/0值/负数",
                    "- 问题描述：数量字段若未定义最小值、最大值与边界口径（是否允许0、是否允许负数、是否允许小数），会导致业务漏洞或系统异常。",
                    "- 错误问题示例：购买数量未限制导致一次下单999999；数量允许0导致生成空订单；负数导致库存回补异常。",
                    "- 解决方案：为每个数量类字段定义：最小值/最大值/步进（整数或小数）、单位、边界是否包含、超限时提示与后端兜底；对导入/批量接口同样生效。",
                    "- 解决方案示例：示例：qty 为整数，1<=qty<=999；超限返回错误码并提示“数量范围为1-999”；导入逐行校验并输出失败明细。",
                    "- 方案收益：避免刷单/超限/数据污染，提升稳定性与可控性。",
                    "- 应用场景：数量、份数、次数、库存变更、票数、积分变动等所有计数量字段。",
                    "- 关联质量标准：精确性",
                ],
            },
            {
                "num": -1,
                "title": "距离/范围上下限（配送/定位/围栏等）",
                "raw": [
                    "- 问题分类：上下限遗漏",
                    "- 关键词：距离上限/下限/范围口径",
                    "- 问题描述：距离/范围字段若未定义上限、下限、单位与计算口径，会导致错误计费、不可达订单或性能问题。",
                    "- 错误问题示例：配送半径未限制导致生成不可配送订单；距离单位混用（米/公里）导致计费错误。",
                    "- 解决方案：明确单位（m/km）、计算口径（直线/路径）、上限下限与舍入规则，并定义超限处理（提示/禁止下单/降级到人工确认）。",
                    "- 解决方案示例：示例：delivery_radius_km 0<r<=30；distance_km 取1位小数四舍五入；超出30km不允许下单并提示。",
                    "- 方案收益：避免业务不可达与计费纠纷，提升体验与可运营性。",
                    "- 应用场景：配送、网点服务范围、定位打卡、围栏、里程计费等。",
                    "- 关联质量标准：精确性",
                ],
            },
            {
                "num": -1,
                "title": "年龄上下限（未成年人/合规）",
                "raw": [
                    "- 问题分类：上下限遗漏",
                    "- 关键词：年龄下限/上限/生日口径",
                    "- 问题描述：年龄规则若未明确计算口径与边界（按生日/自然日/时区），会导致合规风险与错误放行/拦截。",
                    "- 错误问题示例：未限制未成年人注册；生日当天是否满18岁口径不一致导致审核争议。",
                    "- 解决方案：明确年龄计算：以哪个字段为生日、以哪个时区判断、边界是否包含；规定允许范围与异常处理（缺失生日/不可解析）。",
                    "- 解决方案示例：示例：合规判定用“是否已到18周岁生日当天（含）”；缺失生日不允许通过并提示补全。",
                    "- 方案收益：降低合规风险，保证判定一致与可验收。",
                    "- 应用场景：注册、内容分级、支付、考试、未成年人保护等。",
                    "- 关联质量标准：精确性",
                ],
            },
        ]
        kept[insert_idx:insert_idx] = extra

    by_num2 = {s["num"]: s for s in kept}

    if 34 in by_num2:
        tgt = by_num2[34]
        f, _ = extract_fields(tgt["raw"])
        merge_section_into(
            f,
            [by_num.get(35), by_num.get(36), by_num.get(37)],
            "解决方案示例",
            prefix="补充：",
        )
        ensure(f, "问题分类", "权限遗漏")
        ensure(f, "关键词", "RBAC/组织权限/数据权限/状态权限")
        ensure(
            f,
            "解决方案",
            "采用权限矩阵体系化覆盖：控件级 RBAC + 组织结构权限 + 数据权限 + 状态权限（可操作性矩阵），并明确入口权限与条件。",
        )
        ensure(
            f,
            "解决方案示例",
            "示例：RBAC（页面区域/控件权限矩阵 + 路由/菜单入口权限）；组织结构权限（按组织层级/岗位/部门的可见与可操作范围）；数据权限（行/列/范围矩阵 + 过滤口径）；状态权限（决策矩阵：操作×状态）。",
        )
        ensure(f, "方案收益", "避免越权与权限遗漏导致的线上风险，减少返工与联调问题。")
        ensure(f, "应用场景", "任何需要权限控制（菜单/路由/控件/数据范围/状态机操作）的功能。")
        ensure(f, "关联质量标准", "完整性")
        set_fields(tgt, f)

    if 63 in by_num2:
        tgt = by_num2[63]
        f, _ = extract_fields(tgt["raw"])
        merge_section_into(f, [by_num.get(64), by_num.get(65)], "解决方案示例", prefix="补充：")
        ensure(
            f,
            "解决方案示例",
            "示例：将独占条件单独拆出；按处理阶段/属性拆分为多个小矩阵；把公共前置条件提升为“先决条件”避免在矩阵中重复。",
        )
        set_fields(tgt, f)

    if 66 in by_num2:
        tgt = by_num2[66]
        f, _ = extract_fields(tgt["raw"])
        merge_section_into(
            f,
            [by_num.get(67), by_num.get(68), by_num.get(69)],
            "解决方案示例",
            prefix="补充：",
        )
        ensure(
            f,
            "解决方案示例",
            "示例：表达式树/判定矩阵/流程图替代深层缩进；或按判定条件拆分成多个矩阵以提升可读性。",
        )
        set_fields(tgt, f)

    if 86 in by_num2:
        tgt = by_num2[86]
        f, _ = extract_fields(tgt["raw"])
        merge_section_into(f, [by_num.get(87)], "错误问题示例", prefix="补充：")
        ensure(
            f,
            "解决方案",
            "优先遵循业界/国际/国家规范（RFC/ISO/国家标准等），在需求中给出规范链接、适用范围、边界与示例；若需自定义，必须说明偏离原因与兼容策略。",
        )
        ensure(
            f,
            "解决方案示例",
            "示例：手机号/国际电话采用 E.164；邮箱采用 RFC 5322 子集；日期时间采用 ISO 8601；金额精度与舍入规则统一。",
        )
        ensure(f, "方案收益", "避免“自创规则”导致的兼容性问题、数据污染与线上故障。")
        ensure(f, "应用场景", "格式校验、编号/编码、时间口径、对接协议、加密/签名等存在成熟标准的场景。")
        set_fields(tgt, f)

    for s in kept:
        f, _ = extract_fields(s["raw"])
        if s["title"].strip() == "Rule":
            s["title"] = infer_title(f)
        ensure(f, "问题描述", s["title"][:80])
        ensure(f, "解决方案", "补充明确规则与边界条件，并给出可验收的示例与异常处理口径，避免实现与验收产生歧义。")
        ensure(f, "方案收益", "减少歧义与遗漏，提升实现正确性与验收一致性。")
        ensure(f, "应用场景", "需求分析与方案设计阶段，存在同类问题风险时。")
        set_fields(s, f)

    n = 1
    for s in kept:
        s["num"] = n
        n += 1

    out = []
    out.extend(preamble)
    while out and out[-1].strip() == "":
        out.pop()
    out.append("")
    for s in kept:
        out.append(f"#### {s['num']}. {s['title']}")
        out.extend(s["raw"])
        out.append("")

    md_path.write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")


if __name__ == "__main__":
    transform(Path("skills/visual-spec-skill/prompts/vspec_qc/quality_standard.md"))

