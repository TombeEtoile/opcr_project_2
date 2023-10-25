import requests
from bs4 import BeautifulSoup

def scraper_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    class_name = soup.find("li", class_="next").find("a")["href"]
    last_word = class_name[-1]

    return last_word

def get_next_page_link(soup):
    next_link = soup.find("li", class_="next").find("a")["href"]
    return next_link

def process_page_data(last_word):
    print(f"La dernière classe est : {last_word}")
    # Autres opérations de traitement si nécessaire

url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/"

while url:
    last_word = scraper_page(url)
    process_page_data(last_word)
    response = requests.get(url)  # On récupère la nouvelle page
    soup = BeautifulSoup(response.content, 'html.parser')  # On met à jour BeautifulSoup
    url = get_next_page_link(soup)  # On récupère le lien de la page suivante

print("Fin de la catégorie.")

