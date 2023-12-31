import sys
import urllib.parse as parse
import urllib.request as req

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
region_number = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    "stnId": region_number
}

params = parse.urlencode(values)
url = API + "?" + params
print(f"url={url}")

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
