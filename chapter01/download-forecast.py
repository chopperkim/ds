import urllib.parse
import urllib.request

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    "stnId": "108"
}

params = urllib.parse.urlencode(values)

url = API + "?" + params
print(f"url={url}")

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

