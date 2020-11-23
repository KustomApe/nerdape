from selenium import webdriver
import pandas as pd
import time

"""[Initial Setting]
初期設定
"""
options = webdriver.ChromeOptions()
options.add_argument('--headeless')
options.add_argument('--disable-gpu')
options.add_argument('--lang-ja')
browser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
df = pd.DataFrame(columns=['name', 'image', 'price', 'category', 'car'])
url = 'https://motorz-garage.com/parts/'

"""[CSS Selector Setting]
CSSセレクターの設定
"""
PAGER_NEXT = "li.select-page.arrow a[rel='next']"
POSTS = ".product-item-list__item"
PRODUCT_NAME = ".product-item-list__item-name"
IMAGE = ".product-item-list__item-image img"
PRICE = ".product-item-list__item-price"
CATEGORY = ".product-item-list__item-category"
CAR = ".product-item-list__item-car-name"

"""[Activate Section]
実行部分
"""
browser.get(url)

while True: #Continue until getting the last page.
    if len(browser.find_elements_by_css_selector(PAGER_NEXT)) > 0:
        print('Starting to get posts...')
        posts = browser.find_element_by_css_selector(POSTS)
        print(len(posts))
        for post in posts: