import requests
from bs4 import BeautifulSoup


def get_all_categories_pages():

    urls = []
    page_number = 1

    for i in range(3):
        i = f"https://books.toscrape.com/catalogue/category/books/fantasy_19/page-{page_number}.html"
        page_number += 1
        urls.append(i)
    return urls


def get_books_from_categories(url):

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


def get_books_from_all_categories():

    all_books_url = []

    pages = get_all_categories_pages()
    for page in pages:
        get_books_from_categories(url=page)
        for book in get_books_from_categories(url=page):
            all_books_url.append(book)

    return all_books_url


print(get_books_from_all_categories())
