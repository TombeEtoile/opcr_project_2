import requests
from bs4 import BeautifulSoup


def get_data_categories_fct():

    r = requests.get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(r.content, "html.parser")

    navbar = soup.find("ul", class_="nav nav-list")
    for genre in navbar:
        categories_link = genre.find_all("li")
        for nom in categories_link:
            categories_name = nom.find_all("#text")
        print(categories_link)
"""
    for genre in categories_list:
        categories_link.append("li")

        print(categories_link)
"""

