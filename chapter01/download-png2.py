import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
save_name = "test2.png"

mem = urllib.request.urlopen(url).read()

with open(save_name, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다.")