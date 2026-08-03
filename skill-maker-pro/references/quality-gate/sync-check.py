#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PF12 同步门机检守卫 (v3.0.10)

目的：把「版本三重一致 / PF·AP 计数同步」从人工纪律变为可机检。
发布前运行：python sync-check.py [skill_dir]
默认 skill_dir = 本脚本所在 quality-gate/ 的上级（即元技能根目录）。

检查项：
  [V] 版本三重一致：SKILL.md frontmatter version == evolution-state.json version == auto-test.py 版本串
  [A] AP 计数一致：references/anti-patterns/*.md 中最大 AP 编号 == evolution-state.json ap_count
  [P] PF 计数一致：auto-test.py 的 TESTS 项数(内容门) + 1(PF12 同步门) == evolution-state.json pf_count
任一漂移 → 打印 FAIL 并以退出码 1 阻断发布；全过 → 退出码 0。

设计戒律：只查「规范↔文件↔统计」三方一致性，不重复 auto-test.py 的内容门逻辑。
"""
import sys, os, re, json

ENCODING = "utf-8-sig"


def _read(p):
    with open(p, "r", encoding=ENCODING) as f:
        return f.read()


def parse_fm_version(skill_dir):
    p = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(p):
        return None
    text = _read(p)
    m = re.search(r"(?s)^---\n(.*?)\n---", text)
    if not m:
        return None
    for ln in m.group(1).splitlines():
        mm = re.match(r"^version:\s*([\d.]+)", ln.strip())
        if mm:
            return mm.group(1)
    return None


def parse_es_version(skill_dir):
    p = os.path.join(skill_dir, "evolution-state.json")
    if not os.path.exists(p):
        return None
    d = json.loads(_read(p))
    return d.get("version")


def parse_auto_test_version(skill_dir):
    p = os.path.join(skill_dir, "references", "quality-gate", "auto-test.py")
    if not os.path.exists(p):
        return None
    text = _read(p)
    # 匹配 docstring 与打印行中的 (vX.Y.Z)
    vers = re.findall(r"\(v([\d.]+)\)", text)
    if not vers:
        return None
    # 取出现最多的版本串（去重后应唯一）
    uniq = sorted(set(vers), key=vers.count, reverse=True)
    return uniq[0] if len(uniq) == 1 else None  # 多版本串不一致时返回 None 触发告警


def parse_auto_test_content_pf_count(skill_dir):
    p = os.path.join(skill_dir, "references", "quality-gate", "auto-test.py")
    if not os.path.exists(p):
        return None
    text = _read(p)
    # TESTS = [ ("PF1", ...), ("PF11f", ...), ... ] → 统计元组首项以 PF 开头的数量
    m = re.search(r"TESTS\s*=\s*\[(.*?)\]", text, re.S)
    if not m:
        return None
    return len(re.findall(r"\n\s*\(\"PF", m.group(1)))


def parse_max_ap(skill_dir):
    ap_dir = os.path.join(skill_dir, "references", "anti-patterns")
    if not os.path.isdir(ap_dir):
        return None
    max_ap = 0
    for fn in os.listdir(ap_dir):
        if not fn.endswith(".md"):
            continue
        text = _read(os.path.join(ap_dir, fn))
        for num in re.findall(r"AP(\d+)", text):
            max_ap = max(max_ap, int(num))
    return max_ap


def parse_es_counts(skill_dir):
    p = os.path.join(skill_dir, "evolution-state.json")
    if not os.path.exists(p):
        return None, None
    d = json.loads(_read(p))
    return d.get("pf_count"), d.get("dimensions", {}).get("ap_count", {}).get("current")


def main():
    skill_dir = os.path.abspath(
        sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    print("[PF12] 同步门机检守卫 (v3.0.10)")
    print("[DIR] %s" % skill_dir)
    print("=" * 70)

    checks = []

    # [V] 版本三重一致
    v_fm = parse_fm_version(skill_dir)
    v_es = parse_es_version(skill_dir)
    v_at = parse_auto_test_version(skill_dir)
    v_ok = (v_fm == v_es == v_at) and v_fm is not None
    checks.append(("[V] 版本三重一致", v_ok,
                   "SKILL.md=%s | evolution-state=%s | auto-test=%s" % (v_fm, v_es, v_at)))

    # [A] AP 计数一致
    ap_max = parse_max_ap(skill_dir)
    _, ap_es = parse_es_counts(skill_dir)
    a_ok = (ap_max is not None and ap_es is not None and ap_max == ap_es)
    checks.append(("[A] AP 计数一致", a_ok,
                   "references 最大 AP=%s | evolution-state ap_count=%s" % (ap_max, ap_es)))

    # [P] PF 计数一致
    pf_content = parse_auto_test_content_pf_count(skill_dir)
    pf_es, _ = parse_es_counts(skill_dir)
    # 内容门 + PF12 同步门 应等于 pf_count
    p_ok = (pf_content is not None and pf_es is not None and pf_content + 1 == pf_es)
    checks.append(("[P] PF 计数一致", p_ok,
                   "auto-test 内容门=%s (+PF12=1) | evolution-state pf_count=%s" % (pf_content, pf_es)))

    failed = 0
    for name, ok, detail in checks:
        tag = "OK" if ok else "FAIL"
        if not ok:
            failed += 1
        print("  [%s] %s: %s" % (tag, name, detail))

    print("=" * 70)
    if failed == 0:
        print("[PASS] PF12 同步门全一致 - 版本/计数无漂移，可发布。")
        return 0
    print("[FAIL] %d 项漂移 - 先 sync（SKILL.md / evolution-state.json / auto-test.py 版本与计数对齐）再发布。" % failed)
    return 1


if __name__ == "__main__":
    sys.exit(main())
