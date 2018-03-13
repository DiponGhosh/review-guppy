import requests
from bs4 import BeautifulSoup

def Productname(url):
	productName = getProductName(url)
	return productName

def getProductName(url):
	productName = ""
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")

	prod_title = soup.find("span", {"id": "productTitle"})
	'''
	for item in prod_title:
		productName = item.text
	'''
	productName = prod_title.text

	return productName


#url = "https://www.amazon.in/Bose-Companion-III-Multimedia-Speakers/dp/B011KSVFV8/ref=sr_1_10?s=electronics&ie=UTF8&qid=1520917726&sr=1-10&keywords=bose"
#print(Productname(url))