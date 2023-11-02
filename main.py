from package import get_data_categories as cat, get_data_book_by_categories as page, get_data_book as book
import panda as pd

# resultat à obtenir :
# Dict{cat1 : [{book1}, {book2}, {book3}], cat2 : [{book4}, {book5}, {book6}], etc...}

if __name__ == "__main__":

    off_books = []
    off_pages = []
    off_cat = ["https://books.toscrape.com/catalogue/category/books/travel_2/", "https://books.toscrape.com/catalogue/category/books/mystery_3/"]
    list_dict_info_book = []

    for link in off_cat:
        page.get_books_from_all_categories(url_all_pages=link)
        off_pages.append(page.get_books_from_all_categories(url_all_pages=link))

        for books in page.get_books_from_all_categories(url_all_pages=link):
            book.get_data_book(url_book=books)
            off_books.append(book.get_data_book(url_book=books))

    dict_info_book = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), off_books)}
    list_dict_info_book.append(dict_info_book)
    dict_all = {cle: valeur for cle, valeur in zip(off_cat, list_dict_info_book)}

    df =

    print(dict_all)

'''
    all_page = []
    all_books = []

    all_cat = cat.categories_url(url_home="https://books.toscrape.com")

    for link in all_cat:
        page.get_books_from_all_categories(url_all_pages=link)

        for books in page.get_books_from_all_categories(url_all_pages=link):
            book.get_data_book(url_book=books)

            dict_info_book = {cle: valeur for cle, valeur in zip(page.get_books_from_all_categories(url_all_pages=link), book.get_data_book(url_book=books))}
            dict_all = {cle: valeur for cle, valeur in zip(cat.cat_list(url_home="https://books.toscrape.com"), dict_info_book)}

            chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/liste_book_url.csv"
            with open(chemin, "a") as c:
                c.write(str(dict_all))
'''
