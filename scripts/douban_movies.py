import urllib.request
import xml.etree.ElementTree as ET
import re
import html
import json
import os
import hashlib

RSS_URL = "https://www.douban.com/feed/people/237707342/interests"

OUTPUT = "_data/films.json"
IMAGE_DIR = "assets/images/films"


def download_image(url, movie_url):
    """下载电影海报并保存到本地"""

    if not url:
        return ""

    os.makedirs(IMAGE_DIR, exist_ok=True)

    # 用豆瓣电影 ID 作为文件名
    movie_id_match = re.search(r"/subject/(\d+)", movie_url)

    if movie_id_match:
        filename = movie_id_match.group(1) + ".jpg"
    else:
        filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"

    filepath = os.path.join(IMAGE_DIR, filename)

    # 已经下载过就不重复下载
    if os.path.exists(filepath):
        print(f"海报已存在：{filename}")
        return f"/Blog/assets/images/films/{filename}"

    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://movie.douban.com/"
            }
        )

        with urllib.request.urlopen(request, timeout=30) as response:
            image_data = response.read()

        with open(filepath, "wb") as f:
            f.write(image_data)

        print(f"海报下载成功：{filename}")

        return f"/Blog/assets/images/films/{filename}"

    except Exception as e:
        print(f"海报下载失败：{url}")
        print(f"原因：{e}")
        return ""


print("正在读取豆瓣 RSS...")

request = urllib.request.Request(
    RSS_URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

with urllib.request.urlopen(request, timeout=30) as response:
    data = response.read()

root = ET.fromstring(data)

films = []

for item in root.findall(".//item"):

    title = item.findtext("title", "")
    url = item.findtext("link", "")
    description = item.findtext("description", "")
    pub_date = item.findtext("pubDate", "")

    # 只处理豆瓣电影
    if not url.startswith("https://movie.douban.com/subject/"):
        continue

    # 只处理「看过」
    if not title.startswith("看过"):
        continue

    movie_title = title.replace("看过", "", 1).strip()

    # 推荐等级
    rating_match = re.search(
        r"推荐:\s*([^<]+)",
        description
    )

    rating = (
        rating_match.group(1).strip()
        if rating_match
        else ""
    )

    # 短评
    note_match = re.search(
        r"备注:\s*(.*?)(?:</p>|$)",
        description,
        re.S
    )

    note = ""

    if note_match:
        note = html.unescape(
            note_match.group(1)
        ).strip()

    # 豆瓣海报地址
    poster_match = re.search(
        r'<img[^>]+src=["\']([^"\']+)["\']',
        description
    )

    poster_url = (
        poster_match.group(1)
        if poster_match
        else ""
    )

    # 下载到自己的 GitHub
    poster = download_image(
        poster_url,
        url
    )

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

print()
print(f"成功同步 {len(films)} 部电影")
print("海报目录：", IMAGE_DIR)
