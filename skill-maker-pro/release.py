#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v3.0.0 Release Script - Automated packaging + backup + BOM/junk cleanup

Functions:
1. Verify PF quality gate (auto-test.py 9 items)
2. Backup to F:\\QClaw工作空间\\技能创作\\自制技能\\<CN-Name>\\v<Version>\\
3. Clean .git/, %TEMP%, __pycache__, .DS_Store etc.
4. Check/remove UTF-8 BOM
5. Package to zip (no BOM)
6. Output release report

Usage:
    python release.py <skill_dir> [--dry-run] [--skip-pf]
    python release.py F:\\QClaw工作空间\\技能创作\\v3.0-workshop\\drafts\\v3.0-skill --dry-run

Paths (v3.0.0+):
    --backup-base DIR   Backup base (default: $SKILL_BACKUP_BASE or F:\\QClaw工作空间\\技能创作\\自制技能)
    --release-dir DIR   Release output (default: $SKILL_RELEASE_DIR or F:\\QClaw工作空间\\技能创作\\v3.0-workshop\\release)
    Env: SKILL_BACKUP_BASE / SKILL_RELEASE_DIR
    Note: As of v3.0.0, the canonical backup path is F:\\QClaw工作空间\\技能创作淺\自制技能絓\<CN-Name>\\v<Version>\\
          (user's local rule from 2026-07-06, MEMORY.md 铁规则?.
"""

import sys
import os
import re
import json
import shutil
import zipfile
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Tuple


# Junk file/directory patterns
JUNK_PATTERNS = [
    ".git",
    ".DS_Store",
    "Thumbs.db",
    "__pycache__",
    "*.pyc",
    "*.pyo",
    ".pytest_cache",
    ".mypy_cache",
    ".vscode",
    ".idea",
    "*.swp",
    "*~",
    ".env",
    "*.log",
    "*.tmp",
    "%TEMP%residue_check.txt",
    "node_modules",
    "dist",
    "build",
    "*.egg-info",
]


# Chinese name mapping (v3.0.0 maintained 27 skills)
SKILL_NAME_MAP = {
    "skill-maker-pro": "技能制作专家Pro",
    "humanizer-pro": "文风润色专家Pro",
    "data-analyst-pro": "数据分析专家Pro",
    "doc-qa-pro": "文档问答专家Pro",
    "translate-pro": "翻译专家Pro",
    "ppt-pro": "PPT制作专家Pro",
    "script-gen-pro": "脚本生成专家Pro",
    "office-auto-pro": "办公自动化专家Pro",
    "multimodal-pro": "多模态专家Pro",
    "prompt-engineer": "提示词专家",
    "life-plan-pro": "人生规划专家Pro",
    "academic-paper-workshop": "学术论文工作坊",
    "abstract-optimizer": "摘要优化器",
    "plagiarism-precheck": "查重预检专家",
    "literature-mining": "文献挖掘专家",
    "academic-writing-bank": "学术写作词库",
    "academic-docx-toolkit": "学术DOCX工具包",
    "academic-figure-gen": "学术配图生成",
    "academic-chart-gen": "学术图表生成",
    "paper-version-manager": "论文版本管理器",
    "reference-formatter": "参考文献格式化",
    "submission-helper": "投稿助手",
    "paper-review-methodology": "论文审查方法论",
}


def log(level, msg):
    """Unified log output"""
    icons = {"INFO": "[INFO]", "WARN": "[WARN]", "ERROR": "[ERROR]", "OK": "[OK]"}
    print(f"{icons.get(level, '[LOG]')} {msg}")


def find_junk_files(skill_dir):
    """Find junk files"""
    junk = []
    for pattern in JUNK_PATTERNS:
        for item in skill_dir.rglob(pattern):
            if item.is_file() or item.is_dir():
                junk.append(item)
    return sorted(set(junk))


def check_bom(skill_dir):
    """Check UTF-8 BOM files"""
    bom_files = []
    for f in skill_dir.rglob("*.md"):
        try:
            with open(f, "rb") as fp:
                first_bytes = fp.read(3)
                if first_bytes == b"\xef\xbb\xbf":
                    bom_files.append(f)
        except Exception:
            pass
    return bom_files


def remove_bom(skill_dir):
    """Remove UTF-8 BOM, return processed file count"""
    count = 0
    for f in skill_dir.rglob("*.md"):
        try:
            with open(f, "rb") as fp:
                data = fp.read()
            if data.startswith(b"\xef\xbb\xbf"):
                data = data[3:]
                with open(f, "wb") as fp:
                    fp.write(data)
                count += 1
                log("OK", f"  Removed BOM: {f.name}")
        except Exception as e:
            log("WARN", f"  Skip BOM process {f.name}: {e}")
    return count


def read_skill_metadata(skill_dir):
    """Read name/version/slug from SKILL.md"""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {}
    
    content = skill_md.read_text(encoding="utf-8")
    metadata = {}
    
    for key in ["name", "version", "slug", "displayName"]:
        m = re.search(rf"^{key}:\s*(.+?)$", content, re.MULTILINE)
        if m:
            metadata[key] = m.group(1).strip()
    
    return metadata


def get_chinese_name(slug):
    """slug -> Chinese name (Pinyin placeholder, real CN name in v3.1)"""
    return SKILL_NAME_MAP.get(slug, slug)


def backup_to_local(skill_dir, metadata, backup_base=None):
    """Backup to <backup_base>/<CN-Name>/v<Version>/
    
    Args:
        skill_dir: Source skill directory
        metadata: dict with 'slug', 'version', etc.
        backup_base: Override default backup base path (else use env SKILL_BACKUP_BASE or default).
                     Default: F:\\QClaw工作空间\\技能创作\\自制技能
                     Recommended per user rule: F:\\QClaw工作空间\\技能创作淺\自制技能絓\
    """
    slug = metadata.get("slug", skill_dir.name)
    version = metadata.get("version", "v0.0.0")
    cn_name = get_chinese_name(slug)
    
    if backup_base is None:
        backup_base = os.environ.get(
            "SKILL_BACKUP_BASE",
            r"F:\QClaw工作空间\技能创作\自制技能"
        )
    backup_base = Path(backup_base)
    backup_dir = backup_base / cn_name / f"v{version}"
    
    if backup_dir.exists():
        log("WARN", f"Backup directory exists: {backup_dir}")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = backup_base / cn_name / f"v{version}_{ts}"
        log("INFO", f"Changed to: {backup_dir}")
    
    backup_dir.mkdir(parents=True, exist_ok=True)
    log("INFO", f"Backup to: {backup_dir}")
    
    for item in skill_dir.rglob("*"):
        if item.is_file():
            rel = item.relative_to(skill_dir)
            dest = backup_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest)
    
    log("OK", f"  Backup complete: {len(list(backup_dir.rglob('*')))} items")
    return backup_dir


def clean_junk(skill_dir, dry_run=False):
    """Clean junk files"""
    junk = find_junk_files(skill_dir)
    if not junk:
        log("OK", "No junk files")
        return []
    
    log("INFO", f"Found {len(junk)} junk items:")
    for j in junk:
        rel = j.relative_to(skill_dir)
        log("INFO", f"  {rel}")
        if not dry_run:
            try:
                if j.is_dir():
                    shutil.rmtree(j)
                else:
                    j.unlink()
            except Exception as e:
                log("WARN", f"  Delete failed: {e}")
    
    return junk


def make_zip(skill_dir, metadata, release_dir=None):
    """Package to zip (no BOM, no junk)
    
    Args:
        skill_dir: Source skill directory
        metadata: dict with 'slug', 'version', etc.
        release_dir: Override default release output (else use env SKILL_RELEASE_DIR or default).
                     Default: F:\\QClaw工作空间\\技能创作\\v3.0-workshop\\release
    """
    slug = metadata.get("slug", skill_dir.name)
    version = metadata.get("version", "v0.0.0")
    
    if release_dir is None:
        release_dir_str = os.environ.get(
            "SKILL_RELEASE_DIR",
            r"F:\QClaw工作空间\技能创作\v3.0.0-workshop\release"
        )
        release_dir = Path(release_dir_str)
    release_dir.mkdir(parents=True, exist_ok=True)
    
    zip_name = f"{slug}_v{version}_clean.zip"
    zip_path = release_dir / zip_name
    
    if zip_path.exists():
        zip_path.unlink()
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in skill_dir.rglob("*"):
            if item.is_file():
                rel = item.relative_to(skill_dir)
                arcname = f"{slug}/{rel.as_posix()}"
                zf.write(item, arcname)
    
    size_kb = zip_path.stat().st_size / 1024
    log("OK", f"  Package complete: {zip_path} ({size_kb:.1f} KB)")
    return zip_path


def run_pf_check(skill_dir):
    """Run PF quality gate (auto-test.py)"""
    pf_script = skill_dir / "references" / "quality-gate" / "auto-test.py"
    if not pf_script.exists():
        log("ERROR", f"PF script not found: {pf_script}")
        return False
    
    log("INFO", "Running PF quality gate (auto-test.py 9 items)...")
    try:
        result = subprocess.run(
            [sys.executable, str(pf_script), str(skill_dir)],
            capture_output=True, text=True, timeout=60
        )
        print(result.stdout)
        if result.stderr:
            log("WARN", f"stderr: {result.stderr[:500]}")
        return result.returncode == 0
    except Exception as e:
        log("ERROR", f"PF check failed: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="v3.0.0 Release Script")
    parser.add_argument("skill_dir", help="Skill directory path")
    parser.add_argument("--dry-run", action="store_true", help="Dry run, no actual modification/packaging")
    parser.add_argument("--skip-pf", action="store_true", help="Skip PF quality gate (not recommended)")
    parser.add_argument("--skip-backup", action="store_true", help="Skip local backup")
    parser.add_argument("--skip-zip", action="store_true", help="Skip zip packaging")
    parser.add_argument("--backup-base", type=str, default=None,
                        help="Backup base directory (default: $SKILL_BACKUP_BASE or F:\\\\QClaw工作空间\\\\技能创作\\\\自制技能)")
    parser.add_argument("--release-dir", type=str, default=None,
                        help="Release output directory (default: $SKILL_RELEASE_DIR or F:\\\\QClaw工作空间\\\\技能创作\\\\v3.0-workshop\\\\release)")
    args = parser.parse_args()
    
    skill_dir = Path(args.skill_dir)
    if not skill_dir.exists():
        log("ERROR", f"Skill directory not found: {skill_dir}")
        sys.exit(2)
    
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        log("ERROR", f"SKILL.md not found: {skill_md}")
        sys.exit(2)
    
    log("INFO", "=" * 70)
    log("INFO", "v3.0.0 Release Script (argparse + env var support)")
    log("INFO", f"Skill directory: {skill_dir}")
    log("INFO", f"Mode: {'DRY-RUN' if args.dry_run else 'REAL PUBLISH'}")

    _default_backup = r"F:\QClaw工作空间\技能创作\自制技能"
    _default_release = r"F:\QClaw工作空间\技能创作\v3.0.0-workshop\release"
    _actual_backup = args.backup_base or os.environ.get("SKILL_BACKUP_BASE", _default_backup)
    _actual_release = args.release_dir or os.environ.get("SKILL_RELEASE_DIR", _default_release)
    log("INFO", f"Backup base: {_actual_backup}")
    log("INFO", f"Release dir: {_actual_release}")
    log("INFO", "=" * 70)
    
    # Step 1: Read metadata
    log("INFO", "")
    log("INFO", "Step 1: Read SKILL.md metadata")
    metadata = read_skill_metadata(skill_dir)
    if not metadata:
        log("ERROR", "Cannot read metadata from SKILL.md")
        sys.exit(1)
    log("OK", f"  name: {metadata.get('name')}")
    log("OK", f"  displayName: {metadata.get('displayName')}")
    log("OK", f"  version: {metadata.get('version')}")
    log("OK", f"  slug: {metadata.get('slug')}")
    
    # Step 2: Check BOM
    log("INFO", "")
    log("INFO", "Step 2: Check UTF-8 BOM")
    bom_files = check_bom(skill_dir)
    if bom_files:
        log("WARN", f"  Found {len(bom_files)} BOM files")
        if not args.dry_run:
            removed = remove_bom(skill_dir)
            log("OK", f"  Removed BOM from {removed} files")
    else:
        log("OK", "  No BOM files")
    
    # Step 3: Clean junk
    log("INFO", "")
    log("INFO", "Step 3: Clean junk files")
    clean_junk(skill_dir, dry_run=args.dry_run)
    
    # Step 4: PF quality gate
    if not args.skip_pf:
        log("INFO", "")
        log("INFO", "Step 4: PF quality gate (9-item auto check)")
        if not run_pf_check(skill_dir):
            log("ERROR", "PF quality gate failed, aborting")
            sys.exit(1)
        log("OK", "  PF quality gate 9/9 passed")
    
    # Step 5: Local backup
    if not args.skip_backup:
        log("INFO", "")
        log("INFO", "Step 5: Local backup")
        if args.dry_run:
            log("INFO", "  [DRY-RUN] Skip actual backup")
        else:
            backup_dir = backup_to_local(skill_dir, metadata, backup_base=args.backup_base)
            log("OK", f"  Backup complete: {backup_dir}")
    
    # Step 6: Package
    if not args.skip_zip:
        log("INFO", "")
        log("INFO", "Step 6: Package zip")
        if args.dry_run:
            log("INFO", "  [DRY-RUN] Skip actual packaging")
        else:
            zip_path = make_zip(skill_dir, metadata, release_dir=args.release_dir)
            log("OK", f"  Release package: {zip_path}")
    
    log("INFO", "")
    log("INFO", "=" * 70)
    log("OK", "Release process complete")
    if args.dry_run:
        log("INFO", "[DRY-RUN mode] Files not actually modified")
    log("INFO", "=" * 70)


if __name__ == "__main__":
    main()
