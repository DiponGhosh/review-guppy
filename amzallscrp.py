import re
import pandas
import requests
from bs4 import BeautifulSoup


'''
for item in list_rev:
	print(item + "\n\n") '''

def Amzallscrp(url):
	product_link = url

	pattern = r"B[A-Z0-9]{9}"
	asin = ""

	#match = re.search(pattern, product_link)
	if(re.search(pattern, product_link)):
		match = re.search(pattern, product_link)
	else:
		return None
	
	for i in range(match.start(), match.end()):
		asin = asin + product_link[i]

	link = "https://www.amazon.in/product-reviews/" + asin + "/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber="

	cnt = 1



	list_rev_text = []
	list_rev_title = []
	list_rev = []



	while (1):
		r = requests.get(link + str(cnt))
		soup = BeautifulSoup(r.content, "lxml")
		rev_data = soup.find_all("span", {"class": "review-text"})
		rev_title = soup.find_all("a", {"class": "review-title"})

		if not rev_data:
			break

		for item in rev_data:
			list_rev_text.append(item.text)
		for item in rev_title:
			list_rev_title.append(item.text)
		cnt = cnt + 1



	for i in range(0, len(list_rev_text)):
		list_rev.append(list_rev_title[i] + " " + list_rev_text[i])

	return list_rev

