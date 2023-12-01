import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(r.content, "html.parser")


def categories_url(url_home):

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


def dictionary_cat(url_home):

    cat_list = []

    nav_bar = soup.find("div", class_="side_categories")
    all_cat = nav_bar.find_all("a")
    for cat_name in all_cat:
        all_cat_name = cat_name.text.strip()
        cat_list.append(all_cat_name)

    del (cat_list[0])

    dict_cat = {cle: valeur for cle, valeur in zip(cat_list, categories_url(url_home))}

    return dict_cat


def cat_list(url_home):

    cat_name_list = []

    nav_bar = soup.find("div", class_="side_categories")
    all_cat = nav_bar.find_all("a")
    for cat_name in all_cat:
        all_cat_name = cat_name.text.strip()
        cat_name_list.append(all_cat_name)

    del (cat_name_list[0])

    return cat_name_list


# print(categories_url(url_home="https://books.toscrape.com"))
# print(dictionary_cat(url_home="https://books.toscrape.com"))
# print(cat_list(url_home="https://books.toscrape.com"))
