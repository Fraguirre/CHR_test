# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 03:13:36 2023

@author: BEAST OF DARKNESS
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(driver_path,options = options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

driver.get('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php')

Header = driver.find_element("xpath", '//*[@id="main"]/div[3]/div[4]/div/table/tbody/tr/td').text

print(Header)