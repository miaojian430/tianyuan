# -*- coding: utf-8 -*-
"""客户案例模块（依据《客户案例模块 PRD》+《update1.1.md》，2026-09-15）
- cases.html：案例列表页（3 列卡片，≤960px 2 列 / ≤640px 1 列），点击卡片弹出详情弹窗
  案例一 智慧边防（军绿弹窗，独立详情页 case-detail.html，本次未改动其内容）
  案例二 智慧水利 / 案例三 边海防一体化 / 案例四 低空安全 / 案例五 应急监测（新增）
- 新案例详情结构（update1.1）：封面 / 客户原声 / 面临挑战 / 解决方案（架构图+能力列表）/
  关键成效（架构图+成效卡片）/ 推广展望 / 底部 CTA（含脱敏标注）
- 各案例独立配色：卡片行业标签主色浅底、数据数值辅助色高亮、Hover 边框主色；
  弹窗以 CSS 变量主题化（--p/--s/--cover 等），智慧边防保持原军绿默认值不变
- 案例数据集中在 CASES 列表，新增案例在此追加即可
"""
import io, sys, json
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ================= 案例数据（配置化） =================
# 新案例 detail 采用 update1.1 结构：subtitle/coverTags/quote/quoteBy/challenges/
# archSol(300px)+solution[[类型?,名称,描述]] / archRes(260px)+results[[成效,数据]] /
# outlook[] / cta；colors 指定主色/辅助色/深色/卡片封面渐变
CASES = [
{
 "id":"smart-border",
 "media":{"type":"video","video":"data/客户案例/智慧边防_有字幕%20.mp4","note":"边防场景实拍视频"},
 "badge":"实战案例",
 "title":"智慧边防，从“看得见”到“看得准”",
 "desc":"构建防控态势一图展示、同屏联动一图预警、全域态势一图指挥、技防量化一图规划四大核心能力，"
        "实现 AI 赋能存量设备与新型装备智能调度两大关键突破，误报降低 80%，有效报警率 95% 以上。",
 "stats":[{"v":"400m","l":"白天发现距离"},{"v":"↓80%","l":"误报降低"},{"v":"95%+","l":"有效报警率"}],
 "detail":{
   "subtitle":"天元平台赋能边境管控智能化实践",
   "coverTags":["智慧边防","AI预警","无人装备协同","无电无网覆盖"],
   "quote":"报警响了，却看不清是人是兽是风。",
   "quoteBy":"—— 某边防团执勤人员",
   "challenges":[
     ["看不远","老旧枪机白天仅能识别 100–200 米，夜间几乎失效"],
     ["辨不准","移动旗帜、树枝等频繁误报，有效报警率低"],
     ["覆盖难","无电无网区域存在感知盲区，数据回传困难"],
     ["协同弱","装备各自为战，缺乏统一调度与联动"]],
   "arch4":{"img":"data/客户案例/智慧边防-解决方案架构图.png","h":300,"label":"四大核心能力架构图"},
   "capabilities":[
     ["防控态势一图展示","人防、物防、技防力量一张图汇聚，设备一键巡检"],
     ["同屏联动一图预警","智能预警 + 持续定位 + 轨迹回溯，推送一线护边员"],
     ["全域态势一图指挥","智能情报助手，问答式查询，辅助生成分析报告"],
     ["技防量化一图规划","GIS + 遥感三维建模，可视化评估覆盖盲区与补点效能"]],
   "arch2":{"img":"data/客户案例/智慧边防-关键成效图.png","h":260,"label":"两大关键突破架构图"},
   "breakthroughs":[
     {"title":"突破一 · AI 赋能存量设备",
      "desc":"老旧枪机不变焦条件下，白天发现距离由 100–200 米提升至 400 米，"
             "夜间无辅助照明条件下提升至 200 米。",
      "stats":["400m","200m","↓80%"]},
     {"title":"突破二 · 新型装备智能调度",
      "desc":"卫星链路补盲无电无网区域，机器狗联动抵近侦察，破解复杂地形管控难题。",
      "stats":["95%+","卫星链路补盲","机器狗联动侦察"]}],
   "place":"新疆生产建设兵团",
   "cta":"目前已在新疆生产建设兵团开展应用实践"
 }
},
{
 "id":"smart-water",
 "media":{"type":"video","video":"data/客户案例/智慧水利.mp4","note":"水电站库区航拍 + 无人清污船作业场景"},
 "badge":"实战案例",
 "title":"智慧水利，从“人巡人清”到“机巡智清”",
 "desc":"构建水电站机器人巡检、水库无人船清污、存量设备智能增强三大落地场景，"
        "推进来水预测模型、虚拟电厂两项创新应用，实现水利运营智能化升级。",
 "stats":[{"v":"3场景","l":"落地场景"},{"v":"2创新","l":"创新应用"},{"v":"24h","l":"无人清污在线"}],
 "colors":{"primary":"#0a6b8a","secondary":"#00c9a7","deep":"#053a4e",
           "cover":"linear-gradient(135deg,#053a4e,#0a6b8a 60%,#0e7d97)",
           "cardCover":"linear-gradient(135deg,#053a4e,#0a6b8a)"},
 "detail":{
   "subtitle":"平台赋能水利运营智能化实践",
   "coverTags":["智慧水利","具身智能","无人清污","虚拟电厂"],
   "quote":"巡检靠手电、清污靠打捞、调度靠电话——这是我们多年的工作方式。",
   "quoteBy":"—— 某水电站一线运维人员",
   "challenges":[
     ["设备巡检","依靠人员现场逐项检查，手工记录、经验判断"],
     ["水面清污","依靠人员现场打捞，效率低、安全风险高"],
     ["水务调度","依靠人工监屏、电话沟通、台账记录"],
     ["数据孤岛","存量摄像头识别效率单一，数据无法分析"]],
   "archSol":{"img":"data/客户案例/水利-解决方案架构图.png","h":300,"label":"3场景+2创新架构图"},
   "solution":[
     ["落地场景","水电站机器人巡检","机器狗+轮式机器人，覆盖厂房设备、屋顶、坝坡"],
     ["落地场景","水库无人船清污","AIR 小型灵活 + PRO 大型高效，24h 在线、自动返航"],
     ["落地场景","存量设备智能增强","边缘算力盒+多模态算法，人员合规/周界安全/设备状态"],
     ["创新应用","来水预测模型","五步闭环：数据摸排→联合立项→模型研发→范围试用→效果评估"],
     ["创新应用","虚拟电厂","聚合水电资源，价格预测、调度策略、控制执行"]],
   "archRes":{"img":"data/客户案例/水利-关键成效图.png","h":260,"label":"关键成效架构图"},
   "results":[
    ["巡检效率","高风险作业替代，效率大幅提升"],
    ["清污能力","24h 在线，收集宽度达 15m"],
    ["设备增强","异常事件自动截帧定位"],
    ["创新突破","全国首创/首例/首建"]],
   "outlook":[
    "全国首创：来水预测模型智能体",
    "全国首例：自动化清污船水库治理案例",
    "全国首建：小型水电虚拟电厂"],
   "place":"西南地区某水电企业",
   "cta":"已在西南地区某水电企业开展应用实践"
 }
},
{
 "id":"coast-defense",
 "media":{"type":"video","video":"data/客户案例/智慧边海防_有字幕.mp4","note":"边海防地形航拍 + 平台态势大屏"},
 "badge":"实战案例",
 "title":"边海防一体化，从“分散试点”到“一网统管”",
 "desc":"构建边海防融合指挥调度平台，实现五地市存量资源一网纳管、AI 赋能情指行一体化、"
        "空天地海立体感知，打造边海防创新标杆。",
 "stats":[{"v":"5市联动","l":"多地市一网纳管"},{"v":"20+场景","l":"应用场景"},{"v":"85%","l":"小目标识别率"}],
 "colors":{"primary":"#1a4a7a","secondary":"#00b4d8","deep":"#0f2f4f",
           "cover":"linear-gradient(135deg,#0f2f4f,#1a4a7a 60%,#23629b)",
           "cardCover":"linear-gradient(135deg,#0f2f4f,#1a4a7a)"},
 "detail":{
   "subtitle":"平台赋能边海防融合指挥调度实践",
   "coverTags":["边海防一体化","空天地海","一网统管","AI赋能"],
   "quote":"复杂的山海地形，传统监控存在大量视线死角，难以实现全域覆盖。",
   "quoteBy":"—— 某边海防一线人员",
   "challenges":[
    ["感知盲区覆盖不足","深山密林、近海滩涂植被遮挡严重，传统监控存在大量视线死角"],
    ["智能研判精准度低","AI 智能分析覆盖有限，复杂环境易产生大量无效告警，缺乏统一风险研判模型"],
    ["指挥割裂处置闭环缺失","五级指挥链路未完全打通，告警流转滞后，线上闭环机制不完善"],
    ["装备零散难以协同","侦测、干扰、反制装备独立操作，缺乏统一平台调度与联动机制"]],
   "archSol":{"img":"data/客户案例/广西边海防-解决方案架构图.png","h":300,"label":"边海防融合指挥调度平台架构图"},
   "solution":[
    ["情指行一体","AI 赋能情报分析、指挥调度、行动支撑，覆盖“预警识别→智能分析→报告生成→辅助决策→实时调度→现场辅助→自动巡检→机动处置”全链条"],
    ["数据/业务/场景融合","打通跨部门数据壁垒，实现数据融合、业务融合、场景融合，推动党政军警民数据汇聚共享"],
    ["五地联动一网统管","区、市、县三级平台互联互通，五地市存量软件平台与硬件设备统一接入，不替换、不搬迁"],
    ["空天地海立体感知","融合地面智能设备、无人机、无人船及北斗卫星，打造“空-天-地-海-哨”五位一体感知网"]],
   "innovations":[
    ["空天地海一体","卫星通信、无人机机巢、北斗定位、卫星遥感"],
    ["水文气象×海防","潮汐窗口研判、台风风暴潮调度、滩涂浅水航线识别、河口红树林监测"]],
   "archRes":{"img":"data/客户案例/广西边海防-关键成效图.png","h":260,"label":"关键成效架构图"},
   "results":[
    ["无人机自动巡航","巡查从 1 小时+ 压缩至 20 分钟"],
    ["小目标精准识别","1080p 摄像头实现 500m 远距离行人识别"],
    ["跨设备目标匹配","准确率 85%"],
    ["潮汐窗口研判","已验证预警 16 艘次"],
    ["海防查缉","伪装渔船暗舱查获走私冻品 47 吨"],
    ["创新突破","全国首个边海防三级数据融合标杆；全国首个边防行业大模型；全国首建“产学研用”转化枢纽"]],
   "outlook":[
    "全国首个：边海防三级数据融合标杆",
    "全国首个：边防行业大模型",
    "全国首建：“产学研用”转化枢纽",
    "计划推动：建立 TB 级边海防数据库和知识图谱 / 打造不少于 20 个大模型应用落地场景 / 引入 2 家顶级高校或科研机构共创数据场景 / 打造申报不少于 1 个国家级奖项"],
   "place":"华南某边海防区域",
   "cta":"已在华南某边海防区域开展应用实践"
 }
},
{
 "id":"low-altitude",
 "media":{"type":"placeholder","note":"城市低空无人机巡航 + 察打一体设备"},
 "badge":"实战案例",
 "title":"低空安全，从“被动应对”到“察打一体”",
 "desc":"构建情指行一体+平峰一体+察打一体三位一体管控体系，实现核心区禁飞筑铁壁、"
        "预警区全域织密网，打造低空安全示范样板。",
 "stats":[{"v":"2km","l":"核心区禁飞"},{"v":"10km","l":"预警区覆盖"},{"v":"1000+","l":"机型识别覆盖"}],
 "colors":{"primary":"#2a1a5a","secondary":"#ff6b4a","deep":"#170d2e",
           "cover":"linear-gradient(135deg,#170d2e,#2a1a5a 60%,#3a2676)",
           "cardCover":"linear-gradient(135deg,#170d2e,#2a1a5a)"},
 "detail":{
   "subtitle":"平台赋能低空安全管控实践",
   "coverTags":["低空安全","察打一体","情指行一体","平峰一体"],
   "quote":"低空威胁来了，传统手段发现难、处置慢。",
   "quoteBy":"—— 某低空安全管控一线人员",
   "challenges":[
     ["探测盲区覆盖不足","无线电静默、自主飞行无人机难以发现"],
     ["装备零散难以协同","侦测、干扰、反制装备独立操作"],
     ["智能研判精准度低","鸟群、风筝等干扰误报频发"],
     ["处置手段单一滞后","以射频干扰驱离为主，缺乏分层处置"]],
   "archSol":{"img":"data/客户案例/低空安全-解决方案架构图.png","h":300,"label":"三大系统一体联动架构图"},
   "solution":[
     ["情指行一体","AI 赋能情报分析、指挥调度、行动支撑"],
     ["平峰一体","日常防控 + 特情防控全程保障"],
     ["察打一体","无人机侦查 + 无人机反制一体联动"]],
   "archRes":{"img":"data/客户案例/低空安全-关键成效图.png","h":260,"label":"关键成效架构图"},
   "results":[
     ["重大活动保障","核心区禁飞、预警区全域覆盖"],
     ["城市网格化","千余机型全覆盖，秒级刷新空情"],
     ["边防查缉","无人机走私运毒，AI 侦测定位飞手"],
     ["卫星补盲","遥感变化检测，从源头发现窝点"]],
   "outlook":[
     "全国首批：反恐战线低空数据融合标杆",
     "全国首个：低空反恐实战大模型应用",
     "全国首批：“察打一体”装备体系示范"],
   "place":"华南某地低空安全管控",
   "cta":"已在华南某地低空安全管控中开展应用实践"
 }
},
{
 "id":"emergency-monitor",
 "media":{"type":"video","video":"data/客户案例/应急监测_冰川监测.mp4","note":"冰湖遥感影像 + 应急监测车部署场景"},
 "badge":"创新应用",
 "title":"应急监测，从“事后处置”到“事前预判”",
 "desc":"构建“天—空—地—湖”一体化冰湖灾害链应急监测体系，研发感—通—算—用四维增强技术，"
        "实现裂缝监测、形变预测、态势报告生成，为事中保障和事后处置提供决策辅助。",
 "stats":[{"v":"四维增强","l":"感通算用"},{"v":"天基数据","l":"卫星遥感"},{"v":"AI推演","l":"灾害态势推演"}],
 "colors":{"primary":"#8a1a2a","secondary":"#ff8c42","deep":"#4d0e18",
           "cover":"linear-gradient(135deg,#4d0e18,#8a1a2a 60%,#a32836)",
           "cardCover":"linear-gradient(135deg,#4d0e18,#8a1a2a)"},
 "detail":{
   "subtitle":"平台赋能冰湖灾害链应急监测实践",
   "coverTags":["应急监测","感通算用","天基数据","AI推演"],
   "quote":"极端环境下，人到不了、数据回不来，怎么提前预判？",
   "quoteBy":"—— 某应急监测一线人员",
   "challenges":[
     ["极端环境","高海拔、无网无电无路，人员难以到达"],
     ["数据回传难","卫星链路不稳定，传输效率低"],
     ["监测精度不足","遥感图像模糊、缺失，多源数据未融合"],
     ["决策支撑弱","缺乏态势报告自动生成和灾害推演能力"]],
   "archSol":{"img":"data/客户案例/应急监测-解决方案架构图.png","h":300,"label":"感通算用四维增强架构图"},
   "solution":[
     ["态势感知增强","扩散模型+AI 算法，遥感图像无损放大、降噪、修复"],
     ["网络传输增强","卫星链路优化+数据压缩加密，保障极端环境链路稳定"],
     ["计算增强","边缘计算+平台计算，模型蒸馏 70B→2-5B，三无场景部署"],
     ["应用增强","大模型智能体编排+数字孪生，自动生成态势报告，AI 推演"]],
   "archRes":{"img":"data/客户案例/应急监测-关键成效图.png","h":260,"label":"关键成效架构图"},
   "results":[
     ["监测能力","裂缝监测、形变预测、态势报告生成"],
     ["态势感知","3D 态势感知图，风险点位标注"],
     ["决策支撑","多源数据融合分析，决策辅助和方案支撑"]],
   "outlook":[
     "与应急管理、自然资源、水利等主管部门对接",
     "与自然灾害防治、高原研究等科研机构合作",
     "推动冰湖灾害链应急保障领域创新试点落地"],
   "place":"西南某高原地区",
   "cta":"已在西南某高原地区开展应用实践"
 }
}
]

# 军绿调色板（智慧边防详情页主色）：深 / 主 / 中 / 浅背景 / 边线 / 挑战橙
MIL = "#3E4A2B", "#5A6B3F", "#2F3B22", "#F1F3E6", "#C4CDA8", "#D9632C"

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;")
            .replace(">","&gt;").replace('"',"&quot;"))

def hex2rgb(h):
    h = h.lstrip("#")
    return int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)

# ---------- 各案例独立配色（update1.1 §1.3） ----------
# 智慧边防无 colors → 沿用主平台蓝卡片 + 军绿弹窗默认值（保持原样不动）
def case_theme_css(c):
    col = c.get("colors")
    if not col:
        return ""
    cid = c["id"]
    p, s = col["primary"], col["secondary"]
    r, g, b = hex2rgb(p)
    return """
/* %s 配色 */
.cs-card[data-case="%s"] .cs-cover{background:%s}
.cs-card[data-case="%s"] .cs-badge{background:rgba(%d,%d,%d,.82)}
.cs-card[data-case="%s"] .cs-tag{background:rgba(%d,%d,%d,.10);color:%s}
.cs-card[data-case="%s"] .cs-stat b{color:%s}
.cs-card[data-case="%s"]:hover{border-color:%s}
.cs-card[data-case="%s"]:hover .cs-go{color:%s}
.cmd[data-theme="%s"]{--cover:%s;--p:%s;--s:%s;--panel:#fff;--deep:%s;
  --chal:#ff6b4a;--arch:%s;--archbg:#FAFBFC;--brk:%s;
  --chipbg:rgba(%d,%d,%d,.08);--chipline:rgba(%d,%d,%d,.28);
  --btn:linear-gradient(90deg,%s,%s);--btnc:#fff}
""" % (c["title"], cid, col["cardCover"],
       cid, r, g, b,
       cid, r, g, b, p,
       cid, s,
       cid, p,
       cid, p,
       cid, col["cover"], p, s, col["deep"],
       p, p,
       r, g, b, r, g, b,
       p, s)

themes_css = "".join(case_theme_css(c) for c in CASES)

# ---------- 列表页卡片 ----------
def list_card(c):
    stats = "".join('<div class="cs-stat"><b>%s</b><small>%s</small></div>'
                    % (esc(s["v"]), esc(s["l"])) for s in c["stats"])
    badge = ('<span class="cs-badge"><i class="dot"></i>%s</span>'
             % esc(c["badge"])) if c.get("badge") else ""
    # 卡片标签：取详情页统一标签前 3 个（与详情页一致，无“#”号）
    tags = "".join('<span class="cs-tag">%s</span>' % esc(t)
                   for t in [t.lstrip("#") for t in c["detail"]["coverTags"][:3]])
    href = "case-detail.html" if c["id"] == "smart-border" else "cases.html#case=" + c["id"]
    place = c["detail"].get("place", "")
    place_html = ('<div class="cs-place">'
                  '<svg viewBox="0 0 24 24" width="11" height="11" aria-hidden="true">'
                  '<path d="M12 2C8.1 2 5 5.1 5 9c0 5.2 7 13 7 13s7-7.8 7-13c0-3.9-3.1-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z" fill="currentColor"/></svg>'
                  '已落地 · %s</div>' % esc(place)) if place else ""
    m = c["media"]
    if m.get("video"):
        # 卡片封面：仅加载首帧（preload=metadata）作为封面；放大播放图标触发灯箱
        cover_media = ('<video src="%s" muted loop playsinline preload="metadata"></video>'
                       % esc(m["video"]))
        zoom = ('<button class="cs-zoom" type="button" data-zsrc="%s" aria-label="放大播放" '
                'title="放大播放">&#9654;</button>' % esc(m["video"]))
    elif m.get("img"):
        cover_media = '<img src="%s" alt="%s" loading="lazy">' % (esc(m["img"]), esc(c["title"]))
        zoom = ('<button class="cs-zoom cs-zoom-img" type="button" data-zsrc="%s" '
                'aria-label="放大查看" title="放大查看">&#128269;</button>' % esc(m["img"]))
    else:
        cover_media = ('<div class="cs-cover-ph"><b>&#9654;</b><small>%s</small></div>'
                       % esc(m.get("note", "")))
        zoom = ""
    return """
      <a class="cs-card rv" href="%s" data-case="%s">
        <div class="cs-cover">%s%s%s</div>
        <div class="cs-pb">
          <div class="cs-tags">%s</div>
          <h3>%s</h3>
          <p>%s</p>
          <div class="cs-stats">%s</div>
          <div class="cs-foot">%s<span class="cs-go">查看详情 &#8594;</span></div>
        </div>
      </a>""" % (href, esc(c["id"]), cover_media, badge, zoom, tags,
                 esc(c["title"]), esc(c["desc"]), stats, place_html)

cards_html = "".join(list_card(c) for c in CASES)

cso = """
<div class="banner pad"><div class="banner-in">
  <h1>客户案例</h1>
  <p class="lead">一站式全链路数字化信息服务平台 · 赋能行业智能化转型</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 客户案例</div></div>

<section class="sec">
  <div class="wrap">
    <div class="cs-grid">
      __CARDS__
      <div class="cs-card cs-more rv" aria-disabled="true">
        <div class="cs-cover cs-cover-more"><span class="cs-plus">+</span></div>
        <div class="cs-pb"><h3>更多行业案例即将上线</h3>
          <p>自然资源 · 智慧农业 · 交通物流 · 城市治理……</p></div>
      </div>
    </div>
  </div>
</section>

<!-- ===== 案例详情弹窗（各案例独立配色，内容由 window.CASES 渲染） ===== -->
<div class="cmd" id="caseModal" aria-hidden="true">
  <div class="cmd-mask" data-close="1"></div>
  <div class="cmd-panel" role="dialog" aria-modal="true" aria-labelledby="cmTitle">
    <button class="cmd-x" type="button" data-close="1" aria-label="关闭案例详情">&#10005;</button>
    <div class="cmd-scroll" id="cmScroll"></div>
  </div>
</div>
""".replace("__CARDS__", cards_html)

CASES_CSS = """
<style>
/* ===== 案例列表卡片（默认配色与主平台一致） ===== */
.cs-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.cs-card{display:flex;flex-direction:column;background:#fff;border:1px solid #B4C7E7;
  border-radius:14px;overflow:hidden;text-decoration:none;color:inherit;
  box-shadow:0 2px 8px rgba(15,61,117,.06);transition:transform .2s,box-shadow .2s,border-color .2s}
.cs-card:hover{transform:translateY(-5px);box-shadow:0 16px 40px rgba(10,60,140,.12);
  border-color:#00A0E9}
.cs-cover{position:relative;height:170px;background:linear-gradient(135deg,#0C315E,#1B5A9E);overflow:hidden}
.cs-cover::after{content:"";position:absolute;inset:0;
  background:linear-gradient(to top,rgba(9,37,70,.62),transparent 55%);pointer-events:none}
.cs-cover-ph{position:absolute;inset:0;display:flex;flex-direction:column;gap:8px;
  align-items:center;justify-content:center;color:rgba(255,255,255,.75)}
.cs-cover-ph b{display:flex;align-items:center;justify-content:center;width:44px;height:44px;
  border-radius:50%;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.35);
  font-size:16px}
.cs-cover-ph small{font-size:11.5px}
.cs-cover video,.cs-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cs-badge{position:absolute;top:10px;left:10px;z-index:2;display:inline-flex;align-items:center;gap:7px;
  background:rgba(15,61,117,.82);color:#fff;font-size:12px;font-weight:700;
  padding:4px 10px;border-radius:4px;backdrop-filter:blur(2px)}
.cs-badge .dot{width:7px;height:7px;border-radius:50%;background:#6FE3FF;
  animation:cs-pulse 2s infinite}
@keyframes cs-pulse{0%{box-shadow:0 0 0 0 rgba(111,227,255,.55)}
  70%{box-shadow:0 0 0 7px rgba(111,227,255,0)}100%{box-shadow:0 0 0 0 rgba(111,227,255,0)}}
.cs-pb{padding:16px 18px 18px;display:flex;flex-direction:column;flex:1}
.cs-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.cs-tag{background:#DCE9F5;color:#0F3D75;font-size:11px;font-weight:700;
  padding:2px 8px;border-radius:4px}
.cs-pb h3{font-size:15.5px;color:#0F3D75;margin:0 0 8px;line-height:1.4;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cs-pb p{font-size:13px;color:#33414E;line-height:1.8;margin:0;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.cs-stats{display:flex;gap:18px;flex-wrap:wrap;margin:14px 0 12px;
  padding-top:12px;border-top:1px dashed #D6DEE9}
.cs-stat b{display:block;font-size:20px;font-weight:700;color:#0F3D75}
.cs-stat small{display:block;font-size:11.5px;color:#5C6670;margin-top:2px}
.cs-foot{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:auto}
.cs-place{display:flex;align-items:center;gap:4px;font-size:11.5px;color:#7A8694;
  min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex-shrink:1}
.cs-place svg{flex:none}
.cs-go{font-size:13px;font-weight:700;color:#00608C;flex:none}
.cs-card:hover .cs-go{color:#00A0E9}
/* 占位卡 */
.cs-more{border-style:dashed;background:#FBFCFE;cursor:default}
.cs-more:hover{transform:none;box-shadow:0 2px 8px rgba(15,61,117,.06);border-color:#B4C7E7}
.cs-cover-more{background:#F0F5FB;display:flex;align-items:center;justify-content:center}
.cs-cover-more::after{display:none}
.cs-plus{display:flex;align-items:center;justify-content:center;width:52px;height:52px;
  border-radius:50%;background:#fff;border:1px dashed #9FB6CF;color:#0F3D75;
  font-size:26px;font-weight:400;line-height:1}
.cs-more .cs-pb h3{color:#5C6670}
.cs-more .cs-pb p{display:block;color:#8894A0}
/* ===== 案例详情弹窗（CSS 变量主题化；智慧边防默认军绿） ===== */
.cmd{position:fixed;inset:0;z-index:1200;display:none}
.cmd.open{display:flex;align-items:center;justify-content:center;padding:22px}
.cmd-mask{position:absolute;inset:0;background:rgba(10,22,40,.55);
  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.cmd-panel{position:relative;width:100%;max-width:880px;max-height:92vh;
  background:var(--panel,#F1F3E6);border-radius:18px;overflow:hidden;display:flex;flex-direction:column;
  transform:translateY(48px);opacity:0;transition:transform .35s ease,opacity .35s ease;
  box-shadow:0 24px 70px rgba(15,25,8,.35)}
.cmd.open .cmd-panel{transform:none;opacity:1}
.cmd-x{position:absolute;top:12px;right:12px;z-index:5;width:38px;height:38px;border-radius:50%;
  border:0;background:rgba(255,255,255,.16);color:#fff;font-size:15px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;transition:background .2s}
.cmd-x:hover{background:rgba(255,255,255,.32)}
.cmd-scroll{overflow-y:auto;overscroll-behavior:contain}
/* 封面：案例主色渐变 + 底部遮罩 */
.cm-cover{position:relative;min-height:280px;display:flex;flex-direction:column;
  justify-content:flex-end;padding:26px 30px;
  background:var(--cover,linear-gradient(135deg,#232D18,#3E4A2B 55%,#55663A))}
.cm-cover video,.cm-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cm-cover .cm-shade{position:absolute;inset:0;
  background:linear-gradient(to top,rgba(18,24,10,.88),rgba(18,24,10,.25) 60%,transparent)}
.cm-cover .cm-in{position:relative}
.cm-ctags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}
.cm-ctags span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);
  color:#EAF0DC;font-size:12px;padding:3px 10px;border-radius:4px}
.cm-cover h2{color:#fff;font-size:26px;line-height:1.45;margin:0 0 8px}
.cm-sub{color:#C9D6A8;font-size:14px;margin:0}
/* 正文 */
.cm-body{padding:24px 30px 30px}
.cm-h{display:flex;align-items:center;gap:8px;margin:26px 0 14px;font-size:17px;
  color:var(--deep,#2F3B22);font-weight:700}
.cm-h:first-child{margin-top:0}
.cm-h::before{content:"";width:4px;height:18px;border-radius:2px;
  background:linear-gradient(180deg,var(--p,#5A6B3F),var(--s,#5A6B3F))}
/* 客户原声 */
.cm-quote{background:#fff;border-radius:10px;padding:16px 18px;border-left:4px solid var(--p,#5A6B3F)}
.cm-quote p{margin:0;font-size:15px;line-height:1.95;color:#2E3A20}
.cm-quote small{display:block;margin-top:8px;font-size:12.5px;color:#7C8894}
/* 挑战 2×2：竖线统一橙色系 */
.cm-grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.cm-chal{background:#fff;border-radius:10px;padding:14px 16px;border-left:4px solid var(--chal,#D9632C)}
.cm-chal b{display:block;font-size:14.5px;color:var(--deep,#2F3B22);margin-bottom:5px}
.cm-chal p{margin:0;font-size:13px;line-height:1.8;color:#5C6670}
/* 架构图占位：主色虚线，支持替换真实图片 */
.cm-arch{background:var(--archbg,#F7F9EE);border:1.5px dashed var(--arch,#9DAA84);border-radius:12px;
  display:flex;flex-direction:column;gap:8px;align-items:center;justify-content:center;
  color:#7C8894;overflow:hidden}
.cm-arch img{width:100%;height:100%;object-fit:cover;border:0}
.cm-arch b{font-size:14px;color:var(--p,#5A6B3F)}
.cm-arch small{font-size:11.5px}
/* 方案能力列表：竖线用案例主色 */
.cm-cap{background:#fff;border-radius:10px;padding:14px 16px;border-left:4px solid var(--p,#5A6B3F)}
.cm-cap b{display:block;font-size:14.5px;color:var(--deep,#2F3B22);margin-bottom:5px}
.cm-cap p{margin:0;font-size:13px;line-height:1.8;color:#5C6670}
.cm-type{display:inline-block;font-size:11px;font-weight:700;color:var(--p,#5A6B3F);
  background:var(--chipbg,#EDF0E0);border-radius:4px;padding:2px 8px;margin-bottom:7px}
/* 成效卡片：竖线用辅助色 */
.cm-res{background:#fff;border-radius:10px;padding:14px 16px;border-left:4px solid var(--s,#5A6B3F)}
.cm-res b{display:block;font-size:14.5px;color:var(--deep,#2F3B22);margin-bottom:5px}
.cm-res p{margin:0;font-size:13.5px;line-height:1.8;color:#33414E;font-weight:700}
/* 推广展望 */
.cm-outlook{background:#fff;border-radius:10px;padding:14px 18px;margin:0;list-style:none}
.cm-outlook li{position:relative;padding:8px 0 8px 22px;font-size:13.5px;color:#33414E;line-height:1.8}
.cm-outlook li::before{content:"";position:absolute;left:2px;top:17px;width:9px;height:9px;
  border-radius:2px;background:linear-gradient(135deg,var(--p,#5A6B3F),var(--s,#5A6B3F))}
/* 突破卡（智慧边防） */
.cm-brk{background:#fff;border-radius:10px;overflow:hidden;border:1px solid var(--chipline,#DDE2CB)}
.cm-brk-h{background:var(--brk,#3E4A2B);color:#fff;font-size:14.5px;font-weight:700;padding:10px 16px}
.cm-brk-b{padding:14px 16px}
.cm-brk-b p{margin:0 0 12px;font-size:13px;line-height:1.85;color:#33414E}
.cm-brk-stats{display:flex;flex-wrap:wrap;gap:6px}
.cm-brk-stats span{font-size:11.5px;color:var(--brk,#3E4A2B);background:var(--chipbg,#EDF0E0);
  border:1px solid var(--chipline,#C4CDA8);border-radius:4px;padding:2px 8px;font-weight:700}
/* 底部 CTA：深主色底 + 主色→辅助色渐变按钮 */
.cm-cta{margin-top:26px;background:var(--deep,#2F3B22);border-radius:12px;padding:20px 24px;
  display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.cm-cta p{margin:0;color:#EAF0DC;font-size:14px;line-height:1.8}
.cm-cta .btn-wt{display:inline-block;background:var(--btn,#fff);color:var(--btnc,#2F3B22);
  font-size:14px;font-weight:700;padding:11px 22px;border-radius:6px;text-decoration:none;
  white-space:nowrap;transition:opacity .2s}
.cm-cta .btn-wt:hover{opacity:.88}
.cm-mask-note{margin:10px 0 0;font-size:11.5px;color:#98A4AD}
/* 响应式 */
@media(max-width:960px){.cs-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.cm-grid2{grid-template-columns:1fr}
  .cm-cover{min-height:240px;padding:20px}
  .cm-cover h2{font-size:21px}
  .cm-body{padding:20px 18px 22px}}
@media(max-width:640px){.cs-grid{grid-template-columns:1fr}
  .cmd.open{padding:0;align-items:flex-end}
  .cmd-panel{max-height:94vh;border-radius:18px 18px 0 0}}
@media(prefers-reduced-motion:reduce){.cmd-panel{transition:none}
  .cs-badge .dot{animation:none}
  .cs-card,.cs-card:hover{transition:none}}
/* ===== 视频放大播放（卡片角标 + 弹窗播放按钮 + 灯箱） ===== */
.cs-zoom{position:absolute;top:10px;right:10px;z-index:3;width:30px;height:30px;border-radius:50%;
  background:rgba(0,0,0,.55);color:#fff;border:0;cursor:pointer;font-size:15px;
  display:flex;align-items:center;justify-content:center;backdrop-filter:blur(2px);transition:.2s}
.cs-zoom:hover{background:rgba(0,0,0,.78);transform:scale(1.06)}
.cm-play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;
  gap:10px;background:rgba(0,0,0,.18);color:#fff;border:0;cursor:pointer;z-index:3;transition:.2s}
.cm-play:hover{background:rgba(0,0,0,.32)}
.cm-play .ico{width:72px;height:72px;border-radius:50%;background:rgba(255,255,255,.18);
  border:2px solid rgba(255,255,255,.78);display:flex;align-items:center;justify-content:center;
  font-size:24px;backdrop-filter:blur(3px);box-shadow:0 6px 20px rgba(0,0,0,.4);transition:.2s}
.cm-play:hover .ico{transform:scale(1.08);background:rgba(255,255,255,.28)}
.cm-play small{font-size:13px;font-weight:700;letter-spacing:2px;
  text-shadow:0 2px 6px rgba(0,0,0,.6)}
.vlb{position:fixed;inset:0;z-index:1400;display:flex;align-items:center;justify-content:center}
.vlb[hidden]{display:none}
.vlb-mask{position:absolute;inset:0;background:rgba(0,0,0,.88);backdrop-filter:blur(4px)}
.vlb-inner{position:relative;max-width:1100px;width:92vw;max-height:88vh;background:#000;
  border-radius:8px;overflow:hidden;display:flex;align-items:center;justify-content:center}
.vlb-inner video{width:100%;max-height:88vh;display:block;background:#000}
.vlb-close{position:absolute;top:14px;right:14px;width:38px;height:38px;border-radius:50%;
  background:rgba(255,255,255,.16);color:#fff;border:1px solid rgba(255,255,255,.4);
  font-size:16px;cursor:pointer;backdrop-filter:blur(6px);transition:.2s}
.vlb-close:hover{background:rgba(255,255,255,.28)}
@media(max-width:640px){.cm-play .ico{width:54px;height:54px;font-size:20px}
  .cm-play small{font-size:12px;letter-spacing:1px}}
__THEMES__
</style>
""".replace("__THEMES__", themes_css)

CASES_JS = """
<script>
(function(){
  'use strict';
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var CASES = window.CASES || [];
  var modal = document.getElementById('caseModal');
  if(!modal) return;
  var scroll = document.getElementById('cmScroll');
  var xBtn = modal.querySelector('.cmd-x');
  var lastFocus = null;

  function esc(s){return String(s).replace(/[&<>"]/g,function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function byId(id){for(var i=0;i<CASES.length;i++){if(CASES[i].id===id)return CASES[i];}return null;}

  function archHtml(a){
    var inner = a.img
      ? '<img src="'+esc(a.img)+'" alt="'+esc(a.label)+'">'
      : '<b>'+esc(a.label)+'</b><small>架构图占位 · 支持替换为真实图片</small>';
    return '<div class="cm-arch" style="height:'+a.h+'px">'+inner+'</div>';
  }
  function head(t){return '<div class="cm-h">'+t+'</div>';}
  function coverHtml(c, d, media){
    var ctags = (d.coverTags||[]).map(function(t){return '<span>'+esc(t)+'</span>';}).join('');
    return '<div class="cm-cover">'+media+'<div class="cm-shade"></div><div class="cm-in">'+
        '<div class="cm-ctags">'+ctags+'</div>'+
        '<h2 id="cmTitle">'+esc(c.title)+'</h2>'+
        '<p class="cm-sub">'+esc(d.subtitle||'')+'</p>'+
      '</div></div>';
  }

  /* 智慧边防（旧结构：四大核心能力 + 两大关键突破）——保持不变 */
  function renderLegacy(c){
    var d = c.detail || {};
    var m = c.media || {};
    var media = '';
    if(m.video){
      media='<video src="'+esc(m.video)+'" muted loop playsinline preload="metadata"></video>'
           +'<button class="cm-play" type="button" data-zsrc="'+esc(m.video)+'" aria-label="放大播放">'
           +'<span class="ico">&#9654;</span><small>放大播放</small></button>';
    }
    else if(m.img){media='<img src="'+esc(m.img)+'" alt="'+esc(c.title)+'">'
           +'<button class="cm-play cm-play-img" type="button" data-zsrc="'+esc(m.img)+'" aria-label="放大查看">'
           +'<span class="ico">&#10530;</span><small>放大查看</small></button>';}
    var chal = (d.challenges||[]).map(function(x){
      return '<div class="cm-chal"><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';}).join('');
    var caps = (d.capabilities||[]).map(function(x){
      return '<div class="cm-cap"><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';}).join('');
    var brks = (d.breakthroughs||[]).map(function(x){
      var st=(x.stats||[]).map(function(s){return '<span>'+esc(s)+'</span>';}).join('');
      return '<div class="cm-brk"><div class="cm-brk-h">'+esc(x.title)+
             '</div><div class="cm-brk-b"><p>'+esc(x.desc)+'</p>'+
             '<div class="cm-brk-stats">'+st+'</div></div></div>';}).join('');
    var arch4 = d.arch4 ? archHtml(d.arch4) : '';
    var arch2 = d.arch2 ? archHtml(d.arch2) : '';
    return coverHtml(c, d, media) +
      '<div class="cm-body">'+
        head('客户原声')+
        '<div class="cm-quote"><p>“'+esc(d.quote||'')+'”</p><small>'+esc(d.quoteBy||'')+'</small></div>'+
        head('面临挑战')+'<div class="cm-grid2">'+chal+'</div>'+
        head('四大核心能力')+arch4+
        '<div class="cm-grid2" style="margin-top:12px">'+caps+'</div>'+
        head('两大关键突破')+arch2+
        '<div class="cm-grid2" style="margin-top:12px">'+brks+'</div>'+
        '<div class="cm-cta"><p>'+esc(d.cta||'')+'</p>'+
          '<a class="btn-wt" href="contact.html">联系我们获取方案 &#8594;</a></div>'+
      '</div>';
  }

  /* 新案例（update1.1 结构：解决方案 / 创新点（可选）/ 关键成效 / 推广展望 / CTA+脱敏标注） */
  function renderV11(c){
    var d = c.detail || {};
    var m = c.media || {};
    var media = '';
    if(m.video){
      media='<video src="'+esc(m.video)+'" muted loop playsinline preload="metadata"></video>'
           +'<button class="cm-play" type="button" data-zsrc="'+esc(m.video)+'" aria-label="放大播放">'
           +'<span class="ico">&#9654;</span><small>放大播放</small></button>';
    }
    else if(m.img){media='<img src="'+esc(m.img)+'" alt="'+esc(c.title)+'">'
           +'<button class="cm-play cm-play-img" type="button" data-zsrc="'+esc(m.img)+'" aria-label="放大查看">'
           +'<span class="ico">&#10530;</span><small>放大查看</small></button>';}
    var chal = (d.challenges||[]).map(function(x){
      return '<div class="cm-chal"><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';}).join('');
    var sol = (d.solution||[]).map(function(x){
      var tp = x.length === 3 ? '<span class="cm-type">'+esc(x[0])+'</span>' : '';
      var t = x.length === 3 ? x[1] : x[0], p = x.length === 3 ? x[2] : x[1];
      return '<div class="cm-cap">'+tp+'<b>'+esc(t)+'</b><p>'+esc(p)+'</p></div>';}).join('');
    var res = (d.results||[]).map(function(x){
      return '<div class="cm-res"><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';}).join('');
    var outlook = (d.outlook||[]).map(function(t){return '<li>'+esc(t)+'</li>';}).join('');
    var archSol = d.archSol ? archHtml(d.archSol) : '';
    var archRes = d.archRes ? archHtml(d.archRes) : '';
    return coverHtml(c, d, media) +
      '<div class="cm-body">'+
        head('客户原声')+
        '<div class="cm-quote"><p>“'+esc(d.quote||'')+'”</p><small>'+esc(d.quoteBy||'')+'</small></div>'+
        head('面临挑战')+'<div class="cm-grid2">'+chal+'</div>'+
        head('解决方案')+archSol+
        '<div class="cm-grid2" style="margin-top:12px">'+sol+'</div>'+
        ((d.innovations && d.innovations.length) ?
          (head('创新点')+'<div class="cm-grid2" style="margin-top:12px">'
            +d.innovations.map(function(x){return '<div class="cm-cap"><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';}).join('')
            +'</div>') : '')+
        head('关键成效')+archRes+
        '<div class="cm-grid2" style="margin-top:12px">'+res+'</div>'+
        head('推广展望')+'<ul class="cm-outlook">'+outlook+'</ul>'+
        '<div class="cm-cta"><p>'+esc(d.cta||'')+'</p>'+
          '<a class="btn-wt" href="contact.html">联系我们获取方案 &#8594;</a></div>'+
        '<p class="cm-mask-note">注：案例中客户与地域信息已按脱敏规范处理。</p>'+
      '</div>';
  }

  function render(c){
    var d = c.detail || {};
    scroll.innerHTML = (d.solution || d.results) ? renderV11(c) : renderLegacy(c);
    modal.setAttribute('data-theme', c.id);
    scroll.scrollTop = 0;
  }

  function setHash(id){
    try{ history.replaceState(null,'', id ? '#case='+id : location.pathname+location.search); }
    catch(e){}
  }
  function open(id){
    var c = byId(id);
    if(!c) return;
    render(c);
    modal.classList.add('open');
    modal.setAttribute('aria-hidden','false');
    document.body.style.overflow = 'hidden';
    lastFocus = document.activeElement;
    xBtn.focus();
    setHash(id);
  }
  function close(){
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
    if(lastFocus && lastFocus.focus) lastFocus.focus();
    setHash(null);
  }

  /* 卡片点击 → 弹窗；无 JS 时智慧边防跳独立详情页兜底 */
  Array.prototype.forEach.call(document.querySelectorAll('[data-case]'), function(el){
    el.addEventListener('click', function(e){
      e.preventDefault();
      open(el.getAttribute('data-case'));
    });
  });

  /* 关闭：✕ / 遮罩 / ESC */
  Array.prototype.forEach.call(modal.querySelectorAll('[data-close]'), function(el){
    el.addEventListener('click', close);
  });
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && modal.classList.contains('open')) close();
  });

  /* 入口与 hash 联动：#case=案例id */
  function fromHash(){
    var m = /^#case=([\\w-]+)$/.exec(location.hash);
    if(m) open(m[1]);
  }
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
</script>
<!-- 图片/视频放大播放灯箱 -->
<div id="videoLightbox" class="vlb" hidden aria-hidden="true">
  <div class="vlb-mask"></div>
  <div class="vlb-inner">
    <button class="vlb-close" type="button" aria-label="关闭播放">✕</button>
    <video id="vlbVideo" controls></video>
    <img id="vlbImg" alt="" >
  </div>
</div>
<script>
(function(){
  var lb = document.getElementById('videoLightbox');
  if(!lb) return;
  var v  = document.getElementById('vlbVideo');
  var im = document.getElementById('vlbImg');
  function isVideo(s){return /\.(mp4|webm|mov|m4v)(\?|#|$)/i.test(s||'');}
  function close(){
    lb.hidden = true;
    lb.setAttribute('aria-hidden','true');
    try{v.pause(); v.removeAttribute('src'); v.load();}catch(e){}
    im.removeAttribute('src');
    v.style.display='none'; im.style.display='none';
  }
  function open(src){
    if(isVideo(src)){
      v.src = src; im.removeAttribute('src');
      v.style.display=''; im.style.display='none';
    }else{
      im.src = src; v.removeAttribute('src');
      im.style.display=''; v.style.display='none';
    }
    lb.hidden = false;
    lb.setAttribute('aria-hidden','false');
    if(isVideo(src)) v.play().catch(function(){});
  }
  lb.querySelector('.vlb-close').addEventListener('click', close);
  lb.querySelector('.vlb-mask').addEventListener('click', close);
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && !lb.hidden) close();
  });
  document.addEventListener('click', function(e){
    var t = e.target.closest('[data-zsrc]');
    if(!t) return;
    e.preventDefault();
    e.stopPropagation();
    open(t.getAttribute('data-zsrc'));
  });
})();
</script>
"""

cases_json = json.dumps(CASES, ensure_ascii=False)
cases_head = "<script>window.CASES=%s;</script>%s" % (cases_json, CASES_CSS)

w("cases.html", page("客户案例 | 天元平台",
  "天元平台客户案例：智慧边防、智慧水利、边海防一体化、低空安全、应急监测等行业的智能化实践成果。",
  "cases", cso, extra_head=cases_head, extra_js=CASES_JS))

# ================= 案例独立详情页（军绿主题，智慧边防，本次未改动） =================
D = CASES[0]
d = D["detail"]

def arch_block(a):
    inner = ('<img src="%s" alt="%s">' % (esc(a["img"]), esc(a["label"]))) if a["img"] else \
            ('<b>%s</b><small>架构图占位 · 支持替换为真实图片</small>' % esc(a["label"]))
    return ('<div class="cm-arch" style="height:%dpx">%s</div>' % (a["h"], inner))

chal_html = "".join('<div class="cm-chal"><b>%s</b><p>%s</p></div>'
                    % (esc(x[0]), esc(x[1])) for x in d["challenges"])
caps_html = "".join('<div class="cm-cap"><b>%s</b><p>%s</p></div>'
                    % (esc(x[0]), esc(x[1])) for x in d["capabilities"])
brks_html = "".join(
    '<div class="cm-brk"><div class="cm-brk-h">%s</div><div class="cm-brk-b"><p>%s</p>'
    '<div class="cm-brk-stats">%s</div></div></div>'
    % (esc(b["title"]), esc(b["desc"]),
       "".join('<span>%s</span>' % esc(s) for s in b["stats"]))
    for b in d["breakthroughs"])
spec_html = "".join('<div><span>%s</span><small>%s</small></div>'
                    % (esc(s["v"]), esc(s["l"])) for s in D["stats"])
ctags_html = "".join('<span>%s</span>' % esc(t) for t in d["coverTags"])

cd = """
<div class="banner pad" style="background:linear-gradient(135deg,#232D18,#3E4A2B 55%,#55663A)">
<div class="banner-in">
  <div class="cm-ctags" style="margin-bottom:14px">__CTAGS__</div>
  <h1>__TITLE__</h1>
  <p class="lead">__SUBTITLE__</p>
  <div class="spec">__SPEC__</div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> /
  <a href="cases.html">客户案例</a> / 智慧边防</div></div>

<section class="sec">
  <div class="wrap">
    <div class="cm-body" style="padding:0;max-width:920px;margin:0 auto">
      <div class="cm-h">客户原声</div>
      <div class="cm-quote"><p>“__QUOTE__”</p><small>__QUOTEBY__</small></div>
      <div class="cm-h">面临挑战</div>
      <div class="cm-grid2">__CHAL__</div>
      <div class="cm-h">四大核心能力</div>
      __ARCH4__
      <div class="cm-grid2" style="margin-top:12px">__CAPS__</div>
      <div class="cm-h">两大关键突破</div>
      __ARCH2__
      <div class="cm-grid2" style="margin-top:12px">__BRKS__</div>
      <div class="cm-cta"><p>__CTA__</p>
        <a class="btn-wt" href="contact.html">联系我们获取方案 &#8594;</a></div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k" style="color:#5A6B3F">MORE</div>
      <h2 style="color:#2F3B22">相关推荐</h2></div>
    <div class="grid3 rv">
      <a class="card" href="cases.html"><div class="ico">例</div><h3>更多客户案例</h3>
        <p>返回案例列表，查看各行业实践成果。</p></a>
      <a class="card" href="solutions.html"><div class="ico">解</div><h3>行业解决方案</h3>
        <p>按行业查找业务痛点与对应方案。</p></a>
      <a class="card" href="products.html"><div class="ico">天</div><h3>天元平台产品与能力</h3>
        <p>从数据获取到行动执行的全链路能力。</p></a>
    </div>
  </div>
</section>

<!-- 图片/视频放大播放灯箱 -->
<div id="videoLightbox" class="vlb" hidden aria-hidden="true">
  <div class="vlb-mask"></div>
  <div class="vlb-inner">
    <button class="vlb-close" type="button" aria-label="关闭播放">✕</button>
    <video id="vlbVideo" controls></video>
    <img id="vlbImg" alt="" >
  </div>
</div>
<script>
(function(){
  var lb = document.getElementById('videoLightbox');
  if(!lb) return;
  var v  = document.getElementById('vlbVideo');
  var im = document.getElementById('vlbImg');
  function isVideo(s){return /\.(mp4|webm|mov|m4v)(\?|#|$)/i.test(s||'');}
  function close(){
    lb.hidden = true;
    lb.setAttribute('aria-hidden','true');
    try{v.pause(); v.removeAttribute('src'); v.load();}catch(e){}
    im.removeAttribute('src');
    v.style.display='none'; im.style.display='none';
  }
  function open(src){
    if(isVideo(src)){
      v.src = src; im.removeAttribute('src');
      v.style.display=''; im.style.display='none';
    }else{
      im.src = src; v.removeAttribute('src');
      im.style.display=''; v.style.display='none';
    }
    lb.hidden = false;
    lb.setAttribute('aria-hidden','false');
    if(isVideo(src)) v.play().catch(function(){});
  }
  lb.querySelector('.vlb-close').addEventListener('click', close);
  lb.querySelector('.vlb-mask').addEventListener('click', close);
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && !lb.hidden) close();
  });
  document.addEventListener('click', function(e){
    var t = e.target.closest('[data-zsrc]');
    if(!t) return;
    e.preventDefault();
    e.stopPropagation();
    open(t.getAttribute('data-zsrc'));
  });
})();
</script>
"""
cd = (cd.replace("__CTAGS__", ctags_html).replace("__TITLE__", esc(D["title"]))
        .replace("__SUBTITLE__", esc(d["subtitle"])).replace("__SPEC__", spec_html)
        .replace("__QUOTE__", esc(d["quote"])).replace("__QUOTEBY__", esc(d["quoteBy"]))
        .replace("__CHAL__", chal_html).replace("__ARCH4__", arch_block(d["arch4"]))
        .replace("__CAPS__", caps_html).replace("__ARCH2__", arch_block(d["arch2"]))
        .replace("__BRKS__", brks_html).replace("__CTA__", esc(d["cta"])))

cd_css = CASES_CSS.replace("<style>", "<style>\n/* 独立详情页：复用弹窗组件样式（军绿默认值），仅智慧边防，不含其他案例主题 */"
        ).replace(themes_css, "\n")

w("case-detail.html", page("智慧边防案例 | 天元平台",
  "天元平台智慧边防实践：从“看得见”到“看得准”，误报降低 80%，有效报警率 95% 以上。",
  "cases", cd, extra_head=cd_css))

print("第二批完成（客户案例 PRD + update1.1 版）")
