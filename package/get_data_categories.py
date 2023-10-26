import requests
from bs4 import BeautifulSoup

url_home = "https://books.toscrape.com"


def get_data_categories_fct(url):

    r = requests.get(url_home)
    soup = BeautifulSoup(r.content, "html.parser")

    categories = []
    all_invalid_url = []
    all_valid_url = []

    navbar = soup.find("div", class_="side_categories")
    urls = navbar.find_all("a")

    for link in urls:
        href = link.attrs['href']
        categories.append(href)

    for change in categories:
        invalid_url = change.replace("catalogue", "https://books.toscrape.com/catalogue")
        all_invalid_url.append(invalid_url)

    for modification in all_invalid_url:
        valid_url = modification.replace("/index.html", "/")
        all_valid_url.append(valid_url)

    del(all_valid_url[0])

    return all_valid_url
