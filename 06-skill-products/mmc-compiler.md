# mmc-compiler — 多模型方言编译

> **功能一句话**：把不同大模型厂商（千问/GLM/DeepSeek/豆包/月之暗面…）的输出方言统一编译到 PEF 标准方言，验证"同一输入在不同模型间主体不丢失、变量组合一致、结果收敛"。

© 2026 沈鹭 (banbanry) · 厦门恒元架构科技有限公司 · MIT License
来源：https://github.com/banbanry/mmc-compiler

## 功能（对应 SKILL.md）

- **方言注册表**：openai / deepseek / claude / doubao / glm / gemini 六种响应路径识别
- **术语归一**：异名同义概念映射（跨模型术语对齐）
- **三元组编译**：P（主体）/ E（变量 name-kind-value）/ F（结果）强制结构化提取
- **推理模型回退**：`reasoning_content` 空 content 回退（Qwen3.5-27B / GLM-4.7 / DS-R1 实测）
- **JSON 结构化变量提取**：GLM/DeepSeek `{variables:[...]}` 结构优先、正则回退

## 理论依据（PEF 布局映射）

| PEF 组件 | 落地 |
|---|---|
| P/E/F 三元原语 | 编译目标强制三元组 JSON（subject/variables/results） |
| A3 变量分流 | 变量标注 E_in（可控输入）/ E_out（不可控输出） |
| 跨模型对齐 | 多模型编译 = 多模型偏差的"方言归一"（CIC 跨模型治理的应用） |
| π 锚坐标 | 每个编译产物分配 π 锚 seq（单调递增，可追溯） |

## 代码与 demo

- **代码仓库**：https://github.com/banbanry/mmc-compiler （SKILL.md + scripts/mmc_cli.py + benchmarks/）
- **demo**：`python mmc_cli.py compile --input response.json --dialect <厂商>`

## 验证证据（真实运行）

**2026-09 真实 API 测试：5 模型 × 4 厂商**（输入：BF1 稀疏注意力论文 arXiv:2608.20427）：

| 模型 | 通道 | 编译 | 方言归一 | 主体保留 | 结论覆盖 |
|---|---|---|---|---|---|
| Qwen3.5-27B | 硅基流动 | ✅ | openai | ✅ | 8/8 |
| GLM-4.7-Flash | 智谱 | ✅ | openai | ✅ | 8/8 |
| GLM-4.5-Flash | 智谱 | ✅ | openai | ✅ | 4/8* |
| DeepSeek-V3 | DeepSeek | ✅ | openai | ✅ | 8/8 |
| DeepSeek-R1 | DeepSeek | ✅ | openai | ✅ | 7/8 |

*\*GLM-4.5-Flash 输出精炼未罗列具体长度——模型行为差异，非编译丢失。*

详细报告：`examples/mmc-compiler/EVALUATION-live-models.md`

**测试中修复的 2 个真实方言盲区**：① 推理模型 `reasoning_content` 回退；② `_extract_vars()` JSON 结构化变量提取（修复后 GLM 变量 0→6 个）。

---
