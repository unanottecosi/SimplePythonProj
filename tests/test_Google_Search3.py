'''
Created on Dec 25, 2023

@author: danieldu
'''
# Max Base
# https://github.com/BaseMax

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

from Base import InitiateDriver


driver = InitiateDriver.startBrowser()

driver.get('https://www.google.com/')
sleep(1)
search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys('BaseMax' + Keys.RETURN)
sleep(1)
print(driver.title)
sleep(2)
driver.quit()
