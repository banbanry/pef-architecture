# -*- coding: utf-8 -*-
"""
PEF 精华过滤评分器（Anti-屎山 / 防数据污染）
===========================================
对扫描结果打分分级，过滤：草稿、残缺、假设/AI幻觉、死路、冗余堆叠。

评分维度（每文档）：
  base_level  : S=10 / A=7 / B=4 / C=1         — 机制信号强度
  mech        : M机制词命中数                    — PEF体系特征
  completeness: 字符数完整度（<500残篇, <2000偏短）
  draft_flag  : 文件名草稿特征（草稿/初稿/临时/备份/副本/未命名/新建/old/旧版/tmp/测试/示例/demo）
  halluc      : 假设/幻觉词密度（假设/推测/可能/也许/大概/或许/据说/猜测/不确定/大概/应该）
  dup         : 重复内容（与同组文档内容哈希相似）
  知识库价值   : kb_score + core句可读性

四档输出：
  A 精华   → 可入知识库（S级+机制强+完整）
  B 可留   → 参考价值（A级或中等）
  C 待清理 → 低质/偏短/草稿特征
  D 疑似垃圾 → 建议隔离（残篇/幻觉词密集/纯草稿）
"""
import json, re, hashlib, os
from collections import Counter, defaultdict

scan = json.load(open(r'D:\WorkBuddy\pefmod_scan_result.json', encoding='utf-8'))
ok = [r for r in scan if r.get('status') == 'OK']

DRAFT_RE = re.compile(r'草稿|初稿|初版|临时|备份|副本|未命名|新建|旧版|old|tmp|测试|示例|demo|备份|拷贝|copy|改\d|_\d{4}|_v\d|V\d+_草|草稿箱', re.I)
HALLUC_RE = re.compile(r'假设|推测|可能|也许|大概|或许|据说|猜测|不确定|应该|猜想|臆测|幻|hallucin', re.I)

def quality_score(r):
    """返回 (总分, 各维度, 档位, 原因)"""
    level_score = {'S': 10, 'A': 7, 'B': 4, 'C': 1}[r.get('level', 'C')]
    pef = r.get('pef', {})
    mech = pef.get('M', 0)
    chars = r.get('chars', 0)
    name = r.get('name', '')

    # 完整度
    if chars < 300:
        comp = -5; comp_tag = '残篇(<300字)'
    elif chars < 800:
        comp = -3; comp_tag = '偏短(<800字)'
    elif chars < 2000:
        comp = -1; comp_tag = '较短'
    else:
        comp = 0; comp_tag = '完整'

    # 草稿特征
    draft = -4 if DRAFT_RE.search(name) else 0

    # 幻觉词密度（取前2000字采样）
    sample = ''
    core = r.get('core') or []
    if core:
        sample = ' '.join(core)
    hall_cnt = len(HALLUC_RE.findall(sample))
    hall = -min(3, hall_cnt)

    # 机制强度加成
    mech_bonus = min(4, mech // 3)

    total = level_score + mech_bonus + comp + draft + hall

    # 档位判定
    reasons = []
    if total >= 12:
        grade = 'A'
        reasons.append('高价值')
    elif total >= 8:
        grade = 'B'
        reasons.append('参考')
    elif total >= 4:
        grade = 'C'
        reasons.append('待清理')
    else:
        grade = 'D'
        reasons.append('疑似垃圾')
    if comp < 0:
        reasons.append(comp_tag)
    if draft < 0:
        reasons.append('草稿特征')
    if hall < 0:
        reasons.append(f'幻觉词x{hall_cnt}')
    if mech >= 5:
        reasons.append(f'机制强M{mech}')
    if not reasons:
        reasons.append('普通')

    return {
        'total': total, 'level': r.get('level'), 'mech': mech,
        'comp': comp, 'draft': draft, 'hall': hall,
        'grade': grade, 'reasons': reasons,
    }

# 重复检测（用 core 句 + 文件名+大小指纹）
def content_fingerprint(r):
    core = (r.get('core') or [])
    return hashlib.md5('|'.join(core).encode()).hexdigest()[:16] if core else ''

fp_map = defaultdict(list)
for r in ok:
    fp = content_fingerprint(r)
    if fp:
        fp_map[fp].append(r)

dups = []
for fp, items in fp_map.items():
    if len(items) >= 2:
        for a in items:
            for b in items:
                if a['name'] != b['name'] and a['rel'] < b['rel']:
                    dups.append({
                        'a': a['name'], 'a_rel': a['rel'],
                        'b': b['name'], 'b_rel': b['rel'],
                        'fp': fp, 'chars_a': a['chars'], 'chars_b': b['chars'],
                    })

# 汇总
results = []
for r in ok:
    q = quality_score(r)
    results.append({**r, 'quality': q})

grade_cnt = Counter(q['grade'] for r in results for q in [r['quality']])
print(f"总扫描: {len(ok)} 份")
print(f"精华分级: {dict(grade_cnt)}")
print(f"重复对: {len(dups)}")

# 保存
with open(r'D:\WorkBuddy\pefmod_quality.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
with open(r'D:\WorkBuddy\pefmod_dups.json', 'w', encoding='utf-8') as f:
    json.dump(dups, f, ensure_ascii=False, indent=1)
print("✅ 已保存 pefmod_quality.json + pefmod_dups.json")

# 抽样输出
print("\n=== A精华 抽样(前15) ===")
for r in [x for x in results if x['quality']['grade'] == 'A'][:15]:
    print(f"  [{r['quality']['total']}] {r['name'][:40]} | {r['quality']['reasons'][:2]}")
print("\n=== D疑似垃圾 抽样(前10) ===")
for r in [x for x in results if x['quality']['grade'] == 'D'][:10]:
    print(f"  [{r['quality']['total']}] {r['name'][:40]} chars={r['chars']} | {r['quality']['reasons']}")
