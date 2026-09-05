# -*- coding: utf-8 -*-
"""
PEFMOD 目录全量扫描（第二遍）
================================
复用 pef_dir_scanner 引擎，对 PEFMOD 目录扫描：
  - PEF资料库 863 文档（去重优先）
  - 原始素材 独有 241 文档
  - PEF记忆体 54 + 知识卡片 47 + 记忆层开发 9
去重规则：PEF资料库优先（整理版），原始素材只扫独有部分。
"""
import os, re, json, sys, time

# 复用扫描引擎模块
sys.path.insert(0, r'D:\WorkBuddy')
from pef_dir_scanner import (extract_text, pef_score, classify_block,
                             token_chunk, map_kb_category_filename,
                             map_kb_category, map_exp_layer)
import hashlib
from collections import Counter

def scan_one(path, rel):
    """扫描单个文档，返回结果 dict 或 None"""
    text = extract_text(path)
    if not text or len(text) < 30:
        return None
    chunks = [c for c in token_chunk(text) if len(c) >= 30]
    blocks = []
    for ci, chunk in enumerate(chunks):
        scores = pef_score(chunk)
        blocks.append({'ci': ci, 'text': chunk, 'scores': scores,
                       'level': classify_block(scores),
                       'hash': hashlib.md5(chunk.encode()).hexdigest()[:8]})
    lv = Counter(b['level'] for b in blocks)
    sa = [b for b in blocks if b['level'] in ('S', 'A')]
    p_sum = sum(b['scores']['P'] for b in sa)
    e_sum = sum(b['scores']['E'] for b in sa)
    f_sum = sum(b['scores']['F'] for b in sa)
    m_sum = sum(b['scores']['M'] for b in sa)
    doc_level = ('S' if any(b['level'] == 'S' for b in blocks) else
                 'A' if sa else 'B' if blocks else 'C')
    kb_from_name, exp_from_name = map_kb_category_filename(os.path.basename(path))
    if kb_from_name:
        kb_cat, kb_score = kb_from_name, 99
        exp_layer, exp_score = exp_from_name, 99
    else:
        kb_cat, kb_score = map_kb_category(text)
        exp_layer, exp_score = map_exp_layer(text)
    core_sents = []
    for b in sorted(sa, key=lambda x: -x['scores']['total'])[:4]:
        sents = re.split(r'(?<=[。！？!?])', b['text'])
        best = max(sents, key=lambda s: pef_score(s)['total'], default='')
        if best and len(best) > 20:
            core_sents.append(best.strip()[:150])
    toks = Counter()
    for b in sa[:8]:
        for w in ['公理', '算子', '探针', '物流', '民爆', '提示词', '专利', 'PIMEM',
                  'CLE', 'CIC', 'MOD3', 'π', '测试', '验证', '方法论', '硬件']:
            if w.lower() in b['text'].lower():
                toks[w] += 1
    return {
        'name': os.path.basename(path), 'rel': rel, 'ext': os.path.splitext(path)[1].lower(),
        'chars': len(text), 'n_chunks': len(blocks),
        'level': doc_level, 'levels': dict(lv),
        'pef': {'P': p_sum, 'E': e_sum, 'F': f_sum, 'M': m_sum},
        'dom_pef': max(['P', 'E', 'F'], key=lambda k: {'P': p_sum, 'E': e_sum, 'F': f_sum}[k]),
        'kb_category': kb_cat, 'kb_score': kb_score,
        'exp_layer': exp_layer, 'exp_score': exp_score,
        'core': core_sents[:3],
        'keywords': [k for k, v in toks.most_common(8) if v > 0][:8],
        'status': 'OK',
    }

def collect_docs():
    """收集去重后的文档列表"""
    base = r'D:\WorkBuddy\PEFMOD'
    # 先收集原始素材独有（指纹 = 文件名+大小）
    def fingerprint(path):
        return (os.path.basename(path), os.path.getsize(path))
    lib_fps = set()
    lib_files = []
    for dirpath, _, filenames in os.walk(os.path.join(base, 'PEF资料库')):
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext in ('.docx', '.doc', '.pdf', '.md', '.txt', '.docm'):
                full = os.path.join(dirpath, fn)
                lib_files.append(full)
                lib_fps.add(fingerprint(full))
    raw_only = []
    for dirpath, _, filenames in os.walk(os.path.join(base, '原始素材')):
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext in ('.docx', '.doc', '.pdf', '.md', '.txt', '.docm'):
                full = os.path.join(dirpath, fn)
                if fingerprint(full) not in lib_fps:
                    raw_only.append(full)
    other = []
    for sub in ['PEF记忆体', '知识卡片', '记忆层开发']:
        for dirpath, _, filenames in os.walk(os.path.join(base, sub)):
            for fn in filenames:
                ext = os.path.splitext(fn)[1].lower()
                if ext in ('.docx', '.doc', '.pdf', '.md', '.txt', '.docm'):
                    other.append(os.path.join(dirpath, fn))
    return lib_files, raw_only, other

if __name__ == '__main__':
    t0 = time.time()
    print("===== PEFMOD 目录全量扫描 =====")
    lib_files, raw_only, other = collect_docs()
    print(f"PEF资料库: {len(lib_files)} | 原始素材独有: {len(raw_only)} | 其他(记忆体/卡片/开发): {len(other)}")
    print(f"待扫描总数: {len(lib_files) + len(raw_only) + len(other)}")

    results = []
    all_files = [('PEF资料库', f) for f in lib_files] + \
                [('原始素材', f) for f in raw_only] + \
                [('其他', f) for f in other]
    for i, (grp, path) in enumerate(all_files):
        rel = os.path.relpath(path, r'D:\WorkBuddy\PEFMOD')
        r = scan_one(path, rel)
        if r:
            r['group'] = grp
            results.append(r)
        if (i + 1) % 100 == 0:
            print(f"  [{i+1}/{len(all_files)}] 完成, 有效 {len(results)}")
            with open(r'D:\WorkBuddy\pefmod_scan_partial.json', 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False)

    with open(r'D:\WorkBuddy\pefmod_scan_result.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False)
    total_chars = sum(r['chars'] for r in results)
    print(f"\n✅ 完成: {len(results)} 份有效, {total_chars:,} 字符, 耗时 {time.time()-t0:.0f}s")
