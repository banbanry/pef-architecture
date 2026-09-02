> **Source**: https://github.com/banbanry/pef-architecture/03-operator-library
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生

# 03 — PEF 算子库

本层是 PEF 三元架构（P/E/F）的**算子库**，包含完整细分、扩展版和工程适配补充。算子是 PEF 架构中可复用的基本操作单元，按 P（主体）/ E（变量）/ F（结果）三元分类。

## 文档列表

| 文档 | 内容 | 规模 |
|------|------|------|
| [operator-library-core.md](operator-library-core.md) | **算子库完整细分** — PEF 三元架构算子的完整分类和定义 | ~44K 字符 |
| [operator-library-v3-800.md](operator-library-v3-800.md) | **扩展版 V3.0 — 800条新算子** — 跨度 1600–2026 年，与原模板 680 条无重复，完整去重校验 | ~69K 字符 |
| [operator-library-3.8-probe.md](operator-library-3.8-probe.md) | **3.8探针系统适配补充** — CLE V3.8.2 代码探针系统的 11个E层算子适配集成 + 95项发现报告 | ~4K 字符 |

## 算子分类体系

PEF 算子按三元架构分类：

- **P 层算子（主体）**：主体声明、主体识别、主体边界定义、主体类型判定
- **E 层算子（变量）**：变量分流（E_in/E_out）、变量追踪、变量越界检测、势差计算
- **F 层算子（结果）**：结果生成、结果审计、结果追溯、PASS/FAIL 裁决

每个算子都绑定 π 锚坐标，确保可追溯、不可伪造。

## 阅读顺序

1. 先读 `operator-library-core.md` 理解完整分类体系
2. 再读 `operator-library-v3-800.md` 查看扩展算子
3. `operator-library-3.8-probe.md` 作为工程适配参考

## 与其他层的关系

算子库是 PEF 架构的**操作层**，向上支撑：
- `01-core-spec/` 中的设计规范定义了算子的使用规则
- `02-applications/` 中的应用扩展调用具体算子
- `04-engineering-cases/` 中的工程案例是算子的实际部署

---
*PEF Architecture © 2026 banbanry. Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
