import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='thumbnail')
for result in results:
    name = result.find('a', class_='title')
    description = result.find('p', class_='description')
    price = result.find('h4', class_='price')
    print(
        f"Product: {name.text} Description: {description.text} Price: {price.text}")
