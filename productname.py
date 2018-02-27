import requests
from bs4 import BeautifulSoup

def Productname(url):
	productName = ""
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")

	prod_title = soup.find_all("span", {"id": "productTitle"})

	for item in prod_title:
		productName = item.text

	return productName