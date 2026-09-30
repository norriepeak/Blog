---
layout: page
title: Films
permalink: /films/
---

我看过的电影，以及留在豆瓣上的一些记录。

<div class="film-list">
<p>TEST123</p>

<p>数量：{{ site.data.films.size }}</p>

{% for film in site.data.films %}

<div class="film-card">

  <div class="film-poster">
    {% if film.poster %}
    <img src="{{ film.poster }}" alt="{{ film.title }}">
    {% endif %}
  </div>


  <div class="film-info">

    <h2>
      《{{ film.title }}》
    </h2>


    {% if film.rating %}
    <p class="film-rating">
      ⭐⭐⭐⭐⭐
      <br>
      星级：{{ film.rating }}
    </p>
    {% endif %}


    {% if film.note %}
    <p class="film-note">
      <strong>短评：</strong><br>
      {{ film.note }}
    </p>
    {% endif %}


    <p>
      <a href="{{ film.url }}" target="_blank">
        豆瓣页面 →
      </a>
    </p>

  </div>

</div>

{% endfor %}

</div>
