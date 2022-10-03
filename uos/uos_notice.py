from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date


def clean_text(text):
    text = text.replace("\n", "").replace("\t", "").replace("\r", "")
    text = text.replace("\\n", "").replace("\\t", "").replace("\\r", "")
    text = text.lstrip().rstrip()
    return text


def format_notice(notice):
    notice.insert(0, "🔥{}의 공지!🔥".format(date.today()))
    notice = str(notice).replace(',', '\n').replace("'", "")
    return notice


def get_html(url):
    html = urlopen(url)
    bsobject = BeautifulSoup(html, 'html.parser')
    return bsobject


def get_general_notice(url="https://www.uos.ac.kr/korNotice/list.do?list_id=FA1"):
    bsobject = get_html(url)
    soup = bsobject.find('ul', class_='brd-lstp1')

    results = list()

    for box in soup.find_all('div'):
        try:
            _type = box.find('p', class_='num').get_text()
            if _type == '공지':
                results.append(box.find('div', class_='ti').get_text().replace(',', ''))
        except AttributeError:
            pass
    results.sort()
    results.insert(0, "---일반 공지사항---")
    return format_notice(results)


def get_academic_notice(url="https://www.uos.ac.kr/korNotice/list.do?list_id=FA2"):
    bsobject = get_html(url)
    soup = bsobject.find('ul', class_='brd-lstp1')

    results = list()

    for box in soup.find_all('div'):
        try:
            _type = box.find('p', class_='num').get_text()
            if _type == '공지':
                results.append(box.find('div', class_='ti').get_text().replace(',', ''))
        except AttributeError:
            pass
    results.sort()
    results.insert(0, "---학사 공지사항---")
    return format_notice(results)


def get_scholarship_notice(url="https://scholarship.uos.ac.kr/scholarship/notice/notice/list.do?brdBbsseq=1"):
    bsobject = get_html(url)
    soup = bsobject.find('tbody')
    main = soup.find_all('td', class_='left_L fontBold')
    results = list()
    for box in main:
        results.append(clean_text(box.get_text()))
    results.sort()
    results.insert(0, "---장학 공지사항---")
    return format_notice(results)
