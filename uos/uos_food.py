from urllib.request import urlopen
from bs4 import BeautifulSoup


def uos_food():
    url = "https://www.uos.ac.kr/food/placeList.do"

    html = urlopen(url)
    bsobject = BeautifulSoup(html, 'html.parser')
    soup = bsobject.find_all('table')

    # 아침
    # morning=soup[0].find_all('td',class_='al')[0].get_text()

    # 점심
    _lunch = soup[0].find_all('td', class_='al')[1].get_text()
    lunch = _lunch.split('코너')

    for i, content in enumerate(lunch):
        lunch[i] = ("코너" + content).replace(',', '')

    lunch = str(lunch[1:])[1:-1].replace(',', '\n')
    # 저녁
    _dinner = soup[0].find_all('td', class_='al')[2].get_text()
    dinner = _dinner.split('코너')

    for i, content in enumerate(dinner):
        dinner[i] = ("코너" + content).replace(',', '')
    dinner = str(dinner[1:])[1:-1].replace(',', '\n')
    return lunch, dinner
