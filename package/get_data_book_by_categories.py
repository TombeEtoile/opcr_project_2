import requests
from bs4 import BeautifulSoup


def scrap_page_number(url_all_pages):
    # scrap le nombre de page d'une catégorie

    r = requests.get(url_all_pages)
    soup = BeautifulSoup(r.content, "html.parser")

    urls = []

    try:
        page_number = soup.find("li", {"class": "current"}).text.strip().split()

        html = ".html"
        page = "page-"
        max_page_str = page_number[3]
        max_page = int(max_page_str)
        min_page = 1

        for i in range(max_page):
            i = f"{url_all_pages}{page}{min_page}{html}"
            min_page += 1

            urls.append(i)

    except AttributeError:
        index_html = "index.html"
        i = f"{url_all_pages}{index_html}"

        urls.append(i)

    return urls


def get_books_from_categories(url_all_pages):
    # scraper tous les livres de la page 1 d'une catégorie

    r = requests.get(url_all_pages)
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


def get_books_from_all_categories(url_all_pages):
    # appel la fonction 2 et 3 pour scraper tous les livres de toutes les pages "next"

    all_books_url = []

    pages = scrap_page_number(url_all_pages)
    for page in pages:
        get_books_from_categories(url_all_pages=page)
        for book in get_books_from_categories(url_all_pages=page):
            all_books_url.append(book)

    return all_books_url


# fausse_liste = ['https://books.toscrape.com/catalogue/category/books/travel_2/', 'https://books.toscrape.com/catalogue/category/books/mystery_3/', 'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/']

# print(scrap_page_number(url_all_pages="https://books.toscrape.com/catalogue/category/books/travel_2/"))
# print(get_books_from_categories(url_all_pages="https://books.toscrape.com/catalogue/category/books/fantasy_19/"))
# print(get_books_from_all_categories(url_all_pages="https://books.toscrape.com/catalogue/category/books/fantasy_19/"))


def dictionary_books(url_all_pages):

    list_books_name = []

    for books in get_books_from_all_categories(url_all_pages):
        url_split_1 = books.replace("https://books.toscrape.com/catalogue/", "")
        url_split_2 = url_split_1.replace("/index.html", "")
        list_books_name.append(url_split_2)

    dict_books = {cle: valeur for cle, valeur in zip(list_books_name, get_books_from_all_categories(url_all_pages))}

    return dict_books


def book_name(url_all_pages):

    list_books_name2 = []

    for books in get_books_from_all_categories(url_all_pages):
        url_split_1 = books.replace("https://books.toscrape.com/catalogue/", "")
        url_split_2 = url_split_1.replace("/index.html", "")
        url_split_3 = url_split_2.replace("-", " ")
        list_books_name2.append(url_split_3)

    return list_books_name2


# print(dictionary_books(url_all_pages="https://books.toscrape.com/catalogue/category/books/fantasy_19/"))
# print(book_name(url_all_pages="https://books.toscrape.com/catalogue/category/books/fantasy_19/"))
