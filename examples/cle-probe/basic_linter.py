#!/usr/bin/env python3
"""
基础正则 Linter — 模拟 clang-tidy / Bandit 的基础检测能力
用于与 CLE Code Probe 做检出率对照。

这个 linter 只做最基础的正则匹配，不做 AST 解析、不做跨函数分析、
不做污点传播、不做证据融合——代表"标准 linter 的基础能力上限"。
"""

import re
import sys
import json
from pathlib import Path


# ── 基础正则规则集（模拟 clang-tidy / cppcheck / Bandit 的基础检测） ──
BASIC_RULES = [
    {
        "id": "B001",
        "name": "malloc未检查NULL",
        "severity": "P0",
        "category": "RESOURCE_BOUND",
        "pattern": r'(?:char|int|void|\w+)\s*\*\s*\w+\s*=\s*\([^)]*\)\s*malloc\s*\(',
        "description": "malloc返回值未检查NULL（基础正则只能检测malloc调用，无法判断后续是否有NULL检查）",
    },
    {
        "id": "B002",
        "name": "除零风险",
        "severity": "P0",
        "category": "STATE_BOUNDEDNESS",
        "pattern": r'/\s*(?:0|0x0|0\.0|0\.0f)\b',
        "description": "直接除以常量零（基础正则只能检测常量除零，无法检测变量除零）",
    },
    {
        "id": "B003",
        "name": "sprintf无边界",
        "severity": "P1",
        "category": "BUFFER_OVERFLOW",
        "pattern": r'\bsprintf\s*\(',
        "description": "使用sprintf（无边界的字符串格式化）",
    },
    {
        "id": "B004",
        "name": "strcpy无边界",
        "severity": "P1",
        "category": "BUFFER_OVERFLOW",
        "pattern": r'\bstrcpy\s*\(',
        "description": "使用strcpy（无边界的字符串拷贝）",
    },
    {
        "id": "B005",
        "name": "gets危险函数",
        "severity": "P0",
        "category": "BUFFER_OVERFLOW",
        "pattern": r'\bgets\s*\(',
        "description": "使用gets（已被C11标准移除的危险函数）",
    },
    {
        "id": "B006",
        "name": "system命令注入",
        "severity": "P0",
        "category": "COMMAND_INJECTION",
        "pattern": r'\bsystem\s*\(',
        "description": "调用system()（可能存在命令注入风险，基础正则无法判断参数是否可控）",
    },
    {
        "id": "B007",
        "name": "scanf无边界",
        "severity": "P1",
        "category": "BUFFER_OVERFLOW",
        "pattern": r'\bscanf\s*\([^)]*%s',
        "description": "scanf使用%s无宽度限制（可能导致缓冲区溢出）",
    },
    {
        "id": "B008",
        "name": "硬编码密码",
        "severity": "P1",
        "category": "HARDCODED_SECRET",
        "pattern": r'(?:password|passwd|pwd|secret|api_key|token)\s*=\s*["\'][^"\']+["\']',
        "description": "硬编码密码或密钥（基础正则匹配）",
    },
]


def strip_comments_and_strings(code):
    """剥离注释和字符串字面量（基础版，不处理跨行）"""
    # 移除单行注释
    code = re.sub(r'//[^\n]*', '', code)
    # 移除多行注释（基础版）
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # 移除字符串字面量（基础版）
    code = re.sub(r'"[^"]*"', '""', code)
    return code


def run_basic_linter(file_path):
    """运行基础正则 linter"""
    code = Path(file_path).read_text(encoding="utf-8", errors="replace")
    # 不剥离注释，因为基础linter通常也会检测注释中的内容（虽然不应该）
    # 这里做基础版：只剥离字符串，不剥离注释
    code_for_scan = re.sub(r'"[^"]*"', '""', code)

    findings = []
    lines = code.split("\n")

    for rule in BASIC_RULES:
        for match in re.finditer(rule["pattern"], code_for_scan):
            # 计算行号
            line_num = code_for_scan[:match.start()].count("\n") + 1
            line_text = lines[line_num - 1].strip() if line_num <= len(lines) else ""
            findings.append({
                "rule_id": rule["id"],
                "name": rule["name"],
                "severity": rule["severity"],
                "category": rule["category"],
                "line": line_num,
                "line_text": line_text[:80],
                "description": rule["description"],
            })

    p0_count = sum(1 for f in findings if f["severity"] == "P0")
    p1_count = sum(1 for f in findings if f["severity"] == "P1")

    return {
        "linter": "basic_regex_linter",
        "file": str(file_path),
        "total_findings": len(findings),
        "p0_count": p0_count,
        "p1_count": p1_count,
        "findings": findings,
        "limitations": [
            "仅正则匹配，无AST解析",
            "无跨函数分析",
            "无污点传播分析",
            "无证据融合",
            "无法判断malloc后是否有NULL检查",
            "无法判断变量除零（只能检测常量除零）",
            "无法判断system()参数是否可控",
        ],
    }


def main():
    if len(sys.argv) < 2:
        print("用法: python basic_linter.py <file.c> [--json]")
        sys.exit(1)

    file_path = sys.argv[1]
    output_json = "--json" in sys.argv

    result = run_basic_linter(file_path)

    if output_json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"基础正则 Linter — {file_path}")
        print(f"总发现: {result['total_findings']} (P0={result['p0_count']}, P1={result['p1_count']})")
        print()
        for f in result["findings"]:
            print(f"  [{f['severity']}] {f['rule_id']} {f['name']} line {f['line']}")
            print(f"       {f['line_text']}")
        print()
        print("局限性:")
        for lim in result["limitations"]:
            print(f"  - {lim}")


if __name__ == "__main__":
    main()
