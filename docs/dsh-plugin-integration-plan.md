# PEF 五件套 × DeepSeek Harness — 插件化设计（可行性评估 + 落地路径）

> **版本**：V1.0 · 2026-09-05
> **背景**：DeepSeek Harness（DSH）「万物皆插件」生态上线（v0.1 MIT 开源，Cordis 插件系统；官方 MCP 桥 + 企查查团队发起 dsh-mcp-connector 连接器市场，2026-08-25 已收录 82 张服务卡片覆盖 9 大类）。评估把 PEF 四 Skill（cle-code-probe / pimem-memory / pef-longtext / mmc-compiler）插件化接入 DSH 的可行性。

---

## 一、结论

**可行，4/4 通过，且形态选择有讲究：**

| Skill | 适配形态 | 可行性 | 理由 |
|---|---|---|---|
| cle-code-probe | **Tool 插件** | ✅ 高 | 本地确定性审计能力，天然契合 DSH "内置工具与 MCP 插件同一审批+沙箱" 模型 |
| pimem-memory | **Tool 插件** | ✅ 高 | 本地记忆仓库；差异化卖点：π 锚防漂移可验真记忆（DSH 通用记忆无验真） |
| pef-longtext | **Tool 插件** | ✅ 高 | 本地长文本审计；补充 DSH 大上下文场景的"内容质检"能力 |
| mmc-compiler | **Tool 插件 + 可配置 Provider** | ✅ 中高 | 编译引擎本地；多模型通道走可配置 API（需用户 key） |

**关键判断依据**（DSH 官方 extension-cookbook 决策准则）：
> 插件自己持有的本地能力 → 定义并注册 **Tool**；外部 Server 暴露的远程能力 → 挂载 **MCP Client Plugin**；新模型线协议 → 实现 **LLM Adapter**。*"不要为了看起来可移植就给本地函数套上 MCP。"*

四个 skill 全部是**本地 Python 能力**（零/少依赖）→ 正确形态是 **Tool 插件**（`dsh-tool-*`），不是硬套 MCP。只有 mmc-compiler 的多模型通道属于外部 API，按"可配置 Provider"处理。

---

## 二、DSH 生态现状（2026-09 核验）

| 项 | 现状 |
|---|---|
| DeepSeek Harness | 官方开源 `github.com/deepseek-ai/deepseek-harness`，v0.1，MIT，Cordis 插件系统 |
| 插件化范围 | 模型 / 工具 / 技能 / 会话 / 沙箱 / 存储 / Agent Loop / 调度 / UI 全部可替换 |
| MCP 接入 | 官方插件 `@deepseek-ai/dsh-mcp-client`（一 server 一插件：discover tools → ctx.tools.register()）；`dsh-plugin-mcp` 官方标准桥（Claude Code 级特性） |
| 安全模型 | **内置工具和 MCP 插件走同一套审批 + 沙箱**；连接器负责发现/授权/验证/配置/生命周期，DSH 宿主 MCP Client 负责执行 |
| 插件市场 | `dsh-mcp-connector`（企查查发起，开源）：82 卡片 / 9 大类；社区市场 dsh-plugin（400+）、DSH Plugin Hub 等 |
| Skills 机制 | 支持 Skills：section + tool registration + inject() 技能内容——**与现有 SKILL.md 结构兼容** |

---

## 三、插件化架构设计

### 3.1 总体结构（遵循 PEF 五层布局）

```
DeepSeek Harness（宿主）
  ├── PEF 插件族（dsh-tool-*，Cordis 插件）
  │     ├── dsh-tool-cle-probe      → audit / byzantine / inject / verify
  │     ├── dsh-tool-pimem-memory   → init / remember / query / diff / verify
  │     ├── dsh-tool-pef-longtext   → scan / report
  │     └── dsh-tool-mmc-compiler   → compile（多模型 Provider 可配置）
  ├── 统一审批 + 沙箱（DSH 内置）
  └── SKILL.md → 插件描述（description + inject 内容，兼容 DSH Skills 机制）
```

### 3.2 插件实现骨架（以 cle-code-probe 为例）

```typescript
// dsh-tool-cle-probe 插件（Cordis 格式）
export default definePlugin(() => {
  const audit = async (args: { path: string }) => {
    // 调 resources/cle_deploy.py audit，走 DSH 沙箱执行
    return deterministic_result;   // FAIL / PASS / GAMMA + findings + 哈希链
  };
  return {
    name: 'dsh-tool-cle-probe',
    tools: [
      { name: 'cle_audit',      description: '确定性代码审计（物理不变量算子）', inputSchema: {...}, invoke: audit },
      { name: 'cle_byzantine',  description: '拜占庭对抗测试（11 场景）',        inputSchema: {...}, invoke: byzantine },
      { name: 'cle_inject',     description: '脏数据注入验收（L3 金丝雀）',      inputSchema: {...}, invoke: inject },
      { name: 'cle_verify',     description: '模块完整性验证',                   inputSchema: {...}, invoke: verify },
    ],
  };
});
```

### 3.3 Tool 注册清单（4 Skill → 13 个 tool）

| 插件 | Tools | 输入 | 输出 |
|---|---|---|---|
| cle-code-probe | `cle_audit` `cle_byzantine` `cle_inject` `cle_verify` | 文件路径 / 代码 | FAIL/PASS/GAMMA + findings + SHA-256 印章 |
| pimem-memory | `mem_init` `mem_remember` `mem_query` `mem_diff` `mem_verify` | 主体声明 / 演化记录 | 漂移告警 / 哈希链验真结果 |
| pef-longtext | `lt_scan` `lt_report` | 文本路径 / chunk 大小 | 12 类拜占庭污点报告 + C 层 10 项校验 |
| mmc-compiler | `mmc_compile` | 响应 JSON / 方言 | openai 方言归一 + P/E/F 三元组 + π 锚 seq |

### 3.4 审批与沙箱（安全设计）

- 全部 tool 走 DSH 统一审批流（首次调用需用户批准）
- 代码审计/文本扫描在沙箱内执行（DSH 沙箱机制），禁止宿主文件系统写权限
- mmc-compiler 的 API key 走 DSH 凭证管理（`DSH_` 前缀隔离，只放行显式配置的 env）

---

## 四、差异化定位（为什么值得上）

| 对比维度 | DSH 市场现有卡片（82 张） | PEF 五件套 |
|---|---|---|
| 类型 | 远程数据查询连接器（企查查/法律/办公/数据） | **本地确定性工具链**（审计/记忆/质检/编译） |
| 哲学 | 连接外部数据源 | **不信任输出，验证输出**——把"AI 说自己对"变成"能证明自己对" |
| 记忆 | 通用记忆（无验真） | PIMEM π 锚防漂移可验真记忆 |
| 长文本 | 大上下文（读得进） | 长文本质检（读得进还审得出污染） |
| 多模型 | 单模型路由 | MMC 多模型方言归一 + 一致性验证 |

**市场空白**：82 张卡片都是"获取信息"，PEF 五件套是"验证信息"——同一生态里没有直接竞品。

---

## 五、落地路径（4 阶段）

| 阶段 | 内容 | 工作量 | 产出 |
|---|---|---|---|
| **P0 适配** | 4 个 skill 各写 Cordis 插件骨架 + tool 注册 + SKILL.md 描述映射 | 2-3 天 | `dsh-tool-*` 4 个插件 |
| **P1 沙箱与审批** | 接 DSH 沙箱执行、审批流、凭证隔离 | 2 天 | 安全通过 |
| **P2 上架** | 注册到 dsh-mcp-connector Connector Registry（Descriptor：command/args/env/cwd）+ dsh-plugin 社区市场 | 1 天 | 市场卡片 |
| **P3 推广** | README 中英双语 + demo 录屏 + A/B 验证展示 | 2 天 | 转化物料 |

---

## 六、风险与诚实边界

| 风险 | 级别 | 说明 |
|---|---|---|
| DSH v0.1 生态未稳 | ⚠️ 中 | 插件 API 快速变动，P0 阶段需锁定当前版本；升级需回归 |
| 探针/长文本本地执行 | ⚠️ 中 | 必须走沙箱，沙箱能力受限时审计大文件需分片（pef77 已有重型模式） |
| mmc 多模型通道 | ⚠️ 低 | 需用户配各厂商 key；免费额度耗尽即 402（实测），文档需写明 |
| 工具调用超时 | ⚠️ 低 | 长文本 scan 大文件可能超 DSH 默认 60s，需按 tool 配置 call_timeout |
| 与官方 MCP 桥的取舍 | ℹ️ 决策 | 官方准则明确"本地能力→Tool"，不套 MCP；若未来要暴露为远程服务再迁 MCP |

---

## 七、结论一句话

**可行且值得做**：四 skill 是 DSH 生态中稀缺的"本地确定性工具链"，形态选 Tool 插件（非硬套 MCP）符合官方准则；差异化定位"不信任输出，验证输出"填补市场空白；落地成本约 1 周（P0-P3）。

---

*PEF × DSH · 不信任输出，验证输出。© 2026 沈鹭 (banbanry) · 厦门恒元架构科技有限公司 · MIT License*
