# cle-code-probe — 确定性代码探针

> **功能一句话**：当 AI 自审不可信时，用确定性物理不变量算子 + 1000 条故障库做代码审计，输出 PASS/FAIL/GAMMA 裁决，全流程哈希链留痕。

© 2026 沈鹭 (banbanry) · 厦门恒元架构科技有限公司 · MIT License
来源：https://github.com/banbanry/cle-code-probe

## 功能（对应 SKILL.md）

- 确定性审计：4 大物理不变量算子 + 11 个 PEF 扩展算子 + Python 14 算子
- 跨函数污点传播（ProgramGraph + BFS + 别名分析 + 三级 SANITIZER）
- 拜占庭对抗 11 场景真实执行、注入验收（L3 金丝雀防假测试）
- π-锚调度（SecurePiDigitProvider）、D-S 证据融合、状态向量 S1-S7、SHA-256 裁决印章

## 理论依据（PEF 布局映射）

| PEF 组件 | 落地 |
|---|---|
| A1 π-切片形态约束 | SecurePiDigitProvider 锚位派生 |
| A3 变量分流 / A4 时序因果 | E_in/E_out 分流声明 + 哈希链时序锁 |
| A5/A6 锚位绑定与单调 | 720 条特征库按 π 分片注册 |
| A7 审计可追溯 | AuditLogChain 哈希链 |
| MOD3 三态审问 | 洋葱流水线 Gate0-10 三级阻断 |

## 代码与 demo

- **代码仓库**：https://github.com/banbanry/cle-code-probe （SKILL.md + scripts/ 16 模块）
- **本地 Skill 路径**：`~/.doubao/agent_mode/workspace/.user_skills/cle-code-probe/`
- **demo**：`python cle_deploy.py audit source.c` / `byzantine` / `inject` / `verify`

## 验证证据（真实运行）

| 测试 | 结果 | 证据文件 |
|---|---|---|
| 全量回归 | 49/49 PASS | （Skill 内） |
| 拜占庭对抗 | 11/11 PASS | `examples/cle-probe/byzantine-result.txt` |
| 含漏洞 C 样本 | **FAIL**（P0=1 除零, P1=1 sprintf 无边界） | `examples/cle-probe/audit-result.txt` |

**诚实边界**：污点检测为行级引擎（跨函数参数传递漏检，需 L2 AI 审查补充）；S3/S5/S7 标记 `_pending`；720 条特征库为骨架待人工验证。

---
