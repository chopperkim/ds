import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
save_name = "test1.png"

urllib.request.urlretrieve(url, save_name)
print("저장되었습니다.")
