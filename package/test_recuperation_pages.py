import requests
from bs4 import BeautifulSoup


def scraping_pages():

    r = requests.get("https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html")
    soup = BeautifulSoup(r.content, "html.parser")

    link_page = []

    link = soup.find_all("a")
    print(link)
