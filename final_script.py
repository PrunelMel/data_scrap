from urllib.request import urlopen

import mechanicalsoup, sqlite3

from bs4 import BeautifulSoup

page = urlopen("https://myads.africa")

code = page.read().decode("utf-8")

soup = BeautifulSoup(code, "html.parser")

browser = mechanicalsoup.Browser()

div = soup.select("div.ad-listing ")

def db_con ():
    try:
        connection = sqlite3.connect("product.sqlite3")
        connection.cursor().execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id VARCHAR(15), category VARCHAR(50), title VARCHAR(500), location VARCHAR(500), price VARCHAR(50), date VARCHAR(50));")

        return connection
    
    except Exception as e :

        return e

productId = db_con().cursor().execute("SELECT product_id FROM products").fetchall()

pdId = [i[0] for i in productId]

if productId is Exception:
    print("Database Error")

else:

    n = 0

    response = dict()

    while(n < len(div)):

        p_id = div[n].find_all("a", class_ = "save-ad")[0]['data-adid']

        if p_id in pdId :
            
            print("Exist")

            n+=1
            
            continue

        else:

            con = db_con()
            
            id = div[n].find_all("a", class_ = "save-ad")[0]['data-adid']

            category = div[n].select("div.category-title")[0].get_text()

            title = div[n].select("div.ad-listing h3")[0].get_text()

            loc = div[n].find_all("i", class_ = "fa-map-marker")[0].find_next("a").get_text()

            price = div[n].select("div.price")[0].text

            date = div[n].select("ul.ad-meta-info")[0].contents[1].get_text()

            con.cursor().execute(f"INSERT INTO products (product_id,category,title,location,price,date) VALUES (?,?,?,?,?,?)", (id, category, title, loc, price, date))

            con.commit()

            print("Update Made")

        n+=1

    print("Success")
print(pdId)

"""data = [i.contents[1].get_text(":").split(":") for i in div]

category = [i.get_text() for i in cat]

title = [i.get_text() for i in ttl]

priceList = [i.text for i in pr]

dateList = [i.contents[1].get_text() for i in dt]

loc = [i.find_all("i", class_ = "fa-map-marker")[0].find_next("a").get_text() for i in div]

pr = soup.select("div.price" )

dt = soup.select("ul.ad-meta-info")

cat = soup.select("div.category-title")

ttl = soup.select("div.ad-listing h3")

response[n] = {'id':div[n].find_all("a", class_ = "save-ad")[0]['data-adid'],
                       
            'category':div[n].select("div.category-title")[0].get_text(),

            'title':div[n].select("div.ad-listing h3")[0].get_text(),

            'location':div[n].find_all("i", class_ = "fa-map-marker")[0].find_next("a").get_text(),

            'price':div[n].select("div.price")[0].text,

            'date':div[n].select("ul.ad-meta-info")[0].contents[1].get_text()
        }
        """