> **Source**: https://github.com/banbanry/pef-architecture/04-engineering-cases
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生

# 04 — 工程应用案例

本层展示 PEF 架构在**实际工程项目**中的部署和应用。这些案例证明 PEF 架构不是纸上理论，而是可以落地的工程实践。

## 案例列表

### CLE V3.8.2 — 确定性代码探针系统

CLE（Code Logic Extractor）是一个基于 PEF 架构的确定性代码探针系统，用于代码逻辑提取、审计和验证。

| 文档 | 内容 | 规模 |
|------|------|------|
| [cle-probe/cle-l1-l3-technical.md](cle-probe/cle-l1-l3-technical.md) | **L1-L3 三层完整技术文档** — 五阶段全量整合 + PEF算子库扩展 + 双层交叉审计 + 拜占庭注入验收 | ~25K 字符 |
| [cle-probe/cle-systematic-integration.md](cle-probe/cle-systematic-integration.md) | **系统性整合文档** — 五阶段完整工作流设计 + 公底层定义 + 部署连接指南 | ~23K 字符 |
| [cle-probe/cle-five-stage-workflow.md](cle-probe/cle-five-stage-workflow.md) | **五阶段完整合并文档** — 五阶段工作流的完整合并版本 | ~41K 字符 |

## CLE 系统架构

CLE 系统采用三层架构：

- **L1 — 探针层**：代码探针植入，提取代码逻辑和状态
- **L2 — 审计层**：PEF 算子库扩展，双层交叉审计，π锚定追踪
- **L3 — 裁决层**：拜占庭注入验收，PASS/FAIL 裁决，熔断机制

五阶段工作流：探针植入 → 逻辑提取 → 状态追踪 → 交叉审计 → 裁决验收

## PEF 架构在 CLE 中的应用

| PEF 概念 | CLE 中的实现 |
|----------|--------------|
| P（主体） | 代码探针实例，显式声明探针身份和边界 |
| E（变量） | 代码状态变量，E_in（可控输入）/ E_out（环境观测）分流 |
| F（结果） | 逻辑提取结果，可追溯至 (P, E, t)，π锚定审计 |
| π 锚定 | 每次探针操作绑定 π 坐标，不可伪造 |
| MOD3 | 三态审问强度，驱动审计严格度 |
| 熔断 | 拜占庭注入检测到异常时立即熔断 |

## 阅读顺序

1. 先读 `cle-systematic-integration.md` 理解整体工作流
2. 再读 `cle-l1-l3-technical.md` 深入三层技术细节
3. `cle-five-stage-workflow.md` 作为完整合并参考

## 其他工程案例

- **弘信物流进出口单表单处理器**（810项目）— PEF 架构的生产部署，见根目录 README 的 Real-World Deployment 章节
- **pef-core-reference** — 代码参考实现，见 https://github.com/banbanry/pef-core-reference

---
*PEF Architecture © 2026 banbanry. Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
