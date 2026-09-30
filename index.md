---
layout: default
---

<div class="home-intro">

<h1>norrie</h1>

<p class="subtitle">
notes · films · photos
</p>

<p class="description">
一些关于生活、电影、摄影和世界的记录。<br>
Notes from somewhere on the internet.
</p>

</div>

<hr>

<h2>Notes</h2>

<div class="post-list-custom">

{% for post in site.posts %}

<article class="post-item">

<div class="post-date">
{{ post.date | date: "%Y.%m.%d" }}
</div>

<div class="post-content">

<h3>
<a href="{{ post.url | relative_url }}">{{ post.title }}</a>
</h3>

<p>
{{ post.excerpt }}
</p>

</div>

</article>

{% endfor %}

</div>
