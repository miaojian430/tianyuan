# -*- coding: utf-8 -*-
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

ct = """
<div class="banner pad"><div class="banner-in">
  <h1>联系我们</h1>
  <p class="lead">无论是业务咨询、技术对接还是生态合作，请告诉我们你的需求，我们将在工作日内响应。</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 联系我们</div></div>

<section class="sec">
  <div class="wrap">
    <div class="grid2">
      <div class="rv">
        <h2 style="font-size:24px;color:#0F3D75;margin-bottom:18px">在线咨询</h2>
        <form class="form" data-validate novalidate>
          <div class="frow"><label>姓名 <i>*</i></label>
            <input type="text" name="name" data-rule="req" autocomplete="name" placeholder="请输入您的姓名">
            <div class="err">请填写姓名</div></div>
          <div class="frow"><label>手机号 <i>*</i></label>
            <input type="tel" name="tel" data-rule="tel" inputmode="numeric" autocomplete="tel"
              maxlength="11" placeholder="请输入 11 位手机号">
            <div class="err">请填写正确的 11 位手机号</div></div>
          <div class="frow"><label>单位名称</label>
            <input type="text" name="org" autocomplete="organization" placeholder="选填"></div>
          <div class="frow"><label>需求描述</label>
            <textarea name="msg" placeholder="选填：简述您关注的行业、场景或问题"></textarea></div>
          <button class="btn btn-p btn-w btn-lg" type="submit">提交咨询</button>
          <div class="form-ok" style="display:none;margin-top:16px;background:#EEF4FA;
            border-left:3px solid #00A0E9;padding:13px 18px;border-radius:4px;
            font-size:13.5px;color:#1A1A1A">
            <b style="color:#0F3D75">提交成功</b>：我们已收到您的咨询，将在 1 个工作日内与您联系。
          </div>
          <p class="fnote">提交即表示您同意我们依据<a href="legal.html">《隐私政策》</a>
            处理您的信息，仅用于本次业务联系，不作他用。</p>
        </form>
      </div>
      <div class="rv">
        <h2 style="font-size:24px;color:#0F3D75;margin-bottom:18px">联系方式</h2>
        <div class="form">
          <p style="font-size:14.5px;line-height:2.1;color:#1A1A1A">
            <b style="color:#0F3D75">商务合作</b><br>
            电话：<a href="tel:【待补充】" style="color:#00608C">【待补充】</a><br>
            邮箱：<a href="mailto:【待补充】" style="color:#00608C">【待补充】</a><br><br>
            <b style="color:#0F3D75">技术支持</b><br>
            邮箱：<a href="mailto:【待补充】" style="color:#00608C">【待补充】</a><br><br>
            <b style="color:#0F3D75">媒体问询</b><br>
            邮箱：<a href="mailto:【待补充】" style="color:#00608C">【待补充】</a><br><br>
            <b style="color:#0F3D75">办公地址</b><br>【待补充】<br><br>
            <b style="color:#0F3D75">工作时间</b><br>工作日 9:00–17:30
          </p>
          <div style="margin-top:22px;padding-top:20px;border-top:1px solid #D6DCE1">
            <b style="color:#0F3D75;font-size:14px">微信公众号</b>
            <div style="margin-top:10px;width:120px;height:120px;background:#EEF4FA;
              border:1px solid #BEC3C8;border-radius:6px;display:flex;align-items:center;
              justify-content:center;font-size:12px;color:#5C6670;text-align:center">
              【二维码待补充】</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">FAQ</div><h2>常见问题</h2></div>
    <div class="faq rv">
      <div class="faq-i"><button class="faq-q" type="button">天元平台与通用云平台有什么不同？<span>+</span></button>
        <div class="faq-a">核心差异在四点：空天地一体化数据源（覆盖高、低轨卫星及 45+ 全球地面站）、
          从数据获取到行动执行的一站式全链路闭环、国产化全栈适配，以及多智能体编排与自我进化能力。</div></div>
      <div class="faq-i"><button class="faq-q" type="button">平台主要赋能哪些行业场景？<span>+</span></button>
        <div class="faq-a">目前主要覆盖应急管理、自然资源监测、智慧农业、交通物流、城市治理五大核心场景。
          更多行业方案详见《天元行业应用解决方案》系列文档。</div></div>
      <div class="faq-i"><button class="faq-q" type="button">如何保障数据与模型的安全？<span>+</span></button>
        <div class="faq-a">全栈安全合规体系横向贯穿所有层级，包括统一身份与分级授权、
          加密脱敏与数据不出域、AI 安全治理（抗注入、对抗防护）、全链路行为审计与溯源。</div></div>
      <div class="faq-i"><button class="faq-q" type="button">是否支持国产化环境部署？<span>+</span></button>
        <div class="faq-a">支持。从算力底座到 AI 模型均满足自主可控要求，
          具体适配清单可在签署保密协议后提供。</div></div>
      <div class="faq-i"><button class="faq-q" type="button">是否提供试用或演示环境？<span>+</span></button>
        <div class="faq-a">【待补充 · 需明确试用范围、期限与审批流程】</div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">MAP</div><h2>办公地点</h2></div>
    <div class="rv" style="background:#EEF4FA;border:1px solid #BEC3C8;border-radius:8px;height:300px;
      display:flex;align-items:center;justify-content:center;color:#5C6670;font-size:13.5px">
      【地图嵌入占位 · 建议懒加载或静态图 + 点击跳转，避免阻塞首屏】
    </div>
    <div class="note rv"><b>合规提示：</b>留言反馈与销售线索表单应分开设置，避免线索混淆；
      若支持文件上传，需限制格式（PDF/DOC/JPG）与大小（≤10MB）。</div>
  </div>
</section>
"""
w("contact.html", page("联系我们 | 天元平台",
  "联系天元平台团队：业务咨询、技术对接、生态合作。", "contact", ct))
print("联系页完成")
