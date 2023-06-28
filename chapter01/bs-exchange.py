import requests as requests
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
html = res.read()

soup = BeautifulSoup(html, "html.parser")

data_list = soup.select("#exchangeList > li")
for data in data_list:
    title = data.select_one(".h_lst > span").string
    value = data.select_one(".head_info > .value").string
    print(f"{title}/KRW = {value}")
