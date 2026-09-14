# -*- coding: utf-8 -*-
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

def pane(key, name, lead, pain, flow, value, extra=""):
    pl = "".join('<div class="card"><div class="ico">痛</div><h3>%s</h3><p>%s</p></div>' % (a,b) for a,b in pain)
    fl = "".join("<li>%s</li>" % x for x in flow)
    return """
    <div class="pane%s" data-p="%s" id="%s">
      <div class="sec-h left rv"><h2 style="font-size:24px">%s</h2><p>%s</p></div>
      <div class="grid3 rv">%s</div>
      <div class="grid2 rv" style="margin-top:22px">
        <div class="card" style="border-left:3px solid #1B5A9E"><h3>天元方案</h3>
          <p style="line-height:2">%s</p>
          <ul>%s</ul></div>
        <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
          <p style="font-size:19px;font-weight:700;color:#0F3D75;line-height:1.7">%s</p>
          %s</div>
      </div>
    </div>
    """ % (" on" if key=="emergency" else "", key, key, name, lead, pl,
           " → ".join(flow[:4]) if False else "完整链路：", fl, value, extra)

def sec_pane(key, name, lead, pains, steps, value, applies, vals):
    ph = "".join('<div class="card"><div class="ico">痛</div><h3>%s</h3><p>%s</p></div>' % (a,b) for a,b in pains)
    li = "".join("<li>%s</li>" % s for s in steps)
    vl = "".join("<li>%s</li>" % v for v in vals)
    on = " on" if key == "emergency" else ""
    return """
    <div class="pane%s" data-p="%s" id="%s">
      <div class="sec-h left rv"><h2 style="font-size:24px">%s</h2><p>%s</p></div>
      <div class="grid3 rv">%s</div>
      <div class="grid2 rv" style="margin-top:22px">
        <div class="card" style="border-left:3px solid #1B5A9E"><h3>天元方案</h3>
          <ul style="margin-top:8px">%s</ul></div>
        <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
          <p style="font-size:19px;font-weight:700;color:#0F3D75;line-height:1.7;margin-bottom:10px">%s</p>
          <ul>%s</ul>
          <p style="margin-top:12px;font-size:13px;color:#5C6670"><b>适用场景：</b>%s</p></div>
      </div>
    </div>
    """ % (on, key, key, name, lead, ph, li, value, vl, applies)

sol = """
<div class="banner pad"><div class="banner-in">
  <h1>解决方案</h1>
  <p class="lead">基于天元平台能力，主要赋能五大核心场景 —— 从痛点到方案到价值，一一对应。</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 解决方案</div></div>

<section class="sec">
  <div class="wrap">
    <div class="tabs rv">
      <div class="tab on" data-t="emergency">应急管理</div>
      <div class="tab" data-t="resource">自然资源监测</div>
      <div class="tab" data-t="agri">智慧农业</div>
      <div class="tab" data-t="logistics">交通物流</div>
      <div class="tab" data-t="city">城市治理</div>
    </div>
""" \
+ sec_pane("emergency","应急管理","让应急响应从“小时级”缩短至“分钟级”。",
  [("数据获取慢","灾害发生后，卫星数据获取慢，难以及时掌握灾区情况。"),
   ("融合难","无人机、物联网等多源数据难以快速融合，态势不统一。"),
   ("调度依赖人工","指挥调度依赖人工经验，响应链条长。")],
  ["<b>天元·灵观</b>快速获取灾区卫星影像","<b>天元·灵数</b>融合无人机与物联网数据",
   "<b>认知计算与决策引擎</b>进行灾情研判","<b>天元·灵动</b>调度无人机 / 无人车执行救援"],
  "应急响应时间从“小时级”缩短至“分钟级”",
  "抢险救灾、森林防火、防汛抗旱、重大活动保障",
  ["响应链路大幅压缩","多源态势统一呈现","降低一线人员作业风险"]) \
+ sec_pane("resource","自然资源监测","让变化发现从“滞后”变为“及时”。",
  [("监测范围大","国土、林业、水利等监测范围广，覆盖难以周全。"),
   ("巡查成本高","人工巡查投入大，频次受限。"),
   ("变化发现滞后","违建、毁林、污染等问题发现不及时。")],
  ["<b>天元·灵观</b>定期获取遥感影像","<b>天元·灵炼</b>训练变化检测模型",
   "<b>认知计算与决策引擎</b>自动识别违建 / 毁林 / 污染","<b>天元·灵动</b>调度无人机核查"],
  "监测覆盖率提升至 100%，人工巡查成本降低 60%",
  "国土监察、林草监管、水利监测、环保督察",
  ["覆盖范围无盲区","巡查人力显著下降","问题发现前置"]) \
+ sec_pane("agri","智慧农业","让农事决策从“靠经验”变为“靠数据”。",
  [("监测靠经验","农情判断依赖人工经验，缺乏量化依据。"),
   ("病虫害发现晚","病虫害发现滞后，防治窗口易错失。"),
   ("精准作业弱","施药作业粗放，投入与产出不匹配。")],
  ["<b>天元·灵观</b>获取多光谱遥感","<b>天元·灵数</b>融合气象与土壤数据",
   "<b>认知计算与决策引擎</b>进行长势分析与病虫害预警","<b>天元·灵动</b>调度无人机精准施药"],
  "农药使用量减少 30%，产量提升 10–15%",
  "种植监测、病虫害防治、精准施药、产量预估",
  ["投入品使用更精准","产量与品质提升","农事决策有据可依"]) \
+ sec_pane("logistics","交通物流","让偏远地区配送不再难。",
  [("配送难","偏远地区路网条件差，末端配送困难。"),
   ("监测不及时","路况与风险监测滞后，调度被动。"),
   ("协同弱","多式联运各环节协同不足，效率受限。")],
  ["<b>天元·灵观</b>获取路网遥感","<b>天元·灵数</b>融合交通流数据",
   "<b>认知计算与决策引擎</b>进行路径规划与风险预警","<b>天元·灵动</b>调度无人车 / 无人机配送"],
  "偏远地区配送时效提升 50%，物流成本降低 25%",
  "末端配送、干线监控、多式联运、应急运输",
  ["末端可达性提升","运输成本下降","风险预警前置"]) \
+ sec_pane("city","城市治理","让问题从“靠举报发现”变为“主动识别”。",
  [("事项多","城市管理事项繁杂，人力难以全面覆盖。"),
   ("发现靠举报","问题发现依赖群众举报，被动滞后。"),
   ("处置靠人工","处置流程依赖人工派单，周期长。")],
  ["<b>天元·灵观</b>获取城市遥感","<b>天元·灵数</b>融合摄像头与 IoT 数据",
   "<b>认知计算与决策引擎</b>自动识别违建 / 垃圾 / 积水","<b>天元·灵动</b>调度网格员 / 无人设备处置"],
  "问题发现率提升 80%，处置周期缩短 50%",
  "违建巡查、环卫监管、防汛排涝、网格化管理",
  ["问题发现更主动","处置闭环缩短","管理效能提升"]) + """
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CASES</div><h2>相关成功案例</h2></div>
    <div class="grid2 rv">
      <a class="pcard" href="case-detail.html">
        <div class="ph" style="background:linear-gradient(135deg,#0F3D75,#1B5A9E)">【案例配图待补充】</div>
        <div class="pb"><h3>【案例标题占位 · 待补充】</h3>
          <p>【案例摘要占位。客户名称与成果数据须经客户授权后发布。】</p>
          <span class="more">查看案例详情 &#8594;</span></div></a>
      <a class="pcard" href="case-detail.html">
        <div class="ph" style="background:linear-gradient(135deg,#1B5A9E,#3F6491)">【案例配图待补充】</div>
        <div class="pb"><h3>【案例标题占位 · 待补充】</h3>
          <p>【案例摘要占位。客户名称与成果数据须经客户授权后发布。】</p>
          <span class="more">查看案例详情 &#8594;</span></div></a>
    </div>
    <div class="note rv"><b>要求：</b>案例应优先匹配同行业客户，代入感与说服力更高；
      展示前须取得客户书面授权。</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">RESOURCES</div><h2>相关资源</h2></div>
    <div class="grid3 rv">
      <div class="card"><div class="ico">书</div><h3>行业白皮书</h3>
        <p>【白皮书名称待补充】</p>
        <a class="more" href="contact.html">留资下载 &#8594;</a></div>
      <div class="card"><div class="ico">案</div><h3>方案资料</h3>
        <p>《天元行业应用解决方案》系列文档</p>
        <a class="more" href="contact.html">留资下载 &#8594;</a></div>
      <div class="card"><div class="ico">课</div><h3>培训与认证</h3>
        <p>面向合作伙伴的能力建设课程。【课程安排待补充】</p>
        <a class="more" href="contact.html">咨询详情 &#8594;</a></div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2>需要针对你所在行业的定制方案？</h2>
    <p>预约行业顾问，我们将结合你的实际场景提供可落地的方案建议。</p>
    <a class="btn btn-p btn-lg" href="contact.html">预约行业顾问</a></div>
</section>
"""
w("solutions.html", page("解决方案 | 天元平台",
  "天元平台五大核心场景解决方案：应急管理、自然资源监测、智慧农业、交通物流、城市治理。",
  "solutions", sol))
print("解决方案完成")
