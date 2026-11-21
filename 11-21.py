"""import requests

url = "https://www.weather.com.cn/weather/101010100.shtml"

for i in range(3):
    print(f"第 {i+1} 次尝试...")
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        print("状态码:", r.status_code)
        print("长度:", len(r.text))
        with open("weather.html", "w", encoding="utf-8") as f:
            f.write(r.text)
        print("已保存 weather.html")
        break
    except Exception as e:
        print("失败:", type(e).__name__)
        print("原因:", str(e)[:120])"""

"""import requests
r=requests.get("https://www.weather.com.cn/weather/101010100.shtml",
               headers={"User-Agent":"Mozilla/5.0"},
               timeout=15)
print(r.status_code,len(r.text))
with open("weather.html","w",encoding="utf-8")as f:
    f.write(r.text)
print("已经保存weather.html")"""

"""import  requests
url="https://www.weather.com.cn/weather/101010100.shtml"
for i in range(3):
    print(f"第{i+1}次尝试...")
    try:
        r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"},timeout=15)
        print("状态码:",r.status_code)
        print("长度:",len(r.text))
        with open("weather.html","w",encoding="utf-8")as f:
            f.write(r.text)
        print("已经保存weather.html")
        break
    except Exception as e:
        print("失败：",type(e).__name__)
        print("原因：",str(e)[:120])"""

"""from bs4 import BeautifulSoup
with open("weather.html","r",encoding="utf-8")as f:
    html=f.read()
soup=BeautifulSoup(html,"html.parser")
days=soup.find_all("li",class_="sky")
print("找到天数：",len(days))
lines=["===北京未来7天天气==="]
for day in days:
    date=day.find("h1").get_text(strip=True)
    wea=day.find("p",class_="wea").get_text(strip=True)
    tem=day.find("p",class_="tem")
    high=tem.find("span").get_text(strip=True)
    low=tem.find("i").get_text(strip=True)
    line=(f"{date}  {wea}  {high}/{low}")
    print(line)
    lines.append(line)
text="\n".join(lines)
import requests
url = "https://www.weather.com.cn/weather/101010100.shtml"
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
r.encoding = "utf-8"  
print("状态码:", r.status_code, "长度:", len(r.text))
with open("天气.txt","w",encoding="utf-8")as f:
    f.write(text) 

print("已经保存 天气.txt")   """

import requests
from bs4 import BeautifulSoup
url="https://www.weather.com.cn/weather/101120801.shtml"
r=requests.get(url,headers={"User-Agent": "Mozilla/5.0"},timeout=15)
r.encoding="utf-8"  
print("状态码：",r.status_code,"长度:",len(r.text))
soup=BeautifulSoup(r.text,"html.parser")
print(soup.title.get_text(strip=True))
days=soup.find_all("li",class_="sky")
print("找到的天数：",len(days))
lines=["===泰安未来7天天气=="]
for day in days:
    date=day.find("h1").get_text(strip=True)
    wea=day.find("p",class_="wea").get_text(strip=True)
    tem=day.find("p",class_="tem")
    high_tag=tem.find("span")
    low_tag=tem.find("i")
    low=low_tag.get_text(strip=True) if low_tag else "?"
    if high_tag:
        line=f"{date}   {wea}   {high_tag.get_text(strip=True)}/{low}"
    else:
        line=f"{date}   {wea}   最高暂无/{low}"
    print(line)
    lines.append(line)
with open("天气.txt","w",encoding="utf-8")as f:
    f.write("\n".join(lines))
print("已经保存 天气.txt")