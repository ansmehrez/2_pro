import requests
from bs4 import BeautifulSoup

ur1 = 'https://books.toscrape.com/'

response=requests.get(ur1)

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    rating= book.p["class"][1]
    price = book.select('.price_color')[0].get_text()
    print("Book titled: " + title + " has a rating of: " + rating + " stars " + price+"$")