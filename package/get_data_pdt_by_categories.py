import requests
from bs4 import BeautifulSoup


def get_all_categories_pages():

    urls = []
    page_number = 1

    for i in range(3):
        i = f"http://books.toscrape.com/catalogue/category/books/fantasy_19/page-{page_number}.html"
        page_number += 1
        urls.append(i)
    return urls


def get_books_from_categories():

    r = requests.get("http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html")
    soup = BeautifulSoup(r.content, "html.parser")

    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for link in books:
        books_link = link.find_all_next("a")
        return books_link


def get_books_from_all_page_by_categories():

    pages = get_all_categories_pages()
    for page in pages:
        get_books_from_categories(url=pages)
        return page


print(get_books_from_categories())
