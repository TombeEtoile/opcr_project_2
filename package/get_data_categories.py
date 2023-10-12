import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
url_code = requests.get(url)
soup = BeautifulSoup(url_code.content, 'html.parser')

categories_soup = soup.find_all("ul", {"class": "nav nav-list"})
categories_list = []
for link in soup.find_all("a"):
    categories_list.append(link.get("href"))
    if

print(categories_list)
