import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/category/books/nonfiction_13/"
r = requests.get(base_url)
soup = BeautifulSoup(r.content, "html.parser")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

next_url = []
test_url = []

next_button = soup.find('li', class_='next')

while next_button is not None:
    next_page_relative_url = next_button.find('a', href=True)['href']

    page = requests.get(base_url + next_page_relative_url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    next_button = soup.find('li', class_='next')
    for href in next_button:
        link_page = href.attrs["href"]
        next_url.append(base_url + link_page)

    if next_url == TypeError:
        break

    print(next_url)

# créer fonction + return pour avoir le résultat en une liste



"""
def scraping_page():

    next_url = []

    next_button = soup.find("li", {"class": "next"})
    for href in next_button:
        link_page = href.attrs["href"]
        next_url.append(url_cat + link_page)

    return next_url


print(scraping_page())
"""
