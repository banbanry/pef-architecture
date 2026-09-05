# PEF Dir Scanner — 目录遍历扫描归类引擎

> **设计规范 + 可运行代码 + 真实数据验证 + 篡改检测演示**
> 作者: banbanry (沈鹭) · MIT License

---

## 1. 设计规范（Design Spec）

### 1.1 目标

对任意目录下的文档做 **token 级深度遍历 → PEF 三元拆解 → 知识库分类映射**，产出可审计、可复算的归类结果。这是 PEF 三级闭环引擎中"① 内生循环（token深挖）"的通用化——不再依赖单一语料，可扫任意目录。

### 1.2 处理流水线（五步）

```
Step 1 遍历目录收集文档（docx/doc/pdf/md/txt/docm/pptx）
Step 2 提取全文（python-docx / fitz / zipfile 正则 / python-pptx）
Step 3 token 级切块（600字/重叠120）→ PEF 三元信号打分 → 分级(S/A/B/C)
Step 4 文档级 PEF 三元摘要 + 知识库 10 节点分类映射 + 8层经验整理映射
Step 5 输出归类结果 JSON + 校对报告（对比已有分类索引）
```

### 1.3 PEF 三元信号词典

| 元 | 含义 | 信号词示例 |
|---|---|---|
| **P** | 主体：谁在做 | 本架构/本系统/引擎/模型/算子/探针/AI/大模型/硬件/审计/CLE/CIC |
| **E** | 变量：用什么做 | 变量/输入/输出/参数/状态/阈值/偏差/漂移/锚/π/哈希/时序/E_in/E_out/熵/势差 |
| **F** | 结果：得到什么 | 结果/结论/裁决/判定/PASS/FAIL/熔断/验证/闭环/交付/审计轨迹/证据 |
| **M** | 机制：体系特征 | 公理/铁则/熔断/审计/锚定/隔离/时序/因果/不可伪/MOD3/拜占庭/影子图/第一性原理 |

### 1.4 分级标准（S/A/B/C）

```
S: 强机制信号(M≥3) 或 强结论信号(F≥6且total≥10) — 核心结论
A: total≥6     — 机制描述
B: total≥2     — 过程例子
C: 其余        — 噪声
```

### 1.5 分类映射双轨

- **文件名强规则优先**（最高置信 99）：专利/交底书→知识产权；提示词→提示词工程；物流/民爆→工程应用；算子→算子库；白皮书/规范→理论与设计
- **内容信号兜底**：KB_CATEGORIES 词典命中打分取最高

### 1.6 可复算性

每份文档输出：chars / n_chunks / level / levels / pef四元分 / dom_pef / kb_category / exp_layer / core(核心句) / keywords。所有分类决策可追溯到信号词命中。

---

## 2. 可运行代码

`pef_dir_scanner.py` — 单文件、零外部依赖（文本提取层可选依赖 python-docx/fitz/python-pptx，缺失时自动降级 zipfile 正则）。

```bash
# 默认扫描 经验整理 + 902 批次
python pef_dir_scanner.py

# 输出
#   pef_scan_result.json  — 全量归类结果（196份/191有效）
#   pef_scan_report.md    — 可读报告（分类分布/三元分布/分级/逐份清单/校对）
```

---

## 3. 真实数据验证（2026-09-05 实扫）

**输入**：`D:\WorkBuddy\经验整理`（143份）+ `D:\WorkBuddy\902`（53份）

**结果**：

| 维度 | 结果 |
|---|---|
| 扫描文档 | 196 份 |
| 有效提取 | 191 份（5 份 pptx 无法提取，已记录） |
| 总字符 | 5,309,743（531 万字） |
| PEF 三元主导 | E(变量)=123 · P(主体)=61 · F(结果)=7 |
| 文档分级 | S=172 · A=13 · B=6 · C=0 |
| 知识库分类 | 02-理论与设计=80 · 03-测试与验证=76 · 08-工程案例=22 · 07=7 · 01=5 · 09=1 |

**校对发现**（vs 人工分类 docs_data.json）：
- 13 份文件名强信号与人工分类明显冲突（如 `PEF算子库.docx` 被归基础架构层而非工程应用层；`PEF-MOD3 提示词工程...` 应归提示词层）→ 详见 `review_list.json`

---

## 4. 篡改检测演示

扫描结果本身可被 PEF 审计链保护——对 `pef_scan_result.json` 的每条记录做哈希链，任何一条被篡改都会导致整链断裂：

```python
import json, hashlib

def build_chain(records):
    prev = 'GENESIS'
    chain = []
    for r in records:
        body = json.dumps(r, sort_keys=True, ensure_ascii=False).encode()
        h = hashlib.sha256(body + prev.encode()).hexdigest()[:16]
        chain.append({'name': r['name'], 'hash': h, 'prev': prev[:16]})
        prev = h
    return chain

records = json.load(open('pef_scan_result.json', encoding='utf-8'))
chain = build_chain(records)
print(f"审计链: {len(chain)} 条记录，尾哈希 {chain[-1]['hash']}")
# 篡改任一条 → 重新计算链尾哈希 ≠ 原尾哈希 → 检测
```

---

## 5. 目录结构

```
pef-dir-scanner/
├── README.md              # 本文件（设计规范+验证+演示）
├── pef_dir_scanner.py     # 可运行扫描引擎（单文件，第一遍：经验整理+902）
├── pef_scan_result.json   # 实测输出（196份归类）
├── pef_scan_report.md     # 实测报告
├── review_list.json       # 13份校对冲突清单
├── pefmod_scanner.py      # 第二遍：PEFMOD 目录全量扫描（去重版）
└── pefmod_scan_result.json # PEFMOD 实测输出（1200份 / 2452万字）
```

---

## 6. 第二遍实测：PEFMOD 目录（2026-09-05）

**输入**：`D:\WorkBuddy\PEFMOD`（PEF资料库 863 + 原始素材独有 241 + 记忆体/卡片/开发 110）

**结果**：

| 维度 | 结果 |
|---|---|
| 待扫描 | 1214 份（去重后） |
| 有效提取 | 1200 份 |
| 总字符 | 24,523,828（2452 万字） |
| 耗时 | 140 秒 |
| PEF 三元主导 | E=756 · P=347 · F=97 |
| 文档分级 | S=1000 · A=136 · B=63 · C=1 |
| 10节点分类 | 测试验证427 · 理论设计355 · 经验整理150 · 工程案例106 · 算子63 · AI研究48 · 版本27 · 原始归档13 · 记忆体8 |

**去重策略**：PEF资料库（整理版）优先，原始素材只扫指纹独有部分（674 份重复被跳过）。

