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
