from bs4 import BeautifulSoup
try:
    with open("daidu.html" , "r" , encoding="utf-8")as f:
        html_content=f.read()
except FileNotFoundError:
    exit()
soup=BeautifulSoup(html_content,"html.parser")
links=soup.find_all("a")
for link in links:
    href=link.get("href")
    if href:
        print(href)