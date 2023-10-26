from package import get_data_categories as cat, get_data_book_by_categories as page, get_data_book as book


if __name__ == "__main__":

    all_cat = cat.get_data_categories_fct(url="https://books.toscrape.com/")
    for url_cat in all_cat:
        all_product = page.get_books_from_categories(url=url_cat)
        for url_product in all_product:
            all_info_books = book.get_data_book(url=url_product)

            print(all_info_books)
