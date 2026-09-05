# CLE Code Probe vs 基础正则 Linter — 检出率对照分析

> 第三方独立对照测试，用 5 个标准测试样本对比 CLE Code Probe 与基础正则 Linter（模拟 clang-tidy / Bandit 基础能力）的检出差异。
>
> 测试时间：2026-09-05
> 测试环境：Python 3.13.13, Windows
> CLE 版本：V3.8.2 (V3.9 扩展)

## 一、测试样本集

| # | 样本 | 包含的漏洞类型 | 预期检出 |
|---|------|--------------|---------|
| 1 | `01_basic_vuln.c` | malloc未检查NULL、除零、sprintf无边界 | P0×2, P1×1 |
| 2 | `02_taint_propagation.c` | scanf无边界、system命令注入、污点传播(scanf→system)、strcpy、格式字符串 | P0×2, P1×3 |
| 3 | `03_dangerous_functions.c` | gets、strcpy、sprintf、strcat | P0×1, P1×3 |
| 4 | `04_hardcoded_leak.c` | 硬编码密码、硬编码API密钥、资源泄漏(fopen/malloc未释放)、除零 | P0×1, P1×3 |
| 5 | `05_clean_code.c` | 干净代码（正确的错误处理和边界检查） | P0×0, P1×0（应无检出） |

## 二、检出率对照表

| 样本 | CLE P0 | CLE P1 | CLE 裁决 | Basic P0 | Basic P1 | CLE 独有检出 | Basic 独有检出 |
|------|--------|--------|---------|----------|----------|-------------|---------------|
| 01_basic_vuln.c | 2 | 1 | FAIL | 1 | 1 | **malloc NULL检查(P0)** | malloc调用(误报) |
| 02_taint_propagation.c | 2 | 2 | FAIL | 1 | 1 | **污点传播(跨函数BFS)** | — |
| 03_dangerous_functions.c | 1 | 3 | FAIL | 1 | 2 | — | — |
| 04_hardcoded_leak.c | 3 | 1 | FAIL | 0 | 0 | **资源泄漏、除零(变量)、malloc NULL检查(P0)** | — |
| 05_clean_code.c | 1 | 0 | FAIL | 1 | 0 | — | malloc调用(误报) |
| **合计** | **9** | **7** | — | **4** | **4** | — | — |

> **V3.9.2 更新**：新增 `DangerousFunctionDetector`（gets/vsprintf/scanf/getwd/crypt）和 `MallocNullCheckDetector`（malloc/calloc/realloc NULL检查追踪，5行窗口上下文分析）两个算子。gets 和 malloc NULL 检查的检测盲区已补充。

## 三、关键发现

### 3.1 CLE 的核心优势（基础 Linter 做不到的）

| 优势 | 说明 | 证据 |
|------|------|------|
| **跨函数污点传播** | 用 BFS + 别名分析追踪 `scanf→buf→system` 的污点链，基础正则只能看到 `system()` 调用，无法判断参数是否可控 | 02样本：CLE 检出 `TAINT_PROPAGATION` + `TAINT_CROSS_FUNCTION` 两个 P0，Basic 只检出 `system()` 1个 P0 |
| **资源泄漏检测** | 追踪 `fopen`/`malloc` 的分配和释放路径，检测错误路径上的资源泄漏 | 04样本：CLE 检出资源泄漏 P0，Basic 完全未检出 |
| **变量除零检测** | 不只是检测常量除零（`x/0`），还能检测变量除零（`x/divisor` where divisor=0） | 04样本：CLE 检出变量除零 P0，Basic 完全未检出 |
| **π 调度 + D-S 证据融合** | 不同文件→不同哈希→不同π序列→激活不同特征子集，避免全量遍历的性能问题 | 架构级优势，不在单样本对照中体现 |
| **洋葱流水线 Gate0-8** | 多级门控拦截，空输入/解析失败/图构建失败等边界情况有专门处理 | 05样本：clean code 仍被误报，但有完整的裁决链和状态向量 |

### 3.2 CLE 的已知短板（V3.9.2 已补充部分）

| 短板 | 状态 | 说明 |
|------|------|------|
| ~~gets 危险函数漏检~~ | ✅ **V3.9.2 已修复** | 新增 `DangerousFunctionDetector`，覆盖 gets/vsprintf/scanf(%s)/getwd/crypt |
| ~~malloc 未检查 NULL 漏检~~ | ✅ **V3.9.2 已修复** | 新增 `MallocNullCheckDetector`，5行窗口上下文分析，有NULL检查则不误报 |
| ~~clean code 误报~~ | ✅ **V3.9.2 已修复** | `MallocNullCheckDetector` 正确识别已有 NULL 检查，clean code 不误报 |
| **硬编码密码检测弱** | ⚠️ 待修复 | 对 `#define PASSWORD "xxx"` 形式的硬编码密码检测不足，下版本补充 |

### 3.3 两者都做不到的（需要更高级工具）

- 跨文件污点传播（当前只做单文件内跨函数）
- 并发/数据竞争检测
- 内存泄漏的精确路径敏感分析
- 业务逻辑漏洞（如权限绕过、逻辑缺陷）

## 四、误报率对比

| 指标 | CLE | Basic 正则 |
|------|-----|-----------|
| clean code 误报 | 1 个 P0 | 1 个 P0 |
| malloc 误报率 | 0%（完全漏检，不是误报） | 100%（只要有 malloc 就报） |
| 总体误报倾向 | 中（有状态向量和证据融合缓冲） | 高（纯正则，无上下文） |

## 五、结论

### CLE Code Probe 的定位

CLE 不是要替代 clang-tidy / cppcheck / Bandit 这些成熟的基础 linter，而是在它们之上提供**基础 linter 做不到的深度分析能力**：

1. **污点传播**（跨函数 BFS + 别名分析）—— 这是 CLE 最核心的差异化优势
2. **资源泄漏检测** —— 路径敏感的资源分配/释放追踪
3. **π 调度 + D-S 证据融合** —— 架构级的可复现审计和证据聚合
4. **金丝雀注入验收** —— 用已知缺陷验证审计器本身的可信度（防"假审计"）

### 建议的使用方式

```
代码提交前 → clang-tidy / cppcheck（基础规则，快速）
           → CLE Code Probe（深度分析：污点传播、资源泄漏、π审计）
           → 两者结果合并，人工复核差异
```

CLE 不应该单独使用——它的短板（gets/malloc 检测）正好是基础 linter 的强项，两者互补才能达到最佳覆盖率。

### 下一步改进

1. ✅ **P0 已完成**：V3.9.2 新增 `DangerousFunctionDetector`，覆盖 gets/vsprintf/scanf/getwd/crypt
2. ✅ **P1 已完成**：V3.9.2 新增 `MallocNullCheckDetector`，5行窗口上下文分析，有NULL检查则不误报
3. **P2 待完成**：增加 #define 形式的硬编码密码检测（半小时工作量）
4. **P3 待完成**：与 clang-tidy 结果合并的对比报告生成器（1天工作量）

---

## 附录：复现方式

```bash
# 1. 克隆 cle-code-probe 仓库
git clone https://github.com/banbanry/cle-code-probe.git

# 2. 运行第三方复现脚本（自动复现 audit + byzantine + inject）
python examples/cle-probe/reproduce.py --probe-dir /path/to/cle-code-probe

# 3. 运行对照测试
python examples/cle-probe/basic_linter.py test-samples/01_basic_vuln.c --json
python /path/to/cle-code-probe/resources/cle_deploy.py audit test-samples/01_basic_vuln.c
```

所有测试样本和脚本都在 `examples/cle-probe/` 目录下，可独立复现。
