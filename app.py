from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>黄老板的个人主页</title>
  <style>
    :root {
      --ink: #263238;
      --muted: #64748b;
      --primary: #5661e8;
      --soft: #f4f6fb;
      --card: #ffffff;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      color: var(--ink);
      background: #fff;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                   "PingFang SC", "Microsoft YaHei", sans-serif;
      line-height: 1.7;
    }

    a { color: inherit; text-decoration: none; }

    .nav {
      position: sticky;
      top: 0;
      z-index: 10;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px max(6vw, 20px);
      background: rgba(255,255,255,.92);
      border-bottom: 1px solid #edf0f5;
      backdrop-filter: blur(12px);
    }

    .brand { font-weight: 800; font-size: 1.15rem; }
    .nav-links { display: flex; gap: 22px; color: var(--muted); font-size: .95rem; }
    .nav-links a:hover { color: var(--primary); }

    .hero {
      min-height: 580px;
      display: grid;
      grid-template-columns: 1.2fr .8fr;
      align-items: center;
      gap: 40px;
      padding: 70px max(8vw, 24px);
      background: linear-gradient(135deg, #f3f5ff, #fff 60%, #eefaf7);
    }

    .eyebrow {
      display: inline-block;
      padding: 6px 12px;
      border-radius: 999px;
      background: #e8eaff;
      color: var(--primary);
      font-size: .9rem;
      font-weight: 700;
    }

    h1 { margin: 18px 0 12px; font-size: clamp(2.5rem, 6vw, 4.5rem); line-height: 1.15; }
    .hero p { max-width: 620px; color: var(--muted); font-size: 1.1rem; }

    .button {
      display: inline-block;
      margin-top: 16px;
      padding: 12px 20px;
      border-radius: 10px;
      background: var(--primary);
      color: white;
      font-weight: 700;
    }

    .hero-photo {
      width: min(100%, 360px);
      aspect-ratio: 1;
      justify-self: center;
      object-fit: cover;
      border-radius: 28px;
      box-shadow: 0 24px 60px #3843a733;
    }

    section { padding: 76px max(8vw, 24px); }
    section:nth-of-type(even) { background: var(--soft); }

    .section-heading { margin-bottom: 30px; }
    .section-heading h2 { margin: 0 0 8px; font-size: 2rem; }
    .section-heading p { margin: 0; color: var(--muted); }

    .about-grid, .video-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
      align-items: center;
    }

    .card {
      padding: 24px;
      border: 1px solid #edf0f5;
      border-radius: 18px;
      background: var(--card);
      box-shadow: 0 8px 28px #1725540a;
    }

    .tags { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }
    .tag { padding: 7px 12px; border-radius: 999px; background: #eef0ff; color: #4852c9; font-size: .9rem; }

    .gallery, .projects, .timeline {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .gallery img {
      width: 100%;
      height: 245px;
      object-fit: cover;
      border-radius: 16px;
      transition: transform .2s ease;
    }

    .gallery img:hover { transform: translateY(-4px); }

    .project-card h3 { margin-top: 0; }
    .project-card p { color: var(--muted); }

    .video-frame {
      width: 100%;
      border-radius: 16px;
      background: #111;
    }

    .timeline-item { border-left: 3px solid #c9ccff; }
    .timeline-item h3 { margin-top: 0; }
    .timeline-item .year { color: var(--primary); font-weight: 800; }

    .contact {
      text-align: center;
      background: #252b55 !important;
      color: white;
    }

    .contact p { color: #d7daf5; }
    .contact .button { background: white; color: #343c9c; }

    footer {
      padding: 22px;
      text-align: center;
      color: var(--muted);
      font-size: .9rem;
    }

    @media (max-width: 760px) {
      .nav { align-items: flex-start; gap: 12px; flex-direction: column; }
      .nav-links { flex-wrap: wrap; gap: 12px; }
      .hero, .about-grid, .video-grid { grid-template-columns: 1fr; }
      .hero { text-align: center; }
      .hero p { margin-left: auto; margin-right: auto; }
      .gallery, .projects, .timeline { grid-template-columns: 1fr; }
      section { padding-top: 56px; padding-bottom: 56px; }
    }
  </style>
</head>
<body>
  <nav class="nav">
    <a class="brand" href="#home">黄老板 · 个人主页</a>
    <div class="nav-links">
      <a href="#about">关于我</a>
      <a href="#gallery">照片</a>
      <a href="#video">视频</a>
      <a href="#projects">项目</a>
      <a href="#contact">联系</a>
    </div>
  </nav>

  <header class="hero" id="home">
    <div>
      <span class="eyebrow">你好，欢迎来到我的小站</span>
      <h1>你好，我是黄老板。</h1>
      <p>
        我是一名热爱购物、写作与探索新事物的创作者。
        我喜欢把灵感变成具体的作品，也喜欢用镜头记录生活里值得珍藏的瞬间。
        滕王高阁临江渚，佩玉鸣鸾罢歌舞。每个人的生活都值得被记录和分享，我希望这个小站能成为我与世界交流的窗口。
      </p>
      <a class="button" href="#about">了解更多</a>
    </div>
    <img class="hero-photo"
         src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=900&q=85"
         alt="个人头像">
  </header>

  <section id="about">
    <div class="section-heading">
      <h2>关于我</h2>
      <p>一些关于我的故事、兴趣和正在学习的事情。</p>
    </div>
    <div class="about-grid">
      <div class="card">
        <h3>把好奇心放进日常</h3>
        <p>
          我相信生活不只有目标和结果，也有沿途的观察与体验。
          平时我会阅读、拍照、做一些小项目，也会尝试不同的工具和想法。
          这个网页是我的个人空间，用来整理作品、记录成长，并分享喜欢的事物。
          人生自古谁无死，留取丹心照汗青。希望在这里留下我的一些思考和创作，也希望能与有趣的人交流。
          孤独、寂寞、无助时，记得还有这个小站在陪伴你。
        </p>
        <p>
          如果你也对创意、技术或旅行感兴趣，欢迎通过页面下方的联系方式和我交流。
        </p>
      </div>
      <div class="card">
        <h3>我喜欢做的事</h3>
        <p>不断尝试新事物，也持续打磨自己感兴趣的领域。</p>
        <div class="tags">
          <span class="tag">摄影</span>
          <span class="tag">网页设计</span>
          <span class="tag">阅读</span>
          <span class="tag">旅行</span>
          <span class="tag">写作</span>
          <span class="tag">咖啡</span>
        </div>
      </div>
    </div>
  </section>

  <section id="gallery">
    <div class="section-heading">
      <h2>照片墙</h2>
      <p>收藏一些旅行、自然和日常生活中的美好画面。</p>
    </div>
    <div class="gallery">
      <img src="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=85" alt="湖边山景">
      <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=85" alt="户外旅行风景">
      <img src="https://images.unsplash.com/photo-1490730141103-6cac27aaab94?auto=format&fit=crop&w=900&q=85" alt="日落风景">
      <img src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=900&q=85" alt="清晨的自然风景">
      <img src="https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85" alt="山野风景">
      <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=900&q=85" alt="森林小路">
    </div>
  </section>

  <section id="video">
    <div class="section-heading">
      <h2>视频日记</h2>
      <p>放一段喜欢的视频，也可以替换成自己的旅行或生活记录。</p>
    </div>
    <div class="video-grid">
      <video class="video-frame" controls poster="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1000&q=85">
        <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
        您的浏览器暂不支持 HTML 视频播放。
      </video>
      <div class="card">
        <h3>慢下来，看看身边</h3>
        <p>
          有时，一段短视频就能让人重新注意到平常忽略的细节。
          这里可以放旅行片段、作品介绍、生活记录，或一段简短的自我介绍。
        </p>
        <p>你可以将视频文件放在项目的 <code>static</code> 文件夹中，再修改上方的播放地址。</p>
      </div>
    </div>
  </section>

  <section id="projects">
    <div class="section-heading">
      <h2>我的小项目</h2>
      <p>这里可以展示作品、课程项目、兴趣尝试或正在进行的计划。</p>
    </div>
    <div class="projects">
      <article class="card project-card">
        <h3>个人摄影集</h3>
        <p>整理日常拍摄的照片，记录不同季节、城市和旅途中的光影。</p>
        <span class="tag">摄影 · 进行中</span>
      </article>
      <article class="card project-card">
        <h3>读书笔记</h3>
        <p>把读过的书和思考整理成简短笔记，方便回顾，也期待与人交流。</p>
        <span class="tag">阅读 · 持续更新</span>
      </article>
      <article class="card project-card">
        <h3>网页设计练习</h3>
        <p>尝试用简单、清晰的页面呈现内容，持续学习前端和用户体验设计。</p>
        <span class="tag">设计 · 学习中</span>
      </article>
    </div>
  </section>

  <section id="experience">
    <div class="section-heading">
      <h2>成长记录</h2>
      <p>用时间线记录重要的学习、工作或生活经历。</p>
    </div>
    <div class="timeline">
      <div class="card timeline-item">
        <span class="year">2024</span>
        <h3>开始记录作品</h3>
        <p>建立个人作品和灵感档案，给自己的想法一个可以持续生长的地方。</p>
      </div>
      <div class="card timeline-item">
        <span class="year">2025</span>
        <h3>尝试新的方向</h3>
        <p>学习新的工具，参与有趣的小项目，并把过程中的收获记录下来。</p>
      </div>
      <div class="card timeline-item">
        <span class="year">现在</span>
        <h3>继续探索</h3>
        <p>保持好奇，认真完成手头的事情，也为下一次新的尝试做好准备。</p>
      </div>
    </div>
  </section>

  <section class="contact" id="contact">
    <h2>和我打个招呼吧</h2>
    <p>如果你想交流、合作，或者只是想分享一个好点子，欢迎联系我。tele:18905620065</p>
    <a class="button" href="mailto:hello@example.com">发送邮件</a>
  </section>

  <footer>
    © 2026年11月16日 黄老板的个人主页 · 用 Flask 制作
  </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(debug=True)