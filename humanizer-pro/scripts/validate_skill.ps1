<#
.SYNOPSIS
  Skill validation script — checks SKILL.md structure and metadata
.DESCRIPTION
  Lightweight validation for prompt-based Skills.
  Verifies YAML frontmatter, required fields, and content structure.
#>
param([string]$SkillDir = $PSScriptRoot)

$ErrorActionPreference = "Stop"
$skillName = Split-Path $SkillDir -Leaf
$errors = 0
$warnings = 0

Write-Host "=== Skill Validation: $skillName ===" -ForegroundColor Cyan

# 1. SKILL.md exists
$mdPath = Join-Path $SkillDir "SKILL.md"
if (-not (Test-Path $mdPath)) {
    Write-Host "[FAIL] SKILL.md not found" -ForegroundColor Red
    $errors++
    exit 1
}
Write-Host "[PASS] SKILL.md exists" -ForegroundColor Green

# 2. Read content
$content = Get-Content $mdPath -Raw -Encoding UTF8
$lines = $content -split "`r?`n"

# 3. YAML frontmatter
$hasFrontmatter = ($lines[0].Trim() -eq '---')
if (-not $hasFrontmatter) {
    Write-Host "[FAIL] No YAML frontmatter" -ForegroundColor Red
    $errors++
} else {
    Write-Host "[PASS] YAML frontmatter present" -ForegroundColor Green
    
    # Extract YAML
    $yaml = @{}
    $inYaml = $false
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq '---' -and -not $inYaml) { $inYaml = $true; continue }
        if ($lines[$i].Trim() -eq '---' -and $inYaml) { break }
        if ($inYaml -and $lines[$i].Trim() -match '^(.+?):\s*(.*)') {
            $yaml[$matches[1]] = $matches[2].Trim()
        }
    }
    
    # Required fields
    $required = @("name","version","description","author","license")
    foreach ($f in $required) {
        if ($yaml.ContainsKey($f) -and $yaml[$f]) {
            Write-Host "[PASS] $f = $($yaml[$f].Substring(0,[Math]::Min(50,$yaml[$f].Length)))" -ForegroundColor Green
        } else {
            Write-Host "[FAIL] Missing required field: $f" -ForegroundColor Red
            $errors++
        }
    }
}

# 4. Content length
$contentLen = $content.Length
if ($contentLen -lt 2000) {
    Write-Host "[WARN] Content too short: ${contentLen} chars (min 2000)" -ForegroundColor Yellow
    $warnings++
} else {
    Write-Host "[PASS] Content length: ${contentLen} chars" -ForegroundColor Green
}

# 5. Has triggers or usage
if ($content -match 'triggers:|触发|关键词|使用场景|Usage') {
    Write-Host "[PASS] Trigger/usage section found" -ForegroundColor Green
} else {
    Write-Host "[WARN] No trigger/usage section" -ForegroundColor Yellow
    $warnings++
}

# 6. No internal references
$internal = @("乾穹","Tiangongge","tiangongge","天工阁","14脑","八卦","代谢管线")
$foundInternal = @()
foreach ($term in $internal) {
    if ($content -match [regex]::Escape($term)) {
        $foundInternal += $term
    }
}
if ($foundInternal.Count -gt 0) {
    Write-Host "[FAIL] Internal references found: $($foundInternal -join ', ')" -ForegroundColor Red
    $errors++
} else {
    Write-Host "[PASS] No internal references" -ForegroundColor Green
}

# Summary
Write-Host ""
if ($errors -eq 0 -and $warnings -eq 0) {
    Write-Host "=== RESULT: PASS (0 errors, 0 warnings) ===" -ForegroundColor Green
    exit 0
} elseif ($errors -eq 0) {
    Write-Host "=== RESULT: CONDITIONAL PASS ($errors errors, $warnings warnings) ===" -ForegroundColor Yellow
    exit 0
} else {
    Write-Host "=== RESULT: FAIL ($errors errors, $warnings warnings) ===" -ForegroundColor Red
    exit 1
}
