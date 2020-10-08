import requests as req
from bs4 import BeautifulSoup as bs
from webbrowser import open as op # varsayılan tarayıcıdan linkleri açmak için

aranacak = input("Stack overflow da aramak istediğiniz: ")
sonuc_miktari = input("Kaç sonuç istersiniz: ")

url = f"https://stackoverflow.com/search?q={aranacak} isaccepted:yes"
r = req.get(url,headers={"key":"AUhTWzNQcZkCA2Qnff5hbQ(("})

a = 0
for i in bs(r.text,"html.parser").find_all("a",{"class":"question-hyperlink"}):
    if i.get("href").startswith("/questions"):
        op("https://stackoverflow.com" + str(i.get("href")))
        a += 1
        if a == int(sonuc_miktari): break
    else:
        print("Sonuç bulunamadı")
        break
