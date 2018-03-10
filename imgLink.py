import requests
from bs4 import BeautifulSoup

def ImgLink(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    imgHtml = soup.find("span", {"class": "a-button-thumbnail"})

    imgLink = imgHtml.contents[0].contents[1].contents[1]['src']
    startIndex = imgLink.find('_')
    endIndex = imgLink.rfind('.')
    imgSubStr = imgLink[startIndex:endIndex]
    imgLink = imgLink.replace(imgSubStr, '_SS500_', 1)

    return imgLink