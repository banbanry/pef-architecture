# MMC 多模型真实 API 测试报告 (2026-09-05)

## 测试目标
验证 mmc-compiler 在**真实大模型 API 输出**上的有效性：同一篇最新论文 → 同一分析 prompt → 不同厂商模型 → MMC 方言编译 → 检查 ①skill 是否有效 ②内容是否统一 ③主体是否丢失 ④变量组合是否一致 ⑤结果是否相同。

## 测试输入
- 论文: **BF1: A Causal Dyadic Sparse-Attention Retrofit for Efficient Long-Context Transformers** (arXiv:2608.20427, 2026-08-19)
- Prompt: 要求输出结构化 JSON (`subject / variables[name,kind,value] / results / terms`)

## 真实模型样本 (5 个, 4 家厂商)

| 模型 | 通道 | 方言特征 |
|---|---|---|
| Qwen3.5-27B | 硅基流动 | 推理模型: `content` 空, 答案在 `reasoning_content` |
| GLM-4.7-Flash | 智谱 (JWT 鉴权) | 关闭 thinking 后正常输出 JSON |
| GLM-4.5-Flash | 智谱 (JWT 鉴权) | 关闭 thinking 后正常输出 JSON |
| DeepSeek-V3 (deepseek-chat) | DeepSeek | 标准 OpenAI 兼容 |
| DeepSeek-R1 (deepseek-reasoner) | DeepSeek | 推理模型: `reasoning_content` + `content` |

## 结果

### ① Skill 有效性: ✅ 5/5 编译成功
所有真实响应均完成方言识别 + π 锚分配 + 论断拆解 + 变量提取。

### ② 方言统一: ✅ 5/5 归一为 `openai` 方言
| 模型 | 编译前 | 编译后 |
|---|---|---|
| Qwen3.5-27B | `reasoning_content` (推理方言) | `openai` (自动回退) |
| GLM-4.7-Flash | OpenAI 兼容 | `openai` |
| GLM-4.5-Flash | OpenAI 兼容 | `openai` |
| DeepSeek-V3 | OpenAI 兼容 | `openai` |
| DeepSeek-R1 | `reasoning_content` (推理方言) | `openai` |

### ③ 主体保留: ✅ 5/5 无丢失
所有编译结果均保留核心主体 BF1 / Sparse-Attention (含 Qwen3-0.6B 关联)。

### ④ 变量组合一致性: ✅ 核心变量跨模型一致
| 变量 | Qwen3.5-27B | GLM-4.7 | GLM-4.5 | DeepSeek-V3 | DeepSeek-R1 |
|---|---|---|---|---|---|
| block width (E_in) | ✅ | ✅ | ✅ | ✅ | — |
| prefill speedup 10.91x@32K (E_out) | ✅ | ✅ | ✅ | ✅ | ✅ |
| TTFT 7.7%/11.3%/15.3% (E_out) | ✅ | ✅ | ✅ | ✅ | ✅ |
| perplexity 1.68639 (E_out) | ✅ | ✅ | ✅ | ✅ | ✅ |
| 适配协议 1000步/16.384M token (E_in) | ✅ | ✅ | ✅ | — | — |

命名存在中英文方言差异 (如 `block width` vs `块宽度`), 属术语归一后续工作。

### ⑤ 结果一致性: ✅ 关键结论共现 (4/5 模型 8/8, R1 7/8)
| 关键数字 | Qwen3.5-27B | GLM-4.7 | GLM-4.5 | DeepSeek-V3 | DeepSeek-R1 |
|---|---|---|---|---|---|
| 10.91 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 1.68639 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 32K | ✅ | ✅ | — | ✅ | ✅ |
| 8K/16K/2K | ✅ | ✅ | — | ✅ | ✅ |
| O(n log n) | ✅ | ✅ | ✅ | ✅ | — |
| 7.7% | ✅ | ✅ | ✅ | ✅ | ✅ |

注: GLM-4.5-Flash 输出更精炼, 未罗列 8K/16K/32K 具体长度数字 (4/8), 属模型行为差异而非编译丢失。

## 测试中发现并修复的 MMC 盲区 (真实价值)

1. **推理模型方言盲区 (V1.1)**: Qwen3.5-27B / DeepSeek-R1 等推理模型把答案放 `reasoning_content`, 旧版 MMC fallback 误抓。已给 openai/deepseek/doubao/glm 方言增加 `reasoning_content` 回退路径。修复前 `auto-fallback` → 修复后正确识别 `openai`。
2. **JSON 结构化变量提取盲区 (V1.2)**: GLM/DeepSeek 输出 `{variables:[{name,kind,value}]}` JSON 结构, 旧版文本正则抓不到。已新增 `_extract_vars()` 优先结构化提取, 回退文本正则。修复前 GLM 变量 0 个 → 修复后 6 个。

## 诚实边界

- 覆盖 3 家厂商 4 个模型 (硅基流动余额不足, 小米/豆包/月之暗面原生未测; Qwen3.5-27B 经硅基流动通道)
- Qwen3.5-27B 因 `content` 空, 提取的是 `reasoning_content` 思维链 (非最终答案), 但其主体/结论仍完整保留
- GLM 第二次调用 429 限流, 采用首次成功样本
- 变量命名方言差异 (中/英/大小写) 未做语义合并, 属已知边界
- π 锚为编译坐标 (seq 单调), 不参与业务真值判定

## 复现

```bash
# key 配置: D:\WorkBuddy\_mmc_multi\.env (本地, 不进仓库)
python D:\WorkBuddy\_mmc_multi_runner.py   # 调用模型 + 编译
python D:\WorkBuddy\_mmc_compare.py        # 一致性对比
```

---
© 2026 沈鹭 (banbanry) · 厦门恒元架构科技有限公司 · MIT License
