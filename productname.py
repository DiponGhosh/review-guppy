#productname.py

import requests
from bs4 import BeautifulSoup

#defining header
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
}

def Productname(url):
	productName = getProductName(url)
	return productName

def getProductName(url):
	productName = ""

	#sending request to get the HTML of the page
	for i in range(0, 3):
		r = requests.get(url, headers=HEADERS)
		if r.status_code == 200:
			break
	if r.status_code != 200:
		return None

	soup = BeautifulSoup(r.content, "lxml")

	#finding product title
	prod_title = soup.find("span", {"id": "productTitle"})
	'''
	for item in prod_title:
		productName = item.text
	'''
	productName = prod_title.text

	return productName


#url = "https://www.amazon.in/Bose-Companion-III-Multimedia-Speakers/dp/B011KSVFV8/ref=sr_1_10?s=electronics&ie=UTF8&qid=1520917726&sr=1-10&keywords=bose"
#print(Productname(url))