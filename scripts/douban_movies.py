import urllib.request
import xml.etree.ElementTree as ET
import re
import html

RSS_URL = "https://www.douban.com/feed/people/237707342/interests"

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

print("\n找到的电影：\n")

count = 0

for item in root.findall(".//item"):
    title = item.findtext("title", "")
    url = item.findtext("link", "")
    description = item.findtext("description", "")

    # 只处理豆瓣电影
    if not url.startswith("https://movie.douban.com/subject/"):
        continue

    # 只处理「看过」
    if not title.startswith("看过"):
        continue

    movie_title = title.replace("看过", "", 1).strip()

    # 提取推荐等级
    rating_match = re.search(r"推荐:\s*([^<]+)", description)
    rating = rating_match.group(1).strip() if rating_match else ""

    # 提取备注
    note_match = re.search(r"备注:\s*(.*?)(?:</p>|$)", description, re.S)
    note = html.unescape(note_match.group(1)).strip() if note_match else ""

    # 提取海报
    poster_match = re.search(
        r'<img[^>]+src=["\']([^"\']+)["\']',
        description
    )
    poster = poster_match.group(1) if poster_match else ""

    print(f"电影：{movie_title}")
    print(f"推荐：{rating}")
    print(f"短评：{note}")
    print(f"海报：{poster}")
    print(f"豆瓣：{url}")
    print("-" * 50)

    count += 1

print(f"\n共找到 {count} 部「看过」电影。")
