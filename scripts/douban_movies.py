import urllib.request
import xml.etree.ElementTree as ET
import re
import html
import json
import os

RSS_URL = "https://www.douban.com/feed/people/237707342/interests"
OUTPUT = "_data/films.json"

request = urllib.request.Request(
    RSS_URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("正在读取豆瓣 RSS...")

with urllib.request.urlopen(request, timeout=30) as response:
    data = response.read()

root = ET.fromstring(data)

films = []

for item in root.findall(".//item"):
    title = item.findtext("title", "")
    url = item.findtext("link", "")
    description = item.findtext("description", "")
    pub_date = item.findtext("pubDate", "")

    # 只处理电影
    if not url.startswith("https://movie.douban.com/subject/"):
        continue

    # 只处理「看过」
    if not title.startswith("看过"):
        continue

    movie_title = title.replace("看过", "", 1).strip()

    rating_match = re.search(
        r"推荐:\s*([^<]+)",
        description
    )
    rating = rating_match.group(1).strip() if rating_match else ""

    note_match = re.search(
        r"备注:\s*(.*?)(?:</p>|$)",
        description,
        re.S
    )
    note = html.unescape(
        note_match.group(1).strip()
    ) if note_match else ""

    poster_match = re.search(
        r'<img[^>]+src=["\']([^"\']+)["\']',
        description
    )
    poster = poster_match.group(1) if poster_match else ""

    films.append({
        "title": movie_title,
        "url": url,
        "poster": poster,
        "rating": rating,
        "note": note,
        "date": pub_date
    })

os.makedirs("_data", exist_ok=True)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(
        films,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"成功保存 {len(films)} 部电影")
