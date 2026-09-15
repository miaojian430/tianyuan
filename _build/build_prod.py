# -*- coding: utf-8 -*-
"""产品与能力页 —— 唯一产品能力目录页（依据 update.md 重构，2026-09-14）
结构：Banner / 分层能力一览（交互式架构图 + 层级筛选器 + 产品卡）/ 产品清单 / 页尾 CTA
- Banner：三关键词小字 + 行业数智化全链路产品体系，不出现 1+3+1+1+N
- 架构图五横行，层级可点，与筛选器、产品卡联动高亮
- 筛选器无“全部”，单选，默认数据融合层，支持 ?f= 与页内 hash 联动
- 产品卡（依据《产品卡信息精简 PRD》，2026-09-14）：
  媒体区 16:9 / 顶部标签（仅能力分类，2–6 字）/ 产品名 / 功能介绍 /
  关键指标（独立一行，不重复介绍中已出现的数字）/ 申请试用 | 查看详情
  已删除独立“功能定位”“客户价值”字段；视频入口仅在媒体区右上角图标
- 全部数字指标为演示口径，待产品部门复核
"""
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ---------- 数据：六层产品卡 ----------
# (层级key, 分组锚点, 层级 · 引擎, 灵魂问题 or None,
#   卡片[锚点, 产品名, 能力分类标签, 功能介绍, 关键指标(·分隔), 媒体 dict or None])
# 媒体素材取自 data/产品与能力/：{"video":..} 自动播放入口在媒体区，{"img":..} 为产品图
MEDIA = {
 "fusion-lingguan": {"img":"data/产品与能力/天元灵观/天基信息服务系统.png"},
 "fusion-lingshu":  {"video":"data/产品与能力/天元灵数/天元·灵数_加字幕.mp4"},
 "fusion-network":  None,
 "cognition-lingyu":{"video":"data/产品与能力/天元灵语/天元·灵语_加字幕.mp4"},
 "cognition-linglian":{"video":"data/产品与能力/天元灵炼/天元·灵炼_加字幕.mp4"},
 "cognition-lingzhi":{"img":"data/产品与能力/天元灵智/dify截图.jpg"},
 "cognition-engine":{"video":"data/产品与能力/天元认知计算/天元认知计算_行业应用_开源情报+海洋油污+应急信息服务_有字幕.mp4"},
 "embodied-lingdong":{"img":"data/产品与能力/天元灵动/天元灵动.png"},
 "market-assets":   {"img":"data/产品与能力/数智集市/一套多元数据融合资源池.png"},
 "market-agents":   {"img":"data/产品与能力/数智集市/一套行业智能组件库.png"},
 "market-assistant":{"img":"data/产品与能力/数智集市/一套数智服务工具链.png"},
}
# 顶部标签对照：基础支撑 / 数据获取·数据治理·通信保障 / 本体建模·模型工厂·
# 智能体工厂·编排调度 / 具身智能调度 / 资产流通·技能流通·信息服务 /
# 身份安全·数据安全·AI 安全·审计溯源
LAYERS = [
 ("infra","infra","基础设施层 · 天元·智算底座",None,[
   ("infra-cluster","智算集群","基础支撑",
    "国产全栈适配，算力池化与统一资源管理，支持弹性扩容。",
    "算力利用率 +30%"),
   ("infra-network","高速互联","基础支撑",
    "RDMA 高速互联与分布式并行存储，训练效率提升 50%。",
    "TB 级存储吞吐"),
   ("infra-edge","边云协同","基础支撑",
    "云端训练与边缘推理无缝协同，边缘延迟 ≤50ms。",
    "带宽成本降低 40%"),
 ]),
 ("fusion","fusion","数据融合层 · 空天地数据融合引擎","数据从哪来",[
   ("fusion-lingguan","天元·灵观","数据获取",
    "便捷获取卫星数据，覆盖高、低轨卫星及 44 个全球地面站，小时级获取。",
    "星地协同智能指挥"),
   ("fusion-lingshu","天元·灵数","数据治理",
    "多源数据治理与融合，50+ 自动化管道，人工干预减少 60%。",
    "20+ 数据集 · 融合效率 3 倍"),
   ("fusion-network","空天地一体化网络","通信保障",
    "星地链路、5G/专网、边缘组网自适应切换，保障高带宽低延迟。",
    "多链路自适应切换"),
 ]),
 ("cognition","cognition","认知决策层 · 认知计算与决策引擎","数据怎么用",[
   ("cognition-lingyu","天元·灵语","本体建模",
    "自动本体建模，支持 200+ AI 动作，业务人员无需编程即可调用。",
    "Skill 级业务操作"),
   ("cognition-linglian","天元·灵炼","模型工厂",
    "数据标注、大模型后训练与联邦学习，模型迭代月级缩短至周级。",
    "7 项应用模型 · 增量训练"),
   ("cognition-lingzhi","天元·灵智","智能体工厂",
    "智能体开发、编排与运行，支持多智能体任务编排与自我进化。",
    "业务场景快速落地"),
   ("cognition-engine","认知计算引擎","编排调度",
    "自动调度数据、模型、智能体与 Skill，实现端到端流程闭环。",
    "统一能力调度编排"),
 ]),
 ("embodied","embodied","行动执行层 · 具身智能行动执行引擎","指令怎么执行",[
   ("embodied-lingdong","天元·灵动","具身智能调度",
    "统一调度无人机、无人车、机器狗，调度响应 ≤1s，作业精度厘米级。",
    "协同效率 +50% · 人力成本 −70%"),
 ]),
 ("market","market","数智市集 · 天元·灵集",None,[
   ("market-assets","数智资产广场","资产流通",
    "汇聚数据集、本体、算法、模型等数字资产，支持上架、检索与复用。",
    "数字资产一站式流通"),
   ("market-agents","智能体及技能广场","技能流通",
    "汇聚智能体、Skill、Workflow 等，支持按需调用。",
    "技能按需即取即用"),
   ("market-assistant","天元·信息服务助手","信息服务",
    "行业信息服务统一入口，提供智能问答、记忆、多轮对话等能力。",
    "数智资产在线交互"),
 ]),
 ("security","security","安全支撑体系 · 全栈安全合规",None,[
   ("security-iam","身份与访问控制","身份安全",
    "统一身份，分级授权。",
    "身份 / 权限 / 访问统一管控"),
   ("security-data","数据安全与隐私","数据安全",
    "加密脱敏，数据不出域，密级流转。",
    "全生命周期数据保护"),
   ("security-ai","AI 安全治理","AI 安全",
    "抗注入，模型可信赖，对抗防护。",
    "全流程 AI 风险防控"),
   ("security-audit","行为审计与溯源","审计溯源",
    "全链路审计，操作可追溯。",
    "事件定位与回溯"),
 ]),
]

# 筛选器：无“全部”，默认数据融合（fusion）
FILTERS = [("infra","智算底座"),("fusion","数据融合"),("cognition","认知决策"),
           ("embodied","行动执行"),("market","数智市集"),("security","安全合规")]
DEFAULT_F = "fusion"

# ---------- 数据：产品清单（12 项）----------
# (产品名, 层级, 一句话说明, 关键指标, 目标锚点)
REG = [
 ("天元·智算底座", "基础设施层", "国产化高性能算力与数据存储支持", "算力利用率 +30%", "#infra"),
 ("天元·灵观", "数据融合层", "天基数据获取，覆盖高、低轨卫星及 44 个全球地面站", "小时级获取", "#fusion-lingguan"),
 ("天元·灵数", "数据融合层", "数据治理与融合，50+ 自动化管道", "人工干预减少 60%", "#fusion-lingshu"),
 ("空天地一体化网络", "数据融合层", "星地链路、5G/专网、边缘组网自适应切换", "高带宽低延迟", "#fusion-network"),
 ("天元·灵语", "认知决策层", "本体建模，支持 200+ AI 动作", "无需编程调用 AI", "#cognition-lingyu"),
 ("天元·灵炼", "认知决策层", "模型工厂，支持增量训练与联邦学习", "月级→周级", "#cognition-linglian"),
 ("天元·灵智", "认知决策层", "智能体工厂，支持多智能体任务编排", "快速落地", "#cognition-lingzhi"),
 ("认知计算引擎", "认知决策层", "自动调度数据、模型、智能体与 Skill", "端到端闭环", "#cognition-engine"),
 ("天元·灵动", "行动执行层", "具身智能调度，覆盖无人机、无人车、机器狗", "≤1s 响应 · 厘米级", "#embodied-lingdong"),
 ("天元·灵集", "数智市集", "数智能力集散与流通平台", "资产/智能体广场", "#market"),
 ("天元·信息服务助手", "数智市集", "行业信息服务统一入口", "智能问答/多轮对话", "#market-assistant"),
 ("全栈安全合规", "安全合规", "身份、数据、AI、审计全流程安全", "横向贯穿", "#security"),
]


def card_html(card):
    anchor, name, tag, desc, kpi = card[:5]
    m = MEDIA.get(anchor)
    kpis = [x.strip() for x in (kpi or "").split("·") if x.strip()]
    kpi_html = ('\n          <ul class="pcv-kpi">%s</ul>'
                % "".join('<li>%s</li>' % k for k in kpis)) if kpis else ""
    if m and m.get("video"):
        media = ('\n          <video src="%s" controls muted loop playsinline preload="metadata"></video>'
                 % m["video"])
        play = '<span class="pcv-play">&#9654;</span>'
    elif m and m.get("img"):
        media = '\n          <img src="%s" alt="%s" loading="lazy">' % (m["img"], name)
        play = ""
    else:
        media = ('\n          <div class="pcv-ph"><b>&#9654;</b><small>视频封面 / 产品图 / 场景图占位</small></div>')
        play = '<span class="pcv-play">&#9654;</span>'
    return """
      <div class="pcv rv" id="%s">
        <div class="pcv-media" data-media>%s
          %s
        </div>
        <div class="pcv-body">
          <div class="pcv-tags"><span>%s</span></div>
          <h3>%s</h3>
          <p class="pcv-desc">%s</p>%s
          <div class="pcv-act">
            <a class="btn btn-s" href="contact.html">申请试用</a>
            <a class="btn btn-o" href="#list">查看详情 &#8594;</a>
          </div>
        </div>
      </div>""" % (anchor, media, play, tag, name, desc, kpi_html)


def layers_html():
    out = []
    for key, ganchor, title, soul, cards in LAYERS:
        soul_html = (' <span class="pl-q">%s</span>' % soul) if soul else ""
        cards_html = "\n".join(card_html(c) for c in cards)
        out.append("""
    <div class="pl-group" data-group="%s" id="%s">
      <div class="pl-h rv"><h3>%s%s</h3></div>
      <div class="pcv-grid">%s
      </div>
    </div>""" % (key, ganchor, title, soul_html, cards_html))
    return "".join(out)


# 交互式架构图：五横行；层级可点（data-f），与筛选器联动高亮
ARCH = """
    <div class="arch rv" data-arch>
      <div class="arch-row">
        <div class="arch-lb">应用层（N）</div>
        <div class="arch-body">
          <span class="arch-chip">应急减灾</span><span class="arch-chip">边防管控</span>
          <span class="arch-chip">海洋应用</span><span class="arch-chip">开源情报</span>
          <span class="arch-chip ghost">更多行业：能源 / 低空 / 林草 / 电网</span>
        </div>
      </div>
      <div class="arch-row" data-f="market">
        <div class="arch-lb">数智市集</div>
        <div class="arch-body">
          <span class="arch-chip">天元·灵集</span>
          <span class="arch-chip ghost">数智资产广场 · 智能体及技能广场 · 天元·信息服务助手</span>
        </div>
      </div>
      <div class="arch-row">
        <div class="arch-lb">三大核心引擎</div>
        <div class="arch-body arch-3">
          <a class="arch-e" data-f="fusion" href="#fusion">
            <b>空天地数据融合引擎</b>
            <span>天元·灵观 · 天元·灵数 · 空天地一体化网络</span></a>
          <a class="arch-e" data-f="cognition" href="#cognition">
            <b>认知计算与决策引擎</b>
            <span>天元·灵语 · 天元·灵炼 · 天元·灵智 · 认知计算引擎</span></a>
          <a class="arch-e" data-f="embodied" href="#embodied">
            <b>具身智能行动执行引擎</b>
            <span>天元·灵动</span></a>
        </div>
      </div>
      <div class="arch-row" data-f="infra">
        <div class="arch-lb">基础设施层</div>
        <div class="arch-body">
          <span class="arch-chip">天元·智算底座</span>
          <span class="arch-chip ghost">智算集群 / 高速互联 / 边云协同，国产化全栈适配</span>
        </div>
      </div>
      <div class="arch-row arch-sec" data-f="security">
        <div class="arch-lb">安全体系（横向贯穿）</div>
        <div class="arch-body">
          <span class="arch-chip">全栈安全合规体系</span>
          <span class="arch-chip ghost">身份与访问控制 · 数据安全与隐私 · AI 安全治理 · 行为审计与溯源</span>
        </div>
      </div>
    </div>
"""

chips_html = "".join(
    '<button class="pfchip%s" type="button" data-k="%s">%s</button>'
    % (" on" if k == DEFAULT_F else "", k, t) for k, t in FILTERS)

reg_rows = "".join(
    '<tr><td>%d</td><td style="color:#0F3D75;font-weight:700">%s</td><td>%s</td>'
    '<td>%s</td><td>%s</td>'
    '<td><a class="reg-link" href="%s" data-target="%s">查看能力 &#8594;</a></td></tr>'
    % (i + 1, r[0], r[1], r[2], r[3], r[4], r[4].lstrip("#"))
    for i, r in enumerate(REG))

prod = """
<div class="banner pad" id="top"><div class="banner-in">
  <span style="display:inline-block;background:#00A0E9;color:#1A1A1A;font-size:12px;font-weight:700;
    padding:4px 12px;border-radius:3px;letter-spacing:1px;margin-bottom:12px">数据融合 · 认知决策 · 行动执行</span>
  <h1>行业数智化全链路产品体系</h1>
  <p class="lead">12 项核心产品，覆盖智算底座、数据融合、认知决策、行动执行、数智市集、安全合规六大能力层级，<br>
    提供从数据获取到行动执行的闭环能力。</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px">
    <a class="btn btn-p btn-lg" href="#layers">查看产品能力</a>
    <a class="btn btn-o btn-lg" href="contact.html">获取产品资料</a>
  </div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 产品与能力</div></div>

<!-- ===== 分层能力一览：架构图 + 筛选器 + 产品卡 ===== -->
<section class="sec" id="layers">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CAPABILITIES</div><h2>分层能力一览</h2></div>

__ARCH__

    <div class="pfbar rv" role="tablist" aria-label="按层级筛选">
      <span class="lb">按层级筛选</span>
      __CHIPS__
    </div>

    __LAYERS__

    <div class="pl-empty rv" data-empty style="display:none">
      <div style="padding:34px 24px;text-align:center;color:#5C6670">
        暂无符合条件的能力，请调整筛选条件，或
        <a href="contact.html" style="color:#00608C;text-decoration:underline">联系销售获取最新方案</a>。
      </div>
    </div>

    <div class="info rv"><b>说明：</b>所有数字指标均为演示口径，待产品部门复核；
      产品卡媒体区已接入 data/产品与能力/ 素材（视频静音循环，右上角图标标示），
      智算底座与安全合规层素材待补充，接入后自动替换占位。</div>
  </div>
</section>

<!-- ===== 产品清单 ===== -->
<section class="sec alt" id="list">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">PRODUCT LIST</div><h2>产品清单</h2></div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th>序号</th><th>产品名</th><th>层级</th><th>一句话说明</th><th>关键指标</th><th>操作</th></tr></thead>
      <tbody>
        __REG__
      </tbody></table></div>
    <div class="info rv"><b>说明：</b>关键指标为演示口径，待产品部门复核。</div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2>需要完整产品规格？</h2>
    <p>留下姓名与电话，我们将发送产品资料并与您进一步沟通。</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-p btn-lg" href="contact.html">获取产品资料</a>
      <a class="btn btn-o btn-lg" href="#list">查看产品清单</a></div></div>
</section>
"""

prod = prod.replace("__ARCH__", ARCH)
prod = prod.replace("__CHIPS__", chips_html)
prod = prod.replace("__LAYERS__", layers_html())
prod = prod.replace("__REG__", reg_rows)

EXTRA_CSS = """
<style>
/* 交互式架构图：五横行，层级可点 */
.arch{border:1px solid #B4C7E7;border-radius:8px;overflow:hidden;background:#fff;margin-bottom:18px}
.arch-row{display:flex;border-bottom:1px solid #DCE9F5;align-items:stretch}
.arch-row:last-child{border-bottom:0}
.arch-row[data-f]{cursor:pointer}
.arch-lb{flex:0 0 150px;background:#0F3D75;color:#fff;font-size:13.5px;font-weight:700;
  display:flex;align-items:center;justify-content:center;padding:14px 10px;text-align:center}
.arch-sec .arch-lb{background:#0C315E}
.arch-body{flex:1;padding:14px 16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.arch-chip{background:#DCE9F5;color:#0F3D75;font-size:12.5px;font-weight:700;
  padding:5px 12px;border-radius:3px}
.arch-chip.ghost{background:#fff;color:#5C6670;font-weight:400;border:1px dashed #B4C7E7}
.arch-3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:14px 16px}
.arch-e{display:block;background:#F5F8FB;border:1px solid #B4C7E7;border-left:3px solid #00A0E9;
  border-radius:6px;padding:13px 14px;transition:.2s;text-decoration:none;cursor:pointer}
.arch-e:hover{background:#DCE9F5;transform:translateY(-2px)}
.arch-e b{display:block;font-size:14px;color:#0F3D75;margin-bottom:4px}
.arch-e span{display:block;font-size:11.5px;color:#5C6670;line-height:1.6}
/* 架构图选中态：与筛选器联动 */
.arch-row.on .arch-lb{background:#00A0E9}
.arch-row.on .arch-body{background:#F1F8FD}
.arch-e.on{background:#DCE9F5;border-color:#00A0E9}
/* 层级筛选器（单选，无“全部”） */
.pfbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px;
  padding:14px 16px;background:#fff;border:1px solid #BEC3C8;border-radius:8px}
.pfbar .lb{font-size:13px;color:#5C6670;font-weight:700;margin-right:4px}
.pfchip{background:#fff;border:1px solid #BEC3C8;color:#33414E;font-size:13px;
  padding:6px 14px;border-radius:16px;cursor:pointer;font-family:inherit;transition:.15s}
.pfchip:hover{border-color:#00A0E9;color:#00608C}
.pfchip.on{background:#0F3D75;border-color:#0F3D75;color:#fff;font-weight:700}
/* 分层分组 */
.pl-group{margin-top:26px}
.pl-h{margin-bottom:14px}
.pl-h h3{font-size:20px;color:#0F3D75;border-left:3px solid #00A0E9;padding-left:10px;margin:0}
.pl-q{display:inline-block;font-size:11px;font-weight:700;color:#0A4A75;background:#CCECFB;
  padding:2px 8px;border-radius:3px;margin-left:8px;vertical-align:2px}
/* 产品卡：桌面 3 列 / 平板 2 列 / 手机 1 列 */
.pcv-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.pcv{background:#fff;border:1px solid #B4C7E7;border-radius:10px;overflow:hidden;
  display:flex;flex-direction:column;box-shadow:0 1px 3px rgba(15,61,117,.06);transition:box-shadow .2s}
.pcv:hover{box-shadow:0 6px 18px rgba(15,61,117,.14)}
.pcv.hl{outline:3px solid #00A0E9;outline-offset:2px}
/* 媒体区：16:9，视频封面/产品图/场景图，右上角播放图标 */
.pcv-media{position:relative;width:100%;padding-top:56.25%;background:#EEF4FA;overflow:hidden}
.pcv-media video,.pcv-media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0}
.pcv-media video{background:#0C1524}
.pcv-ph{position:absolute;inset:0;display:flex;flex-direction:column;gap:8px;
  align-items:center;justify-content:center;color:#7C8894;
  border-bottom:1px dashed #B4C7E7;transition:opacity .4s}
.pcv-ph b{display:flex;align-items:center;justify-content:center;width:46px;height:46px;
  border-radius:50%;background:#0F3D75;color:#fff;font-size:17px;opacity:.85}
.pcv-ph small{font-size:11.5px}
.pcv-media:not(.ld) .pcv-ph{opacity:.3}
.pcv-play{position:absolute;top:8px;right:8px;width:28px;height:28px;border-radius:50%;
  background:rgba(15,61,117,.72);color:#fff;display:flex;align-items:center;
  justify-content:center;font-size:11px;pointer-events:none}
.pcv-body{padding:16px 18px 18px;display:flex;flex-direction:column;flex:1}
.pcv-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.pcv-tags span{background:#DCE9F5;color:#0F3D75;font-size:11px;font-weight:700;
  padding:2px 8px;border-radius:3px}
.pcv-body h3{font-size:17.5px;color:#0F3D75;margin:0 0 6px}
.pcv-desc{font-size:13px;color:#33414E;line-height:1.8;margin:0 0 10px}
.pcv-kpi{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:0 0 14px;padding:0}
.pcv-kpi li{font-size:11.5px;color:#0A4A75;background:#F1F7FC;border:1px solid #C9DCEF;
  border-radius:3px;padding:2px 8px}
.pcv-act{display:flex;gap:10px;flex-wrap:wrap;margin-top:auto}
.reg-link{color:#00608C;font-weight:700;text-decoration:none;white-space:nowrap}
.reg-link:hover{color:#0F3D75;text-decoration:underline}
@media(max-width:1024px){.pcv-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:860px){.arch-row{flex-direction:column}
  .arch-lb{flex:none;width:100%;padding:9px}
  .arch-3{grid-template-columns:1fr}}
@media(max-width:680px){.pcv-grid{grid-template-columns:1fr}
  .pfbar .lb{width:100%;margin-bottom:2px}}
</style>
"""

EXTRA_JS = """
<script>
(function(){
  'use strict';
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s,c){return (c||document).querySelector(s);}
  function $$(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s));}

  var bar = $('.pfbar');
  if(!bar) return;
  var groups  = $$('.pl-group');
  var chips   = $$('.pfchip', bar);
  var archEls = $$('[data-f]');           /* 架构图可点层级（行 + 引擎块） */
  var emptyBox = $('[data-empty]');
  var KEYS = chips.map(function(c){return c.dataset.k;});
  var DEFAULT = 'fusion';                 /* 默认数据融合层 */

  function scrollToEl(el, block){
    if(!el) return;
    setTimeout(function(){
      el.scrollIntoView({behavior: REDUCED?'auto':'smooth', block: block||'start'});
    }, 60);
  }

  /* 筛选 + 架构图高亮 + 产品卡显隐 */
  function setFilter(k, scroll){
    if(KEYS.indexOf(k) < 0) k = DEFAULT;
    chips.forEach(function(x){ x.classList.toggle('on', x.dataset.k === k); });
    var shown = 0, target = null;
    groups.forEach(function(g){
      var ok = g.dataset.group === k;
      g.style.display = ok ? '' : 'none';
      if(ok){ shown++; target = g; }
    });
    if(emptyBox) emptyBox.style.display = shown ? 'none' : '';
    archEls.forEach(function(el){ el.classList.toggle('on', el.dataset.f === k); });
    if(scroll && target) scrollToEl(target, 'start');
    return k;
  }

  /* 筛选器切换 → 架构图 + 产品卡 */
  chips.forEach(function(c){
    c.addEventListener('click', function(){ setFilter(c.dataset.k, true); });
  });

  /* 架构图层级点击 → 筛选器选中 + 产品卡滚动定位 */
  archEls.forEach(function(el){
    el.addEventListener('click', function(e){
      e.preventDefault();
      setFilter(el.dataset.f, true);
    });
  });

  /* 入口：?f= 优先，其次页内 hash（导航/页脚锚点），默认数据融合层 */
  var init = DEFAULT;
  try{
    var f = new URLSearchParams(location.search).get('f');
    if(f && KEYS.indexOf(f) >= 0) init = f;
    else{
      var h = location.hash.replace('#','');
      if(h && KEYS.indexOf(h) >= 0) init = h;
    }
  }catch(e){}
  setFilter(init, false);
  if(init !== DEFAULT){
    var g = $('.pl-group[data-group="'+init+'"]');
    if(g) setTimeout(function(){
      g.scrollIntoView({behavior: REDUCED?'auto':'smooth', block:'start'});
    }, 150);
  }

  /* 同页 hash 变化（导航/页脚锚点点击）联动筛选 */
  window.addEventListener('hashchange', function(){
    var h = location.hash.replace('#','');
    if(h && KEYS.indexOf(h) >= 0) setFilter(h, true);
  });

  /* 产品清单“查看能力”：滚动到对应产品卡 / 分组并高亮 */
  $$('.reg-link').forEach(function(a){
    a.addEventListener('click', function(e){
      e.preventDefault();
      var id = a.getAttribute('href').replace('#','');
      var el = document.getElementById(id);
      if(!el) return;
      var g = el.classList.contains('pl-group') ? el : el.closest('.pl-group');
      if(g && g.style.display === 'none') setFilter(g.dataset.group, false);
      scrollToEl(el, 'center');
      el.classList.add('hl');
      setTimeout(function(){ el.classList.remove('hl'); }, 2200);
    });
  });

  /* 媒体懒加载：首屏前 3 张立即加载，其余进入视口（前 200px）再加载 */
  var medias = $$('[data-media]');
  medias.slice(0, 3).forEach(function(m){ m.classList.add('ld'); });
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('ld'); io.unobserve(en.target); }
      });
    }, {rootMargin:'200px'});
    medias.slice(3).forEach(function(m){ io.observe(m); });
  } else {
    medias.forEach(function(m){ m.classList.add('ld'); });
  }
})();
</script>
"""

w("products.html", page("产品与能力 | 天元平台",
  "天元平台产品体系：12 项核心产品，覆盖智算底座、数据融合、认知决策、行动执行、数智市集、安全合规六大能力层级，提供从数据获取到行动执行的闭环能力。",
  "products", prod, extra_head=EXTRA_CSS, extra_js=EXTRA_JS))
