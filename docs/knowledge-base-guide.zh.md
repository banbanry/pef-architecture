# PEF 架构 · 知识库导读与同步映射（GitHub 版）

> **Source**: https://github.com/banbanry/pef-architecture/docs/knowledge-base-guide.zh.md
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **English**: [knowledge-base-guide.en.md](knowledge-base-guide.en.md)
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生

本页是 PEF 架构公开仓库的**理论导读**，与飞书知识库同步映射。帮助读者快速定位：这个仓库是什么、文件怎么组织、核心理论是什么。

---

## 一、仓库定位（30 秒看懂）

**PEF（Positional Evidence Framework / Primary Entity–Execution Variable–Final Result）** 是一套锚定确定性元架构：以数学常数 π 为不可伪坐标轴，用 P（主体）/E（变量）/F（结果）三元原语约束 AI 行为，通过审计链、熔断、多模型对齐实现**可审计、可复算、可追溯**的 AI 产出。

**一句话**：给 AI 的产出盖"防伪身份证"，让幻觉、篡改、漂移无处遁形。

**核心主张**：唯锚才有势差产生（Only the anchor produces the potential difference）。锚是不可伪造、不可回退、全局唯一的基础——软件中是超越数 π，物理中是热力学定律。

---

## 二、仓库目录导读（34 个文件）

| 层级 | 内容 | 核心文档 |
|---|---|---|
| **根目录（入门）** | 5 个理论摘要 + Demo | [README](../README.md) · [primitives 原语](../primitives.md) · [pi-anchor π锚](../pi-anchor.md) · [mod3 三态](../mod3.md) · [topology 拓扑](../topology.md) · [axioms 公理](../axioms.md) · [demo_minimal.py](../demo_minimal.py) |
| **01-core-spec（核心规范）** | 完整设计规范 + 可执行引擎 | [7.6 Pro 设计规范](pef-7.6-pro-design-spec.md) · [三级闭环引擎规范](pef-three-tier-closed-loop-engine.md) · [引擎实现 pef_cl_engine.py](pef_cl_engine.py) · [端到端 pef_cl_e2e.py](pef_cl_e2e.py) · [时间理论附录](time-theory-appendix.md) |
| **02-applications（应用）** | π锚点应用扩展 | [CIC 跨模型治理](../02-applications/cic-cross-model-governance.md) · [PIMEM 基因记忆](../02-applications/pimem-genetic-memory.md) |
| **03-operator-library（算子库）** | P/E/F/M 四层算子 | [800算子库](../03-operator-library/operator-library-v3-800.md) · [CLE探针算子](../03-operator-library/operator-library-3.8-probe.md) |
| **04-engineering-cases（工程案例）** | CLE 探针落地 | [五阶段工作流](../04-engineering-cases/cle-probe/cle-five-stage-workflow.md) · [L1-L3技术](../04-engineering-cases/cle-probe/cle-l1-l3-technical.md) |
| **05-references（参考）** | 外部验证 | [AI编程三剑客](../05-references/ai-programming-trio.md) · [多模态幻觉报告](../05-references/multimodal-hallucination-report.md) |
| **推广文章** | 中文叙事 | [我用π做锚 — AI 可审计代码架构实验](../docs/promotion-article-zh.md) |

---

## 三、核心理论导读：三级闭环引擎

最新核心成果（2026-09-05 上线）：**PEF 三级闭环引擎**（内生循环 → 外部校准 → 多模型编译对齐）

| 级 | 环节 | 作用 | 代码 |
|---|---|---|---|
| ① | **内生循环（token深挖）** | 纯规则引擎切块打分，S/A/B/C 分级，零外部成本 | 参考实现见 01-core-spec 规范 |
| ② | **外部校准（多模型偏差）** | 12探针前置过滤 + GLM/Claude/GPT 独立裁决 | [pef_cl_engine.py](pef_cl_engine.py) |
| ③ | **多模型编译对齐** | P/E/F 统一Schema → 偏差率 ρ → PASS/FAIL 熔断 | 同上 |

**实测结果**（142 份灰烬语料）：低置信块全部 FAIL（ρ=0.57~0.87 多模型分歧熔断）、高置信块全部 PASS（ρ=0.02 一致通过）；16 条审计账本哈希链完整性通过。

运行方式：

```bash
# 离线演示（3场景 + 篡改检测）
python 01-core-spec/pef_cl_engine.py

# 端到端串联（读取 tier1 中间结果 → 低置信升级 → 校准）
python 01-core-spec/pef_cl_e2e.py
```

---

## 四、理论同步映射（GitHub ↔ 飞书知识库）

| GitHub 文档 | 飞书知识库对应页 |
|---|---|
| 根目录 5 摘要（primitives/pi-anchor/mod3/topology/axioms） | 02-理论与设计 |
| 01-core-spec（7.6 Pro 规范） | 02-理论与设计 · 公理A1-A8 |
| 01-core-spec（三级闭环引擎） | 灰烬token级深挖定案 |
| 02-applications（CIC/PIMEM） | 02-理论与设计 · 06-PEF记忆体 |
| 03-operator-library（800算子） | 01-算子定义与规范 · 800算子库4层级 |
| 04-engineering-cases（CLE探针） | 03-测试与验证 · 08-902批次 |
| 05-references（三剑客/幻觉报告） | 05-知识卡片库 |

---

## 五、公开声明

本仓库内容为**公开理论**，采用 MIT 许可。欢迎评审、挑战、复现。
- 仓库：https://github.com/banbanry/pef-architecture
- 代码参考实现：[pef-core-reference](https://github.com/banbanry/pef-core-reference)
- 作者：banbanry (沈鹭)
- 核心主张：**唯锚才有势差产生**（Anchored Determinism Meta-Architecture）

*PEF Architecture © 2026 banbanry. Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
