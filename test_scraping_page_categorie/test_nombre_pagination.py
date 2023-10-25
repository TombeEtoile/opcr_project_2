import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com/catalogue/category/books/fantasy_19/page-1.html")
soup = BeautifulSoup(r.content, "html.parser")

page_number = soup.find("li", {"class": "current"}).text.strip().split()
max_page_str = page_number[3]
max_page = int(max_page_str)
html = ".html"


def scrap_pages():

    urls = []
    min_page = 1

    for i in range(max_page):
        i = f"https://books.toscrape.com/catalogue/category/books/fantasy_19/page-{min_page}{html}"
        min_page += 1
        urls.append(i)

    return urls


print(scrap_pages())
