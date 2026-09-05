# pimem-memory — π-基因链记忆仓库

> **功能一句话**：用 π 锚为"主体"分配永久身份基因（Π_anchor），存储只读基线（P_base）与演化谱系（Chain），支持记忆查询、漂移比对、哈希链验真——**AI 跨会话"忘了约定/参数被静默改掉"时秒级发现主体漂移**。

© 2026 沈鹭 (banbanry) · 厦门恒元架构科技有限公司 · MIT License
来源：https://github.com/banbanry/pimem-memory

## 功能（对应 SKILL.md）

| 命令 | 用途 |
|---|---|
| `init` | 基因初始化：分配 Π_anchor + 写 P_base + 创世上链（每主体一次） |
| `remember` | 追加演化记录（ΔV_i → J_i，哈希链锁定） |
| `query` / `tree` | 演化谱系回溯 |
| `diff` | **漂移比对**：当前状态 vs 基线定义类字段（核心） |
| `verify` | 哈希链 + 注册表验真（篡改时退出码=1） |

## 理论依据（PEF 布局映射）

- 设计依据：PEF-EXT-MEM-004 PIMEM 设计理论 V1.0（**PEF-π 第四项运用**）
- 核心三元组 `(Π_anchor, P_base, Chain)`：π 锚一次性分配身份基因（A5/A6）→ 只读基线快照（DEF 字段参与漂移比对 / STATE 字段允许演化）→ 哈希链锁定演化谱系（A7）
- 漂移即 A3 变量分流的记忆版：定义类字段是"不可变承诺"（类似 E_in 约束），运行时状态允许演化（类似 E_out 观测）

## 代码与 demo

- **代码仓库**：https://github.com/banbanry/pimem-memory （SKILL.md + scripts/pimem_cli.py）
- **demo**：`python pimem_cli.py --root . init --name RateLimiter ...` → `remember` → `diff --current-file current_state.json` → `verify`

## 验证证据（真实运行）

| 测试 | 结果 | 证据文件 |
|---|---|---|
| 主体初始化 | GENESIS 上链 ✅ | `examples/pimem-memory/pimem_memory/registry.json` |
| 演化追加 | seq=1 FAIL ρ=0.7 MOD3=2 ✅ | `examples/pimem-memory/pimem_memory/chain_π-0-3.json` |
| **漂移比对** | **检出 limit: '100' → '999'**（定义类字段偏移告警）✅ | `examples/pimem-memory/current_state.json` |
| 哈希链验真 | 2 条记录完整，注册表摘要一致 ✅ | `verify` 输出 |

---
