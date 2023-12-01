from package import get_data_categories as cat, get_data_book_by_categories as page, get_data_book as book
import csv
import os
from operator import itemgetter

# resultat à obtenir :
# [{book1}, {book2}, {book3}], {book4}, {book5}, {book6}], etc...}]

if __name__ == "__main__":

    all_info = []
    all_pages = []
    dict_all_info = {}

    # fausse_liste = ["https://books.toscrape.com/catalogue/category/books/travel_2/", "https://books.toscrape.com/catalogue/category/books/fantasy_19/"]
    cat.categories_url(url_home="https://books.toscrape.com/")

    for link in cat.categories_url(url_home="https://books.toscrape.com/"):
        page.dictionary_books(url_all_pages=link)
        all_pages.append(page.dictionary_books(url_all_pages=link))

        for books in page.dictionary_books(url_all_pages=link).values():
            book.get_data_book(url_book=books)
            all_info.append(book.get_data_book(url_book=books))
            test_all_info = book.get_data_book(url_book=books)

    for dictionnary in all_info:
        img_book = dictionnary["image produit"]

        chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/list_img_url.csv"
        with open(chemin, 'a') as f:
            f.write(img_book)
            f.write('\n')

    # print(test_all_info)
    # print(book.get_data_book(url_book=books)["categorie parente"])

            # test_dict_book_info = {cle: valeur for cle, valeur in zip(all_pages, all_info)}

            # print(book.get_data_book(url_book=books))

    # print(all_info.sort(key=itemgetter("categorie parente")))
    # print(all_info[0]["categorie parente"])
    # print(all_info[0])

    # print(all_info[0]["image produit"])

    """
    def write_data_to_csv(data, filename):
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    all_info.sort(key=itemgetter('categorie parente'))

    grouped_data = {}
    for data_entry in all_info:
        category = data_entry['categorie parente']
        if category not in grouped_data:
            grouped_data[category] = []
        grouped_data[category].append(data_entry)

    for category, data in grouped_data.items():
        filename = f'{category}.csv'
        write_data_to_csv(data, filename)
"""
