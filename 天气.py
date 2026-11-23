import requests
from bs4 import BeautifulSoup 
url="https://www.weather.com.cn/weather/101120801.shtml"
s=requests.Session()
s.strust_env=False
r=s.get(url,headers={"User-Agent": "Mozilla/5.0"},timeout=15)
r.encoding="utf-8"
print("状态码:",r.status_code,"长度",len(r.text))
soup=BeautifulSoup(r.text,"html.parser")
days=soup.find_all("li",class_="sky")
print("找到天数：",len(days))
lines=["===泰安未来七天天气==="]
for day in days[:3]:
    date=day.find("h1").get_text(strip=True)
    wea=day.find("p",class_="wea").get_text(strip=True)
    tem=day.find("p",class_="tem")
    high_tag=tem.find("span")
    high=high_tag.get_text(strip=True)if high_tag else "?"
    low_tag=tem.find("i")
    low=low_tag.get_text(strip=True)if low_tag else "?"
    win_1=day.find("p",class_="win")
    win_2=win_1.find("i")if win_1 else None
    win=win_2.get_text(strip=True)if win_2 else "?"
    line=f"{date} {wea} {high}/{low} {win}"
    print(line)
    lines.append(line)
with open("天气.txt","w",encoding="utf-8") as f:
    f.write("\n".join(lines))
print("已经保存 天气.txt")