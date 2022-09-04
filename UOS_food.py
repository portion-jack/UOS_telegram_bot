from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date


def clean_text(text):
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("\r", "")
    text = text.lstrip()
    text = text.rstrip()
    return text


"""
html = urlopen(url)
bsobject = BeautifulSoup(html, 'html.parser')
soup = bsobject.find('ul', class_='brd-lstp1')
"""
