import requests
from bs4 import BeautifulSoup

cat_url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/"

r = requests.get(cat_url)
soup = BeautifulSoup(r.content, "html.parser")

next_button = soup.find("li", {"class": "next"})
# <li class="next"><a href="page-2.html">next</a></li>

all_url = []
number = []


def scrap_page():
    # scraper url page 2

    for href in next_button:
        link_page = href.attrs["href"]
        next_page = cat_url + link_page

        return next_page


page_number = soup.find("li", {"class": "current"}).text.strip().split()


def scrap_all_url():

    for link in all_url:
        url = link.url(all_url)

    scrap_page()


print(page_number[3])

"""
for href in next_page:
    link_page = href.attrs["href"]
    link_list.append(url + link_page)
"""