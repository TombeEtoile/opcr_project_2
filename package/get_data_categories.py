import requests
from bs4 import BeautifulSoup


def get_data_categories_fct():

    r = requests.get("https://books.toscrape.com/index.html")
    soup = BeautifulSoup(r.content, "html.parser")

    categories = []
    all_valid_url = []

    navbar = soup.find("div", class_="side_categories")
    urls = navbar.find_all("a")

    for link in urls:
        href = link.attrs['href']
        categories.append(href)

    for change in categories:
        valid_url = change.replace("catalogue", "https://books.toscrape.com/catalogue")
        all_valid_url.append(valid_url)
    del(all_valid_url[0])

    return all_valid_url


print(get_data_categories_fct())
