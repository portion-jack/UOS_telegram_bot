from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date


def clean_text(text):
    text = text.replace("\n", "")
    text = text.replace("\\n", "")
    text = text.replace("\t", "")
    text = text.replace("\r", "")
    text = text.lstrip()
    text = text.rstrip()
    return text


def get_food(url="https://www.uos.ac.kr/food/placeList.do?epTicket=LOG"):
    html = urlopen(url)
    bsobject = BeautifulSoup(html, 'html.parser')
    soup = bsobject.find_all('tr')
    result = list()

    sentence = soup[2].find_all('td', class_='al')[1].get_text()
    result.append(str(sentence.replace(",", "").split("코너")[1:]).replace(",", "\n").replace("'", "")[1:-3])
    result.insert(0, '~점심~')
    sentence = soup[2].find_all('td', class_='al')[2].get_text()
    result.append(str(sentence.replace(",", "").split("코너")[1:]).replace(",", "\n").replace("'", "")[1:-3])
    result.insert(-1, '~저녁~')
    return result


def uos_food():
    ans = get_food()
    ans = clean_text(str(ans)).replace(',','\n')
    return ans
