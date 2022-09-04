# modules #
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date

from telegram.ext import Updater
from telegram.ext import CommandHandler


def clean_text(text):
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("\r", "")
    text = text.lstrip()
    text = text.rstrip()
    return text


def get_general_notice(url):
    html = urlopen(url)
    bsobject = BeautifulSoup(html, 'html.parser')
    soup = bsobject.find('ul', class_='brd-lstp1')

    results = list()

    for box in soup.find_all('div'):
        try:
            _type = box.find('p', class_='num').get_text()
            if _type == '공지':
                results.append(box.find('div', class_='ti').get_text())
        except AttributeError:
            pass
    results.sort()
    return results


def get_academic_notice(url):
    html = urlopen(url)
    bsobject = BeautifulSoup(html, 'html.parser')
    soup = bsobject.find('ul', class_='brd-lstp1')

    results = list()

    for box in soup.find_all('div'):
        try:
            _type = box.find('p', class_='num').get_text()
            if _type == '공지':
                results.append(box.find('div', class_='ti').get_text())
        except AttributeError:
            pass
    results.sort()
    return results


def get_scholarship_notice(url):
    html = urlopen(url)
    bsobject = BeautifulSoup(html, 'html.parser')
    soup = bsobject.find('tbody')
    main = soup.find_all('td', class_='left_L fontBold')
    results = list()
    for notice in main:
        results.append(clean_text(notice.get_text()))
    results.sort()
    return results


# 일반공
general_notice = "https://www.uos.ac.kr/korNotice/list.do?list_id=FA1"
notice_1 = get_general_notice(general_notice)

# 학사공지
academic_notice = "https://www.uos.ac.kr/korNotice/list.do?list_id=FA2"
notice_2 = get_academic_notice(academic_notice)

# 장학공지
schoolarship_notice = "https://scholarship.uos.ac.kr/scholarship/notice/notice/list.do?brdBbsseq=1"
notice_3 = get_scholarship_notice(schoolarship_notice)

notice_1.insert(0, ",---일반 공지사항---")
notice_2.insert(0, ",---학사 공지사항---")
notice_3.insert(0, ",---장학 공지사항---")

notice = notice_1 + notice_2 + notice_3
notice.insert(0, "🔥{}의 공지!🔥".format(date.today()))
notice = str(notice).replace(',', '\n').replace("'", "")

def bring_notice():
    return notice