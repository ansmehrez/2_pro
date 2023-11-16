import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

response = requests.get(url)

# التحقق من نجاح الطلب
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all("article")

    for book in books:
        title = book.h3.a["title"]
        
        # التحقق من وجود التقييم قبل الوصول إليه
        rating = book.p["class"][1] if "class" in book.p.attrs else "N/A"
        
        price = book.select('.price_color')[0].get_text()

        # استخدام f-string لتحسين عرض النص
        print(f"Book titled: {title} has a rating of: {rating} stars. Price: {price}$")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
