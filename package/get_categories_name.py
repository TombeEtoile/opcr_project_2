import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup


def categories_name():

    r = requests.get("https://books.toscrape.com")
    soup = BeautifulSoup(r.content, "html.parser")

    cat_list = []

    nav_bar = soup.find("ul", class_="nav nav-list").text.lstrip().strip()
    all_cat = nav_bar.replace("\n", "")
    cat_list.append(all_cat)

    return cat_list


print(categories_name())
