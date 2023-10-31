from package import get_data_categories as cat, get_data_book_by_categories as page, get_data_book as book

# resultat à obtenir :
# Dict{cat1 : [{book1}, {book2}, {book3}], cat2 : [{book4}, {book5}, {book6}], etc...}

if __name__ == "__main__":

    # print(cat.dictionary_cat(url="https://books.toscrape.com"))
    # print(page.dictionary_books(url_cat="https://books.toscrape.com/catalogue/category/books/fantasy_19/"))
    # print(book.get_data_book())

    all_urls = []
    all_urls_page_1 = []
    all_book = []

    all_cat = cat.categories_url(url_home="https://books.toscrape.com")
    for categories in all_cat:
        page.scrap_page_number(url_cat=categories)
        all_urls.append(page.scrap_page_number(url_cat=categories))

    # print(all_urls)

    for urls in all_urls:
        page.get_books_from_categories(url_page_1=urls)
        all_urls_page_1.append(page.get_books_from_categories(url_page_1=urls))

    print(all_urls_page_1)

"""
    for link in all_urls_page_1:
        page.get_books_from_all_categories(url_all_pages=link)
        all_book.append(page.get_books_from_all_categories(url_all_pages=link))
"""

    # print(all_book)
