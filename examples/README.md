# Examples — Skill 实测证据（可复现）

> **这一层是本仓库区别于"纯理论仓库"的关键**：以下 4 组实例全部来自**真实运行的 Skill**（本机 Python 3 直接执行），不是纸面描述。每个目录含输入、原始输出与结果说明，评审者可自行复现。

| 实例 | 验证内容 | 关键结果 | 复现命令 |
|---|---|---|---|
| [`cle-probe/`](cle-probe/) | 确定性代码探针（CLE V3.8.2） | 拜占庭 11/11 PASS；含漏洞样本 **FAIL（P0=1 除零, P1=1 无边界 sprintf）** | `python cle_deploy.py byzantine` / `python cle_deploy.py audit vuln_sample.c` |
| [`pimem-memory/`](pimem-memory/) | π-基因链记忆仓库（PIMEM） | **漂移检出**：定义类字段 limit 100→999 告警；哈希链 2 条完整；验真 PASS | `python pimem_cli.py --root . diff --anchor "π-0-3" --current-file current_state.json` |
| [`pef-longtext/`](pef-longtext/) | 长文本拜占庭污点审计（PEF-7.7） | **6 类污点全部检出**：时间逆序 / π伪造 / 灰色地带 / 无锚论断 / 重复内容 / 数值矛盾 | `python pef77_cli.py --out-dir . scan --input byzantine_sample.txt` |
| [`mmc-compiler/`](mmc-compiler/) | 多模型方言编译（MMC） | **5 模型 × 4 厂商真实 API**：编译 5/5、方言归一 5/5、主体保留 5/5 | 见 `EVALUATION-live-models.md` |

---

## 1. cle-probe — 确定性代码探针

**验证目标**：LLM 自审不可信时，用确定性物理不变量算子做代码审计。

- `byzantine-result.txt`：11 个拜占庭对抗场景**全部 PASS**（含 π 耗尽防护、MAX_LINE 安全降级）
- `vuln_sample.c` + `audit-result.txt`：含漏洞 C 样本（malloc 未检 NULL / 除零 / sprintf 无边界）→ 裁决 **FAIL**，`p0_count=1`（DIV_ZERO_10 除零）、`p1_count=1`（BUF_UNSAFE_11）

> **诚实边界**：当前引擎为行级污点追踪（SKILL.md 已声明）；malloc 未检查 NULL 属跨语句模式，PEF 算子覆盖与行级引擎的边界以 SKILL.md 为准。

## 2. pimem-memory — π-基因链记忆仓库

**验证目标**：跨会话记忆的主体漂移检测 + 哈希链验真。

1. `init` 创建主体 RateLimiter（def 字段 limit=100，state 字段 current=0），GENESIS 上链
2. `remember` 追加演化记录（rate=120 → FAIL, ρ=0.7, MOD3=2）
3. `diff` 对比当前状态文件：**检出漂移 `limit: '100' → '999'`**（定义类字段偏移告警）；状态类字段 current=55 属正常演化不告警
4. `verify`：注册表摘要一致 + 哈希链 2 条完整

> 意义：AI 跨会话"忘了当初约定/参数被静默改掉"→ 秒级发现主体漂移。

## 3. pef-longtext — 长文本拜占庭污点审计

**验证目标**：百万字级长文本遍历，确定性检出 12 类拜占庭污点（防 AI 幻觉 / 数据污染）。

`byzantine_sample.txt` 注入 6 类污点 → `report` 全部命中：

| 污点 | 检出 |
|---|---|
| BYZ_TIME_INVERSION（时间逆序，倒果为因） | ✅ |
| BYZ_PI_FORGE（自算/伪造 π 数位） | ✅ |
| BYZ_GREY_UNCERTAINTY（灰色地带未解决） | ✅ |
| BYZ_ANCHOR_MISS（论断无锚点） | ✅ |
| BYZ_DUPLICATE（重复内容指纹，防 AI 屎山） | ✅ |
| BYZ_CONTRADICTION（同一实体数值冲突） | ✅ |

> 历史记录：真实 110 万字语料遍历（220 分片剖面）、36/36 注入召回（V3.1 规则内 85% 召回率的盲区修复后）。

## 4. mmc-compiler — 多模型方言编译

**验证目标**：同一论文接入 5 家国产大模型，MMC 编译器把各模型输出方言归一为 openai 方言，验证内容统一偏移、主体不丢失、变量组合一致。

**2026-09 真实 API 测试（5 模型 × 4 厂商）**：

| 模型 | 通道 | 编译 | 方言 | 主体 | 结论覆盖 |
|---|---|---|---|---|---|
| Qwen3.5-27B | 硅基流动 | ✅ | openai | ✅ | 8/8 |
| GLM-4.7-Flash | 智谱 | ✅ | openai | ✅ | 8/8 |
| GLM-4.5-Flash | 智谱 | ✅ | openai | ✅ | 4/8* |
| DeepSeek-V3 | DeepSeek | ✅ | openai | ✅ | 8/8 |
| DeepSeek-R1 | DeepSeek | ✅ | openai | ✅ | 7/8 |

*\*GLM-4.5-Flash 输出精炼未罗列具体长度数字——模型行为差异，非编译丢失。*

**测试中发现并修复的 2 个真实方言盲区**：① 推理模型（Qwen3.5-27B / GLM-4.7 / DS-R1）答案在 `reasoning_content`、`content` 为空 → 增加回退路径；② GLM/DeepSeek 返回 `{variables:[{name,kind,value}]}` 结构化 JSON，旧文本正则抓不到 → 新增 `_extract_vars()` JSON 结构化提取（修复后 GLM 变量 6 个）。

详细报告见 [`EVALUATION-live-models.md`](mmc-compiler/EVALUATION-live-models.md)（含原始响应保留说明、编译产物路径、诚实边界）。

---

*Examples · 真实运行，可复现，诚实标注边界。*
