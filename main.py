from package import get_data_categories as cat, get_data_book_by_categories as page, get_data_book as book

# resultat à obtenir :
# Dict{cat1 : [{book1}, {book2}, {book3}], cat2 : [{book4}, {book5}, {book6}], etc...}

if __name__ == "__main__":

    # user_request = [input("Quelle catégorie veux-tu scraper (penses à enlever le '/index.html') ? ")]
    # user_request.append(input("Quelle page veux-tu scraper ? "))
    pages_to_scrap = ["https://books.toscrape.com/catalogue/category/books/travel_2/", "https://books.toscrape.com/catalogue/category/books/fantasy_19/"]
    all_pages = []
    all_books = []
    list_dict_book = []

    # cat.categories_url(url_home="https://books.toscrape.com")
    # for link in cat.categories_url(url_home="https://books.toscrape.com"):
    for link in pages_to_scrap:
        page.get_books_from_all_categories(url_all_pages=link)
        # all_pages.append(page.get_books_from_all_categories(url_all_pages=link))

        for books in page.get_books_from_all_categories(url_all_pages=link):
            book.get_data_book(url_book=books)
            all_books.append(book.get_data_book(url_book=books))

    dict_book = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), all_books)}
    # list_dict_book.append(dict_book)
    # dict_all = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), lis)}

    print(dict_book)

    # chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/liste_book_url.csv"
    # with open(chemin, "a") as c:
        # c.write(str(dict_all))

"""
    off_books = []
    off_pages = []
    off_cat_input = input("Quelle catégorie voulez_vous scraper ? ")
    off_cat = [off_cat_input]

    for link in off_cat:
        page.get_books_from_all_categories(url_all_pages=link)
        # off_pages.append(page.get_books_from_all_categories(url_all_pages=link))

        for books in page.get_books_from_all_categories(url_all_pages=link):
            book.get_data_book(url_book=books)
            off_books.append(book.get_data_book(url_book=books))

    # dict_info_book = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), off_books)}
    # dict_info_book = {cle: valeur for cle, valeur in zip(off_book_name, off_books)}
    # list_dict_info_book.append(dict_info_book)
    dict_all = {cle: valeur for cle, valeur in zip(off_cat, off_books)}

    print(dict_all)
"""
