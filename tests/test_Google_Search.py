'''
Created on Dec 25, 2023

@author: danieldu
'''
# Max Base
# https://github.com/BaseMax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from time import sleep
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless"
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.google.com/')
sleep(1)
search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys('BaseMax' + Keys.RETURN)
sleep(1)
print(driver.title)
sleep(2)
driver.quit()
