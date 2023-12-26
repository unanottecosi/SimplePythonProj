'''
Created on Dec 25, 2023

@author: danieldu
'''
# Max Base
# https://github.com/BaseMax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.google.com/')
sleep(1)
search = browser.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys('BaseMax' + Keys.RETURN)
sleep(1)
print(browser.title)
sleep(2)
browser.quit()