import requests
from bs4 import BeautifulSoup

url_home = "https://books.toscrape.com/catalogue/category/books/nonfiction_13"


def scrap_page_number(url):
    # scrap le nombre de page d'une catégorie

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    page_number = soup.find("li", {"class": "current"}).text.strip().split()
    max_page_str = page_number[3]
    max_page = int(max_page_str)

    return max_page


def url_adaptation(url):

    html = ".html"
    page = "page-"

    urls = []
    min_page = 1

    for i in range(scrap_page_number(url)):
        i = f"{url}{page}{min_page}{html}"
        min_page += 1
        urls.append(i)

    return urls


def get_books_from_categories(url):
    # scraper tous les livres de la page 1 d'une catégorie

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    all_links = []
    all_books_link = []
    all_valid_url = []

    books_container = soup.find_all("div", class_="image_container")

    for a in books_container:
        book_link = a.find("a")
        all_links.append(book_link)

    for link in all_links:
        href = link.attrs['href']
        all_books_link.append(href)

    for change in all_books_link:
        valid_url = change.replace("../../..", "https://books.toscrape.com/catalogue")
        all_valid_url.append(valid_url)

    return all_valid_url


def get_books_from_all_categories(url):
    # appel la fonction 2 et 3 pour scraper tous les livres de toutes les pages "next"

    all_books_url = []

    pages = scrap_page_number(url)
    for page in url_adaptation(url):
        get_books_from_categories(url=page)
        for book in get_books_from_categories(url=page):
            all_books_url.append(book)

    return all_books_url


print(get_books_from_all_categories())
