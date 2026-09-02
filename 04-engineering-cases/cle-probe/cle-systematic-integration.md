> **Source**: https://github.com/banbanry/pef-architecture/04-engineering-cases/cle-probe
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生


# CLE V3.8.2 — 系统性整合文档

CLE V3.8.2

确定性代码探针系统

系统性整合文档

五阶段完整工作流设计 + 公底层定义 + 部署连接指南

物理不变量守卫者 · 洋葱流水线 Gate 0-8

版本: V3.8.2

日期: 2026-09-02

## 第一章 系统总览与架构

### 1.1 设计理念

CLE V3.8.2 是一套确定性代码审计系统，核心理念是"不依赖AI主观判断"。通过物理不变量算子 + 1000条PEF/MOD故障库匹配 + 洋葱流水线Gate0-8，输出结构化的PASS/FAIL/GAMMA裁决。

系统经历了五个开发阶段，逐步从基础节点级检测演进到包含跨函数污点传播、D-S证据融合、SecurePi调度、状态向量S1-S7和裁决印章的完整审计框架。

### 1.2 五阶段开发历程

### 1.3 模块依赖关系

所有模块均依赖公底层(cle_base_layer.py)提供统一常量和类型定义。模块间通过明确的接口连接，禁止跨层直接调用。

cle_base_layer (公底层)

│

├── Phase 1: cle_probe_engine

│     └── 依赖: base_layer

├── Phase 2: ds_evidence_fusion

│     └── 依赖: base_layer

├── Phase 3: byzantine_tests

│     └── 依赖: base_layer

├── Phase 4: taint_propagation

│     └── 依赖: base_layer

├── Phase 4: integrated_pipeline

│     └── 依赖: base_layer + probe_engine + taint + ds

└── Phase 5: secure_pi_provider

└── 依赖: base_layer + integrated + probe + ds

### 1.4 洋葱流水线 Gate 0-8 总览

审计流程严格按照8个Gate顺序执行，每个Gate有独立的阻断/通过逻辑，形成洋葱式层层防御。

## 第二章 公底层定义 (防数据污染)

### 2.1 为什么需要公底层

在五阶段开发过程中，不同模块各自定义了常量(如DANGER_SINK=0x001)和数据类型(如CodeNode、AuditEvent)。如果不统一定义，AI在理解和使用这些概念时会产生混淆：

- Phase 1的cle_probe_engine用dict表示CodeNode，Phase 4的taint_propagation用dataclass
- DANGER_SINK在多个文件中重复定义，值可能不一致
- Severity和Verdict的字符串值在各模块中硬编码
- StateVector的健康阈值在Phase 2和Phase 5中定义不同
公底层(cle_base_layer.py)通过"单一事实来源"原则解决这些问题：所有常量、类型、阈值只在此模块定义一次，其他模块统一导入使用。

### 2.2 公底层定义的九大部分

#### 2.2.1 节点属性位掩码 (NodeAttr)

使用Python IntFlag枚举保证类型安全和位运算正确性。

#### 2.2.2 严重级别与裁决类型

Severity枚举定义四级严重度，Verdict枚举定义四种裁决结果。全系统统一使用这些枚举值，禁止字符串硬编码。

class Severity(Enum):

P0    = "P0"      # 致命: 确定性安全缺陷, 硬阻断

P1    = "P1"      # 严重: 需人工复核

GAMMA = "GAMMA"   # 降级: 探针无法确定

INFO  = "INFO"    # 信息: 不影响裁决

class Verdict(Enum):

FAIL   = "FAIL"    # 存在P0级安全缺陷

REVIEW = "REVIEW"  # 需人工复核

PASS   = "PASS"    # 未发现安全模式违规

GAMMA  = "GAMMA"   # 置信度不足/输入无效/π耗尽

#### 2.2.3 PEF三层映射

PEF = Process / Execute / Feedback，每层违规由对应算子检测。公底层统一定义PEFLayer和PEFCategory枚举。

#### 2.2.4 核心数据类型

CodeNode和AuditEvent是全系统统一的数据结构。公底层提供dataclass定义和dict转换方法，确保Phase 1(dict格式)和Phase 4(dataclass格式)之间的互操作。

#### 2.2.5 状态向量S1-S7

公底层统一定义StateVector的七个分量和健康阈值，防止Phase 2和Phase 5使用不同的阈值标准。

#### 2.2.6 系统配置参数

SystemConfig类集中管理所有物理极限参数，禁止在模块内部硬编码。

#### 2.2.7 模块注册表

ModuleRegistry记录所有模块的元信息(文件名、Phase、依赖链、导出接口)，防止AI混淆不同Phase的功能边界。

#### 2.2.8 公共工具函数

compute_sha256_prefix、strip_c_comments、strip_string_literals、has_null_check_in_context等公共函数统一定义在公底层，所有模块统一调用。

#### 2.2.9 公共API入口

get_version()和get_module_info()提供系统级元信息查询接口。

## 第三章 Phase 1 — 节点级算子与洋葱流水线

### 3.1 模块概述

cle_probe_engine.py 实现了CLE V3.8.2的洋葱流水线Gate 0-8基础架构，包含四大物理不变量算子中的三个：时间单调性、资源界限和状态有界性。

### 3.2 四大物理不变量算子

#### 3.2.1 OP_TimeMonotonicity (时间单调性)

检测时间戳溢出和时序缺陷。核心检测模式：Hal_GetTick()*N乘法溢出，其中N为字面量常数。

严重级别: P0 | PEF覆盖: E-TIMING, F-ERROR

#### 3.2.2 OP_ResourceBound (资源界限)

检测malloc/fopen/socket等资源分配函数的返回值是否被检查。V3.8.1增强：多行上下文窗口(±3行)查找NULL检查。

严重级别: P0 | PEF覆盖: E-RESOURCE, E-CONCURRENCY

#### 3.2.3 OP_StateBoundedness (状态有界性)

检测除法未检查除数为零、整数溢出截断、数组越界等状态边界违反。V3.8.1增强：字符串字面量剥离防止假阳性。

严重级别: P0/P1 | PEF覆盖: P-INIT, P-PARAM, E-ARITH

#### 3.2.4 OP_TaintPropagation (污点传播)

Phase 1版本为简单的单函数taint_table匹配，在Phase 4中被完整重写为跨函数图遍历。

### 3.3 Gate 0-8 执行流程

源码输入

│

▼ Gate 0: 空输入阻断 → GAMMA

│

▼ 注释剥离 (strip_comments)

│

▼ Gate 1: 解析CodeNode → 0节点则GAMMA

│

▼ Gate 2: 建图 → 图无效则GAMMA

│

▼ Gate 3-6: 节点级算子遍历

│   ├── OP_TimeMonotonicity → P0

│   ├── OP_ResourceBound → P0

│   └── OP_StateBoundedness → P0/P1

│

▼ Gate 7: 图级算子 (污点传播)

│

▼ Gate 8: 裁决与印章

│   ├── 统计P0/P1

│   ├── 计算状态向量S1-S7

│   └── 生成SHA-256哈希链

│

▼ 输出裁决JSON

### 3.4 关键接口

## 第四章 Phase 2 — D-S证据融合

### 4.1 理论框架

Dempster-Shafer证据理论替换简单加权平均，实现真正的多源证据融合。识别框架 Θ = {FAIL, PASS, UNCERTAIN}，幂集2^Θ含8个子集。

### 4.2 核心概念

- Mass函数(BPA): m将2^Θ的每个子集映射到[0,1], m(∅)=0, Σm(A)=1
- 信任函数: Bel(A) = Σ m(B), ∀B⊆A — 对A为真的最小支持程度
- 似然函数: Pl(A) = Σ m(B), ∀B∩A≠∅ — 对A为真的最大支持程度
- 冲突系数: K = Σ m1(B)*m2(C), B∩C=∅ — 证据矛盾程度
### 4.3 冲突解决策略

### 4.4 四大证据源

系统从四个独立证据源构建Mass函数，然后通过fuse_evidence()自动选择组合规则进行融合：

### 4.5 S3置信度计算

S3 = max(Bel(FAIL), Bel(PASS))

- Pl(UNCERTAIN) * 0.5          # 不确定性惩罚

- (1 - avg_reliability) * 0.3    # 冲突可靠性惩罚

健康阈值: S3 >= 0.8

### 4.6 裁决逻辑

P0确定性发现 → FAIL (硬阻断, DS融合不覆盖)

AI发现P0但Layer1未检出 → REVIEW (AI_ONLY)

Bel(FAIL) > 0.5 → FAIL (DS证据强支持)

Bel(PASS) > 0.5 且 S3 >= 0.8 → PASS

S3 < 0.8 → GAMMA (置信度不足)

混合证据 → REVIEW (需人工复核)

## 第五章 Phase 3 — 拜占庭对抗测试

### 5.1 设计理念

"连探针本身都不信任" — 每个测试场景模拟一种攻击者视角的对抗性输入，验证探针防御机制是否有效。所有测试必须返回结构化结果: PASS(防御成功) / FAIL(防御失败) / GAMMA(安全降级)。

### 5.2 11个测试场景

### 5.3 S5拜占庭风险计算

S5 = failed_byzantine / total_byzantine = 0/11 = 0.0

健康阈值: S5 <= 0.2 → 当前健康(0.0 <= 0.2)

## 第六章 Phase 4 — 跨函数污点传播与集成流水线

### 6.1 跨函数污点传播 (taint_propagation.py)

#### 6.1.1 ProgramGraph 程序图

从CodeNode列表构建程序图，包含三类边：

- DATA_FLOW: 同一函数内变量赋值的数据流边
- PARAM_EDGE: 跨函数参数传递边 (实参→形参)
- CALL_EDGE: 函数调用边 (caller→callee)
#### 6.1.2 BFS路径搜索

从SOURCE节点到SINK节点执行广度优先搜索，沿数据流边和参数传递边遍历，找到传播路径。

#### 6.1.3 别名分析(传递闭包)

变量赋值链追踪(p=q→q的污点传播给p)，参数传递别名(实参↔形参双向映射)。使用BFS计算传递闭包获取所有别名。

#### 6.1.4 SANITIZER三级阻断检测

这是Phase 4的核心创新，确保SANITIZER在以下三种位置都能被检测到：

### 6.2 集成洋葱流水线 (integrated_pipeline.py)

#### 6.2.1 双解析器架构

集成流水线使用双解析器，互补盲区：

- 解析器A: 增强版主引擎RegexParser — 为所有函数调用创建节点(不只是已知模式)
- 解析器B: 污点传播模块RegexParser — 用于图级分析(函数定义、参数提取)
#### 6.2.2 Gate 7增强

gate7_enhanced_taint() 同时运行主引擎的简单污点检测和跨函数污点传播分析，合并结果去重。

#### 6.2.3 Gate 8增强

gate8_ds_verdict() 集成D-S证据融合，计算完整状态向量S1-S7，替换简单加权平均。

#### 6.2.4 15个集成测试场景

## 第七章 Phase 5 — SecurePi + S1-S7 + 裁决印章

### 7.1 SecurePiDigitProvider 哈希偏移π调度

基于源码哈希+步数联合SHA-256生成π数字(0-9)，用于故障库调度激活。

#### 7.1.1 核心机制

1. 计算源码SHA-256哈希 → source_hash

2. 对每个step, 计算 SHA-256(source_hash + step) → step_hash

3. 从step_hash提取偏移量 offset = int(step_hash[:8], 16) % PI_CACHE_SIZE

4. π数字 = int(PI_DIGITS_1000[offset])

5. 相同step + 相同输入 → 相同π数字 (可复现)

6. 相同step + 不同输入 → 不同π数字 (防共因穿透)

7. step >= PI_CACHE_SIZE → 返回-1 (π耗尽 → GAMMA降级)

#### 7.1.2 故障库π绑定

### 7.2 Gate0-8 独立阻断验证

GateIndependentVerifier验证每个Gate可以独立阻断流水线，不受其他Gate影响。这是拜占庭测伪的核心。

### 7.3 状态向量S1-S7完整计算

StateVectorCalculator独立计算7个状态分量，不依赖base_result默认值(防篡改)。健康阈值由公底层统一定义。

### 7.4 裁决印章 VerdictSeal

生成不可篡改的裁决印章，三层SHA-256哈希链：

1. source_hash: SHA-256(源码) 前32字符

2. hash_self:   SHA-256(裁决报告JSON) 前32字符

3. hash_chain:  SHA-256(source_hash + hash_self + verdict) 前32字符

篡改检测: 任何字段被修改 → hash不一致 → 验证失败

### 7.5 第五阶段完整流水线

run_phase5_pipeline() 在第四阶段集成流水线基础上增加π调度、Gate验证、状态向量和印章。11个测试全部通过。

## 第八章 部署连接指南

### 8.1 文件部署结构

/data/user/work/

├── cle_base_layer.py       # 公底层 (Phase 0)

├── cle_probe_engine.py    # Phase 1: 节点级算子

├── ds_evidence_fusion.py   # Phase 2: D-S证据融合

├── byzantine_tests.py      # Phase 3: 拜占庭测试

├── taint_propagation.py    # Phase 4: 污点传播

├── integrated_pipeline.py # Phase 4: 集成流水线

├── secure_pi_provider.py  # Phase 5: SecurePi + 印章

├── layer2_cross_audit.py  # Layer 2: 交叉比对

├── cle_deploy.py           # 部署入口 (连接所有模块)

└── fault_library_1000.json # 1000条故障库

### 8.2 模块连接方式

所有模块通过Python的import机制连接，公底层提供统一的常量和类型定义。部署入口cle_deploy.py连接所有模块，提供统一的调用接口。

#### 8.2.1 导入链

cle_deploy.py (部署入口)

│

├── from cle_base_layer import *       # 公底层常量/类型

├── from cle_probe_engine import *     # Phase 1

├── from ds_evidence_fusion import *   # Phase 2

├── from byzantine_tests import *     # Phase 3

├── from taint_propagation import *    # Phase 4

├── from integrated_pipeline import *  # Phase 4 (集成)

├── from secure_pi_provider import *   # Phase 5

└── from layer2_cross_audit import *   # Layer 2

#### 8.2.2 调用链

外部使用者只需调用cle_deploy.py的CLEDeployer类，内部自动按正确顺序调用各Phase模块：

CLEDeployer.run_audit(source_code)

└── run_phase5_pipeline(source_code)        # Phase 5入口

└── run_integrated_probe(source_code)  # Phase 4入口

├── gate0_empty_block()           # Phase 1: Gate 0

├── enhanced_gate1_parse()         # Phase 4: 增强解析

├── parse_with_taint_module()      # Phase 4: 污点解析

├── gate2_build_graph()           # Phase 1: Gate 2

├── gates3_6_node_operators()     # Phase 1: Gate 3-6

├── gate7_enhanced_taint()        # Phase 4: Gate 7

└── gate8_ds_verdict()            # Phase 2+4: Gate 8

└── SecurePiDigitProvider()           # Phase 5: π调度

└── StateVectorCalculator()          # Phase 5: S1-S7

└── VerdictSeal.generate_seal()      # Phase 5: 印章

### 8.3 部署使用方式

#### 8.3.1 单文件审计

python3 cle_deploy.py audit source.c

执行Phase 1-5完整流水线，输出裁决报告含状态向量和印章。

#### 8.3.2 双层审计

python3 cle_deploy.py dual source.c

执行Layer 1(CLE探针) + Layer 2(AI语义审查)交叉比对，生成最终裁决。

#### 8.3.3 拜占庭测试

python3 cle_deploy.py byzantine

执行11个对抗性测试场景，验证探针防御机制。

#### 8.3.4 模块验证

python3 cle_deploy.py verify

验证所有模块的导入完整性和基本功能。

### 8.4 编程式调用

from cle_deploy import CLEDeployer

deployer = CLEDeployer()

# 单层审计

result = deployer.run_audit(source_code, 'test.c')

print(result['verdict'])  # FAIL/PASS/GAMMA

# 双层审计

result = deployer.run_dual_audit(source_code, 'test.c')

# result['ai_review_prompt'] → 发给AI → 获取JSON → finalize_cross_audit()

# 拜占庭测试

report = deployer.run_byzantine()

print(report['final_verdict'])  # PASS

# 模块验证

verification = deployer.verify_modules()

print(verification['all_passed'])  # True/False

## 第九章 完整工作流设计整合

### 9.1 端到端审计流程

以下是CLE V3.8.2从源码输入到最终裁决的完整工作流，整合了全部五个阶段的能力：

#### Step 1: 输入加载 (部署入口)

- 用户通过cle_deploy.py提交源码(文件/字符串/Markdown)
- Deployer.load_source()统一加载，支持从Markdown提取C源码
- Gate 0空输入阻断：空/纯空白/纯注释 → GAMMA
#### Step 2: 预处理 (公底层)

- 注释剥离: strip_c_comments() — 防止注释伪造(拜占庭场景1)
- 字符串剥离: strip_string_literals() — 防止字符串内/的假阳性
#### Step 3: 双解析器解析 (Phase 4)

- 解析器A: enhanced_gate1_parse() — 为所有函数调用创建节点
- 解析器B: parse_with_taint_module() — RegexParser解析为CodeNode + GraphBuilder建图
- Gate 1阻断: 零节点 → GAMMA
#### Step 4: 图构建 (Phase 1+4)

- 主引擎图: gate2_build_graph() — 线性边连接
- 污点传播图: GraphBuilder.build() — DATA_FLOW/PARAM_EDGE/CALL_EDGE三类边
- Gate 2阻断: 图无效 → GAMMA
#### Step 5: 节点级算子遍历 (Phase 1, Gate 3-6)

- OP_TimeMonotonicity: 检测时间戳溢出 → P0
- OP_ResourceBound: 检测资源未检查(±3行窗口) → P0
- OP_StateBoundedness: 检测除法/溢出/越界 → P0/P1
- 异常隔离: 算子异常被捕获，记录GAMMA事件，不中断链
#### Step 6: 图级污点传播 (Phase 4, Gate 7)

- TaintPropagationAnalyzer.analyze() — BFS路径搜索
- 别名分析: 传递闭包追踪变量赋值链和参数传递
- SANITIZER三级阻断检测: 函数内行号/BFS路径中间函数/中间调用函数
- 未阻断路径 → P0, SANITIZER阻断 → P1(REVIEW)
#### Step 7: D-S证据融合 (Phase 2, Gate 8)

- 构建4个证据源Mass函数: Layer1/Signature/AST
- fuse_evidence()自动选择Dempster/Yager规则
- compute_s3_confidence()计算S3置信度
- P0硬阻断 → FAIL (DS融合不覆盖确定性发现)
#### Step 8: SecurePi调度 (Phase 5)

- SecurePiDigitProvider: 基于source_hash+step生成π数字
- 故障库π绑定: 0-3通用/4-DOC/5-MOD/6-LLM/7-WEB/8-9-EVASION
- π耗尽 → 返回-1 → GAMMA降级
#### Step 9: 状态向量计算 (Phase 5)

- StateVectorCalculator.calculate_full() — 独立计算S1-S7
- 健康阈值: S3>=0.8, S5<=0.2, S6<0.8
- 不依赖base_result默认值(防篡改)
#### Step 10: 裁决印章 (Phase 5)

- VerdictSeal.generate_seal() — 三层SHA-256哈希链
- source_hash + hash_self + hash_chain
- 篡改检测: verdict FAIL→PASS → hash不一致
#### Step 11: 拜占庭验证 (Phase 3)

- run_all_byzantine_tests() — 11个对抗场景
- S5 = failed_byzantine / total_byzantine
- 全部通过 → S5=0.0 → 健康
#### Step 12: 输出裁决 (部署入口)

- 最终裁决: FAIL/PASS/GAMMA/REVIEW
- 状态向量S1-S7 + 健康判定
- π调度信息 + 裁决印章 + 验证结果
- SHA-256哈希链保证不可篡改
### 9.2 数据流整合图

源码输入

│

▼ [Gate 0] 空输入? → GAMMA ───┐

│                              │

▼ 预处理: 注释剥离+字符串剥离   │

│                              │

▼ [Gate 1] 双解析器 → CodeNode │

│   零节点? → GAMMA ──────────┤

│                              │

▼ [Gate 2] 建图 → ProgramGraph │

│   图无效? → GAMMA ──────────┤

│                              │

▼ [Gate 3-6] 节点级算子         │

│   Time/Resource/State → P0   │

│                              │

▼ [Gate 7] 污点传播             │

│   BFS+别名+SANITIZER三级阻断  │

│   SOURCE→SINK无阻断 → P0     │

│   SANITIZER阻断 → P1(REVIEW) │

│                              │

▼ [Gate 8] D-S融合 + 裁决       │

│   P0 > 0 → FAIL (硬阻断)     │

│   Bel(FAIL)>0.5 → FAIL       │

│   S3 < 0.8 → GAMMA           │

│   Bel(PASS)>0.5 → PASS       │

│                              │

▼ SecurePi调度                  │

│   π耗尽 → GAMMA降级           │

│                              │

▼ 状态向量 S1-S7                │

│   健康判定                    │

│                              │

▼ 裁决印章                      │

│   SHA-256三层哈希链           │

│                              │

▼ 拜占庭验证 (11场景)           │

│   S5 = 0.0 (全部通过)         │

│                              │

▼ 最终输出                      │

│   verdict + findings + S1-S7 │

│   + π + 印章 + 验证           │

│                              │

└──────────────────────────────┘

### 9.3 防数据污染机制总结

公底层(cle_base_layer.py)通过以下机制防止AI混淆概念和数据污染：

## 第十章 补充的代码接口

### 10.1 公底层模块 (cle_base_layer.py)

新增的公底层模块统一定义了九大部分：

- NodeAttr: 节点属性位掩码枚举(IntFlag)
- Severity/Verdict: 严重级别和裁决类型枚举
- PEFLayer/PEFCategory: PEF三层映射枚举
- CodeNode/AuditEvent/StateVector: 核心数据类型(dataclass)
- SystemConfig: 系统配置参数集中管理
- ModuleRegistry: 模块注册表与依赖链追踪
- 公共工具函数: compute_sha256_prefix/strip_c_comments等
### 10.2 部署入口 (cle_deploy.py)

新增的部署入口模块连接所有Phase，提供统一调用接口：

### 10.3 命令行接口

用法: python3 cle_deploy.py <mode> [filepath] [options]

模式:

audit <file>      单文件审计 (Phase 1-5完整流水线)

dual <file>       双层审计 (Layer 1 + Layer 2交叉比对)

byzantine         拜占庭对抗测试 (11个场景)

verify            模块完整性验证

选项:

--verbose, -v     详细输出findings详情

### 10.4 接口完整性验证清单

### 10.5 系统局限性诚实声明

CLE V3.8.2 存在以下物理极限，审计时需知晓：

- 1. 正则解析非完整AST → 宏展开/模板元编程失效
- 2. 符号执行路径爆炸 → 受限于MAX_PATHS=1000
- 3. D-S证据Mass函数参数为经验值 → 无数学最优证明
- 4. OP_TimeMonotonicity模式脆弱 → 仅识别直接写法
- 5. 跨函数污点传播已完整 → 15个测试全通过
- 6. 拜占庭测试完整覆盖 → 11个场景全通过(S5=0.0)
- 7. 特征库720条为伪码生成 → 需人工验证
- 8. 权限校验非跨平台 → Windows无chmod
- 9. AI Layer 2欺诈风险 → V1-V6反欺诈协议强制执行
## 附录

### 附录A: 物理极限参数配置

MAX_PATHS = 1000              # 符号执行最大路径数

TIMEOUT_SECONDS = 30          # 单次扫描超时

AST_COVERAGE_THRESHOLD = 0.5  # AST覆盖率下限

MAX_LINE_LENGTH = 10000       # 正则匹配最大行长度

PI_CACHE_SIZE = 100           # π数字缓存大小

NULL_CHECK_WINDOW = 3         # 多行NULL检查窗口

DS_CONFLICT_LOW = 0.5        # D-S冲突低阈值

DS_CONFLICT_HIGH = 0.75       # D-S冲突高阈值

BYZANTINE_TOTAL = 11          # 拜占庭场景总数

BYZANTINE_RISK_THRESHOLD = 0.2 # S5健康阈值

### 附录B: 节点属性位掩码速查

### 附录C: 模块文件清单

### 附录D: 反欺诈验证协议 (V1-V6)

每次Layer 2 AI审查完成后强制执行，AI无权自行豁免：

| 阶段 | 名称 | 核心模块 | 关键能力 |
| --- | --- | --- | --- |
| Phase 1 | 节点级算子 | cle_probe_engine.py | Gate 0-8, Time/Resource/State算子 |
| Phase 2 | D-S证据融合 | ds_evidence_fusion.py | Mass函数, Dempster/Yager组合, S3置信度 |
| Phase 3 | 拜占庭对抗测试 | byzantine_tests.py | 11个对抗场景, 防御机制验证 |
| Phase 4 | 跨函数污点传播 | taint_propagation.py + integrated_pipeline.py | ProgramGraph, BFS, 别名分析, 集成流水线 |
| Phase 5 | SecurePi + 印章 | secure_pi_provider.py | 哈希偏移π调度, S1-S7, SHA-256印章 |


| Gate | 名称 | 阻断条件 | 阻断裁决 |
| --- | --- | --- | --- |
| Gate 0 | 空输入阻断 | 源码为空/纯空白/纯注释 | GAMMA |
| Gate 1 | 解析CodeNode | 解析出0个节点 | GAMMA |
| Gate 2 | 建图 | 图无效(无节点/无边) | GAMMA |
| Gate 3 | 时间单调性 | Hal_GetTick()*N溢出 | FAIL(P0) |
| Gate 4 | 资源界限 | malloc/fopen/socket未检查NULL | FAIL(P0) |
| Gate 5 | 状态有界性 | 除法未检查除数为零 | FAIL(P0) |
| Gate 6 | 节点属性 | 算子异常被隔离 | GAMMA |
| Gate 7 | 图级污点传播 | SOURCE→SINK无SANITIZER阻断 | FAIL(P0)/REVIEW(P1) |
| Gate 8 | D-S融合+裁决 | S3<0.8 / Bel(FAIL)>0.5 / π耗尽 | FAIL/GAMMA |


| 属性 | 值 | 含义 |
| --- | --- | --- |
| DANGER_SINK | 0x001 | 危险汇聚点 (system, exec, strcpy...) |
| SAFE_SINK | 0x002 | 安全汇聚点 (经清洗) |
| SOURCE_INPUT | 0x004 | 外部输入源 (scanf, recv, read...) |
| SANITIZER | 0x008 | 清洗函数 (escape, validate...) |
| BLOCKER | 0x010 | 阻断函数 (auth_check...) |
| FLOAT_OP | 0x020 | 浮点运算 |
| BLOCKING_DELAY | 0x040 | 阻塞延时 (abort, exit...) |
| ALLOC_CALL | 0x080 | 内存分配 (malloc, calloc...) |
| DEALLOC_CALL | 0x100 | 内存释放 (free, fclose...) |
| LOCK_ACQUIRE | 0x200 | 锁获取 (pthread_mutex_lock) |
| LOCK_RELEASE | 0x400 | 锁释放 (pthread_mutex_unlock) |
| TAINTED | 0x800 | 污点标记 (传播过程中标记) |


| 维度 | 物理含义 | 计算公式 | 健康阈值 |
| --- | --- | --- | --- |
| S1 | 可解析性 | parsed_nodes / total_nodes | 无 |
| S2 | 图完整性 | min(1.0, edges / (nodes-1)) | 无 |
| S3 | 置信度 | D-S融合Bel/Pl函数 | >= 0.8 |
| S4 | 偏差率 | unexpected / total_findings | 无 |
| S5 | 拜占庭风险 | failed_byzantine / total | <= 0.2 |
| S6 | π覆盖率 | pi_step / pi_cache_size | < 0.8 |
| S7 | AST覆盖率 | ast_parsed / total_nodes | 无 |


| 参数 | 默认值 | 用途 |
| --- | --- | --- |
| MAX_PATHS | 1000 | 符号执行最大路径数 |
| TIMEOUT_SECONDS | 30 | 单次扫描超时 |
| PI_CACHE_SIZE | 100 | π数字缓存大小 |
| MAX_LINE_LENGTH | 10000 | 正则匹配最大行长度 |
| NULL_CHECK_WINDOW | 3 | 多行NULL检查窗口(±N行) |
| DS_CONFLICT_LOW | 0.5 | D-S冲突系数低阈值 |
| DS_CONFLICT_HIGH | 0.75 | D-S冲突系数高阈值 |


| 函数名 | 用途 | Gate |
| --- | --- | --- |
| gate0_empty_block(source) | 空输入检查 | Gate 0 |
| gate1_parse_nodes(lines, filename) | 解析CodeNode | Gate 1 |
| gate2_build_graph(nodes) | 构建程序图 | Gate 2 |
| gates3_6_node_operators(graph, lines) | 节点级算子遍历 | Gate 3-6 |
| gate7_graph_operators(graph) | 图级污点检测 | Gate 7 |
| gate8_verdict(graph, findings, source) | 裁决与印章 | Gate 8 |
| run_probe(source_text, filename) | 完整流水线入口 | All |


| 冲突系数K | 策略 | 规则 | 可靠性 |
| --- | --- | --- | --- |
| K < 0.5 | 正常融合 | Dempster归一化组合 | HIGH |
| 0.5 <= K < 0.75 | 警告融合 | Yager规则(冲突保留到Θ) | MEDIUM |
| K >= 0.75 | 高冲突 | Yager规则 + 标记不可靠 | LOW |


| 证据源 | FAIL质量 | PASS质量 | 特点 |
| --- | --- | --- | --- |
| Layer1 CLE探针 | P0×0.25/条(上限0.85) | 剩余分配 | 确定性, 权重最高 |
| Layer2 AI审查 | P0×0.10/条(上限0.6) | 剩余分配 | 有幻觉风险, 权重低 |
| 特征签名匹配 | 比例×0.4(上限0.5) | 剩余分配 | 模式匹配 |
| AST子图分析 | 发现×0.08(上限0.4) | 剩余分配 | 结构分析 |


| # | 场景 | 攻击载荷 | 防御机制 | 结果 |
| --- | --- | --- | --- | --- |
| 1 | 语料投毒 | 注释中伪造SAFE_SINK | strip_comments()注释剥离 | PASS |
| 2 | 共因穿透 | 预测π序列(20步) | source_hash+step联合SHA-256 | PASS |
| 3 | 时序撕裂 | 污点路径分片到3函数 | GlobalTaintTable跨分片合并 | PASS |
| 4 | ReDoS注入 | 50000字符+灾难正则 | MAX_LINE_LENGTH截断+超时 | PASS |
| 5 | 特征库篡改 | P0→P1降级 | SHA-256哈希校验 | PASS |
| 6 | 算子崩溃隔离 | 注入抛异常算子 | try-except捕获+GAMMA事件 | PASS |
| 7 | 状态向量篡改 | S5=0.0(实际0.273) | 裁决使用独立计算值 | PASS |
| 8 | 审计结果篡改 | verdict FAIL→PASS | SHA-256哈希链检测 | PASS |
| 9 | 空输入绕过 | 6种空/纯注释输入 | Gate 0空输入阻断→GAMMA | PASS |
| 10 | π耗尽 | 消耗π缓存请求15步 | get_digit返回-1→GAMMA | PASS |
| 11 | MAX_LINE=0 | 行长度限制设为0 | <=0安全降级为GAMMA | PASS |


| 级别 | 检测位置 | 检测条件 |
| --- | --- | --- |
| 1 | 函数内行号 | SANITIZER在SOURCE/SINK所在函数中且行号在两者之间 |
| 2 | BFS路径中间函数 | SANITIZER在BFS路径涉及的中间函数中 |
| 3 | 中间调用函数 | SOURCE之后/SINK之前的函数调用，被调用函数含SANITIZER |


| # | 场景 | 预期裁决 | 预期P0 |
| --- | --- | --- | --- |
| 1 | 函数内污点(scanf→system) | FAIL | 1 |
| 2 | 跨函数污点(scanf→exec→system) | FAIL | 1 |
| 3 | SANITIZER阻断(scanf→escape→system) | REVIEW | 0 |
| 4 | 别名传播(src→p→q→system) | FAIL | 1 |
| 5 | 安全代码(无SOURCE/SINK) | PASS | 0 |
| 6 | 空输入 | GAMMA | 0 |
| 7 | 多源单汇聚(scanf+getenv→system) | FAIL | >=1 |
| 8 | fopen未检查(P0) | FAIL | >=1 |
| 9 | malloc未检查(P0) | FAIL | >=1 |
| 10 | fopen有NULL检查(安全) | PASS | 0 |
| 11 | 时间戳溢出(Hal_GetTick*1000) | FAIL | >=1 |
| 12 | 除法未检查除数为零 | FAIL | >=1 |
| 13 | 跨函数SANITIZER阻断 | REVIEW | 0 |
| 14 | 混合缺陷(污点+资源) | FAIL | >=2 |
| 15 | 安全(fopen+NULL+escape阻断) | REVIEW | 0 |


| 故障库名称 | π范围 | 用途 |
| --- | --- | --- |
| general (通用) | 0-3 | 通用特征匹配 |
| doc (文档) | 4 | 文档类缺陷 |
| mod (模块) | 5 | 模块架构契约 |
| llm (AI) | 6 | AI语义审查 |
| web (Web) | 7 | Web安全 |
| evasion (对抗) | 8-9 | 对抗性测试 |


| Gate | 测试场景 | 阻断条件 | 结果 |
| --- | --- | --- | --- |
| Gate 0 | 空输入阻断 | 空字符串 → GAMMA | PASS |
| Gate 1 | 零节点阻断 | 纯注释 → 0节点 → GAMMA | PASS |
| Gate 2 | 图无效阻断 | 单声明 → 图退化 → GAMMA | PASS |
| Gate 3 | 时间单调性P0 | Hal_GetTick*1000 → P0 | PASS |
| Gate 4 | 资源界限P0 | fopen未检查 → P0 | PASS |
| Gate 5 | 状态有界性P0 | 除法未检查 → P0 | PASS |
| Gate 6 | 节点属性P0 | malloc未检查 → P0 | PASS |
| Gate 7 | 污点传播P0 | scanf→system → P0 | PASS |
| Gate 7 | SANITIZER阻断P1 | scanf→escape→system → REVIEW | PASS |
| Gate 8 | D-S融合FAIL | P0硬阻断 → FAIL | PASS |
| Gate 8 | S3不足GAMMA | 空输入 → GAMMA | PASS |
| Gate 8 | π耗尽GAMMA | cache=5请求6步 → GAMMA | PASS |


| 机制 | 实现方式 | 防止的问题 |
| --- | --- | --- |
| 单一事实来源 | 所有常量只在base_layer定义一次 | 不同模块使用不同常量值 |
| 类型安全枚举 | IntFlag/Enum替代裸整数/字符串 | 拼写错误导致逻辑bug |
| 统一数据结构 | CodeNode/AuditEvent/StateVector统一定义 | dict/dataclass混用导致类型错误 |
| 集中配置管理 | SystemConfig类管理所有参数 | 硬编码参数无法统一调整 |
| 模块注册表 | ModuleRegistry记录模块元信息 | AI混淆不同Phase的功能边界 |
| 依赖链追踪 | get_dependency_chain()获取完整依赖 | 循环依赖或缺失依赖 |
| 公共工具函数 | 统一hash/strip/check函数 | 不同模块用不同算法导致不一致 |


| 类/方法 | 用途 | 连接的Phase |
| --- | --- | --- |
| CLEDeployer | 部署器主类 | All |
| CLEDeployer.load_source() | 加载源码(文件/MD/字符串) | 部署 |
| CLEDeployer.run_audit() | 单层审计(Phase 1-5) | 1-5 |
| CLEDeployer.run_dual_audit() | 双层审计(Layer1+Layer2) | 1-5+L2 |
| CLEDeployer.run_byzantine() | 拜占庭测试 | 3 |
| CLEDeployer.verify_modules() | 模块完整性验证 | All |
| CLEDeployer.print_report() | 格式化报告输出 | All |
| DeployConfig | 部署配置参数 | All |


| 接口 | 模块 | 状态 | 验证方法 |
| --- | --- | --- | --- |
| gate0_empty_block | Phase 1 | 完整 | 空输入→GAMMA |
| gate1_parse_nodes | Phase 1 | 完整 | 解析CodeNode列表 |
| gate2_build_graph | Phase 1 | 完整 | 建图+边连接 |
| gates3_6_node_operators | Phase 1 | 完整 | 三算子遍历 |
| gate7_enhanced_taint | Phase 4 | 完整 | 跨函数污点+BFS |
| gate8_ds_verdict | Phase 2+4 | 完整 | D-S融合+S1-S7 |
| fuse_evidence | Phase 2 | 完整 | Dempster/Yager自动选择 |
| compute_s3_confidence | Phase 2 | 完整 | Bel/Pl置信度计算 |
| run_all_byzantine_tests | Phase 3 | 完整 | 11场景全通过 |
| TaintPropagationAnalyzer | Phase 4 | 完整 | BFS+别名+SANITIZER |
| run_integrated_probe | Phase 4 | 完整 | 双解析器集成 |
| SecurePiDigitProvider | Phase 5 | 完整 | 哈希偏移π调度 |
| GateIndependentVerifier | Phase 5 | 完整 | 12个Gate阻断 |
| StateVectorCalculator | Phase 5 | 完整 | S1-S7独立计算 |
| VerdictSeal | Phase 5 | 完整 | 三层哈希链印章 |
| run_phase5_pipeline | Phase 5 | 完整 | Phase 1-5完整流水线 |
| CLEDeployer | 部署入口 | 新增 | 统一调用接口 |
| ModuleRegistry | 公底层 | 新增 | 模块注册+依赖链 |


| 属性 | 值 | 检测算子 |
| --- | --- | --- |
| DANGER_SINK | 0x001 | TaintPropagation |
| SAFE_SINK | 0x002 | TaintPropagation |
| SOURCE_INPUT | 0x004 | TaintPropagation |
| SANITIZER | 0x008 | TaintPropagation |
| BLOCKER | 0x010 | TaintPropagation |
| FLOAT_OP | 0x020 | StateBoundedness |
| BLOCKING_DELAY | 0x040 | TimeMonotonicity |
| ALLOC_CALL | 0x080 | ResourceBound |
| DEALLOC_CALL | 0x100 | ResourceBound |
| LOCK_ACQUIRE | 0x200 | ResourceBound |
| LOCK_RELEASE | 0x400 | ResourceBound |
| TAINTED | 0x800 | TaintPropagation |


| 文件名 | Phase | 模块名 | 代码行数(约) |
| --- | --- | --- | --- |
| cle_base_layer.py | 0 | 公底层定义 | 350 |
| cle_probe_engine.py | 1 | 节点级算子引擎 | 714 |
| ds_evidence_fusion.py | 2 | D-S证据融合 | 705 |
| byzantine_tests.py | 3 | 拜占庭对抗测试 | 701 |
| taint_propagation.py | 4 | 跨函数污点传播 | 952 |
| integrated_pipeline.py | 4 | 集成洋葱流水线 | 862 |
| secure_pi_provider.py | 5 | SecurePi+印章 | 1023 |
| layer2_cross_audit.py | L2 | 交叉比对引擎 | 418 |
| cle_deploy.py | 部署 | 部署入口(新增) | 320 |
| fault_library_1000.json | 数据 | 1000条故障库 | 1000条 |


| # | 验证项 | 通过标准 | 不通过后果 |
| --- | --- | --- | --- |
| V1 | 来源溯源 | AI能指出具体代码行号和推理过程 | 标记AI欺诈, 结果作废 |
| V2 | 独立复现 | 不使用工具也能发现同样问题 | 降级为AI_ONLY_LOW |
| V3 | 遍历证据 | 给出阅读路径(文件→函数→行号) | 标记AI未遍历, 审查无效 |
| V4 | 盲区自检 | 诚实区分工具发现和AI推理发现 | 触发信任重置 |
| V5 | 编译验证 | AI发现应覆盖编译器报错 | 需补充审查 |
| V6 | 冒烟测试 | PASS必须意味着代码可运行 | 降级为GAMMA |




---
*PEF Architecture © 2026 banbanry (沈鹭). Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
