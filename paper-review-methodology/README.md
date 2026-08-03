# Paper Review Methodology / 学术论文全面审查方法论

> From 15+ real-world review iterations and 4 major versions — now packaged as a reusable OpenClaw skill, with 29 methods across 7 systems including desensitization review.

> 从15+次真实论文审查迭代和4个大版本中提炼出的29类全面审查方法论（含脱敏筛查），封装为可复用的 OpenClaw 技能。

---

## Overview

This skill provides a systematic framework for reviewing academic papers, covering every aspect from macro-level assessment to sentence-level execution. It was developed through extensive practice reviewing a Chinese engineering master's thesis across 15+ iterations from v11 to V3.0.10 (scores evolving from 71 to 91.5).

29 review methods are organized into **7 major systems**, enabling structured, repeatable, and auditable paper reviews.

## What's Inside

### 7 Major Systems

| # | System | Methods | Key Capabilities |
|---|--------|:-------:|-----------------|
| I | **Macro Assessment** | 4 | 4-dimension scoring, score tracking, 19-point review, 3-step expert review |
| II | **Problem Grading** | 3 | P0-P3 severity classification, hard/soft error taxonomy, data ripple effect analysis |
| III | **Specialized Review** | 8 | Figure citation audit, text-figure decoupling, AI-language purification, module consistency |
| IV | **Structural Comparison** | 3 | Architecture conflict analysis, cross-version reference audit, dual-version scoring |
| V | **Data Compliance** | 5 | Data authenticity, dual-attribution, abstract symmetry, reference check, desensitization review |
| VI | **Requirement Audit** | 3 | 14-decision audit, 7-expert-requirement audit, safe baseline strategy |
| VII | **Execution Methods** | 3 | Modification checklist, paragraph-by-paragraph comparison, P0 fix audit |

### Highlight Features

- **Desensitization Review (5-level L1-L5)** — systematic privacy audit for skills and papers before publishing, covering personal info, credentials, and proprietary data
- **P0/P1/P2/P3 Severity Grading** — industrial-grade defect classification adapted to academic papers
- **AI Language Purification (A/B/C levels)** — detect and rewrite AI-generated writing patterns specific to Chinese academic prose
- **Data Ripple Effect Analysis** — trace how a single data error propagates across chapters
- **Dual-Attribution Detection** — identify when the same metric is attributed to two different causes
- **Safe Baseline Strategy** — merge multiple versions while preserving data integrity
- **Score Evolution Tracking** — quantify paper quality improvements across revisions

## Usage Examples

### Quick Review
> "审查这篇论文" / "Review this paper"

The skill triggers automatically and applies the full 29-method framework.

### Figure Audit
> "检查论文的插图引用是否规范" / "Check if all figures are properly cited"

Runs specialized review #8 (figure citation audit), #9 (text-figure decoupling analysis), #10 (deletion feasibility).

### AI Language Check
> "检测论文中的AI生成痕迹" / "Detect AI-generated language patterns"

Runs specialized review #13 (A/B/C-level AI language framework).

### Version Comparison
> "对比V3.0和V3.1两个版本" / "Compare version V3.0 with V3.1"

Runs structural comparison #17 (cross-version reference audit) and #18 (dual-version scoring).

## Scoring Formula

```
Total Score = Content Completeness × 0.30
            + Logical Integrity × 0.25
            + Logical Closure × 0.25
            + AI Detection Score × 0.20

Quality threshold: 85/100 (submission-ready)
```

## File Structure

```
paper-review-methodology/
├── SKILL.md                              # Main skill file (navigation, workflow, scoring)
└── references/
    ├── macro-assessment.md               # Methods #1-4: Macro assessment
    ├── problem-grading.md                # Methods #5-7: Problem grading
    ├── specialized-review.md             # Methods #8-15: Specialized reviews
    ├── structural-comparison.md          # Methods #16-18: Structural comparison
    ├── data-compliance.md                # Methods #19-23: Data & compliance
    ├── requirement-audit.md              # Methods #24-26: Requirement audit
    └── execution-methods.md              # Methods #27-29: Execution methods
```

## Language Support

- **Primary**: Chinese (simplified) — all review templates and terminology in Chinese
- **Triggers**: Both Chinese and English trigger words supported
- **Output**: Chinese academic review reports

## Background

This methodology was developed and battle-tested during the review of an engineering master's thesis on industrial digitalization and traceability systems. Over 15 review iterations across 4 major version lineages, it evolved from ad-hoc feedback into a structured, comprehensive framework.

The real-world results: the thesis improved from an initial score of 71 to a final score of 91.5, with all P0 critical defects resolved and zero fabricated data points.

## Installation

```bash
# Via ClawHub
clawhub install paper-review-methodology

# Via SkillHub (China)
skillhub install paper-review-methodology
```

## 作者

人类Nan

## 许可

Open for academic use. Attribution appreciated.
