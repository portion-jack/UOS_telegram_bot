from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


def get_wether():
    option = Options()
    option.add_argument('headless')
    option.add_argument('--window-size=1000,625')
    browser = webdriver.Chrome(executable_path='/Users/jack/utils/chromedriver', options=option)

    path = r'/Users/jack/utils/chromedriver'
    browser.get('https://weather.naver.com/today/09230104')
    time.sleep(1)
    screenshow = browser.save_screenshot('weather.png')
    browser.quit()
