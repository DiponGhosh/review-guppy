import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
}

def ImgLink(url):

    for i in range(0, 3):
        r = requests.get(url, headers=HEADERS)
        if r.status_code == 200:
            break

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.content, "lxml")

    imgHtml = soup.find("span", {"class": "a-button-thumbnail"})

    imgLink = imgHtml.contents[0].contents[1].contents[1]['src']
    startIndex = imgLink.find('_')
    endIndex = imgLink.rfind('.')
    imgSubStr = imgLink[startIndex:endIndex]
    imgLink = imgLink.replace(imgSubStr, '_SS500_', 1)

    return imgLink