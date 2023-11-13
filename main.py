from package import get_data_categories as cat, get_data_book_by_categories as page, get_data_book as book

# resultat à obtenir :
# Dict{cat1 : [{book1}, {book2}, {book3}], cat2 : [{book4}, {book5}, {book6}], etc...}

if __name__ == "__main__":

    all_books = []
    all_pages = []

    cat.categories_url(url_home="https://books.toscrape.com")

    for link in cat.categories_url(url_home="https://books.toscrape.com"):
        page.get_books_from_all_categories(url_all_pages=link)
        all_pages.append(page.get_books_from_all_categories(url_all_pages=link))

        for books in page.get_books_from_all_categories(url_all_pages=link):
            book.get_data_book(url_book=books)
            all_books.append(book.get_data_book(url_book=books))

    # dict_book = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), all_books)}
    # final_dict_book = {cle: valeur for cle, valeur in zip(cat.categories_url(url_home="https://books.toscrape.com"), dict_book)}

    test_dict = {cle: valeur for cle, valeur in zip(cat.categories_url(url_home="https://books.toscrape.com"), all_pages)}
    test_dict_2 = {cle: valeur for cle, valeur in zip(cat.categories_url(url_home="https://books.toscrape.com"), {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), all_books)})}

    chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/liste_book_url.csv"
    with open(chemin, "a") as c:
        c.write(str(test_dict_2))

"""
    pages_to_scrap = ["https://books.toscrape.com/catalogue/category/books/travel_2/", "https://books.toscrape.com/catalogue/category/books/fantasy_19/"]
    all_cat = []
    all_pages = []

    # cat.categories_url(url_home="https://books.toscrape.com")
    # for link in cat.categories_url(url_home="https://books.toscrape.com"):
    # for link in pages_to_scrap:
        page.get_books_from_all_categories(url_all_pages=link)
        # all_pages.append(page.get_books_from_all_categories(url_all_pages=link))

        for books in page.get_books_from_all_categories(url_all_pages=link):
            book.get_data_book(url_book=books)
            all_books.append(book.get_data_book(url_book=books))

    dict_book = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), all_books)}
    dict_book_2 = book.get_data_book(url_book=pages_to_scrap)
    # list_dict_book.append(dict_book)
    # dict_all = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), lis)}
    
    chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/liste_book_url.xlsx"
    with open(chemin, "a") as c:
        c.write(str(dict_book_2))
"""