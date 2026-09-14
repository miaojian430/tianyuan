# -*- coding: utf-8 -*-
"""产品与能力页 —— 依据《产品详情V1.2》+《引擎V1.2》重建
体系总纲：1 底座 + 3 大核心引擎 + 1 数智市集 + 1 安全体系 + N 行业应用
引擎能力并入本页（#engine），不单独建一级菜单
"""
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ---------- 数据：三大核心引擎 ----------
ENGINES = [
 ("空天地数据融合引擎", "数据从哪来",
  "以空天地一体化数据源为核心，快速获取、治理与融合卫星遥感、无人机、物联网等多源数据，"
  "并通过星地链路、5G/专网、边缘组网自适应切换保障传输，让天基数据直达业务。",
  [("天元·灵观","天基数据获取","便捷获取卫星数据，AI 简化任务需求，星地协同智能指挥。覆盖高、低轨卫星及 44 个全球地面站","卫星数据获取周期从“天级”缩短至“小时级”"),
   ("天元·灵数","数据治理与融合","智能数据治理，多源数据融合（卫星遥感、无人机、物联网），沉淀 20+ 数据集，拥有 50+ 自动化管道","数据治理人工干预减少 60%，多源数据融合效率提升 3 倍"),
   ("空天地一体化网络","通信全流程保障","确保数据传输的高带宽与低延迟。支持星地链路、5G/专网、边缘组网等多种通信方式自适应切换","保障数据链路稳定可靠")]),
 ("认知计算与决策引擎", "数据怎么用",
  "以本体建模读懂业务，以模型工厂和智能体工厂持续生产模型与智能体，"
  "并由认知计算引擎统一调度数据、模型、智能体与 Skill，形成从数据到决策的流程闭环。",
  [("天元·灵语","本体建模","自动本体建模，Skill 级业务操作，支持 200+ AI 动作；构建行业知识建模、时空本体建模、图谱推理与因果分析","业务人员无需编程即可调用 AI 能力"),
   ("天元·灵炼","模型工厂","数据在线 AI 标注，大模型后训练，完成 7 项应用模型，支持增量训练与联邦学习","模型迭代周期从“月级”缩短至“周级”"),
   ("天元·灵智","智能体工厂","提供智能体开发、编排与运行能力，支持多智能体任务编排与自我进化","智能体开发效率提升，业务场景快速落地"),
   ("认知计算引擎","智能体编排框架","能够自动调度数据、模型、智能体与 Skill，实现信息服务的流程闭环","为上层应用提供统一的能力调度与编排支撑，实现端到端流程闭环")]),
 ("具身智能行动执行引擎", "指令怎么执行",
  "面向无人机、无人车、机器狗等多类具身设备，实现统一调度与链路自适应下发，"
  "结合视觉增强完成厘米级精准作业，打通从决策到行动的最后一公里。",
  [("天元·灵动","具身智能调度","覆盖无人机、无人车、机器狗等多类具身设备；统一调度，链路自适应下发；具备视觉增强，支持小、中、大覆盖半径（作业面积 5m²–100km²）的精准作业","多设备协同效率提升 50%，调度响应 ≤1s；作业精度提升至厘米级，人力成本降低 70%")]),
]

def engine_cards():
    out=[]
    for name, tag, intro, mods in ENGINES:
        ml = "".join(
          '<div class="card" data-fl="prod" data-f="%s"><h4>%s</h4>'
          '<p style="font-size:12.5px;color:#00A0E9;margin:2px 0 7px;font-weight:700">%s</p>'
          '<p>%s</p><ul><li>%s</li></ul></div>'
          % (FL_MAP[name], m[0], m[1], m[2], m[3]) for m in mods)
        out.append("""
    <div class="ecard rv">
      <div class="ecard-h">
        <div>
          <span class="e-tag">%s</span>
          <h3>%s</h3>
        </div>
        <a class="e-more" href="product-detail.html#%s">查看分层详情 &#8594;</a>
      </div>
      <p class="e-intro">%s</p>
      <div class="grid%s">%s
      </div>
    </div>""" % (tag, name, ANCH_MAP[name], intro, "3" if len(mods)>1 else "3", ml))
    return "".join(out)

FL_MAP = {"空天地数据融合引擎":"fusion","认知计算与决策引擎":"cognition","具身智能行动执行引擎":"embodied"}
ANCH_MAP = {"空天地数据融合引擎":"fusion","认知计算与决策引擎":"cognition","具身智能行动执行引擎":"embodied"}

# ---------- 数据：智算底座 ----------
INFRA = [
 ("智算集群","支持国产全栈适配，提供算力池化与统一资源管理","算力资源利用率提升 30%+，支持弹性扩容"),
 ("高速互联","RDMA 高速互联网络，分布式并行存储","训练效率提升 50%，存储吞吐达 TB 级"),
 ("边云协同","支持云端训练与边缘端推理的无缝协同","边缘推理延迟 ≤50ms，带宽成本降低 40%"),
]

# ---------- 数据：数智市集 ----------
MARKET = [
 ("数智资产广场","汇聚数据集、本体、算法、模型等数字资产，支持上架、检索与复用。"),
 ("智能体及技能广场","汇聚智能体、Skill、Workflow 等，支持按需调用。"),
 ("天元·信息服务助手","行业信息服务的统一入口，提供通用智能问答、记忆、多轮对话等问答能力，可通过认知计算引擎在线对数智市集中的各类资产进行体验与交互。"),
]

# ---------- 数据：安全体系 ----------
SEC = [
 ("身份与访问控制","统一身份，分级授权。"),
 ("数据安全与隐私","加密脱敏，数据不出域，密级流转。"),
 ("AI 安全治理","抗注入，模型可信赖，对抗防护。"),
 ("行为审计与溯源","全链路审计，操作可追溯。"),
]

# ---------- 数据：产品注册表（12 项）----------
REG = [
 ("天元·智算底座","基础设施层","国产化、高性能的算力与数据存储支持，算力池化与统一资源管理，确保底层稳固。","infra"),
 ("天元·灵观","数据融合层","天基数据获取，便捷获取卫星数据，AI 简化任务需求，星地协同智能指挥，覆盖高、低轨卫星及 44 个全球地面站。","fusion"),
 ("天元·灵数","数据融合层","数据治理与融合，智能数据治理，多源数据融合（卫星遥感、无人机、物联网），50+ 自动化管道。","fusion"),
 ("空天地一体化网络","数据融合层","通信全流程保障，星地链路、5G/专网、边缘组网等多种通信方式自适应切换。","fusion"),
 ("天元·灵语","认知决策层","本体建模，自动本体建模，Skill 级业务操作，支持 200+ AI 动作，业务人员无需编程即可调用 AI 能力。","cognition"),
 ("天元·灵炼","认知决策层","模型工厂，数据在线 AI 标注，大模型后训练，支持增量训练与联邦学习，模型迭代周期从“月级”缩短至“周级”。","cognition"),
 ("天元·灵智","认知决策层","智能体工厂，提供智能体开发、编排与运行能力，支持多智能体任务编排与自我进化。","cognition"),
 ("认知计算引擎","认知决策层","智能体编排框架，自动调度数据、模型、智能体与 Skill，实现信息服务的流程闭环。","cognition"),
 ("天元·灵动","行动执行层","具身智能调度，覆盖无人机、无人车、机器狗等多类具身设备，统一调度与精准作业。","embodied"),
 ("天元·灵集","数智市集","数智能力集散与流通平台，包含数智资产广场、智能体及技能广场。","market"),
 ("天元·信息服务助手","数智市集","行业信息服务的统一入口，提供通用智能问答、记忆、多轮对话等问答能力，可通过认知计算引擎在线体验与交互数智市集各类资产。","market"),
 ("全栈安全合规","安全合规","身份与访问控制、数据安全与隐私、AI 安全治理、行为审计与溯源，横向贯穿所有层级。","security"),
]

# ---------- 数据：典型场景 ----------
SCENES = [
 ("边防预警与研判处置","多元信息融合的态势感知、预警发现、研判处置，无人装备协同闭环。","solutions.html"),
 ("海洋污染溯源分析","油膜识别与起始点反演，输出嫌疑船舶排序及证据链。","solutions.html"),
 ("灾害应急对比分析","自然语言拉取灾前灾后影像，建筑物损毁、水体淹没范围对比。","solutions.html"),
]

prod = """
<div class="banner pad"><div class="banner-in">
  <span style="display:inline-block;background:#00A0E9;color:#1A1A1A;font-size:12px;font-weight:700;
    padding:4px 12px;border-radius:3px;letter-spacing:1px;margin-bottom:12px">1 + 3 + 1 + 1 + N</span>
  <h1>产品与能力</h1>
  <p class="lead">1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用。<br>
    构建从卫星原始数据获取到行动指令下达的全链路闭环系统。</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px">
    <a class="btn btn-p btn-lg" href="#engine">了解三大引擎</a>
    <a class="btn btn-o btn-lg" href="product-detail.html">平台完整详情</a>
  </div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 产品与能力</div></div>

<!-- ===== 体系总纲 ===== -->
<section class="sec" id="arch">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">ARCHITECTURE</div><h2>体系总纲</h2>
      <p>1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用</p></div>

    <div class="arch rv">
      <div class="arch-row">
        <div class="arch-lb">应用层（N）</div>
        <div class="arch-body">
          <span class="arch-chip">应急减灾</span><span class="arch-chip">边防管控</span>
          <span class="arch-chip">海洋应用</span><span class="arch-chip">开源情报</span>
          <span class="arch-chip ghost">更多行业：能源 / 低空 / 林草 / 电网</span>
        </div>
      </div>
      <div class="arch-row">
        <div class="arch-lb">数智市集</div>
        <div class="arch-body">
          <span class="arch-chip">天元·灵集</span>
          <span class="arch-chip ghost">数智资产广场 · 智能体及技能广场 · 天元·信息服务助手</span>
        </div>
      </div>
      <div class="arch-row">
        <div class="arch-lb">三大核心引擎</div>
        <div class="arch-body arch-3">
          <a class="arch-e" href="#engine">
            <b>空天地数据融合引擎</b>
            <span>天元·灵观 · 天元·灵数 · 空天地一体化网络</span></a>
          <a class="arch-e" href="#engine">
            <b>认知计算与决策引擎</b>
            <span>天元·灵语 · 天元·灵炼 · 天元·灵智 · 认知计算引擎</span></a>
          <a class="arch-e" href="#engine">
            <b>具身智能行动执行引擎</b>
            <span>天元·灵动</span></a>
        </div>
      </div>
      <div class="arch-row">
        <div class="arch-lb">基础设施层</div>
        <div class="arch-body">
          <span class="arch-chip">天元·智算底座</span>
          <span class="arch-chip ghost">智算集群 / 高速互联 / 边云协同，国产化全栈适配</span>
        </div>
      </div>
      <div class="arch-row arch-sec">
        <div class="arch-lb">安全体系（横向）</div>
        <div class="arch-body">
          <span class="arch-chip">全栈安全合规体系</span>
          <span class="arch-chip ghost">身份与访问控制 · 数据安全与隐私 · AI 安全治理 · 行为审计与溯源</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== 三大核心引擎（引擎能力并入本页）===== -->
<section class="sec alt" id="engine">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CORE ENGINES</div><h2>三大核心引擎</h2>
      <p>融合人工智能与智能体技术，实现从空天地数据融合到认知决策、再到行动执行的全链路闭环。</p></div>
    __ENGINES__
  </div>
</section>

<!-- ===== 分层能力（可筛选）===== -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CAPABILITIES</div><h2>分层能力一览</h2>
      <p>按分类口径筛选，卡片对应各层具体产品。</p></div>

    <div class="filter-bar rv" data-group="prod">
      <span class="lb">按分类筛选</span>
      <button class="chip" data-k="infra" type="button">智算底座</button>
      <button class="chip" data-k="fusion" type="button">数据融合</button>
      <button class="chip" data-k="cognition" type="button">认知决策</button>
      <button class="chip" data-k="embodied" type="button">行动执行</button>
      <button class="chip" data-k="market" type="button">数智市集</button>
      <button class="chip" data-k="security" type="button">安全合规</button>
    </div>
    <div class="selected" data-selected="prod"></div>

    <div id="infra" style="margin:14px 0">
      <h2 style="font-size:20px;color:#0F3D75;border-left:3px solid #00A0E9;padding-left:10px">
        基础设施层 · 天元 · 智算底座</h2>
      <p style="font-size:13.5px;color:#5C6670;margin-top:6px">
        提供国产化、高性能的算力与数据存储支持，确保底层稳固。</p>
    </div>
    <div class="grid3 rv" style="margin-bottom:16px">
      __INFRA__
    </div>

    <div id="market" style="margin:34px 0 14px">
      <h2 style="font-size:20px;color:#0F3D75;border-left:3px solid #00A0E9;padding-left:10px">
        数智市集 · 天元 · 灵集</h2>
      <p style="font-size:13.5px;color:#5C6670;margin-top:6px">
        作为数智能力的集散与流通平台，连接能力供给与业务消费。</p>
    </div>
    <div class="grid3 rv" style="margin-bottom:16px">
      __MARKET__
    </div>

    <div id="security" style="margin:34px 0 14px">
      <h2 style="font-size:20px;color:#0F3D75;border-left:3px solid #00A0E9;padding-left:10px">
        安全支撑体系 · 全栈安全合规</h2>
      <p style="font-size:13.5px;color:#5C6670;margin-top:6px">
        横向贯穿所有层级，提供全流程安全保障。</p>
    </div>
    <div class="grid4 rv">
      __SEC__
    </div>

    <div class="nlist rv" data-empty="prod" style="display:none;margin-top:20px">
      <div style="padding:34px 24px;text-align:center;color:#5C6670">
        暂无符合条件的能力，请调整筛选条件，或
        <a href="contact.html" style="color:#00608C;text-decoration:underline">联系销售获取最新方案</a>。
      </div></div>
  </div>
</section>

<!-- ===== 产品注册表 ===== -->
<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">PRODUCT REGISTRY</div><h2>产品注册表（能力清单）</h2>
      <p>12 项产品，按层级归属；点击产品名可跳转至对应分层。</p></div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th>产品名</th><th>层级</th><th>一句话说明</th></tr></thead>
      <tbody>
        __REG__
      </tbody></table></div>
    <div class="info rv"><b>分类口径：</b>
      全部 / 智算底座 / 数据融合 / 认知决策 / 行动执行 / 数智市集 / 安全合规</div>
  </div>
</section>

<!-- ===== 典型场景 ===== -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">SCENARIOS</div><h2>典型应用场景</h2></div>
    <div class="grid3 rv">
      __SCENES__
    </div>
  </div>
</section>

<!-- ===== 交付物 ===== -->
<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">DOCUMENTS</div><h2>交付物 / 文档清单</h2></div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th>文档</th><th>形式</th><th>状态</th></tr></thead>
      <tbody>
        <tr><td style="color:#0F3D75;font-weight:700">平台白皮书</td><td>PDF · 约 8MB</td>
          <td><a href="contact.html" style="color:#00608C;text-decoration:underline">待提供</a></td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">产品规格书</td><td>PDF · 约 3MB</td>
          <td><a href="contact.html" style="color:#00608C;text-decoration:underline">待提供</a></td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">API 文档</td><td>在线文档</td>
          <td><a href="contact.html" style="color:#00608C;text-decoration:underline">待提供</a></td></tr>
      </tbody></table></div>
    <div class="note rv"><b>待补充：</b>官网未标注具体版本号与发布日期，
      正式发布前需在《产品详情》原稿中补充。</div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2>需要完整产品规格？</h2>
    <p>留下姓名与电话，我们将发送产品资料并与您进一步沟通。</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-p btn-lg" href="contact.html">获取产品资料</a>
      <a class="btn btn-o btn-lg" href="product-detail.html">查看平台详情</a></div></div>
</section>
"""

# ---------- 填充 ----------
prod = prod.replace("__ENGINES__", engine_cards())
prod = prod.replace("__INFRA__", "\n      ".join(
  '<div class="card" data-fl="prod" data-f="infra"><div class="ico">%s</div><h3>%s</h3>'
  '<p>%s</p><ul><li>%s</li></ul></div>' % (n[0], n[0], n[1], n[2]) for n in INFRA))
prod = prod.replace("__MARKET__", "\n      ".join(
  '<div class="card" data-fl="prod" data-f="market"><h3>%s</h3><p>%s</p></div>' % (m[0], m[1]) for m in MARKET))
prod = prod.replace("__SEC__", "\n      ".join(
  '<div class="card" data-fl="prod" data-f="security"><h4>%s</h4><p>%s</p></div>' % (s[0], s[1]) for s in SEC))
prod = prod.replace("__REG__", "\n        ".join(
  '<tr><td style="color:#0F3D75;font-weight:700">%s</td><td>%s</td>'
  '<td><a href="#%s" style="color:#5C6670">%s</a></td></tr>' % (r[0], r[1], r[3], r[2]) for r in REG))
prod = prod.replace("__SCENES__", "\n      ".join(
  '<div class="card"><h3>%s</h3><p>%s</p>'
  '<a class="more" href="%s">查看解决方案 &#8594;</a></div>' % (s[0], s[1], s[2]) for s in SCENES))

EXTRA = """
<style>
.arch{border:1px solid #B4C7E7;border-radius:8px;overflow:hidden;background:#fff}
.arch-row{display:flex;border-bottom:1px solid #DCE9F5;align-items:stretch}
.arch-row:last-child{border-bottom:0}
.arch-lb{flex:0 0 150px;background:#0F3D75;color:#fff;font-size:13.5px;font-weight:700;
  display:flex;align-items:center;justify-content:center;padding:14px 10px;text-align:center}
.arch-sec .arch-lb{background:#0C315E}
.arch-body{flex:1;padding:14px 16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.arch-chip{background:#DCE9F5;color:#0F3D75;font-size:12.5px;font-weight:700;
  padding:5px 12px;border-radius:3px}
.arch-chip.ghost{background:#fff;color:#5C6670;font-weight:400;
  border:1px dashed #B4C7E7}
.arch-3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:14px 16px}
.arch-e{display:block;background:#F5F8FB;border:1px solid #B4C7E7;border-left:3px solid #00A0E9;
  border-radius:6px;padding:13px 14px;transition:.2s}
.arch-e:hover{background:#DCE9F5;transform:translateY(-2px)}
.arch-e b{display:block;font-size:14px;color:#0F3D75;margin-bottom:4px}
.arch-e span{display:block;font-size:11.5px;color:#5C6670;line-height:1.6}
.ecard{background:#fff;border:1px solid #B4C7E7;border-radius:10px;padding:24px 26px;margin-bottom:18px;
  box-shadow:0 1px 3px rgba(15,61,117,.06)}
.ecard-h{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;flex-wrap:wrap;
  padding-bottom:12px;border-bottom:1px solid #DCE9F5;margin-bottom:12px}
.ecard-h h3{font-size:21px;color:#0F3D75;font-weight:700;margin:0}
.e-tag{display:inline-block;background:#00A0E9;color:#1A1A1A;font-size:11.5px;font-weight:700;
  padding:3px 10px;border-radius:3px;margin-bottom:7px}
.e-more{font-size:13px;color:#00608C;font-weight:700;white-space:nowrap}
.e-more:hover{color:#0F3D75;text-decoration:underline}
.e-intro{font-size:14px;color:#5C6670;line-height:1.95;margin-bottom:18px}
@media(max-width:860px){
  .arch-row{flex-direction:column}
  .arch-lb{flex:none;width:100%;padding:9px}
  .arch-3{grid-template-columns:1fr}
}
</style>
"""

w("products.html", page("产品与能力 | 天元平台",
  "天元平台产品体系：1 个底座 + 3 大核心引擎（空天地数据融合、认知计算与决策、具身智能行动执行）+ 1 个数智市集 + 1 个安全体系 + N 个行业应用。",
  "products", prod, extra_head=EXTRA))
