import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
full_page = requests.get(url)
soup = BeautifulSoup(full_page.content, 'html.parser')

page_html = full_page.text

page_title = soup.title.text
title = [page_title]

page_h1 = soup.h1.text
h1 = [page_h1]

product_img = soup.find_all("img", alt=page_h1)
img_src = []
for element in product_img:
    img_src.append(element["src"])

page_link = soup.find_all("a")
page_link_list = []
category_link_list = []
for link in soup.find_all("a"):
    page_link_list.append(link.get("href"))
category = [s for s in page_link_list if "category" in s]

class_rating = "star-rating Two"
rating = class_rating.split()

news_content_section = soup.find('div', id="content_inner")
description_all = []
for tag in soup.findAll('p'):
    description_all.append(tag.get_text())
description = description_all[3]

liste_valeur_produit = soup.find_all("th")
liste_info_produit = soup.find_all("td")
price_ttc = liste_info_produit[2].get_text()
price_ht = liste_info_produit[3].get_text()
upc = liste_info_produit[0].get_text()
availability = liste_info_produit[5].get_text()

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
    "Url de l'image produit :", img_src, "\n",
    "La catégorie est", category[0], " et la sous-catégorie est ", category[1], "\n",
    "Nombre d'étoiles :", rating[1], "\n",
    "Le nombre d'article(s) restant (", liste_valeur_produit[5].get_text(), ") est de :", availability, "\n",
    "Le prix incluant les taxes (", liste_valeur_produit[2].get_text(), ") est de :", price_ttc,
    "et celui excluant les taxes (", liste_valeur_produit[3].get_text(), ") est de :", price_ht, "\n",
    "L'", liste_valeur_produit[0].get_text(), "du produit est :", upc, "\n",
    "La description du produit est :", description)
