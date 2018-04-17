#amzallscrp.py
import re
import pandas
import requests
from bs4 import BeautifulSoup
from threading import Thread


HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
}


'''
for item in list_rev:
	print(item + "\n\n") '''
list_rev_final= []
threads = []

def Amzallscrp(url):
	product_link = url
	#number_of_review = GetReviewNumber(url)

	global list_rev_final
	global threads
	list_rev_final = []
	threads = []

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
	links = []
	for i in range(1, 11):
		links.append(link + str(i))


	in_parallel(scrape, links)

	if not list_rev_final:
		return None
		
	return list_rev_final


def scrape(url):
    list_rev_text = []
    list_rev_title = []
    list_rev = []

    for i in range(0, 3):
        r = requests.get(url, headers=HEADERS)
        if r.status_code == 200:
            break

    if r.status_code != 200:
        return False	

    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.content, "lxml")
    rev_data = soup.find_all("span", {"class": "review-text"})
    rev_title = soup.find_all("a", {"class": "review-title"})

    for item in rev_data:
        if item.text:
	        list_rev_text.append(item.text)
    for item in rev_title:
        if item.text:
	        list_rev_title.append(item.text)

    for i in range(0, len(list_rev_text)):
	    list_rev.append(list_rev_title[i] + " " + list_rev_text[i])
    #print(len(list_rev))
    global list_rev_final
    list_rev_final = list_rev_final + list_rev

    return True


def in_parallel(fn, l):
    for i in l:
        process = Thread(target=fn, args=[i])
        process.start()
        threads.append(process)
    
    for process in threads:
        process.join()

#in_parallel(scrape, links)


def GetReviewNumber(url):
	revNumber = ""
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")

	custRevNum = soup.find_all("span", {"id": "acrCustomerReviewText"})

	#revNumber = custRevNum[0].text
	for item in custRevNum:
		revNumber = item.text

	revNum = int(''.join(re.findall(r"\d+", revNumber)))

	print("printing value of revNum: " + str(revNum))


	return revNum