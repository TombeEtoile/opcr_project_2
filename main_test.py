import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(r.content, "html.parser")

cat_list = []

nav_bar = soup.find("div", class_="side_categories")
all_cat = nav_bar.find_all("a")
for cat_name in all_cat:
    all_cat_name = cat_name.text.strip()
    cat_list.append(all_cat_name)

del(cat_list[0])

print(cat_list)
