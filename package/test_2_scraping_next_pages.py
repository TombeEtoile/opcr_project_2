import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com/catalogue/category/books/fantasy_19/")
soup = BeautifulSoup(r.content, "html.parser")


def scrap_page():
    # scraper url page 2

    url = r.url
    link_list = []
    all_next_pages = []

    next_page = soup.find("li", {"class": "next"})

    for href in next_page:
        link_page = href.attrs["href"]
        link_list.append(url + link_page)

    return link_list


def scrap_all_pages():

    next_page = scrap_page()
    all_next_pages = []

    for next_page in scrap_page():
        scrap_page(next_page)

scrap_all_pages()
