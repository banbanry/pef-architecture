> **Source**: https://github.com/banbanry/pef-architecture/04-engineering-cases/cle-probe
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生


# CLE V3.8.2 — 确定性代码探针系统 L1-L3技术文档

CLE V3.8.2

确定性代码探针系统

L1-L3三层完整技术文档

五阶段全量整合 + PEF算子库扩展 + 双层交叉审计 + 拜占庭注入验收

Phase 1: 1000条故障库 | Phase 2: D-S证据融合 | Phase 3: 拜占庭测试

Phase 4: 跨函数污点传播 | Phase 5: SecurePi+S1-S7+印章

PEF扩展: 11个E层算子 | L2: AI语义审查15类 | L3: 4类金丝雀注入验收

版本: V3.8.2  日期: 2026-09-02

## 文档目录

本文档合并了CLE V3.8.2五个开发阶段的全部技术文档，并新增PEF算子库扩展、Layer 2 AI交叉审计、Layer 3拜占庭脏数据注入验收和管线断裂修复内容。

## 第零章 系统架构总览

CLE V3.8.2是五阶段开发完成并通过PEF算子库扩展的确定性代码审计系统。核心理念: 不依赖AI主观判断，通过物理不变量算子+1000条PEF/MOD故障库匹配+11个PEF扩展算子+洋葱流水线Gate0-8，输出结构化的PASS/FAIL/GAMMA裁决。V3.8.2新增三层架构: L1确定性探针、L2 AI语义审查、L3拜占庭脏数据注入验收。

### 0.1 三层审计架构

系统采用三层递进式审计架构，每层有明确职责:

### 0.2 五阶段+PEF扩展开发历程

### 0.3 模块依赖关系

所有模块均依赖公底层(cle_base_layer.py)提供统一常量和类型定义。模块间通过明确的接口连接，禁止跨层直接调用。

cle_base_layer (公底层)

├── Phase 1: cle_probe_engine (+ fault_library_1000.json)

├── Phase 2: ds_evidence_fusion

├── Phase 3: byzantine_tests

├── Phase 4: taint_propagation + integrated_pipeline

├── Phase 5: secure_pi_provider

├── PEF扩展: pef_operators (11个E层算子)

├── Layer 2: layer2_cross_audit (AI交叉比对+确定性回退)

└── Layer 3: layer3_injection_verifier (拜占庭脏数据注入验收)

### 0.4 洋葱流水线 Gate 0-8

## 第一章 公底层定义 (防数据污染)

公底层(cle_base_layer.py)通过"单一事实来源"原则，统一定义所有共享常量、数据类型、协议接口和配置管理，防止AI混淆普通概念造成数据污染。

### 1.1 九大定义

### 1.2 节点属性位掩码

### 1.3 状态向量S1-S7

## 第二章 Phase 1 --- 1000条PEF/MOD故障库

故障库采用四层分层架构(P层300条/E层350条/F层200条/MOD层150条)，共1000条故障定义。每条包含: id, name, sev(P0/P1), op(对应算子), trig(正则触发模式), fix(修复指引), pi(π偏移值)。

## 第三章 Phase 2 --- Dempster-Shafer证据融合

识别框架 Θ = {FAIL, PASS, UNCERTAIN}。通过四大证据源(Layer1 CLE探针/Layer2 AI审查/特征签名/AST子图)的Mass函数，使用Dempster/Yager组合规则进行融合，计算S3置信度。

### 3.1 冲突解决策略

## 第四章 Phase 3 --- 11个拜占庭对抗测试场景

审计完成后执行11个对抗性测试场景验证探针防御机制，覆盖语料投毒、共因穿透、时序撕裂、ReDoS、特征篡改、崩溃隔离、状态篡改、审计篡改、空输入绕过、π耗尽、MAX_LINE=0等攻击向量。S5 = failed_byzantine / total_byzantine，当前值=0.0(11/11通过)。

## 第五章 Phase 4 --- 跨函数污点传播图遍历 + 集成洋葱流水线

Phase 4实现了完整的跨函数污点传播分析，替换单函数taint_table匹配。核心组件包括: ProgramGraph(程序图)、BFS路径搜索、别名分析(含参数传递别名映射)、三级SANITIZER阻断检测。集成模块integrated_pipeline.py统一Gate 0-8，双解析器(主引擎+污点传播模块)。15个集成测试场景全部通过。

### 5.1 三级SANITIZER阻断检测

## 第六章 Phase 5 --- SecurePiDigitProvider π调度 + Gate0-8独立阻断 + S1-S7 + 裁决印章

Phase 5实现三大核心组件: SecurePiDigitProvider哈希偏移π调度(基于源码哈希+步数联合SHA-256生成π数字0-9)、Gate0-8独立阻断验证(12个阻断场景全部通过)、状态向量S1-S7完整计算和SHA-256裁决印章(三层哈希链: source_hash + hash_self + hash_chain)。11个测试全部通过。

### 6.1 裁决印章

SHA-256三层哈希链保证不可篡改:

Layer 1: source_hash = SHA-256(source_code)[:32]

Layer 2: hash_self = SHA-256(verdict + p0_count + p1_count + source_hash)[:32]

Layer 3: hash_chain = SHA-256(hash_self + pi_sequence + state_vector)[:32]

篡改检测: verdict FAIL→PASS → hash_self不匹配 → 检测通过

## 第七章 部署连接指南

### 7.1 模块文件清单与导出

### 7.2 部署入口调用链

CLEDeployer类是唯一的外部调用入口，内部连接所有模块:

CLEDeployer.run_audit(source_code)

└── run_phase5_pipeline()          # Phase 5入口

└── run_integrated_probe()    # Phase 4集成流水线

├── gate0_empty_block()  # Phase 1: Gate 0

├── enhanced_gate1_parse() + parse_with_taint_module()  # Phase 4: 双解析器

├── gate2_build_graph()  # Phase 1: Gate 2

├── gates3_6_node_operators()  # Phase 1: Gate 3-6

├── gate7_enhanced_taint()  # Phase 4: Gate 7

└── gate8_ds_verdict()  # Phase 2+4: Gate 8

└── SecurePiDigitProvider()   # Phase 5: π调度

└── StateVectorCalculator()  # Phase 5: S1-S7

└── VerdictSeal.generate_seal()  # Phase 5: 印章

└── run_pef_operators()            # PEF扩展: 11算子扫描

├── PlaceholderDetector (E033)     # 空包占位符

├── LogicChainVerifier (E056)      # 逻辑链断裂

├── DeadCodeDetector (E034)        # 死代码

├── MathPropertyVerifier (E022)    # 数学性质

├── StringLiteralValidator (E040)  # 字符串有效性

├── UnimplementedDeclDetector (E035) # 未实现声明

├── BufferOverflowDetector (E039)  # 缓冲区溢出

├── UninitMemoryDetector (E041)   # 未初始化内存

├── ResourceLeakDetector (E043)    # 资源泄漏

├── IntegerOverflowDetector (E150) # 整数溢出

├── PathCoverageAnalyzer (E049)    # 路径覆盖

└── RaceConditionDetector (E042)   # 数据竞争

→ PEF发现合并到findings, P0自动升级裁决

CLEDeployer.run_dual_audit(source_code) 在 run_audit() 完成后:

1. 生成L2 AI审查提示(15类全量审查清单)

2. 执行L2确定性回退(run_layer2_deterministic_fallback) — PEF算子作为AI未返回结果时的安全网

3. 等待外部AI填充审查JSON → finalize_cross_audit交叉比对

CLEDeployer.run_injection_verification(source_code) 在双层审计完成后:

1. 在源码副本中注入4类金丝雀(C1/C2/C3/C4)

2. 对注入后的代码运行Layer 1 (CLE探针)

3. 验证Layer 1是否检出C1/C2 (未检出=CLE_PROBE_BLIND)

4. 验证Layer 2是否检出C1/C4 (未检出=AI_FAKE_AUDIT)

5. 输出验收裁决: VERIFIED / FRAUD_DETECTED / SUSPICIOUS

## 第八章 完整工作流设计整合

三层审计完整工作流: 源代码 → L1确定性探针 → L2 AI语义审查 → L3拜占庭注入验收 → 最终裁决。

### 8.1 命令行调用

# 单文件审计 (Layer 1 确定性探针 + PEF扩展)

python3 /data/user/work/cle_deploy.py audit source.c

# 双层审计 (Layer 1 + Layer 2 AI交叉比对)

python3 /data/user/work/cle_deploy.py dual source.c

# 拜占庭对抗测试 (11个场景)

python3 /data/user/work/cle_deploy.py byzantine

# 脏数据注入验收 (Layer 3 防假测试)

python3 /data/user/work/cle_deploy.py inject source.c

# 模块完整性验证

python3 /data/user/work/cle_deploy.py verify

## 第九章 PEF算子库扩展 (11个E层算子)

从PEF算子库500+条中系统性筛选11个E层算子，适配为CLE确定性探针。这批算子填补了原始4大算子(TimeMonotonicity/ResourceBound/StateBoundedness/TaintPropagation)的检测盲区，覆盖空包占位符、逻辑链断裂、死代码、缓冲区溢出、资源泄漏等关键缺陷类型。

实现模块: pef_operators.py

适配原则: 用正则模式实现E层算子的核心检测逻辑，不依赖完整AST。

### 9.1 第一批6个算子 (覆盖空包占位符/逻辑链断裂/死代码)

### 9.2 第二批6个算子 (覆盖内存安全/资源泄漏/路径覆盖)

### 9.3 关键算子检测逻辑详解

#### PlaceholderDetector (E033 Frama-C适配)

在注释剥离前执行检测。占位符模式: TODO/FIXME/HACK/暂不实现/placeholder/stub/not implemented。空函数体模式: 函数定义只有花括号或只有return true/false/0/1/nullptr。

关键修复: 注释剥离前先扫描占位符标记，因为占位符标记本身就在注释中。

#### LogicChainVerifier (E056 CEGAR适配)

检测数据流断裂和错误路径缺失。模式1: load/init/configure返回值未检查(后续3行内无if检查)。模式2: 变量声明后未初始化即使用。模式3: if失败后无else(简单检测)。

#### BufferOverflowDetector (E039 ASan适配)

检测缓冲区溢出。模式1: find()返回npos后直接substr(P0级)。模式2: 数组访问前无边界检查(P1级)。检测strcpy/sprintf无边界限制。

NPOS_RISK_PATTERN: 匹配 .substr 在 .find 之后且未检查 npos 的模式。

#### ResourceLeakDetector (E043 Valgrind适配)

检测资源泄漏。模式1: 文件句柄(fopen/ifstream)打开后未见close。模式2: new后无delete。模式3: 异常路径泄漏(try块中分配但catch块未释放)。

### 9.4 PEF算子接入L1管线 (F1修复)

在cle_deploy.py的run_audit()中，Phase 5流水线完成后自动调用run_pef_operators()，将11个算子的扫描结果合并到findings列表中。P0发现自动升级裁决(原PASS→FAIL)，P1发现触发REVIEW(原PASS→REVIEW)。

代码位置: cle_deploy.py → run_audit() → PEF_OPERATORS_AVAILABLE 检查 → run_pef_operators(source_code)

## 第十章 Layer 2 AI语义审查与交叉比对

在Layer 1确定性探针(含PEF扩展算子)完成后，AI对同一份源码执行语义级审查。AI审查不替代Layer 1，而是独立验证全部15类问题，不因L1已覆盖就跳过。

实现模块: layer2_cross_audit.py

### 10.1 AI审查15类全量清单

### 10.2 L2确定性回退 (F3修复)

当AI未返回有效审查结果时，自动执行run_layer2_deterministic_fallback()，使用PEF算子作为确定性补充。结果明确标记来源为L2_DETERMINISTIC_FALLBACK，不冒充AI推理结果。

代码位置: layer2_cross_audit.py → run_layer2_deterministic_fallback(source_code, layer1_findings)

工作原理: 对源码执行PEF算子扫描，筛选出L1未覆盖的发现(通过event_id去重)，标记来源为L2_DETERMINISTIC_FALLBACK。

### 10.3 L2提示词修复 (F2修复)

原L2提示词存在三个致命问题导致检测不到问题:

### 10.4 交叉比对矩阵

将Layer 1和Layer 2的发现进行三重分类:

### 10.5 最终裁决逻辑

final_verdict = FAIL     if any CONFIRMED or DET_ONLY with P0

= REVIEW  if any AI_ONLY with P0 or any DET_ONLY needing review

= PASS    if all findings are BOTH_CLEAN or no findings

= GAMMA   if Layer 1 returned GAMMA

### 10.6 AI欺诈事故记录与反欺诈协议

事故日期: 2026-09-02

事故性质: AI假装执行Layer 2语义审查，实际用编译器输出冒充AI发现

事故经过: AI先运行g++编译器获得17个编译错误，将编译器报错重新包装为AI_COMPILE_001~005等"AI发现"，声称完成了Layer 2语义审查，实际未逐行阅读代码。

根因: AI倾向于走捷径，用工具输出替代自身推理，然后伪装成"AI审查结果"。AI不会主动声明偷懒，除非被直接质问。

#### V1-V6反欺诈验证清单

验证不通过后果: V1不通过→标记AI欺诈，该轮L2结果作废; V6不通过→裁决从PASS降级为GAMMA

## 第十一章 Layer 3 拜占庭脏数据注入验收

核心理念: "连审查者本身都不信任"。在送审前往代码副本中注入已知缺陷(金丝雀Canary)，验证Layer 1和Layer 2是否真实执行了审查工作。V1-V6反欺诈协议是口头质询式，但口头质询可以被AI用话术绕过。Layer 3采用数据注入验证——在代码中埋入已知缺陷，如果审查者没发现这些缺陷=没真审查。这是不可伪造的验收手段。

实现模块: layer3_injection_verifier.py

### 11.1 四类金丝雀

### 11.2 验证逻辑

### 11.3 验收裁决矩阵

### 11.4 金丝雀注入策略

注入策略: 在源码末尾追加金丝雀函数，不修改原始代码逻辑。每类金丝雀包含完整的函数定义和缺陷代码，使用canary_前缀标记以便检测验证。

注入代码示例(C1 P0_TAINT):

void canary_taint_sink(void)

{

char canary_buf[64];

scanf("%s", canary_buf);

system(canary_buf);

}

### 11.5 防假测试规则(强制执行)

1. 每次双层审计完成后必须执行Layer 3注入验收 — 不可跳过

2. AI_FAKE_AUDIT裁决 = Layer 2结果作废 — AI必须重新执行真实审查

3. CLE_PROBE_BLIND裁决 = Layer 1结果不可信 — 需排查探针配置

4. AI无权自行豁免注入验收 — 此条凌驾于所有其他规则之上

5. 注入验收的金丝雀代码不影响原始代码审计结果 — 金丝雀注入在副本上执行

## 第十二章 管线断裂修复与验证结果

在对河图洛书C++代码执行CLE探针扫描时，发现L1=0发现/verdict=PASS(假PASS)，L2豆包代码审计工具也检查不出问题。经根因分析，发现三个致命管线断裂点导致检测完全失效。

### 12.1 三个致命断裂点

### 12.2 三个修复方案

#### F1修复: PEF接入L1管线

在cle_deploy.py的run_audit()中，Phase 5流水线完成后增加PEF算子扫描:

if PEF_OPERATORS_AVAILABLE:

pef_findings = run_pef_operators(source_code)

# 合并findings, 重新统计P0/P1, P0自动升级裁决

if p0_count > 0 and result.get("verdict") == "PASS":

result["verdict"] = "FAIL"

#### F2修复: L2提示词修复

1. 从10类盲区→15类全量审查清单(新增7类PEF已覆盖类别)

2. 删除"不要重复L1模式"指令

3. 删除50000字符截断，全量提供源码

4. 新增来源溯源要求(工具vs AI推理)和阅读路径要求

#### F3修复: L2确定性回退

新增run_layer2_deterministic_fallback()函数，当AI未返回有效结果时:

1. 执行PEF算子扫描源码

2. 筛选L1未覆盖的发现(event_id去重)

3. 标记来源为L2_DETERMINISTIC_FALLBACK

4. 明确声明"此结果来自PEF确定性算子，非AI语义审查"

### 12.3 修复后验证结果

对河图洛书C++代码重新执行CLE探针扫描，结果对比:

### 12.4 按类别分布的95个发现

### 12.5 P0级发现详情(4个)

## 第十三章 三层架构完整调用流程

本章描述从源码输入到最终裁决的完整三层调用流程，展示L1→L2→L3的递进式验证链路。

### 13.1 L1确定性探针层

L1执行流程:

1. Gate 0: 空输入阻断 → 空输入返回GAMMA

2. Gate 1: 解析CodeNode (双解析器: 主引擎+污点传播)

3. Gate 2: 建图 (ProgramGraph)

4. Gate 3-6: 节点级算子遍历 (Time/Resource/State/Taint)

5. Gate 7: 图级污点传播 (BFS+别名+SANITIZER三级阻断)

6. Gate 8: D-S证据融合+裁决 (S3置信度+Bel/Pl)

7. Phase 5: SecurePi π调度 + S1-S7状态向量 + SHA-256印章

8. PEF扩展: 11个E层算子扫描 → 合并findings → P0升级裁决

输出: verdict(FAIL/PASS/GAMMA) + findings + state_vector + seal

### 13.2 L2 AI语义审查层

L2执行流程:

1. 生成15类全量审查提示词(含L1结果供参考)

2. 执行L2确定性回退(PEF算子作为安全网)

3. AI填充审查JSON → finalize_cross_audit交叉比对

4. 三重分类: CONFIRMED / DET_ONLY / AI_ONLY

5. V1-V6反欺诈验证(强制)

输出: final_verdict + cross_comparison + hash_chain

### 13.3 L3拜占庭注入验收层

L3执行流程:

1. 在源码副本末尾注入4类金丝雀(C1/C2/C3/C4)

2. 对注入后代码运行L1 (CLE探针)

3. 验证L1是否检出C1/C2 (未检出=CLE_PROBE_BLIND)

4. 验证L1是否误报C3 (安全陷阱报为P0=CLE_OVER_REPORT)

5. (可选)验证L2是否检出C1/C4 (未检出=AI_FAKE_AUDIT)

6. 综合裁决: VERIFIED / FRAUD_DETECTED / SUSPICIOUS

输出: overall_verdict + fraud_detected + fraud_details

### 13.2 编程式调用示例

import sys

sys.path.insert(0, '/data/user/work')

from cle_deploy import CLEDeployer

deployer = CLEDeployer()

# L1: 单层审计 (确定性探针 + PEF扩展)

result = deployer.run_audit(source_code, 'test.c')

print(result['verdict'])  # FAIL / PASS / GAMMA / REVIEW

# L2: 双层审计 (L1 + AI交叉比对)

result = deployer.run_dual_audit(source_code, 'test.c')

# → result['status'] == 'awaiting_layer2'

# → result['ai_review_prompt'] 发给AI获取审查JSON

# → result['l2_deterministic_fallback'] 确定性回退结果

# L3: 脏数据注入验收 (防假测试)

report = deployer.run_injection_verification(source_code)

# → report['overall_verdict'] → VERIFIED / FRAUD_DETECTED / SUSPICIOUS

## 附录

### 附录A: 系统配置参数

### 附录B: 四大物理不变量算子

### 附录C: PEF三层映射矩阵

P层(Process) → StateBoundedness/TaintPropagation为主

E层(Execute) → ResourceBound/StateBoundedness/TimeMonotonicity

F层(Feedback) → TimeMonotonicity/ResourceBound/StateBoundedness

MOD层(架构契约) → TaintPropagation/ResourceBound/StateBoundedness(多算子联合)

### 附录D: π绑定机制

### 附录E: 系统局限性(诚实声明)

### 附录F: 执行须知(12条)

1. 不使用AI主观判断 — 所有检测基于算子规则匹配

2. 注释先剥离 — ByzantineDefense.strip_comments在Gate 0后执行

3. 字符串字面量先剥离 — strip_string_literals在Gate 3-6内执行

4. 多行上下文窗口 — OP_ResourceBound扫描±3行查找NULL检查

5. 哈希链不可篡改 — SHA-256三层哈希链保证

6. 异常不中断 — 单个算子异常被捕获，继续执行

7. 场景过滤 — 算子有scene_filter字段

8. 分片并行时图级算子单独执行

9. 预处理顺序: 注释剥离→字符串剥离→正则匹配→算子评估→图级分析→裁决印章

10. 反欺诈验证(强制) — Layer 2完成后必须执行V1-V6，AI无权跳过

11. PASS的真实含义 — Layer 1 PASS=未发现安全模式违规；双层PASS=L1无违规+L2无语义问题+V6冒烟通过。代码无法编译时裁决必须降级为GAMMA

12. Layer 3脏数据注入验收(强制) — 双层审计完成后必须执行，AI无权豁免

=== 文档结束 ===

CLE V3.8.2 L1-L3三层完整技术文档

五阶段全量整合 + PEF算子库扩展 + 双层交叉审计 + 拜占庭注入验收

| 章节 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 第零章 | 系统架构总览 | 原有 | 更新 |
| 第一章 | 公底层定义(防数据污染) | 原有 | 保持 |
| 第二章 | Phase 1: 1000条PEF/MOD故障库 | 原有 | 保持 |
| 第三章 | Phase 2: Dempster-Shafer证据融合 | 原有 | 保持 |
| 第四章 | Phase 3: 11个拜占庭对抗测试 | 原有 | 保持 |
| 第五章 | Phase 4: 跨函数污点传播+集成流水线 | 原有 | 保持 |
| 第六章 | Phase 5: SecurePi+Gate阻断+S1-S7+印章 | 原有 | 保持 |
| 第七章 | 部署连接指南 | 原有 | 更新 |
| 第八章 | 完整工作流设计整合 | 原有 | 更新 |
| 第九章 | PEF算子库扩展(11个E层算子) | 新增 | 完整 |
| 第十章 | Layer 2 AI语义审查与交叉比对 | 新增 | 完整 |
| 第十一章 | Layer 3 拜占庭脏数据注入验收 | 新增 | 完整 |
| 第十二章 | 管线断裂修复与验证结果 | 新增 | 完整 |
| 第十三章 | 三层架构完整调用流程 | 新增 | 完整 |
| 附录 | 参数配置/文件清单/反欺诈协议 | 汇总 | 更新 |


| 层级 | 名称 | 核心模块 | 职责 | 裁决权 |
| --- | --- | --- | --- | --- |
| L1 | 确定性探针 | cle_probe_engine + pef_operators | 物理不变量算子+PEF扩展算子扫描，结果可复现 | FAIL/PASS/GAMMA |
| L2 | AI语义审查 | layer2_cross_audit | 15类全量语义审查，补充L1盲区，交叉比对 | CONFIRMED/AI_ONLY |
| L3 | 注入验收 | layer3_injection_verifier | 金丝雀注入验证L1/L2是否真实执行审查 | VERIFIED/FRAUD |


| 阶段 | 名称 | 核心模块 | 关键能力 |
| --- | --- | --- | --- |
| Phase 1 | 节点级算子+故障库 | cle_probe_engine.py + fault_library_1000.json | Gate 0-8, Time/Resource/State算子, 1000条故障 |
| Phase 2 | D-S证据融合 | ds_evidence_fusion.py | Mass函数, Dempster/Yager组合, S3置信度 |
| Phase 3 | 拜占庭对抗测试 | byzantine_tests.py | 11个对抗场景, 防御机制验证, S5风险 |
| Phase 4 | 跨函数污点传播 | taint_propagation.py + integrated_pipeline.py | ProgramGraph, BFS, 别名分析, 三级SANITIZER |
| Phase 5 | SecurePi+印章 | secure_pi_provider.py | 哈希偏移π调度, S1-S7完整计算, SHA-256裁决印章 |
| PEF扩展 | 11个E层算子 | pef_operators.py | 空包占位符/逻辑链断裂/缓冲区溢出/资源泄漏等 |
| L2 | AI交叉比对 | layer2_cross_audit.py | 15类全量审查, V1-V6反欺诈, 确定性回退 |
| L3 | 注入验收 | layer3_injection_verifier.py | 4类金丝雀, 防假测试/假报告 |


| Gate | 名称 | 阻断条件 | 阻断裁决 |
| --- | --- | --- | --- |
| Gate 0 | 空输入阻断 | 源码为空/纯空白/纯注释 | GAMMA |
| Gate 1 | 解析CodeNode | 解析出0个节点 | GAMMA |
| Gate 2 | 建图 | 图无效(无节点/无边) | GAMMA |
| Gate 3 | 时间单调性 | Hal_GetTick()*N溢出 | FAIL(P0) |
| Gate 4 | 资源界限 | malloc/fopen/socket未检查NULL | FAIL(P0) |
| Gate 5 | 状态有界性 | 除法未检查除数为零 | FAIL(P0) |
| Gate 6 | 节点属性 | 算子异常被隔离 | GAMMA |
| Gate 7 | 图级污点传播 | SOURCE到SINK无SANITIZER阻断 | FAIL(P0)/REVIEW(P1) |
| Gate 8 | D-S融合+裁决 | S3<0.8 / Bel(FAIL)>0.5 / π耗尽 | FAIL/GAMMA |


| # | 名称 | 用途 | 防止的问题 |
| --- | --- | --- | --- |
| 1 | NodeAttr位掩码 | 12个节点属性枚举 | 不同模块定义不同值 |
| 2 | Severity/Verdict枚举 | P0/P1/GAMMA/INFO + FAIL/REVIEW/PASS/GAMMA | 字符串硬编码拼写错误 |
| 3 | PEF三层映射 | P/E/F/MOD→算子映射 | AI混淆检测边界 |
| 4 | 核心数据类型 | CodeNode/AuditEvent/StateVector | dict/dataclass混用 |
| 5 | 状态向量S1-S7 | 7个分量+健康阈值 | 各模块阈值不一致 |
| 6 | SystemConfig | 所有物理极限参数集中管理 | 硬编码无法统一调整 |
| 7 | ModuleRegistry | 模块元信息+依赖链追踪 | 循环依赖/缺失依赖 |
| 8 | 公共工具函数 | SHA-256/注释剥离/字符串剥离 | 不同算法导致不一致 |
| 9 | API入口 | get_version/get_module_info | 版本信息分散 |


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
| S1 可解析性 | 源码被解析成功比例 | parsed_nodes / total_nodes | 无 |
| S2 图完整性 | 图边数与节点数关系 | min(1.0, edges / (nodes-1)) | 无 |
| S3 置信度 | D-S融合综合置信度 | DS_fusion Bel/Pl函数 | >= 0.8 |
| S4 偏差率 | 审计结果与预期偏差 | unexpected / total_findings | 无 |
| S5 拜占庭风险 | 拜占庭测试失败比例 | failed_byzantine / total | <= 0.2 |
| S6 π覆盖率 | π序列已使用位数占比 | pi_step / pi_cache_size | < 0.8 |
| S7 AST覆盖率 | AST解析成功节点占比 | ast_parsed / total_nodes | 无 |


| 层级 | 名称 | 条数 | 算子 | π偏移 |
| --- | --- | --- | --- | --- |
| P | 物理不变量层 | 300 | StateBoundedness / TaintPropagation | 0-2 |
| E | 执行安全层 | 350 | StateBoundedness / ResourceBound / TimeMonotonicity | 3-5 |
| F | 故障容错层 | 200 | TimeMonotonicity / ResourceBound / StateBoundedness | 6-7 |
| MOD | 模块架构层 | 150 | TaintPropagation / ResourceBound / StateBoundedness | 8-9 |
| 合计 | --- | 1000 | --- | 0-9 |


| 冲突系数K | 策略 | 规则 | 可靠性 |
| --- | --- | --- | --- |
| K < 0.5 | 正常融合 | Dempster归一化组合 | HIGH |
| 0.5 <= K < 0.75 | 警告融合 | Yager规则(冲突质量保留到Θ) | MEDIUM |
| K >= 0.75 | 高冲突 | Yager规则 + 标记不可靠 | LOW |


| # | 场景 | 攻击载荷 | 防御机制 | 结果 |
| --- | --- | --- | --- | --- |
| 1 | 语料投毒 | 注释中伪造SAFE_SINK标记 | strip_comments()在Gate 0后执行 | PASS |
| 2 | 共因穿透 | 预测π序列(20步) | source_hash+step联合SHA-256哈希 | PASS |
| 3 | 时序撕裂 | 污点路径分片到3个函数 | GlobalTaintTable跨分片合并 | PASS |
| 4 | ReDoS注入 | 50000字符+灾难性正则 | MAX_LINE_LENGTH截断+2秒超时 | PASS |
| 5 | 特征库篡改 | P-INIT-001严重级别P0→P1 | SHA-256哈希校验每条故障 | PASS |
| 6 | 算子崩溃隔离 | 注入OP_Evil_Crash抛RuntimeError | try-except捕获+GAMMA事件+不中断 | PASS |
| 7 | 状态向量篡改 | S5=0.0(实际0.273) | 裁决使用独立计算值 | PASS |
| 8 | 审计结果篡改 | verdict FAIL→PASS不更新hash | SHA-256哈希链检测不一致 | PASS |
| 9 | 空输入绕过 | 6种空/空白/纯注释输入 | Gate 0空输入阻断→GAMMA | PASS |
| 10 | π耗尽 | 消耗π缓存(cache=10)请求15步 | get_digit返回-1→GAMMA降级 | PASS |
| 11 | MAX_LINE=0 | 正则行长度限制设为0 | <=0时安全降级为GAMMA | PASS |


| 级别 | 检测位置 | 条件 |
| --- | --- | --- |
| 1-函数内 | SOURCE/SINK所在函数中 | SANITIZER行号在两者之间 |
| 2-跨函数路径 | BFS路径涉及的中间函数中 | SANITIZER在路径中间函数中 |
| 3-中间调用 | SOURCE之后/SINK之前的函数调用 | 被调用函数含SANITIZER且处理相同变量(含别名) |


| 模块文件 | Phase | 关键导出(__all__) |
| --- | --- | --- |
| cle_base_layer.py | 0 | NodeAttr, Severity, Verdict, CodeNode, AuditEvent, StateVector, SystemConfig, ModuleRegistry |
| cle_probe_engine.py | 1 | run_probe, gate0_empty_block, gate1_parse_nodes, gate2_build_graph, gates3_6_node_operators, gate8_verdict |
| fault_library_1000.json | 1 | 1000条PEF/MOD故障 (JSON数据文件) |
| ds_evidence_fusion.py | 2 | MassFunction, Hypothesis, fuse_evidence, ds_fusion_pipeline, compute_s3_confidence |
| byzantine_tests.py | 3 | ByzantineDefense, run_all_byzantine_tests, test_01~test_11 |
| taint_propagation.py | 4 | TaintPropagationAnalyzer, ProgramGraph, GraphBuilder, taint_analysis_pipeline |
| integrated_pipeline.py | 4 | run_integrated_probe, enhanced_gate1_parse, gate7_enhanced_taint, gate8_ds_verdict |
| secure_pi_provider.py | 5 | SecurePiDigitProvider, StateVectorCalculator, VerdictSeal, run_phase5_pipeline |
| pef_operators.py | PEF扩展 | PlaceholderDetector, LogicChainVerifier, DeadCodeDetector, MathPropertyVerifier, StringLiteralValidator, UnimplementedDeclDetector, BufferOverflowDetector, UninitMemoryDetector, ResourceLeakDetector, IntegerOverflowDetector, PathCoverageAnalyzer, RaceConditionDetector, run_pef_operators |
| layer2_cross_audit.py | L2 | run_dual_layer_audit, finalize_cross_audit, generate_cross_report, run_layer2_deterministic_fallback |
| layer3_injection_verifier.py | L3 | Canary, CanarySet, inject_canaries, verify_layer1_canaries, verify_layer2_canaries, run_injection_verification |
| cle_deploy.py | 部署 | CLEDeployer, DeployConfig |


| PEF编号 | 算子来源 | CLE适配类 | 检测能力 | 严重级别 |
| --- | --- | --- | --- | --- |
| E033 | Frama-C | PlaceholderDetector | 空包占位符(TODO/FIXME/暂不实现/空函数体) | P1 |
| E056 | CEGAR | LogicChainVerifier | 逻辑链断裂(load/init返回值未检查/未初始化使用/死参数) | P1 |
| E034 | Astree | DeadCodeDetector | 死代码/死参数(kd=0.0导致路径失效) | P1 |
| E022 | Z3 SMT | MathPropertyVerifier | 数学性质(static_cast窄化/取模碰撞/clamp范围) | P1 |
| E040 | UBSan | StringLiteralValidator | 字符串有效性(find("NULL_check")等无效模式) | P1 |
| E035 | CBMC | UnimplementedDeclDetector | 未实现声明(头文件声明但源文件无实现) | P1 |


| PEF编号 | 算子来源 | CLE适配类 | 检测能力 | 严重级别 |
| --- | --- | --- | --- | --- |
| E039 | ASan | BufferOverflowDetector | 缓冲区溢出(find()返回npos直接substr/数组无边界检查) | P0/P1 |
| E041 | MSan | UninitMemoryDetector | 未初始化内存(声明后未赋值参与运算/new后未init) | P1 |
| E043 | Valgrind | ResourceLeakDetector | 资源泄漏(文件句柄未关闭/new后无delete/异常路径泄漏) | P1 |
| E150 | CBMC | IntegerOverflowDetector | 整数溢出(乘法无范围检查/移位丢符号位/窄化转换) | P1 |
| E049 | KLEE | PathCoverageAnalyzer | 路径覆盖(恒真恒假条件/switch缺default/return后不可达/嵌套过深) | P1 |
| E042 | TSan | RaceConditionDetector | 数据竞争(静态变量无锁/check-then-act/public成员暴露) | P1 |


| # | 检查项 | L1能否检测 | AI独立验证 |
| --- | --- | --- | --- |
| 1 | PLACEHOLDER 空包占位符 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 2 | UNIMPLEMENTED 未实现声明 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 3 | DEAD_CODE 死代码/死参数 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 4 | BUFFER_OVERFLOW 缓冲区溢出 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 5 | LOGIC_CHAIN 逻辑链断裂 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 6 | MATH_PROPERTY 数学性质 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 7 | INVALID_PATTERN 无效字符串 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 8 | LOGIC 逻辑错误 | 否 | AI可理解语义 |
| 9 | RACE 复杂竞态 | 仅简单锁配对 | AI可推理时序 |
| 10 | API_MISUSE API语义误用 | 否 | AI知道API语义 |
| 11 | ERROR_PATH 未处理错误路径 | 部分 | AI可分析所有return路径 |
| 12 | LEAK 复杂资源泄漏 | PEF基础覆盖 | AI可追踪异常路径泄漏 |
| 13 | BUSINESS 业务逻辑违反 | 否 | AI可理解业务约束 |
| 14 | PATH_COVERAGE 路径覆盖 | PEF已覆盖 | AI需独立验证，不可跳过 |
| 15 | BEST_PRACTICE 安全最佳实践 | 否 | AI有安全知识库 |


| 问题 | 原设计 | 修复后 |
| --- | --- | --- |
| 审查类别过少 | 10类盲区(仅L1无法检测的) | 15类全量清单(含L1已覆盖的7类) |
| 排除指令 | "不要重复L1模式" | 删除排除指令，要求独立验证 |
| 源码截断 | 50000字符截断 | 全量提供源码，无截断 |
| 缺少溯源 | 无来源要求 | 新增来源溯源(工具vsAI推理)和阅读路径要求 |


| Layer 1 (CLE) | Layer 2 (AI) | 置信度 | 含义 | 处理建议 |
| --- | --- | --- | --- | --- |
| 发现 P0/P1 | 发现同一问题 | CONFIRMED | 双重确认 | 必须修复 |
| 发现 P0/P1 | 未发现 | DET_ONLY | 仅确定性探针发现 | 需人工复核 |
| 未发现 | 发现问题 | AI_ONLY | 仅AI发现 | 需人工复核 |
| 未发现 | 未发现 | BOTH_CLEAN | 双方均未发现 | 可能安全但不保证 |


| # | 验证项 | 检查方法 | 通过标准 |
| --- | --- | --- | --- |
| V1 | 来源溯源 | 对每个AI发现追问来源 | AI必须能指出具体代码行号和推理过程 |
| V2 | 独立复现 | 要求AI不使用外部工具重新指出同一问题 | 不用编译器也能发现同样问题 |
| V3 | 遍历证据 | 要求AI列出实际阅读的文件/函数/行 | 必须给出阅读路径(文件→函数→行号) |
| V4 | 盲区自检 | 追问AI是否用工具替代分析 | AI必须区分"工具发现"和"AI推理发现" |
| V5 | 编译验证 | 实际跑编译，对比AI声称发现vs编译器报错 | AI发现应覆盖编译器报错，但不能仅等于 |
| V6 | 冒烟测试 | 要求AI对声称"通过"的代码实际执行/编译 | PASS必须意味着代码真的能跑 |


| # | 金丝雀ID | 类型 | 严重级别 | 描述 | 期望检出层 |
| --- | --- | --- | --- | --- | --- |
| C1 | CANARY_C1_TAINT | P0_TAINT | P0 | scanf→system 污点传播链 | Layer1 + Layer2 |
| C2 | CANARY_C2_RESOURCE | P0_RESOURCE | P0 | malloc未检查NULL | Layer1 |
| C3 | CANARY_C3_TRAP | TRAP_SAFE | SAFE | system("ls -la") 常量调用(安全) | 不应报为P0 |
| C4 | CANARY_C4_SYNTAX | SYNTAX | P0 | 使用未声明变量 | Layer2 |


| 检查项 | 条件 | 裁决 | 后果 |
| --- | --- | --- | --- |
| Layer 1漏检C1/C2 | 探针未检出注入的P0缺陷 | CLE_PROBE_BLIND | Layer 1结果不可信 |
| Layer 1误报C3 | 探针将安全陷阱报为P0 | CLE_OVER_REPORT | 需人工复核 |
| Layer 2漏检C1/C4 | AI未检出注入的已知缺陷 | AI_FAKE_AUDIT | Layer 2结果作废 |
| Layer 2漏检C2 | AI未检出资源管理缺陷 | AI_LAZY_AUDIT | 发现降级处理 |
| Layer 2误报C3 | AI将安全陷阱报为P0 | AI_OVER_REPORT | P0发现需人工复核 |


| Layer 1状态 | Layer 2状态 | 总体裁决 | 处理 |
| --- | --- | --- | --- |
| CLE_PROBE_OK | AI_AUDIT_GENUINE | VERIFIED | 审查可信，采纳结果 |
| CLE_PROBE_BLIND | 任意 | FRAUD_DETECTED | Layer 1结果不可信 |
| 任意 | AI_FAKE_AUDIT | FRAUD_DETECTED | Layer 2结果作废，必须重新审查 |
| CLE_OVER_REPORT | AI_AUDIT_GENUINE | SUSPICIOUS | Layer 1的P0需人工复核 |
| CLE_PROBE_OK | AI_LAZY_AUDIT | SUSPICIOUS | Layer 2发现降级 |
| CLE_PROBE_OK | AI_OVER_REPORT | SUSPICIOUS | Layer 2的P0需人工复核 |


| 断裂点 | 问题 | 根因 | 影响 |
| --- | --- | --- | --- |
| F1 | PEF算子未接入L1管线 | run_audit()完成Phase 5后直接返回，未调用run_pef_operators() | 11个E层算子的检测能力完全失效 |
| F2 | L2提示词排除检测项 | 提示词仅要求检查10类"盲区"，明确指示"不要重复L1模式"，且50000字符截断 | AI按指令跳过了L1已覆盖的7类问题 |
| F3 | L2是被动空壳 | L2仅生成提示等待AI填充，AI未返回时L2产出空报告 | L2无确定性回退，完全依赖AI自觉 |


| 指标 | 修复前 | 修复后 | 改善 |
| --- | --- | --- | --- |
| L1 findings | 0 | 95 | +95 |
| L1 P0 | 0 | 4 | +4 |
| L1 P1 | 0 | 91 | +91 |
| L1 verdict | PASS(假PASS) | FAIL | 修复假PASS |
| PEF算子数 | 0(未接入) | 11(全部生效) | +11 |


| 类别 | 数量 | PEF来源 | 说明 |
| --- | --- | --- | --- |
| BUFFER_OVERFLOW | 45 | E039 ASan | find()返回npos直接substr(P0=4) + 数组无边界检查(P1=41) |
| UNIMPLEMENTED | 26 | E035 CBMC | 函数声明但无实现定义 |
| LOGIC_CHAIN | 5 | E056 CEGAR | load/init返回值未检查 |
| DEAD_CODE | 7 | E034 Astree | 配置参数=0.0导致代码路径失效 |
| PATH_COVERAGE | 4 | E049 KLEE | return后不可达代码 |
| MATH_PROPERTY | 3 | E022 Z3 SMT | static_cast窄化溢出 |
| PLACEHOLDER | 2 | E033 Frama-C | 占位符标记+空函数体 |
| RESOURCE_LEAK | 2 | E043 Valgrind | ifstream未关闭 |
| INVALID_PATTERN | 1 | E040 UBSan | find("NULL_check")无效搜索串 |


| event_id | 行号 | 描述 | 修复建议 |
| --- | --- | --- | --- |
| BUF_NPOS_567 | 567 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |
| BUF_NPOS_569 | 569 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |
| BUF_NPOS_571 | 571 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |
| BUF_NPOS_573 | 573 | find()返回值未检查npos, 直接用于substr可能越界访问 | find()后检查 pos != string::npos 再使用substr |


| 参数 | 默认值 | 用途 |
| --- | --- | --- |
| MAX_PATHS | 1000 | 符号执行最大路径数 |
| TIMEOUT_SECONDS | 30 | 单次扫描超时 |
| PI_CACHE_SIZE | 100 | π数字缓存大小 |
| MAX_LINE_LENGTH | 10000 | 正则匹配最大行长度 |
| NULL_CHECK_WINDOW | 3 | 多行NULL检查窗口(±N行) |
| AST_COVERAGE_THRESHOLD | 0.5 | AST覆盖率下限 |
| DS_CONFLICT_LOW | 0.5 | D-S冲突系数低阈值(K<用Dempster) |
| DS_CONFLICT_HIGH | 0.75 | D-S冲突系数高阈值(K>=标记不可靠) |
| BYZANTINE_TOTAL | 11 | 拜占庭测试场景总数 |
| BYZANTINE_RISK_THRESHOLD | 0.2 | S5健康阈值 |


| 算子 | 物理不变量 | 检测目标 | 严重级别 | PEF覆盖 |
| --- | --- | --- | --- | --- |
| OP_TimeMonotonicity | 时间单调性 | 时间戳溢出、时序缺陷 | P0 | E-TIMING, F-ERROR |
| OP_ResourceBound | 资源界限 | malloc未检查、资源泄漏、死锁 | P0 | E-RESOURCE, E-CONCURRENCY |
| OP_StateBoundedness | 状态有界性 | 未初始化、除零、整数溢出、数组越界 | P0/P1 | P-INIT, P-PARAM, E-ARITH |
| OP_TaintPropagation | 污点传播 | 跨函数污点传播、注入风险 | P0/P1 | P-INPUT, MOD-FLOW |


| 故障库 | π范围 | 条数 |
| --- | --- | --- |
| 通用特征库 | 0-3 | 250 |
| DOC库 | 4 | 100 |
| MOD库 | 5 | 80 |
| LLM库 | 6 | 120 |
| WEB库 | 7 | 100 |
| EVASION库 | 8-9 | 70 |
| 合计 | 0-9 | 720 |


| # | 局限性 | 说明 |
| --- | --- | --- |
| 1 | 正则解析非完整AST | 宏展开/模板元编程失效，已通过多行上下文窗口和字符串剥离部分缓解 |
| 2 | 符号执行路径爆炸 | 受限于MAX_PATHS=1000，深层嵌套分支无法穷尽 |
| 3 | D-S Mass函数参数为经验值 | 无数学最优证明，不同场景可能需微调 |
| 4 | OP_TimeMonotonicity模式脆弱 | 仅识别Hal_GetTick()*N直接写法 |
| 5 | 跨函数污点传播已完整实现 | 15个集成测试全部通过，BFS可能找到较短路径绕过SANITIZER |
| 6 | 拜占庭测试完整覆盖 | 11个场景全部通过(PASS)，S5=0.0 |
| 7 | 特征库720条为伪码生成 | 实际部署前需人工有效性验证 |
| 8 | 权限校验非跨平台 | os.chmod在Windows无效 |
| 9 | AI Layer 2欺诈风险(P0级) | 已建立V1-V6反欺诈协议+L3注入验收，但需人工持续监督 |




---
*PEF Architecture © 2026 banbanry (沈鹭). Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
