from urllib.request import urlopen

import mechanicalsoup

from bs4 import BeautifulSoup

page = urlopen("https://myads.africa")

code = page.read().decode("utf-8")

soup = BeautifulSoup(code, "html.parser")

browser = mechanicalsoup.Browser()

div = soup.select("div.ad-listing ")

n = 0

response = dict()

while(n < len(div)):
    response[n] = {'id':div[n].find_all("a", class_ = "save-ad")[0]['data-adid'], 
                   'category':div[n].select("div.category-title")[0].get_text(), 
                   'title':div[n].select("div.ad-listing h3")[0].get_text(),
                   'location':div[n].find_all("i", class_ = "fa-map-marker")[0].find_next("a").get_text(),
                   'price':div[n].select("div.price")[0].text,
                   'date':div[n].select("ul.ad-meta-info")[0].contents[1].get_text()
                }
    n+=1

print(response)