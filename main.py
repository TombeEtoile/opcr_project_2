import requests
from bs4 import BeautifulSoup

page_url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
full_page = requests.get("http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")
soup = BeautifulSoup(full_page.content, 'html.parser')

page_html = full_page.text

page_title = soup.title.text

page_h1 = soup.h1.text

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

liste_valeur_produit = soup.find_all("th")
liste_info_produit = soup.find_all("td")
'''
dic_info_pdt = {"Valeur": liste_valeur_produit, "Information": liste_info_produit}
for valeur in dic_info_pdt.values():
    print(valeur)
'''

print(
    "Titre de la page :", page_title, "\n",
    "Url de l'image produit :", product_img_src, "\n",
    "La catégorie est", link_match[0], " et la sous-catégorie est ", link_match[1], "\n",
    "Nombre d'étoiles :", class_rating_tbl[1], "\n",
    "Le nombre d'article(s) restant (", liste_valeur_produit[5].get_text(), ") est de :", liste_info_produit[5].get_text(), "\n",
    "Le prix incluant les taxes (", liste_valeur_produit[2].get_text(), ") est de :", liste_info_produit[2].get_text(),
    "et celui excluant les taxes (", liste_valeur_produit[3].get_text(), ") est de :", liste_info_produit[3].get_text(), "\n",
    "L'", liste_valeur_produit[0].get_text(), "du produit est :", liste_info_produit[0].get_text())
