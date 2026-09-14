# -*- coding: utf-8 -*-
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ============ 搜索页 ============
IDX = """
<script>
window.SITE_INDEX=[
 {t:"天元平台",d:"一站式场景化数智平台，感通算用一体化全链路闭环。",k:"产品",u:"products.html"},
 {t:"产品与能力",d:"1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用。",k:"产品",u:"products.html"},
 {t:"空天地数据融合引擎",d:"获取、治理与融合卫星遥感、无人机、物联网等多源数据，让天基数据直达业务。",k:"引擎",u:"products.html#fusion"},
 {t:"认知计算与决策引擎",d:"本体建模读懂业务，模型工厂与智能体工厂持续生产，认知计算引擎统一调度。",k:"引擎",u:"products.html#cognition"},
 {t:"具身智能行动执行引擎",d:"面向无人机、无人车、机器狗等多类具身设备，统一调度与厘米级精准作业。",k:"引擎",u:"products.html#embodied"},
 {t:"天元·灵观",d:"天基数据获取，覆盖高、低轨卫星及 44 个全球地面站，获取周期天级→小时级。",k:"产品",u:"products.html#fusion"},
 {t:"天元·灵数",d:"数据治理与融合，多源数据融合，20+ 数据集，50+ 自动化管道。",k:"产品",u:"products.html#fusion"},
 {t:"空天地一体化网络",d:"通信全流程保障，星地链路、5G/专网、边缘组网自适应切换。",k:"产品",u:"products.html#fusion"},
 {t:"天元·灵语",d:"本体建模，Skill 级业务操作，支持 200+ AI 动作。",k:"产品",u:"products.html#cognition"},
 {t:"天元·灵炼",d:"模型工厂，数据在线 AI 标注，大模型后训练，模型迭代月级→周级。",k:"产品",u:"products.html#cognition"},
 {t:"天元·灵智",d:"智能体工厂，支持多智能体任务编排与自我进化。",k:"产品",u:"products.html#cognition"},
 {t:"认知计算引擎",d:"智能体编排框架，自动调度数据、模型、智能体与 Skill。",k:"产品",u:"products.html#cognition"},
 {t:"天元·灵动",d:"具身智能调度，覆盖无人机、无人车、机器狗，作业精度厘米级。",k:"产品",u:"products.html#embodied"},
 {t:"天元·灵集",d:"数智市集，数智资产广场 + 智能体及技能广场 + 天元·信息服务助手。",k:"产品",u:"products.html#market"},
 {t:"天元·智算底座",d:"智算集群 / 高速互联 / 边云协同，国产化全栈适配。",k:"产品",u:"products.html#infra"},
 {t:"全栈安全合规",d:"身份与访问控制、数据安全与隐私、AI 安全治理、行为审计与溯源。",k:"产品",u:"products.html#security"},
 {t:"解决方案",d:"应急管理、自然资源监测、智慧农业、交通物流、城市治理。",k:"解决方案",u:"solutions.html"},
 {t:"客户案例",d:"天元平台赋能各行业的实践成果，点击卡片查看案例详情。",k:"案例",u:"cases.html"},
 {t:"智慧边防案例",d:"从“看得见”到“看得准”：四大核心能力 + 两大关键突破，误报降低 80%，有效报警率 95%+。",k:"案例",u:"case-detail.html"},
 {t:"关于我们",d:"研究院简介、发展历程与资质荣誉。",k:"关于",u:"about.html"},
 {t:"新闻动态",d:"平台进展、技术成果与行业合作资讯。",k:"动态",u:"news.html"},
 {t:"加入我们",d:"算法、研发、产品与市场岗位。",k:"招聘",u:"careers.html"},
 {t:"联系我们",d:"商务合作、技术支持与在线咨询表单。",k:"联系",u:"contact.html"},
 {t:"隐私政策",d:"个人信息收集、使用、存储与删除说明。",k:"合规",u:"legal.html"},
 {t:"服务条款",d:"网站使用规范与免责声明。",k:"合规",u:"legal.html#terms"},
 {t:"Cookie 声明",d:"Cookie 类型、用途与管理方式。",k:"合规",u:"legal.html#cookie"},
 {t:"网站地图",d:"全站页面结构一览。",k:"导航",u:"sitemap.html"}
];
</script>
"""
sr = """
<div class="banner pad"><div class="banner-in">
  <h1>站内搜索</h1>
  <p class="lead">支持标题、摘要与标签检索，关键词高亮显示。</p>
  <div style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap;max-width:760px">
    <input id="searchInput" type="search" autocomplete="off"
      placeholder="输入关键词，如“应急”“低空”“案例”"
      style="flex:1;min-width:240px;min-height:50px;padding:12px 16px;border-radius:4px;
      border:1px solid rgba(255,255,255,.45);background:rgba(255,255,255,.14);
      color:#fff;font-size:15px;font-family:inherit">
    <button id="searchBtn" class="btn btn-p btn-lg" type="button">搜索</button>
  </div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 站内搜索</div></div>

<section class="sec">
  <div class="wrap">
    <div class="filter-bar rv" style="justify-content:space-between">
      <span id="histBox" style="display:none">
        <span class="lb">最近搜索</span><span id="histList" style="display:inline"></span>
        <button id="clearHist" class="clear-all" type="button">一键清除</button>
      </span>
      <span>
        <span class="lb">排序</span>
        <select id="sortSel" style="min-height:38px;padding:6px 12px;border:1px solid #BEC3C8;
          border-radius:4px;font-size:13px;font-family:inherit">
          <option value="rel">按相关度</option>
        </select>
      </span>
    </div>

    <div id="resBox" class="rv" style="display:none">
      <p style="font-size:14px;color:#5C6670;margin-bottom:14px">
        找到 <b id="resCount" style="color:#0F3D75">0</b> 条与
        “<b id="resWord" style="color:#0F3D75"></b>” 相关的结果</p>
      <div class="nlist" id="resList"></div>
    </div>

    <div id="emptyBox" class="rv" style="display:none;background:#fff;border:1px solid #BEC3C8;
      border-radius:8px;padding:40px 30px;text-align:center">
      <h3 style="font-size:18px;color:#0F3D75;margin-bottom:10px">没有找到相关结果</h3>
      <p style="font-size:14px;color:#5C6670;margin-bottom:20px">
        换个关键词试试，或直接浏览下面的热门内容。</p>
      <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap">
        <a class="btn btn-s" href="products.html">天元平台</a>
        <a class="btn btn-s" href="solutions.html">解决方案</a>
        <a class="btn btn-s" href="cases.html">客户案例</a>
        <a class="btn btn-s" href="contact.html">联系我们</a></div>
    </div>

    <div class="info rv"><b>隐私说明：</b>搜索历史保存在浏览器本地（localStorage），
      不上传服务器；保留最近 10 条，30 天自动过期，支持一键清除。</div>
  </div>
</section>
"""
w("search.html", page("站内搜索 | 天元平台",
  "在天元官网内检索产品、解决方案、案例与资讯。", "index", sr, extra_head=IDX))

# ============ 404 ============
e404 = """
<div class="banner pad" style="text-align:center"><div class="banner-in">
  <div style="font-size:88px;font-weight:700;color:#00A0E9;line-height:1">404</div>
  <h1 style="margin-top:14px">页面走失了</h1>
  <p class="lead" style="margin:14px auto 0">你访问的页面不存在或已被移动。不必担心，
    可以从下面这些地方重新开始。</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px">
    <a class="btn btn-p btn-lg" href="index.html">返回首页</a>
    <a class="btn btn-o btn-lg" href="search.html">站内搜索</a></div>
</div></div>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">POPULAR</div><h2>热门页面</h2></div>
    <div class="grid3 rv">
      <a class="card" href="products.html"><div class="ico">天</div>
        <h3>天元平台</h3><p>产品与能力：分层能力与产品清单。</p></a>
      <a class="card" href="solutions.html"><div class="ico">解</div>
        <h3>解决方案</h3><p>按行业查找痛点与对应方案。</p></a>
      <a class="card" href="contact.html"><div class="ico">联</div>
        <h3>联系我们</h3><p>商务咨询与技术支持。</p></a>
    </div>
  </div>
</section>
"""
w("404.html", page("页面不存在（404） | 天元平台",
  "页面走失了，请返回首页或前往热门页面。", "index", e404))

# ============ 500 ============
e500 = """
<div class="banner pad" style="text-align:center"><div class="banner-in">
  <div style="font-size:88px;font-weight:700;color:#00A0E9;line-height:1">500</div>
  <h1 style="margin-top:14px">系统正在紧急维护中</h1>
  <p class="lead" style="margin:14px auto 0">预计稍后恢复，请耐心等待。
    给您带来不便，我们深表歉意。</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px">
    <a class="btn btn-p btn-lg" href="index.html">返回首页</a>
    <a class="btn btn-o btn-lg" href="contact.html">联系我们</a></div>
</div></div>
<section class="sec"><div class="wrap">
  <div class="form rv">
    <h3 style="color:#0F3D75;margin-bottom:12px">其他联系方式</h3>
    <p style="font-size:14px;color:#5C6670;line-height:2">
      技术支持：<a href="mailto:【待补充】" style="color:#00608C">【待补充】</a><br>
      服务电话：<a href="tel:【待补充】" style="color:#00608C">【待补充】</a><br>
      工作时间：工作日 9:00–17:30
    </p>
    <div class="info" style="margin-top:18px"><b>实现建议：</b>预计恢复时间优先采用后台动态配置；
      无配置时展示本页静态兜底文案，避免出现空白或报错代码。</div>
  </div>
</div></section>
"""
w("500.html", page("系统维护中（500） | 天元平台",
  "系统正在紧急维护中，预计稍后恢复。", "index", e500))

# ============ 合规页 ============
lg = """
<div class="banner pad"><div class="banner-in">
  <h1>法律与合规</h1>
  <p class="lead">隐私政策 · 服务条款 · Cookie 声明</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 法律与合规</div></div>

<section class="sec">
  <div class="wrap">
    <div class="tabs rv">
      <div class="tab on" data-t="privacy">隐私政策</div>
      <div class="tab" data-t="terms">服务条款</div>
      <div class="tab" data-t="cookie">Cookie 声明</div>
    </div>

    <div class="pane on" data-p="privacy" id="privacy">
      <div class="form rv">
        <h2 style="color:#0F3D75;margin-bottom:16px;font-size:22px">隐私政策</h2>
        <p style="color:#5C6670;line-height:2">
          <b style="color:#0F3D75">一、我们收集的信息</b><br>
          当你通过本网站的咨询表单联系我们时，我们会收集你主动填写的姓名、手机号，
          以及你选填的单位名称与需求描述。除此之外，我们仅收集保障网站正常运行所必需的技术信息。<br><br>
          <b style="color:#0F3D75">二、信息的使用</b><br>
          收集的信息仅用于与你联系、回应你的咨询，以及改进网站服务。
          <b>我们不会将你的个人信息用于其他目的，也不会向无关第三方出售或提供。</b><br><br>
          <b style="color:#0F3D75">三、信息的存储与保护</b><br>
          我们采取符合行业标准的技术与管理措施保护你的信息，
          存储期限为实现处理目的所必需的最短时间，法律法规另有规定的从其规定。<br><br>
          <b style="color:#0F3D75">四、你的权利</b><br>
          你有权查询、复制、更正、删除我们持有的你的个人信息，也有权撤回此前作出的同意。
          如需行使上述权利，可通过<a href="contact.html" style="color:#00608C;text-decoration:underline">本页</a>
          提供的联系方式与我们联系，我们将在法定期限内响应。<br><br>
          <b style="color:#0F3D75">五、政策更新</b><br>
          本政策可能随法律法规与业务变化而更新，更新后的版本将在本页公布。
        </p>
        <div class="note"><b>待审：</b>本条款为通用模板文本，正式发布前须由法务与合规部门审定，
          并补充数据留存期限、跨境传输（如涉及）、未成年人信息处理等具体条款。</div>
      </div>
    </div>

    <div class="pane" data-p="terms" id="terms">
      <div class="form rv">
        <h2 style="color:#0F3D75;margin-bottom:16px;font-size:22px">服务条款</h2>
        <p style="color:#5C6670;line-height:2">
          <b style="color:#0F3D75">一、使用规范</b><br>
          你在使用本网站时，不得从事任何违反法律法规、
          损害国家利益或侵害他人合法权益的行为；不得通过技术手段干扰网站的正常运行。<br><br>
          <b style="color:#0F3D75">二、知识产权</b><br>
          本网站的内容（包括但不限于文字、图片、标识、版式设计）受相关法律法规保护。
          <b>未经书面许可，不得转载、复制或用于商业用途。</b><br><br>
          <b style="color:#0F3D75">三、免责声明</b><br>
          本网站所载信息仅供参考。我们会努力确保内容准确，
          <b>但不对信息的完整性、时效性与适用性作出明示或默示的保证。</b>
          因使用本网站信息而产生的任何后果，由使用者自行承担。<br><br>
          <b style="color:#0F3D75">四、条款变更</b><br>
          我们保留在必要时修改本条款的权利，修改后的条款将在本页公布。
        </p>
        <div class="note"><b>待审：</b>须由法务部门审定后发布，关键条款可按规范要求加粗标注。</div>
      </div>
    </div>

    <div class="pane" data-p="cookie" id="cookie">
      <div class="form rv">
        <h2 style="color:#0F3D75;margin-bottom:16px;font-size:22px">Cookie 声明</h2>
        <p style="color:#5C6670;line-height:2">
          <b style="color:#0F3D75">一、什么是 Cookie</b><br>
          Cookie 是网站存储在你浏览器中的小型文本文件，用于识别你的设备与记录偏好。<br><br>
          <b style="color:#0F3D75">二、我们使用的类型</b><br>
          <b>必要 Cookie：</b>保障网站基本功能运行，如记录你的 Cookie 偏好选择，无法关闭。<br>
          <b>偏好 Cookie：</b>记录你的界面与浏览设置，提升使用体验。<br><br>
          <b style="color:#0F3D75">三、如何管理</b><br>
          你可以通过本站底部的 Cookie 提示条选择“仅必要 Cookie”，
          也可以在浏览器设置中删除或阻止 Cookie。你的选择会被记录在本地，不会重复打扰。<br><br>
          <b style="color:#0F3D75">四、说明</b><br>
          <b>本网站目前不使用用于广告投放或跨站追踪的 Cookie。</b>
          若未来引入相关功能，我们将在本页更新说明并重新征求你的同意。
        </p>
        <div class="info"><b>实现说明：</b>Cookie 提示条在首次访问时弹出，
          用户选择记录在 localStorage，避免每次访问重复弹出。</div>
      </div>
    </div>
  </div>
</section>
"""
w("legal.html", page("隐私政策 · 服务条款 · Cookie 声明 | 天元平台",
  "天元官网的隐私政策、服务条款与 Cookie 声明。", "index", lg))

# ============ 网站地图 ============
sm = """
<div class="banner pad"><div class="banner-in">
  <h1>网站地图</h1>
  <p class="lead">全站页面结构一览，便于快速定位。</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 网站地图</div></div>

<section class="sec"><div class="wrap">
  <div class="grid2 rv">
    <div class="card">
      <h3>P0 · 核心页面</h3>
      <ul style="margin-top:10px">
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="index.html">首页</a></li>
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="products.html">产品总览</a></li>
        <li style="padding:7px 0"><a href="contact.html">联系我们</a></li>
      </ul></div>
    <div class="card">
      <h3>P1 · 信任与深度信息</h3>
      <ul style="margin-top:10px">
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="products.html">产品与能力 · 天元平台</a></li>
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="cases.html">案例总览</a></li>
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="case-detail.html">案例详情</a></li>
        <li style="padding:7px 0"><a href="about.html">关于我们</a></li>
      </ul></div>
    <div class="card">
      <h3>P2 · 内容与扩展</h3>
      <ul style="margin-top:10px">
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="news.html">新闻动态</a></li>
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="careers.html">加入我们</a></li>
        <li style="padding:7px 0"><a href="solutions.html">解决方案</a></li>
      </ul></div>
    <div class="card">
      <h3>P3 · 体验兜底与合规</h3>
      <ul style="margin-top:10px">
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="search.html">站内搜索</a></li>
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="404.html">404 页面</a></li>
        <li style="padding:7px 0;border-bottom:1px solid #D6DCE1"><a href="500.html">500 页面</a></li>
        <li style="padding:7px 0"><a href="legal.html">隐私 / 条款 / Cookie</a></li>
      </ul></div>
  </div>
  <div class="info rv"><b>多语言规划：</b>语言切换位于导航栏右侧，URL 采用 /zh/、/en/ 语义化结构；
    默认语言根据浏览器语言自动检测并支持手动切换；翻译缺失时回退至默认语言版本。
    翻译资源建议以 JSON/YAML 独立管理，与代码仓库分离。</div>
</div></section>
"""
w("sitemap.html", page("网站地图 | 天元平台",
  "天元官网全站页面结构一览。", "index", sm))

print("第四批完成")
