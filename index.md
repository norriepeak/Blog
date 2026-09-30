---
layout: default
---

<div class="home-intro">

<h1>Norrie Peak</h1>

<p class="subtitle">
notes · films · photos · life
</p>

<p class="description">
一些关于生活、电影、摄影和世界的记录。<br>
Notes from somewhere on the internet.
</p>

</div>

<div class="post-list-custom">

{% for post in site.posts %}

<article class="post-item">

<div class="post-date">
{{ post.date | date: "%Y.%m.%d" }}
</div>

<div class="post-content">

<h2>
<a href="{{ post.url | relative_url }}">{{ post.title }}</a>
</h2>

</div>

</article>

{% endfor %}

</div>
