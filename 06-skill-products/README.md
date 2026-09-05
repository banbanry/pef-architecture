# Skill Products — PEF 工程化落地五件套

> **这是 PEF 架构从"理论"到"可用产品"的完整链路**。每个 Skill = 功能定义（SKILL.md）+ 可运行代码（独立 GitHub 仓库）+ 理论依据（PEF 公理/原语映射）+ demo/测试 + 真实验证证据（`../examples/`）。

**链路结构**（遵循 PEF 五层布局）：

```
理论层（根目录 5 文档：axioms / primitives / pi-anchor / mod3 / topology）
   ↓ 实例化
规范层（01-core-spec：pef-7.6-pro-design-spec）
   ↓ 工程化
产品层（本目录：4 个 Skill，代码在独立 GitHub 仓库）
   ↓ 验证
证据层（examples/：4 组真实运行测试）
   ↓ 联动
应用层（02-applications：CIC / PIMEM 设计理论）+ 飞书知识库
```

---

## 产品矩阵

| Skill | 一句话 | 理论映射 | 代码仓库 | 验证证据 |
|---|---|---|---|---|
| [**cle-code-probe**](cle-code-probe.md) | 确定性代码探针：AI 自审不可信时的物理不变量审计 | A1/A3/A4/A7 + MOD3 + 洋葱流水线 | [github.com/banbanry/cle-code-probe](https://github.com/banbanry/cle-code-probe) | [examples/cle-probe](../examples/cle-probe/)：49/49 回归、11/11 拜占庭、FAIL 裁决 |
| [**pimem-memory**](pimem-memory.md) | π-基因链记忆仓库：跨会话主体漂移检测 + 哈希链验真 | A5/A6/A7 + PEF-π 第四项运用 | [github.com/banbanry/pimem-memory](https://github.com/banbanry/pimem-memory) | [examples/pimem-memory](../examples/pimem-memory/)：漂移检出 limit 100→999 |
| [**pef-longtext**](pef-longtext.md) | 长文本拜占庭污点审计：百万字遍历 + 12 类污点确定性检出 | A2/A4 + 洋葱 L1-L4 + C 层 10 项校验 | [github.com/banbanry/pef-longtext](https://github.com/banbanry/pef-longtext) | [examples/pef-longtext](../examples/pef-longtext/)：6/6 污点命中 |
| [**mmc-compiler**](mmc-compiler.md) | 多模型方言编译：把各厂商模型输出归一为统一方言 | P/E/F 三元原语 + 跨模型对齐 | [github.com/banbanry/mmc-compiler](https://github.com/banbanry/mmc-compiler) | [examples/mmc-compiler](../examples/mmc-compiler/)：5 模型真实 API 测试 |

---

## 完整链路示例（cle-code-probe）

```
axioms.md A1（π-切片形态约束）          ← 理论
   ↓
01-core-spec 洋葱流水线三级阻断设计      ← 规范
   ↓
SKILL.md + resources/ 16 模块（代码）   ← 产品（GitHub 仓库）
   ↓
examples/cle-probe/audit-result.txt    ← 验证（真实运行输出）
   ↓
README.md 阅读路径                     ← 导航
```

---

*Skill Products · 理论 → 规范 → 代码 → 验证，全链路可追溯。© 2026 沈鹭 (banbanry) · MIT License*
