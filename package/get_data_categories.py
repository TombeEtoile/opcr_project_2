import requests
from bs4 import BeautifulSoup


def get_data_categories_fct():

    r = requests.get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(r.content, "html.parser")
    categories_link = []
    categories_name = []

    navbar = soup.find("ul", class_="nav nav-list")
    categories_list = navbar.find_all("a", href_="")

    print(categories_list)


get_data_categories_fct()
