from urllib.request import urlopen

from bs4 import BeautifulSoup

page = urlopen("https://myads.africa")

file = open("source_code.txt","w+")

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")


file.write(soup.prettify())

file.close()