from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import PyQt5
import time
"""[Initial Settings]
初期設定
"""
options = webdriver.ChromeOptions()
options.add_argument('--headeless')
options.add_argument('--disable-gpu')
options.add_argument('--lang-ja')
browser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

"""[CSS Selector Settings]
CSSセレクターの設定
"""
PAGER = "li.pager-next a"
word = input("検索したいキーワードを入力してください：")
df_main = pd.DataFrame(columns=['在庫有無','タイトル','値段','URL'])
df_graf = pd.DataFrame(columns=['SOLD','PRICE'])
n = 1
res = browser.get("https://www.mercari.com/jp/search/?page="+str(n)+"&keyword="+word)

print(res)
browser.get(res)
while True:
    if PAGER:
        item_boxlist = browser.find_elements_by_css_selector(".items-box")
        for item_box in item_boxlist:
            try:
                if len(item_box.find_elements_by_css_selector(".item-sold-out-badge")) > 0:
                    sold = "SOLD"
                else:
                    sold = "NOT SOLD"
                sub_title = item_box.find_element_by_class_name("items-box-body")
                title = sub_title.find_element_by_tag_name("h3").text
                item_price = item_box.find_element_by_css_selector(".items-box-price")
                price_text = item_price.text
                price_text = re.sub(r",", "", price_text).lstrip("¥ ")
                price_text_int = int(price_text)
                print(price_text_int)
                url = item_box.find_element_by_tag_name("a").get_attribute("href")
                data  = pd.Series( [ sold,title,price_text_int,url ], index=df_main.columns )
                grdata = pd.Series( [ sold,price_text_int ], index=df_graf.columns )
                df_main = df_main.append( data, ignore_index=True )
                df_graf = df_graf.append( grdata, ignore_index=True )
            except Exception as e:
                print(e)
        btn = browser.find_element_by_css_selector(PAGER).get_attribute('href')
        n += 1
        print('next url:{}'.format(btn))
        time.sleep(3)
        browser.get(btn)
        print('Moving to next page...')
    else:
        print('No items anymore...')
        break
print(df_main)
sns.stripplot(x='SOLD', y='PRICE', data=df_graf)
plt.show()
sns.pairplot(df_graf,hue="SOLD")
plt.show()
print('Writing out to CSV file...')
df_main.to_csv("pricedata.csv", encoding="utf_8_sig")
print("Done")