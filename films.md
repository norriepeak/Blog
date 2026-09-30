---
layout: page
title: Films
permalink: /films/
---

我看过的电影，以及留在豆瓣上的一些记录。

电影数据数量：{{ site.data.films.size }}

{% if site.data.films %}
{% for film in site.data.films %}

<div class="film-entry">

  {% if film.poster %}
  <img src="{{ film.poster }}" alt="{{ film.title }}">
  {% endif %}

  <div class="film-info">

    <h2>
      <a href="{{ film.url }}" target="_blank">
        {{ film.title }}
      </a>
    </h2>

    {% if film.rating %}
    <p>{{ film.rating }}</p>
    {% endif %}

    {% if film.note %}
    <p>{{ film.note }}</p>
    {% endif %}

  </div>

</div>

{% endfor %}
{% else %}

还没有电影记录。

{% endif %}
