> **Source**: https://github.com/banbanry/pef-architecture/03-operator-library
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生


# PEF 算子库补充 — 3.8探针系统适配

PEF算子库补充文档

CLE V3.8.2 代码探针系统

11个E层算子适配集成 + 95项发现报告

日期: 2026-09-02

## 1. 概述

本文档记录从PEF算子库(500+条)中系统性筛选11个E层算子适配为CLE确定性探针的过程。这些算子分为两批集成:

1. 第一批(B1): 5+1个算子，覆盖空包占位符、逻辑链断裂、死代码等
1. 第二批(B2): 6个算子，覆盖内存安全、资源泄漏、路径覆盖等
## 2. PEF算子映射表 (11个算子)

## 3. 河图洛书代码扫描统计

对河图洛书工程化重构代码(C++17, 约1100行)执行11个PEF算子扫描，共检出95个问题:

### 3.1 按严重级别

### 3.2 按检测类别

## 4. 管线集成修复 (3个致命断裂)

在集成PEF算子时发现原有管线存在三个致命断裂点，导致L1和L2都无法检测出上述95个问题:

### 4.1 断裂点1: PEF算子未接入L1管线

run_audit()只调用run_phase5_pipeline()运行原始4个CLE算子。11个PEF算子完全游离于管线之外。原始4算子设计目标是C风格危险函数(malloc/system/scanf)，对C++代码检出为0。

修复F1: 在run_audit()返回前调用run_pef_operators()，将95个发现合并到findings列表，P0自动升级裁决为FAIL。

### 4.2 断裂点2: L2提示词主动排除检测项

L2提示词第69行写"不要重复Layer 1已经能检测的模式"。但L1原始4算子对C++代码检出为0！AI被告知跳过L1"能检测"的模式。同时L2的10类盲区清单缺少7类PEF覆盖的类别。

修复F2: 从10类盲区扩展为15类全量审查清单，删除排除指令，删除50000字符截断，新增来源溯源要求。

### 4.3 断裂点3: L2是被动空壳

run_dual_layer_audit()只生成文本提示返回awaiting_layer2状态，不调用AI模型也不执行检测。如果AI不执行真实审查，L2产出为空。

修复F3: 新增run_layer2_deterministic_fallback()，当AI未返回结果时自动执行PEF算子作为确定性补充。

## 5. 修复前后对比

## 6. P0严重问题详情 (4个)

以下4个P0问题由E039 ASan(BufferOverflowDetector)检出，是河图洛书代码中最严重的安全缺陷:

--- 文档结束 ---

| PEF编号 | 算子来源 | CLE适配类 | 检测能力 | 级别 | 检出 | 批次 | 检测模式 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E033 | Frama-C | PlaceholderDetector | 空包占位符检测 | P1 | 2 | B1 | 检测TODO/FIXME/暂不实现注释和空函数体 |
| E056 | CEGAR | LogicChainVerifier | 逻辑链断裂检测 | P1 | 5 | B1 | 检测load/init返回值未检查、未初始化变量使用、死参数 |
| E034 | Astree | DeadCodeDetector | 死代码/死参数检测 | P1 | 7 | B1 | 检测kd=0.0等配置参数导致代码路径失效 |
| E022 | Z3 SMT | MathPropertyVerifier | 数学性质验证 | P1 | 3 | B1 | 检测static_cast窄化溢出、取模碰撞、clamp范围不一致 |
| E040 | UBSan | StringLiteralValidator | 字符串有效性验证 | P1 | 1 | B1 | 检测find("NULL_check")等无效搜索串 |
| E035 | CBMC | UnimplementedDeclDetector | 未实现声明检测 | P1 | 26 | B1 | 检测头文件声明但源文件无实现定义的函数 |
| E039 | ASan | BufferOverflowDetector | 缓冲区溢出/越界检测 | P0*4 | 45 | B2 | 检测find()返回npos后直接substr、数组索引无边界检查 |
| E041 | MSan | UninitMemoryDetector | 未初始化内存检测 | P1 | 0 | B2 | 检测声明后未赋值参与运算、new后未初始化 |
| E043 | Valgrind | ResourceLeakDetector | 资源泄漏检测 | P1 | 2 | B2 | 检测文件句柄未关闭、new后无delete、异常路径泄漏 |
| E150 | CBMC | IntegerOverflowDetector | 整数溢出检测 | P1 | 0 | B2 | 检测乘法无范围检查、移位丢符号位、窄化转换 |
| E049 | KLEE | PathCoverageAnalyzer | 路径覆盖分析 | P1 | 4 | B2 | 检测恒真恒假条件、switch缺default、return后不可达代码 |
| E042 | TSan | RaceConditionDetector | 数据竞争检测 | P1 | 0 | B2 | 检测静态变量无锁修改、check-then-act竞态、public成员暴露 |


| 严重级别 | 数量 |
| --- | --- |
| P0 (严重) | 4 |
| P1 (高危) | 91 |
| 总计 | 95 |


| 检测类别 | 数量 | PEF来源 |
| --- | --- | --- |
| BUFFER_OVERFLOW 缓冲区溢出 | 45 | E039 ASan |
| UNIMPLEMENTED 未实现声明 | 26 | E035 CBMC |
| DEAD_CODE 死代码 | 7 | E034 Astree |
| LOGIC_CHAIN 逻辑链断裂 | 5 | E056 CEGAR |
| PATH_COVERAGE 路径覆盖 | 4 | E049 KLEE |
| MATH_PROPERTY 数学性质 | 3 | E022 Z3 SMT |
| PLACEHOLDER 空包占位符 | 2 | E033 Frama-C |
| RESOURCE_LEAK 资源泄漏 | 2 | E043 Valgrind |
| INVALID_PATTERN 无效字符串 | 1 | E040 UBSan |
| UNINIT_MEMORY 未初始化内存 | 0 | E041 MSan |
| INTEGER_OVERFLOW 整数溢出 | 0 | E150 CBMC |
| RACE_CONDITION 数据竞争 | 0 | E042 TSan |


| 指标 | 修复前 | 修复后 |
| --- | --- | --- |
| L1检出 | 0个 | 95个 (P0=4, P1=91) |
| 裁决 | PASS (假PASS) | FAIL |
| L2提示词类别 | 10类 (排除L1模式) | 15类 (全量审查) |
| L2源码截断 | 50000字符截断 | 无截断(全量) |
| L2回退机制 | 无(空壳) | PEF确定性回退 |
| PEF算子集成 | 游离于管线外 | 11算子接入run_audit() |


| 行号 | 级别 | 描述 | 修复建议 |
| --- | --- | --- | --- |
| 567 | P0 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |
| 569 | P0 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |
| 571 | P0 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |
| 573 | P0 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |




---
*PEF Architecture © 2026 banbanry (沈鹭). Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
