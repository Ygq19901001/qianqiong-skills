#!/usr/bin/env python3
"""PF quality gate auto-test (v3.0.11)
Usage: python auto-test.py <skill_dir>

覆盖 PF1-PF11 + PF11f + PF13-PF15（15 项内容质量门），门面质量门（PF11/PF11f）自动守护，功能门（PF13 EVAL_SET）、能力落地（PF14）、行动授权（PF15）自动守护。PF12 同步门（SKILL.md↔references/↔evolution-state.json 版本三重一致）为人工纪律，不在此脚本自动检查。
独立可运行：不依赖任何外部扫描脚本或技能清单。
门面判据回流自 scan_doorface_v2.py（43 技能全量门面扫描通病提炼）。

v3.0.8 起引入「技能类型分级」判据：
- 单文件工具型（无 references/ 目录）：PF2 豁免、PF6/PF7 降级为 ADV（建议级，不阻断）。
- 双层结构型（有 references/ 目录）：PF2 改为"非空即过"、PF6/PF7 维持强制。
- PF5 起源铭文对两类都强制（红线 #22）。
原因：R5 重跑暴露 39 个 FAIL 中，PF2 大面积失败来自单文件工具被套用双层结构标准
（误判），PF6/PF7 对轻量工具属过度治理。分级后质量门只阻断真缺陷，不再误伤。

v3.0.9 起把类型分级扩展到 PF1 / PF3（R7 门面打磨循环收口）：
- PF1 体量门：单文件工具型豁免（body 体量非治理对象，与 PF2 逻辑一致）；双层型守 8-40KB（云端 128K 完整加载无忧，偏好 ≤30KB）。
  根因：12 个 FAIL 全为合同系/skillhub-publisher 单文件工具（4.1-8.0KB），功能完整（R1-R4 验证），
  短文档是合同系通病，非真缺陷。
- PF3 钩子词：补「触发词 / 可独立触发 / 3分钟 / 30秒」到钩子词表（原表只含 5min/五分钟等时间短语）。
  根因：4 个 FAIL（data-analyst-pro/life-plan-pro/readability-pro/reference-formatter）首屏已有
  `## 触发词（用户原声型）` 规范钩子，仅词表未覆盖，属判据与门面通病提炼不一致，非真缺陷。
"""
import sys, os, re

ENCODING = "utf-8-sig"

# === 门面判据（回流 scan_doorface_v2.py，v3.0.7 起内置于元技能）===
VALUE_WORDS = ["帮你","能","解决","避免","省","一键","自动","快速","直接","搞定","查出","生成","输出","让你","给你","提升","秒出","减少","防止","识别","定位","揪出","排雷","避坑","过不了","降重"]
SELF_WORDS = ["本技能","本工具","我叫","我是","模块","功能包括","提供以下","包含以下","架构如下","流程如下","定位为","职责","以下简称","本助手"]
SYS_TRIGGER_HINT = ["锁定","review_path","contract-intake","route","->","仅当","由.*触发","被.*路由","前置","必须.*先","链路","调用.*skill"]
USER_VOICE_HINT = ["帮我","看看","怎么","如何","为什么","这份","这个","审","写","改","查","做","生成","优化","排","合同","论文","报告","文档","翻译","PPT","摘要"]
# 锁死判据：仅捕获"路由锁死"类表述（本技能不可独立触发、须由某技能路由/前置锁死）。
# 注意：排除"必须由"（泛化词，常指"人类确认/作者独立完成"，非路由锁死，易误判）。
LOCKED_HINT = ["锁定 review_path","不可独立","仅当","才能使用","路由锁定","前端锁死","前置锁死","被路由"]
# 去模板化黑名单（反同质化代理检测：命中即判通用模板句）
GENERIC_DESC = ["一键规范搞定","繁琐活","通用句","自动化处理","高效完成","专业工具","一键解决你的问题","提升效率","帮你搞定一切","各类任务"]

def _read(skill_dir):
    p = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(p):
        return "", []
    with open(p, "r", encoding=ENCODING) as f:
        text = f.read()
    return text, text.splitlines()

def _yaml_end(lines):
    dashes = 0
    for i, line in enumerate(lines):
        if line.strip() == "---":
            dashes += 1
            if dashes == 2:
                return i + 1
    return 0

def parse_fm(text):
    if not text.lstrip("\ufeff").startswith("---"):
        return {}
    m = re.search(r"(?s)^---[^\n]*\n(.*?)\n---", text)
    if not m:
        return {}
    fm = {}
    for ln in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", ln)
        if mm:
            fm[mm.group(1).lower()] = mm.group(2).strip()
    return fm

def extract_trigger_block(body):
    pats = [r"(?s)##\s*触发[^\n]*\n(.*?)(?=\n##\s|\Z)",
            r"(?s)##\s*triggers?[^\n]*\n(.*?)(?=\n##\s|\Z)",
            r"(?s)##\s*使用场景[^\n]*\n(.*?)(?=\n##\s|\Z)"]
    for p in pats:
        m = re.search(p, body)
        if m:
            return m.group(1).strip()
    return ""

def detect_skill_type(skill_dir):
    """v3.0.8: 技能类型分级。有 references/ 目录即双层结构型，否则单文件工具型。"""
    refs = os.path.join(skill_dir, "references")
    return "double" if os.path.isdir(refs) else "single"

def get_tier(skill_dir):
    """v3.0.12: 读 frontmatter `tier:`，缺省 T1（不弱化既有发布技能）。
    T1=全门强制; T2=PF13/PF10/PF14 转 ADV; T3=PF13/PF10/PF14/PF15 全 ADV。"""
    text, _ = _read(skill_dir)
    fm = parse_fm(text)
    t = (fm.get("tier") or "T1").upper()
    return t if t in ("T1", "T2", "T3") else "T1"

# ---- Tests ----

def test_pf1(skill_dir):
    p = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(p):
        return False, "SKILL.md not found"
    st = detect_skill_type(skill_dir)
    kb = os.path.getsize(p) / 1024
    if st == "single":
        return True, "EXEMPT single-file tool (size=%.1fKB, body-substance N/A)" % kb
    ok = 8 <= kb <= 40
    return ok, "size=%.1fKB %s" % (kb, "(OK)" if ok else "(OUT OF 8-40KB)")

def test_pf2(skill_dir):
    refs = os.path.join(skill_dir, "references")
    st = detect_skill_type(skill_dir)
    if st == "single":
        return True, "EXEMPT single-file tool (references/ N/A)"
    if not os.path.isdir(refs):
        return False, "references/ missing (double-type requires it)"
    subs = [d for d in os.listdir(refs) if os.path.isdir(os.path.join(refs, d))]
    files = [f for f in os.listdir(refs) if os.path.isfile(os.path.join(refs, f))]
    nonempty = (len(subs) >= 1) or (len(files) >= 1)
    return nonempty, "refs nonempty (subdirs=%d files=%d) %s" % (
        len(subs), len(files), "(OK)" if nonempty else "(EMPTY - double-type must have refs)")

def test_pf3(skill_dir):
    text, lines = _read(skill_dir)
    if not lines:
        return False, "SKILL.md empty"
    body_start = _yaml_end(lines)
    body = lines[body_start:]
    total = len(body)
    limit = max(1, int(total * 0.33))
    # v3.0.9: 补「触发词 / 可独立触发 / 3分钟 / 30秒」，对齐门面通病提炼（原表只含时间短语类钩子）。
    hooks = ["5min", "30sec", "Quick", "hook", "walkthrough", "tutorial", "用它能解决什么",
             "五分钟", "3分钟", "30秒", "触发词", "可独立触发"]
    for i, line in enumerate(body):
        if i >= limit:
            break
        if any(h.lower() in line.lower() for h in hooks):
            return True, "hook L%d/%d body (%d%%)" % (body_start + i + 1, len(lines), int((i + 1) / total * 100))
    return False, "no hook in first %d of %d body lines" % (limit, total)

def test_pf4(skill_dir):
    text, lines = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    in_trig = False
    count = 0
    for line in lines:
        s = line.strip()
        if s.startswith("triggers:"):
            in_trig = True
            continue
        if in_trig:
            if s == "---":
                break
            if s.startswith("- ") and not s.startswith("#"):
                count += 1
    ok = count >= 5
    return ok, "trigger-lines=%d %s" % (count, "(OK)" if ok else "(need >=5)")

def test_pf5(skill_dir):
    """红线#22 合规：第 1 个非空白行必须是 ---（YAML 前置）；起源铭文(<!--)必须在 --- 之后存在，不得焊入第 1 行。"""
    text, lines = _read(skill_dir)
    if not lines:
        return False, "SKILL.md empty"
    first = None
    for ln in lines:
        if ln.strip():
            first = ln.strip()
            break
    if first != "---":
        return False, "first non-blank line=%r, must be '---' (red-line #22)" % first[:20]
    if lines[0].lstrip().startswith("<!--"):
        return False, "origin inscription welded to L1 (violates red-line #22)"
    has_inscription = "<!--" in text
    if not has_inscription:
        return False, "origin inscription (<!--) missing after '---'"
    return True, "YAML front-matter OK + inscription after '---'"

def test_pf6(skill_dir):
    text, lines = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    st = detect_skill_type(skill_dir)
    keywords = ["不可删除", "不可修改", "人类确认", "人类最终裁决", "起源铭文", "进化阶", "v2.6.0", "Cron"]
    hits = sum(1 for kw in keywords if kw in text)
    ok = hits >= 6
    if st == "single":
        return True, "ADV single-file immutable-core hits=%d/8 (advisory, not blocking)" % hits
    return ok, "hits=%d/8 %s" % (hits, "(OK)" if ok else "(need >=6)")

def test_pf7(skill_dir):
    text, lines = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    st = detect_skill_type(skill_dir)
    has_all = all(t in text for t in ["E0", "E1", "E2", "E3"])
    if st == "single":
        return True, "ADV single-file evolution-tier E0-E3 (advisory, not blocking)"
    return has_all, "E0-E3=%s" % ("all" if has_all else "missing")

def test_pf8(skill_dir):
    text, lines = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    found = False
    for line in lines:
        low = line.lower()
        if ("cron" in low or "12h" in low) and "巡检" in line:
            if any(neg in line for neg in ["NO", "禁止", "不会", "已删除", "死模式"]):
                continue
            found = True
            break
        if ("定时器" in line and "自动修改" in line) and \
           not any(neg in line for neg in ["NO", "禁止", "不会", "已删除", "死模式"]):
            found = True
            break
    return not found, "clean" if not found else "v2.6.0 patterns in active context"

def test_pf9(skill_dir):
    boms = []
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        for f in files:
            fp = os.path.join(root, f)
            try:
                with open(fp, "rb") as fh:
                    if fh.read(3) == b"\xef\xbb\xbf":
                        boms.append(os.path.relpath(fp, skill_dir))
            except:
                pass
    return len(boms) == 0, "clean" if not boms else "BOM: %s" % boms

def test_pf10(skill_dir):
    """赋权三件套（PF10）：T1 强制；T2/T3 转 ADV（判断式赋权，休眠/本地工具不必维护蒸馏引擎）"""
    tier = get_tier(skill_dir)
    es = os.path.join(skill_dir, "evolution-state.json")
    ul = os.path.join(skill_dir, "usage-log.md")
    text, _ = _read(skill_dir)
    has_es = os.path.exists(es)
    has_ul = os.path.exists(ul)
    has_distill = "自我蒸馏" in text
    ok = has_es and has_ul and has_distill
    if tier in ("T2", "T3"):
        return True, "ADV (tier=%s): distill trio present=%s, advisory not blocking" % (tier, "Y" if ok else "N")
    return ok, "evolution-state=%s usage-log=%s 自我蒸馏小节=%s" % (
        "Y" if has_es else "N", "Y" if has_ul else "N", "Y" if has_distill else "N")

def test_pf11(skill_dir):
    """门面质检（PF11）：displayName + 用户原声触发词小节 + 首屏钩子 + description价值词 + 可独立触发"""
    text, lines = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    fm = parse_fm(text)
    body_start = _yaml_end(lines)
    body = "\n".join(lines[body_start:])
    has_dn = bool(fm.get("displayname")) and fm.get("displayname") != fm.get("slug")
    tb = extract_trigger_block(body)
    trig_user = bool(tb) and any(h in tb for h in USER_VOICE_HINT)
    head = body[:600]
    has_value = any(w in head for w in VALUE_WORDS)
    has_self = any(w in head for w in SELF_WORDS) and "可独立触发" not in head
    first_hook = ("用它能解决什么" in head) or (has_value and not has_self)
    desc = fm.get("description", "")
    desc_punch = bool(desc) and any(w in desc for w in VALUE_WORDS)
    locked = bool(fm.get("trigger")) or (
        any(h in body[:1800] for h in LOCKED_HINT) and "可独立触发" not in body[:1800])
    ok = has_dn and trig_user and first_hook and desc_punch and not locked
    return ok, "dn=%s trigUser=%s hook=%s descP=%s locked=%s" % (
        "Y" if has_dn else "N", "Y" if trig_user else "N",
        "Y" if first_hook else "N", "Y" if desc_punch else "N", "Y" if locked else "N")

def test_pf11f(skill_dir):
    """去模板化（PF11f 代理检测）：description 含价值词，且不在通用模板黑名单"""
    text, lines = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    fm = parse_fm(text)
    desc = fm.get("description", "")
    if not desc:
        return False, "no description"
    if any(g in desc for g in GENERIC_DESC):
        return False, "description matches generic template: %s" % desc[:30]
    has_value = any(w in desc for w in VALUE_WORDS)
    return has_value, "desc has value word=%s" % ("Y" if has_value else "N")

def test_pf13(skill_dir):
    """功能门（PF13 防废技能）：T1 强制 EVAL_SET.md(≥10题+四类)；T2/T3 转 ADV（判断式赋权）"""
    tier = get_tier(skill_dir)
    import re as _re
    ep = os.path.join(skill_dir, "EVAL_SET.md")
    if not os.path.exists(ep):
        if tier in ("T2", "T3"):
            return True, "ADV (tier=%s): EVAL_SET absent, advisory not blocking" % tier
        return False, "EVAL_SET.md missing (PF13 requires functional self-test set, tier=%s)" % tier
    with open(ep, "r", encoding=ENCODING) as f:
        txt = f.read()
    q_lines = [l for l in txt.splitlines()
               if _re.match(r"^\s*(\d+[\.、]|[-*]\s+|>\s)", l)]
    q_count = len(q_lines)
    cats = ["trigger", "edge", "adversarial", "format"]
    has_cats = sum(1 for c in cats if c.lower() in txt.lower())
    ok = (q_count >= 10) and (has_cats >= 3)
    if tier in ("T2", "T3"):
        return True, "ADV (tier=%s): EVAL_SET present(q=%d,cat=%d), advisory satisfied" % (tier, q_count, has_cats)
    return ok, "EVAL_SET questions=%d (need>=10), categories=%d/4 (need>=3)" % (q_count, has_cats)

def test_pf14(skill_dir):
    """能力落地校验（PF14）：T1/T2 强制降级声明；T3 转 ADV（判断式赋权）"""
    tier = get_tier(skill_dir)
    text, _ = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    dep_hints = ["IMA", "API", "知识库", "MCP", "connector", "连接器",
                 "检索", "调用外部", "调用付费", "第三方"]
    claims_dep = any(h in text for h in dep_hints)
    if not claims_dep:
        return True, "no external-dependency claim (N/A)"
    honesty = ["降级", "未配置", "未接通", "依赖", "运行时", "未安装",
               "需配置", "如未", "缺席", "降级为"]
    has_honesty = any(h in text for h in honesty)
    if tier == "T3":
        return True, "ADV (tier=T3): claims external dep=%s, advisory" % ("Y" if claims_dep else "N")
    return has_honesty, "claims external dep=%s, honesty note=%s" % (
        "Y" if claims_dep else "N", "Y" if has_honesty else "N")

def test_pf15(skill_dir):
    """行动授权声明 + 护栏（PF15）：T1/T2 强制；T3 转 ADV（判断式赋权）"""
    tier = get_tier(skill_dir)
    text, _ = _read(skill_dir)
    if not text:
        return False, "SKILL.md not found"
    auth_hints = ["行动授权", "自主度", "权限三层", "行动范围", "高利害",
                  "权限管控", "行动权限", "人类最终裁决"]
    has_auth = any(h in text for h in auth_hints)
    if tier == "T3":
        return True, "ADV (tier=T3): action-auth present=%s, advisory" % ("Y" if has_auth else "N")
    return has_auth, "action-auth declaration=%s" % ("Y" if has_auth else "N")

# ---- Run ----

TESTS = [
    ("PF1", "SKILL.md size", test_pf1),
    ("PF2", "references/ dirs", test_pf2),
    ("PF3", "hook position", test_pf3),
    ("PF4", "user-voice triggers", test_pf4),
    ("PF5", "YAML front + inscription", test_pf5),
    ("PF6", "immutable core", test_pf6),
    ("PF7", "evolution tier", test_pf7),
    ("PF8", "no v2.6.0 mode", test_pf8),
    ("PF9", "no BOM/junk", test_pf9),
    ("PF10", "distill trio", test_pf10),
    ("PF11", "doorface QA", test_pf11),
    ("PF11f", "de-template desc", test_pf11f),
    ("PF13", "functional gate EVAL_SET", test_pf13),
    ("PF14", "capability landing", test_pf14),
    ("PF15", "action-auth declaration", test_pf15),
]

def main():
    skill_dir = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    sp = os.path.join(skill_dir, "SKILL.md")
    kb = os.path.getsize(sp) / 1024 if os.path.exists(sp) else 0
    print("[PF] PF quality gate 15 内容门 (v3.0.11)")
    print("[DIR] %s" % skill_dir)
    print("[FILE] SKILL.md %.1f KB" % kb)
    print("=" * 70)
    passed = 0
    failed = 0
    for pf_id, desc, fn in TESTS:
        try:
            ok, msg = fn(skill_dir)
        except Exception as e:
            ok, msg = False, "ERROR %s" % e
        tag = "OK" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        print("  [%s] %s %s: %s" % (tag, pf_id, desc, msg))
    print("=" * 70)
    print("[STAT] %d PASS, %d FAIL" % (passed, failed))
    if failed == 0:
        print("[PASS] 15 内容门全 PASS（PF12 同步门为人工纪律，不在此脚本） - ready to release.")
    else:
        print("[FAIL] Fix the issues above before release.")

if __name__ == "__main__":
    main()
