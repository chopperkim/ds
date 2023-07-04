import sys, re, time, os
import urllib.request as req
import urllib.parse as parse
import json

PHOTOZOU_API = "https://api.photozou.jp/rest/search_public.json"
CACHE_DIR = "images/cache_gyudon"


def search_photo(keyword, offset=0, limit=100):
    # API 쿼리 조합하기
    keyword_enc = parse.quote_plus(keyword)
    query = f"keyword={parse.quote(keyword)}&offset={offset}&limit={limit}"
    url = f"{PHOTOZOU_API}?{query}"

    # 캐시 전용 폴더 만들기
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    cache = CACHE_DIR + "/" + re.sub(r'[^a-zA-Z0-9\%\#]+', '_', url)
    if os.path.exists(cache):
        return json.load(open(cache, "r", encoding="utf-8"))
    print(f"[API] {url}")
    req.urlretrieve(url, cache)
    time.sleep(1)
    return json.load(open(cache, "r", encoding="utf-8"))


# 이미지 다운로드 하기
def download_thumb(info, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    if info is None:
        return
    if not "photo" in info["info"]:
        print("[ERROR] broken info")
        return
    photolist = info["info"]["photo"]
    for photo in photolist:
        title = photo["photo_title"]
        photo_id = photo["photo_id"]
        url = photo["thumbnail_image_url"]
        path = save_dir + "/" + str(photo_id) + "_thumb.jpg"
        if os.path.exists(path):
            continue
        try:
            print(f"[download]{title}{photo_id}")
            req.urlretrieve(url, path)
            time.sleep(1)
        except Exception as e:
            print(f"[ERROR] failed to download url={url}")


# 모두 검색하고 다운르도 하기
def download_all(keyword, save_dir, maxphoto = 1000):
    offset = 0
    limit = 100
    while True:
        # API 호출
        info = search_photo(keyword, offset=offset, limit=limit)
        if info is None:
            print("[ERROR] no result")
            return
        if (not "info" in info) or (not "photo_num" in info["info"]):
            print("[ERROR] broken data")
            return
        photo_num = info["info"]["photo_num"]
        if photo_num == 0:
            print(f"photo_num = 0, offset={offset}")
            return
        # 사진 정보가 포함되어 있으면 다운로드 받기
        print(f"*** download offset={offset}")
        download_thumb(info, save_dir)
        offset += limit
        if offset >= maxphoto:
            break

if __name__ == '__main__':
    # 모듈로 사용할 수 있게 설정
    download_all("牛丼", "images/gyudon")