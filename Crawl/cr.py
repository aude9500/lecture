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


def driversetting(DownloadPath):    #무슨 파일 받는지 모르니깐 청소를 해주는 함수

    options =  webdriver.ChromeOptions()
    options.add_experimental_option("prefs",{"download.default_directory": DownloadPath,
                                             "download.prompt_for_download":False,
                                             "download.directory_upgrade": False,
                                             "safebrowsing_for_trusted_sources_enabled": False,
                                             "safebrowsing,enabled": False})

    # if 1:
    # options.add_argument('headless')

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


    return []

if __name__ == '__main__':
    gen()