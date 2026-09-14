# -*- coding: utf-8 -*-
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

ARCH = """
<section class="sec alt">
  <div class="wrap">
    <div class="sec-h rv"><div class="k">ARCHITECTURE</div><h2>1 + 3 + 1 + N　产品体系</h2>
      <p>1 个底座 + 3 大核心引擎 + 1 个安全体系 + N 个行业应用，
        实现从卫星原始数据获取到行动指令下达的全链路闭环。</p></div>
    <div class="rv" style="background:#fff;border:1px solid #BEC3C8;border-radius:8px;padding:26px 22px">
      <div style="background:#EEF4FA;border:1px solid #BEC3C8;border-radius:6px;padding:16px;
        text-align:center;margin-bottom:9px">
        <b style="color:#0F3D75;font-size:15px">N 个行业应用</b><br>
        <span style="font-size:12.5px;color:#5C6670">应急管理 · 自然资源 · 智慧农业 · 交通物流 · 城市治理</span></div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-bottom:9px">
        <div style="background:#E8EEF5;border:1px solid #BEC3C8;border-radius:6px;padding:15px 8px;text-align:center">
          <b style="color:#0F3D75;font-size:13.5px">空天地数据融合引擎</b><br>
          <span style="font-size:11.5px;color:#5C6670">数据从哪来</span></div>
        <div style="background:#E8EEF5;border:1px solid #BEC3C8;border-radius:6px;padding:15px 8px;text-align:center">
          <b style="color:#0F3D75;font-size:13.5px">认知计算与决策引擎</b><br>
          <span style="font-size:11.5px;color:#5C6670">数据怎么用</span></div>
        <div style="background:#E8EEF5;border:1px solid #BEC3C8;border-radius:6px;padding:15px 8px;text-align:center">
          <b style="color:#0F3D75;font-size:13.5px">具身智能行动执行引擎</b><br>
          <span style="font-size:11.5px;color:#5C6670">指令怎么执行</span></div>
      </div>
      <div style="background:#0F3D75;color:#fff;border-radius:6px;padding:16px;text-align:center;margin-bottom:9px">
        <b>天元 · 智算底座</b><br>
        <span style="font-size:12.5px;color:#CFDCEA">国产化 · 高性能 · 算力与存储支撑</span></div>
      <div style="background:#FAE7EA;border:1px solid #C8102E;border-radius:6px;padding:13px;text-align:center">
        <b style="color:#C8102E;font-size:13.5px">全栈安全合规体系　横向贯穿所有层级</b><br>
        <span style="font-size:12px;color:#5C6670">身份与访问控制 · 数据安全与隐私 · AI 安全治理 · 行为审计与溯源</span></div>
    </div>
    <div class="info rv"><b>说明：</b>安全体系不是独立层级，而是横向贯穿基础设施、
      数据感知、认知决策、行动管控四层的支撑体系。</div>
  </div>
</section>
"""

# ============ 首页 ============
idx = """
<header class="banner">
  <div class="banner-in" style="padding:96px 24px 88px">
    <span style="display:inline-block;background:#00A0E9;color:#1A1A1A;font-size:12.5px;
      font-weight:700;padding:5px 14px;border-radius:3px;letter-spacing:1px;margin-bottom:20px">
      空天地一体化 · 全链路闭环</span>
    <h1>天元<br>一站式场景化<br><em>数智平台</em></h1>
    <p class="lead">基于空天地一体化数据，融合人工智能与智能体技术，实现从卫星原始数据获取到
      行动指令下达的全链路闭环，为客户提供“感、通、算、用”一体化的数智化解决方案。</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:32px">
      <a class="btn btn-p btn-lg" href="product-detail.html">了解平台能力</a>
      <a class="btn btn-o btn-lg" href="contact.html">预约演示</a>
    </div>
    <div class="spec">
      <div><span>45+</span><small>全球地面站</small></div>
      <div><span>1+3+1+1+N</span><small>产品体系架构</small></div>
      <div><span>5</span><small>大核心场景</small></div>
      <div><span>国产全栈</span><small>自主可控适配</small></div>
    </div>
  </div>
</header>

<!-- 差异化优势 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h rv"><div class="k">WHY TIANYUAN</div><h2>四大差异化优势</h2>
      <p>与通用云平台不同，天元的核心差异在于数据源、闭环能力、国产化与智能体驱动。</p></div>
    <div class="grid4">
      <div class="card rv"><div class="ico">源</div><h3>空天地一体化数据源</h3>
        <p>覆盖高、低轨卫星及 45+ 全球地面站，实现天基数据直达业务。</p></div>
      <div class="card rv"><div class="ico">链</div><h3>全链路闭环</h3>
        <p>从数据获取、治理、认知决策到终端执行，无需拼接多家供应商。</p></div>
      <div class="card rv"><div class="ico">国</div><h3>国产化全栈适配</h3>
        <p>从算力底座到 AI 模型，满足自主可控要求。</p></div>
      <div class="card rv"><div class="ico">智</div><h3>智能体驱动</h3>
        <p>多智能体任务编排与自我进化，让系统越用越聪明。</p></div>
    </div>
  </div>
</section>
""" + ARCH + """
<!-- 三大核心引擎 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h rv"><div class="k">CORE ENGINES</div><h2>三大核心引擎</h2>
      <p>分别回答三个问题：数据从哪来、数据怎么用、指令怎么执行。</p></div>
    <div class="grid3">
      <a class="pcard rv" href="products.html#engine">
        <div class="ph" style="background:linear-gradient(135deg,#0F3D75,#1B5A9E)">
          <span class="ph-tag">数据从哪来</span>空天地数据融合引擎</div>
        <div class="pb"><h3>空天地数据融合引擎</h3>
          <p>以空天地一体化数据源为核心，快速获取、治理与融合卫星遥感、无人机、物联网等多源数据，
            并通过星地链路、5G/专网、边缘组网自适应切换保障传输，让天基数据直达业务。</p>
          <ul style="margin-top:10px;font-size:12.5px;color:#5C6670">
            <li>天元·灵观 · 天元·灵数 · 空天地一体化网络</li>
            <li>数据获取周期：天级 → 小时级</li></ul>
          <span class="more">查看详情 &#8594;</span></div></a>
      <a class="pcard rv" href="products.html#engine">
        <div class="ph" style="background:linear-gradient(135deg,#1B5A9E,#3F6491)">
          <span class="ph-tag">数据怎么用</span>认知计算与决策引擎</div>
        <div class="pb"><h3>认知计算与决策引擎</h3>
          <p>以本体建模读懂业务，以模型工厂和智能体工厂持续生产模型与智能体，
            并由认知计算引擎统一调度数据、模型、智能体与 Skill，形成从数据到决策的流程闭环。</p>
          <ul style="margin-top:10px;font-size:12.5px;color:#5C6670">
            <li>天元·灵语 · 天元·灵炼 · 天元·灵智 · 认知计算引擎</li>
            <li>模型迭代：月级 → 周级</li></ul>
          <span class="more">查看详情 &#8594;</span></div></a>
      <a class="pcard rv" href="products.html#engine">
        <div class="ph" style="background:linear-gradient(135deg,#0C315E,#16487E)">
          <span class="ph-tag">指令怎么执行</span>具身智能行动执行引擎</div>
        <div class="pb"><h3>具身智能行动执行引擎</h3>
          <p>面向无人机、无人车、机器狗等多类具身设备，实现统一调度与链路自适应下发，
            结合视觉增强完成厘米级精准作业，打通从决策到行动的最后一公里。</p>
          <ul style="margin-top:10px;font-size:12.5px;color:#5C6670">
            <li>天元·灵动</li>
            <li>多设备协同效率提升 50%，作业精度厘米级</li></ul>
          <span class="more">查看详情 &#8594;</span></div></a>
    </div>
    <div style="text-align:center;margin-top:30px">
      <a class="btn btn-s" href="products.html">查看全部产品能力 &#8594;</a></div>
  </div>
</section>

<!-- 五大场景 -->
<section class="sec alt" id="scene">
  <div class="wrap">
    <div class="sec-h rv"><div class="k">SCENARIOS</div><h2>五大核心行业场景</h2>
      <p>从卫星数据到行动指令，一个平台跑完全流程。</p></div>
    <div class="tabs rv">
      <div class="tab on" data-t="emergency">应急管理</div>
      <div class="tab" data-t="resource">自然资源</div>
      <div class="tab" data-t="agri">智慧农业</div>
      <div class="tab" data-t="logistics">交通物流</div>
      <div class="tab" data-t="city">城市治理</div>
    </div>
    <div class="pane on" data-p="emergency"><div class="grid3">
      <div class="card"><h3>典型痛点</h3><p>灾害发生后，卫星数据获取慢、多源数据融合难、指挥调度依赖人工。</p></div>
      <div class="card"><h3>天元方案</h3><p>灵观快速获取灾区卫星影像 → 灵数融合无人机与物联网数据 →
        认知计算与决策引擎进行灾情研判 → 天元·灵动调度无人机 / 无人车执行救援。</p></div>
      <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
        <p style="font-size:17px;font-weight:700;color:#0F3D75">应急响应时间
          从“小时级”缩短至“分钟级”</p></div>
    </div></div>
    <div class="pane" data-p="resource"><div class="grid3">
      <div class="card"><h3>典型痛点</h3><p>国土、林业、水利等监测范围大，人工巡查成本高，变化发现滞后。</p></div>
      <div class="card"><h3>天元方案</h3><p>灵观定期获取遥感影像 → 灵炼训练变化检测模型 →
        认知计算与决策引擎自动识别违建 / 毁林 / 污染 → 天元·灵动调度无人机核查。</p></div>
      <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
        <p style="font-size:17px;font-weight:700;color:#0F3D75">监测覆盖率提升至 100%，
          人工巡查成本降低 60%</p></div>
    </div></div>
    <div class="pane" data-p="agri"><div class="grid3">
      <div class="card"><h3>典型痛点</h3><p>农情监测靠经验，病虫害发现晚，精准作业能力弱。</p></div>
      <div class="card"><h3>天元方案</h3><p>天元·灵观获取多光谱遥感 → 天元·灵数融合气象与土壤数据 →
        认知计算与决策引擎进行长势分析与病虫害预警 → 天元·灵动调度无人机精准施药。</p></div>
      <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
        <p style="font-size:17px;font-weight:700;color:#0F3D75">农药使用量减少 30%，
          产量提升 10–15%</p></div>
    </div></div>
    <div class="pane" data-p="logistics"><div class="grid3">
      <div class="card"><h3>典型痛点</h3><p>偏远地区配送难，路况监测不及时，多式联运协同弱。</p></div>
      <div class="card"><h3>天元方案</h3><p>天元·灵观获取路网遥感 → 天元·灵数融合交通流数据 →
        认知计算与决策引擎进行路径规划与风险预警 → 天元·灵动调度无人车 / 无人机配送。</p></div>
      <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
        <p style="font-size:17px;font-weight:700;color:#0F3D75">偏远地区配送时效提升 50%，
          物流成本降低 25%</p></div>
    </div></div>
    <div class="pane" data-p="city"><div class="grid3">
      <div class="card"><h3>典型痛点</h3><p>城市管理事项多，发现靠举报，处置靠人工。</p></div>
      <div class="card"><h3>天元方案</h3><p>天元·灵观获取城市遥感 → 天元·灵数融合摄像头与 IoT 数据 →
        认知计算与决策引擎自动识别违建 / 垃圾 / 积水 → 天元·灵动调度网格员 / 无人设备处置。</p></div>
      <div class="card" style="border-left:3px solid #00A0E9"><h3>客户价值</h3>
        <p style="font-size:17px;font-weight:700;color:#0F3D75">问题发现率提升 80%，
          处置周期缩短 50%</p></div>
    </div></div>
    <div style="text-align:center;margin-top:30px">
      <a class="btn btn-s" href="solutions.html">查看完整解决方案 &#8594;</a></div>
  </div>
</section>

<!-- 为什么选择天元 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-h rv"><div class="k">COMPARISON</div><h2>为什么选择天元</h2>
      <p>与竞品常见情况的五个维度对比。</p></div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th>维度</th><th>天元优势</th><th>竞品常见情况</th></tr></thead>
      <tbody>
        <tr><td style="color:#0F3D75;font-weight:700">数据源</td>
          <td>空天地一体化，45+ 全球地面站</td><td>以地面数据为主，天基数据依赖第三方</td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">全链路</td>
          <td>从卫星数据到行动指令，一站式闭环</td><td>需拼接多家供应商，集成成本高</td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">国产化</td>
          <td>国产全栈适配，自主可控</td><td>部分依赖国外算力 / 模型</td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">智能化</td>
          <td>多智能体编排，自我进化</td><td>单点 AI 能力，缺乏系统级智能</td></tr>
        <tr><td style="color:#0F3D75;font-weight:700">安全</td>
          <td>全栈安全合规，数据不出域</td><td>安全能力碎片化</td></tr>
      </tbody></table></div>
    <div class="info rv"><b>说明：</b>上表为产品能力定位对比，
      竞品描述为行业常见情况概括，不指向特定厂商。</div>
  </div>
</section>

<!-- 新闻动态 -->
<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">NEWS</div><h2>新闻动态</h2></div>
    <div class="nlist rv">
      <a href="news.html"><div class="nd"><b>【待补】</b><small>日期</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位 · 待补充。正式发布前请替换为已审定的公开稿件。】</p></div>
        <div class="nt"><span>要闻</span></div></a>
      <a href="news.html"><div class="nd"><b>【待补】</b><small>日期</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位 · 待补充。正式发布前请替换为已审定的公开稿件。】</p></div>
        <div class="nt"><span>技术</span></div></a>
      <a href="news.html"><div class="nd"><b>【待补】</b><small>日期</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位 · 待补充。正式发布前请替换为已审定的公开稿件。】</p></div>
        <div class="nt"><span>生态</span></div></a>
    </div>
    <div style="text-align:center;margin-top:26px">
      <a class="btn btn-s" href="news.html">查看全部动态 &#8594;</a></div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>从卫星原始数据，到可直接下达的行动指令</h2>
    <p>欢迎行业客户与合作伙伴联系我们，留下姓名与电话，我们将在工作日内与您联系。</p>
    <a class="btn btn-p btn-lg" href="contact.html">获取行业解决方案</a>
  </div>
</section>
"""
w("index.html", page("天元 · 一站式场景化数智平台 | 首页",
  "天元平台基于空天地一体化数据，融合人工智能与智能体技术，实现从卫星原始数据获取到行动指令下达的全链路闭环。",
  "index", idx))

# 注：产品与能力页已迁移至 build_prod.py（依据《产品详情V1.2》+《引擎V1.2》重建）
