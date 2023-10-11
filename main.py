import requests
from bs4 import BeautifulSoup
import csv

page_url = input("Quelle URL voulez-vous scraper ?")
full_page = requests.get(page_url)
soup = BeautifulSoup(full_page.content, 'html.parser')

page_html = full_page.text

url = ["http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"]

page_title = soup.title.text
title = [page_title]

page_h1 = soup.h1.text
h1 = [page_h1]

product_img = soup.find_all("img", alt=page_h1)
product_img_src = []
for element in product_img:
    product_img_src.append(element["src"])

page_link = soup.find_all("a")
page_link_list = []
category_link_list = []
for link in soup.find_all("a"):
    page_link_list.append(link.get("href"))
link_match = [s for s in page_link_list if "category" in s]

class_rating = "star-rating Two"
class_rating_tbl = class_rating.split()

product_description = soup.text
description = [product_description]

liste_valeur_produit = soup.find_all("th")
liste_info_produit = soup.find_all("td")


#Test export en CSV
"""
en_tete = ["product_page_url", "universal_product_code_(upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
with open("scraping_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for url, liste_info_produit[0], title, liste_info_produit[2], liste_info_produit[3], liste_info_produit[5], "pas encore réalisé", link_match[1+2], class_rating_tbl[1], product_img_src in zip
"""

#Table des matière
"""
url[--> url de la page produit]
title[--> titre]
h1[--> h1]
link_match[1 --> catégorie, 2 --> sous-catégorie]
product_img_src[--> URL image]
class_rating_tbl[1 --> Nombre d'étoiles produit]
description[--> description du produit]  !!! pas finalisé !!!
liste_info_produit[2 --> valeur TTC]
liste_info_produit[3 --> valeur HT]
liste_info_produit[0 --> UPC]
liste_info_produit[5 --> nombre de produits en stocks]
"""


#Appeler les données
print(
    "Titre de la page :", page_title, "\n",
    "Url de l'image produit :", product_img_src, "\n",
    "La catégorie est", link_match[0], " et la sous-catégorie est ", link_match[1], "\n",
    "Nombre d'étoiles :", class_rating_tbl[1], "\n",
    "Le nombre d'article(s) restant (", liste_valeur_produit[5].get_text(), ") est de :", liste_info_produit[5].get_text(), "\n",
    "Le prix incluant les taxes (", liste_valeur_produit[2].get_text(), ") est de :", liste_info_produit[2].get_text(),
    "et celui excluant les taxes (", liste_valeur_produit[3].get_text(), ") est de :", liste_info_produit[3].get_text(), "\n",
    "L'", liste_valeur_produit[0].get_text(), "du produit est :", liste_info_produit[0].get_text())