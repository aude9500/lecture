import os
import sys
import time as time
import pandas as pd
import numpy as np

import params as pa

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def driversetting(DownloadPath):    #웹 들어가서 세팅하는 것 묻지도 말고 따지지도 말고 따라하자

    options =  webdriver.ChromeOptions()
    options.add_experimental_option("prefs",{"download.default_directory": DownloadPath,
                                             "download.prompt_for_download":False,
                                             "download.directory_upgrade": False,
                                             "safebrowsing_for_trusted_sources_enabled": False,
                                             "safebrowsing,enabled": False})

    # if 1:
    # options.add_argument('headless') 헤드레스가 되면 크롬창 열리지 않고 들어가는 것

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(pa.waitseconds)

    return driver

def gen(): #TargetDay,Farm,Method
    DownloadPath = r"\Users\khs\Downloads\Advanced"
    driver = driversetting(DownloadPath)

    driver.get(pa.HYOSUNG)
    print('run website')
    time.sleep(pa.waitseconds)

    driver.find_element(By.XPATH, '//*[@id="Txt_1"]').send_keys('jarasolar')
    driver.find_element(By.XPATH, '//*[@id="Txt_2"]').send_keys('abcd1234')
    driver.find_element(By.XPATH, '//*[@id="imageField"]').click()
    print('login')
    time.sleep(pa.waitseconds)

    driver.find_element(By.XPATH, '//*[@id="form1"]/div[4]/div[1]/div/ul[2]/a[5]/li').click()
    print('Statistical Report')
    time.sleep(pa.waitseconds)


    return []

if __name__ == '__main__':  #cr.py 실행하면 얘부터 실행 다른 곳에서 함수 불러올 때는 위에서부터 쭈욱 사용
    # Farm = 1
    # TargetDay = '2023-09-10'
    gen()