# Author: Cassio Dalla Barba Everling
# Date:
# Description:

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

import time 

from typing import List

from random import choice as ranchoice


def get_notion_content(url: str) -> List[str]:
    lines: List[str] = []
    page_content = None
    driver: webdriver.Chrome = open_invisible_browser(url)

    time.sleep(1)

    page_content = driver.find_element(By.CLASS_NAME, 'notion-page-content')
    
    lines = [element.text for element in page_content.find_elements(By.TAG_NAME, 'div')[3:-2:5]]

    driver.quit()

    return lines


def open_invisible_browser(url: str = '') -> webdriver.Chrome:
    driver: webdriver.Chrome = None

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    if url != '':
        driver.get(URL)

    return driver


def notion_content_random_picker(url:str) -> str:
    return ranchoice(get_notion_content(url))


if __name__ == '__main__':
    print()
    print()
    print()
    URL = r'''https://www.notion.so/Project-ideas-0fab9561179e4874a4edc46e51a38647?pvs=4'''
    print(notion_content_random_picker(URL).upper())
    print()
    print()
    print()