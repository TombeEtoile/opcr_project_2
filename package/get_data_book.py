import requests
from bs4 import BeautifulSoup
import csv


def get_data_book(url_book):

    r = requests.get(url_book)
    soup = BeautifulSoup(r.content, 'html.parser')

    product_information = []
    breadcrumb = []
    breadcrumb_list = []
    all_p = []
    review = []
    list_2 = []

    url = r.url
    title = soup.title.text.strip().replace(",", " ")
    url_split_1 = url.replace("https://books.toscrape.com/catalogue/", "")
    url_split_2 = url_split_1.replace("/index.html", "")
    name = url_split_2.replace("-", " ").replace(",", " ")
    img = soup.find("img", src_="")
    img_url = img["src"]
    valid_img_url = img_url.replace("../..", "https://books.toscrape.com/")
    product_information = soup.find_all("td")
    try:
        upc = product_information[0].text
    except IndexError:
        upc = ""
    try:
        ht = product_information[2].text
    except IndexError:
        ht = ""
    try:
        ttc = product_information[3].text
    except IndexError:
        ttc = ""
    breadcrumb = soup.find("ul", class_="breadcrumb")
    breadcrumb_list = breadcrumb.find_all("a", href_="")
    cat_url_position = breadcrumb.find_all("a", href_="")[2]
    cat_url = cat_url_position.attrs['href'].replace("../", "https://books.toscrape.com/catalogue/")
    try:
        categorie = breadcrumb_list[2].text
    except IndexError:
        categorie = ""
    all_p = soup.find_all("p")
    try:
        availability = product_information[5].text
    except IndexError:
        availability = ""
    try:
        description = all_p[3].text.replace(",", " ")
    except IndexError:
        description = ""
    class_name = soup.find("p", class_="star-rating")
    class_rating = class_name["class"]
    try:
        product_rating = class_rating[1].replace("One", "1/5").replace("Two", "2/5").replace("Three", "3/5").replace("Four", "4/5").replace("Five", "5/5")
    except IndexError:
        product_rating = ""

    all_information = {
        "url catégorie": cat_url,
        "nom": name,
        "url": url,
        "title": title,
        "image produit": valid_img_url,
        "UPC": upc,
        "prix HT": ht,
        "prix TTC": ttc,
        "categorie parente": categorie,
        "nombre en stock": availability,
        "avis (sur 5)": product_rating,
        "description": description
    }

    return all_information
    # return url, title, valid_img_url, upc, ht, ttc, categorie, availability, product_rating, description

# print(get_data_book(url_book="https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"))
# print(get_data_book(url_book="https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html")["image produit"])

"""
chemin = r"/Users/augustinverdier/PycharmProjects/projet_2/info_book_5.csv"
with open(chemin, "a") as c:
    writer = csv.writer(c)
    for k, v in get_data_book(url_book="https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html").items():
        writer.writerow([k, v])
"""
