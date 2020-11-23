from selenium import webdriver
import pandas as pd
import time

"""[Initial setting]
初期設定
"""
options = webdriver.ChromeOptions()
options.add_argument('--headeless')
options.add_argument('--disable-gpu')