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


def get_books_from_categories(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for book in books:
        books_link = book.find("a", href_="")

    chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/liste_livres.txt"
    with open(chemin, "a",) as f:
        f.write(f"{books_link}")


"""
def get_books_from_all_page_by_categories():
    pages = get_all_categories_pages()
    for page in pages:
        get_books_from_categories(url=page)
        print(f"on scrap + {page}")
"""