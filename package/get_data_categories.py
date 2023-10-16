import requests
from bs4 import BeautifulSoup


def get_data_categories_fct():

    r = requests.get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(r.content, "html.parser")

    categories = []

    navbar = soup.find("div", class_="side_categories")
    urls = navbar.find_all("a")
    for link in urls:
        href = link['href']

        return href


print(get_data_categories_fct())
