# -*- coding: utf-8 -*-
"""产品详情页 —— 依据《产品详情V1.2》重建
产品概述 → 体系总纲 → 差异化优势 → 体系架构 → 分层能力详解 → 典型场景 → 交付物
分层锚点：infra / fusion / cognition / embodied / market / security
"""
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ---------- 差异化优势 ----------
DIFF = [
 ("空天地一体化数据源","覆盖高、低轨卫星及 44 个全球地面站，实现天基数据直达业务。"),
 ("全链路闭环","从数据获取、治理、认知决策到终端执行，无需拼接多家供应商。"),
 ("国产化全栈适配","从算力底座到 AI 模型，满足自主可控要求。"),
 ("智能体驱动","多智能体任务编排与自我进化，让系统越用越聪明。"),
]

# ---------- 分层能力详解 ----------
LAYERS = [
 ("infra","基础设施层","边云协同与智算底座",
  "提供国产化、高性能的算力与数据存储支持，确保底层稳固。",
  [("智算集群","支持国产全栈适配，提供算力池化与统一资源管理","算力资源利用率提升 30%+，支持弹性扩容"),
   ("高速互联","RDMA 高速互联网络，分布式并行存储","训练效率提升 50%，存储吞吐达 TB 级"),
   ("边云协同","支持云端训练与边缘端推理的无缝协同","边缘推理延迟 ≤50ms，带宽成本降低 40%")]),
 ("fusion","数据融合层","空天地数据融合",
  "解决“数据从哪来”的问题，实现多源异构数据的快速获取、治理与融合。",
  [("天元·灵观","天基数据获取。便捷获取卫星数据，AI 简化任务需求，星地协同智能指挥。覆盖高、低轨卫星及 44 个全球地面站","卫星数据获取周期从“天级”缩短至“小时级”"),
   ("天元·灵数","数据治理与融合。智能数据治理，多源数据融合（卫星遥感、无人机、物联网），沉淀 20+ 数据集，拥有 50+ 自动化管道","数据治理人工干预减少 60%，多源数据融合效率提升 3 倍"),
   ("空天地一体化网络","通信全流程保障，确保数据传输的高带宽与低延迟。支持星地链路、5G/专网、边缘组网等多种通信方式自适应切换","保障数据链路高带宽与低延迟")]),
 ("cognition","认知决策层","认知计算与智能决策",
  "解决“数据怎么用”的问题，通过 AI 让机器读懂业务，进行深度研判，并生产可复用的本体、模型与智能体。",
  [("天元·灵语","本体建模。自动本体建模，Skill 级业务操作，支持 200+ AI 动作；构建行业知识建模、时空本体建模、图谱推理与因果分析","业务人员无需编程即可调用 AI 能力"),
   ("天元·灵炼","模型工厂。数据在线 AI 标注，大模型后训练，完成 7 项应用模型，支持增量训练与联邦学习","模型迭代周期从“月级”缩短至“周级”"),
   ("天元·灵智","智能体工厂。提供智能体开发、编排与运行能力，支持多智能体任务编排与自我进化","智能体开发效率提升，业务场景快速落地"),
   ("认知计算引擎","智能体编排框架。能够自动调度数据、模型、智能体与 Skill，实现信息服务的流程闭环","为上层应用提供统一的能力调度与编排支撑，实现端到端流程闭环")]),
 ("embodied","行动执行层","具身智能 AI 调度",
  "解决“指令怎么执行”的问题，实现无人设备的智能化调度与管控。",
  [("天元·灵动","具身智能调度。覆盖无人机、无人车、机器狗等多类具身设备；统一调度，链路自适应下发；具备视觉增强，支持小、中、大覆盖半径（作业面积 5m²–100km²）的精准作业","多设备协同效率提升 50%，调度响应 ≤1s；作业精度提升至厘米级，人力成本降低 70%")]),
 ("market","数智市集","天元·灵集",
  "作为数智能力的集散与流通平台，连接能力供给与业务消费。",
  [("数智资产广场","汇聚数据集、本体、算法、模型等数字资产，支持上架、检索与复用。","—"),
   ("智能体及技能广场","汇聚智能体、Skill、Workflow 等，支持按需调用。","—"),
   ("天元·信息服务助手","行业信息服务的统一入口，提供通用智能问答、记忆、多轮对话等问答能力，可通过认知计算引擎在线对数智市集中的各类资产进行体验与交互。","—")]),
 ("security","安全支撑体系","全栈安全合规",
  "横向贯穿所有层级，提供全流程安全保障。",
  [("身份与访问控制","统一身份，分级授权。","—"),
   ("数据安全与隐私","加密脱敏，数据不出域，密级流转。","—"),
   ("AI 安全治理","抗注入，模型可信赖，对抗防护。","—"),
   ("行为审计与溯源","全链路审计，操作可追溯。","—")]),
]

def layer_blocks():
    out=[]
    for i,(a,ln,name,core,mods) in enumerate(LAYERS):
        rows = "".join(
          '<tr><td style="color:#0F3D75;font-weight:700">%s</td><td>%s</td><td style="color:#0F3D75">%s</td></tr>'
          % (m[0], m[1], m[2]) for m in mods)
        head3 = '<th>模块</th><th>内容要点</th><th>客户价值</th>' if mods[0][2] != "—" else '<th>模块</th><th>说明</th>'
        body  = rows if mods[0][2] != "—" else "".join(
          '<tr><td style="color:#0F3D75;font-weight:700">%s</td><td colspan="2">%s</td></tr>' % (m[0], m[1]) for m in mods)
        out.append("""
    <div id="%s" class="lyr rv">
      <div class="lyr-h"><span class="lyr-n">%d</span>
        <div><div class="lyr-t">%s</div><h3>%s</h3></div></div>
      <p class="lyr-core">%s</p>
      <div class="tbl-wrap"><table class="tbl">
        <thead><tr>%s</tr></thead>
        <tbody>%s</tbody></table></div>
    </div>""" % (a, i+1, ln, name, core, head3, body))
    return "".join(out)

SCENES = [
 ("边防预警与研判处置","多元信息融合的态势感知、预警发现、研判处置，无人装备协同闭环。"),
 ("海洋污染溯源分析","油膜识别与起始点反演，输出嫌疑船舶排序及证据链。"),
 ("灾害应急对比分析","自然语言拉取灾前灾后影像，建筑物损毁、水体淹没范围对比。"),
]

pd = """
<div class="banner pad"><div class="banner-in">
  <div style="display:flex;gap:40px;flex-wrap:wrap;align-items:flex-start">
    <div style="flex:1;min-width:300px">
      <span style="display:inline-block;background:#00A0E9;color:#1A1A1A;font-size:12px;font-weight:700;
        padding:4px 12px;border-radius:3px;letter-spacing:1px;margin-bottom:14px">一站式场景化数智平台</span>
      <h1 style="font-size:38px">天元平台<br>TianYuan Platform</h1>
      <p class="lead">融合人工智能与智能体技术，实现从空天地数据融合到认知决策、再到行动执行的全链路闭环智能系统，
        为客户提供“感、通、算、用”一体化的数智化解决方案。</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px">
        <a class="btn btn-p btn-lg" href="contact.html">申请试用 / 演示</a>
        <a class="btn btn-o btn-lg" href="#doc">下载产品资料</a>
      </div>
      <div class="spec">
        <div><span>1+3+1</span><small>+1+N 体系架构</small></div>
        <div><span>44</span><small>全球地面站</small></div>
        <div><span>≤50ms</span><small>边缘推理延迟</small></div>
        <div><span>国产全栈</span><small>自主可控</small></div>
      </div>
    </div>
    <div style="flex:0 0 380px;min-width:280px;background:rgba(255,255,255,.08);
      border:1px solid rgba(255,255,255,.22);border-radius:8px;height:250px;
      display:flex;align-items:center;justify-content:center;color:#CFDCEA;font-size:13px">
      【平台渲染图 / 演示视频占位 · 待补充】
    </div>
  </div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> /
  <a href="products.html">产品与能力</a> / 天元平台</div></div>

<!-- 体系总纲 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">OVERVIEW</div><h2>体系总纲</h2></div>
    <div class="rv" style="background:#F5F8FB;border:1px solid #B4C7E7;border-radius:8px;padding:24px 26px">
      <p style="font-size:17px;color:#0F3D75;font-weight:700;line-height:2">
        1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用</p>
      <ul style="margin-top:14px;font-size:14px;color:#5C6670;line-height:2.1">
        <li><b style="color:#0F3D75">1 个底座</b>：天元·智算底座</li>
        <li><b style="color:#0F3D75">3 大核心引擎</b>：空天地数据融合引擎 · 认知计算与决策引擎 · 具身智能行动执行引擎</li>
        <li><b style="color:#0F3D75">1 个数智市集</b>：天元·灵集（数智资产广场 + 智能体及技能广场 + 天元·信息服务助手）</li>
        <li><b style="color:#0F3D75">1 个安全体系</b>：全栈安全合规（横向贯穿）</li>
        <li><b style="color:#0F3D75">N 个行业应用</b>：应急减灾 · 边防管控 · 海洋应用 · 开源情报等</li>
      </ul>
      <p style="margin-top:14px;font-size:14px;color:#5C6670;line-height:1.9">
        构建从卫星原始数据获取到行动指令下达的全链路闭环系统。</p>
    </div>
  </div>
</section>

<!-- 差异化优势 -->
<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">WHY TIANYUAN</div><h2>差异化优势</h2>
      <p>与通用云平台不同，天元的四个核心差异。</p></div>
    <div class="grid4 rv">
      __DIFF__
    </div>
  </div>
</section>

<!-- 体系架构图 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">ARCHITECTURE</div><h2>体系架构</h2>
      <p>自上而下：应用层 → 数智市集 → 三大核心引擎 → 基础设施层，安全体系横向贯穿。</p></div>
    <div class="rv" style="background:#0C315E;border-radius:8px;padding:22px 18px;overflow-x:auto">
      <pre style="color:#CFDCEA;font-family:Consolas,'Courier New',monospace;font-size:12px;
        line-height:1.65;margin:0;white-space:pre">
┌──────────────────────────────────────────────────────────────────────────────────┐
│  应用层      应急减灾  │ 边防管控 │ 海洋应用 │ 开源情报 │ 更多行业              │
├──────────────────────────────────────────────────────────────────────────────────┤
│  数智市集 · 天元·灵集    数智资产广场 │ 智能体及技能广场 │ 天元·信息服务助手      │
├──────────────────────────────────────────────────────────────────────────────────┤
│  三大核心引擎                                                                     │
│  ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐     │
│  │ 空天地数据融合引擎    │ │ 认知计算与决策引擎    │ │ 具身智能行动执行引擎  │     │
│  │ · 天元·灵观           │ │ · 天元·灵语           │ │ · 天元·灵动           │     │
│  │ · 天元·灵数           │ │ · 天元·灵炼           │ │                      │     │
│  │ · 空天地一体化网络    │ │ · 天元·灵智           │ │                      │     │
│  │                       │ │ · 认知计算引擎        │ │                      │     │
│  └──────────────────────┘ └──────────────────────┘ └──────────────────────┘     │
├──────────────────────────────────────────────────────────────────────────────────┤
│  基础设施层 · 天元·智算底座   智算集群 / 高速互联 / 边云协同，国产化全栈适配       │
├──────────────────────────────────────────────────────────────────────────────────┤
│  全栈安全合规体系 —— 身份与访问控制 · 数据安全与隐私 · AI 安全治理 · 行为审计      │
└──────────────────────────────────────────────────────────────────────────────────┘</pre>
    </div>
    <div style="text-align:center;margin-top:18px">
      <a class="btn btn-s" href="products.html#arch">查看可交互架构图 &#8594;</a></div>
  </div>
</section>

<!-- 分层能力详解 -->
<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CAPABILITY DETAIL</div><h2>分层能力详解</h2>
      <p>从基础设施到行动执行的完整能力分层。</p></div>
    __LAYERS__
    <div class="note rv"><b>复核提示：</b>本章全部“客户价值”指标来源于《产品详情V1》设计口径，
      正式对外发布前需由产品部门复核基准与来源。</div>
  </div>
</section>

<!-- 典型场景 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">SCENARIOS</div><h2>典型应用场景</h2></div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th>场景</th><th>说明</th><th>关联解决方案</th></tr></thead>
      <tbody>
        __SCENES__
      </tbody></table></div>
  </div>
</section>

<!-- 交付物 -->
<section class="sec alt" id="doc">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">DOCUMENTS</div><h2>交付物 / 文档清单</h2></div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th>文档</th><th>形式</th><th>获取方式</th></tr></thead>
      <tbody>
        <tr><td style="color:#0F3D75;font-weight:700">平台白皮书</td><td>PDF · 约 8MB</td>
          <td><a href="contact.html" style="color:#00608C;text-decoration:underline">留资下载</a></td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">产品规格书</td><td>PDF · 约 3MB</td>
          <td><a href="contact.html" style="color:#00608C;text-decoration:underline">留资下载</a></td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">API 文档</td><td>在线文档</td>
          <td><a href="contact.html" style="color:#00608C;text-decoration:underline">申请权限</a></td></tr>
      </tbody></table></div>
    <div class="note rv"><b>待补充：</b>官网未标注具体版本号与发布日期；
      文档下载需留资（姓名 + 电话），文件大小与版本信息在正式发布前补充。</div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2>想了解天元平台能否解决你的问题？</h2>
    <p>留下姓名与电话，我们的方案顾问将在工作日内与您联系。</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-p btn-lg" href="contact.html">申请产品演示</a>
      <a class="btn btn-o btn-lg" href="products.html">返回产品与能力</a></div></div>
</section>
"""

pd = pd.replace("__DIFF__", "\n      ".join(
  '<div class="card"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>' % (d[0][:2], d[0], d[1]) for d in DIFF))
pd = pd.replace("__LAYERS__", layer_blocks())
pd = pd.replace("__SCENES__", "\n        ".join(
  '<tr><td style="color:#0F3D75;font-weight:700">%s</td><td>%s</td>'
  '<td><a href="solutions.html" style="color:#00608C;text-decoration:underline">查看方案 &#8594;</a></td></tr>'
  % (s[0], s[1]) for s in SCENES))

EXTRA = """
<style>
.lyr{background:#fff;border:1px solid #B4C7E7;border-radius:8px;padding:22px 24px;margin-bottom:18px}
.lyr-h{display:flex;gap:14px;align-items:center;margin-bottom:10px}
.lyr-n{flex:0 0 34px;height:34px;border-radius:50%;background:#0F3D75;color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700}
.lyr-t{font-size:12px;color:#00A0E9;font-weight:700;letter-spacing:1px}
.lyr h3{font-size:18px;color:#0F3D75;margin:0;font-weight:700}
.lyr-core{font-size:13.5px;color:#5C6670;line-height:1.9;margin-bottom:14px}
</style>
"""

w("product-detail.html", page("天元平台 · 一站式场景化数智平台 | 产品详情",
  "天元平台：1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用，实现从空天地数据融合到认知决策、再到行动执行的全链路闭环。",
  "products", pd, extra_head=EXTRA))
