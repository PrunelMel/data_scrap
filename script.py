from urllib.request import urlopen

import mechanicalsoup

from bs4 import BeautifulSoup

page = urlopen("https://myads.africa")

code = page.read().decode("utf-8")

soup = BeautifulSoup(code, "html.parser")

browser = mechanicalsoup.Browser()


#files opening
file = open("div.txt", "w+")

#file2 = open("div2.txt", "w+")

price = open("price.txt", "w+")

date = open("date.txt", "w+")

category = open("category.txt", "w+")

title = open("title.txt", "w+")

location = open("location.txt", "w+")

idfile = open("id.txt", "w+")

#html parsing
div = soup.select("div.ad-listing ")

pr = soup.select("div.price" )

dt = soup.select("ul.ad-meta-info")

cat = soup.select("div.category-title")

ttl = soup.select("div.ad-listing h3")

id = [i.find_all("a", class_ = "save-ad")[0]['data-adid'] for i in div]

loc = [i.find_all("i", class_ = "fa-map-marker")[0].find_next("a").get_text() for i in div]


#loc = soup.select("a[href=javascript:void(0);]")

#file.write(str(soup.find_all("div")))

file.write(str(div))

#file2.write(str([i.contents[1].get_text(":").split(":") for i in div]))

price.write(str([i.text for i in pr]))

date.write(str([i.contents[1].get_text() for i in dt]))

category.write(str([i.get_text() for i in cat]))

title.write(str([i.get_text() for i in ttl]))

idfile.write(str(id))

location.write(str(loc))

#file2.close()

file.close()

price.close()

date.close()

category.close()

title.close()

idfile.close()

location.close()

"""l = div[0].contents[0].contents

for el in l:
    print(el.name)"""