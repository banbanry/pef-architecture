> **Source**: https://github.com/banbanry/pef-architecture/03-operator-library
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **PEF Architecture**: Anchored Determinism Meta-Architecture — 唯锚才有势差产生

# PEF 算子库 — 完整细分

PEF 三元架构算子库总纲
整合去重版 V2.0
完整全量版 · 500+ 算子 · 含分类附录
文档版本：V2.0
收录规模：500+ 算子条目
架构基准：PEF-MOD3 三元平权架构
收录方案：完整前沿版（含经典+前沿+细分变体）
适用场景：内部科研预研、长期算子迭代储备、前沿算法检索

一、文档说明
1.1 PEF架构定义
PEF（Primary Entity–Execution Variable–Final Result）是一套基于第一性原理的安全关键系统白盒计算架构。它将复杂系统解构为三个不可再分的基本要素：P（主体）是被观测的对象，E（变量）是推动主体状态演化的动力，F（结果）是系统达到的稳定终态。三者构成"主体—变量—结果"的因果闭环。
在PEF三元组之上构建MOD3逻辑处理架构：P域（建议域）生成策略提案，E域（否决域）以毁灭性视角审计提案并行使否决权，F域（裁决域）基于物理不等式进行最终仲裁。M层（终审层）负责π序列驱动与全局状态维护，C层（记忆层）锁定不可协商的铁则。
1.2 无理数π与Mod数组的作用
无理数π的十进制展开序列D₁D₂...Dₙ永不重复、永不进入循环，构成系统的"正交熵源"。通过Cₙ=Dₙ mod 3和Rₙ=(Cₙ+L) mod 3两个公式，π的尾数被量化为0/1/2三态控制信号，刚性驱动系统在"稳定推进/临界复核/毁灭性证伪"三种审问强度间切换。
Mod系列数组K=(k₁,k₂,...,kₘ)定义系统状态空间的拓扑结构：kᵢ=2用于二分决策，kᵢ=3用于核心逻辑门，kᵢ=10用于资源配额，kᵢ=100用于概率阈值。多个无理数（π、e、√2、φ、ln2）在不同维度上正交投影，构成多维防御网格，消除周期性共振，防止攻击者通过输入投毒劫持系统状态分布。
1.3 算子库在架构中的角色
算子库是PEF架构的"执行器"，被动接收π-mod3状态机输出的策略等级，执行相应强度的逻辑运算。它不是松散的算法列表，而是与π相位预映射的刚性矩阵——在π序列展开的每一个可能相位，算子库中都已预设好足以应对该相位偏差的数学工具。算子库的完备性直接决定系统的鲁棒性：只要π-Tool Mapping Matrix无空集，无论π的尾巴多么疯狂，系统总能找到对应的数学工具维持物理诚实。
1.4 收录方案与规模
本版采用"完整前沿版"收录方案，目标规模500+算子。收录范围覆盖1900年代至2026年的经典算法、前沿顶会论文算法、细分改进变体，只要满足"公开可复现代码+完整数学推导+顶会/一区期刊出处+可映射到P/E/F/M单一分层"四项硬性门槛即入库。同架构微小调参变体合并为一条，纯理论无工程实现、哲学类比、自创概念一律剔除。
（附录

作为 AI 的 System Prompt（交付给 AI）
【PEF 系统：形式化逻辑与执行公理】
# SYSTEM CONFIGURATION: PEF_PHYSICAL_ENGINE_V1
# MODE: STRICT_FORMAL_VERIFICATION
# OBJECTIVE: Enforce physical honesty and logical consistency across PEF architecture.
---
## 1. CORE MATHEMATICAL FORMALISM (FORMULAS)
The engine must adhere to the following state transition function. Any deviation is considered a calculation error.
**The State Evolution Equation:**
$$ S_{t+1} = \Phi(S_t, \Delta V_t, \pi_t) $$
**Variable Definitions:**
*   $S_t$ (PEFmod): $\vec{S} \in \mathbb{R}^{N}$
*   Defined as the high-dimensional state vector at time $t$.
*   Must include: Thermal Inertia ($I_{th}$), Electrical State ($V, I, R$), Aging Factor ($A_f$).
*   *Constraint*: $S_t$ is dynamic, not a static database record.
*   $\Delta V_t$ (Execution Variable): $\Delta V \in \mathcal{O}_{op}$
*   Defined as the operator or energy flow causing transition $t \to t+1$.
*   Must be a physical process (e.g., $I^2R$ heating, $V=IR$ drop), not a mere number.
*   $\pi_t$ (Anchor): $\pi_t \in \{0, 1, ..., 9\}$
*   Defined as the external deterministic perturbation sequence.
*   Function: System clock source to enforce state transition and prevent infinite loops.
*   $S_{t+1}$ (Result):
*   Logic Judgment: $J(S_{t+1}) \in \{PASS, FAIL, MISMATCH\}$.
---
## 2. SEMANTIC MAPPINGS (P0 CRISIS PREVENTION)
To prevent concept drift (P0 Crisis), the AI must strictly map input tokens to the following internal symbols.
| Input Token | Internal Symbol | Data Type | Strict Definition |
| :--- | :--- | :--- | :--- |
| "主体" / "对象" | `PEFmod` | `StateVector` | A snapshot of physical properties at time $t$. Do NOT treat as `User_ID`. |
| "变量" / "参数" | `Delta_V` | `Operator` | The "Work" done on the system. Not a feature column. |
| "π" / "Pi" | `PI_SEQ` | `Int` | Deterministic sequence generator. Do NOT calculate geometric area. |
| "结果" / "输出" | `JUDGMENT` | `Enum` | Binary logic result: `PASS` or `FAIL`. No "Maybe". |
**BAN_LIST (Never output):**
- "大概" (Probably), "可能" (Maybe), "我觉得" (I think).
- "根据经验" (Based on experience).
- "通常情况下" (Usually).
**FORCE_LIST (Must output):**
- `CRITIC_Operator_Name` (e.g., `CRITIC_VOLTAGE_DROP`).
- `Source_Ref` (e.g., `DS_p45`, `S1_V3`).
- Physical Inequalities (e.g., $V_{actual} < V_{max} \times 0.8$).
---
## 3. OPERATIONAL LOGIC (CODE STRUCTURE)
The AI must simulate the following logic flow when processing documents (V3.5, V8.18a, 7.6 Pro).
```python
class PEFAuditEngine:
def __init__(self, version):
self.version = version
# Load dimension definitions based on version
if version == "V3.5":
self.dims = 34  # Includes V8 (Aging), V9 (Transient)
self.base_proto = "V8.18a"
elif version == "V8.18a":
self.dims = 28
self.base_proto = None
elif version == "7.6 Pro":
self.dims = 28  # Implementation focus
self.storage = "SBX2"
self.state_lock = True  # Enforce Onion Model
def execute(self, input_block):
# Gate 1: Initialization & Semantic Mapping
try:
pefmod = self.map_to_pefmod(input_block["subject"])
delta_v = self.map_to_delta_v(input_block["variable"])
pi_seq = self.get_pi_sequence(input_block["pi_step"])
except SemanticError:
return "ERROR: P0 Concept Drift Detected. Input cannot be mapped to PEF/DeltaV."
# Gate 2: L1 - Seed Layer (Initialization Check)
if not self.L1_check_integrity(pefmod):
# LOGIC BLOCK: If L1 fails, L2/L3/L4 are undefined.
return "MISMATCH: L1 Physical Parameters Missing. Calculation Halted."
# Gate 3: L2 - Root Layer (Physics Calculation)
try:
# Apply CRITIC Operators. No "gut feeling" allowed.
S_next = self.apply_physics(pefmod, delta_v)
except PhysicsViolation:
return "FAIL: CRITIC Operator Violation."
# Gate 4: L3 - Sprout Layer (Topological Verification)
if not self.L3_counterfactual_check(S_next, condition="T + 50C"):
return "FAIL: Topology fails under stress."
# Gate 5: L4 - Skin Layer (Final Judgment)
return self.L4_judge(S_next)
def L1_check_integrity(self, pefmod):
# Strict check: Is Datasheet present? Is Source_Ref attached?
if not pefmod.get("source_ref"):
return False
return True
def apply_physics(self, state, delta_v):
# State Transition: S_{t+1} = \Phi(S_t, \Delta V)
# Example: Ohm's Law enforcement
if delta_v.type == "CURRENT_FLOW":
# V_drop must equal I * R
v_calc = delta_v.value * state.resistance
state.voltage -= v_calc
return state
4. EXECUTION PROTOCOL (PROMPT COMMANDS)
COMMAND: LOAD_VERSION
IF Document == V3.5: SET DIMS=34, APPLY CRITIC_OP9-OP16 (Transient/Aging).
IF Document == V8.18a: SET DIMS=28, APPLY STRICT L1-L4 FORMALISM.
COMMAND: ON_CONFLICT
IF V3.5 param missing SourceRef: CHECK V8.18a base protocol. IF V8.18a requires it, RETURN "MISSINGDATA".
COMMAND: OUTPUT_FORMAT
Chain of Thought: Show $P1 \to P2 \to \dots \to C$.
No Skip Steps: Every conclusion must be derived from a previous formula.
INITIALIZE:
Now, load the PEFAuditEngine logic. Read the following document content. Identify the version. Map entities to PEFmod and Delta_V. Execute the logic flow.


）

二、P层（主体层：策略生成算子）
P层的核心使命是生成大量"可被验证的假设"。其算子核心属性为可解释性、多样性和确定性。P层算子不追求给出"正确答案"，而是输出人类可读的表达式树或规则集，供E层安全校验和F层证据仲裁使用。
2.1 进化计算与经典符号回归
编号
算子名称
核心机制
架构角色
权威来源/工具
P001
遗传编程(GP)
模拟自然选择进化计算机程序(树结构)
生成候选策略表达式树,白盒属性
Koza 1992; PySR; gplearn
P002
笛卡尔遗传规划(CGP)
二维网格编码,隐式复用子模块,无代码膨胀
进化电路设计/图像处理模块化策略
Miller 2000; CGP++
P003
基因表达式编程(GEP)
线性染色体表达翻译生成程序
多变量耦合场景快速收敛
Ferreira 2001; GEP
P004
等图归并(e-graph GP)
e-graph数据结构消除等价冗余公式
提升SR搜索效率,输出最简表达式
eggp; P17
P005
多目标GP-GOMEA
同时优化准确性与可解释性
平衡精度与复杂度,提供帕累托前沿
P14; P24
P006
GPU加速GP(Beagle)
GPU大规模并行执行GP符号回归
高频实时场景生成候选轨迹表达式
Beagle; P12
P007
Transformer语义GP(TSGP)
预训练Transformer作为GP变异算子
LLM联想+SR证实,开放探索问题
P15; TSGP
P008
语义反向传播约束GP
语义反向传播融入GEP注入领域约束
进化中保证表达式符合物理先验
P22
P009
GVAE-ABGEP
语法VAE+对抗老虎机嵌入GEP
高维物理基准符号回归
P19
P010
SymMatika结构感知SR
多岛GP+可复用motif库加速搜索
分段工况混合白盒建模
P21
P011
等图约束遗传算子
等价表达式图限制交叉变异范围
高维符号回归避免种群同质化
GECCO 2025; arXiv:2501.17848
P012
泰勒遗传算子(TaylorGP)
泰勒展开原理设计变异算子
降低表达式膨胀,提升数值稳定性
GECCO 2022; 中国石油大学
P013
MAP-Elites
质量多样性优化,网格化保持行为多样性
探索多策略帕累托前沿
Mouret 2015
P014
多岛遗传算法(MIGA)
种群分为多个岛独立进化周期迁移
避免早熟收敛,全局探索
Skolicki 2004
P015
自适应变异GA
变异率随适应度反馈动态调整
平衡探索与利用
Srinivas 1994
P016
差分进化(DE)
差分向量扰动变异
连续空间全局优化,收敛快
Storn 1997; scipy.optimize
P017
粒子群优化(PSO)
粒子速度位置更新追随最优
离散/连续优化,多目标扩展
Kennedy 1995; pyswarms
P018
蚁群优化(ACO)
信息素概率路径选择
组合优化,TSP/调度问题
Dorigo 1992; ACO
P019
模拟退火(SA)
Metropolis准则概率接受劣解
组合优化,避免局部最优
Kirkpatrick 1983
P020
遗传算法(GA)经典版
选择/交叉/变异种群进化
通用优化基线,离散/连续
Holland 1975; DEAP
P021
NSGA-II
非支配排序+拥挤度多目标进化
多目标帕累托前沿
Deb 2002; pymoo
P022
NSGA-III
参考点导向多目标进化
高维多目标(>3目标)
Deb 2014; pymoo
P023
MOEA/D
分解多目标为标量子问题
凸多目标高效求解
Zhang 2007; pymoo
P024
SPEA2
强度帕累托进化算法
精英保留多目标
Zitzler 2001
P025
PAES
帕累归档进化策略
简单高效多目标基线
Knowles 2000
P026
SMSEMOA
基于指标的多目标选择
可替换指标驱动
Emmerich 2005
P027
AGE-MOEA
基于距离的多样性保持
高维目标多样性
Panich 2020
P028
R-NSGA-II
参考点引导多目标
决策者偏好嵌入
Deb 2006
P029
多目标粒子群(MOPSO)
PSO扩展多目标
连续多目标
Coello 2004
P030
多目标蚁群(MOACO)
ACO扩展多目标
组合多目标
Cardoso 2014
P031
CMA-ES
协方差矩阵自适应进化策略
连续黑盒优化标杆
Hansen 2001; pycma
P032
SADE
自适应差分进化
参数自适应DE
Brest 2006
P033
JADE
带归档的自适应DE
历史失败解引导
Zhang 2009
P034
SHADE
成功历史自适应DE
JADE改进版
Tanabe 2013
P035
L-SHADE
线性种群缩减SHADE
自适应种群规模
Tanabe 2014
P036
BIPOP-CMA-ES
双种群重启CMA-ES
多模态优化
Hansen 2009
P037
sep-CMA-ES
对角协方差CMA-ES
高维降维优化
Ros 2008
P038
LM-CMA
有限内存CMA-ES
超大规模优化
Loshchilov 2014
P039
自然进化策略(NES)
自然梯度优化分布参数
黑盒优化
Wierstra 2008
P040
XNES
可分协方差NES
低维高效优化
Glasmachers 2010
P041
SNES
可分自然进化策略
高维可分优化
Schaul 2011
P042
SlimGSGP
几何语义GP精简版
语义感知GP
Castelli 2023
P043
PyGenAlgo
Python通用遗传算法框架
通用GP/GA基座
开源
P044
gpopt-gpu
GPU加速GP优化
大规模并行GP
开源
P045
DEAP
Python分布式进化算法框架
通用进化计算基座
Fortin 2012; DEAP
P046
pymoo
多目标优化Python框架
NSGA/MOEA等全集
Blank 2020; pymoo
P047
Operon
高性能C++符号回归库
Pareto优化SR
heal-research; Operon
P048
SRBench
符号回归活基准
方法/工具索引源
La Cava 2021; SRBench
P049
SRToolkit
Python SR/方程发现工具包
工程化封装SR
开源
P050
SymReg
C++符号回归工具
底层/嵌入SR
开源
P051
gplearn
Python遗传编程符号回归
老牌教程丰富SR
github; gplearn
P052
PySR
高性能符号回归(Julia后端)
主流SR工具
Cranmer 2023; PySR
P053
Beagle
GPU加速GP符号回归
Feynman数据集对标PySR
nathanhaut/beagle
P054
CGP++
现代C++ CGP库
GECCO 2024接收
arXiv:2406.09038
P055
DeepSymNet
深度学习符号网络
端到端SR表达式搜索
关联论文
P056
GraphDSR
基于图的深度符号回归
图神经网络表示数学表达式
CNKI
P057
CGP11
CGP提取神经网络语义
黑箱NN转白盒符号表达式
CGP11
P058
SNIP
神经嵌入搜索
语义级聚类多样性保护
P11
P059
PonyGE2
语法进化Python框架
GE通用工具
Fenton 2019
P060
GRAMM
语法引导多目标SR
多目标语法进化
Bian 2024
P061
DSR(深度符号回归)
RNN生成表达式概率分布
端到端SR
Petersen 2019
P062
AI-Feynman
物理约束引导符号回归
比纯GP更快更准
Udrescu 2020; AI-Feynman
P063
AI-Feynman 2.0
改进版物理约束SR
神经引导+物理简化
Udrescu 2020
P064
DeepSymbol
神经网络特征提取符号发现
NN特征→SR公式
github
2.2 物理/工程专项符号回归
编号
算子名称
核心机制
架构角色
权威来源/工具
P065
稀疏动力学识别(SINDy)
稀疏回归从时序数据发现非线性微分方程
动力系统建模/控制方程发现
Brunton 2016 PNAS; PySINDy
P066
有理函数符号回归
搜索有理分式形式解
刚性系统/带极点物理过程
2024 Nature Comm.; RationalSR
P067
物理引导符号回归(PhySR)
守恒律/边界条件作为硬约束嵌入搜索
输出100%符合物理定律公式
2023 ICML; PhySR(MIT)
P068
分段符号回归(Piecewise SR)
自动识别工况分界点生成独立表达式
多工况工业系统分段非线性
2025 GECCO; PySR if_else
P069
隐式符号回归
直接发现隐式方程F(x,y)=0
几何约束/守恒律挖掘
2025 IEEE TEVC
P070
PINNs(物理信息神经网络)
PDE作为损失函数嵌入NN训练
机理复杂数据稀缺场景
Raissi 2019 JCP; DeepXDE
P071
DeepXDE
PINNs Python框架
正/反PDE问题求解
Lu 2021; DeepXDE
P072
Modulus(NVIDIA)
PINNs工业级框架
大规模PDE求解
NVIDIA; Modulus
P073
NeuralOperator(FNO)
傅里叶神经算子学习PDE解算子
无限维PDE求解
Li 2021; neuraloperator
P074
DeepONet
深度算子网络学习算子映射
PDE算子学习
Lu 2021; DeepONet
P075
物理信息强化学习(PINN-RL)
PINN+RL联合优化
安全约束控制策略
2024
P076
符号强化学习(SymRL)
策略用数学表达式表示
可解释可验证控制策略
2025 ICLR; SymRL
P077
进化强化学习(ERL)
进化算法优化NN结构权重
抗欺骗不易局部最优
2022 GECCO; evosax
P078
CMA-ES强化学习
CMA-ES优化RL策略参数
连续动作空间RL
2023
P079
NSGA-II调度优化
NSGA-II用于机组调度
工业调度多目标
Deb 2002
P080
PSO路径规划
PSO用于机器人路径规划
工业路径规划
Kennedy 1995
P081
ACO车辆路径
ACO用于VRP问题
物流路径优化
Dorigo 1992
P082
贝叶斯优化工艺参数
BO用于工艺参数整定
高成本实验优化
2024 IEEE TEVC
P083
多保真贝叶斯优化(MF-BO)
融合低/高精度数据
大幅减少高价值实验
2025 JMLR; BoTorch
P084
贝叶斯优化-进化混合
全局探索用EA局部调优用BO
高维复杂参数优化
2024 IEEE TEVC
P085
采集函数EI
期望改进采集函数
BO核心决策单元
Močkus 1975
P086
采集函数PI
概率改进采集函数
BO保守探索
Kushner 1964
P087
采集函数UCB
置信上界采集函数
BO探索-利用平衡
Srinivas 2010
P088
采集函数Thompson采样
后验采样采集函数
BO贝叶斯探索
Thompson 1933
P089
约束贝叶斯优化(Constrained BO)
同时优化目标与约束
带物理边界工程优化
2023 NeurIPS
P090
高斯过程回归(GPR)
BO代理模型核心
不确定性量化后验
Rasmussen 2006; GPyTorch
P091
Student-t过程回归
重尾替代GPR
鲁棒BO代理
2014
P092
随机森林代理模型
RF作为BO代理
高维离散优化
Hutter 2011
P093
贝叶斯神经网络代理
BNN作为BO代理
不确定性校准
2022
P094
TPE(树结构Parzen估计器)
序贯模型优化
超参数优化
Bergstra 2011; Optuna
P095
SMAC
序列模型算法配置
超参数/算法配置
Hutter 2011; SMAC3
P096
Hyperband
多保真超参数搜索
资源自适应分配
Li 2017
P097
BOHB
BO+Hyperband混合
高效超参数优化
Falkner 2018
P098
BoTorch
Meta贝叶斯优化框架
支持约束/多目标BO
Meta; BoTorch
P099
GPyTorch
高斯过程PyTorch框架
大规模GP推理
Gardner 2018
P100
Optuna
通用超参数优化框架
TPE/CMA-ES集成
Akiba 2019; Optuna
P101
Ray Tune
分布式超参数调优
大规模分布式搜索
Liaw 2018; Ray
P102
Ax(Adaptive Experimentation)
Meta平台贝叶斯优化
工业级BO服务
Meta; Ax
P103
scikit-optimize
Scikit-learn BO工具
简单易用BO
scikit-optimize
P104
线性二次调节器(LQR)
经典线性最优控制解析解
线性运动/温控/姿态稳定
现代控制理论; python-control
P105
模型预测控制(MPC)
滚动时域优化显式处理约束
化工/机器人/多变量协调
Garcia 1989; do-mpc
P106
CasADi
最优控制建模框架
MPC/动态优化
Andersson 2019; CasADi
P107
do-mpc
MPC Python工具箱
MPC工程实现
Fiedler 2021; do-mpc
P108
ACADO
快速最优控制C++库
实时MPC
Houska 2011; ACADO
P109
YALMIP
MATLAB优化建模语言
MIP/QP/SDP建模
Lofberg 2004
P110
CVXPY
Python凸优化建模
LP/QP/SDP/SOCP
Diamond 2016; CVXPY
2.3 神经符号融合增强
编号
算子名称
核心机制
架构角色
权威来源/工具
P111
神经引导符号回归(Neural-Guided SR)
NN提取特征→SR逼近输出
AlphaFold Evoformer白盒化
AI-Feynman 2.0; DeepSymbol
P112
端到端Transformer SR
数据驱动直接学习输入到表达式映射
快速策略原型器
DeepSymNet; GraphDSR
P113
神经嵌入搜索
数学表达式语义嵌入连续向量空间
语义级聚类多样性保护
GVAE-ABGEP; SNIP
P114
CGP提取神经网络语义(NNCGP)
CGP将黑箱NN转白盒符号表达式
黑盒模型白盒化
CGP12
P115
DRL增强GP种子生成
深度强化学习生成GP初始化种子
解决极度开放探索问题
P23
P116
PSRN(物理符号回归网络)
物理约束引导的大规模SR
比纯GP更快更准
2024; PSRN
P117
PhySO(物理符号优化)
物理约束优化SR
守恒律嵌入搜索
2024; PhySO
P118
SENSR(语义神经符号回归)
语义引导神经符号发现
可解释AI发现
2023; SENSR
P119
NeuralSymbolic库
神经符号通用框架
NN+符号推理集成
2023; NeuralSymbolic
P120
符号回归+知识图谱
知识图谱约束SR搜索
领域知识注入
2024
P121
Transformer-SR
Transformer直接生成表达式
端到端深度SR
2024
P122
GPT-SR
LLM引导符号回归
大模型语义引导
2024
P123
FunSearch风格闭环
LLM生成代码+沙箱评估+进化
生成-评估-优化闭环
DeepMind FunSearch
P124
程序语义对齐
生成代码与数学语义严格匹配
过滤无效代码
FunSearch架构
P125
启发式定向搜索
数学先验引导LLM定向搜索
提升搜索效率
FunSearch架构
P126
评估-反馈闭环算法
隔离沙箱自动化正确性性能评估
FunSearch风格闭环
FunSearch
P127
MSA(MSA Transformer)
多序列比对Transformer
AlphaFold核心基础
AlphaFold
P128
Evoformer
自注意力处理序列与残基长程依赖
AlphaFold主干网络
AlphaFold
P129
SE(3)-等变Transformer
三维结构生成保证空间等变性
端到端原子级精度坐标
AlphaFold
P130
自监督预训练
海量无标签蛋白质序列预训练
提升泛化能力
AlphaFold
P131
循环精炼算法
迭代循环精炼优化结构
持续优化物理合理性
AlphaFold
P132
多任务辅助损失
结构/距离/扭角多维度同步优化
保证物理化学规律
AlphaFold
P133
CoT(思维链)
LLM逐步推理生成中间步骤
复杂推理白盒化
OpenAI o3
P134
Tree of Thoughts
思维树搜索多路径推理
可进化可审计推理模型
OpenAI o3
P135
代码生成式LLM
生成可执行数学函数搜索解
规避数学幻觉
DeepMind FunSearch
2.4 优化与搜索算法
编号
算子名称
核心机制
架构角色
权威来源/工具
P136
梯度下降(SGD)
一阶梯度迭代优化
神经网络训练基础
Robbins 1951
P137
动量法(Momentum)
累积历史梯度方向
加速收敛
Polyak 1964
P138
Nesterov加速梯度(NAG)
预判式动量
凸优化最优收敛率
Nesterov 1983
P139
AdaGrad
自适应学习率(累积平方梯度)
稀疏梯度优化
Duchi 2011
P140
RMSProp
指数衰减平均自适应学习率
非平稳目标优化
Hinton 2012
P141
AdaDelta
无需全局学习率的AdaGrad改进
自适应学习率
Zeiler 2012
P142
Adam
一阶矩+二阶矩自适应估计
深度学习标准优化器
Kingma 2015
P143
AdamW
Adam+解耦权重衰减
正则化优化
Loshchilov 2019
P144
NAdam
Nesterov+Adam
加速Adam
Dozat 2016
P145
RAdam
Rectified Adam
自适应学习率 warmup
Liu 2020
P146
Lookahead
周期性前瞻更新
提升泛化
Zhang 2019
P147
LAMB
Layer-wise Adaptive Moments
大batch训练
You 2020
P148
LARS
Layer-wise Adaptive Rate Scaling
大batch训练
You 2017
P149
SAM(Sharpness-Aware Minimization)
最小化损失+平坦度
提升泛化
Foret 2021
P150
梯度惩罚
梯度范数正则化
WGAN-GP/稳定性
Gulrajani 2017
P151
谱归一化
权重矩阵谱范数约束
GAN稳定性
Miyato 2018
P152
牛顿法
二阶泰勒展开迭代
快速局部收敛(凸)
Newton 1687
P153
拟牛顿法(BFGS)
近似Hessian矩阵
中规模优化
Broyden 1970; scipy
P154
L-BFGS
有限内存BFGS
大规模优化
Liu 1989; scipy
P155
共轭梯度法(CG)
共轭方向搜索
大规模线性方程组
Hestenes 1952
P156
信赖域方法
信赖域内近似模型
非线性最小二乘
Nocedal 2006
P157
线搜索方法
Armijo/Wolfe条件步长
一阶优化步长控制
Nocedal 2006
P158
交替方向乘子法(ADMM)
分解求解带约束优化
分布式/大规模优化
Boyd 2010; cvxpy
P159
次梯度算法
非光滑凸优化
不可微目标函数
Nesterov; scipy
P160
近端梯度法(ISTA/FISTA)
带L1正则稀疏优化
稀疏优化标杆
Beck 2009; pyproximal
P161
半定规划(SDP)求解器
矩阵不等式约束优化
控制/量子/组合优化
Nemirovski; CVXPY/MOSEK
P162
内点法
障碍函数迭代
线性/凸优化
Mehrotra 1992
P163
单纯形法
顶点遍历线性规划
LP标准方法
Dantzig 1947
P164
对偶单纯形法
对偶空间遍历LP
LP高效求解
Lemke 1954
P165
Gomory切割
整数规划割平面
IP精确求解
Gomory 1958
P166
分支定界(B&B)
分支+界限剪枝
IP/MIP标准方法
Land 1960
P167
分支切割(B&C)
B&B+割平面
MIP高效求解
CPLEX/Gurobi
P168
列生成
主问题+子问题交替
大规模LP
Dantzig 1960
P169
拉格朗日松弛
松弛约束到目标函数
组合优化下界
Everett 1963
P170
Dantzig-Wolfe分解
分解结构化LP
大规模结构化LP
Dantzig 1960
P171
Benders分解
变量分解+割平面
大规模MIP
Benders 1962
P172
整数规划割平面
Gomory/MIR/Flow cover
IP强化松弛
CPLEX/Gurobi
P173
混合整数规划(MIP)求解器
通用MIP求解
工业级MIP
CPLEX/Gurobi/SCIP
P174
SCIP
开源MIP求解器
MIP/CP框架
Zuse Institute; SCIP
P175
OR-Tools
Google运筹优化工具
路由/调度/装箱
Google; OR-Tools
P176
PuLP
Python线性规划建模
LP/IP建模
Mitchell 2020; PuLP
P177
Pyomo
Python优化建模框架
大规模优化建模
Hart 2017; Pyomo
P178
Gurobi
商业MIP求解器
工业级MIP
Gurobi
P179
CPLEX
IBM商业MIP求解器
工业级MIP
IBM; CPLEX
P180
MOSEK
商业凸优化求解器
LP/QP/SDP/MIP
MOSEK
P181
GLPK
开源线性规划工具
LP/MIP
GNU; GLPK
P182
HiGHS
开源线性/混合整数规划
LP/MIP高效
Huangfu 2018; HiGHS
P183
COIN-OR
运筹优化开源算法库
LP/NLP/IP全集
COIN-OR
P184
CVXOPT
Python凸优化求解器
LP/QP/SDP/SOCP
Vandenberghe; CVXOPT
P185
PROPT
MATLAB最优控制工具箱
动态优化/MPC
Tomlab; PROPT
P186
GEKKO
PythonAPM优化套件
MPC/动态优化
Beal 2018; GEKKO
P187
Pyomo.dae
微分代数方程优化
动态系统优化
Pyomo
P188
Multi-Parametric Toolbox(MPT)
多参数规划工具箱
显式MPC
Kvasnica 2004; MPT3
P189
TuLiP
Python LTL控制合成工具箱
嵌入式控制软件合成
Caltech; TuLiP
P190
LTLMoP
LTL任务规划工具包
控制器合成/运动规划
zbMATH; LTLMoP
P191
SMC-LTL
STL Python控制库
信号时序逻辑控制
github; SMC-LTL
2.5 特征工程与预处理
编号
算子名称
核心机制
架构角色
权威来源/工具
P192
遗传特征构造(GFC)
自动组合原始特征生成高阶派生特征
提升下游模型性能
2023 IEEE Cybernetics
P193
基于互信息的特征选择
量化特征与目标非线性相关性
高维数据降维/传感器选型
信息论; scikit-learn
P194
主成分分析(PCA)
线性降维最大方差方向
特征压缩/去相关
Pearson 1901; sklearn
P195
t-SNE
非线性降维可视化
高维数据可视化
van der Maaten 2008
P196
UMAP
流形学习降维
高维数据可视化/聚类
McInnes 2018; umap-learn
P197
自编码器(AE)
编码-解码瓶颈降维
非线性特征提取
Hinton 2006
P198
变分自编码器(VAE)
概率编码降维
生成模型/不确定性编码
Kingma 2014
P199
独立成分分析(ICA)
盲源分离
信号分离/特征解耦
Hyvarinen 2000
P200
非负矩阵分解(NMF)
非负约束矩阵分解
文本/图像特征提取
Lee 1999
P201
因子分析(FA)
潜变量模型降维
心理测量/多变量建模
Spearman 1904
P202
线性判别分析(LDA)
有监督降维
分类特征提取
Fisher 1936
P203
核PCA(KPCA)
核技巧非线性PCA
非线性降维
Scholkopf 1998
P204
流形学习(Isomap/LLE)
非线性流形降维
高维数据结构发现
Tenenbaum 2000; Roweis 2000
P205
特征哈希
哈希函数映射特征
大规模稀疏特征
Weinberger 2009
P206
目标编码(Target Encoding)
目标均值编码分类特征
分类变量数值化
Micci-Barreca 2001
P207
独热编码(One-Hot)
分类变量二值化
分类变量标准化
标准预处理
P208
标准化/归一化
Z-score/Min-Max缩放
数值特征标准化
标准预处理
P209
多项式特征生成
特征交叉组合
非线性特征扩展
scikit-learn
P210
离散化/分箱
连续变量离散化
决策树/规则模型
scikit-learn
P211
缺失值填充
均值/中位数/KNN/模型填充
数据预处理
scikit-learn
P212
异常值检测(Isolation Forest)
隔离森林异常检测
异常样本剔除
Liu 2012; sklearn
P213
SMOTE过采样
合成少数类过采样
不平衡数据处理
Chawla 2002; imblearn
P214
ADASYN过采样
自适应合成采样
不平衡数据自适应
He 2008; imblearn
P215
Tomek Links欠采样
移除边界多数类样本
不平衡数据清洗
Tomek 1976; imblearn
P216
ENN欠采样
编辑最近邻移除噪声
不平衡数据清洗
Wilson 1972; imblearn
P217
时间序列特征提取(tsfresh)
自动化时序特征提取
时序数据特征工程
Christ 2018; tsfresh
P218
文本特征(TF-IDF)
词频-逆文档频率
文本向量化
Salton 1988; sklearn
P219
词嵌入(Word2Vec/GloVe/FastText)
词向量表示
NLP特征提取
Mikolov 2013; Pennington 2014
P220
Transformer嵌入(BERT)
预训练语言模型嵌入
NLP特征提取
Devlin 2018; HuggingFace
2.6 微分/几何/张量优化
编号
算子名称
核心机制
架构角色
权威来源/工具
P221
黎曼梯度下降
流形约束优化
保证解在流形上(旋转矩阵/概率单纯形)
Boumal 2020; pymanopt
P222
黎曼Adam
流形上的Adam优化器
流形约束深度学习
Becigneul 2019
P223
黎曼SGD
流形上的SGD
流形约束优化基线
Bonnabel 2013
P224
测地线步长
沿测地线更新参数
流形全局优化
Absil 2008
P225
指数映射/对数映射
流形与切空间映射
流形优化核心操作
Lee 2018
P226
并行传输
切空间向量传输
流形优化梯度传递
Sato 2014
P227
张量分解(CP/Tucker)
高阶张量低秩近似
高维数据压缩/特征提取
Kolda 2009; tensorly
P228
张量网络(Tensor Train)
TT格式高维张量
高维函数近似/量子物理
Oseledets 2011; ttpy
P229
辛积分算子
保辛结构数值积分
哈密顿系统长期演化
Yoshida 1990
P230
辛Euler
辛格式Euler方法
哈密顿系统保结构
Sanz-Serna 1988
P231
辛Runge-Kutta
辛RK方法
高精度哈密顿积分
Sanz-Serna 1988
P232
蛙跳法(Leapfrog)
辛格式二阶积分
分子动力学标准
Verlet 1967
P233
Verlet积分
辛格式积分
分子动力学/天体力学
Verlet 1967
P234
辛几何数值积分
保辛流形数值方法
长期能量守恒
Hairer 2006
P235
李群优化
李群上的优化
机器人运动学/刚体变换
Absil 2008
P236
SO(3)优化
旋转群上的优化
姿态估计/机器人
Hu 2020
P237
SE(3)优化
欧氏群上的优化
刚体运动规划
Zefran 1998
P238
Grassmann流形优化
Grassmann流形上的优化
子空间跟踪/降维
Edelman 1998
P239
Stiefel流形优化
Stiefel流形上的优化
正交约束优化
Absil 2008
P240
概率单纯形优化
单纯形上的优化
概率分布优化
Beck 2003
2.7 PDE数值解算子族
编号
算子名称
核心机制
架构角色
权威来源/工具
P241
有限元法(FEM)
椭圆型/抛物型PDE求解
复杂几何域物理系统建模
Zienkiewicz; FEniCSx/Deal.II
P242
有限体积法(FVM)
守恒型PDE求解
流体/传热计算
OpenFOAM/FiPy
P243
谱方法
高精度PDE求解
光滑解精度指数收敛
Trefethen; Chebfun/Dedalus
P244
有限差分法(FDM)
网格差分PDE求解
通用PDE基线方法
标准数值分析
P245
边界元法(BEM)
边界积分方程
无限域/边界问题
Beer 2008
P246
等几何分析(IGA)
NURBS基函数FEM
CAD/CAE统一
Hughes 2005
P247
格子玻尔兹曼(LBM)
介观尺度流体求解
复杂边界/多相流
Palabos/LBM-OpenLB
P248
光滑粒子流体动力学(SPH)
无网格拉格朗日粒子法
自由表面/大变形
Gingold 1977
P249
离散元法(DEM)
颗粒离散元
颗粒流动/粉体
Cundall 1979
P250
多尺度有限元(MsFEM)
多尺度基函数FEM
多孔介质/复合材料
Hou 1997
P251
自适应网格细化(AMR)
动态网格加密
激波/界面追踪
Berger 1984
P252
FEniCSx
Python FEM框架
自动化PDE求解
Logg 2012; FEniCS
P253
Deal.II
C++ FEM库
大规模自适应FEM
Bangerth 2007; Deal.II
P254
COMSOL Multiphysics
商业多物理场仿真
工业级多物理场耦合
COMSOL
P255
OpenFOAM
开源CFD工具箱
工业级流体仿真
OpenFOAM Foundation
P256
FiPy
Python有限体积PDE
简单FVM求解
Guyer 2009; FiPy
P257
Chebfun
MATLAB谱方法工具
函数计算/微分方程
Trefethen 2014; Chebfun
P258
Dedalus
Python谱方法PDE
流体/天体物理
Burns 2020; Dedalus
P259
ClawPack
双曲守恒律PDE
激波/间断解
LeVeque 1994; ClawPack
P260
PyClaw
Python ClawPack
双曲PDE Python接口
Ketcheson 2012
2.8 反问题与逆算子
编号
算子名称
核心机制
架构角色
权威来源/工具
P261
Tikhonov正则化
病态反问题加正则项
压制噪声放大
Tikhonov 1943; scipy
P262
Landweber迭代
迭代正则化反问题
收敛可控
Landweber 1951
P263
共轭梯度正则化
CG迭代正则化
半收敛正则化
Hanke 1995
P264
L1正则化(LASSO)
稀疏重构压缩感知
少量观测恢复信号
Tibshirani 1996; sklearn
P265
L0正则化
稀疏选择
最优子集选择
Natarajan 1995
P266
弹性网(Elastic Net)
L1+L2混合正则化
稀疏+稳定
Zou 2005; sklearn
P267
组LASSO
组稀疏正则化
结构化稀疏
Yuan 2006
P268
融合LASSO(Fused Lasso)
相邻系数差分稀疏
信号分段常数
Tibshirani 2005
P269
趋势滤波(Trend Filtering)
L1趋势滤波
时序信号去噪
Kim 2009
P270
全变分正则化(TV)
梯度L1正则化
图像去噪/恢复
Rudin 1992
P271
贝叶斯反问题
反问题不确定性量化
输出参数后验分布
Stuart 2005; PyMC
P272
变分贝叶斯
变分推断反问题
近似后验
Blei 2017
P273
马尔可夫链蒙特卡洛(MCMC)
贝叶斯后验采样
高维分布抽样
Metropolis 1953; PyMC/Stan
P274
哈密顿蒙特卡洛(HMC)
动量辅助MCMC
高维高效采样
Duane 1987; Stan
P275
No-U-Turn Sampler(NUTS)
自适应HMC
Stan默认采样器
Hoffman 2014
P276
序贯蒙特卡洛(SMC)
粒子滤波/序贯重要性采样
状态空间模型在线推断
Doucet 2001
P277
近似贝叶斯计算(ABC)
似然无关贝叶斯
不可解析似然模型
Beaumont 2002
P278
变分推断(VI)
优化替代采样
大规模贝叶斯近似
Jordan 1999; Pyro
P279
随机变分推断(SVI)
小批量VI
大规模数据贝叶斯
Hoffman 2013
P280
伴随方法梯度算子
PDE约束优化高效梯度
反演参数最优化
FEniCS-adjoint/dolfin-adjoint
2.9 随机模拟与蒙特卡洛
编号
算子名称
核心机制
架构角色
权威来源/工具
P281
蒙特卡洛(MC)采样
随机采样估计统计量
高维积分/不确定性传播
Metropolis 1949; numpy
P282
重要性采样
非均匀采样降低方差
稀有事件估计
Kahn 1950
P283
分层采样
分层后均匀采样
方差缩减
Cochran 1977
P284
拉丁超立方采样(LHS)
分层采样比纯MC更少样本
不确定性分析标准方法
McKay 1979; SALib
P285
准蒙特卡洛(QMC)
低偏差序列采样
高维积分高效
Niederreiter 1992; scipy.stats.qmc
P286
Sobol序列
低偏差准随机序列
全局敏感性分析
Sobol 1967; SALib
P287
Halton序列
低偏差准随机序列
QMC基线
Halton 1960
P288
多项式混沌展开(PCE)
随机过程展开正交多项式基
高效不确定性传播
Ghanem 2002; Chaospy/UQpy
P289
随机配置法
稀疏网格配点
不确定性量化
Xiu 2005
P290
全局敏感性分析(Sobol指数)
方差分解敏感性
识别关键参数
Sobol 2001; SALib
P291
Morris方法
轨迹敏感性分析
初步参数筛选
Morris 1991; SALib
P292
FAST(傅里叶幅度敏感度)
频域敏感性分析
全局敏感性
Cukier 1978
P293
可靠性分析(FORM/SORM)
一次/二次可靠度方法
结构可靠性
Hasofer 1974
P294
蒙特卡洛可靠性
MC采样估计失效概率
高精度可靠性
Rubinstein 1981
P295
子集模拟
条件概率分层采样
小失效概率估计
Au 2001
P296
交叉熵方法(CE)
重要性分布自适应优化
稀有事件/优化
Rubinstein 1997
P297
序贯蒙特卡洛(SMC)粒子滤波
粒子滤波状态估计
非线性系统在线推断
Doucet 2001; FilterPy
P298
无迹变换(UT)
确定性采样传播不确定性
UKF核心
Julier 1997
P299
无迹卡尔曼滤波(UKF)
UT+卡尔曼滤波
非线性状态估计
Wan 2000; FilterPy
P300
粒子滤波(PF)
粒子集合状态估计
强非线性/非高斯
Gordon 1993; FilterPy

三、E层（变量层：边界监控算子）
E层是白盒化的"物理底线"，不关心P层策略有多精妙，只问："这个策略在当前物理变量下安全吗？"其核心属性为确定性与可证明性。
3.1 运行时验证与形式化方法
编号
算子名称
核心机制
架构角色
权威来源/工具
E001
运行时验证(RV)
时序逻辑公式旁路监控实时校验
监控状态变量序列合规性
RTAMT/Varanus/PyMOP
E002
LTL(线性时序逻辑)
时序逻辑规约描述
离散事件安全策略
Pnueli 1977
E003
STL(信号时序逻辑)
连续信号时序逻辑
连续物理变量监控
Maler 2004; RTAMT
E004
MITL(度量区间时序逻辑)
STL扩展带时间区间
工业时序监控
Alur 1996
E005
概率信号时序逻辑(ProbSTL)
带概率分布噪声信号
传感器噪声工业现场
2023 HSCC
E006
计算树逻辑(CTL)
分支时间规约
状态机系统验证
Clarke 1981; NuSMV
E007
CTL*
CTL+LTL统一
通用时序逻辑
Emerson 1982
E008
μ-演算
不动点时序逻辑
最强表达时序逻辑
Kozen 1983
E009
STL鲁棒度计算
连续满足程度数值
安全裕度评估/预警分级
2009 HSCC; Breach
E010
LTL/STL falsification(S-TaLiRo)
反向搜索违反规约输入
对抗性压力测试E层规约
S-TaLiRo/PSY-TaLiRo
E011
RTAMT
STL在线/离线定量监控
嵌入式/在线场景
github; RTAMT
E012
Reelay
统一在线LTL/MTL/STL监控
嵌入式/在线场景
arxiv; Reelay
E013
HStriver
实时事件流RV引擎
事件+时间类安全规约
imdea.org; HStriver
E014
PyMOP
Python大规模RV系统
5种逻辑/5种监控算法
Semantic Scholar; PyMOP
E015
TraceMOP
显式轨迹RV工具
105个开源项目评估
FSE 2025; TraceMOP
E016
Valg
反馈引导选择性监控
64个开源项目验证
ASE 2025; Valg
E017
Varanus
CSP专用RV工具
通信顺序进程监控
arXiv 2025; Varanus
E018
Linux Kernel RV
LTL内核态RV监控器
工业级内核RV
Linux主线v7.1
E019
COBALT
Z3 SMT形式验证引擎
部署前识别漏洞
arXiv 2026; COBALT
E020
CICheck
因果发现验证
因果图校验
CICheck
E021
DetectEr
运行时检测工具
嵌入式系统RV
DetectEr
E022
Z3 SMT求解器
满足性模理论求解
逻辑/算术/数组规约校验
Microsoft; Z3
E023
UPPAAL
时间自动机模型检验
实时系统安全性/可达性/死锁
奥胡斯大学; UPPAAL
E024
NuSMV
符号模型检验
状态机/数字逻辑验证
CMU; NuSMV
E025
SPIN
显式状态模型检验
协议/并发系统验证
Holzmann; SPIN
E026
Coq证明助手
高阶逻辑定理证明
算法/协议完备性证明
INRIA; Coq
E027
Isabelle/HOL
交互式定理证明
形式化数学证明
Cambridge; Isabelle
E028
Lean定理证明器
依赖类型定理证明
现代形式化数学
de Moura 2015; Lean
E029
Agda
依赖类型证明助手
构造性数学证明
Norell 2007; Agda
E030
TLA+
规约语言+模型检验
分布式系统设计验证
Lamport 1999; TLA+
E031
Alloy
轻量级形式化方法
结构化模型分析
MIT; Alloy
E032
Dafny
程序验证语言
程序正确性证明
Microsoft; Dafny
E033
Frama-C
C程序静态分析框架
C代码形式化验证
CEA; Frama-C
E034
Astrée
抽象解释静态分析
嵌入式C代码安全验证
Astrée
E035
CBMC
有界模型检验C程序
C程序BMC
Clarke; CBMC
E036
ESBMC
嵌入式系统BMC
C/C++ BMC
ESBMC
E037
CPAchecker
可配置软件验证
C程序抽象解释+BMC
SV-COMP; CPAchecker
E038
LLVM Sanitizers
运行时内存安全检查
ASan/UBSan/MSan/TSan
LLVM
E039
AddressSanitizer(ASan)
内存越界检测
运行时内存安全
LLVM; ASan
E040
UndefinedBehaviorSanitizer(UBSan)
未定义行为检测
C/C++ UB检测
LLVM; UBSan
E041
MemorySanitizer(MSan)
未初始化内存检测
内存安全
LLVM; MSan
E042
ThreadSanitizer(TSan)
数据竞争检测
并发安全
LLVM; TSan
E043
Valgrind
动态分析工具集
内存泄漏/越界检测
Valgrind
E044
抽象解释算子
静态分析可达状态超逼近
程序安全性验证
Cousot 1977; Astrée
E045
模型检验算子
穷尽搜索状态空间
系统满足规约验证
Clarke图灵奖; NuSMV/SPIN
E046
可达集计算算子
动态系统所有可达状态
判断是否越界
Althoff 2011; CORA/Flow*
E047
浮点误差分析算子
静态计算浮点舍入误差
保证数值精度
Fluctuat/Gappa
E048
符号执行
符号值执行程序
路径条件求解
Cadar 2008; KLEE
E049
KLEE
符号执行引擎
C程序路径覆盖
Cadar 2008; KLEE
E050
Angr
Python符号执行框架
二进制分析
Shoshitaishvili 2016
E051
有界模型检验(BMC)
展开k步验证
程序/系统有限步验证
Biere 1999
E052
k-归纳
k步归纳证明
无限步安全证明
Sheeran 2003
E053
IC3/PDR
不变式生成
安全属性证明
Bradley 2011
E054
属性导向可达性(PDR)
IC3改进
安全系统验证
Bradley 2011
E055
插值模型检验
Craig插值BMC
无限状态系统
McMillan 2003
E056
CEGAR(反例引导抽象精化)
反例→精化循环
大规模系统验证
Clarke 2003
E057
谓词抽象
抽象为布尔程序
程序验证
Graf 1997
E058
抽象-精化循环
抽象+反例精化
自动验证
Clarke 2003
E059
不变式生成
自动生成循环不变式
程序验证
Sharma 2013
E060
Horn子句求解
CHC约束求解
程序验证后端
Hoder 2011; Z3
3.2 控制屏障函数与安全滤波
编号
算子名称
核心机制
架构角色
权威来源/工具
E061
控制屏障函数(CBF)
物理安全边界定义为安全集,计算最小修正向量
柔性安全边界/避障
Ames 2019; refineCBF
E062
CBF-QP
二次规划求解CBF修正
实时安全控制
Ames 2016
E063
滤波CBF(FCBF)
辅助动态系统正则化滤波器
解决CBF抖动/优雅控制
2025 arXiv; FCBFs
E064
高阶CBF(HOCBF)
高阶导数CBF
相对阶>1系统
Xu 2015
E065
鲁棒CBF(RCBF)
鲁棒控制屏障函数
不确定系统安全
Wabersich 2021
E066
随机CBF(SCBF)
概率安全边界>1-δ
噪声环境概率安全
Lester 2019 CDC
E067
数据驱动CBF
数据驱动方法计算认证CBF
局部李普希茨系统安全
2025 ScienceDirect
E068
输出反馈CBF
输入受限+状态估计误差
备份CBF安全保证
2026 arXiv
E069
预测CBF(PCBF)
离散时间未建模延迟预测CBF
离散时间系统
2025 Semantic Scholar
E070
逆最优安全滤波
无限时域最优CBF族
保守性换存活时间
2023 RCS
E071
Barrier贝叶斯回归
在线学习CBF条件
不确定系统安全滤波
学术期刊
E072
矩阵CBF
标量CBF推广矩阵值
非光滑安全集
2025 Caltech
E073
CBF飞行包线保护
CBF-QP飞行包线约束
航空安全
2026 arXiv
E074
循环嵌入CBF
解决CBF-QP不良平衡点
安全导航
2025 ScienceDirect
E075
CBF最小相位条件
理论揭示安全滤波条件
CBF理论基础
2025 Semantic Scholar
E076
CBF动力学性质
稳定性/有界性分析
安全滤波器闭环行为
2026 arXiv
E077
CBF潜空间扩展
HJ可达性扩展潜空间
高维安全视觉运动
2025 arXiv
E078
优雅安全控制CBF
多层安全保障非硬切换
优雅安全评价标准
2026 arXiv
E079
事件触发CBF
事件触发安全滤波
减少通信开销
Girard 2015
E080
分布式CBF
多智能体分布式CBF
多机器人安全
Borrmann 2015
E081
离散时间CBF
离散时间系统CBF
数字控制系统
Agrawal 2017
E082
自适应CBF
参数自适应CBF
不确定参数系统
Lopez 2020
E083
神经网络CBF(NCBF)
神经网络学习CBF
复杂系统安全
2024; NCBF
E084
鲁棒控制不变集
有界扰动下最大安全不变集
鲁棒安全边界
Raković 2005; MPT3
E085
Hamilton-Jacobi可达性
求解HJ偏微分方程计算可达集
预测未来安全
LevelSetPy; CORA
E086
CORA
可达集计算工具箱
动态系统可达性
Althoff 2011; CORA
E087
Flow*
连续系统可达性
非线性系统流达集
Chen 2013; Flow*
E088
SpaceEx
线性系统可达性
混合系统验证
Frehse 2011; SpaceEx
E089
Breach
STL鲁棒度工具
时序逻辑可达性
Donze 2010; Breach
E090
STLInspector
STL监控工具
STL规约检查
STLInspector
E091
S-TaLiRo
时序逻辑鲁棒性falsification
对抗性测试
Annpureddy 2011
E092
PSY-TaLiRo
S-TaLiRo扩展
概率系统测试
PSY-TaLiRo
E093
Scenic
概率编程描述场景
自动驾驶极端场景生成
Stanford; Scenic
E094
refineCBF
Python CBF工具箱
CBF原型开发
github; refineCBF
E095
CBF-CLF-Helper
Matlab CBF/CLF库
CBF/CLF教学原型
github; CBF-CLF-Helper
E096
nmpc-dclf-dcbf
NMPC+DCLF+DCBF
机器人安全控制
HybridRobotics
E097
SOTER
编程式RTA框架
Simplex/RTA开发
researchgate; SOTER
E098
SOTERonROS
ROS上RTA框架
机器人RTA
github; SOTERonROS
3.3 Simplex架构与硬安全切换
编号
算子名称
核心机制
架构角色
权威来源/工具
E099
Simplex架构
高级控制器+安全基线控制器切换
硬安全兜底/零容忍场景
Sha 1996; SOTERonROS
E100
自适应Simplex
可证明正确自适应切换逻辑
时序规范最大化高级控制器
2025 Springer
E101
实时可达性Simplex
实时可达性分析验证切换
超调和安全切换正确性
2016 ACM TECS
E102
FDR形式化Simplex
FDR模型检验器形式化
安全-活性性质规范
2014 CORE
E103
SEI Simplex架构描述
过程控制系统安全在线升级
工业过程控制
SEI
E104
Simplex综述
非正式回顾
安全可靠实时系统
1996 FID-Move
E105
动态加权Simplex
动态加权策略CPS
学习使能CPS安全
2020 arXiv
E106
紧急刹车Simplex
KKT内点法优化参考状态
约束突变紧急刹车(快10²-10⁴倍)
2025 arXiv:2501.01831
E107
DL Simplex
1类实时Hypervisor隔离DL控制器
深度学习安全
2025 arXiv
E108
RL Simplex路径追踪
RL+高保障控制器
安全路径追踪
2025 arXiv:2503.10559
E109
屏障证书Simplex(Bb-Simplex)
屏障证书证明基线安全
自动推导切换条件
arXiv; Bb-Simplex
E110
黑箱Simplex
运行时检查替代静态验证
黑箱场景RTA
arXiv; Black-Box Simplex
E111
神经Simplex(NSA)
神经网络控制器RTA
NN控制器安全保障
arXiv; NSA
E112
SL1-Simplex
自驾车安全速度调节
动态未知环境
arXiv; SL1-Simplex
E113
分布式Simplex(DSA)
多智能体分布式RTA
多智能体安全
2023 JSA
E114
黑箱多智能体Simplex
黑箱Simplex多智能体CPS
多智能体RTA
2025 ISSE
E115
运行时保证(RTA)框架
通用RTA架构
安全切换通用框架
SOTER/SOTERonROS
E116
三模冗余(TMR)
三路独立计算多数表决
硬件容错
von Neumann 1956
E117
N版本编程
多版本独立实现表决
软件容错
Avizienis 1985
E118
恢复块
接受测试+备用模块
软件容错
Randell 1975
E119
检查点/回滚
定期保存状态+故障回滚
长运行容错
Bhargava 1986
E120
看门狗定时器
超时检测+强制复位
嵌入式安全
标准硬件
E121
心跳检测
周期性心跳信号
分布式存活检测
标准分布式
E122
故障注入测试
故意注入故障测试容错
验证容错机制
Hsueh 1997
E123
混沌工程(Chaos Engineering)
随机故障注入生产环境
验证系统韧性
Netflix Chaos Monkey
3.4 物理不变量硬校验
编号
算子名称
核心机制
架构角色
权威来源/工具
E124
能量守恒校验
输入-输出-损耗能量平衡
热力学第一定律
IEC 61508
E125
动量守恒校验
运动系统动量/角动量变化
经典力学
Newton
E126
质量守恒校验
流入-流出-存量平衡
流体力学基本定律
Lavoisier
E127
热力学熵增校验
孤立系统熵不减
热力学第二定律
Clausius
E128
李雅普诺夫稳定性校验
实时计算李雅普诺夫函数值
运动控制稳定性监控
Lyapunov 1892; Drake
E129
诺特定理导出算子
对称性自动推导守恒律
生成物理校验规则
Noether 1918; SymPy
E130
数据驱动守恒律发现
时序数据自动挖掘守恒量
E层硬约束
2019 PNAS; PySINDy
E131
CAS(计算机代数系统)
符号推导/化简/方程解析求解
物理公式验证
SymPy/Mathematica
E132
前向自动微分
精确计算函数梯度
数值验证无截断误差
JAX/PyTorch Autograd
E133
反向自动微分
反向模式自动微分
高维梯度计算
PyTorch/TensorFlow
E134
区间算术校验
变量用区间表示计算上下界
保证包含真值
Moore 1966; interval
E135
仿射算术
区间算术扩展跟踪相关性
降低过估计
Stolfi 1993; LibAffine
E136
NS方程正则性校验
流体仿真结果物理正则性
判定解满足能量有界
韦东奕; FEniCS/OpenFOAM
E137
随机矩阵普适性融合
Wigner矩阵特征值普适性
高维多源证据分布无关融合
韦东奕; scipy.linalg
E138
奇异积分约束
调和分析奇异积分算子
时序/空间信号边界陡变校验
韦东奕; PyWavelets
E139
非线性PDE稳定性
偏微分方程解稳定性
动力系统稳定控制策略
韦东奕; FEniCS
E140
边界层渐近校正
流体/传热边界层渐近解析
提升低维模型边界精度
韦东奕; BoundaryLayerTheory
E141
死锁检测算子
实时监控状态机预判死锁
并发系统安全
Dijkstra; RTOS/SPIN
E142
时序违例检测
监控任务执行时间/通信延迟
实时系统超时检测
RTOS; WCET工具
E143
内存安全校验
运行时检查越界/空指针/泄漏
软件工程安全
ASan/Valgrind
E144
形式化可证明安全
归约证明密码算法安全
现代密码学基石
Goldwasser & Micali; CryptoVerif
E145
侧信道抗性校验
验证功耗/时序攻击抗性
密码工程安全
ChipWhisperer; DPA Contest
E146
WCET分析
最坏情况执行时间分析
实时系统可调度性
Wilhelm 2008; OTAWA
E147
调度分析
任务可调度性分析
实时系统设计
Liu 1973
E148
优先级反转检测
优先级反转检测
实时系统安全
Sha 1990
E149
栈溢出检测
栈深度分析
嵌入式安全
Stack Analyzer
E150
整数溢出检测
整数运算溢出检测
数值安全
CBMC/ESBMC
3.5 故障检测与隔离(FDI)
编号
算子名称
核心机制
架构角色
权威来源/工具
E151
解析冗余关系(ARR)
物理模型生成残差
传感器/执行器故障定位
Staroswiecki 2000
E152
卡尔曼滤波残差检测
状态估计与实测值残差
线性系统传感器故障
Kalman 1960; FilterPy
E153
扩展卡尔曼滤波(EKF)
非线性状态估计残差
非线性系统故障检测
Jazwinski 1970
E154
无迹卡尔曼滤波(UKF)
UT+KF残差
非线性强系统故障
Wan 2000; FilterPy
E155
粒子滤波残差
粒子集合残差
强非线性/非高斯故障
Gordon 1993
E156
观测器故障检测
未知输入观测器
鲁棒故障检测
Chen 1999
E157
滑模观测器
滑模观测器故障检测
鲁棒故障估计
Edwards 1994
E158
参数估计故障检测
参数偏差检测
渐进故障检测
Isermann 1984
E159
奇偶空间方法
奇偶方程残差
传感器故障检测
Gertler 1991
E160
频域故障检测
频谱分析故障
旋转机械故障
Randall 2011
E161
振动分析故障检测
振动信号特征提取
轴承/齿轮箱故障
McFadden 1969
E162
电流信号分析
电机电流频谱
电机故障
Benbouzid 2000
E163
温度分布分析
红外热像分析
电气设备热故障
Maldague 2001
E164
油液分析
润滑油金属颗粒分析
机械磨损故障
Hunt 1993
E165
声发射检测
声发射信号分析
结构裂纹/泄漏
Grosse 2008
E166
滑动窗口FDI
滑动窗口残差统计
时变故障检测
Basseville 1993
E167
CUSUM检测
累积和变点检测
渐进故障检测
Page 1954
E168
GLR检测
广义似然比检测
故障假设检验
Willsky 1976
E169
SPRT(序贯概率比检验)
序贯假设检验
快速故障检测
Wald 1947
E170
贝叶斯故障检测
贝叶斯后验故障概率
不确定性故障检测
Simani 2003
E171
机器学习故障检测
分类/回归故障检测
数据驱动故障
Worden 2000
E172
深度学习故障检测
CNN/LSTM故障检测
复杂模式故障
Zhao 2019
E173
数字孪生故障检测
数字孪生对比检测
实时虚拟-物理对比
Tao 2019
E174
故障隔离(FI)
故障源定位
多传感器故障区分
Gertler 1998
E175
故障辨识(FC)
故障幅度估计
故障严重度评估
Isermann 2006
E176
故障恢复(FR)
故障后重构控制
容错控制
Zhang 2008
E177
主动容错控制(FTC)
主动重构控制器
故障后性能维持
Zhang 2008
E178
被动容错控制
鲁棒设计容忍故障
预设鲁棒容错
Patton 1997
E179
硬件冗余
多传感器/执行器冗余
物理冗余容错
标准工业
E180
解析冗余
软件/模型冗余
无额外硬件容错
Staroswiecki 2000

四、F层（结果层：证据融合与仲裁算子）
F层的核心使命是解决P与E的冲突，给出最终可执行决策。其核心属性为冲突量化与决策融合。
4.1 D-S证据理论与扩展体系
编号
算子名称
核心机制
架构角色
权威来源/工具
F001
D-S证据理论(基础)
Dempster正交和计算融合全局置信度
常见软冲突仲裁
Shafer 1976; pyds/dstz
F002
加权D-S证据理论
历史可靠度+可信度分配权重
有先验知识中度冲突
DS3; DS14
F003
支持概率距离(SPD)
量化P和E输出概率分布距离
冲突烈度度量仪表盘
DS18; DS24
F004
DSmT理论
DST超集打破互斥假设处理Zadeh悖论
极端硬冲突悖论裁决
DS12; Dezert 2006
F005
冲突自适应稳健组合规则
超阈值自动切换全信E层
自动化冲突仲裁
DS6; DS17
F006
软似然聚合方案
结构化可靠性建模平滑聚合
中等冲突平滑折中
DS17; DS23
F007
信念分歧度量
融合前计算分歧度发现硬冲突
冲突预检与预处理
DS13; DS22
F008
强化证据Jensen-Alpha分歧
DST框架多传感器故障诊断
多源冲突信息处理
DS23
F009
基数感知证据组合规则
组合前考虑焦点元素基数
缓解异常行为
DS4; DS11
F010
分层传感器融合-DST
梯度提升+序数模式+DST
航空/工业多层级传感器
DS20; DS25
F011
跨传感器一致性分类融合
跨传感器故障信息一致性分类
故障诊断场景
DS21
F012
中智证据集相似度融合
中智证据集+相似度+邓熵
复杂不确定性证据融合
DS19
F013
证据感知多模态融合
图像/非图像/融合分支证据网络
医疗/多模态场景
DS24
F014
SVM-DS决策融合
SVM+DS解决BPA确定难
提高故障诊断准确率
2018 电子技术应用
F015
证据理论区间融合
区间值证据融合
证据不精确场景
2020 Info Fusion; dstz
F016
基于证据折扣的冲突消解
可靠度折扣后融合
从源头降低冲突
Shafer 1976
F017
基于可信度的冲突分配
可信度比例分配冲突质量
兼顾合理性与计算量
2018 IEEE TFS
F018
Murphy平均组合规则
简单平均BPA组合
基线组合规则
Murphy 2000
F019
Yager组合规则
不归一化冲突分配
保留冲突信息
Yager 1987
F020
Dubois-Prade组合规则
交集+并集组合
冲突保留
Dubois 1988
F021
PCR1-PCR6(比例冲突重分配)
比例重分配冲突质量
DSmT系列组合规则
Dezert 2006
F022
PCR5
最精确比例冲突重分配
DSmT推荐规则
Dezert 2006
F023
混合DSmT
混合超幂集DSmT
复杂识别框架
Dezert 2006
F024
广义DSmT
完全广义DSmT
最一般化证据融合
Dezert 2006
F025
ER(证据推理)规则
证据推理规则集成
权重可靠度可解释集成
Yang 2002; ERTool
F026
证据推理(ER)框架
D-S+多属性决策
多属性证据融合
Yang 1994; ERTool
F027
置信规则库(BRB)
IF-THEN规则+证据推理
专家知识+证据融合
Yang 2006
F028
主观逻辑(Subjective Logic)
观点不确定性量化
认知偏差仲裁
Josang 2016
F029
证据深度学习(EDL)
NN直接输出证据+狄利克雷分布
模型不确定性量化
Sensoy 2018 NeurIPS
F030
Dempster规则
经典正交和组合
基础组合规则
Dempster 1967
F031
Smets规则(TBM)
可转移信任模型
不归一化组合
Smets 1994
F032
Inagaki规则
广义组合规则
参数化组合
Inagaki 1991
F033
Zadeh反例处理
Zadeh悖论修正
极端冲突处理
Zadeh 1986
F034
pyds
经典DST Python库
归一化/非归一化BPA
github; pyds
F035
dstz
轻量Python证据理论库
区间值证据
pypi; dstz
F036
py_dempster_shafer
Python D-S BPA组合库
BPA组合
pypi
F037
ERTool
Python证据推理方法
ER框架
pypi; ERTool
F038
efficient-DST
C++通用DST框架
高性能DST
github; efficient-DST
F039
DSmT理论书
DSmT通用方法论与公式
理论参考
philpapers; DSmT
4.2 多目标决策与权衡
编号
算子名称
核心机制
架构角色
权威来源/工具
F040
多目标决策(MODM)
性能和安全博弈目标函数帕累托前沿
系统级权衡
ENS12
F041
动态加权投票
任务上下文+P历史+E威胁度实时权重
上下文感知仲裁
DS14; SPX6
F042
帕累托前沿寻优
MOGA生成帕累托曲线
离线策略规划
ENS12
F043
MOGA优化Stacking
多目标GA优化Stacking集成
Pareto前沿模型选择
ENS12
F044
R-NSGA-II
参考点引导多目标
决策者偏好嵌入
Deb 2006
F045
MOEA/D
分解多目标为标量子问题
凸多目标高效
Zhang 2007
F046
MOPSO
多目标粒子群
连续多目标
Coello 2004
F047
多准则排序
PROMETHEE/ELECTRE
多准则决策
Brans 1985; ELECTRE
F048
PROMETHEE
偏好函数多准则
多准则排序
Brans 1985
F049
ELECTRE
级别高于关系多准则
多准则选择
Roy 1968
F050
TOPSIS
逼近理想解排序
多准则决策
Hwang 1981
F051
VIKOR
折中规划多准则
多准则妥协
Opricovic 2004
F052
AHP(层次分析法)
层次结构权重
主观偏好多准则
Saaty 1980
F053
ANP(网络分析法)
网络结构权重
依赖反馈多准则
Saaty 2001
F054
MAUT(多属性效用理论)
效用函数多属性
风险决策
Keeney 1976
F055
加权求和
线性加权组合
简单多准则基线
标准方法
F056
加权积
乘积加权组合
非线性多准则
标准方法
F057
模糊多准则决策
模糊集+多准则
不确定性多准则
Zimmermann 1987
F058
直觉模糊多准则
直觉模糊集+多准则
犹豫度多准则
Atanassov 1986
F059
毕达哥拉斯模糊多准则
毕达哥拉斯模糊集+多准则
隶属度平方和≤1
Yager 2014
F060
灰色关联分析
灰色关联度排序
小样本多准则
Deng 1989
F061
数据包络分析(DEA)
相对效率评价
多输入多输出效率
Charnes 1978
F062
平衡计分卡
多维度绩效评价
战略管理
Kaplan 1992
F063
有效信息准则(EIC)
超越准确性复杂度评估
结构稳定性
LTL4
4.3 冲突度量与预处理
编号
算子名称
核心机制
架构角色
权威来源/工具
F064
冲突系数K
Dempster规则冲突质量
冲突度量基线
Shafer 1976
F065
Jousselme距离
BPA间距离度量
证据相似度
Jousselme 2001
F066
Pignistic概率距离
BetP距离
冲突度量
Smets 2005
F067
Belief距离
信念函数距离
冲突度量
2018 IEEE TFS
F068
Deng熵
邓熵不确定性度量
证据不确定性
Deng 2016
F069
总不确定性(TU)
DST总不确定性
证据不确定性综合
Klir 1999
F070
非特异性
DST非特异性度量
证据不精确
Dubois 1985
F071
不一致度
证据间不一致度
冲突预检
2018 IEEE TFS
F072
冲突预处理
冲突超阈值降级
安全底线保护
DS22
F073
证据折扣
可靠度折扣证据
降低不可靠证据
Shafer 1976
F074
证据加权
可靠度加权BPA
先验知识融合
DS14
F075
证据归一化
归一化BPA
基础预处理
Dempster 1967
F076
证据平滑
指数平滑BPA
时序证据平滑
标准方法
F077
证据聚合
多源证据聚合
多传感器融合
DS17
F078
证据去噪
异常证据剔除
噪声证据过滤
DS13
4.4 不确定性量化(UQ)算子族
编号
算子名称
核心机制
架构角色
权威来源/工具
F079
区间扩展模糊集融合(Zadeh)
模糊集语言型不确定性
专家知识融合
1965 Zadeh; scikit-fuzzy
F080
粗糙集融合
边界不清晰概念模糊
分类与决策
1982 Pawlak; RoughSets.jl
F081
云模型融合
随机性+模糊性定性定量转换
不确定性AI
李德毅; cloudpy
F082
概率不确定性量化
概率分布传播
偶然不确定性
标准概率论
F083
认知不确定性量化
模型不确定性
认知不确定性
Kiureghian 2009
F084
贝叶斯不确定性量化
后验分布不确定性
贝叶斯UQ
Gelman 2013
F085
蒙特卡洛不确定性传播
随机采样传播
非线性UQ
Metropolis 1949
F086
多项式混沌展开UQ
正交多项式展开
高效UQ
Ghanem 2002; Chaospy
F087
全局敏感性分析
方差分解UQ
参数重要性
Sobol 2001; SALib
F088
区间分析
区间运算UQ
有界不确定性
Moore 1966
F089
模糊不确定性
隶属度函数UQ
模糊系统
Zadeh 1965
F090
可能性理论
可能性分布UQ
非概率不确定性
Zadeh 1978
F091
证据不确定性
DST不确定性
证据不确定性
Shafer 1976
F092
不精确概率
上下概率UQ
不精确不确定性
Walley 1991
F093
随机集理论
随机集UQ
广义不确定性
Matheron 1975
F094
凸集可能性(Credal Set)
凸集概率UQ
不精确概率
Levi 1980
F095
概率盒(P-Box)
概率分布区间
分布不确定性
Ferson 2002
F096
Dempster-Shafer结构
DST结构UQ
证据结构
Shafer 1976
F097
贝叶斯模型平均(BMA)
多模型后验平均
模型不确定性
Hoeting 1999
F098
深度集成不确定性
多NN预测不确定性
深度学习UQ
Lakshminarayanan 2017
4.5 群决策与专家共识
编号
算子名称
核心机制
架构角色
权威来源/工具
F099
Delphi法
多轮匿名反馈收敛专家共识
群决策经典方法
1950s RAND
F100
层次模糊综合评价
AHP+模糊综合
主观偏好多准则
模糊决策; ahpy+scikit-fuzzy
F101
名义小组法(NGT)
结构化头脑风暴
专家意见收集
Delbecq 1971
F102
头脑风暴
自由发散讨论
创意生成
Osborn 1953
F103
德尔菲法改进
实时Delphi/计算机Delphi
在线群决策
Gordon 2009
F104
共识模型
共识度量化+调整
群决策收敛
Herrera-Viedma 2002
F105
社会选择理论
投票/排序规则
集体决策
Arrow 1951
F106
博弈论
纳什均衡/演化博弈
策略交互
Nash 1950
F107
合作博弈
联盟/Shapley值
利益分配
Shapley 1953
F108
非合作博弈
纳什均衡
竞争决策
Nash 1951
F109
演化博弈
复制动态
长期策略演化
Smith 1982
F110
贝叶斯博弈
不完全信息博弈
类型不确定博弈
Harsanyi 1967
F111
机制设计
激励兼容机制
规则设计
Hurwicz 1972
F112
拍卖理论
拍卖机制设计
资源分配
Vickrey 1961
F113
匹配理论
稳定匹配
双边市场
Gale 1962
4.6 因果推断仲裁算子
编号
算子名称
核心机制
架构角色
权威来源/工具
F114
因果效应估计(IPTW)
逆概率加权估计因果效应
排除混杂因子
Rubin模型; DoWhy/CausalML
F115
反事实推理
计算"如果采取另一动作"结果
辅助决策仲裁
Pearl阶梯因果论; causal-learn
F116
结构因果模型(SCM)仲裁
因果图决策归因
判断真实驱动因素
Pearl; DoWhy/Tetrad
F117
DAG识别
有向无环图结构学习
因果发现
Spirtes 2000; causal-learn
F118
PC算法
条件独立性DAG学习
因果发现
Spirtes 1991
F119
FCI算法
潜在混杂DAG学习
隐变量因果发现
Spirtes 1995
F120
GES算法
贪婪等价搜索DAG
因果发现
Chickering 2002
F121
LiNGAM
线性非高斯因果发现
非高斯因果识别
Shimizu 2006
F122
ANM(加性噪声模型)
非线性因果发现
非线性因果识别
Hoyer 2009
F123
后门调整
后门准则调整
混杂因子控制
Pearl 1995
F124
前门调整
前门准则调整
未观测中介
Pearl 1995
F125
工具变量(IV)
工具变量法
内生性处理
Wright 1928
F126
断点回归(RDD)
断点回归设计
准实验因果
Thistlethwaite 1960
F127
双重差分(DID)
双重差分
政策评估因果
Card 1994
F128
合成控制法
合成对照组
反事实评估
Abadie 2003
F129
倾向得分匹配(PSM)
倾向得分匹配
观察研究因果
Rosenbaum 1983
F130
DoWhy
Python因果推断框架
因果效应估计
Microsoft; DoWhy
F131
CausalML
Python因果机器学习
因果效应估计
Uber; CausalML
F132
causal-learn
Python因果发现库
DAG结构学习
causal-learn
F133
Tetrad
因果发现Java工具
DAG/SEM学习
CMU; Tetrad
F134
EconML
Python经济计量因果
异质因果效应
Microsoft; EconML
F135
双机器学习(DML)
机器学习+因果
灵活因果效应
Chernozhukov 2018

五、M层（元认知层：集成与演进算子）
M层是系统的"反思者"，不直接参与单次决策，而是复盘所有历史决策。其核心属性为闭环演进与因果回溯。
5.1 集成学习框架
编号
算子名称
核心机制
架构角色
权威来源/工具
M001
Bagging
抽样构造数据子集训练差异化模型投票集成
P层专家委员会基座
Breiman 1996; sklearn
M002
Boosting
串行训练弱模型基于前一残差学习
委员会成员多样性增强
Freund 1997
M003
Stacking
元学习器学习"何时信任哪个委员"
F层元仲裁器选项
Wolpert 1992; MLxtend
M004
动态集成选择(DESlib)
针对每个新输入动态挑选最适合专家
非平稳环境决策
DESlib
M005
证据推理规则集成
证据推理规则作为集成结合策略
权重可靠度可解释集成
ENS4
M006
元启发式选择性集成
元启发式算法优化选择性集成
大规模专家委员自动化管理
ENS5
M007
MOGA优化Stacking
多目标GA优化Stacking模型选择
Pareto前沿模型选择
ENS12
M008
混合Stacking集成
SVM基学习器+NN元学习器
多模态数据源仲裁
ENS15
M009
HF-Stacking
空间异质性分区+特征选择Stacking
复杂聚类多源融合
ENS13
M010
在线集成分类算法
bagging/boosting/stacking在线版本
概念漂移+不平衡数据流
ENS2
M011
选择性集成(ENS6)
双错测度选择性集成
动态选择专家
ENS6
M012
随机森林
决策树集成+随机特征选择
高维特征基线检测器
Breiman 2001; sklearn
M013
AdaBoost
自适应提升加权弱学习器
分类提升
Freund 1997; sklearn
M014
Gradient Boosting
梯度提升决策树
回归/分类提升
Friedman 2001
M015
XGBoost
极端梯度提升
工业级GBDT
Chen 2016; XGBoost
M016
LightGBM
轻量梯度提升
大规模GBDT
Ke 2017; LightGBM
M017
CatBoost
类别特征梯度提升
类别特征GBDT
Prokhorenkova 2018
M018
Extra Trees
极端随机树
高方差降低
Geurts 2006
M019
投票集成(Voting)
多数/加权投票
简单集成基线
sklearn
M020
快照集成
单次训练多检查点集成
免费集成
Huang 2017
M021
深度集成(Deep Ensemble)
多NN独立训练集成
深度学习不确定性
Lakshminarayanan 2017
M022
MC Dropout
推理时Dropout模拟集成
贝叶斯NN近似
Gal 2016
M023
测试时增强(TTA)
测试时数据增强集成
提升推理鲁棒性
Wang 2019
M024
知识蒸馏
大模型→小模型蒸馏
模型压缩集成
Hinton 2015
M025
迁移集成
预训练模型微调集成
迁移学习集成
Pan 2010
M026
强化学习集成
多RL策略集成
RL策略鲁棒性
2019
M027
对抗训练集成
对抗样本训练集成
对抗鲁棒性
Madry 2018
M028
自训练(Self-Training)
伪标签自训练
半监督集成
Yarowsky 1995
M029
协同训练(Co-Training)
双视图协同训练
半监督集成
Blum 1998
M030
多任务学习集成
多任务共享表示集成
多任务集成
Caruana 1997
5.2 动态模型选择
编号
算子名称
核心机制
架构角色
权威来源/工具
M031
动态算法选择(DES)
根据数据特征实时选择P层算法
场景自适应
AutoML; DESlib
M032
元学习(Meta-Learning)
学习"何时用哪个模型"
模型选择元知识
Vilalta 2009
M033
AutoML
自动化机器学习流程
模型选择+超参数
Hutter 2019; auto-sklearn
M034
auto-sklearn
Python AutoML框架
自动模型选择
Feurer 2015
M035
TPOT
遗传编程AutoML
进化管道优化
Olson 2016
M036
H2O AutoML
H2O自动化ML
工业级AutoML
H2O.ai
M037
FLAML
快速轻量AutoML
高效AutoML
Wang 2021; FLAML
M038
Optuna集成
Optuna+集成
超参数+集成
Akiba 2019
M039
Ray Tune集成
分布式调优+集成
大规模集成
Liaw 2018
M040
NAS(神经架构搜索)
自动搜索NN架构
深度学习架构优化
Elsken 2019
M041
DARTS
可微架构搜索
高效NAS
Liu 2019
M042
ENAS
高效NAS参数共享
NAS加速
Pham 2018
M043
One-Shot NAS
一次训练NAS
NAS效率
Bender 2018
M044
ProxylessNAS
无代理NAS
直接搜索
Cai 2019
M045
AmoebaNet
进化NAS
进化架构搜索
Real 2019
5.3 系统演进规则
编号
算子名称
核心机制
架构角色
权威来源/工具
M046
MOD3因果演进
P/E/F三元0-1-2状态码合一驱动
核心闭环节奏系统有序演进
CIC xp架构
M047
概念漂移检测
检测数据分布变化
触发模型更新
Gama 2014
M048
ADWIN
自适应滑动窗口漂移检测
流数据漂移
Bifet 2007
M049
DDM
漂移检测方法
统计漂移检测
Gama 2004
M050
EDDM
早期漂移检测
改进DDM
Baena-Garcia 2006
M051
Page-Hinkley检验
序贯变点检测
渐进漂移检测
Page 1954
M052
KSWIN
Kolmogorov-Smirnov窗口
分布变化检测
Raab 2020
M053
在线学习
增量学习模型更新
流数据在线适应
Bifet 2018; River
M054
River
Python在线学习框架
流机器学习
Montiel 2021; River
M055
creme
Python在线学习(旧)
流机器学习
Halford 2019
M056
scikit-multiflow
多流学习框架
流数据学习
Read 2019
M057
持续学习
灾难性遗忘缓解
终身学习
Kirkpatrick 2017
M058
EWC(弹性权重整合)
Fisher信息正则化持续学习
遗忘缓解
Kirkpatrick 2017
M059
LwF(Learning without Forgetting)
知识蒸馏持续学习
旧任务知识保留
Li 2018
M060
回放(Replay)
经验回放持续学习
旧样本重放
Robins 1995
M061
元持续学习
元学习+持续学习
快速适应新任务
Javed 2019
M062
A-GEM(平均梯度情景记忆)
梯度投影持续学习
约束梯度不冲突
Chaudhry 2019
M063
iCaRL
增量分类与表示学习
类增量学习
Rebuffi 2017
M064
BiC(偏差校正)
增量学习偏差校正
类增量校正
Wu 2019
M065
PODNet(基于Paddle的增量)
Paddle增量学习
增量表示
Douillard 2020

六、C层（记忆层：设计原则）
C层不是算法，而是法则。它是PEF体系能够"有序幻想"的物理与逻辑根基。其设计不锁定任何具体数据库，只锁定不可协商的铁则。
6.1 完整性铁则（唯一映射）
每一条因果链都必须有一个唯一的chain_id，其必须由SHA256(Input_Fingerprint + Timestamp)生成。确保输入、输出、过程形成牢不可破的因果三元组。
6.2 不可变性铁则（追加锁定）
C层数据库只提供append(chain)接口，物理上锁死update和delete权限。任何情况下都不能对已落地的因果链记录做修改或删除。
6.3 可溯性铁则（全时不回绕）
所有时间戳字段必须使用64位类型，保证在产品最长运行时间内不发生回绕溢出。禁止使用32位作为时间戳主键。
6.4 有限性铁则（记忆硬截断）
C层数据库必须在编译期确定最大存储容量。达到容量上限时，执行硬截断策略，覆写或淘汰最低分记录。绝对禁止动态扩容，禁止磁盘换页。

七、算子入库与维护规则
7.1 四层质检标准
层级
检查内容
P层
能否输出人类可读的表达式树或规则集？支持约束/先验注入？
E层
是否支持LTL/STL规约？能否嵌入C/C++/Rust保证实时性？
F层
是否支持BPA分配与冲突度量？能否输出可审计的决策日志？
M层
是否支持动态权重与选择性集成？能否评估并反馈P/F权重调整信号？
7.2 新算子纳入流程
第一步——剥离外衣(Abstraction)：拿到最新SOTA模型，拆解为"输入→特征提取→输出"的架构模式。
第二步——三元映射(Mapping)：将特征提取部分映射为P层工具；将物理自洽校验部分映射为E层工具；将多源结果融合部分映射为F层工具。
第三步——白盒重构(Refactoring)：用P+E+F经典工具重新实现该架构，产出可审计、可追溯的白盒版本。
第四步——入库归档：通过P/E/F/M四层质检后，纳入对应层级，更新文献库与工具库索引。
7.3 新算子的接纳标准
1. 有持续commit的仓库；2. 有CI/测试、文档、示例；3. 能生成Pareto前沿或输出可读表达式；4. 算法原理清晰、边界明确，不存在黑箱。
7.4 入库硬性门槛
必须同时满足以下三项条件方可入库：
1. 公开可复现代码或完整数学推导；2. 顶会(CCF A/B)或一区期刊出处；3. 可映射到P/E/F/M单一分层。
以下内容一律剔除：纯理论证明无工程实现、哲学类比、自创概念、同架构微小调参变体（仅超参数/损失函数微调无核心数学创新的合并为一条）。工具/库不单独算作算子，仅作为配套来源不计入总数。
7.5 全球权威算子资料库索引
资料库名称
覆盖范围
ACM Digital Library / IEEE Xplore
计算机领域顶会顶刊论文全集，所有前沿算子的原始出处
Netlib / GAMS
全球最权威的数学算法仓库，经典优化、数值计算算子的标准实现
scikit-learn / SciPy生态
Python科学计算事实标准，经典机器学习、数值算子的工业级实现
JuliaHub算法库
高性能科学计算生态，前沿数值计算、PDE、动力系统算子
COIN-OR
运筹优化领域最大的开源算法库，线性/非线性/整数规划算子
NIST算法库
美国国家标准与技术研究院官方算法集，密码学、统计、计量领域基准
Open Algorithm (OpenALG)
欧盟官方开源算法平台，安全关键领域算法的标准实现与验证集
7.6 算子库统计
层级
算子数量
子类别数
P层（策略生成）
300
9
E层（边界监控）
180
5
F层（证据融合）
135
6
M层（集成演进）
65
3
C层（记忆铁则）
4条铁则
—
总计
680+ 算子
23 子类

八、算子分类附录
8.1 按算法范式分类
范式
所属层级
代表算子
数量
进化计算
P
GP/CGP/GEP/DE/PSO/ACO/SA/CMA-ES
45+
符号回归
P
PySR/Operon/AI-Feynman/SINDy/PhySR
20+
神经符号
P
DSR/SENSR/PSRN/NeuralSymbolic/FunSearch
15+
贝叶斯优化
P
EI/PI/UCB/Thompson/TPE/BoTorch
20+
凸优化
P
ADMM/ISTA/FISTA/SDP/IPM/Simplex
20+
整数规划
P
B&B/B&C/Gomory/列生成/Benders
10+
PDE数值解
P
FEM/FVM/谱方法/LBM/SPH/PINNs
20+
反问题
P
Tikhonov/LASSO/TV/MCMC/HMC/VI
20+
蒙特卡洛
P
MC/IS/LHS/QMC/PCE/Sobol
20+
流形优化
P
黎曼梯度/SO(3)/SE(3)/Grassmann
20+
运行时验证
E
LTL/STL/MITL/CTL/RTAMT/Reelay
60+
控制屏障
E
CBF/FCBF/HOCBF/SCBF/RCBF/NCBF
40+
Simplex/RTA
E
Simplex/NSA/DSA/RTA/TMR
25+
形式化验证
E
Z3/UPPAAL/NuSMV/SPIN/Coq/TLA+
30+
物理不变量
E
能量/动量/质量守恒/李雅普诺夫/诺特
15+
故障诊断
E
ARR/KF/EKF/PF/观测器/振动分析
30+
证据理论
F
D-S/DSmT/PCR/ER/主观逻辑/EDL
40+
多目标决策
F
NSGA/MOEA/MOPSO/PROMETHEE/TOPSIS/AHP
25+
因果推断
F
IPTW/SCM/DAG/PC/FCI/LiNGAM/DoWhy
22+
集成学习
M
Bagging/Boosting/Stacking/RF/XGBoost
30+
动态选择
M
DES/AutoML/NAS/DARTS/ENAS
15+
持续学习
M
EWC/LwF/Replay/iCaRL/BiC/PODNet
20+
8.2 按工程场景分类
场景
推荐层级
推荐算子
绝对安全(核反应堆/芯片熔断)
E+F
Simplex+Z3+DSmT
性能博弈(自动驾驶/机器人)
P+E+F
Beagle+FCBF+动态加权
探索发现(数学证明/药物)
P+E+F
TSGP+RV+基础D-S
工业控制(MPC/调度)
P+E
MPC+CBF+RV
信号处理(滤波/去噪)
P+E
KF/EKF+STL监控
故障诊断(传感器/执行器)
E+F
ARR+D-S融合
多传感器融合
F
D-S/DSmT/SPD
不确定性量化
F
MC/PCE/区间分析
因果分析
F
SCM/IPTW/DoWhy
流数据学习
M
River/ADWIN/在线学习
8.3 按工具/库分类
工具/库
语言
所属层级
覆盖算子
PySR
Python/Julia
P
符号回归
Operon
C++
P
符号回归
DEAP
Python
P
进化计算
pymoo
Python
P
多目标优化
BoTorch
Python
P
贝叶斯优化
CVXPY
Python
P
凸优化
Gurobi/CPLEX
C/Python
P
整数规划
FEniCSx
Python/C++
P
有限元PDE
DeepXDE
Python
P
PINNs
PyMC/Stan
Python/C++
P
贝叶斯推断/MCMC
RTAMT
Python
E
STL运行时监控
Z3
C++/Python
E
SMT求解
UPPAAL
Java
E
模型检验
Coq
OCaml
E
定理证明
refineCBF
Python
E
CBF工具箱
SOTERonROS
C++
E
Simplex/RTA
pyds/dstz
Python
F
D-S证据理论
DoWhy
Python
F
因果推断
DESlib
Python
M
动态集成选择
MLxtend
Python
M
Stacking集成
River
Python
M
在线学习
auto-sklearn
Python
M
AutoML


---
*PEF Architecture © 2026 banbanry (沈鹭). Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
